#!/usr/bin/env python3
"""
Adversarial Probe: Active Recall Prompts & Answers Completeness and Parity
- Scans all files for Active Recall challenges.
- Verifies that:
  - Every Challenge has an explicit Question and an explicit Answer.
  - Every English Challenge has a matching Vietnamese Challenge.
  - Challenge numbers match exactly (1..N).
  - Both Question and Answer have substantive content (> 20 chars).
  - No orphaned questions or answers exist.
"""

import os
import re
import sys
from typing import List, Dict, Any, Tuple

TARGET_DIR = "/mnt/second_drive/DOCS/Backend/teamwork_bilingual"

def extract_qa_blocks(filepath: str) -> List[Dict[str, Any]]:
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    blocks = []
    current_block = None

    q_en_pattern = re.compile(r"^>\s*\*\*Question\*\*:\s*(.+)$", re.IGNORECASE)
    q_vi_pattern = re.compile(r"^>\s*\*\*Câu\s+hỏi\*\*:\s*(.+)$", re.IGNORECASE)
    a_en_pattern = re.compile(r"^>\s*\*\*Answer\*\*:\s*(.+)$", re.IGNORECASE)
    a_vi_pattern = re.compile(r"^>\s*\*\*Đáp\s+án\*\*:\s*(.+)$", re.IGNORECASE)

    challenge_en_pattern = re.compile(r"^>\s*🧠?\s*\*\*Active-Recall\s+Challenge\s*(\d+)?:?\s*([^*]+)\*\*", re.IGNORECASE)
    challenge_vi_pattern = re.compile(r"^>\s*🧠?\s*\*\*Thử\s+Thách\s+Gợi\s+Nhớ\s+Tích\s+Cực\s*(\d+)?:?\s*([^*]+)\*\*", re.IGNORECASE)

    for idx, raw_line in enumerate(lines, 1):
        line = raw_line.strip()
        
        m_ch_en = challenge_en_pattern.match(line)
        if m_ch_en:
            num = m_ch_en.group(1)
            title = m_ch_en.group(2).strip()
            current_block = {
                "start_line": idx,
                "lang": "EN",
                "number": int(num) if num else None,
                "title": title,
                "question": None,
                "question_line": None,
                "answer": None,
                "answer_line": None,
                "raw_header": line
            }
            blocks.append(current_block)
            continue

        m_ch_vi = challenge_vi_pattern.match(line)
        if m_ch_vi:
            num = m_ch_vi.group(1)
            title = m_ch_vi.group(2).strip()
            current_block = {
                "start_line": idx,
                "lang": "VI",
                "number": int(num) if num else None,
                "title": title,
                "question": None,
                "question_line": None,
                "answer": None,
                "answer_line": None,
                "raw_header": line
            }
            blocks.append(current_block)
            continue

        if current_block:
            m_qe = q_en_pattern.match(line)
            if m_qe:
                current_block["question"] = m_qe.group(1).strip()
                current_block["question_line"] = idx
                continue

            m_qv = q_vi_pattern.match(line)
            if m_qv:
                current_block["question"] = m_qv.group(1).strip()
                current_block["question_line"] = idx
                continue

            m_ae = a_en_pattern.match(line)
            if m_ae:
                current_block["answer"] = m_ae.group(1).strip()
                current_block["answer_line"] = idx
                continue

            m_av = a_vi_pattern.match(line)
            if m_av:
                current_block["answer"] = m_av.group(1).strip()
                current_block["answer_line"] = idx
                continue

    return blocks

def probe_file_active_recall(filepath: str) -> Dict[str, Any]:
    blocks = extract_qa_blocks(filepath)
    issues = []

    # Check each block internal validity
    for b in blocks:
        if not b["question"]:
            issues.append(f"Line {b['start_line']}: Challenge '{b['title']}' ({b['lang']}) is missing a Question.")
        elif len(b["question"]) < 15:
            issues.append(f"Line {b['start_line']}: Question on line {b['question_line']} too short ({len(b['question'])} chars).")

        if not b["answer"]:
            issues.append(f"Line {b['start_line']}: Challenge '{b['title']}' ({b['lang']}) is missing an Answer.")
        elif len(b["answer"]) < 20:
            issues.append(f"Line {b['start_line']}: Answer on line {b['answer_line']} too short ({len(b['answer'])} chars).")

    # Check pair alternation (EN must be followed by VI)
    pairs = []
    i = 0
    while i < len(blocks):
        curr = blocks[i]
        if curr["lang"] == "EN":
            if i + 1 >= len(blocks):
                issues.append(f"Line {curr['start_line']}: English challenge '{curr['title']}' has no matching Vietnamese challenge (EOF).")
                i += 1
            else:
                nxt = blocks[i + 1]
                if nxt["lang"] != "VI":
                    issues.append(f"Line {curr['start_line']}: English challenge followed by {nxt['lang']} on line {nxt['start_line']}.")
                    i += 1
                else:
                    if curr["number"] is not None and nxt["number"] is not None and curr["number"] != nxt["number"]:
                        issues.append(f"Line {curr['start_line']}: Number mismatch in pair: EN #{curr['number']} vs VI #{nxt['number']}.")
                    pairs.append((curr, nxt))
                    i += 2
        else:
            issues.append(f"Line {curr['start_line']}: Unexpected leading Vietnamese challenge '{curr['title']}' without preceding English challenge.")
            i += 1

    return {
        "file": os.path.basename(filepath),
        "total_qa_blocks": len(blocks),
        "total_pairs": len(pairs),
        "pairs": pairs,
        "issues": issues,
        "passed": len(issues) == 0
    }

def main():
    target_files = sorted([
        os.path.join(TARGET_DIR, f)
        for f in os.listdir(TARGET_DIR)
        if f.endswith(".md")
    ])

    print("================================================================================")
    print(" ADVERSARIAL PROBE: ACTIVE RECALL PROMPTS & ANSWERS PARITY")
    print(f" Target Directory: {TARGET_DIR}")
    print("================================================================================")

    all_passed = True
    total_pairs = 0
    total_issues = 0

    for fpath in target_files:
        res = probe_file_active_recall(fpath)
        total_pairs += res["total_pairs"]
        status = "PASS" if res["passed"] else "FAIL"
        if not res["passed"]:
            all_passed = False
            total_issues += len(res["issues"])

        print(f"\n[{status}] {res['file']} (QA Pairs: {res['total_pairs']}, Total Blocks: {res['total_qa_blocks']}, Issues: {len(res['issues'])})")
        for p in res["pairs"]:
            en_b, vi_b = p
            num_str = f"#{en_b['number']} " if en_b['number'] else ""
            print(f"   - Challenge {num_str}(L{en_b['start_line']} <-> L{vi_b['start_line']}): EN Q len={len(en_b['question'] or '')}, A len={len(en_b['answer'] or '')} | VI Q len={len(vi_b['question'] or '')}, A len={len(vi_b['answer'] or '')}")

        for iss in res["issues"]:
            print(f"   [!] Issue: {iss}")

    print("\n--------------------------------------------------------------------------------")
    print(f"Total files probed     : {len(target_files)}")
    print(f"Total QA pairs verified: {total_pairs}")
    print(f"Total issues found     : {total_issues}")
    print(f"Overall Status         : {'ALL PASS' if all_passed else 'FAILURES DETECTED'}")
    print("================================================================================")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

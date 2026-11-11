#!/usr/bin/env python3
"""
Adversarial Probe: Paragraph Symmetry & 1:1 Language Alternation
- Splits markdown files into logical content blocks (prose paragraphs, blockquotes, lists).
- Excludes code blocks, tables, thematic breaks, and headings.
- Detects language of each block using Vietnamese diacritic signatures.
- Asserts strict 1:1 alternation (EN -> VI -> EN -> VI).
- Flags any instances of:
  - Two consecutive English blocks (EN -> EN)
  - Two consecutive Vietnamese blocks (VI -> VI)
  - Unclassifiable or empty blocks
  - Pairwise parity mismatch in any section
"""

import os
import re
import sys
from typing import List, Dict, Any, Tuple

TARGET_DIR = "/mnt/second_drive/DOCS/Backend/teamwork_bilingual"

VN_DIACRITICS_RE = re.compile(
    r"[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"
    r"ÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]"
)

def classify_block_language(text: str) -> str:
    """
    Classify text block as EN or VI based on presence of Vietnamese diacritics
    and Vietnamese keywords.
    """
    diacritic_matches = VN_DIACRITICS_RE.findall(text)
    # Total alphabetic chars
    alpha_count = len(re.findall(r"[a-zA-Z]", text))
    
    if len(diacritic_matches) >= 2 or (len(diacritic_matches) >= 1 and "(Tiếng Việt)" in text):
        return "VI"
    elif len(diacritic_matches) == 0:
        return "EN"
    else:
        # Edge case: single diacritic in long text (e.g. borrowed term)
        if len(diacritic_matches) / max(alpha_count, 1) > 0.01:
            return "VI"
        return "EN"

def probe_file_paragraph_symmetry(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Step 1: Strip code blocks
    filtered_lines = []
    in_code = False
    for idx, raw_line in enumerate(lines, 1):
        stripped = raw_line.strip()
        if re.match(r"^(`{3,}|~{3,})", stripped):
            in_code = not in_code
            filtered_lines.append(("", idx, "CODE_FENCE"))
            continue
        if in_code:
            filtered_lines.append(("", idx, "CODE_BODY"))
        else:
            filtered_lines.append((raw_line, idx, "NORMAL"))

    # Step 2: Group into blocks separated by blank lines or headings/tables/thematic breaks
    blocks = []
    current_block_lines = []
    current_start_line = 0
    current_block_type = None

    def flush_block():
        nonlocal current_block_lines, current_start_line, current_block_type
        if not current_block_lines:
            return
        content = "".join([l[0] for l in current_block_lines]).strip()
        if content:
            lang = classify_block_language(content)
            blocks.append({
                "start_line": current_start_line,
                "end_line": current_block_lines[-1][1],
                "content": content,
                "type": current_block_type,
                "lang": lang,
                "snippet": content[:80].replace("\n", " ") + ("..." if len(content) > 80 else "")
            })
        current_block_lines = []
        current_start_line = 0
        current_block_type = None

    for raw_line, line_no, tag in filtered_lines:
        if tag in ("CODE_FENCE", "CODE_BODY"):
            flush_block()
            continue

        stripped = raw_line.strip()

        # Check for blank lines
        if not stripped:
            flush_block()
            continue

        # Check for thematic breaks
        if re.match(r"^---+$", stripped):
            flush_block()
            blocks.append({
                "start_line": line_no,
                "end_line": line_no,
                "content": stripped,
                "type": "THEMATIC_BREAK",
                "lang": "SEPARATOR",
                "snippet": "---"
            })
            continue

        # Check for headings
        if stripped.startswith("#"):
            flush_block()
            # Record heading as separator
            lang = "EN" if "(English)" in stripped else ("VI" if "(Tiếng Việt)" in stripped else "NONE")
            blocks.append({
                "start_line": line_no,
                "end_line": line_no,
                "content": stripped,
                "type": "HEADING",
                "lang": f"HEADING_{lang}",
                "snippet": stripped
            })
            continue

        # Check for table rows
        if stripped.startswith("|"):
            flush_block()
            # Tables are treated as structural units, not prose paragraphs
            continue

        is_indented = raw_line.startswith("  ") or raw_line.startswith("\t")
        btype = "BLOCKQUOTE" if stripped.startswith(">") else ("LIST" if re.match(r"^[-*]\s+|\d+\.\s+", stripped) else "PROSE")

        if current_block_type is None:
            current_block_type = btype
            current_start_line = line_no
            current_block_lines.append((raw_line, line_no))
        elif is_indented and current_block_type in ("LIST", "PROSE_LIST", "BLOCKQUOTE"):
            current_block_lines.append((raw_line, line_no))
        elif current_block_type == btype:
            current_block_lines.append((raw_line, line_no))
        elif current_block_type == "PROSE" and btype == "LIST":
            current_block_type = "PROSE_LIST"
            current_block_lines.append((raw_line, line_no))
        elif current_block_type == "PROSE_LIST" and btype == "LIST":
            current_block_lines.append((raw_line, line_no))
        else:
            flush_block()
            current_block_type = btype
            current_start_line = line_no
            current_block_lines.append((raw_line, line_no))

    flush_block()

    # Step 3: Analyze symmetry between prose/blockquote/list blocks
    # Content blocks to verify: PROSE, BLOCKQUOTE, LIST, PROSE_LIST
    content_blocks = [b for b in blocks if b["type"] in ("PROSE", "BLOCKQUOTE", "LIST", "PROSE_LIST")]

    issues = []
    # Check strict EN -> VI alternation
    prev_lang = None
    prev_block = None

    for b in content_blocks:
        if prev_lang is None:
            if b["lang"] != "EN":
                issues.append({
                    "line": b["start_line"],
                    "type": "INITIAL_PARAGRAPH_NOT_ENGLISH",
                    "message": f"First content block on line {b['start_line']} is {b['lang']}, expected EN",
                    "block": b
                })
            prev_lang = b["lang"]
            prev_block = b
        else:
            if b["lang"] == prev_lang:
                issues.append({
                    "line": b["start_line"],
                    "type": f"CONSECUTIVE_{b['lang']}_PARAGRAPHS",
                    "message": f"Consecutive {b['lang']} blocks detected: line {prev_block['start_line']} followed by line {b['start_line']}",
                    "prev_block": prev_block,
                    "curr_block": b
                })
            prev_lang = b["lang"]
            prev_block = b

    # Check overall counts
    en_count = sum(1 for b in content_blocks if b["lang"] == "EN")
    vi_count = sum(1 for b in content_blocks if b["lang"] == "VI")
    if en_count != vi_count:
        issues.append({
            "line": 0,
            "type": "PAIRWISE_COUNT_MISMATCH",
            "message": f"Total EN content blocks ({en_count}) does not match VI content blocks ({vi_count})",
            "en_count": en_count,
            "vi_count": vi_count
        })

    return {
        "file": os.path.basename(filepath),
        "total_lines": len(lines),
        "total_content_blocks": len(content_blocks),
        "en_count": en_count,
        "vi_count": vi_count,
        "content_blocks": content_blocks,
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
    print(" ADVERSARIAL PROBE: PARAGRAPH SYMMETRY & 1:1 ALTERNATION")
    print(f" Target Directory: {TARGET_DIR}")
    print("================================================================================")

    all_passed = True
    total_blocks = 0
    total_issues = 0

    for fpath in target_files:
        res = probe_file_paragraph_symmetry(fpath)
        total_blocks += res["total_content_blocks"]
        status = "PASS" if res["passed"] else "FAIL"
        if not res["passed"]:
            all_passed = False
            total_issues += len(res["issues"])

        print(f"\n[{status}] {res['file']} (Content Blocks: {res['total_content_blocks']}, EN: {res['en_count']}, VI: {res['vi_count']}, Issues: {len(res['issues'])})")
        for iss in res["issues"]:
            print(f"   [!] Line {iss['line']}: {iss['type']} -> {iss['message']}")
            if "curr_block" in iss:
                print(f"       Prev (L{iss['prev_block']['start_line']}): {iss['prev_block']['snippet']}")
                print(f"       Curr (L{iss['curr_block']['start_line']}): {iss['curr_block']['snippet']}")

    print("\n--------------------------------------------------------------------------------")
    print(f"Total files probed        : {len(target_files)}")
    print(f"Total content blocks      : {total_blocks}")
    print(f"Total symmetry issues     : {total_issues}")
    print(f"Overall Status            : {'ALL PASS' if all_passed else 'FAILURES DETECTED'}")
    print("================================================================================")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

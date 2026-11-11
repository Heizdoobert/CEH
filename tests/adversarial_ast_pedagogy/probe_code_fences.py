#!/usr/bin/env python3
"""
Adversarial Probe: Code Block Integrity
- Checks that all code fences (``` or ~~~) are properly closed.
- Checks that 100% of opening code fences have non-empty language identifiers.
- Checks for malformed fences or unbalanced blocks.
"""

import os
import re
import sys
from typing import List, Dict, Any

TARGET_DIR = "/mnt/second_drive/DOCS/Backend/teamwork_bilingual"

def probe_file_code_blocks(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    issues = []
    blocks = []
    in_code = False
    fence_char = ""
    fence_len = 0
    open_line = 0
    open_lang = ""

    fence_pattern = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")

    for idx, line in enumerate(lines, 1):
        m = fence_pattern.match(line)
        if m:
            indent, fence, rest = m.groups()
            rest = rest.strip()
            
            if not in_code:
                # Opening fence
                in_code = True
                fence_char = fence[0]
                fence_len = len(fence)
                open_line = idx
                open_lang = rest
                if not rest:
                    issues.append({
                        "line": idx,
                        "type": "MISSING_LANGUAGE_IDENTIFIER",
                        "content": line.rstrip(),
                        "message": f"Opening fence on line {idx} has empty language identifier."
                    })
            else:
                # Potential closing fence
                if fence[0] == fence_char and len(fence) >= fence_len:
                    # Successfully closed
                    blocks.append({
                        "start_line": open_line,
                        "end_line": idx,
                        "lang": open_lang,
                        "line_count": idx - open_line - 1
                    })
                    in_code = False
                    fence_char = ""
                    fence_len = 0
                    open_line = 0
                    open_lang = ""

    if in_code:
        issues.append({
            "line": open_line,
            "type": "UNCLOSED_CODE_BLOCK",
            "content": f"Opened at line {open_line} with fence {fence_char * fence_len} and lang '{open_lang}'",
            "message": f"Unclosed code block starting at line {open_line} reaches EOF."
        })

    return {
        "file": os.path.basename(filepath),
        "total_lines": len(lines),
        "total_code_blocks": len(blocks),
        "blocks": blocks,
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
    print(" ADVERSARIAL PROBE: CODE BLOCK INTEGRITY & LANGUAGE IDENTIFIERS")
    print(f" Target Directory: {TARGET_DIR}")
    print("================================================================================")

    all_passed = True
    total_blocks = 0
    total_issues = 0

    for fpath in target_files:
        res = probe_file_code_blocks(fpath)
        total_blocks += res["total_code_blocks"]
        status = "PASS" if res["passed"] else "FAIL"
        if not res["passed"]:
            all_passed = False
            total_issues += len(res["issues"])
        
        print(f"\n[{status}] {res['file']} (Blocks: {res['total_code_blocks']}, Issues: {len(res['issues'])})")
        for b in res["blocks"]:
            print(f"   - Lines {b['start_line']}..{b['end_line']}: lang='{b['lang']}' ({b['line_count']} lines)")
        for iss in res["issues"]:
            print(f"   [!] Line {iss['line']}: {iss['type']} -> {iss['message']}")
            print(f"       Raw: {iss['content']}")

    print("\n--------------------------------------------------------------------------------")
    print(f"Total files probed : {len(target_files)}")
    print(f"Total code blocks  : {total_blocks}")
    print(f"Total issues found : {total_issues}")
    print(f"Overall Status     : {'ALL PASS' if all_passed else 'FAILURES DETECTED'}")
    print("================================================================================")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

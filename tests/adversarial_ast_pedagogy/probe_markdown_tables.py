#!/usr/bin/env python3
"""
Adversarial Probe: Markdown Table Column Count Consistency
- Detects every markdown table across all files.
- Checks header row column count vs delimiter row column count vs data row column counts.
- Handles escaped pipes (\|).
- Fails if any row in any table has a column count mismatch.
"""

import os
import re
import sys
from typing import List, Dict, Any, Tuple

TARGET_DIR = "/mnt/second_drive/DOCS/Backend/teamwork_bilingual"

def split_table_row(line: str) -> List[str]:
    """
    Split a table row into cells, handling escaped pipes (\\|).
    Strips leading and trailing empty cells if the row starts/ends with '|'.
    """
    s = line.strip()
    if not s or "|" not in s:
        return []
    
    # Replace escaped pipe with placeholder
    placeholder = "\x00PIPE\x00"
    s_clean = s.replace("\\|", placeholder)
    
    # Split by pipe
    raw_cells = s_clean.split("|")
    
    # If the row starts with |, the first element in split is empty string
    if s.startswith("|") and len(raw_cells) > 0:
        raw_cells = raw_cells[1:]
    # If the row ends with |, the last element in split is empty string
    if s.endswith("|") and len(raw_cells) > 0:
        raw_cells = raw_cells[:-1]
        
    cells = [c.replace(placeholder, "|").strip() for c in raw_cells]
    return cells

def is_delimiter_row(cells: List[str]) -> bool:
    """Check if all cells match delimiter format, e.g., :---: or --- or :--- or ---:"""
    if not cells:
        return False
    delim_re = re.compile(r"^:?-+:?$")
    return all(delim_re.match(c) is not None for c in cells)

def probe_file_tables(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    tables = []
    issues = []
    
    in_code = False
    in_table = False
    current_table = {
        "start_line": 0,
        "header": [],
        "delimiter": [],
        "rows": [],
        "expected_cols": 0
    }

    for idx, raw_line in enumerate(lines, 1):
        line = raw_line.rstrip()
        stripped = line.strip()

        # Check code fence toggle
        if re.match(r"^\s*(`{3,}|~{3,})", stripped):
            in_code = not in_code
            if in_table:
                # End of table
                tables.append(current_table)
                in_table = False
            continue

        if in_code:
            continue

        if "|" in stripped and (stripped.startswith("|") or is_delimiter_row(split_table_row(stripped))):
            cells = split_table_row(stripped)
            if not in_table:
                # Starting new table
                in_table = True
                current_table = {
                    "start_line": idx,
                    "header_line": idx,
                    "header": cells,
                    "delimiter_line": None,
                    "delimiter": [],
                    "rows": [],
                    "expected_cols": len(cells)
                }
            elif current_table["delimiter_line"] is None:
                # Expecting delimiter row
                if is_delimiter_row(cells):
                    current_table["delimiter_line"] = idx
                    current_table["delimiter"] = cells
                    if len(cells) != current_table["expected_cols"]:
                        issues.append({
                            "line": idx,
                            "type": "DELIMITER_COLUMN_MISMATCH",
                            "message": f"Delimiter row on line {idx} has {len(cells)} cols, expected {current_table['expected_cols']}",
                            "raw": line
                        })
                else:
                    # Maybe header had no delimiter or something else
                    issues.append({
                        "line": idx,
                        "type": "MALFORMED_DELIMITER_ROW",
                        "message": f"Row on line {idx} after header is not a valid delimiter row",
                        "raw": line
                    })
            else:
                # Data row
                current_table["rows"].append((idx, cells, line))
                if len(cells) != current_table["expected_cols"]:
                    issues.append({
                        "line": idx,
                        "type": "DATA_ROW_COLUMN_MISMATCH",
                        "message": f"Data row on line {idx} has {len(cells)} cols, expected {current_table['expected_cols']}",
                        "raw": line
                    })
        else:
            if in_table:
                # End current table
                tables.append(current_table)
                in_table = False

    if in_table:
        tables.append(current_table)

    return {
        "file": os.path.basename(filepath),
        "total_lines": len(lines),
        "total_tables": len(tables),
        "tables": tables,
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
    print(" ADVERSARIAL PROBE: MARKDOWN TABLE COLUMN COUNT CONSISTENCY")
    print(f" Target Directory: {TARGET_DIR}")
    print("================================================================================")

    all_passed = True
    total_tables = 0
    total_issues = 0

    for fpath in target_files:
        res = probe_file_tables(fpath)
        total_tables += res["total_tables"]
        status = "PASS" if res["passed"] else "FAIL"
        if not res["passed"]:
            all_passed = False
            total_issues += len(res["issues"])

        print(f"\n[{status}] {res['file']} (Tables: {res['total_tables']}, Issues: {len(res['issues'])})")
        for t_idx, t in enumerate(res["tables"], 1):
            print(f"   Table {t_idx} (lines {t['start_line']}..): cols={t['expected_cols']}, rows={len(t['rows'])}")
        for iss in res["issues"]:
            print(f"   [!] Line {iss['line']}: {iss['type']} -> {iss['message']}")
            print(f"       Raw: {iss['raw']}")

    print("\n--------------------------------------------------------------------------------")
    print(f"Total files probed : {len(target_files)}")
    print(f"Total tables found : {total_tables}")
    print(f"Total issues found : {total_issues}")
    print(f"Overall Status     : {'ALL PASS' if all_passed else 'FAILURES DETECTED'}")
    print("================================================================================")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

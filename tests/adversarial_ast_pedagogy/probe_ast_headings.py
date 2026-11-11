#!/usr/bin/env python3
"""
Adversarial Probe: Heading Hierarchy, Level Skips, and Language Tag Matching
- Parses all markdown headings into an AST.
- Validates bilingual heading pairing:
  - English heading must be immediately followed by Vietnamese heading of the identical level.
  - Or detects any orphaned headings (missing counterpart).
- Validates heading hierarchy:
  - No downward level skips (e.g., H1 -> H3 without H2, H2 -> H4 without H3).
- Validates language tags:
  - Verifies canonical language tags `(English)` and `(Tiếng Việt)`.
  - Flags any heading lacking language tags or with malformed tags.
"""

import os
import re
import sys
from typing import List, Dict, Any, Tuple, Optional

TARGET_DIR = "/mnt/second_drive/DOCS/Backend/teamwork_bilingual"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")
EN_TAG_RE = re.compile(r"\((?:English|ENG)\)\s*$", re.IGNORECASE)
VI_TAG_RE = re.compile(r"\((?:Tiếng\s+Việt|VIE|Vietnamese)\)\s*$", re.IGNORECASE)

def probe_file_headings(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    headings = []
    in_code = False
    
    for idx, raw_line in enumerate(lines, 1):
        line = raw_line.rstrip()
        stripped = line.strip()

        # Check code fence
        if re.match(r"^\s*(`{3,}|~{3,})", stripped):
            in_code = not in_code
            continue
        if in_code:
            continue

        m = HEADING_RE.match(stripped)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            
            # Detect language tag
            lang = None
            if EN_TAG_RE.search(text):
                lang = "EN"
            elif VI_TAG_RE.search(text):
                lang = "VI"
            else:
                lang = "NONE"

            headings.append({
                "line": idx,
                "level": level,
                "text": text,
                "lang": lang,
                "raw": stripped
            })

    issues = []

    # Check 1: Language tags and pairing
    # In this documentation, headings are expected to appear in EN/VI pairs of identical level
    i = 0
    paired_groups = []
    while i < len(headings):
        curr = headings[i]
        
        # Check if current heading has a language tag
        if curr["lang"] == "NONE":
            issues.append({
                "line": curr["line"],
                "type": "MISSING_LANGUAGE_TAG",
                "message": f"Heading level H{curr['level']} on line {curr['line']} has no (English) or (Tiếng Việt) tag",
                "raw": curr["raw"]
            })
            i += 1
            continue

        if curr["lang"] == "EN":
            # Must be followed by VI heading of identical level
            if i + 1 >= len(headings):
                issues.append({
                    "line": curr["line"],
                    "type": "ORPHANED_ENGLISH_HEADING",
                    "message": f"English heading H{curr['level']} on line {curr['line']} has no matching Vietnamese heading (reached EOF)",
                    "raw": curr["raw"]
                })
                i += 1
            else:
                nxt = headings[i + 1]
                if nxt["lang"] != "VI":
                    issues.append({
                        "line": curr["line"],
                        "type": "UNPAIRED_ENGLISH_HEADING",
                        "message": f"English heading H{curr['level']} on line {curr['line']} is followed by {nxt['lang']} heading on line {nxt['line']} instead of VI",
                        "raw": curr["raw"]
                    })
                    i += 1
                elif nxt["level"] != curr["level"]:
                    issues.append({
                        "line": curr["line"],
                        "type": "LEVEL_MISMATCH_IN_PAIR",
                        "message": f"English heading H{curr['level']} on line {curr['line']} paired with Vietnamese heading H{nxt['level']} on line {nxt['line']}",
                        "raw": f"{curr['raw']}  <->  {nxt['raw']}"
                    })
                    paired_groups.append((curr, nxt))
                    i += 2
                else:
                    # Valid pair
                    paired_groups.append((curr, nxt))
                    i += 2
        elif curr["lang"] == "VI":
            # Unexpected leading VI heading without preceding EN heading
            issues.append({
                "line": curr["line"],
                "type": "ORPHANED_VIETNAMESE_HEADING",
                "message": f"Vietnamese heading H{curr['level']} on line {curr['line']} appears without preceding English heading",
                "raw": curr["raw"]
            })
            i += 1

    # Check 2: Level skips across heading hierarchy
    # We track effective current level.
    # Level can increase by at most 1 (e.g. H1 -> H2, H2 -> H3).
    # If it increases by > 1, e.g. H1 -> H3 or H2 -> H4, that's a level skip!
    prev_level = 0
    for h in headings:
        # If this is the second heading of an EN/VI pair with the same level, it doesn't change hierarchy depth
        curr_level = h["level"]
        if prev_level == 0:
            if curr_level > 1:
                issues.append({
                    "line": h["line"],
                    "type": "INITIAL_HEADING_LEVEL_SKIP",
                    "message": f"First heading on line {h['line']} is H{curr_level}, expected H1",
                    "raw": h["raw"]
                })
            prev_level = curr_level
        else:
            if curr_level > prev_level:
                if curr_level - prev_level > 1:
                    issues.append({
                        "line": h["line"],
                        "type": "HEADING_LEVEL_SKIP",
                        "message": f"Heading on line {h['line']} jumps from H{prev_level} to H{curr_level} (skipped level {prev_level + 1})",
                        "raw": h["raw"]
                    })
                prev_level = curr_level
            else:
                # Upwards transition (e.g. H4 -> H2) or same level (e.g. H2 -> H2) is permitted
                prev_level = curr_level

    return {
        "file": os.path.basename(filepath),
        "total_lines": len(lines),
        "total_headings": len(headings),
        "headings": headings,
        "paired_groups": paired_groups,
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
    print(" ADVERSARIAL PROBE: HEADING HIERARCHY, LEVEL SKIPS & LANGUAGE TAG MATCHING")
    print(f" Target Directory: {TARGET_DIR}")
    print("================================================================================")

    all_passed = True
    total_headings = 0
    total_issues = 0

    for fpath in target_files:
        res = probe_file_headings(fpath)
        total_headings += res["total_headings"]
        status = "PASS" if res["passed"] else "FAIL"
        if not res["passed"]:
            all_passed = False
            total_issues += len(res["issues"])

        print(f"\n[{status}] {res['file']} (Headings: {res['total_headings']}, Pairs: {len(res['paired_groups'])}, Issues: {len(res['issues'])})")
        for iss in res["issues"]:
            print(f"   [!] Line {iss['line']}: {iss['type']} -> {iss['message']}")
            print(f"       Raw: {iss['raw']}")

    print("\n--------------------------------------------------------------------------------")
    print(f"Total files probed   : {len(target_files)}")
    print(f"Total headings found : {total_headings}")
    print(f"Total issues found   : {total_issues}")
    print(f"Overall Status       : {'ALL PASS' if all_passed else 'FAILURES DETECTED'}")
    print("================================================================================")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

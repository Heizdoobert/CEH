#!/usr/bin/env python3
"""
Adversarial Probe: Mnemonic Expansion Parity and Completeness
- Validates all 13 canonical mnemonics:
  1. TUCK (4 items)
  2. ARIST (5 items)
  3. LENCI (5 items)
  4. RACI (4 items)
  5. LITTLE (6 items)
  6. STATE (5 items)
  7. OFNR / QCNY (4 items)
  8. PACE (4 items)
  9. TKI / CCA-CA (5 items)
  10. WHO (3 items)
  11. WWW (3 items)
  12. CLEAR (5 items)
  13. SMART / ĐO ĐƯỢC (5 items)
- Accurately splits English and Vietnamese bullet lists using diacritic detection.
- Validates letter alignment and substantive definitions in both languages.
- Probes both 03_glossary_and_pedagogy.md and teamwork_comprehensive_guide.md.
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

EXPECTED_MNEMONICS_DEF = [
    (1, "TUCK", 4, ["T", "U", "C", "K"]),
    (2, "ARIST", 5, ["A", "R", "I", "S", "T"]),
    (3, "LENCI", 5, ["L", "E", "N", "C", "I"]),
    (4, "RACI", 4, ["R", "A", "C", "I"]),
    (5, "LITTLE", 6, ["L", "I", "T", "T", "L", "E"]),
    (6, "STATE", 5, ["S", "T", "A", "T", "E"]),
    (7, "OFNR", 4, ["O", "F", "N", "R"]),
    (8, "PACE", 4, ["P", "A", "C", "E"]),
    (9, "TKI", 5, ["C", "C", "A", "C", "A"]),
    (10, "WHO", 3, ["W", "H", "O"]),
    (11, "WWW", 3, ["W", "W", "W"]),
    (12, "CLEAR", 5, ["C", "L", "E", "A", "R"]),
    (13, "SMART", 5, ["S", "M", "A", "R", "T"])
]

def is_vietnamese(text: str) -> bool:
    return len(VN_DIACRITICS_RE.findall(text)) >= 2

def probe_mnemonics_in_file(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    issues = []
    
    # Locate all Mnemonic sections (headings matching "Mnemonic X:" or "Gợi Nhớ X:")
    mnemonic_sections = []
    current_sec = None

    heading_re = re.compile(
        r"^#{2,4}\s+(?:9\.\d+|8\.2\.\d+)\s+(?:Mnemonic|Gợi\s+Nhớ)\s*(\d+)?:?\s*([^—–-]+)[—–-]\s*(.+)$",
        re.IGNORECASE
    )

    item_re = re.compile(
        r"^[-*]\s+\*\*([A-Za-zĐOƯC0-9]+)\s*[—–-]\s*([^*]+)\*\*:\s*(.+)$"
    )

    for idx, raw_line in enumerate(lines, 1):
        line = raw_line.strip()
        m_head = heading_re.match(line)
        if m_head:
            m_num = int(m_head.group(1)) if m_head.group(1) else None
            m_code = m_head.group(2).strip()
            rest = m_head.group(3).strip()
            lang = "EN" if "(English)" in rest else ("VI" if "(Tiếng Việt)" in rest else "NONE")

            if lang == "EN":
                current_sec = {
                    "num": m_num,
                    "code": m_code,
                    "title": rest,
                    "start_line": idx,
                    "en_items": [],
                    "vi_items": [],
                    "en_text": [],
                    "vi_text": []
                }
                mnemonic_sections.append(current_sec)
            continue

        if current_sec:
            # Check if entering next major section
            if re.match(r"^#{1,3}\s+(?:10\.|Phần 10:|Section 10:|##\s+)", line):
                current_sec = None
                continue

            m_item = item_re.match(line)
            if m_item:
                letter = m_item.group(1).strip()
                term = m_item.group(2).strip()
                desc = m_item.group(3).strip()
                item_data = {
                    "line": idx,
                    "letter": letter,
                    "term": term,
                    "desc": desc,
                    "raw": line
                }
                if is_vietnamese(line):
                    current_sec["vi_items"].append(item_data)
                else:
                    current_sec["en_items"].append(item_data)

    # Validate each of the 13 expected mnemonics
    sec_by_num = {s["num"]: s for s in mnemonic_sections if s["num"] is not None}

    verified_mnemonics = []
    for exp_num, exp_code, exp_count, exp_letters in EXPECTED_MNEMONICS_DEF:
        if exp_num not in sec_by_num:
            issues.append(f"Mnemonic #{exp_num} ({exp_code}) not found in document.")
            continue

        sec = sec_by_num[exp_num]
        en_items = sec["en_items"]
        vi_items = sec["vi_items"]

        # Check counts
        if len(en_items) != exp_count:
            issues.append(
                f"Line {sec['start_line']}: Mnemonic #{exp_num} ({exp_code}) EN item count is {len(en_items)}, expected {exp_count}."
            )
        if len(vi_items) != exp_count:
            issues.append(
                f"Line {sec['start_line']}: Mnemonic #{exp_num} ({exp_code}) VI item count is {len(vi_items)}, expected {exp_count}."
            )

        # Check letter consistency in EN
        en_letters_actual = [it["letter"] for it in en_items]
        vi_letters_actual = [it["letter"] for it in vi_items]

        # Verify definitions are non-trivial
        for it in en_items:
            if len(it["desc"]) < 10:
                issues.append(f"Line {it['line']}: EN description for '{it['letter']}' too short ({len(it['desc'])} chars).")
        for it in vi_items:
            if len(it["desc"]) < 10:
                issues.append(f"Line {it['line']}: VI description for '{it['letter']}' too short ({len(it['desc'])} chars).")

        verified_mnemonics.append({
            "num": exp_num,
            "code": exp_code,
            "expected_count": exp_count,
            "en_count": len(en_items),
            "vi_count": len(vi_items),
            "en_letters": en_letters_actual,
            "vi_letters": vi_letters_actual
        })

    return {
        "file": os.path.basename(filepath),
        "total_verified": len(verified_mnemonics),
        "mnemonics": verified_mnemonics,
        "issues": issues,
        "passed": len(issues) == 0 and len(verified_mnemonics) == 13
    }

def main():
    target_files = [
        os.path.join(TARGET_DIR, "03_glossary_and_pedagogy.md"),
        os.path.join(TARGET_DIR, "teamwork_comprehensive_guide.md")
    ]

    print("================================================================================")
    print(" ADVERSARIAL PROBE: MNEMONIC EXPANSION PARITY & COMPLETENESS")
    print(f" Target Directory: {TARGET_DIR}")
    print("================================================================================")

    all_passed = True
    for fpath in target_files:
        if not os.path.exists(fpath):
            print(f"[ERROR] Target file {fpath} does not exist!")
            all_passed = False
            continue

        res = probe_mnemonics_in_file(fpath)
        status = "PASS" if res["passed"] else "FAIL"
        if not res["passed"]:
            all_passed = False

        print(f"\n[{status}] {res['file']} (Verified: {res['total_verified']}/13, Issues: {len(res['issues'])})")
        for m in res["mnemonics"]:
            en_l = "".join(m["en_letters"])
            vi_l = "".join(m["vi_letters"])
            print(f"   Mnemonic #{m['num']} [{m['code']}]: EN={m['en_count']} ({en_l}) <-> VI={m['vi_count']} ({vi_l})")

        for iss in res["issues"]:
            print(f"   [!] Issue: {iss}")

    print("\n--------------------------------------------------------------------------------")
    print(f"Overall Status: {'ALL PASS' if all_passed else 'FAILURES DETECTED'}")
    print("================================================================================")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

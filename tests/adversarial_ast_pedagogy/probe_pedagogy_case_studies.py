#!/usr/bin/env python3
"""
Adversarial Probe: Case Study Pedagogy Completeness (Challenge-Action-Outcome)
- Verifies that all real-world case studies in Section 6 contain explicit
  Challenge, Action, and Outcome (CAO) components.
- Asserts presence and depth in BOTH English and Vietnamese.
- Evaluates both 02_communication_conflict_cases.md and teamwork_comprehensive_guide.md.
"""

import os
import re
import sys
from typing import List, Dict, Any

TARGET_DIR = "/mnt/second_drive/DOCS/Backend/teamwork_bilingual"

EXPECTED_CASE_STUDIES = [
    {
        "id": "6.1",
        "name": "Apollo 13 Mission Operations",
        "en_markers": ["Apollo 13", "NASA", "Cryogenic Tank", "Gene Kranz", "Tiger Team"],
        "vi_markers": ["Apollo 13", "NASA", "Vụ Nổ Bình Oxy", "Gene Kranz", "Đội Mãnh Hổ", "Tiger Team"],
        "challenge_en": ["catastrophic", "explosion", "failure", "oxygen tank", "dying spacecraft"],
        "challenge_vi": ["thảm khốc", "vụ nổ", "bình oxy", "chết dần"],
        "action_en": ["command architecture", "capcom", "tiger team", "lioh", "power", "slashing"],
        "action_vi": ["kiến trúc chỉ huy", "giao thức capcom", "đội mãnh hổ", "lioh", "điện lực", "cắt giảm"],
        "outcome_en": ["safe return", "principles extracted", "splashdown", "lessons"],
        "outcome_vi": ["trở về an toàn", "bài học", "đúc rút"]
    },
    {
        "id": "6.2",
        "name": "Pixar Braintrust",
        "en_markers": ["Pixar", "Braintrust", "Candor", "Plus-ing", "Catmull"],
        "vi_markers": ["Pixar", "Braintrust", "Thẳng Thắn", "Plus-ing", "Catmull"],
        "challenge_en": ["vulnerability", "early movies are bad", "mediocrity", "defensive"],
        "challenge_vi": ["tổn thương", "tệ hại", "ban đầu"],
        "action_en": ["decoupling critique", "zero mandate", "candor vs polite", "plus-ing"],
        "action_vi": ["tách rời", "không quyền chỉ thị", "thẳng thắn", "cộng thêm"],
        "outcome_en": ["principles extracted", "story rescues", "box office", "creative breakthroughs"],
        "outcome_vi": ["bài học", "đúc rút", "giải cứu kịch bản"]
    },
    {
        "id": "6.3",
        "name": "Aviation CRM & Healthcare Surgical Safety Checklists",
        "en_markers": ["Crew Resource Management", "CRM", "PACE", "WHO", "Surgical Safety Checklist"],
        "vi_markers": ["Quản Trị Nguồn Lực Tổ Bay", "CRM", "PACE", "WHO", "Bảng Kiểm An Toàn"],
        "challenge_en": ["disaster catalysts", "tenerife", "united 173", "authority gradient", "mortality"],
        "challenge_vi": ["thảm họa", "tenerife", "độ dốc quyền lực", "tử vong"],
        "action_en": ["two-challenge rule", "sterile cockpit", "pace", "who checklist", "sign in", "time out", "sign out"],
        "action_vi": ["hai lần cảnh báo", "buồng lái vô trùng", "pace", "bảng kiểm", "sign in", "time out", "sign out"],
        "outcome_en": ["clinical outcomes", "reduction", "mortality drop", "36%", "47%"],
        "outcome_vi": ["kết quả lâm sàng", "giảm 36%", "47%", "tỷ lệ tử vong"]
    }
]

def probe_case_studies_in_file(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    issues = []
    case_results = []

    for cs in EXPECTED_CASE_STUDIES:
        cs_res = {
            "id": cs["id"],
            "name": cs["name"],
            "found_en": False,
            "found_vi": False,
            "challenge_en_found": False,
            "challenge_vi_found": False,
            "action_en_found": False,
            "action_vi_found": False,
            "outcome_en_found": False,
            "outcome_vi_found": False,
        }

        # Check title markers
        text_lower = text.lower()
        cs_res["found_en"] = any(m.lower() in text_lower for m in cs["en_markers"])
        cs_res["found_vi"] = any(m.lower() in text_lower for m in cs["vi_markers"])

        if not cs_res["found_en"]:
            issues.append(f"Case study {cs['id']} ({cs['name']}) missing English title/markers.")
        if not cs_res["found_vi"]:
            issues.append(f"Case study {cs['id']} ({cs['name']}) missing Vietnamese title/markers.")

        # Check Challenge
        cs_res["challenge_en_found"] = any(k.lower() in text_lower for k in cs["challenge_en"])
        cs_res["challenge_vi_found"] = any(k.lower() in text_lower for k in cs["challenge_vi"])
        if not cs_res["challenge_en_found"]:
            issues.append(f"Case study {cs['id']} missing English Challenge analysis.")
        if not cs_res["challenge_vi_found"]:
            issues.append(f"Case study {cs['id']} missing Vietnamese Challenge analysis.")

        # Check Action
        cs_res["action_en_found"] = any(k.lower() in text_lower for k in cs["action_en"])
        cs_res["action_vi_found"] = any(k.lower() in text_lower for k in cs["action_vi"])
        if not cs_res["action_en_found"]:
            issues.append(f"Case study {cs['id']} missing English Action analysis.")
        if not cs_res["action_vi_found"]:
            issues.append(f"Case study {cs['id']} missing Vietnamese Action analysis.")

        # Check Outcome
        cs_res["outcome_en_found"] = any(k.lower() in text_lower for k in cs["outcome_en"])
        cs_res["outcome_vi_found"] = any(k.lower() in text_lower for k in cs["outcome_vi"])
        if not cs_res["outcome_en_found"]:
            issues.append(f"Case study {cs['id']} missing English Outcome analysis.")
        if not cs_res["outcome_vi_found"]:
            issues.append(f"Case study {cs['id']} missing Vietnamese Outcome analysis.")

        case_results.append(cs_res)

    return {
        "file": os.path.basename(filepath),
        "case_results": case_results,
        "issues": issues,
        "passed": len(issues) == 0
    }

def main():
    target_files = [
        os.path.join(TARGET_DIR, "02_communication_conflict_cases.md"),
        os.path.join(TARGET_DIR, "teamwork_comprehensive_guide.md")
    ]

    print("================================================================================")
    print(" ADVERSARIAL PROBE: CASE STUDY PEDAGOGY (CHALLENGE-ACTION-OUTCOME)")
    print(f" Target Directory: {TARGET_DIR}")
    print("================================================================================")

    all_passed = True
    for fpath in target_files:
        if not os.path.exists(fpath):
            print(f"[ERROR] Target file {fpath} does not exist!")
            all_passed = False
            continue

        res = probe_case_studies_in_file(fpath)
        status = "PASS" if res["passed"] else "FAIL"
        if not res["passed"]:
            all_passed = False

        print(f"\n[{status}] {res['file']}")
        for cs in res["case_results"]:
            print(f"   Case {cs['id']}: {cs['name']}")
            print(f"     - EN: Title={'✓' if cs['found_en'] else '✗'}, Challenge={'✓' if cs['challenge_en_found'] else '✗'}, Action={'✓' if cs['action_en_found'] else '✗'}, Outcome={'✓' if cs['outcome_en_found'] else '✗'}")
            print(f"     - VI: Title={'✓' if cs['found_vi'] else '✗'}, Challenge={'✓' if cs['challenge_vi_found'] else '✗'}, Action={'✓' if cs['action_vi_found'] else '✗'}, Outcome={'✓' if cs['outcome_vi_found'] else '✗'}")

        for iss in res["issues"]:
            print(f"   [!] Issue: {iss}")

    print("\n--------------------------------------------------------------------------------")
    print(f"Overall Status: {'ALL PASS' if all_passed else 'FAILURES DETECTED'}")
    print("================================================================================")
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

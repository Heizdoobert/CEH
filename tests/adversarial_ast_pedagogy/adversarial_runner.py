#!/usr/bin/env python3
"""
Master Adversarial Test Runner for Challenger Teamwork 2
Executes all adversarial AST structural verifications, markdown syntax edge-case probes,
and pedagogy completeness audits.
"""

import os
import sys
import time

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from probe_ast_headings import probe_file_headings, TARGET_DIR
from probe_paragraph_symmetry import probe_file_paragraph_symmetry
from probe_code_fences import probe_file_code_blocks
from probe_markdown_tables import probe_file_tables
from probe_pedagogy_case_studies import probe_case_studies_in_file
from probe_pedagogy_active_recall import probe_file_active_recall
from probe_pedagogy_mnemonics import probe_mnemonics_in_file

def run_master_adversarial_suite():
    start_time = time.time()
    
    md_files = sorted([
        os.path.join(TARGET_DIR, f)
        for f in os.listdir(TARGET_DIR)
        if f.endswith(".md")
    ])

    print("================================================================================")
    print(" CHALLENGER 2: MASTER ADVERSARIAL AST & PEDAGOGY VERIFICATION SUITE")
    print(f" Target Directory : {TARGET_DIR}")
    print(f" Probed Files     : {len(md_files)} markdown documents")
    print("================================================================================")

    suite_results = {}
    critical_defects = []

    # 1. AST Headings & Hierarchy
    print("\n>>> PROBE 1: AST Heading Hierarchy, Level Skips & Bilingual Tags...")
    h_pass = True
    total_h = 0
    h_issues = []
    for f in md_files:
        res = probe_file_headings(f)
        total_h += res["total_headings"]
        if not res["passed"]:
            h_pass = False
            for iss in res["issues"]:
                h_issues.append((res["file"], iss))
                critical_defects.append({
                    "probe": "AST_HEADINGS",
                    "file": res["file"],
                    "line": iss["line"],
                    "type": iss["type"],
                    "desc": iss["message"],
                    "evidence": iss["raw"]
                })
    suite_results["Heading Hierarchy & Dual Tags"] = {
        "status": "PASS" if h_pass else "FAIL",
        "total_probed": total_h,
        "issues_count": len(h_issues)
    }

    # 2. Code Block Integrity
    print(">>> PROBE 2: Code Block Triple-Backtick Fences & Language Identifiers...")
    cb_pass = True
    total_cb = 0
    cb_issues = []
    for f in md_files:
        res = probe_file_code_blocks(f)
        total_cb += res["total_code_blocks"]
        if not res["passed"]:
            cb_pass = False
            for iss in res["issues"]:
                cb_issues.append((res["file"], iss))
                critical_defects.append({
                    "probe": "CODE_BLOCKS",
                    "file": res["file"],
                    "line": iss["line"],
                    "type": iss["type"],
                    "desc": iss["message"],
                    "evidence": iss["content"]
                })
    suite_results["Code Block Fences & Language Tags"] = {
        "status": "PASS" if cb_pass else "FAIL",
        "total_probed": total_cb,
        "issues_count": len(cb_issues)
    }

    # 3. Markdown Table Column Consistency
    print(">>> PROBE 3: Markdown Table Column Count Consistency...")
    tbl_pass = True
    total_tbl = 0
    tbl_issues = []
    for f in md_files:
        res = probe_file_tables(f)
        total_tbl += res["total_tables"]
        if not res["passed"]:
            tbl_pass = False
            for iss in res["issues"]:
                tbl_issues.append((res["file"], iss))
                critical_defects.append({
                    "probe": "TABLE_COLUMNS",
                    "file": res["file"],
                    "line": iss["line"],
                    "type": iss["type"],
                    "desc": iss["message"],
                    "evidence": iss["raw"]
                })
    suite_results["Markdown Table Columns"] = {
        "status": "PASS" if tbl_pass else "FAIL",
        "total_probed": total_tbl,
        "issues_count": len(tbl_issues)
    }

    # 4. Paragraph Symmetry & Strict 1:1 Alternation
    print(">>> PROBE 4: Paragraph Symmetry & 1:1 Alternation...")
    sym_pass = True
    total_content = 0
    sym_issues = []
    for f in md_files:
        res = probe_file_paragraph_symmetry(f)
        total_content += res["total_content_blocks"]
        if not res["passed"]:
            sym_pass = False
            for iss in res["issues"]:
                sym_issues.append((res["file"], iss))
    suite_results["Paragraph Symmetry & 1:1 Alternation"] = {
        "status": "PASS" if sym_pass else "FAIL",
        "total_probed": total_content,
        "issues_count": len(sym_issues)
    }

    # 5. Case Study Pedagogy (Challenge-Action-Outcome)
    print(">>> PROBE 5: Case Study Pedagogy (Challenge-Action-Outcome)...")
    cs_pass = True
    cs_targets = [
        os.path.join(TARGET_DIR, "02_communication_conflict_cases.md"),
        os.path.join(TARGET_DIR, "teamwork_comprehensive_guide.md")
    ]
    cs_count = 0
    for f in cs_targets:
        res = probe_case_studies_in_file(f)
        cs_count += len(res["case_results"])
        if not res["passed"]:
            cs_pass = False
            for iss in res["issues"]:
                critical_defects.append({
                    "probe": "CASE_STUDY_PEDAGOGY",
                    "file": res["file"],
                    "line": 0,
                    "type": "MISSING_CAO_ELEMENT",
                    "desc": iss,
                    "evidence": "N/A"
                })
    suite_results["Case Study Pedagogy (CAO)"] = {
        "status": "PASS" if cs_pass else "FAIL",
        "total_probed": cs_count,
        "issues_count": 0 if cs_pass else 1
    }

    # 6. Active Recall Q&A Parity
    print(">>> PROBE 6: Active Recall Prompts & Answers Parity...")
    qa_pass = True
    qa_total = 0
    for f in md_files:
        res = probe_file_active_recall(f)
        qa_total += res["total_pairs"]
        if not res["passed"]:
            qa_pass = False
            for iss in res["issues"]:
                critical_defects.append({
                    "probe": "ACTIVE_RECALL_QA",
                    "file": res["file"],
                    "line": 0,
                    "type": "QA_PARITY_DEFECT",
                    "desc": iss,
                    "evidence": "N/A"
                })
    suite_results["Active Recall Prompts & Answers"] = {
        "status": "PASS" if qa_pass else "FAIL",
        "total_probed": qa_total,
        "issues_count": 0 if qa_pass else 1
    }

    # 7. Mnemonic Expansion Parity
    print(">>> PROBE 7: Mnemonic Expansion Parity & Completeness...")
    mn_pass = True
    mn_total = 0
    mn_targets = [
        os.path.join(TARGET_DIR, "03_glossary_and_pedagogy.md"),
        os.path.join(TARGET_DIR, "teamwork_comprehensive_guide.md")
    ]
    for f in mn_targets:
        res = probe_mnemonics_in_file(f)
        mn_total += res["total_verified"]
        if not res["passed"]:
            mn_pass = False
            for iss in res["issues"]:
                critical_defects.append({
                    "probe": "MNEMONICS_EXPANSION",
                    "file": res["file"],
                    "line": 0,
                    "type": "MNEMONIC_DEFECT",
                    "desc": iss,
                    "evidence": "N/A"
                })
    suite_results["Mnemonic Expansion Parity"] = {
        "status": "PASS" if mn_pass else "FAIL",
        "total_probed": mn_total,
        "issues_count": 0 if mn_pass else 1
    }

    elapsed = time.time() - start_time

    print("\n================================================================================")
    print(" ADVERSARIAL SUITE SUMMARY SCOREBOARD")
    print("================================================================================")
    print(f"{'Probe / Check Name':<45} | {'Probed':<8} | {'Issues':<8} | {'Status':<6}")
    print("--------------------------------------------------------------------------------")
    for name, data in suite_results.items():
        print(f"{name:<45} | {data['total_probed']:<8} | {data['issues_count']:<8} | {data['status']:<6}")
    print("--------------------------------------------------------------------------------")
    print(f"Total Execution Time : {elapsed:.2f}s")
    
    overall_verdict = "REQUEST_CHANGES" if critical_defects or not sym_pass else "APPROVE"
    print(f"Overall Verdict      : {overall_verdict}")
    print("================================================================================")

    if critical_defects:
        print("\n--- CRITICAL DEFECTS LOGGED ---")
        for idx, d in enumerate(critical_defects, 1):
            print(f"Defect #{idx}: [{d['probe']}] in {d['file']} (Line {d['line']})")
            print(f"  Type    : {d['type']}")
            print(f"  Details : {d['desc']}")
            print(f"  Evidence: {d['evidence']}")

    return 0 if overall_verdict == "APPROVE" else 1

if __name__ == "__main__":
    sys.exit(run_master_adversarial_suite())

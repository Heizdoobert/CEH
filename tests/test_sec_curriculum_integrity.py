import os
import re
import urllib.parse
import subprocess
from pathlib import Path
import pytest

SEC_DIR = Path("/mnt/second_drive/DOCS/SEC")
DOCS_DIR = SEC_DIR / "docs"
EXT_DIR = DOCS_DIR / "References" / "External_Downloads"
EXAMS_DIR = DOCS_DIR / "Exams"
REPORTS_DIR = DOCS_DIR / "Reports"
CHEATSHEETS_DIR = DOCS_DIR / "Cheatsheets"
LABS_DIR = SEC_DIR / "labs"
ARSENAL_DIR = SEC_DIR / "scripts" / "arsenal"

def test_root_coordinator_exists():
    """Verify master coordinator exists at root in pure .md, with no .docx or .pdf."""
    root_guide_md = SEC_DIR / "DIEU_PHOI_LO_TRINH_DOC.md"
    assert root_guide_md.exists(), "Root coordinator file DIEU_PHOI_LO_TRINH_DOC.md must exist"
    assert not (SEC_DIR / "DIEU_PHOI_LO_TRINH_DOC.docx").exists(), "DIEU_PHOI_LO_TRINH_DOC.docx must not exist"
    assert not (SEC_DIR / "DIEU_PHOI_LO_TRINH_DOC.pdf").exists(), "DIEU_PHOI_LO_TRINH_DOC.pdf must not exist"
    
    content = root_guide_md.read_text(encoding="utf-8")
    for i in range(1, 7):
        assert f"MỤC TIÊU {i}:" in content, f"Coordinator must contain MỤC TIÊU {i}"

def test_master_curriculum_documents():
    """Verify master curriculum documents exist in .md, and no self-generated .docx or .pdf exists."""
    core_docs = [
        DOCS_DIR / "Roadmap" / "01_Master_Study_Roadmap",
        DOCS_DIR / "Lectures" / "02_Master_Lecture_and_Lab_Plan",
        DOCS_DIR / "Matrix" / "03_Knowledge_Linkage_and_Cross_Reference_Matrix",
        DOCS_DIR / "README",
    ]
    for doc in core_docs:
        md_file = doc.with_suffix(".md")
        docx_file = doc.with_suffix(".docx")
        pdf_file = doc.with_suffix(".pdf")
        
        assert md_file.exists() and md_file.stat().st_size > 0, f"{md_file} must exist and not be empty"
        assert not docx_file.exists(), f"Self-generated DOCX {docx_file} must not exist"
        assert not pdf_file.exists(), f"Self-generated PDF {pdf_file} must not exist"

def test_reference_playbooks():
    """Verify all 7 reference playbooks exist as pure .md, and no self-generated .docx or .pdf exists."""
    playbooks = [
        "01_MITRE_ATTCK_Enterprise_Matrix_Guide",
        "02_Active_Directory_Attack_and_Defense_Playbook",
        "03_OWASP_Top_10_and_API_Security_DeepDive",
        "04_Network_Penetration_Testing_Cheatsheet",
        "05_EDR_Evasion_and_Living_Off_The_Land_LOLBAS",
        "06_NIST_SP_800-115_Technical_Guide",
        "07_OWASP_Top_10_Evolution_Matrix",
    ]
    ref_dir = DOCS_DIR / "References"
    for pb in playbooks:
        md_file = ref_dir / f"{pb}.md"
        docx_file = ref_dir / f"{pb}.docx"
        pdf_file = ref_dir / f"{pb}.pdf"
        
        assert md_file.exists() and md_file.stat().st_size > 0, f"{md_file} must exist"
        assert not docx_file.exists(), f"Extraneous DOCX {docx_file} must not exist"
        assert not pdf_file.exists(), f"Extraneous PDF {pdf_file} must not exist"

def test_external_downloaded_references():
    """Verify authentic external security documents downloaded from internet exist and are valid."""
    assert EXT_DIR.exists(), "External_Downloads directory must exist"
    assert (EXT_DIR / "README.md").exists(), "External_Downloads README.md must exist"
    
    expected_downloads = [
        "Enterprise_VAPT_Report_NIST_SP800-115_Sample.docx",
        "Enterprise_VAPT_Report_NIST_SP800-115_Sample.pdf",
        "NIST_SP_800-115_Technical_Guide_Official.pdf",
        "OWASP_Web_Security_Testing_Guide_WSTG_v4.2.pdf",
        "OWASP_API_Security_Top_10_Official.pdf",
        "OWASP_Top_Ten_Historical_Comparison_2003_to_2021.pdf",
        "SANS_PowerShell_PenTest_CheatSheet_v41.pdf",
        "Metasploit_Framework_CheatSheet.pdf",
        "Wireshark_Display_Filters_CheatSheet.pdf",
        "SQLMap_Injection_CheatSheet_v1.0.pdf",
        "OpenVAS_Vulnerability_Scan_Report_Sample.pdf",
        "SANS_BloodHound_Active_Directory_CheatSheet.pdf",
        "SANS_PenTest_Pivots_and_Payloads.pdf",
        "SANS_Burp_Suite_Web_Pentest_CheatSheet.pdf",
        "SANS_Malware_Analysis_and_Reverse_Engineering.pdf",
        "SANS_Ultimate_Pen_Test_Poster.pdf",
        "SANS_TCPIP_Packet_CheatSheet_2021.pdf",
        "SANS_Cloud_Security_AWS_Azure_GCP.pdf",
        "SANS_PenTest_Rules_of_Engagement_Worksheet.pdf",
    ]
    for filename in expected_downloads:
        file_path = EXT_DIR / filename
        assert file_path.exists(), f"Downloaded file {filename} must exist"
        assert file_path.stat().st_size > 10_000, f"Downloaded file {filename} must be > 10KB"

def test_ceh_and_networking_coverage():
    """Verify CEH and Networking notes are preserved in .md format."""
    ceh_md = list((SEC_DIR / "CEH-Notes").rglob("*.md"))
    net_md = list((SEC_DIR / "01_Computer_Networking").rglob("*.md"))
    lab_md = list((SEC_DIR / "03_Ethical_Hacking_Lab_Reports").rglob("*.md"))
    
    assert len(ceh_md) >= 20, f"Expected >= 20 CEH markdown files, got {len(ceh_md)}"
    assert len(net_md) >= 15, f"Expected >= 15 Networking markdown files, got {len(net_md)}"
    assert len(lab_md) >= 11, f"Expected >= 11 Lab report markdown files, got {len(lab_md)}"

def test_exams_and_scenarios_integrity():
    """Verify CEH question bank (>= 125 Qs) and Red Team scenarios (>= 50 Scenarios)."""
    ceh_bank = EXAMS_DIR / "01_CEH_v12_Practice_Questions_Bank.md"
    scen_bank = EXAMS_DIR / "02_Red_Team_Scenario_Interview_Questions.md"
    
    assert ceh_bank.exists(), f"{ceh_bank} must exist"
    assert scen_bank.exists(), f"{scen_bank} must exist"
    
    ceh_text = ceh_bank.read_text(encoding="utf-8")
    scen_text = scen_bank.read_text(encoding="utf-8")
    
    ceh_questions = re.findall(r'#### Câu (\d+)', ceh_text)
    assert len(ceh_questions) >= 125, f"Expected >= 125 CEH questions, got {len(ceh_questions)}"
    
    scenarios = re.findall(r'#### Kịch bản (\d+)', scen_text)
    assert len(scenarios) >= 50, f"Expected >= 50 Red Team scenarios, got {len(scenarios)}"
    
    # Assert no stray DOCX/PDF in exams dir
    assert not list(EXAMS_DIR.glob("*.docx")), "No DOCX files allowed in Exams dir"
    assert not list(EXAMS_DIR.glob("*.pdf")), "No PDF files allowed in Exams dir"

def test_docker_lab_environment():
    """Verify Docker lab configuration, verify script, and pure markdown guide."""
    compose_file = LABS_DIR / "docker-compose.yml"
    readme_file = LABS_DIR / "README.md"
    verify_script = LABS_DIR / "scripts" / "verify_lab_config.py"
    
    assert compose_file.exists(), f"{compose_file} must exist"
    assert readme_file.exists(), f"{readme_file} must exist"
    assert verify_script.exists(), f"{verify_script} must exist"
    
    # Run the lab verifier script
    res = subprocess.run(["/usr/bin/python3.11", str(verify_script)], capture_output=True, text=True, check=True)
    assert "[SUCCESS] Lab Environment Configuration verified 100% successfully!" in res.stdout

def test_exam_simulator_cli():
    """Verify exam_simulator.py CLI test execution."""
    sim_script = SEC_DIR / "exam_simulator.py"
    assert sim_script.exists(), "exam_simulator.py must exist"
    
    res = subprocess.run(["/usr/bin/python3.11", str(sim_script), "test"], capture_output=True, text=True, check=True)
    assert "[SUCCESS] exam_simulator test passed!" in res.stdout
    assert "Tổng số câu hỏi trắc nghiệm CEH v12: 125 câu" in res.stdout
    assert "Tổng số kịch bản Red Team phỏng vấn: 50 kịch bản" in res.stdout

def test_no_self_generated_docx_or_pdf():
    """Verify that NO self-generated DOCX or PDF files exist for authored markdown documents."""
    # Ensure zero DOCX outside External_Downloads
    all_docx = [f for f in SEC_DIR.rglob("*.docx") if not any(p.startswith(".") for p in f.parts)]
    non_external_docx = [f for f in all_docx if "External_Downloads" not in f.parts]
    assert not non_external_docx, f"Found extraneous DOCX files: {non_external_docx}"
    
    # Ensure no export directory exists
    assert not (DOCS_DIR / "Exports").exists(), "docs/Exports must not exist"
    
    # Ensure all authored master documents have NO parallel .docx or .pdf
    authored_markdowns = [
        SEC_DIR / "DIEU_PHOI_LO_TRINH_DOC.md",
        DOCS_DIR / "Roadmap" / "01_Master_Study_Roadmap.md",
        DOCS_DIR / "Lectures" / "02_Master_Lecture_and_Lab_Plan.md",
        DOCS_DIR / "Matrix" / "03_Knowledge_Linkage_and_Cross_Reference_Matrix.md",
        DOCS_DIR / "README.md",
        EXAMS_DIR / "01_CEH_v12_Practice_Questions_Bank.md",
        EXAMS_DIR / "02_Red_Team_Scenario_Interview_Questions.md",
        LABS_DIR / "README.md",
    ]
    for md in authored_markdowns:
        assert md.exists(), f"Markdown {md} must exist"
        assert not md.with_suffix(".docx").exists(), f"Duplicate DOCX {md.with_suffix('.docx')} must not exist"
        assert not md.with_suffix(".pdf").exists(), f"Duplicate PDF {md.with_suffix('.pdf')} must not exist"
        
    for pb in (DOCS_DIR / "References").glob("*.md"):
        assert not pb.with_suffix(".docx").exists(), f"Extraneous DOCX {pb.with_suffix('.docx')} must not exist"
        assert not pb.with_suffix(".pdf").exists(), f"Extraneous PDF {pb.with_suffix('.pdf')} must not exist"

def test_reports_and_cheatsheets_integrity():
    """Verify VAPT reports and Cheatsheets exist and contain required enterprise content."""
    vapt_report = REPORTS_DIR / "01_Enterprise_VAPT_Report_Template_vi.md"
    debrief_report = REPORTS_DIR / "02_Red_Team_Operation_Debrief_Sample_vi.md"
    red_cheatsheet = CHEATSHEETS_DIR / "01_Red_Team_One_Liners_Cheatsheet.md"
    blue_cheatsheet = CHEATSHEETS_DIR / "02_Blue_Team_Detection_and_Event_IDs.md"
    
    for doc in [vapt_report, debrief_report, red_cheatsheet, blue_cheatsheet]:
        assert doc.exists() and doc.stat().st_size > 1000, f"{doc} must exist and be populated"
        assert not doc.with_suffix(".docx").exists(), f"Extraneous DOCX {doc.with_suffix('.docx')} must not exist"
        assert not doc.with_suffix(".pdf").exists(), f"Extraneous PDF {doc.with_suffix('.pdf')} must not exist"

def test_arsenal_scripts_execution():
    """Verify all Python scripts in scripts/arsenal/ exist and execute properly."""
    assert ARSENAL_DIR.exists(), "scripts/arsenal directory must exist"
    assert (ARSENAL_DIR / "README.md").exists(), "scripts/arsenal/README.md must exist"
    
    # 1. Test JWT Tool Lite
    jwt_script = ARSENAL_DIR / "jwt_tool_lite.py"
    assert jwt_script.exists(), "jwt_tool_lite.py must exist"
    res_jwt = subprocess.run(["/usr/bin/python3.11", str(jwt_script)], capture_output=True, text=True, check=True)
    assert "[SUCCESS] Self-test completed." in res_jwt.stdout
    
    # 2. Test Reverse Shell Generator
    rev_script = ARSENAL_DIR / "reverse_shell_generator.py"
    assert rev_script.exists(), "reverse_shell_generator.py must exist"
    res_rev = subprocess.run(["/usr/bin/python3.11", str(rev_script), "--type", "bash_tcp"], capture_output=True, text=True, check=True)
    assert "bash -i >& /dev/tcp/" in res_rev.stdout
    
    # 3. Test AD BloodHound Analyzer
    ad_script = ARSENAL_DIR / "ad_bloodhound_analyzer.py"
    assert ad_script.exists(), "ad_bloodhound_analyzer.py must exist"
    res_ad = subprocess.run(["/usr/bin/python3.11", str(ad_script)], capture_output=True, text=True, check=True)
    assert "ACTIVE DIRECTORY THREAT & ESCALATION PATH ANALYZER" in res_ad.stdout
    assert "Kerberoastable Service Accounts" in res_ad.stdout

def test_link_integrity_in_markdown():
    """Verify that all file:/// links in coordinator guide, matrix, readme, labs, reports, cheatsheets point to existing files."""
    docs_to_check = [
        SEC_DIR / "DIEU_PHOI_LO_TRINH_DOC.md",
        DOCS_DIR / "Matrix" / "03_Knowledge_Linkage_and_Cross_Reference_Matrix.md",
        DOCS_DIR / "README.md",
        LABS_DIR / "README.md",
        EXT_DIR / "README.md",
        ARSENAL_DIR / "README.md",
        CHEATSHEETS_DIR / "01_Red_Team_One_Liners_Cheatsheet.md",
        CHEATSHEETS_DIR / "02_Blue_Team_Detection_and_Event_IDs.md",
    ]
    
    link_pattern = re.compile(r'\[([^\]]+)\]\(file://([^#\)]+)(?:#[^\)]*)?\)')
    
    total_links_verified = 0
    missing_links = []
    
    for doc in docs_to_check:
        assert doc.exists(), f"{doc} must exist"
        text = doc.read_text(encoding="utf-8")
        matches = link_pattern.findall(text)
        for label, raw_path in matches:
            decoded_path = urllib.parse.unquote(raw_path.strip())
            p = Path(decoded_path)
            if not p.exists():
                missing_links.append((doc.name, label, decoded_path))
            else:
                total_links_verified += 1
                
    assert not missing_links, f"Found broken file links: {missing_links}"
    assert total_links_verified > 60, f"Expected > 60 verified links, got {total_links_verified}"

def test_sec_navigator_cli():
    """Verify sec_navigator.py CLI works and returns valid stats and streams."""
    nav_script = SEC_DIR / "sec_navigator.py"
    assert nav_script.exists(), "sec_navigator.py must exist"
    
    # Test stats
    res_stats = subprocess.run(["/usr/bin/python3.11", str(nav_script), "stats"], capture_output=True, text=True, check=True)
    assert "THỐNG KÊ KHO TRI THỨC" in res_stats.stdout
    assert "125 câu hỏi có đáp án/giải thích" in res_stats.stdout
    
    # Test stream 5
    res_stream = subprocess.run(["/usr/bin/python3.11", str(nav_script), "stream", "5"], capture_output=True, text=True, check=True)
    assert "TÁC CHIẾN RED TEAM" in res_stream.stdout
    assert "[V] OK" in res_stream.stdout

#!/usr/bin/env python3
"""
Active Directory BloodHound & ACL Analyzer
Part of Cybersecurity Arsenal Scripts
Parses BloodHound JSON nodes and edges, identifies critical attack paths:
- Kerberoastable Service Accounts (SPNs)
- AS-REP Roastable Accounts (No Pre-Authentication)
- Unconstrained Delegation Risks
- High-Privilege ACL Misconfigurations (GenericAll, WriteDacl)
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any

# Mock sample AD data for offline testing and lab demonstration
SAMPLE_AD_DATA = {
    "users": [
        {"name": "ALICE@CORP.LOCAL", "adminCount": False, "spn": None, "dontReqPreAuth": False, "delegation": False},
        {"name": "MSSQL_SVC@CORP.LOCAL", "adminCount": False, "spn": "MSSQLSvc/db01.corp.local:1433", "dontReqPreAuth": False, "delegation": False},
        {"name": "IIS_SERVICE@CORP.LOCAL", "adminCount": False, "spn": "HTTP/web.corp.local", "dontReqPreAuth": False, "delegation": True},
        {"name": "BACKUP_ACC@CORP.LOCAL", "adminCount": False, "spn": None, "dontReqPreAuth": True, "delegation": False},
        {"name": "DA_JOHN@CORP.LOCAL", "adminCount": True, "spn": None, "dontReqPreAuth": False, "delegation": False},
    ],
    "acls": [
        {"source": "ALICE@CORP.LOCAL", "target": "IT-HELP-DESK@CORP.LOCAL", "rightName": "AddMember"},
        {"source": "IT-HELP-DESK@CORP.LOCAL", "target": "MSSQL_SVC@CORP.LOCAL", "rightName": "GenericAll"},
        {"source": "MSSQL_SVC@CORP.LOCAL", "target": "DOMAIN ADMINS@CORP.LOCAL", "rightName": "WriteDacl"},
    ]
}

def analyze_users(users: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    results = {
        "kerberoastable": [],
        "asrep_roastable": [],
        "unconstrained_delegation": [],
        "domain_admins": []
    }
    for u in users:
        name = u.get("name", "Unknown")
        if u.get("spn"):
            results["kerberoastable"].append(f"{name} (SPN: {u['spn']})")
        if u.get("dontReqPreAuth"):
            results["asrep_roastable"].append(f"{name}")
        if u.get("delegation"):
            results["unconstrained_delegation"].append(f"{name}")
        if u.get("adminCount"):
            results["domain_admins"].append(f"{name}")
            
    return results

def analyze_acls(acls: List[Dict[str, Any]]) -> List[str]:
    critical_edges = []
    for acl in acls:
        src = acl.get("source", "")
        dst = acl.get("target", "")
        right = acl.get("rightName", "")
        if right in ["GenericAll", "WriteDacl", "ForceChangePassword", "AddMember", "Owns"]:
            critical_edges.append(f"[{right}] {src} ===> {dst}")
    return critical_edges

def main():
    parser = argparse.ArgumentParser(description="Active Directory ACL & BloodHound Analyzer")
    parser.add_argument("--json-file", help="Path to BloodHound users/computers JSON file")
    args = parser.parse_args()
    
    data = SAMPLE_AD_DATA
    if args.json_file:
        p = Path(args.json_file)
        if p.exists():
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            print(f"[!] File {args.json_file} not found. Running with embedded sample data.")
            
    users = data.get("users", [])
    acls = data.get("acls", [])
    
    print("=" * 65)
    print("      ACTIVE DIRECTORY THREAT & ESCALATION PATH ANALYZER")
    print("=" * 65)
    
    u_findings = analyze_users(users)
    print(f"\n[1] Kerberoastable Service Accounts ({len(u_findings['kerberoastable'])} found):")
    for item in u_findings['kerberoastable']:
        print(f"  [+] {item}")
        
    print(f"\n[2] AS-REP Roastable Accounts (No Pre-Auth) ({len(u_findings['asrep_roastable'])} found):")
    for item in u_findings['asrep_roastable']:
        print(f"  [+] {item}")
        
    print(f"\n[3] Unconstrained Delegation Risks ({len(u_findings['unconstrained_delegation'])} found):")
    for item in u_findings['unconstrained_delegation']:
        print(f"  [+] {item}")
        
    acl_findings = analyze_acls(acls)
    print(f"\n[4] Dangerous ACL Escalation Relationships ({len(acl_findings)} found):")
    for item in acl_findings:
        print(f"  [!] {item}")
        
    print("\n" + "=" * 65)
    print("  TỔNG KẾT KHUYẾN NGHỊ KHẮC PHỤC (BLUE TEAM REMEDIATION):")
    print("  * Chuyển service accounts sang gMSA (Group Managed Service Accounts).")
    print("  * Bỏ cờ DONT_REQ_PREAUTH trên toàn bộ người dùng Active Directory.")
    print("  * Rà soát thu hồi quyền GenericAll/WriteDacl trên các nhóm đặc quyền.")
    print("=" * 65)

if __name__ == "__main__":
    main()

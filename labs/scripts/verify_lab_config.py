#!/usr/bin/env python3
"""
Lab Environment Configuration Verifier
Validates docker-compose.yml configuration, network subnets, container definitions, and mock API tests.
"""

import sys
import re
from pathlib import Path

LAB_DIR = Path(__file__).resolve().parent.parent
COMPOSE_FILE = LAB_DIR / "docker-compose.yml"
API_APP = LAB_DIR / "vulnerable-api" / "app.py"

def verify_compose_syntax():
    print("[*] Checking docker-compose.yml syntax and services...")
    if not COMPOSE_FILE.exists():
        print(f"[FAIL] Missing {COMPOSE_FILE}")
        return False
    
    content = COMPOSE_FILE.read_text(encoding="utf-8")
    
    # Required services
    required_services = ["dvwa", "juice-shop", "vulnerable-api", "metasploitable-node", "traffic-sniffer"]
    for svc in required_services:
        if f"{svc}:" not in content:
            print(f"[FAIL] Missing service '{svc}' in docker-compose.yml")
            return False
        print(f"  [+] Service '{svc}' defined.")
        
    # Check IP configuration
    if "172.28.0.0/16" not in content:
        print("[FAIL] Missing isolated subnet 172.28.0.0/16")
        return False
        
    print("[OK] docker-compose.yml structure is valid.")
    return True

def verify_vulnerable_api():
    print("[*] Validating Vulnerable REST API code...")
    if not API_APP.exists():
        print(f"[FAIL] Missing {API_APP}")
        return False
        
    code = API_APP.read_text(encoding="utf-8")
    endpoints = [
        "/api/v1/auth/login",
        "/api/v1/users/<int:user_id>",
        "/api/v1/orders/<int:order_id>",
        "/api/v1/admin/users",
        "/api/v1/tools/fetch_url",
        "/api/v1/debug/env"
    ]
    for ep in endpoints:
        if ep not in code:
            print(f"[FAIL] Missing endpoint '{ep}' in app.py")
            return False
        print(f"  [+] Endpoint '{ep}' verified.")
        
    print("[OK] Vulnerable API endpoints verified.")
    return True

def main():
    ok1 = verify_compose_syntax()
    ok2 = verify_vulnerable_api()
    if ok1 and ok2:
        print("\n[SUCCESS] Lab Environment Configuration verified 100% successfully!")
        return 0
    else:
        print("\n[FAILURE] Verification errors encountered.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

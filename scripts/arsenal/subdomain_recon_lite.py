#!/usr/bin/env python3
"""
Subdomain Recon Lite - Passive OSINT Domain Enumerator
Part of Cybersecurity Arsenal Scripts
Queries Certificate Transparency (CT) logs via crt.sh without requiring API keys or pip packages.
Resolves detected subdomains to IPv4 addresses using Python standard library socket.
"""

import sys
import json
import socket
import urllib.request
import urllib.parse
import argparse
from typing import Set, Tuple, List

def query_crt_sh(domain: str, timeout: int = 15) -> Set[str]:
    """Query crt.sh public JSON API for certificate transparency records."""
    url = f"https://crt.sh/?q=%25.{urllib.parse.quote(domain)}&output=json"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OSINT-Recon-Tool/1.0"}
    )
    subdomains = set()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status == 200:
                data = json.loads(resp.read().decode("utf-8", errors="ignore"))
                for entry in data:
                    name_value = entry.get("name_value", "")
                    # Each name_value can contain multiple domains separated by newlines
                    for sub in name_value.split("\n"):
                        sub = sub.strip().lower()
                        if sub.endswith(domain) and not sub.startswith("*"):
                            subdomains.add(sub)
    except Exception as e:
        print(f"[!] Warning: Query to crt.sh timed out or failed ({e}). Returning local results.")
    return subdomains

def resolve_domain(subdomain: str) -> str:
    """Resolve subdomain to IPv4 address."""
    try:
        return socket.gethostbyname(subdomain)
    except Exception:
        return "(Unresolved / Internal)"

def main():
    parser = argparse.ArgumentParser(description="Subdomain Recon Lite - OSINT CT Log Enumerator")
    parser.add_argument("domain", help="Target apex domain (e.g. example.com)")
    parser.add_argument("--resolve", action="store_true", help="Resolve detected subdomains to IP addresses")
    parser.add_argument("--output", help="Save unique subdomains to file")
    parser.add_argument("--demo", action="store_true", help="Run offline demonstration with sample subdomains")
    
    args = parser.parse_args()
    
    print("=" * 65)
    print(f"      SUBDOMAIN RECON LITE (TARGET: {args.domain})")
    print("=" * 65)
    
    if args.demo:
        subdomains = {
            f"vpn.{args.domain}",
            f"mail.{args.domain}",
            f"portal.{args.domain}",
            f"api.{args.domain}",
            f"dev.{args.domain}",
            f"autodiscover.{args.domain}"
        }
        print("[*] Running in Offline Demonstration Mode.")
    else:
        print(f"[*] Querying Certificate Transparency logs for '{args.domain}'...")
        subdomains = query_crt_sh(args.domain)
        if not subdomains:
            # Fallback to demo mode if network is isolated
            print("[-] No records returned from public CT log (or network offline). Using demonstration sample.")
            subdomains = {f"vpn.{args.domain}", f"mail.{args.domain}", f"portal.{args.domain}", f"api.{args.domain}"}
            
    sorted_subs = sorted(list(subdomains))
    print(f"\n[+] Total Unique Subdomains Discovered: {len(sorted_subs)}\n")
    print(f"{'STT':<4} {'Subdomain':<35} {'Resolved IP':<20}")
    print("-" * 65)
    
    results_to_save = []
    for idx, sub in enumerate(sorted_subs, 1):
        ip = resolve_domain(sub) if args.resolve else "-"
        print(f"{idx:<4} {sub:<35} {ip:<20}")
        results_to_save.append(f"{sub} {ip}" if args.resolve else sub)
        
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("\n".join(results_to_save) + "\n")
        print(f"\n[+] Saved {len(sorted_subs)} records to {args.output}")
        
    print("=" * 65)

if __name__ == "__main__":
    main()

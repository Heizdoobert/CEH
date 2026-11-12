#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEC Lab Environment & CTF Flag Verification Engine
Author: CEH v12 & Red Team Operations Curriculum Contributors
Version: 1.0.0
Description:
    CLI tool to test Docker Lab connectivity and verify solved CTF challenge flags
    via cryptographic hash verification without exposing plaintext flags.
"""

import argparse
import hashlib
import json
import os
import socket
import sys
import time
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
PROGRESS_FILE = SCRIPT_DIR / ".lab_progress.json"

# Challenge Metadata & Secure SHA-256 Hashes
CHALLENGES = {
    "CTF-01": {
        "id": 1,
        "name": "Bẻ khóa Database Hash qua SQLi (DVWA)",
        "target": "DVWA (Port 8080)",
        "points": 100,
        "hash": "0b5279a82391394fd44a1e6207b7dd381cc4147781d3c609168e7b40e27850d8",
        "category": "Web Security / SQL Injection"
    },
    "CTF-02": {
        "id": 2,
        "name": "Khai thác BOLA Đánh cắp Token Admin",
        "target": "Vulnerable REST API (Port 5000)",
        "points": 150,
        "hash": "9c087e60d4f04041fc5f87fcec7d5fe6098601d6157c13811d9ec136cd2ce71c",
        "category": "API Security / BOLA"
    },
    "CTF-03": {
        "id": 3,
        "name": "Leo thang Đặc quyền qua Mass Assignment",
        "target": "Vulnerable REST API (Port 5000)",
        "points": 200,
        "hash": "5d6935e5e963e58649f02faf06df710c33a9945d66ad7824ee341ac7650d17f3",
        "category": "API Security / Mass Assignment"
    },
    "CTF-04": {
        "id": 4,
        "name": "Đột nhập Mạng Nội bộ bằng SSRF",
        "target": "Vulnerable REST API (Port 5000)",
        "points": 250,
        "hash": "4939f5582a328ef80ee4a8badb2540d16da22fc8726ac245ea5e1c3ee95dcb8f",
        "category": "Web & Cloud / SSRF"
    },
    "CTF-05": {
        "id": 5,
        "name": "Khai thác FTP Vô danh & Shell Linux",
        "target": "Metasploitable Node (Port 2121)",
        "points": 300,
        "hash": "b91f63c2cd205c2bbf741943471f7e20ce1b2758d8f702d1221b16515255eccd",
        "category": "Network Exploitation / Privilege Escalation"
    }
}

LAB_TARGETS = [
    {"name": "DVWA (Web)", "host": "127.0.0.1", "port": 8080, "service": "HTTP"},
    {"name": "OWASP Juice Shop", "host": "127.0.0.1", "port": 3000, "service": "HTTP Node.js"},
    {"name": "Vulnerable REST API", "host": "127.0.0.1", "port": 5000, "service": "REST API"},
    {"name": "Metasploitable FTP", "host": "127.0.0.1", "port": 2121, "service": "vsftpd / ProFTPD"},
    {"name": "Metasploitable SSH", "host": "127.0.0.1", "port": 2222, "service": "OpenSSH"},
    {"name": "Metasploitable HTTP", "host": "127.0.0.1", "port": 8088, "service": "Apache HTTP"}
]

TOTAL_POINTS = sum(c["points"] for c in CHALLENGES.values())


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {"solved": {}}
    return {"solved": {}}


def save_progress(data: dict):
    PROGRESS_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def check_port(host: str, port: int, timeout: float = 0.5) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def cmd_health(args):
    print("======================================================================")
    print("               KIỂM TRA KẾT NỐI MÔI TRƯỜNG LAB DOCKER                 ")
    print("======================================================================")
    online_count = 0
    for target in LAB_TARGETS:
        is_up = check_port(target["host"], target["port"])
        status = "[+] ONLINE " if is_up else "[-] OFFLINE"
        print(f" {status:<12} | {target['name']:<25} | Port: {target['port']:<5} | {target['service']}")
        if is_up:
            online_count += 1
            
    print("----------------------------------------------------------------------")
    if online_count == len(LAB_TARGETS):
        print(f"[SUCCESS] Tất cả {online_count}/{len(LAB_TARGETS)} dịch vụ mục tiêu đang hoạt động hoàn hảo!")
    elif online_count > 0:
        print(f"[WARNING] Có {online_count}/{len(LAB_TARGETS)} dịch vụ online. Vui lòng chạy './labs/start_labs.sh'.")
    else:
        print("[!] Lab hiện đang TẮT. Để bắt đầu thực hành, chạy: './labs/start_labs.sh'")


def cmd_submit(args):
    challenge_key = None
    input_id = args.challenge.strip().upper()
    
    # Allow matching by '1', 'CTF-1', 'CTF-01', etc.
    for key, c in CHALLENGES.items():
        if input_id in (str(c["id"]), f"CTF-{c['id']}", f"CTF-0{c['id']}", key):
            challenge_key = key
            break
            
    if not challenge_key:
        print(f"[!] Thử thách không hợp lệ: '{args.challenge}'. Chọn từ 1 đến 5 hoặc CTF-01 đến CTF-05.")
        sys.exit(1)
        
    chal = CHALLENGES[challenge_key]
    user_flag = args.flag.strip()
    flag_hash = hashlib.sha256(user_flag.encode("utf-8")).hexdigest()
    
    print(f"[*] Thẩm định cờ cho: [{challenge_key}] - {chal['name']}")
    
    if flag_hash == chal["hash"]:
        progress = load_progress()
        if "solved" not in progress:
            progress["solved"] = {}
            
        is_new = challenge_key not in progress["solved"]
        progress["solved"][challenge_key] = {
            "name": chal["name"],
            "points": chal["points"],
            "solved_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        save_progress(progress)
        
        print(f"\n🎉 [CHÍNH XÁC!] Chúc mừng! Cờ hợp lệ cho {challenge_key}!")
        print(f"    Điểm cộng: +{chal['points']} pts")
        if not is_new:
            print("    (Lưu ý: Thử thách này bạn đã hoàn thành trước đó)")
        print("\nChạy 'python3 labs/lab_checker.py status' để xem bảng xếp hạng cá nhân.")
    else:
        print("\n❌ [KHÔNG CHÍNH XÁC] Cờ không khớp. Hãy kiểm tra lại kết quả khai thác hoặc format FLAG{...}!")
        sys.exit(1)


def cmd_status(args):
    progress = load_progress()
    solved = progress.get("solved", {})
    earned_points = sum(c["points"] for k, c in solved.items() if k in CHALLENGES)
    pct = (earned_points / TOTAL_POINTS) * 100 if TOTAL_POINTS > 0 else 0
    
    print("======================================================================")
    print("                 BẢNG TIẾN ĐỘ THỬ THÁCH LAB CTF                       ")
    print("======================================================================")
    print(f" Tổng điểm đạt được: {earned_points} / {TOTAL_POINTS} pts ({pct:.1f}%)")
    
    # Progress bar
    bar_width = 30
    filled = int(bar_width * (pct / 100))
    bar = "█" * filled + "░" * (bar_width - filled)
    print(f" Tiến trình: [{bar}]")
    print("----------------------------------------------------------------------")
    print(f" {'Mã':<8} | {'Tên Thử Thách':<36} | {'Điểm':<7} | {'Trạng Thái'}")
    print("----------------------------------------------------------------------")
    
    for key, c in CHALLENGES.items():
        if key in solved:
            st = f"✅ Hoàn thành ({solved[key].get('solved_at', 'N/A')})"
        else:
            st = "⏳ Chưa giải"
        print(f" {key:<8} | {c['name']:<36} | {c['points']:<3} pts | {st}")
        
    print("======================================================================")
    if earned_points == TOTAL_POINTS:
        print("🏆 XUẤT SẮC! BẠN ĐÃ CHINH PHỤC TOÀN BỘ 5 THỬ THÁCH PHÒNG LAB!")
    else:
        print("💡 Xem hướng dẫn giải tại: labs/challenges/01_Hands_On_Lab_Flags_and_Walkthroughs.md")


def cmd_reset(args):
    if PROGRESS_FILE.exists():
        PROGRESS_FILE.unlink()
    print("[+] Đã làm mới tiến độ thực hành CTF thành công.")


def cmd_test(args):
    """Automated test for CI and integrity checking."""
    test_flags = {
        "CTF-01": "FLAG{SQLI_DVWA_UNION_MASTER_2026}",
        "CTF-02": "FLAG{API_BOLA_ADMIN_PROFILE_PWNED}",
        "CTF-03": "FLAG{API_MASS_ASSIGNMENT_ADMIN_TOKEN}",
        "CTF-04": "FLAG{SSRF_INTERNAL_PIVOT_BYPASS}",
        "CTF-05": "FLAG{METASPLOITABLE_ROOT_SHELL_PWNED}"
    }
    
    print("[*] Running automated test for lab_checker...")
    # Verify hash match for all challenges
    for k, flag in test_flags.items():
        assert k in CHALLENGES, f"Missing challenge {k}"
        h = hashlib.sha256(flag.encode("utf-8")).hexdigest()
        assert h == CHALLENGES[k]["hash"], f"Hash mismatch for {k}"
        
    # Test progress save/load
    test_file = SCRIPT_DIR / ".test_progress.json"
    try:
        test_file.write_text(json.dumps({"test": 123}), encoding="utf-8")
        data = json.loads(test_file.read_text(encoding="utf-8"))
        assert data.get("test") == 123
    finally:
        if test_file.exists():
            test_file.unlink()
            
    print(f"[SUCCESS] lab_checker test passed! Verified all {len(CHALLENGES)} challenges.")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="SEC Lab Environment & CTF Flag Verification Engine"
    )
    subparsers = parser.add_subparsers(dest="command", help="Lệnh chức năng")
    
    # Subcommand: health
    subparsers.add_parser("health", help="Kiểm tra trạng thái kết nối các cổng container lab")
    
    # Subcommand: submit
    submit_p = subparsers.add_parser("submit", help="Gửi nộp cờ kiểm tra đáp án")
    submit_p.add_argument("-c", "--challenge", required=True, help="Mã thử thách (1-5 hoặc CTF-01..CTF-05)")
    submit_p.add_argument("-f", "--flag", required=True, help="Chuỗi cờ (ví dụ: FLAG{...})")
    
    # Subcommand: status
    subparsers.add_parser("status", help="Xem bảng điểm và tiến độ cá nhân")
    
    # Subcommand: reset
    subparsers.add_parser("reset", help="Xóa làm mới tiến độ thực hành")
    
    # Subcommand: test
    subparsers.add_parser("test", help="Chạy kiểm thử nội bộ tự động")
    
    args = parser.parse_args()
    
    if args.command == "health":
        cmd_health(args)
    elif args.command == "submit":
        cmd_submit(args)
    elif args.command == "status":
        cmd_status(args)
    elif args.command == "reset":
        cmd_reset(args)
    elif args.command == "test":
        sys.exit(cmd_test(args))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

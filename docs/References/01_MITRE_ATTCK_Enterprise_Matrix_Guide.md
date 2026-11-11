# HƯỚNG DẪN CHIẾN THUẬT MITRE ATT&CK ENTERPRISE DÀNH CHO RED TEAM
## MITRE ATT&CK ENTERPRISE MATRIX: TACTICS, TECHNIQUES & PROCEDURES (TTPs)
**Mã hiệu:** `SEC-REF-MITRE-ATTCK-2026`  
**Phiên bản:** `v15.0 - Enterprise Mapping`  
**Đơn vị biên soạn:** Đội ngũ Chuyên gia Tác chiến An toàn Thông tin (Red Team Operations)  
**Mục đích:** Cung cấp tài liệu tham khảo chính thống, có hệ thống về 14 Tactics trong Ma trận MITRE ATT&CK Enterprise phục vụ hoạt động mô phỏng đối thủ thực tế (Adversary Emulation).

---

## I. TỔNG QUAN 14 CHIẾN THUẬT (14 ENTERPRISE TACTICS)

Ma trận MITRE ATT&CK Enterprise chia vòng đời của một cuộc tấn công mạng có chủ đích thành 14 giai đoạn chiến thuật (Tactics):

```
1. Reconnaissance (Trinh sát)
2. Resource Development (Chuẩn bị Tài nguyên)
3. Initial Access (Thâm nhập Ban đầu)
4. Execution (Thực thi Mã lệnh)
5. Persistence (Duy trì Quyền truy cập)
6. Privilege Escalation (Leo thang Đặc quyền)
7. Defense Evasion (Vượt qua Phòng thủ)
8. Credential Access (Chiếm đoạt Thông tin Xác thực)
9. Discovery (Thám sát Môi trường Nội bộ)
10. Lateral Movement (Di chuyển Ngang)
11. Collection (Thu thập Dữ liệu Mục tiêu)
12. Command and Control (Chỉ huy và Điều khiển - C2)
13. Exfiltration (Trích xuất Dữ liệu ra Ngoài)
14. Impact (Tác động Phá hoại / Mã hóa)
```

---

## II. CHI TIẾT TỪNG CHIẾN THUẬT VÀ KỸ THUẬT RED TEAM TRỌNG TÂM

### 1. RECONNAISSANCE (TA0043 - TRINH SÁT)
*Mục tiêu:* Thu thập thông tin tình báo về mục tiêu (nhân sự, hạ tầng, công nghệ) mà không cần tương tác trực tiếp hoặc chỉ tương tác mức độ tối thiểu.
- **T1595 - Active Scanning:**
  - `T1595.001 (Scanning IP Blocks):` Dò quét dải mạng công khai của tổ chức bằng Masscan/Nmap.
  - `T1595.002 (Vulnerability Scanning):` Dò quét lỗ hổng ứng dụng bằng Nuclei hoặc Nikto.
- **T1593 - Search Open Technical Databases:**
  - Tra cứu Certificate Transparency Logs trên `crt.sh` để tìm Subdomain ẩn.
  - Tra cứu dịch vụ mở cổng trên Shodan / Censys: `org:"Target Corporation" net:203.0.113.0/24`.
- **T1589 - Gather Victim Identity Information:**
  - Lập danh sách định dạng email (ví dụ: `first.last@target.com`) từ LinkedIn và theHarvester.

### 2. RESOURCE DEVELOPMENT (TA0042 - CHUẨN BỊ TÀI NGUYÊN)
*Mục tiêu:* Mua sắm, thiết lập hoặc tạo mới các tài nguyên phục vụ chiến dịch (tên miền, chứng chỉ số, máy chủ C2, tài khoản mồi).
- **T1583 - Acquire Infrastructure:** Mua tên miền tương đồng (Typosquatting/Combosquatting) như `targeet.com` để lừa đảo.
- **T1587 - Develop Capabilities:** Viết mã độc tùy biến (Custom Payloads), sinh mã bọc (Shellcode Crypter/Packer) bằng C#/Go.
- **T1588 - Obtain Capabilities:** Thu thập công cụ mã nguồn mở từ GitHub (Mimikatz, Rubeus, SharpHound, Chisel).

### 3. INITIAL ACCESS (TA0001 - THÂM NHẬP BAN ĐẦU)
*Mục tiêu:* Đặt chân lần đầu tiên vào mạng nội bộ của tổ chức mục tiêu.
- **T1566 - Phishing:**
  - `T1566.001 (Spearphishing Attachment):` Gửi email đính kèm tệp văn bản độc hại (Macro VBA, LNK file, ISO image).
  - `T1566.002 (Spearphishing Link):` Gửi liên kết dẫn đến trang đăng nhập mồi nhử mạo danh Microsoft 365 có cơ chế vượt qua MFA (Evilginx2).
- **T1190 - Exploit Public-Facing Application:**
  - Khai thác lỗ hổng Remote Code Execution (RCE) trên máy chủ Web, VPN Gateway hoặc Exchange Server (ví dụ: ProxyShell, Citrix Bleed).
- **T1078 - Valid Accounts:**
  - Sử dụng tài khoản hợp pháp thu thập được từ các vụ rò rỉ dữ liệu (Credential Stuffing).

### 4. EXECUTION (TA0002 - THỰC THI MÃ LỆNH)
*Mục tiêu:* Chạy mã độc trên hệ thống nạn nhân.
- **T1059 - Command and Scripting Interpreter:**
  - `T1059.001 (PowerShell):` Thực thi script trong bộ nhớ: `powershell -nop -w hidden -enc <base64_payload>`.
  - `T1059.003 (Windows Command Shell):` Thực thi `cmd.exe`.
  - `T1059.005 (Visual Basic):` Macro độc hại trong file Office.
- **T1204 - User Execution:** Lừa người dùng kích hoạt tệp tin giả mạo.

### 5. PERSISTENCE (TA0003 - DUY TRÌ QUYỀN TRUY CẬP)
*Mục tiêu:* Giữ vững quyền kiểm soát ngay cả khi máy tính khởi động lại hoặc tài khoản bị đổi mật khẩu.
- **T1547 - Boot or Logon Autostart Execution:**
  - `T1547.001 (Registry Run Keys):` Thêm đường dẫn mã độc vào `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.
- **T1053 - Scheduled Task/Job:**
  - Tạo tác vụ định kỳ qua lệnh `schtasks /create /tn "SecurityUpdate" /tr "C:\payload.exe" /sc onlogon`.
- **T1543 - Create or Modify System Process:** Tạo Service hệ thống trên Windows bằng lệnh `sc create`.

### 6. PRIVILEGE ESCALATION (TA0004 - LEO THANG ĐẶC QUYỀN)
*Mục tiêu:* Nâng cấp quyền hạn từ User thường lên Local Administrator, SYSTEM (Windows) hoặc root (Linux).
- **T1068 - Exploitation for Privilege Escalation:** Khai thác lỗ hổng nhân Kernel (Dirty COW, PwnKit, PrintNightmare).
- **T1548 - Abuse Elevation Control Mechanism:**
  - `T1548.002 (Bypass UAC):` Vượt qua User Account Control qua Mock Directories hoặc DLL Hijacking.
- **T1574 - Hijack Execution Flow:**
  - DLL Search Order Hijacking: Đặt DLL độc hại vào thư mục ứng dụng ưu tiên tìm kiếm.

### 7. DEFENSE EVASION (TA0005 - VƯỢT QUA PHÒNG THỦ)
*Mục tiêu:* Tránh bị phát hiện bởi Antivirus, EDR, SIEM, SOC team trong suốt chiến dịch.
- **T1562 - Impair Defenses:**
  - `T1562.001 (Disable or Modify Tools):` Vô hiệu hóa Windows Defender qua lệnh PowerShell `Set-MpPreference -DisableRealtimeMonitoring $true`.
  - Vô hiệu hóa Event Tracing for Windows (ETW Patching) để chặn ghi log.
  - Vô hiệu hóa Antimalware Scan Interface (AMSI Patching) để PowerShell thực thi tự do.
- **T1027 - Obfuscated/Encrypted Files or Information:** Mã hóa chuỗi, đóng gói nhị phân, chia nhỏ payload.
- **T1055 - Process Injection:** Tiêm Shellcode vào tiến trình sạch hợp pháp (Process Hollowing, APC Queue Injection vào `explorer.exe` hoặc `svchost.exe`).
- **T1218 - System Binary Proxy Execution (LOLBAS):** Sử dụng các file hệ thống hợp pháp (`certutil.exe`, `mshta.exe`, `rundll32.exe`) để chạy mã độc.

### 8. CREDENTIAL ACCESS (TA0006 - CHIẾM ĐOẠT THÔNG TIN XÁC THỰC)
*Mục tiêu:* Thu thập tài khoản, mật khẩu, hash, vé xác thực Kerberos trên máy nạn nhân.
- **T1003 - OS Credential Dumping:**
  - `T1003.001 (LSASS Memory):` Đọc bộ nhớ tiến trình `lsass.exe` bằng Mimikatz để lấy hash NTLM và plaintext password.
  - `T1003.002 (Security Account Manager):` Dump SAM hive.
  - `T1003.006 (DCSync):` Gửi yêu cầu DRSGetNCChanges đến Domain Controller để lấy trọn bộ cơ sở dữ liệu `NTDS.dit`.
- **T1558 - Steal or Forge Kerberos Tickets:**
  - `T1558.003 (Kerberoasting):` Yêu cầu vé TGS và bẻ khóa offline.
  - `T1558.004 (AS-REP Roasting):` Bắt AS-REP của user không bật pre-authentication.
  - `T1558.001 (Golden Ticket):` Giả mạo vé TGT tối cao bằng khóa bí mật của tài khoản `krbtgt`.
- **T1557 - Adversary-in-the-Middle:**
  - `T1557.001 (LLMNR/NBT-NS Poisoning):` Dùng công cụ Responder nghe lén và bắt NTLMv2 hash trên mạng nội bộ.

### 9. DISCOVERY (TA0007 - THÁM SÁT MÔI TRƯỜNG NỘI BỘ)
*Mục tiêu:* Tìm hiểu về môi trường mạng, máy chủ lân cận, chính sách và cơ cấu Active Directory.
- **T1087 - Account Discovery:** `net user /domain`, `Get-ADUser`.
- **T1482 - Domain Trust Discovery:** `nltest /domain_trusts`.
- **T1018 - Remote System Discovery:** Khảo sát các máy tính khác trong miền bằng `net view` hoặc `AdFind`.
- **T1069 - Permission Groups Discovery:** Thu thập danh sách thành viên nhóm Domain Admins: `net group "Domain Admins" /domain`.
- **T1082 - System Information Discovery:** Thu thập phiên bản OS, Hotfix cài đặt qua lệnh `systeminfo`.

### 10. LATERAL MOVEMENT (TA0008 - DI CHUYỂN NGANG)
*Mục tiêu:* Mở rộng phạm vi kiểm soát từ máy ban đầu sang các máy chủ quan trọng khác trong mạng nội bộ.
- **T1021 - Remote Services:**
  - `T1021.002 (SMB/Windows Admin Shares):` Kết nối đến `C$` share và chạy lệnh từ xa qua `psexec` hoặc `wmiexec`.
  - `T1021.006 (Windows Remote Management - WinRM):` Điều khiển máy từ xa qua PowerShell Remoting (`Enter-PSSession`, `Evil-WinRM`).
- **T1550 - Use Alternate Authentication Material:**
  - `T1550.002 (Pass the Hash):` Dùng NTLM Hash để đăng nhập không cần giải mã.
  - `T1550.003 (Pass the Ticket):` Nạp vé Kerberos TGT/TGS vào bộ nhớ (`klist`, `Rubeus ptt`).

### 11. COLLECTION (TA0009 - THU THẬP DỮ LIỆU)
*Mục tiêu:* Thu thập các tài liệu giá trị cao, mã nguồn, cơ sở dữ liệu, email của mục tiêu.
- **T1005 - Data from Local System:** Tìm kiếm tệp tin chứa từ khóa "password", "confidential", "budget":
  `Get-ChildItem -Path C:\ -Include *.docx,*.xlsx,*.pdf,*.kdbx -Recurse -ErrorAction SilentlyContinue`.
- **T1114 - Email Collection:** Truy cập hòm thư Exchange / Outlook của lãnh đạo cấp cao.
- **T1560 - Archive Collected Data:** Nén dữ liệu thành file ZIP/7z có mật khẩu để chuẩn bị gửi ra ngoài.

### 12. COMMAND AND CONTROL (TA0011 - CHỈ HUY VÀ ĐIỀU KHIỂN)
*Mục tiêu:* Duy trì kênh liên lạc bảo mật giữa máy tấn công và các Agent cắm chốt bên trong mạng.
- **T1071 - Application Layer Protocol:**
  - `T1071.001 (Web Protocols):` Giao tiếp qua HTTP/HTTPS ngụy trang giống lưu lượng duyệt web thông thường.
  - `T1071.004 (DNS):` DNS Tunneling (chèn dữ liệu vào truy vấn TXT/A).
- **T1573 - Encrypted Channel:** Sử dụng mã hóa AES hoặc TLS tùy chỉnh để mã hóa kênh điều khiển C2.
- **T1090 - Proxy:** Chuyển tiếp kết nối qua mạng lưới redirector để che giấu IP thật của máy chủ C2 chính.

### 13. EXFILTRATION (TA0010 - TRÍCH XUẤT DỮ LIỆU RA NGOÀI)
*Mục tiêu:* Đưa dữ liệu nhạy cảm ra khỏi mạng của tổ chức về máy chủ của Red Team an toàn.
- **T1048 - Exfiltration Over Alternative Protocol:**
  - Gửi dữ liệu qua kênh DNS hoặc ICMP.
- **T1567 - Exfiltration Over Web Service:**
  - Tải dữ liệu lên dịch vụ đám mây hợp pháp (Google Drive, Dropbox, Mega, AWS S3) để tránh bị tường lửa chặn.
- **T1029 - Scheduled Transfer:** Gửi dữ liệu từng phần nhỏ vào ban đêm để tránh kích hoạt cảnh báo đột biến lưu lượng mạng.

### 14. IMPACT (TA0040 - TÁC ĐỘNG VÀ CHỨNG MINH RỦI RO)
*Mục tiêu:* Trong diễn tập Red Team, đây là giai đoạn chứng minh khả năng kiểm soát tuyệt đối để hoàn thành mục tiêu (ví dụ: tạo file chứng cứ Proof of Concept, chứng minh quyền ghi vào cơ sở dữ liệu tài chính mà không phá hoại hệ thống).
- **T1486 - Data Encrypted for Impact:** Mô phỏng kịch bản Ransomware (mã hóa một thư mục thử nghiệm).
- **T1490 - Inhibit System Recovery:** Xóa bản sao lưu Volume Shadow Copies (`vssadmin delete shadows /all /quiet`).

---

## III. BẢNG TỔNG HỢP CÔNG CỤ THEO GIAI ĐOẠN TÁC CHIẾN

| Giai đoạn | Bộ công cụ khuyến nghị |
|---|---|
| **Recon & OSINT** | Amass, Sublist3r, theHarvester, Shodan, Maltego, Recon-ng |
| **Initial Access & Phishing** | GoPhish, Evilginx2, Burp Suite Pro, Metasploit, MacroPack |
| **Local Privilege Escalation** | WinPEAS, LinPEAS, SweetPotato, BeRoot, JuicyPotatoNG |
| **Active Directory Attacks** | BloodHound, SharpHound, Impacket, Rubeus, Mimikatz, Certipy |
| **Lateral Movement & Pivoting** | Ligolo-ng, Chisel, Proxychains, CrackMapExec, Evil-WinRM |
| **Command & Control (C2)** | Sliver C2, Mythic, Havoc, Cobalt Strike |
| **Defense & EDR Evasion** | Donut, Inceptor, Flang, Custom C# Loaders, Syswhispers3 |

---
*Tài liệu này được ánh xạ trực tiếp sang các bài giảng lý thuyết trong thư mục `docs/Lectures/` và được xuất ra PDF/DOCX phục vụ đào tạo tác chiến.*

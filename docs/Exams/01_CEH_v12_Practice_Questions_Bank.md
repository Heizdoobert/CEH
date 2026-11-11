# NGÂN HÀNG 125 CÂU HỎI THI THỬ CHUẨN QUỐC TẾ CEH v12 (PRACTICE EXAM BANK)

> **Tài liệu kiểm tra & ôn luyện chứng chỉ Certified Ethical Hacker (CEH v12).**
> Cấu trúc: 125 câu hỏi trắc nghiệm chuẩn EC-Council (Thời gian: 4 giờ, điểm đạt: 70%).
> Bao quát toàn bộ 20 Modules của CEH v12 và ánh xạ tới các bài giảng trong [02_Master_Lecture_and_Lab_Plan.md](file:///mnt/second_drive/DOCS/SEC/docs/Lectures/02_Master_Lecture_and_Lab_Plan.md).
>
> Công cụ luyện thi tương tác: Chạy lệnh `/usr/bin/python3.11 exam_simulator.py quiz --mode ceh --count 20`.

---

## PHẦN 1: MODULE 01 - 10 (CÂU 1 ĐẾN CÂU 65)

### MODULE 01: INTRODUCTION TO ETHICAL HACKING & LEGAL FRAMEWORKS

#### Câu 1 [Module 01]
Trong mô hình bảo mật thông tin, bộ ba CIA bao gồm tính Bảo mật (Confidentiality), Toàn vẹn (Integrity) và Sẵn sàng (Availability). Kỹ thuật tấn công nào sau đây chủ yếu phá vỡ tính **Integrity**?
- A. Tấn công SYN Flood làm sập dịch vụ máy chủ web
- B. Nghe lén lưu lượng HTTP bằng Wireshark không mã hóa
- C. Chỉnh sửa trái phép hồ sơ chuyển tiền trong cơ sở dữ liệu ngân hàng
- D. Tấn công DDoS bằng botnet Mirai
- **Đáp án:** C
- **Giải thích:** Tính toàn vẹn (Integrity) bảo đảm dữ liệu không bị thay đổi, giả mạo bởi bên thứ ba không có thẩm quyền. Việc chỉnh sửa bản ghi tài chính là vi phạm trực tiếp tính Integrity. A và D vi phạm Availability; B vi phạm Confidentiality.
- **Liên kết:** [Module 01 - Introduction.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2001%20Introduction%20to%20Ethical%20Hacking.md)

#### Câu 2 [Module 01]
Sự khác biệt căn bản nhất giữa **Black Box Testing** và **White Box Testing** trong kiểm thử xâm nhập là gì?
- A. White Box tester không được sử dụng các công cụ tự động
- B. Black Box tester không được cung cấp bất kỳ thông tin kiến trúc hay mã nguồn nào trước khi kiểm thử
- C. Black Box luôn đòi hỏi phải có quyền truy cập root vào hệ thống mục tiêu
- D. White Box chỉ áp dụng cho kiểm thử vật lý (Physical security)
- **Đáp án:** B
- **Giải thích:** Trong Black Box testing, chuyên gia đánh giá đóng vai trò như kẻ tấn công ngoài internet, không được cấp sơ đồ mạng hay tài khoản trước. White Box được cấp đầy đủ mã nguồn, cấu hình và sơ đồ hệ thống.
- **Liên kết:** [06_NIST_SP_800-115_Technical_Guide.md](file:///mnt/second_drive/DOCS/SEC/docs/References/06_NIST_SP_800-115_Technical_Guide.md)

#### Câu 3 [Module 01]
Luật pháp Hoa Kỳ nào quy định việc truy cập trái phép vào các hệ thống máy tính được bảo vệ (protected computers) là hành vi phạm tội hình sự?
- A. HIPAA (Health Insurance Portability and Accountability Act)
- B. CFAA (Computer Fraud and Abuse Act - 18 U.S.C. § 1030)
- C. SOX (Sarbanes-Oxley Act)
- D. GDPR (General Data Protection Regulation)
- **Đáp án:** B
- **Giải thích:** CFAA là đạo luật nền tảng tại Mỹ truy tố các hành vi đột nhập máy tính trái phép, cài mã độc và tống tiền mạng.
- **Liên kết:** [Module 01 - Introduction.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2001%20Introduction%20to%20Ethical%20Hacking.md)

#### Câu 4 [Module 01]
Tài liệu pháp lý nào bắt buộc phải được ký kết giữa Chuyên gia kiểm thử xâm nhập và Ban lãnh đạo tổ chức khách hàng TRƯỚC KHI thực hiện bất kỳ hành vi rà quét hay khai thác nào?
- A. CVSS Vector Calculator Sheet
- B. Rules of Engagement (RoE) và Non-Disclosure Agreement (NDA)
- C. Báo cáo kiểm toán ISO 27001
- D. Giấy phép mã nguồn mở GPLv3
- **Đáp án:** B
- **Giải thích:** RoE quy định phạm vi (Scope), thời gian, các hệ thống được phép/không được phép tấn công và liên hệ khẩn cấp; NDA đảm bảo tính bảo mật của dữ liệu khách hàng.
- **Liên kết:** [SANS_PenTest_Rules_of_Engagement_Worksheet.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SANS_PenTest_Rules_of_Engagement_Worksheet.pdf)

#### Câu 5 [Module 01]
Hacker tấn công một tổ chức nhưng không nhằm mục đích vụ lợi cá nhân mà nhằm phơi bày các vi phạm chính trị, bảo vệ môi trường hoặc quyền tự do ngôn luận được xếp vào nhóm nào?
- A. Script Kiddie
- B. Hacktivist
- C. State-sponsored Actor
- D. Black Hat
- **Đáp án:** B
- **Giải thích:** Hacktivist (kết hợp Hacker và Activist) thực hiện tấn công vì động cơ chính trị, xã hội hoặc lý tưởng.
- **Liên kết:** [Module 01 - Introduction.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2001%20Introduction%20to%20Ethical%20Hacking.md)

---

### MODULE 02: FOOTPRINTING AND RECONNAISSANCE

#### Câu 6 [Module 02]
Cú pháp Google Dork nào sau đây dùng để tìm kiếm các tệp cấu hình chứa chuỗi kết nối cơ sở dữ liệu trên các máy chủ web có bật tính năng index?
- A. `site:target.com filetype:pdf "annual report"`
- B. `intitle:"index of" "wp-config.php" "DB_PASSWORD"`
- C. `link:target.com inurl:admin`
- D. `cache:target.com`
- **Đáp án:** B
- **Giải thích:** Cú pháp `intitle:"index of"` tìm thư mục bị Directory Listing, kết hợp chuỗi `wp-config.php` và `DB_PASSWORD` cho phép tìm thấy tệp cấu hình WordPress chứa mật khẩu database cleartext.
- **Liên kết:** [Module 02 - FootPrinting.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2002%20Footprinting%20and%20Reconnaissance.md)

#### Câu 7 [Module 02]
Khi thực hiện truy vấn DNS để thu thập toàn bộ các bản ghi trong một vùng (DNS Zone Transfer), hacker sử dụng câu lệnh nào trong công cụ `dig`?
- A. `dig axfr @ns1.target.com target.com`
- B. `dig mx target.com +short`
- C. `dig ptr 192.168.1.1`
- D. `dig any target.com +trace`
- **Đáp án:** A
- **Giải thích:** Bản ghi loại `axfr` (Asynchronous Transfer Full Range) gửi yêu cầu sao chép toàn bộ cơ sở dữ liệu DNS Zone từ DNS server mục tiêu. Nếu DNS server bị cấu hình sai mở AXFR, toàn bộ máy chủ nội bộ sẽ bị lộ.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 8 [Module 02]
Bản ghi DNS nào chỉ định máy chủ chịu trách nhiệm tiếp nhận và chuyển tiếp thư điện tử (email) của một tên miền?
- A. SOA (Start of Authority)
- B. CNAME (Canonical Name)
- C. MX (Mail Exchange)
- D. TXT (Text Record)
- **Đáp án:** C
- **Giải thích:** Bản ghi MX (Mail Exchange) ánh xạ tên miền tới địa chỉ máy chủ email của tổ chức.
- **Liên kết:** [01_Computer_Networking/02_Application_Layer.md](file:///mnt/second_drive/DOCS/SEC/01_Computer_Networking/02_Application_Layer.md)

#### Câu 9 [Module 02]
Công cụ OSINT nào chuyên tìm kiếm các thiết bị phần cứng, camera IP, máy chủ ICS/SCADA và dịch vụ kết nối trực tiếp với Internet công cộng?
- A. Maltego
- B. Shodan
- C. Wireshark
- D. Nikto
- **Đáp án:** B
- **Giải thích:** Shodan là công cụ tìm kiếm thiết bị kết nối mạng (Search Engine for the Internet of Things) thu thập banner của hàng tỷ thiết bị trên toàn cầu.
- **Liên kết:** [Module 02 - FootPrinting.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2002%20Footprinting%20and%20Reconnaissance.md)

#### Câu 10 [Module 02]
Trong quá trình Footprinting qua mạng xã hội, hacker sử dụng kỹ thuật thu thập siêu dữ liệu (metadata) của ảnh (tọa độ GPS, loại thiết bị camera) được lưu trữ theo định dạng nào?
- A. EXIF (Exchangeable Image File Format)
- B. ASCII
- C. Base64
- D. MIME
- **Đáp án:** A
- **Giải thích:** Metadata EXIF nhúng trong ảnh chụp kỹ thuật số chứa ngày giờ chụp, model camera và kinh độ/vĩ độ GPS chính xác.
- **Liên kết:** [Module 02 - FootPrinting.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2002%20Footprinting%20and%20Reconnaissance.md)

#### Câu 11 [Module 02]
Kỹ thuật thu thập thông tin nào sau đây được coi là **Passive Footprinting** (Thu thập thông tin thụ động)?
- A. Chạy quét cổng `nmap -sS target.com`
- B. Kiểm tra hồ sơ Whois và chứng chỉ số SSL qua crt.sh
- C. Thực hiện leo thang thư mục HTTP bằng Gobuster
- D. Gửi email thăm dò tới nhân viên mục tiêu
- **Đáp án:** B
- **Giải thích:** Passive reconnaissance không gửi bất kỳ gói tin trực tiếp nào tới hạ tầng của mục tiêu mà chỉ tra cứu dữ liệu từ bên thứ ba (Whois registry, Certificate Transparency logs).
- **Liên kết:** [Module 02 - FootPrinting.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2002%20Footprinting%20and%20Reconnaissance.md)

#### Câu 12 [Module 02]
Trang web lưu trữ phiên bản lịch sử của hàng tỷ trang web trong quá khứ thường được hacker dùng để tìm kiếm các tệp bí mật từng vô tình bị lộ là:
- A. Pastebin
- B. Wayback Machine (archive.org)
- C. Exploit-DB
- D. GitHub Gist
- **Đáp án:** B
- **Giải thích:** Wayback Machine chụp và lưu trữ snapshot các trang web theo dòng thời gian, giúp phục hồi các tài liệu nhạy cảm đã bị gỡ bỏ ở phiên bản hiện tại.
- **Liên kết:** [Module 02 - FootPrinting.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2002%20Footprinting%20and%20Reconnaissance.md)

---

### MODULE 03: SCANNING NETWORKS

#### Câu 13 [Module 03]
Lệnh quét Nmap nào sau đây gửi cờ `SYN` và không hoàn tất bắt tay 3 bước TCP (Half-Open Scan)?
- A. `nmap -sT 192.168.1.1`
- B. `nmap -sS 192.168.1.1`
- C. `nmap -sU 192.168.1.1`
- D. `nmap -sA 192.168.1.1`
- **Đáp án:** B
- **Giải thích:** `-sS` thực hiện TCP SYN Scan (Stealth scan). Khi máy chủ phản hồi `SYN/ACK`, Nmap lập tức gửi gói `RST` để hủy kết nối trước khi phiên hoàn tất, giúp hạn chế ghi nhận log kết nối tầng ứng dụng.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 14 [Module 03]
Trong kỹ thuật quét **TCP Xmas Scan** (`nmap -sX`), những cờ TCP nào được bật sáng đồng thời trên header?
- A. SYN, ACK, FIN
- B. FIN, URG, PSH
- C. RST, SYN, ACK
- D. URG, ACK, RST
- **Đáp án:** B
- **Giải thích:** Xmas Scan bật các cờ FIN, URG và PSH (ví von như cây thông noel thắp sáng). Theo chuẩn RFC 793, cổng đóng sẽ phản hồi gói RST; cổng mở sẽ bỏ qua gói tin mà không phản hồi.
- **Liên kết:** [01_Computer_Networking/03_Transport_Layer.md](file:///mnt/second_drive/DOCS/SEC/01_Computer_Networking/03_Transport_Layer.md)

#### Câu 15 [Module 03]
Kỹ thuật quét Nmap nào sau đây được thiết kế chuyên biệt để phát hiện quy tắc lọc của Firewall (Stateful vs Stateless) thay vì xác định cổng mở hay đóng?
- A. `nmap -sA 192.168.1.1` (TCP ACK Scan)
- B. `nmap -sN 192.168.1.1` (TCP Null Scan)
- C. `nmap -sU 192.168.1.1` (UDP Scan)
- D. `nmap -sF 192.168.1.1` (TCP FIN Scan)
- **Đáp án:** A
- **Giải thích:** ACK Scan gửi gói có cờ ACK. Nếu cổng không bị chặn bởi firewall (unfiltered), đích phản hồi RST; nếu không nhận phản hồi hoặc nhận ICMP unreachable, cổng được phân loại là filtered.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 16 [Module 03]
Khi thực hiện quét UDP (`nmap -sU`), nếu một cổng đóng nhận được gói UDP, hệ điều hành đích thường phản hồi gói ICMP nào?
- A. ICMP Type 8 (Echo Request)
- B. ICMP Type 3 Code 3 (Destination Unreachable - Port Unreachable)
- C. ICMP Type 0 (Echo Reply)
- D. ICMP Type 11 (Time Exceeded)
- **Đáp án:** B
- **Giải thích:** Theo RFC 792, khi một gói UDP gửi đến một cổng không có dịch vụ lắng nghe, máy chủ phải phản hồi ICMP Type 3 Code 3 (Port Unreachable).
- **Liên kết:** [SANS_TCPIP_Packet_CheatSheet_2021.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SANS_TCPIP_Packet_CheatSheet_2021.pdf)

#### Câu 17 [Module 03]
Kỹ thuật **Idle Scan** (`nmap -sI <zombie_ip> <target>`) khai thác trường nào trong header IP của một máy tính "Zombie" để suy luận trạng thái cổng của mục tiêu mà không để lộ IP thật?
- A. TTL (Time to Live)
- B. IP ID (Identification Field)
- C. Checksum
- D. TOS (Type of Service)
- **Đáp án:** B
- **Giải thích:** Idle Scan đo lường mức tăng của số tuần tự IP ID trên máy Zombie không hoạt động để xác định xem mục tiêu có gửi gói phản hồi RST/ACK tới Zombie hay không.
- **Liên kết:** [Module 03 - Network Scanning.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2003%20Scanning%20Networks.md)

#### Câu 18 [Module 03]
Tùy chọn Nmap nào bật tính năng dò tìm phiên bản hệ điều hành (OS Detection), phiên bản dịch vụ (Service Version), chạy script mặc định và traceroute đồng thời?
- A. `nmap -A`
- B. `nmap -p-`
- C. `nmap -sT`
- D. `nmap -Pn`
- **Đáp án:** A
- **Giải thích:** Cờ `-A` kích hoạt chế độ "Aggressive scan", bao gồm: OS detection (`-O`), version detection (`-sV`), script scanning (`-sC`) và traceroute.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 19 [Module 03]
Lệnh Nmap nào dùng để quét toàn bộ 65,535 cổng TCP trên máy mục tiêu?
- A. `nmap -p 1-65535 target` hoặc `nmap -p- target`
- B. `nmap --top-ports 65535 target`
- C. `nmap -F target`
- D. `nmap -p all target`
- **Đáp án:** A
- **Giải thích:** Tham số `-p-` là cú pháp viết tắt của dải cổng từ 1 đến 65535.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 20 [Module 03]
Tại sao pentester cần sử dụng tham số `-Pn` khi quét một máy chủ mục tiêu nằm sau tường lửa chặn gói ICMP Echo?
- A. Để mã hóa lưu lượng quét qua TLS
- B. Để bỏ qua giai đoạn Ping Discovery và coi như host luôn sống (Host is up)
- C. Để tăng tốc độ quét lên gấp 10 lần
- D. Để giả mạo địa chỉ MAC nguồn
- **Đáp án:** B
- **Giải thích:** Mặc định Nmap gửi ping ICMP và TCP SYN tới port 80/443 để kiểm tra host có hoạt động không trước khi quét cổng. Nếu tường lửa chặn ping, Nmap sẽ kết luận host down. Cờ `-Pn` ép Nmap quét trực tiếp mà không cần ping.
- **Liên kết:** [Module 03 - Network Scanning.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2003%20Scanning%20Networks.md)

#### Câu 21 [Module 03]
Công cụ quét cổng cực nhanh dựa trên kiến trúc bất đồng bộ (asynchronous transmission) có khả năng quét toàn bộ không gian mạng Internet IPv4 trong dưới 6 phút là:
- A. Nmap
- B. Masscan
- C. Hping3
- D. Angry IP Scanner
- **Đáp án:** B
- **Giải thích:** Masscan truyền các gói tin SYN dạng async độc lập với stack mạng OS, cho phép đẩy tốc độ truyền lên tới 25 triệu gói/giây.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 22 [Module 03]
Kỹ thuật nào sau đây được Nmap sử dụng để phát hiện dấu vết hệ điều hành (OS Fingerprinting)?
- A. So sánh các thuộc tính của TCP Window Size, IP TTL và thứ tự các cờ TCP Options với cơ sở dữ liệu `nmap-os-db`
- B. Đọc tệp `/etc/os-release` qua giao thức FTP ẩn danh
- C. Sử dụng giao thức SNMP để đọc OID hệ thống
- D. Gửi truy vấn HTTP HEAD và đọc trường `Server`
- **Đáp án:** A
- **Giải thích:** Nmap gửi một chuỗi các gói tin probe chuẩn và bất thường (gói SYN kích thước window khác nhau, gói FIN/PSH không hợp lệ) rồi đối chiếu phản hồi TTL, Window size và Options với cơ sở dữ liệu chữ ký hệ điều hành.
- **Liên kết:** [Module 03 - Network Scanning.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2003%20Scanning%20Networks.md)

---

### MODULE 04: ENUMERATION

#### Câu 23 [Module 04]
Giao thức SNMP (Simple Network Management Protocol) phiên bản nào sau đây truyền chuỗi cộng đồng (Community String) dưới dạng văn bản rõ (cleartext) không mã hóa?
- A. Chỉ SNMPv1
- B. Chỉ SNMPv2c
- C. Cả SNMPv1 và SNMPv2c
- D. Chỉ SNMPv3
- **Đáp án:** C
- **Giải thích:** SNMPv1 và SNMPv2c đều truyền Community String (như `public` hoặc `private`) ở dạng plain-text qua cổng UDP 161. Chỉ có SNMPv3 mới hỗ trợ mã hóa và xác thực người dùng (AuthPriv).
- **Liên kết:** [Module 04 - Enumeration.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2004%20Enumeration.md)

#### Câu 24 [Module 04]
Cây phân cấp thông tin quản lý trong giao thức SNMP được định danh thông qua cấu trúc dữ liệu nào?
- A. Active Directory Schema
- B. MIB (Management Information Base) và OID (Object Identifier)
- C. JSON Web Tokens
- D. SAML Assertions
- **Đáp án:** B
- **Giải thích:** MIB là cơ sở dữ liệu phân cấp chứa các đối tượng có thể quản lý được, mỗi đối tượng được truy xuất thông qua một chuỗi số phân cách bằng dấu chấm gọi là OID (Object Identifier).
- **Liên kết:** [Module 04 - Enumeration.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2004%20Enumeration.md)

#### Câu 25 [Module 04]
Công cụ dòng lệnh kinh điển nào trên Kali Linux chuyên dùng để thực hiện liệt kê tài khoản người dùng, nhóm, share và chính sách mật khẩu trên máy chủ Windows qua SMB (cổng 445/139)?
- A. `enum4linux` (hoặc `enum4linux-ng`)
- B. `nikto`
- C. `sqlmap`
- D. `hydra`
- **Đáp án:** A
- **Giải thích:** `enum4linux` là công cụ wrapper gọi Samba client để truy vấn các phiên ẩn danh (null session), lấy RID cycling, danh sách user, share và group policy trên Windows.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 26 [Module 04]
Trong môi trường Active Directory, cổng mặc định nào được giao thức LDAP (Lightweight Directory Access Protocol) sử dụng để cho phép client truy vấn thông tin người dùng và máy tính?
- A. TCP 80
- B. TCP 389 (và TCP 636 cho LDAPS)
- C. TCP 445
- D. TCP 88
- **Đáp án:** B
- **Giải thích:** Cổng TCP 389 là cổng tiêu chuẩn của LDAP, TCP 636 dành cho LDAP qua SSL/TLS (LDAPS), cổng 88 dành cho Kerberos và cổng 445 dành cho SMB.
- **Liên kết:** [02_Active_Directory_Attack_and_Defense_Playbook.md](file:///mnt/second_drive/DOCS/SEC/docs/References/02_Active_Directory_Attack_and_Defense_Playbook.md)

#### Câu 27 [Module 04]
Kỹ thuật **RID Cycling** trong SMB Enumeration khai thác cơ chế nào của hệ điều hành Windows?
- A. Tấn công tràn bộ đệm stack trong lsass.exe
- B. Tăng dần chỉ số Relative Identifier (RID) gán sau Domain SID (ví dụ RID 500 = Administrator, 501 = Guest) để truy vấn tên tài khoản tương ứng
- C. Bắt giữ hash NTLM qua giao thức LLMNR
- D. Giả mạo chứng chỉ số số Kerberos TGT
- **Đáp án:** B
- **Giải thích:** Trong Windows SID (Security Identifier), phần cuối cùng là RID xác định tài khoản hoặc nhóm. Kẻ tấn công gửi các truy vấn liên tục với RID từ 500, 501, 1000, 1001... để liệt kê chính xác tên người dùng dù tài khoản đã bị đổi tên.
- **Liên kết:** [Module 04 - Enumeration.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2004%20Enumeration.md)

#### Câu 28 [Module 04]
Giao thức RPC (Remote Procedure Call) trên Linux/Unix thường sử dụng dịch vụ nào tại cổng TCP 111 để ánh xạ các số chương trình RPC tới các cổng TCP/UDP tương ứng?
- A. `rpcbind` (hoặc `portmap`)
- B. `nfsd`
- C. `inetd`
- D. `systemd`
- **Đáp án:** A
- **Giải thích:** `rpcbind` hoặc `portmapper` lắng nghe ở cổng 111, cho phép client truy vấn bằng lệnh `rpcinfo -p` để biết NFS, NIS hay các daemon RPC khác đang chạy ở cổng nào.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 29 [Module 04]
Để liệt kê danh sách các thư mục chia sẻ NFS (Network File System) từ một máy chủ từ xa, pentester sử dụng câu lệnh nào?
- A. `showmount -e <target_ip>`
- B. `nfsstat -r <target_ip>`
- C. `exportfs -v <target_ip>`
- D. `mount -t cifs <target_ip>`
- **Đáp án:** A
- **Giải thích:** Lệnh `showmount -e` truy vấn danh sách export list của máy chủ NFS để xem thư mục nào đang được chia sẻ cho client hoặc công khai toàn mạng (`*`).
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 30 [Module 04]
Lệnh SMTP nào sau đây được sử dụng để xác minh sự tồn tại của một địa chỉ hòm thư người dùng trên máy chủ mail?
- A. `HELO`
- B. `VRFY`
- C. `DATA`
- D. `QUIT`
- **Đáp án:** B
- **Giải thích:** Lệnh `VRFY <username>` yêu cầu máy chủ SMTP kiểm tra xem người dùng có tồn tại trong cơ sở dữ liệu hòm thư nội bộ hay không mà không cần gửi email thực sự. Lệnh `EXPN` dùng để mở rộng danh sách mailing list.
- **Liên kết:** [Module 04 - Enumeration.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2004%20Enumeration.md)

---

### MODULE 05: VULNERABILITY ANALYSIS

#### Câu 31 [Module 05]
Trong hệ thống đánh giá mức độ nghiêm trọng lỗ hổng bảo mật tiêu chuẩn quốc tế **CVSS v3.1** (Common Vulnerability Scoring System), dải điểm nào đại diện cho mức **Critical**?
- A. 0.1 - 3.9
- B. 4.0 - 6.9
- C. 7.0 - 8.9
- D. 9.0 - 10.0
- **Đáp án:** D
- **Giải thích:** Theo thang điểm CVSS v3.1: None (0.0), Low (0.1 - 3.9), Medium (4.0 - 6.9), High (7.0 - 8.9), và Critical (9.0 - 10.0).
- **Liên kết:** [06_NIST_SP_800-115_Technical_Guide.md](file:///mnt/second_drive/DOCS/SEC/docs/References/06_NIST_SP_800-115_Technical_Guide.md)

#### Câu 32 [Module 05]
Chuỗi định danh duy nhất được tổ chức MITRE cấp phát để theo dõi công khai các lỗ hổng bảo mật phần mềm trên toàn cầu tuân theo định dạng chuẩn nào?
- A. CVE (Common Vulnerabilities and Exposures), ví dụ `CVE-2021-44228`
- B. CWE (Common Weakness Enumeration)
- C. CPE (Common Platform Enumeration)
- D. CAPEC (Common Attack Pattern Enumeration and Classification)
- **Đáp án:** A
- **Giải thích:** CVE là mã định danh lỗ hổng cụ thể theo cú pháp `CVE-YYYY-NNNN`. CWE là phân loại bản chất sai sót lập trình (ví dụ CWE-89: SQL Injection); CPE là mã hóa tên nền tảng hệ thống.
- **Liên kết:** [Module 05 - Vulnerability Analysis.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2005%20Vulnerability%20Analysis.md)

#### Câu 33 [Module 05]
Khi máy quét lỗ hổng thông báo có lỗ hổng SQL Injection trên ứng dụng, nhưng khi pentester kiểm tra thủ công thì thấy mã nguồn thực tế đã sử dụng Prepared Statements và không hề có lỗi, tình huống này được gọi là gì?
- A. True Positive
- B. False Positive (Dương tính giả)
- C. False Negative (Âm tính giả)
- D. True Negative
- **Đáp án:** B
- **Giải thích:** False Positive là trường hợp công cụ quét báo cáo có lỗi nhưng thực tế hệ thống an toàn. Ngược lại, False Negative là hệ thống có lỗi nguy hiểm nhưng máy quét không phát hiện ra.
- **Liên kết:** [06_NIST_SP_800-115_Technical_Guide.md](file:///mnt/second_drive/DOCS/SEC/docs/References/06_NIST_SP_800-115_Technical_Guide.md)

#### Câu 34 [Module 05]
Công cụ quét lỗ hổng mã nguồn mở phổ biến nào sau đây tiền thân là nhánh phát triển tự do của Nessus sau khi Nessus chuyển sang giấy phép thương mại?
- A. OpenVAS (hiện thuộc Greenbone Vulnerability Management)
- B. Nikto
- C. Wireshark
- D. Burp Suite Community
- **Đáp án:** A
- **Giải thích:** Khi Tenable chuyển Nessus thành phần mềm độc quyền vào năm 2005, cộng đồng an ninh mạng đã fork phiên bản mã nguồn mở cuối cùng để tạo nên OpenVAS.
- **Liên kết:** [OpenVAS_Vulnerability_Scan_Report_Sample.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/OpenVAS_Vulnerability_Scan_Report_Sample.pdf)

#### Câu 35 [Module 05]
Trong cơ chế đánh giá độ nghiêm trọng CVSS, nhóm thuộc tính nào thể hiện các đặc tính cố hữu của lỗ hổng không phụ thuộc vào thời gian hay môi trường triển khai?
- A. Temporal Metrics
- B. Environmental Metrics
- C. Base Metrics
- D. Threat Metrics
- **Đáp án:** C
- **Giải thích:** Base Metrics phản ánh tính chất bất biến của lỗ hổng (Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, Confidentiality, Integrity, Availability).
- **Liên kết:** [Module 05 - Vulnerability Analysis.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2005%20Vulnerability%20Analysis.md)

#### Câu 36 [Module 05]
Sự khác biệt căn bản giữa **Vulnerability Assessment** (Đánh giá lỗ hổng) và **Penetration Testing** (Kiểm thử xâm nhập) là gì?
- A. Vulnerability Assessment luôn kiểm tra cả yếu tố xã hội
- B. Vulnerability Assessment chỉ xác định và liệt kê các lỗ hổng tiềm ẩn; Penetration Testing chủ động khai thác (exploit) lỗ hổng để chứng minh tác động thực tế và chiếm quyền kiểm soát
- C. Penetration Testing không được phép sử dụng công cụ tự động
- D. Vulnerability Assessment bắt buộc phải có hợp đồng cam kết bồi thường thiệt hại
- **Đáp án:** B
- **Giải thích:** Vulnerability Assessment tập trung vào việc lập danh mục rủi ro bằng máy quét; Penetration testing đi xa hơn bằng cách khai thác lỗ hổng, leo thang đặc quyền và di chuyển ngang để đánh giá chiều sâu thiệt hại.
- **Liên kết:** [06_NIST_SP_800-115_Technical_Guide.md](file:///mnt/second_drive/DOCS/SEC/docs/References/06_NIST_SP_800-115_Technical_Guide.md)

---

### MODULE 06: SYSTEM HACKING

#### Câu 37 [Module 06]
Công cụ nào sau đây thường được Red Team sử dụng trên hệ điều hành Windows để trích xuất mật khẩu dạng rõ, mã băm NTLM và vé Kerberos trực tiếp từ bộ nhớ tiến trình `lsass.exe`?
- A. Wireshark
- B. Mimikatz
- C. John the Ripper
- D. Hydra
- **Đáp án:** B
- **Giải thích:** Mimikatz (do Benjamin Delpy phát triển) là công cụ kinh điển tương tác với Local Security Authority Subsystem Service (LSASS) để dump credential, tạo vé Golden/Silver Ticket và thực hiện DCSync.
- **Liên kết:** [02_Active_Directory_Attack_and_Defense_Playbook.md](file:///mnt/second_drive/DOCS/SEC/docs/References/02_Active_Directory_Attack_and_Defense_Playbook.md)

#### Câu 38 [Module 06]
Kỹ thuật tấn công **Pass-the-Hash (PtH)** cho phép kẻ tấn công làm điều gì sau khi đã thu được mã băm NTLM của tài khoản quản trị?
- A. Giải mã băm ngược về mật khẩu văn bản rõ bằng thuật toán brute-force
- B. Xác thực trực tiếp tới các máy tính khác trong mạng qua SMB/RPC bằng chính mã băm NTLM mà không cần biết mật khẩu gốc
- C. Thay đổi mã PIN sinh trắc học Windows Hello
- D. Vô hiệu hóa Windows Defender vĩnh viễn
- **Đáp án:** B
- **Giải thích:** Giao thức xác thực NTLM sử dụng hàm băm của mật khẩu làm chìa khóa tính toán challenge-response. Do đó, sở hữu NTLM hash tương đương với việc sở hữu mật khẩu khi xác thực mạng.
- **Liên kết:** [01_MITRE_ATTCK_Enterprise_Matrix_Guide.md](file:///mnt/second_drive/DOCS/SEC/docs/References/01_MITRE_ATTCK_Enterprise_Matrix_Guide.md)

#### Câu 39 [Module 06]
Trên Linux, nếu một tệp thực thi nhị phân được gán cờ quyền **SUID (Set User ID)** thuộc về `root`, điều gì sẽ xảy ra khi một người dùng bình thường chạy tệp đó?
- A. Tiến trình sẽ bị chặn bởi SELinux
- B. Tiến trình sẽ thực thi với đặc quyền của người sở hữu tệp (`root`) thay vì người dùng đang gọi lệnh
- C. Hệ thống sẽ buộc khởi động lại vào Recovery Mode
- D. Mật khẩu của người dùng sẽ bị xóa
- **Đáp án:** B
- **Giải thích:** Cờ SUID (`chmod u+s`) cho phép tiến trình chạy với đặc quyền của chủ sở hữu file. Nếu các tệp như `/usr/bin/find` hoặc `/usr/bin/vim` bị gán SUID root, kẻ tấn công có thể dễ dàng leo thang lên root.
- **Liên kết:** [02_Master_Lecture_and_Lab_Plan.md#bài-giảng-06](file:///mnt/second_drive/DOCS/SEC/docs/Lectures/02_Master_Lecture_and_Lab_Plan.md)

#### Câu 40 [Module 06]
Kỹ thuật che giấu dữ liệu bí mật bên trong một tệp ảnh, video hoặc âm thanh mà không làm thay đổi trực quan hình thức hiển thị bên ngoài của tệp được gọi là:
- A. Cryptography
- B. Steganography (Giấu tin)
- C. Polymorphism
- D. Obfuscation
- **Đáp án:** B
- **Giải thích:** Steganography nhúng dữ liệu vào các bit trọng số thấp nhất (LSB - Least Significant Bit) của điểm ảnh để người xem thông thường không thể nhận biết sự khác biệt.
- **Liên kết:** [Module 06 - System Hacking.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2006%20System%20Hacking.md)

#### Câu 41 [Module 06]
Để xóa dấu vết nhật ký trên máy chủ Linux mục tiêu sau khi hoàn tất phiên tấn công, kỹ thuật nào sau đây thường được kẻ tấn công sử dụng để ngăn không cho lệnh vừa gõ lưu vào tệp lịch sử?
- A. `unset HISTFILE` hoặc `export HISTSIZE=0`
- B. `chmod 777 /var/log`
- C. `systemctl restart sshd`
- D. `touch /etc/shadow`
- **Đáp án:** A
- **Giải thích:** Lệnh `unset HISTFILE` hủy biến môi trường trỏ đến `~/.bash_history`, khiến shell không ghi lại các lệnh của phiên hiện tại khi người dùng thoát ra.
- **Liên kết:** [Module 06 - System Hacking.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2006%20System%20Hacking.md)

#### Câu 42 [Module 06]
Tính năng nào trên hệ thống tệp NTFS của Windows cho phép người dùng hoặc mã độc gắn các luồng dữ liệu ẩn vào một tệp hiện có mà không làm thay đổi kích thước tệp hiển thị trong Windows Explorer?
- A. VSS (Volume Shadow Copies)
- B. ADS (Alternate Data Streams)
- C. BitLocker
- D. EFS (Encrypting File System)
- **Đáp án:** B
- **Giải thích:** ADS cho phép gán luồng dữ liệu phụ theo cú pháp `filename:streamname`. Kẻ tấn công có thể giấu mã thực thi độc hại đằng sau một tệp text hoặc ảnh thông thường.
- **Liên kết:** [Module 06 - System Hacking.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2006%20System%20Hacking.md)

#### Câu 43 [Module 06]
Bảng mã băm được tính toán sẵn (pre-computed hash table) sử dụng hàm rút gọn để giảm thiểu không gian lưu trữ và tăng tốc độ bẻ khóa mật khẩu được gọi là:
- A. Rainbow Table
- B. Hashcat Dictionary
- C. Markov Chain
- D. Lookup Vector
- **Đáp án:** A
- **Giải thích:** Rainbow Table đánh đổi giữa bộ nhớ lưu trữ và thời gian tính toán CPU để tra cứu ngược từ hash ra plain-text trong vài giây, bị vô hiệu hóa khi mật khẩu được gắn Salt ngẫu nhiên.
- **Liên kết:** [Module 06 - System Hacking.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2006%20System%20Hacking.md)

#### Câu 44 [Module 06]
Kỹ thuật **DLL Hijacking** trên Windows xảy ra do nguyên nhân cốt lõi nào?
- A. Hệ thống không kiểm tra tính toàn vẹn chữ ký số của kernel driver
- B. Ứng dụng nạp một thư viện liên kết động (.dll) mà không chỉ định đường dẫn tuyệt đối, dẫn đến việc Windows tìm kiếm DLL theo thứ tự ưu tiên trong đó có thư mục ứng dụng hiện tại
- C. Tệp DLL bị dính lỗi tràn bộ đệm heap
- D. Tiến trình explorer.exe bị crash
- **Đáp án:** B
- **Giải thích:** DLL Search Order Hijacking lợi dụng thứ tự tìm kiếm mặc định của Windows. Kẻ tấn công đặt một DLL độc hại cùng tên vào thư mục ứng dụng để được nạp trước DLL chuẩn trong System32.
- **Liên kết:** [05_EDR_Evasion_and_Living_Off_The_Land_LOLBAS.md](file:///mnt/second_drive/DOCS/SEC/docs/References/05_EDR_Evasion_and_Living_Off_The_Land_LOLBAS.md)

#### Câu 45 [Module 06]
Tệp nào trên Windows lưu trữ toàn bộ mật khẩu mã băm của các tài khoản cục bộ (Local Users) và chỉ có thể truy cập được bởi SYSTEM?
- A. `C:\Windows\System32\drivers\etc\hosts`
- B. `C:\Windows\System32\config\SAM`
- C. `C:\Users\Default\NTUSER.DAT`
- D. `C:\Windows\System32\ntoskrnl.exe`
- **Đáp án:** B
- **Giải thích:** SAM (Security Account Manager) là hive registry lưu trữ password hash của các tài khoản local trên máy Windows độc lập hoặc member workstation.
- **Liên kết:** [Module 06 - System Hacking.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2006%20System%20Hacking.md)

#### Câu 46 [Module 06]
Trong tấn công leo thang đặc quyền Windows, lỗ hổng **Unquoted Service Path** cho phép kẻ tấn công làm gì nếu dịch vụ có đường dẫn dạng `C:\Program Files\My Service\service.exe`?
- A. Đọc trộm bộ nhớ RAM của lsass.exe
- B. Đặt một tệp thực thi độc hại mang tên `C:\Program.exe` hoặc `C:\Program Files\My.exe` để được dịch vụ thực thi với quyền SYSTEM khi khởi động
- C. Tấn công tràn bộ đệm nhân Windows
- D. Vô hiệu hóa UAC (User Account Control)
- **Đáp án:** B
- **Giải thích:** Khi đường dẫn dịch vụ chứa khoảng trắng mà không được bao quanh bởi dấu ngoặc kép `""`, Windows sẽ phân tách và thử thực thi từng tiền tố: `C:\Program.exe`, tiếp đến `C:\Program Files\My.exe`, và cuối cùng mới đến đúng đường dẫn đầy đủ.
- **Liên kết:** [Module 06 - System Hacking.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2006%20System%20Hacking.md)

---

### MODULE 07: MALWARE THREATS

#### Câu 47 [Module 07]
Loại mã độc nào có khả năng tự động lây nhiễm và lan truyền qua mạng tới các máy tính khác mà KHÔNG cần bất kỳ sự tương tác nào của người dùng (Zero-click)?
- A. Trojan Horse
- B. Worm (Sâu máy tính)
- C. Spyware
- D. Adware
- **Đáp án:** B
- **Giải thích:** Worm (ví dụ WannaCry, Conficker) khai thác các lỗ hổng dịch vụ mạng (như EternalBlue SMB) để tự quét, lây nhiễm và sao chép chính nó sang các nút mạng khác một cách độc lập hoàn toàn.
- **Liên kết:** [Module 07 - Malware Threats.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2007%20Malware%20Threats.md)

#### Câu 48 [Module 07]
Mã độc sử dụng kỹ thuật **Polymorphic Code** (Mã đa hình) làm thế nào để liên tục thay đổi chữ ký (signature) nhằm né tránh sự phát hiện của phần mềm Antivirus truyền thống?
- A. Thay đổi địa chỉ MAC của card mạng sau mỗi lần lây nhiễm
- B. Sử dụng một engine mã hóa (mutation engine) để thay đổi chìa khóa mã hóa và cấu trúc giải mã (decryptor stub) trong mỗi thế hệ file nhị phân mới nhưng vẫn giữ nguyên logic hoạt động cốt lõi
- C. Tự động biên dịch lại mã nguồn từ ngôn ngữ C sang Python
- D. Chỉ hoạt động trong chế độ Safe Mode
- **Đáp án:** B
- **Giải thích:** Polymorphic malware sinh ra một decryptor stub khác nhau và sử dụng key mã hóa ngẫu nhiên mỗi lần nhân bản, làm cho mã băm (MD5/SHA256) và chữ ký tĩnh thay đổi hoàn toàn.
- **Liên kết:** [SANS_Malware_Analysis_and_Reverse_Engineering.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SANS_Malware_Analysis_and_Reverse_Engineering.pdf)

#### Câu 49 [Module 07]
Khác với Polymorphic, mã độc **Metamorphic Code** (Mã biến hình) thay đổi cơ chế né tránh như thế nào?
- A. Hoàn toàn không mã hóa thân file, mà dùng trình biên dịch dịch chuyển cấu trúc mã assembly (chèn lệnh NOP, hoán đổi thanh ghi, thay đổi luồng điều khiển) ở mỗi thế hệ
- B. Tự xóa chính mình sau 24 giờ
- C. Đóng gói payload vào tệp PDF
- D. Chạy hoàn toàn trên card đồ họa GPU
- **Đáp án:** A
- **Giải thích:** Metamorphic malware phân tích và viết lại hoàn toàn mã assembly của chính nó ở mỗi phiên bản con (Register swapping, dead code insertion, instruction substitution), không cần dùng decryptor stub.
- **Liên kết:** [SANS_Malware_Analysis_and_Reverse_Engineering.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SANS_Malware_Analysis_and_Reverse_Engineering.pdf)

#### Câu 50 [Module 07]
Loại Trojan nào tạo cửa sau cho phép kẻ tấn công điều khiển máy tính nạn nhân từ xa thông qua giao diện đồ họa GUI, chụp webcam, ghi âm microphone và quản lý tệp?
- A. Defacement Trojan
- B. RAT (Remote Access Trojan)
- C. Ransomware
- D. Rootkit
- **Đáp án:** B
- **Giải thích:** RAT (Remote Access Trojan) là phần mềm gián điệp cung cấp quyền kiểm soát tương tác trực tiếp tới hệ thống bị hại từ xa qua kênh C2.
- **Liên kết:** [Module 07 - Malware Threats.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2007%20Malware%20Threats.md)

#### Câu 51 [Module 07]
Loại phần mềm độc hại nào can thiệp sâu vào nhân hệ điều hành (Kernel-mode), hooking các hàm API của hệ thống (SSDT hooking hoặc IRP hooking) để ẩn giấu hoàn toàn tiến trình, tệp và kết nối mạng của chính nó khỏi Task Manager?
- A. Rootkit
- B. Logic Bomb
- C. Macro Virus
- D. Scareware
- **Đáp án:** A
- **Giải thích:** Rootkit (đặc biệt là Ring 0 / Kernel Rootkit) thay đổi trực tiếp cấu trúc dữ liệu của nhân OS hoặc can thiệp bảng phân phối cuộc gọi hệ thống, đánh lừa các công cụ giám sát userland.
- **Liên kết:** [Module 07 - Malware Threats.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2007%20Malware%20Threats.md)

#### Câu 52 [Module 07]
Khi phân tích mã độc trong môi trường cô lập, giai đoạn nào bao gồm việc chạy mẫu mã độc thực tế trong Sandbox và giám sát các thay đổi registry, tệp và kết nối mạng theo thời gian thực?
- A. Static Code Analysis (Phân tích tĩnh)
- B. Dynamic Analysis (Phân tích động)
- C. Footprinting
- D. Vulnerability Assessment
- **Đáp án:** B
- **Giải thích:** Phân tích động (Dynamic / Behavioral Analysis) quan sát hành vi thực tế của mẫu độc hại khi nó chạy trong môi trường sandbox được theo dõi bởi Process Monitor, Wireshark, RegShot.
- **Liên kết:** [SANS_Malware_Analysis_and_Reverse_Engineering.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SANS_Malware_Analysis_and_Reverse_Engineering.pdf)

#### Câu 53 [Module 07]
Một đoạn mã độc được lập trình viên chèn vào hệ thống từ trước và nằm im lìm cho đến khi một sự kiện cụ thể xảy ra (ví dụ: ngày sinh nhật công ty, hoặc tài khoản nhân viên bị xóa khỏi danh sách nhân sự) mới kích hoạt phá hủy dữ liệu được gọi là:
- A. Logic Bomb (Bom logic)
- B. Macro Trojan
- C. Cryptominer
- D. Fileless Malware
- **Đáp án:** A
- **Giải thích:** Logic Bomb là mã độc được kích hoạt dựa trên điều kiện thời gian hoặc logic nghiệp vụ cụ thể để gây hại cho tổ chức.
- **Liên kết:** [Module 07 - Malware Threats.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2007%20Malware%20Threats.md)

---

### MODULE 08: SNIFFING

#### Câu 54 [Module 08]
Kỹ thuật tấn công nào gửi các gói tin ARP Reply giả mạo tới gateway và máy nạn nhân nhằm làm sai lệch bảng ánh xạ địa chỉ IP - MAC trong switch cục bộ, cho phép hacker thực hiện Man-in-the-Middle (MitM)?
- A. DNS Amplification
- B. ARP Poisoning (ARP Spoofing)
- C. MAC Flooding
- D. BGP Hijacking
- **Đáp án:** B
- **Giải thích:** Giao thức ARP không có cơ chế xác thực nguồn. Khi kẻ tấn công liên tục gửi gói tin ARP giả mạo xưng danh IP của Gateway với địa chỉ MAC của hacker, bảng ARP cache của nạn nhân sẽ bị cập nhật sai.
- **Liên kết:** [01_Computer_Networking/04_Network_Layer.md](file:///mnt/second_drive/DOCS/SEC/01_Computer_Networking/04_Network_Layer.md)

#### Câu 55 [Module 08]
Kỹ thuật **MAC Flooding** làm tràn bảng CAM (Content Addressable Memory) của thiết bị Switch bằng cách gửi hàng ngàn gói tin với địa chỉ MAC nguồn giả mạo nhằm biến Switch thành thiết bị nào sau đây?
- A. Router định tuyến BGP
- B. Hub (chuyển sang chế độ Fail-Open và broadcast gói tin ra tất cả các cổng)
- C. Firewall thế hệ mới (NGFW)
- D. Wireless Access Point
- **Đáp án:** B
- **Giải thích:** Khi bảng CAM bị đầy bộ nhớ, switch không thể học thêm địa chỉ MAC mới và buộc phải chuyển sang chế độ an toàn lỗi (fail-open), gửi broadcast tất cả frame tới mọi cổng, cho phép hacker gắn máy vào cổng bất kỳ để sniff toàn bộ lưu lượng.
- **Liên kết:** [Module 08 - Sniffing.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2008%20Sniffing.md)

#### Câu 56 [Module 08]
Trong công cụ bắt gói tin Wireshark, bộ lọc hiển thị (Display Filter) nào sau đây chỉ lọc các yêu cầu HTTP GET hoặc POST có chứa dữ liệu?
- A. `tcp.port == 80`
- B. `http.request.method == "GET" || http.request.method == "POST"`
- C. `ip.proto == 6`
- D. `arp.opcode == 1`
- **Đáp án:** B
- **Giải thích:** `http.request.method` lọc theo phương thức yêu cầu HTTP của giao thức tầng 7, chính xác hơn bộ lọc tầng 4 `tcp.port == 80`.
- **Liên kết:** [Wireshark_Display_Filters_CheatSheet.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/Wireshark_Display_Filters_CheatSheet.pdf)

#### Câu 57 [Module 08]
Cuộc tấn công làm cạn kiệt toàn bộ dải địa chỉ IP có sẵn trên DHCP Server bằng cách gửi hàng loạt yêu cầu DHCP Discover với các địa chỉ MAC ngụy tạo được gọi là:
- A. DHCP Starvation Attack
- B. Rogue DHCP Server
- C. DNS Cache Poisoning
- D. VLAN Hopping
- **Đáp án:** A
- **Giải thích:** DHCP Starvation làm kiệt quệ pool IP của DHCP server hợp lệ, tạo tiền đề để hacker dựng một Rogue DHCP Server cấp phát Gateway và DNS độc hại cho các máy trạm mới tham gia mạng.
- **Liên kết:** [Module 08 - Sniffing.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2008%20Sniffing.md)

#### Câu 58 [Module 08]
Tính năng bảo mật nào trên thiết bị Switch doanh nghiệp của Cisco được khuyến nghị để ngăn chặn triệt để tấn công DHCP Starvation và Rogue DHCP Server?
- A. Port Security
- B. DHCP Snooping
- C. Dynamic ARP Inspection (DAI)
- D. Spanning Tree Protocol (STP)
- **Đáp án:** B
- **Giải thích:** DHCP Snooping phân loại các cổng thành Trusted (kết nối tới DHCP server thật) và Untrusted (kết nối máy người dùng). Các gói DHCP Offer phát ra từ cổng Untrusted sẽ bị switch drop ngay lập tức.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 59 [Module 08]
Giao thức nào sau đây truyền dữ liệu và thông tin xác thực (username/password) hoàn toàn dưới dạng Cleartext, cực kỳ dễ bị đánh cắp bởi kỹ thuật Sniffing?
- A. SSH (Secure Shell)
- B. HTTPS (HTTP over TLS)
- C. Telnet và FTP
- D. SFTP
- **Đáp án:** C
- **Giải thích:** Telnet (port 23) và FTP (port 21) không có bất kỳ lớp mã hóa nào trên đường truyền. Bất kỳ ai bắt được gói tin đều có thể đọc được user/password bằng Wireshark.
- **Liên kết:** [SANS_TCPIP_Packet_CheatSheet_2021.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SANS_TCPIP_Packet_CheatSheet_2021.pdf)

#### Câu 60 [Module 08]
Kỹ thuật **SSL Stripping** (do Moxie Marlinspike phát triển) hạ cấp bảo mật của người dùng bằng cách nào?
- A. Bẻ khóa thuật toán mã hóa RSA 2048-bit bằng siêu máy tính
- B. Chặn các liên kết chuyển hướng `https://` từ web server và chuyển đổi chúng thành các liên kết `http://` văn bản rõ gửi về trình duyệt của nạn nhân
- C. Xóa chứng chỉ số gốc trong Windows Certificate Store
- D. Tấn công từ chối dịch vụ vào CA
- **Đáp án:** B
- **Giải thích:** SSL Stripping đánh lừa người dùng bằng cách duy trì kết nối HTTPS với server thật nhưng gửi phiên bản HTTP không mã hóa về cho nạn nhân. Cơ chế HSTS (HTTP Strict Transport Security) sinh ra để khắc phục lỗ hổng này.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

---

### MODULE 09: SOCIAL ENGINEERING

#### Câu 61 [Module 09]
Hình thức tấn công Social Engineering nhắm mục tiêu cực kỳ chính xác vào các cá nhân cấp cao trong doanh nghiệp (như CEO, CFO, Giám đốc CNTT) nhằm chiếm đoạt tài sản hoặc thông tin chiến lược được gọi là:
- A. Phishing
- B. Vishing
- C. Whaling
- D. Smishing
- **Đáp án:** C
- **Giải thích:** Whaling (săn cá voi) là hình thức Spear Phishing cấp độ cao nhắm trực diện vào lãnh đạo cấp cao của tổ chức (C-suite executives).
- **Liên kết:** [Module 09 - Social Engineering.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2009%20Social%20Engineering.md)

#### Câu 62 [Module 09]
Hành vi kẻ tấn công đi ngay sau lưng một nhân viên có thẻ từ hợp lệ để lẻn qua cửa kiểm soát an ninh vào tòa nhà mà không cần quẹt thẻ được gọi là kỹ thuật gì?
- A. Shoulder Surfing
- B. Tailgating (hoặc Piggybacking)
- C. Dumpster Diving
- D. Pretexting
- **Đáp án:** B
- **Giải thích:** Tailgating là hình thức xâm nhập vật lý lợi dụng sự lịch sự của nhân viên (giữ cửa giúp người đi sau) để vượt qua cửa kiểm soát an ninh.
- **Liên kết:** [Module 09 - Social Engineering.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2009%20Social%20Engineering.md)

#### Câu 63 [Module 09]
Một kẻ tấn công giả danh nhân viên hỗ trợ kỹ thuật IT gọi điện thoại cho nhân viên kế toán thông báo hệ thống đang nâng cấp và yêu cầu cung cấp mật khẩu để đồng bộ dữ liệu. Kỹ thuật này thuộc hình thức:
- A. Vishing (Voice Phishing) dựa trên Pretexting
- B. Smishing
- C. Watering Hole
- D. Pharming
- **Đáp án:** A
- **Giải thích:** Vishing là hình thức lừa đảo qua giọng nói điện thoại, kết hợp với Pretexting (dựng kịch bản giả định danh tính) để thao túng tâm lý nạn nhân.
- **Liên kết:** [Module 09 - Social Engineering.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2009%20Social%20Engineering.md)

#### Câu 64 [Module 09]
Kỹ thuật tấn công mạng nào cài mã độc vào một trang web ngành nghề uy tín mà các nhân viên của công ty mục tiêu thường xuyên truy cập hàng ngày?
- A. Watering Hole Attack
- B. Typosquatting
- C. Baiting
- D. Reverse Social Engineering
- **Đáp án:** A
- **Giải thích:** Watering Hole (Tấn công hố nước) nhắm vào thói quen duyệt web của nạn nhân. Kẻ tấn công chiếm quyền kiểm soát trang web ngành nghề rồi chèn mã khai thác trình duyệt (drive-by download).
- **Liên kết:** [01_MITRE_ATTCK_Enterprise_Matrix_Guide.md](file:///mnt/second_drive/DOCS/SEC/docs/References/01_MITRE_ATTCK_Enterprise_Matrix_Guide.md)

#### Câu 65 [Module 09]
Kẻ tấn cố tình thả các ổ đĩa USB nhiễm mã độc tại bãi đậu xe hoặc sảnh thang máy của công ty mục tiêu với nhãn dán "Bảng lương quý 4 - Tuyệt mật" nhằm kích thích tính tò mò của nhân viên cắm vào máy tính làm việc. Kỹ thuật này là:
- A. Baiting (Cài mồi)
- B. Quid Pro Quo
- C. Phishing
- D. Eavesdropping
- **Đáp án:** A
- **Giải thích:** Baiting khai thác lòng tham hoặc sự tò mò của con người bằng cách cung cấp một món đồ vật lý (USB, quà tặng) chứa mã độc.
- **Liên kết:** [Module 09 - Social Engineering.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2009%20Social%20Engineering.md)


---

## PHẦN 2: MODULE 10 - 20 (CÂU 66 ĐẾN CÂU 125)

### MODULE 10: DENIAL-OF-SERVICE (DoS / DDoS)

#### Câu 66 [Module 10]
Tấn công **SYN Flood** làm cạn kiệt tài nguyên bộ nhớ của máy chủ mục tiêu (bảng SYN backlog) bằng cách khai thác cơ chế nào của giao thức TCP?
- A. Gửi gói tin TCP FIN liên tục
- B. Gửi hàng loạt gói TCP SYN với địa chỉ IP nguồn ngụy tạo nhưng không bao giờ phản hồi gói ACK cuối cùng để hoàn tất bắt tay 3 bước
- C. Gửi gói TCP RST với kích thước khổng lồ
- D. Đổi hướng cổng kết nối bằng ICMP Redirect
- **Đáp án:** B
- **Giải thích:** Khi nhận gói SYN, máy chủ cấp phát bộ nhớ TCB (Transmission Control Block) và gửi SYN/ACK chờ client phản hồi ACK. Do IP nguồn giả mạo, kết nối rơi vào trạng thái SYN_RECEIVED cho đến khi hết timeout, làm tràn bảng backlog và từ chối các kết nối hợp lệ.
- **Liên kết:** [01_Computer_Networking/03_Transport_Layer.md](file:///mnt/second_drive/DOCS/SEC/01_Computer_Networking/03_Transport_Layer.md)

#### Câu 67 [Module 10]
Cơ chế phòng thủ nào tại tầng hạt nhân (kernel) giúp máy chủ chống lại tấn công SYN Flood mà không cần tăng kích thước hàng đợi backlog?
- A. SYN Cookies
- B. Port Knocking
- C. Address Resolution Protocol
- D. NAT Overload
- **Đáp án:** A
- **Giải thích:** SYN Cookies mã hóa thông tin trạng thái kết nối vào số thứ tự ban đầu (Initial Sequence Number - ISN) của gói SYN/ACK và không cấp phát bộ nhớ TCB cho đến khi client gửi gói ACK hợp lệ phản hồi lại.
- **Liên kết:** [01_Computer_Networking/03_Transport_Layer.md](file:///mnt/second_drive/DOCS/SEC/01_Computer_Networking/03_Transport_Layer.md)

#### Câu 68 [Module 10]
Cuộc tấn công **Smurf Attack** khuếch đại lưu lượng tấn công bằng cách gửi loại gói tin nào tới địa chỉ IP Broadcast của một mạng trung gian?
- A. TCP SYN
- B. ICMP Echo Request với địa chỉ IP nguồn bị giả mạo thành IP của nạn nhân
- C. UDP DNS Query
- D. IGMP Membership Report
- **Đáp án:** B
- **Giải thích:** Gói ICMP Echo Request gửi tới địa chỉ Broadcast sẽ khiến toàn bộ các máy trạm trong mạng đồng loạt gửi phản hồi ICMP Echo Reply dồn dập về địa chỉ IP nguồn giả mạo của nạn nhân.
- **Liên kết:** [Module 10 - DOS and DDOS.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2010%20Denial-of-Service.md)

#### Câu 69 [Module 10]
Tấn công **Slowloris** làm tê liệt máy chủ web (như Apache) bằng cách nào mà chỉ cần băng thông mạng cực kỳ thấp?
- A. Gửi hàng triệu truy vấn HTTP GET mỗi giây
- B. Mở nhiều kết nối HTTP đồng thời và gửi các header HTTP không hoàn chỉnh theo từng khoảng thời gian đều đặn để giữ cho các thread/socket của server luôn ở trạng thái chờ
- C. Khai thác lỗ hổng tràn bộ đệm trong OpenSSL
- D. Tấn công DNS Amplification
- **Đáp án:** B
- **Giải thích:** Slowloris không bao giờ gửi chuỗi kết thúc `\r\n\r\n` của header HTTP. Server giữ kết nối mở để chờ dữ liệu tiếp theo, nhanh chóng làm cạn kiệt giới hạn `MaxClients` hoặc thread pool của máy chủ web.
- **Liên kết:** [Module 10 - DOS and DDOS.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2010%20Denial-of-Service.md)

#### Câu 70 [Module 10]
Tấn công khuếch đại **DNS Amplification Attack** sử dụng giao thức truyền vận nào và khai thác tính năng nào của DNS Server?
- A. Giao thức TCP trên cổng 53
- B. Giao thức UDP trên cổng 53 kết hợp với truy vấn bản ghi lớn (`ANY` hoặc `TXT`) trên các Open DNS Resolvers có hỗ trợ EDNS0
- C. Giao thức ICMP trên cổng 80
- D. Giao thức BGP trên cổng 179
- **Đáp án:** B
- **Giải thích:** UDP là giao thức không hướng kết nối (connectionless), cho phép kẻ tấn công giả mạo IP nguồn của nạn nhân. Truy vấn nhỏ (vài chục byte) với cờ ANY kích hoạt phản hồi DNS khổng lồ (vài nghìn byte) dội về nạn nhân (hệ số khuếch đại lên tới 50 - 70 lần).
- **Liên kết:** [Module 10 - DOS and DDOS.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2010%20Denial-of-Service.md)

#### Câu 71 [Module 10]
Mạng lưới hàng triệu thiết bị Internet vạn vật (IoT như IP Camera, Router gia đình) bị nhiễm mã độc và chịu sự điều khiển tập trung của hacker để thực hiện các cuộc tấn công DDoS khổng lồ được gọi là:
- A. Honeypot Grid
- B. Botnet
- C. Darknet
- D. Blockchain Consensus
- **Đáp án:** B
- **Giải thích:** Botnet (như Mirai) bao gồm các máy tính/thiết bị bị chiếm quyền (Zombies/Bots) nhận lệnh từ máy chủ Command and Control (C2) của Botmaster để tiến hành DDoS quy mô lớn.
- **Liên kết:** [Module 10 - DOS and DDOS.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2010%20Denial-of-Service.md)

---

### MODULE 11: SESSION HIJACKING

#### Câu 72 [Module 11]
Trong tấn công chiếm quyền điều khiển phiên TCP (TCP Session Hijacking), hacker cần phải dự đoán chính xác giá trị nào của luồng truyền thông?
- A. TCP Port nguồn
- B. TCP Sequence Number (Số thứ tự tuần tự gói tin)
- C. Độ dài khóa SSL
- D. TTL của router
- **Đáp án:** B
- **Giải thích:** Để tiêm dữ liệu độc hại vào phiên kết nối TCP đang mở mà không làm đứt kết nối, kẻ tấn công phải dự đoán chính xác số TCP Sequence Number tiếp theo mà bên nhận đang kỳ vọng.
- **Liên kết:** [01_Computer_Networking/03_Transport_Layer.md](file:///mnt/second_drive/DOCS/SEC/01_Computer_Networking/03_Transport_Layer.md)

#### Câu 73 [Module 11]
Cuộc tấn công **Session Fixation** xảy ra khi:
- A. Kẻ tấn công bẻ khóa thuật toán mã hóa AES
- B. Ứng dụng web chấp nhận một Session ID do kẻ tấn công chỉ định sẵn (ví dụ qua URL) và tiếp tục duy trì Session ID này sau khi người dùng đăng nhập thành công
- C. Người dùng quên đăng xuất khỏi máy tính công cộng
- D. Quản trị viên khởi động lại dịch vụ web
- **Đáp án:** B
- **Giải thích:** Trong Session Fixation, hacker cấp cho nạn nhân một liên kết chứa Session ID đã biết. Khi nạn nhân đăng nhập, web server không làm mới Session ID (không gọi regenerate session), dẫn đến hacker dùng lại đúng Session ID đó để chiếm quyền.
- **Liên kết:** [Module 11 - Session Hijacking.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2011%20Session%20Hijacking.md)

#### Câu 74 [Module 11]
Cờ thuộc tính nào của Cookie trong ứng dụng web có tác dụng ngăn chặn hoàn toàn mã JavaScript độc hại (từ lỗi XSS) đọc hoặc đánh cắp Cookie phiên thông qua `document.cookie`?
- A. `Secure`
- B. `HttpOnly`
- C. `SameSite=Strict`
- D. `Domain`
- **Đáp án:** B
- **Giải thích:** Cờ `HttpOnly` chỉ thị cho trình duyệt web chỉ gửi cookie qua các tiêu đề HTTP/HTTPS và cấm các đoạn mã script phía client (JavaScript) truy xuất đối tượng cookie này.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 75 [Module 11]
Cờ `SameSite=Strict` trên Cookie có tác dụng bảo vệ ứng dụng web khỏi loại tấn công nguy hiểm nào sau đây?
- A. SQL Injection
- B. CSRF (Cross-Site Request Forgery)
- C. Buffer Overflow
- D. Path Traversal
- **Đáp án:** B
- **Giải thích:** `SameSite=Strict` ngăn không cho trình duyệt tự động đính kèm cookie xác thực khi người dùng theo liên kết từ một trang web bên thứ ba khác, ngăn chặn triệt để tấn công CSRF.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 76 [Module 11]
Giao thức bảo mật nào ở tầng Network có khả năng vô hiệu hóa hoàn toàn các cuộc tấn công TCP Session Hijacking và Sniffing bằng cách mã hóa và xác thực toàn bộ gói tin IP?
- A. Telnet
- B. IPsec (ESP - Encapsulating Security Payload)
- C. RIPv2
- D. SNMPv1
- **Đáp án:** B
- **Giải thích:** IPsec cung cấp tính bảo mật (Confidentiality qua ESP) và tính toàn vẹn/xác thực nguồn gốc (Integrity qua AH/ESP), khiến kẻ tấn công không thể tiêm gói tin hoặc đọc nội dung mà không có khóa chia sẻ bí mật.
- **Liên kết:** [01_Computer_Networking/04_Network_Layer.md](file:///mnt/second_drive/DOCS/SEC/01_Computer_Networking/04_Network_Layer.md)

---

### MODULE 12: EVADING IDS, FIREWALLS, AND HONEYPOTS

#### Câu 77 [Module 12]
Hệ thống **Honeypot** được thiết kế trong kiến trúc an ninh mạng nhằm mục đích gì?
- A. Làm máy chủ lưu trữ bản sao lưu dự phòng của doanh nghiệp
- B. Làm hệ thống mồi nhử cố tình chứa lỗ hổng để thu hút kẻ tấn công, ghi lại phương thức tác chiến (TTPs) và cảnh báo sớm cho đội ngũ SOC
- C. Tăng tốc độ truy cập internet cho nhân viên
- D. Cân bằng tải cho máy chủ cơ sở dữ liệu
- **Đáp án:** B
- **Giải thích:** Honeypot là hệ thống không chứa giá trị sản xuất thực nhưng được ngụy trang như một máy chủ quan trọng để theo dõi hành vi tấn công và phát hiện xâm nhập sớm.
- **Liên kết:** [Module 12 - Evading IDS, Firewall and HoneyPots/topics.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2012%20Evading%20IDS%20Firewalls%20and%20Honeypots.md)

#### Câu 78 [Module 12]
Kỹ thuật **IP Fragmentation** được sử dụng để vượt qua hệ thống IDS/IPS bằng cách nào?
- A. Thay đổi địa chỉ MAC của card mạng
- B. Phân chia gói tin chứa chữ ký độc hại thành các mảnh IP siêu nhỏ (IP fragments) sao cho mỗi mảnh không đủ chứa toàn bộ chữ ký nhận diện của IDS, sau đó được máy chủ đích ghép lại
- C. Mã hóa gói tin bằng thuật toán AES 256
- D. Gửi gói tin qua mạng ẩn danh Tor
- **Đáp án:** B
- **Giải thích:** Nếu IDS/IPS không thực hiện tái hợp gói tin (Packet reassembly) trước khi kiểm tra chữ ký, các mảnh gói tin độc hại sẽ lọt qua dễ dàng và được máy chủ đích tái lập thành mã độc hoàn chỉnh.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 79 [Module 12]
Tùy chọn nào trong công cụ Nmap cho phép chèn thêm các địa chỉ IP ngụy tạo (Decoys) vào quá trình quét để làm rối loạn nhật ký phân tích của đội ngũ phòng thủ?
- A. `nmap -D RND:10 <target>`
- B. `nmap -f <target>`
- C. `nmap --source-port 53 <target>`
- D. `nmap --mtu 24 <target>`
- **Đáp án:** A
- **Giải thích:** Cờ `-D` (Decoy) tạo ra các gói tin quét song song với địa chỉ IP nguồn ngẫu nhiên hoặc chỉ định, khiến log firewall và IDS tràn ngập địa chỉ IP khác nhau và không thể biết được IP nào là thủ phạm thực sự.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 80 [Module 12]
Kỹ thuật né tránh tường lửa bằng cách ép các gói tin quét sử dụng cổng nguồn quen thuộc như `53` (DNS) hoặc `20` (FTP Data) được thực hiện trong Nmap bằng lệnh nào?
- A. `nmap -g 53` (hoặc `nmap --source-port 53`)
- B. `nmap -p 53`
- C. `nmap -sO`
- D. `nmap --traceroute`
- **Đáp án:** A
- **Giải thích:** Một số tường lửa cũ cấu hình lỏng lẻo cho phép mọi gói tin xuất phát từ cổng nguồn 53 hoặc 20 đi qua mà không kiểm tra trạng thái. Cờ `-g` / `--source-port` ép Nmap sử dụng cổng nguồn này.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 81 [Module 12]
Sự khác biệt cốt lõi giữa **Signature-based IDS** (Nhận diện theo chữ ký) và **Anomaly-based IDS** (Nhận diện theo bất thường) là gì?
- A. Anomaly-based IDS không có khả năng phát hiện tấn công Zero-day
- B. Signature-based IDS chỉ phát hiện các cuộc tấn công đã biết dựa trên mẫu định nghĩa trước; Anomaly-based IDS xây dựng baseline hoạt động bình thường và cảnh báo khi lưu lượng đi chệch khỏi chuẩn đó (có khả năng phát hiện Zero-day)
- C. Signature-based IDS hoạt động ở Layer 2, Anomaly hoạt động ở Layer 7
- D. Signature-based IDS đòi hỏi kết nối đám mây bắt buộc
- **Đáp án:** B
- **Giải thích:** Nhận diện theo chữ ký giống như Antivirus so khớp hash/pattern, bất lực trước biến thể mới. Nhận diện theo bất thường phân tích hành vi và độ lệch thống kê, phát hiện được các cuộc tấn công chưa từng xuất hiện.
- **Liên kết:** [Module 12 - Evading IDS, Firewall and HoneyPots/topics.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2012%20Evading%20IDS%20Firewalls%20and%20Honeypots.md)

#### Câu 82 [Module 12]
Kỹ thuật **DNS Tunneling** (sử dụng các công cụ như `dnscat2` hoặc `iodine`) giúp vượt qua hệ thống kiểm soát mạng doanh nghiệp bằng cách nào?
- A. Mã hóa toàn bộ dữ liệu nhị phân hoặc shell tương tác vào các truy vấn DNS (bản ghi TXT, A) gửi tới một authoritative DNS server do kẻ tấn công kiểm soát qua cổng UDP 53 thường được firewall cho phép đi qua
- B. Tấn công tràn bộ đệm trên máy chủ DNS nội bộ
- C. Tạo kênh VPN qua cổng 443
- D. Bẻ khóa mật khẩu Wi-Fi WPA2
- **Đáp án:** A
- **Giải thích:** Cổng 53 UDP hầu như luôn được mở ở mọi mạng doanh nghiệp để phân giải tên miền. DNS Tunneling đóng gói lưu lượng C2/exfiltration vào payload DNS để lọt qua firewall và proxy kiểm duyệt.
- **Liên kết:** [05_EDR_Evasion_and_Living_Off_The_Land_LOLBAS.md](file:///mnt/second_drive/DOCS/SEC/docs/References/05_EDR_Evasion_and_Living_Off_The_Land_LOLBAS.md)

---

### MODULE 13: HACKING WEB SERVERS

#### Câu 83 [Module 13]
Lỗ hổng cấu hình nguy hiểm nào cho phép người dùng xem được toàn bộ danh sách tệp và thư mục con trong một đường dẫn máy chủ web khi không có tệp chỉ mục mặc định (như `index.html` hoặc `index.php`)?
- A. Cross-Site Scripting
- B. Directory Listing (hoặc Directory Browsing)
- C. SQL Injection
- D. MIME Sniffing
- **Đáp án:** B
- **Giải thích:** Directory Listing phơi bày toàn bộ cấu trúc thư mục, các tệp backup (`.bak`, `.zip`) và tệp mã nguồn lưu tạm của lập trình viên cho kẻ tấn công tải về.
- **Liên kết:** [Module 13 - Hacking web Servers/13_Hacking_Web_Servers.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2013%20Hacking%20Web%20Servers.md)

#### Câu 84 [Module 13]
Tính năng mở rộng nào trên máy chủ web (như IIS hoặc Apache) hỗ trợ các phương thức HTTP như `PUT`, `DELETE`, `MOVE`, `COPY` và nếu bị cấu hình sai mở quyền ghi sẽ cho phép hacker tải lên trực tiếp Webshell vào webroot?
- A. WebDAV (Web Distributed Authoring and Versioning)
- B. FastCGI
- C. Mod_Security
- D. OpenSSL
- **Đáp án:** A
- **Giải thích:** WebDAV mở rộng giao thức HTTP cho phép quản trị viên tải và chỉnh sửa tệp từ xa. Nếu không cấu hình xác thực chặt chẽ, kẻ tấn công có thể dùng phương thức `PUT` để đẩy file webshell độc hại lên server.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

#### Câu 85 [Module 13]
Kỹ thuật **Banner Grabbing** trên máy chủ web giúp pentester thu thập được những thông tin giá trị nào?
- A. Mật khẩu root của máy chủ
- B. Tên máy chủ web (Apache, Nginx, Microsoft-IIS) và số hiệu phiên bản chính xác thông qua tiêu đề phản hồi `Server`
- C. Danh sách email nhân viên
- D. Khóa riêng tư RSA SSL
- **Đáp án:** B
- **Giải thích:** Tiêu đề `Server` trong phản hồi HTTP trả về chi tiết tên phần mềm máy chủ và phiên bản (ví dụ: `Apache/2.4.49 (Unix)`), từ đó pentester có thể tra cứu CVE tương ứng (như Path Traversal CVE-2021-41773).
- **Liên kết:** [Module 13 - Hacking web Servers/13_Hacking_Web_Servers.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2013%20Hacking%20Web%20Servers.md)

#### Câu 86 [Module 13]
Lỗ hổng **Path Traversal** (Leo thang thư mục) trên web server xuất phát từ việc chuỗi đường dẫn đầu vào không được lọc các ký tự điều hướng thư mục nào?
- A. `http://`
- B. `../` hoặc `..\` (Dot-Dot-Slash)
- C. `<script>`
- D. `DROP TABLE`
- **Đáp án:** B
- **Giải thích:** Ký tự `../` trong hệ thống tệp dùng để nhảy về thư mục cha. Nếu ứng dụng web ghép trực tiếp tham số người dùng vào đường dẫn tệp (ví dụ `download.php?file=../../../../etc/passwd`), kẻ tấn công có thể đọc bất kỳ tệp nhạy cảm nào trong hệ thống.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 87 [Module 13]
Trong kiến trúc bảo mật máy chủ web, một mạng vùng đệm được cô lập nằm giữa Internet công cộng và Mạng nội bộ doanh nghiệp (chuyên đặt các máy chủ Web, Mail, DNS) được gọi là:
- A. VPN
- B. DMZ (Demilitarized Zone)
- C. VLAN Trunking
- D. Active Directory Forest
- **Đáp án:** B
- **Giải thích:** DMZ là phân vùng mạng bán tin cậy ngăn cách giữa Internet và mạng nội bộ (LAN). Nếu máy chủ web trong DMZ bị chiếm quyền, firewall ngăn kẻ tấn công xâm nhập trực tiếp vào hệ thống lõi cơ sở dữ liệu nội bộ.
- **Liên kết:** [Module 13 - Hacking web Servers/13_Hacking_Web_Servers.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2013%20Hacking%20Web%20Servers.md)

#### Câu 88 [Module 13]
Công cụ dòng lệnh chuyên quét bảo mật máy chủ web, phát hiện các tệp nguy hiểm tồn tại mặc định, phần mềm máy chủ lỗi thời và các vấn đề cấu hình sai là:
- A. Nikto
- B. Wireshark
- C. Ghidra
- D. John the Ripper
- **Đáp án:** A
- **Giải thích:** Nikto là máy quét mã nguồn mở thực hiện kiểm tra hơn 6700 tệp tin/chương trình nguy hiểm tiềm ẩn và cấu hình sai phổ biến trên máy chủ web.
- **Liên kết:** [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md)

---

### MODULE 14: HACKING WEB APPLICATIONS

#### Câu 89 [Module 14]
Loại lỗ hổng **Cross-Site Scripting (XSS)** nào lưu trữ mã độc vĩnh viễn trong cơ sở dữ liệu máy chủ (ví dụ trong phần bình luận bài viết) và thực thi trên trình duyệt của bất kỳ người dùng nào ghé thăm trang web đó?
- A. Reflected XSS
- B. Stored XSS (hoặc Persistent XSS)
- C. DOM-based XSS
- D. Blind XSS
- **Đáp án:** B
- **Giải thích:** Stored XSS xảy ra khi dữ liệu đầu vào chứa mã độc không được lọc và lưu trực tiếp vào cơ sở dữ liệu. Bất kỳ ai xem bản ghi này đều bị tải và thực thi payload mã độc trên trình duyệt.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 90 [Module 14]
Trong lỗ hổng **DOM-based XSS**, luồng thực thi của payload mã độc diễn ra ở đâu?
- A. Hoàn toàn tại máy chủ web backend
- B. Hoàn toàn tại môi trường JavaScript của trình duyệt người dùng (phía client), không nhất thiết phải gửi payload lên máy chủ
- C. Trên thiết bị định tuyến Router
- D. Trong cơ sở dữ liệu MySQL
- **Đáp án:** B
- **Giải thích:** DOM XSS xuất hiện khi mã JavaScript phía client lấy dữ liệu từ một Source không an toàn (như `location.hash`) và ghi vào một Sink thực thi HTML/JS nguy hiểm (như `document.write` hoặc `innerHTML`) mà không thông qua xử lý của server.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 91 [Module 14]
Lỗ hổng **CSRF (Cross-Site Request Forgery)** lợi dụng cơ chế nào sau đây của trình duyệt web?
- A. Tự động đính kèm cookie xác thực hợp lệ của người dùng khi gửi yêu cầu tới trang web mục tiêu
- B. Khả năng dịch mã hợp ngữ x86
- C. Bộ nhớ cache DNS
- D. Cơ chế kiểm tra chính sách cùng nguồn gốc (Same-Origin Policy)
- **Đáp án:** A
- **Giải thích:** Trình duyệt tự động gửi cookie phiên kèm theo mọi request gửi tới tên miền đích (kể cả khi request đó xuất phát ngầm từ một iframe hoặc form ẩn trên một trang web độc hại của hacker), khiến server tưởng rằng đây là yêu cầu hợp lệ từ người dùng.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 92 [Module 14]
Giải pháp hữu hiệu và phổ biến nhất để triệt tiêu lỗ hổng CSRF trên các biểu mẫu web là gì?
- A. Sử dụng thuật toán mã hóa SHA-256 cho mật khẩu
- B. Triển khai Anti-CSRF Token ngẫu nhiên (hoặc Synchronizer Token Pattern) gắn liền với phiên người dùng và kiểm tra tính hợp lệ của token này trên mỗi yêu cầu thay đổi trạng thái phía server
- C. Chuyển toàn bộ phương thức POST sang GET
- D. Tắt giao thức HTTPS
- **Đáp án:** B
- **Giải thích:** CSRF Token là một chuỗi ngẫu nhiên, bí mật và duy nhất cho mỗi phiên. Trang web độc hại của kẻ tấn công không thể đọc được token này do hạn chế của SOP, do đó không thể giả mạo yêu cầu hợp lệ.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 93 [Module 14]
Lỗ hổng **SSRF (Server-Side Request Forgery)** cho phép kẻ tấn công điều khiển máy chủ web ứng dụng làm việc gì?
- A. Xóa bảng dữ liệu trong cơ sở dữ liệu
- B. Gửi các yêu cầu HTTP/giao thức mạng tùy ý tới các dịch vụ nội bộ (như `http://127.0.0.1` hoặc cloud metadata `http://169.254.169.254`) mà máy ngoài Internet không thể tiếp cận được
- C. Gửi email rác tới danh bạ khách hàng
- D. Đọc trộm mã nguồn ứng dụng qua Git
- **Đáp án:** B
- **Giải thích:** SSRF lợi dụng chức năng fetch URL của server (như tính năng nhập ảnh đại diện từ link ngoài, đọc webhook) để biến server thành bàn đạp tấn công mạng nội bộ hoặc trích xuất IAM credentials từ Cloud Metadata API.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 94 [Module 14]
Địa chỉ IP Magic IP nào thường được các dịch vụ điện toán đám mây như AWS EC2, GCP, Azure sử dụng để cung cấp Instance Metadata Service (IMDS)?
- A. `192.168.1.1`
- B. `169.254.169.254` (Link-Local IP)
- C. `10.0.0.1`
- D. `127.0.0.1`
- **Đáp án:** B
- **Giải thích:** Địa chỉ link-local `169.254.169.254` là endpoint chuẩn của Cloud Metadata. Kẻ tấn công khai thác SSRF để truy vấn `http://169.254.169.254/latest/meta-data/iam/security-credentials/` nhằm đánh cắp AWS Access Keys.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 95 [Module 14]
Lỗ hổng **IDOR (Insecure Direct Object References)**, hay theo chuẩn OWASP API Security là **BOLA (Broken Object Level Authorization)**, xảy ra khi:
- A. Ứng dụng để lộ khóa bí mật trong mã nguồn
- B. Ứng dụng cho phép người dùng truy cập trực tiếp vào đối tượng tài nguyên (như hồ sơ, hóa đơn qua tham số `?user_id=105`) chỉ bằng cách thay đổi ID mà không kiểm tra xem người dùng đó có quyền sở hữu đối tượng hay không
- C. Máy chủ web bị lỗi phần cứng ổ cứng
- D. Token JWT bị hết hạn
- **Đáp án:** B
- **Giải thích:** BOLA/IDOR xảy ra do thiếu cơ chế kiểm tra quyền truy cập ở mức đối tượng (Object-level authorization check). Kẻ tấn công thay đổi ID để xem và chỉnh sửa dữ liệu của bất kỳ người dùng nào khác.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 96 [Module 14]
Chính sách bảo mật trình duyệt web **SOP (Same-Origin Policy)** xác định hai URL có "cùng nguồn gốc" khi chúng thỏa mãn tiêu chí nào?
- A. Cùng địa chỉ IP và hệ điều hành
- B. Cùng Giao thức (Protocol), cùng Tên miền (Host/Domain), và cùng Cổng (Port)
- C. Cùng tên tệp chỉ mục
- D. Cùng thuộc mạng LAN
- **Đáp án:** B
- **Giải thích:** Bộ ba Scheme + Host + Port bắt buộc phải trùng khớp hoàn toàn để hai trang web được coi là cùng origin. Nếu khác dù chỉ là port hoặc giao thức (http vs https), script của một trang không thể đọc dữ liệu của trang kia.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 97 [Module 14]
Cơ chế nào cho phép một máy chủ web nới lỏng chính sách SOP một cách có kiểm soát để các ứng dụng phía client tại tên miền khác có thể gửi yêu cầu API đọc tài nguyên?
- A. CSP (Content Security Policy)
- B. CORS (Cross-Origin Resource Sharing)
- C. HSTS (HTTP Strict Transport Security)
- D. X-Frame-Options
- **Đáp án:** B
- **Giải thích:** CORS sử dụng các tiêu đề HTTP như `Access-Control-Allow-Origin: https://client.example.com` để thông báo cho trình duyệt web cho phép chia sẻ tài nguyên giữa các domain khác nhau.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 98 [Module 14]
Tiêu đề HTTP nào được sử dụng để ngăn chặn tấn công **Clickjacking** bằng cách cấm trình duyệt nhúng trang web vào thẻ `<iframe>` của bên thứ ba?
- A. `X-Content-Type-Options: nosniff`
- B. `X-Frame-Options: DENY` (hoặc cấu hình CSP `frame-ancestors 'none'`)
- C. `Server: Apache`
- D. `Strict-Transport-Security`
- **Đáp án:** B
- **Giải thích:** `X-Frame-Options: DENY` chặn trang web bị render trong bất kỳ frame/iframe nào, ngăn kẻ tấn công tạo lớp phủ trong suốt lừa người dùng nhấp chuột (Clickjacking).
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

---

### MODULE 15: SQL INJECTION (SQLi)

#### Câu 99 [Module 15]
Kỹ thuật **Union-based SQL Injection** yêu cầu hai điều kiện tiên quyết nào để kẻ tấn công có thể ghép dữ liệu từ bảng khác vào kết quả trả về của ứng dụng?
- A. Ứng dụng phải dùng PostgreSQL và có quyền admin
- B. Câu lệnh SELECT tiêm vào phải có cùng số lượng cột với câu lệnh SELECT ban đầu, và các kiểu dữ liệu của các cột tương ứng phải tương thích với nhau
- C. Máy chủ web phải chạy trên hệ điều hành Linux
- D. Bảng dữ liệu phải có ít nhất 1000 bản ghi
- **Đáp án:** B
- **Giải thích:** Cú pháp toán tử `UNION` trong chuẩn SQL yêu cầu cả hai tập hợp kết quả phải có cùng số cột và kiểu dữ liệu ở các cột tương ứng phải tương đồng.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 100 [Module 15]
Khi ứng dụng web hoàn toàn không in bất kỳ dữ liệu truy vấn nào cũng như thông báo lỗi database ra màn hình (Blind SQL Injection), hacker có thể sử dụng kỹ thuật nào sau đây để trích xuất từng ký tự của dữ liệu dựa trên độ trễ phản hồi của máy chủ?
- A. Time-based Blind SQL Injection (sử dụng các hàm như `SLEEP(5)` hoặc `WAITFOR DELAY '0:0:5'`)
- B. Error-based SQL Injection
- C. Union-based SQL Injection
- D. FastCGI Injection
- **Đáp án:** A
- **Giải thích:** Time-based Blind SQLi đặt câu hỏi dạng boolean kết hợp hàm trễ: "Nếu ký tự đầu của mật khẩu là 'a', hãy ngủ 5 giây; ngược lại trả về ngay lập tức". Dựa vào thời gian phản hồi của server, hacker suy luận chính xác từng byte.
- **Liên kết:** [SQLMap_Injection_CheatSheet_v1.0.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SQLMap_Injection_CheatSheet_v1.0.pdf)

#### Câu 101 [Module 15]
Biện pháp kỹ thuật cốt lõi và triệt để nhất để phòng chống mọi hình thức SQL Injection trong phát triển phần mềm là gì?
- A. Mã hóa toàn bộ cơ sở dữ liệu bằng BitLocker
- B. Sử dụng Parameterized Queries (Truy vấn tham số hóa / Prepared Statements) hoặc Object-Relational Mapping (ORM) an toàn
- C. Sử dụng hàm lọc regex xóa bỏ dấu cách
- D. Chạy cơ sở dữ liệu trên cổng phi chuẩn
- **Đáp án:** B
- **Giải thích:** Prepared Statements tách bạch hoàn toàn phần mã lệnh SQL và phần dữ liệu do người dùng truyền vào. Database Engine biên dịch cấu trúc câu lệnh trước, dữ liệu người dùng được xử lý như tham số thuần túy và không bao giờ bị hiểu nhầm thành lệnh thực thi.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 102 [Module 15]
Trong cơ sở dữ liệu Microsoft SQL Server (MSSQL), thủ tục lưu trữ mở rộng nguy hiểm nào cho phép người dùng có quyền quản trị (sa) thực thi trực tiếp các lệnh hệ điều hành Windows (cmd.exe)?
- A. `sp_configure`
- B. `xp_cmdshell`
- C. `xp_regread`
- D. `sp_executesql`
- **Đáp án:** B
- **Giải thích:** `xp_cmdshell` là thủ tục mở rộng của MSSQL cho phép thực thi lệnh shell với đặc quyền của tài khoản chạy dịch vụ SQL Server (thường là Network Service hoặc SYSTEM).
- **Liên kết:** [SQLMap_Injection_CheatSheet_v1.0.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SQLMap_Injection_CheatSheet_v1.0.pdf)

#### Câu 103 [Module 15]
Payload SQL Injection kinh điển `' OR '1'='1` hoạt động như thế nào trong mệnh đề xác thực `WHERE username = '$user' AND password = '$pass'`?
- A. Gây lỗi cú pháp ép database khởi động lại
- B. Biến toàn bộ biểu thức điều kiện WHERE thành luôn đúng (True), khiến câu lệnh trả về bản ghi người dùng đầu tiên (thường là Quản trị viên/admin) mà không cần mật khẩu
- C. Tự động mã hóa mật khẩu người dùng
- D. Đóng kết nối mạng của máy chủ
- **Đáp án:** B
- **Giải thích:** Toán tử logic OR có điều kiện `'1'='1'` luôn trả về giá trị Chân trị (True), vô hiệu hóa hoàn toàn điều kiện kiểm tra mật khẩu phía sau.
- **Liên kết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md)

#### Câu 104 [Module 15]
Bảng hệ thống tiêu chuẩn nào trong MySQL/MariaDB chứa siêu dữ liệu danh sách tất cả các bảng và cột của toàn bộ cơ sở dữ liệu trên máy chủ?
- A. `INFORMATION_SCHEMA.TABLES` và `INFORMATION_SCHEMA.COLUMNS`
- B. `sys.all_objects`
- C. `pg_catalog.pg_tables`
- D. `mysql.user`
- **Đáp án:** A
- **Giải thích:** `INFORMATION_SCHEMA` là schema theo chuẩn ANSI SQL lưu trữ metadata về các database, bảng (`TABLE_NAME`) và cột (`COLUMN_NAME`), là mục tiêu khai thác đầu tiên của hacker để lập bản đồ cấu trúc DB.
- **Liên kết:** [SQLMap_Injection_CheatSheet_v1.0.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SQLMap_Injection_CheatSheet_v1.0.pdf)

#### Câu 105 [Module 15]
Tham số nào trong công cụ tự động hóa `sqlmap` được sử dụng để lấy một tương tác hệ điều hành shell trực tiếp (thông qua kỹ thuật ghi Webshell hoặc xp_cmdshell)?
- A. `--dbs`
- B. `--os-shell`
- C. `--dump`
- D. `--batch`
- **Đáp án:** B
- **Giải thích:** `--os-shell` yêu cầu sqlmap tự động tìm cách tải webshell lên webroot hoặc kích hoạt `xp_cmdshell` để cung cấp shell điều khiển hệ điều hành cho pentester.
- **Liên kết:** [SQLMap_Injection_CheatSheet_v1.0.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SQLMap_Injection_CheatSheet_v1.0.pdf)

---

### MODULE 16: HACKING WIRELESS NETWORKS

#### Câu 106 [Module 16]
Giao thức bảo mật mạng không dây nào sử dụng thuật toán mã hóa dòng RC4 với Vector khởi tạo (IV) chỉ có độ dài 24-bit, dẫn đến việc bị bẻ khóa mật khẩu chỉ trong vài phút?
- A. WPA3-Personal
- B. WPA2-Enterprise
- C. WEP (Wired Equivalent Privacy)
- D. WPA-PSK (TKIP)
- **Đáp án:** C
- **Giải thích:** Chuẩn WEP có không gian khóa IV quá nhỏ (24-bit), làm cho các giá trị IV bị lặp lại sau một số lượng gói tin nhất định. Thuật toán FMS/PTW cho phép tính toán ngược khóa gốc WEP từ các gói tin trùng lặp thu được.
- **Liên kết:** [Module 16 - Wireless Networks.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2016%20Hacking%20Wireless%20Networks.md)

#### Câu 107 [Module 16]
Để bẻ khóa mật khẩu mạng Wi-Fi bảo vệ bằng chuẩn **WPA/WPA2-PSK (Pre-Shared Key)** offline bằng từ điển (Dictionary Attack), hacker bắt buộc phải bắt giữ (sniff) được chuỗi trao đổi gói tin nào?
- A. Quá trình bắt tay 4 bước WPA (EAPOL 4-Way Handshake)
- B. Gói tin DHCP Discover
- C. Bản ghi DNS TXT
- D. Gói tin ARP Request
- **Đáp án:** A
- **Giải thích:** 4-Way Handshake chứa ANonce, SNonce và MIC (Message Integrity Code). Hacker sử dụng từ điển mật khẩu để tính toán PMK/PTK và so sánh MIC để xác định mật khẩu đúng mà không cần kết nối tới Access Point.
- **Liên kết:** [Module 16 - Wireless Networks.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2016%20Hacking%20Wireless%20Networks.md)

#### Câu 108 [Module 16]
Cuộc tấn công nào gửi các khung dữ liệu ngắt kết nối giả mạo (Deauthentication Frames) tới máy trạm của nạn nhân nhằm ép máy trạm phải ngắt kết nối và thực hiện kết nối lại với Access Point để hacker thu thập gói bắt tay?
- A. Deauthentication Attack (Deauth Attack)
- B. Beacon Flooding
- C. WPS Brute-force
- D. Evil Twin Attack
- **Đáp án:** A
- **Giải thích:** Trong chuẩn IEEE 802.11 bản cũ, các khung quản lý (Management Frames như Deauth) không được mã hóa hay ký xác thực. Hacker giả mạo địa chỉ MAC của Access Point để ép client ngắt kết nối tức thời.
- **Liên kết:** [Module 16 - Wireless Networks.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2016%20Hacking%20Wireless%20Networks.md)

#### Câu 109 [Module 16]
Kỹ thuật **Evil Twin Attack** trong mạng không dây được thực hiện như thế nào?
- A. Đặt bom xung điện từ làm hỏng anten Wi-Fi
- B. Hacker thiết lập một Access Point giả mạo phát cùng tên SSID và cùng địa chỉ MAC với AP hợp lệ của tổ chức nhưng với cường độ sóng mạnh hơn để lừa các máy trạm kết nối vào AP giả này
- C. Xâm nhập vào tổng đài điện thoại
- D. Quét cổng qua Bluetooth
- **Đáp án:** B
- **Giải thích:** Evil Twin ngụy trang hoàn hảo thành Access Point hợp lệ. Khi máy trạm tự động chuyển vùng (roaming) sang AP có tín hiệu mạnh hơn của hacker, mọi lưu lượng mạng sẽ bị hacker nghe lén hoặc đưa về Captive Portal giả để thu thập mật khẩu.
- **Liên kết:** [Module 16 - Wireless Networks.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2016%20Hacking%20Wireless%20Networks.md)

#### Câu 110 [Module 16]
Lỗ hổng thiết kế nghiêm trọng trong tính năng kết nối nhanh **WPS (Wi-Fi Protected Setup)** sử dụng mã PIN 8 chữ số cho phép công cụ nào sau đây bẻ khóa mã PIN chỉ sau vài giờ?
- A. Reaver (hoặc Bully)
- B. Wireshark
- C. Nmap
- D. Burp Suite
- **Đáp án:** A
- **Giải thích:** WPS PIN gồm 8 chữ số nhưng số cuối là checksum, và Access Point xác thực 4 số đầu và 3 số sau độc lập với nhau. Tổng số khả năng chỉ là 10,000 + 1,000 = 11,000 lần thử, giúp công cụ Reaver giải mã trong thời gian rất ngắn.
- **Liên kết:** [Module 16 - Wireless Networks.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2016%20Hacking%20Wireless%20Networks.md)

#### Câu 111 [Module 16]
Chuẩn bảo mật thế hệ mới **WPA3** thay thế cơ chế bắt tay 4 bước PSK dễ bị tấn công từ điển bằng giao thức trao đổi khóa an toàn nào sau đây?
- A. SAE (Simultaneous Authentication of Equals - Dragonfly Handshake)
- B. WEP Key Exchange
- C. Cleartext Token
- D. Kerberos AS-REQ
- **Đáp án:** A
- **Giải thích:** SAE (dựa trên thuật toán trao đổi khóa Diffie-Hellman) cung cấp tính năng Forward Secrecy và triệt tiêu khả năng tấn công vét cạn từ điển offline, kể cả khi mật khẩu người dùng đơn giản.
- **Liên kết:** [Module 16 - Wireless Networks.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2016%20Hacking%20Wireless%20Networks.md)

---

### MODULE 17: HACKING MOBILE PLATFORMS

#### Câu 112 [Module 17]
Cơ chế bảo mật nền tảng của hệ điều hành Android thực thi mỗi ứng dụng trong một không gian người dùng Linux độc lập (UID riêng biệt) được gọi là:
- A. Application Sandboxing
- B. Rooting
- C. Sideloading
- D. Debug Mode
- **Đáp án:** A
- **Giải thích:** Android gán cho mỗi ứng dụng cài đặt một UID Linux duy nhất. Sandbox bảo đảm ứng dụng không thể đọc hoặc can thiệp vào tệp dữ liệu và bộ nhớ của ứng dụng khác trừ khi được cấp quyền rõ ràng.
- **Liên kết:** [Module 17 - Mobile Platform/17_Hacking_Mobile_Platforms.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2017%20Hacking%20Mobile%20Platforms.md)

#### Câu 113 [Module 17]
Tệp cấu hình bắt buộc nào trong ứng dụng Android (`.apk`) khai báo toàn bộ các quyền hạn (permissions), các Activity, Service, Broadcast Receiver và Content Provider của ứng dụng?
- A. `AndroidManifest.xml`
- B. `classes.dex`
- C. `resources.arsc`
- D. `build.gradle`
- **Đáp án:** A
- **Giải thích:** `AndroidManifest.xml` là tệp mô tả cấu trúc và chính sách bảo mật cốt lõi của ứng dụng Android, là mục tiêu phân tích đầu tiên của pentester khi dịch ngược file APK.
- **Liên kết:** [Module 17 - Mobile Platform/17_Hacking_Mobile_Platforms.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2017%20Hacking%20Mobile%20Platforms.md)

#### Câu 114 [Module 17]
Công cụ dịch ngược mã nguồn Android nào chuyển đổi tệp bytecode `classes.dex` thành mã Java/Smali gần gũi với mã nguồn gốc của lập trình viên?
- A. Jadx (hoặc Apktool)
- B. Wireshark
- C. OpenVAS
- D. Metasploit
- **Đáp án:** A
- **Giải thích:** Jadx giải dịch ngược mã Dalvik bytecode (.dex) sang mã nguồn Java có thể đọc được; Apktool giải nén tài nguyên và mã assembly Smali.
- **Liên kết:** [Module 17 - Mobile Platform/17_Hacking_Mobile_Platforms.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2017%20Hacking%20Mobile%20Platforms.md)

#### Câu 115 [Module 17]
Hành động can thiệp vào hệ điều hành iOS của Apple nhằm gỡ bỏ cơ chế bảo vệ chữ ký mã (Code Signing enforcement) và sandbox để cấp quyền truy cập root cho người dùng được gọi là:
- A. Jailbreaking
- B. Sideloading
- C. Over-The-Air Update
- D. Phishing
- **Đáp án:** A
- **Giải thích:** Jailbreaking khai thác các lỗ hổng kernel iOS để vô hiệu hóa sandbox và cơ chế kiểm tra chữ ký bắt buộc của Apple, cho phép người dùng cài đặt ứng dụng từ các nguồn bên ngoài App Store (như Cydia).
- **Liên kết:** [Module 17 - Mobile Platform/17_Hacking_Mobile_Platforms.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2017%20Hacking%20Mobile%20Platforms.md)

#### Câu 116 [Module 17]
Framework mã nguồn mở chuyên dùng để hooking vào bộ nhớ runtime của các ứng dụng di động (Android và iOS), giúp bypass SSL Pinning và phát hiện Root/Jailbreak theo thời gian thực là:
- A. Frida
- B. Nmap
- C. Nessus
- D. Snort
- **Đáp án:** A
- **Giải thích:** Frida là công cụ Dynamic Binary Instrumentation (DBI) cho phép pentester tiêm mã JavaScript vào không gian bộ nhớ của tiến trình mobile để thay đổi giá trị trả về của các hàm kiểm tra bảo mật.
- **Liên kết:** [Module 17 - Mobile Platform/17_Hacking_Mobile_Platforms.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2017%20Hacking%20Mobile%20Platforms.md)

---

### MODULE 18: IoT & OT HACKING

#### Câu 117 [Module 18]
Giao thức truyền thông nhắn tin nhẹ (lightweight publish-subscribe) thường xuyên được sử dụng trong các hệ sinh thái thiết bị IoT và xe tự hành kết nối qua cổng TCP 1883 là:
- A. MQTT (Message Queuing Telemetry Transport)
- B. BGP
- C. OSPF
- D. NFS
- **Đáp án:** A
- **Giải thích:** MQTT là giao thức truyền thông điệp gọn nhẹ giữa các sensor và Broker. Mặc định trên cổng 1883 không bật mã hóa và xác thực, cho phép kẻ nghe lén thu thập toàn bộ dữ liệu telemetry nội bộ.
- **Liên kết:** [Module 18 - IOT Hacking/18_IoT_Hacking.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2018%20IoT%20and%20OT%20Hacking.md)

#### Câu 118 [Module 18]
Giao thức công nghiệp cổ điển trong hệ thống kiểm soát công nghiệp ICS/SCADA nào hoàn toàn không có bất kỳ cơ chế xác thực danh tính người gửi hay mã hóa gói tin, khiến việc gửi lệnh điều khiển giả mạo (như tắt van áp suất) cực kỳ dễ dàng?
- A. Modbus (Modbus TCP cổng 502)
- B. HTTPS
- C. SSH
- D. IPsec
- **Đáp án:** A
- **Giải thích:** Modbus được phát triển từ năm 1979 cho các mạng cô lập. Khi kết nối qua Ethernet (Modbus TCP), bất kỳ gói tin nào gửi tới cổng 502 với Function Code hợp lệ đều được PLC thực thi mà không kiểm tra người gửi.
- **Liên kết:** [Module 18 - IOT Hacking/18_IoT_Hacking.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2018%20IoT%20and%20OT%20Hacking.md)

#### Câu 119 [Module 18]
Công cụ dòng lệnh trên Linux chuyên dùng để phân tích và trích xuất cấu trúc hệ thống tệp (file system như SquashFS, CramFS) từ tệp nhị phân Firmware của thiết bị IoT là:
- A. `binwalk`
- B. `curl`
- C. `netcat`
- D. `tcpdump`
- **Đáp án:** A
- **Giải thích:** `binwalk` quét các header ma thuật (magic bytes) bên trong file firmware nhị phân để tự động giải nén hạt nhân Linux và hệ thống tệp chứa mật khẩu mặc định hoặc backdoor.
- **Liên kết:** [Module 18 - IOT Hacking/18_IoT_Hacking.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2018%20IoT%20and%20OT%20Hacking.md)

#### Câu 120 [Module 18]
Giao diện phần cứng vật lý nào trên bo mạch mạch in (PCB) của thiết bị IoT thường được các kỹ sư dùng để debug và cho phép hacker cắm thiết bị chuyển đổi UART/JTAG để lấy quyền Root Shell trực tiếp?
- A. Cổng UART (Universal Asynchronous Receiver-Transmitter) và JTAG
- B. Đầu nối HDMI
- C. Cổng VGA
- D. Jack tai nghe 3.5mm
- **Đáp án:** A
- **Giải thích:** Các chân UART (TX, RX, GND, VCC) và JTAG trên bo mạch thường cung cấp console nối tiếp không đòi hỏi mật khẩu khi bootloader tải, cho phép truy cập shell hệ thống ngay lập tức.
- **Liên kết:** [Module 18 - IOT Hacking/18_IoT_Hacking.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2018%20IoT%20and%20OT%20Hacking.md)

---

### MODULE 19: CLOUD COMPUTING & VIRTUALIZATION

#### Câu 121 [Module 19]
Trong mô hình trách nhiệm chia sẻ (Shared Responsibility Model) của điện toán đám mây cho mô hình **IaaS (Infrastructure as a Service)**, khách hàng chịu trách nhiệm bảo mật cho thành phần nào?
- A. Bảo vệ vật lý của trung tâm dữ liệu
- B. Hệ điều hành máy ảo (OS), Cập nhật bản vá (Patch management), Cấu hình mạng firewall (Security Groups) và Quyền hạn dữ liệu/IAM
- C. Phần cứng máy chủ vật lý
- D. Hệ thống điều hòa và nguồn điện UPS
- **Đáp án:** B
- **Giải thích:** Trong IaaS (như AWS EC2), nhà cung cấp đám mây chịu trách nhiệm bảo mật "of the cloud" (vật lý, hypervisor); khách hàng chịu trách nhiệm bảo mật "in the cloud" (hệ điều hành, ứng dụng, phân quyền và dữ liệu).
- **Liên kết:** [SANS_Cloud_Security_AWS_Azure_GCP.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SANS_Cloud_Security_AWS_Azure_GCP.pdf)

#### Câu 122 [Module 19]
Lỗi cấu hình phổ biến và nghiêm trọng nhất trên dịch vụ lưu trữ đối tượng đám mây như **Amazon S3** là gì?
- A. Cấp quyền truy cập công khai (Public Read/Write) cho nhóm người dùng `AllUsers` hoặc `AuthenticatedUsers` thông qua Bucket Policy sai lầm
- B. Sử dụng dung lượng lưu trữ quá 1 TB
- C. Đặt tên bucket quá ngắn
- D. Bật tính năng Versioning
- **Đáp án:** A
- **Giải thích:** S3 bucket bị cấu hình quyền Public Read/Write cho phép bất kỳ ai trên Internet tải xuống toàn bộ dữ liệu bí mật hoặc ghi đè mã độc vào các tệp tĩnh của trang web.
- **Liên kết:** [SANS_Cloud_Security_AWS_Azure_GCP.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SANS_Cloud_Security_AWS_Azure_GCP.pdf)

#### Câu 123 [Module 19]
Hiện tượng một tiến trình độc hại chạy bên trong một Container (như Docker) thoát ra ngoài và chiếm quyền điều khiển trực tiếp máy chủ Host vật lý được gọi là:
- A. Container Escape (hoặc Container Breakout)
- B. SQL Injection
- C. DNS Poisoning
- D. Cross-Origin Resource Sharing
- **Đáp án:** A
- **Giải thích:** Container Escape xảy ra khi container chạy ở chế độ đặc quyền nguy hiểm (`--privileged`), gắn socket máy chủ (`/var/run/docker.sock`) hoặc do lỗ hổng hạt nhân Linux (như Dirty COW).
- **Liên kết:** [SANS_Cloud_Security_AWS_Azure_GCP.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SANS_Cloud_Security_AWS_Azure_GCP.pdf)

#### Câu 124 [Module 19]
Tính năng bảo mật nào trong AWS Identity and Access Management (IAM) giúp hạn chế tối đa rủi ro lộ quyền bằng cách cung cấp quyền tạm thời tự động hết hạn thay vì dùng Access Key cố định dài hạn?
- A. AWS IAM Roles (sử dụng AWS STS để sinh session token ngắn hạn)
- B. Root Account Access Keys
- C. Cấu hình mật khẩu vĩnh viễn
- D. Bật giao thức FTP
- **Đáp án:** A
- **Giải thích:** IAM Role sử dụng AWS Security Token Service (STS) để phát hành credential tạm thời có hiệu lực ngắn (từ 15 phút đến vài giờ), triệt tiêu rủi ro lộ credential vĩnh viễn.
- **Liên kết:** [SANS_Cloud_Security_AWS_Azure_GCP.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SANS_Cloud_Security_AWS_Azure_GCP.pdf)

#### Câu 125 [Module 20: CRYPTOGRAPHY]
Thuật toán mật mã bất đối xứng (Asymmetric Cryptography) nào sau đây dựa trên độ khó của bài toán phân tích một số nguyên cực lớn thành tích của hai số nguyên tố bí mật?
- A. AES (Advanced Encryption Standard)
- B. RSA (Rivest-Shamir-Adleman)
- C. DES (Data Encryption Standard)
- D. RC4
- **Đáp án:** B
- **Giải thích:** RSA dựa trên tính bất khả thi về mặt tính toán trong việc phân tích thừa số nguyên tố của các số có độ dài 2048 hoặc 4096-bit. AES và DES là mật mã đối xứng khối (Symmetric Block Cipher); RC4 là mật mã đối xứng dòng.
- **Liên kết:** [Module 20 - Cryptography/20_Cryptography.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2020%20Cryptography.md)

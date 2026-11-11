# ĐỀ CƯƠNG BÀI GIẢNG: NHẬP MÔN MẠNG MÁY TÍNH & INTERNET
## (Introduction to Computer Networking: How the Internet Works)

*Dựa trên tác phẩm kinh điển của GS. Charles Severance (Dr. Chuck) – Đại học Michigan*  
*Ngôn ngữ giảng dạy: Tiếng Việt kết hợp thuật ngữ Kỹ thuật Mạng Chuẩn Quốc tế (Standard English Terms)*

---

## 1. THÔNG TIN CHUNG VỀ KHÓA HỌC (COURSE OVERVIEW)

- **Tên khóa học:** Nhập môn Mạng Máy tính và Nguyên lý Hoạt động của Internet
- **Mã môn học dự kiến:** NET101 / CS-NET
- **Thời lượng:** 4 Buổi học (tương đương 16 Tiết học học thuật: 10 tiết Lý thuyết chuyên sâu + 6 tiết Thực hành Lab).
- **Đối tượng học viên:** 
  - Sinh viên chuyên ngành Công nghệ thông tin, Khoa học máy tính, An toàn thông tin (Cybersecurity).
  - Kỹ sư phần mềm, DevOps, Quản trị hệ thống (System Administrator) muốn nắm vững bản chất cốt lõi của hạ tầng mạng.
- **Triết lý giảng dạy (Dr. Chuck's Pedagogy):**  
  *Học mạng từ dưới lên trên và từ trong ra ngoài (De-mystifying the Internet).* Không biến mạng máy tính thành một tập hợp trừu tượng các tiêu chuẩn viễn thông phức tạp, khóa học tái hiện lại hành trình lịch sử đầy trí tuệ: từ bài toán kết nối điện thoại thoại chuyển mạch kênh (Circuit Switching), đến bước đột phá chuyển mạch gói (Packet Switching), cơ chế đóng gói dữ liệu (Encapsulation), và sự hình thành của các giao thức định hình thế giới số ngày nay.

---

## 2. MỤC TIÊU HỌC TẬP (LEARNING OBJECTIVES - BLOOM'S TAXONOMY)

Sau khi hoàn thành khóa học, học viên đạt được các năng lực cụ thể theo các cấp độ nhận thức của Thang đo Bloom:

### 2.1. Cấp độ Nhớ (Remembering)
- Nêu được định nghĩa và chức năng cốt lõi của 4 tầng trong mô hình kiến trúc **TCP/IP** (Link, Internet, Transport, Application) và 7 tầng trong mô hình **OSI**.
- Ghi nhớ cấu trúc định dạng của các loại địa chỉ mạng căn bản: **Địa chỉ MAC** (48-bit), **Địa chỉ IPv4** (32-bit), **Địa chỉ IPv6** (128-bit) và **Cổng dịch vụ (Port Number)** (16-bit).
- Liệt kê được các dải địa chỉ IP riêng tư (**Private IP Addresses**) theo chuẩn RFC 1918 và các cổng chuẩn (Well-known Ports: 80, 443, 22, 53, 993).
- Định nghĩa chính xác các thành phần trong hạ tầng **DNS** (Root Nameservers, TLD Servers, Authoritative Servers, Resolver).

### 2.2. Cấp độ Hiểu (Understanding)
- Phân biệt sự khác biệt bản chất giữa **Chuyển mạch kênh (Circuit Switching)** và **Chuyển mạch gói (Packet Switching)** về hiệu quả sử dụng tài nguyên đường truyền.
- Giải thích cơ chế **Đóng gói (Encapsulation)** và **Mở gói (Decapsulation)** dữ liệu qua các tầng: Dữ liệu (Data) $\rightarrow$ Đoạn (Segment) $\rightarrow$ Gói tin (Packet) $\rightarrow$ Khung (Frame).
- Hiểu rõ nguyên lý vận hành của cơ chế kiểm soát lỗi và kiểm soát luồng của TCP: **Bắt tay ba bước (Three-way Handshake)**, **Số thứ tự (Sequence Number)**, **Gói báo nhận (ACK)**, và **Cửa sổ trượt (Sliding Window)**.
- Phân biệt cơ chế hoạt động của **Mã hóa đối xứng (Symmetric Encryption)** và **Mã hóa bất đối xứng (Asymmetric Encryption)**, cùng vai trò của **Tổ chức cấp phát chứng chỉ số (Certificate Authority - CA)** trong chuỗi tin cậy (Chain of Trust) của giao thức TLS/SSL.

### 2.3. Cấp độ Áp dụng (Applying)
- Tính toán và phân chia dải mạng con (Subnetting) cơ bản; cấu hình và kiểm tra hoạt động của bảng định tuyến tĩnh trên Router.
- Sử dụng thành thạo các công cụ phân tích dòng lệnh mạng tiêu chuẩn: `ping`, `traceroute` (`tracert`), `nslookup`, `dig`, `netstat`, `curl`.
- Sử dụng phần mềm **Wireshark** để bắt gói tin thực tế trên card mạng; giải mã và chỉ ra các trường Header (Ethernet, IPv4, TCP, HTTP) của một luồng truyền dữ liệu.
- Viết ứng dụng mạng Client/Server cơ bản bằng ngôn ngữ Python sử dụng thư viện **Socket**, tự tay tạo bản tin HTTP Request thô và đọc phản hồi từ Web Server.

### 2.4. Cấp độ Phân tích & Đánh giá (Analyzing & Evaluating)
- Phân tích nguyên nhân gây ra vòng lặp định tuyến (Routing Loop) và chứng minh vai trò ngăn ngừa sụp đổ mạng của trường **TTL (Time to Live)** trong gói tin IP.
- Phân tích cơ chế hoạt động của công cụ `traceroute` dựa trên việc cố tình gửi gói tin có TTL tăng dần để kích hoạt thông điệp lỗi **ICMP Time Exceeded**.
- So sánh đánh giá ưu nhược điểm kỹ thuật giữa **TCP** (độ tin cậy cao, hướng kết nối, overhead lớn) và **UDP** (tốc độ cao, phi kết nối, không đảm bảo thứ tự) để lựa chọn giao thức tối ưu cho các bài toán truyền phát video thời gian thực (VoIP, Video Streaming), chơi game online, hay truyền file tin cậy.
- Đánh giá vai trò của **NAT (Network Address Translation)** trong việc kéo dài vòng đời IPv4 và những ảnh hưởng phụ (Side-effects) của nó đối với các kết nối ngang hàng (Peer-to-Peer).

---

## 3. PHÂN BỔ THỜI LƯỢNG KHÓA HỌC (TIME BREAKDOWN)

Khóa học được cấu trúc thành **4 Buổi học (Sessions)**, mỗi buổi gồm 4 tiết học thuật (45 phút/tiết). Tổng cộng 16 tiết học:

| Buổi | Tên Chuyên Đề | Thời Lượng | Nội Dung Cốt Lõi | Hình Thức |
| :--- | :--- | :--- | :--- | :--- |
| **Buổi 1** | **Nền tảng Mạng: Lịch sử, Đóng gói & Tầng Liên kết** | 4 Tiết (3h) | - Tiến trình từ Mạng Viễn thông đến Mạng Gói.<br>- Kiến trúc TCP/IP 4 tầng & Quá trình Encapsulation.<br>- Tầng Liên kết: Môi trường chia sẻ, CSMA/CD, MAC & Ethernet. | Lý thuyết & Thảo luận tình huống |
| **Buổi 2** | **Tầng Mạng (IP), Định tuyến & Hệ thống DNS** | 4 Tiết (3h) | - Địa chỉ IPv4/IPv6, Phân đoạn mạng.<br>- Định tuyến Hop-by-Hop, Vòng lặp gói tin & Cơ chế TTL.<br>- Cấp phát DHCP & Kỹ thuật NAT (RFC 1918).<br>- Kiến trúc Cây phân cấp DNS & Quy trình phân giải đệ quy. | Lý thuyết (2 Tiết) + **Lab 1: Traceroute & DNS Inspection** (2 Tiết) |
| **Buổi 3** | **Tầng Giao vận (TCP/UDP) & Kiểm soát luồng** | 4 Tiết (3h) | - Khái niệm Cổng (Port) & Đa hợp kênh (Multiplexing).<br>- So sánh TCP vs UDP.<br>- Bắt tay 3 bước TCP (SYN, SYN-ACK, ACK).<br>- Cơ chế Cửa sổ trượt (Sliding Window) & Kiểm soát luồng. | Lý thuyết (2 Tiết) + **Lab 2: Phân tích Gói tin với Wireshark** (2 Tiết) |
| **Buổi 4** | **Tầng Ứng dụng, Sockets, Bảo mật TLS & Mô hình OSI** | 4 Tiết (3h) | - Mô hình Client/Server, Giao thức HTTP/1.1 & IMAP.<br>- Lập trình mạng với Berkeley Sockets.<br>- Mật mã học, Khóa công khai/riêng tư & Bắt tay TLS/SSL.<br>- Đối chiếu toàn diện mô hình TCP/IP và mô hình OSI 7 tầng. | Lý thuyết (2 Tiết) + **Lab 3: Python Socket & Raw HTTP Client** (2 Tiết) |

---

## 4. ĐỀ CƯƠNG CHI TIẾT TỪNG MODULE (MODULE-BY-MODULE SYLLABUS)

### MODULE 1: TỪ ĐIỆN THOẠI ĐẾN MẠNG MÁY TÍNH – CHUYỂN MẠCH GÓI (PACKET SWITCHING)
- **1.1. Bài toán truyền thông khoảng cách xa:**
  - Giới hạn của mô hình kết nối vật lý điểm-điểm (Point-to-Point) giữa từng cặp người dùng: Bài toán bùng nổ đường dây $\frac{N(N-1)}{2}$.
  - Sự ra đời của Tổng đài trung tâm và Tổng đài viên (Switchboard Operator).
- **1.2. Mạng Chuyển mạch kênh (Circuit Switching):**
  - Nguyên lý hoạt động: Thiết lập kênh vật lý chuyên biệt và cố định trong suốt cuộc gọi.
  - Phân tích hiệu suất: Lãng phí băng thông nghiêm trọng trong truyền thông dữ liệu máy tính (do lưu lượng máy tính có tính đột biến - Bursty Traffic).
- **1.3. Cuộc cách mạng Chuyển mạch gói (Packet Switching):**
  - Khái niệm Gói tin (Packet) và Bộ định tuyến (Router).
  - Phép ẩn dụ "Bưu thiếp và Hệ thống Bưu điện" của Dr. Chuck.
  - Xếp hàng (Queuing), Ghép kênh theo thời gian thống kê (Statistical Multiplexing).
  - Tự thích ứng khi có sự cố đứt tuyến: Khả năng tự định tuyến lại qua các trạm trung gian.

### MODULE 2: KIẾN TRÚC PHÂN TẦNG TCP/IP & ĐÓNG GÓI DỮ LIỆU (ENCAPSULATION)
- **2.1. Triết lý kiến trúc Internet:**
  - Nguyên lý thiết kế Đầu-cuối (End-to-End Principle): Mạng lõi đơn giản, trí thông minh nằm ở thiết bị rìa.
  - Tính mô-đun hóa và trừu tượng hóa: Các tầng độc lập, giao diện trao đổi dữ liệu chuẩn tắc.
- **2.2. Mô hình 4 tầng TCP/IP (The 4-Layer Internet Model):**
  - Tầng Liên kết (Link Layer).
  - Tầng Mạng / Liên mạng (Internet Layer - IP).
  - Tầng Giao vận (Transport Layer - TCP/UDP).
  - Tầng Ứng dụng (Application Layer).
- **2.3. Quy trình Đóng gói (Encapsulation) & Mở gói (Decapsulation):**
  - Phép ẩn dụ "Búp bê Matryoshka" và những bức thư lồng phong bì.
  - Header, Payload và Trailer qua từng tầng: Application Data $\rightarrow$ TCP Segment (Port) $\rightarrow$ IP Packet (IP Address) $\rightarrow$ Ethernet Frame (MAC Address + FCS/CRC).

### MODULE 3: TẦNG LIÊN KẾT (LINK LAYER) – MÔI TRƯỜNG CHIA SẺ & ĐỊA CHỈ MAC
- **3.1. Bài toán chia sẻ môi trường truyền dẫn (Shared Media):**
  - Phép ẩn dụ 5 người trong phòng kín nói chuyện cùng lúc.
  - Mạng Ethernet sơ khai (Dây cáp đồng trục chia sẻ - Coaxial Bus) và sóng vô tuyến Wi-Fi.
- **3.2. Cơ chế kiểm soát truy cập môi trường:**
  - Giao thức **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection): Lắng nghe trước khi nói, phát hiện va chạm và thuật toán Lùi ngẫu nhiên (Exponential Backoff).
  - So sánh với mô hình luân phiên Token Ring.
- **3.3. Định danh Thiết bị cục bộ – Địa chỉ MAC:**
  - Cấu trúc địa chỉ MAC 48-bit (6 bytes), hiển thị dưới dạng Hexadecimal.
  - Phần OUI (Organizationally Unique Identifier) do IEEE cấp và số định danh card mạng (NIC).
  - Khung Ethernet (Ethernet Frame) và trường kiểm tra lỗi CRC/FCS (Frame Check Sequence).

### MODULE 4: TẦNG MẠNG (INTERNET LAYER) – ĐỊA CHỈ IP, ĐỊNH TUYẾN & NAT
- **4.1. Kiến trúc Địa chỉ IPv4:**
  - Định dạng số 32-bit (Dotted-decimal notation: 4 octets).
  - Phân vùng Địa chỉ: Network ID và Host ID; vai trò của Mặt nạ mạng con (Subnet Mask).
  - Địa chỉ IP Toàn cục (Public IP) vs Cạn kiệt địa chỉ IPv4; Tổng quan giải pháp IPv6 (128-bit).
- **4.2. Nguyên lý Định tuyến Hop-by-Hop:**
  - Router kiểm tra Header IP, tra cứu Bảng định tuyến (Routing Table) và quyết định Chặng nhảy tiếp theo (Next Hop).
  - Router không cần biết toàn bộ hành trình; chỉ cần biết cổng xuất tiếp theo tối ưu.
- **4.3. Chống vòng lặp và Trường TTL (Time to Live):**
  - Sự cố Bão định tuyến khi xuất hiện chu trình lặp vô hạn (Routing Loop).
  - Trường TTL (mặc định 64 hoặc 128): Giảm 1 đơn vị tại mỗi router; khi TTL = 0, gói tin bị hủy và router gửi thông báo lỗi **ICMP Time Exceeded**.
  - Phân tích cơ chế hoạt động của công cụ `traceroute` khai thác TTL.
- **4.4. Cấu hình IP Động (DHCP) & Kỹ thuật NAT:**
  - Giao thức DHCP (DORA: Discover - Offer - Request - Acknowledge).
  - Dải địa chỉ IP nội bộ RFC 1918 (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).
  - Biên dịch địa chỉ mạng (NAT / NAPT): Bảng ánh xạ cổng IP nội bộ và IP công cộng.

### MODULE 5: HỆ THỐNG PHÂN GIẢI TÊN MIỀN (DNS)
- **5.1. Nhu cầu định danh dạng văn bản thay cho số IP nhị phân:**
  - Sự dịch chuyển từ tệp tĩnh `hosts.txt` (thời ARPANET) đến cơ sở dữ liệu phân tán toàn cầu.
- **5.2. Cấu trúc hình cây phân cấp của Không gian Tên miền:**
  - Đọc tên miền từ phải sang trái: Dấu chấm gốc (`.`) $\rightarrow$ Top-Level Domain (TLD: `.com`, `.edu`, `.vn`) $\rightarrow$ Second-Level Domain $\rightarrow$ Subdomain.
  - Tổ chức ICANN và các nhà đăng ký tên miền (Registrars).
- **5.3. Quy trình Phân giải Tên miền (DNS Resolution Process):**
  - Vai trò của DNS Recursive Resolver (máy chủ phân giải đệ quy của ISP / Google 8.8.8.8 / Cloudflare 1.1.1.1).
  - 13 Cụm máy chủ Gốc (Root Servers: A đến M).
  - Máy chủ quản lý tên miền TLD và Máy chủ có thẩm quyền (Authoritative Nameserver).
  - Cơ chế Bộ nhớ đệm (DNS Caching) và chỉ số thời gian sống bản ghi (TTL).

### MODULE 6: TẦNG GIAO VẬN (TRANSPORT LAYER) – TCP VS UDP & KIỂM SOÁT LUỒNG
- **6.1. Đa hợp kênh và Khái niệm Cổng (Port Numbers):**
  - Địa chỉ IP định vị Máy tính (Host); Cổng (Port) định vị Ứng dụng/Tiến trình cụ thể (Process).
  - Cấu trúc Socket = `IP Address : Port Number`.
  - Phân loại cổng: Well-known ports (0-1023), Registered ports (1024-49151), Ephemeral/Dynamic ports (49152-65535).
- **6.2. Giao thức UDP (User Datagram Protocol):**
  - Đặc tính: Đơn giản, không hướng kết nối (Connectionless), không bảo đảm thứ tự và không retransmit.
  - Ứng dụng: DNS, DHCP, Streaming âm thanh/hình ảnh, Gaming.
- **6.3. Giao thức TCP (Transmission Control Protocol) – Độ tin cậy tuyệt đối:**
  - Cơ chế Bắt tay 3 bước (Three-way Handshake): `SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`.
  - Đánh số thứ tự từng byte (Sequence Number) và Xác nhận nhận hàng (Acknowledgment Number).
  - Cơ chế Truyền lại khi hết thời gian chờ (Retransmission Timeout - RTO).
- **6.4. Cơ chế Cửa sổ trượt (Sliding Window) & Kiểm soát luồng (Flow Control):**
  - Trường Window Size trong TCP Header: Bên nhận thông báo dung lượng bộ đệm khả dụng.
  - Tránh làm tràn bộ đệm bên nhận (Buffer Overflow) và thích ứng với tình trạng nghẽn mạng (Congestion Control).

### MODULE 7: TẦNG ỨNG DỤNG (APPLICATION LAYER) & LẬP TRÌNH SOCKET
- **7.1. Mô hình Khách/Chủ (Client/Server Architecture):**
  - Vai trò của Server: Luôn lắng nghe trên một cổng cố định (Listening state).
  - Vai trò của Client: Chủ động khởi tạo kết nối thông qua một cổng ngẫu nhiên tạm thời.
- **7.2. Giao thức HTTP (HyperText Transfer Protocol):**
  - Bản chất văn bản thuần (Plain-text request/response).
  - Cấu trúc HTTP Request: Phương thức (`GET`, `POST`), URI, Headers, Body.
  - Cấu trúc HTTP Response: Status Code (`200 OK`, `301 Moved`, `404 Not Found`, `500 Server Error`), Headers, Content.
- **7.3. Giao thức Thư điện tử (IMAP vs POP3/SMTP):**
  - Lấy thư và đồng bộ thư mục qua IMAP (cổng 143/993).
- **7.4. Giao diện Lập trình Mạng Socket (Berkeley Sockets API):**
  - Trừu tượng hóa kết nối mạng như một tệp tin (File Descriptor: Open, Read, Write, Close).
  - Minh họa luồng lập trình Socket bằng Python.

### MODULE 8: BẢO MẬT TẦNG GIAO VẬN (NETWORK SECURITY & TLS/SSL)
- **8.1. Các mối đe dọa trên đường truyền không bảo mật:**
  - Nghe lén (Eavesdropping / Sniffing), Sửa đổi gói tin (Tampering / Man-in-the-Middle), Mạo danh (Impersonation).
- **8.2. Mật mã học cổ điển vs Mật mã hiện đại:**
  - Mã hóa đối xứng (Symmetric Encryption: AES, DES): Tốc độ cực nhanh nhưng nan giải bài toán chia sẻ khóa bí mật (Key Distribution Problem).
  - Mã hóa bất đối xứng (Asymmetric / Public-Key Encryption: RSA, ECC): Cặp khóa Công khai (Public Key) và Khóa riêng tư (Private Key).
- **8.3. Mô hình lai và Giao thức TLS/SSL:**
  - Dùng mật mã bất đối xứng để đàm phán an toàn Khóa phiên đối xứng (Session Key).
  - Hạ tầng khóa công khai (PKI) và Cơ quan chứng thực (Certificate Authority - CA).
  - Quy trình xác thực Chứng chỉ số X.509 và Bắt tay TLS Handshake.

### MODULE 9: ĐỐI CHIẾU MÔ HÌNH TCP/IP VÀ MÔ HÌNH OSI 7 TẦNG
- **9.1. Lịch sử Cuộc chiến Tiêu chuẩn Mạng (Protocol Wars):**
  - Mô hình OSI (Open Systems Interconnection) do ISO phát triển: Lý thuyết, chặt chẽ, do các ủy ban thiết kế từ trên xuống (Top-down).
  - Mô hình TCP/IP: Triết lý của IETF ("Rough consensus and running code" - Đồng thuận chung và mã nguồn thực tế chạy được).
- **9.2. Ma trận Ánh xạ 7 tầng OSI sang 4 tầng TCP/IP:**
  - Tầng 7 (Application), Tầng 6 (Presentation), Tầng 5 (Session) $\rightarrow$ Gộp vào Tầng Ứng dụng (Application) của TCP/IP.
  - Tầng 4 (Transport) $\leftrightarrow$ Tầng Giao vận (Transport).
  - Tầng 3 (Network) $\leftrightarrow$ Tầng Mạng (Internet / IP).
  - Tầng 2 (Data Link) & Tầng 1 (Physical) $\rightarrow$ Gộp vào Tầng Liên kết (Link Layer / Network Access) của TCP/IP.
- **9.3. Giá trị thực tiễn của từng mô hình:**
  - OSI: Ngôn ngữ chuẩn mực để thảo luận kiến trúc và chẩn đoán sự cố mạng (Troubleshooting layers).
  - TCP/IP: Giao thức thực thi thực tế đang vận hành toàn bộ Internet.

---

## 5. KẾ HOẠCH BÀI THỰC HÀNH LAB (HANDS-ON LAB ACTIVITIES)

### LAB 1: GIẢI MÃ ĐỊNH TUYẾN VỚI PING VÀ TRACEROUTE (90 PHÚT)
- **Mục tiêu:** 
  - Khảo sát thực tế cơ chế Hop-by-Hop và sự sụt giảm của trường TTL.
  - Phân tích thông điệp lỗi ICMP Time Exceeded.
- **Nội dung thực hiện:**
  1. Sử dụng lệnh `ping` với các tham số điều chỉnh TTL:
     ```bash
     ping -c 4 -t 1 google.com   # Trên Linux/macOS
     ping -n 4 -i 1 8.8.8.8       # Trên Windows
     ```
     Quan sát kết quả lỗi trả về từ Default Gateway (`Time to live exceeded`).
  2. Chạy lệnh `traceroute google.com` (hoặc `tracert 8.8.8.8`).
  3. Ghi lại bảng danh sách các chặng Router (IP, Round-trip time - RTT). Nhận diện hiện tượng gói tin bị chặn bởi tường lửa (ký tự dấu sao `* * *`).
  4. Thực hiện tra cứu DNS thủ công bằng `dig +trace google.com` hoặc `nslookup -type=ns .` để xem toàn bộ chuỗi phân giải từ Root Server xuống Authoritative Server.

### LAB 2: BẮT VÀ PHÂN TÍCH GÓI TIN VỚI WIRESHARK (90 PHÚT)
- **Mục tiêu:**
  - Trực quan hóa cấu trúc đóng gói đa tầng (Ethernet Frame $\rightarrow$ IP Header $\rightarrow$ TCP Header $\rightarrow$ HTTP Payload).
  - Kiểm chứng tiến trình Bắt tay 3 bước của TCP.
- **Nội dung thực hiện:**
  1. Khởi động Wireshark, chọn card mạng tích cực (Wi-Fi hoặc Ethernet) và đặt bộ lọc: `tcp.port == 80 || http`.
  2. Dùng trình duyệt truy cập một trang web HTTP thuần (ví dụ: `http://neverssl.com` hoặc máy chủ HTTP thử nghiệm).
  3. Tìm kiếm và phân tích luồng TCP 3-Way Handshake:
     - Gói tin 1: Cờ `[SYN]`, Sequence Number gốc (ISN), Window Size đề xuất.
     - Gói tin 2: Cờ `[SYN, ACK]`, xác nhận gói tin 1 (`ACK = ISN_client + 1`).
     - Gói tin 3: Cờ `[ACK]`, hoàn tất thiết lập kết nối logic.
  4. Mở rộng chi tiết gói tin HTTP Request (`GET / HTTP/1.1`) và chỉ ra từng trường Header của 4 tầng tương ứng.

### LAB 3: TƯƠNG TÁC GIAO THỨC VỚI NETCAT & LẬP TRÌNH PYTHON SOCKET (90 PHÚT)
- **Mục tiêu:**
  - Xóa bỏ sự thần bí của Tầng Ứng dụng: Hiểu rõ ứng dụng mạng bản chất chỉ là gửi và nhận chuỗi ký tự qua một kết nối Socket.
  - Tự tay lập trình một Web Client tối giản bằng Python.
- **Nội dung thực hiện:**
  1. **Bài tập 1: Gửi HTTP Request thô qua dòng lệnh Netcat / Telnet:**
     ```bash
     nc -C data.pr4e.org 80
     GET /code/romeo.txt HTTP/1.1
     Host: data.pr4e.org
     <Enter>
     <Enter>
     ```
     Quan sát mã trạng thái phản hồi `HTTP/1.1 200 OK` cùng nội dung văn bản.
  2. **Bài tập 2: Lập trình Python Socket Client:**
     Viết đoạn mã Python ngắn (dưới 15 dòng) kết nối tới Web Server, gửi chuỗi `GET` và in ra kết quả:
     ```python
     import socket

     mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     mysock.connect(('data.pr4e.org', 80))
     cmd = 'GET /code/romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode()
     mysock.send(cmd)

     while True:
         data = mysock.recv(512)
         if len(data) < 1:
             break
         print(data.decode(), end='')

     mysock.close()
     ```
  3. Thử nghiệm thay đổi đường dẫn URL để chủ động tạo ra mã lỗi `404 Not Found`.

---

## 6. HÌNH THỨC ĐÁNH GIÁ (ASSESSMENT SCHEME)

- **Đánh giá Chuyên cần & Tham gia thảo luận trên lớp:** 10%
- **Bài kiểm tra Trắc nghiệm Định kỳ (Quiz - 5 câu hỏi tình huống chuyên sâu):** 20%
- **Báo cáo Thực hành 3 bài Lab (Wireshark, Traceroute, Socket):** 30%
- **Bài thi Cuối kỳ (Lý thuyết tổng hợp & Phân tích kịch bản mạng):** 40%

---

## 7. TÀI LIỆU HỌC TẬP & THAM KHẢO (REFERENCES)

1. **Giáo trình chính:**
   - Charles Severance (Dr. Chuck). *Introduction to Networking: How the Internet Works*. CreateSpace Independent Publishing Platform, 2015. (Trực tuyến: `http://www.net-intro.com/`).
2. **Tài liệu tham khảo mở rộng:**
   - James F. Kurose, Keith W. Ross. *Computer Networking: A Top-Down Approach (8th Edition)*. Pearson, 2021.
   - W. Richard Stevens. *TCP/IP Illustrated, Volume 1: The Protocols*. Addison-Wesley.
   - Các tài liệu chuẩn hóa IETF RFC: RFC 791 (IPv4), RFC 793 (TCP), RFC 1034/1035 (DNS), RFC 1918 (Private Address Space), RFC 2616 (HTTP/1.1).

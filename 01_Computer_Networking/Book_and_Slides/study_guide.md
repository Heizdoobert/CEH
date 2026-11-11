# CẨM NANG TỰ HỌC: MẠNG MÁY TÍNH & KIẾN TRÚC INTERNET
## (Learner-Focused Computer Networking Study Guide)

*Dựa trên giáo trình của GS. Charles Severance (Univ. of Michigan)*  
*Biên soạn: Đội ngũ Kỹ sư Mạng*

---

## TỔNG QUAN & MỤC TIÊU
- **Đối tượng**: Sinh viên CNTT, ATTT, kỹ sư phần mềm.
- **Mục tiêu**: Nắm vững bản chất Internet, chuẩn hóa thuật ngữ, làm chủ công thức mạng và hoàn thành 5 bài tập thực hành.

---

## BẢNG THUẬT NGỮ CHUẨN HÓA & KHẮC PHỤC DỊCH MÁY
*(Bilingual Glossary & Translation Pitfalls Correction)*

| Thuật ngữ Tiếng Anh | Lỗi dịch thô | Thuật ngữ Chuẩn hóa | Định nghĩa Chuẩn |
| :--- | :--- | :--- | :--- |
| **Router / Routing Table** | *"r bánh xe", "bàn xoay"* | **Bộ định tuyến / Bảng định tuyến** | Thiết bị T3 chuyển gói theo bảng. |
| **Window Size / Sliding Window**| *"kích thước gió"* | **Kích thước cửa sổ / Cửa sổ trượt**| Byte TCP gửi trước khi cần ACK. |
| **Subdomain** | *"tàu ngầm"* | **Tên miền con / Miền cấp dưới** | Miền con trực thuộc tên miền cha. |
| **Acknowledgment (ACK)** | *"Phát hiện ra rồi"* | **Gói tin xác nhận (ACK)** | Tín hiệu xác nhận nhận dữ liệu. |
| **OSI Model** | *"hệ điều hành"* | **Mô hình Tham chiếu OSI 7 tầng** | Khung 7 tầng chuẩn ISO. |
| **Switchboard Operator** | *"người bầu cử"* | **Tổng đài viên viễn thông** | Nối dây tạo mạch thoại thủ công. |
| **Transmission** | *"sự truyền nhiễm"* | **Sự truyền dẫn tín hiệu** | Phát bit lên đường truyền. |
| **Private Key / Public Key** | *"chìa khóa phụ kiện / công cộng"*| **Khóa bí mật / Khóa công khai** | Khóa công khai mã, bí mật giải. |
| **Port / Port Number** | *"cảng biển"* | **Cổng / Số hiệu cổng dịch vụ** | Định danh 16-bit cho tiến trình. |
| **Packet Hop** | *"chuyến nhảy"* | **Chặng chuyển tiếp (Hop)** | Chuyển gói qua một router. |
| **Certificate Authority (CA)** | *"Chính quyền cấp cao"* | **Tổ chức Chứng thực Số (CA)** | Tổ chức ký chứng chỉ số. |
| **Buffer / Buffering** | *"đệm giữ vào dữ liệu"* | **Bộ nhớ đệm (Buffer)** | Vùng nhớ đệm lưu tạm dữ liệu. |
| **Carrier Sense** | *"cảm giác người vận chuyển"*| **Lắng nghe sóng mang** | Nghe đường truyền trước khi phát. |

---

## TÓM TẮT KIẾN THỨC CỐT LÕI (CHƯƠNG 1 ĐẾN CHƯƠNG 9)

### CHƯƠNG 1: SỰ RA ĐỜI CỦA MẠNG & CHUYỂN MẠCH GÓI
1. **Circuit Switching vs Packet Switching**:
   - *Circuit Switching*: Chiếm độc quyền đường truyền suốt phiên thoại; lãng phí tài nguyên và dễ đứt kết nối nếu trạm hỏng.
   - *Packet Switching*: Băm nhỏ dữ liệu thành các **gói tin (Packets)** mang IP nguồn/đích, router chuyển tiếp linh hoạt qua hạ tầng chia sẻ.
   - *Ẩn dụ*: Circuit Switching như thuê riêng một đường dây điện thoại đồng nối thẳng giữa hai nhà (private dedicated phone line); Packet Switching như gửi bưu thiếp qua bưu điện, mỗi bưu thiếp đi xe khác nhau rồi ghép lại tại đích.
2. **Độ trễ Đầu-cuối (End-to-End Delay)**:
   $$D_{total} = D_{proc} + D_{queue} + D_{trans} + D_{prop}$$
   - $D_{proc}$: Trễ xử lý đọc header và tra bảng định tuyến.
   - $D_{queue}$: Trễ xếp hàng trong bộ đệm router.
   - $D_{trans} = \frac{L}{R}$: Trễ truyền tải ($L$: độ dài bit, $R$: bps).
   - $D_{prop} = \frac{d}{s}$: Trễ lan truyền ($d$: mét, $s \approx 2 \times 10^8\ \text{m/s}$).

---

### CHƯƠNG 2: KIẾN TRÚC ĐA TẦNG & CƠ CHẾ ĐÓNG GÓI DỮ LIỆU
1. **Triết lý Phân tầng**: Tách hệ thống thành các tầng độc lập (Separation of Concerns). Tầng trên dùng dịch vụ tầng dưới qua giao diện chuẩn.
2. **Kiến trúc TCP/IP 4 Tầng**:
   - **Application**: Ứng dụng mạng (HTTP, IMAP, DNS). Đơn vị: *Message*.
   - **Transport**: Truyền tiến trình-tới-tiến trình (TCP, UDP). Đơn vị: *Segment / Datagram*.
   - **Internet**: Định tuyến liên mạng (IPv4, IPv6). Đơn vị: *Packet*.
   - **Link**: Truyền khung qua liên kết vật lý (Ethernet, Wi-Fi). Đơn vị: *Frame*.
3. **Đóng gói & Mở gói**:
   - Gửi: Gắn thêm header ($\text{Data} \to \text{Segment} \to \text{Packet} \to \text{Frame}$). Nhận: Bóc tách header từ dưới lên.
   - *Ẩn dụ*: Búp bê Nga Matryoshka: thư nằm trong phong bì Transport, đặt tiếp vào phong bì IP, rồi bọc trong thùng hàng Link.

---

### CHƯƠNG 3: TẦNG LIÊN KẾT & MẠNG CỤC BỘ (LINK LAYER)
1. **Phạm vi**: Truyền khung tin (Frame) giữa các nút kề nhau trong mạng cục bộ (LAN / Single-hop).
2. **Địa chỉ MAC**: Địa chỉ vật lý 48-bit (ví dụ `00:1A:2B:3C:4D:5E`): 24 bit đầu là OUI nhà sản xuất, 24 bit sau định danh NIC.
3. **Cơ chế CSMA/CD trong Ethernet**:
   - *Carrier Sense*: Lắng nghe đường truyền rảnh mới phát tín hiệu.
   - *Multiple Access*: Nhiều thiết bị dùng chung môi trường truyền.
   - *Collision Detection*: Phát hiện xung đột điện áp thì dừng phát và gửi tín hiệu nghẽn (*Jam Signal*).
   - *Binary Exponential Backoff*: Chờ ngẫu nhiên $r \in [0, 2^k - 1]$ khe thời gian trước khi thử lại.
   - *Ẩn dụ kinh điển*: Nhóm người trong phòng kín/phòng tối cùng nói chuyện: lắng nghe trước khi nói (Carrier Sense), dùng chung không gian (Multiple Access), phát hiện va chạm âm thanh thì dừng lại và báo hiệu nghẽn (Collision Detection & Jam Signal), rồi chờ ngẫu nhiên khoảng thời gian khác nhau trước khi thử nói lại.
4. **Khung Ethernet II**: Preamble/SFD (8B), MAC đích/nguồn (6B mỗi trường), EtherType (2B, `0x0800`: IPv4), Payload (46 - 1500B, MTU $1500\ \text{bytes}$), FCS/CRC-32 (4B kiểm tra lỗi).

---

### CHƯƠNG 4: TẦNG MẠNG & GIAO THỨC IP (NETWORK LAYER)
1. **Dịch vụ Best-Effort & Hop-by-Hop**:
   - IP nỗ lực tối đa (*Best-effort*): không đảm bảo gói tin tới đích, không sửa lỗi mất gói.
   - Router chuyển tiếp từng chặng (*Hop-by-Hop*): tra bảng định tuyến ném gói sang Next-Hop kế tiếp.
2. **IPv4 & Công thức Subnet**:
   Địa chỉ IPv4 32-bit gồm Network ID và Host ID, ký pháp CIDR `/n`. Số host khả dụng:
   $$N = 2^{32 - n} - 2$$
   *(Trừ địa chỉ mạng bit host bằng 0 và broadcast bit host bằng 1)*.
3. **IP Riêng (RFC 1918) & NAT**: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`. Router dùng **NAT** chuyển Private IP thành Public IP duy nhất khi ra ngoài Internet.
4. **Trường TTL & Traceroute**:
   - Tiêu đề IP chứa TTL (8-bit). Qua mỗi router: $TTL_{k+1} = TTL_k - 1$.
   - Khi $TTL = 0$, router hủy gói và gửi **ICMP Type 11 (Time Exceeded)** về nguồn.
   - *Traceroute*: Gửi chuỗi gói thăm dò với $TTL = 1, 2, 3...$ ép router phản hồi ICMP lập bản đồ đường đi.

---

### CHƯƠNG 5: HỆ THỐNG PHÂN GIẢI TÊN MIỀN (DNS)
1. **Cây Phân cấp DNS**: Root (`.`) $\to$ TLD (`.com`, `.vn`) $\to$ Authoritative (`example.com`).
2. **Tiến trình Phân giải Tên miền**:
   - Client gửi truy vấn đệ quy (*Recursive*) tới DNS Resolver (`8.8.8.8`).
   - Resolver truy vấn lặp (*Iterative*): Root $\to$ TLD $\to$ Authoritative Server để lấy IP.
   - Bộ đệm DNS (*DNS Cache*) lưu tạm bản ghi theo **TTL** để giảm tải máy chủ và tăng tốc truy vấn.
3. **Bản ghi Cốt lõi**: `A` (IPv4), `AAAA` (IPv6), `CNAME` (bí danh), `MX` (máy chủ mail), `TXT` (xác thực SPF/DKIM).

---

### CHƯƠNG 6: TẦNG GIAO VẬN & ĐIỀU KHIỂN LUỒNG (TRANSPORT LAYER)
1. **Cổng & Socket**:
   - Port 16-bit ($0 - 65535$): Hệ thống ($0 - 1023$), Đăng ký ($1024 - 49151$), Tạm thời ($49152 - 65535$).
   - Kết nối định danh bởi:
     $$\text{Socket Pair} = (\text{Src IP}, \text{Src Port}, \text{Dst IP}, \text{Dst Port}, \text{Protocol})$$
   - *Ẩn dụ*: IP là địa chỉ quán, Port là số bàn, Socket là bồi bàn riêng của bàn đó.
2. **TCP vs UDP**:
   - **TCP**: Hướng kết nối, tin cậy, đúng thứ tự, có kiểm soát luồng và chống nghẽn (Web, Email).
   - **UDP**: Phi kết nối, không bảo đảm đến đích, header nhẹ (8B), trễ thấp (Game, DNS, VoIP).
3. **Bắt tay Ba bước TCP (3-Way Handshake)**:
   - Bước 1: $\text{Client} \xrightarrow{SYN=1,\ seq=x} \text{Server}$
   - Bước 2: $\text{Server} \xrightarrow{SYN=1,\ ACK=1,\ seq=y,\ ack=x+1} \text{Client}$
   - Bước 3: $\text{Client} \xrightarrow{ACK=1,\ seq=x+1,\ ack=y+1} \text{Server}$
4. **Cửa sổ Trượt & Tích BDP**:
   - Bên nhận báo bộ đệm qua `Window Size`. Bên gửi truyền liên tục số byte này không đợi từng ACK.
   - Thông lượng: $Throughput \le \frac{\text{Window Size}}{\text{RTT}}$.
   - $\text{BDP} = \text{Bandwidth} \times \text{RTT}$: Dữ liệu tối đa lấp đầy đường truyền. Nếu $\text{Window Size} < \text{BDP}$, mạng lãng phí băng thông.

---

### CHƯƠNG 7: TẦNG ỨNG DỤNG & LẬP TRÌNH MẠNG
1. **Mô hình Client-Server**: Server chạy thường trực ở trạng thái `LISTEN` trên cổng cố định; Client chủ động kết nối gửi yêu cầu.
2. **Giao thức Dạng Văn bản Thuần**:
   - *HTTP (Stateless)*: Yêu cầu và phản hồi độc lập:
     - Request: `GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n`
     - Response: `HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n[Data]`
   - *Giao thức IMAP (RFC 3501, Port 143/993)*: Quản lý và đồng bộ thư điện tử có trạng thái (*stateful*) trên máy chủ trung tâm (đối lập với HTTP phi trạng thái). Minh họa cặp lệnh mẫu:
     - `C: A142 SELECT INBOX`
     - `S: A142 OK SELECT completed`
3. **Berkeley Sockets API**:
   - Server: `socket()` $\to$ `bind()` $\to$ `listen()` $\to$ `accept()` $\to$ `recv()` / `send()` $\to$ `close()`.
   - Client: `socket()` $\to$ `connect()` $\to$ `send()` / `recv()` $\to$ `close()`.

---

### CHƯƠNG 8: AN TOÀN THÔNG TIN & TẦNG BẢO MẬT SSL/TLS
1. **Tam giác CIA**: Bí mật (Confidentiality), Toàn vẹn (Integrity), Xác thực (Authentication).
2. **Mã hóa Đối xứng vs Bất đối xứng**:
   - *Đối xứng (AES)*: Dùng chung một khóa; tốc độ nhanh nhưng khó phân phối khóa.
   - *Bất đối xứng (RSA)*: Khóa Công khai (Public Key) mã hóa, Khóa Bí mật (Private Key) giải mã.
   - *Ẩn dụ*: Khóa công khai là ổ khóa mở phát cho mọi người; ai cũng bấm khóa được, chỉ người giữ chìa khóa bí mật mới mở được.
3. **Tổ chức CA & Bắt tay TLS**:
   - **CA**: Ký chứng chỉ X.509 xác thực máy chủ, chống tấn công MitM.
   - **Bắt tay TLS**: Dùng mật mã bất đối xứng xác thực máy chủ và thỏa thuận **Khóa phiên (Session Key)** đối xứng để mã hóa dữ liệu.

---

### CHƯƠNG 9: MÔ HÌNH THAM CHIẾU OSI 7 TẦNG & ĐỐI CHIẾU THỰC TIỄN
1. **Mô hình OSI 7 Tầng**: Application (7), Presentation (6), Session (5), Transport (4), Network (3), Data Link (2), Physical (1).
2. **Đối chiếu OSI vs TCP/IP Thực tế**:

| Tầng OSI | Tầng TCP/IP | Vai trò & Giao thức Điển hình |
| :--- | :--- | :--- |
| **Application, Presentation, Session** | **Tầng Ứng dụng (Application)** | Dữ liệu ứng dụng, định dạng, phiên (HTTP, IMAP, DNS). |
| **Transport** | **Tầng Giao vận (Transport)** | Kết nối đầu-cuối qua số cổng (TCP, UDP). |
| **Network** | **Tầng Mạng / Internet** | Định tuyến gói tin liên mạng (IPv4, IPv6, ICMP). |
| **Data Link, Physical** | **Tầng Liên kết (Link Layer)** | Khung truyền tín hiệu vật lý (Ethernet, Wi-Fi). |

3. **Lý do TCP/IP Thắng thế**: Triết lý thực dụng *"Rough consensus and running code"*, tích hợp sẵn vào nhân BSD UNIX và vận hành thực tế trên ARPANET; trong khi OSI quá cồng kềnh trên lý thuyết.

---

## BÀI TẬP THỰC HÀNH CÓ LỜI GIẢI CHI TIẾT (5 BÀI TẬP)

### BÀI TẬP 1: TÍNH TOÁN PHÂN CHIA MẠNG CON IPV4 (SUBNETTING)
- **Đề bài**: Chia dải `192.168.10.0/24` thành 4 subnet đều nhau cho: Kỹ thuật, Kinh doanh, Nhân sự, CSKH.
- **Lời giải**:
  1. Số subnet: $S = 4 = 2^2 \implies$ mượn $k = 2$ bit Host.
  2. Tiền tố mới: $n = 24 + 2 = 26$ (`/26`), Mặt nạ: `255.255.255.192`.
  3. Số host khả dụng mỗi subnet:
     $$N = 2^{32 - 26} - 2 = 2^6 - 2 = 62\ \text{máy trạm / subnet}$$
  4. Bước nhảy: $256 - 192 = 64$. Bảng phân bổ:

| Phòng Ban | Network ID | Dải IP Khả dụng | Broadcast |
| :--- | :--- | :--- | :--- |
| **Kỹ thuật** | `192.168.10.0/26` | `192.168.10.1` $\to$ `192.168.10.62` | `192.168.10.63` |
| **Kinh doanh**| `192.168.10.64/26` | `192.168.10.65` $\to$ `192.168.10.126`| `192.168.10.127` |
| **Nhân sự** | `192.168.10.128/26`| `192.168.10.129` $\to$ `192.168.10.190`| `192.168.10.191` |
| **CSKH** | `192.168.10.192/26`| `192.168.10.193` $\to$ `192.168.10.254`| `192.168.10.255` |

---

### BÀI TẬP 2: THỰC HÀNH LỆNH TRACEROUTE & CƠ CHẾ TTL
- **Đề bài**: Phân tích kết quả lệnh `traceroute 8.8.8.8`:
  ```text
  1  192.168.1.1  1.82 ms  1.91 ms  1.75 ms
  2  10.20.0.1    11.23 ms 10.95 ms 11.10 ms
  3  * * *
  4  72.14.215.85 24.31 ms 24.12 ms 24.25 ms
  5  8.8.8.8      24.50 ms 24.15 ms 24.30 ms
  ```
- **Lời giải**:
  1. *Cơ chế TTL*: Gói có $TTL = 1$, router hop 1 giảm về 0, hủy gói và gửi `ICMP Type 11 (Time Exceeded)`. Gói có $TTL = 2$ tới hop 2 giảm về 0 và kích hoạt ICMP.
  2. *Ký hiệu `* * *` Hop 3*: Request Timed Out. Mạng không đứt do Hop 4, 5 vẫn phản hồi; router hop 3 chặn ICMP hoặc quá tải.
  3. *3 mốc thời gian*: Mỗi hop thăm dò 3 lần, hiển thị RTT khứ hồi tương ứng.

---

### BÀI TẬP 3: PHÂN TÍCH TIẾN TRÌNH BẮT TAY BA BƯỚC TCP
- **Đề bài**: Client A (`10.0.0.2:49200`) kết nối Server B (`203.0.113.10:80`). Cho $ISN_{Client} = 2000$, $ISN_{Server} = 7000$.
- **Lời giải**:
  1. *Bảng 3 gói tin bắt tay*:

| Bước | Chiều | Cờ | Seq | Ack | Trạng thái Client | Trạng thái Server |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | Client $\to$ Server | `SYN` | 2000 | 0 | `SYN_SENT` | `LISTEN` |
| **2** | Server $\to$ Client | `SYN, ACK` | 7000 | 2001 | `SYN_SENT` | `SYN_RCVD` |
| **3** | Client $\to$ Server | `ACK` | 2001 | 7001 | `ESTABLISHED` | `ESTABLISHED` |

  2. *Gói HTTP tiếp theo (400 bytes Payload)*:
     - Client gửi: $\text{Seq} = 2001, \text{Ack} = 7001, \text{Payload} = 400\ \text{bytes}$.
     - Server phản hồi: $\text{Ack} = 2001 + 400 = 2401$ (Nhận đủ đến byte 2400, chờ byte 2401).

---

### BÀI TẬP 4: KHÁM PHÁ VÀ PHÂN GIẢI DNS VỚI NSLOOKUP & DIG
- **Đề bài**: Phân giải tên miền `example.com`.
- **Thực hành & Lời giải**:
  1. *Bản ghi A và MX*: `nslookup -type=A example.com` và `dig example.com MX +short` trả về IPv4 (`93.184.216.34`) và máy chủ mail.
  2. *Phân giải đệ quy*: Lệnh `dig example.com +trace` qua 4 chặng: Root (`.`) $\to$ TLD (`.com`) $\to$ Authoritative (`iana-servers.net`) $\to$ IP đích.
  3. *Ý nghĩa TTL*: TTL (ví dụ `86400`s) quy định thời gian cache DNS lưu bản ghi trước khi hỏi lại nguồn gốc.

---

### BÀI TẬP 5: LẬP TRÌNH PYTHON SOCKET GỬI HTTP REQUEST THUẦN
- **Đề bài**: Dùng thư viện `socket` của Python kết nối cổng 80 của `example.com`, gửi HTTP GET thô và in phản hồi.
- **Mã nguồn (`raw_http.py`)**:

```python
import socket

# Khởi tạo TCP Socket IPv4 và kết nối máy chủ
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(5.0)
host = "example.com"
client.connect((host, 80))

# Gửi HTTP Request thô theo chuẩn RFC (\r\n)
request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
client.sendall(request.encode("utf-8"))

# Đọc phản hồi từ bộ đệm socket
response = b""
while True:
    chunk = client.recv(4096)
    if not chunk:
        break
    response += chunk

client.close()
print(response.decode("utf-8", errors="replace")[:300])
```

- **Phân tích kỹ thuật**:
  - `AF_INET`, `SOCK_STREAM`: Khai báo socket IPv4 và TCP.
  - `\r\n\r\n`: Đánh dấu kết thúc Headers HTTP.
  - `Connection: close`: Báo server đóng kết nối để kết thúc vòng lặp `recv`.

---

## LỜI KẾT & LỘ TRÌNH PHÁT TRIỂN
Làm chủ bản chất mạng từ các bit vật lý đến mã hóa TLS là nền móng vững chắc cho mọi kỹ sư phần mềm và an toàn thông tin.

**Lộ trình đề xuất**:
1. **Wireshark**: Phân tích gói tin DNS, TCP 3-way handshake, TLS handshake.
2. **IPv6**: Làm chủ không gian 128-bit và cơ chế SLAAC.
3. **Giao thức mới**: Tìm hiểu HTTP/2 Multiplexing và HTTP/3 nền QUIC (UDP).
4. **Hạ tầng Cloud**: Vận dụng Subnet và Routing thiết kế VPC trên AWS/Kubernetes.

## Tài liệu hỗ trợ
- [Cheat Sheet - Bảng tóm tắt nhanh](file:///mnt/second_drive/DOCS/SEC/01_Computer_Networking/Book_and_Slides/cheat_sheet.md)
- [Advanced OS Deep Knowledge (bilingual)](file:///home/agent/.gemini/antigravity-cli/brain/a44c0ad8-c1cc-47df-a93b-04561fd0fcf8/os_deep_knowledge.md)
- [Câu hỏi thi - Exam Questions](file:///mnt/second_drive/DOCS/SEC/01_Computer_Networking/Book_and_Slides/exam_questions.md)

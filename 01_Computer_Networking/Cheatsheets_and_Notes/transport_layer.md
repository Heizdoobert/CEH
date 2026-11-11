# Bài 2 – Tầng Transport (Transport Layer)

## 1. Mục tiêu
- Hiểu vai trò của tầng Transport trong việc **đưa dữ liệu** từ ứng dụng tới mạng.
- Phân biệt **TCP** và **UDP** – khi nào dùng cái nào.
- Nắm rõ cơ chế **three‑way handshake**, **flow control**, **congestion control** của TCP.
- Thực hành nhanh trong CLI: tạo kết nối TCP/UDP bằng `nc` (netcat) và quan sát gói tin.

## 2. Khái niệm cơ bản
| Thuật ngữ | Định nghĩa (tiếng Việt) |
|-----------|--------------------------|
| **Transport Layer** | Tầng trung gian giữa Application và Network, chịu trách nhiệm **đóng gói** dữ liệu thành **segment** (TCP) hoặc **datagram** (UDP) và cung cấp các dịch vụ vận chuyển tin cậy hoặc không‑tin cậy. |
| **TCP (Transmission Control Protocol)** | Giao thức **đảm bảo tin cậy**, cung cấp **kết nối** (connection‑oriented), **độ trễ cao hơn** nhưng **đảm bảo** dữ liệu tới đúng thứ tự, không mất. |
| **UDP (User Datagram Protocol)** | Giao thức **không tin cậy**, **không kết nối**, tốc độ nhanh, dùng cho streaming, VoIP, trò chơi thời gian thực. |
| **Three‑way handshake** | Quá trình **thiết lập kết nối** TCP: SYN → SYN‑ACK → ACK. |
| **Flow control** | Cơ chế **quản lý tốc độ** gửi dữ liệu để không làm đầy bộ đệm phía nhận (window size). |
| **Congestion control** | Thuật toán (slow start, congestion avoidance, fast retransmit/recovery) để tránh tắc nghẽn mạng. |

## 3. Các giao thức và tính năng chính
| Giao thức | Đặc điểm | Ứng dụng thực tế |
|-----------|----------|-------------------|
| **TCP** | Kết nối, tin cậy, kiểm soát lỗi, flow \u0026 congestion control | File download (HTTP, FTP), email (SMTP), SSH, MySQL. |
| **UDP** | Không kết nối, không kiểm tra lỗi, tốc độ thấp độ trễ | Video streaming (YouTube live), VoIP (Skype), online gaming, DNS query. |
| **TLS over TCP** | Mã hoá dữ liệu trên kết nối TCP | HTTPS, SSH, VPN TLS. |
| **QUIC (UDP‑based)** | TCP‑like reliability trên UDP, giảm RTT | HTTP/3 (Chrome, Edge). |

## 4. Hoạt động thực hành (10 phút)
### a. Thiết lập kết nối TCP đơn giản với `nc`
```bash
# Terminal 1: chạy server TCP (lắng nghe trên cổng 12345)
nc -l 12345

# Terminal 2: client kết nối và gửi tin
printf "Hello TCP!" | nc localhost 12345
```
- Khi bạn nhập lệnh trên, **Terminal 1** sẽ hiển thị `Hello TCP!`. Đây là minh hoạ **đảm bảo truyền dữ liệu** qua TCP.

### b. Kiểm tra **three‑way handshake** với `tcpdump`
```bash
# Mở một cửa sổ terminal để bắt gói TCP trên cổng 12345
sudo tcpdump -i any tcp port 12345 -vv -X &

# Sau đó thực hiện bước a (client‑server). Bạn sẽ thấy các gói SYN, SYN‑ACK, ACK trong output.
```
> *Lưu ý:* Nếu môi trường không cho phép `sudo`, bỏ qua phần này – vẫn có kết quả truyền dữ liệu.

### c. Gửi datagram UDP với `nc`
```bash
# Terminal 1: server UDP lắng nghe trên cổng 12346
nc -u -l 12346

# Terminal 2: client gửi tin UDP
printf "Hello UDP!" | nc -u localhost 12346
```
- Bạn sẽ nhận được **tin nhắn** nhanh hơn, nhưng nếu mạng mất gói, không có cơ chế tự động **re‑transmit**.

### d. So sánh tốc độ (đơn giản) với `time`
```bash
# Gửi 1 MB dữ liệu qua TCP
head -c 1M /dev/urandom | nc localhost 12345

time head -c 1M /dev/urandom | nc -u localhost 12346
```
- `time` sẽ cho thời gian thực hiện, giúp cảm nhận **độ trễ** giữa TCP và UDP.

## 5. Mini‑Quiz (5 câu)
1. TCP sử dụng **cơ chế nào** để thiết lập kết nối? (Tên quá trình)
2. Khi muốn **độ trễ thấp** cho video streaming, chúng ta thường chọn giao thức nào?
3. Thuật toán nào của TCP giúp **ngăn tắc nghẽn** mạng?
4. `nc -l 12345` mở **cổng** gì và **giao thức** nào?
5. Nếu một gói UDP bị mất, TCP và UDP **xử lý** ra sao khác nhau?

## 6. Tóm tắt nhanh (đánh dấu ★)
- **TCP** = Kết nối, tin cậy, ba‑bước handshake, kiểm soát lỗi, flow \u0026 congestion.
- **UDP** = Không kết nối, nhanh, không bảo đảm.
- Thực hành `nc`, `tcpdump`, `time` để cảm nhận thực tế.
- Kiểm tra hiểu biết qua mini‑quiz.

---
**Tiếp theo:** Bài 3 – Tầng Network. Khi bạn sẵn sàng, tôi sẽ đưa nội dung chi tiết và các lệnh thực hành (ping, traceroute, netmask, routing).

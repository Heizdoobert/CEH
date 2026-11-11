# Cheat Sheet: Mạng Máy Tính

## Công Thức & Định Lý
| Nội dung | Công thức / Định nghĩa | Ghi chú |
|---|---|---|
| **Độ trễ tổng** | $D_{total}=D_{proc}+D_{queue}+D_{trans}+D_{prop}$ | Xử lý, xếp hàng, truyền, lan truyền |
| **Thời gian truyền** | $D_{trans}=\frac{L}{R}$ | $L$: kích thước (bit), $R$: tốc độ (bps) |
| **Thời gian lan truyền** | $D_{prop}=\frac{d}{s}$ | $d$: khoảng cách, $s≈2\times10^8\,\text{m/s}$ |
| **Băng thông‑Delay Product** | $BDP = \text{Bandwidth}\times RTT$ | Lượng dữ liệu tối đa “trong ống” |
| **Số host khả dụng** | $N = 2^{32-n}-2$ | CIDR `/n` cho IPv4 |
| **Window Size / Throughput** | $Throughput \le \frac{\text{Window Size}}{RTT}$ | TCP Sliding Window |
| **TTL** | $TTL_{k+1}=TTL_k-1$ | Khi 0 → ICMP Time Exceeded |

## Thuật Ngữ & Cổng Phổ Biến
| Thuật ngữ | Định nghĩa ngắn gọn | Port (TCP/UDP) |
|---|---|---|
| **HTTP** | Giao thức ứng dụng cho web | 80 (TCP) |
| **HTTPS** | HTTP bảo mật TLS | 443 (TCP) |
| **DNS** | Dịch tên miền → IP | 53 (UDP/TCP) |
| **SMTP** | Gửi mail | 25 (TCP) |
| **POP3** | Nhận mail | 110 (TCP) |
| **IMAP** | Nhận mail (stateful) | 143 (TCP) |
| **SSH** | Đăng nhập bảo mật | 22 (TCP) |
| **FTP** | Truyền file | 21 (TCP) |
| **TLS Handshake** | Thiết lập khóa phiên | — |
| **ICMP** | Thông báo lỗi mạng | — |

## Các Giao Thức & Đặc Trưng
- **Circuit Switching**: Đường truyền cố định, giống thuê riêng một đường dây điện thoại.
- **Packet Switching**: Gói tin độc lập, giống bưu thiếp qua bưu điện.
- **CSMA/CD**: Lắng nghe, dùng chung, phát hiện va chạm, chờ ngẫu nhiên.
- **TCP 3‑Way Handshake**: SYN → SYN‑ACK → ACK.
- **Sliding Window**: Gửi nhiều segment trước khi ACK, dựa vào Window Size.

## Bảng so sánh TCP vs UDP
| Đặc điểm | TCP | UDP |
|---|---|---|
| Kết nối | Có (3‑way) | Không |
| Độ tin cậy | Có (retransmission, ordering) | Không |
| Overhead | Header 20 B | Header 8 B |
| Ứng dụng | Web, Email, SSH | DNS, VoIP, Streaming |

## Ẩn Dụ Nhớ nhanh
- **Router**: “Bộ định tuyến” – giống một trạm xe bus đưa hành khách (gói) tới điểm tới.
- **Port**: “Số bàn” trong nhà hàng – một dịch vụ trên host.
- **Socket**: “Bồi bàn” – cặp (IP, Port) để phục vụ khách.
- **TTL**: “Thời gian sống” – mỗi hop giảm 1, giống bộ đếm vòng đời.
- **CSMA/CD**: “Phòng chờ nói” – lắng nghe, nói khi yên tĩnh, nếu va chạm lặp lại ngẫu nhiên.

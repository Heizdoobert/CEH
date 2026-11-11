# Bài 5 – Tổng kết 5‑tầng & Đề án thực hành (4‑giờ)

## 1. Kế hoạch 4 giờ (lần cuối)
| Thời gian | Nội dung | Hoạt động |
|-----------|----------|-----------|
| **0‑10 phút** | Giới thiệu, mục tiêu toàn khoá | Đặt câu hỏi "Mạng máy tính sẽ thay đổi cuộc sống của bạn như thế nào?" |
| **10‑40 phát** | **Tầng Application** | Giảng giải HTTP/HTTPS, DNS, ví dụ `curl` (thực hành). |
| **40‑80 phút** | **Tầng Transport** | Giải thích TCP vs UDP, three‑way handshake, thực hành `nc`, `tcpdump`. |
| **80‑120 phút** | **Tầng Network** | IP, subnet, routing, thực hành `ping`, `traceroute`, `ip route`. |
| **120‑150 phút** | **Tầng Link & Physical** | Ethernet, Wi‑Fi, MAC, ARP, thực hành `ip link`, `ethtool`, `iwlist`. |
| **150‑170 phút** | **Mini‑quiz tổng hợp** | 10 câu hỏi liên quan tới mọi tầng, trả lời nhanh trên giấy hoặc chat. |
| **170‑190 phút** | **Demo toàn bộ chuỗi** | Từ `curl` (Application) → `nc` (Transport) → `ping` (Network) → `ethtool` (Link) → **Kết luận**. |
| **190‑210 phút** | **Thảo luận & Q&A** | Giải đáp thắc mắc, đề xuất tài liệu tự học. |
| **210‑240 phút** | **Kết thúc & tài liệu** | Phát cheat‑sheet, slide, và đề xuất bài tập thực hành ở nhà. |

## 2. Tổng quan 5‑tầng (cheat‑sheet nhanh)
| Tầng | Vai trò | Giao thức / Công nghệ chính | Ví dụ thực tế |
|------|----------|-----------------------------|----------------|
| **Application** | Giao diện người dùng, định nghĩa giao thức | HTTP/HTTPS, DNS, FTP, SMTP, WebSocket | Trình duyệt tải trang, email client |
| **Transport** | Vận chuyển dữ liệu tin cậy / không tin cậy | TCP (three‑way handshake, flow & congestion), UDP, QUIC | File download (TCP), video streaming (UDP/QUIC) |
| **Network** | Định tuyến, định danh toàn cục | IPv4/IPv6, ICMP, ARP, RIP/OSPF/BGP | Ping, traceroute, routing ISP |
| **Link (Data Link)** | Đóng gói thành frame, địa chỉ MAC, kiểm soát lỗi | Ethernet (802.3), Wi‑Fi (802.11), VLAN, LLDP | LAN cáp, mạng không dây cafe |
| **Physical** | Truyền bit qua vật lý (cáp, ánh sáng, vô tuyến) | Copper (Cat5e/6), Fiber, RF 2.4/5 GHz | Cáp Ethernet, Wi‑Fi hotspot |

## 3. Mini‑quiz tổng hợp (10 câu)
1. Giao thức nào ở tầng Application chịu trách nhiệm **dịch tên miền**? 
2. Trong TCP, quá trình **three‑way handshake** gồm những thông điệp nào? 
3. Khi một gói IP không tới được đích, giao thức nào thường gửi **Thông báo lỗi**? 
4. Địa chỉ MAC dài **bao nhiêu** bit? 
5. `ethtool eth0` cho biết MTU 1500; payload tối đa trong một Ethernet frame là **bao nhiêu** byte? 
6. Wi‑Fi sử dụng cơ chế **tránh va chạm** nào? 
7. Lệnh nào hiển thị **bảng routing** trên Linux? 
8. Giao thức nào cung cấp **độ tin cậy** nhưng lại **chậm hơn** UDP? 
9. Khi muốn đo tốc độ thực tế của một liên kết Ethernet, công cụ nào thường dùng? 
10. Trong mô hình 5‑tầng, **đâu** là tầng duy nhất có thể **mã hoá** dữ liệu (HTTPS)?

## 4. Bài tập thực hành ở nhà (tự luyện)
| Bài tập | Mô tả |
|---------|------|
| **1. HTTP ↔ TCP** | Dùng `nc` để mô phỏng một server TCP trả về một trang HTML đơn giản, sau đó dùng `curl` để lấy trang. |
| **2. UDP video** | Gửi một file video ngắn bằng `nc -u` tới một máy khác và đo độ trễ. |
| **3. Subnet calculation** | Tạo 3 subnet từ mạng 192.168.0.0/24, tính địa chỉ mạng, broadcast, số host. |
| **4. VLAN** | Thiết lập VLAN 20 trên máy Linux, gán địa chỉ IP, kiểm tra kết nối giữa các VLAN. |
| **5. Wi‑Fi scan** | Dùng `iwlist` để liệt kê các SSID xung quanh, chọn một SSID và kết nối bằng `nmcli`. |

## 5. Tài liệu & Slide (được lưu cùng thư mục)
- **Cheat‑sheet**: [/mnt/second_drive/DOCS/SEC/5layer_cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/5layer_cheatsheet.md)
- **Slide** (Markdown → HTML nếu cần): [/mnt/second_drive/DOCS/SEC/5layer_slide.md](file:///mnt/second_drive/DOCS/SEC/5layer_slide.md)

## 6. Kết luận
- 5‑tầng **không tách rời**: mỗi lớp cung cấp dịch vụ cho lớp trên và dựa vào lớp dưới.
- Việc **thực hành** ngay trong CLI giúp học viên cảm nhận rõ ràng *các tín hiệu* và *cấu trúc*.
- Sau buổi 4 giờ, học viên sẽ **hiểu**: cách một yêu cầu web di chuyển từ trình duyệt tới server và ngược lại, qua từng tầng.

---
**Bạn có muốn tôi tạo cheat‑sheet và slide file ngay bây giờ không?** Hoặc có bất kỳ yêu cầu bổ sung nào cho tài liệu cuối cùng.
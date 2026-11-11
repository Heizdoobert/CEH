# Cheat‑sheet – 5 tầng mô hình mạng máy tính (tóm tắt nhanh)

## 1. Application Layer
- **Chức năng:** Giao diện người dùng, định nghĩa giao thức cao cấp.
- **Giao thức chính:** HTTP/HTTPS, DNS, FTP, SMTP/POP3/IMAP, WebSocket, gRPC, TLS/SSL.
- **Ví dụ thực tế:** Trình duyệt tải trang web (`curl https://example.com`), email client gửi/nhận mail, video streaming qua HTTP/3.

## 2. Transport Layer
- **Chức năng:** Đảm bảo truyền dữ liệu giữa các host, cung cấp dịch vụ **tin cậy** (TCP) hoặc **không tin cậy** (UDP).
- **TCP:** Three‑way handshake (SYN‑SYN/ACK‑ACK), flow & congestion control, guarantee order & delivery.
- **UDP:** Không kết nối, ít độ trễ, dùng cho streaming, VoIP, game real‑time.
- **QUIC:** UDP‑based, mang lại tính tin cậy như TCP nhưng độ trễ thấp hơn (HTTP/3).
- **CLI demo:** `nc -l 12345` / `printf "msg" | nc localhost 12345`.

## 3. Network Layer
- **Chức năng:** Định danh toàn cầu (IP), định tuyến các gói qua mạng.
- **IP:** IPv4 (32‑bit) / IPv6 (128‑bit). Không bảo đảm giao hàng → phụ thuộc tầng dưới.
- **Subnet & CIDR:** `a.b.c.d/nn` – `nn` bit mạng, còn lại host. Ví dụ `192.168.10.45/24` → network `192.168.10.0`, broadcast `192.168.10.255`.
- **Routing:** Bảng routing (`ip route`), default gateway, các protocol như RIP, OSPF, BGP.
- **ICMP:** Ping (`ping -c 3 8.8.8.8`), traceroute (`traceroute 8.8.8.8`).

## 4. Data Link Layer (Link)
- **Chức năng:** Đóng gói thành **frame**, dùng **MAC address** để xác định node trong cùng LAN.
- **Ethernet (IEEE 802.3):** CSMA/CD, MTU 1500, tốc độ 10 Mbps‑100 Gbps.
- **Wi‑Fi (IEEE 802.11):** CSMA/CA, băng tần 2.4/5 GHz, tốc độ lên tới 10 Gbps.
- **ARP:** `IP → MAC` trong LAN.
- **VLAN (802.1Q):** Tag 12‑bit, tạo mạng logic riêng.
- **CLI demo:** `ip link show`, `ethtool eth0`, `iwlist wlan0 scanning`.

## 5. Physical Layer
- **Chức năng:** Truyền **bit** qua vật lý – cáp điện (Copper), quang (Fiber), hoặc sóng vô tuyến (Wi‑Fi).
- **Mạng cáp:** Cat5e/6 (100 Mbps‑1 Gbps), Cat6a/7 (10 Gbps), Fiber (40‑100 Gbps).
- **Wi‑Fi:** 2.4 GHz (802.11b/g/n) và 5 GHz (802.11ac/ax).
- **Ví dụ:** Cáp Ethernet nối máy tính tới switch, hoặc hotspot Wi‑Fi cung cấp mạng không dây.

---
**Sử dụng nhanh:**
- **Kiểm tra MAC:** `ip link show`.
- **Kiểm tra MTU & tốc độ:** `ethtool eth0`.
- **Kiểm tra IP/subnet:** `ip -o -f inet addr show`.
- **Kiểm tra routing:** `ip route`.
- **Kiểm tra kết nối:** `ping`, `traceroute`.
- **Kiểm tra Wi‑Fi:** `iwlist wlan0 scanning`.

> **Note:** Các lệnh trên đều có thể chạy trong Linux terminal, không cần phần mềm bên ngoài.

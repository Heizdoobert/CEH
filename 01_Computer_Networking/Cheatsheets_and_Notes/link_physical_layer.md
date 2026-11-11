# Bài 4 – Tầng Link & Physical (Data Link & Physical Layer)

## 1. Mục tiêu (đúng 4‑giờ kế hoạch)
- Hiểu **cách các thiết bị truyền bit** qua môi trường vật lý (cáp, sóng vô tuyến).
- Nắm rõ **Ethernet**, **Wi‑Fi (802.11)**, **MAC address**, **ARP**, **frame**, **collision detection / avoidance**.
- Thực hành nhanh trong CLI: kiểm tra/đọc MAC, cấu hình Ethernet, kiểm tra trạng thái Wi‑Fi, đo tốc độ link.
- Kiểm tra kiến thức qua **mini‑quiz**.

## 2. Khái niệm cơ bản
| Thuật ngữ | Định nghĩa (tiếng Việt) |
|-----------|--------------------------|
| **Physical Layer** | Tầng 1, chịu trách nhiệm **truyền bit** qua tín hiệu điện, quang, hoặc vô tuyến. |
| **Data Link Layer** | Tầng 2, chia dữ liệu thành **frame**, cung cấp **địa chỉ MAC**, kiểm soát lỗi, và **đồng bộ** truyền. |
| **Ethernet** | Công nghệ LAN phổ biến, dùng **cáp xoắn đôi** hoặc **quang**; khung Ethernet chứa `dest MAC`, `src MAC`, `type`, `payload`, `FCS`. |
| **Wi‑Fi (802.11)** | Chuẩn không dây, sử dụng **CSMA/CA** (collision avoidance) thay vì CSMA/CD của Ethernet. |
| **MAC address** | Địa chỉ phần cứng 48‑bit (12 hex digit) duy nhất cho mỗi NIC. |
| **ARP (Address Resolution Protocol)** | Giao thức chuyển đổi **IP → MAC** trong cùng mạng LAN. |
| **MTU (Maximum Transmission Unit)** | Kích thước **khung tối đa** mà một link cho phép (thường 1500 byte cho Ethernet). |

## 3. Giao thức và tính năng chính
| Giao thức / công nghệ | Đặc điểm | Ứng dụng thực tế |
|------------------------|----------|-------------------|
| **Ethernet (IEEE 802.3)** | CSMA/CD, tốc độ 10 Mbps → 100 Gbps, MTU 1500. | LAN văn phòng, data center. |
| **Wi‑Fi (IEEE 802.11ac/ax)** | CSMA/CA, băng tần 2.4 GHz/5 GHz, tốc độ lên tới 10 Gbps. | Mạng không dây gia đình, công cộng. |
| **ARP** | Broadcast request, trả về MAC của IP trong cùng subnet. | Định danh MAC cho giao tiếp Ethernet. |
| **LLDP (Link Layer Discovery Protocol)** | Quảng bá thông tin link (chủng loại, tốc độ). | Quản lý mạng, tự động phát hiện topology. |
| **802.1Q (VLAN tagging)** | Thêm tag 12‑bit vào frame để phân đoạn mạng logic. | Mạng doanh nghiệp, cách ly traffic. |

## 4. Thực hành nhanh trong CLI (10 phút)
### a. Xem địa chỉ MAC của các interface
```bash
ip link show               # hiển thị tên, trạng thái, và MAC (link/ether)
# hoặc dùng ifconfig (nếu có)
ifconfig -a | grep ether
```
Kết quả sẽ có dạng `link/ether aa:bb:cc:dd:ee:ff`.

### b. Kiểm tra tốc độ và MTU hiện tại
```bash
# Kiểm tra MTU và tốc độ (Speed) của interface eth0
ethtool eth0
```
- **Speed:** 1000Mb/s (Gigabit Ethernet) hoặc 100Mb/s.
- **MTU:** thường 1500.

### c. Đo tốc độ thực tế bằng `iperf3` (nếu có)
```bash
# Trên máy này (client) chạy:
iperf3 -c <IP‑server> -t 5
```
Nếu không có `iperf3`, dùng `ping -M do -s 1472 <IP>` để đo **ping size** gần MTU.

### d. Kiểm tra trạng thái Wi‑Fi và danh sách mạng (scan)
```bash
# Xem tên interface Wi‑Fi (thường wlan0)
iw dev

# Scan các AP xung quanh
sudo iwlist wlan0 scanning | grep ESSID
```
> *Nếu `sudo` không cho phép, chỉ chạy `iw dev wlan0 link` để xem AP đang kết nối.*

### e. Thực hiện ARP lookup và kiểm tra bảng ARP
```bash
# Ping một IP trong cùng subnet để tạo entry ARP
ping -c 1 192.168.1.10

# Xem bảng ARP
ip neigh show
```
- Bạn sẽ thấy dòng `192.168.1.10 dev eth0 lladdr aa:bb:cc:dd:ee:ff REACHABLE`.

### f. Thêm VLAN tag (ví dụ 10) vào interface (Linux có `vconfig` hoặc `ip link`)
```bash
# Tạo VLAN 10 trên eth0
sudo ip link add link eth0 name eth0.10 type vlan id 10
sudo ip addr add 192.168.10.2/24 dev eth0.10
sudo ip link set dev eth0.10 up
```
- Kiểm tra: `ip -d link show eth0.10` sẽ hiển thị `vlan id 10`.

## 5. Mini‑Quiz (5 câu)
1. Địa chỉ MAC luôn có độ dài **bao nhiêu** bit? (Ghi dưới dạng bit hoặc hex digit)
2. Khi một Ethernet frame **bị lỗi**, lớp nào chịu trách nhiệm phát hiện và yêu cầu **re‑transmit**?
3. Lệnh `ethtool eth0` trả về **Speed** và **MTU**; nếu MTU là 1500, tối đa payload dữ liệu trong một frame Ethernet là bao nhiêu byte?
4. Giao thức nào dùng để **tìm MAC** của một IP trong cùng subnet?
5. Khi dùng Wi‑Fi, cơ chế tránh va chạm được gọi là gì?

## 6. Tóm tắt nhanh (đánh dấu ★)
- **Physical**: Truyền bit qua cáp (copper, fiber) hoặc sóng (Wi‑Fi).
- **Data Link**: Đóng gói thành frame, dùng **MAC address**, **ARP**, **Ethernet**, **Wi‑Fi**.
- **Ethernet** = CSMA/CD, MTU 1500, tốc độ lên tới 100 Gbps.
- **Wi‑Fi** = CSMA/CA, băng tần 2.4/5 GHz, VLAN & QoS.
- Kiểm tra MAC, MTU, tốc độ với `ip link`, `ethtool`.
- Kiểm tra Wi‑Fi với `iw`, `iwlist`.
- Mini‑quiz để củng cố kiến thức.

---
**Tiếp theo:** Bài 5 – Tổng kết 5‑tầng, chuẩn bị slide, demo toàn bộ chuỗi từ Application → Physical. Khi bạn sẵn sàng, tôi sẽ tạo tài liệu cuối cùng và lời dẫn cho buổi học 4 giờ. 
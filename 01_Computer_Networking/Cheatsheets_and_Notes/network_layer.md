# Bài 3 – Tầng Network (Network Layer)

## 1. Mục tiêu
- Hiểu vai trò của **tầng Network** trong việc định tuyến gói tin qua các mạng khác nhau.
- Nắm được các khái niệm **địa chỉ IP, subnet mask, CIDR, routing**.
- Thực hành nhanh trong CLI: `ping`, `traceroute`, tính toán subnet, cấu hình tĩnh.
- Kiểm tra hiểu biết qua **mini‑quiz**.

## 2. Khái niệm cơ bản
| Thuật ngữ | Định nghĩa (tiếng Việt) |
|-----------|--------------------------|
| **IP address** | Địa chỉ số 32‑bit (IPv4) hoặc 128‑bit (IPv6) xác định thiết bị trên mạng. |
| **Subnet mask** | Mặt nạ mạng, xác định phần **network** và **host** của địa chỉ IP. |
| **CIDR (Classless Inter‑Domain Routing)** | Ký hiệu `a.b.c.d/nn` → `nn` bit mạng, còn lại là host. |
| **Routing** | Quy trình **chọn đường** mà gói tin sẽ đi qua các router để tới đích. |
| **Default gateway** | Router mặc định mà máy gửi gói nếu đích không thuộc cùng subnet. |
| **ICMP** | Giao thức **điều khiển thông tin** dùng cho ping, thông báo lỗi. |

## 3. Các giao thức và tính năng chính
| Giao thức | Đặc điểm | Ứng dụng thực tế |
|-----------|----------|-------------------|
| **IP (IPv4/IPv6)** | Địa chỉ định danh, **không bảo đảm** giao hàng; phụ thuộc vào các giao thức tầng dưới (Ethernet, Wi‑Fi). | Định danh máy tính, router. |
| **ICMP** | Thông báo lỗi, echo request/reply (ping). | Kiểm tra kết nối mạng. |
| **ARP** | Đổi địa chỉ IP sang MAC (Ethernet). | Tìm MAC của máy trong cùng LAN. |
| **Routing protocols** | **RIP**, **OSPF**, **BGP** – truyền thông tin routing giữa router. | ISP, doanh nghiệp lớn. |

## 4. Thực hành nhanh trong CLI (10 phút)
### a. Kiểm tra kết nối tới DNS Google (ping)
```bash
# Gửi 3 gói ICMP tới 8.8.8.8 (Google DNS)
ping -c 3 8.8.8.8
```
> *Nếu `ping` không có trên hệ thống, có thể dùng `curl -I https://8.8.8.8` để kiểm tra phản hồi HTTP.*

### b. Xem đường đi (traceroute) tới một máy ở internet
```bash
traceroute 8.8.8.8
```
> *Nếu `traceroute` chưa cài, dùng `tracepath 8.8.8.8` (có sẵn trên nhiều bản Linux).* 

### c. Tính subnet bằng `ipcalc` (nếu có) hoặc thủ công
```bash
# Ví dụ: IP 192.168.10.45/24
# Subnet mask = 255.255.255.0, Network = 192.168.10.0, Broadcast = 192.168.10.255
```
Bạn có thể dùng công cụ trực tuyến hoặc viết script Python ngắn:
```python
import ipaddress
net = ipaddress.ip_network('192.168.10.45/24', strict=False)
print('Network:', net.network_address)
print('Broadcast:', net.broadcast_address)
print('Usable hosts (first 3):', list(net.hosts())[:3], '…')
```

### d. Kiểm tra bảng routing của máy
```bash
ip route show
```
- Kết quả hiển thị **default gateway** (thường là `0.0.0.0/0 via <router>`). 

### e. Thêm route tĩnh (ví dụ)   
```bash
# Đưa các gói tới mạng 10.0.0.0/8 qua router 192.168.1.1
sudo ip route add 10.0.0.0/8 via 192.168.1.1 dev eth0
```
> *Cần quyền `sudo`; nếu không có, chỉ mô tả bước.*

## 5. Mini‑Quiz (5 câu)
1. Địa chỉ IP `172.16.5.20/16` thuộc **network** nào? (Ghi dưới dạng a.b.c.d/nn)
2. Khi một gói không thể tới đích, giao thức nào ở tầng Network thường trả về thông báo lỗi?
3. Lệnh nào hiển thị **bảng routing** hiện tại của Linux?
4. Đối với IPv4, **subnet mask** `255.255.255.192` tương đương với bao nhiêu bit mạng?
5. Nếu bạn không có `ping` trên hệ thống, công cụ nào khác có thể kiểm tra **kết nối** tới một IP?

## 6. Tóm tắt nhanh (đánh dấu ★)
- **IP** = Địa chỉ duy nhất, không bảo đảm.
- **Subnet** = Xác định mạng con, dùng CIDR `/nn`.
- **Routing** = Chọn đường đi, default gateway là “cổng ra”.
- **ICMP ping** = Kiểm tra khả năng tới.
- **Traceroute** = Theo dõi các hop trên đường đi.
- Kiểm tra và thay đổi routing bằng `ip route`.

---
**Tiếp theo:** Bài 4 – Tầng Link (Data Link) và Physical. Khi bạn sẵn sàng, tôi sẽ tạo nội dung và các lệnh thực hành (ethtool, iwconfig, …).
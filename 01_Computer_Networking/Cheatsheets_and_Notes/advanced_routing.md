# Chương 7 – Định tuyến nâng cao (Advanced Routing)

## 1. Mục tiêu
- Hiểu các giao thức **routing động**: OSPF, BGP, RIP.
- Nắm cách cấu hình **static routing** và **policy‑based routing**.
- Thực hành nhanh trên Linux với `ip route` và `bird`/`quagga`.

## 2. Các giao thức routing chính
| Giao thức | Loại | Đặc điểm | Ứng dụng thực tế |
|-----------|------|----------|-------------------|
| **RIP** (Routing Information Protocol) | Distance‑vector | Độ dài hop‑count, tối đa 15 hop. | Mạng LAN nhỏ.
| **OSPF** (Open Shortest Path First) | Link‑state | Thu thập thông tin toàn mạng, nhanh, hỗ trợ area. | Mạng doanh nghiệp, backbone.
| **BGP** (Border Gateway Protocol) | Path‑vector | Định tuyến liên mạng (Internet), chính sách route. | ISP, data‑center.
| **Static routing** | Manual | Cấu hình tĩnh, dễ kiểm soát. | Các đường đi cố định, VPN.
| **Policy‑based routing** | Rule‑based | Định tuyến dựa trên source/destination, port, protocol. | Traffic engineering.

## 3. Thực hành nhanh (CLI)
### a. Static route
```bash
# Thêm route tới mạng 10.0.0.0/8 qua gateway 192.168.1.1
sudo ip route add 10.0.0.0/8 via 192.168.1.1 dev eth0

# Xem bảng routing
ip route show
```
### b. OSPF với `bird`
```bash
sudo apt-get install -y bird
cat <<EOF | sudo tee /etc/bird/bird.conf
router id 192.168.1.2;
log syslog { debug, trace, info, warning, error, fatal, bug };
protocol ospf {
    area 0.0.0.0 {
        interface "eth0" { cost 10; };
    };
}
EOF
sudo systemctl restart bird
birdc show route
```
### c. BGP với `bird` (simple external peer)
```bash
cat <<EOF | sudo tee -a /etc/bird/bird.conf
protocol bgp mypeer {
    neighbor 203.0.113.1 as 65530;
    local as 65531;
    import all;
    export all;
}
EOF
sudo systemctl restart bird
birdc show route
```
### d. Policy‑based routing (iptables + ip rule)
```bash
# Đánh dấu traffic từ 192.168.1.100 tới port 80
sudo iptables -t mangle -A PREROUTING -s 192.168.1.100 -p tcp --dport 80 -j MARK --set-mark 10
# Thêm rule routing cho mark 10
sudo ip rule add fwmark 10 table 200
# Thêm default route cho bảng 200
sudo ip route add default via 10.0.0.1 dev eth0 table 200
```

## 4. Mini‑quiz
1. OSPF sử dụng thuật toán nào để tính đường ngắn nhất? 
2. BGP quyết định chọn route dựa trên **điểm gì**? (AS‑PATH, LOCAL‑PREF, MED…) 
3. Lệnh `ip route add 10.0.0.0/8 via 192.168.1.1 dev eth0` thực hiện gì? 
4. Trong `iptables`, option `-j MARK --set-mark 10` dùng để làm gì? 
5. Khi muốn xem bảng routing tiêu chuẩn, lệnh nào bạn dùng?

---

# Lab – Định tuyến nâng cao (Advanced Routing)

## Mục tiêu
- Cấu hình static route, OSPF và BGP trên Linux.
- Kiểm tra bảng routing và thực hiện policy‑based routing.

## Bài tập 1 – Static routing
1. Kiểm tra bảng routing hiện tại:
   ```bash
   ip route show
   ```
2. Thêm route tới mạng `10.0.0.0/8` qua gateway `192.168.1.1` trên interface `eth0`:
   ```bash
   sudo ip route add 10.0.0.0/8 via 192.168.1.1 dev eth0
   ```
3. Kiểm tra lại bảng routing và dùng `ping` tới một IP trong mạng 10.0.0.0/8 để xác nhận.
4. Xóa route vừa tạo:
   ```bash
   sudo ip route del 10.0.0.0/8
   ```

## Bài tập 2 – OSPF với Bird
1. Cài đặt Bird (OSPF daemon):
   ```bash
   sudo apt-get install -y bird
   ```
2. Tạo file cấu hình `/etc/bird/bird.conf`:
   ```ini
   router id 192.168.1.2;
   log syslog { info, warning, error, fatal };
   protocol ospf {
       area 0.0.0.0 {
           interface "eth0" { cost 10; };
       };
   }
   ```
3. Khởi động Bird và kiểm tra trạng thái OSPF:
   ```bash
   sudo systemctl restart bird
   birdc show route
   ```
4. Thêm một second router (có cùng area) và quan sát các route được học.

## Bài tập 3 – BGP cơ bản với Bird
1. Mở cổng BGP (TCP 179) trên firewall nếu cần.
2. Thêm peer BGP vào cấu hình `/etc/bird/bird.conf` (sau phần OSPF):
   ```ini
   protocol bgp external_peer {
       neighbor 203.0.113.1 as 65530;
       local as 65531;
       import all;
       export all;
   }
   ```
3. Khởi động lại Bird và kiểm tra bảng BGP:
   ```bash
   sudo systemctl restart bird
   birdc show route protocol bgp
   ```
4. Trên peer (có thể là một VM khác) thiết lập cấu hình tương tự và kiểm tra trao đổi route.

## Bài tập 4 – Policy‑Based Routing (PBR)
1. Đánh dấu traffic HTTP từ IP `192.168.1.100`:
   ```bash
   sudo iptables -t mangle -A PREROUTING -s 192.168.1.100 -p tcp --dport 80 -j MARK --set-mark 10
   ```
2. Thêm rule routing cho mark 10 vào bảng 200:
   ```bash
   sudo ip rule add fwmark 10 table 200
   sudo ip route add default via 10.0.0.1 dev eth0 table 200
   ```
3. Kiểm tra `ip rule list` và thực hiện `curl http://example.com` từ client 192.168.1.100 – lưu ý traffic sẽ đi qua gateway 10.0.0.1.
4. Xóa cấu hình khi hoàn thành:
   ```bash
   sudo iptables -t mangle -D PREROUTING -s 192.168.1.100 -p tcp --dport 80 -j MARK --set-mark 10
   sudo ip rule del fwmark 10 table 200
   sudo ip route flush table 200
   ```

## Bài tập 5 – Kiểm tra hiệu năng routing
1. Dùng `iperf3` để đo throughput giữa hai router (server và client) qua đường tĩnh và qua OSPF/BGP.
2. Ghi lại kết quả và so sánh mức độ overhead.

---

# Lab – Bảo mật mạng (Network Security)

## Mục tiêu
- Thực hành cấu hình firewall, kiểm tra cổng mở, tạo VPN đơn giản và phát hiện tấn công cơ bản.

## Bài tập 1 – Cấu hình firewall với UFW
1. Kiểm tra trạng thái hiện tại:
   ```bash
   sudo ufw status verbose
   ```
2. Đặt chính sách mặc định **deny** cho incoming và **allow** cho outgoing:
   ```bash
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   ```
3. Mở cổng **22/tcp** (SSH) và **443/tcp** (HTTPS):
   ```bash
   sudo ufw allow 22/tcp
   sudo ufw allow 443/tcp
   ```
4. Kích hoạt firewall và xác nhận:
   ```bash
   sudo ufw enable
   sudo ufw status numbered
   ```
5. Thử **ssh** vào máy từ một máy khác và **curl https://example.com** – xác nhận không bị chặn.

## Bài tập 2 – Quét cổng mở trên máy remote (nmap)
1. Cài `nmap` nếu chưa có:
   ```bash
   sudo apt-get install -y nmap
   ```
2. Quét 1000 cổng đầu tiên của máy `192.168.1.20`:
   ```bash
   nmap -p 1-1000 192.168.1.20
   ```
3. Ghi lại các cổng **open** và đề xuất rule firewall tương ứng.

## Bài tập 3 – Thiết lập VPN WireGuard (đơn giản)
1. Cài đặt WireGuard trên cả server và client:
   ```bash
   sudo apt-get install -y wireguard
   ```
2. Trên **server**:
   ```bash
   wg genkey | tee /etc/wireguard/server_private.key | wg pubkey > /etc/wireguard/server_public.key
   wg genkey | tee /etc/wireguard/client_private.key | wg pubkey > /etc/wireguard/client_public.key
   ```
3. Tạo `/etc/wireguard/wg0.conf` trên server (điền key tương ứng):
   ```ini
   [Interface]
   Address = 10.0.0.1/24
   PrivateKey = <SERVER_PRIVATE_KEY>
   ListenPort = 51820

   [Peer]
   PublicKey = <CLIENT_PUBLIC_KEY>
   AllowedIPs = 10.0.0.2/32
   ```
4. Khởi động dịch vụ:
   ```bash
   sudo systemctl enable wg-quick@wg0
   sudo systemctl start wg-quick@wg0
   sudo wg show
   ```
5. Lặp lại trên **client** (đổi địa chỉ, key) và kiểm tra kết nối **ping 10.0.0.1**.

## Bài tập 4 – IDS/IPS cơ bản với Suricata
1. Cài Suricata:
   ```bash
   sudo apt-get install -y suricata
   ```
2. Bật **promiscuous mode** trên giao diện (ví dụ `eth0`):
   ```bash
   sudo ip link set eth0 promisc on
   ```
3. Khởi chạy Suricata để ghi log vào `/var/log/suricata/eve.json`:
   ```bash
   sudo suricata -c /etc/suricata/suricata.yaml -i eth0
   ```
4. Tạo một **attack simple** bằng `hping3` từ máy khác (SYN flood) và quan sát log trong `eve.json`.

## Bài tập 5 – Đánh giá bảo mật website HTTPS
1. Dùng `curl` để kiểm tra chứng chỉ:
   ```bash
   curl -vI https://yourdomain.com 2>&1 | grep "SSL certificate" -A 5
   ```
2. Sử dụng `openssl s_client` để liệt kê cipher suites:
   ```bash
   openssl s_client -connect yourdomain.com:443 -cipher ALL
   ```
3. Đánh giá **TLS version**, **cipher strength**, và đề xuất **upgrade** nếu cần.

---

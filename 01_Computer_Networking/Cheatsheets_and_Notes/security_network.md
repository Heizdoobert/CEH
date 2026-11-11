# Chương 6 – Bảo mật mạng (Network Security)

## 1. Mục tiêu
- Hiểu các **mối đe dọa** phổ biến trong mạng (DoS, MITM, phishing, malware).
- Nắm rõ **cơ chế bảo vệ**: firewall, IDS/IPS, VPN, TLS/SSL, xác thực đa yếu tố.
- Thực hành nhanh trong CLI: cấu hình `ufw`, kiểm tra cổng mở, tạo kết nối VPN đơn giản.

## 2. Các loại tấn công chính
| Loại | Mô tả | Ví dụ thực tế |
|------|-------|---------------|
| **DoS / DDoS** | Gây quá tải tài nguyên máy chủ hoặc mạng. | `hping3 -S -p 80 --flood <target>`
| **Man‑in‑the‑Middle (MITM)** | Người trung gian chặn và thay đổi giao tiếp. | `arpspoof -i eth0 -t 192.168.1.10 -r 192.168.1.1`
| **Phishing** | Giả mạo trang để lấy thông tin đăng nhập. | Email giả mạo, trang login giả.
| **Malware / Ransomware** | Mã độc lây lan qua mạng, mã hoá dữ liệu. | Tải file .exe từ nguồn không tin cậy.

## 3. Cơ chế bảo vệ
- **Firewall** (`ufw`, `iptables`): lọc lưu lượng, chỉ cho phép các cổng cần thiết.
- **IDS/IPS** (`suricata`, `snort`): phát hiện và ngăn chặn mẫu tấn công.
- **VPN** (OpenVPN, WireGuard): mã hoá kênh truyền.
- **TLS/SSL**: bảo vệ HTTP → HTTPS, xác thực server.
- **2FA / MFA**: xác thực đa yếu tố.

## 4. Thực hành nhanh (CLI)
```bash
# Kiểm tra trạng thái firewall (ufw)
sudo ufw status verbose

# Mở cổng 22 (SSH) và đóng tất cả các cổng khác
sudo ufw default deny incoming
sudo ufw allow 22/tcp
sudo ufw enable

# Kiểm tra cổng mở trên remote host (nmap)
nmap -p 1-1024 192.168.1.20

# Tạo kết nối VPN WireGuard (cấu hình nhanh)
sudo apt-get install -y wireguard
wg genkey | tee privatekey | wg pubkey > publickey
# ... viết file /etc/wireguard/wg0.conf và khởi động
sudo wg-quick up wg0
```

## 5. Mini‑quiz
1. DoS khác gì với DDoS? 
2. Lệnh `ufw allow 443/tcp` thực hiện việc gì? 
3. WireGuard sử dụng giao thức nào để mã hoá? 
4. IDS và IPS có điểm khác nhau gì? 
5. Trong TLS, handshake thực hiện mục đích gì?

---

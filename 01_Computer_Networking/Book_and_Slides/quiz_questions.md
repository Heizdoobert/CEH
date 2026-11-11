# BỘ CÂU HỎI TRẮC NGHIỆM ĐÁNH GIÁ NĂNG LỰC MẠNG MÁY TÍNH & INTERNET
## (High-Yield Scenario-Based Networking Quiz & In-Depth Analysis)

*Dựa trên giáo trình: "Introduction to Networking: How the Internet Works" của GS. Charles Severance*  
*Thiết kế: Đội ngũ Giảng viên Mạng & Chuyên gia An ninh Mạng*

---

## HƯỚNG DẪN DÀNH CHO NGƯỜI HỌC & GIẢNG VIÊN
Bộ câu hỏi này không dừng lại ở việc kiểm tra khả năng ghi nhớ lý thuyết thuần túy, mà tập trung vào **tư duy phân tích kịch bản kỹ thuật thực tế (Scenario-based Analytical Thinking)**. Mỗi câu hỏi tái hiện một tình huống mà các kỹ sư quản trị mạng (Network Engineers), lập trình viên Backend/DevOps, hoặc chuyên gia An ninh mạng (Security Analysts) thường xuyên đối mặt trong môi trường sản xuất thực tế cũng như trong các kỳ thi chứng chỉ quốc tế (CompTIA Network+, Cisco CCNA).

---

### CÂU HỎI 1: KHẢO SÁT ĐỊNH TUYẾN & CƠ CHẾ ICMP TIME EXCEEDED CỦA TRACEROUTE

#### Bối cảnh Kỹ thuật (Scenario):
Một kỹ sư mạng đang tiến hành chẩn đoán sự cố suy giảm hiệu năng kết nối từ một máy trạm trong văn phòng đến máy chủ ứng dụng đặt tại Data Center có địa chỉ IP công cộng là `203.0.113.50`. Kỹ sư thực hiện lệnh `traceroute 203.0.113.50` trên máy trạm Linux. Kết quả dòng đầu tiên hiển thị như sau:

```text
traceroute to 203.0.113.50 (203.0.113.50), 30 hops max, 60 byte packets
 1  gateway.local (192.168.1.1)  1.245 ms  1.180 ms  1.152 ms
```

Xét gói tin IP thăm dò (Probe packet) đầu tiên mà máy trạm gửi đi để tạo ra dòng kết quả số 1 nêu trên: Khi gói tin này đến giao diện mạng của thiết bị Default Gateway (`192.168.1.1`), điều gì sẽ diễn ra chính xác nhất tại tầng Mạng (Internet Layer) của thiết bị Gateway này?

---

#### Các Phương án Lựa chọn:
- **A.** Gateway nhận gói tin có `TTL = 1`, thấy địa chỉ IP đích không phải là chính mình nên tăng giá trị `TTL` lên thành `2` rồi chuyển tiếp gói tin sang Router chặng tiếp theo.
- **B.** Gateway nhận gói tin có `TTL = 1`, giảm giá trị trường này đi 1 đơn vị khiến `TTL = 0`. Gateway lập tức hủy (drop) gói tin, đồng thời tạo một bản tin lỗi `ICMP Time Exceeded` (Type 11) gửi ngược về địa chỉ IP của máy trạm.
- **C.** Gateway nhận gói tin có `TTL = 0`, nhận thấy gói tin đã hết hạn nên gửi trả bản tin `ICMP Echo Reply` (Type 0) chứa địa chỉ IP của chính nó để thông báo cho máy trạm biết vị trí chặng 1.
- **D.** Gateway kiểm tra thấy cổng dịch vụ của gói tin bị đóng nên gửi trả bản tin `ICMP Destination Unreachable` (Type 3, Code 3), giúp máy trạm ghi nhận thời gian Round-Trip Time (RTT).

---

#### Đáp án Đúng:
**B. Gateway nhận gói tin có `TTL = 1`, giảm giá trị trường này đi 1 đơn vị khiến `TTL = 0`. Gateway lập tức hủy (drop) gói tin, đồng thời tạo một bản tin lỗi `ICMP Time Exceeded` (Type 11) gửi ngược về địa chỉ IP của máy trạm.**

---

#### Phân tích Chi tiết & Giải thích Sư phạm:
- **Tại sao phương án B ĐÚNG:**
  - Cơ chế cốt lõi của công cụ `traceroute` dựa trên việc chủ động khai thác trường **TTL (Time to Live)** trong IPv4 Header nhằm lập bản đồ các router trung gian.
  - Khi bắt đầu dò chặng 1, máy trạm cố tình tạo gói tin IP với giá trị **`TTL = 1`**.
  - Theo đặc tả giao thức IPv4 (RFC 791), mọi Router khi nhận được một gói tin IP không dành cho chính nó đều phải giảm trường TTL đi 1 đơn vị trước khi định tuyến tiếp.
  - Tại Gateway (`192.168.1.1`), giá trị TTL mới là $1 - 1 = 0$. Theo quy tắc mạng, router **bắt buộc phải hủy (drop) gói tin** để ngăn chặn nguy cơ vòng lặp định tuyến (Routing Loop).
  - Đồng thời, Router sinh ra một thông điệp điều khiển **ICMP Type 11 (Time to Live Exceeded in Transit)** gửi ngược về máy trạm phát gói. Địa chỉ IP nguồn của gói tin ICMP này chính là IP của giao diện router nhận gói (`192.168.1.1`). Nhờ đó, máy trạm trích xuất được địa chỉ IP của Router chặng 1 và tính toán thời gian trễ vòng (RTT) dựa trên chênh lệch thời gian giữa lúc gửi đi và lúc nhận được phản hồi ICMP.

- **Tại sao các phương án gây nhiễu (Distractors) SAI:**
  - **Phương án A SAI:** Router không bao giờ tăng giá trị TTL. TTL chỉ có chiều giảm dần (decrement). Nếu router tăng TTL, vòng lặp định tuyến sẽ không bao giờ kết thúc và làm tê liệt mạng.
  - **Phương án C SAI:** Máy trạm gửi gói tin với `TTL = 1` chứ không phải `TTL = 0`. Hơn nữa, `ICMP Echo Reply` (Type 0) chỉ được sinh ra bởi máy đích để phản hồi gói `ICMP Echo Request` (trong lệnh `ping`), chứ không phải là bản tin báo lỗi hết hạn chặng của router.
  - **Phương án D SAI:** Bản tin `ICMP Destination Unreachable (Port Unreachable - Type 3, Code 3)` chỉ được tạo ra khi gói tin đã đến được **máy chủ đích cuối cùng** (`203.0.113.50`) nhưng máy chủ đó không mở cổng UDP tương ứng. Nó không diễn ra tại router trung gian ở chặng 1.

- **Bối cảnh Kỹ thuật Thực tế & Kỳ thi (Network+ / CCNA):**
  - Trong các bài thi CCNA/Network+, các câu hỏi về cơ chế vận hành của `traceroute` và vai trò của TTL trong việc chặn đứng "Routing Loop" và "Packet Storm" là nội dung trọng tâm. Kỹ sư mạng cần nhớ rõ: Traceroute sử dụng `TTL` tăng dần từ $1, 2, 3...$ và lắng nghe bản tin `ICMP Type 11` từ các router trung gian.

---

### CÂU HỎI 2: PHÂN TÍCH TIẾN TRÌNH BẮT TAY 3 BƯỚC TCP (3-WAY HANDSHAKE)

#### Bối cảnh Kỹ thuật (Scenario):
Một lập trình viên Backend sử dụng Wireshark để phân tích luồng kết nối TCP giữa Web Client (địa chỉ IP `10.0.0.15`, Port `49152`) và Web Server (địa chỉ IP `198.51.100.2`, Port `80`). 

Lập trình viên quan sát thấy gói tin số 1 (Gói khởi tạo kết nối từ Client gửi tới Server) có các thông số kỹ thuật sau:
- Cờ điều khiển: `Flags = [SYN]`
- Số thứ tự khởi tạo: `Sequence Number (raw) = 2.000.000`
- Kích thước cửa sổ đề xuất: `Window Size = 64240`

Giả sử mạng hoạt động hoàn hảo không mất gói, hãy xác định chính xác các giá trị của **Cờ điều khiển (Flags)**, **Sequence Number**, và **Acknowledgment Number** trong **gói tin số 2** (phản hồi từ Server gửi về Client) và **gói tin số 3** (Client gửi ngược lại Server để hoàn tất bắt tay):

---

#### Các Phương án Lựa chọn:
- **A.** 
  - Gói 2: `[SYN, ACK]`, `Seq = 5.000.000`, `Ack = 2.000.000`
  - Gói 3: `[ACK]`, `Seq = 2.000.001`, `Ack = 5.000.000`
- **B.** 
  - Gói 2: `[SYN, ACK]`, `Seq = 5.000.000`, `Ack = 2.000.001`
  - Gói 3: `[ACK]`, `Seq = 2.000.001`, `Ack = 5.000.001`
- **C.** 
  - Gói 2: `[ACK]`, `Seq = 5.000.001`, `Ack = 2.000.001`
  - Gói 3: `[SYN]`, `Seq = 2.000.002`, `Ack = 5.000.002`
- **D.** 
  - Gói 2: `[SYN, ACK]`, `Seq = 2.000.001`, `Ack = 5.000.000`
  - Gói 3: `[ACK]`, `Seq = 5.000.001`, `Ack = 2.000.002`

---

#### Đáp án Đúng:
**B. Gói 2: `[SYN, ACK]`, `Seq = 5.000.000`, `Ack = 2.000.001` | Gói 3: `[ACK]`, `Seq = 2.000.001`, `Ack = 5.000.001`**

---

#### Phân tích Chi tiết & Giải thích Sư phạm:
- **Tại sao phương án B ĐÚNG:**
  - **Quy tắc tiêu tốn Sequence Number của cờ SYN:** Theo chuẩn RFC 793, mặc dù gói tin SYN không mang theo bất kỳ dữ liệu người dùng nào (Payload = 0 bytes), cờ `SYN` (và cả cờ `FIN`) được quy ước **tiêu tốn đúng 1 đơn vị Sequence Number** logic.
  - **Phân tích Gói tin 2 (Server $\rightarrow$ Client):**
    - Server chấp nhận kết nối nên gửi gói tin có bật đồng thời hai cờ `[SYN, ACK]`.
    - Server tự chọn một số thứ tự khởi tạo độc lập của riêng mình (**ISN_server**), giả sử là `Seq = 5.000.000`.
    - Server xác nhận đã nhận được gói SYN của Client bằng cách đặt số Acknowledgment bằng:
      $$\text{Ack} = \text{ISN}_{\text{client}} + 1 = 2.000.000 + 1 = 2.000.001$$
      *(Ý nghĩa: "Tôi đã nhận trọn vẹn gói SYN có số thứ tự 2.000.000 của bạn, byte dữ liệu tiếp theo tôi mong chờ từ bạn là byte 2.000.001")*.
  - **Phân tích Gói tin 3 (Client $\rightarrow$ Server):**
    - Client hoàn tất bắt tay bằng gói tin chỉ bật cờ `[ACK]`.
    - Số thứ tự của Client lúc này tiến lên 1 đơn vị: `Seq = 2.000.001`.
    - Client xác nhận gói SYN của Server bằng cách đặt:
      $$\text{Ack} = \text{ISN}_{\text{server}} + 1 = 5.000.000 + 1 = 5.000.001$$
      *(Ý nghĩa: "Tôi đã nhận trọn vẹn gói SYN có số thứ tự 5.000.000 của Server, byte tiếp theo tôi mong chờ từ Server là 5.000.001")*.

- **Tại sao các phương án gây nhiễu (Distractors) SAI:**
  - **Phương án A SAI:** Đặt `Ack = 2.000.000` ở gói 2 là sai quy tắc. Nếu nhận được `Ack = 2.000.000`, Client sẽ hiểu là Server chưa nhận được byte 2.000.000 và sẽ gửi lại gói SYN ban đầu.
  - **Phương án C SAI:** Gói 2 thiếu cờ `SYN` (chỉ có cờ `ACK`), điều này vi phạm nguyên tắc đồng bộ hóa hai chiều vì Server chưa gửi số ISN của mình cho Client. Gói 3 lại bật cờ `SYN` thay vì chỉ bật cờ `ACK`.
  - **Phương án D SAI:** Nhầm lẫn vị trí của Sequence Number và Acknowledgment Number giữa Server và Client. Server không thể lấy `2.000.001` làm Sequence Number của chính nó.

- **Bối cảnh Kỹ thuật Thực tế & Lập trình Sockets:**
  - Khi phân tích sự cố rớt mạng hoặc tấn công từ chối dịch vụ dạng **SYN Flood**, hiểu rõ logic tăng Sequence Number và cờ SYN/ACK giúp kỹ sư bảo mật phát hiện các gói tin giả mạo hoặc nhận biết hiện tượng Client bị "treo" ở trạng thái `SYN_SENT` còn Server kẹt ở `SYN_RCVD`.

---

### CÂU HỎI 3: KIỂM SOÁT LUỒNG VỚI CỬA SỔ TRƯỢT & HIỆN TƯỢNG ZERO WINDOW

#### Bối cảnh Kỹ thuật (Scenario):
Một máy chủ cơ sở dữ liệu tốc độ cao (Server) đang truyền một tệp kết xuất sao lưu (database dump) có dung lượng 500 MB cho một máy tính trạm văn phòng (Client) thông qua giao thức TCP. Trong quá trình truyền dữ liệu, máy trạm Client bất ngờ bị quá tải CPU do phần mềm quét virus chạy ngầm chiếm dụng 100% tài nguyên xử lý, khiến ứng dụng phía Client không thể gọi hàm `recv()` để đọc dữ liệu từ bộ nhớ đệm nhận (Receive Buffer) của hệ điều hành.

Sau vài giây, gói tin TCP ACK gửi từ Client ngược về Server có trường **`Window Size = 0`**. 

Giao thức TCP tại máy chủ Server sẽ xử lý tình huống này như thế nào để vừa không làm tràn bộ đệm máy trạm, vừa không để kết nối bị "chết lâm sàng"?

---

#### Các Phương án Lựa chọn:
- **A.** Server lập tức gửi gói tin có cờ `[RST]` để ngắt kết nối khẩn cấp, giải phóng tài nguyên bộ nhớ cho hệ điều hành vì coi như Client đã bị sập (crash).
- **B.** Server chuyển sang sử dụng giao thức UDP để đẩy tiếp phần dữ liệu còn lại với tốc độ tối đa, bỏ qua việc kiểm tra bộ đệm của Client.
- **C.** Server tạm dừng gửi dữ liệu người dùng mới, kích hoạt một bộ đếm thời gian (**Persist Timer**), và định kỳ gửi các gói tin thăm dò cửa sổ (**Zero Window Probes**) có kích thước 1 byte để kích thích Client phản hồi cập nhật trạng thái bộ đệm.
- **D.** Server tiếp tục truyền dữ liệu theo đúng tốc độ ban đầu nhưng đính kèm cờ `[PSH]` (Push) trong tiêu đề TCP để ép buộc card mạng của Client phải ghi dữ liệu trực tiếp vào ổ cứng.

---

#### Đáp án Đúng:
**C. Server tạm dừng gửi dữ liệu người dùng mới, kích hoạt một bộ đếm thời gian (Persist Timer), và định kỳ gửi các gói tin thăm dò cửa sổ (Zero Window Probes) có kích thước 1 byte để kích thích Client phản hồi cập nhật trạng thái bộ đệm.**

---

#### Phân tích Chi tiết & Giải thích Sư phạm:
- **Tại sao phương án C ĐÚNG:**
  - **Bản chất của Flow Control (Kiểm soát luồng):** Cơ chế Cửa sổ trượt (Sliding Window) được thiết kế chính xác để bảo vệ bên nhận không bị "ngập lụt" dữ liệu (Buffer Overflow).
  - Khi bộ nhớ đệm tiếp nhận của Client bị đầy (do CPU bận không đọc kịp), Client thông báo **`Window Size = 0` (Zero Window)**. Nhận được tín hiệu này, Server bắt buộc phải ngừng phát dữ liệu mới.
  - **Nguy cơ Bế tắc (Deadlock):** Giả sử sau đó Client xử lý xong dữ liệu trong bộ đệm và gửi một gói ACK thông báo cửa sổ đã mở lại (`Window Size = 32768`). Nếu gói ACK này rủi ro bị **rơi mất trên đường truyền**, Server sẽ mãi mãi chờ thông báo mở cửa sổ từ Client, còn Client lại mãi mãi chờ dữ liệu mới từ Server $\rightarrow$ Kết nối rơi vào tình trạng "chết lâm sàng" (Deadlock)!
  - **Giải pháp Persist Timer & Zero Window Probe:** Để phá vỡ nguy cơ bế tắc này, chuẩn TCP quy định Server phải khởi động một bộ đếm thời gian gọi là **Persist Timer**. Khi bộ đếm hết hạn, Server chủ động phát một gói tin thăm dò đặc biệt (**Zero Window Probe**) chứa đúng **1 byte dữ liệu cũ hoặc byte thăm dò**.
  - Khi nhận được gói thăm dò này, Client buộc phải phản hồi một gói ACK cập nhật dung lượng `Window Size` hiện tại. Quá trình này lặp lại cho đến khi cửa sổ thực sự mở lại, kết nối tiếp tục truyền dữ liệu bình thường.

- **Tại sao các phương án gây nhiễu (Distractors) SAI:**
  - **Phương án A SAI:** Server không gửi cờ `RST`. Hiện tượng Zero Window là một trạng thái điều tiết luồng hoàn toàn hợp lệ và bình thường của TCP khi bên nhận tạm thời quá tải, không phải là lỗi kết nối nghiêm trọng cần hủy bỏ phiên.
  - **Phương án B SAI:** TCP và UDP là hai giao thức hoàn toàn độc lập ở Tầng Giao vận. Một phiên kết nối TCP không thể tự ý "chuyển đổi" sang UDP giữa chừng.
  - **Phương án D SAI:** Cờ `PSH` (Push) chỉ có tác dụng yêu cầu hệ điều hành đẩy dữ liệu từ bộ đệm lên tầng ứng dụng nhanh hơn, chứ không thể ép buộc ghi thẳng vào ổ cứng hay ghi đè lên bộ đệm khi bộ đệm đã đầy 100%.

- **Bối cảnh Kỹ thuật Thực tế & Performance Tuning:**
  - Khi tối ưu hóa hệ thống backend truyền dữ liệu lớn (Streaming, Database Replication, File Storage), việc xuất hiện các gói cảnh báo `TCP ZeroWindow` và `TCP Window Full` trên Wireshark là chỉ dấu rõ ràng cho thấy nút thắt cổ chai (bottleneck) nằm ở tốc độ xử lý hoặc khả năng tiêu thụ I/O của ứng dụng phía Client/Receiver chứ không phải do đường truyền mạng bị chậm.

---

### CÂU HỎI 4: BIÊN DỊCH ĐỊA CHỈ MẠNG (NAT/NAPT) & ĐỊNH TUYẾN GÓI PHẢN HỒI

#### Bối cảnh Kỹ thuật (Scenario):
Một mạng văn phòng sử dụng dải địa chỉ nội bộ chuẩn RFC 1918 là `192.168.1.0/24`. Thiết bị Router biên kết nối Internet có cấu hình tính năng NAPT (Network Address Port Translation) với một địa chỉ IP công cộng (Public IP) duy nhất do nhà mạng ISP cung cấp là `203.0.113.10`.

Tại cùng một thời điểm:
- Máy tính A (`192.168.1.10`) mở trình duyệt gửi yêu cầu HTTP tới Web Server `93.184.216.34:80`, sử dụng cổng nguồn tạm thời là `51234`.
- Máy tính B (`192.168.1.20`) cũng mở trình duyệt gửi yêu cầu HTTP tới chính Web Server `93.184.216.34:80`, và ngẫu nhiên hệ điều hành của máy B cũng cấp phát đúng số cổng nguồn là `51234`.

Khi Router nhận được hai gói tin trên từ mạng nội bộ và chuyển tiếp chúng ra Internet công cộng, Router sẽ xử lý như thế nào để khi Web Server phản hồi, dữ liệu được trả về chính xác cho từng máy tính mà không bị nhầm lẫn?

---

#### Các Phương án Lựa chọn:
- **A.** Router từ chối gói tin của Máy tính B và gửi trả mã lỗi xung đột mạng, vì trên Internet không thể tồn tại hai kết nối có cùng số cổng nguồn `51234`.
- **B.** Router giữ nguyên địa chỉ IP nguồn `192.168.1.10` và `192.168.1.20`, chỉ thay đổi địa chỉ MAC nguồn thành địa chỉ MAC của Router khi gửi ra Internet.
- **C.** Router thay đổi địa chỉ IP nguồn của cả hai gói thành `203.0.113.10`, đồng thời ánh xạ lại cổng nguồn thành hai số cổng công cộng khác nhau (ví dụ: `40001` cho Máy A và `40002` cho Máy B), rồi lưu thông tin tương ứng vào Bảng NAT (NAT Translation Table).
- **D.** Router hợp nhất hai yêu cầu thành một gói tin HTTP duy nhất gửi tới Web Server, sau đó khi nhận dữ liệu về sẽ sao chép làm đôi gửi cho cả hai máy.

---

#### Đáp án Đúng:
**C. Router thay đổi địa chỉ IP nguồn của cả hai gói thành `203.0.113.10`, đồng thời ánh xạ lại cổng nguồn thành hai số cổng công cộng khác nhau (ví dụ: `40001` cho Máy A và `40002` cho Máy B), rồi lưu thông tin tương ứng vào Bảng NAT (NAT Translation Table).**

---

#### Phân tích Chi tiết & Giải thích Sư phạm:
- **Tại sao phương án C ĐÚNG:**
  - **Bản chất của NAPT (Port Address Translation):** Trong hầu hết các router gia đình và văn phòng, kỹ thuật NAT thực chất là **NAPT (Biên dịch cả Địa chỉ IP lẫn Số Cổng)**.
  - Khi Máy tính A gửi gói tin: `Src IP = 192.168.1.10`, `Src Port = 51234`.
  - Khi Máy tính B gửi gói tin: `Src IP = 192.168.1.20`, `Src Port = 51234`.
  - Nếu Router chỉ thay IP thành `203.0.113.10` mà giữ nguyên cổng `51234` cho cả hai, khi Web Server trả lời về `203.0.113.10:51234`, Router sẽ hoàn toàn "mù thông tin", không thể biết gói tin này là của Máy A hay Máy B!
  - Do đó, Router can thiệp sâu vào **cả IP Header lẫn TCP Header**:
    1. Thay IP nguồn của cả hai gói thành IP công cộng: `203.0.113.10`.
    2. Cấp phát hai cổng ngoài ngẫu nhiên duy nhất, ví dụ: gán cho Máy A cổng `40001`, gán cho Máy B cổng `40002`.
    3. Ghi vào **Bảng trạng thái NAT (NAT State Table)**:
       - Dòng 1: `192.168.1.10:51234 <---> 203.0.113.10:40001 <---> 93.184.216.34:80`
       - Dòng 2: `192.168.1.20:51234 <---> 203.0.113.10:40002 <---> 93.184.216.34:80`
    4. Tính toán lại mã kiểm tra lỗi (Checksum) cho cả IP Header và TCP Header rồi mới phát ra Internet.
  - Khi Server phản hồi gói tin về `203.0.113.10:40001`, Router tra bảng NAT, thấy cổng `40001` thuộc về Máy A, nó lập tức sửa IP đích thành `192.168.1.10` và cổng đích thành `51234` rồi đẩy vào mạng LAN. Quá trình diễn ra hoàn toàn trong suốt đối với người dùng và máy chủ.

- **Tại sao các phương án gây nhiễu (Distractors) SAI:**
  - **Phương án A SAI:** Router hoàn toàn không từ chối kết nối. NAPT được thiết kế chính xác để giải quyết bài toán trùng lặp số cổng giữa các máy tính nội bộ khác nhau.
  - **Phương án B SAI:** Các địa chỉ IP nội bộ RFC 1918 (như `192.168.x.x`) là địa chỉ không thể định tuyến trên Internet công cộng (Non-routable). Nếu Router giữ nguyên IP nguồn này gửi ra ngoài, các router của ISP sẽ lập tức vứt bỏ gói tin hoặc Web Server không thể nào định tuyến gói phản hồi quay về được.
  - **Phương án D SAI:** Router là thiết bị hoạt động ở Tầng Mạng/Giao vận, nó không hiểu và không được phép tự ý gộp dữ liệu bản tin HTTP ở Tầng Ứng dụng của hai người dùng khác nhau.

- **Bối cảnh Kỹ thuật Thực tế & DevOps:**
  - Hiểu rõ cơ chế bảng NAPT là chìa khóa để xử lý sự cố kết nối trong các hệ sinh thái Docker / Kubernetes (nơi các container dùng mạng overlay NAT), cũng như giải thích tại sao các giao thức truyền thông ngang hàng P2P (VoIP, BitTorrent, WebRTC) gặp khó khăn khi thiết lập kết nối trực tiếp xuyên qua Router và phải cần đến các giao thức trung gian như STUN/TURN/ICE.

---

### CÂU HỎI 5: BẢO MẬT GIAO VẬN TLS/SSL & CHUỖI XÁC THỰC CHỨNG CHỈ SỐ (CA TRUST CHAIN)

#### Bối cảnh Kỹ thuật (Scenario):
Một người dùng kết nối máy tính xách tay vào mạng Wi-Fi công cộng tại một quán cafe và truy cập vào trang web ngân hàng trực tuyến `https://ebank.vietbank.com.vn`. Ngay lập tức, trình duyệt Chrome chặn kết nối và hiển thị màn hình cảnh báo màu đỏ:

> **"Your connection is not private" (Kết nối của bạn không phải là kết nối riêng tư)**  
> Mã lỗi: `NET::ERR_CERT_AUTHORITY_INVALID`

Trong khi đó, nếu người dùng này ngắt Wi-Fi quán cafe và bật mạng 4G từ điện thoại để truy cập thì website mở ra hoàn toàn bình thường với biểu tượng ổ khóa an toàn màu xanh.

Phân tích nào sau đây giải thích **chính xác nhất bản chất kỹ thuật** của nguyên nhân gây ra cảnh báo trên và mối đe dọa bảo mật tiềm tàng trong tình huống này?

---

#### Các Phương án Lựa chọn:
- **A.** Wi-Fi quán cafe sử dụng chuẩn mã hóa WPA2 yếu làm hỏng khóa đối xứng AES trong quá trình truyền dẫn khung dữ liệu ở Tầng Liên kết.
- **B.** Kẻ tấn công trên mạng Wi-Fi đang thực hiện kỹ thuật tấn công Man-in-the-Middle (MitM), giả mạo máy chủ ngân hàng và cung cấp một Chứng chỉ số tự ký (Self-signed Certificate) không được ký bởi bất kỳ Tổ chức Chứng thực Số (Root CA) tin cậy nào có sẵn trong máy tính của người dùng.
- **C.** Máy chủ ngân hàng đã hết hạn bản quyền tên miền tại cơ quan quản lý tên miền quốc tế ICANN, khiến hệ thống DNS không thể phân giải ra bản ghi địa chỉ IPv4.
- **D.** Trình duyệt người dùng chưa hỗ trợ giao thức HTTP/2, do đó máy chủ ngân hàng từ chối đàm phán thuật toán bắt tay ba bước TCP.

---

#### Đáp án Đúng:
**B. Kẻ tấn công trên mạng Wi-Fi đang thực hiện kỹ thuật tấn công Man-in-the-Middle (MitM), giả mạo máy chủ ngân hàng và cung cấp một Chứng chỉ số tự ký (Self-signed Certificate) không được ký bởi bất kỳ Tổ chức Chứng thực Số (Root CA) tin cậy nào có sẵn trong máy tính của người dùng.**

---

#### Phân tích Chi tiết & Giải thích Sư phạm:
- **Tại sao phương án B ĐÚNG:**
  - **Nguyên lý Chuỗi tin cậy (Chain of Trust) trong TLS:** Trong quá trình bắt tay TLS (TLS Handshake), máy chủ web gửi cho trình duyệt một **Chứng chỉ số X.509** chứa Tên miền, Public Key của máy chủ và **Chữ ký điện tử** của một Cơ quan Chứng thực (Certificate Authority - CA).
  - Trình duyệt và Hệ điều hành (Windows, macOS, Linux, Android, iOS) luôn lưu sẵn một danh bạ các **Root CA uy tín** toàn cầu (như DigiCert, Sectigo, Let's Encrypt...) kèm Public Key gốc của các CA này.
  - Trình duyệt sẽ dùng Public Key của Root CA để giải mã và kiểm tra chữ ký số trên chứng chỉ của máy chủ. Nếu hợp lệ, trình duyệt tin tưởng 100% rằng Public Key này thuộc về đúng ngân hàng `ebank.vietbank.com.vn`.
  - **Kịch bản Tấn công Đứng giữa (Man-in-the-Middle):** Kẻ tấn công ở mạng Wi-Fi mở đã thực hiện kỹ thuật đầu độc ARP (ARP Spoofing) hoặc giả mạo DNS (DNS Spoofing) để hướng luồng truy cập của nạn nhân về máy chủ giả mạo của kẻ tấn công.
  - Để có thể bẻ khóa và đọc lén dữ liệu ngân hàng, kẻ tấn công phải tự tạo ra một cặp khóa và một **Chứng chỉ số mạo danh (Self-signed hoặc ký bởi CA lạ)** rồi đẩy cho trình duyệt nạn nhân.
  - Khi trình duyệt kiểm tra chứng chỉ này, nó phát hiện: *Chữ ký trên chứng chỉ này không xuất phát từ bất kỳ Root CA uy tín nào được cài sẵn trong kho chứng thực của hệ thống!*
  - Do đó, trình duyệt lập tức chặn đứng kết nối và kích hoạt mã lỗi `NET::ERR_CERT_AUTHORITY_INVALID` để bảo vệ tài khoản ngân hàng của người dùng khỏi bị đánh cắp. Khi chuyển sang mạng 4G, người dùng kết nối thẳng tới máy chủ thật nên chứng chỉ hợp lệ và hiển thị ổ khóa xanh.

- **Tại sao các phương án gây nhiễu (Distractors) SAI:**
  - **Phương án A SAI:** Lỗi ở đây xảy ra ở Tầng Giao vận/Ứng dụng (TLS Layer), không liên quan đến chuẩn mã hóa sóng vô tuyến WPA2 của Tầng Liên kết. Nếu khung dữ liệu tầng 2 bị méo tín hiệu, gói tin sẽ bị kiểm tra CRC thất bại và bị loại bỏ chứ không thể sinh ra mã lỗi SSL chi tiết của trình duyệt.
  - **Phương án C SAI:** Lỗi hết hạn tên miền hoặc không phân giải được IP sẽ dẫn đến mã lỗi DNS như `DNS_PROBE_FINISHED_NXDOMAIN` hoặc `ERR_NAME_NOT_RESOLVED`, chứ không kích hoạt lỗi `CERT_AUTHORITY_INVALID` của lớp bảo mật TLS.
  - **Phương án D SAI:** Bắt tay 3 bước TCP diễn ra ở Tầng 4 độc lập và trước khi đàm phán phiên bản HTTP/2. Hơn nữa, nếu client không hỗ trợ HTTP/2, web server sẽ tự động hạ cấp tương thích ngược về HTTP/1.1 thông qua đàm phán ALPN chứ không bao giờ ngắt kết nối với thông báo lỗi chứng chỉ.

- **Bối cảnh Kỹ thuật Thực tế & An ninh Thông tin (SecOps / Ethical Hacking):**
  - Đây là tình huống an ninh mạng kinh điển mà mọi chuyên gia an toàn thông tin đều phải nắm vững. Nó nhấn mạnh vai trò sống còn của Hạ tầng Khóa Công khai (PKI) và cảnh báo người dùng tuyệt đối không bao giờ được bấm "Bỏ qua cảnh báo để tiếp tục" (Proceed anyway) khi truy cập các dịch vụ nhạy cảm trên mạng Wi-Fi công cộng.

---

## BẢNG TỔNG KẾT ĐÁP ÁN NHANH (ANSWER KEY)

| Câu hỏi | Chủ đề Kiến thức | Tầng Mạng Tương ứng | Đáp án Đúng |
| :---: | :--- | :--- | :---: |
| **Câu 1** | Cơ chế Traceroute & ICMP Time Exceeded | Tầng Mạng (Internet Layer - IP) | **B** |
| **Câu 2** | Bắt tay 3 bước & Đánh số Sequence/ACK | Tầng Giao vận (Transport Layer - TCP) | **B** |
| **Câu 3** | Cửa sổ trượt & Hiện tượng Zero Window | Tầng Giao vận (Flow Control) | **C** |
| **Câu 4** | Biên dịch địa chỉ & Bảng ánh xạ cổng NAPT | Tầng Mạng & Giao vận (NAT / RFC 1918) | **C** |
| **Câu 5** | Bắt tay TLS/SSL & Chuỗi xác thực CA | Bảo mật Tầng Giao vận (Transport Security) | **B** |

Mô-đun 03: Quét Mạng

Kịch bản

Trước đó, bạn đã thu thập tất cả thông tin có thể về mục tiêu chẳng hạn như thông tin tổ chức (chi tiết nhân viên, chi tiết đối tác, liên kết web, v.v.), thông tin mạng (tên miền, tên miền phụ, tên miền phụ cấp hai, địa chỉ IP, cấu trúc mạng, v.v.), và thông tin hệ thống (chi tiết hệ điều hành, tài khoản người dùng, mật khẩu, v.v.).

Bây giờ, với vai trò là một hacker đạo đức, hoặc là một người kiểm thử xâm nhập (sau đây gọi là pen tester), bước tiếp theo của bạn sẽ là thực hiện quét cổng và quét mạng trên các địa chỉ IP mà bạn đã thu thập được trong giai đoạn thu thập thông tin. Điều này sẽ giúp bạn xác định một điểm nhập vào mạng mục tiêu.

Quét chính nó không phải là sự xâm nhập thực sự, mà là một hình thức trinh sát mở rộng trong đó hacker đạo đức và kiểm thử xâm nhập học hỏi thêm về mục tiêu, bao gồm thông tin về các cổng và dịch vụ mở, hệ điều hành và bất kỳ sơ suất cấu hình nào. Thông tin thu thập được từ hoạt động trinh sát này giúp bạn chọn các chiến lược tấn công hệ thống hoặc mạng mục tiêu.

Đây là một trong những giai đoạn quan trọng nhất của việc thu thập thông tin tình báo, giúp bạn tạo hồ sơ của tổ chức mục tiêu. Trong quá trình quét, bạn cố gắng thu thập thông tin, bao gồm các địa chỉ IP cụ thể của hệ thống mục tiêu có thể truy cập qua mạng (các máy chủ đang hoạt động), các cổng mở, các dịch vụ tương ứng đang chạy trên các cổng mở và các lỗ hổng trong các máy chủ đang hoạt động.

Quét cổng sẽ giúp bạn xác định các cổng mở và các dịch vụ đang chạy trên các cổng cụ thể, điều này liên quan đến việc kết nối với các cổng hệ thống Giao thức Điều khiển Truyền tải (TCP) và Giao thức Datagram Người dùng (UDP). Quét cổng cũng được sử dụng để phát hiện các lỗ hổng trong các dịch vụ đang chạy trên một cổng.

Các bài lab trong mô-đun này sẽ cung cấp cho bạn kinh nghiệm thực tế trong việc thu thập thông tin về tổ chức mục tiêu bằng cách sử dụng các kỹ thuật quét mạng và quét cổng khác nhau.

Mục tiêu

Mục tiêu của bài lab này là thực hiện quét mạng, quét cổng, phân tích các lỗ hổng mạng, v.v.

Cần thực hiện quét mạng để:

-   Kiểm tra các hệ thống đang hoạt động và các cổng mở

-   Xác định các dịch vụ đang chạy trên hệ thống trực tiếp

-   Thực hiện việc lấy thông tin banner/nhận dạng hệ điều hành

-   Xác định các lỗ hổng mạng

Tổng quan về mạng quét

Quét mạng là quá trình thu thập thông tin chi tiết bổ sung về mục tiêu bằng cách sử dụng các kỹ thuật trinh sát tinh vi và tấn công cao. Mục đích của việc quét là phát hiện các kênh liên lạc có thể khai thác, dò tìm càng nhiều đối tượng nghe càng tốt và theo dõi những đối tượng phản hồi.

Các loại quét:

-   **Quét cổng: Liệt kê các cổng và dịch vụ đang mở**

-   **Quét Mạng: Liệt kê các máy chủ và địa chỉ IP đang hoạt động**

-   **Quét lỗ hổng: Hiển thị sự hiện diện của các điểm yếu đã biết**

Nhiệm vụ bài lab

Các hacker đạo đức và chuyên gia kiểm tra xâm nhập sử dụng nhiều công cụ và kỹ thuật để quét mạng mục tiêu. Các bài lab được khuyến nghị giúp bạn học các kỹ thuật quét mạng khác nhau bao gồm:

1.  Thực hiện phát hiện máy chủ

    -   Thực hiện khám phá máy chủ bằng Nmap

2.  Thực hiện khám phá cổng và dịch vụ

    -   Khám phá các kỹ thuật quét mạng khác nhau bằng Nmap

3.  Thực hiện phát hiện hệ điều hành

    -   Thực hiện khám phá hệ điều hành sử dụng Engine Script Nmap (NSE)

4.  Quét vượt ra ngoài IDS và Tường lửa

    -   Quét vượt qua IDS/tường lửa bằng cách sử dụng các kỹ thuật né tránh khác nhau

5.  Thực hiện quét mạng bằng cách sử dụng các công cụ quét khác nhau

    -   Quét một mạng mục tiêu bằng Metasploit

6.  Thực hiện Quét Mạng sử dụng AI

    -   Quét một mục tiêu bằng ShellGPT

TrướcTiếp

Thí nghiệm 1: Thực hiện Khám phá Máy chủ

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc kiểm thử xâm nhập, bạn nên có khả năng quét và phát hiện các hệ thống/thiết bị mạng đang hoạt động trong mạng mục tiêu. Trong giai đoạn quét mạng của đánh giá bảo mật, nhiệm vụ đầu tiên của bạn là quét các hệ thống/thiết bị mạng được kết nối với mạng mục tiêu trong phạm vi IP được chỉ định và kiểm tra các hệ thống đang hoạt động trong mạng mục tiêu.

**Mục tiêu bài lab**

-   Thực hiện khám phá máy chủ bằng Nmap

**Tổng quan về Khám phá Máy chủ**

Khám phá máy chủ được coi là nhiệm vụ chính trong quá trình quét mạng. Nó được sử dụng để phát hiện các máy chủ hoạt động/sống trong một mạng. Nó cung cấp trạng thái chính xác của các hệ thống trong mạng, từ đó giảm thời gian quét từng cổng trên từng hệ thống trong biển địa chỉ IP để xác định xem máy chủ mục tiêu có đang hoạt động hay không.

Dưới đây là một số ví dụ về các kỹ thuật khám phá máy chủ:

-   Quét ping ARP

-   Quét ping UDP

-   Quét ping ICMP (ping ICMP ECHO, dấu thời gian ICMP, ping ICMP và ping mặt nạ địa chỉ)

-   Quét ping TCP (ping TCP SYN và ping TCP ACK)

-   Quét ping giao thức IP

Nhiệm vụ 1: Thực hiện Khám phá Máy chủ bằng Nmap

Nmap là một tiện ích được sử dụng để khám phá mạng, quản trị mạng và kiểm toán bảo mật. Nó cũng được sử dụng để thực hiện các nhiệm vụ như lập bảng kiểm kê mạng, quản lý lịch nâng cấp dịch vụ và giám sát thời gian hoạt động của máy chủ hoặc dịch vụ.

Ở đây, chúng ta sẽ sử dụng Nmap để khám phá danh sách các máy chủ đang hoạt động trong mạng mục tiêu. Chúng ta có thể sử dụng Nmap để quét các máy chủ đang hoạt động trong mạng mục tiêu bằng các kỹ thuật phát hiện máy chủ khác nhau như quét ping ARP, quét ping UDP, quét ping ICMP ECHO, quét ICMP ECHO ping sweep, v.v.

1.  Theo mặc định, máy Windows 11 được chọn, nhấp vào Parrot Security để chuyển sang máy Parrot Security. Đăng nhập bằng attacker/toor.[Parrot Security](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> Nếu một cửa sổ bật lên Parrot Updater xuất hiện ở góc trên bên phải của Màn hình, hãy bỏ qua và đóng nó.
>
> Nếu một cửa sổ bật lên Hỏi xuất hiện yêu cầu bạn cập nhật máy, hãy nhấp vào Không để đóng cửa sổ.

2.  Mở một cửa sổ Terminal và thực thi sudo su để chạy các chương trình với quyền người dùng root (Khi được yêu cầu, nhập mật khẩu toor).

> Mật khẩu mà bạn nhập sẽ không hiển thị.

3.  Chạy lệnh nmap -sn -PR \[Địa chỉ IP mục tiêu\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.22).

> **-sn: vô hiệu hóa quét cổng và -PR: thực hiện quét ping ARP.**

4.  Kết quả quét xuất hiện, cho thấy Host mục tiêu đang hoạt động, như được hiển thị trong ảnh chụp màn hình.

> Trong bài lab này, chúng tôi đang nhắm vào máy Windows Server 2022 (10.10.1.22).
>
> Quét ping ARP dò thử yêu cầu ARP tới máy chủ mục tiêu; phản hồi ARP có nghĩa là máy chủ đó đang hoạt động.
>
> ![Screenshot](media/image2.jpeg){width="10.6625in" height="8.0in"}

5.  Chạy lệnh nmap -sn -PU \[Địa chỉ IP mục tiêu\], (ở đây, địa chỉ IP mục tiêu là 10.10.1.22). Kết quả quét xuất hiện, cho thấy Host mục tiêu đang hoạt động, như được hiển thị trong ảnh chụp màn hình.

> **-PU: thực hiện quét ping UDP.**
>
> Quét ping UDP gửi các gói UDP đến máy chủ mục tiêu; một phản hồi UDP có nghĩa là máy chủ đang hoạt động. Nếu máy chủ mục tiêu ngoại tuyến hoặc không thể truy cập, các thông báo lỗi khác nhau như \"máy chủ/mạng không thể truy cập\" hoặc \"TTL vượt quá\" có thể được trả về.
>
> ![Screenshot](media/image3.jpeg){width="10.6625in" height="8.0in"}

6.  Bây giờ, chúng ta sẽ thực hiện quét ICMP ECHO ping. Chạy lệnh nmap -sn -PE \[Địa chỉ IP mục tiêu\], (ở đây, địa chỉ IP mục tiêu là 10.10.1.22). Kết quả quét xuất hiện, cho thấy máy chủ mục tiêu đang hoạt động, như hiển thị trong ảnh chụp màn hình.

> **-PE: thực hiện quét ping ICMP ECHO.**
>
> Quét ping ICMP ECHO bao gồm việc gửi các yêu cầu ICMP ECHO tới một máy chủ. Nếu máy chủ mục tiêu đang hoạt động, nó sẽ trả về một hồi đáp ICMP ECHO. Quét này hữu ích để xác định các thiết bị đang hoạt động hoặc xác định xem ICMP có đi qua tường lửa hay không.
>
> ![Screenshot](media/image4.jpeg){width="10.6625in" height="8.0in"}

7.  Bây giờ, chúng ta sẽ thực hiện quét ICMP ECHO ping để phát hiện các máy chủ hoạt động từ một phạm vi địa chỉ IP mục tiêu. Chạy lệnh nmap -sn -PE \[Phạm vi địa chỉ IP mục tiêu\] (trong trường hợp này, phạm vi địa chỉ IP mục tiêu là 10.10.1.10-23). Kết quả quét sẽ xuất hiện, chỉ ra rằng máy chủ mục tiêu đang hoạt động, như được hiển thị trong ảnh chụp màn hình.

> Trong nhiệm vụ bài lab này, chúng ta đang quét các máy Windows 11, Windows Server 2022, Windows Server 2019 và Android. Nếu máy Android bị tắt, hãy điều hướng đến tab Tài nguyên và chọn Android. Nhấp vào biểu tượng Nguồn và Hiển thị ở phần trên của trang, từ các tùy chọn thả xuống, chọn Đặt lại/Khởi động lại và nhấp vào Có.
>
> Chạy quét ICMP ECHO ping được sử dụng để xác định các máy chủ đang hoạt động từ một phạm vi địa chỉ IP bằng cách gửi các yêu cầu ICMP ECHO tới nhiều máy chủ. Nếu một máy chủ đang hoạt động, nó sẽ trả lại một phản hồi ICMP ECHO.
>
> ![Screenshot](media/image5.jpeg){width="10.6625in" height="8.0in"}

8.  Chạy lệnh nmap -sn -PP \[Địa chỉ IP mục tiêu\], (ở đây, địa chỉ IP mục tiêu là 10.10.1.22). Kết quả quét xuất hiện, cho thấy Host mục tiêu đang hoạt động, như được hiển thị trong ảnh chụp màn hình.

> **-PP: thực hiện quét ping dấu thời gian ICMP.**
>
> Ping dấu thời gian ICMP là một loại ping ICMP tùy chọn và bổ sung, trong đó kẻ tấn công gửi truy vấn một thông điệp dấu thời gian để lấy thông tin liên quan đến thời gian hiện tại từ máy chủ mục tiêu.
>
> ![Screenshot](media/image6.jpeg){width="10.6625in" height="8.0in"}

9.  Ngoài các kỹ thuật quét mạng đã đề cập ở trên, bạn cũng có thể sử dụng các kỹ thuật quét sau để thực hiện việc phát hiện máy chủ trên một mạng mục tiêu.

    -   **Quét Ping Mặt Nạ Địa Chỉ ICMP: Kỹ thuật này là một phương án thay thế cho quét ping ICMP ECHO truyền thống, được sử dụng để xác định liệu máy chủ mục tiêu có đang hoạt động hay không, đặc biệt khi các quản trị viên chặn các ping ICMP ECHO.**

> **\# nmap -sn -PM \[địa chỉ IP mục tiêu\]**

-   **Quét Ping TCP SYN: Kỹ thuật này gửi các gói TCP SYN rỗng đến máy chủ mục tiêu, phản hồi ACK có nghĩa là máy chủ đang hoạt động.**

> **\# nmap -sn -PS \[địa chỉ IP mục tiêu\]**

-   **Quét Ping TCP ACK: Kỹ thuật này gửi các gói TCP ACK rỗng đến máy chủ mục tiêu; phản hồi RST có nghĩa là máy chủ đang hoạt động.**

> **\# nmap -sn -PA \[địa chỉ IP mục tiêu\]**

-   **Quét Ping Giao thức IP: Kỹ thuật này gửi các gói thăm dò khác nhau của các giao thức IP khác nhau đến máy chủ mục tiêu, bất kỳ phản hồi nào từ bất kỳ gói thăm dò nào đều cho thấy rằng máy chủ đang hoạt động.**

> **\# nmap -sn -PO \[địa chỉ IP mục tiêu\]**

10. Điều này kết thúc buổi trình diễn việc phát hiện máy chủ mục tiêu trong mạng mục tiêu bằng cách sử dụng các kỹ thuật phát hiện máy chủ khác nhau.

11. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 3.1.1.1**

Thực hiện quét ping ICMP ECHO để phát hiện các máy chủ đang hoạt động trên phân mạng của bạn. Tìm số lượng máy chủ đang hoạt động trong phân mạng (10.10.1.2-23).

![](media/image7.wmf)

Đúng

**Câu hỏi 3.1.1.2**

Thực hiện khám phá máy chủ bằng Nmap để tìm địa chỉ IP của máy chủ lưu trữ www.goodshopping.com.

![](media/image7.wmf)

Đúng

TrướcTiếp

Thí nghiệm 2: Thực hiện Khám phá Cổng và Dịch vụ

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc một người kiểm thử xâm nhập, bước tiếp theo sau khi phát hiện các máy chủ đang hoạt động trong mạng mục tiêu là quét các cổng mở và các dịch vụ đang chạy trên các địa chỉ IP mục tiêu trong mạng mục tiêu. Việc khám phá các cổng mở và dịch vụ này có thể được thực hiện thông qua nhiều công cụ và kỹ thuật quét cổng khác nhau.

**Mục tiêu bài lab**

-   Khám phá các kỹ thuật quét mạng khác nhau bằng Nmap

**Tổng quan về Khám phá Cổng và Dịch vụ**

Các kỹ thuật quét cổng được phân loại theo loại giao thức được sử dụng để giao tiếp trong mạng.

-   Quét TCP

    -   Phương pháp quét TCP mở (quét TCP kết nối/quét mở đầy đủ)

    -   Các phương pháp quét TCP ẩn (Quét nửa mở, Quét cờ TCP nghịch đảo, Quét dò cờ ACK, phương pháp quét TCP bên thứ ba và giả mạo)

-   Quét UDP

-   Quét SCTP

    -   Quét SCTP INIT

    -   Quét SCTP COOKIE/ECHO

-   SSDP và Quét Danh Sách

-   Quét IPv6

Nhiệm vụ 1: Khám phá các Kỹ thuật Quét Mạng khác nhau bằng cách sử dụng Nmap

Nmap đi kèm với nhiều script tích hợp sẵn có thể được sử dụng trong quá trình quét nhằm tìm các cổng mở và các dịch vụ đang chạy trên các cổng đó. Nó gửi các gói được chế tạo đặc biệt đến máy chủ mục tiêu, sau đó phân tích các phản hồi để đạt được mục tiêu của mình. Nmap bao gồm nhiều cơ chế quét cổng (TCP và UDP), phát hiện hệ điều hành, phát hiện phiên bản, quét ping, v.v.

Ở đây, chúng ta sẽ sử dụng Nmap để phát hiện các cổng mở và dịch vụ đang chạy trên các máy chủ hoạt động trong mạng mục tiêu.

1.  Nhấp vào Windows 11 để chuyển sang máy Windows 11 và đăng nhập với Admin\\Pa\$\$w0rd. Nhấp vào biểu tượng Tìm kiếm Windows ( ) trên Màn hình, tìm kiếm zenmap trong ô tìm kiếm và mở ứng dụng.[Windows 11](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)![search%20icon.jpg](media/image8.jpeg){width="0.37222222222222223in" height="0.3375in"}

2.  Zenmap xuất hiện; trong trường Lệnh, gõ nmap -sT -v \[Địa chỉ IP mục tiêu\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.22) và nhấn Quét.

> **-sT: thực hiện quét TCP connect/full open và -v: bật chế độ hiển thị chi tiết (bao gồm tất cả các host và cổng trong kết quả).**

3.  Kết quả quét xuất hiện, hiển thị tất cả các cổng TCP mở và các dịch vụ đang chạy trên máy mục tiêu, như được hiển thị trong ảnh chụp màn hình.

> Quét kết nối TCP hoàn thành một thao tác bắt tay ba bước với máy mục tiêu. Trong thao tác bắt tay ba bước TCP, máy khách gửi một gói SYN, mà người nhận xác nhận bằng gói SYN+ACK. Ngược lại, máy khách xác nhận gói SYN+ACK bằng một gói ACK để hoàn tất kết nối. Khi thao tác bắt tay hoàn tất, máy khách gửi một gói RST để kết thúc kết nối.
>
> thêm\...
>
> ![nmap1.jpg](media/image9.jpeg){width="10.6625in" height="8.0in"}

4.  Nhấp vào tab Ports/Hosts để thu thập thêm thông tin về kết quả quét. Nmap hiển thị Cổng, Giao thức, Trạng thái, Dịch vụ và Phiên bản của bản quét.

> ![Screenshot](media/image10.jpeg){width="10.6625in" height="8.0in"}

5.  Nhấp vào tab Topology để xem sơ đồ mạng của mạng mục tiêu chứa địa chỉ IP đã cung cấp và nhấp vào tùy chọn Fisheye để xem sơ đồ mạng rõ ràng.

> ![Screenshot](media/image11.jpeg){width="10.6625in" height="8.0in"}

6.  Tương tự, nhấp vào tab Chi tiết Máy chủ để xem chi tiết của quét kết nối TCP.

> ![Screenshot](media/image12.jpeg){width="10.6625in" height="8.0in"}

7.  Nhấp vào tab Quét để xem lệnh được sử dụng để thực hiện quét TCP connect/full open.

8.  Nhấp vào tab Dịch vụ nằm ở khung bên trái của cửa sổ. Tab này hiển thị danh sách các dịch vụ.

> ![Screenshot](media/image13.jpeg){width="10.6625in" height="8.0in"}
>
> Bạn có thể sử dụng bất kỳ dịch vụ nào trong số này và các cổng mở của chúng để xâm nhập vào mạng/ máy chủ mục tiêu và thiết lập kết nối.

9.  Trong nhiệm vụ phụ này, chúng ta sẽ thực hiện quét ẩn/quét TCP nửa mở, quét Xmas, quét TCP Maimon và quét thăm dò cờ ACK trên một máy có tường lửa (tức là Windows Server 2022) để quan sát kết quả. Để làm điều này, chúng ta cần bật Windows Firewall trên máy Windows Server 2022.

10. Nhấp vào Windows Server 2022 để chuyển sang máy Windows Server 2022. Nhấp Ctrl+Alt+Delete để kích hoạt máy. Đăng nhập với CEH\\Administrator/Pa\$\$w0rd[Windows Server 2022](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> Ngoài ra, bạn cũng có thể nhấp vào Pa\$\$w0rd dưới hình thu nhỏ của máy Windows Server 2022 trong pane Tài nguyên.

11. Đi đến Bảng điều khiển \--\> Hệ thống và Bảo mật \--\> Tường lửa Windows Defender \--\> Bật hoặc tắt Tường lửa Windows Defender, bật Tường lửa Windows và nhấp OK, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image14.jpeg){width="10.6625in" height="8.0in"}

12. Bây giờ, nhấp vào Windows 11 để chuyển sang máy Windows 11. Trong trường Lệnh của Zenmap, gõ nmap -sS -v \[Địa chỉ IP mục tiêu\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.22) và nhấp vào Quét.[Windows 11](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> **-sS: thực hiện quét ẩn danh/quét TCP nửa mở và -v: bật chế độ đầu ra chi tiết (bao gồm tất cả các máy chủ và cổng trong kết quả).**

13. Kết quả quét xuất hiện, hiển thị tất cả các cổng TCP mở và các dịch vụ đang chạy trên máy mục tiêu, như được trình bày trong ảnh chụp màn hình.

> Quét ẩn danh liên quan đến việc đặt lại kết nối TCP giữa máy khách và máy chủ một cách đột ngột trước khi hoàn tất các tín hiệu bắt tay ba bước, và do đó để kết nối ở trạng thái nửa mở. Kỹ thuật quét này có thể được sử dụng để bỏ qua các quy tắc tường lửa, cơ chế ghi nhật ký và ẩn mình trong lưu lượng mạng.
>
> thêm\...
>
> ![Screenshot](media/image15.jpeg){width="10.6625in" height="8.0in"}

14. Như đã trình bày trong nhiệm vụ trước, bạn có thể thu thập thông tin chi tiết từ kết quả quét trong các tab Ports/Hosts, Topology, Host Details, và Scan.

15. Tương tự, gõ nmap -sX -v \[Địa chỉ IP mục tiêu\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.22) và nhấp vào Quét.

> **-sX: thực hiện quét Giáng Sinh và -v: kích hoạt chế độ hiển thị chi tiết (bao gồm tất cả các máy chủ và cổng trong kết quả).**

16. Kết quả quét xuất hiện, hiển thị rằng các cổng hoặc đang mở hoặc bị lọc trên máy mục tiêu, điều này có nghĩa là một tường lửa đã được cấu hình trên máy mục tiêu.

> Quét Xmas gửi một khung TCP tới hệ thống mục tiêu với các cờ FIN, URG và PUSH được đặt. Nếu mục tiêu đã mở cổng, bạn sẽ không nhận được phản hồi từ hệ thống mục tiêu. Nếu mục tiêu đã đóng cổng, bạn sẽ nhận được phản hồi từ hệ thống mục tiêu với một RST.
>
> \...ít hơn
>
> ![2.jpg](media/image16.jpeg){width="10.6625in" height="8.0in"}

17. Trong trường Lệnh, gõ nmap -sM -v \[Địa chỉ IP mục tiêu\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.22) và nhấp vào Quét.

> **-sM: thực hiện quét TCP Maimon và -v: bật chế độ hiển thị chi tiết (bao gồm tất cả các máy chủ và cổng trong kết quả).**

18. Kết quả quét xuất hiện, hiển thị các cổng đang mở/được lọc trên máy mục tiêu, điều này có nghĩa là một tường lửa đã được cấu hình trên máy mục tiêu.

> Trong quét TCP Maimon, một gói dò FIN/ACK được gửi đến mục tiêu; nếu không có phản hồi, thì cổng là Mở\|Được Lọc, nhưng nếu gói RST được gửi như phản hồi, thì cổng bị đóng.
>
> ![3.jpg](media/image17.jpeg){width="10.6625in" height="8.0in"}

19. Trong trường Lệnh, gõ nmap -sA -v \[Địa chỉ IP mục tiêu\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.22) và nhấp vào Quét.

> **-sA: thực hiện quét cờ ACK và -v: bật chế độ hiển thị chi tiết (bao gồm tất cả các máy chủ và cổng trong kết quả).**

20. Kết quả quét xuất hiện, hiển thị rằng các cổng trên máy mục tiêu đã bị lọc, như được thể hiện trong ảnh chụp màn hình.

> Quét cờ ACK gửi một gói probe ACK với số thứ tự ngẫu nhiên; không có phản hồi ngụ ý rằng cổng bị lọc (tường lửa theo trạng thái hiện diện), và phản hồi RST có nghĩa là cổng không bị lọc.
>
> ![4.jpg](media/image18.jpeg){width="10.6625in" height="8.0in"}

21. Bây giờ, nhấp vào Windows Server 2022 để chuyển sang máy Windows Server 2022. Nhấp vào Ctrl+Alt+Delete để kích hoạt máy. Đăng nhập với CEH\\Administrator/Pa\$\$w0rd.[Windows Server 2022](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> Ngoài ra, bạn cũng có thể nhấp vào Pa\$\$w0rd dưới hình thu nhỏ của máy Windows Server 2022 trong pane Tài nguyên.

22. Tắt Tường lửa Windows Defender từ Bảng điều khiển.

23. Bây giờ, nhấp vào Windows 11 để quay trở lại máy Windows 11. Trong trường Lệnh của Zenmap, gõ nmap -sU -v \[Địa chỉ IP mục tiêu\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.22) và nhấp vào Quét.[Windows 11](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> **-sU: thực hiện quét UDP và -v: bật chế độ chi tiết (bao gồm tất cả các máy chủ và cổng trong kết quả). Quét này có thể mất khoảng 15-20 phút.**

24. Kết quả quét xuất hiện, hiển thị tất cả các cổng UDP đang mở và các dịch vụ đang chạy trên máy mục tiêu, như được hiển thị trong ảnh chụp màn hình.

> Quá trình quét này sẽ mất khoảng 20 phút để hoàn tất và kết quả có thể khác nhau trong môi trường bài lab của bạn.
>
> Quét UDP sử dụng giao thức UDP thay vì TCP. Không có bắt tay ba bước cho quét UDP. Nó gửi các gói UDP tới máy chủ mục tiêu; không có phản hồi có nghĩa là cổng đang mở. Nếu cổng bị đóng, sẽ nhận được một thông điệp ICMP cổng không thể truy cập.
>
> ![Screenshot](media/image19.jpeg){width="10.6625in" height="8.0in"}

25. Ngoài các kỹ thuật quét cổng và khám phá dịch vụ đã đề cập ở trên, bạn cũng có thể sử dụng các kỹ thuật quét sau để thực hiện việc quét cổng và khám phá dịch vụ trên một mạng mục tiêu bằng Nmap.

    -   **Quét tiêu đề IDLE/IPID: Một phương pháp quét cổng TCP có thể được sử dụng để gửi địa chỉ nguồn giả mạo đến một máy tính nhằm khám phá các dịch vụ có sẵn.**

> **\# nmap -sI -v \[địa chỉ IP mục tiêu\]**

-   **Quét SCTP INIT: Một khối INIT được gửi đến máy chủ mục tiêu; phản hồi khối INIT+ACK ngụ ý rằng cổng đang mở, và phản hồi khối ABORT có nghĩa là cổng đang đóng.**

> **\# nmap -sY -v \[địa chỉ IP mục tiêu\]**

-   **Quét SCTP COOKIE ECHO: Một khối COOKIE ECHO được gửi đến máy chủ mục tiêu; không có phản hồi tức là cổng đang mở và phản hồi khối ABORT có nghĩa là cổng đã đóng.**

> **\# nmap -sZ -v \[địa chỉ IP mục tiêu\]**

26. Trong trường Lệnh, gõ nmap -sV \[Địa chỉ IP Mục tiêu\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.22) và nhấn Quét.

> **-sV: phát hiện phiên bản dịch vụ.**

27. Kết quả quét xuất hiện, hiển thị các cổng mở và phiên bản của các dịch vụ đang chạy trên các cổng, như được hiển thị trong ảnh chụp màn hình.

> Phát hiện phiên bản dịch vụ giúp bạn thu thập thông tin về các dịch vụ đang chạy và phiên bản của chúng trên hệ thống mục tiêu. Việc xác định chính xác số phiên bản dịch vụ cho phép bạn xác định hệ thống mục tiêu dễ bị tấn công bởi những khai thác nào.
>
> ![Screenshot](media/image20.jpeg){width="10.6625in" height="8.0in"}

28. Trong trường Command, gõ nmap -A \[Target Subnet\] (trong ví dụ này, subnet mục tiêu là 10.10.1.\*) và nhấn Scan. Bằng cách sử dụng ký tự đại diện \"\*\", bạn có thể quét toàn bộ một subnet hoặc phạm vi IP.

> **-A: cho phép quét tích cực. Tùy chọn quét tích cực hỗ trợ phát hiện hệ điều hành (-O), quét phiên bản (-sV), quét script (-sC) và truy vết đường đi (\--traceroute). Bạn không nên sử dụng -A đối với các mạng mục tiêu mà không có sự cho phép.**

29. Nmap quét toàn bộ mạng và hiển thị thông tin cho tất cả các máy chủ đã được quét, cùng với các cổng và dịch vụ đang mở, loại thiết bị, chi tiết hệ điều hành, v.v., như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image21.jpeg){width="10.6625in" height="8.0in"}

30. Chọn địa chỉ IP 10.10.1.22 từ danh sách các máy chủ ở khung bên trái và nhấp vào tab Chi tiết Máy chủ. Tab này hiển thị thông tin như Trạng thái Máy chủ, Địa chỉ, Hệ điều hành, Cổng được sử dụng, Lớp HĐH, v.v. liên quan đến máy chủ đã chọn.

> ![Screenshot](media/image22.jpeg){width="10.6625in" height="8.0in"}

31. Điều này kết thúc phần trình bày về việc khám phá các cổng mở mục tiêu, dịch vụ, phiên bản dịch vụ, loại thiết bị, chi tiết hệ điều hành, v.v. của các máy chủ hoạt động trong mạng mục tiêu bằng cách sử dụng các kỹ thuật quét khác nhau của Nmap.

32. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 3.2.1.1**

Sử dụng Nmap để thực hiện quét TCP connect/full open và tìm số cổng được sử dụng bởi dịch vụ ldapssl trên máy Windows Server 2022.

![](media/image7.wmf)

Đúng

TrướcTiếp

Thí nghiệm 3: Thực hiện Khám phá Hệ điều hành

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc một chuyên gia kiểm thử xâm nhập, bước tiếp theo sau khi phát hiện các cổng mở và dịch vụ đang chạy trên phạm vi địa chỉ IP mục tiêu là thực hiện việc xác định hệ điều hành. Việc nhận diện hệ điều hành được sử dụng trên hệ thống mục tiêu cho phép bạn đánh giá các lỗ hổng của hệ thống và các khai thác có thể hoạt động trên hệ thống để thực hiện các cuộc tấn công bổ sung.

**Mục tiêu bài lab**

-   Thực hiện khám phá hệ điều hành sử dụng Engine Script Nmap (NSE)

**Tổng quan về Khám phá Hệ điều hành/ Thu thập Banner**

Banner grabbing, hay nhận dạng hệ điều hành (OS fingerprinting), là một phương pháp được sử dụng để xác định hệ điều hành đang chạy trên một hệ thống mục tiêu từ xa.

Có hai loại kỹ thuật khám phá hệ điều hành hoặc thu thập thông tin banner:

-   **Thu thập Banner Chủ động Các gói tin được chế tạo đặc biệt được gửi đến hệ điều hành từ xa, và các phản hồi được ghi chú, sau đó so sánh với cơ sở dữ liệu để xác định hệ điều hành. Phản hồi từ các hệ điều hành khác nhau sẽ khác nhau, do sự khác biệt trong việc triển khai ngăn xếp TCP/IP.**

-   **Thu thập thông tin thụ động về banner Điều này phụ thuộc vào việc triển khai khác nhau của stack và các cách khác nhau mà hệ điều hành phản hồi với các gói tin. Thu thập thông tin banner thụ động bao gồm việc thu thập banner từ các thông báo lỗi, theo dõi lưu lượng mạng, và thu thập banner từ các phần mở rộng của trang.**

Các tham số như TTL và kích thước cửa sổ TCP trong tiêu đề IP của gói dữ liệu đầu tiên trong một phiên TCP đóng vai trò quan trọng trong việc xác định hệ điều hành đang chạy trên máy mục tiêu. Trường TTL xác định thời gian tối đa mà một gói dữ liệu có thể tồn tại trong mạng, và kích thước cửa sổ TCP xác định độ dài của gói dữ liệu được báo cáo. Các giá trị này khác nhau đối với các hệ điều hành khác nhau: bạn có thể tham khảo bảng sau để biết các giá trị TTL và kích thước cửa sổ TCP liên quan đến các hệ điều hành khác nhau.

![2022-03-25_17-55-35.jpg](media/image23.jpeg){width="8.744444444444444in" height="3.604861111111111in"}

Nhiệm vụ 1: Thực hiện Khám phá Hệ điều hành bằng cách sử dụng Công cụ Script Nmap (NSE)

Nmap, cùng với Nmap Script Engine (NSE), có thể trích xuất một lượng lớn thông tin quý giá từ hệ thống mục tiêu. Bên cạnh các lệnh của Nmap, NSE cung cấp các tập lệnh tiết lộ mọi loại thông tin hữu ích từ hệ thống mục tiêu. Sử dụng NSE, bạn có thể thu thập thông tin như hệ điều hành, tên máy tính, tên miền, tên rừng, tên máy tính NetBIOS, tên miền NetBIOS, nhóm làm việc, thời gian hệ thống của hệ thống mục tiêu, v.v.

Ở đây, chúng tôi sẽ sử dụng Nmap để thực hiện khám phá hệ điều hành bằng cách sử dụng tham số -A, tham số -O và NSE.

1.  Nhấp vào Parrot Security để chuyển sang máy Parrot Security và đăng nhập với attacker/toor.[Parrot Security](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> Nếu một cửa sổ bật lên Parrot Updater xuất hiện ở góc trên bên phải của Màn hình, hãy bỏ qua và đóng nó.
>
> Nếu một cửa sổ bật lên Hỏi xuất hiện yêu cầu bạn cập nhật máy, hãy nhấp vào Không để đóng cửa sổ.

2.  Mở một cửa sổ Terminal và thực thi sudo su để chạy các chương trình với quyền người dùng root (Khi được yêu cầu, nhập mật khẩu toor).

> Mật khẩu mà bạn nhập sẽ không hiển thị.

3.  Trong cửa sổ terminal, chạy lệnh nmap -A \[Địa chỉ IP mục tiêu\] (ở đây, máy mục tiêu là Windows Server 2022 \[10.10.1.22\]). Kết quả quét sẽ xuất hiện, hiển thị các cổng mở và các dịch vụ đang chạy cùng với phiên bản của chúng và các thông tin chi tiết về mục tiêu như hệ điều hành, tên máy tính, tên máy NetBIOS, v.v. dưới phần Host script results.

> **-A: thực hiện một quét tấn công.**
>
> Quá trình quét mất khoảng 10 phút để hoàn thành.
>
> ![Screenshot](media/image24.jpeg){width="10.6625in" height="8.0in"} ![Screenshot](media/image25.jpeg){width="10.6625in" height="8.0in"}

4.  Trong cửa sổ terminal, chạy lệnh nmap -O \[Địa chỉ IP mục tiêu\] (trong ví dụ này, máy mục tiêu là Windows Server 2022 \[10.10.1.22\]). Kết quả quét sẽ xuất hiện, hiển thị thông tin về các cổng mở, các dịch vụ tương ứng đang chạy trên các cổng mở và tên hệ điều hành đang chạy trên hệ thống mục tiêu.

> **-O: thực hiện việc phát hiện hệ điều hành.**
>
> ![Screenshot](media/image26.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image27.jpeg){width="10.6625in" height="8.0in"}

5.  Trong cửa sổ terminal, chạy lệnh nmap \--script smb-os-discovery.nse \[Địa chỉ IP mục tiêu\] (ở đây, máy mục tiêu là Windows Server 2022 \[10.10.1.22\]). Kết quả quét sẽ xuất hiện, hiển thị hệ điều hành mục tiêu, tên máy tính, tên máy NetBIOS, v.v. trong phần Host script results.

> **\--script: chỉ định tập lệnh tùy chỉnh và smb-os-discovery.nse: cố gắng xác định hệ điều hành, tên máy tính, miền, nhóm làm việc và thời gian hiện tại qua giao thức SMB (cổng 445 hoặc 139).**
>
> ![Screenshot](media/image28.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image29.jpeg){width="10.6625in" height="8.0in"}

6.  Điều này kết thúc phần trình diễn về việc phát hiện hệ điều hành đang chạy trên hệ thống mục tiêu bằng Nmap.

7.  Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 3.3.1.1**

Sử dụng Nmap Scripting Engine (NSE) để thực hiện khám phá hệ điều hành và tìm hệ điều hành trên máy tại địa chỉ IP 10.10.1.22.

![](media/image7.wmf)

Đúng

TrướcTiếp

Thí nghiệm 4: Quét vượt qua IDS và Tường lửa

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc một chuyên gia kiểm thử xâm nhập, bước tiếp theo sau khi phát hiện hệ điều hành của địa chỉ IP mục tiêu là thực hiện quét mạng mà không bị các ranh giới bảo mật mạng như tường lửa và IDS phát hiện. IDS và tường lửa là những cơ chế bảo mật hiệu quả; tuy nhiên, chúng vẫn có một số hạn chế về bảo mật. Bạn có thể được yêu cầu tiến hành các cuộc tấn công để khai thác những hạn chế này bằng các kỹ thuật né tránh IDS/tường lửa khác nhau như phân mảnh gói tin, định tuyến nguồn, giả mạo địa chỉ IP, v.v. Quét vượt qua IDS và tường lửa cho phép bạn đánh giá bảo mật IDS và tường lửa của mạng mục tiêu.

**Mục tiêu bài lab**

-   Quét vượt qua IDS/tường lửa bằng cách sử dụng các kỹ thuật né tránh khác nhau

**Tổng quan về quét vượt ra ngoài IDS và Tường lửa**

Hệ thống Phát hiện Xâm nhập (IDS) và tường lửa là các cơ chế bảo mật nhằm ngăn chặn người trái phép truy cập vào mạng. Tuy nhiên, ngay cả IDS và tường lửa cũng có một số hạn chế về bảo mật. Tường lửa và IDS nhằm tránh lưu lượng độc hại (gói tin) xâm nhập vào mạng, nhưng một số kỹ thuật có thể được sử dụng để gửi các gói tin có mục đích đến mục tiêu và né tránh IDS/tường lửa.

Các kỹ thuật để tránh IDS/tường lửa:

-   **Phân mảnh gói tin: Gửi các gói dò bị phân mảnh đến mục tiêu dự định, mục tiêu sẽ lắp ráp lại sau khi nhận tất cả các mảnh**

-   **Định tuyến Nguồn: Chỉ định đường đi định tuyến cho gói dữ liệu bị sai để đến đích dự định**

-   **Thao túng Cổng Nguồn: Thao túng cổng nguồn thực với cổng nguồn phổ biến để né tránh IDS/tường lửa**

-   **Địa chỉ IP mồi nhử: Tạo hoặc chỉ định thủ công các địa chỉ IP của các mồi nhử để IDS/tường lửa không thể xác định địa chỉ IP thực sự**

-   **Giả mạo Địa chỉ IP: Thay đổi địa chỉ IP nguồn để cuộc tấn công có vẻ như đến từ người khác**

-   **Tạo gói tin tùy chỉnh: Gửi các gói tin tùy chỉnh để quét mục tiêu dự kiến vượt qua tường lửa**

-   **Ngẫu nhiên hóa thứ tự máy chủ: Quét số lượng máy chủ trong mạng mục tiêu theo thứ tự ngẫu nhiên để quét mục tiêu dự định nằm phía sau tường lửa**

-   **Gửi Checksum Sai: Gửi các gói tin với checksum TCP/UDP sai hoặc giả mạo đến mục tiêu dự định**

-   **Máy chủ Proxy: Sử dụng một chuỗi các máy chủ proxy để che giấu nguồn gốc thực sự của một cuộc quét và tránh một số hạn chế của IDS/tường lửa**

-   **Trình ẩn danh: Sử dụng các trình ẩn danh cho phép họ vượt qua các bộ lọc Internet và né tránh một số quy tắc IDS và tường lửa**

Nhiệm vụ 1: Quét vượt qua IDS/Firewall bằng cách sử dụng các Kỹ thuật Trốn tránh khác nhau

Nmap cung cấp nhiều tính năng để giúp hiểu các mạng phức tạp với các cơ chế bảo mật được bật và hỗ trợ các cơ chế để vượt qua các biện pháp phòng thủ triển khai kém. Sử dụng Nmap, có thể triển khai nhiều kỹ thuật khác nhau, có thể vượt qua các cơ chế bảo mật IDS/tường lửa.

Ở đây, chúng ta sẽ sử dụng Nmap để né tránh IDS/firewall bằng cách sử dụng các kỹ thuật khác nhau như phân mảnh gói tin, thao tác cổng nguồn, MTU và mồi địa chỉ IP.

1.  Nhấp vào Windows 11 để chuyển sang máy Windows 11.[Windows 11](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

2.  Điều hướng tới Bảng điều khiển \--\> Hệ thống và Bảo mật \--\> Tường lửa Windows Defender \--\> Bật hoặc tắt Tường lửa Windows Defender, bật Tường lửa Windows Defender và nhấp OK, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image30.jpeg){width="10.6625in" height="8.0in"}

3.  Thu nhỏ cửa sổ Bảng Điều Khiển, nhấp vào biểu tượng Tìm kiếm Windows ( ) trên Màn hình. Tìm kiếm wireshark trong ô tìm kiếm và nhấp vào Mở để khởi chạy nó.![search3icon.jpg](media/image8.jpeg){width="0.37222222222222223in" height="0.3375in"}

4.  Cửa sổ Wireshark Network Analyzer xuất hiện, bắt đầu bắt các gói bằng cách nhấp đúp vào ethernet hoặc giao diện có sẵn (ở đây là Ethernet).

> Nếu cửa sổ Cập nhật Phần mềm xuất hiện, hãy nhấp vào Nhắc tôi sau.

5.  Nhấp vào Parrot Security để chuyển sang máy Parrot Security. Mở một cửa sổ Terminal và thực thi sudo su để chạy các chương trình với quyền người dùng root (Khi được nhắc, nhập mật khẩu toor).[Parrot Security](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> Mật khẩu mà bạn nhập sẽ không hiển thị.

6.  Bây giờ, chạy lệnh cd để chuyển đến thư mục gốc.

7.  Trong cửa sổ terminal, chạy lệnh nmap -f \[Địa chỉ IP mục tiêu\], (ở đây, máy mục tiêu là Windows 11 \[10.10.1.11\]).

> **Công tắc -f được sử dụng để chia gói IP thành các gói mảnh nhỏ.**
>
> Phân mảnh gói tin đề cập đến việc chia một gói thăm dò thành nhiều gói nhỏ hơn (mảnh) khi gửi nó đến một mạng. Khi những gói này đến một máy chủ, các IDS và tường lửa phía sau máy chủ thường xếp tất cả chúng vào hàng đợi và xử lý từng gói một. Tuy nhiên, vì phương pháp xử lý này tiêu tốn nhiều CPU cũng như tài nguyên mạng hơn, cấu hình của hầu hết IDS khiến nó bỏ qua các gói bị phân mảnh trong quá trình quét cổng.
>
> thêm\...

8.  Mặc dù Tường lửa Windows Defender đã được bật trên hệ thống mục tiêu (ở đây là Windows 11), bạn vẫn có thể nhận được kết quả hiển thị tất cả các cổng TCP mở cùng với tên của các dịch vụ đang chạy trên các cổng, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image31.jpeg){width="10.6625in" height="8.0in"}

9.  Nhấn vào Windows 11 để chuyển sang máy Windows 11 (máy mục tiêu). Bạn có thể quan sát các gói tin bị phân mảnh được Wireshark ghi lại, như hiển thị trong ảnh chụp màn hình.[Windows 11](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> ![Screenshot](media/image32.jpeg){width="10.6625in" height="8.0in"}

10. Nhấp vào Parrot Security để chuyển sang máy Parrot Security.[Parrot Security](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

11. Trong cửa sổ Parrot Terminal, chạy lệnh nmap -g 80 \[Địa chỉ IP mục tiêu\], (ở đây, địa chỉ IP mục tiêu là 10.10.1.11).

> Trong lệnh này, bạn có thể sử dụng tùy chọn -g hoặc \--source-port để thực hiện thao tác thay đổi cổng nguồn.
>
> Thao túng cổng nguồn đề cập đến việc thao túng các số cổng thực với các số cổng phổ biến để tránh IDS/tường lửa: điều này hữu ích khi tường lửa được cấu hình để cho phép các gói tin từ các cổng nổi tiếng như HTTP, DNS, FTP, v.v.

12. Kết quả hiển thị, hiển thị tất cả các cổng TCP đang mở cùng với tên các dịch vụ đang chạy trên các cổng đó, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image33.jpeg){width="10.6625in" height="8.0in"}

13. Nhấp vào Windows 11 để chuyển sang máy Windows 11 (máy mục tiêu). Trong cửa sổ Wireshark, cuộn xuống và bạn có thể quan sát các gói TCP cho thấy rằng cổng số 80 được sử dụng để quét các cổng khác của máy mục tiêu, như được hiển thị trong ảnh chụp màn hình.[Windows 11](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> ![Screenshot](media/image34.jpeg){width="10.6625in" height="8.0in"}

14. Nhấp vào Parrot Security để chuyển sang máy Parrot Security.[Parrot Security](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

15. Bây giờ, chạy lệnh nmap -mtu 8 \[Địa chỉ IP mục tiêu\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.11).

> Trong lệnh này, -mtu: chỉ định số đơn vị truyền tối đa (MTU) (ở đây, 8 byte của gói tin).
>
> Sử dụng MTU, các gói nhỏ hơn được truyền đi thay vì gửi một gói hoàn chỉnh mỗi lần. Kỹ thuật này né tránh cơ chế lọc và phát hiện được kích hoạt trên máy mục tiêu.
>
> ![Screenshot](media/image35.jpeg){width="10.6625in" height="8.0in"}

16. Nhấp vào Windows 11 để chuyển sang máy Windows 11 (máy mục tiêu). Trong cửa sổ Wireshark, cuộn xuống và bạn có thể quan sát các gói bị phân mảnh có độ dài tối đa là 8 byte, như được hiển thị trong ảnh chụp màn hình.[Windows 11](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> ![16new.jpg](media/image36.jpeg){width="10.6625in" height="8.0in"}

17. Nhấp vào Parrot Security để chuyển sang máy Parrot Security.[Parrot Security](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

18. Bây giờ, chạy lệnh nmap -D RND:10 \[Địa chỉ IP mục tiêu\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.11).

> Trong lệnh này, -D: thực hiện quét mồi nhử và RND: tạo các địa chỉ IP ngẫu nhiên và không bị hạn chế (ở đây, 10).
>
> Kỹ thuật giả mạo địa chỉ IP đề cập đến việc tạo ra hoặc chỉ định thủ công các địa chỉ IP của các mồi nhử để né tránh IDS/tường lửa. Kỹ thuật này làm cho IDS/tường lửa khó xác định địa chỉ IP nào thực sự quét mạng và địa chỉ IP nào là mồi nhử. Bằng cách sử dụng lệnh này, Nmap tự động tạo ra một số lượng mồi nhử ngẫu nhiên cho việc quét và đặt địa chỉ IP thực giữa các địa chỉ IP mồi nhử một cách ngẫu nhiên.
>
> thêm\...
>
> ![Screenshot](media/image37.jpeg){width="10.6625in" height="8.0in"}

19. Bây giờ, nhấp vào Windows 11 để chuyển sang máy Windows 11 (máy đích). Trong cửa sổ Wireshark, cuộn xuống và bạn có thể quan sát các gói hiển thị nhiều địa chỉ IP trong phần nguồn, như được hiển thị trong ảnh chụp màn hình.[Windows 11](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> ![Screenshot](media/image38.jpeg){width="10.6625in" height="8.0in"}

20. Nhấp vào Parrot Security để chuyển sang máy Parrot Security.[Parrot Security](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

21. Trong cửa sổ terminal, chạy lệnh nmap -sT -Pn \--spoof-mac 0 \[Địa chỉ IP mục tiêu\] (trong đây, địa chỉ IP mục tiêu là 10.10.1.11).

> Trong lệnh này \--spoof-mac 0 đại diện cho việc ngẫu nhiên hóa địa chỉ MAC, -sT: thực hiện quét TCP connect/full open, -Pn được sử dụng để bỏ qua bước khám phá máy chủ.
>
> Kỹ thuật giả mạo địa chỉ MAC liên quan đến việc giả mạo một địa chỉ MAC với địa chỉ MAC của người dùng hợp pháp trên mạng. Kỹ thuật này cho phép bạn gửi các gói yêu cầu đến máy/mạng mục tiêu giả vờ là một máy chủ hợp pháp.
>
> ![Screenshot](media/image39.jpeg){width="10.6625in" height="8.0in"}

22. Nhấp vào Windows 11 để chuyển sang máy Windows 11 (máy đích). Trong cửa sổ Wireshark, cuộn xuống và bạn có thể quan sát các gói TCP đã được bắt, như hiển thị trong ảnh chụp màn hình.[Windows 11](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> ![Screenshot](media/image40.jpeg){width="10.6625in" height="8.0in"}

23. Điều này kết thúc phần trình diễn việc tránh IDS và tường lửa bằng cách sử dụng các kỹ thuật thoát ẩn khác nhau trong Nmap.

24. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 3.4.1.1**

Sử dụng công cụ Nmap để quét vượt qua IDS/firewall của máy mục tiêu (Windows 11). Nhập tùy chọn Nmap được sử dụng để tách gói IP thành các gói mảnh nhỏ. Lưu ý: Bật Windows Firewall để thực hiện nhiệm vụ này.

![](media/image7.wmf)

Đúng

Thí nghiệm 5: Thực hiện quét mạng bằng các công cụ quét khác nhau

**kịch bản bài lab bài lab**

Thông tin thu được ở các bước trước có thể không đủ để tiết lộ các lỗ hổng tiềm ẩn trong mạng mục tiêu: có thể có nhiều thông tin hơn có sẵn mà có thể giúp tìm ra những kẽ hở trong mạng mục tiêu. Là một hacker đạo đức và kiểm thử xâm nhập, bạn nên tìm kiếm càng nhiều thông tin càng tốt về các hệ thống trong mạng mục tiêu bằng cách sử dụng các công cụ quét mạng khác nhau khi cần thiết. Thí nghiệm này sẽ trình bày các kỹ thuật/lệnh/phương pháp khác có thể hỗ trợ bạn trong việc khai thác thông tin về các hệ thống trong mạng mục tiêu bằng cách sử dụng các công cụ quét khác nhau.

**Mục tiêu bài lab**

-   Quét một mạng mục tiêu bằng Metasploit

**Tổng quan về các công cụ quét mạng**

Các công cụ quét được sử dụng để quét và xác định các máy chủ đang hoạt động, các cổng mở, các dịch vụ đang chạy trên mạng mục tiêu, thông tin vị trí, thông tin NetBIOS và thông tin về tất cả các cổng TCP/IP và UDP đang mở. Thông tin thu được từ các công cụ này sẽ hỗ trợ một hacker đạo đức trong việc tạo hồ sơ của tổ chức mục tiêu và quét mạng để tìm các cổng mở của các thiết bị được kết nối.

Nhiệm vụ 1: Quét một Mạng Mục tiêu bằng Metasploit

Metasploit Framework là một công cụ cung cấp thông tin về các lỗ hổng bảo mật trong hệ thống của tổ chức mục tiêu, và hỗ trợ trong việc kiểm thử xâm nhập và phát triển chữ ký IDS. Nó tạo điều kiện cho các nhiệm vụ của kẻ tấn công, người viết khai thác và người viết payload. Một lợi thế chính của framework là phương pháp mô-đun, tức là cho phép kết hợp bất kỳ khai thác nào với bất kỳ payload nào.

Ở đây, chúng tôi sẽ sử dụng Metasploit để khám phá các máy chủ đang hoạt động, các cổng mở, các dịch vụ đang chạy và chi tiết hệ điều hành của các hệ thống có trong mạng mục tiêu.

1.  Nhấp vào Parrot Security để chuyển sang máy Parrot Security. Mở một cửa sổ Terminal và thực thi sudo su để chạy các chương trình với quyền người dùng root (Khi được nhắc, nhập mật khẩu toor).[Parrot Security](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)

> Mật khẩu mà bạn nhập sẽ không hiển thị.

2.  Thực hiện lệnh msfconsole để khởi động Metasploit.

> ![Screenshot](media/image41.jpeg){width="10.6625in" height="8.0in"}

3.  Một dòng lệnh msf xuất hiện. Gõ nmap -Pn -sS -A -oX Test 10.10.1.0/24 và nhấn Enter để quét mạng con, như được hiển thị trong ảnh chụp màn hình.

> Ở đây, chúng tôi đang quét toàn bộ mạng con 10.10.1.0/24 để tìm các máy chủ đang hoạt động.

4.  Nmap bắt đầu quét mạng con và hiển thị kết quả. Quá trình quét mất khoảng 5 phút để hoàn thành.

5.  Sau khi quét hoàn tất, Nmap hiển thị thông tin máy chủ trong mạng mục tiêu cùng với các cổng mở, dịch vụ và liệt kê hệ điều hành.

> ![Screenshot](media/image42.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image43.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image44.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image45.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image46.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image47.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image48.jpeg){width="10.6625in" height="8.0in"}

6.  Gõ tìm kiếm portscan và nhấn Enter. Các mô-đun quét cổng của Metasploit xuất hiện, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image49.jpeg){width="10.6625in" height="8.0in"}

7.  Ở đây, chúng ta sẽ sử dụng mô-đun auxiliary/scanner/portscan/syn để thực hiện quét SYN trên các hệ thống mục tiêu. Để làm điều đó, gõ use auxiliary/scanner/portscan/syn và nhấn Enter.

8.  Chúng tôi sẽ sử dụng mô-đun này để thực hiện quét SYN đối với phạm vi địa chỉ IP mục tiêu (10.10.1.5-23) để tìm cổng 80 mở thông qua giao diện eth0.

> Để làm điều đó, hãy thực hiện các lệnh dưới đây:

-   **đặt GIAO DIỆN eth0**

-   **đặt CẢNG 80**

-   **đặt RHOSTS 10.10.1.5-23**

-   **đặt THREADS 50**

> **PORTS: chỉ định các cổng để quét (ví dụ: 22-25, 80, 110-900), RHOSTS: chỉ định phạm vi địa chỉ mục tiêu hoặc định danh CIDR, và THREADS: chỉ định số lượng luồng đồng thời (mặc định 1).**

9.  Sau khi xác định các giá trị trên, gõ run và nhấn Enter, để bắt đầu quét phạm vi địa chỉ IP mục tiêu.

> Tương tự, bạn cũng có thể chỉ định một phạm vi cổng để quét đối với phạm vi địa chỉ IP mục tiêu.
>
> ![Screenshot](media/image50.jpeg){width="10.6625in" height="8.0in"}

10. Kết quả xuất hiện, hiển thị cổng mở 80 trên các máy chủ đang hoạt động, như được hiển thị trong ảnh chụp màn hình.

> ![10.jpg](media/image51.jpeg){width="10.6625in" height="8.0in"}

11. Bây giờ, chúng ta sẽ thực hiện quét TCP để tìm các cổng mở trên các hệ thống mục tiêu.

12. Để tải module auxiliary/scanner/portscan/tcp, gõ use auxiliary/scanner/portscan/tcp và nhấn Enter. Chạy lệnh show options để xem các tùy chọn của module.

> ![Screenshot](media/image52.jpeg){width="10.6625in" height="8.0in"}

13. Gõ lệnh set RHOSTS \[Địa chỉ IP mục tiêu\] và nhấn Enter.

> Ở đây, chúng tôi sẽ thực hiện quét TCP để tìm các cổng mở trên một địa chỉ IP duy nhất (10.10.1.22), vì quét nhiều địa chỉ IP tốn nhiều thời gian.

14. Gõ run và nhấn Enter để phát hiện các cổng TCP mở trên hệ thống mục tiêu.

> Quá trình quét sẽ mất khoảng 20 phút để hoàn tất.

15. Kết quả xuất hiện, hiển thị tất cả các cổng TCP đang mở trên địa chỉ IP mục tiêu (10.10.1.22).

> ![15q.jpg](media/image53.jpeg){width="10.6625in" height="8.0in"}

16. Bây giờ khi chúng ta đã xác định được các máy chủ đang hoạt động trên mạng mục tiêu, chúng ta có thể tiếp tục cố gắng xác định các hệ điều hành đang chạy trên các hệ thống mục tiêu. Vì có các hệ thống trong quét của chúng ta có cổng 445 mở, chúng ta sẽ sử dụng module scanner/smb/version để xác định phiên bản Windows đang chạy trên mục tiêu và phiên bản Samba trên máy chủ Linux.

17. Để làm điều đó, trước tiên gõ back, để quay lại dòng lệnh msf. Sau đó, gõ use auxiliary/scanner/smb/smb_version và nhấn enter.

18. Chúng tôi sẽ sử dụng mô-đun này để chạy quét phiên bản SMB trên phạm vi địa chỉ IP mục tiêu (10.10.1.5-23). Để thực hiện điều đó, hãy nhập các lệnh dưới đây:

    -   **đặt RHOSTS 10.10.1.5-23**

    -   **đặt THREADS 11**

19. Gõ run để khám phá phiên bản SMB trên các hệ thống mục tiêu.

20. Kết quả xuất hiện, hiển thị chi tiết hệ điều hành của các máy chủ mục tiêu.

> ![Screenshot](media/image54.jpeg){width="10.6625in" height="8.0in"}

21. Bạn có thể tiếp tục khám phá các mô-đun khác nhau của Metasploit như mô-đun FTP để xác định phiên bản FTP đang chạy trên máy chủ mục tiêu.

22. Thông tin này có thể được sử dụng thêm để thực hiện phân tích lỗ hổng trên các dịch vụ mở được phát hiện trên các máy chủ mục tiêu.

23. Điều này kết thúc phần trình diễn về việc thu thập thông tin về các cổng mở, danh sách các dịch vụ đang chạy trên các máy chủ hoạt động, và các thông tin liên quan đến hệ điều hành, cùng những thông tin khác.

24. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 3.5.1.1**

Sử dụng Metasploit để quét máy mục tiêu. Trong khi sử dụng mô-đun phụ trợ Metasploit "auxiliary/scanner/smb/smb_version", nhập phạm vi máy chủ từ xa (RHOSTS) được chỉ định.

![](media/image7.wmf)

Đúng

Bài Thí Nghiệm 6: Thực Hiện Quét Mạng Sử Dụng AI

**kịch bản bài lab bài lab**

Là những hacker đạo đức và chuyên viên kiểm tra xâm nhập, việc tận dụng các công cụ và kỹ thuật tiên tiến để phát hiện các lỗ hổng ẩn trong mạng mục tiêu là cực kỳ quan trọng. bài lab này tập trung vào việc sử dụng các công cụ quét mạng được hỗ trợ bởi AI như ShellGPT để thu thập thông tin toàn diện về các hệ thống trong mạng mục tiêu.

**Mục tiêu bài lab**

-   Quét mục tiêu bằng ShellGPT

**Tổng quan về Quét Mạng sử dụng AI**

Quét mạng sử dụng AI nâng cao an ninh mạng bằng cách tự động phát hiện các lỗ hổng và mối đe dọa. Các công cụ do AI điều khiển phân tích lưu lượng mạng, xác định các bất thường và dự đoán các cuộc tấn công tiềm ẩn với độ chính xác cao, cung cấp các cơ chế phòng thủ chủ động và giảm thời gian phản hồi cho các nhóm an ninh mạng.

Nhiệm vụ 1: Quét mục tiêu bằng ShellGPT

ShellGPT là một công cụ được hỗ trợ bởi AI có thể hỗ trợ quét mạng bằng cách tự động hóa các nhiệm vụ như xác định thiết bị đang hoạt động, phát hiện các cổng mở và phân tích lỗ hổng mạng. Nó sử dụng các thuật toán tiên tiến để cung cấp các thông tin chuyên sâu hiệu quả, theo thời gian thực, đảm bảo bảo mật mạng và tối ưu hóa hiệu suất.

Ở đây, chúng tôi sẽ sử dụng ShellGPT để khám phá các máy chủ đang hoạt động, các cổng mở, các dịch vụ đang chạy và chi tiết hệ điều hành của các hệ thống có trong mạng mục tiêu.

Các lệnh được tạo ra bởi ShellGPT có thể thay đổi tùy thuộc vào prompt được sử dụng và các công cụ có sẵn trên máy. Do những biến số này, kết quả đầu ra được tạo ra bởi ShellGPT có thể khác với những gì được hiển thị trong các ảnh chụp màn hình. Sự khác biệt này xuất phát từ tính chất động của quá trình xử lý của AI và các môi trường đa dạng mà nó hoạt động. Do đó, bạn có thể quan sát thấy sự khác biệt về cú pháp lệnh, cách thực thi và kết quả khi thực hiện nhiệm vụ bài lab này.

1.  Trước khi bắt đầu bài lab này, nhấp vào Parrot Security để chuyển sang Parrot Security và đăng nhập bằng tài khoản toor. Mở cửa sổ Terminal và thực hiện sudo su để chạy các chương trình với quyền root (Khi được yêu cầu, nhập mật khẩu toor), máy và tích hợp ShellGPT bằng cách làm theo các bước được cung cấp trong Integrate ShellGPT in Parrot Security Machine.pdf.[Parrot Security](https://labclient.labondemand.com/Instructions/5da1ddfd-f62c-4a51-86c9-7e01db5164d7)[Integrate ShellGPT in Parrot Security Machine.pdf](https://labondemand.blob.core.windows.net/content/lab168796/instructions267915/Integrate%20ShellGPT%20in%20Parrot%20%20Security%20Machine.pdf)

> Ngoài ra, bạn có thể làm theo các bước để tích hợp ShellGPT được cung cấp trong Mô-đun 00: Tích hợp ShellGPT trên Máy Parrot Security.

2.  Sau khi tích hợp API ShellGPT vào Parrot Security Machine, trong cửa sổ terminal chạy sgpt \--chat scan \--shell \"Sử dụng hping3 để thực hiện quét ICMP trên địa chỉ IP mục tiêu 10.10.1.11 và dừng sau 10 lần lặp\" để thực hiện quét ICMP trên địa chỉ IP mục tiêu.

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![scan1.jpg](media/image55.jpeg){width="10.6625in" height="8.0in"}

3.  Bây giờ, chạy lệnh sgpt \--chat scan \--shell \"Chạy quét hping3 ACK trên cổng 80 của địa chỉ IP mục tiêu 10.10.1.11\" để thực hiện quét ACK trên địa chỉ IP mục tiêu.

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image56.jpeg){width="10.6625in" height="8.0in"}

4.  Nhấn Ctrl + C để dừng quét.

5.  Chạy sgpt \--chat scan \--shell \"Quét mạng mục tiêu 10.10.1.0/24 để tìm các máy chủ đang hoạt động và chỉ đặt các địa chỉ IP vào tệp scan1.txt\" để thực hiện khám phá máy chủ.

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.

6.  Bây giờ chạy lệnh pluma scan1.txt để mở tệp scan1.txt và xem địa chỉ IP của các máy chủ đang hoạt động trong mạng con mục tiêu.

> ![Screenshot](media/image57.jpeg){width="10.6625in" height="8.0in"}

7.  Đóng cửa sổ trình soạn thảo văn bản.

8.  Để thực hiện quét nmap đối với các địa chỉ IP đã được thu thập ở bước trước, hãy chạy lệnh sgpt \--chat scan \--shell \"Chạy một quét nmap nhanh nhưng toàn diện đối với scan1.txt với mức độ chi tiết thấp và ghi kết quả vào scan2.txt\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image58.jpeg){width="10.6625in" height="8.0in"}

9.  Sau khi quét xong, chạy lệnh pluma scan2.txt để mở tệp scan2.txt và xem kết quả quét.

> ![Screenshot](media/image59.jpeg){width="10.6625in" height="8.0in"}

10. Đóng cửa sổ trình soạn thảo văn bản.

11. Chạy lệnh sgpt \--chat scan \--shell \"Sử dụng nmap để thực hiện quét ping ICMP ECHO trên mạng mục tiêu 10.10.1.0/24\" để thực hiện quét ping ICMP ECHO trên mạng mục tiêu.

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image60.jpeg){width="9.934003718285215in" height="7.453414260717411in"}

12. Bây giờ, chúng ta sẽ thực hiện quét cổng bằng cách sử dụng ShellGPT, để làm điều đó, chạy lệnh sgpt \--chat scan \--shell \"Sử dụng nmap để tìm các cổng mở trên địa chỉ IP mục tiêu 10.10.1.11\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.

13. Kết quả quét sẽ xuất hiện hiển thị tất cả các cổng mở, liên quan đến địa chỉ IP mục tiêu.

> ![Screenshot](media/image61.jpeg){width="7.168167104111986in" height="5.378226159230096in"}

14. Bây giờ, chúng ta sẽ thực hiện quét ẩn trên một địa chỉ IP mục tiêu, để làm điều đó, chạy lệnh sgpt \--chat scan \--shell \"Thực hiện quét ẩn trên địa chỉ IP mục tiêu 10.10.1.11 và hiển thị kết quả\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image62.jpeg){width="8.013304899387576in" height="6.012328302712161in"}

15. Để thực hiện quét XMAS trên địa chỉ IP mục tiêu, chạy lệnh sgpt \--chat scan \--shell \"Thực hiện quét XMAS trên IP mục tiêu 10.10.1.11\".

> ![Screenshot](media/image63.jpeg){width="7.199575678040245in" height="5.401791338582677in"}

16. Chạy lệnh sgpt \--chat scan \--shell \"Sử dụng Nmap để quét các cổng mở và dịch vụ trên danh sách địa chỉ IP trong scan1.txt và chỉ sao chép thông tin về cổng, dịch vụ và phiên bản cùng với địa chỉ IP tương ứng vào một tệp mới gọi là scan3.txt\" để quét các dịch vụ và cổng mở trên danh sách địa chỉ IP đã thu thập ở Bước #6.

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.

17. Khi quét xong, chạy lệnh pluma scan3.txt để xem kết quả quét.

> ![Screenshot](media/image64.jpeg){width="5.992623578302712in" height="4.49622375328084in"}

18. Đóng cửa sổ trình soạn thảo văn bản.

19. Bây giờ chúng ta sẽ sử dụng Metasploit để phát hiện các cổng mở trên hệ thống mục tiêu, chạy lệnh sgpt \--chat scan \--shell \"Sử dụng Metasploit để phát hiện các cổng mở trên địa chỉ IP 10.10.1.22\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image65.jpeg){width="6.004943132108487in" height="4.505469160104987in"}
>
> ![Screenshot](media/image66.jpeg){width="8.92650699912511in" height="6.697496719160105in"}

20. Để thực hiện việc khám phá phiên bản dịch vụ trên một hệ thống mục tiêu, chạy lệnh sgpt \--chat scan \--shell \"Sử dụng Nmap để quét các cổng mở, thông tin MAC, các dịch vụ đang chạy trên các cổng mở cùng phiên bản của chúng trên địa chỉ IP mục tiêu 10.10.1.11\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image67.jpeg){width="8.260009842519684in" height="6.19742782152231in"}

21. Chúng ta sẽ thực hiện khám phá hệ điều hành bằng ShellGPT, để làm điều này hãy chạy lệnh sgpt \--chat scan \--shell \"Sử dụng giá trị TTL và xác định hệ điều hành đang chạy trên địa chỉ IP mục tiêu 10.10.1.11, hiển thị giá trị TTL và hệ điều hành\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image68.jpeg){width="6.389783464566929in" height="4.794211504811899in"}

22. Chạy sgpt \--chat scan \--shell \"Sử dụng giá trị TTL và xác định hệ điều hành đang chạy trên địa chỉ IP mục tiêu 10.10.1.9, hiển thị giá trị TTL và hệ điều hành\"

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image69.jpeg){width="6.60241469816273in" height="4.953746719160105in"}

23. Chúng tôi sẽ tiến hành khám phá hệ điều hành (OS) bằng Nmap trên danh sách địa chỉ IP đã có được ở Bước#6, để thực hiện việc này hãy chạy sgpt \--chat scan \--shell \"Sử dụng engine script của Nmap để thực hiện khám phá hệ điều hành trên các địa chỉ IP mục tiêu trong scan1.txt\"

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image70.jpeg){width="7.2372036307961505in" height="5.430024059492563in"}
>
> ![Screenshot](media/image71.jpeg){width="8.41558508311461in" height="6.314155730533684in"}
>
> ![Screenshot](media/image72.jpeg){width="6.787456255468067in" height="5.092582020997376in"}

24. Chúng tôi sẽ tự động hóa các nhiệm vụ quét mạng khác nhau bằng cách tạo script tùy chỉnh chạy tự động và lấy kết quả mong muốn.

25. Trong cửa sổ terminal, chạy lệnh sgpt \--chat scan \--shell \"Phát triển một script sẽ tự động hóa các nỗ lực quét mạng và tìm ra các hệ thống đang hoạt động, cổng mở, dịch vụ đang chạy, phiên bản dịch vụ, v.v. trên dải IP mục tiêu 10.10.1.0/24\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image73.jpeg){width="6.902778871391076in" height="5.179106517935258in"}

26. Để sử dụng kỹ thuật Mồi Nhử Địa Chỉ IP để quét, chạy lệnh sgpt \--chat scan \--shell \"Để tránh IDS/Tường lửa, sử dụng kỹ thuật mồi nhử địa chỉ IP để quét địa chỉ IP mục tiêu 10.10.1.22\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image74.jpeg){width="6.911515748031496in" height="5.185662729658793in"}

27. Bây giờ, chạy lệnh sgpt \--chat scan \--shell \"Trong file scan1.txt xóa các mục 10.10.1.14 và 10.10.1.13, sau đó hiển thị kết quả\" để xóa địa chỉ IP khỏi file scan1.txt và hiển thị kết quả.

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image75.jpeg){width="6.947131452318461in" height="5.212384076990376in"}

28. Chạy lệnh sgpt \--chat scancode \--code \"Tạo một script Python để thực hiện quét Nmap nhanh nhưng toàn diện trên các địa chỉ IP trong scan1.txt và sau đó thực hiện quét lỗ hổng bằng nikto đối với từng địa chỉ IP trong scan1.txt\" để tạo một script Python thực hiện quét Nmap.

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image76.jpeg){width="5.551027996500437in" height="4.164898293963255in"}

29. Bây giờ, sao chép mã Python và gõ pluma python_scan.py trong terminal. Một cửa sổ trình soạn thảo văn bản sẽ mở, dán mã vào cửa sổ trình soạn thảo văn bản, lưu tệp và đóng nó lại.

> ![Screenshot](media/image77.jpeg){width="6.28738845144357in" height="4.717384076990376in"}

30. Bây giờ, trong cửa sổ terminal, gõ python3 python_scan.py để chạy script.

> ![Screenshot](media/image78.jpeg){width="9.566903980752405in" height="7.177982283464567in"}
>
> ![Screenshot](media/image79.jpeg){width="8.252772309711286in" height="6.191998031496063in"}

31. Ngoài các lệnh đã đề cập ở trên, bạn có thể khám phá thêm các tùy chọn khác trong công cụ ShellGPT và sử dụng nhiều công cụ khác để thực hiện Quét Mạng trên máy mục tiêu.

32. Điều này kết thúc phần trình diễn sử dụng ShellGPT để khám phá các máy chủ đang hoạt động, cổng mở, các dịch vụ đang chạy và chi tiết hệ điều hành của các hệ thống có trong mạng mục tiêu.

33. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 3.6.1.1**

Viết một lệnh nhắc ShellGPT và thực thi nó trên máy Parrot Security, để thực hiện quét cổng trên máy ảo Windows 11 (10.10.1.11). Nhập tên dịch vụ đang chạy trên cổng 139.

![](media/image7.wmf)

Đúng

TrướcTiếp

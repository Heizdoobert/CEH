Mô-đun 04: Liệt kê

Kịch bản

Với sự phát triển của các công nghệ và ứng dụng mạng, các cuộc tấn công mạng đang tăng mạnh cả về số lượng lẫn mức độ nghiêm trọng. Những kẻ tấn công liên tục tìm kiếm các lỗ hổng trong dịch vụ và ứng dụng trên mạng và máy chủ. Khi họ tìm thấy một sai sót hoặc lỗ hổng trong một dịch vụ chạy qua Internet, họ ngay lập tức khai thác nó để xâm phạm toàn bộ hệ thống. Bất kỳ dữ liệu nào khác mà họ tìm thấy có thể được sử dụng thêm để xâm phạm các hệ thống mạng khác. Tương tự, những kẻ tấn công tìm kiếm và sử dụng các máy trạm có quyền quản trị, và chạy các ứng dụng có lỗi, để thực thi mã tùy ý hoặc cấy virus nhằm làm tăng mức độ thiệt hại cho mạng.

Trong bước đầu tiên của đánh giá bảo mật và thử nghiệm xâm nhập của tổ chức bạn, bạn thu thập thông tin từ nguồn mở về tổ chức của mình. Trong bước thứ hai, bạn thu thập thông tin về các cổng và dịch vụ mở, hệ điều hành, và bất kỳ sai sót cấu hình nào.

Bước tiếp theo đối với một hacker có đạo đức hoặc kiểm thử viên xâm nhập là thăm dò mạng mục tiêu sâu hơn bằng cách thực hiện liệt kê. Sử dụng các kỹ thuật khác nhau, bạn nên trích xuất thêm chi tiết về mạng như danh sách máy tính, tên người dùng, nhóm người dùng, cổng, hệ điều hành, tên máy, tài nguyên mạng và dịch vụ.

Thông tin thu được từ việc liệt kê sẽ giúp bạn xác định các điểm yếu trong bảo mật hệ thống mà kẻ tấn công có thể tìm cách khai thác. Thông tin như vậy cũng có thể cho phép kẻ tấn công thực hiện các cuộc tấn công mật khẩu để truy cập trái phép vào các tài nguyên hệ thống thông tin.

Trong các bước trước, bạn đã thu thập thông tin cần thiết về mục tiêu mà không vi phạm bất kỳ ranh giới pháp lý nào. Tuy nhiên, xin lưu ý rằng các hoạt động liệt kê có thể là bất hợp pháp tùy thuộc vào chính sách của tổ chức và bất kỳ luật nào đang có hiệu lực tại địa phương của bạn. Là một hacker đạo đức hoặc kiểm thử thâm nhập, bạn nên luôn luôn có được sự cho phép thích hợp trước khi thực hiện việc liệt kê.

Mục tiêu

Mục tiêu của bài lab là trích xuất thông tin về tổ chức mục tiêu bao gồm, nhưng không giới hạn ở:

-   Tên máy, hệ điều hành của chúng, dịch vụ và cổng

-   Tài nguyên mạng

-   Tên người dùng và nhóm người dùng

-   Danh sách các chia sẻ trên từng máy chủ trong mạng

-   Chính sách và mật khẩu

-   Bảng định tuyến

-   Cài đặt kiểm toán và dịch vụ

-   Chi tiết SNMP và FQDN

Tổng quan về Liệt kê

Liệt kê tạo ra một kết nối chủ động với hệ thống và thực hiện các truy vấn có hướng để thu thập thêm thông tin về mục tiêu. Nó trích xuất danh sách các máy tính, tên người dùng, nhóm người dùng, cổng, hệ điều hành, tên máy, tài nguyên mạng và dịch vụ bằng nhiều kỹ thuật khác nhau. Các kỹ thuật liệt kê được tiến hành trong môi trường mạng nội bộ.

Nhiệm vụ bài lab

Các hacker đạo đức hoặc chuyên gia kiểm thử xâm nhập sử dụng nhiều công cụ và kỹ thuật để liệt kê mạng mục tiêu. Các bài lab được khuyến nghị giúp bạn học các kỹ thuật liệt kê khác nhau bao gồm:

1.  Thực hiện liệt kê NetBIOS

    -   Thực hiện liệt kê NetBIOS bằng cách sử dụng các tiện ích dòng lệnh của Windows

2.  Thực hiện liệt kê SNMP

    -   Thực hiện liệt kê SNMP bằng cách sử dụng SnmpWalk

3.  Thực hiện liệt kê LDAP

    -   Thực hiện liệt kê LDAP bằng cách sử dụng Active Directory Explorer (AD Explorer)

4.  Thực hiện liệt kê NFS

    -   Thực hiện liệt kê NFS sử dụng RPCScan và SuperEnum

5.  Thực hiện liệt kê DNS

    -   Thực hiện liệt kê DNS bằng cách chuyển vùng

6.  Thực hiện liệt kê SMTP

    -   Thực hiện liệt kê SMTP bằng cách sử dụng Nmap

7.  Thực hiện liệt kê bằng các công cụ liệt kê khác nhau

    -   Liệt kê thông tin bằng cách sử dụng Kiểm kê Mạng Toàn cầu

8.  Thực hiện liệt kê bằng AI

    -   Thực hiện liệt kê bằng ShellGPT

Thí nghiệm 1: Thực hiện Liệt kê NetBIOS

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc kiểm thử xâm nhập, bước đầu tiên của bạn trong việc liệt kê hệ thống Windows là khai thác API NetBIOS. Liệt kê NetBIOS cho phép bạn thu thập thông tin về mục tiêu như danh sách các máy tính thuộc miền mục tiêu, các chia sẻ trên từng máy chủ trong mạng mục tiêu, các chính sách, mật khẩu, v.v. Dữ liệu này có thể được sử dụng để thăm dò các máy tính để biết thông tin chi tiết về mạng và tài nguyên máy chủ.

**Mục tiêu bài lab**

-   Thực hiện liệt kê NetBIOS bằng cách sử dụng các tiện ích dòng lệnh của Windows

**Tổng quan về Liệt kê NetBIOS**

NetBIOS là viết tắt của Network Basic Input Output System (Hệ thống Nhập xuất Cơ bản Mạng). Windows sử dụng NetBIOS để chia sẻ tập tin và máy in. Tên NetBIOS là một tên máy tính duy nhất được gán cho các hệ thống Windows, bao gồm một chuỗi ASCII 16 ký tự nhằm xác định thiết bị mạng qua TCP/IP. 15 ký tự đầu tiên được sử dụng cho tên thiết bị, và ký tự thứ 16 được dành cho dịch vụ hoặc loại bản ghi tên.

Dịch vụ NetBIOS dễ bị tấn công, vì nó đơn giản để khai thác và chạy trên các hệ thống Windows ngay cả khi không được sử dụng. Việc liệt kê NetBIOS cho phép kẻ tấn công đọc hoặc ghi vào một hệ thống máy tính từ xa (tùy thuộc vào việc các chia sẻ có sẵn hay không) hoặc thực hiện một cuộc tấn công từ chối dịch vụ (DoS).

Nhiệm vụ 1: Thực hiện Liệt kê NetBIOS sử dụng các tiện ích Dòng lệnh Windows

Nbtstat giúp khắc phục sự cố liên quan đến việc phân giải tên NETBIOS. Lệnh nbtstat loại bỏ và sửa các mục đã tải sẵn bằng cách sử dụng một số công tắc phân biệt chữ hoa chữ thường. Nbtstat có thể được sử dụng để liệt kê thông tin như thống kê giao thức NetBIOS qua TCP/IP (NetBT), bảng tên NetBIOS cho cả máy tính cục bộ và máy tính từ xa, và bộ nhớ đệm tên NetBIOS.

Lệnh net use kết nối một máy tính với, hoặc ngắt kết nối nó khỏi, một tài nguyên chia sẻ. Nó cũng hiển thị thông tin về các kết nối máy tính.

Ở đây, chúng ta sẽ sử dụng Nbtstat và Net use, các tiện ích dòng lệnh của Windows, để thực hiện liệt kê NetBIOS trên mạng mục tiêu.

Ở đây, chúng ta sẽ sử dụng máy Windows Server 2019 (10.10.1.19) để nhắm tới máy Windows 11 (10.10.1.11).

1.  Theo mặc định, máy Windows 11 được chọn. Nhấp vào Windows Server 2019 để chuyển sang máy Windows Server 2019. Nhấp vào Ctrl+Alt+Delete để kích hoạt máy và đăng nhập bằng Administrator/Pa\$\$w0rd[Windows Server 2019Ctrl+Alt+Delete](https://labclient.labondemand.com/Instructions/691e8f3a-07ba-400e-abe8-95c40abefa3b)

> Ngoài ra, bạn cũng có thể nhấp vào Pa\$\$w0rd dưới hình thu nhỏ của máy Windows Server 2019 trong pane Tài nguyên.
>
> Màn hình Mạng xuất hiện, nhấp vào Có để cho phép PC của bạn có thể được các PC và thiết bị khác trên mạng phát hiện.

2.  Mở một cửa sổ Command Prompt và chạy lệnh nbtstat -a \[Địa chỉ IP của máy từ xa\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.11).

> Trong lệnh này, -a hiển thị bảng tên NetBIOS của một máy tính từ xa.

3.  Kết quả xuất hiện, hiển thị bảng tên NetBIOS của một máy tính từ xa (ở đây là máy WINDOWS11), như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image2.jpeg){width="10.6625in" height="8.0in"}

4.  Trong cùng một cửa sổ Command Prompt, chạy lệnh nbtstat -c.

> Trong lệnh này, -c liệt kê nội dung của bộ nhớ đệm tên NetBIOS của máy tính từ xa.

5.  Kết quả xuất hiện, hiển thị nội dung của bộ đệm tên NetBIOS, bảng tên NetBIOS và địa chỉ IP đã được giải quyết của chúng.

> Có thể trích xuất thông tin này mà không cần tạo một phiên null (một phiên không xác thực).
>
> ![Screenshot](media/image3.jpeg){width="10.6625in" height="8.0in"}

6.  Bây giờ, chạy lệnh net use. Kết quả hiển thị thông tin về mục tiêu như trạng thái kết nối, thư mục/ổ đĩa chia sẻ và thông tin mạng, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image4.jpeg){width="10.6625in" height="8.0in"}

7.  Sử dụng thông tin này, những kẻ tấn công có thể đọc hoặc ghi vào hệ thống máy tính từ xa, tùy thuộc vào việc các chia sẻ có sẵn hay không, hoặc thậm chí phát động một cuộc tấn công DoS.

8.  Điều này kết thúc phần trình bày về cách thực hiện liệt kê NetBIOS sử dụng các tiện ích dòng lệnh Windows như Nbtstat và Net use.

9.  Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 4.1.1.1**

Đặt tên cho thư mục/ổ đĩa chia sẻ có sẵn trên máy Windows Server 2019.

Thí nghiệm 2: Thực hiện liệt kê SNMP

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc kiểm thử xâm nhập, bước tiếp theo của bạn là thực hiện liệt kê SNMP để trích xuất thông tin về các tài nguyên mạng (chẳng hạn như máy chủ, bộ định tuyến, thiết bị và các chia sẻ) và thông tin mạng (chẳng hạn như bảng ARP, bảng định tuyến, thông tin cụ thể về thiết bị và thống kê lưu lượng).

Sử dụng thông tin này, bạn có thể tiếp tục quét mục tiêu để tìm các lỗ hổng tiềm ẩn, xây dựng chiến lược tấn công và phát động các cuộc tấn công.

**Mục tiêu bài lab**

-   Thực hiện liệt kê SNMP bằng cách sử dụng SnmpWalk

**Tổng quan về Liệt kê SNMP**

SNMP (Giao thức Quản lý Mạng Đơn giản) là một giao thức lớp ứng dụng chạy trên UDP (Giao thức Gói dữ liệu Người dùng) và duy trì cũng như quản lý các bộ định tuyến, trung tâm và công tắc trên mạng IP. Các đại lý SNMP chạy trên các thiết bị mạng trên mạng Windows và UNIX.

Liệt kê SNMP sử dụng SNMP để tạo danh sách các tài khoản người dùng và thiết bị trên máy tính mục tiêu. SNMP sử dụng hai loại thành phần phần mềm để giao tiếp: tác nhân SNMP và trạm quản lý SNMP. Tác nhân SNMP được đặt trên thiết bị mạng, và trạm quản lý SNMP giao tiếp với tác nhân.

Nhiệm vụ 1: Thực hiện Liệt kê SNMP bằng SnmpWalk

SnmpWalk là một công cụ dòng lệnh quét nhiều nút SNMP ngay lập tức và xác định một tập hợp các biến có sẵn để truy cập mạng mục tiêu. Nó được gửi đến nút gốc để thông tin từ tất cả các nút phụ như bộ định tuyến và switch có thể được lấy về.

Ở đây, chúng tôi sẽ sử dụng SnmpWalk để thực hiện điều tra SNMP trên hệ thống mục tiêu.

1.  Nhấp vào Parrot Security để chuyển sang máy Parrot Security. Đăng nhập với attacker/toor, mở một cửa sổ Terminal và thực hiện sudo su để chạy các chương trình với tư cách người dùng root (Khi được yêu cầu, nhập mật khẩu toor).[Parrot Security](https://labclient.labondemand.com/Instructions/691e8f3a-07ba-400e-abe8-95c40abefa3b)

> Mật khẩu mà bạn nhập sẽ không hiển thị.

2.  Chạy lệnh snmpwalk -v1 -c public \[địa chỉ IP đích\] (ở đây, địa chỉ IP đích là 10.10.1.22).

> **-v: chỉ định số phiên bản SNMP (1 hoặc 2c hoặc 3) và -c: đặt chuỗi cộng đồng.**

3.  Kết quả hiển thị tất cả các OID, biến và các thông tin liên quan khác.

> ![Screenshot](media/image5.jpeg){width="10.6625in" height="8.0in"}

4.  Chạy lệnh snmpwalk -v2c -c public \[Địa chỉ IP mục tiêu\] để thực hiện việc liệt kê SNMPv2 trên máy mục tiêu (ở đây, địa chỉ IP mục tiêu là 10.10.1.22).

> **-v: chỉ định phiên bản SNMP (ở đây, chọn 2c) và -c: đặt chuỗi cộng đồng.**

5.  Kết quả hiển thị dữ liệu được truyền từ đại lý SNMP đến máy chủ SNMP, bao gồm thông tin về máy chủ, thông tin đăng nhập người dùng và các tham số khác.

> ![Screenshot](media/image6.jpeg){width="10.6625in" height="8.0in"}

6.  Đây kết thúc phần trình bày về cách thực hiện liệt kê SNMP bằng SnmpWalk.

7.  Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 4.2.1.1**

Sử dụng SnmpWalk để thực hiện liệt kê SNMP trên máy Windows Server 2022. Nhập tùy chọn để thiết lập chuỗi cộng đồng.

thí nghiệm 3: thực hiện việc liệt kê ldap

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc chuyên viên thử nghiệm xâm nhập, bước tiếp theo sau khi liệt kê SNMP là thực hiện liệt kê LDAP để truy cập danh sách thư mục trong Active Directory hoặc các dịch vụ thư mục khác. Các dịch vụ thư mục cung cấp thông tin được cấu trúc theo cấp bậc và logic về các thành phần của mạng, từ danh sách máy in đến thư mục email doanh nghiệp. Theo nghĩa này, chúng giống như sơ đồ tổ chức của một công ty.

Liệt kê LDAP cho phép bạn thu thập thông tin về tên người dùng, địa chỉ, chi tiết phòng ban, tên máy chủ, v.v.

**Mục tiêu bài lab**

-   Thực hiện liệt kê LDAP bằng cách sử dụng Active Directory Explorer (AD Explorer)

**Tổng quan về Liệt kê LDAP**

LDAP (Giao thức Truy cập Thư mục Nhẹ) là một giao thức Internet dùng để truy cập các dịch vụ thư mục phân tán qua mạng. LDAP sử dụng DNS (Hệ thống Tên Miền) để tra cứu nhanh và giải quyết các truy vấn một cách nhanh chóng. Một client bắt đầu một phiên LDAP bằng cách kết nối tới DSA (Đại lý Hệ thống Thư mục), thường trên cổng TCP 389, và gửi một yêu cầu thao tác tới DSA, sau đó DSA sẽ phản hồi. BER (Quy tắc Mã hóa Cơ bản) được sử dụng để truyền thông tin giữa client và server. Người ta có thể tra cứu ẩn danh dịch vụ LDAP để lấy thông tin nhạy cảm như tên người dùng, địa chỉ, chi tiết phòng ban và tên máy chủ.

Nhiệm vụ 1: Thực hiện liệt kê LDAP sử dụng Trình khám phá Active Directory (AD Explorer)

Trình khám phá Active Directory (AD Explorer) là một công cụ xem và chỉnh sửa Active Directory (AD) nâng cao. Nó có thể được sử dụng để điều hướng cơ sở dữ liệu AD một cách dễ dàng, xác định các vị trí yêu thích, xem thuộc tính và đặc điểm của đối tượng mà không cần mở các hộp thoại, chỉnh sửa quyền, xem sơ đồ của đối tượng và thực hiện các tìm kiếm tinh vi có thể được lưu lại và thực hiện lại.

Ở đây, chúng tôi sẽ sử dụng AD Explorer để thực hiện liệt kê LDAP trên một miền AD và sửa đổi các tài khoản người dùng miền.

1.  Nhấp vào Windows Server 2019 để chuyển sang máy Windows Server 2019 và nhấp vào Ctrl+Alt+Delete để kích hoạt máy. Đăng nhập bằng Administrator/Pa\$\$w0rd.[Windows Server 2019Ctrl+Alt+Delete](https://labclient.labondemand.com/Instructions/691e8f3a-07ba-400e-abe8-95c40abefa3b)

2.  Điều hướng đến Z:\\CEHv13 Module 04 Enumeration\\LDAP Enumeration Tools\\Active Directory Explorer và nhấp đúp vào ADExplorer.exe.

3.  Cửa sổ Thỏa thuận cấp phép Active Directory Explorer xuất hiện; nhấp vào Đồng ý.

4.  Cửa sổ bật lên Kết nối với Active Directory xuất hiện; nhập địa chỉ IP của mục tiêu vào trường Kết nối với (tại đây, chúng ta đang nhắm tới máy Windows Server 2022: 10.10.1.22) và nhấp OK.

> ![Screenshot](media/image7.jpeg){width="10.6625in" height="8.0in"}

5.  Trình duyệt Active Directory hiển thị cấu trúc thư mục Active Directory trong khung bên trái, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image8.jpeg){width="10.6625in" height="8.0in"}

6.  Bây giờ, mở rộng DC=CEH, DC=com và CN=Users bằng cách nhấp vào dấu "+" để khám phá chi tiết người dùng trong miền.

> ![Screenshot](media/image9.jpeg){width="10.6625in" height="8.0in"}

7.  Nhấp vào bất kỳ tên người dùng nào (trong ngăn bên trái) để hiển thị thuộc tính của nó trong ngăn bên phải.

> ![Screenshot](media/image10.jpeg){width="10.6625in" height="8.0in"}

8.  Nhấp chuột phải vào bất kỳ thuộc tính nào trong khung bên phải (ở đây là displayName) và nhấp vào Sửa... từ menu ngữ cảnh để chỉnh sửa hồ sơ người dùng.

> ![Screenshot](media/image11.jpeg){width="15.0in" height="9.376388888888888in"}

9.  Cửa sổ Modify Attribute xuất hiện. Trước tiên, chọn tên người dùng trong phần Value, sau đó nhấp vào nút Modify.... Cửa sổ bật lên Edit Value xuất hiện. Đổi tên người dùng trong trường Value data và nhấp OK để lưu các thay đổi.

10. Bạn có thể đọc và chỉnh sửa các thuộc tính hồ sơ người dùng khác theo cùng một cách.

11. Điều này kết thúc phần trình diễn về cách thực hiện liệt kê LDAP bằng AD Explorer.

12. Bạn cũng có thể sử dụng các công cụ liệt kê LDAP khác như Softerra LDAP Administrator (https://www.ldapadministrator.com), LDAP Admin Tool (https://www.ldapsoft.com), LDAP Account Manager (https://www.ldap-account-manager.org), và LDAP Search (https://securityxploded.com) để thực hiện liệt kê LDAP trên mục tiêu.

13. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 4.3.1.1**

Thực hiện liệt kê LDAP bằng cách sử dụng Active Directory Explorer (AD Explorer) và tìm địa chỉ IP của máy Domain Controller.

![](media/image12.wmf)

Đúng

**Câu hỏi 4.3.1.2**

Thực hiện liệt kê LDAP bằng cách sử dụng Active Directory Explorer (AD Explorer) và tìm userPrincipalName cho người dùng có tên Jason M.

Thí nghiệm 4: Thực hiện liệt kê NFS

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc kiểm tra xâm nhập, bước tiếp theo sau khi nhận dạng LDAP là thực hiện nhận dạng NFS để xác định các thư mục được xuất và trích xuất danh sách các khách hàng kết nối với máy chủ, cùng với địa chỉ IP của họ và dữ liệu được chia sẻ liên quan đến họ.

Sau khi thu thập được thông tin này, có thể giả mạo địa chỉ IP mục tiêu để truy cập đầy đủ các tập tin chia sẻ trên máy chủ.

**Mục tiêu bài lab**

-   Thực hiện liệt kê NFS sử dụng RPCScan và SuperEnum

**Tổng quan về Liệt kê NFS**

NFS (Hệ thống Tệp Mạng) là một loại hệ thống tệp cho phép người dùng máy tính truy cập, xem, lưu trữ và cập nhật tệp qua một máy chủ từ xa. Dữ liệu từ xa này có thể được truy cập bởi máy tính khách theo cùng cách mà nó được truy cập trên hệ thống cục bộ.

Nhiệm vụ 1: Thực hiện Liệt kê NFS sử dụng RPCScan và SuperEnum

RPCScan giao tiếp với các dịch vụ RPC (gọi thủ tục từ xa) và kiểm tra các cấu hình sai trên các chia sẻ NFS. Nó liệt kê các dịch vụ RPC, điểm gắn kết và các thư mục có thể truy cập qua NFS. Nó cũng có thể liệt kê đệ quy các chia sẻ NFS. SuperEnum bao gồm một tập lệnh thực hiện việc liệt kê cơ bản bất kỳ cổng mở nào, bao gồm cả cổng NFS (2049).

Ở đây, chúng tôi sẽ sử dụng RPCScan và SuperEnum để liệt kê các dịch vụ NFS đang chạy trên máy mục tiêu.

Trước khi bắt đầu nhiệm vụ này, cần phải bật dịch vụ NFS trên máy mục tiêu (Windows Server 2019). Việc này sẽ được thực hiện trong Bước #1-6.

1.  Nhấp vào Windows Server 2019 để chuyển sang máy Windows Server 2019. Trên máy Windows Server 2019, nhấp vào nút Bắt đầu ở góc dưới bên trái của Màn hình nền và mở Trình quản lý Máy chủ.[Windows Server 2019](https://labclient.labondemand.com/Instructions/691e8f3a-07ba-400e-abe8-95c40abefa3b)

> Nếu bạn đã đăng xuất khỏi máy Windows Server 2019, hãy nhấn Ctrl+Alt+Delete, sau đó đăng nhập bằng Administrator/Pa\$\$w0rd.[Ctrl+Alt+Delete](https://labclient.labondemand.com/Instructions/691e8f3a-07ba-400e-abe8-95c40abefa3b)

2.  Cửa sổ chính của Trình quản lý Máy chủ xuất hiện. Theo mặc định, Bảng điều khiển sẽ được chọn; nhấp vào Thêm vai trò và tính năng.

> ![Screenshot](media/image13.jpeg){width="10.6625in" height="8.0in"}

3.  Cửa sổ Trình hướng dẫn Thêm Vai trò và Tính năng xuất hiện. Nhấp vào Tiếp theo ở đây và trong các trình hướng dẫn Loại Cài đặt và Chọn Máy chủ.

4.  Mục Vai Trò Máy Chủ xuất hiện. Mở rộng Dịch Vụ Tệp và Lưu Trữ và chọn hộp kiểm cho Máy Chủ NFS dưới tùy chọn Dịch Vụ Tệp và iSCSI, như được hiển thị trong ảnh chụp màn hình. Nhấp vào Tiếp theo.

> Trong cửa sổ bật lên Thêm các tính năng cần thiết cho Máy chủ cho NFS?, nhấp vào nút Thêm tính năng.
>
> ![Screenshot](media/image14.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image15.jpeg){width="10.6625in" height="8.0in"}

5.  Trong phần Tính năng, nhấp vào Tiếp theo. Phần Xác nhận xuất hiện; nhấp vào Cài đặt để cài đặt các tính năng đã chọn.

6.  Các tính năng bắt đầu được cài đặt, với tiến trình được hiển thị bởi thanh trạng thái Cài đặt tính năng. Khi cài đặt hoàn tất, nhấp vào Đóng.

7.  Sau khi bật dịch vụ NFS, cần kiểm tra xem nó có đang chạy trên hệ thống mục tiêu (Windows Server 2019) hay không. Để thực hiện điều này, chúng ta sẽ sử dụng máy Parrot Security.

8.  Nhấp vào Parrot Security để chuyển sang máy Parrot Security. Mở một cửa sổ Terminal và thực thi sudo su để chạy các chương trình với quyền người dùng root (Khi được nhắc, nhập mật khẩu toor).[Parrot Security](https://labclient.labondemand.com/Instructions/691e8f3a-07ba-400e-abe8-95c40abefa3b)

> Mật khẩu mà bạn nhập sẽ không hiển thị.

9.  Thực thi lệnh nmap -p 2049 \[Địa chỉ IP mục tiêu\] (ở đây địa chỉ IP mục tiêu là 10.10.1.19).

> **-p: chỉ định cổng.**

10. Kết quả quét xuất hiện cho thấy cổng 2049 đang mở, và dịch vụ NFS đang chạy trên đó, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image16.jpeg){width="10.6625in" height="8.0in"}

11. Chạy lệnh cd SuperEnum để chuyển đến thư mục SuperEnum.

12. Chạy lệnh echo \"10.10.1.19\" \>\> Target.txt để tạo một tệp chứa địa chỉ IP của máy mục tiêu (10.10.1.19).

> Bạn có thể nhập nhiều địa chỉ IP vào tệp Target.txt. Tuy nhiên, trong nhiệm vụ này chúng ta chỉ nhắm mục tiêu vào một máy, Windows Server 2019 (10.10.1.19).
>
> ![Screenshot](media/image17.jpeg){width="10.6625in" height="8.0in"}

13. Thực thi ./superenum command. Dưới mục Nhập tên tệp danh sách IP kèm đường dẫn, nhập Target.txt và nhấn Enter.

> Nếu bạn gặp lỗi khi chạy script ./superenum, hãy thực hiện lệnh chmod +x superenum, sau đó lặp lại Bước #13.
>
> ![Screenshot](media/image18.jpeg){width="10.6625in" height="8.0in"}

14. Kịch bản bắt đầu quét địa chỉ IP mục tiêu để tìm các dịch vụ NFS mở và các dịch vụ khác.

> Quét sẽ mất khoảng 15-20 phút để hoàn thành.

15. Sau khi quét xong, kéo xuống để xem kết quả. Quan sát thấy cổng 2049 đang mở và dịch vụ NFS đang chạy trên đó.

> ![Screenshot](media/image19.jpeg){width="10.6625in" height="8.0in"}

16. Bạn cũng có thể quan sát các cổng mở khác và các dịch vụ đang chạy trên chúng.

17. Trong cửa sổ terminal, chạy lệnh cd .. để trở về thư mục gốc.

18. Bây giờ, chúng ta sẽ thực hiện liệt kê NFS bằng cách sử dụng RPCScan. Để làm điều đó, chạy lệnh cd RPCScan.

19. Chạy python3 rpc-scan.py \[Địa chỉ IP mục tiêu\] \--rpc command (ở đây, địa chỉ IP mục tiêu là 10.10.1.19, máy Windows Server 2019).

> **\--rpc: liệt kê RPC (portmapper).**

20. Kết quả xuất hiện, hiển thị rằng cổng 2049 đang mở, và dịch vụ NFS đang chạy trên đó.

> ![Screenshot](media/image20.jpeg){width="10.6625in" height="8.0in"}

21. Điều này kết thúc buổi trình diễn về việc thực hiện liệt kê NFS bằng SuperEnum và RPCScan.

22. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 4.4.1.1**

Thực hiện Liệt kê NFS sử dụng RPCScan và SuperEnum và tìm cổng được sử dụng bởi dịch vụ NFS trên 10.10.1.19.

Thí nghiệm 5: Thực hiện liệt kê DNS

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc kiểm thử xâm nhập, bước tiếp theo sau khi liệt kê NFS là thực hiện liệt kê DNS. Quá trình này cung cấp thông tin như tên máy chủ DNS, tên host, tên máy, tên người dùng, địa chỉ IP và các bí danh được gán trong một miền mục tiêu.

**Mục tiêu bài lab**

-   Thực hiện liệt kê DNS bằng cách chuyển vùng

**Tổng quan về Liệt kê DNS**

Các kỹ thuật liệt kê DNS được sử dụng để thu thập thông tin về các máy chủ DNS và cơ sở hạ tầng mạng của tổ chức mục tiêu. Việc liệt kê DNS có thể được thực hiện bằng các kỹ thuật sau:

-   Chuyển vùng

Nhiệm vụ 1: Thực hiện Liệt kê DNS bằng cách Chuyển vùng

Chuyển vùng DNS là quá trình chuyển một bản sao của tệp vùng DNS từ máy chủ DNS chính sang máy chủ DNS phụ. Trong hầu hết các trường hợp, máy chủ DNS duy trì một máy chủ dự phòng hoặc máy chủ phụ để dự phòng, máy này lưu giữ tất cả thông tin được lưu trữ trong máy chủ chính.

Nếu cài đặt chuyển vùng DNS được bật trên máy chủ DNS mục tiêu, nó sẽ cung cấp thông tin DNS; nếu không, nó sẽ trả về lỗi nói rằng việc chuyển vùng đã thất bại hoặc từ chối chuyển vùng.

Ở đây, chúng tôi sẽ thực hiện việc liệt kê DNS thông qua chuyển vùng bằng cách sử dụng các tiện ích dig (hệ thống dựa trên Linux) và nslookup (hệ thống dựa trên Windows).

1.  Chúng ta sẽ bắt đầu với việc liệt kê DNS của các máy chủ DNS Linux. Nhấp vào Parrot Security để chuyển sang máy Parrot Security và đăng nhập với attacket/toor.[Parrot Security](https://labclient.labondemand.com/Instructions/691e8f3a-07ba-400e-abe8-95c40abefa3b)

2.  Mở một cửa sổ Terminal và thực thi sudo su để chạy các chương trình với quyền người dùng root (Khi được yêu cầu, nhập mật khẩu toor).

> Mật khẩu mà bạn nhập sẽ không hiển thị.

3.  Bây giờ, chạy lệnh cd để chuyển đến thư mục gốc.

4.  Chạy lệnh dig ns \[Tên Miền Mục Tiêu\] (ở đây, tên miền mục tiêu là www.certifiedhacker.com).

> Trong lệnh này, ns trả về các máy chủ tên trong kết quả

5.  Lệnh trên truy xuất thông tin về tất cả các máy chủ tên DNS của miền mục tiêu và hiển thị nó trong PHẦN TRẢ LỜI, như được hiển thị trong ảnh chụp màn hình.

> Trên các hệ thống dựa trên Linux, lệnh dig được sử dụng để truy vấn các máy chủ tên DNS nhằm lấy thông tin về địa chỉ máy chủ đích, máy chủ tên, các máy chủ thư, v.v.
>
> ![Screenshot](media/image21.jpeg){width="10.6625in" height="8.0in"}

6.  Chạy lệnh dig @\[NameServer\] \[Target Domain\] axfr (ở đây, tên máy chủ là ns1.bluehost.com và miền mục tiêu là www.certifiedhacker.com).

> Trong lệnh này, axfr lấy thông tin vùng.

7.  Kết quả xuất hiện, hiển thị rằng máy chủ khả dụng, nhưng việc Chuyển dữ liệu đã thất bại, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image22.jpeg){width="10.6625in" height="8.0in"}

8.  Sau khi lấy thông tin máy chủ tên DNS, kẻ tấn công có thể sử dụng một trong các máy chủ để kiểm tra xem DNS mục tiêu có cho phép chuyển vùng hay không. Ở đây, chuyển vùng không được phép cho miền mục tiêu; đây là lý do lệnh đã dẫn đến thông báo: Chuyển không thành công. Một người kiểm thử xâm nhập nên thử chuyển vùng DNS trên các miền khác nhau của tổ chức mục tiêu.

9.  Bây giờ, chúng ta sẽ thực hiện liệt kê DNS trên các máy chủ DNS Windows.

10. Nhấp vào Windows 11 để chuyển sang máy Windows 11.[Windows 11](https://labclient.labondemand.com/Instructions/691e8f3a-07ba-400e-abe8-95c40abefa3b)

11. Nhấp vào biểu tượng Tìm kiếm trên Windows ( ) trên Màn hình. Tìm kiếm cmd trong trường tìm kiếm, Command Prompt xuất hiện trong kết quả, nhấp vào Mở để khởi chạy nó.![search6icon.jpg](media/image23.jpeg){width="0.3763888888888889in" height="0.3375in"}

12. Cửa sổ Dấu nhắc lệnh xuất hiện; thực hiện lệnh nslookup.

13. Trong chế độ tương tác của nslookup, thực hiện lệnh set querytype=soa.

14. Nhập tên miền mục tiêu certifiedhacker.com và nhấn Enter. Điều này sẽ giải quyết thông tin của tên miền mục tiêu.

> set querytype=soa đặt loại truy vấn thành bản ghi SOA (Start of Authority) để lấy thông tin quản trị về vùng DNS của miền mục tiêu certifiedhacker.com.

15. Kết quả xuất hiện, hiển thị thông tin về miền mục tiêu như máy chủ tên chính và địa chỉ thư chịu trách nhiệm, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image24.jpeg){width="10.6625in" height="8.0in"}

16. Trong chế độ tương tác nslookup, thực hiện lệnh ls -d \[Name Server\] (ở đây, tên là ns1.bluehost.com).

> Trong lệnh này, ls -d yêu cầu một chuyển vùng của máy chủ tên được chỉ định.

17. Kết quả xuất hiện, hiển thị rằng máy chủ DNS đã từ chối việc chuyển vùng, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image25.jpeg){width="10.6625in" height="8.0in"}

18. Sau khi lấy thông tin máy chủ tên DNS, kẻ tấn công có thể sử dụng một trong các máy chủ để kiểm tra xem DNS của mục tiêu có cho phép chuyển vùng hay không. Ở đây, việc chuyển vùng đã bị từ chối đối với tên miền mục tiêu. Một người kiểm thử xâm nhập nên cố gắng thực hiện chuyển vùng DNS trên các tên miền khác nhau của tổ chức mục tiêu.

19. Điều này kết thúc buổi trình diễn việc thực hiện chuyển vùng DNS bằng các lệnh dig và nslookup.

20. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 4.5.1.1**

Bạn có thể thực hiện chuyển vùng trên máy chủ chính của certifiedhacker.com không? (Có/Không)

![](media/image12.wmf)

Đúng

**Câu hỏi 4.5.1.2**

Thực hiện liệt kê DNS và tìm "địa chỉ email chịu trách nhiệm" cho tên miền certifiedhacker.com.

Thí nghiệm 6: Thực hiện liệt kê SMTP

**kịch bản bài lab bài lab**

Là một hacker đạo đức hoặc kiểm thử xâm nhập, bước tiếp theo là thực hiện liệt kê SMTP. Liệt kê SMTP được thực hiện để thu thập danh sách người dùng hợp lệ, địa chỉ giao hàng, người nhận tin nhắn trên một máy chủ SMTP.

**Mục tiêu bài lab**

-   Thực hiện liệt kê SMTP bằng cách sử dụng Nmap

**Tổng quan về Liệt kê SMTP**

Giao thức Truyền Thư Điện Tử Đơn giản (SMTP) là một giao thức truyền thông dựa trên tiêu chuẩn internet cho việc truyền thư điện tử. Hệ thống thư thường sử dụng SMTP cùng với POP3 và IMAP, cho phép người dùng lưu trữ tin nhắn trong hộp thư của máy chủ và tải chúng từ máy chủ khi cần thiết. SMTP sử dụng các máy chủ trao đổi thư (MX) để định hướng thư qua DNS. Nó chạy trên cổng TCP 25, 2525 hoặc 587.

Nhiệm vụ 1: Thực hiện Liệt kê SMTP bằng Nmap

Công cụ lập trình kịch bản Nmap có thể được sử dụng để liệt kê dịch vụ SMTP đang chạy trên hệ thống mục tiêu, nhằm thu thập thông tin về tất cả các tài khoản người dùng trên máy chủ SMTP.

Ở đây, chúng ta sẽ sử dụng Nmap để thực hiện liệt kê SMTP.

1.  Trong máy Parrot Security, mở một cửa sổ Terminal và thực hiện sudo su để chạy các chương trình với quyền người dùng root (Khi được nhắc, nhập mật khẩu toor).

2.  Chạy lệnh nmap -p 25 \--script=smtp-enum-users \[Địa chỉ IP đích\] (ở đây, địa chỉ IP đích là 10.10.1.19).

> **-p: chỉ định cổng, và \--script: đối số được sử dụng để chạy một script nhất định (ở đây, script là smtp-enum-users).**

3.  Kết quả hiển thị danh sách tất cả các người dùng email có thể trên máy mục tiêu (10.10.1.19), như được hiển thị trong ảnh chụp màn hình bên dưới.

> ![Screenshot](media/image26.jpeg){width="10.6625in" height="8.0in"}

4.  Chạy lệnh nmap -p 25 \--script=smtp-open-relay \[Địa chỉ IP đích\] (ở đây, địa chỉ IP đích là 10.10.1.19).

> **-p: chỉ định cổng, và đối số -script: được sử dụng để chạy một tập lệnh nhất định (ở đây, tập lệnh là smtp-open-relay).**

5.  Kết quả xuất hiện hiển thị danh sách các máy chủ SMTP mở trên máy mục tiêu (10.10.1.19), như được hiển thị trong ảnh chụp màn hình bên dưới.

> ![Screenshot](media/image27.jpeg){width="10.6625in" height="8.0in"}

6.  Chạy lệnh nmap -p 25 \--script=smtp-commands \[Địa chỉ IP mục tiêu\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.19).

> **-p: chỉ định cổng, và đối số -script: được sử dụng để chạy một script nhất định (ở đây, script là smtp-commands).**

7.  Một danh sách tất cả các lệnh SMTP có sẵn trong thư mục Nmap xuất hiện. Bạn có thể khám phá thêm các lệnh để thu thập thông tin chi tiết về máy chủ mục tiêu.

> ![Screenshot](media/image28.jpeg){width="10.6625in" height="8.0in"}

8.  Sử dụng thông tin này, những kẻ tấn công có thể thực hiện các cuộc tấn công phun mật khẩu để truy cập trái phép vào các tài khoản người dùng.

9.  Điều này kết thúc phần trình diễn việc liệt kê SMTP bằng cách sử dụng Nmap.

10. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 4.6.1.1**

Sử dụng Nmap để thực hiện liệt kê SMTP nhằm liệt kê danh sách tất cả người dùng email có thể có trên máy Windows Server 2019. Nhập số lượng người dùng được liệt kê trên máy mục tiêu

bài lab 7: Thực hiện liệt kê bằng các công cụ liệt kê khác nhau

**kịch bản bài lab bài lab**

Các chi tiết thu thập được trong các bước trước có thể không tiết lộ tất cả các lỗ hổng tiềm ẩn trong mạng mục tiêu. Có thể còn nhiều thông tin khác có sẵn có thể giúp tin tặc xác định các kẽ hở để khai thác. Là một hacker có đạo đức, bạn nên sử dụng một loạt các công cụ để tìm được càng nhiều thông tin càng tốt về các hệ thống của mạng mục tiêu. Hoạt động bài lab này sẽ minh họa các công cụ liệt kê thêm để trích xuất nhiều thông tin hơn về hệ thống mục tiêu.

**Mục tiêu bài lab**

-   Liệt kê thông tin bằng cách sử dụng Kiểm kê Mạng Toàn cầu

**Tổng quan về các công cụ liệt kê**

Tóm tắt những gì bạn đã học cho đến nay, các công cụ liệt kê được sử dụng để thu thập thông tin chi tiết về các hệ thống mục tiêu nhằm khai thác chúng. Thông tin được thu thập bởi các công cụ liệt kê này bao gồm dữ liệu về dịch vụ NetBIOS, tên người dùng và tên miền, thư mục chia sẻ, mạng (chẳng hạn như bảng ARP, bảng định tuyến, lưu lượng, v.v.), tài khoản người dùng, dịch vụ thư mục, v.v.

Nhiệm vụ 1: Liệt kê Thông tin bằng cách sử dụng Kiểm kê Mạng Toàn cầu

Global Network Inventory được sử dụng như một công cụ quét kiểm toán trong môi trường không triển khai và không cần phần mềm tác nhân. Nó quét một hoặc nhiều máy tính theo dải IP hoặc tên miền, như được định nghĩa trong tập tin máy chủ của Global Network Inventory.

Ở đây, chúng tôi sẽ sử dụng Global Network Inventory để liệt kê các loại dữ liệu khác nhau từ một phạm vi địa chỉ IP mục tiêu hoặc một địa chỉ IP đơn lẻ.

1.  Nhấp vào Windows 11 để chuyển sang máy Windows 11, nhấp vào biểu tượng Tìm kiếm ( ) trên Màn hình. Nhập Global vào trường tìm kiếm, Global Network Inventory xuất hiện trong kết quả, nhấp vào Mở để khởi chạy nó.[Windows 11](https://labclient.labondemand.com/Instructions/691e8f3a-07ba-400e-abe8-95c40abefa3b)![search7icon.jpg](media/image23.jpeg){width="0.3763888888888889in" height="0.3375in"}

> ![Screenshot](media/image29.jpeg){width="10.6625in" height="8.0in"}
>
> Nếu một cửa sổ bật lên Kiểm soát Tài khoản Người dùng xuất hiện, hãy nhấp vào Có.

2.  Trình hướng dẫn Giới thiệu về Global Network Inventory xuất hiện; nhấp vào Tôi đồng ý.

> ![Screenshot](media/image30.jpeg){width="10.6625in" height="8.0in"}

3.  Giao diện Người dùng (GUI) Kiểm kê Mạng Toàn cầu xuất hiện. Nhấp vào Đóng trên cửa sổ bật lên Mẹo trong Ngày.

> ![Screenshot](media/image31.jpeg){width="10.6625in" height="8.0in"}

4.  Cửa sổ Trình thuật sĩ Kiểm toán Mới xuất hiện; nhấp vào Tiếp theo.

> ![Screenshot](media/image32.jpeg){width="10.6625in" height="8.0in"}

5.  Trong mục Chế độ Quét Kiểm tra, nhấp vào nút radio Quét địa chỉ đơn, sau đó nhấp vào Tiếp theo.

> Bạn cũng có thể quét một phạm vi IP bằng cách nhấp vào nút radio quét phạm vi IP, sau đó bạn sẽ chỉ định phạm vi IP mục tiêu.
>
> ![Screenshot](media/image33.jpeg){width="10.6625in" height="8.0in"}

6.  Trong phần Quét Địa chỉ Đơn, hãy chỉ định địa chỉ IP mục tiêu trong trường Tên của tùy chọn Địa chỉ đơn (trong ví dụ này, địa chỉ IP mục tiêu là 10.10.1.22); Nhấn Tiếp theo.

> ![Screenshot](media/image34.jpeg){width="10.6625in" height="8.0in"}

7.  Phần tiếp theo là Cài đặt Xác thực; chọn nút radio Kết nối làm và nhập thông tin đăng nhập máy Windows Server 2022 (Tên miền\\Tên người dùng: Quản trị viên và Mật khẩu: Pa\$\$w 0rd), sau đó nhấp Tiếp theo.

> Trong thực tế, kẻ tấn công không biết thông tin đăng nhập của máy từ xa. Trong kịch bản bài lab này, họ chọn tùy chọn Kết nối với tư cách người dùng đang đăng nhập và thực hiện quét để xác định máy nào đang hoạt động trong mạng. Với tùy chọn này, họ sẽ không thể trích xuất tất cả thông tin về hệ thống mục tiêu. Vì bài lab này chỉ nhằm mục đích đánh giá, chúng tôi đã nhập trực tiếp thông tin đăng nhập của máy từ xa.
>
> ![Screenshot](media/image35.jpeg){width="10.6625in" height="8.0in"}

8.  Trong bước cuối cùng của trình hướng dẫn, để nguyên các cài đặt mặc định và nhấp vào Hoàn tất.

> ![Screenshot](media/image36.jpeg){width="10.6625in" height="8.0in"}

9.  Cửa sổ tiến trình Quét sẽ xuất hiện.

> ![Screenshot](media/image37.jpeg){width="10.6625in" height="8.0in"}

10. Kết quả được hiển thị khi quá trình quét kết thúc. Bản tóm tắt quét của địa chỉ IP mục tiêu đã quét (10.10.1.22) xuất hiện.

> Kết quả quét có thể thay đổi khi bạn thực hiện nhiệm vụ này.
>
> ![Screenshot](media/image38.jpeg){width="10.6625in" height="8.0in"}

11. Di chuột qua chi tiết Máy tính dưới tab Tóm tắt quét để xem tóm tắt quét, như được hiển thị trong ảnh chụp màn hình.

> ![A.jpg](media/image39.jpeg){width="10.6625in" height="8.0in"}

12. Nhấp vào tab Hệ điều hành và di chuột qua chi tiết Windows để xem toàn bộ thông tin chi tiết của máy.

> ![B.jpg](media/image40.jpeg){width="10.6625in" height="8.0in"}

13. Nhấp vào tab BIOS, và di chuột qua chi tiết của Windows để hiển thị thông tin cài đặt BIOS chi tiết.

> ![C.jpg](media/image41.jpeg){width="10.6625in" height="8.0in"}

14. Nhấp vào tab NetBIOS, và di chuyển con trỏ chuột qua bất kỳ ứng dụng NetBIOS nào để hiển thị thông tin chi tiết về NetBIOS của mục tiêu.

> Di chuột qua từng ứng dụng NetBIOS để xem chi tiết của nó.
>
> ![D.jpg](media/image42.jpeg){width="10.6625in" height="8.0in"}

15. Nhấp vào tab Nhóm người dùng và di chuột qua bất kỳ tên người dùng nào để hiển thị thông tin chi tiết về nhóm người dùng.

> Di chuột qua từng tên người dùng để xem chi tiết của nó.
>
> ![E.jpg](media/image43.jpeg){width="10.6625in" height="8.0in"}

16. Nhấp vào tab Người dùng, và di chuột qua tên người dùng để xem chi tiết đăng nhập của máy mục tiêu.

> ![F.jpg](media/image44.jpeg){width="10.6625in" height="8.0in"}

17. Nhấp vào tab Dịch vụ và di chuột qua bất kỳ dịch vụ nào để xem chi tiết của nó.

> ![G.jpg](media/image45.jpeg){width="10.6625in" height="8.0in"}

18. Nhấp vào tab Phần mềm đã cài đặt và di chuột qua bất kỳ phần mềm nào để xem chi tiết của nó.

> ![H.jpg](media/image46.jpeg){width="10.6625in" height="8.0in"}

19. Nhấp vào tab Chia sẻ, và di chuyển con trỏ chuột qua bất kỳ thư mục chia sẻ nào để xem chi tiết của nó.

> ![I.jpg](media/image47.jpeg){width="10.6625in" height="8.0in"}

20. Tương tự, bạn có thể nhấp vào các tab khác như Hệ thống Máy tính, Bộ xử lý, Bo mạch chính, Bộ nhớ, Hệ thống SNMP và Cập nhật nóng. Di chuột qua các phần tử dưới mỗi tab để xem thông tin chi tiết của chúng.

21. Điều này kết thúc phần trình diễn cách thực hiện liệt kê bằng cách sử dụng Hệ thống Kiểm kê Mạng Toàn cầu.

22. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 4.7.1.1**

Thực hiện liệt kê sử dụng Global Network Inventory và tìm tên đầy đủ của Hệ điều hành được cài đặt trên máy tại 10.10.1.22.

Thí nghiệm 8: Thực hiện liệt kê sử dụng AI

**kịch bản bài lab bài lab**

Trong bài lab này, bạn sẽ sử dụng các công cụ và kỹ thuật hỗ trợ bởi AI để thực hiện việc liệt kê trên một mạng mục tiêu. Mục tiêu là thu thập thông tin chi tiết về các tài nguyên và hạ tầng mạng, điều này sẽ giúp bạn xác định các điểm yếu tiềm ẩn và lập kế hoạch cho các hoạt động kiểm tra xâm nhập tiếp theo.

**Mục tiêu bài lab**

-   Thực hiện Liệt kê bằng ShellGPT

**Tổng quan về liệt kê sử dụng AI**

Trí tuệ nhân tạo (AI) có thể cải thiện đáng kể quá trình liệt kê bằng cách tự động hoá các nhiệm vụ, phân tích các bộ dữ liệu lớn và xác định các mẫu mà các công cụ truyền thống có thể bỏ sót. AI có thể hợp lý hóa quy trình liệt kê, làm cho nó nhanh hơn, hiệu quả hơn và chính xác hơn.

Nhiệm vụ 1: Thực hiện Liệt kê bằng ShellGPT

ShellGPT là một công cụ mạnh mẽ tận dụng trí tuệ nhân tạo, cụ thể là GPT-4, để hỗ trợ trong nhiều nhiệm vụ khác nhau, bao gồm việc liệt kê mạng cho kiểm thử xâm nhập. Bằng cách sử dụng ShellGPT, các hacker mũ trắng có thể tự động hóa quá trình liệt kê, thu thập phân tích dữ liệu sâu sắc và xác định các lỗ hổng tiềm ẩn hiệu quả hơn.

Ở đây, chúng ta sẽ sử dụng ShellGPT để thực hiện liệt kê trên địa chỉ IP mục tiêu.

Các lệnh được tạo ra bởi ShellGPT có thể thay đổi tùy thuộc vào prompt được sử dụng và các công cụ có sẵn trên máy. Do những biến số này, kết quả đầu ra được tạo ra bởi ShellGPT có thể khác với những gì được hiển thị trong các ảnh chụp màn hình. Sự khác biệt này xuất phát từ tính chất động của quá trình xử lý của AI và các môi trường đa dạng mà nó hoạt động. Do đó, bạn có thể quan sát thấy sự khác biệt về cú pháp lệnh, cách thực thi và kết quả khi thực hiện nhiệm vụ bài lab này.

1.  Trước khi bắt đầu bài lab này, nhấp vào Parrot Security để chuyển sang máy Parrot Security và tích hợp ShellGPT bằng cách làm theo các bước được cung cấp trong Integrate ShellGPT in Parrot Security Machine.pdf.[Parrot Security](https://labclient.labondemand.com/Instructions/691e8f3a-07ba-400e-abe8-95c40abefa3b)[Integrate ShellGPT in Parrot Security Machine.pdf](https://labondemand.blob.core.windows.net/content/lab168797/instructions267929/Integrate%20ShellGPT%20in%20Parrot%20%20Security%20Machine.pdf)

> Ngoài ra, bạn có thể làm theo các bước để tích hợp ShellGPT được cung cấp trong Mô-đun 00: Tích hợp ShellGPT trên Máy Parrot Security.

2.  Sau khi tích hợp API ShellGPT vào Parrot Security Machine, trong cửa sổ terminal, chạy lệnh sgpt \--shell \"Thực hiện liệt kê NetBIOS trên địa chỉ IP mục tiêu 10.10.1.11\" để thực hiện liệt kê NetBIOS trên hệ thống mục tiêu.

> Trong dấu nhắc, gõ E và nhấn Enter để thực thi lệnh.
>
> ![f1obz9k5.jpg](media/image48.jpeg){width="10.6625in" height="8.0in"}

3.  Chạy lệnh sgpt \--shell \"Lấy thông tin NetBIOS cho IP 10.10.1.11 và hiển thị các tên liên quan\" để xem các tên liên quan của hệ thống mục tiêu.

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image49.jpeg){width="10.6625in" height="8.0in"}

4.  Để thực hiện liệt kê NetBIOS bằng cách sử dụng Nmap, chạy lệnh sgpt \--shell \"Liệt kê NetBIOS trên địa chỉ IP mục tiêu 10.10.1.22 với nmap\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image50.jpeg){width="10.6625in" height="8.0in"}

5.  Chúng tôi sẽ thực hiện liệt kê SNMP bằng ShellGPT, để làm điều này, hãy chạy lệnh sgpt \--chat enum \--shell \"Thực hiện liệt kê SNMP trên địa chỉ IP mục tiêu 10.10.1.22 bằng SnmpWalk và hiển thị kết quả ở đây\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image51.jpeg){width="10.6625in" height="8.0in"}

6.  Chạy lệnh sgpt \--chat enum \--shell \"Thực hiện liệt kê SNMP trên IP mục tiêu 10.10.1.22 bằng cách sử dụng nmap và hiển thị kết quả ở đây\" để thực hiện liệt kê SNMP bằng Nmap.

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image52.jpeg){width="10.6625in" height="8.0in"}

7.  Chạy lệnh sgpt \--chat enum \--shell \"Thực hiện các tiến trình SNMP trên IP mục tiêu 10.10.1.22 bằng nmap và hiển thị kết quả ở đây\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image53.jpeg){width="10.6625in" height="8.0in"}

8.  Để thực hiện liệt kê SMTP trên IP mục tiêu, chạy lệnh sgpt \--chat enum \--shell \"Thực hiện liệt kê SMTP trên IP mục tiêu 10.10.1.19.\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image54.jpeg){width="10.6625in" height="8.0in"}

9.  Chúng tôi sẽ thực hiện liệt kê DNS với Nmap bằng ShellGPT, để làm điều đó hãy chạy lệnh sgpt \--chat enum \--shell \"Sử dụng Nmap để thực hiện liệt kê DNS trên tên miền mục tiêu www.certifiedhacker.com\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image55.jpeg){width="10.6625in" height="8.0in"}

10. Để thực hiện giám sát bộ nhớ đệm DNS trên miền mục tiêu, chạy lệnh sgpt \--chat enum \--shell \"Sử dụng lệnh dig để thực hiện giám sát bộ nhớ đệm DNS trên miền mục tiêu www.certifiedhacker.com bằng phương pháp đệ quy. Sử dụng IP máy chủ DNS là 162.241.216.11\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image56.jpeg){width="10.6625in" height="8.0in"}

11. Chạy lệnh sgpt \--chat enum \--shell \"Sử dụng lệnh dig để thực hiện việc dò tầm bộ nhớ đệm DNS trên tên miền mục tiêu www.certifiedhacker.com bằng phương pháp không đệ quy. Sử dụng IP máy chủ DNS là 162.241.216.11\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image57.jpeg){width="10.6625in" height="8.0in"}

12. Để thực hiện liệt kê IPsec bằng cách sử dụng ShellGPT, chạy lệnh sgpt \--shell \"Thực hiện liệt kê IPsec trên IP mục tiêu 10.10.1.22 với Nmap\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image58.jpeg){width="10.6625in" height="8.0in"}

13. Chúng tôi sẽ thực hiện việc liệt kê SMB bằng ShellGPT, để làm điều đó, hãy chạy lệnh sgpt \--shell \"Quét địa chỉ IP mục tiêu 10.10.1.22 cho cổng sử dụng SMB với Nmap\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image59.jpeg){width="10.6625in" height="8.0in"}

14. Để tạo và thực thi một kịch bản tùy chỉnh nhằm tự động hóa các tác vụ liệt kê mạng, chạy lệnh sgpt \--chat enum \--shell \"Phát triển và thực thi một kịch bản sẽ tự động hóa các tác vụ liệt kê mạng khác nhau trên phạm vi IP mục tiêu 10.10.1.0/24\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image60.jpeg){width="10.6625in" height="8.0in"}

15. Chúng tôi sẽ thực hiện liệt kê LDAP bằng cách sử dụng ShellGPT, để làm điều đó, hãy chạy lệnh sgpt \--shell \"Sử dụng script nmap để thực hiện ldap-brute-force trên IP 10.10.1.22\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image61.jpeg){width="10.6625in" height="8.0in"}

16. Để thực hiện liệt kê FTP, chạy lệnh sgpt \--shell \"Sử dụng Nmap để thực hiện liệt kê FTP trên www.certifiedhacker.com\".

> Trong dấu nhắc, gõ E và nhấn Enter để thực hiện lệnh.
>
> ![Screenshot](media/image62.jpeg){width="10.6625in" height="8.0in"}

17. Kết quả hiển thị các cổng mở hiện có trên trang web, bạn có thể thấy rằng cổng 21, nơi dịch vụ FTP đang chạy, đang mở.

18. Ngoài các lệnh đã đề cập, bạn có thể khám phá thêm các tùy chọn bổ sung trong công cụ ShellGPT và sử dụng nhiều công cụ khác để tiến hành liệt kê trên mục tiêu.

19. Điều này kết thúc phần trình bày về cách thực hiện liệt kê bằng ShellGPT.

20. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 4.8.1.1**

Trên máy Parrot Security, viết một lệnh ShellGPT và thực thi nó để thực hiện liệt kê SMB trên máy Windows Server 2022 (10.10.1.22), xác định dịch vụ đang chạy trên cổng 445 trên máy Windows Server 2022.

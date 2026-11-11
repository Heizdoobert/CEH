Mô-đun 05: Phân tích lỗ hổng

Kịch bản

Trước đó, tất cả thông tin có thể về một hệ thống mục tiêu như tên hệ thống, chi tiết hệ điều hành, tài nguyên mạng được chia sẻ, chính sách và chi tiết mật khẩu, cũng như người dùng và nhóm người dùng đã được thu thập.

Bây giờ, là một hacker đạo đức hoặc chuyên gia kiểm thử xâm nhập (sau đây gọi là pen tester), bước tiếp theo của bạn là thực hiện nghiên cứu lỗ hổng và đánh giá lỗ hổng trên hệ thống hoặc mạng mục tiêu. Hacker đạo đức hoặc pen tester cần tiến hành nghiên cứu kỹ lưỡng với sự trợ giúp của thông tin thu thập được trong các giai đoạn footprinting và scanning để phát hiện lỗ hổng.

Đánh giá lỗ hổng quét mạng để tìm các điểm yếu an ninh đã biết: nó nhận diện, đo lường và phân loại các lỗ hổng an ninh trong hệ thống máy tính, mạng và kênh truyền thông; và đánh giá các hệ thống mục tiêu để tìm các lỗ hổng như bản vá thiếu, dịch vụ không cần thiết, xác thực yếu và mã hóa yếu. Ngoài ra, nó hỗ trợ các chuyên gia bảo mật trong việc bảo vệ mạng bằng cách xác định các kẽ hở hoặc lỗ hổng trong cơ chế bảo mật hiện tại trước khi kẻ tấn công khai thác chúng.

Thông tin thu thập được từ đánh giá lỗ hổng giúp bạn xác định các điểm yếu có thể bị khai thác và dự đoán hiệu quả của các biện pháp bảo mật bổ sung trong việc bảo vệ tài nguyên thông tin khỏi các cuộc tấn công.

Các bài lab trong mô-đun này sẽ mang đến cho bạn trải nghiệm trực tiếp trong việc thu thập thông tin về các điểm yếu tiềm ẩn trong hệ thống mục tiêu bằng cách sử dụng các nguồn trực tuyến khác nhau và các công cụ đánh giá lỗ hổng.

Mục tiêu

Mục tiêu của bài lab này là trích xuất thông tin về hệ thống mục tiêu bao gồm, nhưng không giới hạn ở:

-   Lỗ hổng mạng

-   Các cổng và dịch vụ Giao thức Kiểm soát Truyền vận/Giao thức Gói Tin Người dùng (TCP/UDP) đang lắng nghe

-   Lỗi/lỗ hổng cấu hình ứng dụng và dịch vụ

-   Phiên bản hệ điều hành đang chạy trên máy tính hoặc thiết bị

-   Các ứng dụng được cài đặt trên máy tính

-   Tài khoản có mật khẩu yếu

-   Các tệp và thư mục có quyền hạn yếu

-   Các dịch vụ và ứng dụng mặc định có thể sẽ phải gỡ cài đặt

-   Những sai lầm trong cấu hình bảo mật của các ứng dụng phổ biến

-   Máy tính bị phơi bày trước các lỗ hổng đã biết hoặc được báo cáo công khai

Tổng quan về đánh giá lỗ hổng

Một lỗ hổng đề cập đến một điểm yếu trong thiết kế hoặc triển khai của một hệ thống có thể bị lợi dụng để xâm phạm bảo mật của hệ thống. Nó thường là một sơ hở bảo mật cho phép kẻ tấn công xâm nhập hệ thống bằng cách vượt qua xác thực người dùng. Thông thường có hai nguyên nhân chính dẫn đến hệ thống dễ bị tấn công trong mạng, là cấu hình sai phần mềm hoặc phần cứng và thực tiễn lập trình kém. Kẻ tấn công khai thác các lỗ hổng này để thực hiện các loại tấn công khác nhau vào tài nguyên của tổ chức.

Nhiệm vụ bài lab

Những hacker đạo đức hoặc chuyên gia kiểm thử xâm nhập sử dụng nhiều công cụ và kỹ thuật để thu thập thông tin về các lỗ hổng tiềm ẩn trong hệ thống hoặc mạng mục tiêu. Các bài lab được khuyến nghị sẽ hỗ trợ bạn học các kỹ thuật đánh giá lỗ hổng khác nhau bao gồm:

1.  Thực hiện nghiên cứu lỗ hổng với các hệ thống và cơ sở dữ liệu chấm điểm lỗ hổng

    -   Tiến hành nghiên cứu lỗ hổng trong Danh mục Yếu điểm Chung (CWE)

2.  Thực hiện đánh giá lỗ hổng bằng cách sử dụng các công cụ đánh giá lỗ hổng khác nhau

    -   Thực hiện phân tích lỗ hổng sử dụng OpenVAS

3.  Thực hiện phân tích lỗ hổng sử dụng AI

    -   Thực hiện phân tích lỗ hổng sử dụng ShellGPT

TrướcTiếp

bài lab 1: Thực hiện nghiên cứu lỗ hổng với các hệ thống và cơ sở dữ liệu đánh giá lỗ hổng

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc kiểm thử thâm nhập, bước đầu tiên của bạn là tìm kiếm các lỗ hổng trong hệ thống hoặc mạng mục tiêu bằng cách sử dụng các hệ thống và cơ sở dữ liệu đánh giá lỗ hổng. Nghiên cứu lỗ hổng cung cấp nhận thức về các kỹ thuật tiên tiến để xác định sai sót hoặc kẽ hở trong phần mềm có thể bị khai thác. Sử dụng thông tin này, bạn có thể áp dụng nhiều mánh khóe và kỹ thuật khác nhau để thực hiện các cuộc tấn công vào hệ thống mục tiêu.

**Mục tiêu bài lab**

-   Tiến hành nghiên cứu lỗ hổng trong Danh mục Yếu điểm Chung (CWE)

**Tổng quan về các lỗ hổng trong Hệ thống và Cơ sở dữ liệu Xếp hạng Lỗ hổng**

Các cơ sở dữ liệu về lỗ hổng bảo mật thu thập và duy trì thông tin về các lỗ hổng khác nhau có trong các hệ thống thông tin.

Dưới đây là một số hệ thống chấm điểm lỗ hổng và cơ sở dữ liệu:

-   Danh mục các điểm yếu phổ biến (CWE)

-   Các Lỗ Hổng và Phơi Bày Thường Gặp (CVE)

-   Cơ sở dữ liệu lỗ hổng quốc gia (NVD)

Nhiệm vụ 1: Thực hiện Nghiên cứu Lỗ hổng trong Danh mục Yếu điểm Thường gặp (CWE)

Liệt kê Các Điểm Yếu Thường Gặp (CWE) là một hệ thống phân loại các lỗ hổng và điểm yếu phần mềm. Nó có nhiều danh mục điểm yếu, điều đó có nghĩa là CWE có thể được cộng đồng sử dụng hiệu quả như một cơ sở để xác định, giảm thiểu và ngăn ngừa điểm yếu. Hơn nữa, CWE có một kỹ thuật tìm kiếm tiên tiến với đó bạn có thể tìm kiếm và xem các điểm yếu dựa trên các khái niệm nghiên cứu, khái niệm phát triển và khái niệm kiến trúc.

Ở đây, chúng tôi sẽ sử dụng CWE để xem các lỗ hổng hệ thống cơ bản mới nhất.

1.  Theo mặc định, máy Windows 11 được chọn, nhấn Ctrl+Alt+Delete để kích hoạt máy và đăng nhập bằng Admin/Pa\$\$w0rd.[Ctrl+Alt+Delete](https://labclient.labondemand.com/Instructions/cb8b499d-5398-4b4e-9f84-ab80e90ebde4)

> Màn hình Mạng xuất hiện, nhấp vào Có để cho phép PC của bạn có thể được các PC và thiết bị khác trên mạng phát hiện.

2.  Mở bất kỳ trình duyệt web nào và truy cập vào trang web https://cwe.mitre.org/ (ở đây, chúng tôi đang sử dụng Mozilla Firefox).

> Nếu cửa sổ pop-up Trình duyệt Mặc định xuất hiện, hãy bỏ chọn hộp kiểm Luôn thực hiện kiểm tra này khi khởi động Firefox và nhấp vào nút Không phải bây giờ.
>
> Nếu một cửa sổ pop-up Mới trong Firefox: Chặn Nội dung xuất hiện, hãy làm theo các bước và nhấp vào bắt đầu duyệt để hoàn tất việc xem thông tin.

3.  Trang web CWE xuất hiện. Điều hướng đến tab Tìm kiếm, trong Tìm kiếm Tùy chỉnh của Google dưới phần Truy cập Nhanh Danh sách CWE và tìm kiếm SMB trong trường tìm kiếm.

> Ở đây, chúng tôi đang tìm kiếm các lỗ hổng của các dịch vụ đang chạy đã được phát hiện trong các hệ thống mục tiêu ở các bài lab mô-đun trước đó (Mô-đun 04 Liệt kê).
>
> ![Screenshot](media/image2.jpeg){width="6.715990813648294in" height="5.0389610673665794in"}

4.  Kết quả tìm kiếm xuất hiện, cuộn xuống để xem các lỗ hổng cơ bản trong dịch vụ mục tiêu (ở đây là SMB). Bạn có thể nhấp vào bất kỳ liên kết nào để xem thông tin chi tiết về lỗ hổng.

> Kết quả tìm kiếm có thể khác nhau khi bạn thực hiện nhiệm vụ này
>
> ![Screenshot](media/image3.jpeg){width="6.9735881452318464in" height="5.2322353455818025in"}

5.  Bây giờ, hãy nhấp vào bất kỳ liên kết nào (ở đây, CWE-284) để xem thông tin chi tiết về lỗ hổng bảo mật.

> ![Screenshot](media/image4.jpeg){width="6.911480752405949in" height="5.185636482939633in"}

6.  Tương tự, bạn có thể nhấp vào các lỗ hổng khác và xem thông tin chi tiết.

7.  Bây giờ, điều hướng đến tab Danh sách CWE. Phiên bản Danh sách CWE sẽ được hiển thị. Cuộn xuống, và dưới mục Bản đồ ngoại vi, chọn CWE Top 25 (2023).

> Kết quả có thể khác nhau khi bạn thực hiện nhiệm vụ này.
>
> ![Screenshot](media/image5.jpeg){width="7.800216535433071in" height="5.852448600174978in"}

8.  Một trang web xuất hiện, hiển thị CWE VIEW: Những điểm yếu trong 25 điểm yếu phần mềm nguy hiểm nhất của CWE năm 2023. Kéo xuống và xem danh sách các điểm yếu trong 25 điểm yếu phần mềm nguy hiểm nhất của CWE năm 2023 dưới mục Relationships. Bạn có thể kiểm tra từng điểm yếu để xem thông tin chi tiết về nó.

> Thông tin này có thể được sử dụng để khai thác các lỗ hổng trong phần mềm và tiến hành các cuộc tấn công thêm.
>
> Kết quả hiển thị năm xuất bản có thể khác khi bạn thực hiện nhiệm vụ này.
>
> ![Screenshot](media/image6.jpeg){width="10.6625in" height="8.0in"}

9.  Tương tự, bạn cũng có thể quay lại trang web CWE và khám phá các tùy chọn khác.

10. Kẻ tấn công có thể tìm thấy các lỗ hổng trên các dịch vụ đang chạy trên hệ thống mục tiêu và khai thác chúng để tiến hành các cuộc tấn công.

11. Điều này kết thúc phần trình diễn kiểm tra các lỗ hổng trong Danh mục Phân loại Lỗi Thường Gặp (CWE).

12. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 5.1.1.1**

Tìm kiếm danh sách Các Lỗi Phổ Biến (CWE) và tìm tên của lỗ hổng với ID CWE 591.

![](media/image7.wmf)

**Câu hỏi 5.1.1.2**

Tìm kiếm danh sách Liệt kê Các Lỗ Hổng Thường Gặp (CWE) và tìm lỗ hổng hàng đầu trong danh sách "Các Lỗ Hổng Trong 25 Lỗi Phần Mềm Nguy Hiểm Nhất CWE 2023."

![](media/image7.wmf)

TrướcTiếp

Thí nghiệm 2: Thực hiện Đánh giá Lỗ hổng Bảo mật bằng cách sử dụng Các Công cụ Đánh giá Lỗ hổng khác nhau

**kịch bản bài lab bài lab**

Thông tin thu thập được trong các bài lab trước có thể không đủ để tiết lộ các lỗ hổng tiềm ẩn của mục tiêu: có thể có nhiều thông tin hơn có sẵn mà có thể giúp tìm ra các sơ hở. Là một hacker đạo đức, bạn nên tìm kiếm càng nhiều thông tin càng tốt bằng cách sử dụng tất cả các công cụ có sẵn. bài lab này sẽ trình bày các thông tin khác mà bạn có thể trích xuất từ mục tiêu bằng cách sử dụng các công cụ đánh giá lỗ hổng khác nhau.

**Mục tiêu bài lab**

-   Thực hiện phân tích lỗ hổng sử dụng OpenVAS

**Tổng quan về đánh giá lỗ hổng**

Đánh giá lỗ hổng là một cuộc kiểm tra chi tiết về khả năng của một hệ thống hoặc ứng dụng, bao gồm các quy trình và kiểm soát bảo mật hiện tại, để chống lại các mối đe dọa khai thác. Nó quét các mạng để tìm các điểm yếu bảo mật đã biết, và nhận diện, đo lường và phân loại các lỗ hổng bảo mật trong hệ thống máy tính, mạng và kênh truyền thông. Nó xác định, định lượng và xếp hạng các lỗ hổng có thể gặp phải trước các mối đe dọa trong hệ thống. Ngoài ra, nó hỗ trợ các chuyên gia bảo mật trong việc bảo vệ mạng bằng cách xác định các lỗ hổng hoặc điểm yếu trong cơ chế bảo mật hiện tại trước khi kẻ tấn công khai thác chúng.

Có hai phương pháp để quét lỗ hổng mạng:

-   Quét chủ động

-   Quét thụ động

Nhiệm vụ 1: Thực hiện Phân tích Lỗ hổng bằng OpenVAS

OpenVAS là một khuôn khổ của nhiều dịch vụ và công cụ cung cấp một giải pháp quét lỗ hổng và quản lý lỗ hổng toàn diện và mạnh mẽ. Khả năng của nó bao gồm kiểm tra không xác thực, kiểm tra xác thực, nhiều giao thức Internet và công nghiệp cấp cao và cấp thấp khác nhau, tinh chỉnh hiệu suất cho quét quy mô lớn, và một ngôn ngữ lập trình nội bộ mạnh mẽ để triển khai bất kỳ bài kiểm tra lỗ hổng nào. Trình quét bảo mật thực tế đi kèm với một nguồn dữ liệu được cập nhật thường xuyên các Bài Kiểm Tra Lỗ Hổng Mạng (NVTs) - tổng cộng hơn 50.000.

Ở đây, chúng tôi sẽ thực hiện phân tích lỗ hổng bằng cách sử dụng OpenVAS.

Trong nhiệm vụ này, chúng ta sẽ sử dụng máy Parrot Security (10.10.1.13) làm máy chủ và máy Windows Server 2022 (10.10.1.22) làm máy mục tiêu.

1.  Nhấp vào Parrot Security để chuyển sang máy Parrot Security và đăng nhập với attacker/toor.[Parrot Security](https://labclient.labondemand.com/Instructions/cb8b499d-5398-4b4e-9f84-ab80e90ebde4)

> Nếu một cửa sổ bật lên Parrot Updater xuất hiện ở góc trên bên phải của Màn hình, hãy bỏ qua và đóng nó.
>
> Nếu một cửa sổ bật lên Hỏi xuất hiện yêu cầu bạn cập nhật máy, hãy nhấp vào Không để đóng cửa sổ.

2.  Mở một cửa sổ Terminal và thực thi sudo su để chạy các chương trình với quyền người dùng root (Khi được yêu cầu, nhập mật khẩu toor).

> Mật khẩu mà bạn nhập sẽ không hiển thị.

3.  Chạy lệnh docker run -d -p 443:443 \--name openvas mikesplain/openvas để khởi chạy OpenVAS.

4.  Sau khi công cụ khởi tạo, nhấp vào biểu tượng Firefox ở phần trên của Màn hình chính.

5.  Trình duyệt Firefox xuất hiện, truy cập https://127.0.0.1/. Trang đăng nhập OpenVAS xuất hiện, đăng nhập với admin/admin.

> Nếu một trang Cảnh báo xuất hiện, nhấp vào Nâng cao và chọn Chấp nhận Rủi ro và Tiếp tục.
>
> ![Screenshot](media/image8.jpeg){width="10.6625in" height="8.0in"}

6.  Bảng điều khiển OpenVAS xuất hiện. Điều hướng tới Quét \--\> Nhiệm vụ từ thanh Menu.

> Nếu xuất hiện một cửa sổ bật lên chào mừng đến với quản lý tác vụ quét, hãy đóng nó lại.
>
> ![Screenshot](media/image9.jpeg){width="10.6625in" height="8.0in"}

7.  Di chuột qua biểu tượng đũa và nhấp vào tùy chọn Trình thuật sĩ tác vụ.

> ![Screenshot](media/image10.jpeg){width="10.6625in" height="8.0in"}

8.  Cửa sổ Trình hướng dẫn tác vụ xuất hiện; nhập địa chỉ IP đích vào trường địa chỉ IP hoặc tên máy chủ (ở đây, hệ thống đích là Windows Server 2022 \[10.10.1.22\]) và nhấn nút Bắt đầu quét.

> ![Screenshot](media/image11.jpeg){width="10.6625in" height="8.0in"}

9.  Nhiệm vụ xuất hiện trong mục Nhiệm vụ; OpenVAS bắt đầu quét địa chỉ IP mục tiêu.

10. Chờ trạng thái chuyển từ Đã yêu cầu sang Hoàn thành. Khi quá trình hoàn tất, nhấp vào nút Hoàn thành dưới cột Trạng thái để xem các lỗ hổng đã tìm thấy trong hệ thống mục tiêu.

> Quét mất khoảng 20 phút để hoàn tất.
>
> Nếu bạn đã đăng xuất khỏi phiên, hãy đăng nhập lại bằng thông tin đăng nhập admin/admin.
>
> ![Screenshot](media/image12.jpeg){width="10.6625in" height="8.0in"}

11. Báo cáo: Kết quả xuất hiện, hiển thị các lỗ hổng đã phát hiện cùng với mức độ nghiêm trọng và số cổng mà chúng đang chạy.

> Kết quả có thể khác nhau khi bạn thực hiện nhiệm vụ này.
>
> ![open1.jpg](media/image13.jpeg){width="10.6625in" height="8.0in"}

12. Nhấp vào bất kỳ lỗ hổng nào trong cột Lỗ hổng để xem thông tin chi tiết của nó.

13. Thông tin chi tiết về lỗ hổng được chọn xuất hiện, như hiển thị trong ảnh chụp màn hình.

> ![open4.jpg](media/image14.jpeg){width="10.6625in" height="8.0in"}

14. Tương tự, bạn có thể kiểm tra các Báo cáo khác bằng cách di chuột qua phần Báo cáo: Kết quả để xem các Báo cáo khác liên quan đến các lỗ hổng trong hệ thống mục tiêu.

15. Tiếp theo, hãy xem xét các phát hiện, bao gồm tất cả các lỗ hổng cao hoặc nghiêm trọng. Sử dụng kỹ năng của bạn một cách thủ công để xác minh lỗ hổng. Thách thức với các trình quét lỗ hổng là chúng khá hạn chế; chúng chỉ hoạt động tốt cho một bài kiểm tra nội bộ hoặc kiểm tra hộp trắng nếu thông tin đăng nhập được biết. Chúng ta sẽ khám phá điều đó ngay bây giờ: quay lại công cụ OpenVAS của bạn, và thiết lập để quét cùng một lần nữa; nhưng lần này, hãy bật tường lửa trên máy Windows Server 2022.

16. Bây giờ, chúng ta sẽ bật Tường lửa Windows trên hệ thống mục tiêu và quét nó để tìm các lỗ hổng bảo mật.

17. Nhấp vào Windows Server 2022 để chuyển sang máy Windows Server 2022 và nhấn Ctrl+Alt+Delete rồi đăng nhập bằng CEH\\Administrator / Pa\$\$w0rd.[Windows Server 2022Ctrl+Alt+Delete](https://labclient.labondemand.com/Instructions/cb8b499d-5398-4b4e-9f84-ab80e90ebde4)

18. Đi tới Bảng điều khiển \--\> Hệ thống và Bảo mật \--\> Tường lửa Windows Defender \--\> Bật hoặc tắt Tường lửa Windows Defender, kích hoạt Tường lửa Windows và nhấn OK.

> Bằng cách bật Tường lửa, bạn đang làm cho công cụ quét khó quét các lỗ hổng trong hệ thống mục tiêu hơn.
>
> ![Screenshot](media/image15.jpeg){width="10.6625in" height="8.0in"}

19. Nhấp vào Parrot Security để chuyển sang máy Parrot Security và thực hiện Các bước #7-9 để tạo một nhiệm vụ khác để quét hệ thống mục tiêu.[Parrot Security](https://labclient.labondemand.com/Instructions/cb8b499d-5398-4b4e-9f84-ab80e90ebde4)

20. Một tác vụ mới được tạo xuất hiện dưới mục Tasks và bắt đầu quét hệ thống mục tiêu để tìm các lỗ hổng.

21. Sau khi quét xong, nhấp vào nút Xong dưới cột Trạng thái.

> Quét mất khoảng 15-20 phút để hoàn thành.

22. Báo cáo: Kết quả xuất hiện, hiển thị các lỗ hổng được phát hiện cùng với mức độ nghiêm trọng và số cổng mà chúng đang chạy.

> Kết quả có thể khác nhau khi bạn thực hiện nhiệm vụ này.
>
> ![open3.jpg](media/image16.jpeg){width="10.6625in" height="8.0in"}

23. Kết quả quét cho máy mục tiêu trước và sau khi Windows Firewall được bật là giống nhau, do đó chỉ ra rằng hệ thống mục tiêu vẫn dễ bị tấn công ngay cả khi Firewall được bật.

24. Điều này kết thúc buổi trình diễn phân tích lỗ hổng bảo mật sử dụng OpenVAS.

25. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

26. Nhấp vào Windows Server 2022 để chuyển sang máy Windows Server 2022 và nhấp Ctrl+Alt+Delete để đăng nhập với Administrator/Pa\$\$w0rd.[Windows Server 2022Ctrl+Alt+Delete](https://labclient.labondemand.com/Instructions/cb8b499d-5398-4b4e-9f84-ab80e90ebde4)

27. Đi đến Bảng điều khiển \--\> Hệ thống và Bảo mật \--\> Tường lửa Windows Defender \--\> Bật hoặc tắt Tường lửa Windows Defender, vô hiệu hóa Tường lửa Windows và nhấn OK.

**Câu hỏi 5.2.1.1**

Thực hiện phân tích lỗ hổng cho máy mục tiêu (10.10.1.22) sử dụng OpenVAS và tìm số lượng lỗ hổng trong hệ thống. Nhập mức độ nghiêm trọng của lỗ hổng Báo cáo Enumeration DCE/RPC và MSRPC Services.

![](media/image7.wmf)

TrướcTiếp

bài lab 3: Thực hiện Phân tích Lỗ hổng bằng AI

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc người kiểm thử xâm nhập, bạn phải thừa nhận những hạn chế của các phương pháp thông thường trong việc tiết lộ tất cả các lỗ hổng tiềm ẩn. Do đó, bạn sẽ sử dụng các công cụ phân tích lỗ hổng dựa trên AI để xác định và đánh giá các điểm yếu bảo mật trong một môi trường mạng mô phỏng.

**Mục tiêu bài lab**

-   Thực hiện phân tích lỗ hổng sử dụng ShellGPT

**Tổng quan về phân tích lỗ hổng sử dụng AI**

Phân tích lỗ hổng với AI sử dụng các thuật toán tiên tiến để khám phá các lỗi bảo mật ẩn trong mạng. Các công cụ dựa trên AI trích xuất dữ liệu toàn diện, ưu tiên các rủi ro và tăng cường phòng thủ, giúp các hacker đạo đức dự đoán và giảm thiểu các mối đe dọa mới một cách hiệu quả. Cách tiếp cận đổi mới này nâng cao khả năng sẵn sàng về an ninh mạng bằng cách tận dụng độ chính xác và khả năng thích ứng của AI.

Nhiệm vụ 1: Thực hiện Phân tích Lỗ hổng bằng ShellGPT

ShellGPT nhanh chóng giải thích và thực hiện các lệnh, tiến hành quét, xác định các điểm yếu và đề xuất các chiến lược giảm thiểu trong thời gian thực. Bản chất thích ứng của nó tạo điều kiện cho việc điều hướng năng động qua các hệ thống phức tạp, tăng cường hiệu quả và độ chính xác trong phân tích lỗ hổng. Bằng cách tích hợp ShellGPT, bạn có thể có được một đồng minh mạnh mẽ trong việc bảo vệ các hệ sinh thái kỹ thuật số, tận dụng khả năng của AI để phát hiện và xử lý các rủi ro bảo mật với tốc độ và độ chính xác chưa từng có.

Ở đây, chúng ta sẽ sử dụng ShellGPT để phát hiện các lỗ hổng tiềm ẩn trong mục tiêu.

Các lệnh được tạo ra bởi ShellGPT có thể thay đổi tùy thuộc vào prompt được sử dụng và các công cụ có sẵn trên máy. Do những biến số này, kết quả đầu ra được tạo ra bởi ShellGPT có thể khác với những gì được hiển thị trong các ảnh chụp màn hình. Sự khác biệt này xuất phát từ tính chất động của quá trình xử lý của AI và các môi trường đa dạng mà nó hoạt động. Do đó, bạn có thể quan sát thấy sự khác biệt về cú pháp lệnh, cách thực thi và kết quả khi thực hiện nhiệm vụ bài lab này.

1.  Trước khi bắt đầu bài lab này, nhấp vào Parrot Security để chuyển sang máy Parrot Security và tích hợp ShellGPT bằng cách làm theo các bước được cung cấp trong Integrate ShellGPT in Parrot Security Machine.pdf.[Parrot Security](https://labclient.labondemand.com/Instructions/cb8b499d-5398-4b4e-9f84-ab80e90ebde4)[Integrate ShellGPT in Parrot Security Machine.pdf](https://labondemand.blob.core.windows.net/content/lab168798/instructions267929/Integrate%20ShellGPT%20in%20Parrot%20%20Security%20Machine.pdf)

> Ngoài ra, bạn có thể làm theo các bước để tích hợp ShellGPT được cung cấp trong Mô-đun 00: Tích hợp ShellGPT trên Máy Parrot Security.

2.  Sau khi tích hợp API ShellGPT vào Parrot Security Machine, trong cửa sổ terminal, chạy sgpt \--chat nikto \--shell \"Quét URL https://www.certifiedhacker.com để xác định các lỗ hổng tiềm ẩn với nikto\" để khởi động quá trình quét Nikto trên trang web mục tiêu.

> Trong dấu nhắc lệnh, gõ E và nhấn Enter để thực thi lệnh.
>
> ![Screenshot](media/image17.jpeg){width="10.6625in" height="8.0in"}

3.  Kết quả quét hiển thị các lỗ hổng đã phát hiện trên trang web mục tiêu (tại đây, www.certifiedhacker.com), như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image18.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image19.jpeg){width="10.6625in" height="8.0in"}
>
> Việc quét Nikto mất nhiều thời gian để hoàn thành. Bạn có thể kết thúc việc quét bằng cách nhấn Ctrl + Z.

4.  Trong terminal, chạy lệnh sgpt \--chat vuln \--shell \"Thực hiện quét lỗ hổng trên URL mục tiêu http://www.moviescope.com bằng Nmap\" để thực hiện quét lỗ hổng trên website mục tiêu. Kết quả sẽ hiển thị các cổng mở và các dịch vụ đang chạy trên website mục tiêu.

> ![Screenshot](media/image20.jpeg){width="10.6625in" height="8.0in"}

5.  Chạy sgpt \--chat vuln \--shell \"Thực hiện quét lỗ hổng trên URL mục tiêu http://testphp.vulnweb.com với skipfish\" để quét URL mục tiêu bằng công cụ skipfish.

> Nếu một thông báo xuất hiện, hãy nhấn bất kỳ phím nào để tiếp tục quá trình quét.
>
> ![Screenshot](media/image21.jpeg){width="10.6625in" height="8.0in"}

6.  Skipfish bắt đầu quét URL mục tiêu. Sau khi quá trình quét hoàn tất thành công, báo cáo được lưu tại vị trí /tmp/skipfish_scan_output/, với tên là index.html. Điều hướng đến vị trí này, nhấn chuột phải vào index.html và mở bằng trình duyệt web Firefox ESR, như được hiển thị trong ảnh chụp màn hình.

> Vị trí của báo cáo quét có thể khác nhau. Bạn có thể xem vị trí trong lệnh skipfish được ShellGPT tạo ra.
>
> ![Screenshot](media/image22.jpeg){width="10.6625in" height="8.0in"}

7.  Cửa sổ trình duyệt Firefox xuất hiện hiển thị báo cáo quét đầy đủ, như được thể hiện trong ảnh chụp màn hình.

> ![Screenshot](media/image23.jpeg){width="10.6625in" height="8.0in"}

8.  Ngoài các lệnh đã đề cập, bạn có thể khám phá thêm các tùy chọn khác trong công cụ ShellGPT và sử dụng nhiều công cụ khác để tiến hành đánh giá lỗ hổng trên mục tiêu.

9.  Điều này kết thúc buổi trình diễn về việc thực hiện đánh giá lỗ hổng trên hệ thống mục tiêu bằng ShellGPT.

10. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 5.3.1.1**

Viết một lệnh nhắc sử dụng ShellGPT để thực hiện quét lỗ hổng trên trang web www.certifiedhacker.com bằng trình quét lỗ hổng Nikto. Nhập nội dung của tiêu đề không phổ biến \'host header\' được tìm thấy trong quá trình quét lỗ hổng.

![](media/image7.wmf)

TrướcTiếp

bài lab 3: Thực hiện Phân tích Lỗ hổng bằng AI

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc người kiểm thử xâm nhập, bạn phải thừa nhận những hạn chế của các phương pháp thông thường trong việc tiết lộ tất cả các lỗ hổng tiềm ẩn. Do đó, bạn sẽ sử dụng các công cụ phân tích lỗ hổng dựa trên AI để xác định và đánh giá các điểm yếu bảo mật trong một môi trường mạng mô phỏng.

**Mục tiêu bài lab**

-   Thực hiện phân tích lỗ hổng sử dụng ShellGPT

**Tổng quan về phân tích lỗ hổng sử dụng AI**

Phân tích lỗ hổng với AI sử dụng các thuật toán tiên tiến để khám phá các lỗi bảo mật ẩn trong mạng. Các công cụ dựa trên AI trích xuất dữ liệu toàn diện, ưu tiên các rủi ro và tăng cường phòng thủ, giúp các hacker đạo đức dự đoán và giảm thiểu các mối đe dọa mới một cách hiệu quả. Cách tiếp cận đổi mới này nâng cao khả năng sẵn sàng về an ninh mạng bằng cách tận dụng độ chính xác và khả năng thích ứng của AI.

Nhiệm vụ 1: Thực hiện Phân tích Lỗ hổng bằng ShellGPT

ShellGPT nhanh chóng giải thích và thực hiện các lệnh, tiến hành quét, xác định các điểm yếu và đề xuất các chiến lược giảm thiểu trong thời gian thực. Bản chất thích ứng của nó tạo điều kiện cho việc điều hướng năng động qua các hệ thống phức tạp, tăng cường hiệu quả và độ chính xác trong phân tích lỗ hổng. Bằng cách tích hợp ShellGPT, bạn có thể có được một đồng minh mạnh mẽ trong việc bảo vệ các hệ sinh thái kỹ thuật số, tận dụng khả năng của AI để phát hiện và xử lý các rủi ro bảo mật với tốc độ và độ chính xác chưa từng có.

Ở đây, chúng ta sẽ sử dụng ShellGPT để phát hiện các lỗ hổng tiềm ẩn trong mục tiêu.

Các lệnh được tạo ra bởi ShellGPT có thể thay đổi tùy thuộc vào prompt được sử dụng và các công cụ có sẵn trên máy. Do những biến số này, kết quả đầu ra được tạo ra bởi ShellGPT có thể khác với những gì được hiển thị trong các ảnh chụp màn hình. Sự khác biệt này xuất phát từ tính chất động của quá trình xử lý của AI và các môi trường đa dạng mà nó hoạt động. Do đó, bạn có thể quan sát thấy sự khác biệt về cú pháp lệnh, cách thực thi và kết quả khi thực hiện nhiệm vụ bài lab này.

1.  Trước khi bắt đầu bài lab này, nhấp vào Parrot Security để chuyển sang máy Parrot Security và tích hợp ShellGPT bằng cách làm theo các bước được cung cấp trong Integrate ShellGPT in Parrot Security Machine.pdf.[Parrot Security](https://labclient.labondemand.com/Instructions/cb8b499d-5398-4b4e-9f84-ab80e90ebde4)[Integrate ShellGPT in Parrot Security Machine.pdf](https://labondemand.blob.core.windows.net/content/lab168798/instructions267929/Integrate%20ShellGPT%20in%20Parrot%20%20Security%20Machine.pdf)

> Ngoài ra, bạn có thể làm theo các bước để tích hợp ShellGPT được cung cấp trong Mô-đun 00: Tích hợp ShellGPT trên Máy Parrot Security.

2.  Sau khi tích hợp API ShellGPT vào Parrot Security Machine, trong cửa sổ terminal, chạy sgpt \--chat nikto \--shell \"Quét URL https://www.certifiedhacker.com để xác định các lỗ hổng tiềm ẩn với nikto\" để khởi động quá trình quét Nikto trên trang web mục tiêu.

> Trong dấu nhắc lệnh, gõ E và nhấn Enter để thực thi lệnh.
>
> ![Screenshot](media/image17.jpeg){width="10.6625in" height="8.0in"}

3.  Kết quả quét hiển thị các lỗ hổng đã phát hiện trên trang web mục tiêu (tại đây, www.certifiedhacker.com), như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image18.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image19.jpeg){width="10.6625in" height="8.0in"}
>
> Việc quét Nikto mất nhiều thời gian để hoàn thành. Bạn có thể kết thúc việc quét bằng cách nhấn Ctrl + Z.

4.  Trong terminal, chạy lệnh sgpt \--chat vuln \--shell \"Thực hiện quét lỗ hổng trên URL mục tiêu http://www.moviescope.com bằng Nmap\" để thực hiện quét lỗ hổng trên website mục tiêu. Kết quả sẽ hiển thị các cổng mở và các dịch vụ đang chạy trên website mục tiêu.

> ![Screenshot](media/image20.jpeg){width="10.6625in" height="8.0in"}

5.  Chạy sgpt \--chat vuln \--shell \"Thực hiện quét lỗ hổng trên URL mục tiêu http://testphp.vulnweb.com với skipfish\" để quét URL mục tiêu bằng công cụ skipfish.

> Nếu một thông báo xuất hiện, hãy nhấn bất kỳ phím nào để tiếp tục quá trình quét.
>
> ![Screenshot](media/image21.jpeg){width="10.6625in" height="8.0in"}

6.  Skipfish bắt đầu quét URL mục tiêu. Sau khi quá trình quét hoàn tất thành công, báo cáo được lưu tại vị trí /tmp/skipfish_scan_output/, với tên là index.html. Điều hướng đến vị trí này, nhấn chuột phải vào index.html và mở bằng trình duyệt web Firefox ESR, như được hiển thị trong ảnh chụp màn hình.

> Vị trí của báo cáo quét có thể khác nhau. Bạn có thể xem vị trí trong lệnh skipfish được ShellGPT tạo ra.
>
> ![Screenshot](media/image22.jpeg){width="10.6625in" height="8.0in"}

7.  Cửa sổ trình duyệt Firefox xuất hiện hiển thị báo cáo quét đầy đủ, như được thể hiện trong ảnh chụp màn hình.

> ![Screenshot](media/image23.jpeg){width="10.6625in" height="8.0in"}

8.  Ngoài các lệnh đã đề cập, bạn có thể khám phá thêm các tùy chọn khác trong công cụ ShellGPT và sử dụng nhiều công cụ khác để tiến hành đánh giá lỗ hổng trên mục tiêu.

9.  Điều này kết thúc buổi trình diễn về việc thực hiện đánh giá lỗ hổng trên hệ thống mục tiêu bằng ShellGPT.

10. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 5.3.1.1**

Viết một lệnh nhắc sử dụng ShellGPT để thực hiện quét lỗ hổng trên trang web www.certifiedhacker.com bằng trình quét lỗ hổng Nikto. Nhập nội dung của tiêu đề không phổ biến \'host header\' được tìm thấy trong quá trình quét lỗ hổng.

![](media/image7.wmf)

TrướcTiếp

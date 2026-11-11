Mô-đun 11: Chiếm quyền điều khiển phiên

Kịch bản

Tấn công chiếm quyền điều khiển phiên đề cập đến việc khai thác cơ chế tạo mã thông báo phiên hoặc kiểm soát bảo mật mã thông báo cho phép kẻ tấn công thiết lập kết nối trái phép với máy chủ mục tiêu. Kẻ tấn công đoán hoặc đánh cắp ID phiên hợp lệ (xác định người dùng đã được xác thực) và sử dụng nó để thiết lập phiên với máy chủ.

Với tư cách là một hacker có đạo đức hoặc người kiểm tra thâm nhập, bạn nên hiểu các khái niệm chiếm quyền điều khiển phiên khác nhau, cách kẻ tấn công thực hiện chiếm quyền điều khiển phiên cấp ứng dụng và cấp mạng cũng như các công cụ khác nhau được sử dụng để khởi động kiểu tấn công này. Bạn cũng có thể triển khai các biện pháp bảo mật ở cả cấp độ ứng dụng và mạng để bảo vệ mạng của mình khỏi bị chiếm quyền điều khiển phiên. Việc chiếm quyền điều khiển cấp ứng dụng liên quan đến việc giành quyền kiểm soát phiên người dùng Giao thức truyền siêu văn bản (HTTP) bằng cách lấy ID phiên. Việc chiếm quyền điều khiển ở cấp độ mạng được ngăn chặn bằng mã hóa gói, có thể đạt được bằng các giao thức như IPsec, SSL và SSH.

Mục tiêu

Mục tiêu của lab là thực hiện chiếm quyền điều khiển phiên và các nhiệm vụ khác bao gồm nhưng không giới hạn ở:

-   Cướp phiên bằng cách chặn lưu lượng giữa máy chủ và máy khách

-   Ăn cắp ID phiên người dùng bằng cách chặn lưu lượng truy cập

-   Phát hiện các cuộc tấn công chiếm quyền điều khiển phiên

Tổng quan về chiếm quyền điều khiển phiên

Việc chiếm quyền điều khiển phiên có thể chủ động hoặc thụ động, tùy thuộc vào mức độ liên quan của kẻ tấn công:

-   **Chiếm quyền điều khiển phiên hoạt động: Kẻ tấn công tìm thấy một phiên đang hoạt động và chiếm lấy nó**

-   **Chiếm quyền điều khiển phiên thụ động: Kẻ tấn công chiếm quyền điều khiển một phiên và thay vì chiếm quyền điều khiển, họ sẽ giám sát và ghi lại tất cả lưu lượng truy cập trong phiên đó**

Nhiệm vụ bài lab

Tin tặc đạo đức hoặc người kiểm tra thâm nhập sử dụng nhiều công cụ và kỹ thuật để thực hiện chiếm quyền điều khiển phiên trên hệ thống mục tiêu. Các bài lab được đề xuất sẽ hỗ trợ bạn tìm hiểu các kỹ thuật chiếm quyền điều khiển phiên khác nhau bao gồm:

1.  Thực hiện chiếm quyền điều khiển phiên

    -   Cướp một phiên sử dụng Caido

    -   Chặn lưu lượng HTTP bằng Hetty

2.  Phát hiện chiếm quyền điều khiển phiên

    -   Phát hiện chiếm quyền điều khiển phiên bằng Wireshark

Lab 1: Thực hiện chiếm quyền điều khiển phiên

**Kịch bản bài lab**

Việc chiếm quyền điều khiển phiên cho phép kẻ tấn công chiếm lấy phiên hoạt động bằng cách bỏ qua quá trình xác thực. Nó liên quan đến việc đánh cắp hoặc đoán ID phiên hợp lệ của nạn nhân mà máy chủ sử dụng để xác định người dùng đã được xác thực và sử dụng nó để thiết lập kết nối với máy chủ. Máy chủ phản hồi các yêu cầu của kẻ tấn công như thể nó đang liên lạc với người dùng đã được xác thực, sau đó kẻ tấn công có thể thực hiện bất kỳ hành động nào trên hệ thống đó.

Những kẻ tấn công có thể sử dụng tính năng chiếm quyền điều khiển phiên để thực hiện nhiều loại tấn công khác nhau như tấn công man-in-the-middle (MITM) và Denial-of-Service (DoS). Một cuộc tấn công MITM xảy ra khi kẻ tấn công đặt mình giữa máy khách được ủy quyền và máy chủ để chặn thông tin truyền theo một trong hai hướng. Một cuộc tấn công DoS xảy ra khi kẻ tấn công đánh hơi thông tin nhạy cảm và sử dụng nó để làm cho tài nguyên máy chủ hoặc mạng không có sẵn cho người dùng, thường bằng cách gửi quá nhiều yêu cầu đến mục tiêu cho đến khi hệ thống bị quá tải.

Là một hacker có đạo đức chuyên nghiệp hoặc người kiểm tra thâm nhập, bạn phải có kiến ​​thức cần thiết để chiếm quyền điều khiển các phiên nhằm kiểm tra các hệ thống trong mạng mục tiêu.

bài lab trong bài tập này trình bày cách chiếm quyền điều khiển phiên hoạt động giữa hai điểm cuối.

**Mục tiêu bài lab**

-   Cướp một phiên sử dụng Caido

-   Chặn lưu lượng HTTP bằng Hetty

**Tổng quan về chiếm quyền điều khiển phiên**

Việc chiếm quyền điều khiển phiên có thể được chia thành ba giai đoạn chính:

-   **Theo dõi kết nối: Kẻ tấn công sử dụng trình thám thính mạng để theo dõi nạn nhân và máy chủ hoặc sử dụng công cụ như Nmap để quét mạng để tìm mục tiêu có chuỗi TCP dễ dự đoán**

-   **Giải đồng bộ kết nối: Trạng thái không đồng bộ xảy ra khi kết nối giữa mục tiêu và máy chủ đã được thiết lập hoặc ổn định khi không truyền dữ liệu hoặc khi số thứ tự của máy chủ không bằng số xác nhận của máy khách (hoặc ngược lại)**

-   **Tiêm gói của kẻ tấn công: Sau khi kẻ tấn công làm gián đoạn kết nối giữa máy chủ và mục tiêu, chúng có thể tiêm dữ liệu vào mạng hoặc tích cực tham gia với tư cách là người trung gian, truyền dữ liệu giữa mục tiêu và máy chủ, đồng thời đọc và tiêm dữ liệu theo ý muốn**

Nhiệm vụ 1: Cướp một phiên bằng Caido

Caido hỗ trợ các chuyên gia bảo mật và những người đam mê kiểm tra các ứng dụng web một cách hiệu quả. Nó cung cấp các công cụ khám phá, bao gồm sơ đồ trang web, lịch sử và các tính năng chặn, hỗ trợ xác định các lỗ hổng và phân tích các yêu cầu trong thời gian thực. Người dùng có thể sửa đổi các yêu cầu đến bằng cách sử dụng các công cụ Chuyển tiếp và Giả mạo, nâng cao khả năng tùy chỉnh thử nghiệm và hiểu biết về bảo mật hệ thống. Tự động hóa được hỗ trợ thông qua công cụ Tự động hóa, cho phép phát hiện lỗ hổng nhanh hơn bằng cách thử nghiệm các yêu cầu đối với danh sách từ lớn. Giao diện người dùng trực quan của Caido đơn giản hóa việc kiểm tra bảo mật cho cả người mới và chuyên gia với điều hướng rõ ràng và các điều khiển thân thiện với người dùng.

Ở đây, chúng tôi sẽ sử dụng Caido để thực hiện chiếm quyền điều khiển phiên trên máy mục tiêu.

Trước khi bắt đầu tác vụ này, chúng ta cần định cấu hình cài đặt proxy trong máy của nạn nhân, trong tác vụ này sẽ là máy Windows Server 2019.

1.  Nhấp vào Windows 11 để chuyển sang máy Windows 11. Đăng nhập bằng Admin/Pa\$\$w0rd.[Windows 11](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

2.  Nhấp vào biểu tượng Windows Tìm kiếm trên Máy tính để bàn, tìm kiếm cmd và khởi chạy Dấu nhắc lệnh từ thanh tìm kiếm.

3.  Chạy lệnh ipconfig/flushdns để đặt lại bộ đệm dns và đóng Dấu nhắc lệnh.

> ![kk.jpg](media/image2.jpeg){width="10.6625in" height="8.0in"}

4.  Nhấp vào biểu tượng Windows Tìm kiếm trên Máy tính để bàn, tìm kiếm Caido và khởi chạy Caido từ thanh tìm kiếm.

5.  Cửa sổ ứng dụng Caido xuất hiện, hãy nhấp vào menu bên cạnh nút Bắt đầu và chọn Chỉnh sửa.

> ![Screenshot](media/image3.jpeg){width="10.6625in" height="8.0in"}

6.  Trong cửa sổ Chỉnh sửa phiên bản, hãy nhấp vào nút radio bên cạnh Tất cả giao diện (0.0.0.0) để nghe trên tất cả giao diện mạng có sẵn và nhấp vào Lưu.

> ![c10.jpg](media/image4.jpeg){width="10.6625in" height="8.0in"}

7.  Nhấp vào nút Bắt đầu để bắt đầu phiên bản cục bộ.

> ![Screenshot](media/image5.jpeg){width="10.6625in" height="8.0in"}

8.  Cửa sổ bật lên chào mừng bạn đến với Caido xuất hiện, nhấp vào Đăng nhập nếu bạn đã có tài khoản. Nếu không, hãy chọn Chưa có tài khoản?, bạn sẽ được chuyển hướng đến Trang tổng quan.

> ![Screenshot](media/image6.jpeg){width="10.6625in" height="8.0in"}

9.  Cửa sổ tạo tài khoản xuất hiện, tại đây hãy điền thông tin chi tiết và nhấp vào Tạo tài khoản.

> ![c13.jpg](media/image7.jpeg){width="10.6625in" height="8.0in"}

10. Đăng nhập vào tài khoản thư của bạn, bạn sẽ nhận được thư xác minh từ Nhóm Caido.sao chép mã và dán vào cửa sổ xác minh Caido.

> ![c14.jpg](media/image8.jpeg){width="10.6625in" height="8.0in"}

11. Sau khi nhập mã, tài khoản của bạn sẽ được kích hoạt như trong ảnh chụp màn hình.

> ![Screenshot](media/image9.jpeg){width="10.6625in" height="8.0in"}

12. Điều hướng quay lại ứng dụng Caido, trong cửa sổ bật lên Chào mừng bạn đến với Caido, nhấp vào Đăng nhập.

> ![Screenshot](media/image10.jpeg){width="10.6625in" height="8.0in"}

13. Trang Chào mừng bạn đến với Caido sẽ xuất hiện, nhập thông tin xác thực của bạn và nhấp vào Đăng nhập.

> ![c17.jpg](media/image11.jpeg){width="10.6625in" height="8.0in"}

14. Sau khi đăng nhập, cửa sổ bật lên Đăng ký phiên bản Caido của bạn sẽ xuất hiện. Nhập Chiếm quyền điều khiển phiên và nhấp vào Đăng ký.

> ![Screenshot](media/image12.jpeg){width="10.6625in" height="8.0in"}

15. Cửa sổ đăng nhập bằng Caido xuất hiện, nhấp vào Cho phép để cho phép truy cập. Ủy quyền hoàn tất! Pop-up xuất hiện, đóng trình duyệt web và quay lại ứng dụng.

> ![c19.jpg](media/image13.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image14.jpeg){width="10.6625in" height="8.0in"}

16. Cửa sổ chính Caido xuất hiện.

> Nếu cửa sổ bật lên Caido xuất hiện, hãy nhấp vào Tiếp theo hoặc Ok trong tất cả các cửa sổ bật lên.
>
> ![Screenshot](media/image15.jpeg){width="10.6625in" height="8.0in"}

17. Nhấp vào nút + Tạo dự án để tạo dự án mới. Tạo một cửa sổ bật lên dự án xuất hiện, đặt tên là Chiếm quyền điều khiển phiên và nhấp vào Tạo.

> ![c21.jpg](media/image16.jpeg){width="10.6625in" height="8.0in"}

18. Nhấp vào tùy chọn Chặn ở khung bên trái, như minh họa trong ảnh chụp màn hình bên dưới.

> ![Screenshot](media/image17.jpeg){width="10.6625in" height="8.0in"}

19. Nhấp vào biểu tượng Chuyển tiếp và đợi cho đến khi biểu tượng này chuyển sang Đang xếp hàng. Nút này sẽ bẫy và hiển thị phản hồi hoặc yêu cầu tiếp theo từ máy của nạn nhân trong tab Chặn.

> Biểu tượng Chuyển tiếp tự động chuyển từ màu xanh sang màu đỏ.
>
> ![c23.jpg](media/image18.jpeg){width="10.6625in" height="8.0in"}

20. Nhấp vào Windows Server 2019 để chuyển sang máy Windows Server 2019. Nhấp vào Ctrl+Alt+Delete để kích hoạt máy và đăng nhập bằng Quản trị viên/Pa\$\$w0rd.[Windows Server 2019](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

> Màn hình Mạng xuất hiện, hãy nhấp vào Có để cho phép các PC và thiết bị khác trên mạng có thể phát hiện ra PC của bạn.

21. Mở trình duyệt web Firefox và điều hướng đến http://10.10.1.11:8080/ca.crt. Chứng chỉ CA sẽ được tải xuống tự động như trong ảnh chụp màn hình.

> ![c2.jpg](media/image19.jpeg){width="10.6625in" height="8.0in"}

22. Trong trình duyệt web Firefox, hãy chọn Cài đặt từ menu ngữ cảnh.

> ![Screenshot](media/image20.jpeg){width="10.6625in" height="8.0in"}

23. Trên trang Cài đặt, hãy tìm kiếm Chứng chỉ và mở Xem Chứng chỉ.

> ![Screenshot](media/image21.jpeg){width="10.6625in" height="8.0in"}

24. Điều hướng đến tab Cơ quan và nhấp vào Nhập...

> ![Screenshot](media/image22.jpeg){width="10.6625in" height="8.0in"}

25. Trong cửa sổ Chọn tệp chứa (các) chứng chỉ CA để nhập , hãy chọn tệp ca.crt đã tải xuống gần đây và nhấp vào Mở.

> ![Screenshot](media/image23.jpeg){width="10.6625in" height="8.0in"}

26. Khi được nhắc, hãy nhấp vào hộp kiểm Tin cậy CA này để xác định trang web và nhấp vào OK. Nhấp vào OK trong cửa sổ Trình quản lý chứng chỉ.

> ![Screenshot](media/image24.jpeg){width="10.6625in" height="8.0in"}

27. Trên trang Cài đặt, hãy tìm kiếm proxy và mở nó.

> ![Screenshot](media/image25.jpeg){width="10.6625in" height="8.0in"}

28. Trang Cài đặt kết nối xuất hiện và nhấp vào Cấu hình proxy thủ công để định cấu hình proxy.

29. Đặt Proxy HTTP thành 10.10.1.11 và chuyển thành 8080, chọn hộp Cũng sử dụng proxy này cho HTTPS rồi nhấp vào OK.

> ![Screenshot](media/image26.jpeg){width="10.6625in" height="8.0in"}

30. Sau khi lưu, hãy đóng Cài đặt và cửa sổ trình duyệt. Bây giờ bạn đã định cấu hình cài đặt proxy trên máy của nạn nhân.

31. Mở một tab mới trong trình duyệt web Firefox và đặt con trỏ chuột vào thanh địa chỉ, nhập www.moviescope.com và nhấn Enter.

> Nếu một thông báo xuất hiện cho biết rằng Kết nối của bạn không phải là kết nối riêng tư. Nhấp vào nút Nâng cao. Trên trang tiếp theo, hãy nhấp vào Tiếp tục tới www.moviescope.com (không an toàn) để mở trang web.

32. Bây giờ, hãy nhấp vào Windows 11 để chuyển về máy của kẻ tấn công (Windows 11) và quan sát rằng Caido đã bắt đầu nắm bắt các yêu cầu từ máy của nạn nhân.[Windows 11](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

> ![Screenshot](media/image27.jpeg){width="10.6625in" height="8.0in"}

33. Trên tab Yêu cầu , đối với tất cả các yêu cầu www.moviescope.com, hãy sửa đổi www.moviescope.com thành www.goodshopping.com trong tất cả các yêu cầu GET và Chuyển tiếp tất cả các yêu cầu đã ghi lại.

> ![Screenshot](media/image28.jpeg){width="10.6625in" height="8.0in"}

34. Theo cách tương tự, hãy sửa đổi mọi yêu cầu GET được Caido ghi lại cho đến khi bạn thấy trang www.goodshopping.com trong máy của nạn nhân. Bạn sẽ cần chuyển đổi qua lại từ máy của nạn nhân để xem trạng thái trình duyệt trong khi thực hiện việc này.

> Nếu bạn không nhận được bất kỳ yêu cầu nào hoặc thấy tab Yêu cầu trống thì hãy chuyển sang máy Windows Server 2019 và làm mới trình duyệt để ghi lại yêu cầu.

35. Bây giờ, hãy nhấp vào Windows Server 2019 để chuyển sang máy của nạn nhân (Windows Server 2019); trình duyệt hiển thị trang web mà kẻ tấn công muốn máy của nạn nhân nhìn thấy (trong ví dụ này là www.goodshopping.com).[Windows Server 2019](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

36. Nạn nhân đã điều hướng đến www.moviescope.com nhưng giờ nhìn thấy www.goodshopping.com; trong khi thanh địa chỉ hiển thị www. moviescope.com, cửa sổ hiển thị www.goodshopping.com.

> ![Screenshot](media/image29.jpeg){width="10.6625in" height="8.0in"}

37. Bây giờ, chúng ta sẽ thay đổi cài đặt proxy về cài đặt mặc định. Để làm như vậy, trong trình duyệt Firefox, hãy chọn Cài đặt từ menu ngữ cảnh. Trên trang Cài đặt, hãy tìm kiếm proxy và mở nó. Trang Cài đặt kết nối xuất hiện, chọn nút radio Không có proxy và nhấp vào OK.

38. Điều này kết thúc phần minh họa thực hiện chiếm quyền điều khiển phiên bằng Caido.

39. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 11.1.1.1**

Sử dụng công cụ Caido trên máy tấn công (10.10.1.11) để chiếm quyền điều khiển phiên được thiết lập khi người dùng trên máy nạn nhân (10.10.1.19) truy cập trang web www.moviescope.com và chuyển hướng đến www.goodshopping.com bằng trình duyệt Firefox. Tab Phản hồi nằm ở phần nào.

![](media/image30.wmf)

Đúng

Nhiệm vụ 2: Chặn lưu lượng HTTP bằng Hetty

Hetty là bộ công cụ HTTP để nghiên cứu bảo mật. Nó nhằm mục đích trở thành một giải pháp thay thế nguồn mở cho phần mềm thương mại như Burp Suite Pro, với các tính năng mạnh mẽ phù hợp với nhu cầu của InfoSec và cộng đồng tiền thưởng lỗi. Hetty có thể được sử dụng để thực hiện tấn công Machine-in-the-middle (MITM), tạo/chỉnh sửa yêu cầu theo cách thủ công và phát lại các yêu cầu được ủy quyền cho máy khách HTTP, đồng thời chặn thêm các yêu cầu và phản hồi để xem xét thủ công.

Ở đây, chúng ta sẽ sử dụng công cụ Hetty để chặn lưu lượng HTTP trên hệ thống đích.

Ở đây, chúng tôi sẽ sử dụng máy Windows 11 làm máy tấn công và máy Windows Server 2022 làm máy mục tiêu.

1.  Nhấp vào Windows 11 để chuyển sang máy Windows 11.[Windows 11](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

2.  Điều hướng đến E:\\CEH-Tools\\CEHv13 Mô-đun 11 Session Hijacking\\Hetty và nhấp đúp vào hetty.exe.

> Nếu cửa sổ Mở tệp - Cảnh báo bảo mật xuất hiện, hãy nhấp vào Chạy.

3.  Cửa sổ Dấu nhắc Lệnh xuất hiện và Hetty khởi chạy.

> ![Screenshot](media/image31.jpeg){width="10.6625in" height="8.0in"}

4.  Bây giờ, hãy thu nhỏ tất cả các cửa sổ và khởi chạy bất kỳ trình duyệt web nào (tại đây, Mozilla Firefox). Truy cập http://localhost:8080 để mở trang tổng quan Hetty.

5.  Trong trang tổng quan Hetty, hãy nhấp vào nút QUẢN LÝ DỰ ÁN.

> ![Screenshot](media/image32.jpeg){width="10.6625in" height="8.0in"}

6.  Trang dự án xuất hiện, hãy nhập Tên dự án dưới dạng Moviescope và nhấp vào nút + TẠO & MỞ DỰ ÁN.

> ![Screenshot](media/image33.jpeg){width="10.6625in" height="8.0in"}

7.  Bạn có thể quan sát thấy tên dự án mới Moviescope đã được tạo trong phần Quản lý dự án với trạng thái là Đang hoạt động.

> ![Screenshot](media/image34.jpeg){width="10.6625in" height="8.0in"}

8.  Nhấp vào biểu tượng Nhật ký proxy ( )) từ ngăn bên trái.![2022-04-13_15-20-45.png](media/image35.png){width="0.25972222222222224in" height="0.23402777777777778in"}

9.  Trang Nhật ký proxy xuất hiện như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image36.jpeg){width="10.6625in" height="8.0in"}

10. Bây giờ, hãy nhấp vào Windows Server 2022 để chuyển sang máy Windows Server 2022. Nhấp vào Ctrl+Alt+Delete để kích hoạt máy và đăng nhập bằng Quản trị viên/Pa\$\$w0rd.[Windows Server 2022](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

> Màn hình Mạng xuất hiện, hãy nhấp vào Có để cho phép các PC và thiết bị khác trên mạng có thể phát hiện ra PC của bạn.

11. Mở trình duyệt web Google Chrome , nhấp vào biểu tượng Tùy chỉnh và kiểm soát Google Chrome và chọn Cài đặt từ menu ngữ cảnh.

> ![Screenshot](media/image37.jpeg){width="10.6625in" height="8.0in"}

12. Trên trang Cài đặt, cuộn xuống và nhấp vào Hệ thống trong ngăn bên trái.

> ![Screenshot](media/image38.jpeg){width="10.6625in" height="8.0in"}

13. Cuộn xuống phần Hệ thống và nhấp vào Mở cài đặt proxy trên máy tính của bạn để định cấu hình proxy.

> ![Screenshot](media/image39.jpeg){width="10.6625in" height="8.0in"}

14. Cửa sổ Cài đặt xuất hiện với cài đặt Proxy ở ngăn bên phải.

15. Trong phần Thiết lập proxy thủ công, hãy thực hiện các thay đổi sau:

    -   Trong tùy chọn Sử dụng máy chủ proxy, hãy nhấp vào nút Tắt để bật .

    -   Trong trường Địa chỉ, hãy nhập 10.10.1.11 (địa chỉ IP của máy của kẻ tấn công, tại đây, Windows 11).

    -   Trong trường Cổng, nhập 8080.

    -   Nhấp vào Lưu.

> ![Screenshot](media/image40.jpeg){width="10.6625in" height="8.0in"}

16. Sau khi lưu, hãy đóng Cài đặt và cửa sổ trình duyệt. Bây giờ bạn đã định cấu hình cài đặt proxy trên máy của nạn nhân.

17. Bây giờ, trong trình duyệt web, hãy truy cập http://www.moviescope.com.

> ![Screenshot](media/image41.jpeg){width="10.6625in" height="8.0in"}

18. Nhấp vào Windows 11 để chuyển sang máy Windows 11.[Windows 11](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

19. Bạn có thể quan sát thấy nhật ký được ghi lại trong trang Nhật ký proxy. Ở đây, chúng tôi đang tập trung vào nhật ký được liên kết với trang web moviescope.com.

> ![Screenshot](media/image42.jpeg){width="10.6625in" height="8.0in"}

20. Nhấp vào Windows Server 2022 để chuyển về máy Windows Server 2022.[Windows Server 2022](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

21. Trong trang web MovieScope , hãy đăng nhập với tư cách nạn nhân bằng thông tin đăng nhập là sam/test.

> ![Screenshot](media/image43.jpeg){width="10.6625in" height="8.0in"}

22. Bây giờ, hãy nhấp vào Windows 11 để chuyển sang máy Windows 11.[Windows 11](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

23. Trong trang Nhật ký proxy, hãy cuộn xuống để kiểm tra thêm nhật ký trên trang web moviescope. Kiểm tra nhật ký POST được ghi lại cho trang web mục tiêu.

> ![Screenshot](media/image44.jpeg){width="10.6625in" height="8.0in"}

24. Chọn yêu cầu ĐĂNG và ở phần dưới của trang, hãy chọn tab Nội dung trong phần ĐĂNG.

25. Trong tab Nội dung , bạn có thể quan sát thông tin xác thực của người dùng đã thu thập, như minh họa trong ảnh chụp màn hình.

> ![2.27.jpg](media/image45.jpeg){width="10.6625in" height="8.0in"}

26. Thông tin xác thực đã thu thập có thể được sử dụng để đăng nhập vào tài khoản của người dùng mục tiêu và lấy thêm thông tin nhạy cảm.

27. Bây giờ, chúng ta sẽ thay đổi cài đặt proxy về cài đặt mặc định. Để làm như vậy, hãy nhấp vào Windows Server 2022 để chuyển trở lại máy Windows Server 2022 và thực hiện lại Bước 13-15.[Windows Server 2022](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

> Nếu bạn đã đăng xuất khỏi máy Windows Server 2022, hãy nhấp vào Ctrl+Alt+Delete, sau đó đăng nhập bằng CEH\\Administrator / Pa\$\$w0rd.

28. Trong cửa sổ Cài đặt, trong phần Thiết lập proxy thủ công ở ngăn bên phải, hãy nhấp vào nút Bật để chuyển lại thành Tắt, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image46.jpeg){width="10.6625in" height="8.0in"}

29. Điều này kết thúc việc trình diễn việc chặn lưu lượng HTTP bằng Hetty.

30. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 11.1.2.1**

Sử dụng công cụ Hetty để chặn lưu lượng HTTP trên máy Windows Server 2022. Nhập url đã được nhập vào thanh địa chỉ của trình duyệt để mở bảng điều khiển Hetty.

![](media/image30.wmf)

**Câu 11.1.2.2**

Sử dụng công cụ Hetty để chặn lưu lượng HTTP trên máy Windows Server 2022. Mật khẩu bị bắt trong công cụ Hetty bằng cách chặn lưu lượng truy cập của Windows Server 2022 là gì?

![](media/image30.wmf)

Lab 2: Phát hiện chiếm quyền điều khiển phiên

**Kịch bản bài lab**

Việc chiếm quyền điều khiển phiên rất nguy hiểm; nó khiến nạn nhân có nguy cơ bị đánh cắp danh tính, lừa đảo và mất thông tin nhạy cảm. Tất cả các mạng sử dụng TCP/IP đều dễ bị tấn công bởi các kiểu tấn công chiếm quyền điều khiển khác nhau. Hơn nữa, những kiểu tấn công này rất khó phát hiện và thường không được chú ý trừ khi kẻ tấn công gây ra thiệt hại nghiêm trọng. Tuy nhiên, thực hiện theo các phương pháp hay nhất có thể bảo vệ khỏi các cuộc tấn công chiếm quyền điều khiển phiên.

Là một hacker có đạo đức chuyên nghiệp hoặc người kiểm tra thâm nhập, điều quan trọng là bạn phải có kiến ​​thức cần thiết để phát hiện các cuộc tấn công chiếm quyền điều khiển phiên và bảo vệ hệ thống của tổ chức bạn trước chúng. May mắn thay, có nhiều công cụ khác nhau có thể giúp bạn phát hiện các cuộc tấn công chiếm quyền điều khiển phiên như trình thám thính gói, IDS và SIEM.

**Mục tiêu bài lab**

-   Phát hiện chiếm quyền điều khiển phiên bằng Wireshark

**Tổng quan về Phát hiện chiếm quyền điều khiển phiên**

Có hai phương pháp chính có thể được sử dụng để phát hiện việc chiếm quyền điều khiển phiên:

-   **Phương pháp thủ công: Liên quan đến việc sử dụng phần mềm đánh hơi gói như Wireshark để theo dõi các cuộc tấn công chiếm quyền điều khiển phiên; trình thám thính gói sẽ nắm bắt các gói đang được truyền qua mạng, sau đó được phân tích bằng nhiều công cụ lọc khác nhau**

-   **Phương pháp tự động: Liên quan đến việc sử dụng Hệ thống phát hiện xâm nhập (IDS) và Hệ thống ngăn chặn xâm nhập (IPS) để giám sát lưu lượng truy cập mạng đến; nếu một gói khớp với bất kỳ dấu hiệu tấn công nào trong cơ sở dữ liệu nội bộ, IDS sẽ tạo cảnh báo và IPS sẽ chặn lưu lượng truy cập vào cơ sở dữ liệu**

Nhiệm vụ 1: Phát hiện chiếm quyền điều khiển phiên bằng Wireshark

Wireshark cho phép bạn nắm bắt và duyệt tương tác lưu lượng truy cập đang chạy trên mạng. Công cụ này sử dụng WinPcap để chụp các gói và do đó chỉ có thể chụp các gói trên các mạng được WinPcap hỗ trợ. Nó nắm bắt lưu lượng mạng trực tiếp từ các mạng Ethernet, IEEE 802.11, PPP/HDLC, ATM, Bluetooth, USB, Token Ring, Frame Relay và FDDI. Các chuyên gia bảo mật có thể sử dụng Wireshark để theo dõi và phát hiện các nỗ lực chiếm quyền điều khiển phiên.

Ở đây, chúng tôi sẽ sử dụng công cụ Wireshark để phát hiện các cuộc tấn công chiếm quyền điều khiển phiên theo cách thủ công trên hệ thống đích.

Chúng tôi sẽ sử dụng máy Parrot Security (10.10.1.13) để thực hiện cuộc tấn công chiếm quyền điều khiển phiên trên máy Windows 11 (10.10.1.11).

1.  Nhấp vào Windows 11 để chuyển sang máy Windows 11.[Windows 11](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

2.  Nhấp vào biểu tượng Windows Tìm kiếm trên Máy tính để bàn, tìm kiếm Wireshark trong thanh tìm kiếm và khởi chạy nó.

3.  Cửa sổ Trình phân tích mạng Wireshark xuất hiện, bắt đầu ghi lại lưu lượng truy cập mạng trên giao diện mạng chính (tại đây, Ethernet).

4.  Bây giờ, chúng ta sẽ tiến hành một cuộc tấn công chiếm quyền điều khiển phiên trên máy mục tiêu (Windows 11) bằng cách sử dụng Bettercap.

> Để làm như vậy, bạn có thể làm theo các Bước 8-11 bên dưới hoặc tham khảo Nhiệm vụ 2 (Chặn lưu lượng truy cập HTTP bằng cách sử dụng Bettercap) trong Lab 1.

5.  Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

6.  Mở cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu). Chạy cd để chuyển đến thư mục gốc.

7.  Chạy bettercap -iface eth0 để đặt giao diện mạng.

> **-iface: chỉ định giao diện để liên kết (ở đây là eth0).**
>
> ![Screenshot](media/image47.jpeg){width="10.6625in" height="8.0in"}

8.  Nhập net.probe trên và nhấn Enter. Mô-đun này sẽ gửi các loại gói thăm dò khác nhau tới từng IP trong mạng con hiện tại để mô-đun net.recon phát hiện chúng.

9.  Nhập net.recon trên và nhấn Enter. Mô-đun này chịu trách nhiệm đọc định kỳ bảng ARP của hệ thống để phát hiện các máy chủ mới trên mạng.

> Mô-đun net.recon hiển thị các địa chỉ IP hoạt động được phát hiện trong mạng. Trong thời gian thực, mô-đun này sẽ bắt đầu đánh hơi các gói mạng.

10. Nhập net.sniff on và nhấn Enter. Mô-đun này chịu trách nhiệm thực hiện việc đánh hơi trên mạng.

11. Bạn có thể quan sát thấy Bettercap bắt đầu đánh hơi lưu lượng mạng trên các máy khác nhau trong mạng, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image48.jpeg){width="10.6625in" height="8.0in"}

12. Nhấp vào Windows 11 để quay lại máy Windows 11 và quan sát số lượng lớn gói ARP được Wireshark ghi lại, như hiển thị trong ảnh chụp màn hình.[Windows 11](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

> Bettercap gửi một số yêu cầu phát ARP đến máy chủ (hoặc máy chủ có khả năng hoạt động). Số lượng yêu cầu ARP cao cho thấy rằng hệ thống tại 10.10.1.13 (hệ thống của kẻ tấn công trong nhiệm vụ này) đang hoạt động như một máy khách cho tất cả các địa chỉ IP trong mạng con, nghĩa là tất cả các gói từ nút nạn nhân (trong trường hợp này là 10.10.1.11) trước tiên sẽ đi đến hệ thống máy chủ (10.10.1.13) rồi đến cổng. Tương tự, bất kỳ gói nào đến nút nạn nhân trước tiên sẽ được chuyển tiếp từ cổng vào hệ thống máy chủ, sau đó từ hệ thống máy chủ đến nút nạn nhân.
>
> thêm\...
>
> ![Screenshot](media/image49.jpeg){width="10.6625in" height="8.0in"}

13. Phần này kết thúc phần minh họa cách phát hiện cuộc tấn công chiếm quyền điều khiển phiên bằng Wireshark.

14. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 11.2.1.1**

Sử dụng công cụ Bettercap (có sẵn trong máy Parrot Security) để đánh hơi lưu lượng truy cập trên hệ thống đích (10.10.1.11). Sử dụng công cụ Wireshark trên hệ thống đích (10.10.1.11) để phát hiện nỗ lực chiếm quyền điều khiển phiên. Lưu lượng truy cập trên giao thức nào cho biết nỗ lực chiếm quyền điều khiển phiên trong Wireshark?

Lab 2: Phát hiện chiếm quyền điều khiển phiên

**Kịch bản bài lab**

Việc chiếm quyền điều khiển phiên rất nguy hiểm; nó khiến nạn nhân có nguy cơ bị đánh cắp danh tính, lừa đảo và mất thông tin nhạy cảm. Tất cả các mạng sử dụng TCP/IP đều dễ bị tấn công bởi các kiểu tấn công chiếm quyền điều khiển khác nhau. Hơn nữa, những kiểu tấn công này rất khó phát hiện và thường không được chú ý trừ khi kẻ tấn công gây ra thiệt hại nghiêm trọng. Tuy nhiên, thực hiện theo các phương pháp hay nhất có thể bảo vệ khỏi các cuộc tấn công chiếm quyền điều khiển phiên.

Là một hacker có đạo đức chuyên nghiệp hoặc người kiểm tra thâm nhập, điều quan trọng là bạn phải có kiến ​​thức cần thiết để phát hiện các cuộc tấn công chiếm quyền điều khiển phiên và bảo vệ hệ thống của tổ chức bạn trước chúng. May mắn thay, có nhiều công cụ khác nhau có thể giúp bạn phát hiện các cuộc tấn công chiếm quyền điều khiển phiên như trình thám thính gói, IDS và SIEM.

**Mục tiêu bài lab**

-   Phát hiện chiếm quyền điều khiển phiên bằng Wireshark

**Tổng quan về Phát hiện chiếm quyền điều khiển phiên**

Có hai phương pháp chính có thể được sử dụng để phát hiện việc chiếm quyền điều khiển phiên:

-   **Phương pháp thủ công: Liên quan đến việc sử dụng phần mềm đánh hơi gói như Wireshark để theo dõi các cuộc tấn công chiếm quyền điều khiển phiên; trình thám thính gói sẽ nắm bắt các gói đang được truyền qua mạng, sau đó được phân tích bằng nhiều công cụ lọc khác nhau**

-   **Phương pháp tự động: Liên quan đến việc sử dụng Hệ thống phát hiện xâm nhập (IDS) và Hệ thống ngăn chặn xâm nhập (IPS) để giám sát lưu lượng truy cập mạng đến; nếu một gói khớp với bất kỳ dấu hiệu tấn công nào trong cơ sở dữ liệu nội bộ, IDS sẽ tạo cảnh báo và IPS sẽ chặn lưu lượng truy cập vào cơ sở dữ liệu**

Nhiệm vụ 1: Phát hiện chiếm quyền điều khiển phiên bằng Wireshark

Wireshark cho phép bạn nắm bắt và duyệt tương tác lưu lượng truy cập đang chạy trên mạng. Công cụ này sử dụng WinPcap để chụp các gói và do đó chỉ có thể chụp các gói trên các mạng được WinPcap hỗ trợ. Nó nắm bắt lưu lượng mạng trực tiếp từ các mạng Ethernet, IEEE 802.11, PPP/HDLC, ATM, Bluetooth, USB, Token Ring, Frame Relay và FDDI. Các chuyên gia bảo mật có thể sử dụng Wireshark để theo dõi và phát hiện các nỗ lực chiếm quyền điều khiển phiên.

Ở đây, chúng tôi sẽ sử dụng công cụ Wireshark để phát hiện các cuộc tấn công chiếm quyền điều khiển phiên theo cách thủ công trên hệ thống đích.

Chúng tôi sẽ sử dụng máy Parrot Security (10.10.1.13) để thực hiện cuộc tấn công chiếm quyền điều khiển phiên trên máy Windows 11 (10.10.1.11).

1.  Nhấp vào Windows 11 để chuyển sang máy Windows 11.[Windows 11](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

2.  Nhấp vào biểu tượng Windows Tìm kiếm trên Máy tính để bàn, tìm kiếm Wireshark trong thanh tìm kiếm và khởi chạy nó.

3.  Cửa sổ Trình phân tích mạng Wireshark xuất hiện, bắt đầu ghi lại lưu lượng truy cập mạng trên giao diện mạng chính (tại đây, Ethernet).

4.  Bây giờ, chúng ta sẽ tiến hành một cuộc tấn công chiếm quyền điều khiển phiên trên máy mục tiêu (Windows 11) bằng cách sử dụng Bettercap.

> Để làm như vậy, bạn có thể làm theo các Bước 8-11 bên dưới hoặc tham khảo Nhiệm vụ 2 (Chặn lưu lượng truy cập HTTP bằng cách sử dụng Bettercap) trong Lab 1.

5.  Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

6.  Mở cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu). Chạy cd để chuyển đến thư mục gốc.

7.  Chạy bettercap -iface eth0 để đặt giao diện mạng.

> **-iface: chỉ định giao diện để liên kết (ở đây là eth0).**
>
> ![Screenshot](media/image47.jpeg){width="10.6625in" height="8.0in"}

8.  Nhập net.probe trên và nhấn Enter. Mô-đun này sẽ gửi các loại gói thăm dò khác nhau tới từng IP trong mạng con hiện tại để mô-đun net.recon phát hiện chúng.

9.  Nhập net.recon trên và nhấn Enter. Mô-đun này chịu trách nhiệm đọc định kỳ bảng ARP của hệ thống để phát hiện các máy chủ mới trên mạng.

> Mô-đun net.recon hiển thị các địa chỉ IP hoạt động được phát hiện trong mạng. Trong thời gian thực, mô-đun này sẽ bắt đầu đánh hơi các gói mạng.

10. Nhập net.sniff on và nhấn Enter. Mô-đun này chịu trách nhiệm thực hiện việc đánh hơi trên mạng.

11. Bạn có thể quan sát thấy Bettercap bắt đầu đánh hơi lưu lượng mạng trên các máy khác nhau trong mạng, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image48.jpeg){width="10.6625in" height="8.0in"}

12. Nhấp vào Windows 11 để quay lại máy Windows 11 và quan sát số lượng lớn gói ARP được Wireshark ghi lại, như hiển thị trong ảnh chụp màn hình.[Windows 11](https://labclient.labondemand.com/Instructions/74e97a21-759d-4cfd-9430-90ef35be9a35)

> Bettercap gửi một số yêu cầu phát ARP đến máy chủ (hoặc máy chủ có khả năng hoạt động). Số lượng yêu cầu ARP cao cho thấy rằng hệ thống tại 10.10.1.13 (hệ thống của kẻ tấn công trong nhiệm vụ này) đang hoạt động như một máy khách cho tất cả các địa chỉ IP trong mạng con, nghĩa là tất cả các gói từ nút nạn nhân (trong trường hợp này là 10.10.1.11) trước tiên sẽ đi đến hệ thống máy chủ (10.10.1.13) rồi đến cổng. Tương tự, bất kỳ gói nào đến nút nạn nhân trước tiên sẽ được chuyển tiếp từ cổng vào hệ thống máy chủ, sau đó từ hệ thống máy chủ đến nút nạn nhân.
>
> thêm\...
>
> ![Screenshot](media/image49.jpeg){width="10.6625in" height="8.0in"}

13. Phần này kết thúc phần minh họa cách phát hiện cuộc tấn công chiếm quyền điều khiển phiên bằng Wireshark.

14. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 11.2.1.1**

Sử dụng công cụ Bettercap (có sẵn trong máy Parrot Security) để đánh hơi lưu lượng truy cập trên hệ thống đích (10.10.1.11). Sử dụng công cụ Wireshark trên hệ thống đích (10.10.1.11) để phát hiện nỗ lực chiếm quyền điều khiển phiên. Lưu lượng truy cập trên giao thức nào cho biết nỗ lực chiếm quyền điều khiển phiên trong Wireshark?

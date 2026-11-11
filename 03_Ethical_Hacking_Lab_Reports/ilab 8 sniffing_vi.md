Mô-đun 08: Đánh hơi

Kịch bản

Các mô-đun trước đã dạy cách làm hư hại các hệ thống mục tiêu bằng cách lây nhiễm chúng bằng phần mềm độc hại, điều này cho phép kiểm soát hạn chế hoặc toàn bộ hệ thống mục tiêu để tiếp tục thực hiện việc trích xuất dữ liệu.

Bây giờ, là một hacker có đạo đức hoặc kiểm thử xâm nhập, việc hiểu về sniffing mạng là rất quan trọng. Packet sniffing cho phép một người quan sát và truy cập toàn bộ lưu lượng mạng từ một điểm nhất định. Nó giám sát bất kỳ bit thông tin nào vào hoặc ra khỏi mạng. Có hai loại sniffing: thụ động và chủ động. Sniffing thụ động đề cập đến việc sniffing trên mạng dựa trên hub; sniffing chủ động đề cập đến việc sniffing trên mạng dựa trên switch.

Mặc dù việc nghe lén thụ động từng là chủ yếu, kiến trúc bảo mật mạng thích hợp đã được triển khai (mạng dựa trên switch) để giảm thiểu loại tấn công này. Tuy nhiên, vẫn có một vài kẽ hở trong việc triển khai mạng dựa trên switch có thể mở ra cơ hội cho kẻ tấn công nghe trộm lưu lượng mạng.

Kẻ tấn công xâm nhập mạng bằng cách sử dụng các công cụ nghe lén (sniffer), trong đó họ chủ yếu nhắm vào các giao thức dễ bị nghe lén. Một số giao thức dễ bị tấn công bao gồm HTTP, FTP, SMTP, POP, Telnet, IMAP và NNTP. Lưu lượng bị nghe lén bao gồm dữ liệu như mật khẩu FTP và Telnet, các phiên trò chuyện, email và lưu lượng web, cùng với lưu lượng DNS. Khi kẻ tấn công có được những thông tin nhạy cảm này, họ có thể cố gắng mạo danh các phiên người dùng mục tiêu.

Do đó, một hacker đạo đức hoặc kiểm thử xâm nhập cần đánh giá bảo mật của hạ tầng mạng, tìm ra các lỗ hổng trong mạng bằng cách sử dụng các công cụ kiểm toán mạng khác nhau, và vá chúng để đảm bảo một môi trường mạng an toàn.

Các bài lab trong mô-đun này cung cấp trải nghiệm thời gian thực trong việc thực hiện bắt gói tin trên mạng mục tiêu bằng cách sử dụng các kỹ thuật và công cụ bắt gói tin khác nhau.

Mục tiêu

Mục tiêu của bài lab là thực hiện việc theo dõi mạng và các nhiệm vụ khác bao gồm, nhưng không giới hạn ở:

-   Nghe lén mạng

-   Phân tích các gói dữ liệu đến và đi để phát hiện bất kỳ cuộc tấn công nào

-   Khắc phục sự cố mạng để cải thiện hiệu suất

-   Bảo vệ mạng khỏi các cuộc tấn công

Tổng quan về nghe lén mạng

Theo dõi dữ liệu rất đơn giản trong các mạng dựa trên hub, vì lưu lượng trên một đoạn đi qua tất cả các máy chủ liên quan đến đoạn đó. Tuy nhiên, hầu hết các mạng ngày nay hoạt động trên các switch. Switch là một thiết bị mạng máy tính tiên tiến. Sự khác biệt chính giữa hub và switch là hub truyền dữ liệu dòng đến từng cổng trên máy và không có việc ánh xạ dòng, trong khi switch xem địa chỉ Điều khiển Truy cập Phương tiện (MAC) liên quan đến từng khung đi qua nó và gửi dữ liệu đến cổng yêu cầu. Địa chỉ MAC là địa chỉ phần cứng xác định duy nhất từng nút của một mạng.

Bộ nghe gói tin được sử dụng để chuyển đổi card mạng (NIC) của hệ thống chủ sang chế độ đa nhiệm. NIC ở chế độ đa nhiệm sau đó có thể bắt các gói tin được gửi đến mạng cụ thể. Có hai loại nghe gói tin. Mỗi loại được sử dụng cho các loại mạng khác nhau. Hai loại đó là:

-   **Nghe lén thụ động: Nghe lén thụ động không gửi bất kỳ gói dữ liệu nào. Nó chỉ ghi lại và theo dõi các gói dữ liệu đang lưu thông trong mạng**

-   **Nghe trộm Chủ động: Nghe trộm chủ động tìm kiếm lưu lượng trên một mạng LAN chuyển mạch bằng cách chủ động tiêm lưu lượng vào mạng LAN; nó cũng đề cập đến việc nghe trộm qua một thiết bị chuyển mạch**

Nhiệm vụ bài lab

Các hacker đạo đức hoặc chuyên gia kiểm thử xâm nhập sử dụng nhiều công cụ và kỹ thuật để thực hiện việc theo dõi mạng. Các bài lab được khuyến nghị giúp học các kỹ thuật theo dõi mạng khác nhau bao gồm:

1.  Thực hiện đánh hơi chủ động

    -   Thực hiện tràn MAC bằng cách sử dụng macof

    -   Thực hiện tấn công cạn kiệt DHCP bằng cách sử dụng Yersinia

2.  Thực hiện theo dõi mạng sử dụng các công cụ theo dõi khác nhau

    -   Thực hiện theo dõi mật khẩu bằng Wireshark

3.  Phát hiện đánh hơi mạng

    -   Phát hiện tấn công ARP và chế độ promiscuous trong mạng dựa trên switch

Thí nghiệm 1: Thực hiện Sniffing Chủ động

**kịch bản bài lab bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc chuyên viên kiểm thử xâm nhập, bước đầu tiên là thực hiện sniffing chủ động trên mạng mục tiêu bằng cách sử dụng các kỹ thuật sniffing chủ động khác nhau như ngập MAC, cạn kiệt DHCP, đầu độc ARP, hoặc MITM. Trong sniffing chủ động, Ethernet chuyển mạch không truyền thông tin tới tất cả các hệ thống kết nối qua LAN như trong mạng dựa trên hub.

Trong việc sniffing chủ động, lưu lượng ARP được tiêm chủ động vào một LAN để sniff xung quanh một mạng chuyển mạch và chụp lưu lượng của nó. Một trình sniffer gói có thể lấy tất cả thông tin có thể nhìn thấy trên mạng và ghi lại nó để xem lại sau. Một kiểm thử viên có thể thấy tất cả thông tin trong gói, bao gồm dữ liệu lẽ ra phải được giữ ẩn.

Một hacker đạo đức hoặc chuyên gia kiểm tra xâm nhập cần đảm bảo rằng mạng của tổ chức được bảo mật khỏi các cuộc tấn công sniffing đang hoạt động bằng cách phân tích các gói dữ liệu đến và đi để phát hiện bất kỳ cuộc tấn công nào.

**Mục tiêu bài lab**

-   Thực hiện tràn MAC bằng cách sử dụng macof

-   Thực hiện tấn công cạn kiệt DHCP bằng cách sử dụng Yersinia

**Tổng quan về việc ngửi dữ liệu chủ động**

Sniffing chủ động liên quan đến việc gửi nhiều gói dò mạng để xác định các điểm truy cập. Dưới đây là danh sách các kỹ thuật sniffing chủ động khác nhau:

-   **Ngập MAC: Liên quan đến việc làm đầy bảng CAM bằng các cặp địa chỉ MAC và IP giả cho đến khi nó đầy**

-   **Độc hại DNS: Liên quan đến việc lừa một máy chủ DNS tin rằng nó đã nhận được thông tin xác thực trong khi thực tế thì không**

-   **Độc hại ARP: Bao gồm việc tạo ra một số lượng lớn gói tin yêu cầu và trả lời ARP giả để làm quá tải một switch**

-   **Tấn công DHCP: Bao gồm thực hiện tấn công cạn kiệt DHCP và tấn công máy chủ DHCP giả mạo**

-   **Đánh cắp cổng switch: Liên quan đến việc làm ngập switch với các gói ARP miễn phí giả mạo có địa chỉ MAC mục tiêu làm nguồn**

-   **Tấn công giả mạo: Liên quan đến việc thực hiện giả mạo MAC, nhảy VLAN và tấn công STP để đánh cắp thông tin nhạy cảm**

Nhiệm vụ 1: Thực hiện MAC Flooding bằng macof

Tấn công tràn MAC là một kỹ thuật được sử dụng để xâm phạm bảo mật của các switch mạng kết nối các phân đoạn mạng hoặc thiết bị mạng. Kẻ tấn công sử dụng kỹ thuật tràn MAC để buộc switch hoạt động như một hub, nhờ đó họ có thể dễ dàng theo dõi lưu lượng mạng.

macof là một công cụ trên Unix và Linux, là một phần của bộ công cụ dsniff. Nó làm ngập mạng cục bộ với các địa chỉ MAC và địa chỉ IP ngẫu nhiên, khiến một số switch gặp lỗi và mở ở chế độ lặp lại, từ đó tạo điều kiện thuận lợi cho việc giám sát. Công cụ này làm ngập bảng CAM của switch (131.000 mỗi phút) bằng cách gửi các mục MAC giả mạo. Khi bảng MAC đầy, switch sẽ chuyển sang hoạt động giống như hub, nơi kẻ tấn công có thể theo dõi dữ liệu đang được phát.

Ở đây, chúng tôi sẽ sử dụng công cụ macof để thực hiện MAC flooding.

1.  Theo mặc định, máy Windows 11 được chọn, để khởi động máy Parrot Security, nhấp vào Parrot Security và đăng nhập bằng attacker/toor.[Parrot Security](https://labclient.labondemand.com/Instructions/e24ba80f-a3b3-42e8-9ac3-e74faaa4fc16)

> Nếu một cửa sổ bật lên Parrot Updater xuất hiện ở góc trên bên phải của Màn hình, hãy bỏ qua và đóng nó.
>
> Nếu một cửa sổ bật lên Hỏi xuất hiện yêu cầu bạn cập nhật máy, hãy nhấp vào Không để đóng cửa sổ.

2.  Nhấp vào Ứng dụng ở góc trên bên trái của Màn hình và điều hướng đến Pentesting \--\> Thu thập Thông tin \--\> wireshark.

> ![Screenshot](media/image2.jpeg){width="10.6625in" height="8.0in"}

3.  Một cửa sổ bật lên bảo mật xuất hiện, xác thực bằng cách cung cấp toor làm mật khẩu.

4.  Cửa sổ Wireshark Network Analyzer xuất hiện, bắt đầu ghi lại lưu lượng mạng trên giao diện mạng chính (ở đây là eth0).

> ![Screenshot](media/image3.jpeg){width="10.6625in" height="8.0in"}

5.  Giữ ứng dụng Wireshark đang chạy.

6.  Mở một cửa sổ Terminal và thực thi sudo su để chạy các chương trình với quyền người dùng root (Khi được yêu cầu, nhập mật khẩu toor).

> Mật khẩu mà bạn nhập sẽ không hiển thị.

7.  Bây giờ, chạy lệnh cd để chuyển đến thư mục gốc.

> ![Screenshot](media/image4.jpeg){width="10.6625in" height="8.0in"}

8.  Thực thi macof -i eth0 -n 10 trong thư mục gốc.

> **-i: chỉ định giao diện và -n: chỉ định số lượng gói tin sẽ được gửi (ở đây, 10).**
>
> Bạn cũng có thể nhắm mục tiêu một hệ thống duy nhất bằng cách sử dụng lệnh macof -i eth0 -d \[Địa chỉ IP đích\] (-d: Chỉ định địa chỉ IP đích).

9.  Lệnh này sẽ bắt đầu làm đầy bảng CAM với các địa chỉ MAC ngẫu nhiên, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image5.jpeg){width="10.6625in" height="8.0in"}

10. Chuyển sang cửa sổ Wireshark và quan sát các gói IPv4 từ các địa chỉ IP ngẫu nhiên.

11. Nhấp vào bất kỳ gói IPv4 nào đã được chụp và mở rộng nút Ethernet II trong phần chi tiết gói. Thông tin về địa chỉ MAC nguồn và đích sẽ được hiển thị, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image6.jpeg){width="10.6625in" height="8.0in"}

12. Tương tự, bạn có thể chuyển sang một máy khác để xem cùng các gói tin đã được Wireshark ghi lại trên máy Parrot Security.

13. Macof gửi các gói dữ liệu với địa chỉ MAC và IP ngẫu nhiên đến tất cả các máy đang hoạt động trong mạng cục bộ. Nếu bạn sử dụng nhiều mục tiêu, bạn sẽ quan sát thấy các gói dữ liệu giống nhau trên tất cả các máy mục tiêu.

14. Đóng cửa sổ Wireshark. Nếu xuất hiện pop-up \'Gói dữ liệu chưa được lưu\...\', hãy nhấp vào \'Dừng và Thoát mà không Lưu\' để đóng ứng dụng Wireshark.

> ![Screenshot](media/image7.jpeg){width="10.6625in" height="8.0in"}

15. Điều này kết thúc phần trình bày về cách thực hiện tấn công tràn MAC bằng macof.

16. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 8.1.1.1**

Sử dụng macof trên máy Parrot Security để thực hiện tràn MAC trên máy mục tiêu Windows 11. Kích thước mặc định của các gói IP mà macof sử dụng để tràn bảng CAM với địa chỉ MAC ngẫu nhiên là bao nhiêu?

![](media/image8.wmf)

Sai

Nhiệm vụ 2: Thực hiện tấn công cạn kiệt DHCP bằng Yersinia

Trong một cuộc tấn công cạn kiệt DHCP, kẻ tấn công làm tràn máy chủ DHCP bằng cách gửi một số lượng lớn các yêu cầu DHCP và sử dụng tất cả các địa chỉ IP có sẵn mà máy chủ DHCP có thể cấp. Kết quả là, máy chủ không thể cấp thêm địa chỉ IP nào nữa, dẫn đến một cuộc tấn công Từ chối Dịch vụ (DoS). Vì vấn đề này, người dùng hợp pháp không thể lấy hoặc gia hạn địa chỉ IP của họ, và do đó không thể truy cập mạng của họ. Cuộc tấn công này có thể được thực hiện bằng cách sử dụng các công cụ khác nhau như Yersinia và Hyenae.

Yersinia là một công cụ mạng được thiết kế để tận dụng các điểm yếu trong các giao thức mạng khác nhau như DHCP. Nó giả vờ là một khung vững chắc để phân tích và kiểm tra các mạng và hệ thống đã triển khai.

Ở đây, chúng tôi sẽ sử dụng công cụ Yersinia để thực hiện một cuộc tấn công cạn kiệt DHCP trên hệ thống mục tiêu.

1.  Trên máy Parrot Security, khởi chạy Wireshark và bắt đầu bắt gói tin trên cổng ethernet hoặc giao diện khả dụng (ở đây là eth0).

> ![Screenshot](media/image9.jpeg){width="10.6625in" height="8.0in"}

2.  Giữ ứng dụng Wireshark đang chạy.

3.  Mở một cửa sổ Terminal và thực thi sudo su để chạy các chương trình với quyền người dùng root (Khi được yêu cầu, nhập mật khẩu toor). Chạy cd để điều hướng đến thư mục gốc.

> Nhấp vào biểu tượng Tối đa cửa sổ để làm tối đa cửa sổ terminal.
>
> Chế độ tương tác của ứng dụng Yersinia chỉ hoạt động trong cửa sổ terminal được phóng to tối đa.

4.  Chạy yersinia -I để mở Yersinia ở chế độ tương tác.

> **-I: Bắt đầu một phiên tương tác.**
>
> ![Screenshot](media/image10.jpeg){width="10.6625in" height="8.0in"}

5.  Chế độ tương tác Yersinia xuất hiện trong cửa sổ terminal.

6.  Để loại bỏ cửa sổ Thông báo, nhấn bất kỳ phím nào, sau đó nhấn h để được trợ giúp.

7.  Tùy chọn Lệnh có sẵn xuất hiện, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image11.jpeg){width="10.6625in" height="8.0in"}

8.  Nhấn phím q để thoát khỏi các tùy chọn trợ giúp.

9.  Nhấn F2 để chọn chế độ DHCP. Trong chế độ DHCP, các Trường STP ở phần dưới của cửa sổ sẽ đổi thành các Trường DHCP, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image12.jpeg){width="10.6625in" height="8.0in"}

10. Nhấn x để liệt kê các lựa chọn tấn công có sẵn.

11. Cửa sổ Attack Panel xuất hiện; nhấn 1 để bắt đầu một cuộc tấn công cạn kiệt DHCP.

> ![Screenshot](media/image13.jpeg){width="10.6625in" height="8.0in"}

12. Yersinia bắt đầu gửi các gói DHCP tới giao diện mạng như hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image14.jpeg){width="10.6625in" height="8.0in"}

13. Sau vài giây, nhấn q để dừng cuộc tấn công và kết thúc Yersinia, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image15.jpeg){width="10.6625in" height="8.0in"}

14. Bây giờ, chuyển sang cửa sổ Wireshark và quan sát số lượng lớn các gói DHCP được bắt, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image16.jpeg){width="10.6625in" height="8.0in"}

15. Nhấp vào bất kỳ gói DHCP nào và mở rộng nút Ethernet II trong phần chi tiết gói. Thông tin về địa chỉ MAC nguồn và đích được hiển thị, như trong ảnh chụp màn hình.

> ![Screenshot](media/image17.jpeg){width="10.6625in" height="8.0in"}

16. Đóng cửa sổ Wireshark. Nếu xuất hiện hộp thoại Unsaved packets..., hãy nhấp vào Stop và Quit without Saving.

17. Điều này kết thúc phần trình diễn cách thực hiện tấn công cạn kiệt DHCP bằng Yersinia.

18. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 8.1.2.1**

Sử dụng Yersinia trên máy Parrot Security để thực hiện một cuộc tấn công cạn kiệt DHCP. Cổng nguồn mặc định được Yersinia sử dụng trong chế độ DHCP là gì?

Thí nghiệm 2: Thực hiện bắt gói tin mạng sử dụng các công cụ bắt gói tin khác nhau

**kịch bản bài lab bài lab**

Dữ liệu truyền qua kênh HTTP chảy ở định dạng văn bản thuần túy và do đó dễ bị các cuộc tấn công MITM. Quản trị viên mạng có thể sử dụng công cụ sniffing với mục đích hữu ích như để khắc phục sự cố mạng, kiểm tra các vấn đề an ninh và gỡ lỗi các triển khai giao thức. Tuy nhiên, một kẻ tấn công có thể sử dụng các công cụ sniffing như Wireshark để dò tìm lưu lượng dữ liệu giữa client và server. Lưu lượng dữ liệu mà kẻ tấn công thu được có thể chứa thông tin nhạy cảm như thông tin đăng nhập, từ đó có thể được sử dụng để thực hiện các hoạt động độc hại như mạo danh phiên người dùng.

Một kẻ tấn công cần phải thao túng chức năng của switch để xem tất cả lưu lượng đi qua nó. Một chương trình bắt gói tin (còn được gọi là sniffer) chỉ có thể chụp các gói dữ liệu từ một mạng con nhất định, có nghĩa là nó không thể bắt các gói từ mạng khác. Thường thì một laptop bất kỳ có thể cắm vào mạng và truy cập vào mạng đó. Nhiều doanh nghiệp để các cổng switch của họ mở. Một trình sniffer đặt trên mạng ở chế độ promiscuous có thể chụp và phân tích tất cả lưu lượng mạng. Các chương trình sniffer tắt bộ lọc được sử dụng bởi card giao diện mạng Ethernet (NIC) để ngăn máy chủ nhìn thấy lưu lượng của các trạm khác. Do đó, các chương trình sniffer có thể nhìn thấy lưu lượng của mọi người.

Thông tin thu thập được ở bước trước có thể không đủ để tiết lộ các điểm yếu tiềm ẩn của mục tiêu. Có thể có thêm thông tin giúp tìm ra các lỗ hổng trong mục tiêu. Một hacker đạo đức cần thực hiện các đánh giá bảo mật mạng và đề xuất các kỹ thuật khắc phục phù hợp để giảm thiểu các cuộc tấn công. Thí nghiệm này cung cấp trải nghiệm thực hành về cách sử dụng các công cụ sniffing để theo dõi lưu lượng mạng và ghi lại nó trên một giao diện từ xa.

**Mục tiêu bài lab**

-   Thực hiện theo dõi mật khẩu bằng Wireshark

**Tổng quan về các công cụ nghe lén mạng**

Các quản trị viên hệ thống sử dụng các công cụ tự động để giám sát mạng của họ, nhưng những kẻ tấn công lạm dụng các công cụ này để nghe trộm dữ liệu mạng. Các công cụ nghe trộm mạng có thể được sử dụng để thực hiện phân tích mạng chi tiết. Khi bảo vệ một mạng, điều quan trọng là phải có càng nhiều chi tiết về lưu lượng gói tin càng tốt. Bằng cách quét mạng một cách chủ động, một thợ săn mối đe dọa có thể duy trì sự cảnh giác và phản ứng nhanh chóng với các cuộc tấn công.

Nhiệm vụ 1: Thực hiện Sniffing Mật khẩu sử dụng Wireshark

Wireshark là một công cụ phân tích gói mạng được sử dụng để bắt các gói mạng và hiển thị dữ liệu gói một cách chi tiết. Công cụ này sử dụng Winpcap để tự bắt các gói trên các mạng được hỗ trợ. Nó nắm bắt lưu lượng mạng trực tiếp từ các mạng Ethernet, IEEE 802.11, PPP/HDLC, ATM, Bluetooth, USB, Token Ring, Frame Relay và FDDI. Các tệp đã bắt có thể được chỉnh sửa theo chương trình thông qua dòng lệnh. Một bộ lọc để hiển thị dữ liệu tùy chỉnh có thể được tinh chỉnh bằng cách sử dụng bộ lọc hiển thị.

Ở đây, chúng ta sẽ sử dụng công cụ Wireshark để thực hiện việc nghe trộm mật khẩu.

Trong nhiệm vụ này, chúng ta sẽ sử dụng máy Windows Server 2019 (10.10.1.19) làm máy chủ và máy Windows 11 (10.10.1.11) làm máy mục tiêu.

1.  Nhấp vào Windows Server 2019 để chuyển sang máy Windows Server 2019 và đăng nhập bằng Administrator/Pa\$\$w0rd.[Windows Server 2019](https://labclient.labondemand.com/Instructions/e24ba80f-a3b3-42e8-9ac3-e74faaa4fc16)

> Màn hình Mạng xuất hiện, nhấp vào Có để cho phép PC của bạn có thể được các PC và thiết bị khác trên mạng phát hiện.

2.  Tìm Wireshark từ thanh tìm kiếm và khởi chạy nó.

> Nếu cửa sổ Cập nhật Phần mềm xuất hiện, nhấp vào Nhắc tôi sau.

3.  Cửa sổ Wireshark Network Analyzer xuất hiện, bắt đầu bắt lưu lượng mạng trên giao diện mạng chính (ở đây là Ethernet 2).

4.  Wireshark bắt đầu ghi lại tất cả các gói được tạo ra trong khi lưu lượng được nhận bởi hoặc gửi từ máy của bạn.

> ![zzzz.jpg](media/image18.jpeg){width="10.6625in" height="8.0in"}

5.  Bây giờ, bấm vào Windows 11 để chuyển sang máy Windows 11, đăng nhập bằng Admin/Pa\$\$w0rd.[Windows 11](https://labclient.labondemand.com/Instructions/e24ba80f-a3b3-42e8-9ac3-e74faaa4fc16)

> Ngoài ra, bạn cũng có thể nhấp vào Pa\$\$w0rd dưới hình thu nhỏ máy Windows 11 trong ngăn Tài nguyên.
>
> Nếu trình hướng dẫn Chào mừng đến với Windows xuất hiện, hãy nhấn Tiếp tục và trong trình hướng dẫn Đăng nhập bằng Microsoft, nhấn Hủy.
>
> Màn hình Mạng xuất hiện, nhấp vào Có để cho phép PC của bạn có thể được các PC và thiết bị khác trên mạng phát hiện.

6.  Mở bất kỳ trình duyệt web nào, và truy cập http://www.moviescope.com/ (ở đây, chúng tôi đang sử dụng Mozilla Firefox).

7.  Trang chủ MOVIESCOPE xuất hiện; đăng nhập bằng sam/test.

> ![Screenshot](media/image19.jpeg){width="10.6625in" height="8.0in"}

8.  Nhấp vào Windows Server 2019 để quay lại máy Windows Server 2019, và trong cửa sổ Wireshark, nhấp vào biểu tượng Dừng bắt gói trên thanh công cụ.[Windows Server 2019](https://labclient.labondemand.com/Instructions/e24ba80f-a3b3-42e8-9ac3-e74faaa4fc16)

> ![Screenshot](media/image20.jpeg){width="10.6625in" height="8.0in"}

9.  Nhấp vào Tệp \--\> Lưu Như... ở góc trên bên trái của cửa sổ để lưu các gói tin đã chụp.

> ![Screenshot](media/image21.jpeg){width="10.6625in" height="8.0in"}

10. Cửa sổ Wireshark: Lưu Tệp Ghi Nhận Dư Liệu Xuất Hiện. Chọn bất kỳ vị trí nào để lưu tệp, đặt Tên tệp là Password Sniffing, và nhấp Lưu.

> ![L2T1S10.jpg](media/image22.jpeg){width="10.6625in" height="8.0in"}

11. Trong trường Áp dụng bộ lọc hiển thị, hãy gõ http.request.method == POST và nhấp vào biểu tượng mũi tên (\--\> ) để áp dụng bộ lọc.

> Áp dụng cú pháp này giúp bạn thu hẹp tìm kiếm cho lưu lượng HTTP POST.

12. Wireshark chỉ lọc các gói lưu lượng http POST, như hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image23.jpeg){width="10.6625in" height="8.0in"}

13. Bây giờ, điều hướng đến Chỉnh sửa \--\> Tìm gói từ thanh menu.

> ![Screenshot](media/image24.jpeg){width="10.6625in" height="8.0in"}

14. Phần Tìm Gói xuất hiện bên dưới trường bộ lọc hiển thị.

15. Nhấp vào Bộ lọc hiển thị, chọn Chuỗi từ các tùy chọn thả xuống, nhấp vào Hẹp & Rộng và chọn Hẹp (UTF-8 / ASCII) từ các tùy chọn thả xuống và nhấp vào Danh sách gói tin, chọn Chi tiết gói tin từ các tùy chọn thả xuống.

16. Trong trường bên cạnh String, gõ pwd và nhấp vào nút Find.

> ![2.1.16.jpg](media/image25.jpeg){width="10.6625in" height="8.0in"}

17. Wireshark bây giờ sẽ hiển thị mật khẩu đã bị đánh cắp từ các gói tin đã được bắt.

18. Mở rộng nút HTML Form URL Encoded: application/x-www-form-urlencoded từ phần chi tiết gói, và xem tên người dùng và mật khẩu đã được ghi lại, như hiển thị trong ảnh chụp màn hình.

> ![2.1.18.jpg](media/image26.jpeg){width="10.6625in" height="8.0in"}

19. Đóng cửa sổ Wireshark.

20. Nhấp vào Windows 11 để chuyển sang máy Windows 11, đóng trình duyệt web và đăng xuất khỏi tài khoản Admin.[Windows 11](https://labclient.labondemand.com/Instructions/e24ba80f-a3b3-42e8-9ac3-e74faaa4fc16)

> ![Screenshot](media/image27.jpeg){width="10.6625in" height="8.0in"}

21. Nhấp vào Windows Server 2019 để chuyển trở lại máy Windows Server 2019.[Windows Server 2019](https://labclient.labondemand.com/Instructions/e24ba80f-a3b3-42e8-9ac3-e74faaa4fc16)

22. Tìm kiếm Kết nối Máy tính Từ xa từ thanh tìm kiếm và khởi chạy nó.

23. Hộp thoại Kết nối Màn hình Từ xa xuất hiện; nhấp vào Hiển thị Tùy chọn.

> Nếu một địa chỉ IP đã truy cập trước đó xuất hiện trong trường Máy tính, hãy xóa nó.
>
> ![Screenshot](media/image28.jpeg){width="10.6625in" height="8.0in"}

24. Hộp thoại mở rộng; dưới tab Chung, nhập 10.10.1.11 vào ô Máy tính và Jason vào ô Tên người dùng; nhấp vào Kết nối.

> Địa chỉ IP và tên đăng nhập có thể khác trong môi trường bài lab của bạn. Thông tin đăng nhập hệ thống mục tiêu (Jason và qwerty) mà chúng tôi đang sử dụng ở đây được lấy trong các bài lab trước đó.
>
> ![Screenshot](media/image29.jpeg){width="10.6625in" height="8.0in"}

25. Cửa sổ bật lên Bảo mật Windows xuất hiện. Nhập Mật khẩu (qwerty) và nhấn OK.

> Nếu tùy chọn \'Ghi nhớ tôi\' được chọn, hãy bỏ chọn nó.
>
> ![Screenshot](media/image30.jpeg){width="10.6625in" height="8.0in"}

26. Cửa sổ bật lên Kết nối Máy tính Từ xa xuất hiện; nhấp vào Có.

> ![Screenshot](media/image31.jpeg){width="10.6625in" height="8.0in"}

27. Một kết nối từ xa tới hệ thống mục tiêu (Windows 11) xuất hiện.

> Nếu một cửa sổ Chọn cài đặt quyền riêng tư cho thiết bị của bạn xuất hiện, nhấp vào Tiếp theo, trong cửa sổ tiếp theo nhấp vào Tiếp theo và trong cửa sổ tiếp theo nhấp vào Chấp nhận.

28. Trong cửa sổ Máy tính để bàn, nhấp vào biểu tượng Tìm kiếm của Windows và tìm kiếm Bảng điều khiển trong thanh tìm kiếm và khởi chạy nó.

29. Cửa sổ Bảng điều khiển xuất hiện; điều hướng tới Hệ thống và Bảo mật \--\> Công cụ Windows. Trong bảng điều khiển Công cụ Windows, nhấp đúp vào Dịch vụ.

> ![Screenshot](media/image32.jpeg){width="10.6625in" height="8.0in"}

30. Cửa sổ Dịch vụ xuất hiện. Chọn Remote Packet Capture Protocol v.0 (experimental), nhấp chuột phải vào dịch vụ, và nhấp Bắt đầu.

> ![Screenshot](media/image33.jpeg){width="10.6625in" height="8.0in"}

31. Trạng thái của dịch vụ Giao thức Ghi gói từ xa v.0 (thử nghiệm) sẽ chuyển sang Đang chạy, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image34.jpeg){width="10.6625in" height="8.0in"}

32. Đóng tất cả các cửa sổ đang mở trên máy Windows 11 và đóng Kết nối Máy tính Từ xa.

> Nếu một cửa sổ bật lên kết nối Máy tính Từ xa xuất hiện, hãy nhấp vào OK.

33. Bây giờ, trong Windows Server 2019, mở Wireshark và nhấp vào biểu tượng Tùy chọn Ghi lại trên thanh công cụ.

> ![23ddd.jpg](media/image35.jpeg){width="10.6625in" height="8.0in"}

34. Cửa sổ Tùy chọn Bắt gói Wireshark xuất hiện; nhấp vào nút Quản lý Giao diện...

> ![Screenshot](media/image36.jpeg){width="10.6625in" height="8.0in"}

35. Cửa sổ Quản lý Giao diện xuất hiện; nhấp vào tab Giao diện Từ xa, sau đó nhấp vào biểu tượng Thêm máy chủ từ xa và giao diện của nó (+).

> ![12121.jpg](media/image37.jpeg){width="10.6625in" height="8.0in"}

36. Cửa sổ Giao diện Từ xa xuất hiện. Trong trường văn bản Máy chủ, nhập địa chỉ IP của máy mục tiêu (ở đây là 10.10.1.11); và trong trường Cổng, nhập số cổng là 2002.

37. Trong phần Xác thực, chọn nút radio Xác thực bằng Mật khẩu và nhập thông tin đăng nhập của máy mục tiêu (ở đây là Jason và qwerty); nhấn OK.

> Địa chỉ IP và thông tin đăng nhập người dùng có thể khác nhau khi bạn thực hiện tác vụ này.
>
> ![Screenshot](media/image38.jpeg){width="10.6625in" height="8.0in"}

38. Một giao diện từ xa mới được thêm vào cửa sổ Quản lý Giao diện; nhấp vào OK.

> ![Screenshot](media/image39.jpeg){width="10.6625in" height="8.0in"}

39. Giao diện từ xa mới được thêm xuất hiện trong cửa sổ Tùy chọn Ghi lại của Wireshark; nhấp vào Bắt đầu.

> ![Screenshot](media/image40.jpeg){width="10.6625in" height="8.0in"}

40. Nhấp vào Windows 11 để chuyển sang máy Windows 11, và đăng nhập bằng Jason/qwerty. Ở đây, bạn đang đăng nhập với tư cách là nạn nhân.[Windows 11](https://labclient.labondemand.com/Instructions/e24ba80f-a3b3-42e8-9ac3-e74faaa4fc16)

41. Đóng vai trò là mục tiêu, mở bất kỳ trình duyệt web nào và truy cập http://www.goodshopping.com (ở đây, chúng tôi đang sử dụng Mozilla Firefox).

> Mặc dù chúng ta chỉ đang duyệt Internet ở đây, bạn cũng có thể đăng nhập vào tài khoản của mình và sniff các thông tin đăng nhập.
>
> ![Screenshot](media/image41.jpeg){width="10.6625in" height="8.0in"}

42. Nhấp vào Windows Server 2019 để chuyển trở lại máy Windows Server 2019. Wireshark bắt đầu ghi lại các gói dữ liệu ngay khi người dùng (ở đây là bạn) bắt đầu duyệt Internet, như hiển thị trong ảnh chụp màn hình.[Windows Server 2019](https://labclient.labondemand.com/Instructions/e24ba80f-a3b3-42e8-9ac3-e74faaa4fc16)

> ![Screenshot](media/image42.jpeg){width="10.6625in" height="8.0in"}

43. Sau một thời gian, nhấp vào biểu tượng Dừng bắt gói trên thanh công cụ để dừng việc bắt gói trực tiếp.

44. Bằng cách này, bạn có thể sử dụng Wireshark để bắt lưu lượng trên một giao diện từ xa.

> Trong thời gian thực, khi kẻ tấn công có được thông tin đăng nhập của máy nạn nhân, họ cố gắng chiếm quyền giao diện từ xa của nó và giám sát lưu lượng mà người dùng duyệt để tiết lộ thông tin bí mật của người dùng.

45. Điều này kết thúc buổi trình diễn cách thực hiện việc bắt mật khẩu bằng Wireshark.

46. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 8.2.1.1**

Sử dụng công cụ Wireshark để thực hiện việc nghe trộm mật khẩu. Bộ lọc hiển thị Wireshark nào hiển thị lưu lượng HTTP POST?

![](media/image8.wmf)

Thí nghiệm 3: Phát hiện theo dõi mạng

**kịch bản bài lab bài lab**

Các bài lab trước đã chứng minh cách một kẻ tấn công thực hiện nghe trộm bằng các kỹ thuật và công cụ khác nhau. bài lab này giúp bạn hiểu các kỹ thuật phòng thủ có thể được sử dụng để bảo vệ mạng mục tiêu khỏi các cuộc tấn công nghe trộm.

Một hacker đạo đức chuyên nghiệp hoặc chuyên gia kiểm thử xâm nhập nên có khả năng phát hiện việc rình nghe mạng trong mạng. Một công cụ rình nghe trên mạng chỉ thu thập dữ liệu và chạy ở chế độ promiscuous, vì vậy nó không dễ bị phát hiện. Chế độ promiscuous cho phép thiết bị mạng chặn và đọc từng gói dữ liệu mạng khi chúng đến đầy đủ. Công cụ rình nghe không để lại dấu vết, vì nó không truyền dữ liệu. Do đó, để phát hiện các nỗ lực rình nghe, bạn phải sử dụng các kỹ thuật và công cụ phát hiện rình nghe mạng khác nhau được thảo luận trong bài thực hành này.

**Mục tiêu bài lab**

-   Phát hiện tấn công ARP và chế độ promiscuous trong mạng dựa trên switch

**Tổng quan về Phát hiện Đánh hơi Mạng**

Sniffing mạng liên quan đến việc sử dụng các công cụ sniffer cho phép giám sát và phân tích gói dữ liệu theo thời gian thực trên các mạng máy tính. Các sniffer mạng này có thể được phát hiện bằng cách sử dụng các kỹ thuật khác nhau như:

-   **Phương pháp Ping: Xác định xem một hệ thống trên mạng có đang chạy ở chế độ lắng nghe toàn bộ hay không**

-   **Phương pháp DNS: Xác định các thiết bị nghe lén trong mạng bằng cách phân tích sự tăng lưu lượng mạng**

-   **Phương pháp ARP: Gửi một ARP không phát sóng đến tất cả các nút trong mạng; một nút trên mạng chạy ở chế độ promiscuous sẽ lưu trữ địa chỉ ARP cục bộ**

Nhiệm vụ 1: Phát hiện ARP Poisoning và Chế độ Promiscuous trong Mạng Dựa trên Switch

ARP poisoning liên quan đến việc giả mạo nhiều gói ARP request và reply để làm quá tải một switch. ARP cache poisoning là phương pháp tấn công mạng LAN bằng cách cập nhật bộ nhớ đệm ARP của máy tính mục tiêu với cả gói ARP request và reply giả mạo nhằm thay đổi địa chỉ MAC Ethernet Lớp 2 (của card mạng) thành địa chỉ mà kẻ tấn công có thể theo dõi. Kẻ tấn công sử dụng ARP poisoning để nghe lén trên mạng mục tiêu. Như vậy, kẻ tấn công có thể đánh cắp thông tin nhạy cảm, ngăn chặn truy cập mạng và web, và thực hiện các cuộc tấn công DoS và MITM.

Chế độ promiscuous cho phép một thiết bị mạng chặn và đọc từng gói mạng đến một cách toàn bộ. Bộ ngắt gói (sniffer) chuyển NIC của một hệ thống sang chế độ promiscuous, để nó lắng nghe tất cả dữ liệu truyền trên phân đoạn của nó. Một bộ ngắt gói có thể liên tục giám sát tất cả lưu lượng mạng tới máy tính thông qua NIC bằng cách giải mã thông tin được đóng gói trong gói dữ liệu. Chế độ promiscuous trong mạng có thể được phát hiện bằng nhiều công cụ khác nhau.

Hacker đạo đức và kiểm thử xâm nhập phải đánh giá tổ chức hoặc mục tiêu kiểm tra để tìm các lỗ hổng nhiễm độc ARP.

Ở đây, chúng tôi sẽ phát hiện việc tấn công ARP trong một mạng dựa trên switch bằng Wireshark và chúng tôi sẽ sử dụng Công cụ Lập trình Kịch bản Nmap (NSE) để kiểm tra xem liệu một hệ thống trên Ethernet cục bộ có đang đặt card mạng ở chế độ promiscuous hay không.

Trong nhiệm vụ này, chúng ta sẽ sử dụng máy Windows Server 2019 làm máy chủ để thực hiện ARP poisoning, và sẽ theo dõi lưu lượng giữa các máy Windows 11 và Parrot Security. Chúng ta sẽ sử dụng cùng một máy (Windows Server 2019) để phát hiện ARP poisoning và sử dụng máy Windows 11 để phát hiện chế độ promiscuous trong mạng.

1.  Nhấp vào Windows Server 2019 để chuyển sang máy Windows Server 2019.[Windows Server 2019](https://labclient.labondemand.com/Instructions/e24ba80f-a3b3-42e8-9ac3-e74faaa4fc16)

2.  Trong cửa sổ Máy tính để bàn, nhấp vào biểu tượng Tìm kiếm của Windows và tìm kiếm \'cain\' trong thanh tìm kiếm rồi khởi chạy nó.

3.  Cửa sổ chính của Cain & Abel xuất hiện, nhấp vào Cấu hình từ thanh menu để cấu hình card ethernet.

> ![Screenshot](media/image43.jpeg){width="10.6625in" height="8.0in"}

4.  Cửa sổ Hộp thoại Cấu hình xuất hiện. Tab Sniffer được chọn theo mặc định. Đảm bảo rằng Bộ điều hợp liên kết với địa chỉ IP của máy được chọn và nhấp vào OK.

> ![Screenshot](media/image44.jpeg){width="10.6625in" height="8.0in"}

5.  Nhấp vào biểu tượng Start/Stop Sniffer trên thanh công cụ để bắt đầu quá trình sniffing.

> ![dg.jpg](media/image45.jpeg){width="10.6625in" height="8.0in"}

6.  Cửa sổ bật lên Cain xuất hiện với thông báo Cảnh báo, bấm OK.

7.  Bây giờ, nhấp vào tab Sniffer.

8.  Nhấp vào biểu tượng cộng (+) hoặc nhấp chuột phải trong cửa sổ và chọn Quét Địa chỉ MAC để quét mạng tìm các thiết bị.

9.  Cửa sổ Quét Địa chỉ MAC xuất hiện. Chọn nút radio Tất cả các máy chủ trong mạng con của tôi. Chọn hộp kiểm Tất cả Kiểm tra; sau đó, nhấp OK.

> ![Screenshot](media/image46.jpeg){width="10.6625in" height="8.0in"}

10. Cain & Abel bắt đầu quét các địa chỉ MAC và liệt kê tất cả những địa chỉ được tìm thấy.

11. Sau khi quét xong, một danh sách tất cả các địa chỉ IP đang hoạt động cùng với địa chỉ MAC tương ứng của chúng được hiển thị, như được trình bày trong ảnh chụp màn hình.

> ![Screenshot](media/image47.jpeg){width="10.6625in" height="8.0in"}

12. Bây giờ, nhấp vào tab APR ở dưới cùng của cửa sổ.

13. Các tùy chọn APR xuất hiện ở khung bên trái. Nhấp vào bất kỳ đâu trong phần trên cùng ở khung bên phải để kích hoạt biểu tượng cộng (+).

> ![fgd.jpg](media/image48.jpeg){width="10.6625in" height="8.0in"}

14. Nhấp vào biểu tượng cộng (+); một cửa sổ ARP Poison Routing Mới xuất hiện; từ đó chúng ta có thể thêm IP để nghe lưu lượng.

15. Để giám sát lưu lượng giữa hai hệ thống (ở đây là Windows 11 và Parrot Security), từ ngăn bên trái, nhấp để chọn 10.10.1.11 (Windows 11) và từ ngăn bên phải, nhấp 10.10.1.13 (Parrot Security); nhấp OK. Bằng cách này, bạn đang cài đặt Cain thực hiện tấn công ARP giữa mục tiêu thứ nhất và thứ hai.

> ![Screenshot](media/image49.jpeg){width="10.6625in" height="8.0in"}

16. Nhấp để chọn quét địa chỉ IP đích đã tạo được hiển thị trong tab Cấu hình / Gói đã định tuyến.

17. Nhấp vào biểu tượng Start/Stop APR để bắt đầu ghi lại các gói ARP.

18. Sau khi nhấn vào biểu tượng Bắt đầu/Dừng APR, Cain & Abel bắt đầu tấn công ARP và trạng thái quét thay đổi thành Đang tấn công, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image50.jpeg){width="10.6625in" height="8.0in"}

19. Cain & Abel chặn lưu lượng đi qua giữa hai máy này.

20. Để tạo lưu lượng giữa các máy, bạn cần ping một máy mục tiêu bằng máy còn lại.

21. Nhấp vào Parrot Security để chuyển sang máy Parrot Security.[Parrot Security](https://labclient.labondemand.com/Instructions/e24ba80f-a3b3-42e8-9ac3-e74faaa4fc16)

22. Mở một cửa sổ Terminal và thực thi sudo su để chạy các chương trình với quyền người dùng root (Khi được yêu cầu, nhập mật khẩu toor). Chạy lệnh cd để chuyển đến thư mục gốc.

23. Chạy lệnh hping3 \[Địa chỉ IP mục tiêu\] -c 100000 (ở đây, địa chỉ IP mục tiêu là 10.10.1.11 \[Windows 11\]).

> **-c: chỉ định số lượng gói tin.**

24. Lệnh này sẽ bắt đầu gửi ping đến máy mục tiêu (Windows 11) với 100.000 gói dữ liệu.

> ![Screenshot](media/image51.jpeg){width="10.6625in" height="8.0in"}

25. Giữ lệnh đang chạy và ngay lập tức nhấp vào Windows Server 2019 để chuyển sang máy Windows Server 2019.[Windows Server 2019](https://labclient.labondemand.com/Instructions/e24ba80f-a3b3-42e8-9ac3-e74faaa4fc16)

26. Trong cửa sổ Máy tính để bàn, nhấp vào biểu tượng Tìm kiếm của Windows và tìm kiếm wireshark trong thanh tìm kiếm và khởi chạy nó.

27. Cửa sổ Phân tích Mạng Wireshark xuất hiện; nhấp vào Chỉnh sửa trên thanh menu và chọn Tùy chọn...

> ![Screenshot](media/image52.jpeg){width="10.6625in" height="8.0in"}

28. Cửa sổ Wireshark . Preferences xuất hiện; mở rộng nút Protocols.

29. Cuộn xuống trong nút Protocols và chọn tùy chọn ARP/RARP.

30. Từ ngăn bên phải, nhấp vào hộp kiểm Phát hiện cơn bão ARP và đảm bảo rằng hộp kiểm Phát hiện cấu hình địa chỉ IP trùng lặp được chọn; nhấp vào OK.

> ![Screenshot](media/image53.jpeg){width="10.6625in" height="8.0in"}

31. Bây giờ, nhấp đúp vào adapter liên quan đến mạng của bạn (ở đây là Ethernet2) để bắt đầu ghi lại các gói mạng.

> ![Screenshot](media/image54.jpeg){width="10.6625in" height="8.0in"}

32. Wireshark bắt đầu bắt lưu lượng giữa hai máy, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image55.jpeg){width="10.6625in" height="8.0in"}

33. Chuyển sang cửa sổ Cain & Abel để quan sát các gói dữ liệu đang di chuyển giữa hai máy.

> ![Screenshot](media/image56.jpeg){width="10.6625in" height="8.0in"}

34. Bây giờ, chuyển sang Wireshark và nhấp vào biểu tượng Dừng bắt gói để dừng việc bắt gói.

35. Nhấp vào Analyze từ thanh menu và chọn Expert Information từ các tùy chọn thả xuống. Cửa sổ Wireshark . Expert Information xuất hiện; nhấp để mở rộng nút Warning được gắn nhãn Duplicate IP address configured (10.10.1.11), đang chạy trên giao thức ARP/RARP.

> ![Screenshot](media/image57.jpeg){width="10.6625in" height="8.0in"}

36. Sắp xếp cửa sổ Thông tin Chuyên gia của Wireshark phía trên cửa sổ Wireshark để bạn có thể xem số gói và phần Chi tiết gói.

37. Trong cửa sổ Thông tin Chuyên gia của Wireshark, nhấp vào bất kỳ gói nào (ở đây, 463).

> ![Screenshot](media/image58.jpeg){width="10.6625in" height="8.0in"}

38. Khi chọn số gói tin, Wireshark sẽ làm nổi bật gói tin, và thông tin liên quan được hiển thị trong phần chi tiết gói tin. Đóng cửa sổ Thông tin Chuyên viên của Wireshark.

39. Các cảnh báo được đánh dấu màu vàng cho thấy đã phát hiện địa chỉ IP trùng lặp tại một địa chỉ MAC, như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image59.jpeg){width="10.6625in" height="8.0in"}
>
> Tấn công ARP spoofing thành công bằng cách thay đổi địa chỉ IP của máy tính của kẻ tấn công thành địa chỉ IP của máy tính mục tiêu. Trong quá trình này, một gói tin yêu cầu và trả lời ARP giả mạo được đặt vào bộ nhớ cache ARP của mục tiêu. Vì gói tin trả lời ARP đã bị giả mạo, máy tính đích (mục tiêu) sẽ gửi các khung dữ liệu tới máy tính của kẻ tấn công, nơi kẻ tấn công có thể chỉnh sửa các khung dữ liệu trước khi gửi chúng đến máy nguồn (Người dùng A) trong một tấn công MITM. Tại thời điểm này, kẻ tấn công có thể phát động một cuộc tấn công DoS bằng cách liên kết một địa chỉ MAC không tồn tại với địa chỉ IP của cổng hoặc có thể âm thầm theo dõi lưu lượng, sau đó chuyển tiếp nó đến đích mục tiêu.

40. Đây kết thúc phần trình bày về cách phát hiện tấn công ARP trong mạng dựa trên switch.

41. Đóng cửa sổ Wireshark và để tất cả các cửa sổ khác vẫn chạy.

42. Bây giờ, chúng ta sẽ thực hiện phát hiện chế độ promiscuous bằng cách sử dụng Nmap.

43. Bây giờ, nhấp vào Ubuntu để chuyển sang máy Ubuntu và đăng nhập bằng Ubuntu/toor.[Ubuntu](https://labclient.labondemand.com/Instructions/e24ba80f-a3b3-42e8-9ac3-e74faaa4fc16)

44. Trên máy Ubuntu, mở cửa sổ Terminal và thực hiện lệnh sudo su để chạy các chương trình dưới quyền người dùng root (Khi được yêu cầu, nhập mật khẩu toor)

45. Chạy lệnh apt install nmap -y để cài đặt nmap.

> ![Screenshot](media/image60.jpeg){width="10.6625in" height="8.0in"}

46. Chạy nmap \--script=sniffer-detect \[Địa chỉ IP mục tiêu/ Phạm vi Địa chỉ IP\] (ở đây, địa chỉ IP mục tiêu là 10.10.1.19 \[Windows Server 2019\]) để bắt đầu quét.

47. Kết quả quét xuất hiện, hiển thị \'Có khả năng ở chế độ đa lập\' dưới phần \'Kết quả script của máy chủ\'. Điều này cho thấy hệ thống mục tiêu đang ở chế độ đa lập.

> ![nmap.jpg](media/image61.jpeg){width="10.6625in" height="8.0in"}

48. Đóng cửa sổ terminal và ghi lại tất cả thông tin đã thu thập được.

49. Đóng tất cả các cửa sổ đang mở trên tất cả các máy (đảm bảo rằng ARP poisoning không đang chạy trên Windows Server 2019), và ghi lại tất cả thông tin đã thu thập được.

**Câu hỏi 8.3.1.1**

Sử dụng Cain và Abel trên máy Windows Server 2019 để thực hiện ARP poisoning, và quan sát lưu lượng giữa các máy Windows 11 và Parrot Security. Hơn nữa, sử dụng Wireshark trên cùng máy Windows Server 2019 để phát hiện ARP poisoning. Mức độ nghiêm trọng của các gói ARP/RARP được hiển thị trong cửa sổ thông tin chuyên gia của Wireshark là gì?

![](media/image8.wmf)

Câu hỏi 8.3.1.2

Sử dụng Công cụ Kịch bản Nmap (NSE) để kiểm tra xem một hệ thống trên mạng Ethernet cục bộ có đang để card mạng ở chế độ đa tiếp nhận (promiscuous mode) hay không. Kịch bản NSE của Nmap nào phát hiện xem một giao diện mạng có đang ở chế độ đa tiếp nhận không?

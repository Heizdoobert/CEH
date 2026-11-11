**Chương 4: Tầng Mạng: Mặt Phẳng Dữ Liệu (Data Plane)**

Chúng ta đã biết ở chương trước rằng lớp vận chuyển cung cấp nhiều hình thức giao tiếp giữa các tiến trình bằng cách dựa vào dịch vụ giao tiếp giữa máy chủ với máy chủ của lớp mạng. Chúng tôi cũng biết rằng lớp vận chuyển thực hiện như vậy mà không có bất kỳ kiến ​​thức nào về cách lớp mạng thực sự triển khai dịch vụ này. Vì vậy, có lẽ bây giờ bạn đang thắc mắc, điều gì ẩn giấu trong dịch vụ liên lạc giữa các máy chủ, điều gì khiến nó hoạt động?

Trong chương này và chương tiếp theo, chúng ta sẽ tìm hiểu chính xác cách lớp mạng có thể cung cấp dịch vụ liên lạc giữa máy chủ với máy chủ. Chúng ta sẽ thấy rằng không giống như các lớp vận chuyển và ứng dụng, có một phần của lớp mạng trong mỗi máy chủ và bộ định tuyến trong mạng. Do đó, các giao thức lớp mạng nằm trong số những thách thức nhất (và do đó là một trong những giao thức thú vị nhất!) trong ngăn xếp giao thức.

Vì lớp mạng được cho là lớp phức tạp nhất trong ngăn xếp giao thức nên chúng ta sẽ có rất nhiều nền tảng để trình bày ở đây. Thật vậy, có rất nhiều thứ cần đề cập đến nên chúng tôi sẽ đề cập đến lớp mạng trong hai chương. Chúng ta sẽ thấy rằng lớp mạng có thể được phân tách thành hai phần tương tác, mặt phẳng dữ liệu và mặt phẳng điều khiển. Trong Chương 4, trước tiên chúng ta sẽ đề cập đến các chức năng mặt phẳng dữ liệu của lớp mạng---các chức năng của mỗi bộ định tuyến trong lớp mạng xác định cách một datagram (nghĩa là gói lớp mạng) đến trên một trong các liên kết đầu vào của bộ định tuyến được chuyển tiếp đến một trong các liên kết đầu ra của bộ định tuyến đó. Chúng tôi sẽ đề cập đến cả chuyển tiếp IP truyền thống (trong đó việc chuyển tiếp dựa trên địa chỉ đích của gói dữ liệu) và chuyển tiếp tổng quát (trong đó việc chuyển tiếp và các chức năng khác có thể được thực hiện bằng cách sử dụng các giá trị trong một số trường khác nhau trong tiêu đề của gói dữ liệu). Chúng ta sẽ nghiên cứu chi tiết về giao thức IPv4 và IPv6 cũng như địa chỉ. Trong Chương 5, chúng ta sẽ đề cập đến các chức năng mặt phẳng điều khiển của lớp mạng---logic toàn mạng kiểm soát cách định tuyến một gói dữ liệu

**Network Layer: Mặt phẳng dữ liệu**

**CHƯƠNG**

![](media/image1.png){width="5.5in" height="6.930965660542432in"}

![](media/image2.png){width="5.5in" height="0.9567311898512686in"}

giữa các bộ định tuyến dọc theo đường dẫn từ máy chủ nguồn đến máy chủ đích. Chúng tôi sẽ đề cập đến các thuật toán định tuyến cũng như các giao thức định tuyến, chẳng hạn như OSPF và BGP, được sử dụng rộng rãi trên Internet ngày nay. Theo truyền thống, các giao thức định tuyến mặt phẳng điều khiển và các chức năng chuyển tiếp mặt phẳng dữ liệu này đã được triển khai cùng nhau, nguyên khối trong một bộ định tuyến. Mạng được xác định bằng phần mềm (SDN) phân tách rõ ràng mặt phẳng dữ liệu và mặt phẳng điều khiển bằng cách triển khai các chức năng mặt phẳng điều khiển này như một dịch vụ riêng biệt, thường là trong một "bộ điều khiển" từ xa. Chúng tôi cũng sẽ đề cập đến bộ điều khiển SDN trong Chương 5.

Sự khác biệt giữa các chức năng mặt phẳng dữ liệu và mặt phẳng điều khiển trong lớp mạng là một khái niệm quan trọng cần ghi nhớ khi bạn tìm hiểu về lớp mạng - nó sẽ giúp cấu trúc suy nghĩ của bạn về lớp mạng và phản ánh quan điểm hiện đại về vai trò của lớp mạng trong mạng máy tính.

**4.1 Tổng quan về Network Layer**

Hình 4.1 cho thấy một mạng đơn giản với hai máy chủ H1 và H2 và một số bộ định tuyến trên đường dẫn giữa H1 và H2. Giả sử H1 đang gửi thông tin đến H2 và xem xét vai trò của lớp mạng trong các máy chủ này và trong các bộ định tuyến can thiệp. Lớp mạng trong H1 lấy các phân đoạn từ lớp vận chuyển trong H1, đóng gói từng phân đoạn thành một datagram và sau đó gửi các datagram đó đến bộ định tuyến gần đó, R1. Tại máy chủ nhận H2, lớp mạng nhận các datagram từ bộ định tuyến R2 gần đó, trích xuất các phân đoạn của lớp vận chuyển và phân phối các phân đoạn này lên lớp vận chuyển tại H2. Vai trò mặt phẳng dữ liệu chính của mỗi bộ định tuyến là chuyển tiếp các gói dữ liệu từ các liên kết đầu vào đến các liên kết đầu ra của nó; Vai trò chính của mặt phẳng điều khiển mạng là điều phối các hành động chuyển tiếp cục bộ trên mỗi bộ định tuyến này để các gói dữ liệu cuối cùng được truyền từ đầu đến cuối, dọc theo đường dẫn của bộ định tuyến giữa máy chủ nguồn và máy chủ đích. Lưu ý rằng các bộ định tuyến trong Hình 4.1 được hiển thị với một ngăn xếp giao thức bị cắt ngắn, nghĩa là không có lớp nào phía trên lớp mạng, bởi vì bộ định tuyến không chạy các giao thức lớp ứng dụng và lớp vận chuyển như những giao thức mà chúng ta đã xem xét trong Chương 2 và 3.

**4.1.1 Chuyển tiếp và định tuyến: Mặt phẳng dữ liệu và điều khiển**

Vai trò chính của lớp mạng rất đơn giản---để di chuyển các gói từ máy chủ gửi đến máy chủ nhận. Để làm như vậy, có thể xác định hai chức năng quan trọng của lớp mạng:

• Chuyển tiếp. Khi một gói đến liên kết đầu vào của bộ định tuyến, bộ định tuyến phải di chuyển gói đến liên kết đầu ra thích hợp. Ví dụ: gói đến từ Host H1 đến Router R1 trong Hình 4.1 phải được chuyển tiếp đến bộ định tuyến tiếp theo trên đường dẫn tới H2. Như chúng ta sẽ thấy, chuyển tiếp chỉ là một chức năng (mặc dù hầu hết

liên kết

Thuộc vật chất

Mạng

Mạng doanh nghiệp

liên kết

Thuộc vật chất

Ứng dụng

Chuyên chở

Mạng

End System H2

Router R1

Router R2

liên kết

Thuộc vật chất

Ứng dụng

Chuyên chở

Mạng

End System H1

liên kết

Thuộc vật chất

Mạng

liên kết

Thuộc vật chất

Mạng

liên kết

Thuộc vật chất

Mạng

liên kết

Thuộc vật chất

Mạng

*Hình 4.1 ♦ Lớp mạng*

cái phổ biến và quan trọng!) được triển khai trong mặt phẳng dữ liệu. Trong trường hợp tổng quát hơn mà chúng tôi sẽ đề cập trong Phần 4.4, một gói cũng có thể bị chặn thoát khỏi bộ định tuyến (ví dụ: nếu gói bắt nguồn từ một máy chủ gửi độc hại đã biết hoặc nếu gói được định hướng đến một máy chủ đích bị cấm), hoặc có thể bị sao chép và gửi qua nhiều liên kết gửi đi. • Lộ trình. Lớp mạng phải xác định tuyến đường hoặc đường đi của các gói khi chúng truyền từ người gửi đến người nhận. Các thuật toán tính toán các đường dẫn này được gọi là thuật toán định tuyến. Ví dụ, một thuật toán định tuyến sẽ xác định đường đi mà các gói tin đi từ H1 đến H2 trong Hình 4.1. Định tuyến được thực hiện trong mặt phẳng điều khiển của lớp mạng.

Các thuật ngữ chuyển tiếp và định tuyến thường được sử dụng thay thế cho nhau khi thảo luận về lớp mạng. Chúng ta sẽ sử dụng những thuật ngữ này một cách chính xác hơn trong cuốn sách này. Chuyển tiếp đề cập đến hành động cục bộ của bộ định tuyến trong việc chuyển gói từ giao diện liên kết đầu vào sang giao diện liên kết đầu ra thích hợp. Việc chuyển tiếp diễn ra trong khoảng thời gian rất ngắn (thường là vài nano giây) và do đó thường được triển khai trong phần cứng. Định tuyến đề cập đến quy trình trên toàn mạng nhằm xác định đường dẫn từ đầu đến cuối mà các gói đi từ nguồn đến đích. Việc định tuyến diễn ra trong khoảng thời gian dài hơn nhiều (thường là giây) và như chúng ta sẽ thấy thường được triển khai trong phần mềm. Sử dụng phép tương tự lái xe của chúng ta, hãy xem xét chuyến đi từ Pennsylvania đến Florida do du khách của chúng ta thực hiện ở Phần 1.3.1. Trong chuyến đi này, tài xế của chúng tôi đi qua nhiều nút giao thông trên đường đến Florida. Chúng ta có thể coi việc chuyển tiếp là quá trình đi qua một nút giao thông duy nhất: Một ô tô đi vào nút giao thông từ một con đường và xác định đường nào sẽ đi để rời nút giao thông đó. Chúng ta có thể coi định tuyến là quá trình lập kế hoạch cho chuyến đi từ Pennsylvania đến Florida: Trước khi bắt đầu chuyến đi, người lái xe đã tham khảo bản đồ và chọn một trong nhiều con đường có thể, với mỗi con đường bao gồm một loạt các đoạn đường được kết nối tại các nút giao.

Một yếu tố quan trọng trong mỗi bộ định tuyến mạng là bảng chuyển tiếp của nó. Bộ định tuyến chuyển tiếp gói bằng cách kiểm tra giá trị của một hoặc nhiều trường trong tiêu đề của gói đến và sau đó sử dụng các giá trị tiêu đề này để lập chỉ mục vào bảng chuyển tiếp của nó. Giá trị được lưu trữ trong mục nhập bảng chuyển tiếp cho các giá trị đó cho biết giao diện liên kết gửi đi tại bộ định tuyến mà gói đó sẽ được chuyển tiếp. Ví dụ, trong Hình 4.2, một gói có giá trị trường tiêu đề là 0110 đến bộ định tuyến. Bộ định tuyến lập chỉ mục vào bảng chuyển tiếp của nó và xác định rằng giao diện liên kết đầu ra cho gói này là giao diện 2. Sau đó, bộ định tuyến chuyển tiếp gói nội bộ đến giao diện 2. Trong Phần 4.2, chúng ta sẽ xem xét bên trong bộ định tuyến và kiểm tra chức năng chuyển tiếp chi tiết hơn nhiều. Chuyển tiếp là chức năng chính được thực hiện bởi chức năng mặt phẳng dữ liệu của lớp mạng.

Mặt phẳng điều khiển: Cách tiếp cận truyền thống

Nhưng bây giờ chắc chắn bạn đang thắc mắc ngay từ đầu các bảng chuyển tiếp của bộ định tuyến được cấu hình như thế nào. Đây là một vấn đề quan trọng, một vấn đề cho thấy sự tương tác quan trọng giữa chuyển tiếp (trong mặt phẳng dữ liệu) và định tuyến (trong mặt phẳng điều khiển). Như được hiển thị

trong Hình 4.2, thuật toán định tuyến xác định nội dung của bảng chuyển tiếp của bộ định tuyến. Trong ví dụ này, thuật toán định tuyến chạy trong mỗi bộ định tuyến và cả chức năng chuyển tiếp và định tuyến đều được chứa trong bộ định tuyến. Như chúng ta sẽ thấy trong Phần 5.3 và 5.4, hàm thuật toán định tuyến trong một bộ định tuyến giao tiếp với hàm thuật toán định tuyến trong các bộ định tuyến khác để tính toán các giá trị cho bảng chuyển tiếp của nó. Việc giao tiếp này được thực hiện như thế nào? Bằng cách trao đổi các thông điệp định tuyến chứa thông tin định tuyến theo một giao thức định tuyến! Chúng tôi sẽ đề cập đến các thuật toán và giao thức định tuyến trong Phần 5.2 đến 5.4.

Các mục đích riêng biệt và khác nhau của các chức năng chuyển tiếp và định tuyến có thể được minh họa rõ hơn bằng cách xem xét trường hợp giả định (không thực tế nhưng khả thi về mặt kỹ thuật) của một mạng trong đó tất cả các bảng chuyển tiếp được cấu hình trực tiếp bởi các nhà khai thác mạng con người có mặt thực tế tại các bộ định tuyến. Trong trường hợp này, không cần giao thức định tuyến nào! Tất nhiên, người vận hành con người sẽ cần phải tương tác với nhau để đảm bảo rằng các bảng chuyển tiếp được cấu hình sao cho các gói tin đến được đích dự kiến. Cũng có khả năng là cấu hình của con người sẽ dễ xảy ra lỗi hơn và phản ứng chậm hơn nhiều với những thay đổi trong cấu trúc liên kết mạng so với giao thức định tuyến. Do đó, chúng tôi thật may mắn khi tất cả các mạng đều có cả chức năng chuyển tiếp và định tuyến!

Chuyển tiếp địa phương

tiêu đề bảng

đầu ra

Mặt phẳng điều khiển

Mặt phẳng dữ liệu

Thuật toán định tuyến

Các giá trị trong tiêu đề của gói tin đến

*Hình 4.2 ♦ Thuật toán định tuyến xác định giá trị trong bảng chuyển tiếp*

Mặt phẳng điều khiển: Phương pháp tiếp cận SDN

Cách tiếp cận để triển khai chức năng định tuyến được hiển thị trong Hình 4.2---với mỗi bộ định tuyến có thành phần định tuyến giao tiếp với thành phần định tuyến của các bộ định tuyến khác---là cách tiếp cận truyền thống được các nhà cung cấp định tuyến áp dụng trong sản phẩm của họ, ít nhất là cho đến gần đây. Tuy nhiên, quan sát của chúng tôi rằng con người có thể định cấu hình các bảng chuyển tiếp theo cách thủ công cho thấy rằng có thể có các cách khác để chức năng của bảng điều khiển xác định nội dung của các bảng chuyển tiếp mặt phẳng dữ liệu.

Hình 4.3 cho thấy một cách tiếp cận khác trong đó một bộ điều khiển từ xa riêng biệt về mặt vật lý sẽ tính toán và phân phối các bảng chuyển tiếp để mỗi bộ định tuyến sử dụng. Lưu ý rằng các thành phần mặt phẳng dữ liệu của Hình 4.2 và 4.3 giống hệt nhau. Trong hình 4.3; tuy nhiên, chức năng định tuyến mặt phẳng điều khiển được tách biệt khỏi

Chuyển tiếp địa phương

tiêu đề bảng

đầu ra

Bộ điều khiển từ xa

Các giá trị trong tiêu đề của gói tin đến

Mặt phẳng điều khiển

Mặt phẳng dữ liệu

*Hình 4.3 ♦ Bộ điều khiển từ xa xác định và phân phối các giá trị trong*

bảng chuyển tiếp

bộ định tuyến vật lý---thiết bị định tuyến chỉ thực hiện chuyển tiếp, trong khi bộ điều khiển từ xa tính toán và phân phối các bảng chuyển tiếp. Bộ điều khiển từ xa có thể được triển khai trong một trung tâm dữ liệu từ xa với độ tin cậy và dự phòng cao và có thể được quản lý bởi ISP hoặc một số bên thứ ba. Bộ định tuyến và bộ điều khiển từ xa có thể giao tiếp như thế nào? Bằng cách trao đổi các tin nhắn chứa bảng chuyển tiếp và các thông tin định tuyến khác. Cách tiếp cận mặt phẳng điều khiển được hiển thị trong Hình 4.3 là trọng tâm của mạng được xác định bằng phần mềm (SDN), trong đó mạng được "xác định bằng phần mềm" vì bộ điều khiển tính toán các bảng chuyển tiếp và tương tác với các bộ định tuyến được triển khai trong phần mềm. Càng ngày, việc triển khai phần mềm này càng mở, nghĩa là, tương tự như mã hệ điều hành Linux, mã này được cung cấp công khai, cho phép các ISP (và các nhà nghiên cứu và sinh viên mạng!) Đổi mới và đề xuất các thay đổi đối với phần mềm kiểm soát chức năng lớp mạng. Chúng ta sẽ đề cập đến mặt phẳng điều khiển SDN trong Phần 5.5.

**4.1.2 Mô hình dịch vụ mạng**

Trước khi đi sâu vào mặt phẳng dữ liệu của lớp mạng, hãy kết thúc phần giới thiệu của chúng tôi bằng cách xem xét rộng hơn và xem xét các loại dịch vụ khác nhau có thể được cung cấp bởi lớp mạng. Khi lớp vận chuyển tại máy chủ gửi truyền một gói vào mạng (nghĩa là chuyển nó xuống lớp mạng tại máy chủ gửi), lớp vận chuyển có thể dựa vào lớp mạng để chuyển gói đến đích không? Khi nhiều gói được gửi đi, chúng có được gửi đến lớp vận chuyển trong máy chủ nhận theo thứ tự chúng được gửi không? Liệu lượng thời gian giữa việc gửi hai lần truyền gói tuần tự có giống với lượng thời gian giữa việc nhận chúng không? Mạng có cung cấp bất kỳ phản hồi nào về tình trạng tắc nghẽn trong mạng không? Câu trả lời cho những câu hỏi này và những câu hỏi khác được xác định bởi mô hình dịch vụ do lớp mạng cung cấp. Mô hình dịch vụ mạng xác định các đặc điểm của việc phân phối gói tin từ đầu đến cuối giữa máy gửi và máy nhận.

Bây giờ chúng ta hãy xem xét một số dịch vụ khả thi mà lớp mạng có thể cung cấp. Những dịch vụ này có thể bao gồm:

• Đảm bảo giao hàng. Dịch vụ này đảm bảo rằng gói tin được gửi bởi máy chủ nguồn cuối cùng sẽ đến máy chủ đích. • Đảm bảo giao hàng với độ trễ có giới hạn. Dịch vụ này không chỉ đảm bảo việc phân phối gói mà còn phân phối trong giới hạn độ trễ giữa các máy chủ được chỉ định (ví dụ: trong vòng 100 mili giây). • Giao gói theo thứ tự. Dịch vụ này đảm bảo rằng các gói đến đích theo thứ tự chúng được gửi. • Đảm bảo băng thông tối thiểu. Dịch vụ lớp mạng này mô phỏng hoạt động của liên kết truyền có tốc độ bit được chỉ định (ví dụ: 1 Mbps) giữa máy chủ gửi và máy chủ nhận. Miễn là máy chủ gửi truyền các bit (như một phần

số gói) ở tốc độ dưới tốc độ bit được chỉ định, sau đó tất cả các gói cuối cùng sẽ được gửi đến máy chủ đích. • Bảo vệ. Lớp mạng có thể mã hóa tất cả các datagram ở nguồn và giải mã chúng ở đích, do đó cung cấp tính bảo mật cho tất cả các phân đoạn của lớp vận chuyển.

Đây chỉ là danh sách một phần các dịch vụ mà lớp mạng có thể cung cấp---có vô số biến thể có thể có.

Lớp mạng của Internet cung cấp một dịch vụ duy nhất, được gọi là dịch vụ nỗ lực tối đa. Với dịch vụ nỗ lực tối đa, các gói không được đảm bảo sẽ được nhận theo thứ tự chúng được gửi và thậm chí việc gửi cuối cùng của chúng cũng không được đảm bảo. Không có sự đảm bảo nào về độ trễ từ đầu đến cuối cũng như không có sự đảm bảo về băng thông tối thiểu. Có vẻ như dịch vụ nỗ lực tối đa là một uyển ngữ cho việc không có dịch vụ nào cả---một mạng không phân phát gói tin nào đến đích sẽ thỏa mãn định nghĩa về dịch vụ phân phối nỗ lực tối đa! Các kiến ​​trúc mạng khác đã xác định và triển khai các mô hình dịch vụ vượt xa dịch vụ nỗ lực tối đa của Internet. Ví dụ, kiến ​​trúc mạng ATM \[Black 1995\] cung cấp độ trễ theo thứ tự được đảm bảo, độ trễ có giới hạn và băng thông tối thiểu được đảm bảo. Cũng đã có những mở rộng mô hình dịch vụ được đề xuất cho kiến ​​trúc Internet; ví dụ: kiến ​​trúc Intserv \[RFC 1633\] nhằm mục đích cung cấp sự đảm bảo độ trễ ở đầu cuối và giao tiếp không bị tắc nghẽn. Điều thú vị là, bất chấp những giải pháp thay thế được phát triển tốt này, mô hình dịch vụ cơ bản với nỗ lực tối đa của Internet kết hợp với việc cung cấp băng thông đầy đủ và các giao thức cấp ứng dụng thích ứng với băng thông như giao thức DASH mà chúng ta gặp trong Phần 2.6.2 được cho là đã được chứng minh là "đủ tốt" để kích hoạt một loạt ứng dụng đáng kinh ngạc, bao gồm các dịch vụ phát video trực tuyến như Netflix và video-over-IP, các ứng dụng hội nghị thời gian thực như Skype và Facetime.

Tổng quan về Chương 4

Bây giờ đã cung cấp cái nhìn tổng quan về lớp mạng, chúng tôi sẽ đề cập đến thành phần mặt phẳng dữ liệu của lớp mạng trong các phần sau của chương này. Trong Phần 4.2, chúng ta sẽ đi sâu vào các hoạt động phần cứng bên trong của bộ định tuyến, bao gồm xử lý gói đầu vào và đầu ra, cơ chế chuyển mạch nội bộ của bộ định tuyến cũng như xếp hàng và lập lịch gói. Trong Phần 4.3, chúng ta sẽ xem xét chuyển tiếp IP truyền thống, trong đó các gói được chuyển tiếp đến cổng đầu ra dựa trên địa chỉ đích IP của chúng. Chúng ta sẽ gặp cách đánh địa chỉ IP, các giao thức IPv4 và IPv6 nổi tiếng, v.v. Trong Phần 4.4, chúng tôi sẽ đề cập đến việc chuyển tiếp tổng quát hơn, trong đó các gói có thể được chuyển tiếp đến các cổng đầu ra dựa trên một số lượng lớn các giá trị tiêu đề (tức là không chỉ dựa trên địa chỉ đích IP). Packets có thể bị chặn hoặc sao chép trên bộ định tuyến hoặc có thể ghi lại một số giá trị trường tiêu đề nhất định---tất cả đều dưới sự kiểm soát của phần mềm. Hình thức chuyển tiếp gói tổng quát hơn này là thành phần chính của mặt phẳng dữ liệu mạng hiện đại, bao gồm mặt phẳng dữ liệu trong các mạng được xác định bằng phần mềm (SDN). Trong Phần 4.5, chúng ta sẽ tìm hiểu về "hộp trung gian" có thể thực hiện các chức năng ngoài việc chuyển tiếp.

Chúng tôi đề cập ở đây rằng các thuật ngữ chuyển tiếp và chuyển mạch thường được sử dụng thay thế cho nhau bởi các nhà nghiên cứu và thực hành mạng máy tính; chúng tôi cũng sẽ sử dụng cả hai thuật ngữ thay thế cho nhau trong sách giáo khoa này. Mặc dù chúng ta đang nói về chủ đề thuật ngữ, nhưng cũng cần đề cập đến hai thuật ngữ khác thường được sử dụng thay thế cho nhau nhưng chúng ta sẽ sử dụng cẩn thận hơn. Chúng tôi sẽ bảo lưu thuật ngữ chuyển mạch gói có nghĩa là một thiết bị chuyển mạch gói chung chuyển gói từ giao diện liên kết đầu vào sang giao diện liên kết đầu ra, theo các giá trị trong trường tiêu đề của gói. Một số bộ chuyển mạch gói, được gọi là bộ chuyển mạch lớp liên kết (được xem xét trong Chương 6), đưa ra quyết định chuyển tiếp dựa trên các giá trị trong các trường của khung lớp liên kết; do đó các thiết bị chuyển mạch được gọi là thiết bị lớp liên kết (lớp 2). Các bộ chuyển mạch gói khác, được gọi là bộ định tuyến, đưa ra quyết định chuyển tiếp dựa trên các giá trị trường tiêu đề trong datagram lớp mạng. Routers do đó là các thiết bị lớp mạng (lớp 3). (Để đánh giá đầy đủ sự khác biệt quan trọng này, bạn có thể muốn xem lại Phần 1.5.2, trong đó chúng ta thảo luận về các datagram lớp mạng và các khung lớp liên kết cũng như mối quan hệ của chúng.) Vì trọng tâm của chúng ta trong chương này là về lớp mạng nên chúng ta sẽ chủ yếu sử dụng thuật ngữ bộ định tuyến thay cho chuyển mạch gói.

**4.2 Bên trong Router có gì?**

Bây giờ chúng ta đã tổng quan về dữ liệu và mặt phẳng điều khiển trong lớp mạng, sự khác biệt quan trọng giữa chuyển tiếp và định tuyến cũng như các dịch vụ và chức năng của lớp mạng, hãy chuyển sự chú ý của chúng ta sang chức năng chuyển tiếp của nó---việc truyền gói thực tế từ các liên kết đến của bộ định tuyến đến các liên kết đi thích hợp tại bộ định tuyến đó.

Khung nhìn cấp cao về kiến ​​trúc bộ định tuyến chung được hiển thị trong Hình 4.4. Bốn thành phần bộ định tuyến có thể được xác định:

Cổng đầu vào

Cổng đầu ra

Cổng đầu vào

Cổng đầu ra

Bộ xử lý định tuyến Định tuyến, mặt phẳng điều khiển quản lý (phần mềm)

Chuyển tiếp mặt phẳng dữ liệu (phần cứng)

Switch

vải vóc

*Hình 4.4 ♦ Kiến trúc Router*

• Cổng đầu vào. Một cổng đầu vào thực hiện một số chức năng chính. Nó thực hiện chức năng lớp vật lý là chấm dứt liên kết vật lý đến tại bộ định tuyến; điều này được thể hiện ở hộp ngoài cùng bên trái của cổng đầu vào và hộp ngoài cùng bên phải của cổng đầu ra trong Hình 4.4. Cổng đầu vào cũng thực hiện các chức năng của lớp liên kết cần thiết để tương tác với lớp liên kết ở phía bên kia của liên kết đến; điều này được thể hiện bằng các hộp ở giữa trong cổng đầu vào và đầu ra. Có lẽ điều quan trọng nhất là chức năng tra cứu cũng được thực hiện tại cổng đầu vào; điều này sẽ xảy ra ở hộp ngoài cùng bên phải của cổng đầu vào. Ở đây, bảng chuyển tiếp được tham khảo để xác định cổng đầu ra của bộ định tuyến mà gói đến sẽ được chuyển tiếp qua kết cấu chuyển mạch. Các gói điều khiển (ví dụ: các gói mang thông tin giao thức định tuyến) được chuyển tiếp từ cổng đầu vào đến bộ xử lý định tuyến. Lưu ý rằng thuật ngữ "cổng" ở đây---chỉ các giao diện đầu vào và đầu ra vật lý của bộ định tuyến---khác biệt rõ rệt với các cổng phần mềm liên kết với các ứng dụng mạng và ổ cắm được thảo luận trong Chương 2 và 3. Trên thực tế, số lượng cổng được bộ định tuyến hỗ trợ có thể dao động từ một số lượng tương đối nhỏ trong bộ định tuyến doanh nghiệp đến hàng trăm cổng 10 Gbps trong bộ định tuyến ở biên của ISP, nơi số lượng đường đến có xu hướng lớn nhất. Ví dụ: Juniper MX2020, bộ định tuyến biên, hỗ trợ tới 800 cổng Ethernet 100 Gbps, với tổng công suất hệ thống bộ định tuyến là 800 Tbps \[Juniper MX 2020 2020\].

• Chuyển vải. Cơ cấu chuyển mạch kết nối các cổng đầu vào của bộ định tuyến với các cổng đầu ra của nó. Cơ cấu chuyển mạch này hoàn toàn nằm trong bộ định tuyến---một mạng bên trong bộ định tuyến mạng!

• Cổng đầu ra. Cổng đầu ra lưu trữ các gói nhận được từ kết cấu chuyển mạch và truyền các gói này trên liên kết đi bằng cách thực hiện các chức năng lớp liên kết và lớp vật lý cần thiết. Khi một liên kết là hai chiều (nghĩa là mang lưu lượng theo cả hai hướng), cổng đầu ra thường sẽ được ghép nối với cổng đầu vào cho liên kết đó trên cùng một thẻ đường truyền.

• Bộ xử lý định tuyến. Bộ xử lý định tuyến thực hiện các chức năng của mặt phẳng điều khiển. Trong các bộ định tuyến truyền thống, nó thực thi các giao thức định tuyến (chúng ta sẽ nghiên cứu trong Phần 5.3 và 5.4), duy trì các bảng định tuyến và thông tin trạng thái liên kết đính kèm, đồng thời tính toán bảng chuyển tiếp cho bộ định tuyến. Trong bộ định tuyến SDN, bộ xử lý định tuyến chịu trách nhiệm liên lạc với bộ điều khiển từ xa để (trong số các hoạt động khác) nhận các mục trong bảng chuyển tiếp do bộ điều khiển từ xa tính toán và cài đặt các mục này vào các cổng đầu vào của bộ định tuyến. Bộ xử lý định tuyến cũng thực hiện các chức năng quản lý mạng mà chúng ta sẽ nghiên cứu trong Phần 5.7.

Các cổng đầu vào, cổng đầu ra và cơ cấu chuyển mạch của bộ định tuyến hầu như luôn được triển khai trong phần cứng, như trong Hình 4.4. Để đánh giá cao lý do tại sao cần triển khai phần cứng, hãy xem xét rằng với liên kết đầu vào 100 Gbps và gói dữ liệu IP 64 byte, cổng đầu vào chỉ có 5,12 ns để xử lý gói dữ liệu trước khi gói dữ liệu khác có thể đến. Nếu N cổng được kết hợp trên một card đường truyền (như thường được thực hiện trong thực tế), đường dẫn xử lý datagram phải hoạt động nhanh hơn N lần---quá nhiều

triển khai phần mềm nhanh chóng. Phần cứng chuyển tiếp có thể được triển khai bằng cách sử dụng thiết kế phần cứng của chính nhà cung cấp bộ định tuyến hoặc được xây dựng bằng chip silicon thương mại đã mua (ví dụ: được bán bởi các công ty như Intel và Broadcom).

Trong khi mặt phẳng dữ liệu hoạt động ở quy mô thời gian nano giây, các chức năng điều khiển của bộ định tuyến---thực thi các giao thức định tuyến, phản hồi các liên kết đi lên hoặc xuống được đính kèm, liên lạc với bộ điều khiển từ xa (trong trường hợp SDN) và thực hiện các chức năng quản lý---hoạt động ở khoảng thời gian mili giây hoặc giây. Do đó, các chức năng mặt phẳng điều khiển này thường được triển khai trong phần mềm và thực thi trên bộ xử lý định tuyến (thường là CPU truyền thống).

Trước khi đi sâu vào chi tiết bên trong bộ định tuyến, chúng ta hãy quay lại phép tương tự của chúng ta ở đầu chương này, trong đó việc chuyển tiếp gói được so sánh với việc ô tô vào và rời khỏi một tổng đài. Giả sử rằng nút giao thông là một bùng binh và khi một chiếc ô tô đi vào bùng binh thì cần phải xử lý một chút. Hãy xem xét những thông tin nào cần thiết cho quá trình xử lý này:

• Chuyển tiếp dựa trên điểm đến. Giả sử ô tô dừng lại ở một trạm nhập cảnh và cho biết điểm đến cuối cùng của nó (không phải ở bùng binh địa phương mà là điểm đến cuối cùng của hành trình). Một nhân viên tại trạm vào tra cứu điểm đến cuối cùng, xác định lối ra bùng binh dẫn đến điểm đến cuối cùng đó và cho người lái xe biết nên đi theo lối ra bùng binh nào.

• Chuyển tiếp tổng quát. Người phục vụ cũng có thể xác định lối ra của xe dựa trên nhiều yếu tố khác ngoài điểm đến. Ví dụ: đoạn đường ra được chọn có thể phụ thuộc vào nguồn gốc của ô tô, ví dụ như tiểu bang cấp biển số ô tô. Ô tô từ một số tiểu bang nhất định có thể được hướng dẫn sử dụng một đoạn đường ra (dẫn đến đích bằng đường chậm), trong khi ô tô từ các tiểu bang khác có thể được hướng dẫn sử dụng một đoạn đường ra khác (dẫn đến đích qua đường cao tốc). Quyết định tương tự có thể được đưa ra dựa trên kiểu dáng, nhãn hiệu và năm sản xuất của chiếc xe. Hoặc một chiếc ô tô được coi là không đủ điều kiện đi đường có thể bị chặn và không được phép đi qua bùng binh. Trong trường hợp chuyển tiếp tổng quát, bất kỳ yếu tố nào cũng có thể góp phần vào việc người phục vụ lựa chọn lối ra cho một ô tô nhất định.

Sau khi ô tô đi vào bùng binh (có thể chứa đầy các ô tô khác đi vào từ đường vào khác và đi đến các lối ra bùng binh khác), cuối cùng ô tô sẽ rời khỏi đoạn đường ra khỏi bùng binh theo quy định, nơi nó có thể gặp những ô tô khác đang rời khỏi bùng binh tại lối ra đó.

Chúng ta có thể dễ dàng nhận ra các thành phần chính của bộ định tuyến trong Hình 4.4 trong ví dụ tương tự này---đường vào và trạm vào tương ứng với cổng đầu vào (có chức năng tra cứu để xác định cổng đi cục bộ); bùng binh tương ứng với vải công tắc; và đường ra bùng binh tương ứng với cổng ra. Với sự tương tự này, cần phải xem xét nơi nào có thể xảy ra tắc nghẽn. Điều gì sẽ xảy ra nếu ô tô đến với tốc độ chóng mặt (ví dụ: bùng binh ở Đức hoặc Ý!) nhưng nhân viên nhà ga lại chậm? Người phục vụ phải làm việc nhanh như thế nào để đảm bảo không có xe dự phòng trên đường vào? Ngay cả với một người phục vụ nhanh như chớp, điều gì sẽ xảy ra nếu ô tô

đi qua bùng binh một cách chậm rãi---vẫn có thể xảy ra việc sao lưu chứ? Và điều gì sẽ xảy ra nếu hầu hết các ô tô đi vào tất cả các đoạn đường vào của bùng binh đều muốn rời khỏi bùng binh ở cùng một đoạn đường ra---việc sao lưu có thể xảy ra ở đoạn đường ra hoặc ở nơi khác không? Vòng xuyến sẽ hoạt động như thế nào nếu chúng ta muốn chỉ định mức độ ưu tiên cho các ô tô khác nhau hoặc chặn một số ô tô nhất định đi vào bùng binh ngay từ đầu? Tất cả những điều này đều tương tự như những câu hỏi quan trọng mà các nhà thiết kế bộ định tuyến và chuyển mạch phải đối mặt.

Trong các phần phụ sau, chúng ta sẽ xem xét các chức năng của bộ định tuyến chi tiết hơn. \[Turner 1988; McKeown 1997a; Gà gô 1998; Iyer 2008; Serpanos 2011; Zilberman 2019\] đưa ra thảo luận về các kiến ​​trúc bộ định tuyến cụ thể. Để cụ thể và đơn giản, ban đầu chúng ta giả định trong phần này rằng các quyết định chuyển tiếp chỉ dựa trên địa chỉ đích của gói chứ không dựa trên một tập hợp tổng quát các trường tiêu đề gói. Chúng ta sẽ đề cập đến trường hợp chuyển tiếp gói tổng quát hơn trong Phần 4.4.

**4.2.1 Đầu vào Port Xử lý và chuyển tiếp dựa trên đích đến**

Một cái nhìn chi tiết hơn về quá trình xử lý đầu vào được thể hiện trong Hình 4.5. Như vừa thảo luận, chức năng kết thúc dòng của cổng đầu vào và xử lý lớp liên kết thực hiện các lớp vật lý và liên kết cho liên kết đầu vào riêng lẻ đó. Việc tra cứu được thực hiện ở cổng đầu vào là trọng tâm trong hoạt động của bộ định tuyến---ở đây, bộ định tuyến sử dụng bảng chuyển tiếp để tra cứu cổng đầu ra mà gói đến sẽ được chuyển tiếp qua cơ cấu chuyển mạch. Bảng chuyển tiếp được bộ xử lý định tuyến tính toán và cập nhật (sử dụng giao thức định tuyến để tương tác với bộ xử lý định tuyến trong các bộ định tuyến mạng khác) hoặc được nhận từ bộ điều khiển SDN từ xa. Bảng chuyển tiếp được sao chép từ bộ xử lý định tuyến sang các thẻ dòng qua một bus riêng (ví dụ: bus PCI) được biểu thị bằng đường đứt nét từ bộ xử lý định tuyến đến các thẻ dòng đầu vào trong Hình 4.4. Với bản sao ẩn như vậy ở mỗi thẻ dòng, các quyết định chuyển tiếp có thể được thực hiện cục bộ, tại mỗi cổng đầu vào mà không cần gọi bộ xử lý định tuyến tập trung trên cơ sở mỗi gói và do đó tránh được tắc nghẽn xử lý tập trung.

Bây giờ chúng ta hãy xem xét trường hợp \"đơn giản nhất\" mà cổng đầu ra mà gói đến sẽ được chuyển sang dựa trên địa chỉ đích của gói. Trong trường hợp địa chỉ IP 32 bit, việc triển khai bảng chuyển tiếp một cách mạnh mẽ sẽ có một mục nhập cho mọi địa chỉ đích có thể có. Vì có hơn 4 tỷ địa chỉ khả thi nên tùy chọn này hoàn toàn không khả thi.

Chấm dứt dòng

Xử lý liên kết dữ liệu

(giao thức, giải mã)

Tra cứu, chuyển tiếp,

đang xếp hàng Switch

vải vóc

*Hình 4.5 ♦ Xử lý cổng đầu vào*

Để làm ví dụ về cách xử lý vấn đề quy mô này, hãy giả sử rằng bộ định tuyến của chúng tôi có bốn liên kết, được đánh số từ 0 đến 3 và các gói đó sẽ được chuyển tiếp đến các giao diện liên kết như sau:

Giao diện liên kết phạm vi địa chỉ đích

11001000 00010111 00010000 00000000 đến 11001000 00010111 00010111 11111111

11001000 00010111 00011000 00000000 đến 11001000 00010111 00011000 11111111

11001000 00010111 00011001 00000000 đến 11001000 00010111 00011111 11111111

Nếu không thì

Rõ ràng, với ví dụ này, không cần thiết phải có 4 tỷ mục trong bảng chuyển tiếp của bộ định tuyến. Ví dụ: chúng ta có thể có bảng chuyển tiếp sau chỉ với bốn mục:

Giao diện liên kết tiền tố

11001000 00010111 00010 11001000 00010111 00011000 11001000 00010111 00011 Ngược lại

Với kiểu bảng chuyển tiếp này, bộ định tuyến khớp tiền tố của địa chỉ đích của gói với các mục trong bảng; nếu trùng khớp, bộ định tuyến sẽ chuyển tiếp gói đến một liên kết được liên kết với kết quả khớp. Ví dụ: giả sử địa chỉ đích của gói là 11001000 00010111 00010110 10100001; vì tiền tố 21-bit của địa chỉ này khớp với mục nhập đầu tiên trong bảng nên bộ định tuyến sẽ chuyển tiếp gói đến giao diện liên kết 0. Nếu tiền tố không khớp với bất kỳ mục nào trong ba mục đầu tiên thì bộ định tuyến sẽ chuyển tiếp gói đến giao diện mặc định 3. Mặc dù điều này nghe có vẻ đơn giản nhưng có một sự tinh tế rất quan trọng ở đây. Bạn có thể nhận thấy rằng một địa chỉ đích có thể khớp với nhiều mục nhập. Ví dụ: 24 bit đầu tiên của địa chỉ 11001000 00010111 00011000 10101010 khớp với mục nhập thứ hai trong bảng và 21 bit đầu tiên của địa chỉ khớp với mục nhập thứ ba trong bảng. Khi có nhiều kết quả khớp, bộ định tuyến sẽ sử dụng quy tắc khớp tiền tố dài nhất; nghĩa là, nó tìm mục nhập phù hợp dài nhất trong bảng và chuyển tiếp gói đến giao diện liên kết được liên kết với kết quả khớp tiền tố dài nhất. Chúng ta sẽ thấy chính xác lý do tại sao điều này

quy tắc khớp tiền tố dài nhất được sử dụng khi chúng ta nghiên cứu địa chỉ Internet chi tiết hơn trong Phần 4.3.

Với sự tồn tại của một bảng chuyển tiếp, việc tra cứu về mặt khái niệm rất đơn giản--- logic phần cứng chỉ tìm kiếm trong bảng chuyển tiếp để tìm kết quả khớp tiền tố dài nhất. Nhưng ở tốc độ truyền Gigabit, việc tra cứu này phải được thực hiện tính bằng nano giây (hãy nhớ lại ví dụ trước đây của chúng tôi về liên kết 10 Gbps và gói dữ liệu IP 64 byte). Vì vậy, không chỉ việc tra cứu phải được thực hiện trong phần cứng mà còn cần đến các kỹ thuật ngoài tìm kiếm tuyến tính đơn giản thông qua một bảng lớn; khảo sát về các thuật toán tra cứu nhanh có thể được tìm thấy trong \[Gupta 2001, Ruiz-Sanchez 2001\]. Cũng phải đặc biệt chú ý đến thời gian truy cập bộ nhớ, dẫn đến các thiết kế có DRAM nhúng trên chip và bộ nhớ SRAM (được sử dụng làm bộ nhớ đệm DRAM) nhanh hơn. Trong thực tế, Bộ nhớ có thể định địa chỉ nội dung bậc ba (TCAM) cũng thường được sử dụng để tra cứu \[Yu 2004\]. Với TCAM, địa chỉ IP 32 bit được hiển thị trong bộ nhớ, trả về nội dung của mục nhập bảng chuyển tiếp cho địa chỉ đó trong thời gian cơ bản không đổi. Bộ định tuyến và chuyển mạch Cisco Catalyst 6500 và 7600 Series có thể chứa tới một triệu mục trong bảng chuyển tiếp TCAM \[Cisco TCAM 2014\].

Khi cổng đầu ra của gói đã được xác định thông qua tra cứu, gói có thể được gửi vào cơ cấu chuyển mạch. Trong một số thiết kế, một gói có thể tạm thời bị chặn không cho đi vào kết cấu chuyển mạch nếu các gói từ các cổng đầu vào khác hiện đang sử dụng kết cấu. Một gói bị chặn sẽ được xếp hàng đợi tại cổng đầu vào và sau đó được lên lịch để truyền qua kết cấu vào một thời điểm sau đó. Chúng ta sẽ xem xét kỹ hơn việc chặn, xếp hàng và lập lịch các gói (ở cả cổng đầu vào và cổng đầu ra) trong thời gian ngắn. Mặc dù "tra cứu" được cho là hành động quan trọng nhất trong quá trình xử lý cổng đầu vào, nhưng nhiều hành động khác phải được thực hiện: (1) quá trình xử lý lớp vật lý và lớp liên kết phải diễn ra, như đã thảo luận trước đây; (2) số phiên bản, tổng kiểm tra và trường thời gian tồn tại của gói---tất cả những thông tin này chúng ta sẽ nghiên cứu trong Phần 4.3---phải được kiểm tra và hai trường sau phải được viết lại; và (3) các bộ đếm được sử dụng để quản lý mạng (chẳng hạn như số lượng gói dữ liệu IP đã nhận được) phải được cập nhật.

Hãy kết thúc cuộc thảo luận của chúng ta về việc xử lý cổng đầu vào bằng cách lưu ý rằng các bước cổng đầu vào để tìm kiếm địa chỉ IP đích ("khớp") và sau đó gửi gói vào cơ cấu chuyển mạch đến cổng đầu ra được chỉ định ("hành động") là một trường hợp cụ thể của một khái niệm trừu tượng "khớp cộng với hành động" tổng quát hơn được thực hiện trong nhiều thiết bị nối mạng, không chỉ các bộ định tuyến. Trong các bộ chuyển mạch lớp liên kết (được đề cập trong Chương 6), địa chỉ đích của lớp liên kết được tra cứu và một số hành động có thể được thực hiện ngoài việc gửi khung vào cơ cấu chuyển mạch tới cổng đầu ra. Trong tường lửa (được đề cập trong Chương 8)---các thiết bị lọc các gói đến đã chọn---một gói đến có tiêu đề phù hợp với tiêu chí nhất định (ví dụ: sự kết hợp giữa địa chỉ nguồn/đích IP và số cổng của lớp vận chuyển) có thể bị loại bỏ (hành động). Trong trình dịch địa chỉ mạng (NAT, được đề cập trong Phần 4.3), gói đến có số cổng lớp vận chuyển khớp với một giá trị nhất định sẽ có số cổng được ghi lại trước khi chuyển tiếp (hành động). Thật vậy, khái niệm trừu tượng "kết hợp với hành động" \[Bosshart 2013\] vừa mạnh mẽ vừa phổ biến trong các thiết bị mạng ngày nay, đồng thời là trọng tâm của khái niệm chuyển tiếp tổng quát mà chúng ta sẽ nghiên cứu trong Phần 4.4.

**4.2.2 Chuyển mạch**

Cơ cấu chuyển mạch là trung tâm của bộ định tuyến, vì thông qua cơ cấu này mà các gói thực sự được chuyển mạch (nghĩa là được chuyển tiếp) từ cổng đầu vào sang cổng đầu ra. Việc chuyển đổi có thể được thực hiện theo một số cách, như trong Hình 4.6:

• Chuyển đổi qua bộ nhớ. Các bộ định tuyến đơn giản nhất, sớm nhất là các máy tính truyền thống, việc chuyển đổi giữa các cổng đầu vào và đầu ra được thực hiện dưới sự điều khiển trực tiếp của CPU (bộ xử lý định tuyến). Các cổng đầu vào và đầu ra hoạt động như các thiết bị I/O truyền thống trong hệ điều hành truyền thống. Cổng đầu vào có gói đến trước tiên sẽ báo hiệu cho bộ xử lý định tuyến thông qua một ngắt. Sau đó gói được sao chép từ cổng đầu vào vào bộ nhớ bộ xử lý. Sau đó, bộ xử lý định tuyến trích xuất địa chỉ đích từ tiêu đề, tra cứu cổng đầu ra thích hợp trong bảng chuyển tiếp và sao chép gói vào bộ đệm của cổng đầu ra. Trong trường hợp này, nếu băng thông bộ nhớ sao cho có thể ghi vào hoặc đọc từ bộ nhớ tối đa B gói mỗi giây thì thông lượng chuyển tiếp tổng thể (tổng tốc độ mà các gói được truyền từ cổng đầu vào đến cổng đầu ra) phải nhỏ hơn B/2. Cũng lưu ý rằng hai gói không thể được chuyển tiếp

Ký ức

MỘT

B

C

X

Y

Z

Ký ức

Chìa khóa:

Cổng đầu vào Cổng đầu ra

MỘT

X Y Z

B

C

Mạng kết nối

MỘT

B

C

X

Y

Z

xe buýt

*Hình 4.6 ♦ Ba kỹ thuật chuyển mạch*

cùng một lúc, ngay cả khi chúng có các cổng đích khác nhau, vì mỗi lần chỉ có thể thực hiện một lần đọc/ghi một bộ nhớ trên bus hệ thống dùng chung. Một số bộ định tuyến hiện đại chuyển đổi qua bộ nhớ. Tuy nhiên, điểm khác biệt lớn so với các bộ định tuyến đời đầu là việc tra cứu địa chỉ đích và lưu trữ gói vào vị trí bộ nhớ thích hợp được thực hiện bằng cách xử lý trên các thẻ dòng đầu vào. Theo một số cách, các bộ định tuyến chuyển đổi qua bộ nhớ trông rất giống các bộ xử lý đa bộ nhớ dùng chung, với việc xử lý trên thẻ dòng chuyển (ghi) các gói vào bộ nhớ của cổng đầu ra thích hợp. Bộ chuyển mạch dòng Catalyst 8500 của Cisco \[Cisco 8500 2020\] chuyển mạch nội bộ các gói thông qua bộ nhớ dùng chung. • Chuyển đổi qua xe buýt. Theo cách tiếp cận này, cổng đầu vào chuyển gói trực tiếp đến cổng đầu ra qua bus chia sẻ mà không cần sự can thiệp của bộ xử lý định tuyến. Điều này thường được thực hiện bằng cách đặt trước cổng đầu vào một nhãn chuyển mạch nội bộ (tiêu đề) cho gói cho biết cổng đầu ra cục bộ mà gói này đang được chuyển đến và truyền gói lên bus. Tất cả các cổng đầu ra đều nhận được gói, nhưng chỉ cổng phù hợp với nhãn mới giữ được gói. Nhãn sau đó sẽ được gỡ bỏ tại cổng đầu ra vì nhãn này chỉ được sử dụng trong bộ chuyển mạch để đi qua bus. Nếu nhiều gói đến bộ định tuyến cùng lúc, mỗi gói ở một cổng đầu vào khác nhau, tất cả trừ một gói phải đợi vì mỗi lần chỉ có một gói có thể đi qua xe buýt. Bởi vì mọi gói phải đi qua một bus duy nhất nên tốc độ chuyển mạch của bộ định tuyến bị giới hạn ở tốc độ bus; trong sự tương tự về bùng binh của chúng ta, điều này giống như thể bùng binh chỉ có thể chứa một ô tô tại một thời điểm. Tuy nhiên, chuyển đổi qua bus thường là đủ cho các bộ định tuyến hoạt động trong mạng doanh nghiệp và khu vực địa phương nhỏ. Bộ định tuyến Cisco 6500 \[Cisco 6500 2020\] chuyển mạch nội bộ các gói qua bus bảng nối đa năng 32 Gbps. • Chuyển mạch qua mạng kết nối. Một cách để khắc phục giới hạn băng thông của một bus chia sẻ là sử dụng mạng kết nối phức tạp hơn, chẳng hạn như các mạng đã được sử dụng trước đây để kết nối các bộ xử lý trong kiến ​​trúc máy tính đa bộ xử lý. Crossbar switch là một mạng kết nối bao gồm 2N bus kết nối N cổng đầu vào với N cổng đầu ra, như trong Hình 4.6. Mỗi bus dọc giao với mỗi bus ngang tại một điểm giao nhau, có thể được mở hoặc đóng bất kỳ lúc nào bằng bộ điều khiển kết cấu chuyển mạch (có logic là một phần của chính kết cấu chuyển mạch). Khi một gói đến từ cổng A và cần được chuyển tiếp đến cổng Y, bộ điều khiển chuyển mạch sẽ đóng điểm giao nhau ở giao điểm của bus A và Y, sau đó cổng A sẽ gửi gói lên bus của nó và gói này chỉ được đón bởi bus Y. Lưu ý rằng một gói từ cổng B có thể được chuyển tiếp đến cổng X cùng một lúc, vì các gói A-to-Y và B-to-X sử dụng các bus đầu vào và đầu ra khác nhau. Do đó, không giống như hai phương pháp chuyển mạch trước đó, các chuyển mạch crossbar có khả năng chuyển tiếp nhiều gói tin song song. Crossbar switch không bị chặn---một gói được chuyển tiếp đến một cổng đầu ra sẽ không bị chặn đến cổng đầu ra đó miễn là hiện tại không có gói nào khác được chuyển tiếp đến cổng đầu ra đó. Tuy nhiên, nếu hai gói từ hai cổng đầu vào khác nhau được định hướng đến cùng một cổng đầu ra thì một gói sẽ phải đợi ở đầu vào, vì mỗi lần chỉ có thể gửi một gói qua bất kỳ bus nào. Dòng Cisco 12000

thiết bị chuyển mạch \[Cisco 12000 2020\] sử dụng mạng chuyển mạch thanh ngang; dòng Cisco 7600 có thể được cấu hình để sử dụng bộ chuyển mạch bus hoặc thanh ngang \[Cisco 7600 2020\]. Các mạng kết nối phức tạp hơn sử dụng nhiều giai đoạn của các phần tử chuyển mạch để cho phép các gói từ các cổng đầu vào khác nhau tiến tới cùng một cổng đầu ra cùng lúc thông qua cơ cấu chuyển mạch nhiều giai đoạn. Xem \[Tobagi 1990\] để biết khảo sát về kiến ​​trúc chuyển mạch. Cisco CRS sử dụng chiến lược chuyển mạch không chặn ba giai đoạn. Khả năng chuyển mạch của bộ định tuyến cũng có thể được mở rộng bằng cách chạy song song nhiều loại vải chuyển mạch. Theo phương pháp này, cổng đầu vào và cổng đầu ra được kết nối với N loại vải chuyển mạch hoạt động song song. Cổng đầu vào chia gói thành K khối nhỏ hơn và gửi ("phun") các khối thông qua K trong số N loại vải chuyển mạch này tới cổng đầu ra đã chọn, cổng này sẽ tập hợp lại K khối trở lại gói ban đầu.

**4.2.3 Xử lý đầu ra Port**

Quá trình xử lý cổng đầu ra, được hiển thị trong Hình 4.7, lấy các gói đã được lưu trong bộ nhớ của cổng đầu ra và truyền chúng qua liên kết đầu ra. Điều này bao gồm việc lựa chọn (tức là lập lịch) và xếp hàng các gói để truyền và thực hiện các chức năng truyền lớp vật lý và lớp liên kết cần thiết.

**4.2.4 Việc xếp hàng xảy ra ở đâu?**

Nếu chúng ta xem xét chức năng của cổng đầu vào và đầu ra cũng như các cấu hình được hiển thị trong Hình 4.6, thì rõ ràng là hàng đợi gói có thể hình thành ở cả cổng đầu vào và cổng đầu ra, giống như chúng ta đã xác định các trường hợp ô tô có thể đợi ở đầu vào và đầu ra của nút giao thông trong ví dụ về đường vòng của chúng ta. Vị trí và phạm vi xếp hàng (tại hàng đợi cổng đầu vào hoặc hàng đợi cổng đầu ra) sẽ phụ thuộc vào tải lưu lượng, tốc độ tương đối của kết cấu chuyển mạch và tốc độ đường truyền. Bây giờ chúng ta hãy xem xét các hàng đợi này chi tiết hơn một chút, vì khi các hàng đợi này lớn lên, bộ nhớ của bộ định tuyến cuối cùng có thể cạn kiệt và mất gói sẽ xảy ra khi không còn bộ nhớ để lưu trữ các gói đến. Hãy nhớ lại rằng trong các cuộc thảo luận trước đó, chúng ta đã nói rằng các gói "bị mất trong mạng" hoặc "bị rơi ở bộ định tuyến". Chính tại đây, tại các hàng đợi này trong bộ định tuyến, nơi các gói tin như vậy thực sự bị rơi và mất.

Chấm dứt dòng

Xử lý liên kết dữ liệu

(giao thức, đóng gói)

Hàng đợi (bộ đệm

quản lý) Switch

vải vóc

*Hình 4.7 ♦ Xử lý cổng đầu ra*

Giả sử rằng tốc độ đường truyền đầu vào và đầu ra (tốc độ truyền) đều có tốc độ truyền gói Rline trên giây giống hệt nhau và có N cổng đầu vào và N cổng đầu ra. Để đơn giản hóa cuộc thảo luận hơn nữa, hãy giả sử rằng tất cả các gói có cùng độ dài cố định và các gói đó đến cổng đầu vào một cách đồng bộ. Nghĩa là, thời gian để gửi một gói trên bất kỳ liên kết nào bằng thời gian để nhận một gói trên bất kỳ liên kết nào và trong khoảng thời gian đó, không hoặc một gói có thể đến trên liên kết đầu vào. Xác định tốc độ truyền kết cấu chuyển mạch Rswitch là tốc độ mà các gói có thể được di chuyển từ cổng đầu vào sang cổng đầu ra. Nếu Rswitch nhanh hơn Rline N lần thì chỉ xảy ra hàng đợi không đáng kể ở các cổng đầu vào. Điều này là do ngay cả trong trường hợp xấu nhất, khi tất cả N dòng đầu vào đang nhận gói và tất cả các gói sẽ được chuyển tiếp đến cùng một cổng đầu ra, mỗi lô N gói (một gói cho mỗi cổng đầu vào) có thể bị xóa thông qua kết cấu chuyển mạch trước khi lô tiếp theo đến.

Xếp hàng đầu vào

Nhưng điều gì sẽ xảy ra nếu cơ cấu chuyển mạch không đủ nhanh (so với tốc độ đường truyền đầu vào) để truyền tất cả các gói đến qua cơ cấu mà không bị chậm trễ? Trong trường hợp này, việc xếp hàng gói cũng có thể xảy ra ở các cổng đầu vào, vì các gói phải nối với hàng đợi cổng đầu vào để chờ đến lượt chúng được chuyển qua cơ cấu chuyển mạch sang cổng đầu ra. Để minh họa một hệ quả quan trọng của việc xếp hàng này, hãy xem xét cơ cấu chuyển mạch thanh ngang và giả sử rằng (1) tất cả tốc độ liên kết đều giống hệt nhau, (2) rằng một gói có thể được truyền từ bất kỳ một cổng đầu vào nào đến một cổng đầu ra nhất định trong cùng một khoảng thời gian cần thiết để nhận được một gói trên một liên kết đầu vào và (3) các gói được chuyển từ hàng đợi đầu vào nhất định đến hàng đợi đầu ra mong muốn của chúng theo cách thức FCFS. Nhiều gói có thể được truyền song song, miễn là cổng đầu ra của chúng khác nhau. Tuy nhiên, nếu hai gói ở phía trước của hai hàng đợi đầu vào được dành cho cùng một hàng đợi đầu ra thì một trong các gói sẽ bị chặn và phải đợi ở hàng đợi đầu vào---kết cấu chuyển mạch chỉ có thể chuyển một gói đến một cổng đầu ra nhất định tại một thời điểm.

Hình 4.8 cho thấy một ví dụ trong đó hai gói (được tô đậm) ở phía trước hàng đợi đầu vào của chúng được dành cho cùng một cổng đầu ra phía trên bên phải. Giả sử rằng cơ cấu chuyển mạch chọn chuyển gói từ phía trước hàng đợi phía trên bên trái. Trong trường hợp này, gói có màu tối ở hàng đợi phía dưới bên trái phải chờ. Nhưng không chỉ gói bóng tối này phải chờ mà cả gói bóng mờ xếp sau gói đó trong hàng đợi phía dưới bên trái, mặc dù không có sự tranh chấp ở cổng đầu ra ở giữa bên phải (đích của gói bóng mờ nhẹ). Hiện tượng này được gọi là chặn đầu dòng (HOL) trong một chuyển mạch xếp hàng đầu vào - một gói được xếp hàng đợi trong hàng đợi đầu vào phải chờ truyền qua kết cấu (mặc dù cổng đầu ra của nó trống) vì nó bị chặn bởi một gói khác ở đầu đường truyền. \[Karol 1987\] chỉ ra rằng do chặn HOL, hàng đợi đầu vào sẽ tăng đến độ dài không giới hạn (một cách không chính thức, điều này tương đương với việc nói rằng sẽ xảy ra mất gói đáng kể) theo một số giả định nhất định ngay khi tốc độ gói đến trên các liên kết đầu vào chỉ đạt 58% dung lượng của chúng. Một số giải pháp chặn HOL được thảo luận trong \[McKeown 1997\].

Xếp hàng đầu ra

Tiếp theo hãy xem xét liệu việc xếp hàng có thể xảy ra ở các cổng đầu ra của switch hay không. Giả sử rằng Rswitch lại nhanh hơn Rline N lần và các gói đến mỗi N cổng đầu vào đều được định hướng đến cùng một cổng đầu ra. Trong trường hợp này, trong thời gian cần thiết để gửi một gói đến liên kết đi, N gói mới sẽ đến cổng đầu ra này (một gói từ mỗi N cổng đầu vào). Vì cổng đầu ra chỉ có thể truyền một gói duy nhất trong một đơn vị thời gian (thời gian truyền gói), nên N gói đến sẽ phải xếp hàng (chờ) để truyền qua liên kết đi. Sau đó, N gói nữa có thể đến trong thời gian cần thiết để truyền chỉ một trong N gói vừa được xếp hàng trước đó. Và vân vân. Do đó, hàng đợi gói có thể hình thành tại các cổng đầu ra ngay cả khi kết cấu chuyển mạch nhanh hơn N lần so với tốc độ đường truyền cổng. Cuối cùng, số lượng gói hàng đợi có thể tăng lên đủ lớn để làm cạn kiệt bộ nhớ khả dụng ở cổng đầu ra.

Switch

vải vóc

Tranh chấp cổng đầu ra tại thời điểm t -

một gói tối có thể được chuyển

Gói màu xanh nhạt gặp phải tình trạng chặn HOL

Switch

vải vóc

Chìa khóa:

dành cho cổng đầu ra phía trên

dành cho cổng đầu ra trung bình

dành cho cổng đầu ra thấp hơn

*Hình 4.8 ♦ Chặn HOL tại và chuyển mạch xếp hàng đầu vào*

Khi không có đủ bộ nhớ để đệm một gói đến, phải đưa ra quyết định loại bỏ gói đến (chính sách được gọi là thả đuôi) hoặc loại bỏ một hoặc nhiều gói đã xếp hàng để nhường chỗ cho gói mới đến. Trong một số trường hợp, có thể thuận lợi hơn nếu bỏ (hoặc đánh dấu tiêu đề của) gói trước khi bộ đệm đầy để cung cấp tín hiệu tắc nghẽn cho người gửi. Việc đánh dấu này có thể được thực hiện bằng cách sử dụng các bit Thông báo tắc nghẽn rõ ràng mà chúng tôi đã nghiên cứu trong Phần 3.7.2. Một số chính sách đánh dấu và thả gói chủ động (được gọi chung là thuật toán quản lý hàng đợi tích cực (AQM)) đã được đề xuất và phân tích \[Labrador 1999, Hollot 2002\]. Một trong những thuật toán AQM được nghiên cứu và triển khai rộng rãi nhất là thuật toán Phát hiện sớm ngẫu nhiên (RED) \[Christiansen 2001\]. Các chính sách AQM gần đây hơn bao gồm PIE (Bộ điều khiển tích phân theo tỷ lệ được cải tiến \[RFC 8033\]) và CoDel \[Nichols 2012\].

Xếp hàng cổng đầu ra được minh họa trong Hình 4.9. Tại thời điểm t, một gói đã đến mỗi cổng đầu vào đến, mỗi cổng được gửi đến cổng đi cao nhất. Giả sử tốc độ đường truyền giống hệt nhau và một bộ chuyển mạch hoạt động ở tốc độ gấp ba lần tốc độ đường truyền, muộn hơn một đơn vị thời gian (nghĩa là trong thời gian cần thiết để nhận hoặc gửi một gói), cả ba gói ban đầu đã được chuyển đến cổng đi và được xếp hàng chờ truyền. Trong đơn vị thời gian tiếp theo, một trong ba gói này sẽ được truyền qua liên kết đi. Trong ví dụ của chúng tôi, hai gói tin mới đã đến phía đầu vào của

Switch

vải vóc

Tranh chấp cổng đầu ra tại thời điểm t

Một gói thời gian sau

Switch

vải vóc

*Hình 4.9 ♦ Xếp hàng cổng đầu ra*

công tắc; một trong những gói này được dành cho cổng đầu ra cao nhất này. Hậu quả của việc xếp hàng như vậy là bộ lập lịch gói tại cổng đầu ra phải chọn một gói trong số các gói được xếp hàng để truyền - một chủ đề chúng ta sẽ đề cập trong phần sau.

Bao nhiêu bộ đệm là "Đủ?"

Nghiên cứu của chúng tôi ở trên đã chỉ ra cách hàng đợi gói hình thành khi các gói gói đến cổng đầu vào hoặc cổng đầu ra (nhiều khả năng) của bộ định tuyến và tốc độ đến gói tạm thời vượt quá tốc độ gói có thể được chuyển tiếp. Khoảng thời gian không khớp này tồn tại càng lâu thì hàng đợi sẽ càng dài, cho đến khi bộ đệm của một cổng trở nên đầy và các gói bị loại bỏ. Một câu hỏi tự nhiên là nên cung cấp bao nhiêu vùng đệm tại một cảng. Hóa ra câu trả lời cho câu hỏi này phức tạp hơn nhiều so với những gì người ta có thể tưởng tượng và có thể dạy chúng ta khá nhiều điều về sự tương tác tinh tế giữa những người gửi nhận biết tắc nghẽn ở rìa mạng và lõi mạng!

**Trong nhiều năm, nguyên tắc chung \[RFC 3439\] đối với kích thước bộ đệm là lượng bộ đệm (B) phải bằng thời gian khứ hồi trung bình (RTT, giả sử là 250 mgiây) nhân với dung lượng liên kết (C). Do đó, liên kết 10 Gbps có RTT là 250 msec sẽ cần lượng bộ đệm bằng B = RTT \# C = 2,5 Gbit bộ đệm. Kết quả này dựa trên phân tích động lực xếp hàng của một số lượng tương đối nhỏ TCP luồng \[Villamizar 1994\]. Tuy nhiên, những nỗ lực lý thuyết và thử nghiệm gần đây hơn \[Appenzeller 2004\] cho thấy rằng khi một số lượng lớn các luồng TCP độc lập (N) đi qua một liên kết thì lượng bộ đệm cần thiết là B = RTT \# C\> 2N. Trong các mạng lõi, nơi một số lượng lớn luồng TCP thường đi qua các liên kết bộ định tuyến đường trục lớn, giá trị của N có thể lớn, với việc giảm kích thước bộ đệm cần thiết trở nên khá đáng kể. \[Appenzeller 2004; Wischik 2005; Beheshti 2008\] cung cấp các thảo luận rất dễ đọc về vấn đề kích thước bộ đệm từ quan điểm lý thuyết, triển khai và vận hành.**

Thật thú vị khi nghĩ rằng nhiều bộ đệm hơn phải tốt hơn---bộ đệm lớn hơn sẽ cho phép bộ định tuyến hấp thụ những biến động lớn hơn về tốc độ đến của gói, do đó làm giảm tỷ lệ mất gói của bộ định tuyến. Nhưng bộ đệm lớn hơn cũng có nghĩa là độ trễ xếp hàng có thể kéo dài hơn. Đối với người chơi game và người dùng hội nghị truyền hình tương tác, chỉ tính hàng chục mili giây. Việc tăng số lượng bộ đệm trên mỗi bước nhảy lên 10 lần để giảm mất gói có thể làm tăng độ trễ đầu cuối lên gấp 10 lần! RTT tăng cũng làm cho TCP người gửi ít phản hồi hơn và phản hồi chậm hơn trước tình trạng tắc nghẽn mới bắt đầu và/hoặc mất gói. Những cân nhắc dựa trên độ trễ này cho thấy rằng việc lưu vào bộ đệm là một con dao hai lưỡi---bộ đệm có thể được sử dụng để hấp thụ những biến động thống kê ngắn hạn về lưu lượng truy cập nhưng cũng có thể dẫn đến độ trễ gia tăng và những lo ngại liên quan. Việc đệm cũng hơi giống muối---chỉ cần một lượng muối phù hợp sẽ khiến thức ăn ngon hơn, nhưng quá nhiều sẽ khiến thức ăn không ăn được!

Trong cuộc thảo luận ở trên, chúng tôi đã ngầm giả định rằng nhiều người gửi độc lập đang cạnh tranh băng thông và bộ đệm tại một liên kết bị tắc nghẽn. Mặc dù đây có lẽ là một giả định tuyệt vời cho các bộ định tuyến trong lõi mạng, nhưng ở biên mạng

điều này có thể không giữ được. Hình 4.10(a) hiển thị bộ định tuyến tại nhà gửi các phân đoạn TCP tới máy chủ trò chơi từ xa. Theo \[Nichols 2012\], giả sử rằng phải mất 20 mili giây để truyền một gói (chứa phân đoạn TCP của người chơi), có độ trễ xếp hàng không đáng kể ở những nơi khác trên đường dẫn đến máy chủ trò chơi và RTT là 200 mili giây. Như trong Hình 4.10(b), giả sử rằng tại thời điểm t = 0, một loạt 25 gói đến hàng đợi. Sau đó, một trong những gói được xếp hàng này sẽ được truyền đi cứ sau 20 ms, do đó tại thời điểm t = 200 ms, ACK đầu tiên sẽ đến, giống như gói thứ 21 đang được truyền. Việc ACK đến này khiến người gửi TCP gửi một gói khác được xếp hàng đợi tại liên kết gửi đi của bộ định tuyến gia đình. Tại thời điểm t = 220, ACK tiếp theo sẽ đến và một phân đoạn TCP khác được người chơi phát hành và được xếp hàng đợi khi gói thứ 22 đang được truyền đi, v.v. Bạn nên thuyết phục bản thân rằng trong trường hợp này, việc tính giờ ACK sẽ dẫn đến một gói mới đến hàng đợi mỗi khi gói được xếp hàng đợi được gửi đi, dẫn đến kích thước hàng đợi tại liên kết gửi đi của bộ định tuyến gia đình luôn là năm gói! Nghĩa là, đường ống đầu cuối đã đầy (chuyển các gói đến đích với tốc độ nghẽn cổ chai đường dẫn là một gói cứ sau 20 ms), nhưng độ trễ hàng đợi là không đổi và liên tục. Kết quả là, game thủ không hài lòng với độ trễ và phụ huynh (thậm chí còn biết đến Wireshark!) cảm thấy bối rối vì họ không hiểu tại sao độ trễ lại kéo dài và kéo dài quá mức, ngay cả khi không có lưu lượng truy cập nào khác trên mạng gia đình.

Kịch bản trên về độ trễ kéo dài do tình trạng lưu vào bộ đệm liên tục được gọi là vùng đệm và minh họa rằng không chỉ thông lượng quan trọng mà độ trễ tối thiểu cũng quan trọng \[Kleinrock 2018\] và sự tương tác giữa những người gửi ở rìa mạng và hàng đợi trong mạng thực sự có thể phức tạp và tinh tế. Tiêu chuẩn DOCSIS 3.1 dành cho mạng cáp mà chúng ta sẽ nghiên cứu trong Chương 6, gần đây đã bổ sung một cơ chế AQM cụ thể \[RFC 8033, RFC 8034\] để chống lại hiện tượng phồng đệm, đồng thời duy trì hiệu suất thông lượng lớn.

250 mili giây RTT

Thời gian (ms)

chiều dài hàng đợi

Một. b.

Mạng gia đình

internet

*Hình 4.10 ♦ Bufferbloat: hàng đợi liên tục*

**4.2.5 Packet Lập kế hoạch**

Bây giờ chúng ta hãy quay lại câu hỏi xác định thứ tự các gói được xếp hàng đợi được truyền qua một liên kết đi. Vì bản thân bạn chắc chắn đã nhiều lần phải xếp hàng dài chờ đợi và quan sát cách phục vụ khách hàng chờ đợi, nên chắc chắn bạn đã quen thuộc với nhiều nguyên tắc xếp hàng thường được sử dụng trong các bộ định tuyến. Có cơ chế đến trước được phục vụ trước (FCFS hay còn gọi là nhập trước xuất trước FIFO). Người Anh nổi tiếng với việc kiên nhẫn và trật tự trong việc xếp hàng FCFS tại các bến xe buýt và trong chợ ("Ồ, bạn đang xếp hàng à?"). Các quốc gia khác hoạt động trên cơ sở ưu tiên, trong đó một nhóm khách hàng đang chờ được ưu tiên phục vụ hơn các khách hàng đang chờ khác. Ngoài ra còn có xếp hàng vòng tròn, trong đó khách hàng lại được chia thành các lớp (như trong xếp hàng ưu tiên) nhưng mỗi lớp khách hàng lần lượt được cung cấp dịch vụ.

Nhập trước xuất trước (FIFO)

Hình 4.11 cho thấy sự trừu tượng hóa mô hình xếp hàng cho nguyên tắc lập lịch liên kết FIFO. Packets đến hàng đợi đầu ra liên kết, chờ truyền nếu liên kết hiện đang bận truyền gói khác. Nếu không có đủ không gian đệm để giữ gói đến, chính sách loại bỏ gói của hàng đợi sẽ xác định xem gói sẽ bị loại bỏ (mất) hay các gói khác sẽ bị xóa khỏi hàng đợi để tạo khoảng trống cho gói đến, như đã thảo luận ở trên. Trong cuộc thảo luận bên dưới, chúng tôi sẽ bỏ qua việc loại bỏ gói. Khi một gói được truyền hoàn toàn qua liên kết đi (nghĩa là nhận dịch vụ), nó sẽ bị xóa khỏi hàng đợi.

Nguyên tắc lập lịch FIFO (còn được gọi là đến trước được phục vụ trước hoặc FCFS) chọn các gói để truyền liên kết theo cùng thứ tự mà chúng đến hàng đợi liên kết đầu ra. Tất cả chúng ta đều quen thuộc với việc xếp hàng FIFO từ các trung tâm dịch vụ, nơi khách hàng đến xếp hàng ở phía sau của một hàng chờ duy nhất, giữ nguyên trật tự và sau đó được phục vụ khi họ đến đầu hàng. Hình 4.12 thể hiện hàng đợi FIFO đang hoạt động. Packet các lượt đến được biểu thị bằng các mũi tên được đánh số phía trên dòng thời gian phía trên, với số cho biết thứ tự gói tin đến. Các gói khởi hành riêng lẻ được hiển thị bên dưới dòng thời gian phía dưới. Thời gian gói tin sử dụng (đang được truyền) được biểu thị bằng hình chữ nhật được tô bóng giữa hai mốc thời gian. TRONG

Nơi đến Khởi hành

Hàng đợi (khu vực chờ)

Liên kết (máy chủ)

*Hình 4.11 ♦ Trừu tượng hóa hàng đợi FIFO*

ví dụ của chúng tôi ở đây, giả sử rằng mỗi gói mất ba đơn vị thời gian để truyền đi. Theo nguyên tắc FIFO, các gói sẽ rời đi theo đúng thứ tự mà chúng đến. Lưu ý rằng sau khi gói 4 rời đi, liên kết vẫn không hoạt động (vì các gói 1 đến 4 đã được truyền và xóa khỏi hàng đợi) cho đến khi gói 5 đến.

Xếp hàng ưu tiên

Theo hàng đợi ưu tiên, các gói đến liên kết đầu ra được phân loại thành các lớp ưu tiên khi đến hàng đợi, như trong Hình 4.13. Trong thực tế, nhà điều hành mạng có thể định cấu hình hàng đợi để các gói mang thông tin quản lý mạng (ví dụ: như được biểu thị bằng số cổng nguồn hoặc đích TCP/UDP) được ưu tiên hơn lưu lượng truy cập của người dùng; Ngoài ra, các gói thoại qua thời gian thựcIP có thể được ưu tiên hơn so với lưu lượng truy cập không theo thời gian thực như các gói e-mail. Mỗi lớp ưu tiên thường có hàng đợi riêng. Khi chọn gói để truyền, mức độ ưu tiên

Thời gian

Lượt đến

Khởi hành

Packet đang phục vụ

Thời gian

t = 0 t = 2 t = 4 t = 6 t = 8 t = 10 t = 12 t = 14

*Hình 4.12 ♦ Hàng đợi FIFO đang hoạt động*

Nơi đến Khởi hành

Hàng đợi có mức độ ưu tiên thấp

(khu vực chờ)

Phân loại

Hàng đợi ưu tiên cao

(khu vực chờ)

Liên kết (máy chủ)

*Hình 4.13 ♦ Mô hình xếp hàng ưu tiên*

TRUNG LẬP NET

Chúng ta đã thấy rằng các cơ chế lập lịch gói (ví dụ: lập lịch lưu lượng ưu tiên có mức độ ưu tiên nghiêm ngặt và WFQ) có thể được sử dụng để cung cấp các mức dịch vụ khác nhau cho các "lớp" lưu lượng khác nhau. Định nghĩa về những gì cấu thành chính xác một "loại" lưu lượng truy cập tùy thuộc vào ISP quyết định, nhưng có thể dựa trên bất kỳ tập hợp trường nào trong tiêu đề gói dữ liệu IP. Ví dụ: trường cổng trong tiêu đề gói dữ liệu IP có thể được sử dụng để phân loại các gói dữ liệu theo "dịch vụ nổi tiếng" được liên kết với cổng đó: Gói dữ liệu quản lý mạng SNMP (cổng 161) có thể được gán cho lớp ưu tiên cao hơn gói dữ liệu giao thức e-mail IMAP (cổng 143 hoặc 993) và do đó nhận được dịch vụ tốt hơn. ISP cũng có thể sử dụng địa chỉ nguồn IP của gói dữ liệu để cung cấp mức độ ưu tiên cho các gói dữ liệu được gửi bởi một số công ty nhất định (những người có lẽ đã trả tiền cho ISP để có được đặc quyền này) so với các gói dữ liệu được gửi từ các công ty khác (những người chưa trả tiền); một ISP

NGUYÊN TẮC TRONG THỰC HÀNH

kỷ luật xếp hàng sẽ truyền một gói từ lớp ưu tiên cao nhất có hàng đợi không trống (nghĩa là có các gói đang chờ truyền). Việc lựa chọn giữa các gói có cùng mức độ ưu tiên thường được thực hiện theo cách FIFO.

Hình 4.14 minh họa hoạt động của hàng đợi ưu tiên với hai lớp ưu tiên. Packets 1, 3 và 4 thuộc lớp ưu tiên cao, còn các gói 2 và 5 thuộc lớp ưu tiên thấp. Packet 1 đến và nhận thấy liên kết không hoạt động, bắt đầu truyền. Trong quá trình truyền gói 1, gói 2 và 3 sẽ đến và được xếp vào hàng đợi có mức độ ưu tiên thấp và cao tương ứng. Sau khi truyền gói 1, gói 3 (gói có mức độ ưu tiên cao) được chọn để truyền qua gói 2 (gói này, mặc dù đến sớm hơn, vẫn là gói có mức độ ưu tiên thấp). Khi kết thúc quá trình truyền gói 3, gói 2 sẽ bắt đầu truyền. Packet 4 (gói có mức độ ưu tiên cao) đến trong quá trình truyền gói 2 (gói có mức độ ưu tiên thấp). Theo nguyên tắc xếp hàng ưu tiên không ưu tiên trước, việc truyền gói tin không bị gián đoạn một khi nó

Lượt đến

Khởi hành

Packet đang phục vụ

Thời gian

Thời gian t = 0 t = 2 t = 4 t = 6 t = 8 t = 10 t = 12 t = 14

*Hình 4.14 ♦ Hàng đợi ưu tiên đang hoạt động*

thậm chí có thể chặn lưu lượng truy cập bằng địa chỉ nguồn IP ở một công ty hoặc quốc gia nhất định. Có nhiều cơ chế cho phép ISP cung cấp các mức dịch vụ khác nhau cho các loại lưu lượng khác nhau. Câu hỏi thực sự là những chính sách và luật nào xác định những gì ISP thực sự có thể làm. Tất nhiên, những luật này sẽ khác nhau tùy theo quốc gia; xem \[Smithsonian 2017\] để biết bản khảo sát ngắn gọn. Ở đây, chúng ta sẽ xem xét ngắn gọn chính sách của Hoa Kỳ về cái được gọi là "tính trung lập ròng".

Thuật ngữ "tính trung lập ròng" không có quyết định chính xác, nhưng Lệnh về Bảo vệ và Thúc đẩy Internet Mở \[FCC 2015\] tháng 3 năm 2015 của Ủy ban Truyền thông Liên bang Hoa Kỳ cung cấp ba quy tắc "rõ ràng, rõ ràng" hiện nay thường được liên kết với tính trung lập ròng:

• "Không chặn. . . . Một người tham gia cung cấp dịch vụ truy cập Internet băng thông rộng, . . . sẽ không chặn nội dung, ứng dụng, dịch vụ hợp pháp hoặc thiết bị không gây hại, tùy theo sự quản lý mạng hợp lý." • "Không hạn chế. . . . Một người tham gia cung cấp dịch vụ truy cập Internet băng thông rộng,\... không được làm suy giảm hoặc suy giảm lưu lượng truy cập Internet hợp pháp dựa trên nội dung, ứng dụng hoặc dịch vụ Internet hoặc việc sử dụng thiết bị không gây hại, tùy thuộc vào sự quản lý mạng hợp lý." • \"Không ưu tiên trả phí\.... Một người tham gia cung cấp dịch vụ truy cập Internet băng thông rộng, \.... sẽ không tham gia vào ưu tiên trả phí. \"Ưu tiên trả phí\" đề cập đến việc quản lý mạng của nhà cung cấp băng thông rộng để trực tiếp hoặc gián tiếp ưu tiên một số lưu lượng truy cập hơn lưu lượng truy cập khác, bao gồm thông qua việc sử dụng các kỹ thuật như định hình lưu lượng truy cập, ưu tiên, đặt trước tài nguyên hoặc các hình thức quản lý lưu lượng ưu tiên khác,\....\"

Khá thú vị, trước Lệnh, các hành vi của ISP vi phạm hai quy tắc đầu tiên đã được tuân thủ \[Faulhaber 2012\]. Năm 2005, một ISP ở Bắc Carolina đã đồng ý ngừng hoạt động chặn khách hàng sử dụng Vonage, một dịch vụ lồng tiếngIP cạnh tranh với dịch vụ điện thoại của chính họ. Năm 2007, Comcast bị đánh giá là đã can thiệp vào lưu lượng BitTorrent P2P bằng cách tạo và gửi nội bộ các gói TCP RST tới người gửi và người nhận BitTorrent, khiến họ đóng kết nối BitTorrent \[FCC 2008\].

Cả hai bên trong cuộc tranh luận về tính trung lập ròng đã được tranh luận gay gắt, chủ yếu tập trung vào mức độ mà tính trung lập ròng mang lại lợi ích cho khách hàng, đồng thời thúc đẩy sự đổi mới. Xem \[Peha 2006, Faulhaber 2012, Economides 2017, Madhyastha 2017\].

Lệnh FCC năm 2015 về Bảo vệ và Thúc đẩy Internet Mở, trong đó cấm các ISP chặn, hạn chế hoặc cung cấp mức ưu tiên trả phí, đã được thay thế bằng Lệnh Khôi phục Tự do Internet năm 2017 của FCC, \[FCC 2017\], trong đó hủy bỏ các lệnh cấm này và thay vào đó tập trung vào tính minh bạch của ISP. Với rất nhiều sự quan tâm và rất nhiều thay đổi, có thể an toàn khi nói rằng chúng ta chưa thấy chương cuối cùng được viết về tính trung lập ròng ở Hoa Kỳ hoặc ở nơi khác.

đã bắt đầu. Trong trường hợp này, gói 4 xếp hàng để truyền và bắt đầu được truyền sau khi quá trình truyền gói 2 hoàn tất.

Xếp hàng theo vòng tròn và xếp hàng công bằng có trọng số (WFQ)

Theo nguyên tắc xếp hàng vòng tròn, các gói được sắp xếp thành các lớp giống như xếp hàng ưu tiên. Tuy nhiên, thay vì có mức độ ưu tiên dịch vụ nghiêm ngặt giữa các lớp, bộ lập lịch luân chuyển luân phiên dịch vụ giữa các lớp. Trong dạng lập lịch vòng tròn đơn giản nhất, gói lớp 1 được truyền đi, tiếp theo là gói lớp 2, tiếp theo là gói lớp 1, tiếp theo là gói lớp 2, v.v. Cái gọi là kỷ luật xếp hàng bảo toàn công việc sẽ không bao giờ cho phép liên kết không hoạt động bất cứ khi nào có các gói (thuộc bất kỳ loại nào) được xếp hàng để truyền. Kỷ luật quay vòng bảo toàn công việc tìm kiếm gói của một lớp nhất định nhưng không tìm thấy gói nào sẽ ngay lập tức kiểm tra lớp tiếp theo theo trình tự vòng tròn.

Hình 4.15 minh họa hoạt động của hàng đợi quay vòng hai lớp. Trong ví dụ này, các gói 1, 2 và 4 thuộc về lớp 1, các gói 3 và 5 thuộc về lớp thứ hai. Packet 1 bắt đầu truyền ngay khi đến hàng đợi đầu ra. Packets 2 và 3 đến trong quá trình truyền gói 1 và do đó xếp hàng để truyền. Sau khi truyền gói 1, bộ lập lịch liên kết sẽ tìm gói lớp 2 và do đó truyền gói 3. Sau khi truyền gói 3, bộ lập lịch sẽ tìm gói lớp 1 và do đó truyền gói 2. Sau khi truyền gói 2, gói 4 là gói duy nhất được xếp hàng đợi; do đó nó được truyền ngay sau gói 2.

Một dạng tổng quát của xếp hàng vòng tròn đã được triển khai rộng rãi trong các bộ định tuyến được gọi là kỷ luật xếp hàng công bằng có trọng số (WFQ) \[Demers 1990; Parekh 1993. WFQ được minh họa trong Hình 4.16. Tại đây, các gói đến được phân loại và xếp hàng trong khu vực chờ thích hợp cho mỗi lớp. Giống như lập lịch vòng tròn, bộ lập lịch WFQ sẽ phục vụ các lớp theo cách vòng tròn---đầu tiên phục vụ lớp 1, sau đó phục vụ lớp 2, sau đó phục vụ lớp 3 và sau đó (giả sử có ba lớp) lặp lại mẫu dịch vụ. WFQ cũng là một nguyên tắc xếp hàng bảo toàn công việc và

Lượt đến

Packet đang phục vụ

Khởi hành

Thời gian

Thời gian t = 0 t = 2 t = 4 t = 6 t = 8 t = 10 t = 12 t = 14

*Hình 4.15 ♦ Hàng đợi robin hai lớp đang hoạt động*

do đó sẽ ngay lập tức chuyển sang lớp tiếp theo trong chuỗi dịch vụ khi tìm thấy hàng đợi lớp trống.

**WFQ khác với vòng tròn ở chỗ mỗi lớp có thể nhận được lượng dịch vụ khác nhau trong bất kỳ khoảng thời gian nào. Cụ thể, mỗi lớp i được gán một trọng số wi. Theo WFQ, trong bất kỳ khoảng thời gian nào có các gói lớp i được gửi, lớp i sau đó sẽ được đảm bảo nhận được một phần dịch vụ bằng wi\>(gwj), trong đó tổng ở mẫu số được lấy trên tất cả các lớp cũng có các gói được xếp hàng đợi để truyền. Trong trường hợp xấu nhất, ngay cả khi tất cả các lớp đều có các gói được xếp hàng đợi, lớp i vẫn sẽ được đảm bảo nhận được một phần wi \>(gwj) băng thông, trong trường hợp xấu nhất này tổng trong mẫu số là trên tất cả các lớp. Do đó, đối với một liên kết có tốc độ truyền R, lớp i sẽ luôn đạt được thông lượng ít nhất là R \# wi \>(gwj). Mô tả của chúng tôi về WFQ đã được lý tưởng hóa, vì chúng tôi chưa xem xét thực tế là các gói là rời rạc và việc truyền gói sẽ không bị gián đoạn để bắt đầu truyền gói khác; \[Demers 1990; Parekh 1993\] thảo luận về vấn đề đóng gói này.**

**4.3 Giao thức Internet (IP): IPv4, Đánh địa chỉ, IPv6, v.v.**

Nghiên cứu của chúng ta về lớp mạng cho đến nay trong Chương 4---khái niệm về thành phần dữ liệu và mặt phẳng điều khiển của lớp mạng, sự phân biệt giữa chuyển tiếp và định tuyến, nhận dạng các mô hình dịch vụ mạng khác nhau và cái nhìn của chúng ta bên trong một bộ định tuyến---thường không tham chiếu đến bất kỳ kiến ​​trúc hoặc giao thức mạng máy tính cụ thể nào. Trong phần này, chúng ta sẽ tập trung vào các khía cạnh chính của lớp mạng trên Internet ngày nay và Giao thức Internet nổi tiếng (IP).

Hiện nay có hai phiên bản IP được sử dụng. Trước tiên, chúng ta sẽ xem xét giao thức IP phiên bản 4 được triển khai rộng rãi, thường được gọi đơn giản là IPv4 \[RFC 791\] trong Phần 4.3.1. Chúng tôi sẽ kiểm tra IP phiên bản 6 \[RFC 2460; RFC 4291\], có

Phân loại nơi đến nơi khởi hành

w1

w2

liên kết w3

*Hình 4.16 ♦ Xếp hàng công bằng có trọng số*

được đề xuất thay thế IPv4, trong Phần 4.3.4. Ở giữa, chúng ta sẽ chủ yếu đề cập đến việc đánh địa chỉ Internet---một chủ đề có vẻ khá khô khan và thiên về chi tiết nhưng chúng ta sẽ thấy điều quan trọng là phải hiểu cách thức hoạt động của lớp mạng Internet. Nắm vững địa chỉ IP chính là nắm vững chính lớp mạng của Internet!

**4.3.1 Định dạng IPv4 Datagram**

Hãy nhớ lại rằng gói lớp mạng của Internet được gọi là datagram. Chúng tôi bắt đầu nghiên cứu về IP bằng cái nhìn tổng quan về cú pháp và ngữ nghĩa của gói dữ liệu IPv4. Bạn có thể nghĩ rằng không có gì khô khan hơn cú pháp và ngữ nghĩa của các bit trong gói. Tuy nhiên, datagram đóng vai trò trung tâm trên Internet---mọi sinh viên mạng và chuyên gia đều cần xem, tiếp thu và làm chủ nó. (Và để biết rằng các tiêu đề giao thức thực sự có thể thú vị khi nghiên cứu, hãy xem \[Pomeranz 2010\]). Định dạng datagram IPv4 được hiển thị trong Hình 4.17. Các trường chính trong datagram IPv4 như sau:

• Số phiên bản. 4 bit này chỉ định phiên bản giao thức IP của datagram. Bằng cách xem số phiên bản, bộ định tuyến có thể xác định cách diễn giải phần còn lại của gói dữ liệu IP. Các phiên bản khác nhau của IP sử dụng các định dạng datagram khác nhau. Định dạng datagram cho IPv4 được hiển thị trong Hình 4.17. Định dạng datagram cho phiên bản mới của IP (IPv6) được thảo luận trong Phần 4.3.4. • chiều dài Header. Bởi vì một datagram IPv4 có thể chứa một số lượng tùy chọn khác nhau (được bao gồm trong tiêu đề của datagram IPv4), nên cần có 4 bit này

Phiên bản Loại dịch vụ Header

chiều dài

Lớp trên

giao thức

Bộ nhận dạng 16-bit

Thời gian để sống

Cờ bù phân mảnh 13 bit

Datagram độ dài (byte)

Header tổng kiểm tra

32 bit

Địa chỉ nguồn 32-bit IP

Địa chỉ đích 32-bit IP

Tùy chọn (nếu có)

dữ liệu

*Hình 4.17 ♦ IPv4 định dạng datagram*

để xác định vị trí trong gói dữ liệu IP tải trọng (ví dụ: phân đoạn lớp vận chuyển được gói gọn trong gói dữ liệu này) thực sự bắt đầu. Hầu hết các datagram IP không chứa các tùy chọn, do đó, datagram IP điển hình có tiêu đề 20 byte. • Loại hình dịch vụ. Các bit loại dịch vụ (TOS) được bao gồm trong tiêu đề IPv4 để cho phép phân biệt các loại gói dữ liệu IP khác nhau với nhau. Ví dụ: có thể hữu ích khi phân biệt các gói dữ liệu thời gian thực (chẳng hạn như các gói được sử dụng bởi ứng dụng điện thoại IP) với lưu lượng truy cập không theo thời gian thực (ví dụ: FTP). Mức độ dịch vụ cụ thể được cung cấp là vấn đề chính sách được quản trị viên mạng xác định và định cấu hình cho bộ định tuyến đó. Chúng ta cũng đã biết trong Phần 3.7.2 rằng hai trong số các bit TOS được sử dụng cho Thông báo tắc nghẽn rõ ràng. • chiều dài Datagram. Đây là tổng chiều dài của gói dữ liệu IP (tiêu đề cộng với dữ liệu), được đo bằng byte. Vì trường này dài 16 bit nên kích thước tối đa theo lý thuyết của gói dữ liệu IP là 65.535 byte. Tuy nhiên, các gói dữ liệu hiếm khi lớn hơn 1.500 byte, điều này cho phép gói dữ liệu IP vừa với trường tải trọng của khung Ethernet có kích thước tối đa. • Định danh, cờ, bù phân mảnh. Ba trường này liên quan đến cái gọi là phân mảnh IP, khi một gói dữ liệu IP lớn được chia thành nhiều gói dữ liệu IP nhỏ hơn, sau đó được chuyển tiếp độc lập đến đích, nơi chúng được tập hợp lại trước khi dữ liệu tải trọng của chúng (xem bên dưới) được chuyển lên lớp vận chuyển tại máy chủ đích. Điều thú vị là phiên bản mới của IP, IPv6 không cho phép phân mảnh. Chúng tôi sẽ không đề cập đến sự phân mảnh ở đây; nhưng độc giả có thể tìm thấy phần thảo luận chi tiết trên mạng, trong số những tài liệu "đã bị loại bỏ" từ các phiên bản trước của cuốn sách này. • Thời gian sống. Trường thời gian tồn tại (TTL) được đưa vào để đảm bảo rằng các gói dữ liệu không lưu hành mãi mãi (ví dụ: do vòng lặp định tuyến tồn tại lâu) trong mạng. Trường này được giảm đi một mỗi lần datagram được xử lý bởi bộ định tuyến. Nếu trường TTL đạt tới 0, bộ định tuyến phải loại bỏ datagram đó. • Giao thức. Trường này thường chỉ được sử dụng khi gói dữ liệu IP đến đích cuối cùng. Giá trị của trường này cho biết giao thức lớp vận chuyển cụ thể mà phần dữ liệu của gói dữ liệu IP này sẽ được chuyển tới. Ví dụ: giá trị 6 cho biết phần dữ liệu được chuyển tới TCP, trong khi giá trị 17 chỉ ra rằng dữ liệu được chuyển tới UDP. Để biết danh sách tất cả các giá trị có thể có, hãy xem \[Số giao thức IANA 2016\]. Lưu ý rằng số giao thức trong gói dữ liệu IP có vai trò tương tự như vai trò của trường số cổng trong phân đoạn lớp vận chuyển. Số giao thức là chất keo gắn kết mạng và các lớp vận chuyển với nhau, trong khi số cổng là chất keo gắn kết các lớp vận chuyển và ứng dụng với nhau. Chúng ta sẽ thấy trong Chương 6 rằng khung lớp liên kết cũng có một trường đặc biệt liên kết lớp liên kết với lớp mạng. • Header tổng kiểm tra. Tổng kiểm tra tiêu đề hỗ trợ bộ định tuyến phát hiện lỗi bit trong gói dữ liệu IP đã nhận. Tổng kiểm tra tiêu đề được tính bằng cách xử lý mỗi 2 byte trong tiêu đề dưới dạng số và tính tổng các số này bằng cách sử dụng số học bù 1. Như đã thảo luận trong Phần 3.3, phần bù 1 của tổng này, được gọi là tổng kiểm tra Internet, được lưu trữ trong trường tổng kiểm tra. Bộ định tuyến tính toán tổng kiểm tra tiêu đề cho mỗi gói dữ liệu IP nhận được và phát hiện tình trạng lỗi nếu

tổng kiểm tra mang trong tiêu đề gói dữ liệu không bằng tổng kiểm tra được tính toán. Routers thường loại bỏ các datagram đã được phát hiện có lỗi. Lưu ý rằng tổng kiểm tra phải được tính toán lại và lưu trữ lại ở mỗi bộ định tuyến, vì trường TTL và có thể cả trường tùy chọn cũng sẽ thay đổi. Một cuộc thảo luận thú vị về các thuật toán nhanh để tính tổng kiểm tra Internet là \[RFC 1071\]. Một câu hỏi thường được đặt ra vào thời điểm này là tại sao TCP/IP thực hiện kiểm tra lỗi ở cả lớp truyền tải và lớp mạng? Có một số lý do cho sự lặp lại này. Trước tiên, hãy lưu ý rằng chỉ tiêu đề IP mới được kiểm tra tổng ở lớp IP, trong khi tổng kiểm tra TCP/ UDP được tính trên toàn bộ phân đoạn TCP/UDP. Thứ hai, TCP/ UDP và IP không nhất thiết phải thuộc cùng một ngăn xếp giao thức. Về nguyên tắc, TCP có thể chạy trên một giao thức lớp mạng khác (ví dụ: ATM) \[Black 1995\]) và IP có thể mang dữ liệu sẽ không được chuyển đến TCP/UDP. • Địa chỉ nguồn và đích IP. Khi một nguồn tạo một datagram, nó sẽ chèn địa chỉ IP của nó vào trường địa chỉ IP nguồn và chèn địa chỉ của đích cuối cùng vào trường địa chỉ IP đích. Thông thường, máy chủ nguồn xác định địa chỉ đích thông qua tra cứu DNS, như đã thảo luận trong Chương 2. Chúng ta sẽ thảo luận chi tiết về địa chỉ IP trong Phần 4.3.2. • Tùy chọn. Các trường tùy chọn cho phép mở rộng tiêu đề IP. Các tùy chọn Header vốn hiếm khi được sử dụng---do đó quyết định tiết kiệm chi phí bằng cách không đưa thông tin vào các trường tùy chọn vào mỗi tiêu đề gói dữ liệu. Tuy nhiên, sự tồn tại đơn thuần của các tùy chọn cũng làm phức tạp vấn đề---vì các tiêu đề gói dữ liệu có thể có độ dài thay đổi, nên người ta không thể xác định tiên nghiệm nơi trường dữ liệu sẽ bắt đầu. Ngoài ra, vì một số gói dữ liệu có thể yêu cầu xử lý tùy chọn còn những gói khác thì không, lượng thời gian cần thiết để xử lý gói dữ liệu IP tại bộ định tuyến có thể khác nhau rất nhiều. Những cân nhắc này trở nên đặc biệt quan trọng đối với quá trình xử lý IP trong bộ định tuyến và máy chủ hiệu suất cao. Vì những lý do này và những lý do khác, các tùy chọn IP không được đưa vào tiêu đề IPv6, như đã thảo luận trong Phần 4.3.4. • Dữ liệu (tải trọng). Cuối cùng, chúng ta đến với trường cuối cùng và quan trọng nhất---lý do tồn tại của datagram ngay từ đầu! Trong hầu hết các trường hợp, trường dữ liệu của gói dữ liệu IP chứa phân đoạn lớp vận chuyển (TCP hoặc UDP) sẽ được chuyển đến đích. Tuy nhiên, trường dữ liệu có thể mang các loại dữ liệu khác, chẳng hạn như thông báo ICMP (được thảo luận trong Phần 5.6).

Lưu ý rằng một datagram IP có tổng cộng 20 byte tiêu đề (giả sử không có tùy chọn nào). Nếu gói dữ liệu mang phân đoạn TCP thì mỗi gói dữ liệu mang tổng cộng 40 byte tiêu đề (20 byte tiêu đề IP cộng với 20 byte tiêu đề TCP) cùng với thông báo lớp ứng dụng.

**4.3.2 IPv4 Đánh địa chỉ**

Bây giờ chúng ta chuyển sự chú ý sang việc đánh địa chỉ IPv4. Mặc dù bạn có thể nghĩ rằng việc đánh địa chỉ phải là một chủ đề đơn giản, hy vọng đến cuối phần này bạn sẽ tin rằng việc đánh địa chỉ Internet không chỉ là một chủ đề thú vị, tinh tế và thú vị.

nhưng cũng là một trong những thứ có tầm quan trọng trung tâm đối với Internet. Bạn có thể tìm thấy cách xử lý tuyệt vời về cách đánh địa chỉ IPv4 trong chương đầu tiên của \[Stewart 1999\].

Tuy nhiên, trước khi thảo luận về địa chỉ IP, chúng ta cần nói đôi điều về cách các máy chủ và bộ định tuyến được kết nối với Internet. Một máy chủ thường chỉ có một liên kết duy nhất vào mạng; khi IP trong máy chủ muốn gửi một datagram, nó sẽ thực hiện việc đó qua liên kết này. Ranh giới giữa máy chủ và liên kết vật lý được gọi là giao diện. Bây giờ hãy xem xét một bộ định tuyến và các giao diện của nó. Bởi vì công việc của bộ định tuyến là nhận một datagram trên một liên kết và chuyển tiếp datagram trên một số liên kết khác, nên một bộ định tuyến nhất thiết phải có hai hoặc nhiều liên kết mà nó được kết nối. Ranh giới giữa bộ định tuyến và bất kỳ liên kết nào của nó cũng được gọi là giao diện. Do đó, một bộ định tuyến có nhiều giao diện, mỗi giao diện cho mỗi liên kết của nó. Bởi vì mọi máy chủ và bộ định tuyến đều có khả năng gửi và nhận IP datagram, IP yêu cầu mỗi giao diện máy chủ và bộ định tuyến phải có địa chỉ IP riêng. Do đó, địa chỉ IP được liên kết về mặt kỹ thuật với một giao diện, thay vì với máy chủ hoặc bộ định tuyến chứa giao diện đó.

Mỗi địa chỉ IP dài 32 bit (tương đương 4 byte) và do đó có tổng cộng 232 (hoặc khoảng 4 tỷ) địa chỉ IP có thể có. Các địa chỉ này thường được viết bằng cái gọi là ký hiệu thập phân chấm, trong đó mỗi byte của địa chỉ được viết ở dạng thập phân và được phân tách bằng dấu chấm (dấu chấm) khỏi các byte khác trong địa chỉ. Ví dụ: hãy xem xét địa chỉ IP 193.32.216.9. 193 là số thập phân tương đương với 8 bit đầu tiên của địa chỉ; 32 là số thập phân tương đương với 8 bit thứ hai của địa chỉ, v.v. Như vậy, địa chỉ 193.32.216.9 dưới dạng ký hiệu nhị phân là

11000001 00100000 11011000 00001001

Mỗi giao diện trên mọi máy chủ và bộ định tuyến trong Internet toàn cầu phải có một địa chỉ IP duy nhất trên toàn cầu (ngoại trừ các giao diện đằng sau NAT, như đã thảo luận trong Phần 4.3.3). Tuy nhiên, những địa chỉ này không thể được chọn theo cách dù muốn hay không. Một phần địa chỉ IP của giao diện sẽ được xác định bởi mạng con mà nó được kết nối.

Hình 4.18 cung cấp một ví dụ về giao diện và địa chỉ IP. Trong hình này, một bộ định tuyến (có ba giao diện) được sử dụng để kết nối bảy máy chủ. Hãy xem xét kỹ các địa chỉ IP được gán cho giao diện máy chủ và bộ định tuyến vì có một số điều cần lưu ý. Ba máy chủ ở phần trên bên trái của Hình 4.18 và giao diện bộ định tuyến mà chúng được kết nối, tất cả đều có địa chỉ IP có dạng 223.1.1.xxx. Nghĩa là, tất cả chúng đều có 24 bit ngoài cùng bên trái trong địa chỉ IP. Bốn giao diện này cũng được kết nối với nhau bằng một mạng không chứa bộ định tuyến. Mạng này có thể được kết nối với nhau bằng Ethernet LAN, trong trường hợp đó các giao diện sẽ được kết nối bằng bộ chuyển mạch Ethernet (như chúng ta sẽ thảo luận trong Chương 6) hoặc bằng điểm truy cập không dây (như chúng ta sẽ thảo luận trong Chương 7). Hiện tại, chúng tôi sẽ trình bày mạng không có bộ định tuyến này kết nối các máy chủ này dưới dạng đám mây và đi sâu vào phần bên trong của các mạng đó trong Chương 6 và 7.

Theo thuật ngữ IP, mạng này kết nối ba giao diện máy chủ và một giao diện bộ định tuyến tạo thành một mạng con \[RFC 950\]. (Mạng con còn được gọi là mạng IP hoặc đơn giản là

một mạng trong tài liệu Internet.) Địa chỉ IP gán một địa chỉ cho mạng con này: 223.1.1.0/24, trong đó ký hiệu /24 ("dấu gạch chéo-24"), đôi khi được gọi là mặt nạ mạng con, cho biết rằng 24 bit ngoài cùng bên trái của số lượng 32 bit xác định địa chỉ mạng con. Do đó, mạng con 223.1.1.0/24 bao gồm ba giao diện máy chủ (223.1.1.1, 223.1.1.2 và 223.1.1.3) và một giao diện bộ định tuyến (223.1.1.4). Bất kỳ máy chủ bổ sung nào được gắn vào mạng con 223.1.1.0/24 sẽ phải có địa chỉ có dạng 223.1.1.xxx. Có hai mạng con bổ sung được hiển thị trong Hình 4.18: mạng 223.1.2.0/24 và mạng con 223.1.3.0/24. Hình 4.19 minh họa ba mạng con IP có trong Hình 4.18.

Định nghĩa IP của mạng con không bị giới hạn ở các phân đoạn Ethernet kết nối nhiều máy chủ với giao diện bộ định tuyến. Để hiểu rõ hơn ở đây, hãy xem Hình 4.20, minh họa ba bộ định tuyến được kết nối với nhau bằng liên kết điểm-điểm. Mỗi bộ định tuyến có ba giao diện, một giao diện cho mỗi liên kết điểm-điểm và một giao diện cho liên kết quảng bá kết nối trực tiếp bộ định tuyến với một cặp máy chủ. Những mạng con nào có mặt ở đây? Ba mạng con, 223.1.1.0/24, 223.1.2.0/24 và 223.1.3.0/24, tương tự như các mạng con mà chúng ta gặp trong Hình 4.18. Nhưng lưu ý rằng có ba mạng con bổ sung trong ví dụ này: một mạng con, 223.1.9.0/24, dành cho các giao diện kết nối bộ định tuyến R1 và R2; một mạng con khác, 223.1.8.0/24, dành cho các giao diện kết nối bộ định tuyến R2 và R3; và mạng con thứ ba, 223.1.7.0/24, dành cho các giao diện kết nối bộ định tuyến R3 và R1. Đối với hệ thống kết nối chung gồm các bộ định tuyến và máy chủ, chúng ta có thể sử dụng công thức sau để xác định các mạng con trong hệ thống:

223.1.1.1

223.1.2.1

223.1.2.2

223.1.1.2

223.1.1.4 223.1.2.9

223.1.3.27

223.1.1.3

223.1.3.1 223.1.3.2

*Hình 4.18 ♦ Địa chỉ giao diện và mạng con*

Để xác định các mạng con, hãy tách từng giao diện khỏi máy chủ hoặc bộ định tuyến của nó, tạo ra các nhóm mạng bị cô lập, với các giao diện kết thúc điểm cuối của các mạng bị cô lập. Mỗi mạng bị cô lập này được gọi là mạng con.

Nếu áp dụng quy trình này cho hệ thống được kết nối trong Hình 4.20, chúng ta sẽ có sáu đảo hoặc mạng con.

Từ cuộc thảo luận ở trên, rõ ràng là một tổ chức (chẳng hạn như một công ty hoặc tổ chức học thuật) có nhiều phân đoạn Ethernet và liên kết điểm-điểm sẽ có nhiều mạng con, với tất cả các thiết bị trên một mạng con nhất định có cùng địa chỉ mạng con. Về nguyên tắc, các mạng con khác nhau có thể có địa chỉ mạng con khác nhau. Tuy nhiên, trong thực tế, địa chỉ mạng con của chúng thường có nhiều điểm chung. Để hiểu lý do tại sao, tiếp theo chúng ta hãy chú ý đến cách xử lý địa chỉ trên Internet toàn cầu.

Chiến lược gán địa chỉ của Internet được gọi là Định tuyến liên miền không phân loại (CIDR---được phát âm là rượu táo) \[RFC 4632\]. CIDR khái quát hóa khái niệm địa chỉ mạng con. Giống như địa chỉ mạng con, địa chỉ IP 32 bit được chia thành hai phần và lại có dạng thập phân chấm chấm a.b.c.d/x, trong đó x biểu thị số bit trong phần đầu tiên của địa chỉ.

X bit quan trọng nhất của địa chỉ có dạng a.b.c.d/x cấu thành phần mạng của địa chỉ IP và thường được gọi là tiền tố (hoặc tiền tố mạng) của địa chỉ. Một tổ chức thường được chỉ định một khối địa chỉ liền kề, tức là một dải địa chỉ có tiền tố chung (xem tính năng Nguyên tắc trong thực hành). Trong trường hợp này, địa chỉ IP của các thiết bị trong tổ chức sẽ chia sẻ tiền tố chung. Khi chúng tôi đề cập đến giao thức định tuyến BGP của Internet trong

223.1.1.0/24

223.1.2.0/24

223.1.3.0/24

*Hình 4.19 ♦ Subnet địa chỉ*

Phần 5.4, chúng ta sẽ thấy rằng chỉ các bit tiền tố x hàng đầu này mới được các bộ định tuyến bên ngoài mạng của tổ chức xem xét. Nghĩa là, khi một bộ định tuyến bên ngoài tổ chức chuyển tiếp một datagram có địa chỉ đích nằm trong tổ chức thì chỉ cần xem xét các bit x hàng đầu của địa chỉ đó. Điều này làm giảm đáng kể kích thước của bảng chuyển tiếp trong các bộ định tuyến này, vì một mục nhập duy nhất có dạng a.b.c.d/x sẽ đủ để chuyển tiếp các gói đến bất kỳ đích nào trong tổ chức.

32-x bit còn lại của một địa chỉ có thể được coi là để phân biệt giữa các thiết bị trong tổ chức, tất cả đều có cùng tiền tố mạng. Đây là những bit sẽ được xem xét khi chuyển tiếp gói tin tại các bộ định tuyến trong tổ chức. Các bit bậc thấp hơn này có thể (hoặc có thể không) có cấu trúc mạng con bổ sung, chẳng hạn như cấu trúc đã thảo luận ở trên. Ví dụ: giả sử 21 bit đầu tiên của địa chỉ CIDRized a.b.c.d/21 chỉ định tiền tố mạng của tổ chức và chung cho địa chỉ IP của tất cả các thiết bị trong tổ chức đó. 11 bit còn lại xác định các máy chủ cụ thể trong tổ chức. Cấu trúc bên trong của tổ chức có thể sao cho 11 bit ngoài cùng bên phải này được sử dụng để chia mạng con trong tổ chức, như đã thảo luận ở trên. Ví dụ: a.b.c.d/24 có thể đề cập đến một mạng con cụ thể trong tổ chức.

Trước khi CIDR được thông qua, các phần mạng của địa chỉ IP bị giới hạn ở độ dài 8, 16 hoặc 24 bit, một sơ đồ địa chỉ được gọi là địa chỉ phân lớp,

223.1.8.1 223.1.8.0

223.1.9.1 223.1.7.1

223.1.2.6

223.1.2.1 223.1.2.2 223.1.3.1 223.1.3.2

223.1.1.3

223.1.7.0 223.1.9.2

223.1.3.27

223.1.1.1 223.1.1.4

R1

R2

R3

*Hình 4.20 ♦ Ba bộ định tuyến kết nối sáu mạng con*

vì các mạng con có địa chỉ mạng con 8, 16 và 24 bit lần lượt được gọi là mạng lớp A, B và C. Yêu cầu phần mạng con của địa chỉ IP phải dài chính xác 1, 2 hoặc 3 byte hóa ra lại gây khó khăn cho việc hỗ trợ số lượng ngày càng tăng nhanh chóng của các tổ chức có mạng con vừa và nhỏ. Mạng con lớp C (/24) chỉ có thể chứa tối đa 28 2 2 5 254 máy chủ (hai trong số 28 5 256 địa chỉ được dành riêng cho mục đích sử dụng đặc biệt)---quá nhỏ đối với nhiều tổ chức. Tuy nhiên, mạng con loại B (/16), hỗ trợ tới 65.634 máy chủ, là quá lớn. Theo địa chỉ lớp, một tổ chức có 2.000 máy chủ thường được phân bổ một địa chỉ mạng con lớp B (/16). Điều này dẫn đến sự cạn kiệt nhanh chóng của không gian địa chỉ lớp B và khả năng sử dụng kém không gian địa chỉ được chỉ định. Ví dụ: tổ chức sử dụng địa chỉ lớp B cho 2.000 máy chủ của mình đã được phân bổ đủ không gian địa chỉ cho tối đa 65.534 giao diện---để lại hơn 63.000 địa chỉ mà các tổ chức khác không thể sử dụng.

Ví dụ này về một ISP kết nối tám tổ chức với Internet minh họa rõ ràng cách các địa chỉ CIDRized được phân bổ cẩn thận tạo điều kiện thuận lợi cho việc định tuyến. Giả sử, như trong Hình 4.21, ISP (mà chúng ta gọi là Fly-By-Night-ISP) quảng cáo với thế giới bên ngoài rằng nó sẽ được gửi bất kỳ gói dữ liệu nào có 20 bit địa chỉ đầu tiên khớp với 200.23.16.0/20. Phần còn lại của thế giới không cần biết rằng trong khối địa chỉ 200.23.16.0/20 trên thực tế có tám tổ chức khác, mỗi tổ chức có mạng con riêng. Khả năng sử dụng một tiền tố duy nhất để quảng cáo nhiều mạng thường được gọi là tổng hợp địa chỉ (cũng là tổng hợp tuyến đường hoặc tóm tắt tuyến đường).

Việc tổng hợp địa chỉ hoạt động cực kỳ hiệu quả khi địa chỉ được phân bổ theo khối cho các ISP và sau đó từ ISP đến các tổ chức khách hàng. Nhưng điều gì sẽ xảy ra khi địa chỉ không được phân bổ theo cách phân cấp như vậy? Ví dụ: điều gì sẽ xảy ra nếu Fly-By-Night-ISP mua lại ISP-R-Us và sau đó Tổ chức 1 kết nối với Internet thông qua công ty con ISP-R-Us? Như được hiển thị trong Hình 4.21, công ty con ISPs-R-Us sở hữu khối địa chỉ 199.31.0.0/16, nhưng rất tiếc, địa chỉ IP của Tổ chức 1 lại nằm ngoài khối địa chỉ này. Nên làm gì đây? Chắc chắn, Tổ chức 1 có thể đánh số lại tất cả các bộ định tuyến và máy chủ của mình để có địa chỉ trong khối địa chỉ ISPs-R-Us. Nhưng đây là một giải pháp tốn kém và Tổ chức 1 có thể sẽ được giao lại cho một công ty con khác trong tương lai. Giải pháp thường được áp dụng là Tổ chức 1 giữ địa chỉ IP của mình ở 200.23.18.0/23. Trong trường hợp này, như trong Hình 4.22, Fly-By-Night-ISP tiếp tục quảng cáo khối địa chỉ 200.23.16.0/20 và ISP-R-Us tiếp tục quảng cáo khối địa chỉ 199.31.0.0/16. Tuy nhiên, ISPs-R-Us hiện cũng quảng cáo khối địa chỉ cho Tổ chức 1, 200.23.18.0/23. Khi các bộ định tuyến khác trên Internet lớn hơn nhìn thấy khối địa chỉ 200.23.16.0/20 (từ Fly-By-Night-ISP) và 200.23.18.0/23 (từ ISPsR-Us) và muốn định tuyến đến một địa chỉ trong khối 200.23.18.0/23, chúng sẽ sử dụng kết hợp tiền tố dài nhất (xem Phần 4.2.1) và định tuyến tới ISP-R-Us, vì nó quảng cáo tiền tố địa chỉ dài nhất (tức là cụ thể nhất) khớp với địa chỉ đích.

NGUYÊN TẮC TRONG THỰC HÀNH

Tổ chức 0

200.23.16.0/23

Tổ chức 1

Bay-By-Night-ISP

"Gửi cho tôi bất cứ thứ gì có địa chỉ bắt đầu từ 200.23.16.0/20"

ISP-R-Us

200.23.18.0/23

Tổ chức 2

200.23.20.0/23

Tổ chức 7

200.23.30.0/23

internet

"Gửi cho tôi bất cứ thứ gì có địa chỉ bắt đầu từ 199.31.0.0/16"

*Hình 4.21 ♦ Đánh địa chỉ phân cấp và tập hợp tuyến đường*

Tổ chức 0

200.23.16.0/23

Tổ chức 2

Bay-By-Night-ISP

"Gửi cho tôi bất cứ thứ gì có địa chỉ bắt đầu từ 200.23.16.0/20"

ISP-R-Us

200.23.20.0/23

Tổ chức 7

200.23.30.0/23

Tổ chức 1

200.23.18.0/23

internet

"Gửi cho tôi bất cứ thứ gì có địa chỉ bắt đầu 199.31.0.0/16 hoặc 200.23.18.0/23"

*Hình 4.22 ♦ ISPs-R-Us có lộ trình cụ thể hơn đến Tổ chức 1*

Sẽ thật thiếu sót nếu không đề cập đến một loại địa chỉ IP khác, địa chỉ quảng bá IP 255.255.255.255. Khi một máy chủ gửi một datagram có địa chỉ đích 255.255.255.255, tin nhắn sẽ được gửi đến tất cả các máy chủ trên cùng một mạng con. Routers cũng có thể tùy chọn chuyển tiếp tin nhắn sang các mạng con lân cận (mặc dù chúng thường không làm như vậy).

Bây giờ đã nghiên cứu chi tiết về địa chỉ IP, chúng ta cần biết máy chủ và mạng con lấy địa chỉ của chúng như thế nào ngay từ đầu. Hãy bắt đầu bằng cách xem cách một tổ chức lấy một khối địa chỉ cho các thiết bị của mình và sau đó xem cách một thiết bị (chẳng hạn như máy chủ) được chỉ định một địa chỉ từ trong khối địa chỉ của tổ chức.

Lấy một khối địa chỉ

Để có được khối địa chỉ IP để sử dụng trong mạng con của tổ chức, trước tiên quản trị viên mạng có thể liên hệ với ISP của tổ chức đó, họ sẽ cung cấp địa chỉ từ khối địa chỉ lớn hơn đã được phân bổ cho ISP. Ví dụ: bản thân ISP có thể đã được phân bổ khối địa chỉ 200.23.16.0/20. Ngược lại, ISP có thể chia khối địa chỉ của mình thành tám khối địa chỉ liền kề có kích thước bằng nhau và cung cấp một trong các khối địa chỉ này cho mỗi tổ chức trong số tối đa tám tổ chức được ISP này hỗ trợ, như được hiển thị bên dưới. (Chúng tôi đã gạch chân phần mạng con của các địa chỉ này để bạn thuận tiện.)

Khối ISP: 200.23.16.0/20 11001000 00010111 00010000 00000000

Tổ chức 0 200.23.16.0/23 11001000 00010111 00010000 00000000

Tổ chức 1 200.23.18.0/23 11001000 00010111 00010010 00000000

Tổ chức 2 200.23.20.0/23 11001000 00010111 00010100 00000000

...   ...                       ...

Tổ chức 7 200.23.30.0/23 11001000 00010111 00011110 00000000

Mặc dù lấy một bộ địa chỉ từ ISP là một cách để có được một khối địa chỉ nhưng đó không phải là cách duy nhất. Rõ ràng, chính ISP cũng phải có cách nào đó để có được một khối địa chỉ. Có cơ quan toàn cầu nào chịu trách nhiệm cuối cùng trong việc quản lý không gian địa chỉ IP và phân bổ khối địa chỉ cho ISP và các tổ chức khác không? Quả thực là có! Địa chỉ IP được quản lý dưới sự quản lý của Tập đoàn Internet cấp số và tên miền (ICANN) \[ICANN 2020\], dựa trên các nguyên tắc được nêu trong \[RFC 7020\]. Vai trò của tổ chức ICANN phi lợi nhuận không chỉ là phân bổ địa chỉ IP mà còn quản lý các máy chủ gốc DNS. Nó còn có nhiệm vụ gây nhiều tranh cãi là gán tên miền và giải quyết tranh chấp tên miền. ICANN phân bổ địa chỉ cho các cơ quan đăng ký Internet khu vực (ví dụ: ARIN, RIPE, APNIC và LACNIC, cùng nhau tạo thành Địa chỉ

Tổ chức hỗ trợ ICANN \[ASO-ICANN 2020\]) và xử lý việc phân bổ/quản lý địa chỉ trong khu vực của họ.

Lấy địa chỉ Host: Giao thức cấu hình động Host

Khi một tổ chức đã có được một khối địa chỉ, tổ chức đó có thể gán các địa chỉ IP riêng lẻ cho các giao diện máy chủ và bộ định tuyến trong tổ chức của mình. Quản trị viên hệ thống thường sẽ định cấu hình thủ công các địa chỉ IP trong bộ định tuyến (thường là từ xa, bằng công cụ quản lý mạng). Địa chỉ Host cũng có thể được định cấu hình theo cách thủ công, nhưng thông thường việc này được thực hiện bằng Giao thức cấu hình động Host (DHCP) \[RFC 2131\]. DHCP cho phép máy chủ tự động lấy (được cấp phát) địa chỉ IP. Quản trị viên mạng có thể định cấu hình DHCP để một máy chủ nhất định nhận được cùng một địa chỉ IP mỗi lần kết nối với mạng hoặc một máy chủ có thể được chỉ định một địa chỉ IP tạm thời sẽ khác nhau mỗi lần máy chủ kết nối với mạng. Ngoài việc gán địa chỉ máy chủ IP, DHCP còn cho phép máy chủ tìm hiểu thông tin bổ sung, chẳng hạn như mặt nạ mạng con, địa chỉ của bộ định tuyến bước nhảy đầu tiên (thường được gọi là cổng mặc định) và địa chỉ của máy chủ DNS cục bộ của nó.

Do khả năng tự động hóa các khía cạnh liên quan đến mạng của DHCP trong việc kết nối máy chủ vào mạng nên nó thường được gọi là giao thức plug-and-play hoặc zeroconf (không cấu hình). Khả năng này khiến nó trở nên rất hấp dẫn đối với quản trị viên mạng, những người lẽ ra phải thực hiện các tác vụ này một cách thủ công! DHCP cũng được sử dụng rộng rãi trong các mạng truy cập Internet dân dụng, mạng doanh nghiệp và trong mạng LAN không dây, nơi các máy chủ tham gia và rời khỏi mạng thường xuyên. Ví dụ, hãy xem xét trường hợp một sinh viên mang máy tính xách tay từ phòng ký túc xá đến thư viện rồi đến lớp học. Có khả năng là ở mỗi địa điểm, học sinh sẽ kết nối vào một mạng con mới và do đó sẽ cần một địa chỉ IP mới tại mỗi địa điểm. DHCP là lý tưởng cho tình huống này, vì có nhiều người dùng đến và đi và chỉ cần địa chỉ trong một khoảng thời gian giới hạn. Giá trị của khả năng plug-and-play của DHCP rất rõ ràng, vì không thể tưởng tượng được rằng quản trị viên hệ thống có thể cấu hình lại máy tính xách tay tại mỗi vị trí và rất ít sinh viên (ngoại trừ những người tham gia lớp học mạng máy tính!) có chuyên môn để định cấu hình máy tính xách tay của họ theo cách thủ công.

DHCP là giao thức máy khách-máy chủ. Máy khách thường là máy chủ mới đến muốn lấy thông tin cấu hình mạng, bao gồm địa chỉ IP cho chính nó. Trong trường hợp đơn giản nhất, mỗi mạng con (theo nghĩa địa chỉ của Hình 4.20) sẽ có một máy chủ DHCP. Nếu không có máy chủ nào trên mạng con thì cần có tác nhân chuyển tiếp DHCP (thường là bộ định tuyến) biết địa chỉ của máy chủ DHCP cho mạng đó. Hình 4.23 cho thấy máy chủ DHCP được gắn vào mạng con 223.1.2/24, với bộ định tuyến đóng vai trò là tác nhân chuyển tiếp cho các máy khách đến được gắn vào mạng con 223.1.1/24 và 223.1.3/24. Trong cuộc thảo luận bên dưới, chúng tôi giả định rằng máy chủ DHCP có sẵn trên mạng con.

Đối với máy chủ mới đến, giao thức DHCP là một quy trình gồm bốn bước, như trong Hình 4.24 đối với cài đặt mạng được hiển thị trong Hình 4.23. Trong hình này, yiadr (như trong "địa chỉ Internet của bạn") cho biết địa chỉ được phân bổ cho khách hàng mới đến. Bốn bước là:

• DHCP khám phá máy chủ. Nhiệm vụ đầu tiên của máy chủ mới đến là tìm máy chủ DHCP để tương tác. Việc này được thực hiện bằng cách sử dụng thông báo khám phá DHCP mà khách hàng sẽ gửi trong gói UDP tới cổng 67. Gói UDP được gói gọn trong gói dữ liệu IP. Nhưng datagram này nên được gửi cho ai? Máy chủ thậm chí không biết địa chỉ IP của mạng mà nó đang kết nối, càng không biết địa chỉ của máy chủ DHCP cho mạng này. Vì điều này, ứng dụng khách DHCP tạo một gói dữ liệu IP chứa thông báo khám phá DHCP của nó cùng với địa chỉ đích phát sóng IP là 255.255.255.255 và địa chỉ nguồn \"máy chủ này\" IP là 0.0.0.0. Máy khách DHCP chuyển gói dữ liệu IP tới lớp liên kết, sau đó lớp này sẽ phát khung này tới tất cả các nút được gắn vào mạng con (chúng tôi sẽ đề cập chi tiết về việc phát sóng lớp liên kết trong Phần 6.4). • DHCP ưu đãi máy chủ. Máy chủ DHCP nhận được thông báo khám phá DHCP sẽ phản hồi lại máy khách bằng thông báo ưu đãi DHCP được phát cho tất cả mọi người

223.1.1.1

223.1.1.2

223.1.1.4 223.1.2.9

223.1.3.27

223.1.1.3

223.1.3.1 223.1.3.2

223.1.2.1

223.1.2.5

223.1.2.2

Đang đến

DHCP khách hàng

DHCP máy chủ

*Hình 4.23 ♦ DHCP máy khách và máy chủ*

DHCP máy chủ:

223.1.2.5 Khách hàng đang đến

DHCP khám phá

Thời gian Thời gian

src: 0.0.0.0, 68 đích: 255.255.255.255,67 DHCPDISCOVER yaddr: 0.0.0.0 ID giao dịch: 654

src: 223.1.2.5, 67 đích: 255.255.255.255,68 DHCPOFFER yaddrr: 223.1.2.4 ID giao dịch: 654 DHCP ID máy chủ: 223.1.2.5 Thời gian tồn tại: 3600 giây

DHCP ưu đãi

src: 223.1.2.5, 67 đích: 255.255.255.255,68 DHCPACK yaddrr: 223.1.2.4 ID giao dịch: 655 DHCP ID máy chủ: 223.1.2.5 Thời gian tồn tại: 3600 giây

DHCP ACK

src: 0.0.0.0, 68 đích: 255.255.255.255, 67 DHCPREQUEST yaddrr: 223.1.2.4 ID giao dịch: 655 DHCP ID máy chủ: 223.1.2.5 Thời gian tồn tại: 3600 giây

DHCP yêu cầu

*Hình 4.24 ♦ DHCP tương tác giữa máy khách và máy chủ*

các nút trên mạng con, lại sử dụng địa chỉ quảng bá IP là 255.255.255.255. (Bạn có thể muốn nghĩ xem tại sao phản hồi của máy chủ này cũng phải được phát sóng). Vì một số máy chủ DHCP có thể có mặt trên mạng con, nên khách hàng có thể thấy mình ở vị trí tuyệt vời khi có thể chọn trong số một số ưu đãi. Mỗi thông báo ưu đãi máy chủ chứa ID giao dịch của thông báo khám phá đã nhận, địa chỉ IP được đề xuất cho máy khách, mặt nạ mạng và thời gian thuê địa chỉ IP---khoảng thời gian mà địa chỉ IP sẽ hợp lệ. Thông thường máy chủ đặt thời gian thuê thành vài giờ hoặc vài ngày \[Droms 2002\].

• DHCP yêu cầu. Máy khách mới đến sẽ chọn trong số một hoặc nhiều ưu đãi của máy chủ và phản hồi ưu đãi đã chọn của nó bằng thông báo yêu cầu DHCP, phản hồi lại các tham số cấu hình. • DHCP ACK. Máy chủ phản hồi thông báo yêu cầu DHCP bằng thông báo DHCP ACK, xác nhận các tham số được yêu cầu.

Sau khi khách hàng nhận được DHCP ACK, quá trình tương tác sẽ hoàn tất và khách hàng có thể sử dụng địa chỉ DHCP được phân bổ IP trong thời gian thuê. Vì khách hàng có thể muốn sử dụng địa chỉ của mình sau khi hợp đồng thuê hết hạn, DHCP cũng cung cấp cơ chế cho phép khách hàng gia hạn hợp đồng thuê trên địa chỉ IP.

Từ khía cạnh di động, DHCP có một thiếu sót rất đáng kể. Vì địa chỉ IP mới được lấy từ DHCP mỗi khi một nút kết nối với mạng con mới, nên không thể duy trì kết nối TCP với ứng dụng từ xa khi nút di động di chuyển giữa các mạng con. Trong Chương 7, chúng ta sẽ tìm hiểu cách mạng di động di động cho phép máy chủ lưu giữ địa chỉ IP và các kết nối TCP đang diễn ra khi nó di chuyển giữa các trạm cơ sở trong mạng di động của nhà cung cấp. Bạn có thể tìm thêm thông tin chi tiết về DHCP trong \[Droms 2002\] và \[dhc 2020\]. Việc triển khai tham chiếu mã nguồn mở của DHCP hiện có tại Internet Systems Consortium \[ISC 2020\].

**4.3.3 Dịch địa chỉ mạng (NAT)**

Dựa trên cuộc thảo luận của chúng ta về địa chỉ Internet và định dạng gói dữ liệu IPv4, giờ đây chúng ta đã biết rõ rằng mọi thiết bị có khả năng IP đều cần có địa chỉ IP. Với sự phát triển nhanh chóng của các mạng con văn phòng nhỏ, văn phòng tại nhà (SOHO), điều này dường như ngụ ý rằng bất cứ khi nào SOHO muốn cài đặt mạng LAN để kết nối nhiều máy, ISP sẽ cần phải phân bổ một loạt địa chỉ để bao phủ tất cả các thiết bị IP của SOHO (bao gồm điện thoại, máy tính bảng, thiết bị chơi game, IP TV, máy in, v.v.). Nếu mạng con ngày càng lớn hơn thì khối địa chỉ lớn hơn sẽ phải được phân bổ. Nhưng điều gì sẽ xảy ra nếu ISP đã phân bổ các phần liền kề trong dải địa chỉ hiện tại của mạng SOHO? Và điều mà chủ nhà điển hình muốn (hoặc nên cần) biết cách quản lý địa chỉ IP ngay từ đầu là gì? May mắn thay, có một cách tiếp cận đơn giản hơn để phân bổ địa chỉ đã được sử dụng ngày càng rộng rãi trong các tình huống như vậy: dịch địa chỉ mạng (NAT) \[RFC 2663; RFC 3022; Huston 2004, Trương 2007; Huston 2017\].

Hình 4.25 minh họa hoạt động của bộ định tuyến hỗ trợ NAT. Bộ định tuyến hỗ trợ NAT, nằm trong nhà, có giao diện là một phần của mạng gia đình ở bên phải Hình 4.25. Việc đánh địa chỉ trong mạng gia đình chính xác như chúng ta đã thấy ở trên---cả bốn giao diện trong mạng gia đình đều có cùng địa chỉ mạng con là 10.0.0.0/24. Không gian địa chỉ 10.0.0.0/8 là một trong ba phần của không gian địa chỉ IP được dành riêng trong \[RFC 1918\] cho mạng riêng hoặc một khu vực có địa chỉ riêng, chẳng hạn như mạng gia đình trong Hình 4.25. Một lĩnh vực có địa chỉ riêng đề cập đến một mạng có địa chỉ chỉ có ý nghĩa đối với

các thiết bị trong mạng đó. Để biết tại sao điều này lại quan trọng, hãy xem xét thực tế là có hàng trăm nghìn mạng gia đình, nhiều mạng sử dụng cùng một không gian địa chỉ, 10.0.0.0/24. Các thiết bị trong mạng gia đình nhất định có thể gửi gói cho nhau bằng cách sử dụng địa chỉ 10.0.0.0/24. Tuy nhiên, các gói được chuyển tiếp ra ngoài mạng gia đình vào mạng Internet toàn cầu lớn hơn rõ ràng không thể sử dụng các địa chỉ này (làm địa chỉ nguồn hoặc địa chỉ đích) vì có hàng trăm nghìn mạng đang sử dụng khối địa chỉ này. Nghĩa là, địa chỉ 10.0.0.0/24 chỉ có thể có ý nghĩa trong mạng gia đình nhất định. Nhưng nếu địa chỉ riêng chỉ có ý nghĩa trong một mạng nhất định, thì địa chỉ được xử lý như thế nào khi các gói được gửi đến hoặc nhận từ Internet toàn cầu, trong đó địa chỉ nhất thiết phải là duy nhất? Câu trả lời nằm ở sự hiểu biết NAT.

Bộ định tuyến hỗ trợ NAT không giống bộ định tuyến đối với thế giới bên ngoài. Thay vào đó, bộ định tuyến NAT hoạt động với thế giới bên ngoài như một thiết bị duy nhất có một địa chỉ IP duy nhất. Trong Hình 4.25, tất cả lưu lượng truy cập rời khỏi bộ định tuyến gia đình để truy cập Internet lớn hơn có địa chỉ nguồn IP là 138.76.29.7 và tất cả lưu lượng truy cập vào bộ định tuyến gia đình phải có địa chỉ đích là 138.76.29.7. Về bản chất, bộ định tuyến hỗ trợ NAT đang ẩn các chi tiết của mạng gia đình với thế giới bên ngoài. (Bên cạnh đó, bạn có thể thắc mắc các máy tính trong mạng gia đình lấy địa chỉ của chúng ở đâu và bộ định tuyến lấy địa chỉ IP duy nhất ở đâu. Thông thường, câu trả lời là giống nhau---DHCP! Bộ định tuyến lấy địa chỉ từ máy chủ DHCP của ISP và bộ định tuyến chạy máy chủ DHCP để cung cấp địa chỉ cho các máy tính trong mạng NAT-DHCP-không gian địa chỉ của mạng gia đình do bộ định tuyến kiểm soát.)

10.0.0.1

138.76.29.7

10.0.0.4 10.0.0.2

10.0.0.3

NAT bảng dịch

phía WAN

138.76.29.7, 5001

phía mạng LAN

10.0.0.1, 3345

. . . . . .

S = 138,76,29,7, 5001 D = 128,119,40,186, 80

S = 128.119.40.186, 80 D = 138.76.29.7, 5001

S = 128.119.40.186, 80 D = 10.0.0.1, 3345

S = 10.0.0.1, 3345 D = 128.119.40.186, 80

*Hình 4.25 ♦ Dịch địa chỉ mạng*

Nếu tất cả các gói dữ liệu đến bộ định tuyến NAT từ WAN có cùng địa chỉ đích IP (cụ thể là giao diện phía WAN của bộ định tuyến NAT), thì làm cách nào bộ định tuyến biết máy chủ nội bộ mà nó sẽ chuyển tiếp một gói dữ liệu nhất định đến? Bí quyết là sử dụng bảng dịch NAT tại bộ định tuyến NAT và đưa số cổng cũng như địa chỉ IP vào các mục trong bảng.

Hãy xem xét ví dụ trong Hình 4.25. Giả sử người dùng ngồi trong mạng gia đình phía sau máy chủ 10.0.0.1 yêu cầu một trang Web trên một số máy chủ Web (cổng 80) có địa chỉ IP 128.119.40.186. Máy chủ 10.0.0.1 gán số cổng nguồn (tùy ý) 3345 và gửi datagram vào mạng LAN. Bộ định tuyến NAT nhận datagram, tạo số cổng nguồn mới 5001 cho datagram, thay thế địa chỉ IP nguồn bằng địa chỉ IP phía WAN của nó 138.76.29.7 và thay thế số cổng nguồn ban đầu 3345 bằng số cổng nguồn mới 5001. Khi tạo số cổng nguồn mới, Bộ định tuyến NAT có thể chọn bất kỳ số cổng nguồn nào hiện không có trong bảng dịch NAT. (Lưu ý rằng vì trường số cổng dài 16 bit nên giao thức NAT có thể hỗ trợ hơn 60.000 kết nối đồng thời với một địa chỉ IP phía WAN duy nhất cho bộ định tuyến!) NAT trong bộ định tuyến cũng thêm một mục nhập vào bảng dịch NAT của nó. Máy chủ Web hoàn toàn không biết rằng datagram đến chứa yêu cầu HTTP đã bị bộ định tuyến NAT thao túng, sẽ phản hồi bằng một datagram có địa chỉ đích là địa chỉ IP của bộ định tuyến NAT và có số cổng đích là 5001. Khi gói dữ liệu này đến bộ định tuyến NAT, bộ định tuyến sẽ lập chỉ mục Bảng dịch NAT sử dụng địa chỉ IP đích và số cổng đích để lấy địa chỉ IP thích hợp (10.0.0.1) và số cổng đích (3345) cho trình duyệt trong mạng gia đình. Sau đó, bộ định tuyến sẽ ghi lại địa chỉ đích và số cổng đích của datagram và chuyển tiếp datagram vào mạng gia đình.

NAT đã được triển khai rộng rãi trong những năm gần đây. Nhưng NAT không phải là không có những lời gièm pha. Đầu tiên, người ta có thể lập luận rằng số cổng được sử dụng để đánh địa chỉ các tiến trình chứ không phải để đánh địa chỉ các máy chủ. Sự vi phạm này thực sự có thể gây ra sự cố cho các máy chủ chạy trên mạng gia đình, vì như chúng ta đã thấy trong Chương 2, các quy trình máy chủ chờ các yêu cầu đến ở các số cổng phổ biến và các máy ngang hàng trong giao thức P2P cần chấp nhận các kết nối đến khi hoạt động với tư cách là máy chủ. Làm cách nào một thiết bị ngang hàng có thể kết nối với một thiết bị ngang hàng khác đứng sau máy chủ NAT và có địa chỉ NAT do DHCP cung cấp? Giải pháp kỹ thuật cho những vấn đề này bao gồm NAT công cụ truyền tải \[RFC 5389\] \[RFC 5389, RFC 5128, Ford 2005\]. Nhiều lập luận "triết học" hơn cũng đã được đưa ra để chống lại NAT bởi những người theo chủ nghĩa kiến ​​trúc thuần túy. Ở đây, mối lo ngại là các bộ định tuyến được coi là thiết bị lớp 3 (tức là lớp mạng) và chỉ nên xử lý các gói cho đến lớp mạng. NAT vi phạm nguyên tắc này rằng các máy chủ phải trao đổi trực tiếp với nhau mà không can thiệp vào các nút sửa đổi địa chỉ IP, ít hơn nhiều số cổng. Chúng ta sẽ quay lại cuộc tranh luận này sau trong Phần 4.5, khi chúng ta đề cập đến các hộp trung gian.

**4.3.4 IPv6**

Vào đầu những năm 1990, Lực lượng Đặc nhiệm Kỹ thuật Internet đã bắt đầu nỗ lực phát triển giao thức kế thừa cho giao thức IPv4. Động lực chính cho nỗ lực này là nhận ra rằng không gian địa chỉ IPv4 32-bit đang bắt đầu được sử dụng hết với các mạng con mới

KIỂM TRA DỮ LIỆU: TƯỜNG CHÁY VÀ HỆ THỐNG PHÁT HIỆN XÂM NHẬP

Giả sử bạn được giao nhiệm vụ quản lý mạng gia đình, phòng ban, trường đại học hoặc công ty. Những kẻ tấn công, biết phạm vi địa chỉ IP trong mạng của bạn, có thể dễ dàng gửi các gói dữ liệu IP tới các địa chỉ trong phạm vi của bạn. Các gói dữ liệu này có thể thực hiện tất cả những việc sai trái, bao gồm lập bản đồ mạng của bạn bằng tính năng quét ping và quét cổng, đánh sập các máy chủ dễ bị tấn công bằng các gói không đúng định dạng, quét các cổng TCP/UDP đang mở trên các máy chủ trong mạng của bạn và lây nhiễm các máy chủ bằng cách đưa phần mềm độc hại vào các gói. Với tư cách là quản trị viên mạng, bạn sẽ làm gì với tất cả những kẻ xấu ngoài kia, mỗi kẻ có khả năng gửi các gói độc hại vào mạng của bạn? Hai cơ chế bảo vệ phổ biến trước các cuộc tấn công gói độc hại là tường lửa và hệ thống phát hiện xâm nhập (IDS).

Với tư cách là quản trị viên mạng, trước tiên bạn có thể thử cài đặt tường lửa giữa mạng của mình và Internet. (Hầu hết các bộ định tuyến truy cập ngày nay đều có khả năng tường lửa.) Tường lửa kiểm tra các trường tiêu đề datagram và phân đoạn, từ chối các datagram đáng ngờ xâm nhập vào mạng nội bộ. Ví dụ: tường lửa có thể được cấu hình để chặn tất cả các gói yêu cầu tiếng vang ICMP (xem Phần 5.6), do đó ngăn chặn kẻ tấn công thực hiện quét cổng truyền thống trên phạm vi địa chỉ IP của bạn. Tường lửa cũng có thể chặn các gói dựa trên địa chỉ nguồn và đích IP cũng như số cổng. Ngoài ra, tường lửa có thể được cấu hình để theo dõi các kết nối TCP, chỉ cấp quyền truy cập vào các datagram thuộc các kết nối được phê duyệt.

Bảo vệ bổ sung có thể được cung cấp với IDS. IDS, thường nằm ở ranh giới mạng, thực hiện "kiểm tra gói sâu", kiểm tra không chỉ các trường tiêu đề mà còn cả tải trọng trong datagram (bao gồm cả dữ liệu lớp ứng dụng). IDS có cơ sở dữ liệu về chữ ký gói được biết là một phần của các cuộc tấn công. Cơ sở dữ liệu này được tự động cập nhật khi các cuộc tấn công mới được phát hiện. Khi các gói đi qua IDS, IDS sẽ cố gắng khớp các trường tiêu đề và tải trọng với chữ ký trong cơ sở dữ liệu chữ ký của nó. Nếu tìm thấy sự trùng khớp như vậy, một cảnh báo sẽ được tạo. Hệ thống ngăn chặn xâm nhập (IPS) tương tự như IDS, ngoại trừ việc nó thực sự chặn các gói ngoài việc tạo cảnh báo. Chúng ta sẽ khám phá tường lửa và IDS chi tiết hơn trong Phần 4.5 và trong Chương 8.

Tường lửa và IDS có thể bảo vệ hoàn toàn mạng của bạn khỏi mọi cuộc tấn công không? Câu trả lời rõ ràng là không, vì những kẻ tấn công liên tục tìm ra các cuộc tấn công mới mà chưa có chữ ký. Nhưng tường lửa và IDS dựa trên chữ ký truyền thống rất hữu ích trong việc bảo vệ mạng của bạn khỏi các cuộc tấn công đã biết.

TẬP TRUNG VÀO AN NINH

và các nút IP được gắn vào Internet (và được phân bổ các địa chỉ IP duy nhất) với tốc độ chóng mặt. Để đáp ứng nhu cầu về không gian địa chỉ IP lớn này, giao thức IP mới, IPv6, đã được phát triển. Các nhà thiết kế của IPv6 cũng nhân cơ hội này để điều chỉnh và tăng cường các khía cạnh khác của IPv4, dựa trên kinh nghiệm vận hành tích lũy được với IPv4.

Thời điểm mà các địa chỉ IPv4 sẽ được phân bổ hoàn toàn (và do đó không có mạng mới nào có thể kết nối với Internet) là chủ đề gây tranh cãi đáng kể. Ước tính của hai người đứng đầu nhóm làm việc về Kỳ vọng thời gian sử dụng địa chỉ của IETF là địa chỉ sẽ cạn kiệt lần lượt vào năm 2008 và 2018 \[Solensky 1996\]. Vào tháng 2 năm 2011, IANA đã phân bổ nhóm địa chỉ IPv4 chưa được chỉ định cuối cùng còn lại cho cơ quan đăng ký khu vực. Mặc dù các cơ quan đăng ký này vẫn còn sẵn các địa chỉ IPv4 trong nhóm của họ, nhưng một khi các địa chỉ này đã cạn kiệt, sẽ không còn khối địa chỉ khả dụng nào có thể được phân bổ từ nhóm trung tâm \[Huston 2011a\]. Một cuộc khảo sát gần đây về IPv4 tình trạng cạn kiệt không gian địa chỉ và các bước được thực hiện để kéo dài tuổi thọ của không gian địa chỉ là \[Richter 2015\]; phân tích gần đây về việc sử dụng địa chỉ IPv4 là \[Huston 2019\].

Mặc dù các ước tính vào giữa những năm 1990 về tình trạng cạn kiệt địa chỉ IPv4 cho thấy rằng có thể còn một khoảng thời gian đáng kể cho đến khi không gian địa chỉ IPv4 cạn kiệt, người ta nhận thấy rằng cần có thời gian đáng kể để triển khai một công nghệ mới trên quy mô rộng lớn như vậy và do đó quá trình phát triển IP phiên bản 6 (IPv6) \[RFC 2460\] đã được bắt đầu \[RFC 1752\]. (Một câu hỏi thường gặp là điều gì đã xảy ra với IPv5? Ban đầu người ta hình dung rằng giao thức ST-2 sẽ trở thành IPv5, nhưng ST-2 sau đó đã bị loại bỏ.) Một nguồn thông tin tuyệt vời về IPv6 là \[Huitema 1998\].

IPv6 Datagram Định dạng

Định dạng của datagram IPv6 được hiển thị trong Hình 4.26. Những thay đổi quan trọng nhất được giới thiệu trong IPv6 được thể hiện rõ ở định dạng datagram:

• Khả năng đánh địa chỉ mở rộng. IPv6 tăng kích thước của địa chỉ IP từ 32 lên 128 bit. Điều này đảm bảo rằng thế giới sẽ không hết địa chỉ IP. Giờ đây, mọi hạt cát trên hành tinh đều có thể được định địa chỉ IP. Ngoài các địa chỉ unicast và multicast, IPv6 đã giới thiệu một loại địa chỉ mới, được gọi là địa chỉ Anycast, cho phép một datagram được gửi đến bất kỳ một trong nhóm máy chủ nào. (Ví dụ, tính năng này có thể được sử dụng để gửi HTTP GET đến trang gần nhất trong số các trang nhân bản có chứa một tài liệu nhất định.) • Tiêu đề 40 byte được sắp xếp hợp lý. Như được thảo luận bên dưới, một số trường IPv4 đã bị loại bỏ hoặc trở thành tùy chọn. Tiêu đề có độ dài cố định 40 byte thu được cho phép bộ định tuyến xử lý nhanh hơn gói dữ liệu IP. Mã hóa tùy chọn mới cho phép xử lý tùy chọn linh hoạt hơn. • Ghi nhãn dòng chảy. IPv6 có định nghĩa khó nắm bắt về luồng. RFC 2460 tuyên bố rằng điều này cho phép "gắn nhãn các gói thuộc các luồng cụ thể mà người gửi

yêu cầu xử lý đặc biệt, chẳng hạn như chất lượng dịch vụ không mặc định hoặc dịch vụ thời gian thực." Ví dụ: việc truyền âm thanh và video có thể được coi là một luồng. Mặt khác, các ứng dụng truyền thống hơn, chẳng hạn như truyền tệp và e-mail, có thể không được coi là luồng. Có thể lưu lượng truy cập được thực hiện bởi người dùng có mức độ ưu tiên cao (ví dụ: ai đó trả tiền để có dịch vụ tốt hơn cho lưu lượng truy cập của họ) cũng có thể được coi là một luồng. Tuy nhiên, điều rõ ràng là các nhà thiết kế của IPv6 đã thấy trước nhu cầu cuối cùng là có thể phân biệt giữa các luồng, ngay cả khi ý nghĩa chính xác của luồng vẫn chưa được xác định.

Như đã lưu ý ở trên, so sánh Hình 4.26 với Hình 4.17 cho thấy cấu trúc đơn giản hơn, hợp lý hơn của gói dữ liệu IPv6. Các trường sau được xác định trong IPv6:

• Phiên bản. Trường 4 bit này xác định số phiên bản IP. Không có gì ngạc nhiên khi IPv6 mang giá trị 6 trong trường này. Lưu ý rằng việc đặt số 4 vào trường này sẽ không tạo ra datagram IPv4 hợp lệ. (Nếu đúng như vậy, cuộc sống sẽ đơn giản hơn rất nhiều---xem phần thảo luận bên dưới về quá trình chuyển đổi từ IPv4 sang IPv6.) • Lớp lưu lượng truy cập. Trường lớp lưu lượng truy cập 8 bit, như trường TOS trong IPv4, có thể được sử dụng để ưu tiên các gói dữ liệu nhất định trong một luồng hoặc có thể được sử dụng để ưu tiên các gói dữ liệu từ các ứng dụng nhất định (ví dụ: lồng tiếng-IP) so với các gói dữ liệu từ các ứng dụng khác (ví dụ: SMTP e-mail). • Nhãn dòng chảy. Như đã thảo luận ở trên, trường 20 bit này được sử dụng để xác định luồng datagram. • chiều dài Payload. Giá trị 16 bit này được coi là số nguyên không dấu cho biết số byte trong gói dữ liệu IPv6 theo sau tiêu đề gói dữ liệu 40 byte có độ dài cố định.

Phiên bản Lớp lưu lượng

Payload độ dài HDR Tiếp theo Giới hạn bước nhảy

Nhãn luồng

32 bit

Địa chỉ nguồn

(128 bit)

Địa chỉ đích

(128 bit)

dữ liệu

*Hình 4.26 ♦ IPv6 định dạng datagram*

• Tiêu đề tiếp theo. Trường này xác định giao thức mà nội dung (trường dữ liệu) của gói dữ liệu này sẽ được gửi tới (ví dụ: tới TCP hoặc UDP). Trường này sử dụng các giá trị giống như trường giao thức trong tiêu đề IPv4. • Giới hạn bước nhảy. Nội dung của trường này được giảm đi một bởi mỗi bộ định tuyến chuyển tiếp datagram. Nếu số lượng giới hạn hop đạt tới 0, bộ định tuyến phải loại bỏ datagram đó. • Địa chỉ nguồn và đích. Các định dạng khác nhau của địa chỉ IPv6 128-bit được mô tả trong RFC 4291. • Dữ liệu. Đây là phần tải trọng của datagram IPv6. Khi gói dữ liệu đến đích, tải trọng sẽ bị xóa khỏi gói dữ liệu IP và được chuyển sang giao thức được chỉ định trong trường tiêu đề tiếp theo.

Cuộc thảo luận ở trên đã xác định mục đích của các trường được bao gồm trong datagram IPv6. So sánh định dạng gói dữ liệu IPv6 trong Hình 4.26 với định dạng gói dữ liệu IPv4 mà chúng ta đã thấy trong Hình 4.17, chúng tôi nhận thấy rằng một số trường xuất hiện trong gói dữ liệu IPv4 không còn xuất hiện trong gói dữ liệu IPv6:

• Phân mảnh/tập hợp lại. IPv6 không cho phép phân mảnh và tập hợp lại ở các bộ định tuyến trung gian; những hoạt động này chỉ có thể được thực hiện bởi nguồn và đích. Nếu một datagram IPv6 mà bộ định tuyến nhận được quá lớn để có thể chuyển tiếp qua liên kết đi, bộ định tuyến chỉ cần hủy gói dữ liệu đó và gửi thông báo lỗi "Packet Quá Lớn" ICMP (xem Phần 5.6) lại cho người gửi. Sau đó, người gửi có thể gửi lại dữ liệu bằng kích thước gói dữ liệu IP nhỏ hơn. Phân mảnh và tập hợp lại là một hoạt động tốn thời gian; loại bỏ chức năng này khỏi bộ định tuyến và đặt nó ngay vào hệ thống cuối sẽ tăng tốc đáng kể IP chuyển tiếp trong mạng. • Header tổng kiểm tra. Vì các giao thức lớp vận chuyển (ví dụ: TCP và UDP) và lớp liên kết (ví dụ: Ethernet) trong các lớp Internet thực hiện kiểm tra tổng, nên các nhà thiết kế của IP có thể cảm thấy rằng chức năng này đủ dư thừa trong lớp mạng nên có thể loại bỏ nó. Một lần nữa, việc xử lý nhanh các gói IP là mối quan tâm hàng đầu. Hãy nhớ lại cuộc thảo luận của chúng ta về IPv4 trong Phần 4.3.1 rằng vì tiêu đề IPv4 chứa trường TTL (tương tự như trường giới hạn số bước nhảy trong IPv6), tổng kiểm tra tiêu đề IPv4 cần được tính toán lại ở mọi bộ định tuyến. Giống như việc phân mảnh và tập hợp lại, đây cũng là một hoạt động tốn kém trong IPv4. • Tùy chọn. Trường tùy chọn không còn là một phần của tiêu đề IP tiêu chuẩn nữa. Tuy nhiên, nó vẫn chưa biến mất. Thay vào đó, trường tùy chọn là một trong những tiêu đề tiếp theo có thể được trỏ đến từ bên trong tiêu đề IPv6. Nghĩa là, giống như các tiêu đề giao thức TCP hoặc UDP có thể là tiêu đề tiếp theo trong gói IP, trường tùy chọn cũng vậy. Việc loại bỏ trường tùy chọn sẽ tạo ra tiêu đề IP có độ dài cố định 40 byte.

Đang chuyển đổi từ IPv4 sang IPv6

Bây giờ chúng ta đã xem chi tiết kỹ thuật của IPv6, chúng ta hãy xem xét một vấn đề rất thực tế: Internet công cộng dựa trên IPv4 sẽ được chuyển đổi sang IPv6 như thế nào? Vấn đề là trong khi các hệ thống có khả năng IPv6 mới có thể tương thích ngược, tức là có thể gửi, định tuyến và nhận các gói dữ liệu IPv4, thì các hệ thống có khả năng IPv4 đã được triển khai lại không có khả năng xử lý các gói dữ liệu IPv6. Có thể có một số tùy chọn \[Huston 2011b, RFC 4213\].

Một tùy chọn là tuyên bố ngày gắn cờ---ngày và giờ nhất định khi tất cả các máy Internet sẽ bị tắt và nâng cấp từ IPv4 lên IPv6. Quá trình chuyển đổi công nghệ lớn gần đây nhất (từ sử dụng NCP sang sử dụng TCP để có dịch vụ vận tải đáng tin cậy) đã xảy ra gần 40 năm trước. Ngay cả khi đó \[RFC 801\], khi Internet còn rất nhỏ và vẫn được quản lý bởi một số ít "pháp sư", người ta đã nhận ra rằng một ngày chào cờ như vậy là không thể thực hiện được. Ngày nay, một ngày chào cờ liên quan đến hàng tỷ thiết bị thậm chí còn khó tưởng tượng hơn.

Cách tiếp cận chuyển đổi IPv4-to-IPv6 đã được áp dụng rộng rãi nhất trong thực tế liên quan đến việc tạo đường hầm \[RFC 4213\]. Ý tưởng cơ bản đằng sau việc tạo đường hầm---một khái niệm quan trọng với các ứng dụng trong nhiều tình huống khác ngoài quá trình chuyển đổi IPv4sang-IPv6, bao gồm cả việc sử dụng rộng rãi trong các mạng di động toàn IP mà chúng ta sẽ đề cập trong Chương 7---là như sau. Giả sử hai nút IPv6 (trong ví dụ này là B và E trong Hình 4.27) muốn tương tác bằng cách sử dụng các gói dữ liệu IPv6 nhưng được kết nối với nhau bằng cách can thiệp vào các bộ định tuyến IPv4. Chúng tôi gọi tập hợp các bộ định tuyến IPv4 nằm giữa hai bộ định tuyến IPv6 như một đường hầm, như được minh họa trong Hình 4.27. Với đường hầm, nút IPv6 ở phía gửi của đường hầm (trong ví dụ này là B) lấy toàn bộ gói dữ liệu IPv6 và đặt nó vào trường dữ liệu (tải trọng) của gói dữ liệu IPv4. Sau đó, datagram IPv4 này được gửi đến nút IPv6 ở phía nhận của đường hầm (trong ví dụ này là E) và được gửi đến nút đầu tiên trong đường hầm (trong ví dụ này là C). Các bộ định tuyến IPv4 can thiệp trong đường hầm định tuyến gói dữ liệu IPv4 này với nhau, giống như cách chúng thực hiện với bất kỳ gói dữ liệu nào khác, vui vẻ không biết rằng bản thân gói dữ liệu IPv4 đã chứa một gói dữ liệu IPv6 hoàn chỉnh. Nút IPv6 ở phía nhận của đường hầm cuối cùng nhận được gói dữ liệu IPv4 (nó là đích của gói dữ liệu IPv4!), xác định rằng gói dữ liệu IPv4 chứa gói dữ liệu IPv6 (bằng cách quan sát rằng trường số giao thức trong gói dữ liệu IPv4 là 41 \[RFC 4213\], chỉ ra rằng Tải trọng IPv4 là một gói dữ liệu IPv6), trích xuất gói dữ liệu IPv6 và sau đó định tuyến gói dữ liệu IPv6 chính xác như khi nó nhận được gói dữ liệu IPv6 từ một hàng xóm IPv6 được kết nối trực tiếp.

Chúng tôi kết thúc phần này bằng cách lưu ý rằng mặc dù việc áp dụng IPv6 ban đầu diễn ra chậm chạp \[Lawton 2001; Huston 2008b\], động lực đang được xây dựng. NIST \[NIST IPv6 2020\] báo cáo rằng hơn một phần ba tên miền cấp hai của chính phủ Hoa Kỳ được kích hoạt IPv6. Về phía khách hàng, Google báo cáo rằng khoảng 25 phần trăm khách hàng truy cập các dịch vụ của Google thực hiện việc này thông qua IPv6 \[Google IPv6 2020\]. Các phép đo gần đây khác \[Czyz 2014\] chỉ ra rằng việc áp dụng IPv6 đang tăng tốc. Sự phổ biến của các thiết bị như điện thoại hỗ trợ IP và các thiết bị di động khác

cung cấp thêm động lực để triển khai rộng rãi hơn IPv6. Chương trình đối tác thế hệ thứ ba của Châu Âu \[3GPP 2020\] đã chỉ định IPv6 làm sơ đồ đánh địa chỉ tiêu chuẩn cho đa phương tiện di động.

Một bài học quan trọng mà chúng ta có thể học được từ trải nghiệm IPv6 là việc thay đổi các giao thức lớp mạng là vô cùng khó khăn. Kể từ đầu những năm 1990, nhiều giao thức lớp mạng mới đã được coi là cuộc cách mạng lớn tiếp theo của Internet, nhưng cho đến nay hầu hết các giao thức này đều có mức độ thâm nhập hạn chế. Các giao thức này bao gồm IPv6, giao thức multicast và giao thức dự trữ tài nguyên; thảo luận về hai loại giao thức sau này có thể được tìm thấy trong phần bổ sung trực tuyến cho văn bản này. Thật vậy, việc đưa các giao thức mới vào lớp mạng cũng giống như thay thế nền móng của một ngôi nhà - rất khó thực hiện nếu không phá bỏ toàn bộ ngôi nhà hoặc ít nhất là tạm thời di dời cư dân trong ngôi nhà. Mặt khác, Internet đã chứng kiến ​​sự triển khai nhanh chóng các giao thức mới ở lớp ứng dụng. Tất nhiên, những ví dụ kinh điển là Web, tin nhắn tức thời, phương tiện truyền thông trực tuyến, trò chơi được phân phối và các hình thức truyền thông xã hội khác nhau. Việc giới thiệu các giao thức lớp ứng dụng mới cũng giống như thêm một lớp sơn mới vào một ngôi nhà---việc này tương đối dễ thực hiện và nếu bạn chọn một màu hấp dẫn, những người khác trong khu vực lân cận sẽ sao chép bạn.

MỘT

B

C

D

E

F

IPv6

A đến B: IPv6

Chế độ xem vật lý

B đến C: IPv4 (đóng gói IPv6)

D đến E: IPv4 (đóng gói IPv6)

E đến F: IPv6

IPv6 IPv4 IPv4 IPv6 IPv6

Luồng: X Nguồn: A Đích: F

dữ liệu

Nguồn: B Đích: E

Nguồn: B Đích: E

MỘT

B

E

F

IPv6

Chế độ xem logic

IPv6

Đường hầm

IPv6 IPv6

Luồng: X Nguồn: A Đích: F

dữ liệu

Luồng: X Nguồn: A Đích: F

dữ liệu

Luồng: X Nguồn: A Đích: F

dữ liệu

*Hình 4.27 ♦ Đào hầm*

Tóm lại, trong tương lai, chúng ta chắc chắn có thể mong đợi sẽ thấy những thay đổi trong lớp mạng của Internet, nhưng những thay đổi này có thể sẽ xảy ra ở quy mô thời gian chậm hơn nhiều so với những thay đổi sẽ xảy ra ở lớp ứng dụng.

**4.4 Chuyển tiếp tổng quát và SDN**

Hãy nhớ lại rằng Phần 4.2.1 mô tả chuyển tiếp dựa trên đích là hai bước tìm kiếm địa chỉ IP đích ("khớp"), sau đó gửi gói vào cơ cấu chuyển mạch tới cổng đầu ra được chỉ định ("hành động"). Bây giờ chúng ta hãy xem xét một mô hình "kết hợp-cộng-hành động" tổng quát hơn đáng kể, trong đó việc "khớp" có thể được thực hiện trên nhiều trường tiêu đề được liên kết với các giao thức khác nhau ở các lớp khác nhau trong ngăn xếp giao thức. "Hành động" có thể bao gồm chuyển tiếp gói đến một hoặc nhiều cổng đầu ra (như trong chuyển tiếp dựa trên đích), cân bằng tải các gói trên nhiều giao diện gửi đi dẫn đến một dịch vụ (như trong cân bằng tải), ghi lại các giá trị tiêu đề (như trong NAT), cố tình chặn/thả gói (như trong tường lửa), gửi gói đến một máy chủ đặc biệt để xử lý và thực hiện hành động tiếp theo (như trong DPI), v.v.

Trong chuyển tiếp tổng quát, bảng khớp-cộng-hành động khái quát hóa khái niệm bảng chuyển tiếp dựa trên đích mà chúng ta đã gặp trong Phần 4.2.1. Bởi vì các quyết định chuyển tiếp có thể được thực hiện bằng cách sử dụng địa chỉ nguồn và đích của lớp mạng và/hoặc lớp liên kết, nên các thiết bị chuyển tiếp được hiển thị trong Hình 4.28 được mô tả chính xác hơn là "bộ chuyển mạch gói" thay vì "bộ định tuyến" lớp 3 hoặc "bộ chuyển mạch" lớp 2. Do đó, trong phần còn lại của phần này và trong Phần 5.5, chúng tôi sẽ gọi các thiết bị này là chuyển mạch gói, sử dụng thuật ngữ đang được áp dụng rộng rãi trong tài liệu SDN.

Hình 4.28 hiển thị bảng kết hợp hành động trong mỗi chuyển mạch gói, với bảng được tính toán, cài đặt và cập nhật bởi bộ điều khiển từ xa. Chúng tôi lưu ý rằng mặc dù các thành phần điều khiển tại các chuyển mạch gói riêng lẻ có thể tương tác với nhau (ví dụ: theo cách tương tự như trong Hình 4.2), nhưng trên thực tế, khả năng kết hợp hành động tổng quát được triển khai thông qua bộ điều khiển từ xa tính toán, cài đặt và cập nhật các bảng này. Bạn có thể mất một phút để so sánh Hình 4.2, 4.3 và 4.28---bạn nhận thấy những điểm tương đồng và khác biệt nào giữa chuyển tiếp dựa trên đích được hiển thị trong Hình 4.2 và 4.3 và chuyển tiếp tổng quát được hiển thị trong Hình 4.28?

Cuộc thảo luận sau đây của chúng tôi về chuyển tiếp tổng quát sẽ dựa trên OpenFlow \[McKeown 2008, ONF 2020, Casado 2014, Tourrilhes 2014\]---một tiêu chuẩn dễ thấy đã đi tiên phong trong khái niệm về bộ điều khiển và trừu tượng hóa chuyển tiếp khớp với hành động, cũng như cuộc cách mạng SDN nói chung \[Feamster 2013\]. Chúng ta sẽ chủ yếu xem xét OpenFlow 1.0, phiên bản này đã giới thiệu chức năng và tóm tắt SDN chính theo cách đặc biệt rõ ràng và ngắn gọn. Các phiên bản sau của OpenFlow đã giới thiệu các khả năng bổ sung nhờ kinh nghiệm có được thông qua

thực hiện và sử dụng; Bạn có thể tìm thấy các phiên bản hiện tại và cũ hơn của tiêu chuẩn OpenFlow tại \[ONF 2020\].

Mỗi mục trong bảng chuyển tiếp khớp với hành động, được gọi là bảng quy trình trong OpenFlow, bao gồm:

• Một tập hợp các giá trị trường tiêu đề mà gói tin đến sẽ phù hợp. Như trong trường hợp chuyển tiếp dựa trên đích, việc so khớp dựa trên phần cứng được thực hiện nhanh nhất trong bộ nhớ TCAM, với hơn một triệu mục nhập địa chỉ đích có thể thực hiện được \[Bosshart 2013\]. Một gói không phù hợp với mục nhập bảng luồng có thể bị loại bỏ hoặc gửi đến bộ điều khiển từ xa để xử lý thêm. Trong thực tế, một bảng luồng có thể được triển khai bởi nhiều bảng luồng vì lý do hiệu suất hoặc chi phí \[Bosshart 2013\], nhưng ở đây chúng ta sẽ tập trung vào tính trừu tượng của một bảng luồng duy nhất.

Bộ điều khiển từ xa

Các giá trị trong tiêu đề của gói tin đến

Bảng luồng cục bộ

\... \... \... \...

\... \... \... \...

\... \... \... \...

Headers Hành động đếm

Mặt phẳng điều khiển

Mặt phẳng dữ liệu

*Hình 4.28 ♦ Chuyển tiếp tổng quát: Mỗi chuyển mạch gói chứa một*

bảng kết hợp hành động cộng được tính toán và phân phối bởi bộ điều khiển từ xa

• Một tập hợp các bộ đếm được cập nhật khi các gói được khớp với các mục trong bảng luồng. Các bộ đếm này có thể bao gồm số lượng gói được khớp với mục nhập bảng đó và thời gian kể từ khi mục nhập bảng được cập nhật lần cuối. • Một tập hợp các hành động được thực hiện khi một gói khớp với một mục trong bảng luồng. Những hành động này có thể là chuyển tiếp gói đến một cổng đầu ra nhất định, loại bỏ gói, tạo bản sao của gói và gửi chúng đến nhiều cổng đầu ra và/hoặc viết lại các trường tiêu đề đã chọn.

Chúng ta sẽ tìm hiểu cách so khớp và hành động chi tiết hơn ở Phần 4.4.1 và 4.4.2 tương ứng. Sau đó, chúng tôi sẽ nghiên cứu cách sử dụng bộ sưu tập quy tắc khớp chuyển đổi trên mỗi gói trên toàn mạng để triển khai nhiều chức năng bao gồm định tuyến, chuyển mạch lớp 2, tường lửa, cân bằng tải, mạng ảo, v.v. trong Phần 4.4.3. Cuối cùng, chúng tôi lưu ý rằng bảng luồng về cơ bản là một API, sự trừu tượng hóa mà qua đó hành vi của một bộ chuyển mạch gói riêng lẻ có thể được lập trình; chúng ta sẽ thấy trong Phần 4.4.3 rằng các hành vi trên toàn mạng có thể được lập trình tương tự bằng cách lập trình/cấu hình phù hợp các bảng này trong bộ sưu tập các bộ chuyển mạch gói mạng \[Casado 2014\].

**4.4.1 Trận đấu**

Hình 4.29 hiển thị 11 trường tiêu đề gói và ID cổng đến có thể khớp với quy tắc khớp cộng hành động của OpenFlow 1.0. Nhớ lại Phần 1.5.2 rằng khung lớp liên kết (lớp 2) đến bộ chuyển mạch gói sẽ chứa gói dữ liệu lớp mạng (lớp 3) làm tải trọng của nó, do đó tải trọng này thường chứa phân đoạn lớp vận chuyển (lớp 4). Quan sát đầu tiên mà chúng tôi đưa ra là tính năng trừu tượng hóa đối sánh của OpenFlow cho phép thực hiện đối sánh trên các trường đã chọn từ ba lớp tiêu đề giao thức (do đó, việc thách thức khá trắng trợn nguyên tắc phân lớp mà chúng tôi đã nghiên cứu trong Phần 1.5). Vì chúng ta chưa đề cập đến lớp liên kết nên chỉ cần nói rằng địa chỉ MAC nguồn và đích được hiển thị trong Hình 4.29 là địa chỉ lớp liên kết được liên kết với giao diện gửi và nhận của khung; bằng cách chuyển tiếp trên cơ sở địa chỉ Ethernet thay vì địa chỉ IP, chúng ta có thể thấy rằng thiết bị hỗ trợ OpenFlow có thể hoạt động tương tự

Xâm nhập

Port

Src MAC

MAC Dst

Loại đạo đức

Vlan

NHẬN DẠNG

Vlan

Giá trị IP Src IP Dst IP Proto

IP ĐKDV

TCP/UDP

Src Port

TCP/UDP

Dst Port

Lớp vận chuyển Lớp mạng Lớp liên kết

*Hình 4.29 ♦ Packet các trường khớp, bảng luồng OpenFlow 1.0*

như một bộ định tuyến (thiết bị lớp 3) chuyển tiếp các gói dữ liệu cũng như các khung chuyển tiếp của bộ chuyển mạch (thiết bị lớp 2). Trường loại Ethernet tương ứng với giao thức lớp trên (ví dụ: IP) mà trọng tải của khung sẽ được phân kênh và các trường Vlan liên quan đến cái gọi là mạng cục bộ ảo mà chúng ta sẽ nghiên cứu trong Chương 6. Tập hợp 12 giá trị có thể khớp trong đặc tả OpenFlow 1.0 đã tăng lên 41 giá trị trong các thông số kỹ thuật OpenFlow gần đây hơn \[Bosshart 2014\].

Cổng vào đề cập đến cổng đầu vào tại bộ chuyển mạch gói mà gói được nhận. Địa chỉ nguồn IP của gói, địa chỉ đích IP, trường giao thức IP và loại trường dịch vụ IP đã được thảo luận trước đó trong Phần 4.3.1. Các trường số cổng nguồn và cổng đích của lớp vận chuyển cũng có thể được khớp.

Các mục trong bảng quy trình cũng có thể có ký tự đại diện. Ví dụ: địa chỉ IP của 128.119.\*.\* trong bảng luồng sẽ khớp với trường địa chỉ tương ứng của bất kỳ gói dữ liệu nào có 128.119 là 16 bit đầu tiên trong địa chỉ của nó. Mỗi mục trong bảng quy trình cũng có mức độ ưu tiên liên quan. Nếu một gói khớp với nhiều mục trong bảng luồng, thì kết quả khớp được chọn và hành động tương ứng sẽ là mục có mức độ ưu tiên cao nhất mà gói khớp với.

Cuối cùng, chúng tôi nhận thấy rằng không phải tất cả các trường trong tiêu đề IP đều có thể khớp. Ví dụ: OpenFlow không cho phép khớp trên cơ sở trường TTL hoặc trường độ dài gói dữ liệu. Tại sao một số trường được phép khớp, trong khi những trường khác thì không? Không còn nghi ngờ gì nữa, câu trả lời liên quan đến sự cân bằng giữa chức năng và độ phức tạp. "Nghệ thuật" trong việc lựa chọn một sự trừu tượng là cung cấp đủ chức năng để hoàn thành một nhiệm vụ (trong trường hợp này là triển khai, định cấu hình và quản lý một loạt các chức năng của lớp mạng mà trước đây đã được triển khai thông qua một loạt các thiết bị lớp mạng), mà không tạo ra quá nhiều gánh nặng cho sự trừu tượng với quá nhiều chi tiết và tổng quát đến mức nó trở nên cồng kềnh và không thể sử dụng được. Butler Lampson đã có câu nói nổi tiếng \[Lampson 1983\]:

Hãy làm từng việc một và làm thật tốt. Một giao diện phải nắm bắt được những điều cần thiết tối thiểu của một sự trừu tượng. Đừng khái quát hóa; khái quát hóa nói chung là sai.

Với sự thành công của OpenFlow, người ta có thể phỏng đoán rằng các nhà thiết kế của nó thực sự đã chọn rất tốt sự trừu tượng của họ. Bạn có thể tìm thấy chi tiết bổ sung về kết hợp OpenFlow trong \[ONF 2020\].

**4.4.2 Hành động**

Như được hiển thị trong Hình 4.28, mỗi mục trong bảng luồng có một danh sách không hoặc nhiều hành động xác định quá trình xử lý sẽ được áp dụng cho gói phù hợp với mục nhập của bảng luồng. Nếu có nhiều hành động, chúng sẽ được thực hiện theo thứ tự được chỉ định trong danh sách.

Trong số những hành động quan trọng nhất có thể thực hiện được là: • Chuyển tiếp. Một gói đến có thể được chuyển tiếp đến một cổng đầu ra vật lý cụ thể, phát quảng bá trên tất cả các cổng (ngoại trừ cổng mà nó đến) hoặc phát đa hướng trên một bộ cổng đã chọn. Gói tin có thể được đóng gói và gửi đến bộ điều khiển từ xa cho thiết bị này. Sau đó, bộ điều khiển đó có thể (hoặc không) thực hiện một số hành động đối với gói đó, bao gồm cài đặt các mục trong bảng luồng mới và có thể trả gói tin về thiết bị để chuyển tiếp theo bộ quy tắc bảng luồng được cập nhật. • Đánh rơi. Một mục trong bảng luồng không có hành động nào cho biết rằng gói phù hợp sẽ bị loại bỏ. • Trường sửa đổi. Các giá trị trong 10 trường tiêu đề gói (tất cả các trường lớp 2, 3 và 4 được hiển thị trong Hình 4.29 ngoại trừ trường Giao thức IP) có thể được ghi lại trước khi gói được chuyển tiếp đến cổng đầu ra đã chọn.

**4.4.3 Ví dụ về OpenFlow về hành động kết hợp cộng trong hành động**

Bây giờ đã xem xét cả thành phần kết hợp và hành động của chuyển tiếp tổng quát, hãy đặt những ý tưởng này lại với nhau trong bối cảnh mạng mẫu được hiển thị trong Hình 4.30. Mạng có 6 máy chủ (h1, h2, h3, h4, h5 và h6) và ba bộ chuyển mạch gói (s1, s2 và s3), mỗi bộ có bốn giao diện cục bộ (được đánh số từ 1 đến 4). Chúng tôi sẽ xem xét một số hành vi trên toàn mạng mà chúng tôi muốn triển khai và các mục trong bảng quy trình trong s1, s2 và s3 cần thiết để triển khai hành vi này.

s3 s3

s1

s2

Host h6 10.3.0.6

Bộ điều khiển OpenFlow

Host h5 10.3.0.5

Host h1 10.1.0.1 Host h2 10.1.0.2

Host h3 10.2.0.3

Host h4 10.2.0.4

*Hình 4.30 ♦ Mạng kết hợp hành động OpenFlow với ba gói*

thiết bị chuyển mạch, 6 máy chủ và bộ điều khiển OpenFlow

Ví dụ đầu tiên: Chuyển tiếp đơn giản

Một ví dụ rất đơn giản, giả sử rằng hành vi chuyển tiếp mong muốn là các gói từ h5 hoặc h6 được định hướng đến h3 hoặc h4 sẽ được chuyển tiếp từ s3 đến s1, sau đó từ s1 đến s2 (do đó tránh hoàn toàn việc sử dụng liên kết giữa s3 và s2). Mục nhập bảng luồng trong s1 sẽ là:

Bảng quy trình s1 (Ví dụ 1)

Hành động trận đấu

Vào Port = 1 ; IP Src = 10.3.\*.\* ; IP Dst = 10,2.\*.\* Chuyển tiếp(4)

... ...

Tất nhiên, chúng ta cũng sẽ cần một mục trong bảng luồng trong s3 để các datagram được gửi từ h5 hoặc h6 được chuyển tiếp đến s1 qua giao diện gửi đi 3:

Bảng quy trình s3 (Ví dụ 1)

Hành động trận đấu

IP Src = 10.3.\*.\* ; IP Dst = 10,2.\*.\* Chuyển tiếp(3)

... ...

Cuối cùng, chúng ta cũng cần một mục trong bảng luồng trong s2 để hoàn thành ví dụ đầu tiên này, để các gói dữ liệu đến từ s1 được chuyển tiếp đến đích của chúng, máy chủ h3 hoặc h4:

Bảng quy trình s2 (Ví dụ 1)

Hành động trận đấu

Cổng vào = 2; IP Dst = 10.2.0.3 Chuyển tiếp(3)

Cổng vào = 2; IP Dst = 10.2.0.4 Chuyển tiếp(4)

... ...

Ví dụ thứ hai: Cân bằng tải

Ví dụ thứ hai, hãy xem xét kịch bản cân bằng tải, trong đó các gói dữ liệu từ h3 có đích đến 10.1.\*.\* sẽ được chuyển tiếp qua liên kết trực tiếp giữa s2 và s1, trong khi các gói dữ liệu từ h4 có đích đến 10.1.\*.\* sẽ được chuyển tiếp qua liên kết giữa s2 và s3 (và sau đó từ s3 đến s1). Lưu ý rằng không thể đạt được hành vi này bằng chuyển tiếp dựa trên đích của IP. Trong trường hợp này, bảng luồng trong s2 sẽ là:

Bảng luồng s2 (Ví dụ 2)

Hành động trận đấu

Cổng vào = 3; IP Dst = 10.1.\*.\* Chuyển tiếp(2)

Cổng vào = 4; IP Dst = 10.1.\*.\* Chuyển tiếp(1)

... ...

Các mục trong bảng luồng cũng cần thiết tại s1 để chuyển tiếp các datagram nhận được từ s2 tới h1 hoặc h2; và các mục trong bảng luồng là cần thiết tại s3 để chuyển tiếp các datagram nhận được trên giao diện 4 từ s2 qua giao diện 3 tới s1. Xem liệu bạn có thể tìm ra các mục trong bảng luồng này ở s1 và s3 hay không.

Ví dụ thứ ba: Tường lửa

Ví dụ thứ ba, hãy xem xét một kịch bản tường lửa trong đó s2 chỉ muốn nhận lưu lượng truy cập (trên bất kỳ giao diện nào của nó) được gửi từ các máy chủ được gắn vào s3.

Bảng luồng s2 (Ví dụ 3)

Hành động trận đấu

IP Src = 10.3.\*.\* IP Dst = 10.2.0.3 Chuyển tiếp(3)

IP Src = 10.3.\*.\* IP Dst = 10.2.0.4 Chuyển tiếp(4)

... ...

Nếu không có mục nào khác trong bảng luồng của s2 thì chỉ lưu lượng truy cập từ 10.3.\*.\* mới được chuyển tiếp đến các máy chủ gắn liền với s2.

Mặc dù chúng tôi chỉ xem xét một số tình huống cơ bản ở đây nhưng hy vọng rằng tính linh hoạt và lợi thế của việc chuyển tiếp tổng quát là rõ ràng. Trong các bài tập về nhà, chúng ta sẽ khám phá cách sử dụng bảng luồng để tạo ra nhiều hành vi logic khác nhau, bao gồm các mạng ảo---hai hoặc nhiều mạng riêng biệt về mặt logic (mỗi mạng có hành vi chuyển tiếp độc lập và riêng biệt)---sử dụng cùng một bộ chuyển mạch và liên kết gói vật lý. Trong Phần 5.5, chúng ta sẽ quay lại bảng luồng khi nghiên cứu các bộ điều khiển SDN tính toán và phân phối các bảng luồng cũng như giao thức được sử dụng để liên lạc giữa bộ chuyển mạch gói và bộ điều khiển của nó.

Các bảng luồng khớp-cộng-hành động mà chúng ta đã thấy trong phần này thực sự là một dạng lập trình hạn chế, chỉ định cách bộ định tuyến sẽ chuyển tiếp và thao tác (ví dụ: thay đổi trường tiêu đề) một gói dữ liệu, dựa trên sự khớp giữa các giá trị tiêu đề của gói dữ liệu và các điều kiện khớp. Người ta có thể tưởng tượng một dạng khả năng lập trình thậm chí còn phong phú hơn---một ngôn ngữ lập trình với các cấu trúc cấp cao hơn như biến, số học mục đích chung và các phép toán Boolean, biến, hàm và câu lệnh điều kiện, cũng như các cấu trúc cụ thể.

được thiết kế để xử lý datagram ở tốc độ đường truyền. P4 (Bộ xử lý Packet độc lập với giao thức lập trình) \[P4 2020\] là một ngôn ngữ như vậy và đã thu hút được sự quan tâm cũng như sức hút đáng kể kể từ khi được giới thiệu cách đây 5 năm \[Bosshart 2014\].

**4.5 Hộp giữa**

Routers là những con ngựa thồ của lớp mạng và trong chương này, chúng ta đã tìm hiểu cách chúng hoàn thành công việc "bánh mì và bơ" là chuyển tiếp các gói dữ liệu IP tới đích của chúng. Nhưng trong chương này và các chương trước, chúng ta cũng đã gặp các thiết bị mạng khác ("hộp") trong mạng nằm trên đường dẫn dữ liệu và thực hiện các chức năng khác ngoài chuyển tiếp. Chúng tôi đã gặp bộ nhớ đệm Web trong Phần 2.2.5; TCP bộ chia kết nối trong phần 3.7; và dịch địa chỉ mạng (NAT), tường lửa và hệ thống phát hiện xâm nhập trong Phần 4.3.4. Chúng ta đã tìm hiểu trong Phần 4.4 rằng chuyển tiếp tổng quát cho phép bộ định tuyến hiện đại thực hiện tường lửa và cân bằng tải một cách dễ dàng và tự nhiên bằng các hoạt động "kết hợp cộng với hành động" tổng quát.

Trong 20 năm qua, chúng tôi đã chứng kiến ​​sự tăng trưởng vượt bậc của các hộp trung gian như vậy, được RFC 3234 định nghĩa là:

"bất kỳ hộp trung gian nào thực hiện các chức năng ngoài các chức năng tiêu chuẩn, thông thường của bộ định tuyến IP trên đường dẫn dữ liệu giữa máy chủ nguồn và máy chủ đích"

Chúng ta có thể xác định rộng rãi ba loại dịch vụ được thực hiện bởi các hộp trung gian:

• NAT Bản dịch. Như chúng ta đã thấy trong Phần 4.3.4, các hộp NAT triển khai việc đánh địa chỉ mạng riêng, ghi lại tiêu đề gói dữ liệu IP địa chỉ và số cổng. • Dịch vụ bảo mật. Tường lửa chặn lưu lượng dựa trên giá trị trường tiêu đề hoặc chuyển hướng gói để xử lý bổ sung, chẳng hạn như kiểm tra gói sâu (DPI). Hệ thống phát hiện xâm nhập (IDS) có thể phát hiện các mẫu được xác định trước và lọc các gói tương ứng. Bộ lọc e-mail cấp ứng dụng chặn các e-mail được coi là rác, lừa đảo hoặc gây ra mối đe dọa bảo mật. • Nâng cao hiệu suất. Các hộp trung gian này thực hiện các dịch vụ như nén, lưu vào bộ nhớ đệm nội dung và cân bằng tải các yêu cầu dịch vụ (ví dụ: yêu cầu HTTP hoặc truy vấn công cụ tìm kiếm) tới một trong các nhóm máy chủ có thể cung cấp dịch vụ mong muốn.

Nhiều hộp trung gian khác \[RFC 3234\] cung cấp các khả năng thuộc ba loại dịch vụ này, trong cả mạng di động có dây và không dây \[Wang 2011\].

Với sự gia tăng của các hộp trung gian, người phục vụ cần vận hành, quản lý và nâng cấp thiết bị này. Hộp phần cứng chuyên dụng riêng biệt, riêng biệt

ngăn xếp phần mềm và các kỹ năng quản lý/vận hành riêng biệt dẫn đến chi phí vốn và hoạt động đáng kể. Có lẽ không có gì đáng ngạc nhiên khi các nhà nghiên cứu đang khám phá việc sử dụng phần cứng thông dụng (mạng, điện toán và lưu trữ) bằng phần mềm chuyên dụng được xây dựng trên nền tảng phần mềm chung---chính xác là cách tiếp cận được thực hiện trong SDN một thập kỷ trước---để triển khai các dịch vụ này. Cách tiếp cận này được gọi là ảo hóa chức năng mạng (NFV) \[Mijumbi 2016\]. Một cách tiếp cận khác cũng đã được khám phá là thuê ngoài chức năng hộp trung gian cho đám mây \[Sherry 2012\].

Trong nhiều năm, kiến ​​trúc Internet có sự tách biệt rõ ràng giữa lớp mạng và lớp vận chuyển/ứng dụng. Vào thời xa xưa này, lớp mạng bao gồm các bộ định tuyến, hoạt động trong lõi mạng, để chuyển tiếp các gói dữ liệu tới đích của chúng chỉ bằng cách sử dụng các trường trong tiêu đề gói dữ liệu IP. Các lớp vận chuyển và ứng dụng được triển khai trên các máy chủ hoạt động ở biên mạng. Hosts trao đổi các gói với nhau trong các phân đoạn lớp vận chuyển và các tin nhắn lớp ứng dụng. Các hộp trung gian ngày nay rõ ràng đã vi phạm sự phân tách này: một hộp NAT, nằm giữa bộ định tuyến và máy chủ, ghi lại các địa chỉ IP lớp mạng và số cổng của lớp vận chuyển; tường lửa trong mạng chặn các gói dữ liệu đáng ngờ bằng cách sử dụng các trường tiêu đề lớp ứng dụng (ví dụ: HTTP), lớp vận chuyển và lớp mạng; Các cổng bảo mật e-mail được chèn vào giữa người gửi e-mail (dù có độc hại hay không) và người nhận e-mail dự định, lọc các tin nhắn e-mail của lớp ứng dụng dựa trên các địa chỉ IP trong danh sách trắng/danh sách đen cũng như nội dung tin nhắn e-mail. Trong khi có những người coi những hộp trung gian như vậy là một thứ kiến ​​trúc ghê tởm \[Garfinkel 2003\], thì những người khác lại chấp nhận triết lý rằng những hộp trung gian như vậy "tồn tại vì những lý do quan trọng và lâu dài"---rằng chúng đáp ứng một nhu cầu quan trọng---và rằng chúng ta sẽ có nhiều hơn, chứ không phải ít hơn, các hộp trung gian trong tương lai \[Walfish 2004\]. Xem phần trong thanh bên đính kèm về "Đối số từ đầu đến cuối" để có một góc nhìn hơi khác về câu hỏi về vị trí đặt chức năng dịch vụ trong mạng.

NGUYÊN TẮC KIẾN TRÚC INTERNET

Với sự thành công phi thường của Internet, người ta có thể tự nhiên thắc mắc về các nguyên tắc kiến ​​trúc đã hướng dẫn sự phát triển của cái được cho là hệ thống được thiết kế lớn nhất và phức tạp nhất từng được nhân loại xây dựng. RFC 1958, có tựa đề "Nguyên tắc kiến ​​trúc của Internet", gợi ý rằng những nguyên tắc này, nếu thực sự tồn tại, thực sự rất tối thiểu:

\"Nhiều thành viên của cộng đồng Internet sẽ lập luận rằng không có kiến ​​trúc mà chỉ có một truyền thống, điều này đã không được viết ra trong 25 năm đầu tiên (hoặc ít nhất là không phải bởi IAB). Tuy nhiên, nói một cách rất chung chung, cộng đồng tin rằng mục tiêu là kết nối, công cụ là Giao thức Internet và trí thông minh là từ đầu đến cuối chứ không phải ẩn trong mạng.\" \[RFC 1958\]

NGUYÊN TẮC TRONG THỰC HÀNH

Vì vậy, chúng tôi có nó! Mục tiêu là cung cấp khả năng kết nối, sẽ chỉ có một giao thức lớp mạng (giao thức IP nổi tiếng mà chúng ta đã nghiên cứu trong chương này) và "sự thông minh" (người ta có thể nói là "độ phức tạp") sẽ được đặt ở rìa mạng, thay vì trong lõi mạng. Chúng ta hãy xem xét hai điều cần cân nhắc cuối cùng này chi tiết hơn một chút.

ĐỒNG HỒ GIỜ IP

Đến bây giờ, chúng ta đã làm quen với chồng giao thức Internet năm lớp mà chúng ta gặp lần đầu trong Hình 1.23. Một hình ảnh trực quan khác của ngăn xếp này, được hiển thị trong Hình 4.31 và đôi khi được gọi là "đồng hồ cát IP," minh họa "vòng eo hẹp" của kiến ​​trúc Internet nhiều lớp. Mặc dù Internet có nhiều giao thức ở lớp vật lý, liên kết, truyền tải và ứng dụng nhưng chỉ có một giao thức lớp mạng---giao thức IP. Đây là một giao thức phải được triển khai bởi từng thiết bị trong số hàng tỷ thiết bị được kết nối Internet. Vòng eo hẹp này đã đóng một vai trò quan trọng trong sự phát triển phi thường của Internet. Tính đơn giản tương đối của giao thức IP và thực tế là đó là yêu cầu phổ biến duy nhất cho kết nối Internet đã cho phép nhiều loại mạng phong phú---với các công nghệ lớp liên kết cơ bản rất khác nhau, từ Ethernet đến WiFi đến mạng di động đến mạng quang trở thành một phần của Internet. \[Clark 1997\] lưu ý rằng vai trò của phần eo hẹp mà ông gọi là "lớp trải dài" là để "... che giấu sự khác biệt chi tiết giữa các công nghệ \[cơ bản\] khác nhau này và đưa ra giao diện dịch vụ thống nhất cho các ứng dụng ở trên". Đối với lớp IP nói riêng: \"Làm thế nào để lớp mở rộng IP đạt được mục đích của nó? Nó xác định một tập hợp dịch vụ cơ bản, được thiết kế cẩn thận để có thể xây dựng chúng từ nhiều công nghệ mạng cơ bản. Phần mềm, như một phần của lớp Internet \[tức là mạng\], chuyển những gì mà mỗi công nghệ lớp thấp hơn này cung cấp thành dịch vụ chung của lớp Internet.\"

Để thảo luận về vòng eo hẹp, bao gồm các ví dụ ngoài Internet, hãy xem \[Beck 2019; Akhshabi 2011\]. Ở đây chúng tôi lưu ý rằng khi kiến ​​trúc Internet bước vào tuổi thọ trung bình (chắc chắn,

IP

TCP UDP

HTTP SMTP DASH NHANH CHÓNG

RTP ...

Ethernet PPP ...

WiFi Bluetooth PDCP

đài phát thanh sợi đồng

*Hình 4.31 ♦ Đồng hồ cát Internet eo hẹp*

Độ tuổi từ 40 đến 50 của Internet đủ tiêu chuẩn cho độ tuổi trung niên!), người ta có thể nhận thấy rằng "vòng eo hẹp" của nó thực sự có thể mở rộng ra một chút (như thường xảy ra ở tuổi trung niên!) thông qua sự gia tăng của các hộp trung gian.

CUỘC TRANH LUẬN KẾT THÚC

Nguyên tắc thứ ba trong RFC 1958---rằng "trí thông minh là từ đầu đến cuối chứ không phải ẩn trong mạng"---nói đến việc sắp xếp các chức năng trong mạng. Ở đây, chúng ta đã thấy rằng cho đến khi các hộp trung gian xuất hiện gần đây, hầu hết chức năng Internet thực sự được đặt ở rìa mạng. Cần lưu ý rằng, trái ngược hoàn toàn với mạng điện thoại thế kỷ 20---có các điểm cuối "ngu ngốc" (không thể lập trình) và các công tắc thông minh---Internet luôn có các điểm cuối thông minh (máy tính có thể lập trình), cho phép đặt các chức năng phức tạp tại các điểm cuối đó. Nhưng một lập luận mang tính nguyên tắc hơn về việc thực sự đặt chức năng ở các điểm cuối đã được đưa ra trong một bài báo cực kỳ có ảnh hưởng \[Saltzer 1984\] trình bày rõ ràng "lập luận từ đầu đến cuối". Nó tuyên bố:

\"\.... . . có một danh sách các chức năng, mỗi chức năng có thể được triển khai theo bất kỳ cách nào: bởi hệ thống con truyền thông, bởi khách hàng của nó, với tư cách là một liên doanh hoặc có lẽ dư thừa, mỗi chức năng thực hiện phiên bản riêng của mình. Khi lập luận về lựa chọn này, các yêu cầu của ứng dụng cung cấp cơ sở cho một lớp lập luận như sau:

Chức năng được đề cập chỉ có thể được triển khai đầy đủ và chính xác khi có kiến ​​thức và sự trợ giúp của ứng dụng đứng ở điểm cuối của hệ thống truyền thông. Do đó, việc cung cấp chức năng bị nghi vấn đó như một tính năng của chính hệ thống thông tin liên lạc là không thể. (Đôi khi, phiên bản chưa hoàn thiện của chức năng do hệ thống liên lạc cung cấp có thể hữu ích trong việc nâng cao hiệu suất.)

Chúng tôi gọi dòng lý luận chống lại việc triển khai hàm cấp thấp này là "đối số từ đầu đến cuối".

Một ví dụ minh họa đối số end-to-end là việc truyền dữ liệu đáng tin cậy. Vì các gói có thể bị mất trong mạng (ví dụ: ngay cả khi không có lỗi tràn bộ đệm, bộ định tuyến đang giữ gói được xếp trong hàng đợi có thể gặp sự cố hoặc một phần mạng trong đó gói được xếp trong hàng đợi sẽ bị tách ra do lỗi liên kết), nên các điểm cuối (trong trường hợp này là thông qua giao thức TCP) phải thực hiện kiểm soát lỗi. Như chúng ta sẽ thấy trong Chương 6, một số giao thức lớp liên kết thực sự thực hiện kiểm soát lỗi cục bộ, nhưng chỉ riêng việc kiểm soát lỗi cục bộ này là "không đầy đủ" và không đủ để cung cấp khả năng truyền dữ liệu đáng tin cậy từ đầu đến cuối. Và do đó, việc truyền dữ liệu đáng tin cậy phải được thực hiện từ đầu đến cuối.

RFC 1958 có chủ ý chỉ bao gồm hai tài liệu tham khảo, cả hai đều là "các tài liệu cơ bản về kiến ​​trúc Internet". Một trong số đó là bản thân bài báo end-to-end \[Saltzer 1984\]; bài viết thứ hai \[Clark 1988\] thảo luận về triết lý thiết kế của Giao thức Internet DARPA. Cả hai đều là những cuốn sách thú vị "phải đọc" đối với bất kỳ ai quan tâm đến kiến ​​trúc Internet. Những phần tiếp theo của \[Clark 1988\] là \[Blumenthal 2001; Clark 2005\] xem xét lại kiến ​​trúc Internet trong bối cảnh môi trường phức tạp hơn nhiều mà Internet ngày nay phải vận hành.

**4.6 Tóm tắt**

Trong chương này, chúng ta đã đề cập đến các chức năng mặt phẳng dữ liệu của lớp mạng---các chức năng của bộ định tuyến xác định cách các gói đến trên một trong các liên kết đầu vào của bộ định tuyến được chuyển tiếp đến một trong các liên kết đầu ra của bộ định tuyến đó. Chúng tôi bắt đầu bằng cách xem xét chi tiết các hoạt động nội bộ của bộ định tuyến, nghiên cứu chức năng cổng đầu vào và đầu ra cũng như chuyển tiếp dựa trên đích, cơ chế chuyển mạch nội bộ của bộ định tuyến, quản lý hàng đợi gói, v.v. Chúng tôi đã đề cập đến cả chuyển tiếp IP truyền thống (trong đó việc chuyển tiếp dựa trên địa chỉ đích của gói dữ liệu) và chuyển tiếp tổng quát (trong đó việc chuyển tiếp và các chức năng khác có thể được thực hiện bằng cách sử dụng các giá trị trong một số trường khác nhau trong tiêu đề của gói dữ liệu) và thấy tính linh hoạt của cách tiếp cận sau. Chúng tôi cũng đã nghiên cứu chi tiết các giao thức IPv4 và IPv6 cũng như địa chỉ Internet mà chúng tôi nhận thấy sâu sắc hơn, tinh tế hơn và thú vị hơn nhiều so với những gì chúng tôi mong đợi. Chúng tôi đã hoàn thành nghiên cứu về mặt phẳng dữ liệu lớp mạng bằng nghiên cứu về hộp trung gian và thảo luận rộng rãi về kiến ​​trúc Internet.

Với sự hiểu biết mới tìm thấy về mặt phẳng dữ liệu của lớp mạng, giờ đây chúng ta đã sẵn sàng đi sâu vào mặt phẳng điều khiển của lớp mạng trong Chương 5!

**Bài tập về nhà vấn đề và câu hỏi**

Câu hỏi ôn tập chương 4

MỤC 4.1 R1. Chúng ta hãy xem lại một số thuật ngữ được sử dụng trong cuốn sách này. Hãy nhớ lại rằng

tên của gói lớp vận chuyển là phân đoạn và tên của gói lớp liên kết là khung. Tên của gói lớp mạng là gì? Hãy nhớ lại rằng cả bộ định tuyến và bộ chuyển mạch lớp liên kết đều được gọi là bộ chuyển mạch gói. Sự khác biệt cơ bản giữa bộ định tuyến và bộ chuyển mạch lớp liên kết là gì? R2. Chúng tôi lưu ý rằng chức năng của lớp mạng có thể được chia thành

chức năng mặt phẳng dữ liệu và chức năng mặt phẳng điều khiển. Các chức năng chính của mặt phẳng dữ liệu là gì? Của mặt phẳng điều khiển? R3. Chúng tôi đã phân biệt giữa chức năng chuyển tiếp và chức năng định tuyến.

hoạt động được thực hiện ở lớp mạng. Sự khác biệt chính giữa định tuyến và chuyển tiếp là gì?

R4. Vai trò của bảng chuyển tiếp trong bộ định tuyến là gì? R5. Chúng ta đã nói rằng mô hình dịch vụ của lớp mạng "xác định các đặc điểm của

vận chuyển các gói tin từ đầu đến cuối giữa các máy chủ gửi và nhận." Mô hình dịch vụ của lớp mạng Internet là gì? Mô hình dịch vụ Internet đưa ra những đảm bảo gì liên quan đến việc phân phối các gói dữ liệu từ máy chủ này đến máy chủ khác?

MỤC 4.2 R6. Trong Phần 4.2, chúng ta đã thấy rằng một bộ định tuyến thường bao gồm các cổng đầu vào, cổng đầu ra,

một cơ cấu chuyển mạch và một bộ xử lý định tuyến. Điều nào trong số này được thực hiện trong

BÀI TẬP VÀ CÂU HỎI 365

phần cứng và cái nào được thực hiện trong phần mềm? Tại sao? Quay trở lại khái niệm về mặt phẳng dữ liệu và mặt phẳng điều khiển của lớp mạng, được triển khai trong phần cứng và mặt phẳng điều khiển được triển khai trong phần mềm? Tại sao? R7. Thảo luận tại sao mỗi cổng đầu vào trong bộ định tuyến tốc độ cao lại lưu trữ một bản sao ẩn của

bảng chuyển tiếp. R8. Chuyển tiếp dựa trên điểm đến có nghĩa là gì? Điều này khác với

chuyển tiếp tổng quát (giả sử bạn đã đọc Phần 4.4, cách tiếp cận nào trong hai cách tiếp cận được Mạng do Phần mềm xác định)? R9. Giả sử gói đến khớp với hai hoặc nhiều mục trong địa chỉ của bộ định tuyến

bảng chuyển tiếp. Với chuyển tiếp dựa trên đích truyền thống, bộ định tuyến áp dụng quy tắc nào để xác định quy tắc nào trong số này sẽ được áp dụng để xác định cổng đầu ra mà gói đến sẽ được chuyển sang? R10. Ba loại cơ cấu chuyển mạch được thảo luận trong Phần 4.2. Liệt kê và tóm tắt

tả từng loại. Cái nào, nếu có, có thể gửi song song nhiều gói trên vải? R11. Mô tả việc mất gói có thể xảy ra như thế nào tại các cổng đầu vào. Mô tả cách mất gói

tại các cổng đầu vào có thể được loại bỏ (không cần sử dụng bộ đệm vô hạn). R12. Mô tả việc mất gói có thể xảy ra như thế nào tại các cổng đầu ra. Sự mất mát này có thể xảy ra trước

thông hơi bằng cách tăng tốc độ vải chuyển mạch? R13. Chặn HOL là gì? Nó xảy ra ở cổng đầu vào hay cổng đầu ra? R14. Trong Phần 4.2, chúng ta đã nghiên cứu FIFO, Ưu tiên, Round Robin (RR) và Weighted

Nguyên tắc lập lịch gói hàng xếp hàng công bằng (WFQ)? Nguyên tắc xếp hàng nào đảm bảo rằng tất cả các gói khởi hành theo đúng thứ tự chúng đến? R15. Hãy đưa ra một ví dụ cho thấy tại sao một nhà điều hành mạng có thể muốn một lớp

các gói được ưu tiên hơn các loại gói khác. R16. Sự khác biệt cơ bản giữa lập lịch gói RR và WFQ là gì? Là

có trường hợp nào (Gợi ý: Xem xét trọng số WFQ) trong đó RR và WFQ sẽ hoạt động giống hệt nhau?

MỤC 4.3 R17. Giả sử Host A gửi Host B a TCP phân đoạn được gói gọn trong dữ liệu IP-

gram. Khi Host B nhận được datagram, làm thế nào lớp mạng trong Host B biết nó nên chuyển phân đoạn (tức là tải trọng của datagram) tới TCP thay vì tới UDP hoặc tới một số giao thức lớp trên khác? R18. Trường nào trong tiêu đề IP có thể được sử dụng để đảm bảo rằng gói được chuyển tiếp

thông qua không quá N bộ định tuyến? R19. Hãy nhớ lại rằng chúng ta đã thấy tổng kiểm tra Internet được sử dụng trong cả hai lớp vận chuyển

phân đoạn (trong tiêu đề UDP và TCP, Hình 3.7 và 3.29 tương ứng) và trong các gói dữ liệu lớp mạng (tiêu đề IP, Hình 4.17). Bây giờ hãy xem xét một phương tiện giao thông

phân đoạn lớp được gói gọn trong gói dữ liệu IP. Tổng kiểm tra trong tiêu đề phân đoạn và tiêu đề gói dữ liệu có được tính toán trên bất kỳ byte chung nào trong gói dữ liệu IP không? Giải thích câu trả lời của bạn. R20. Khi một datagram lớn bị phân mảnh thành nhiều datagram nhỏ hơn, trong đó

những datagram nhỏ hơn này có được tập hợp lại thành một datagram lớn hơn không? R21. Bộ định tuyến có địa chỉ IP không? Nếu vậy thì bao nhiêu? R22. Hệ nhị phân 32 bit tương đương với địa chỉ IP 223.1.3.27 là gì? R23. Truy cập máy chủ sử dụng DHCP để lấy địa chỉ IP, mặt nạ mạng, mặc định của nó

bộ định tuyến và địa chỉ IP của máy chủ DNS cục bộ của nó. Liệt kê các giá trị này. R24. Giả sử có ba bộ định tuyến giữa máy chủ nguồn và máy chủ đích.

Bỏ qua sự phân mảnh, một datagram IP được gửi từ máy chủ nguồn đến máy chủ đích sẽ di chuyển qua bao nhiêu giao diện? Có bao nhiêu bảng chuyển tiếp sẽ được lập chỉ mục để di chuyển datagram từ nguồn đến đích? R25. Giả sử một ứng dụng tạo ra các khối 40 byte dữ liệu cứ sau 20 mili giây,

và mỗi đoạn được gói gọn trong một phân đoạn TCP và sau đó là một datagram IP. Bao nhiêu phần trăm của mỗi datagram sẽ là chi phí chung và bao nhiêu phần trăm sẽ là dữ liệu ứng dụng? R26. Giả sử bạn mua một bộ định tuyến không dây và kết nối nó với modem cáp.

Ngoài ra, giả sử rằng ISP của bạn tự động gán cho thiết bị được kết nối của bạn (tức là bộ định tuyến không dây của bạn) một địa chỉ IP. Ngoài ra, giả sử rằng bạn có năm PC ở nhà sử dụng 802.11 để kết nối không dây với bộ định tuyến không dây. Địa chỉ IP được gán cho năm PC như thế nào? Bộ định tuyến không dây có sử dụng NAT không? Tại sao hoặc tại sao không? R27. Thuật ngữ \"tập hợp tuyến đường\" có nghĩa là gì? Tại sao nó hữu ích cho bộ định tuyến

để thực hiện tổng hợp tuyến đường? R28. Giao thức "plug-and-play" hoặc "zeroconf" nghĩa là gì? R29. Địa chỉ mạng riêng là gì? Nên sử dụng datagram với mạng riêng

địa chỉ có bao giờ hiện diện trên Internet công cộng lớn hơn không? Giải thích. R30. So sánh và đối chiếu trường tiêu đề IPv4 và IPv6. Họ có cái nào không

lĩnh vực chung? R31. Người ta nói rằng khi IPv6 chuyển qua IPv4 bộ định tuyến, IPv6 sẽ xử lý

IPv4 đường hầm làm giao thức lớp liên kết. Bạn có đồng ý với tuyên bố này? Tại sao hoặc tại sao không?

MỤC 4.4 R32. Chuyển tiếp tổng quát khác với chuyển tiếp dựa trên điểm đến như thế nào? R33. Sự khác biệt giữa bảng chuyển tiếp mà chúng tôi gặp phải trong

chuyển tiếp dựa trên đích trong Phần 4.1 và bảng quy trình của OpenFlow mà chúng tôi đã gặp trong Phần 4.4?

VẤN ĐỀ 367

R34. Hoạt động "kết hợp với hành động" của bộ định tuyến hoặc bộ chuyển mạch có nghĩa là gì? TRONG

trong trường hợp chuyển tiếp gói dựa trên đích, cái gì phù hợp và hành động được thực hiện là gì? Trong trường hợp SDN, hãy đặt tên cho ba trường có thể khớp và ba hành động có thể thực hiện. R35. Kể tên ba trường tiêu đề trong gói dữ liệu IP có thể được "khớp" trong Open-

Chuyển tiếp tổng quát luồng 1.0. Ba trường tiêu đề gói dữ liệu IP không thể \"khớp\" trong OpenFlow là gì?

**Vấn đề**

P1. Hãy xem xét mạng dưới đây.

Một. Hiển thị bảng chuyển tiếp trong bộ định tuyến A, sao cho tất cả lưu lượng truy cập được gửi đến máy chủ

H3 được chuyển tiếp qua giao diện 3. b. Bạn có thể viết ra một bảng chuyển tiếp trong bộ định tuyến A sao cho tất cả lưu lượng truy cập

từ H1 đến máy chủ H3 được chuyển tiếp qua giao diện 3, trong khi tất cả lưu lượng truy cập từ H2 đến máy chủ H3 được chuyển tiếp qua giao diện 4? (Gợi ý: Đây là một câu hỏi mẹo.)

B

MỘT

D

H3

H1

H2

C

P2. Giả sử hai gói đến hai cổng đầu vào khác nhau của bộ định tuyến một cách chính xác

cùng một lúc. Ngoài ra, giả sử không có gói nào khác ở bất kỳ đâu trong bộ định tuyến. Một. Giả sử hai gói được chuyển tiếp đến hai cổng đầu ra khác nhau.

Có thể chuyển tiếp hai gói thông qua kết cấu chuyển mạch cùng lúc khi kết cấu sử dụng xe buýt dùng chung không? b. Giả sử hai gói được chuyển tiếp đến hai cổng đầu ra khác nhau.

Có thể chuyển tiếp hai gói thông qua kết cấu chuyển mạch cùng lúc khi kết cấu sử dụng chuyển mạch qua bộ nhớ không? c. Giả sử hai gói được chuyển tiếp đến cùng một cổng đầu ra. Có phải không?

Có thể chuyển tiếp hai gói thông qua kết cấu chuyển mạch cùng lúc khi kết cấu sử dụng thanh ngang không?

P3. Trong Phần 4.2.4, người ta nói rằng nếu R_switch nhanh hơn R_line N lần,

khi đó chỉ xảy ra việc xếp hàng không đáng kể ở các cổng đầu vào, ngay cả khi tất cả các gói được chuyển tiếp đến cùng một cổng đầu ra. Bây giờ giả sử R_switch = R_line, nhưng tất cả các gói sẽ được chuyển tiếp đến các cổng đầu ra khác nhau. Gọi D là thời gian để truyền gói tin. Là một hàm của D, độ trễ xếp hàng đầu vào tối đa cho một gói đối với (a) bộ nhớ, (b) bus và (c) kết cấu chuyển mạch thanh ngang là bao nhiêu? P4. Hãy xem xét công tắc được hiển thị bên dưới. Giả sử rằng tất cả các datagram đều có cùng

có độ dài cố định, bộ chuyển mạch hoạt động theo kiểu phân khe, đồng bộ và trong một khe thời gian, một datagram có thể được truyền từ cổng đầu vào sang cổng đầu ra. Cơ cấu chuyển mạch là một thanh ngang sao cho nhiều nhất một datagram có thể được chuyển đến một cổng đầu ra nhất định trong một khe thời gian, nhưng các cổng đầu ra khác nhau có thể nhận datagram từ các cổng đầu vào khác nhau trong một khe thời gian. Số lượng khe thời gian tối thiểu cần thiết để chuyển các gói được hiển thị từ cổng đầu vào sang cổng đầu ra của chúng là bao nhiêu, giả sử bất kỳ thứ tự lập lịch hàng đợi đầu vào nào bạn muốn (tức là nó không cần phải có chặn HOL)? Số lượng vị trí lớn nhất cần thiết là bao nhiêu, giả sử thứ tự lập kế hoạch trong trường hợp xấu nhất mà bạn có thể nghĩ ra, giả sử rằng hàng đợi đầu vào không trống không bao giờ nhàn rỗi?

X Y Switch

vải vóc

Cổng đầu ra X

Cổng đầu ra Y

Cổng đầu ra Z

X

YZ

P5. Giả sử rằng chính sách lập lịch WEQ được áp dụng cho bộ đệm hỗ trợ

ba lớp và giả sử các trọng số là 0,5, 0,25 và 0,25 cho ba lớp.

Một. Giả sử mỗi lớp có một số lượng lớn các gói tin trong bộ đệm.

Ba lớp này có thể được phục vụ theo trình tự nào để đạt được trọng số WFQ? (Đối với lập lịch quay vòng, trình tự tự nhiên là 123123123. . .). b. Giả sử lớp 1 và 2 có số lượng lớn gói trong bộ đệm,

và không có gói lớp 3 nào trong bộ đệm. Ba lớp này có thể được phân phát theo trình tự nào để đạt được trọng số WFQ?

VẤN ĐỀ 369

P6. Hãy xem xét hình dưới đây. Trả lời các câu hỏi sau:

Thời gian

Lượt đến

Khởi hành

Packet đang phục vụ

Thời gian

t = 0 t = 2 t = 4 t = 6 t = 8 t = 10 t = 12 t = 14

Một. Giả sử dịch vụ FIFO, chỉ ra thời điểm các gói từ gói 2 đến gói

12 người rời khỏi hàng đợi. Đối với mỗi gói, độ trễ giữa thời điểm nó đến và thời điểm bắt đầu của khe mà nó được truyền là bao nhiêu? Độ trễ trung bình này trên tất cả 12 gói là bao nhiêu? b. Bây giờ giả sử một dịch vụ ưu tiên và giả sử rằng các gói số lẻ

có mức độ ưu tiên cao và các gói được đánh số chẵn có mức độ ưu tiên thấp. Chỉ ra thời điểm các gói từ 2 đến 12 rời khỏi hàng đợi. Đối với mỗi gói, độ trễ giữa thời điểm nó đến và thời điểm bắt đầu của khe mà nó được truyền là bao nhiêu? Độ trễ trung bình này trên tất cả 12 gói là bao nhiêu? c. Bây giờ giả sử dịch vụ quay vòng. Giả sử rằng các gói 1, 2, 3, 6, 11 và

12 là từ lớp 1 và các gói 4, 5, 7, 8, 9 và 10 là từ lớp 2. Chỉ ra thời điểm các gói từ 2 đến 12 rời khỏi hàng đợi. Đối với mỗi gói, độ trễ giữa lúc nó đến và lúc nó rời đi là bao nhiêu? Độ trễ trung bình trên tất cả 12 gói là bao nhiêu? d. Bây giờ giả sử dịch vụ xếp hàng công bằng có trọng số (WFQ). Giả sử kỳ lạ-

các gói được đánh số là từ lớp 1 và các gói được đánh số chẵn là từ lớp 2. Lớp 1 có trọng số WFQ là 2, trong khi lớp 2 có trọng số WFQ là 1. Lưu ý rằng có thể không đạt được lịch trình WFQ lý tưởng hóa như được mô tả trong văn bản, vì vậy hãy cho biết lý do tại sao bạn chọn gói cụ thể để đưa vào sử dụng tại mỗi khe thời gian. Đối với mỗi gói, độ trễ giữa lúc nó đến và lúc nó đi là bao nhiêu? Độ trễ trung bình trên tất cả 12 gói là bao nhiêu? đ. Bạn nhận thấy điều gì về độ trễ trung bình trong cả bốn trường hợp (FIFO, RR,

mức độ ưu tiên và WFQ)?

P7. Hãy xem xét lại con số của P6.

Một. Giả sử một dịch vụ ưu tiên, với các gói 1, 4, 5, 6 và 11 có mức độ ưu tiên cao.

các gói ưu tiên. Các gói còn lại có mức độ ưu tiên thấp. Chỉ ra các vị trí trong đó các gói từ 2 đến 12 rời khỏi hàng đợi. b. Bây giờ giả sử rằng dịch vụ round robin được sử dụng với các gói 1, 4, 5, 6 và

11 gói thuộc một loại lưu lượng và các gói còn lại thuộc loại lưu lượng thứ hai. Chỉ ra các vị trí trong đó các gói từ 2 đến 12 rời khỏi hàng đợi. c. Bây giờ giả sử dịch vụ WFQ được sử dụng với các gói 1, 4, 5, 6 và 11

thuộc một loại lưu lượng và các gói còn lại thuộc loại lưu lượng thứ hai. Loại 1 có trọng số WFQ là 1, trong khi loại 2 có trọng số WFQ là 2 (lưu ý rằng các trọng số này khác với câu hỏi trước). Chỉ ra các vị trí trong đó các gói từ 2 đến 12 rời khỏi hàng đợi. Xem thêm cảnh báo trong câu hỏi trên về dịch vụ WFQ. P8. Hãy xem xét một mạng datagram sử dụng địa chỉ máy chủ 32 bit. Giả sử một bộ định tuyến

có bốn liên kết, được đánh số từ 0 đến 3 và các gói sẽ được chuyển tiếp đến các giao diện liên kết như sau:

Giao diện liên kết phạm vi địa chỉ đích

11100000 00000000 00000000 00000000 đến 11100000 00111111 11111111 11111111

11100000 01000000 00000000 00000000 đến 11100000 01000000 11111111 11111111

11100000 01000001 00000000 00000000 đến 11100001 01111111 11111111 11111111

nếu không thì

Một. Cung cấp bảng chuyển tiếp có năm mục, sử dụng kết hợp tiền tố dài nhất-

ing và chuyển tiếp các gói đến các giao diện liên kết chính xác. b. Mô tả cách bảng chuyển tiếp của bạn xác định liên kết thích hợp

khuôn mặt cho các datagram có địa chỉ đích:

11001000 10010001 01010001 01010101 11100001 01000000 11000011 00111100 11100001 10000000 00010001 01110111

VẤN ĐỀ 371

P9. Hãy xem xét một mạng datagram sử dụng địa chỉ máy chủ 8 bit. Giả sử một bộ định tuyến

sử dụng kết hợp tiền tố dài nhất và có bảng chuyển tiếp sau:

Giao diện khớp tiền tố

Đối với mỗi giao diện trong số bốn giao diện, hãy cung cấp phạm vi liên quan của máy chủ đích

địa chỉ và số lượng địa chỉ trong phạm vi. P10. Hãy xem xét một mạng datagram sử dụng địa chỉ máy chủ 8 bit. Giả sử một bộ định tuyến

sử dụng kết hợp tiền tố dài nhất và có bảng chuyển tiếp sau:

Giao diện khớp tiền tố

nếu không thì

Đối với mỗi giao diện trong số bốn giao diện, hãy cung cấp phạm vi liên quan của máy chủ đích

địa chỉ và số lượng địa chỉ trong phạm vi. P11. Hãy xem xét một bộ định tuyến kết nối ba mạng con: Subnet 1, Subnet 2,

và Subnet 3. Giả sử tất cả các giao diện trong mỗi mạng con trong số ba mạng con này đều bắt buộc phải có tiền tố 223.1.17/24. Ngoài ra, giả sử rằng Subnet 1 là cần thiết để hỗ trợ ít nhất 60 giao diện, Subnet 2 là hỗ trợ ít nhất 90 giao diện và Subnet 3 là hỗ trợ ít nhất 12 giao diện. Cung cấp ba địa chỉ mạng (có dạng a.b.c.d/x) thỏa mãn các ràng buộc này. P12. Trong Phần 4.2.2, một bảng chuyển tiếp mẫu (sử dụng kết hợp tiền tố dài nhất)

được đưa ra. Viết lại bảng chuyển tiếp này bằng ký hiệu a.b.c.d/x thay vì ký hiệu chuỗi nhị phân. P13. Trong bài toán P8, bạn được yêu cầu cung cấp bảng chuyển tiếp (sử dụng bảng chuyển tiếp dài nhất

khớp tiền tố). Viết lại bảng chuyển tiếp này bằng ký hiệu a.b.c.d/x thay vì ký hiệu chuỗi nhị phân. P14. Hãy xem xét một mạng con có tiền tố 128.119.40.128/26. Hãy cho một ví dụ về một

IP địa chỉ (có dạng xxx.xxx.xxx.xxx) có thể được chỉ định cho mạng này.

Giả sử một ISP sở hữu khối địa chỉ có dạng 128.119.40.64/26. Giả sử nó muốn tạo bốn mạng con từ khối này, với mỗi khối có cùng số lượng địa chỉ IP. Các tiền tố (có dạng a.b.c.d/x) cho bốn mạng con là gì? P15. Hãy xem xét cấu trúc liên kết được hiển thị trong Hình 4.20. Ký hiệu ba mạng con với

máy chủ (bắt đầu theo chiều kim đồng hồ lúc 12:00) là Mạng A, B và C. Biểu thị các mạng con không có máy chủ là Mạng D, E và F. a. Gán địa chỉ mạng cho mỗi mạng trong số sáu mạng con này với các thông số sau:

ràng buộc: Tất cả địa chỉ phải được phân bổ từ 214.97.254/23; Subnet A phải có đủ địa chỉ để hỗ trợ 250 giao diện; Subnet B phải có đủ địa chỉ để hỗ trợ 120 giao diện; và Subnet C phải có đủ địa chỉ để hỗ trợ 120 giao diện. Tất nhiên, mỗi mạng con D, E và F sẽ có thể hỗ trợ hai giao diện. Đối với mỗi mạng con, phép gán phải có dạng a.b.c.d/x hoặc a.b.c.d/x -- e.f.g.h/y. b. Sử dụng câu trả lời của bạn cho phần (a), hãy cung cấp các bảng chuyển tiếp (sử dụng long-

est khớp tiền tố) cho mỗi bộ định tuyến trong số ba bộ định tuyến. P16. Sử dụng dịch vụ whois tại Cơ quan đăng ký số Internet Hoa Kỳ

(http://www.arin.net/whois) để xác định khối địa chỉ IP cho ba trường đại học. Dịch vụ whois có thể được sử dụng để xác định chắc chắn vị trí địa lý của một địa chỉ IP cụ thể không? Sử dụng www.maxmind.com để xác định vị trí của các máy chủ Web tại mỗi trường đại học này. P17. Giả sử các datagram được giới hạn ở 1.500 byte (bao gồm cả tiêu đề) giữa

nguồn Host A và đích Host B. Giả sử tiêu đề IP 20 byte, cần bao nhiêu datagram để gửi một bản MP3 gồm 5 triệu byte? Giải thích cách bạn tính toán câu trả lời của bạn. P18. Hãy xem xét việc thiết lập mạng trong Hình 4.25. Giả sử rằng ISP thay vào đó

gán cho bộ định tuyến địa chỉ 24.34.112.235 và địa chỉ mạng của mạng gia đình là 192.168.1/24. Một. Gán địa chỉ cho tất cả các giao diện trong mạng gia đình. b. Giả sử mỗi máy chủ có hai kết nối TCP đang diễn ra, tất cả đều tới cổng 80 tại

máy chủ 128.119.40.86. Cung cấp sáu mục tương ứng trong bảng dịch NAT. P19. Giả sử bạn quan tâm đến việc phát hiện số lượng máy chủ đằng sau NAT.

Bạn quan sát thấy lớp IP đóng dấu số nhận dạng một cách tuần tự trên mỗi gói IP. Số nhận dạng của gói IP đầu tiên do máy chủ tạo ra là số ngẫu nhiên và số nhận dạng của gói IP tiếp theo được gán tuần tự. Giả sử tất cả các gói IP được tạo bởi các máy chủ phía sau NAT đều được gửi ra thế giới bên ngoài. Một. Dựa trên quan sát này và giả sử bạn có thể đánh hơi được tất cả các gói được gửi bởi

NAT ở bên ngoài, bạn có thể phác thảo một kỹ thuật đơn giản để phát hiện số lượng máy chủ duy nhất đằng sau NAT không? Biện minh cho câu trả lời của bạn.

VẤN ĐỀ 373

b\. Nếu số nhận dạng không được gán tuần tự mà ngẫu nhiên

được giao, kỹ thuật của bạn có hiệu quả không? Biện minh cho câu trả lời của bạn. P20. Trong bài toán này, chúng ta sẽ tìm hiểu tác động của NAT lên các ứng dụng P2P.

Giả sử một người ngang hàng có tên người dùng Arnold phát hiện ra thông qua truy vấn rằng một người ngang hàng có tên người dùng Bernard có một tệp mà nó muốn tải xuống. Ngoài ra, giả sử rằng Bernard và Arnold đều đứng sau NAT. Cố gắng nghĩ ra một kỹ thuật cho phép Arnold thiết lập kết nối TCP với Bernard mà không cần cấu hình NAT dành riêng cho ứng dụng. Nếu bạn gặp khó khăn khi nghĩ ra một kỹ thuật như vậy, hãy thảo luận lý do tại sao. P21. Hãy xem xét mạng SDN OpenFlow được hiển thị trong Hình 4.30. Giả định

rằng hành vi chuyển tiếp mong muốn đối với các gói dữ liệu đến s2 như sau: • bất kỳ gói dữ liệu nào đến cổng đầu vào 1 từ các máy chủ h5 hoặc h6 được dành cho các máy chủ h1 hoặc h2 nên được chuyển tiếp qua cổng đầu ra 2; • bất kỳ gói dữ liệu nào đến cổng đầu vào 2 từ máy chủ h1 hoặc h2 được gửi đến máy chủ h5 hoặc h6 phải được chuyển tiếp qua cổng đầu ra 1; • bất kỳ gói dữ liệu nào đến trên cổng đầu vào 1 hoặc 2 và được gửi đến máy chủ h3 hoặc h4 phải được gửi đến máy chủ được chỉ định; • Máy chủ h3 và h4 có thể gửi datagram cho nhau. Chỉ định các mục trong bảng quy trình trong s2 thực hiện hành vi chuyển tiếp này. P22. Hãy xem xét lại mạng SDN OpenFlow được hiển thị trong Hình 4.30. Giả định

rằng hành vi chuyển tiếp mong muốn đối với các gói dữ liệu đến từ máy chủ h3 hoặc h4 tại s2 như sau: • mọi gói dữ liệu đến từ máy chủ h3 và có đích đến là h1, h2, h5 hoặc h6 phải được chuyển tiếp theo chiều kim đồng hồ trong mạng; • bất kỳ gói dữ liệu nào đến từ máy chủ h4 và được gửi đến h1, h2, h5 hoặc h6 phải được chuyển tiếp theo hướng ngược chiều kim đồng hồ trong mạng. Chỉ định các mục trong bảng quy trình trong s2 thực hiện hành vi chuyển tiếp này. P23. Hãy xem xét lại kịch bản từ P21 ở trên. Cung cấp các mục trong bảng quy trình tại

chuyển mạch gói s1 và s3, sao cho mọi gói dữ liệu đến có địa chỉ nguồn là h3 hoặc h4 đều được định tuyến đến máy chủ đích được chỉ định trong trường địa chỉ đích trong gói dữ liệu IP. (Gợi ý: Các quy tắc bảng chuyển tiếp của bạn nên bao gồm các trường hợp một datagram đến được dành cho một máy chủ được gắn trực tiếp hoặc nên được chuyển tiếp đến một bộ định tuyến lân cận để phân phối máy chủ cuối cùng ở đó.) P24. Hãy xem xét lại mạng SDN OpenFlow được hiển thị trong Hình 4.30. Giả định

chúng tôi muốn switch s2 hoạt động như một tường lửa. Chỉ định bảng luồng trong s2 thực hiện các hành vi tường lửa sau (chỉ định một bảng luồng khác nhau cho mỗi trong số bốn hành vi tường lửa bên dưới) để phân phối các gói dữ liệu

định mệnh là h3 và h4. Bạn không cần chỉ định hành vi chuyển tiếp trong s2 để chuyển tiếp lưu lượng truy cập đến các bộ định tuyến khác. • Chỉ lưu lượng truy cập đến từ máy chủ h1 và h6 mới được gửi đến máy chủ h3 hoặc h4 (tức là lưu lượng truy cập đến từ máy chủ h2 và h5 sẽ bị chặn). • Chỉ cho phép lưu lượng truy cập TCP được gửi tới máy chủ h3 hoặc h4 (tức là lưu lượng truy cập UDP đó bị chặn). • Chỉ lưu lượng truy cập đến h3 mới được phân phối (tức là tất cả lưu lượng truy cập đến h4 đều bị chặn). • Chỉ UDP lưu lượng truy cập từ h1 và đích đến h3 mới được phân phối. Tất cả các lưu lượng truy cập khác đều bị chặn. P25. Hãy xem xét ngăn xếp giao thức Internet trong Hình 1.23 và 4.31. Bạn có muốn

coi giao thức ICMP là giao thức lớp mạng hay giao thức lớp vận chuyển? Biện minh cho câu trả lời của bạn.

**Wireshark Phòng thí nghiệm: IP**

Trong trang Web của cuốn sách giáo khoa này, www.pearsonhighered.com/cs-resources, bạn sẽ tìm thấy một bài tập thực hành Wireshark kiểm tra hoạt động của giao thức IP và đặc biệt là định dạng gói dữ liệu IP.

Điều gì đã đưa bạn đến với chuyên ngành mạng?

Tôi đang làm lập trình viên tại UCLA vào cuối những năm 1960. Công việc của tôi được hỗ trợ bởi Cơ quan Dự án Nghiên cứu Tiên tiến Quốc phòng Hoa Kỳ (lúc đó gọi là ARPA và bây giờ là DARPA). Tôi đang làm việc trong phòng thí nghiệm của Giáo sư Leonard Kleinrock tại Trung tâm Đo lường Mạng của ARPANet mới được thành lập. Nút đầu tiên của ARPANet được cài đặt tại UCLA vào ngày 1 tháng 9 năm 1969. Tôi chịu trách nhiệm lập trình một máy tính được sử dụng để nắm bắt thông tin hiệu suất về ARPANet và báo cáo lại thông tin này để so sánh với các mô hình toán học và dự đoán về hiệu suất của mạng.

Tôi và một số sinh viên tốt nghiệp khác được giao trách nhiệm làm việc trên cái gọi là giao thức cấp máy chủ của ARPAnet - các quy trình và định dạng cho phép nhiều loại máy tính khác nhau trên mạng tương tác với nhau. Đó là một cuộc khám phá hấp dẫn về một thế giới mới (đối với tôi) về điện toán và truyền thông phân tán.

Bạn có tưởng tượng rằng IP sẽ trở nên phổ biến như ngày nay khi bạn thiết kế giao thức lần đầu tiên không?

Khi Bob Kahn và tôi lần đầu tiên làm việc về vấn đề này vào năm 1973, tôi nghĩ chúng tôi chủ yếu tập trung vào câu hỏi trọng tâm: Làm thế nào chúng ta có thể khiến các mạng gói không đồng nhất tương tác với nhau, giả sử rằng chúng ta thực sự không thể tự thay đổi các mạng đó? Chúng tôi hy vọng rằng chúng tôi có thể tìm ra cách cho phép một tập hợp tùy ý các mạng chuyển mạch gói được kết nối với nhau theo cách minh bạch, để các máy chủ có thể giao tiếp từ đầu đến cuối mà không cần phải thực hiện bất kỳ bản dịch nào ở giữa. Tôi nghĩ chúng ta biết rằng chúng ta đang giải quyết

Vinton G. Cerf đã giữ chức Phó Chủ tịch kiêm Giám đốc Truyền bá Internet của Google từ năm 2005. Ông đã phục vụ hơn 15 năm tại MCI ở nhiều vị trí khác nhau, kết thúc nhiệm kỳ của mình ở đó với tư cách là Phó Chủ tịch Cấp cao về Chiến lược Công nghệ. Ông được biết đến rộng rãi với tư cách là người đồng thiết kế các giao thức TCP/IP và kiến ​​trúc của Internet. Trong thời gian từ 1976 đến 1982 tại Cơ quan Dự án Nghiên cứu Tiên tiến của Bộ Quốc phòng Hoa Kỳ (DARPA), ông đóng vai trò chủ chốt dẫn dắt sự phát triển của Internet và các kỹ thuật bảo mật và truyền thông gói liên quan đến Internet. Ông nhận Huân chương Tự do của Tổng thống Hoa Kỳ năm 2005 và Huân chương Công nghệ Quốc gia Hoa Kỳ năm 1997. Ông có bằng Cử nhân Toán học tại Đại học Stanford và bằng Thạc sĩ và Tiến sĩ về khoa học máy tính tại UCLA.

**Vinton G. Cerf**

PHỎNG VẤN VỚI...

Được phép của Vinton G. Cerf

![](media/image3.png){width="5.5in" height="7.071428258967629in"}

với công nghệ mạnh mẽ và có thể mở rộng, nhưng tôi nghi ngờ rằng chúng ta không có một hình ảnh rõ ràng về thế giới sẽ như thế nào với hàng tỷ máy tính được kết nối với nhau trên Internet.

Bây giờ bạn hình dung điều gì về tương lai của mạng và Internet? Bạn nghĩ những thách thức/trở ngại lớn nào đang ở phía trước trong quá trình phát triển của họ?

Tôi tin rằng bản thân Internet và các mạng nói chung sẽ tiếp tục phát triển. Hiện đã có hàng tỷ thiết bị hỗ trợ Internet trên Internet, bao gồm các thiết bị như điện thoại di động, tủ lạnh, thiết bị trợ giúp kỹ thuật số cá nhân, máy chủ gia đình, tivi, cũng như các loại máy tính xách tay, máy chủ thông thường, v.v. Những thách thức lớn bao gồm hỗ trợ về tính di động, thời lượng pin, dung lượng của các liên kết truy cập vào mạng và khả năng mở rộng lõi quang của mạng một cách không giới hạn. Việc mở rộng Internet liên hành tinh là một dự án đang được tiến hành tốt tại NASA và các cơ quan không gian khác. Chúng tôi vẫn cần thêm địa chỉ IPv6 \[128bit\] vào định dạng gói IPv4 \[địa chỉ 32 bit\] ban đầu. Danh sách còn dài!

Ai đã truyền cảm hứng cho bạn một cách chuyên nghiệp?

Đồng nghiệp của tôi Bob Kahn; cố vấn luận án của tôi, Gerald Estrin; người bạn thân nhất của tôi, Steve Crocker (chúng tôi gặp nhau ở trường trung học và anh ấy đã giới thiệu cho tôi máy tính vào năm 1960!); và hàng nghìn kỹ sư đang tiếp tục phát triển Internet ngày nay.

Bạn có lời khuyên nào dành cho các sinh viên đang theo học lĩnh vực mạng/Internet không?

Hãy suy nghĩ bên ngoài những hạn chế của các hệ thống hiện có---hãy tưởng tượng những gì có thể xảy ra; nhưng sau đó hãy nỗ lực tìm ra cách đạt được điều đó từ tình trạng hiện tại. Dám ước mơ. "Internet of Things" là giai đoạn lớn tiếp theo của việc mở rộng Internet. An toàn, bảo mật, quyền riêng tư, độ tin cậy và quyền tự chủ đều cần được chú ý. Việc mở rộng liên hành tinh của Internet trên mặt đất bắt đầu như một thiết kế mang tính suy đoán nhưng đang trở thành hiện thực. Có thể phải mất hàng thập kỷ để thực hiện điều này, hết sứ mệnh này đến sứ mệnh khác, nhưng có thể diễn giải: "Tầm với của một người phải vượt quá tầm với của anh ta, hay thiên đường để làm gì?"

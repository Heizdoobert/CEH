**Chương 6: Tầng Liên Kết Dữ Liệu và Mạng LAN (Link Layer and LANs)**

Trong hai chương trước, chúng ta đã biết rằng lớp mạng cung cấp dịch vụ liên lạc giữa hai máy chủ mạng bất kỳ. Giữa hai máy chủ, các gói dữ liệu di chuyển qua một loạt các liên kết truyền thông, một số có dây và một số không dây, bắt đầu từ máy chủ nguồn, đi qua một loạt các bộ chuyển mạch gói (bộ chuyển mạch và bộ định tuyến) và kết thúc tại máy chủ đích. Khi chúng ta tiếp tục đi xuống ngăn xếp giao thức, từ lớp mạng đến lớp liên kết, chúng ta tự nhiên thắc mắc làm thế nào các gói được gửi qua các liên kết riêng lẻ tạo nên đường dẫn liên lạc hai đầu. Các datagram lớp mạng được gói gọn trong các khung lớp liên kết như thế nào để truyền qua một liên kết đơn? Các giao thức lớp liên kết khác nhau có được sử dụng trong các liên kết khác nhau dọc theo đường truyền thông không? Xung đột truyền tải trong các liên kết quảng bá được giải quyết như thế nào? Có địa chỉ ở lớp liên kết không và nếu có thì địa chỉ của lớp liên kết hoạt động như thế nào với địa chỉ của lớp mạng mà chúng ta đã học ở Chương 4? Và chính xác thì sự khác biệt giữa switch và router là gì? Chúng ta sẽ trả lời những câu hỏi này và những câu hỏi quan trọng khác trong chương này.

Khi thảo luận về lớp liên kết, chúng ta sẽ thấy rằng có hai loại kênh lớp liên kết cơ bản khác nhau. Loại đầu tiên là các kênh quảng bá, kết nối nhiều máy chủ trong mạng LAN không dây, trong mạng vệ tinh và trong mạng truy cập cáp đồng trục lai (HFC). Vì nhiều máy chủ được kết nối với cùng một kênh liên lạc quảng bá nên cần có cái gọi là giao thức truy cập trung bình để điều phối việc truyền khung. Trong một số trường hợp, bộ điều khiển trung tâm có thể được sử dụng để phối hợp

**Link Layer và mạng LAN**

**CHƯƠNG**

![](media/image1.png){width="5.5in" height="6.930965660542432in"}

![](media/image2.png){width="5.5in" height="0.9567311898512686in"}

truyền động; trong các trường hợp khác, các máy chủ tự điều phối việc truyền tải. Loại kênh lớp liên kết thứ hai là liên kết truyền thông điểm-điểm, chẳng hạn như liên kết thường thấy giữa hai bộ định tuyến được kết nối bằng liên kết đường dài hoặc giữa máy tính văn phòng của người dùng và bộ chuyển mạch Ethernet gần đó mà nó được kết nối. Việc phối hợp truy cập vào liên kết điểm-điểm đơn giản hơn; Tài liệu tham khảo trên trang Web của cuốn sách này thảo luận chi tiết về Giao thức điểm-điểm (PPP), được sử dụng trong các cài đặt khác nhau, từ dịch vụ quay số qua đường dây điện thoại đến truyền tải khung hình điểm-điểm tốc độ cao qua các liên kết cáp quang.

Chúng ta sẽ khám phá một số khái niệm và công nghệ lớp liên kết quan trọng trong chương này. Chúng ta sẽ đi sâu hơn vào việc phát hiện và sửa lỗi, một chủ đề mà chúng ta đã đề cập ngắn gọn trong Chương 3. Chúng ta sẽ xem xét các mạng đa truy cập và mạng LAN chuyển mạch, bao gồm cả Ethernet---cho đến nay là công nghệ mạng LAN có dây phổ biến nhất. Chúng ta cũng sẽ xem xét mạng LAN ảo và mạng trung tâm dữ liệu. Mặc dù WiFi và mạng LAN không dây nói chung là các chủ đề ở lớp liên kết nhưng chúng ta sẽ trì hoãn việc nghiên cứu những chủ đề quan trọng này cho đến Chương 7.

**6.1 Giới thiệu về Link Layer**

Hãy bắt đầu với một số thuật ngữ quan trọng. Trong chương này, chúng ta sẽ thấy thuận tiện khi đề cập đến bất kỳ thiết bị nào chạy giao thức lớp liên kết (tức là lớp 2) dưới dạng nút. Các nút bao gồm máy chủ, bộ định tuyến, bộ chuyển mạch và điểm truy cập WiFi (được thảo luận trong Chương 7). Chúng tôi cũng sẽ đề cập đến các kênh liên lạc kết nối các nút lân cận dọc theo đường dẫn liên lạc dưới dạng liên kết. Để một datagram có thể được truyền từ máy chủ nguồn đến máy chủ đích, nó phải được di chuyển qua từng liên kết riêng lẻ trong đường dẫn từ đầu đến cuối. Ví dụ, trong mạng công ty được hiển thị ở cuối Hình 6.1, hãy xem xét việc gửi một datagram từ một trong các máy chủ không dây đến một trong các máy chủ. Datagram này thực sự sẽ đi qua sáu liên kết: một liên kết WiFi giữa máy chủ gửi và điểm truy cập WiFi, một liên kết Ethernet giữa điểm truy cập và bộ chuyển mạch lớp liên kết; một liên kết giữa bộ chuyển mạch lớp liên kết và bộ định tuyến, một liên kết giữa hai bộ định tuyến; một liên kết Ethernet giữa bộ định tuyến và bộ chuyển mạch lớp liên kết; và cuối cùng là liên kết Ethernet giữa switch và máy chủ. Trên một liên kết nhất định, nút truyền sẽ đóng gói datagram trong khung lớp liên kết và truyền khung đó vào liên kết.

Để hiểu rõ hơn về lớp liên kết và cách nó liên quan đến lớp mạng, chúng ta hãy xem xét một sự tương tự về vận chuyển. Hãy xem xét một đại lý du lịch đang lên kế hoạch cho một chuyến đi cho một khách du lịch đi từ Princeton, New Jersey đến Lausanne, Thụy Sĩ. Đại lý du lịch quyết định rằng thuận tiện nhất cho du khách là đi xe limousine từ Princeton đến sân bay JFK, sau đó đi máy bay từ sân bay JFK đến sân bay Geneva, và cuối cùng là đi tàu từ sân bay Geneva đến ga xe lửa Lausanne. Một lần

*Hình 6.1 ♦ Sáu bước nhảy lớp liên kết giữa máy chủ và máy chủ không dây*

đại lý du lịch thực hiện ba lần đặt chỗ trước, công ty xe limousine Princeton có trách nhiệm đưa khách du lịch từ Princeton đến JFK; trách nhiệm của công ty hàng không là đưa khách du lịch từ JFK đến Geneva; và dịch vụ xe lửa Thụy Sĩ có trách nhiệm đưa đón khách du lịch từ Geneva đến Lausanne. Mỗi chặng trong số ba chặng của chuyến đi đều "trực tiếp" giữa hai địa điểm "liền kề". Lưu ý rằng ba phân đoạn vận tải được quản lý bởi các công ty khác nhau và sử dụng hoàn toàn

các phương thức vận chuyển khác nhau (xe limousine, máy bay và tàu hỏa). Mặc dù các phương thức vận chuyển khác nhau nhưng mỗi phương thức đều cung cấp dịch vụ cơ bản là di chuyển hành khách từ địa điểm này đến địa điểm liền kề. Trong sự tương tự về vận chuyển này, khách du lịch là một datagram, mỗi phân đoạn vận chuyển là một liên kết, phương thức vận chuyển là một giao thức lớp liên kết và đại lý du lịch là một giao thức định tuyến.

**6.1.1 Dịch vụ được cung cấp bởi Link Layer**

Mặc dù dịch vụ cơ bản của bất kỳ lớp liên kết nào là di chuyển một datagram từ nút này sang nút lân cận qua một liên kết truyền thông duy nhất, nhưng chi tiết của dịch vụ được cung cấp có thể khác nhau tùy theo giao thức của lớp liên kết này sang giao thức tiếp theo. Các dịch vụ có thể được cung cấp bởi giao thức lớp liên kết bao gồm:

• Đóng khung. Hầu như tất cả các giao thức lớp liên kết đều đóng gói từng datagram lớp mạng trong khung lớp liên kết trước khi truyền qua liên kết. Một khung bao gồm một trường dữ liệu, trong đó datagram lớp mạng được chèn vào và một số trường tiêu đề. Cấu trúc của khung được xác định bởi giao thức lớp liên kết. Chúng ta sẽ thấy một số định dạng khung khác nhau khi xem xét các giao thức lớp liên kết cụ thể trong nửa sau của chương này. • Truy cập liên kết. Giao thức điều khiển truy cập môi trường (MAC) chỉ định các quy tắc theo đó một khung được truyền lên liên kết. Đối với các liên kết điểm-điểm có một người gửi ở một đầu liên kết và một người nhận ở đầu kia của liên kết, giao thức MAC rất đơn giản (hoặc không tồn tại)---người gửi có thể gửi một khung bất cứ khi nào liên kết không hoạt động. Trường hợp thú vị hơn là khi nhiều nút chia sẻ một liên kết quảng bá duy nhất---được gọi là vấn đề đa truy cập. Ở đây, giao thức MAC dùng để điều phối việc truyền khung của nhiều nút. • Giao hàng đáng tin cậy. Khi giao thức lớp liên kết cung cấp dịch vụ phân phối đáng tin cậy, nó đảm bảo di chuyển từng datagram lớp mạng qua liên kết mà không gặp lỗi. Hãy nhớ lại rằng một số giao thức lớp vận chuyển nhất định (chẳng hạn như TCP) cũng cung cấp dịch vụ phân phối đáng tin cậy. Tương tự như dịch vụ phân phối đáng tin cậy của lớp vận chuyển, dịch vụ phân phối đáng tin cậy của lớp liên kết có thể đạt được bằng các báo nhận và truyền lại (xem Phần 3.4). Dịch vụ phân phối đáng tin cậy của lớp liên kết thường được sử dụng cho các liên kết có xu hướng có tỷ lệ lỗi cao, chẳng hạn như liên kết không dây, với mục tiêu sửa lỗi cục bộ---trên liên kết xảy ra lỗi---thay vì buộc truyền lại dữ liệu từ đầu đến cuối bằng giao thức lớp vận chuyển hoặc lớp ứng dụng. Tuy nhiên, việc phân phối đáng tin cậy của lớp liên kết có thể được coi là chi phí không cần thiết đối với các liên kết có lỗi bit thấp, bao gồm cáp quang, cáp đồng trục và nhiều liên kết đồng xoắn đôi. Vì lý do này, nhiều giao thức lớp liên kết có dây không cung cấp dịch vụ phân phối đáng tin cậy. • Phát hiện và sửa lỗi. Phần cứng lớp liên kết trong nút nhận có thể quyết định không chính xác rằng một bit trong khung bằng 0 khi nó được truyền dưới dạng

một và ngược lại. Những lỗi bit như vậy được gây ra bởi sự suy giảm tín hiệu và nhiễu điện từ. Bởi vì không cần phải chuyển tiếp một datagram có lỗi nên nhiều giao thức lớp liên kết cung cấp cơ chế phát hiện các lỗi bit đó. Điều này được thực hiện bằng cách yêu cầu nút truyền bao gồm các bit phát hiện lỗi trong khung và yêu cầu nút nhận thực hiện kiểm tra lỗi. Hãy nhớ lại trong Chương 3 và 4 rằng lớp truyền tải và lớp mạng của Internet cũng cung cấp một dạng phát hiện lỗi có giới hạn---tổng kiểm tra Internet. Việc phát hiện lỗi ở lớp liên kết thường phức tạp hơn và được thực hiện trong phần cứng. Sửa lỗi tương tự như phát hiện lỗi, ngoại trừ việc bộ thu không chỉ phát hiện khi nào xảy ra lỗi bit trong khung mà còn xác định chính xác vị trí xảy ra lỗi trong khung (và sau đó sửa các lỗi này).

**6.1.2 Link Layer được triển khai ở đâu?**

Trước khi đi sâu vào nghiên cứu chi tiết về lớp liên kết, chúng ta hãy kết thúc phần giới thiệu này bằng cách xem xét câu hỏi lớp liên kết được triển khai ở đâu. Lớp liên kết của máy chủ được triển khai bằng phần cứng hay phần mềm? Nó có được triển khai trên một thẻ hoặc chip riêng biệt không và nó giao tiếp như thế nào với các thành phần phần cứng và hệ điều hành còn lại của máy chủ?

Hình 6.2 thể hiện một kiến ​​trúc máy chủ điển hình. Khả năng Ethernet được tích hợp vào chipset bo mạch chủ hoặc được triển khai thông qua chip Ethernet chuyên dụng giá rẻ. Phần lớn, lớp liên kết được triển khai trên một con chip gọi là bộ điều hợp mạng, đôi khi còn được gọi là bộ điều khiển giao diện mạng (NIC). Bộ điều hợp mạng triển khai nhiều dịch vụ lớp liên kết bao gồm định khung, truy cập liên kết, phát hiện lỗi, v.v. Do đó, phần lớn chức năng của bộ điều khiển lớp liên kết được triển khai trong phần cứng. Ví dụ: bộ điều hợp dòng 700 của Intel \[Intel 2020\] triển khai các giao thức Ethernet mà chúng ta sẽ nghiên cứu trong Phần 6.5; bộ điều khiển Atheros AR5006 \[Atheros 2020\] triển khai các giao thức WiFi 802.11 mà chúng ta sẽ nghiên cứu trong Chương 7.

Ở phía gửi, bộ điều khiển lấy một datagram đã được tạo và lưu trữ trong bộ nhớ máy chủ bởi các lớp cao hơn của ngăn xếp giao thức, đóng gói datagram đó trong khung lớp liên kết (điền vào các trường khác nhau của khung), sau đó truyền khung vào liên kết truyền thông, theo giao thức truy cập liên kết. Ở phía nhận, bộ điều khiển nhận toàn bộ khung và trích xuất datagram của lớp mạng. Nếu lớp liên kết thực hiện phát hiện lỗi thì bộ điều khiển gửi sẽ thiết lập các bit phát hiện lỗi trong tiêu đề khung và bộ điều khiển nhận sẽ thực hiện phát hiện lỗi.

Hình 6.2 cho thấy rằng trong khi hầu hết lớp liên kết được triển khai trong phần cứng thì một phần của lớp liên kết được triển khai trong phần mềm chạy trên CPU của máy chủ. Các thành phần phần mềm của lớp liên kết thực hiện chức năng lớp liên kết cấp cao hơn như tập hợp thông tin địa chỉ lớp liên kết và kích hoạt

phần cứng điều khiển. Về phía nhận, phần mềm lớp liên kết phản hồi các ngắt của bộ điều khiển (ví dụ, do nhận được một hoặc nhiều khung), xử lý các điều kiện lỗi và truyền một datagram lên lớp mạng. Do đó, lớp liên kết là sự kết hợp giữa phần cứng và phần mềm - vị trí trong ngăn xếp giao thức nơi phần mềm gặp phần cứng. \[Intel 2020\] cung cấp thông tin tổng quan dễ đọc (cũng như mô tả chi tiết) về bộ điều khiển XL710 từ quan điểm lập trình phần mềm.

**6.2 Kỹ thuật phát hiện và sửa lỗi**

Trong phần trước, chúng tôi đã lưu ý rằng việc phát hiện và sửa lỗi cấp độ bit---phát hiện và sửa lỗi sai lệch của các bit trong khung lớp liên kết được gửi từ nút này đến nút lân cận được kết nối vật lý khác---là hai dịch vụ thường được cung cấp bởi lớp liên kết. Chúng ta đã thấy trong Chương 3 rằng các dịch vụ phát hiện và sửa lỗi cũng thường được cung cấp ở lớp vận chuyển. Trong phần này, chúng ta sẽ xem xét một số kỹ thuật đơn giản nhất có thể được sử dụng để phát hiện và, trong một số

*Hình 6.2 ♦ Bộ điều hợp mạng: Mối quan hệ của nó với các thành phần máy chủ khác*

và chức năng ngăn xếp giao thức

Host

Ký ức

Xe buýt bo mạch chủ

CPU

Bộ điều khiển

Truyền dẫn vật lý

Liên kết bộ điều hợp mạng

Thuộc vật chất

Chuyên chở

Mạng

liên kết

Ứng dụng

trường hợp, hãy sửa các lỗi bit đó. Bản thân việc xử lý đầy đủ lý thuyết và cách thực hiện chủ đề này đã là chủ đề của nhiều sách giáo khoa (ví dụ, \[Schwartz 1980\] hoặc \[Bertsekas 1991\]), và cách xử lý của chúng tôi ở đây nhất thiết phải ngắn gọn. Mục tiêu của chúng tôi ở đây là phát triển cảm giác trực quan về khả năng mà các kỹ thuật phát hiện và sửa lỗi cung cấp cũng như xem cách một số kỹ thuật đơn giản hoạt động và được sử dụng trong thực tế trong lớp liên kết.

Hình 6.3 minh họa bối cảnh cho nghiên cứu của chúng tôi. Tại nút gửi, dữ liệu D, được bảo vệ khỏi lỗi bit, được tăng cường bằng các bit phát hiện và sửa lỗi (EDC). Thông thường, dữ liệu cần được bảo vệ không chỉ bao gồm datagram được truyền xuống từ lớp mạng để truyền qua liên kết mà còn bao gồm thông tin địa chỉ cấp liên kết, số thứ tự và các trường khác trong tiêu đề khung liên kết. Cả D và EDC đều được gửi đến nút nhận trong khung cấp liên kết. Tại nút nhận, một chuỗi bit D′ và EDC′ được nhận. Lưu ý rằng D′ và EDC′ có thể khác với D và EDC ban đầu do sự thay đổi bit trong quá trình truyền.

Thử thách của người nhận là xác định xem D′ có giống với D ban đầu hay không, vì nó chỉ nhận được D′ và EDC′. Diễn đạt chính xác về quyết định của người nhận trong Hình 6.3 (chúng tôi hỏi liệu lỗi có được phát hiện hay không, chứ không phải lỗi có xảy ra hay không!) là quan trọng. Các kỹ thuật phát hiện và sửa lỗi cho phép bộ thu đôi khi, nhưng không phải luôn luôn, phát hiện ra rằng các lỗi bit đã xảy ra. Ngay cả khi sử dụng các bit phát hiện lỗi vẫn có thể có các lỗi bit không được phát hiện; nghĩa là người nhận có thể không biết rằng thông tin nhận được có lỗi bit. Như một

*Hình 6.3 ♦ Kịch bản phát hiện và sửa lỗi*

EDC\'D\'

Đã phát hiện lỗi

Datagram

EDC D

d bit dữ liệu

Liên kết dễ bị lỗi bit

tất cả các bit trong D\'

ĐƯỢC RỒI

?

N

Y

Datagram

CHÀO

hậu quả là người nhận có thể phân phối một gói dữ liệu bị hỏng đến lớp mạng hoặc không biết rằng nội dung của một trường trong tiêu đề của khung đã bị hỏng. Do đó, chúng tôi muốn chọn một sơ đồ phát hiện lỗi để giữ xác suất xảy ra những sự cố như vậy ở mức nhỏ. Nói chung, các kỹ thuật phát hiện và sửa lỗi phức tạp hơn (nghĩa là những kỹ thuật có xác suất cho phép lỗi bit không được phát hiện nhỏ hơn) phải chịu chi phí lớn hơn---cần nhiều tính toán hơn để tính toán và truyền số lượng lớn hơn các bit phát hiện và sửa lỗi.

Bây giờ chúng ta hãy xem xét ba kỹ thuật phát hiện lỗi trong dữ liệu được truyền--- kiểm tra tính chẵn lẻ (để minh họa các ý tưởng cơ bản đằng sau việc phát hiện và sửa lỗi), phương pháp tổng kiểm tra (thường được sử dụng nhiều hơn trong lớp vận chuyển) và kiểm tra dự phòng theo chu kỳ (thường được sử dụng nhiều hơn trong lớp liên kết trong bộ chuyển đổi).

**6.2.1 Kiểm tra tính chẵn lẻ**

Có lẽ hình thức phát hiện lỗi đơn giản nhất là sử dụng một bit chẵn lẻ. Giả sử thông tin được gửi đi, D trong Hình 6.4, có d bit. Trong sơ đồ chẵn lẻ, người gửi chỉ cần thêm một bit bổ sung và chọn giá trị của nó sao cho tổng số bit 1 trong d + 1 bit (thông tin gốc cộng với một bit chẵn lẻ) là chẵn. Đối với các sơ đồ chẵn lẻ lẻ, giá trị bit chẵn lẻ được chọn sao cho có số lẻ là 1s. Hình 6.4 minh họa sơ đồ chẵn lẻ, với bit chẵn lẻ duy nhất được lưu trữ trong một trường riêng biệt.

Hoạt động của máy thu cũng đơn giản chỉ với một bit chẵn lẻ. Người nhận chỉ cần đếm số 1 trong các bit d + 1 nhận được. Nếu tìm thấy số lẻ các bit có giá trị 1 với sơ đồ chẵn lẻ, thì máy thu biết rằng đã xảy ra ít nhất một lỗi bit. Chính xác hơn, nó biết rằng một số lỗi bit lẻ đã xảy ra.

Nhưng điều gì sẽ xảy ra nếu xảy ra số lỗi bit chẵn? Bạn nên thuyết phục bản thân rằng điều này sẽ dẫn đến một lỗi không được phát hiện. Nếu xác suất xảy ra lỗi bit nhỏ và các lỗi có thể được coi là xảy ra độc lập từ bit này sang bit khác thì xác suất xảy ra lỗi nhiều bit trong một gói sẽ cực kỳ nhỏ. Trong trường hợp này, một bit chẵn lẻ có thể đủ. Tuy nhiên, các phép đo đã chỉ ra rằng, thay vì xảy ra độc lập, các lỗi thường tập trung lại với nhau thành "các đợt". Trong điều kiện lỗi bùng nổ, xác suất lỗi không được phát hiện trong khung được bảo vệ bởi tính chẵn lẻ một bit có thể đạt tới 50% \[Spragins 1991\]. Rõ ràng, cần có một sơ đồ phát hiện lỗi mạnh mẽ hơn (và may mắn thay, nó được sử dụng trong thực tế!). Nhưng trước khi kiểm tra các sơ đồ phát hiện lỗi được sử dụng trong thực tế, chúng ta hãy xem xét một sơ đồ đơn giản

*Hình 6.4 ♦ Tính chẵn lẻ một bit*

0 1 1 1 0 0 0 1 1 0 1 0 1 0 1 1

d bit dữ liệu

Chẵn lẻ

chút

khái quát hóa tính chẵn lẻ một bit sẽ cung cấp cho chúng ta cái nhìn sâu sắc về các kỹ thuật sửa lỗi.

Hình 6.5 cho thấy sự khái quát hóa hai chiều của sơ đồ chẵn lẻ một bit. Ở đây, d bit trong D được chia thành i hàng và j cột. Giá trị chẵn lẻ được tính cho mỗi hàng và cho mỗi cột. Các bit chẵn lẻ i + j + 1 thu được bao gồm các bit phát hiện lỗi của khung lớp liên kết.

Bây giờ giả sử có một lỗi bit xảy ra trong d bit thông tin ban đầu. Với sơ đồ chẵn lẻ hai chiều này, tính chẵn lẻ của cả cột và hàng chứa bit bị lật sẽ bị lỗi. Do đó, người nhận không chỉ có thể phát hiện thực tế là đã xảy ra một lỗi bit đơn lẻ mà còn có thể sử dụng các chỉ số cột và hàng của cột và hàng có lỗi chẵn lẻ để thực sự xác định bit bị hỏng và sửa lỗi đó! Hình 6.5 cho thấy một ví dụ trong đó bit có giá trị 1 ở vị trí (2,2) bị hỏng và chuyển sang 0---một lỗi có thể được phát hiện và sửa được ở bộ thu. Mặc dù cuộc thảo luận của chúng ta tập trung vào d bit thông tin ban đầu, nhưng một lỗi duy nhất trong bản thân các bit chẵn lẻ cũng có thể được phát hiện và sửa chữa được. Tính chẵn lẻ hai chiều cũng có thể phát hiện (nhưng không chính xác!) bất kỳ sự kết hợp nào của hai lỗi trong một gói. Các tính chất khác của sơ đồ chẵn lẻ hai chiều được khám phá trong các bài toán ở cuối chương.

*Hình 6.5 ♦ Tính chẵn lẻ hai chiều*

1 0 1 0 1 1

1 1 1 1 0 0

0 1 1 1 0 1

0 0 1 0 1 0

1 0 1 0 1 1

1 0 1 1 0 0

0 1 1 1 0 1

0 0 1 0 1 0

Tính chẵn lẻ của hàng

Lỗi chẵn lẻ

Lỗi chẵn lẻ

Không có lỗi Lỗi bit đơn có thể sửa được

d1,1

d2,1

. . .

di,1

di+1,1

. . .

. . .

. . .

. . .

. . .

d1, j

d2, j

. . .

di, j

di+1,j

d1,j+1

d2,j+1

. . .

di,j+1

di+1,j+1

Cột chẵn lẻ

Khả năng của máy thu trong việc phát hiện và sửa lỗi được gọi là sửa lỗi chuyển tiếp (FEC). Những kỹ thuật này thường được sử dụng trong các thiết bị lưu trữ và phát lại âm thanh như đĩa CD âm thanh. Trong cài đặt mạng, các kỹ thuật FEC có thể được sử dụng riêng lẻ hoặc kết hợp với các kỹ thuật ARQ lớp liên kết tương tự như những kỹ thuật chúng ta đã xem xét trong Chương 3. Các kỹ thuật FEC rất có giá trị vì chúng có thể làm giảm số lượng yêu cầu truyền lại của người gửi. Có lẽ quan trọng hơn, chúng cho phép sửa lỗi ngay lập tức ở máy thu. Điều này tránh phải chờ độ trễ lan truyền khứ hồi cần thiết để người gửi nhận được gói NAK và để gói được truyền lại truyền trở lại người nhận---một lợi thế quan trọng tiềm tàng đối với các ứng dụng mạng thời gian thực \[Rubenstein 1998\] hoặc các liên kết (chẳng hạn như các liên kết không gian sâu) có độ trễ truyền dài. Nghiên cứu kiểm tra việc sử dụng FEC trong các giao thức kiểm soát lỗi bao gồm \[Biersack 1992; Nonnenmacher 1998; Byers 1998; Shacham 1990\].

**6.2.2 Phương pháp kiểm tra tổng**

Trong kỹ thuật kiểm tra tổng, d bit dữ liệu trong Hình 6.4 được coi là một chuỗi các số nguyên k-bit. Một phương pháp kiểm tra tổng đơn giản là tính tổng các số nguyên k-bit này và sử dụng tổng kết quả làm bit phát hiện lỗi. Tổng kiểm tra Internet dựa trên phương pháp này---byte dữ liệu được coi là số nguyên 16 bit và được tính tổng. Phần bù 1 của tổng này sau đó tạo thành tổng kiểm tra Internet được mang trong tiêu đề phân đoạn. Như đã thảo luận trong Phần 3.3, người nhận kiểm tra tổng kiểm tra bằng cách lấy phần bù 1 của tổng dữ liệu nhận được (bao gồm cả tổng kiểm tra) và kiểm tra xem kết quả có phải là tất cả các bit 0 hay không. Nếu bất kỳ bit nào là 1 thì sẽ có lỗi. RFC 1071 thảo luận chi tiết về thuật toán tổng kiểm tra Internet và cách triển khai nó. Trong giao thức TCP và UDP, tổng kiểm tra Internet được tính toán trên tất cả các trường (bao gồm trường tiêu đề và trường dữ liệu). Trong IP, tổng kiểm tra được tính toán trên tiêu đề IP (vì phân đoạn UDP hoặc TCP có tổng kiểm tra riêng). Trong các giao thức khác, chẳng hạn như XTP \[Strayer 1992\], một tổng kiểm tra được tính trên tiêu đề và một tổng kiểm tra khác được tính trên toàn bộ gói.

Phương pháp kiểm tra tổng yêu cầu chi phí gói tương đối ít. Ví dụ: tổng kiểm tra trong TCP và UDP chỉ sử dụng 16 bit. Tuy nhiên, chúng cung cấp khả năng bảo vệ tương đối yếu trước các lỗi so với kiểm tra dự phòng theo chu kỳ, được thảo luận dưới đây và thường được sử dụng trong lớp liên kết. Một câu hỏi tự nhiên tại thời điểm này là Tại sao việc kiểm tra tổng được sử dụng ở lớp vận chuyển và kiểm tra dự phòng theo chu kỳ được sử dụng ở lớp liên kết? Hãy nhớ lại rằng lớp vận chuyển thường được triển khai trong phần mềm trên máy chủ như một phần của hệ điều hành của máy chủ. Bởi vì việc phát hiện lỗi ở lớp vận chuyển được triển khai trong phần mềm nên điều quan trọng là phải có sơ đồ phát hiện lỗi đơn giản và nhanh chóng như kiểm tra tổng. Mặt khác, việc phát hiện lỗi ở lớp liên kết được triển khai trong phần cứng chuyên dụng trong các bộ điều hợp, có thể nhanh chóng thực hiện các hoạt động CRC phức tạp hơn. Feldmeier \[Feldmeier 1995\] trình bày các kỹ thuật triển khai phần mềm nhanh chóng không chỉ cho các mã tổng kiểm tra có trọng số mà còn cho cả CRC (xem bên dưới) và các mã khác.

**6.2.3 Kiểm tra dự phòng theo chu kỳ (CRC)**

Một kỹ thuật phát hiện lỗi được sử dụng rộng rãi trong các mạng máy tính ngày nay dựa trên mã kiểm tra dự phòng theo chu kỳ (CRC). Mã CRC còn được gọi là mã đa thức, vì có thể xem chuỗi bit được gửi dưới dạng đa thức có hệ số là giá trị 0 và 1 trong chuỗi bit, với các phép toán trên chuỗi bit được hiểu là số học đa thức.

Mã CRC hoạt động như sau. Hãy xem xét đoạn dữ liệu d-bit, D, mà nút gửi muốn gửi đến nút nhận. Người gửi và người nhận trước tiên phải đồng ý về mẫu bit r + 1, được gọi là bộ tạo, chúng ta sẽ ký hiệu là G. Chúng ta sẽ yêu cầu bit có ý nghĩa nhất (ngoài cùng bên trái) của G là 1. Ý tưởng chính đằng sau mã CRC được hiển thị trong Hình 6.6. Đối với một phần dữ liệu D nhất định, người gửi sẽ chọn r bit bổ sung, R và nối chúng vào D sao cho mẫu bit d + r kết quả (được hiểu là số nhị phân) chia hết chính xác cho G (tức là không có số dư) bằng cách sử dụng số học modulo-2. Quá trình kiểm tra lỗi bằng CRC rất đơn giản: Bộ thu chia d + r bit nhận được cho G. Nếu số dư khác 0 thì bộ thu biết rằng đã xảy ra lỗi; nếu không thì dữ liệu được chấp nhận là chính xác.

Tất cả các phép tính CRC được thực hiện theo số học modulo-2 mà không cần cộng hoặc mượn trong phép trừ. Điều này có nghĩa là phép cộng và phép trừ giống hệt nhau và cả hai đều tương đương với phép trừ hoặc (XOR) theo bit của toán hạng. Vì vậy, ví dụ,

1011 XOR 0101 = 1110

1001 XOR 1101 = 0100

Ngoài ra, chúng ta cũng có tương tự

1011 - 0101 = 1110

1001 - 1101 = 0100

Phép nhân và phép chia giống như trong số học cơ số 2, ngoại trừ việc mọi phép cộng hoặc phép trừ bắt buộc đều được thực hiện mà không mang hoặc mượn. Như thường lệ

*Hình 6.6 ♦ CRC*

d bit r bit

D: Bit dữ liệu được gửi

D • 2r XOR R

R: Các bit CRC Mẫu bit

công thức toán học

**số học nhị phân, phép nhân với 2k trái sẽ dịch chuyển mẫu bit k vị trí. Do đó, với D và R, đại lượng D \# 2r XOR R mang lại mẫu bit d + r như trong Hình 6.6. Chúng ta sẽ sử dụng đặc tính đại số này của mẫu bit d + r từ Hình 6.6 trong phần thảo luận bên dưới.**

Bây giờ chúng ta hãy chuyển sang câu hỏi quan trọng về cách người gửi tính R. Hãy nhớ lại rằng chúng ta muốn tìm R sao cho có một n sao cho

**D#2r XOR R = nG**

**Tức là ta muốn chọn R sao cho G chia thành D#2r XOR R không có số dư. Nếu chúng ta XOR (nghĩa là thêm modulo-2, không mang) R vào cả hai vế của phương trình trên, chúng ta sẽ nhận được**

**D#2r = nG XOR R**

**Phương trình này cho chúng ta biết rằng nếu chúng ta chia D \# 2r cho G thì giá trị của phần dư chính xác là R. Nói cách khác, chúng ta có thể tính R là**

**R = số dư D#2r**

G

**Hình 6.7 minh họa phép tính này cho trường hợp D = 101110, d = 6, G = 1001, và r = 3. 9 bit được truyền trong trường hợp này là 101 110 011. Bạn nên tự mình kiểm tra các phép tính này và cũng kiểm tra xem thực sự D \# 2r = 101011 \# G XOR R.**

*Hình 6.7 ♦ Tính toán CRC mẫu*

1 0 0 1 1 0 1 1 1 0 0 0 0

1 0 1 0 1 1

1 0 0 1 1 0 1 0 0 0 1 0 1 0 1 0 0 1 1 1 0 0 0 0 1 1 0 0 1 0 0 1 1 0 1 0 1 0 0 1

0 1 1

G

D

R

Các tiêu chuẩn quốc tế đã được xác định cho các bộ tạo 8-, 12-, 16- và 32-bit, G. Tiêu chuẩn CRC-32 32-bit, đã được áp dụng trong một số giao thức IEEE cấp liên kết, sử dụng một bộ tạo

GCRC@32 = 100000100110000010001110110110111

Mỗi tiêu chuẩn CRC có thể phát hiện các lỗi chùm ít hơn r + 1 bit. (Điều này có nghĩa là tất cả các lỗi bit liên tiếp từ r bit trở xuống sẽ được phát hiện.) Hơn nữa, theo các giả định thích hợp, một cụm có độ dài lớn hơn r + 1 bit được phát hiện với xác suất 1 - 0,5r. Ngoài ra, mỗi tiêu chuẩn CRC có thể phát hiện bất kỳ số lỗi bit lẻ nào. Xem \[Williams 1993\] để thảo luận về việc thực hiện kiểm tra CRC. Lý thuyết đằng sau mã CRC và thậm chí các mã mạnh hơn nằm ngoài phạm vi của văn bản này. Văn bản \[Schwartz 1980\] đưa ra lời giới thiệu tuyệt vời về chủ đề này.

**6.3 Nhiều liên kết và giao thức truy cập**

Trong phần giới thiệu chương này, chúng ta đã lưu ý rằng có hai loại liên kết mạng: liên kết điểm-điểm và liên kết quảng bá. Một liên kết điểm-điểm bao gồm một người gửi ở một đầu của liên kết và một người nhận ở đầu kia của liên kết. Nhiều giao thức lớp liên kết đã được thiết kế cho các liên kết điểm-điểm; giao thức điểm-điểm (PPP) và điều khiển liên kết dữ liệu cấp cao (HDLC) là hai giao thức như vậy. Loại liên kết thứ hai, liên kết quảng bá, có thể có nhiều nút gửi và nhận, tất cả đều được kết nối với cùng một kênh quảng bá chung, duy nhất. Thuật ngữ phát sóng được sử dụng ở đây vì khi bất kỳ một nút nào truyền một khung, kênh đó sẽ phát khung đó và mỗi nút khác sẽ nhận được một bản sao. Ethernet và mạng LAN không dây là những ví dụ về công nghệ lớp liên kết quảng bá. Trong phần này, chúng ta sẽ lùi lại một bước so với các giao thức lớp liên kết cụ thể và trước tiên xem xét một vấn đề có tầm quan trọng trung tâm đối với lớp liên kết: cách phối hợp truy cập của nhiều nút gửi và nhận vào một kênh quảng bá được chia sẻ---vấn đề đa truy cập. Các kênh phát sóng thường được sử dụng trong mạng LAN, các mạng tập trung về mặt địa lý trong một tòa nhà (hoặc trong khuôn viên công ty hoặc trường đại học). Vì vậy, chúng ta sẽ xem xét cách sử dụng nhiều kênh truy cập trong mạng LAN ở cuối phần này.

Tất cả chúng ta đều quen thuộc với khái niệm phát thanh truyền hình - truyền hình đã sử dụng nó kể từ khi nó được phát minh. Nhưng truyền hình truyền thống là phát sóng một chiều (nghĩa là một nút cố định truyền đến nhiều nút nhận), trong khi các nút trên kênh phát sóng của mạng máy tính có thể vừa gửi vừa nhận. Có lẽ một sự tương tự thích hợp hơn của con người đối với một kênh phát sóng là một bữa tiệc cocktail, nơi nhiều người tụ tập trong một căn phòng lớn (không khí cung cấp phương tiện phát sóng) để trò chuyện và lắng nghe. Sự tương tự hay thứ hai là điều mà nhiều độc giả sẽ quen thuộc---một lớp học---nơi mà (các) giáo viên và (các) học sinh đều chia sẻ cùng một phương tiện phát sóng duy nhất. Một vấn đề trung tâm trong

cả hai kịch bản đều là xác định ai sẽ nói chuyện (nghĩa là truyền vào kênh) và khi nào. Là con người, chúng ta đã phát triển một bộ giao thức phức tạp để chia sẻ kênh phát sóng:

"Hãy cho mọi người một cơ hội để nói." "Đừng nói cho đến khi bạn được nói chuyện." "Đừng độc chiếm cuộc trò chuyện." "Hãy giơ tay nếu bạn có câu hỏi." "Đừng ngắt lời khi ai đó đang nói." "Đừng ngủ khi ai đó đang nói chuyện."

Tương tự, các mạng máy tính cũng có các giao thức---còn gọi là giao thức đa truy cập---theo đó các nút điều chỉnh việc truyền tải của chúng vào kênh phát sóng được chia sẻ. Như được hiển thị trong Hình 6.8, nhiều giao thức truy cập cần thiết trong nhiều cài đặt mạng khác nhau, bao gồm cả mạng truy cập có dây và không dây cũng như mạng vệ tinh. Mặc dù về mặt kỹ thuật, mỗi nút đều truy cập kênh phát sóng thông qua bộ chuyển đổi của nó, nhưng trong phần này, chúng tôi sẽ gọi nút đó là nút gửi và

*Hình 6.8 ♦ Nhiều kênh truy cập khác nhau*

Dây dùng chung (ví dụ: mạng truy cập cáp)

Chia sẻ không dây

(ví dụ: Wi-Fi)

Tiệc cocktail vệ tinh

Cái đầu

kết thúc

thiết bị nhận. Trong thực tế, hàng trăm hoặc thậm chí hàng nghìn nút có thể liên lạc trực tiếp qua kênh quảng bá.

Bởi vì tất cả các nút đều có khả năng truyền khung, nên có nhiều hơn hai nút có thể truyền khung cùng một lúc. Khi điều này xảy ra, tất cả các nút đều nhận được nhiều khung hình cùng một lúc; nghĩa là các khung được truyền va chạm ở tất cả các máy thu. Thông thường, khi có xung đột, không nút nhận nào có thể hiểu được bất kỳ khung nào được truyền đi; theo một nghĩa nào đó, tín hiệu của các khung va chạm trở nên gắn bó chặt chẽ với nhau. Do đó, tất cả các khung hình liên quan đến xung đột đều bị mất và kênh quảng bá bị lãng phí trong khoảng thời gian xung đột. Rõ ràng, nếu nhiều nút muốn truyền các khung hình thường xuyên thì nhiều lần truyền sẽ dẫn đến xung đột và phần lớn băng thông của kênh quảng bá sẽ bị lãng phí.

Để đảm bảo rằng kênh quảng bá thực hiện công việc hữu ích khi có nhiều nút hoạt động, cần phải phối hợp việc truyền của các nút hoạt động bằng cách nào đó. Công việc phối hợp này là trách nhiệm của giao thức đa truy cập. Trong 40 năm qua, hàng nghìn bài báo và hàng trăm luận án tiến sĩ đã được viết trên nhiều giao thức truy cập; một cuộc khảo sát toàn diện về 20 năm đầu tiên của nhóm công việc này là \[Rom 1990\]. Hơn nữa, nghiên cứu tích cực về các giao thức đa truy cập vẫn tiếp tục do sự xuất hiện liên tục của các loại liên kết mới, đặc biệt là các liên kết không dây mới.

Trong những năm qua, hàng chục giao thức đa truy cập đã được triển khai trong nhiều công nghệ lớp liên kết khác nhau. Tuy nhiên, chúng ta có thể phân loại bất kỳ giao thức đa truy cập nào thuộc một trong ba loại: giao thức phân vùng kênh, giao thức truy cập ngẫu nhiên và giao thức thay phiên nhau. Chúng tôi sẽ đề cập đến các loại giao thức đa truy cập này trong ba phần phụ sau.

Hãy kết thúc phần tổng quan này bằng cách lưu ý rằng, lý tưởng nhất là giao thức đa truy cập cho kênh quảng bá có tốc độ R bit trên giây phải có các đặc điểm mong muốn sau:

1\. Khi chỉ có một nút có dữ liệu cần gửi, nút đó có thông lượng R bps. 2. Khi M nút có dữ liệu cần gửi, mỗi nút này có thông lượng R/M

bps. Điều này không nhất thiết ngụ ý rằng mỗi nút trong số M nút luôn có tốc độ R/M tức thời, mà đúng hơn là mỗi nút phải có tốc độ truyền trung bình là R/M trong một khoảng thời gian được xác định phù hợp. 3. Giao thức được phân cấp; nghĩa là không có nút chính nào đại diện cho một

điểm lỗi duy nhất của mạng. 4. Giao thức đơn giản nên việc thực hiện không tốn kém.

**6.3.1 Giao thức phân vùng kênh**

Hãy nhớ lại thảo luận ban đầu của chúng ta ở Phần 1.3 rằng ghép kênh phân chia theo thời gian (TDM) và ghép kênh phân chia theo tần số (FDM) là hai kỹ thuật có thể

được sử dụng để phân vùng băng thông của kênh phát sóng giữa tất cả các nút chia sẻ kênh đó. Ví dụ: giả sử kênh hỗ trợ N nút và tốc độ truyền của kênh là R bps. TDM chia thời gian thành các khung thời gian và chia mỗi khung thời gian thành N khe thời gian. (Không nên nhầm lẫn khung thời gian TDM với đơn vị dữ liệu lớp liên kết được trao đổi giữa các bộ điều hợp gửi và nhận, còn được gọi là khung. Để giảm nhầm lẫn, trong tiểu mục này, chúng ta sẽ đề cập đến đơn vị dữ liệu lớp liên kết được trao đổi dưới dạng một gói.) Mỗi ​​khe thời gian sau đó được gán cho một trong N nút. Bất cứ khi nào một nút có một gói để gửi, nó sẽ truyền các bit của gói trong khoảng thời gian được chỉ định trong khung TDM quay vòng. Thông thường, kích thước khe được chọn sao cho một gói có thể được truyền trong một khe thời gian. Hình 6.9 cho thấy một ví dụ TDM bốn nút đơn giản. Quay trở lại sự tương tự của bữa tiệc cocktail của chúng ta, một bữa tiệc cocktail do TDM quản lý sẽ cho phép một người dự tiệc phát biểu trong một khoảng thời gian cố định, sau đó cho phép một người dự tiệc khác phát biểu trong cùng một khoảng thời gian, v.v. Khi mọi người đã có cơ hội nói chuyện, mô hình đó sẽ lặp lại.

TDM hấp dẫn vì nó loại bỏ xung đột và hoàn toàn công bằng: Mỗi nút có tốc độ truyền riêng là R/N bps trong mỗi thời gian khung hình. Tuy nhiên, nó có hai nhược điểm lớn. Đầu tiên, một nút bị giới hạn ở tốc độ trung bình R/N bps ngay cả khi nó là nút duy nhất có gói để gửi. Hạn chế thứ hai là nút phải luôn chờ đến lượt của nó trong chuỗi truyền---ngay cả khi đó là nút duy nhất có khung để gửi. Hãy tưởng tượng người dự tiệc là người duy nhất có điều gì để nói (và hãy tưởng tượng rằng đây là trường hợp thậm chí còn hiếm hơn khi mọi người đều

*Hình 6.9 ♦ Ví dụ về TDM và FDM bốn nút*

4KHz

FDM

TDM

liên kết

4KHz

Chỗ

Tất cả các vị trí có nhãn "2" được dành riêng cho một cặp người gửi-người nhận cụ thể.

Frame

Chìa khóa:

muốn nghe người đó nói gì). Rõ ràng, TDM sẽ là một lựa chọn tồi cho giao thức đa truy cập đối với bên cụ thể này.

Trong khi TDM chia sẻ kênh quảng bá kịp thời, FDM chia kênh R bps thành các tần số khác nhau (mỗi tần số có băng thông R/N) và gán mỗi tần số cho một trong N nút. Do đó, FDM tạo ra N kênh R/N bps nhỏ hơn từ kênh R bps đơn lớn hơn. FDM chia sẻ cả ưu điểm và nhược điểm của TDM. Nó tránh xung đột và phân chia băng thông một cách công bằng giữa N nút. Tuy nhiên, FDM cũng có nhược điểm chính với TDM - nút bị giới hạn ở băng thông R/N, ngay cả khi đó là nút duy nhất có gói để gửi.

Giao thức phân vùng kênh thứ ba là đa truy nhập phân chia theo mã (CDMA). Trong khi TDM và FDM ấn định các khe thời gian và tần số tương ứng cho các nút thì CDMA ấn định một mã khác nhau cho mỗi nút. Sau đó, mỗi nút sẽ sử dụng mã duy nhất của mình để mã hóa các bit dữ liệu mà nó gửi. Nếu các mã được chọn cẩn thận, mạng CDMA có đặc tính tuyệt vời là các nút khác nhau có thể truyền đồng thời nhưng vẫn đảm bảo các máy thu tương ứng của chúng nhận được chính xác các bit dữ liệu được mã hóa của người gửi (giả sử người nhận biết mã của người gửi) bất chấp việc các nút khác gây nhiễu việc truyền. CDMA đã được sử dụng trong các hệ thống quân sự một thời gian (do đặc tính chống nhiễu của nó) và hiện nay được sử dụng rộng rãi trong dân sự, đặc biệt là trong điện thoại di động. Bởi vì việc sử dụng CDMA gắn chặt với các kênh không dây nên chúng ta sẽ dành phần thảo luận về các chi tiết kỹ thuật của CDMA cho đến Chương 7. Bây giờ, chỉ cần biết rằng các mã CDMA, như các khe thời gian trong TDM và các tần số trong FDM, có thể được phân bổ cho nhiều người dùng kênh truy cập.

**6.3.2 Giao thức truy cập ngẫu nhiên**

Lớp giao thức đa truy cập rộng thứ hai là các giao thức truy cập ngẫu nhiên. Trong giao thức truy cập ngẫu nhiên, nút truyền luôn truyền ở tốc độ tối đa của kênh, cụ thể là R bps. Khi có xung đột, mỗi nút liên quan đến xung đột sẽ liên tục truyền lại khung của nó (tức là gói) cho đến khi khung của nó đi qua mà không bị xung đột. Nhưng khi một nút gặp xung đột, nó không nhất thiết phải truyền lại khung ngay lập tức. Thay vào đó, nó đợi một độ trễ ngẫu nhiên trước khi truyền lại khung. Mỗi nút liên quan đến xung đột chọn độ trễ ngẫu nhiên độc lập. Vì độ trễ ngẫu nhiên được chọn độc lập nên có thể một trong các nút sẽ chọn độ trễ đủ nhỏ hơn độ trễ của các nút va chạm khác và do đó sẽ có thể lẻn khung của nó vào kênh mà không bị xung đột.

Có hàng chục, thậm chí hàng trăm giao thức truy cập ngẫu nhiên được mô tả trong tài liệu \[Rom 1990; Bertsekas 1991\]. Trong phần này chúng tôi sẽ mô tả một số giao thức truy cập ngẫu nhiên được sử dụng phổ biến nhất---các giao thức ALOHA \[Abramson 1970; Abramson 1985; Abramson 2009\] và các giao thức đa truy nhập cảm nhận sóng mang (CSMA) \[Kleinrock 1975b\]. Ethernet \[Metcalfe 1976\] là giao thức CSMA phổ biến và được triển khai rộng rãi.

ALOHA có rãnh

Hãy bắt đầu nghiên cứu về các giao thức truy cập ngẫu nhiên bằng một trong những giao thức truy cập ngẫu nhiên đơn giản nhất, giao thức ALOHA có rãnh. Trong mô tả của chúng tôi về ALOHA có rãnh, chúng tôi giả định như sau:

• Tất cả các khung bao gồm chính xác L bit. • Thời gian được chia thành các khe có kích thước L/R giây (nghĩa là một khe bằng thời gian truyền một khung). • Các nút chỉ bắt đầu truyền khung khi bắt đầu các khe. • Các nút được đồng bộ hóa để mỗi nút biết khi nào các khe bắt đầu. • Nếu hai hoặc nhiều khung xung đột trong một khe thì tất cả các nút sẽ phát hiện sự kiện xung đột trước khi khe kết thúc.

Giả sử p là một xác suất, nghĩa là một số từ 0 đến 1. Hoạt động của ALOHA được chia rãnh trong mỗi nút rất đơn giản:

• Khi nút có khung mới để gửi, nó sẽ đợi cho đến khi bắt đầu khe tiếp theo và truyền toàn bộ khung trong khe đó. • Nếu không có xung đột, nút đó đã truyền khung của nó thành công và do đó không cần phải xem xét việc truyền lại khung. (Nút có thể chuẩn bị một khung mới để truyền, nếu có.) • Nếu có xung đột, nút sẽ phát hiện xung đột trước khi kết thúc khe. Nút truyền lại khung của nó trong mỗi khe tiếp theo với xác suất p cho đến khi khung được truyền đi mà không bị xung đột.

Bằng cách truyền lại với xác suất p, chúng tôi muốn nói rằng nút tung một đồng xu sai lệch một cách hiệu quả; các đầu sự kiện tương ứng với "truyền lại", xảy ra với xác suất p. Các đuôi sự kiện tương ứng với "bỏ qua ô và tung đồng xu lại vào ô tiếp theo"; điều này xảy ra với xác suất (1 - p). Tất cả các nút liên quan đến vụ va chạm đều tung đồng xu của mình một cách độc lập.

ALOHA có rãnh dường như có nhiều lợi thế. Không giống như phân vùng kênh, ALOHA có rãnh cho phép một nút truyền liên tục ở tốc độ tối đa R, khi nút đó là nút hoạt động duy nhất. (Một nút được cho là đang hoạt động nếu nó có khung để gửi.) ALOHA có rãnh cũng có tính phân cấp cao, vì mỗi nút phát hiện xung đột và quyết định độc lập thời điểm truyền lại. (Tuy nhiên, ALOHA có rãnh yêu cầu các khe phải được đồng bộ hóa trong các nút; ngay sau đây chúng ta sẽ thảo luận về phiên bản không có khe cắm của giao thức ALOHA, cũng như các giao thức CSMA, không có giao thức nào trong số đó yêu cầu đồng bộ hóa như vậy.) ALOHA có rãnh cũng là một giao thức cực kỳ đơn giản.

ALOHA có rãnh hoạt động tốt khi chỉ có một nút hoạt động, nhưng hiệu quả như thế nào khi có nhiều nút hoạt động? Có hai khả năng hiệu quả

mối quan tâm ở đây. Đầu tiên, như trong Hình 6.10, khi có nhiều nút hoạt động, một phần nhất định của các khe sẽ có xung đột và do đó sẽ bị "lãng phí". Mối quan tâm thứ hai là một phần khác của các vị trí sẽ trống vì tất cả các nút đang hoạt động sẽ không truyền do chính sách truyền xác suất. Các khe "không bị lãng phí" duy nhất sẽ là các khe trong đó có chính xác một nút truyền. Một khe trong đó có chính xác một nút truyền được gọi là khe thành công. Hiệu quả của giao thức đa truy cập có khe cắm được xác định là tỷ lệ dài hạn của các khe thành công trong trường hợp có một số lượng lớn các nút hoạt động, mỗi nút luôn có một số lượng lớn khung để gửi. Lưu ý rằng nếu không sử dụng hình thức kiểm soát truy cập nào và mỗi nút phải truyền lại ngay lập tức sau mỗi lần xung đột thì hiệu quả sẽ bằng không. ALOHA có rãnh rõ ràng làm tăng hiệu quả vượt quá 0, nhưng tăng bao nhiêu?

Bây giờ chúng ta tiến hành phác thảo cách rút ra hiệu quả tối đa của ALOHA theo rãnh. Để giữ cho đạo hàm này đơn giản, hãy sửa đổi giao thức một chút và giả sử rằng mỗi nút cố gắng truyền một khung trong mỗi khe với xác suất p. (Nghĩa là, chúng ta giả định rằng mỗi nút luôn có một khung để gửi và nút đó truyền với xác suất p cho khung mới cũng như cho khung đã bị xung đột.) Giả sử có N nút. Khi đó xác suất để một khe nhất định là một khe thành công là xác suất để một trong các nút truyền và N - 1 nút còn lại không truyền. Xác suất mà một nút nhất định truyền đi là p; xác suất các nút còn lại không truyền là (1 - p)N-1. Do đó, xác suất một nút nhất định thành công là p(1 - p)N-1. Vì có N nút nên xác suất để bất kỳ nút nào trong số N nút thành công là Np(1 - p)N-1.

*Hình 6.10 ♦ Các nút 1, 2 và 3 xung đột ở khe đầu tiên. Nút 2 cuối cùng*

thành công ở vị trí thứ tư, nút 1 ở vị trí thứ tám và nút 3 ở vị trí thứ chín

Nút 3

Chìa khóa:

C = Khe va chạm E = Khe trống S = Khe thành công

Nút 2

Nút 1

Thời gian C E C S E C E S S

Do đó, khi có N nút hoạt động, hiệu quả của ALOHA được phân khe là Np(1 - p)N-1. Để đạt được hiệu quả tối đa cho N nút hoạt động, chúng ta phải tìm p\* tối đa hóa biểu thức này. (Xem các bài tập về nhà để biết tóm tắt chung về đạo hàm này.) Và để đạt được hiệu suất tối đa cho một số lượng lớn các nút hoạt động, chúng ta lấy giới hạn của Np\*(1 - p\*)N-1 khi N tiến đến vô cùng. (Một lần nữa, hãy xem các bài tập về nhà.) Sau khi thực hiện các phép tính này, chúng ta sẽ thấy rằng hiệu suất tối đa của giao thức là 1/e = 0,37. Nghĩa là, khi một số lượng lớn các nút có nhiều khung để truyền thì (tốt nhất) chỉ có 37% số khe thực hiện công việc hữu ích. Như vậy, tốc độ truyền hiệu dụng của kênh không phải là R bps mà chỉ là 0,37 R bps! Một phân tích tương tự cũng cho thấy 37% các vị trí trống và 26% các vị trí có xung đột. Hãy tưởng tượng người quản trị mạng nghèo đã mua hệ thống ALOHA có khe tốc độ 100 Mbps, hy vọng có thể sử dụng mạng để truyền dữ liệu giữa một số lượng lớn người dùng với tốc độ tổng hợp, chẳng hạn như 80 Mbps! Mặc dù kênh có khả năng truyền một khung hình nhất định ở tốc độ toàn kênh là 100 Mbps nhưng về lâu dài, thông lượng thành công của kênh này sẽ dưới 37 Mbps.

ALOHA

Giao thức ALOHA có rãnh yêu cầu tất cả các nút đồng bộ hóa quá trình truyền của chúng để bắt đầu ở đầu khe. Giao thức ALOHA đầu tiên \[Abramson 1970\] thực sự là một giao thức phi tập trung hoàn toàn, không có khe cắm. Trong ALOHA thuần túy, khi một khung hình đến lần đầu tiên (nghĩa là một gói dữ liệu lớp mạng được truyền xuống từ lớp mạng tại nút gửi), nút đó sẽ ngay lập tức truyền toàn bộ khung hình đó vào kênh phát sóng. Nếu một khung được truyền gặp phải xung đột với một hoặc nhiều đường truyền khác thì nút đó sẽ ngay lập tức (sau khi truyền hoàn toàn khung bị va chạm của nó) truyền lại khung đó với xác suất p. Ngược lại, nút sẽ đợi thời gian truyền khung. Sau thời gian chờ này, nó sẽ truyền khung với xác suất p hoặc đợi (không hoạt động) trong thời gian khung khác với xác suất 1 -- p.

Để xác định hiệu quả tối đa của ALOHA thuần túy, chúng tôi tập trung vào một nút riêng lẻ. Chúng tôi sẽ đưa ra các giả định tương tự như trong phân tích ALOHA theo khe của chúng tôi và lấy thời gian truyền khung làm đơn vị thời gian. Tại bất kỳ thời điểm nào, xác suất một nút đang truyền khung là p. Giả sử khung này bắt đầu truyền tại thời điểm t0. Như được hiển thị trong Hình 6.11, để khung này được truyền thành công, không nút nào khác có thể bắt đầu truyền trong khoảng thời gian \[t0 - 1, t0\]. Việc truyền như vậy sẽ trùng với thời điểm bắt đầu truyền khung của nút i. Xác suất để tất cả các nút khác không bắt đầu truyền trong khoảng thời gian này là (1 - p)N-1. Tương tự, không nút nào khác có thể bắt đầu truyền trong khi nút i đang truyền, vì quá trình truyền như vậy sẽ trùng lặp với phần truyền sau của nút i. Xác suất để tất cả các nút khác không bắt đầu truyền trong khoảng thời gian này cũng là (1 - p)N-1. Do đó, xác suất để một nút nhất định truyền thành công là p(1 - p)2(N-1). Bằng cách lấy các giới hạn như trong trường hợp ALOHA có rãnh, chúng tôi thấy rằng hiệu quả tối đa của giao thức ALOHA thuần túy chỉ bằng 1/(2e)---chính xác bằng một nửa so với ALOHA có rãnh. Đây là cái giá phải trả cho một giao thức ALOHA phi tập trung hoàn toàn.

Đa truy nhập nhận biết sóng mang (CSMA)

Trong cả ALOHA có khe và thuần túy, quyết định truyền của một nút được thực hiện độc lập với hoạt động của các nút khác được gắn vào kênh phát sóng. Cụ thể, một nút không chú ý đến việc liệu nút khác có đang truyền khi nó bắt đầu truyền hay không và cũng không dừng truyền nếu nút khác bắt đầu can thiệp vào quá trình truyền của nó. Tương tự như bữa tiệc cocktail của chúng ta, các giao thức ALOHA khá giống một người thích tiệc tùng thô lỗ, người tiếp tục nói huyên thuyên bất kể người khác có đang nói hay không. Là con người, chúng ta có những giao thức con người cho phép chúng ta không chỉ cư xử lịch sự hơn mà còn giảm lượng thời gian "va chạm" với nhau trong cuộc trò chuyện và do đó, tăng lượng dữ liệu chúng ta trao đổi trong các cuộc trò chuyện. Cụ thể, có hai quy tắc quan trọng trong cuộc trò chuyện lịch sự của con người:

• Lắng nghe trước khi nói. Nếu người khác đang nói, hãy đợi cho đến khi họ nói xong. Trong thế giới mạng, điều này được gọi là cảm biến sóng mang - một nút lắng nghe kênh trước khi truyền. Nếu một khung từ một nút khác hiện đang được truyền vào kênh, nút đó sẽ đợi cho đến khi nó phát hiện không có đường truyền nào trong một khoảng thời gian ngắn rồi bắt đầu truyền. • Nếu có người khác bắt đầu nói chuyện cùng lúc thì hãy ngừng nói. Trong thế giới mạng, điều này được gọi là phát hiện xung đột - một nút truyền lắng nghe kênh trong khi nó đang truyền. Nếu nó phát hiện một nút khác đang truyền một khung gây nhiễu, nó sẽ dừng truyền và đợi một khoảng thời gian ngẫu nhiên trước khi lặp lại chu kỳ cảm nhận và truyền khi không hoạt động.

Hai quy tắc này được thể hiện trong họ đa truy cập cảm nhận sóng mang (CSMA) và CSMA với các giao thức phát hiện xung đột (CSMA/CD) \[Kleinrock 1975b; Metcalfe 1976; Lâm 1980; Ròm 1990\]. Nhiều biến thể về CSMA và

*Hình 6.11 ♦ Can thiệp vào việc truyền tải trong ALOHA thuần túy*

Thời gian

Sẽ trùng lặp với sự bắt đầu của

khung của tôi

t0 -- 1 t0 t0 + 1

Sẽ trùng lặp với phần cuối của

khung của tôi

Khung nút i

CSMA/CD đã được đề xuất. Ở đây, chúng ta sẽ xem xét một số đặc điểm cơ bản và quan trọng nhất của CSMA và CSMA/CD.

Câu hỏi đầu tiên bạn có thể hỏi về CSMA là tại sao, nếu tất cả các nút thực hiện cảm biến sóng mang, xung đột có xảy ra ngay từ đầu không? Cuối cùng, một nút sẽ không truyền bất cứ khi nào nó cảm nhận được rằng một nút khác đang truyền. Câu trả lời cho câu hỏi này có thể được minh họa tốt nhất bằng cách sử dụng biểu đồ không-thời gian \[Molle 1987\]. Hình 6.12 cho thấy sơ đồ không-thời gian gồm bốn nút (A, B, C, D) được gắn vào một bus quảng bá tuyến tính. Trục hoành hiển thị vị trí của từng nút trong không gian; trục tung biểu thị thời gian.

Tại thời điểm t0, nút B cảm nhận được kênh không hoạt động vì hiện tại không có nút nào khác đang truyền. Nút B do đó bắt đầu truyền, với các bit của nó lan truyền theo cả hai hướng dọc theo môi trường phát sóng. Sự truyền đi xuống của các bit của B trong Hình 6.12 với thời gian ngày càng tăng cho thấy rằng cần một lượng thời gian khác 0 để các bit của B thực sự lan truyền (mặc dù ở tốc độ gần tốc độ ánh sáng) dọc theo môi trường phát sóng. Tại thời điểm t1 (t1 7 t0), nút D có khung để gửi. Mặc dù nút B hiện đang truyền tại thời điểm t1, nhưng các bit được B truyền vẫn chưa đến được D và do đó D cảm nhận được

NORM ABRAMSON VÀ ALOHANET

Norm Abramson, một kỹ sư tiến sĩ, có niềm đam mê lướt web và quan tâm đến chuyển mạch gói. Sự kết hợp lợi ích này đã đưa ông đến với Đại học Hawaii vào năm 1969. Hawaii bao gồm nhiều hòn đảo miền núi, gây khó khăn cho việc lắp đặt và vận hành các mạng lưới trên đất liền. Khi không lướt web, Abramson nghĩ đến cách thiết kế một mạng thực hiện chuyển mạch gói qua sóng vô tuyến. Mạng do ông thiết kế có một máy chủ trung tâm và một số nút phụ nằm rải rác trên Quần đảo Hawaii. Mạng có hai kênh, mỗi kênh sử dụng một dải tần số khác nhau. Kênh đường xuống phát các gói tin từ máy chủ trung tâm đến máy chủ phụ; và kênh ngược dòng đã gửi các gói từ máy chủ thứ cấp đến máy chủ trung tâm. Ngoài việc gửi các gói thông tin, máy chủ trung tâm còn gửi trên kênh hạ lưu một xác nhận cho mỗi gói được nhận thành công từ máy chủ thứ cấp.

Bởi vì các máy chủ thứ cấp truyền các gói theo kiểu phân quyền nên chắc chắn sẽ xảy ra xung đột trên kênh ngược dòng. Quan sát này đã khiến Abramson nghĩ ra giao thức ALOHA thuần túy, như được mô tả trong chương này. Năm 1970, với sự tài trợ liên tục từ ARPA, Abramson đã kết nối ALOHAnet của mình với ARPAnet. Công trình của Abramson quan trọng không chỉ vì đây là ví dụ đầu tiên về mạng gói vô tuyến mà còn vì nó đã truyền cảm hứng cho Bob Metcalfe. Vài năm sau, Metcalfe sửa đổi giao thức ALOHA để tạo giao thức CSMA/CD và mạng LAN Ethernet.

LỊCH SỬ TRƯỜNG HỢP

kênh rỗi ở thời điểm t1. Theo giao thức CSMA, D bắt đầu truyền khung của nó. Một thời gian ngắn sau, quá trình truyền của B bắt đầu cản trở quá trình truyền của D tại D. Từ Hình 6.12, rõ ràng là độ trễ truyền kênh từ đầu đến cuối của kênh quảng bá---thời gian cần thiết để tín hiệu truyền từ một trong các nút này sang nút khác---sẽ đóng một vai trò quan trọng trong việc xác định hiệu suất của nó. Độ trễ lan truyền này càng dài thì khả năng nút cảm nhận sóng mang chưa thể cảm nhận được quá trình truyền đã bắt đầu ở một nút khác trong mạng càng lớn.

Đa truy cập Carrier Sense với tính năng phát hiện va chạm (CSMA/CD)

Trong Hình 6.12, các nút không thực hiện phát hiện xung đột; cả B và D tiếp tục truyền toàn bộ khung của chúng mặc dù đã xảy ra xung đột. Khi một nút thực hiện phát hiện xung đột, nó sẽ ngừng truyền ngay khi phát hiện xung đột. Hình 6.13 cho thấy kịch bản tương tự như trong Hình 6.12, ngoại trừ hai

*Hình 6.12 ♦ Sơ đồ không-thời gian của hai nút CSMA va chạm*

truyền động

MỘT

Thời gian Thời gian

Không gian

t 0

t 1

B C D

mỗi nút hủy bỏ quá trình truyền của chúng trong một thời gian ngắn sau khi phát hiện xung đột. Rõ ràng, việc thêm tính năng phát hiện xung đột vào giao thức đa truy cập sẽ giúp thực hiện giao thức bằng cách không truyền toàn bộ khung vô dụng, bị hỏng (do nhiễu với khung từ nút khác).

Trước khi phân tích giao thức CSMA/CD, bây giờ chúng ta hãy tóm tắt hoạt động của nó từ góc độ của một bộ điều hợp (trong một nút) được gắn vào kênh phát sóng:

1\. Bộ điều hợp lấy datagram từ lớp mạng, chuẩn bị lớp liên kết

frame và đặt bộ đệm bộ điều hợp khung. 2. Nếu bộ điều hợp cảm nhận được rằng kênh không hoạt động (nghĩa là không có năng lượng tín hiệu

vào bộ chuyển đổi từ kênh), nó bắt đầu truyền khung. Mặt khác, nếu bộ điều hợp cảm nhận được rằng kênh đang bận, nó sẽ đợi cho đến khi cảm nhận được không có năng lượng tín hiệu và sau đó bắt đầu truyền khung. 3. Trong khi truyền, bộ chuyển đổi sẽ giám sát sự hiện diện của năng lượng tín hiệu

đến từ các bộ điều hợp khác sử dụng kênh phát sóng.

*Hình 6.13 ♦ CSMA có phát hiện va chạm*

MỘT

Thời gian Thời gian

Phát hiện/hủy bỏ va chạm

thời gian

Không gian

t 0

t 1

B C D

4\. Nếu bộ chuyển đổi truyền toàn bộ khung mà không phát hiện thấy năng lượng tín hiệu từ

các bộ điều hợp khác, bộ chuyển đổi được hoàn thiện với khung. Mặt khác, nếu bộ điều hợp phát hiện năng lượng tín hiệu từ các bộ điều hợp khác trong khi truyền, nó sẽ hủy bỏ việc truyền (nghĩa là nó dừng truyền khung của nó). 5. Sau khi hủy bỏ, bộ điều hợp sẽ đợi một khoảng thời gian ngẫu nhiên rồi quay lại

bước 2.

Hy vọng rằng nhu cầu đợi một khoảng thời gian ngẫu nhiên (chứ không phải cố định) là rõ ràng---nếu hai nút truyền khung hình cùng lúc và sau đó cả hai đều đợi cùng một khoảng thời gian cố định thì chúng sẽ tiếp tục xung đột mãi mãi. Nhưng khoảng thời gian thích hợp để chọn thời gian lùi ngẫu nhiên là bao nhiêu? Nếu khoảng thời gian lớn và số lượng nút xung đột nhỏ, các nút có thể sẽ đợi một khoảng thời gian lớn (với kênh vẫn ở chế độ rảnh) trước khi lặp lại bước cảm nhận và truyền khi không hoạt động. Mặt khác, nếu khoảng thời gian nhỏ và số lượng nút xung đột lớn thì có khả năng các giá trị ngẫu nhiên được chọn sẽ gần giống nhau và các nút truyền sẽ lại xung đột. Điều chúng tôi muốn là một khoảng thời gian ngắn khi số lượng nút va chạm nhỏ và dài khi số lượng nút va chạm lớn.

**Thuật toán lùi số mũ nhị phân, được sử dụng trong Ethernet cũng như trong các giao thức đa truy cập mạng cáp DOCSIS \[DOCSIS 3.1 2014\], giải quyết vấn đề này một cách dễ dàng. Cụ thể, khi truyền một khung đã trải qua n xung đột, một nút chọn giá trị K một cách ngẫu nhiên từ {0,1,2, . . . . 2n-1}. Do đó, một khung càng trải qua nhiều xung đột thì khoảng thời gian mà K được chọn càng lớn. Đối với Ethernet, lượng thời gian thực tế mà một nút chờ là K \# 512 bit lần (tức là K nhân với lượng thời gian cần thiết để gửi 512 bit vào Ethernet) và giá trị tối đa mà n có thể nhận được giới hạn ở mức 10.**

Hãy xem một ví dụ. Giả sử rằng một nút cố gắng truyền một khung lần đầu tiên và trong khi truyền nó phát hiện ra xung đột. Nút sau đó chọn K = 0 với xác suất 0,5 hoặc chọn K = 1 với xác suất 0,5. Nếu nút chọn K = 0 thì ngay lập tức nó bắt đầu cảm nhận kênh. Nếu nút chọn K = 1, nó sẽ đợi 512 bit thời gian (ví dụ: 5,12 micro giây cho Ethernet 100 Mbps) trước khi bắt đầu chu kỳ cảm nhận và truyền khi không hoạt động. Sau va chạm thứ hai, K được chọn với xác suất bằng nhau từ {0,1,2,3}. Sau ba lần va chạm, K được chọn với xác suất bằng nhau từ {0,1,2,3,4,5,6,7}. Sau 10 lần va chạm trở lên, K được chọn với xác suất bằng nhau từ {0,1,2, . . . , 1023}. Do đó, kích thước của các tập mà K được chọn tăng theo cấp số nhân với số lượng va chạm; vì lý do này, thuật toán này được gọi là thuật toán lùi số mũ nhị phân.

Ở đây chúng tôi cũng lưu ý rằng mỗi khi một nút chuẩn bị một khung mới để truyền, nó sẽ chạy thuật toán CSMA/CD, không tính đến bất kỳ xung đột nào có thể xảy ra trong quá khứ gần đây. Vì vậy, có thể một nút có khung mới sẽ ngay lập tức có thể truyền thành công trong khi một số nút khác đang ở trạng thái chờ theo cấp số nhân.

Hiệu suất CSMA/CD

Khi chỉ một nút có khung để gửi, nút đó có thể truyền ở tốc độ kênh đầy đủ (ví dụ: đối với tốc độ thông thường của Ethernet là 10 Mbps, 100 Mbps hoặc 1 Gbps). Tuy nhiên, nếu nhiều nút có khung để truyền thì tốc độ truyền hiệu quả của kênh có thể thấp hơn nhiều. Chúng tôi xác định hiệu quả của CSMA/CD là khoảng thời gian dài trong đó các khung được truyền trên kênh mà không có xung đột khi có một số lượng lớn các nút hoạt động, trong đó mỗi nút có một số lượng lớn khung để gửi. Để trình bày một dạng gần đúng dạng đóng về hiệu suất của Ethernet, hãy gọi dprop biểu thị thời gian tối đa cần thiết để truyền năng lượng tín hiệu giữa hai bộ điều hợp bất kỳ. Giả sử dtrans là thời gian để truyền khung có kích thước tối đa (khoảng 1,2 mili giây cho Ethernet 10 Mbps). Việc rút ra hiệu quả của CSMA/CD nằm ngoài phạm vi của cuốn sách này (xem \[Lam 1980\] và \[Bertsekas 1991\]). Ở đây chúng ta chỉ đơn giản phát biểu phép tính gần đúng sau:

Hiệu suất = 1 + 5dprop\>dtrans Chúng tôi thấy từ công thức này rằng khi dprop tiến đến 0 thì hiệu suất tiến đến 1. Điều này phù hợp với trực giác của chúng tôi rằng nếu độ trễ lan truyền bằng 0, các nút va chạm sẽ hủy bỏ ngay lập tức mà không lãng phí kênh. Ngoài ra, khi dtrans trở nên rất lớn, hiệu quả sẽ tiến tới mức 1. Điều này cũng trực quan vì khi một khung lấy kênh, nó sẽ giữ kênh trong một thời gian rất dài; do đó, kênh sẽ hoạt động hiệu quả trong hầu hết thời gian.

**6.3.3 Giao thức thay phiên nhau**

Hãy nhớ lại rằng hai thuộc tính mong muốn của giao thức đa truy cập là (1) khi chỉ có một nút hoạt động, nút hoạt động có thông lượng là R bps và (2) khi M nút hoạt động thì mỗi nút hoạt động có thông lượng gần R/M bps. Giao thức ALOHA và CSMA có thuộc tính đầu tiên này nhưng không có thuộc tính thứ hai. Điều này đã thúc đẩy các nhà nghiên cứu tạo ra một loại giao thức khác - giao thức thay phiên nhau. Giống như các giao thức truy cập ngẫu nhiên, có hàng chục giao thức thay phiên nhau và mỗi giao thức này có nhiều biến thể. Chúng ta sẽ thảo luận về hai giao thức quan trọng hơn ở đây. Đầu tiên là giao thức bỏ phiếu. Giao thức bỏ phiếu yêu cầu một trong các nút được chỉ định là nút chính. Nút chính thăm dò từng nút theo kiểu vòng tròn. Cụ thể, nút chính trước tiên sẽ gửi một tin nhắn đến nút 1, nói rằng nó (nút 1) có thể truyền tối đa số lượng khung hình tối đa. Sau khi nút 1 truyền một số khung, nút chính sẽ thông báo cho nút 2 rằng nó (nút 2) có thể truyền tới số lượng khung tối đa. (Nút chính có thể xác định khi nào một nút đã gửi xong các khung của nó bằng cách quan sát việc thiếu tín hiệu trên kênh.) Quy trình tiếp tục theo cách này, với nút chính sẽ thăm dò từng nút theo cách tuần hoàn.

Giao thức thăm dò loại bỏ các xung đột và các khe trống gây khó khăn cho các giao thức truy cập ngẫu nhiên. Điều này cho phép bỏ phiếu đạt được hiệu quả cao hơn nhiều. Nhưng

nó cũng có một số hạn chế. Hạn chế đầu tiên là giao thức đưa ra độ trễ thăm dò---khoảng thời gian cần thiết để thông báo cho nút mà nó có thể truyền. Ví dụ: nếu chỉ có một nút hoạt động thì nút đó sẽ truyền với tốc độ nhỏ hơn R bps, vì nút chính phải thăm dò lần lượt từng nút không hoạt động mỗi khi nút hoạt động gửi số lượng khung tối đa. Hạn chế thứ hai, có khả năng nghiêm trọng hơn, là nếu nút chính bị lỗi, toàn bộ kênh sẽ không hoạt động. Giao thức Bluetooth mà chúng ta sẽ nghiên cứu trong Phần 6.3 là một ví dụ về giao thức thăm dò ý kiến.

Giao thức thay phiên nhau thứ hai là giao thức chuyển mã thông báo. Trong giao thức này không có nút chính. Một khung nhỏ, có mục đích đặc biệt được gọi là mã thông báo được trao đổi giữa các nút theo một thứ tự cố định nào đó. Ví dụ: nút 1 có thể luôn gửi mã thông báo đến nút 2, nút 2 có thể luôn gửi mã thông báo đến nút 3 và nút N có thể luôn gửi mã thông báo đến nút 1. Khi một nút nhận được mã thông báo, nó chỉ giữ mã thông báo nếu nó có một số khung để truyền; nếu không, nó sẽ ngay lập tức chuyển tiếp mã thông báo đến nút tiếp theo. Nếu một nút có khung để truyền khi nhận được mã thông báo, nó sẽ gửi tới số lượng khung tối đa và sau đó chuyển tiếp mã thông báo đến nút tiếp theo. Việc chuyển mã thông báo được phân cấp và hiệu quả cao. Nhưng nó cũng có vấn đề của nó. Ví dụ: lỗi của một nút có thể làm hỏng toàn bộ kênh. Hoặc nếu một nút vô tình bỏ qua việc phát hành mã thông báo thì một số quy trình khôi phục phải được thực hiện để đưa mã thông báo trở lại lưu thông. Trong những năm qua, nhiều giao thức chuyển mã thông báo đã được phát triển, bao gồm giao thức giao diện dữ liệu phân tán sợi quang (FDDI) \[Jain 1994\] và giao thức vòng mã thông báo IEEE 802.5 \[IEEE 802.5 2012\] và mỗi giao thức đều phải giải quyết những vấn đề này cũng như các vấn đề khó khăn khác.

**6.3.4 DOCSIS: Giao thức lớp liên kết để truy cập Internet qua cáp**

Trong ba phần phụ trước, chúng ta đã tìm hiểu về ba loại giao thức đa truy cập rộng rãi: giao thức phân vùng kênh, giao thức truy cập ngẫu nhiên và giao thức thay phiên nhau. Mạng truy cập cáp sẽ là một trường hợp điển hình xuất sắc ở đây, vì chúng ta sẽ tìm thấy các khía cạnh của từng loại trong số ba loại giao thức đa truy cập này với mạng truy cập cáp!

Hãy nhớ lại Phần 1.2.1 rằng mạng truy cập cáp thường kết nối hàng nghìn modem cáp dân dụng với hệ thống đầu cuối modem cáp (CMTS) ở đầu cuối mạng cáp. Thông số kỹ thuật giao diện dịch vụ dữ liệu qua cáp (DOCSIS) \[DOCSIS 3.1 2014; Hamzeh 2015\] chỉ định kiến ​​trúc mạng dữ liệu cáp và các giao thức của nó. DOCSIS sử dụng FDM để phân chia các phân đoạn mạng hạ lưu (CMTS đến modem) và ngược dòng (modem đến CMTS) thành nhiều kênh tần số. Mỗi kênh hạ lưu có độ rộng từ 24 MHz đến 192 MHz, với thông lượng tối đa khoảng 1,6 Gbps trên mỗi kênh; mỗi kênh ngược dòng có độ rộng kênh từ 6,4 MHz đến 96 MHz, với thông lượng ngược dòng tối đa khoảng 1 Gbps. Mỗi thượng nguồn và hạ lưu

kênh là một kênh phát sóng. Frames được CMTS truyền trên kênh hạ lưu được tất cả các modem cáp nhận kênh đó nhận; Tuy nhiên, do chỉ có một CMTS truyền vào kênh hạ lưu nên không có vấn đề đa truy cập. Tuy nhiên, hướng ngược dòng thú vị hơn và thách thức hơn về mặt kỹ thuật, vì nhiều modem cáp chia sẻ cùng một kênh (tần số) ngược dòng với CMTS và do đó xung đột có thể xảy ra.

Như minh họa trong Hình 6.14, mỗi kênh ngược dòng được chia thành các khoảng thời gian (giống TDM), mỗi kênh chứa một chuỗi các khe nhỏ trong đó các modem cáp có thể truyền tới CMTS. CMTS cấp quyền rõ ràng cho các modem cáp riêng lẻ truyền trong các khe cắm nhỏ cụ thể. CMTS thực hiện điều này bằng cách gửi một tin nhắn điều khiển được gọi là tin nhắn MAP trên kênh xuôi dòng để chỉ định modem cáp nào (có dữ liệu cần gửi) có thể truyền trong khe cắm mini nào trong khoảng thời gian được chỉ định trong tin nhắn điều khiển. Do các khe cắm mini được phân bổ rõ ràng cho các modem cáp nên CMTS có thể đảm bảo không có xung đột truyền tải trong khe cắm mini.

Nhưng làm thế nào CMTS biết được modem cáp nào có dữ liệu cần gửi ngay từ đầu? Điều này được thực hiện bằng cách yêu cầu các modem cáp gửi các khung yêu cầu khe nhỏ đến CMTS trong một tập hợp các khe nhỏ khoảng thời gian đặc biệt dành riêng cho mục đích này, như trong Hình 6.14. Các khung yêu cầu khe nhỏ này được truyền theo cách truy cập ngẫu nhiên và do đó có thể xung đột với nhau. Modem cáp không thể nhận biết liệu kênh ngược dòng có bận hay không phát hiện xung đột. Thay vào đó, modem cáp suy ra rằng khung yêu cầu khe nhỏ của nó gặp phải xung đột nếu nó không nhận được phản hồi cho việc phân bổ được yêu cầu trong bản tin điều khiển xuôi dòng tiếp theo. Khi xảy ra xung đột, modem cáp sử dụng hàm mũ nhị phân

*Hình 6.14 ♦ Kênh ngược dòng và hạ lưu giữa CMTS và*

modem cáp

Nhà ở với

modem cáp

Khe nhỏ chứa khung yêu cầu khe nhỏ

Các khe nhỏ được chỉ định chứa các khung dữ liệu ngược dòng của modem cáp

Đầu cáp

Khung BẢN ĐỒ cho

khoảng \[t1,t2\]

CMTS

Kênh hạ lưu tôi

Kênh ngược dòng j

t1 t2

backoff để trì hoãn việc truyền lại khung yêu cầu khe nhỏ của nó tới một khe thời gian trong tương lai. Khi có ít lưu lượng trên kênh ngược dòng, modem cáp thực sự có thể truyền các khung dữ liệu trong các khe được gán trên danh nghĩa cho các khung yêu cầu khe nhỏ (và do đó tránh phải chờ phân bổ khe nhỏ).

Do đó, mạng truy cập cáp đóng vai trò là một ví dụ tuyệt vời về nhiều giao thức truy cập đang hoạt động---FDM, TDM, truy cập ngẫu nhiên và các khe thời gian được phân bổ tập trung trong một mạng!

**6.4 Mạng cục bộ chuyển mạch**

Đã bao phủ các mạng quảng bá và nhiều giao thức truy cập trong phần trước, hãy chuyển sự chú ý của chúng ta sang các mạng cục bộ được chuyển mạch. Hình 6.15 hiển thị một mạng cục bộ được chuyển đổi kết nối ba phòng ban, hai máy chủ và một bộ định tuyến với bốn bộ chuyển mạch. Vì các bộ chuyển mạch này hoạt động ở lớp liên kết nên chúng chuyển đổi các khung của lớp liên kết (chứ không phải các datagram của lớp mạng), không nhận ra địa chỉ của lớp mạng và không sử dụng các thuật toán định tuyến như OSPF để xác định

*Hình 6.15 ♦ Mạng tổ chức được kết nối với nhau bằng bốn thiết bị chuyển mạch*

Máy chủ thư

Để bên ngoài

internet

1 Gbps

1 Gbps

1 Gbps

Kỹ thuật điện Khoa học máy tính

100 Mbps (sợi)

100 Mbps (sợi) 100 Mbps (sợi)

Hỗn hợp cáp 10 Mbps, 100 Mbps, 1 Gbps, Cat 5

Máy chủ web

Kỹ thuật máy tính

đường dẫn thông qua mạng của các thiết bị chuyển mạch lớp 2. Thay vì sử dụng địa chỉ IP, chúng ta sẽ sớm thấy rằng chúng sử dụng địa chỉ lớp liên kết để chuyển tiếp các khung lớp liên kết thông qua mạng chuyển mạch. Chúng ta sẽ bắt đầu nghiên cứu về mạng LAN chuyển mạch bằng cách trước tiên đề cập đến việc đánh địa chỉ lớp liên kết (Phần 6.4.1). Sau đó, chúng tôi kiểm tra giao thức Ethernet nổi tiếng (Phần 6.4.2). Sau khi kiểm tra địa chỉ lớp liên kết và Ethernet, chúng ta sẽ xem cách các bộ chuyển mạch lớp liên kết hoạt động (Phần 6.4.3), sau đó xem (Phần 6.4.4) các bộ chuyển mạch này thường được sử dụng như thế nào để xây dựng mạng LAN quy mô lớn.

**6.4.1 Đánh địa chỉ lớp liên kết và ARP**

Hosts và bộ định tuyến có địa chỉ lớp liên kết. Bây giờ bạn có thể thấy điều này đáng ngạc nhiên, hãy nhớ lại Chương 4 rằng các máy chủ và bộ định tuyến cũng có địa chỉ lớp mạng. Bạn có thể hỏi, tại sao chúng ta lại cần có địa chỉ ở cả lớp mạng và lớp liên kết? Ngoài việc mô tả cú pháp và chức năng của các địa chỉ lớp liên kết, trong phần này chúng tôi hy vọng làm sáng tỏ lý do tại sao hai lớp địa chỉ này lại hữu ích và trên thực tế là không thể thiếu. Chúng tôi cũng sẽ đề cập đến Giao thức phân giải địa chỉ (ARP), cung cấp cơ chế dịch các địa chỉ IP sang địa chỉ lớp liên kết.

Địa chỉ MAC

Trên thực tế, không phải máy chủ và bộ định tuyến có địa chỉ lớp liên kết mà là các bộ điều hợp của chúng (nghĩa là giao diện mạng) mới có địa chỉ lớp liên kết. Do đó, một máy chủ hoặc bộ định tuyến có nhiều giao diện mạng sẽ có nhiều địa chỉ lớp liên kết được liên kết với nó, giống như nó cũng sẽ có nhiều địa chỉ IP được liên kết với nó. Tuy nhiên, điều quan trọng cần lưu ý là các switch lớp liên kết không có địa chỉ lớp liên kết được liên kết với các giao diện kết nối với máy chủ và bộ định tuyến của chúng. Điều này là do công việc của bộ chuyển mạch lớp liên kết là mang các gói dữ liệu giữa các máy chủ và bộ định tuyến; một bộ chuyển mạch thực hiện công việc này một cách minh bạch, nghĩa là không cần máy chủ hoặc bộ định tuyến phải xác định địa chỉ khung một cách rõ ràng cho bộ chuyển mạch can thiệp. Điều này được minh họa trong hình 6.16. Địa chỉ lớp liên kết được gọi khác nhau là địa chỉ LAN, địa chỉ vật lý hoặc địa chỉ MAC. Vì địa chỉ MAC dường như là thuật ngữ phổ biến nhất nên từ nay chúng ta sẽ gọi địa chỉ lớp liên kết là địa chỉ MAC. Đối với hầu hết các mạng LAN (bao gồm Ethernet và mạng LAN không dây 802.11), địa chỉ MAC dài 6 byte, cung cấp 248 địa chỉ MAC có thể có. Như được hiển thị trong Hình 6.16, các địa chỉ 6 byte này thường được biểu thị bằng ký hiệu thập lục phân, với mỗi byte địa chỉ được biểu thị dưới dạng một cặp số thập lục phân. Mặc dù địa chỉ MAC được thiết kế cố định nhưng giờ đây bạn có thể thay đổi địa chỉ MAC của bộ điều hợp thông qua phần mềm. Tuy nhiên, trong phần còn lại của phần này, chúng tôi sẽ giả định rằng địa chỉ MAC của bộ điều hợp là cố định.

Một đặc tính thú vị của địa chỉ MAC là không có hai bộ điều hợp nào có cùng địa chỉ. Điều này có vẻ đáng ngạc nhiên vì các bộ điều hợp được sản xuất ở nhiều quốc gia bởi nhiều công ty. Làm thế nào một công ty sản xuất bộ chuyển đổi ở Đài Loan có thể đảm bảo rằng họ đang sử dụng các địa chỉ khác với địa chỉ của một công ty sản xuất?

bộ điều hợp ở Bỉ? Câu trả lời là IEEE quản lý không gian địa chỉ MAC. Đặc biệt, khi một công ty muốn sản xuất bộ điều hợp, họ sẽ mua một phần không gian địa chỉ bao gồm 224 địa chỉ với một khoản phí danh nghĩa. IEEE phân bổ đoạn 224 địa chỉ bằng cách cố định 24 bit đầu tiên của địa chỉ MAC và cho phép công ty tạo ra các kết hợp duy nhất của 24 bit cuối cùng cho mỗi bộ chuyển đổi.

Địa chỉ MAC của bộ điều hợp có cấu trúc phẳng (ngược lại với cấu trúc phân cấp) và không thay đổi cho dù bộ điều hợp đi đến đâu. Một máy tính xách tay có giao diện Ethernet luôn có cùng một địa chỉ MAC, bất kể máy tính ở đâu. Điện thoại thông minh có giao diện 802.11 luôn có cùng địa chỉ MAC, bất kể điện thoại thông minh ở đâu. Ngược lại, hãy nhớ lại rằng, địa chỉ IP có cấu trúc phân cấp (nghĩa là phần mạng và phần máy chủ) và địa chỉ IP của máy chủ cần được thay đổi khi máy chủ di chuyển, tức là thay đổi mạng mà nó được gắn vào. Địa chỉ MAC của bộ chuyển đổi tương tự như số an sinh xã hội của một người, cũng có cấu trúc địa chỉ phẳng và không thay đổi cho dù người đó đi đâu. Địa chỉ IP tương tự như địa chỉ gửi thư của một người, có thứ bậc và phải được thay đổi bất cứ khi nào một người di chuyển. Giống như một người có thể thấy hữu ích khi có cả địa chỉ bưu điện và số an sinh xã hội, việc có cả địa chỉ lớp mạng và địa chỉ MAC cũng rất hữu ích đối với giao diện máy chủ và bộ định tuyến.

Khi bộ điều hợp muốn gửi một khung đến một số bộ điều hợp đích, bộ điều hợp gửi sẽ chèn địa chỉ MAC của bộ điều hợp đích vào khung rồi gửi khung vào mạng LAN. Như chúng ta sẽ sớm thấy, một switch thỉnh thoảng phát một khung hình đến trên tất cả các giao diện của nó. Chúng ta sẽ thấy trong Chương 7 rằng 802.11 cũng phát các khung. Do đó, bộ chuyển đổi có thể nhận được một khung không được gửi đến nó. Do đó, khi một bộ điều hợp nhận được một khung, nó sẽ kiểm tra xem địa chỉ MAC đích có

*Hình 6.16 ♦ Mỗi giao diện kết nối với mạng LAN có một MAC duy nhất*

Địa chỉ

88-B2-2F-54-1A-0F 5C-66-AB-90-75-B1

1A-23-F9-CD-06-9B

49-BD-D2-C7-56-2A

trong khung khớp với địa chỉ MAC của chính nó. Nếu có sự trùng khớp, bộ điều hợp sẽ trích xuất gói dữ liệu kèm theo và chuyển gói dữ liệu đó lên ngăn xếp giao thức. Nếu không khớp, bộ điều hợp sẽ loại bỏ khung mà không chuyển gói dữ liệu lớp mạng lên. Như vậy, đích chỉ bị gián đoạn khi nhận được khung.

Tuy nhiên, đôi khi bộ điều hợp gửi muốn tất cả các bộ điều hợp khác trên mạng LAN nhận và xử lý khung mà nó sắp gửi. Trong trường hợp này, bộ điều hợp gửi sẽ chèn một địa chỉ quảng bá MAC đặc biệt vào trường địa chỉ đích của khung. Đối với mạng LAN sử dụng địa chỉ 6 byte (chẳng hạn như Ethernet và 802.11), địa chỉ quảng bá là một chuỗi gồm 48 số 1 liên tiếp (nghĩa là FF-FF-FF-FF-FF-FF theo ký hiệu thập lục phân).

Giao thức phân giải địa chỉ (ARP)

Vì có cả địa chỉ lớp mạng (ví dụ: địa chỉ Internet IP) và địa chỉ lớp liên kết (tức là địa chỉ MAC), nên cần phải dịch giữa chúng. Đối với Internet, đây là công việc của Giao thức phân giải địa chỉ (ARP) \[RFC 826\].

Để hiểu sự cần thiết của một giao thức như ARP, hãy xem xét mạng được hiển thị trong Hình 6.17. Trong ví dụ đơn giản này, mỗi máy chủ và bộ định tuyến có một địa chỉ IP và một địa chỉ MAC duy nhất. Như thường lệ, địa chỉ IP được hiển thị dưới dạng thập phân chấm

GIỮ CÁC LỚP ĐỘC LẬP

Có một số lý do tại sao giao diện máy chủ và bộ định tuyến có địa chỉ MAC ngoài địa chỉ lớp mạng. Đầu tiên, mạng LAN được thiết kế cho các giao thức lớp mạng tùy ý, không chỉ dành cho IP và Internet. Nếu bộ điều hợp được chỉ định địa chỉ IP thay vì địa chỉ MAC "trung tính" thì bộ điều hợp sẽ không dễ dàng hỗ trợ các giao thức lớp mạng khác (ví dụ: IPX hoặc DECnet). Thứ hai, nếu bộ điều hợp sử dụng địa chỉ lớp mạng thay vì địa chỉ MAC thì địa chỉ lớp mạng sẽ phải được lưu trữ trong RAM bộ điều hợp và được cấu hình lại mỗi khi bộ điều hợp được di chuyển (hoặc bật nguồn). Một tùy chọn khác là không sử dụng bất kỳ địa chỉ nào trong bộ điều hợp và yêu cầu mỗi bộ điều hợp chuyển dữ liệu (thường là một gói dữ liệu IP) của mỗi khung mà nó nhận được trong ngăn xếp giao thức. Lớp mạng sau đó có thể kiểm tra địa chỉ lớp mạng phù hợp. Một vấn đề với tùy chọn này là máy chủ sẽ bị gián đoạn bởi mọi khung hình được gửi trên mạng LAN, bao gồm cả các khung hình được dành cho các máy chủ khác trên cùng mạng LAN quảng bá. Tóm lại, để các lớp trở thành các khối xây dựng độc lập phần lớn trong kiến ​​trúc mạng, các lớp khác nhau cần có sơ đồ địa chỉ riêng. Hiện tại chúng ta đã thấy ba loại địa chỉ: tên máy chủ cho lớp ứng dụng, địa chỉ IP cho lớp mạng và địa chỉ MAC cho lớp liên kết.

NGUYÊN TẮC TRONG THỰC HÀNH

ký hiệu và địa chỉ MAC được hiển thị bằng ký hiệu thập lục phân. Vì mục đích của cuộc thảo luận này, trong phần này chúng ta sẽ giả định rằng switch phát tất cả các khung; nghĩa là, bất cứ khi nào một switch nhận được một khung trên một giao diện, nó sẽ chuyển tiếp khung đó trên tất cả các giao diện khác của nó. Trong phần tiếp theo, chúng tôi sẽ cung cấp giải thích chính xác hơn về cách thức hoạt động của các switch.

Bây giờ, giả sử máy chủ có địa chỉ IP 222.222.222.220 muốn gửi một datagram IP tới máy chủ 222.222.222.222. Trong ví dụ này, cả nguồn và đích đều nằm trong cùng một mạng con, theo cách đánh địa chỉ của Phần 4.3.3. Để gửi một datagram, nguồn phải cung cấp cho bộ điều hợp của nó không chỉ IP datagram mà còn cả địa chỉ MAC cho đích 222.222.222.222. Bộ điều hợp gửi sau đó sẽ xây dựng khung lớp liên kết chứa địa chỉ MAC của đích và gửi khung vào mạng LAN.

Câu hỏi quan trọng được giải quyết trong phần này là Máy chủ gửi xác định địa chỉ MAC cho máy chủ đích có địa chỉ IP 222.222.222.222 như thế nào? Như bạn có thể đoán, nó sử dụng ARP. Mô-đun ARP trong máy chủ gửi sẽ lấy bất kỳ địa chỉ IP nào trên cùng mạng LAN làm đầu vào và trả về địa chỉ MAC tương ứng. Trong ví dụ hiện tại, máy chủ gửi 222.222.222.220 cung cấp mô-đun ARP của nó địa chỉ IP 222.222.222.222 và mô-đun ARP trả về địa chỉ MAC tương ứng 49-BD-D2-C7-56-2A.

Vì vậy, chúng tôi thấy rằng ARP phân giải địa chỉ IP thành địa chỉ MAC. Theo nhiều cách, nó tương tự như DNS (được nghiên cứu ở Phần 2.5), phân giải tên máy chủ thành địa chỉ IP. Tuy nhiên, một điểm khác biệt quan trọng giữa hai trình phân giải là DNS phân giải tên máy chủ cho các máy chủ ở bất kỳ đâu trên Internet, trong khi ARP chỉ phân giải địa chỉ IP cho các máy chủ và giao diện bộ định tuyến trên cùng một mạng con. Nếu một nút ở California cố gắng sử dụng ARP để phân giải địa chỉ IP cho một nút ở Mississippi, ARP sẽ trả về lỗi.

*Hình 6.17 ♦ Mỗi giao diện trên mạng LAN có địa chỉ IP và MAC*

Địa chỉ

IP:222.222.222.221

IP:222.222.222.220

IP:222.222.222.223

IP:222.222.222.222

5C-66-AB-90-75-B1

1A-23-F9-CD-06-9B

49-BD-D2-C7-56-2A

88-B2-2F-54-1A-0F

MỘT

B

C

Bây giờ chúng ta đã giải thích ARP làm gì, hãy xem cách nó hoạt động. Mỗi máy chủ và bộ định tuyến có một bảng ARP trong bộ nhớ, bảng này chứa ánh xạ các địa chỉ IP tới địa chỉ MAC. Hình 6.18 cho thấy bảng ARP trong máy chủ 222.222.222.220 trông như thế nào. Bảng ARP cũng chứa giá trị thời gian tồn tại (TTL), cho biết thời điểm mỗi ánh xạ sẽ bị xóa khỏi bảng. Lưu ý rằng một bảng không nhất thiết phải chứa mục nhập cho mọi máy chủ và bộ định tuyến trên mạng con; một số có thể chưa bao giờ được nhập vào bảng và một số khác có thể đã hết hạn. Thời gian hết hạn thông thường cho một mục nhập là 20 phút kể từ khi mục nhập đó được đặt vào bảng ARP.

Bây giờ, giả sử rằng máy chủ 222.222.222.220 muốn gửi một datagram có địa chỉ IP đến một máy chủ hoặc bộ định tuyến khác trên mạng con đó. Máy chủ gửi cần lấy địa chỉ MAC của đích được cung cấp địa chỉ IP. Nhiệm vụ này thật dễ dàng nếu bảng ARP của người gửi có mục nhập cho nút đích. Nhưng điều gì sẽ xảy ra nếu bảng ARP hiện không có mục nhập cho đích đến? Cụ thể, giả sử 222.222.222.220 muốn gửi datagram tới 222.222.222.222. Trong trường hợp này, người gửi sử dụng giao thức ARP để phân giải địa chỉ. Đầu tiên, người gửi xây dựng một gói đặc biệt gọi là gói ARP. Gói ARP có một số trường, bao gồm gửi và nhận IP và địa chỉ MAC. Cả gói truy vấn và phản hồi ARP đều có cùng định dạng. Mục đích của gói truy vấn ARP là truy vấn tất cả các máy chủ và bộ định tuyến khác trên mạng con để xác định địa chỉ MAC tương ứng với địa chỉ IP đang được giải quyết.

Quay lại ví dụ của chúng tôi, 222.222.222.220 chuyển gói truy vấn ARP tới bộ điều hợp cùng với dấu hiệu cho thấy bộ điều hợp sẽ gửi gói đến địa chỉ quảng bá MAC, cụ thể là FF-FF-FF-FF-FF-FF. Bộ điều hợp đóng gói gói ARP trong khung lớp liên kết, sử dụng địa chỉ quảng bá cho địa chỉ đích của khung và truyền khung vào mạng con. Hãy nhớ lại sự tương tự về số an sinh xã hội/địa chỉ bưu chính của chúng ta, một truy vấn ARP tương đương với việc một người hét lên trong một căn phòng đông đúc gồm nhiều ngăn ở một công ty nào đó (chẳng hạn như AnyCorp): "Số an sinh xã hội của người có địa chỉ bưu chính là Cubicle 13, Room 112, AnyCorp, Palo Alto, California?" Khung chứa truy vấn ARP được tất cả các bộ điều hợp khác trên mạng con nhận và (do địa chỉ quảng bá) mỗi bộ điều hợp chuyển gói ARP trong khung tới mô-đun ARP của nó. Mỗi mô-đun ARP này sẽ kiểm tra xem địa chỉ IP của nó có khớp với địa chỉ IP đích trong gói ARP hay không. Người có kết quả trùng khớp sẽ gửi lại máy chủ truy vấn một gói ARP phản hồi với ánh xạ mong muốn. Sau đó, máy chủ truy vấn 222.222.222.220 có thể cập nhật bảng ARP của nó và gửi gói dữ liệu IP của nó, được đóng gói trong khung lớp liên kết có MAC đích là máy chủ hoặc bộ định tuyến phản hồi truy vấn ARP trước đó.

*Hình 6.18 ♦ Có thể có bảng ARP trong 222.222.222.220*

IP Địa chỉ MAC Địa chỉ TTL

222.222.222.221 88-B2-2F-54-1A-0F 13:45:00

222.222.222.223 5C-66-AB-90-75-B1 13:52:00

Có một số điều thú vị cần lưu ý về giao thức ARP. Đầu tiên, tin nhắn truy vấn ARP được gửi trong khung phát sóng, trong khi tin nhắn phản hồi ARP được gửi trong khung tiêu chuẩn. Trước khi đọc tiếp, bạn nên suy nghĩ tại sao lại như vậy. Thứ hai, ARP là plug-and-play; nghĩa là, bảng ARP được tạo tự động---nó không cần phải được quản trị viên hệ thống định cấu hình. Và nếu một máy chủ bị ngắt kết nối khỏi mạng con, mục nhập của nó cuối cùng sẽ bị xóa khỏi các bảng ARP khác trong mạng con.

Học sinh thường thắc mắc ARP là giao thức lớp liên kết hay giao thức lớp mạng. Như chúng ta đã thấy, gói ARP được gói gọn trong khung lớp liên kết và do đó nằm về mặt kiến ​​trúc phía trên lớp liên kết. Tuy nhiên, gói ARP có các trường chứa địa chỉ lớp liên kết và do đó được cho là giao thức lớp liên kết, nhưng nó cũng chứa địa chỉ lớp mạng và do đó cũng được cho là giao thức lớp mạng. Cuối cùng, ARP có lẽ tốt nhất nên được coi là một giao thức nằm giữa ranh giới giữa các lớp liên kết và mạng---không vừa khít với ngăn xếp giao thức phân lớp đơn giản mà chúng ta đã nghiên cứu trong Chương 1. Đó là sự phức tạp của các giao thức trong thế giới thực!

Đang gửi Datagram từ Subnet

Bây giờ đã rõ cách ARP hoạt động khi một máy chủ muốn gửi một datagram đến một máy chủ khác trên cùng mạng con. Nhưng bây giờ chúng ta hãy xem xét tình huống phức tạp hơn khi một máy chủ trên mạng con muốn gửi một datagram lớp mạng đến một máy chủ ngoài mạng con (nghĩa là qua một bộ định tuyến đến một mạng con khác). Chúng ta hãy thảo luận vấn đề này trong bối cảnh Hình 6.19, minh họa một mạng đơn giản bao gồm hai mạng con được kết nối với nhau bởi một bộ định tuyến.

Có một số điều thú vị cần lưu ý về Hình 6.19. Mỗi máy chủ có chính xác một địa chỉ IP và một bộ điều hợp. Tuy nhiên, như đã thảo luận trong Chương 4, bộ định tuyến có địa chỉ IP cho mỗi giao diện của nó. Đối với mỗi giao diện bộ định tuyến cũng có mô-đun ARP (trong bộ định tuyến) và bộ điều hợp. Vì bộ định tuyến trong Hình 6.19 có hai giao diện nên nó có hai địa chỉ IP, hai mô-đun ARP và hai bộ điều hợp. Tất nhiên, mỗi bộ chuyển đổi trong mạng đều có địa chỉ MAC riêng.

*Hình 6.19 ♦ Hai mạng con được kết nối với nhau bằng bộ định tuyến*

IP:111.111.111.110 IP:111.111.111.111

IP:111.111.111.112

IP:222.222.222.221

IP:222.222.222.222

74-29-9C-E8-FF-55

CC-49-DE-D0-AB-7D

E6-E9-00-17-BB-4B

1A-23-F9-CD-06-9B IP:222.222.222.220

88-B2-2F-54-1A-0F

49-BD-D2-C7-56-2A

Cũng lưu ý rằng Subnet 1 có địa chỉ mạng 111.111.111/24 và Subnet 2 có địa chỉ mạng 222.222.222/24. Do đó, tất cả các giao diện được kết nối với Subnet 1 đều có địa chỉ có dạng 111.111.111.xxx và tất cả các giao diện được kết nối với Subnet 2 đều có địa chỉ có dạng 222.222.222.xxx.

Bây giờ, hãy xem xét cách máy chủ trên Subnet 1 gửi gói dữ liệu đến máy chủ trên Subnet 2. Cụ thể, giả sử máy chủ 111.111.111.111 muốn gửi gói dữ liệu IP đến máy chủ 222.222.222.222. Máy chủ gửi chuyển gói dữ liệu tới bộ điều hợp của nó như thường lệ. Nhưng máy chủ gửi cũng phải chỉ ra cho bộ điều hợp của nó một địa chỉ MAC đích thích hợp. Bộ chuyển đổi nên sử dụng địa chỉ MAC nào? Người ta có thể đoán rằng địa chỉ MAC thích hợp là địa chỉ của bộ chuyển đổi dành cho máy chủ 222.222.222.222, cụ thể là 49-BD-D2-C7-56-2A. Tuy nhiên, suy đoán này sẽ sai! Nếu bộ điều hợp gửi sử dụng địa chỉ MAC đó thì không có bộ điều hợp nào trên Subnet 1 bận tâm chuyển gói dữ liệu IP lên lớp mạng của nó, vì địa chỉ đích của khung sẽ không khớp với địa chỉ MAC của bất kỳ bộ điều hợp nào trên Subnet 1. Gói dữ liệu sẽ chết và đi đến thiên đường gói dữ liệu.

Nếu xem xét kỹ Hình 6.19, chúng ta sẽ thấy rằng để một datagram đi từ 111.111.111.111 đến máy chủ trên Subnet 2, datagram trước tiên phải được gửi đến giao diện bộ định tuyến 111.111.111.110, đó là địa chỉ IP của bộ định tuyến bước nhảy đầu tiên trên đường dẫn đến đích cuối cùng. Do đó, địa chỉ MAC thích hợp cho khung là địa chỉ của bộ điều hợp cho giao diện bộ định tuyến 111.111.111.110, cụ thể là E6-E9-00-17BB-4B. Làm cách nào máy chủ gửi có được địa chỉ MAC của 111.111.111.110? Tất nhiên là bằng cách sử dụng ARP! Sau khi bộ điều hợp gửi có địa chỉ MAC này, nó sẽ tạo một khung (chứa datagram có địa chỉ tới 222.222.222.222) và gửi khung vào Subnet 1. Bộ điều hợp bộ định tuyến trên Subnet 1 thấy rằng khung lớp liên kết được gửi đến nó và do đó chuyển khung này đến lớp mạng của bộ định tuyến. Hoan hô---gram dữ liệu IP đã được di chuyển thành công từ máy chủ nguồn sang bộ định tuyến! Nhưng chúng tôi chưa kết thúc. Chúng ta vẫn phải di chuyển datagram từ bộ định tuyến đến đích. Bộ định tuyến bây giờ phải xác định giao diện chính xác mà datagram sẽ được chuyển tiếp. Như đã thảo luận trong Chương 4, việc này được thực hiện bằng cách tham khảo bảng chuyển tiếp trong bộ định tuyến. Bảng chuyển tiếp cho bộ định tuyến biết rằng datagram sẽ được chuyển tiếp qua giao diện bộ định tuyến 222.222.222.220. Sau đó, giao diện này chuyển gói dữ liệu đến bộ điều hợp của nó, bộ điều hợp này sẽ đóng gói gói dữ liệu trong một khung mới và gửi khung vào Subnet 2. Lần này, địa chỉ MAC đích của khung thực sự là địa chỉ MAC của đích cuối cùng. Và làm thế nào để bộ định tuyến có được địa chỉ MAC đích này? Tất nhiên là từ ARP!

ARP cho Ethernet được định nghĩa trong RFC 826. Phần giới thiệu hay về ARP được đưa ra trong hướng dẫn TCP/IP, RFC 1180. Chúng ta sẽ khám phá ARP chi tiết hơn trong các bài tập về nhà.

**6.4.2 Ethernet**

Ethernet đã chiếm lĩnh khá nhiều thị trường mạng LAN có dây. Trong những năm 1980 và đầu những năm 1990, Ethernet phải đối mặt với nhiều thách thức từ các công nghệ LAN khác, bao gồm

vòng mã thông báo, FDDI và ATM. Một số công nghệ khác đã thành công trong việc chiếm lĩnh một phần thị trường mạng LAN trong một vài năm. Nhưng kể từ khi được phát minh vào giữa những năm 1970, Ethernet đã tiếp tục phát triển và giữ vững vị trí thống trị của mình. Ngày nay, Ethernet cho đến nay là công nghệ mạng LAN có dây phổ biến nhất và có thể nó sẽ vẫn như vậy trong tương lai gần. Người ta có thể nói rằng Ethernet đã có mặt trong mạng cục bộ giống như Internet đã có mặt trong mạng toàn cầu.

Có nhiều lý do dẫn đến thành công của Ethernet. Đầu tiên, Ethernet là mạng LAN tốc độ cao được triển khai rộng rãi đầu tiên. Bởi vì nó được triển khai sớm nên các quản trị viên mạng đã trở nên quen thuộc với Ethernet---những điều kỳ diệu cũng như những điểm kỳ quặc của nó---và không muốn chuyển sang các công nghệ LAN khác khi chúng xuất hiện. Thứ hai, vòng token, FDDI và ATM phức tạp hơn và đắt tiền hơn Ethernet, điều này càng khiến các quản trị viên mạng không muốn chuyển đổi. Thứ ba, lý do thuyết phục nhất để chuyển sang công nghệ LAN khác (chẳng hạn như FDDI hoặc ATM) thường là tốc độ dữ liệu cao hơn của công nghệ mới; tuy nhiên, Ethernet luôn chống trả, tạo ra các phiên bản hoạt động ở tốc độ dữ liệu bằng hoặc cao hơn. Ethernet chuyển mạch cũng được giới thiệu vào đầu những năm 1990, giúp tăng thêm tốc độ dữ liệu hiệu quả. Cuối cùng, vì Ethernet đã quá phổ biến nên phần cứng Ethernet (đặc biệt là bộ điều hợp và bộ chuyển mạch) đã trở thành một mặt hàng và có giá cực kỳ rẻ.

Mạng LAN Ethernet ban đầu được phát minh vào giữa những năm 1970 bởi Bob Metcalfe và David Boggs. Mạng LAN Ethernet ban đầu sử dụng bus đồng trục để kết nối các nút. Cấu trúc liên kết bus cho Ethernet thực sự đã tồn tại trong suốt những năm 1980 và giữa những năm 1990. Ethernet với cấu trúc liên kết bus là một mạng LAN quảng bá---tất cả các khung được truyền sẽ di chuyển đến và được xử lý bởi tất cả các bộ điều hợp được kết nối với bus. Hãy nhớ lại rằng chúng ta đã trình bày giao thức đa truy cập CSMA/CD của Ethernet với độ trễ hàm mũ nhị phân trong Phần 6.3.2.

Vào cuối những năm 1990, hầu hết các công ty và trường đại học đã thay thế mạng LAN của họ bằng cài đặt Ethernet bằng cấu trúc liên kết hình sao dựa trên trung tâm. Trong cài đặt như vậy, các máy chủ (và bộ định tuyến) được kết nối trực tiếp với một hub bằng dây đồng xoắn đôi. Hub là một thiết bị lớp vật lý hoạt động trên các bit riêng lẻ chứ không phải trên các khung. Khi một bit, đại diện cho số 0 hoặc số 1, đến từ một giao diện, trung tâm chỉ cần tạo lại bit đó, tăng cường độ năng lượng của nó và truyền bit đó đến tất cả các giao diện khác. Do đó, Ethernet với cấu trúc liên kết hình sao dựa trên trung tâm cũng là một mạng LAN quảng bá---bất cứ khi nào một trung tâm nhận được một bit từ một trong các giao diện của nó, nó sẽ gửi một bản sao trên tất cả các giao diện khác của nó. Đặc biệt, nếu một hub nhận các khung từ hai giao diện khác nhau cùng một lúc thì sẽ xảy ra xung đột và các nút tạo khung phải truyền lại.

Vào đầu những năm 2000, Ethernet đã trải qua một sự thay đổi mang tính tiến hóa lớn khác. Việc cài đặt Ethernet tiếp tục sử dụng cấu trúc liên kết hình sao, nhưng trung tâm ở trung tâm đã được thay thế bằng một bộ chuyển mạch. Chúng ta sẽ xem xét sâu hơn về Ethernet chuyển mạch ở phần sau của chương này. Hiện tại, chúng tôi chỉ đề cập rằng một bộ chuyển mạch không chỉ "không va chạm" mà còn là một bộ chuyển mạch gói lưu trữ và chuyển tiếp thực sự; nhưng không giống như các bộ định tuyến hoạt động qua lớp 3, một bộ chuyển mạch chỉ hoạt động qua lớp 2.

Cấu trúc Ethernet Frame

Chúng ta có thể tìm hiểu nhiều về Ethernet bằng cách kiểm tra khung Ethernet, được hiển thị trong Hình 6.20. Để làm cho cuộc thảo luận này về khung Ethernet trở thành một bối cảnh hữu hình, hãy xem xét việc gửi một gói dữ liệu IP từ máy chủ này đến máy chủ khác, với cả hai máy chủ trên cùng một mạng LAN Ethernet (ví dụ: mạng LAN Ethernet trong Hình 6.17.) (Mặc dù tải trọng của khung Ethernet của chúng tôi là một gói dữ liệu IP, chúng tôi lưu ý rằng khung Ethernet cũng có thể mang các gói lớp mạng khác.) Hãy để bộ chuyển đổi gửi, bộ chuyển đổi A, có địa chỉ MAC AA-AA-AA-AA-AA-AA và bộ chuyển đổi nhận, bộ chuyển đổi B, có địa chỉ MAC BB-BB-BB-BB-BB-BB. Bộ điều hợp gửi đóng gói gói dữ liệu IP trong khung Ethernet và chuyển khung đó đến lớp vật lý. Bộ điều hợp nhận nhận khung từ lớp vật lý, trích xuất gói dữ liệu IP và chuyển gói dữ liệu IP đến lớp mạng. Trong bối cảnh này, bây giờ chúng ta hãy xem xét sáu trường của khung Ethernet, như trong Hình 6.20.

• Trường dữ liệu (46 đến 1.500 byte). Trường này mang datagram IP. Đơn vị truyền tải tối đa (MTU) của Ethernet là 1.500 byte. Điều này có nghĩa là nếu datagram IP vượt quá 1.500 byte thì máy chủ phải phân mảnh datagram đó, như đã thảo luận trong Phần 4.3.2. Kích thước tối thiểu của trường dữ liệu là 46 byte. Điều này có nghĩa là nếu gói dữ liệu IP nhỏ hơn 46 byte thì trường dữ liệu phải được \"nhồi\" để điền vào 46 byte. Khi sử dụng tính năng nhồi, dữ liệu được chuyển đến lớp mạng sẽ chứa nội dung nhồi cũng như gói dữ liệu IP. Lớp mạng sử dụng trường độ dài trong tiêu đề gói dữ liệu IP để loại bỏ nội dung nhồi nhét. • Địa chỉ đích (6 byte). Trường này chứa địa chỉ MAC của bộ điều hợp đích, BB-BB-BB-BB-BB-BB. Khi bộ điều hợp B nhận được khung Ethernet có địa chỉ đích là BB-BB-BB-BB-BB-BB hoặc địa chỉ quảng bá MAC, nó sẽ chuyển nội dung của trường dữ liệu của khung đến lớp mạng; nếu nó nhận được một khung có bất kỳ địa chỉ MAC nào khác, nó sẽ loại bỏ khung đó. • Địa chỉ nguồn (6 byte). Trường này chứa địa chỉ MAC của bộ điều hợp truyền khung vào mạng LAN, trong ví dụ này là AA-AA-AA-AA-AA-AA. • Trường gõ (2 byte). Trường loại cho phép Ethernet ghép các giao thức lớp mạng. Để hiểu điều này, chúng ta cần lưu ý rằng máy chủ có thể sử dụng các giao thức lớp mạng khác ngoài IP. Trong thực tế, một máy chủ nhất định có thể hỗ trợ nhiều giao thức lớp mạng sử dụng các giao thức khác nhau cho các ứng dụng khác nhau.

*Hình 6.20 ♦ Cấu trúc khung Ethernet*

Lời nói đầu CRC Đích. Địa chỉ

Địa chỉ nguồn

Kiểu

dữ liệu

Vì lý do này, khi khung Ethernet đến bộ điều hợp B, bộ điều hợp B cần biết giao thức lớp mạng nào sẽ chuyển (nghĩa là phân kênh) nội dung của trường dữ liệu. IP và các giao thức lớp mạng khác (ví dụ: Novell IPX hoặc AppleTalk), mỗi giao thức đều có số loại được tiêu chuẩn hóa riêng. Hơn nữa, giao thức ARP (được thảo luận trong phần trước) có số loại riêng và nếu khung đến chứa gói ARP (tức là có trường loại 0806 thập lục phân), gói ARP sẽ được phân kênh theo giao thức ARP. Lưu ý rằng trường loại tương tự với trường giao thức trong gói dữ liệu lớp mạng và trường số cổng trong phân đoạn lớp vận chuyển; tất cả các trường này dùng để gắn giao thức ở một lớp với giao thức ở lớp trên. • Kiểm tra dự phòng theo chu kỳ (CRC) (4 byte). Như đã thảo luận trong Phần 6.2.3, mục đích của trường CRC là cho phép bộ điều hợp nhận, bộ điều hợp B, phát hiện các lỗi bit trong khung. • Lời mở đầu (8 byte). Khung Ethernet bắt đầu bằng trường mở đầu 8 byte. Mỗi byte trong số 7 byte đầu tiên của phần mở đầu có giá trị 10101010; byte cuối cùng là 10101011. 7 byte đầu tiên của phần mở đầu dùng để "đánh thức" các bộ điều hợp nhận và đồng bộ hóa đồng hồ của chúng với đồng hồ của người gửi. Tại sao đồng hồ không đồng bộ? Hãy nhớ rằng bộ điều hợp A nhằm mục đích truyền khung ở tốc độ 10 Mbps, 100 Mbps hoặc 1 Gbps, tùy thuộc vào loại mạng LAN Ethernet. Tuy nhiên, vì không có gì là hoàn hảo tuyệt đối nên bộ chuyển đổi A sẽ không truyền khung hình đúng tốc độ mục tiêu; sẽ luôn có một số sai lệch so với tốc độ mục tiêu, một sự chênh lệch mà các bộ điều hợp khác trên mạng LAN không biết trước. Bộ điều hợp nhận có thể khóa đồng hồ của bộ điều hợp A chỉ bằng cách khóa các bit trong 7 byte đầu tiên của phần mở đầu. 2 bit cuối cùng của byte thứ tám của phần mở đầu (hai bit 1 liên tiếp đầu tiên) cảnh báo adapter B rằng "thứ quan trọng" sắp đến.

Tất cả các công nghệ Ethernet đều cung cấp dịch vụ không kết nối cho lớp mạng. Nghĩa là, khi bộ điều hợp A muốn gửi một datagram đến bộ điều hợp B, bộ điều hợp A sẽ đóng gói datagram đó trong khung Ethernet và gửi khung đó vào mạng LAN mà không cần bắt tay trước với bộ điều hợp B. Dịch vụ không kết nối lớp 2 này tương tự như dịch vụ datagram lớp 3 của IP và dịch vụ không kết nối lớp 4 của UDP.

Công nghệ Ethernet cung cấp dịch vụ không đáng tin cậy cho lớp mạng. Cụ thể, khi bộ chuyển đổi B nhận được khung từ bộ chuyển đổi A, nó sẽ chạy khung thông qua kiểm tra CRC, nhưng không gửi xác nhận khi khung vượt qua kiểm tra CRC cũng như không gửi xác nhận phủ định khi khung không vượt qua kiểm tra CRC. Khi một khung không vượt qua được quá trình kiểm tra CRC, bộ chuyển đổi B sẽ loại bỏ khung đó. Do đó, bộ chuyển đổi A không biết liệu khung truyền của nó có đến được bộ chuyển đổi B và vượt qua kiểm tra CRC hay không. Việc thiếu phương tiện truyền tải đáng tin cậy (ở lớp liên kết) giúp làm cho Ethernet trở nên đơn giản và rẻ tiền. Nhưng điều đó cũng có nghĩa là luồng datagram truyền đến lớp mạng có thể có những khoảng trống.

Nếu có khoảng trống do khung Ethernet bị loại bỏ, ứng dụng tại Host B có thấy khoảng trống không? Như chúng ta đã tìm hiểu ở Chương 3, điều này phụ thuộc vào việc ứng dụng đang sử dụng UDP hay TCP. Nếu ứng dụng đang sử dụng UDP thì ứng dụng trong Host B thực sự sẽ thấy các khoảng trống trong dữ liệu. Mặt khác, nếu ứng dụng đang sử dụng TCP thì TCP trong Host B sẽ không thừa nhận dữ liệu chứa trong các khung bị loại bỏ, khiến TCP trong Host A truyền lại. Lưu ý rằng khi TCP truyền lại dữ liệu, dữ liệu cuối cùng sẽ quay trở lại bộ điều hợp Ethernet nơi nó bị loại bỏ. Do đó, theo nghĩa này, Ethernet thực hiện truyền lại dữ liệu, mặc dù Ethernet không biết liệu nó đang truyền một gói dữ liệu hoàn toàn mới với dữ liệu hoàn toàn mới hay một gói dữ liệu chứa dữ liệu đã được truyền ít nhất một lần.

Công nghệ Ethernet

Trong cuộc thảo luận ở trên, chúng tôi đã đề cập đến Ethernet như thể nó là một tiêu chuẩn giao thức duy nhất. Nhưng trên thực tế, Ethernet có nhiều loại khác nhau, với những từ viết tắt hơi gây nhầm lẫn như 10BASE-T, 10BASE-2, 100BASE-T, 1000BASE-LX,

BOB METCALFE VÀ ETHERNET

Là nghiên cứu sinh tiến sĩ tại Đại học Harvard vào đầu những năm 1970, Bob Metcalfe đã làm việc trên ARPAnet tại MIT. Trong quá trình học, anh cũng được tiếp xúc với công việc của Abramson về ALOHA và các giao thức truy cập ngẫu nhiên. Sau khi hoàn thành bằng tiến sĩ và ngay trước khi bắt đầu công việc tại Trung tâm nghiên cứu Xerox Palo Alto (Xerox PARC), anh đã đến thăm Abramson và các đồng nghiệp tại Đại học Hawaii trong ba tháng, để có cái nhìn trực tiếp về ALOHAnet. Tại Xerox PARC, Metcalfe được tiếp xúc với máy tính Alto, loại máy tính này về nhiều mặt là tiền thân của máy tính cá nhân những năm 1980. Metcalfe nhận thấy sự cần thiết phải nối mạng các máy tính này theo cách không tốn kém. Được trang bị kiến ​​thức về ARPAnet, ALOHAnet và các giao thức truy cập ngẫu nhiên, Metcalfe---cùng với đồng nghiệp David Boggs---đã phát minh ra Ethernet.

Ethernet ban đầu của Metcalfe và Boggs chạy ở tốc độ 2,94 Mbps và liên kết tới 256 máy chủ cách nhau tới một dặm. Metcalfe và Boggs đã thành công trong việc thuyết phục hầu hết các nhà nghiên cứu tại Xerox PARC giao tiếp thông qua máy tính Alto của họ. Metcalfe sau đó đã tạo dựng một liên minh giữa Xerox, Digital và Intel để thiết lập Ethernet thành tiêu chuẩn Ethernet 10 Mbps, được IEEE phê chuẩn. Xerox không tỏ ra quan tâm nhiều đến việc thương mại hóa Ethernet. Năm 1979, Metcalfe thành lập công ty riêng của mình, 3Com, chuyên phát triển và thương mại hóa công nghệ mạng, bao gồm cả công nghệ Ethernet. Đặc biệt, 3Com đã phát triển và tiếp thị các card Ethernet vào đầu những năm 1980 cho các máy tính IBM cực kỳ phổ biến.

LỊCH SỬ TRƯỜNG HỢP

10GBASE-T và 40GBASE-T. Những công nghệ này và nhiều công nghệ Ethernet khác đã được chuẩn hóa trong nhiều năm bởi nhóm làm việc IEEE 802.3 CSMA/CD (Ethernet) \[IEEE 802.3 2020\]. Mặc dù những từ viết tắt này có vẻ gây nhầm lẫn nhưng thực sự có một trật tự đáng kể ở đây. Phần đầu tiên của từ viết tắt đề cập đến tốc độ của tiêu chuẩn: 10, 100, 1000 hoặc 10G, tương ứng là 10 Megabit (mỗi giây), 100 Megabit, Gigabit, 10 Gigabit và 40 Gigibit Ethernet. "BASE" dùng để chỉ Ethernet băng cơ sở, nghĩa là phương tiện vật lý chỉ mang lưu lượng Ethernet; hầu hết tất cả các tiêu chuẩn 802.3 đều dành cho Ethernet băng cơ sở. Phần cuối cùng của từ viết tắt đề cập đến chính phương tiện vật lý; Ethernet vừa là đặc điểm kỹ thuật của lớp liên kết vừa là lớp vật lý và được truyền qua nhiều phương tiện vật lý khác nhau bao gồm cáp đồng trục, dây đồng và cáp quang. Nói chung, chữ "T" dùng để chỉ dây đồng xoắn đôi.

Trong lịch sử, Ethernet ban đầu được hình thành như một đoạn cáp đồng trục. Các tiêu chuẩn 10BASE-2 và 10BASE-5 đời đầu chỉ định Ethernet 10 Mbps qua hai loại cáp đồng trục, mỗi loại có chiều dài giới hạn ở 500 mét. Có thể đạt được thời gian chạy dài hơn bằng cách sử dụng bộ lặp - một thiết bị lớp vật lý nhận tín hiệu ở phía đầu vào và tái tạo tín hiệu ở phía đầu ra. Cáp đồng trục rất phù hợp với quan điểm của chúng tôi về Ethernet như một phương tiện quảng bá---tất cả các khung được truyền bởi một giao diện đều được nhận ở các giao diện khác và giao thức CDMA/CD của Ethernet giải quyết tốt vấn đề đa truy cập. Các nút chỉ cần gắn vào cáp và thì đấy, chúng ta có một mạng cục bộ!

Ethernet đã trải qua một loạt các bước phát triển trong nhiều năm và Ethernet ngày nay rất khác so với các thiết kế cấu trúc liên kết bus ban đầu sử dụng cáp đồng trục. Trong hầu hết các cài đặt hiện nay, các nút được kết nối với một bộ chuyển mạch thông qua các đoạn điểm-điểm được làm bằng dây đồng xoắn đôi hoặc cáp quang, như trong Hình 6.15--6.17.

Vào giữa những năm 1990, Ethernet được chuẩn hóa ở tốc độ 100 Mbps, nhanh hơn 10 lần so với Ethernet 10 Mbps. Giao thức Ethernet MAC ban đầu và định dạng khung được giữ nguyên nhưng các lớp vật lý tốc độ cao hơn được xác định cho dây đồng (100BASE-T) và cáp quang (100BASE-FX, 100BASE-SX, 100BASE-BX). Hình 6.21 cho thấy các tiêu chuẩn khác nhau này cũng như giao thức Ethernet MAC và định dạng khung phổ biến. Ethernet 100 Mbps được giới hạn ở khoảng cách 100 mét trên đôi dây xoắn và

Thuộc vật chất

Chuyên chở

Mạng

liên kết

Ứng dụng

100BASE-TX

100BASE-T4

100BASE-T2

Giao thức MAC và định dạng khung

100BASE-SX

100BASE-FX

100BASE-BX

*Hình 6.21 ♦ Chuẩn Ethernet 100 Mbps: Lớp liên kết chung,*

các lớp vật lý khác nhau

vài km qua cáp quang, cho phép kết nối các bộ chuyển mạch Ethernet ở các tòa nhà khác nhau.

Gigabit Ethernet là phần mở rộng của các tiêu chuẩn Ethernet 10 Mbps và 100 Mbps rất thành công. Cung cấp tốc độ dữ liệu thô 40.000 Mbps, 40 Gigabit Ethernet duy trì khả năng tương thích hoàn toàn với cơ sở thiết bị Ethernet khổng lồ được cài đặt. Tiêu chuẩn cho Gigabit Ethernet, được gọi là IEEE 802.3z, thực hiện như sau:

• Sử dụng định dạng khung Ethernet tiêu chuẩn (Hình 6.20) và tương thích ngược với công nghệ 10BASE-T và 100BASE-T. Điều này cho phép tích hợp dễ dàng Gigabit Ethernet với cơ sở thiết bị Ethernet được cài đặt hiện có. • Cho phép liên kết điểm-điểm cũng như các kênh quảng bá được chia sẻ. Liên kết điểm-điểm sử dụng bộ chuyển mạch trong khi các kênh quảng bá sử dụng hub, như được mô tả trước đó. Trong thuật ngữ Gigabit Ethernet, các trung tâm được gọi là nhà phân phối đệm. • Sử dụng CSMA/CD cho các kênh phát sóng chia sẻ. Để có hiệu quả chấp nhận được, khoảng cách tối đa giữa các nút phải được hạn chế nghiêm ngặt. • Cho phép hoạt động song công hoàn toàn ở tốc độ 40 Gbps theo cả hai hướng đối với các kênh điểm-điểm.

Ban đầu hoạt động trên cáp quang, Gigabit Ethernet hiện có thể chạy trên cáp UTP loại 5 (cho 1000BASE-T và 10GBASE-T).

Hãy kết thúc cuộc thảo luận của chúng ta về công nghệ Ethernet bằng cách đặt ra một câu hỏi có thể khiến bạn lo lắng. Vào thời của cấu trúc liên kết bus và cấu trúc liên kết hình sao dựa trên trung tâm, Ethernet rõ ràng là một liên kết quảng bá (như được định nghĩa trong Phần 6.3), trong đó xảy ra xung đột khung khi các nút được truyền cùng lúc. Để giải quyết những xung đột này, tiêu chuẩn Ethernet bao gồm giao thức CSMA/CD, đặc biệt hiệu quả đối với mạng LAN quảng bá có dây trải rộng trên một khu vực địa lý nhỏ. Nhưng nếu việc sử dụng Ethernet phổ biến ngày nay là cấu trúc liên kết hình sao dựa trên chuyển mạch, sử dụng chuyển mạch gói lưu trữ và chuyển tiếp, thì liệu có thực sự cần đến giao thức Ethernet MAC nữa không? Như chúng ta sẽ thấy ngay sau đây, một switch điều phối việc truyền của nó và không bao giờ chuyển tiếp nhiều hơn một khung hình trên cùng một giao diện vào bất kỳ lúc nào. Hơn nữa, các bộ chuyển mạch hiện đại là song công hoàn toàn, do đó mỗi bộ chuyển mạch và một nút có thể gửi các khung cho nhau cùng lúc mà không bị nhiễu. Nói cách khác, trong mạng LAN Ethernet dựa trên chuyển mạch không có xung đột và do đó không cần giao thức MAC!

Như chúng ta đã thấy, Ethernet ngày nay rất khác so với Ethernet ban đầu do Metcalfe và Boggs hình thành hơn 40 năm trước---tốc độ đã tăng gấp ba lần, khung Ethernet được truyền qua nhiều phương tiện khác nhau, Ethernet chuyển mạch đã trở nên thống trị và hiện nay ngay cả giao thức MAC cũng thường không cần thiết! Có phải tất cả những thứ này thực sự vẫn là Ethernet? Tất nhiên, câu trả lời là "có, theo định nghĩa". Tuy nhiên, điều thú vị cần lưu ý là thông qua tất cả những thay đổi này, có

thực sự đã là một hằng số lâu dài không thay đổi trong suốt 30 năm qua--- định dạng khung của Ethernet. Có lẽ đây chính là trung tâm thực sự và vượt thời gian của tiêu chuẩn Ethernet.

**6.4.3 Lớp liên kết Switches**

Cho đến thời điểm này, chúng ta vẫn cố tình mơ hồ về chức năng thực sự của một công tắc và cách thức hoạt động của nó. Vai trò của bộ chuyển mạch là nhận các khung lớp liên kết đến và chuyển tiếp chúng đến các liên kết gửi đi; chúng ta sẽ nghiên cứu chi tiết chức năng chuyển tiếp này trong tiểu mục này. Chúng ta sẽ thấy rằng bản thân bộ chuyển mạch là trong suốt đối với các máy chủ và bộ định tuyến trong mạng con; nghĩa là, máy chủ/bộ định tuyến gửi khung đến máy chủ/bộ định tuyến khác (thay vì gửi khung cho bộ chuyển mạch) và vui vẻ gửi khung vào mạng LAN mà không biết rằng bộ chuyển mạch sẽ nhận khung và chuyển tiếp nó. Tốc độ khung hình đến bất kỳ giao diện đầu ra nào của bộ chuyển mạch có thể tạm thời vượt quá dung lượng liên kết của giao diện đó. Để giải quyết vấn đề này, giao diện đầu ra của switch có bộ đệm, giống như cách giao diện đầu ra của bộ định tuyến có bộ đệm cho datagram. Bây giờ chúng ta hãy xem xét kỹ hơn cách hoạt động của switch.

Chuyển tiếp và lọc

Lọc là chức năng chuyển đổi xác định liệu một khung có nên được chuyển tiếp đến một giao diện nào đó hay chỉ nên loại bỏ. Chuyển tiếp là chức năng chuyển đổi xác định các giao diện mà khung sẽ được hướng tới và sau đó di chuyển khung đến các giao diện đó. Switch việc lọc và chuyển tiếp được thực hiện bằng bảng chuyển đổi. Bảng chuyển đổi chứa các mục nhập cho một số nhưng không nhất thiết là tất cả các máy chủ và bộ định tuyến trên mạng LAN. Một mục trong bảng chuyển đổi chứa (1) địa chỉ MAC, (2) giao diện chuyển đổi dẫn tới địa chỉ MAC đó và (3) thời điểm mục nhập được đặt trong bảng. Một bảng chuyển đổi ví dụ cho công tắc trên cùng trong Hình 6.15 được hiển thị trong Hình 6.22. Mô tả về chuyển tiếp khung này nghe có vẻ giống với thảo luận của chúng ta về chuyển tiếp datagram

*Hình 6.22 ♦ Một phần của bảng công tắc dành cho công tắc trên cùng trong*

*Hình 6.15*

Địa chỉ giao diện thời gian

62-FE-F7-11-89-A3 9:32

7C-BA-B2-B4-91-10 9:36

\.... \.... \...

trong Chương 4. Thật vậy, trong cuộc thảo luận về chuyển tiếp tổng quát ở Phần 4.4, chúng ta đã biết rằng nhiều bộ chuyển mạch gói hiện đại có thể được cấu hình để chuyển tiếp trên cơ sở địa chỉ MAC đích lớp 2 (tức là hoạt động như một bộ chuyển mạch lớp 2) hoặc địa chỉ đích lớp 3 IP (tức là hoạt động như một bộ định tuyến lớp 3). Tuy nhiên, chúng tôi sẽ phân biệt quan trọng việc chuyển tiếp các gói dựa trên địa chỉ MAC thay vì trên địa chỉ IP. Chúng ta cũng sẽ thấy rằng bảng chuyển mạch truyền thống (tức là trong ngữ cảnh không phải SDN) được xây dựng theo cách rất khác với bảng chuyển tiếp của bộ định tuyến.

Để hiểu cách lọc và chuyển tiếp switch hoạt động, giả sử một khung có địa chỉ đích DD-DD-DD-DD-DD-DD đến switch trên giao diện x. Switch lập chỉ mục bảng của nó bằng địa chỉ MAC DD-DD-DD-DD-DD-DD. Có ba trường hợp có thể xảy ra:

• Không có mục nào trong bảng cho DD-DD-DD-DD-DD-DD. Trong trường hợp này, switch chuyển tiếp các bản sao của khung tới bộ đệm đầu ra trước tất cả các giao diện ngoại trừ giao diện x. Nói cách khác, nếu không có mục nào cho địa chỉ đích, switch sẽ phát khung này. • Có một mục trong bảng liên kết DD-DD-DD-DD-DD-DD với giao diện x. Trong trường hợp này, khung đến từ phân đoạn mạng LAN có chứa bộ điều hợp DD-DD-DD-DD-DD-DD. Không cần chuyển tiếp khung tới bất kỳ giao diện nào khác, switch sẽ thực hiện chức năng lọc bằng cách loại bỏ khung. • Có một mục trong bảng, liên kết DD-DD-DD-DD-DD-DD với giao diện y≠x. Trong trường hợp này, khung cần được chuyển tiếp đến đoạn LAN gắn với giao diện y. Bộ chuyển mạch thực hiện chức năng chuyển tiếp của nó bằng cách đặt khung vào bộ đệm đầu ra trước giao diện y.

Chúng ta hãy xem qua các quy tắc này cho công tắc trên cùng trong Hình 6.15 và bảng chuyển đổi của nó trong Hình 6.22. Giả sử một khung có địa chỉ đích 62-FEF7-11-89-A3 đến switch từ giao diện 1. Switch kiểm tra bảng của nó và thấy rằng đích nằm trên đoạn LAN được kết nối với giao diện 1 (nghĩa là Kỹ thuật điện). Điều này có nghĩa là khung đã được phát trên đoạn LAN chứa đích. Do đó, switch lọc (nghĩa là loại bỏ) khung. Bây giờ, giả sử một khung có cùng địa chỉ đích đến từ giao diện 2. Switch lại kiểm tra bảng của nó và thấy rằng đích nằm ở hướng của giao diện 1; do đó, nó chuyển tiếp khung đến bộ đệm đầu ra trước giao diện 1. Từ ví dụ này, rõ ràng là miễn là bảng chuyển đổi hoàn chỉnh và chính xác, thì bộ chuyển mạch sẽ chuyển tiếp các khung tới đích mà không cần phát sóng.

Theo nghĩa này, switch "thông minh hơn" hub. Nhưng làm thế nào để bảng chuyển đổi này được cấu hình ngay từ đầu? Có giao thức định tuyến lớp liên kết nào tương đương với các giao thức định tuyến lớp mạng không? Hay người quản lý làm việc quá sức phải cấu hình bảng chuyển đổi theo cách thủ công?

Tự học

Bộ chuyển mạch có một đặc tính tuyệt vời (đặc biệt đối với quản trị viên mạng đã làm việc quá sức) là bảng của nó được xây dựng tự động, linh hoạt và tự chủ--- mà không cần bất kỳ sự can thiệp nào từ quản trị viên mạng hoặc từ giao thức cấu hình. Nói cách khác, switch có khả năng tự học. Khả năng này được thực hiện như sau:

1\. Bảng chuyển đổi ban đầu trống. 2. Đối với mỗi khung hình đến nhận được trên một giao diện, switch sẽ lưu vào bảng của nó

\(1\) địa chỉ MAC trong trường địa chỉ nguồn của khung, (2) giao diện nơi khung đến và (3) thời gian hiện tại. Theo cách này, switch ghi vào bảng của nó phân đoạn LAN nơi người gửi cư trú. Nếu cuối cùng mọi máy chủ trong mạng LAN đều gửi một khung thì cuối cùng mọi máy chủ sẽ được ghi vào bảng. 3. Switch sẽ xóa một địa chỉ trong bảng nếu không nhận được khung nào cùng với địa chỉ đó

địa chỉ làm địa chỉ nguồn sau một khoảng thời gian (thời gian lão hóa). Theo cách này, nếu một PC được thay thế bằng một PC khác (với bộ chuyển đổi khác), địa chỉ MAC của PC gốc cuối cùng sẽ bị xóa khỏi bảng chuyển đổi.

Hãy cùng tìm hiểu thuộc tính tự học của nút chuyển trên cùng trong Hình 6.15 và bảng chuyển đổi tương ứng của nó trong Hình 6.22. Giả sử tại thời điểm 9:39 một khung có địa chỉ nguồn 01-12-23-34-45-56 đến từ giao diện 2. Giả sử rằng địa chỉ này không có trong bảng chuyển đổi. Sau đó switch thêm một mục mới vào bảng, như trong Hình 6.23.

Tiếp tục với ví dụ tương tự này, giả sử rằng thời gian lão hóa cho bộ chuyển mạch này là 60 phút và không có khung nào có địa chỉ nguồn 62-FE-F7-11-89-A3 đến bộ chuyển mạch trong khoảng thời gian từ 9:32 đến 10:32. Sau đó vào lúc 10:32, switch sẽ xóa địa chỉ này khỏi bảng của nó.

*Hình 6.23 ♦ Switch tìm hiểu về vị trí của bộ chuyển đổi có địa chỉ*

01-12-23-34-45-56

Thời gian giao diện địa chỉ

01-12-23-34-45-56 9:39

62-FE-F7-11-89-A3 9:32

7C-BA-B2-B4-91-10 9:36

\.... \.... \...

Switches là thiết bị plug-and-play vì chúng không yêu cầu sự can thiệp của quản trị viên mạng hoặc người dùng. Quản trị viên mạng muốn cài đặt một bộ chuyển mạch không cần làm gì khác hơn là kết nối các phân đoạn mạng LAN với các giao diện của bộ chuyển mạch. Quản trị viên không cần phải định cấu hình bảng chuyển đổi tại thời điểm cài đặt hoặc khi máy chủ bị xóa khỏi một trong các phân đoạn mạng LAN. Switches cũng ở chế độ song công hoàn toàn, nghĩa là bất kỳ giao diện chuyển mạch nào cũng có thể gửi và nhận cùng một lúc.

Thuộc tính của chuyển mạch lớp liên kết

Sau khi đã mô tả hoạt động cơ bản của switch lớp liên kết, bây giờ chúng ta hãy xem xét các tính năng và thuộc tính của chúng. Chúng ta có thể xác định một số ưu điểm của việc sử dụng bộ chuyển mạch, thay vì các liên kết quảng bá như xe buýt hoặc cấu trúc liên kết hình sao dựa trên trung tâm:

• Loại bỏ va chạm. Trong mạng LAN được xây dựng từ các bộ chuyển mạch (và không có hub), sẽ không có băng thông bị lãng phí do xung đột! Các bộ chuyển mạch đệm các khung và không bao giờ truyền nhiều hơn một khung trên một phân đoạn tại một thời điểm. Giống như một bộ định tuyến, thông lượng tổng hợp tối đa của một bộ chuyển mạch là tổng của tất cả các tốc độ giao diện của bộ chuyển mạch. Do đó, các thiết bị chuyển mạch mang lại sự cải thiện hiệu suất đáng kể so với mạng LAN có liên kết quảng bá. • Liên kết không đồng nhất. Bởi vì một switch tách biệt một liên kết này với một liên kết khác nên các liên kết khác nhau trong mạng LAN có thể hoạt động ở tốc độ khác nhau và có thể chạy trên các phương tiện khác nhau. Ví dụ: bộ chuyển mạch trên cùng trong Hình 6.15 có thể có ba liên kết đồng 1000BASE-T 1 Gbps, hai liên kết sợi 100BASE-FX 100 Mbps và một liên kết đồng 100BASE-T. Vì vậy, bộ chuyển mạch là giải pháp lý tưởng để kết hợp thiết bị cũ với thiết bị mới. • Sự quản lý. Ngoài việc cung cấp khả năng bảo mật nâng cao (xem thanh bên trong Tập trung vào bảo mật), bộ chuyển mạch còn giúp dễ dàng quản lý mạng. Ví dụ: nếu bộ điều hợp gặp trục trặc và liên tục gửi các khung Ethernet (được gọi là bộ điều hợp giật), bộ chuyển mạch có thể phát hiện sự cố và ngắt kết nối bên trong bộ điều hợp bị trục trặc. Với tính năng này, quản trị viên mạng không cần phải ra khỏi giường và lái xe trở lại làm việc để khắc phục sự cố. Tương tự, việc cắt cáp sẽ chỉ ngắt kết nối máy chủ đang sử dụng cáp bị cắt để kết nối với bộ chuyển mạch. Vào thời cáp đồng trục, nhiều nhà quản lý mạng đã phải mất hàng giờ "đi dọc đường" (hay chính xác hơn là "bò sàn") để tìm ra điểm đứt cáp khiến toàn bộ mạng bị sập. Switches cũng thu thập số liệu thống kê về việc sử dụng băng thông, tỷ lệ xung đột và loại lưu lượng truy cập, đồng thời cung cấp thông tin này cho người quản lý mạng. Thông tin này có thể được sử dụng để gỡ lỗi và khắc phục sự cố cũng như lập kế hoạch phát triển mạng LAN trong tương lai. Các nhà nghiên cứu đang khám phá việc bổ sung thêm chức năng quản lý vào mạng LAN Ethernet trong quá trình triển khai nguyên mẫu \[Casado 2007; Koponen 2011\].

Switches So với Routers

Như chúng ta đã học trong Chương 4, bộ định tuyến là các bộ chuyển mạch gói lưu trữ và chuyển tiếp để chuyển tiếp các gói sử dụng địa chỉ lớp mạng. Mặc dù switch cũng là một switch gói lưu trữ và chuyển tiếp, nhưng về cơ bản nó khác với bộ định tuyến ở chỗ nó chuyển tiếp các gói bằng địa chỉ MAC. Trong khi bộ định tuyến là bộ chuyển mạch gói lớp 3 thì bộ chuyển mạch là bộ chuyển mạch gói lớp 2. Tuy nhiên, hãy nhớ lại rằng chúng ta đã học trong Phần 4.4 rằng các bộ chuyển mạch hiện đại sử dụng thao tác "match plus action" có thể được sử dụng để chuyển tiếp khung lớp 2 dựa trên địa chỉ MAC đích của khung, cũng như gói dữ liệu lớp 3 sử dụng địa chỉ đích IP của gói dữ liệu. Thật vậy, chúng tôi đã thấy rằng các thiết bị chuyển mạch sử dụng tiêu chuẩn OpenFlow có thể thực hiện chuyển tiếp gói tổng quát dựa trên bất kỳ trường nào trong số 11 trường tiêu đề khung, datagram và lớp vận chuyển khác nhau.

Mặc dù bộ chuyển mạch và bộ định tuyến về cơ bản là khác nhau nhưng quản trị viên mạng thường phải lựa chọn giữa chúng khi cài đặt thiết bị kết nối. Ví dụ, đối với mạng trong Hình 6.15, quản trị viên mạng có thể dễ dàng sử dụng bộ định tuyến thay vì bộ chuyển mạch để kết nối các mạng LAN của bộ phận, máy chủ và bộ định tuyến cổng internet. Thật vậy, bộ định tuyến sẽ cho phép liên lạc giữa các bộ phận mà không tạo ra xung đột. Cho rằng cả bộ chuyển mạch và bộ định tuyến đều là ứng cử viên cho các thiết bị kết nối, ưu và nhược điểm của hai phương pháp này là gì?

NGHE MỘT MẠNG LAN CHUYỂN ĐỔI: CHUYỂN ĐỔI NGỘ ĐỘC

Khi một máy chủ được kết nối với một bộ chuyển mạch, nó thường chỉ nhận các khung dành cho nó. Ví dụ, hãy xem xét một mạng LAN chuyển mạch trong Hình 6.17. Khi máy chủ A gửi một khung đến máy chủ B và có một mục dành cho máy chủ B trong bảng chuyển đổi thì bộ chuyển mạch sẽ chỉ chuyển tiếp khung đó đến máy chủ B. Nếu máy chủ C đang chạy một trình thám thính, máy chủ C sẽ không thể đánh hơi khung A-to-B này. Do đó, trong môi trường mạng LAN chuyển mạch (ngược lại với môi trường liên kết quảng bá như mạng LAN 802.11 hoặc mạng LAN Ethernet dựa trên trung tâm), kẻ tấn công sẽ khó đánh hơi các khung hơn. Tuy nhiên, do switch phát các khung có địa chỉ đích không có trong bảng chuyển mạch, nên sniffer tại C vẫn có thể đánh hơi một số khung không dành cho C. Hơn nữa, một sniffer sẽ có thể đánh hơi tất cả các khung phát Ethernet có địa chỉ đích phát sóng FF--FF--FF--FF--FF--FF. Một cuộc tấn công nổi tiếng chống lại một switch, được gọi là switch Ngộ độc, là gửi hàng tấn gói đến switch với nhiều địa chỉ MAC nguồn giả khác nhau, do đó lấp đầy bảng switch với các mục nhập không có thật và không còn chỗ cho địa chỉ MAC của các máy chủ hợp pháp. Điều này làm cho bộ chuyển mạch phát hầu hết các khung hình, sau đó trình thám thính có thể thu được các khung hình này \[Skoudis 2006\]. Vì cuộc tấn công này khá phức tạp ngay cả đối với một kẻ tấn công tinh vi, nên các thiết bị chuyển mạch ít bị đánh cắp hơn đáng kể so với các hub và mạng LAN không dây.

TẬP TRUNG VÀO AN NINH

Đầu tiên hãy xem xét những ưu và nhược điểm của thiết bị chuyển mạch. Như đã đề cập ở trên, thiết bị chuyển mạch là plug-and-play, một đặc tính được tất cả các quản trị viên mạng làm việc quá sức trên thế giới trân trọng. Switches cũng có thể có tốc độ lọc và chuyển tiếp tương đối cao---như trong Hình 6.24, các thiết bị chuyển mạch chỉ phải xử lý các khung thông qua lớp 2, trong khi các bộ định tuyến phải xử lý các gói dữ liệu qua lớp 3. Mặt khác, để ngăn chặn việc quay vòng các khung quảng bá, cấu trúc liên kết hoạt động của mạng chuyển mạch bị giới hạn ở một cây bao trùm. Ngoài ra, một mạng chuyển mạch lớn sẽ yêu cầu các bảng ARP lớn trong máy chủ và bộ định tuyến và sẽ tạo ra lưu lượng và xử lý ARP đáng kể. Hơn nữa, các bộ chuyển mạch rất dễ bị ảnh hưởng bởi các cơn bão phát sóng---nếu một máy chủ gặp trục trặc và truyền một luồng khung phát sóng Ethernet vô tận, các bộ chuyển mạch sẽ chuyển tiếp tất cả các khung này, khiến toàn bộ mạng bị sập.

Bây giờ hãy xem xét những ưu và nhược điểm của bộ định tuyến. Bởi vì địa chỉ mạng thường có thứ bậc (và không phẳng, cũng như địa chỉ MAC), các gói thường không chuyển qua các bộ định tuyến ngay cả khi mạng có các đường dẫn dự phòng. (Tuy nhiên, các gói có thể quay vòng khi các bảng của bộ định tuyến bị định cấu hình sai; nhưng như chúng ta đã tìm hiểu trong Chương 4, IP sử dụng trường tiêu đề gói dữ liệu đặc biệt để hạn chế việc quay vòng.) Do đó, các gói không bị giới hạn trong cây bao trùm và có thể sử dụng đường dẫn tốt nhất giữa nguồn và đích. Bởi vì các bộ định tuyến không có giới hạn về cây bao trùm nên chúng cho phép xây dựng Internet với cấu trúc liên kết phong phú, chẳng hạn như bao gồm nhiều liên kết hoạt động giữa Châu Âu và Bắc Mỹ. Một tính năng khác của bộ định tuyến là chúng cung cấp khả năng bảo vệ tường lửa chống lại các cơn bão phát sóng lớp 2. Tuy nhiên, có lẽ nhược điểm đáng kể nhất của bộ định tuyến là chúng không phải là plug-and-play---chúng và các máy chủ kết nối với chúng cần có địa chỉ IP để được định cấu hình. Ngoài ra, bộ định tuyến thường có thời gian xử lý trên mỗi gói lớn hơn so với bộ chuyển mạch vì chúng phải xử lý thông qua các trường lớp 3. Cuối cùng, có hai cách khác nhau để phát âm từ bộ định tuyến, là "rootor" hoặc "rowter", và mọi người lãng phí rất nhiều thời gian để tranh cãi về cách phát âm thích hợp \[Perlman 1999\].

Cho rằng cả thiết bị chuyển mạch và bộ định tuyến đều có ưu và nhược điểm (như được tóm tắt trong Bảng 6.1), khi nào mạng tổ chức (ví dụ: khuôn viên trường đại học) nên

*Hình 6.24 ♦ Packet xử lý trong switch, bộ định tuyến và máy chủ*

Host

Ứng dụng

Host

Chuyên chở

Mạng

liên kết

Thuộc vật chất

liên kết

Thuộc vật chất

Mạng

Switch Router

liên kết

Thuộc vật chất

Ứng dụng

Chuyên chở

Mạng

liên kết

Thuộc vật chất

mạng hoặc mạng khuôn viên công ty) sử dụng bộ chuyển mạch và khi nào nên sử dụng bộ định tuyến? Thông thường, các mạng nhỏ bao gồm vài trăm máy chủ có một vài phân đoạn mạng LAN. Switches là đủ cho các mạng nhỏ này vì chúng bản địa hóa lưu lượng truy cập và tăng thông lượng tổng hợp mà không yêu cầu bất kỳ cấu hình nào của địa chỉ IP. Nhưng các mạng lớn hơn bao gồm hàng nghìn máy chủ thường bao gồm các bộ định tuyến trong mạng (ngoài các bộ chuyển mạch). Các bộ định tuyến cung cấp khả năng cách ly lưu lượng mạnh mẽ hơn, kiểm soát các cơn bão phát sóng và sử dụng các tuyến đường "thông minh" hơn giữa các máy chủ trong mạng.

Để thảo luận thêm về những ưu và nhược điểm của mạng chuyển mạch so với mạng định tuyến, cũng như thảo luận về cách công nghệ mạng LAN chuyển mạch có thể được mở rộng để đáp ứng số lượng máy chủ nhiều hơn hai bậc so với Ethernet ngày nay, hãy xem \[Meyers 2004; Kim 2008\].

**6.4.4 Mạng cục bộ ảo (VLAN)**

Trong cuộc thảo luận trước đây của chúng ta về Hình 6.15, chúng ta đã lưu ý rằng các mạng LAN tổ chức hiện đại thường được cấu hình theo thứ bậc, với mỗi nhóm làm việc (bộ phận) có mạng LAN chuyển mạch riêng được kết nối với mạng LAN chuyển mạch của các nhóm khác thông qua hệ thống phân cấp chuyển mạch. Mặc dù cấu hình như vậy hoạt động tốt trong thế giới lý tưởng nhưng thế giới thực thường không lý tưởng. Ba nhược điểm có thể được xác định trong cấu hình trong Hình 6.15:

• Thiếu sự cô lập giao thông. Mặc dù hệ thống phân cấp bản địa hóa lưu lượng truy cập nhóm trong một bộ chuyển mạch duy nhất, nhưng lưu lượng phát sóng (ví dụ: các khung mang tin nhắn ARP và DHCP hoặc các khung có điểm đến chưa được bộ chuyển mạch tự học) vẫn phải đi qua toàn bộ mạng tổ chức. Việc giới hạn phạm vi lưu lượng phát sóng như vậy sẽ cải thiện hiệu suất mạng LAN. Có lẽ quan trọng hơn, việc hạn chế lưu lượng phát sóng mạng LAN vì lý do bảo mật/quyền riêng tư cũng có thể được khuyến khích. Ví dụ: nếu một nhóm bao gồm nhóm quản lý điều hành của công ty và một nhóm khác bao gồm các nhân viên bất mãn đang chạy phần mềm nghe lén gói Wireshark, thì người quản lý mạng có thể muốn lưu lượng truy cập của các giám đốc điều hành thậm chí không bao giờ đến được máy chủ của nhân viên. Kiểu cách ly này có thể được cung cấp bởi

Bảng 6.1 ♦ So sánh đặc điểm điển hình của các kết nối phổ biến

thiết bị

Trung tâm Routers Switches

Cách ly giao thông Không Có Có

Cắm và chạy Có Không Có

Định tuyến tối ưu Không Có Không

thay thế công tắc trung tâm trong Hình 6.15 bằng bộ định tuyến. Chúng ta sẽ sớm thấy rằng sự cô lập này cũng có thể đạt được thông qua giải pháp chuyển mạch (lớp 2). • Sử dụng công tắc không hiệu quả. Nếu thay vì ba nhóm, tổ chức có 10 nhóm thì cần có 10 công tắc cấp một. Nếu mỗi nhóm nhỏ, chẳng hạn như dưới 10 người, thì một bộ chuyển mạch 96 cổng có thể sẽ đủ lớn để chứa tất cả mọi người, nhưng bộ chuyển mạch đơn này sẽ không cung cấp khả năng cách ly giao thông. • Quản lý người dùng. Nếu một nhân viên di chuyển giữa các nhóm, hệ thống cáp vật lý phải được thay đổi để kết nối nhân viên đó với một bộ chuyển mạch khác trong Hình 6.15. Nhân viên thuộc hai nhóm khiến vấn đề càng trở nên khó khăn hơn.

May mắn thay, mỗi khó khăn này đều có thể được giải quyết bằng một switch hỗ trợ mạng cục bộ ảo (VLAN). Như tên cho thấy, một bộ chuyển mạch hỗ trợ Vlan cho phép xác định nhiều mạng cục bộ ảo trên một cơ sở hạ tầng mạng cục bộ vật lý duy nhất. Hosts trong một VLAN giao tiếp với nhau như thể chúng (và không có máy chủ nào khác) được kết nối với bộ chuyển mạch. Trong Vlan dựa trên cổng, các cổng (giao diện) của bộ chuyển mạch được người quản lý mạng chia thành các nhóm. Mỗi nhóm tạo thành một Vlan, với các cổng trong mỗi Vlan tạo thành một miền quảng bá (tức là lưu lượng phát sóng từ một cổng chỉ có thể đến các cổng khác trong nhóm). Hình 6.25 cho thấy một switch có 16 cổng. Ports 2 đến 8 thuộc về EE VLAN, trong khi cổng 9 đến 15 thuộc về CS VLAN (cổng 1 và 16 chưa được gán). VLAN này giải quyết tất cả các khó khăn nêu trên---các khung VLAN EE và CS được cách ly với nhau, hai switch trong Hình 6.15 đã được thay thế bằng một switch duy nhất và nếu người dùng ở cổng switch 8 tham gia Phòng CS, nhà điều hành mạng chỉ cần cấu hình lại phần mềm VLAN để cổng 8 hiện được liên kết với CS VLAN. Người ta có thể dễ dàng hình dung cách cấu hình và vận hành bộ chuyển mạch Vlan - người quản lý mạng khai báo một cổng thuộc về

*Hình 6.25 ♦ Một switch đơn có hai VLAN được cấu hình*

Kỹ thuật điện

(Cổng Vlan 2--8)

Khoa học máy tính (cổng VLAN 9--15)

đối với một Vlan nhất định (với các cổng không được khai báo thuộc về một Vlan mặc định) bằng phần mềm quản lý bộ chuyển mạch, một bảng ánh xạ cổng tới Vlan được duy trì trong bộ chuyển mạch; và phần cứng chuyển mạch chỉ phân phối các khung giữa các cổng thuộc cùng một VLAN.

Nhưng bằng cách cô lập hoàn toàn hai VLAN, chúng tôi đã đưa ra một khó khăn mới! Làm thế nào lưu lượng truy cập từ Phòng EE có thể được gửi đến Phòng CS? Một cách để xử lý vấn đề này là kết nối cổng chuyển đổi Vlan (ví dụ: cổng 1 trong Hình 6.25) với bộ định tuyến bên ngoài và định cấu hình cổng đó thuộc cả EE và CS Vlan. Trong trường hợp này, mặc dù các bộ phận EE và CS dùng chung một bộ chuyển mạch vật lý, nhưng cấu hình logic sẽ trông như thể bộ phận EE và CS có các bộ chuyển mạch riêng biệt được kết nối qua bộ định tuyến. Một gói dữ liệu IP đi từ EE đến bộ phận CS trước tiên sẽ đi qua EE Vlan để đến bộ định tuyến và sau đó được bộ định tuyến chuyển tiếp trở lại qua CS Vlan tới máy chủ CS. May mắn thay, các nhà cung cấp bộ chuyển mạch giúp người quản lý mạng dễ dàng thực hiện các cấu hình như vậy bằng cách xây dựng một thiết bị duy nhất chứa cả bộ chuyển mạch Vlan và bộ định tuyến, do đó không cần có bộ định tuyến bên ngoài riêng biệt. Bài tập về nhà ở cuối chương sẽ khám phá kịch bản này một cách chi tiết hơn.

Quay trở lại Hình 6.15, bây giờ hãy giả sử rằng thay vì có một khoa Kỹ thuật Máy tính riêng biệt, một số giảng viên EE và CS được đặt trong một tòa nhà riêng biệt, nơi (tất nhiên!) họ cần truy cập mạng và (tất nhiên!) họ muốn trở thành một phần của VLAN của khoa mình. Hình 6.26 cho thấy một switch 8 cổng thứ hai, trong đó các cổng switch đã được xác định là thuộc về EE hoặc CS VLAN, nếu cần. Nhưng hai công tắc này nên được kết nối với nhau như thế nào? Một giải pháp dễ dàng là xác định một cổng thuộc CS VLAN trên mỗi bộ chuyển mạch (tương tự đối với EE VLAN) và kết nối các cổng này với nhau, như trong Hình 6.26(a). Tuy nhiên, giải pháp này không mở rộng quy mô vì N VLANS sẽ yêu cầu N cổng trên mỗi bộ chuyển mạch chỉ để kết nối hai bộ chuyển mạch.

Một cách tiếp cận có khả năng mở rộng hơn để kết nối các bộ chuyển mạch Vlan được gọi là trung kế Vlan. Trong phương pháp trunking VLAN được hiển thị trong Hình 6.26(b), một cổng đặc biệt trên mỗi switch (cổng 16 trên switch bên trái và cổng 1 trên switch bên phải) được cấu hình làm cổng trunk để kết nối hai switch VLAN. Cổng trung kế thuộc về tất cả các Vlan và các khung được gửi đến bất kỳ Vlan nào sẽ được chuyển tiếp qua liên kết trung kế đến bộ chuyển mạch khác. Nhưng điều này đặt ra một câu hỏi khác: Làm thế nào một switch biết rằng một frame đến một cổng trung kế thuộc về một VLAN cụ thể? IEEE đã xác định định dạng khung Ethernet mở rộng, 802.1Q, cho các khung đi qua đường trục Vlan. Như được hiển thị trong Hình 6.27, khung 802.1Q bao gồm khung Ethernet tiêu chuẩn với thẻ Vlan bốn byte được thêm vào tiêu đề mang nhận dạng của Vlan mà khung đó thuộc về. Thẻ VLAN được thêm vào khung bởi switch ở phía gửi của đường trục VLAN, được phân tích cú pháp và loại bỏ bởi switch ở phía nhận của đường trục. Bản thân thẻ Vlan bao gồm trường Mã định danh giao thức thẻ (TPID) 2 byte (với giá trị thập lục phân cố định là 81-00), trường Thông tin kiểm soát thẻ 2 byte chứa trường định danh Vlan 12 bit và trường ưu tiên 3 bit có mục đích tương tự như trường TOS của gói dữ liệu IP.

*Hình 6.26 ♦ Kết nối hai VLAN switch với hai VLAN:*

\(a\) hai dây cáp (b) nối với nhau

Kỹ thuật điện

(Cổng VLAN 2--8) b.

Một.

Kỹ thuật điện

(Cổng VLAN 2, 3, 6)

Liên kết trung kế

Khoa học máy tính (cổng VLAN 9--15)

Khoa học máy tính (cổng VLAN 4, 5, 7)

*Hình 6.27 ♦ Khung Ethernet gốc (trên cùng), Ethernet được gắn thẻ 802.1Q*

Khung VLAN (bên dưới)

Lời nói đầu CRC Đích. Địa chỉ

Địa chỉ nguồn

Kiểu

dữ liệu

Lời mở đầu CRC\' Đích. Địa chỉ

Địa chỉ nguồn

Kiểu

Thông tin kiểm soát thẻ Mã định danh giao thức thẻ

được tính toán lại

CRT

dữ liệu

Trong cuộc thảo luận này, chúng tôi chỉ đề cập ngắn gọn về Vlan và tập trung vào Vlan dựa trên cổng. Chúng ta cũng nên đề cập rằng VLAN có thể được định nghĩa theo nhiều cách khác. Trong Vlan dựa trên MAC, người quản lý mạng chỉ định bộ địa chỉ MAC thuộc về mỗi Vlan; bất cứ khi nào một thiết bị gắn vào một cổng, cổng đó sẽ được kết nối vào Vlan thích hợp dựa trên địa chỉ MAC của thiết bị. Vlan cũng có thể được xác định dựa trên các giao thức lớp mạng (ví dụ: IPv4, IPv6 hoặc Appletalk) và các tiêu chí khác. Vlan cũng có thể được mở rộng trên các bộ định tuyến IP, cho phép các nhóm mạng LAN được kết nối với nhau để tạo thành một Vlan duy nhất có thể trải rộng trên toàn cầu \[Yu 2011\]. Xem tiêu chuẩn 802.1Q \[IEEE 802.1q 2005\] để biết thêm chi tiết.

**6.5 Ảo hóa liên kết: Mạng dưới dạng Link Layer**

Bởi vì chương này liên quan đến các giao thức lớp liên kết và vì chúng ta sắp kết thúc chương này nên hãy cùng suy ngẫm xem sự hiểu biết của chúng ta về thuật ngữ liên kết đã phát triển như thế nào. Chúng ta bắt đầu chương này bằng cách xem liên kết như một sợi dây vật lý kết nối hai máy chủ đang giao tiếp. Khi nghiên cứu nhiều giao thức truy cập, chúng tôi thấy rằng nhiều máy chủ có thể được kết nối bằng một dây chung và "dây" kết nối các máy chủ có thể là quang phổ vô tuyến hoặc phương tiện khác. Điều này khiến chúng tôi coi liên kết một cách trừu tượng hơn là một kênh, thay vì một sợi dây. Trong nghiên cứu của chúng tôi về Ethernet LAN (Hình 6.15), chúng tôi thấy rằng phương tiện kết nối thực sự có thể là một cơ sở hạ tầng chuyển mạch khá phức tạp. Tuy nhiên, trong suốt quá trình phát triển này, bản thân các máy chủ vẫn duy trì quan điểm rằng phương tiện kết nối chỉ đơn giản là một kênh lớp liên kết kết nối hai hoặc nhiều máy chủ. Ví dụ, chúng ta đã thấy rằng một máy chủ Ethernet có thể hoàn toàn không biết liệu nó được kết nối với các máy chủ LAN khác bằng một đoạn mạng LAN ngắn duy nhất (Hình 6.17) hay bởi một mạng LAN chuyển mạch phân tán về mặt địa lý (Hình 6.15) hay bởi một VLAN (Hình 6.26).

Trong trường hợp kết nối modem quay số giữa hai máy chủ, liên kết kết nối hai máy chủ thực sự là mạng điện thoại---một mạng viễn thông toàn cầu, tách biệt về mặt logic với các bộ chuyển mạch, liên kết và ngăn xếp giao thức riêng để truyền dữ liệu và báo hiệu. Tuy nhiên, từ quan điểm của lớp liên kết Internet, kết nối quay số qua mạng điện thoại được xem như một "dây" đơn giản. Theo nghĩa này, Internet ảo hóa mạng điện thoại, xem mạng điện thoại như một công nghệ lớp liên kết cung cấp kết nối lớp liên kết giữa hai máy chủ Internet. Bạn có thể nhớ lại thảo luận của chúng ta về mạng lớp phủ trong Chương 2 rằng mạng lớp phủ cũng xem Internet như một phương tiện để cung cấp kết nối giữa các nút lớp phủ, tìm cách phủ lớp Internet giống như cách Internet phủ lớp mạng điện thoại.

Trong phần này, chúng ta sẽ xem xét các mạng Chuyển mạch nhãn đa giao thức (MPLS). Không giống như mạng điện thoại chuyển mạch kênh, MPLS là mạng chuyển mạch gói,

mạng mạch ảo theo đúng nghĩa của nó. Nó có các định dạng gói và hành vi chuyển tiếp riêng. Vì vậy, từ quan điểm sư phạm, việc thảo luận về MPLS rất phù hợp với việc nghiên cứu lớp mạng hoặc lớp liên kết. Tuy nhiên, từ quan điểm Internet, chúng ta có thể coi MPLS, giống như mạng điện thoại và Ethernet chuyển mạch, là công nghệ lớp liên kết phục vụ cho các thiết bị IP kết nối với nhau. Vì vậy, chúng ta sẽ xem xét MPLS trong phần thảo luận về lớp liên kết. Mạng Frame-relay và ATM cũng có thể được sử dụng để kết nối các thiết bị IP, mặc dù chúng đại diện cho công nghệ cũ hơn một chút (nhưng vẫn được triển khai) và sẽ không được đề cập ở đây; xem cuốn sách rất dễ đọc \[Goralski 1999\] để biết thêm chi tiết. Việc xử lý MPLS của chúng tôi nhất thiết phải ngắn gọn vì toàn bộ sách có thể được (và đã được) viết trên các mạng này. Chúng tôi khuyên dùng \[Davie 2000\] để biết chi tiết về MPLS. Ở đây chúng tôi sẽ tập trung chủ yếu vào cách các máy chủ MPLS kết nối với các thiết bị IP, mặc dù chúng tôi cũng sẽ đi sâu hơn một chút vào các công nghệ cơ bản.

**6.5.1 Chuyển mạch nhãn đa giao thức (MPLS)**

Multiprotocol Label Switching (MPLS) evolved from a number of industry efforts in the mid-to-late 1990s to improve the forwarding speed of IP routers by adopting a key concept from the world of virtual-circuit networks: a fixed-length label. The goal was not to abandon the destination-based IP datagram-forwarding infrastructure for one based on fixed-length labels and virtual circuits, but to augment it by selectively labeling datagrams and allowing routers to forward datagrams based on fixed-length labels (rather than destination IP addresses) when possible. Điều quan trọng là các kỹ thuật này hoạt động song song với IP, sử dụng địa chỉ và định tuyến IP. IETF đã hợp nhất những nỗ lực này trong giao thức MPLS \[RFC 3031, RFC 3032\], kết hợp hiệu quả các kỹ thuật VC vào mạng datagram được định tuyến.

Hãy bắt đầu nghiên cứu về MPLS bằng cách xem xét định dạng của khung lớp liên kết được xử lý bởi bộ định tuyến có khả năng MPLS. Figure 6.28 shows that a link-layer frame transmitted between MPLS-capable devices has a small MPLS header added between the layer-2 (e.g., Ethernet) header and layer-3 (i.e., IP) header. RFC 3032 xác định định dạng tiêu đề MPLS cho các liên kết đó; Các tiêu đề được xác định cho ATM và các mạng chuyển tiếp khung cũng như trong các RFC khác. Trong số các trường trong MPLS

PPP hoặc Ethernet

tiêu đề Tiêu đề MPLS Tiêu đề IP Phần còn lại của khung lớp liên kết

Nhãn Exp S TTL

*Hình 6.28 ♦ Tiêu đề MPLS: Nằm giữa lớp liên kết và lớp mạng*

tiêu đề

tiêu đề là nhãn, 3 bit dành riêng cho sử dụng thử nghiệm, một bit S duy nhất, được sử dụng để biểu thị sự kết thúc của một loạt các tiêu đề MPLS "xếp chồng" (một chủ đề nâng cao mà chúng tôi sẽ không đề cập ở đây) và một trường thời gian tồn tại.

Rõ ràng ngay từ Hình 6.28 rằng khung được tăng cường MPLS chỉ có thể được gửi giữa các bộ định tuyến có cả hai khả năng MPLS (vì bộ định tuyến không có khả năng MPLS sẽ khá bối rối khi tìm thấy tiêu đề MPLS nơi nó dự kiến ​​​​sẽ tìm thấy tiêu đề IP!). Một bộ định tuyến có khả năng MPLS thường được gọi là bộ định tuyến chuyển mạch nhãn, vì nó chuyển tiếp khung MPLS bằng cách tra cứu nhãn MPLS trong bảng chuyển tiếp của nó và sau đó chuyển ngay gói dữ liệu đến giao diện đầu ra thích hợp. Do đó, bộ định tuyến có khả năng MPLS không cần trích xuất địa chỉ đích IP và thực hiện tra cứu kết quả khớp tiền tố dài nhất trong bảng chuyển tiếp. Nhưng làm cách nào để bộ định tuyến biết liệu hàng xóm của nó có thực sự có khả năng MPLS hay không và làm cách nào bộ định tuyến biết nhãn nào để liên kết với đích IP đã cho? Để trả lời những câu hỏi này, chúng ta cần xem xét sự tương tác giữa một nhóm bộ định tuyến có khả năng MPLS.

Trong ví dụ ở Hình 6.29, các bộ định tuyến từ R1 đến R4 có khả năng MPLS. R5 và R6 là các bộ định tuyến IP tiêu chuẩn. R1 đã quảng cáo tới R2 và R3 rằng nó (R1) có thể định tuyến đến đích A và khung nhận được có nhãn MPLS 6 sẽ được chuyển tiếp đến đích A. Router R3 đã quảng cáo tới bộ định tuyến R4 rằng nó có thể định tuyến đến đích A và D, đồng thời các khung đến có nhãn MPLS 10 và 12 tương ứng sẽ được chuyển hướng tới các đích đó. Router R2 cũng đã quảng cáo tới bộ định tuyến R4 rằng nó (R2) có thể đến đích A và khung nhận được có nhãn MPLS 8 sẽ được chuyển về A. Lưu ý rằng bộ định tuyến R4 hiện đang ở vị trí thú vị khi có hai MPLS

*Hình 6.29 ♦ Chuyển tiếp tăng cường MPLS*

R4

trong nhãn

nhãn ra

A D A

giao diện đích

R6

R5

R3

R2

D

MỘT

R1

trong nhãn

nhãn ra

A D

giao diện đích

trong nhãn

nhãn ra

\- MỘT

giao diện đích ra trong nhãn

nhãn ra

MỘT

giao diện đích

đường dẫn đến A: qua giao diện 0 với nhãn MPLS đi 10 và qua giao diện 1 với nhãn MPLS là 8. Bức tranh rộng được vẽ trong Hình 6.29 là IP các thiết bị R5, R6, A và D được kết nối với nhau thông qua cơ sở hạ tầng MPLS (các bộ định tuyến có khả năng MPLS R1, R2, R3 và R4) theo cách tương tự như một mạng LAN chuyển mạch hoặc mạng ATM có thể kết nối với nhau IP thiết bị. Và giống như mạng LAN hoặc mạng ATM chuyển mạch, các bộ định tuyến MPLScapable R1 đến R4 thực hiện điều này mà không cần chạm vào tiêu đề IP của gói.

Trong cuộc thảo luận ở trên, chúng tôi chưa chỉ định giao thức cụ thể được sử dụng để phân phối nhãn giữa các bộ định tuyến có khả năng MPLS, vì các chi tiết về tín hiệu này nằm ngoài phạm vi của cuốn sách này. Tuy nhiên, chúng tôi lưu ý rằng nhóm làm việc IETF về MPLS đã chỉ định trong \[RFC 3468\] rằng phần mở rộng của giao thức RSVP, được gọi là RSVP-TE \[RFC 3209\], sẽ là trọng tâm nỗ lực của nhóm đối với tín hiệu MPLS. Chúng tôi cũng chưa thảo luận về cách MPLS thực sự tính toán các đường dẫn cho các gói giữa các bộ định tuyến có khả năng MPLS cũng như cách nó thu thập thông tin trạng thái liên kết (ví dụ: lượng băng thông liên kết không được MPLS bảo lưu) để sử dụng trong các tính toán đường dẫn này. Các thuật toán định tuyến trạng thái liên kết hiện có (ví dụ: OSPF) đã được mở rộng để tràn thông tin này đến các bộ định tuyến có khả năng MPLS. Điều thú vị là các thuật toán tính toán đường dẫn thực tế không được chuẩn hóa và hiện dành riêng cho nhà cung cấp.

Cho đến nay, điểm nhấn trong thảo luận của chúng ta về MPLS là MPLS thực hiện chuyển mạch dựa trên nhãn mà không cần xem xét địa chỉ IP của gói. Tuy nhiên, những ưu điểm thực sự của MPLS và lý do quan tâm hiện nay đến MPLS không nằm ở khả năng tăng tốc độ chuyển mạch mà nằm ở khả năng quản lý lưu lượng mới mà MPLS cho phép. Như đã lưu ý ở trên, R4 có hai đường dẫn MPLS tới A. Nếu việc chuyển tiếp được thực hiện ở lớp IP trên cơ sở địa chỉ IP, thì các giao thức định tuyến IP mà chúng ta đã nghiên cứu trong Chương 5 sẽ chỉ xác định một đường dẫn duy nhất, có chi phí thấp nhất tới A. Do đó, MPLS cung cấp khả năng chuyển tiếp các gói dọc theo các tuyến mà không thể thực hiện được bằng các giao thức định tuyến IP tiêu chuẩn. Đây là một dạng kỹ thuật lưu lượng đơn giản sử dụng MPLS \[RFC 3346; RFC 3272; RFC 2702; Xiao 2000\], trong đó nhà điều hành mạng có thể ghi đè định tuyến IP thông thường và buộc một số lưu lượng truy cập hướng tới một đích nhất định dọc theo một đường dẫn và lưu lượng truy cập khác hướng đến cùng một đích dọc theo một đường dẫn khác (cho dù vì chính sách, hiệu suất hay một số lý do khác).

Cũng có thể sử dụng MPLS cho nhiều mục đích khác. Nó có thể được sử dụng để thực hiện khôi phục nhanh các đường chuyển tiếp MPLS, ví dụ: định tuyến lại lưu lượng truy cập qua đường dẫn chuyển đổi dự phòng được tính toán trước để ứng phó với lỗi liên kết \[Kar 2000; Hoàng 2002; RFC 3469\]. Cuối cùng, chúng tôi lưu ý rằng MPLS có thể và đã được sử dụng để triển khai cái gọi là mạng riêng ảo (VPN). Khi triển khai VPN cho khách hàng, ISP sử dụng mạng hỗ trợ MPLS của mình để kết nối các mạng khác nhau của khách hàng với nhau. MPLS có thể được sử dụng để tách biệt cả tài nguyên và địa chỉ được sử dụng bởi VPN của khách hàng với tài nguyên và địa chỉ của những người dùng khác qua mạng của ISP; xem \[DeClercq 2002\] để biết thêm chi tiết.

Cuộc thảo luận của chúng tôi về MPLS rất ngắn gọn và chúng tôi khuyến khích bạn tham khảo các tài liệu tham khảo mà chúng tôi đã đề cập. Chúng tôi lưu ý rằng MPLS đã nổi lên trước sự phát triển của mạng được xác định bằng phần mềm mà chúng tôi đã nghiên cứu trong Chương 5 và nhiều khả năng kỹ thuật lưu lượng của MPLS cũng có thể đạt được thông qua SDN và mô hình chuyển tiếp tổng quát mà chúng tôi đã nghiên cứu trong Chương 4. Chỉ có tương lai mới biết liệu MPLS và SDN có tiếp tục cùng tồn tại hay không, hay liệu các công nghệ mới hơn (như SDN) cuối cùng sẽ thay thế MPLS hay không.

**6.6 Mạng trung tâm dữ liệu**

Các công ty Internet như Google, Microsoft, Amazon và Alibaba đã xây dựng các trung tâm dữ liệu khổng lồ, mỗi trung tâm chứa hàng chục đến hàng trăm nghìn máy chủ. Như đã thảo luận ngắn gọn ở thanh bên ở Phần 1.2, các trung tâm dữ liệu không chỉ được kết nối với Internet mà còn bao gồm bên trong các mạng máy tính phức tạp, được gọi là mạng trung tâm dữ liệu, kết nối các máy chủ nội bộ của chúng. Trong phần này, chúng tôi giới thiệu ngắn gọn về mạng trung tâm dữ liệu cho các ứng dụng đám mây.

Nói rộng ra, trung tâm dữ liệu phục vụ ba mục đích. Đầu tiên, họ cung cấp nội dung như trang Web, kết quả tìm kiếm, e-mail hoặc truyền phát video tới người dùng. Thứ hai, chúng đóng vai trò là cơ sở hạ tầng điện toán song song ồ ạt cho các tác vụ xử lý dữ liệu cụ thể, chẳng hạn như tính toán chỉ mục phân tán cho các công cụ tìm kiếm. Thứ ba, họ cung cấp điện toán đám mây cho các công ty khác. Thật vậy, ngày nay xu hướng chính trong điện toán là các công ty sử dụng nhà cung cấp đám mây như Amazon Web Services, Microsoft Azure và Alibaba Cloud để xử lý cơ bản tất cả các nhu cầu CNTT của họ.

**6.6.1 Kiến trúc trung tâm dữ liệu**

Các thiết kế trung tâm dữ liệu được công ty giữ bí mật cẩn thận vì chúng thường mang lại lợi thế cạnh tranh quan trọng cho các công ty điện toán đám mây hàng đầu. Chi phí của một trung tâm dữ liệu lớn là rất lớn, vượt quá 12 triệu USD mỗi tháng cho một trung tâm dữ liệu có 100.000 máy chủ trong năm 2009 \[Greenberg 2009a\]. Trong số các chi phí này, khoảng 45 phần trăm có thể do chính các vật chủ chi trả (cần được thay thế sau mỗi 3--4 năm); 25 phần trăm cho cơ sở hạ tầng, bao gồm máy biến áp, hệ thống cung cấp điện liên tục (UPS), máy phát điện khi mất điện dài hạn và hệ thống làm mát; 15 phần trăm cho chi phí tiện ích điện khi rút điện; và 15 phần trăm cho kết nối mạng, bao gồm thiết bị mạng (bộ chuyển mạch, bộ định tuyến và bộ cân bằng tải), liên kết bên ngoài và chi phí lưu lượng chuyển tuyến. (Trong những tỷ lệ phần trăm này, chi phí cho thiết bị được khấu hao để áp dụng thước đo chi phí chung cho mua hàng một lần và các chi phí liên tục như điện.) Trong khi mạng không phải là chi phí lớn nhất, đổi mới mạng là chìa khóa để giảm chi phí tổng thể và tối đa hóa hiệu suất \[Greenberg 2009a\].

Những con ong thợ trong trung tâm dữ liệu là vật chủ. Các máy chủ trong trung tâm dữ liệu, được gọi là lưỡi dao và trông giống hộp bánh pizza, nói chung là các máy chủ hàng hóa bao gồm CPU, bộ nhớ và ổ lưu trữ. Các máy chủ được xếp thành các giá, mỗi giá thường có từ 20 đến 40 lưỡi dao. Ở đầu mỗi giá, có một công tắc, được đặt tên phù hợp là công tắc Top of Rack (TOR), dùng để kết nối các máy chủ trong giá với nhau và với các công tắc khác trong trung tâm dữ liệu. Cụ thể, mỗi máy chủ trong rack có giao diện mạng kết nối với bộ chuyển mạch TOR của nó và mỗi bộ chuyển mạch TOR có các cổng bổ sung có thể kết nối với các bộ chuyển mạch khác. Ngày nay, các máy chủ thường có kết nối Ethernet 40 Gbps hoặc 100 Gbps với bộ chuyển mạch TOR \[FB 2019; Greenberg 2015; Roy 2015; Singh 2015\]. Mỗi máy chủ cũng được chỉ định địa chỉ IP nội bộ trung tâm dữ liệu của riêng mình.

Mạng trung tâm dữ liệu hỗ trợ hai loại lưu lượng: lưu lượng truy cập giữa các máy khách bên ngoài và máy chủ nội bộ và lưu lượng truy cập giữa các máy chủ nội bộ. Để xử lý các luồng giữa máy khách bên ngoài và máy chủ nội bộ, mạng trung tâm dữ liệu bao gồm một hoặc nhiều bộ định tuyến biên, kết nối mạng trung tâm dữ liệu với Internet công cộng. Do đó, mạng trung tâm dữ liệu sẽ kết nối các giá đỡ với nhau và kết nối các giá đỡ với bộ định tuyến biên. Hình 6.30 thể hiện một ví dụ về mạng trung tâm dữ liệu. Thiết kế mạng trung tâm dữ liệu, nghệ thuật thiết kế mạng kết nối và các giao thức kết nối các giá đỡ với nhau và với các bộ định tuyến biên, đã trở thành một nhánh quan trọng của nghiên cứu mạng máy tính trong những năm gần đây. (Xem tài liệu tham khảo trong phần này.)

Cân bằng tải

Trung tâm dữ liệu đám mây, chẳng hạn như trung tâm do Google, Microsoft, Amazon và Alibaba điều hành, cung cấp đồng thời nhiều ứng dụng, chẳng hạn như ứng dụng tìm kiếm, e-mail và video. Để hỗ trợ các yêu cầu từ khách hàng bên ngoài, mỗi ứng dụng được liên kết với một địa chỉ IP hiển thị công khai để khách hàng gửi yêu cầu và nhận phản hồi từ đó. Bên trong trung tâm dữ liệu, các yêu cầu bên ngoài được ưu tiên

*Hình 6.30 ♦ Mạng trung tâm dữ liệu với cấu trúc liên kết phân cấp*

internet

MỘT

C

B

Giá đỡ máy chủ

Công tắc TOR

Công tắc cấp 2

Công tắc cấp 1

Bộ định tuyến truy cập

Bộ định tuyến biên giới

Cân bằng tải

hướng đến một bộ cân bằng tải có nhiệm vụ phân phối các yêu cầu đến các máy chủ, cân bằng tải trên các máy chủ như một chức năng của tải hiện tại của chúng \[Patel 2013; Eisenbud 2016\]. Một trung tâm dữ liệu lớn thường sẽ có một số bộ cân bằng tải, mỗi bộ cân bằng tải dành cho một tập hợp các ứng dụng đám mây cụ thể. Bộ cân bằng tải như vậy đôi khi được gọi là "bộ chuyển đổi lớp 4" vì nó đưa ra quyết định dựa trên số cổng đích (lớp 4) cũng như địa chỉ IP đích trong gói. Khi nhận được yêu cầu cho một ứng dụng cụ thể, bộ cân bằng tải sẽ chuyển tiếp yêu cầu đó đến một trong các máy chủ xử lý ứng dụng đó. (Sau đó, máy chủ có thể gọi dịch vụ của các máy chủ khác để giúp xử lý yêu cầu.) Bộ cân bằng tải không chỉ cân bằng tải công việc trên các máy chủ mà còn cung cấp chức năng giống NAT, dịch địa chỉ IP công khai bên ngoài sang địa chỉ IP nội bộ của máy chủ thích hợp, sau đó dịch ngược lại các gói truyền theo hướng ngược lại trở lại máy khách. Điều này ngăn không cho máy khách liên hệ trực tiếp với máy chủ, điều này có lợi ích bảo mật là ẩn cấu trúc mạng nội bộ và ngăn máy khách tương tác trực tiếp với máy chủ.

Kiến trúc phân cấp

Đối với một trung tâm dữ liệu nhỏ chỉ có vài nghìn máy chủ, một mạng đơn giản bao gồm bộ định tuyến biên, bộ cân bằng tải và vài chục giá đỡ được kết nối với nhau bằng một bộ chuyển mạch Ethernet duy nhất có thể là đủ. Nhưng để mở rộng quy mô lên hàng chục đến hàng trăm nghìn máy chủ, một trung tâm dữ liệu thường sử dụng hệ thống phân cấp các bộ định tuyến và chuyển mạch, chẳng hạn như cấu trúc liên kết được hiển thị trong Hình 6.30. Ở trên cùng của hệ thống phân cấp, bộ định tuyến biên kết nối với các bộ định tuyến truy cập (chỉ có hai bộ định tuyến được hiển thị trong Hình 6.30, nhưng có thể có nhiều bộ định tuyến khác). Bên dưới mỗi bộ định tuyến truy cập có ba tầng chuyển mạch. Mỗi bộ định tuyến truy cập kết nối với một bộ chuyển mạch cấp cao nhất và mỗi bộ chuyển mạch cấp cao nhất kết nối với nhiều bộ chuyển mạch cấp hai và một bộ cân bằng tải. Mỗi công tắc cấp hai lần lượt kết nối với nhiều giá đỡ thông qua công tắc TOR của giá đỡ (công tắc cấp ba). Tất cả các liên kết thường sử dụng Ethernet cho các giao thức lớp liên kết và lớp vật lý, với sự kết hợp giữa cáp đồng và cáp quang. Với thiết kế phân cấp như vậy, có thể mở rộng quy mô trung tâm dữ liệu lên hàng trăm nghìn máy chủ.

Vì điều quan trọng đối với nhà cung cấp ứng dụng đám mây là phải liên tục cung cấp các ứng dụng có tính sẵn sàng cao nên các trung tâm dữ liệu cũng bao gồm thiết bị mạng dự phòng và các liên kết dự phòng trong thiết kế của họ (không được hiển thị trong Hình 6.30). Ví dụ: mỗi bộ chuyển mạch TOR có thể kết nối với hai bộ chuyển mạch cấp 2 và mỗi bộ định tuyến truy cập, bộ chuyển mạch cấp 1 và bộ chuyển mạch cấp 2 có thể được sao chép và tích hợp vào thiết kế \[Cisco 2012; Greenberg 2009b\]. Trong thiết kế phân cấp trong Hình 6.30, hãy quan sát rằng các máy chủ bên dưới mỗi bộ định tuyến truy cập tạo thành một mạng con duy nhất. Để bản địa hóa lưu lượng phát sóng ARP, mỗi mạng con này được phân chia thành các mạng con Vlan nhỏ hơn, mỗi mạng con bao gồm vài trăm máy chủ \[Greenberg 2009a\].

Mặc dù kiến ​​trúc phân cấp thông thường vừa được mô tả giải quyết được vấn đề về quy mô, nhưng nó bị hạn chế về khả năng lưu trữ giữa các máy chủ \[Greenberg 2009b\]. Để hiểu hạn chế này, hãy xem lại Hình 6.30 và giả sử mỗi máy chủ kết nối với bộ chuyển mạch TOR của nó bằng liên kết 10 Gbps, trong khi các liên kết giữa các bộ chuyển mạch

là các liên kết Ethernet 100 Gbps. Hai máy chủ trong cùng một giá luôn có thể giao tiếp ở tốc độ tối đa 10 Gbps, chỉ bị giới hạn bởi tốc độ của bộ điều khiển giao diện mạng của máy chủ. Tuy nhiên, nếu có nhiều luồng đồng thời trong mạng trung tâm dữ liệu, tốc độ tối đa giữa hai máy chủ ở các giá đỡ khác nhau có thể thấp hơn nhiều. Để hiểu rõ hơn về vấn đề này, hãy xem xét mẫu lưu lượng truy cập bao gồm 40 luồng đồng thời giữa 40 cặp máy chủ trong các giá đỡ khác nhau. Cụ thể, giả sử mỗi trong số 10 máy chủ ở giá 1 trong Hình 6.30 gửi một luồng đến máy chủ tương ứng ở giá 5. Tương tự, có 10 luồng đồng thời giữa các cặp máy chủ trong giá 2 và 6, 10 luồng đồng thời giữa các giá 3 và 7 và 10 luồng đồng thời giữa các giá 4 và 8. Nếu mỗi luồng chia sẻ đều dung lượng của một liên kết với các luồng khác đi qua liên kết đó, thì 40 luồng đi qua liên kết A-to-B 100 Gbps (cũng như liên kết B-to-C 100 Gbps), mỗi liên kết sẽ chỉ nhận được 100 Gbps / 40 = 2,5 Gbps, thấp hơn đáng kể so với tốc độ giao diện mạng 10 Gbps. Vấn đề càng trở nên nghiêm trọng hơn đối với các luồng giữa các máy chủ cần di chuyển lên cấp cao hơn.

Có một số giải pháp khả thi cho vấn đề này:

• Một giải pháp khả thi cho hạn chế này là triển khai các bộ chuyển mạch và bộ định tuyến tốc độ cao hơn. Nhưng điều này sẽ làm tăng đáng kể chi phí của trung tâm dữ liệu vì các bộ chuyển mạch và bộ định tuyến có tốc độ cổng cao sẽ rất đắt. • Giải pháp thứ hai cho vấn đề này, có thể được áp dụng bất cứ khi nào có thể, là đặt cùng vị trí các dịch vụ và dữ liệu liên quan càng gần nhau càng tốt (ví dụ: trong cùng một giá hoặc trong một giá gần đó) \[Roy 2015; Singh 2015\] để giảm thiểu giao tiếp giữa các giá đỡ thông qua các bộ chuyển mạch cấp 2 hoặc cấp 1. Nhưng điều này chỉ có thể đi xa hơn, vì yêu cầu chính trong trung tâm dữ liệu là tính linh hoạt trong việc bố trí các tính toán và dịch vụ \[Greenberg 2009b; Farrington 2010\]. Ví dụ: một công cụ tìm kiếm Internet quy mô lớn có thể chạy trên hàng nghìn máy chủ trải rộng trên nhiều giá đỡ với yêu cầu băng thông đáng kể giữa tất cả các cặp máy chủ. Tương tự, dịch vụ điện toán đám mây (chẳng hạn như Amazon Web Services hoặc Microsoft Azure) có thể muốn đặt nhiều máy ảo bao gồm dịch vụ của khách hàng trên các máy chủ vật lý có dung lượng lớn nhất bất kể vị trí của chúng trong trung tâm dữ liệu. Nếu các máy chủ vật lý này được trải rộng trên nhiều giá đỡ thì tình trạng tắc nghẽn mạng như mô tả ở trên có thể dẫn đến hiệu suất kém. • Phần cuối cùng của giải pháp là cung cấp khả năng kết nối tăng cường giữa bộ chuyển mạch TOR và bộ chuyển mạch cấp 2 cũng như giữa bộ chuyển mạch cấp 2 và bộ chuyển mạch cấp 1. Ví dụ, như trong Hình 6.31, mỗi bộ chuyển mạch TOR có thể được kết nối với hai bộ chuyển mạch cấp 2, sau đó cung cấp nhiều đường dẫn liên kết và chuyển mạch tách biệt giữa các giá đỡ. Trong Hình 6.31, có bốn đường dẫn riêng biệt giữa bộ chuyển mạch cấp 2 đầu tiên và bộ chuyển mạch cấp 2 thứ hai, cùng nhau cung cấp dung lượng tổng hợp là 400 Gbps giữa hai bộ chuyển mạch cấp 2 đầu tiên. Việc tăng mức độ kết nối giữa các tầng có hai lợi ích đáng kể: vừa tăng công suất vừa tăng độ tin cậy (do tính đa dạng của đường dẫn) giữa các thiết bị chuyển mạch. Trong trung tâm dữ liệu của Facebook \[FB 2014; FB 2019\], mỗi TOR được kết nối với bốn bộ chuyển mạch cấp 2 khác nhau và mỗi bộ chuyển mạch cấp 2 được kết nối với bốn bộ chuyển mạch cấp 1 khác nhau.

Hậu quả trực tiếp của việc tăng cường khả năng kết nối giữa các tầng trong mạng trung tâm dữ liệu là việc định tuyến đa đường có thể trở thành công dân hạng nhất trong các mạng này. Các luồng theo mặc định là các luồng đa đường. Một sơ đồ rất đơn giản để đạt được định tuyến đa đường là Equal Cost Multi Path (ECMP) \[RFC 2992\], thực hiện lựa chọn bước nhảy tiếp theo ngẫu nhiên dọc theo các chuyển mạch giữa nguồn và đích. Các kế hoạch nâng cao sử dụng cân bằng tải chi tiết hơn cũng đã được đề xuất \[Alizadeh 2014; Noormohammadpour 2018\]. Mặc dù các sơ đồ này thực hiện định tuyến đa đường ở cấp độ luồng, nhưng cũng có những thiết kế định tuyến các gói riêng lẻ trong một luồng giữa nhiều đường dẫn \[He 2015; Raiciu 2010\].

**6.6.2 Xu hướng kết nối mạng trung tâm dữ liệu**

Mạng trung tâm dữ liệu đang phát triển nhanh chóng, với các xu hướng được thúc đẩy bởi việc giảm chi phí, ảo hóa, các hạn chế về vật lý, tính mô đun và tùy chỉnh.

Giảm chi phí

Để giảm chi phí của các trung tâm dữ liệu, đồng thời cải thiện hiệu suất độ trễ và thông lượng, cũng như dễ dàng mở rộng và triển khai, các gã khổng lồ về đám mây Internet đang liên tục triển khai các thiết kế mạng trung tâm dữ liệu mới. Mặc dù một số thiết kế này là độc quyền, những thiết kế khác (ví dụ: \[FB 2019\]) được mở hoặc mô tả rõ ràng trong tài liệu mở (ví dụ: \[Greenberg 2009b; Singh 2015\]). Do đó, nhiều xu hướng quan trọng có thể được xác định.

Hình 6.31 minh họa một trong những xu hướng quan trọng nhất trong mạng trung tâm dữ liệu---sự xuất hiện của mạng phân cấp, phân tầng kết nối các máy chủ trung tâm dữ liệu. Về mặt khái niệm, hệ thống phân cấp này phục vụ cùng mục đích như một bộ chuyển mạch thanh ngang lớn (rất, rất!), mà chúng ta đã nghiên cứu trong Phần 4.2.2, cho phép bất kỳ máy chủ nào trong trung tâm dữ liệu giao tiếp với bất kỳ máy chủ nào khác. Nhưng như chúng ta đã thấy, tầng này

*Hình 6.31 ♦ Cấu trúc liên kết mạng dữ liệu có tính liên kết cao*

Giá đỡ máy chủ

Công tắc TOR

Công tắc cấp 2

Công tắc cấp 1

Mạng kết nối có nhiều ưu điểm so với chuyển mạch thanh ngang khái niệm, bao gồm nhiều đường dẫn từ nguồn đến đích và tăng dung lượng (do định tuyến đa đường) và độ tin cậy (do có nhiều đường dẫn chuyển mạch và liên kết tách rời giữa hai máy chủ bất kỳ).

Mạng kết nối trung tâm dữ liệu bao gồm một số lượng lớn các thiết bị chuyển mạch có kích thước nhỏ. Ví dụ: trong cơ cấu trung tâm dữ liệu Jupiter của Google, một cấu hình có 48 liên kết giữa bộ chuyển mạch ToR và các máy chủ của nó bên dưới, đồng thời kết nối lên tới 8 bộ chuyển mạch cấp 2; một bộ chuyển mạch cấp 2 có liên kết đến 256 bộ chuyển mạch ToR và liên kết tới 16 bộ chuyển mạch cấp 1 \[Singh 2015\]. Trong kiến ​​trúc trung tâm dữ liệu của Facebook, mỗi công tắc ToR kết nối tối đa bốn công tắc cấp 2 khác nhau (mỗi công tắc ở một "mặt phẳng spline" khác nhau) và mỗi công tắc cấp 2 kết nối tối đa 4 trong số 48 công tắc cấp 1 trong mặt phẳng spline của nó; có bốn mặt phẳng spline. Bộ chuyển mạch cấp 1 và cấp 2 lần lượt kết nối với số lượng bộ chuyển mạch cấp 2 hoặc ToR lớn hơn, có thể mở rộng, bên dưới \[FB 2019\]. Đối với một số nhà khai thác trung tâm dữ liệu lớn nhất, các thiết bị chuyển mạch này đang được xây dựng nội bộ từ silicon thông thường, có sẵn, bán sẵn \[Greenberg 2009b; Roy 2015; Singh 2015\] thay vì được mua từ các nhà cung cấp thiết bị chuyển mạch. Mạng kết nối nhiều lớp (tầng, nhiều tầng) đa chuyển mạch như trong Hình 6.31 và được triển khai trong các kiến ​​trúc trung tâm dữ liệu đã thảo luận ở trên được gọi là mạng Clos, được đặt theo tên của Charles Clos, người đã nghiên cứu các mạng như vậy \[Clos 1953\] trong bối cảnh chuyển mạch điện thoại. Kể từ đó, một lý thuyết phong phú về mạng Clos đã được phát triển, tìm kiếm ứng dụng bổ sung trong mạng trung tâm dữ liệu và trong các mạng kết nối đa bộ xử lý.

Quản lý và kiểm soát SDN tập trung

Bởi vì trung tâm dữ liệu được quản lý bởi một tổ chức duy nhất, nên có lẽ điều tự nhiên là một số nhà khai thác trung tâm dữ liệu lớn nhất, bao gồm Google, Microsoft và Facebook, đang áp dụng khái niệm kiểm soát tập trung hợp lý giống SDN. Kiến trúc của chúng cũng phản ánh sự tách biệt rõ ràng giữa mặt phẳng dữ liệu (bao gồm các thiết bị chuyển mạch hàng hóa tương đối đơn giản) và mặt phẳng điều khiển dựa trên phần mềm, như chúng ta đã thấy trong Phần 5.5. Do quy mô khổng lồ của các trung tâm dữ liệu của họ, việc cấu hình tự động và quản lý trạng thái vận hành, như chúng ta đã gặp trong Phần 5.7, cũng rất quan trọng.

Ảo hóa

Ảo hóa đã là động lực thúc đẩy phần lớn sự phát triển của mạng lưới trung tâm dữ liệu và điện toán đám mây nói chung. Máy ảo (VM) tách phần mềm chạy các ứng dụng khỏi phần cứng vật lý. Việc tách rời này cũng cho phép di chuyển liền mạch các máy ảo giữa các máy chủ vật lý, có thể được đặt trên các giá đỡ khác nhau. Giao thức Ethernet và IP tiêu chuẩn có những hạn chế trong việc cho phép di chuyển máy ảo trong khi vẫn duy trì kết nối mạng hoạt động trên các máy chủ. Vì tất cả các mạng trung tâm dữ liệu được quản lý bởi một cơ quan hành chính duy nhất, nên một giải pháp hay cho vấn đề này là xử lý toàn bộ mạng trung tâm dữ liệu như một mạng lớp 2, phẳng, đơn lẻ. Hãy nhớ lại rằng trong mạng Ethernet thông thường, giao thức ARP duy trì liên kết giữa địa chỉ IP và địa chỉ phần cứng (MAC) trên một mạng.

giao diện. Để mô phỏng hiệu ứng của việc tất cả các máy chủ kết nối với một bộ chuyển mạch \"đơn\", cơ chế ARP được sửa đổi để sử dụng hệ thống truy vấn kiểu DNS thay vì phát sóng và thư mục duy trì ánh xạ địa chỉ IP được gán cho một VM và bộ chuyển đổi vật lý nào mà VM hiện được kết nối trong mạng trung tâm dữ liệu. Các kế hoạch có thể mở rộng để thực hiện thiết kế cơ bản này đã được đề xuất trong \[Mysore 2009; Greenberg 2009b\] và đã được triển khai thành công ở các trung tâm dữ liệu hiện đại.

Ràng buộc vật lý

Không giống như Internet diện rộng, mạng trung tâm dữ liệu hoạt động trong môi trường không chỉ có dung lượng rất cao (liên kết 40 Gbps và 100 Gbps hiện đã phổ biến) mà còn có độ trễ cực thấp (micro giây). Do đó, kích thước bộ đệm nhỏ và các giao thức kiểm soát tắc nghẽn như TCP và các biến thể của nó không có quy mô tốt trong các trung tâm dữ liệu. Trong các trung tâm dữ liệu, các giao thức kiểm soát tắc nghẽn phải phản ứng nhanh và hoạt động ở chế độ tổn thất cực thấp, vì việc phục hồi tổn thất và hết thời gian chờ có thể dẫn đến cực kỳ kém hiệu quả. Một số phương pháp tiếp cận để giải quyết vấn đề này đã được đề xuất và triển khai, từ các biến thể TCP dành riêng cho trung tâm dữ liệu \[Alizadeh 2010\] đến triển khai công nghệ Truy cập bộ nhớ trực tiếp từ xa (RDMA) trên Ethernet tiêu chuẩn \[Zhu 2015; Moshref 2016; Quách 2016\]. Lý thuyết lập lịch cũng đã được áp dụng để phát triển các cơ chế tách lập lịch luồng khỏi kiểm soát tốc độ, cho phép các giao thức kiểm soát tắc nghẽn rất đơn giản trong khi vẫn duy trì mức sử dụng cao của các liên kết \[Alizadeh 2013; Hồng 2012\].

Tính mô-đun và tùy chỉnh phần cứng

Một xu hướng chính khác là sử dụng các trung tâm dữ liệu mô-đun dựa trên container (MDC) vận chuyển \[YouTube 2009; Waldrop 2007\]. Trong MDC, một nhà máy xây dựng một "trung tâm dữ liệu mini" trong một container vận chuyển tiêu chuẩn dài 12 mét và vận chuyển container đến vị trí trung tâm dữ liệu. Mỗi container có tới vài nghìn máy chủ, xếp thành hàng chục giá đỡ, xếp sát nhau. Tại vị trí trung tâm dữ liệu, nhiều container được kết nối với nhau và với Internet. Khi một thùng chứa đúc sẵn được triển khai tại trung tâm dữ liệu, nó thường khó phục vụ. Do đó, mỗi vùng chứa được thiết kế để giảm nhẹ hiệu suất: khi các thành phần (máy chủ và thiết bị chuyển mạch) bị lỗi theo thời gian, vùng chứa vẫn tiếp tục hoạt động nhưng hiệu suất bị suy giảm. Khi nhiều thành phần bị lỗi và hiệu suất giảm xuống dưới ngưỡng, toàn bộ vùng chứa sẽ bị xóa và thay thế bằng một vùng chứa mới.

Xây dựng một trung tâm dữ liệu từ các container tạo ra những thách thức mạng mới. Với MDC, có hai loại mạng: mạng nội bộ container trong mỗi container và mạng lõi kết nối từng container \[Guo 2009; Farrington 2010\]. Trong mỗi container, ở quy mô lên tới vài nghìn máy chủ, có thể xây dựng một mạng được kết nối đầy đủ bằng cách sử dụng các bộ chuyển mạch Gigabit Ethernet thông thường rẻ tiền. Tuy nhiên, thiết kế mạng lõi, kết nối hàng trăm đến hàng nghìn container trong khi cung cấp băng thông từ máy chủ đến máy chủ cao trên các vùng chứa cho khối lượng công việc thông thường, vẫn là một vấn đề đầy thách thức. Một con lai

kiến trúc chuyển mạch điện/quang để kết nối các thùng chứa được mô tả trong \[Farrington 2010\].

Một xu hướng quan trọng khác là các nhà cung cấp đám mây lớn đang ngày càng xây dựng hoặc tùy chỉnh mọi thứ trong trung tâm dữ liệu của họ, bao gồm bộ điều hợp mạng, bộ định tuyến chuyển mạch, TOR, phần mềm và giao thức mạng \[Greenberg 2015; Singh 2015\]. Một xu hướng khác do Amazon đi tiên phong là cải thiện độ tin cậy với "vùng sẵn sàng", về cơ bản tái tạo các trung tâm dữ liệu riêng biệt trong các tòa nhà khác nhau gần đó. Bằng cách đặt các tòa nhà gần đó (cách nhau vài km), dữ liệu giao dịch có thể được đồng bộ hóa giữa các trung tâm dữ liệu trong cùng một vùng sẵn sàng đồng thời cung cấp khả năng chịu lỗi \[Amazon 2014\]. Nhiều cải tiến hơn trong thiết kế trung tâm dữ liệu có thể sẽ tiếp tục xuất hiện.

**6.7 Hồi tưởng: Một ngày trong đời của một yêu cầu trang web**

Bây giờ chúng ta đã đề cập đến lớp liên kết trong chương này cũng như các lớp mạng, vận chuyển và ứng dụng trong các chương trước, hành trình của chúng ta xuống ngăn xếp giao thức đã hoàn tất! Ngay từ đầu cuốn sách này (Phần 1.1), chúng tôi đã viết "phần lớn cuốn sách này liên quan đến các giao thức mạng máy tính" và trong năm chương đầu tiên, chúng tôi chắc chắn đã thấy rằng điều này thực sự đúng! Trước khi đi vào các chương chủ đề trong phần thứ hai của cuốn sách này, chúng tôi muốn kết thúc hành trình của mình trong ngăn xếp giao thức bằng cách xem xét tổng thể, tích hợp các giao thức mà chúng tôi đã tìm hiểu cho đến nay. Sau đó, một cách để có được cái nhìn "bức tranh lớn" này là xác định nhiều (nhiều!) giao thức có liên quan đến việc đáp ứng ngay cả yêu cầu đơn giản nhất: tải xuống một trang Web. Hình 6.32 minh họa bối cảnh của chúng tôi: một sinh viên, Bob, kết nối máy tính xách tay với bộ chuyển mạch Ethernet của trường anh ấy và tải xuống một trang Web (giả sử trang chủ của www.google.com). Như chúng ta đã biết, có rất nhiều việc đang diễn ra "dưới mui xe" để đáp ứng yêu cầu tưởng chừng đơn giản này. Phòng thí nghiệm Wireshark ở cuối chương này sẽ kiểm tra các tệp theo dõi có chứa một số gói liên quan đến các tình huống tương tự một cách chi tiết hơn.

**6.7.1 Bắt đầu: DHCP, UDP, IP và Ethernet**

Giả sử Bob khởi động máy tính xách tay của mình và sau đó kết nối nó với cáp Ethernet được kết nối với bộ chuyển mạch Ethernet của trường, sau đó cáp này được kết nối với bộ định tuyến của trường, như trong Hình 6.32. Bộ định tuyến của trường được kết nối với ISP, trong ví dụ này là comcast.net. Trong ví dụ này, comcast.net đang cung cấp dịch vụ DNS cho trường học; do đó, máy chủ DNS nằm trong mạng Comcast chứ không phải mạng trường học. Chúng tôi giả định rằng máy chủ DHCP đang chạy trong bộ định tuyến, như thường lệ.

Khi Bob kết nối máy tính xách tay của mình với mạng lần đầu tiên, anh ấy không thể làm bất cứ điều gì (ví dụ: tải xuống một trang Web) nếu không có địa chỉ IP. Vì vậy, vấn đề đầu tiên liên quan đến mạng

hành động mà máy tính xách tay của Bob thực hiện là chạy giao thức DHCP để lấy địa chỉ IP cũng như các thông tin khác từ máy chủ DHCP cục bộ:

1\. Hệ điều hành trên máy tính xách tay của Bob tạo thông báo yêu cầu DHCP

(Phần 4.3.3) và đặt thông báo này trong phân đoạn UDP (Phần 3.3) với cổng đích 67 (máy chủ DHCP) và cổng nguồn 68 (máy kháchDHCP). Sau đó, phân đoạn UDP được đặt trong một gói dữ liệu IP (Phần 4.3.1) với địa chỉ đích IP phát sóng (255.255.255.255) và địa chỉ IP nguồn là 0.0.0.0, vì máy tính xách tay của Bob chưa có địa chỉ IP. 2. Sau đó, datagram IP chứa thông báo yêu cầu DHCP được đặt bên trong

khung Ethernet (Phần 6.4.2). Khung Ethernet có địa chỉ MAC đích là FF:FF:FF:FF:FF:FF để khung này sẽ được phát tới tất cả các thiết bị được kết nối với bộ chuyển mạch (hy vọng bao gồm cả máy chủ DHCP); Địa chỉ MAC nguồn của khung là địa chỉ máy tính xách tay của Bob, 00:16:D3:23:68:8A. 3. Khung Ethernet quảng bá chứa yêu cầu DHCP là khung đầu tiên

được máy tính xách tay của Bob gửi tới bộ chuyển mạch Ethernet. Switch phát khung hình đến trên tất cả các cổng đi, bao gồm cả cổng được kết nối với bộ định tuyến.

00:22:6B:45:1F:1B 68.85.2.1

00:16:D3:23:68:8A 68.85.2.101

máy chủ comcast.net DNS 68.87.71.226

www.google.com Máy chủ web 64.233.169.105

Mạng lưới trường học

68.80.2.0/24

Mạng lưới Comcast

68.80.0.0/13

Mạng của Google

64.233.160.0/19

1--7 8--13

18--24 14--17

*Hình 6.32 ♦ Một ngày trong vòng đời của một yêu cầu trang Web: Cài đặt mạng*

và hành động

4\. Bộ định tuyến nhận khung Ethernet quảng bá chứa yêu cầu DHCP

trên giao diện của nó với địa chỉ MAC 00:22:6B:45:1F:1B và gói dữ liệu IP được trích xuất từ ​​khung Ethernet. Địa chỉ đích phát sóng IP của gói dữ liệu chỉ ra rằng gói dữ liệu IP này phải được xử lý bởi các giao thức lớp trên tại nút này, do đó tải trọng của gói dữ liệu (đoạn UDP) do đó được phân kênh (Phần 3.2) lên đến UDP và thông báo yêu cầu DHCP được trích xuất từ ​​phân đoạn UDP. Máy chủ DHCP hiện có thông báo yêu cầu DHCP. 5. Giả sử rằng máy chủ DHCP chạy trong bộ định tuyến có thể phân bổ IP

địa chỉ trong khối CIDR (Phần 4.3.3) 68.85.2.0/24. Trong ví dụ này, tất cả các địa chỉ IP được sử dụng trong trường học đều nằm trong khối địa chỉ của Comcast. Giả sử máy chủ DHCP phân bổ địa chỉ 68.85.2.101 cho máy tính xách tay của Bob. Máy chủ DHCP tạo thông báo DHCP ACK (Phần 4.3.3) chứa địa chỉ IP này, cũng như địa chỉ IP của máy chủ DNS (68.87.71.226), địa chỉ IP cho bộ định tuyến cổng mặc định (68.85.2.1) và khối mạng con (68.85.2.0/24) (tương đương với "mặt nạ mạng"). Thông báo DHCP được đặt bên trong phân đoạn UDP, được đặt bên trong một datagram IP, được đặt bên trong khung Ethernet. Khung Ethernet có địa chỉ MAC nguồn của giao diện của bộ định tuyến với mạng gia đình (00:22:6B:45:1F:1B) và địa chỉ MAC đích của máy tính xách tay của Bob (00:16:D3:23:68:8A). 6. Khung Ethernet chứa DHCP ACK được bộ định tuyến gửi (unicast)

tới công tắc. Vì bộ chuyển mạch có khả năng tự học (Phần 6.4.3) và trước đó đã nhận được khung Ethernet (chứa yêu cầu DHCP) từ máy tính xách tay của Bob, nên bộ chuyển mạch chỉ biết chuyển tiếp khung có địa chỉ 00:16:D3:23:68:8A tới cổng đầu ra dẫn đến máy tính xách tay của Bob. 7. Máy tính xách tay của Bob nhận được khung Ethernet chứa DHCP ACK, trích xuất

gói dữ liệu IP từ khung Ethernet, trích xuất phân đoạn UDP từ gói dữ liệu IP và trích xuất thông báo DHCP ACK từ phân đoạn UDP. Sau đó, ứng dụng khách DHCP của Bob sẽ ghi lại địa chỉ IP của nó và địa chỉ IP của máy chủ DNS của nó. Nó cũng cài đặt địa chỉ của cổng mặc định vào bảng chuyển tiếp IP (Phần 4.1). Máy tính xách tay của Bob sẽ gửi tất cả các datagram có địa chỉ đích bên ngoài mạng con 68.85.2.0/24 của nó tới cổng mặc định. Tại thời điểm này, máy tính xách tay của Bob đã khởi tạo các thành phần mạng và sẵn sàng bắt đầu xử lý việc tìm nạp trang Web. (Lưu ý rằng chỉ có hai bước DHCP cuối cùng trong số bốn bước được trình bày ở Chương 4 là thực sự cần thiết.)

**6.7.2 Vẫn đang bắt đầu: DNS và ARP**

Khi Bob nhập URL của www.google.com vào trình duyệt Web của mình, anh ấy bắt đầu một chuỗi sự kiện dài mà cuối cùng sẽ dẫn đến việc trang chủ của Google được hiển thị trên trình duyệt Web của anh ấy. Trình duyệt Web của Bob bắt đầu quá trình bằng cách tạo một ổ cắm TCP (Phần 2.7) sẽ được sử dụng để gửi yêu cầu HTTP (Phần 2.2) tới www.google.com. Để tạo ổ cắm, máy tính xách tay của Bob cần biết

địa chỉ IP của www.google.com. Chúng ta đã tìm hiểu trong Phần 2.5 rằng giao thức DNS được sử dụng để cung cấp dịch vụ dịch địa chỉ từ tên sangIP này.

8\. Do đó, hệ điều hành trên máy tính xách tay của Bob tạo ra thông báo truy vấn DNS

(Mục 2.5.3), đưa chuỗi "www.google.com" vào phần câu hỏi của tin nhắn DNS. Thông báo DNS này sau đó được đặt trong phân đoạn UDP với cổng đích là 53 (máy chủDNS). Sau đó, phân đoạn UDP được đặt trong gói dữ liệu IP với địa chỉ đích IP là 68.87.71.226 (địa chỉ của máy chủ DNS được trả về trong DHCP ACK ở bước 5) và địa chỉ IP nguồn là 68.85.2.101. 9. Sau đó, máy tính xách tay của Bob sẽ đặt datagram chứa thông báo truy vấn DNS vào

một khung Ethernet. Khung này sẽ được gửi (được đánh địa chỉ, ở lớp liên kết) đến bộ định tuyến cổng trong mạng của trường Bob. Tuy nhiên, mặc dù máy tính xách tay của Bob biết địa chỉ IP của bộ định tuyến cổng nối của trường (68.85.2.1) thông qua thông báo DHCP ACK ở bước 5 ở trên, nhưng nó không biết địa chỉ MAC của bộ định tuyến cổng nối. Để lấy địa chỉ MAC của bộ định tuyến cổng, máy tính xách tay của Bob sẽ cần sử dụng giao thức ARP (Phần 6.4.1). 10. Máy tính xách tay của Bob tạo thông báo truy vấn ARP với địa chỉ mục tiêu IP là

68.85.2.1 (cổng mặc định), đặt thông báo ARP trong khung Ethernet có địa chỉ đích phát sóng (FF:FF:FF:FF:FF:FF) và gửi khung Ethernet tới bộ chuyển mạch, khung này sẽ phân phối khung tới tất cả các thiết bị được kết nối, bao gồm cả bộ định tuyến cổng. 11. Bộ định tuyến cổng nhận khung chứa thông báo truy vấn ARP trên

giao diện với mạng trường học và nhận thấy rằng địa chỉ IP đích là 68.85.2.1 trong thông báo ARP khớp với địa chỉ IP của giao diện của nó. Do đó, bộ định tuyến cổng chuẩn bị phản hồi ARP, chỉ ra rằng địa chỉ MAC 00:22:6B:45:1F:1B của nó tương ứng với địa chỉ IP 68.85.2.1. Nó đặt thông báo trả lời ARP trong khung Ethernet, với địa chỉ đích là 00:16:D3:23:68:8A (máy tính xách tay của Bob) và gửi khung tới bộ chuyển mạch, chuyển khung đến máy tính xách tay của Bob. 12. Máy tính xách tay của Bob nhận được khung chứa tin nhắn trả lời ARP và

trích xuất địa chỉ MAC của bộ định tuyến cổng (00:22:6B:45:1F:1B) từ tin nhắn trả lời ARP. 13. Máy tính xách tay của Bob giờ đây (cuối cùng!) có thể xử lý khung Ethernet chứa DNS

truy vấn địa chỉ MAC của bộ định tuyến cổng. Lưu ý rằng datagram IP trong khung này có địa chỉ đích IP là 68.87.71.226 (máy chủ DNS), trong khi khung có địa chỉ đích là 00:22:6B:45:1F:1B (bộ định tuyến cổng). Máy tính xách tay của Bob gửi khung này tới bộ chuyển mạch, bộ chuyển mạch này sẽ chuyển khung này đến bộ định tuyến cổng.

**6.7.3 Vẫn đang bắt đầu: Định tuyến nội miền tới máy chủ DNS**

14\. Bộ định tuyến cổng nhận khung và trích xuất gói dữ liệu IP chứa

truy vấn DNS. Router tra cứu địa chỉ đích của datagram này

(68.87.71.226) và xác định từ bảng chuyển tiếp của nó rằng datagram sẽ được gửi đến bộ định tuyến ngoài cùng bên trái trong mạng Comcast trong Hình 6.32. Gói dữ liệu IP được đặt bên trong khung lớp liên kết thích hợp cho liên kết kết nối bộ định tuyến của trường với bộ định tuyến Comcast ngoài cùng bên trái và khung được gửi qua liên kết này. 15. Bộ định tuyến ngoài cùng bên trái trong mạng Comcast nhận khung, trích xuất

IP datagram, kiểm tra địa chỉ đích của datagram (68.87.71.226) và xác định giao diện gửi đi để chuyển tiếp datagram tới máy chủ DNS từ bảng chuyển tiếp của nó, đã được điền vào bởi giao thức nội miền của Comcast (chẳng hạn như RIP, OSPF hoặc IS-IS, Phần 5.3) cũng như giao thức liên miền của Internet, BGP (Phần 5.4). 16. Cuối cùng, datagram IP chứa truy vấn DNS sẽ đến DNS

máy chủ. Máy chủ DNS trích xuất thông báo truy vấn DNS, tra cứu tên www.google.com trong cơ sở dữ liệu DNS của nó (Phần 2.5) và tìm bản ghi tài nguyên DNS chứa địa chỉ IP (64.233.169.105) cho www.google.com. (giả sử rằng nó hiện được lưu trữ trong máy chủ DNS). Hãy nhớ lại rằng dữ liệu được lưu trong bộ nhớ đệm này có nguồn gốc từ máy chủ DNS có thẩm quyền (Phần 2.5.2) cho google.com. Máy chủ DNS tạo một thông báo trả lời DNS chứa ánh xạ tên máy chủ đến địa chỉ IP này và đặt thông báo trả lời DNS trong phân đoạn UDP và phân đoạn trong gói dữ liệu IP được gửi tới máy tính xách tay của Bob (68.85.2.101). Datagram này sẽ được chuyển tiếp trở lại qua mạng Comcast tới bộ định tuyến của trường và từ đó, qua bộ chuyển mạch Ethernet tới máy tính xách tay của Bob. 17. Máy tính xách tay của Bob trích xuất địa chỉ IP của máy chủ www.google.com từ

DNS tin nhắn. Cuối cùng, sau rất nhiều nỗ lực, máy tính xách tay của Bob giờ đã sẵn sàng liên hệ với máy chủ www.google.com!

**6.7.4 Web Client-Server Tương tác: TCP và HTTP**

18\. Bây giờ máy tính xách tay của Bob có địa chỉ IP của www.google.com, nó có thể tạo

TCP socket (Phần 2.7) sẽ được sử dụng để gửi tin nhắn HTTP GET (Phần 2.2.3) tới www.google.com. Khi Bob tạo ổ cắm TCP, TCP trong máy tính xách tay của Bob trước tiên phải thực hiện bắt tay ba chiều (Phần 3.5.6) với TCP trong www.google.com. Do đó, máy tính xách tay của Bob trước tiên tạo phân đoạn TCP SYN với cổng đích 80 (dành cho HTTP), đặt phân đoạn TCP bên trong một gói dữ liệu IP có địa chỉ IP đích là 64.233.169.105 (www.google.com), đặt gói dữ liệu bên trong một khung có địa chỉ MAC đích là 00:22:6B:45:1F:1B (bộ định tuyến cổng) và gửi khung tới bộ chuyển mạch. 19. Các bộ định tuyến trong mạng trường học, mạng của Comcast và mạng của Google

chuyển tiếp datagram chứa TCP SYN tới www.google.com, sử dụng bảng chuyển tiếp trong mỗi bộ định tuyến, như trong các bước 14--16 ở trên. Hãy nhớ lại rằng các mục trong bảng chuyển tiếp bộ định tuyến quản lý việc chuyển tiếp các gói qua liên kết giữa các miền giữa mạng Comcast và Google được xác định bởi giao thức BGP (Chương 5).

20\. Cuối cùng, datagram chứa TCP SYN sẽ đến www.google.com.

Thông báo TCP SYN được trích xuất từ ​​datagram và được phân kênh tới ổ cắm chào mừng được liên kết với cổng 80. Ổ cắm kết nối (Phần 2.7) được tạo cho kết nối TCP giữa máy chủ Google HTTP và máy tính xách tay của Bob. Một phân đoạn TCP SYNACK (Phần 3.5.6) được tạo, đặt bên trong một datagram có địa chỉ tới máy tính xách tay của Bob và cuối cùng được đặt bên trong khung lớp liên kết thích hợp cho liên kết kết nối www.google.com với bộ định tuyến bước nhảy đầu tiên của nó. 21. Datagram chứa phân đoạn TCP SYNACK được chuyển tiếp qua

mạng Google, Comcast và trường học, cuối cùng là bộ điều khiển Ethernet trong máy tính xách tay của Bob. Datagram được phân kênh trong hệ điều hành tới ổ cắm TCP được tạo ở bước 18, chuyển sang trạng thái được kết nối. 22. Với ổ cắm trên máy tính xách tay của Bob bây giờ (cuối cùng!) đã sẵn sàng để gửi byte tới

www.google.com, trình duyệt của Bob tạo thông báo HTTP GET (Phần 2.2.3) chứa URL cần tìm nạp. Sau đó, thông báo HTTP GET được ghi vào ổ cắm, với thông báo GET trở thành tải trọng của phân đoạn TCP. Phân đoạn TCP được đặt trong một datagram và được gửi và gửi tới www.google.com như trong các bước 18--20 ở trên. 23. Máy chủ HTTP tại www.google.com đọc thông báo HTTP GET từ

ổ cắm TCP, tạo thông báo phản hồi HTTP (Phần 2.2), đặt nội dung trang Web được yêu cầu vào phần nội dung của thông báo phản hồi HTTP và gửi thông báo vào ổ cắm TCP. 24. Datagram chứa thông báo trả lời HTTP được chuyển tiếp qua

Mạng Google, Comcast và trường học rồi đến máy tính xách tay của Bob. Chương trình trình duyệt Web của Bob đọc phản hồi HTTP từ socket, trích xuất html cho trang Web từ nội dung của phản hồi HTTP và cuối cùng (cuối cùng!) hiển thị trang Web!

Kịch bản của chúng tôi ở trên đã bao phủ rất nhiều nền tảng mạng! Nếu bạn đã hiểu hầu hết hoặc tất cả ví dụ trên thì bạn cũng đã nắm được rất nhiều kiến ​​thức kể từ lần đầu tiên đọc Phần 1.1, nơi chúng tôi viết "phần lớn cuốn sách này liên quan đến các giao thức mạng máy tính" và bạn có thể đã tự hỏi giao thức thực sự là gì! Như ví dụ trên có vẻ chi tiết, chúng tôi đã bỏ qua một số giao thức bổ sung có thể có (ví dụ: NAT chạy trong bộ định tuyến cổng của trường, truy cập không dây vào mạng của trường, giao thức bảo mật để truy cập mạng trường học hoặc mã hóa phân đoạn hoặc gói dữ liệu, giao thức quản lý mạng) và những điều cần cân nhắc (Bộ nhớ đệm web, phân cấp DNS) mà người ta sẽ gặp phải trên Internet công cộng. Chúng ta sẽ đề cập đến một số chủ đề này và nhiều chủ đề khác trong phần thứ hai của cuốn sách này.

Cuối cùng, chúng tôi lưu ý rằng ví dụ của chúng tôi ở trên là một cái nhìn tích hợp và toàn diện, nhưng cũng rất "chi tiết" về nhiều giao thức mà chúng tôi đã nghiên cứu trong phần đầu tiên của cuốn sách này. Ví dụ này tập trung nhiều vào "làm thế nào" hơn là "tại sao". Để có cái nhìn rộng hơn, phản ánh rõ hơn về thiết kế các giao thức mạng nói chung, bạn có thể muốn đọc lại "Các nguyên tắc kiến ​​trúc của Internet" trong Phần 4.5 và các tài liệu tham khảo trong đó.

**6.8 Tóm tắt**

Trong chương này, chúng ta đã xem xét lớp liên kết---các dịch vụ của nó, các nguyên tắc cơ bản hoạt động của nó và một số giao thức cụ thể quan trọng sử dụng các nguyên tắc này trong việc triển khai các dịch vụ của lớp liên kết.

Chúng tôi thấy rằng dịch vụ cơ bản của lớp liên kết là di chuyển gói dữ liệu lớp mạng từ một nút (máy chủ, bộ chuyển mạch, bộ định tuyến, điểm truy cập WiFi) sang nút liền kề. Chúng ta thấy rằng tất cả các giao thức lớp liên kết hoạt động bằng cách đóng gói một datagram lớp mạng trong khung lớp liên kết trước khi truyền khung đó qua liên kết đến nút liền kề. Tuy nhiên, ngoài chức năng đóng khung chung này, chúng ta đã biết rằng các giao thức lớp liên kết khác nhau cung cấp các dịch vụ truy cập, phân phối và truyền dẫn liên kết rất khác nhau. Những khác biệt này một phần là do sự đa dạng của các loại liên kết mà các giao thức lớp liên kết phải hoạt động. Một liên kết điểm-điểm đơn giản có một người gửi và người nhận duy nhất giao tiếp qua một "dây" duy nhất. Một liên kết đa truy cập được chia sẻ giữa nhiều người gửi và người nhận; do đó, giao thức lớp liên kết cho kênh đa truy cập có một giao thức (giao thức đa truy cập của nó) để điều phối truy cập liên kết. Trong trường hợp MPLS, "liên kết" kết nối hai nút liền kề (ví dụ: hai bộ định tuyến IP liền kề nhau theo nghĩa IP---rằng chúng là các bộ định tuyến IP bước nhảy tiếp theo hướng tới một số đích) thực sự có thể là một mạng bên trong và của chính nó. Theo một nghĩa nào đó, ý tưởng về một mạng được coi là một liên kết có vẻ không có gì lạ. Ví dụ, một liên kết điện thoại kết nối modem/máy tính gia đình với modem/bộ định tuyến từ xa thực sự là một đường dẫn xuyên qua mạng điện thoại tinh vi và phức tạp.

Trong số các nguyên tắc cơ bản của giao tiếp lớp liên kết, chúng tôi đã kiểm tra các kỹ thuật phát hiện và sửa lỗi, nhiều giao thức truy cập, đánh địa chỉ lớp liên kết, ảo hóa (VLAN) và xây dựng mạng LAN chuyển mạch mở rộng và mạng trung tâm dữ liệu. Phần lớn sự tập trung ngày nay ở lớp liên kết là vào các mạng chuyển mạch này. Trong trường hợp phát hiện/sửa lỗi, chúng tôi đã kiểm tra cách có thể thêm các bit bổ sung vào tiêu đề của khung để phát hiện và trong một số trường hợp sửa lỗi lật bit có thể xảy ra khi khung được truyền qua liên kết. Chúng tôi đã đề cập đến các sơ đồ tính chẵn lẻ và tổng kiểm tra đơn giản, cũng như kiểm tra dự phòng theo chu kỳ mạnh mẽ hơn. Sau đó chúng tôi chuyển sang chủ đề về nhiều giao thức truy cập. Chúng tôi đã xác định và nghiên cứu ba phương pháp tiếp cận rộng rãi để điều phối quyền truy cập vào kênh quảng bá: phương pháp phân vùng kênh (TDM, FDM), phương pháp truy cập ngẫu nhiên (giao thức ALOHA và giao thức CSMA) và phương pháp tiếp cận thay phiên nhau (bỏ phiếu và chuyển mã thông báo). Chúng tôi đã nghiên cứu mạng truy cập cáp và thấy rằng nó sử dụng nhiều phương pháp đa truy cập này. Chúng tôi thấy rằng hệ quả của việc có nhiều nút chia sẻ một kênh quảng bá là nhu cầu cung cấp địa chỉ nút ở lớp liên kết. Chúng tôi đã biết rằng địa chỉ lớp liên kết khá khác với địa chỉ lớp mạng và trong trường hợp của Internet, một giao thức đặc biệt (ARP---Giao thức phân giải địa chỉ) được sử dụng để dịch giữa hai dạng địa chỉ này và đã nghiên cứu chi tiết về giao thức Ethernet cực kỳ thành công. Sau đó, chúng tôi đã kiểm tra cách các nút chia sẻ kênh phát sóng tạo thành một mạng LAN và cách nhiều mạng LAN có thể được kết nối với nhau để tạo thành các mạng LAN lớn hơn---tất cả đều không có sự can thiệp

CÁC BÀI TẬP VÀ CÂU HỎI về bài tập về nhà 519

định tuyến lớp mạng để kết nối các nút cục bộ này. Chúng tôi cũng đã tìm hiểu cách có thể tạo nhiều mạng LAN ảo trên một cơ sở hạ tầng mạng LAN vật lý.

Chúng tôi đã kết thúc nghiên cứu về lớp liên kết bằng cách tập trung vào cách mạng MPLS cung cấp dịch vụ lớp liên kết khi chúng kết nối các bộ định tuyến IP và tổng quan về thiết kế mạng cho các trung tâm dữ liệu lớn ngày nay. Chúng ta đã kết thúc chương này (và thực tế là năm chương đầu tiên) bằng cách xác định nhiều giao thức cần thiết để tìm nạp một trang Web đơn giản. Sau khi đã hoàn tất lớp liên kết, hành trình của chúng ta xuống ngăn xếp giao thức đã kết thúc! Chắc chắn, lớp vật lý nằm bên dưới lớp liên kết, nhưng các chi tiết của lớp vật lý có lẽ tốt nhất nên dành cho một khóa học khác (ví dụ: về lý thuyết truyền thông, thay vì mạng máy tính). Tuy nhiên, chúng ta đã đề cập đến một số khía cạnh của lớp vật lý trong chương này và trong Chương 1 (thảo luận của chúng ta về phương tiện vật lý trong Phần 1.2). Chúng ta sẽ xem xét lại lớp vật lý khi nghiên cứu các đặc điểm liên kết không dây trong chương tiếp theo.

Mặc dù hành trình của chúng ta về ngăn xếp giao thức đã kết thúc nhưng nghiên cứu về mạng máy tính của chúng ta vẫn chưa kết thúc. Trong ba chương tiếp theo, chúng ta sẽ đề cập đến mạng không dây, bảo mật mạng và mạng đa phương tiện. Bốn chủ đề này không thể xếp gọn vào bất kỳ một lớp nào một cách thuận tiện; thực sự, mỗi chủ đề cắt ngang nhiều lớp. Do đó, việc hiểu các chủ đề này (được coi là chủ đề nâng cao trong một số văn bản về mạng) đòi hỏi phải có nền tảng vững chắc trong tất cả các lớp của ngăn xếp giao thức---nền tảng mà nghiên cứu của chúng ta về lớp liên kết hiện đã hoàn thành!

**Bài tập về nhà vấn đề và câu hỏi**

Chương 6 Câu hỏi ôn tập

MỤC 6.1--6.2 R1. Hãy xem xét sự tương tự về vận chuyển trong Phần 6.1.1. Nếu hành khách là

Tương tự như datagram, cái gì tương tự với khung lớp liên kết? R2. Nếu tất cả các liên kết trên Internet đều cung cấp dịch vụ phân phối đáng tin cậy thì liệu

dịch vụ giao hàng đáng tin cậy TCP có dư thừa không? Tại sao hoặc tại sao không? R3. Một số dịch vụ có thể có mà giao thức lớp liên kết có thể cung cấp là gì

đến lớp mạng? Dịch vụ nào trong số các dịch vụ lớp liên kết này có dịch vụ tương ứng trong IP? Trong TCP?

MỤC 6.3 R4. Giả sử hai nút bắt đầu truyền cùng lúc một gói có độ dài L

trên kênh quảng bá có tốc độ R. Biểu thị độ trễ truyền giữa hai nút là dprop. Sẽ có va chạm nếu dprop 6 L/R? Tại sao hoặc tại sao không? R5. Trong Phần 6.3, chúng tôi đã liệt kê bốn đặc điểm mong muốn của một kênh phát sóng.

ALOHA có rãnh có những đặc điểm nào sau đây? Việc chuyển mã thông báo có những đặc điểm nào sau đây?

R6. Trong CSMA/CD, sau lần va chạm thứ năm, xác suất để một nút

chọn K = 4? Kết quả K = 4 tương ứng với độ trễ bao nhiêu giây trên mạng Ethernet 10 Mbps? R7. Mô tả các giao thức bỏ phiếu và chuyển mã thông báo bằng cách sử dụng sự tương tự của cocktail

tương tác của các bên. R8. Tại sao giao thức vòng mã thông báo sẽ không hiệu quả nếu mạng LAN có dung lượng rất lớn

chu vi?

MỤC 6.4 R9. Không gian địa chỉ MAC lớn đến mức nào? Không gian địa chỉ IPv4? IPv6

không gian địa chỉ? R10. Giả sử các nút A, B và C đều gắn vào cùng một mạng LAN quảng bá (thông qua

bộ điều hợp của họ). Nếu A gửi hàng nghìn IP datagram tới B với mỗi khung đóng gói được gửi đến địa chỉ MAC của B, bộ điều hợp của C có xử lý các khung này không? Nếu vậy, bộ điều hợp của C có chuyển các gói dữ liệu IP trong các khung này tới lớp mạng C không? Câu trả lời của bạn sẽ thay đổi như thế nào nếu A gửi các khung có địa chỉ quảng bá MAC? R11. Tại sao truy vấn ARP được gửi trong khung phát sóng? Tại sao là ARP

phản hồi được gửi trong khung có địa chỉ MAC đích cụ thể? R12. Đối với mạng trong Hình 6.19, bộ định tuyến có hai mô-đun ARP, mỗi mô-đun có

bảng ARP của riêng mình. Có thể địa chỉ MAC giống nhau xuất hiện trong cả hai bảng không? R13. So sánh cấu trúc khung của 10BASE-T, 100BASE-T và Gigabit

Ethernet. Chúng khác nhau như thế nào? R14. Hãy xem xét Hình 6.15. Có bao nhiêu mạng con, trong địa chỉ

ý nghĩa của Mục 4.3? R15. Số lượng Vlan tối đa có thể được cấu hình trên một switch là bao nhiêu?

hỗ trợ giao thức 802.1Q? Tại sao? R16. Giả sử N switch hỗ trợ nhóm K VLAN được kết nối thông qua

một giao thức trung kế. Cần bao nhiêu cổng để kết nối các switch? Biện minh cho câu trả lời của bạn.

**Vấn đề**

P1. Giả sử nội dung thông tin của gói là mẫu bit 1110 0110 1001

0101 và sơ đồ chẵn lẻ đang được sử dụng. Giá trị của trường chứa các bit chẵn lẻ sẽ là bao nhiêu trong trường hợp sơ đồ chẵn lẻ hai chiều? Câu trả lời của bạn phải sao cho trường tổng kiểm tra có độ dài tối thiểu được sử dụng. P2. Chỉ ra (đưa ra một ví dụ khác ngoài ví dụ trong Hình 6.5) rằng không gian hai chiều

kiểm tra tính chẵn lẻ có thể sửa và phát hiện một lỗi bit đơn lẻ. Chỉ ra (cho ví dụ) một lỗi bit kép có thể được phát hiện nhưng không thể sửa được.

VẤN ĐỀ 521

P3. Giả sử phần thông tin của gói (D trong Hình 6.3) chứa

10 byte bao gồm biểu diễn ASCII nhị phân không dấu 8 bit của chuỗi "Internet". Tính toán tổng kiểm tra Internet cho dữ liệu này. P4. Hãy xem xét vấn đề trước, nhưng thay vào đó, giả sử 10 byte này chứa

Một. biểu diễn nhị phân của các số từ 1 đến 10. b. biểu diễn ASCII của các chữ cái từ B đến K (chữ hoa). c. biểu diễn ASCII của các chữ cái từ b đến k (chữ thường). d. Tính toán tổng kiểm tra Internet cho dữ liệu này. P5. Xét bộ tạo 5 bit, G = 10011, và giả sử D có giá trị

1010101010. Giá trị của R là bao nhiêu? P6. Xét bài toán trước, nhưng giả sử D có giá trị

Một. 1000100101. b. 0101101010.c. 0110100011.P7. Trong bài toán này, chúng ta khám phá một số tính chất của CRC. Vì

trình tạo G (= 1001) nêu ở Mục 6.2.3, trả lời các câu hỏi sau. Một. Tại sao nó có thể phát hiện bất kỳ lỗi bit nào trong dữ liệu D? b. G ở trên có thể phát hiện bất kỳ số lỗi bit lẻ nào không? Tại sao? P8. Trong Phần 6.3, chúng tôi đã cung cấp một bản phác thảo về cách tính hiệu quả của

ALOHA có rãnh. Trong bài toán này chúng ta sẽ hoàn thành việc dẫn xuất. Một. Hãy nhớ lại rằng khi có N nút hoạt động, hiệu quả của việc phân chia rãnh

ALOHA là Np(1 - p)N-1. Tìm giá trị của p để tối đa hóa biểu thức này. b. Sử dụng giá trị của p tìm được trong (a), tìm hiệu suất của ALOHA có rãnh

bằng cách cho N tiến tới vô cùng. Gợi ý: (1 - 1/N)N tiến tới 1/e khi N tiến đến vô cùng. P9. Chứng tỏ rằng hiệu suất cực đại của ALOHA thuần túy là 1/(2e). Lưu ý: Cái này

vấn đề thật dễ dàng nếu bạn đã giải quyết được vấn đề trên! P 10. Hãy xem xét hai nút A và B sử dụng giao thức ALOHA có rãnh để điều khiển

có xu hướng cho một kênh. Giả sử nút A có nhiều dữ liệu để truyền hơn nút B và xác suất truyền lại của nút A là pA lớn hơn xác suất truyền lại của nút B, pB. Một. Cung cấp công thức tính thông lượng trung bình của nút A. Tổng cộng là bao nhiêu

hiệu quả của giao thức với hai nút này? b. Nếu pA = 2pB, thông lượng trung bình của nút A có lớn gấp đôi thông lượng của nút A không?

B? Tại sao hoặc tại sao không? Nếu không, làm thế nào bạn có thể chọn pA và pB để thực hiện điều đó?

c\. Nói chung, giả sử có N nút, trong đó nút A có truyền lại

xác suất nhiệm vụ là 2p và tất cả các nút khác có xác suất truyền lại là p. Cung cấp các biểu thức để tính thông lượng trung bình của nút A và của bất kỳ nút nào khác. P11. Giả sử bốn nút đang hoạt động---các nút A, B, C và D---đang cạnh tranh quyền truy cập

tới một kênh sử dụng ALOHA có rãnh. Giả sử mỗi nút có vô số gói cần gửi. Mỗi nút cố gắng truyền trong mỗi khe với xác suất p. Khe đầu tiên được đánh số là khe 1, khe thứ hai được đánh số là khe 2, v.v. Một. Xác suất để nút A thành công lần đầu tiên ở ô 4 là bao nhiêu? b. Xác suất để một số nút (A, B, C hoặc D) thành công trong

khe 5? c. Xác suất để thành công đầu tiên xảy ra ở ô 4 là bao nhiêu? d. Hiệu quả của hệ thống bốn nút này là gì? P12. Vẽ đồ thị hiệu quả của ALOHA được chia rãnh và ALOHA thuần túy như là một hàm của

p cho các giá trị sau của N: a. N = 10. b. N = 30. c. N = 50. P13. Hãy xem xét một kênh quảng bá có N nút và tốc độ truyền R bps.

Giả sử kênh quảng bá sử dụng tính năng thăm dò vòng (với một nút thăm dò bổ sung) cho đa truy cập. Giả sử khoảng thời gian từ khi một nút hoàn thành việc truyền cho đến khi nút tiếp theo được phép truyền (nghĩa là độ trễ kiểm soát vòng) là dpoll. Giả sử rằng trong vòng thăm dò, một nút nhất định được phép truyền tối đa Q bit. Thông lượng tối đa của kênh phát sóng là gì? P14. Hãy xem xét ba mạng LAN được kết nối với nhau bởi hai bộ định tuyến, như trong Hình 6.33.

Một. Gán địa chỉ IP cho tất cả các giao diện. Cho Subnet 1 lần sử dụng

địa chỉ dạng 192.168.1.xxx; đối với Subnet 2 sử dụng địa chỉ có dạng 192.168.2.xxx; và đối với Subnet 3, hãy sử dụng địa chỉ có dạng 192.168.3.xxx. b. Gán địa chỉ MAC cho tất cả các bộ điều hợp. c. Hãy cân nhắc việc gửi một datagram IP từ Host E tới Host B. Giả sử tất cả

các bảng ARP đã được cập nhật. Liệt kê tất cả các bước, như đã thực hiện đối với ví dụ về bộ định tuyến đơn trong Phần 6.4.1. d. Lặp lại (c), bây giờ giả sử rằng bảng ARP trong máy chủ gửi trống

(và các bảng khác được cập nhật). P15. Hãy xem xét Hình 6.33. Bây giờ chúng tôi thay thế bộ định tuyến giữa mạng con 1 và 2

bằng công tắc S1 và gắn nhãn bộ định tuyến giữa mạng con 2 và 3 là R1.

VẤN ĐỀ 523

Một. Hãy cân nhắc việc gửi một datagram IP từ Host E đến Host F. Sẽ Host E hỏi bộ định tuyến

R1 để giúp chuyển tiếp datagram? Tại sao? Trong khung Ethernet chứa gói dữ liệu IP, nguồn và đích IP và địa chỉ MAC là gì? b. Giả sử E muốn gửi một datagram IP tới B và giả sử rằng E

Bộ đệm ARP không chứa địa chỉ MAC của B. E có thực hiện truy vấn ARP để tìm địa chỉ MAC của B không? Tại sao? Trong khung Ethernet (chứa gói dữ liệu IP gửi đến B) được gửi đến bộ định tuyến R1, nguồn và đích IP và địa chỉ MAC là gì? c. Giả sử Host A muốn gửi một datagram IP tới Host B, và cả A đều không

Bộ đệm ARP chứa địa chỉ MAC của B và bộ đệm ARP của B không chứa địa chỉ MAC của A. Hơn nữa, giả sử rằng bảng chuyển tiếp của switch S1 chỉ chứa các mục dành cho Host B và bộ định tuyến R1. Do đó, A sẽ phát đi thông báo yêu cầu ARP. S1 sẽ thực hiện hành động gì sau khi nhận được thông báo yêu cầu ARP? Bộ định tuyến R1 cũng sẽ nhận được thông báo yêu cầu ARP này phải không? Nếu vậy, R1 có chuyển tiếp tin nhắn tới Subnet 3 không? Sau khi Host B nhận được tin nhắn yêu cầu ARP này, nó sẽ gửi lại cho Host A một tin nhắn phản hồi ARP. Nhưng nó có gửi tin nhắn truy vấn ARP để hỏi địa chỉ MAC của A không? Tại sao? Switch S1 sẽ làm gì khi nhận được tin nhắn phản hồi ARP từ Host B? P16. Hãy xem xét vấn đề trước đó, nhưng bây giờ giả sử rằng bộ định tuyến giữa các thiết bị phụ

lưới 2 và 3 được thay thế bằng switch. Trả lời các câu hỏi (a)--(c) ở bài toán trước trong bối cảnh mới này.

*Hình 6.33 ♦ Ba mạng con, được kết nối với nhau bằng bộ định tuyến*

Subnet 3

E

F

C

Subnet 2

D

MỘT

B

Subnet 1

**P17. Hãy nhớ lại rằng với giao thức CSMA/CD, adapter đợi K#512 bit lần**

sau va chạm, trong đó K được rút ngẫu nhiên. Với K = 100, bộ điều hợp phải đợi bao lâu cho đến khi quay lại Bước 2 đối với kênh quảng bá 100 Mbps? Đối với kênh phát sóng 1 Gbps? P18. Giả sử các nút A và B nằm trên cùng một kênh quảng bá 10 Mbps và

độ trễ truyền giữa hai nút là 325 bit lần. Giả sử các gói CSMA/CD và Ethernet được sử dụng cho kênh quảng bá này. Giả sử nút A bắt đầu truyền một khung và trước khi kết thúc, nút B bắt đầu truyền một khung. A có thể kết thúc quá trình truyền trước khi phát hiện B đã truyền không? Tại sao hoặc tại sao không? Nếu câu trả lời là có thì A tin nhầm rằng khung của nó đã được truyền thành công mà không xảy ra xung đột. Gợi ý: Giả sử tại thời điểm t = 0 bit, A bắt đầu truyền một khung. Trong trường hợp xấu nhất, A truyền khung có kích thước tối thiểu 512 + 64 bit lần. Vì vậy A sẽ kết thúc việc truyền khung hình ở thời điểm t = 512 + 64 bit. Vì vậy, câu trả lời là không, nếu tín hiệu của B đến A trước thời gian bit t = 512 + 64 bit. Trong trường hợp xấu nhất, khi nào tín hiệu của B đến được A? P19. Giả sử các nút A và B nằm trên cùng một kênh quảng bá 10 Mbps và

độ trễ truyền giữa hai nút là 245 bit lần. Giả sử A và B gửi các khung Ethernet cùng lúc, các khung này va chạm nhau, sau đó A và B chọn các giá trị K khác nhau trong thuật toán CSMA/CD. Giả sử không có nút nào khác đang hoạt động, việc truyền lại từ A và B có thể xung đột với nhau không? Đối với mục đích của chúng ta, chỉ cần thực hiện ví dụ sau là đủ. Giả sử A và B bắt đầu truyền ở thời điểm t = 0 bit. Cả hai đều phát hiện va chạm ở thời điểm t = 245 t bit. Giả sử KA = 0 và KB = 1. B lập kế hoạch truyền lại vào thời điểm nào? A bắt đầu truyền tin vào thời điểm nào? (Lưu ý: Các nút phải đợi kênh nhàn rỗi sau khi quay lại Bước 2---xem giao thức.) Tín hiệu của A đến B vào thời điểm nào? B có hạn chế truyền tin vào thời gian đã định không? P20. Trong bài toán này, bạn sẽ tính được hiệu quả của bội số giống CSMA/CD

giao thức truy cập. Trong giao thức này, thời gian được chia thành các khe và tất cả các bộ điều hợp đều được đồng bộ hóa với các khe đó. Tuy nhiên, không giống như ALOHA có rãnh, độ dài của một khe (tính bằng giây) nhỏ hơn nhiều so với thời gian khung (thời gian để truyền một khung). Gọi S là chiều dài của một khe. Giả sử tất cả các khung có độ dài không đổi L = kRS, trong đó R là tốc độ truyền của kênh và k là số nguyên lớn. Giả sử có N nút, mỗi nút có số lượng khung vô hạn để gửi. Chúng tôi cũng giả định rằng dprop 6 S, sao cho tất cả các nút có thể phát hiện xung đột trước khi kết thúc một khe thời gian. Giao thức như sau: • Nếu, đối với một khe nhất định, không có nút nào sở hữu kênh, tất cả các nút tranh giành kênh; cụ thể, mỗi nút truyền trong khe với xác suất p. Nếu chính xác một nút truyền trong khe, nút đó sẽ chiếm hữu kênh cho k - 1 khe tiếp theo và truyền toàn bộ khung của nó.

• Nếu một số nút sở hữu kênh, tất cả các nút khác sẽ không truyền cho đến khi nút sở hữu kênh đó truyền xong khung của nó. Khi nút này đã truyền khung của nó, tất cả các nút sẽ tranh giành kênh.

Lưu ý rằng kênh luân phiên giữa hai trạng thái: trạng thái sản xuất,

kéo dài chính xác k ô và trạng thái không sản xuất, kéo dài trong một số ô ngẫu nhiên. Rõ ràng, hiệu suất kênh là tỷ lệ k/(k + x), trong đó x là số lượng khe không hiệu quả liên tiếp dự kiến.

Một. Với N và p cố định, hãy xác định hiệu quả của giao thức này.

b\. Với N cố định, hãy xác định p để tối đa hóa hiệu quả.

c\. Sử dụng p (là hàm số của N) tìm được trong (b), hãy xác định hiệu quả

ciency khi N tiến tới vô cùng.

d\. Chứng minh rằng hiệu suất này tiến tới 1 khi độ dài khung hình trở nên lớn.

P21. Xét hình 6.33 trong bài toán P14. Cung cấp địa chỉ MAC và IP

địa chỉ cho các giao diện tại Host A, cả hai bộ định tuyến và Host F. Giả sử Host A gửi một gói dữ liệu đến Host F. Cung cấp địa chỉ MAC nguồn và đích trong khung đóng gói gói dữ liệu IP này khi khung được truyền (i) từ A đến bộ định tuyến bên trái, (ii) từ bộ định tuyến bên trái đến bộ định tuyến bên phải, (iii) từ bộ định tuyến phù hợp tới F. Đồng thời cung cấp địa chỉ nguồn và đích IP trong gói dữ liệu IP được gói gọn trong khung tại mỗi thời điểm này.

P22. Bây giờ giả sử rằng bộ định tuyến ngoài cùng bên trái trong Hình 6.33 được thay thế bằng một bộ chuyển mạch.

Hosts A, B, C, D và bộ định tuyến bên phải đều được kết nối hình sao vào bộ chuyển mạch này. Cung cấp địa chỉ MAC nguồn và đích trong khung đóng gói gói dữ liệu IP này khi khung được truyền (i) từ A đến bộ chuyển mạch, (ii) từ bộ chuyển mạch sang bộ định tuyến bên phải, (iii) từ bộ định tuyến bên phải đến F. Đồng thời cung cấp địa chỉ nguồn và đích IP trong gói dữ liệu IP được đóng gói trong khung tại mỗi thời điểm này.

P23. Hãy xem xét Hình 6.15. Giả sử rằng tất cả các liên kết là 1 Gbps. Tối đa là gì?

tổng thông lượng tổng hợp có thể đạt được giữa 9 máy chủ và 2 máy chủ trong mạng này? Bạn có thể giả định rằng bất kỳ máy chủ hoặc máy chủ nào cũng có thể gửi đến bất kỳ máy chủ hoặc máy chủ nào khác. Tại sao?

P24. Giả sử ba thiết bị chuyển mạch phòng ban trong Hình 6.15 được thay thế bằng các hub.

Tất cả các liên kết là 1 Gbps. Bây giờ hãy trả lời các câu hỏi đặt ra ở bài P23.

P25. Giả sử rằng tất cả các switch trong Hình 6.15 đều được thay thế bằng hub. Tất cả các liên kết

là 1Gbps. Bây giờ hãy trả lời các câu hỏi đặt ra ở bài P23.

P26. Hãy xem xét hoạt động của một learning switch trong bối cảnh mạng

trong đó 6 nút có nhãn từ A đến F được kết nối hình sao vào một bộ chuyển mạch Ethernet. Giả sử (i) B gửi một khung cho E, (ii) E trả lời bằng một khung cho B, (iii) A gửi một khung cho B, (iv) B trả lời bằng một khung cho A. Bảng chuyển đổi

VẤN ĐỀ 525

ban đầu trống rỗng. Hiển thị trạng thái của bảng chuyển đổi trước và sau mỗi sự kiện này. Đối với mỗi sự kiện này, hãy xác định (các) liên kết mà khung được truyền sẽ được chuyển tiếp trên đó và giải thích ngắn gọn câu trả lời của bạn. P27. Trong vấn đề này, chúng tôi khám phá việc sử dụng các gói nhỏ cho ứng dụng Voice-over-IP

cation. Một trong những nhược điểm của kích thước gói nhỏ là phần lớn băng thông liên kết bị tiêu thụ bởi các byte trên cao. Cuối cùng, giả sử gói bao gồm P byte và 5 byte tiêu đề. Một. Hãy cân nhắc việc gửi trực tiếp nguồn giọng nói được mã hóa kỹ thuật số. Giả sử

nguồn được mã hóa ở tốc độ không đổi 128 kbps. Giả sử mỗi gói được lấp đầy hoàn toàn trước khi nguồn gửi gói vào mạng. Thời gian cần thiết để lấp đầy một gói là độ trễ đóng gói. Theo L, hãy xác định độ trễ đóng gói tính bằng mili giây. b. Độ trễ đóng gói lớn hơn 20 mili giây có thể gây ra sự cố đáng chú ý và

tiếng vang khó chịu. Xác định độ trễ đóng gói cho L = 1.500 byte (tương ứng với gói Ethernet có kích thước tối đa) và cho L = 50 (tương ứng với gói ATM). c. Tính toán độ trễ lưu trữ và chuyển tiếp tại một switch duy nhất với tốc độ liên kết là

R = 622 Mbps cho L = 1.500 byte và cho L = 50 byte. d. Nhận xét về lợi ích của việc sử dụng kích thước gói nhỏ. P28. Hãy xem xét VLAN chuyển mạch đơn trong Hình 6.25 và giả sử một mạng bên ngoài

bộ định tuyến được kết nối với cổng chuyển đổi 1. Gán địa chỉ IP cho máy chủ EE và CS và giao diện bộ định tuyến. Theo dõi các bước được thực hiện ở cả lớp mạng và lớp liên kết để truyền một gói dữ liệu IP từ máy chủ EE sang máy chủ CS (Gợi ý: Đọc lại phần thảo luận về Hình 6.19 trong văn bản). P29. Hãy xem xét mạng MPLS được hiển thị trong Hình 6.29 và giả sử rằng định tuyến-

ers R5 và R6 hiện đã được kích hoạt MPLS. Giả sử chúng ta muốn thực hiện kỹ thuật lưu lượng để các gói từ R6 dành cho A được chuyển sang A qua R6-R4-R3-R1 và các gói từ R5 dành cho A được chuyển qua R5-R4-R2-R1. Hiển thị các bảng MPLS trong R5 và R6, cũng như bảng đã sửa đổi trong R4, điều đó sẽ giúp thực hiện được điều này. P30. Hãy xem xét lại tình huống tương tự như trong bài toán trước, nhưng giả sử

các gói từ R6 dành cho D được chuyển qua R6-R4-R3, trong khi các gói từ R5 đến D được chuyển qua R4-R2-R1-R3. Hiển thị các bảng MPLS trong tất cả các bộ định tuyến để thực hiện điều này. P31. Trong bài toán này, bạn sẽ tập hợp phần lớn những gì bạn đã học về

Các giao thức Internet. Giả sử bạn bước vào một căn phòng, kết nối với Ethernet và muốn tải xuống một trang Web. Tất cả các bước giao thức diễn ra là gì, bắt đầu từ việc bật nguồn PC cho đến truy cập trang Web? Giả sử không có gì trong DNS hoặc bộ nhớ đệm của trình duyệt khi bạn bật PC.

PHÒNG THÍ NGHIỆM WIRESHARK: 802.11 ETHERNET 527

(Gợi ý: Các bước bao gồm việc sử dụng các giao thức Ethernet, DHCP, ARP, DNS, TCP và HTTP.) Chỉ rõ rõ ràng trong các bước của bạn cách bạn lấy IP và địa chỉ MAC của bộ định tuyến cổng. P32. Hãy xem xét mạng trung tâm dữ liệu với cấu trúc liên kết phân cấp trong Hình 6.30.

Giả sử bây giờ có 80 cặp luồng, với 10 luồng giữa giá thứ nhất và thứ chín, 10 luồng giữa giá thứ hai và thứ mười, v.v. Hơn nữa, giả sử rằng tất cả các liên kết trong mạng là 10 Gbps, ngoại trừ các liên kết giữa máy chủ và bộ chuyển mạch TOR là 1 Gbps. Một. Mỗi luồng có cùng tốc độ dữ liệu; xác định tốc độ tối đa của dòng chảy. b. Đối với cùng một kiểu lưu lượng, hãy xác định tốc độ tối đa của luồng cho

cấu trúc liên kết có tính liên kết cao trong Hình 6.31. c. Bây giờ giả sử có một mẫu lưu lượng truy cập tương tự nhưng liên quan đến 20 máy chủ trên

mỗi giá và 160 cặp dòng chảy. Xác định tốc độ dòng chảy tối đa cho hai cấu trúc liên kết. P33. Hãy xem xét mạng phân cấp trong Hình 6.30 và giả sử rằng dữ liệu

center cần hỗ trợ phân phối e-mail và video giữa các ứng dụng khác. Giả sử bốn khung máy chủ được dành riêng cho e-mail và bốn khung dành riêng cho video. Đối với mỗi ứng dụng, tất cả bốn giá đỡ phải nằm bên dưới một bộ chuyển mạch cấp 2 vì các liên kết cấp 2 đến cấp 1 không có đủ băng thông để hỗ trợ lưu lượng truy cập trong ứng dụng. Đối với ứng dụng e-mail, giả sử rằng trong 99,9% thời gian chỉ có ba giá đỡ được sử dụng và ứng dụng video có các kiểu sử dụng giống hệt nhau. Một. Ứng dụng e-mail cần sử dụng phần thứ tư trong khoảng thời gian nào?

giá đỡ? Còn đối với ứng dụng video thì sao? b. Giả sử việc sử dụng e-mail và việc sử dụng video là độc lập thì phần nào

bao lâu thì (tương đương, xác suất để) cả hai ứng dụng đều cần giá đỡ thứ tư là bao nhiêu? c. Giả sử rằng việc một ứng dụng thiếu hụt dịch vụ là có thể chấp nhận được.

ers trong 0,001 phần trăm thời gian hoặc ít hơn (gây ra tình trạng suy giảm hiệu suất trong những khoảng thời gian hiếm gặp đối với người dùng). Thảo luận cách sử dụng cấu trúc liên kết trong Hình 6.31 sao cho chỉ có bảy giá được gán chung cho hai ứng dụng (giả sử rằng cấu trúc liên kết có thể hỗ trợ tất cả lưu lượng).

**Wireshark Phòng thí nghiệm: Ethernet 802.11**

Tại trang web Companion dành cho sách giáo khoa này, http://www.pearsonhighered.com/cs-resources/, bạn sẽ tìm thấy phòng thí nghiệm Wireshark kiểm tra hoạt động của giao thức IEEE 802.3 và định dạng khung Wireshark. Phòng thí nghiệm Wireshark thứ hai kiểm tra dấu vết gói được thực hiện trong kịch bản mạng gia đình.

**Albert Greenberg**

PHỎNG VẤN VỚI...

Albert Greenberg là Phó chủ tịch tập đoàn Microsoft phụ trách Mạng Azure. Ông lãnh đạo quá trình phát triển của nhóm Azure Networking, nhóm chịu trách nhiệm kết nối mạng R&D tại Microsoft - trong và xuyên suốt các trung tâm dữ liệu cũng như các địa điểm biên; mạng lưới mặt đất và dưới biển toàn cầu; mạng quang; giảm tải FPGA và SmartNIC; truy cập và kết nối mạng đám mây lai; mạng máy chủ và ảo hóa mạng; bộ cân bằng tải ứng dụng và các thiết bị ảo mạng; dịch vụ và phân tích mạng; dịch vụ an ninh; mạng container; mạng phân phối nội dung; mạng biên bao gồm tăng tốc ứng dụng và 5G cũng như mạng của bên thứ nhất. Để đáp ứng những thách thức về tính linh hoạt và chất lượng đi kèm với quy mô đám mây, nhóm của anh đã phát triển và áp dụng phần cứng tùy chỉnh, máy học và nguồn mở. Albert chuyển đến Microsoft vào năm 2007 để đổi mới trên Đám mây và đưa mạng vào máy chủ (ảo hóa mạng), trong số rất nhiều ý tưởng đã xuất hiện trong bài báo VL2 của anh ấy và nền tảng của mạng Đám mây ngày nay.

Trước khi gia nhập Microsoft, Albert đã làm việc tại Bell Labs và AT&T Labs với tư cách là thành viên AT&T. Ông đã giúp xây dựng các hệ thống và công cụ chạy mạng của AT&T, đồng thời đi tiên phong về kiến ​​trúc và hệ thống trên nền tảng của mạng được xác định bằng phần mềm. Ông có bằng AB về Toán học của Đại học Dartmouth và bằng Tiến sĩ Khoa học Máy tính của Đại học Washington.

Albert là thành viên của Học viện Kỹ thuật Quốc gia và là thành viên ACM. Ông đã nhận được Giải thưởng Máy tính và Truyền thông IEEE Koji Kobayashi, Giải thưởng ACM Sigcomm, và các giải thưởng bài báo ACM Sigcomm và Sigmetrics Test of Time. Albert và vợ Kathryn là bậc cha mẹ đáng tự hào của bốn cô con gái. Anh lớn lên ở New Orleans. Trong khi Seattle Seahawks là đội của anh ấy, anh ấy không thể lay chuyển được tình cảm của mình dành cho Saints.

![](media/image3.png){width="5.5in" height="7.062255030621173in"}

Điều gì đã đưa bạn đến với chuyên ngành mạng?

Tôi luôn thích giải quyết các vấn đề trong thế giới thực và cũng thích toán học. Tôi nhận thấy rằng lĩnh vực kết nối mạng có rất nhiều không gian và phạm vi để thực hiện cả hai điều đó. Sự kết hợp đó rất hấp dẫn đối với tôi. Trong khi làm luận án tiến sĩ tại Đại học Washington, tôi đã được hưởng lợi từ ảnh hưởng của Ed Lazowska về mặt hệ thống, cũng như Richard Ladner và Martin Tompa về mặt toán học và lý thuyết. Một trong những dự án khóa học MS của tôi là làm cho hai máy từ cùng một nhà cung cấp có thể nói chuyện với nhau. Bây giờ có vẻ như bạn không thể ngăn máy móc liên lạc!

Bạn có lời khuyên nào dành cho các sinh viên đang theo học lĩnh vực mạng/Internet không?

Bộ mặt của mạng đang thay đổi. Nó đang trở thành một môi trường rất đa dạng, hòa nhập và cởi mở. Ý tôi là theo hai cách. Đầu tiên, chúng ta sẽ thấy sự đa dạng hơn nhiều giữa các nhà phát triển và nhà nghiên cứu mạng của chúng ta, bao gồm cả phụ nữ và các nhóm ít được đại diện khác trong lĩnh vực công nghệ. Tôi tự hào về sự đa dạng và hòa nhập của nhóm tại Microsoft cũng như các nhóm trước đây của tôi tại AT&T. Sự đa dạng giúp chúng ta kiên cường hơn, có khả năng thích ứng tốt hơn với sự thay đổi và đưa ra quyết định tốt hơn. Thứ hai, người ta có thể mang lại sự đa dạng về kỹ năng và sở thích kỹ thuật cho mạng lưới. Những mối quan tâm đó có thể là về kiến ​​trúc, ngôn ngữ lập trình, quang học, phương pháp hình thức, khoa học dữ liệu, AI hoặc thiết kế hệ thống đáng tin cậy và có khả năng chịu lỗi. Các hệ thống nguồn mở đang có tác động to lớn. SONiC, một sáng kiến ​​nguồn mở dựa trên Linux dành cho các hệ điều hành mạng, là một ví dụ điển hình. Hãy đọc cuốn sách này và vận dụng toàn bộ kỹ năng, kinh nghiệm và kiến ​​thức của bạn để tạo ra các mạng lưới trong tương lai. SDN và Phân tổ mang lại sự đa dạng và cởi mở. Thật thú vị.

Bạn có thể mô tả một hoặc hai dự án thú vị nhất mà bạn đã thực hiện trong sự nghiệp của mình không? Những thách thức lớn nhất là gì?

Cho đến nay, đám mây là thứ lớn nhất sẽ xuất hiện trong một thời gian dài. Những thách thức ở đó vượt trội so với những thách thức hệ thống khác mà tôi đã từng giải quyết, một phần vì đám mây kết hợp rất nhiều khía cạnh của hệ thống. Các kịch bản đám mây đặt ra thách thức rất lớn cho việc kết nối mạng. Công nghệ mạng truyền thống chỉ là một phần của nó; trong thực tế ngày nay có hệ điều hành và hệ thống phân tán, kiến ​​trúc, hiệu suất, bảo mật, độ tin cậy, học máy, khoa học dữ liệu và quản lý -- toàn bộ hệ thống. Nếu chúng ta từng nghĩ những khu vực riêng lẻ này là những "khu vườn", thì chúng ta có thể nghĩ đám mây như một "trang trại" được tạo thành từ tất cả những khu vườn tuyệt vời này. Và mối quan tâm vận hành trong việc thiết kế, giám sát và quản lý một hệ thống quy mô toàn cầu cực kỳ đáng tin cậy là rất quan trọng vì đám mây cung cấp cơ sở hạ tầng cực kỳ quan trọng cho chính phủ, ngành công nghiệp, giáo dục, v.v. Tất cả những điều đó phải vững chắc; nó cần được an toàn; nó cần phải đáng tin cậy. Tất nhiên, phần mềm là chìa khóa để giám sát và quản lý hiệu quả một đám mây khổng lồ như vậy. Ở đây, SDN đóng vai trò trung tâm trong việc quản lý và cung cấp trên quy mô lớn, về bản chất, tạo ra một trung tâm dữ liệu được xác định bằng phần mềm. Phần mềm cũng cho phép chúng tôi đổi mới nhanh chóng.

Bạn hình dung thế nào về tương lai của mạng và Internet? Bạn nghĩ những thách thức/trở ngại lớn nào đang ở phía trước trong quá trình phát triển của họ, đặc biệt là trong lĩnh vực mạng trung tâm dữ liệu và mạng biên?

Tôi đã nói về Cloud và chúng tôi chỉ nói 10% trong quá trình phát triển của nó. Tuy nhiên, rõ ràng là việc phân chia công việc trong hệ thống end-to-end sẽ ngày càng trở thành một vấn đề quan trọng. Bao nhiêu tính toán và lưu trữ sẽ diễn ra trong ứng dụng và ở máy chủ cuối? Bao nhiêu điều sẽ xảy ra trong các thành phần đám mây ở "cạnh" của mạng, tại hoặc gần máy chủ hoặc vùng chứa cuối? Và bao nhiêu điều sẽ xảy ra trong chính các trung tâm dữ liệu. Tất cả những điều này sẽ được sắp xếp như thế nào? Chúng ta sẽ thấy điện toán đám mây được đẩy đến gần bờ hơn và chúng ta sẽ thấy sự tăng trưởng "theo chiều ngang" -- một hệ sinh thái mạng/dữ liệu/điện toán toàn diện phong phú hơn -- không chỉ tăng trưởng, chẳng hạn như trong một trung tâm dữ liệu. Đây sẽ là một lĩnh vực có nhiều đổi mới. Mạng không dây 5G sẽ là một phần quan trọng của sự kết hợp này.

Ai đã truyền cảm hứng cho bạn một cách chuyên nghiệp?

Tôi đã học được rất nhiều điều, ở cả Microsoft và AT&T, từ khách hàng và từ trang web trực tiếp. Việc tương tác với các kỹ sư đã truyền cảm hứng cho tôi vì niềm đam mê của họ đối với nhà phát triển và nhà phát triển trong toàn bộ vòng đời (từ phát minh đến phát triển đến triển khai đến ngừng hoạt động cuối cùng) của các hệ thống và dịch vụ vận hành. Đây là những người am hiểu kiến ​​trúc và hệ thống từ đầu đến cuối, từ trong ra ngoài. Họ thật tuyệt khi được làm việc cùng và có rất nhiều hiểu biết sâu sắc, kinh nghiệm cũng như kiến ​​thức để chia sẻ, cho dù đó là Azure Cloud của Microsoft hay trước đó trong mạng lưới AT&T trong sự nghiệp của tôi. Tôi cũng thích làm việc với các nhà nghiên cứu, những người đã thiết lập một số nguyên tắc cơ bản cho việc thiết kế và quản lý các hệ thống quy mô lớn này.

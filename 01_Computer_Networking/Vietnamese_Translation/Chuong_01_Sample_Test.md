**Chương 1: Mạng Máy Tính và Internet**

Internet ngày nay được coi là hệ thống kỹ thuật lớn nhất từng được nhân loại tạo ra, với hàng trăm triệu máy tính, liên kết truyền thông và Switch được kết nối; với hàng tỷ người dùng kết nối qua máy tính xách tay, máy tính bảng và điện thoại thông minh; cùng với hàng loạt các \"vật kết nối Internet\" mới bao gồm máy chơi game, hệ thống giám sát, đồng hồ, kính mắt, bộ điều nhiệt và ô tô. Với quy mô to lớn cùng vô số thành phần và ứng dụng đa dạng như vậy, liệu có hy vọng nào để hiểu được cách thức Internet vận hành hay không? Liệu có những nguyên tắc chỉ đạo và cấu trúc cốt lõi nào có thể cung cấp nền tảng để hiểu một hệ thống lớn và phức tạp đến kinh ngạc như vậy không? Và nếu có, liệu việc tìm hiểu về mạng máy tính có thực sự vừa thú vị vừa hấp dẫn không? Thật may mắn, câu trả lời cho tất cả các câu hỏi này là một tiếng CÓ vang dội! Quả thực, mục tiêu của chúng tôi trong cuốn sách này là mang đến cho bạn một phần giới thiệu hiện đại về lĩnh vực mạng máy tính đầy năng động, cung cấp cho bạn những nguyên tắc và hiểu biết thực tiễn cần thiết để hiểu không chỉ các mạng ngày nay mà còn cả các mạng trong tương lai.

Chương đầu tiên này trình bày một cái nhìn tổng quan sâu rộng về mạng máy tính và Internet. Mục tiêu ở đây là vẽ nên một bức tranh toàn cảnh và thiết lập bối cảnh cho phần còn lại của cuốn sách, giúp ta thấy được cả khu rừng thay vì chỉ nhìn từng cái cây. Chúng ta sẽ tìm hiểu nhiều khía cạnh trong chương giới thiệu này và thảo luận về nhiều thành phần cấu thành một mạng máy tính mà không làm mất đi bức tranh tổng thể.

Chúng tôi cấu trúc phần tổng quan về mạng máy tính trong chương này như sau. Sau khi giới thiệu một số thuật ngữ và khái niệm cơ bản, trước tiên chúng ta sẽ xem xét các thành phần phần cứng và phần mềm cơ bản tạo nên mạng. Chúng ta sẽ bắt đầu từ biên mạng (network edge) và tìm hiểu về các End Systems cùng các ứng dụng mạng đang chạy trên mạng. Sau đó, chúng ta sẽ khám phá lõi mạng (network core), xem xét các liên kết

**CHƯƠNG**

**Mạng Máy Tính và Internet**

![](media/image1.png){width="5.5in" height="6.930965660542432in"}

![](media/image2.png){width="5.5in" height="0.9567311898512686in"}

và các Switch dùng để truyền tải dữ liệu, cũng như các mạng truy cập (access networks) và phương tiện vật lý kết nối các End Systems với lõi mạng. Chúng ta sẽ hiểu rằng Internet là một mạng của các mạng, và tìm hiểu cách các mạng này kết nối với nhau.

Sau khi hoàn thành phần tổng quan về biên và lõi của mạng máy tính, chúng ta sẽ có cái nhìn rộng hơn và trừu tượng hơn trong nửa sau của chương này. Chúng ta sẽ xem xét độ trễ (delay), mất gói (loss) và thông lượng (throughput) dữ liệu trong mạng máy tính và cung cấp các mô hình định lượng đơn giản cho thông lượng và độ trễ đầu-cuối: các mô hình tính đến độ trễ truyền dẫn (transmission delay), độ trễ lan truyền (propagation delay) và độ trễ hàng đợi (queuing delay). Sau đó, chúng ta sẽ giới thiệu một số nguyên tắc kiến trúc then chốt trong mạng máy tính, cụ thể là phân tầng giao thức (protocol layering) và các mô hình dịch vụ (service models). Chúng ta cũng sẽ tìm hiểu rằng các mạng máy tính dễ bị tổn thương trước nhiều loại tấn công khác nhau; chúng ta sẽ khảo sát một số cuộc tấn công này và xem xét cách làm cho mạng máy tính trở nên an toàn hơn. Cuối cùng, chúng ta sẽ khép lại chương này với một lược sử ngắn gọn về mạng máy tính.

**1.1 Internet là gì?**

Trong cuốn sách này, chúng tôi sử dụng mạng Internet công cộng --- một mạng máy tính cụ thể --- làm phương tiện chính để thảo luận về mạng máy tính và các giao thức mạng. Nhưng Internet là gì? Có một vài cách để trả lời câu hỏi này. Đầu tiên, chúng ta có thể mô tả các thành phần cơ bản (nuts-and-bolts) của Internet, tức là các thành phần phần cứng và phần mềm cơ bản cấu thành nên Internet. Thứ hai, chúng ta có thể mô tả Internet dưới góc độ một cơ sở hạ tầng mạng cung cấp dịch vụ cho các ứng dụng phân tán. Hãy bắt đầu với mô tả các thành phần cơ bản, sử dụng Hình 1.1 để minh họa cho phần thảo luận của chúng ta.

**1.1.1 Mô tả các thành phần cơ bản (Nuts-and-Bolts)**

Internet là một mạng máy tính kết nối hàng tỷ thiết bị tính toán trên toàn thế giới. Cách đây không lâu, các thiết bị tính toán này chủ yếu là máy tính để bàn truyền thống, máy trạm Linux và các Server lưu trữ và truyền tải thông tin như trang Web và thư điện tử. Tuy nhiên, ngày càng có nhiều người dùng kết nối Internet bằng điện thoại thông minh và máy tính bảng --- ngày nay, gần một nửa dân số thế giới là người dùng Internet di động tích cực với tỷ lệ dự kiến sẽ tăng lên 75% vào năm 2025 \[Statista 2019\]. Hơn nữa, các \"vật thể\" phi truyền thống kết nối Internet như TV, máy chơi game, bộ điều nhiệt, hệ thống an ninh gia đình, đồ gia dụng, đồng hồ, kính mắt, ô tô, hệ thống điều khiển giao thông, v.v. đang được kết nối với Internet. Quả thực, thuật ngữ mạng máy tính bắt đầu nghe có vẻ hơi cũ kỹ trước vô số thiết bị phi truyền thống đang được kết nối vào Internet. Trong thuật ngữ chuyên môn về Internet, tất cả các thiết bị này được gọi là Hosts hoặc End Systems. Theo một số ước tính, có khoảng 18 tỷ thiết bị được kết nối với Internet vào năm 2017, và con số này sẽ đạt 28,5 tỷ vào năm 2022 \[Cisco VNI 2020\].

*Hình 1.1 ♦ Một số thành phần của Internet*

Chú giải:

Đèn giao thông Bộ điều nhiệt Tủ lạnh Datacenter Workstation

Host (= End System)

Máy tính di động

Trạm thu phát (Base station) Router Điện thoại di động

Tháp thu phát Smartphone

hoặc máy tính bảng Link-layer

Switch Server

Content Provider Network (Mạng nhà cung cấp nội dung)

Quốc gia hoặc

Global ISP (ISP Toàn cầu)

Datacenter Network (Mạng trung tâm dữ liệu)

Datacenter Network (Mạng trung tâm dữ liệu)

Mobile Network (Mạng di động)

Enterprise Network (Mạng doanh nghiệp)

Home Network (Mạng gia đình)

Local or Regional ISP (ISP Địa phương hoặc Khu vực)

Các End Systems được kết nối với nhau bằng một mạng lưới các liên kết truyền thông và thiết bị chuyển mạch gói (packet switches). Trong Mục 1.2, chúng ta sẽ thấy rằng có nhiều loại liên kết truyền thông, được tạo thành từ các loại phương tiện vật lý khác nhau bao gồm cáp đồng trục, dây đồng, sợi quang và phổ sóng vô tuyến. Các liên kết khác nhau có thể truyền dữ liệu ở tốc độ khác nhau, với tốc độ truyền dẫn của một liên kết được đo bằng bit/giây. Khi một End System có dữ liệu muốn gửi đến một End System khác, End System gửi sẽ phân đoạn dữ liệu và thêm các byte tiêu đề (header) vào mỗi phân đoạn. Các gói thông tin kết quả, được gọi là Packets trong thuật ngữ mạng máy tính, sau đó được gửi qua mạng đến End System đích, nơi chúng được ghép nối lại thành dữ liệu ban đầu.

Một bộ chuyển mạch gói (packet switch) tiếp nhận một Packet đến trên một trong các liên kết truyền thông đầu vào của nó và chuyển tiếp Packet đó trên một trong các liên kết truyền thông đầu ra. Bộ chuyển mạch gói có nhiều hình dạng và chủng loại, nhưng hai loại nổi bật nhất trong Internet ngày nay là Routers và Link-layer Switches. Cả hai loại thiết bị chuyển mạch này đều chuyển tiếp các Packets về phía đích cuối cùng của chúng. Link-layer Switches thường được sử dụng trong các mạng truy cập, trong khi Routers thường được sử dụng trong lõi mạng (network core). Trình tự các liên kết truyền thông và bộ chuyển mạch gói mà một Packet đi qua từ End System gửi đến End System nhận được gọi là tuyến đường (route) hoặc đường dẫn (path) qua mạng. Cisco dự đoán lưu lượng IP toàn cầu hàng năm sẽ đạt gần 5 zettabytes (10²¹ bytes) vào năm 2022 \[Cisco VNI 2020\].

Các mạng chuyển mạch gói (vốn vận chuyển các Packets) theo nhiều cách tương tự như mạng lưới giao thông gồm đường cao tốc, đường bộ và các giao lộ (vốn vận chuyển các phương tiện xe cộ). Hãy lấy ví dụ về một nhà máy cần vận chuyển một lượng lớn hàng hóa đến một kho hàng đích cách xa hàng nghìn km. Tại nhà máy, hàng hóa được chia nhỏ và bốc lên một đội xe tải. Mỗi chiếc xe tải sau đó di chuyển độc lập qua mạng lưới đường cao tốc, đường bộ và giao lộ để đến nhà kho đích. Tại nhà kho đích, hàng hóa được dỡ xuống và tập hợp cùng phần còn lại của chuyến hàng đến từ cùng một đợt vận chuyển. Như vậy, theo nhiều khía cạnh, Packets tương tự như xe tải, các liên kết truyền thông tương tự như đường cao tốc và đường bộ, bộ chuyển mạch gói tương tự như các giao lộ, và các End Systems tương tự như các tòa nhà. Giống như một chiếc xe tải đi theo một lộ trình qua mạng lưới giao thông, một Packet cũng đi theo một lộ trình qua mạng máy tính.

Các End Systems truy cập Internet thông qua các Nhà cung cấp dịch vụ Internet (ISPs), bao gồm các ISP dân cư như công ty truyền hình cáp hoặc điện thoại địa phương; ISP doanh nghiệp; ISP trường đại học; ISP cung cấp truy cập WiFi tại sân bay, khách sạn, quán cà phê và các địa điểm công cộng khác; và các ISP dữ liệu di động, cung cấp quyền truy cập di động cho điện thoại thông minh và các thiết bị khác của chúng ta. Bản thân mỗi ISP là một mạng lưới các bộ chuyển mạch gói và các liên kết truyền thông. Các ISP cung cấp nhiều loại hình truy cập mạng cho các End Systems, bao gồm truy cập băng rộng dân cư như cable modem hoặc DSL, truy cập mạng cục bộ tốc độ cao và truy cập không dây di động. Các ISP cũng cung cấp quyền truy cập Internet cho các nhà cung cấp nội dung, kết nối trực tiếp các Servers với Internet. Bản chất của Internet là kết nối các End Systems với nhau, do đó

Các ISPs cung cấp quyền truy cập cho các End Systems cũng phải được kết nối liên thông với nhau. Do đó, các ISP tầng dưới này được kết nối liên thông thông qua các ISP tầng trên cấp quốc gia và quốc tế, và các ISP tầng trên này được kết nối trực tiếp với nhau. Một ISP tầng trên bao gồm các Routers tốc độ cao được kết nối liên thông bằng các liên kết cáp quang tốc độ cao. Mỗi mạng ISP, dù là tầng trên hay tầng dưới, đều được quản lý độc lập, chạy giao thức IP (xem bên dưới) và tuân thủ các quy ước đặt tên và địa chỉ nhất định. Chúng ta sẽ tìm hiểu kỹ hơn về các ISP và sự kết nối liên thông giữa chúng trong Mục 1.3.

Các End Systems, bộ chuyển mạch gói và các thành phần khác của Internet chạy các giao thức để điều khiển việc gửi và nhận thông tin bên trong Internet. Giao thức điều khiển truyền vận (Transmission Control Protocol - TCP) và Giao thức Internet (Internet Protocol - IP) là hai trong số các giao thức quan trọng nhất trên Internet. Giao thức IP quy định định dạng của các Packets được gửi và nhận giữa các Routers và End Systems. Các giao thức chính của Internet được gọi chung là TCP/IP. Chúng ta sẽ bắt đầu tìm hiểu về các giao thức trong chương giới thiệu này. Nhưng đó mới chỉ là khởi đầu --- phần lớn cuốn sách này bàn về các giao thức mạng!

Với tầm quan trọng của các giao thức đối với Internet, điều cốt yếu là mọi người phải thống nhất về chức năng của từng giao thức để có thể tạo ra các hệ thống và sản phẩm có khả năng tương tác với nhau. Đây là nơi các tiêu chuẩn phát huy vai trò. Các tiêu chuẩn Internet được phát triển bởi Lực lượng Đặc nhiệm Kỹ thuật Internet (Internet Engineering Task Force - IETF) \[IETF 2020\]. Các tài liệu tiêu chuẩn của IETF được gọi là Yêu cầu Nhận xét (Requests for Comments - RFCs). RFC ban đầu chỉ là những yêu cầu nhận xét chung (vì thế mới có tên gọi này) nhằm giải quyết các bài toán thiết kế mạng và giao thức mà tiền thân của Internet gặp phải \[Allman 2011\]. Các RFC thường mang tính kỹ thuật cao và rất chi tiết. Chúng định nghĩa các giao thức như TCP, IP, HTTP (cho Web) và SMTP (cho e-mail). Hiện tại có gần 9000 RFC. Các tổ chức khác cũng chỉ định các tiêu chuẩn cho các thành phần mạng, đặc biệt là các liên kết mạng. Ví dụ: Ủy ban Tiêu chuẩn LAN IEEE 802 \[IEEE 802 2020\] chỉ định các tiêu chuẩn Ethernet và mạng không dây WiFi.

**1.1.2 Mô tả dưới góc độ dịch vụ (A Services Description)**

Cuộc thảo luận của chúng ta ở trên đã xác định nhiều mảnh ghép cấu thành Internet. Nhưng chúng ta cũng có thể mô tả Internet từ một góc độ hoàn toàn khác --- cụ thể là một cơ sở hạ tầng cung cấp dịch vụ cho các ứng dụng. Ngoài các ứng dụng truyền thống như e-mail và lướt Web, các ứng dụng Internet còn bao gồm các ứng dụng trên điện thoại thông minh và máy tính bảng, bao gồm nhắn tin qua Internet, bản đồ với thông tin giao thông đường bộ thời gian thực, truyền phát nhạc (streaming), truyền phát phim và truyền hình, mạng xã hội trực tuyến, hội nghị truyền hình, trò chơi nhiều người và hệ thống gợi ý dựa trên vị trí. Các ứng dụng này được gọi là các ứng dụng phân tán (distributed applications), vì chúng liên quan đến nhiều End Systems trao đổi dữ liệu với nhau. Điều quan trọng là các ứng dụng Internet chạy trên các End Systems --- chúng không chạy trong các bộ chuyển mạch gói (packet switches) ở lõi mạng. Mặc dù các bộ chuyển mạch gói tạo điều kiện thuận lợi cho việc trao đổi dữ liệu giữa các End Systems, nhưng chúng không quan tâm đến ứng dụng là nguồn phát hay điểm nhận dữ liệu.

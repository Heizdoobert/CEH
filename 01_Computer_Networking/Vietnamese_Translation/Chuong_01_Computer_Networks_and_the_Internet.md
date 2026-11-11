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

Hãy cùng khám phá thêm một chút về ý nghĩa của cơ sở hạ tầng cung cấp dịch vụ cho các ứng dụng. Để đạt được mục tiêu này, giả sử bạn có một ý tưởng mới thú vị về một ứng dụng Internet phân tán, một ý tưởng có thể mang lại lợi ích to lớn cho nhân loại hoặc một ý tưởng có thể đơn giản giúp bạn trở nên giàu có và nổi tiếng. Bạn có thể biến ý tưởng này thành một ứng dụng Internet thực tế bằng cách nào? Vì các ứng dụng chạy trên hệ thống cuối nên bạn sẽ cần phải viết các chương trình chạy trên hệ thống cuối. Ví dụ: bạn có thể viết chương trình của mình bằng Java, C hoặc Python. Bây giờ, vì bạn đang phát triển một ứng dụng Internet phân tán nên các chương trình chạy trên các hệ thống đầu cuối khác nhau sẽ cần gửi dữ liệu cho nhau. Và ở đây chúng ta đi đến một vấn đề trọng tâm---một vấn đề dẫn đến một cách khác để mô tả Internet như một nền tảng cho các ứng dụng. Làm thế nào một chương trình chạy trên một hệ thống đầu cuối hướng dẫn Internet phân phối dữ liệu đến một chương trình khác chạy trên hệ thống đầu cuối khác?

Các hệ thống đầu cuối được kết nối với Internet cung cấp một giao diện ổ cắm chỉ định cách một chương trình chạy trên một hệ thống đầu cuối yêu cầu cơ sở hạ tầng Internet phân phối dữ liệu đến một chương trình đích cụ thể đang chạy trên một hệ thống đầu cuối khác. Giao diện ổ cắm Internet này là một bộ quy tắc mà chương trình gửi phải tuân theo để Internet có thể phân phối dữ liệu đến chương trình đích. Chúng ta sẽ thảo luận chi tiết về giao diện ổ cắm Internet trong Chương 2. Bây giờ, hãy rút ra một sự tương tự đơn giản, một sự tương tự mà chúng ta sẽ thường xuyên sử dụng trong cuốn sách này. Giả sử Alice muốn gửi thư cho Bob bằng dịch vụ bưu chính. Tất nhiên, Alice không thể chỉ viết bức thư (dữ liệu) và thả bức thư ra ngoài cửa sổ. Thay vào đó, dịch vụ bưu chính yêu cầu Alice bỏ bức thư vào một phong bì; viết tên đầy đủ, địa chỉ và mã zip của Bob vào giữa phong bì; niêm phong phong bì; dán tem vào góc trên bên phải của phong bì; và cuối cùng, thả phong bì vào hộp thư dịch vụ bưu chính chính thức. Do đó, dịch vụ bưu chính có "giao diện dịch vụ bưu chính" hoặc bộ quy tắc riêng mà Alice phải tuân theo để dịch vụ bưu chính chuyển thư của cô ấy cho Bob. Theo cách tương tự, Internet có một giao diện ổ cắm mà chương trình gửi dữ liệu phải tuân theo để Internet phân phối dữ liệu đến chương trình sẽ nhận dữ liệu.

Tất nhiên, dịch vụ bưu chính cung cấp nhiều hơn một dịch vụ cho khách hàng của mình. Nó cung cấp chuyển phát nhanh, xác nhận tiếp nhận, sử dụng thông thường và nhiều dịch vụ khác. Theo cách tương tự, Internet cung cấp nhiều dịch vụ cho các ứng dụng của nó. Khi bạn phát triển một ứng dụng Internet, bạn cũng phải chọn một trong các dịch vụ của Internet cho ứng dụng của mình. Chúng ta sẽ mô tả các dịch vụ của Internet trong Chương 2.

Chúng tôi vừa đưa ra hai mô tả về Internet; một về các thành phần phần cứng và phần mềm, một về cơ sở hạ tầng để cung cấp dịch vụ cho các ứng dụng phân tán. Nhưng có lẽ bạn vẫn còn bối rối không biết Internet là gì. Chuyển mạch gói và TCP/IP là gì? Bộ định tuyến là gì? Những loại liên kết truyền thông nào hiện có trên Internet? Ứng dụng phân tán là gì? Làm thế nào một bộ điều nhiệt hoặc cân cơ thể có thể được gắn vào Internet? Nếu bây giờ bạn cảm thấy hơi choáng ngợp trước tất cả những điều này, đừng lo lắng---mục đích của cuốn sách này là giới thiệu cho bạn những điều cơ bản và then chốt của Internet cũng như các nguyên tắc chi phối cách thức và

tại sao nó hoạt động. Chúng tôi sẽ giải thích những thuật ngữ và câu hỏi quan trọng này trong các phần và chương sau.

**1.1.3 Giao thức là gì?**

Bây giờ chúng ta đã hiểu được một chút về Internet là gì, hãy xem xét một từ thông dụng quan trọng khác trong mạng máy tính: giao thức. Giao thức là gì? Một giao thức làm gì?

Một sự tương tự của con người

Có lẽ dễ hiểu nhất khái niệm giao thức mạng máy tính bằng cách trước tiên xem xét một số điểm tương tự của con người, vì con người chúng ta luôn thực hiện các giao thức. Hãy cân nhắc xem bạn sẽ làm gì khi muốn hỏi ai đó về thời gian trong ngày. Một trao đổi điển hình được thể hiện trong Hình 1.2. Giao thức của con người (hoặc cách cư xử tốt, tại

*Hình 1.2 ♦ Giao thức của con người và giao thức mạng máy tính*

NHẬN http://www.pearsonhighered.com/

cs-tài nguyên/

TCP yêu cầu kết nối

Thời gian Thời gian

TCP trả lời kết nối

\<file\>

CHÀO

Có thời gian không?

Thời gian Thời gian

CHÀO

2:00

ít nhất) ra lệnh rằng trước tiên một người phải đưa ra lời chào ("Xin chào" đầu tiên trong Hình 1.2) để bắt đầu giao tiếp với người khác. Phản hồi điển hình cho "Xin chào" là một tin nhắn "Xin chào" được trả về. Một cách ngầm định, người ta sẽ nhận câu trả lời "Xin chào" thân mật như một dấu hiệu cho thấy người ta có thể tiếp tục và hỏi thời gian trong ngày. Một phản hồi khác với câu "Xin chào" ban đầu (chẳng hạn như "Đừng làm phiền tôi!" hoặc "Tôi không nói được tiếng Anh" hoặc một số câu trả lời không in được) có thể cho thấy sự không sẵn lòng hoặc không có khả năng giao tiếp. Trong trường hợp này, giao thức của con người sẽ không hỏi thời gian trong ngày. Đôi khi một người không nhận được câu trả lời nào cho một câu hỏi, trong trường hợp đó người ta thường từ bỏ việc hỏi người đó về thời gian. Lưu ý rằng trong giao thức con người của chúng ta, có những tin nhắn cụ thể mà chúng ta gửi và những hành động cụ thể mà chúng ta thực hiện để phản hồi những tin nhắn trả lời đã nhận được hoặc các sự kiện khác (chẳng hạn như không trả lời trong một khoảng thời gian nhất định). Rõ ràng, các tin nhắn được truyền và nhận cũng như các hành động được thực hiện khi các tin nhắn này được gửi hoặc nhận hoặc các sự kiện khác xảy ra, đóng vai trò trung tâm trong giao thức của con người. Nếu mọi người thực hiện các giao thức khác nhau (ví dụ: nếu một người có cách cư xử còn người kia thì không, hoặc nếu một người hiểu khái niệm về thời gian còn người kia thì không), thì các giao thức đó sẽ không tương tác với nhau và không thể thực hiện được công việc hữu ích nào. Điều này cũng đúng trong mạng---cần có hai (hoặc nhiều) thực thể giao tiếp chạy cùng một giao thức để hoàn thành một nhiệm vụ.

Hãy xem xét sự tương tự thứ hai của con người. Giả sử bạn đang học trong một lớp đại học (ví dụ như lớp mạng máy tính!). Giáo viên đang nói liên tục về các nghi thức và bạn đang bối rối. Giáo viên dừng lại hỏi: "Có câu hỏi nào không?" (một tin nhắn được truyền đến và nhận bởi tất cả học sinh chưa ngủ). Bạn giơ tay (truyền một thông điệp ngầm tới giáo viên). Giáo viên của bạn thừa nhận bạn bằng một nụ cười và nói \"Có . . . \" (một thông điệp được truyền đi khuyến khích bạn đặt câu hỏi - giáo viên thích được đặt câu hỏi) và sau đó bạn đặt câu hỏi (nghĩa là truyền tải thông điệp của bạn đến giáo viên của bạn). Giáo viên của bạn nghe câu hỏi của bạn (nhận tin nhắn câu hỏi của bạn) và câu trả lời (truyền câu trả lời cho bạn). Một lần nữa, chúng ta thấy rằng việc truyền và nhận tin nhắn cũng như một tập hợp các hành động thông thường được thực hiện khi những tin nhắn này được gửi và nhận là trọng tâm của giao thức hỏi đáp này.

Giao thức mạng

Giao thức mạng tương tự như giao thức của con người, ngoại trừ việc các thực thể trao đổi tin nhắn và thực hiện hành động là các thành phần phần cứng hoặc phần mềm của một số thiết bị (ví dụ: máy tính, điện thoại thông minh, máy tính bảng, bộ định tuyến hoặc thiết bị có khả năng kết nối mạng khác). Tất cả hoạt động trên Internet liên quan đến hai hoặc nhiều thực thể giao tiếp từ xa đều được quản lý bởi một giao thức. Ví dụ: các giao thức được triển khai bằng phần cứng trong hai máy tính được kết nối vật lý sẽ kiểm soát luồng bit trên "dây" giữa hai card giao diện mạng; các giao thức kiểm soát tắc nghẽn trong hệ thống cuối kiểm soát tốc độ truyền gói tin giữa người gửi và người nhận; các giao thức trong bộ định tuyến xác định đường dẫn của gói từ nguồn đến đích. Các giao thức đang chạy

khắp mọi nơi trên Internet, và do đó phần lớn cuốn sách này nói về các giao thức mạng máy tính.

Như một ví dụ về giao thức mạng máy tính mà bạn có thể quen thuộc, hãy xem xét điều gì xảy ra khi bạn thực hiện một yêu cầu tới máy chủ Web, nghĩa là khi bạn nhập URL của một trang Web vào trình duyệt Web của mình. Kịch bản được minh họa ở nửa bên phải của Hình 1.2. Đầu tiên, máy tính của bạn sẽ gửi tin nhắn yêu cầu kết nối đến máy chủ Web và chờ phản hồi. Máy chủ Web cuối cùng sẽ nhận được thông báo yêu cầu kết nối của bạn và trả lại thông báo trả lời kết nối. Biết rằng bây giờ bạn có thể yêu cầu tài liệu Web, máy tính của bạn sẽ gửi tên của trang Web mà nó muốn tìm nạp từ máy chủ Web đó trong thông báo GET. Cuối cùng, máy chủ Web trả về trang Web (file) về máy tính của bạn.

Với các ví dụ về con người và mạng ở trên, việc trao đổi tin nhắn và các hành động được thực hiện khi những tin nhắn này được gửi và nhận là các yếu tố xác định chính của một giao thức:

Giao thức xác định định dạng và thứ tự của các tin nhắn được trao đổi giữa hai hoặc nhiều thực thể giao tiếp, cũng như các hành động được thực hiện khi truyền và/hoặc nhận tin nhắn hoặc sự kiện khác.

Internet và các mạng máy tính nói chung sử dụng rộng rãi các giao thức. Các giao thức khác nhau được sử dụng để thực hiện các nhiệm vụ giao tiếp khác nhau. Khi đọc qua cuốn sách này, bạn sẽ biết rằng một số giao thức rất đơn giản và dễ hiểu, trong khi một số khác lại phức tạp và mang tính trí tuệ sâu sắc. Nắm vững lĩnh vực mạng máy tính tương đương với việc hiểu cái gì, tại sao và như thế nào của các giao thức mạng.

**1.2 Biên mạng**

Trong phần trước, chúng tôi đã trình bày tổng quan cấp cao về Internet và các giao thức mạng. Bây giờ chúng ta sẽ đi sâu hơn một chút vào các thành phần của Internet. Chúng ta bắt đầu trong phần này ở rìa mạng và xem xét các thành phần mà chúng ta quen thuộc nhất---cụ thể là máy tính, điện thoại thông minh và các thiết bị khác mà chúng ta sử dụng hàng ngày. Trong phần tiếp theo, chúng ta sẽ chuyển từ biên mạng đến lõi mạng và kiểm tra việc chuyển mạch và định tuyến trong mạng máy tính.

Hãy nhớ lại phần trước rằng trong thuật ngữ mạng máy tính, máy tính và các thiết bị khác được kết nối với Internet thường được gọi là hệ thống đầu cuối. Chúng được gọi là hệ thống đầu cuối vì chúng nằm ở rìa Internet, như trong Hình 1.3. Các hệ thống đầu cuối của Internet bao gồm máy tính để bàn

*Hình 1.3 ♦ Tương tác giữa hệ thống cuối*

Content Provider Network (Mạng nhà cung cấp nội dung)

Quốc gia hoặc

Global ISP (ISP Toàn cầu)

Datacenter Network (Mạng trung tâm dữ liệu)

Datacenter Network (Mạng trung tâm dữ liệu)

Mobile Network (Mạng di động)

Enterprise Network (Mạng doanh nghiệp)

Home Network (Mạng gia đình)

Local or Regional ISP (ISP Địa phương hoặc Khu vực)

(ví dụ: máy tính để bàn, máy Mac và hộp Linux), máy chủ (ví dụ: máy chủ Web và e-mail) và thiết bị di động (ví dụ: máy tính xách tay, điện thoại thông minh và máy tính bảng). Hơn nữa, ngày càng có nhiều "thứ" phi truyền thống được gắn vào Internet dưới dạng hệ thống cuối (xem tính năng Lịch sử trường hợp).

Hệ thống cuối còn được gọi là máy chủ vì chúng lưu trữ (nghĩa là chạy) các chương trình ứng dụng như chương trình trình duyệt Web, chương trình máy chủ Web, e-mail.

chương trình máy khách hoặc chương trình máy chủ e-mail. Trong suốt cuốn sách này, chúng tôi sẽ sử dụng các thuật ngữ máy chủ và hệ thống đầu cuối thay thế cho nhau; nghĩa là máy chủ = hệ thống cuối. Hosts đôi khi còn được chia thành hai loại: máy khách và máy chủ. Một cách không chính thức, khách hàng có xu hướng là máy tính để bàn, máy tính xách tay, điện thoại thông minh, v.v., trong khi máy chủ có xu hướng là những cỗ máy mạnh mẽ hơn để lưu trữ và phân phối các trang Web, truyền phát video, chuyển tiếp e-mail, v.v. Ngày nay, hầu hết các máy chủ mà từ đó chúng ta nhận được kết quả tìm kiếm, e-mail, trang Web, video và nội dung ứng dụng di động đều nằm trong các trung tâm dữ liệu lớn. Ví dụ: tính đến năm 2020, Google có 19 trung tâm dữ liệu trên bốn châu lục, tổng cộng có vài triệu máy chủ. Hình 1.3 bao gồm hai trung tâm dữ liệu như vậy và thanh bên Lịch sử trường hợp mô tả các trung tâm dữ liệu chi tiết hơn.

TRUNG TÂM DỮ LIỆU VÀ ĐIỆN TOÁN ĐÁM MÂY

Các công ty Internet như Google, Microsoft, Amazon và Alibaba đã xây dựng các trung tâm dữ liệu khổng lồ, mỗi trung tâm chứa hàng chục đến hàng trăm nghìn máy chủ. Các trung tâm dữ liệu này không chỉ được kết nối với Internet, như trong Hình 1.1, mà còn bao gồm bên trong các mạng máy tính phức tạp kết nối các máy chủ của trung tâm dữ liệu. Các trung tâm dữ liệu là động cơ đằng sau các ứng dụng Internet mà chúng ta sử dụng hàng ngày.

Nói rộng ra, các trung tâm dữ liệu phục vụ ba mục đích mà chúng tôi mô tả ở đây trong bối cảnh cụ thể của Amazon. Đầu tiên, họ phục vụ các trang thương mại điện tử của Amazon tới người dùng, ví dụ như các trang mô tả sản phẩm và thông tin mua hàng. Thứ hai, chúng đóng vai trò là cơ sở hạ tầng điện toán song song ồ ạt cho các tác vụ xử lý dữ liệu dành riêng cho Amazon. Thứ ba, họ cung cấp điện toán đám mây cho các công ty khác. Quả thực, ngày nay xu hướng chính trong điện toán là các công ty sử dụng nhà cung cấp đám mây như Amazon để xử lý cơ bản tất cả các nhu cầu CNTT của họ. Ví dụ: Airbnb và nhiều công ty dựa trên Internet khác không sở hữu và quản lý trung tâm dữ liệu của riêng họ mà thay vào đó vận hành toàn bộ dịch vụ dựa trên Web của họ trên đám mây Amazon, được gọi là Amazon Web Services (AWS).

Những con ong thợ trong trung tâm dữ liệu là vật chủ. Chúng phục vụ nội dung (ví dụ: các trang Web và video), lưu trữ e-mail và tài liệu, đồng thời thực hiện chung các phép tính phân tán quy mô lớn. Máy chủ trong trung tâm dữ liệu, được gọi là lưỡi dao và trông giống hộp bánh pizza, thường là máy chủ hàng hóa bao gồm CPU, bộ nhớ và bộ lưu trữ trên ổ đĩa. Các máy chủ được xếp thành các giá, mỗi giá thường có từ 20 đến 40 cánh. Sau đó, các giá đỡ được kết nối với nhau bằng các thiết kế mạng trung tâm dữ liệu phức tạp và đang phát triển. Mạng trung tâm dữ liệu sẽ được thảo luận chi tiết hơn trong Chương 6.

LỊCH SỬ TRƯỜNG HỢP

**1.2.1 Mạng truy cập**

Sau khi xem xét các ứng dụng và hệ thống đầu cuối ở "biên mạng", tiếp theo chúng ta hãy xem xét mạng truy cập---mạng kết nối vật lý hệ thống đầu cuối với bộ định tuyến đầu tiên (còn được gọi là "bộ định tuyến biên") trên đường dẫn từ hệ thống đầu cuối đến bất kỳ hệ thống đầu cuối ở xa nào khác. Hình 1.4 thể hiện một số kiểu truy cập

*Hình 1.4 ♦ Mạng truy cập*

Content Provider Network (Mạng nhà cung cấp nội dung)

Quốc gia hoặc

Global ISP (ISP Toàn cầu)

Datacenter Network (Mạng trung tâm dữ liệu)

Datacenter Network (Mạng trung tâm dữ liệu)

Mobile Network (Mạng di động)

Enterprise Network (Mạng doanh nghiệp)

Home Network (Mạng gia đình)

Local or Regional ISP (ISP Địa phương hoặc Khu vực)

các mạng có đường kẻ dày, bóng mờ và các cài đặt (không dây tại nhà, doanh nghiệp và di động diện rộng) mà chúng được sử dụng.

Truy cập tại nhà: DSL, Cáp, FTTH và 5G Không dây cố định

Tính đến năm 2020, hơn 80% hộ gia đình ở Châu Âu và Hoa Kỳ có quyền truy cập Internet \[Statista 2019\]. Với việc sử dụng rộng rãi mạng truy cập gia đình, hãy bắt đầu tổng quan về mạng truy cập bằng cách xem xét cách các gia đình kết nối với Internet.

Ngày nay, hai loại truy cập băng rộng dân cư phổ biến nhất là đường dây thuê bao kỹ thuật số (DSL) và cáp. Một nơi cư trú thường có được quyền truy cập Internet DSL từ cùng một công ty điện thoại địa phương (telco) cung cấp quyền truy cập điện thoại địa phương có dây. Vì vậy, khi sử dụng DSL, công ty viễn thông của khách hàng cũng chính là ISP của khách hàng. Như được hiển thị trong Hình 1.5, modem DSL của mỗi khách hàng sử dụng dữ liệu trao đổi đường dây điện thoại hiện có với bộ ghép kênh truy cập đường dây thuê bao kỹ thuật số (DSLAM) đặt tại văn phòng trung tâm địa phương (CO) của công ty viễn thông. Modem DSL trong nhà lấy dữ liệu số và chuyển nó sang âm thanh tần số cao để truyền qua dây điện thoại tới CO; tín hiệu tương tự từ nhiều ngôi nhà như vậy được dịch trở lại định dạng kỹ thuật số tại DSLAM.

Đường dây điện thoại dân dụng mang đồng thời cả dữ liệu và tín hiệu điện thoại truyền thống, được mã hóa ở các tần số khác nhau:

• Kênh tải xuống tốc độ cao, trong băng tần 50 kHz đến 1 MHz • Kênh tải lên tốc độ trung bình, trong băng tần 4 kHz đến 50 kHz • Kênh điện thoại hai chiều thông thường, trong băng tần 0 đến 4 kHz

Cách tiếp cận này làm cho liên kết DSL đơn xuất hiện như thể có ba liên kết riêng biệt, do đó một cuộc gọi điện thoại và kết nối Internet có thể chia sẻ liên kết DSL tại

*Hình 1.5 ♦ Truy cập Internet DSL*

Máy tính gia đình

Điện thoại nhà

modem DSL

internet

Điện thoại

mạng

Bộ chia

Đường dây điện thoại hiện có: Điện thoại 0-4KHz; Dữ liệu ngược dòng 4-50KHz; Dữ liệu xuôi dòng 50KHz-- 1 MHz

Văn phòng trung tâm

DSLAM

cùng một lúc. (Chúng tôi sẽ mô tả kỹ thuật ghép kênh phân chia tần số này trong Phần 1.3.1.) Về phía khách hàng, bộ chia tách dữ liệu và tín hiệu điện thoại đến nhà và chuyển tiếp tín hiệu dữ liệu đến modem DSL. Về phía viễn thông, trong CO, DSLAM tách dữ liệu và tín hiệu điện thoại rồi gửi dữ liệu vào Internet. Hàng trăm, thậm chí hàng nghìn hộ gia đình kết nối vào một DSLAM.

Các tiêu chuẩn DSL xác định nhiều tốc độ truyền, bao gồm tốc độ truyền tải xuôi dòng là 24 Mbs và 52 Mbs cũng như tốc độ truyền tải ngược dòng là 3,5 Mbps và 16 Mbps; tiêu chuẩn mới nhất cung cấp tốc độ tổng hợp ngược dòng và hạ lưu là 1 Gbps \[ITU 2014\]. Bởi vì tốc độ xuôi dòng và ngược dòng khác nhau nên khả năng truy cập được cho là không đối xứng. Tốc độ truyền tải xuôi và ngược dòng thực tế đạt được có thể thấp hơn tốc độ đã nêu ở trên, vì nhà cung cấp DSL có thể cố tình giới hạn cước phí dân cư khi cung cấp dịch vụ theo cấp độ (các mức giá khác nhau, có sẵn ở các mức giá khác nhau). Tốc độ tối đa cũng bị giới hạn bởi khoảng cách giữa nhà và CO, thước đo của đường dây xoắn đôi và mức độ nhiễu điện. Các kỹ sư đã thiết kế rõ ràng DSL cho khoảng cách ngắn giữa nhà và CO; nói chung, nếu nơi cư trú không nằm trong phạm vi 5 đến 10 dặm từ CO, nơi cư trú phải sử dụng hình thức truy cập Internet thay thế.

Trong khi DSL tận dụng cơ sở hạ tầng điện thoại địa phương hiện có của công ty viễn thông thì việc truy cập Internet qua cáp lại tận dụng cơ sở hạ tầng truyền hình cáp hiện có của công ty truyền hình cáp. Một nơi cư trú được truy cập Internet cáp từ cùng một công ty cung cấp truyền hình cáp. Như minh họa trong hình 1.6, cáp quang

*Hình 1.6 ♦ Mạng truy nhập cáp quang-đồng trục lai*

Cáp quang

Cáp đồng trục

Hàng trăm ngôi nhà

Đầu cáp

Hàng trăm ngôi nhà

Nút sợi

Nút sợi

internet

CMTS

kết nối đầu cáp với các nút giao cấp khu dân cư, từ đó cáp đồng trục truyền thống được sử dụng để tiếp cận các ngôi nhà và căn hộ riêng lẻ. Mỗi ngã ba khu dân cư thường có từ 500 đến 5.000 ngôi nhà. Bởi vì cả cáp quang và cáp đồng trục đều được sử dụng trong hệ thống này nên nó thường được gọi là cáp đồng trục lai (HFC).

Truy cập internet bằng cáp cần có modem đặc biệt, được gọi là modem cáp. Giống như modem DSL, modem cáp thường là một thiết bị bên ngoài và kết nối với PC ở nhà thông qua cổng Ethernet. (Chúng ta sẽ thảo luận chi tiết về Ethernet trong Chương 6.) Ở đầu cáp, hệ thống đầu cuối modem cáp (CMTS) phục vụ chức năng tương tự như DSLAM của mạng DSL--- chuyển tín hiệu tương tự được gửi từ modem cáp ở nhiều hộ gia đình phía dưới trở lại định dạng kỹ thuật số. Modem cáp chia mạng HFC thành hai kênh, kênh xuôi dòng và kênh ngược dòng. Giống như DSL, quyền truy cập thường không đối xứng, kênh hạ lưu thường được phân bổ tốc độ truyền cao hơn kênh ngược dòng. Các tiêu chuẩn DOCSIS 2.0 và 3.0 xác định tốc độ bit tải xuống lần lượt là 40 Mbps và 1,2 Gbps và tốc độ tải lên tương ứng là 30 Mbps và 100 Mbps. Như trong trường hợp mạng DSL, tốc độ tối đa có thể đạt được có thể không đạt được do tốc độ dữ liệu theo hợp đồng thấp hơn hoặc do phương tiện truyền thông bị suy giảm.

Một đặc điểm quan trọng của truy cập Internet cáp là nó là phương tiện phát sóng được chia sẻ. Cụ thể, mỗi gói được gửi bởi đầu cuối sẽ di chuyển xuôi dòng trên mọi liên kết đến mọi nhà và mọi gói được gửi bởi một nhà sẽ di chuyển trên kênh ngược dòng tới đầu cuối. Vì lý do này, nếu nhiều người dùng đồng thời tải xuống một tệp video trên kênh hạ lưu, tốc độ thực tế mà mỗi người dùng nhận được tệp video của họ sẽ thấp hơn đáng kể so với tốc độ hạ lưu cáp tổng hợp. Mặt khác, nếu chỉ có một vài người dùng đang hoạt động và tất cả họ đều lướt Web thì mỗi người dùng thực sự có thể nhận được các trang Web ở tốc độ truyền tải cáp đầy đủ, bởi vì người dùng sẽ hiếm khi yêu cầu một trang Web vào cùng một thời điểm. Vì kênh ngược dòng cũng được chia sẻ nên cần có giao thức đa truy cập phân tán để điều phối việc truyền và tránh xung đột. (Chúng ta sẽ thảo luận chi tiết về vấn đề va chạm này ở Chương 6.)

Mặc dù mạng DSL và cáp hiện đại diện cho phần lớn truy cập băng thông rộng dân dụng ở Hoa Kỳ, một công nghệ sắp ra mắt cung cấp tốc độ cao hơn nữa là cáp quang đến nhà (FTTH) \[Băng thông rộng cáp quang 2020\]. Đúng như tên gọi, khái niệm FTTH rất đơn giản---cung cấp đường dẫn cáp quang từ CO trực tiếp đến nhà. FTTH có khả năng cung cấp tốc độ truy cập Internet ở phạm vi gigabit trên giây.

Có một số công nghệ cạnh tranh để phân phối quang học từ CO đến các hộ gia đình. Mạng phân phối quang đơn giản nhất được gọi là cáp quang trực tiếp, với một cáp quang để lại CO cho mỗi nhà. Thông thường hơn, mỗi sợi cáp rời khỏi văn phòng trung tâm thực tế được nhiều gia đình chia sẻ; Phải đến khi sợi quang đến gần các gia đình, nó mới được chia thành các sợi dành riêng cho từng khách hàng. Có hai kiến ​​trúc mạng phân phối quang cạnh tranh nhau thực hiện

sự phân chia này: mạng quang chủ động (AON) và mạng quang thụ động (PON). AON về cơ bản là Ethernet chuyển mạch, được thảo luận trong Chương 6.

Ở đây, chúng tôi thảo luận ngắn gọn về PON, được sử dụng trong dịch vụ FiOS của Verizon. Hình 1.7 cho thấy FTTH sử dụng kiến ​​trúc phân phối PON. Mỗi ngôi nhà đều có một thiết bị đầu cuối mạng quang (ONT), được kết nối bằng cáp quang chuyên dụng với bộ chia lân cận. Bộ chia kết hợp một số ngôi nhà (thường dưới 100) vào một sợi quang chung, duy nhất, kết nối với thiết bị đầu cuối đường truyền quang (OLT) trong CO của công ty viễn thông. OLT, cung cấp chuyển đổi giữa tín hiệu quang và điện, kết nối với Internet thông qua bộ định tuyến viễn thông. Ở nhà, người dùng kết nối bộ định tuyến gia đình (thường là bộ định tuyến không dây) với ONT và truy cập Internet thông qua bộ định tuyến gia đình này. Trong kiến ​​trúc PON, tất cả các gói được gửi từ OLT đến bộ chia đều được sao chép tại bộ chia (tương tự như đầu cáp).

Ngoài DSL, Cable và FTTH, mạng không dây cố định 5G đang bắt đầu được triển khai. Mạng không dây cố định 5G không chỉ hứa hẹn khả năng truy cập dân cư tốc độ cao mà còn thực hiện được điều đó mà không cần lắp đặt hệ thống cáp tốn kém và dễ bị hỏng từ CO của công ty viễn thông đến nhà. Với mạng không dây cố định 5G, sử dụng công nghệ tạo chùm tia, dữ liệu được gửi không dây từ trạm gốc của nhà cung cấp đến modem trong nhà. Bộ định tuyến không dây WiFi được kết nối với modem (có thể được gói cùng nhau), tương tự như cách bộ định tuyến không dây WiFi được kết nối với cáp hoặc modem DSL. Mạng di động 5G được đề cập trong Chương 7.

Truy cập trong Doanh nghiệp (và Gia đình): Ethernet và WiFi

Trong khuôn viên công ty và trường đại học cũng như trong môi trường gia đình ngày càng phổ biến, mạng cục bộ (LAN) được sử dụng để kết nối hệ thống đầu cuối với bộ định tuyến biên. Mặc dù có nhiều loại công nghệ mạng LAN, Ethernet cho đến nay vẫn là công nghệ truy cập phổ biến nhất trong mạng doanh nghiệp, trường đại học và mạng gia đình. Như thể hiện trong

*Hình 1.7 ♦ Truy cập Internet FTTH*

Văn phòng trung tâm Internet

Bộ chia quang ONT

ONT

ONT

OLT

Sợi quang học

Hình 1.8, Người dùng Ethernet sử dụng dây đồng xoắn đôi để kết nối với bộ chuyển mạch Ethernet, một công nghệ được thảo luận chi tiết trong Chương 6. Bộ chuyển mạch Ethernet hoặc mạng gồm các bộ chuyển mạch được kết nối với nhau như vậy sau đó sẽ được kết nối với Internet lớn hơn. Với quyền truy cập Ethernet, người dùng thường có quyền truy cập 100 Mbps đến hàng chục Gbps vào bộ chuyển mạch Ethernet, trong khi máy chủ có thể có quyền truy cập 1 Gbps 10 Gbps.

Tuy nhiên, ngày càng có nhiều người truy cập Internet không dây từ máy tính xách tay, điện thoại thông minh, máy tính bảng và những "thứ" khác. Trong cài đặt mạng LAN không dây, người dùng không dây truyền/nhận gói đến/từ điểm truy cập được kết nối với mạng của doanh nghiệp (rất có thể sử dụng Ethernet có dây), điểm truy cập này được kết nối với Internet có dây. Người dùng mạng LAN không dây thường phải ở trong phạm vi vài chục mét tính từ điểm truy cập. Truy cập mạng LAN không dây dựa trên công nghệ IEEE 802.11, thường được gọi là WiFi, hiện có ở khắp mọi nơi---trường đại học, văn phòng kinh doanh, quán cà phê, sân bay, nhà ở và thậm chí cả trên máy bay. Như đã thảo luận chi tiết trong Chương 7, 802.11 ngày nay cung cấp tốc độ truyền chia sẻ lên tới hơn 100 Mbps. Mặc dù mạng truy cập Ethernet và WiFi ban đầu được triển khai trong môi trường doanh nghiệp (công ty, trường đại học), chúng cũng là các thành phần phổ biến của mạng gia đình. Nhiều gia đình kết hợp truy cập băng thông rộng dân dụng (nghĩa là modem cáp hoặc DSL) với các công nghệ mạng LAN không dây rẻ tiền này để tạo ra các mạng gia đình mạnh mẽ. Hình 1.9 thể hiện một mạng gia đình điển hình. Mạng gia đình này bao gồm một máy tính xách tay chuyển vùng, nhiều thiết bị gia dụng được kết nối Internet cũng như một PC có dây; một trạm cơ sở (điểm truy cập không dây), giao tiếp với PC không dây và các thiết bị không dây khác trong nhà; và bộ định tuyến gia đình kết nối điểm truy cập không dây và bất kỳ thiết bị gia đình có dây nào khác với Internet. Mạng này cho phép các thành viên trong gia đình truy cập Internet băng thông rộng với một thành viên chuyển vùng từ nhà bếp ra sân sau đến phòng ngủ.

*Hình 1.8 ♦ Truy cập Internet Ethernet*

Ethernet

công tắc

Thể chế

bộ định tuyến

1 Gbps

1 Gbps

1 Gbps

Máy chủ

Gửi tới tổ chức

ISP

Truy cập không dây diện rộng: 3G và LTE 4G và 5G

Các thiết bị di động như iPhone và thiết bị Android đang được sử dụng để nhắn tin, chia sẻ ảnh trên mạng xã hội, thanh toán di động, xem phim, phát nhạc trực tuyến và hơn thế nữa khi đang di chuyển. Các thiết bị này sử dụng cùng cơ sở hạ tầng không dây được sử dụng cho điện thoại di động để gửi/nhận các gói thông qua trạm gốc do nhà cung cấp mạng di động vận hành. Không giống như WiFi, người dùng chỉ cần ở trong phạm vi vài chục km (trái ngược với vài chục mét) tính từ trạm gốc.

Các công ty viễn thông đã đầu tư rất lớn vào cái gọi là mạng không dây thế hệ thứ tư (4G), cung cấp tốc độ tải xuống trong thế giới thực lên tới 60 Mbps. Nhưng ngay cả các công nghệ truy cập diện rộng tốc độ cao hơn---mạng không dây diện rộng thế hệ thứ năm (5G)---đã được triển khai. Chúng tôi sẽ đề cập đến các nguyên tắc cơ bản của mạng không dây và tính di động, cũng như các công nghệ WiFi, 4G và 5G (và hơn thế nữa!) trong Chương 7.

**1.2.2 Phương tiện vật lý**

Trong tiểu mục trước, chúng tôi đã đưa ra cái nhìn tổng quan về một số công nghệ truy cập mạng quan trọng nhất trên Internet. Khi mô tả những công nghệ này, chúng tôi cũng chỉ ra phương tiện vật lý được sử dụng. Ví dụ: chúng tôi đã nói rằng HFC sử dụng kết hợp cáp quang và cáp đồng trục. Chúng tôi đã nói rằng DSL và Ethernet sử dụng dây đồng. Và chúng tôi đã nói rằng mạng truy cập di động sử dụng phổ tần vô tuyến. Trong tiểu mục này, chúng tôi cung cấp một cái nhìn tổng quan ngắn gọn về những phương tiện này và các phương tiện truyền dẫn khác thường được sử dụng trên Internet.

Để xác định ý nghĩa của phương tiện vật chất, chúng ta hãy suy ngẫm về vòng đời ngắn ngủi của một bit. Hãy xem xét việc một bit di chuyển từ hệ thống đầu cuối này, thông qua một loạt các liên kết và bộ định tuyến, đến hệ thống đầu cuối khác. Điều đáng thương này đã bị đá đi khắp nơi và truyền đi rất nhiều lần! Hệ thống đầu cuối nguồn đầu tiên truyền

*Hình 1.9 ♦ Một mạng gia đình điển hình*

Internet đầu cuối cáp

Home Network (Mạng gia đình)

bit, và ngay sau đó bộ định tuyến đầu tiên trong chuỗi sẽ nhận được bit; sau đó bộ định tuyến đầu tiên truyền bit và ngay sau đó bộ định tuyến thứ hai nhận được bit; và vân vân. Do đó, bit của chúng ta, khi di chuyển từ nguồn đến đích, sẽ đi qua một loạt các cặp máy phát-máy thu. Đối với mỗi cặp máy phát-máy thu, bit được gửi bằng cách truyền sóng điện từ hoặc xung quang qua môi trường vật lý. Môi trường vật lý có thể có nhiều hình dạng và dạng thức và không nhất thiết phải cùng loại đối với mỗi cặp máy phát-máy thu dọc theo đường dẫn. Ví dụ về phương tiện vật lý bao gồm dây đồng xoắn đôi, cáp đồng trục, cáp quang đa mode, phổ vô tuyến mặt đất và phổ vô tuyến vệ tinh. Phương tiện vật lý được chia thành hai loại: phương tiện có hướng dẫn và phương tiện không có hướng dẫn. Với phương tiện truyền thông được dẫn hướng, sóng được dẫn dọc theo một môi trường rắn, chẳng hạn như cáp quang, dây đồng xoắn đôi hoặc cáp đồng trục. Với phương tiện truyền thông không được điều khiển, sóng lan truyền trong khí quyển và ngoài không gian, chẳng hạn như trong mạng LAN không dây hoặc kênh vệ tinh kỹ thuật số.

Nhưng trước khi đi vào đặc điểm của các loại phương tiện truyền thông khác nhau, chúng ta hãy nói đôi lời về giá thành của chúng. Chi phí thực tế của liên kết vật lý (dây đồng, cáp quang, v.v.) thường tương đối nhỏ so với các chi phí mạng khác. Đặc biệt, chi phí lao động liên quan đến việc lắp đặt liên kết vật lý có thể cao hơn nhiều so với chi phí vật liệu. Vì lý do này, nhiều nhà xây dựng lắp đặt cáp xoắn đôi, cáp quang và cáp đồng trục ở mọi phòng trong tòa nhà. Ngay cả khi ban đầu chỉ sử dụng một phương tiện, rất có thể phương tiện khác có thể được sử dụng trong tương lai gần và do đó tiết kiệm được tiền do không phải đặt thêm dây trong tương lai.

Dây đồng xoắn đôi

Phương tiện truyền dẫn dẫn hướng ít tốn kém nhất và được sử dụng phổ biến nhất là dây đồng xoắn đôi. Trong hơn một trăm năm, nó đã được sử dụng bởi các mạng điện thoại. Trên thực tế, hơn 99% kết nối có dây từ điện thoại cầm tay đến tổng đài điện thoại địa phương đều sử dụng dây đồng xoắn đôi. Hầu hết chúng ta đều đã từng nhìn thấy những cặp dây xoắn trong nhà mình (hoặc của cha mẹ, ông bà!) và môi trường làm việc. Cặp xoắn gồm hai dây đồng cách điện, mỗi dây dày khoảng 1 mm, được sắp xếp theo hình xoắn ốc đều. Các dây được xoắn lại với nhau để giảm nhiễu điện từ các cặp dây tương tự ở gần nhau. Thông thường, một số cặp được bó lại với nhau thành một cáp bằng cách bọc các cặp này trong một tấm chắn bảo vệ. Một cặp dây tạo thành một liên kết truyền thông duy nhất. Cặp xoắn không được che chắn (UTP) thường được sử dụng cho các mạng máy tính trong tòa nhà, nghĩa là cho mạng LAN. Tốc độ dữ liệu cho mạng LAN sử dụng cặp xoắn ngày nay nằm trong khoảng từ 10 Mbps đến 10 Gbps. Tốc độ dữ liệu có thể đạt được phụ thuộc vào độ dày của dây và khoảng cách giữa máy phát và máy thu.

Khi công nghệ cáp quang xuất hiện vào những năm 1980, nhiều người chê bai cáp xoắn đôi vì tốc độ bit tương đối thấp của nó. Một số người thậm chí còn cảm thấy

công nghệ cáp quang sẽ thay thế hoàn toàn cáp xoắn đôi. Nhưng cặp xoắn không bỏ cuộc dễ dàng như vậy. Công nghệ xoắn đôi hiện đại, chẳng hạn như cáp loại 6a, có thể đạt tốc độ dữ liệu 10 Gbps cho khoảng cách lên tới một trăm mét. Cuối cùng, cặp xoắn đã nổi lên như một giải pháp vượt trội cho mạng LAN tốc độ cao.

Như đã thảo luận trước đó, cặp xoắn cũng thường được sử dụng để truy cập Internet dân dụng. Chúng tôi nhận thấy rằng công nghệ modem quay số cho phép truy cập ở tốc độ lên tới 56 kbps qua cặp dây xoắn. Chúng tôi cũng thấy rằng công nghệ DSL (đường dây thuê bao kỹ thuật số) đã cho phép người dùng dân cư truy cập Internet với tốc độ hàng chục Mbps qua cặp xoắn (khi người dùng sống gần văn phòng trung tâm của ISP).

Cáp đồng trục

Giống như cáp xoắn đôi, cáp đồng trục gồm có hai dây dẫn bằng đồng nhưng hai dây dẫn này đồng tâm chứ không phải song song. Với cấu trúc này cùng lớp cách nhiệt và che chắn đặc biệt, cáp đồng trục có thể đạt được tốc độ truyền dữ liệu cao. Cáp đồng trục khá phổ biến trong các hệ thống truyền hình cáp. Như chúng ta đã thấy trước đó, hệ thống truyền hình cáp gần đây đã được kết hợp với modem cáp để cung cấp cho người dùng dân cư khả năng truy cập Internet với tốc độ hàng trăm Mbps. Trong truyền hình cáp và truy cập Internet qua cáp, bộ phát chuyển tín hiệu số sang một dải tần số cụ thể và tín hiệu tương tự thu được sẽ được gửi từ bộ phát đến một hoặc nhiều bộ thu. Cáp đồng trục có thể được sử dụng làm phương tiện chia sẻ có hướng dẫn. Cụ thể, một số hệ thống đầu cuối có thể được kết nối trực tiếp với cáp, mỗi hệ thống đầu cuối sẽ nhận bất cứ thứ gì được hệ thống đầu cuối kia gửi đi.

Sợi quang

Sợi quang là một môi trường mỏng, linh hoạt dẫn truyền các xung ánh sáng, với mỗi xung đại diện cho một bit. Một sợi quang duy nhất có thể hỗ trợ tốc độ bit cực lớn, lên tới hàng chục hoặc thậm chí hàng trăm gigabit mỗi giây. Chúng miễn nhiễm với nhiễu điện từ, có độ suy giảm tín hiệu rất thấp lên tới 100 km và rất khó nghe lén. Những đặc điểm này đã làm cho cáp quang trở thành phương tiện truyền dẫn dẫn đường dài được ưa chuộng, đặc biệt đối với các tuyến liên kết ở nước ngoài. Nhiều mạng điện thoại đường dài ở Hoa Kỳ và các nơi khác hiện chỉ sử dụng cáp quang. Cáp quang cũng phổ biến trong xương sống của Internet. Tuy nhiên, chi phí cao của các thiết bị quang học---chẳng hạn như máy phát, máy thu và bộ chuyển mạch---đã cản trở việc triển khai chúng để truyền tải quãng đường ngắn, chẳng hạn như trong mạng LAN hoặc vào nhà trong mạng truy cập dân cư. Tốc độ liên kết tiêu chuẩn của Nhà cung cấp quang học (OC) nằm trong khoảng từ 51,8 Mbps đến 39,8 Gbps; những thông số kỹ thuật này thường được gọi là OC-n, trong đó tốc độ liên kết bằng n × 51,8 Mbps. Các tiêu chuẩn được sử dụng ngày nay bao gồm OC-1, OC-3, OC-12, OC-24, OC-48, OC-96, OC-192, OC-768.

Kênh vô tuyến mặt đất

Các kênh vô tuyến mang tín hiệu trong phổ điện từ. Chúng là một phương tiện hấp dẫn vì không cần lắp đặt dây vật lý, có thể xuyên tường, cung cấp kết nối cho người dùng di động và có khả năng truyền tín hiệu ở khoảng cách xa. Các đặc tính của kênh vô tuyến phụ thuộc đáng kể vào môi trường truyền sóng và khoảng cách truyền tín hiệu. Các cân nhắc về môi trường xác định tổn thất đường truyền và pha đinh bóng (làm giảm cường độ tín hiệu khi tín hiệu truyền qua một khoảng cách và xung quanh/xuyên qua các vật thể cản trở), pha đinh đa đường (do phản xạ tín hiệu khỏi các vật thể gây nhiễu) và nhiễu (do truyền khác và tín hiệu điện từ).

Các kênh vô tuyến mặt đất có thể được phân loại thành ba nhóm: các kênh hoạt động ở khoảng cách rất ngắn (ví dụ: một hoặc hai mét); những hoạt động ở khu vực địa phương, thường kéo dài từ mười đến vài trăm mét; và những hoạt động trên phạm vi rộng, kéo dài hàng chục km. Các thiết bị cá nhân như tai nghe không dây, bàn phím và thiết bị y tế hoạt động trong khoảng cách ngắn; các công nghệ mạng LAN không dây được mô tả trong Phần 1.2.1 sử dụng các kênh vô tuyến cục bộ; công nghệ truy cập di động sử dụng các kênh vô tuyến diện rộng. Chúng ta sẽ thảo luận chi tiết về các kênh radio trong Chương 7.

Kênh vô tuyến vệ tinh

Một vệ tinh liên lạc liên kết hai hoặc nhiều máy phát/thu vi sóng trên Trái đất, được gọi là các trạm mặt đất. Vệ tinh nhận tín hiệu truyền trên một băng tần, tái tạo tín hiệu bằng bộ lặp (được thảo luận bên dưới) và truyền tín hiệu trên tần số khác. Hai loại vệ tinh được sử dụng trong liên lạc: vệ tinh địa tĩnh và vệ tinh quay quanh quỹ đạo trái đất thấp (LEO).

Các vệ tinh địa tĩnh luôn ở trên cùng một vị trí trên Trái đất. Sự hiện diện cố định này đạt được bằng cách đặt vệ tinh vào quỹ đạo ở độ cao 36.000 km so với bề mặt Trái đất. Khoảng cách lớn này từ trạm mặt đất qua vệ tinh trở lại trạm mặt đất gây ra độ trễ truyền tín hiệu đáng kể là 280 mili giây. Tuy nhiên, các liên kết vệ tinh, có thể hoạt động ở tốc độ hàng trăm Mbps, thường được sử dụng ở những khu vực không có quyền truy cập DSL hoặc truy cập Internet qua cáp.

Các vệ tinh LEO được đặt gần Trái đất hơn nhiều và không tồn tại vĩnh viễn ở một vị trí trên Trái đất. Chúng quay quanh Trái đất (giống như Mặt trăng) và có thể liên lạc với nhau cũng như với các trạm mặt đất. Để cung cấp vùng phủ sóng liên tục cho một khu vực, cần phải đặt nhiều vệ tinh trên quỹ đạo. Hiện nay có nhiều hệ thống thông tin liên lạc tầm thấp đang được phát triển. Công nghệ vệ tinh LEO có thể được sử dụng để truy cập Internet trong tương lai.

*Hình 1.10 ♦ Lõi mạng*

Content Provider Network (Mạng nhà cung cấp nội dung)

Quốc gia hoặc

Global ISP (ISP Toàn cầu)

Datacenter Network (Mạng trung tâm dữ liệu)

Datacenter Network (Mạng trung tâm dữ liệu)

Mobile Network (Mạng di động)

Enterprise Network (Mạng doanh nghiệp)

Home Network (Mạng gia đình)

Local or Regional ISP (ISP Địa phương hoặc Khu vực)

**1.3 Lõi mạng**

Sau khi đã xem xét ranh giới của Internet, bây giờ chúng ta hãy nghiên cứu sâu hơn bên trong lõi mạng---mạng lưới các chuyển mạch gói và liên kết kết nối các hệ thống đầu cuối của Internet. Hình 1.10 làm nổi bật lõi mạng bằng các đường đậm và bóng mờ.

**1.3.1 Packet Chuyển mạch**

Trong một ứng dụng mạng, các hệ thống cuối trao đổi tin nhắn với nhau. Tin nhắn có thể chứa bất cứ điều gì người thiết kế ứng dụng muốn. Tin nhắn có thể thực hiện chức năng điều khiển (ví dụ: tin nhắn "Xin chào" trong ví dụ bắt tay của chúng tôi trong Hình 1.2) hoặc có thể chứa dữ liệu, chẳng hạn như tin nhắn e-mail, hình ảnh JPEG hoặc tệp âm thanh MP3. Để gửi tin nhắn từ hệ thống đầu nguồn đến hệ thống đầu cuối đích, nguồn sẽ chia các tin nhắn dài thành các khối dữ liệu nhỏ hơn được gọi là gói. Giữa nguồn và đích, mỗi gói di chuyển thông qua các liên kết truyền thông và chuyển mạch gói (trong đó có hai loại chiếm ưu thế là bộ định tuyến và chuyển mạch lớp liên kết). Packets được truyền qua mỗi liên kết truyền thông với tốc độ bằng tốc độ truyền đầy đủ của liên kết. Vì vậy, nếu hệ thống đầu cuối nguồn hoặc bộ chuyển mạch gói đang gửi một gói L bit qua một liên kết có tốc độ truyền R bit/giây thì thời gian để truyền gói là L/R giây.

Truyền tải lưu trữ và chuyển tiếp

Hầu hết các chuyển mạch gói sử dụng phương thức truyền lưu trữ và chuyển tiếp ở đầu vào của các liên kết. Truyền lưu trữ và chuyển tiếp có nghĩa là bộ chuyển mạch gói phải nhận toàn bộ gói trước khi nó có thể bắt đầu truyền bit đầu tiên của gói lên liên kết ngoài. Để khám phá việc truyền tải lưu trữ và chuyển tiếp chi tiết hơn, hãy xem xét một mạng đơn giản bao gồm hai hệ thống đầu cuối được kết nối bởi một bộ định tuyến duy nhất, như trong Hình 1.11. Một bộ định tuyến thường có nhiều liên kết sự cố, vì nhiệm vụ của nó là chuyển một gói đến thành một liên kết đi; trong ví dụ đơn giản này, bộ định tuyến có nhiệm vụ khá đơn giản là chuyển gói từ một liên kết (đầu vào) sang liên kết duy nhất được đính kèm khác. Trong ví dụ này, nguồn có ba gói, mỗi gói gồm L bit, để gửi đến đích. Tại thời điểm nhanh như trong Hình 1.11, nguồn đã truyền một số gói 1 và mặt trước của gói 1 đã đến bộ định tuyến. Vì bộ định tuyến sử dụng tính năng lưu trữ và chuyển tiếp nên tại thời điểm này, bộ định tuyến không thể truyền các bit mà nó đã nhận được; thay vào đó, trước tiên nó phải đệm (tức là "lưu trữ") các bit của gói. Chỉ sau khi bộ định tuyến đã nhận được tất cả các bit của gói, nó mới có thể bắt đầu truyền (tức là "chuyển tiếp") gói lên liên kết ngoài. Để hiểu rõ hơn về quá trình truyền lưu trữ và chuyển tiếp, bây giờ chúng ta hãy tính khoảng thời gian trôi qua kể từ khi nguồn bắt đầu gửi gói cho đến khi đích nhận được toàn bộ gói. (Ở đây chúng ta sẽ bỏ qua độ trễ lan truyền---thời gian cần thiết để các bit truyền qua dây với tốc độ gần bằng tốc độ ánh sáng---sẽ được thảo luận trong Phần 1.4.) Nguồn bắt đầu truyền tại thời điểm 0; tại thời điểm L/R giây, nguồn đã truyền toàn bộ gói và toàn bộ gói đã được nhận và lưu trữ tại bộ định tuyến (vì không có độ trễ truyền). Tại thời điểm L/R giây, do bộ định tuyến vừa nhận được toàn bộ gói tin nên nó có thể bắt đầu truyền gói tin lên liên kết ngoài tới đích; tại thời điểm 2L/R, bộ định tuyến đã truyền toàn bộ gói và toàn bộ gói đã được đích nhận. Do đó, tổng độ trễ là 2L/R. Nếu

Thay vào đó, hãy chuyển các bit được chuyển tiếp ngay khi chúng đến (không nhận toàn bộ gói trước), khi đó tổng độ trễ sẽ là L/R do các bit không được giữ ở bộ định tuyến. Tuy nhiên, như chúng ta sẽ thảo luận trong Phần 1.4, các bộ định tuyến cần nhận, lưu trữ và xử lý toàn bộ gói trước khi chuyển tiếp.

Bây giờ hãy tính khoảng thời gian trôi qua kể từ khi nguồn bắt đầu gửi gói đầu tiên cho đến khi đích nhận được cả ba gói. Như trước đây, tại thời điểm L/R, bộ định tuyến bắt đầu chuyển tiếp gói đầu tiên. Nhưng cũng tại thời điểm L/R, nguồn sẽ bắt đầu gửi gói thứ hai vì nó vừa gửi xong toàn bộ gói đầu tiên. Như vậy, tại thời điểm 2L/R, đích đã nhận được gói đầu tiên và bộ định tuyến đã nhận được gói thứ hai. Tương tự, tại thời điểm 3L/R, đích đã nhận được hai gói đầu tiên và bộ định tuyến đã nhận được gói thứ ba. Cuối cùng, tại thời điểm 4L/R đích đã nhận được cả ba gói tin!

Bây giờ chúng ta hãy xem xét trường hợp chung của việc gửi một gói từ nguồn đến đích qua một đường dẫn bao gồm N liên kết với mỗi tốc độ R (do đó, có N-1 bộ định tuyến giữa nguồn và đích). Áp dụng logic tương tự như trên, chúng ta thấy độ trễ từ đầu đến cuối là:

dend@to@end = N L

R (1.1)

Bây giờ bạn có thể muốn thử xác định độ trễ đối với các gói P được gửi qua một loạt N liên kết.

Trì hoãn xếp hàng và mất Packet

Mỗi chuyển mạch gói có nhiều liên kết gắn liền với nó. Đối với mỗi liên kết được đính kèm, bộ chuyển mạch gói có một bộ đệm đầu ra (còn gọi là hàng đợi đầu ra), nơi lưu trữ các gói mà bộ định tuyến sắp gửi vào liên kết đó. Bộ đệm đầu ra đóng một vai trò quan trọng trong việc chuyển mạch gói. Nếu một gói đến cần được truyền vào một liên kết nhưng thấy liên kết đó bận với việc truyền gói khác thì gói đến phải đợi trong bộ đệm đầu ra. Do đó, ngoài độ trễ lưu trữ và chuyển tiếp, các gói còn phải chịu độ trễ xếp hàng bộ đệm đầu ra. Những độ trễ này có thể thay đổi và phụ thuộc vào

*Hình 1.11 ♦ Chuyển mạch gói lưu trữ và chuyển tiếp*

Nguồn

R bps

Đích Mặt trước của gói 1 được lưu trong bộ định tuyến, chờ các bit còn lại trước khi chuyển tiếp

mức độ tắc nghẽn trong mạng. Vì dung lượng bộ đệm là hữu hạn nên gói đến có thể thấy rằng bộ đệm đã đầy hoàn toàn với các gói khác đang chờ truyền. Trong trường hợp này, việc mất gói sẽ xảy ra---gói đến hoặc một trong các gói đã được xếp hàng đợi sẽ bị loại bỏ.

Hình 1.12 minh họa một mạng chuyển mạch gói đơn giản. Như trong Hình 1.11, các gói được biểu diễn bằng các tấm ba chiều. Chiều rộng của tấm biểu thị số bit trong gói. Trong hình này, tất cả các gói có cùng chiều rộng và do đó có cùng chiều dài. Giả sử Hosts A và B đang gửi gói đến Host E. Hosts A và B trước tiên gửi gói của họ dọc theo liên kết Ethernet 100 Mbps đến bộ định tuyến đầu tiên. Sau đó, bộ định tuyến sẽ hướng các gói này đến liên kết 15 Mbps. Nếu trong một khoảng thời gian ngắn, tốc độ đến của các gói đến bộ định tuyến (khi được chuyển đổi thành bit trên giây) vượt quá 15 Mbps, tắc nghẽn sẽ xảy ra tại bộ định tuyến khi các gói xếp hàng trong bộ đệm đầu ra của liên kết trước khi được truyền vào liên kết. Ví dụ: nếu Host A và B mỗi người gửi một loạt năm gói liên tiếp nhau cùng một lúc thì hầu hết các gói này sẽ mất một khoảng thời gian chờ đợi trong hàng đợi. Trên thực tế, tình huống này hoàn toàn tương tự với nhiều tình huống thường ngày -- chẳng hạn như khi chúng ta xếp hàng chờ giao dịch viên ngân hàng hoặc đợi trước trạm thu phí. Chúng ta sẽ xem xét độ trễ xếp hàng này chi tiết hơn trong Phần 1.4.

Bảng chuyển tiếp và giao thức định tuyến

Trước đó, chúng ta đã nói rằng bộ định tuyến nhận một gói đến trên một trong các liên kết truyền thông được đính kèm của nó và chuyển tiếp gói đó đến một liên kết truyền thông được đính kèm khác. Nhưng làm thế nào để bộ định tuyến xác định nên liên kết nào

*Hình 1.12 ♦ Packet chuyển mạch*

Ethernet 100 Mb/giây

Chú giải:

Packets

MỘT

B

C

D E

15 Mb/giây

Hàng đợi các gói tin chờ liên kết đầu ra

chuyển tiếp gói tin lên? Packet chuyển tiếp thực sự được thực hiện theo nhiều cách khác nhau trong các loại mạng máy tính khác nhau. Ở đây, chúng tôi mô tả ngắn gọn cách nó được thực hiện trên Internet.

Trên Internet, mọi hệ thống đầu cuối đều có một địa chỉ được gọi là địa chỉ IP. Khi hệ thống đầu cuối nguồn muốn gửi một gói đến hệ thống đầu cuối đích, nguồn sẽ bao gồm địa chỉ IP của đích trong tiêu đề của gói. Giống như địa chỉ bưu chính, địa chỉ này có cấu trúc phân cấp. Khi một gói đến một bộ định tuyến trong mạng, bộ định tuyến sẽ kiểm tra một phần địa chỉ đích của gói và chuyển tiếp gói đến bộ định tuyến lân cận. Cụ thể hơn, mỗi bộ định tuyến có một bảng chuyển tiếp ánh xạ các địa chỉ đích (hoặc một phần địa chỉ đích) tới các liên kết ngoài của bộ định tuyến đó. Khi một gói đến bộ định tuyến, bộ định tuyến sẽ kiểm tra địa chỉ và tìm kiếm bảng chuyển tiếp của nó, sử dụng địa chỉ đích này để tìm liên kết ra ngoài thích hợp. Sau đó, bộ định tuyến sẽ hướng gói tin đến liên kết ngoài này.

Quá trình định tuyến từ đầu đến cuối tương tự như một người lái xe ô tô không sử dụng bản đồ mà thay vào đó thích hỏi đường. Ví dụ: giả sử Joe đang lái xe từ Philadelphia đến 156 Lakeside Drive ở Orlando, Florida. Lần đầu tiên Joe lái xe đến trạm xăng gần nhà và hỏi cách đến 156 Lakeside Drive ở Orlando, Florida. Nhân viên trạm xăng trích xuất phần địa chỉ ở Florida và nói với Joe rằng anh ta cần đi lên đường cao tốc liên bang I-95 South, nơi có lối vào ngay cạnh trạm xăng. Anh ấy cũng nói với Joe rằng khi đến Florida, anh ấy nên nhờ người khác ở đó. Sau đó, Joe đi theo I-95 South cho đến khi đến Jacksonville, Florida, lúc đó anh ấy hỏi một nhân viên trạm xăng khác để chỉ đường. Người phục vụ trích xuất phần địa chỉ ở Orlando và nói với Joe rằng anh ta nên tiếp tục đi trên đường I-95 đến Bãi biển Daytona rồi hỏi người khác. Tại Bãi biển Daytona, một nhân viên trạm xăng khác cũng trích xuất phần địa chỉ của Orlando và nói với Joe rằng anh ta nên đi thẳng I-4 đến Orlando. Joe đi I-4 và xuống ở lối ra Orlando. Joe đến gặp một nhân viên trạm xăng khác, và lần này người phục vụ trích xuất phần địa chỉ của Lakeside Drive và nói cho Joe biết con đường anh ta phải đi để đến Lakeside Drive. Khi Joe đến Lakeside Drive, anh ấy hỏi một đứa trẻ đang đi xe đạp cách đến đích. Đứa trẻ trích xuất phần 156 của địa chỉ và chỉ vào ngôi nhà. Joe cuối cùng cũng đến được đích cuối cùng của mình. Trong phép so sánh trên, nhân viên trạm xăng và trẻ em đi xe đạp cũng tương tự như bộ định tuyến.

Chúng ta vừa biết rằng bộ định tuyến sử dụng địa chỉ đích của gói để lập chỉ mục cho bảng chuyển tiếp và xác định liên kết ra ngoài thích hợp. Nhưng tuyên bố này đặt ra một câu hỏi khác: Làm thế nào để thiết lập các bảng chuyển tiếp? Chúng được cấu hình thủ công trong từng bộ định tuyến hay Internet sử dụng quy trình tự động hơn? Vấn đề này sẽ được nghiên cứu sâu trong Chương 5. Nhưng để kích thích sự quan tâm của bạn ở đây, chúng ta sẽ lưu ý rằng Internet có một số giao thức định tuyến đặc biệt được sử dụng để tự động thiết lập các bảng chuyển tiếp. Ví dụ, một giao thức định tuyến có thể xác định đường đi ngắn nhất từ ​​mỗi bộ định tuyến đến từng đích và sử dụng kết quả đường đi ngắn nhất để định cấu hình các bảng chuyển tiếp trong bộ định tuyến.

**1.3.2 Circuit Switching**

Có hai cách tiếp cận cơ bản để di chuyển dữ liệu qua mạng liên kết và chuyển mạch: chuyển mạch và chuyển mạch gói. Đã đề cập đến các mạng chuyển mạch gói ở phần trước, bây giờ chúng ta chuyển sự chú ý sang các mạng chuyển mạch kênh.

Trong các mạng chuyển mạch kênh, các tài nguyên cần thiết dọc theo đường dẫn (bộ đệm, tốc độ truyền liên kết) để cung cấp cho hoạt động liên lạc giữa các hệ thống đầu cuối được dành riêng trong suốt thời gian phiên liên lạc giữa các hệ thống đầu cuối. Trong mạng chuyển mạch gói, những tài nguyên này không được bảo lưu; Các tin nhắn của phiên sử dụng tài nguyên theo yêu cầu và do đó, có thể phải chờ (nghĩa là xếp hàng) để truy cập vào liên kết truyền thông. Một sự tương tự đơn giản, hãy xem xét hai nhà hàng, một nhà hàng yêu cầu đặt chỗ trước và một nhà hàng khác không yêu cầu đặt chỗ trước cũng như không chấp nhận chúng. Đối với nhà hàng yêu cầu đặt chỗ trước, chúng tôi phải gặp rắc rối khi gọi điện trước khi rời khỏi nhà. Nhưng về nguyên tắc, khi đến nhà hàng, chúng ta có thể ngồi ngay lập tức và gọi món. Đối với nhà hàng không yêu cầu đặt chỗ trước, chúng ta không cần mất công đặt bàn. Nhưng khi đến nhà hàng, chúng ta có thể phải đợi một bàn mới có thể ngồi được.

Mạng điện thoại truyền thống là ví dụ về mạng chuyển mạch. Hãy xem điều gì sẽ xảy ra khi một người muốn gửi thông tin (thoại hoặc fax) cho người khác qua mạng điện thoại. Trước khi người gửi có thể gửi thông tin, mạng phải thiết lập kết nối giữa người gửi và người nhận. Đây là một kết nối thực sự mà các công tắc trên đường dẫn giữa người gửi và người nhận duy trì trạng thái kết nối cho kết nối đó. Trong thuật ngữ điện thoại, kết nối này được gọi là mạch điện. Khi mạng thiết lập mạch, nó cũng dự trữ tốc độ truyền không đổi trong các liên kết của mạng (đại diện cho một phần công suất truyền của mỗi liên kết) trong suốt thời gian kết nối. Vì tốc độ truyền nhất định đã được dành riêng cho kết nối người gửi đến người nhận này nên người gửi có thể truyền dữ liệu đến người nhận với tốc độ không đổi được đảm bảo.

Hình 1.13 minh họa mạng chuyển mạch. Trong mạng này, bốn thiết bị chuyển mạch được kết nối với nhau bằng bốn liên kết. Mỗi liên kết này có bốn mạch, do đó mỗi liên kết có thể hỗ trợ bốn kết nối đồng thời. Các máy chủ (ví dụ: PC và máy trạm) đều được kết nối trực tiếp với một trong các thiết bị chuyển mạch. Khi hai máy chủ muốn liên lạc, mạng sẽ thiết lập kết nối đầu cuối chuyên dụng giữa hai máy chủ. Do đó, để Host A giao tiếp với Host B, trước tiên mạng phải dự trữ một mạch trên mỗi liên kết trong số hai liên kết. Trong ví dụ này, kết nối đầu cuối chuyên dụng sử dụng mạch thứ hai trong liên kết đầu tiên và mạch thứ tư trong liên kết thứ hai. Vì mỗi liên kết có bốn mạch nên đối với mỗi liên kết được sử dụng bởi kết nối đầu cuối, kết nối sẽ nhận được 1/4 tổng công suất truyền của liên kết trong suốt thời gian kết nối. Do đó, ví dụ: nếu mỗi liên kết giữa các thiết bị chuyển mạch liền kề có tốc độ truyền là 1 Mbps thì mỗi kết nối chuyển mạch kênh đầu cuối sẽ nhận được tốc độ truyền chuyên dụng là 250 kbps.

*Hình 1.13 ♦ Một mạng chuyển mạch đơn giản gồm 4 switch*

và bốn liên kết

Ngược lại, hãy xem xét điều gì sẽ xảy ra khi một máy chủ muốn gửi gói đến máy chủ khác qua mạng chuyển mạch gói, chẳng hạn như Internet. Giống như chuyển mạch, gói được truyền qua một loạt các liên kết truyền thông. Nhưng khác với chuyển mạch kênh, gói được gửi vào mạng mà không dự trữ bất kỳ tài nguyên liên kết nào. Nếu một trong các liên kết bị tắc nghẽn do các gói khác cần được truyền qua liên kết cùng lúc thì gói đó sẽ phải chờ trong bộ đệm ở phía gửi của liên kết truyền và bị trễ. Internet nỗ lực hết sức để cung cấp các gói tin một cách kịp thời nhưng không đưa ra bất kỳ sự đảm bảo nào.

Ghép kênh trong mạng chuyển mạch

Một mạch trong một liên kết được triển khai bằng cách ghép kênh phân chia theo tần số (FDM) hoặc ghép kênh phân chia theo thời gian (TDM). Với FDM, phổ tần số của một liên kết được chia cho các kết nối được thiết lập trên toàn liên kết. Cụ thể, liên kết dành một băng tần cho mỗi kết nối trong suốt thời gian kết nối. Trong mạng điện thoại, dải tần này thường có độ rộng 4 kHz (nghĩa là 4.000 hertz hoặc 4.000 chu kỳ mỗi giây). Không có gì ngạc nhiên khi độ rộng của băng tần được gọi là băng thông. Các đài phát thanh FM cũng sử dụng FDM để chia sẻ phổ tần số từ 88 MHz đến 108 MHz, với mỗi đài được phân bổ một dải tần số cụ thể.

Đối với liên kết TDM, thời gian được chia thành các khung có thời lượng cố định và mỗi khung được chia thành một số khe thời gian cố định. Khi mạng thiết lập kết nối qua một liên kết, mạng sẽ dành một khe thời gian trong mỗi khung cho kết nối này. Các khe này được dành riêng cho mục đích sử dụng duy nhất của kết nối đó, với một khe thời gian có sẵn để sử dụng (trong mỗi khung) để truyền dữ liệu của kết nối.

Hình 1.14 minh họa FDM và TDM cho một liên kết mạng cụ thể hỗ trợ tối đa bốn mạch. Đối với FDM, miền tần số được phân thành bốn băng tần, mỗi băng thông 4 kHz. Đối với TDM, miền thời gian được phân thành các khung, với bốn khe thời gian trong mỗi khung; mỗi mạch được gán cùng một khe chuyên dụng trong các khung TDM quay. Đối với TDM, tốc độ truyền của mạch bằng tốc độ khung hình nhân với số bit trong một khe. Ví dụ: nếu liên kết truyền 8.000 khung hình mỗi giây và mỗi khe bao gồm 8 bit thì tốc độ truyền của mỗi mạch là 64 kbps.

Những người ủng hộ chuyển mạch gói luôn lập luận rằng chuyển mạch là lãng phí vì các mạch chuyên dụng không hoạt động trong thời gian im lặng. Ví dụ: khi một người trong cuộc gọi điện thoại ngừng nói chuyện, các tài nguyên mạng nhàn rỗi (dải tần số hoặc khe thời gian trong các liên kết dọc theo tuyến đường kết nối) không thể được sử dụng bởi các kết nối đang diễn ra khác. Một ví dụ khác về việc các tài nguyên này có thể bị sử dụng không đúng mức, hãy xem xét một bác sĩ X quang sử dụng mạng chuyển mạch để truy cập từ xa một loạt ảnh X-quang. Bác sĩ X quang thiết lập kết nối, yêu cầu một hình ảnh, xem hình ảnh và sau đó yêu cầu một hình ảnh mới. Tài nguyên mạng được phân bổ cho kết nối nhưng không được sử dụng (tức là bị lãng phí) trong thời gian dự tính của bác sĩ X quang. Những người ủng hộ chuyển mạch gói cũng chỉ ra rằng việc thiết lập các mạch đầu cuối và dự trữ dung lượng truyền dẫn đầu cuối là phức tạp và cần có phần mềm tín hiệu phức tạp để phối hợp hoạt động của các bộ chuyển mạch dọc theo đường dẫn đầu cuối.

*Hình 1.14 ♦ Với FDM, mỗi mạch liên tục nhận được một phần tín hiệu*

băng thông. Với TDM, mỗi mạch nhận được tất cả băng thông theo định kỳ trong khoảng thời gian ngắn (nghĩa là trong các khe)

4KHz

TDM

FDM

Tần số liên kết

4KHz

Chỗ

Chú giải:

Tất cả các vị trí có nhãn "2" được dành riêng cho một cặp người gửi-người nhận cụ thể.

Frame

Thời gian

Trước khi kết thúc cuộc thảo luận về chuyển mạch, chúng ta hãy xem xét một ví dụ bằng số để hiểu rõ hơn về chủ đề này. Chúng ta hãy xem xét phải mất bao lâu để gửi một tệp 640.000 bit từ Host A đến Host B qua mạng chuyển mạch. Giả sử tất cả các liên kết trong mạng đều sử dụng TDM với 24 slot và có tốc độ bit là 1,536 Mbps. Ngoài ra, giả sử rằng phải mất 500 mili giây để thiết lập mạch đầu cuối trước khi Host A có thể bắt đầu truyền tệp. Mất bao lâu để gửi tập tin? Mỗi mạch có tốc độ truyền (1,536 Mbps)/24 = 64 kbps, do đó phải mất (640.000 bit)/(64 kbps) = 10 giây để truyền tệp. Với 10 giây này, chúng tôi thêm thời gian thiết lập mạch, dành 10,5 giây để gửi tệp. Lưu ý rằng thời gian truyền không phụ thuộc vào số lượng liên kết: Thời gian truyền sẽ là 10 giây nếu mạch đầu cuối đi qua một liên kết hoặc một trăm liên kết. (Độ trễ từ đầu đến cuối thực tế cũng bao gồm độ trễ lan truyền; xem Phần 1.4.)

Packet Chuyển đổi so với Circuit Switching

Sau khi đã mô tả chuyển mạch kênh và chuyển mạch gói, chúng ta hãy so sánh cả hai. Những người chỉ trích chuyển mạch gói thường lập luận rằng chuyển mạch gói không phù hợp với các dịch vụ thời gian thực (ví dụ: các cuộc gọi điện thoại và cuộc gọi hội nghị video) vì độ trễ đầu cuối thay đổi và không thể đoán trước (chủ yếu do độ trễ xếp hàng thay đổi và không thể đoán trước). Những người ủng hộ chuyển mạch gói cho rằng (1) nó cung cấp khả năng chia sẻ dung lượng truyền tải tốt hơn so với chuyển mạch kênh và (2) nó đơn giản hơn, hiệu quả hơn và ít tốn kém hơn khi thực hiện so với chuyển mạch kênh. Một cuộc thảo luận thú vị về chuyển mạch gói và chuyển mạch kênh là \[MolineroFernandez 2002\]. Nói chung, những người không thích rắc rối với việc đặt chỗ nhà hàng thích chuyển mạch gói hơn chuyển mạch kênh.

Tại sao chuyển mạch gói hiệu quả hơn? Hãy xem một ví dụ đơn giản. Giả sử người dùng chia sẻ liên kết 1 Mbps. Ngoài ra, giả sử rằng mỗi người dùng luân phiên giữa các khoảng thời gian hoạt động khi người dùng tạo dữ liệu với tốc độ không đổi 100 kbps và các khoảng thời gian không hoạt động khi người dùng không tạo ra dữ liệu. Giả sử thêm rằng người dùng chỉ hoạt động trong 10% thời gian (và uống cà phê nhàn rỗi trong 90% thời gian còn lại). Với chuyển mạch, 100 kbps phải được dành riêng cho mỗi người dùng mọi lúc. Ví dụ: với TDM chuyển mạch kênh, nếu khung một giây được chia thành 10 khe thời gian, mỗi khe 100 ms thì mỗi người dùng sẽ được phân bổ một khe thời gian cho mỗi khung.

Do đó, liên kết chuyển mạch kênh chỉ có thể hỗ trợ 10 người dùng đồng thời (= 1 Mbps/100 kbps). Với chuyển mạch gói, xác suất để một người dùng cụ thể hoạt động là 0,1 (tức là 10%). Nếu có 35 người dùng thì xác suất có 11 người dùng hoạt động đồng thời trở lên là khoảng 0,0004. (Bài tập về nhà P8 nêu cách đạt được xác suất này.) Khi có 10 người dùng hoạt động đồng thời trở xuống (xảy ra với xác suất 0,9996), tốc độ đến tổng hợp của dữ liệu nhỏ hơn hoặc bằng 1 Mbps, tốc độ đầu ra của liên kết. Do đó, khi có 10 người dùng hoạt động trở xuống, các gói của người dùng sẽ truyền qua liên kết về cơ bản.

không chậm trễ, giống như trường hợp chuyển mạch. Khi có hơn 10 người dùng hoạt động đồng thời thì tốc độ đến tổng hợp của các gói sẽ vượt quá khả năng đầu ra của liên kết và hàng đợi đầu ra sẽ bắt đầu tăng lên. (Nó tiếp tục tăng cho đến khi tốc độ đầu vào tổng hợp giảm xuống dưới 1 Mbps, tại thời điểm đó hàng đợi sẽ bắt đầu giảm độ dài.) Bởi vì xác suất có hơn 10 người dùng hoạt động đồng thời trong ví dụ này là rất nhỏ, chuyển mạch gói về cơ bản cung cấp hiệu suất tương tự như chuyển mạch kênh, nhưng làm như vậy trong khi cho phép số lượng người dùng nhiều hơn ba lần.

Bây giờ chúng ta hãy xem xét một ví dụ đơn giản thứ hai. Giả sử có 10 người dùng và một người dùng đột nhiên tạo ra một nghìn gói 1.000 bit, trong khi những người dùng khác vẫn không hoạt động và không tạo gói. Trong chuyển mạch TDM với 10 khe trên mỗi khung và mỗi khe bao gồm 1.000 bit, người dùng tích cực chỉ có thể sử dụng một khe thời gian trên mỗi khung để truyền dữ liệu, trong khi chín khe thời gian còn lại trong mỗi khung vẫn ở chế độ rảnh. Sẽ mất 10 giây trước khi tất cả một triệu bit dữ liệu của người dùng đang hoạt động được truyền đi. Trong trường hợp chuyển mạch gói, người dùng đang hoạt động có thể liên tục gửi các gói của mình với tốc độ liên kết đầy đủ là 1 Mbps, vì không có người dùng nào khác tạo ra các gói cần được ghép kênh với các gói của người dùng đang hoạt động. Trong trường hợp này, tất cả dữ liệu của người dùng đang hoạt động sẽ được truyền trong vòng 1 giây.

Các ví dụ trên minh họa hai cách mà hiệu suất của chuyển mạch gói có thể vượt trội hơn so với chuyển mạch kênh. Họ cũng nêu bật sự khác biệt quan trọng giữa hai hình thức chia sẻ tốc độ truyền của liên kết giữa nhiều luồng dữ liệu. Chuyển mạch kênh phân bổ trước việc sử dụng liên kết truyền tải bất kể nhu cầu, với thời gian liên kết được phân bổ nhưng không cần thiết sẽ không được sử dụng. Packet mặt khác chuyển đổi phân bổ việc sử dụng liên kết theo yêu cầu. Dung lượng truyền liên kết sẽ chỉ được chia sẻ trên cơ sở từng gói giữa những người dùng có gói cần được truyền qua liên kết.

Mặc dù chuyển mạch gói và chuyển mạch kênh đều phổ biến trong các mạng viễn thông ngày nay nhưng xu hướng chắc chắn là theo hướng chuyển mạch gói. Thậm chí nhiều mạng điện thoại chuyển mạch ngày nay đang dần chuyển sang chuyển mạch gói. Đặc biệt, các mạng điện thoại thường sử dụng chuyển mạch gói cho phần cuộc gọi điện thoại ra nước ngoài đắt tiền.

**1.3.3 Mạng của các mạng**

Trước đó chúng ta đã thấy rằng các hệ thống đầu cuối (PC, điện thoại thông minh, máy chủ Web, máy chủ thư, v.v.) kết nối với Internet thông qua ISP truy cập. ISP truy cập có thể cung cấp kết nối có dây hoặc không dây, sử dụng một loạt công nghệ truy cập bao gồm DSL, cáp, FTTH, Wi-Fi và di động. Lưu ý rằng ISP truy cập không nhất thiết phải là công ty viễn thông hoặc công ty truyền hình cáp; thay vào đó, nó có thể là một trường đại học (cung cấp quyền truy cập Internet cho sinh viên, nhân viên và giảng viên) hoặc một công ty (cung cấp quyền truy cập cho nhân viên của mình). Nhưng việc kết nối người dùng cuối và nhà cung cấp nội dung với một ISP truy cập chỉ là một phần nhỏ trong việc giải bài toán kết nối hàng tỷ hệ thống cuối tạo nên Internet. Để hoàn thành câu đố này, bản thân các ISP truy cập phải

được kết nối với nhau. Điều này được thực hiện bằng cách tạo ra một mạng lưới các mạng---hiểu được cụm từ này là chìa khóa để hiểu được Internet.

Qua nhiều năm, mạng lưới hình thành nên Internet đã phát triển thành một cấu trúc rất phức tạp. Phần lớn sự phát triển này được thúc đẩy bởi kinh tế và chính sách quốc gia, hơn là bởi những cân nhắc về hiệu quả hoạt động. Để hiểu cấu trúc mạng Internet ngày nay, chúng ta hãy dần dần xây dựng một loạt cấu trúc mạng, trong đó mỗi cấu trúc mới sẽ gần đúng hơn với Internet phức tạp mà chúng ta có ngày nay. Hãy nhớ lại rằng mục tiêu bao trùm là kết nối các ISP truy cập để tất cả các hệ thống đầu cuối có thể gửi gói tin cho nhau. Một cách tiếp cận đơn giản là để mỗi ISP truy cập kết nối trực tiếp với mọi ISP truy cập khác. Tất nhiên, thiết kế dạng lưới như vậy là quá tốn kém đối với các ISP truy cập, vì nó yêu cầu mỗi ISP truy cập phải có một liên kết liên lạc riêng với mỗi trong số hàng trăm nghìn ISP truy cập khác trên toàn thế giới.

Cấu trúc mạng đầu tiên của chúng tôi, Cấu trúc mạng 1, kết nối tất cả các ISP truy cập với một ISP chuyển tuyến toàn cầu duy nhất. ISP chuyển tiếp toàn cầu (tưởng tượng) của chúng tôi là một mạng lưới gồm các bộ định tuyến và liên kết truyền thông không chỉ trải rộng trên toàn cầu mà còn có ít nhất một bộ định tuyến gần mỗi bộ định tuyến trong số hàng trăm nghìn ISP truy cập. Tất nhiên, ISP toàn cầu sẽ rất tốn kém khi xây dựng một mạng lưới rộng khắp như vậy. Để có lợi nhuận, nó sẽ tính phí kết nối của từng ISP truy cập một cách tự nhiên, với mức giá phản ánh (nhưng không nhất thiết phải tỷ lệ thuận với) lượng lưu lượng truy cập mà ISP truy cập trao đổi với ISP toàn cầu. Vì ISP truy cập trả tiền cho ISP chuyển tiếp toàn cầu nên ISP truy cập được cho là khách hàng và ISP chuyển tiếp toàn cầu được cho là nhà cung cấp.

Bây giờ, nếu một số công ty xây dựng và vận hành ISP vận chuyển toàn cầu có lãi thì việc các công ty khác xây dựng ISP vận chuyển toàn cầu của riêng họ và cạnh tranh với ISP vận chuyển toàn cầu ban đầu là điều đương nhiên. Điều này dẫn tới Cấu trúc Mạng 2, bao gồm hàng trăm nghìn ISP truy cập và nhiều ISP chuyển tiếp toàn cầu. Các ISP truy cập chắc chắn thích Cấu trúc mạng 2 hơn Cấu trúc mạng 1 vì giờ đây họ có thể chọn trong số các nhà cung cấp dịch vụ vận chuyển toàn cầu cạnh tranh tùy theo giá cả và dịch vụ của họ. Tuy nhiên, xin lưu ý rằng bản thân các ISP chuyển tuyến toàn cầu phải kết nối với nhau: Nếu không, các ISP truy cập được kết nối với một trong các nhà cung cấp dịch vụ chuyển tuyến toàn cầu sẽ không thể liên lạc với các ISP truy cập được kết nối với các nhà cung cấp dịch vụ chuyển tuyến toàn cầu khác.

Cấu trúc mạng 2, vừa được mô tả, là một hệ thống phân cấp hai tầng với các nhà cung cấp dịch vụ vận chuyển toàn cầu nằm ở tầng trên cùng và truy cập các ISP ở tầng dưới cùng. Điều này giả định rằng các ISP chuyển tiếp toàn cầu không chỉ có khả năng tiếp cận từng ISP truy cập mà còn thấy việc làm đó là mong muốn về mặt kinh tế. Trên thực tế, mặc dù một số ISP có phạm vi phủ sóng toàn cầu ấn tượng và kết nối trực tiếp với nhiều ISP truy cập, nhưng không có ISP nào có mặt ở mọi thành phố trên thế giới. Thay vào đó, ở bất kỳ khu vực cụ thể nào, có thể có một ISP khu vực mà các ISP truy cập trong khu vực đó kết nối. Sau đó, mỗi ISP khu vực sẽ kết nối với các ISP cấp 1. ISP cấp 1 tương tự như ISP chuyển tuyến toàn cầu (tưởng tượng) của chúng tôi; nhưng các ISP cấp 1, thực sự tồn tại, không hiện diện ở mọi thành phố trên thế giới. Có khoảng chục ISP cấp 1, bao gồm Truyền thông cấp 3, AT&T, Sprint và NTT. Điều thú vị là không có nhóm nào chính thức

tình trạng xử phạt cấp 1; như người ta vẫn nói---nếu bạn phải hỏi xem bạn có phải là thành viên của một nhóm hay không thì có lẽ là không.

Quay trở lại với mạng lưới này, không chỉ có nhiều ISP cấp 1 cạnh tranh mà còn có thể có nhiều ISP khu vực cạnh tranh trong một khu vực. Trong hệ thống phân cấp như vậy, mỗi ISP truy cập sẽ thanh toán cho ISP khu vực mà nó kết nối và mỗi ISP khu vực sẽ thanh toán cho ISP cấp 1 mà nó kết nối. (ISP truy cập cũng có thể kết nối trực tiếp với ISP cấp 1, trong trường hợp đó ISP sẽ trả tiền cho ISP cấp 1). Vì vậy, có mối quan hệ nhà cung cấp khách hàng ở mỗi cấp độ của hệ thống phân cấp. Lưu ý rằng các ISP cấp 1 không trả tiền cho bất kỳ ai vì họ đứng đầu hệ thống phân cấp. Vấn đề còn phức tạp hơn nữa, ở một số khu vực, có thể có một ISP khu vực lớn hơn (có thể trải rộng trên toàn bộ quốc gia) mà các ISP khu vực nhỏ hơn trong khu vực đó kết nối tới; ISP khu vực lớn hơn sẽ kết nối với ISP cấp 1. Ví dụ, ở Trung Quốc, có các ISP truy cập ở mỗi thành phố, kết nối với các ISP cấp tỉnh, sau đó kết nối với các ISP cấp quốc gia, cuối cùng kết nối với các ISP cấp 1 \[Tian 2012\]. Chúng tôi gọi hệ thống phân cấp nhiều tầng này, hệ thống này vẫn chỉ gần đúng với Internet ngày nay, là Cấu trúc Mạng 3.

Để xây dựng một mạng gần giống với Internet ngày nay hơn, chúng ta phải thêm các điểm hiện diện (PoP), nhiều điểm truy cập, ngang hàng và trao đổi Internet (IXP) vào Cấu trúc mạng phân cấp 3. PoP tồn tại ở tất cả các cấp của hệ thống phân cấp, ngoại trừ cấp dưới cùng (ISP truy cập). PoP chỉ đơn giản là một nhóm gồm một hoặc nhiều bộ định tuyến (ở cùng một vị trí) trong mạng của nhà cung cấp nơi các ISP của khách hàng có thể kết nối với ISP của nhà cung cấp. Để mạng khách hàng kết nối với PoP của nhà cung cấp, mạng đó có thể thuê liên kết tốc độ cao từ nhà cung cấp dịch vụ viễn thông bên thứ ba để kết nối trực tiếp một trong các bộ định tuyến của họ với bộ định tuyến tại PoP. Bất kỳ ISP nào (ngoại trừ ISP cấp 1) đều có thể chọn kết nối nhiều nhà, nghĩa là kết nối với hai hoặc nhiều ISP của nhà cung cấp. Vì vậy, ví dụ: một ISP truy cập có thể kết nối nhiều nhà với hai ISP khu vực hoặc có thể kết nối nhiều nhà với hai ISP khu vực và cả với ISP cấp 1. Tương tự, một ISP khu vực có thể có nhiều ISP cấp 1. Khi một ISP có nhiều nhà, nó có thể tiếp tục gửi và nhận các gói vào Internet ngay cả khi một trong các nhà cung cấp của nó gặp lỗi.

Như chúng ta vừa tìm hiểu, ISP của khách hàng trả tiền cho ISP của nhà cung cấp của họ để có được khả năng kết nối Internet toàn cầu. Số tiền mà ISP khách hàng trả cho nhà cung cấp ISP phản ánh lượng lưu lượng truy cập mà ISP trao đổi với nhà cung cấp. Để giảm những chi phí này, một cặp ISP lân cận ở cùng cấp độ phân cấp có thể ngang hàng, nghĩa là họ có thể kết nối trực tiếp các mạng của mình với nhau để tất cả lưu lượng truy cập giữa chúng đi qua kết nối trực tiếp thay vì thông qua các trung gian ngược dòng. Khi hai ISP ngang hàng, thường không có sự giải quyết, nghĩa là ISP không trả tiền cho bên kia. Như đã lưu ý trước đó, các ISP cấp 1 cũng ngang hàng với nhau, không cần thanh toán. Để có phần thảo luận dễ đọc về mối quan hệ ngang hàng và khách hàng-nhà cung cấp, hãy xem \[Van der Berg 2008\]. Tương tự như vậy, một công ty bên thứ ba có thể tạo Điểm trao đổi Internet (IXP), đây là điểm gặp gỡ nơi nhiều ISP có thể ngang hàng với nhau. IXP thường ở trong một tòa nhà độc lập với các công tắc riêng \[Ager 2012\]. Hiện nay có hơn 600 IXP trên Internet \[PeeringDB 2020\]. Chúng tôi gọi hệ sinh thái này---bao gồm các ISP truy cập, ISP khu vực, ISP cấp 1, PoP, multi-homing, ngang hàng và IXP---là Cấu trúc Mạng 4.

Cuối cùng chúng ta cũng đã đến Cấu trúc Mạng 5, mô tả Internet ngày nay. Cấu trúc mạng 5, được minh họa trong Hình 1.15, được xây dựng dựa trên Cấu trúc mạng 4 bằng cách thêm các mạng cung cấp nội dung. Google hiện là một trong những ví dụ hàng đầu về mạng lưới cung cấp nội dung như vậy. Theo văn bản này, Google có 19 trung tâm dữ liệu lớn được phân bổ trên khắp Bắc Mỹ, Châu Âu, Châu Á, Nam Mỹ và Úc với mỗi trung tâm dữ liệu có hàng chục hoặc hàng trăm nghìn máy chủ. Ngoài ra, Google có các trung tâm dữ liệu nhỏ hơn, mỗi trung tâm có vài trăm máy chủ; những trung tâm dữ liệu nhỏ hơn này thường nằm trong IXP. Tất cả các trung tâm dữ liệu của Google đều được kết nối với nhau thông qua mạng TCP/IP riêng của Google, mạng này trải rộng trên toàn cầu nhưng vẫn tách biệt với Internet công cộng. Điều quan trọng là mạng riêng của Google chỉ mang lưu lượng truy cập đến/từ máy chủ Google. Như được hiển thị trong Hình 1.15, mạng riêng của Google cố gắng "vượt qua" các cấp cao hơn của Internet bằng cách ngang hàng (không có sự dàn xếp) với các ISP cấp thấp hơn, bằng cách kết nối trực tiếp với họ hoặc bằng cách kết nối với họ tại IXP \[Labovitz 2010\]. Tuy nhiên, do nhiều ISP truy cập vẫn chỉ có thể kết nối được bằng cách chuyển qua mạng cấp 1 nên mạng Google cũng kết nối với ISP cấp 1 và trả tiền cho các ISP đó đối với lưu lượng truy cập mà nó trao đổi với họ. Bằng cách tạo mạng riêng, nhà cung cấp nội dung không chỉ giảm các khoản thanh toán cho các ISP cấp cao hơn mà còn có quyền kiểm soát tốt hơn về cách thức phân phối dịch vụ của mình đến người dùng cuối. Cơ sở hạ tầng mạng của Google được mô tả chi tiết hơn trong Phần 2.6.

Tóm lại, Internet ngày nay---một mạng lưới các mạng---rất phức tạp, bao gồm khoảng chục ISP cấp 1 và hàng trăm nghìn ISP cấp thấp hơn. Các ISP rất đa dạng về phạm vi phủ sóng, một số trải dài trên nhiều lục địa và đại dương, trong khi một số khác chỉ giới hạn ở các khu vực địa lý hẹp. Các ISP cấp thấp hơn kết nối với các ISP cấp cao hơn và các ISP cấp cao hơn kết nối với nhau. Người dùng và nhà cung cấp nội dung là khách hàng của ISP cấp thấp hơn và ISP cấp thấp hơn là khách hàng của ISP cấp cao hơn. Trong những năm gần đây, các nhà cung cấp nội dung lớn cũng đã tạo mạng riêng của họ và kết nối trực tiếp với các ISP cấp thấp hơn nếu có thể.

*Hình 1.15 ♦ Kết nối các ISP*

truy cập

ISP

truy cập

ISP

truy cập

ISP

truy cập

ISP

truy cập

ISP

truy cập

ISP

truy cập

ISP

truy cập

ISP

Khu vực

ISP

Cấp 1

ISP

Nhà cung cấp nội dung

(ví dụ: Google) Cấp 1

ISP

IXP

Khu vực

ISP

IXP IXP

**1.4 Độ trễ, mất mát và Throughput trong mạng Packet-Switched**

Quay lại Phần 1.1, chúng ta đã nói rằng Internet có thể được xem như một cơ sở hạ tầng cung cấp các dịch vụ cho các ứng dụng phân tán chạy trên các hệ thống đầu cuối. Lý tưởng nhất là chúng ta muốn các dịch vụ Internet có thể di chuyển nhiều dữ liệu như chúng ta muốn giữa hai hệ thống đầu cuối bất kỳ, ngay lập tức mà không bị mất dữ liệu. Than ôi, đây là một mục tiêu cao cả, một mục tiêu không thể đạt được trên thực tế. Thay vào đó, mạng máy tính nhất thiết phải hạn chế thông lượng (lượng dữ liệu mỗi giây có thể được truyền) giữa các hệ thống đầu cuối, gây ra độ trễ giữa các hệ thống đầu cuối và thực sự có thể làm mất gói tin. Một mặt, thật không may là các quy luật vật lý của thực tế lại gây ra sự chậm trễ và mất mát cũng như hạn chế thông lượng. Mặt khác, vì mạng máy tính gặp phải những vấn đề này nên có rất nhiều vấn đề hấp dẫn xung quanh cách giải quyết vấn đề - quá đủ để lấp đầy một khóa học về mạng máy tính và thúc đẩy hàng nghìn luận án tiến sĩ! Trong phần này, chúng ta sẽ bắt đầu kiểm tra và định lượng độ trễ, mất mát và thông lượng trong mạng máy tính.

**1.4.1 Tổng quan về độ trễ trong mạng Packet-Switched**

Hãy nhớ lại rằng một gói bắt đầu ở một máy chủ (nguồn), đi qua một loạt các bộ định tuyến và kết thúc hành trình của nó ở một máy chủ khác (đích). Khi một gói di chuyển từ một nút (máy chủ hoặc bộ định tuyến) đến nút tiếp theo (máy chủ hoặc bộ định tuyến) dọc theo đường dẫn này, gói sẽ phải chịu một số loại độ trễ tại mỗi nút dọc theo đường dẫn. Điều quan trọng nhất trong số các độ trễ này là độ trễ xử lý nút, độ trễ xếp hàng, độ trễ truyền và độ trễ lan truyền; cùng với nhau, những độ trễ này tích tụ lại để tạo ra tổng độ trễ nút. Hiệu suất của nhiều ứng dụng Internet---chẳng hạn như tìm kiếm, duyệt Web, e-mail, bản đồ, nhắn tin tức thời và giọng nói-IP---bị ảnh hưởng rất nhiều bởi độ trễ mạng. Để có được sự hiểu biết sâu sắc về chuyển mạch gói và mạng máy tính, chúng ta phải hiểu bản chất và tầm quan trọng của những độ trễ này.

Các loại độ trễ

Hãy cùng khám phá những độ trễ này trong bối cảnh của Hình 1.16. Là một phần của tuyến đường đầu cuối giữa nguồn và đích, một gói được gửi từ nút ngược dòng thông qua bộ định tuyến A đến bộ định tuyến B. Mục tiêu của chúng tôi là mô tả độ trễ của nút tại bộ định tuyến A. Lưu ý rằng bộ định tuyến A có một liên kết ngoài dẫn đến bộ định tuyến B. Liên kết này được bắt đầu bằng một hàng đợi (còn được gọi là bộ đệm). Khi gói đến bộ định tuyến A từ nút ngược dòng, bộ định tuyến A sẽ kiểm tra tiêu đề của gói để xác định liên kết ngoài thích hợp cho gói và sau đó chuyển gói đến liên kết này. Trong ví dụ này, liên kết ngoài của gói là liên kết dẫn đến bộ định tuyến B. Một gói chỉ có thể được truyền trên một liên kết nếu không có gói nào khác hiện đang được truyền trên liên kết và nếu không có gói nào khác trước nó trong hàng đợi; nếu liên kết là

hiện đang bận hoặc nếu có các gói khác đã được xếp hàng cho liên kết thì gói mới đến sẽ tham gia vào hàng đợi.

Độ trễ xử lý

Thời gian cần thiết để kiểm tra tiêu đề của gói và xác định nơi chuyển gói đến là một phần của độ trễ xử lý. Độ trễ xử lý cũng có thể bao gồm các yếu tố khác, chẳng hạn như thời gian cần thiết để kiểm tra lỗi cấp độ bit trong gói xảy ra khi truyền các bit của gói từ nút ngược dòng đến bộ định tuyến A. Độ trễ xử lý trong bộ định tuyến tốc độ cao thường ở mức micro giây hoặc ít hơn. Sau quá trình xử lý nút này, bộ định tuyến sẽ chuyển gói đến hàng đợi trước liên kết đến bộ định tuyến B. (Trong Chương 4, chúng ta sẽ nghiên cứu chi tiết về cách hoạt động của bộ định tuyến.)

Trì hoãn xếp hàng

Tại hàng đợi, gói gặp phải độ trễ xếp hàng khi nó chờ được truyền lên liên kết. Độ dài độ trễ xếp hàng của một gói cụ thể sẽ phụ thuộc vào số lượng gói đến trước đó đang được xếp hàng và chờ truyền lên liên kết. Nếu hàng đợi trống và không có gói nào khác hiện đang được truyền thì độ trễ xếp hàng của gói của chúng tôi sẽ bằng 0. Mặt khác, nếu lưu lượng lớn và nhiều gói khác cũng đang chờ để được truyền thì độ trễ xếp hàng sẽ kéo dài. Chúng ta sẽ sớm thấy rằng số lượng gói mà gói đến có thể mong đợi tìm thấy là một hàm của cường độ và tính chất của lưu lượng đến hàng đợi. Trong thực tế, độ trễ trong hàng đợi có thể ở mức từ micro giây đến mili giây.

Độ trễ truyền

Giả sử rằng các gói được truyền theo cách đến trước được phục vụ trước, như cách phổ biến trong các mạng chuyển mạch gói, gói của chúng ta chỉ có thể được truyền sau khi tất cả các gói đến trước khi nó được truyền đi. Biểu thị độ dài của

*Hình 1.16 ♦ Độ trễ nút tại bộ định tuyến A*

MỘT

B

Xử lý nút

Xếp hàng (chờ truyền)

Quá trình lây truyền

Tuyên truyền

gói bằng L bit và biểu thị tốc độ truyền của liên kết từ bộ định tuyến A đến bộ định tuyến B bằng R bit/giây. Ví dụ: đối với liên kết Ethernet 10 Mbps, tốc độ là R = 10 Mbps; đối với liên kết Ethernet 100 Mbps, tốc độ là R = 100 Mbps. Độ trễ truyền là L/R. Đây là lượng thời gian cần thiết để đẩy (nghĩa là truyền) tất cả các bit của gói vào liên kết. Trong thực tế, độ trễ truyền thường ở mức từ micro giây đến mili giây.

Độ trễ lan truyền

Khi một bit được đẩy vào liên kết, nó cần được truyền đến bộ định tuyến B. Thời gian cần thiết để truyền từ đầu liên kết đến bộ định tuyến B là độ trễ truyền. Bit lan truyền với tốc độ truyền của liên kết. Tốc độ lan truyền phụ thuộc vào môi trường vật lý của liên kết (nghĩa là cáp quang, dây đồng xoắn đôi, v.v.) và nằm trong phạm vi

**2 #108 mét/giây đến 3 #108 mét/giây**

bằng hoặc nhỏ hơn một chút so với tốc độ ánh sáng. Độ trễ truyền là khoảng cách giữa hai bộ định tuyến chia cho tốc độ truyền. Nghĩa là, độ trễ truyền là d/s, trong đó d là khoảng cách giữa bộ định tuyến A và bộ định tuyến B và s là tốc độ truyền của liên kết. Khi bit cuối cùng của gói truyền đến nút B, nó và tất cả các bit trước đó của gói sẽ được lưu trữ trong bộ định tuyến B. Toàn bộ quá trình sau đó tiếp tục với bộ định tuyến B hiện đang thực hiện chuyển tiếp. Trong các mạng diện rộng, độ trễ truyền sóng vào khoảng mili giây.

So sánh độ trễ truyền và lan truyền

Những người mới tham gia vào lĩnh vực mạng máy tính đôi khi gặp khó khăn trong việc hiểu sự khác biệt giữa độ trễ truyền và độ trễ lan truyền. Sự khác biệt là tinh tế nhưng quan trọng. Độ trễ truyền là khoảng thời gian cần thiết để bộ định tuyến đẩy gói tin ra ngoài; nó là hàm của độ dài gói và tốc độ truyền của liên kết, nhưng không liên quan gì đến khoảng cách giữa hai bộ định tuyến. Mặt khác, độ trễ lan truyền là thời gian cần một chút để truyền từ bộ định tuyến này sang bộ định tuyến tiếp theo; nó là một hàm của khoảng cách giữa hai bộ định tuyến, nhưng không liên quan gì đến độ dài gói tin hoặc tốc độ truyền của liên kết.

Một sự tương tự có thể làm rõ các khái niệm về độ trễ truyền và lan truyền. Hãy xem xét một đường cao tốc có trạm thu phí cứ sau 100 km, như trong Hình 1.17. Bạn có thể coi các đoạn đường cao tốc giữa các trạm thu phí là các đường liên kết và các trạm thu phí là các bộ định tuyến. Giả sử ô tô di chuyển (nghĩa là lan truyền) trên đường cao tốc với tốc độ 100 km/giờ (nghĩa là khi một ô tô rời khỏi trạm thu phí, nó ngay lập tức tăng tốc lên 100 km/giờ và duy trì tốc độ đó giữa các trạm thu phí). Tiếp theo, giả sử có 10 ô tô đi cùng nhau như một đoàn lữ hành, nối tiếp nhau theo một thứ tự cố định. Bạn có thể coi mỗi chiếc ô tô là một mảnh nhỏ và đoàn lữ hành là một gói hàng. Cũng giả sử rằng mỗi

VideoNote Khám phá độ trễ lan truyền và độ trễ truyền

dịch vụ trạm thu phí (nghĩa là truyền) một ô tô với tốc độ một ô tô trong 12 giây và trời đã khuya nên ô tô của đoàn lữ hành là những ô tô duy nhất trên đường cao tốc. Cuối cùng, giả sử rằng bất cứ khi nào chiếc xe đầu tiên của đoàn lữ hành đến trạm thu phí, nó sẽ đợi ở lối vào cho đến khi chín chiếc xe còn lại đến và xếp hàng phía sau. (Do đó, toàn bộ đoàn xe phải được lưu giữ tại trạm thu phí trước khi bắt đầu được chuyển tiếp.) Thời gian cần thiết để trạm thu phí đẩy toàn bộ đoàn xe lên đường cao tốc là (10 ô tô)/(5 ô tô/phút) = 2 phút. Thời gian này tương tự như độ trễ truyền trong bộ định tuyến. Thời gian cần thiết để một ô tô đi từ lối ra của trạm thu phí này đến trạm thu phí tiếp theo là 100 km/(100 km/giờ) = 1 giờ. Thời gian này tương tự như độ trễ lan truyền. Do đó, thời gian từ khi đoàn xe được lưu trước trạm thu phí cho đến khi đoàn lữ hành được lưu trước trạm thu phí tiếp theo là tổng độ trễ truyền và độ trễ lan truyền---trong ví dụ này là 62 phút.

Hãy khám phá sự tương tự này nhiều hơn một chút. Điều gì sẽ xảy ra nếu thời gian phục vụ trạm thu phí cho một đoàn lữ hành lớn hơn thời gian để ô tô di chuyển giữa các trạm thu phí? Ví dụ, bây giờ giả sử ô tô di chuyển với tốc độ 1.000 km/giờ và trạm thu phí phục vụ ô tô với tốc độ một ô tô mỗi phút. Khi đó thời gian trễ di chuyển giữa hai trạm thu phí là 6 phút và thời gian phục vụ một đoàn lữ hành là 10 phút. Trong trường hợp này, một số ô tô đầu tiên trong đoàn sẽ đến trạm thu phí thứ hai trước khi những ô tô cuối cùng trong đoàn rời khỏi trạm thu phí đầu tiên. Tình huống này cũng xảy ra trong các mạng chuyển mạch gói---các bit đầu tiên trong gói có thể đến bộ định tuyến trong khi nhiều bit còn lại trong gói vẫn đang chờ được bộ định tuyến trước truyền đi.

Nếu một bức tranh nói được cả ngàn lời thì một hình ảnh động cũng phải nói được một triệu lời nói. Trang web của cuốn sách giáo khoa này cung cấp một hình ảnh động tương tác minh họa độc đáo và tương phản độ trễ truyền và độ trễ lan truyền. Người đọc rất được khuyến khích đến thăm hoạt hình đó. \[Smith 2009\] cũng cung cấp một cuộc thảo luận rất dễ hiểu về sự lan truyền, xếp hàng và độ trễ truyền tải.

Nếu chúng ta đặt dproc, dqueue, dtrans và dprop biểu thị độ trễ xử lý, xếp hàng, truyền và lan truyền, thì tổng độ trễ nút được tính bằng

dnodal = dproc + dqueue + dtrans + dprop

Sự đóng góp của các thành phần trễ này có thể thay đổi đáng kể. Ví dụ: dprop có thể không đáng kể (ví dụ: vài micro giây) đối với một liên kết kết nối hai bộ định tuyến trong cùng một khuôn viên trường đại học; tuy nhiên, dprop là hàng trăm mili giây đối với hai bộ định tuyến được kết nối với nhau bằng liên kết vệ tinh địa tĩnh và có thể là

*Hình 1.17 ♦ Tương tự đoàn lữ hành*

Đoàn lữ hành mười xe

Trạm thu phí

Trạm thu phí

100 km 100 km

thuật ngữ chiếm ưu thế trong dnodal. Tương tự, dtrans có thể dao động từ không đáng kể đến đáng kể. Đóng góp của nó thường không đáng kể đối với tốc độ truyền từ 10 Mbps trở lên (ví dụ: đối với mạng LAN); tuy nhiên, có thể mất hàng trăm mili giây đối với các gói Internet lớn được gửi qua liên kết modem quay số tốc độ thấp. Độ trễ xử lý, dproc, thường không đáng kể; tuy nhiên, nó ảnh hưởng mạnh mẽ đến thông lượng tối đa của bộ định tuyến, là tốc độ tối đa mà bộ định tuyến có thể chuyển tiếp gói tin.

**1.4.2 Trì hoãn hàng đợi và mất Packet**

Thành phần phức tạp và thú vị nhất của độ trễ nút là độ trễ hàng đợi, dqueue. Trên thực tế, độ trễ trong hàng đợi rất quan trọng và thú vị trong mạng máy tính đến nỗi hàng ngàn bài báo và nhiều cuốn sách đã viết về nó \[Bertsekas 1991; Kleinrock 1975, Kleinrock 1976\]. Ở đây chúng tôi chỉ đưa ra một cuộc thảo luận trực quan, cấp cao về độ trễ trong hàng đợi; người đọc tò mò hơn có thể muốn xem qua một số cuốn sách (hoặc thậm chí viết luận án tiến sĩ về chủ đề này!). Không giống như ba độ trễ còn lại (cụ thể là dproc, dtrans và dprop), độ trễ xếp hàng có thể khác nhau tùy theo gói. Ví dụ: nếu 10 gói đến hàng đợi trống cùng một lúc, gói đầu tiên được truyền sẽ không bị trễ xếp hàng, trong khi gói cuối cùng được truyền sẽ chịu độ trễ xếp hàng tương đối lớn (trong khi nó chờ chín gói còn lại được truyền đi). Do đó, khi mô tả độ trễ xếp hàng, người ta thường sử dụng các thước đo thống kê, chẳng hạn như độ trễ xếp hàng trung bình, phương sai của độ trễ xếp hàng và xác suất độ trễ xếp hàng vượt quá một số giá trị được chỉ định.

Khi nào độ trễ xếp hàng lớn và khi nào nó không đáng kể? Câu trả lời cho câu hỏi này phụ thuộc vào tốc độ lưu lượng đến hàng đợi, tốc độ truyền của liên kết và bản chất của lưu lượng đến, nghĩa là lưu lượng đến theo chu kỳ hay đến theo đợt. Để hiểu rõ hơn ở đây, hãy biểu thị tốc độ trung bình mà các gói đến hàng đợi (a tính bằng đơn vị gói/giây). Hãy nhớ lại rằng R là tốc độ truyền tải; nghĩa là, đó là tốc độ (tính bằng bit/giây) mà tại đó các bit được đẩy ra khỏi hàng đợi. Cũng giả sử, để đơn giản, tất cả các gói đều bao gồm L bit. Khi đó tốc độ trung bình mà các bit đến hàng đợi là La bit/giây. Cuối cùng, giả sử rằng hàng đợi rất lớn, do đó về cơ bản nó có thể chứa vô số bit. Tỷ lệ La/R, được gọi là cường độ lưu lượng, thường đóng vai trò quan trọng trong việc ước tính mức độ trễ của hàng đợi. Nếu La/R \> 1 thì tốc độ trung bình mà các bit đến hàng đợi sẽ vượt quá tốc độ mà các bit có thể được truyền từ hàng đợi. Trong tình huống không may này, hàng đợi sẽ có xu hướng tăng lên không giới hạn và độ trễ của hàng đợi sẽ tiến tới vô cùng! Vì vậy, một trong những nguyên tắc vàng trong kỹ thuật giao thông là: Thiết kế hệ thống của bạn sao cho cường độ giao thông không lớn hơn 1.

Bây giờ hãy xem xét trường hợp La/R ≤ 1. Ở đây, bản chất của lưu lượng truy cập đến ảnh hưởng đến độ trễ xếp hàng. Ví dụ: nếu các gói đến định kỳ---tức là, cứ mỗi giây L/R lại có một gói đến---khi đó mọi gói sẽ đến hàng đợi trống và sẽ không có độ trễ xếp hàng. Mặt khác, nếu các gói đến theo từng đợt nhưng định kỳ thì có thể có độ trễ xếp hàng trung bình đáng kể. Ví dụ: giả sử N gói đến đồng thời sau mỗi (L/R)N giây. Khi đó gói đầu tiên được truyền không có độ trễ xếp hàng; gói thứ hai được truyền có độ trễ xếp hàng

của L/R giây; và tổng quát hơn, gói thứ n được truyền có độ trễ xếp hàng là (n - 1)L/R giây. Chúng tôi coi đây là bài tập để bạn tính toán độ trễ xếp hàng trung bình trong ví dụ này.

Hai ví dụ về sự xuất hiện định kỳ được mô tả ở trên mang tính học thuật một chút. Thông thường, quá trình đến hàng đợi là ngẫu nhiên; nghĩa là, các gói đến không theo bất kỳ mẫu nào và các gói được đặt cách nhau một khoảng thời gian ngẫu nhiên. Trong trường hợp thực tế hơn này, đại lượng La/R thường không đủ để mô tả đầy đủ số liệu thống kê độ trễ xếp hàng. Tuy nhiên, nó rất hữu ích trong việc đạt được sự hiểu biết trực quan về mức độ trễ của hàng đợi. Đặc biệt, nếu cường độ lưu lượng gần bằng 0 thì các gói đến sẽ rất ít và xa nhau và không chắc gói đến sẽ tìm thấy gói khác trong hàng đợi. Do đó, độ trễ xếp hàng trung bình sẽ gần bằng 0. Mặt khác, khi cường độ lưu lượng gần bằng 1, sẽ có những khoảng thời gian tốc độ đến vượt quá khả năng truyền tải (do sự thay đổi về tốc độ đến của gói) và hàng đợi sẽ hình thành trong những khoảng thời gian này; khi tốc độ đến nhỏ hơn khả năng truyền tải thì độ dài của hàng đợi sẽ co lại. Tuy nhiên, khi cường độ lưu lượng tiến tới 1, chiều dài hàng đợi trung bình sẽ ngày càng lớn hơn. Sự phụ thuộc định tính của độ trễ xếp hàng trung bình vào cường độ giao thông được thể hiện trong Hình 1.18.

Một khía cạnh quan trọng của Hình 1.18 là thực tế là khi cường độ lưu lượng tiến tới 1, độ trễ xếp hàng trung bình tăng nhanh. Cường độ tăng một phần trăm nhỏ sẽ dẫn đến độ trễ tăng theo phần trăm lớn hơn nhiều. Có lẽ bạn đã từng gặp hiện tượng này trên đường cao tốc. Nếu bạn thường xuyên lái xe trên một con đường thường bị tắc nghẽn thì việc con đường đó thường bị tắc nghẽn có nghĩa là cường độ giao thông của nó gần bằng 1. Nếu một sự kiện nào đó gây ra lưu lượng giao thông thậm chí lớn hơn một chút so với bình thường thì độ trễ mà bạn gặp phải có thể rất lớn.

Để thực sự hiểu rõ ý nghĩa của việc trì hoãn xếp hàng, bạn nên truy cập lại trang Web sách giáo khoa một lần nữa, nơi cung cấp hình ảnh động tương tác về hàng đợi. Nếu bạn đặt tốc độ đến của gói đủ cao để cường độ lưu lượng vượt quá 1, bạn sẽ thấy hàng đợi tăng dần theo thời gian.

*Hình 1.18 ♦ Sự phụ thuộc của độ trễ xếp hàng trung bình vào cường độ giao thông*

Độ trễ xếp hàng trung bình

La/R

Packet Thua

Trong các cuộc thảo luận ở trên, chúng tôi đã giả định rằng hàng đợi có khả năng chứa vô số gói. Trong thực tế, hàng đợi trước một liên kết có dung lượng hữu hạn, mặc dù dung lượng hàng đợi phụ thuộc rất nhiều vào thiết kế và chi phí của bộ định tuyến. Bởi vì dung lượng hàng đợi là hữu hạn nên độ trễ gói không thực sự đạt tới mức vô cùng khi cường độ lưu lượng tiến tới 1. Thay vào đó, một gói có thể đến để tìm thấy một hàng đợi đầy đủ. Không có nơi nào để lưu trữ gói như vậy, bộ định tuyến sẽ loại bỏ gói đó; tức là gói tin sẽ bị mất. Sự tràn này tại hàng đợi một lần nữa có thể được nhìn thấy trong hoạt ảnh tương tác khi cường độ lưu lượng truy cập lớn hơn 1.

Từ quan điểm của hệ thống cuối, việc mất gói sẽ giống như một gói được truyền vào lõi mạng nhưng không bao giờ thoát ra khỏi mạng tại đích. Tỷ lệ gói bị mất tăng lên khi cường độ lưu lượng tăng. Do đó, hiệu suất tại một nút thường được đo không chỉ về độ trễ mà còn về khả năng mất gói. Như chúng ta sẽ thảo luận trong các chương tiếp theo, một gói bị mất có thể được truyền lại trên cơ sở end-to-end để đảm bảo rằng tất cả dữ liệu cuối cùng sẽ được truyền từ nguồn tới đích.

**1.4.3 Độ trễ từ đầu đến cuối**

Cuộc thảo luận của chúng ta cho đến thời điểm này đã tập trung vào độ trễ nút, nghĩa là độ trễ tại một bộ định tuyến. Bây giờ chúng ta hãy xem xét tổng độ trễ từ nguồn đến đích. Để hiểu được khái niệm này, giả sử có N - 1 bộ định tuyến giữa máy chủ nguồn và máy chủ đích. Chúng ta cũng hãy giả sử rằng mạng không bị tắc nghẽn (do đó độ trễ xếp hàng là không đáng kể), độ trễ xử lý tại mỗi bộ định tuyến và tại máy chủ nguồn là dproc, tốc độ truyền ra khỏi mỗi bộ định tuyến và ra khỏi máy chủ nguồn là R bit/giây và tốc độ truyền trên mỗi liên kết là dprop. Độ trễ nút tích lũy và tạo ra độ trễ từ đầu đến cuối,

dend-end = N (dproc + dtrans + dprop) (1.2)

trong đó, một lần nữa, dtrans = L/R, trong đó L là kích thước gói. Lưu ý rằng Công thức 1.2 là sự tổng quát hóa của Công thức 1.1, không tính đến độ trễ xử lý và lan truyền. Chúng tôi để bạn khái quát hóa phương trình 1.2 cho trường hợp độ trễ không đồng nhất tại các nút và sự hiện diện của độ trễ xếp hàng trung bình tại mỗi nút.

Theo dõi lộ trình

Để có được cảm giác thực tế về độ trễ đầu cuối trong mạng máy tính, chúng ta có thể sử dụng chương trình Traceroute. Traceroute là một chương trình đơn giản có thể chạy trên bất kỳ máy chủ Internet nào. Khi người dùng chỉ định tên máy chủ đích, chương trình trong máy chủ nguồn sẽ gửi nhiều gói đặc biệt tới đích đó. Khi các gói này di chuyển đến đích, chúng sẽ đi qua một loạt bộ định tuyến. Khi bộ định tuyến nhận được một trong những gói đặc biệt này, nó sẽ gửi lại nguồn một tin nhắn ngắn chứa tên và địa chỉ của bộ định tuyến.

VideoNote Sử dụng Traceroute để khám phá đường dẫn mạng và đo độ trễ mạng

Cụ thể hơn, giả sử có N - 1 bộ định tuyến giữa nguồn và đích. Sau đó, nguồn sẽ gửi N gói đặc biệt vào mạng, mỗi gói được gửi đến đích cuối cùng. N gói đặc biệt này được đánh dấu từ 1 đến N, với gói đầu tiên được đánh dấu 1 và gói cuối cùng được đánh dấu N. Khi bộ định tuyến thứ n nhận được gói thứ n được đánh dấu n, bộ định tuyến không chuyển tiếp gói đến đích mà thay vào đó gửi một tin nhắn trở lại nguồn. Khi máy đích nhận được gói thứ N, nó cũng trả về một tin nhắn cho nguồn. Nguồn ghi lại khoảng thời gian trôi qua kể từ khi nó gửi một gói đến khi nhận được thông báo phản hồi tương ứng; nó cũng ghi lại tên và địa chỉ của bộ định tuyến (hoặc máy chủ đích) trả về tin nhắn. Theo cách này, nguồn có thể xây dựng lại tuyến đường được thực hiện bởi các gói truyền từ nguồn đến đích và nguồn có thể xác định độ trễ khứ hồi tới tất cả các bộ định tuyến can thiệp. Traceroute thực sự lặp lại thí nghiệm vừa mô tả ba lần, do đó nguồn thực sự gửi 3 • N gói đến đích. RFC 1393 mô tả chi tiết Traceroute.

Dưới đây là ví dụ về đầu ra của chương trình Traceroute, trong đó tuyến đường được truy tìm từ máy chủ nguồn gaia.cs.umass.edu (tại Đại học Massachusetts) đến máy chủ trong khoa khoa học máy tính tại Đại học Sorbonne ở Paris (trước đây trường đại học này được gọi là UPMC). Đầu ra có sáu cột: cột đầu tiên là giá trị n được mô tả ở trên, tức là số lượng bộ định tuyến dọc theo tuyến đường; cột thứ hai là tên của bộ định tuyến; cột thứ ba là địa chỉ của bộ định tuyến (có dạng xxx.xxx.xxx.xxx); ba cột cuối cùng là độ trễ khứ hồi của ba thử nghiệm. Nếu nguồn nhận được ít hơn ba tin nhắn từ bất kỳ bộ định tuyến cụ thể nào (do mất gói trong mạng), Traceroute sẽ đặt dấu hoa thị ngay sau số bộ định tuyến và báo cáo ít hơn ba lần khứ hồi cho bộ định tuyến đó.

1 gw-vlan-2451.cs.umass.edu (128.119.245.1) 1,899 ms 3,266 ms 3,280 ms 2 j-cs-gw-int-10-240.cs.umass.edu (10.119.240.254) 1,296 ms 1,276 ms 1,245 ms 3 n5-rt-1-1-xe-2-1-0.gw.umass.edu (128.119.3.33) 2,237 ms 2,217 ms 2,187 ms 4 core1-rt-et-5-2-0.gw.umass.edu (128.119.0.9) 0,351 ms 0,392 ms 0,380 ms 5 border1-rt-et-5-0-0.gw.umass.edu (192.80.83.102) 0,345 ms 0,345 ms 0,344 ms 6 nox300gw1-umass-re.nox.org (192.5.89.101) 3,260 ms 0,416 ms 3,127 ms 7 nox300gw1-umass-re.nox.org (192.5.89.101) 3,165 ms 7,326 ms 7,311 ms 8 198,71.45.237 (198,71.45.237) 77,826 ms 77,246 ms 77,744 ms 9 renater-lb1-gw.mx1.par.fr.geant.net (62.40.124.70) 79.357 ms 77.729 79.152 ms 10 193.51.180.109 (193.51.180.109) 78.379 ms 79.936 80,042 mili giây 11 \* 193.51.180.109 (193.51.180.109) 80.640 mili giây \* 12 \* 195.221.127.182 (195.221.127.182) 78.408 mili giây \* 13 195.221.127.182 (195.221.127.182) 80.686 ms 80.796 ms 78.434 ms 14 r-upmc1.reseau.jussieu.fr (134.157.254.10) 78.399 ms \* 81.353 ms

Trong hình trên, có 14 bộ định tuyến giữa nguồn và đích. Hầu hết các bộ định tuyến này đều có tên và tất cả chúng đều có địa chỉ. Ví dụ: tên của Router 4 là core1-rt-et-5-2-0.gw.umass.edu và địa chỉ của nó là 128.119.0.9. Nhìn vào dữ liệu được cung cấp cho cùng bộ định tuyến này, chúng ta thấy rằng trong thử nghiệm đầu tiên trong số ba thử nghiệm, độ trễ truyền đi giữa nguồn và bộ định tuyến là 0,351 mili giây. Độ trễ khứ hồi cho hai thử nghiệm tiếp theo là 0,392 và 0,380 mili giây. Các độ trễ khứ hồi này bao gồm tất cả các độ trễ vừa được thảo luận, bao gồm độ trễ truyền, độ trễ lan truyền, độ trễ xử lý bộ định tuyến và độ trễ hàng đợi.

Vì độ trễ trong hàng đợi thay đổi theo thời gian nên độ trễ khứ hồi của gói n gửi đến bộ định tuyến n đôi khi có thể dài hơn độ trễ khứ hồi của gói n+1 gửi đến bộ định tuyến n+1. Thật vậy, chúng ta quan sát thấy hiện tượng này trong ví dụ trên: độ trễ đối với Router 12 nhỏ hơn độ trễ đối với Router 11! Cũng lưu ý rằng độ trễ khứ hồi tăng lên đáng kể khi đi từ bộ định tuyến 7 đến bộ định tuyến 8. Điều này là do liên kết cáp quang xuyên Đại Tây Dương giữa bộ định tuyến 7 và 8, dẫn đến độ trễ truyền tương đối lớn. Có một số chương trình phần mềm miễn phí cung cấp giao diện đồ họa cho Traceroute; một trong những mục yêu thích của chúng tôi là PingPlotter \[PingPlotter 2020\].

End System, Đơn đăng ký và các sự chậm trễ khác

Ngoài độ trễ xử lý, truyền tải và lan truyền, có thể có thêm độ trễ đáng kể trong hệ thống cuối. Ví dụ: hệ thống cuối muốn truyền gói vào phương tiện dùng chung (ví dụ: như trong trường hợp WiFi hoặc modem cáp) có thể cố tình trì hoãn việc truyền gói như một phần của giao thức chia sẻ phương tiện với các hệ thống đầu cuối khác; Chúng ta sẽ xem xét chi tiết các giao thức như vậy trong Chương 6. Một độ trễ quan trọng khác là độ trễ đóng gói phương tiện, hiện diện trong các ứng dụng Voiceover-IP (VoIP). Trong VoIP, trước tiên bên gửi phải điền vào gói bằng giọng nói được số hóa được mã hóa trước khi chuyển gói tới Internet. Thời gian này để lấp đầy một gói---được gọi là độ trễ đóng gói---có thể rất quan trọng và có thể ảnh hưởng đến chất lượng cảm nhận của người dùng về cuộc gọi VoIP. Vấn đề này sẽ được khám phá sâu hơn trong bài tập về nhà ở cuối chương này.

**1.4.4 Throughput trong Mạng máy tính**

Ngoài độ trễ và mất gói, một thước đo hiệu suất quan trọng khác trong mạng máy tính là thông lượng đầu cuối. Để xác định thông lượng, hãy xem xét chuyển một tệp lớn từ Host A sang Host B qua mạng máy tính. Ví dụ: việc truyền này có thể là một video clip lớn từ máy tính này sang máy tính khác. Thông lượng tức thời tại bất kỳ thời điểm nào là tốc độ (tính bằng bit/giây) mà Host B đang nhận tệp. (Nhiều ứng dụng hiển thị thông lượng tức thời trong quá trình tải xuống trong giao diện người dùng---có lẽ bạn đã quan sát thấy điều này trước đây! Bạn có thể muốn thử

đo độ trễ từ đầu đến cuối và thông lượng tải xuống giữa bạn và các máy chủ trên Internet bằng ứng dụng speedtest \[Speedtest 2020\].) Nếu tệp bao gồm F bit và quá trình truyền mất T giây để Host B nhận tất cả các bit F, thì thông lượng trung bình của quá trình truyền tệp là F/T bit/giây. Đối với một số ứng dụng, chẳng hạn như điện thoại Internet, mong muốn có độ trễ thấp và thông lượng tức thời luôn vượt quá ngưỡng nào đó (ví dụ: trên 24 kbps đối với một số ứng dụng điện thoại Internet và trên 256 kbps đối với một số ứng dụng video thời gian thực). Đối với các ứng dụng khác, kể cả những ứng dụng liên quan đến truyền tập tin, độ trễ không quan trọng nhưng cần có thông lượng cao nhất có thể.

Để hiểu rõ hơn về khái niệm quan trọng của thông lượng, hãy xem xét một vài ví dụ. Hình 1.19(a) hiển thị hai hệ thống đầu cuối, một máy chủ và một máy khách, được kết nối bằng hai liên kết truyền thông và một bộ định tuyến. Hãy xem xét thông lượng truyền tệp từ máy chủ đến máy khách. Đặt Rs biểu thị tốc độ liên kết giữa máy chủ và bộ định tuyến; và Rc biểu thị tốc độ liên kết giữa bộ định tuyến và máy khách. Giả sử rằng các bit duy nhất được gửi trong toàn bộ mạng là các bit từ máy chủ đến máy khách. Bây giờ chúng tôi hỏi, trong kịch bản lý tưởng này, thông lượng máy chủ đến máy khách là bao nhiêu? Để trả lời câu hỏi này, chúng ta có thể coi bit là chất lỏng và các liên kết truyền thông là đường ống. Rõ ràng, máy chủ không thể bơm bit qua liên kết của nó với tốc độ nhanh hơn Rs bps; và bộ định tuyến không thể chuyển tiếp bit với tốc độ nhanh hơn Rc bps. Nếu là 6 Rs Rc thì các bit được máy chủ bơm sẽ "chảy" ngay qua bộ định tuyến và đến máy khách với tốc độ Rs bps, cho thông lượng là Rs bps. Mặt khác, nếu Rc 6 Rs thì bộ định tuyến sẽ không thể chuyển tiếp các bit nhanh như khi nhận được chúng. Trong trường hợp này, các bit sẽ chỉ rời khỏi bộ định tuyến ở tốc độ Rc, mang lại thông lượng từ đầu đến cuối là Rc. (Cũng lưu ý rằng nếu các bit tiếp tục đến bộ định tuyến với tốc độ Rs và tiếp tục rời khỏi bộ định tuyến ở Rc, thì lượng bit tồn đọng tại bộ định tuyến đang chờ truyền đến máy khách sẽ ngày càng tăng---một tình huống không mong muốn nhất!)

*Hình 1.19 ♦ Throughput để truyền tệp từ máy chủ đến máy khách*

Máy chủ

Rs

R1 R2 RN

Rc

Khách hàng

Máy chủ

Một.

b\.

Khách hàng

Do đó, đối với mạng hai liên kết đơn giản này, thông lượng là min{Rc, Rs}, tức là tốc độ truyền của liên kết thắt cổ chai. Sau khi đã xác định được thông lượng, giờ đây chúng ta có thể ước tính thời gian cần thiết để truyền một tệp lớn F bit từ máy chủ đến máy khách dưới dạng F/min{Rs, Rc}. Trong một ví dụ cụ thể, giả sử bạn đang tải xuống tệp MP3 có F = 32 triệu bit, máy chủ có tốc độ truyền Rs = 2 Mbps và bạn có liên kết truy cập Rc = 1 Mbps. Thời gian cần thiết để chuyển tập tin là 32 giây. Tất nhiên, những biểu thức này về thông lượng và thời gian truyền chỉ là xấp xỉ vì chúng không tính đến độ trễ lưu trữ và chuyển tiếp và xử lý cũng như các vấn đề về giao thức.

Hình 1.19(b) hiện hiển thị một mạng có N liên kết giữa máy chủ và máy khách, với tốc độ truyền của N liên kết là R1, R2, c, RN. Áp dụng phân tích tương tự như đối với mạng hai liên kết, chúng tôi thấy rằng thông lượng truyền tệp từ máy chủ đến máy khách là min{R1, R2, c, RN}, một lần nữa là tốc độ truyền của liên kết thắt cổ chai dọc theo đường dẫn giữa máy chủ và máy khách.

Bây giờ hãy xem xét một ví dụ khác được thúc đẩy bởi Internet ngày nay. Hình 1.20(a) cho thấy hai hệ thống đầu cuối, một máy chủ và một máy khách, được kết nối với mạng máy tính. Hãy xem xét thông lượng truyền tệp từ máy chủ đến máy khách. Máy chủ được kết nối với mạng bằng liên kết truy cập tốc độ Rs và máy khách được kết nối với mạng bằng liên kết truy cập tốc độ Rc. Bây giờ giả sử rằng tất cả các liên kết trong lõi của mạng truyền thông đều có tốc độ truyền rất cao, cao hơn nhiều so với Rs và Rc. Quả thực, ngày nay, cốt lõi của Internet được cung cấp quá nhiều đường truyền tốc độ cao nên ít bị tắc nghẽn. Cũng giả sử rằng các bit duy nhất được gửi trong toàn bộ mạng là các bit từ máy chủ đến máy khách. Bởi vì lõi của mạng máy tính giống như một đường ống rộng trong ví dụ này, tốc độ bit có thể truyền từ nguồn tới đích lại là mức tối thiểu là Rs và Rc, nghĩa là thông lượng = min{Rs, Rc}. Do đó, yếu tố hạn chế về thông lượng trên Internet ngày nay thường là mạng truy cập.

Ví dụ cuối cùng, hãy xem Hình 1.20(b) trong đó có 10 máy chủ và 10 máy khách được kết nối với lõi của mạng máy tính. Trong ví dụ này, có 10 lượt tải xuống đồng thời diễn ra, bao gồm 10 cặp máy khách-máy chủ. Giả sử rằng 10 lượt tải xuống này là lưu lượng truy cập duy nhất trên mạng ở thời điểm hiện tại. Như được hiển thị trong hình, có một liên kết trong lõi được tất cả 10 lượt tải xuống đi qua. Ký hiệu R cho tốc độ truyền của liên kết này R. Giả sử rằng tất cả các liên kết truy cập máy chủ có cùng tốc độ Rs, tất cả các liên kết truy cập máy khách có cùng tốc độ Rc và tốc độ truyền của tất cả các liên kết trong lõi---ngoại trừ một liên kết chung có tốc độ R---lớn hơn nhiều so với Rs, Rc và R. Bây giờ chúng ta hỏi, thông lượng tải xuống là bao nhiêu? Rõ ràng, nếu tốc độ của liên kết chung, R, lớn---chẳng hạn như lớn hơn cả Rs và Rc một trăm lần---thì thông lượng cho mỗi lần tải xuống một lần nữa sẽ là min{Rs, Rc}. Nhưng nếu tốc độ của liên kết chung có cùng thứ tự với R và Rc thì sao? Thông lượng sẽ là bao nhiêu trong trường hợp này? Chúng ta hãy xem một ví dụ cụ thể. Giả sử Rs = 2 Mbps, Rc = 1 Mbps, R = 5 Mbps và liên kết chung chia đều tốc độ truyền của nó cho 10 lượt tải xuống. Sau đó

Nút thắt cổ chai cho mỗi lần tải xuống không còn nằm trong mạng truy cập mà thay vào đó là liên kết được chia sẻ trong lõi, chỉ cung cấp cho mỗi lần tải xuống thông lượng 500 kbps. Do đó, thông lượng đầu cuối cho mỗi lần tải xuống hiện giảm xuống còn 500 kbps. Các ví dụ trong Hình 1.19 và Hình 1.20(a) cho thấy thông lượng phụ thuộc vào tốc độ truyền của các liên kết mà dữ liệu chảy qua. Chúng ta đã thấy rằng khi không có lưu lượng nào khác can thiệp vào, thông lượng có thể chỉ xấp xỉ bằng tốc độ truyền tối thiểu dọc theo đường dẫn giữa nguồn và đích. Ví dụ trong Hình 1.20(b) cho thấy rằng thông lượng nói chung không chỉ phụ thuộc vào tốc độ truyền của các liên kết dọc theo đường dẫn mà còn phụ thuộc vào lưu lượng can thiệp. Đặc biệt, một liên kết có tốc độ truyền cao tuy nhiên có thể là liên kết thắt cổ chai cho việc truyền tệp nếu nhiều luồng dữ liệu khác cũng đi qua liên kết đó. Chúng ta sẽ xem xét thông lượng trong mạng máy tính chặt chẽ hơn trong các bài tập về nhà và trong các chương tiếp theo.

*Hình 1.20 ♦ Thông lượng từ đầu đến cuối: (a) Máy khách tải xuống một tệp từ*

máy chủ; (b) 10 client tải về từ 10 server

Máy chủ

Rs

Rc

Một. b.

Khách hàng 10 Khách hàng

10 máy chủ

Liên kết cổ chai công suất R

**1.5 Lớp giao thức và mô hình dịch vụ của chúng**

Từ cuộc thảo luận của chúng ta cho đến nay, rõ ràng Internet là một hệ thống cực kỳ phức tạp. Chúng ta đã thấy rằng Internet có rất nhiều phần: nhiều ứng dụng và giao thức, nhiều loại hệ thống đầu cuối, các chuyển mạch gói và nhiều loại phương tiện cấp liên kết khác nhau. Với sự phức tạp to lớn này, liệu có hy vọng nào về việc tổ chức một kiến ​​trúc mạng hay ít nhất là cuộc thảo luận của chúng ta về kiến ​​trúc mạng không? May mắn thay, câu trả lời cho cả hai câu hỏi là có.

**1.5.1 Kiến trúc lớp**

Trước khi cố gắng sắp xếp những suy nghĩ của chúng ta về kiến ​​trúc Internet, chúng ta hãy tìm kiếm sự tương tự với con người. Trên thực tế, chúng ta luôn phải đối mặt với những hệ thống phức tạp trong cuộc sống hàng ngày. Hãy tưởng tượng nếu ai đó yêu cầu bạn mô tả, ví dụ, hệ thống hàng không. Bạn sẽ tìm thấy cấu trúc như thế nào để mô tả hệ thống phức tạp này bao gồm các đại lý bán vé, nhân viên kiểm tra hành lý, nhân viên cổng, phi công, máy bay, kiểm soát không lưu và hệ thống định tuyến máy bay trên toàn thế giới? Một cách để mô tả hệ thống này có thể là mô tả chuỗi hành động bạn thực hiện (hoặc người khác thực hiện thay bạn) khi bạn bay trên một hãng hàng không. Bạn mua vé, kiểm tra hành lý, đi đến cổng và cuối cùng được đưa lên máy bay. Máy bay cất cánh và được định tuyến đến đích. Sau khi máy bay hạ cánh, bạn xuống máy bay ở cổng và nhận hành lý. Nếu chuyến đi tồi tệ, bạn phàn nàn về chuyến bay với đại lý bán vé (chẳng nhận được gì cho nỗ lực của mình). Kịch bản này được thể hiện trong Hình 1.21.

*Hình 1.21 ♦ Đi máy bay: hành động*

Vé (mua)

Hành lý (ký gửi)

Cổng (tải)

Đường băng cất cánh

Định tuyến máy bay

Vé (khiếu nại)

Hành lý (yêu cầu)

Cổng (dỡ hàng)

Đường băng hạ cánh

Định tuyến máy bay

Định tuyến máy bay

Ở đây, chúng ta có thể thấy một số điểm tương đồng với mạng máy tính: Bạn đang được hãng hàng không vận chuyển từ nguồn đến đích; một gói được chuyển từ máy chủ nguồn đến máy chủ đích trên Internet. Nhưng đây không hoàn toàn là sự tương tự mà chúng tôi đang theo đuổi. Chúng ta đang tìm kiếm một số cấu trúc trong Hình 1.21. Nhìn vào Hình 1.21, chúng tôi lưu ý rằng có chức năng bán vé ở mỗi đầu; Ngoài ra còn có chức năng hành lý dành cho hành khách đã có vé và chức năng cổng dành cho hành khách đã có vé và đã kiểm tra hành lý. Đối với hành khách đã qua cổng (tức là hành khách đã mua vé, kiểm tra hành lý và qua cổng) có chức năng cất cánh và hạ cánh, trong khi bay có chức năng định tuyến trên máy bay. Điều này gợi ý rằng chúng ta có thể xem xét chức năng trong Hình 1.21 theo chiều ngang, như trong Hình 1.22.

Hình 1.22 đã chia chức năng hàng không thành các lớp, cung cấp một khuôn khổ để chúng ta có thể thảo luận về việc đi lại bằng đường hàng không. Lưu ý rằng mỗi lớp, kết hợp với các lớp bên dưới nó, thực hiện một số chức năng, một số dịch vụ. Ở lớp bán vé trở xuống, việc chuyển một người từ quầy hàng không này sang quầy hàng không khác được thực hiện. Ở tầng hành lý trở xuống, việc chuyển người và hành lý từ ký gửi hành lý đến nhận hành lý được thực hiện. Lưu ý rằng hạng hành lý chỉ cung cấp dịch vụ này cho người đã có vé. Tại lớp cổng, việc chuyển người và hành lý từ cổng khởi hành đến cổng đến được thực hiện. Ở tầng cất cánh/hạ cánh, việc vận chuyển hành khách và hành lý của họ từ đường băng này sang đường băng khác được thực hiện. Mỗi lớp cung cấp dịch vụ của mình bằng cách (1) thực hiện một số hành động nhất định trong lớp đó (ví dụ: ở lớp cổng, bốc và dỡ người từ máy bay) và bằng (2) sử dụng các dịch vụ của lớp ngay bên dưới nó (ví dụ: trong lớp cổng, sử dụng dịch vụ vận chuyển hành khách từ đường băng đến đường băng của lớp cất cánh/hạ cánh).

Kiến trúc phân lớp cho phép chúng ta thảo luận về một phần cụ thể, được xác định rõ ràng của một hệ thống lớn và phức tạp. Bản thân sự đơn giản hóa này có giá trị đáng kể bằng cách cung cấp tính mô-đun, giúp việc thay đổi việc triển khai dịch vụ do lớp cung cấp trở nên dễ dàng hơn nhiều. Miễn là lớp cung cấp cùng một dịch vụ cho lớp bên trên nó và sử dụng cùng các dịch vụ từ lớp bên dưới nó, phần còn lại của hệ thống sẽ không thay đổi khi việc triển khai của lớp thay đổi. (Ghi chú

*Hình 1.22 ♦ Phân lớp chức năng hàng không theo chiều ngang*

Vé (mua)

Hành lý (ký gửi)

Cổng (tải)

Đường băng cất cánh

Định tuyến máy bay Định tuyến máy bay Định tuyến máy bay

Vé (khiếu nại)

Hành lý (yêu cầu)

Cổng (dỡ hàng)

Đường băng hạ cánh

Định tuyến máy bay

Vé

Hành lý

Cổng

Cất cánh/hạ cánh

Định tuyến máy bay

Sân bay đến Sân bay khởi hành Giao thông hàng không trung gian

trung tâm điều khiển

rằng việc thay đổi cách triển khai một dịch vụ rất khác với việc thay đổi chính dịch vụ đó!) Ví dụ: nếu chức năng của cổng bị thay đổi (ví dụ: để người lên và xuống theo độ cao), phần còn lại của hệ thống hàng không sẽ không thay đổi vì lớp cổng vẫn cung cấp chức năng tương tự (bốc xếp hành khách); nó chỉ đơn giản thực hiện chức năng đó theo một cách khác sau khi thay đổi. Đối với các hệ thống lớn và phức tạp được cập nhật liên tục, khả năng thay đổi cách triển khai dịch vụ mà không ảnh hưởng đến các thành phần khác của hệ thống là một ưu điểm quan trọng khác của việc phân lớp.

Phân lớp giao thức

Nhưng đủ về các hãng hàng không. Bây giờ chúng ta hãy chuyển sự chú ý của chúng ta sang các giao thức mạng. Để cung cấp cấu trúc cho việc thiết kế các giao thức mạng, các nhà thiết kế mạng tổ chức các giao thức---và phần cứng và phần mềm mạng triển khai các giao thức đó---theo các lớp. Mỗi giao thức thuộc về một trong các lớp, giống như mỗi chức năng trong kiến ​​trúc hàng không trong Hình 1.22 thuộc về một lớp. Một lần nữa chúng ta quan tâm đến các dịch vụ mà một lớp cung cấp cho lớp bên trên---được gọi là mô hình dịch vụ của một lớp. Giống như trong ví dụ về hãng hàng không của chúng tôi, mỗi lớp cung cấp dịch vụ của mình bằng cách (1) thực hiện một số hành động nhất định trong lớp đó và bằng cách (2) sử dụng các dịch vụ của lớp ngay bên dưới nó. Ví dụ, các dịch vụ được cung cấp bởi lớp n có thể bao gồm việc phân phối tin nhắn một cách đáng tin cậy từ biên này sang biên khác của mạng. Điều này có thể được thực hiện bằng cách sử dụng dịch vụ gửi tin nhắn cạnh-cạnh không đáng tin cậy của lớp n - 1 và thêm chức năng của lớp n để phát hiện và truyền lại các tin nhắn bị mất.

Một lớp giao thức có thể được triển khai trong phần mềm, phần cứng hoặc kết hợp cả hai. Các giao thức lớp ứng dụng---chẳng hạn như HTTP và SMTP---hầu như luôn được triển khai trong phần mềm của các hệ thống cuối; các giao thức tầng vận chuyển cũng vậy. Vì lớp vật lý và lớp liên kết dữ liệu chịu trách nhiệm xử lý giao tiếp qua một liên kết cụ thể nên chúng thường được triển khai trong thẻ giao diện mạng (ví dụ: thẻ giao diện Ethernet hoặc WiFi) được liên kết với một liên kết nhất định. Lớp mạng thường là sự triển khai hỗn hợp giữa phần cứng và phần mềm. Cũng lưu ý rằng giống như các chức năng trong kiến ​​trúc hàng không phân lớp được phân phối giữa các sân bay và trung tâm điều khiển chuyến bay khác nhau tạo nên hệ thống, giao thức lớp n cũng được phân bổ giữa các hệ thống cuối, chuyển mạch gói và các thành phần khác tạo nên mạng. Nghĩa là, thường có một phần của giao thức lớp n trong mỗi thành phần mạng này.

Phân lớp giao thức có lợi thế về mặt khái niệm và cấu trúc \[RFC 3439\]. Như chúng ta đã thấy, phân lớp cung cấp một cách có cấu trúc để thảo luận về các thành phần hệ thống. Tính mô-đun giúp cập nhật các thành phần hệ thống dễ dàng hơn. Tuy nhiên, chúng tôi đề cập rằng một số nhà nghiên cứu và kỹ sư mạng kịch liệt phản đối việc phân lớp \[Wakeman 1992\]. Một nhược điểm tiềm tàng của việc phân lớp là một lớp có thể trùng lặp chức năng của lớp thấp hơn. Ví dụ: nhiều ngăn xếp giao thức cung cấp khả năng phục hồi lỗi trên cơ sở mỗi liên kết và cơ sở từ đầu đến cuối. Hạn chế tiềm ẩn thứ hai là chức năng ở một lớp có thể cần thông tin (ví dụ: giá trị dấu thời gian) chỉ có ở lớp khác; điều này vi phạm mục tiêu tách các lớp.

Khi kết hợp với nhau, các giao thức của các lớp khác nhau được gọi là ngăn xếp giao thức. Ngăn xếp giao thức Internet bao gồm năm lớp: lớp vật lý, liên kết, mạng, vận chuyển và ứng dụng, như trong Hình 1.23. Nếu xem xét Mục lục, bạn sẽ thấy rằng chúng tôi đã sắp xếp cuốn sách này một cách đại khái bằng cách sử dụng các lớp của chồng giao thức Internet. Chúng tôi thực hiện cách tiếp cận từ trên xuống, đầu tiên bao phủ lớp ứng dụng và sau đó tiến dần xuống dưới.

Application Layer

Lớp ứng dụng là nơi chứa các ứng dụng mạng và các giao thức lớp ứng dụng của chúng. Lớp ứng dụng của Internet bao gồm nhiều giao thức, chẳng hạn như giao thức HTTP (cung cấp khả năng yêu cầu và truyền tài liệu Web), SMTP (cung cấp khả năng truyền các thông điệp e-mail) và FTP (cung cấp khả năng truyền tệp giữa hai hệ thống đầu cuối). Chúng ta sẽ thấy rằng một số chức năng mạng nhất định, chẳng hạn như dịch các tên thân thiện với con người cho các hệ thống cuối Internet như www.ietf.org sang địa chỉ mạng 32-bit, cũng được thực hiện với sự trợ giúp của giao thức lớp ứng dụng cụ thể, cụ thể là hệ thống tên miền (DNS). Chúng ta sẽ thấy trong Chương 2 rằng việc tạo và triển khai các giao thức lớp ứng dụng mới của riêng mình rất dễ dàng.

Giao thức lớp ứng dụng được phân phối trên nhiều hệ thống đầu cuối, với ứng dụng trong một hệ thống đầu cuối sử dụng giao thức để trao đổi các gói thông tin với ứng dụng trong hệ thống đầu cuối khác. Chúng tôi sẽ coi gói thông tin này ở lớp ứng dụng dưới dạng tin nhắn.

Transport Layer

Lớp vận chuyển của Internet vận chuyển các tin nhắn lớp ứng dụng giữa các điểm cuối ứng dụng. Trên Internet, có hai giao thức truyền tải, TCP và UDP, một trong hai giao thức này có thể truyền tải các tin nhắn lớp ứng dụng. TCP cung cấp dịch vụ hướng kết nối cho các ứng dụng của nó. Dịch vụ này bao gồm việc phân phối đảm bảo lớp ứng dụng

*Hình 1.23 ♦ Ngăn xếp giao thức Internet*

Chuyên chở

Ứng dụng

Mạng

liên kết

Thuộc vật chất

Năm lớp

ngăn xếp giao thức Internet

tin nhắn đến đích và điều khiển luồng (nghĩa là khớp tốc độ người gửi/người nhận). TCP cũng chia các tin nhắn dài thành các đoạn ngắn hơn và cung cấp cơ chế kiểm soát tắc nghẽn để nguồn điều chỉnh tốc độ truyền của nó khi mạng bị tắc nghẽn. Giao thức UDP cung cấp dịch vụ không kết nối cho các ứng dụng của nó. Đây là một dịch vụ đơn giản, không cung cấp độ tin cậy, không kiểm soát luồng và không kiểm soát tắc nghẽn. Trong cuốn sách này, chúng ta sẽ coi gói lớp vận chuyển là một phân đoạn.

Network Layer

Lớp mạng của Internet chịu trách nhiệm di chuyển các gói lớp mạng được gọi là datagram từ máy chủ này sang máy chủ khác. Giao thức lớp vận chuyển Internet (TCP hoặc UDP) trong máy chủ nguồn chuyển một phân đoạn lớp vận chuyển và địa chỉ đích đến lớp mạng, giống như cách bạn gửi cho dịch vụ bưu chính một lá thư có địa chỉ đích. Sau đó, lớp mạng cung cấp dịch vụ phân phối phân đoạn đến lớp vận chuyển trong máy chủ đích.

Lớp mạng của Internet bao gồm giao thức IP nổi tiếng, xác định các trường trong datagram cũng như cách các hệ thống cuối và bộ định tuyến hoạt động trên các trường này. Chỉ có một giao thức IP và tất cả các thành phần Internet có lớp mạng phải chạy giao thức IP. Lớp mạng của Internet cũng chứa các giao thức định tuyến xác định các tuyến đường mà các gói dữ liệu đi giữa nguồn và đích. Internet có nhiều giao thức định tuyến. Như chúng ta đã thấy trong Phần 1.3, Internet là một mạng gồm nhiều mạng và trong mạng, quản trị viên mạng có thể chạy bất kỳ giao thức định tuyến nào mong muốn. Mặc dù lớp mạng chứa cả giao thức IP và nhiều giao thức định tuyến, nhưng nó thường được gọi đơn giản là lớp IP, phản ánh thực tế rằng IP là chất keo gắn kết Internet lại với nhau.

Link Layer

Lớp mạng của Internet định tuyến một datagram thông qua một loạt các bộ định tuyến giữa nguồn và đích. Để di chuyển gói từ một nút (máy chủ hoặc bộ định tuyến) sang nút tiếp theo trong tuyến, lớp mạng sẽ dựa vào các dịch vụ của lớp liên kết. Cụ thể, tại mỗi nút, lớp mạng chuyển datagram xuống lớp liên kết, lớp này sẽ phân phối datagram đến nút tiếp theo dọc theo tuyến đường. Tại nút tiếp theo này, lớp liên kết chuyển datagram lên lớp mạng.

Các dịch vụ được cung cấp bởi lớp liên kết phụ thuộc vào giao thức lớp liên kết cụ thể được sử dụng trên liên kết. Ví dụ: một số giao thức lớp liên kết cung cấp khả năng phân phối đáng tin cậy, từ nút truyền, qua một liên kết, đến nút nhận. Lưu ý rằng dịch vụ phân phối đáng tin cậy này khác với dịch vụ phân phối đáng tin cậy của TCP, dịch vụ cung cấp khả năng phân phối đáng tin cậy từ hệ thống đầu này đến hệ thống đầu cuối khác. Ví dụ về các giao thức lớp liên kết bao gồm Ethernet, WiFi và giao thức DOCSIS của mạng truy cập cáp. Vì các datagram thường cần phải đi qua nhiều liên kết để di chuyển từ nguồn tới đích, nên một datagram có thể được xử lý bởi các giao thức lớp liên kết khác nhau tại các liên kết khác nhau dọc theo tuyến đường của nó. Ví dụ: một datagram có thể được xử lý bằng Ethernet trên một liên kết và bằng PPP trên

liên kết tiếp theo. Lớp mạng sẽ nhận được một dịch vụ khác nhau từ mỗi giao thức lớp liên kết khác nhau. Trong cuốn sách này, chúng ta sẽ gọi các gói lớp liên kết là các khung.

Physical Layer

Trong khi công việc của lớp liên kết là di chuyển toàn bộ khung từ một thành phần mạng này sang thành phần mạng lân cận thì công việc của lớp vật lý là di chuyển các bit riêng lẻ trong khung từ nút này sang nút tiếp theo. Các giao thức trong lớp này lại phụ thuộc vào liên kết và hơn nữa còn phụ thuộc vào phương tiện truyền dẫn thực tế của liên kết (ví dụ: dây đồng xoắn đôi, cáp quang đơn mode). Ví dụ, Ethernet có nhiều giao thức lớp vật lý: một cho dây đồng xoắn đôi, một cho cáp đồng trục, một cho cáp quang, v.v. Trong mỗi trường hợp, một bit được di chuyển qua liên kết theo một cách khác nhau.

**1.5.2 Đóng gói**

Hình 1.24 cho thấy đường dẫn vật lý mà dữ liệu đi xuống ngăn xếp giao thức của hệ thống đầu cuối gửi, lên và xuống ngăn xếp giao thức của một bộ chuyển mạch lớp liên kết can thiệp

*Hình 1.24 ♦ Hosts, bộ định tuyến và bộ chuyển mạch lớp liên kết; mỗi cái chứa một*

tập hợp các lớp khác nhau, phản ánh sự khác biệt về chức năng của chúng

M

M

M

M

Ht Ht

ht

Hn

Hn Hl

Ht Hn Hl

Chuyển mạch lớp liên kết

Router

Ứng dụng

Chuyên chở

Mạng

liên kết

Thuộc vật chất

Tin nhắn

Segment

Datagram

Frame

M

M

M

M

Ht Ht

ht

Hn

Hn Hl

liên kết

Thuộc vật chất

Nguồn

Mạng

liên kết

Thuộc vật chất

Điểm đến

Ứng dụng

Chuyên chở

Mạng

liên kết

Thuộc vật chất

M Ht Hn Hl M

Ht Hn M Ht Hn M

Ht Hn Hl M Ht Hn Hl M

và bộ định tuyến, sau đó nâng lên ngăn xếp giao thức ở hệ thống đầu nhận. Như chúng ta sẽ thảo luận sau trong cuốn sách này, bộ định tuyến và bộ chuyển mạch lớp liên kết đều là bộ chuyển mạch gói. Tương tự như các hệ thống đầu cuối, bộ định tuyến và bộ chuyển mạch lớp liên kết sắp xếp phần cứng và phần mềm mạng của chúng thành các lớp. Nhưng các bộ định tuyến và bộ chuyển mạch lớp liên kết không triển khai tất cả các lớp trong ngăn xếp giao thức; họ thường chỉ thực hiện các lớp dưới cùng. Như được hiển thị trong Hình 1.24, các bộ chuyển mạch lớp liên kết thực hiện lớp 1 và 2; bộ định tuyến triển khai các lớp từ 1 đến 3. Ví dụ: điều này có nghĩa là bộ định tuyến Internet có khả năng triển khai giao thức IP (giao thức lớp 3), trong khi các bộ chuyển mạch lớp liên kết thì không. Sau này chúng ta sẽ thấy rằng mặc dù các bộ chuyển mạch lớp liên kết không nhận ra địa chỉ IP nhưng chúng có khả năng nhận dạng địa chỉ lớp 2, chẳng hạn như địa chỉ Ethernet. Lưu ý rằng các máy chủ triển khai tất cả năm lớp; điều này phù hợp với quan điểm cho rằng kiến ​​trúc Internet đặt phần lớn sự phức tạp của nó vào các biên của mạng.

Hình 1.24 cũng minh họa khái niệm đóng gói quan trọng. Tại máy chủ gửi, một tin nhắn lớp ứng dụng (M trong Hình 1.24) được chuyển đến lớp vận chuyển. Trong trường hợp đơn giản nhất, lớp vận chuyển nhận thông báo và thêm thông tin bổ sung (được gọi là thông tin tiêu đề của lớp vận chuyển, Ht trong Hình 1.24) sẽ được sử dụng bởi lớp vận chuyển bên nhận. Thông báo lớp ứng dụng và thông tin tiêu đề lớp vận chuyển cùng nhau tạo thành phân đoạn lớp vận chuyển. Do đó, phân đoạn lớp vận chuyển sẽ đóng gói thông điệp của lớp ứng dụng. Thông tin được thêm vào có thể bao gồm thông tin cho phép lớp vận chuyển phía người nhận gửi tin nhắn đến ứng dụng thích hợp và các bit phát hiện lỗi cho phép người nhận xác định xem các bit trong tin nhắn có bị thay đổi trong lộ trình hay không. Sau đó, lớp vận chuyển chuyển phân đoạn này đến lớp mạng, lớp này sẽ thêm thông tin tiêu đề của lớp mạng (Hn trong Hình 1.24) chẳng hạn như địa chỉ hệ thống đầu cuối nguồn và đích, tạo ra một datagram lớp mạng. Sau đó, datagram được chuyển đến lớp liên kết, lớp này (tất nhiên!) sẽ thêm thông tin tiêu đề lớp liên kết của riêng nó và tạo khung lớp liên kết. Vì vậy, chúng ta thấy rằng ở mỗi lớp, một gói có hai loại trường: trường tiêu đề và trường tải trọng. Tải trọng thường là một gói từ lớp trên.

Một sự tương tự hữu ích ở đây là việc gửi một bản ghi nhớ nội bộ từ văn phòng chi nhánh công ty này sang văn phòng chi nhánh công ty khác thông qua dịch vụ bưu chính công cộng. Giả sử Alice, người đang ở một văn phòng chi nhánh, muốn gửi một bản ghi nhớ cho Bob, người đang ở một văn phòng chi nhánh khác. Bản ghi nhớ tương tự như thông báo ở lớp ứng dụng. Alice đặt bản ghi nhớ vào một phong bì nội bộ có ghi tên và bộ phận của Bob ở mặt trước của phong bì. Phong bì liên văn phòng tương tự như một phân đoạn của lớp vận chuyển---nó chứa thông tin tiêu đề (tên của Bob và số phòng ban) và nó đóng gói thông điệp của lớp ứng dụng (bản ghi nhớ). Khi phòng thư của văn phòng chi nhánh gửi nhận được phong bì liên văn phòng, nó sẽ đặt phong bì nội bộ vào trong một phong bì khác phù hợp để gửi qua dịch vụ bưu chính công cộng. Phòng thư gửi cũng ghi địa chỉ bưu điện của văn phòng chi nhánh gửi và nhận trên phong bì bưu điện. Đây, phong bì bưu điện

tương tự như datagram---nó đóng gói phân đoạn lớp vận chuyển (phong bì nội bộ), đóng gói thông điệp gốc (bản ghi nhớ). Dịch vụ bưu chính chuyển phong bì bưu chính đến phòng thư của văn phòng chi nhánh nhận. Ở đó, quá trình giải đóng gói được bắt đầu. Phòng thư trích xuất bản ghi nhớ nội bộ và chuyển nó cho Bob. Cuối cùng, Bob mở phong bì và lấy lá thư ra.

Quá trình đóng gói có thể phức tạp hơn mô tả ở trên. Ví dụ: một thông báo lớn có thể được chia thành nhiều phân đoạn lớp vận chuyển (bản thân mỗi phân đoạn này có thể được chia thành nhiều gói dữ liệu lớp mạng). Ở đầu nhận, một đoạn như vậy sau đó phải được xây dựng lại từ các datagram cấu thành của nó.

**1.6 Mạng đang bị tấn công**

Internet đã trở thành sứ mệnh quan trọng đối với nhiều tổ chức ngày nay, bao gồm các công ty lớn và nhỏ, trường đại học và cơ quan chính phủ. Nhiều cá nhân cũng dựa vào Internet cho nhiều hoạt động nghề nghiệp, xã hội và cá nhân của họ. Hàng tỷ "thứ", bao gồm cả thiết bị đeo và thiết bị gia đình, hiện đang được kết nối với Internet. Nhưng đằng sau tất cả tiện ích và sự phấn khích này, có một mặt tối, một mặt mà "kẻ xấu" cố gắng tàn phá cuộc sống hàng ngày của chúng ta bằng cách làm hỏng các máy tính được kết nối Internet của chúng ta, vi phạm quyền riêng tư của chúng ta và khiến các dịch vụ Internet mà chúng ta phụ thuộc vào không thể hoạt động được.

Lĩnh vực an ninh mạng nói về cách kẻ xấu có thể tấn công mạng máy tính và cách chúng ta, những chuyên gia sắp trở thành chuyên gia về mạng máy tính, có thể bảo vệ mạng khỏi những cuộc tấn công đó hoặc tốt hơn nữa là thiết kế các kiến ​​trúc mới miễn nhiễm với những cuộc tấn công như vậy ngay từ đầu. Với tần suất và sự đa dạng của các cuộc tấn công hiện tại cũng như mối đe dọa của các cuộc tấn công mới và có sức tàn phá cao hơn trong tương lai, an ninh mạng đã trở thành chủ đề trung tâm trong lĩnh vực mạng máy tính. Một trong những đặc điểm của cuốn sách này là nó đặt vấn đề an ninh mạng lên hàng đầu.

Vì chúng ta chưa có chuyên môn về mạng máy tính và các giao thức Internet nên chúng ta sẽ bắt đầu ở đây bằng cách khảo sát một số vấn đề liên quan đến bảo mật phổ biến hơn hiện nay. Điều này sẽ kích thích sự khao khát của chúng ta về những cuộc thảo luận quan trọng hơn trong các chương sắp tới. Vì vậy, chúng ta bắt đầu ở đây bằng cách hỏi đơn giản, điều gì có thể xảy ra sai sót? Mạng máy tính dễ bị tổn thương như thế nào? Một số loại tấn công phổ biến nhất hiện nay là gì?

Kẻ xấu có thể đưa phần mềm độc hại vào Host của bạn qua Internet

Chúng ta kết nối các thiết bị với Internet vì chúng ta muốn nhận/gửi dữ liệu từ/đến Internet. Điều này bao gồm tất cả các loại nội dung hay, bao gồm các bài đăng trên Instagram, Internet

kết quả tìm kiếm, phát nhạc trực tuyến, cuộc gọi hội nghị video, phát trực tuyến phim, v.v. Tuy nhiên, thật không may, cùng với tất cả những thứ tốt đẹp đó lại có những thứ độc hại---được gọi chung là phần mềm độc hại---cũng có thể xâm nhập và lây nhiễm vào thiết bị của chúng ta. Khi phần mềm độc hại lây nhiễm vào thiết bị của chúng ta, nó có thể thực hiện mọi hành vi sai trái, bao gồm xóa các tệp của chúng ta và cài đặt phần mềm gián điệp thu thập thông tin cá nhân của chúng ta, chẳng hạn như số an sinh xã hội, mật khẩu và thao tác gõ phím, sau đó gửi thông tin này (tất nhiên là qua Internet!) lại cho kẻ xấu. Máy chủ bị xâm nhập của chúng tôi cũng có thể được đăng ký vào mạng gồm hàng nghìn thiết bị bị xâm nhập tương tự, được gọi chung là mạng botnet mà kẻ xấu kiểm soát và lợi dụng để phát tán e-mail spam hoặc phân tán các cuộc tấn công từ chối dịch vụ (sẽ sớm được thảo luận) chống lại các máy chủ được nhắm mục tiêu.

Phần lớn phần mềm độc hại hiện nay có khả năng tự sao chép: khi lây nhiễm vào một máy chủ, từ máy chủ đó, nó sẽ tìm cách xâm nhập vào các máy chủ khác qua Internet và từ các máy chủ mới bị nhiễm, nó sẽ tìm cách xâm nhập vào nhiều máy chủ khác. Theo cách này, phần mềm độc hại tự sao chép có thể lây lan nhanh theo cấp số nhân.

Kẻ xấu có thể tấn công máy chủ và cơ sở hạ tầng mạng

Một loại mối đe dọa bảo mật rộng rãi khác được gọi là tấn công từ chối dịch vụ (DoS). Đúng như tên gọi, một cuộc tấn công DoS khiến người dùng hợp pháp không thể sử dụng mạng, máy chủ hoặc phần cơ sở hạ tầng khác. Máy chủ web, máy chủ e-mail, máy chủ DNS (được thảo luận trong Chương 2) và mạng tổ chức đều có thể bị tấn công DoS. Trang web Bản đồ tấn công kỹ thuật số cho phép sử dụng để hình dung các cuộc tấn công DoS hàng ngày hàng đầu trên toàn thế giới \[DAM 2020\]. Hầu hết các cuộc tấn công DoS trên Internet thuộc một trong ba loại:

• Tấn công lỗ hổng. Điều này liên quan đến việc gửi một số tin nhắn được thiết kế kỹ lưỡng đến một ứng dụng hoặc hệ điều hành dễ bị tấn công đang chạy trên máy chủ được nhắm mục tiêu. Nếu chuỗi gói phù hợp được gửi đến một ứng dụng hoặc hệ điều hành dễ bị tấn công, dịch vụ có thể dừng hoặc tệ hơn là máy chủ có thể gặp sự cố. • Bandwidth lũ lụt. Kẻ tấn công gửi một loạt gói đến máy chủ được nhắm mục tiêu---nhiều gói đến mức liên kết truy cập của mục tiêu bị tắc, ngăn chặn các gói hợp pháp đến được máy chủ. • Ngập kết nối. Kẻ tấn công thiết lập một số lượng lớn các kết nối TCP mở một nửa hoặc mở hoàn toàn (TCP kết nối được thảo luận trong Chương 3) tại máy chủ mục tiêu. Máy chủ có thể bị sa lầy với những kết nối không có thật này đến mức nó ngừng chấp nhận các kết nối hợp pháp.

Bây giờ chúng ta hãy khám phá cuộc tấn công làm tràn băng thông chi tiết hơn. Nhắc lại cuộc thảo luận về phân tích độ trễ và mất mát của chúng ta trong Phần 1.4.2, rõ ràng là nếu máy chủ có tốc độ truy cập là R bps thì kẻ tấn công sẽ cần gửi lưu lượng truy cập với tốc độ xấp xỉ R bps để gây ra thiệt hại. Nếu R rất lớn, một nguồn tấn công đơn lẻ có thể không tạo ra đủ lưu lượng truy cập để gây hại cho máy chủ. Hơn nữa, nếu tất cả

lưu lượng phát ra từ một nguồn duy nhất, bộ định tuyến ngược dòng có thể phát hiện cuộc tấn công và chặn tất cả lưu lượng truy cập từ nguồn đó trước khi lưu lượng truy cập đến gần máy chủ. Trong một cuộc tấn công DoS (DDoS) phân tán, được minh họa trong Hình 1.25, kẻ tấn công kiểm soát nhiều nguồn và có mỗi nguồn tấn công lưu lượng truy cập vào mục tiêu. Với cách tiếp cận này, tốc độ lưu lượng tổng hợp trên tất cả các nguồn được kiểm soát cần phải xấp xỉ R để làm tê liệt dịch vụ. Các cuộc tấn công DDoS lợi dụng các botnet với hàng nghìn máy chủ bao gồm là chuyện thường xuyên xảy ra hiện nay \[DAM 2020\]. Các cuộc tấn công DDos khó phát hiện và chống lại hơn nhiều so với cuộc tấn công DoS từ một máy chủ.

Chúng tôi khuyến khích bạn cân nhắc câu hỏi sau khi tìm hiểu cuốn sách này: Các nhà thiết kế mạng máy tính có thể làm gì để chống lại các cuộc tấn công DoS? Chúng ta sẽ thấy rằng cần có các biện pháp phòng vệ khác nhau cho ba loại tấn công DoS.

Kẻ Xấu Có Thể Đánh Hơi Packets

Nhiều người dùng ngày nay truy cập Internet thông qua các thiết bị không dây, chẳng hạn như máy tính xách tay có kết nối WiFi hoặc thiết bị cầm tay có kết nối Internet di động (được đề cập trong Chương 7). Mặc dù việc truy cập Internet ở mọi nơi cực kỳ thuận tiện và mang lại những ứng dụng mới tuyệt vời cho người dùng di động, nhưng nó cũng tạo ra một lỗ hổng bảo mật lớn---bằng cách đặt một bộ thu thụ động gần bộ phát không dây, bộ thu đó sẽ

*Hình 1.25 ♦ Tấn công từ chối dịch vụ phân tán*

kẻ tấn công

"bắt đầu tấn công"

thây ma

thây ma

thây ma

Nạn nhân

thây ma

thây ma

có thể có được một bản sao của mỗi gói được truyền đi! Các gói này có thể chứa tất cả các loại thông tin nhạy cảm, bao gồm mật khẩu, số an sinh xã hội, bí mật thương mại và tin nhắn cá nhân riêng tư. Một máy thu thụ động ghi lại một bản sao của mỗi gói tin bay qua được gọi là packet sniffer.

Sniffers cũng có thể được triển khai trong môi trường có dây. Trong môi trường quảng bá có dây, như trong nhiều mạng LAN Ethernet, trình nghe lén gói có thể lấy được bản sao của các gói quảng bá được gửi qua mạng LAN. Như được mô tả trong Phần 1.2, các công nghệ truy cập cáp cũng phát các gói tin và do đó dễ bị đánh cắp. Hơn nữa, kẻ xấu có quyền truy cập vào bộ định tuyến truy cập hoặc liên kết truy cập Internet của tổ chức có thể tạo ra một trình thám thính tạo bản sao của mọi gói đến/từ tổ chức. Các gói được đánh hơi sau đó có thể được phân tích ngoại tuyến để tìm thông tin nhạy cảm.

Packet-phần mềm đánh hơi được cung cấp miễn phí trên nhiều trang Web khác nhau và dưới dạng sản phẩm thương mại. Các giáo sư giảng dạy một khóa học về mạng thường giao các bài tập trong phòng thí nghiệm liên quan đến việc viết chương trình tái thiết dữ liệu lớp ứng dụng và đánh hơi gói. Thật vậy, các lab Wireshark \[Wireshark 2020\] được liên kết với văn bản này (xem phần giới thiệu Wireshark lab ở cuối chương này) sử dụng chính xác một trình thu thập gói tin như vậy!

Bởi vì các trình nghe lén gói là thụ động---nghĩa là chúng không đưa các gói vào kênh---nên rất khó bị phát hiện. Vì vậy, khi chúng ta gửi các gói vào một kênh không dây, chúng ta phải chấp nhận khả năng kẻ xấu nào đó có thể ghi lại các bản sao của các gói của chúng ta. Như bạn có thể đoán, một số biện pháp phòng vệ tốt nhất chống lại việc đánh hơi gói liên quan đến mật mã. Chúng ta sẽ xem xét mật mã khi nó áp dụng cho an ninh mạng trong Chương 8.

Kẻ xấu có thể hóa trang thành người mà bạn tin tưởng

Thật dễ dàng một cách đáng ngạc nhiên (bạn sẽ có kiến ​​thức để làm điều đó ngay khi bạn xem qua nội dung này!) để tạo một gói có địa chỉ nguồn, nội dung gói và địa chỉ đích tùy ý, sau đó truyền gói thủ công này vào Internet, gói này sẽ chuyển tiếp gói đến đích một cách nghiêm túc. Hãy tưởng tượng người nhận không nghi ngờ (chẳng hạn như bộ định tuyến Internet) nhận được gói như vậy, coi địa chỉ nguồn (sai) là trung thực và sau đó thực hiện một số lệnh được nhúng trong nội dung của gói (chẳng hạn như sửa đổi bảng chuyển tiếp của nó). Khả năng đưa các gói vào Internet bằng địa chỉ nguồn sai được gọi là IP giả mạo và chỉ là một trong nhiều cách mà một người dùng có thể giả mạo thành một người dùng khác.

Để giải quyết vấn đề này, chúng ta sẽ cần xác thực điểm cuối, tức là một cơ chế cho phép chúng ta xác định một cách chắc chắn liệu thông báo có bắt nguồn từ nơi chúng ta nghĩ hay không. Một lần nữa, chúng tôi khuyến khích bạn suy nghĩ về cách thực hiện điều này đối với các ứng dụng và giao thức mạng khi bạn đọc qua các chương của cuốn sách này. Chúng ta sẽ khám phá các cơ chế xác thực điểm cuối trong Chương 8.

Khi kết thúc phần này, cần xem xét tại sao Internet lại trở thành một nơi không an toàn như vậy ngay từ đầu. Về bản chất, câu trả lời là Internet ban đầu được thiết kế theo cách đó, dựa trên mô hình "một nhóm người dùng tin tưởng lẫn nhau gắn liền với một mạng minh bạch" \[Blumenthal 2001\]---một mô hình trong đó (theo định nghĩa) không cần đến bảo mật. Nhiều khía cạnh của kiến ​​trúc Internet ban đầu phản ánh sâu sắc khái niệm về sự tin cậy lẫn nhau. Ví dụ: khả năng một người dùng gửi gói cho bất kỳ người dùng nào khác là mặc định chứ không phải là khả năng được yêu cầu/được cấp và danh tính người dùng được lấy theo mệnh giá đã khai báo, thay vì được xác thực theo mặc định.

Nhưng Internet ngày nay chắc chắn không liên quan đến việc "người dùng tin tưởng lẫn nhau". Tuy nhiên, người dùng ngày nay vẫn cần liên lạc khi họ không nhất thiết phải tin tưởng lẫn nhau, có thể muốn liên lạc ẩn danh, có thể liên lạc gián tiếp thông qua các bên thứ ba (ví dụ: bộ nhớ đệm Web, mà chúng ta sẽ nghiên cứu ở Chương 2, hoặc các tác nhân hỗ trợ di động, mà chúng ta sẽ nghiên cứu ở Chương 7), và có thể không tin tưởng vào phần cứng, phần mềm và thậm chí cả không khí mà họ giao tiếp qua đó. Hiện tại, chúng ta đang phải đối mặt với nhiều thách thức liên quan đến bảo mật khi đọc cuốn sách này: Chúng ta nên tìm kiếm các biện pháp bảo vệ chống lại hoạt động đánh hơi, giả mạo điểm cuối, tấn công trung gian, tấn công DDoS, phần mềm độc hại, v.v. Chúng ta nên nhớ rằng giao tiếp giữa những người dùng đáng tin cậy lẫn nhau là ngoại lệ chứ không phải là quy tắc. Chào mừng đến với thế giới mạng máy tính hiện đại!

**1.7 Lịch sử mạng máy tính và Internet**

Phần 1.1 đến 1.6 trình bày tổng quan về công nghệ mạng máy tính và Internet. Bây giờ bạn nên biết đủ để gây ấn tượng với gia đình và bạn bè của bạn! Tuy nhiên, nếu bạn thực sự muốn trở thành người nổi tiếng trong bữa tiệc cocktail tiếp theo, bạn nên rắc lên bài diễn thuyết của mình những mẩu tin nhỏ về lịch sử hấp dẫn của Internet \[Segaller 1998\].

**1.7.1 Sự phát triển của Packet Chuyển mạch: 1961--1972**

Lĩnh vực mạng máy tính và Internet ngày nay bắt nguồn từ đầu những năm 1960, khi mạng điện thoại là mạng truyền thông thống trị thế giới. Hãy nhớ lại Phần 1.3 rằng mạng điện thoại sử dụng chuyển mạch để truyền thông tin từ người gửi đến người nhận---một lựa chọn thích hợp cho rằng giọng nói được truyền ở tốc độ không đổi giữa người gửi và người nhận. Do tầm quan trọng ngày càng tăng của máy tính vào đầu những năm 1960 và sự ra đời của máy tính chia sẻ thời gian, có lẽ việc xem xét cách kết nối các máy tính với nhau để chúng có thể được chia sẻ giữa các khu vực địa lý là điều tự nhiên.

người dùng phân tán. Lưu lượng do những người dùng như vậy tạo ra có thể sẽ bùng nổ--- các khoảng thời gian hoạt động, chẳng hạn như gửi lệnh đến máy tính từ xa, sau đó là các khoảng thời gian không hoạt động trong khi chờ phản hồi hoặc trong khi xem xét phản hồi nhận được.

Ba nhóm nghiên cứu trên khắp thế giới, mỗi nhóm không biết về công việc của những người khác \[Leiner 1998\], bắt đầu phát minh ra chuyển mạch gói như một giải pháp thay thế hiệu quả và mạnh mẽ cho chuyển mạch kênh. Công trình được xuất bản đầu tiên về kỹ thuật chuyển mạch gói là của Leonard Kleinrock \[Kleinrock 1961; Kleinrock 1964\], khi đó là nghiên cứu sinh tại MIT. Sử dụng lý thuyết xếp hàng, công trình của Kleinrock đã chứng minh một cách rõ ràng tính hiệu quả của phương pháp chuyển mạch gói đối với các nguồn lưu lượng truy cập bùng nổ. Năm 1964, Paul Baran \[Baran 1964\] tại Viện Rand đã bắt đầu nghiên cứu việc sử dụng chuyển mạch gói cho giọng nói an toàn trên các mạng quân sự, và tại Phòng thí nghiệm Vật lý Quốc gia ở Anh, Donald Davies và Roger Scantlebury cũng đang phát triển ý tưởng của họ về chuyển mạch gói.

Công việc tại MIT, Rand và NPL đã đặt nền móng cho Internet ngày nay. Nhưng Internet cũng có một lịch sử lâu dài về thái độ hãy xây dựng nó và thể hiện nó cũng có từ những năm 1960. J. C. R. Licklider \[Tháng 12 năm 1990\] và Lawrence Roberts, cả hai đều là đồng nghiệp của Kleinrock tại MIT, tiếp tục dẫn dắt chương trình khoa học máy tính tại Cơ quan Dự án Nghiên cứu Tiên tiến (ARPA) ở Hoa Kỳ. Roberts đã xuất bản một kế hoạch tổng thể cho ARPAnet \[Roberts 1967\], mạng máy tính chuyển mạch gói đầu tiên và là tổ tiên trực tiếp của Internet công cộng ngày nay. Vào Ngày lễ Lao động năm 1969, bộ chuyển mạch gói đầu tiên được lắp đặt tại UCLA dưới sự giám sát của Kleinrock và ba bộ chuyển mạch gói bổ sung đã được lắp đặt ngay sau đó tại Viện nghiên cứu Stanford (SRI), UC Santa Barbara và Đại học Utah (Hình 1.26). Tiền thân non trẻ của Internet có bốn nút lớn vào cuối năm 1969. Kleinrock nhớ lại lần đầu tiên sử dụng mạng để thực hiện đăng nhập từ xa từ UCLA đến SRI, đã làm hỏng hệ thống \[Kleinrock 2004\].

Đến năm 1972, ARPAnet đã phát triển lên khoảng 15 nút và được Robert Kahn trình diễn công khai lần đầu tiên. Giao thức giữa máy chủ với máy chủ đầu tiên giữa các hệ thống cuối ARPAnet, được gọi là giao thức điều khiển mạng (NCP), đã được hoàn thành \[RFC 001\]. Với giao thức end-to-end sẵn có, giờ đây các ứng dụng có thể được viết. Ray Tomlinson viết chương trình e-mail đầu tiên vào năm 1972.

**1.7.2 Mạng độc quyền và liên kết mạng: 1972--1980**

ARPAnet ban đầu là một mạng khép kín. Để liên lạc với máy chủ ARPAnet, một máy chủ phải được gắn vào một ARPAnet IMP khác. Vào đầu đến giữa những năm 1970, các mạng chuyển mạch gói độc lập bổ sung ngoài ARPAnet đã ra đời: ALOHANet, mạng vi sóng liên kết các trường đại học trên quần đảo Hawaii \[Abramson 1970\], cũng như mạng vệ tinh gói \[RFC 829\] và mạng vô tuyến gói của DARPA \[Kahn 1978\]; Telenet, dịch vụ chuyển mạch gói thương mại BBN

mạng dựa trên công nghệ ARPAnet; Cyclades, mạng chuyển mạch gói của Pháp do Louis Pouzin tiên phong \[Think 2012\]; Các mạng chia sẻ thời gian như Tymnet và mạng Dịch vụ Thông tin GE, cùng nhiều mạng khác, vào cuối những năm 1960 và đầu những năm 1970 \[Schwartz 1977\]; SNA của IBM (1969--1974), song song với ARPAnet \[Schwartz 1977\].

Số lượng mạng ngày càng tăng. Với nhận thức hoàn hảo, chúng ta có thể thấy rằng thời điểm đã chín muồi để phát triển một kiến ​​trúc toàn diện nhằm kết nối các mạng với nhau. Tiên phong nghiên cứu về các mạng kết nối (dưới sự tài trợ của Cơ quan Dự án Nghiên cứu Quốc phòng Tiên tiến (DARPA)), về bản chất là tạo ra

*Hình 1.26 ♦ Chuyển mạch gói sớm*

Ảnh Mark J. Terrill/AP

![](media/image3.png){width="5.5in" height="7.749511154855643in"}

một mạng lưới các mạng được thực hiện bởi Vinton Cerf và Robert Kahn \[Cerf 1974\]; thuật ngữ internetting được đặt ra để mô tả công việc này.

Những nguyên tắc kiến ​​trúc này được thể hiện trong TCP. Tuy nhiên, các phiên bản đầu tiên của TCP khá khác so với TCP ngày nay. Các phiên bản đầu tiên của TCP đã kết hợp việc phân phối dữ liệu theo trình tự đáng tin cậy thông qua truyền lại hệ thống cuối (vẫn là một phần của TCP ngày nay) với các chức năng chuyển tiếp (ngày nay được thực hiện bởi IP). Thử nghiệm ban đầu với TCP, kết hợp với nhận thức về tầm quan trọng của dịch vụ truyền tải từ đầu đến cuối, không được kiểm soát luồng, không đáng tin cậy đối với các ứng dụng như giọng nói được đóng gói, đã dẫn đến việc tách IP ra khỏi TCP và phát triển giao thức UDP. Ba giao thức Internet quan trọng mà chúng ta thấy ngày nay---TCP, UDP và IP---về mặt khái niệm đã có vào cuối những năm 1970.

Ngoài nghiên cứu liên quan đến Internet của DARPA, nhiều hoạt động kết nối mạng quan trọng khác cũng đang được tiến hành. Ở Hawaii, Norman Abramson đang phát triển ALOHAnet, một mạng vô tuyến dựa trên gói cho phép nhiều địa điểm ở xa trên Quần đảo Hawaii liên lạc với nhau. Giao thức ALOHA \[Abramson 1970\] là giao thức đa truy cập đầu tiên, cho phép người dùng phân tán về mặt địa lý chia sẻ một phương tiện truyền thông quảng bá duy nhất (tần số vô tuyến). Metcalfe và Boggs được xây dựng trên giao thức đa truy cập của Abramson hoạt động được khi họ phát triển giao thức Ethernet \[Metcalfe 1976\] cho các mạng phát sóng chia sẻ dựa trên dây. Điều thú vị là giao thức Ethernet của Metcalfe và Boggs được thúc đẩy bởi nhu cầu kết nối nhiều PC, máy in và ổ đĩa dùng chung \[Perkins 1994\]. 25 năm trước, trước cuộc cách mạng PC và sự bùng nổ của mạng, Metcalfe và Boggs đã đặt nền móng cho mạng LAN PC ngày nay.

**1.7.3 Sự phổ biến của các mạng: 1980--1990**

Đến cuối những năm 1970, khoảng hai trăm máy chủ đã được kết nối với ARPAnet. Vào cuối những năm 1980, số lượng máy chủ kết nối với Internet công cộng, một liên minh các mạng trông giống như Internet ngày nay, đã lên tới con số một trăm nghìn. Những năm 1980 sẽ là thời kỳ tăng trưởng vượt bậc.

Phần lớn sự tăng trưởng đó là kết quả của một số nỗ lực khác biệt nhằm tạo ra các mạng máy tính liên kết các trường đại học với nhau. BITNET cung cấp e-mail và chuyển tập tin giữa một số trường đại học ở vùng Đông Bắc. CSNET (mạng khoa học máy tính) được thành lập để liên kết các nhà nghiên cứu đại học không có quyền truy cập vào ARPAnet. Năm 1986, NSFNET được thành lập để cung cấp quyền truy cập vào các trung tâm siêu máy tính do NSF tài trợ. Bắt đầu với tốc độ đường trục ban đầu là 56 kbps, đường trục của NSFNET sẽ chạy ở tốc độ 1,5 Mbps vào cuối thập kỷ này và sẽ đóng vai trò là đường trục chính liên kết các mạng khu vực.

Trong cộng đồng ARPAnet, nhiều phần cuối cùng của kiến ​​trúc Internet ngày nay đã được đưa vào sử dụng. Ngày 1 tháng 1 năm 1983 chứng kiến ​​việc triển khai chính thức TCP/IP làm giao thức máy chủ tiêu chuẩn mới cho ARPAnet (thay thế giao thức NCP). Quá trình chuyển đổi \[RFC 801\] từ NCP sang TCP/IP là một sự kiện trong ngày gắn cờ---tất cả các máy chủ đều được yêu cầu chuyển sang TCP/IP kể từ ngày đó. Vào cuối những năm 1980,

các phần mở rộng quan trọng đã được thực hiện cho TCP để triển khai kiểm soát tắc nghẽn dựa trên máy chủ \[Jacobson 1988\]. DNS, được sử dụng để ánh xạ giữa tên Internet mà con người có thể đọc được (ví dụ: gaia.cs.umass.edu) và địa chỉ IP 32-bit của nó, cũng được phát triển \[RFC 1034\].

Song song với sự phát triển ARPAnet này (phần lớn là nỗ lực của Hoa Kỳ), vào đầu những năm 1980, người Pháp đã khởi động dự án Minitel, một kế hoạch đầy tham vọng nhằm đưa mạng dữ liệu đến mọi nhà. Được chính phủ Pháp tài trợ, hệ thống Minitel bao gồm mạng chuyển mạch gói công cộng (dựa trên bộ giao thức X.25), máy chủ Minitel và thiết bị đầu cuối rẻ tiền có tích hợp modem tốc độ thấp. Minitel đã đạt được thành công lớn vào năm 1984 khi chính phủ Pháp tặng thiết bị đầu cuối Minitel miễn phí cho mỗi hộ gia đình Pháp muốn có. Các trang web của Minitel bao gồm các trang web miễn phí---chẳng hạn như trang web danh bạ điện thoại---cũng như các trang web riêng tư, thu phí dựa trên việc sử dụng từ mỗi người dùng. Vào thời kỳ đỉnh cao vào giữa những năm 1990, nó cung cấp hơn 20.000 dịch vụ, từ ngân hàng gia đình đến cơ sở dữ liệu nghiên cứu chuyên ngành. Minitel có mặt ở phần lớn các ngôi nhà ở Pháp 10 năm trước khi hầu hết người Mỹ biết đến Internet.

**1.7.4 Sự bùng nổ Internet: Những năm 1990**

Những năm 1990 đã mở ra một số sự kiện tượng trưng cho sự phát triển không ngừng và sự thương mại hóa sắp diễn ra của Internet. ARPAnet, tổ tiên của Internet, đã không còn tồn tại. Năm 1991, NSFNET dỡ bỏ các hạn chế đối với việc sử dụng NSFNET cho mục đích thương mại. Bản thân NSFNET sẽ ngừng hoạt động vào năm 1995, với lưu lượng đường trục Internet được thực hiện bởi các Nhà cung cấp dịch vụ Internet thương mại.

Sự kiện chính của những năm 1990 là sự xuất hiện của ứng dụng World Wide Web, đưa Internet đến các gia đình và doanh nghiệp của hàng triệu người trên toàn thế giới. Web phục vụ như một nền tảng cho phép và triển khai hàng trăm ứng dụng mới mà chúng ta coi là đương nhiên ngày nay, bao gồm tìm kiếm (ví dụ: Google và Bing), thương mại Internet (ví dụ: Amazon và eBay) và các mạng xã hội (ví dụ: Facebook).

Web được phát minh tại CERN bởi Tim Berners-Lee trong khoảng thời gian từ 1989 đến 1991 \[Berners-Lee 1989\], dựa trên những ý tưởng bắt nguồn từ công trình trước đó về siêu văn bản từ những năm 1940 của Vannevar Bush \[Bush 1945\] và từ những năm 1960 của Ted Nelson \[Xanadu 2012\]. Berners-Lee và các cộng sự của ông đã phát triển các phiên bản đầu tiên của HTML, HTTP, máy chủ Web và trình duyệt---bốn thành phần chính của Web. Vào khoảng cuối năm 1993, có khoảng hai trăm máy chủ Web đang hoạt động, tập hợp các máy chủ này chỉ là điềm báo về những gì sắp xảy ra. Vào khoảng thời gian này, một số nhà nghiên cứu đang phát triển trình duyệt Web với giao diện GUI, trong đó có Marc Andreessen, người cùng với Jim Clark thành lập nên Khảm Communications, sau này trở thành Netscape Communications Corporation \[Cusumano 1998; Quittner 1998\]. Đến năm 1995, sinh viên đại học đã sử dụng trình duyệt Netscape để lướt Web hàng ngày. Vào khoảng thời gian này các công ty---lớn và nhỏ---bắt đầu hoạt động

Máy chủ web và giao dịch thương mại qua Web. Năm 1996, Microsoft bắt đầu sản xuất trình duyệt, điều này bắt đầu cuộc chiến trình duyệt giữa Netscape và Microsoft, mà Microsoft đã giành chiến thắng vài năm sau đó \[Cusumano 1998\].

Nửa sau của thập niên 1990 là thời kỳ Internet phát triển và đổi mới vượt bậc, với các tập đoàn lớn và hàng nghìn công ty khởi nghiệp tạo ra các sản phẩm và dịch vụ Internet. Đến cuối thiên niên kỷ, Internet đã hỗ trợ hàng trăm ứng dụng phổ biến, trong đó có bốn ứng dụng nổi bật:

• E-mail, bao gồm các tệp đính kèm và e-mail có thể truy cập Web • Web, bao gồm duyệt Web và thương mại trên Internet • Nhắn tin nhanh, với danh sách liên hệ • Chia sẻ tệp MP3 ngang hàng, được tiên phong bởi Napster

Điều thú vị là hai ứng dụng nổi bật đầu tiên đến từ cộng đồng nghiên cứu, trong khi hai ứng dụng cuối cùng được tạo ra bởi một số doanh nhân trẻ.

Giai đoạn từ 1995 đến 2001 là giai đoạn thăng trầm của Internet trên thị trường tài chính. Trước khi có lãi, hàng trăm công ty khởi nghiệp về Internet đã phát hành cổ phiếu lần đầu ra công chúng và bắt đầu giao dịch trên thị trường chứng khoán. Nhiều công ty được định giá hàng tỷ đô la mà không có bất kỳ dòng doanh thu đáng kể nào. Cổ phiếu Internet sụp đổ vào năm 2000--2001 và nhiều công ty khởi nghiệp đóng cửa. Tuy nhiên, một số công ty đã nổi lên như những người chiến thắng lớn trong lĩnh vực Internet, bao gồm Microsoft, Cisco, Yahoo, eBay, Google và Amazon.

**1.7.5 Thiên niên kỷ mới**

Trong hai thập kỷ đầu thế kỷ 21, có lẽ không có công nghệ nào làm thay đổi xã hội nhiều hơn Internet cùng với điện thoại thông minh có kết nối Internet. Và sự đổi mới trong mạng máy tính vẫn tiếp tục với tốc độ nhanh chóng. Những tiến bộ đang được thực hiện trên mọi mặt trận, bao gồm việc triển khai các bộ định tuyến nhanh hơn và tốc độ truyền cao hơn trong cả mạng truy cập và mạng đường trục. Nhưng những diễn biến sau đây đáng được quan tâm đặc biệt:

• Kể từ đầu thiên niên kỷ, chúng ta đã chứng kiến ​​sự triển khai tích cực truy cập Internet băng thông rộng đến từng gia đình---không chỉ modem cáp và DSL mà còn cả cáp quang tới gia đình và giờ đây là mạng không dây cố định 5G như đã thảo luận trong Phần 1.2. Truy cập Internet tốc độ cao này đã tạo tiền đề cho vô số ứng dụng video, bao gồm phân phối video do người dùng tạo (ví dụ: YouTube), phát trực tuyến phim và chương trình truyền hình theo yêu cầu (ví dụ: Netflix) và hội nghị video nhiều người (ví dụ: Skype, Facetime và Google Hangouts). • Sự phổ biến ngày càng tăng của truy cập Internet không dây tốc độ cao không chỉ giúp duy trì kết nối liên tục khi đang di chuyển mà còn cho phép các ứng dụng mới dành riêng cho vị trí như Yelp, Tinder và Waz. Số lượng thiết bị không dây kết nối Internet vượt số lượng thiết bị có dây

vào năm 2011. Truy cập không dây tốc độ cao này đã tạo tiền đề cho sự xuất hiện nhanh chóng của máy tính cầm tay (iPhone, Android, iPad, v.v.), có khả năng truy cập Internet liên tục và không bị ràng buộc. • Các mạng xã hội trực tuyến---chẳng hạn như Facebook, Instagram, Twitter và WeChat (cực kỳ phổ biến ở Trung Quốc)---đã tạo ra mạng lưới người dùng khổng lồ trên Internet. Nhiều mạng xã hội trong số này được sử dụng rộng rãi để nhắn tin cũng như chia sẻ ảnh. Nhiều người dùng Internet ngày nay "sống" chủ yếu trong một hoặc nhiều mạng xã hội. Thông qua API của họ, các mạng xã hội trực tuyến tạo ra nền tảng cho các ứng dụng nối mạng mới, bao gồm thanh toán di động và trò chơi được phân phối. • Như đã thảo luận trong Phần 1.3.3, các nhà cung cấp dịch vụ trực tuyến, chẳng hạn như Google và Microsoft, đã triển khai mạng riêng rộng rãi của riêng họ, mạng này không chỉ kết nối với các trung tâm dữ liệu phân bổ toàn cầu của họ mà còn được sử dụng để vượt qua Internet nhiều nhất có thể bằng cách kết nối trực tiếp với các ISP cấp thấp hơn. Kết quả là Google cung cấp kết quả tìm kiếm và quyền truy cập e-mail gần như ngay lập tức, như thể trung tâm dữ liệu của họ đang chạy trong máy tính của chính một người. • Nhiều công ty thương mại Internet hiện đang chạy các ứng dụng của họ trên "đám mây"---chẳng hạn như trên EC2 của Amazon, Azure của Microsoft hoặc trên Đám mây Alibaba. Nhiều công ty và trường đại học cũng đã chuyển các ứng dụng Internet của họ (ví dụ: e-mail và lưu trữ web) sang đám mây. Các công ty đám mây không chỉ cung cấp cho các ứng dụng môi trường điện toán và lưu trữ có thể mở rộng mà còn cung cấp cho các ứng dụng quyền truy cập ngầm vào mạng riêng hiệu suất cao của họ.

**1.8 Tóm tắt**

Trong chương này, chúng ta đã đề cập đến một lượng lớn tài liệu! Chúng ta đã xem xét các phần cứng và phần mềm khác nhau tạo nên Internet nói riêng và mạng máy tính nói chung. Chúng tôi bắt đầu ở rìa mạng, xem xét các hệ thống và ứng dụng cuối cũng như dịch vụ truyền tải được cung cấp cho các ứng dụng chạy trên hệ thống cuối. Chúng tôi cũng xem xét các công nghệ lớp liên kết và phương tiện vật lý thường thấy trong mạng truy cập. Sau đó, chúng tôi đi sâu hơn vào mạng, vào lõi mạng, xác định chuyển mạch gói và chuyển mạch là hai phương pháp cơ bản để truyền dữ liệu qua mạng viễn thông và chúng tôi đã xem xét điểm mạnh và điểm yếu của từng phương pháp. Chúng tôi cũng đã xem xét cấu trúc của Internet toàn cầu và biết rằng Internet là một mạng lưới các mạng. Chúng tôi thấy rằng cấu trúc phân cấp của Internet, bao gồm các ISP cấp cao hơn và cấp thấp hơn, đã cho phép nó mở rộng quy mô để bao gồm hàng nghìn mạng.

Trong phần thứ hai của chương giới thiệu này, chúng ta đã xem xét một số chủ đề trọng tâm trong lĩnh vực mạng máy tính. Đầu tiên chúng tôi xem xét nguyên nhân gây ra độ trễ, thông lượng và mất gói trong mạng chuyển mạch gói. Chúng tôi đã phát triển các mô hình định lượng đơn giản về độ trễ truyền, lan truyền và xếp hàng cũng như thông lượng; chúng ta sẽ sử dụng rộng rãi các mô hình độ trễ này trong các bài tập về nhà xuyên suốt cuốn sách này. Tiếp theo, chúng ta xem xét việc phân lớp giao thức và các mô hình dịch vụ, những nguyên tắc kiến ​​trúc quan trọng trong mạng mà chúng ta cũng sẽ đề cập lại trong suốt cuốn sách này. Chúng tôi cũng đã khảo sát một số cuộc tấn công bảo mật phổ biến hơn trong thời đại Internet. Chúng ta đã kết thúc phần giới thiệu về mạng bằng lịch sử ngắn gọn về mạng máy tính. Chương đầu tiên tự nó là một khóa học nhỏ về mạng máy tính.

Vì vậy, chúng ta thực sự đã đề cập đến một lượng kiến ​​thức khổng lồ trong chương đầu tiên này! Nếu bạn hơi choáng ngợp, đừng lo lắng. Trong các chương tiếp theo, chúng ta sẽ xem xét lại tất cả những ý tưởng này và trình bày chúng chi tiết hơn (đó là một lời hứa chứ không phải một mối đe dọa!). Tại thời điểm này, chúng tôi hy vọng bạn kết thúc chương này với trực giác vẫn đang phát triển về các phần tạo nên mạng lưới, vốn từ vựng về mạng lưới vẫn đang phát triển (đừng ngại quay lại chương này) và mong muốn tìm hiểu thêm về mạng lưới ngày càng tăng. Đó là nhiệm vụ phía trước của chúng ta trong phần còn lại của cuốn sách này.

Lập bản đồ đường đi cuốn sách này

Trước khi bắt đầu bất kỳ chuyến đi nào, bạn nên luôn xem qua bản đồ đường đi để làm quen với những con đường và ngã ba chính phía trước. Đối với chuyến đi mà chúng ta sắp bắt đầu, đích đến cuối cùng là sự hiểu biết sâu sắc về cách thức, cái gì và lý do của mạng máy tính. Lộ trình của chúng tôi là trình tự các chương của cuốn sách này:

1\. Mạng máy tính và Internet 2. Application Layer 3. Transport Layer 4. Network Layer: Mặt phẳng dữ liệu 5. Network Layer: Mặt phẳng điều khiển 6. Link Layer và mạng LAN 7. Mạng không dây và di động 8. Bảo mật trong mạng máy tính

Chương 2 đến Chương 6 là năm chương cốt lõi của cuốn sách này. Bạn nên chú ý rằng các chương này được sắp xếp xung quanh bốn lớp trên cùng của giao thức Internet năm lớp. Xin lưu ý thêm rằng hành trình của chúng tôi sẽ bắt đầu ở đầu ngăn xếp giao thức Internet, cụ thể là lớp ứng dụng và sẽ đi xuống. Lý do đằng sau hành trình từ trên xuống này là khi chúng ta hiểu được các ứng dụng, chúng ta có thể

hiểu các dịch vụ mạng cần thiết để hỗ trợ các ứng dụng này. Sau đó, chúng ta có thể kiểm tra các cách khác nhau mà các dịch vụ đó có thể được triển khai bởi kiến ​​trúc mạng. Do đó, việc đề cập đến các ứng dụng sớm sẽ mang lại động lực cho phần còn lại của văn bản.

Nửa sau của cuốn sách---Chương 7 và 8---đi sâu vào hai chủ đề cực kỳ quan trọng (và có phần độc lập) trong mạng máy tính hiện đại. Trong Chương 7, chúng ta xem xét các mạng không dây và di động, bao gồm mạng LAN không dây (bao gồm WiFi và Bluetooth), mạng di động (bao gồm 4G và 5G) và tính di động. Chương 8 đề cập đến vấn đề bảo mật trong mạng máy tính, trước tiên xem xét nền tảng của mã hóa và bảo mật mạng, sau đó chúng ta xem xét lý thuyết cơ bản đang được áp dụng như thế nào trong nhiều bối cảnh Internet.

**Bài tập về nhà vấn đề và câu hỏi**

Câu hỏi ôn tập chương 1

MỤC 1.1 R1. Sự khác biệt giữa máy chủ và hệ thống đầu cuối là gì? Liệt kê một số khác nhau-

các loại hệ thống đầu cuối. Máy chủ Web có phải là hệ thống đầu cuối không? R2. Từ giao thức thường được sử dụng để mô tả quan hệ ngoại giao. Làm thế nào

Wikipedia mô tả nghi thức ngoại giao? R3. Tại sao các tiêu chuẩn lại quan trọng đối với các giao thức?

MỤC 1.2 R4. Liệt kê bốn công nghệ truy cập. Phân loại từng người là truy cập gia đình, doanh nghiệp

truy cập hoặc truy cập không dây diện rộng. R5. Tốc độ truyền HFC được dành riêng hay chia sẻ giữa những người dùng? Có va chạm

có thể xảy ra trong kênh HFC xuôi dòng? Tại sao hoặc tại sao không? R6. Liệt kê các công nghệ truy cập dân cư có sẵn trong thành phố của bạn. Đối với mỗi

loại quyền truy cập, cung cấp tốc độ xuôi dòng được quảng cáo, tốc độ ngược dòng và giá hàng tháng. R7. Tốc độ truyền của mạng LAN Ethernet là bao nhiêu? R8. Một số phương tiện vật lý mà Ethernet có thể chạy qua là gì? R9. HFC, DSL và FTTH đều được sử dụng để truy cập dân cư. Đối với mỗi

những công nghệ truy cập này cung cấp một loạt các tốc độ truyền và nhận xét liệu tốc độ truyền được chia sẻ hay dành riêng. R10. Mô tả các công nghệ truy cập Internet không dây phổ biến nhất hiện nay.

So sánh và đối chiếu chúng.

CÁC BÀI TẬP VÀ CÂU HỎI về bài tập về nhà 67

MỤC 1.3 R11. Giả sử có chính xác một chuyển mạch gói giữa máy chủ gửi và máy chủ

máy chủ nhận. Tốc độ truyền giữa máy chủ gửi và bộ chuyển mạch và giữa bộ chuyển mạch và máy chủ nhận lần lượt là R1 và R2. Giả sử rằng switch sử dụng chuyển mạch gói lưu trữ và chuyển tiếp, tổng độ trễ từ đầu đến cuối để gửi một gói có độ dài L là bao nhiêu? (Bỏ qua hàng đợi, độ trễ lan truyền và độ trễ xử lý.) R12. Mạng chuyển mạch kênh có ưu điểm gì so với mạng chuyển mạch gói?

công việc? TDM có những ưu điểm gì so với FDM trong mạng chuyển mạch kênh? R13. Giả sử người dùng chia sẻ liên kết 2 Mbps. Ngoài ra, giả sử mỗi người dùng truyền liên tục

tốc độ tối đa là 1 Mbps khi truyền, nhưng mỗi người dùng chỉ truyền 20% thời gian. (Xem phần thảo luận về ghép kênh thống kê ở Phần 1.3.) a. Khi sử dụng chuyển mạch, có thể hỗ trợ bao nhiêu người dùng? b. Đối với phần còn lại của vấn đề này, giả sử chuyển mạch gói được sử dụng. Tại sao

về cơ bản sẽ không có độ trễ xếp hàng trước liên kết nếu hai hoặc ít người dùng truyền cùng một lúc? Tại sao sẽ có độ trễ xếp hàng nếu ba người dùng truyền cùng một lúc? c. Tìm xác suất mà một người dùng nhất định đang truyền. d. Giả sử bây giờ có ba người dùng. Tìm xác suất để tại bất kỳ thời điểm nào

thời gian, cả ba người dùng đều truyền đồng thời. Tìm khoảng thời gian mà hàng đợi tăng lên. R14. Tại sao hai ISP ở cùng cấp độ phân cấp thường ngang hàng với nhau

khác? IXP kiếm tiền bằng cách nào? R15. Một số nhà cung cấp nội dung đã tạo ra mạng lưới riêng của họ. Mô tả Google

mạng. Điều gì thúc đẩy các nhà cung cấp nội dung tạo ra các mạng này?

MỤC 1.4 R16. Xem xét việc gửi một gói từ máy chủ nguồn đến máy chủ đích qua

tuyến đường cố định. Liệt kê các thành phần độ trễ trong độ trễ đầu cuối. Độ trễ nào trong số này là không đổi và độ trễ nào có thể thay đổi? R17. Truy cập hoạt hình tương tác Độ trễ truyền so với lan truyền tại

trang Web đồng hành. Trong số các tốc độ, độ trễ truyền và kích thước gói có sẵn, hãy tìm một sự kết hợp mà người gửi kết thúc việc truyền trước khi bit đầu tiên của gói đến được người nhận. Tìm một sự kết hợp khác mà bit đầu tiên của gói đến được người nhận trước khi người gửi kết thúc việc truyền. R18. Mất bao lâu để một gói có độ dài 1.000 byte được truyền trên một

**Khoảng cách liên kết 2.500 km, tốc độ truyền 2,5 \# 108 m/s và tốc độ truyền 2 Mbps? Tổng quát hơn, mất bao lâu để một gói có độ dài L được truyền qua một liên kết có khoảng cách d, tốc độ truyền s và đường truyền**

tốc độ R bps? Độ trễ này có phụ thuộc vào độ dài gói không? Độ trễ này có phụ thuộc vào tốc độ truyền không? R19. Giả sử Host A muốn gửi một tệp lớn tới Host B. Đường dẫn từ Host A đến Host

B có ba liên kết, tốc độ R1 = 500 kbps, R2 = 2 Mbps và R3 = 1 Mbps. Một. Giả sử không có lưu lượng nào khác trong mạng, thông lượng của

chuyển tập tin? b. Giả sử tệp có kích thước 4 triệu byte. Chia kích thước tệp cho thông qua-

đặt, sẽ mất khoảng bao lâu để chuyển tệp tới Host B? c. Lặp lại (a) và (b), nhưng bây giờ với R2 giảm xuống 100 kbps. R20. Giả sử hệ thống cuối A muốn gửi một tệp lớn đến hệ thống cuối B. Tại một thời điểm rất

mức cao, mô tả cách hệ thống cuối A tạo các gói từ tệp. Khi một trong những gói này đến bộ định tuyến, bộ định tuyến sẽ sử dụng thông tin gì trong gói để xác định liên kết mà gói được chuyển tiếp? Tại sao việc chuyển mạch gói trên Internet lại giống như việc lái xe từ thành phố này sang thành phố khác và hỏi đường trên đường đi? R21. Truy cập hoạt ảnh tương tác Xếp hàng và Mất mát tại trang Web đồng hành.

Tốc độ phát thải tối đa và tốc độ truyền tối thiểu là bao nhiêu? Với những mức giá đó, cường độ giao thông là bao nhiêu? Chạy hoạt ảnh tương tác với các tốc độ này và xác định xem mất bao lâu để xảy ra mất gói. Sau đó lặp lại thử nghiệm lần thứ hai và xác định lại xem mất bao lâu để xảy ra mất gói. Các giá trị có khác nhau không? Tại sao hoặc tại sao không?

MỤC 1.5 R22. Liệt kê năm nhiệm vụ mà một lớp có thể thực hiện. Có thể là một (hoặc nhiều) trong số

những nhiệm vụ này có thể được thực hiện bởi hai (hoặc nhiều) lớp? R23. Năm lớp trong ngăn xếp giao thức Internet là gì? Hiệu trưởng là gì

trách nhiệm của từng lớp này? R24. Thông báo lớp ứng dụng là gì? Một phân đoạn lớp vận chuyển? Một mạng lưới-

datagram lớp công việc? Khung lớp liên kết? R25. Bộ định tuyến xử lý những lớp nào trong ngăn xếp giao thức Internet? Nằm nào-

ers có thực hiện quá trình chuyển đổi lớp liên kết không? Máy chủ xử lý những lớp nào?

MỤC 1.6

R26. Phần mềm độc hại tự sao chép là gì? R27. Mô tả cách tạo botnet và cách sử dụng nó để tấn công DDoS. R28. Giả sử Alice và Bob đang gửi gói tin cho nhau qua máy tính

mạng. Giả sử Trudy định vị mình trong mạng để cô ấy có thể nắm bắt tất cả các gói do Alice gửi và gửi bất cứ thứ gì cô ấy muốn cho Bob; cô ấy cũng có thể nắm bắt tất cả các gói tin do Bob gửi và gửi bất cứ thứ gì cô ấy muốn cho Alice. Liệt kê một số điều ác độc mà Trudy có thể làm từ vị trí này.

VẤN ĐỀ 69

**Vấn đề**

P1. Thiết kế và mô tả một giao thức cấp ứng dụng được sử dụng giữa một

máy rút tiền tự động và máy tính tập trung của ngân hàng. Giao thức của bạn phải cho phép xác minh thẻ và mật khẩu của người dùng, truy vấn số dư tài khoản (được duy trì tại máy tính tập trung) và thực hiện rút tiền tài khoản (nghĩa là tiền được giải ngân cho người dùng). Các thực thể giao thức của bạn sẽ có thể xử lý trường hợp quá phổ biến khi không có đủ tiền trong tài khoản để chi trả cho việc rút tiền. Chỉ định giao thức của bạn bằng cách liệt kê các tin nhắn được trao đổi và hành động được thực hiện bởi máy rút tiền tự động hoặc máy tính tập trung của ngân hàng trong việc truyền và nhận tin nhắn. Phác thảo hoạt động của giao thức của bạn trong trường hợp rút tiền đơn giản không có lỗi, sử dụng sơ đồ tương tự như trong Hình 1.2. Nêu rõ các giả định mà giao thức của bạn đưa ra về dịch vụ truyền tải cơ bản từ đầu đến cuối. P2. Phương trình 1.1 đưa ra công thức tính độ trễ từ đầu đến cuối của việc gửi một gói

có độ dài L trên N liên kết có tốc độ truyền R. Tổng quát hóa công thức này để gửi P các gói như vậy nối tiếp nhau qua N liên kết. P3. Hãy xem xét một ứng dụng truyền dữ liệu với tốc độ ổn định (ví dụ:

người gửi tạo ra một đơn vị dữ liệu N-bit cứ sau k đơn vị thời gian, trong đó k nhỏ và cố định). Ngoài ra, khi một ứng dụng như vậy khởi động, nó sẽ tiếp tục chạy trong một khoảng thời gian tương đối dài. Trả lời các câu hỏi sau, chứng minh ngắn gọn câu trả lời của bạn: a. Mạng chuyển mạch gói hay mạng chuyển mạch kênh sẽ phù hợp hơn?

thích hợp cho ứng dụng này? Tại sao? b. Giả sử rằng mạng chuyển mạch gói được sử dụng và lưu lượng duy nhất trong

mạng này đến từ các ứng dụng như được mô tả ở trên. Hơn nữa, giả sử rằng tổng tốc độ dữ liệu của ứng dụng nhỏ hơn dung lượng của mỗi liên kết. Có cần một số hình thức kiểm soát tắc nghẽn không? Tại sao? P4. Hãy xem xét mạng chuyển mạch kênh trong Hình 1.13. Hãy nhớ lại rằng có

bốn mạch trên mỗi liên kết. Dán nhãn cho bốn công tắc A, B, C và D theo chiều kim đồng hồ. Một. Số lượng kết nối đồng thời tối đa có thể có trong

tiến triển bất cứ lúc nào trong mạng này? b. Giả sử rằng tất cả các kết nối đều nằm giữa các công tắc A và C.

số lượng kết nối đồng thời tối đa có thể được thực hiện? c. Giả sử chúng ta muốn tạo bốn kết nối giữa các công tắc A và C,

và bốn kết nối khác giữa các thiết bị chuyển mạch B và D. Chúng ta có thể định tuyến các cuộc gọi này qua bốn liên kết để đáp ứng tất cả tám kết nối không?

P5. Xem lại sự tương tự giữa ô tô và đoàn lữ hành ở Phần 1.4. Giả sử tốc độ lan truyền

là 100 km/giờ. Một. Giả sử đoàn lữ hành đi được 175 km, bắt đầu trước một trạm thu phí,

đi qua trạm thu phí thứ hai và kết thúc ngay sau trạm thu phí thứ ba. Độ trễ từ đầu đến cuối là gì? b. Lặp lại (a), bây giờ giả sử rằng có tám chiếc xe trong đoàn lữ hành

thường. P6. Vấn đề cơ bản này bắt đầu khám phá độ trễ lan truyền và truyền

độ trễ sion, hai khái niệm trung tâm trong mạng dữ liệu. Xét hai máy chủ A và B được kết nối bằng một liên kết duy nhất có tốc độ R bps. Giả sử hai máy chủ cách nhau m mét và giả sử tốc độ truyền dọc theo liên kết là s mét/giây. Host A là gửi một gói có kích thước L bit tới Host B. a. Biểu thị độ trễ lan truyền, dprop, theo m và s. b. Xác định thời gian truyền của gói dtrans theo L và R. c. Bỏ qua độ trễ xử lý và xếp hàng, thu được biểu thức cho kết thúc-

độ trễ từ đầu đến cuối. d. Giả sử Host A bắt đầu truyền gói tin tại thời điểm t = 0. Tại thời điểm t =

dtrans, bit cuối cùng của gói ở đâu? đ. Giả sử dprop lớn hơn dtrans. Tại thời điểm t = dtrans thì đâu là điểm đầu tiên?

chút của gói? f. Giả sử dprop nhỏ hơn dtrans. Tại thời điểm t = dtrans, bit đầu tiên của

**gói tin? g. Giả sử s = 2,5 #108, L = 1500 byte và R = 10 Mbps. Tìm**

khoảng cách m sao cho dprop bằng dtrans. P7. Trong vấn đề này, chúng tôi xem xét việc gửi giọng nói theo thời gian thực từ Host A tới Host B

qua mạng chuyển mạch gói (VoIP). Host Chuyển đổi giọng nói tương tự thành luồng bit kỹ thuật số 64 kbps một cách nhanh chóng. Host A sau đó nhóm các bit thành các gói 56 byte. Có một liên kết giữa Hosts A và B; tốc độ truyền của nó là 10 Mbps và độ trễ lan truyền của nó là 10 mili giây. Ngay khi Host A thu thập một gói, nó sẽ gửi gói đó đến Host B. Ngay sau khi Host B nhận được toàn bộ gói, nó sẽ chuyển đổi các bit của gói thành tín hiệu tương tự. Bao nhiêu thời gian trôi qua kể từ khi một bit được tạo ra (từ tín hiệu tương tự ban đầu tại Host A) cho đến khi bit được giải mã (như một phần của tín hiệu tương tự tại Host B)? P8. Giả sử người dùng chia sẻ liên kết 10 Mbps. Cũng giả sử mỗi người dùng yêu cầu 200 kbps

khi truyền, nhưng mỗi người dùng chỉ truyền 10% thời gian. (Xem phần thảo luận về chuyển mạch gói và chuyển mạch kênh ở Phần 1.3.) a. Khi sử dụng chuyển mạch, có thể hỗ trợ bao nhiêu người dùng? b. Đối với phần còn lại của vấn đề này, giả sử chuyển mạch gói được sử dụng. Tìm thấy

xác suất mà một người dùng nhất định đang truyền tải.

Khám phá độ trễ lan truyền và độ trễ truyền

VideoLưu ý

VẤN ĐỀ 71

c\. Giả sử có 120 người dùng. Tìm xác suất để tại thời điểm bất kỳ,

chính xác n người dùng đang truyền tải đồng thời. (Gợi ý: Sử dụng phân phối nhị thức.) d. Tìm xác suất để có 51 người dùng trở lên truyền

đồng thời. P9. Hãy xem xét thảo luận trong Phần 1.3 về chuyển mạch gói và chuyển mạch kênh-

trong đó một ví dụ được cung cấp với liên kết 1 Mbps. Người dùng đang tạo dữ liệu với tốc độ 100 kbps khi bận nhưng chỉ bận tạo dữ liệu với xác suất p = 0,1. Giả sử rằng liên kết 1 Mbps được thay thế bằng liên kết 1 Gbps. Một. N là gì, số lượng người dùng tối đa có thể được hỗ trợ đồng thời

đang chuyển mạch một cách thận trọng? b. Bây giờ hãy xem xét chuyển mạch gói và số lượng người dùng M người dùng. Cho một

công thức (theo p, M, N) cho xác suất có nhiều hơn N người dùng đang gửi dữ liệu. P10. Xét một gói có độ dài L bắt đầu ở hệ thống đầu cuối A và truyền qua

**ba liên kết đến một hệ thống đích. Ba liên kết này được kết nối bằng hai chuyển mạch gói. Đặt di, si và Ri biểu thị độ dài, tốc độ truyền và tốc độ truyền của liên kết i, với i = 1, 2, 3. Bộ chuyển mạch gói làm trễ mỗi gói theo dproc. Giả sử không có độ trễ xếp hàng, theo di, si, Ri, (i = 1, 2, 3) và L, tổng độ trễ từ đầu đến cuối của gói là bao nhiêu? Giả sử bây giờ gói là 1.500 byte, tốc độ truyền trên cả ba liên kết là 2,5 \# 108m/s, tốc độ truyền của cả ba liên kết là 2,5 Mbps, độ trễ xử lý chuyển mạch gói là 3 ms, độ dài của liên kết đầu tiên là 5.000 km, chiều dài của liên kết thứ hai là 4.000 km và độ dài của liên kết cuối cùng là 1.000 km. Đối với những giá trị này, độ trễ từ đầu đến cuối là bao nhiêu? P11. Trong bài toán trên, giả sử R1 = R2 = R3 = R và dproc = 0. Hơn nữa**

Giả sử rằng bộ chuyển mạch gói không lưu trữ và chuyển tiếp các gói mà thay vào đó truyền ngay lập tức từng bit mà nó nhận được trước khi đợi toàn bộ gói đến. Độ trễ từ đầu đến cuối là gì? P12. Bộ chuyển mạch gói nhận một gói và xác định liên kết ngoài mà nó

gói tin cần được chuyển tiếp. Khi gói đến, một gói khác đã được truyền đi một nửa trên liên kết ngoài này và bốn gói khác đang chờ được truyền. Packets được truyền theo thứ tự đến. Giả sử tất cả các gói đều có kích thước 1.500 byte và tốc độ liên kết là 2,5 Mbps. Độ trễ xếp hàng cho gói là bao nhiêu? Tổng quát hơn, độ trễ xếp hàng là bao nhiêu khi tất cả các gói có độ dài L, tốc độ truyền là R, x bit của gói hiện đang được truyền đã được truyền và n gói đã có trong hàng đợi? P13. (a) Giả sử N gói đến đồng thời tới một liên kết mà tại đó không có gói nào

hiện đang được truyền đi hoặc xếp hàng đợi. Mỗi gói có độ dài L và liên kết có tốc độ truyền R. Độ trễ xếp hàng trung bình của N gói là bao nhiêu?

\(b\) Bây giờ giả sử rằng N gói như vậy đến liên kết sau mỗi LN/R giây.

Độ trễ xếp hàng trung bình của một gói là bao nhiêu? P14. Hãy xem xét độ trễ xếp hàng trong bộ đệm của bộ định tuyến. Hãy để tôi biểu thị cường độ giao thông;

nghĩa là I = La/R. Giả sử độ trễ xếp hàng có dạng IL/R (1 - I) đối với I 6 1. a. Cung cấp công thức tính độ trễ tổng cộng, nghĩa là độ trễ hàng đợi cộng với

độ trễ truyền tải. b. Vẽ tổng độ trễ dưới dạng hàm của L /R. P15. Gọi a biểu thị tốc độ các gói đến một liên kết tính bằng gói/giây và đặt µ

biểu thị tốc độ truyền của liên kết tính bằng gói/giây. Dựa vào công thức tính độ trễ tổng cộng (tức là độ trễ xếp hàng cộng với độ trễ truyền) rút ra từ bài toán trước, rút ​​ra công thức tính độ trễ tổng theo a và µ. P16. Hãy xem xét bộ đệm của bộ định tuyến trước một liên kết ngoài. Trong vấn đề này, bạn

**sẽ sử dụng công thức Little, một công thức nổi tiếng từ lý thuyết xếp hàng. Gọi N là số gói trung bình trong bộ đệm cộng với gói được truyền. Gọi a biểu thị tốc độ các gói đến liên kết. Gọi d biểu thị tổng độ trễ trung bình (tức là độ trễ xếp hàng cộng với độ trễ truyền) mà một gói gặp phải. Công thức Little là N = a \# d. Giả sử trung bình bộ đệm chứa 100 gói và độ trễ xếp hàng gói trung bình là 20 ms. Tốc độ truyền của liên kết là 100 gói/giây. Sử dụng công thức Little, tốc độ đến trung bình của gói là bao nhiêu, giả sử không có gói bị mất? P17. Một. Tổng quát hóa phương trình 1.2 ở mục 1.4.3 cho xử lý không đồng nhất**

tốc độ, tốc độ truyền và độ trễ lan truyền. b. Lặp lại (a), nhưng bây giờ cũng giả sử rằng có độ trễ xếp hàng trung bình là

dqueue tại mỗi nút. P18. Thực hiện Traceroute giữa nguồn và đích trên cùng một lục địa

vào ba giờ khác nhau trong ngày. Một. Tìm độ lệch trung bình và độ lệch chuẩn của độ trễ khứ hồi tại mỗi

ba giờ. b. Tìm số lượng bộ định tuyến trên đường đi vào mỗi thời điểm trong ba giờ. đã làm

đường dẫn thay đổi trong bất kỳ giờ nào? c. Cố gắng xác định số lượng mạng ISP mà gói Traceroute

đi từ nguồn tới đích. Routers có tên và/hoặc địa chỉ IP tương tự sẽ được coi là một phần của cùng một ISP. Trong thử nghiệm của bạn, độ trễ lớn nhất có xảy ra ở các giao diện ngang hàng giữa các ISP lân cận không? d. Lặp lại những điều trên cho nguồn và đích ở các châu lục khác nhau.

So sánh kết quả giữa các lục địa và liên lục địa.

Sử dụng Traceroute để khám phá đường dẫn mạng và đo độ trễ mạng

VideoLưu ý

VẤN ĐỀ 73

P19. Định luật Metcalfe phát biểu rằng giá trị của một mạng máy tính tỷ lệ thuận với

bình phương số lượng người dùng được kết nối của hệ thống. Gọi n là số lượng người dùng trong mạng máy tính. Giả sử mỗi người dùng gửi một tin nhắn cho mỗi người dùng khác thì sẽ gửi bao nhiêu tin nhắn? Câu trả lời của bạn có ủng hộ định luật Metcalfe không?

P20. Hãy xem ví dụ về thông lượng tương ứng với Hình 1.20(b). Hiện nay

giả sử rằng có M cặp máy khách-máy chủ chứ không phải 10. Ký hiệu Rs, Rc và R cho tốc độ của các liên kết máy chủ, liên kết máy khách và liên kết mạng. Giả sử tất cả các liên kết khác có dung lượng dồi dào và không có lưu lượng nào khác trong mạng ngoài lưu lượng được tạo bởi cặp máy khách-máy chủ M. Rút ra biểu thức tổng quát về thông lượng theo Rs, Rc, R và M.

P21. Hãy xem xét Hình 1.19(b). Bây giờ giả sử có M đường đi giữa

máy chủ và máy khách. Không có hai con đường chia sẻ bất kỳ liên kết nào. Đường dẫn k (k = 1, c, M) gồm N liên kết có tốc độ truyền Rk

1, Rk 2, c, Rk N. Nếu máy chủ chỉ có thể sử dụng một đường dẫn để gửi dữ liệu đến máy khách thì thông lượng tối đa mà máy chủ có thể đạt được là bao nhiêu? Nếu máy chủ có thể sử dụng tất cả M đường dẫn để gửi dữ liệu thì thông lượng tối đa mà máy chủ có thể đạt được là bao nhiêu?

P22. Hãy xem xét Hình 1.19(b). Giả sử rằng mỗi liên kết giữa máy chủ và

khách hàng có xác suất mất gói p và xác suất mất gói cho các liên kết này là độc lập. Xác suất để một gói tin (được gửi bởi máy chủ) được người nhận nhận thành công là bao nhiêu? Nếu một gói bị mất trên đường dẫn từ máy chủ đến máy khách thì máy chủ sẽ truyền lại gói đó. Trung bình, máy chủ sẽ truyền lại gói bao nhiêu lần để máy khách nhận được gói thành công?

P23. Hãy xem xét Hình 1.19(a). Giả sử rằng chúng ta biết liên kết thắt cổ chai dọc theo

đường dẫn từ máy chủ đến máy khách là liên kết đầu tiên có tốc độ Rs bit/giây. Giả sử chúng ta gửi một cặp gói liên tục từ máy chủ đến máy khách và không có lưu lượng truy cập nào khác trên đường dẫn này. Giả sử mỗi gói có kích thước L bit và cả hai liên kết đều có cùng độ trễ lan truyền dprop. Một. Thời gian giữa các gói tin đến đích là bao nhiêu? Tức là bao nhiêu

thời gian trôi qua kể từ khi bit cuối cùng của gói đầu tiên đến cho đến khi bit cuối cùng của gói thứ hai đến? b. Bây giờ giả sử rằng liên kết thứ hai là liên kết thắt cổ chai (tức là Rc 6 Rs). Là

có thể hàng đợi gói thứ hai ở hàng đợi đầu vào của liên kết thứ hai? Giải thích. Bây giờ giả sử máy chủ gửi gói thứ hai T giây sau khi gửi gói đầu tiên. T phải lớn đến mức nào để đảm bảo không phải xếp hàng trước liên kết thứ hai? Giải thích.

P24. Giả sử bạn muốn chuyển gấp dữ liệu 50 terabyte từ Boston tới

Los Angeles. Bạn có sẵn một liên kết chuyên dụng 100 Mbps để truyền dữ liệu. Bạn muốn truyền dữ liệu qua liên kết này hay thay vào đó sử dụng dịch vụ chuyển phát qua đêm của FedEx? Giải thích.

P25. Giả sử hai máy chủ A và B cách nhau 20.000 km và có cùng

**được kết nối bởi một liên kết trực tiếp có tốc độ R = 5 Mbps. Giả sử tốc độ truyền qua liên kết là 2,5 #108 mét/giây. Một. Tính tích độ trễ băng thông, R#dprop. b. Hãy xem xét việc gửi một tệp 800.000 bit từ Host A đến Host B. Giả sử**

tập tin được gửi liên tục dưới dạng một tin nhắn lớn. Số bit tối đa sẽ có trong liên kết tại bất kỳ thời điểm nào là bao nhiêu? c. Cung cấp giải thích về tích độ trễ băng thông. d. Chiều rộng (tính bằng mét) của một bit trong liên kết là bao nhiêu? Nó dài hơn một

sân bóng? đ. Rút ra biểu thức tổng quát cho độ rộng của một bit theo

tốc độ truyền s, tốc độ truyền R và độ dài của liên kết m.

P26. Đề cập đến bài toán P24, giả sử chúng ta có thể sửa đổi R. Với giá trị nào của R là

chiều rộng một chút dài bằng chiều dài của liên kết?

P27. Hãy xem xét vấn đề P24 nhưng bây giờ có liên kết R = 500 Mbps.

**Một. Tính tích độ trễ băng thông, R#dprop. b. Hãy xem xét việc gửi một tệp 800.000 bit từ Host A đến Host B. Giả sử**

tập tin được gửi liên tục dưới dạng một tin nhắn lớn. Số bit tối đa sẽ có trong liên kết tại bất kỳ thời điểm nào là bao nhiêu? c. Chiều rộng (tính bằng mét) của một bit trong liên kết là bao nhiêu?

P28. Tham khảo lại bài P24.

Một. Mất bao lâu để gửi tập tin, giả sử nó được gửi liên tục? b. Giả sử bây giờ file được chia thành 20 gói với mỗi gói

chứa 40.000 bit. Giả sử mỗi gói được người nhận xác nhận và thời gian truyền của gói xác nhận là không đáng kể. Cuối cùng, giả sử rằng người gửi không thể gửi gói tin cho đến khi gói tin trước đó được xác nhận. Mất bao lâu để gửi tập tin? c. So sánh kết quả từ (a) và (b).

P29. Giả sử có một liên kết vi sóng 10 Mbps giữa một thiết bị địa tĩnh

**vệ tinh và trạm gốc của nó trên Trái đất. Mỗi phút vệ tinh sẽ chụp một bức ảnh kỹ thuật số và gửi nó đến trạm gốc. Giả sử tốc độ lan truyền là 2,4 \# 108 mét/giây. Một. Độ trễ lan truyền của liên kết là gì? b. Sản phẩm độ trễ băng thông, R \# dprop là gì? c. Gọi x là kích thước của bức ảnh. Giá trị nhỏ nhất của x là bao nhiêu**

liên kết vi sóng được truyền liên tục?

VẤN ĐỀ 75

P30. Hãy xem xét sự tương tự của du lịch hàng không trong phần thảo luận của chúng ta về việc phân lớp ở Phần 1.5,

và việc bổ sung các tiêu đề vào các đơn vị dữ liệu giao thức khi chúng chảy xuống ngăn xếp giao thức. Có khái niệm tương đương về thông tin tiêu đề được thêm vào hành khách và hành lý khi họ di chuyển xuống ngăn xếp giao thức hàng không không? P31. Trong các mạng chuyển mạch gói hiện đại, bao gồm cả Internet, phân đoạn máy chủ nguồn

dài, các tin nhắn ở lớp ứng dụng (ví dụ: một hình ảnh hoặc một tệp nhạc) thành các gói nhỏ hơn và gửi các gói đó vào mạng. Người nhận sau đó tập hợp lại các gói tin thành tin nhắn ban đầu. Chúng tôi gọi quá trình này là phân đoạn tin nhắn. Hình 1.27 minh họa việc vận chuyển một tin nhắn từ đầu đến cuối có và không có phân đoạn tin nhắn. Hãy xem xét một thông báo dài 106 bit được gửi từ nguồn tới đích trong Hình 1.27. Giả sử mỗi liên kết trong hình là 5 Mbps. Bỏ qua sự lan truyền, xếp hàng và độ trễ xử lý. Một. Cân nhắc gửi tin nhắn từ nguồn tới đích mà không cần tin nhắn

sự phân đoạn. Mất bao lâu để chuyển tin nhắn từ máy chủ nguồn sang gói chuyển mạch đầu tiên? Hãy nhớ rằng mỗi switch sử dụng tính năng chuyển mạch gói lưu trữ và chuyển tiếp, tổng thời gian để di chuyển tin nhắn từ máy chủ nguồn đến máy chủ đích là bao nhiêu? b. Bây giờ giả sử thông điệp được phân thành 100 gói, mỗi gói

gói có độ dài 10.000 bit. Mất bao lâu để chuyển gói đầu tiên từ máy chủ nguồn sang bộ chuyển mạch đầu tiên? Khi gói đầu tiên được gửi từ bộ chuyển mạch thứ nhất sang bộ chuyển mạch thứ hai, gói thứ hai sẽ được gửi từ máy chủ nguồn đến bộ chuyển mạch đầu tiên. Lúc nào gói thứ hai sẽ được nhận đầy đủ ở lần chuyển mạch đầu tiên? c. Mất bao lâu để di chuyển tệp từ máy chủ nguồn đến đích

máy chủ khi phân đoạn tin nhắn được sử dụng? So sánh kết quả này với câu trả lời của bạn ở phần (a) và nhận xét.

*Hình 1.27 ♦ Vận chuyển tin nhắn end-to-end: (a) không có tin nhắn*

phân đoạn; (b) với phân đoạn tin nhắn

Nguồn A. Packet chuyển đổi Packet chuyển đổi Đích

Tin nhắn

Nguồnb. Packet chuyển đổi

Packet

Packet chuyển đổi Đích

d\. Ngoài việc giảm độ trễ, lý do nào để sử dụng tin nhắn

phân đoạn? đ. Thảo luận về những hạn chế của việc phân đoạn tin nhắn. P32. Thử nghiệm với hoạt ảnh tương tác Phân đoạn tin nhắn ở phần cuối của cuốn sách

Trang web. Độ trễ trong hoạt ảnh tương tác có tương ứng với độ trễ trong bài toán trước không? Độ trễ truyền liên kết ảnh hưởng như thế nào đến độ trễ tổng thể từ đầu đến cuối đối với chuyển mạch gói (với phân đoạn tin nhắn) và đối với chuyển đổi tin nhắn? P33. Hãy cân nhắc gửi một tệp lớn F bit từ Host A đến Host B. Có ba

các liên kết (và hai thiết bị chuyển mạch) giữa A và B và các liên kết này không bị tắc nghẽn (nghĩa là không có độ trễ xếp hàng). Host Phân đoạn tệp thành các phân đoạn có S bit và thêm 80 bit tiêu đề vào mỗi phân đoạn, tạo thành các gói L = 80 + S bit. Mỗi liên kết có tốc độ truyền R bps. Tìm giá trị của S để giảm thiểu độ trễ khi di chuyển tệp từ Host A đến Host B. Bỏ qua độ trễ truyền. P34. Skype cung cấp một dịch vụ cho phép bạn thực hiện cuộc gọi điện thoại từ máy tính đến máy

điện thoại thông thường. Điều này có nghĩa là cuộc gọi thoại phải truyền qua cả Internet và qua mạng điện thoại. Thảo luận về cách điều này có thể được thực hiện.

**Wireshark Phòng thí nghiệm**

\"Nói với tôi và tôi quên. Cho tôi xem và tôi nhớ. Cho tôi tham gia và tôi hiểu.\"

Tục ngữ Trung Quốc

Sự hiểu biết của một người về các giao thức mạng thường có thể được nâng cao đáng kể bằng cách xem chúng hoạt động và thử nghiệm với chúng---quan sát chuỗi tin nhắn được trao đổi giữa hai thực thể giao thức, đi sâu vào chi tiết về hoạt động của giao thức, khiến các giao thức thực hiện một số hành động nhất định và quan sát những hành động này cũng như hậu quả của chúng. Điều này có thể được thực hiện trong các tình huống mô phỏng hoặc trong môi trường mạng thực như Internet. Các hình ảnh động tương tác trên trang Web sách giáo khoa áp dụng cách tiếp cận đầu tiên. Trong phòng thí nghiệm Wireshark, chúng tôi sẽ áp dụng phương pháp thứ hai. Bạn sẽ chạy các ứng dụng mạng trong nhiều tình huống khác nhau bằng cách sử dụng máy tính trên bàn làm việc, ở nhà hoặc trong phòng thí nghiệm. Bạn sẽ quan sát các giao thức mạng trong máy tính của mình, tương tác và trao đổi tin nhắn với các thực thể giao thức đang thực thi ở nơi khác trên Internet. Vì vậy, bạn và máy tính của bạn sẽ là một phần không thể thiếu trong các phòng thí nghiệm trực tiếp này. Bạn sẽ quan sát---và bạn sẽ học hỏi---bằng cách thực hành.

Công cụ cơ bản để quan sát các thông điệp được trao đổi giữa các thực thể giao thức đang thực thi được gọi là packet sniffer. Đúng như tên gọi, trình thám thính gói sẽ sao chép (đánh hơi) các tin nhắn được máy tính của bạn gửi và nhận một cách thụ động; nó cũng hiển thị nội dung của các trường giao thức khác nhau của các tin nhắn được ghi lại này. Ảnh chụp màn hình của trình thám thính gói Wireshark được hiển thị trong Hình 1.28. Wireshark là một

PHÒNG THÍ NGHIỆM WIRESHARK 77

trình thám thính gói miễn phí chạy trên máy tính Windows, Linux/Unix và Mac. Xuyên suốt cuốn sách này, bạn sẽ tìm thấy Wireshark phòng thí nghiệm cho phép bạn khám phá một số giao thức được nghiên cứu trong chương. Trong phòng thí nghiệm Wireshark đầu tiên này, bạn sẽ lấy và cài đặt bản sao của Wireshark, truy cập một trang Web, nắm bắt và kiểm tra các thông báo giao thức được trao đổi giữa trình duyệt Web của bạn và máy chủ Web.

Bạn có thể tìm thấy thông tin chi tiết đầy đủ về phòng thí nghiệm Wireshark đầu tiên này (bao gồm hướng dẫn về cách lấy và cài đặt Wireshark) tại trang Web www.pearson.com/cs-resources.

*Hình 1.28 ♦ Một ảnh chụp màn hình Wireshark (Wireshark ảnh chụp màn hình được in lại*

được sự cho phép của Quỹ Wireshark.)

Menu lệnh

Danh sách các gói bị bắt

Chi tiết về tiêu đề gói đã chọn

Packet nội dung ở dạng thập lục phân và ASCII

![](media/image4.png){width="5.5in" height="3.776666666666667in"}

![](media/image5.png){width="5.5in" height="3.776666666666667in"}

Điều gì khiến bạn quyết định chuyên về công nghệ mạng/Internet?

Khi còn là nghiên cứu sinh tiến sĩ tại MIT vào năm 1959, tôi đã nhìn xung quanh và thấy rằng hầu hết các bạn cùng lớp của tôi đang nghiên cứu trong lĩnh vực lý thuyết thông tin và lý thuyết mã hóa do nhà nghiên cứu vĩ đại Claude Shannon sáng lập. Tôi đánh giá rằng anh ấy đã giải quyết được hầu hết các vấn đề quan trọng rồi. Những vấn đề nghiên cứu còn lại rất khó và đối với tôi dường như ít gây hậu quả hơn. Vì vậy, tôi quyết định dấn thân vào một lĩnh vực mới mà chưa có ai nghĩ tới. Thật hạnh phúc, tại MIT, xung quanh tôi có rất nhiều máy tính, và tôi thấy rõ rằng sớm hay muộn những chiếc máy này sẽ cần liên lạc với nhau. Vào thời điểm đó, không có cách nào hiệu quả để họ làm như vậy và giải pháp cho vấn đề quan trọng này sẽ có tác động. Tôi đã có cách tiếp cận vấn đề này và vì vậy, trong nghiên cứu Tiến sĩ của mình, tôi quyết định tạo ra một lý thuyết toán học để lập mô hình, đánh giá, thiết kế và tối ưu hóa các mạng dữ liệu hiệu quả và đáng tin cậy.

Công việc đầu tiên của bạn trong ngành máy tính là gì? Nó đòi hỏi điều gì?

Tôi đã tham dự khóa học buổi tối tại CCNY từ năm 1951 đến năm 1957 để lấy bằng cử nhân kỹ thuật điện. Ban ngày, tôi làm việc đầu tiên với tư cách là kỹ thuật viên và sau đó là kỹ sư điện tại một công ty điện tử công nghiệp nhỏ tên là Photobell. Khi ở đó, tôi đã giới thiệu công nghệ kỹ thuật số cho dòng sản phẩm của họ. Về cơ bản, chúng tôi đang sử dụng các thiết bị quang điện để phát hiện sự hiện diện của một số vật phẩm nhất định (hộp, người, v.v.) và việc sử dụng mạch lúc đó được gọi là bộ dao động đa năng ổn định chính là thứ chúng tôi cần để đưa quy trình xử lý kỹ thuật số vào lĩnh vực phát hiện này. Những mạch này tình cờ là những khối xây dựng nên máy tính và được gọi là flip-flop hoặc công tắc trong tiếng địa phương ngày nay.

Điều gì đang diễn ra trong đầu bạn khi bạn gửi tin nhắn giữa các máy chủ đầu tiên (từ UCLA đến Viện nghiên cứu Stanford)?

Thành thật mà nói, chúng tôi không hề biết tầm quan trọng của sự kiện đó. Chúng ta đã không chuẩn bị một thông điệp đặc biệt có ý nghĩa lịch sử, như nhiều nhà phát minh trong quá khứ đã làm (Samuel Morse với "What hath God wrought." hay Alexander Graham Bell với "Watson, đến đây! Tôi muốn bạn." hay Neal Armstrong với "Đó là một bước đi nhỏ bé của một con người, nhưng là một bước nhảy vọt khổng lồ của nhân loại.") Những người đó thật thông minh! Họ hiểu truyền thông và quan hệ công chúng. Tất cả những gì chúng tôi muốn làm là chứng minh khả năng đăng nhập từ xa vào máy tính SRI. Vì vậy chúng tôi đã gõ chữ "L",

PHỎNG VẤN VỚI...

**Leonard Kleinrock**

Leonard Kleinrock là giáo sư khoa học máy tính tại Đại học California, Los Angeles. Năm 1969, máy tính của ông tại UCLA đã trở thành nút đầu tiên của Internet. Việc ông sáng tạo ra lý thuyết toán học về nguyên lý chuyển mạch gói vào năm 1961 đã trở thành công nghệ đằng sau Internet. Anh ấy đã nhận được B.E.E. từ City College of New York (CCNY) và bằng thạc sĩ và tiến sĩ về kỹ thuật điện của MIT.

Được phép của Leonard Kleinrock

![](media/image6.png){width="5.5in" height="7.228571741032371in"}

được nhận chính xác, chúng tôi gõ "o" được nhận chính xác, sau đó chúng tôi gõ "g" khiến máy chủ SRI gặp sự cố! Vì vậy, hóa ra thông điệp của chúng tôi là thông điệp ngắn nhất và có lẽ mang tính tiên tri nhất từ ​​​​trước đến nay, cụ thể là "Lo!" như trong \"Lo và kìa!\"

Đầu năm đó, tôi được trích dẫn trong một thông cáo báo chí của UCLA nói rằng một khi mạng đã hoạt động, chúng ta có thể truy cập vào các tiện ích máy tính từ nhà và văn phòng của mình một cách dễ dàng như khi chúng ta có quyền truy cập vào kết nối điện và điện thoại. Vì vậy, tầm nhìn của tôi lúc đó là Internet sẽ có mặt ở mọi nơi, luôn bật, luôn sẵn có, bất kỳ ai với bất kỳ thiết bị nào cũng có thể kết nối từ bất kỳ vị trí nào và nó sẽ vô hình. Tuy nhiên, tôi chưa bao giờ lường trước được rằng người mẹ 99 tuổi của tôi sẽ sử dụng Internet cùng lúc với đứa cháu gái 5 tuổi của tôi---và quả thực bà đã làm như vậy!

Tầm nhìn của bạn về tương lai của mạng là gì?

Phần dễ dàng của tầm nhìn là dự đoán chính cơ sở hạ tầng. Tôi dự đoán rằng chúng ta sẽ chứng kiến ​​sự triển khai đáng kể các thiết bị di động và không dây trong không gian thông minh để tạo ra thứ mà tôi muốn gọi là Internet Vô hình. Bước này sẽ cho phép chúng ta chuyển từ thế giới không gian ảo sang thế giới vật chất của không gian thông minh. Môi trường của chúng ta (bàn làm việc, tường, xe cộ, đồng hồ, thắt lưng, móng tay, cơ thể, v.v.) sẽ trở nên sống động nhờ công nghệ, thông qua bộ truyền động, cảm biến, logic, xử lý, lưu trữ, máy ảnh, micrô, loa, màn hình và giao tiếp. Công nghệ nhúng này sẽ cho phép môi trường của chúng ta cung cấp các dịch vụ IP ở bất cứ đâu và bất cứ khi nào chúng ta muốn. Khi tôi bước vào phòng, phòng sẽ biết tôi bước vào. Tôi sẽ có thể giao tiếp với môi trường của mình một cách tự nhiên, như bằng tiếng Anh nói, xúc giác, cử chỉ và cuối cùng là thông qua giao diện não-Internet; các yêu cầu của tôi sẽ tạo ra các câu trả lời hiển thị các trang Web cho tôi từ màn hình trên tường, qua kính mắt của tôi, dưới dạng lời nói, hình ảnh ba chiều, v.v. Nhìn xa hơn một chút, tôi thấy một tương lai mạng bao gồm các thành phần chính bổ sung sau. Tôi thấy các tác nhân phần mềm thông minh tùy chỉnh được triển khai trên mạng có chức năng khai thác dữ liệu, hành động dựa trên dữ liệu đó, quan sát xu hướng và thực hiện các nhiệm vụ một cách linh hoạt và thích ứng. Tôi thấy việc triển khai công nghệ chuỗi khối cung cấp sổ cái phân tán không thể chối cãi, không thể thay đổi cùng với hệ thống danh tiếng mang lại độ tin cậy cho nội dung và chức năng. Tôi thấy lưu lượng mạng được tạo ra nhiều hơn đáng kể không phải do con người mà do các thiết bị nhúng, các tác nhân phần mềm thông minh và sổ cái phân tán. Tôi thấy một bộ sưu tập lớn các hệ thống tự tổ chức đang kiểm soát mạng lưới rộng lớn và nhanh chóng này. Tôi thấy ngay lập tức một lượng lớn thông tin xuất hiện trên mạng này với thông tin này đang được xử lý và lọc rất lớn. Internet vô hình về cơ bản sẽ là một hệ thống thần kinh có sức lan tỏa toàn cầu. Tôi thấy tất cả những điều này và hơn thế nữa khi chúng ta tiến sâu vào thế kỷ XXI.

Phần khó hơn của tầm nhìn là dự đoán các ứng dụng và dịch vụ luôn làm chúng ta ngạc nhiên theo những cách ấn tượng (e-mail, công nghệ tìm kiếm, World Wide Web, blog, mạng ngang hàng, mạng xã hội, nội dung do người dùng tạo, chia sẻ

nhạc, hình ảnh và video, v.v.). Những ứng dụng này "đến bất ngờ", đột ngột, không lường trước được và bùng nổ. Thật là một thế giới tuyệt vời cho thế hệ tiếp theo khám phá!

Những gì mọi người đã truyền cảm hứng cho bạn một cách chuyên nghiệp?

Cho đến nay, đó là Claude Shannon đến từ MIT, một nhà nghiên cứu xuất sắc, người có khả năng liên hệ các ý tưởng toán học của mình với thế giới vật chất theo những cách rất trực quan. Anh ấy là một thành viên xuất sắc trong ủy ban luận án tiến sĩ của tôi.

Bạn có lời khuyên nào dành cho các sinh viên đang theo học lĩnh vực mạng/Internet không?

Internet và tất cả những gì nó mang lại là một biên giới mới rộng lớn, liên tục chứa đầy những thách thức đáng kinh ngạc. Có chỗ cho sự đổi mới lớn. Đừng bị hạn chế bởi công nghệ ngày nay. Hãy tiếp cận và tưởng tượng những gì có thể xảy ra và sau đó biến nó thành hiện thực.

**Chương 1: Mạng Máy Tính và Internet**

Internet ngày nay được coi là hệ thống kỹ thuật lớn nhất từng được nhân loại tạo ra, với hàng trăm triệu máy tính, liên kết truyền thông và Switch được kết nối; với hàng tỷ người dùng kết nối qua máy tính xách tay, máy tính bảng và điện thoại thông minh; cùng với hàng loạt các \"vật kết nối Internet\" mới bao gồm máy chơi game, hệ thống giám sát, đồng hồ, kính mắt, bộ điều nhiệt và ô tô. Với quy mô to lớn cùng vô số thành phần và ứng dụng đa dạng như vậy, liệu có hy vọng nào để hiểu được cách thức Internet vận hành hay không? Liệu có những nguyên tắc chỉ đạo và cấu trúc cốt lõi nào có thể cung cấp nền tảng để hiểu một hệ thống lớn và phức tạp đến kinh ngạc như vậy không? Và nếu có, liệu việc tìm hiểu về mạng máy tính có thực sự vừa thú vị vừa hấp dẫn không? Thật may mắn, câu trả lời cho tất cả các câu hỏi này là một tiếng CÓ vang dội! Quả thực, mục tiêu của chúng tôi trong cuốn sách này là mang đến cho bạn một phần giới thiệu hiện đại về lĩnh vực mạng máy tính đầy năng động, cung cấp cho bạn những nguyên tắc và hiểu biết thực tiễn cần thiết để hiểu không chỉ các mạng ngày nay mà còn cả các mạng trong tương lai.

Chương đầu tiên này trình bày một cái nhìn tổng quan sâu rộng về mạng máy tính và Internet. Mục tiêu ở đây là vẽ nên một bức tranh toàn cảnh và thiết lập bối cảnh cho phần còn lại của cuốn sách, giúp ta thấy được cả khu rừng thay vì chỉ nhìn từng cái cây. Chúng ta sẽ tìm hiểu nhiều khía cạnh trong chương giới thiệu này và thảo luận về nhiều thành phần cấu thành một mạng máy tính mà không làm mất đi bức tranh tổng thể.

Chúng tôi cấu trúc phần tổng quan về mạng máy tính trong chương này như sau. Sau khi giới thiệu một số thuật ngữ và khái niệm cơ bản, trước tiên chúng ta sẽ xem xét các thành phần phần cứng và phần mềm cơ bản tạo nên mạng. Chúng ta sẽ bắt đầu từ biên mạng (network edge) và tìm hiểu về các End Systems cùng các ứng dụng mạng đang chạy trên mạng. Sau đó, chúng ta sẽ khám phá lõi mạng (network core), xem xét các liên kết

**CHƯƠNG**

**Mạng Máy Tính và Internet**

![](media/image1.png){width="5.5in" height="6.930965660542432in"}

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

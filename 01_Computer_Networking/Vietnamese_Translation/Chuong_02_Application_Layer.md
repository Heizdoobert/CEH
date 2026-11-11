**Chương 2: Tầng Ứng Dụng (Application Layer)**

Các ứng dụng mạng là lý do tồn tại của mạng máy tính---nếu chúng ta không thể nghĩ ra bất kỳ ứng dụng hữu ích nào thì sẽ không cần đến cơ sở hạ tầng và giao thức mạng để hỗ trợ chúng. Kể từ khi Internet ra đời, rất nhiều ứng dụng hữu ích và mang tính giải trí đã thực sự được tạo ra. Những ứng dụng này là động lực thúc đẩy sự thành công của Internet, thúc đẩy mọi người ở gia đình, trường học, chính phủ và doanh nghiệp biến Internet trở thành một phần không thể thiếu trong hoạt động hàng ngày của họ.

Các ứng dụng Internet bao gồm các ứng dụng dựa trên văn bản cổ điển đã trở nên phổ biến trong những năm 1970 và 1980: e-mail văn bản, truy cập máy tính từ xa, truyền tệp và nhóm tin. Chúng bao gồm ứng dụng tuyệt vời vào giữa những năm 1990, World Wide Web, bao gồm lướt Web, tìm kiếm và thương mại điện tử. Kể từ đầu thiên niên kỷ mới, các ứng dụng mới và có tính hấp dẫn cao tiếp tục xuất hiện, bao gồm giọng nói qua IP và hội nghị truyền hình như Skype, Facetime và Google Hangouts; video do người dùng tạo như YouTube và phim theo yêu cầu như Netflix; và các trò chơi trực tuyến nhiều người chơi như Second Life và World of Warcraft. Trong cùng thời gian này, chúng ta đã chứng kiến ​​sự xuất hiện của một thế hệ ứng dụng mạng xã hội mới---chẳng hạn như Facebook, Instagram và Twitter---đã tạo ra mạng lưới con người trên mạng hoặc bộ định tuyến và liên kết truyền thông của Internet. Và gần đây nhất, cùng với sự xuất hiện của điện thoại thông minh và sự phổ biến của truy cập Internet không dây 4G/5G, đã có rất nhiều ứng dụng di động dựa trên vị trí, bao gồm các ứng dụng đăng ký, hẹn hò và dự báo giao thông đường bộ phổ biến (như Yelp, Tinder và Waz), ứng dụng thanh toán di động (như WeChat và Apple Pay) và các ứng dụng nhắn tin (như WeChat và WhatsApp). Rõ ràng, các ứng dụng Internet mới và thú vị không hề bị chậm lại. Có lẽ một số độc giả của văn bản này sẽ tạo ra thế hệ ứng dụng Internet hấp dẫn tiếp theo!

**Application Layer**

**CHƯƠNG**

![](media/image1.png){width="5.5in" height="6.930965660542432in"}

![](media/image2.png){width="5.5in" height="0.9567311898512686in"}

Trong chương này, chúng ta nghiên cứu các khía cạnh khái niệm và triển khai của các ứng dụng mạng. Chúng tôi bắt đầu bằng cách xác định các khái niệm chính của lớp ứng dụng, bao gồm các dịch vụ mạng được yêu cầu bởi các ứng dụng, máy khách và máy chủ, quy trình và giao diện của lớp vận chuyển. Chúng tôi kiểm tra chi tiết một số ứng dụng mạng, bao gồm Web, e-mail, DNS, phân phối tệp ngang hàng (P2P) và truyền phát video. Sau đó, chúng tôi đề cập đến việc phát triển ứng dụng mạng, trên cả TCP và UDP. Đặc biệt, chúng tôi nghiên cứu giao diện socket và tìm hiểu một số ứng dụng máy khách-máy chủ đơn giản bằng Python. Chúng tôi cũng cung cấp một số bài tập lập trình socket thú vị và thú vị ở cuối chương.

Lớp ứng dụng là nơi đặc biệt tốt để bắt đầu nghiên cứu các giao thức của chúng ta. Đó là mảnh đất quen thuộc. Chúng ta đã làm quen với nhiều ứng dụng dựa trên các giao thức mà chúng ta sẽ nghiên cứu. Nó sẽ cho chúng ta cảm nhận tốt về nội dung của các giao thức và sẽ giới thiệu cho chúng ta nhiều vấn đề tương tự mà chúng ta sẽ gặp lại khi nghiên cứu các giao thức lớp truyền tải, mạng và lớp liên kết.

**2.1 Nguyên tắc ứng dụng mạng**

Giả sử bạn có ý tưởng về một ứng dụng mạng mới. Có lẽ ứng dụng này sẽ là một dịch vụ tuyệt vời cho nhân loại, hoặc sẽ làm hài lòng giáo sư của bạn, hoặc sẽ mang lại cho bạn sự giàu có lớn, hoặc đơn giản là sẽ rất thú vị khi phát triển. Dù động cơ có thể là gì, bây giờ chúng ta hãy xem xét cách bạn biến ý tưởng thành một ứng dụng mạng trong thế giới thực.

Cốt lõi của việc phát triển ứng dụng mạng là viết các chương trình chạy trên các hệ thống đầu cuối khác nhau và giao tiếp với nhau qua mạng. Ví dụ: trong ứng dụng Web có hai chương trình riêng biệt giao tiếp với nhau: chương trình trình duyệt chạy trên máy chủ của người dùng (máy tính để bàn, máy tính xách tay, máy tính bảng, điện thoại thông minh, v.v.); và chương trình máy chủ Web đang chạy trên máy chủ của máy chủ Web. Một ví dụ khác, trong ứng dụng Video theo yêu cầu, chẳng hạn như Netflix (xem Phần 2.6), có một chương trình do Netflix cung cấp chạy trên điện thoại thông minh, máy tính bảng hoặc máy tính của người dùng; và chương trình máy chủ Netflix chạy trên máy chủ Netflix. Máy chủ thường (nhưng chắc chắn không phải luôn luôn) được đặt trong trung tâm dữ liệu, như trong Hình 2.1.

Vì vậy, khi phát triển ứng dụng mới, bạn cần viết phần mềm chạy trên nhiều hệ thống đầu cuối. Phần mềm này có thể được viết, ví dụ, bằng C, Java hoặc Python. Điều quan trọng là bạn không cần phải viết phần mềm chạy trên các thiết bị lõi mạng, chẳng hạn như bộ định tuyến hoặc bộ chuyển mạch lớp liên kết. Ngay cả khi bạn muốn viết phần mềm ứng dụng cho các thiết bị lõi mạng này, bạn cũng không thể làm được điều đó. Như chúng ta đã học ở Chương 1 và như được trình bày trước đó trong Hình 1.24, các thiết bị lõi mạng không hoạt động ở lớp ứng dụng mà thay vào đó hoạt động ở các lớp thấp hơn--- cụ thể là ở lớp mạng trở xuống. Thiết kế cơ bản này---cụ thể là giới hạn phần mềm ứng dụng trong các hệ thống cuối---như trong Hình 2.1, đã tạo điều kiện cho sự phát triển và triển khai nhanh chóng một loạt các ứng dụng mạng.

Chuyên chở

Mạng

Liên kết dữ liệu

Thuộc vật chất

Chuyên chở

Mạng

Liên kết dữ liệu

Thuộc vật chất

Chuyên chở

Mạng

Liên kết dữ liệu

Thuộc vật chất

Mạng lưới nhà cung cấp nội dung

Quốc gia hoặc

ISP toàn cầu

Mạng trung tâm dữ liệu

Mạng trung tâm dữ liệu

Mạng di động

Mạng doanh nghiệp

ISP địa phương hoặc khu vực

Ứng dụng

Ứng dụng

Ứng dụng

Mạng gia đình

*Hình 2.1 ♦ Quá trình giao tiếp của một ứng dụng mạng diễn ra*

giữa các hệ thống đầu cuối ở lớp ứng dụng

**2.1.1 Kiến trúc ứng dụng mạng**

Trước khi đi sâu vào mã hóa phần mềm, bạn nên có một kế hoạch kiến ​​trúc rộng rãi cho ứng dụng của mình. Hãy nhớ rằng kiến ​​trúc của ứng dụng khác biệt rõ rệt với kiến ​​trúc mạng (ví dụ: kiến ​​trúc Internet năm lớp được thảo luận trong Chương 1). Từ quan điểm của nhà phát triển ứng dụng, kiến ​​trúc mạng là cố định và cung cấp một bộ dịch vụ cụ thể cho ứng dụng. Mặt khác, kiến ​​trúc ứng dụng được thiết kế bởi nhà phát triển ứng dụng và chỉ ra cách cấu trúc ứng dụng trên các hệ thống cuối khác nhau. Khi chọn kiến ​​trúc ứng dụng, nhà phát triển ứng dụng có thể sẽ dựa trên một trong hai mô hình kiến ​​trúc chiếm ưu thế được sử dụng trong các ứng dụng mạng hiện đại: kiến ​​trúc máy khách-máy chủ hoặc kiến ​​trúc ngang hàng (P2P).

Trong kiến ​​trúc máy khách-máy chủ, có một máy chủ luôn bật, được gọi là máy chủ, phục vụ các yêu cầu từ nhiều máy chủ khác, được gọi là máy khách. Một ví dụ điển hình là ứng dụng Web mà các dịch vụ máy chủ Web luôn hoạt động yêu cầu từ các trình duyệt chạy trên máy khách. Khi một máy chủ Web nhận được yêu cầu về một đối tượng từ máy khách, nó sẽ phản hồi bằng cách gửi đối tượng được yêu cầu đến máy khách. Lưu ý rằng với kiến ​​trúc client-server, các client không giao tiếp trực tiếp với nhau; ví dụ: trong ứng dụng Web, hai trình duyệt không giao tiếp trực tiếp. Một đặc điểm khác của kiến ​​trúc máy khách-máy chủ là máy chủ có một địa chỉ cố định, nổi tiếng, được gọi là địa chỉ IP (chúng ta sẽ thảo luận sớm). Vì máy chủ có một địa chỉ cố định, phổ biến và vì máy chủ luôn bật nên máy khách luôn có thể liên hệ với máy chủ bằng cách gửi gói đến địa chỉ IP của máy chủ. Một số ứng dụng nổi tiếng có kiến ​​trúc máy khách-máy chủ bao gồm Web, FTP, Telnet và e-mail. Kiến trúc máy khách-máy chủ được hiển thị trong Hình 2.2(a).

Thông thường trong ứng dụng máy khách-máy chủ, máy chủ một máy chủ không có khả năng đáp ứng tất cả các yêu cầu từ máy khách. Ví dụ: một trang mạng xã hội phổ biến có thể nhanh chóng bị quá tải nếu nó chỉ có một máy chủ xử lý tất cả các yêu cầu của nó. Vì lý do này, một trung tâm dữ liệu, nơi chứa một số lượng lớn máy chủ, thường được sử dụng để tạo ra một máy chủ ảo mạnh mẽ. Các dịch vụ Internet phổ biến nhất---chẳng hạn như các công cụ tìm kiếm (ví dụ: Google, Bing, Baidu), thương mại Internet (ví dụ: Amazon, eBay, Alibaba), e-mail trên web (ví dụ: Gmail và Yahoo Mail), phương tiện truyền thông xã hội (ví dụ: Facebook, Instagram, Twitter và WeChat)---chạy trong một hoặc nhiều trung tâm dữ liệu. Như đã thảo luận trong Phần 1.3.3, Google có 19 trung tâm dữ liệu được phân bổ trên khắp thế giới, xử lý chung các dịch vụ tìm kiếm, YouTube, Gmail và các dịch vụ khác. Một trung tâm dữ liệu có thể có hàng trăm nghìn máy chủ cần được cấp nguồn và bảo trì. Ngoài ra, các nhà cung cấp dịch vụ phải trả chi phí kết nối và băng thông định kỳ để gửi dữ liệu từ trung tâm dữ liệu của họ.

Trong kiến ​​trúc P2P, có sự phụ thuộc tối thiểu (hoặc không) vào các máy chủ chuyên dụng trong trung tâm dữ liệu. Thay vào đó, ứng dụng khai thác giao tiếp trực tiếp giữa các cặp máy chủ được kết nối không liên tục, được gọi là các máy ngang hàng. Các thiết bị ngang hàng không thuộc sở hữu của nhà cung cấp dịch vụ mà thay vào đó là máy tính để bàn và máy tính xách tay do người dùng kiểm soát, với hầu hết các thiết bị ngang hàng cư trú tại nhà, trường đại học và văn phòng. Bởi vì các đồng nghiệp giao tiếp

không thông qua một máy chủ chuyên dụng, kiến ​​trúc này được gọi là ngang hàng. Một ví dụ về ứng dụng P2P phổ biến là ứng dụng chia sẻ tệp BitTorrent.

Một trong những tính năng hấp dẫn nhất của kiến ​​trúc P2P là khả năng tự mở rộng của chúng. Ví dụ: trong ứng dụng chia sẻ tệp P2P, mặc dù mỗi thiết bị ngang hàng tạo ra khối lượng công việc bằng cách yêu cầu tệp, nhưng mỗi thiết bị ngang hàng cũng bổ sung năng lực dịch vụ cho hệ thống bằng cách phân phối tệp cho các thiết bị ngang hàng khác. Kiến trúc P2P cũng hiệu quả về mặt chi phí vì chúng thường không yêu cầu cơ sở hạ tầng máy chủ và băng thông máy chủ đáng kể (ngược lại với thiết kế máy khách-máy chủ có trung tâm dữ liệu). Tuy nhiên, các ứng dụng P2P phải đối mặt với những thách thức về bảo mật, hiệu suất và độ tin cậy do cấu trúc phi tập trung cao của chúng.

**2.1.2 Quy trình giao tiếp**

Trước khi xây dựng ứng dụng mạng, bạn cũng cần hiểu biết cơ bản về cách các chương trình chạy trong nhiều hệ thống đầu cuối giao tiếp với nhau. Theo thuật ngữ của hệ điều hành, thực ra không phải các chương trình mà là các tiến trình

Một. Kiến trúc máy khách-máy chủ b. Kiến trúc ngang hàng

*Hình 2.2 ♦ (a) Kiến trúc client-server; (b) kiến ​​trúc P2P*

giao tiếp. Một quy trình có thể được coi là một chương trình đang chạy trong hệ thống cuối. Khi các tiến trình đang chạy trên cùng một hệ thống cuối, chúng có thể giao tiếp với nhau bằng giao tiếp giữa các tiến trình, sử dụng các quy tắc do hệ điều hành của hệ thống cuối điều chỉnh. Nhưng trong cuốn sách này, chúng tôi không đặc biệt quan tâm đến cách các tiến trình trong cùng một máy chủ giao tiếp với nhau như thế nào mà thay vào đó là cách các tiến trình chạy trên các máy chủ khác nhau (có khả năng là các hệ điều hành khác nhau) giao tiếp như thế nào.

Các tiến trình trên hai hệ thống đầu cuối khác nhau giao tiếp với nhau bằng cách trao đổi tin nhắn trên mạng máy tính. Quá trình gửi sẽ tạo và gửi tin nhắn vào mạng; quá trình nhận sẽ nhận những thông báo này và có thể phản hồi bằng cách gửi lại thông báo. Hình 2.1 minh họa rằng các tiến trình giao tiếp với nhau nằm trong lớp ứng dụng của ngăn xếp giao thức năm lớp.

Quy trình máy khách và máy chủ

Một ứng dụng mạng bao gồm các cặp tiến trình gửi tin nhắn cho nhau qua mạng. Ví dụ, trong ứng dụng Web, một tiến trình trình duyệt máy khách trao đổi các thông báo với một tiến trình máy chủ Web. Trong hệ thống chia sẻ tệp P2P, một tệp được chuyển từ một tiến trình trong một máy ngang hàng sang một tiến trình trong một máy ngang hàng khác. Đối với mỗi cặp quy trình giao tiếp, chúng tôi thường gắn nhãn một trong hai quy trình là máy khách và quy trình còn lại là máy chủ. Với Web, trình duyệt là một tiến trình máy khách và máy chủ Web là một tiến trình máy chủ. Với tính năng chia sẻ tệp P2P, thiết bị ngang hàng đang tải tệp xuống được gắn nhãn là máy khách và thiết bị ngang hàng đang tải tệp lên được gắn nhãn là máy chủ.

Bạn có thể đã quan sát thấy rằng trong một số ứng dụng, chẳng hạn như trong chia sẻ tệp P2P, một quy trình có thể vừa là máy khách vừa là máy chủ. Thật vậy, một quy trình trong hệ thống chia sẻ tệp P2P có thể tải lên và tải xuống tệp. Tuy nhiên, trong bối cảnh của bất kỳ phiên giao tiếp cụ thể nào giữa một cặp quy trình, chúng ta vẫn có thể gắn nhãn một quy trình là máy khách và quy trình kia là máy chủ. Chúng tôi xác định các quy trình máy khách và máy chủ như sau:

Trong bối cảnh phiên giao tiếp giữa một cặp quy trình, quy trình bắt đầu giao tiếp (nghĩa là ban đầu liên hệ với quy trình khác khi bắt đầu phiên) được gắn nhãn là máy khách. Quá trình đang chờ được liên hệ để bắt đầu phiên là máy chủ.

Trong Web, quy trình trình duyệt sẽ khởi tạo liên hệ với quy trình máy chủ Web; do đó tiến trình trình duyệt là máy khách và tiến trình máy chủ Web là máy chủ. Trong chia sẻ tệp P2P, khi Thiết bị ngang hàng A yêu cầu Thiết bị ngang hàng B gửi một tệp cụ thể, Thiết bị ngang hàng A là máy khách và Thiết bị ngang hàng B là máy chủ trong bối cảnh của phiên giao tiếp cụ thể này. Khi không có sự nhầm lẫn, đôi khi chúng tôi cũng sẽ sử dụng thuật ngữ "phía máy khách và phía máy chủ của ứng dụng". Ở cuối chương này, chúng ta sẽ tìm hiểu mã đơn giản cho cả phía máy khách và máy chủ của các ứng dụng mạng.

Giao diện giữa quy trình và mạng máy tính

Như đã lưu ý ở trên, hầu hết các ứng dụng bao gồm các cặp quy trình giao tiếp, với hai quy trình trong mỗi cặp gửi tin nhắn cho nhau. Bất kỳ tin nhắn nào được gửi từ tiến trình này sang tiến trình khác đều phải đi qua mạng cơ bản. Một quá trình gửi tin nhắn vào và nhận tin nhắn từ mạng thông qua giao diện phần mềm được gọi là ổ cắm. Hãy xem xét một sự tương tự để giúp chúng ta hiểu các quy trình và ổ cắm. Một quá trình tương tự như một ngôi nhà và ổ cắm của nó tương tự như cánh cửa của nó. Khi một tiến trình muốn gửi tin nhắn đến một tiến trình khác trên một máy chủ khác, nó sẽ đẩy tin nhắn ra khỏi cửa (ổ cắm) của nó. Quá trình gửi này giả định rằng có một cơ sở hạ tầng giao thông ở phía bên kia cánh cửa của nó sẽ vận chuyển thông điệp đến cửa của quá trình đích. Khi tin nhắn đến máy chủ đích, tin nhắn sẽ đi qua cửa (ổ cắm) của quy trình nhận và quy trình nhận sẽ xử lý tin nhắn.

Hình 2.3 minh họa giao tiếp socket giữa hai tiến trình giao tiếp qua Internet. (Hình 2.3 giả định rằng giao thức truyền tải cơ bản được các tiến trình sử dụng là giao thức TCP của Internet.) Như được hiển thị trong hình này, ổ cắm là giao diện giữa lớp ứng dụng và lớp vận chuyển trong máy chủ. Nó còn được gọi là Giao diện lập trình ứng dụng (API) giữa ứng dụng và mạng, vì socket là giao diện lập trình mà các ứng dụng mạng được xây dựng. Nhà phát triển ứng dụng có quyền kiểm soát mọi thứ ở phía lớp ứng dụng của socket nhưng có rất ít quyền kiểm soát phía lớp vận chuyển của socket. Kiểm soát duy nhất mà nhà phát triển ứng dụng có ở phía tầng vận chuyển là (1) lựa chọn giao thức truyền tải và (2) có lẽ là khả năng khắc phục một số vấn đề.

Quá trình

Host hoặc

máy chủ

Host hoặc

máy chủ

Kiểm soát bởi nhà phát triển ứng dụng

Được kiểm soát bởi quy trình của nhà phát triển ứng dụng

TCP với

bộ đệm, biến Internet

Được điều khiển bởi hệ điều hành

Được điều khiển bởi hệ điều hành

TCP với

bộ đệm, biến

Socket Socket

*Hình 2.3 ♦ Quy trình ứng dụng, ổ cắm và giao thức truyền tải cơ bản*

các tham số của lớp vận chuyển như bộ đệm tối đa và kích thước phân đoạn tối đa (sẽ được đề cập trong Chương 3). Khi nhà phát triển ứng dụng chọn giao thức truyền tải (nếu có sẵn lựa chọn), ứng dụng sẽ được xây dựng bằng cách sử dụng các dịch vụ của lớp vận chuyển do giao thức đó cung cấp. Chúng ta sẽ tìm hiểu chi tiết về socket trong Phần 2.7.

Quy trình xử lý địa chỉ

Để gửi thư bưu chính đến một địa điểm cụ thể, điểm đến cần phải có địa chỉ. Tương tự, để một tiến trình chạy trên một máy chủ có thể gửi các gói đến một tiến trình đang chạy trên một máy chủ khác, thì tiến trình nhận cần phải có một địa chỉ. Để xác định quy trình nhận, cần phải chỉ định hai phần thông tin: (1) địa chỉ của máy chủ và (2) mã nhận dạng chỉ định quy trình nhận trong máy chủ đích.

Trên Internet, máy chủ được xác định bằng địa chỉ IP của nó. Chúng ta sẽ thảo luận chi tiết về địa chỉ IP trong Chương 4. Hiện tại, tất cả những gì chúng ta cần biết là địa chỉ IP là số lượng 32 bit mà chúng ta có thể coi là nhận dạng duy nhất máy chủ. Ngoài việc biết địa chỉ của máy chủ mà thư được gửi đến, quy trình gửi cũng phải xác định quy trình nhận (cụ thể hơn là ổ cắm nhận) đang chạy trong máy chủ. Thông tin này là cần thiết vì nhìn chung một máy chủ có thể chạy nhiều ứng dụng mạng. Số cổng đích phục vụ mục đích này. Các ứng dụng phổ biến đã được gán số cổng cụ thể. Ví dụ: một máy chủ Web được xác định bằng cổng số 80. Một quy trình máy chủ thư (sử dụng giao thức SMTP) được xác định bằng cổng số 25. Bạn có thể tìm thấy danh sách các số cổng phổ biến cho tất cả các giao thức chuẩn Internet tại www.iana.org. Chúng ta sẽ kiểm tra số cổng một cách chi tiết trong Chương 3.

**2.1.3 Dịch vụ vận chuyển có sẵn cho ứng dụng**

Hãy nhớ lại rằng socket là giao diện giữa tiến trình ứng dụng và giao thức tầng vận chuyển. Ứng dụng ở phía gửi sẽ đẩy tin nhắn qua socket. Ở phía bên kia của socket, giao thức tầng vận chuyển có trách nhiệm đưa các thông báo đến socket của quá trình nhận.

Nhiều mạng, bao gồm cả Internet, cung cấp nhiều hơn một giao thức tầng vận chuyển. Khi bạn phát triển một ứng dụng, bạn phải chọn một trong các giao thức lớp vận chuyển có sẵn. Làm thế nào để bạn thực hiện sự lựa chọn này? Rất có thể, bạn sẽ nghiên cứu các dịch vụ được cung cấp bởi các giao thức lớp vận chuyển có sẵn, sau đó chọn giao thức có các dịch vụ phù hợp nhất với nhu cầu ứng dụng của bạn. Tình huống tương tự như việc lựa chọn vận chuyển bằng tàu hỏa hoặc máy bay để đi lại giữa hai thành phố. Bạn phải chọn cái này hay cái kia và mỗi phương thức vận chuyển sẽ cung cấp các dịch vụ khác nhau. (Ví dụ: tàu hỏa cung cấp dịch vụ đón và trả khách ở trung tâm thành phố, trong khi máy bay cung cấp thời gian di chuyển ngắn hơn.)

Các dịch vụ mà giao thức tầng vận chuyển có thể cung cấp cho các ứng dụng gọi nó là gì? Chúng ta có thể phân loại rộng rãi các dịch vụ có thể có theo bốn khía cạnh: truyền dữ liệu đáng tin cậy, thông lượng, thời gian và bảo mật.

Truyền dữ liệu đáng tin cậy

Như đã thảo luận ở Chương 1, các gói tin có thể bị thất lạc trong mạng máy tính. Ví dụ: một gói có thể tràn bộ đệm trong bộ định tuyến hoặc có thể bị máy chủ hoặc bộ định tuyến loại bỏ sau khi một số bit của nó bị hỏng. Đối với nhiều ứng dụng---chẳng hạn như thư điện tử, truyền tệp, truy cập máy chủ từ xa, truyền tài liệu Web và ứng dụng tài chính---việc mất dữ liệu có thể gây ra hậu quả nghiêm trọng (trong trường hợp sau là đối với ngân hàng hoặc khách hàng!). Vì vậy, để hỗ trợ các ứng dụng này, cần phải làm gì đó để đảm bảo rằng dữ liệu được gửi bởi một đầu của ứng dụng sẽ được phân phối chính xác và đầy đủ đến đầu kia của ứng dụng. Nếu một giao thức cung cấp dịch vụ phân phối dữ liệu được đảm bảo như vậy thì nó được cho là cung cấp khả năng truyền dữ liệu đáng tin cậy. Một dịch vụ quan trọng mà giao thức tầng vận chuyển có thể cung cấp cho ứng dụng là truyền dữ liệu đáng tin cậy từ tiến trình này sang tiến trình khác. Khi một giao thức truyền tải cung cấp dịch vụ này, quá trình gửi có thể chuyển dữ liệu của nó vào ổ cắm và hoàn toàn tin tưởng rằng dữ liệu sẽ đến mà không có lỗi ở quá trình nhận.

Khi giao thức lớp vận chuyển không cung cấp khả năng truyền dữ liệu đáng tin cậy, một số dữ liệu được gửi bởi quy trình gửi có thể không bao giờ đến được quy trình nhận. Điều này có thể được chấp nhận đối với các ứng dụng có khả năng chịu mất mát, đáng chú ý nhất là các ứng dụng đa phương tiện như âm thanh/video hội thoại có thể chịu được một lượng mất dữ liệu nhất định. Trong các ứng dụng đa phương tiện này, dữ liệu bị mất có thể dẫn đến một trục trặc nhỏ trong âm thanh/video---không phải là sự suy giảm nghiêm trọng.

Throughput

Trong Chương 1, chúng tôi đã giới thiệu khái niệm về thông lượng khả dụng, trong bối cảnh phiên giao tiếp giữa hai quy trình dọc theo đường dẫn mạng, là tốc độ mà quy trình gửi có thể phân phối bit cho quy trình nhận. Vì các phiên khác sẽ chia sẻ băng thông dọc theo đường dẫn mạng và vì các phiên khác này sẽ đến và đi nên thông lượng khả dụng có thể dao động theo thời gian. Những quan sát này dẫn đến một dịch vụ tự nhiên khác mà giao thức tầng vận chuyển có thể cung cấp, đó là thông lượng sẵn có được đảm bảo ở một số tốc độ xác định. Với dịch vụ như vậy, ứng dụng có thể yêu cầu thông lượng được đảm bảo là r bit/giây và giao thức truyền tải khi đó sẽ đảm bảo rằng thông lượng khả dụng luôn ít nhất là r bit/giây. Dịch vụ thông lượng được đảm bảo như vậy sẽ thu hút nhiều ứng dụng. Ví dụ: nếu một ứng dụng điện thoại Internet mã hóa giọng nói ở tốc độ 32 kbps, nó cần gửi dữ liệu vào mạng và gửi dữ liệu đến ứng dụng nhận ở tốc độ này. Nếu giao thức truyền tải không thể cung cấp thông lượng này thì ứng dụng sẽ cần mã hóa ở tốc độ thấp hơn (và nhận đủ thông lượng để duy trì tốc độ mã hóa thấp hơn này) hoặc có thể phải từ bỏ, vì việc nhận được một nửa thông lượng cần thiết chẳng hạn như ít hoặc không được sử dụng cho ứng dụng điện thoại Internet này. Các ứng dụng có yêu cầu về thông lượng được coi là các ứng dụng nhạy cảm với băng thông. Nhiều ứng dụng đa phương tiện hiện nay nhạy cảm với băng thông, mặc dù một số ứng dụng đa phương tiện có thể sử dụng băng thông thích ứng.

kỹ thuật mã hóa để mã hóa giọng nói hoặc video được số hóa ở tốc độ phù hợp với thông lượng hiện có.

Trong khi các ứng dụng nhạy cảm với băng thông có các yêu cầu thông lượng cụ thể, thì các ứng dụng linh hoạt có thể tận dụng nhiều hoặc ít thông lượng hiện có. Thư điện tử, truyền tập tin và truyền Web đều là những ứng dụng linh hoạt. Tất nhiên, thông lượng càng nhiều thì càng tốt. Có một câu ngạn ngữ nói rằng người ta không thể quá giàu, quá gầy hoặc có quá nhiều năng suất!

Thời gian

Giao thức tầng vận chuyển cũng có thể cung cấp sự đảm bảo về thời gian. Giống như đảm bảo thông lượng, đảm bảo thời gian có thể có nhiều hình thức và hình thức. Một ví dụ đảm bảo có thể là mọi bit mà người gửi bơm vào ổ cắm sẽ đến ổ cắm của người nhận không quá 100 mili giây sau đó. Dịch vụ như vậy sẽ hấp dẫn các ứng dụng tương tác thời gian thực, chẳng hạn như điện thoại Internet, môi trường ảo, hội nghị từ xa và trò chơi nhiều người chơi, tất cả đều yêu cầu hạn chế chặt chẽ về thời gian trong việc phân phối dữ liệu để có hiệu quả, xem \[Gauthier 1999; Ramjee 1994\]. Ví dụ, sự chậm trễ kéo dài trong điện thoại Internet có xu hướng dẫn đến những khoảng dừng không tự nhiên trong cuộc trò chuyện; trong trò chơi nhiều người chơi hoặc môi trường tương tác ảo, độ trễ kéo dài giữa việc thực hiện hành động và xem phản hồi từ môi trường (ví dụ: từ một người chơi khác ở cuối kết nối đầu cuối) khiến ứng dụng có cảm giác kém thực tế hơn. Đối với các ứng dụng không theo thời gian thực, độ trễ thấp hơn luôn được ưu tiên hơn độ trễ cao hơn, nhưng không có ràng buộc chặt chẽ nào được đặt ra đối với độ trễ đầu cuối.

Bảo vệ

Cuối cùng, một giao thức truyền tải có thể cung cấp cho ứng dụng một hoặc nhiều dịch vụ bảo mật. Ví dụ: trong máy chủ gửi, giao thức truyền tải có thể mã hóa tất cả dữ liệu được truyền bởi quá trình gửi và trong máy chủ nhận, giao thức lớp vận chuyển có thể giải mã dữ liệu trước khi gửi dữ liệu đến quá trình nhận. Dịch vụ như vậy sẽ cung cấp tính bảo mật giữa hai quy trình, ngay cả khi dữ liệu được quan sát bằng cách nào đó giữa quy trình gửi và nhận. Giao thức truyền tải cũng có thể cung cấp các dịch vụ bảo mật khác ngoài tính bảo mật, bao gồm tính toàn vẹn dữ liệu và xác thực điểm cuối, các chủ đề mà chúng tôi sẽ đề cập chi tiết trong Chương 8.

**2.1.4 Dịch vụ vận tải được cung cấp bởi Internet**

Cho đến thời điểm này, chúng ta đã xem xét các dịch vụ truyền tải mà mạng máy tính có thể cung cấp nói chung. Bây giờ chúng ta hãy tìm hiểu cụ thể hơn và kiểm tra loại dịch vụ vận tải được cung cấp bởi Internet. Internet (và, tổng quát hơn, các mạng TCP/ IP) cung cấp hai giao thức truyền tải cho các ứng dụng, UDP và TCP. Khi bạn (với tư cách là nhà phát triển ứng dụng) tạo một ứng dụng mạng mới cho

Internet, một trong những quyết định đầu tiên bạn phải đưa ra là nên sử dụng UDP hay TCP. Mỗi giao thức này cung cấp một bộ dịch vụ khác nhau cho các ứng dụng gọi. Hình 2.4 thể hiện các yêu cầu dịch vụ đối với một số ứng dụng được chọn.

TCP Dịch vụ

Mô hình dịch vụ TCP bao gồm dịch vụ hướng kết nối và dịch vụ truyền dữ liệu đáng tin cậy. Khi một ứng dụng gọi TCP làm giao thức truyền tải của nó, ứng dụng đó sẽ nhận được cả hai dịch vụ này từ TCP.

• Dịch vụ hướng kết nối. TCP yêu cầu máy khách và máy chủ trao đổi thông tin điều khiển lớp vận chuyển với nhau trước khi các thông báo cấp ứng dụng bắt đầu truyền đi. Cái gọi là thủ tục bắt tay này cảnh báo máy khách và máy chủ, cho phép họ chuẩn bị cho sự tấn công dữ dội của các gói tin. Sau giai đoạn bắt tay, một kết nối TCP được cho là tồn tại giữa các socket của hai tiến trình. Kết nối là kết nối song công hoàn toàn trong đó hai tiến trình có thể gửi tin nhắn cho nhau qua kết nối cùng một lúc. Khi ứng dụng gửi xong tin nhắn, nó phải ngắt kết nối. Trong Chương 3, chúng ta sẽ thảo luận chi tiết về dịch vụ hướng kết nối và xem xét cách triển khai nó. • Dịch vụ truyền dữ liệu đáng tin cậy. Quá trình giao tiếp có thể dựa vào TCP để phân phối tất cả dữ liệu được gửi mà không gặp lỗi và theo đúng thứ tự. Khi một bên của ứng dụng chuyển một luồng byte vào một ổ cắm, nó có thể tin tưởng vào TCP để phân phối cùng một luồng byte đó đến ổ cắm nhận mà không có byte nào bị thiếu hoặc trùng lặp.

Mất dữ liệu ứng dụng Throughput nhạy cảm với thời gian

Truyền/tải tập tin Không mất mát Đàn hồi Không

E-mail Không mất mát Đàn hồi Không

Tài liệu web Không mất mát Đàn hồi (vài kbps) Không

Điện thoại Internet/Hội nghị truyền hình

Âm thanh có khả năng chịu mất mát: vài kbps--1 Mbps Video: 10 kbps--5 Mbps

Có: 100 giây

Truyền trực tuyến khả năng chịu mất mát được lưu trữ Tương tự như trên Có: âm thanh/video vài giây

Trò chơi tương tác Chịu mất vài kbps--10 kbps Có: 100 giây

Nhắn tin trên điện thoại thông minh Không mất Co giãn Có và không

*Hình 2.4 ♦ Yêu cầu của các ứng dụng mạng được chọn*

TCP cũng bao gồm cơ chế kiểm soát tắc nghẽn, một dịch vụ vì lợi ích chung của Internet hơn là vì lợi ích trực tiếp của quá trình giao tiếp. Cơ chế kiểm soát tắc nghẽn TCP điều tiết quá trình gửi (máy khách hoặc máy chủ) khi mạng bị tắc nghẽn giữa người gửi và người nhận. Như chúng ta sẽ thấy trong Chương 3, kiểm soát tắc nghẽn TCP cũng cố gắng giới hạn mỗi kết nối TCP ở mức chia sẻ băng thông mạng hợp lý.

UDP Dịch vụ

UDP là một giao thức truyền tải gọn nhẹ, đơn giản, cung cấp các dịch vụ tối thiểu. UDP không có kết nối, do đó không có bắt tay trước khi hai quá trình bắt đầu giao tiếp. UDP cung cấp dịch vụ truyền dữ liệu không đáng tin cậy---nghĩa là khi một quy trình gửi tin nhắn vào ổ cắm UDP, UDP không đảm bảo rằng tin nhắn sẽ đến được quy trình nhận. Hơn nữa, các tin nhắn đến quá trình nhận có thể không đúng thứ tự.

ĐẢM BẢO TCP

Cả TCP và UDP đều không cung cấp bất kỳ mã hóa nào---dữ liệu mà quá trình gửi chuyển vào ổ cắm của nó cũng chính là dữ liệu truyền qua mạng tới quy trình đích. Vì vậy, ví dụ: nếu quá trình gửi gửi mật khẩu ở dạng văn bản rõ ràng (tức là không được mã hóa) vào ổ cắm của nó, thì mật khẩu văn bản rõ ràng sẽ di chuyển qua tất cả các liên kết giữa người gửi và người nhận, có khả năng bị đánh hơi và phát hiện ở bất kỳ liên kết can thiệp nào. Vì quyền riêng tư và các vấn đề bảo mật khác đã trở nên quan trọng đối với nhiều ứng dụng nên cộng đồng Internet đã phát triển một tính năng nâng cao cho TCP, được gọi là Transport Layer Bảo mật (TLS) \[RFC 5246\]. TCP-enhanced-with-TLS không chỉ thực hiện mọi việc mà TCP truyền thống thực hiện mà còn cung cấp các dịch vụ bảo mật quan trọng giữa các quy trình, bao gồm mã hóa, tính toàn vẹn dữ liệu và xác thực điểm cuối. Chúng tôi nhấn mạnh rằng TLS không phải là giao thức truyền tải Internet thứ ba, cùng cấp độ với TCP và UDP, mà thay vào đó là một cải tiến của TCP, với những cải tiến được triển khai trong lớp ứng dụng. Đặc biệt, nếu một ứng dụng muốn sử dụng các dịch vụ của TLS, thì nó cần phải bao gồm mã TLS (các lớp và thư viện hiện có, được tối ưu hóa cao) ở cả phía máy khách và phía máy chủ của ứng dụng. TLS có API socket riêng tương tự như API socket TCP truyền thống. Khi một ứng dụng sử dụng TLS, quá trình gửi sẽ chuyển dữ liệu văn bản rõ ràng tới ổ cắm TLS; TLS trong máy chủ gửi sau đó mã hóa dữ liệu và chuyển dữ liệu được mã hóa đến ổ cắm TCP. Dữ liệu được mã hóa di chuyển qua Internet đến ổ cắm TCP trong quá trình nhận. Ổ cắm nhận chuyển dữ liệu được mã hóa tới TLS để giải mã dữ liệu. Cuối cùng, TLS chuyển dữ liệu văn bản rõ ràng qua ổ cắm TLS của nó tới quy trình nhận. Chúng tôi sẽ đề cập đến TLS một cách chi tiết trong Chương 8.

TẬP TRUNG VÀO AN NINH

UDP không bao gồm cơ chế kiểm soát tắc nghẽn, vì vậy phía gửi UDP có thể bơm dữ liệu vào lớp bên dưới (lớp mạng) với bất kỳ tốc độ nào mà nó muốn. (Tuy nhiên, lưu ý rằng thông lượng thực tế từ đầu đến cuối có thể thấp hơn tốc độ này do khả năng truyền tải hạn chế của các liên kết can thiệp hoặc do tắc nghẽn).

Dịch vụ không được cung cấp bởi giao thức truyền tải Internet

Chúng tôi đã tổ chức các dịch vụ giao thức truyền tải theo bốn khía cạnh: truyền dữ liệu đáng tin cậy, thông lượng, thời gian và bảo mật. Dịch vụ nào trong số này được cung cấp bởi TCP và UDP? Chúng tôi đã lưu ý rằng TCP cung cấp khả năng truyền dữ liệu đầu cuối đáng tin cậy. Và chúng tôi cũng biết rằng TCP có thể dễ dàng được nâng cao ở lớp ứng dụng với TLS để cung cấp các dịch vụ bảo mật. Nhưng trong mô tả ngắn gọn của chúng tôi về TCP và UDP, rõ ràng là thiếu bất kỳ đề cập nào về đảm bảo thông lượng hoặc thời gian--- các dịch vụ không được cung cấp bởi các giao thức truyền tải Internet ngày nay. Phải chăng điều này có nghĩa là các ứng dụng nhạy cảm với thời gian như điện thoại Internet không thể chạy trên Internet ngày nay? Câu trả lời rõ ràng là không---Internet đã lưu trữ các ứng dụng nhạy cảm với thời gian trong nhiều năm. Các ứng dụng này thường hoạt động khá tốt vì chúng được thiết kế để đối phó với tình trạng thiếu bảo đảm này ở mức độ lớn nhất có thể. Tuy nhiên, thiết kế thông minh có những hạn chế khi độ trễ quá lớn hoặc thông lượng từ đầu đến cuối bị hạn chế. Tóm lại, Internet ngày nay thường có thể cung cấp dịch vụ thỏa đáng cho các ứng dụng nhạy cảm với thời gian, nhưng nó không thể cung cấp bất kỳ đảm bảo nào về thời gian hoặc thông lượng.

Hình 2.5 chỉ ra các giao thức truyền tải được sử dụng bởi một số ứng dụng Internet phổ biến. Chúng tôi thấy rằng e-mail, truy cập thiết bị đầu cuối từ xa, Web và truyền tệp đều sử dụng TCP. Các ứng dụng này đã chọn TCP chủ yếu vì TCP cung cấp khả năng truyền dữ liệu đáng tin cậy, đảm bảo rằng tất cả dữ liệu cuối cùng sẽ đến đích. Bởi vì các ứng dụng điện thoại Internet (chẳng hạn như Skype) thường có thể chấp nhận một số mất mát nhưng yêu cầu tốc độ tối thiểu để có hiệu quả, các nhà phát triển ứng dụng điện thoại Internet

Ứng dụng Giao thức lớp ứng dụng làm cơ sở cho giao thức truyền tải

Thư điện tử

Truy cập thiết bị đầu cuối từ xa

Web

Truyền tập tin

Truyền phát đa phương tiện

Điện thoại Internet

SMTP \[RFC 5321\]

Telnet \[RFC 854\]

HTTP 1.1 \[RFC 7230\]

FTP \[RFC 959\]

HTTP (ví dụ: YouTube), DASH

SIP \[RFC 3261\], RTP \[RFC 3550\] hoặc độc quyền (ví dụ: Skype)

TCP

TCP

TCP

TCP

TCP

UDP hoặc TCP

*Hình 2.5 ♦ Các ứng dụng Internet phổ biến, lớp ứng dụng của chúng*

các giao thức và các giao thức vận chuyển cơ bản của chúng

thường thích chạy các ứng dụng của họ trên UDP, do đó tránh được cơ chế kiểm soát tắc nghẽn và chi phí gói của TCP. Nhưng vì nhiều tường lửa được cấu hình để chặn (hầu hết các loại) lưu lượng UDP nên các ứng dụng điện thoại Internet thường được thiết kế để sử dụng TCP làm bản sao lưu nếu giao tiếp UDP không thành công.

**2.1.5 Giao thức lớp ứng dụng**

Chúng ta vừa biết rằng các tiến trình mạng giao tiếp với nhau bằng cách gửi tin nhắn vào socket. Nhưng những thông điệp này được cấu trúc như thế nào? Ý nghĩa của các trường khác nhau trong tin nhắn là gì? Khi nào các tiến trình gửi tin nhắn? Những câu hỏi này đưa chúng ta vào lĩnh vực của các giao thức lớp ứng dụng. Giao thức lớp ứng dụng xác định cách các quy trình của ứng dụng chạy trên các hệ thống đầu cuối khác nhau truyền thông điệp cho nhau. Cụ thể, giao thức lớp ứng dụng xác định:

• Các loại tin nhắn được trao đổi, ví dụ, tin nhắn yêu cầu và tin nhắn phản hồi • Cú pháp của các loại tin nhắn khác nhau, chẳng hạn như các trường trong tin nhắn và cách mô tả các trường • Ngữ nghĩa của các trường, tức là ý nghĩa của thông tin trong các trường • Quy tắc xác định thời điểm và cách thức một quá trình gửi tin nhắn và phản hồi tin nhắn

Một số giao thức lớp ứng dụng được chỉ định trong RFC và do đó thuộc phạm vi công cộng. Ví dụ: giao thức lớp ứng dụng của Web, HTTP (Giao thức truyền siêu văn bản \[RFC 7230\]), có sẵn dưới dạng RFC. Nếu nhà phát triển trình duyệt tuân theo các quy tắc của HTTP RFC, trình duyệt sẽ có thể truy xuất các trang Web từ bất kỳ máy chủ Web nào cũng tuân theo các quy tắc của HTTP RFC. Nhiều giao thức lớp ứng dụng khác là độc quyền và cố ý không có sẵn trong phạm vi công cộng. Ví dụ: Skype sử dụng các giao thức lớp ứng dụng độc quyền.

Điều quan trọng là phải phân biệt giữa các ứng dụng mạng và các giao thức lớp ứng dụng. Giao thức lớp ứng dụng chỉ là một phần của ứng dụng mạng (mặc dù, là một phần rất quan trọng của ứng dụng theo quan điểm của chúng tôi!). Hãy xem xét một vài ví dụ. Web là một ứng dụng máy khách-máy chủ cho phép người dùng lấy tài liệu từ máy chủ Web theo yêu cầu. Ứng dụng Web bao gồm nhiều thành phần, bao gồm tiêu chuẩn cho các định dạng tài liệu (nghĩa là HTML), trình duyệt Web (ví dụ: Chrome và Microsoft Internet Explorer), máy chủ Web (ví dụ: máy chủ Apache và Microsoft) và giao thức lớp ứng dụng. Giao thức lớp ứng dụng của Web, HTTP, xác định định dạng và trình tự các thông báo được trao đổi giữa trình duyệt và máy chủ Web. Vì vậy, HTTP chỉ là một phần (mặc dù là một phần quan trọng) của ứng dụng Web. Một ví dụ khác, chúng ta sẽ thấy trong Phần 2.6 rằng dịch vụ video của Netflix cũng có nhiều thành phần,

bao gồm các máy chủ lưu trữ và truyền video, các máy chủ khác quản lý việc thanh toán và các chức năng khác của máy khách, máy khách (ví dụ: ứng dụng Netflix trên điện thoại thông minh, máy tính bảng hoặc máy tính của bạn) và giao thức DASH cấp ứng dụng xác định định dạng và chuỗi tin nhắn được trao đổi giữa máy chủ và máy khách Netflix. Do đó, DASH chỉ là một phần (mặc dù là một phần quan trọng) của ứng dụng Netflix.

**2.1.6 Các ứng dụng mạng được đề cập trong cuốn sách này**

Các ứng dụng mới đang được phát triển mỗi ngày. Thay vì đề cập đến một số lượng lớn các ứng dụng Internet theo kiểu bách khoa toàn thư, chúng tôi đã chọn tập trung vào một số lượng nhỏ các ứng dụng vừa phổ biến vừa quan trọng. Trong chương này, chúng ta thảo luận về năm ứng dụng quan trọng: Web, thư điện tử, dịch vụ thư mục, truyền phát video và các ứng dụng P2P. Đầu tiên chúng ta thảo luận về Web, không chỉ vì đây là một ứng dụng cực kỳ phổ biến mà còn vì giao thức lớp ứng dụng của nó, HTTP, rất đơn giản và dễ hiểu. Sau đó chúng ta thảo luận về thư điện tử, ứng dụng tuyệt vời đầu tiên của Internet. E-mail phức tạp hơn Web ở chỗ nó sử dụng không chỉ một mà nhiều giao thức lớp ứng dụng. Sau e-mail, chúng tôi đề cập tới DNS, nơi cung cấp dịch vụ thư mục cho Internet. Hầu hết người dùng không tương tác trực tiếp với DNS; thay vào đó, người dùng gọi DNS một cách gián tiếp thông qua các ứng dụng khác (bao gồm Web, truyền tệp và thư điện tử). DNS minh họa độc đáo cách một phần chức năng mạng lõi (dịch tên mạng sang địa chỉ mạng) có thể được triển khai ở lớp ứng dụng trên Internet. Sau đó, chúng tôi thảo luận về P2P các ứng dụng chia sẻ tệp và hoàn thành nghiên cứu ứng dụng của mình bằng cách thảo luận về việc truyền phát video theo yêu cầu, bao gồm việc phân phối video được lưu trữ qua các mạng phân phối nội dung.

**2.2 Trang web và HTTP**

Cho đến đầu những năm 1990, Internet được sử dụng chủ yếu bởi các nhà nghiên cứu, học giả và sinh viên đại học để đăng nhập vào máy chủ từ xa, truyền tệp từ máy chủ cục bộ sang máy chủ từ xa và ngược lại, để nhận và gửi tin tức cũng như nhận và gửi thư điện tử. Mặc dù những ứng dụng này đã (và tiếp tục) cực kỳ hữu ích, Internet về cơ bản vẫn chưa được biết đến bên ngoài cộng đồng học thuật và nghiên cứu. Sau đó, vào đầu những năm 1990, một ứng dụng quan trọng mới xuất hiện---World Wide Web \[Berners-Lee 1994\]. Web là ứng dụng Internet đầu tiên lọt vào mắt xanh của công chúng. Nó thay đổi đáng kể cách mọi người tương tác trong và ngoài môi trường làm việc của họ. Nó đã nâng Internet từ chỉ một trong nhiều mạng dữ liệu về cơ bản thành mạng dữ liệu duy nhất.

Có lẽ điều thu hút người dùng nhất là Web hoạt động theo yêu cầu. Người dùng nhận được những gì họ muốn, khi họ muốn. Điều này không giống như phát sóng truyền thống

đài phát thanh và truyền hình, buộc người dùng phải theo dõi khi nhà cung cấp nội dung cung cấp nội dung. Ngoài việc được cung cấp theo yêu cầu, Web còn có nhiều tính năng tuyệt vời khác được mọi người yêu thích và trân trọng. Bất kỳ cá nhân nào cũng có thể dễ dàng cung cấp thông tin trên Web---mọi người đều có thể trở thành nhà xuất bản với chi phí cực kỳ thấp. Các siêu liên kết và công cụ tìm kiếm giúp chúng ta điều hướng trong một đại dương thông tin. Hình ảnh và video kích thích các giác quan của chúng ta. Biểu mẫu, JavaScript, video và nhiều thiết bị khác cho phép chúng tôi tương tác với các trang và trang web. Và Web cùng các giao thức của nó đóng vai trò là nền tảng cho YouTube, e-mail trên nền Web (chẳng hạn như Gmail) và hầu hết các ứng dụng Internet di động, bao gồm Instagram và Google Maps.

**2.2.1 Tổng quan về HTTP**

Giao thức truyền siêu văn bản (HTTP), giao thức lớp ứng dụng của Web, là trung tâm của Web. Nó được định nghĩa trong \[RFC 1945\], \[RFC 7230\] và \[RFC 7540\]. HTTP được triển khai trong hai chương trình: chương trình máy khách và chương trình máy chủ. Chương trình máy khách và chương trình máy chủ, thực thi trên các hệ thống đầu cuối khác nhau, trao đổi với nhau bằng cách trao đổi tin nhắn HTTP. HTTP xác định cấu trúc của các tin nhắn này cũng như cách máy khách và máy chủ trao đổi tin nhắn. Trước khi giải thích chi tiết HTTP, chúng ta nên xem lại một số thuật ngữ Web.

Một trang Web (còn gọi là tài liệu) bao gồm các đối tượng. Một đối tượng chỉ đơn giản là một tệp---chẳng hạn như tệp HTML, hình ảnh JPEG, tệp Javascrpt, tệp biểu định kiểu CCS hoặc video clip---có thể được định địa chỉ bằng một URL duy nhất. Hầu hết các trang Web bao gồm một tệp HTML cơ sở và một số đối tượng được tham chiếu. Ví dụ: nếu một trang Web chứa văn bản HTML và năm hình ảnh JPEG thì trang Web đó có sáu đối tượng: tệp HTML cơ sở cộng với năm hình ảnh. Tệp HTML cơ sở tham chiếu các đối tượng khác trong trang bằng URL của đối tượng. Mỗi URL có hai thành phần: tên máy chủ của máy chủ chứa đối tượng và tên đường dẫn của đối tượng. Ví dụ: URL

http://www.someSchool.edu/someDepartment/picture.gif

có www.someSchool.edu cho tên máy chủ và /someDepartment/picture. gif cho tên đường dẫn. Bởi vì các trình duyệt Web (chẳng hạn như Internet Explorer và Chrome) triển khai phía máy khách của HTTP, nên trong ngữ cảnh của Web, chúng tôi sẽ sử dụng các từ trình duyệt và máy khách thay thế cho nhau. Các máy chủ web, triển khai phía máy chủ của HTTP, chứa các đối tượng Web, mỗi đối tượng được định địa chỉ bằng một URL. Các máy chủ Web phổ biến bao gồm Apache và Microsoft Internet Information Server.

HTTP xác định cách máy khách Web yêu cầu các trang Web từ máy chủ Web và cách máy chủ chuyển trang Web đến máy khách. Chúng ta sẽ thảo luận chi tiết về sự tương tác giữa máy khách và máy chủ ở phần sau, nhưng ý tưởng chung được minh họa trong Hình 2.6. Khi người dùng yêu cầu một trang Web (ví dụ: nhấp vào siêu liên kết), trình duyệt sẽ gửi

HTTP yêu cầu gửi tin nhắn về các đối tượng trong trang tới máy chủ. Máy chủ nhận được yêu cầu và phản hồi bằng các thông báo phản hồi HTTP có chứa các đối tượng.

HTTP sử dụng TCP làm giao thức truyền tải cơ bản (thay vì chạy trên UDP). Ứng dụng khách HTTP trước tiên sẽ khởi tạo kết nối TCP với máy chủ. Sau khi kết nối được thiết lập, trình duyệt và máy chủ sẽ xử lý quyền truy cập TCP thông qua giao diện ổ cắm của chúng. Như được mô tả trong Phần 2.1, về phía máy khách, giao diện socket là cánh cửa giữa tiến trình máy khách và kết nối TCP; về phía máy chủ, nó là cánh cửa giữa tiến trình máy chủ và kết nối TCP. Máy khách gửi tin nhắn yêu cầu HTTP vào giao diện socket của nó và nhận HTTP tin nhắn phản hồi từ giao diện socket của nó. Tương tự, máy chủ HTTP nhận thông báo yêu cầu từ giao diện ổ cắm của nó và gửi thông báo phản hồi đến giao diện ổ cắm của nó. Sau khi máy khách gửi tin nhắn vào giao diện ổ cắm của nó, tin nhắn đó sẽ không nằm trong tay máy khách và "nằm trong tay" của TCP. Hãy nhớ lại Phần 2.1 rằng TCP cung cấp dịch vụ truyền dữ liệu đáng tin cậy tới HTTP. Điều này ngụ ý rằng mỗi thông báo yêu cầu HTTP được gửi bởi tiến trình máy khách cuối cùng sẽ đến máy chủ nguyên vẹn; tương tự, mỗi thông báo phản hồi HTTP được gửi bởi quy trình máy chủ cuối cùng sẽ đến máy khách nguyên vẹn. Ở đây chúng ta thấy một trong những lợi thế lớn của kiến ​​trúc phân lớp---HTTP không cần phải lo lắng về dữ liệu bị mất hoặc chi tiết về cách TCP khôi phục sau khi mất hoặc sắp xếp lại dữ liệu trong mạng. Đó là công việc của TCP và các giao thức ở các lớp thấp hơn của ngăn xếp giao thức.

Điều quan trọng cần lưu ý là máy chủ gửi các tệp được yêu cầu đến máy khách mà không lưu trữ bất kỳ thông tin trạng thái nào về máy khách. Nếu một máy khách cụ thể yêu cầu cùng một đối tượng hai lần trong khoảng thời gian vài giây, thì máy chủ sẽ không phản hồi bằng cách nói rằng nó chỉ phục vụ đối tượng đó cho máy khách; thay vào đó, máy chủ sẽ gửi lại đối tượng vì nó đã hoàn toàn quên mất những gì nó đã làm trước đó. Bởi vì máy chủ HTTP duy trì

HTTP yêu cầu

HTTP phản hồi

HTTP phản hồi

HTTP yêu cầu

PC chạy Internet Explorer

Điện thoại thông minh Android chạy Google Chrome

Máy chủ chạy máy chủ Web Apache

*Hình 2.6 ♦ HTTP hành vi phản hồi yêu cầu*

không có thông tin về khách hàng, HTTP được cho là giao thức không trạng thái. Chúng tôi cũng lưu ý rằng Web sử dụng kiến ​​trúc ứng dụng máy khách-máy chủ, như được mô tả trong Phần 2.1. Máy chủ Web luôn hoạt động với địa chỉ IP cố định và phục vụ các yêu cầu từ hàng triệu trình duyệt khác nhau.

Phiên bản gốc của HTTP được gọi là HTTP/1.0 và có từ đầu những năm 1990 \[RFC 1945\]. Tính đến năm 2020, phần lớn giao dịch HTTP diễn ra trên HTTP/1.1 \[RFC 7230\]. Tuy nhiên, ngày càng có nhiều trình duyệt và máy chủ Web hỗ trợ phiên bản mới của HTTP có tên HTTP/2 \[RFC 7540\]. Ở cuối phần này, chúng tôi sẽ giới thiệu về HTTP/2.

**2.2.2 Kết nối không liên tục và liên tục**

Trong nhiều ứng dụng Internet, máy khách và máy chủ giao tiếp trong một khoảng thời gian dài, máy khách thực hiện một loạt yêu cầu và máy chủ phản hồi từng yêu cầu đó. Tùy thuộc vào ứng dụng và cách ứng dụng đang được sử dụng, hàng loạt yêu cầu có thể được thực hiện liên tục, định kỳ theo khoảng thời gian đều đặn hoặc không liên tục. Khi tương tác máy khách-máy chủ này diễn ra trên TCP, nhà phát triển ứng dụng cần đưa ra quyết định quan trọng---mỗi cặp yêu cầu/phản hồi nên được gửi qua một kết nối TCP riêng biệt hay tất cả các yêu cầu và phản hồi tương ứng của chúng nên được gửi qua cùng một kết nối TCP? Theo cách tiếp cận trước đây, ứng dụng được cho là sử dụng các kết nối không liên tục; và trong cách tiếp cận thứ hai, các kết nối liên tục. Để hiểu sâu hơn về vấn đề thiết kế này, chúng ta hãy xem xét ưu điểm và nhược điểm của kết nối liên tục trong bối cảnh của một ứng dụng cụ thể, cụ thể là HTTP, có thể sử dụng cả kết nối không liên tục và kết nối liên tục. Mặc dù HTTP sử dụng các kết nối liên tục ở chế độ mặc định, nhưng thay vào đó, HTTP máy khách và máy chủ có thể được định cấu hình để sử dụng các kết nối không liên tục.

HTTP với kết nối không liên tục

Hãy xem qua các bước chuyển một trang Web từ máy chủ sang máy khách trong trường hợp kết nối không liên tục. Giả sử trang này bao gồm một tệp HTML cơ bản và 10 hình ảnh JPEG và tất cả 11 đối tượng này đều nằm trên cùng một máy chủ. Hơn nữa, giả sử URL của tệp HTML cơ sở là

http://www.someSchool.edu/someDepartment/home.index

Đây là những gì xảy ra:

1\. Quá trình máy khách HTTP khởi tạo kết nối TCP tới máy chủ

www.someSchool.edu trên cổng số 80, đây là số cổng mặc định cho HTTP. Được liên kết với kết nối TCP, sẽ có một ổ cắm ở máy khách và một ổ cắm ở máy chủ.

2\. Máy khách HTTP gửi thông báo yêu cầu HTTP tới máy chủ thông qua ổ cắm của nó.

Thông báo yêu cầu bao gồm tên đường dẫn /someDepartment/home .index. (Chúng ta sẽ thảo luận chi tiết về thông báo HTTP bên dưới.) 3. Tiến trình máy chủ HTTP nhận thông báo yêu cầu qua socket của nó, truy xuất

đối tượng /someDepartment/home.index từ bộ lưu trữ của nó (RAM hoặc đĩa), đóng gói đối tượng trong thông báo phản hồi HTTP và gửi thông báo phản hồi đến máy khách thông qua ổ cắm của nó. 4. Quá trình máy chủ HTTP yêu cầu TCP đóng kết nối TCP. (Nhưng TCP

không thực sự chấm dứt kết nối cho đến khi nó biết chắc chắn rằng máy khách đã nhận được thông báo phản hồi nguyên vẹn.) 5. Máy khách HTTP nhận được thông báo phản hồi. Điểm kết nối TCP

nates. Thông báo cho biết đối tượng được đóng gói là một tệp HTML. Máy khách trích xuất tệp từ thông báo phản hồi, kiểm tra tệp HTML và tìm các tham chiếu đến 10 đối tượng JPEG. 6. Sau đó, bốn bước đầu tiên được lặp lại cho từng đối tượng JPEG được tham chiếu.

Khi trình duyệt nhận được trang Web, nó sẽ hiển thị trang đó cho người dùng. Hai trình duyệt khác nhau có thể diễn giải (nghĩa là hiển thị cho người dùng) một trang Web theo những cách hơi khác nhau. HTTP không liên quan gì đến cách khách hàng diễn giải một trang Web. Thông số kỹ thuật HTTP (\[RFC 1945\] và \[RFC 7540\]) chỉ xác định giao thức liên lạc giữa chương trình HTTP máy khách và chương trình HTTP máy chủ.

Các bước trên minh họa cách sử dụng kết nối không liên tục, trong đó mỗi kết nối TCP được đóng sau khi máy chủ gửi đối tượng---kết nối không tồn tại đối với các đối tượng khác. HTTP/1.0 sử dụng kết nối TCP không liên tục. Lưu ý rằng mỗi kết nối TCP không liên tục sẽ truyền tải chính xác một thông báo yêu cầu và một thông báo phản hồi. Do đó, trong ví dụ này, khi người dùng yêu cầu trang Web, 11 kết nối TCP sẽ được tạo.

Trong các bước được mô tả ở trên, chúng tôi đã cố tình mơ hồ về việc liệu máy khách có nhận được 10 ảnh JPEG qua 10 kết nối TCP nối tiếp hay liệu một số ảnh JPEG có được nhận qua các kết nối TCP song song hay không. Thật vậy, người dùng có thể định cấu hình một số trình duyệt để kiểm soát mức độ song song. Trình duyệt có thể mở nhiều kết nối TCP và yêu cầu các phần khác nhau của trang Web qua nhiều kết nối. Như chúng ta sẽ thấy trong chương tiếp theo, việc sử dụng các kết nối song song sẽ rút ngắn thời gian phản hồi.

Trước khi tiếp tục, hãy thực hiện phép tính tổng thể để ước tính khoảng thời gian trôi qua kể từ khi khách hàng yêu cầu tệp HTML cơ sở cho đến khi khách hàng nhận được toàn bộ tệp. Để đạt được mục đích này, chúng tôi xác định thời gian khứ hồi (RTT), là thời gian cần thiết để một gói nhỏ di chuyển từ máy khách đến máy chủ và sau đó quay lại máy khách. RTT bao gồm độ trễ truyền gói, độ trễ xếp hàng gói trong các bộ định tuyến và chuyển mạch trung gian cũng như độ trễ xử lý gói. (Những độ trễ này đã được thảo luận trong Phần 1.4.) Bây giờ hãy xem xét điều gì xảy ra khi người dùng nhấp vào một siêu liên kết. Như được hiển thị trong Hình 2.7, điều này khiến trình duyệt khởi tạo kết nối TCP giữa trình duyệt và máy chủ Web; điều này liên quan đến

"bắt tay ba chiều"---máy khách gửi một phân đoạn TCP nhỏ đến máy chủ, máy chủ xác nhận và phản hồi bằng một phân đoạn TCP nhỏ và cuối cùng, máy khách xác nhận lại máy chủ. Hai phần đầu tiên của quá trình bắt tay ba chiều chiếm một RTT. Sau khi hoàn thành hai phần đầu tiên của quá trình bắt tay, khách hàng sẽ gửi thông báo yêu cầu HTTP kết hợp với phần thứ ba của quá trình bắt tay ba chiều (sự xác nhận) vào kết nối TCP. Khi thông báo yêu cầu đến máy chủ, máy chủ sẽ gửi tệp HTML vào kết nối TCP. Yêu cầu/phản hồi HTTP này sẽ chiếm hết RTT khác. Do đó, đại khái, tổng thời gian phản hồi là hai RTT cộng với thời gian truyền tệp HTML tại máy chủ.

HTTP với kết nối liên tục

Kết nối không liên tục có một số thiếu sót. Đầu tiên, một kết nối hoàn toàn mới phải được thiết lập và duy trì cho từng đối tượng được yêu cầu. Đối với mỗi kết nối này, bộ đệm TCP phải được phân bổ và các biến TCP phải được lưu giữ trong cả máy khách và máy chủ. Điều này có thể đặt một gánh nặng đáng kể lên máy chủ Web, nơi có thể phục vụ đồng thời các yêu cầu từ hàng trăm máy khách khác nhau. Thứ hai,

Thời gian tại khách hàng

Thời gian ở máy chủ

Bắt đầu kết nối TCP

RTT

Tệp yêu cầu

RTT

Đã nhận được toàn bộ tập tin

Thời gian truyền file

*Hình 2.7 ♦ Tính toán mặt sau cho thời gian cần thiết*

để yêu cầu và nhận một tệp HTML

như chúng tôi vừa mô tả, mỗi đối tượng phải chịu độ trễ phân phối hai RTT---một RTT để thiết lập kết nối TCP và một RTT để yêu cầu và nhận một đối tượng.

Với kết nối liên tục HTTP/1.1, máy chủ sẽ để kết nối TCP mở sau khi gửi phản hồi. Các yêu cầu và phản hồi tiếp theo giữa cùng một máy khách và máy chủ có thể được gửi qua cùng một kết nối. Cụ thể, toàn bộ trang Web (trong ví dụ trên, tệp HTML cơ sở và 10 hình ảnh) có thể được gửi qua một kết nối TCP liên tục duy nhất. Hơn nữa, nhiều trang Web nằm trên cùng một máy chủ có thể được gửi từ máy chủ đến cùng một máy khách qua một kết nối TCP liên tục duy nhất. Những yêu cầu đối với các đối tượng này có thể được thực hiện liên tiếp mà không cần chờ phản hồi cho các yêu cầu đang chờ xử lý (đường ống). Thông thường, máy chủ HTTP sẽ đóng kết nối khi không được sử dụng trong một thời gian nhất định (khoảng thời gian chờ có thể định cấu hình). Khi máy chủ nhận được yêu cầu quay lại, nó sẽ gửi các đối tượng quay lại. Chế độ mặc định của HTTP sử dụng kết nối liên tục với đường ống. Chúng ta sẽ so sánh một cách định lượng hiệu suất của các kết nối không liên tục và liên tục trong các bài tập về nhà ở Chương 2 và 3. Bạn cũng nên xem \[Heidemann 1997; Nielsen 1997; RFC 7540\].

**2.2.3 HTTP Định dạng tin nhắn**

Thông số kỹ thuật HTTP \[RFC 1945; RFC 7230; RFC 7540\] bao gồm các định nghĩa về định dạng thông báo HTTP. Có hai loại tin nhắn HTTP, tin nhắn yêu cầu và tin nhắn phản hồi, cả hai loại này đều được thảo luận bên dưới.

HTTP Tin nhắn yêu cầu

Dưới đây chúng tôi cung cấp thông báo yêu cầu HTTP điển hình:

GET /somedir/page.html HTTP/1.1 Host: www.someschool.edu Kết nối: đóng Tác nhân người dùng: Mozilla/5.0 Ngôn ngữ chấp nhận: fr

Chúng ta có thể học được nhiều điều bằng cách xem xét kỹ thông báo yêu cầu đơn giản này. Trước hết, chúng ta thấy rằng tin nhắn được viết bằng văn bản ASCII thông thường, để một người có trình độ máy tính bình thường có thể đọc được nó. Thứ hai, chúng ta thấy rằng thông báo bao gồm năm dòng, mỗi dòng theo sau là một dấu xuống dòng và một dòng cấp dữ liệu. Dòng cuối cùng được theo sau bởi một dòng trả về đầu dòng và nguồn cấp dữ liệu bổ sung. Mặc dù thông báo yêu cầu cụ thể này có năm dòng, nhưng thông báo yêu cầu có thể có nhiều dòng hơn hoặc chỉ có một dòng. Dòng đầu tiên của thông báo yêu cầu HTTP được gọi là dòng yêu cầu; các dòng tiếp theo được gọi là dòng tiêu đề. Dòng yêu cầu có ba trường: trường phương thức, trường URL và trường phiên bản HTTP. Trường phương thức có thể nhận nhiều giá trị khác nhau, bao gồm GET, POST, HEAD, PUT và DELETE.

Phần lớn các tin nhắn yêu cầu HTTP sử dụng phương thức GET. Phương thức GET được sử dụng khi trình duyệt yêu cầu một đối tượng, với đối tượng được yêu cầu được xác định trong trường URL. Trong ví dụ này, trình duyệt đang yêu cầu đối tượng /somedir/ page.html. Phiên bản này đã tự giải thích; trong ví dụ này, trình duyệt triển khai phiên bản HTTP/1.1.

Bây giờ hãy xem các dòng tiêu đề trong ví dụ. Dòng tiêu đề Host: www.someschool.edu chỉ định máy chủ chứa đối tượng. Bạn có thể cho rằng dòng tiêu đề này là không cần thiết vì đã có sẵn kết nối TCP với máy chủ. Tuy nhiên, như chúng ta sẽ thấy trong Phần 2.2.5, thông tin được cung cấp bởi dòng tiêu đề máy chủ được yêu cầu bởi bộ đệm proxy Web. Bằng cách bao gồm dòng tiêu đề Connection: close, trình duyệt sẽ thông báo cho máy chủ rằng nó không muốn bận tâm đến các kết nối liên tục; nó muốn máy chủ đóng kết nối sau khi gửi đối tượng được yêu cầu. Dòng tiêu đề User-agent: chỉ định tác nhân người dùng, tức là loại trình duyệt đang thực hiện yêu cầu tới máy chủ. Ở đây tác nhân người dùng là Mozilla/5.0, một trình duyệt Firefox. Dòng tiêu đề này hữu ích vì máy chủ thực sự có thể gửi các phiên bản khác nhau của cùng một đối tượng tới các loại tác nhân người dùng khác nhau. (Mỗi phiên bản được xử lý bằng cùng một URL.) Cuối cùng, tiêu đề Ngôn ngữ chấp nhận: cho biết rằng người dùng muốn nhận phiên bản tiếng Pháp của đối tượng, nếu đối tượng đó tồn tại trên máy chủ; nếu không, máy chủ sẽ gửi phiên bản mặc định của nó. Tiêu đề Ngôn ngữ chấp nhận: chỉ là một trong nhiều tiêu đề đàm phán nội dung có sẵn trong HTTP.

Sau khi xem một ví dụ, bây giờ chúng ta hãy xem định dạng chung của một thông báo yêu cầu, như trong Hình 2.8. Chúng tôi thấy rằng định dạng chung tuân theo ví dụ trước đó của chúng tôi. Tuy nhiên, bạn có thể nhận thấy rằng sau các dòng tiêu đề (và dấu xuống dòng bổ sung và nguồn cấp dữ liệu dòng) có một "nội dung thực thể". Cơ quan thực thể

phương pháp sp sp cr lf

tên trường tiêu đề cr lf:

Header dòng

Dòng trống

Cơ thể thực thể

Dòng yêu cầu

giá trị sp

cr lf

cr lf

tên trường tiêu đề: giá trị sp

Phiên bản URL

*Hình 2.8 ♦ Định dạng chung của thông báo yêu cầu HTTP*

trống với phương thức GET nhưng được sử dụng với phương thức POST. Ứng dụng khách HTTP thường sử dụng phương thức POST khi người dùng điền vào biểu mẫu---ví dụ: khi người dùng cung cấp từ tìm kiếm cho công cụ tìm kiếm. Với thông báo POST, người dùng vẫn yêu cầu một trang Web từ máy chủ, nhưng nội dung cụ thể của trang Web phụ thuộc vào những gì người dùng đã nhập vào các trường biểu mẫu. Nếu giá trị của trường phương thức là POST thì phần nội dung thực thể chứa nội dung người dùng đã nhập vào các trường biểu mẫu.

Sẽ thật thiếu sót nếu không đề cập rằng yêu cầu được tạo bằng biểu mẫu không nhất thiết phải sử dụng phương thức POST. Thay vào đó, biểu mẫu HTML thường sử dụng phương thức GET và bao gồm dữ liệu đã nhập (trong các trường biểu mẫu) trong URL được yêu cầu. Ví dụ: nếu một biểu mẫu sử dụng phương thức GET, có hai trường và đầu vào của hai trường là khỉ và chuối thì URL sẽ có cấu trúc www.somesite.com/animalsearch?monkeys&bananas. Trong quá trình lướt Web hàng ngày của bạn, có thể bạn đã nhận thấy các URL mở rộng thuộc loại này.

Phương thức HEAD tương tự như phương thức GET. Khi máy chủ nhận được yêu cầu bằng phương thức HEAD, nó sẽ phản hồi bằng thông báo HTTP nhưng sẽ loại bỏ đối tượng được yêu cầu. Các nhà phát triển ứng dụng thường sử dụng phương thức HEAD để gỡ lỗi. Phương pháp PUT thường được sử dụng cùng với các công cụ xuất bản Web. Nó cho phép người dùng tải một đối tượng lên một đường dẫn (thư mục) cụ thể trên một máy chủ Web cụ thể. Phương pháp PUT cũng được sử dụng bởi các ứng dụng cần tải đối tượng lên máy chủ Web. Phương thức DELETE cho phép người dùng hoặc ứng dụng xóa một đối tượng trên máy chủ Web.

HTTP Tin nhắn phản hồi

Dưới đây chúng tôi cung cấp thông báo phản hồi HTTP điển hình. Thông báo phản hồi này có thể là phản hồi cho thông báo yêu cầu ví dụ vừa thảo luận.

HTTP/1.1 200 OK Kết nối: đóng Ngày: Thứ ba, ngày 18 tháng 8 năm 2015 15:44:04 GMT Máy chủ: Apache/2.2.3 (CentOS) Sửa đổi lần cuối: Thứ ba, ngày 18 tháng 8 năm 2015 15:11:03 GMT Độ dài nội dung: 6821 Loại nội dung: văn bản/html

(dữ liệu dữ liệu dữ liệu dữ liệu dữ liệu \...)

Chúng ta hãy xem xét cẩn thận thông báo phản hồi này. Nó có ba phần: một dòng trạng thái ban đầu, sáu dòng tiêu đề và sau đó là phần nội dung thực thể. Phần thân thực thể là phần cốt lõi của thông báo---nó chứa chính đối tượng được yêu cầu (được biểu thị bằng dữ liệu dữ liệu dữ liệu dữ liệu dữ liệu \...). Dòng trạng thái có ba trường: trường phiên bản giao thức, mã trạng thái và thông báo trạng thái tương ứng. Trong ví dụ này, dòng trạng thái cho biết rằng máy chủ đang sử dụng HTTP/1.1 và mọi thứ đều ổn (nghĩa là máy chủ đã tìm thấy và đang gửi đối tượng được yêu cầu).

Bây giờ chúng ta hãy nhìn vào các dòng tiêu đề. Máy chủ sử dụng dòng tiêu đề Connection: close để thông báo cho máy khách rằng nó sẽ đóng kết nối TCP sau khi gửi tin nhắn. Dòng tiêu đề Date: cho biết ngày và giờ khi máy chủ tạo và gửi phản hồi HTTP. Lưu ý rằng đây không phải là thời điểm đối tượng được tạo hoặc sửa đổi lần cuối; đó là lúc máy chủ truy xuất đối tượng từ hệ thống tệp của nó, chèn đối tượng vào thông báo phản hồi và gửi thông báo phản hồi. Dòng tiêu đề Máy chủ: cho biết rằng thông báo được tạo bởi máy chủ Web Apache; nó tương tự như dòng tiêu đề User-agent: trong thông báo yêu cầu HTTP. Dòng tiêu đề Last-Modified: cho biết ngày và giờ đối tượng được tạo hoặc sửa đổi lần cuối. Tiêu đề Last-Modified: mà chúng tôi sẽ sớm đề cập chi tiết hơn, rất quan trọng đối với bộ nhớ đệm đối tượng, cả trong máy khách cục bộ và máy chủ bộ đệm mạng (còn được gọi là máy chủ proxy). Dòng tiêu đề Độ dài nội dung: cho biết số byte trong đối tượng được gửi. Dòng tiêu đề Content-Type: cho biết đối tượng trong phần nội dung thực thể là văn bản HTML. (Loại đối tượng được biểu thị chính thức bằng tiêu đề Content-Type: chứ không phải bằng phần mở rộng tệp.)

Sau khi xem xét một ví dụ, bây giờ chúng ta hãy xem xét định dạng chung của một thông báo phản hồi, được hiển thị trong Hình 2.9. Định dạng chung này của thông báo phản hồi khớp với ví dụ trước về thông báo phản hồi. Hãy nói thêm một vài từ về mã trạng thái và cụm từ của chúng. Mã trạng thái và cụm từ liên quan cho biết kết quả của yêu cầu. Một số mã trạng thái phổ biến và các cụm từ liên quan bao gồm:

• 200 OK: Yêu cầu thành công và thông tin được trả về trong phản hồi. • 301 Đã di chuyển vĩnh viễn: Đối tượng được yêu cầu đã được di chuyển vĩnh viễn; URL mới được chỉ định trong tiêu đề Vị trí: của thông báo phản hồi. Phần mềm máy khách sẽ tự động truy xuất URL mới.

phiên bản sp sp cr lf

tên trường tiêu đề cr lf:

Header dòng

Dòng trống

Cơ thể thực thể

Dòng trạng thái

giá trị

cr

sp

sp lf

cr lf

tên trường tiêu đề: giá trị

cụm từ mã trạng thái

*Hình 2.9 ♦ Định dạng chung của thông báo phản hồi HTTP*

• 400 Yêu cầu Không hợp lệ: Đây là mã lỗi chung cho biết rằng máy chủ không thể hiểu được yêu cầu. • 404 Not Found: Tài liệu được yêu cầu không tồn tại trên máy chủ này. • 505 HTTP Phiên bản không được hỗ trợ: Phiên bản giao thức HTTP được yêu cầu không được máy chủ hỗ trợ.

Bạn muốn xem thông báo phản hồi HTTP thực tế như thế nào? Điều này rất được khuyến khích và rất dễ thực hiện! Telnet đầu tiên vào máy chủ Web yêu thích của bạn. Sau đó nhập thông báo yêu cầu một dòng cho một số đối tượng được lưu trữ trên máy chủ. Ví dụ: nếu bạn có quyền truy cập vào dấu nhắc lệnh, hãy nhập:

telnet gaia.cs.umass.edu 80

NHẬN /kurose_ross/interactive/index.php HTTP/1.1 Host: gaia.cs.umass.edu

(Nhấn dấu xuống dòng hai lần sau khi nhập dòng cuối cùng.) Thao tác này sẽ mở kết nối TCP tới cổng 80 của máy chủ gaia.cs.umass.edu và sau đó gửi thông báo yêu cầu HTTP. Bạn sẽ thấy thông báo phản hồi bao gồm tệp HTML cơ sở cho các bài tập về nhà tương tác của sách giáo khoa này. Nếu bạn chỉ muốn xem các dòng thông báo HTTP và không nhận chính đối tượng đó, hãy thay thế GET bằng HEAD.

Trong phần này, chúng ta đã thảo luận về một số dòng tiêu đề có thể được sử dụng trong các thông báo yêu cầu và phản hồi HTTP. Đặc tả HTTP xác định nhiều, rất nhiều dòng tiêu đề khác có thể được chèn bởi trình duyệt, máy chủ Web và máy chủ bộ đệm mạng. Chúng tôi chỉ đề cập đến một số lượng nhỏ trong tổng số các dòng tiêu đề. Chúng tôi sẽ đề cập thêm một số vấn đề bên dưới và một số nhỏ khác khi thảo luận về bộ nhớ đệm Web mạng trong Phần 2.2.5. Một cuộc thảo luận toàn diện và dễ đọc về giao thức HTTP, bao gồm các tiêu đề và mã trạng thái của nó, được đưa ra trong \[Krishnamurthy 2001\].

Làm cách nào để trình duyệt quyết định những dòng tiêu đề nào sẽ được đưa vào thông báo yêu cầu? Làm thế nào để máy chủ Web quyết định những dòng tiêu đề nào sẽ được đưa vào thông báo phản hồi? Trình duyệt sẽ tạo các dòng tiêu đề theo chức năng của loại và phiên bản trình duyệt, cấu hình người dùng của trình duyệt và liệu trình duyệt hiện có phiên bản đối tượng được lưu trong bộ nhớ đệm hay không, nhưng có thể đã lỗi thời. Máy chủ web hoạt động tương tự: Có các sản phẩm, phiên bản và cấu hình khác nhau, tất cả đều ảnh hưởng đến dòng tiêu đề nào được đưa vào thông báo phản hồi.

**2.2.4 Tương tác giữa người dùng và máy chủ: Cookie**

Chúng tôi đã đề cập ở trên rằng máy chủ HTTP không có trạng thái. Điều này giúp đơn giản hóa việc thiết kế máy chủ và cho phép các kỹ sư phát triển các máy chủ Web hiệu suất cao có thể xử lý hàng nghìn kết nối TCP đồng thời. Tuy nhiên, điều mong muốn đối với một trang Web là xác định người dùng vì máy chủ muốn hạn chế quyền truy cập của người dùng.

Sử dụng Wireshark để điều tra giao thức HTTP

VideoLưu ý

hoặc vì nó muốn cung cấp nội dung như một chức năng nhận dạng người dùng. Vì những mục đích này, HTTP sử dụng cookie. Cookie, được định nghĩa trong \[RFC 6265\], cho phép các trang web theo dõi người dùng. Hầu hết các trang web thương mại lớn hiện nay đều sử dụng cookie.

Như được hiển thị trong Hình 2.10, công nghệ cookie có bốn thành phần: (1) dòng tiêu đề cookie trong thông báo phản hồi HTTP; (2) dòng tiêu đề cookie trong thông báo yêu cầu HTTP; (3) tệp cookie được lưu giữ trên hệ thống cuối của người dùng và được quản lý bởi trình duyệt của người dùng; và (4) cơ sở dữ liệu phụ trợ tại trang Web. Sử dụng Hình 2.10, hãy xem qua một ví dụ về cách hoạt động của cookie. Giả sử Susan, người luôn

Máy chủ máy khách Máy chủ máy chủ

tin nhắn yêu cầu http thông thường

phản hồi http thông thường

Set-cookie: 1678

cookie thông báo yêu cầu http thông thường: 1678

tin nhắn phản hồi http thông thường

cookie thông báo yêu cầu http thông thường: 1678

tin nhắn phản hồi http thông thường

Thời gian

Một tuần sau

ebay: 8734

Máy chủ tạo ID 1678 cho người dùng

Thời gian

Tệp cookie

Chìa khóa:

amazon: 1678

ebay: 8734

amazon: 1678

ebay: 8734

Hành động dành riêng cho cookie

truy cập

truy cập

mục nhập trong cơ sở dữ liệu phụ trợ

Hành động dành riêng cho cookie

*Hình 2.10 ♦ Giữ trạng thái người dùng bằng cookie*

truy cập Web bằng Internet Explorer từ PC ở nhà của cô ấy, liên hệ với Amazon.com lần đầu tiên. Giả sử rằng trước đây cô ấy đã truy cập trang eBay. Khi yêu cầu đến máy chủ Amazon Web, máy chủ sẽ tạo một số nhận dạng duy nhất và tạo một mục nhập trong cơ sở dữ liệu phụ trợ được lập chỉ mục theo số nhận dạng. Sau đó, máy chủ Web Amazon sẽ phản hồi trình duyệt của Susan, bao gồm trong phản hồi HTTP một tiêu đề Set-cookie: chứa số nhận dạng. Ví dụ: dòng tiêu đề có thể là:

Set-cookie: 1678

Khi trình duyệt của Susan nhận được thông báo phản hồi HTTP, nó sẽ thấy tiêu đề Set-cookie:. Sau đó, trình duyệt sẽ thêm một dòng vào tệp cookie đặc biệt mà nó quản lý. Dòng này bao gồm tên máy chủ của máy chủ và số nhận dạng trong tiêu đề Set-cookie:. Lưu ý rằng tệp cookie đã có mục nhập cho eBay vì Susan đã truy cập trang đó trước đây. Khi Susan tiếp tục duyệt trang Amazon, mỗi lần cô ấy yêu cầu một trang Web, trình duyệt của cô ấy sẽ tra cứu tệp cookie của cô ấy, trích xuất số nhận dạng của cô ấy cho trang web này và đặt một dòng tiêu đề cookie bao gồm số nhận dạng trong yêu cầu HTTP. Cụ thể, mỗi yêu cầu HTTP của cô gửi tới máy chủ Amazon đều bao gồm dòng tiêu đề:

Bánh quy: 1678

Bằng cách này, máy chủ Amazon có thể theo dõi hoạt động của Susan trên trang Amazon. Mặc dù trang web Amazon không nhất thiết phải biết tên của Susan, nhưng nó biết chính xác những trang mà người dùng đã truy cập, theo thứ tự nào và vào thời gian nào! Amazon sử dụng cookie để cung cấp dịch vụ giỏ hàng của mình---Amazon có thể duy trì danh sách tất cả các giao dịch mua dự định của Susan để cô ấy có thể thanh toán chung cho chúng vào cuối phiên.

Ví dụ: nếu Susan quay lại trang web của Amazon một tuần sau, trình duyệt của cô ấy sẽ tiếp tục đặt dòng tiêu đề Cookie: 1678 trong các thông báo yêu cầu. Amazon cũng giới thiệu các sản phẩm cho Susan dựa trên các trang Web mà cô đã truy cập tại Amazon trước đây. Nếu Susan cũng đăng ký với Amazon---cung cấp tên đầy đủ, địa chỉ email, địa chỉ gửi thư và thông tin thẻ tín dụng---Amazon có thể đưa thông tin này vào cơ sở dữ liệu của mình, từ đó liên kết tên của Susan với số nhận dạng của cô ấy (và tất cả các trang cô ấy đã truy cập tại trang này trước đây!). Đây là cách Amazon và các trang thương mại điện tử khác cung cấp dịch vụ "mua sắm chỉ bằng một cú nhấp chuột"---khi Susan chọn mua một mặt hàng trong lần truy cập tiếp theo, cô ấy không cần nhập lại tên, số thẻ tín dụng hoặc địa chỉ của mình.

Từ cuộc thảo luận này, chúng tôi thấy rằng cookie có thể được sử dụng để nhận dạng người dùng. Lần đầu tiên người dùng truy cập một trang web, người dùng có thể cung cấp thông tin nhận dạng người dùng (có thể là tên của họ). Trong các phiên tiếp theo, trình duyệt chuyển tiêu đề cookie đến máy chủ, từ đó xác định người dùng cho máy chủ. Do đó, cookie có thể được sử dụng để tạo lớp phiên người dùng bên trên HTTP không trạng thái. Ví dụ: khi người dùng đăng nhập vào

một ứng dụng e-mail dựa trên Web (chẳng hạn như Hotmail), trình duyệt sẽ gửi thông tin cookie đến máy chủ, cho phép máy chủ nhận dạng người dùng trong suốt phiên làm việc của người dùng với ứng dụng.

Mặc dù cookie thường đơn giản hóa trải nghiệm mua sắm trên Internet cho người dùng nhưng chúng vẫn gây tranh cãi vì cũng có thể bị coi là xâm phạm quyền riêng tư. Như chúng ta vừa thấy, bằng cách sử dụng kết hợp cookie và thông tin tài khoản do người dùng cung cấp, một trang Web có thể tìm hiểu nhiều điều về người dùng và có khả năng bán thông tin này cho bên thứ ba.

**2.2.5 Bộ nhớ đệm web**

Bộ nhớ đệm Web---còn được gọi là máy chủ proxy---là một thực thể mạng đáp ứng các yêu cầu HTTP thay mặt cho máy chủ Web gốc. Bộ đệm Web có bộ lưu trữ đĩa riêng và giữ bản sao của các đối tượng được yêu cầu gần đây trong bộ lưu trữ này. Như được hiển thị trong Hình 2.11, trình duyệt của người dùng có thể được cấu hình sao cho tất cả các yêu cầu HTTP của người dùng trước tiên được chuyển hướng đến bộ đệm Web \[RFC 7234\]. Khi trình duyệt được định cấu hình, mỗi yêu cầu của trình duyệt cho một đối tượng trước tiên sẽ được chuyển hướng đến bộ đệm Web. Ví dụ: giả sử một trình duyệt đang yêu cầu đối tượng http://www.someschool.edu/ campus.gif. Đây là những gì xảy ra:

1\. Trình duyệt thiết lập kết nối TCP tới bộ đệm Web và gửi HTTP

yêu cầu đối tượng vào bộ đệm Web. 2. Bộ nhớ đệm Web sẽ kiểm tra xem liệu nó có bản sao của đối tượng được lưu trữ cục bộ hay không. Nếu nó

làm như vậy, bộ đệm Web sẽ trả về đối tượng trong thông báo phản hồi HTTP tới trình duyệt máy khách. 3. Nếu bộ đệm Web không có đối tượng, bộ đệm Web sẽ mở kết nối TCP

tới máy chủ gốc, tức là tới www.someschool.edu. Bộ đệm Web

HTTP yêu cầu

HTTP phản hồi

HTTP yêu cầu

HTTP phản hồi

HTTP yêu cầu

HTTP phản hồi

HTTP yêu cầu

HTTP phản hồi

Khách hàng

Nguồn gốc

máy chủ

Nguồn gốc

máy chủ

Khách hàng

Máy chủ proxy

*Hình 2.11 ♦ Máy khách yêu cầu đối tượng thông qua bộ đệm Web*

sau đó gửi yêu cầu HTTP cho đối tượng vào kết nối bộ nhớ đệm tới máy chủ TCP. Sau khi nhận được yêu cầu này, máy chủ gốc sẽ gửi đối tượng trong phản hồi HTTP tới bộ đệm Web. 4. Khi bộ đệm Web nhận được đối tượng, nó sẽ lưu một bản sao vào bộ nhớ cục bộ và

gửi một bản sao, trong thông báo phản hồi HTTP, tới trình duyệt máy khách (qua kết nối TCP hiện có giữa trình duyệt máy khách và bộ đệm Web).

Lưu ý rằng bộ đệm vừa là máy chủ vừa là máy khách. Khi nó nhận được yêu cầu từ và gửi phản hồi tới trình duyệt, nó là một máy chủ. Khi nó gửi yêu cầu đến và nhận phản hồi từ máy chủ gốc, nó là máy khách.

Thông thường, bộ đệm Web được ISP mua và cài đặt. Ví dụ: một trường đại học có thể cài đặt bộ đệm trên mạng của trường và định cấu hình tất cả các trình duyệt của trường để trỏ đến bộ đệm. Hoặc một ISP dân cư lớn (chẳng hạn như Comcast) có thể cài đặt một hoặc nhiều bộ nhớ đệm trong mạng của mình và định cấu hình trước các trình duyệt được cung cấp để trỏ đến các bộ nhớ đệm đã cài đặt.

Bộ nhớ đệm web đã được triển khai trên Internet vì hai lý do. Đầu tiên, bộ đệm Web có thể giảm đáng kể thời gian phản hồi cho một yêu cầu của máy khách, đặc biệt nếu băng thông thắt cổ chai giữa máy khách và máy chủ gốc nhỏ hơn nhiều so với băng thông thắt cổ chai giữa máy khách và bộ đệm. Nếu có kết nối tốc độ cao giữa máy khách và bộ đệm, như thường lệ, và nếu bộ đệm có đối tượng được yêu cầu, thì bộ đệm sẽ có thể phân phối đối tượng một cách nhanh chóng đến máy khách. Thứ hai, như chúng tôi sẽ sớm minh họa bằng một ví dụ, bộ nhớ đệm Web có thể làm giảm đáng kể lưu lượng trên đường liên kết truy cập Internet của tổ chức. Bằng cách giảm lưu lượng truy cập, tổ chức (ví dụ: công ty hoặc trường đại học) không phải nâng cấp băng thông nhanh chóng, do đó giảm chi phí. Hơn nữa, bộ nhớ đệm Web có thể làm giảm đáng kể lưu lượng Web trên Internet nói chung, từ đó cải thiện hiệu suất cho tất cả các ứng dụng.

Để hiểu sâu hơn về lợi ích của bộ nhớ đệm, hãy xem xét một ví dụ trong Hình 2.12. Hình này cho thấy hai mạng---mạng tổ chức và phần còn lại của Internet công cộng. Mạng tổ chức là mạng LAN tốc độ cao. Một bộ định tuyến trong mạng tổ chức và một bộ định tuyến trên Internet được kết nối bằng liên kết 15 Mbps. Các máy chủ gốc được gắn vào Internet nhưng được đặt trên toàn cầu. Giả sử kích thước đối tượng trung bình là 1 Mbits và tốc độ yêu cầu trung bình từ trình duyệt của tổ chức đến máy chủ gốc là 15 yêu cầu mỗi giây. Giả sử rằng các thông báo yêu cầu HTTP có kích thước nhỏ không đáng kể và do đó không tạo ra lưu lượng truy cập nào trong mạng hoặc trong liên kết truy cập (từ bộ định tuyến của tổ chức đến bộ định tuyến Internet). Ngoài ra, giả sử rằng khoảng thời gian cần thiết kể từ khi bộ định tuyến ở phía Internet của liên kết truy cập trong Hình 2.12 chuyển tiếp một yêu cầu HTTP (trong một gói dữ liệu IP) cho đến khi nó nhận được phản hồi (thường là trong nhiều gói dữ liệu IP) là trung bình hai giây. Một cách không chính thức, chúng tôi gọi độ trễ cuối cùng này là "độ trễ Internet".

Tổng thời gian phản hồi---nghĩa là thời gian từ khi trình duyệt yêu cầu một đối tượng cho đến khi nhận được đối tượng---là tổng của độ trễ mạng LAN, độ trễ truy cập (nghĩa là độ trễ giữa hai bộ định tuyến) và độ trễ Internet. Bây giờ chúng ta hãy làm

Internet công cộng

Mạng lưới tổ chức

Liên kết truy cập 15 Mbps

Mạng LAN 100 Mb/giây

Máy chủ gốc

*Hình 2.12 ♦ Điểm nghẽn giữa mạng tổ chức và Internet*

một tính toán rất thô sơ để ước tính độ trễ này. Cường độ lưu lượng trên mạng LAN (xem Phần 1.4.2) là

**(15 yêu cầu/giây) \# (1 Mbits/yêu cầu)/(100 Mbps) = 0,15**

trong khi cường độ lưu lượng truy cập trên liên kết truy cập (từ bộ định tuyến Internet đến bộ định tuyến tổ chức) là

**(15 yêu cầu/giây) \# (1 Mbits/yêu cầu)/(15 Mbps) = 1**

Cường độ lưu lượng 0,15 trên mạng LAN thường dẫn đến độ trễ tối đa là hàng chục mili giây; do đó, chúng ta có thể bỏ qua độ trễ của mạng LAN. Tuy nhiên, như đã thảo luận trong Phần 1.4.2, khi cường độ lưu lượng tiến tới 1 (như trường hợp liên kết truy cập trong Hình 2.12), độ trễ trên liên kết trở nên rất lớn và tăng lên không giới hạn. Do đó, thời gian phản hồi trung bình để đáp ứng các yêu cầu sẽ ở mức vài phút, nếu không muốn nói là nhiều hơn, điều này là không thể chấp nhận được đối với người dùng của tổ chức. Rõ ràng là phải làm gì đó.

Một giải pháp khả thi là tăng tốc độ truy cập từ 15 Mbps lên 100 Mbps. Điều này sẽ giảm cường độ lưu lượng truy cập trên liên kết truy cập xuống 0,15, nghĩa là độ trễ giữa hai bộ định tuyến là không đáng kể. Trong trường hợp này, tổng thời gian phản hồi sẽ khoảng hai giây, tức là độ trễ Internet. Nhưng giải pháp này cũng có nghĩa là tổ chức phải nâng cấp liên kết truy cập của mình từ 15 Mbps lên 100 Mbps, một đề xuất tốn kém.

Bây giờ hãy xem xét giải pháp thay thế là không nâng cấp liên kết truy cập mà thay vào đó cài đặt bộ đệm Web trong mạng tổ chức. Giải pháp này được minh họa trong hình 2.13. Tỷ lệ truy cập---tỷ lệ yêu cầu được bộ đệm đáp ứng--- thường nằm trong khoảng từ 0,2 đến 0,7 trong thực tế. Để minh họa, hãy giả sử rằng bộ đệm cung cấp tỷ lệ truy cập là 0,4 cho tổ chức này. Vì máy khách và bộ đệm được kết nối với cùng một mạng LAN tốc độ cao nên 40% yêu cầu sẽ được bộ đệm đáp ứng gần như ngay lập tức, chẳng hạn như trong vòng 10 mili giây. Tuy nhiên, 60% yêu cầu còn lại vẫn cần được máy chủ gốc đáp ứng. Nhưng chỉ với 60% đối tượng được yêu cầu đi qua liên kết truy cập, cường độ lưu lượng truy cập trên liên kết truy cập sẽ giảm từ 1,0 xuống 0,6. Thông thường, một

Internet công cộng

Mạng lưới tổ chức

Liên kết truy cập 15 Mbps

Thể chế

bộ nhớ đệm

Mạng LAN 100 Mb/giây

Máy chủ gốc

*Hình 2.13 ♦ Thêm bộ đệm vào mạng tổ chức*

cường độ lưu lượng nhỏ hơn 0,8 tương ứng với độ trễ nhỏ, chẳng hạn như hàng chục mili giây, trên liên kết 15 Mbps. Độ trễ này không đáng kể so với độ trễ hai giây của Internet. Với những cân nhắc này, do đó độ trễ trung bình là

**0,4 \# (0,01 giây) + 0,6 \# (2,01 giây)**

chỉ lớn hơn 1,2 giây một chút. Do đó, giải pháp thứ hai này thậm chí còn cung cấp thời gian phản hồi thấp hơn giải pháp đầu tiên và không yêu cầu tổ chức nâng cấp liên kết với Internet. Tất nhiên, tổ chức này phải mua và cài đặt bộ đệm Web. Nhưng chi phí này thấp---nhiều bộ nhớ đệm sử dụng phần mềm miền công cộng chạy trên các PC rẻ tiền.

Thông qua việc sử dụng Mạng phân phối nội dung (CDN), bộ nhớ đệm Web ngày càng đóng một vai trò quan trọng trên Internet. Một công ty CDN cài đặt nhiều bộ đệm được phân phối theo địa lý trên Internet, từ đó bản địa hóa phần lớn lưu lượng truy cập. Có CDN dùng chung (như Akamai và Limelight) và CDN chuyên dụng (như Google và Netflix). Chúng ta sẽ thảo luận chi tiết hơn về CDN trong Phần 2.6.

GET có điều kiện

Mặc dù bộ nhớ đệm có thể làm giảm thời gian phản hồi của người dùng nhưng nó gây ra một vấn đề mới---bản sao của một đối tượng nằm trong bộ nhớ đệm có thể đã cũ. Nói cách khác, đối tượng nằm trong máy chủ Web có thể đã được sửa đổi do bản sao được lưu vào bộ nhớ đệm ở máy khách. May mắn thay, HTTP có cơ chế cho phép bộ đệm xác minh rằng các đối tượng của nó đã được cập nhật. Cơ chế này được gọi là GET có điều kiện \[RFC 7232\]. Thông báo yêu cầu HTTP được gọi là thông báo GET có điều kiện nếu (1) thông báo yêu cầu sử dụng phương thức GET và (2) thông báo yêu cầu bao gồm dòng tiêu đề If-Modified-Since:.

Để minh họa cách hoạt động của GET có điều kiện, chúng ta hãy xem qua một ví dụ. Đầu tiên, thay mặt cho trình duyệt yêu cầu, bộ đệm proxy sẽ gửi thông báo yêu cầu đến máy chủ Web:

NHẬN /fruit/kiwi.gif HTTP/1.1 Host: www.exotiquecuisine.com

Thứ hai, máy chủ Web gửi thông báo phản hồi có đối tượng được yêu cầu tới bộ đệm:

HTTP/1.1 200 OK Ngày: Thứ bảy, ngày 3 tháng 10 năm 2015 15:39:29 Máy chủ: Apache/1.3.0 (Unix) Sửa đổi lần cuối: Thứ tư, ngày 9 tháng 9 năm 2015 09:23:24 Loại nội dung: image/gif

(dữ liệu dữ liệu dữ liệu dữ liệu dữ liệu \...)

Bộ đệm chuyển tiếp đối tượng đến trình duyệt yêu cầu nhưng cũng lưu trữ đối tượng cục bộ. Điều quan trọng là bộ đệm cũng lưu trữ ngày sửa đổi lần cuối cùng với đối tượng. Thứ ba, một tuần sau, một trình duyệt khác yêu cầu cùng một đối tượng thông qua bộ đệm và đối tượng đó vẫn còn trong bộ đệm. Vì đối tượng này có thể đã được sửa đổi tại máy chủ Web trong tuần qua nên bộ nhớ đệm sẽ thực hiện kiểm tra cập nhật bằng cách đưa ra lệnh GET có điều kiện. Cụ thể, bộ đệm sẽ gửi:

GET /fruit/kiwi.gif HTTP/1.1 Host: www.exotiquecuisine.com If-modified-since: Thứ Tư, ngày 9 tháng 9 năm 2015 09:23:24

Lưu ý rằng giá trị của dòng tiêu đề If-modified-since: hoàn toàn bằng giá trị của dòng tiêu đề Last-Modified: được máy chủ gửi một tuần trước. GET có điều kiện này yêu cầu máy chủ chỉ gửi đối tượng nếu đối tượng đã được sửa đổi kể từ ngày được chỉ định. Giả sử đối tượng chưa được sửa đổi kể từ ngày 9 tháng 9 năm 2015 09:23:24. Sau đó, thứ tư, máy chủ Web gửi thông báo phản hồi tới bộ đệm:

HTTP/1.1 304 Chưa sửa đổi Ngày: Thứ bảy, ngày 10 tháng 10 năm 2015 15:39:29 Máy chủ: Apache/1.3.0 (Unix)

(nội dung thực thể trống)

Chúng tôi thấy rằng để đáp lại GET có điều kiện, máy chủ Web vẫn gửi thông báo phản hồi nhưng không bao gồm đối tượng được yêu cầu trong thông báo phản hồi. Việc bao gồm đối tượng được yêu cầu sẽ chỉ lãng phí băng thông và tăng thời gian phản hồi trong nhận thức của người dùng, đặc biệt nếu đối tượng có kích thước lớn. Lưu ý rằng thông báo phản hồi cuối cùng này có 304 Not Modified trong dòng trạng thái, thông báo này cho bộ đệm biết rằng nó có thể tiếp tục và chuyển tiếp bản sao đối tượng được lưu trong bộ nhớ đệm (của bộ đệm proxy) tới trình duyệt yêu cầu.

**2.2.6 HTTP/2**

HTTP/2 \[RFC 7540\], được chuẩn hóa vào năm 2015, là phiên bản mới đầu tiên của HTTP kể từ HTTP/1.1, được chuẩn hóa vào năm 1997. Kể từ khi chuẩn hóa, HTTP/2 đã phát triển, với hơn 40% trong số 10 triệu trang web hàng đầu hỗ trợ HTTP/2 trong 2020 \[W3Techs\]. Hầu hết các trình duyệt---bao gồm Google Chrome, Internet Explorer, Safari, Opera và Firefox---cũng hỗ trợ HTTP/2.

Mục tiêu chính của HTTP/2 là giảm độ trễ nhận thấy bằng cách cho phép ghép kênh yêu cầu và phản hồi qua một kết nối TCP duy nhất, cung cấp mức độ ưu tiên yêu cầu và đẩy máy chủ, đồng thời cung cấp khả năng nén hiệu quả các trường tiêu đề HTTP. HTTP/2 không thay đổi HTTP phương thức, mã trạng thái, URL hoặc trường tiêu đề. Thay vào đó, HTTP/2 thay đổi cách định dạng và vận chuyển dữ liệu giữa máy khách và máy chủ.

Để thúc đẩy nhu cầu về HTTP/2, hãy nhớ rằng HTTP/1.1 sử dụng các kết nối TCP liên tục, cho phép gửi một trang Web từ máy chủ đến máy khách qua một kết nối TCP duy nhất. Bằng cách chỉ có một kết nối TCP trên mỗi trang Web, số lượng ổ cắm trên máy chủ sẽ giảm xuống và mỗi trang Web được vận chuyển sẽ nhận được một phần băng thông mạng hợp lý (như được thảo luận bên dưới). Nhưng các nhà phát triển trình duyệt Web nhanh chóng phát hiện ra rằng việc gửi tất cả các đối tượng trong một trang Web qua một kết nối TCP có vấn đề chặn Head of Line (HOL). Để hiểu cách chặn HOL, hãy xem xét một trang Web bao gồm một trang cơ sở HTML, một video clip lớn ở gần đầu trang Web và nhiều đối tượng nhỏ bên dưới video. Hơn nữa, giả sử có một liên kết tắc nghẽn tốc độ thấp đến trung bình (ví dụ: liên kết không dây tốc độ thấp) trên đường dẫn giữa máy chủ và máy khách. Sử dụng một kết nối TCP duy nhất, video clip sẽ mất nhiều thời gian để đi qua liên kết thắt cổ chai, trong khi các đối tượng nhỏ bị trì hoãn khi chúng chờ phía sau video clip; tức là đoạn video ở đầu dòng sẽ chặn các vật thể nhỏ phía sau nó. Trình duyệt HTTP/1.1 thường giải quyết vấn đề này bằng cách mở nhiều kết nối TCP song song, nhờ đó các đối tượng trong cùng một trang web được gửi song song tới trình duyệt. Bằng cách này, các đối tượng nhỏ có thể đến và hiển thị trong trình duyệt nhanh hơn nhiều, do đó giảm độ trễ mà người dùng nhận thấy.

TCP kiểm soát tắc nghẽn, được thảo luận chi tiết trong Chương 3, cũng cung cấp cho trình duyệt một động cơ ngoài ý muốn để sử dụng nhiều kết nối TCP song song thay vì một kết nối liên tục duy nhất. Nói một cách đại khái, kiểm soát tắc nghẽn TCP nhằm mục đích cung cấp cho mỗi kết nối TCP chia sẻ liên kết thắt cổ chai một phần bằng nhau về băng thông khả dụng của liên kết đó; vì vậy nếu có n TCP kết nối hoạt động trên một liên kết thắt cổ chai thì mỗi kết nối sẽ nhận được khoảng 1/n băng thông. Bằng cách mở nhiều kết nối TCP song song để vận chuyển một trang Web, trình duyệt có thể "lừa đảo" và lấy phần lớn băng thông liên kết. Nhiều trình duyệt HTTP/1.1 mở tối đa sáu kết nối TCP song song không chỉ để tránh việc chặn HOL mà còn để có thêm băng thông.

Một trong những mục tiêu chính của HTTP/2 là loại bỏ (hoặc ít nhất là giảm số lượng) kết nối TCP song song để truyền tải một trang Web. Điều này không chỉ làm giảm số lượng ổ cắm cần mở và bảo trì trên máy chủ mà còn cho phép kiểm soát tắc nghẽn TCP hoạt động như dự kiến. Nhưng chỉ với một kết nối TCP để truyền một trang Web, HTTP/2 yêu cầu các cơ chế được thiết kế cẩn thận để tránh chặn HOL.

HTTP/2 Đóng khung

Giải pháp HTTP/2 để chặn HOL là chia từng tin nhắn thành các khung nhỏ và xen kẽ các tin nhắn yêu cầu và phản hồi trên cùng một kết nối TCP. Để hiểu điều này, hãy xem lại ví dụ về một trang Web bao gồm một video clip lớn và 8 đối tượng nhỏ hơn. Như vậy máy chủ sẽ nhận được 9 yêu cầu đồng thời từ bất kỳ trình duyệt nào muốn xem trang Web này. Đối với mỗi yêu cầu này, máy chủ cần gửi 9 thông báo phản hồi HTTP cạnh tranh tới trình duyệt. Giả sử tất cả các khung đều thuộc

có độ dài cố định, video clip bao gồm 1000 khung hình và mỗi đối tượng nhỏ hơn bao gồm hai khung hình. Với tính năng xen kẽ khung hình, sau khi gửi một khung hình từ video clip, các khung hình đầu tiên của từng đối tượng nhỏ sẽ được gửi đi. Sau đó, sau khi gửi khung hình thứ hai của video clip, khung hình cuối cùng của từng đối tượng nhỏ sẽ được gửi. Do đó, tất cả các đối tượng nhỏ hơn sẽ được gửi sau khi gửi tổng cộng 18 khung hình. Nếu không sử dụng tính năng xen kẽ, các đối tượng nhỏ hơn sẽ chỉ được gửi sau khi gửi 1016 khung hình. Do đó, cơ chế tạo khung HTTP/2 có thể giảm đáng kể độ trễ do người dùng nhận thấy.

Khả năng chia nhỏ tin nhắn HTTP thành các khung độc lập, xen kẽ chúng và sau đó tập hợp lại chúng ở đầu bên kia là cải tiến quan trọng nhất của HTTP/2. Việc đóng khung được thực hiện bởi lớp con đóng khung của giao thức HTTP/2. Khi máy chủ muốn gửi phản hồi HTTP, phản hồi sẽ được xử lý bởi lớp con đóng khung, tại đó nó được chia thành các khung. Trường tiêu đề của phản hồi trở thành một khung và phần nội dung của tin nhắn được chia thành một khung để có thêm khung. Sau đó, các khung của phản hồi được xen kẽ bởi lớp con tạo khung trong máy chủ với các khung của các phản hồi khác và được gửi qua kết nối TCP liên tục duy nhất. Khi các khung đến máy khách, trước tiên chúng được tập hợp lại thành các thông báo phản hồi ban đầu ở lớp con tạo khung và sau đó được trình duyệt xử lý như bình thường. Tương tự, các yêu cầu HTTP của khách hàng được chia thành các khung và xen kẽ.

Ngoài việc chia nhỏ từng thông báo HTTP thành các khung độc lập, lớp con tạo khung cũng mã hóa nhị phân các khung. Các giao thức nhị phân phân tích cú pháp hiệu quả hơn, dẫn đến các khung nhỏ hơn một chút và ít xảy ra lỗi hơn.

Ưu tiên tin nhắn phản hồi và đẩy máy chủ

Ưu tiên tin nhắn cho phép nhà phát triển tùy chỉnh mức độ ưu tiên tương đối của các yêu cầu để tối ưu hóa hiệu suất ứng dụng tốt hơn. Như chúng ta vừa tìm hiểu, lớp con định khung sắp xếp các thông điệp thành các luồng dữ liệu song song được gửi đến cùng một người yêu cầu. Khi một máy khách gửi các yêu cầu đồng thời đến máy chủ, nó có thể ưu tiên các phản hồi mà nó yêu cầu bằng cách chỉ định trọng số từ 1 đến 256 cho mỗi tin nhắn. Số cao hơn cho thấy mức độ ưu tiên cao hơn. Bằng cách sử dụng các trọng số này, máy chủ có thể gửi các khung đầu tiên cho các phản hồi có mức độ ưu tiên cao nhất. Ngoài ra, máy khách còn nêu rõ sự phụ thuộc của từng tin nhắn vào các tin nhắn khác bằng cách chỉ định ID của tin nhắn mà nó phụ thuộc vào.

Một tính năng khác của HTTP/2 là khả năng máy chủ gửi nhiều phản hồi cho một yêu cầu của khách hàng. Nghĩa là, ngoài việc phản hồi yêu cầu ban đầu, máy chủ có thể đẩy các đối tượng bổ sung đến máy khách mà không cần máy khách phải yêu cầu từng đối tượng. Điều này có thể thực hiện được vì trang cơ sở HTML chỉ ra các đối tượng cần thiết để hiển thị đầy đủ trang Web. Vì vậy, thay vì chờ đợi các yêu cầu HTTP đối với các đối tượng này, máy chủ có thể phân tích trang HTML, xác định các đối tượng cần thiết và gửi chúng đến máy khách trước khi nhận được yêu cầu rõ ràng đối với các đối tượng này. Đẩy máy chủ giúp loại bỏ độ trễ tăng thêm do phải chờ yêu cầu.

HTTP/3

QUIC, được thảo luận trong Chương 3, là một giao thức "vận chuyển" mới được triển khai trong lớp ứng dụng qua giao thức cơ bản UDP. QUIC có một số tính năng mà HTTP mong muốn, chẳng hạn như ghép kênh tin nhắn (xen kẽ), kiểm soát luồng trên mỗi luồng và thiết lập kết nối có độ trễ thấp. HTTP/3 vẫn là giao thức HTTP mới được thiết kế để hoạt động trên QUIC. Tính đến năm 2020, HTTP/3 được mô tả trong bản nháp trên Internet và vẫn chưa được chuẩn hóa hoàn toàn. Nhiều tính năng HTTP/2 (chẳng hạn như xen kẽ tin nhắn) được QUIC gộp lại, cho phép thiết kế hợp lý, đơn giản hơn cho HTTP/3.

**2.3 Thư điện tử trên Internet**

Thư điện tử đã xuất hiện từ khi Internet bắt đầu xuất hiện. Nó là ứng dụng phổ biến nhất khi Internet còn sơ khai \[Segaller 1998\] và đã trở nên phức tạp và mạnh mẽ hơn qua nhiều năm. Nó vẫn là một trong những ứng dụng quan trọng và được sử dụng nhiều nhất trên Internet.

Giống như thư bưu chính thông thường, e-mail là một phương tiện liên lạc không đồng bộ---mọi người gửi và đọc tin nhắn khi thấy thuận tiện cho họ mà không cần phải phối hợp với lịch trình của người khác. Ngược lại với thư bưu chính, thư điện tử nhanh, dễ phân phối và không tốn kém. Email hiện đại có nhiều tính năng mạnh mẽ, bao gồm thư có tệp đính kèm, siêu liên kết, văn bản có định dạng HTML và ảnh nhúng.

Trong phần này, chúng ta xem xét các giao thức lớp ứng dụng là trung tâm của e-mail Internet. Nhưng trước khi chúng ta đi vào thảo luận sâu hơn về các giao thức này, chúng ta hãy có cái nhìn tổng thể về hệ thống thư Internet và các thành phần chính của nó.

Hình 2.14 trình bày một cái nhìn tổng quát về hệ thống thư Internet. Từ sơ đồ này, chúng ta thấy rằng nó có ba thành phần chính: tác nhân người dùng, máy chủ thư và Giao thức truyền thư đơn giản (SMTP). Bây giờ chúng ta mô tả từng thành phần này trong bối cảnh người gửi, Alice, gửi một e-mail đến người nhận, Bob. Tác nhân người dùng cho phép người dùng đọc, trả lời, chuyển tiếp, lưu và soạn tin nhắn. Ví dụ về tác nhân người dùng cho e-mail bao gồm Microsoft Outlook, Apple Mail, Gmail dựa trên web, Ứng dụng Gmail chạy trên điện thoại thông minh, v.v. Khi Alice soạn xong thư, tác nhân người dùng của cô sẽ gửi thư đến máy chủ thư của cô, nơi thư được đặt trong hàng đợi thư gửi đi của máy chủ thư. Khi Bob muốn đọc thư, tác nhân người dùng của anh ấy sẽ lấy thư từ hộp thư trong máy chủ thư của anh ấy.

Máy chủ thư tạo thành cốt lõi của cơ sở hạ tầng e-mail. Mỗi người nhận, chẳng hạn như Bob, có một hộp thư đặt tại một trong các máy chủ thư. Hộp thư của Bob quản lý và lưu giữ các tin nhắn đã được gửi cho anh ấy. Một thư thông thường bắt đầu hành trình của nó trong tác nhân người dùng của người gửi, sau đó di chuyển đến máy chủ thư của người gửi và sau đó

đi đến máy chủ thư của người nhận, nơi nó được gửi vào hộp thư của người nhận. Khi Bob muốn truy cập các thư trong hộp thư của anh ấy, máy chủ thư chứa hộp thư của anh ấy sẽ xác thực Bob (bằng tên người dùng và mật khẩu của anh ấy). Máy chủ thư của Alice cũng phải xử lý các lỗi trong máy chủ thư của Bob. Nếu máy chủ của Alice không thể gửi thư đến máy chủ của Bob thì máy chủ của Alice sẽ giữ thư trong hàng đợi thư và cố gắng chuyển thư sau. Việc thử lại thường được thực hiện sau mỗi 30 phút; nếu không thành công sau vài ngày, máy chủ sẽ xóa tin nhắn và thông báo cho người gửi (Alice) bằng một tin nhắn e-mail.

SMTP là giao thức lớp ứng dụng chính cho thư điện tử trên Internet. Nó sử dụng dịch vụ truyền dữ liệu đáng tin cậy của TCP để chuyển thư từ máy chủ thư của người gửi đến máy chủ thư của người nhận. Giống như hầu hết các giao thức lớp ứng dụng, SMTP có hai bên: phía máy khách, thực thi trên máy chủ thư của người gửi và phía máy chủ, thực thi trên máy chủ thư của người nhận. Cả hai phía máy khách và máy chủ của

Hàng đợi tin nhắn đi

Chìa khóa:

Hộp thư người dùng

SMTP

Tác nhân người dùng

Tác nhân người dùng

Tác nhân người dùng

Tác nhân người dùng

Tác nhân người dùng

Tác nhân người dùng

Máy chủ thư

Máy chủ thư

Máy chủ thư

SMTP

SMTP

*Hình 2.14 ♦ Cái nhìn tổng quát về hệ thống e-mail Internet*

SMTP chạy trên mọi máy chủ thư. Khi máy chủ thư gửi thư đến các máy chủ thư khác, nó hoạt động như một ứng dụng khách SMTP. Khi máy chủ thư nhận thư từ các máy chủ thư khác, nó hoạt động như một máy chủ SMTP.

**2.3.1 SMTP**

SMTP, được định nghĩa trong RFC 5321, là trung tâm của thư điện tử trên Internet. Như đã đề cập ở trên, SMTP chuyển thư từ máy chủ thư của người gửi đến máy chủ thư của người nhận. SMTP cũ hơn nhiều so với HTTP. (SMTP RFC ban đầu có từ năm 1982 và SMTP đã xuất hiện trước đó rất lâu.) Mặc dù SMTP có nhiều phẩm chất tuyệt vời, được chứng minh bằng sự phổ biến của nó trên Internet, tuy nhiên, nó vẫn là một công nghệ kế thừa có những đặc điểm cổ xưa nhất định. Ví dụ: nó giới hạn phần nội dung (không chỉ phần tiêu đề) của tất cả các thư ở dạng ASCII 7 bit đơn giản. Hạn chế này có ý nghĩa vào đầu những năm 1980 khi khả năng truyền tải còn khan hiếm và không có ai gửi e-mail các tệp đính kèm lớn hoặc các tệp hình ảnh, âm thanh hoặc video lớn. Nhưng ngày nay, trong kỷ nguyên đa phương tiện, hạn chế ASCII 7 bit có phần khó khăn---nó yêu cầu dữ liệu đa phương tiện nhị phân phải được mã hóa thành ASCII trước khi được gửi qua SMTP; và nó yêu cầu thông báo ASCII tương ứng phải được giải mã trở lại thành nhị phân sau khi truyền SMTP. Hãy nhớ lại Phần 2.2 rằng HTTP không yêu cầu dữ liệu đa phương tiện phải được mã hóa ASCII trước khi truyền.

Để minh họa hoạt động cơ bản của SMTP, hãy xem qua một tình huống phổ biến. Giả sử Alice muốn gửi cho Bob một tin nhắn ASCII đơn giản.

1\. Alice gọi tác nhân người dùng của mình để lấy e-mail, cung cấp địa chỉ e-mail của Bob (đối với

ví dụ: bob@someschool.edu), soạn tin nhắn và hướng dẫn tác nhân người dùng gửi tin nhắn. 2. Tác nhân người dùng của Alice gửi thư đến máy chủ thư của cô ấy, nơi nó được đặt trong một

hàng đợi tin nhắn. 3. Phía máy khách của SMTP, đang chạy trên máy chủ thư của Alice, sẽ thấy thông báo trong

hàng đợi tin nhắn. Nó mở kết nối TCP tới máy chủ SMTP, chạy trên máy chủ thư của Bob. 4. Sau vài lần bắt tay SMTP ban đầu, ứng dụng khách SMTP sẽ gửi tin nhắn của Alice

vào kết nối TCP. 5. Tại máy chủ thư của Bob, phía máy chủ của SMTP nhận được tin nhắn. Thư của Bob

sau đó máy chủ sẽ đặt tin nhắn vào hộp thư của Bob. 6. Bob gọi tác nhân người dùng của mình để đọc tin nhắn khi thuận tiện.

Kịch bản được tóm tắt trong Hình 2.15.

Điều quan trọng cần lưu ý là SMTP thường không sử dụng máy chủ thư trung gian để gửi thư, ngay cả khi hai máy chủ thư được đặt ở hai đầu đối diện nhau trên thế giới. Nếu máy chủ của Alice ở Hồng Kông và máy chủ của Bob ở St. Louis thì kết nối TCP là kết nối trực tiếp giữa máy chủ Hồng Kông và St. Louis. TRONG

Cụ thể, nếu máy chủ thư của Bob ngừng hoạt động, thư vẫn còn trong máy chủ thư của Alice và chờ lần thử mới---thư không được đặt trong một số máy chủ thư trung gian.

Bây giờ chúng ta hãy xem xét kỹ hơn cách SMTP chuyển thư từ máy chủ thư gửi sang máy chủ thư nhận. Chúng ta sẽ thấy rằng giao thức SMTP có nhiều điểm tương đồng với các giao thức được sử dụng để tương tác trực tiếp giữa con người với nhau. Đầu tiên, ứng dụng khách SMTP (chạy trên máy chủ máy chủ gửi thư) có TCP thiết lập kết nối tới cổng 25 tại máy chủ SMTP (chạy trên máy chủ máy chủ thư nhận). Nếu máy chủ ngừng hoạt động, máy khách sẽ thử lại sau. Sau khi kết nối này được thiết lập, máy chủ và máy khách sẽ thực hiện một số bắt tay ở lớp ứng dụng---giống như con người thường giới thiệu bản thân trước khi truyền thông tin từ nơi này sang nơi khác, SMTP máy khách và máy chủ tự giới thiệu trước khi truyền thông tin. Trong giai đoạn bắt tay SMTP này, ứng dụng khách SMTP cho biết địa chỉ e-mail của người gửi (người tạo thư) và địa chỉ e-mail của người nhận. Khi máy khách và máy chủ SMTP đã tự giới thiệu với nhau, máy khách sẽ gửi tin nhắn. SMTP có thể tin tưởng vào dịch vụ truyền dữ liệu đáng tin cậy của TCP để đưa tin nhắn đến máy chủ mà không gặp lỗi. Sau đó, máy khách lặp lại quy trình này trên cùng kết nối TCP nếu nó có các tin nhắn khác cần gửi đến máy chủ; nếu không, nó sẽ hướng dẫn TCP đóng kết nối.

Tiếp theo, chúng ta hãy xem bản chép lại ví dụ về các tin nhắn được trao đổi giữa máy khách SMTP (C) và máy chủ SMTP (S). Tên máy chủ của máy khách là crepes.fr và tên máy chủ của máy chủ là hamburger.edu. Các dòng văn bản ASCII có phần mở đầu bằng C: chính xác là những dòng mà máy khách gửi vào ổ cắm TCP của nó và các dòng văn bản ASCII có phần mở đầu bằng S: chính xác là những dòng mà máy chủ gửi vào ổ cắm TCP của nó. Bản ghi sau đây bắt đầu ngay khi kết nối TCP được thiết lập.

S:  220 hamburger.edu C:  HELO crepes.fr

SMTP

Máy chủ thư của Alice

Máy chủ thư của Bob

của Alice

đại lý

Đại lý của Bob

Hàng đợi tin nhắn

Chìa khóa:

Hộp thư người dùng

*Hình 2.15 ♦ Alice gửi tin nhắn cho Bob*

S:  250 Xin chào crepes.fr, rất vui được gặp bạn C:  MAIL FROM: \<alice@crepes.fr\> S:  250 alice@crepes.fr \... Người gửi ok C:  RCPT TO: \<bob@hamburger.edu\> S:  250 bob@hamburger.edu \... Người nhận ok C:  DỮ LIỆU S:  354 Nhập thư, kết thúc bằng ". trên một dòng C:  Bạn có thích sốt cà chua không? C:  Còn dưa chua thì sao? C: . S:  250 Tin nhắn được chấp nhận gửi C:  QUIT S:  221 hamburger.edu đóng kết nối

Trong ví dụ trên, khách hàng gửi một tin nhắn ("Bạn có thích sốt cà chua không? Còn dưa chua thì sao?") từ máy chủ thư crepes.fr đến máy chủ thư hamburger.edu. Là một phần của cuộc đối thoại, khách hàng đã đưa ra năm lệnh: HELO (viết tắt của HELLO), MAIL FROM, RCPT TO, DATA và QUIT. Những lệnh này là tự giải thích. Máy khách cũng gửi một dòng bao gồm một dấu chấm duy nhất, cho biết phần cuối của tin nhắn đến máy chủ. (Trong thuật ngữ ASCII, mỗi tin nhắn kết thúc bằng CRLF.CRLF, trong đó CR và LF lần lượt là viết tắt của dấu xuống dòng và nguồn cấp dòng.) Máy chủ đưa ra câu trả lời cho từng lệnh, với mỗi câu trả lời có mã trả lời và một số giải thích bằng tiếng Anh (tùy chọn). Ở đây chúng tôi đề cập rằng SMTP sử dụng kết nối liên tục: Nếu máy chủ thư gửi có một số thư cần gửi đến cùng một máy chủ thư nhận, nó có thể gửi tất cả thư qua cùng một kết nối TCP. Đối với mỗi tin nhắn, khách hàng bắt đầu quá trình bằng một THƯ mới TỪ: crepes.fr, chỉ định phần cuối của tin nhắn có khoảng thời gian cách ly và chỉ đưa ra QUIT sau khi tất cả tin nhắn đã được gửi.

Chúng tôi khuyên bạn nên sử dụng Telnet để thực hiện đối thoại trực tiếp với máy chủ SMTP. Để làm điều này, hãy phát hành

máy chủ telnetTên 25

trong đó serverName là tên của máy chủ thư cục bộ. Khi thực hiện việc này, bạn chỉ cần thiết lập kết nối TCP giữa máy chủ cục bộ của bạn và máy chủ thư. Sau khi gõ dòng này, bạn sẽ nhận được ngay phản hồi 220 từ máy chủ. Sau đó đưa ra các lệnh SMTP HELO, MAIL FROM, RCPT TO, DATA, CRLF.CRLF và QUIT vào những thời điểm thích hợp. Bạn cũng nên thực hiện Bài tập lập trình 3 ở cuối chương này. Trong nhiệm vụ đó, bạn sẽ xây dựng một tác nhân người dùng đơn giản triển khai phía máy khách của SMTP. Nó sẽ cho phép bạn gửi tin nhắn e-mail đến người nhận tùy ý thông qua máy chủ thư cục bộ.

**2.3.2 Định dạng thư**

Khi Alice viết một bức thư gửi qua đường bưu điện thông thường cho Bob, cô ấy có thể bao gồm tất cả các loại thông tin tiêu đề ngoại vi ở đầu thư, chẳng hạn như địa chỉ của Bob, địa chỉ gửi lại của chính cô ấy và ngày tháng. Tương tự, khi một tin nhắn e-mail được gửi từ người này sang người khác, một tiêu đề chứa thông tin ngoại vi sẽ đứng trước nội dung của tin nhắn. Thông tin ngoại vi này được chứa trong một loạt các dòng tiêu đề, được xác định trong RFC 5322. Các dòng tiêu đề và nội dung của thông báo được phân tách bằng một dòng trống (nghĩa là bằng CRLF). RFC 5322 chỉ định định dạng chính xác cho các dòng tiêu đề thư cũng như cách diễn giải ngữ nghĩa của chúng. Như với HTTP, mỗi dòng tiêu đề chứa văn bản có thể đọc được, bao gồm một từ khóa, theo sau là dấu hai chấm, theo sau là một giá trị. Một số từ khóa là bắt buộc và những từ khóa khác là tùy chọn. Mỗi tiêu đề phải có dòng tiêu đề From: và dòng tiêu đề To:; tiêu đề có thể bao gồm dòng tiêu đề Chủ đề: cũng như các dòng tiêu đề tùy chọn khác. Điều quan trọng cần lưu ý là các dòng tiêu đề này khác với các lệnh SMTP mà chúng ta đã nghiên cứu trong Phần 2.3.1 (mặc dù chúng chứa một số từ phổ biến như "from" và "to"). Các lệnh trong phần đó là một phần của giao thức bắt tay SMTP; các dòng tiêu đề được xem xét trong phần này là một phần của thư.

Tiêu đề thư điển hình trông như thế này:

Từ: alice@crepes.fr Đến: bob@hamburger.edu Chủ đề: Tìm kiếm ý nghĩa cuộc sống.

Sau tiêu đề thư là một dòng trống; sau đó là nội dung thư (trong ASCII) theo sau. Bạn nên sử dụng Telnet để gửi thư đến máy chủ thư có chứa một số dòng tiêu đề, trong đó có dòng tiêu đề Chủ đề:. Để thực hiện việc này, hãy phát hành telnet serverName 25, như đã thảo luận trong Phần 2.3.1.

**2.3.3 Giao thức truy cập thư**

Sau khi SMTP gửi thư từ máy chủ thư của Alice đến máy chủ thư của Bob, thư sẽ được đặt vào hộp thư của Bob. Cho rằng Bob (người nhận) thực thi tác nhân người dùng của mình trên máy chủ cục bộ của anh ấy (ví dụ: điện thoại thông minh hoặc PC), việc cân nhắc việc đặt một máy chủ thư trên máy chủ cục bộ của anh ấy là điều tự nhiên. Với cách tiếp cận này, máy chủ thư của Alice sẽ đối thoại trực tiếp với PC của Bob. Tuy nhiên, có một vấn đề với cách tiếp cận này. Hãy nhớ lại rằng máy chủ thư quản lý các hộp thư và chạy phía máy khách và máy chủ của SMTP. Nếu máy chủ thư của Bob đặt trên máy chủ cục bộ của anh ấy thì máy chủ của Bob sẽ phải luôn bật và kết nối với Internet để nhận thư mới, có thể đến bất kỳ lúc nào. Điều này là không thực tế đối với nhiều người dùng Internet. Thay vào đó, một người dùng thông thường chạy một tác nhân người dùng trên máy chủ cục bộ nhưng truy cập vào hộp thư của nó được lưu trữ trên máy chủ thư dùng chung luôn bật. Máy chủ thư này được chia sẻ với những người dùng khác.

Bây giờ hãy xem xét đường đi của một thông điệp email khi nó được gửi từ Alice đến Bob. Chúng tôi vừa biết được rằng tại một thời điểm nào đó trên đường dẫn, thư e-mail cần được gửi vào máy chủ thư của Bob. Điều này có thể được thực hiện đơn giản bằng cách yêu cầu tác nhân người dùng của Alice gửi thư trực tiếp đến máy chủ thư của Bob. Tuy nhiên, thông thường tác nhân người dùng của người gửi không đối thoại trực tiếp với máy chủ thư của người nhận. Thay vào đó, như trong Hình 2.16, tác nhân người dùng của Alice sử dụng SMTP hoặc HTTP để gửi thư e-mail đến máy chủ thư của cô ấy, sau đó máy chủ thư của Alice sử dụng SMTP (với tư cách là ứng dụng khách SMTP) để chuyển tiếp thư e-mail đến máy chủ thư của Bob. Tại sao phải thực hiện quy trình hai bước? Chủ yếu là do không chuyển tiếp qua máy chủ thư của Alice, tác nhân người dùng của Alice không có bất kỳ quyền truy đòi nào vào máy chủ thư đích không thể truy cập được. Bằng cách yêu cầu Alice gửi e-mail đầu tiên vào máy chủ thư của cô ấy, máy chủ thư của Alice có thể liên tục cố gắng gửi thư đến máy chủ thư của Bob, cứ 30 phút một lần, cho đến khi máy chủ thư của Bob hoạt động. (Và nếu máy chủ thư của Alice bị hỏng thì cô ấy có quyền khiếu nại với quản trị viên hệ thống của mình!)

Nhưng vẫn còn thiếu một mảnh ghép cho câu đố! Làm thế nào để một người nhận như Bob, đang chạy một tác nhân người dùng trên máy chủ cục bộ của anh ấy, nhận được các tin nhắn đang nằm trong máy chủ thư của anh ấy? Lưu ý rằng tác nhân người dùng của Bob không thể sử dụng SMTP để nhận tin nhắn vì việc lấy tin nhắn là thao tác kéo, trong khi SMTP là giao thức đẩy.

Ngày nay, có hai cách phổ biến để Bob lấy e-mail của mình từ máy chủ thư. Nếu Bob đang sử dụng e-mail trên web hoặc ứng dụng điện thoại thông minh (chẳng hạn như Gmail), thì tác nhân người dùng sẽ sử dụng HTTP để truy xuất e-mail của Bob. Trường hợp này yêu cầu máy chủ thư của Bob phải có giao diện HTTP cũng như giao diện SMTP (để liên lạc với máy chủ thư của Alice). Phương pháp thay thế, thường được sử dụng với các ứng dụng thư như Microsoft Outlook, là sử dụng Giao thức truy cập thư Internet (IMAP) được xác định trong RFC 3501. Cả hai phương pháp HTTP và IMAP đều cho phép Bob quản lý các thư mục, được duy trì trong máy chủ thư của Bob. Bob có thể di chuyển thư vào các thư mục do anh ấy tạo, xóa thư, đánh dấu thư là quan trọng, v.v.

**2.4 DNS---Dịch vụ thư mục của Internet**

Con người chúng ta có thể được nhận dạng theo nhiều cách. Ví dụ, chúng ta có thể được nhận dạng bằng những cái tên ghi trên giấy khai sinh của chúng ta. Chúng ta có thể được nhận dạng bằng số an sinh xã hội của mình. Chúng tôi có thể được xác định bằng số giấy phép lái xe của chúng tôi.

SMTP

Máy chủ thư của Alice

Máy chủ thư của Bob

của Alice

đại lý

Đại lý của Bob

SMTP

hoặc HTTP

HTTP

hoặc IMAP

*Hình 2.16 ♦ Giao thức e-mail và các thực thể giao tiếp của chúng*

Mặc dù mỗi từ có thể được sử dụng để nhận dạng con người, nhưng trong một bối cảnh nhất định, một mã định danh có thể phù hợp hơn mã định danh khác. Ví dụ: máy tính tại IRS (cơ quan thu thuế khét tiếng ở Hoa Kỳ) thích sử dụng số an sinh xã hội có độ dài cố định hơn là tên trên giấy khai sinh. Mặt khác, những người bình thường thích tên giấy khai sinh dễ nhớ hơn là số an sinh xã hội. (Thật vậy, bạn có thể tưởng tượng mình nói: \"Xin chào. Tên tôi là 132-67-9875. Xin hãy gặp chồng tôi, 178-87-1146.\")

Giống như con người có thể được nhận dạng theo nhiều cách, các máy chủ Internet cũng vậy. Một mã định danh cho máy chủ là tên máy chủ của nó. Tên máy chủ---chẳng hạn như www.facebook.com, www.google.com, gaia.cs.umass.edu---có tính dễ nhớ và do đó được con người đánh giá cao. Tuy nhiên, tên máy chủ cung cấp rất ít thông tin, nếu có, về vị trí trên Internet của máy chủ. (Tên máy chủ như www.eurecom.fr, kết thúc bằng mã quốc gia .fr, cho chúng ta biết rằng máy chủ có thể ở Pháp, nhưng không nói gì thêm.) Hơn nữa, vì tên máy chủ có thể bao gồm các ký tự chữ và số có độ dài thay đổi nên bộ định tuyến sẽ khó xử lý chúng. Vì những lý do này, các máy chủ cũng được xác định bằng cái gọi là địa chỉ IP.

Chúng ta thảo luận chi tiết về các địa chỉ IP trong Chương 4, nhưng bây giờ sẽ rất hữu ích nếu nói một vài lời ngắn gọn về chúng. Địa chỉ IP bao gồm bốn byte và có cấu trúc phân cấp cứng nhắc. Địa chỉ IP trông giống như 121.7.106.83, trong đó mỗi dấu chấm phân tách một trong các byte được biểu thị bằng ký hiệu thập phân từ 0 đến 255. Địa chỉ IP có tính phân cấp vì khi chúng tôi quét địa chỉ từ trái sang phải, chúng tôi thu được ngày càng nhiều thông tin cụ thể hơn về vị trí của máy chủ trên Internet (nghĩa là trong mạng nào, trong mạng của các mạng). Tương tự, khi chúng tôi quét một địa chỉ bưu điện từ dưới lên trên, chúng tôi sẽ thu được ngày càng nhiều thông tin cụ thể hơn về vị trí của người nhận.

**2.4.1 Dịch vụ được cung cấp bởi DNS**

Chúng ta vừa thấy rằng có hai cách để xác định máy chủ---bằng tên máy chủ và bằng địa chỉ IP. Mọi người thích mã định danh tên máy chủ dễ nhớ hơn, trong khi các bộ định tuyến thích các địa chỉ IP có độ dài cố định, có cấu trúc phân cấp. Để điều hòa các tùy chọn này, chúng tôi cần một dịch vụ thư mục dịch tên máy chủ sang địa chỉ IP. Đây là nhiệm vụ chính của hệ thống tên miền Internet (DNS). DNS là (1) cơ sở dữ liệu phân tán được triển khai theo hệ thống phân cấp của máy chủ DNS và (2) giao thức lớp ứng dụng cho phép máy chủ truy vấn cơ sở dữ liệu phân tán. Các máy chủ DNS thường là các máy UNIX chạy phần mềm Miền tên Internet Berkeley (BIND) \[BIND 2020\]. Giao thức DNS chạy trên UDP và sử dụng cổng 53.

DNS thường được sử dụng bởi các giao thức lớp ứng dụng khác, bao gồm HTTP và SMTP, để dịch tên máy chủ do người dùng cung cấp sang địa chỉ IP. Ví dụ: hãy xem xét điều gì sẽ xảy ra khi một trình duyệt (tức là ứng dụng khách HTTP), chạy trên máy chủ của một số người dùng, yêu cầu URL www.someschool.edu/index.html. Để máy chủ của người dùng có thể gửi tin nhắn yêu cầu HTTP tới Web

máy chủ www.someschool.edu, máy chủ của người dùng trước tiên phải có địa chỉ IP của www.someschool.edu. Điều này được thực hiện như sau.

1\. Máy người dùng tương tự chạy phía máy khách của ứng dụng DNS. 2. Trình duyệt trích xuất tên máy chủ, www.someschool.edu, từ URL

và chuyển tên máy chủ cho phía máy khách của ứng dụng DNS. 3. Máy khách DNS gửi truy vấn chứa tên máy chủ đến máy chủ DNS. 4. Cuối cùng, ứng dụng khách DNS nhận được phản hồi, bao gồm địa chỉ IP cho

tên máy chủ. 5. Sau khi trình duyệt nhận được địa chỉ IP từ DNS, nó có thể bắt đầu một cuộc trò chuyện TCP

nối với quy trình máy chủ HTTP đặt tại cổng 80 tại địa chỉ IP đó.

Từ ví dụ này, chúng tôi thấy rằng DNS tăng thêm độ trễ---đôi khi đáng kể---cho các ứng dụng Internet sử dụng nó. May mắn thay, như chúng ta thảo luận bên dưới, địa chỉ IP mong muốn thường được lưu vào bộ nhớ đệm trong máy chủ DNS "gần đó", giúp giảm lưu lượng mạng DNS cũng như độ trễ DNS trung bình.

DNS cung cấp một số dịch vụ quan trọng khác ngoài việc dịch tên máy chủ sang địa chỉ IP:

• Host bí danh. Một máy chủ có tên máy chủ phức tạp có thể có một hoặc nhiều tên bí danh. Ví dụ: tên máy chủ như Relay1.west-coast .enterprise.com có ​​thể có hai bí danh như Enterprise.com và www.enterprise.com. Trong trường hợp này, tên máy chủ tiếp sức1 .west-coast.enterprise.com được cho là tên máy chủ chuẩn. Tên máy chủ bí danh, khi xuất hiện, thường dễ nhớ hơn tên máy chủ chuẩn. DNS có thể được ứng dụng gọi ra để lấy tên máy chủ chuẩn cho tên máy chủ bí danh được cung cấp cũng như địa chỉ IP của máy chủ. • Bí danh máy chủ thư. Vì những lý do hiển nhiên, điều rất mong muốn là địa chỉ e-mail có thể dễ nhớ. Ví dụ: nếu Bob có tài khoản với Yahoo Mail thì địa chỉ e-mail của Bob có thể đơn giản là bob@yahoo.com. Tuy nhiên, tên máy chủ của máy chủ thư Yahoo phức tạp hơn và ít dễ nhớ hơn nhiều so với tên máy chủ đơn giản là yahoo.com (ví dụ: tên máy chủ chuẩn có thể giống như Relay1.west-coast.yahoo.com). DNS có thể được ứng dụng thư gọi ra để lấy tên máy chủ chuẩn cho tên máy chủ bí danh được cung cấp cũng như địa chỉ IP của máy chủ. Trên thực tế, bản ghi MX (xem bên dưới) cho phép máy chủ thư và máy chủ Web của công ty có tên máy chủ (bí danh) giống hệt nhau; ví dụ: máy chủ Web và máy chủ thư của công ty đều có thể được gọi là Enterprise.com. • Phân phối tải. DNS cũng được sử dụng để thực hiện phân phối tải giữa các máy chủ được sao chép, chẳng hạn như các máy chủ Web được sao chép. Các trang web bận rộn, chẳng hạn như cnn.com, được sao chép trên nhiều máy chủ, với mỗi máy chủ chạy trên một hệ thống đầu cuối khác nhau và mỗi máy chủ có một địa chỉ IP khác nhau. Đối với các máy chủ Web được sao chép, một bộ IP

do đó, địa chỉ được liên kết với một tên máy chủ bí danh. Cơ sở dữ liệu DNS chứa tập hợp các địa chỉ IP này. Khi khách hàng thực hiện truy vấn DNS cho một tên được ánh xạ tới một tập hợp địa chỉ, máy chủ sẽ phản hồi với toàn bộ tập hợp địa chỉ IP nhưng sẽ xoay vòng thứ tự của các địa chỉ trong mỗi phản hồi. Bởi vì khách hàng thường gửi thông báo yêu cầu HTTP của mình tới địa chỉ IP được liệt kê đầu tiên trong tập hợp, nên vòng quay DNS sẽ phân phối lưu lượng giữa các máy chủ được sao chép. DNS xoay vòng cũng được sử dụng cho e-mail để nhiều máy chủ thư có thể có cùng tên bí danh. Ngoài ra, các công ty phân phối nội dung như Akamai đã sử dụng DNS theo những cách phức tạp hơn \[Dilley 2002\] để phân phối nội dung Web (xem Phần 2.6.3).

DNS được chỉ định trong RFC 1034 và RFC 1035, đồng thời được cập nhật trong một số RFC bổ sung. Đây là một hệ thống phức tạp và chúng tôi chỉ đề cập đến các khía cạnh chính trong hoạt động của nó ở đây. Độc giả quan tâm có thể tham khảo các RFC này và cuốn sách của Albitz và Liu \[Albitz 1993\]; xem thêm bài viết hồi cứu \[Mockapetris 1988\], trong đó cung cấp một mô tả hay về cái gì và tại sao của DNS, và \[Mockapetris 2005\].

**2.4.2 Tổng quan về cách hoạt động của DNS**

Bây giờ chúng tôi trình bày tổng quan cấp cao về cách DNS hoạt động. Cuộc thảo luận của chúng ta sẽ tập trung vào dịch vụ dịch địa chỉ từ tên máy chủ sangIP.

Giả sử rằng một số ứng dụng (chẳng hạn như trình duyệt Web hoặc ứng dụng thư khách) đang chạy trên máy chủ của người dùng cần dịch tên máy chủ sang địa chỉ IP. Ứng dụng sẽ gọi phía máy khách của DNS, chỉ định tên máy chủ cần dịch. (Trên nhiều máy dựa trên UNIX, gethostbyname() là lệnh gọi hàm mà ứng dụng gọi để thực hiện dịch.) DNS trong máy chủ của người dùng sau đó

DNS: CÁC CHỨC NĂNG MẠNG QUAN TRỌNG QUA MÔ HÌNH MÁY CHỦ KHÁCH HÀNG

Giống như HTTP, FTP và SMTP, giao thức DNS là giao thức lớp ứng dụng vì nó (1) chạy giữa các hệ thống cuối giao tiếp bằng cách sử dụng mô hình máy khách-máy chủ và (2) dựa vào giao thức truyền tải hai đầu cơ bản để truyền thông báo DNS giữa các hệ thống cuối giao tiếp. Tuy nhiên, theo một nghĩa khác, vai trò của DNS hoàn toàn khác với các ứng dụng Web, truyền tệp và e-mail. Không giống như các ứng dụng này, DNS không phải là ứng dụng mà người dùng tương tác trực tiếp. Thay vào đó, DNS cung cấp chức năng Internet cốt lõi---cụ thể là dịch tên máy chủ sang địa chỉ IP cơ bản của chúng, cho các ứng dụng người dùng và phần mềm khác trên Internet. Chúng tôi đã lưu ý trong Phần 1.2 rằng phần lớn sự phức tạp trong kiến ​​trúc Internet nằm ở "biên" của mạng. DNS, thực hiện quy trình dịch tên sang địa chỉ quan trọng bằng cách sử dụng máy khách và máy chủ nằm ở rìa mạng, là một ví dụ khác về triết lý thiết kế đó.

NGUYÊN TẮC TRONG THỰC HÀNH

tiếp quản, gửi tin nhắn truy vấn vào mạng. Tất cả các tin nhắn truy vấn và trả lời DNS được gửi trong các gói dữ liệu UDP tới cổng 53. Sau một khoảng thời gian chờ, từ mili giây đến vài giây, DNS trong máy chủ của người dùng sẽ nhận được tin nhắn trả lời DNS cung cấp ánh xạ mong muốn. Ánh xạ này sau đó được chuyển đến ứng dụng gọi. Do đó, từ góc độ ứng dụng gọi trong máy chủ của người dùng, DNS là một hộp đen cung cấp dịch vụ dịch thuật đơn giản, dễ hiểu. Nhưng trên thực tế, hộp đen triển khai dịch vụ này rất phức tạp, bao gồm một số lượng lớn máy chủ DNS được phân bổ trên toàn cầu cũng như giao thức lớp ứng dụng chỉ định cách máy chủ DNS và máy chủ truy vấn giao tiếp với nhau.

Một thiết kế đơn giản cho DNS sẽ có một máy chủ DNS chứa tất cả ánh xạ. Trong thiết kế tập trung này, máy khách chỉ cần chuyển tất cả truy vấn đến một máy chủ DNS duy nhất và máy chủ DNS sẽ phản hồi trực tiếp cho máy khách đang truy vấn. Mặc dù tính đơn giản của thiết kế này rất hấp dẫn nhưng nó không phù hợp với Internet ngày nay với số lượng máy chủ khổng lồ (và ngày càng tăng). Các vấn đề với thiết kế tập trung bao gồm:

• Một điểm thất bại duy nhất. Nếu máy chủ DNS gặp sự cố thì toàn bộ Internet cũng vậy! • Lưu lượng giao thông. Một máy chủ DNS sẽ phải xử lý tất cả các truy vấn DNS (đối với tất cả các yêu cầu HTTP và thư e-mail được tạo từ hàng trăm triệu máy chủ). • Cơ sở dữ liệu tập trung từ xa. Một máy chủ DNS không thể "gần gũi" với tất cả các máy khách truy vấn. Nếu chúng tôi đặt máy chủ DNS duy nhất ở Thành phố New York thì tất cả các truy vấn từ Úc phải truyền sang bên kia địa cầu, có thể qua các liên kết chậm và tắc nghẽn. Điều này có thể dẫn đến sự chậm trễ đáng kể. • BẢO TRÌ. Máy chủ DNS duy nhất sẽ phải lưu giữ hồ sơ của tất cả các máy chủ Internet. Cơ sở dữ liệu tập trung này không chỉ rất lớn mà còn phải được cập nhật thường xuyên để chứa mọi máy chủ mới.

Tóm lại, cơ sở dữ liệu tập trung trong một máy chủ DNS đơn giản là không thể mở rộng quy mô. Do đó, DNS được phân phối theo thiết kế. Trên thực tế, DNS là một ví dụ tuyệt vời về cách triển khai cơ sở dữ liệu phân tán trên Internet.

Cơ sở dữ liệu phân tán, phân cấp

Để giải quyết vấn đề về quy mô, DNS sử dụng một số lượng lớn máy chủ, được tổ chức theo kiểu phân cấp và phân bổ trên toàn thế giới. Không có máy chủ DNS nào có tất cả ánh xạ cho tất cả các máy chủ trên Internet. Thay vào đó, ánh xạ được phân phối trên các máy chủ DNS. Theo phép tính gần đúng đầu tiên, có ba loại máy chủ DNS---máy chủ DNS gốc, máy chủ miền cấp cao nhất (TLD) DNS và máy chủ DNS có thẩm quyền---được tổ chức theo cấp bậc như trong Hình 2.17. Để hiểu cách ba loại máy chủ này tương tác với nhau, giả sử máy khách DNS muốn xác định địa chỉ IP cho tên máy chủ www.amazon.com. Theo ước tính đầu tiên, các sự kiện sau sẽ diễn ra. Đầu tiên khách hàng liên hệ với một trong

máy chủ gốc trả về địa chỉ IP cho máy chủ TLD cho tên miền cấp cao nhất com. Sau đó, khách hàng sẽ liên hệ với một trong các máy chủ TLD này, máy chủ này sẽ trả về địa chỉ IP của máy chủ có thẩm quyền cho amazon.com. Cuối cùng, khách hàng liên hệ với một trong các máy chủ có thẩm quyền của amazon.com, máy chủ này sẽ trả về địa chỉ IP cho tên máy chủ www.amazon.com. Chúng tôi sẽ sớm kiểm tra quá trình tra cứu DNS này một cách chi tiết hơn. Nhưng trước tiên chúng ta hãy xem xét kỹ hơn ba loại máy chủ DNS này:

• Máy chủ DNS gốc. Có hơn 1000 phiên bản máy chủ gốc nằm rải rác trên khắp thế giới, như trong Hình 2.18. Các máy chủ gốc này là bản sao của 13 máy chủ gốc khác nhau, được quản lý bởi 12 tổ chức khác nhau và được điều phối thông qua Cơ quan cấp số hiệu Internet \[IANA 2020\]. Bạn có thể tìm thấy danh sách đầy đủ các máy chủ tên gốc, cùng với các tổ chức quản lý chúng và địa chỉ IP của chúng tại \[Root Servers 2020\]. Máy chủ tên gốc cung cấp địa chỉ IP của máy chủ TLD. • Máy chủ tên miền cấp cao nhất (TLD). Đối với mỗi miền cấp cao nhất---các miền cấp cao nhất như com, org, net, edu và gov và tất cả các miền cấp cao nhất của quốc gia như uk, fr, ca và jp---có máy chủ TLD (hoặc cụm máy chủ). Công ty Dịch vụ đăng ký toàn cầu Verisign duy trì các máy chủ TLD cho miền cấp cao nhất com và công ty Edu Cause duy trì các máy chủ TLD cho miền cấp cao nhất edu. Cơ sở hạ tầng mạng hỗ trợ TLD có thể lớn và phức tạp; xem \[Osterweil 2012\] để biết thông tin tổng quan về mạng Verisign. Xem \[danh sách TLD 2020\] để biết danh sách tất cả các tên miền cấp cao nhất. Máy chủ TLD cung cấp địa chỉ IP cho máy chủ DNS có thẩm quyền. • Máy chủ DNS có thẩm quyền. Mọi tổ chức có máy chủ có thể truy cập công khai (chẳng hạn như máy chủ Web và máy chủ thư) trên Internet phải cung cấp bản ghi DNS có thể truy cập công khai để ánh xạ tên của các máy chủ đó tới địa chỉ IP. Máy chủ DNS có thẩm quyền của tổ chức chứa các bản ghi DNS này. Tổ chức có thể chọn triển khai máy chủ DNS có thẩm quyền của riêng mình để lưu giữ những hồ sơ này; Ngoài ra, tổ chức có thể trả tiền để lưu trữ những hồ sơ này trong một

edu DNS máy chủ org DNS máy chủ và máy chủ DNS

nyu.edu DNS máy chủ facebook.com

DNS máy chủ

amazon.com

DNS máy chủ

máy chủ pbs.org DNS

máy chủ umass.edu DNS

Máy chủ DNS gốc

*Hình 2.17 ♦ Một phần phân cấp của máy chủ DNS*

máy chủ DNS có thẩm quyền của một số nhà cung cấp dịch vụ. Hầu hết các trường đại học và các công ty lớn đều triển khai và duy trì máy chủ DNS có thẩm quyền chính và phụ (dự phòng) của riêng họ.

Các máy chủ gốc, TLD và DNS có thẩm quyền đều thuộc hệ thống phân cấp của máy chủ DNS, như trong Hình 2.17. Có một loại máy chủ DNS quan trọng khác được gọi là máy chủ DNS cục bộ. Máy chủ DNS cục bộ không hoàn toàn thuộc về hệ thống phân cấp của máy chủ nhưng vẫn là trung tâm của kiến ​​trúc DNS. Mỗi ISP---chẳng hạn như ISP dân cư hoặc ISP tổ chức---có máy chủ DNS cục bộ (còn được gọi là máy chủ tên mặc định). Khi máy chủ kết nối với ISP, ISP sẽ cung cấp cho máy chủ địa chỉ IP của một hoặc nhiều máy chủ DNS cục bộ của nó (thường thông qua DHCP, được thảo luận trong Chương 4). Bạn có thể dễ dàng xác định địa chỉ IP của máy chủ DNS cục bộ của mình bằng cách truy cập cửa sổ trạng thái mạng trong Windows hoặc UNIX. Máy chủ DNS cục bộ của máy chủ thường "gần" với máy chủ. Đối với ISP của tổ chức, máy chủ DNS cục bộ có thể nằm trên cùng mạng LAN với máy chủ; đối với một ISP dân cư, nó thường cách biệt với máy chủ không quá một vài bộ định tuyến. Khi máy chủ thực hiện truy vấn DNS, truy vấn sẽ được gửi đến máy chủ DNS cục bộ, hoạt động như một proxy, chuyển tiếp truy vấn vào hệ thống phân cấp máy chủ DNS, như chúng ta sẽ thảo luận chi tiết hơn bên dưới.

Chúng ta hãy xem một ví dụ đơn giản. Giả sử máy chủ cse.nyu.edu muốn có địa chỉ IP của gaia.cs.umass.edu. Ngoài ra, giả sử rằng máy chủ DNS cục bộ của NYU dành cho cse.nyu.edu được gọi là dns.nyu.edu và máy chủ DNS có thẩm quyền dành cho gaia.cs.umass.edu được gọi là dns.umass.edu. Như thể hiện trong

0 Máy chủ 1--10 Máy chủ 11--20 Máy chủ 21+ Máy chủ

Chìa khóa:

*Hình 2.18 ♦ DNS máy chủ gốc năm 2020*

Hình 2.19, máy chủ cse.nyu.edu trước tiên gửi tin nhắn truy vấn DNS tới máy chủ DNS cục bộ của nó, dns.nyu.edu. Thông báo truy vấn chứa tên máy chủ cần dịch, cụ thể là gaia.cs.umass.edu. Máy chủ DNS cục bộ chuyển tiếp thông báo truy vấn đến máy chủ DNS gốc. Máy chủ DNS gốc ghi lại hậu tố edu và trả về máy chủ DNS cục bộ một danh sách các địa chỉ IP cho các máy chủ TLD chịu trách nhiệm về edu. Sau đó, máy chủ DNS cục bộ sẽ gửi lại thông báo truy vấn đến một trong các máy chủ TLD này. Máy chủ TLD ghi lại hậu tố umass.edu và phản hồi bằng địa chỉ IP của máy chủ DNS có thẩm quyền của Đại học Massachusetts, cụ thể là dns.umass.edu. Cuối cùng, máy chủ DNS cục bộ gửi lại thông báo truy vấn trực tiếp đến dns.umass.edu, thông báo này phản hồi bằng địa chỉ IP của gaia .cs.umass.edu. Lưu ý rằng trong ví dụ này, để có được ánh xạ cho một tên máy chủ, tám tin nhắn DNS đã được gửi: bốn tin nhắn truy vấn và bốn tin nhắn trả lời! Chúng ta sẽ sớm thấy bộ nhớ đệm DNS giảm lưu lượng truy vấn này như thế nào.

Ví dụ trước của chúng tôi giả định rằng máy chủ TLD biết máy chủ DNS có thẩm quyền đối với tên máy chủ. Nói chung, điều này không phải lúc nào cũng đúng. Thay vào đó, máy chủ TLD

Máy chủ yêu cầu

cse.nyu.edu

Máy chủ DNS cục bộ TLD DNS máy chủ dns.nyu.edu

Máy chủ gốc DNS

Máy chủ DNS có thẩm quyền

dns.umass.edu

gaia.cs.umass.edu

*Hình 2.19 ♦ Tương tác của các máy chủ DNS khác nhau*

có thể chỉ biết máy chủ DNS trung gian, do đó máy chủ này biết máy chủ DNS có thẩm quyền đối với tên máy chủ. Ví dụ: giả sử lại rằng Đại học Massachusetts có máy chủ DNS cho trường đại học, được gọi là dns.umass.edu. Ngoài ra, giả sử rằng mỗi khoa tại Đại học Massachusetts có máy chủ DNS riêng và mỗi máy chủ DNS của phòng ban đều có thẩm quyền đối với tất cả các máy chủ trong khoa. Trong trường hợp này, khi máy chủ DNS trung gian, dns.umass.edu, nhận được truy vấn về máy chủ có tên máy chủ kết thúc bằng cs.umass.edu, nó sẽ trả về dns.nyu.edu địa chỉ IP của dns.cs.umass.edu, địa chỉ này có thẩm quyền đối với tất cả tên máy chủ kết thúc bằng cs.umass.edu. Sau đó, máy chủ DNS cục bộ dns.nyu .edu sẽ gửi truy vấn đến máy chủ DNS có thẩm quyền, máy chủ này trả về ánh xạ mong muốn tới máy chủ DNS cục bộ, từ đó trả về ánh xạ tới máy chủ yêu cầu. Trong trường hợp này, tổng cộng 10 tin nhắn DNS đã được gửi!

Ví dụ trong Hình 2.19 sử dụng cả truy vấn đệ quy và truy vấn lặp. Truy vấn được gửi từ cse.nyu.edu đến dns.nyu.edu là một truy vấn đệ quy, vì truy vấn yêu cầu dns.nyu.edu thay mặt nó lấy ánh xạ. Tuy nhiên, ba truy vấn tiếp theo được lặp lại vì tất cả các câu trả lời đều được trả về trực tiếp cho dns.nyu.edu. Về lý thuyết, mọi truy vấn DNS đều có thể lặp lại hoặc đệ quy. Ví dụ: Hình 2.20 hiển thị chuỗi truy vấn DNS trong đó tất cả các truy vấn đều là đệ quy. Trong thực tế, các truy vấn thường tuân theo mẫu trong Hình 2.19: Truy vấn từ máy chủ yêu cầu đến máy chủ DNS cục bộ là truy vấn đệ quy và các truy vấn còn lại là truy vấn lặp.

DNS Bộ nhớ đệm

Cuộc thảo luận của chúng ta cho đến nay vẫn chưa bỏ qua bộ nhớ đệm DNS, một tính năng cực kỳ quan trọng của hệ thống DNS. Trên thực tế, DNS khai thác rộng rãi DNS bộ nhớ đệm để cải thiện hiệu suất trễ và giảm số lượng tin nhắn DNS lan truyền khắp Internet. Ý tưởng đằng sau bộ nhớ đệm DNS rất đơn giản. Trong chuỗi truy vấn, khi máy chủ DNS nhận được câu trả lời DNS (ví dụ: chứa ánh xạ từ tên máy chủ đến địa chỉ IP), nó có thể lưu ánh xạ vào bộ nhớ cục bộ của nó. Ví dụ, trong Hình 2.19, mỗi lần máy chủ DNS cục bộ dns.nyu.edu nhận được phản hồi từ máy chủ DNS nào đó, nó có thể lưu vào bộ nhớ đệm bất kỳ thông tin nào có trong phản hồi đó. Nếu một cặp tên máy chủ/IP được lưu vào bộ nhớ đệm trong máy chủ DNS và một truy vấn khác đến máy chủ DNS cho cùng một tên máy chủ, thì máy chủ DNS có thể cung cấp địa chỉ IP mong muốn, ngay cả khi địa chỉ đó không có thẩm quyền đối với tên máy chủ đó. Bởi vì các máy chủ và ánh xạ giữa tên máy chủ và địa chỉ IP không phải là vĩnh viễn nên máy chủ DNS sẽ loại bỏ thông tin được lưu trong bộ nhớ đệm sau một khoảng thời gian (thường được đặt thành hai ngày).

Ví dụ: giả sử rằng máy chủ apricot.nyu.edu truy vấn dns.nyu.edu để tìm địa chỉ IP cho tên máy chủ cnn.com. Hơn nữa, giả sử rằng vài giờ sau, một máy chủ NYU khác, chẳng hạn như kiwi.nyu.edu, cũng truy vấn dns.nyu.edu với cùng tên máy chủ. Nhờ bộ nhớ đệm, máy chủ DNS cục bộ sẽ có thể trả về ngay địa chỉ IP của cnn.com cho máy chủ yêu cầu thứ hai này mà không cần phải truy vấn bất kỳ máy chủ DNS nào khác. Máy chủ DNS cục bộ có thể

Máy chủ yêu cầu

cse.nyu.edu

Máy chủ DNS cục bộ TLD DNS máy chủ dns.nyu.edu

Máy chủ gốc DNS

Máy chủ DNS có thẩm quyền

dns.umass.edu

gaia.cs.umass.edu

*Hình 2.20 ♦ Truy vấn đệ quy trong DNS*

cũng lưu vào bộ nhớ đệm địa chỉ IP của máy chủ TLD, do đó cho phép máy chủ DNS cục bộ bỏ qua máy chủ DNS gốc trong chuỗi truy vấn. Trên thực tế, do bộ nhớ đệm, tất cả các máy chủ gốc đều bị bỏ qua ngoại trừ một phần rất nhỏ DNS truy vấn.

**2.4.3 DNS Bản ghi và tin nhắn**

Các máy chủ DNS cùng triển khai các bản ghi tài nguyên lưu trữ (RR) cơ sở dữ liệu phân tán DNS, bao gồm các RR cung cấp ánh xạ địa chỉ tên máy chủ đếnIP. Mỗi tin nhắn trả lời DNS mang một hoặc nhiều bản ghi tài nguyên. Trong tiểu mục này và tiểu mục tiếp theo, chúng tôi cung cấp tổng quan ngắn gọn về DNS bản ghi và thông báo tài nguyên; có thể tìm thêm thông tin chi tiết trong \[Albitz 1993\] hoặc trong DNS RFC \[RFC 1034; RFC 1035\].

Bản ghi tài nguyên là một bộ gồm bốn bộ chứa các trường sau:

(Tên, Giá trị, Loại, TTL)

TTL là thời gian tồn tại của bản ghi tài nguyên; nó xác định khi nào nên xóa tài nguyên khỏi bộ đệm. Trong các bản ghi mẫu dưới đây, chúng tôi bỏ qua trường TTL. Ý nghĩa của Tên và Giá trị phụ thuộc vào Loại:

• Nếu Loại=A thì Tên là tên máy chủ và Giá trị là địa chỉ IP cho tên máy chủ. Do đó, bản ghi Loại A cung cấp ánh xạ địa chỉ tên máy chủ đếnIP tiêu chuẩn. Ví dụ: (relay1.bar.foo.com, 145.37.93.126, A) là bản ghi Loại A. • Nếu Loại=NS thì Tên là một miền (chẳng hạn như foo.com) và Giá trị là tên máy chủ của máy chủ DNS có thẩm quyền biết cách lấy địa chỉ IP cho các máy chủ trong miền. Bản ghi này được sử dụng để định tuyến các truy vấn DNS sâu hơn trong chuỗi truy vấn. Ví dụ: (foo.com, dns.foo.com, NS) là bản ghi Loại NS. • Nếu Loại=CNAME thì Giá trị là tên máy chủ chuẩn cho tên máy chủ bí danh Tên. Bản ghi này có thể cung cấp cho máy chủ truy vấn tên chuẩn cho tên máy chủ. Ví dụ: (foo.com, Relay1.bar.foo.com, CNAME) là bản ghi CNAME. • Nếu Loại=MX thì Giá trị là tên chuẩn của máy chủ thư có tên máy chủ bí danh. Ví dụ: (foo.com, mail.bar.foo.com, MX) là bản ghi MX. Bản ghi MX cho phép tên máy chủ của máy chủ thư có bí danh đơn giản. Lưu ý rằng bằng cách sử dụng bản ghi MX, một công ty có thể có cùng tên bí danh cho máy chủ thư của mình và cho một trong các máy chủ khác của công ty đó (chẳng hạn như máy chủ Web của công ty đó). Để có được tên chuẩn cho máy chủ thư, ứng dụng khách DNS sẽ truy vấn bản ghi MX; để lấy tên chuẩn cho máy chủ khác, ứng dụng khách DNS sẽ truy vấn bản ghi CNAME.

Nếu máy chủ DNS có thẩm quyền đối với một tên máy chủ cụ thể thì máy chủ DNS sẽ chứa bản ghi Loại A cho tên máy chủ đó. (Ngay cả khi máy chủ DNS không có thẩm quyền, nó vẫn có thể chứa bản ghi Loại A trong bộ đệm của nó.) Nếu máy chủ không có thẩm quyền đối với tên máy chủ thì máy chủ sẽ chứa bản ghi Loại NS cho miền bao gồm tên máy chủ; nó cũng sẽ chứa bản ghi Loại A cung cấp địa chỉ IP của máy chủ DNS trong trường Giá trị của bản ghi NS. Ví dụ: giả sử máy chủ edu TLD không có thẩm quyền đối với máy chủ gaia.cs.umass.edu. Sau đó, máy chủ này sẽ chứa bản ghi cho miền bao gồm máy chủ gaia.cs.umass .edu, chẳng hạn như (umass.edu, dns.umass.edu, NS). Máy chủ edu TLD cũng sẽ chứa bản ghi Loại A, bản ghi này ánh xạ máy chủ DNS dns.umass.edu tới địa chỉ IP, chẳng hạn như (dns.umass.edu, 128.119.40.111, A).

DNS Tin nhắn

Trước đó trong phần này, chúng ta đã đề cập đến DNS tin nhắn truy vấn và trả lời. Đây là hai loại tin nhắn DNS duy nhất. Hơn nữa, cả tin nhắn truy vấn và trả lời đều có cùng định dạng, như trong Hình 2.21. Ngữ nghĩa của các trường khác nhau trong tin nhắn DNS như sau:

• 12 byte đầu tiên là phần tiêu đề, có một số trường. Trường đầu tiên là số 16 bit xác định truy vấn. Mã định danh này được sao chép vào tin nhắn trả lời cho một truy vấn, cho phép khách hàng đối chiếu các câu trả lời nhận được với các truy vấn đã gửi. Có một số cờ trong trường cờ. Cờ truy vấn/trả lời 1 bit cho biết tin nhắn là truy vấn (0) hay trả lời (1). Cờ có thẩm quyền 1 bit được đặt trong tin nhắn trả lời khi máy chủ DNS là máy chủ có thẩm quyền cho tên được truy vấn. Cờ mong muốn đệ quy 1 bit được đặt khi máy khách (máy chủ hoặc máy chủ DNS) mong muốn máy chủ DNS thực hiện đệ quy khi nó không có bản ghi. Trường có sẵn đệ quy 1 bit được đặt trong thư trả lời nếu máy chủ DNS hỗ trợ đệ quy. Trong tiêu đề cũng có bốn trường. Các trường này cho biết số lần xuất hiện của bốn loại phần dữ liệu theo sau tiêu đề. • Phần câu hỏi chứa thông tin về truy vấn đang được thực hiện. Phần này bao gồm (1) trường tên chứa tên đang được truy vấn và (2) trường loại cho biết loại câu hỏi đang được hỏi về tên---ví dụ: địa chỉ máy chủ được liên kết với tên (Loại A) hoặc máy chủ thư cho tên (Loại MX).

Nhận dạng

Số lượng câu hỏi

Số lượng RR thẩm quyền

Tên, loại trường cho truy vấn

12 byte

RR để phản hồi truy vấn

Hồ sơ cho các máy chủ có thẩm quyền

Thông tin "hữu ích" bổ sung có thể được sử dụng

Cờ

Số câu trả lời RR

Số lượng RR bổ sung

Quyền hạn (số lượng bản ghi tài nguyên có thể thay đổi)

Thông tin bổ sung (số lượng bản ghi tài nguyên có thể thay đổi)

Câu trả lời (số lượng bản ghi tài nguyên có thể thay đổi)

Câu hỏi (số lượng câu hỏi có thể thay đổi)

*Hình 2.21 ♦ Định dạng tin nhắn DNS*

• Trong thư trả lời từ máy chủ DNS, phần câu trả lời chứa các bản ghi tài nguyên cho tên được truy vấn ban đầu. Hãy nhớ lại rằng trong mỗi bản ghi tài nguyên đều có Loại (ví dụ: A, NS, CNAME và MX), Giá trị và TTL. Một câu trả lời có thể trả về nhiều RR trong câu trả lời, vì tên máy chủ có thể có nhiều địa chỉ IP (ví dụ: đối với các máy chủ Web được sao chép, như đã thảo luận trước đó trong phần này). • Phần thẩm quyền chứa các bản ghi của các máy chủ có thẩm quyền khác. • Phần bổ sung chứa các hồ sơ hữu ích khác. Ví dụ: trường câu trả lời trong câu trả lời cho truy vấn MX chứa bản ghi tài nguyên cung cấp tên máy chủ chuẩn của máy chủ thư. Phần bổ sung chứa bản ghi Loại A cung cấp địa chỉ IP cho tên máy chủ chuẩn của máy chủ thư.

Bạn muốn gửi tin nhắn truy vấn DNS trực tiếp từ máy chủ mà bạn đang làm việc tới máy chủ DNS nào đó như thế nào? Điều này có thể dễ dàng được thực hiện bằng chương trình nslookup, chương trình này có sẵn trên hầu hết các nền tảng Windows và UNIX. Ví dụ: từ máy chủ Windows, hãy mở Dấu nhắc Lệnh và gọi chương trình nslookup bằng cách chỉ cần gõ "nslookup". Sau khi gọi nslookup, bạn có thể gửi truy vấn DNS tới bất kỳ máy chủ DNS nào (root, TLD hoặc có thẩm quyền). Sau khi nhận được tin nhắn trả lời từ máy chủ DNS, nslookup sẽ hiển thị các bản ghi có trong tin nhắn trả lời (ở định dạng mà con người có thể đọc được). Để thay thế cho việc chạy nslookup từ máy chủ của bạn, bạn có thể truy cập một trong nhiều trang Web cho phép bạn sử dụng nslookup từ xa. (Chỉ cần gõ "nslookup" vào công cụ tìm kiếm và bạn sẽ được đưa đến một trong những trang này.) Phòng thí nghiệm DNS Wireshark ở cuối chương này sẽ cho phép bạn khám phá DNS chi tiết hơn nhiều.

Chèn bản ghi vào cơ sở dữ liệu DNS

Cuộc thảo luận ở trên tập trung vào cách truy xuất các bản ghi từ cơ sở dữ liệu DNS. Bạn có thể thắc mắc làm thế nào các bản ghi được đưa vào cơ sở dữ liệu ngay từ đầu. Hãy xem cách thực hiện điều này trong bối cảnh của một ví dụ cụ thể. Giả sử bạn vừa thành lập một công ty khởi nghiệp mới thú vị có tên Network Utopia. Điều đầu tiên bạn chắc chắn muốn làm là đăng ký tên miền networkutopia.com tại một nhà đăng ký. Nhà đăng ký là một thực thể thương mại xác minh tính duy nhất của tên miền, nhập tên miền vào cơ sở dữ liệu DNS (như được thảo luận bên dưới) và thu một khoản phí nhỏ từ bạn cho các dịch vụ của họ. Trước năm 1999, một nhà đăng ký duy nhất, Network Solutions, đã độc quyền đăng ký tên miền cho các miền com, net và org. Nhưng hiện nay có nhiều nhà đăng ký cạnh tranh để giành khách hàng và Tập đoàn Internet cấp số và tên miền (ICANN) công nhận các nhà đăng ký khác nhau. Danh sách đầy đủ các nhà đăng ký được công nhận có tại http://www.internic.net.

Khi bạn đăng ký tên miền networkutopia.com với một số nhà đăng ký, bạn cũng cần cung cấp cho nhà đăng ký tên và IP địa chỉ của các máy chủ DNS có thẩm quyền chính và phụ của bạn. Giả sử tên và địa chỉ IP là dns1.networkutopia.com, dns2.networkutopia.com, 212.2.212.1 và 212.212.212.2. Đối với mỗi trong số hai điều này có thẩm quyền DNS

DNS LỖI LỖI

Chúng ta đã thấy rằng DNS là một thành phần quan trọng của cơ sở hạ tầng Internet, với nhiều dịch vụ quan trọng---bao gồm Web và e-mail---đơn giản là không thể hoạt động nếu không có nó. Do đó, chúng tôi tự nhiên hỏi, làm thế nào DNS có thể bị tấn công? Có phải DNS là một con vịt đang ngồi chờ bị loại khỏi dịch vụ trong khi gỡ bỏ hầu hết các ứng dụng Internet không?

Kiểu tấn công đầu tiên bạn nghĩ đến là tấn công làm tràn băng thông DDoS (xem Phần 1.6) nhằm vào các máy chủ DNS. Ví dụ: kẻ tấn công có thể cố gắng gửi đến mỗi máy chủ gốc DNS một lượng lớn gói tin, nhiều đến mức phần lớn các truy vấn DNS hợp pháp không bao giờ nhận được câu trả lời. Một cuộc tấn công DDoS quy mô lớn như vậy chống lại các máy chủ gốc DNS thực sự đã diễn ra vào ngày 21 tháng 10 năm 2002. Trong cuộc tấn công này, những kẻ tấn công đã tận dụng một mạng botnet để gửi vô số tin nhắn ping ICMP đến từng địa chỉ trong số 13 địa chỉ DNS gốc IP. (ICMP thông báo được thảo luận trong Phần 5.6. Hiện tại, chỉ cần biết rằng gói ICMP là loại đặc biệt của IP datagram.) May mắn thay, cuộc tấn công quy mô lớn này gây ra thiệt hại tối thiểu, ít hoặc không ảnh hưởng đến trải nghiệm Internet của người dùng. Những kẻ tấn công đã thành công trong việc hướng một lượng lớn gói tin đến các máy chủ gốc. Nhưng nhiều máy chủ gốc DNS được bảo vệ bởi các bộ lọc gói, được định cấu hình để luôn chặn tất cả các tin nhắn ping ICMP hướng đến máy chủ gốc. Do đó, các máy chủ được bảo vệ này không bị ảnh hưởng và hoạt động như bình thường. Hơn nữa, hầu hết các máy chủ DNS cục bộ đều lưu vào bộ nhớ đệm địa chỉ IP của các máy chủ tên miền cấp cao nhất, cho phép quá trình truy vấn thường bỏ qua các máy chủ gốc DNS.

Một cuộc tấn công DDoS có khả năng hiệu quả hơn chống lại DNS là gửi vô số truy vấn DNS tới các máy chủ tên miền cấp cao nhất, chẳng hạn như tới các máy chủ tên miền cấp cao nhất xử lý tên miền .com. Khó lọc hơn các truy vấn DNS hướng đến máy chủ DNS; và các máy chủ tên miền cấp cao nhất không dễ bị vượt qua như các máy chủ gốc. Một cuộc tấn công như vậy đã diễn ra nhằm vào nhà cung cấp dịch vụ miền cấp cao nhất Dyn vào ngày 21 tháng 10 năm 2016. Cuộc tấn công DDoS này được thực hiện thông qua một số lượng lớn DNS yêu cầu tra cứu từ một mạng botnet bao gồm khoảng một trăm nghìn thiết bị IoT như máy in, IP máy ảnh, cổng dân cư và thiết bị giám sát trẻ em đã bị nhiễm phần mềm độc hại Mirai. Trong gần cả ngày, Amazon, Twitter, Netflix, Github và Spotify đều bị làm phiền.

DNS có thể bị tấn công theo những cách khác. Trong cuộc tấn công trung gian, kẻ tấn công chặn các truy vấn từ máy chủ và trả về các câu trả lời không có thật. Trong cuộc tấn công đầu độc DNS, kẻ tấn công gửi các câu trả lời giả đến máy chủ DNS, lừa máy chủ chấp nhận các bản ghi giả vào bộ nhớ đệm của nó. Ví dụ, một trong những cuộc tấn công này có thể được sử dụng để chuyển hướng người dùng Web không nghi ngờ đến trang Web của kẻ tấn công. DNS Tiện ích mở rộng bảo mật (DNSSEC \[Gieben 2004; RFC 4033\] đã được thiết kế và triển khai để bảo vệ chống lại những hành vi khai thác như vậy. DNSSEC, phiên bản bảo mật của DNS, giải quyết nhiều cuộc tấn công có thể xảy ra này và đang trở nên phổ biến trên Internet.

TẬP TRUNG VÀO AN NINH

máy chủ, nhà đăng ký sau đó sẽ đảm bảo rằng bản ghi Loại NS và Loại A được nhập vào máy chủ TLD com. Cụ thể, đối với máy chủ có thẩm quyền chính cho networkutopia.com, nhà đăng ký sẽ chèn hai bản ghi tài nguyên sau vào hệ thống DNS:

(networkutopia.com, dns1.networkutopia.com, NS) (dns1.networkutopia.com, 212.212.212.1, A)

Bạn cũng sẽ phải đảm bảo rằng bản ghi tài nguyên Loại A cho máy chủ Web www.networkutopia.com và bản ghi tài nguyên Loại MX cho máy chủ thư mail.networkutopia.com của bạn được nhập vào các máy chủ DNS có thẩm quyền của bạn. (Cho đến gần đây, nội dung của mỗi máy chủ DNS đã được định cấu hình tĩnh, chẳng hạn như từ tệp cấu hình do người quản lý hệ thống tạo. Gần đây hơn, tùy chọn CẬP NHẬT đã được thêm vào giao thức DNS để cho phép dữ liệu được thêm hoặc xóa động khỏi cơ sở dữ liệu thông qua các thông báo DNS. \[RFC 2136\] và \[RFC 3007\] chỉ định DNS cập nhật động.) Một lần nữa Sau khi hoàn thành các bước này, mọi người sẽ có thể truy cập trang Web của bạn và gửi e-mail cho nhân viên tại công ty bạn. Hãy kết thúc cuộc thảo luận của chúng ta về DNS bằng cách xác minh rằng tuyên bố này là đúng. Việc xác minh này cũng giúp củng cố những gì chúng tôi đã tìm hiểu về DNS. Giả sử Alice ở Úc muốn xem trang Web www.networkutopia.com. Như đã thảo luận trước đó, máy chủ của cô ấy trước tiên sẽ gửi truy vấn DNS đến máy chủ DNS cục bộ của cô ấy. Sau đó, máy chủ DNS cục bộ sẽ liên hệ với máy chủ TLD com. (Máy chủ DNS cục bộ cũng sẽ phải liên hệ với máy chủ DNS gốc nếu địa chỉ của máy chủ TLD com không được lưu vào bộ nhớ đệm.) Máy chủ TLD này chứa các bản ghi tài nguyên Loại NS và Loại A được liệt kê ở trên, vì nhà đăng ký đã chèn các bản ghi tài nguyên này vào tất cả các máy chủ TLD com. Máy chủ com TLD gửi phản hồi đến máy chủ DNS cục bộ của Alice, với phản hồi chứa hai bản ghi tài nguyên. Sau đó, máy chủ DNS cục bộ sẽ gửi truy vấn DNS tới 212.212.212.1, yêu cầu bản ghi Loại A tương ứng với www.networkutopia.com. Bản ghi này cung cấp địa chỉ IP của máy chủ Web mong muốn, chẳng hạn như 212.212.71.4, mà máy chủ DNS cục bộ sẽ gửi lại cho máy chủ của Alice. Trình duyệt của Alice hiện có thể bắt đầu kết nối TCP tới máy chủ 212.212.71.4 và gửi yêu cầu HTTP qua kết nối. Ối! Có rất nhiều điều đang diễn ra hơn những gì bạn thấy khi lướt Web!

**2.5 Peer-to-Peer Phân phối tệp**

Cho đến nay, các ứng dụng được mô tả trong chương này---bao gồm Web, e-mail và DNS---tất cả đều sử dụng kiến ​​trúc máy khách-máy chủ với sự phụ thuộc đáng kể vào các máy chủ cơ sở hạ tầng luôn hoạt động. Hãy nhớ lại Phần 2.1.1 rằng với kiến ​​trúc P2P, có sự phụ thuộc tối thiểu (hoặc không) vào các máy chủ cơ sở hạ tầng luôn hoạt động. Thay vào đó, các cặp máy chủ được kết nối không liên tục, được gọi là ngang hàng, giao tiếp trực tiếp với nhau. Các thiết bị ngang hàng không thuộc sở hữu của nhà cung cấp dịch vụ mà thay vào đó là PC, máy tính xách tay và điện thoại thông minh do người dùng điều khiển.

Trong phần này, chúng ta xem xét một ứng dụng P2P rất tự nhiên, cụ thể là phân phối một tệp lớn từ một máy chủ đến một số lượng lớn máy chủ (được gọi là ngang hàng). Tệp này có thể là phiên bản mới của hệ điều hành Linux, bản vá phần mềm cho hệ điều hành hiện có hoặc tệp video MPEG. Trong phân phối tệp máy khách-máy chủ, máy chủ phải gửi một bản sao của tệp cho từng máy ngang hàng---đặt gánh nặng to lớn lên máy chủ và tiêu tốn một lượng lớn băng thông máy chủ. Trong phân phối tệp P2P, mỗi thiết bị ngang hàng có thể phân phối lại bất kỳ phần nào của tệp mà nó đã nhận được cho bất kỳ thiết bị ngang hàng nào khác, từ đó hỗ trợ máy chủ trong quá trình phân phối. Tính đến năm 2020, giao thức phân phối tệp P2P phổ biến nhất là BitTorrent. Được phát triển ban đầu bởi Bram Cohen, hiện nay có nhiều ứng dụng khách BitTorrent độc lập khác nhau tuân thủ giao thức BitTorrent, cũng như có một số ứng dụng khách trình duyệt Web tuân thủ giao thức HTTP. Trong tiểu mục này, trước tiên chúng tôi kiểm tra khả năng tự mở rộng của kiến ​​trúc P2P trong bối cảnh phân phối tệp. Sau đó chúng tôi mô tả BitTorrent một cách chi tiết, nêu bật các đặc điểm và tính năng quan trọng nhất của nó.

Khả năng mở rộng của Kiến trúc P2P

Để so sánh kiến ​​trúc máy khách-máy chủ với kiến ​​trúc ngang hàng và minh họa khả năng tự mở rộng vốn có của P2P, giờ đây chúng tôi xem xét một mô hình định lượng đơn giản để phân phối tệp tới một nhóm ngang hàng cố định cho cả hai loại kiến ​​trúc. Như được hiển thị trong Hình 2.22, máy chủ và các máy ngang hàng được kết nối với Internet với quyền truy cập

internet

Tập tin: F

Máy chủ

chúng ta

u1 u2

u3

d1

d2

d3

u4

u5 u6

d4

d5

d6

bạn

dN

*Hình 2.22 ♦ Một bài toán phân phối file minh họa*

liên kết. Biểu thị tốc độ tải lên liên kết truy cập của máy chủ thứ i theo ui và tốc độ tải xuống liên kết truy cập của máy ngang hàng thứ i theo di. Đồng thời biểu thị kích thước của tệp sẽ được phân phối (tính bằng bit) bởi F và số lượng đồng nghiệp muốn lấy bản sao của tệp bởi N. Thời gian phân phối là thời gian cần thiết để có được một bản sao của tệp cho tất cả N đồng nghiệp. Trong phân tích của chúng tôi về thời gian phân phối bên dưới, đối với cả kiến ​​trúc máy khách-máy chủ và kiến ​​trúc P2P, chúng tôi đưa ra giả định đơn giản hóa (và nói chung là chính xác \[Akella 2003\]) rằng lõi Internet có băng thông dồi dào, ngụ ý rằng tất cả các tắc nghẽn đều nằm trong mạng truy cập. Chúng tôi cũng cho rằng máy chủ và máy khách không tham gia vào bất kỳ ứng dụng mạng nào khác, do đó tất cả băng thông truy cập tải lên và tải xuống của chúng có thể được dành hoàn toàn cho việc phân phối tệp này.

Trước tiên hãy xác định thời gian phân phối cho kiến ​​trúc máy khách-máy chủ mà chúng ta biểu thị bằng Dcs. Trong kiến ​​trúc máy khách-máy chủ, không có máy ngang hàng nào hỗ trợ việc phân phối tệp. Chúng tôi đưa ra những nhận xét sau:

• Máy chủ phải truyền một bản sao của tệp tới mỗi N máy ngang hàng. Vì vậy, máy chủ phải truyền các bit NF. Vì tốc độ upload của máy chủ là us nên thời gian phân phối file tối thiểu phải là NF/us. • Gọi dmin là tốc độ download của mạng ngang hàng có tốc độ download thấp nhất, tức là dmin = min5d1, dp, . . . , dN6. Thiết bị ngang hàng có tốc độ tải xuống thấp nhất không thể lấy được tất cả F bit của tệp trong thời gian ít hơn F/dmin giây. Như vậy, thời gian phân bố tối thiểu ít nhất là F/dmin.

Kết hợp hai quan sát này lại với nhau, chúng ta có được

Dcs Ú maxb NF

chúng ta

, F

dmin

r\.

Điều này cung cấp giới hạn dưới về thời gian phân phối tối thiểu cho kiến ​​trúc máy khách-máy chủ. Trong các bài tập về nhà, bạn sẽ được yêu cầu chứng minh rằng máy chủ có thể lập lịch truyền của nó để thực sự đạt được giới hạn dưới. Vì vậy, hãy coi giới hạn dưới được cung cấp ở trên làm thời gian phân phối thực tế, nghĩa là

Dcs = maxb NF

chúng ta

, F

dmin

r (2.1)

Chúng ta thấy từ phương trình 2.1 rằng với N đủ lớn, thời gian phân phối máy khách-máy chủ được cho bởi NF/us. Do đó, thời gian phân phối tăng tuyến tính với số lượng đồng nghiệp N. Vì vậy, ví dụ: nếu số lượng đồng nghiệp từ tuần này sang tuần tiếp theo tăng hàng nghìn lần từ một nghìn lên một triệu thì thời gian cần thiết để phân phối tệp cho tất cả các đồng nghiệp sẽ tăng thêm 1.000.

Bây giờ chúng ta hãy thực hiện phân tích tương tự cho kiến ​​trúc P2P, trong đó mỗi thiết bị ngang hàng có thể hỗ trợ máy chủ phân phối tệp. Đặc biệt, khi một thiết bị ngang hàng nhận được một số dữ liệu tệp, nó có thể sử dụng khả năng tải lên của chính mình để phân phối lại dữ liệu cho các thiết bị ngang hàng khác. Tính toán thời gian phân phối cho kiến ​​trúc P2P có phần phức tạp hơn so với kiến ​​trúc máy khách-máy chủ, vì thời gian phân phối phụ thuộc vào cách mỗi thiết bị ngang hàng phân phối các phần của tệp cho các thiết bị ngang hàng khác. Tuy nhiên, có thể thu được một biểu thức đơn giản cho thời gian phân phối tối thiểu \[Kumar 2006\]. Để đạt được mục đích này, trước tiên chúng tôi đưa ra những nhận xét sau:

• Khi bắt đầu phân phối, chỉ có máy chủ mới có tệp. Để đưa tệp này vào cộng đồng ngang hàng, máy chủ phải gửi từng bit của tệp ít nhất một lần vào liên kết truy cập của nó. Như vậy, thời gian phân phối tối thiểu ít nhất là F/us. (Không giống như sơ đồ máy khách-máy chủ, một bit được máy chủ gửi một lần có thể không cần phải được máy chủ gửi lại vì các đồng nghiệp có thể phân phối lại bit đó cho nhau.) • Giống như kiến ​​trúc máy khách-máy chủ, thiết bị ngang hàng có tốc độ tải xuống thấp nhất không thể lấy được tất cả F bit của tệp trong ít hơn F/dmin giây. Như vậy, thời gian phân bố tối thiểu ít nhất là F/dmin. • Cuối cùng, hãy quan sát rằng tổng dung lượng tải lên của toàn bộ hệ thống bằng tốc độ tải lên của máy chủ cộng với tốc độ tải lên của từng thiết bị ngang hàng riêng lẻ, nghĩa là utotal = us + u1 + g+ uN. Hệ thống phải phân phối (tải lên) các bit F cho mỗi N ngang hàng, do đó cung cấp tổng số bit NF. Điều này không thể được thực hiện với tốc độ nhanh hơn tổng cộng. Do đó, thời gian phân phối tối thiểu cũng ít nhất là NF/(us + u1 + g+ uN).

Kết hợp ba quan sát này lại với nhau, chúng ta thu được thời gian phân phối tối thiểu cho P2P, ký hiệu là DP2P.

DP2P Ú tối đa c

F chúng tôi

, F

dmin

, NF

chúng tôi + một

N

tôi=1

ui

s (2.2)

Phương trình 2.2 cung cấp giới hạn dưới cho thời gian phân phối tối thiểu cho kiến ​​trúc P2P. Hóa ra là nếu chúng ta tưởng tượng rằng mỗi thiết bị ngang hàng có thể phân phối lại một chút ngay khi nhận được bit đó thì sẽ có một sơ đồ phân phối lại thực sự đạt được giới hạn dưới này \[Kumar 2006\]. (Chúng tôi sẽ chứng minh trường hợp đặc biệt của kết quả này trong bài tập về nhà.) Trong thực tế, khi các phần của tệp được phân phối lại thay vì các bit riêng lẻ, Phương trình 2.2 đóng vai trò gần đúng về thời gian phân phối tối thiểu thực tế. Vì vậy, hãy lấy giới hạn dưới được cung cấp bởi phương trình 2.2 làm thời gian phân phối tối thiểu thực tế, nghĩa là,

DP2P = tối đa c

F chúng tôi

, F

dmin

, NF

chúng tôi + một

N

tôi=1

ui

s (2.3)

Hình 2.23 so sánh thời gian phân phối tối thiểu cho kiến ​​trúc client-server và P2P giả định rằng tất cả các máy ngang hàng đều có cùng tốc độ tải lên u. Trong Hình 2.23, chúng ta đặt F/u = 1 giờ, us = 10u, và dmin Ú us. Do đó, một máy ngang hàng có thể truyền toàn bộ tệp trong một giờ, tốc độ truyền của máy chủ gấp 10 lần tốc độ tải lên ngang hàng và (để đơn giản) tốc độ tải xuống ngang hàng được đặt đủ lớn để không gây ảnh hưởng. Chúng ta thấy trong Hình 2.23 rằng đối với kiến ​​trúc máy khách-máy chủ, thời gian phân phối tăng tuyến tính và không bị ràng buộc khi số lượng máy ngang hàng tăng lên. Tuy nhiên, đối với kiến ​​trúc P2P, thời gian phân phối tối thiểu không những luôn ít hơn thời gian phân phối của kiến ​​trúc máy khách-máy chủ; thời gian này cũng ít hơn một giờ đối với bất kỳ số lượng ngang hàng N nào. Do đó, các ứng dụng có kiến ​​trúc P2P có thể tự mở rộng quy mô. Khả năng mở rộng này là hệ quả trực tiếp của việc các đồng nghiệp vừa là nhà phân phối lại vừa là người tiêu dùng bit.

BitTorrent

BitTorrent là giao thức P2P phổ biến để phân phối tệp \[Chao 2011\]. Trong biệt ngữ BitTorrent, tập hợp tất cả các đồng nghiệp tham gia phân phối một tệp cụ thể được gọi là torrent. Các thiết bị ngang hàng trong torrent tải xuống các đoạn tệp có kích thước bằng nhau của tệp khác, với kích thước đoạn thông thường là 256 KByte. Khi một thiết bị ngang hàng lần đầu tiên tham gia torrent, nó không có đoạn nào. Theo thời gian nó tích lũy ngày càng nhiều khối. Trong khi nó tải xuống các khối, nó cũng tải các khối lên các đồng nghiệp khác. Sau khi một đồng nghiệp đã có được toàn bộ tệp, nó có thể (ích kỷ) rời khỏi torrent hoặc (một cách vị tha) vẫn ở trong torrent và tiếp tục tải các đoạn lên các đồng nghiệp khác. Ngoài ra, bất kỳ thiết bị ngang hàng nào cũng có thể rời khỏi torrent bất cứ lúc nào chỉ với một tập hợp con các đoạn và sau đó tham gia lại torrent.

N

Thời gian phân phối tối thiểu

0,5

1,5

2,5

1.0

3.0

2.0

3,5

Client-Server

P2P

*Hình 2.23 ♦ Thời gian phân phối cho P2P và kiến ​​trúc client-server*

Bây giờ chúng ta hãy xem xét kỹ hơn cách BitTorrent hoạt động. Vì BitTorrent là một giao thức và hệ thống khá phức tạp nên chúng tôi sẽ chỉ mô tả các cơ chế quan trọng nhất của nó, tìm hiểu kỹ một số chi tiết; điều này sẽ cho phép chúng ta nhìn thấy khu rừng qua những tán cây. Mỗi torrent có một nút cơ sở hạ tầng được gọi là trình theo dõi. Khi một thiết bị ngang hàng tham gia vào torrent, nó sẽ tự đăng ký với trình theo dõi và định kỳ thông báo cho trình theo dõi rằng nó vẫn ở trong torrent. Bằng cách này, trình theo dõi sẽ theo dõi các đồng nghiệp đang tham gia torrent. Một torrent nhất định có thể có ít hơn mười hoặc hơn một nghìn torrent tham gia vào bất kỳ thời điểm nào.

Như được hiển thị trong Hình 2.24, khi một đồng nghiệp mới, Alice, tham gia torrent, trình theo dõi sẽ chọn ngẫu nhiên một tập hợp con các đồng nghiệp (cụ thể là 50) từ nhóm các đồng nghiệp tham gia và gửi địa chỉ IP của 50 đồng nghiệp này cho Alice. Sở hữu danh sách các đồng nghiệp này, Alice cố gắng thiết lập các kết nối TCP đồng thời với tất cả các đồng nghiệp trong danh sách này. Hãy gọi tất cả các đồng nghiệp mà Alice thành công trong việc thiết lập kết nối TCP là "các đồng nghiệp lân cận". (Trong Hình 2.24, Alice được cho thấy chỉ có ba đồng nghiệp lân cận. Thông thường, cô ấy sẽ có nhiều hơn nữa.) Theo thời gian, một số đồng nghiệp này có thể rời đi và những đồng nghiệp khác (ngoài 50 đồng nghiệp lân cận) có thể cố gắng thiết lập TCP kết nối với Alice. Vì vậy, các đồng nghiệp lân cận của một đồng nghiệp sẽ dao động theo thời gian.

Trình theo dõi

Khối giao dịch

ngang hàng

Lấy danh sách các đồng nghiệp

Alice

*Hình 2.24 ♦ Phân phối file bằng BitTorrent*

Tại bất kỳ thời điểm nào, mỗi thiết bị ngang hàng sẽ có một tập hợp con các đoạn từ tệp, với các thiết bị ngang hàng khác nhau có các tập hợp con khác nhau. Theo định kỳ, Alice sẽ hỏi từng đồng nghiệp lân cận của mình (qua kết nối TCP) để biết danh sách các khối mà họ có. Nếu Alice có L hàng xóm khác nhau, cô ấy sẽ nhận được L danh sách các khối. Với kiến ​​thức này, Alice sẽ đưa ra yêu cầu (một lần nữa qua kết nối TCP) cho những đoạn mà cô ấy hiện không có.

Vì vậy, tại bất kỳ thời điểm nào, Alice sẽ có một tập hợp con các khối và sẽ biết hàng xóm của cô ấy có những khối nào. Với thông tin này, Alice sẽ phải đưa ra hai quyết định quan trọng. Đầu tiên, cô ấy nên yêu cầu những phần nào trước từ hàng xóm của mình? Và thứ hai, cô ấy nên gửi những phần được yêu cầu đến những người hàng xóm nào? Khi quyết định yêu cầu khối nào, Alice sử dụng một kỹ thuật gọi là hiếm nhất trước. Ý tưởng là xác định, trong số những khối mà cô ấy không có, những khối hiếm nhất trong số những khối hàng xóm của cô ấy (nghĩa là những khối có ít bản sao lặp lại nhất trong số những khối hàng xóm của cô ấy) và sau đó yêu cầu những khối hiếm nhất đó trước tiên. Theo cách này, các đoạn hiếm nhất sẽ được phân phối lại nhanh hơn, nhằm mục đích (gần như) cân bằng số lượng bản sao của từng đoạn trong torrent.

Để xác định yêu cầu nào cô ấy phản hồi, BitTorrent sử dụng thuật toán giao dịch thông minh. Ý tưởng cơ bản là Alice ưu tiên cho những người hàng xóm hiện đang cung cấp dữ liệu của cô ấy ở tốc độ cao nhất. Cụ thể, đối với mỗi người hàng xóm của mình, Alice liên tục đo tốc độ cô nhận được bit và xác định bốn người đang cho cô ăn bit ở tốc độ cao nhất. Sau đó, cô ấy đáp lại bằng cách gửi các đoạn cho bốn đồng nghiệp này. Cứ sau 10 giây, cô ấy lại tính toán lại tỷ lệ và có thể sửa đổi nhóm bốn đồng nghiệp. Trong biệt ngữ BitTorrent, bốn thiết bị ngang hàng này được cho là không bị nghẹt thở. Điều quan trọng là cứ sau 30 giây, cô ấy cũng chọn ngẫu nhiên thêm một người hàng xóm và gửi cho họ những phần nhỏ. Hãy gọi người ngang hàng được chọn ngẫu nhiên là Bob. Trong biệt ngữ BitTorrent, Bob được cho là người lạc quan không bị nghẹt thở. Vì Alice đang gửi dữ liệu cho Bob nên cô ấy có thể trở thành một trong bốn người tải lên hàng đầu của Bob, trong trường hợp đó Bob sẽ bắt đầu gửi dữ liệu cho Alice. Nếu tốc độ Bob gửi dữ liệu đến Alice đủ cao thì Bob có thể trở thành một trong bốn người tải lên hàng đầu của Alice. Nói cách khác, cứ sau 30 giây, Alice sẽ chọn ngẫu nhiên một đối tác giao dịch mới và bắt đầu giao dịch với đối tác đó. Nếu hai người ngang hàng hài lòng với giao dịch, họ sẽ xếp nhau vào danh sách bốn người đứng đầu và tiếp tục giao dịch với nhau cho đến khi một trong hai người tìm được đối tác tốt hơn. Hiệu quả là các đồng nghiệp có khả năng tải lên với tốc độ tương thích có xu hướng tìm thấy nhau. Việc lựa chọn hàng xóm ngẫu nhiên cũng cho phép các đồng nghiệp mới nhận được nhiều phần để họ có thể có thứ gì đó để trao đổi. Tất cả các đồng nghiệp lân cận khác ngoài năm đồng nghiệp này (bốn đồng nghiệp "hàng đầu" và một đồng nghiệp thăm dò) đều "nghẹt thở", nghĩa là họ không nhận được bất kỳ khối nào từ Alice. BitTorrent có một số cơ chế thú vị chưa được thảo luận ở đây, bao gồm các phần (khối nhỏ), đường dẫn, lựa chọn đầu tiên ngẫu nhiên, chế độ kết thúc và chống đánh cắp \[Cohen 2003\].

Cơ chế khuyến khích giao dịch vừa mô tả thường được gọi là ăn miếng trả miếng \[Cohen 2003\]. Người ta đã chứng minh rằng kế hoạch khuyến khích này có thể bị phá vỡ \[Liogkas 2006; Locher 2006; Piatek 2008\]. Tuy nhiên, hệ sinh thái BitTorrent vẫn cực kỳ thành công, với hàng triệu người cùng lúc tích cực chia sẻ tệp trong

hàng trăm ngàn torrent. Nếu BitTorrent được thiết kế mà không có sự ăn miếng trả miếng (hoặc một biến thể), nhưng nếu không thì hoàn toàn giống nhau, BitTorrent thậm chí có thể sẽ không tồn tại ngay bây giờ, vì phần lớn người dùng sẽ là những người đi tự do \[Saroiu 2002\].

Chúng tôi kết thúc cuộc thảo luận của mình về P2P bằng cách đề cập ngắn gọn đến một ứng dụng khác của P2P, đó là Bảng Hast phân phối (DHT). Bảng băm phân tán là một cơ sở dữ liệu đơn giản, với các bản ghi cơ sở dữ liệu được phân phối trên các cơ sở dữ liệu ngang hàng trong hệ thống P2P. DHT đã được triển khai rộng rãi (ví dụ: trong BitTorrent) và là chủ đề của nhiều nghiên cứu sâu rộng. Tổng quan được cung cấp trong Ghi chú Video trên trang web đồng hành.

**2.6 Mạng phân phối nội dung và truyền phát video**

Theo nhiều ước tính, video phát trực tuyến---bao gồm Netflix, YouTube và Amazon Prime---chiếm khoảng 80% lưu lượng truy cập Internet vào năm 2020 \[Cisco 2020\]. Phần này chúng tôi sẽ cung cấp cái nhìn tổng quan về cách triển khai các dịch vụ truyền phát video phổ biến trên Internet ngày nay. Chúng ta sẽ thấy chúng được triển khai bằng cách sử dụng các giao thức và máy chủ cấp ứng dụng hoạt động theo một số cách giống như bộ đệm.

**2.6.1 Video trên Internet**

Trong các ứng dụng video được lưu trữ trực tuyến, phương tiện cơ bản là video được ghi trước, chẳng hạn như phim, chương trình truyền hình, sự kiện thể thao được ghi trước hoặc video do người dùng tạo trước (chẳng hạn như những video thường thấy trên YouTube). Những video được ghi trước này được đặt trên máy chủ và người dùng gửi yêu cầu đến máy chủ để xem video theo yêu cầu. Nhiều công ty Internet ngày nay cung cấp video phát trực tuyến, bao gồm Netflix, YouTube (Google), Amazon và TikTok.

Nhưng trước khi bắt đầu thảo luận về truyền phát video, trước tiên chúng ta nên tìm hiểu nhanh về chính phương tiện video. Video là một chuỗi hình ảnh, thường được hiển thị ở tốc độ không đổi, chẳng hạn như 24 hoặc 30 hình ảnh mỗi giây. Một hình ảnh được mã hóa kỹ thuật số, không nén bao gồm một mảng pixel, với mỗi pixel được mã hóa thành một số bit để biểu thị độ chói và màu sắc. Một đặc điểm quan trọng của video là nó có thể được nén, do đó đánh đổi chất lượng video bằng tốc độ bit. Các thuật toán nén sẵn có ngày nay có thể nén video về cơ bản ở bất kỳ tốc độ bit nào bạn muốn. Tất nhiên, tốc độ bit càng cao thì chất lượng hình ảnh càng tốt và trải nghiệm xem tổng thể của người dùng càng tốt.

Từ góc độ mạng, có lẽ đặc điểm nổi bật nhất của video là tốc độ bit cao. Video Internet nén thường có tốc độ từ 100 kbps đối với video chất lượng thấp đến hơn 4 Mbps đối với phát trực tuyến phim độ phân giải cao; Truyền phát 4K có tốc độ bit trên 10 Mbps. Điều này có thể dẫn đến lưu lượng truy cập và dung lượng lưu trữ khổng lồ, đặc biệt đối với video cao cấp. Ví dụ: một 2 Mbps

Đi bộ qua các bảng băm phân tán

VideoLưu ý

video có thời lượng 67 phút sẽ tiêu tốn 1 gigabyte dung lượng lưu trữ và lưu lượng. Cho đến nay, thước đo hiệu suất quan trọng nhất để truyền phát video là thông lượng trung bình từ đầu đến cuối. Để cung cấp khả năng phát liên tục, mạng phải cung cấp thông lượng trung bình cho ứng dụng phát trực tuyến ít nhất bằng tốc độ bit của video nén.

Chúng tôi cũng có thể sử dụng tính năng nén để tạo nhiều phiên bản của cùng một video, mỗi phiên bản có mức chất lượng khác nhau. Ví dụ: chúng ta có thể sử dụng tính năng nén để tạo ba phiên bản của cùng một video, ở tốc độ 300 kbps, 1 Mbps và 3 Mbps. Sau đó, người dùng có thể quyết định xem phiên bản nào họ muốn xem tùy theo băng thông hiện có của họ. Người dùng có kết nối Internet tốc độ cao có thể chọn phiên bản 3 Mbps; người dùng xem video qua 3G bằng điện thoại thông minh có thể chọn phiên bản 300 kbps.

**2.6.2 HTTP Truyền phát và DASH**

Khi phát trực tuyến HTTP, video chỉ được lưu trữ tại máy chủ HTTP dưới dạng tệp thông thường có URL cụ thể. Khi người dùng muốn xem video, ứng dụng khách sẽ thiết lập kết nối TCP với máy chủ và đưa ra yêu cầu HTTP GET cho URL đó. Sau đó, máy chủ sẽ gửi tệp video trong thông báo phản hồi HTTP, nhanh như các giao thức mạng cơ bản và điều kiện lưu lượng truy cập cho phép. Về phía máy khách, các byte được thu thập trong bộ đệm ứng dụng máy khách. Khi số byte trong bộ đệm này vượt quá ngưỡng xác định trước, ứng dụng khách sẽ bắt đầu phát lại---cụ thể là ứng dụng truyền phát video sẽ định kỳ lấy các khung hình video từ bộ đệm ứng dụng khách, giải nén các khung hình và hiển thị chúng trên màn hình của người dùng. Do đó, ứng dụng truyền phát video đang hiển thị video khi nó đang nhận và đệm các khung hình tương ứng với các phần sau của video.

Mặc dù tính năng phát trực tuyến HTTP, như được mô tả trong đoạn trước, đã được triển khai rộng rãi trong thực tế (ví dụ: bởi YouTube kể từ khi thành lập), nhưng nó có một thiếu sót lớn: Tất cả các ứng dụng khách đều nhận được cùng một mã hóa video, mặc dù có sự khác biệt lớn về lượng băng thông có sẵn cho một ứng dụng khách, cả trên các ứng dụng khách khác nhau và cũng theo thời gian cho cùng một ứng dụng khách. Điều này đã dẫn đến sự phát triển của một loại phát trực tuyến mới dựa trên HTTP, thường được gọi là Truyền phát thích ứng động qua HTTP (DASH). Trong DASH, video được mã hóa thành nhiều phiên bản khác nhau, mỗi phiên bản có tốc độ bit khác nhau và tương ứng là mức chất lượng khác nhau. Máy khách yêu cầu động các đoạn video có độ dài vài giây. Khi lượng băng thông khả dụng cao, máy khách sẽ tự nhiên chọn các đoạn từ phiên bản tốc độ cao; và khi băng thông khả dụng thấp, nó sẽ tự động chọn phiên bản tốc độ thấp. Máy khách chọn từng phần khác nhau bằng HTTP GET thông báo yêu cầu \[Akhshabi 2011\].

DASH cho phép khách hàng có tốc độ truy cập Internet khác nhau phát trực tuyến video ở các tốc độ mã hóa khác nhau. Khách hàng có kết nối 3G tốc độ thấp có thể nhận được phiên bản tốc độ bit thấp (và chất lượng thấp) và khách hàng có kết nối cáp quang có thể nhận được phiên bản chất lượng cao. DASH cũng cho phép khách hàng thích ứng với băng thông có sẵn nếu băng thông đầu cuối có sẵn thay đổi trong phiên. Tính năng này là

đặc biệt quan trọng đối với người dùng di động, những người thường thấy tính sẵn có của băng thông dao động khi họ di chuyển đến các trạm cơ sở.

Với DASH, mỗi phiên bản video được lưu trữ trong máy chủ HTTP, mỗi phiên bản có một URL khác nhau. Máy chủ HTTP cũng có tệp kê khai cung cấp URL cho từng phiên bản cùng với tốc độ bit của nó. Trước tiên, khách hàng yêu cầu tệp kê khai và tìm hiểu về các phiên bản khác nhau. Sau đó, máy khách sẽ chọn từng đoạn một bằng cách chỉ định một URL và phạm vi byte trong thông báo yêu cầu HTTP GET cho mỗi đoạn. Trong khi tải xuống các đoạn, máy khách cũng đo băng thông nhận được và chạy thuật toán xác định tốc độ để chọn đoạn cần yêu cầu tiếp theo. Đương nhiên, nếu máy khách có nhiều video được lưu vào bộ đệm và nếu băng thông nhận đo được cao thì nó sẽ chọn một đoạn từ phiên bản tốc độ bit cao. Và tất nhiên, nếu máy khách có ít video được lưu vào bộ đệm và băng thông nhận được đo được thấp, nó sẽ chọn một đoạn từ phiên bản tốc độ bit thấp. Do đó, DASH cho phép khách hàng tự do chuyển đổi giữa các mức chất lượng khác nhau.

**2.6.3 Mạng phân phối nội dung**

Ngày nay, nhiều công ty video trên Internet đang phân phối các luồng đa Mbps theo yêu cầu cho hàng triệu người dùng hàng ngày. YouTube chẳng hạn, với thư viện hàng trăm triệu video, mỗi ngày phân phối hàng trăm triệu luồng video đến người dùng trên toàn thế giới. Truyền tất cả lưu lượng truy cập này đến các địa điểm trên khắp thế giới trong khi vẫn cung cấp khả năng phát liên tục và tính tương tác cao rõ ràng là một nhiệm vụ đầy thách thức.

Đối với một công ty video trên Internet, có lẽ cách tiếp cận đơn giản nhất để cung cấp dịch vụ truyền phát video là xây dựng một trung tâm dữ liệu lớn duy nhất, lưu trữ tất cả video trong trung tâm dữ liệu và truyền phát video trực tiếp từ trung tâm dữ liệu đến khách hàng trên toàn thế giới. Nhưng có ba vấn đề lớn với cách tiếp cận này. Đầu tiên, nếu máy khách ở xa trung tâm dữ liệu, các gói từ máy chủ đến máy khách sẽ đi qua nhiều liên kết truyền thông và có thể đi qua nhiều ISP, trong đó một số ISP có thể nằm ở các châu lục khác nhau. Nếu một trong những liên kết này cung cấp thông lượng nhỏ hơn tốc độ tiêu thụ video thì thông lượng từ đầu đến cuối cũng sẽ thấp hơn tốc độ tiêu thụ, dẫn đến sự chậm trễ gây khó chịu cho người dùng. (Hãy nhớ lại Chương 1 rằng thông lượng từ đầu đến cuối của một luồng bị chi phối bởi thông lượng tại liên kết thắt cổ chai.) Khả năng điều này xảy ra tăng lên khi số lượng liên kết trong đường dẫn từ đầu đến cuối tăng lên. Hạn chế thứ hai là một video phổ biến có thể sẽ được gửi nhiều lần qua cùng một liên kết truyền thông. Điều này không chỉ gây lãng phí băng thông mạng mà bản thân công ty video Internet sẽ phải trả tiền cho nhà cung cấp ISP (được kết nối với trung tâm dữ liệu) của mình để gửi đi gửi lại các byte giống nhau vào Internet. Vấn đề thứ ba với giải pháp này là một trung tâm dữ liệu có một điểm lỗi duy nhất---nếu trung tâm dữ liệu hoặc các liên kết với Internet của nó bị hỏng, nó sẽ không thể phân phối bất kỳ luồng video nào.

Để đáp ứng thách thức phân phối lượng lớn dữ liệu video cho người dùng trên toàn thế giới, hầu hết tất cả các công ty phát trực tuyến video lớn đều sử dụng Mạng phân phối nội dung (CDN). CDN quản lý các máy chủ ở

nhiều vị trí được phân bổ theo địa lý, lưu trữ bản sao của video (và các loại nội dung Web khác, bao gồm tài liệu, hình ảnh và âm thanh) trong máy chủ của nó và cố gắng hướng từng yêu cầu của người dùng đến vị trí CDN sẽ cung cấp trải nghiệm người dùng tốt nhất. CDN có thể là CDN riêng, nghĩa là do chính nhà cung cấp nội dung sở hữu; ví dụ: CDN của Google phân phối video YouTube và các loại nội dung khác. CDN có thể là CDN của bên thứ ba phân phối nội dung thay mặt cho nhiều nhà cung cấp nội dung; Akamai, Limelight và Level-3 đều vận hành CDN của bên thứ ba. Một cái nhìn tổng quan rất dễ đọc về CDN hiện đại là \[Leighton 2009; Nygren 2010\].

CDN thường áp dụng một trong hai triết lý đặt máy chủ khác nhau \[Huang 2008\]:

• Vào sâu. Một triết lý do Akamai tiên phong là thâm nhập sâu vào mạng truy cập của các Nhà cung cấp dịch vụ Internet, bằng cách triển khai các cụm máy chủ tại các ISP truy cập trên toàn thế giới. (Mạng truy cập được mô tả trong Phần 1.3.) Akamai thực hiện phương pháp này với các cụm ở hàng nghìn địa điểm. Mục tiêu là đến gần hơn với người dùng cuối, từ đó cải thiện độ trễ và thông lượng mà người dùng nhận thấy bằng cách giảm số lượng liên kết và bộ định tuyến giữa người dùng cuối và máy chủ CDN nơi họ nhận nội dung. Do thiết kế có tính phân tán cao này nên nhiệm vụ duy trì và quản lý các cụm trở nên khó khăn. • Mang về nhà. Triết lý thiết kế thứ hai, được Limelight và nhiều công ty CDN khác áp dụng, là đưa các ISP về nhà bằng cách xây dựng các cụm lớn với số lượng nhỏ hơn (ví dụ: hàng chục) trang web. Thay vì vào bên trong các ISP truy cập, các CDN này thường đặt cụm của chúng trong Điểm trao đổi Internet (IXP) (xem Phần 1.3). So với triết lý thiết kế chuyên sâu, thiết kế mang về nhà thường dẫn đến chi phí quản lý và bảo trì thấp hơn, có thể phải trả giá bằng độ trễ cao hơn và thông lượng thấp hơn cho người dùng cuối.

Khi các cụm của nó đã được thiết lập xong, CDN sẽ sao chép nội dung trên các cụm của nó. CDN có thể không muốn đặt bản sao của mọi video trong mỗi cụm vì một số video hiếm khi được xem hoặc chỉ phổ biến ở một số quốc gia. Trên thực tế, nhiều CDN không đẩy video vào cụm của chúng mà thay vào đó sử dụng chiến lược kéo đơn giản: Nếu khách hàng yêu cầu video từ cụm không lưu trữ video thì cụm sẽ truy xuất video (từ kho lưu trữ trung tâm hoặc từ một cụm khác) và lưu trữ một bản sao cục bộ trong khi truyền phát video đến khách hàng cùng một lúc. Tương tự như bộ nhớ đệm Web (xem Phần 2.2.5), khi bộ nhớ của cụm đầy, nó sẽ xóa các video không được yêu cầu thường xuyên.

Hoạt động CDN

Sau khi đã xác định được hai cách tiếp cận chính trong việc triển khai CDN, bây giờ chúng ta hãy đi sâu vào chi tiết về cách thức hoạt động của CDN. Khi một trình duyệt trong máy của người dùng

máy chủ được hướng dẫn truy xuất một video cụ thể (được xác định bằng URL), CDN phải chặn yêu cầu để có thể (1) xác định cụm máy chủ CDN phù hợp cho máy khách đó tại thời điểm đó và (2) chuyển hướng yêu cầu của máy khách đến máy chủ trong cụm đó. Chúng tôi sẽ thảo luận ngắn gọn về cách CDN có thể xác định cụm phù hợp. Nhưng trước tiên hãy xem xét cơ chế đằng sau việc chặn và chuyển hướng một yêu cầu.

Hầu hết CDN đều tận dụng DNS để chặn và chuyển hướng yêu cầu; một cuộc thảo luận thú vị về việc sử dụng DNS như vậy là \[Vixie 2009\]. Hãy xem xét một điều đơn giản

CƠ SỞ HẠ TẦNG MẠNG CỦA GOOGLE

Để hỗ trợ hàng loạt dịch vụ của mình---bao gồm tìm kiếm, Gmail, lịch, video YouTube, bản đồ, tài liệu và mạng xã hội---Google đã triển khai một mạng riêng và cơ sở hạ tầng CDN rộng khắp. Cơ sở hạ tầng CDN của Google có ba tầng cụm máy chủ:

• Mười chín "trung tâm dữ liệu lớn" ở Bắc Mỹ, Châu Âu và Châu Á \[Google Locations 2020\], với mỗi trung tâm dữ liệu có khoảng 100.000 máy chủ. Các trung tâm dữ liệu lớn này chịu trách nhiệm cung cấp nội dung động (và thường được cá nhân hóa), bao gồm kết quả tìm kiếm và thư Gmail. • Với khoảng 90 cụm trong IXP rải rác khắp thế giới, mỗi cụm bao gồm hàng trăm máy chủ \[Adhikari 2011a\] \[Google CDN 2020\]. Các cụm này chịu trách nhiệm phân phát nội dung tĩnh, bao gồm cả video YouTube. • Hàng trăm cụm "enter-deep" nằm trong ISP truy cập. Ở đây một cụm thường bao gồm hàng chục máy chủ trong một giá đỡ. Các máy chủ chuyên sâu này thực hiện phân tách TCP (xem Phần 3.7) và cung cấp nội dung tĩnh \[Chen 2011\], bao gồm các phần tĩnh của trang Web thể hiện kết quả tìm kiếm.

Tất cả các trung tâm dữ liệu và vị trí cụm này đều được kết nối với nhau bằng mạng riêng của Google. Khi người dùng thực hiện truy vấn tìm kiếm, truy vấn thường được gửi trước tiên qua ISP cục bộ tới bộ nhớ đệm sâu gần đó, từ đó nội dung tĩnh được truy xuất; trong khi cung cấp nội dung tĩnh cho máy khách, bộ nhớ đệm lân cận cũng chuyển tiếp truy vấn qua mạng riêng của Google tới một trong các trung tâm dữ liệu lớn, từ đó truy xuất các kết quả tìm kiếm được cá nhân hóa. Đối với video YouTube, bản thân video có thể đến từ một trong các bộ đệm mang về nhà, trong khi các phần của trang Web xung quanh video có thể đến từ bộ nhớ đệm sâu gần đó và các quảng cáo xung quanh video đến từ trung tâm dữ liệu. Tóm lại, ngoại trừ các ISP địa phương, các dịch vụ đám mây của Google phần lớn được cung cấp bởi cơ sở hạ tầng mạng độc lập với Internet công cộng.

NGHIÊN CỨU TRƯỜNG HỢP

ví dụ để minh họa cách DNS thường liên quan. Giả sử nhà cung cấp nội dung, NetCinema, thuê công ty CDN bên thứ ba, KingCDN, để phân phối video của mình cho khách hàng. Trên các trang Web NetCinema, mỗi video của nó được gán một URL bao gồm chuỗi "video" và mã nhận dạng duy nhất cho chính video đó; ví dụ: Transformers 7 có thể được chỉ định http://video.netcinema.com/6Y7B23V. Sáu bước sau đó sẽ xảy ra, như trong Hình 2.25:

1\. Người dùng truy cập vào trang Web tại NetCinema. 2. Khi người dùng nhấp vào liên kết http://video.netcinema.com/6Y7B23V,

máy chủ của người dùng gửi truy vấn DNS cho video.netcinema.com. 3. Máy chủ DNS cục bộ (LDNS) của người dùng chuyển tiếp truy vấn DNS tới một truy vấn có thẩm quyền

DNS máy chủ dành cho NetCinema, máy chủ này quan sát chuỗi "video" trong tên máy chủ video.netcinema.com. Để "chuyển giao" truy vấn DNS cho KingCDN, thay vì trả về địa chỉ IP, máy chủ DNS có thẩm quyền của NetCinema sẽ trả về LDNS một tên máy chủ trong miền của KingCDN, ví dụ: a1105.kingcdn.com. 4. Từ thời điểm này trở đi, truy vấn DNS sẽ đi vào cơ sở hạ tầng DNS riêng tư của KingCDN

kết cấu. LDNS của người dùng sau đó sẽ gửi truy vấn thứ hai, bây giờ là a1105.kingcdn. com và hệ thống DNS của KingCDN cuối cùng sẽ trả về địa chỉ IP của máy chủ nội dung KingCDN cho LDNS. Do đó, ở đây, trong hệ thống DNS của KingCDN, máy chủ CDN mà khách hàng sẽ nhận nội dung của nó sẽ được chỉ định.

Máy chủ DNS cục bộ

NetCinema có thẩm quyền

DNS máy chủ

www.NetCinema.com

KingCDN có thẩm quyền

máy chủ Máy chủ phân phối nội dung KingCDN

*Hình 2.25 ♦ DNS chuyển hướng yêu cầu của người dùng đến máy chủ CDN*

5\. LDNS chuyển tiếp địa chỉ IP của nút CDN cung cấp nội dung tới nút

máy chủ của người dùng. 6. Sau khi máy khách nhận được địa chỉ IP cho máy chủ nội dung KingCDN, nó sẽ thiết lập-

tạo kết nối TCP trực tiếp với máy chủ tại địa chỉ IP đó và đưa ra yêu cầu HTTP GET cho video. Nếu DASH được sử dụng, trước tiên máy chủ sẽ gửi cho khách hàng một tệp kê khai có danh sách các URL, một URL cho mỗi phiên bản của video và khách hàng sẽ tự động chọn các đoạn từ các phiên bản khác nhau.

Chiến lược lựa chọn cụm

Cốt lõi của bất kỳ hoạt động triển khai CDN nào là chiến lược lựa chọn cụm, tức là cơ chế hướng động các máy khách đến cụm máy chủ hoặc trung tâm dữ liệu trong CDN. Như chúng ta vừa thấy, CDN tìm hiểu địa chỉ IP của máy chủ LDNS của khách hàng thông qua tra cứu DNS của khách hàng. Sau khi tìm hiểu địa chỉ IP này, CDN cần chọn một cụm thích hợp dựa trên địa chỉ IP này. CDN thường sử dụng các chiến lược lựa chọn cụm độc quyền. Bây giờ chúng tôi khảo sát ngắn gọn một số cách tiếp cận, mỗi cách đều có ưu điểm và nhược điểm riêng.

Một chiến lược đơn giản là chỉ định máy khách vào cụm gần nhất về mặt địa lý. Sử dụng cơ sở dữ liệu vị trí địa lý thương mại (chẳng hạn như Quova \[Quova 2020\] và MaxMind \[MaxMind 2020\]), mỗi địa chỉ LDNS IP được ánh xạ tới một vị trí địa lý. Khi nhận được yêu cầu DNS từ một LDNS cụ thể, CDN sẽ chọn cụm gần nhất về mặt địa lý, tức là cụm cách LDNS ít km nhất "theo đường chim bay". Giải pháp như vậy có thể hoạt động khá tốt đối với phần lớn khách hàng \[Agarwal 2009\]. Tuy nhiên, đối với một số khách hàng, giải pháp có thể hoạt động kém vì cụm gần nhất về mặt địa lý có thể không phải là cụm gần nhất về độ dài hoặc số bước nhảy của đường dẫn mạng. Hơn nữa, một vấn đề cố hữu với tất cả các phương pháp tiếp cận dựa trên DNS là một số người dùng cuối được cấu hình để sử dụng LDNS được định vị từ xa \[Shaikh 2001; Mao 2002\], trong trường hợp đó vị trí LDNS có thể ở xa vị trí của khách hàng. Hơn nữa, chiến lược đơn giản này bỏ qua sự thay đổi về độ trễ và băng thông khả dụng theo thời gian của các đường dẫn Internet, luôn chỉ định cùng một cụm cho một máy khách cụ thể.

Để xác định cụm tốt nhất cho máy khách dựa trên điều kiện lưu lượng truy cập hiện tại, thay vào đó, CDN có thể thực hiện các phép đo thời gian thực định kỳ về hiệu suất trễ và mất mát giữa cụm của chúng và máy khách. Ví dụ: CDN có thể yêu cầu mỗi cụm của nó gửi các thăm dò định kỳ (ví dụ: tin nhắn ping hoặc truy vấn DNS) tới tất cả các LDNS trên toàn thế giới. Một nhược điểm của phương pháp này là nhiều LDNS được cấu hình để không phản hồi với các thăm dò như vậy.

**2.6.4 Nghiên cứu điển hình: Netflix và YouTube**

Chúng tôi kết thúc cuộc thảo luận về phát trực tuyến video được lưu trữ bằng cách xem xét hai triển khai quy mô lớn rất thành công: Netflix và YouTube. Chúng ta sẽ thấy rằng mỗi hệ thống này có một cách tiếp cận rất khác nhau nhưng vẫn sử dụng nhiều nguyên tắc cơ bản được thảo luận trong phần này.

Netflix

Tính đến năm 2020, Netflix là nhà cung cấp dịch vụ phim và phim truyền hình trực tuyến hàng đầu ở Bắc Mỹ. Như chúng tôi thảo luận bên dưới, việc phân phối video Netflix có hai thành phần chính: đám mây Amazon và cơ sở hạ tầng CDN riêng của nó.

Netflix có một trang web xử lý nhiều chức năng, bao gồm đăng ký và đăng nhập người dùng, thanh toán, danh mục phim để duyệt và tìm kiếm cũng như hệ thống đề xuất phim. Như được hiển thị trong Hình 2.26, trang Web này (và các cơ sở dữ liệu phụ trợ liên quan của nó) chạy hoàn toàn trên các máy chủ Amazon trong đám mây Amazon. Ngoài ra, đám mây Amazon xử lý các chức năng quan trọng sau:

• Nhập nội dung. Trước khi Netflix có thể phân phối phim cho khách hàng, trước tiên Netflix phải nhập và xử lý phim. Netflix nhận các phiên bản phim chính của studio và tải chúng lên máy chủ trên đám mây Amazon. • Xử lý nội dung. Các máy trong đám mây Amazon tạo ra nhiều định dạng khác nhau cho từng bộ phim, phù hợp với nhiều loại trình phát video khách hàng chạy trên máy tính để bàn, điện thoại thông minh và máy chơi game được kết nối với TV. Một phiên bản khác được tạo cho từng định dạng này và ở nhiều tốc độ bit, cho phép truyền phát thích ứng qua HTTP bằng DASH. • Tải các phiên bản lên CDN của nó. Khi tất cả các phiên bản của một bộ phim đã được tạo, các máy chủ trong đám mây Amazon sẽ tải các phiên bản đó lên CDN của nó.

Đám mây Amazon

máy chủ CDN

máy chủ CDN

Tải phiên bản lên CDN

máy chủ CDN

Khách hàng

Tệp kê khai

Đoạn video (DASH)

*Hình 2.26 ♦ Nền tảng phát video trực tuyến Netflix*

Khi Netflix lần đầu tiên triển khai dịch vụ phát video trực tuyến vào năm 2007, họ đã thuê ba công ty CDN bên thứ ba để phân phối nội dung video của mình. Netflix kể từ đó đã tạo CDN riêng của mình, từ đó nó phát trực tuyến tất cả các video của mình. Để tạo CDN của riêng mình, Netflix đã cài đặt các giá đỡ máy chủ cả trong IXP và trong chính các ISP dân cư. Netflix hiện có giá đỡ máy chủ ở hơn 200 địa điểm IXP; xem \[Bottger 2018\] \[Netflix Open Connect 2020\] để biết danh sách hiện tại về các IXP chứa giá đỡ Netflix. Ngoài ra còn có hàng trăm địa điểm ISP chứa giá đỡ Netflix; đồng thời xem \[Netflix Open Connect 2020\], nơi Netflix cung cấp hướng dẫn cho các đối tác ISP tiềm năng về cách cài đặt giá Netflix (miễn phí) cho mạng của họ. Mỗi máy chủ trong giá có một số cổng Ethernet 10 Gbps và dung lượng lưu trữ hơn 100 terabyte. Số lượng máy chủ trong một giá khác nhau: Cài đặt IXP thường có hàng chục máy chủ và chứa toàn bộ thư viện video phát trực tuyến Netflix, bao gồm nhiều phiên bản video để hỗ trợ DASH. Netflix không sử dụng bộ nhớ đệm kéo (Phần 2.2.5) để đưa các máy chủ CDN của mình vào IXP và ISP. Thay vào đó, Netflix phân phối bằng cách đẩy video lên máy chủ CDN của mình trong giờ thấp điểm. Đối với những vị trí không thể chứa toàn bộ thư viện, Netflix chỉ đưa ra những video phổ biến nhất, được xác định hàng ngày. Thiết kế Netflix CDN được mô tả chi tiết trong các video YouTube \[Netflix Video 1\] và \[Netflix Video 2\]; xem thêm \[Bottger 2018\].

Sau khi mô tả các thành phần của kiến ​​trúc Netflix, chúng ta hãy xem xét kỹ hơn sự tương tác giữa máy khách và các máy chủ khác nhau có liên quan đến việc phân phối phim. Như đã chỉ ra trước đó, các trang Web để duyệt thư viện video Netflix được cung cấp từ các máy chủ trên đám mây Amazon. Khi người dùng chọn phim để phát, phần mềm Netflix chạy trên đám mây Amazon trước tiên sẽ xác định máy chủ CDN nào có bản sao của phim. Trong số các máy chủ có phim, phần mềm sẽ xác định máy chủ "tốt nhất" cho yêu cầu của khách hàng đó. Nếu máy khách đang sử dụng ISP dân dụng có giá máy chủ Netflix CDN được cài đặt trong ISP đó và giá này có bản sao của phim được yêu cầu thì máy chủ trong giá này thường được chọn. Nếu không, máy chủ ở IXP gần đó thường được chọn.

Sau khi Netflix xác định máy chủ CDN sẽ phân phối nội dung, Netflix sẽ gửi cho khách hàng địa chỉ IP của máy chủ cụ thể cũng như tệp kê khai có URL cho các phiên bản khác nhau của phim được yêu cầu. Sau đó, máy khách và máy chủ CDN đó tương tác trực tiếp bằng phiên bản DASH độc quyền. Cụ thể, như được mô tả trong Phần 2.6.2, máy khách sử dụng tiêu đề phạm vi byte trong các thông báo yêu cầu HTTP GET để yêu cầu các đoạn từ các phiên bản khác nhau của phim. Netflix sử dụng các đoạn dài khoảng bốn giây \[Adhikari 2012\]. Trong khi các đoạn đang được tải xuống, máy khách sẽ đo thông lượng nhận được và chạy thuật toán xác định tốc độ để xác định chất lượng của đoạn tiếp theo cần yêu cầu.

Netflix thể hiện nhiều nguyên tắc chính được thảo luận trước đó trong phần này, bao gồm phát trực tuyến thích ứng và phân phối CDN. Tuy nhiên, vì Netflix sử dụng CDN riêng của mình, chỉ phân phối video (chứ không phải các trang Web), Netflix có thể đơn giản hóa và điều chỉnh thiết kế CDN của mình. Đặc biệt, Netflix không cần sử dụng chuyển hướng DNS, như đã thảo luận trong Phần 2.6.3, để kết nối một máy khách cụ thể với máy chủ CDN; thay vào đó, phần mềm Netflix (chạy trên đám mây Amazon) trực tiếp thông báo

khách hàng sử dụng một máy chủ CDN cụ thể. Hơn nữa, Netflix CDN sử dụng bộ nhớ đệm đẩy thay vì bộ nhớ đệm kéo (Phần 2.2.5): nội dung được đẩy vào máy chủ vào thời gian đã lên lịch vào giờ thấp điểm, thay vì tự động khi bộ nhớ đệm bị thiếu.

YouTube

Với hàng trăm giờ video được tải lên YouTube mỗi phút và vài tỷ lượt xem video mỗi ngày, YouTube chắc chắn là trang chia sẻ video lớn nhất thế giới. YouTube bắt đầu dịch vụ vào tháng 4 năm 2005 và được Google mua lại vào tháng 11 năm 2006. Mặc dù thiết kế và giao thức của Google/YouTube là độc quyền nhưng thông qua một số nỗ lực đo lường độc lập, chúng tôi có thể hiểu cơ bản về cách YouTube vận hành \[Zink 2009; Torres 2011; Adhikari 2011a\]. Giống như Netflix, YouTube sử dụng rộng rãi công nghệ CDN để phân phối video của mình \[Torres 2011\]. Tương tự như Netflix, Google sử dụng CDN riêng của mình để phân phối video YouTube và đã cài đặt cụm máy chủ ở hàng trăm địa điểm IXP và ISP khác nhau. Từ những địa điểm này và trực tiếp từ các trung tâm dữ liệu khổng lồ của mình, Google phân phối video YouTube \[Adhikari 2011a\]. Tuy nhiên, không giống như Netflix, Google sử dụng bộ nhớ đệm kéo, như được mô tả trong Phần 2.2.5 và chuyển hướng DNS, như được mô tả trong Phần 2.6.3. Trong hầu hết các trường hợp, chiến lược chọn cụm của Google sẽ hướng máy khách đến cụm mà RTT giữa máy khách và cụm là thấp nhất; tuy nhiên, để cân bằng tải giữa các cụm, đôi khi máy khách được chuyển hướng (thông qua DNS) đến một cụm ở xa hơn \[Torres 2011\].

YouTube sử dụng tính năng phát trực tuyến HTTP, thường cung cấp một số lượng nhỏ phiên bản khác nhau cho video, mỗi phiên bản có tốc độ bit khác nhau và mức chất lượng tương ứng. YouTube không sử dụng tính năng phát trực tuyến thích ứng (chẳng hạn như DASH) mà thay vào đó yêu cầu người dùng chọn phiên bản theo cách thủ công. Để tiết kiệm băng thông và tài nguyên máy chủ có thể bị lãng phí do thay đổi vị trí hoặc chấm dứt sớm, YouTube sử dụng yêu cầu phạm vi byte HTTP để hạn chế luồng dữ liệu được truyền sau khi lượng video mục tiêu được tìm nạp trước.

Hàng triệu video được tải lên YouTube mỗi ngày. Video YouTube không chỉ được truyền trực tuyến từ máy chủ đến máy khách qua HTTP mà người tải lên YouTube còn tải video của họ từ máy khách lên máy chủ qua HTTP. YouTube xử lý từng video mà nó nhận được, chuyển đổi nó sang định dạng video YouTube và tạo ra nhiều phiên bản ở các tốc độ bit khác nhau. Quá trình xử lý này diễn ra hoàn toàn trong trung tâm dữ liệu của Google. (Xem nghiên cứu điển hình về cơ sở hạ tầng mạng của Google ở ​​Phần 2.6.3.)

**2.7 Socket Lập trình: Tạo ứng dụng mạng**

Bây giờ chúng ta đã xem xét một số ứng dụng mạng quan trọng, hãy cùng khám phá cách các chương trình ứng dụng mạng thực sự được tạo ra như thế nào. Hãy nhớ lại Phần 2.1 rằng một ứng dụng mạng điển hình bao gồm một cặp chương trình---chương trình khách và

một chương trình máy chủ---nằm trong hai hệ thống đầu cuối khác nhau. Khi hai chương trình này được thực thi, một tiến trình máy khách và một tiến trình máy chủ sẽ được tạo và các tiến trình này giao tiếp với nhau bằng cách đọc và ghi vào các ổ cắm. Do đó, khi tạo một ứng dụng mạng, nhiệm vụ chính của nhà phát triển là viết mã cho cả chương trình máy khách và máy chủ.

Có hai loại ứng dụng mạng. Một loại là một triển khai mà hoạt động của nó được chỉ định trong một tiêu chuẩn giao thức, chẳng hạn như RFC hoặc một số tài liệu tiêu chuẩn khác; một ứng dụng như vậy đôi khi được gọi là "mở", vì tất cả các quy tắc chỉ định hoạt động của nó đều được biết đến. Để thực hiện như vậy, các chương trình máy khách và máy chủ phải tuân thủ các quy tắc do RFC đưa ra. Ví dụ: chương trình máy khách có thể là một triển khai phía máy khách của giao thức HTTP, được mô tả trong Phần 2.2 và được xác định chính xác trong RFC 2616; tương tự, chương trình máy chủ có thể là một triển khai của giao thức máy chủ HTTP, cũng được xác định chính xác trong RFC 2616. Nếu một nhà phát triển viết mã cho chương trình máy khách và một nhà phát triển khác viết mã cho chương trình máy chủ và cả hai nhà phát triển đều tuân thủ cẩn thận các quy tắc của RFC thì hai chương trình sẽ có thể tương tác với nhau. Thật vậy, nhiều ứng dụng mạng ngày nay liên quan đến giao tiếp giữa các chương trình máy khách và máy chủ được tạo bởi các nhà phát triển độc lập---ví dụ: trình duyệt Google Chrome giao tiếp với máy chủ Web Apache hoặc ứng dụng khách BitTorrent giao tiếp với trình theo dõi BitTorrent.

Loại ứng dụng mạng khác là ứng dụng mạng độc quyền. Trong trường hợp này, các chương trình máy khách và máy chủ sử dụng giao thức lớp ứng dụng chưa được xuất bản công khai trong RFC hoặc nơi khác. Một nhà phát triển (hoặc nhóm phát triển) duy nhất tạo ra cả chương trình máy khách và máy chủ, đồng thời nhà phát triển có toàn quyền kiểm soát nội dung trong mã. Nhưng vì mã không triển khai giao thức mở nên các nhà phát triển độc lập khác sẽ không thể phát triển mã tương tác với ứng dụng.

Trong phần này, chúng ta sẽ xem xét các vấn đề chính trong việc phát triển ứng dụng máy khách-máy chủ và chúng ta sẽ "làm bẩn tay" bằng cách xem mã triển khai một ứng dụng máy khách-máy chủ rất đơn giản. Trong giai đoạn phát triển, một trong những quyết định đầu tiên mà nhà phát triển phải đưa ra là liệu ứng dụng sẽ chạy trên TCP hay trên UDP. Hãy nhớ lại rằng TCP được định hướng kết nối và cung cấp kênh luồng byte đáng tin cậy thông qua đó dữ liệu được truyền giữa hai hệ thống đầu cuối. UDP không có kết nối và gửi các gói dữ liệu độc lập từ hệ thống đầu này sang hệ thống đầu kia mà không có bất kỳ đảm bảo nào về việc phân phối. Cũng nhớ lại rằng khi một chương trình máy khách hoặc máy chủ thực hiện một giao thức được xác định bởi RFC, nó phải sử dụng số cổng phổ biến được liên kết với giao thức đó; ngược lại, khi phát triển một ứng dụng độc quyền, nhà phát triển phải cẩn thận tránh sử dụng các số cổng nổi tiếng như vậy. (Port số đã được thảo luận ngắn gọn trong Phần 2.1. Chúng được trình bày chi tiết hơn trong Chương 3.)

Chúng tôi giới thiệu lập trình socket UDP và TCP bằng ứng dụng UDP đơn giản và ứng dụng TCP đơn giản. Chúng tôi trình bày các ứng dụng UDP và TCP đơn giản trong Python 3. Chúng tôi có thể viết mã bằng Java, C hoặc C++, nhưng chúng tôi chủ yếu chọn Python vì Python trình bày rõ ràng các khái niệm ổ cắm khóa. Với

Python có ít dòng mã hơn và mỗi dòng có thể được giải thích cho người lập trình mới làm quen mà không gặp khó khăn. Nhưng không cần phải lo lắng nếu bạn chưa quen với Python. Bạn sẽ có thể dễ dàng theo dõi mã nếu bạn có kinh nghiệm lập trình bằng Java, C hoặc C++.

Nếu bạn quan tâm đến lập trình máy khách-máy chủ bằng Java, bạn nên xem Trang web đồng hành để biết sách giáo khoa này; trên thực tế, bạn có thể tìm thấy ở đó tất cả các ví dụ trong phần này (và các phòng thí nghiệm liên quan) bằng Java. Đối với những độc giả quan tâm đến lập trình máy khách-máy chủ bằng C, có một số tài liệu tham khảo hữu ích \[Donahoo 2001; Stevens 1997; Sương giá 1994\]; Các ví dụ Python của chúng tôi bên dưới có giao diện tương tự như C.

**2.7.1 Socket Lập trình với UDP**

Trong tiểu mục này, chúng ta sẽ viết các chương trình máy khách-máy chủ đơn giản sử dụng UDP; trong phần sau, chúng ta sẽ viết các chương trình tương tự sử dụng TCP.

Hãy nhớ lại Phần 2.1 rằng các tiến trình chạy trên các máy khác nhau giao tiếp với nhau bằng cách gửi tin nhắn vào các socket. Chúng ta đã nói rằng mỗi quy trình tương tự như một ngôi nhà và ổ cắm của quy trình tương tự như một cánh cửa. Ứng dụng nằm ở một bên cửa trong nhà; giao thức lớp vận chuyển nằm ở phía bên kia cánh cửa với thế giới bên ngoài. Nhà phát triển ứng dụng có quyền kiểm soát mọi thứ ở phía lớp ứng dụng của socket; tuy nhiên, nó có rất ít quyền kiểm soát phía tầng vận chuyển.

Bây giờ chúng ta hãy xem xét kỹ hơn sự tương tác giữa hai quy trình giao tiếp sử dụng ổ cắm UDP. Trước khi quá trình gửi có thể đẩy một gói dữ liệu ra khỏi cửa socket, khi sử dụng UDP, trước tiên nó phải đính kèm địa chỉ đích vào gói. Sau khi gói đi qua socket của người gửi, Internet sẽ sử dụng địa chỉ đích này để định tuyến gói qua Internet đến socket trong quá trình nhận. Khi gói đến ổ cắm nhận, quá trình nhận sẽ lấy gói qua ổ cắm, sau đó kiểm tra nội dung của gói và thực hiện hành động thích hợp.

Vì vậy, bây giờ bạn có thể đang thắc mắc, địa chỉ đích được đính kèm với gói dữ liệu là gì? Như bạn có thể mong đợi, địa chỉ IP của máy chủ đích là một phần của địa chỉ đích. Bằng cách bao gồm địa chỉ đích IP trong gói, các bộ định tuyến trên Internet sẽ có thể định tuyến gói qua Internet đến máy chủ đích. Nhưng vì một máy chủ có thể đang chạy nhiều tiến trình ứng dụng mạng, mỗi tiến trình có một hoặc nhiều ổ cắm, nên cũng cần phải xác định ổ cắm cụ thể trên máy chủ đích. Khi một socket được tạo ra, một mã định danh gọi là số cổng sẽ được gán cho nó. Vì vậy, như bạn mong đợi, địa chỉ đích của gói cũng bao gồm số cổng của ổ cắm. Tóm lại, quá trình gửi sẽ gắn vào gói một địa chỉ đích, bao gồm địa chỉ IP của máy chủ đích và số cổng của ổ cắm đích. Hơn nữa, như chúng ta sẽ sớm thấy, địa chỉ nguồn của người gửi---bao gồm

IP địa chỉ của máy chủ nguồn và số cổng của ổ cắm nguồn---cũng được đính kèm với gói. Tuy nhiên, việc đính kèm địa chỉ nguồn vào gói thường không được mã ứng dụng UDP thực hiện; thay vào đó nó được thực hiện tự động bởi hệ điều hành cơ bản.

Chúng ta sẽ sử dụng ứng dụng máy khách-máy chủ đơn giản sau đây để trình diễn cách lập trình socket cho cả UDP và TCP:

1\. Máy khách đọc một dòng ký tự (dữ liệu) từ bàn phím và gửi dữ liệu

đến máy chủ. 2. Máy chủ nhận dữ liệu và chuyển các ký tự thành chữ hoa. 3. Máy chủ gửi dữ liệu đã sửa đổi cho máy khách. 4. Máy khách nhận được dữ liệu đã sửa đổi và hiển thị dòng trên màn hình của nó.

Hình 2.27 nêu bật hoạt động chính liên quan đến socket của máy khách và máy chủ giao tiếp qua dịch vụ truyền tải UDP.

Tạo ổ cắm, cổng=x:

Máy chủ

serverSocket = socket(AF_INET,SOCK_DGRAM)

(Chạy trên serverIP)

Khách hàng

Đọc đoạn UDP từ

máy chủSocket

Viết trả lời

chỉ định địa chỉ khách hàng,

số cổng

máy chủSocket

Tạo datagram với serverIP

và cổng=x; gửi datagram qua

clientSocket

Tạo ổ cắm: clientSocket = socket(AF_INET,SOCK_DGRAM)

Đọc datagram từ

clientSocket

Đóng clientSocket

*Hình 2.27 ♦ Ứng dụng client-server sử dụng UDP*

Bây giờ chúng ta hãy bắt tay vào xem cặp chương trình máy khách-máy chủ để triển khai UDP của ứng dụng đơn giản này. Chúng tôi cũng cung cấp bản phân tích chi tiết, từng dòng sau mỗi chương trình. Chúng ta sẽ bắt đầu với ứng dụng khách UDP, ứng dụng này sẽ gửi một thông báo cấp ứng dụng đơn giản đến máy chủ. Để máy chủ có thể nhận và trả lời tin nhắn của máy khách, nó phải sẵn sàng và đang chạy---nghĩa là nó phải chạy như một tiến trình trước khi máy khách gửi tin nhắn của nó.

Chương trình máy khách được gọi là UDPClient.py và chương trình máy chủ được gọi là UDPServer.py. Để nhấn mạnh các vấn đề chính, chúng tôi cố tình cung cấp mã ở mức tối thiểu. "Code tốt" chắc chắn sẽ có thêm một vài dòng phụ trợ, đặc biệt là để xử lý các trường hợp lỗi. Đối với ứng dụng này, chúng tôi đã chọn tùy ý 12000 cho số cổng máy chủ.

UDPClient.py

Đây là mã cho phía máy khách của ứng dụng:

từ nhập socket \* serverName = \'hostname\' serverPort = 12000 clientSocket = socket(AF_INET, SOCK_DGRAM) message = input(\'Nhập câu viết thường:\') clientSocket.sendto(message.encode(),(serverName, serverPort)) modMessage, serverAddress = clientSocket.recvfrom(2048) print(modifiedMessage.decode()) clientSocket.close()

Bây giờ chúng ta hãy xem các dòng mã khác nhau trong UDPClient.py.

từ nhập ổ cắm \*

Mô-đun ổ cắm tạo thành nền tảng của tất cả các giao tiếp mạng trong Python. Bằng cách bao gồm dòng này, chúng tôi sẽ có thể tạo các ổ cắm trong chương trình của mình.

serverName = \'tên máy chủ\' serverPort = 12000

Dòng đầu tiên đặt biến serverName thành chuỗi 'tên máy chủ'. Ở đây, chúng tôi cung cấp một chuỗi chứa địa chỉ IP của máy chủ (ví dụ: "128.138.32.126") hoặc tên máy chủ của máy chủ (ví dụ: "cis.poly.edu"). Nếu chúng ta sử dụng tên máy chủ thì việc tra cứu DNS sẽ tự động được thực hiện để lấy địa chỉ IP.) Dòng thứ hai đặt biến số nguyên serverPort thành 12000.

clientSocket = socket(AF_INET, SOCK_DGRAM)

Dòng này tạo socket của máy khách, được gọi là clientSocket. Tham số đầu tiên cho biết họ địa chỉ; cụ thể là AF_INET cho biết mạng cơ bản đang sử dụng IPv4. (Đừng lo lắng về điều này ngay bây giờ---chúng ta sẽ thảo luận về IPv4 trong Chương 4.) Tham số thứ hai chỉ ra rằng ổ cắm thuộc loại SOCK_DGRAM, có nghĩa là nó là ổ cắm UDP (chứ không phải ổ cắm TCP). Lưu ý rằng chúng tôi không chỉ định số cổng của ổ cắm máy khách khi tạo nó; thay vào đó chúng tôi để hệ điều hành làm việc này cho chúng tôi. Bây giờ cửa của quy trình khách đã được tạo, chúng ta sẽ tạo một thông báo để gửi qua cửa.

message = input(\'Nhập câu viết thường:\')

input() là một hàm có sẵn trong Python. Khi lệnh này được thực thi, người dùng tại máy khách sẽ được nhắc với dòng chữ "Nhập câu viết thường:" Sau đó, người dùng sử dụng bàn phím để nhập một dòng, dòng này sẽ được đưa vào thông báo biến. Bây giờ chúng ta đã có một socket và một tin nhắn, chúng ta sẽ muốn gửi tin nhắn qua socket đến máy chủ đích.

clientSocket.sendto(message.encode(), (serverName, serverPort))

Trong dòng trên, trước tiên chúng ta chuyển đổi thông báo từ loại chuỗi sang loại byte, vì chúng ta cần gửi byte vào một ổ cắm; việc này được thực hiện bằng phương thức Encode(). Phương thức sendto() gắn địa chỉ đích (serverName, serverPort) vào tin nhắn và gửi gói kết quả vào socket của tiến trình, clientSocket. (Như đã đề cập trước đó, địa chỉ nguồn cũng được gắn vào gói, mặc dù việc này được thực hiện tự động chứ không phải rõ ràng bằng mã.) Gửi tin nhắn từ máy khách đến máy chủ qua ổ cắm UDP thật đơn giản! Sau khi gửi gói, client chờ nhận dữ liệu từ server.

đã sửa đổiMessage, serverAddress = clientSocket.recvfrom(2048)

Với dòng trên, khi một gói đến từ Internet tại ổ cắm của máy khách, dữ liệu của gói được đưa vào biến modMessage và địa chỉ nguồn của gói được đưa vào biến serverAddress. Biến serverAddress chứa cả địa chỉ IP của máy chủ và số cổng của máy chủ. Chương trình UDPClient thực sự không cần thông tin địa chỉ máy chủ này vì nó đã biết địa chỉ máy chủ ngay từ đầu; nhưng dòng Python này vẫn cung cấp địa chỉ máy chủ. Phương thức recvfrom cũng lấy kích thước bộ đệm 2048 làm đầu vào. (Kích thước bộ đệm này hoạt động cho hầu hết các mục đích.)

in(modifiedMessage.decode())

Dòng này in ra postedMessage trên màn hình của người dùng, sau khi chuyển đổi thông báo từ byte thành chuỗi. Nó phải là dòng ban đầu mà người dùng đã gõ, nhưng bây giờ được viết hoa.

clientSocket.close()

Dòng này đóng ổ cắm. Quá trình sau đó chấm dứt.

UDPServer.py

Bây giờ chúng ta hãy xem phía máy chủ của ứng dụng:

từ nhập ổ cắm \* serverPort = 12000 serverSocket = socket(AF_INET, SOCK_DGRAM) serverSocket.bind((\'\', serverPort)) print(\"Máy chủ đã sẵn sàng nhận\") trong khi True: tin nhắn, clientAddress = serverSocket.recvfrom(2048) đã sửa đổiMessage = message.decode().upper() serverSocket.sendto(modifiedMessage.encode(), clientAddress)

Lưu ý rằng phần đầu của UDPServer tương tự như UDPClient. Nó cũng nhập mô-đun ổ cắm, cũng đặt biến số nguyên serverPort thành 12000 và cũng tạo một ổ cắm loại SOCK_DGRAM (ổ cắm UDP). Dòng mã đầu tiên khác biệt đáng kể so với UDPClient là:

serverSocket.bind((\'\', serverPort))

Dòng trên liên kết (nghĩa là gán) số cổng 12000 cho ổ cắm của máy chủ. Do đó, trong UDPServer, mã (được viết bởi nhà phát triển ứng dụng) đang gán rõ ràng số cổng cho ổ cắm. Theo cách này, khi bất kỳ ai gửi gói đến cổng 12000 tại địa chỉ IP của máy chủ, gói đó sẽ được chuyển hướng đến ổ cắm này. UDPServer sau đó sẽ đi vào một vòng lặp while; vòng lặp while sẽ cho phép UDPServer nhận và xử lý các gói từ máy khách vô thời hạn. Trong vòng lặp while, UDPServer đợi gói tin đến.

tin nhắn, clientAddress = serverSocket.recvfrom(2048)

Dòng mã này tương tự như những gì chúng ta đã thấy trong UDPClient. Khi một gói đến socket của máy chủ, dữ liệu của gói sẽ được đưa vào thông báo có thể thay đổi và

địa chỉ nguồn của gói được đưa vào biến clientAddress. Biến clientAddress chứa cả địa chỉ IP của máy khách và số cổng của máy khách. Ở đây, UDPServer sẽ sử dụng thông tin địa chỉ này vì nó cung cấp địa chỉ trả lại, tương tự như địa chỉ trả lại với thư bưu điện thông thường. Với thông tin địa chỉ nguồn này, máy chủ hiện biết nơi cần gửi phản hồi của nó.

đã sửa đổiMessage = message.decode().upper()

Dòng này là trung tâm của ứng dụng đơn giản của chúng tôi. Nó lấy dòng được gửi bởi máy khách và sau khi chuyển đổi tin nhắn thành một chuỗi, nó sử dụng phương thức Upper() để viết hoa nó.

serverSocket.sendto(modifiedMessage.encode(), clientAddress)

Dòng cuối cùng này đính kèm địa chỉ của máy khách (địa chỉ IP và số cổng) vào thông báo viết hoa (sau khi chuyển đổi chuỗi thành byte) và gửi gói kết quả vào ổ cắm của máy chủ. (Như đã đề cập trước đó, địa chỉ máy chủ cũng được đính kèm với gói, mặc dù việc này được thực hiện tự động chứ không phải rõ ràng bằng mã.) Sau đó, Internet sẽ phân phối gói đến địa chỉ máy khách này. Sau khi máy chủ gửi gói, nó vẫn ở trong vòng lặp while, chờ gói UDP khác đến (từ bất kỳ máy khách nào đang chạy trên bất kỳ máy chủ nào).

Để kiểm tra cặp chương trình, bạn chạy UDPClient.py trên một máy chủ và UDPServer.py trên một máy chủ khác. Đảm bảo bao gồm tên máy chủ hoặc địa chỉ IP thích hợp của máy chủ trong UDPClient.py. Tiếp theo, bạn thực thi UDPServer.py, chương trình máy chủ đã biên dịch, trên máy chủ lưu trữ. Điều này tạo ra một quy trình trong máy chủ không hoạt động cho đến khi được một số khách hàng liên hệ. Sau đó, bạn thực thi UDPClient.py, chương trình máy khách đã biên dịch, trong máy khách. Điều này tạo ra một quá trình trong máy khách. Cuối cùng, để sử dụng ứng dụng ở máy khách, bạn nhập một câu theo sau là dấu xuống dòng.

Để phát triển ứng dụng máy khách-máy chủ UDP của riêng bạn, bạn có thể bắt đầu bằng cách sửa đổi một chút chương trình máy khách hoặc máy chủ. Ví dụ: thay vì chuyển đổi tất cả các chữ cái thành chữ hoa, máy chủ có thể đếm số lần chữ s xuất hiện và trả về số này. Hoặc bạn có thể sửa đổi client để sau khi nhận được câu viết hoa, người dùng có thể tiếp tục gửi thêm câu đến máy chủ.

**2.7.2 Socket Lập trình với TCP**

Không giống như UDP, TCP là giao thức hướng kết nối. Điều này có nghĩa là trước khi máy khách và máy chủ có thể bắt đầu gửi dữ liệu cho nhau, trước tiên chúng cần bắt tay và thiết lập kết nối TCP. Một đầu của kết nối TCP được gắn vào ổ cắm máy khách và đầu còn lại được gắn vào ổ cắm máy chủ. Khi tạo kết nối TCP, chúng tôi liên kết với nó địa chỉ ổ cắm máy khách (địa chỉ IP và số cổng) và địa chỉ ổ cắm máy chủ (địa chỉ IP và số cổng). Với kết nối TCP được thiết lập, khi một bên muốn gửi dữ liệu sang bên kia, nó chỉ cần hủy kết nối

dữ liệu vào kết nối TCP thông qua ổ cắm của nó. Điều này khác với UDP, trong đó máy chủ phải đính kèm địa chỉ đích vào gói trước khi thả nó vào ổ cắm.

Bây giờ chúng ta hãy xem xét kỹ hơn sự tương tác giữa các chương trình máy khách và máy chủ trong TCP. Máy khách có nhiệm vụ bắt đầu liên lạc với máy chủ. Để máy chủ có thể phản hồi với liên hệ ban đầu của khách hàng, máy chủ phải sẵn sàng. Điều này ngụ ý hai điều. Đầu tiên, như trong trường hợp UDP, máy chủ TCP phải chạy như một quy trình trước khi máy khách cố gắng bắt đầu liên hệ. Thứ hai, chương trình máy chủ phải có một cửa đặc biệt---chính xác hơn là một ổ cắm đặc biệt---chào đón một số liên hệ ban đầu từ một tiến trình máy khách đang chạy trên một máy chủ tùy ý. Sử dụng phép so sánh ngôi nhà/cánh cửa của chúng tôi cho một quy trình/ổ cắm, đôi khi chúng tôi sẽ coi lần liên hệ đầu tiên của khách hàng là "gõ cửa chào đón".

Khi quy trình máy chủ đang chạy, quy trình máy khách có thể bắt đầu kết nối TCP với máy chủ. Việc này được thực hiện trong chương trình máy khách bằng cách tạo một ổ cắm TCP. Khi máy khách tạo ổ cắm TCP của mình, nó sẽ chỉ định địa chỉ của ổ cắm chào mừng trong máy chủ, cụ thể là địa chỉ IP của máy chủ máy chủ và số cổng của ổ cắm. Sau khi tạo ổ cắm, máy khách bắt đầu bắt tay ba chiều và thiết lập kết nối TCP với máy chủ. Quá trình bắt tay ba chiều diễn ra trong lớp vận chuyển hoàn toàn vô hình đối với các chương trình máy khách và máy chủ.

Trong quá trình bắt tay ba chiều, quy trình máy khách sẽ gõ cửa chào đón quy trình máy chủ. Khi máy chủ "nghe thấy" tiếng gõ, nó sẽ tạo ra một cánh cửa mới---chính xác hơn là một ổ cắm mới dành riêng cho khách hàng cụ thể đó. Trong ví dụ bên dưới, cửa chào đón là một đối tượng ổ cắm TCP mà chúng tôi gọi là serverSocket; socket mới được tạo dành riêng cho máy khách thực hiện kết nối được gọi là ConnectionSocket. Những sinh viên gặp phải ổ cắm TCP lần đầu tiên đôi khi nhầm lẫn giữa ổ cắm chào mừng (là điểm liên hệ ban đầu của tất cả các máy khách muốn giao tiếp với máy chủ) và mỗi ổ cắm kết nối phía máy chủ mới được tạo sau đó để liên lạc với từng máy khách.

Từ góc độ của ứng dụng, ổ cắm của máy khách và ổ cắm kết nối của máy chủ được kết nối trực tiếp bằng một đường ống. Như được hiển thị trong Hình 2.28, quy trình máy khách có thể gửi các byte tùy ý vào ổ cắm của nó và TCP đảm bảo rằng quy trình máy chủ sẽ nhận được (thông qua ổ cắm kết nối) từng byte theo thứ tự được gửi. TCP do đó cung cấp dịch vụ đáng tin cậy giữa các quy trình máy khách và máy chủ. Hơn nữa, giống như mọi người có thể vào và ra cùng một cửa, tiến trình máy khách không chỉ gửi byte vào mà còn nhận byte từ ổ cắm của nó; tương tự, quy trình máy chủ không chỉ nhận byte mà còn gửi byte vào ổ cắm kết nối của nó.

Chúng tôi sử dụng cùng một ứng dụng máy khách-máy chủ đơn giản để trình diễn lập trình socket với TCP: Máy khách gửi một dòng dữ liệu đến máy chủ, máy chủ viết hoa dòng đó và gửi lại cho máy khách. Hình 2.29 nêu bật hoạt động chính liên quan đến socket của máy khách và máy chủ giao tiếp qua dịch vụ truyền tải TCP.

TCPClient.py

Đây là mã cho phía máy khách của ứng dụng:

từ nhập ổ cắm \* serverName = \'servername\' serverPort = 12000 clientSocket = socket(AF_INET, SOCK_STREAM) clientSocket.connect((serverName,serverPort)) question = input(\'Nhập câu chữ thường:\') clientSocket.send(sentence.encode()) modSentence = clientSocket.recv(1024) print(\'Từ máy chủ: \', đã sửa đổiSentence.decode())  clientSocket.close()

Bây giờ chúng ta hãy xem xét các dòng khác nhau trong mã có sự khác biệt đáng kể so với cách triển khai UDP. Dòng đầu tiên như vậy là tạo ổ cắm máy khách.

clientSocket = socket(AF_INET, SOCK_STREAM)

Dòng này tạo socket của máy khách, được gọi là clientSocket. Tham số đầu tiên lại chỉ ra rằng mạng cơ bản đang sử dụng IPv4. Tham số thứ hai

Tiến trình máy khách Tiến trình máy chủ

Ổ cắm máy khách

Ổ cắm chào mừng

Cái bắt tay ba chiều

Byte byte ổ cắm kết nối

*Hình 2.28 ♦ Tiến trình TCPServer có hai socket*

cho biết ổ cắm thuộc loại SOCK_STREAM, có nghĩa là ổ cắm đó là ổ cắm TCP (chứ không phải ổ cắm UDP). Lưu ý rằng chúng tôi lại không chỉ định số cổng của ổ cắm máy khách khi tạo nó; thay vào đó chúng tôi để hệ điều hành làm việc này cho chúng tôi. Bây giờ dòng mã tiếp theo rất khác so với những gì chúng ta thấy trong UDPClient:

clientSocket.connect((serverName,serverPort))

Hãy nhớ lại rằng trước khi máy khách có thể gửi dữ liệu đến máy chủ (hoặc ngược lại) bằng ổ cắm TCP, kết nối TCP trước tiên phải được thiết lập giữa máy khách và máy chủ. các

Đóng kết nốiSocket

Viết trả lời cho ConnectionSocket

Đọc yêu cầu từ ConnectionSocket

Tạo ổ cắm, port=x,

cho yêu cầu đến:

Máy chủ

máy chủSocket =

ổ cắm()

Đợi yêu cầu kết nối đến: ConnectionSocket = serverSocket.accept()

(Chạy trên serverIP)

Khách hàng

TCP thiết lập kết nối Tạo socket, kết nối

tới serverIP, cổng=x:

clientSocket =

ổ cắm()

Đọc trả lời từ

clientSocket

Gửi yêu cầu bằng cách sử dụng

clientSocket

Đóng clientSocket

*Hình 2.29 ♦ Ứng dụng client-server sử dụng TCP*

dòng trên bắt đầu kết nối TCP giữa máy khách và máy chủ. Tham số của phương thức connect() là địa chỉ phía máy chủ của kết nối. Sau khi dòng mã này được thực thi, quá trình bắt tay ba chiều được thực hiện và kết nối TCP được thiết lập giữa máy khách và máy chủ.

câu = input(\'Nhập câu viết thường:\')

Giống như UDPClient, phần trên nhận được một câu từ người dùng. Câu chuỗi tiếp tục thu thập các ký tự cho đến khi người dùng kết thúc dòng bằng cách gõ dấu xuống dòng. Dòng mã tiếp theo cũng rất khác so với UDPClient:

clientSocket.send(sentence.encode())

Dòng trên gửi câu qua socket của máy khách và vào kết nối TCP. Lưu ý rằng chương trình không tạo gói một cách rõ ràng và đính kèm địa chỉ đích vào gói, như trường hợp với ổ cắm UDP. Thay vào đó, chương trình máy khách chỉ cần thả các byte trong câu chuỗi vào kết nối TCP. Sau đó, máy khách sẽ chờ nhận byte từ máy chủ.

đã sửa đổiSentence = clientSocket.recv(2048)

Khi các ký tự đến từ máy chủ, chúng sẽ được đặt vào chuỗi đã sửa đổi. Các ký tự tiếp tục tích lũy trong câu đã sửa đổi cho đến khi dòng kết thúc bằng ký tự trả về đầu dòng. Sau khi in câu viết hoa, chúng ta đóng socket của client:

clientSocket.close()

Dòng cuối cùng này đóng ổ cắm và do đó, đóng kết nối TCP giữa máy khách và máy chủ. Nó khiến TCP trong máy khách gửi tin nhắn TCP tới TCP trên máy chủ (xem Phần 3.5).

TCPServer.py

Bây giờ chúng ta hãy xem chương trình máy chủ.

từ nhập ổ cắm \* serverPort = 12000 serverSocket = socket(AF_INET,SOCK_STREAM) serverSocket.bind((\'\',serverPort)) serverSocket.listen(1) print(\'Máy chủ đã sẵn sàng nhận\')

trong khi Đúng: ConnectionSocket, addr = serverSocket.accept() câu = ConnectionSocket.recv(1024).decode() viết hoaSentence = câu.upper() ConnectionSocket.send(capitalizedSentence.encode())  ConnectionSocket.close()

Bây giờ chúng ta hãy xem các dòng khác biệt đáng kể so với UDPServer và TCPClient. Giống như TCPClient, máy chủ tạo ổ cắm TCP với:

serverSocket=socket(AF_INET,SOCK_STREAM)

Tương tự như UDPServer, chúng tôi liên kết số cổng máy chủ, serverPort, với ổ cắm này:

serverSocket.bind((\'\',serverPort))

Nhưng với TCP, serverSocket sẽ là ổ cắm chào đón của chúng tôi. Sau khi thiết lập cánh cửa chào đón này, chúng ta sẽ đợi và lắng nghe một số khách hàng gõ cửa:

serverSocket.listen(1)

Dòng này yêu cầu máy chủ lắng nghe các yêu cầu kết nối TCP từ máy khách. Tham số chỉ định số lượng kết nối được xếp hàng tối đa (ít nhất là 1).

ConnectionSocket, addr = serverSocket.accept()

Khi một máy khách gõ cửa này, chương trình sẽ gọi phương thức Accept() cho serverSocket, phương thức này tạo ra một ổ cắm mới trong máy chủ, được gọi là ConnectionSocket, dành riêng cho máy khách cụ thể này. Sau đó, máy khách và máy chủ hoàn tất quá trình bắt tay, tạo kết nối TCP giữa clientSocket của máy khách và ConnectionSocket của máy chủ. Khi kết nối TCP được thiết lập, máy khách và máy chủ hiện có thể gửi byte cho nhau qua kết nối. Với TCP, tất cả byte được gửi từ một bên chỉ được đảm bảo đến được bên kia nhưng cũng được đảm bảo đến theo thứ tự.

ConnectionSocket.close()

Trong chương trình này, sau khi gửi câu đã sửa đổi cho máy khách, chúng ta đóng socket kết nối. Nhưng vì serverSocket vẫn mở nên giờ đây một máy khách khác có thể gõ cửa và gửi cho máy chủ một câu để sửa đổi.

Điều này hoàn thành cuộc thảo luận của chúng ta về lập trình socket trong TCP. Bạn được khuyến khích chạy hai chương trình trên hai máy chủ riêng biệt và cũng có thể sửa đổi chúng để đạt được các mục tiêu hơi khác nhau. Bạn nên so sánh cặp chương trình UDP với cặp chương trình TCP và xem chúng khác nhau như thế nào. Bạn cũng nên thực hiện nhiều bài tập lập trình socket được mô tả ở cuối Chương 2, 4 và 9. Cuối cùng, chúng tôi hy vọng một ngày nào đó, sau khi thành thạo các chương trình socket này và các chương trình socket nâng cao hơn, bạn sẽ viết được ứng dụng mạng phổ biến của riêng mình, trở nên rất giàu có và nổi tiếng, đồng thời ghi nhớ các tác giả của cuốn sách giáo khoa này!

**2.8 Tóm tắt**

Trong chương này, chúng ta đã nghiên cứu các khía cạnh khái niệm và triển khai của các ứng dụng mạng. Chúng ta đã tìm hiểu về kiến ​​trúc máy khách-máy chủ phổ biến được nhiều ứng dụng Internet áp dụng và thấy việc sử dụng nó trong các giao thức HTTP, SMTP và DNS. Chúng tôi đã nghiên cứu một số chi tiết về các giao thức cấp ứng dụng quan trọng này và các ứng dụng liên quan tương ứng của chúng (Web, truyền tệp, e-mail và DNS). Chúng ta đã tìm hiểu về kiến ​​trúc P2P và đối chiếu nó với kiến ​​trúc máy khách-máy chủ. Chúng tôi cũng đã tìm hiểu về cách truyền phát video và cách các hệ thống phân phối video hiện đại tận dụng CDN. Chúng tôi đã kiểm tra cách sử dụng API socket để xây dựng các ứng dụng mạng. Chúng ta đã hướng dẫn cách sử dụng ổ cắm cho các dịch vụ truyền tải từ đầu đến cuối hướng kết nối (TCP) và không kết nối (UDP). Bước đầu tiên trong hành trình tìm hiểu kiến ​​trúc mạng phân lớp của chúng ta hiện đã hoàn tất!

Ở phần đầu của cuốn sách này, trong Phần 1.1, chúng tôi đã đưa ra một định nghĩa khá mơ hồ, cơ bản về một giao thức: "định dạng và thứ tự của các tin nhắn được trao đổi giữa hai hoặc nhiều thực thể giao tiếp, cũng như các hành động được thực hiện khi truyền và/hoặc nhận một tin nhắn hoặc sự kiện khác". Tài liệu trong chương này và đặc biệt là nghiên cứu chi tiết của chúng tôi về các giao thức HTTP, SMTP và DNS, hiện đã bổ sung thêm nội dung đáng kể cho định nghĩa này. Giao thức là một khái niệm quan trọng trong mạng; nghiên cứu của chúng tôi về các giao thức ứng dụng giờ đây đã cho chúng tôi cơ hội phát triển cảm nhận trực quan hơn về nội dung của các giao thức.

Trong Phần 2.1, chúng tôi đã mô tả các mô hình dịch vụ mà TCP và UDP cung cấp cho các ứng dụng gọi chúng. Chúng tôi thậm chí còn xem xét kỹ hơn các mô hình dịch vụ này khi phát triển các ứng dụng đơn giản chạy trên TCP và UDP trong Phần 2.7. Tuy nhiên, chúng tôi đã nói rất ít về cách TCP và UDP cung cấp các mô hình dịch vụ này. Ví dụ: chúng tôi biết rằng TCP cung cấp dịch vụ dữ liệu đáng tin cậy nhưng chúng tôi chưa cho biết nó thực hiện điều đó như thế nào. Trong chương tiếp theo, chúng ta sẽ xem xét cẩn thận không chỉ cái gì mà còn cả cách thức và lý do của các giao thức truyền tải.

Được trang bị kiến ​​thức về cấu trúc ứng dụng Internet và các giao thức cấp độ ứng dụng, giờ đây chúng ta đã sẵn sàng đi sâu hơn vào ngăn xếp giao thức và kiểm tra lớp truyền tải trong Chương 3.

**Bài tập về nhà vấn đề và câu hỏi**

Câu hỏi ôn tập chương 2

MỤC 2.1 R1. Liệt kê năm ứng dụng Internet không độc quyền và giao thức lớp ứng dụng

cols mà họ sử dụng. R2. Sự khác biệt giữa kiến ​​trúc mạng và kiến ​​trúc ứng dụng là gì? R3. Đối với một phiên giao tiếp giữa một cặp tiến trình, tiến trình nào được

máy khách và máy chủ là gì? R4. Đối với ứng dụng chia sẻ tệp P2P, bạn có đồng ý với nhận định, "Không có

khái niệm về phía máy khách và máy chủ của một phiên giao tiếp\"? Tại sao có hoặc tại sao không? R5. Thông tin nào được sử dụng bởi một tiến trình chạy trên một máy chủ để xác định một máy chủ chuyên nghiệp?

ngừng chạy trên máy chủ khác? R6. Giả sử bạn muốn thực hiện một giao dịch từ máy khách ở xa tới máy chủ như

nhanh nhất có thể. Bạn sẽ sử dụng UDP hay TCP? Tại sao? R7. Tham khảo Hình 2.4, chúng ta thấy rằng không có ứng dụng nào được liệt kê trong Hình

2.4 yêu cầu cả việc không mất dữ liệu và thời gian. Bạn có thể hình dung ra một ứng dụng không yêu cầu mất dữ liệu và cũng rất nhạy cảm với thời gian không? R8. Liệt kê bốn loại dịch vụ rộng rãi mà một giao thức truyền tải có thể cung cấp.

Đối với mỗi loại dịch vụ, hãy cho biết liệu UDP hoặc TCP (hoặc cả hai) có cung cấp dịch vụ như vậy hay không. R9. Hãy nhớ lại rằng TCP có thể được nâng cao bằng TLS để cung cấp quy trình này đến quy trình khác

dịch vụ bảo mật, bao gồm cả mã hóa. TLS hoạt động ở lớp vận chuyển hay lớp ứng dụng? Nếu nhà phát triển ứng dụng muốn TCP được nâng cao bằng TLS thì nhà phát triển phải làm gì?

PHẦN 2.2--2.5 R10. Giao thức bắt tay có ý nghĩa gì? R11. Tại sao HTTP, SMTP và IMAP chạy trên TCP thay vì trên UDP? R12. Hãy xem xét một trang web thương mại điện tử muốn lưu giữ hồ sơ mua hàng cho mỗi

khách hàng của nó. Mô tả cách thực hiện điều này với cookie.

R13. Mô tả cách bộ nhớ đệm Web có thể giảm độ trễ trong việc nhận yêu cầu

sự vật. Bộ nhớ đệm web sẽ giảm độ trễ cho tất cả các đối tượng được người dùng yêu cầu hay chỉ cho một số đối tượng? Tại sao? R14. Telnet vào máy chủ Web và gửi tin nhắn yêu cầu nhiều dòng. Bao gồm trong

thông báo yêu cầu dòng tiêu đề If-modified-since: để buộc thông báo phản hồi có mã trạng thái 304 Not Modified. R15. Liệt kê một số ứng dụng nhắn tin phổ biến. Họ có sử dụng các giao thức giống như SMS không?

VẤN ĐỀ VÀ CÂU HỎI BÀI TẬP 167

R16. Giả sử Alice, với một tài khoản e-mail trên nền Web (chẳng hạn như Hotmail hoặc Gmail),

gửi tin nhắn cho Bob, người truy cập thư từ máy chủ thư của anh ấy bằng IMAP. Thảo luận về cách truyền tin nhắn từ máy chủ của Alice đến máy chủ của Bob. Hãy chắc chắn liệt kê một loạt các giao thức lớp ứng dụng được sử dụng để di chuyển thông điệp giữa hai máy chủ. R17. In ra tiêu đề của email bạn vừa nhận được. Làm sao

nhiều Đã nhận: có dòng tiêu đề nào không? Phân tích từng dòng tiêu đề trong tin nhắn. R18. Sự cố chặn HOL trong HTTP/1.1 là gì? HTTP/2 cố gắng như thế nào

giải quyết nó? R19. Máy chủ Web và máy chủ thư của một tổ chức có thể có

chính xác cùng một bí danh cho tên máy chủ (ví dụ: foo.com)? Loại RR chứa tên máy chủ của máy chủ thư sẽ là loại gì? R20. Xem qua các email bạn đã nhận và kiểm tra tiêu đề của thư đã gửi

từ người dùng có địa chỉ email .edu. Có thể xác định từ tiêu đề địa chỉ IP của máy chủ mà tin nhắn được gửi đi không? Thực hiện tương tự với thư được gửi từ tài khoản Gmail.

MỤC 2.5 R21. Trong BitTorrent, giả sử Alice cung cấp các đoạn cho Bob trong suốt 30 giây

khoảng thời gian. Liệu Bob có nhất thiết phải trả ơn và cung cấp các phần cho Alice trong cùng khoảng thời gian này không? Tại sao hoặc tại sao không? R22. Hãy xem xét một Alice ngang hàng mới tham gia BitTorrent mà không sở hữu bất kỳ khối nào.

Nếu không có bất kỳ phần nào, cô ấy không thể trở thành người tải lên top 4 cho bất kỳ đồng nghiệp nào khác, vì cô ấy không có gì để tải lên. Vậy thì làm thế nào Alice có được miếng đầu tiên? R23. Mạng lớp phủ là gì? Nó có bao gồm các bộ định tuyến không? Các cạnh trong là gì

mạng lớp phủ?

MỤC 2.6 R24. CDN thường áp dụng một trong hai triết lý bố trí máy chủ khác nhau.

Kể tên và mô tả ngắn gọn chúng. R25. Bên cạnh những cân nhắc liên quan đến mạng như độ trễ, mất mát và băng thông

hiệu suất, còn có những yếu tố quan trọng khác ảnh hưởng đến việc thiết kế chiến lược lựa chọn máy chủ CDN. Họ là gì?

MỤC 2.7 R26. Trong Phần 2.7, máy chủ UDP được mô tả chỉ cần một ổ cắm, trong khi

máy chủ TCP cần có hai ổ cắm. Tại sao? Nếu máy chủ TCP hỗ trợ n kết nối đồng thời, mỗi kết nối từ một máy chủ khách khác nhau, thì máy chủ TCP sẽ cần bao nhiêu ổ cắm?

R27. Đối với ứng dụng máy khách-máy chủ trên TCP được mô tả trong Phần 2.7, tại sao

chương trình máy chủ có phải được thực thi trước chương trình máy khách không? Đối với ứng dụng máy khách-máy chủ trên UDP, tại sao chương trình máy khách có thể được thực thi trước chương trình máy chủ?

**Vấn đề**

P1. Đúng hay sai?

Một. Người dùng yêu cầu một trang Web bao gồm một số văn bản và ba hình ảnh.

Đối với trang này, khách hàng sẽ gửi một tin nhắn yêu cầu và nhận bốn tin nhắn phản hồi. b. Hai trang Web riêng biệt (ví dụ: www.mit.edu/research

.html và www.mit.edu/students.html) có thể được gửi qua cùng một kết nối liên tục. c. Với các kết nối không liên tục giữa trình duyệt và máy chủ gốc, đó là

có thể để một phân đoạn TCP mang hai thông báo yêu cầu HTTP riêng biệt. d. Tiêu đề Ngày: trong thông báo phản hồi HTTP cho biết thời điểm

đối tượng trong phản hồi được sửa đổi lần cuối. đ. HTTP tin nhắn phản hồi không bao giờ có nội dung tin nhắn trống. P2. SMS, iMessage, Wechat và WhatsApp đều là các tin nhắn thời gian thực trên điện thoại thông minh.

hệ thống hiền triết. Sau khi thực hiện một số nghiên cứu trên Internet, đối với mỗi hệ thống này hãy viết một đoạn văn về các giao thức mà chúng sử dụng. Sau đó viết một đoạn văn giải thích chúng khác nhau như thế nào. P3. Hãy xem xét một khách hàng HTTP muốn truy xuất một tài liệu Web tại một thời điểm nhất định

URL. Địa chỉ IP của máy chủ HTTP ban đầu không xác định. Những giao thức lớp vận chuyển và ứng dụng nào ngoài HTTP là cần thiết trong kịch bản này? P4. Hãy xem xét chuỗi ký tự ASCII sau đây được ghi lại bởi

Wireshark khi trình duyệt gửi tin nhắn HTTP GET (tức là đây là nội dung thực tế của tin nhắn HTTP GET). Các ký tự \<cr\>\<lf\> là các ký tự xuống dòng và ký tự xuống dòng (nghĩa là chuỗi ký tự in nghiêng \<cr\> trong văn bản bên dưới biểu thị một ký tự xuống dòng duy nhất được chứa tại thời điểm đó trong tiêu đề HTTP). Trả lời các câu hỏi sau, cho biết bạn tìm thấy câu trả lời ở đâu trong thông báo HTTP GET bên dưới.

GET /cs453/index.html HTTP/1.1\<cr\>\<lf\>Host: gai a.cs.umass.edu\<cr\>\<lf\>User-Agent: Mozilla/5.0 ( Windows;U; Windows NT 5.1; en-US; rv:1.7.2) Gec ko/20040804 Netscape/7.2 (ax) \<cr\>\<lf\>Chấp nhận:ex t/xml, application/xml, application/xhtml+xml, text /html;q=0.9, text/plain;q=0.8,image/png,\*/\*;q=0.5

VẤN ĐỀ 169

\<cr\>\<lf\>Ngôn ngữ chấp nhận: en-us,en;q=0.5\<cr\>\<lf\>AcceptEncoding: zip,deflate\<cr\>\<lf\>Bộ ký tự chấp nhận: ISO -8859-1,utf-8;q=0.7,\*;q=0.7\<cr\>\<lf\>Keep-Alive: 300\<cr\> \<lf\>Kết nối:keep-alive\<cr\>\<lf\>\<cr\>\<lf\>

Một. URL của tài liệu được trình duyệt yêu cầu là gì? b. Trình duyệt đang chạy phiên bản HTTP nào? c. Trình duyệt có yêu cầu kết nối không liên tục hay liên tục không? d. Địa chỉ IP của máy chủ lưu trữ mà trình duyệt đang chạy là gì? đ. Loại trình duyệt nào khởi tạo thông báo này? Tại sao loại trình duyệt

cần thiết trong thông báo yêu cầu HTTP? P5. Văn bản bên dưới hiển thị câu trả lời được gửi từ máy chủ để đáp lại HTTP

NHẬN tin nhắn trong câu hỏi trên. Trả lời các câu hỏi sau, cho biết bạn tìm thấy câu trả lời ở đâu trong thông báo bên dưới.

HTTP/1.1 200 OK\<cr\>\<lf\>Ngày: Thứ ba, 07 tháng 3 năm 2008 12:39:45GMT\<cr\>\<lf\>Máy chủ: Apache/2.0.52 (Fedora) \<cr\>\<lf\>Sửa đổi lần cuối: Thứ bảy, ngày 10 tháng 12 năm 2005 18:27:46 GMT\<cr\>\<lf\>ETag: "526c3-f22-a88a4c80"\<cr\>\<lf\>Phạm vi chấp nhận: byte\<cr\>\<lf\>Độ dài nội dung: 3874\<cr\>\<lf\> Keep-Alive: timeout=max=100\<cr\>\<lf\>Kết nối: Keep-Alive\<cr\>\<lf\>Loại nội dung: text/html; charset= ISO-8859-1\<cr\>\<lf\>\<cr\>\<lf\>\<!doctype html public "- //w3c//dtd html 4.0transitional//en"\>\<lf\>\<html\>\<lf\> \<head\>\<lf\> \<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"\>\<lf\> \<meta name="GENERATOR" content="Mozilla/4.79 \[en\] (Windows NT 5.0; U) Netscape\]"\>\<lf\> \<title\>CMPSCI 453 / 591 / NTU-ST550ASpring 2005 trang chủ\</title\>\<lf\>\</head\>\<lf\> \<nhiều văn bản tài liệu khác ở đây (không hiển thị)\>

Một. Máy chủ có thể tìm thấy tài liệu thành công hay không? Mấy giờ

câu trả lời tài liệu có được cung cấp không? b. Tài liệu được sửa đổi lần cuối khi nào? c. Có bao nhiêu byte trong tài liệu được trả về? d. 5 byte đầu tiên của tài liệu được trả về là gì? Có phải máy chủ

đồng ý với một kết nối liên tục? P6. Lấy thông số kỹ thuật HTTP/1.1 (RFC 2616). Trả lời như sau

câu hỏi: a. Giải thích cơ chế được sử dụng để truyền tín hiệu giữa máy khách và máy chủ

để chỉ ra rằng một kết nối liên tục đang bị đóng. Máy khách, máy chủ hoặc cả hai có thể báo hiệu việc đóng kết nối không?

b\. HTTP cung cấp những dịch vụ mã hóa nào? c. Một khách hàng có thể mở ba hoặc nhiều kết nối đồng thời với một địa chỉ nhất định không?

máy chủ? d. Máy chủ hoặc máy khách có thể đóng kết nối truyền tải giữa chúng

nếu một trong hai phát hiện kết nối đã không hoạt động trong một thời gian. Có thể một bên bắt đầu đóng kết nối trong khi bên kia đang truyền dữ liệu qua kết nối này? Giải thích. P7. Giả sử trong trình duyệt Web của bạn, bạn nhấp vào một liên kết để nhận được một trang Web.

Địa chỉ IP cho URL được liên kết không được lưu vào bộ nhớ đệm trong máy chủ lưu trữ cục bộ của bạn, vì vậy cần phải tra cứu DNS để lấy địa chỉ IP. Giả sử rằng n máy chủ DNS được truy cập trước khi máy chủ của bạn nhận được địa chỉ IP từ DNS; các lượt truy cập liên tiếp phải chịu RTT RTT1, . . . , RTTn. Hơn nữa, giả sử rằng trang Web được liên kết với liên kết chứa chính xác một đối tượng, bao gồm một lượng nhỏ văn bản HTML. Đặt RTT0 biểu thị RTT giữa máy chủ cục bộ và máy chủ chứa đối tượng. Giả sử thời gian truyền đối tượng bằng 0, thời gian trôi qua bao lâu kể từ khi máy khách nhấp vào liên kết cho đến khi máy khách nhận được đối tượng? P8. Tham khảo Bài toán P7, giả sử tệp HTML tham chiếu tới 8 tệp rất nhỏ

các đối tượng trên cùng một máy chủ. Bỏ qua thời gian truyền, thời gian trôi qua với a. HTTP không liên tục không có kết nối TCP song song? b. Không liên tục HTTP với trình duyệt được định cấu hình song song cho 6

kết nối? c. Kiên trì HTTP? P9. Hãy xem Hình 2.12, trong đó có một mạng lưới tổ chức được kết nối với

Internet. Giả sử kích thước đối tượng trung bình là 1.000.000 bit và tốc độ yêu cầu trung bình từ trình duyệt của tổ chức đến máy chủ gốc là 16 yêu cầu mỗi giây. Ngoài ra, giả sử rằng khoảng thời gian cần thiết kể từ khi bộ định tuyến ở phía Internet của liên kết truy cập chuyển tiếp yêu cầu HTTP cho đến khi nhận được phản hồi trung bình là ba giây (xem Phần 2.2.5). Lập mô hình tổng thời gian phản hồi trung bình là tổng của độ trễ truy cập trung bình (nghĩa là độ trễ từ bộ định tuyến Internet đến bộ định tuyến của tổ chức) và độ trễ Internet trung bình. Đối với độ trễ truy cập trung bình, sử dụng ∆/(1 - ∆b), trong đó ∆ là thời gian trung bình cần thiết để gửi một đối tượng qua liên kết truy cập và b là tốc độ đến của các đối tượng đến liên kết truy cập. Một. Tìm tổng thời gian phản hồi trung bình. b. Bây giờ giả sử bộ đệm được cài đặt trong mạng LAN của tổ chức. Giả sử

tỷ lệ trượt là 0,4. Tìm tổng thời gian phản hồi. P10. Hãy xem xét một liên kết ngắn, dài 10 mét, qua đó người gửi có thể truyền với tốc độ

150 bit/giây theo cả hai hướng. Giả sử các gói chứa dữ liệu dài 100.000 bit và các gói chỉ chứa điều khiển (ví dụ: ACK hoặc

VẤN ĐỀ 171

bắt tay) dài 200 bit. Giả sử rằng mỗi kết nối song song có N kết nối nhận được 1/N băng thông liên kết. Bây giờ hãy xem xét giao thức HTTP và giả sử rằng mỗi đối tượng được tải xuống có độ dài 100 Kbit và đối tượng được tải xuống ban đầu chứa 10 đối tượng được tham chiếu từ cùng một người gửi. Liệu việc tải xuống song song thông qua các phiên bản song song của HTTP không liên tục có hợp lý trong trường hợp này không? Bây giờ hãy xem xét HTTP liên tục. Bạn có mong đợi lợi ích đáng kể so với trường hợp không liên tục không? Biện minh và giải thích câu trả lời của bạn. P11. Hãy xem xét kịch bản được giới thiệu trong bài toán trước. Bây giờ giả sử rằng

liên kết được Bob chia sẻ với bốn người dùng khác. Bob sử dụng các phiên bản song song của HTTP không liên tục và bốn người dùng còn lại sử dụng HTTP không liên tục mà không tải xuống song song. Một. Các kết nối song song của Bob có giúp anh ấy truy cập các trang Web nhanh hơn không?

Tại sao hoặc tại sao không? b. Nếu tất cả năm người dùng mở năm phiên bản song song của HTTP không liên tục, thì

liệu các kết nối song song của Bob có còn mang lại lợi ích không? Tại sao hoặc tại sao không? P12. Viết một chương trình TCP đơn giản cho một máy chủ chấp nhận các dòng đầu vào từ một máy chủ

ent và in các dòng này lên đầu ra tiêu chuẩn của máy chủ. (Bạn có thể thực hiện việc này bằng cách sửa đổi chương trình TCPServer.py trong văn bản.) Biên dịch và thực thi chương trình của bạn. Trên bất kỳ máy nào khác có trình duyệt Web, hãy đặt máy chủ proxy trong trình duyệt thành máy chủ đang chạy chương trình máy chủ của bạn; cũng cấu hình số cổng một cách thích hợp. Trình duyệt của bạn bây giờ sẽ gửi thông báo yêu cầu GET đến máy chủ của bạn và máy chủ của bạn sẽ hiển thị thông báo trên đầu ra tiêu chuẩn của nó. Sử dụng nền tảng này để xác định xem trình duyệt của bạn có tạo thông báo GET có điều kiện cho các đối tượng được lưu vào bộ nhớ đệm cục bộ hay không. P13. Hãy cân nhắc việc gửi qua HTTP/2 một trang Web bao gồm một video clip,

và năm hình ảnh. Giả sử video clip được truyền dưới dạng 2000 khung hình và mỗi hình ảnh có ba khung hình. Một. Nếu tất cả các khung hình video được gửi trước mà không xen kẽ thì có bao nhiêu khung hình

Cần có "thời gian khung hình" cho đến khi tất cả năm hình ảnh được gửi? b. Nếu các khung được xen kẽ thì cần bao nhiêu thời gian khung cho đến khi cả năm khung

hình ảnh được gửi đi. P14. Hãy xem xét trang Web trong bài toán 13. Bây giờ mức độ ưu tiên HTTP/2 là

được tuyển dụng. Giả sử tất cả các hình ảnh được ưu tiên hơn video clip và hình ảnh đầu tiên được ưu tiên hơn hình ảnh thứ hai, hình ảnh thứ hai được ưu tiên hơn hình ảnh thứ ba, v.v. Cần bao nhiêu thời gian khung hình cho đến khi hình ảnh thứ hai được gửi? P15. Sự khác biệt giữa THƯ TỪ: trong SMTP và Từ: trong

chính tin nhắn thư? P16. SMTP đánh dấu phần cuối của nội dung thư như thế nào? Thế còn HTTP thì sao? Có thể

HTTP sử dụng phương pháp tương tự như SMTP để đánh dấu phần cuối của nội dung thư? Giải thích.

P17. Đọc RFC 5321 cho SMTP. MTA có nghĩa là gì? Hãy xem xét những điều sau-

nhận được e-mail spam (được sửa đổi từ một e-mail spam thực sự). Giả sử chỉ có người tạo ra e-mail spam này là độc hại và tất cả các máy chủ khác đều trung thực, hãy xác định máy chủ độc hại đã tạo ra e-mail spam này.

Từ - Thứ Sáu, 07 tháng 11 13:41:30 2008 Đường dẫn trả về: \<tennis5@pp33head.com\> Đã nhận: từ barmail.cs.umass.edu (barmail.cs.umass.edu \[128.119.240.3\]) bởi cs.umass.edu (8.13.1/8.12.6) cho \<hg@cs.umass.edu\>; Thứ Sáu, ngày 7 tháng 11 năm 2008 13:27:10 -0500 Đã nhận: từ asusus-4b96 (localhost \[127.0.0.1\]) bởi barmail.cs.umass.edu (Tường lửa thư rác) cho \<hg@cs.umass. edu\>; Thứ Sáu, ngày 7 tháng 11 năm 2008 13:27:07 -0500 (EST) Đã nhận: từ asusus-4b96 (\[58.88.21.177\]) qua barmail. cs.umass.edu cho \<hg@cs.umass.edu\>; Thứ sáu, 07 tháng 11 năm 2008 13:27:07 -0500 (EST) Đã nhận: từ \[58.88.21.177\] bởi inbnd55.exchangeddd. com; Thứ bảy, 8 tháng 11 năm 2008 01:27:07 +0700 Từ: "Jonny" \<tennis5@pp33head.com\> Đến: \<hg@cs.umass.edu\> Chủ đề: Cách đảm bảo khoản tiết kiệm của bạn

P18. Một. Cơ sở dữ liệu whois là gì?

b\. Sử dụng nhiều cơ sở dữ liệu whois khác nhau trên Internet để lấy tên của hai

DNS máy chủ. Cho biết cơ sở dữ liệu whois nào bạn đã sử dụng. c. Sử dụng nslookup trên máy chủ cục bộ của bạn để gửi DNS truy vấn tới ba DNS

máy chủ: máy chủ DNS cục bộ của bạn và hai máy chủ DNS bạn đã tìm thấy ở phần (b). Hãy thử truy vấn các báo cáo Loại A, NS và MX. Tóm tắt những phát hiện của bạn. d. Sử dụng nslookup để tìm máy chủ Web có nhiều địa chỉ IP. Làm

máy chủ Web của cơ quan bạn (trường học hoặc công ty) có nhiều địa chỉ IP? đ. Sử dụng cơ sở dữ liệu whois ARIN để xác định dải địa chỉ IP được sử dụng bởi

trường đại học của bạn. f. Mô tả cách kẻ tấn công có thể sử dụng cơ sở dữ liệu whois và công cụ nslookup

để thực hiện trinh sát một tổ chức trước khi phát động một cuộc tấn công. g. Thảo luận tại sao cơ sở dữ liệu whois nên được công khai.

VẤN ĐỀ 173

P19. Trong bài toán này, chúng tôi sử dụng công cụ đào hữu ích có sẵn trên các máy chủ Unix và Linux để

khám phá hệ thống phân cấp của máy chủ DNS. Hãy nhớ lại rằng trong Hình 2.19, máy chủ DNS trong hệ thống phân cấp DNS ủy quyền một truy vấn DNS cho máy chủ DNS thấp hơn trong hệ thống phân cấp, bằng cách gửi lại cho máy khách DNS tên của máy chủ DNS cấp thấp hơn đó. Đầu tiên hãy đọc trang man để đào, sau đó trả lời các câu hỏi sau. Một. Bắt đầu với máy chủ DNS gốc (từ một trong các máy chủ gốc \[a-m\].

root-servers.net), hãy bắt đầu một chuỗi truy vấn cho địa chỉ IP cho máy chủ Web của bộ phận bạn bằng cách sử dụng dig. Hiển thị danh sách tên máy chủ DNS trong chuỗi ủy quyền khi trả lời truy vấn của bạn. b. Lặp lại phần (a) cho một số trang web phổ biến, chẳng hạn như google.com, yahoo

.com hoặc amazon.com. P20. Giả sử bạn có thể truy cập vào bộ nhớ đệm trong máy chủ DNS cục bộ tại nơi bạn khởi hành.

tâm trí. Bạn có thể đề xuất một cách để xác định đại khái các máy chủ Web (bên ngoài bộ phận của bạn) được người dùng trong bộ phận của bạn ưa chuộng nhất không? Giải thích. P21. Giả sử bộ phận của bạn có một máy chủ DNS cục bộ cho tất cả các máy tính trong

phòng. Bạn là người dùng bình thường (tức là không phải quản trị viên mạng/hệ thống). Bạn có thể xác định liệu một trang Web bên ngoài có thể được truy cập từ máy tính trong bộ phận của bạn vài giây trước không? Giải thích. P22. Hãy cân nhắc việc phân phối một tệp có dung lượng F = 20 Gbits cho N đồng nghiệp. Máy chủ có

tốc độ tải lên của us = 30 Mbps và mỗi thiết bị ngang hàng có tốc độ tải xuống di = 2 Mbps và tốc độ tải lên là u. Đối với N = 10, 100 và 1.000 và u = 300 Kbps, 700 Kbps và 2 Mbps, hãy chuẩn bị biểu đồ đưa ra thời gian phân phối tối thiểu cho từng kết hợp N và u cho cả phân phối máy khách và máy chủ P2P. P23. Hãy xem xét việc phân phối một tệp F bit cho N ngang hàng bằng cách sử dụng kho lưu trữ máy khách-máy chủ.

kiến trúc. Giả sử một mô hình linh hoạt trong đó máy chủ có thể truyền đồng thời tới nhiều thiết bị ngang hàng, truyền đến từng thiết bị ngang hàng ở các tốc độ khác nhau, miễn là tốc độ kết hợp không vượt quá chúng ta. Một. Giả sử rằng chúng tôi/N ... dmin. Chỉ định một sơ đồ phân phối có khả năng phân phối

thời gian hoạt động của NF/us. b. Giả sử rằng chúng tôi/N Ú dmin. Chỉ định một sơ đồ phân phối có khả năng phân phối

thời gian phản ứng F/dmin. c. Kết luận rằng thời gian phân phối tối thiểu nói chung được cho bởi

max5NF/chúng tôi, F/dmin6. P24. Hãy cân nhắc việc phân phối một tệp F bit cho N ngang hàng bằng kiến ​​trúc P2P.

Giả sử một mô hình chất lỏng. Để đơn giản, giả sử rằng dmin rất lớn, do đó băng thông tải xuống ngang hàng không bao giờ là nút cổ chai. Một. Giả sử rằng chúng ta ... (us + u1 + . . . + uN)/N. Chỉ định phân phối

sơ đồ có thời gian phân phối F/us.

b\. Giả sử chúng ta Ú (us + u1 + . . . + uN)/N. Chỉ định phân phối

lược đồ có thời gian phân phối là NF/(us + u1 + . . . + uN). c. Kết luận rằng thời gian phân phối tối thiểu nói chung được cho bởi

max5F/us, NF/(us + u1 + . . . + uN)6. P25. Hãy xem xét một mạng lớp phủ có N ngang hàng đang hoạt động, với mỗi cặp ngang hàng có

đang kết nối TCP đang hoạt động. Ngoài ra, giả sử rằng các kết nối TCP đi qua tổng số M bộ định tuyến. Có bao nhiêu nút và cạnh trong mạng lớp phủ tương ứng? P26. Giả sử Bob tham gia torrent BitTorrent, nhưng anh ấy không muốn tải lên bất kỳ

dữ liệu cho bất kỳ đồng nghiệp nào khác (được gọi là free-riding). Một. Bob tuyên bố rằng anh ấy có thể nhận được bản sao hoàn chỉnh của tệp được chia sẻ

bởi bầy đàn. Yêu cầu của Bob có khả thi không? Tại sao hoặc tại sao không? b. Bob tuyên bố thêm rằng anh ấy có thể làm cho việc "đi xe tự do" của mình trở nên hiệu quả hơn.

hiệu quả bằng cách sử dụng một tập hợp nhiều máy tính (có địa chỉ IP riêng biệt) trong phòng máy tính ở khoa của anh ấy. Làm thế nào anh ấy có thể làm điều đó? P27. Hãy xem xét một hệ thống DASH có N phiên bản video (tại N khác nhau

tốc độ và chất lượng) và N phiên bản âm thanh (với N tốc độ và chất lượng khác nhau). Giả sử chúng tôi muốn cho phép người chơi chọn bất kỳ lúc nào trong số N phiên bản video và bất kỳ N phiên bản âm thanh nào. Một. Nếu chúng tôi tạo các tệp sao cho âm thanh được trộn lẫn với video thì máy chủ

chỉ gửi một luồng phương tiện tại một thời điểm nhất định, máy chủ sẽ cần lưu trữ bao nhiêu tệp (mỗi tệp có một URL khác nhau)? b. Thay vào đó, nếu máy chủ gửi các luồng âm thanh và video riêng biệt và có

máy khách đồng bộ hóa các luồng, máy chủ sẽ cần lưu trữ bao nhiêu tệp? P28. Cài đặt và biên dịch các chương trình Python TCPClient và UDPClient trên một

máy chủ và TCPServer và UDPServer trên máy chủ khác. Một. Giả sử bạn chạy TCPClient trước khi chạy TCPServer. Điều gì xảy ra?

Tại sao? b. Giả sử bạn chạy UDPClient trước khi chạy UDPServer. Điều gì xảy ra?

Tại sao? c. Điều gì xảy ra nếu bạn sử dụng số cổng khác nhau cho máy khách và máy chủ

bên? P29. Giả sử rằng trong UDPClient.py, sau khi tạo socket, chúng ta thêm dòng:

clientSocket.bind((\'\', 5432)) Có cần thiết phải thay đổi UDPServer.py không? Số cổng cho các ổ cắm trong UDPClient và UDPServer là gì? Họ là gì trước khi thực hiện thay đổi này?

BÀI VIỆC LẬP TRÌNH SOCKET 175

P30. Bạn có thể định cấu hình trình duyệt của mình để mở nhiều kết nối đồng thời không

tới một trang Web? Ưu điểm và nhược điểm của việc có nhiều kết nối TCP đồng thời là gì? P31. Chúng tôi đã thấy rằng các ổ cắm Internet TCP coi dữ liệu được gửi dưới dạng byte

phát trực tuyến nhưng ổ cắm UDP nhận ra ranh giới tin nhắn. Ưu điểm và nhược điểm của API định hướng byte so với việc API nhận dạng rõ ràng và duy trì ranh giới thông báo do ứng dụng xác định là gì? P32. Máy chủ Web Apache là gì? Nó có giá bao nhiêu? Chức năng gì-

hiện tại nó có không? Bạn có thể muốn xem Wikipedia để trả lời câu hỏi này.

**Socket Bài tập lập trình**

Trang web đồng hành bao gồm sáu bài tập lập trình socket. Bốn nhiệm vụ đầu tiên được tóm tắt dưới đây. Bài tập thứ năm sử dụng giao thức ICMP và được tóm tắt ở cuối Chương 5. Học sinh nên hoàn thành một số bài tập, nếu không phải tất cả, trong số các bài tập này. Học sinh có thể tìm thấy thông tin chi tiết đầy đủ về các bài tập này, cũng như các đoạn mã Python quan trọng, tại trang Web www.pearsonhighered.com/cs-resources.

Bài tập 1: Máy chủ Web

Trong bài tập này, bạn sẽ phát triển một máy chủ Web đơn giản bằng Python có khả năng xử lý chỉ một yêu cầu. Cụ thể, máy chủ Web của bạn sẽ (i) tạo ổ cắm kết nối khi được máy khách (trình duyệt) liên hệ; (ii) nhận yêu cầu HTTP từ kết nối này; (iii) phân tích yêu cầu để xác định tệp cụ thể được yêu cầu; (iv) lấy tệp được yêu cầu từ hệ thống tệp của máy chủ; (v) tạo thông báo phản hồi HTTP bao gồm tệp được yêu cầu trước các dòng tiêu đề; và (vi) gửi phản hồi qua kết nối TCP tới trình duyệt yêu cầu. Nếu trình duyệt yêu cầu một tệp không có trong máy chủ của bạn, máy chủ của bạn sẽ trả về thông báo lỗi "404 Not Found".

Trong Trang web đồng hành, chúng tôi cung cấp mã khung cho máy chủ của bạn. Công việc của bạn là hoàn thành mã, chạy máy chủ và sau đó kiểm tra máy chủ bằng cách gửi yêu cầu từ các trình duyệt chạy trên các máy chủ khác nhau. Nếu bạn chạy máy chủ của mình trên một máy chủ đã có máy chủ Web chạy trên đó thì bạn nên sử dụng một cổng khác với cổng 80 cho máy chủ Web của mình.

Bài tập 2: UDP Pinger

Trong bài tập lập trình này, bạn sẽ viết chương trình ping máy khách bằng Python. Máy khách của bạn sẽ gửi một tin nhắn ping đơn giản đến máy chủ, nhận lại tin nhắn pong tương ứng từ máy chủ và xác định độ trễ giữa thời điểm máy khách

đã gửi tin nhắn ping và nhận được tin nhắn pong. Độ trễ này được gọi là Thời gian khứ hồi (RTT). Chức năng do máy khách và máy chủ cung cấp tương tự như chức năng được cung cấp bởi chương trình ping tiêu chuẩn có sẵn trong các hệ điều hành hiện đại. Tuy nhiên, các chương trình ping tiêu chuẩn sử dụng Giao thức tin nhắn điều khiển Internet (ICMP) (chúng ta sẽ nghiên cứu trong Chương 5). Ở đây chúng ta sẽ tạo một chương trình ping dựa trên UDP không chuẩn (nhưng đơn giản!)

Chương trình ping của bạn là gửi 10 tin nhắn ping đến máy chủ mục tiêu qua UDP. Đối với mỗi tin nhắn, khách hàng của bạn phải xác định và in RTT khi tin nhắn pong tương ứng được trả về. Vì UDP là giao thức không đáng tin cậy nên gói được gửi bởi máy khách hoặc máy chủ có thể bị mất. Vì lý do này, khách hàng không thể đợi vô thời hạn để trả lời tin nhắn ping. Bạn nên yêu cầu khách hàng đợi tối đa một giây để nhận được phản hồi từ máy chủ; nếu không nhận được phản hồi, khách hàng sẽ cho rằng gói tin đã bị mất và in thông báo tương ứng.

Trong nhiệm vụ này, bạn sẽ được cung cấp mã hoàn chỉnh cho máy chủ (có sẵn trên Trang web đồng hành). Công việc của bạn là viết mã máy khách, mã này sẽ rất giống với mã máy chủ. Trước tiên bạn nên nghiên cứu kỹ mã máy chủ. Sau đó, bạn có thể viết mã máy khách, tự do cắt và dán các dòng từ mã máy chủ.

Nhiệm vụ 3: Ứng dụng thư

Mục tiêu của nhiệm vụ lập trình này là tạo một ứng dụng thư khách đơn giản để gửi e-mail đến bất kỳ người nhận nào. Khách hàng của bạn sẽ cần thiết lập kết nối TCP với máy chủ thư (ví dụ: máy chủ thư Google), đối thoại với máy chủ thư bằng giao thức SMTP, gửi thư e-mail đến người nhận (ví dụ: bạn bè của bạn) qua máy chủ thư và cuối cùng đóng kết nối TCP với máy chủ thư.

Đối với nhiệm vụ này, Trang web đồng hành cung cấp mã khung cho khách hàng của bạn. Công việc của bạn là hoàn thành mã và kiểm tra ứng dụng khách của mình bằng cách gửi e-mail đến các tài khoản người dùng khác nhau. Bạn cũng có thể thử gửi qua các máy chủ khác nhau (ví dụ: qua máy chủ thư Google và qua máy chủ thư trường đại học của bạn).

Nhiệm vụ 4: Proxy web

Trong bài tập này, bạn sẽ phát triển một proxy Web. Khi proxy của bạn nhận được yêu cầu HTTP cho một đối tượng từ trình duyệt, nó sẽ tạo một yêu cầu HTTP mới cho cùng một đối tượng và gửi nó đến máy chủ gốc. Khi proxy nhận được phản hồi HTTP tương ứng với đối tượng từ máy chủ gốc, nó sẽ tạo phản hồi HTTP mới, bao gồm cả đối tượng và gửi nó đến máy khách.

Đối với nhiệm vụ này, Trang web đồng hành cung cấp mã khung cho máy chủ proxy. Công việc của bạn là hoàn thành mã và sau đó kiểm tra nó bằng cách yêu cầu các trình duyệt khác nhau yêu cầu các đối tượng Web thông qua proxy của bạn.

PHÒNG THÍ NGHIỆM WIRESHARK: DNS 177

**Wireshark Phòng thí nghiệm: HTTP**

Sau khi đã bắt đầu sử dụng công cụ đánh hơi gói Wireshark trong Lab 1, giờ đây chúng tôi đã sẵn sàng sử dụng Wireshark để điều tra các giao thức đang hoạt động. Trong phòng thí nghiệm này, chúng ta sẽ khám phá một số khía cạnh của giao thức HTTP: tương tác GET/trả lời cơ bản, định dạng thông báo HTTP, truy xuất tệp HTML lớn, truy xuất tệp HTML có URL nhúng, kết nối liên tục và không liên tục cũng như xác thực và bảo mật HTTP.

Như trường hợp của tất cả các phòng thí nghiệm Wireshark, mô tả đầy đủ về phòng thí nghiệm này có sẵn trên trang web của cuốn sách này, www.pearsonhighered.com/cs-resources.

**Wireshark Phòng thí nghiệm: DNS**

Trong phòng thí nghiệm này, chúng ta xem xét kỹ hơn phía máy khách của DNS, giao thức dịch tên máy chủ Internet thành địa chỉ IP. Hãy nhớ lại Phần 2.5 rằng vai trò của máy khách trong DNS tương đối đơn giản---máy khách gửi truy vấn đến máy chủ DNS cục bộ của nó và nhận được phản hồi phản hồi. Nhiều điều có thể diễn ra một cách bí mật, không bị máy khách DNS nhìn thấy, khi các máy chủ DNS phân cấp liên lạc với nhau để giải quyết đệ quy hoặc lặp đi lặp lại truy vấn DNS của máy khách. Tuy nhiên, từ quan điểm của máy khách DNS, giao thức khá đơn giản---một truy vấn được tạo ra tới máy chủ DNS cục bộ và nhận được phản hồi từ máy chủ đó. Chúng tôi quan sát DNS hoạt động trong phòng thí nghiệm này.

Như trường hợp của tất cả các phòng thí nghiệm Wireshark, mô tả đầy đủ về phòng thí nghiệm này có sẵn trên trang web của cuốn sách này, www.pearsonhighered.com/cs-resources.

PHỎNG VẤN VỚI\...

**Tim Berners-Lee**

Ngài Tim Berners-Lee được biết đến là người phát minh ra World Wide Web. Năm 1989, khi đang làm nghiên cứu sinh tại CERN, ông đã đề xuất một hệ thống quản lý thông tin phân tán dựa trên Internet bao gồm phiên bản gốc của giao thức HTTP. Cùng năm đó, anh đã triển khai thành công thiết kế của mình trên máy khách và máy chủ. Ông đã nhận được giải thưởng Turing năm 2016 vì "phát minh ra World Wide Web, trình duyệt Web đầu tiên cũng như các giao thức và thuật toán cơ bản cho phép Web mở rộng quy mô". Ông là Đồng sáng lập của World Wide Web Foundation và hiện là Giáo sư Khoa học Máy tính tại Đại học Oxford và là giáo sư tại CSAIL tại MIT.

Ban đầu bạn học vật lý. Mạng giống với vật lý như thế nào?

Khi nghiên cứu vật lý, bạn tưởng tượng những quy luật ứng xử nào ở quy mô rất nhỏ có thể tạo ra thế giới quy mô lớn như chúng ta thấy. Khi bạn thiết kế một hệ thống toàn cầu như Web, bạn cố gắng phát minh ra các quy tắc hoạt động của các trang Web và các liên kết cũng như những thứ có thể tạo ra một thế giới quy mô lớn như chúng ta mong muốn. Một cái là phân tích và cái kia là tổng hợp, nhưng chúng rất giống nhau.

Điều gì đã ảnh hưởng đến việc bạn chuyên về mạng lưới?

Sau tấm bằng vật lý của tôi, các công ty nghiên cứu viễn thông dường như là nơi thú vị nhất. Bộ vi xử lý vừa mới ra đời và viễn thông đang chuyển đổi rất nhanh từ logic nối dây sang hệ thống dựa trên bộ vi xử lý. Nó rất thú vị.

Phần thử thách nhất trong công việc của bạn là gì?

Khi hai nhóm bất đồng sâu sắc về điều gì đó nhưng cuối cùng lại muốn đạt được mục tiêu chung, việc tìm ra chính xác ý nghĩa của mỗi nhóm và những hiểu lầm ở đâu có thể rất khó khăn. Chủ tịch của bất kỳ nhóm làm việc nào cũng biết điều đó. Tuy nhiên, đây là những gì cần thiết để đạt được tiến bộ hướng tới sự đồng thuận trên quy mô lớn.

Được phép của Tim Berners-Lee

![](media/image3.png){width="5.5in" height="8.25in"}

Những gì mọi người đã truyền cảm hứng cho bạn một cách chuyên nghiệp?

Cha mẹ tôi, những người tham gia vào những ngày đầu của máy tính, đã khiến tôi say mê với toàn bộ chủ đề này. Mike Sendall và Peggie Rimmer, những người mà tôi đã từng làm việc cho nhiều lần tại CERN, nằm trong số những người đã dạy và khuyến khích tôi. Sau này tôi học cách ngưỡng mộ mọi người, trong đó có Vanevar Bush, Doug Englebart, và Ted Nelson, những người từng có ước mơ tương tự vào thời của họ nhưng không được hưởng lợi từ sự tồn tại của PC và Internet để có thể hiện thực hóa điều đó.

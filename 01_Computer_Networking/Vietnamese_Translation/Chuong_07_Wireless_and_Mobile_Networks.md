**Chương 7: Mạng Không Dây và Mạng Di Động (Wireless & Mobile Networks)**

Trong thế giới điện thoại, 25 năm qua là những năm hoàng kim của điện thoại di động. Số lượng thuê bao di động trên toàn thế giới đã tăng từ 34 triệu năm 1993 lên 8,3 tỷ thuê bao vào năm 2019. Hiện số lượng thuê bao điện thoại di động còn lớn hơn cả số người trên hành tinh của chúng ta. Nhiều ưu điểm của điện thoại di động là điều hiển nhiên đối với tất cả mọi người---bất cứ nơi nào, bất cứ lúc nào, truy cập không dây vào mạng điện thoại toàn cầu thông qua một thiết bị nhẹ có tính di động cao. Gần đây hơn, điện thoại thông minh, máy tính bảng và máy tính xách tay đã được kết nối không dây với Internet thông qua mạng di động hoặc WiFi. Và ngày càng có nhiều thiết bị như máy chơi game, máy điều nhiệt, hệ thống an ninh gia đình, thiết bị gia dụng, đồng hồ, kính mắt, ô tô, hệ thống điều khiển giao thông và nhiều thiết bị khác được kết nối không dây với Internet.

Từ quan điểm mạng, những thách thức đặt ra khi kết nối các thiết bị di động và không dây này, đặc biệt ở lớp liên kết và lớp mạng, rất khác so với các mạng máy tính có dây truyền thống nên một chương riêng dành cho việc nghiên cứu mạng không dây và mạng di động (tức là chương này) là phù hợp.

Chúng ta sẽ bắt đầu chương này bằng việc thảo luận về người dùng di động, liên kết không dây và mạng cũng như mối quan hệ của họ với các mạng lớn hơn (thường có dây) mà họ kết nối. Chúng ta sẽ phân biệt giữa những thách thức đặt ra bởi tính chất không dây của các liên kết truyền thông trong các mạng như vậy và bởi tính di động mà các liên kết không dây này cho phép. Việc tạo ra sự khác biệt quan trọng này---giữa mạng không dây và tính di động---sẽ cho phép chúng tôi tách biệt, xác định và nắm vững tốt hơn các khái niệm chính trong từng lĩnh vực.

Chúng ta sẽ bắt đầu với phần tổng quan về cơ sở hạ tầng truy cập không dây và thuật ngữ liên quan. Sau đó chúng ta sẽ xem xét các đặc điểm của liên kết không dây này trong

**CHƯƠNG**

**Mạng không dây và di động**

![](media/image1.png){width="5.5in" height="6.930965660542432in"}

![](media/image2.png){width="5.5in" height="0.9567311898512686in"}

Mục 7.2. Chúng tôi đưa ra phần giới thiệu ngắn gọn về đa truy cập phân chia theo mã (CDMA), một giao thức truy cập phương tiện chia sẻ thường được sử dụng trong các mạng không dây, trong Phần 7.2. Trong Phần 7.3, chúng ta sẽ xem xét các khía cạnh cấp độ liên kết của tiêu chuẩn mạng LAN không dây IEEE 802.11 (WiFi) ở một mức độ sâu hơn; chúng tôi cũng sẽ nói đôi lời về mạng khu vực cá nhân không dây Bluetooth. Trong Phần 7.4, chúng tôi sẽ cung cấp thông tin tổng quan về truy cập Internet di động, bao gồm 4G và các công nghệ di động 5G mới nổi cung cấp cả truy cập Internet thoại và tốc độ cao. Trong Phần 7.5, chúng ta sẽ chú ý đến tính di động, tập trung vào các vấn đề về định vị người dùng di động, định tuyến tới người dùng di động và "chuyển giao" người dùng di động di chuyển linh hoạt từ điểm kết nối này sang điểm khác. Chúng tôi sẽ xem xét cách triển khai các dịch vụ di động này trong mạng di động 4G/5G và trong tiêu chuẩn Di động IP trong Phần 7.6. Cuối cùng, chúng ta sẽ xem xét tác động của các liên kết không dây và tính di động lên các giao thức tầng vận chuyển và các ứng dụng nối mạng trong Phần 7.7.

**7.1 Giới thiệu**

Hình 7.1 cho thấy bối cảnh trong đó chúng ta sẽ xem xét các chủ đề về truyền thông và di động dữ liệu không dây. Chúng ta sẽ bắt đầu bằng cách trình bày cuộc thảo luận của mình đủ tổng quát để bao quát nhiều loại mạng, bao gồm cả mạng LAN không dây như WiFi và mạng di động 4G và 5G; chúng ta sẽ đi sâu vào thảo luận chi tiết hơn về các kiến ​​trúc không dây cụ thể trong các phần sau. Chúng ta có thể xác định các thành phần sau trong mạng không dây:

• Máy chủ không dây. Như trong trường hợp mạng có dây, máy chủ là thiết bị hệ thống cuối chạy các ứng dụng. Máy chủ không dây có thể là điện thoại thông minh, máy tính bảng hoặc máy tính xách tay hoặc có thể là thiết bị Internet of Things (IoT) như cảm biến, thiết bị, ô tô hoặc bất kỳ thiết bị nào khác trong vô số thiết bị được kết nối với Internet. Bản thân các máy chủ có thể di động hoặc không. • Liên kết không dây. Máy chủ kết nối với trạm cơ sở (được xác định bên dưới) hoặc với máy chủ không dây khác thông qua liên kết truyền thông không dây. Các công nghệ liên kết không dây khác nhau có tốc độ truyền khác nhau và có thể truyền qua các khoảng cách khác nhau. Hình 7.2 cho thấy hai đặc điểm chính, tốc độ truyền liên kết và phạm vi phủ sóng của các tiêu chuẩn mạng không dây phổ biến hơn. (Hình này chỉ nhằm cung cấp ý tưởng sơ bộ về những đặc điểm này. Ví dụ: một số loại mạng này hiện chỉ đang được triển khai và một số tốc độ liên kết có thể tăng hoặc giảm vượt quá các giá trị được hiển thị tùy thuộc vào khoảng cách, điều kiện kênh và số lượng người dùng trong mạng không dây.) Chúng tôi sẽ đề cập đến các tiêu chuẩn này ở phần sau của nửa đầu chương này; chúng ta cũng sẽ xem xét các đặc điểm liên kết không dây khác (chẳng hạn như tỷ lệ lỗi bit và nguyên nhân gây ra lỗi bit) trong Phần 7.2.

Trong Hình 7.1, các liên kết không dây kết nối các máy chủ không dây nằm ở rìa mạng vào cơ sở hạ tầng mạng lớn hơn. Chúng tôi xin nói thêm rằng các liên kết không dây đôi khi cũng được sử dụng trong mạng để kết nối các bộ định tuyến, bộ chuyển mạch và các thiết bị mạng khác. Tuy nhiên, trọng tâm của chúng ta trong chương này sẽ là việc sử dụng truyền thông không dây ở biên mạng, vì ở đây có nhiều thách thức kỹ thuật thú vị nhất và hầu hết sự tăng trưởng đang diễn ra. • Trạm cơ sở. Trạm cơ sở là một phần quan trọng của cơ sở hạ tầng mạng không dây. Không giống như máy chủ không dây và liên kết không dây, trạm cơ sở không có đối tác rõ ràng trong mạng có dây. Trạm gốc chịu trách nhiệm gửi và nhận dữ liệu (ví dụ: gói) đến và từ máy chủ không dây được liên kết với trạm gốc đó. Một trạm cơ sở thường sẽ chịu trách nhiệm điều phối việc truyền tải nhiều máy chủ không dây mà nó được liên kết. Khi chúng tôi nói máy chủ không dây được "liên kết" với trạm gốc, chúng tôi muốn nói rằng (1) máy chủ nằm trong khoảng cách liên lạc không dây của trạm gốc và (2) máy chủ sử dụng trạm gốc đó để chuyển tiếp dữ liệu giữa nó (máy chủ) và mạng lớn hơn. Tháp di động trong mạng di động và các điểm truy cập trong mạng LAN không dây 802.11 là ví dụ về các trạm cơ sở.

*Hình 7.1 ♦ Các thành phần của mạng không dây*

Hạ tầng mạng

Chìa khóa:

Điểm truy cập không dây

Vùng phủ sóng

Máy chủ không dây

Máy chủ không dây đang chuyển động

Trong Hình 7.1, trạm cơ sở được kết nối với mạng lớn hơn (ví dụ: Internet, mạng công ty hoặc mạng gia đình), do đó hoạt động như một trạm chuyển tiếp lớp liên kết giữa máy chủ không dây và phần còn lại của thế giới mà máy chủ liên lạc. Hosts được liên kết với trạm gốc thường được coi là hoạt động ở chế độ cơ sở hạ tầng, vì tất cả các dịch vụ mạng truyền thống (ví dụ: gán địa chỉ và định tuyến) đều được cung cấp bởi mạng mà máy chủ được kết nối qua trạm gốc. Trong mạng ad hoc, máy chủ không dây không có cơ sở hạ tầng để kết nối. Trong trường hợp không có cơ sở hạ tầng như vậy, bản thân các máy chủ phải cung cấp các dịch vụ như định tuyến, gán địa chỉ, dịch tên giống DNS, v.v. Khi một máy chủ di động di chuyển ra ngoài phạm vi của một trạm gốc và vào phạm vi của một trạm gốc khác, nó sẽ thay đổi điểm kết nối của nó vào mạng lớn hơn (tức là thay đổi trạm gốc mà nó được liên kết)---một quá trình được gọi là chuyển giao hoặc chuyển giao. Tính di động như vậy đặt ra nhiều câu hỏi đầy thách thức. Nếu máy chủ có thể di chuyển, làm cách nào để tìm vị trí hiện tại của máy chủ di động trong mạng để dữ liệu có thể được chuyển tiếp đến máy chủ di động đó? Việc đánh địa chỉ được thực hiện như thế nào khi máy chủ có thể ở một trong nhiều vị trí có thể? Nếu máy chủ di chuyển trong khi kết nối hoặc gọi điện thoại TCP, dữ liệu được định tuyến như thế nào để kết nối

*Hình 7.2 ♦ Tốc độ và phạm vi truyền không dây cho WiFi, mạng di động*

Chuẩn 4G/5G và Bluetooth (lưu ý: trục không tuyến tính)

802.11ax

802.11ac

802.11n

802.11 à, à

5G

4G LTE

802.11g

802.11b

Bluetooth

Tầm trung ngoài trời trong nhà

ngoài trời

Tầm xa

ngoài trời 10--30m 50--200m 200m--4Km 4Km--15Km

14Gbps

10Gbps

3,5Gbps

600 Mb/giây

54 Mb/giây

2 Mb/giây

11 Mb/giây

tiếp tục không bị gián đoạn? Những câu hỏi này và nhiều (rất nhiều!) câu hỏi khác làm cho mạng không dây và mạng di động trở thành một lĩnh vực nghiên cứu mạng thú vị. • Cơ sở hạ tầng mạng. Đây là mạng lớn hơn mà máy chủ không dây có thể muốn liên lạc.

Sau khi thảo luận về "các phần" của mạng không dây, chúng tôi lưu ý rằng các phần này có thể được kết hợp theo nhiều cách khác nhau để tạo thành các loại mạng không dây khác nhau. Bạn có thể thấy việc phân loại các loại mạng không dây này hữu ích khi đọc tiếp trong chương này hoặc đọc/tìm hiểu thêm về các mạng không dây ngoài cuốn sách này. Ở mức cao nhất, chúng tôi có thể phân loại mạng không dây theo hai tiêu chí: (i) liệu một gói trong mạng không dây có đi qua chính xác một bước nhảy không dây hay nhiều bước nhảy không dây hay không và (ii) liệu có cơ sở hạ tầng như trạm gốc trong mạng hay không:

• Single-hop, dựa trên cơ sở hạ tầng. Các mạng này có trạm cơ sở được kết nối với mạng có dây lớn hơn (ví dụ: Internet). Hơn nữa, tất cả giao tiếp đều diễn ra giữa trạm cơ sở này và máy chủ không dây qua một bước nhảy không dây duy nhất. Mạng 802.11 bạn sử dụng trong lớp học, quán cà phê hoặc thư viện; và các mạng dữ liệu 4G LTE mà chúng ta sẽ tìm hiểu sau đây đều thuộc loại này. Phần lớn các tương tác hàng ngày của chúng ta là với các mạng không dây dựa trên cơ sở hạ tầng, một bước nhảy. • Một bước nhảy, không cần cơ sở hạ tầng. Trong các mạng này, không có trạm gốc nào được kết nối với mạng không dây. Tuy nhiên, như chúng ta sẽ thấy, một trong các nút trong mạng một chặng này có thể phối hợp việc truyền của các nút khác. Mạng Bluetooth (kết nối các thiết bị không dây nhỏ như bàn phím, loa và tai nghe mà chúng ta sẽ nghiên cứu trong Phần 7.3.6) là mạng một bước nhảy, không có cơ sở hạ tầng. • Multi-hop, dựa trên cơ sở hạ tầng. Trong các mạng này, có một trạm gốc được kết nối với mạng lớn hơn. Tuy nhiên, một số nút không dây có thể phải chuyển tiếp liên lạc của chúng qua các nút không dây khác để liên lạc qua trạm gốc. Một số mạng cảm biến không dây và cái gọi là mạng lưới không dây được triển khai trong nhà thuộc loại này. • Đa chặng, không cần cơ sở hạ tầng. Không có trạm gốc trong các mạng này và các nút có thể phải chuyển tiếp tin nhắn giữa một số nút khác để đến đích. Các nút cũng có thể là thiết bị di động, với khả năng kết nối thay đổi giữa các nút---một loại mạng được gọi là mạng ad hoc di động (MANET). Nếu các nút di động là phương tiện thì mạng là mạng ad hoc dành cho xe cộ (VANET). Như bạn có thể tưởng tượng, việc phát triển các giao thức cho các mạng như vậy là một thách thức và là chủ đề của nhiều nghiên cứu đang diễn ra.

Trong chương này, chúng ta sẽ chủ yếu giới hạn ở các mạng một chặng và sau đó chủ yếu là các mạng dựa trên cơ sở hạ tầng.

Bây giờ chúng ta hãy tìm hiểu sâu hơn về những thách thức kỹ thuật nảy sinh trong mạng không dây và mạng di động. Chúng ta sẽ bắt đầu bằng cách xem xét từng liên kết không dây riêng lẻ, trì hoãn việc thảo luận về tính di động cho đến phần sau của chương này.

**7.2 Liên kết không dây và đặc điểm mạng**

Các liên kết không dây khác với các liên kết có dây ở một số điểm quan trọng:

• Giảm cường độ tín hiệu. Bức xạ điện từ suy yếu khi nó truyền qua vật chất (ví dụ: tín hiệu vô tuyến truyền qua tường). Ngay cả trong không gian trống, tín hiệu sẽ bị phân tán, dẫn đến cường độ tín hiệu giảm (đôi khi được gọi là suy hao đường truyền) khi khoảng cách giữa người gửi và người nhận tăng lên. • Sự can thiệp từ các nguồn khác. Các nguồn vô tuyến phát trong cùng băng tần sẽ gây nhiễu lẫn nhau. Ví dụ: điện thoại không dây 2,4 GHz và mạng LAN không dây 802.11b truyền trong cùng một dải tần. Do đó, người dùng mạng LAN không dây 802.11b nói chuyện trên điện thoại không dây 2,4 GHz có thể mong đợi rằng cả mạng và điện thoại đều không hoạt động tốt. Ngoài nhiễu từ các nguồn phát, nhiễu điện từ trong môi trường (ví dụ: động cơ gần đó, lò vi sóng) có thể gây nhiễu. Vì lý do này, một số tiêu chuẩn 802.11 gần đây hoạt động ở dải tần 5GHz. • Lan truyền đa đường. Sự lan truyền đa đường xảy ra khi các phần của sóng điện từ phản xạ khỏi vật thể và mặt đất, đi theo những đường đi có độ dài khác nhau giữa người gửi và người nhận. Điều này dẫn đến việc làm mờ tín hiệu nhận được ở máy thu. Việc di chuyển các đối tượng giữa người gửi và người nhận có thể khiến việc truyền đa đường thay đổi theo thời gian.

Để biết thảo luận chi tiết về các đặc tính, mô hình và phép đo của kênh không dây, hãy xem \[Anderson 1995; Almers 2007\].

Cuộc thảo luận ở trên gợi ý rằng lỗi bit sẽ phổ biến hơn trong các liên kết không dây so với các liên kết có dây. Vì lý do này, có lẽ không có gì đáng ngạc nhiên khi các giao thức liên kết không dây (chẳng hạn như giao thức 802.11 mà chúng tôi sẽ xem xét trong phần sau) không chỉ sử dụng các mã phát hiện lỗi CRC mạnh mẽ mà còn sử dụng các giao thức truyền dữ liệu đáng tin cậy ở cấp độ liên kết để truyền lại các khung bị hỏng.

Sau khi xem xét những suy giảm có thể xảy ra trên kênh không dây, tiếp theo chúng ta hãy chuyển sự chú ý của chúng ta sang máy chủ nhận tín hiệu không dây. Máy chủ này nhận được tín hiệu điện từ là sự kết hợp giữa dạng suy giảm của tín hiệu gốc do người gửi truyền (bị suy giảm do hiệu ứng suy giảm và lan truyền đa đường mà chúng ta đã thảo luận ở trên, cùng với các tác động khác) và nhiễu nền trong môi trường. Tỷ lệ tín hiệu trên nhiễu (SNR) là thước đo tương đối về cường độ của tín hiệu nhận được (tức là thông tin được truyền đi) và nhiễu này. SNR thường được đo bằng đơn vị decibel (dB), một đơn vị đo mà một số người cho rằng được sử dụng bởi

kỹ sư điện chủ yếu để gây nhầm lẫn cho các nhà khoa học máy tính. SNR, được đo bằng dB, gấp 20 lần tỷ lệ logarit cơ số 10 của biên độ tín hiệu thu được và biên độ của nhiễu. Với mục đích của chúng ta ở đây, chúng ta chỉ cần biết rằng SNR lớn hơn giúp máy thu dễ dàng trích xuất tín hiệu truyền từ nhiễu nền hơn.

*Hình 7.3 (được điều chỉnh từ \[Holland 2001\]) cho thấy tỷ lệ lỗi bit (BER) - nói một cách đại khái là xác suất mà một bit truyền được nhận bị lỗi ở bộ thu - so với SNR đối với ba kỹ thuật điều chế khác nhau để mã hóa thông tin truyền tải trên một kênh không dây lý tưởng hóa. Lý thuyết điều chế và mã hóa, cũng như trích xuất tín hiệu và BER, nằm ngoài phạm vi của văn bản này (xem \[Schwartz 1980; Goldsmith 2005\] để thảo luận về các chủ đề này). Tuy nhiên, Hình 7.3 minh họa một số đặc điểm của lớp vật lý rất quan trọng trong việc hiểu các giao thức truyền thông không dây ở lớp cao hơn:*

• Đối với sơ đồ điều chế nhất định, SNR càng cao thì BER càng thấp. Vì người gửi có thể tăng SNR bằng cách tăng công suất truyền, nên người gửi có thể giảm xác suất nhận được khung bị lỗi bằng cách tăng công suất truyền. Tuy nhiên, lưu ý rằng có rất ít lợi ích thực tế trong việc tăng công suất vượt quá một ngưỡng nhất định, chẳng hạn như giảm BER từ 10-12 xuống 10-13. Cũng có những nhược điểm liên quan đến việc tăng công suất truyền: Người gửi phải tiêu tốn nhiều năng lượng hơn

*Hình 7.3 ♦ Tỷ lệ lỗi bit, tốc độ truyền và SNR*

10--7

10--6

10--5

10--4

10--3

10--2

10--1

SNR (dB)

BER

QAM16 (4 Mb/giây)

QAM256 (8 Mb/giây)

BPSK (1 Mb/giây)

(một mối quan tâm quan trọng đối với người dùng di động chạy bằng pin) và việc truyền của người gửi có nhiều khả năng gây nhiễu việc truyền của người gửi khác (xem Hình 7.4(b)). • Đối với một SNR nhất định, kỹ thuật điều chế có tốc độ truyền bit cao hơn (dù có lỗi hay không) sẽ có BER cao hơn. Ví dụ, trong Hình 7.3, với SNR là 10 dB, điều chế BPSK với tốc độ truyền 1 Mbps có BER nhỏ hơn 10-7, trong khi với điều chế QAM16 với tốc độ truyền 4 Mbps, BER là 10-1, quá cao để có ích trong thực tế. Tuy nhiên, với SNR là 20 dB, điều chế QAM16 có tốc độ truyền 4 Mbps và BER là 10-7, trong khi điều chế BPSK có tốc độ truyền chỉ 1 Mbps và BER thấp đến mức (theo nghĩa đen) "ngoài bảng xếp hạng". Nếu một người có thể chịu được BER bằng 10-7, thì tốc độ truyền cao hơn do QAM16 cung cấp sẽ khiến nó trở thành kỹ thuật điều chế được ưu tiên trong tình huống này. Những cân nhắc này làm phát sinh đặc điểm cuối cùng, được mô tả tiếp theo. • Lựa chọn động kỹ thuật điều chế lớp vật lý có thể được sử dụng để điều chỉnh kỹ thuật điều chế phù hợp với điều kiện kênh. SNR (và do đó là BER) có thể thay đổi do tính di động hoặc do những thay đổi trong môi trường. Điều chế và mã hóa thích ứng được sử dụng trong WiFi 802.11 cũng như trong các mạng dữ liệu di động 4G và 5G mà chúng ta sẽ nghiên cứu trong Phần 7.3 và 7.4. Ví dụ, điều này cho phép lựa chọn kỹ thuật điều chế cung cấp tốc độ truyền cao nhất có thể tùy thuộc vào ràng buộc về BER, đối với các đặc tính kênh nhất định.

Tỷ lệ lỗi bit cao hơn và thay đổi theo thời gian không phải là điểm khác biệt duy nhất giữa liên kết có dây và không dây. Hãy nhớ lại rằng trong trường hợp các liên kết quảng bá có dây, tất cả các nút

*Hình 7.4 ♦ Vấn đề ẩn thiết bị đầu cuối do chướng ngại vật (a) và fade (b)*

A A

C

B C

Vị tríb. Một.

Cường độ tín hiệu

B

nhận các truyền từ tất cả các nút khác. Trong trường hợp các liên kết không dây, tình huống không đơn giản như trong Hình 7.4. Giả sử rằng Trạm A đang truyền đến Trạm B. Giả sử rằng Trạm C đang truyền đến Trạm B. Với cái gọi là vấn đề thiết bị đầu cuối ẩn, các chướng ngại vật lý trong môi trường (ví dụ, một ngọn núi hoặc một tòa nhà) có thể ngăn A và C nghe thấy đường truyền của nhau, mặc dù đường truyền của A và C thực sự đang gây nhiễu ở đích B. Điều này được thể hiện trong Hình 7.4(a). Kịch bản thứ hai dẫn đến những va chạm không thể phát hiện được ở máy thu là do cường độ tín hiệu bị suy giảm khi truyền qua môi trường không dây. Hình 7.4(b) minh họa trường hợp A và C được đặt sao cho tín hiệu của chúng không đủ mạnh để phát hiện đường truyền của nhau, tuy nhiên tín hiệu của chúng đủ mạnh để gây nhiễu lẫn nhau tại trạm B. Như chúng ta sẽ thấy trong Phần 7.3, vấn đề thiết bị đầu cuối ẩn và sự mờ dần khiến cho việc đa truy cập trong mạng không dây phức tạp hơn đáng kể so với mạng có dây.

**7.2.1 CDMA**

Hãy nhớ lại Chương 6 rằng khi các máy chủ liên lạc qua một phương tiện dùng chung, cần có một giao thức để các tín hiệu được gửi bởi nhiều người gửi không gây nhiễu ở người nhận. Trong Chương 6, chúng tôi đã mô tả ba loại giao thức truy cập môi trường: phân vùng kênh, truy cập ngẫu nhiên và thay phiên nhau. Đa truy cập phân chia theo mã (CDMA) thuộc họ giao thức phân vùng kênh. Nó phổ biến trong mạng LAN không dây và công nghệ di động. Vì CDMA rất quan trọng trong thế giới không dây nên bây giờ chúng ta sẽ xem xét nhanh CDMA trước khi đi vào các công nghệ truy cập không dây cụ thể trong các phần tiếp theo.

Trong giao thức CDMA, mỗi bit được gửi đi sẽ được mã hóa bằng cách nhân bit đó với một tín hiệu (mã) thay đổi với tốc độ nhanh hơn nhiều (được gọi là tốc độ sứt mẻ) so với chuỗi bit dữ liệu ban đầu. Hình 7.5 cho thấy một kịch bản mã hóa/giải mã CDMA đơn giản, lý tưởng. Giả sử tốc độ các bit dữ liệu gốc đến bộ mã hóa CDMA xác định đơn vị thời gian; nghĩa là, mỗi bit dữ liệu gốc được truyền đi cần có một khe thời gian một bit. Gọi di là giá trị của bit dữ liệu cho khe bit thứ i. Để thuận tiện về mặt toán học, chúng tôi biểu thị một bit dữ liệu có giá trị 0 là -1. Mỗi khe bit được chia nhỏ thành M khe nhỏ; trong Hình 7.5, M = 8, mặc dù trong thực tế M lớn hơn nhiều. Mã CDMA được người gửi sử dụng bao gồm một chuỗi các giá trị M, cm, m = 1, . . . , M, mỗi giá trị nhận giá trị +1 hoặc -1. Trong ví dụ ở Hình 7.5, mã CDMA M-bit đang được người gửi sử dụng là (1, 1, 1, -1, 1, -1, -1, -1).

Để minh họa cách CDMA hoạt động, chúng ta hãy tập trung vào bit dữ liệu thứ i, di. Đối với khe nhỏ thứ m của thời gian truyền bit của di, đầu ra của bộ mã hóa CDMA, Zi,m, là giá trị của di nhân với bit thứ m trong mã CDMA được chỉ định, cm:

**Zi,m = di \# cm (7.1)**

Trong một thế giới đơn giản, không có người gửi can thiệp, người nhận sẽ nhận được các bit được mã hóa, Zi,m, và khôi phục bit dữ liệu gốc, di, bằng cách tính toán:

di = 1

M a

M

m=1

**Zi,m \# cm (7.2)**

Người đọc có thể muốn xem chi tiết của ví dụ trong Hình 7.5 để thấy rằng các bit dữ liệu gốc thực sự được khôi phục chính xác ở máy thu bằng phương trình 7.2.

*Hình 7.5 ♦ Một ví dụ CDMA đơn giản: Mã hóa bên gửi, giải mã bên nhận*

1 1 1

--1 --1--1--1

1 1 1

--1 --1--1--1

--1 --1 --1

1 1 1

--1 --1--1--1

1 1 1

Khe thời gian 1 đã nhận được đầu vào

Khe thời gian 0 đã nhận được đầu vào

Mã số

--1 --1 --1--1

1 1 1

--1 --1--1--1

1 1 1 Bit dữ liệu

Mã 1 1 1

--1 --1--1--1

1 1 1

--1 --1--1--1

d1 = --1

d0 = 1

Khe thời gian 1

Đầu ra kênh người gửi Zi,m

Người nhận

Zi,m di • cm =

Zi,m • cmd

tôi

m=1

M

S

Khe thời gian 1 kênh đầu ra

Khe thời gian đầu ra 0 kênh

Khe thời gian 0

d1 = --1

d0 = 1 --1

Tuy nhiên, thế giới không còn lý tưởng nữa và như đã lưu ý ở trên, CDMA phải hoạt động khi có sự can thiệp của những người gửi đang mã hóa và truyền dữ liệu của họ bằng cách sử dụng một mã được chỉ định khác. Nhưng làm thế nào máy thu CDMA có thể khôi phục các bit dữ liệu gốc của người gửi khi các bit dữ liệu đó bị rối với các bit được truyền bởi những người gửi khác? CDMA hoạt động dựa trên giả định rằng các tín hiệu bit truyền gây nhiễu là bổ sung. Ví dụ: điều này có nghĩa là nếu ba người gửi gửi giá trị 1 và người gửi thứ tư gửi giá trị -1 trong cùng một khe nhỏ, thì tín hiệu nhận được ở tất cả người nhận trong khe nhỏ đó là 2 (vì 1 + 1 + 1 - 1 = 2). Khi có nhiều người gửi, người gửi s tính toán các lần truyền được mã hóa của nó, Zs

i,m, theo cách tương tự như trong phương trình 7.1. Tuy nhiên, giá trị nhận được ở máy thu trong khe nhỏ thứ m của khe bit thứ i hiện là tổng số bit được truyền từ tất cả N người gửi trong khe nhỏ đó:

Z\*

tôi, m = một

N

s=1

Z s

Tôi

Thật ngạc nhiên, nếu mã của người gửi được chọn cẩn thận, thì mỗi người nhận có thể khôi phục dữ liệu được gửi bởi một người gửi nhất định từ tín hiệu tổng hợp chỉ bằng cách sử dụng mã của người gửi theo cách giống hệt như trong Phương trình 7.2:

di = 1

M a

M

m=1

Zi,m

**\* \# cm (7.3)**

như trong Hình 7.6, đối với ví dụ CDMA hai người gửi. Mã CDMA M-bit đang được người gửi phía trên sử dụng là (1, 1, 1, -1, 1, -1, -1, -1), trong khi mã CDMA đang được người gửi phía dưới sử dụng là (1, -1, 1, 1, 1, -1, 1, 1). Hình 7.6 minh họa bộ thu khôi phục các bit dữ liệu gốc từ bộ gửi phía trên. Lưu ý rằng người nhận có thể trích xuất dữ liệu từ người gửi 1 bất chấp việc truyền tải bị nhiễu từ người gửi 2.

Hãy nhớ lại sự tương tự về cocktail của chúng ta ở Chương 6. Giao thức CDMA tương tự như việc những người dự tiệc nói bằng nhiều ngôn ngữ; trong những trường hợp như vậy, con người thực sự khá giỏi trong việc khóa cuộc trò chuyện bằng ngôn ngữ mà họ hiểu, đồng thời lọc ra những cuộc trò chuyện còn lại. Ở đây chúng ta thấy rằng CDMA là một giao thức phân vùng trong đó nó phân vùng không gian mã (ngược lại với thời gian hoặc tần số) và gán cho mỗi nút một phần dành riêng của không gian mã.

Cuộc thảo luận của chúng ta ở đây về CDMA nhất thiết phải ngắn gọn; trong thực tế có một số vấn đề khó khăn cần được giải quyết. Đầu tiên, để máy thu CDMA có thể trích xuất tín hiệu của một người gửi cụ thể, mã CDMA phải được chọn cẩn thận. Thứ hai, cuộc thảo luận của chúng ta đã giả định rằng cường độ tín hiệu nhận được từ nhiều người gửi khác nhau là như nhau; trong thực tế, điều này có thể khó đạt được. Có rất nhiều tài liệu đề cập đến những vấn đề này và các vấn đề khác liên quan đến CDMA; xem \[Pickholtz 1982; Viterbi 1995\] để biết chi tiết.

**7.3 WiFi: Mạng LAN không dây 802.11**

Phổ biến ở nơi làm việc, gia đình, cơ sở giáo dục, quán cà phê, sân bay và góc phố, mạng LAN không dây hiện là một trong những công nghệ mạng truy cập quan trọng nhất trên Internet ngày nay. Mặc dù có nhiều công nghệ và tiêu chuẩn cho

*Hình 7.6 ♦ Ví dụ về CDMA hai người gửi*

Người nhận 1

1 1 1

--1 --1--1--1

1 1 1

--1 --1--1--1

Khe thời gian 1 đã nhận được đầu vào

Khe thời gian 0 đã nhận được đầu vào

Bit dữ liệu

Bit dữ liệu

1 1 1

--1 --1--1--1

1 1 1

--1 --1--1--1 Mã

Người gửi

1 1 1

--1

1 1 1

--1

--1 --1

1 1 1 1 1 Mã số

Mã số

\+

--2

2 2 2

--2

--2

2 2 2

--2

Kênh, Zi,m \*

Zi,m di • cm =

Zi,m • cmd

tôi

m=1

M

S

d1 = --1

d0 = 1

d1 = 1

\*

Zi,m di • cm =

d0 = 1

d1 = --1

d0 = 1

Mạng LAN không dây được phát triển vào những năm 1990, một loại tiêu chuẩn cụ thể rõ ràng đã nổi lên là người chiến thắng: mạng LAN không dây IEEE 802.11, còn được gọi là WiFi. Trong phần này, chúng ta sẽ xem xét kỹ các mạng LAN không dây 802.11, kiểm tra cấu trúc khung, giao thức truy cập trung bình và kết nối mạng của các mạng LAN 802.11 với mạng LAN Ethernet có dây.

Như được tóm tắt trong Bảng 7.1, có một số tiêu chuẩn 802.11 \[IEEE 802.11 2020\]. 802.11 b, g, n, ac, ax là các thế hệ tiếp theo của công nghệ 802.11 nhắm đến mạng cục bộ không dây (WLAN), thường có phạm vi dưới 70 m trong môi trường văn phòng tại nhà, nơi làm việc hoặc doanh nghiệp. Các tiêu chuẩn 802.11 n, ac và ax gần đây đã được gắn nhãn tương ứng là WiFi 4, 5 và 6 --- chắc chắn là đang cạnh tranh với nhãn hiệu mạng di động 4G và 5G. Các tiêu chuẩn 802.11 af, ah hoạt động ở khoảng cách xa hơn và nhắm đến Internet of Things, mạng cảm biến và các ứng dụng đo lường.

Các tiêu chuẩn 802.11 b, g, n, ac, ax khác nhau đều có chung một số đặc điểm, bao gồm định dạng khung 802.11 mà chúng ta sẽ nghiên cứu sau đây và tương thích ngược, nghĩa là, chẳng hạn, một thiết bị di động chỉ có khả năng 802.11 g vẫn có thể tương tác với trạm gốc 802.11 ac hoặc 802.11 ax mới hơn. Tất cả chúng đều sử dụng cùng một giao thức truy cập môi trường, CSMA/CA, mà chúng ta cũng sẽ thảo luận ngay sau đây, đồng thời, 802.11 ax cũng hỗ trợ lập lịch tập trung bởi trạm gốc truyền từ các thiết bị không dây liên quan.

Tuy nhiên, như trong Bảng 7.1, các tiêu chuẩn có một số khác biệt lớn ở lớp vật lý. Các thiết bị 802.11 hoạt động ở hai dải tần số khác nhau: 2,4--2,485 GHz (gọi tắt là dải tần 2,4 GHz) và 5,1--5,8 GHz (gọi tắt là dải tần 5 GHz). Dải tần 2,4 GHz là dải tần không được cấp phép, trong đó các thiết bị 802.11 có thể cạnh tranh phổ tần với điện thoại và thiết bị 2,4 GHz như lò vi sóng. Ở tốc độ 5 GHz, mạng LAN 802.11 có khoảng cách truyền ngắn hơn đối với mức công suất nhất định và chịu nhiều ảnh hưởng hơn từ sự lan truyền đa đường. Các tiêu chuẩn 802.11n, 802.11ac và 802.11ax sử dụng nhiều ăng-ten đầu vào nhiều đầu ra (MIMO); nghĩa là, hai hoặc nhiều ăng-ten ở phía gửi và hai hoặc nhiều ăng-ten ở phía nhận đang truyền/nhận các tín hiệu khác nhau

Tiêu chuẩn IEEE 802.11 Năm Tốc độ dữ liệu tối đa Phạm vi Tần số

802.11 b 11 Mb/giây 30 m 2,4 ghz

802,11 g 54 Mb/giây 30 m 2,4 ghz

802.11n (WiFi 4) 70m 2.4, 5GHz

802.11 ac (WiFi 5) 3,47 Gpbs 70 m 5 GHz

Rìu 802.11 (WiFi 6) 2020 (dự kiến) 14 Gbps 70 m 2.4, 5 GHz

802.11 af 35--560 Mbps 1 Km băng tần TV không được sử dụng (54--790 MHz)

802.11 à 347 Mb/giây 1 Km 900 Mhz

Bảng 7.1 ♦ Tóm tắt các tiêu chuẩn IEEE 802.11

\[Diggavi 2004\]. Các trạm gốc 802.11ac và 802.11 ax có thể truyền đồng thời đến nhiều trạm và sử dụng ăng-ten "thông minh" để điều chỉnh dạng chùm tia thích ứng với mục tiêu truyền theo hướng của máy thu. Điều này làm giảm nhiễu và tăng khoảng cách đạt được ở tốc độ dữ liệu nhất định. Tốc độ dữ liệu trong Bảng 7.1 dành cho môi trường lý tưởng hóa, ví dụ: máy thu gần trạm gốc, không bị nhiễu---một kịch bản mà chúng ta khó có thể gặp phải trong thực tế! Như người ta vẫn nói, YMMV: Số dặm của bạn (hoặc trong trường hợp này là tốc độ dữ liệu không dây của bạn) Có thể thay đổi.

**7.3.1 Kiến trúc mạng LAN không dây 802.11**

Hình 7.7 minh họa các thành phần chính của kiến ​​trúc mạng LAN không dây 802.11. Khối xây dựng cơ bản của kiến ​​trúc 802.11 là tập dịch vụ cơ bản (BSS). BSS chứa một hoặc nhiều trạm không dây và trạm cơ sở trung tâm, được gọi là điểm truy cập (AP) theo cách nói của 802.11. Hình 7.7 cho thấy AP trong mỗi BSS kết nối với một thiết bị kết nối (chẳng hạn như bộ chuyển mạch hoặc bộ định tuyến), từ đó dẫn đến Internet. Trong mạng gia đình thông thường, có một AP và một bộ định tuyến (thường được tích hợp với nhau thành một thiết bị) kết nối BSS với Internet.

Giống như các thiết bị Ethernet, mỗi trạm không dây 802.11 có một địa chỉ MAC 6 byte được lưu trong phần sụn của bộ điều hợp của trạm (nghĩa là thẻ giao diện mạng 802.11). Mỗi AP cũng có một địa chỉ MAC cho giao diện không dây của nó. Giống như Ethernet, các địa chỉ MAC này được quản lý bởi IEEE và (về lý thuyết) là duy nhất trên toàn cầu.

Như đã lưu ý trong Phần 7.1, mạng LAN không dây triển khai AP thường được gọi là mạng LAN không dây cơ sở hạ tầng, với "cơ sở hạ tầng" là các AP cùng với

*Hình 7.7 ♦ Kiến trúc mạng LAN IEEE 802.11*

Internet Switch hoặc bộ định tuyến

AP

BSS 1

BSS 2

AP

cơ sở hạ tầng Ethernet có dây kết nối các AP và bộ định tuyến. Hình 7.8 cho thấy các trạm IEEE 802.11 cũng có thể tự nhóm lại với nhau để tạo thành một mạng ad hoc---một mạng không có điều khiển trung tâm và không có kết nối với "thế giới bên ngoài". Ở đây, mạng được hình thành "nhanh chóng" bởi các thiết bị di động ở gần nhau, có nhu cầu liên lạc và không tìm thấy cơ sở hạ tầng mạng hiện có ở vị trí của chúng. Mạng ad hoc có thể được hình thành khi mọi người có máy tính xách tay gặp nhau (ví dụ: trong phòng hội nghị, tàu hỏa hoặc ô tô) và muốn trao đổi dữ liệu khi không có AP tập trung. Đã có sự quan tâm rất lớn đến mạng ad hoc khi các thiết bị di động giao tiếp tiếp tục phát triển. Tuy nhiên, trong phần này chúng ta sẽ tập trung chú ý vào cơ sở hạ tầng mạng LAN không dây.

Kênh và Hiệp hội

Trong 802.11, mỗi trạm không dây cần liên kết với một AP trước khi nó có thể gửi hoặc nhận dữ liệu lớp mạng. Mặc dù tất cả các tiêu chuẩn 802.11 đều sử dụng liên kết nhưng chúng ta sẽ thảo luận cụ thể về chủ đề này trong bối cảnh của IEEE 802.11b, g, n, ac, ax.

Khi quản trị viên mạng cài đặt một AP, quản trị viên sẽ chỉ định Mã nhận dạng bộ dịch vụ (SSID) một hoặc hai từ cho điểm truy cập. (Ví dụ: khi bạn chọn Wi-Fi trong Cài đặt trên iPhone, một danh sách sẽ hiển thị hiển thị SSID của từng AP trong phạm vi.) Quản trị viên cũng phải chỉ định số kênh cho AP. Để hiểu số kênh, hãy nhớ lại rằng 802.11 hoạt động ở dải tần từ 2,4 GHz đến 2,4835 GHz. Trong băng tần 85 MHz này, 802.11 xác định 11 kênh chồng chéo một phần. Hai kênh bất kỳ không chồng chéo khi và chỉ khi chúng được phân tách bằng bốn kênh trở lên. Đặc biệt, bộ kênh 1, 6 và 11 là bộ duy nhất gồm 3 kênh không chồng chéo. Điều này có nghĩa là quản trị viên có thể tạo một mạng LAN không dây với tốc độ truyền tối đa tổng hợp gấp ba lần tốc độ truyền tối đa được hiển thị trong Bảng 7.1 bằng cách cài đặt ba AP 802.11 tại cùng một vị trí vật lý, gán các kênh 1, 6 và 11 cho các AP và kết nối từng AP bằng một bộ chuyển mạch.

*Hình 7.8 ♦ Mạng ad hoc IEEE 802.11*

BSS

Bây giờ chúng ta đã có hiểu biết cơ bản về các kênh 802.11, hãy mô tả một tình huống thú vị (và không hoàn toàn hiếm gặp)---đó là tình huống có nhiều WiFi. Khu rừng WiFi là bất kỳ vị trí vật lý nào nơi trạm không dây nhận được tín hiệu đủ mạnh từ hai AP trở lên. Ví dụ: ở nhiều quán cà phê ở Thành phố New York, một trạm không dây có thể nhận tín hiệu từ nhiều AP gần đó. Một trong những AP có thể được quản lý bởi quán cà phê, trong khi những AP khác có thể ở trong các căn hộ dân cư gần quán cà phê. Mỗi AP này có thể nằm trong một mạng con IP khác nhau và sẽ được chỉ định một kênh độc lập.

Bây giờ, giả sử bạn bước vào một khu rừng WiFi như vậy bằng điện thoại thông minh, máy tính bảng hoặc máy tính xách tay của mình, tìm kiếm quyền truy cập Internet không dây và một chiếc bánh nướng xốp việt quất. Giả sử có năm AP trong khu vực WiFi. Để có quyền truy cập Internet, thiết bị không dây của bạn cần tham gia chính xác một trong các mạng con và do đó cần liên kết với chính xác một trong các AP. Liên kết có nghĩa là thiết bị không dây tạo ra một dây ảo giữa chính nó và AP. Cụ thể, chỉ AP được liên kết mới gửi các khung dữ liệu (nghĩa là các khung chứa dữ liệu, chẳng hạn như datagram) đến thiết bị không dây của bạn và thiết bị không dây của bạn sẽ chỉ gửi các khung dữ liệu vào Internet thông qua AP được liên kết. Nhưng làm cách nào để thiết bị không dây của bạn liên kết với một AP cụ thể? Và cơ bản hơn, làm thế nào để thiết bị không dây của bạn biết những AP nào, nếu có, đang ở trong rừng?

Chuẩn 802.11 yêu cầu AP gửi định kỳ các khung báo hiệu, mỗi khung bao gồm địa chỉ SSID và MAC của AP. Thiết bị không dây của bạn biết rằng các AP đang gửi các khung báo hiệu, sẽ quét 11 kênh, tìm kiếm các khung báo hiệu từ bất kỳ AP nào có thể ở ngoài đó (một số trong số đó có thể đang truyền trên cùng một kênh---ngoài kia là một khu rừng rậm!). Sau khi tìm hiểu về các AP có sẵn từ các khung báo hiệu, bạn (hoặc thiết bị không dây của bạn) chọn một trong các AP để liên kết.

Tiêu chuẩn 802.11 không chỉ định thuật toán để chọn AP có sẵn nào để liên kết; thuật toán đó được giao cho các nhà thiết kế chương trình cơ sở và phần mềm 802.11 trong thiết bị không dây của bạn. Thông thường, thiết bị chọn AP có khung báo hiệu được nhận với cường độ tín hiệu cao nhất. Mặc dù cường độ tín hiệu cao là tốt (xem ví dụ: Hình 7.3), cường độ tín hiệu không phải là đặc tính AP duy nhất sẽ xác định hiệu suất mà thiết bị nhận được. Cụ thể, có thể AP được chọn có thể có tín hiệu mạnh nhưng có thể bị quá tải với các thiết bị liên kết khác (cần chia sẻ băng thông không dây tại AP đó), trong khi AP không tải không được chọn do tín hiệu yếu hơn một chút. Do đó, một số cách lựa chọn AP khác gần đây đã được đề xuất \[Vasudevan 2005; Nicholson 2006; Sundaresan 2006\]. Để có cuộc thảo luận thú vị và thực tế về cách đo cường độ tín hiệu, hãy xem \[Bardwell 2004\].

Quá trình quét kênh và lắng nghe các khung báo hiệu được gọi là quét thụ động (xem Hình 7.9a). Một thiết bị không dây cũng có thể thực hiện chức năng quét tích cực bằng cách phát sóng khung thăm dò mà tất cả các AP trong phạm vi của thiết bị không dây sẽ nhận được, như trong Hình 7.9b. Các AP phản hồi khung yêu cầu thăm dò bằng khung phản hồi thăm dò. Sau đó, thiết bị không dây có thể chọn AP để liên kết trong số các AP phản hồi.

*Hình 7.9 ♦ Quét chủ động và thụ động các điểm truy cập*

H1

AP 2 AP 1

BBS 1

Một. Quét thụ động

1\. Khung báo hiệu được gửi từ các AP 2. Khung yêu cầu liên kết đã gửi: H1 đến AP đã chọn 3. Khung phản hồi liên kết đã gửi: AP đã chọn đến H1

Một. Đang quét 1. Phát khung yêu cầu thăm dò từ H1 2. Khung phản hồi thăm dò được gửi từ các AP 3. Khung yêu cầu liên kết đã gửi: H1 đến AP đã chọn 4. Khung phản hồi liên kết đã gửi: AP đã chọn đến H1

BBS 2

H1

AP 2 AP 1

BBS 1 BBS 2

Sau khi chọn AP để liên kết, thiết bị không dây sẽ gửi khung yêu cầu liên kết đến AP và AP sẽ phản hồi bằng khung phản hồi liên kết. Lưu ý rằng bắt tay yêu cầu/phản hồi thứ hai này là cần thiết khi quét chủ động, vì AP phản hồi khung yêu cầu thăm dò ban đầu không biết AP nào trong số (có thể nhiều) AP phản hồi mà thiết bị sẽ chọn liên kết, giống như cách mà máy khách DHCP có thể chọn trong số nhiều máy chủ DHCP (xem Hình 4.21). Sau khi được liên kết với một AP, thiết bị sẽ muốn tham gia mạng con (theo nghĩa địa chỉ IP của Mục 4.3.3) mà AP thuộc về. Do đó, thiết bị thường sẽ gửi tin nhắn khám phá DHCP (xem Hình 4.21) vào mạng con thông qua AP để lấy địa chỉ IP trên mạng con. Sau khi có được địa chỉ, phần còn lại của thế giới sẽ xem thiết bị đó đơn giản như một máy chủ khác có địa chỉ IP trong mạng con đó.

Để tạo liên kết với một AP cụ thể, thiết bị không dây có thể được yêu cầu xác thực chính nó với AP. Mạng LAN không dây 802.11 cung cấp một số lựa chọn thay thế để xác thực và truy cập. Một cách tiếp cận được nhiều công ty sử dụng là cho phép truy cập vào mạng không dây dựa trên địa chỉ MAC của thiết bị. Cách tiếp cận thứ hai, được nhiều quán cà phê Internet sử dụng, sử dụng tên người dùng và mật khẩu. Trong cả hai trường hợp, AP thường liên lạc với máy chủ xác thực, chuyển tiếp thông tin giữa thiết bị không dây và máy chủ xác thực bằng giao thức như RADIUS \[RFC 2865\] hoặc DIAMETER \[RFC 6733\]. Việc tách máy chủ xác thực khỏi AP cho phép một máy chủ xác thực phục vụ nhiều AP, tập trung các quyết định xác thực và truy cập (thường nhạy cảm) trong một máy chủ duy nhất và giữ

Chi phí AP và độ phức tạp thấp. Chúng ta sẽ thấy trong chương 8 rằng giao thức IEEE 802.11i mới xác định các khía cạnh bảo mật của họ giao thức 802.11 thực hiện chính xác cách tiếp cận này.

**7.3.2 Giao thức MAC 802.11**

Khi thiết bị không dây được liên kết với AP, nó có thể bắt đầu gửi và nhận các khung dữ liệu đến và đi từ điểm truy cập. Nhưng vì nhiều thiết bị không dây hoặc bản thân AP có thể muốn truyền các khung dữ liệu cùng lúc trên cùng một kênh nên cần có giao thức đa truy cập để điều phối việc truyền. Trong phần sau, chúng tôi sẽ gọi các thiết bị hoặc AP là các "trạm" không dây chia sẻ kênh đa truy cập. Như đã thảo luận trong Chương 6 và Phần 7.2.1, nói chung có ba loại giao thức đa truy cập: phân vùng kênh (bao gồm CDMA), truy cập ngẫu nhiên và thay phiên nhau. Lấy cảm hứng từ sự thành công to lớn của Ethernet và giao thức truy cập ngẫu nhiên của nó, các nhà thiết kế 802.11 đã chọn giao thức truy cập ngẫu nhiên cho mạng LAN không dây 802.11. Giao thức truy cập ngẫu nhiên này được gọi là CSMA với tính năng tránh xung đột hoặc ngắn gọn hơn là CSMA/CA. Giống như CSMA/CD của Ethernet, "CSMA" trong CSMA/CA là viết tắt của "đa truy cập cảm nhận sóng mang", nghĩa là mỗi trạm sẽ cảm nhận kênh trước khi truyền và không truyền khi kênh cảm thấy bận. Mặc dù cả Ethernet và 802.11 đều sử dụng truy cập ngẫu nhiên cảm biến sóng mang, hai giao thức MAC có những khác biệt quan trọng. Đầu tiên, thay vì sử dụng phát hiện va chạm, 802.11 sử dụng kỹ thuật tránh va chạm. Thứ hai, do tỷ lệ lỗi bit tương đối cao của các kênh không dây, 802.11 (không giống Ethernet) sử dụng sơ đồ xác nhận/truyền lại lớp liên kết (ARQ). Chúng tôi sẽ mô tả các sơ đồ xác nhận lớp liên kết và tránh xung đột của 802.11 bên dưới.

Hãy nhớ lại Phần 6.3.2 và 6.4.2 rằng với thuật toán phát hiện xung đột của Ethernet, trạm Ethernet sẽ lắng nghe kênh khi nó truyền. Nếu trong khi truyền, nó phát hiện ra một trạm khác cũng đang truyền, nó sẽ hủy truyền và cố gắng truyền lại sau khi đợi một khoảng thời gian nhỏ ngẫu nhiên. Không giống như giao thức Ethernet 802.3, giao thức MAC 802.11 không thực hiện phát hiện xung đột. Có hai lý do quan trọng cho việc này:

• Khả năng phát hiện xung đột đòi hỏi khả năng gửi (tín hiệu riêng của trạm) và nhận (để xác định xem trạm khác có đang truyền) cùng một lúc hay không. Do cường độ tín hiệu thu được thường rất nhỏ so với cường độ tín hiệu truyền đi ở bộ chuyển đổi 802.11 nên việc xây dựng phần cứng có thể phát hiện xung đột sẽ rất tốn kém. • Quan trọng hơn, ngay cả khi bộ chuyển đổi có thể truyền và nghe cùng lúc (và có thể hủy bỏ việc truyền khi nó cảm nhận được kênh bận), bộ chuyển đổi vẫn không thể phát hiện tất cả các xung đột, do vấn đề đầu cuối ẩn và mờ dần, như đã thảo luận trong Phần 7.2.

Bởi vì mạng LAN không dây 802.11 không sử dụng tính năng phát hiện xung đột nên khi một trạm bắt đầu truyền một khung, nó sẽ truyền toàn bộ khung đó; nghĩa là, từng là một nhà ga

*Hình 7.10 ♦ 802.11 sử dụng các xác nhận lớp liên kết*

Điểm đến

DIFS

SIFS

dữ liệu

ách

Nguồn

đã bắt đầu thì không có đường quay lại. Như người ta có thể mong đợi, việc truyền toàn bộ khung hình (đặc biệt là các khung hình dài) khi xảy ra xung đột có thể làm giảm đáng kể hiệu suất của giao thức đa truy cập. Để giảm khả năng xảy ra xung đột, 802.11 sử dụng một số kỹ thuật tránh xung đột mà chúng ta sẽ thảo luận ngay sau đây. Tuy nhiên, trước khi xem xét việc tránh xung đột, trước tiên chúng ta cần kiểm tra sơ đồ xác nhận lớp liên kết của 802.11. Hãy nhớ lại Phần 7.2 rằng khi một trạm trong mạng LAN không dây gửi một khung, khung đó có thể không đến được trạm đích một cách nguyên vẹn vì nhiều lý do. Để giải quyết khả năng thất bại không đáng kể này, giao thức MAC 802.11 sử dụng các xác nhận của lớp liên kết. Như được hiển thị trong Hình 7.10, khi trạm đích nhận được một khung vượt qua CRC, nó sẽ đợi một khoảng thời gian ngắn được gọi là Khoảng cách giữa các khung ngắn (SIFS) và sau đó gửi lại khung xác nhận. Nếu trạm truyền không nhận được xác nhận trong một khoảng thời gian nhất định, nó sẽ cho rằng đã xảy ra lỗi và truyền lại khung bằng giao thức CSMA/CA để truy cập kênh. Nếu không nhận được xác nhận sau một số lần truyền lại cố định, trạm phát sẽ từ bỏ và loại bỏ khung.

Sau khi thảo luận về cách 802.11 sử dụng các xác nhận của lớp liên kết, giờ đây chúng ta đã có thể mô tả giao thức 802.11 CSMA/CA. Giả sử rằng một trạm (thiết bị không dây hoặc AP) có khung để truyền.

1\. Nếu ban đầu trạm cảm nhận được kênh nhàn rỗi, nó sẽ truyền khung của nó sau một

khoảng thời gian ngắn được gọi là Không gian liên khung phân tán (DIFS); xem Hình 7.10. 2. Mặt khác, trạm chọn giá trị độ trễ ngẫu nhiên bằng cách sử dụng số mũ nhị phân

thời gian chờ (như chúng ta đã gặp trong Phần 6.3.2) và đếm ngược giá trị này sau DIFS khi kênh được cảm nhận là không hoạt động. Trong khi kênh được cảm nhận là bận, giá trị bộ đếm vẫn bị đóng băng. 3. Khi bộ đếm đạt đến 0 (lưu ý rằng điều này chỉ có thể xảy ra khi bộ đếm

nel được cảm nhận là không hoạt động), trạm sẽ truyền toàn bộ khung và sau đó chờ xác nhận. 4. Nếu nhận được một xác nhận, trạm phát sẽ biết rằng khung của nó

đã được nhận chính xác tại trạm đích. Nếu trạm có một khung khác để gửi, nó sẽ bắt đầu giao thức CSMA/CA ở bước 2. Nếu không nhận được xác nhận, trạm truyền sẽ quay lại giai đoạn quay lại ở bước 2, với giá trị ngẫu nhiên được chọn từ một khoảng thời gian lớn hơn.

Hãy nhớ lại rằng trong giao thức đa truy cập CSMA/CD của Ethernet (Phần 6.3.2), một trạm bắt đầu truyền ngay khi kênh được cảm nhận là không hoạt động. Tuy nhiên, với CSMA/CA, trạm sẽ không truyền trong khi đếm ngược, ngay cả khi nó cảm nhận được kênh đang rảnh. Tại sao CSMA/CD và CDMA/CA lại áp dụng những cách tiếp cận khác nhau ở đây?

Để trả lời câu hỏi này, hãy xem xét một tình huống trong đó hai trạm đều có một khung dữ liệu để truyền, nhưng không có trạm nào truyền ngay lập tức vì mỗi trạm đều cảm nhận được rằng trạm thứ ba đã truyền. Với CSMA/CD của Ethernet, hai trạm sẽ truyền tải ngay khi chúng phát hiện ra rằng trạm thứ ba đã truyền xong. Điều này sẽ gây ra xung đột, đây không phải là vấn đề nghiêm trọng trong CSMA/CD, vì cả hai trạm sẽ hủy quá trình truyền và do đó tránh được việc truyền vô ích các phần còn lại trong khung của chúng. Tuy nhiên, trong 802.11, tình hình lại hoàn toàn khác. Vì 802.11 không phát hiện xung đột và hủy bỏ quá trình truyền nên toàn bộ khung bị xung đột sẽ được truyền đi toàn bộ. Do đó, mục tiêu của 802.11 là tránh xung đột bất cứ khi nào có thể. Trong 802.11, nếu hai trạm cảm thấy kênh bận, cả hai đều ngay lập tức chuyển sang thời gian chờ ngẫu nhiên, hy vọng chọn được các giá trị thời gian chờ khác nhau. Nếu các giá trị này thực sự khác nhau thì khi kênh không hoạt động, một trong hai trạm sẽ bắt đầu truyền trước trạm kia và (nếu hai trạm không bị ẩn với nhau) "trạm thua" sẽ nghe thấy tín hiệu của "trạm chiến thắng", đóng băng bộ đếm của nó và không truyền cho đến khi trạm chiến thắng hoàn thành việc truyền. Bằng cách này, tránh được va chạm tốn kém. Tất nhiên, xung đột vẫn có thể xảy ra với 802.11 trong trường hợp này: Hai trạm có thể bị ẩn khỏi nhau hoặc hai trạm có thể chọn ngẫu nhiên

các giá trị độ trễ đủ gần để đường truyền từ trạm bắt đầu đầu tiên vẫn chưa đến được trạm thứ hai. Hãy nhớ lại rằng chúng ta đã gặp phải vấn đề này trước đó trong cuộc thảo luận về các thuật toán truy cập ngẫu nhiên trong bối cảnh Hình 6.12.

Xử lý các thiết bị đầu cuối ẩn: RTS và CTS

Giao thức MAC 802.11 cũng bao gồm một sơ đồ đặt trước tiện lợi (nhưng tùy chọn) giúp tránh xung đột ngay cả khi có các thiết bị đầu cuối ẩn. Hãy cùng tìm hiểu sơ đồ này trong bối cảnh của Hình 7.11, minh họa hai trạm không dây và một điểm truy cập. Cả hai trạm không dây đều nằm trong phạm vi phủ sóng của AP (có phạm vi phủ sóng được hiển thị dưới dạng vòng tròn bóng mờ) và cả hai đều được liên kết với AP. Tuy nhiên, do bị mờ dần, phạm vi tín hiệu của các trạm không dây bị giới hạn ở bên trong các vòng tròn được tô bóng như trong Hình 7.11. Do đó, mỗi trạm không dây đều bị ẩn với trạm kia, mặc dù không trạm nào bị ẩn khỏi AP.

Bây giờ chúng ta hãy xem tại sao các thiết bị đầu cuối ẩn có thể có vấn đề. Giả sử Trạm H1 đang truyền một khung và đang truyền một nửa khung của H1, Trạm H2 muốn gửi một khung đến AP. H2, không nghe thấy đường truyền từ H1, trước tiên sẽ đợi một khoảng DIFS rồi mới truyền khung, dẫn đến xung đột. Do đó, kênh sẽ bị lãng phí trong toàn bộ thời gian truyền H1 cũng như trong quá trình truyền H2.

Để tránh vấn đề này, giao thức IEEE 802.11 cho phép một trạm sử dụng khung điều khiển Yêu cầu gửi (RTS) ngắn và khung điều khiển Clear to Send (CTS) ngắn để dành quyền truy cập vào kênh. Khi người gửi muốn gửi khung DATA, trước tiên nó có thể gửi khung RTS đến AP, cho biết tổng thời gian cần thiết để truyền khung DATA và khung xác nhận (ACK). Khi AP nhận được khung RTS, nó sẽ phản hồi bằng cách phát khung CTS. Khung CTS này

*Hình 7.11 ♦ Ví dụ về thiết bị đầu cuối ẩn: H1 bị ẩn khỏi H2 và*

ngược lại

AP H1 H2

phục vụ hai mục đích: Nó cung cấp cho người gửi quyền rõ ràng để gửi và cũng hướng dẫn các trạm khác không gửi trong khoảng thời gian dành riêng.

Do đó, trong Hình 7.12, trước khi truyền khung DATA, H1 trước tiên sẽ phát khung RTS, khung này được tất cả các trạm trong vòng kết nối của nó nghe thấy, bao gồm cả AP. Sau đó, AP sẽ phản hồi bằng khung CTS, khung này được tất cả các trạm trong phạm vi phủ sóng của nó nghe thấy, bao gồm cả H1 và H2. Trạm H2, sau khi nghe thấy CTS, sẽ ngừng truyền trong khoảng thời gian được chỉ định trong khung CTS. Các khung RTS, CTS, DATA và ACK được hiển thị trong Hình 7.12.

*Hình 7.12 ♦ Tránh va chạm bằng khung RTS và CTS*

Đích Tất cả các nút khác

Trì hoãn quyền truy cập

Nguồn

DIFS

ACK

SIFS

SIFS

SIFS

DỮ LIỆU

CTS

CTS

ACK

RTS

Việc sử dụng khung RTS và CTS có thể cải thiện hiệu suất theo hai cách quan trọng:

• Vấn đề về trạm ẩn được giảm thiểu do khung DATA dài chỉ được truyền sau khi kênh đã được đặt trước. • Bởi vì khung RTS và CTS ngắn, nên xung đột liên quan đến khung RTS hoặc CTS sẽ chỉ kéo dài trong khoảng thời gian của khung RTS hoặc CTS ngắn. Khi các khung RTS và CTS được truyền chính xác, các khung DATA và ACK sau sẽ được truyền mà không bị xung đột.

Bạn được khuyến khích xem hoạt hình 802.11 trên trang Web của sách giáo khoa. Hoạt hình tương tác này minh họa giao thức CSMA/CA, bao gồm chuỗi trao đổi RTS/CTS.

Mặc dù trao đổi RTS/CTS có thể giúp giảm xung đột nhưng nó cũng gây ra độ trễ và tiêu tốn tài nguyên kênh. Vì lý do này, trao đổi RTS/CTS chỉ được sử dụng (nếu có) để dành kênh cho việc truyền khung DATA dài. Trong thực tế, mỗi trạm không dây có thể đặt ngưỡng RTS sao cho chuỗi RTS/CTS chỉ được sử dụng khi khung dài hơn ngưỡng. Đối với nhiều trạm không dây, giá trị ngưỡng RTS mặc định lớn hơn độ dài khung tối đa, do đó chuỗi RTS/CTS bị bỏ qua đối với tất cả các khung DATA được gửi.

Sử dụng 802.11 làm liên kết điểm-điểm

Cuộc thảo luận của chúng ta cho đến nay đã tập trung vào việc sử dụng 802.11 trong cài đặt đa truy cập. Chúng ta nên đề cập rằng nếu hai nút đều có ăng-ten định hướng, chúng có thể hướng ăng-ten định hướng của chúng vào nhau và chạy giao thức 802.11 qua cái về cơ bản là liên kết điểm-điểm. Do chi phí thấp của phần cứng thông thường 802.11, việc sử dụng ăng-ten định hướng và công suất truyền dẫn tăng lên cho phép 802.11 được sử dụng như một phương tiện rẻ tiền để cung cấp các kết nối điểm-điểm không dây trên khoảng cách hàng chục km. \[Raman 2007\] mô tả một trong những mạng không dây đa bước nhảy đầu tiên như vậy, hoạt động ở vùng đồng bằng nông thôn sông Hằng ở Ấn Độ bằng cách sử dụng các liên kết điểm-điểm 802.11.

**7.3.3 IEEE 802.11 Frame**

Mặc dù khung 802.11 có nhiều điểm tương đồng với khung Ethernet nhưng nó cũng chứa một số trường dành riêng cho việc sử dụng nó cho các liên kết không dây. Khung 802.11 được hiển thị trong Hình 7.13. Các số phía trên mỗi trường trong khung biểu thị độ dài của các trường tính bằng byte; các số phía trên mỗi trường con trong trường điều khiển khung biểu thị độ dài của các trường con tính bằng bit. Bây giờ chúng ta hãy kiểm tra các trường trong khung cũng như một số trường con quan trọng hơn trong trường điều khiển của khung.

Payload và trường CRC

Trọng tâm của khung là tải trọng, thường bao gồm gói dữ liệu IP hoặc gói ARP. Mặc dù trường này được phép dài tới 2.312 byte, nhưng nó

thường ít hơn 1.500 byte, chứa gói dữ liệu IP hoặc gói ARP. Giống như khung Ethernet, khung 802.11 bao gồm kiểm tra dự phòng theo chu kỳ 32 bit (CRC) để bộ thu có thể phát hiện các lỗi bit trong khung nhận được. Như chúng ta đã thấy, lỗi bit phổ biến hơn nhiều trong mạng LAN không dây so với mạng LAN có dây, do đó CRC thậm chí còn hữu ích hơn ở đây.

Trường địa chỉ

Có lẽ sự khác biệt nổi bật nhất trong khung 802.11 là nó có bốn trường địa chỉ, mỗi trường có thể chứa một địa chỉ MAC 6 byte. Nhưng tại sao lại có bốn trường địa chỉ? Trường MAC nguồn và trường MAC đích không đủ như đối với Ethernet? Hóa ra là cần có ba trường địa chỉ cho mục đích liên mạng---cụ thể là để di chuyển gói dữ liệu lớp mạng từ trạm không dây qua AP tới giao diện bộ định tuyến. Trường địa chỉ thứ tư được sử dụng khi các AP chuyển tiếp khung hình cho nhau ở chế độ đặc biệt. Vì chúng ta chỉ xem xét mạng lưới cơ sở hạ tầng ở đây nên hãy tập trung chú ý vào ba trường địa chỉ đầu tiên. Chuẩn 802.11 định nghĩa các trường này như sau:

• Địa chỉ 2 là địa chỉ MAC của trạm truyền khung. Do đó, nếu một trạm không dây truyền khung, địa chỉ MAC của trạm đó sẽ được chèn vào trường địa chỉ 2. Tương tự, nếu một AP truyền khung, địa chỉ MAC của AP sẽ được chèn vào trường địa chỉ 2.

• Địa chỉ 1 là địa chỉ MAC của trạm không dây nhận khung. Do đó, nếu trạm không dây di động truyền khung, địa chỉ 1 chứa địa chỉ MAC của AP đích. Tương tự, nếu một AP truyền khung, địa chỉ 1 chứa địa chỉ MAC của trạm không dây đích. • Để hiểu địa chỉ 3, hãy nhớ lại rằng BSS (bao gồm AP và các trạm không dây) là một phần của mạng con và mạng con này kết nối với các mạng con khác thông qua một số giao diện bộ định tuyến. Địa chỉ 3 chứa địa chỉ MAC của giao diện bộ định tuyến này.

*Hình 7.13 ♦ Khung 802.11*

Frame điều khiển

0-2312 Frame (các số biểu thị độ dài trường tính bằng byte):

Địa chỉ

Thời lượng Payload CRC

Giao thức

phiên bản

tới AP

Từ

AP

Hơn

mảnh vỡ

Quyền lực

quản lý

Hơn

dữ liệu

Địa chỉ

Địa chỉ

Địa chỉ

Kiểm soát tuần tự

Loại Loại phụ Thử lại WEP Rsvd

Frame trường điều khiển được mở rộng (các số biểu thị độ dài trường tính bằng bit):

Để hiểu rõ hơn về mục đích của địa chỉ 3, chúng ta hãy xem qua một ví dụ về liên mạng trong bối cảnh Hình 7.14. Trong hình này, có hai AP, mỗi AP chịu trách nhiệm cho một số trạm không dây. Mỗi AP có kết nối trực tiếp với bộ định tuyến, từ đó kết nối với Internet toàn cầu. Chúng ta nên nhớ rằng AP là một thiết bị lớp liên kết và do đó không "nói" IP cũng như không hiểu địa chỉ IP. Bây giờ hãy xem xét việc di chuyển một datagram từ giao diện bộ định tuyến R1 sang Trạm không dây H1. Bộ định tuyến không biết rằng có một AP giữa nó và H1; từ góc độ của bộ định tuyến, H1 chỉ là một máy chủ trong một trong các mạng con mà nó (bộ định tuyến) được kết nối.

• Bộ định tuyến biết địa chỉ IP của H1 (từ địa chỉ đích của datagram), sử dụng ARP để xác định địa chỉ MAC của H1, giống như trong mạng LAN Ethernet thông thường. Sau khi có được địa chỉ MAC của H1, giao diện bộ định tuyến R1 sẽ đóng gói datagram trong khung Ethernet. Trường địa chỉ nguồn của khung này chứa địa chỉ MAC của R1 và trường địa chỉ đích chứa địa chỉ MAC của H1. • Khi khung Ethernet đến AP, AP sẽ chuyển đổi khung Ethernet 802.3 thành khung 802.11 trước khi truyền khung này vào kênh không dây. AP điền địa chỉ 1 và địa chỉ 2 bằng địa chỉ MAC của H1 và địa chỉ MAC của chính nó, tương ứng như mô tả ở trên. Đối với địa chỉ 3, AP sẽ chèn địa chỉ MAC của R1. Bằng cách này, H1 có thể xác định (từ địa chỉ 3) địa chỉ MAC của giao diện bộ định tuyến đã gửi datagram vào mạng con.

*Hình 7.14 ♦ Việc sử dụng các trường địa chỉ trong khung 802.11: Gửi khung*

giữa H1 và R1

Internet Router

AP H1 R1

BSS 1

BSS 2

AP

Bây giờ hãy xem xét điều gì xảy ra khi trạm không dây H1 phản hồi bằng cách di chuyển datagram từ H1 sang R1.

• H1 tạo một khung 802.11, điền vào các trường cho địa chỉ 1 và địa chỉ 2 bằng địa chỉ MAC của AP và địa chỉ MAC của H1 tương ứng như mô tả ở trên. Đối với địa chỉ 3, H1 chèn địa chỉ MAC của R1. • Khi AP nhận được khung 802.11, nó sẽ chuyển khung này thành khung Ethernet. Trường địa chỉ nguồn cho khung này là địa chỉ MAC của H1 và trường địa chỉ đích là địa chỉ MAC của R1. Do đó, địa chỉ 3 cho phép AP xác định địa chỉ MAC đích thích hợp khi xây dựng khung Ethernet.

Tóm lại, địa chỉ 3 đóng vai trò quan trọng trong việc kết nối mạng BSS với mạng LAN có dây.

Các trường điều khiển Số thứ tự, Thời lượng và Frame

Hãy nhớ lại rằng trong 802.11, bất cứ khi nào một trạm nhận được khung hình từ một trạm khác một cách chính xác, nó sẽ gửi lại một xác nhận. Vì các xác nhận có thể bị thất lạc nên trạm gửi có thể gửi nhiều bản sao của một khung nhất định. Như chúng ta đã thấy trong phần thảo luận về giao thức rdt2.1 (Phần 3.4.1), việc sử dụng số thứ tự cho phép máy thu phân biệt giữa khung mới được truyền và khung truyền lại của khung trước đó. Do đó, trường số thứ tự trong khung 802.11 phục vụ chính xác mục đích tương tự ở lớp liên kết giống như ở lớp vận chuyển ở Chương 3.

Hãy nhớ lại rằng giao thức 802.11 cho phép trạm phát dự trữ kênh trong một khoảng thời gian bao gồm thời gian truyền khung dữ liệu của nó và thời gian truyền xác nhận. Giá trị thời lượng này được bao gồm trong trường thời lượng của khung (cả đối với khung dữ liệu và khung RTS và CTS).

Như được hiển thị trong Hình 7.13, trường điều khiển khung bao gồm nhiều trường con. Chúng tôi sẽ chỉ nói vài lời về một số trường con quan trọng hơn; để có cuộc thảo luận đầy đủ hơn, bạn nên tham khảo đặc tả 802.11 \[Held 2001; Quạ 1997; IEEE 802.11 1999\]. Các trường loại và loại phụ được sử dụng để phân biệt các khung liên kết, RTS, CTS, ACK và dữ liệu. Các trường đến và từ được sử dụng để xác định ý nghĩa của các trường địa chỉ khác nhau. (Những ý nghĩa này thay đổi tùy thuộc vào việc sử dụng chế độ ad hoc hay chế độ cơ sở hạ tầng, và trong trường hợp chế độ cơ sở hạ tầng, trạm không dây hay AP đang gửi khung.) Cuối cùng, trường WEP cho biết liệu mã hóa có được sử dụng hay không (WEP sẽ được thảo luận trong Chương 8).

**7.3.4 Tính di động giống nhau IP Subnet**

Để tăng phạm vi vật lý của mạng LAN không dây, các công ty và trường đại học thường triển khai nhiều BSS trong cùng một mạng con IP. Điều này tự nhiên làm nảy sinh vấn đề về tính di động giữa các BSS---làm thế nào để các trạm không dây di chuyển liền mạch từ BSS này sang BSS khác trong khi vẫn duy trì các phiên TCP đang diễn ra? Như chúng ta sẽ thấy trong phần này, tính di động có thể được xử lý một cách tương đối đơn giản khi các BSS là một phần

của mạng con. Khi các trạm di chuyển giữa các mạng con, sẽ cần đến các giao thức quản lý di động phức tạp hơn, chẳng hạn như những giao thức chúng ta sẽ nghiên cứu trong Phần 7.5 và 7.6.

Bây giờ chúng ta hãy xem một ví dụ cụ thể về tính di động giữa các BSS trong cùng một mạng con. Hình 7.15 cho thấy hai BSS được kết nối với nhau với một máy chủ H1, chuyển từ BSS1 sang BSS2. Vì trong ví dụ này, thiết bị kết nối kết nối hai BSS không phải là bộ định tuyến nên tất cả các trạm trong hai BSS, bao gồm cả các AP, đều thuộc cùng một mạng con IP. Do đó, khi H1 chuyển từ BSS1 sang BSS2, nó có thể giữ địa chỉ IP và tất cả các kết nối TCP đang diễn ra của nó. Nếu thiết bị kết nối là một bộ định tuyến thì H1 sẽ phải lấy địa chỉ IP mới trong mạng con mà nó đang di chuyển. Việc thay đổi địa chỉ này sẽ làm gián đoạn (và cuối cùng chấm dứt) mọi kết nối TCP đang diễn ra tại H1. Trong Phần 7.6, chúng ta sẽ thấy cách sử dụng giao thức di động lớp mạng, chẳng hạn như di động IP, để tránh vấn đề này.

Nhưng điều gì cụ thể xảy ra khi H1 chuyển từ BSS1 sang BSS2? Khi H1 rời khỏi AP1, H1 phát hiện tín hiệu yếu đi từ AP1 và bắt đầu quét tìm tín hiệu mạnh hơn. H1 nhận các khung báo hiệu từ AP2 (trong nhiều môi trường công ty và trường đại học sẽ có cùng SSID với AP1). Sau đó, H1 tách liên kết với AP1 và liên kết với AP2, trong khi vẫn giữ địa chỉ IP của nó và duy trì các phiên TCP đang diễn ra.

Điều này giải quyết vấn đề chuyển giao từ quan điểm của máy chủ và AP. Nhưng còn công tắc trong Hình 7.15 thì sao? Làm sao nó biết rằng máy chủ đã chuyển từ AP này sang AP khác? Như bạn có thể nhớ lại trong Chương 6, các switch "tự học" và tự động xây dựng các bảng chuyển tiếp của chúng. Tính năng tự học này xử lý tốt các chuyển động không thường xuyên (ví dụ: khi nhân viên được chuyển từ bộ phận này sang bộ phận khác); tuy nhiên, bộ chuyển mạch không được thiết kế để hỗ trợ người dùng có tính di động cao muốn duy trì kết nối TCP trong khi di chuyển giữa các BSS. Để đánh giá vấn đề ở đây, hãy nhớ lại rằng trước khi di chuyển, bộ chuyển mạch có một mục trong bảng chuyển tiếp ghép nối địa chỉ MAC của H1 với giao diện bộ chuyển mạch đi qua đó có thể tiếp cận H1. Nếu H1 ban đầu nằm trong BSS1 thì datagram có đích đến H1 sẽ được chuyển hướng đến H1 thông qua AP1. Tuy nhiên, khi H1 liên kết với BSS2, các khung của nó sẽ được chuyển hướng tới AP2. Một giải pháp (thực sự hơi khó khăn) là AP2 gửi khung Ethernet quảng bá có địa chỉ nguồn của H1 tới bộ chuyển mạch ngay sau đó.

*Hình 7.15 ♦ Tính di động trong cùng một mạng con*

BSS 1 BSS 2

H1

Switch

AP 1 AP 2

hiệp hội mới. Khi switch nhận được khung, nó sẽ cập nhật bảng chuyển tiếp, cho phép truy cập H1 thông qua AP2. Nhóm tiêu chuẩn 802.11f đang phát triển giao thức liên AP để xử lý những vấn đề này và các vấn đề liên quan.

Cuộc thảo luận của chúng tôi ở trên đã tập trung vào tính di động với cùng mạng con LAN. Hãy nhớ lại rằng các VLAN mà chúng ta đã nghiên cứu trong Phần 6.4.4 có thể được sử dụng để kết nối các nhóm mạng LAN lại với nhau thành một mạng LAN ảo lớn có thể trải rộng trên một khu vực địa lý rộng lớn. Tính di động giữa các trạm cơ sở trong một VLAN như vậy có thể được xử lý theo cách tương tự như trên \[Yu 2011\].

KHÁM PHÁ VỊ TRÍ: ĐỊNH VỊ GPS VÀ WIFI

Nhiều ứng dụng điện thoại thông minh hữu ích và quan trọng nhất hiện nay là các ứng dụng di động dựa trên vị trí, bao gồm Foursquare, Yelp, Uber, Pokémon Go và Waze. Tất cả các ứng dụng phần mềm này đều sử dụng API cho phép chúng trích xuất vị trí địa lý hiện tại trực tiếp từ điện thoại thông minh. Bạn đã bao giờ tự hỏi làm thế nào điện thoại thông minh của bạn có được vị trí địa lý chưa? Ngày nay, việc này được thực hiện bằng cách kết hợp hai hệ thống, Hệ thống định vị toàn cầu (GPS) và Hệ thống định vị WiFi (WPS).

GPS, với một chùm gồm hơn 30 vệ tinh, phát thông tin về thời gian và vị trí của vệ tinh, do đó mỗi máy thu GPS sẽ sử dụng thông tin này để ước tính vị trí địa lý của nó. Chính phủ Hoa Kỳ đã tạo ra hệ thống, duy trì nó và cho phép bất kỳ ai có máy thu GPS đều có thể truy cập miễn phí. Các vệ tinh có đồng hồ nguyên tử rất ổn định, được đồng bộ hóa với nhau và với đồng hồ mặt đất. Các vệ tinh cũng biết vị trí của chúng với độ chính xác cao. Mỗi vệ tinh GPS liên tục phát tín hiệu vô tuyến chứa thời gian và vị trí hiện tại của nó. Nếu máy thu GPS thu được thông tin này từ ít nhất bốn vệ tinh, nó có thể giải các phương trình tam giác để ước tính vị trí của nó.

Tuy nhiên, GPS không phải lúc nào cũng cung cấp vị trí địa lý chính xác nếu nó không có tầm nhìn thẳng với ít nhất bốn vệ tinh GPS hoặc khi có sự can thiệp từ các hệ thống liên lạc tần số cao khác. Điều này đặc biệt đúng trong môi trường đô thị, nơi các tòa nhà cao tầng thường xuyên chặn tín hiệu GPS. Đây là lúc hệ thống định vị WiFi ra tay giải cứu. Hệ thống định vị WiFi sử dụng cơ sở dữ liệu về các điểm truy cập WiFi, được duy trì độc lập bởi nhiều công ty Internet khác nhau, bao gồm Google, Apple và Microsoft. Mỗi cơ sở dữ liệu chứa thông tin về hàng triệu điểm truy cập WiFi, bao gồm SSID của từng điểm truy cập và ước tính vị trí địa lý của nó. Để hiểu cách hệ thống định vị WiFi sử dụng cơ sở dữ liệu như vậy, hãy xem xét điện thoại thông minh Android cùng với dịch vụ định vị của Google. Từ mỗi điểm truy cập gần đó, điện thoại thông minh sẽ nhận và đo cường độ tín hiệu của tín hiệu báo hiệu (xem Phần 7.3.1), chứa SSID của điểm truy cập. Do đó, điện thoại thông minh có thể liên tục gửi tin nhắn đến dịch vụ định vị của Google (trên đám mây) bao gồm SSID của các điểm truy cập gần đó và cường độ tín hiệu tương ứng. Nó cũng sẽ gửi vị trí GPS của nó (thu được thông qua chương trình phát sóng vệ tinh

LỊCH SỬ TRƯỜNG HỢP

tín hiệu, như mô tả ở trên) khi có sẵn. Sử dụng thông tin về cường độ tín hiệu, Google sẽ ước tính khoảng cách giữa điện thoại thông minh và từng điểm truy cập WiFi. Tận dụng những khoảng cách ước tính này, nó có thể giải các phương trình tam giác để ước tính vị trí địa lý của điện thoại thông minh. Cuối cùng, ước tính dựa trên WiFi này được kết hợp với ước tính dựa trên vệ tinh GPS để tạo thành ước tính tổng hợp, sau đó được gửi trở lại điện thoại thông minh và được các ứng dụng di động dựa trên vị trí sử dụng.

Nhưng bạn vẫn có thể thắc mắc làm thế nào Google (và Apple, Microsoft, v.v.) có được và duy trì cơ sở dữ liệu về các điểm truy cập và đặc biệt là vị trí địa lý của điểm truy cập? Hãy nhớ rằng đối với một điểm truy cập nhất định, mọi điện thoại thông minh Android ở gần sẽ gửi đến dịch vụ vị trí của Google cường độ tín hiệu nhận được từ điểm truy cập cũng như vị trí ước tính của điện thoại thông minh. Do hàng nghìn điện thoại thông minh có thể đi ngang qua điểm truy cập trong bất kỳ ngày nào, dịch vụ định vị của Google sẽ có rất nhiều dữ liệu để sử dụng trong việc ước tính vị trí của điểm truy cập, một lần nữa bằng cách giải các phương trình tam giác. Do đó, các điểm truy cập giúp điện thoại thông minh xác định vị trí của chúng và đến lượt điện thoại thông minh giúp các điểm truy cập xác định vị trí của chúng!

**7.3.5 Tính năng nâng cao trong 802.11**

Chúng ta sẽ kết thúc phần giới thiệu về 802.11 bằng một cuộc thảo luận ngắn về hai khả năng nâng cao có trong mạng 802.11. Như chúng ta sẽ thấy, những khả năng này không được quy định hoàn toàn trong tiêu chuẩn 802.11 mà được thực hiện nhờ các cơ chế được chỉ định trong tiêu chuẩn. Điều này cho phép các nhà cung cấp khác nhau triển khai các khả năng này bằng cách sử dụng các phương pháp tiếp cận (độc quyền) của riêng họ, có lẽ mang lại cho họ lợi thế cạnh tranh.

**Thích ứng tốc độ 802.11**

Chúng ta đã thấy trước đó trong Hình 7.3 rằng các kỹ thuật điều chế khác nhau (với tốc độ truyền khác nhau mà chúng cung cấp) phù hợp với các kịch bản SNR khác nhau. Ví dụ, hãy xem xét một người dùng di động 802.11 cách trạm gốc 20 mét, với tỷ lệ tín hiệu trên nhiễu cao. Với SNR cao, người dùng có thể liên lạc với trạm gốc bằng kỹ thuật điều chế lớp vật lý cung cấp tốc độ truyền cao trong khi duy trì BER thấp. Đây là một người dùng hạnh phúc! Giả sử bây giờ người dùng trở nên di động, rời khỏi trạm gốc, với SNR giảm khi khoảng cách từ trạm gốc tăng lên. Trong trường hợp này, nếu kỹ thuật điều chế được sử dụng trong giao thức 802.11 hoạt động giữa trạm gốc và người dùng không thay đổi, BER sẽ trở nên cao đến mức không thể chấp nhận được khi SNR giảm và cuối cùng sẽ không có khung truyền nào được nhận chính xác.

Vì lý do này, một số triển khai 802.11 có khả năng thích ứng tốc độ để lựa chọn một cách thích ứng kỹ thuật điều chế lớp vật lý cơ bản để sử dụng dựa trên các đặc điểm kênh hiện tại hoặc gần đây. Nếu một nút gửi hai khung liên tiếp mà không nhận được xác nhận (một dấu hiệu ngầm về lỗi bit trên

kênh), tốc độ truyền sẽ giảm trở lại tốc độ thấp hơn tiếp theo. Nếu 10 khung hình liên tiếp được xác nhận hoặc nếu bộ hẹn giờ theo dõi thời gian kể từ lần dự phòng cuối cùng hết hạn thì tốc độ truyền sẽ tăng lên tốc độ cao hơn tiếp theo. Cơ chế thích ứng tốc độ này có chung triết lý "thăm dò" như cơ chế kiểm soát tắc nghẽn của TCP---khi các điều kiện tốt (được phản ánh bằng biên nhận ACK), tốc độ truyền sẽ tăng lên cho đến khi có điều gì đó "xấu" xảy ra (thiếu biên nhận ACK); khi có điều gì đó "xấu" xảy ra, tốc độ truyền tải sẽ giảm. Do đó, việc thích ứng với tốc độ 802.11 và kiểm soát tắc nghẽn TCP cũng tương tự như việc đứa trẻ liên tục thúc giục cha mẹ mình ngày càng nhiều (ví dụ như kẹo cho trẻ nhỏ, giờ giới nghiêm muộn hơn đối với thanh thiếu niên) cho đến khi cuối cùng cha mẹ nói "Đủ rồi!" và đứa trẻ lùi lại (chỉ để thử lại sau khi hy vọng điều kiện đã được cải thiện!). Một số kế hoạch khác cũng đã được đề xuất để cải thiện kế hoạch điều chỉnh tỷ lệ tự động cơ bản này \[Kamerman 1997; Hà Lan 2001; Lacage 2004\].

Quản lý nguồn điện

Nguồn điện là nguồn tài nguyên quý giá trong các thiết bị di động và do đó, tiêu chuẩn 802.11 cung cấp khả năng quản lý nguồn điện cho phép các nút 802.11 giảm thiểu lượng thời gian mà các chức năng cảm nhận, truyền và nhận cũng như mạch điện khác của chúng cần phải "bật". Quản lý nguồn 802.11 hoạt động như sau. Một nút có thể luân phiên rõ ràng giữa trạng thái ngủ và thức (không khác gì một học sinh buồn ngủ trong lớp học!). Nút báo hiệu cho điểm truy cập rằng nó sẽ chuyển sang chế độ ngủ bằng cách đặt bit quản lý năng lượng trong tiêu đề của khung 802.11 thành 1. Sau đó, bộ hẹn giờ trong nút được đặt để đánh thức nút ngay trước khi AP được lên lịch gửi khung báo hiệu của nó (hãy nhớ rằng AP thường gửi khung báo hiệu cứ sau 100 mili giây). Vì AP biết từ bit truyền tải điện đã thiết lập rằng nút sẽ chuyển sang chế độ ngủ nên nó (AP) biết rằng nó không nên gửi bất kỳ khung nào đến nút đó và sẽ đệm bất kỳ khung nào dành cho máy chủ đang ngủ để truyền sau.

Nút sẽ thức dậy ngay trước khi AP gửi khung báo hiệu và nhanh chóng chuyển sang trạng thái hoạt động hoàn toàn (không giống như sinh viên buồn ngủ, việc đánh thức này chỉ cần 250 micro giây \[Kamerman 1997\]!). Các khung báo hiệu được AP gửi đi chứa danh sách các nút có khung đã được lưu vào bộ đệm tại AP. Nếu không có khung đệm nào cho nút, nó có thể chuyển sang chế độ ngủ. Mặt khác, nút có thể yêu cầu rõ ràng rằng các khung được đệm được gửi bằng cách gửi tin nhắn thăm dò tới AP. Với thời gian giữa các tín hiệu là 100 mili giây, thời gian đánh thức là 250 micro giây và thời gian nhỏ tương tự để nhận khung báo hiệu và kiểm tra để đảm bảo rằng không có khung đệm nào được lưu vào bộ đệm, một nút không có khung để gửi hoặc nhận có thể ở trạng thái ngủ trong 99% thời gian, dẫn đến tiết kiệm năng lượng đáng kể.

**7.3.6 Mạng khu vực cá nhân: Bluetooth**

Mạng Bluetooth dường như đã nhanh chóng trở thành một phần của cuộc sống hàng ngày. Có lẽ bạn đã sử dụng mạng Bluetooth làm công nghệ "thay thế cáp" để kết nối

máy tính của bạn bằng bàn phím, chuột không dây hoặc thiết bị ngoại vi khác. Hoặc có lẽ bạn đã sử dụng mạng Bluetooth để kết nối tai nghe không dây, loa, đồng hồ hoặc vòng theo dõi sức khỏe với điện thoại thông minh hoặc để kết nối điện thoại thông minh của bạn với hệ thống âm thanh của ô tô. Trong tất cả các trường hợp này, Bluetooth hoạt động trong phạm vi ngắn (hàng chục mét trở xuống), ở mức năng lượng thấp và chi phí thấp. Vì lý do này, mạng Bluetooth đôi khi được gọi là mạng khu vực cá nhân không dây (WPAN) hoặc piconet.

Mặc dù mạng Bluetooth nhỏ và có thiết kế tương đối đơn giản nhưng chúng chứa nhiều kỹ thuật mạng cấp liên kết mà chúng ta đã nghiên cứu trước đó, bao gồm ghép kênh phân chia theo thời gian (TDM) và phân chia tần số (Phần 6.3.1), dự phòng ngẫu nhiên (Phần 6.3.2), thăm dò (Phần 6.3.3), phát hiện và sửa lỗi (Phần 6.2), truyền dữ liệu đáng tin cậy qua ACK và NAKS (Phần 3.4.1). Và đó chỉ là đang xem xét lớp liên kết của Bluetooth!

Mạng Bluetooth hoạt động ở băng tần vô tuyến 2,4 GHz Công nghiệp, Khoa học và Y tế (ISM) không được cấp phép cùng với các thiết bị gia dụng khác như lò vi sóng, thiết bị mở cửa gara và điện thoại không dây. Do đó, mạng Bluetooth được thiết kế rõ ràng có tính đến tiếng ồn và nhiễu. Kênh không dây Bluetooth được vận hành theo cách TDM, với các khe thời gian là 625 micro giây. Trong mỗi khe thời gian, người gửi truyền trên một trong 79 kênh, với kênh (tần số) thay đổi theo cách đã biết nhưng giả ngẫu nhiên từ khe này sang khe khác. Hình thức nhảy kênh này, được gọi là trải phổ nhảy tần (FHSS), được sử dụng để nhiễu từ một thiết bị khác hoặc thiết bị hoạt động trong băng tần ISM sẽ chỉ cản trở giao tiếp Bluetooth trong tối đa một tập hợp con các khe cắm. Tốc độ dữ liệu Bluetooth có thể đạt tới 3 Mbps.

Mạng Bluetooth là mạng ad hoc---không cần cơ sở hạ tầng mạng (ví dụ: điểm truy cập). Thay vào đó, các thiết bị Bluetooth phải tự tổ chức thành một piconet gồm tối đa tám thiết bị hoạt động, như trong Hình 7.16. Một trong những thiết bị này

*Hình 7.16 ♦ Một piconet Bluetooth*

Bán kính phủ sóng

Thiết bị chính

Thiết bị khách

Thiết bị đỗ

Chìa khóa:

M

M

C

C C C

P

P

P

P

P

được chỉ định là thiết bị chính, các thiết bị còn lại đóng vai trò là máy khách. Nút chính thực sự điều khiển piconet---đồng hồ của nó xác định thời gian trong piconet (ví dụ: xác định ranh giới khe TDM), nó xác định trình tự nhảy tần giữa các khe, nó kiểm soát việc đưa các thiết bị khách vào piconet, nó kiểm soát công suất (100 mW, 2,5 mW hoặc 1 mW) mà các thiết bị khách truyền tải; và sử dụng tính năng bỏ phiếu để cấp cho khách hàng quyền truyền tải sau khi được chấp nhận vào mạng. Ngoài các thiết bị đang hoạt động, còn có thể có tới 255 thiết bị "đậu" trong piconet. Các thiết bị đỗ này thường ở một dạng "chế độ ngủ" nào đó để tiết kiệm năng lượng (như chúng ta đã thấy với quản lý nguồn 802.11) và sẽ thức dậy định kỳ, theo lịch trình của thiết bị chủ, để nhận các thông báo báo hiệu từ thiết bị chủ. Thiết bị đỗ không thể liên lạc cho đến khi trạng thái của nó được thay đổi từ trạng thái đỗ sang hoạt động bởi nút chính.

Vì mạng Bluetooth ad hoc phải tự tổ chức nên cần xem xét cách chúng khởi động lại cấu trúc mạng của mình. Khi nút chính muốn hình thành mạng Bluetooth, trước tiên nó phải xác định thiết bị Bluetooth nào khác nằm trong phạm vi phủ sóng; đây là vấn đề khám phá hàng xóm. Master thực hiện điều này bằng cách phát một loạt 32 tin nhắn truy vấn, mỗi tin nhắn trên một kênh tần số khác nhau và lặp lại trình tự truyền tới 128 lần. Một thiết bị khách lắng nghe trên tần số đã chọn của nó, hy vọng nghe được một trong các thông báo yêu cầu của thiết bị chủ trên tần số này. Khi nghe thấy một thông báo yêu cầu, nó sẽ lùi lại một khoảng thời gian ngẫu nhiên trong khoảng từ 0 đến 0,3 giây (để tránh xung đột với các nút phản hồi khác, gợi nhớ đến thời gian chờ nhị phân của Ethernet) và sau đó phản hồi lại nút chủ bằng một thông báo chứa ID thiết bị của nó.

Khi Bluetooth master đã phát hiện ra tất cả các máy khách tiềm năng trong phạm vi, nó sẽ mời những máy khách đó muốn tham gia piconet. Giai đoạn thứ hai này được gọi là phân trang Bluetooth và gợi nhớ đến các máy khách 802.11 liên kết với một trạm cơ sở. Thông qua quá trình phân trang, thiết bị chủ sẽ thông báo cho máy khách về kiểu nhảy tần sẽ được sử dụng và đồng hồ của người gửi. Master bắt đầu quá trình phân trang bằng cách gửi lại 32 tin nhắn mời phân trang giống hệt nhau, mỗi tin nhắn hiện được gửi đến một khách hàng cụ thể, nhưng lại sử dụng các tần số khác nhau, vì khách hàng đó vẫn chưa học được mẫu nhảy tần. Khi máy khách trả lời bằng tin nhắn ACK cho tin nhắn mời phân trang, máy chủ sẽ gửi thông tin nhảy tần, thông tin đồng bộ hóa đồng hồ và địa chỉ thành viên đang hoạt động cho máy khách, sau đó cuối cùng thăm dò ý kiến ​​của máy khách, hiện đang sử dụng mẫu nhảy tần, để đảm bảo rằng máy khách được kết nối vào mạng.

Trong cuộc thảo luận ở trên, chúng tôi chỉ đề cập đến mạng không dây của Bluetooth. Các giao thức cấp cao hơn cung cấp khả năng truyền gói dữ liệu đáng tin cậy, truyền phát âm thanh và video giống như mạch, thay đổi mức công suất truyền, thay đổi trạng thái hoạt động/không hoạt động (và các trạng thái khác), v.v. Các phiên bản gần đây hơn của Bluetooth đã giải quyết các vấn đề về năng lượng thấp và bảo mật. Để biết thêm thông tin về Bluetooth, độc giả quan tâm nên tham khảo \[Bisdikian 2001, Colbach 2017 và Bluetooth 2020\].

**7.4 Mạng di động: 4G và 5G**

Trong phần trước, chúng tôi đã kiểm tra cách máy chủ có thể truy cập Internet khi ở trong vùng lân cận của điểm truy cập WiFi 802.11 (AP). Nhưng như chúng ta đã thấy, các AP có vùng phủ sóng nhỏ và máy chủ chắc chắn sẽ không thể liên kết với mọi AP mà nó gặp phải. Do đó, việc truy cập WiFi hầu như không phổ biến đối với người dùng khi đang di chuyển.

Ngược lại, truy cập mạng di động 4G đã nhanh chóng trở nên phổ biến. Một nghiên cứu đo lường gần đây với hơn một triệu thuê bao mạng di động ở Hoa Kỳ cho thấy họ có thể tìm thấy tín hiệu 4G trong hơn 90% thời gian, với tốc độ tải xuống từ 20 Mbps trở lên. Người dùng của ba nhà mạng di động lớn của Hàn Quốc có thể tìm thấy tín hiệu 4G trong khoảng từ 95 đến 99,5% thời gian \[Open Signal 2019\]. Do đó, việc truyền phát video HD hoặc tham gia hội nghị truyền hình khi đang di chuyển trên ô tô, xe buýt hoặc tàu cao tốc hiện nay đã trở nên phổ biến. Sự phổ biến của truy cập Internet 4G cũng đã cho phép vô số ứng dụng IoT mới như hệ thống xe đạp và xe tay ga dùng chung được kết nối Internet cũng như các ứng dụng điện thoại thông minh như thanh toán di động (phổ biến ở Trung Quốc kể từ năm 2018) và nhắn tin dựa trên Internet (WeChat, WhatsApp, v.v.).

Thuật ngữ di động đề cập đến thực tế là vùng được bao phủ bởi mạng di động được phân chia thành một số vùng phủ sóng địa lý, được gọi là ô. Mỗi ô chứa một trạm cơ sở truyền tín hiệu đến và nhận tín hiệu từ các thiết bị di động hiện có trong ô của nó. Vùng phủ sóng của một ô phụ thuộc vào nhiều yếu tố, bao gồm công suất phát của trạm gốc, công suất phát của thiết bị, vật cản của các tòa nhà trong ô cũng như chiều cao và loại ăng-ten của trạm gốc.

Trong phần này, chúng tôi cung cấp cái nhìn tổng quan về mạng di động 4G hiện tại và 5G mới nổi. Chúng ta sẽ xem xét bước nhảy đầu tiên không dây giữa thiết bị di động và trạm cơ sở, cũng như mạng lõi toànIP của nhà cung cấp dịch vụ di động kết nối bước nhảy đầu tiên không dây vào mạng của nhà cung cấp dịch vụ, các mạng của nhà cung cấp dịch vụ khác và Internet lớn hơn. Có lẽ đáng ngạc nhiên (do nguồn gốc của mạng di động di động trong thế giới điện thoại, vốn có kiến ​​trúc mạng rất khác với Internet), chúng ta sẽ gặp nhiều nguyên tắc kiến ​​trúc trong mạng 4G mà chúng ta đã gặp trong các nghiên cứu tập trung vào Internet ở Chương 1--6, bao gồm phân lớp giao thức, phân biệt ranh giới/lõi, sự kết nối của nhiều mạng nhà cung cấp để tạo thành một "mạng các mạng" toàn cầu và sự phân tách rõ ràng giữa các mặt phẳng dữ liệu và điều khiển với điều khiển tập trung hợp lý. Bây giờ chúng ta sẽ nhìn những nguyên tắc này qua lăng kính mạng di động (chứ không phải qua lăng kính Internet) và do đó sẽ thấy những nguyên tắc này được thể hiện theo những cách khác nhau. Và tất nhiên, với mạng của nhà cung cấp dịch vụ có lõi allIP, chúng ta cũng sẽ gặp nhiều giao thức Internet mà hiện nay chúng ta đã biết rõ. Chúng tôi sẽ đề cập đến các chủ đề 4G bổ sung---quản lý di động trong Phần 7.6 và bảo mật 4G trong Phần 8.8---sau khi phát triển các nguyên tắc cơ bản cần thiết cho các chủ đề này.

Cuộc thảo luận của chúng tôi ở đây về mạng 4G và 5G sẽ tương đối ngắn gọn. Mạng di động di động là một lĩnh vực có chiều rộng và chiều sâu lớn, với nhiều trường đại học cung cấp một số khóa học về chủ đề này. Những độc giả muốn hiểu sâu hơn được khuyến khích xem \[Goodman 1997; Kaaranen 2001; Lâm 2001; Korhonen 2003;

Schiller 2003; Palat 2009; Scourias 2012; Người quay 2012; Akyildiz 2010\], cũng như những cuốn sách đặc biệt xuất sắc và đầy đủ \[Mouly 1992; Sauter 2014\].

Giống như Internet RFC xác định kiến ​​trúc và giao thức tiêu chuẩn Internet, mạng 4G và 5G cũng được xác định bởi các tài liệu tiêu chuẩn được gọi là Thông số kỹ thuật. Những tài liệu này được cung cấp miễn phí trực tuyến tại \[3GPP 2020\]. Cũng giống như RFC, các thông số kỹ thuật có thể giúp đọc khá dày đặc và chi tiết. Nhưng khi bạn có một câu hỏi, chúng là nguồn chính xác cho câu trả lời!

7.4.1 Mạng Di động 4G LTE: Kiến trúc và Các Thành phần

Các mạng 4G phổ biến tính đến thời điểm viết bài này vào năm 2020 đều triển khai tiêu chuẩn Tiến hóa dài hạn 4G, hay nói ngắn gọn hơn là 4G LTE. Trong phần này, chúng tôi sẽ mô tả mạng 4G LTE. Hình 7.17 thể hiện các thành phần chính của kiến ​​trúc mạng 4G LTE. Mạng được chia thành mạng vô tuyến ở biên của mạng di động và mạng lõi. Tất cả các thành phần mạng giao tiếp với nhau bằng giao thức IP mà chúng ta đã nghiên cứu trong Chương 4. Giống như các mạng 2G và 3G trước đó, 4G LTE có đầy đủ các từ viết tắt và tên thành phần khá khó hiểu. Chúng tôi sẽ cố gắng giải quyết tình trạng lộn xộn đó bằng cách trước tiên tập trung vào các chức năng của thành phần và cách các thành phần khác nhau của mạng 4G LTE tương tác với nhau trong cả mặt phẳng dữ liệu và mặt phẳng điều khiển:

• Thiết bị di động. Đây là điện thoại thông minh, máy tính bảng, máy tính xách tay hoặc thiết bị IoT kết nối với mạng của nhà cung cấp dịch vụ di động. Đây là nơi chạy các ứng dụng như trình duyệt web, ứng dụng bản đồ, ứng dụng thoại và hội nghị truyền hình, ứng dụng thanh toán di động, v.v. Thiết bị di động thường triển khai đầy đủ ngăn xếp giao thức Internet 5 lớp, bao gồm các lớp vận chuyển và ứng dụng, như chúng ta đã thấy với các máy chủ ở biên mạng Internet. Thiết bị di động là điểm cuối mạng, có địa chỉ IP (có được thông qua NAT, như chúng ta sẽ thấy). Thiết bị di động cũng có mã nhận dạng 64-bit duy nhất trên toàn cầu được gọi là Nhận dạng thuê bao di động quốc tế (IMSI), được lưu trữ trên thẻ SIM (Mô-đun nhận dạng thuê bao). IMSI xác định thuê bao trong hệ thống mạng của nhà cung cấp dịch vụ di động trên toàn thế giới, bao gồm cả quốc gia và mạng của nhà cung cấp dịch vụ di động tại nhà mà thuê bao thuộc về. Ở một khía cạnh nào đó, IMSI tương tự như địa chỉ MAC. Thẻ SIM còn lưu trữ thông tin về các dịch vụ mà thuê bao có thể truy cập và mã hóa thông tin khóa cho thuê bao đó. Trong thuật ngữ chính thức của 4G LTE, thiết bị di động được gọi là Thiết bị người dùng (UE). Tuy nhiên, trong sách giáo khoa này, chúng tôi sẽ sử dụng thuật ngữ "thiết bị di động" thân thiện hơn với người đọc. Ở đây chúng tôi cũng lưu ý rằng thiết bị di động không phải lúc nào cũng di động; ví dụ: thiết bị có thể là cảm biến nhiệt độ cố định hoặc camera giám sát. • Trạm cơ sở. Trạm cơ sở nằm ở "biên" mạng của nhà cung cấp dịch vụ và chịu trách nhiệm quản lý tài nguyên vô tuyến không dây và các thiết bị di động trong vùng phủ sóng của nó (được hiển thị dưới dạng ô lục giác trong Hình 7.17). Như chúng ta sẽ thấy, thiết bị di động sẽ tương tác với trạm gốc để gắn vào mạng của nhà cung cấp dịch vụ. Trạm gốc phối hợp xác thực thiết bị và phân bổ tài nguyên

(channel access) in the radio access network. In this sense, cellular base station functions are comparable (but by no means identical) to those of APs in wireless LANs. But cellular base stations have several other important roles not found in wireless LANs. In particular, base stations create device-specific IP tunnels from the mobile device to gateways and interact among themselves to handle device mobility among cells. Nearby base stations also coordinate among themselves to manage the radio spectrum to minimize interference between cells. In the official 4G LTE terminology, the base station is referred to as an "eNode-B," which is rather opaque and non-descriptive. In this textbook, we will instead use the reader-friendlier term "base station" throughout. As an aside, if you find LTE terminology a bit opaque, you aren't alone! The etymology of "eNode-B" is rooted in earlier 3G terminology, where network function points were referred to as "nodes," with "B" harkening back to earlier "Base Station (BS)" 1G terminology or "Base Transceiver Station (BTS)" in 2G terminology. 4G LTE is an "e"volution over 3G, and hence, an "e" now precedes "Node-B" in 4G LTE terminology. This name opaqueness shows no signs in stopping! In 5G systems, eNode-B functions are now referred to as "ng-eNB"; perhaps you can guess what that acronym stands for! • Home Subscriber Server (HSS). As shown in Figure 7.18, the HSS is a control-plane element. The HSS is a database, storing information about the mobile devices for which the HSS's network is their home network. It is used in conjunction with the MME (discussed below) for device authentication. • Serving Gateway (S-GW), Packet Data Network Gateway (P-GW), and other network routers. As shown in Figure 7.18, the Serving Gateway and the Packet Data Network Gateway are two routers (often collocated in practice) that

Thực thể Quản lý Di động (MME)

Cổng phục vụ

(S-GW)

Dịch vụ thuê bao tại nhà (HSS)

Cổng PDN

(P-GW)

truy cập vô tuyến lõi Packet tăng cường toàn IP (EPC)

mạng

tới Internet

Thiết bị di động

Trạm gốc

*Hình 7.17 ♦ Các thành phần của kiến trúc 4G LTE*

nằm trên đường dữ liệu giữa thiết bị di động và Internet. Cổng PDN cũng cung cấp địa chỉ NAT IP cho các thiết bị di động và thực hiện các chức năng NAT (xem Mục 4.3.4). Cổng PDN là phần tử LTE cuối cùng mà một gói dữ liệu xuất phát từ thiết bị di động gặp trước khi vào Internet rộng lớn hơn. Đối với thế giới bên ngoài, P-GW trông giống như bất kỳ bộ định tuyến cổng nào khác; khả năng di động của các nút di động trong mạng LTE của nhà cung cấp dịch vụ di động được che giấu khỏi thế giới bên ngoài phía sau P-GW. Ngoài các bộ định tuyến cổng này, toàn bộ lõi IP của nhà cung cấp dịch vụ di động sẽ có các bộ định tuyến bổ sung có vai trò tương tự như các bộ định tuyến IP truyền thống---để chuyển tiếp các gói dữ liệu IP giữa các bộ định tuyến với nhau theo các đường dẫn thường kết thúc tại các phần tử của mạng lõi LTE.

• Thực thể Quản lý Di động (MME). MME cũng là một phần tử mặt điều khiển, như được minh họa trong Hình 7.18. Cùng với HSS, nó đóng vai trò quan trọng trong việc xác thực thiết bị muốn kết nối vào mạng của nó. Nó cũng thiết lập các đường hầm trên đường dữ liệu từ/đến thiết bị và bộ định tuyến cổng Internet PDN, đồng thời duy trì thông tin về vị trí ô của thiết bị di động đang hoạt động trong mạng di động của nhà mạng. Nhưng, như được minh họa trong Hình 7.18, nó không nằm trong đường dẫn chuyển tiếp cho các gói dữ liệu của thiết bị di động được gửi đi và nhận từ Internet.

Xác thực. Điều này quan trọng đối với mạng và thiết bị di động kết nối

to the network to mutually authenticate each other---for the network to know that the attaching device is indeed the device associated with a given IMSI, and for the mobile device to know that the network to which it is attaching is also a legitimate cellular carrier network. We will cover authentication in Chapter 8 and cover 4G authentication in Section 8.8. Here, we simply note that the MME plays a middleman role between the mobile and Home Subscriber Service (HSS) in the mobile's home network. Specifically, after receiving an attach request from mobile device, the local MME contacts the HSS in the mobile's home network. The mobile's home HSS then returns enough encrypted information to the local MME to prove to the mobile device that the home HSS is performing authentication through this MME, and for the mobile device to prove to the MME that it is indeed the mobile associated with that IMSI. When a mobile device is attached to its home network, the HSS to be contacted during authentication is located within that same home network. However, when a mobile device is roaming on a visited network operated by a different cellular network carrier, the MME in that roaming network will need to contact the HSS in the mobile device's home network.

Thiết lập đường dẫn. Như được hiển thị ở nửa dưới của Hình 7.18, đường dẫn dữ liệu từ

thiết bị di động tới bộ định tuyến cổng của nhà mạng bao gồm một bước nhảy không dây đầu tiên giữa thiết bị di động và trạm gốc, và các đường hầm IP được nối tiếp giữa trạm gốc và Cổng Dịch Vụ, và giữa Cổng Dịch Vụ và Cổng PDN. Các đường hầm được thiết lập dưới sự điều khiển của MME và được sử dụng để chuyển tiếp dữ liệu (thay vì chuyển tiếp trực tiếp giữa các bộ định tuyến mạng) nhằm tạo điều kiện thuận lợi cho tính di động của thiết bị---khi một thiết bị di chuyển, chỉ các điểm cuối của đường hầm

Kiểm soát

máy bay

Dữ liệu người dùng

máy bay

MME

HSS

Trạm gốc

Trạm gốc

P-GW S-GW

S-GW

Cổng gói dữ liệu (P-GW)

*Hình 7.18 ♦ Các thành phần mặt phẳng dữ liệu và mặt phẳng điều khiển LTE*

việc kết thúc tại trạm gốc cần được thay đổi, trong khi các điểm cuối của đường hầm khác và Chất lượng Dịch vụ liên quan đến đường hầm vẫn không thay đổi. Theo dõi vị trí ô. Khi thiết bị di chuyển giữa các ô, các trạm gốc

sẽ cập nhật cho MME về vị trí của thiết bị. Nếu thiết bị di động đang ở chế độ ngủ nhưng vẫn di chuyển giữa các ô, các trạm gốc sẽ không thể theo dõi vị trí của thiết bị. Trong trường hợp này, việc xác định vị trí thiết bị để đánh thức sẽ là trách nhiệm của MME, thông qua một quá trình được gọi là paging.

Bảng 7.2 tóm tắt các yếu tố kiến trúc LTE chính mà chúng ta đã thảo luận ở trên và so sánh các chức năng này với những chức năng mà chúng ta đã gặp trong nghiên cứu về mạng LAN không dây WiFi (WLAN).

Mô tả phần tử LTE Tương tự chức năng WLAN

Thiết bị di động (UE: Thiết bị người dùng) Thiết bị không dây/di động có khả năng IP của người dùng cuối (ví dụ: điện thoại thông minh, máy tính bảng, máy tính xách tay)

Host, hệ thống đầu cuối

Trạm gốc (eNode-B) phía mạng của liên kết truy cập không dây vào mạng LTE

Điểm truy cập (AP), mặc dù trạm gốc LTE thực hiện nhiều chức năng không có trong WLAN

Thực thể Quản lý Di động (MME)

Điều phối viên cho dịch vụ thiết bị di động: xác thực, quản lý di động

Điểm truy cập (AP), mặc dù MME thực hiện nhiều chức năng không có trong mạng WLAN

Máy chủ thuê bao tại nhà (HSS) Nằm trong mạng gia đình của thiết bị di động, cung cấp xác thực, đặc quyền truy cập trong mạng gia đình và mạng khách

Không có tương đương WLAN

Cổng phục vụ (S-GW), Cổng PDN (P-GW)

Routers trong mạng của nhà điều hành di động, điều phối việc chuyển tiếp ra ngoài mạng của nhà điều hành

Các bộ định tuyến iBGP và eBGP trong mạng ISP truy cập

Mạng truy cập vô tuyến Liên kết không dây giữa thiết bị di động và trạm gốc

Liên kết không dây 802.11 giữa thiết bị di động và AP

Bảng 7.2 ♦ Các phần tử LTE và các chức năng WLAN (WiFi) tương tự

SỰ TIẾN HÓA KIẾN TRÚC TỪ 2G ĐẾN 3G ĐẾN 4G

Trong một khoảng thời gian tương đối ngắn là 20 năm, các mạng di động của các nhà điều hành đã trải qua một sự chuyển đổi đáng kinh ngạc từ việc hầu như chỉ là các mạng điện thoại chuyển mạch kênh sang trở thành các mạng dữ liệu chuyển mạch gói hoàn toàn, bao gồm giọng nói chỉ là một trong nhiều ứng dụng. Sự chuyển đổi này đã diễn ra như thế nào từ góc độ kiến trúc? Có một "ngày cờ hiệu", khi các mạng hướng điện thoại trước đây bị tắt đi và mạng di động chuyển mạch gói hoàn toàn được bật lên không? Hay các thành phần trong các mạng hướng điện thoại trước đây bắt đầu đảm nhận cả chức năng chuyển mạch kênh (di sản) và chuyển mạch gói (mới), như chúng ta đã thấy với sự chuyển đổi từ IPv4 sang IPv6 trong Mục 4.3.5?

Hình 7.19 được lấy từ ấn bản thứ 7 trước đây của sách giáo khoa này, vốn bao quát cả mạng di động 2G và 3G. (Chúng tôi đã loại bỏ tài liệu lịch sử này, mặc dù vẫn có thể truy cập trên trang web của cuốn sách, để tập trung sâu hơn vào LTE 4G trong ấn bản thứ 8 này). Mặc dù mạng 2G là mạng điện thoại di động chuyển mạch kênh, việc so sánh Hình 7.17 và 7.19 minh họa một cấu trúc khái niệm tương tự, mặc dù dành cho thoại thay vì dịch vụ dữ liệu---một cạnh không dây được kiểm soát bởi trạm gốc, một cổng kết nối từ mạng của nhà mạng ra thế giới bên ngoài, và các điểm tổng hợp giữa các trạm gốc và cổng kết nối.

LỊCH SỬ TRƯỜNG HỢP

Trạm gốc

bộ điều khiển

Trạm gốc

bộ điều khiển

Chuyển mạch di động

Trung tâm

Cổng di động

Chuyển đổi

Trung tâm

Hệ thống trạm gốc (BSS)

Hệ thống trạm gốc (BSS)

Điện thoại công cộng

Mạng

G

*Hình 7.19 ♦ Các thành phần của kiến trúc di động 2G, hỗ trợ chuyển mạch mạch*

dịch vụ thoại với mạng lõi của nhà mạng

Trung tâm chuyển mạch di động cổng

G

Bộ điều khiển mạng radio (RNC) Cổng GPRS

Nút Hỗ Trợ Phục Vụ Nút Hỗ Trợ GPRS

G

Chuyển mạch di động

Trung tâm

Điện thoại công cộng

Mạng

Internet công cộng

*Hình 7.20 ♦ Kiến trúc hệ thống 3G: hỗ trợ chuyển mạch mạch riêng biệt*

dịch vụ thoại và dịch vụ dữ liệu chuyển mạch gói với mạng lõi của nhà cung cấp dịch vụ

*Figure 7.20 (also taken from the 7th edition of this textbook) shows the main architectural components of the 3G cellular architecture, which supports both circuit-switched voice service and packet-switched data services. Here, the transition from a voice-only network to a combined voice and data network is clear: the existing core 2G cellular voice network elements remained untouched. However, additional cellular data functionality was added in parallel to, and functioned independently from, the existing core voice network at that time. As shown in Figure 7.20, the splitting point into these two separate core voice and data networks happened at the network edge, at the base station in the radio access network. The alternative---integrating new data services directly into the core elements of the existing cellular voice network---would have raised the same challenges encountered in integrating new (IPv6) and legacy (IPv4) technologies in the Internet. The carriers also wanted to leverage and exploit their considerable investment of existing infrastructure (and profitable services!) in their existing cellular voice network.*

**7.4.2 Ngăn xếp Giao thức LTE**

Vì kiến trúc 4G LTE là kiến trúc toànIP nên chúng ta đã rất quen thuộc với các giao thức lớp cao hơn trong dãy giao thức LTE, đặc biệt là IP, TCP, UDP và các giao thức lớp ứng dụng khác nhau, từ các nghiên cứu của chúng ta trong Chương 2 đến Chương 5. Do đó, các giao thức LTE mới mà chúng ta sẽ tập trung ở đây chủ yếu ở lớp liên kết, lớp vật lý và trong tính di động quản lý.

Hình 7.21 cho thấy các ngăn xếp giao thức mặt người dùng tại nút di động LTE, trạm gốc và cổng phục vụ. Chúng ta sẽ đề cập đến một số giao thức mặt điều khiển của LTE sau khi nghiên cứu quản lý di động LTE (Mục 7.6) và bảo mật (Mục 8.8). Như có thể thấy từ Hình 7.21, hầu hết các hoạt động giao thức mặt người dùng mới và thú vị đang diễn ra tại liên kết vô tuyến không dây giữa thiết bị di động và trạm gốc.

LTE chia lớp liên kết của thiết bị di động thành ba tiểu lớp:

• Packet Hội tụ dữ liệu. Tầng con trên cùng của tầng liên kết này nằm ngay dưới IP. Giao thức Hội tụ dữ liệu Packet (PDCP) \[3GPP PDCP 2019\] thực hiện nén/giải nén tiêu đề IP nhằm giảm số bit được gửi qua liên kết không dây, và mã hóa/giải mã các gói dữ liệu IP bằng các khóa được thiết lập thông qua các thông điệp tín hiệu giữa thiết bị di động LTE và Thực thể Quản lý Di động (MME) khi thiết bị di động lần đầu kết nối với mạng; chúng tôi sẽ đề cập đến các khía cạnh bảo mật LTE trong Mục 8.8.2. • Điều khiển Liên kết Radio. Giao thức Điều khiển Liên kết Radio (RLC) \[3GPP RLCP 2018\] thực hiện hai chức năng quan trọng: (i) phân mảnh (ở phía gửi) và lắp ráp lại (ở phía nhận) các gói dữ liệu IP quá lớn để phù hợp với

Trạm gốc Cổng mạng PDN

(P-GW) Cổng phục vụ

(S-GW)

đến/ từ Internet

IP Packet Hội tụ Dữ liệu

Liên kết radio

Truy cập trung bình

Liên kết

GTP-U

IP

Liên kết

Vật lý

UDP GTP-U

IP

Liên kết

Vật lý

UDP GTP-U

IP

Liên kết

Vật lý

UDP Ứng dụng

Vật lý

Vận chuyển

IP Packet Hội tụ Dữ liệu

Liên kết radio

Truy cập trung bình

Vật lý

*Hình 7.21 ♦ Ngăn xếp giao thức mặt dữ liệu LTE*

các khung lớp liên kết cơ bản, và (ii) truyền dữ liệu đáng tin cậy lớp liên kết thông qua việc sử dụng giao thức ARQ dựa trên ACK/NAK. Hãy nhớ rằng chúng ta đã nghiên cứu các yếu tố cơ bản của các giao thức ARQ trong Mục 3.4.1. • Điều khiển truy cập phương tiện (MAC). Lớp MAC thực hiện lập lịch truyền, nghĩa là, yêu cầu và sử dụng các khe truyền sóng radio được mô tả trong Mục 7.4.4. Tiểu lớp MAC cũng thực hiện các chức năng phát hiện/sửa lỗi bổ sung, bao gồm việc sử dụng truyền bit dư thừa như một kỹ thuật sửa lỗi tiến. Lượng dư thừa có thể được điều chỉnh theo điều kiện kênh.

Hình 7.21 cũng cho thấy việc sử dụng các đường hầm trong đường dữ liệu người dùng. Như đã thảo luận ở trên, các đường hầm này được thiết lập, dưới sự kiểm soát của MME, khi thiết bị di động lần đầu tiên kết nối với mạng. Mỗi đường hầm giữa hai điểm cuối có một định danh điểm cuối đường hầm (TEID) duy nhất. Khi trạm gốc nhận các datagram từ thiết bị di động, nó đóng gói chúng bằng Giao thức Đường hầm GPRS \[3GPP GTPv1-U 2019\], bao gồm cả TEID, và gửi chúng trong các phân đoạn UDP đến Cổng Dịch vụ (Serving Gateway) ở đầu kia của đường hầm. Ở phía nhận, trạm gốc mở gói các datagram UDP được đường hầm hóa, trích xuất datagram IP được đóng gói hướng đến thiết bị di động, và chuyển tiếp datagram IP đó qua bước sóng không dây tới thiết bị di động.

**7.4.3 Mạng Truy cập Vô tuyến LTE**

LTE uses a combination of frequency division multiplexing and time division multiplexing on the downstream channel, known as orthogonal frequency division multiplexing (OFDM) \[Hwang 2009\]. (The term "orthogonal" comes from the fact the signals being sent on different frequency channels are created so that they interfere very little with each other, even when channel frequencies are tightly spaced). In LTE, each active mobile device is allocated one or more 0.5 ms time slots in one or more of the channel frequencies. Figure 7.22 shows an allocation of eight time slots over four frequencies. By being allocated increasingly more time slots (whether on the same frequency or on different frequencies), a mobile device is able to achieve increasingly higher transmission rates. Slot (re)allocation among mobile devices can be performed as often as once every millisecond. Different modulation schemes can also be used to change the transmission rate; see our earlier discussion of Figure 7.3 and dynamic selection of modulation schemes in WiFi networks.

Việc phân bổ các khe thời gian cụ thể cho thiết bị di động không được tiêu chuẩn LTE quy định. Thay vào đó, quyết định thiết bị di động nào được phép truyền trong một khe thời gian nhất định trên một tần số nhất định được xác định bởi các thuật toán lập lịch do nhà cung cấp thiết bị LTE và/hoặc nhà điều hành mạng cung cấp. Với lập lịch cơ hội \[Bender 2000; Kolding 2003; Kulkarni 2005\], việc kết hợp giao thức lớp vật lý với điều kiện kênh giữa thiết bị gửi và nhận và lựa chọn các thiết bị nhận mà các gói tin sẽ được gửi dựa trên điều kiện kênh cho phép trạm gốc tận dụng tốt nhất phương tiện không dây. Ngoài ra, người dùng

Các mức độ ưu tiên và dịch vụ theo hợp đồng (ví dụ: bạc, vàng hoặc bạch kim) có thể được sử dụng trong việc lập lịch truyền gói dữ liệu xuống. Ngoài các khả năng LTE đã được mô tả ở trên, LTE-Advanced cho phép băng thông xuống của hàng trăm Mbps bằng cách phân bổ các kênh tổng hợp cho thiết bị di động \[Akyildiz 2010\].

**7.4.4 Chức năng LTE bổ sung: Kết nối mạng và Quản lý năng lượng**

Hãy kết thúc nghiên cứu về 4G LTE tại đây bằng cách xem xét hai chức năng quan trọng bổ sung của LTE: (i) quá trình mà thiết bị di động lần đầu kết nối với mạng và (ii) các kỹ thuật được thiết bị di động sử dụng, cùng với các phần tử mạng lõi, để quản lý việc sử dụng năng lượng của nó.

Gắn kết mạng

Quá trình mà một thiết bị di động kết nối với mạng của nhà mạng di động được chia thành ba giai đoạn chính:

• Kết nối với Trạm Cơ sở. Giai đoạn đầu tiên của việc kết nối thiết bị này có mục đích tương tự, nhưng thực tế khá khác với, giao thức liên kết 802.11 mà chúng ta đã nghiên cứu trong Mục 7.31. Một thiết bị di động muốn kết nối với mạng của nhà cung cấp dịch vụ di động sẽ bắt đầu một quá trình khởi động (bootstrap) để tìm hiểu về, và sau đó liên kết với, một trạm cơ sở gần đó. Thiết bị di động ban đầu sẽ tìm kiếm tất cả các kênh trong tất cả các dải tần số để tìm tín hiệu đồng bộ chính được phát sóng định kỳ

*Hình 7.22 ♦ Hai mươi khe thời gian 0,5 ms được tổ chức thành các khung 10 ms tại mỗi*

tần số. Một phân bổ tám khe được hiển thị bằng màu đậm.

f1

f2

f3

f4

f5

f6

0,5 1,0 1,5 2,0 2,5 9,0 9,5 10,0

every 5 ms by a base station. Once this signal is found, the mobile device remains on this frequency and locates the secondary synchronization signal. With information found in this second signal, the device can locate (following several further steps) additional information such as channel bandwidth, channel configurations, and the cellular carrier information of that base station. Armed with this information, the mobile device can select a base station to associate with (preferentially attaching to its home network, if available) and establish a control-plane signaling connection across the wireless hop with that base station. This mobile-to-base-station channel will be used through the remainder of the network attachment process. • Mutual Authentication. In our earlier description of the Mobility Management Entity (MME) in Section 7.4.1, we noted that the base station contacts the local MME to perform mutual authentication---a process that we'll study in further detail in Section 8.8.2. This is the second phase of network attachment, allowing the network to know that the attaching device is indeed the device associated with a given IMSI, and the mobile device to know that the network to which it is attaching is also a legitimate cellular carrier network. Once this second phase of network attachment is complete, the MME and mobile device have mutually authenticated each other, and the MME also knows the identity of the base station to which the mobile is attached. Armed with this information, the MME is now ready to configure the Mobile-device-to-PDN-gateway data path. • Mobile-device-to-PDN-gateway Data Path Configuration. The MME contacts the PDN gateway (which also provides a NAT address for the mobile device), the Serving gateway, and the base station to establish the two tunnels shown in Figure 7.21. Once this phase is complete, the mobile device is able to send/receive IP datagrams via the base station through these tunnels to and from the Internet!

Quản lý Năng lượng: Chế độ Ngủ

Hãy nhớ lại trong cuộc thảo luận trước đây của chúng ta về các tính năng nâng cao trong 802.11 (Mục 7.3.5) và Bluetooth (Mục 7.3.6) rằng một bộ phát/thu trong thiết bị không dây có thể chuyển sang trạng thái ngủ để tiết kiệm năng lượng khi nó không đang phát hoặc nhận dữ liệu, nhằm giảm thiểu thời gian mà mạch của thiết bị di động cần được \"bật\" để gửi/nhận dữ liệu và để dò kênh. Trong 4G LTE, một thiết bị di động đang ở trạng thái ngủ có thể ở một trong hai trạng thái ngủ khác nhau. Trong trạng thái nhận gián đoạn, thường được thiết lập sau vài trăm mili giây không hoạt động \[Sauter 2014\], thiết bị di động và trạm gốc sẽ lên lịch trước các khoảng thời gian định kỳ (thường cách nhau vài trăm mili giây) mà tại đó thiết bị di động sẽ thức dậy và chủ động theo dõi kênh để nhận các truyền dẫn từ trạm gốc xuống thiết bị di động; ngoài các khoảng thời gian được lên lịch này, bộ phát/thu của thiết bị di động sẽ ở trạng thái ngủ.

Nếu trạng thái tiếp nhận gián đoạn có thể được coi là "giấc ngủ nhẹ," trạng thái ngủ thứ hai---trạng thái Nhàn rỗi---xuất hiện sau những khoảng thời gian dài hơn từ 5 đến 10 giây không hoạt động, có thể được coi là "giấc ngủ sâu." Khi ở trong giấc ngủ sâu này, radio của thiết bị di động thức dậy và theo dõi kênh thậm chí còn ít thường xuyên hơn. Thật vậy, giấc ngủ này sâu đến mức nếu thiết bị di động di chuyển vào một ô mới trong mạng của nhà mạng

Trong khi ngủ, nó không cần phải thông báo cho trạm gốc mà trước đó nó đã kết nối. Do đó, khi tỉnh dậy định kỳ từ trạng thái ngủ sâu này, thiết bị di động sẽ cần thiết lập lại một kết nối với một trạm gốc (có thể mới) để kiểm tra các thông điệp paging được MME phát sóng đến các trạm gốc gần trạm gốc mà thiết bị di động đã kết nối trước đó. Những thông điệp paging điều khiển này, được các trạm gốc phát sóng tới tất cả các thiết bị di động trong vùng phủ sóng của chúng, cho biết thiết bị di động nào nên hoàn toàn tỉnh dậy và thiết lập lại kết nối dữ liệu với một trạm gốc (xem Hình 7.18) để nhận các gói tin đến.

**7.4.5 Mạng Di Động Toàn Cầu: Một Mạng lưới của các Mạng lưới**

Sau khi đã nghiên cứu kiến trúc mạng di động 4G, hãy lùi lại một bước và xem xét cách mạng di động toàn cầu---tự nó là một "mạng của các mạng" giống như Internet---được tổ chức.

Hình 7.23 cho thấy điện thoại thông minh di động của người dùng được kết nối qua trạm cơ sở 4G vào mạng gia đình của họ. Mạng di động gia đình của người dùng được vận hành bởi một nhà mạng di động

Mạng nhà mạng di động

Cổng

Người đăng ký chính

Máy chủ

Đã truy cập mạng nhà cung cấp di động

Cổng

Internet công cộng

và IPX

*Hình 7.23 ♦ Mạng dữ liệu di động toàn cầu: một mạng lưới các mạng.*

nhà mạng như Verizon, AT&T, T-Mobile hoặc Sprint ở Hoa Kỳ; Orange ở Pháp; hoặc SK Telecom ở Hàn Quốc. Mạng của người dùng tại nhà, lần lượt, được kết nối với các mạng của các nhà mạng di động khác và với Internet toàn cầu, thông qua một hoặc nhiều bộ định tuyến cổng trong mạng tại nhà, như được thể hiện trong Hình 7.23. Các mạng di động tự nó kết nối với nhau thông qua Internet công cộng hoặc thông qua Mạng Trao đổi Giao thức Internet Packet (IPX) \[GSMA 2018a\]. IPX là một mạng được quản lý đặc biệt để kết nối các nhà mạng di động, tương tự như các Điểm Trao đổi Internet (xem Hình 1.15) để kết nối giữa các ISP. Từ Hình 7.23, chúng ta có thể thấy rằng mạng di động toàn cầu thực sự là một "mạng lưới các mạng" --- giống như Internet (nhớ lại Hình 1.15 và Mục 5.4). Các mạng 4G cũng có thể kết nối với các mạng thoại/dữ liệu di động 3G và các mạng chỉ thoại trước đó.

Chúng ta sẽ quay lại sớm với các chủ đề bổ sung về 4G LTE --- quản lý di động trong Mục 7.6, và an ninh 4G trong Mục 8.8.2 --- sau này, sau khi phát triển các nguyên tắc cơ bản cần thiết cho các chủ đề này. Bây giờ hãy cùng xem nhanh các mạng 5G đang nổi lên.

7.4.6 Mạng di động 5G

Dịch vụ dữ liệu diện rộng tối ưu sẽ là dịch vụ có tốc độ kết nối gigabit phổ biến khắp nơi, độ trễ cực thấp và không giới hạn số lượng người dùng và thiết bị có thể được hỗ trợ trong bất kỳ khu vực nào. Dịch vụ như vậy sẽ mở ra cơ hội cho tất cả các loại ứng dụng mới, bao gồm thực tế ảo tăng cường và thực tế ảo phổ biến, điều khiển phương tiện tự hành qua kết nối không dây, điều khiển robot trong các nhà máy qua kết nối không dây, và thay thế các công nghệ truy cập cho hộ gia đình, chẳng hạn như DSL và cáp, bằng các dịch vụ Internet cố định không dây (tức là kết nối không dây cho hộ gia đình từ các trạm gốc đến modem trong nhà).

Dự kiến rằng 5G, với các phiên bản được cải tiến dần có khả năng được triển khai trong thập kỷ 2020, sẽ tiến một bước lớn hướng tới việc đạt được các mục tiêu của dịch vụ dữ liệu khu vực rộng tối ưu. Người ta dự đoán rằng 5G sẽ cung cấp tăng khoảng 10 lần về tốc độ đỉnh, giảm 10 lần độ trễ và tăng 100 lần dung lượng lưu lượng so với 4G \[Qualcomm 2019\].

Về cơ bản, 5G đề cập đến "5G NR (Radio Mới)", là tiêu chuẩn được 3GPP áp dụng. Tuy nhiên, vẫn tồn tại các công nghệ 5G khác ngoài NR. Ví dụ, mạng 5G TF độc quyền của Verizon hoạt động trên các tần số 28 và 39 GHz và chỉ được sử dụng cho dịch vụ Internet không dây cố định, không dùng cho điện thoại thông minh.

Các tiêu chuẩn 5G chia các tần số thành hai nhóm: FR1 (450 MHz--6 GHz) và FR2 (24 GHz--52 GHz). Hầu hết các triển khai ban đầu sẽ nằm trong không gian FR1, mặc dù đã có những triển khai sớm tính đến năm 2020 trong không gian FR2 cho truy cập Internet cố định tại nhà như đã đề cập ở trên. Quan trọng là, các khía cạnh của lớp vật lý (tức là không dây) của 5G không tương thích ngược với các hệ thống truyền thông di động 4G như LTE: cụ thể, nó không thể được cung cấp cho các điện thoại thông minh hiện có chỉ bằng cách nâng cấp trạm gốc hoặc cập nhật phần mềm. Do đó, trong quá trình chuyển đổi sang 5G, các nhà mạng không dây sẽ cần đầu tư đáng kể vào hạ tầng vật lý.

Các tần số FR2 cũng được biết đến như là các tần số sóng milimet. Trong khi các tần số sóng milimet cho phép tốc độ dữ liệu nhanh hơn nhiều, chúng đi kèm với hai nhược điểm chính:

• Tần số sóng milimét có phạm vi ngắn hơn nhiều từ trạm gốc đến thiết bị thu. Điều này làm cho công nghệ sóng milimét không phù hợp ở các khu vực nông thôn và đòi hỏi việc triển khai trạm gốc dày đặc hơn ở các khu vực đô thị. • Liên lạc bằng sóng milimét rất dễ bị ảnh hưởng bởi môi trường khí quyển. Cây cối gần đó và mưa có thể gây ra vấn đề khi sử dụng ngoài trời.

5G không phải là một tiêu chuẩn đồng nhất, mà thay vào đó bao gồm ba tiêu chuẩn cùng tồn tại \[Dahlman 2018\]:

• eMBB (Enhanced Mobile Broadband). Initial deployments of 5G NR have focused on eMBB, which provides for increased bandwidth for higher download and upload speeds, as well as a moderate reduction in latency when compared to 4G LTE. eMBB enables rich media applications, such as mobile augmented reality and virtual reality, as well as mobile 4K resolution and 360° video streaming. • URLLC (Ultra Reliable Low-Latency Communications). URLLC is targeted towards applications that are highly latency-sensitive, such as factory automation and autonomous driving. URLLC is targeting latencies of 1msec. As of this writing, technologies that enable URLLC are still being standardized. • mMTC (Massive Machine Type Communications). mMTC is a narrowband access type for sensing, metering, and monitoring applications. One priority for the design of 5G networks is to lower barriers for network connectivity for IoT devices. In addition to lowering latency, emerging technologies for 5G networks are focusing on reducing power requirements, making the use of IoT devices more pervasive than has been with 4G LTE.

5G và Tần số Sóng Milimet

Nhiều cải tiến của 5G sẽ là kết quả trực tiếp của việc làm việc trong các tần số sóng milimét trong dải 24 GHz--52 GHz. Ví dụ, các tần số này cung cấp khả năng đạt được tăng 100 lần về dung lượng so với 4G. Để có cái nhìn sâu hơn về điều này, dung lượng có thể được định nghĩa là tích của ba đại lượng \[Björnson 2017\]:

dung lượng = mật độ tế bào \* phổ khả dụng \* hiệu suất phổ

nơi mật độ tế bào được tính bằng đơn vị tế bào/km2, phổ khả dụng được tính bằng đơn vị Hertz, và hiệu suất phổ là một phép đo mức độ hiệu quả mà mỗi trạm cơ sở có thể giao tiếp với người dùng và được tính bằng đơn vị bps/Hz/tế bào. Bằng cách nhân các đơn vị này, dễ thấy rằng dung lượng được tính bằng đơn vị bps/km2. Đối với từng thuật ngữ trong ba thuật ngữ này, giá trị sẽ lớn hơn cho 5G so với 4G:

• Bởi vì tần số milimét có phạm vi ngắn hơn nhiều so với tần số 4G LTE, cần nhiều trạm gốc hơn, điều này dẫn đến mật độ tế bào tăng lên. • Bởi vì 5G FR2 hoạt động trong một dải tần số lớn hơn nhiều (52 − 24 = 28 GHz) so với 4G LTE (lên đến khoảng 2 GHz), nó có nhiều phổ khả dụng hơn. • Về hiệu quả phổ, lý thuyết thông tin cho rằng nếu bạn muốn tăng gấp đôi hiệu quả phổ, cần tăng công suất 17 lần \[Björnson 2017\]. Thay vì tăng công suất, 5G sử dụng công nghệ MIMO (cùng công nghệ mà chúng ta đã gặp trong nghiên cứu về mạng 802.11 ở Mục 7.3), sử dụng nhiều anten tại mỗi trạm gốc. Thay vì phát tín hiệu theo mọi hướng, mỗi anten MIMO áp dụng kỹ thuật tạo chùm (beam forming) và hướng tín hiệu đến người dùng. Công nghệ MIMO cho phép một trạm gốc gửi tín hiệu đến 10--20 người dùng cùng một lúc trên cùng dải tần số.

Bằng cách tăng cả ba thành phần trong phương trình dung lượng, 5G được kỳ vọng sẽ cung cấp tăng 100 lần về dung lượng ở các khu vực đô thị. Tương tự, nhờ băng tần rộng hơn nhiều, 5G được kỳ vọng sẽ cung cấp tốc độ tải xuống tối đa 1 Gbps hoặc cao hơn.

Tuy nhiên, tín hiệu sóng milimét dễ bị các tòa nhà và cây cối cản trở. Cần có các trạm tế bào nhỏ để lấp đầy các khoảng trống về phạm vi phủ sóng giữa các trạm cơ sở và người dùng. Ở một khu vực có mật độ dân số cao, khoảng cách giữa hai trạm tế bào nhỏ có thể dao động từ 10 đến 100 mét \[Dahlman 2018\].

Mạng lõi 5G

Mạng lõi 5G là mạng dữ liệu quản lý tất cả các kết nối thoại di động, dữ liệu và Internet của 5G. Mạng lõi 5G đang được thiết kế lại để tích hợp tốt hơn với Internet và các dịch vụ dựa trên đám mây, và cũng bao gồm các máy chủ và bộ nhớ đệm phân tán khắp mạng, do đó giảm độ trễ. Ảo hóa chức năng mạng (như đã thảo luận trong Chương 4 và 5), và chia lát mạng cho các ứng dụng và dịch vụ khác nhau, sẽ được quản lý trong lõi.

Thông số kỹ thuật lõi 5G mới giới thiệu những thay đổi lớn trong cách mạng di động hỗ trợ nhiều loại dịch vụ với hiệu suất khác nhau. Giống như trong trường hợp của mạng lõi 4G (nhớ lại Hình 7.17 và 7.18), lõi 5G chuyển tiếp lưu lượng dữ liệu từ các thiết bị đầu cuối, xác thực thiết bị và quản lý tính di động của thiết bị. Lõi 5G cũng chứa tất cả các thành phần mạng mà chúng ta đã gặp trong Mục 7.4.2---các thiết bị di động, các ô (cell), các trạm gốc, và Thực thể Quản lý Di động (nay được chia thành hai tiểu phần, như đã thảo luận dưới đây), HSS, và các cổng Serving và PDN.

Mặc dù mạng lõi 4G và 5G thực hiện các chức năng tương tự, nhưng có một số khác biệt quan trọng trong kiến trúc lõi 5G mới. Lõi 5G được thiết kế cho việc tách biệt hoàn toàn điều khiển và mặt phẳng người dùng (xem Chương 5). Lõi 5G hoàn toàn bao gồm các chức năng mạng dựa trên phần mềm được ảo hóa. Kiến trúc mới này sẽ cung cấp

các nhà điều hành sự linh hoạt để đáp ứng các yêu cầu đa dạng của các ứng dụng 5G khác nhau. Một số chức năng mạng lõi 5G mới bao gồm \[Rommer 2019\]:

• Chức năng Mặt phẳng Người dùng (UPF). Tách biệt điều khiển và mặt phẳng người dùng (xem Chương 5) cho phép xử lý gói dữ liệu được phân phối và đẩy ra gần biên mạng. • Chức năng Quản lý Truy cập và Di động (AMF). Nucleus 5G về cơ bản phân tách Thực thể Quản lý Di động 4G (MME) thành hai phần chức năng: AMF và SMF. AMF nhận tất cả thông tin kết nối và phiên từ thiết bị người dùng cuối nhưng chỉ xử lý các nhiệm vụ quản lý kết nối và di động. • Chức năng Quản lý Phiên (SMF). Quản lý phiên được thực hiện bởi Chức năng Quản lý Phiên (SMF). SMF chịu trách nhiệm tương tác với mặt phẳng dữ liệu tách rời. SMF cũng thực hiện quản lý địa chỉ IP và đóng vai trò DHCP.

Tính đến thời điểm viết bài này (2020), 5G đang trong giai đoạn đầu triển khai, và nhiều tiêu chuẩn 5G vẫn chưa được hoàn thiện. Chỉ thời gian mới chứng minh liệu 5G có trở thành dịch vụ không dây băng thông rộng phổ biến, liệu nó có cạnh tranh thành công với WiFi cho dịch vụ không dây trong nhà, liệu nó có trở thành một thành phần quan trọng của tự động hóa nhà máy và cơ sở hạ tầng phương tiện tự lái, và liệu nó có đưa chúng ta tiến một bước lớn đến dịch vụ không dây khu vực rộng cuối cùng hay không.

**7.5 Quản lý Di động: Nguyên tắc**

Sau khi đã đề cập đến tính chất không dây của các liên kết truyền thông trong mạng không dây, bây giờ là lúc chúng ta chuyển sự chú ý sang khả năng di động mà các liên kết không dây này mang lại. Theo nghĩa rộng nhất, một thiết bị di động là thiết bị thay đổi điểm kết nối vào mạng theo thời gian. Bởi vì thuật ngữ di động đã mang nhiều ý nghĩa khác nhau trong cả thế giới máy tính lẫn viễn thông, trước tiên chúng ta nên cân nhắc cẩn thận các hình thức của tính di động.

**7.5.1 Tính di động của thiết bị: Góc nhìn từ lớp mạng**

Từ quan điểm của tầng mạng, một thiết bị di động về mặt vật lý sẽ gây ra một tập hợp thách thức rất khác nhau cho tầng mạng, tùy thuộc vào mức độ hoạt động của thiết bị khi nó di chuyển giữa các điểm kết nối với mạng. Ở một đầu của phổ, tình huống (a) trong Hình 7.24 là người dùng di động tự mình di chuyển về mặt vật lý giữa các mạng, nhưng tắt thiết bị di động khi di chuyển. Ví dụ, một sinh viên có thể ngắt kết nối khỏi mạng không dây của lớp học và tắt thiết bị của mình, sau đó đến khu ăn uống và kết nối với điểm truy cập không dây.

kết nối mạng ở đó trong khi ăn, sau đó ngắt kết nối và tắt nguồn khỏi mạng dining commons, đi bộ đến thư viện, và kết nối với mạng không dây của thư viện trong khi học. Từ quan điểm mạng, thiết bị này không di động---nó gắn vào một mạng truy cập và vẫn ở trong mạng truy cập đó khi bật. Trong trường hợp này, thiết bị kết nối tuần tự với, và sau đó ngắt kết nối với, từng mạng truy cập không dây gặp phải. Trường hợp thiết bị (không) di động này có thể được xử lý hoàn toàn bằng các cơ chế mạng mà chúng ta đã học ở Mục 7.3 và 7.4.

Trong tình huống (b) trong Hình 7.24, thiết bị có thể di chuyển về mặt vật lý nhưng vẫn gắn với cùng một mạng truy cập. Thiết bị này cũng không di chuyển từ góc nhìn của tầng mạng. Thêm vào đó, nếu thiết bị vẫn kết nối với cùng một trạm phát 802.11 AP hoặc trạm cơ sở LTE, thiết bị thậm chí còn không di chuyển từ góc nhìn của tầng liên kết.

Từ góc độ mạng, sự quan tâm của chúng ta đối với tính di động của thiết bị thực sự bắt đầu từ trường hợp (c), khi một thiết bị thay đổi mạng truy cập của nó (ví dụ, WLAN 802.11 hoặc trạm LTE) trong khi tiếp tục gửi và nhận các gói IP, và trong khi duy trì các kết nối cấp cao hơn (ví dụ, TCP). Ở đây, mạng sẽ cần cung cấp việc chuyển giao---một quá trình chuyển trách nhiệm chuyển tiếp các gói tin đến/từ một AP hoặc trạm cơ sở sang thiết bị di động---khi thiết bị di chuyển giữa các WLAN hoặc giữa các ô LTE. Chúng ta sẽ trình bày chi tiết về việc chuyển giao trong Mục 7.6. Nếu việc chuyển giao xảy ra trong các mạng truy cập thuộc về cùng một nhà cung cấp mạng, nhà cung cấp đó có thể tự điều phối việc chuyển giao. Khi một thiết bị di động di chuyển giữa nhiều mạng nhà cung cấp, như trong kịch bản (d), các nhà cung cấp phải phối hợp việc chuyển giao cùng nhau, điều này làm cho quá trình chuyển giao trở nên phức tạp hơn nhiều.

**7.5.2 Mạng gia đình và Chuyển vùng trên các mạng đã truy cập**

Như chúng ta đã tìm hiểu trong các thảo luận về mạng di động 4G LTE ở Mục 7.4.1, mỗi thuê bao đều có một "nhà" với một nhà cung cấp dịch vụ di động nào đó. Chúng ta đã tìm hiểu rằng Dịch vụ Thuê bao Nhà (HSS) lưu trữ thông tin về từng thuê bao của mình, bao gồm ID thiết bị duy nhất toàn cầu (nhúng trong thẻ SIM của thuê bao), thông tin về các dịch vụ mà thuê bao có thể truy cập, các khóa mã hóa sẽ được sử dụng cho

\(a\) Khả năng di chuyển của thiết bị giữa các mạng truy cập, nhưng tắt nguồn khi di chuyển giữa các mạng truy cập

\(b\) Chỉ di chuyển thiết bị trong cùng mạng truy cập không dây, trong mạng của một nhà cung cấp duy nhất

\(c\) Khả năng di chuyển của thiết bị giữa các mạng truy cập trong mạng của một nhà cung cấp duy nhất, đồng thời duy trì các kết nối đang hoạt động

\(d\) Tính di động của thiết bị giữa nhiều mạng nhà cung cấp, trong khi vẫn duy trì các kết nối hiện có

*Hình 7.24 ♦ Các mức độ di động khác nhau, từ lớp mạng*

quan điểm

thông tin liên lạc và thông tin thanh toán/chi phí. Khi một thiết bị được kết nối với mạng di động, ngoài mạng gốc của nó, thiết bị đó được cho là đang chuyển vùng trên một mạng đã tham quan. Khi một thiết bị di động kết nối và chuyển vùng trên một mạng đã tham quan, sẽ cần có sự phối hợp giữa mạng gốc và mạng đã tham quan.

Internet không có khái niệm mạnh mẽ một cách tương tự về mạng gia đình hay mạng được ghé thăm. Trong thực tế, mạng gia đình của một sinh viên có thể là mạng do trường của họ vận hành; đối với các chuyên gia di động, mạng gia đình của họ có thể là mạng của công ty họ. Mạng được ghé thăm có thể là mạng của một trường học hoặc một công ty mà họ đang ghé thăm. Nhưng không có khái niệm mạng gia đình/mạng được ghé thăm được nhúng sâu trong kiến trúc của Internet. Giao thức Mobile IP \[Perkins 1998, RFC 5944\], mà chúng tôi sẽ trình bày ngắn gọn trong Mục 7.6, là một đề xuất đã tích hợp mạnh mẽ khái niệm mạng gia đình/mạng được ghé thăm. Nhưng Mobile IP chỉ được triển khai/sử dụng hạn chế trong thực tế. Cũng có những hoạt động đang được thực hiện dựa trên cơ sở hạ tầng IP hiện có nhằm cung cấp truy cập mạng xác thực trên các mạng IP được ghé thăm. Eduroam \[Eduroam 2020\] là một trong những hoạt động như vậy.

Khái niệm về một thiết bị di động có một mạng gia đình mang lại hai lợi ích quan trọng: mạng gia đình cung cấp một vị trí duy nhất nơi có thể tìm thấy thông tin về thiết bị đó, và (như chúng ta sẽ thấy) nó có thể phục vụ như một điểm điều phối cho việc liên lạc tới/ từ một thiết bị di động đang đi lại.

Để hiểu giá trị tiềm năng của điểm trung tâm về thông tin và phối hợp, hãy xem xét phép ẩn dụ con người về một người trưởng thành độ tuổi 20 là Bob chuyển ra khỏi nhà gia đình. Bob trở nên linh động, sống ở nhiều ký túc xá và căn hộ khác nhau, và thường thay đổi địa chỉ. Nếu một người bạn cũ là Alice muốn liên lạc, làm sao Alice có thể tìm được địa chỉ hiện tại của Bob? Một cách phổ biến là liên hệ với gia đình, vì một người trưởng thành độ tuổi 20 thường đăng ký địa chỉ hiện tại với gia đình (nếu không vì lý do nào khác thì cũng để cha mẹ có thể gửi tiền giúp trả tiền thuê nhà!). Ngôi nhà gia đình trở thành địa điểm duy nhất mà người khác có thể đến như bước đầu tiên để liên lạc với Bob. Thêm vào đó, việc liên lạc qua bưu điện sau này từ Alice có thể là gián tiếp (ví dụ, thư gửi trước đến nhà gia đình của Bob rồi được chuyển tiếp cho Bob) hoặc trực tiếp (ví dụ, Alice sử dụng địa chỉ nhận được từ cha mẹ của Bob để gửi thư trực tiếp cho Bob).

**7.5.3 Định tuyến Trực tiếp và Gián tiếp đến/đi từ Thiết bị Di động**

Bây giờ chúng ta hãy xem xét một vấn đề nan giải mà máy chủ kết nối Internet (mà chúng ta sẽ gọi là một máy tương tác) trong Hình 7.25 gặp phải khi muốn giao tiếp với một thiết bị di động có thể nằm trong mạng viễn thông di động gốc của thiết bị đó, hoặc có thể đang di chuyển trong một mạng được thăm. Trong phần phát triển dưới đây, chúng ta sẽ áp dụng một góc nhìn mạng di động 4G/5G, vì các mạng này có lịch sử lâu dài trong việc hỗ trợ tính di động của thiết bị. Nhưng như chúng ta sẽ thấy, những thách thức cơ bản và các cách tiếp cận giải pháp cơ bản để hỗ trợ tính di động của thiết bị đều có thể áp dụng tương đương trong cả mạng di động và Internet.

Như được thể hiện trong Hình 7.25, chúng ta sẽ giả định rằng thiết bị di động có một định danh duy nhất trên toàn cầu liên kết với nó. Trong các mạng di động 4G, LTE (xem Mục 7.4),

điều này sẽ là Số Nhận dạng Người đăng ký Di động Quốc tế (IMSI) và một số điện thoại liên quan, được lưu trên thẻ SIM của thiết bị di động. Đối với người dùng Internet di động, đây sẽ là một địa chỉ IP cố định trong phạm vi địa chỉ IP của mạng gốc của nó, như trong trường hợp kiến trúc Di động IP.

Những phương pháp nào có thể được sử dụng trong kiến trúc mạng di động để cho phép một datagram được gửi bởi người liên lạc đến thiết bị di động đó? Ba phương pháp cơ bản có thể được xác định và được thảo luận dưới đây. Như chúng ta sẽ thấy, hai phương pháp cuối cùng trong số này được áp dụng trong thực tế.

Tận dụng cơ sở hạ tầng địa chỉ IP hiện có

Có lẽ cách đơn giản nhất để định tuyến đến một thiết bị di động trong một mạng đã ghé thăm là đơn giản sử dụng cơ sở hạ tầng địa chỉ IP hiện có---không thêm gì mới vào kiến trúc. Còn gì dễ dàng hơn!

Hãy nhớ lại từ cuộc thảo luận của chúng ta về Hình 4.21 rằng một ISP sử dụng BGP để quảng bá các tuyến đến các mạng đích bằng cách liệt kê các phạm vi địa chỉ đã được CIDR hóa của các mạng có thể truy cập. Do đó, một mạng đã được ghé thăm có thể quảng bá đến tất cả các mạng khác rằng một

Mạng gia đình

cổng

Mạng đã truy cập

79.129/16 Mạng Gia Đình

128.119/16

Mạng đã truy cập

cổng

Quản lý di động Người đăng ký tại nhà

Dịch vụ

Phóng viên

Công khai hay riêng tư

Internet

Quản lý di chuyển

NAT IP: 10.0.0.99 IMSI 78:4f:43:98:d9:27

Thường trú IP: 128.119.40.186 IMSI 78:4f:43:98:d9:27

*Hình 7.25 ♦ Các yếu tố của kiến trúc mạng di động*

thiết bị di động cụ thể cư trú trong mạng của nó chỉ bằng cách quảng bá một địa chỉ rất cụ thể---địa chỉ vĩnh viễn 32-bit IP đầy đủ của thiết bị di động---về cơ bản thông báo cho các mạng khác rằng nó có đường đi để sử dụng nhằm chuyển tiếp các gói dữ liệu đến thiết bị di động đó. Các mạng lân cận sau đó sẽ lan truyền thông tin định tuyến này khắp mạng như một phần của quy trình BGP bình thường để cập nhật thông tin định tuyến và bảng chuyển tiếp. Vì các gói dữ liệu sẽ luôn được chuyển tiếp đến bộ định tuyến quảng bá điểm đến cụ thể nhất cho địa chỉ đó (xem Mục 4.3), tất cả các gói dữ liệu gửi đến thiết bị di động đó sẽ được chuyển tiếp tới mạng đã ghé thăm. Nếu thiết bị di động rời khỏi một mạng đã ghé thăm và tham gia một mạng khác, mạng đã ghé thăm mới có thể quảng bá một tuyến đường mới, rất cụ thể đến thiết bị di động, và mạng đã ghé thăm cũ có thể rút thông tin định tuyến của nó liên quan đến thiết bị di động.

Điều này giải quyết hai vấn đề cùng một lúc, và thực hiện mà không cần thay đổi cơ sở hạ tầng lớp mạng! Các mạng khác biết vị trí của thiết bị di động, và việc định tuyến các gói dữ liệu tới thiết bị di động trở nên dễ dàng, vì bảng chuyển tiếp sẽ chỉ dẫn các gói dữ liệu đến mạng mà thiết bị đang ghé thăm. Tuy nhiên, nhược điểm nghiêm trọng là vấn đề khả năng mở rộng---các bộ định tuyến mạng sẽ phải duy trì các mục trong bảng chuyển tiếp cho có thể là hàng tỷ thiết bị di động, và cập nhật mục của thiết bị mỗi khi thiết bị di chuyển sang mạng khác. Rõ ràng, phương pháp này sẽ không hoạt động trong thực tế. Một số nhược điểm bổ sung được khám phá trong các bài toán ở cuối chương này.

Một phương pháp thay thế, thực tế hơn (và một phương pháp đã được áp dụng trong thực tế) là chuyển chức năng di động từ lõi mạng ra biên mạng---một chủ đề lặp lại trong nghiên cứu kiến trúc Internet của chúng ta. Một cách tự nhiên để làm điều này là thông qua mạng gốc của thiết bị di động. Tương tự như cách cha mẹ theo dõi vị trí của con cái 20 tuổi, một thực thể quản lý di động (MME) trong mạng gốc của thiết bị di động có thể theo dõi mạng mà thiết bị di động đang truy cập. Thông tin này có thể được lưu trữ trong cơ sở dữ liệu, được hiển thị là cơ sở dữ liệu HSS trong Hình 7.25. Cần có một giao thức hoạt động giữa mạng truy cập và mạng gốc để cập nhật mạng mà thiết bị di động đang truy cập. Bạn có thể nhớ rằng chúng ta đã gặp các thành phần MME và HSS trong nghiên cứu về 4G LTE. Chúng ta sẽ tái sử dụng tên các thành phần này ở đây, vì chúng rất mô tả, và cũng bởi vì chúng được triển khai rộng rãi trong các mạng 4G.

Let's next consider the visited network elements shown in Figure 7.25 in more detail. The mobile device will clearly need an IP address in the visited network. The possibilities here include using a permanent address associated with the mobile device's home network, allocating a new address in the address range of the visited network, or providing an IP address via NAT (see Section 4.3.4). In the latter two cases, a mobile device has a transient identifier (a newly allocated IP address) in addition to its permanent identifiers stored in the HSS in its home network. These cases are analogous to a writer addressing a letter to the address of the house in which our mobile 20-something adult is currently living. In the case of a NAT address, datagrams destined to the mobile device would eventually reach the NAT gateway router in the visited network, which would then perform NAT address translation and forward the datagram to the mobile device.

Chúng ta hiện đã thấy một số thành phần của giải pháp cho bài toán nan giải của liên lạc viên trong Hình 7.24: mạng gốc và mạng được truy cập, MME và HSS, và địa chỉ thiết bị di động. Nhưng làm thế nào để các gói tin được địa chỉ và chuyển tiếp đến thiết bị di động? Vì chỉ HSS (chứ không phải các bộ định tuyến toàn mạng) biết vị trí của thiết bị di động, một liên lạc viên không thể đơn giản gửi gói tin đến địa chỉ vĩnh viễn của thiết bị di động và đưa nó vào mạng. Một số điều khác phải được thực hiện. Có thể xác định hai phương pháp: định tuyến gián tiếp và định tuyến trực tiếp.

Định tuyến gián tiếp tới thiết bị di động

Hãy cùng xem xét lại người tương tác muốn gửi một gói dữ liệu tới thiết bị di động. Trong phương pháp định tuyến gián tiếp, người tương tác chỉ cần đặt địa chỉ gói dữ liệu tới địa chỉ cố định của thiết bị di động và gửi gói dữ liệu vào mạng, hoàn toàn không biết liệu thiết bị di động có đang ở mạng nhà hay ở mạng khách; do đó, tính di động hoàn toàn minh bạch đối với người tương tác. Các gói dữ liệu như vậy trước tiên được định tuyến, như thường lệ, tới mạng nhà của thiết bị di động. Điều này được minh họa trong bước 1 trong Hình 7.26.

Cổng mạng gia đình

Mạng đã truy cập

79.129/16 Mạng Gia Đình

128.119/16

Đã truy cập cổng mạng

Quản lý di chuyển

Người đăng ký chính

Dịch vụ

Phóng viên

Quản lý di chuyển

NAT IP: 10.0.0.99 IMSI 78:4f:43:98:d9:27

Thường trú IP: 128.119.40.186 IMSI 78:4f:43:98:d9:27

4b

4a

*Hình 7.26 ♦ Định tuyến gián tiếp tới thiết bị di động*

Bây giờ chúng ta hãy chuyển sự chú ý sang HSS, chịu trách nhiệm tương tác với các mạng đã ghé thăm để theo dõi vị trí của thiết bị di động, và router cổng của mạng gốc. Một nhiệm vụ của router cổng này là phải chú ý đến việc nhận datagram gửi đến một thiết bị có mạng gốc trong mạng đó, nhưng hiện đang ở trong một mạng đã ghé thăm. Router cổng của mạng gốc sẽ chặn datagram này, tham khảo với HSS để xác định mạng đã ghé thăm mà thiết bị di động đang cư trú, và chuyển tiếp datagram về phía router cổng của mạng đã ghé thăm---bước 2 trong Hình 7.26. Router cổng của mạng đã ghé thăm sau đó chuyển tiếp datagram về phía thiết bị di động---bước 3 trong Hình 7.26. Nếu sử dụng dịch NAT, như trong Hình 7.26, router cổng của mạng đã ghé thăm thực hiện dịch NAT.

It is instructive to consider the rerouting at the home network in bit more detail. Clearly, the home network gateway will need to forward the arriving datagram to the gateway router in the visited network. On the other hand, it is desirable to leave the correspondent's datagram intact, since the application receiving the datagram should be unaware that the datagram was forwarded via the home network. Both goals can be satisfied by having the home gateway encapsulate the correspondent's original complete datagram within a new (larger) datagram. This larger datagram is then addressed and delivered to the visited network's gateway router, which will decapsulate the datagram---that is, remove the correspondent's original datagram from within the larger encapsulating datagram---and forward (step 3 in Figure 7.26) the original datagram to the mobile device. The sharp reader will note that the encapsulation/decapsulation described here is precisely the notion of tunneling, discussed in Section 4.3 in the context of IPv6; indeed, we also discussed the use of tunneling in the context of Figure 7.18, when we introduced the 4G LTE data plane.

Cuối cùng, hãy xem xét cách thiết bị di động gửi các gói dữ liệu đến bên liên lạc. Trong bối cảnh của Hình 7.26, thiết bị di động rõ ràng sẽ cần phải chuyển tiếp gói dữ liệu thông qua bộ định tuyến cổng mạng đã được ghé thăm, để thực hiện dịch NAT. Nhưng sau đó, bộ định tuyến cổng mạng đã ghé thăm nên chuyển tiếp gói dữ liệu đến bên liên lạc như thế nào? Như được thể hiện trong Hình 7.26, có hai lựa chọn ở đây: (4a) gói dữ liệu có thể được đóng gói trở lại bộ định tuyến cổng nhà và gửi đến bên liên lạc từ đó, hoặc (4b) gói dữ liệu có thể được truyền trực tiếp từ mạng đã ghé thăm đến bên liên lạc---một phương pháp được biết đến là tách địa phương \[GSMA 2019a\] trong LTE. Hãy tóm tắt cuộc thảo luận của chúng ta về định tuyến gián tiếp bằng cách xem lại chức năng tầng mạng mới cần thiết để hỗ trợ khả năng di chuyển.

• Một giao thức liên kết thiết bị di động với mạng đã thăm. Thiết bị di động sẽ cần liên kết với mạng đã thăm, và tương tự sẽ cần ngắt liên kết khi rời khỏi mạng đã thăm. • Một giao thức đăng ký từ mạng đã thăm đến HSS của mạng gốc. Mạng đã thăm sẽ cần đăng ký vị trí của thiết bị di động với HSS trong mạng gốc, và có thể sử dụng thông tin thu được từ HSS để thực hiện xác thực thiết bị.

• Một giao thức tạo kênh đóng gói datagram giữa cổng mạng tại nhà và bộ định tuyến cổng mạng của mạng được ghé thăm. Bên gửi thực hiện đóng gói và chuyển tiếp datagram gốc của người liên lạc; ở phía nhận, bộ định tuyến cổng thực hiện tháo gói, dịch NAT, và chuyển tiếp datagram gốc đến thiết bị di động.

The previous discussion provides all the needed elements for a mobile device to maintain an ongoing connection with a correspondent as the device moves among networks. When a device roams from one visited network to another, the new visited network information needs to be updated in the home network HSS, and the homegateway-router-to-visited-gateway-router tunnel endpoint needs to be moved. But will the mobile device see an interrupted flow of datagrams as it moves between networks? As long as the time between the mobile device disconnection from one visited network and its attachment to the next visited network is small, few datagrams will be lost. Recall from Chapter 3 that end-to-end connections can experience datagram loss due to network congestion. Hence, occasional datagram loss within a connection when a device moves between networks is by no means a catastrophic problem. If loss-free communication is required, upper-layer mechanisms will recover from datagram loss, whether such loss results from network congestion or from device mobility.

Cuộc thảo luận của chúng ta ở trên đã được thực hiện một cách khá chung chung. Một phương pháp định tuyến gián tiếp được sử dụng trong tiêu chuẩn di động IP \[RFC 5944\], cũng như trong các mạng 4G LTE \[Sauter 2014\]. Chi tiết của chúng, đặc biệt là các thủ tục tạo đường hầm được sử dụng, chỉ khác một chút so với cuộc thảo luận chung của chúng ta ở trên.

Định tuyến trực tiếp đến thiết bị di động

Phương pháp định tuyến gián tiếp được minh họa trong Hình 7.26 gặp phải một sự kém hiệu quả được gọi là vấn đề định tuyến tam giác---các gói dữ liệu được gửi đến thiết bị di động phải được chuyển tiếp trước đến mạng nhà và sau đó đến mạng đang thăm, ngay cả khi có một lộ trình hiệu quả hơn nhiều giữa thiết bị di động đang hoạt động và người gửi dữ liệu. Trong trường hợp xấu nhất, hãy tưởng tượng một người dùng di động đang hoạt động trên cùng một mạng mà là mạng nhà của một đồng nghiệp ở nước ngoài mà người dùng di động của chúng ta đang thăm. Hai người đang ngồi cạnh nhau và trao đổi dữ liệu. Datagrams giữa người dùng di động và đồng nghiệp ở nước ngoài của anh ta sẽ được chuyển tiếp đến mạng nhà của người dùng di động và sau đó lại quay trở lại mạng đang thăm!

Định tuyến trực tiếp khắc phục sự kém hiệu quả của định tuyến tam giác, nhưng điều đó phải trả bằng chi phí phức tạp bổ sung. Trong phương pháp định tuyến trực tiếp, được minh họa trong Hình 7.27, tương tác trước tiên phát hiện mạng mà thiết bị di động đang cư trú. Điều này được thực hiện bằng cách truy vấn HSS trong mạng nhà của thiết bị di động, giả sử (như trong trường hợp định tuyến gián tiếp) rằng mạng mà thiết bị di động đang thăm quan đã được đăng ký trong HSS. Điều này được thể hiện ở các bước 1 và 2 trong Hình 7.27. Sau đó, tương tác chuyển tiếp các datagram từ mạng của nó trực tiếp đến bộ định tuyến gateway trong mạng mà thiết bị di động đang thăm quan.

Trong khi định tuyến trực tiếp khắc phục được vấn đề định tuyến tam giác, nó lại đưa ra hai thách thức quan trọng bổ sung:

• Một giao thức vị trí người dùng di động là cần thiết để đối tác liên lạc truy vấn HSS nhằm lấy mạng đã ghé thăm của thiết bị di động (bước 1 và 2 trong Hình 7.27). Điều này bổ sung cho giao thức cần thiết để thiết bị di động đăng ký vị trí của mình với HSS của nó. • Khi thiết bị di động di chuyển từ mạng đã ghé thăm này sang mạng đã ghé thăm khác, đối tác liên lạc sẽ biết như thế nào để chuyển các gói dữ liệu đến mạng đã ghé thăm mới? Trong trường hợp định tuyến gián tiếp, vấn đề này đã được giải quyết dễ dàng bằng cách cập nhật HSS trong mạng gốc và thay đổi điểm cuối của đường hầm để kết thúc tại bộ định tuyến cổng của mạng đã ghé thăm mới. Tuy nhiên, với định tuyến trực tiếp, thay đổi mạng đã ghé thăm này không dễ xử lý như vậy, vì HSS chỉ được đối tác liên lạc truy vấn vào đầu phiên. Do đó, cần có các cơ chế giao thức bổ sung để chủ động cập nhật cho đối tác liên lạc mỗi khi thiết bị di động di chuyển. Hai bài toán ở cuối chương này khám phá các giải pháp cho vấn đề này.

Cổng mạng gia đình

Mạng đã truy cập

79.129/16 Mạng Gia Đình

128.119/16

Đã truy cập cổng mạng

Người đăng ký chính

Dịch vụ

Phóng viên

Quản lý di chuyển

NAT IP: 10.0.0.99 IMSI 78:4f:43:98:d9:27

Thường trú IP: 128.119.40.186 IMSI 78:4f:43:98:d9:27

Quản lý di chuyển

*Hình 7.27 ♦ Định tuyến trực tiếp đến thiết bị di động*

**7.6 Quản lý Di động trong Thực tiễn**

Trong phần trước, chúng ta đã xác định những thách thức cơ bản chính và các giải pháp tiềm năng trong việc phát triển kiến trúc mạng để hỗ trợ khả năng di chuyển của thiết bị: khái niệm về mạng nhà và mạng đến thăm; vai trò của mạng nhà như một điểm trung tâm thông tin và kiểm soát cho các thiết bị di động đăng ký vào mạng nhà đó; các chức năng điều khiển cần thiết bởi thực thể quản lý di động của mạng nhà để theo dõi thiết bị di động khi nó di chuyển giữa các mạng đến thăm; và các cách tiếp cận mặt dữ liệu như định tuyến trực tiếp và gián tiếp để cho phép một thiết bị tương tác và một thiết bị di động trao đổi các gói dữ liệu. Bây giờ hãy xem cách các nguyên tắc này được áp dụng vào thực tế! Trong Mục 7.2.1, chúng ta sẽ nghiên cứu quản lý di động trong mạng 4G/5G; trong Mục 7.2.1, chúng ta sẽ xem Mobile IP, được đề xuất cho Internet.

**7.6.1 Quản lý di động trong mạng 4G/5G**

Nghiên cứu trước đây của chúng tôi về các kiến trúc 4G và 5G đang nổi lên trong Mục 7.4 đã làm quen với chúng tôi với tất cả các phần tử mạng đóng vai trò trung tâm trong quản lý di động 4G/5G. Bây giờ chúng ta hãy minh họa cách các phần tử đó tương tác với nhau để cung cấp dịch vụ di động trong các mạng 4G/5G hiện nay \[Sauter 2014; GSMA 2019b\], vốn có nguồn gốc từ các mạng dữ liệu và thoại di động 3G trước đó \[Sauter 2014\], và thậm chí còn từ các mạng thoại chỉ 2G trước đó \[Mouly 1992\]. Điều này sẽ giúp chúng ta tổng hợp những gì đã học được cho đến nay, cho phép chúng ta giới thiệu một vài chủ đề nâng cao hơn, và cung cấp một cái nhìn vào những gì có thể xảy ra với quản lý di động 5G.

Hãy xem xét một kịch bản đơn giản trong đó một người dùng di động (ví dụ, một hành khách trong ô tô), với một điện thoại thông minh kết nối với mạng 4G/5G đang truy cập, bắt đầu phát trực tuyến một video HD từ một máy chủ từ xa, và sau đó di chuyển từ vùng phủ sóng của một trạm gốc 4G/5G sang trạm khác. Bốn bước chính trong kịch bản này được hiển thị trong Hình 7.28:

1\. Liên kết thiết bị di động và trạm gốc. Thiết bị di động liên kết với

một trạm gốc trong mạng được truy cập. 2. Cấu hình mặt điều khiển của các phần tử mạng cho thiết bị di động. The

mạng đã truy cập và mạng gia đình thiết lập trạng thái mặt điều khiển chỉ ra rằng thiết bị di động đang cư trú trong mạng đã truy cập. 3. Cấu hình mặt dữ liệu của các đường hầm chuyển tiếp cho thiết bị di động. Mạng đã

mạng được liên kết và mạng gia đình thiết lập các đường hầm mà qua đó thiết bị di động và máy chủ truyền phát có thể gửi/nhận các gói dữ liệu IP, sử dụng định tuyến gián tiếp thông qua cổng Mạng Dữ liệu Packet của mạng gia đình (P-GW). 4. Chuyển giao thiết bị di động từ một trạm gốc sang trạm khác. Thiết bị di động

thay đổi điểm kết nối của nó với mạng được truy cập, thông qua việc chuyển giao từ một trạm gốc sang trạm gốc khác.

Bây giờ hãy xem xét từng bước trong bốn bước này chi tiết hơn.

1\. Liên kết trạm gốc. Hãy nhớ rằng trong Mục 7.4.2, chúng ta đã nghiên cứu các thủ tục mà qua đó thiết bị di động liên kết với trạm gốc. Chúng ta đã biết rằng thiết bị di động lắng nghe tất cả các tần số để nhận các tín hiệu chính được truyền từ các trạm gốc trong khu vực của nó. Thiết bị di động dần dần thu thập thêm thông tin về các trạm gốc này, cuối cùng chọn trạm gốc mà nó sẽ liên kết, và thiết lập kênh điều khiển-tín hiệu với trạm gốc đó. Là một phần của liên kết này, thiết bị di động cung cấp cho trạm gốc Mã số thuê bao di động quốc tế (IMSI) của nó, thứ định danh duy nhất cho thiết bị di động cũng như mạng gốc và các thông tin thuê bao bổ sung khác.

2\. Cấu hình mặt điều khiển của các phần tử mạng LTE cho thiết bị di động. Khi kênh tín hiệu từ thiết bị di động đến trạm gốc đã được thiết lập, trạm gốc có thể liên hệ với MME trong mạng đang thăm. MME sẽ tham khảo và cấu hình một số phần tử 4G/5G trong cả mạng gốc và mạng đang thăm để thiết lập trạng thái thay mặt cho nút di động:

• MME sẽ sử dụng IMSI và các thông tin khác do thiết bị di động cung cấp để truy xuất thông tin xác thực, mã hóa và dịch vụ mạng có sẵn cho thuê bao đó. Thông tin đó có thể nằm trong bộ nhớ đệm cục bộ của MME, được truy xuất từ một MME khác mà thiết bị di động đã liên hệ gần đây, hoặc được truy xuất từ HSS trong mạng gốc của thiết bị di động. Quá trình xác thực lẫn nhau (mà chúng ta sẽ trình bày chi tiết hơn trong Mục 8.8) đảm bảo rằng

Mạng đã truy cập

Cổng PDN

(P-GW)

Máy chủ truyền phát

Mạng Internet gia đình

Cổng PDN

(P-GW)

Cổng phục vụ (S-GW)

Trạm gốc

HSS MME

Trạm gốc

*Hình 7.28 ♦ Một ví dụ về kịch bản di động 4G/5G*

mạng được ghé thăm chắc chắn về danh tính của thiết bị di động và rằng thiết bị có thể xác thực mạng mà nó đang kết nối. • MME thông báo cho HSS trong mạng gốc của thiết bị di động rằng thiết bị di động hiện đang cư trú trong mạng được ghé thăm, và HSS cập nhật cơ sở dữ liệu của nó. • Trạm gốc và thiết bị di động chọn các tham số cho kênh dữ liệu sẽ được thiết lập giữa thiết bị di động và trạm gốc (nhớ rằng một kênh tín hiệu điều khiển đã đang hoạt động).

3\. Cấu hình mặt phẳng dữ liệu của các đường hầm chuyển tiếp cho thiết bị di động. MME tiếp theo cấu hình mặt phẳng dữ liệu cho thiết bị di động, như được minh họa trong Hình 7.29. Hai đường hầm được thiết lập. Một đường hầm là giữa trạm gốc và một Serving Gateway trong mạng đã ghé thăm. Đường hầm thứ hai là giữa Serving Gateway đó và bộ định tuyến PDN Gateway trong mạng gốc của thiết bị di động. 4G LTE thực hiện hình thức định tuyến gián tiếp đối xứng này --- tất cả lưu lượng đến/từ thiết bị di động sẽ được dẫn qua mạng gốc của thiết bị. Các đường hầm 4G/5G sử dụng Giao thức Đường hầm GPRS (GTP), được quy định trong \[3GPP GTPv1-U 2019\]. ID Điểm Kết Thúc Đường Hầm (TEID) trong tiêu đề GTP chỉ ra đường hầm mà một gói dữ liệu thuộc về, cho phép nhiều luồng được ghép kênh và tách kênh bởi GTP giữa các điểm kết thúc đường hầm.

Việc so sánh cấu hình của các đường hầm trong Hình 7.29 (trường hợp di động di chuyển trong mạng thăm) với Hình 7.18 (trường hợp di động) là có tính hướng dẫn.

Mạng đã truy cập

Cổng PDN (P-GW)

Máy chủ truyền phát

Mạng Internet gia đình

Cổng PDN

(P-GW)

Cổng phục vụ (S-GW)

Trạm gốc

MME

Trạm gốc

*Hình 7.29 ♦ Đường hầm trong mạng 4G/5G giữa Máy chủ phục vụ*

Cổng mạng trong mạng đã truy cập và cổng PDN trong mạng gốc

chỉ trong mạng gốc của thiết bị di động). Chúng ta thấy rằng trong cả hai trường hợp, Serving Gateway cùng tồn tại trong mạng với thiết bị di động, nhưng PDN Gateway (luôn luôn là PDN Gateway trong mạng gốc của thiết bị di động) có thể ở một mạng khác với thiết bị di động. Đây chính xác là định tuyến gián tiếp. Một phương án thay thế cho định tuyến gián tiếp, được biết đến như local breakout \[GSMA 2019a\], đã được chỉ định trong đó Serving Gateway thiết lập một đường hầm tới PDN Gateway trong mạng địa phương, mạng ghé thăm. Tuy nhiên, trong thực tế, local breakout không được sử dụng rộng rãi \[Sauter 2014\].

Khi các đường hầm đã được cấu hình và kích hoạt, thiết bị di động bây giờ có thể chuyển tiếp các gói tin đến/từ Internet thông qua cổng PDN trong mạng nhà của nó!

4\. Quản lý chuyển giao. Một lần chuyển giao xảy ra khi thiết bị di động thay đổi liên kết của nó từ một trạm cơ sở sang trạm cơ sở khác. Quá trình chuyển giao được mô tả dưới đây là như nhau, bất kể thiết bị di động đang ở trong mạng gốc của nó hay đang đi lạc sang một mạng thăm.

Như minh họa trong Hình 7.30, các gói dữ liệu đến/đi từ thiết bị ban đầu (trước khi chuyển giao) được chuyển tiếp đến thiết bị di động thông qua một trạm gốc (mà chúng ta sẽ gọi là trạm gốc nguồn), và sau khi chuyển giao được định tuyến đến thiết bị di động thông qua một trạm gốc khác (mà chúng ta sẽ gọi là trạm gốc đích). Như chúng ta sẽ thấy, việc chuyển giao giữa các trạm gốc không chỉ dẫn đến việc thiết bị di động truyền/nhận tới/từ một trạm gốc mới mà còn dẫn đến thay đổi phía trạm gốc của đường hầm từ Serving-Gateway đến trạm gốc trong Hình 7.29. Trong trường hợp đơn giản nhất của

Cổng PDN

(P-GW)

Cổng phục vụ (S-GW)

MME

Trạm gốc nguồn

Cơ sở mục tiêu

trạm

*Hình 7.30 ♦ Các bước trong việc bàn giao thiết bị di động từ nguồn*

trạm gốc đến trạm gốc mục tiêu

chuyển giao, khi hai trạm cơ sở ở gần nhau và thuộc cùng một mạng, tất cả các thay đổi xảy ra do chuyển giao do đó tương đối cục bộ. Cụ thể, cổng PDN đang được sử dụng bởi Gateway Phục vụ vẫn hoàn toàn không biết về tính di động của thiết bị. Tất nhiên, các kịch bản chuyển đổi phức tạp hơn sẽ yêu cầu sử dụng các cơ chế phức tạp hơn \[Sauter 2014; GSMA 2019a\].

There may be several reasons for handover to occur. For example, the signal between the current base station and the mobile may have deteriorated to such an extent that communication is severely impaired. Or a cell may have become overloaded, handling a large amount of traffic; handing over mobile devices to less congested nearby cells may alleviate this congestion. A mobile device periodically measures characteristics of a beacon signal from its current base station as well as signals from nearby base stations that it can "hear." These measurements are reported once or twice a second to the mobile device's current (source) base station. Based on these measurements, the current loads of mobiles in nearby cells, and other factors, the source base station may choose to initiate a handover. The 4G/5G standards do not specify a specific algorithm to be used by a base station to determine whether or not to perform handover, or which target base station to choose; this is an active area of research \[Zheng 2008; Alexandris 2016\].

Hình 7.30 minh họa các bước liên quan khi trạm gốc nguồn quyết định chuyển giao một thiết bị di động cho trạm gốc mục tiêu.

1\. Trạm gốc (nguồn) hiện tại chọn trạm gốc mục tiêu, và gửi một

Thông điệp Yêu cầu Chuyển giao đến trạm cơ sở mục tiêu. 2. Trạm cơ sở mục tiêu kiểm tra xem liệu nó có tài nguyên để hỗ trợ thiết bị di động hay không

thiết bị và các yêu cầu về chất lượng dịch vụ của nó. Nếu có, nó sẽ phân bổ trước các tài nguyên kênh (ví dụ: khe thời gian) trên mạng truy cập vô tuyến của mình và các tài nguyên khác cho thiết bị đó. Việc phân bổ tài nguyên trước này giúp thiết bị di động không phải trải qua giao thức kết nối với trạm gốc tốn thời gian đã được thảo luận trước đó, cho phép việc chuyển giao được thực hiện nhanh nhất có thể. Trạm gốc mục tiêu trả lời trạm gốc nguồn bằng thông điệp Xác nhận Yêu cầu Chuyển giao, chứa tất cả thông tin tại trạm gốc mục tiêu mà thiết bị di động sẽ cần để kết nối với trạm gốc mới. 3. Trạm gốc nguồn nhận được Xác nhận Yêu cầu Chuyển giao

tin nhắn và thông báo cho thiết bị di động về danh tính của trạm gốc mục tiêu và thông tin truy cập kênh. Tại thời điểm này, thiết bị di động có thể bắt đầu gửi/nhận các gói dữ liệu đến/từ trạm gốc mục tiêu mới. Theo quan điểm của thiết bị di động, việc chuyển giao bây giờ đã hoàn tất! Tuy nhiên, vẫn còn một số công việc cần làm trong mạng. 4. Trạm gốc nguồn cũng sẽ ngừng chuyển tiếp các gói dữ liệu đến thiết bị di động

thiết bị và thay vào đó chuyển tiếp bất kỳ gói dữ liệu nào được đóng gói mà nó nhận được đến trạm gốc mục tiêu, trạm này sau đó sẽ chuyển tiếp các gói dữ liệu này đến thiết bị di động. 5. Trạm gốc mục tiêu thông báo cho MME rằng nó (trạm gốc mục tiêu) sẽ

trạm gốc mới phục vụ thiết bị di động. MME, lần lượt, phát tín hiệu

tới Cổng phục vụ và trạm gốc mục tiêu để cấu hình lại đường hầm từ Cổng phục vụ đến trạm gốc để kết thúc tại trạm gốc mục tiêu, thay vì tại trạm gốc nguồn. 6. Trạm gốc mục tiêu xác nhận lại với trạm gốc nguồn rằng đường hầm

đã được cấu hình lại, cho phép trạm gốc nguồn giải phóng tài nguyên liên quan đến thiết bị di động đó. 7. Tại thời điểm này, trạm gốc mục tiêu cũng có thể bắt đầu gửi các gói dữ liệu đến

thiết bị di động, bao gồm các datagram được trạm gốc gửi đến trạm cơ sở mục tiêu trong quá trình chuyển vùng, cũng như các datagram mới đến trên đường hầm được cấu hình lại từ Gateway Phục vụ. Nó cũng có thể chuyển tiếp các datagram đi nhận được từ thiết bị di động vào đường hầm đến Gateway Phục vụ.

Các cấu hình chuyển vùng trong các mạng 4G LTE hiện nay, như đã được thảo luận ở trên, cũng sẽ được sử dụng trong các mạng 5G mới nổi trong tương lai \[GSMA 2019c\]. Tuy nhiên, hãy nhớ rằng, từ phần thảo luận của chúng ta ở Mục 7.4.6, các mạng 5G sẽ dày đặc hơn, với kích thước ô nhỏ hơn đáng kể. Điều này sẽ khiến việc chuyển giao trở thành một chức năng mạng quan trọng hơn rất nhiều. Ngoài ra, độ trễ chuyển giao thấp sẽ rất quan trọng đối với nhiều ứng dụng thời gian thực 5G. Việc di chuyển plane điều khiển mạng di động sang khung SDN mà chúng ta đã nghiên cứu trước đó trong Chương 5 \[GSMA 2018b; Condoluci 2018\] hứa hẹn sẽ cho phép triển khai plane điều khiển mạng di động 5G có dung lượng cao hơn và độ trễ thấp hơn. Việc áp dụng SDN trong ngữ cảnh 5G là chủ đề của nhiều nghiên cứu \[Giust 2015; Ordonez-Lucena 2017; Nguyen 2016\].

**7.6.2 Di động IP**

Internet ngày nay không có bất kỳ cơ sở hạ tầng nào được triển khai rộng rãi cung cấp các loại dịch vụ cho người dùng di động \"trên đường\" mà chúng ta gặp đối với các mạng di động 4G/5G. Nhưng điều này chắc chắn không phải do thiếu các giải pháp kỹ thuật để cung cấp các dịch vụ như vậy trong bối cảnh Internet! Thật vậy, kiến trúc và các giao thức Mobile IP \[RFC 5944\] mà chúng ta sẽ thảo luận ngắn gọn bên dưới đã được chuẩn hóa bởi các RFC của Internet trong hơn 20 năm, và nghiên cứu vẫn tiếp tục về các giải pháp di động mới, an toàn hơn và tổng quát hơn \[Venkataramani 2014\].

Thay vào đó, có lẽ nguyên nhân là do thiếu các trường hợp kinh doanh và ứng dụng thúc đẩy \[Arkko 2012\] và sự phát triển cũng như triển khai kịp thời các giải pháp di động thay thế trong các mạng di động đã làm giảm sự triển khai của Mobile IP. Hãy nhớ rằng 20 năm trước, các mạng di động 2G đã cung cấp một giải pháp cho các dịch vụ thoại di động (ứng dụng "sát thủ" cho người dùng di động); ngoài ra, các mạng 3G thế hệ tiếp theo hỗ trợ cả thoại và dữ liệu đã ở trên đường chân trời. Có lẽ giải pháp công nghệ kép---dịch vụ di động thông qua các mạng di động khi chúng ta thực sự di chuyển và "on the go" (tức là phía bên phải cùng của phổ di động trong Hình 7.24) và dịch vụ Internet thông qua các mạng 802.11 hoặc mạng có dây khi chúng ta đứng yên hoặc di chuyển

cục bộ (tức là, phía bên trái nhất của phổ di động trong Hình 7.24)---mà chúng ta đã có 20 năm trước và vẫn còn đến ngày nay sẽ tiếp tục tồn tại trong tương lai. Tuy nhiên, sẽ hữu ích khi tóm tắt nhanh về tiêu chuẩn Mobile IP ở đây, vì nó cung cấp nhiều dịch vụ giống như mạng di động và thực hiện nhiều nguyên tắc cơ bản về di động giống nhau. Các ấn bản trước của cuốn sách giáo khoa này đã cung cấp một nghiên cứu sâu hơn về Mobile IP so với những gì chúng ta sẽ trình bày ở đây; độc giả quan tâm có thể tìm thấy tài liệu đã nghỉ hưu này trên trang web của cuốn sách giáo khoa này. Kiến trúc Internet và các giao thức hỗ trợ di động, tổng hợp được gọi là Mobile IP, chủ yếu được định nghĩa trong RFC 5944 dành cho IPv4. Mobile IP, giống như 4G/5G, là một tiêu chuẩn phức tạp và sẽ cần một cuốn sách riêng để mô tả chi tiết; thực sự một cuốn sách như vậy là \[Perkins 1998b\]. Mục tiêu khiêm tốn của chúng tôi ở đây là cung cấp cái nhìn tổng quan về những khía cạnh quan trọng nhất của Mobile IP.

The overall architecture and elements of Mobile IP are strikingly similar to that of cellular provider networks. There is a strong notion of a home network, in which a mobile device has a permanent IP address, and visited networks (known as "foreign" networks in Mobile IP), where the mobile device will be allocated a care-of-address. The home agent in Mobile IP has a similar function to the LTE HSS: it tracks the location of a mobile device by receiving updates from foreign agents in foreign networks visited by that mobile device, just as the HSS receives updates from Mobility Management Entities (MMEs) in visited networks in which a 4G mobile device resides. And both 4G/5G and Mobile IP use indirect routing to a mobile node, using tunnels to connect the gateway routers in the home and visited/foreign networks. Table 7.3 summarizes the elements of the Mobile IP architecture, along with a comparison with similar elements in 4G/5G networks

Thảo luận về phần tử di động 4G/5G IP

Mạng gia đình Mạng gia đình

Mạng đã truy cập Mạng nước ngoài

Định danh IMSI Địa chỉ vĩnh viễn IP Thông tin địa chỉ định tuyến toàn cầu duy nhất

Dịch vụ thuê bao tại nhà (HSS) đại lý tại nhà

Thực thể quản lý di động (MME) đại lý nước ngoài

Mặt phẳng dữ liệu: chuyển tiếp gián tiếp thông qua mạng gốc, với việc tạo đường hầm giữa mạng gốc và mạng thăm, và tạo đường hầm bên trong mạng mà thiết bị di động đang cư trú

Mặt phẳng dữ liệu: chuyển tiếp gián tiếp qua mạng gốc, với việc tạo đường hầm giữa mạng gốc và mạng thăm

Trạm gốc (eNode-B) Điểm truy cập (AP) Không có công nghệ AP cụ thể nào được chỉ định trong Mobile IP

Mạng truy cập vô tuyến WLAN Không có công nghệ WLAN cụ thể nào được chỉ định trong Mobile IP

Bảng 7.3 ♦ Những điểm chung giữa kiến trúc 4G/5G và Mobile IP

Tiêu chuẩn di động IP bao gồm ba phần chính:

• Khám phá đại lý. Mobile IP định nghĩa các giao thức được sử dụng bởi một đại lý ngoại quốc để quảng bá các dịch vụ di động của nó đến một thiết bị di động muốn kết nối vào mạng của nó. Các dịch vụ đó sẽ bao gồm việc cung cấp một địa chỉ care-of cho thiết bị di động để sử dụng trong mạng ngoại quốc, đăng ký thiết bị di động với đại lý nhà trong mạng nhà của thiết bị di động, và chuyển tiếp các gói dữ liệu đến/từ thiết bị di động, cùng các dịch vụ khác. • Đăng ký với đại lý nhà. Mobile IP định nghĩa các giao thức được sử dụng bởi thiết bị di động và/hoặc đại lý ngoại quốc để đăng ký và hủy đăng ký một địa chỉ care-of với đại lý nhà của thiết bị di động. • Định tuyến gián tiếp các gói dữ liệu. Mobile IP cũng định nghĩa cách thức các gói dữ liệu được chuyển tiếp đến các thiết bị di động bởi đại lý nhà, bao gồm các quy tắc chuyển tiếp gói dữ liệu và xử lý các điều kiện lỗi, và một số hình thức tạo kênh \[RFC 2003, RFC 2004\].

Một lần nữa, phần trình bày của chúng tôi về Mobile IP ở đây đã được tóm tắt một cách cố ý. Người đọc quan tâm nên tham khảo các tài liệu tham khảo trong phần này, hoặc các bài thảo luận chi tiết hơn về Mobile IP trong các ấn bản trước của sách giáo khoa này.

**7.7 Không dây và Di động: Tác động đến các giao thức lớp cao hơn**

In this chapter, we've seen that wireless networks differ significantly from their wired counterparts at both the link layer (as a result of wireless channel characteristics such as fading, multipath, and hidden terminals) and at the network layer (as a result of mobile users who change their points of attachment to the network). But are there important differences at the transport and application layers? It's tempting to think that these differences will be minor, since the network layer provides the same best-effort delivery service model to upper layers in both wired and wireless networks. Similarly, if protocols such as TCP or UDP are used to provide transportlayer services to applications in both wired and wireless networks, then the application layer should remain unchanged as well. In one sense, our intuition is right---TCP and UDP can (and do) operate in networks with wireless links. On the other hand, transport protocols in general, and TCP in particular, can sometimes have very different performance in wired and wireless networks, and it is here, in terms of performance, that differences are manifested. Let's see why.

Hãy nhớ rằng TCP truyền lại một đoạn dữ liệu bị mất hoặc bị hỏng trên đường truyền giữa người gửi và người nhận. Trong trường hợp người dùng di động, mất mát có thể do tắc nghẽn mạng (tràn bộ nhớ đệm của bộ định tuyến) hoặc do chuyển vùng (ví dụ, do độ trễ trong việc định tuyến lại các đoạn dữ liệu tới điểm kết nối mới của thiết bị di động với mạng). Trong tất cả các trường hợp

cases, TCP's receiver-to-sender ACK indicates only that a segment was not received intact; the sender is unaware of whether the segment was lost due to congestion, during handover, or due to detected bit errors. In all cases, the sender's response is the same---to retransmit the segment. TCP's congestion-control response is also the same in all cases---TCP decreases its congestion window, as discussed in Section 3.7. By unconditionally decreasing its congestion window, TCP implicitly assumes that segment loss results from congestion rather than corruption or handover. We saw in Section 7.2 that bit errors are much more common in wireless networks than in wired networks. When such bit errors occur or when handover loss occurs, there's really no reason for the TCP sender to decrease its congestion window (and thus decrease its sending rate). Indeed, it may well be the case that router buffers are empty and packets are flowing along the end-to-end path unimpeded by congestion.

Các nhà nghiên cứu nhận ra vào đầu đến giữa những năm 1990 rằng với tỷ lệ lỗi bit cao trên các liên kết không dây và khả năng mất khi chuyển mạng, phản ứng điều khiển tắc nghẽn của TCP có thể gặp vấn đề trong môi trường không dây. Ba loại phương pháp chính có thể được áp dụng để xử lý vấn đề này:

• Local recovery. Local recovery protocols recover from bit errors when and where (e.g., at the wireless link) they occur, for example, the 802.11 ARQ protocol we studied in Section 7.3, or more sophisticated approaches that use both ARQ and FEC \[Ayanoglu 1995\] that we saw in use in 4G/5G networks in Section 7.4.2. • TCP sender awareness of wireless links. In the local recovery approaches, the TCP sender is blissfully unaware that its segments are traversing a wireless link. An alternative approach is for the TCP sender and receiver to be aware of the existence of a wireless link, to distinguish between congestive losses occurring in the wired network and corruption/loss occurring at the wireless link, and to invoke congestion control only in response to congestive wired-network losses. \[Liu 2003\] investigates techniques for distinguishing between losses on the wired and wireless segments of an end-to-end path. \[Huang 2013\] provides insights on developing transport protocol mechanisms and applications that are more LTEfriendly. • Split-connection approaches. In a split-connection approach \[Bakre 1995\], the end-to-end connection between the mobile user and the other end point is broken into two transport-layer connections: one from the mobile host to the wireless access point, and one from the wireless access point to the other communication end point (which we'll assume here is a wired host). The end-to-end connection is thus formed by the concatenation of a wireless part and a wired part. The transport layer over the wireless segment can be a standard TCP connection \[Bakre 1995\], or a specially tailored error recovery protocol on top of UDP. \[Yavatkar 1994\] investigates the use of a transport-layer selective repeat protocol over the wireless connection. Measurements reported in \[Wei 2006\] indicate that split TCP connections have been widely used in cellular data networks, and that significant improvements can indeed be made through the use of split TCP connections.

Việc chúng tôi đề cập đến TCP qua các liên kết không dây ở đây tất yếu chỉ ngắn gọn. Các khảo sát sâu về các thách thức và giải pháp của TCP trong mạng không dây có thể được tìm thấy trong \[Hanabali 2005; Leung 2006\]. Chúng tôi khuyến khích bạn tham khảo các tài liệu tham khảo để biết chi tiết về lĩnh vực nghiên cứu đang tiếp tục này.

Having considered transport-layer protocols, let us next consider the effect of wireless and mobility on application-layer protocols. Because of the shared nature of the wireless spectrum, applications that operate over wireless links, particularly over cellular wireless links, must treat bandwidth as a scarce commodity. For example, a Web server serving content to a Web browser executing on a 4G smartphone will likely not be able to provide the same image-rich content that it gives to a browser operating over a wired connection. Although wireless links do provide challenges at the application layer, the mobility they enable also makes possible a rich set of location-aware and context-aware applications \[Baldauf 2007\]. More generally, wireless and mobile networks will continue to play a key role in realizing the ubiquitous computing environments of the future \[Weiser 1991\]. It's fair to say that we've only seen the tip of the iceberg when it comes to the impact of wireless and mobile networks on networked applications and their protocols!

**7.8 Tóm tắt**

Mạng không dây và di động lần đầu tiên đã cách mạng hóa viễn thông và hiện nay đang ngày càng có ảnh hưởng sâu sắc trong thế giới mạng máy tính. Với khả năng truy cập mạng toàn cầu bất cứ lúc nào, ở bất cứ đâu và không bị ràng buộc, chúng không chỉ làm cho việc truy cập mạng trở nên phổ biến hơn, mà còn mở ra một loạt các dịch vụ mới phụ thuộc vào vị trí đầy hứng thú. Với tầm quan trọng ngày càng tăng của mạng không dây và di động, chương này tập trung vào các nguyên tắc, công nghệ liên kết phổ biến và kiến trúc mạng để hỗ trợ thông tin liên lạc không dây và di động.

We began this chapter with an introduction to wireless and mobile networks, drawing an important distinction between the challenges posed by the wireless nature of the communication links in such networks, and by the mobility that these wireless links enable. This allowed us to better isolate, identify, and master the key concepts in each area. We focused first on wireless communication, considering the characteristics of a wireless link in Section 7.2. In Sections 7.3 and 7.4, we examined the link-level aspects of the IEEE 802.11 (WiFi) wireless LAN standard, Bluetooth, and 4G/5G cellular neworks. We then turned our attention to the issue of mobility. In Section 7.5, we identified several forms of mobility, with points along this spectrum posing different challenges and admitting different solutions. We considered the problems of locating and routing to a mobile user, as well as approaches for handing over the mobile user who dynamically moves from one point of attachment to the network to another. We examined how these issues were addressed in 4G/5G networks and in the

BÀI TẬP VÀ CÂU HỎI VỀ NHÀ 597

Tiêu chuẩn di động IP. Cuối cùng, chúng tôi đã xem xét ảnh hưởng của các liên kết không dây và tính di động đối với các giao thức tầng vận chuyển và các ứng dụng mạng trong Mục 7.7.

Mặc dù chúng tôi đã dành một chương toàn bộ để nghiên cứu các mạng không dây và di động, nhưng một cuốn sách toàn bộ (hoặc nhiều hơn) sẽ cần thiết để khám phá đầy đủ lĩnh vực hấp dẫn và đang phát triển nhanh chóng này. Chúng tôi khuyến khích bạn tìm hiểu sâu hơn về lĩnh vực này bằng cách tham khảo nhiều tài liệu tham khảo được cung cấp trong chương này.

**Bài Tập và Câu Hỏi**

Câu hỏi ôn tập Chương 7

MỤC 7.1 R1. Điều gì có nghĩa khi một mạng không dây hoạt động trong chế độ "hạ tầng"

"chế độ"? Nếu mạng không ở chế độ hạ tầng, nó đang ở chế độ hoạt động nào, và sự khác biệt giữa chế độ hoạt động đó và chế độ hạ tầng là gì? R2. Có bốn loại mạng không dây được xác định trong phân loại của chúng ta là

Mục 7.1? Bạn đã sử dụng loại mạng không dây nào trong số này?

MỤC 7.2 R3. Sự khác nhau giữa các loại kênh không dây sau là gì

các suy giảm: mất mát đường truyền, lan truyền đa đường, nhiễu từ các nguồn khác? R4. Khi một nút di động càng ngày càng xa khỏi trạm gốc, thì

hai hành động mà một trạm gốc có thể thực hiện để đảm bảo rằng xác suất mất khung dữ liệu được truyền không tăng?

MỤC 7.3 R5. Mô tả vai trò của các khung beacon trong 802.11. R6. Đúng hay sai: Trước khi một trạm 802.11 truyền một khung dữ liệu, nó phải trước tiên

gửi một khung RTS và nhận một khung CTS tương ứng. R7. Tại sao các xác nhận được sử dụng trong 802.11 nhưng không sử dụng trong Ethernet có dây? R8. Đúng hay sai: Ethernet và 802.11 sử dụng cùng một cấu trúc khung. R9. Mô tả cách ngưỡng RTS hoạt động. R10. Giả sử các khung RTS và CTS của IEEE 802.11 dài bằng tiêu chuẩn

Khung DATA và ACK. Liệu có lợi ích gì khi sử dụng các khung CTS và RTS không? Tại sao hoặc tại sao không? R11. Mục 7.3.4 thảo luận về tính di động 802.11, trong đó một trạm không dây di chuyển

từ một BSS sang BSS khác trong cùng một subnet. Khi các AP được kết nối với nhau qua một switch, một AP có thể cần gửi một khung với địa chỉ MAC giả mạo để khiến switch chuyển tiếp khung một cách đúng đắn. Tại sao?

R12. Những khác biệt giữa một thiết bị chủ trong mạng Bluetooth và

một trạm gốc trong mạng 802.11? R13. Vai trò của trạm gốc trong kiến trúc di động 4G/5G là gì? Với

các thành phần mạng 4G/5G khác (thiết bị di động, MME, HSS, Serving Gateway Router, PDN Gateway Router) mà nó trực tiếp giao tiếp trong mặt phẳng điều khiển là gì? Trong mặt phẳng dữ liệu thì sao? R14. IMSI (International Mobile Subscriber Identity) là gì? R15. Vai trò của Home Subscriber Service (HSS) trong mạng di động 4G/5G là gì?

kiến trúc? Với những thành phần mạng 4G/5G nào khác (thiết bị di động, trạm gốc, MME, Cổng phục vụ Router, Cổng PDN Router) mà nó giao tiếp trực tiếp trong mặt phẳng điều khiển? Trong mặt phẳng dữ liệu? R16. Vai trò của Thực thể Quản lý Di động (MME) trong 4G/5G là gì

kiến trúc di động? Nó tương tác trực tiếp với những thành phần mạng 4G/5G nào khác (thiết bị di động, trạm gốc, HSS, Serving Gateway Router, PDN Gateway Router) trong mặt phẳng điều khiển? Còn trong mặt phẳng dữ liệu thì sao? R17. Mô tả mục đích của hai đường hầm trong mặt phẳng dữ liệu của mạng di động 4G/5G

kiến trúc. Khi một thiết bị di động được kết nối với mạng nhà của chính nó, tại phần tử mạng 4G/5G nào (thiết bị di động, trạm gốc, HSS, MME, Serving Gateway Router, PDN Gateway Router) mỗi đầu của mỗi trong hai đường hầm kết thúc? R18. Ba lớp con nào tồn tại trong lớp liên kết trong ngăn xếp giao thức LTE?

Mô tả ngắn gọn chức năng của chúng. R19. Mạng truy cập không dây LTE có sử dụng FDMA, TDMA hay cả hai không? Giải thích

câu trả lời của bạn. R20. Mô tả hai chế độ ngủ có thể có của thiết bị di động 4G/5G. Trong mỗi

các chế độ ngủ này, thiết bị di động có giữ kết nối với cùng một trạm gốc giữa thời điểm nó đi vào chế độ ngủ và thời điểm nó thức dậy và gửi/nhận một gói dữ liệu mới lần đầu tiên không? R21. Ý nghĩa của "mạng đã ghé thăm" và "mạng gốc" trong mạng 4G/5G là gì

Kiến trúc mạng di động? R22. Liệt kê ba điểm khác biệt quan trọng giữa mạng di động 4G và 5G.

MỤC 7.5 R23. Có nghĩa là gì khi nói rằng một thiết bị di động đang "roaming"? R24. "Chuyển giao" của một thiết bị mạng có nghĩa là gì? R25. Sự khác nhau giữa định tuyến trực tiếp và gián tiếp các gói dữ liệu tới/

từ một máy chủ di động đang đi lại? R26. "Định tuyến tam giác" có nghĩa là gì?

BÀI TOÁN 599

MỤC 7.6 R27. Mô tả những điểm tương đồng và khác biệt trong cấu hình đường hầm khi một thiết bị di động

thiết bị đang ở trong mạng gốc của nó, so với khi nó đang chuyển vùng trong một mạng được ghé thăm. R 28. Khi một thiết bị di động được chuyển giao từ một trạm cơ sở sang trạm cơ sở khác trong một

Mạng 4G/5G, yếu tố mạng nào đưa ra quyết định khởi xướng việc chuyển giao đó? Yếu tố mạng nào chọn trạm gốc đích mà thiết bị di động sẽ được chuyển giao? R 29. Mô tả cách thức và thời điểm đường dẫn chuyển tiếp của các gói dữ liệu nhập vào mạng thăm viếng-

làm việc và định sẵn cho thiết bị di động thay đổi trước, trong và sau khi bàn giao. R 30. Xem xét các yếu tố sau của kiến trúc Mobile IP: mạng nhà-

công việc, địa chỉ IP mạng nước ngoài cố định, đại lý nhà, đại lý nước ngoài, chuyển tiếp mặt phẳng dữ liệu, Điểm truy cập (AP) và WLAN ở cạnh mạng. Những yếu tố tương đương gần nhất trong kiến trúc mạng di động 4G/5G là gì?

MỤC 7.7 R31. Ba phương pháp nào có thể được sử dụng để tránh việc chỉ có một kết nối không dây duy nhất

liên kết làm giảm hiệu suất của một kết nối TCP tầng truyền tải đầu-cuối?

**Vấn đề**

P1. Xem xét ví dụ CDMA một người gửi trong Hình 7.5. Điều gì sẽ xảy ra với

đầu ra của người gửi (cho 2 bit dữ liệu được hiển thị) nếu mã CDMA của người gửi là (1, -1, 1, -1, 1, 1, 1, -1)? P2. Xem xét người gửi 2 trong Hình 7.6. Đầu ra của người gửi đối với kênh là gì

(trước khi nó được thêm vào tín hiệu từ người gửi 1), Z2 i,m? P3. Giả sử rằng bộ thu trong Hình 7.6 muốn nhận dữ liệu đang được gửi

bởi người gửi 2. Chứng minh (bằng cách tính toán) rằng người nhận thực sự có thể phục hồi dữ liệu của người gửi 2 từ tín hiệu kênh tổng hợp bằng cách sử dụng mã của người gửi 2. P4. Đối với ví dụ hai người gửi, hai người nhận, đưa ra một ví dụ về hai CDMA

mã chứa các giá trị 1 và 21 mà không cho phép hai bộ thu trích xuất các bit truyền gốc từ hai máy phát CDMA. P5. Giả sử có hai nhà cung cấp dịch vụ Internet cung cấp truy cập WiFi tại một quán cà phê cụ thể, với

mỗi ISP vận hành AP riêng của mình và có khối địa chỉ IP riêng. a. Hơn nữa hãy giả sử rằng do tai nạn, mỗi ISP đã cấu hình AP của mình để hoạt động-

đã ăn qua kênh 11. Liệu giao thức 802.11 có hoàn toàn bị phá vỡ trong tình huống này không? Thảo luận về những gì xảy ra khi hai trạm, mỗi trạm liên kết với một ISP khác nhau, cố gắng truyền cùng một lúc. b. Bây giờ giả sử rằng một AP hoạt động qua kênh 1 và cái kia qua

kênh 11. Câu trả lời của bạn thay đổi như thế nào?

P6. Trong bước 4 của giao thức CSMA/CA, một trạm mà truyền thành công một

Khung bắt đầu giao thức CSMA/CA cho khung thứ hai tại bước 2, thay vì tại bước 1. Lý do gì mà các nhà thiết kế CSMA/CA có thể đã nghĩ đến khi khiến một trạm như vậy không truyền khung thứ hai ngay lập tức (nếu kênh được cảm nhận là nhàn rỗi)? P7. Giả sử một trạm 802.11b được cấu hình để luôn luôn đặt trước kênh với

chuỗi RTS/CTS. Giả sử trạm này đột ngột muốn truyền 1.500 byte dữ liệu, và tất cả các trạm khác đang nhàn rỗi vào thời điểm này. Dưới dạng hàm của SIFS và DIFS, và bỏ qua độ trễ truyền sóng cũng như giả sử không có lỗi bit, tính thời gian cần thiết để truyền khung dữ liệu và nhận xác nhận. P8. Xem xét kịch bản được hiển thị trong Hình 7.31, trong đó có bốn trạm không dây

các nút, A, B, C và D. Phạm vi phủ sóng vô tuyến của bốn nút được hiển thị qua các hình bầu dục có màu; tất cả các nút sử dụng cùng một tần số. Khi A truyền tín hiệu, chỉ có B có thể nghe/nhận được; khi B truyền, cả A và C đều có thể nghe/nhận từ B; khi C truyền, cả B và D đều có thể nghe/nhận từ C; khi D truyền, chỉ có C có thể nghe/nhận từ D. Giả sử bây giờ mỗi nút đều có nguồn tin nhắn vô hạn mà nó muốn

gửi đến từng nút khác. Nếu điểm đến của một tin nhắn không phải là một nút lân cận ngay lập tức, thì tin nhắn đó phải được chuyển tiếp. Ví dụ, nếu A muốn gửi đến D, một tin nhắn từ A trước tiên phải được gửi đến B, sau đó B gửi tin nhắn đến C, và C tiếp tục gửi tin nhắn đến D. Thời gian được chia thành các khe, với thời gian truyền một tin nhắn mất chính xác một khe, ví dụ, như trong slotted Aloha. Trong một khe, một nút có thể thực hiện một trong các hành động sau: (i) gửi một tin nhắn, (ii) nhận một tin nhắn (nếu chính xác một tin nhắn đang được gửi đến nó), (iii) giữ im lặng. Như thường lệ, nếu một nút nghe thấy hai hoặc nhiều lần truyền đồng thời, sẽ xảy ra va chạm và không có tin nhắn nào được truyền đi thành công. Ở đây bạn có thể giả sử rằng không có lỗi cấp bit, và do đó nếu chính xác một tin nhắn được gửi đi, nó sẽ được nhận chính xác bởi những nút nằm trong bán kính truyền của người gửi. a. Giả sử bây giờ có một bộ điều khiển toàn tri (tức là một bộ điều khiển biết

trạng thái của từng nút trong mạng) có thể chỉ huy mỗi nút làm bất cứ điều gì mà nó (bộ điều khiển toàn tri) muốn, tức là, gửi một tin nhắn, nhận một

*Hình 7.31 ♦ Kịch bản cho bài toán P8*

A B C D

BÀI TOÁN 601

tin nhắn, hoặc giữ im lặng. Với bộ điều khiển toàn tri này, tốc độ tối đa mà một tin nhắn dữ liệu có thể được truyền từ C đến A là bao nhiêu, giả sử không có tin nhắn nào khác giữa bất kỳ cặp nguồn/đích nào khác? b. Giả sử bây giờ A gửi tin nhắn đến B, và D gửi tin nhắn đến C.

Tốc độ tối đa kết hợp mà các thông điệp dữ liệu có thể truyền từ A đến B và từ D đến C là bao nhiêu? c. Giả sử bây giờ A gửi thông điệp đến B, và C gửi thông điệp đến D.

Tốc độ tối đa kết hợp mà các thông điệp dữ liệu có thể di chuyển từ A đến B và từ C đến D là bao nhiêu? d. Giả sử bây giờ các liên kết không dây được thay bằng các liên kết có dây. Lặp lại

các câu hỏi (a) đến (c) một lần nữa trong kịch bản có dây này. e. Bây giờ giả sử chúng ta lại ở trong kịch bản không dây, và rằng đối với mỗi

tin nhắn dữ liệu được gửi từ nguồn đến đích, đích sẽ gửi lại một tin nhắn ACK về nguồn (ví dụ, như trong TCP). Cũng giả sử rằng mỗi tin nhắn ACK chiếm một khe. Lặp lại các câu hỏi (a)--(c) ở trên cho kịch bản này. P9. Mô tả định dạng của khung Bluetooth. Bạn sẽ phải đọc một số thông tin-

tìm kiếm bên ngoài văn bản để tìm thông tin này. Có điều gì trong định dạng khung mà vốn dĩ giới hạn số lượng nút hoạt động trong một mạng lên tám nút hoạt động không? Giải thích. P10. Xem xét kịch bản LTE lý tưởng sau. Kênh hạ lưu

(xem Hình 7.22) được phân chia theo khe thời gian, trên F tần số. Có bốn nút, A, B, C và D, có thể kết nối với trạm cơ sở với tốc độ lần lượt là 10 Mbps, 5 Mbps, 2,5 Mbps và 1 Mbps, trên kênh hạ lưu. Những tốc độ này giả định rằng trạm cơ sở sử dụng tất cả các khe thời gian có sẵn trên tất cả F tần số để gửi chỉ đến một trạm duy nhất. Trạm cơ sở có một lượng dữ liệu vô hạn để gửi đến mỗi nút, và có thể gửi đến bất kỳ một trong bốn nút này sử dụng bất kỳ tần số nào trong F tần số trong bất kỳ khe thời gian nào của khung phụ hạ lưu. a. Tốc độ tối đa mà trạm cơ sở có thể gửi đến các nút là bao nhiêu,

giả sử nó có thể gửi đến bất kỳ nút nào mà nó chọn trong mỗi khe thời gian? Giải pháp của bạn có công bằng không? Giải thích và định nghĩa bạn hiểu thế nào là "công bằng." b. Nếu có một yêu cầu công bằng rằng mỗi nút phải nhận một lượng bằng nhau

lượng dữ liệu trong mỗi khoảng thời gian một giây, tốc độ truyền trung bình bởi trạm gốc (đến tất cả các nút) trong khung phụ hạ chiều là bao nhiêu? Giải thích cách bạn đưa ra câu trả lời của mình. c. Giả sử tiêu chí công bằng là bất kỳ nút nào cũng có thể nhận tối đa

gấp đôi lượng dữ liệu so với bất kỳ nút nào khác trong suốt tiểu khung. Tốc độ truyền trung bình bởi trạm gốc (đến tất cả các nút) trong tiểu khung là bao nhiêu? Giải thích cách bạn đưa ra câu trả lời của mình. P11. Trong Mục 7.5, một giải pháp được đề xuất cho phép người dùng di động duy trì

địa chỉ IP của họ khi họ di chuyển giữa các mạng nước ngoài là để một mạng nước ngoài quảng bá một tuyến đường rất cụ thể tới người dùng di động và sử dụng cái sẵn có

cơ sở hạ tầng định tuyến để truyền thông tin này khắp mạng. Chúng tôi xác định khả năng mở rộng là một mối quan tâm. Giả sử khi một người dùng di động di chuyển từ mạng này sang mạng khác, mạng nước ngoài mới quảng bá một tuyến cụ thể tới người dùng di động, và mạng nước ngoài cũ rút tuyến của mình. Hãy xem xét cách thông tin định tuyến được truyền trong thuật toán vec-tơ khoảng cách (đặc biệt trong trường hợp định tuyến liên miền giữa các mạng trải khắp toàn cầu). a. Liệu các bộ định tuyến khác có thể gửi các gói dữ liệu ngay lập tức tới địa chỉ mới

mạng nước ngoài ngay khi mạng nước ngoài bắt đầu quảng bá lộ trình của nó? b. Có khả năng các bộ định tuyến khác nhau tin rằng các mạng nước ngoài khác nhau

chứa người dùng di động? c. Thảo luận về khoảng thời gian mà các bộ định tuyến khác trong mạng sẽ cuối cùng-

hình thành con đường đến người dùng di động. P12. Trong các mạng 4G/5G, việc chuyển giao sẽ có ảnh hưởng gì đến độ trễ đầu-cuối của

các gói dữ liệu giữa nguồn và đích? P13. Xem xét một thiết bị di động bật nguồn và kết nối với một mạng LTE đã truy cập

mạng A, và giả sử rằng việc định tuyến gián tiếp đến thiết bị di động từ mạng gốc H của nó đang được sử dụng. Sau đó, trong khi đi roaming, thiết bị di chuyển ra ngoài phạm vi của mạng thăm A và vào phạm vi của mạng LTE thăm B. Bạn sẽ thiết kế một quá trình chuyển giao từ trạm cơ sở BS.A trong mạng thăm A sang trạm cơ sở BS.B trong mạng thăm B. Phác thảo các bước cần thực hiện, chú ý xác định các thành phần mạng liên quan (và mạng mà chúng thuộc về), để hoàn thành việc chuyển giao này. Giả sử rằng sau khi chuyển giao xong, đường hầm từ mạng gốc đến mạng thăm sẽ kết thúc ở mạng thăm B. P14. Xem xét lại kịch bản trong Bài toán P13. Nhưng bây giờ giả sử rằng đường hầm

Từ mạng nhà H đến mạng thăm A sẽ tiếp tục được sử dụng. Tức là, mạng thăm A sẽ đóng vai trò như một điểm neo sau khi chuyển giao. (Ngoài ra: đây thực ra là quy trình được sử dụng để định tuyến các cuộc gọi thoại chuyển mạch mạch đến điện thoại di động đang trong chế độ roaming trong mạng GSM 2G.) Trong trường hợp này, sẽ cần xây dựng thêm các đường hầm để tiếp cận thiết bị di động trong mạng thăm cư trú B. Một lần nữa, phác thảo các bước cần thực hiện, chú ý xác định các phần tử mạng liên quan (và các mạng mà chúng thuộc về) để thực hiện việc chuyển giao này. Một ưu điểm và một nhược điểm của phương pháp này so với phương pháp được sử dụng trong giải pháp của bạn cho Bài toán P13 là gì?

**Wireshark Phòng thí nghiệm: WiFi**

Trên trang web cho cuốn sách giáo khoa này, www.pearsonhighered.com/cs-resources, cũng được phản chiếu trên trang web của giảng viên, http://gaia.cs.umass.edu/kurose_ross, bạn sẽ tìm thấy một phòng thí nghiệm Wireshark cho chương này nhằm thu và nghiên cứu các khung 802.11 được trao đổi giữa một máy tính xách tay không dây và một điểm truy cập.

Vui lòng mô tả một vài dự án thú vị nhất mà bạn đã làm việc trong suốt sự nghiệp của mình. Những thách thức lớn nhất là gì?

Vào giữa những năm 90 tại USC và ISI, tôi đã có cơ hội tuyệt vời làm việc với những người như Steve Deering, Mark Handley và Van Jacobson về thiết kế các giao thức định tuyến đa hướng (đặc biệt là PIM). Tôi đã cố gắng mang nhiều bài học thiết kế kiến trúc từ đa hướng vào thiết kế các mạng lưới giám sát môi trường sinh thái, nơi lần đầu tiên tôi thực sự bắt đầu coi trọng các ứng dụng và nghiên cứu đa ngành. Nhu cầu đổi mới đồng thời trong không gian xã hội và công nghệ là điều khiến tôi rất quan tâm đến lĩnh vực nghiên cứu gần đây của mình, y tế di động. Những thách thức trong định tuyến đa hướng, cảm biến môi trường và

MỘT CUỘC PHỎNG VẤN VỚI...

**Deborah Estrin**

Được sự cho phép của Deborah Estrin

Deborah Estrin is a Professor of Computer Science and Associate Dean for Impact at Cornell Tech in New York City and a Professor of Public Health at Weill Cornell Medical College. She received her Ph.D. (1985) in Computer Science from M.I.T. and her B.S. (1980) from UC Berkeley. Estrin's early research focused on the design of network protocols, including multicast and inter-domain routing. In 2002 Estrin founded the NSF-funded Science and Technology Center at UCLA, Center for Embedded Networked Sensing (CENS http://cens.ucla.edu.). CENS launched new areas of multi-disciplinary computer systems research from sensor networks for environmental monitoring, to participatory sensing and mobile health. As described in her 2013 TEDMED talk, she explores how individuals can benefit from the pervasive data byproducts of digital and IoT interactions for health and life management. Professor Estrin is an elected member of the American Academy of Arts and Sciences (2007), the National Academy of Engineering (2009), and the National Academy of Medicine (2019). She is a Fellow of the IEEE, ACM, and AAAS. She was selected as the first ACM-W Athena Lecturer (2006), awarded the Anita Borg Institute's Women of Vision Award for Innovation (2007), inducted into the WITI hall of fame (2008), received honorary doctorates from EPFL (2008) and Uppsala University (2011), and was selected as a MacArthur Fellow (2018).

![](media/image3.png){width="5.5in" height="7.071428258967629in"}

Sức khỏe di động đa dạng như các lĩnh vực vấn đề, nhưng điều chúng có chung là cần chú ý xem liệu chúng ta có định nghĩa vấn đề đúng khi chúng ta lặp lại giữa thiết kế và triển khai, nguyên mẫu và thí điểm. Không có vấn đề nào trong số này có thể giải quyết chỉ bằng phân tích, mô phỏng hoặc thậm chí trong các thí nghiệm phòng thí nghiệm được xây dựng. Chúng thách thức khả năng duy trì kiến trúc sạch của chúng ta trong bối cảnh các vấn đề và ngữ cảnh lộn xộn, và chúng đòi hỏi sự hợp tác rộng rãi.

Bạn thấy những thay đổi và đổi mới nào sẽ xảy ra trong mạng không dây và di động trong tương lai?

In a prior edition of this interview I said that I have never put much faith into predicting the future, but I did go on to speculate that we might see the end of feature phones (i.e., those that are not programmable and are used only for voice and text messaging) as smart phones become more and more powerful and the primary point of Internet access for many---and now not so many years later that is clearly the case. I also predicted that we would see the continued proliferation of embedded SIMs by which all sorts of devices have the ability to communicate via the cellular network at low data rates. While that has occurred, we see many devices and "Internet of Things" that use embedded WiFi and other lower power, shorter range, forms of connectivity to local hubs. I did not anticipate at that time the emergence of a large consumer wearables market or interactive voice agents like Siri and Alexa. By the time the next edition is published I expect broad proliferation of personal applications that leverage data from IoT and other digital traces.

Bạn thấy tương lai của mạng và Internet sẽ như thế nào?

Again I think it's useful to look both back and forward. Previously I commented that the efforts in named data and software-defined networking would emerge to create a more manageable, evolvable, and richer infrastructure and more generally represent moving the role of architecture higher up in the stack. In the beginnings of the Internet, architecture was layer 4 and below, with applications being more siloed/monolithic, sitting on top. Now data and analytics dominate transport. The adoption of SDN (which I was really happy to see introduced into the 7th edition of this book) has been well beyond what I ever anticipated. That said, new challenges have emerged from higher up in the stack. Machine Learning based systems and services favor scale, particularly when they rely on continuous consumer engagement (clicks) for financial viability. The resulting information ecosystem has become far more monolithic than in earlier decades. This is a challenge for networking, the Internet, and frankly our society.

Những người nào đã truyền cảm hứng cho bạn về mặt nghề nghiệp?

Có ba người nổi bật trong tâm trí tôi. Đầu tiên là Dave Clark, bí quyết và người hùng thầm lặng của cộng đồng Internet. Tôi thật may mắn khi có mặt vào những ngày đầu để chứng kiến ông một cách như "nguyên tắc tổ chức" của IAB và quản trị Internet; vị linh mục của sự đồng thuận sơ bộ và mã chạy. Thứ hai là Scott Shenker, vì sự xuất sắc trí tuệ, chính trực và kiên trì của ông. Tôi luôn cố gắng đạt được, nhưng hiếm khi có được, sự rõ ràng của ông trong việc xác định các vấn đề và giải pháp. Ông luôn là người đầu tiên tôi gửi email để xin lời khuyên về mọi vấn đề lớn nhỏ. Thứ ba là chị tôi, Judy Estrin, người đã có sự sáng tạo và cam kết dành nửa đầu sự nghiệp của mình để đưa các ý tưởng và khái niệm ra thị trường; và bây giờ có đủ dũng khí để nghiên cứu, viết và tư vấn về cách xây dựng lại nó để hỗ trợ một nền dân chủ lành mạnh hơn.

Bạn có những khuyến nghị gì cho sinh viên muốn làm việc trong ngành khoa học máy tính và mạng máy tính?

Trước tiên, xây dựng một nền tảng vững chắc trong công việc học tập của bạn, kết hợp với bất kỳ và mọi kinh nghiệm làm việc thực tế mà bạn có thể có. Khi bạn tìm kiếm một môi trường làm việc, hãy tìm kiếm cơ hội trong những lĩnh vực vấn đề mà bạn thực sự quan tâm và với những đội nhóm thông minh mà bạn có thể học hỏi và làm việc cùng để xây dựng những điều quan trọng.

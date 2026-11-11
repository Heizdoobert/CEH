Mô-đun 02: Dấu chân và Trinh sát

Kịch bản

Trinh sát đề cập đến việc thu thập thông tin về mục tiêu, đây là bước đầu tiên trong bất kỳ cuộc tấn công nào vào hệ thống. Nó có nguồn gốc từ các hoạt động quân sự, trong đó thuật ngữ này đề cập đến nhiệm vụ thu thập thông tin về kẻ thù. Trinh sát giúp kẻ tấn công thu hẹp phạm vi nỗ lực của chúng và hỗ trợ trong việc lựa chọn vũ khí tấn công. Những kẻ tấn công sử dụng thông tin thu thập được để tạo ra một kế hoạch chi tiết hoặc \"dấu chân\" của tổ chức, giúp chúng chọn chiến lược hiệu quả nhất để xâm phạm an ninh hệ thống và mạng.

Tương tự, việc đánh giá bảo mật của một hệ thống hoặc mạng bắt đầu bằng việc trinh sát và theo dõi mục tiêu. Tin tặc có đạo đức và người kiểm tra thâm nhập (bút) phải thu thập đủ thông tin về mục tiêu đánh giá trước khi bắt đầu đánh giá. Tin tặc có đạo đức và chuyên gia kiểm thử xâm nhập (pentester) nên mô phỏng tất cả các bước mà kẻ tấn công thường tuân theo để có được ý tưởng hợp lý về tình hình bảo mật của tổ chức mục tiêu. Trong trường hợp này, bạn làm việc như một hacker có đạo đức trong một tổ chức lớn. Tổ chức của bạn cảnh giác trước những tin tức liên quan đến các phương thức tấn công mới đang gây khó khăn cho các tổ chức lớn trên khắp thế giới. Hơn nữa, tổ chức của bạn trước đây từng là mục tiêu của một vụ vi phạm an ninh lớn khi dữ liệu cá nhân của một số khách hàng của tổ chức này bị lộ trên các trang mạng xã hội.

Bạn đã được các nhà quản lý cấp cao yêu cầu thực hiện đánh giá an ninh chủ động của công ty. Trước khi bắt đầu bất kỳ đánh giá nào, bạn nên thảo luận và xác định phạm vi với ban quản lý; phạm vi đánh giá xác định các hệ thống, mạng, chính sách và thủ tục, nguồn nhân lực và bất kỳ thành phần nào khác của hệ thống yêu cầu đánh giá bảo mật. Bạn cũng nên đồng ý với ban quản lý về các quy tắc cam kết (RoE) - những điều nên làm và không nên làm khi đánh giá. Sau khi có được sự chấp thuận cần thiết để thực hiện hack có đạo đức, bạn nên bắt đầu thu thập thông tin về tổ chức mục tiêu. Khi bạn bắt đầu quá trình theo dõi một cách có phương pháp, bạn sẽ có được bản thiết kế chi tiết về hồ sơ bảo mật của tổ chức mục tiêu. Thuật ngữ \"bản thiết kế\" đề cập đến hồ sơ hệ thống duy nhất của tổ chức mục tiêu là kết quả của dấu chân.

Các bài lab trong mô-đun này sẽ cung cấp cho bạn trải nghiệm thời gian thực trong việc thu thập nhiều thông tin khác nhau về tổ chức mục tiêu từ nhiều nguồn mở hoặc có thể truy cập công khai khác nhau.

Mục tiêu

Mục tiêu của bài lab là trích xuất thông tin về tổ chức mục tiêu bao gồm nhưng không giới hạn ở:

-   **Thông tin về tổ chức Chi tiết về nhân viên, địa chỉ và chi tiết liên hệ, chi tiết về đối tác, liên kết web, công nghệ web, bằng sáng chế, nhãn hiệu, v.v.**

-   **Thông tin mạng Miền, miền phụ, khối mạng, cấu trúc liên kết mạng, bộ định tuyến đáng tin cậy, tường lửa, địa chỉ IP của hệ thống có thể truy cập, bản ghi Whois, bản ghi DNS và thông tin liên quan khác**

-   **Thông tin hệ thống Hệ điều hành, hệ điều hành máy chủ web, vị trí của máy chủ web, tài khoản người dùng và mật khẩu, v.v.**

Tổng quan về Dấu chân

Dấu chân đề cập đến quá trình thu thập thông tin về mạng mục tiêu và môi trường của nó, giúp đánh giá tình trạng bảo mật của cơ sở hạ tầng CNTT của tổ chức mục tiêu. Nó cũng giúp xác định mức độ rủi ro liên quan đến thông tin có thể truy cập công khai của tổ chức.

Dấu chân có thể được phân loại thành dấu chân thụ động và dấu chân chủ động:

-   **Dấu chân thụ động: Liên quan đến việc thu thập thông tin mà không có sự tương tác trực tiếp. Kiểu dấu chân này chủ yếu hữu ích khi có yêu cầu rằng các hoạt động thu thập thông tin không bị mục tiêu phát hiện.**

-   **Dấu chân tích cực: Liên quan đến việc thu thập thông tin với sự tương tác trực tiếp. Trong quá trình theo dõi hoạt động, mục tiêu có thể nhận ra quá trình thu thập thông tin đang diễn ra khi chúng ta tương tác công khai với mạng mục tiêu.**

**Nhiệm vụ bài lab**

Tin tặc đạo đức hoặc chuyên gia kiểm thử xâm nhập (pentester) sử dụng nhiều công cụ và kỹ thuật để thu thập thông tin về mục tiêu. Các bài lab được đề xuất sẽ hỗ trợ bạn học các kỹ thuật in dấu chân khác nhau bao gồm:

1.  Thực hiện dấu chân thông qua công cụ tìm kiếm

    -   Thu thập thông tin bằng các kỹ thuật hack nâng cao của Google

2.  Thực hiện dấu chân thông qua Dịch vụ nghiên cứu Internet

    -   Tìm tên miền, tên miền phụ và Máy chủ lưu trữ của công ty bằng Netcraft và DNSdumpster

3.  Thực hiện dấu chân thông qua các trang mạng xã hội

    -   Thu thập thông tin cá nhân từ nhiều trang mạng xã hội khác nhau bằng Sherlock

4.  Thực hiện dấu chân Whois

    -   Thực hiện tra cứu Whois bằng DomainTools

5.  Thực hiện dấu chân DNS

    -   Thu thập thông tin DNS bằng tiện ích dòng lệnh nslookup và công cụ trực tuyến

6.  Thực hiện dấu chân mạng

    -   Thực hiện theo dõi mạng trong Máy Windows và Linux

7.  Thực hiện dấu chân email

    -   Thu thập thông tin về mục tiêu bằng cách truy tìm email bằng eMailTrackerPro

8.  Thực hiện dấu chân bằng nhiều công cụ dấu chân khác nhau

    -   Dấu chân mục tiêu bằng Recon-ng

9.  Thực hiện Dấu chân bằng AI

    -   Dấu chân mục tiêu bằng Shellgpt

**Giải pháp:**

Nhiệm vụ 1: Thu thập thông tin bằng Kỹ thuật hack nâng cao của Google

Hack nâng cao của Google đề cập đến nghệ thuật tạo các truy vấn công cụ tìm kiếm phức tạp bằng cách sử dụng các toán tử nâng cao của Google để trích xuất thông tin nhạy cảm hoặc ẩn về một công ty mục tiêu từ kết quả tìm kiếm của Google. Điều này có thể cung cấp thông tin về các trang web dễ bị khai thác.

Ở đây, chúng tôi sẽ coi EC-Council là một tổ chức mục tiêu. Tuy nhiên, bạn có thể chọn một tổ chức mục tiêu theo lựa chọn của bạn.

1.  Theo mặc định, máy Windows 11 được chọn, hãy nhấp vào Ctrl+Alt+Delete và đăng nhập bằng Admin/Pa\$\$w0rd.

> Ngoài ra, bạn cũng có thể nhấp vào nút Ctrl+Alt+Delete trong hình thu nhỏ của máy Windows 11 trong ngăn Tài nguyên.
>
> Ngoài ra, bạn cũng có thể nhấp vào Pa\$\$w0rd trong hình thu nhỏ của máy Windows 11 trong ngăn Tài nguyên.
>
> Màn hình Mạng xuất hiện, hãy nhấp vào Có để cho phép các PC và thiết bị khác trên mạng có thể phát hiện ra PC của bạn.

2.  Khởi chạy bất kỳ trình duyệt web nào và truy cập https://www.google.com (ở đây, chúng tôi đang sử dụng Mozilla Firefox).

> Nếu cửa sổ Trình cập nhật phần mềm Firefox xuất hiện, hãy nhấp vào Không.

-   Nếu cửa sổ bật lên Trình duyệt mặc định xuất hiện, hãy bỏ chọn hộp kiểm Luôn thực hiện kiểm tra này khi khởi động Firefox và nhấp vào nút Không phải bây giờ .

-   Nếu thông báo xuất hiện, hãy nhấp vào Được rồi, hiểu rồi để xem xong thông tin.

3.  Trong thanh tìm kiếm, hãy tìm kiếm intitle:login site:eccouncil.org. Lệnh tìm kiếm này sử dụng các toán tử nâng cao intitle và trang web của Google để hạn chế kết quả ở các trang trên trang web eccouncil.org có chứa các trang đăng nhập. Một ví dụ được hiển thị trong ảnh chụp màn hình bên dưới.

> Tại đây, toán tử Tìm kiếm nâng cao của Google này có thể giúp những kẻ tấn công và chuyên gia kiểm thử xâm nhập (pentester) trích xuất các trang đăng nhập của trang web của tổ chức mục tiêu. Những kẻ tấn công có thể khiến các trang đăng nhập phải hứng chịu nhiều cuộc tấn công khác nhau, chẳng hạn như tấn công cưỡng bức thông tin xác thực, tấn công tiêm nhiễm và các cuộc tấn công ứng dụng web khác. Tương tự, việc đánh giá các trang đăng nhập chống lại các cuộc tấn công khác nhau là rất quan trọng để thử nghiệm thâm nhập.
>
> ![Screenshot](media/image2.jpeg){width="6.752567804024497in" height="5.066404199475065in"}

4.  Tương tự, hãy nhập lệnh EC-Council filetype:pdf ceh vào thanh tìm kiếm để tìm kiếm kết quả dựa trên phần mở rộng tệp và từ khóa (ở đây, ceh). Nhấp vào bất kỳ liên kết nào từ kết quả (tại đây, CEH-brochure.pdf) để xem tệp pdf.

> Ở đây, loại tệp pdf được tìm kiếm cho tổ chức EC-Council mục tiêu. Kết quả có thể khác khi bạn thực hiện tác vụ này.
>
> Tệp PDF và các tài liệu khác từ trang web mục tiêu có thể cung cấp thông tin nhạy cảm về sản phẩm và dịch vụ của mục tiêu. Chúng có thể giúp kẻ tấn công xác định vectơ tấn công để khai thác mục tiêu.
>
> ![Screenshot](media/image3.jpeg){width="5.81633530183727in" height="4.363955599300088in"}

5.  Trang xuất hiện hiển thị tệp PDF, như trong ảnh chụp màn hình.

> ![Screenshot](media/image4.jpeg){width="6.477517497812773in" height="4.860037182852143in"}

6.  Ngoài các toán tử nâng cao của Google đã nói ở trên, bạn cũng có thể sử dụng các toán tử sau để thực hiện tìm kiếm nâng cao nhằm thu thập thêm thông tin về tổ chức mục tiêu từ các nguồn có sẵn công khai.

    -   **cache: Toán tử này cho phép bạn xem phiên bản được lưu trong bộ nhớ cache của trang web. \[cache:www.eccouncil.org\]- Truy vấn trả về phiên bản được lưu trong bộ nhớ đệm của trang web www.eccouncil.org**

    -   **allinurl: Toán tử này hạn chế kết quả ở các trang chứa tất cả các thuật ngữ truy vấn được chỉ định trong URL. \[allinurl: EC-Council professional\]-Truy vấn chỉ trả về các trang chứa từ \"EC-Council\" và \"career\" trong URL**

    -   **inurl: Toán tử này giới hạn kết quả ở các trang chứa từ được chỉ định trong URL \[inurl: copy site:www.eccouncil.org\]-Truy vấn chỉ trả về các trang trong trang EC-Council trong đó URL có từ \"copy\"**

    -   **allintitle: Toán tử này giới hạn kết quả ở các trang chứa tất cả các thuật ngữ truy vấn được chỉ định trong tiêu đề. \[allintitle: detect Malware\]-Truy vấn chỉ trả về các trang chứa từ \"phát hiện\" và \"phần mềm độc hại\" trong tiêu đề**

    -   **inanchor: Toán tử này giới hạn kết quả ở các trang chứa cụm từ truy vấn được chỉ định trong văn bản liên kết trên các liên kết đến trang. \[Inanchor chống vi-rút:Norton\]-Truy vấn chỉ trả về các trang có văn bản liên kết trên các liên kết đến các trang chứa từ \"Norton\" và trang chứa từ \"Chống vi-rút\"**

    -   **allinanchor: Toán tử này hạn chế kết quả ở các trang chứa tất cả các thuật ngữ truy vấn được chỉ định trong văn bản liên kết trên các liên kết đến trang. \[allinanchor: nhà cung cấp dịch vụ đám mây tốt nhất\]-Truy vấn chỉ trả về các trang trong đó văn bản liên kết trên các liên kết đến các trang chứa các từ \"tốt nhất\", \"đám mây\", \"dịch vụ\" và \"nhà cung cấp\"**

    -   **link: Toán tử này tìm kiếm các trang web hoặc trang có chứa liên kết đến trang web hoặc trang được chỉ định. \[link:www.eccouncil.org\]-Tìm các trang trỏ đến trang chủ của EC-Council**

    -   **liên quan: Toán tử này hiển thị các trang web tương tự hoặc liên quan đến URL được chỉ định. \[liên quan:www.eccouncil.org\]-Query cung cấp cho trang kết quả của công cụ tìm kiếm Google các trang web tương tự như eccouncil.org**

    -   **info: Toán tử này tìm thông tin cho trang web được chỉ định. \[info:eccouncil.org\]-Query cung cấp thông tin về trang chủ www.eccouncil.org**

    -   **vị trí: Toán tử này tìm thông tin cho một vị trí cụ thể. \[location: EC-Council\]-Truy vấn cho bạn kết quả dựa trên thuật ngữ EC-Council**

7.  Điều này kết thúc phần trình diễn thu thập thông tin bằng cách sử dụng các kỹ thuật hack tiên tiến của Google. Bạn có thể tự mình thực hiện một loạt truy vấn bằng cách sử dụng các toán tử nâng cao này của Google và thu thập thông tin liên quan về tổ chức mục tiêu.

8.  Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

Lab 2: Thực hiện Dấu chân thông qua Dịch vụ Nghiên cứu Internet

**Kịch bản bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc chuyên gia kiểm thử xâm nhập (pentester), bạn sẽ có thể trích xuất nhiều thông tin khác nhau về tổ chức mục tiêu của mình từ các dịch vụ nghiên cứu trên Internet. Bằng cách đó, bạn có thể trích xuất thông tin quan trọng như tên miền, tên miền phụ, hệ điều hành, vị trí địa lý, chi tiết nhân viên, email, thông tin tài chính, chi tiết cơ sở hạ tầng, trang web và nội dung ẩn của tổ chức mục tiêu, v.v.

Sử dụng thông tin này, bạn có thể xây dựng chiến lược hack để đột nhập vào mạng của tổ chức mục tiêu và có thể thực hiện các kiểu tấn công hệ thống nâng cao khác.

**Mục tiêu bài lab**

-   Tìm tên miền và tên miền phụ của công ty bằng Netcraft và DNSdumpster

**Tổng quan về Dịch vụ Nghiên cứu Internet**

Các dịch vụ nghiên cứu trên Internet như dịch vụ tìm kiếm người, dịch vụ cảnh báo, dịch vụ tài chính và trang web việc làm, cung cấp thông tin về tổ chức mục tiêu; ví dụ: chi tiết cơ sở hạ tầng, vị trí thực tế, chi tiết nhân viên, v.v. Ngoài ra, các nhóm, diễn đàn và blog có thể cung cấp thông tin nhạy cảm về tổ chức mục tiêu như thông tin mạng công cộng, thông tin hệ thống và thông tin cá nhân. Các kho lưu trữ trên Internet có thể cung cấp thông tin nhạy cảm đã bị xóa khỏi World Wide Web (WWW).

Nhiệm vụ 1: Tìm Tên miền, Tên miền phụ và Máy chủ của Công ty bằng Netcraft và DNSdumpster

Tên miền và tên miền phụ là một phần của cơ sở hạ tầng mạng quan trọng đối với bất kỳ tổ chức nào. Tên miền cấp cao nhất (TLD) và tên miền phụ của công ty có thể cung cấp nhiều thông tin hữu ích như lịch sử tổ chức, dịch vụ và sản phẩm cũng như thông tin liên hệ. Trang web công cộng được thiết kế để thể hiện sự hiện diện của một tổ chức trên Internet và có sẵn để truy cập miễn phí.

Tại đây, chúng tôi sẽ trích xuất tên miền và tên miền phụ của công ty bằng công cụ Netcraft và DNSdumpster.

1.  Khởi chạy bất kỳ trình duyệt web nào và truy cập https://www.netcraft.com (ở đây, chúng tôi đang sử dụng Mozilla Firefox).

2.  Trang Netcraft xuất hiện như trong ảnh chụp màn hình.

> Nếu cửa sổ bật lên của cookie xuất hiện, hãy nhấp vào Chấp nhận.

3.  Nhấp vào biểu tượng menu từ góc trên bên phải của trang và điều hướng đến Tài nguyên -\> Công cụ nghiên cứu.

4.  Trong Công cụ \| trang Netcraft, hãy nhấp vào tùy chọn Báo cáo trang web.

> Nếu cửa sổ bật lên cookie xuất hiện, hãy nhấp vào CHẤP NHẬN COOKIE.

5.  Trang web đó đang chạy cái gì? trang xuất hiện. Để trích xuất thông tin liên quan đến trang web của tổ chức như cơ sở hạ tầng, công nghệ được sử dụng, tên miền phụ, nền tảng, mạng, v.v., hãy nhập URL của trang web mục tiêu (tại đây, https://www.certifiedhacker.com) vào trường văn bản, sau đó nhấp vào nút TÌM KIẾM như minh họa trong ảnh chụp màn hình.

6.  Báo cáo trang web cho trang https://www.certifiedhacker.com xuất hiện, chứa thông tin liên quan đến Nền, Mạng, Lịch sử lưu trữ, v.v., như minh họa trong ảnh chụp màn hình.

7.  Trong phần Mạng, hãy nhấp vào liên kết trang web (tại đây, certifiedhacker.com) trong trường Miền để xem các miền phụ.

8.  Kết quả sẽ hiển thị các tên miền phụ của trang web mục tiêu cùng với thông tin về netblock và hệ điều hành, như trong ảnh chụp màn hình.

9.  Bây giờ, chúng tôi sẽ tìm thấy Máy chủ DNS của công ty cùng với Geo IP và ánh xạ tên miền bằng trang web DNSdumpster.

10. Mở một tab mới trong trình duyệt Firefox và truy cập https://dnsdumpster.com/. Tìm kiếm certifiedhacker.com trong hộp tìm kiếm.

11. Trang web hiển thị GEOIP của Vị trí lưu trữ, như minh họa trong ảnh chụp màn hình.

12. Cuộn xuống để xem danh sách Máy chủ DNS, Bản ghi MX, Bản ghi máy chủ (A) cùng với địa chỉ IP của chúng.

13. Hơn nữa, cuộn xuống để xem bản đồ tên miền của trang web.

> Bấm vào bản đồ để xem hình ảnh kích thước đầy đủ.
>
> Nhấp lại để thoát khỏi hình ảnh kích thước đầy đủ.

14. Nhấp vào nút Tải xuống .xlsx của Máy chủ để tải xuống danh sách máy chủ.

15. Điều hướng đến thư mục Tải xuống và nhấp đúp vào tệp certifiedhacker.com-xxxxxxx.xlsx để xem danh sách Máy chủ.

> Trong cửa sổ Trình hướng dẫn kích hoạt Microsoft Office , hãy nhấp vào Đóng.
>
> Ở đầu trang tính Excel, hãy nhấp vào Bật chỉnh sửa.

16. Bảng Excel hiển thị các chi tiết như Tên máy chủ, Địa chỉ IP, DNS ngược, Chủ sở hữu Netblock, Quốc gia, HTTP /Title, v.v.

17. Phần này kết thúc phần minh họa tìm kiếm tên miền, tên miền phụ và Máy chủ lưu trữ của công ty bằng công cụ Netcraft và DNSdumpster. Những kẻ tấn công có thể sử dụng danh sách tên miền phụ được thu thập này để thực hiện các cuộc tấn công ứng dụng web vào tổ chức mục tiêu, chẳng hạn như tấn công tiêm nhiễm, tấn công vũ phu và tấn công từ chối dịch vụ (DoS).

18. Bạn cũng có thể sử dụng các công cụ như Pentest-Tools Tìm tên miền phụ (https://pentest-tools.com), để xác định tên miền và tên miền phụ của bất kỳ trang web mục tiêu nào.

19. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 2.2.1.1**

Sử dụng trang web DNSdumpster (https://dnsdumpster.com/) để lấy Máy chủ DNS của miền Certifiedhacker.com cùng với Geo IP và ánh xạ miền. Nhập Địa chỉ IP của Máy chủ DNS ns2.bluehost.com của miền mục tiêu.

![](media/image5.wmf)

**Câu 2.2.1.2**

Tìm kiếm www.eccouncil.org trên Netcraft (https://www.netcraft.com) và xác định hệ điều hành của máy chủ web lưu trữ trang web www.eccouncil.org.

Lab 3: Thực hiện Dấu chân thông qua các trang mạng xã hội

**Kịch bản bài lab**

Là một hacker đạo đức chuyên nghiệp, trong quá trình thu thập thông tin, bạn cần thu thập thông tin cá nhân về những nhân viên làm việc ở những vị trí quan trọng trong tổ chức mục tiêu; ví dụ: Giám đốc An ninh Thông tin, Kiến trúc sư Bảo mật hoặc Quản trị viên Mạng. Bằng cách theo dõi các trang mạng xã hội, bạn có thể trích xuất thông tin cá nhân như tên, chức vụ, tên tổ chức, địa điểm hiện tại và trình độ học vấn. Hơn nữa, bạn có thể tìm thấy thông tin chuyên nghiệp như công ty hoặc doanh nghiệp, vị trí hiện tại, số điện thoại, ID email, ảnh, video, v.v. Thông tin được thu thập có thể hữu ích để thực hiện kỹ thuật xã hội và các loại tấn công nâng cao khác.

**Mục tiêu bài lab**

-   Thu thập thông tin cá nhân từ nhiều trang mạng xã hội khác nhau bằng Sherlock

**Tổng quan về các trang mạng xã hội**

Các trang mạng xã hội là các dịch vụ, nền tảng trực tuyến hoặc các trang web khác cho phép mọi người kết nối và xây dựng mối quan hệ giữa các cá nhân. Mọi người thường duy trì hồ sơ trên các trang mạng xã hội để cung cấp thông tin cơ bản về bản thân và giúp tạo và duy trì kết nối với người khác; hồ sơ thường chứa các thông tin như tên, thông tin liên lạc (số điện thoại di động, địa chỉ email), thông tin bạn bè, thông tin về các thành viên trong gia đình, sở thích, hoạt động của họ, v.v. Trên các trang mạng xã hội, mọi người cũng có thể đăng thông tin cá nhân của mình như ngày sinh, thông tin học vấn, lý lịch việc làm, tên vợ/chồng, v.v. Các tổ chức thường đăng tải những thông tin như đối tác tiềm năng, trang web và tin tức sắp tới về công ty. Vì vậy, các trang mạng xã hội thường tỏ ra là nguồn thông tin có giá trị. Ví dụ về các trang web như vậy bao gồm LinkedIn, Facebook, Instagram, Twitter, Pinterest, YouTube, v.v.

Nhiệm vụ 1: Thu thập thông tin cá nhân từ các trang mạng xã hội khác nhau bằng Sherlock

Sherlock là một công cụ dựa trên python được sử dụng để thu thập thông tin về một người mục tiêu trên nhiều trang mạng xã hội khác nhau. Sherlock tìm kiếm một số lượng lớn các trang mạng xã hội cho một người dùng mục tiêu nhất định, định vị người đó và hiển thị kết quả cùng với URL hoàn chỉnh liên quan đến người mục tiêu.

Ở đây, chúng tôi sẽ sử dụng Sherlock để thu thập thông tin cá nhân về mục tiêu từ các trang mạng xã hội.

Tại đây, chúng tôi đang thu thập thông tin về Elon Musk. Tuy nhiên, bạn có thể chọn mục tiêu theo ý muốn.

1.  Bật máy ảo Parrot Security

2.  Nhấp vào Bảo mật Parrot để chuyển sang máy Parrot và đăng nhập bằng kẻ tấn công/toor. Mở cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).[Parrot Security](https://labclient.labondemand.com/Instructions/e6a97cad-3982-464f-a2d8-79d028c77385)

> Mật khẩu bạn gõ sẽ không hiển thị.

3.  Chạy lệnh sherlock \"Elon Musk\" và bạn sẽ nhận được tất cả các URL liên quan đến Elon Musk, như minh họa trong ảnh chụp màn hình. Cuộn xuống để xem tất cả các kết quả.

> Kết quả có thể khác khi bạn thực hiện tác vụ này. Nếu bạn nhận được bất kỳ thông báo lỗi nào ở giữa, hãy bỏ qua chúng.
>
> ![Screenshot](media/image6.jpeg){width="6.353413167104112in" height="4.766922572178478in"}

4.  Những kẻ tấn công có thể sử dụng thêm các URL đã thu thập để lấy thông tin nhạy cảm về mục tiêu như DOB, tình trạng việc làm và thông tin về tổ chức mà chúng đang làm việc, bao gồm chiến lược kinh doanh, khách hàng tiềm năng và kế hoạch dự án sắp tới.

5.  Điều này kết thúc việc trình diễn thu thập thông tin cá nhân từ các trang mạng xã hội khác nhau bằng Sherlock.

6.  Bạn cũng có thể sử dụng các công cụ như Công cụ tìm kiếm trên mạng xã hội (https://www.social-searcher.com) để thu thập thông tin bổ sung liên quan đến công ty mục tiêu và nhân viên của công ty đó từ các trang mạng xã hội.

7.  Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 2.3.1.1**

Sử dụng công cụ Sherlock để thu thập tất cả các URL liên quan đến Elon Musk từ nhiều trang mạng xã hội khác nhau. Nhập URL đầy đủ liên quan đến Elon Musk được lấy từ trang mạng xã hội Codewars.

![](media/image7.wmf)

Lab 4: Thực hiện Dấu chân Whois

**Kịch bản bài lab**

Trong quá trình theo dấu chân, việc thu thập thông tin về địa chỉ IP và miền mục tiêu thu được trong các bước thu thập thông tin trước đó là rất quan trọng. Với tư cách là một hacker có đạo đức chuyên nghiệp hoặc người kiểm tra thâm nhập, bạn sẽ có thể thực hiện dấu vết Whois trên mục tiêu; phương pháp này cung cấp thông tin tên miền mục tiêu như chủ sở hữu, nhà đăng ký, chi tiết đăng ký, máy chủ định danh, thông tin liên hệ, v.v. Bằng cách sử dụng thông tin này, bạn có thể tạo bản đồ mạng của tổ chức, thực hiện các cuộc tấn công kỹ thuật xã hội và lấy thông tin chi tiết nội bộ của mạng.

**Mục tiêu bài lab**

-   Thực hiện tra cứu Whois bằng DomainTools

**Tổng quan về Dấu chân Whois**

bài lab này tập trung vào cách thực hiện tra cứu Whois và phân tích kết quả. Whois là giao thức truy vấn và phản hồi được sử dụng để truy vấn cơ sở dữ liệu lưu trữ người dùng đã đăng ký hoặc người được chuyển nhượng tài nguyên Internet như tên miền, khối địa chỉ IP hoặc hệ thống tự trị. Giao thức này lắng nghe các yêu cầu trên cổng 43 (TCP). Cơ quan đăng ký Internet khu vực (RIR) duy trì cơ sở dữ liệu Whois và chứa thông tin cá nhân của chủ sở hữu tên miền. Đối với mỗi tài nguyên, cơ sở dữ liệu Whois cung cấp các bản ghi văn bản chứa thông tin về chính tài nguyên đó và thông tin liên quan của người được chuyển nhượng, người đăng ký và thông tin quản trị (ngày tạo và ngày hết hạn).

Nhiệm vụ 1: Thực hiện Tra cứu Whois bằng DomainTools

Tại đây, chúng tôi sẽ thu thập thông tin mục tiêu bằng cách thực hiện tra cứu Whois bằng DomainTools.

1.  Nhấp vào Windows 11 để chuyển sang máy Windows 11 , mở bất kỳ trình duyệt web nào và truy cập https://whois.domaintools.com (ở đây, chúng tôi đang sử dụng Mozilla Firefox).[Windows 11](https://labclient.labondemand.com/Instructions/e6a97cad-3982-464f-a2d8-79d028c77385)

2.  Trang web Tra cứu Whois xuất hiện như trong ảnh chụp màn hình. Bây giờ, trong thanh tìm kiếm, hãy tìm kiếm www.certifiedhacker.com.

> ![Screenshot](media/image8.jpeg){width="6.601517935258093in" height="4.953073053368329in"}

3.  Kết quả tìm kiếm này hiển thị các chi tiết liên quan đến URL đã nhập, www.certifiedhacker.com, bao gồm các chi tiết về tổ chức như chi tiết đăng ký, máy chủ tên, địa chỉ IP, vị trí, v.v., như được hiển thị trong ảnh chụp màn hình.

> ![Screenshot](media/image9.jpeg){width="6.451140638670166in" height="4.840246062992126in"}
>
> ![Screenshot](media/image10.jpeg){width="6.648017279090114in" height="4.987961504811898in"}

4.  Phần này kết thúc phần trình diễn thu thập thông tin về tổ chức mục tiêu bằng cách thực hiện tra cứu Whois bằng DomainTools.

5.  Bằng cách sử dụng thông tin này, kẻ tấn công có thể tạo bản đồ mạng của tổ chức và tiếp tục đánh lừa chủ sở hữu tên miền bằng kỹ thuật xã hội cũng như lấy được thông tin chi tiết nội bộ của mạng.

6.  Bạn cũng có thể sử dụng các công cụ tra cứu Whois khác như SmartWhois (https://www.tamos.com), Batch IP Converter (http://www.sabsoft.com), v.v. để trích xuất thêm thông tin Whois mục tiêu.

7.  Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 2.4.1.1**

Thực hiện tra cứu Whois bằng DomainTools và tìm URL thuộc về nhà đăng ký của trang web www.certifiedhacker.com.

Lab 5: Thực hiện Dấu chân DNS

**Kịch bản bài lab**

Là một hacker có đạo đức chuyên nghiệp, bạn cần thu thập thông tin DNS của miền mục tiêu có được trong các bước trước đó. Bạn cần thực hiện theo dõi dấu vết DNS để thu thập thông tin về máy chủ DNS, bản ghi DNS và loại máy chủ được tổ chức mục tiêu sử dụng. Dữ liệu vùng DNS bao gồm tên miền DNS, tên máy tính, địa chỉ IP, máy chủ thư miền, bản ghi dịch vụ và nhiều thông tin khác về mạng mục tiêu.

Bằng cách sử dụng thông tin này, bạn có thể xác định các máy chủ chính được kết nối trong mạng và thực hiện các cuộc tấn công lừa đảo qua mạng để thu thập nhiều thông tin hơn nữa.

**Mục tiêu bài lab**

-   Thu thập thông tin DNS bằng tiện ích dòng lệnh nslookup và công cụ trực tuyến

**Tổng quan về DNS**

DNS được coi là nguồn trung gian cho mọi hoạt động liên lạc qua Internet. Chức năng chính của DNS là dịch tên miền sang địa chỉ IP và ngược lại để cho phép liên lạc giữa người-máy-mạng-internet. Vì mỗi thiết bị có một địa chỉ IP duy nhất nên con người khó có thể ghi nhớ tất cả các địa chỉ IP của ứng dụng được yêu cầu. DNS giúp chuyển đổi địa chỉ IP sang định dạng miền dễ hiểu hơn, giúp giảm bớt gánh nặng cho con người.

Nhiệm vụ 1: Thu thập thông tin DNS bằng Tiện ích dòng lệnh nslookup và Công cụ trực tuyến

nslookup là một tiện ích dòng lệnh quản trị mạng, thường được sử dụng để truy vấn DNS để lấy tên miền hoặc ánh xạ địa chỉ IP hoặc cho bất kỳ bản ghi DNS cụ thể nào khác. Tiện ích này có sẵn dưới dạng tiện ích dòng lệnh và ứng dụng web.

Tại đây, chúng tôi sẽ thực hiện thu thập thông tin DNS về các tổ chức mục tiêu bằng cách sử dụng tiện ích dòng lệnh nslookup và ứng dụng web NSLOOKUP.

1.  Trong máy Windows 11, hãy khởi chạy Dấu nhắc lệnh và chạy lệnh nslookup. Thao tác này sẽ hiển thị máy chủ mặc định và địa chỉ của nó được chỉ định cho máy Windows 11.

2.  Trong chế độ tương tác nslookup, hãy nhập set type=a và nhấn Enter. Việc đặt loại là \"a\" sẽ định cấu hình nslookup để truy vấn địa chỉ IP của một miền nhất định.

3.  Nhập miền mục tiêu www.certifiedhacker.com và nhấn Enter. Thao tác này sẽ giải quyết địa chỉ IP và hiển thị kết quả như trong ảnh chụp màn hình.

> ![Screenshot](media/image11.jpeg){width="6.1363670166229225in" height="4.604073709536308in"}

4.  Hai dòng đầu tiên trong kết quả là:

> Máy chủ: dns.google và Địa chỉ: 8.8.8.8
>
> Điều này chỉ định rằng kết quả đã được chuyển hướng đến máy chủ mặc định được lưu trữ trên máy cục bộ (Windows 11) để phân giải miền được yêu cầu của bạn.

5.  Do đó, nếu phản hồi đến từ máy chủ của máy cục bộ của bạn (Google), chứ không phải máy chủ lưu trữ hợp pháp miền www.certifiedhacker.com; nó được coi là một câu trả lời không có thẩm quyền. Ở đây, địa chỉ IP của miền mục tiêu www.certifiedhacker.com là 162.241.216.11.

6.  Vì kết quả trả về không có thẩm quyền nên bạn cần có được máy chủ định danh có thẩm quyền của miền.

7.  Nhập set type=cname và nhấn Enter. Việc tra cứu CNAME được thực hiện trực tiếp trên máy chủ định danh có thẩm quyền của tên miền và liệt kê các bản ghi CNAME cho tên miền.

8.  Nhập certifiedhacker.com và nhấn Enter.

9.  Thao tác này sẽ trả về máy chủ định danh có thẩm quyền của miền (ns1.bluehost.com), cùng với địa chỉ máy chủ thư (dnsadmin.box5331.bluehost.com), như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image12.jpeg){width="7.237015529308836in" height="5.429882983377078in"}

10. Vì bạn đã có được máy chủ tên có thẩm quyền nên bạn sẽ cần xác định địa chỉ IP của máy chủ tên.

11. Ra lệnh set type=a và nhấn Enter.

12. Nhập ns1.bluehost.com (hoặc máy chủ định danh chính được hiển thị trong môi trường lab của bạn) và nhấn Enter. Điều này trả về địa chỉ IP của máy chủ, như trong ảnh chụp màn hình.

> ![Screenshot](media/image13.jpeg){width="6.20782261592301in" height="4.657687007874015in"}

13. Máy chủ tên có thẩm quyền lưu trữ các bản ghi liên quan đến tên miền. Vì vậy, nếu kẻ tấn công có thể xác định máy chủ tên có thẩm quyền (máy chủ tên chính) và lấy địa chỉ IP liên quan của nó, kẻ đó có thể cố gắng khai thác máy chủ để thực hiện các cuộc tấn công như DoS, DDoS, Chuyển hướng URL, v.v.

14. Bạn cũng có thể thực hiện các thao tác tương tự bằng công cụ trực tuyến NSLOOKUP. Tiến hành một loạt truy vấn và xem lại thông tin để làm quen với công cụ NSLOOKUP và thu thập thông tin.

15. Bây giờ, chúng tôi sẽ sử dụng công cụ trực tuyến NSLOOKUP để thu thập thông tin DNS về tên miền mục tiêu.

16. Mở bất kỳ trình duyệt web nào và truy cập http://www.kloth.net/services/nslookup.php (ở đây, chúng tôi đang sử dụng Mozilla Firefox).

17. Trang web NSLOOKUP xuất hiện như trong ảnh chụp màn hình.

18. Sau khi trang web mở ra, trong trường Miền: , hãy nhập www.certifiedhacker.com. Đặt trường Truy vấn: thành \[A (địa chỉ IPv4)\] mặc định và nhấp vào nút Tra cứu để xem lại kết quả được hiển thị.

> ![Screenshot](media/image14.jpeg){width="6.121019247594051in" height="4.592557961504812in"}

19. Trong trường Truy vấn: , hãy nhấp vào mũi tên thả xuống và kiểm tra các tùy chọn khác nhau có sẵn, như minh họa trong ảnh chụp màn hình.

20. Như bạn có thể thấy, có tùy chọn cho AAAA (địa chỉ IPv6); chọn mục đó và nhấp vào Tra cứu. Thực hiện các truy vấn liên quan đến vấn đề này vì cũng có những cuộc tấn công có thể xảy ra trên mạng IPv6.

> ![1.11.jpg](media/image15.jpeg){width="6.059019028871391in" height="4.546041119860018in"}
>
> ![Screenshot](media/image16.jpeg){width="6.21402012248469in" height="4.662335958005249in"}

21. Điều này kết thúc việc trình diễn thu thập thông tin DNS bằng tiện ích dòng lệnh nslookup và công cụ trực tuyến NSLOOKUP.

22. Bạn cũng có thể sử dụng các công cụ tra cứu DNS như DNSdumpster (https://dnsdumpster.com) để trích xuất thông tin DNS mục tiêu bổ sung.

23. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 2.5.1.1**

Sử dụng tiện ích dòng lệnh nslookup để tìm máy chủ tên chính của trang web www.certifiedhacker.com.

Lab 6: Thực hiện Dấu chân Mạng

**Kịch bản bài lab**

Với địa chỉ IP, tên máy chủ và miền có được trong các bước thu thập thông tin trước đó, với tư cách là một hacker chuyên nghiệp, nhiệm vụ tiếp theo của bạn là thực hiện theo dõi mạng để thu thập thông tin liên quan đến mạng của tổ chức mục tiêu như phạm vi mạng, traceroute, giá trị TTL, v.v. Thông tin này sẽ giúp bạn tạo bản đồ của mạng mục tiêu và thực hiện cuộc tấn công trung gian.

**Mục tiêu bài lab**

-   Thực hiện theo dõi mạng trong Máy Windows và Linux

**Tổng quan về Dấu chân Mạng**

Dấu chân mạng là một quá trình tích lũy dữ liệu liên quan đến một môi trường mạng cụ thể. Nó cho phép các hacker có đạo đức vẽ sơ đồ mạng và phân tích mạng mục tiêu chi tiết hơn để thực hiện các cuộc tấn công nâng cao.

Nhiệm vụ 1: Thực hiện theo dõi mạng trong máy Windows và Linux

Tuyến đường là đường dẫn mà gói mạng đi qua giữa nguồn và đích. Định tuyến theo dõi mạng là một quá trình xác định đường dẫn và các máy chủ nằm giữa nguồn và đích. Định tuyến theo dõi mạng cung cấp thông tin quan trọng như địa chỉ IP của máy chủ nằm giữa nguồn và đích, cho phép bạn ánh xạ cấu trúc liên kết mạng của tổ chức. Traceroute có thể được sử dụng để trích xuất thông tin về cấu trúc liên kết mạng, bộ định tuyến đáng tin cậy, vị trí tường lửa, v.v.

Ở đây, chúng tôi sẽ thực hiện theo dõi mạng bằng cả máy Windows và Linux.

Ở đây, chúng tôi sẽ coi www.certifiedhacker.com là trang web mục tiêu. Tuy nhiên, bạn có thể chọn miền mục tiêu theo ý muốn.

1.  Trong máy Windows 11, hãy mở cửa sổ Dấu nhắc lệnh. Chạy lệnh tracert www.certifiedhacker.com để xem các bước nhảy mà các gói đã thực hiện trước khi đến đích.

> Kết quả có thể khác nhau khi bạn thực hiện bài lab.
>
> ![Screenshot](media/image17.jpeg){width="6.415518372703412in" height="4.8135192475940505in"}

2.  Chạy tracert /? lệnh để xem các tùy chọn khác nhau cho lệnh, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image18.jpeg){width="5.989994531933508in" height="4.494251968503937in"}

3.  Chạy lệnh tracert -h 5 www.certifiedhacker.com để thực hiện theo dõi nhưng chỉ cho phép tối đa 5 bước nhảy.

> -h: Số bước nhảy tối đa.
>
> ![Screenshot](media/image19.jpeg){width="6.524017935258093in" height="4.8949256342957135in"}

4.  Sau khi xem kết quả, đóng cửa sổ nhắc lệnh.

5.  Bây giờ, hãy nhấp vào Bảo mật Parrot để chuyển sang máy Bảo mật Parrot và mở cửa sổ terminal / dòng lệnh.[Parrot Security](https://labclient.labondemand.com/Instructions/e6a97cad-3982-464f-a2d8-79d028c77385)

6.  Chạy lệnh traceroute www.certifiedhacker.com để xem các bước nhảy mà các gói đã thực hiện trước khi đến đích.

> Vì chúng ta đã thiết lập một mạng đơn giản nên bạn có thể tìm thấy bước nhảy trực tiếp từ nguồn tới đích đích. Tuy nhiên, ảnh chụp màn hình có thể khác nhau tùy thuộc vào đích đến.
>
> ![Screenshot](media/image20.jpeg){width="6.4000196850393705in" height="4.801890857392826in"}

7.  Phần này kết thúc phần minh họa việc thực hiện định tuyến mạng bằng máy Windows và Linux.

8.  Bạn cũng có thể sử dụng các công cụ theo dõi khác như PingPlotter (https://www.pingplotter.com/), Traceroute NG (https://www.solarwinds.com), v.v. để trích xuất thông tin mạng bổ sung của tổ chức mục tiêu.

9.  Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 2.6.1.1**

Thực hiện theo dõi mạng bằng lệnh traceroute trên máy Parrot cho miền www.certifiedhacker.com. Nhập địa chỉ IP của miền mục tiêu.

Lab 7: Thực hiện in dấu chân email

**Kịch bản bài lab**

Là một hacker có đạo đức chuyên nghiệp, bạn cần có khả năng theo dõi email của các cá nhân (nhân viên) từ một tổ chức mục tiêu để thu thập thông tin quan trọng có thể giúp xây dựng chiến lược hack hiệu quả. Theo dõi email cho phép bạn thu thập thông tin như địa chỉ IP, máy chủ thư, chi tiết hệ điều hành, vị trí địa lý, thông tin về các nhà cung cấp dịch vụ liên quan đến việc gửi thư, v.v. Bằng cách sử dụng thông tin này, bạn có thể thực hiện kỹ thuật xã hội và các cuộc tấn công nâng cao khác.

**Mục tiêu bài lab**

-   Thu thập thông tin về mục tiêu bằng cách truy tìm email bằng eMailTrackerPro

**Tổng quan về Dấu chân Email**

Dấu chân hoặc theo dõi e-mail là một phương pháp để giám sát hoặc theo dõi email được gửi đến người nhận dự kiến. Kiểu theo dõi này có thể thực hiện được thông qua các bản ghi được đóng dấu thời gian kỹ thuật số tiết lộ ngày và giờ khi mục tiêu nhận và mở một email cụ thể.

Dấu chân email tiết lộ thông tin như:.

-   Địa chỉ IP hệ thống của người nhận

-   Tọa độ GPS và bản đồ vị trí của người nhận

-   Khi một tin nhắn email được nhận và đọc

-   Loại máy chủ được người nhận sử dụng

-   Thông tin về hệ điều hành và trình duyệt

-   Nếu một email phá hoại được gửi đi

-   Thời gian đọc email

-   Người nhận có truy cập bất kỳ liên kết nào được gửi trong email hay không

-   PDF và các loại tệp đính kèm khác

-   Nếu tin nhắn được đặt hết hạn sau một thời gian nhất định

Nhiệm vụ 1: Thu thập thông tin về mục tiêu bằng cách truy tìm email bằng eMailTrackerPro

Tiêu đề email là một phần quan trọng của bất kỳ email nào và nó được coi là nguồn thông tin tuyệt vời cho bất kỳ hacker có đạo đức nào thực hiện các cuộc tấn công nhằm vào mục tiêu. Tiêu đề email chứa thông tin chi tiết về người gửi, thông tin định tuyến, sơ đồ địa chỉ, ngày, chủ đề, người nhận, v.v. Ngoài ra, tiêu đề email giúp tin tặc có đạo đức theo dõi đường dẫn định tuyến của email trước khi gửi nó đến người nhận.

Tại đây, chúng tôi sẽ thu thập thông tin bằng cách phân tích tiêu đề email bằng eMailTrackerPro.

1.  Nhấp vào Windows 11 để chuyển sang máy Windows 11 , điều hướng đến E:\\CEH-Tools\\CEHv13 Mô-đun 02 Footprinting and Reconnaissance\\Email Tracking Tools\\eMailTrackerPro và nhấp đúp vào emt.exe.[Windows 11](https://labclient.labondemand.com/Instructions/e6a97cad-3982-464f-a2d8-79d028c77385)

2.  Nếu cửa sổ bật lên Kiểm soát tài khoản người dùng xuất hiện, hãy nhấp vào Có.

3.  Cửa sổ Thiết lập eMailTrackerPro xuất hiện. Làm theo các bước của trình hướng dẫn (bằng cách chọn các tùy chọn mặc định) để cài đặt eMailTrackerPro.

4.  Sau khi quá trình cài đặt hoàn tất, trong Hoàn tất Trình hướng dẫn thiết lập eMailTrackerPro, hãy bỏ chọn hộp kiểm Hiển thị Readme và nhấp vào nút Hoàn tất để khởi chạy eMailTrackerPro.

> ![Screenshot](media/image21.jpeg){width="6.384518810148731in" height="4.790260279965004in"}

5.  Cửa sổ chính của eMailTrackerPro xuất hiện cùng với cửa sổ bật lên Lựa chọn phiên bản; nhấp vào OK.

> ![Screenshot](media/image22.jpeg){width="6.741017060367454in" height="5.057738407699038in"}

6.  Cửa sổ chính eMailTrackerPro xuất hiện như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image23.jpeg){width="5.385441819772528in" height="4.040659448818897in"}

7.  Để theo dõi tiêu đề email, hãy nhấp vào biểu tượng Báo cáo dấu vết của tôi từ phần Xem . (tại đây, bạn sẽ thấy báo cáo đầu ra của tiêu đề email được theo dõi).

8.  Nhấp vào biểu tượng Tiêu đề theo dõi từ phần Dấu vết email mới để bắt đầu theo dõi.

> ![Screenshot](media/image24.jpeg){width="5.795325896762905in" height="4.348192257217848in"}

9.  Một cửa sổ bật lên sẽ xuất hiện; chọn Theo dõi email tôi đã nhận được. Sao chép tiêu đề email từ email đáng ngờ mà bạn muốn theo dõi và dán tiêu đề đó vào trường Tiêu đề email: trong phần Nhập chi tiết .

> ![Screenshot](media/image25.jpeg){width="6.6172517497812775in" height="4.964877515310586in"}

10. Để tìm tiêu đề email, hãy mở bất kỳ trình duyệt web nào và đăng nhập vào bất kỳ tài khoản email nào bạn chọn; từ hộp thư đến email, mở thư bạn muốn xem tiêu đề.

> Trong Gmail, hãy tìm tiêu đề email bằng cách làm theo các bước:

-   Mở một email; nhấp vào mũi tên biểu tượng dấu chấm (Thêm) bên cạnh biểu tượng Trả lời ở góc trên bên phải của ngăn thư.

-   Chọn Hiển thị bản gốc từ danh sách.

-   Cửa sổ Thư gốc xuất hiện trong tab trình duyệt mới với tất cả thông tin chi tiết về email, bao gồm tiêu đề email

> ![st10.jpg](media/image26.jpeg){width="6.1361439195100616in" height="4.603907480314961in"}
>
> Trong Outlook, tìm tiêu đề email bằng cách làm theo các bước:

-   Bấm đúp vào email để mở nó trong cửa sổ mới

-   Nhấp vào biểu tượng ... (Tác vụ khác) ở bên phải ngăn thông báo để mở tùy chọn tin nhắn

-   Từ các tùy chọn, hãy nhấp vào Xem

-   Cửa sổ xem nguồn thư xuất hiện với tất cả thông tin chi tiết về email, bao gồm tiêu đề email

> ![mail2.jpg](media/image27.jpeg){width="6.554905949256343in" height="4.918101487314086in"}

11. Sao chép toàn bộ văn bản tiêu đề email và dán vào trường Tiêu đề email: của eMailTrackerPro và nhấp vào Dấu vết.

> Ở đây, chúng tôi đang phân tích tiêu đề email từ tài khoản gmail. Tuy nhiên, bạn cũng có thể phân tích tiêu đề email từ tài khoản Outlook.
>
> ![mail3.jpg](media/image28.jpeg){width="6.4928947944007in" height="4.871574803149606in"}

12. Cửa sổ Báo cáo dấu vết của tôi sẽ mở ra.

13. Vị trí email sẽ được theo dõi trong Bản đồ (GUI bản đồ thế giới). Bạn cũng có thể xem bản tóm tắt bằng cách chọn Tóm tắt qua email ở phía bên phải cửa sổ. Phần Bảng ngay bên dưới Bản đồ hiển thị toàn bộ bước nhảy trong tuyến đường, cùng với IP và các vị trí nghi ngờ cho mỗi bước nhảy.

> ![13.jpg](media/image29.jpeg){width="6.893605643044619in" height="5.172226596675416in"}

14. Để kiểm tra dữ liệu Network Whois, hãy nhấp vào nút Network Whois bên dưới Tóm tắt Email để xem dữ liệu Network Whois.

> ![st14.jpg](media/image30.jpeg){width="6.498188976377953in" height="4.875546806649169in"}

15. Điều này kết thúc việc trình diễn thu thập thông tin thông qua phân tích tiêu đề email bằng eMailTrackerPro.

16. Bạn cũng có thể sử dụng các công cụ theo dõi email như MxToolbox (https://mxtoolbox.com/), Social Catfish (https://socialcatfish.com/), IP2Location Email Header Tracer (https://www.ip2location.com/), v.v. để theo dõi email và trích xuất thông tin mục tiêu như danh tính người gửi, máy chủ thư, địa chỉ IP, vị trí của người gửi, v.v.

17. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 2.7.1.1**

Trên máy Windows 11, sử dụng công cụ eMailTrackerPro có tại E:\\CEH-Tools\\CEHv13 Module 02 Footprinting and Reconnaissance\\Email Tracking Tools\\eMailTrackerPro để thu thập thông tin về email bằng cách phân tích tiêu đề email. Quan sát đầu ra và nhập CÓ nếu công cụ có tính năng "Báo cáo lạm dụng"; nếu không, hãy nhập KHÔNG.

Lab 8: Thực hiện Dấu chân bằng nhiều công cụ Dấu chân khác nhau

**Kịch bản bài lab**

Thông tin được thu thập ở các bước trước có thể không đủ để tiết lộ các lỗ hổng tiềm ẩn của mục tiêu. Có thể có nhiều thông tin hơn có thể giúp tìm ra sơ hở trong mục tiêu. Là một hacker có đạo đức, bạn nên tìm kiếm càng nhiều thông tin càng tốt về mục tiêu bằng nhiều công cụ khác nhau. Hoạt động trong bài lab này sẽ chứng minh những thông tin khác mà bạn có thể trích xuất từ ​​mục tiêu bằng cách sử dụng các công cụ dấu chân khác nhau.

**Mục tiêu bài lab**

-   Dấu chân mục tiêu bằng Recon-ng

**Tổng quan về Công cụ Dấu chân**

Công cụ Footprinting được sử dụng để thu thập thông tin cơ bản về hệ thống mục tiêu nhằm khai thác chúng. Thông tin được thu thập bởi các công cụ dấu chân chứa thông tin vị trí IP của mục tiêu, thông tin định tuyến, thông tin doanh nghiệp, địa chỉ, số điện thoại và số an sinh xã hội, chi tiết về nguồn của email và tệp, thông tin DNS, thông tin tên miền, v.v.

Nhiệm vụ 1: Theo dõi mục tiêu bằng Recon-ng

Recon-ng là một khung trinh sát web với các mô-đun độc lập và tương tác cơ sở dữ liệu cung cấp một môi trường trong đó có thể tiến hành trinh sát dựa trên web nguồn mở. Tại đây, chúng tôi sẽ sử dụng Recon-ng để thực hiện trinh sát mạng, thu thập thông tin nhân sự và thu thập thông tin mục tiêu từ các trang mạng xã hội.

Ở đây, chúng tôi sẽ coi www.certifiedhacker.com là trang web mục tiêu. Tuy nhiên, bạn có thể chọn miền mục tiêu theo ý muốn.

Kết quả thu được có thể khác khi bạn thực hiện nhiệm vụ thí nghiệm này.

1.  Trong máy Bảo mật Parrot, hãy mở một cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập cả mật khẩu).

> Mật khẩu bạn gõ sẽ không hiển thị.

2.  Bây giờ, hãy chạy lệnh cd để chuyển đến thư mục gốc và chạy lệnh recon-ng để khởi chạy ứng dụng.

> ![Screenshot](media/image31.jpeg){width="6.989016841644794in" height="5.243811242344707in"}

3.  Chạy lệnh trợ giúp để xem tất cả các lệnh cho phép bạn thêm/xóa bản ghi vào cơ sở dữ liệu, truy vấn cơ sở dữ liệu, v.v.

> ![Screenshot](media/image32.jpeg){width="10.6625in" height="8.0in"}

4.  Chạy lệnh cài đặt tất cả trên thị trường để cài đặt tất cả các mô-đun có sẵn trong bản recon-ng.

> Bỏ qua các lỗi trong khi chạy lệnh.
>
> ![Screenshot](media/image33.jpeg){width="9.578534558180227in" height="7.186708223972004in"}

5.  Sau khi cài đặt mô-đun, hãy chạy lệnh tìm kiếm mô-đun. Điều này hiển thị tất cả các mô-đun có sẵn trong recon-ng.

> ![Screenshot](media/image34.jpeg){width="10.6625in" height="8.0in"}

6.  Bạn sẽ có thể thực hiện khám phá, khai thác, trinh sát mạng, v.v. bằng cách tải các mô-đun cần thiết.

7.  Chạy lệnh không gian làm việc để xem các lệnh liên quan đến không gian làm việc.

> ![Screenshot](media/image35.jpeg){width="10.6625in" height="8.0in"}

8.  Tạo một không gian làm việc để thực hiện trinh sát mạng. Trong nhiệm vụ này, chúng ta sẽ tạo một không gian làm việc có tên là CEH.

9.  Để tạo không gian làm việc, hãy chạy lệnh tạo không gian làm việc CEH. Điều này tạo ra một không gian làm việc có tên CEH.

> ![Screenshot](media/image36.jpeg){width="6.927015529308837in" height="5.1972922134733155in"}

10. Nhập danh sách không gian làm việc. Thao tác này sẽ hiển thị danh sách các không gian làm việc (cùng với không gian làm việc được thêm ở bước trước) có trong cơ sở dữ liệu không gian làm việc.

> ![Screenshot](media/image37.jpeg){width="10.6625in" height="8.0in"}

11. Thêm miền mà bạn muốn thực hiện trinh sát mạng.

12. Ra lệnh chèn miền db.

13. Trong tùy chọn miền (TEXT), hãy nhập certifiedhacker.com và nhấn Enter. Trong tùy chọn ghi chú (TEXT) nhấn Enter. Điều này thêm Certifiedhacker.com vào không gian làm việc hiện tại.

14. Bạn có thể xem miền đã thêm bằng cách đưa ra lệnh hiển thị miền như trong ảnh chụp màn hình.

> ![Screenshot](media/image38.jpeg){width="10.6625in" height="8.0in"}

15. Thu thập thông tin liên quan đến máy chủ được liên kết với certifiedhacker.com bằng cách tải các mô-đun trinh sát mạng như brute_hosts, Netcraft và Bing.

16. Ra lệnh tải mô-đun để xem tất cả các mô-đun liên quan đến cưỡng bức vũ phu. Trong nhiệm vụ này, chúng ta sẽ sử dụng mô-đun recon/domains-hosts/brute_hosts để thu thập máy chủ.

> ![Screenshot](media/image39.jpeg){width="10.6625in" height="8.0in"}

17. Để tải mô-đun recon/domains-hosts/brute_hosts , hãy đưa ra lệnh tải mô-đun recon/domains-hosts/brute_hosts.

18. Đưa ra lệnh chạy. Điều này bắt đầu thu hoạch các máy chủ, như thể hiện trong ảnh chụp màn hình.

> ![Screenshot](media/image40.jpeg){width="10.6625in" height="8.0in"}

19. Quan sát xem máy chủ đã được thêm bằng cách chạy mô-đun recon/domains-hosts/brute_hosts.

> ![Screenshot](media/image41.jpeg){width="10.6625in" height="8.0in"}

20. Bây giờ bạn đã thu thập được các máy chủ liên quan đến Certifiedhacker.com bằng mô-đun brute_hosts. Bạn có thể sử dụng các mô-đun khác như Netcraft và Bing để thu thập thêm máy chủ.

> Sử dụng lệnh quay lại để quay lại terminal / dòng lệnh thuộc tính CEH.
>
> Để phân giải máy chủ bằng mô-đun Bing, hãy sử dụng các lệnh sau:

-   **quay lại**

-   **mô-đun tải recon/domains-hosts/bing_domain_web**

-   **chạy**

21. Bây giờ, hãy thực hiện tra cứu ngược cho từng địa chỉ IP (địa chỉ IP thu được trong quá trình trinh sát) để phân giải thành tên máy chủ tương ứng.

22. Thực thi lệnh tải mô-đun Reverse_resolve để xem tất cả các mô-đun được liên kết với từ khóa Reverse_resolve. Trong nhiệm vụ này, chúng ta sẽ sử dụng mô-đun recon/hosts-hosts/reverse_resolve.

23. Chạy lệnh recon/hosts-hosts/reverse_resolve tải mô-đun để tải mô-đun.

24. Ra lệnh chạy để bắt đầu tra cứu ngược lại.

> ![Screenshot](media/image42.jpeg){width="8.683063210848644in" height="6.51484251968504in"}

25. Sau khi thực hiện xong quy trình tra cứu ngược, hãy chạy lệnh hiển thị máy chủ. Điều này sẽ hiển thị tất cả các máy chủ đã được thu hoạch cho đến nay, như trong ảnh chụp màn hình.

> ![Screenshot](media/image43.jpeg){width="6.857233158355205in" height="5.1449343832020995in"}

26. Bây giờ, hãy sử dụng lệnh quay lại để quay lại terminal / dòng lệnh thuộc tính CEH.

27. Bây giờ, bạn đã thu thập được một số máy chủ, chúng tôi sẽ chuẩn bị một báo cáo chứa tất cả các máy chủ.

28. Thực thi lệnh báo cáo tải mô-đun để xem tất cả các mô-đun được liên kết với từ khóa báo cáo. Trong bài lab này, chúng tôi sẽ lưu báo cáo ở định dạng HTML. Vì vậy, mô-đun được sử dụng là báo cáo/html.

29. Chạy lệnh báo cáo tải mô-đun/html.

30. Lưu ý rằng bạn cần chỉ định giá trị cho các tùy chọn CREATOR và CUSTOMER trong khi giá trị FILENAME đã được đặt và bạn có thể thay đổi giá trị nếu cần. Để làm như vậy, hãy chạy các lệnh dưới đây:

    -   **tùy chọn đặt TÊN TỆP /home/Attacker/Desktop/results.html. Bằng cách ban hành lệnh này, bạn đang đặt tên báo cáo là results.html và đường dẫn lưu trữ tệp dưới dạng Máy tính để bàn.**

    -   **tùy chọn đặt CREATOR \[tên của bạn\] (tại đây, Jason).**

    -   **tùy chọn đặt Mạng lưới hacker được chứng nhận của KHÁCH HÀNG (vì bạn đã thực hiện thăm dò mạng trên miền certifiedhacker.com).**

31. Sử dụng lệnh chạy và nhấn Enter để tạo báo cáo cho tất cả các máy chủ đã được thu hoạch.

> ![1.13.jpg](media/image44.jpeg){width="7.089822834645669in" height="5.319444444444445in"}

32. Báo cáo đã tạo sẽ được lưu vào /home/kẻ tấn công/Máy tính để bàn/.

33. Điều hướng đến /home/Attacker/Desktop/, nhấp chuột phải vào tệp results.html, nhấp vào Mở bằng và chọn trình duyệt Web Firefox ESR từ các tùy chọn có sẵn.

> ![Screenshot](media/image45.jpeg){width="8.90140857392826in" height="6.678665791776028in"}

34. Báo cáo đã tạo sẽ xuất hiện trong trình duyệt Firefox, hiển thị bản tóm tắt về máy chủ đã thu hoạch.

35. Bạn có thể mở rộng nút Máy chủ để xem tất cả các máy chủ đã thu hoạch, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image46.jpeg){width="8.473732502187227in" height="6.357782152230971in"}

36. Đóng tất cả các cửa sổ đang mở.

37. Cho đến nay, chúng tôi đã sử dụng công cụ Recon-ng để thực hiện trinh sát mạng trên miền mục tiêu

38. Bây giờ, chúng ta sẽ sử dụng Recon-ng để thu thập thông tin nhân sự.

39. Mở cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).

> Mật khẩu bạn gõ sẽ không hiển thị.

40. Chạy lệnh cd để chuyển đến thư mục gốc và chạy lệnh recon-ng.

41. Thêm không gian làm việc bằng cách ra lệnh không gian làm việc tạo trinh sát và nhấn Enter. Điều này tạo ra một không gian làm việc có tên trinh sát.

> ![Screenshot](media/image47.jpeg){width="9.357573272090988in" height="7.020923009623797in"}

42. Đặt một miền và thực hiện dấu vết trên đó để trích xuất các liên hệ có sẵn trong miền.

43. Thực thi lệnh tải recon/domains-contacts/whois_pocs của mô-đun. Mô-đun này sử dụng ARIN Whois RWS để thu thập dữ liệu POC từ các truy vấn Whois cho tên miền nhất định.

44. Chạy lệnh thông tin để xem các tùy chọn cần thiết để chạy mô-đun này.

45. Chạy tùy chọn đặt lệnh SOURCE facebook.com để thêm facebook.com làm miền mục tiêu.

> Ở đây, chúng tôi đang sử dụng facebook.com làm tên miền mục tiêu để thu thập thông tin liên hệ.
>
> ![Screenshot](media/image48.jpeg){width="6.964175415573053in" height="5.225172790901137in"}

46. Thực hiện lệnh chạy. Mô-đun recon/domains-contacts/whois_pocs trích xuất các địa chỉ liên hệ được liên kết với miền và hiển thị chúng, như minh họa trong ảnh chụp màn hình

> Kết quả có thể khác nhau khi bạn thực hiện bài lab.
>
> ![Screenshot](media/image49.jpeg){width="10.49726377952756in" height="7.8760247156605425in"}

47. Cho đến thời điểm hiện tại, chúng tôi đã có được các liên hệ liên quan đến miền. Ghi lại tên của những người liên hệ này. Đóng tất cả các cửa sổ đang mở.

48. Bây giờ, chúng tôi sẽ sử dụng Recon-ng để trích xuất danh sách tên miền phụ và địa chỉ IP được liên kết với URL mục tiêu.

49. Mở cửa sổ terminal / dòng lệnh và thực thi sudo su để chạy các chương trình với tư cách là người dùng root (Khi được nhắc, hãy nhập mật khẩu).

> Mật khẩu bạn gõ sẽ không hiển thị.

50. Bây giờ, hãy chạy lệnh cd để chuyển đến thư mục gốc và chạy lệnh recon-ng.

51. Để trích xuất danh sách miền phụ và địa chỉ IP được liên kết với URL mục tiêu, chúng ta cần tải mô-đun recon/domains-hosts/hackertarget.

52. Chạy lệnh tải recon/domains-hosts/hackertarget mô-đun và chạy tùy chọn đặt lệnh SOURCE Certifiedhacker.com.

53. Thực hiện lệnh chạy. Mô-đun recon/domains-hosts/hackertarget tìm kiếm danh sách miền phụ và địa chỉ IP được liên kết với URL mục tiêu và trả về danh sách miền phụ cũng như địa chỉ IP của chúng.

> ![Screenshot](media/image50.jpeg){width="9.136614173228347in" height="6.85513779527559in"}

54. Điều này kết thúc việc trình diễn thu thập thông tin máy chủ của miền mục tiêu và thu thập thông tin nhân sự của tổ chức mục tiêu.

55. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 2.8.1.1**

Sử dụng công cụ Recon-ng để thu thập thông tin nhân sự. Nhập tên mô-đun Recon-ng để trích xuất các liên hệ được liên kết với miền và hiển thị chúng.

Lab 9: Thực hiện Dấu chân bằng AI

**Kịch bản bài lab**

Trong bài lab này, bạn sẽ sử dụng AI để phân tích và lập bản đồ dấu chân kỹ thuật số từ dữ liệu mạng xã hội. AI sẽ xác định các mẫu và nêu bật các rủi ro về quyền riêng tư. Bằng cách so sánh những hiểu biết sâu sắc do AI tạo ra với phân tích thủ công, sinh viên sẽ hiểu được sức mạnh và những hạn chế của AI trong an ninh mạng.

**Mục tiêu bài lab**

-   Dấu chân mục tiêu bằng ShellGPT

**Tổng quan về Dấu chân sử dụng AI**

Dấu chân sử dụng AI tăng tốc quá trình trinh sát bằng cách tự động hóa việc thu thập và phân tích dữ liệu, cho phép các chuyên gia bảo mật phát hiện ra các lỗ hổng hiệu quả hơn. Dấu vết được hỗ trợ bởi AI giúp tăng cường thông tin về mối đe dọa bằng cách xác định các mẫu và điểm bất thường trong lượng dữ liệu khổng lồ, cung cấp thông tin chuyên sâu hơn về các rủi ro tiềm ẩn. Là một hacker có đạo đức, bạn nên tìm kiếm càng nhiều thông tin càng tốt về mục tiêu bằng AI.

Nhiệm vụ 1: Dấu chân mục tiêu bằng ShellGPT

Dấu chân với ShellGPT liên quan đến việc tận dụng khả năng tạo tập lệnh shell cùng với khả năng xử lý ngôn ngữ của GPT. Bằng cách tạo các tập lệnh phù hợp, ShellGPT tự động hóa việc thu thập dữ liệu từ nhiều nguồn khác nhau, bao gồm cơ sở dữ liệu WHOIS và diễn đàn trực tuyến. Nó phân tích và trích xuất thông tin liên quan như đăng ký tên miền, địa chỉ IP và cấu hình mạng. ShellGPT hợp lý hóa quy trình trinh sát, cho phép phân tích và xác định hiệu quả các lỗ hổng bảo mật tiềm ẩn. Sự tích hợp của nó giúp tăng cường giai đoạn in ấn với tự động hóa và xử lý dữ liệu thông minh.

Ở đây, chúng tôi sẽ sử dụng ShellGPT để thực hiện dấu chân trên mục tiêu.

Các lệnh do ShellGPT tạo ra có thể khác nhau tùy thuộc vào lời nhắc được sử dụng và các công cụ có sẵn trên máy. Do các biến này, kết quả đầu ra do ShellGPT tạo ra có thể khác với kết quả hiển thị trong ảnh chụp màn hình. Những khác biệt này xuất phát từ tính chất năng động trong quá trình xử lý của AI và môi trường đa dạng mà nó hoạt động. Do đó, bạn có thể quan sát thấy sự khác biệt trong cú pháp lệnh, cách thực thi và kết quả khi thực hiện nhiệm vụ thí nghiệm này.

1.  Trước khi bắt đầu bài lab này, hãy nhấp vào Bảo mật Parrot để chuyển sang máy Bảo mật Parrot và kết hợp ShellGPT bằng cách làm theo các bước được cung cấp trong Tích hợp ShellGPT trong Parrot Security Machine.pdf.[Parrot Security](https://labclient.labondemand.com/Instructions/e6a97cad-3982-464f-a2d8-79d028c77385)[Integrate ShellGPT in Parrot Security Machine.pdf](https://labondemand.blob.core.windows.net/content/lab168795/instructions267887/Integrate%20ShellGPT%20in%20Parrot%20%20Security%20Machine.pdf)

> Ngoài ra, bạn có thể làm theo các bước để tích hợp ShellGPT được cung cấp trong Mô-đun 00: Tích hợp ShellGPT trong Máy bảo mật Parrot.

2.  Sau khi kết hợp API ShellGPT trong máy Parrot Security, chúng tôi sẽ sử dụng ShellGPT để thu thập các email liên quan đến tổ chức mục tiêu. Để làm như vậy, hãy chạy sgpt \--chat foot \--shell \"Sử dụng theHarvester để thu thập các tài khoản email được liên kết với \'microsoft.com\', giới hạn kết quả ở 200 và tận dụng \'baidu\' làm nguồn dữ liệu\".

> Trong lời nhắc, hãy nhập E và nhấn Enter để thực thi lệnh.

3.  ShellGPT sẽ thu thập email bằng công cụHarvester và hiển thị danh sách email cũng như máy chủ.

> ![Screenshot](media/image51.jpeg){width="8.663008530183728in" height="6.499795494313211in"}
>
> ![Screenshot](media/image52.jpeg){width="10.6625in" height="8.0in"}

4.  Chúng tôi sẽ thực hiện dấu vết thông qua các trang mạng xã hội bằng cách sử dụng ShellGPT, để thực hiện việc này, hãy chạy lệnh sgpt \--chat foot \--shell \"Sử dụng Sherlock để thu thập thông tin cá nhân về \'Sundar Pichai\' và lưu kết quả vào lệnh recon2.txt\".

> Trong lời nhắc, hãy nhập E và nhấn Enter để thực thi lệnh.
>
> ![Screenshot](media/image53.jpeg){width="7.578013998250219in" height="5.685731627296588in"}

5.  Sau khi thực thi lệnh, trong terminal / dòng lệnh, hãy chạy lệnh ls để xem nội dung trong thư mục làm việc hiện tại.

> ![Screenshot](media/image54.jpeg){width="6.9734022309711285in" height="5.232095363079615in"}

6.  Chúng ta có thể thấy file recon2.txt được tạo bằng lệnh trước đó. Trong cửa sổ terminal, hãy chạy lệnh Pluma recon2.txt để xem nội dung của lệnh. Đóng cửa sổ soạn thảo văn bản.

> ![Screenshot](media/image55.jpeg){width="8.101589020122484in" height="6.07856627296588in"}ls

7.  Chúng tôi sẽ thực hiện tra cứu DNS bằng ShellGPT, để thực hiện việc này, hãy chạy lệnh sgpt \--chatfoot \--shell \"Cài đặt và sử dụng DNSRecon để thực hiện liệt kê DNS trên miền mục tiêu www.certifiedhacker.com\".

> Trong lời nhắc, hãy nhập E và nhấn Enter để thực thi lệnh.
>
> ![Screenshot](media/image56.jpeg){width="6.880639763779527in" height="5.162496719160105in"}

8.  Trong terminal / dòng lệnh, hãy chạy lệnh sgpt \--chat Footprint \--shell \"Thực hiện theo dõi mạng để khám phá các bộ định tuyến trên đường dẫn đến máy chủ đích www.certifiedhacker.com\" để thực hiện Traceroute tới một mục tiêu.

> Trong lời nhắc, hãy nhập E và nhấn Enter để thực thi lệnh.
>
> ![Screenshot](media/image57.jpeg){width="6.834016841644795in" height="5.127515310586177in"}

9.  Bây giờ hãy chạy sgpt \--chat Footprint \--shell \"Phát triển tập lệnh Python sẽ chấp nhận tên miền microsoft.com làm đầu vào và thực thi một loạt lệnh theo dõi trang web, bao gồm tra cứu DNS, truy xuất bản ghi WHOIS, liệt kê email, v.v. để thu thập thông tin về miền mục tiêu\" để chạy tập lệnh python nhằm tự động hóa các tác vụ theo dõi.

> Trong lời nhắc, hãy nhập E và nhấn Enter để thực thi lệnh.
>
> Có thể mất chút thời gian để phát triển và chạy tập lệnh.
>
> ![Screenshot](media/image58.jpeg){width="8.492509842519684in" height="6.371871172353456in"}

10. Ngoài các lệnh đã nói ở trên, bạn có thể khám phá thêm các tùy chọn bổ sung trong công cụ ShellGPT và sử dụng nhiều công cụ khác để tiến hành theo dõi mục tiêu.

11. Điều này kết thúc phần minh họa việc thực hiện dấu vết bằng ShellGPT.

12. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 2.9.1.1**

Sử dụng ShellGPT, viết lời nhắc và thực thi nó để thực hiện liệt kê DNS trên www.certifiedhacker.com. Nhập địa chỉ IP của NS ns2.bluehost.com.

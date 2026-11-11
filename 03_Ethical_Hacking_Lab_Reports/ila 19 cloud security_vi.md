Mô-đun 19: Điện toán đám mây

Kịch bản

Điện toán đám mây là một công nghệ mới nổi cung cấp các dịch vụ điện toán như ứng dụng kinh doanh trực tuyến, lưu trữ dữ liệu trực tuyến và webmail qua Internet. Việc triển khai đám mây cho phép phân bổ lực lượng lao động, giảm chi phí tổ chức, cung cấp bảo mật dữ liệu, v.v. Khi các doanh nghiệp ngày càng áp dụng các dịch vụ đám mây, hệ thống đám mây đã trở thành mục tiêu để những kẻ tấn công truy cập trái phép vào dữ liệu có giá trị được lưu trữ trong đó. Do đó, điều cần thiết là phải thường xuyên thực hiện pen testing trên các hệ thống đám mây để theo dõi tình trạng bảo mật của chúng.

Các quản trị viên bảo mật cho rằng hệ thống đám mây dễ bị tấn công DoS hơn vì chúng liên quan đến nhiều cá nhân hoặc khách hàng, khiến các cuộc tấn công DoS có khả năng rất nguy hiểm. Do khối lượng công việc cao trên một dịch vụ bị ngập lụt, các hệ thống này cố gắng cung cấp thêm sức mạnh tính toán (nhiều máy ảo hơn, nhiều phiên bản dịch vụ hơn) để xử lý khối lượng công việc và cuối cùng chúng sẽ thất bại.

Mặc dù các hệ thống đám mây cố gắng ngăn chặn những kẻ tấn công bằng cách cung cấp thêm sức mạnh tính toán, nhưng chúng vô tình hỗ trợ những kẻ tấn công bằng cách gây ra thiệt hại đáng kể nhất có thể xảy ra đối với tính khả dụng của dịch vụ - một quy trình bắt đầu từ một điểm truy nhập duy nhất của cuộc tấn công tràn ngập. Do đó, những kẻ tấn công không cần phải tấn công tất cả các máy chủ cung cấp một dịch vụ cụ thể mà chỉ cần tấn công một địa chỉ dựa trên đám mây duy nhất vào một dịch vụ không khả dụng. Vì vậy, bảo mật đầy đủ là rất quan trọng trong bối cảnh này, bởi vì các dịch vụ điện toán đám mây dựa trên việc chia sẻ.

Là một hacker có đạo đức và người thử nghiệm thâm nhập, bạn phải có kiến ​​thức vững chắc về hack nền tảng đám mây bằng nhiều công cụ và kỹ thuật khác nhau. Các bài lab trong mô-đun này sẽ cung cấp cho bạn trải nghiệm thời gian thực trong việc khai thác các lỗ hổng tiềm ẩn trong nền tảng đám mây mục tiêu bằng nhiều phương pháp và công cụ hack khác nhau. Tuy nhiên, việc hack nền tảng đám mây có thể là bất hợp pháp tùy thuộc vào chính sách của tổ chức và bất kỳ luật nào đang có hiệu lực. Với tư cách là người kiểm tra đạo đức hoặc bút, bạn phải luôn có được sự cho phép thích hợp trước khi thực hiện hack hệ thống.

Mục tiêu

Mục tiêu của bài lab là thực hiện hack nền tảng đám mây và các nhiệm vụ khác bao gồm nhưng không giới hạn ở:

-   Thực hiện liệt kê nhóm S3

-   Khai thác các nhóm S3 bị định cấu hình sai

-   Nâng cao đặc quyền của tài khoản người dùng IAM mục tiêu bằng cách khai thác các cấu hình sai trong chính sách người dùng

Tổng quan về Điện toán đám mây

Điện toán đám mây đề cập đến việc cung cấp các khả năng CNTT theo yêu cầu, trong đó cơ sở hạ tầng và ứng dụng CNTT được cung cấp cho người đăng ký dưới dạng dịch vụ được đo lường qua mạng. Các dịch vụ đám mây được phân thành ba loại, đó là cơ sở hạ tầng dưới dạng dịch vụ (IaaS), nền tảng dưới dạng dịch vụ (PaaS) và phần mềm dưới dạng dịch vụ (SaaS), cung cấp các kỹ thuật khác nhau để phát triển đám mây.

Nhiệm vụ bài lab

Tin tặc đạo đức hoặc chuyên gia kiểm thử xâm nhập (pentester) sử dụng nhiều công cụ và kỹ thuật để tấn công nền tảng đám mây mục tiêu. Các bài lab được đề xuất sẽ hỗ trợ bạn tìm hiểu các kỹ thuật hack nền tảng đám mây khác nhau bao gồm:

1.  Thực hiện trinh sát trên Azure

    -   Trinh sát Azure với AADInternals

2.  Khai thác thùng S3

    -   Khai thác các nhóm S3 mở bằng AWS CLI

3.  Thực hiện leo thang đặc quyền để đạt được đặc quyền cao hơn

    -   Nâng cao đặc quyền của người dùng IAM bằng cách khai thác chính sách người dùng bị định cấu hình sai

4.  Thực hiện đánh giá lỗ hổng trên Docker image

    -   Đánh giá lỗ hổng trên hình ảnh Docker bằng Trivy

Lab 1: Thực hiện trinh sát trên Azure

**Kịch bản bài lab**

Là một hacker có đạo đức, bạn cần biết cách sử dụng các công cụ tạo tập lệnh dựa trên lệnh PowerShell để tiến hành trinh sát và thu thập thông tin. Thông tin này sau đó có thể được sử dụng để đánh giá tình trạng bảo mật của các hệ thống khác trong mạng.

**Mục tiêu bài lab**

-   Trinh sát Azure với AADInternals

**Tổng quan về Công cụ Trinh sát**

Các công cụ trinh sát đóng vai trò là tài sản không thể thiếu đối với những kẻ tấn công trong việc hack đám mây, cung cấp cho chúng thông tin cần thiết và hiểu biết sâu sắc cần thiết để tổ chức các cuộc tấn công thành công chống lại môi trường đám mây.

Nhiệm vụ 1: Trinh sát Azure với AADInternals

AADInternals chủ yếu tập trung vào việc kiểm tra và tấn công các môi trường Azure Active Directory (AAD), nó vẫn có thể được sử dụng như một phần của nỗ lực trinh sát đám mây rộng hơn. Công cụ này có một số tính năng như liệt kê người dùng, trích xuất thông tin xác thực, trích xuất và thao tác mã thông báo, leo thang đặc quyền, v.v.

Trong bài lab này, chúng tôi sẽ thực hiện trinh sát Azure Active Directory với tư cách là người ngoài.

1.  Nhấp vào Windows 11 để chuyển sang máy Windows 11. Nhấp vào Ctrl+Alt+Delete để kích hoạt máy và đăng nhập bằng Admin/Pa\$\$w0rd.[Windows 11](https://labclient.labondemand.com/Instructions/7981ff11-6b1e-489c-a7f4-f384ab9a0ed0)

2.  Điều hướng đến E:\\CEH-Tools\\CEHv13 Mô-đun 19 Điện toán đám mây\\Công cụ GitHub\\ và sao chép thư mục AADInternals rồi dán vào Máy tính để bàn.

> ![Screenshot](media/image2.jpeg){width="10.6625in" height="8.0in"}

3.  Trong loại tìm kiếm Windows powershell và trong PowerShell nhấp vào Chạy với tư cách quản trị viên để mở cửa sổ PowerShell dành cho quản trị viên.

> Nếu cửa sổ Kiểm soát tài khoản người dùng xuất hiện, hãy nhấp vào Có.

4.  Trong cửa sổ PowerShell, hãy chạy lệnh cd C:\\Users\\Admin\\Desktop\\AADIternals để điều hướng đến thư mục AADInternals.

5.  Trong cửa sổ PowerShell, hãy chạy lệnh Install-Module AADInternals để cài đặt mô-đun AADInternals.

> Trong phần Bạn có muốn PowerShellGet cài đặt và nhập nhà cung cấp NuGet ngay bây giờ không? Nhập câu hỏi Y và nhấn Enter. Trong phần Bạn có chắc chắn muốn cài đặt các mô-đun từ \"PSGallery\" không? loại câu hỏi A và nhấn Enter.
>
> ![Screenshot](media/image3.jpeg){width="10.6625in" height="8.0in"}

6.  Bây giờ, hãy chạy lệnh Nhập mô-đun AADInternals để nhập mô-đun AADInternals.

> ![Screenshot](media/image4.jpeg){width="10.6625in" height="8.0in"}

7.  Bây giờ, chúng tôi sẽ thu thập thông tin có sẵn công khai của Azure AD mục tiêu như thương hiệu Đối tượng thuê, Tên đối tượng thuê, ID Đối tượng thuê cùng với tên của các miền đã được xác minh.

8.  Trong cửa sổ PowerShell, hãy chạy Invoke-AADIntReconAsOutsider -DomainName company.com \| Lệnh định dạng bảng.

> Trong lệnh trên, thay thế company.com bằng tên miền của công ty mục tiêu (ở đây, chúng tôi đang sử dụng eccouncil.org).
>
> ![Screenshot](media/image5.jpeg){width="10.6625in" height="8.0in"}

9.  Từ ảnh chụp màn hình ở trên, chúng tôi có thể thu thập thông tin như DNS, MX, SPF, DMARC, DKIM, v.v.

10. Bây giờ, chúng ta sẽ thực hiện liệt kê người dùng trong Azure AD, trong cửa sổ PowerShell, nhập Invoke-AADintUserEnumerationAsOutsider -UserName user@company.com rồi nhấn Enter.

> Trong lệnh trên, thay thế user@company.com bằng địa chỉ email của người dùng mục tiêu.
>
> ![aad1.jpg](media/image6.jpeg){width="10.6625in" height="8.0in"}

11. Chúng ta có thể thấy rằng kết quả xuất hiện, Đúng trong trường Tồn tại ngụ ý rằng tài khoản Azure có tên người dùng đã cho tồn tại và kẻ tấn công có thể thực hiện các cuộc tấn công tiếp theo.

12. Chúng tôi cũng có thể thực hiện việc liệt kê người dùng bằng cách đặt tên người dùng vào tệp văn bản, bằng cách chạy Get-Content .\\users.txt \| Gọi-AADIntUserEnumerationAsOutsider -Phương thức bình thường. Trong đó tệp user.txt chứa địa chỉ email mục tiêu.

13. Bây giờ, để nhận thông tin đăng nhập cho loại miền Get-AADIntLoginInformation -Domain company.com và nhấn Enter.

> Trong lệnh trên, thay thế company.com bằng tên miền của công ty mục tiêu (ở đây, chúng tôi đang sử dụng eccouncil.org).
>
> ![Screenshot](media/image7.jpeg){width="10.6625in" height="8.0in"}

14. Bây giờ, để nhận thông tin đăng nhập cho người dùng, hãy nhập Get-AADIntLoginInformation -Domain user@company và nhấn Enter.

> Trong lệnh trên, thay thế user@company.com bằng địa chỉ email của người dùng mục tiêu.
>
> ![aad2.jpg](media/image8.jpeg){width="10.6625in" height="8.0in"}

15. Để lấy ID đối tượng thuê cho người dùng, miền hoặc Mã thông báo truy cập nhất định, hãy nhập Get-AADintTenantID -Domain company.com.

> Trong lệnh trên, thay thế company.com bằng tên miền của công ty mục tiêu (ở đây, chúng tôi đang sử dụng eccouncil.org).
>
> ![Screenshot](media/image9.jpeg){width="10.6625in" height="8.0in"}

16. Để nhận miền đã đăng ký từ người thuê miền đã cho Get-AADIntTenantDomains -Domain company.com

> Trong lệnh trên, thay thế company.com bằng tên miền của công ty mục tiêu (ở đây, chúng tôi đang sử dụng eccouncil.org).
>
> ![Screenshot](media/image10.jpeg){width="10.6625in" height="8.0in"}

17. Chúng ta có thể thấy rằng tất cả các miền được liên kết với đối tượng thuê sẽ được liệt kê.

18. Ngoài ra, bạn có thể truy cập trang web https://aadinternals.com/osint/ và nhập ID đối tượng thuê, tên miền hoặc email để nhận thông tin có sẵn công khai cho đối tượng thuê nhất định.

19. Khởi chạy trình duyệt Firefox và truy cập https://aadinternals.com/osint/ và nhập tên miền vào hộp tìm kiếm rồi nhấp vào nút Nhận thông tin.

> Ở đây chúng tôi đặt tên miền là eccouncil.org.

20. Chúng ta sẽ nhận được thông tin Domain và danh sách các miền kết nối với tên miền được cung cấp.

> ![Screenshot](media/image11.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image12.jpeg){width="10.6625in" height="8.0in"}

21. Theo cách tương tự, bạn có thể nhập ID đối tượng thuê và email vào trường tìm kiếm để xem thông tin liên quan đến đối tượng thuê và người dùng.

22. Điều này kết thúc phần trình diễn trinh sát Azure với AADInternals.

23. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 19.1.1.1**

Trên máy Windows 11, hãy sử dụng công cụ AADIntenals có tại E:\\CEH-Tools\\CEHv13 Module 19 Cloud Computing\\GitHub Tools\\ để thực hiện Trinh sát trên Azure AD. Trong khi thực hiện liệt kê người dùng trong Azure AD, trường Tồn tại sẽ hiển thị gì nếu người dùng tồn tại.

Lab 2: Khai thác nhóm S3

**Kịch bản bài lab**

Là một hacker có đạo đức chuyên nghiệp hoặc chuyên gia kiểm thử xâm nhập (pentester), bạn phải có kiến ​​thức vững chắc về việc liệt kê các nhóm S3. Bằng cách sử dụng nhiều kỹ thuật khác nhau, bạn có thể khai thác các cấu hình sai trong quá trình triển khai nhóm và vi phạm cơ chế bảo mật để xâm phạm quyền riêng tư của dữ liệu. Việc để phiên vùng lưu trữ S3 chạy cho phép bạn sửa đổi các tệp như JavaScript hoặc mã liên quan và đưa phần mềm độc hại vào các tệp vùng lưu trữ. Hơn nữa, việc tìm vị trí và tên của nhóm sẽ giúp bạn kiểm tra tính bảo mật của nhóm và xác định các lỗ hổng trong quá trình triển khai.

**Mục tiêu bài lab**

-   Khai thác các nhóm S3 mở bằng AWS CLI

**Tổng quan về nhóm S3**

Bộ chứa S3 được khách hàng và người dùng cuối sử dụng để lưu trữ tài liệu văn bản, PDF, video, hình ảnh, v.v. Để lưu trữ tất cả những dữ liệu này, người dùng cần tạo một bộ chứa có tên duy nhất.

Dưới đây là một số kỹ thuật có thể được áp dụng để xác định Bộ chứa AWS S3:

-   **Kiểm tra HTML: Phân tích mã nguồn của các trang web HTML ở chế độ nền để tìm URL tới nhóm S3 mục tiêu**

-   **URL cưỡng bức: Sử dụng Burp Suite để thực hiện tấn công bạo lực vào URL của nhóm mục tiêu nhằm xác định URL chính xác của nó**

-   **Tìm tên miền phụ: Sử dụng các công cụ như Findsubdomains và Robtex để xác định các tên miền phụ liên quan đến nhóm mục tiêu**

-   **Tìm kiếm IP ngược: Sử dụng các công cụ tìm kiếm như Bing để thực hiện tìm kiếm IP ngược nhằm xác định các miền của nhóm S3 mục tiêu**

-   **Hack nâng cao của Google: Sử dụng toán tử tìm kiếm nâng cao của Google như \"inurl\" để tìm kiếm các URL liên quan đến nhóm S3 mục tiêu**

Nhiệm vụ 1: Khai thác nhóm S3 mở bằng AWS CLI

Giao diện dòng lệnh AWS (CLI) là một công cụ hợp nhất để quản lý các dịch vụ AWS. Chỉ với một công cụ để tải xuống và đặt cấu hình, bạn có thể kiểm soát nhiều dịch vụ AWS từ dòng lệnh và tự động hóa chúng thông qua tập lệnh.

Trước khi bắt đầu tác vụ này, bạn phải tạo tài khoản AWS của mình (https://aws.amazon.com).

1.  Trong máy Bảo mật Parrot, hãy nhấp vào biểu tượng MATE Terminal trong menu để khởi chạy terminal / dòng lệnh.

2.  Cửa sổ Prot Terminal xuất hiện. Trong cửa sổ terminal, nhập sudo su và nhấn Enter để chạy các chương trình với tư cách là người dùng root cũng sử dụng hoặc làm mật khẩu.

> Mật khẩu bạn gõ sẽ không hiển thị.

3.  Bây giờ, hãy nhập cd và nhấn Enter để chuyển đến thư mục gốc.

> ![Screenshot](media/image13.jpeg){width="10.6625in" height="8.0in"}

4.  Trong cửa sổ terminal, nhập pip3 install awscli rồi nhấn Enter để cài đặt AWS CLI.

> ![Screenshot](media/image14.jpeg){width="10.6625in" height="8.0in"}

5.  Bây giờ, chúng ta cần định cấu hình AWS CLI. Để định cấu hình AWS CLI trong cửa sổ terminal, hãy nhập aws configure và nhấn Enter.

> ![Screenshot](media/image15.jpeg){width="10.6625in" height="8.0in"}

6.  Nó sẽ yêu cầu các chi tiết sau:

    -   ID khóa truy cập AWS

    -   Khóa truy cập bí mật AWS

    -   Tên vùng mặc định

    -   Định dạng đầu ra mặc định

7.  Để cung cấp những chi tiết này, bạn cần đăng nhập vào tài khoản AWS của mình.

8.  Nhấp vào biểu tượng Firefox từ phần trên cùng của Màn hình.

9.  Đăng nhập vào tài khoản AWS mà bạn đã tạo khi bắt đầu nhiệm vụ này. Nhấp vào biểu tượng trình duyệt Firefox trong menu, nhập https://console.aws.amazon.com vào thanh địa chỉ và nhấn Enter.

> Nếu bạn chưa có tài khoản AWS, hãy tạo một tài khoản bằng Gói miễn phí cơ bản, sau đó tiến hành các tác vụ.

10. Trang Đăng nhập Dịch vụ web của Amazon xuất hiện; nhập tài khoản email của bạn vào trường địa chỉ email của người dùng gốc và nhấp vào Tiếp theo.

> ![10.jpg](media/image16.jpeg){width="10.6625in" height="8.0in"}

11. Nhập mật khẩu tài khoản AWS của bạn vào trường Mật khẩu và nhấp vào Đăng nhập.

> Nếu cửa sổ Kiểm tra bảo mật xuất hiện, hãy nhập hình ảnh xác thực và nhấp vào Gửi.
>
> ![11.jpg](media/image17.jpeg){width="10.6625in" height="8.0in"}

12. Nhấp vào menu thả xuống tài khoản AWS và nhấp vào Thông tin xác thực bảo mật, như minh họa trong ảnh chụp màn hình.

> ![qw.jpg](media/image18.jpeg){width="10.6625in" height="8.0in"}

13. Cuộn xuống phần Khóa truy cập .

14. Nhấp vào nút Tạo khóa truy cập. Trong Tiếp tục tạo khóa truy cập?; chọn hộp kiểm và nhấp vào Tạo khóa truy cập.

> ![qswdfghj.jpg](media/image19.jpeg){width="10.6625in" height="8.0in"}
>
> ![14.2.jpg](media/image20.jpeg){width="10.6625in" height="8.0in"}

15. Sao chép Khóa truy cập và chuyển sang cửa sổ terminal / dòng lệnh.

> ![wsdfg.jpg](media/image21.jpeg){width="10.6625in" height="8.0in"}

16. Trong cửa sổ terminal, nhấp chuột phải vào; chọn Dán từ menu ngữ cảnh để dán ID khóa truy cập AWS đã sao chép và nhấn Enter. Nó sẽ nhắc bạn đến Khóa truy cập bí mật AWS. Chuyển sang Tài khoản AWS của bạn trong trình duyệt.

17. Sao chép Khóa truy cập bí mật và thu nhỏ cửa sổ trình duyệt. Chuyển sang cửa sổ terminal / dòng lệnh.

18. Trong cửa sổ terminal, hãy nhấp chuột phải vào, chọn Dán từ menu ngữ cảnh để dán Khóa truy cập bí mật đã sao chép và nhấn Enter. Nó sẽ nhắc bạn tên vùng mặc định.

19. Trong trường Tên khu vực mặc định, hãy nhập eu-west-1 và nhấn Enter.

20. Lời nhắc Định dạng đầu ra mặc định xuất hiện; hãy để mặc định và nhấn Enter.

> ![wsdc.jpg](media/image22.jpeg){width="10.6625in" height="8.0in"}

21. Nhằm mục đích minh họa, chúng tôi đã tạo một nhóm S3 mở có tên certifiedhacker02 trong dịch vụ AWS. Chúng ta sẽ sử dụng cái xô đó trong nhiệm vụ này.

> Bạn có thể tìm thấy nhóm S3 công khai trong giai đoạn liệt kê.

22. Hãy để chúng tôi liệt kê các thư mục trong nhóm Certifiedhacker02. Trong cửa sổ terminal, nhập aws s3 ls s3://\[Tên nhóm\] (ở đây, Tên nhóm là certifiedhacker02) rồi nhấn Enter.

> Tên nhóm có thể khác trong môi trường bài lab của bạn tùy thuộc vào nhóm bạn đang nhắm mục tiêu.

23. Thao tác này sẽ hiển thị cho bạn danh sách các thư mục trong nhóm certifiedhacker02 S3, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image23.jpeg){width="10.6625in" height="8.0in"}

24. Bây giờ, hãy phóng to cửa sổ trình duyệt, nhập certifiedhacker02.s3.amazonaws.com vào thanh địa chỉ và nhấn Enter.

25. Thao tác này sẽ hiển thị cho bạn danh sách đầy đủ các thư mục và tệp có sẵn trong nhóm này.

> ![Screenshot](media/image24.jpeg){width="10.6625in" height="8.0in"}

26. Thu nhỏ cửa sổ trình duyệt và chuyển sang terminal / dòng lệnh.

27. Hãy để chúng tôi di chuyển một số tệp vào nhóm Certifiedhacker02. Để thực hiện việc này, trong cửa sổ terminal, nhập echo \"Bạn đã bị hack\" \>\> Hack.txt và nhấn Enter.

28. Bằng cách đưa ra lệnh này, bạn đang tạo một tệp có tên Hack.txt.

> ![Screenshot](media/image25.jpeg){width="10.6625in" height="8.0in"}

29. Chúng ta hãy thử di chuyển tệp Hack.txt vào nhóm certifiedhacker02. Trong cửa sổ terminal, nhập aws s3 mv Hack.txt s3://certifiedhacker02 và nhấn Enter.

30. Bạn đã di chuyển thành công tệp Hack.txt vào nhóm certifiedhacker02.

> ![Screenshot](media/image26.jpeg){width="10.6625in" height="8.0in"}

31. Để xác minh xem tệp có bị di chuyển hay không, hãy chuyển sang cửa sổ trình duyệt và phóng to nó. Tải lại trang.

32. Bạn có thể quan sát thấy tệp Hack.txt được chuyển sang nhóm Certifiedhacker02, như minh họa trong ảnh chụp màn hình.

> ![Screenshot](media/image27.jpeg){width="10.6625in" height="8.0in"}

33. Thu nhỏ cửa sổ trình duyệt và chuyển sang cửa sổ terminal / dòng lệnh.

34. Hãy để chúng tôi xóa tệp Hack.txt khỏi nhóm certifiedhacker02. Trong cửa sổ terminal, nhập aws s3 rm s3://certifiedhacker02/Hack.txt rồi nhấn Enter.

35. Bằng cách ban hành lệnh này, bạn đã xóa thành công tệp Hack.txt khỏi nhóm certifiedhacker02.

> ![Screenshot](media/image28.jpeg){width="10.6625in" height="8.0in"}

36. Để xác minh xem tệp có bị xóa hay không, hãy chuyển sang cửa sổ trình duyệt và tải lại trang.

37. Tệp Hack.txt sẽ bị xóa khỏi nhóm certifiedhacker02.

> ![Screenshot](media/image29.jpeg){width="10.6625in" height="8.0in"}

38. Do đó, bạn có thể thêm hoặc xóa tệp khỏi nhóm S3 đang mở.

39. Điều này kết thúc phần trình diễn khai thác các nhóm S3 công cộng.

40. Đừng kết thúc bài thực hành vì chúng ta sẽ tiếp tục nó trong #Nhiệm vụ tiếp theo.

**Câu 19.2.1.1**

Sử dụng công cụ AWS CLI để khai thác các nhóm S3 mở (certifiedhacker02) trong dịch vụ AWS. Xác định lệnh liệt kê tổng số tệp có sẵn trong nhóm S3 \"certifiedhacker02\". Lưu ý: Bạn phải tạo tài khoản AWS (https://aws.amazon.com) để thực hiện tác vụ này. Nhập lệnh đã được sử dụng trong bài lab này để liệt kê nội dung của nhóm Certifiedhacker02.

Lab 3: Thực hiện nâng cao đặc quyền để đạt được đặc quyền cao hơn

**Kịch bản bài lab**

Là một hacker đạo đức chuyên nghiệp hoặc chuyên gia kiểm thử xâm nhập (pentester), bạn phải cố gắng nâng cao đặc quyền bằng cách sử dụng khóa truy cập tài khoản người dùng và khóa truy cập bí mật có được bằng cách sử dụng các kỹ thuật lừa đảo xã hội khác nhau. Trong quá trình leo thang đặc quyền, bạn cố gắng giành được quyền truy cập hoàn toàn vào tài khoản của người dùng IAM mục tiêu, sau đó cố gắng đạt được các đặc quyền cấp cao hơn trong môi trường AWS.

Trong nền tảng đám mây, do các lỗi trong hệ thống phân bổ quyền truy cập như lỗi mã hóa và lỗi thiết kế, khách hàng, bên thứ ba hoặc nhân viên có thể có được quyền truy cập cao hơn quyền truy cập mà họ được phép sử dụng. Mối đe dọa này phát sinh do các lỗ hổng xác thực, ủy quyền và trách nhiệm giải trình (AAA), lỗ hổng cấp phép và hủy cung cấp của người dùng, lỗ hổng ảo hóa, vai trò và trách nhiệm không rõ ràng, cấu hình sai, v.v.

Trong bài lab này, chúng tôi sẽ khai thác chính sách cấp phép người dùng bị định cấu hình sai để nâng cấp đặc quyền lên cấp quản trị viên.

**Mục tiêu bài lab**

-   Nâng cao đặc quyền của người dùng IAM bằng cách khai thác chính sách người dùng bị định cấu hình sai

**Tổng quan về nâng cao đặc quyền**

Đặc quyền là các vai trò bảo mật được chỉ định cho người dùng để sử dụng các chương trình, tính năng, hệ điều hành, chức năng, tệp, mã, v.v. cụ thể để hạn chế quyền truy cập tùy thuộc vào loại người dùng. Cần phải leo thang đặc quyền khi bạn muốn truy cập các tài nguyên hệ thống mà bạn không được phép truy cập. Nó diễn ra dưới hai hình thức: dọc và ngang.

-   **Nâng cao đặc quyền theo chiều ngang: Người dùng trái phép cố gắng truy cập tài nguyên, chức năng và các đặc quyền khác của người dùng được ủy quyền có quyền truy cập tương tự**

-   **Nâng cao đặc quyền theo chiều dọc: Người dùng trái phép cố gắng truy cập vào tài nguyên và chức năng của người dùng có đặc quyền cao hơn như quản trị viên ứng dụng hoặc trang web**

Nhiệm vụ 1: Nâng cao đặc quyền của người dùng IAM bằng cách khai thác Chính sách người dùng bị định cấu hình sai

Chính sách là một thực thể, khi được gắn vào danh tính hoặc tài nguyên, sẽ xác định các quyền của nó. Bạn có thể sử dụng Bảng điều khiển quản lý AWS, AWS CLI hoặc API AWS để tạo các chính sách do khách hàng quản lý trong IAM. Chính sách do khách hàng quản lý là các chính sách độc lập mà bạn quản lý trong tài khoản AWS của mình. Sau đó, bạn có thể đính kèm các chính sách vào danh tính (người dùng, nhóm và vai trò) trong tài khoản AWS của mình. Nếu chính sách người dùng không được định cấu hình đúng cách, kẻ tấn công có thể khai thác chúng để giành quyền truy cập quản trị viên đầy đủ vào tài khoản AWS của người dùng mục tiêu.

Bạn cần định cấu hình aws cli cho bài lab này, hãy tham khảo bài lab 2: Khai thác nhóm S3, Nhiệm vụ 1: Khai thác nhóm S3 mở bằng AWS CLI, Bước#1-20.

Trước khi bắt đầu tác vụ này, hãy tạo một người dùng IAM (Thử nghiệm) với các cài đặt mặc định và tạo một chính sách (Thử nghiệm) với các quyền bao gồm iam:AttachUserPolicy, iam:ListUserPolicies, sts:AssumeRole và iam:ListRoles, như hiển thị trong ảnh chụp màn hình bên dưới. Những chính sách này có thể bị kẻ tấn công khai thác để giành được các đặc quyền cấp quản trị viên.![iv9qiwy3.jpg](media/image30.jpeg){width="11.415277777777778in" height="5.285416666666666in"}

1.  Trong máy Bảo mật Parrot, hãy nhấp vào biểu tượng MATE Terminal trong menu để khởi chạy terminal / dòng lệnh.

2.  Cửa sổ Prot Terminal xuất hiện. Trong cửa sổ terminal, nhập sudo su và nhấn Enter để chạy các chương trình với tư cách là người dùng root và người dùng cũng như mật khẩu.

3.  Sau khi định cấu hình AWS CLI, chúng tôi tạo chính sách người dùng và đính kèm chính sách đó vào tài khoản người dùng IAM mục tiêu để nâng cấp đặc quyền.

4.  Trong cửa sổ terminal, nhập vim user-policy.json rồi nhấn Enter.

> Lệnh này sẽ tạo một tệp có tên chính sách người dùng trong thư mục kẻ tấn công.
>
> ![Screenshot](media/image31.jpeg){width="10.6625in" height="8.0in"}

5.  Trình soạn thảo văn bản dòng lệnh xuất hiện; nhấn I và nhập tập lệnh bên dưới:

> {
>
> KiểuSao chép
>
> \"Phiên bản\":2012-10-17\",
>
> \"Tuyên bố\": \[
>
> \"Hiệu ứng:\"Cho phép\",
>
> \"Hành động:\"\*\",
>
> \"Tài nguyên:\"\*\"
>
> }
>
> \]
>
> }
>
> Đây là chính sách AdministratorAccess cung cấp cho quản trị viên quyền truy cập vào người dùng IAM mục tiêu.
>
> Bỏ qua các ký hiệu \$ trong tập lệnh.

6.  Sau khi nhập tập lệnh được cung cấp ở bước trước, hãy nhấn nút Esc. Sau đó, nhập :wq! và nhấn Enter để lưu tài liệu văn bản.

> ![Screenshot](media/image32.jpeg){width="10.6625in" height="8.0in"}

7.  Bây giờ, chúng tôi sẽ đính kèm chính sách đã tạo (chính sách người dùng) vào tài khoản người dùng IAM mục tiêu. Để làm như vậy, hãy nhập aws iam create-policy \--policy-name user-policy \--policy-document file://user-policy.json và nhấn Enter.

> Nếu bạn nhận được lỗi rằng chính sách đã tồn tại, hãy đổi tên tệp và thử lại.

8.  Chính sách người dùng đã tạo sẽ hiển thị, hiển thị nhiều chi tiết khác nhau như PolicyName, PolicyId và Arn.

> ![qwdaasd.jpg](media/image33.jpeg){width="10.6625in" height="8.0in"}

9.  Trong terminal / dòng lệnh, nhập aws iam Attach-user-policy \--user-name \[Tên người dùng mục tiêu\] \--policy-arn arn:aws:iam::\[ID tài khoản\]:policy/user-policy và nhấn Enter.

10. Lệnh trên sẽ đính kèm chính sách (chính sách người dùng) vào tài khoản người dùng IAM mục tiêu (tại đây, kiểm tra).

> ![myubgfd.jpg](media/image34.jpeg){width="10.6625in" height="8.0in"}

11. Bây giờ, hãy nhập aws iam list-attached-user-policies \--user-name \[Tên người dùng mục tiêu\] và nhấn Enter để xem các chính sách đính kèm của người dùng mục tiêu (tại đây, kiểm tra).

12. Kết quả hiện ra, hiển thị tên chính sách đính kèm (chính sách người dùng), như trong ảnh chụp màn hình.

> ![sdvsvds.jpg](media/image35.jpeg){width="10.6625in" height="8.0in"}

13. Bây giờ bạn đã nâng cấp thành công các đặc quyền của tài khoản người dùng IAM mục tiêu, bạn có thể liệt kê tất cả người dùng IAM trong môi trường AWS. Để làm như vậy, hãy nhập aws iam list-users và nhấn Enter.

14. Kết quả hiện ra, hiển thị danh sách người dùng IAM như trong ảnh chụp màn hình.

> ![qwdqwdqwd.jpg](media/image36.jpeg){width="10.6625in" height="8.0in"}

15. Tương tự, bạn có thể sử dụng nhiều lệnh khác nhau để có được thông tin đầy đủ về môi trường AWS chẳng hạn như danh sách nhóm S3, chính sách người dùng, chính sách vai trò và chính sách nhóm cũng như để tạo người dùng mới.

    -   Danh sách nhóm S3: aws s3api list-buckets \--query \"Buckets\[\].Name\"

    -   Chính sách người dùng: aws iam list-user-policies

    -   Chính sách vai trò: aws iam list-role-policies

    -   Chính sách nhóm: aws iam list-group-policies

    -   Tạo người dùng: aws iam create-user

16. Phần này kết thúc minh họa về việc tăng đặc quyền của người dùng IAM bằng cách khai thác chính sách người dùng bị định cấu hình sai.

17. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 19.3.1.1**

Nâng cao đặc quyền của người dùng IAM bằng cách khai thác chính sách người dùng bị định cấu hình sai. Lệnh aws nào sẽ liệt kê tất cả chính sách người dùng?

Lab 4: Thực hiện đánh giá lỗ hổng trên Docker Images

**Kịch bản bài lab**

Là một hacker có đạo đức chuyên nghiệp hoặc chuyên gia kiểm thử xâm nhập (pentester), chuyên môn về đánh giá lỗ hổng của Docker là rất quan trọng. Bằng cách tận dụng các công cụ như Trivy, bạn có thể phân tích hình ảnh Docker, xác định và khai thác các lỗ hổng. Quét tích cực và kiểm tra thủ công sẽ phát hiện các cấu hình yếu, cho phép bạn vi phạm bảo mật và cấy mã độc, đồng thời hiểu rõ vị trí hình ảnh sẽ hỗ trợ kiểm tra và giảm thiểu bảo mật toàn diện.

**Mục tiêu bài lab**

-   Đánh giá lỗ hổng trên hình ảnh Docker bằng Trivy

**Tổng quan về Docker Images**

Hình ảnh Docker là các gói nhẹ, độc lập, có thể thực thi được, chứa mọi thứ cần thiết để chạy một ứng dụng phần mềm, bao gồm mã, thời gian chạy, thư viện và phần phụ thuộc. Chúng cho phép triển khai nhất quán trên nhiều môi trường khác nhau, đơn giản hóa việc phân phối phần mềm, đồng thời hỗ trợ khả năng mở rộng và tái tạo trong môi trường được đóng gói.

Nhiệm vụ 1: Đánh giá lỗ hổng trên Docker Images bằng Trivy

Trivy là một trình quét bảo mật mạnh mẽ giúp phát hiện các lỗ hổng và cấu hình sai trên nhiều mục tiêu, bao gồm hình ảnh vùng chứa, hệ thống tệp, kho lưu trữ Git, hình ảnh máy ảo, Kubernetes và AWS. Với các trình quét toàn diện, Trivy xác định các lỗ hổng gói hệ điều hành, thông tin nhạy cảm, sự cố IaC, v.v., cung cấp giải pháp bảo mật mạnh mẽ cho cơ sở hạ tầng của bạn.

1.  Trong máy Bảo mật Parrot, hãy nhấp vào biểu tượng MATE Terminal trong menu để khởi chạy terminal / dòng lệnh.

2.  Cửa sổ Prot Terminal xuất hiện. Trong cửa sổ terminal, nhập sudo su và nhấn Enter để chạy các chương trình với tư cách là người dùng root.

3.  Trong trường \[sudo\] mật khẩu dành cho kẻ tấn công, hãy nhập toor làm mật khẩu và nhấn Enter.

> Mật khẩu bạn gõ sẽ không hiển thị.
>
> Thu nhỏ terminal / dòng lệnh để có cái nhìn rõ hơn về đầu ra
>
> ![Screenshot](media/image37.jpeg){width="10.6625in" height="8.0in"}

4.  Trong bài lab này, chúng tôi sẽ quét hai hình ảnh docker, đầu tiên là hình ảnh an toàn và thứ hai là hình ảnh dễ bị tấn công.

5.  Thực thi lệnh docker pull ubuntu để cài đặt hình ảnh docker đầu tiên.

> ![Screenshot](media/image38.jpeg){width="10.6625in" height="8.0in"}

6.  Sau khi hình ảnh được kéo, chúng tôi sẽ thực hiện đánh giá lỗ hổng. Thực thi lệnh hình ảnh tầm thường trên Ubuntu.

> ![Screenshot](media/image39.jpeg){width="10.6625in" height="8.0in"}

7.  Trong ảnh chụp màn hình ở trên, chúng ta có thể nhận thấy rằng chúng ta có hoàn toàn 0 lỗ hổng và nó hoàn toàn an toàn.

8.  Bây giờ, chúng ta sẽ phân tích hình ảnh lỗ hổng. thực thi lệnh docker pull nginx:1.19.6 để kéo hình ảnh dễ bị tấn công.

> ![Screenshot](media/image40.jpeg){width="10.6625in" height="8.0in"}

9.  Thực thi lệnh trivy image nginx:1.19.6 để quét hình ảnh.

> ![Screenshot](media/image41.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image42.jpeg){width="10.6625in" height="8.0in"}
>
> ![Screenshot](media/image43.jpeg){width="10.6625in" height="8.0in"}

10. Trong ảnh chụp màn hình ở trên, chúng ta có thể thấy rằng chúng ta có tổng cộng 401 lỗ hổng cũng được phân loại cùng với các CVE đã đề cập.

11. Điều này kết thúc phần minh họa đánh giá lỗ hổng trên hình ảnh docker bằng Trivy

12. Đóng tất cả các cửa sổ đang mở và ghi lại tất cả thông tin thu được.

**Câu 19.4.1.1**

Trong máy Parrot, cài đặt các hình ảnh Ubuntu và nginx:1.19.6 và quét bằng trình quét bảo mật tầm thường. Nhập mức độ nghiêm trọng có thể quan sát được đối với lỗ hổng bsdutils của hình ảnh docker nginx:1.19.6.

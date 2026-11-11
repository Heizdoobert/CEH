**Chương 8: An Ninh Mạng Máy Tính (Security in Computer Networks)**

Ngay từ Phần 1.6, chúng tôi đã mô tả một số lớp tấn công Internet phổ biến và gây hại nhất, bao gồm tấn công phần mềm độc hại, từ chối dịch vụ, nghe lén, giả mạo nguồn và sửa đổi và xóa tin nhắn. Mặc dù kể từ đó chúng ta đã học được rất nhiều về mạng máy tính, chúng ta vẫn chưa xem xét cách bảo vệ mạng trước những cuộc tấn công đó. Với kiến thức mới có được về mạng máy tính và giao thức Internet, chúng ta sẽ nghiên cứu kỹ hơn về giao tiếp an toàn và, cụ thể, cách mạng máy tính có thể được bảo vệ khỏi những kẻ xấu đáng ghét đó.

Hãy để chúng tôi giới thiệu Alice và Bob, hai người muốn giao tiếp và mong muốn làm như vậy một cách "an toàn." Vì đây là một văn bản về mạng, chúng ta nên lưu ý rằng Alice và Bob có thể là hai bộ định tuyến muốn trao đổi bảng định tuyến một cách an toàn, một máy khách và máy chủ muốn thiết lập kết nối truyền tải an toàn, hoặc hai ứng dụng e-mail muốn trao đổi e-mail an toàn---tất cả các trường hợp này sẽ được xem xét sau trong chương này. Alice và Bob là những nhân vật nổi tiếng trong cộng đồng an ninh, có lẽ vì tên của họ thú vị hơn so với một thực thể chung chung được gọi là "A" muốn giao tiếp an toàn với một thực thể chung chung được gọi là "B." Các mối tình, giao tiếp thời chiến và các giao dịch kinh doanh là những nhu cầu con người thường được nhắc đến về giao tiếp an toàn; ưu tiên trường hợp đầu tiên so với hai trường hợp sau, chúng tôi rất vui khi sử dụng Alice và Bob làm người gửi và người nhận, và tưởng tượng họ trong kịch bản đầu tiên này.

Chúng ta đã nói rằng Alice và Bob muốn giao tiếp và mong muốn thực hiện điều đó một cách "an toàn," nhưng chính xác thì điều này có nghĩa là gì? Như chúng ta sẽ thấy, an ninh (giống như tình yêu) là một thứ nhiều vẻ đẹp; tức là, có nhiều khía cạnh của an ninh. Chắc chắn, Alice và Bob sẽ muốn nội dung giao tiếp của họ giữ bí mật khỏi một kẻ nghe trộm. Họ có lẽ cũng muốn đảm bảo rằng khi họ

**An ninh trong Mạng Máy tính**

**CHƯƠNG**

![](media/image1.png){width="5.5in" height="6.930965660542432in"}

![](media/image2.png){width="5.5in" height="0.9567311898512686in"}

Giao tiếp, họ thực sự đang giao tiếp với nhau, và nếu việc giao tiếp của họ bị một kẻ nghe lén can thiệp, thì sự can thiệp này sẽ được phát hiện. Trong phần đầu của chương này, chúng ta sẽ đề cập đến các kỹ thuật mật mã cơ bản cho phép mã hóa giao tiếp, xác thực bên mà người ta đang giao tiếp, và đảm bảo tính toàn vẹn của tin nhắn.

Trong phần thứ hai của chương này, chúng ta sẽ xem xét cách các nguyên tắc cơ bản của mật mã học có thể được sử dụng để tạo ra các giao thức mạng an toàn. Một lần nữa, với cách tiếp cận từ trên xuống, chúng ta sẽ xem xét các giao thức an toàn ở mỗi (bốn lớp hàng đầu), bắt đầu từ lớp ứng dụng. Chúng ta sẽ xem xét cách bảo mật e-mail, cách bảo mật một kết nối TCP, cách cung cấp an ninh tổng thể ở lớp mạng, và cách bảo mật một mạng LAN không dây. Trong phần thứ ba của chương này, chúng ta sẽ xem xét bảo mật vận hành, liên quan đến việc bảo vệ các mạng của tổ chức khỏi các cuộc tấn công. Cụ thể, chúng ta sẽ xem xét kỹ lưỡng cách các tường lửa và hệ thống phát hiện xâm nhập có thể tăng cường bảo mật cho mạng của tổ chức.

**8.1 An ninh mạng là gì?**

Hãy bắt đầu việc nghiên cứu bảo mật mạng của chúng ta bằng cách trở lại với những người yêu nhau, Alice và Bob, những người muốn giao tiếp "một cách an toàn." Điều này chính xác có nghĩa là gì? Chắc chắn, Alice chỉ muốn Bob là người duy nhất có thể hiểu được thông điệp mà cô ấy đã gửi, mặc dù họ đang giao tiếp qua một phương tiện không an toàn, nơi một kẻ xâm nhập (Trudy, kẻ xâm nhập) có thể chặn bất cứ thứ gì được truyền từ Alice đến Bob. Bob cũng muốn chắc chắn rằng thông điệp mà anh nhận được từ Alice thực sự được gửi bởi Alice, và Alice muốn đảm bảo rằng người mà cô ấy đang giao tiếp thực sự là Bob. Alice và Bob cũng muốn chắc chắn rằng nội dung của các thông điệp của họ không bị thay đổi trong quá trình truyền. Họ cũng muốn được đảm bảo rằng họ có thể giao tiếp ngay từ đầu (tức là không ai từ chối cho họ quyền truy cập vào các tài nguyên cần thiết để giao tiếp). Dựa trên những cân nhắc này, chúng ta có thể xác định các đặc tính mong muốn của giao tiếp an toàn.

• Bảo mật. Chỉ người gửi và người nhận dự kiến mới có thể hiểu nội dung của tin nhắn được truyền. Vì kẻ nghe trộm có thể chặn thông điệp, điều này tất yếu đòi hỏi tin nhắn phải được mã hóa theo cách nào đó để một tin nhắn bị chặn không thể bị kẻ chặn hiểu được. Khía cạnh bảo mật này có lẽ là ý nghĩa thường được nhận thức nhất của thuật ngữ giao tiếp an toàn. Chúng ta sẽ nghiên cứu các kỹ thuật mật mã để mã hóa và giải mã dữ liệu trong Mục 8.2. • Tính toàn vẹn của tin nhắn. Alice và Bob muốn đảm bảo rằng nội dung liên lạc của họ không bị thay đổi, dù là cố ý hay vô tình, trong quá trình truyền. Các mở rộng đối với các kỹ thuật kiểm tra tổng mà chúng ta đã gặp trong truyền tải tin cậy

and data link protocols can be used to provide such message integrity. We will study message integrity in Section 8.3. • End-point authentication. Both the sender and receiver should be able to confirm the identity of the other party involved in the communication---to confirm that the other party is indeed who or what they claim to be. Face-to-face human communication solves this problem easily by visual recognition. When communicating entities exchange messages over a medium where they cannot see the other party, authentication is not so simple. When a user wants to access an inbox, how does the mail server verify that the user is the person he or she claims to be? We study end-point authentication in Section 8.4. • Operational security. Almost all organizations (companies, universities, and so on) today have networks that are attached to the public Internet. These networks therefore can potentially be compromised. Attackers can attempt to deposit worms into the hosts in the network, obtain corporate secrets, map the internal network configurations, and launch DoS attacks. We'll see in Section 8.9 that operational devices such as firewalls and intrusion detection systems are used to counter attacks against an organization's network. A firewall sits between the organization's network and the public network, controlling packet access to and from the network. An intrusion detection system performs "deep packet inspection," alerting the network administrators about suspicious activity.

Sau khi đã xác định rõ chúng ta hiểu thế nào về bảo mật mạng, hãy cùng xem xét chính xác những thông tin mà một kẻ xâm nhập có thể truy cập được và những hành động mà kẻ xâm nhập có thể thực hiện. Hình 8.1 minh họa kịch bản này. Alice, người gửi, muốn gửi dữ liệu cho Bob, người nhận. Để trao đổi dữ liệu một cách an toàn, đồng thời đáp ứng các yêu cầu về tính bảo mật, xác thực điểm cuối và toàn vẹn thông điệp, Alice và Bob sẽ trao đổi các thông điệp điều khiển và thông điệp dữ liệu (theo cách tương tự mà các người gửi và người nhận TCP trao đổi các phân đoạn điều khiển và các phân đoạn dữ liệu).

Người gửi an toàn

Alice

Trudy

Kênh

Điều khiển, tin nhắn dữ liệu

Người nhận an toàn

Bob

Dữ liệu Dữ liệu

*Hình 8.1 ♦ Người gửi, người nhận và kẻ xâm nhập (Alice, Bob và Trudy)*

Tất cả hoặc một số các tin nhắn này thường sẽ được mã hóa. Như đã thảo luận trong Mục 1.6, một kẻ xâm nhập có thể thực hiện

• nghe lén---ngửi và ghi lại các tin nhắn điều khiển và dữ liệu trên kênh. • sửa đổi, chèn hoặc xóa các tin nhắn hoặc nội dung tin nhắn.

Như chúng ta sẽ thấy, trừ khi các biện pháp đối phó thích hợp được thực hiện, những khả năng này cho phép kẻ xâm nhập tiến hành nhiều loại tấn công an ninh khác nhau: theo dõi giao tiếp (có thể đánh cắp mật khẩu và dữ liệu), giả mạo một thực thể khác, chiếm đoạt phiên làm việc đang diễn ra, từ chối dịch vụ đối với người dùng mạng hợp pháp bằng cách làm quá tải tài nguyên hệ thống, v.v. Một bản tóm tắt về các cuộc tấn công đã được báo cáo được duy trì tại Trung tâm Điều phối CERT \[CERT 2020\].

Having established that there are indeed real threats loose in the Internet, what are the Internet equivalents of Alice and Bob, our friends who need to communicate securely? Certainly, Bob and Alice might be human users at two end systems, for example, a real Alice and a real Bob who really do want to exchange secure e-mail. They might also be participants in an electronic commerce transaction. For example, a real Bob might want to transfer his credit card number securely to a Web server to purchase an item online. Similarly, a real Alice might want to interact with her bank online. The parties needing secure communication might themselves also be part of the network infrastructure. Recall that the domain name system (DNS, see Section 2.4) or routing daemons that exchange routing information (see Chapter 5) require secure communication between two parties. The same is true for network management applications, a topic we examined in Chapter 5). An intruder that could actively interfere with DNS lookups (as discussed in Section 2.4), routing computations (Sections 5.3 and 5.4), or network management functions (Sections 5.5 and 5.7) could wreak havoc in the Internet.

Sau khi đã thiết lập khung, một số định nghĩa quan trọng nhất, và nhu cầu về bảo mật mạng, hãy cùng chuyển sang tìm hiểu mật mã học. Trong khi việc sử dụng mật mã học để cung cấp tính bảo mật là hiển nhiên, chúng ta sẽ sớm thấy rằng nó cũng là trung tâm để cung cấp xác thực điểm cuối và tính toàn vẹn của thông điệp---làm cho mật mã học trở thành nền tảng của bảo mật mạng.

**8.2 Nguyên tắc của Mật mã học**

Mặc dù mật mã học có một lịch sử lâu dài ít nhất từ thời Julius Caesar, các kỹ thuật mật mã hiện đại, bao gồm nhiều kỹ thuật được sử dụng trên Internet, dựa trên những tiến bộ đạt được trong 30 năm qua. Cuốn sách của Kahn, The Codebreakers \[Kahn 1967\], và cuốn sách của Singh, The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography \[Singh 1999\], cung cấp một cái nhìn đầy hấp dẫn về

lịch sử dài của mật mã học. Một cuộc thảo luận đầy đủ về chính mật mã học đòi hỏi một cuốn sách hoàn chỉnh \[Bishop 2003; Kaufman 2002; Schneier 2015\], vì vậy chúng tôi chỉ đề cập tới những khía cạnh thiết yếu của mật mã học, đặc biệt là khi chúng được áp dụng trên Internet. Chúng tôi cũng lưu ý rằng mặc dù trọng tâm của phần này sẽ là việc sử dụng mật mã học để đảm bảo tính bí mật, nhưng chúng ta sẽ thấy ngay rằng các kỹ thuật mật mã học gắn chặt với xác thực, toàn vẹn thông điệp, chống chối bỏ, và nhiều hơn nữa.

Các kỹ thuật mật mã cho phép người gửi che giấu dữ liệu sao cho kẻ xâm nhập không thể thu thập được thông tin gì từ dữ liệu bị chặn. Tất nhiên, người nhận phải có khả năng khôi phục dữ liệu gốc từ dữ liệu đã được che giấu. Hình 8.2 minh họa một số thuật ngữ quan trọng.

Giả sử bây giờ Alice muốn gửi một tin nhắn cho Bob. Tin nhắn của Alice ở dạng gốc của nó (ví dụ: "Bob, I love you. Alice") được gọi là bản rõ (plaintext), hoặc bản minh bạch (cleartext). Alice mã hóa tin nhắn bản rõ của mình bằng một thuật toán mã hóa để tin nhắn đã mã hóa, được gọi là bản mật (ciphertext), trông không thể hiểu được đối với bất kỳ kẻ xâm nhập nào. Thú vị thay, trong nhiều hệ thống mật mã hiện đại, bao gồm cả các hệ thống được sử dụng trên Internet, kỹ thuật mã hóa tự nó là điều đã biết --- được công bố, chuẩn hóa và có sẵn cho mọi người (ví dụ: \[RFC 1321; RFC 3447; RFC 2420; NIST 2001\]), kể cả kẻ xâm nhập tiềm năng! Rõ ràng, nếu ai cũng biết phương pháp mã hóa dữ liệu, thì phải có một số thông tin bí mật ngăn kẻ xâm nhập giải mã dữ liệu được truyền đi. Đây chính là vai trò của các khóa.

Trong Hình 8.2, Alice cung cấp một khóa, KA, một chuỗi các con số hoặc ký tự, làm đầu vào cho thuật toán mã hóa. Thuật toán mã hóa nhận khóa và thông điệp bản rõ, m, làm đầu vào và tạo ra bản mã làm đầu ra. Ký hiệu KA(m) ám chỉ dạng bản mã (được mã hóa sử dụng khóa KA) của thông điệp bản rõ, m. Thuật toán mã hóa thực sự sử dụng khóa KA sẽ hiển nhiên từ ngữ cảnh. Tương tự, Bob sẽ cung cấp một khóa, KB, cho thuật toán giải mã.

*Hình 8.2 ♦ Các thành phần mật mã*

Mã hóa

thuật toán

Bản mã

Kênh

Trudy

Alice Bob

Giải mã

thuật toán

Văn bản thuần

Chìa khóa:

Chìa khóa

Văn bản thuần

KA

KB

đó nhận bản mã và khóa của Bob làm đầu vào và tạo ra bản rõ gốc làm đầu ra. Điều đó có nghĩa là, nếu Bob nhận được một tin nhắn mã hóa KA(m), anh ta giải mã nó bằng cách tính KB(KA(m)) = m. Trong các hệ thống khóa đối xứng, khóa của Alice và Bob giống nhau và là bí mật. Trong các hệ thống khóa công khai, một cặp khóa được sử dụng. Một trong các khóa được cả Bob và Alice biết (thực ra, nó được cả thế giới biết). Khóa còn lại chỉ được biết bởi Bob hoặc Alice (nhưng không phải cả hai). Trong hai phần tiếp theo, chúng ta xem xét chi tiết hơn các hệ thống khóa đối xứng và khóa công khai.

**8.2.1 Mã hóa khóa đối xứng**

Tất cả các thuật toán mật mã đều liên quan đến việc thay thế một thứ này bằng một thứ khác, ví dụ, lấy một đoạn văn bản rõ và sau đó tính toán và thay thế bằng bản mã thích hợp để tạo ra thông điệp được mã hóa. Trước khi nghiên cứu một hệ thống mật mã hiện đại dựa trên khóa, trước tiên chúng ta hãy làm quen bằng cách nghiên cứu một thuật toán khóa đối xứng rất cũ, rất đơn giản được gán cho Julius Caesar, được biết đến với tên gọi mật mã Caesar (một mật mã là một phương pháp để mã hóa dữ liệu).

Đối với văn bản tiếng Anh, mật mã Caesar hoạt động bằng cách lấy từng chữ cái trong thông điệp gốc và thay thế bằng chữ cái cách k chữ cái sau đó (cho phép quay vòng; tức là, chữ cái z sẽ được theo sau bởi chữ cái a) trong bảng chữ cái. Ví dụ, nếu k = 3, thì chữ cái a trong văn bản gốc trở thành d trong văn bản mã; b trong văn bản gốc trở thành e trong văn bản mã, và cứ tiếp tục như vậy. Ở đây, giá trị k đóng vai trò là khóa. Ví dụ, thông điệp gốc "bob, i love you. Alice" trở thành "ere, l oryh brx. dolfh" trong văn bản mã. Mặc dù văn bản mã thực sự trông giống như chữ vô nghĩa, nhưng sẽ không mất nhiều thời gian để phá mã nếu bạn biết rằng mật mã Caesar đang được sử dụng, vì chỉ có 25 giá trị khóa có thể.

Một cải tiến so với mã Caesar là mã đơn chữ cái, cũng thay thế một chữ cái trong bảng chữ cái bằng một chữ cái khác trong bảng chữ cái. Tuy nhiên, thay vì thay thế theo một mẫu đều đặn (ví dụ, thay thế với một độ lệch k cho tất cả các chữ cái), bất kỳ chữ cái nào cũng có thể được thay thế bằng bất kỳ chữ cái nào khác, miễn là mỗi chữ cái có một chữ cái thay thế duy nhất, và ngược lại. Quy tắc thay thế trong Hình 8.3 cho thấy một một quy tắc có thể dùng để mã hóa văn bản gốc.

Thông điệp văn bản thuần "bob, i love you. Alice" trở thành "nkn, s gktc wky. Mgsbc." Do đó, giống như trường hợp của mã Caesar, điều này trông như tiếng lóng. Một mã đơn bảng chữ cái cũng sẽ có vẻ tốt hơn mã Caesar ở chỗ có 26! (theo cấp số 1026) cặp chữ cái có thể thay vì chỉ 25 cặp có thể. Một phương pháp thử tất cả (brute-force) một cách toàn diện với tất cả 1026 cặp có thể

*Hình 8.3 ♦ Một mật mã đơn chữ cái*

Chữ cái bản rõ: a b c d e f g h i j k l m n o p q r s t u v w x y z\
Chữ cái mật mã: m n b v c x z a s d f g h j k l p o i u y t r e w q

would require far too much work to be a feasible way of breaking the encryption algorithm and decoding the message. However, by statistical analysis of the plaintext language, for example, knowing that the letters e and t are the most frequently occurring letters in typical English text (accounting for 13 percent and 9 percent of letter occurrences), and knowing that particular two-and three-letter occurrences of letters appear quite often together (for example, "in," "it," "the," "ion," "ing," and so forth) make it relatively easy to break this code. If the intruder has some knowledge about the possible contents of the message, then it is even easier to break the code. For example, if Trudy the intruder is Bob's wife and suspects Bob of having an affair with Alice, then she might suspect that the names "bob" and "alice" appear in the text. If Trudy knew for certain that those two names appeared in the ciphertext and had a copy of the example ciphertext message above, then she could immediately determine seven of the 26 letter pairings, requiring 109 fewer possibilities to be checked by a brute-force method. Indeed, if Trudy suspected Bob of having an affair, she might well expect to find some other choice words in the message as well.

Khi xem xét mức độ dễ dàng mà Trudy có thể phá vỡ sơ đồ mã hóa của Bob và Alice, người ta có thể phân biệt ba kịch bản khác nhau, tùy thuộc vào thông tin mà kẻ xâm nhập có.

• Ciphertext-only attack. In some cases, the intruder may have access only to the intercepted ciphertext, with no certain information about the contents of the plaintext message. We have seen how statistical analysis can help in a ciphertext-only attack on an encryption scheme. • Known-plaintext attack. We saw above that if Trudy somehow knew for sure that "bob" and "alice" appeared in the ciphertext message, then she could have determined the (plaintext, ciphertext) pairings for the letters a, l, i, c, e, b, and o. Trudy might also have been fortunate enough to have recorded all of the ciphertext transmissions and then found Bob's own decrypted version of one of the transmissions scribbled on a piece of paper. When an intruder knows some of the (plaintext, ciphertext) pairings, we refer to this as a known-plaintext attack on the encryption scheme. • Chosen-plaintext attack. In a chosen-plaintext attack, the intruder is able to choose the plaintext message and obtain its corresponding ciphertext form. For the simple encryption algorithms we've seen so far, if Trudy could get Alice to send the message, "The quick brown fox jumps over the lazy dog," she could completely break the encryption scheme. We'll see shortly that for more sophisticated encryption techniques, a chosen-plaintext attack does not necessarily mean that the encryption technique can be broken.

Năm trăm năm trước, các kỹ thuật cải tiến mã hóa đơn chữ cái, được gọi là mã hóa đa chữ cái, đã được phát minh. Ý tưởng đằng sau mã hóa đa chữ cái là sử dụng nhiều mã hóa đơn chữ cái, với một cách cụ thể

monoalphabetic cipher to encode a letter in a specific position in the plaintext message. Thus, the same letter, appearing in different positions in the plaintext message, might be encoded differently. An example of a polyalphabetic encryption scheme is shown in Figure 8.4. It has two Caesar ciphers (with k = 5 and k = 19), shown as rows. We might choose to use these two Caesar ciphers, C1 and C2, in the repeating pattern C1, C2, C2, C1, C2. That is, the first letter of plaintext is to be encoded using C1, the second and third using C2, the fourth using C1, and the fifth using C2. The pattern then repeats, with the sixth letter being encoded using C1, the seventh with C2, and so on. The plaintext message "bob, i love you." is thus encrypted "ghu, n etox dhz." Note that the first b in the plaintext message is encrypted using C1, while the second b is encrypted using C2. In this example, the encryption and decryption "key" is the knowledge of the two Caesar keys (k = 5, k = 19) and the pattern C1, C2, C2, C1, C2.

Mã khối

Bây giờ chúng ta hãy tiến tới thời hiện đại và xem xét cách mã hóa khóa đối xứng được thực hiện ngày nay. Chúng ta tập trung vào các chữ mã khối, được sử dụng trong nhiều giao thức Internet bảo mật, bao gồm PGP (cho e-mail bảo mật), TLS (cho việc bảo mật các kết nối TCP), và IPsec (cho việc bảo mật truyền tải ở lớp mạng).

Trong một thuật toán mã hóa khối, thông điệp cần được mã hóa được xử lý theo các khối có kích thước k bit. Ví dụ, nếu k = 64, thì thông điệp sẽ được chia thành các khối 64 bit, và mỗi khối được mã hóa riêng biệt. Để mã hóa một khối, cipher sử dụng một ánh xạ một-một để ánh xạ khối k bit của bản rõ sang khối k bit của bản mã. Hãy cùng xem một ví dụ. Giả sử k = 3, do đó mã hóa khối ánh xạ các đầu vào 3 bit (bản rõ) sang các đầu ra 3 bit (bản mã). Một ánh xạ khả thi được đưa ra trong Bảng 8.1. Lưu ý rằng đây là một ánh xạ một-một; tức là, mỗi đầu vào có một đầu ra khác nhau. Thuật toán mã hóa khối này chia thông điệp thành các khối 3 bit và mã hóa mỗi khối theo ánh xạ trên. Bạn nên xác minh rằng thông điệp 010110001111 được mã hóa thành 101000111001.

Tiếp tục với ví dụ về khối 3-bit này, lưu ý rằng ánh xạ trong Bảng 8.1 chỉ là một ánh xạ trong số nhiều ánh xạ có thể. Có bao nhiêu ánh xạ có thể? Để trả lời câu hỏi này, hãy quan sát rằng một ánh xạ không gì khác hơn là một hoán vị của tất cả các đầu vào có thể. Có 2\^3 (= 8) đầu vào có thể (liệt kê dưới

*Hình 8.4 ♦ Một mật mã đa bảng chữ cái sử dụng hai mật mã Caesar*

Chữ thường: a b c d e f g h i j k l m n o p q r s t u v w x y z C1(k = 5): C2(k = 19):

f g h i j k l m n o p q r s t u v w x y z a b c d e t u v w x y z a b c d e f g h i j k l m n o p q r s

các cột đầu vào). Tám đầu vào này có thể được hoán vị theo 8! = 40.320 cách khác nhau. Vì mỗi hoán vị này xác định một ánh xạ, nên có 40.320 ánh xạ có thể. Chúng ta có thể xem mỗi ánh xạ này như một khóa---nếu Alice và Bob đều biết ánh xạ (khóa), họ có thể mã hóa và giải mã các tin nhắn được gửi giữa họ.

Cuộc tấn công bằng phương pháp brute-force đối với mật mã này là cố gắng giải mã văn bản mật bằng cách sử dụng tất cả các ánh xạ. Với chỉ 40.320 ánh xạ (khi k = 3), điều này có thể nhanh chóng được thực hiện trên một máy tính để bàn. Để ngăn chặn các cuộc tấn công brute-force, các mật mã khối thường sử dụng các khối lớn hơn nhiều, bao gồm k = 64 bit hoặc thậm chí lớn hơn. Lưu ý rằng số lượng ánh xạ có thể có đối với một mật mã khối k chung là 2k!, điều này là cực kỳ lớn ngay cả với các giá trị vừa phải của k (chẳng hạn như k = 64).

Mặc dù các mật mã khối đầy đủ bảng, như vừa được mô tả, với các giá trị trung bình của k có thể tạo ra các sơ đồ mã hóa khóa đối xứng mạnh mẽ, nhưng thật không may là chúng khó thực hiện. Với k = 64 và với một ánh xạ xác định, Alice và Bob sẽ cần phải duy trì một bảng với 2\^64 giá trị đầu vào, điều này là không khả thi. Hơn nữa, nếu Alice và Bob thay đổi khóa, họ sẽ phải mỗi người tái tạo bảng. Do đó, một mật mã khối đầy đủ bảng, cung cấp các ánh xạ định trước giữa tất cả các đầu vào và đầu ra (như trong ví dụ trên), đơn giản là không khả thi.

Instead, block ciphers typically use functions that simulate randomly permuted tables. An example (adapted from \[Kaufman 2002\]) of such a function for k = 64 bits is shown in Figure 8.5. The function first breaks a 64-bit block into 8 chunks, with each chunk consisting of 8 bits. Each 8-bit chunk is processed by an 8-bit to 8-bit table, which is of manageable size. For example, the first chunk is processed by the table denoted by T1. Next, the 8 output chunks are reassembled into a 64-bit block. The positions of the 64 bits in the block are then scrambled (permuted) to produce a 64-bit output. This output is fed back to the 64-bit input, where another cycle begins. After n such cycles, the function provides a 64-bit block of ciphertext. The purpose of the rounds is to make each input bit affect most (if not all) of the final output bits. (If only one round were used, a given input bit would affect only 8 of the 64 output bits.) The key for this block cipher algorithm would be the eight permutation tables (assuming the scramble function is publicly known).

Ngày nay có một số mật mã khối phổ biến, bao gồm DES (viết tắt của Chuẩn Mã Hóa Dữ Liệu), 3DES và AES (viết tắt của Mã Hóa Nâng Cao)

Bảng 8.1 ♦ Một thuật toán mã hóa khối 3-bit cụ thể

đầu vào đầu ra đầu vào đầu ra

Tiêu chuẩn). Mỗi một trong các tiêu chuẩn này sử dụng các hàm, thay vì các bảng đã được xác định trước, theo kiểu của Hình 8.5 (dù phức tạp hơn và đặc thù cho mỗi mã hóa). Mỗi thuật toán này cũng sử dụng một chuỗi bit làm khóa. Ví dụ, DES sử dụng các khối 64-bit với khóa 56-bit. AES sử dụng các khối 128-bit và có thể hoạt động với các khóa dài 128, 192 và 256 bit. Khóa của một thuật toán xác định các ánh xạ và hoán vị \"bảng con\" cụ thể bên trong thuật toán. Cuộc tấn công dò kiếm mạnh cho từng mã hóa này là thử tất cả các khóa, áp dụng thuật toán giải mã với mỗi khóa. Quan sát thấy rằng với độ dài khóa là n, có 2\^n khóa khả dĩ. NIST \[NIST 2001\] ước tính rằng một máy có thể phá DES 56-bit trong một giây (tức là thử tất cả 2\^56 khóa trong một giây) sẽ cần khoảng 149 nghìn tỷ năm để phá khóa AES 128-bit.

Xâu khối mã hóa

Trong các ứng dụng mạng máy tính, chúng ta thường cần mã hóa các thông điệp dài hoặc các luồng dữ liệu dài. Nếu chúng ta áp dụng một mật mã khối như đã mô tả bằng cách đơn giản cắt thông điệp thành các khối k-bit và mã hóa từng khối một cách độc lập, một vấn đề tinh vi nhưng quan trọng sẽ xảy ra. Để thấy điều này, hãy quan sát rằng hai hoặc nhiều khối bản rõ có thể giống nhau. Ví dụ, bản rõ trong hai hoặc nhiều khối có thể là "HTTP/1.1". Đối với những khối giống nhau này, rõ ràng một mật mã khối sẽ tạo ra cùng một bản mã. Một kẻ tấn công có thể đoán ra bản rõ khi thấy các khối bản mã giống nhau và thậm chí có thể giải mã toàn bộ thông điệp bằng cách xác định các khối bản mã giống nhau và sử dụng kiến thức về cấu trúc giao thức cơ bản \[Kaufman 2002\].

*Hình 8.5 ♦ Một ví dụ về mật mã khối*

Đầu ra 64-bit

Vòng lặp cho n vòng

8 bit

8 bit

T1

8 bit

8 bit

T2

8 bit

8 bit

T3

8 bit

Đầu vào 64-bit

8 bit

T4

8 bit

8 bit

T5

8 bit

8 bit

T6

8 bit

8 bit

T7

8 bit

8 bit

T8

bộ trộn 64-bit

To address this problem, we can mix some randomness into the ciphertext so that identical plaintext blocks produce different ciphertext blocks. To explain this idea, let m(i) denote the ith plaintext block, c(i) denote the ith ciphertext block, and a ⊕b denote the exclusive-or (XOR) of two bit strings, a and b. (Recall that the 0 ⊕0 = 1 ⊕1 = 0 and 0 ⊕1 = 1 ⊕0 = 1, and the XOR of two bit strings is done on a bit-by-bit basis. So, for example, 10101010 ⊕11110000 = 01011010.) Also, denote the block-cipher encryption algorithm with key S as KS. The basic idea is as follows. The sender creates a random k-bit number r(i) for the ith block and calculates c(i) = KS(m(i) ⊕r(i )). Note that a new k-bit random number is chosen for each block. The sender then sends c(1), r(1), c(2), r(2), c(3), r(3), and so on. Since the receiver receives c(i) and r(i), it can recover each block of the plaintext by computing m(i) = KS(c(i)) ⊕r(i ). It is important to note that, although r(i) is sent in the clear and thus can be sniffed by Trudy, she cannot obtain the plaintext m(i), since she does not know the key KS. Also note that if two plaintext blocks m(i) and m(j) are the same, the corresponding ciphertext blocks c(i) and c(j) will be different (as long as the random numbers r(i) and r(j) are different, which occurs with very high probability).

Ví dụ, hãy xem xét bộ mã hóa khối 3-bit trong Bảng 8.1. Giả sử bản rõ là 010010010. Nếu Alice mã hóa trực tiếp bản rõ này, mà không bao gồm tính ngẫu nhiên, bản mã kết quả sẽ trở thành 101101101. Nếu Trudy nghe trộm bản mã này, vì mỗi ba khối mã hóa đều giống nhau, cô ấy có thể suy đoán chính xác rằng mỗi ba khối bản rõ cũng giống nhau. Bây giờ giả sử thay vào đó Alice tạo ra các khối ngẫu nhiên r(1) = 001, r(2) = 111, và r(3) = 100 và sử dụng kỹ thuật trên để tạo bản mã c(1) = 100, c(2) = 010, và c(3) = 000. Lưu ý rằng ba khối bản mã khác nhau mặc dù các khối bản rõ giống nhau. Sau đó, Alice gửi c(1), r(1), c(2), và r(2). Bạn nên xác minh rằng Bob có thể lấy lại bản rõ ban đầu bằng cách sử dụng khóa chia sẻ KS.

Người đọc tinh tường sẽ nhận thấy rằng việc giới thiệu tính ngẫu nhiên giải quyết một vấn đề nhưng lại tạo ra một vấn đề khác: cụ thể là, Alice phải truyền gấp đôi số bit so với trước đây. Thật vậy, đối với mỗi bit mật mã, cô ấy bây giờ cũng phải gửi một bit ngẫu nhiên, làm tăng gấp đôi băng thông cần thiết. Để vừa có bánh vừa ăn bánh, các mật mã khối thường sử dụng một kỹ thuật gọi là Xích Khối Mật Mã (CBC). Ý tưởng cơ bản là chỉ gửi một giá trị ngẫu nhiên cùng với thông điệp đầu tiên, và sau đó người gửi và người nhận sử dụng các khối mã đã tính toán thay cho các số ngẫu nhiên tiếp theo. Cụ thể, CBC hoạt động như sau:

1\. Trước khi mã hóa tin nhắn (hoặc luồng dữ liệu), người gửi tạo ra một

chuỗi k-bit ngẫu nhiên, được gọi là Vector Khởi tạo (IV). Ký hiệu vector khởi tạo này bằng c(0). Người gửi gửi IV đến người nhận dưới dạng văn bản rõ. 2. Đối với khối đầu tiên, người gửi tính m(1) ⊕ c(0), tức là tính toán phép loại trừ\...

sive-or của khối bản rõ đầu tiên với IV. Sau đó nó chạy kết quả qua thuật toán mã hóa khối để lấy khối bản mã tương ứng; tức là, c(1) = KS(m(1) ⊕c(0)). Người gửi gửi khối đã mã hóa c(1) đến người nhận. 3. Đối với khối thứ i, người gửi tạo khối bản mã thứ i từ c(i) =

KS(m(i) ⊕ c(i - 1)).

Hãy cùng xem xét một số hệ quả của phương pháp này. Thứ nhất, người nhận vẫn có thể khôi phục lại thông điệp gốc. Thật vậy, khi người nhận nhận được c(i), nó sẽ giải mã nó bằng KS để thu được s(i) = m(i) ⊕ c(i - 1); vì người nhận cũng biết c(i - 1), nó sẽ thu được khối bản rõ từ m(i) = s(i) ⊕ c(i - 1). Thứ hai, ngay cả khi hai khối bản rõ giống nhau, các bản mã tương ứng (hầu như luôn luôn) sẽ khác nhau. Thứ ba, mặc dù người gửi gửi IV ở dạng rõ, một kẻ xâm nhập vẫn sẽ không thể giải mã các khối bản mã, vì kẻ xâm nhập không biết khóa bí mật S. Cuối cùng, người gửi chỉ gửi một khối dư thừa (IV), do đó tăng băng thông sử dụng một cách không đáng kể cho các thông điệp dài (gồm hàng trăm khối).

Ví dụ, bây giờ chúng ta hãy xác định văn bản mã hóa cho mã hóa khối 3-bit trong Bảng 8.1 với văn bản rõ 010010010 và IV = c(0) = 001. Người gửi đầu tiên sử dụng IV để tính c(1) = KS(m(1) ⊕ c(0)) = 100. Sau đó người gửi tính c(2) = KS(m(2) ⊕ c(1)) = KS(010 ⊕ 100) = 000, và c(3) = KS(m(3) ⊕ c(2)) = KS(010 ⊕ 000) = 101. Người đọc nên xác minh rằng người nhận, biết IV và KS, có thể phục hồi văn bản rõ ban đầu.

CBC có một hệ quả quan trọng khi thiết kế các giao thức mạng an toàn: chúng ta sẽ cần cung cấp một cơ chế trong giao thức để phân phối IV từ người gửi đến người nhận. Chúng ta sẽ xem cách điều này được thực hiện cho một số giao thức sau trong chương này.

**8.2.2 Mã hóa khóa công khai**

Trong hơn 2.000 năm (từ thời mã hóa Caesar cho đến những năm 1970), truyền thông được mã hóa yêu cầu hai bên tham gia phải chia sẻ một bí mật chung --- khóa đối xứng được sử dụng để mã hóa và giải mã. Một khó khăn với phương pháp này là hai bên phải bằng cách nào đó đồng ý về khóa chung; nhưng để làm được điều đó, bản thân quá trình này cũng cần phải có truyền thông an toàn. Có lẽ các bên có thể gặp nhau trước và đồng ý về khóa trực tiếp (ví dụ, hai centurion của Caesar có thể gặp nhau tại các phòng tắm ở La Mã) và sau đó giao tiếp bằng mã hóa. Tuy nhiên, trong một thế giới kết nối mạng, các bên giao tiếp có thể sẽ không bao giờ gặp nhau và có thể chỉ trao đổi qua mạng.

Có khả năng nào để hai bên giao tiếp bằng mã hóa mà không cần một khóa bí mật chung đã biết trước không? Vào năm 1976, Diffie và Hellman \[Diffie 1976\] đã trình bày một thuật toán (hiện nay được biết đến với tên gọi Trao đổi Khóa Diffie-Hellman) để thực hiện điều đó---một cách tiếp cận hoàn toàn khác biệt và vô cùng tinh tế đối với giao tiếp an toàn, điều này đã dẫn đến sự phát triển của các hệ thống mật mã khóa công khai ngày nay. Chúng ta sẽ thấy ngay rằng các hệ thống mật mã khóa công khai cũng có một số đặc điểm tuyệt vời khiến chúng hữu ích không chỉ cho việc mã hóa, mà còn cho xác thực và chữ ký số. Thú vị là, đã xuất hiện thông tin rằng các ý tưởng tương tự như trong \[Diffie 1976\] và \[RSA 1978\] đã được phát triển độc lập vào đầu những năm 1970 trong một loạt các báo cáo bí mật của các nhà nghiên cứu tại Nhóm An ninh Điện tử-Truyền thông ở Vương quốc Anh \[Ellis 1987\].

Như thường xảy ra, những ý tưởng tuyệt vời có thể xuất hiện độc lập ở nhiều nơi; may mắn thay, những tiến bộ về khóa công khai không chỉ diễn ra trong bí mật, mà còn diễn ra trước công chúng nữa.

Việc sử dụng mật mã khóa công khai về mặt khái niệm khá đơn giản. Giả sử Alice muốn liên lạc với Bob. Như được minh họa trong Hình 8.6, thay vì Bob và Alice chia sẻ một khóa bí mật duy nhất (như trong trường hợp hệ thống khóa đối xứng), Bob (người nhận tin nhắn của Alice) thay vào đó có hai khóa---một khóa công khai có sẵn cho mọi người trên thế giới (bao gồm cả Trudy, kẻ xâm nhập) và một khóa riêng tư chỉ Bob biết. Chúng ta sẽ sử dụng ký hiệu K+

B và K-

B để chỉ khóa công khai và khóa riêng của Bob, tương ứng. Để giao tiếp với Bob, Alice trước tiên lấy khóa công khai của Bob. Alice sau đó mã hóa thông điệp của mình, m, gửi cho Bob bằng cách sử dụng khóa công khai của Bob và một thuật toán mã hóa đã biết (ví dụ, tiêu chuẩn hóa); nghĩa là, Alice tính toán K+

B(m). Bob nhận được tin nhắn được mã hóa của Alice và sử dụng khóa riêng của mình cùng với một thuật toán giải mã đã biết (ví dụ, tiêu chuẩn hóa) để giải mã tin nhắn được mã hóa của Alice. Tức là, Bob tính toán K-

B(K+

B(m)). Chúng ta sẽ thấy bên dưới rằng có các thuật toán mã hóa/giải mã và các kỹ thuật để chọn khóa công khai và khóa riêng sao cho K-

B(K+

B(m)) = m; nghĩa là, áp dụng khóa công khai của Bob, K+

B, tới một tin nhắn, m (để nhận K+

B(m)), và sau đó áp dụng khóa riêng của Bob, K-

B, đến phiên bản mã hóa của m (tức là, tính toán K-

B(K+

B(m))) trả về m. Đây là một kết quả đáng chú ý! Theo cách này, Alice có thể sử dụng khóa công khai có sẵn của Bob để gửi một tin nhắn bí mật cho Bob mà không cần cả hai phải phân phối bất kỳ khóa bí mật nào! Chúng ta sẽ sớm thấy rằng chúng ta có thể hoán đổi giữa mã hóa khóa công khai và khóa riêng và đạt được cùng một kết quả đáng chú ý----tức là, K-

B (B +(m)) = K+

B (K-

B(m)) = m. Mặc dù mật mã khóa công khai rất hấp dẫn, một mối quan ngại ngay lập tức xuất hiện. Vì khóa mã hóa của Bob là công khai, bất cứ ai cũng có thể gửi một thông điệp đã được mã hóa

*Hình 8.6 ♦ Mã hóa khóa công khai*

Mã hóa

thuật toán

Bản mã

Giải mã

thuật toán

Tin nhắn văn bản thuần túy, m

Tin nhắn văn bản thuần túy, m

Khóa giải mã riêng

m = KB

--(KB

+(m))

KB

--

KB

+(m)

Khóa mã hóa công khai

KB

\+

tin nhắn gửi đến Bob, bao gồm Alice hoặc ai đó giả vờ là Alice. Trong trường hợp sử dụng một khóa bí mật chung, việc người gửi biết khóa bí mật ngầm định xác định người gửi đối với người nhận. Tuy nhiên, trong trường hợp mã hóa khóa công khai, điều này không còn đúng nữa vì bất kỳ ai cũng có thể gửi một tin nhắn được mã hóa đến Bob sử dụng khóa công khai có sẵn của Bob. Một chữ ký số, một chủ đề mà chúng ta sẽ nghiên cứu trong Mục 8.3, là cần thiết để liên kết người gửi với một tin nhắn.

RSA

Mặc dù có thể có nhiều thuật toán giải quyết những mối quan tâm này, thuật toán RSA (đặt theo tên các nhà sáng lập của nó, Ron Rivest, Adi Shamir và Leonard Adleman) gần như đã trở thành đồng nghĩa với mã hóa khóa công khai. Trước tiên, hãy xem RSA hoạt động như thế nào và sau đó xem xét lý do tại sao nó hoạt động.

RSA sử dụng rộng rãi các phép toán số học sử dụng số học modulo-n. Vì vậy, hãy cùng ôn lại một cách ngắn gọn về số học modulo. Hãy nhớ rằng x mod n đơn giản có nghĩa là phần dư của x khi chia cho n; ví dụ, 19 mod 5 = 4. Trong số học modulo, người ta thực hiện các phép toán thông thường của cộng, nhân và lũy thừa. Tuy nhiên, kết quả của mỗi phép toán được thay thế bằng phần dư nguyên còn lại khi kết quả được chia cho n. Việc cộng và nhân trong số học modulo được thuận tiện nhờ các sự thật hữu ích sau:

\[(a mod n) + (b mod n)\] mod n = (a + b) mod n

\[(a mod n) - (b mod n)\] mod n = (a - b) mod n

**\[(a mod n) \# (b mod n)\] mod n = (a \# b) mod n**

Theo điều thứ ba, ta có (a mod n)\^d mod n = a\^d mod n, đây là một đẳng thức mà chúng ta sớm thấy rất hữu ích.

Giả sử bây giờ Alice muốn gửi một tin nhắn được mã hóa RSA đến Bob, như minh họa trong Hình 8.6. Trong thảo luận về RSA của chúng ta, hãy luôn ghi nhớ rằng một tin nhắn không gì khác hơn là một mẫu bit, và mọi mẫu bit đều có thể được đại diện duy nhất bằng một số nguyên (cùng với độ dài của mẫu bit đó). Ví dụ, giả sử một tin nhắn là mẫu bit 1001; tin nhắn này có thể được đại diện bởi số nguyên thập phân 9. Do đó, khi mã hóa một tin nhắn bằng RSA, điều đó tương đương với việc mã hóa số nguyên duy nhất đại diện cho tin nhắn.

Có hai thành phần liên quan với nhau của RSA:

• Việc lựa chọn khóa công khai và khóa riêng • Thuật toán mã hóa và giải mã

Để tạo các khóa RSA công khai và riêng tư, Bob thực hiện các bước sau:

1\. Chọn hai số nguyên tố lớn, p và q. p và q nên lớn bao nhiêu?

Giá trị càng lớn, việc phá RSA càng khó, nhưng thời gian thực hiện càng lâu

thực hiện việc mã hóa và giải mã. Phòng thí nghiệm RSA khuyến nghị rằng tích của p và q nên ở mức khoảng 1.024 bit. Để thảo luận về cách tìm các số nguyên tố lớn, xem \[Caldwell 2020\]. 2. Tính n = pq và z = (p - 1)(q - 1). 3. Chọn một số, e, nhỏ hơn n, mà không có các ước số chung (ngoài 1)

với z. (Trong trường hợp này, e và z được cho là nguyên tố cùng nhau.) Chữ e được sử dụng vì giá trị này sẽ được dùng trong mã hóa. 4. Tìm một số, d, sao cho ed - 1 chia hết (tức là không còn dư)

bởi z. Chữ cái d được sử dụng vì giá trị này sẽ được dùng trong giải mã. Nói cách khác, với e, chúng ta chọn d sao cho

ed mod z = 1

5\. Khóa công khai mà Bob công khai cho thế giới, K+

B, là cặp số (n, e); khóa riêng của anh ấy, K-

B, là cặp số (n, d).

Việc mã hóa của Alice và giải mã của Bob được thực hiện như sau:

• Giả sử Alice muốn gửi cho Bob một mẫu bit được biểu diễn bởi số nguyên m (với m ≤ n). Để mã hóa, Alice thực hiện phép lũy thừa me, sau đó tính phần dư nguyên khi me bị chia cho n. Nói cách khác, giá trị được mã hóa, c, của thông điệp bản rõ m của Alice là

c = me chia lấy dư n

Mẫu bit tương ứng với bản mã c này được gửi cho Bob. • Để giải mã thông điệp bản mã nhận được, c, Bob tính toán

m = cd mod n

**which requires the use of his private key (n, d). As a simple example of RSA, suppose Bob chooses p = 5 and q = 7. (Admittedly, these values are far too small to be secure.) Then n = 35 and z = 24. Bob chooses e = 5, since 5 and 24 have no common factors. Finally, Bob chooses d = 29, since 5 \# 29 - 1 (that is, ed - 1) is exactly divisible by 24. Bob makes the two values, n = 35 and e = 5, public and keeps the value d = 29 secret. Observing these two public values, suppose Alice now wants to send the letters l, o, v, and e to Bob. Interpreting each letter as a number between 1 and 26 (with a being 1, and z being 26), Alice and Bob perform the encryption and decryption shown in Tables 8.2 and 8.3, respectively. Note that in this example, we consider each of the four letters as a distinct message. A more realistic example would be to convert the four letters into their 8-bit ASCII representations and then encrypt the integer corresponding to the resulting 32-bit bit pattern. (Such a realistic example generates numbers that are much too long to print in a textbook!)**

Với việc ví dụ "đồ chơi" trong Bảng 8.2 và 8.3 đã tạo ra một số số cực lớn, và với việc chúng ta đã thấy trước đó rằng p và q nên có độ dài vài trăm bit, nhiều vấn đề thực tiễn liên quan đến RSA xuất hiện. Làm thế nào để chọn các số nguyên tố lớn? Sau đó làm thế nào để chọn e và d? Làm thế nào để thực hiện phép lũy thừa với các số lớn? Một cuộc thảo luận về những vấn đề quan trọng này vượt quá phạm vi của cuốn sách này; xem \[Kaufman 2002\] và các tài liệu tham khảo ở đó để biết chi tiết.

Khóa phiên

Chúng tôi lưu ý rằng việc lũy thừa theo yêu cầu của RSA là một quá trình khá tốn thời gian. Do đó, RSA thường được sử dụng trong thực tiễn kết hợp với mật mã khóa đối xứng. Ví dụ, nếu Alice muốn gửi cho Bob một lượng dữ liệu được mã hóa lớn, cô ấy có thể làm như sau. Trước tiên, Alice chọn một khóa sẽ được sử dụng để mã hóa dữ liệu; khóa này được gọi là khóa phiên, và được ký hiệu là KS. Alice phải thông báo cho Bob về khóa phiên, vì đây là khóa đối xứng chung mà họ sẽ sử dụng với mật mã khóa đối xứng (ví dụ, với DES hoặc AES). Alice mã hóa khóa phiên bằng khóa công khai của Bob, tức là tính c = (KS)e mod n. Bob nhận khóa phiên được mã hóa bởi RSA, c, và giải mã nó để thu được

Bảng 8.2 ♦ Mã hóa RSA của Alice, e = 5, n = 35

Chữ thường m: biểu diễn số me Mã hóa c = me mod n

l 248832

o 759375

v 5153632

e

Bảng 8.3 ♦ Giải mã RSA của Bob, d = 29, n = 35

Bản mã c cd m = cd mod n Chữ cái bản rõ

4819685721067509150915091411825223071697 l

127834039403948858939111232757568359375 o

851643319086537701956194499721106030592 v

1000000000000000000000000000000 e

khóa phiên, KS. Bob giờ đây biết khóa phiên mà Alice sẽ sử dụng cho việc truyền dữ liệu được mã hóa của cô ấy.

Tại sao RSA lại hoạt động?

Mã hóa/giải mã RSA có vẻ khá kỳ diệu. Tại sao bằng cách áp dụng thuật toán mã hóa và sau đó thuật toán giải mã, người ta lại thu được thông điệp gốc? Để hiểu tại sao RSA hoạt động, một lần nữa đặt n = pq, trong đó p và q là các số nguyên tố lớn được sử dụng trong thuật toán RSA.

Hãy nhớ rằng, theo mã hóa RSA, một thông điệp (được biểu diễn duy nhất bởi một số nguyên), m, được nâng lên lũy thừa e với phép toán modulo-n, tức là,

c = me chia lấy dư n

Giải mã được thực hiện bằng cách nâng giá trị này lên mũ d, một lần nữa sử dụng toán học modulo-n. Kết quả của một bước mã hóa theo sau bởi một bước giải mã là (me mod n)d mod n. Bây giờ chúng ta hãy xem chúng ta có thể nói gì về giá trị này. Như đã đề cập trước đó, một tính chất quan trọng của toán học modulo là (a mod n)d mod n = ad mod n cho bất kỳ giá trị a, n và d nào. Do đó, sử dụng a = me trong tính chất này, chúng ta có

(me mod n)d mod n = med mod n

Do đó, vẫn còn phải chứng minh rằng med mod n = m. Mặc dù chúng ta đang cố gắng loại bỏ một phần phép thuật về lý do tại sao RSA hoạt động, để thiết lập điều này, chúng ta sẽ cần sử dụng một kết quả khá kỳ diệu từ lý thuyết số ở đây. Cụ thể, chúng ta sẽ cần kết quả nói rằng nếu p và q là số nguyên tố, n = pq, và z = (p - 1)(q - 1), thì xy mod n giống như x(y mod z) mod n \[Kaufman 2002\]. Áp dụng kết quả này với x = m và y = ed, ta có

med mod n = m(ed mod z) mod n

Nhưng hãy nhớ rằng chúng ta đã chọn e và d sao cho ed mod z = 1. Điều này cho chúng ta

med mod n = m1 mod n = m

đây chính xác là kết quả mà chúng ta đang tìm kiếm! Bằng cách đầu tiên lấy lũy thừa với số mũ e (tức là mã hóa) và sau đó lấy lũy thừa với số mũ d (tức là giải mã), chúng ta thu được giá trị ban đầu, m. Thậm chí còn tuyệt vời hơn là trường hợp nếu chúng ta đầu tiên lấy lũy thừa với số mũ d và sau đó lấy lũy thừa với số mũ e---tức là, chúng ta đảo ngược thứ tự mã hóa và giải mã, thực hiện phép giải mã trước và sau đó áp dụng phép mã hóa---chúng ta cũng thu được giá trị ban đầu, m. Kết quả tuyệt vời này ngay lập tức xuất phát từ số học mô-đun:

(md mod n)e mod n = mde mod n = med mod n = (me mod n)d mod n

Sự an toàn của RSA dựa trên thực tế là hiện chưa có thuật toán nào được biết để phân tích nhanh một số, trong trường hợp này là giá trị công khai n, thành các số nguyên tố p và q. Nếu biết p và q, thì với giá trị công khai e, người ta có thể dễ dàng tính toán khóa bí mật d. Mặt khác, chưa biết liệu có tồn tại các thuật toán phân tích số nhanh hay không, và theo nghĩa này, sự an toàn của RSA không được đảm bảo. Với những tiến bộ gần đây trong điện toán lượng tử, và các thuật toán phân tích nhanh được công bố cho máy tính lượng tử, có lo ngại rằng RSA có thể không an toàn mãi mãi \[MIT TR 2019\]. Tuy nhiên, việc thực hiện thực tế các thuật toán này vẫn có vẻ còn xa trong tương lai.

Một thuật toán mã hóa khóa công khai phổ biến khác là thuật toán Diffie-Hellman, mà chúng ta sẽ khám phá ngắn gọn trong các bài tập về nhà. Diffie-Hellman không linh hoạt như RSA ở chỗ nó không thể được sử dụng để mã hóa các thông điệp có độ dài tùy ý; tuy nhiên, nó có thể được sử dụng để thiết lập khóa phiên đối xứng, mà khóa này lần lượt được sử dụng để mã hóa các thông điệp.

**8.3 Tính toàn vẹn thông điệp và Chữ ký số**

Trong phần trước, chúng ta đã thấy cách mã hóa có thể được sử dụng để cung cấp tính bảo mật cho hai thực thể đang giao tiếp. Trong phần này, chúng ta sẽ chuyển sang chủ đề mật mã quan trọng không kém là cung cấp tính toàn vẹn của thông điệp (còn được gọi là xác thực thông điệp). Cùng với tính toàn vẹn của thông điệp, chúng ta sẽ thảo luận hai chủ đề liên quan trong phần này: chữ ký số và xác thực điểm cuối.

Chúng tôi định nghĩa vấn đề tính toàn vẹn của thông điệp bằng cách sử dụng, một lần nữa, Alice và Bob. Giả sử Bob nhận được một thông điệp (có thể được mã hóa hoặc ở dạng văn bản thuần túy) và anh ấy tin rằng thông điệp này được gửi bởi Alice. Để xác thực thông điệp này, Bob cần xác minh:

1\. Thông điệp thực sự xuất phát từ Alice. 2. Thông điệp không bị sửa đổi trên đường đi đến Bob.

Chúng ta sẽ thấy trong các Mục 8.4 đến 8.7 rằng vấn đề về tính toàn vẹn của thông điệp là một mối quan tâm quan trọng trong hầu hết tất cả các giao thức mạng bảo mật.

Lấy một ví dụ cụ thể, hãy xem xét một mạng máy tính sử dụng thuật toán định tuyến trạng thái liên kết (như OSPF) để xác định các tuyến giữa mỗi cặp bộ định tuyến trong mạng (xem Chương 5). Trong một thuật toán trạng thái liên kết, mỗi bộ định tuyến cần phát thông điệp trạng thái liên kết tới tất cả các bộ định tuyến khác trong mạng. Thông điệp trạng thái liên kết của một bộ định tuyến bao gồm danh sách các nút kề trực tiếp của nó và chi phí trực tiếp tới các nút này. Khi một bộ định tuyến nhận được thông điệp trạng thái liên kết từ tất cả các bộ định tuyến khác, nó có thể tạo ra một bản đồ hoàn chỉnh của mạng, chạy thuật toán định tuyến chi phí thấp nhất của nó và cấu hình bảng chuyển tiếp. Một cuộc tấn công tương đối dễ dàng vào thuật toán định tuyến là Trudy phân phối các thông điệp trạng thái liên kết giả mạo với thông tin trạng thái liên kết không chính xác. Do đó, cần đảm bảo tính toàn vẹn của thông điệp --- khi bộ định tuyến B nhận được thông điệp trạng thái liên kết từ bộ định tuyến A, bộ định tuyến B nên xác thực rằng bộ định tuyến A thực sự đã tạo ra thông điệp và hơn nữa, không ai làm giả thông điệp trong quá trình truyền.

Trong phần này, chúng tôi mô tả một kỹ thuật toàn vẹn thông điệp phổ biến được sử dụng bởi nhiều giao thức mạng an toàn. Nhưng trước khi làm điều đó, chúng ta cần đề cập đến một chủ đề quan trọng khác trong mật mã học---các hàm băm mật mã.

**8.3.1 Hàm Băm Mã Hóa**

Như được hiển thị trong Hình 8.7, một hàm băm nhận một đầu vào, m, và tính toán một chuỗi có kích thước cố định H(m) được gọi là băm. Tổng kiểm tra Internet (Chương 3) và CRCs (Chương 6) đáp ứng định nghĩa này. Một hàm băm mật mã học cần phải có đặc tính bổ sung sau:

• Về mặt tính toán, điều không khả thi là tìm hai thông điệp khác nhau x và y sao cho H(x) = H(y).

Không chính thức, thuộc tính này có nghĩa là về mặt tính toán, kẻ xâm nhập không thể thay thế một thông điệp bằng một thông điệp khác được bảo vệ bởi hàm băm. Tức là, nếu (m, H(m)) là thông điệp và hàm băm của thông điệp được tạo bởi người gửi, thì kẻ xâm nhập không thể giả mạo nội dung của một thông điệp khác, y, có cùng giá trị băm như thông điệp gốc.

Hãy thuyết phục bản thân rằng một kiểm tra tổng đơn giản, chẳng hạn như kiểm tra tổng trên Internet, sẽ là một hàm băm mật mã kém. Thay vì thực hiện phép toán bù 1 (như trong kiểm tra tổng trên Internet), hãy tính toán tổng kiểm tra bằng cách coi mỗi ký tự như một byte và cộng các byte lại với nhau theo từng khối 4 byte một. Giả sử Bob nợ Alice 100,99 đô la và gửi một IOU cho Alice gồm chuỗi văn bản "IOU100.99BOB." Biểu diễn ASCII (theo ký hiệu thập lục phân) của các chữ cái này là 49,4F,55,31,30,30,2E,39,39,42,4F,42.

*Hình 8.8 (phía trên) cho thấy tổng kiểm tra 4 byte cho thông điệp này là B2 C1 D2 AC. Một thông điệp hơi khác (và tốn kém hơn nhiều đối với Bob)*

*Hình 8.7 ♦ Hàm băm*

Hàm băm nhiều-đến-một

Tin nhắn dài: m

Thân gửi Alice: Đây là một bức thư RẤT dài vì có quá nhiều điều để nói\..... \...\...\.... \...\...\....

Bob

Độ dài cố định

băm: H(m)

Opgmdvboijrtnsd gghPPdogm;lcvkb

được hiển thị ở nửa dưới của Hình 8.8. Các thông điệp "IOU100.99BOB" và "IOU900.19BOB" có cùng một giá trị kiểm tra. Do đó, thuật toán kiểm tra đơn giản này vi phạm yêu cầu ở trên. Dựa trên dữ liệu gốc, rất dễ dàng để tìm một bộ dữ liệu khác có cùng giá trị kiểm tra. Rõ ràng, vì mục đích bảo mật, chúng ta sẽ cần một hàm băm mạnh hơn so với kiểm tra.

Thuật toán băm MD5 của Ron Rivest \[RFC 1321\] hiện đang được sử dụng rộng rãi. Nó tính toán một băm 128-bit thông qua quy trình bốn bước bao gồm bước đệm (thêm một số 1, sau đó theo sau là đủ số 0 để độ dài của thông điệp thỏa mãn các điều kiện nhất định), bước thêm vào (thêm một biểu diễn 64-bit của độ dài thông điệp trước khi đệm), khởi tạo một bộ cộng dồn, và bước lặp cuối cùng trong đó các khối 16 từ của thông điệp được xử lý (biến đổi) trong bốn vòng. Để biết mô tả về MD5 (bao gồm triển khai mã nguồn C) tham khảo \[RFC 1321\].

Thuật toán băm quan trọng thứ hai đang được sử dụng ngày nay là Thuật toán Băm An toàn (SHA-1) \[FIPS 1995\]. Thuật toán này dựa trên các nguyên tắc tương tự như những nguyên tắc được sử dụng trong thiết kế của MD4 \[RFC 1320\], tiền thân của MD5. SHA-1, một tiêu chuẩn liên bang của Mỹ, được yêu cầu sử dụng bất cứ khi nào cần một thuật toán băm mật mã cho các ứng dụng liên bang. Nó tạo ra một bản một chiều (message digest) dài 160-bit. Độ dài đầu ra dài hơn làm cho SHA-1 an toàn hơn.

**8.3.2 Mã Xác Thực Thông Điệp**

Bây giờ chúng ta hãy quay lại vấn đề về tính toàn vẹn của tin nhắn. Giờ đây khi chúng ta đã hiểu các hàm băm, hãy thử lần đầu cách mà chúng ta có thể thực hiện tính toàn vẹn của tin nhắn:

*Hình 8.8 ♦ Thông điệp ban đầu và thông điệp gian lận có cùng*

tổng kiểm tra!

Tin nhắn

Tôi nợ BOB 100,99

Biểu diễn ASCII 4F 2E 4F

B2 C1 D2 AC Tổng kiểm tra

Tin nhắn

Tôi nợ 900,19 Bob

Biểu diễn ASCII 4F 2E 4F

B2 C1 D2 AC Tổng kiểm tra

1\. Alice tạo thông điệp m và tính toán hàm băm H(m) (ví dụ, với SHA-1). 2. Alice sau đó thêm H(m) vào thông điệp m, tạo ra một thông điệp mở rộng

(m, H(m)), và gửi thông điệp mở rộng đến Bob. 3. Bob nhận được một thông điệp mở rộng (m, h) và tính H(m). Nếu H(m) = h,

Bob kết luận rằng mọi thứ đều ổn.

Cách tiếp cận này rõ ràng là có khuyết điểm. Trudy có thể tạo ra một tin nhắn giả m´ trong đó cô ấy nói rằng cô ấy là Alice, tính H(m´), và gửi cho Bob (m´, H(m´)). Khi Bob nhận được tin nhắn, mọi thứ đều đúng theo bước 3, vì vậy Bob không nghi ngờ bất kỳ hành vi lừa đảo nào.

Để thực hiện tính toàn vẹn của tin nhắn, ngoài việc sử dụng các hàm băm mật mã, Alice và Bob sẽ cần một bí mật chung s. Bí mật chung này, không gì khác hơn là một chuỗi bit, được gọi là khóa xác thực. Sử dụng bí mật chung này, tính toàn vẹn của tin nhắn có thể được thực hiện như sau:

1\. Alice tạo thông điệp m, kết hợp s với m để tạo m + s, và tính toán

băm H(m + s) (ví dụ, với SHA-1). H(m + s) được gọi là mã xác thực thông điệp (MAC). 2. Alice sau đó nối MAC vào thông điệp m, tạo thành thông điệp mở rộng

(m, H(m + s)), và gửi thông điệp mở rộng đến Bob. 3. Bob nhận được thông điệp mở rộng (m, h) và nhận biết s, tính MAC

H(m + s). Nếu H(m + s) = h, Bob kết luận rằng mọi thứ đều ổn.

Tóm tắt quy trình được trình bày trong Hình 8.9. Người đọc nên lưu ý rằng MAC ở đây (viết tắt của "message authentication code" -- mã xác thực thông điệp) không phải là cùng một MAC được sử dụng trong các giao thức lớp liên kết (viết tắt của "medium access control" -- điều khiển truy cập phương tiện)!

Một đặc điểm hay của MAC là nó không yêu cầu một thuật toán mã hóa. Thật vậy, trong nhiều ứng dụng, bao gồm cả thuật toán định tuyến trạng thái liên kết được mô tả trước đó, các thực thể giao tiếp chỉ quan tâm đến tính toàn vẹn của thông điệp và

*Hình 8.9 ♦ Mã xác thực thông điệp (MAC)*

H(.)

H(.)

m

m

m

m

s

s

s

\+ Internet

So sánh

Chìa khóa:

= Tin nhắn

= Bí mật chung

H(m+s)

H(m+s)

không quan tâm đến tính bảo mật của thông điệp. Sử dụng MAC, các thực thể có thể xác thực các thông điệp mà họ gửi cho nhau mà không cần phải tích hợp các thuật toán mã hóa phức tạp vào quá trình đảm bảo tính toàn vẹn.

Như bạn có thể mong đợi, một số tiêu chuẩn khác nhau cho MAC đã được đề xuất trong nhiều năm qua. Tiêu chuẩn phổ biến nhất hiện nay là HMAC, có thể được sử dụng với cả MD5 hoặc SHA-1. HMAC thực sự chạy dữ liệu và khóa xác thực qua hàm băm hai lần \[Kaufman 2002; RFC 2104\].

Vẫn còn một vấn đề quan trọng. Chúng ta phân phối khóa xác thực chia sẻ đến các thực thể giao tiếp như thế nào? Ví dụ, trong thuật toán định tuyến trạng thái liên kết, chúng ta sẽ cần phân phối khóa xác thực bí mật đến từng bộ định tuyến trong hệ thống tự trị. (Lưu ý rằng tất cả các bộ định tuyến có thể sử dụng cùng một khóa xác thực.) Một quản trị viên mạng thực sự có thể thực hiện điều này bằng cách trực tiếp đến thăm từng bộ định tuyến. Hoặc, nếu quản trị viên mạng là người lười biếng, và nếu từng bộ định tuyến có khóa công khai riêng của nó, quản trị viên mạng có thể phân phối khóa xác thực cho bất kỳ bộ định tuyến nào bằng cách mã hóa nó với khóa công khai của bộ định tuyến đó và sau đó gửi khóa đã mã hóa qua mạng đến bộ định tuyến.

**8.3.3 Chữ ký kỹ thuật số**

Hãy nghĩ về số lần bạn đã ký tên mình trên một tờ giấy trong tuần vừa qua. Bạn ký séc, biên lai thẻ tín dụng, tài liệu pháp lý và thư từ. Chữ ký của bạn chứng thực rằng chính bạn (không phải người khác) đã thừa nhận và/hoặc đồng ý với nội dung của tài liệu. Trong một thế giới kỹ thuật số, người ta thường muốn chỉ ra chủ sở hữu hoặc người tạo ra một tài liệu, hoặc để biểu thị sự đồng ý của mình với nội dung của tài liệu. Chữ ký số là một kỹ thuật mã hóa để đạt được những mục tiêu này trong thế giới kỹ thuật số.

Cũng giống như chữ ký viết tay, việc ký số nên được thực hiện theo cách có thể xác minh và không thể làm giả. Tức là, phải có khả năng chứng minh rằng một tài liệu được ký bởi một cá nhân thực sự được ký bởi chính cá nhân đó (chữ ký phải có thể xác minh) và chỉ cá nhân đó mới có thể ký tài liệu (chữ ký không thể bị làm giả).

Bây giờ hãy xem xét cách chúng ta có thể thiết kế một sơ đồ chữ ký điện tử. Hãy quan sát rằng khi Bob ký một tin nhắn, Bob phải đặt điều gì đó lên tin nhắn mà là duy nhất đối với anh ấy. Bob có thể cân nhắc đính kèm một MAC làm chữ ký, trong đó MAC được tạo bằng cách ghép khóa của anh ấy (duy nhất đối với anh ấy) vào tin nhắn, sau đó lấy giá trị băm. Nhưng để Alice xác minh chữ ký, cô ấy cũng phải có một bản sao của khóa, trong trường hợp đó khóa sẽ không còn duy nhất đối với Bob. Do đó, MAC sẽ không thực hiện được công việc ở đây.

Hãy nhớ rằng với mật mã khóa công khai, Bob có cả một khóa công khai và khóa riêng, với cả hai khóa này đều là duy nhất đối với Bob. Do đó, mật mã khóa công khai là một ứng cử viên tuyệt vời để cung cấp chữ ký số. Bây giờ hãy cùng xem nó được thực hiện như thế nào.

Giả sử Bob muốn ký kỹ thuật số một tài liệu, m. Chúng ta có thể coi tài liệu này như một tệp hoặc một tin nhắn mà Bob sẽ ký và gửi. Như minh họa trong Hình 8.10, để ký tài liệu này, Bob chỉ đơn giản sử dụng khóa riêng của mình, K-

B, để tính toán

K-

B(m). Ban đầu, có thể sẽ có vẻ lạ khi Bob sử dụng khóa riêng của mình (mà, như chúng ta đã thấy trong Mục 8.2, đã được dùng để giải mã một tin nhắn đã được mã hóa bằng khóa công khai của anh ấy) để ký một tài liệu. Nhưng hãy nhớ rằng mã hóa và giải mã không gì khác hơn là các phép toán học (lũy thừa lên luỹ thừa e hoặc d trong RSA; xem Mục 8.2) và hãy nhớ rằng mục tiêu của Bob không phải là để làm xáo trộn hay che khuất nội dung của tài liệu, mà là ký tài liệu theo một cách có thể xác minh và không thể làm giả. Chữ ký số của Bob trên tài liệu là K-

B(m). Chữ ký số K-

B(m) có đáp ứng các yêu cầu của chúng ta về khả năng xác minh và không thể làm giả không? Giả sử Alice có m và K-

B(m). Cô ấy muốn chứng minh tại tòa (có tính kiện tụng) rằng Bob thực sự đã ký vào tài liệu và là người duy nhất có thể đã ký vào tài liệu. Alice lấy khóa công khai của Bob, K+

B, và áp dụng nó vào chữ ký số, K-

B(m), liên quan đến tài liệu, m. Tức là, cô ấy tính K+

B(K-

B(m)), và voilà, với một màn trình diễn đầy kịch tính, cô ấy tạo ra m, hoàn toàn trùng khớp với tài liệu gốc! Alice sau đó lập luận rằng chỉ có Bob mới có thể ký tài liệu, vì những lý do sau:

• Người nào ký thông điệp phải đã sử dụng khóa riêng, KB, trong việc tính toán chữ ký K-

B(m), sao cho K+

B(K-

B(m)) = m. • Người duy nhất có thể biết khóa riêng, KB, là Bob. Hãy nhớ lại từ cuộc thảo luận của chúng ta về RSA trong Mục 8.2 rằng biết khóa công khai, K+

B, không có ích trong việc học khóa riêng, K-

B. Do đó, người duy nhất có thể biết K-

B là người đã tạo ra cặp khóa, (K+

B, K-

B), trước tiên, Bob. (Lưu ý rằng điều này giả định, tuy nhiên, rằng Bob chưa cung cấp K-

B đối với bất kỳ ai, cũng không ai đã lấy trộm K-

B từ Bob.)

Cũng quan trọng cần lưu ý rằng nếu tài liệu gốc, m, bất kỳ lúc nào được sửa đổi thành một dạng khác, m´, chữ ký mà Bob tạo ra cho m sẽ không còn hợp lệ cho m´,

*Hình 8.10 ♦ Tạo chữ ký số cho một tài liệu*

Mã hóa

thuật toán

Tin nhắn: m

Riêng tư của Bob

phím, KB

--

Thân gửi Alice: Xin lỗi vì tôi đã không thể viết thư trong suốt thời gian dài. Kể từ khi chúng ta\..... \...\...\.... \...\...\....

Bob

Thông điệp đã ký:

KB

-- (m)

fadfg54986fgnzmcnv T98734ngldskg02j ser09tugkjdﬂg \...\...\....

kể từ K+

B(K-

B(m)) không bằng m´. Do đó, chúng ta thấy rằng chữ ký số cũng cung cấp tính toàn vẹn của thông điệp, cho phép người nhận xác minh rằng thông điệp không bị thay đổi cũng như nguồn gốc của thông điệp.

Một mối lo ngại khi ký dữ liệu bằng mã hóa là việc mã hóa và giải mã tốn nhiều tài nguyên tính toán. Với chi phí của việc mã hóa và giải mã, việc ký dữ liệu thông qua mã hóa/giải mã hoàn toàn có thể là quá mức cần thiết. Một phương pháp hiệu quả hơn là đưa các hàm băm vào chữ ký số. Nhớ lại từ Mục 8.3.2 rằng một thuật toán băm nhận một thông điệp, m, có độ dài tùy ý và tính toán một "dấu vân tay" có độ dài cố định của thông điệp, ký hiệu là H(m). Sử dụng một hàm băm, Bob ký bản băm của một thông điệp thay vì chính thông điệp đó, nghĩa là Bob tính toán K-

B(H(m)). Vì H(m) thường nhỏ hơn nhiều so với thông điệp gốc m, nỗ lực tính toán cần thiết để tạo chữ ký số được giảm đáng kể.

Trong bối cảnh Bob gửi một tin nhắn cho Alice, Hình 8.11 cung cấp một tóm tắt về quy trình vận hành của việc tạo chữ ký số. Bob đưa tin nhắn dài ban đầu của mình qua một hàm băm. Sau đó, anh ta ký số kết quả băm này bằng khóa riêng của mình. Tin nhắn gốc (dưới dạng văn bản rõ) cùng với bản tóm tắt tin nhắn đã được ký số (sau đây gọi là chữ ký số) sau đó được gửi tới Alice. Hình 8.12 cung cấp một tóm tắt về quy trình vận hành của chữ ký. Alice áp dụng khóa công khai của người gửi lên tin nhắn để thu được kết quả băm. Alice cũng

*Hình 8.11 ♦ Gửi một tin nhắn có chữ ký số*

Riêng tư của Bob

phím, KB

--

Hàm băm nhiều-đến-một

Tin nhắn dài

Thân gửi Alice: Đây là một bức thư RẤT dài vì có quá nhiều điều để nói\..... \...\...\.... \...\...\....

Bob

Độ dài cố định

băm

Opgmdvboijrtnsd gghPPdogm;lcvkb

Đã ký

băm gói để gửi

đến Alice

Fgkopdgoo69cmxw 54psdterma\[asofmz

Mã hóa

thuật toán

áp dụng hàm băm cho thông điệp bản rõ để thu được kết quả băm thứ hai. Nếu hai giá trị băm khớp nhau, thì Alice có thể chắc chắn về tính toàn vẹn và tác giả của thông điệp.

Trước khi tiếp tục, chúng ta hãy so sánh ngắn gọn chữ ký số với MAC, vì chúng có những điểm tương đồng nhưng cũng có những điểm khác biệt quan trọng. Cả chữ ký số và MAC đều bắt đầu bằng một tin nhắn (hoặc một tài liệu). Để tạo MAC từ tin nhắn, chúng tôi nối thêm khóa xác thực vào tin nhắn, sau đó lấy hàm băm của kết quả. Lưu ý rằng cả mã hóa khóa chung và khóa đối xứng đều không liên quan đến việc tạo MAC. Để tạo chữ ký số, trước tiên chúng tôi lấy hàm băm của tin nhắn và sau đó mã hóa tin nhắn bằng khóa riêng của mình (sử dụng mật mã khóa chung). Do đó, chữ ký số là một kỹ thuật "nặng hơn" vì nó yêu cầu Cơ sở hạ tầng khóa công khai (PKI) cơ bản với các cơ quan chứng nhận như được mô tả bên dưới. Chúng ta sẽ thấy trong Phần 8.4 rằng PGP---một hệ thống e-mail bảo mật phổ biến---sử dụng chữ ký điện tử để đảm bảo tính toàn vẹn của thư. Chúng ta đã thấy rằng OSPF sử dụng MAC để đảm bảo tính toàn vẹn của tin nhắn. Chúng ta sẽ thấy trong Phần 8.5 và 8.6 rằng MAC cũng được sử dụng cho các giao thức bảo mật lớp vận chuyển và lớp mạng phổ biến.

Công chúng của Bob

phím, KB

\+

Tin nhắn dài

Thân gửi Alice: Đây là một bức thư RẤT dài vì có quá nhiều điều để nói\..... \...\...\.... \...\...\....

Bob

Độ dài cố định

băm

Opgmdvboijrtnsd gghPPdogm;lcvkb

Đã ký

băm

Fgkopdgoo69cmxw 54psdterma\[asofmz

So sánh hàm băm nhiều-đến-một

Độ dài cố định

băm

Opgmdvboijrtnsd gghPPdogm;lcvkb

Mã hóa

thuật toán

*Hình 8.12 ♦ Xác minh một thông điệp đã được ký*

Chứng nhận khóa công khai

Một ứng dụng quan trọng của chữ ký số là chứng nhận khóa công khai, tức là chứng nhận rằng một khóa công khai thuộc về một thực thể cụ thể. Chứng nhận khóa công khai được sử dụng trong nhiều giao thức mạng an toàn phổ biến, bao gồm IPsec và TLS.

Để hiểu rõ hơn về vấn đề này, hãy xem xét một phiên bản thương mại điện tử của trò đùa \"pizza\" cổ điển. Alice làm trong ngành giao pizza và nhận đơn hàng qua Internet. Bob, một người yêu thích pizza, gửi cho Alice một tin nhắn văn bản thuần túy bao gồm địa chỉ nhà và loại pizza mà anh ta muốn. Trong tin nhắn này, Bob cũng đính kèm chữ ký số (tức là, một băm đã ký của tin nhắn văn bản gốc) để chứng minh với Alice rằng anh ta là nguồn gốc thực sự của tin nhắn. Để xác minh chữ ký, Alice lấy khóa công khai của Bob (có thể từ máy chủ khóa công khai hoặc từ tin nhắn e-mail) và kiểm tra chữ ký số. Bằng cách này, cô đảm bảo rằng chính Bob, chứ không phải một thiếu niên nghịch ngợm, đã đặt món.

Tất cả những điều này nghe có vẻ ổn cho đến khi Trudy thông minh xuất hiện. Như được minh họa trong Hình 8.13, Trudy đang thực hiện một trò chơi khăm. Cô ấy gửi một tin nhắn cho Alice trong đó nói rằng cô ấy là Bob, cung cấp địa chỉ nhà của Bob và đặt một chiếc pizza. Trong tin nhắn này, cô ấy cũng bao gồm khóa công khai của mình (Trudy), mặc dù Alice một cách tự nhiên cho rằng đó là khóa công khai của Bob. Trudy cũng đính kèm một chữ ký số, được tạo ra bằng khóa riêng của chính cô ấy (Trudy). Sau khi nhận được tin nhắn, Alice áp dụng khóa công khai của Trudy (nghĩ rằng đó là khóa của Bob) vào chữ ký số và kết luận rằng tin nhắn văn bản thực sự được tạo bởi Bob. Bob sẽ rất ngạc nhiên khi nhân viên giao hàng mang một chiếc pizza phô mai pepperoni và cá cơm đến nhà mình!

Chúng ta thấy từ ví dụ này rằng để mật mã khóa công khai hữu ích, bạn cần phải có khả năng xác minh rằng bạn đang sở hữu khóa công khai thực sự của thực thể (người, bộ định tuyến, trình duyệt, và những thứ tương tự) mà bạn muốn liên lạc. Ví dụ, khi Alice muốn liên lạc với Bob sử dụng mật mã khóa công khai, cô ấy cần xác minh rằng khóa công khai được cho là của Bob thực sự là của Bob.

Liên kết một khóa công khai với một thực thể cụ thể thường được thực hiện bởi một Cơ quan cấp chứng chỉ (CA), nhiệm vụ của họ là xác nhận danh tính và phát hành chứng chỉ. Một CA có các vai trò sau:

1\. Một CA xác minh rằng một thực thể (một người, một router, v.v.) là người mà nó nói rằng họ là.

Không có quy trình bắt buộc cho việc chứng nhận được thực hiện như thế nào. Khi làm việc với một CA, người ta phải tin tưởng rằng CA đã thực hiện việc xác minh danh tính một cách nghiêm ngặt phù hợp. Ví dụ, nếu Trudy có thể bước vào CA Fly-by-Night và đơn giản nói "Tôi là Alice" và nhận các chứng chỉ liên quan đến danh tính của Alice, thì người ta không nên đặt nhiều niềm tin vào các khóa công khai được chứng nhận bởi CA Fly-by-Night. Mặt khác, người ta có thể (hoặc có thể không!) sẵn sàng tin tưởng một CA là một phần của chương trình liên bang hoặc tiểu bang. Bạn chỉ có thể tin tưởng danh tính gắn với một khóa công khai ở mức độ mà bạn có thể tin tưởng CA và các kỹ thuật xác minh danh tính của nó. Thật là một mạng lưới niềm tin rắc rối mà chúng ta dệt nên! 2. Khi CA xác minh danh tính của thực thể, CA tạo ra một chứng chỉ

nó liên kết khóa công khai của thực thể với danh tính. Chứng chỉ chứa

*Hình 8.13 ♦ Trudy giả danh Bob sử dụng mã hóa khóa công khai*

Riêng tư của Trudy

chìa khóa, KT

--

Công chúng của Trudy

chìa khóa, KT

\+

Đã ký (sử dụng khóa riêng của Trudy)

bản tóm tắt thông điệp

Fgkopdgoo69cmxw 54psdterma\[asofmz

Tin nhắn

Alice, giao một chiếc pizza cho tôi.

Bob

Hàm băm nhiều-đến-một

Alice sử dụng khóa công khai của Trudy, nghĩ rằng

nó là của Bob, và

kết luận rằng thông điệp là từ Bob

BÁNH PIZZA

Mã hóa

thuật toán

khóa công khai và thông tin nhận dạng duy nhất toàn cầu về chủ sở hữu của khóa công khai (ví dụ, tên con người hoặc địa chỉ IP). Chứng chỉ được ký số bởi CA. Các bước này được hiển thị trong Hình 8.14.

Hãy cùng xem chứng chỉ có thể được sử dụng như thế nào để chống lại những trò đùa đặt pizza, như Trudy, và những người không mong muốn khác. Khi Bob đặt món, anh ấy cũng gửi chứng chỉ được CA ký. Alice sử dụng khóa công khai của CA để kiểm tra tính hợp lệ của chứng chỉ của Bob và lấy khóa công khai của Bob.

Cả Liên minh Viễn thông Quốc tế (ITU) và IETF đều đã phát triển các tiêu chuẩn cho CA. ITU X.509 \[ITU 2005a\] xác định một dịch vụ xác thực cũng như cú pháp cụ thể cho các chứng chỉ. \[RFC 1422\] mô tả quản lý khóa dựa trên CA để sử dụng với thư điện tử Internet an toàn. Nó tương thích với X.509 nhưng vượt ra ngoài X.509 bằng cách thiết lập các thủ tục và quy ước cho một kiến trúc quản lý khóa. Bảng 8.4 mô tả một số trường quan trọng trong một chứng chỉ.

Bảng 8.4 ♦ Các trường được chọn trong khóa công khai X.509 và RFC 1422

Mô tả Tên Trường

Phiên bản Số phiên bản của đặc tả X.509

Số sê-ri định danh duy nhất do CA cấp cho một chứng chỉ

Chữ ký Chỉ định thuật toán được CA sử dụng để ký chứng chỉ này

Tên nhà phát hành Nhận dạng của CA phát hành chứng chỉ này, theo định danh tên riêng (DN) \[RFC 4514\]

Thời hạn hiệu lực Bắt đầu và kết thúc thời gian hiệu lực của chứng chỉ

Tên chủ thể: Thực thể mà khóa công khai liên kết với chứng chỉ này, theo định dạng DN

Khóa công khai của chủ thể Khóa công khai của chủ thể cũng như chỉ định của thuật toán khóa công khai (và các tham số thuật toán) sẽ được sử dụng với khóa này

**8.4 Xác thực Điểm đầu**

Xác thực đầu cuối là quá trình một thực thể chứng minh danh tính của mình với một thực thể khác qua mạng máy tính, ví dụ, một người dùng chứng minh danh tính của mình với máy chủ email. Là con người, chúng ta xác thực lẫn nhau theo nhiều cách: Chúng ta nhận ra khuôn mặt của nhau khi gặp mặt, chúng ta nhận ra giọng nói của nhau trên điện thoại, chúng ta được xác thực bởi nhân viên hải quan, người kiểm tra chúng ta dựa trên hình ảnh trong hộ chiếu.

*Hình 8.14 ♦ Bob có khóa công khai của mình được chứng thực bởi CA*

Chứng chỉ được ký bởi CA của Bob chứa

khóa công khai của anh ấy, KB

\+

Cơ quan chứng nhận (CA) (KB

+, B)

riêng tư của CA

chìa khóa, KCA

--

Mã hóa

thuật toán

Trong phần này, chúng ta xem xét cách một bên có thể xác thực bên kia khi hai bên đang giao tiếp qua mạng. Chúng ta tập trung vào việc xác thực một bên "trực tiếp", tại thời điểm mà giao tiếp thực sự đang diễn ra. Một ví dụ cụ thể là người dùng xác thực chính mình với một máy chủ email. Đây là một vấn đề hơi khác so với việc chứng minh rằng một thông điệp nhận được vào một thời điểm trong quá khứ thực sự đến từ người gửi được tuyên bố, như đã được nghiên cứu trong Mục 8.3.

Khi thực hiện xác thực qua mạng, các bên truyền thông không thể dựa vào thông tin sinh trắc học, chẳng hạn như hình dáng bên ngoài hoặc dấu vân giọng nói. Thật vậy, chúng ta sẽ thấy trong các nghiên cứu trường hợp sau rằng thường là các phần tử mạng như bộ định tuyến và các tiến trình máy khách/máy chủ phải xác thực lẫn nhau. Ở đây, việc xác thực phải được thực hiện chỉ dựa trên các thông điệp và dữ liệu được trao đổi như một phần của giao thức xác thực. Thông thường, một giao thức xác thực sẽ chạy trước khi hai bên truyền thông thực hiện một số giao thức khác (ví dụ: giao thức truyền dữ liệu đáng tin cậy, giao thức trao đổi thông tin định tuyến, hoặc giao thức email). Giao thức xác thực trước hết thiết lập danh tính của các bên để bên kia hài lòng; chỉ sau khi xác thực, các bên mới bắt tay vào công việc hiện tại.

Như trong trường hợp phát triển giao thức truyền dữ liệu đáng tin cậy (rdt) của chúng ta trong Chương 3, chúng ta sẽ thấy việc phát triển các phiên bản khác nhau của một giao thức xác thực tại đây là hữu ích, mà chúng ta sẽ gọi là ap (giao thức xác thực), và tìm các lỗ hổng trong từng phiên bản khi tiến hành. (Nếu bạn thích quá trình tiến hóa từng bước của một thiết kế như vậy, bạn cũng có thể thích \[Bryant 1988\], kể về câu chuyện hư cấu giữa các nhà thiết kế của một hệ thống xác thực mạng mở, và sự khám phá của họ về nhiều vấn đề tinh vi liên quan.)

Giả sử rằng Alice cần xác thực bản thân với Bob. Có lẽ giao thức xác thực đơn giản nhất mà chúng ta có thể tưởng tượng là Alice chỉ gửi một tin nhắn cho Bob nói rằng cô ấy là Alice. Giao thức này được trình bày trong Hình 8.15. Khiếm khuyết ở đây là rõ ràng---không có cách nào để Bob thực sự biết rằng người gửi tin nhắn "Tôi là Alice" thực sự là Alice. Ví dụ, Trudy (kẻ xâm nhập) cũng có thể gửi một tin nhắn như vậy.

*Hình 8.15 ♦ Giao thức ap1.0 và một kịch bản thất bại*

Alice

Tôi là Alice

Bob

Trudy Trudy

Alice

Tôi là Alice

Bob

Giao thức xác thực ap2.0

Nếu Alice có một địa chỉ mạng nổi tiếng (ví dụ, một địa chỉ IP) mà từ đó cô ấy luôn giao tiếp, Bob có thể cố gắng xác thực Alice bằng cách xác minh rằng địa chỉ nguồn trên gói tin IP mang thông điệp xác thực khớp với địa chỉ nổi tiếng của Alice. Trong trường hợp này, Alice sẽ được xác thực. Điều này có thể ngăn một kẻ xâm nhập rất thiếu kinh nghiệm về mạng mạo danh Alice, nhưng nó sẽ không ngăn được sinh viên quyết tâm học quyển sách này, hoặc nhiều người khác!

From our study of the network and data link layers, we know that it is not that hard (for example, if one had access to the operating system code and could build one's own operating system kernel, as is the case with Linux and several other freely available operating systems) to create an IP datagram, put whatever IP source address we want (for example, Alice's well-known IP address) into the IP datagram, and send the datagram over the link-layer protocol to the first-hop router. From then on, the incorrectly source-addressed datagram would be dutifully forwarded to Bob. This approach, shown in Figure 8.16, is a form of IP spoofing. IP spoofing can be avoided if Trudy's first-hop router is configured to forward only datagrams containing Trudy's IP source address \[RFC 2827\]. However, this capability is not universally deployed or enforced. Bob would thus be foolish to assume that Trudy's network manager (who might be Trudy herself) had configured Trudy's first-hop router to forward only appropriately addressed datagrams.

Giao thức xác thực ap3.0

Một phương pháp cổ điển để xác thực là sử dụng mật khẩu bí mật. Mật khẩu là một bí mật được chia sẻ giữa người xác thực và người được xác thực. Gmail, Facebook, telnet, FTP và nhiều dịch vụ khác sử dụng xác thực bằng mật khẩu. Trong giao thức ap3.0, Alice do đó gửi mật khẩu bí mật của cô ấy cho Bob, như minh họa trong Hình 8.17.

*Hình 8.16 ♦ Giao thức ap2.0 và một kịch bản thất bại*

Alice

Tôi là Alice

Địa chỉ IP của Alice

Bob

Trudy

Alice

Tôi là Alice

Địa chỉ IP của Alice

Bob

Trudy

Vì mật khẩu được sử dụng rộng rãi, chúng ta có thể nghi ngờ rằng giao thức ap3.0 khá an toàn. Nếu vậy, chúng ta sẽ sai! Lỗ hổng bảo mật ở đây là rõ ràng. Nếu Trudy nghe lén giao tiếp của Alice, cô ấy có thể biết được mật khẩu của Alice. Để bạn không nghĩ điều này là ít khả năng, hãy xem xét thực tế rằng khi bạn Telnet đến một máy khác và đăng nhập, mật khẩu đăng nhập được gửi không mã hóa đến máy chủ Telnet. Ai đó kết nối với LAN của máy khách hoặc máy chủ Telnet có thể dò gói (đọc và lưu) tất cả các gói được truyền trên LAN và do đó đánh cắp mật khẩu đăng nhập. Trên thực tế, đây là một phương pháp nổi tiếng để đánh cắp mật khẩu (xem, ví dụ, \[Jimenez 1997\]). Mối đe dọa như vậy rõ ràng là rất thực tế, vì vậy ap3.0 rõ ràng không thể sử dụng được.

Giao thức xác thực ap3.1

Ý tưởng tiếp theo của chúng tôi để sửa ap3.0 là tự nhiên mã hóa mật khẩu. Bằng cách mã hóa mật khẩu, chúng ta có thể ngăn Trudy biết mật khẩu của Alice. Nếu chúng ta giả sử rằng Alice và Bob chia sẻ một khóa bí mật đối xứng, KA-B, thì Alice có thể mã hóa mật khẩu và gửi thông điệp nhận dạng của mình, "Tôi là Alice," cùng với mật khẩu đã được mã hóa tới Bob. Sau đó, Bob giải mã mật khẩu và, giả sử mật khẩu đúng, xác thực Alice. Bob cảm thấy yên tâm khi xác thực Alice vì Alice không chỉ biết mật khẩu mà còn biết giá trị của khóa bí mật chung cần thiết để mã hóa mật khẩu. Hãy gọi giao thức này là ap3.1.

Mặc dù đúng là ap3.1 ngăn Trudy học được mật khẩu của Alice, việc sử dụng mật mã ở đây không giải quyết được vấn đề xác thực. Bob bị ảnh hưởng

*Hình 8.17 ♦ Giao thức ap3.0 và một kịch bản thất bại*

Alice

Tôi là Alice, mật khẩu

Được

Bob

Trudy

Alice

Tôi là Alice,

mật khẩu

Được

Bob

Trudy

Máy ghi băng

Chìa khóa:

Về một cuộc tấn công phát lại: Trudy chỉ cần nghe lén giao tiếp của Alice, ghi lại phiên bản mật khẩu đã được mã hóa, và phát lại phiên bản mật khẩu đã mã hóa cho Bob để giả vờ rằng cô ấy là Alice. Việc sử dụng mật khẩu mã hóa trong ap3.1 không làm cho tình huống khác biệt rõ ràng so với giao thức ap3.0 trong Hình 8.17.

Giao thức xác thực ap4.0

The failure scenario in Figure 8.17 resulted from the fact that Bob could not distinguish between the original authentication of Alice and the later playback of Alice's original authentication. That is, Bob could not tell if Alice was live (that is, was currently really on the other end of the connection) or whether the messages he was receiving were a recorded playback of a previous authentication of Alice. The very (very) observant reader will recall that the three-way TCP handshake protocol needed to address the same problem---the server side of a TCP connection did not want to accept a connection if the received SYN segment was an old copy (retransmission) of a SYN segment from an earlier connection. How did the TCP server side solve the problem of determining whether the client was really live? It chose an initial sequence number that had not been used in a very long time, sent that number to the client, and then waited for the client to respond with an ACK segment containing that number. We can adopt the same idea here for authentication purposes.

Một số nonce là một con số mà một giao thức chỉ sử dụng một lần trong suốt đời. Nghĩa là, khi một giao thức sử dụng một nonce, nó sẽ không bao giờ dùng lại con số đó. Giao thức ap4.0 của chúng tôi sử dụng nonce như sau:

1\. Alice gửi tin nhắn "I am Alice" cho Bob. 2. Bob chọn một số ngẫu nhiên, R, và gửi nó cho Alice. 3. Alice mã hóa số ngẫu nhiên bằng khóa bí mật đối xứng của Alice và Bob, KA-B, và

gửi nonce đã được mã hóa, KA-B (R), trở lại cho Bob. Như trong giao thức ap3.1, thực tế rằng Alice biết KA-B và sử dụng nó để mã hóa một giá trị cho phép Bob biết rằng thông điệp anh nhận được được tạo ra bởi Alice. Nonce được sử dụng để đảm bảo rằng Alice đang hoạt động. 4. Bob giải mã thông điệp nhận được. Nếu nonce đã giải mã bằng với nonce mà anh ấy

gửi Alice, sau đó Alice được xác thực.

Giao thức ap4.0 được minh họa trong Hình 8.18. Bằng cách sử dụng giá trị chỉ dùng một lần trong đời, R, và sau đó kiểm tra giá trị trả về, KA-B (R), Bob có thể chắc chắn rằng Alice vừa là người mà cô ấy tự nhận (vì cô ấy biết giá trị khóa bí mật cần thiết để mã hóa R) vừa đang trực tuyến (vì cô ấy đã mã hóa nonce, R, mà Bob vừa tạo ra).

Việc sử dụng một số nonce và mã hóa khóa đối xứng tạo thành cơ sở của ap4.0. Một câu hỏi tự nhiên là liệu chúng ta có thể sử dụng số nonce và mã hóa khóa công khai (thay vì mã hóa khóa đối xứng) để giải quyết vấn đề xác thực hay không. Vấn đề này được nghiên cứu trong các bài tập ở cuối chương.

**8.5 Bảo mật Email**

Trong các phần trước, chúng ta đã xem xét các vấn đề cơ bản trong an ninh mạng, bao gồm mật mã khóa đối xứng và khóa công khai, xác thực điểm cuối, phân phối khóa, tính toàn vẹn của thông điệp và chữ ký số. Bây giờ chúng ta sẽ xem xét cách các công cụ này được sử dụng để cung cấp an ninh trên Internet.

Thú vị là, có thể cung cấp các dịch vụ bảo mật ở bất kỳ bốn lớp hàng đầu của ngăn xếp giao thức Internet. Khi bảo mật được cung cấp cho một giao thức lớp ứng dụng cụ thể, ứng dụng sử dụng giao thức đó sẽ hưởng một hoặc nhiều dịch vụ bảo mật, chẳng hạn như tính bí mật, xác thực hoặc tính toàn vẹn. Khi bảo mật được cung cấp cho một giao thức lớp vận chuyển, tất cả các ứng dụng sử dụng giao thức đó đều hưởng các dịch vụ bảo mật của giao thức vận chuyển. Khi bảo mật được cung cấp ở lớp mạng trên cơ sở từng host, tất cả các phân đoạn lớp vận chuyển (và do đó tất cả dữ liệu lớp ứng dụng) đều hưởng các dịch vụ bảo mật của lớp mạng. Khi bảo mật được cung cấp trên cơ sở liên kết, thì dữ liệu trong tất cả các khung đi qua liên kết sẽ nhận các dịch vụ bảo mật của liên kết.

Trong các Mục 8.5 đến 8.8, chúng tôi xem xét cách các công cụ bảo mật đang được sử dụng trong các lớp ứng dụng, truyền tải, mạng và liên kết. Phù hợp với cấu trúc chung của cuốn sách này, chúng tôi bắt đầu từ đỉnh của ngăn xếp giao thức và thảo luận về bảo mật tại lớp ứng dụng. Cách tiếp cận của chúng tôi là sử dụng một ứng dụng cụ thể, thư điện tử, làm nghiên cứu điển hình về bảo mật lớp ứng dụng. Sau đó, chúng tôi sẽ di chuyển xuống ngăn xếp giao thức. Chúng tôi sẽ xem xét giao thức TLS (cung cấp bảo mật tại lớp truyền tải), IPsec (cung cấp bảo mật tại lớp mạng), và bảo mật của giao thức mạng LAN không dây IEEE 802.11.

Bạn có thể đang tự hỏi tại sao chức năng bảo mật lại được cung cấp ở nhiều lớp khác nhau trên Internet. Liệu có phải chỉ cần cung cấp chức năng bảo mật ở lớp mạng là đủ và xong chuyện? Có hai câu trả lời cho câu hỏi này. Thứ nhất, mặc dù bảo mật ở lớp mạng có thể cung cấp "phủ sóng toàn bộ" bằng cách mã hóa tất cả dữ liệu trong các gói dữ liệu (tức là, tất cả các đoạn ở lớp vận chuyển)

*Hình 8.18 ♦ Giao thức ap4.0 và một kịch bản thất bại*

Alice

R

KA--B(R)

Tôi là Alice

Bob

và bằng cách xác thực tất cả các địa chỉ nguồn IP, nó không thể cung cấp bảo mật ở mức người dùng. Ví dụ, một trang thương mại điện tử không thể dựa vào bảo mật ở lớp IP để xác thực một khách hàng đang mua hàng tại trang thương mại điện tử. Do đó, cần có chức năng bảo mật ở các lớp cao hơn cũng như bao phủ tổng thể ở các lớp thấp hơn. Thứ hai, việc triển khai các dịch vụ Internet mới, bao gồm cả dịch vụ bảo mật, thường dễ dàng hơn ở các lớp cao hơn của ngăn xếp giao thức. Trong khi chờ đợi bảo mật được triển khai rộng rãi ở lớp mạng, điều này có lẽ vẫn còn nhiều năm nữa, nhiều nhà phát triển ứng dụng "chỉ làm thôi" và đưa chức năng bảo mật vào các ứng dụng yêu thích của họ. Một ví dụ kinh điển là Pretty Good Privacy (PGP), cung cấp e-mail an toàn (sẽ được thảo luận sau trong phần này). Chỉ yêu cầu mã ứng dụng khách và máy chủ, PGP là một trong những công nghệ bảo mật đầu tiên được sử dụng rộng rãi trên Internet.

**8.5.1 Email An Toàn**

Chúng ta hiện nay sử dụng các nguyên tắc mật mã trong các Mục 8.2 đến 8.3 để tạo ra một hệ thống email an toàn. Chúng ta tạo thiết kế cấp cao này một cách tăng dần, ở mỗi bước giới thiệu các dịch vụ bảo mật mới. Khi thiết kế một hệ thống email an toàn, hãy nhớ ví dụ có phần gay gắt được giới thiệu trong Mục 8.1---mối tình giữa Alice và Bob. Hãy tưởng tượng rằng Alice muốn gửi một tin nhắn email cho Bob, và Trudy muốn xâm nhập.

Before plowing ahead and designing a secure e-mail system for Alice and Bob, we should consider which security features would be most desirable for them. First and foremost is confidentiality. As discussed in Section 8.1, neither Alice nor Bob wants Trudy to read Alice's e-mail message. The second feature that Alice and Bob would most likely want to see in the secure e-mail system is sender authentication. In particular, when Bob receives the message "I don't love you anymore. I never want to see you again. Formerly yours, Alice," he would naturally want to be sure that the message came from Alice and not from Trudy. Another feature that the two lovers would appreciate is message integrity, that is, assurance that the message Alice sends is not modified while en route to Bob. Finally, the e-mail system should provide receiver authentication; that is, Alice wants to make sure that she is indeed sending the letter to Bob and not to someone else (for example, Trudy) who is impersonating Bob.

Vì vậy, hãy bắt đầu bằng việc giải quyết mối quan tâm hàng đầu, đó là tính bảo mật. Cách trực tiếp nhất để đảm bảo tính bảo mật là Alice mã hóa thông điệp bằng công nghệ khóa đối xứng (như DES hoặc AES) và Bob giải mã thông điệp khi nhận được. Như đã thảo luận trong Mục 8.2, nếu khóa đối xứng đủ dài, và nếu chỉ Alice và Bob có khóa, thì sẽ cực kỳ khó cho bất kỳ ai khác (bao gồm cả Trudy) đọc được thông điệp. Mặc dù cách tiếp cận này đơn giản, nhưng nó có khó khăn cơ bản mà chúng ta đã thảo luận trong Mục 8.2--- đó là phân phối khóa đối xứng sao cho chỉ Alice và Bob có bản sao của khóa. Vì vậy, chúng ta tự nhiên cân nhắc một phương pháp thay thế---mã hóa khóa công khai (sử dụng, ví dụ, RSA).

Phương pháp khóa công khai, Bob công khai khóa công khai của mình (ví dụ, trên một máy chủ khóa công khai hoặc trên trang Web cá nhân của anh ấy), Alice mã hóa tin nhắn của mình bằng khóa công khai của Bob, và cô ấy gửi tin nhắn đã mã hóa đến địa chỉ e-mail của Bob. Khi Bob nhận được tin nhắn, anh ấy chỉ cần giải mã nó bằng khóa riêng của mình. Giả sử rằng Alice chắc chắn rằng khóa công khai là khóa công khai của Bob, phương pháp này là một cách tuyệt vời để đảm bảo tính bảo mật mong muốn. Tuy nhiên, một vấn đề là mã hóa khóa công khai tương đối kém hiệu quả, đặc biệt đối với các tin nhắn dài.

Để khắc phục vấn đề về hiệu suất, hãy sử dụng một khóa phiên (được thảo luận trong Mục 8.2.2). Cụ thể, Alice (1) chọn một khóa phiên đối xứng ngẫu nhiên, KS, (2) mã hóa thông điệp của cô ấy, m, bằng khóa đối xứng, (3) mã hóa khóa đối xứng bằng khóa công khai của Bob, KB +, (4) nối thông điệp đã mã hóa và khóa đối xứng đã mã hóa để tạo thành một "gói", và (5) gửi gói này đến địa chỉ email của Bob. Các bước được minh họa trong Hình 8.19. (Trong hình này và các hình tiếp theo, dấu "+" trong vòng tròn biểu thị nối chuỗi và dấu "-" trong vòng tròn biểu thị tách chuỗi.) Khi Bob nhận được gói, anh ấy (1) sử dụng khóa riêng của mình, K-

B, để lấy khóa đối xứng, KS, và (2) sử dụng khóa đối xứng KS để giải mã thông điệp m.

Sau khi đã thiết kế một hệ thống e-mail an toàn cung cấp tính bảo mật, bây giờ chúng ta hãy thiết kế một hệ thống khác cung cấp cả xác thực người gửi và tính toàn vẹn của thông điệp. Chúng ta sẽ giả sử, trước mắt, rằng Alice và Bob không còn quan tâm đến bảo mật (họ muốn chia sẻ cảm xúc của mình với mọi người!), và chỉ quan tâm đến xác thực người gửi và tính toàn vẹn của thông điệp. Để thực hiện nhiệm vụ này, chúng ta sử dụng chữ ký số và tổng kiểm tra thông điệp, như được mô tả trong Mục 8.3. Cụ thể, Alice (1) áp dụng một hàm băm, H (ví dụ, MD5), lên thông điệp của cô ấy, m, để thu được tổng kiểm tra thông điệp, (2) ký kết quả của hàm băm với khóa riêng của cô ấy, K-

A, để tạo chữ ký số, (3) nối thông điệp gốc (chưa mã hóa) với chữ ký để tạo thành một gói, và (4) gửi gói này đến địa chỉ email của Bob. Khi Bob nhận được gói, anh ấy (1) áp dụng khóa công khai của Alice, K+

A, tới chữ ký

*Hình 8.19 ♦ Alice đã sử dụng một khóa phiên đối xứng, KS, để gửi một bí mật*

thư điện tử gửi Bob

KS(.) KS(.) KS(m) KS(m)

KS

KS

KB

+(.)

KB

+(KS) KB

+(KS)

m m

\+ -- Internet

KB

--(.)

Alice gửi thư điện tử m Bob nhận thư điện tử m

bản tin tóm tắt và (2) so sánh kết quả của phép toán này với giá trị băm của chính anh ta, H, của thông điệp. Các bước được minh họa trong Hình 8.20. Như đã thảo luận trong Mục 8.3, nếu hai kết quả giống nhau, Bob có thể khá tự tin rằng thông điệp đến từ Alice và không bị thay đổi.

Bây giờ hãy xem xét việc thiết kế một hệ thống e-mail cung cấp tính bảo mật, xác thực người gửi và toàn vẹn thông điệp. Điều này có thể được thực hiện bằng cách kết hợp các quy trình trong Hình 8.19 và 8.20. Alice trước tiên tạo một gói sơ bộ, giống hệt như trong Hình 8.20, bao gồm thông điệp gốc của cô cùng với một băm được ký số của thông điệp. Cô sau đó coi gói sơ bộ này như một thông điệp riêng và gửi thông điệp mới này qua các bước của người gửi trong Hình 8.19, tạo ra một gói mới được gửi đến Bob. Các bước được Alice áp dụng được thể hiện trong Hình 8.21. Khi Bob nhận được gói, anh trước tiên áp dụng phía của mình trong Hình 8.19 và sau đó

*Hình 8.20 ♦ Sử dụng hàm băm và chữ ký số để cung cấp*

xác thực người gửi và tính toàn vẹn của tin nhắn

H(.) KA

--(.) KA

+(.) KA

--(H(m)) KA

--(H(m)) m

m

m

\+ -- Internet

Alice gửi thư điện tử m Bob nhận thư điện tử m

H(.)

So sánh

*Hình 8.21 ♦ Alice sử dụng mật mã khóa đối xứng, khóa công khai*

mật mã học, một hàm băm, và một chữ ký số để cung cấp tính bí mật, xác thực người gửi, và toàn vẹn thông điệp

H(.) KA

--(.)

KS(.)

KS

KA

--(H(m)) m

m

\+

\+ đến Internet

KB

+(.)

phía của Hình 8.20. Cần rõ ràng rằng thiết kế này đạt được mục tiêu cung cấp tính bảo mật, xác thực người gửi và tính toàn vẹn của tin nhắn. Lưu ý rằng, trong sơ đồ này, Alice sử dụng mã hóa khóa công khai hai lần: một lần với khóa riêng của chính cô ấy và một lần với khóa công khai của Bob. Tương tự, Bob cũng sử dụng mã hóa khóa công khai hai lần --- một lần với khóa riêng của mình và một lần với khóa công khai của Alice.

Thiết kế e-mail bảo mật được trình bày trong Hình 8.21 có thể cung cấp mức độ an toàn thỏa đáng cho hầu hết người dùng e-mail trong hầu hết các trường hợp. Tuy nhiên, vẫn còn một vấn đề quan trọng cần được giải quyết. Thiết kế trong Hình 8.21 yêu cầu Alice phải lấy khóa công khai của Bob, và yêu cầu Bob phải lấy khóa công khai của Alice. Việc phân phối các khóa công khai này không phải là vấn đề đơn giản. Ví dụ, Trudy có thể giả mạo thành Bob và đưa cho Alice khóa công khai của cô ấy trong khi nói rằng đó là khóa công khai của Bob, cho phép cô ấy nhận được tin nhắn dành cho Bob. Như chúng ta đã học trong Phần 8.3, một phương pháp phổ biến để phân phối khóa công khai một cách an toàn là chứng thực các khóa công khai bằng cách sử dụng một CA.

**8.5.2 PGP**

Được viết bởi Phil Zimmermann vào năm 1991, Pretty Good Privacy (PGP) là một ví dụ tốt về một sơ đồ mã hóa email \[PGP 2020\]. Thiết kế của PGP về cơ bản giống như thiết kế được trình bày trong Hình 8.21. Tùy thuộc vào phiên bản, phần mềm PGP sử dụng MD5 hoặc SHA để tính toán bản tóm tắt thông điệp; CAST, triple-DES, hoặc IDEA cho mã hóa khóa đối xứng; và RSA cho mã hóa khóa công khai.

Khi PGP được cài đặt, phần mềm sẽ tạo một cặp khóa công khai cho người dùng. Khóa công khai có thể được đăng trên trang Web của người dùng hoặc đặt trên một máy chủ khóa công khai. Khóa riêng tư được bảo vệ bằng việc sử dụng mật khẩu. Mật khẩu phải được nhập mỗi khi người dùng truy cập khóa riêng tư. PGP cho phép người dùng lựa chọn việc ký số thông điệp, mã hóa thông điệp, hoặc cả hai việc ký số và mã hóa. Hình 8.22 hiển thị một thông điệp đã được ký bởi PGP. Thông điệp này xuất hiện sau tiêu đề MIME. Dữ liệu được mã hóa trong thông điệp là K-

A (H(m)), tức là, bản tóm tắt thông điệp được ký số. Như chúng ta đã thảo luận ở trên, để Bob có thể xác minh tính toàn vẹn của thông điệp, anh ấy cần phải có quyền truy cập vào khóa công khai của Alice.

*Hình 8.22 ♦ Một tin nhắn được ký PGP*

\-\-\-\--BEGIN PGP SIGNED MESSAGE\-\-\-\-- Hash: SHA1 Bob: Tối nay tôi có thể gặp bạn không? Với tất cả đam mê, Alice \-\-\-\--BEGIN PGP SIGNATURE\-\-\-\-- Version: PGP for Personal Privacy 5.0 Charset: noconv yhHJRHhGJGhgg/12EpJ+lo8gE4vB3mqJhFEvZP9t6n7G6m5Gw2 \-\-\-\--END PGP SIGNATURE\-\-\-\--

Hình 8.23 cho thấy một thông điệp PGP bí mật. Thông điệp này cũng xuất hiện sau tiêu đề MIME. Tất nhiên, thông điệp văn bản thuần túy không được bao gồm trong thông điệp e-mail bí mật. Khi một người gửi (chẳng hạn như Alice) muốn cả tính bảo mật và tính toàn vẹn, PGP sẽ chứa một thông điệp giống như Hình 8.23 trong thông điệp của Hình 8.22.

PGP cũng cung cấp một cơ chế để chứng thực khóa công khai, nhưng cơ chế này khá khác so với CA thông thường. Khóa công khai PGP được chứng thực bằng một mạng lưới tin cậy. Alice có thể tự chứng thực bất kỳ cặp khóa/tên người dùng nào khi cô ấy tin rằng cặp đó thực sự thuộc về nhau. Ngoài ra, PGP cho phép Alice nói rằng cô ấy tin tưởng một người dùng khác để đảm bảo tính xác thực của nhiều khóa hơn. Một số người dùng PGP ký khóa của nhau bằng cách tổ chức các bữa tiệc ký khóa. Người dùng tập trung trực tiếp, trao đổi khóa công khai, và chứng thực khóa của nhau bằng cách ký chúng với khóa riêng của mình.

**8.6 Bảo mật các kết nối TCP: TLS**

Trong phần trước, chúng ta đã thấy cách các kỹ thuật mật mã có thể cung cấp tính bảo mật, tính toàn vẹn dữ liệu và xác thực đầu cuối cho một ứng dụng cụ thể, đó là e-mail. Trong phần này, chúng ta sẽ hạ xuống một tầng trong ngăn xếp giao thức và xem xét cách mật mã có thể nâng cao TCP với các dịch vụ bảo mật, bao gồm tính bảo mật, tính toàn vẹn dữ liệu và xác thực đầu cuối. Phiên bản nâng cao của TCP này thường được gọi là Transport Layer Security (TLS), đã được chuẩn hóa bởi IETF \[RFC 4346\]. Một phiên bản trước đó và tương tự của giao thức này là SSL phiên bản 3.

Giao thức SSL ban đầu được thiết kế bởi Netscape, nhưng những ý tưởng cơ bản về bảo mật TCP đã xuất hiện trước công trình của Netscape (ví dụ, xem Woo \[Woo 1994\]). Kể từ khi ra đời, SSL và phiên bản kế tiếp của nó là TLS đã được triển khai rộng rãi. TLS được tất cả các trình duyệt Web và máy chủ Web phổ biến hỗ trợ, và nó được sử dụng bởi Gmail cũng như hầu hết các trang thương mại điện tử trên Internet (bao gồm Amazon, eBay và TaoBao). Hàng trăm tỷ đô la được chi cho TLS mỗi năm. Trên thực tế, nếu bạn từng mua bất cứ thứ gì qua Internet bằng thẻ tín dụng của mình, việc truyền thông tin giữa trình duyệt của bạn và máy chủ cho giao dịch này gần như chắc chắn đã diễn ra qua TLS. (Bạn có thể nhận biết rằng TLS đang được trình duyệt của bạn sử dụng khi URL bắt đầu bằng https: thay vì http.)

*Hình 8.23 ♦ Một tin nhắn PGP bí mật*

\-\-\-\--BEGIN PGP MESSAGE\-\-\-\-- Phiên bản: PGP for Personal Privacy 5.0 u2R4d+/jKmn8Bc5+hgDsqAewsDfrGdszX68liKm5F6Gc4sDfcXyt RfdS10juHgbcfDssWe7/K=lKhnMikLo0+1/BvcX4t==Ujk9PbcD4 Thdf2awQfgHbnmKlok8iy6gThlp \-\-\-\--END PGP MESSAGE

Để hiểu được nhu cầu về TLS, hãy cùng xem qua một tình huống thương mại Internet điển hình. Bob đang lướt Web và đến trang web của Alice Incorporated, nơi bán nước hoa. Trang web của Alice Incorporated hiển thị một biểu mẫu mà Bob cần điền loại nước hoa và số lượng mong muốn, địa chỉ của anh ấy, và số thẻ thanh toán. Bob nhập thông tin này, nhấn Gửi, và mong nhận được các chai nước hoa đã mua (thông qua thư bưu điện thông thường); anh ấy cũng mong nhận được hóa đơn cho đơn hàng của mình trong sao kê thẻ thanh toán tiếp theo. Tất cả nghe có vẻ tốt, nhưng nếu không áp dụng các biện pháp bảo mật, Bob có thể gặp phải một vài bất ngờ.

• Nếu không sử dụng bảo mật (mã hóa), kẻ tấn công có thể chặn đơn hàng của Bob và lấy thông tin thẻ thanh toán của anh ấy. Kẻ tấn công sau đó có thể thực hiện các giao dịch mua hàng với chi phí của Bob. • Nếu không sử dụng tính toàn vẹn dữ liệu, một kẻ tấn công có thể sửa đổi đơn hàng của Bob, khiến anh ấy mua gấp mười lần số lượng nước hoa mong muốn. • Cuối cùng, nếu không sử dụng xác thực máy chủ, một máy chủ có thể hiển thị logo nổi tiếng của Alice Incorporated trong khi thực tế trang web được duy trì bởi Trudy, người đang giả mạo Alice Incorporated. Sau khi nhận được đơn hàng của Bob, Trudy có thể lấy tiền của Bob và bỏ chạy. Hoặc Trudy có thể thực hiện hành vi đánh cắp danh tính bằng cách thu thập tên, địa chỉ và số thẻ tín dụng của Bob.

TLS giải quyết những vấn đề này bằng cách nâng cao TCP với tính bảo mật, tính toàn vẹn dữ liệu, xác thực máy chủ và xác thực khách hàng.

TLS thường được sử dụng để cung cấp bảo mật cho các giao dịch diễn ra qua HTTP. Tuy nhiên, vì TLS bảo mật TCP, nó có thể được sử dụng bởi bất kỳ ứng dụng nào chạy trên TCP. TLS cung cấp một Giao diện Lập trình Ứng dụng (API) đơn giản với các socket, điều này tương tự và tương đồng với API của TCP. Khi một ứng dụng muốn sử dụng TLS, ứng dụng đó bao gồm các lớp/thư viện SSL. Như thể hiện trong Hình 8.24, mặc dù về kỹ thuật TLS nằm trong tầng ứng dụng, từ góc nhìn của nhà phát triển nó là một giao thức truyền tải cung cấp các dịch vụ của TCP được nâng cấp với các dịch vụ bảo mật.

*Hình 8.24 ♦ Mặc dù TLS về mặt kỹ thuật nằm trong tầng ứng dụng,*

từ quan điểm của nhà phát triển, đây là một giao thức lớp vận chuyển

TCP

tầng con TLS

IP

Ứng dụng

Lớp ứng dụng

TCP được cải thiện với TLS

ổ cắm

ổ cắm

TCP

IP

Ứng dụng

TCP API

ổ cắm

**8.6.1 Bức tranh tổng thể**

Chúng ta bắt đầu bằng việc mô tả một phiên bản đơn giản hóa của TLS, một phiên bản sẽ cho phép chúng ta hiểu tổng quan về lý do và cách thức của TLS. Chúng ta sẽ gọi phiên bản đơn giản hóa này của TLS là "gần như TLS." Sau khi mô tả gần như TLS, trong phần tiếp theo chúng ta sẽ mô tả TLS thật sự, bổ sung các chi tiết. Gần như TLS (và TLS) có ba giai đoạn: bắt tay, tạo khóa, và truyền dữ liệu. Bây giờ chúng ta sẽ mô tả ba giai đoạn này cho một phiên giao tiếp giữa một client (Bob) và một server (Alice), với Alice có một cặp khóa riêng/công khai và một chứng chỉ liên kết danh tính của cô ấy với khóa công khai của cô.

Handshake

Trong giai đoạn bắt tay, Bob cần (a) thiết lập một kết nối TCP với Alice, (b) xác minh rằng Alice thực sự là Alice, và (c) gửi cho Alice một khóa bí mật chính, khóa này sẽ được cả Alice và Bob sử dụng để tạo tất cả các khóa đối xứng mà họ cần cho phiên TLS. Ba bước này được minh họa trong Hình 8.25. Lưu ý rằng một khi kết nối TCP được thiết lập, Bob gửi cho Alice một thông điệp chào. Alice sau đó phản hồi bằng chứng chỉ của cô ấy, trong đó chứa khóa công khai của cô ấy. Như đã thảo luận trong Mục 8.3, vì chứng chỉ đã được một CA chứng thực, Bob biết chắc chắn rằng khóa công khai trong chứng chỉ thuộc về Alice. Bob sau đó tạo một Khóa Bí mật Chính (Master Secret, MS) (khóa này chỉ được sử dụng cho phiên TLS này), mã hóa MS bằng khóa công khai của Alice để tạo

*Hình 8.25 ♦ Cái bắt tay gần như TLS, bắt đầu với một TCP*

kết nối

TCP DANH TỪ

TCP/SYNACK

Giải mã EMS với KA

-- để có được MS

EMS = KA

+(MS)

TCP XÁC NHẬN

TLS xin chào

chứng chỉ

\(b\)

\(a\)

\(c\) Tạo Master

Bí mật (MS)

Mật khẩu chính được mã hóa (EMS), và gửi EMS này cho Alice. Alice giải mã EMS bằng khóa riêng của cô ấy để lấy MS. Sau giai đoạn này, cả Bob và Alice (và không ai khác) đều biết mật khẩu chính cho phiên TLS này.

Phái sinh khóa

Về nguyên tắc, MS, hiện nay được chia sẻ bởi Bob và Alice, có thể được sử dụng làm khóa phiên đối xứng cho tất cả các việc mã hóa và kiểm tra tính toàn vẹn dữ liệu tiếp theo. Tuy nhiên, thường được coi là an toàn hơn cho Alice và Bob khi mỗi người sử dụng các khóa mã hóa khác nhau, và cũng sử dụng các khóa khác nhau cho việc mã hóa và kiểm tra tính toàn vẹn. Do đó, cả Alice và Bob đều sử dụng MS để tạo ra bốn khóa:

• EB = khóa mã hóa phiên cho dữ liệu gửi từ Bob đến Alice • MB = khóa HMAC phiên cho dữ liệu gửi từ Bob đến Alice, trong đó HMAC \[RFC 2104\] là mã xác thực thông điệp băm chuẩn hóa (MAC) mà chúng ta đã gặp trong mục 8.3.2 • EA = khóa mã hóa phiên cho dữ liệu gửi từ Alice đến Bob • MA = khóa HMAC phiên cho dữ liệu gửi từ Alice đến Bob

Alice và Bob mỗi người tạo ra bốn khóa từ MS. Điều này có thể thực hiện đơn giản bằng cách chia MS thành bốn khóa. (Nhưng trên thực tế TLS nó phức tạp hơn một chút, như chúng ta sẽ thấy.) Vào cuối giai đoạn tạo khóa, cả Alice và Bob đều có đủ bốn khóa. Hai khóa mã hóa sẽ được sử dụng để mã hóa dữ liệu; hai khóa HMAC sẽ được sử dụng để xác minh tính toàn vẹn của dữ liệu.

Chuyển dữ liệu

Giờ đây, Alice và Bob chia sẻ bốn khóa phiên giống nhau (EB, MB, EA và MA), họ có thể bắt đầu gửi dữ liệu bảo mật cho nhau qua kết nối TCP. Vì TCP là giao thức luồng byte nên cách tiếp cận tự nhiên sẽ là TLS mã hóa dữ liệu ứng dụng một cách nhanh chóng và sau đó chuyển dữ liệu được mã hóa nhanh chóng tới TCP. Nhưng nếu làm điều này, chúng ta sẽ đặt HMAC ở đâu để kiểm tra tính toàn vẹn? Chúng tôi chắc chắn không muốn đợi đến cuối phiên TCP để xác minh tính toàn vẹn của tất cả dữ liệu của Bob đã được gửi trong toàn bộ phiên! Để giải quyết vấn đề này, TLS chia luồng dữ liệu thành các bản ghi, gắn thêm HMAC vào mỗi bản ghi để kiểm tra tính toàn vẹn, sau đó mã hóa bản ghi+HMAC. Để tạo HMAC, Bob nhập dữ liệu bản ghi cùng với khóa MB vào hàm băm, như được thảo luận trong Phần 8.3. Để mã hóa bản ghi gói+HMAC, Bob sử dụng khóa mã hóa phiên EB của mình. Sau đó, gói mã hóa này được chuyển tới TCP để truyền qua Internet.

Mặc dù cách tiếp cận này tiến xa, nhưng nó vẫn chưa hoàn toàn chắc chắn khi nói đến việc đảm bảo tính toàn vẹn dữ liệu cho toàn bộ luồng tin nhắn. Cụ thể, giả sử Trudy là một người ở giữa và có khả năng chèn, xóa và thay thế các đoạn trong luồng các đoạn TCP được gửi giữa Alice và Bob. Trudy, cho

ví dụ, có thể chụp hai phân đoạn được gửi bởi Bob, đảo ngược thứ tự của các phân đoạn, điều chỉnh các số thứ tự của chuỗi TCP (điều này không được mã hóa), và sau đó gửi hai phân đoạn đảo ngược thứ tự đó cho Alice. Giả sử mỗi phân đoạn TCP bao bọc chính xác một bản ghi, bây giờ hãy cùng xem cách Alice xử lý các phân đoạn này.

1\. TCP chạy trong Alice sẽ nghĩ mọi thứ đều ổn và vượt qua hai bản ghi

tới lớp phụ TLS. 2. TLS trong Alice sẽ giải mã hai bản ghi. 3. TLS trong Alice sẽ sử dụng HMAC trong mỗi bản ghi để xác minh tính toàn vẹn dữ liệu

của hai bản ghi. 4. TLS sau đó sẽ truyền các luồng byte đã giải mã của hai bản ghi đến

lớp ứng dụng; nhưng luồng byte đầy đủ nhận được bởi Alice sẽ không theo đúng thứ tự do các bản ghi bị đảo ngược!

Bạn được khuyến khích đi qua các kịch bản tương tự khi Trudy xóa các phân đoạn hoặc khi Trudy phát lại các phân đoạn.

Giải pháp cho vấn đề này, như bạn có thể đoán, là sử dụng số thứ tự. TLS thực hiện điều này như sau. Bob duy trì một bộ đếm số thứ tự, bắt đầu từ số không và tăng lên cho mỗi bản ghi TLS mà anh ấy gửi. Bob thực sự không bao gồm số thứ tự trong bản ghi, nhưng khi anh ấy tính HMAC, anh ấy bao gồm số thứ tự trong phép tính HMAC. Do đó, HMAC giờ đây là một hàm băm của dữ liệu cộng với khóa HMAC MB và số thứ tự hiện tại. Alice theo dõi số thứ tự của Bob, cho phép cô xác minh tính toàn vẹn dữ liệu của một bản ghi bằng cách bao gồm số thứ tự thích hợp trong phép tính HMAC. Việc sử dụng số thứ tự TLS này ngăn Trudy thực hiện một cuộc tấn công người trung gian, chẳng hạn như sắp xếp lại hoặc phát lại các phân đoạn. (Tại sao?)

TLS Ghi âm

Bản ghi TLS (cũng như bản ghi gần như TLS) được hiển thị trong Hình 8.26. Bản ghi bao gồm một trường loại, trường phiên bản, trường độ dài, trường dữ liệu và trường HMAC. Lưu ý rằng ba trường đầu tiên không được mã hóa. Trường loại chỉ ra liệu bản ghi là một thông điệp bắt tay hay một thông điệp chứa dữ liệu ứng dụng. Nó cũng được sử dụng để đóng kết nối TLS, như được thảo luận bên dưới. TLS ở đầu nhận sử dụng trường độ dài để trích xuất các bản ghi TLS ra khỏi luồng byte TCP đến. Trường phiên bản thì tự giải thích.

*Hình 8.26 ♦ Định dạng bản ghi cho TLS*

Phiên bản Độ dài Loại Dữ liệu HMAC

Được mã hóa bằng EB

**8.6.2 Một Bức Tranh Đầy Đủ Hơn**

Phần phụ trước đã đề cập đến giao thức gần như TLS; nó giúp chúng ta có một hiểu biết cơ bản về lý do và cách thức của TLS. Bây giờ khi chúng ta đã có một hiểu biết cơ bản, chúng ta có thể đào sâu hơn một chút và xem xét những điều thiết yếu của giao thức TLS thực sự. Song song với việc đọc mô tả về giao thức TLS này, bạn nên hoàn thành phòng thí nghiệm Wireshark TLS, có sẵn trên trang Web của sách giáo khoa.

TLS Handshake

SSL không yêu cầu Alice và Bob sử dụng một thuật toán khóa đối xứng cụ thể hoặc một thuật toán khóa công khai cụ thể. Thay vào đó, TLS cho phép Alice và Bob thỏa thuận về các thuật toán mật mã vào đầu phiên TLS, trong giai đoạn bắt tay. Ngoài ra, trong giai đoạn bắt tay, Alice và Bob gửi các số nonce cho nhau, được sử dụng trong việc tạo các khóa phiên (EB, MB, EA và MA). Các bước của quá trình bắt tay thực tế của TLS như sau:

1\. Khách hàng gửi một danh sách các thuật toán mã hóa mà nó hỗ trợ, cùng với một

số ngẫu nhiên của khách hàng. 2. Từ danh sách, máy chủ chọn một thuật toán đối xứng (ví dụ, AES)

và một thuật toán khóa công khai (ví dụ, RSA với độ dài khóa cụ thể), và thuật toán HMAC (MD5 hoặc SHA-1) cùng với các khóa HMAC. Nó gửi lại cho máy khách các lựa chọn của mình, cũng như một chứng chỉ và một nonce của máy chủ. 3. Máy khách xác minh chứng chỉ, trích xuất khóa công khai của máy chủ, tạo ra một

Bí mật Trước Thạc sĩ (PMS), mã hóa PMS bằng khóa công khai của máy chủ, và gửi PMS đã mã hóa đến máy chủ. 4. Sử dụng cùng một hàm tạo khóa (như được quy định bởi tiêu chuẩn TLS)

khách hàng và máy chủ độc lập tính toán Bí mật Chính (MS) từ PMS và các số nonce. MS sau đó được chia ra để tạo hai khóa mã hóa và hai khóa HMAC. Hơn nữa, khi bộ mã đối xứng được chọn sử dụng CBC (chẳng hạn như 3DES hoặc AES), thì cũng sẽ có hai Vectơ Khởi tạo (IV) --- một cho mỗi phía của kết nối --- được lấy từ MS. Kể từ đó, tất cả các thông điệp gửi giữa khách hàng và máy chủ đều được mã hóa và xác thực (bằng HMAC). 5. Khách hàng gửi HMAC của tất cả các thông điệp bắt tay. 6. Máy chủ gửi HMAC của tất cả các thông điệp bắt tay.

Hai bước cuối cùng bảo vệ quá trình bắt tay khỏi bị giả mạo. Để thấy điều này, hãy quan sát rằng ở bước 1, khách hàng thường cung cấp một danh sách các thuật toán---một số mạnh, một số yếu. Danh sách các thuật toán này được gửi dưới dạng văn bản rõ ràng, vì các thuật toán mã hóa và khóa vẫn chưa được thỏa thuận. Trudy, với vai trò là người ở giữa, có thể xóa các thuật toán mạnh khỏi danh sách, buộc khách hàng chọn một thuật toán yếu.

ngăn chặn một cuộc tấn công giả mạo như vậy, trong bước 5, khách hàng gửi HMAC của chuỗi các thông điệp bắt tay mà nó đã gửi và nhận. Máy chủ có thể so sánh HMAC này với HMAC của các thông điệp bắt tay mà nó đã nhận và gửi. Nếu có sự không nhất quán, máy chủ có thể chấm dứt kết nối. Tương tự, máy chủ gửi HMAC của các thông điệp bắt tay mà nó đã thấy, cho phép khách hàng kiểm tra sự không nhất quán.

Bạn có thể thắc mắc tại sao lại có nonces ở bước 1 và 2. Số thứ tự không đủ để ngăn chặn cuộc tấn công phát lại phân đoạn sao? Câu trả lời là có, nhưng chúng không ngăn chặn được "cuộc tấn công phát lại kết nối". Hãy xem xét cuộc tấn công lặp lại kết nối sau đây. Giả sử Trudy đánh hơi được tất cả tin nhắn giữa Alice và Bob. Ngày hôm sau, Trudy giả dạng Bob và gửi cho Alice chính xác chuỗi tin nhắn mà Bob đã gửi cho Alice vào ngày hôm trước. Nếu Alice không sử dụng nonces, cô ấy sẽ trả lời chính xác bằng chuỗi tin nhắn tương tự mà cô ấy đã gửi ngày hôm trước. Alice sẽ không nghi ngờ bất kỳ hoạt động kinh doanh hài hước nào, vì mỗi tin nhắn cô nhận được sẽ vượt qua quá trình kiểm tra tính toàn vẹn. Nếu Alice là một máy chủ thương mại điện tử, cô ấy sẽ nghĩ rằng Bob đang đặt hàng thứ hai (với cùng một thứ). Mặt khác, bằng cách đưa một số nonce vào giao thức, Alice sẽ gửi các số nonce khác nhau cho mỗi phiên TCP, khiến cho các khóa mã hóa sẽ khác nhau trong hai ngày. Do đó, khi Alice nhận được bản ghi TLS phát lại từ Trudy, bản ghi sẽ không vượt qua được quá trình kiểm tra tính toàn vẹn và giao dịch thương mại điện tử không có thật sẽ không thành công. Tóm lại, trong TLS, nonces được sử dụng để chống lại "cuộc tấn công phát lại kết nối" và số thứ tự được sử dụng để bảo vệ chống lại việc phát lại các gói riêng lẻ trong một phiên đang diễn ra.

Đóng kết nối

At some point, either Bob or Alice will want to end the TLS session. One approach would be to let Bob end the TLS session by simply terminating the underlying TCP connection---that is, by having Bob send a TCP FIN segment to Alice. But such a naive design sets the stage for the truncation attack whereby Trudy once again gets in the middle of an ongoing TLS session and ends the session early with a TCP FIN. If Trudy were to do this, Alice would think she received all of Bob's data when actuality she only received a portion of it. The solution to this problem is to indicate in the type field whether the record serves to terminate the TLS session. (Although the TLS type is sent in the clear, it is authenticated at the receiver using the record's HMAC.) By including such a field, if Alice were to receive a TCP FIN before receiving a closure TLS record, she would know that something funny was going on.

Điều này kết thúc phần giới thiệu của chúng ta về TLS. Chúng ta đã thấy rằng nó sử dụng nhiều nguyên tắc mật mã được thảo luận trong các Mục 8.2 và 8.3. Những độc giả muốn khám phá TLS ở một mức độ sâu hơn có thể đọc cuốn sách rất dễ đọc của Rescorla về SSL/ TLS \[Rescorla 2001\].

**8.7 Bảo mật Lớp Mạng: IPsec và Mạng Riêng Ảo**

Giao thức bảo mật IP, thường được biết đến nhiều hơn với tên gọi IPsec, cung cấp bảo mật ở tầng mạng. IPsec bảo vệ các gói tin IP giữa bất kỳ hai thực thể ở tầng mạng, bao gồm cả máy chủ và bộ định tuyến. Như chúng ta sẽ sớm mô tả, nhiều tổ chức (các tập đoàn, cơ quan chính phủ, tổ chức phi lợi nhuận, v.v.) sử dụng IPsec để tạo các mạng riêng ảo (VPN) chạy trên Internet công cộng.

Trước khi đi vào chi tiết của IPsec, hãy lùi lại một bước và xem xét việc cung cấp tính bảo mật ở lớp mạng có ý nghĩa gì. Với bảo mật ở lớp mạng giữa một cặp thực thể mạng (ví dụ, giữa hai bộ định tuyến, giữa hai máy chủ, hoặc giữa một bộ định tuyến và một máy chủ), thực thể gửi sẽ mã hóa các phần tải của tất cả các gói dữ liệu mà nó gửi đến thực thể nhận. Phần tải được mã hóa có thể là một đoạn TCP, một đoạn UDP, một thông điệp ICMP, v.v. Nếu dịch vụ cấp lớp mạng này được triển khai, tất cả dữ liệu gửi từ thực thể này đến thực thể kia---bao gồm e-mail, các trang Web, các thông điệp bắt tay TCP và các thông điệp quản lý (chẳng hạn như ICMP và SNMP)---sẽ bị ẩn khỏi bất kỳ bên thứ ba nào có thể đang theo dõi mạng. Vì lý do này, bảo mật lớp mạng được cho là cung cấp "phủ kín toàn bộ".

Ngoài việc bảo mật, một giao thức bảo mật lớp mạng cũng có thể cung cấp các dịch vụ bảo mật khác. Ví dụ, nó có thể cung cấp xác thực nguồn, để thực thể nhận có thể xác minh nguồn của datagram được bảo vệ. Một giao thức bảo mật lớp mạng có thể cung cấp tính toàn vẹn dữ liệu, để thực thể nhận có thể kiểm tra bất kỳ sự giả mạo nào của datagram có thể đã xảy ra trong khi datagram đang được truyền đi. Một dịch vụ bảo mật lớp mạng cũng có thể cung cấp khả năng ngăn chặn tấn công phát lại, nghĩa là Bob có thể phát hiện bất kỳ datagram trùng lặp nào mà một kẻ tấn công có thể chèn vào. Chúng ta sẽ sớm thấy rằng IPsec thực sự cung cấp các cơ chế cho tất cả các dịch vụ bảo mật này, tức là, cho bảo mật, xác thực nguồn, tính toàn vẹn dữ liệu và ngăn chặn tấn công phát lại.

**8.7.1 IPsec và Mạng Riêng Ảo (VPNs)**

Một tổ chức mở rộng qua nhiều vùng địa lý thường mong muốn có mạng IP riêng, để các máy chủ và máy trạm của nó có thể gửi dữ liệu cho nhau một cách an toàn và bảo mật. Để đạt được mục tiêu này, tổ chức có thể triển khai một mạng vật lý độc lập---bao gồm các bộ định tuyến, các liên kết và cơ sở hạ tầng DNS---hoàn toàn tách biệt với Internet công cộng. Một mạng tách rời như vậy, dành riêng cho một tổ chức cụ thể, được gọi là mạng riêng. Không có gì ngạc nhiên, một mạng riêng có thể rất tốn kém, vì tổ chức cần mua, cài đặt và duy trì cơ sở hạ tầng mạng vật lý của riêng mình.

Thay vì triển khai và duy trì một mạng riêng, ngày nay nhiều tổ chức tạo các VPN trên Internet công cộng hiện có. Với VPN, lưu lượng liên văn phòng của tổ chức được gửi qua Internet công cộng thay vì qua một mạng vật lý

mạng độc lập. Nhưng để đảm bảo tính bảo mật, lưu lượng giữa các văn phòng được mã hóa trước khi nó đi vào Internet công cộng. Một ví dụ đơn giản về VPN được minh họa trong Hình 8.27. Ở đây, tổ chức bao gồm một trụ sở chính, một văn phòng chi nhánh và các nhân viên kinh doanh đi công tác thường truy cập Internet từ phòng khách sạn của họ. (Trong hình chỉ có một nhân viên kinh doanh được hiển thị.) Trong VPN này, bất cứ khi nào hai máy chủ trong trụ sở chính gửi IP datagram cho nhau hoặc bất cứ khi nào hai máy chủ trong văn phòng chi nhánh muốn liên lạc, họ sử dụng IPv4 thông thường (tức là, không có dịch vụ IPsec). Tuy nhiên, khi hai máy chủ của tổ chức liên lạc qua một đường truyền đi qua Internet công cộng, lưu lượng được mã hóa trước khi vào Internet.

Để cảm nhận cách hoạt động của VPN, hãy cùng đi qua một ví dụ đơn giản trong bối cảnh của Hình 8.27. Khi một máy chủ tại trụ sở chính gửi một datagram IP đến một nhân viên kinh doanh ở khách sạn, bộ định tuyến cổng tại trụ sở chính sẽ chuyển datagram IPv4 bình thường thành một datagram IPsec và sau đó chuyển datagram IPsec này vào Internet. Datagam IPsec này thực chất có một tiêu đề IPv4 truyền thống, để các bộ định tuyến trong Internet công cộng xử lý datagram như thể nó là một datagram IPv4 thông thường --- đối với chúng, datagram là một datagram hoàn toàn bình thường. Nhưng, như thể hiện trong Hình 8.27, phần tải của datagram IPsec bao gồm một tiêu đề IPsec, được sử dụng để xử lý IPsec; hơn nữa, phần tải của datagram IPsec được mã hóa. Khi

*Hình 8.27 ♦ Mạng riêng ảo (VPN)*

IP tiêu đề

Đầu IPsec

Tải trọng bảo mật

IP tiêu đề

Đầu IPsec

Tải trọng bảo mật

IP tiêu đề

Đầu IPsec

Tải trọng bảo mật

IP tiêu đề Payload

IP tiêu đề Payload

Laptop với IPsec

Router với/IPv4 và

IPsec

Router với/IPv4 và

IPsec

Văn phòng chi nhánh

Trụ sở chính

Nhân viên bán hàng ở khách sạn

Internet công cộng

Gói tin IPsec đến laptop của nhân viên bán hàng, hệ điều hành trên laptop sẽ giải mã phần dữ liệu (và cung cấp các dịch vụ bảo mật khác, như xác minh tính toàn vẹn của dữ liệu) và chuyển phần dữ liệu chưa được mã hóa lên giao thức lớp trên (ví dụ, đến TCP hoặc UDP).

Chúng tôi vừa mới đưa ra một cái nhìn tổng quan cấp cao về cách một tổ chức có thể sử dụng IPsec để tạo ra một VPN. Để nhìn thấy toàn cảnh, chúng tôi đã bỏ qua nhiều chi tiết quan trọng. Bây giờ hãy cùng xem xét kỹ hơn.

**8.7.2 Giao thức AH và ESP**

IPsec là một thực thể khá phức tạp---nó được định nghĩa trong hơn một tá RFC. Hai RFC quan trọng là RFC 4301, mô tả tổng thể kiến trúc bảo mật IP, và RFC 6071, cung cấp tổng quan về bộ giao thức IPsec. Mục tiêu của chúng tôi trong sách giáo khoa này, như thường lệ, không chỉ đơn giản là nhai lại các RFC khô khan và khó hiểu, mà thay vào đó là áp dụng một cách tiếp cận thực tiễn và sư phạm hơn để mô tả các giao thức.

Trong bộ giao thức IPsec, có hai giao thức chính: giao thức Xác thực (AH) và giao thức Bảo mật Bao gói (ESP). Khi một thực thể IPsec nguồn (thường là một máy chủ hoặc bộ định tuyến) gửi các gói dữ liệu an toàn đến một thực thể đích (cũng là một máy chủ hoặc bộ định tuyến), nó thực hiện việc này bằng giao thức AH hoặc giao thức ESP. Giao thức AH cung cấp xác thực nguồn và tính toàn vẹn dữ liệu nhưng không cung cấp tính bảo mật. Giao thức ESP cung cấp xác thực nguồn, tính toàn vẹn dữ liệu và bảo mật. Vì bảo mật thường rất quan trọng đối với VPN và các ứng dụng IPsec khác, giao thức ESP được sử dụng phổ biến hơn nhiều so với giao thức AH. Để làm rõ IPsec và tránh phần lớn sự phức tạp của nó, chúng ta sẽ tập trung hoàn toàn vào giao thức ESP. Những độc giả muốn tìm hiểu thêm về giao thức AH được khuyến khích tham khảo các RFC và các tài nguyên trực tuyến khác.

**8.7.3 Liên kết bảo mật**

Các gói dữ liệu IPsec được gửi giữa các cặp thực thể mạng, chẳng hạn như giữa hai máy chủ, giữa hai bộ định tuyến, hoặc giữa một máy chủ và một bộ định tuyến. Trước khi gửi các gói dữ liệu IPsec từ thực thể nguồn đến thực thể đích, các thực thể nguồn và đích tạo một kết nối logic tại lớp mạng. Kết nối logic này được gọi là hiệp hội bảo mật (SA). Một SA là một kết nối logic đơn giản; nghĩa là, nó chỉ đi một chiều từ nguồn đến đích. Nếu cả hai thực thể muốn gửi các gói dữ liệu bảo mật cho nhau, thì cần thiết lập hai SA (tức là hai kết nối logic), mỗi chiều một kết nối.

Ví dụ, hãy xem xét lại VPN của tổ chức trong Hình 8.27. Tổ chức này gồm một văn phòng trụ sở chính, một văn phòng chi nhánh và, giả sử, n nhân viên bán hàng đi công tác. Để làm ví dụ, giả sử rằng có lưu lượng IPsec hai chiều giữa trụ sở chính và văn phòng chi nhánh và lưu lượng IPsec hai chiều giữa trụ sở chính và các nhân viên bán hàng. Trong VPN này, có bao nhiêu SA? Để trả lời câu hỏi này, lưu ý rằng có hai SA giữa bộ định tuyến cổng trụ sở chính và bộ định tuyến cổng văn phòng chi nhánh (một cho mỗi chiều); đối với mỗi

máy tính xách tay của nhân viên kinh doanh, có hai SA giữa bộ định tuyến cổng trung tâm và máy tính xách tay (một cái cho mỗi hướng). Vì vậy, tổng cộng có (2 + 2n) SA. Tuy nhiên, cần nhớ rằng không phải tất cả lưu lượng được gửi ra Internet bởi các bộ định tuyến cổng hoặc bởi các máy tính xách tay đều được bảo mật IPsec. Ví dụ, một máy chủ tại trung tâm có thể muốn truy cập một máy chủ Web (như Amazon hoặc Google) trên Internet công cộng. Do đó, bộ định tuyến cổng (và các máy tính xách tay) sẽ phát ra cả các gói tin IPv4 thông thường và các gói tin IPsec bảo mật.

Bây giờ chúng ta hãy xem xét "bên trong" một SA. Để làm cho cuộc thảo luận trở nên cụ thể và dễ hiểu, hãy thực hiện điều này trong bối cảnh của một SA từ router R1 đến router R2 trong Hình 8.28. (Bạn có thể coi R1 là router cổng chính của trụ sở và R2 là router cổng của chi nhánh từ Hình 8.27.) R1 sẽ duy trì thông tin trạng thái về SA này, điều này sẽ bao gồm:

• Một định danh 32-bit cho SA, gọi là Chỉ số Tham số Bảo mật (SPI) • Giao diện xuất phát của SA (trong trường hợp này là 200.168.1.100) và giao diện đích của SA (trong trường hợp này là 193.68.2.23) • Loại mã hóa sẽ được sử dụng (ví dụ, 3DES với CBC) • Khóa mã hóa • Loại kiểm tra tính toàn vẹn (ví dụ, HMAC với MD5) • Khóa xác thực

Khi nào router R1 cần xây dựng một datagram IPsec để chuyển tiếp qua SA này, nó truy cập vào thông tin trạng thái này để xác định cách nó nên xác thực và mã hóa datagram. Tương tự, router R2 sẽ duy trì cùng thông tin trạng thái này cho SA và sẽ sử dụng thông tin này để xác thực và giải mã bất kỳ datagram IPsec nào đến từ SA.

Một thực thể IPsec (router hoặc host) thường duy trì thông tin trạng thái cho nhiều SA. Ví dụ, trong ví dụ VPN ở Hình 8.27 với n nhân viên bán hàng, router cổng của trụ sở chính duy trì thông tin trạng thái cho (2 + 2n) SA. Một thực thể IPsec lưu trữ thông tin trạng thái cho tất cả các SA của nó trong Cơ sở Dữ liệu Liên kết Bảo mật (SAD), là một cấu trúc dữ liệu trong nhân hệ điều hành của thực thể đó.

*Hình 8.28 ♦ Liên kết bảo mật (SA) từ R1 đến R2*

Internet

SA R1

172.16.1/24

Trụ sở chi nhánh văn phòng

200.168.1.100 193.68.2.23

172.16.2/24

R2

**8.7.4 IPsec Datagram**

Sau khi đã mô tả các SA, chúng ta có thể mô tả gói dữ liệu IPsec thực tế. IPsec có hai dạng gói khác nhau, một cho chế độ gọi là tunnel và một cho chế độ gọi là transport. Chế độ tunnel, phù hợp hơn cho VPN, được triển khai rộng rãi hơn so với chế độ transport. Để giúp đơn giản hóa IPsec và tránh nhiều phức tạp của nó, từ đây chúng ta sẽ tập trung hoàn toàn vào chế độ tunnel. Khi bạn đã nắm vững chế độ tunnel, bạn sẽ có thể dễ dàng học về chế độ transport một cách tự nhiên.

Định dạng gói dữ liệu của datagram IPsec được hiển thị trong Hình 8.29. Bạn có thể nghĩ rằng định dạng gói dữ liệu thật nhàm chán và nhạt nhẽo, nhưng chúng ta sẽ sớm thấy rằng datagram IPsec thực sự trông và có vị giống như một món ăn Tex-Mex phổ biến! Hãy xem xét các trường của IPsec trong bối cảnh của Hình 8.28. Giả sử bộ định tuyến R1 nhận một datagram IPv4 thông thường từ máy chủ 172.16.1.17 (trong mạng trụ sở chính) được gửi đến máy chủ 172.16.2.48 (trong mạng chi nhánh). Router R1 sử dụng công thức sau để chuyển đổi datagram "IPv4 gốc" này thành một datagram IPsec:

• Thêm vào phía sau của datagram IPv4 gốc (bao gồm các trường tiêu đề gốc!) một trường "ESP trailer" • Mã hóa kết quả sử dụng thuật toán và khóa được chỉ định bởi SA • Thêm vào phía trước của giá trị đã mã hóa này một trường gọi là "ESP header"; gói kết quả được gọi là "enchilada" • Tạo một MAC xác thực trên toàn bộ enchilada sử dụng thuật toán và khóa được chỉ định trong SA • Thêm MAC vào phía sau của enchilada tạo thành phần payload • Cuối cùng, tạo một tiêu đề IP hoàn toàn mới với tất cả các trường tiêu đề IPv4 cổ điển (thường dài 20 byte), mà nó thêm vào trước payload

Lưu ý rằng gói tin IPsec kết quả là một gói tin IPv4 thực thụ, với các trường tiêu đề IPv4 truyền thống theo sau bởi một phần tải. Nhưng trong trường hợp này, phần tải

*Hình 8.29 ♦ Định dạng gói dữ liệu IPsec*

Tiêu đề IP mới

Tiêu đề ESP

rơ moóc ESP

Tiêu đề ESP MAC Original IP

Dữ liệu gói tin IP gốc

Được mã hóa

"Enchilada" đã được xác thực

Độ dài đệm Padding Header tiếp theo SPI Số thứ tự

chứa tiêu đề ESP, gói dữ liệu IP gốc, đoạn giới thiệu ESP và trường xác thực ESP (với gói dữ liệu gốc và đoạn giới thiệu ESP được mã hóa). Gói dữ liệu IP ban đầu có 172.16.1.17 cho địa chỉ IP nguồn và 172.16.2.48 cho địa chỉ đích IP. Vì gói dữ liệu IPsec bao gồm gói dữ liệu IP ban đầu nên các địa chỉ này được bao gồm (và được mã hóa) như một phần tải trọng của gói IPsec. Nhưng còn địa chỉ nguồn và đích IP nằm trong tiêu đề IP mới, tức là trong tiêu đề ngoài cùng bên trái của gói dữ liệu IPsec thì sao? Như bạn có thể mong đợi, chúng được đặt thành giao diện bộ định tuyến nguồn và đích ở hai đầu của đường hầm, cụ thể là 200.168.1.100 và 193.68.2.23. Ngoài ra, số giao thức trong trường tiêu đề IPv4 mới này không được đặt thành số của TCP, UDP hoặc SMTP mà thay vào đó là 50, chỉ định rằng đây là gói dữ liệu IPsec sử dụng giao thức ESP.

Sau khi R1 gửi gói dữ liệu IPsec vào Internet công cộng, nó sẽ đi qua nhiều bộ định tuyến trước khi đến R2. Mỗi bộ định tuyến này sẽ xử lý gói dữ liệu như thể đó là một gói dữ liệu thông thường --- chúng hoàn toàn không nhận biết rằng gói dữ liệu đang mang dữ liệu được mã hóa IPsec. Đối với các bộ định tuyến Internet công cộng này, vì địa chỉ IP đích trong phần đầu ngoài là R2, điểm đến cuối cùng của gói dữ liệu là R2.

Sau khi đã đi qua một ví dụ về cách một gói tin IPsec được xây dựng, hãy cùng nhìn kỹ hơn vào các thành phần bên trong. Chúng ta thấy trong Hình 8.29 rằng phần đuôi ESP bao gồm ba trường: padding (đệm); độ dài padding; và header tiếp theo. Hãy nhớ rằng các bộ mã khối yêu cầu thông điệp cần được mã hóa phải là bội số nguyên của độ dài khối. Padding (bao gồm các byte vô nghĩa) được sử dụng sao cho khi cộng với gói tin gốc (cùng với các trường độ dài padding và header tiếp theo), "thông điệp" kết quả là số nguyên của các khối. Trường độ dài padding cho thực thể nhận biết mức độ padding đã được chèn vào (và do đó cần được loại bỏ). Header tiếp theo xác định loại (ví dụ, UDP) của dữ liệu chứa trong trường payload-data. Dữ liệu payload (thường là gói tin IP gốc) và phần đuôi ESP được nối với nhau và sau đó được mã hóa.

Được thêm vào phía trước của đơn vị mã hóa này là tiêu đề ESP, được gửi rõ ràng và bao gồm hai trường: SPI và trường số thứ tự. SPI cho thực thể nhận biết SA mà datagram thuộc về; thực thể nhận có thể sử dụng SPI để tra cứu SAD của mình nhằm xác định các thuật toán và khóa xác thực/mã hóa thích hợp. Trường số thứ tự được sử dụng để phòng chống các cuộc tấn công phát lại.

Thực thể gửi cũng thêm một MAC xác thực. Như đã nêu trước đó, thực thể gửi tính toán một MAC trên toàn bộ gói dữ liệu (bao gồm tiêu đề ESP, gói IP gốc, và phần đuôi ESP---với gói và phần đuôi được mã hóa). Hãy nhớ rằng để tính MAC, người gửi thêm một khóa MAC bí mật vào gói dữ liệu và sau đó tính toán một hàm băm cố định độ dài từ kết quả.

Khi R2 nhận được gói tin IPsec, R2 quan sát thấy địa chỉ IP đích của gói tin là chính R2. Do đó, R2 xử lý gói tin. Vì trường giao thức (trong header IP bên trái nhất) là 50, R2 thấy rằng nó nên áp dụng xử lý IPsec ESP cho gói tin. Trước tiên, nhìn vào toàn bộ dữ liệu, R2 sử dụng SPI để xác định gói tin thuộc SA nào. Thứ hai, nó tính toán MAC của dữ liệu và xác minh rằng MAC phù hợp với giá trị trong ESP.

Trường MAC. Nếu đúng như vậy, nó biết rằng món enchilada đến từ R1 và chưa bị can thiệp. Thứ ba, nó kiểm tra trường số thứ tự để xác minh rằng datagram là mới (và không phải là datagram bị phát lại). Thứ tư, nó giải mã đơn vị được mã hóa bằng thuật toán giải mã và khóa liên kết với SA. Thứ năm, nó loại bỏ phần đệm và trích xuất datagram IP gốc, nguyên bản. Và cuối cùng, thứ sáu, nó chuyển tiếp datagram gốc vào mạng văn phòng chi nhánh hướng tới điểm đến cuối cùng của nó. Chà, thật là một công thức phức tạp, đúng không? Chà, chưa ai nói rằng việc chuẩn bị và giải mã một món enchilada là dễ dàng!

There is actually another important subtlety that needs to be addressed. It centers on the following question: When R1 receives an (unsecured) datagram from a host in the headquarters network, and that datagram is destined to some destination IP address outside of headquarters, how does R1 know whether it should be converted to an IPsec datagram? And if it is to be processed by IPsec, how does R1 know which SA (of many SAs in its SAD) should be used to construct the IPsec datagram? The problem is solved as follows. Along with a SAD, the IPsec entity also maintains another data structure called the Security Policy Database (SPD). The SPD indicates what types of datagrams (as a function of source IP address, destination IP address, and protocol type) are to be IPsec processed; and for those that are to be IPsec processed, which SA should be used. In a sense, the information in a SPD indicates "what" to do with an arriving datagram; the information in the SAD indicates "how" to do it.

Tóm tắt các Dịch vụ IPsec

So what services does IPsec provide, exactly? Let us examine these services from the perspective of an attacker, say Trudy, who is a woman-in-the-middle, sitting somewhere on the path between R1 and R2 in Figure 8.28. Assume throughout this discussion that Trudy does not know the authentication and encryption keys used by the SA. What can and cannot Trudy do? First, Trudy cannot see the original datagram. If fact, not only is the data in the original datagram hidden from Trudy, but so is the protocol number, the source IP address, and the destination IP address. For datagrams sent over the SA, Trudy only knows that the datagram originated from 200.168.1.100 and is destined to 193.68.2.23. She does not know if it is carrying TCP, UDP, or ICMP data; she does not know if it is carrying HTTP, SMTP, or some other type of application data. This confidentiality thus goes a lot farther than SSL. Second, suppose Trudy tries to tamper with a datagram in the SA by flipping some of its bits. When this tampered datagram arrives at R2, it will fail the integrity check (using the MAC), thwarting Trudy's vicious attempts once again. Third, suppose Trudy tries to masquerade as R1, creating a IPsec datagram with source 200.168.1.100 and destination 193.68.2.23. Trudy's attack will be futile, as this datagram will again fail the integrity check at R2. Finally, because IPsec includes sequence numbers, Trudy will not be able create a successful replay attack. In summary, as claimed at the beginning of this section, IPsec provides---between any pair of devices that process packets through the network layer---confidentiality, source authentication, data integrity, and replay-attack prevention.

**8.7.5 IKE: Quản lý khóa trong IPsec**

Khi một VPN có số lượng điểm cuối nhỏ (ví dụ, chỉ hai bộ định tuyến như trong Hình 8.28), quản trị viên mạng có thể nhập thủ công thông tin SA (thuật toán mã hóa/xác thực và khóa, cũng như SPI) vào SAD của các điểm cuối. Việc "nhập khóa thủ công" như vậy rõ ràng là không thực tế đối với một VPN lớn, có thể bao gồm hàng trăm hoặc thậm chí hàng nghìn bộ định tuyến và máy chủ IPsec. Các triển khai lớn, phân tán theo địa lý yêu cầu một cơ chế tự động để tạo các SA. IPsec thực hiện điều này thông qua giao thức Internet Key Exchange (IKE), được quy định trong RFC 5996.

IKE có một số điểm tương đồng với quá trình bắt tay trong SSL (xem Mục 8.6). Mỗi thực thể IPsec đều có chứng chỉ, bao gồm khóa công khai của thực thể đó. Giống như SSL, giao thức IKE yêu cầu hai thực thể trao đổi chứng chỉ, thương lượng các thuật toán xác thực và mã hóa, và trao đổi an toàn tài liệu khóa để tạo khóa phiên trong các SA của IPsec. Khác với SSL, IKE sử dụng hai pha để thực hiện các nhiệm vụ này.

Hãy cùng điều tra hai giai đoạn này trong bối cảnh của hai bộ định tuyến, R1 và R2, trong Hình 8.28. Giai đoạn đầu tiên bao gồm hai lần trao đổi các cặp tin nhắn giữa R1 và R2:

• During the first exchange of messages, the two sides use Diffie-Hellman (see Homework Problems) to create a bi-directional IKE SA between the routers. To keep us all confused, this bi-directional IKE SA is entirely different from the IPsec SAs discussed in Sections 8.6.3 and 8.6.4. The IKE SA provides an authenticated and encrypted channel between the two routers. During this first messagepair exchange, keys are established for encryption and authentication for the IKE SA. Also established is a master secret that will be used to compute IPSec SA keys later in phase 2. Observe that during this first step, RSA public and private keys are not used. In particular, neither R1 nor R2 reveals its identity by signing a message with its private key. • During the second exchange of messages, both sides reveal their identity to each other by signing their messages. However, the identities are not revealed to a passive sniffer, since the messages are sent over the secured IKE SA channel. Also during this phase, the two sides negotiate the IPsec encryption and authentication algorithms to be employed by the IPsec SAs.

Trong pha 2 của IKE, hai bên tạo một SA ở mỗi hướng. Vào cuối pha 2, các khóa phiên mã hóa và xác thực được thiết lập trên cả hai bên cho hai SA. Sau đó, hai bên có thể sử dụng các SA để gửi các gói dữ liệu được bảo mật, như được mô tả trong Mục 8.7.3 và 8.7.4. Động cơ chính cho việc có hai pha trong IKE là chi phí tính toán---vì pha thứ hai không liên quan đến bất kỳ mật mã khóa công khai nào, IKE có thể tạo một số lượng lớn các SA giữa hai thực thể IPsec với chi phí tính toán tương đối thấp.

**8.8 Bảo mật Mạng LAN Không dây và Mạng Di động 4G/5G**

An ninh là một mối quan tâm đặc biệt quan trọng trong các mạng không dây, nơi kẻ tấn công có thể nghe lén các khung dữ liệu chỉ bằng cách đặt một thiết bị thu nhận ở bất kỳ đâu trong phạm vi truyền của thiết bị gửi. Điều này đúng cả trong mạng LAN không dây 802.11, cũng như trong mạng di động 4G/5G. Trong cả hai bối cảnh, chúng ta sẽ thấy việc sử dụng rộng rãi các kỹ thuật an ninh cơ bản mà chúng ta đã học trước đó trong chương này, bao gồm việc sử dụng nonce để xác thực, băm mật mã để đảm bảo tính toàn vẹn của thông điệp, suy ra các khóa đối xứng chia sẻ để mã hóa dữ liệu phiên người dùng, và việc sử dụng rộng rãi tiêu chuẩn mã hóa AES. Chúng ta cũng sẽ thấy, giống như trong các bối cảnh Internet có dây, rằng các giao thức bảo mật không dây đã trải qua sự tiến hóa liên tục, khi các nhà nghiên cứu và hacker phát hiện ra các điểm yếu và lỗi trong các giao thức bảo mật hiện có.

Trong phần này, chúng tôi trình bày một giới thiệu ngắn gọn về bảo mật không dây trong cả môi trường 802.11 (WiFi) và 4G/5G. Để có một cách tiếp cận sâu hơn, hãy tham khảo các cuốn sách về bảo mật 802.11 rất dễ đọc \[Edney 2003; Wright 2015\], phần trình bày xuất sắc về bảo mật 3G/4G/5G trong \[Sauter 2014\], và các khảo sát gần đây \[Zou 2016; Kohlios 2018\].

**8.8.1 Xác thực và Thỏa thuận Khóa trong Mạng LAN Không dây 802.11**

Hãy bắt đầu cuộc thảo luận về bảo mật 802.11 của chúng ta bằng cách xác định hai (trong nhiều \[Zou 2016\]) mối quan tâm bảo mật quan trọng mà chúng ta muốn một mạng 802.11 xử lý:

• Mutual authentication. Before a mobile device is allowed to fully attach to an access point and send datagrams to remote hosts, the network will typically want to first authenticate the device---to verify the identity of the mobile device attaching to the network, and to check that device's access privileges. Similarly, the mobile device will want to authenticate the network to which it is attaching---to make sure that the network it is joining is truly the network to which it wants to attach. This two-way authentication is known as mutual authentication. • Encryption. Since 802.11 frames will be exchanged over a wireless channel that can be sniffed and manipulated by potential ne'er do-wells, it will be important to encrypt link-level frames carrying user-level data exchanged between the mobile device and the access point (AP). Symmetric key encryption is used in practice, since encryption and decryption must be performed at high speeds. The mobile device and AP will need to derive the symmetric encryption and decryption keys to be used.

Hình 8.30 minh họa tình huống một thiết bị di động muốn kết nối với mạng 802.11. Chúng ta thấy hai thành phần mạng thông thường mà chúng ta đã gặp

Trong nghiên cứu trước của chúng tôi về mạng 802.11 ở Mục 7.3---thiết bị di động và AP. Chúng ta cũng thấy một thành phần kiến trúc mới, máy chủ xác thực (AS) sẽ chịu trách nhiệm xác thực thiết bị di động. Máy chủ xác thực có thể được đặt cùng vị trí với AP, nhưng phổ biến hơn và như được minh họa trong Hình 8.30, nó được triển khai như một máy chủ riêng biệt cung cấp dịch vụ xác thực. Đối với việc xác thực, AP hoạt động như một thiết bị trung gian, chuyển tiếp các thông điệp xác thực và dẫn xuất khóa giữa thiết bị di động và máy chủ xác thực. Một máy chủ xác thực như vậy thường sẽ cung cấp dịch vụ xác thực cho tất cả các AP trong mạng của nó.

Chúng ta có thể xác định bốn giai đoạn riêng biệt trong quá trình xác thực lẫn nhau và suy ra cũng như sử dụng khóa mã hóa trong Hình 8.30:

1\. Khám phá. Trong giai đoạn khám phá, AP quảng bá sự hiện diện của nó và các biểu mẫu

xác thực và mã hóa có thể được cung cấp cho thiết bị di động. Thiết bị di động sau đó yêu cầu các hình thức xác thực và mã hóa cụ thể mà nó mong muốn. Mặc dù thiết bị và AP đã trao đổi tin nhắn, nhưng thiết bị vẫn chưa được xác thực cũng như chưa có khóa mã hóa để truyền khung dữ liệu qua liên kết không dây, do đó sẽ cần thêm một số bước nữa trước khi thiết bị có thể giao tiếp an toàn thông qua AP. 2. Xác thực lẫn nhau và suy ra khóa đối xứng chia sẻ. Đây là

bước quan trọng trong việc "bảo đảm" kênh 802.11. Như chúng ta sẽ thấy, bước này là

Thiết bị di động

AP: điểm truy cập

Mạng có dây

AS: xác thực

máy chủ

Khám phá các khả năng bảo mật

Giao tiếp được mã hóa giữa thiết bị di động và máy chủ từ xa qua AP

Phân phối khóa phiên đối xứng chia sẻ

Xác thực lẫn nhau và suy ra khóa đối xứng chia sẻ

*Hình 8.30 ♦ Xác thực lẫn nhau và suy ra khóa mã hóa*

trong WPA

được tạo điều kiện thuận lợi đáng kể bằng cách giả định (điều này đúng trong thực tế cả ở mạng 802.11 và 4G/5G) rằng máy chủ xác thực và thiết bị di động đã có một bí mật chung trước khi bắt đầu xác thực lẫn nhau. Trong bước này, thiết bị và máy chủ xác thực sẽ sử dụng bí mật chung này cùng với các số nonce (để ngăn chặn các cuộc tấn công chuyển tiếp) và băm mật mã (để đảm bảo tính toàn vẹn của thông điệp) trong việc xác thực lẫn nhau. Họ cũng sẽ tạo ra khóa phiên chung được sử dụng bởi thiết bị di động và AP để mã hóa các khung dữ liệu truyền qua liên kết không dây 802.11. 3. Phân phối khóa phiên đối xứng chung. Vì khóa mã hóa đối xứng

được dẫn xuất tại thiết bị di động và máy chủ xác thực, sẽ cần một giao thức để máy chủ xác thực thông báo cho AP về khóa phiên đối xứng chia sẻ. Mặc dù điều này khá đơn giản, nhưng nó vẫn là một bước cần thiết. 4. Giao tiếp được mã hóa giữa thiết bị di động và một máy chủ từ xa thông qua

AP. Liên lạc này xảy ra như chúng ta đã thấy trước đó trong Mục 7.3.2, với các khung liên kết (link-layer frames) được gửi giữa thiết bị di động và AP được mã hóa bằng khóa phiên chia sẻ được tạo và phân phối bởi Các Bước 2 và 3. Mã hóa khóa đối xứng AES, mà chúng ta đã đề cập trước đó trong Mục 8.2.1, thường được sử dụng trong thực tế để mã hóa/giải mã dữ liệu khung 802.11.

Xác thực lẫn nhau và Phát sinh Khóa Phi đối xứng Phiên chia sẻ

Các chủ đề về xác thực lẫn nhau và việc tạo khóa phiên đối xứng chia sẻ là các thành phần trung tâm của bảo mật 802.11. Vì chính tại đây người ta đã phát hiện ra các lỗ hổng bảo mật trong các phiên bản 802.11 trước đó, hãy giải quyết những thách thức này trước.

Vấn đề về bảo mật 802.11 đã thu hút sự chú ý đáng kể cả trong các chuyên gia kỹ thuật lẫn truyền thông. Mặc dù đã có nhiều thảo luận, nhưng lại ít có tranh luận---mọi người đều đồng ý rằng đặc tả bảo mật 802.11 ban đầu, được biết đến chung dưới tên Bảo mật Tương đương Dây (Wired Equivalent Privacy - WEP), chứa một số lỗi bảo mật nghiêm trọng \[Fluhrer 2001; Stubblefield 2002\]. Khi những lỗi này được phát hiện, phần mềm công khai nhanh chóng xuất hiện khai thác các lỗ hổng này, khiến người dùng WLAN 802.11 được bảo vệ bằng WEP trở nên dễ bị tấn công bảo mật như những người không sử dụng bất kỳ tính năng bảo mật nào. Những độc giả quan tâm đến việc tìm hiểu về WEP có thể tham khảo các tài liệu tham khảo, cũng như các ấn bản trước của cuốn giáo trình này, đã đề cập đến WEP. Như thường lệ, tài liệu đã rút gọn từ cuốn sách này có sẵn trên Trang web Hỗ trợ đi kèm.

WiFi Protected Access (WPA1) được phát triển vào năm 2003 bởi Liên minh WiFi \[WiFi 2020\] nhằm khắc phục các lỗ hổng bảo mật của WEP. Phiên bản ban đầu của WPA1 đã cải thiện WEP bằng cách giới thiệu kiểm tra tính toàn vẹn của thông điệp, và tránh các cuộc tấn công cho phép người dùng suy ra khóa mã hóa sau khi quan sát luồng các thông điệp được mã hóa trong một khoảng thời gian. WPA1 nhanh chóng nhường chỗ cho WPA2, phiên bản này bắt buộc sử dụng mã hóa khóa đối xứng AES.

Cốt lõi của WPA là một giao thức bắt tay bốn chiều thực hiện cả xác thực lẫn nhau và suy diễn khóa phiên đối xứng chia sẻ. Giao thức bắt tay được minh họa trong Hình 8.31 dưới dạng đơn giản hóa. Lưu ý rằng cả thiết bị di động (M) và máy chủ xác thực (AS) đều bắt đầu biết một khóa bí mật chia sẻ KAS-M

(ví dụ, một mật khẩu). Một trong những nhiệm vụ của họ sẽ là tạo ra một khóa phiên đối xứng chung, KM-AP, sẽ được sử dụng để mã hóa/giải mã các khung dữ liệu mà sau đó được truyền giữa thiết bị di động (M) và AP.

Xác thực lẫn nhau và suy ra khóa phiên đối xứng chung được thực hiện trong hai bước đầu tiên, a và b, của quy trình bắt tay bốn chiều được thể hiện trong Hình 8.31. Các bước c và d được sử dụng để suy ra một khóa thứ hai dùng cho liên lạc nhóm; xem \[Kohlios 2018; Zou 2016\] để biết chi tiết.

a\. Trong bước đầu tiên này, máy chủ xác thực (AS) tạo ra một nonce, NonceAS,

và gửi nó đến thiết bị di động. Nhớ lại từ Mục 8.4 rằng các số ngẫu nhiên được sử dụng để tránh các cuộc tấn công phát lại và chứng minh "tính sống" của bên kia đang được xác thực.

b\. Thiết bị di động, M, nhận nonce, NonceAS, từ AS và\...

tạo ra một nonce riêng của nó, NonceM. Thiết bị di động sau đó tạo khóa phiên chia sẻ đối xứng, KM-AP, sử dụng NonceAS, NonceM, khóa bí mật chia sẻ ban đầu KAS-M, địa chỉ MAC của nó và địa chỉ MAC của AS. Sau đó, nó gửi nonce của mình, NonceM, và một giá trị được ký HMAC (xem Hình 8.9) mã hóa NonceAS và khóa bí mật chia sẻ ban đầu.

AS nhận được tin nhắn này từ M. Bằng cách nhìn vào ver- được ký HMAC

phiên của số lần sử dụng một lần mà nó vừa mới gửi, NonceAS, máy chủ xác thực biết thiết bị di động đang hoạt động; vì thiết bị di động có thể mã hóa bằng khóa bí mật chia sẻ, KAS-M, AS cũng biết rằng thiết bị di động

M: Thiết bị di động

AS: xác thực

máy chủ

một

b

NonceAS Phát sinh khóa phiên KM-AP sử dụng KAS-M, NonceAS, NonceM

Sinh khóa phiên KM-AP sử dụng KAS-M, NonceAS, NonceM

KAS-M

KAS-M

NonceM, HMAC(f(KAS-M, NonceAS))

c

d

c, d: được sử dụng để dẫn xuất khóa nhóm

*Hình 8.31 ♦ Bắt tay bốn bước WPA2*

thực sự là thiết bị mà nó tự nhận (tức là, một thiết bị biết bí mật ban đầu được chia sẻ). Do đó, AS đã xác thực thiết bị di động! AS cũng có thể thực hiện tính toán chính xác giống như thiết bị di động để suy ra khóa phiên đối xứng được chia sẻ, KM-AP, sử dụng NonceM mà nó nhận được, NonceAS, khóa bí mật ban đầu KAS-M, địa chỉ MAC của nó và địa chỉ MAC của thiết bị di động. Tại thời điểm này, cả thiết bị di động và máy chủ xác thực đều đã tính toán cùng một khóa đối xứng chia sẻ, KM-AP, sẽ được sử dụng để mã hóa/giải mã các khung dữ liệu truyền giữa thiết bị di động và AP. AS thông báo cho AP về giá trị khóa này trong Bước 3 ở Hình 8.30.

WPA3 đã được phát hành vào tháng 6 năm 2018 như một bản cập nhật cho WPA2. Bản cập nhật này giải quyết một cuộc tấn công vào giao thức bắt tay bốn bước có thể gây ra việc tái sử dụng các nonce đã sử dụng trước đó \[Vanhoef 2017\] nhưng vẫn cho phép sử dụng bắt tay bốn bước như một giao thức kế thừa và bao gồm các độ dài khóa dài hơn, cùng với các thay đổi khác \[WiFi 2019\].

**Giao thức Nhắn tin Bảo mật 802.11**

Hình 8.32 cho thấy các giao thức được sử dụng để triển khai khung bảo mật 802.11 đã được đề cập ở trên. Giao thức Xác thực Mở rộng (EAP) \[RFC 3748\] định nghĩa định dạng thông điệp đầu-cuối được sử dụng trong chế độ yêu cầu/phản hồi đơn giản giữa thiết bị di động và máy chủ xác thực, và được chứng nhận theo WPA2. Như được hiển thị trong Hình 8.32, các thông điệp EAP được đóng gói bằng EAPoL (EAP trên LAN) và gửi qua liên kết không dây 802.11. Các thông điệp EAP này sau đó được giải đóng gói tại điểm truy cập, và sau đó được đóng gói lại bằng giao thức RADIUS để

M: Thiết bị di động

AP: điểm truy cập

Mạng có dây

AS: xác thực

máy chủ

EAP TLS

EAP

EAP qua LAN (EAPoL) RADIUS

IEEE 802.11 UDP/IP

*Hình 8.32 ♦ EAP là một giao thức đầu-cuối. Các thông điệp EAP là*

được đóng gói bằng EAPoL qua liên kết không dây giữa thiết bị di động và điểm truy cập, và sử dụng RADIUS qua UDP/IP giữa điểm truy cập và máy chủ xác thực

truyền qua UDP/IP tới máy chủ xác thực. Mặc dù máy chủ và giao thức RADIUS \[RFC 2865\] không bắt buộc, chúng là các thành phần tiêu chuẩn de facto. Giao thức DIAMETER vừa được tiêu chuẩn hóa gần đây \[RFC 3588\] dự kiến sẽ thay thế RADIUS trong tương lai.

**8.8.2 Xác thực và Thỏa thuận Khóa trong Mạng Di động 4G/5G**

Trong phần này, chúng tôi mô tả cơ chế xác thực lẫn nhau và tạo khóa trong mạng 4G/5G. Nhiều phương pháp mà chúng ta sẽ gặp ở đây tương tự như những phương pháp mà chúng ta vừa nghiên cứu trong mạng 802.11, với điểm khác biệt đáng chú ý là trong mạng 4G/5G, các thiết bị di động có thể được kết nối với mạng gốc của chúng (tức là mạng nhà cung cấp dịch vụ di động mà họ đã đăng ký), hoặc có thể đang ở trạng thái đi lang thang trên mạng thăm. Trong trường hợp sau, mạng thăm và mạng gốc sẽ cần tương tác khi xác thực thiết bị di động và tạo các khóa mã hóa. Trước khi tiếp tục, bạn có thể muốn làm quen lại với kiến trúc mạng 4G/5G bằng cách đọc lại các Mục 7.4 và 7.7.1.

The goals of mutual authentication and key generation are the same in the 4G/5G setting as in the 802.11 setting. In order to encrypt the contents of frames being transmitted over the wireless channel, the mobile device and base station will need to derive a shared symmetric encryption key. In addition, the network to which the mobile device is attaching will need to authenticate the device's identity and check its access privileges. Similarly, the mobile device will also want to authenticate the network to which it is attaching. While the network's need to authenticate a mobile device may be obvious, the need for authentication in the reverse direction may not be so clear. However, there are documented cases of ne'er-do-wells operating rogue cellular base stations that entice unsuspecting mobile devices to attach to the rogue network, exposing a device to a number of attacks \[Li 2017\]. So, as in the case of 802.11 WLANs, a mobile device should exercise abundant caution when attaching to a cellular network!

Hình 8.33 minh họa kịch bản thiết bị di động kết nối với mạng di động 4G. Ở đầu Hình 8.33, chúng ta thấy nhiều thành phần 4G mà chúng ta đã gặp trước đó trong Phần 7.4---thiết bị di động (M), trạm cơ sở (BS), thực thể quản lý di động (MME) trong mạng mà thiết bị di động muốn gắn vào và dịch vụ thuê bao gia đình (HSS) trong mạng gia đình của thiết bị di động. So sánh Hình 8.30 và 8.33 cho thấy những điểm tương đồng và khác biệt giữa cài đặt bảo mật 802.11 và 4G. Chúng ta lại thấy một thiết bị di động và một trạm cơ sở; khóa phiên của người dùng được lấy trong quá trình đính kèm mạng, KBS-M, sẽ được sử dụng để mã hóa/giải mã các khung được truyền qua liên kết không dây của họ. 4G MME và HSS cùng nhau sẽ đóng vai trò tương tự như vai trò của máy chủ xác thực trong cài đặt 802.11. Lưu ý rằng HSS và thiết bị di động cũng chia sẻ một bí mật chung, KHSS-M, được cả hai thực thể biết trước khi bắt đầu xác thực. Khóa này được lưu trong thẻ SIM của thiết bị di động và trong cơ sở dữ liệu HSS trong mạng gia đình của thiết bị di động.

Giao thức Xác thực và Thỏa thuận Khóa (AKA) 4G bao gồm các bước sau:

a\. Yêu cầu xác thực đến HSS. Khi thiết bị di động lần đầu tiên yêu cầu, thông qua một

trạm gốc, để kết nối với mạng, nó gửi một thông điệp gắn kết chứa danh tính thuê bao di động quốc tế (IMSI) của nó được chuyển tiếp tới Thực thể Quản lý Di động (MME). Sau đó, MME sẽ gửi IMSI và thông tin về mạng đã truy cập (hiển thị là "thông tin VN" trong Hình 8.33) tới Dịch vụ Thuê bao Gốc (HSS) trong mạng gốc của thiết bị. Trong Phần 7.4, chúng tôi đã mô tả cách MME có thể giao tiếp với HSS thông qua mạng toàn cầu của các mạng di động liên kết với nhau. b. Phản hồi xác thực từ HSS. HSS thực hiện mã hóa

các hoạt động sử dụng khóa bí mật được chia sẻ trước, KHSS-M, để tạo ra một mã xác thực, auth_token, và một mã phản hồi xác thực dự kiến, xresHSS. auth_token chứa thông tin được HSS mã hóa bằng KHSS-M cho phép thiết bị di động biết rằng người đã tính toán auth_token biết khóa bí mật. Ví dụ, giả sử HSS tính KHSS-M(IMSI), tức là, mã hóa IMSI của thiết bị bằng KHSS-M và gửi giá trị đó dưới dạng auth_token. Khi thiết bị di động nhận giá trị đã mã hóa đó và sử dụng khóa bí mật của mình để giải mã giá trị này, tức là, để tính toán

Quản lý di động

Trạm cơ sở thực thể (MME)

(BS)

HSS

Người đăng ký chính

Dịch vụ (HSS) Thiết bị di động

\(M\)

Đã truy cập Mạng Gia đình

KHSS-M

đính kèm đính kèm YÊU_CẦU_XÁC_THỰC (IMSI, thông tin VN)

mã thông báo xác thực mã thông báo xác thực

resM resM

d OK, phím OK

sự dẫn xuất khóa

KHSS-M

KBS-M

c

e

d

cơ sở dữ liệu

một

PHẢN_HỒI_XÁC_THỰC (token xác thực, xresHSS, khóa)

*Hình 8.33 ♦ Xác thực lẫn nhau và thỏa thuận khóa trong 4G LTE*

mạng di động

KHSS-M(KHSS-M(IMSI)) 5 IMSI, nó biết rằng HSS đã tạo auth_token biết khóa bí mật của nó. Do đó, thiết bị di động có thể xác thực HSS. Mã phản hồi xác thực dự kiến, xresHSS, chứa một giá trị mà

thiết bị di động sẽ cần có khả năng tính toán (sử dụng KHSS-M) và trả về MME để chứng minh rằng nó (thiết bị di động) biết khóa bí mật, do đó xác thực thiết bị di động đối với MME. Lưu ý rằng MME chỉ đóng vai trò trung gian ở đây, nhận thông tin xác thực

thông điệp phản hồi xác thực, giữ xresHSS để sử dụng sau, trích xuất mã thông báo xác thực và chuyển tiếp nó đến thiết bị di động. Cụ thể, nó không cần biết, và sẽ không biết, khóa bí mật, KHSS-M. c. Phản hồi xác thực từ thiết bị di động. Thiết bị di động nhận

auth_token và tính toán KHSS-M(KHSS-M(IMSI)) 5 IMSI, do đó xác thực HSS. Thiết bị di động sau đó tính toán một giá trị resM---sử dụng khóa bí mật của nó để thực hiện cùng một phép tính mật mã mà HSS đã thực hiện để tính xresHSS---và gửi giá trị này đến MME. d. Xác thực thiết bị di động. MMS so sánh giá trị do thiết bị di động tính toán

của resM với giá trị xresHSS tính toán từ HSS. Nếu chúng khớp, thiết bị di động được xác thực, vì thiết bị di động đã chứng minh cho MME rằng cả nó và HSS đều biết khóa bí mật chung. MMS thông báo cho trạm gốc và thiết bị di động rằng xác thực lẫn nhau đã hoàn tất, và gửi cho trạm gốc các khóa sẽ được sử dụng trong bước e. e. Dẫn xuất khóa cho mặt bằng dữ liệu và mặt bằng điều khiển. Thiết bị di động và cơ sở

Mỗi trạm sẽ xác định các khóa được sử dụng để mã hóa/giải mã các khung truyền của họ qua kênh không dây. Các khóa riêng biệt sẽ được tạo ra cho việc truyền khung dữ liệu và khung điều khiển. Thuật toán mã hóa AES mà chúng ta đã thấy được sử dụng trong mạng 802.11 cũng được sử dụng trong mạng 4G/5G.

Cuộc thảo luận ở trên của chúng tôi đã tập trung vào xác thực và thỏa thuận khóa trong mạng 4G. Mặc dù nhiều phần của bảo mật 4G đang được tiếp tục áp dụng vào 5G, nhưng có một số thay đổi quan trọng:

• Đầu tiên, hãy lưu ý rằng trong phần thảo luận ở trên, chính MME trong mạng thăm viếng là người đưa ra quyết định xác thực. Một thay đổi quan trọng đang diễn ra trong bảo mật mạng 5G là cho phép dịch vụ xác thực được cung cấp bởi mạng gốc, trong khi mạng thăm viếng chỉ đóng vai trò trung gian nhỏ hơn. Mặc dù mạng thăm viếng vẫn có thể từ chối yêu cầu xác thực từ thiết bị di động, nhưng quyết định chấp nhận yêu cầu xác thực trong kịch bản 5G mới này phụ thuộc vào mạng gốc. • Mạng 5G sẽ hỗ trợ giao thức Xác thực và Thỏa thuận Khóa (AKA) được mô tả ở trên, cũng như hai giao thức bổ sung mới cho xác thực và thỏa thuận khóa. Một trong số này, được biết đến với tên gọi AKA¿, có liên quan chặt chẽ đến giao thức AKA của 4G. Nó cũng sử dụng khóa bí mật chia sẻ trước, KHSS-M. Tuy nhiên, vì nó sử dụng giao thức EAP mà chúng ta đã gặp trước đó trong Hình 8.33 trong bối cảnh xác thực 802.11, nên AKA¿ của 5G có các luồng thông điệp khác so với giao thức đó.

của 4G AKA. Giao thức 5G mới thứ hai được thiết kế cho môi trường IoT, và không yêu cầu một khóa bí mật được chia sẻ trước. • Một thay đổi bổ sung trong 5G là sử dụng các kỹ thuật mật mã khóa công khai để mã hóa danh tính vĩnh viễn của thiết bị (tức là IMSI của nó) sao cho nó không bao giờ được truyền dưới dạng văn bản rõ.

Trong phần này, chúng tôi chỉ tóm tắt sơ lược về xác thực lẫn nhau và thỏa thuận khóa trong mạng 4G/5G. Như chúng ta đã thấy, chúng sử dụng rộng rãi các kỹ thuật bảo mật mà chúng ta đã nghiên cứu trước đó trong chương này. Thông tin chi tiết hơn về bảo mật 4G/5G có thể được tìm thấy trong \[3GPP SAE 2019; Cable Labs 2019; Cichonski 2017\].

**8.9 An ninh Vận hành: Tường lửa và Hệ thống Phát hiện Xâm nhập**

We've seen throughout this chapter that the Internet is not a very safe place---bad guys are out there, wreaking all sorts of havoc. Given the hostile nature of the Internet, let's now consider an organization's network and the network administrator who administers it. From a network administrator's point of view, the world divides quite neatly into two camps---the good guys (who belong to the organization's network, and who should be able to access resources inside the organization's network in a relatively unconstrained manner) and the bad guys (everyone else, whose access to network resources must be carefully scrutinized). In many organizations, ranging from medieval castles to modern corporate office buildings, there is a single point of entry/exit where both good guys and bad guys entering and leaving the organization are security-checked. In a castle, this was done at a gate at one end of the drawbridge; in a corporate building, this is done at the security desk. In a computer network, when traffic entering/leaving a network is security-checked, logged, dropped, or forwarded, it is done by operational devices known as firewalls, intrusion detection systems (IDSs), and intrusion prevention systems (IPSs).

**8.9.1 Tường lửa**

Tường lửa là sự kết hợp giữa phần cứng và phần mềm, ngăn cách mạng nội bộ của tổ chức với Internet rộng lớn, cho phép một số gói dữ liệu đi qua và chặn các gói khác. Tường lửa cho phép quản trị viên mạng kiểm soát quyền truy cập giữa thế giới bên ngoài và các tài nguyên bên trong mạng được quản lý bằng cách quản lý luồng lưu lượng đến và đi từ các tài nguyên này. Tường lửa có ba mục tiêu:

• Tất cả lưu lượng từ bên ngoài vào bên trong, và ngược lại, đều đi qua tường lửa. Hình 8.34 cho thấy một tường lửa, nằm chính giữa ranh giới giữa mạng được quản lý và phần còn lại của Internet. Trong khi các tổ chức lớn có thể sử dụng

nhiều lớp tường lửa hoặc tường lửa phân tán \[Skoudis 2006\], việc đặt một tường lửa tại một điểm truy cập duy nhất vào mạng, như minh họa trong Hình 8.34, giúp dễ dàng quản lý và thực thi chính sách truy cập an ninh. • Chỉ lưu lượng được phép, theo định nghĩa của chính sách an ninh địa phương, sẽ được cho phép đi qua. Khi tất cả lưu lượng vào và ra khỏi mạng tổ chức phải đi qua tường lửa, tường lửa có thể hạn chế quyền truy cập cho lưu lượng được phép. • Bản thân tường lửa không bị xâm nhập. Tường lửa bản thân là một thiết bị kết nối với mạng. Nếu không được thiết kế hoặc lắp đặt đúng cách, nó có thể bị xâm nhập, trong trường hợp đó nó chỉ cung cấp một cảm giác an toàn giả (ngay cả còn tệ hơn là không có tường lửa!).

Cisco và Check Point là hai trong số các nhà cung cấp tường lửa hàng đầu hiện nay. Bạn cũng có thể dễ dàng tạo một tường lửa (bộ lọc gói) từ một máy Linux bằng cách sử dụng iptables (phần mềm công cộng thường được đi kèm với Linux). Hơn nữa, như đã thảo luận trong Chương 4 và 5, tường lửa hiện nay thường được triển khai trong các bộ định tuyến và được điều khiển từ xa bằng cách sử dụng SDN.

Tường lửa có thể được phân loại thành ba loại: bộ lọc gói dữ liệu truyền thống, bộ lọc trạng thái và cổng ứng dụng. Chúng ta sẽ lần lượt đề cập đến từng loại trong các mục phụ sau đây.

*Hình 8.34 ♦ Vị trí tường lửa giữa mạng được quản lý và*

thế giới bên ngoài

Được quản lý

mạng

Tường lửa

Internet công cộng

Bộ lọc Packet truyền thống

Như được minh họa trong Hình 8.34, một tổ chức thường có một bộ định tuyến cổng (gateway router) kết nối mạng nội bộ của nó với ISP (và do đó với Internet công cộng rộng lớn hơn). Tất cả lưu lượng ra vào mạng nội bộ đều đi qua bộ định tuyến này, và chính tại bộ định tuyến này việc lọc gói dữ liệu diễn ra. Bộ lọc gói dữ liệu kiểm tra từng datagram một cách riêng lẻ, xác định xem datagram có nên được phép đi qua hay nên bị loại bỏ dựa trên các quy tắc cụ thể của quản trị viên. Các quyết định lọc thường dựa trên:

• Địa chỉ nguồn hoặc đích IP • Loại giao thức trong trường IP của gói tin: TCP, UDP, ICMP, OSPF, v.v. • Cổng nguồn và đích TCP hoặc UDP • Các bit cờ TCP: SYN, ACK, v.v. • Loại thông điệp ICMP • Các quy tắc khác nhau cho các gói tin ra vào mạng • Các quy tắc khác nhau cho các giao diện bộ định tuyến khác nhau

Một quản trị viên mạng cấu hình tường lửa dựa trên chính sách của tổ chức. Chính sách này có thể xem xét năng suất của người dùng và việc sử dụng băng thông cũng như các mối quan tâm về bảo mật của tổ chức. Bảng 8.5 liệt kê một số chính sách mà tổ chức có thể có và cách chúng sẽ được xử lý với bộ lọc gói. Ví dụ, nếu tổ chức không muốn bất kỳ kết nối TCP nào đến ngoại trừ những kết nối dành cho máy chủ Web công cộng của mình, nó có thể chặn tất cả các phân đoạn SYN TCP đến ngoại trừ các phân đoạn SYN TCP có cổng đích là 80 và địa chỉ IP đích tương ứng với máy chủ Web. Nếu tổ chức không muốn người dùng của mình chiếm dụng băng thông truy cập với các ứng dụng radio Internet, nó có thể chặn tất cả các kết nối không quan trọng

Bảng 8.5 ♦ Chính sách và các quy tắc lọc tương ứng cho tổ chức

mạng 130.207/16 với máy chủ Web tại 130.207.244.203

Cài đặt Tường lửa Chính sách

Không truy cập Web từ bên ngoài. Loại bỏ tất cả các gói đi đến bất kỳ địa chỉ IP nào, cổng 80.

Không có kết nối TCP đến, ngoại trừ những kết nối chỉ dành cho máy chủ Web công cộng của tổ chức.

Bỏ tất cả các gói SYN TCP đến bất kỳ IP nào ngoại trừ 130.207.244.203, cổng 80.

Ngăn chặn radio trên web tiêu tốn băng thông có sẵn.

Bỏ tất cả các gói UDP đến ngoại trừ các gói DNS.

Ngăn mạng của bạn bị sử dụng để thực hiện tấn công DoS loại smurf.

Loại bỏ tất cả các gói tin ICMP ping gửi đến địa chỉ "broadcast" (ví dụ 130.207.255.255).

Ngăn mạng của bạn bị truy vết đường đi. Loại bỏ tất cả lưu lượng ICMP TTL hết hạn đi ra ngoài.

UDP lưu lượng (vì radio Internet thường được gửi qua UDP). Nếu tổ chức không muốn mạng nội bộ của mình bị người ngoài lập bản đồ (tracerouted), họ có thể chặn tất cả các thông điệp TTL hết hạn ICMP rời khỏi mạng của tổ chức.

Chính sách lọc có thể dựa trên sự kết hợp của địa chỉ và số cổng. Ví dụ, một bộ định tuyến lọc có thể chuyển tiếp tất cả các gói tin Telnet (những gói có số cổng là 23) ngoại trừ những gói đi tới và đi từ danh sách các địa chỉ IP cụ thể. Chính sách này cho phép các kết nối Telnet đi đến và từ các máy chủ trong danh sách được phép. Thật không may, việc dựa vào các địa chỉ bên ngoài để thiết lập chính sách không cung cấp sự bảo vệ nào chống lại các gói tin có địa chỉ nguồn bị giả mạo.

Lọc cũng có thể dựa trên việc bit ACK của TCP có được đặt hay không. Thủ thuật này khá hữu ích nếu một tổ chức muốn cho phép các máy khách nội bộ kết nối với các máy chủ bên ngoài nhưng muốn ngăn các máy khách bên ngoài kết nối với các máy chủ nội bộ. Nhớ lại từ Phần 3.5 rằng đoạn đầu tiên trong mỗi kết nối TCP có bit ACK được đặt thành 0, trong khi tất cả các đoạn khác trong kết nối đều có bit ACK được đặt thành 1. Do đó, nếu một tổ chức muốn ngăn chặn các máy khách bên ngoài khởi tạo kết nối đến các máy chủ nội bộ, nó chỉ cần lọc tất cả các đoạn đến có bit ACK được đặt thành 0. Chính sách này chặn tất cả các kết nối TCP xuất phát từ bên ngoài, nhưng cho phép các kết nối xuất phát từ bên trong.

Các quy tắc tường lửa được triển khai trên các bộ định tuyến thông qua danh sách kiểm soát truy cập, với mỗi giao diện bộ định tuyến có danh sách riêng của nó. Một ví dụ về một danh sách kiểm soát truy cập cho tổ chức 222.22/16 được trình bày trong Bảng 8.6. Danh sách kiểm soát truy cập này dành cho một giao diện kết nối bộ định tuyến với các nhà cung cấp dịch vụ Internet bên ngoài của tổ chức. Các quy tắc được áp dụng cho mỗi gói dữ liệu đi qua giao diện từ trên xuống dưới. Hai quy tắc đầu tiên cùng nhau cho phép người dùng nội bộ truy cập Web: Quy tắc đầu tiên cho phép bất kỳ gói TCP nào với cổng đích 80 ra khỏi mạng của tổ chức; quy tắc thứ hai cho phép bất kỳ gói TCP nào với cổng nguồn 80 và bit ACK được đặt vào mạng của tổ chức. Lưu ý rằng nếu một nguồn bên ngoài cố gắng thiết lập kết nối TCP với

Bảng 8.6 ♦ Một danh sách kiểm soát truy cập cho giao diện bộ định tuyến

hành động địa chỉ nguồn địa chỉ đích giao thức cổng nguồn cổng đích bit cờ

cho phép 222.22/16 ngoài 222.22/16 TCP \> 1023 bất kỳ

cho phép bên ngoài 222.22/16 222.22/16 TCP \> 1023 ACK

cho phép 222.22/16 ngoài 222.22/16 UDP \> 1023 ---

cho phép bên ngoài 222.22/16 222.22/16 UDP \> 1023 ---

từ chối tất cả tất cả tất cả tất cả tất cả tất cả

một máy chủ nội bộ, kết nối sẽ bị chặn, ngay cả khi cổng nguồn hoặc cổng đích là 80. Hai quy tắc tiếp theo cùng nhau cho phép các gói DNS vào và ra khỏi mạng của tổ chức. Tóm lại, danh sách kiểm soát truy cập có phần hạn chế này chặn tất cả lưu lượng trừ lưu lượng Web được khởi tạo từ bên trong tổ chức và lưu lượng DNS. \[CERT Filtering 2012\] cung cấp danh sách các bộ lọc gói cổng/giao thức được khuyến nghị để tránh một số lỗ hổng bảo mật nổi tiếng trong các ứng dụng mạng hiện có.

Độc giả có trí nhớ tốt có thể nhớ rằng chúng ta đã gặp các danh sách kiểm soát truy cập tương tự như Bảng 8.6 khi chúng ta nghiên cứu chuyển tiếp tổng quát trong Mục 4.4.3 của Chương 4. Thật vậy, chúng tôi đã cung cấp một ví dụ ở đó về cách các quy tắc chuyển tiếp tổng quát có thể được sử dụng để xây dựng tường lửa lọc gói tin.

Bộ lọc Packet có trạng thái

Trong bộ lọc gói truyền thống, các quyết định lọc được thực hiện trên từng gói một cách độc lập. Các bộ lọc trạng thái thực sự theo dõi các kết nối TCP, và sử dụng kiến thức này để đưa ra các quyết định lọc.

Để hiểu các bộ lọc trạng thái, hãy xem lại danh sách kiểm soát truy cập trong Bảng 8.6. Mặc dù khá hạn chế, danh sách kiểm soát truy cập trong Bảng 8.6 vẫn cho phép bất kỳ gói tin nào từ bên ngoài đến với ACK = 1 và cổng nguồn 80 đi qua bộ lọc. Những gói tin như vậy có thể được tin tặc sử dụng để cố gắng làm sập các hệ thống nội bộ bằng các gói tin bị hỏng, tiến hành các cuộc tấn công từ chối dịch vụ hoặc lập bản đồ mạng nội bộ. Giải pháp đơn giản là chặn các gói ACK TCP cũng, nhưng cách tiếp cận này sẽ ngăn người dùng nội bộ của tổ chức truy cập Web.

Bộ lọc trạng thái (stateful) giải quyết vấn đề này bằng cách theo dõi tất cả các kết nối TCP đang diễn ra trong một bảng kết nối. Điều này có thể thực hiện được vì tường lửa có thể quan sát sự bắt đầu của một kết nối mới thông qua việc quan sát quá trình bắt tay ba bước (SYN, SYNACK và ACK); và nó có thể quan sát sự kết thúc của một kết nối khi thấy một gói FIN cho kết nối đó. Tường lửa cũng có thể (một cách thận trọng) giả định rằng kết nối đã kết thúc khi không thấy bất kỳ hoạt động nào trên kết nối đó trong, ví dụ, 60 giây. Một bảng kết nối ví dụ cho tường lửa được hiển thị trong Bảng 8.7. Bảng kết nối này chỉ ra rằng hiện tại có ba kết nối TCP đang diễn ra, tất cả đều được khởi tạo từ bên trong tổ chức. Ngoài ra, bộ lọc trạng thái bao gồm một cột mới, "kiểm tra kết nối", trong danh sách kiểm soát truy cập của nó, như

Bảng 8.7 ♦ Bảng kết nối cho bộ lọc có trạng thái

địa chỉ nguồn địa chỉ đích cổng nguồn cổng đích

222.22.1.7 37.96.87.123 12699

222.22.93.2 199.1.205.23 37654

222.22.65.143 203.77.240.43 48712

được hiển thị trong Bảng 8.8. Lưu ý rằng Bảng 8.8 giống hệt với danh sách kiểm soát truy cập trong Bảng 8.6, ngoại trừ bây giờ nó cho thấy rằng kết nối cần được kiểm tra theo hai trong số các quy tắc.

Hãy cùng xem qua một số ví dụ để xem bảng kết nối và danh sách kiểm soát truy cập mở rộng hoạt động như thế nào. Giả sử kẻ tấn công cố gắng gửi một gói không đúng định dạng vào mạng của tổ chức bằng cách gửi một gói dữ liệu có cổng nguồn TCP 80 và có cờ ACK được đặt. Hơn nữa, giả sử rằng gói này có số cổng nguồn 12543 và địa chỉ nguồn IP 150.23.23.155. Khi gói này đến tường lửa, tường lửa sẽ kiểm tra danh sách kiểm soát truy cập trong Bảng 8.7, trong đó cho biết bảng kết nối cũng phải được kiểm tra trước khi cho phép gói này vào mạng của tổ chức. Tường lửa kiểm tra bảng kết nối một cách hợp lệ, thấy rằng gói này không phải là một phần của kết nối TCP đang diễn ra và từ chối gói. Ví dụ thứ hai, giả sử một người dùng nội bộ muốn lướt một trang Web bên ngoài. Vì người dùng này trước tiên gửi phân đoạn TCP SYN nên kết nối TCP của người dùng sẽ được ghi lại trong bảng kết nối. Khi máy chủ Web gửi lại các gói (với bit ACK nhất thiết phải được đặt), tường lửa sẽ kiểm tra bảng và thấy rằng một kết nối tương ứng đang được tiến hành. Do đó, tường lửa sẽ cho phép các gói này đi qua, do đó không can thiệp vào hoạt động lướt Web của người dùng nội bộ.

Cổng ứng dụng

Trong các ví dụ trên, chúng ta đã thấy rằng lọc ở cấp gói cho phép một tổ chức thực hiện lọc thô dựa trên nội dung của các header IP và TCP/UDP, bao gồm địa chỉ IP, số cổng và các bit xác nhận. Nhưng nếu một tổ chức muốn cung cấp dịch vụ Telnet cho một tập hợp người dùng nội bộ bị giới hạn thì sao

Bảng 8.8 ♦ Danh sách kiểm soát truy cập cho bộ lọc duy trì trạng thái

địa chỉ nguồn hành động

địa chỉ đích

giao thức cổng nguồn cổng đích cờ bit kiểm tra kết nối

cho phép 222.22/16 ngoài 222.22/16 TCP \> 1023 bất kỳ

cho phép bên ngoài 222.22/16 222.22/16 TCP \> 1023 ACK X

cho phép 222.22/16 ngoài 222.22/16 UDP \> 1023 ---

cho phép bên ngoài 222.22/16 222.22/16 UDP \> 1023 --- X

từ chối tất cả tất cả tất cả tất cả tất cả tất cả

(khác với địa chỉ IP)? Vậy còn nếu tổ chức muốn những người dùng được đặc quyền này xác thực bản thân trước khi được phép tạo các phiên Telnet ra thế giới bên ngoài thì sao? Những nhiệm vụ như vậy vượt quá khả năng của các bộ lọc truyền thống và bộ lọc có trạng thái. Thật vậy, thông tin về danh tính của người dùng nội bộ là dữ liệu lớp ứng dụng và không được bao gồm trong các tiêu đề IP/TCP/UDP.

Để có mức độ bảo mật tinh vi hơn, tường lửa phải kết hợp bộ lọc gói với cổng ứng dụng. Cổng ứng dụng nhìn vượt ra ngoài các tiêu đề IP/TCP/UDP và đưa ra quyết định chính sách dựa trên dữ liệu ứng dụng. Một cổng ứng dụng là một máy chủ chuyên biệt theo ứng dụng mà qua đó tất cả dữ liệu ứng dụng (vào và ra) phải đi qua. Nhiều cổng ứng dụng có thể chạy trên cùng một máy chủ, nhưng mỗi cổng là một máy chủ riêng biệt với các tiến trình của riêng nó.

Để hiểu thêm về các cổng ứng dụng, hãy thiết kế một tường lửa chỉ cho phép một tập hợp hạn chế các người dùng nội bộ sử dụng Telnet ra bên ngoài và ngăn tất cả các khách hàng bên ngoài Telnet vào bên trong. Chính sách như vậy có thể thực hiện bằng cách kết hợp giữa bộ lọc gói (trên bộ định tuyến) và cổng ứng dụng Telnet, như minh họa trong Hình 8.35. Bộ lọc của bộ định tuyến được cấu hình để chặn tất cả các kết nối Telnet ngoại trừ những kết nối xuất phát từ địa chỉ IP của cổng ứng dụng. Cấu hình bộ lọc như vậy buộc tất cả kết nối Telnet đi ra ngoài phải đi qua cổng ứng dụng. Bây giờ hãy xem xét một người dùng nội bộ muốn Telnet ra thế giới bên ngoài. Người dùng phải thiết lập một phiên Telnet với cổng ứng dụng trước. Một ứng dụng chạy trong cổng, lắng nghe các phiên Telnet đến, sẽ nhắc

*Hình 8.35 ♦ Tường lửa bao gồm một cổng ứng dụng và một bộ lọc*

Ứng dụng

cổng

Host-tới-cổng

Phiên Telnet

Cổng đến từ xa

chủ phiên Telnet

Router và lọc

yêu cầu người dùng nhập ID người dùng và mật khẩu. Khi người dùng cung cấp thông tin này, cổng ứng dụng sẽ kiểm tra xem người dùng có quyền Telnet ra bên ngoài hay không. Nếu không, kết nối Telnet từ người dùng nội bộ đến cổng sẽ bị cổng chặn. Nếu người dùng có quyền, thì cổng sẽ (1) yêu cầu người dùng nhập tên máy chủ của máy chủ bên ngoài mà người dùng muốn kết nối, (2) thiết lập phiên Telnet giữa cổng và máy chủ bên ngoài, và (3) chuyển tiếp tất cả dữ liệu từ người dùng đến máy chủ bên ngoài, và chuyển tiếp tất cả dữ liệu từ máy chủ bên ngoài đến người dùng. Do đó, cổng ứng dụng Telnet không chỉ thực hiện xác thực người dùng mà còn đóng vai trò như một máy chủ Telnet và một khách hàng Telnet, chuyển tiếp thông tin giữa người dùng và máy chủ Telnet từ xa. Lưu ý rằng bộ lọc sẽ cho phép bước 2 vì cổng khởi xướng kết nối Telnet ra bên ngoài.

ẨN DANH VÀ RIÊNG TƯ

Giả sử bạn muốn truy cập một trang Web gây tranh cãi (ví dụ, một trang của nhà hoạt động chính trị) và bạn (1) không muốn tiết lộ địa chỉ IP của mình cho trang Web, (2) không muốn ISP địa phương của bạn (có thể là ISP ở nhà hoặc văn phòng) biết rằng bạn đang truy cập trang đó, và (3) không muốn ISP địa phương thấy dữ liệu bạn đang trao đổi với trang Web. Nếu bạn sử dụng phương pháp truyền thống kết nối trực tiếp tới trang Web mà không có bất kỳ mã hóa nào, bạn sẽ thất bại ở cả ba điểm. Ngay cả khi bạn sử dụng SSL, bạn cũng thất bại ở hai điểm đầu tiên: Địa chỉ IP nguồn của bạn được trình bày cho trang Web trong mỗi gói dữ liệu bạn gửi; và địa chỉ đích của mỗi gói mà bạn gửi có thể dễ dàng bị ISP địa phương đánh hơi.

Để đạt được quyền riêng tư và ẩn danh, bạn có thể sử dụng kết hợp giữa một máy chủ proxy đáng tin cậy và SSL, như minh họa trong Hình 8.36. Với phương pháp này, trước tiên bạn thực hiện một kết nối SSL tới proxy đáng tin cậy. Sau đó, bạn gửi, vào kết nối SSL này,

TIỀN SỬ BỆNH

*Hình 8.36 ♦ Cung cấp ẩn danh và quyền riêng tư với một máy chủ proxy*

Alice

Vô danh hóa

Đại diện

SSL

Văn bản rõ

một yêu cầu HTTP cho một trang tại trang web mong muốn. Khi proxy nhận được yêu cầu HTTP được mã hóa SSL, nó giải mã yêu cầu và chuyển tiếp yêu cầu HTTP dạng văn bản rõ ràng đến trang web. Trang web sau đó phản hồi cho proxy, và proxy chuyển tiếp phản hồi này cho bạn qua SSL. Bởi vì trang web chỉ thấy địa chỉ IP của proxy, chứ không phải địa chỉ của máy khách của bạn, bạn thực sự đang truy cập trang web một cách ẩn danh. Và vì tất cả lưu lượng giữa bạn và proxy đều được mã hóa, nhà cung cấp dịch vụ Internet địa phương của bạn không thể xâm phạm quyền riêng tư bằng cách ghi lại các trang bạn đã truy cập hoặc ghi lại dữ liệu bạn đang trao đổi. Nhiều công ty ngày nay (như proxify.com) cung cấp các dịch vụ proxy như vậy.

Tất nhiên, trong giải pháp này, proxy của bạn biết mọi thứ: Nó biết địa chỉ IP của bạn và địa chỉ IP của trang web bạn đang lướt; và nó có thể thấy tất cả lưu lượng ở dạng văn bản rõ ràng được trao đổi giữa bạn và trang Web. Do đó, giải pháp như vậy chỉ tốt khi có độ tin cậy của người được ủy quyền. Một cách tiếp cận mạnh mẽ hơn, được dịch vụ bảo mật và ẩn danh TOR thực hiện, là định tuyến lưu lượng truy cập của bạn thông qua một loạt máy chủ proxy không thông đồng \[TOR 2020\]. Đặc biệt, TOR cho phép các cá nhân độc lập đóng góp proxy vào nhóm proxy của nó. Khi người dùng kết nối với máy chủ bằng TOR, TOR sẽ chọn ngẫu nhiên (từ nhóm proxy của nó) một chuỗi gồm ba proxy và định tuyến tất cả lưu lượng truy cập giữa máy khách và máy chủ qua chuỗi. Theo cách này, giả sử các proxy không thông đồng, không ai biết rằng giao tiếp diễn ra giữa địa chỉ IP của bạn và trang Web mục tiêu. Hơn nữa, mặc dù văn bản rõ ràng được gửi giữa proxy cuối cùng và máy chủ, proxy cuối cùng không biết địa chỉ IP nào đang gửi và nhận văn bản rõ ràng.

Mạng nội bộ thường có nhiều cổng ứng dụng, ví dụ, các cổng cho Telnet, HTTP, FTP và e-mail. Trên thực tế, máy chủ thư của một tổ chức (xem Mục 2.3) và bộ nhớ đệm Web là các cổng ứng dụng.

Cổng ứng dụng cũng không thiếu nhược điểm. Thứ nhất, cần một cổng ứng dụng khác nhau cho mỗi ứng dụng. Thứ hai, sẽ có một mức phạt về hiệu suất phải trả, vì tất cả dữ liệu sẽ được chuyển tiếp qua cổng. Điều này trở thành mối quan tâm đặc biệt khi nhiều người dùng hoặc ứng dụng sử dụng cùng một máy cổng. Cuối cùng, phần mềm khách hàng phải biết cách liên hệ với cổng khi người dùng thực hiện yêu cầu, và phải biết cách thông báo cho cổng ứng dụng máy chủ bên ngoài nào cần kết nối.

**8.9.2 Hệ thống Phát hiện Xâm nhập**

Chúng ta vừa thấy rằng một bộ lọc gói (truyền thống và có trạng thái) kiểm tra các trường tiêu đề IP, TCP, UDP, và ICMP khi quyết định những gói nào được phép đi qua tường lửa. Tuy nhiên, để phát hiện nhiều loại tấn công, chúng ta cần thực hiện kiểm tra gói sâu, tức là nhìn xa hơn các trường tiêu đề và vào dữ liệu ứng dụng thực tế mà các gói mang theo. Như chúng ta đã thấy ở Mục 8.9.1, các cổng ứng dụng thường thực hiện kiểm tra gói sâu. Nhưng một cổng ứng dụng chỉ thực hiện điều này cho một ứng dụng cụ thể.

Clearly, there is a niche for yet another device---a device that not only examines the headers of all packets passing through it (like a packet filter), but also performs deep packet inspection (unlike a packet filter). When such a device observes a suspicious packet, or a suspicious series of packets, it could prevent those packets from entering the organizational network. Or, because the activity is only deemed as suspicious, the device could let the packets pass, but send alerts to a network administrator, who can then take a closer look at the traffic and take appropriate actions. A device that generates alerts when it observes potentially malicious traffic is called an intrusion detection system (IDS). A device that filters out suspicious traffic is called an intrusion prevention system (IPS). In this section we study both systems---IDS and IPS---together, since the most interesting technical aspect of these systems is how they detect suspicious traffic (and not whether they send alerts or drop packets). We will henceforth collectively refer to IDS systems and IPS systems as IDS systems.

Một IDS có thể được sử dụng để phát hiện một loạt các cuộc tấn công, bao gồm lập bản đồ mạng (phát sinh, ví dụ, từ nmap), quét cổng, quét ngăn xếp TCP, các cuộc tấn công DoS làm tràn băng thông, sâu máy tính và virus, các cuộc tấn công khai thác lỗ hổng hệ điều hành, và các cuộc tấn công khai thác lỗ hổng ứng dụng. (Xem Mục 1.6 để khảo sát các cuộc tấn công mạng.) Ngày nay, hàng nghìn tổ chức sử dụng hệ thống IDS. Nhiều hệ thống đã triển khai này là hệ thống sở hữu độc quyền, được tiếp thị bởi Cisco, Check Point và các nhà cung cấp thiết bị bảo mật khác. Nhưng nhiều hệ thống IDS đã triển khai là hệ thống công cộng, chẳng hạn như hệ thống IDS Snort rất phổ biến (mà chúng ta sẽ thảo luận ngay sau đây).

Một tổ chức có thể triển khai một hoặc nhiều cảm biến IDS trong mạng tổ chức của mình. Hình 8.37 cho thấy một tổ chức có ba cảm biến IDS. Khi nhiều cảm biến được triển khai, chúng thường hoạt động phối hợp, gửi thông tin về hoạt động lưu lượng đáng ngờ tới bộ xử lý IDS trung tâm, bộ này thu thập và tích hợp thông tin và gửi cảnh báo tới các quản trị viên mạng khi thấy phù hợp. Trong Hình 8.37, tổ chức đã phân vùng mạng của mình thành hai khu vực: một khu vực bảo mật cao, được bảo vệ bằng bộ lọc gói tin và cổng ứng dụng và được các cảm biến IDS giám sát; và một khu vực bảo mật thấp hơn---được gọi là vùng phi quân sự (DMZ)---chỉ được bảo vệ bằng bộ lọc gói tin, nhưng cũng được các cảm biến IDS giám sát. Lưu ý rằng DMZ bao gồm các máy chủ của tổ chức cần giao tiếp với bên ngoài, chẳng hạn như máy chủ Web công cộng và máy chủ DNS có thẩm quyền.

Bạn có thể đang tự hỏi ở giai đoạn này, tại sao lại cần nhiều cảm biến IDS? Tại sao không chỉ đặt một cảm biến IDS ngay phía sau bộ lọc gói tin (hoặc thậm chí tích hợp với bộ lọc gói tin) như trong Hình 8.37? Chúng ta sẽ sớm thấy rằng một IDS không chỉ cần thực hiện kiểm tra gói tin sâu mà còn phải so sánh mỗi gói tin đi qua với hàng chục nghìn "chữ ký"; điều này có thể là một lượng xử lý đáng kể, đặc biệt nếu tổ chức nhận được lưu lượng gigabit/giây từ Internet. Bằng cách đặt các cảm biến IDS xa hơn về phía hạ lưu, mỗi cảm biến chỉ nhìn thấy một phần lưu lượng của tổ chức, và có thể dễ dàng theo kịp. Tuy nhiên, các hệ thống IDS và IPS hiệu suất cao hiện nay đã có sẵn, và nhiều tổ chức thực sự có thể chỉ cần một cảm biến đặt gần bộ định tuyến truy cập của mình.

Hệ thống IDS được phân loại rộng rãi thành hai loại: hệ thống dựa trên chữ ký hoặc hệ thống dựa trên hành vi bất thường. Một IDS dựa trên chữ ký duy trì một cơ sở dữ liệu rộng lớn các chữ ký tấn công. Mỗi chữ ký là một tập hợp các quy tắc liên quan đến một hoạt động xâm nhập. Một chữ ký có thể chỉ đơn giản là danh sách các đặc điểm về một gói một gói (ví dụ: số cổng nguồn và đích, loại giao thức và một chuỗi bit cụ thể trong phần tải của gói), hoặc có thể liên quan đến một chuỗi các gói. Các chữ ký này thường được tạo ra bởi các kỹ sư bảo mật mạng có tay nghề cao, những người nghiên cứu các cuộc tấn công đã biết. Người quản trị mạng của một tổ chức có thể tùy chỉnh các chữ ký hoặc thêm chữ ký của riêng họ vào cơ sở dữ liệu.

Về mặt vận hành, một hệ thống IDS dựa trên chữ ký sẽ theo dõi mọi gói tin đi qua nó, so sánh từng gói tin được theo dõi với các chữ ký trong cơ sở dữ liệu của nó. Nếu một gói tin (hoặc một loạt gói tin) khớp với một chữ ký trong cơ sở dữ liệu, IDS sẽ tạo ra một cảnh báo. Cảnh báo có thể được gửi cho quản trị viên mạng qua một tin nhắn e-mail, có thể được gửi đến hệ thống quản lý mạng, hoặc chỉ đơn giản là được ghi lại để kiểm tra trong tương lai.

*Hình 8.37 ♦ Một tổ chức triển khai bộ lọc, cổng ứng dụng,*

và cảm biến IDS

Internet

Máy chủ web

máy chủ FTP

máy chủ DNS

Mạng nội bộ

Ứng dụng

cổng

Khu phi quân sự

Bộ lọc

Chìa khóa:

= cảm biến IDS

Hệ thống IDS dựa trên chữ ký, mặc dù được triển khai rộng rãi, có một số hạn chế. Quan trọng nhất, chúng yêu cầu kiến thức trước về cuộc tấn công để tạo ra một chữ ký chính xác. Nói cách khác, một IDS dựa trên chữ ký hoàn toàn mù lòa trước các cuộc tấn công mới chưa được ghi nhận. Một nhược điểm khác là ngay cả khi một chữ ký được khớp, nó có thể không phải là kết quả của một cuộc tấn công, dẫn đến cảnh báo giả. Cuối cùng, vì mỗi gói dữ liệu phải được so sánh với một bộ sưu tập chữ ký rộng lớn, IDS có thể bị quá tải trong quá trình xử lý và thực sự không phát hiện được nhiều gói dữ liệu độc hại.

Hệ thống IDS dựa trên bất thường tạo một hồ sơ lưu lượng khi quan sát lưu lượng trong hoạt động bình thường. Nó sau đó tìm kiếm các luồng gói tin có thống kê bất thường, ví dụ, tỷ lệ phần trăm ICMP gói tin quá mức hoặc sự tăng trưởng theo cấp số nhân đột ngột trong việc quét cổng và quét ping. Điều tuyệt vời về các hệ thống IDS dựa trên bất thường là chúng không dựa vào kiến thức trước về các cuộc tấn công hiện có---tức là, chúng có khả năng phát hiện các cuộc tấn công mới chưa được ghi chép. Mặt khác, việc phân biệt giữa lưu lượng bình thường và lưu lượng thống kê bất thường là một vấn đề cực kỳ khó khăn. Cho đến nay, hầu hết các triển khai IDS chủ yếu dựa trên chữ ký, mặc dù một số bao gồm một số tính năng dựa trên bất thường.

Hít khịt

Snort là một IDS mã nguồn mở, thuộc miền công cộng với hàng trăm nghìn lần triển khai hiện có \[Snort 2012; Koziol 2003\]. Nó có thể chạy trên các nền tảng Linux, UNIX và Windows. Nó sử dụng giao diện sniffing chung libpcap, cũng được Wireshark và nhiều công cụ dò gói tin khác sử dụng. Nó có thể dễ dàng xử lý lưu lượng 100 Mbps; đối với các cài đặt có tốc độ lưu lượng gigabit/giây, có thể cần nhiều cảm biến Snort.

Để có được một vài hiểu biết về Snort, hãy cùng xem một ví dụ về chữ ký Snort:

cảnh báo icmp \$EXTERNAL_NET bất kỳ -\> \$HOME_NET bất kỳ (msg:"ICMP PING NMAP"; dsize: 0; itype: 8;)

Chữ ký này được khớp với bất kỳ gói ICMP nào đi vào mạng của tổ chức (\$HOME_NET) từ bên ngoài (\$EXTERNAL_NET), có loại 8 (ICMP ping), và có phần dữ liệu trống (dsize = 0). Vì nmap (xem Phần 1.6) tạo ra các gói ping với những đặc điểm cụ thể này, chữ ký này được thiết kế để phát hiện quét ping nmap. Khi một gói được khớp với chữ ký này, Snort sẽ tạo cảnh báo kèm theo thông điệp "ICMP PING NMAP".

Có lẽ điều ấn tượng nhất về Snort là cộng đồng rộng lớn các người dùng và chuyên gia bảo mật duy trì cơ sở dữ liệu chữ ký của nó. Thông thường, chỉ trong vài giờ sau khi một cuộc tấn công mới xuất hiện, cộng đồng Snort sẽ viết và phát hành chữ ký của cuộc tấn công đó, sau đó được hàng trăm nghìn triển khai Snort trên toàn thế giới tải về. Hơn nữa, bằng cách sử dụng cú pháp chữ ký Snort, các quản trị viên mạng có thể điều chỉnh các chữ ký theo nhu cầu của tổ chức mình bằng cách sửa đổi các chữ ký hiện có hoặc tạo các chữ ký hoàn toàn mới.

**8.10 Tóm tắt**

Trong chương này, chúng ta đã xem xét các cơ chế khác nhau mà những người tình bí mật của chúng ta, Bob và Alice, có thể sử dụng để giao tiếp một cách an toàn. Chúng ta đã thấy rằng Bob và Alice quan tâm đến tính bảo mật (để chỉ họ mới có thể hiểu nội dung của một tin nhắn được truyền đi), xác thực điểm cuối (để họ chắc chắn rằng họ đang nói chuyện với nhau), và tính toàn vẹn của tin nhắn (để họ chắc chắn rằng các tin nhắn của họ không bị thay đổi trong quá trình truyền). Tất nhiên, nhu cầu về giao tiếp an toàn không chỉ giới hạn ở những người tình bí mật. Thật vậy, chúng ta đã thấy trong các Mục 8.5 đến 8.8 rằng bảo mật có thể được sử dụng ở nhiều lớp khác nhau trong kiến trúc mạng để bảo vệ chống lại những kẻ xấu có một kho tàng các hình thức tấn công sẵn có.

Phần đầu của chương này trình bày các nguyên tắc khác nhau về cơ sở của việc truyền thông an toàn. Trong Mục 8.2, chúng tôi đã đề cập đến các kỹ thuật mã hóa để mã hóa và giải mã dữ liệu, bao gồm mã hóa khóa đối xứng và mã hóa khóa công khai. DES và RSA đã được xem xét như các nghiên cứu điển hình cụ thể của hai lớp kỹ thuật mã hóa chính được sử dụng trong các mạng ngày nay.

Trong Phần 8.3, chúng ta đã xem xét hai phương pháp để đảm bảo tính toàn vẹn của thông điệp: mã xác thực thông điệp (MAC) và chữ ký số. Hai phương pháp này có một số điểm tương đồng. Cả hai đều sử dụng các hàm băm mật mã và cả hai kỹ thuật đều cho phép chúng ta xác minh nguồn gốc của thông điệp cũng như tính toàn vẹn của chính thông điệp. Một khác biệt quan trọng là MAC không dựa vào mã hóa trong khi chữ ký số yêu cầu một cơ sở hạ tầng khóa công khai. Cả hai kỹ thuật đều được sử dụng rộng rãi trong thực tiễn, như chúng ta đã thấy ở các Phần 8.5 đến 8.8. Hơn nữa, chữ ký số được sử dụng để tạo chứng chỉ số, điều này quan trọng để xác minh tính hợp lệ của các khóa công khai. Trong Phần 8.4, chúng ta đã xem xét xác thực đầu cuối và giới thiệu các số nonce để chống lại tấn công phát lại.

Trong các Mục 8.5 đến 8.8, chúng ta đã xem xét một số giao thức bảo mật mạng được sử dụng rộng rãi trong thực tế. Chúng ta thấy rằng mật mã khóa đối xứng là cốt lõi của PGP, SSL, IPsec và bảo mật không dây. Chúng ta thấy rằng mật mã khóa công khai rất quan trọng cho cả PGP và TLS. Chúng ta thấy rằng PGP sử dụng chữ ký số để đảm bảo tính toàn vẹn của thông điệp, trong khi TLS và IPsec sử dụng MAC. Chúng ta cũng đã khám phá bảo mật trong các mạng không dây, bao gồm mạng WiFi và mạng di động 4G/5G. Sau khi hiểu các nguyên tắc cơ bản của mật mã, và đã nghiên cứu cách các nguyên tắc này thực sự được sử dụng, bạn hiện nay có thể thiết kế các giao thức mạng an toàn của riêng mình!

Với các kỹ thuật được đề cập trong các Mục 8.2 đến 8.8, Bob và Alice có thể giao tiếp một cách an toàn. Nhưng sự bảo mật chỉ là một phần nhỏ trong bức tranh an ninh mạng. Như chúng ta đã học trong Mục 8.9, ngày càng nhiều, trọng tâm trong an ninh mạng đã chuyển sang việc bảo vệ cơ sở hạ tầng mạng trước một cuộc tấn công tiềm năng từ kẻ xấu. Trong phần sau của chương này, chúng ta do đó đã đề cập đến các hệ thống tường lửa và IDS, những hệ thống kiểm tra các gói dữ liệu vào và ra khỏi mạng của tổ chức.

**Bài Tập và Câu Hỏi**

Bài tập ôn tập Chương 8

MỤC 8.1 R1. Sự khác nhau giữa tính bảo mật của thông điệp và tính toàn vẹn của thông điệp là gì

tính toàn vẹn? Bạn có thể giữ bí mật mà không có tính toàn vẹn không? Bạn có thể có tính toàn vẹn mà không giữ bí mật không? Hãy giải thích câu trả lời của bạn. R2. Các thực thể Internet (bộ định tuyến, bộ chuyển mạch, máy chủ DNS, máy chủ Web, người dùng cuối

các hệ thống, v.v.) thường cần giao tiếp một cách bảo mật. Hãy đưa ra ba cặp ví dụ cụ thể về các thực thể Internet có thể muốn giao tiếp an toàn.

MỤC 8.2 R3. Từ góc độ dịch vụ, một sự khác biệt quan trọng giữa một

hệ thống khóa đối xứng và hệ thống khóa công khai? R4. Giả sử rằng một kẻ xâm nhập có một tin nhắn được mã hóa cũng như bản tin đã được giải mã

phiên bản của tin nhắn đó. Kẻ xâm nhập có thể thực hiện cuộc tấn công chỉ mã hóa, cuộc tấn công văn bản rõ biết trước, hay cuộc tấn công văn bản rõ chọn trước không? R5. Xem xét một mã khối 8-bit. Có bao nhiêu khối đầu vào khả thi

mã này có? Có bao nhiêu ánh xạ khả thi? Nếu chúng ta xem mỗi ánh xạ như một khóa, thì mã này có bao nhiêu khóa khả thi? R6. Giả sử N người muốn giao tiếp với mỗi người khác trong số N - 1 người khác

những người sử dụng mã hóa khóa đối xứng. Mọi liên lạc giữa bất kỳ hai người nào, i và j, đều có thể nhìn thấy được bởi tất cả những người khác trong nhóm N này, và không ai khác trong nhóm này nên có khả năng giải mã liên lạc của họ. Hệ thống cần bao nhiêu khóa tổng thể? Bây giờ giả sử rằng mã hóa khóa công khai được sử dụng. Trong trường hợp này cần bao nhiêu khóa? R7. Giả sử n = 10.000, a = 10.023, và b = 10.004. Sử dụng một định danh của modulo-

**sử dụng số học modular để tính nhẩm trong đầu (a \# b) mod n. R8. Giả sử bạn muốn mã hóa thông điệp 10101111 bằng cách mã hóa**

số thập phân tương ứng với thông điệp. Số thập phân là gì?

MỤC 8.3--8.4 R9. Hash cung cấp kiểm tra tính toàn vẹn của thông điệp tốt hơn như thế nào so với

mã kiểm tra (chẳng hạn như mã kiểm tra Internet)? R10. Bạn có thể "giải mã" một băm của một tin nhắn để lấy tin nhắn gốc không? Giải thích

câu trả lời của bạn.

R11. Xem xét một biến thể của thuật toán MAC (Hình 8.9) nơi người gửi

gửi (m, H(m) + s), trong đó H(m) + s là sự kết hợp của H(m) và s. Sự biến thể này có sai sót không? Tại sao hoặc tại sao không? R12. Một tài liệu đã ký có thể xác minh và không thể làm giả có nghĩa là gì? R13. Theo cách nào mà băm của tin nhắn được mã hóa bằng khóa công khai cung cấp tốt hơn

chữ ký số hơn là thông điệp được mã hóa khóa công khai? R14. Giả sử certifier.com tạo một chứng chỉ cho foo.com. Thông thường,

Toàn bộ chứng chỉ sẽ được mã hóa bằng khóa công khai của certifier.com. Đúng hay sai? R15. Giả sử Alice có một tin nhắn mà cô ấy sẵn sàng gửi cho bất kỳ ai yêu cầu.

Hàng nghìn người muốn nhận được thông điệp của Alice, nhưng mỗi người đều muốn chắc chắn về tính toàn vẹn của thông điệp. Trong bối cảnh này, bạn có nghĩ rằng một sơ đồ đảm bảo tính toàn vẹn dựa trên MAC hay dựa trên chữ ký số phù hợp hơn không? Tại sao? R16. Mục đích của nonce trong giao thức xác thực đầu cuối là gì? R17. Nói rằng một nonce là giá trị chỉ sử dụng một lần trong đời có ý nghĩa gì? Ý nghĩa này thuộc về ai?

cả đời? R18. Liệu chế độ bảo toàn tính toàn vẹn của tin nhắn dựa trên HMAC có dễ bị phát lại không

các cuộc tấn công? Nếu có, làm thế nào một giá trị nonce có thể được tích hợp vào sơ đồ để loại bỏ tính dễ bị tổn thương này?

MỤC 8.5--8.8 R19. Giả sử Bob nhận được một tin nhắn PGP từ Alice. Làm thế nào Bob biết

chắc chắn rằng Alice đã tạo ra tin nhắn (thay vì, ví dụ, Trudy)? PGP có sử dụng MAC cho tính toàn vẹn của tin nhắn không? R20. Trong bản ghi TLS, có một trường cho các số thứ tự TLS. Đúng hay sai? R21. Mục đích của các nonce ngẫu nhiên trong bắt tay TLS là gì? R22. Giả sử một phiên TLS sử dụng một mã hóa khối với CBC. Đúng hay sai:

Máy chủ gửi IV cho máy khách một cách rõ ràng. R23. Giả sử Bob bắt đầu một kết nối TCP với Trudy người đang giả mạo

Alice. Trong quá trình bắt tay, Trudy gửi cho Bob chứng chỉ của Alice. Bob sẽ phát hiện ra rằng anh ta không đang giao tiếp với Alice ở bước nào của thuật toán bắt tay TLS? R24. Xem xét việc gửi một luồng gói tin từ Host A đến Host B sử dụng IPsec.

Thông thường, một SA mới sẽ được thiết lập cho mỗi gói được gửi trong luồng. Đúng hay sai? R25. Giả sử rằng TCP đang được chạy qua IPsec giữa trụ sở chính và

văn phòng chi nhánh trong Hình 8.28. Nếu TCP truyền lại cùng một gói tin, thì hai gói tin tương ứng được gửi bởi R1 sẽ có cùng số thứ tự trong tiêu đề ESP. Đúng hay sai?

BÀI TẬP VÀ CÂU HỎI VỀ NHÀ 681

R26. Một IKE SA và một IPsec SA là cùng một thứ. Đúng hay sai? R27. Xem xét WEP cho 802.11. Giả sử rằng dữ liệu là 10101100 và khóa-

dòng dữ liệu là 1111000. Bản mã kết quả là gì?

MỤC 8.9

R28. Bộ lọc gói trạng thái duy trì hai cấu trúc dữ liệu. Hãy liệt kê tên chúng và nêu ngắn gọn

mô tả những gì họ làm. R29. Xem xét một bộ lọc gói truyền thống (không trạng thái). Bộ lọc gói này có thể lọc

gói dựa trên các bit cờ TCP cũng như các trường tiêu đề khác. Đúng hay sai? R30. Trong bộ lọc gói truyền thống, mỗi giao diện có thể có kiểm soát truy cập riêng của nó

danh sách. Đúng hay sai? R31. Tại sao một cổng ứng dụng phải hoạt động cùng với bộ lọc định tuyến để

hiệu quả? R32. IDS và IPS dựa trên chữ ký kiểm tra chi tiết các gói dữ liệu của TCP và UDP

các đoạn. Đúng hay sai?

**Vấn đề**

P1. Sử dụng mật mã đơn chữ cái trong Hình 8.3, mã hóa thông điệp "This is

một vấn đề dễ dàng." Giải mã thông điệp "rmij'u uamu xyj." P2. Chứng minh rằng cuộc tấn công plaintext đã biết của Trudy, trong đó cô ấy biết (bản mã-

cặp dịch văn bản, văn bản thuần túy cho bảy chữ cái, giảm số lượng các thay thế khả thi cần kiểm tra trong ví dụ ở Mục 8.2.1 khoảng 10\^9. P3. Xem xét hệ thống đa bảng chữ cái được hiển thị trong Hình 8.4. Liệu một lựa chọn-

cuộc tấn công văn bản thuần túy có thể lấy mã hóa văn bản thuần túy của thông điệp "The quick brown fox jumps over the lazy dog." có đủ để giải mã tất cả các thông điệp không? Tại sao hoặc tại sao không? P4. Xem xét mã hóa khối trong Hình 8.5. Giả sử rằng mỗi mã hóa khối

Ti đơn giản chỉ đảo ngược thứ tự của tám bit đầu vào (vì vậy, ví dụ, 11110000 sẽ trở thành 00001111). Giả sử thêm rằng bộ trộn 64-bit không thay đổi bất kỳ bit nào (vì vậy giá trị đầu ra của bit thứ m bằng với giá trị đầu vào của bit thứ m). (a) Với n = 3 và đầu vào 64-bit gốc bằng 10100000 lặp lại tám lần, giá trị đầu ra là gì? (b) Lặp lại phần (a) nhưng bây giờ thay đổi bit cuối cùng của đầu vào 64-bit gốc từ 0 thành 1. (c) Lặp lại các phần (a) và (b) nhưng bây giờ giả sử rằng bộ trộn 64-bit đảo ngược thứ tự của 64 bit. P5. Xem xét mã hóa khối trong Hình 8.5. Đối với một "khóa" nhất định, Alice và Bob sẽ

cần giữ tám bảng, mỗi bảng 8 bit nhân 8 bit. Đối với Alice (hoặc Bob) để lưu trữ tất cả tám bảng, cần bao nhiêu bit bộ nhớ? Con số này so với số bit cần thiết cho một bộ mã khối 64 bit đầy đủ như thế nào?

P6. Xem xét mật mã khối 3-bit trong Bảng 8.1. Giả sử bản rõ là

100100100\. (a) Ban đầu giả sử rằng CBC không được sử dụng. Kết quả của văn bản mã hóa là gì? (b) Giả sử Trudy nghe lén văn bản mã hóa. Giả sử cô ấy biết rằng một bộ mã hóa khối 3-bit mà không sử dụng CBC đang được áp dụng (nhưng không biết mã hóa cụ thể), cô ấy có thể suy ra gì? (c) Bây giờ giả sử rằng CBC được sử dụng với IV = 111. Kết quả của văn bản mã hóa là gì? P7. (a) Sử dụng RSA, chọn p = 3 và q = 11, và mã hóa từ "dog" bằng cách

mã hóa từng chữ cái riêng biệt. Áp dụng thuật toán giải mã cho phiên bản đã mã hóa để khôi phục lại thông điệp bản rõ ban đầu. (b) Lặp lại phần (a) nhưng bây giờ mã hóa "dog" như một thông điệp m. P8. Xem xét RSA với p = 5 và q = 11.

a\. n và z là gì? b. Giả sử e bằng 3. Tại sao đây là lựa chọn chấp nhận được cho e? c. Tìm d sao cho de = 1 (mod z) và d ≤ 160. d. Mã hóa thông điệp m = 8 sử dụng khóa (n, e). Gọi c là giá trị tương ứng

văn bản mã hóa. Hiển thị tất cả các bước. Gợi ý: Để đơn giản hóa các phép tính, hãy sử dụng thực tế:

**\[(a mod n) \# (b mod n)\] mod n = (a \# b) mod n**

P9. Trong vấn đề này, chúng ta sẽ khám phá mã hóa khóa công khai Diffie-Hellman (DH)

thuật toán, cho phép hai thực thể đồng ý trên một khóa chung. Thuật toán DH sử dụng một số nguyên tố lớn p và một số lớn khác g nhỏ hơn p. Cả p và g đều được công khai (để kẻ tấn công có thể biết chúng). Trong DH, Alice và Bob mỗi người độc lập chọn khóa bí mật riêng, lần lượt là SA và SB. Sau đó, Alice tính khóa công khai của mình, TA, bằng cách lấy g mũ SA rồi lấy mod p. Tương tự, Bob tính khóa công khai của mình TB bằng cách lấy g mũ SB rồi lấy mod p. Alice và Bob sau đó trao đổi khóa công khai của họ qua Internet. Alice tính khóa bí mật chung S bằng cách lấy TB mũ SA rồi lấy mod p. Tương tự, Bob tính khóa chung S′ bằng cách lấy TA mũ SB rồi lấy mod p. a. Chứng minh rằng, nói chung, Alice và Bob nhận được cùng một khóa đối xứng, rằng

là, chứng minh S = S′. b. Với p = 11 và g = 2, giả sử Alice và Bob chọn khóa riêng SA = 5

và SB = 12, tương ứng. Tính khóa công khai của Alice và Bob, TA và TB. Hiển thị tất cả các bước làm. c. Tiếp tục phần (b), bây giờ tính S như khóa đối xứng chia sẻ.

Hiển thị tất cả các bước. d. Cung cấp một sơ đồ thời gian cho thấy cách Diffie-Hellman có thể bị tấn công

bởi một kẻ trung gian. Sơ đồ thời gian nên có ba đường thẳng đứng, một cho Alice, một cho Bob, và một cho kẻ tấn công Trudy.

BÀI TOÁN 683

P10. Giả sử Alice muốn giao tiếp với Bob sử dụng mã hóa khóa đối xứng

sử dụng mật mã phiên với khóa phiên KS. Trong Mục 8.2, chúng ta đã tìm hiểu cách mật mã khóa công khai có thể được sử dụng để phân phối khóa phiên từ Alice đến Bob. Trong bài toán này, chúng ta khám phá cách phân phối khóa phiên---mà không dùng mật mã khóa công khai---bằng cách sử dụng trung tâm phân phối khóa (KDC). KDC là một máy chủ chia sẻ một khóa đối xứng bí mật duy nhất với mỗi người dùng đã đăng ký. Đối với Alice và Bob, ký hiệu các khóa này là KA@KDC và KB@KDC. Thiết kế một phương án sử dụng KDC để phân phối KS cho Alice và Bob. Phương án của bạn nên sử dụng ba thông điệp để phân phối khóa phiên: một thông điệp từ Alice gửi đến KDC; một thông điệp từ KDC gửi đến Alice; và cuối cùng một thông điệp từ Alice gửi đến Bob. Thông điệp đầu tiên là KA@KDC (A, B). Sử dụng ký hiệu KA@KDC, KB@KDC, S, A, và B để trả lời các câu hỏi sau. a. Thông điệp thứ hai là gì? b. Thông điệp thứ ba là gì? P11. Tính toán một thông điệp thứ ba, khác với hai thông điệp trong Hình 8.8, mà

có cùng một giá trị kiểm tra với các tin nhắn trong Hình 8.8. P12. Giả sử Alice và Bob chia sẻ hai khóa bí mật: một khóa xác thực S1 và một

khóa mã hóa đối xứng S2. Bổ sung Hình 8.9 sao cho cả tính toàn vẹn và tính bảo mật đều được cung cấp. P13. Trong giao thức phân phối tệp BitTorrent P2P (xem Chương 2), hạt giống

chia tệp thành các khối, và các máy ngang hàng phân phối lại các khối cho nhau. Nếu không có bất kỳ biện pháp bảo vệ nào, một kẻ tấn công có thể dễ dàng gây một mớ hỗn loạn trong một torrent bằng cách giả danh một máy ngang hàng tốt và gửi các khối giả đến một tập hợp nhỏ các máy ngang hàng trong torrent. Những máy ngang hàng không nghi ngờ này sau đó phân phối lại các khối giả cho các máy ngang hàng khác, mà các máy này lại tiếp tục phân phối các khối giả cho nhiều máy ngang hàng hơn nữa. Do đó, việc BitTorrent có một cơ chế cho phép một máy ngang hàng xác minh tính toàn vẹn của một khối là rất quan trọng, để nó không phân phối lại các khối giả. Giả sử rằng khi một máy ngang hàng tham gia một torrent, nó ban đầu nhận được một tệp .torrent từ một nguồn hoàn toàn đáng tin cậy. Mô tả một phương án đơn giản cho phép các máy ngang hàng xác minh tính toàn vẹn của các khối. P14. Giao thức định tuyến OSPF sử dụng MAC thay vì chữ ký số để cung cấp

tính toàn vẹn của thông điệp. Tại sao bạn nghĩ MAC được chọn thay vì chữ ký số? P15. Hãy xem xét giao thức xác thực của chúng ta trong Hình 8.18, trong đó Alice xác thực-

ticates bản thân với Bob, điều mà chúng ta đã thấy hoạt động tốt (tức là, chúng ta không tìm thấy sai sót nào trong đó). Giờ hãy giả sử rằng trong khi Alice đang xác thực bản thân với Bob, Bob cũng phải xác thực bản thân với Alice. Hãy đưa ra một kịch bản mà Trudy, giả vờ là Alice, có thể xác thực bản thân với Bob với tư cách là Alice. (Gợi ý: Xem xét rằng trình tự các thao tác của giao thức, một khi Trudy khởi tạo và một khi Bob khởi tạo, có thể được xen kẽ tùy ý. Chú ý đặc biệt đến thực tế rằng cả Bob và Alice sẽ sử dụng một nonce, và nếu không cẩn thận, cùng một nonce có thể bị sử dụng một cách ác ý.)

BÀI TOÁN 685

P16. Một câu hỏi tự nhiên là liệu chúng ta có thể sử dụng một giá trị nonce và mật mã khóa công khai để

giải quyết vấn đề xác thực đầu cuối trong Mục 8.4. Xem xét giao thức tự nhiên sau: (1) Alice gửi thông điệp "Tôi là Alice" đến Bob. (2) Bob chọn một số ngẫu nhiên (nonce) R và gửi nó cho Alice. (3) Alice sử dụng khóa riêng của mình để mã hóa số ngẫu nhiên và gửi giá trị kết quả đến Bob. (4) Bob áp dụng khóa công khai của Alice vào thông điệp nhận được. Như vậy, Bob tính R và xác thực Alice. a. Vẽ sơ đồ của giao thức này, sử dụng ký hiệu cho khóa công khai và khóa riêng.

được sử dụng trong sách giáo khoa. b. Giả sử rằng không sử dụng chứng chỉ. Hãy mô tả cách Trudy có thể trở thành

một "người phụ nữ-ở-giữa" bằng cách chặn các tin nhắn của Alice và sau đó giả vờ là Alice đối với Bob. P17. Hình 8.21 cho thấy các thao tác mà Alice phải thực hiện với PGP để pro-

đảm bảo tính bảo mật, xác thực và toàn vẹn. Vẽ sơ đồ các thao tác tương ứng mà Bob phải thực hiện trên gói tin nhận được từ Alice. P18. Giả sử Alice muốn gửi một e-mail cho Bob. Bob có một cặp khóa công khai và riêng tư

cặp (K B

+, K B

**-), và Alice có chứng chỉ của Bob. Nhưng Alice không có cặp khóa công khai, khóa riêng. Alice và Bob (và toàn bộ thế giới) sử dụng cùng một hàm băm H(#). a. Trong tình huống này, có thể thiết kế một phương pháp để Bob có thể xác minh không**

rằng Alice đã tạo ra tin nhắn? Nếu có, hãy chỉ ra cách bằng sơ đồ khối cho Alice và Bob. b. Có thể thiết kế một phương án cung cấp tính bảo mật khi gửi không

tin nhắn từ Alice đến Bob? Nếu có, hãy trình bày cách thực hiện bằng sơ đồ khối cho Alice và Bob. P19. Xem xét đầu ra Wireshark dưới đây cho một phần của phiên SSL.

a\. Gói Wireshark 112 được gửi bởi client hay server? b. Địa chỉ và số cổng IP của server là gì? c. Giả sử không có mất mát và không có gửi lại, số thứ tự sẽ là gì-

số của phần TCP tiếp theo được gửi bởi khách hàng? d. Gói Wireshark số 112 chứa bao nhiêu bản ghi SSL? e. Gói 112 có chứa Master Secret hay Encrypted Master Secret hay không?

cả hai cũng không? f. Giả sử rằng trường loại bắt tay là 1 byte và mỗi trường độ dài là

3 byte, giá trị của byte đầu tiên và byte cuối cùng của Master Secret (hoặc Encrypted Master Secret) là gì? g. Tin nhắn bắt tay được mã hóa của client tính đến bao nhiêu

SSL bản ghi? h. Thông điệp bắt tay được mã hóa của máy chủ tính đến bao nhiêu

Các bản ghi SSL?

P20. Trong Mục 8.6.1, đã chỉ ra rằng nếu không có số thứ tự, Trudy (một người phụ nữ-

ở giữa) có thể gây ra hoạ trong một phiên TLS bằng cách hoán đổi các đoạn TCP. Trudy có thể làm điều gì tương tự bằng cách xóa một đoạn TCP không? Cô ấy cần làm gì để thành công trong cuộc tấn công xóa? Nó sẽ có tác động gì?

(Ảnh chụp màn hình Wireshark được tái bản với sự cho phép của Quỹ Wireshark.)

P21. Giả sử Alice và Bob đang giao tiếp qua một phiên TLS. Giả sử một

kẻ tấn công, người không có bất kỳ khóa chia sẻ nào, chèn một đoạn TCP giả vào luồng gói với kiểm tra chẵn lẻ TCP và số thứ tự chính xác (và địa chỉ IP và số cổng chính xác). Liệu TLS ở phía nhận có chấp nhận gói giả và chuyển tải trọng đến ứng dụng nhận không? Tại sao hoặc tại sao không? P22. Các câu hỏi đúng/sai sau liên quan đến Hình 8.28.

a\. Khi một máy chủ trong 172.16.1/24 gửi một gói tin đến máy chủ của Amazon.com,

Bộ định tuyến R1 sẽ mã hóa gói dữ liệu bằng IPsec.

![](media/image3.png){width="5.5in" height="3.860400262467192in"}

CÁC VẤN ĐỀ 687

b\. Khi một máy chủ trong 172.16.1/24 gửi một gói dữ liệu đến một máy chủ trong 172.16.2/24, thì

bộ định tuyến R1 sẽ thay đổi địa chỉ nguồn và đích của datagram IP. c. Giả sử một máy chủ trong 172.16.1/24 khởi tạo một kết nối TCP tới một máy chủ Web

trong 172.16.2/24. Như một phần của kết nối này, tất cả các gói dữ liệu gửi bởi R1 sẽ có số giao thức 50 trong trường header IPv4 ở bên trái nhất. d. Xem xét việc gửi một đoạn TCP từ một máy chủ trong 172.16.1/24 đến một máy chủ trong

172.16.2/24. Giả sử xác nhận cho phân đoạn này bị mất, do đó TCP gửi lại phân đoạn. Vì IPsec sử dụng số thứ tự, R1 sẽ không gửi lại phân đoạn TCP. P23. Xem xét ví dụ trong Hình 8.28. Giả sử Trudy là một phụ nữ trong-

ở giữa, người có thể chèn các datagram vào luồng các datagram đi từ R1 đến R2. Như một phần của tấn công phát lại, Trudy gửi một bản sao trùng lặp của một trong các datagram được gửi từ R1 đến R2. Liệu R2 có giải mã datagram trùng lặp và chuyển tiếp nó vào mạng chi nhánh không? Nếu không, hãy mô tả chi tiết cách R2 phát hiện datagram trùng lặp. P24. Cung cấp bảng lọc và bảng kết nối cho một tường lửa trạng thái mà

hạn chế càng nhiều càng tốt nhưng thực hiện các điều sau: a. Cho phép tất cả người dùng nội bộ thiết lập các phiên Telnet với các máy chủ bên ngoài. b. Cho phép người dùng bên ngoài truy cập trang Web của công ty tại 222.22.0.12. c. Ngoài ra, chặn tất cả lưu lượng vào và ra. Mạng nội bộ là 222.22/16. Trong giải pháp của bạn, giả sử rằng kết nối-

Bảng phiên hiện đang lưu trữ ba kết nối, tất cả đều từ bên trong ra bên ngoài. Bạn sẽ cần tạo ra các địa chỉ và số cổng IP thích hợp. P25. Giả sử Alice muốn truy cập trang Web activist.com bằng cách sử dụng một phương pháp giống TOR

dịch vụ. Dịch vụ này sử dụng hai máy chủ proxy không thông đồng, Proxy1 và Proxy2. Alice trước tiên lấy chứng chỉ (mỗi chứng chỉ chứa một khóa công khai) cho Proxy1 và Proxy2 từ một máy chủ trung tâm nào đó. Ký hiệu K1

+( ), K2

+( ), K1

-( ), và K2

-( ) cho việc mã hóa/giải mã với khóa công khai và khóa riêng RSA. a. Sử dụng sơ đồ thời gian, cung cấp một giao thức (đơn giản nhất có thể) mà

cho phép Alice thiết lập một khóa phiên chia sẻ S1 với Proxy1. Ký hiệu S1(m) để mã hóa/giải mã dữ liệu m với khóa chia sẻ S1. b. Sử dụng sơ đồ thời gian, cung cấp một giao thức (càng đơn giản càng tốt) mà

cho phép Alice thiết lập một khóa phiên chia sẻ S2 với Proxy2 mà không tiết lộ địa chỉ IP của cô ấy cho Proxy2. c. Giả sử bây giờ các khóa chia sẻ S1 và S2 đã được thiết lập. Sử dụng một

sơ đồ thời gian, cung cấp một giao thức (đơn giản nhất có thể và không sử dụng mật mã khóa công khai) cho phép Alice yêu cầu một trang html từ activist.com mà không tiết lộ địa chỉ IP của cô ấy cho Proxy2 và không tiết lộ cho Proxy1 trang web mà cô ấy đang truy cập. Sơ đồ của bạn nên kết thúc với một yêu cầu HTTP đến activist.com.

**Wireshark Phòng thí nghiệm: SSL**

Trong phòng thí nghiệm này (có sẵn từ trang web của sách), chúng tôi nghiên cứu giao thức Lớp Bảo mật Sockets (SSL). Hãy nhớ lại từ Mục 8.6 rằng SSL được sử dụng để bảo mật một kết nối TCP, và rằng nó được sử dụng rộng rãi trong thực tế cho các giao dịch Internet an toàn. Trong phòng thí nghiệm này, chúng tôi sẽ tập trung vào các bản ghi SSL được gửi qua kết nối TCP. Chúng tôi sẽ cố gắng phân định và phân loại từng bản ghi, với mục tiêu hiểu lý do và cách thức cho mỗi bản ghi. Chúng tôi nghiên cứu các loại bản ghi SSL khác nhau cũng như các trường trong các thông điệp SSL. Chúng tôi thực hiện điều này bằng cách phân tích một bản theo dõi các bản ghi SSL được gửi giữa máy chủ của bạn và một máy chủ thương mại điện tử.

**Phòng thí nghiệm IPsec**

Trong phòng thí nghiệm này (có sẵn trên trang Web của sách), chúng ta sẽ khám phá cách tạo các IPsec SA giữa các máy Linux. Bạn có thể thực hiện phần đầu của phòng thí nghiệm với hai máy Linux thông thường, mỗi máy có một bộ điều hợp Ethernet. Nhưng đối với phần thứ hai của phòng thí nghiệm, bạn sẽ cần bốn máy Linux, trong đó hai máy có hai bộ điều hợp Ethernet. Trong nửa sau của phòng thí nghiệm, bạn sẽ tạo các IPsec SA sử dụng giao thức ESP ở chế độ tunnel. Bạn sẽ thực hiện điều này bằng cách đầu tiên tạo các SA một cách thủ công, sau đó nhờ IKE tạo các SA.

Điều gì đã khiến bạn chuyên về lĩnh vực bảo mật mạng?

Điều này nghe có vẻ lạ, nhưng câu trả lời rất đơn giản: Nó thật sự thú vị. Nền tảng của tôi là lập trình hệ thống và quản trị hệ thống, điều này dẫn đến bảo mật một cách khá tự nhiên. Và tôi luôn quan tâm đến truyền thông, bắt đầu từ những công việc lập trình hệ thống bán thời gian khi tôi còn học đại học.

Công việc của tôi về an ninh vẫn tiếp tục được thúc đẩy bởi hai điều---một là mong muốn giữ cho máy tính hữu ích, điều này có nghĩa là chức năng của chúng không thể bị những kẻ tấn công làm hỏng, và hai là mong muốn bảo vệ quyền riêng tư.

Tầm nhìn của bạn về Usenet là gì vào thời điểm bạn phát triển nó? Còn bây giờ thì sao?

Chúng tôi ban đầu xem đó như một cách để nói về khoa học máy tính và lập trình máy tính trên khắp cả nước, với nhiều sử dụng địa phương cho các vấn đề hành chính, quảng cáo bán hàng, và những thứ tương tự. Thực tế, dự đoán ban đầu của tôi là mỗi ngày một đến hai tin nhắn, từ 50 đến 100 trang web là nhiều nhất---tính đến bất cứ lúc nào. Tuy nhiên, sự phát triển thực sự là ở các chủ đề liên quan đến con người, bao gồm---nhưng không giới hạn---tương tác giữa con người với máy tính. Các nhóm tin tức yêu thích của tôi, qua nhiều năm, đã là những thứ như rec.woodworking, cũng như sci.crypt.

Ở một mức độ nào đó, tin tức mạng đã bị Web thay thế. Nếu hôm nay tôi bắt đầu thiết kế nó, nó sẽ trông rất khác. Nhưng nó vẫn nổi trội như một cách để tiếp cận một khán giả rất rộng quan tâm đến chủ đề này, mà không cần phải phụ thuộc vào các trang Web cụ thể.

Có ai đã truyền cảm hứng cho bạn trong công việc không? Bằng những cách nào?

Giáo sư Fred Brooks---người sáng lập và là chủ tịch đầu tiên của khoa khoa học máy tính tại Đại học North Carolina ở Chapel Hill, người quản lý đội ngũ đã phát triển IBM S/360 và OS/360, và là tác giả của cuốn The Mythical Man-Month---đã là một nhân vật phi thường

MỘT CUỘC PHỎNG VẤN VỚI...

**Steven M. Bellovin**

Được sự cho phép của Steven Bellovin

Steven M. Bellovin gia nhập giảng viên tại Đại học Columbia sau nhiều năm làm việc tại Phòng Thí nghiệm Nghiên cứu Dịch vụ Mạng tại AT&T Labs Research ở Florham Park, New Jersey. Ông tập trung vào mạng, bảo mật, và lý do tại sao hai lĩnh vực này không tương thích. Năm 1995, ông được trao Giải thưởng Thành tựu Trọn đời Usenix cho công trình của mình trong việc tạo ra Usenet, mạng trao đổi nhóm tin đầu tiên liên kết hai hoặc nhiều máy tính và cho phép người dùng chia sẻ thông tin và tham gia thảo luận. Steve cũng là một thành viên được bầu của Viện Kỹ thuật Quốc gia. Ông nhận bằng Cử nhân từ Đại học Columbia và bằng Tiến sĩ từ Đại học North Carolina tại Chapel Hill.

![](media/image4.png){width="5.5in" height="7.071428258967629in"}

ảnh hưởng đến sự nghiệp của tôi. Hơn bất cứ điều gì khác, ông đã dạy quan điểm và sự đánh đổi---cách nhìn nhận các vấn đề trong bối cảnh của thế giới thực (và mức độ lộn xộn của thế giới thực hơn nhiều so với những gì một nhà lý thuyết mong muốn), và cách cân bằng các lợi ích cạnh tranh khi thiết kế một giải pháp. Hầu hết công việc máy tính là kỹ thuật---nghệ thuật đưa ra những sự đánh đổi đúng đắn để thỏa mãn nhiều mục tiêu mâu thuẫn.

Tầm nhìn của bạn về tương lai của mạng và an ninh là gì?

Cho đến nay, phần lớn an ninh mà chúng ta có đến từ việc cô lập. Ví dụ, một tường lửa hoạt động bằng cách ngắt quyền truy cập vào một số máy và dịch vụ nhất định. Nhưng chúng ta đang ở trong thời đại kết nối ngày càng tăng---việc cô lập mọi thứ đã trở nên khó khăn hơn. Tệ hơn nữa, các hệ thống sản xuất của chúng ta yêu cầu nhiều thành phần tách biệt hơn, được kết nối với nhau qua mạng lưới. Bảo vệ tất cả điều đó là một trong những thách thức lớn nhất của chúng ta.

Bạn sẽ nói những tiến bộ lớn nhất trong an ninh là gì? Chúng ta còn phải tiến xa bao nhiêu nữa?

Ít nhất về mặt khoa học, chúng ta biết cách thực hiện mật mã học. Điều đó đã giúp ích rất nhiều. Nhưng hầu hết các vấn đề về bảo mật đều do mã lỗi, và đó là một vấn đề khó hơn nhiều. Thực ra, đó là vấn đề chưa được giải quyết lâu đời nhất trong khoa học máy tính, và tôi nghĩ nó sẽ vẫn như vậy. Thách thức là tìm cách bảo mật các hệ thống khi chúng ta phải xây dựng chúng từ các thành phần không an toàn. Chúng ta đã có thể làm điều đó để đảm bảo độ tin cậy khi gặp sự cố phần cứng; liệu chúng ta có thể làm tương tự cho bảo mật không?

Bạn có lời khuyên nào cho sinh viên về Internet và bảo mật mạng không?

Học các cơ chế là phần dễ dàng. Học cách "suy nghĩ một cách hoang tưởng" thì khó hơn. Bạn phải nhớ rằng các phân phối xác suất không áp dụng---kẻ tấn công có thể và sẽ tìm ra những điều kiện không thể xảy ra. Và các chi tiết rất quan trọng---rất nhiều.

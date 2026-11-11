**Chương 5: Tầng Mạng: Mặt Phẳng Điều Khiển (Control Plane)**

Trong chương này, chúng ta sẽ hoàn thành hành trình của mình qua lớp mạng bằng cách đề cập đến thành phần mặt phẳng điều khiển của lớp mạng---logic toàn mạng kiểm soát không chỉ cách một gói dữ liệu được định tuyến dọc theo đường dẫn từ đầu đến cuối từ máy chủ nguồn đến máy chủ đích mà còn cả cách cấu hình và quản lý các thành phần và dịch vụ của lớp mạng. Trong Phần 5.2, chúng tôi sẽ đề cập đến các thuật toán định tuyến truyền thống để tính toán các đường dẫn có chi phí thấp nhất trong biểu đồ; các thuật toán này là cơ sở cho hai giao thức định tuyến Internet được triển khai rộng rãi: OSPF và BGP, mà chúng tôi sẽ lần lượt đề cập đến trong Phần 5.3 và 5.4. Như chúng ta sẽ thấy, OSPF là một giao thức định tuyến hoạt động trong mạng của một ISP. BGP là giao thức định tuyến dùng để kết nối tất cả các mạng trên Internet; BGP do đó thường được coi là "chất keo" gắn kết Internet lại với nhau. Theo truyền thống, các giao thức định tuyến mặt phẳng điều khiển đã được triển khai cùng với các chức năng chuyển tiếp mặt phẳng dữ liệu một cách nguyên khối trong một bộ định tuyến. Như chúng ta đã tìm hiểu trong phần giới thiệu của Chương 4, mạng được xác định bằng phần mềm (SDN) tạo ra sự tách biệt rõ ràng giữa dữ liệu và mặt phẳng điều khiển, triển khai các chức năng của mặt phẳng điều khiển trong một dịch vụ "bộ điều khiển" riêng biệt và tách biệt khỏi các thành phần chuyển tiếp của bộ định tuyến mà nó điều khiển. Chúng tôi sẽ đề cập đến bộ điều khiển SDN trong Phần 5.5.

Trong Phần 5.6 và 5.7, chúng tôi sẽ đề cập đến một số vấn đề cơ bản về quản lý mạng IP: ICMP (Giao thức thông báo điều khiển Internet) và SNMP (Giao thức quản lý mạng đơn giản).

**Network Layer: Mặt phẳng điều khiển**

**CHƯƠNG**

![](media/image1.png){width="5.5in" height="6.930965660542432in"}

![](media/image2.png){width="5.5in" height="0.9567311898512686in"}

**5.1 Giới thiệu**

Hãy nhanh chóng thiết lập bối cảnh cho nghiên cứu của chúng ta về mặt phẳng điều khiển mạng bằng cách xem lại Hình 4.2 và 4.3. Ở đó, chúng tôi thấy rằng bảng chuyển tiếp (trong trường hợp chuyển tiếp dựa trên đích) và bảng luồng (trong trường hợp chuyển tiếp tổng quát) là các thành phần chính liên kết các mặt phẳng điều khiển và dữ liệu của lớp mạng. Chúng tôi đã biết rằng các bảng này chỉ định hành vi chuyển tiếp mặt phẳng dữ liệu cục bộ của bộ định tuyến. Chúng tôi thấy rằng trong trường hợp chuyển tiếp tổng quát, các hành động được thực hiện có thể không chỉ bao gồm chuyển tiếp gói đến cổng đầu ra của bộ định tuyến mà còn loại bỏ gói, sao chép gói và/hoặc viết lại các trường tiêu đề gói lớp 2, 3 hoặc 4.

Trong chương này, chúng ta sẽ nghiên cứu cách tính toán, duy trì và cài đặt các bảng chuyển tiếp và bảng luồng đó. Trong phần giới thiệu về lớp mạng ở Phần 4.1, chúng ta đã biết rằng có hai cách tiếp cận khả thi để thực hiện điều đó.

• Điều khiển trên mỗi bộ định tuyến. Hình 5.1 minh họa trường hợp thuật toán định tuyến chạy trong mỗi bộ định tuyến; cả chức năng chuyển tiếp và định tuyến đều được chứa

Mặt phẳng điều khiển

Mặt phẳng dữ liệu

Thuật toán định tuyến

Chuyển tiếp

Bàn

*Hình 5.1 ♦ Điều khiển trên mỗi bộ định tuyến: Các thành phần thuật toán định tuyến riêng lẻ*

tương tác trong mặt phẳng điều khiển

trong mỗi bộ định tuyến. Mỗi bộ định tuyến có một thành phần định tuyến giao tiếp với các thành phần định tuyến trong các bộ định tuyến khác để tính toán các giá trị cho bảng chuyển tiếp của nó. Phương pháp điều khiển trên mỗi bộ định tuyến này đã được sử dụng trên Internet trong nhiều thập kỷ. Các giao thức OSPF và BGP mà chúng ta sẽ nghiên cứu trong Phần 5.3 và 5.4 dựa trên phương pháp kiểm soát trên mỗi bộ định tuyến này. • Điều khiển tập trung một cách logic. Hình 5.2 minh họa trường hợp trong đó bộ điều khiển tập trung tính toán và phân phối các bảng chuyển tiếp được sử dụng bởi mỗi bộ định tuyến. Như chúng ta đã thấy trong Phần 4.4 và 4.5, tính trừu tượng kết hợp hành động kết hợp tổng quát cho phép bộ định tuyến thực hiện chuyển tiếp IP truyền thống cũng như một tập hợp phong phú các chức năng khác (chia sẻ tải, tường lửa và NAT) đã được triển khai trước đó trong các hộp trung gian riêng biệt.

Bộ điều khiển định tuyến tập trung logic

Mặt phẳng điều khiển

Mặt phẳng dữ liệu

Đại lý kiểm soát (CA)

CA

CA

CA

CA

*Hình 5.2 ♦ Điều khiển tập trung logic: Một cách điều khiển riêng biệt, điển hình là điều khiển từ xa,*

bộ điều khiển tương tác với các tác nhân điều khiển cục bộ (CA)

Bộ điều khiển tương tác với tác nhân điều khiển (CA) trong mỗi bộ định tuyến thông qua giao thức được xác định rõ ràng để định cấu hình và quản lý bảng quy trình của bộ định tuyến đó. Thông thường, CA có chức năng tối thiểu; công việc của nó là giao tiếp với bộ điều khiển và thực hiện theo lệnh của bộ điều khiển. Không giống như các thuật toán định tuyến trong Hình 5.1, các CA không tương tác trực tiếp với nhau cũng như không tham gia tích cực vào việc tính toán bảng chuyển tiếp. Đây là điểm khác biệt chính giữa điều khiển trên mỗi bộ định tuyến và điều khiển tập trung về mặt logic.

Bằng cách kiểm soát "tập trung một cách hợp lý" \[Levin 2012\], chúng tôi muốn nói rằng dịch vụ kiểm soát định tuyến được truy cập như thể nó là một điểm dịch vụ trung tâm duy nhất, mặc dù dịch vụ này có thể được triển khai qua nhiều máy chủ vì lý do khả năng chịu lỗi và khả năng mở rộng hiệu suất. Như chúng ta sẽ thấy trong Phần 5.5, SDN áp dụng khái niệm này về bộ điều khiển tập trung một cách hợp lý---một cách tiếp cận đang được sử dụng nhiều hơn trong triển khai sản xuất. Google sử dụng SDN để điều khiển các bộ định tuyến trong mạng diện rộng toàn cầu B4 nội bộ kết nối các trung tâm dữ liệu của nó \[Jain 2013\]. SWAN \[Hong 2013\], từ Microsoft Research, sử dụng bộ điều khiển tập trung hợp lý để quản lý việc định tuyến và chuyển tiếp giữa mạng diện rộng và mạng trung tâm dữ liệu. Các hoạt động triển khai chính của ISP, bao gồm ActiveCore của COMCAST và Access 4.0 của Deutsche Telecom đang tích cực tích hợp SDN vào mạng của họ. Và như chúng ta sẽ thấy trong Chương 8, điều khiển SDN cũng là trọng tâm của mạng di động 4G/5G. \[AT&T 2019\] lưu ý, \"... SDN, không phải là tầm nhìn, mục tiêu hay lời hứa. Đó là hiện thực. Vào cuối năm tới, 75% chức năng mạng của chúng tôi sẽ được ảo hóa hoàn toàn và được kiểm soát bằng phần mềm.\" China Telecom và China Unicom đang sử dụng SDN cả trong trung tâm dữ liệu và giữa các trung tâm dữ liệu \[Li 2015\].

**5.2 Thuật toán định tuyến**

Trong phần này, chúng ta sẽ nghiên cứu các thuật toán định tuyến, với mục tiêu là xác định các đường dẫn tốt (tương đương các tuyến đường), từ người gửi đến người nhận, thông qua mạng các bộ định tuyến. Thông thường, con đường "tốt" là con đường có chi phí thấp nhất. Tuy nhiên, chúng ta sẽ thấy rằng trên thực tế, những mối quan tâm trong thế giới thực như các vấn đề về chính sách (ví dụ: một quy tắc như "bộ định tuyến x, thuộc tổ chức Y, không nên chuyển tiếp bất kỳ gói nào có nguồn gốc từ mạng thuộc sở hữu của tổ chức Z") cũng có tác dụng. Chúng tôi lưu ý rằng cho dù mặt phẳng điều khiển mạng áp dụng phương pháp điều khiển trên mỗi bộ định tuyến hay phương pháp tập trung về mặt logic thì luôn phải có một chuỗi các bộ định tuyến được xác định rõ ràng mà gói sẽ đi qua khi di chuyển từ máy gửi đến máy chủ nhận. Do đó, các thuật toán định tuyến tính toán các đường dẫn này có tầm quan trọng cơ bản và là một ứng cử viên khác cho danh sách 10 khái niệm mạng cơ bản quan trọng hàng đầu của chúng tôi.

Một biểu đồ được sử dụng để xây dựng các vấn đề định tuyến. Hãy nhớ lại rằng đồ thị G = (N, E) là tập hợp N các nút và tập hợp E các cạnh, trong đó mỗi cạnh là một cặp nút từ N. Trong bối cảnh định tuyến lớp mạng, các nút trong biểu đồ biểu thị

bộ định tuyến---các điểm tại đó các quyết định chuyển tiếp gói được thực hiện---và các cạnh kết nối các nút này thể hiện các liên kết vật lý giữa các bộ định tuyến này. Sự trừu tượng hóa đồ thị của mạng máy tính như vậy được thể hiện trong Hình 5.3. Khi nghiên cứu giao thức định tuyến liên miền BGP, chúng ta sẽ thấy rằng các nút đại diện cho các mạng và cạnh kết nối hai nút đó biểu thị kết nối hướng (được gọi là ngang hàng) giữa hai mạng. Để xem một số biểu đồ thể hiện bản đồ mạng thực, hãy xem \[CAIDA 2020\]; để thảo luận về các mô hình dựa trên đồ thị khác nhau mô hình hóa Internet tốt như thế nào, xem \[Zegura 1997, Faloutsos 1999, Li 2004\].

Như được minh họa trong Hình 5.3, một cạnh cũng có một giá trị đại diện cho giá của nó. Thông thường, chi phí của một cạnh có thể phản ánh độ dài vật lý của liên kết tương ứng (ví dụ: liên kết xuyên đại dương có thể có chi phí cao hơn liên kết trên mặt đất đường ngắn), tốc độ liên kết hoặc chi phí bằng tiền liên quan đến liên kết. Vì mục đích của chúng tôi, chúng tôi sẽ chỉ coi chi phí cận biên là hiển nhiên và không cần lo lắng về cách xác định chúng. Đối với bất kỳ cạnh (x, y) nào trong E, chúng ta biểu thị c(x, y) là chi phí của cạnh giữa các nút x và y. Nếu cặp (x, y) không thuộc E thì ta đặt c(x, y) = ∞. Ngoài ra, chúng ta sẽ chỉ xem xét các đồ thị vô hướng (tức là các đồ thị có các cạnh không có hướng) trong cuộc thảo luận của chúng ta ở đây, do đó cạnh (x, y) giống với cạnh (y, x) và c(x, y) = c(y, x); tuy nhiên, các thuật toán mà chúng tôi nghiên cứu có thể dễ dàng mở rộng cho trường hợp liên kết được định hướng với chi phí khác nhau theo mỗi hướng. Ngoài ra, nút y được gọi là nút lân cận của nút x nếu (x, y) thuộc E.

Cho rằng chi phí được gán cho các cạnh khác nhau trong biểu đồ trừu tượng, mục tiêu tự nhiên của thuật toán định tuyến là xác định các đường dẫn ít tốn kém nhất giữa nguồn và đích. Để làm cho vấn đề này chính xác hơn, hãy nhớ lại rằng một đường đi trong đồ thị G = (N, E) là một chuỗi các nút (x1, x2, g, xp) sao cho mỗi cặp (x1, x2), (x2, x3), g, (xp-1, xp) là các cạnh trong E. Chi phí của một đường đi (x1, x2, g, xp) chỉ đơn giản là tổng của tất cả chi phí cạnh dọc theo đường đi, nghĩa là,

x y

v

bạn z

w

*Hình 5.3 ♦ Mô hình đồ thị trừu tượng của mạng máy tính*

c(x1, x2) + c(x2, x3) + g+ c(xp-1, xp). Với hai nút x và y bất kỳ, thường có nhiều đường dẫn giữa hai nút, với mỗi đường dẫn có một chi phí. Một hoặc nhiều đường đi này là đường đi có chi phí thấp nhất. Do đó, vấn đề chi phí thấp nhất rất rõ ràng: Tìm đường đi giữa nguồn và đích có chi phí thấp nhất. Ví dụ, trong Hình 5.3, đường dẫn có chi phí thấp nhất giữa nút nguồn u và nút đích w là (u, x, y, w) với chi phí đường dẫn là 3. Lưu ý rằng nếu tất cả các cạnh trong biểu đồ có cùng chi phí thì đường dẫn có chi phí thấp nhất cũng là đường dẫn ngắn nhất (nghĩa là đường dẫn có số lượng liên kết nhỏ nhất giữa nguồn và đích).

Như một bài tập đơn giản, hãy thử tìm đường đi có chi phí thấp nhất từ ​​nút u đến z trong Hình 5.3 và suy ngẫm một chút về cách bạn tính toán đường đi đó. Nếu giống như hầu hết mọi người, bạn đã tìm ra đường đi từ u đến z bằng cách xem xét Hình 5.3, vạch ra một số đường đi từ u đến z, và bằng cách nào đó thuyết phục bản thân rằng con đường bạn đã chọn có chi phí thấp nhất trong số tất cả các con đường có thể. (Bạn đã kiểm tra tất cả 17 đường dẫn có thể có giữa u và z chưa? Có lẽ là không!) Phép tính như vậy là một ví dụ về thuật toán định tuyến tập trung---thuật toán định tuyến được chạy ở một vị trí, bộ não của bạn, với thông tin đầy đủ về mạng. Nhìn rộng ra, một cách để chúng ta có thể phân loại các thuật toán định tuyến là tùy theo chúng được tập trung hay phi tập trung.

• Thuật toán định tuyến tập trung tính toán đường dẫn có chi phí thấp nhất giữa nguồn và đích bằng cách sử dụng kiến ​​thức toàn cầu, đầy đủ về mạng. Nghĩa là, thuật toán lấy kết nối giữa tất cả các nút và tất cả chi phí liên kết làm đầu vào. Điều này sau đó yêu cầu thuật toán bằng cách nào đó có được thông tin này trước khi thực sự thực hiện phép tính. Bản thân việc tính toán có thể được chạy tại một địa điểm (ví dụ: bộ điều khiển tập trung logic như trong Hình 5.2) hoặc có thể được sao chép trong thành phần định tuyến của mỗi bộ định tuyến (ví dụ: như trong Hình 5.1). Tuy nhiên, đặc điểm phân biệt chính ở đây là thuật toán có thông tin đầy đủ về kết nối và chi phí liên kết. Các thuật toán có thông tin trạng thái toàn cầu thường được gọi là thuật toán trạng thái liên kết (LS), vì thuật toán phải nhận biết được chi phí của mỗi liên kết trong mạng. Chúng ta sẽ nghiên cứu thuật toán LS trong Phần 5.2.1. • Trong thuật toán định tuyến phi tập trung, việc tính toán đường dẫn có chi phí thấp nhất được thực hiện theo cách lặp lại, phân tán bởi các bộ định tuyến. Không có nút nào có thông tin đầy đủ về chi phí của tất cả các liên kết mạng. Thay vào đó, mỗi nút chỉ bắt đầu với kiến ​​thức về chi phí của các liên kết được gắn trực tiếp của chính nó. Sau đó, thông qua quá trình tính toán lặp đi lặp lại và trao đổi thông tin với các nút lân cận, nút đó sẽ dần dần tính toán đường đi có chi phí thấp nhất tới một đích hoặc một tập hợp các đích. Thuật toán định tuyến phi tập trung mà chúng ta sẽ nghiên cứu bên dưới trong Phần 5.2.2 được gọi là thuật toán vectơ khoảng cách (DV), bởi vì mỗi nút duy trì một vectơ ước tính chi phí (khoảng cách) đến tất cả các nút khác trong mạng. Các thuật toán phi tập trung như vậy, với việc trao đổi tin nhắn tương tác giữa

các bộ định tuyến lân cận có lẽ phù hợp hơn với các mặt phẳng điều khiển nơi các bộ định tuyến tương tác trực tiếp với nhau, như trong Hình 5.1.

Cách rộng thứ hai để phân loại các thuật toán định tuyến là tùy theo chúng là tĩnh hay động. Trong thuật toán định tuyến tĩnh, các tuyến đường thay đổi rất chậm theo thời gian, thường là do sự can thiệp của con người (ví dụ: chi phí của con người khi chỉnh sửa thủ công một liên kết). Các thuật toán định tuyến động thay đổi đường dẫn định tuyến khi tải lưu lượng mạng hoặc cấu trúc liên kết thay đổi. Một thuật toán động có thể được chạy định kỳ hoặc để đáp ứng trực tiếp với các thay đổi về cấu trúc liên kết hoặc chi phí liên kết. Mặc dù các thuật toán động phản ứng nhanh hơn với các thay đổi của mạng nhưng chúng cũng dễ gặp phải các vấn đề hơn như vòng lặp định tuyến và dao động tuyến đường.

Cách thứ ba để phân loại các thuật toán định tuyến là tùy theo chúng nhạy cảm với tải hay không nhạy cảm với tải. Trong thuật toán phụ thuộc vào tải, chi phí liên kết thay đổi linh hoạt để phản ánh mức độ tắc nghẽn hiện tại trong liên kết cơ bản. Nếu chi phí cao liên quan đến một liên kết hiện đang bị tắc nghẽn, thuật toán định tuyến sẽ có xu hướng chọn các tuyến đường xung quanh một liên kết bị tắc nghẽn như vậy. Mặc dù các thuật toán định tuyến ARPAnet ban đầu rất nhạy cảm với tải \[McQuillan 1980\] nhưng đã gặp phải một số khó khăn \[Huitema 1998\]. Các thuật toán định tuyến Internet ngày nay (chẳng hạn như RIP, OSPF và BGP) không nhạy cảm với tải vì chi phí của liên kết không phản ánh rõ ràng mức độ tắc nghẽn hiện tại (hoặc quá khứ gần đây).

**5.2.1 Thuật toán định tuyến trạng thái liên kết (LS)**

Hãy nhớ lại rằng trong thuật toán trạng thái liên kết, cấu trúc liên kết mạng và tất cả chi phí liên kết đều được biết đến, nghĩa là có sẵn làm đầu vào cho thuật toán LS. Trong thực tế, điều này được thực hiện bằng cách yêu cầu mỗi nút phát các gói trạng thái liên kết tới tất cả các nút khác trong mạng, với mỗi gói trạng thái liên kết chứa danh tính và chi phí của các liên kết đính kèm của nó. Trong thực tế (ví dụ, với giao thức định tuyến OSPF của Internet, được thảo luận trong Phần 5.3), điều này thường được thực hiện bằng thuật toán quảng bá trạng thái liên kết \[Perlman 1999\]. Kết quả của việc phát sóng các nút là tất cả các nút đều có chế độ xem mạng giống hệt và đầy đủ. Sau đó, mỗi nút có thể chạy thuật toán LS và tính toán cùng một tập hợp các đường dẫn có chi phí thấp nhất như mọi nút khác.

Thuật toán định tuyến trạng thái liên kết mà chúng tôi trình bày dưới đây được gọi là thuật toán Dijkstra, được đặt theo tên của người phát minh ra nó. Một thuật toán có liên quan chặt chẽ là thuật toán Prim; xem \[Cormen 2001\] để biết thảo luận chung về thuật toán đồ thị. Thuật toán của Dijkstra tính toán đường dẫn có chi phí thấp nhất từ ​​một nút (nguồn mà chúng ta sẽ gọi là u) đến tất cả các nút khác trong mạng. Thuật toán của Dijkstra có tính lặp lại và có đặc tính là sau lần lặp thứ k của thuật toán, các đường dẫn có chi phí thấp nhất được biết đến bởi k nút đích và trong số các đường dẫn có chi phí thấp nhất đến tất cả các đích

các nút, k đường dẫn này sẽ có k chi phí nhỏ nhất. Hãy xác định ký hiệu sau:

• D(v): chi phí của đường đi có chi phí thấp nhất từ ​​nút nguồn đến đích v kể từ lần lặp lại thuật toán này. • p(v): nút trước đó (láng giềng của v) dọc theo đường dẫn có chi phí thấp nhất hiện tại từ nguồn đến v. • N′: tập con của các nút; v nằm trong N′ nếu đường đi có chi phí thấp nhất từ ​​nguồn đến v được biết rõ ràng.

Thuật toán định tuyến tập trung bao gồm một bước khởi tạo, sau đó là một vòng lặp. Số lần vòng lặp được thực hiện bằng số nút trong mạng. Sau khi kết thúc, thuật toán sẽ tính toán các đường đi ngắn nhất từ ​​nút nguồn u đến mọi nút khác trong mạng.

Thuật toán trạng thái liên kết (LS) cho nút nguồn u

1 Khởi tạo: 2 N\' = {u} 3 cho tất cả các nút v 4 nếu v là lân cận của u 5 thì D(v) = c(u,v) 6 ngược lại D(v) = ∞ 8 Vòng 9 tìm w không thuộc N\' sao cho D(w) tối thiểu 10 cộng w vào N\' 11 cập nhật D(v) cho mỗi lân cận v của w và không thuộc N\': 12 D(v) = min(D(v), D(w)+ c(w,v) ) 13 /\* chi phí mới tới v là chi phí cũ tới v hoặc đã biết 14 chi phí đường đi tối thiểu tới w cộng với chi phí từ w đến v \*/ 15 cho đến khi N\'= N

Ví dụ: hãy xem xét mạng trong Hình 5.3 và tính toán các đường dẫn có chi phí thấp nhất từ ​​u đến tất cả các đích có thể. Bảng tóm tắt tính toán của thuật toán được trình bày trong Bảng 5.1, trong đó mỗi dòng trong bảng đưa ra giá trị của các biến của thuật toán ở cuối vòng lặp. Hãy xem xét chi tiết một số bước đầu tiên.

• Trong bước khởi tạo, các đường dẫn có chi phí thấp nhất hiện đã biết từ u đến các lân cận gắn trực tiếp của nó, v, x và w, được khởi tạo lần lượt là 2, 1 và 5. Ghi chú trong

cụ thể là chi phí của w được đặt thành 5 (mặc dù chúng ta sẽ sớm thấy rằng đường dẫn có chi phí thấp hơn thực sự tồn tại) vì đây là chi phí của liên kết trực tiếp (một bước nhảy) từ u đến w. Chi phí của y và z được đặt thành vô cùng vì chúng không được kết nối trực tiếp với u. • Trong lần lặp đầu tiên, chúng ta tìm kiếm trong số các nút chưa được thêm vào tập N′ và tìm nút đó có chi phí thấp nhất tính đến thời điểm kết thúc lần lặp trước. Nút đó là x, với giá là 1 và do đó x được thêm vào tập N′. Dòng 12 của thuật toán LS sau đó được thực hiện để cập nhật D(v) cho tất cả các nút v, thu được kết quả hiển thị ở dòng thứ hai (Bước 1) trong Bảng 5.1. Chi phí của đường đi tới v không đổi. Chi phí của đường dẫn đến w (là 5 khi kết thúc quá trình khởi tạo) qua nút x được tìm thấy có chi phí là 4. Do đó, đường dẫn có chi phí thấp hơn này được chọn và đường dẫn trước của w dọc theo đường đi ngắn nhất từ ​​u được đặt thành x. Tương tự, chi phí cho y (đến x) được tính là 2 và bảng được cập nhật tương ứng. • Trong lần lặp thứ hai, các nút v và y được tìm thấy có đường đi có chi phí thấp nhất (2), và chúng ta phá vỡ ràng buộc tùy ý và thêm y vào tập N′ để N′ bây giờ chứa u, x và y. Chi phí cho các nút còn lại chưa thuộc N′, tức là các nút v, w và z được cập nhật qua dòng 12 của thuật toán LS, thu được kết quả như ở hàng thứ ba trong Bảng 5.1. • Và vân vân. . .

Khi thuật toán LS kết thúc, đối với mỗi nút, chúng ta có nút trước nó dọc theo đường dẫn có chi phí thấp nhất từ ​​nút nguồn. Đối với mỗi phần trước, chúng ta cũng có phần trước của nó, và theo cách này, chúng ta có thể xây dựng toàn bộ đường đi từ nguồn đến tất cả các đích. Bảng chuyển tiếp trong một nút, chẳng hạn như nút u, sau đó có thể được xây dựng từ thông tin này bằng cách lưu trữ, đối với mỗi đích, nút bước nhảy tiếp theo trên đường dẫn có chi phí thấp nhất từ ​​u đến đích. Hình 5.4 cho thấy các đường dẫn có chi phí thấp nhất và bảng chuyển tiếp trong u cho mạng trong Hình 5.3.

Bảng 5.1 ♦ Chạy thuật toán trạng thái liên kết trên mạng trong Hình 5.3

bước N' D (v), p (v) D (w), p (w) D (x), p (x) D (y), p (y) D (z), p (z)

u 2, u 5, u 1,u ∞ ∞

ux 2, u 4, x 2, x ∞

uxy 2, u 3, y 4, y

uxyv 3, y 4, y

uxyvw 4, y

uxyvwz

Độ phức tạp tính toán của thuật toán này là gì? Nghĩa là, với n nút (không tính nguồn), phải thực hiện bao nhiêu tính toán trong trường hợp xấu nhất để tìm ra đường đi có chi phí thấp nhất từ ​​nguồn đến tất cả các đích? Trong lần lặp đầu tiên, chúng ta cần tìm kiếm qua tất cả n nút để xác định nút w, không thuộc N′ có chi phí tối thiểu. Trong lần lặp thứ hai, chúng ta cần kiểm tra n - 1 nút để xác định chi phí tối thiểu; trong lần lặp thứ ba n - 2 nút, v.v. Nhìn chung, tổng số nút chúng ta cần tìm kiếm trong tất cả các lần lặp là n(n + 1)/2, và do đó chúng ta nói rằng việc triển khai thuật toán LS trước đó có độ phức tạp trong trường hợp xấu nhất là bình phương n: O(n2). (Việc triển khai thuật toán này phức tạp hơn, sử dụng cấu trúc dữ liệu được gọi là heap, có thể tìm giá trị tối thiểu ở dòng 9 theo logarit thay vì thời gian tuyến tính, do đó làm giảm độ phức tạp.)

Trước khi hoàn thành phần thảo luận về thuật toán LS, chúng ta hãy xem xét một bệnh lý có thể phát sinh. Ví dụ, Hình 5.5 cho thấy một cấu trúc liên kết mạng đơn giản trong đó chi phí liên kết bằng với tải mang trên liên kết, phản ánh độ trễ có thể xảy ra. Trong ví dụ này, chi phí liên kết không cân xứng; nghĩa là, c(u,v) chỉ bằng c(v,u) nếu tải mang trên cả hai hướng trên liên kết (u,v) là như nhau. Trong ví dụ này, nút z khởi tạo một đơn vị lưu lượng dành cho w, nút x cũng khởi tạo một đơn vị lưu lượng dành cho w, và nút y đưa vào một lượng lưu lượng bằng e, cũng dành cho w. Định tuyến ban đầu được hiển thị trong Hình 5.5(a) với chi phí liên kết tương ứng với lượng lưu lượng được mang theo.

Khi thuật toán LS được chạy tiếp theo, nút y xác định (dựa trên chi phí liên kết được hiển thị trong Hình 5.5(a)) rằng đường đi theo chiều kim đồng hồ tới w có chi phí là 1, trong khi đường đi ngược chiều kim đồng hồ đến w (mà nó đã sử dụng) có chi phí là 1 + e. Do đó, đường đi có chi phí thấp nhất của y đến w hiện theo chiều kim đồng hồ. Tương tự, x xác định rằng đường dẫn có chi phí thấp nhất mới của nó tới w cũng theo chiều kim đồng hồ, dẫn đến chi phí được hiển thị trong Hình 5.5(b). Khi thuật toán LS được chạy tiếp theo, các nút x, y và z đều phát hiện đường dẫn có chi phí bằng 0 tới w theo hướng ngược chiều kim đồng hồ và tất cả đều định tuyến lưu lượng truy cập của chúng đến các tuyến ngược chiều kim đồng hồ. Lần tiếp theo khi thuật toán LS được chạy, x, y và z đều định tuyến lưu lượng truy cập của chúng theo các tuyến theo chiều kim đồng hồ.

Có thể làm gì để ngăn chặn những dao động như vậy (có thể xảy ra trong bất kỳ thuật toán nào, không chỉ thuật toán LS, sử dụng số liệu liên kết dựa trên tắc nghẽn hoặc độ trễ)? Một giải pháp là yêu cầu chi phí liên kết không phụ thuộc vào lượng lưu lượng truy cập

Liên kết đích

v w

x y z

(u, v) (u, x) (u, x) (u, x) (u, x) x y

v

bạn z

w

*Hình 5.4 ♦ Đường dẫn và bảng chuyển tiếp có chi phí thấp nhất cho nút u*

được thực hiện---một giải pháp không thể chấp nhận được vì một mục tiêu của định tuyến là tránh các liên kết bị tắc nghẽn cao (ví dụ: độ trễ cao). Một giải pháp khác là đảm bảo rằng không phải tất cả các bộ định tuyến đều chạy thuật toán LS cùng một lúc. Đây có vẻ là một giải pháp hợp lý hơn, vì chúng tôi hy vọng rằng ngay cả khi các bộ định tuyến chạy thuật toán LS với cùng một chu kỳ, thì phiên bản thực thi của thuật toán sẽ không giống nhau ở mỗi nút. Điều thú vị là các nhà nghiên cứu đã phát hiện ra rằng các bộ định tuyến trên Internet có thể tự đồng bộ hóa với nhau \[Floyd Synchronization 1994\]. Nghĩa là, mặc dù ban đầu họ thực thi thuật toán trong cùng một khoảng thời gian nhưng ở các thời điểm khác nhau, phiên bản thực thi thuật toán cuối cùng có thể trở thành và duy trì được đồng bộ hóa tại các bộ định tuyến. Một cách để tránh hiện tượng tự đồng bộ hóa như vậy là mỗi bộ định tuyến sẽ ngẫu nhiên hóa thời gian gửi quảng cáo liên kết.

Sau khi nghiên cứu thuật toán LS, chúng ta hãy xem xét thuật toán định tuyến chính khác được sử dụng trong thực tế ngày nay---thuật toán định tuyến vectơ khoảng cách.

w

y

z

x

e

1 + e

Một. Định tuyến ban đầu

e

w

y

z

x

2 + e

1 + e

b\. x, y phát hiện đường đi tốt hơn tới w, theo chiều kim đồng hồ

w

y

z

x

1 + e

2+ e

c\. x, y, z phát hiện đường đi tốt hơn

đến w, ngược chiều kim đồng hồ

w

y

z

x

2 + e

1 + e

d\. x, y, z, phát hiện đường đi tốt hơn tới w, theo chiều kim đồng hồ

e

e

e

*Hình 5.5 ♦ Dao động với định tuyến nhạy cảm với tắc nghẽn*

**5.2.2 Thuật toán định tuyến vectơ khoảng cách (DV)**

Trong khi thuật toán LS là thuật toán sử dụng thông tin toàn cục thì thuật toán vectơ khoảng cách (DV) là thuật toán lặp, không đồng bộ và phân tán. Nó được phân phối ở chỗ mỗi nút nhận một số thông tin từ một hoặc nhiều nút lân cận được gắn trực tiếp, thực hiện phép tính và sau đó phân phối kết quả tính toán của nó cho các nút lân cận. Nó lặp đi lặp lại ở chỗ quá trình này tiếp tục cho đến khi không còn thông tin nào được trao đổi giữa các hàng xóm. (Điều thú vị là thuật toán cũng tự kết thúc---không có tín hiệu nào cho thấy quá trình tính toán sẽ dừng; nó chỉ dừng lại.) Thuật toán không đồng bộ ở chỗ nó không yêu cầu tất cả các nút hoạt động theo từng bước khóa với nhau. Chúng ta sẽ thấy rằng thuật toán phân tán, lặp lại, tự kết thúc, không đồng bộ thú vị và vui nhộn hơn nhiều so với thuật toán tập trung!

Trước khi trình bày thuật toán DV, sẽ rất hữu ích khi thảo luận về mối quan hệ quan trọng tồn tại giữa chi phí của các đường đi có chi phí thấp nhất. Gọi dx(y) là chi phí của đường đi có chi phí thấp nhất từ ​​nút x đến nút y. Khi đó chi phí thấp nhất có liên quan đến phương trình Bellman-Ford nổi tiếng, cụ thể là:

dx(y) = minv5c(x, v) + dv(y)6, (5.1)

trong đó minv trong phương trình được lấy trên tất cả các lân cận của x. Phương trình BellmanFord khá trực quan. Thật vậy, sau khi đi từ x đến v, nếu chúng ta đi theo đường đi có chi phí thấp nhất từ ​​v đến y thì chi phí đường đi sẽ là c(x, v) + dv(y). Vì chúng ta phải bắt đầu bằng việc du hành đến một hàng xóm v nào đó, nên chi phí nhỏ nhất từ ​​x đến y là giá trị nhỏ nhất của c(x, v) + dv(y) trên tất cả các hàng xóm v.

Nhưng đối với những người có thể nghi ngờ về tính hợp lệ của phương trình, hãy kiểm tra nút nguồn u và nút đích z trong Hình 5.3. Nút nguồn u có ba nút lân cận: nút v, x và w. Bằng cách đi dọc theo các đường khác nhau trong đồ thị, dễ dàng thấy rằng dv(z) = 5, dx(z) = 3, và dw(z) = 3. Thay các giá trị này vào phương trình 5.1, cùng với các chi phí c(u, v) = 2, c(u, x) = 1, và c(u, w) = 5, ta có du(z) = min52 + 5, 5 + 3, 1 + 36 = 4, điều này rõ ràng là đúng và đó chính xác là những gì thuật toán Dijskstra đã mang lại cho chúng ta đối với cùng một mạng. Việc xác minh nhanh chóng này sẽ giúp giảm bớt mọi hoài nghi mà bạn có thể có.

Phương trình Bellman-Ford không chỉ là một sự tò mò mang tính trí tuệ. Nó thực sự có tầm quan trọng thực tiễn đáng kể: lời giải của phương trình Bellman-Ford cung cấp các mục trong bảng chuyển tiếp của nút x. Để thấy điều này, hãy đặt v\* là bất kỳ nút lân cận nào đạt được mức tối thiểu trong phương trình 5.1. Sau đó, nếu nút x muốn gửi một gói đến nút y dọc theo đường dẫn có chi phí thấp nhất thì trước tiên nó phải chuyển tiếp gói đến nút v\*. Do đó, bảng chuyển tiếp của nút x sẽ chỉ định nút v\* làm bộ định tuyến bước nhảy tiếp theo cho đích cuối cùng y. Một đóng góp thực tế quan trọng khác của phương trình Bellman-Ford là nó gợi ý hình thức giao tiếp giữa các hàng xóm sẽ diễn ra trong thuật toán DV.

Ý tưởng cơ bản là như sau. Mỗi nút x bắt đầu bằng Dx(y), ước tính chi phí của đường đi có chi phí thấp nhất từ ​​chính nó đến nút y, cho tất cả các nút, y, trong N. Đặt Dx = \[Dx(y): y in N\] là vectơ khoảng cách của nút x, là vectơ ước tính chi phí từ x đến tất cả các nút khác, y, trong N. Với thuật toán DV, mỗi nút x duy trì thông tin định tuyến sau:

• Đối với mỗi lân cận v, chi phí c(x,v) từ x đến lân cận gắn trực tiếp, v • Vectơ khoảng cách của nút x, nghĩa là Dx = \[Dx(y): y in N\], chứa ước tính của x về chi phí của nó tới tất cả các đích, y, trong N • Vectơ khoảng cách của mỗi lân cận của nó, nghĩa là Dv = \[Dv(y): y in N\] cho mỗi lân cận v của x

Trong thuật toán không đồng bộ, phân tán, thỉnh thoảng mỗi nút sẽ gửi một bản sao của vectơ khoảng cách đến từng nút lân cận. Khi nút x nhận được một vectơ khoảng cách mới từ bất kỳ nút lân cận w nào, nó sẽ lưu vectơ khoảng cách của w và sau đó sử dụng phương trình Bellman-Ford để cập nhật vectơ khoảng cách của chính nó như sau:

Dx(y) = minv5c(x, v) + Dv(y)6 cho mỗi nút y trong N

Nếu vectơ khoảng cách của nút x đã thay đổi do bước cập nhật này, thì nút x sau đó sẽ gửi vectơ khoảng cách đã cập nhật của nó tới từng nút lân cận, từ đó các nút này có thể cập nhật vectơ khoảng cách của chính chúng. Thật kỳ diệu, miễn là tất cả các nút tiếp tục trao đổi vectơ khoảng cách của chúng theo kiểu không đồng bộ, mỗi ước tính chi phí Dx(y) sẽ hội tụ về dx(y), chi phí thực tế của đường đi có chi phí thấp nhất từ ​​nút x đến nút y \[Bertsekas 1991\]!

Thuật toán vectơ khoảng cách (DV)

Tại mỗi nút, x:

1 Khởi tạo: 2 cho tất cả các đích y trong N: 3 Dx(y)= c(x,y)/\* nếu y không phải là hàng xóm thì c(x,y)= ∞ \*/ 4 cho mỗi hàng xóm w 5 Dw(y) = ? cho tất cả các đích y trong N 6 cho mỗi hàng xóm w 7 gửi vectơ khoảng cách Dx = \[Dx(y): y in N\] tới w 9 vòng 10 đợi (cho đến khi tôi thấy chi phí liên kết thay đổi đối với hàng xóm nào đó w hoặc 11 cho đến khi tôi nhận được vectơ khoảng cách từ hàng xóm nào đó w) 13 cho mỗi y trong N: 14 Dx(y) = minv{c(x,v) + Dv(y)} 16 nếu Dx(y) thay đổi cho bất kỳ đích y nào 17 gửi vectơ khoảng cách Dx = \[Dx(y): y in N\] tới tất cả hàng xóm 19 mãi mãi

Trong thuật toán DV, nút x cập nhật ước tính vectơ khoảng cách của nó khi nó thấy sự thay đổi chi phí ở một trong các liên kết được gắn trực tiếp của nó hoặc nhận được bản cập nhật vectơ khoảng cách từ một số hàng xóm. Nhưng để cập nhật bảng chuyển tiếp của chính nó cho đích y cho trước, điều mà nút x thực sự cần biết không phải là khoảng cách đường đi ngắn nhất tới y mà thay vào đó là nút lân cận v\*(y) là bộ định tuyến bước nhảy tiếp theo dọc theo đường đi ngắn nhất tới y. Như bạn có thể mong đợi, bộ định tuyến bước nhảy tiếp theo v\*(y) là hàng xóm v đạt được mức tối thiểu trong Dòng 14 của thuật toán DV. (Nếu có nhiều lân cận v đạt mức tối thiểu thì v\*(y) có thể là bất kỳ lân cận giảm thiểu nào.) Do đó, trong các Dòng 13--14, đối với mỗi đích y, nút x cũng xác định v\*(y) và cập nhật bảng chuyển tiếp của nó cho đích y.

Hãy nhớ lại rằng thuật toán LS là một thuật toán tập trung theo nghĩa là nó yêu cầu mỗi nút trước tiên phải có được bản đồ mạng hoàn chỉnh trước khi chạy thuật toán Dijkstra. Thuật toán DV được phân cấp và không sử dụng thông tin toàn cầu như vậy. Thật vậy, thông tin duy nhất mà một nút sẽ có là chi phí của các liên kết đến các nút lân cận được gắn trực tiếp và thông tin mà nó nhận được từ các nút lân cận này. Mỗi nút chờ cập nhật từ bất kỳ nút lân cận nào (Dòng 10--11), tính toán vectơ khoảng cách mới của nó khi nhận được bản cập nhật (Dòng 14) và phân phối vectơ khoảng cách mới của nó cho các nút lân cận (Dòng 16--17). Các thuật toán giống DV được sử dụng trong nhiều giao thức định tuyến trong thực tế, bao gồm RIP và BGP của Internet, ISO IDRP, Novell IPX và ARPAnet gốc.

Hình 5.6 minh họa hoạt động của thuật toán DV cho mạng ba nút đơn giản được hiển thị ở đầu hình. Hoạt động của thuật toán được minh họa một cách đồng bộ, trong đó tất cả các nút đồng thời nhận vectơ khoảng cách từ các nút lân cận, tính toán các vectơ khoảng cách mới và thông báo cho các nút lân cận nếu vectơ khoảng cách của chúng thay đổi. Sau khi nghiên cứu ví dụ này, bạn nên tự thuyết phục mình rằng thuật toán cũng hoạt động chính xác theo cách không đồng bộ, với việc tính toán nút và tạo/tiếp nhận cập nhật xảy ra bất kỳ lúc nào.

Cột ngoài cùng bên trái của hình hiển thị ba bảng định tuyến ban đầu cho mỗi nút trong số ba nút. Ví dụ: bảng ở góc trên bên trái là bảng định tuyến ban đầu của nút x. Trong một bảng định tuyến cụ thể, mỗi hàng là một vectơ khoảng cách--- cụ thể, bảng định tuyến của mỗi nút bao gồm vectơ khoảng cách của chính nó và của mỗi nút lân cận. Do đó, hàng đầu tiên trong bảng định tuyến ban đầu của nút x là

Dx = \[Dx(x), Dx(y), Dx(z)\] = \[0, 2, 7\]. Hàng thứ hai và thứ ba trong bảng này lần lượt là các vectơ khoảng cách nhận được gần đây nhất từ ​​các nút y và z. Vì lúc khởi tạo nút x chưa nhận được bất kỳ thứ gì từ nút y hoặc z nên các mục ở hàng thứ hai và thứ ba được khởi tạo thành vô cùng.

Sau khi khởi tạo, mỗi nút sẽ gửi vectơ khoảng cách của nó tới hai nút lân cận. Điều này được minh họa trong Hình 5.6 bằng các mũi tên từ cột đầu tiên của bảng đến cột thứ hai của bảng. Ví dụ: nút x gửi vectơ khoảng cách Dx = \[0, 2, 7\] tới cả hai nút y và z. Sau khi nhận được các bản cập nhật, mỗi nút sẽ tính toán lại vectơ khoảng cách của chính nó. Ví dụ: nút x tính toán

Dx(x) = 0

Dx(y) = min5c(x,y) + Dy(y), c(x,z) + Dz(y)6 = min52 + 0, 7 + 16 = 2

Dx(z) = min5c(x,y) + Dy(z), c(x,z) + Dz(z)6 = min52 + 1, 7 + 06 = 3

Do đó, cột thứ hai hiển thị, đối với mỗi nút, vectơ khoảng cách mới của nút cùng với vectơ khoảng cách vừa nhận được từ các nút lân cận. Lưu ý, ví dụ, rằng

Bảng nút y

Bảng nút x

0 2 7

x y z

\` \` \` \` \`\`

Thời gian

y

x

z

Bảng nút z

từ

chi phí để

x y z

0 2 3

x y z

2 0 1 7 1 0

từ

chi phí để

x y z

0 2 3

x y z

2 0 1 3 1 0

từ

chi phí để

x y z

2 0 1

x y z

\` \` \`

\` \` \`

từ

chi phí để

x y z

0 2 7

x y z

2 0 1 7 1 0

từ

chi phí để

x y z

0 2 3

x y z

2 0 1 3 1 0

từ

chi phí để

x y z

7 1 0

x y z

\` \` \` \` \`\`

từ

chi phí để

x y z

0 2 7

x y z

2 0 1 3 1 0

từ

chi phí để

x y z

0 2 3

x y z

2 0 1 3 1 0

từ

chi phí để

x y z

*Hình 5.6 ♦ Thuật toán vectơ khoảng cách (DV) đang hoạt động*

ước tính của nút x về chi phí nhỏ nhất đối với nút z, Dx(z), đã thay đổi từ 7 thành 3. Cũng lưu ý rằng đối với nút x, nút y lân cận đạt được mức tối thiểu trong dòng 14 của thuật toán DV; do đó, ở giai đoạn này của thuật toán, tại nút x, chúng ta có v\*(y) = y và v\*(z) = y.

Sau khi các nút tính toán lại vectơ khoảng cách của chúng, chúng lại gửi vectơ khoảng cách đã cập nhật đến các nút lân cận (nếu có thay đổi). Điều này được minh họa trong Hình 5.6 bằng các mũi tên từ cột thứ hai của bảng đến cột thứ ba của bảng. Lưu ý rằng chỉ các nút x và z gửi bản cập nhật: vectơ khoảng cách của nút y không thay đổi nên nút y không gửi bản cập nhật. Sau khi nhận được các bản cập nhật, các nút sẽ tính toán lại vectơ khoảng cách và cập nhật bảng định tuyến của chúng, được hiển thị trong cột thứ ba.

Quá trình nhận các vectơ khoảng cách được cập nhật từ các hàng xóm, tính toán lại các mục trong bảng định tuyến và thông báo cho các hàng xóm về chi phí đã thay đổi của đường đi có chi phí thấp nhất tới đích tiếp tục cho đến khi không có thông báo cập nhật nào được gửi. Tại thời điểm này, do không có thông báo cập nhật nào được gửi nên sẽ không có phép tính toán nào trong bảng định tuyến tiếp theo và thuật toán sẽ chuyển sang trạng thái không hoạt động; nghĩa là tất cả các nút sẽ thực hiện chờ ở Dòng 10--11 của thuật toán DV. Thuật toán vẫn ở trạng thái không hoạt động cho đến khi chi phí liên kết thay đổi, như được thảo luận tiếp theo.

Thuật toán vectơ khoảng cách: Thay đổi chi phí liên kết và lỗi liên kết

Khi một nút chạy thuật toán DV phát hiện sự thay đổi về chi phí liên kết từ chính nó sang nút lân cận (Dòng 10--11), nút đó sẽ cập nhật vectơ khoảng cách (Dòng 13--14) và nếu có thay đổi về chi phí của đường dẫn có chi phí thấp nhất, hãy thông báo cho các nút lân cận (Dòng 16--17) về vectơ khoảng cách mới của nó. Hình 5.7(a) minh họa một kịch bản trong đó chi phí liên kết từ y đến x thay đổi từ 4 thành 1. Ở đây chúng tôi chỉ tập trung vào các mục trong bảng khoảng cách của y' và z tới đích x. Thuật toán DV khiến chuỗi sự kiện sau xảy ra:

• Tại thời điểm t0, y phát hiện sự thay đổi chi phí liên kết (chi phí đã thay đổi từ 4 thành 1), cập nhật vectơ khoảng cách của nó và thông báo cho các hàng xóm của nó về sự thay đổi này do vectơ khoảng cách của nó đã thay đổi. • Tại thời điểm t1, z nhận được cập nhật từ y và cập nhật bảng của nó. Nó tính toán chi phí nhỏ nhất mới cho x (nó đã giảm từ chi phí 5 xuống chi phí 2) và gửi vectơ khoảng cách mới của nó tới các hàng xóm của nó. • Tại thời điểm t2, y nhận được thông tin cập nhật của z và cập nhật bảng khoảng cách của nó. Chi phí tối thiểu của y không thay đổi và do đó y không gửi bất kỳ thông điệp nào đến z. Thuật toán đi đến trạng thái không hoạt động.

Do đó, chỉ cần hai lần lặp để thuật toán DV đạt đến trạng thái không hoạt động. Tin vui về chi phí giảm giữa x và y đã được lan truyền nhanh chóng trên mạng.

Bây giờ chúng ta hãy xem điều gì có thể xảy ra khi chi phí liên kết tăng lên. Giả sử chi phí liên kết giữa x và y tăng từ 4 lên 60, như trong Hình 5.7(b).

1\. Trước khi chi phí liên kết thay đổi, Dy(x) = 4, Dy(z) = 1, Dz(y) = 1, và Dz(x) = 5.

Tại thời điểm t0, y phát hiện sự thay đổi chi phí liên kết (chi phí đã thay đổi từ 4 lên 60). y tính toán đường đi có chi phí tối thiểu mới của nó tới x để có chi phí là

Dy(x) = min5c(y,x) + Dx(x), c(y,z) + Dz(x)6 = min560 + 0, 1 + 56 = 6

Tất nhiên, với cái nhìn toàn cầu về mạng, chúng ta có thể thấy rằng chi phí mới này thông qua

z sai rồi. Nhưng nút thông tin duy nhất y có là chi phí trực tiếp của nó tới x là 60 và z đã nói với y lần cuối rằng z có thể đến x với chi phí là 5. Vì vậy, để đến x, y bây giờ sẽ định tuyến qua z, hoàn toàn mong đợi rằng z sẽ có thể đến x với chi phí là 5. Kể từ t1, chúng ta có một vòng định tuyến---để đến x, y đi qua z và z đi qua y. Vòng lặp định tuyến giống như một lỗ đen---một gói tin dành cho x đến y hoặc z kể từ t1 sẽ nảy qua lại giữa hai nút này mãi mãi (hoặc cho đến khi bảng chuyển tiếp được thay đổi). 2. Vì nút y đã tính chi phí tối thiểu mới cho x nên nó thông báo cho z về chi phí tối thiểu mới của nó.

vectơ khoảng cách tại thời điểm t1. 3. Một thời gian sau t1, z nhận được vectơ khoảng cách mới của y, cho biết rằng y

chi phí tối thiểu của x là 6. z biết rằng nó có thể đến y với chi phí là 1 và do đó tính chi phí nhỏ nhất mới cho x của Dz(x) = min550 + 0,1 + 66 = 7. Vì chi phí nhỏ nhất của z đối với x đã tăng lên, nên nó sẽ thông báo cho y về vectơ khoảng cách mới của nó tại t2. 4. Tương tự, sau khi nhận được vectơ khoảng cách mới của z, y xác định

Dy(x) = 8 và gửi z vectơ khoảng cách của nó. z sau đó xác định Dz(x) = 9 và gửi y vectơ khoảng cách của nó, v.v.

Quá trình này sẽ tiếp tục trong bao lâu? Bạn nên thuyết phục bản thân rằng vòng lặp sẽ tồn tại trong 44 lần lặp (trao đổi thông báo giữa y và z)---cho đến khi z cuối cùng tính toán chi phí của đường đi qua y lớn hơn 50. Tại thời điểm này, z sẽ (cuối cùng!) xác định rằng đường đi có chi phí thấp nhất tới x là thông qua kết nối trực tiếp tới x. vậy thì bạn sẽ

y

x

Một. b.

z

y

x

z

*Hình 5.7 ♦ Thay đổi chi phí liên kết*

định tuyến tới x qua z. Kết quả của tin xấu về việc tăng chi phí liên kết thực sự đã lan truyền rất chậm! Điều gì sẽ xảy ra nếu chi phí liên kết c(y, x) thay đổi từ 4 thành 10.000 và chi phí c(z, x) là 9.999? Vì những tình huống như vậy, bài toán mà chúng ta gặp đôi khi được gọi là bài toán đếm đến vô cùng.

Thuật toán vectơ khoảng cách: Thêm đảo ngược bị nhiễm độc

Có thể tránh được kịch bản lặp cụ thể vừa mô tả bằng cách sử dụng một kỹ thuật được gọi là đảo ngược bị đầu độc. Ý tưởng rất đơn giản---nếu z định tuyến qua y để đến đích x thì z sẽ thông báo cho y rằng khoảng cách của nó tới x là vô cùng, nghĩa là z sẽ thông báo cho y rằng Dz(x) = ∞ (mặc dù z biết thực tế Dz(x) = 5). z sẽ tiếp tục nói lời nói dối trắng trợn này với y miễn là nó định tuyến đến x qua y. Vì y tin rằng z không có đường dẫn đến x nên y sẽ không bao giờ cố gắng định tuyến đến x qua z, miễn là z tiếp tục định tuyến đến x qua y (và nói dối về việc làm như vậy).

Bây giờ chúng ta hãy xem cách đảo ngược độc hại giải quyết vấn đề lặp cụ thể mà chúng ta gặp phải trước đây trong Hình 5.5(b). Kết quả của sự đảo ngược bị nhiễm độc là bảng khoảng cách của y chỉ ra Dz(x) = ∞. Khi chi phí của liên kết (x, y) thay đổi từ 4 đến 60 tại thời điểm t0, y cập nhật bảng của nó và tiếp tục định tuyến trực tiếp đến x, mặc dù với chi phí cao hơn là 60, và thông báo cho z về chi phí mới của nó tới x, nghĩa là Dy(x) = 60. Sau khi nhận được bản cập nhật tại t1, z ngay lập tức chuyển tuyến của nó sang x thông qua liên kết trực tiếp (z, x) với chi phí là 50. Vì đây là đường dẫn có chi phí thấp nhất mới đến x, và vì vậy đường đi không còn đi qua y nữa, z bây giờ báo cho y rằng Dz(x) = 50 tại t2. Sau khi nhận được bản cập nhật từ z, y cập nhật bảng khoảng cách của nó với Dy(x) = 51. Ngoài ra, vì z hiện nằm trên đường có chi phí thấp nhất của y tới x, y sẽ đầu độc đường đi ngược từ z đến x bằng cách thông báo cho z tại thời điểm t3 rằng Dy(x) = ∞ (mặc dù y biết rằng Dy(x) = 51 trên thực tế).

Liệu việc đảo ngược bị nhiễm độc có giải quyết được vấn đề đếm đến vô cùng chung không? Nó không. Bạn nên thuyết phục bản thân rằng các vòng lặp liên quan đến ba nút trở lên (chứ không chỉ đơn giản là hai nút lân cận ngay lập tức) sẽ không bị phát hiện bằng kỹ thuật đảo ngược bị đầu độc.

So sánh thuật toán định tuyến LS và DV

Các thuật toán DV và LS có những cách tiếp cận bổ sung cho việc định tuyến tính toán. Trong thuật toán DV, mỗi nút chỉ giao tiếp với các nút lân cận được kết nối trực tiếp, nhưng nó cung cấp cho các nút lân cận ước tính chi phí thấp nhất từ ​​chính nó tới tất cả các nút (mà nó biết) trong mạng. Thuật toán LS yêu cầu thông tin toàn cầu. Do đó, khi được triển khai trong mỗi bộ định tuyến, chẳng hạn như trong Hình 4.2 và 5.1, mỗi nút sẽ cần liên lạc với tất cả các nút khác (thông qua quảng bá), nhưng nó chỉ cho chúng biết chi phí của các liên kết được kết nối trực tiếp của nó. Hãy kết thúc nghiên cứu của chúng ta về thuật toán LS và DV bằng cách so sánh nhanh một số thuộc tính của chúng. Hãy nhớ lại rằng N là tập hợp các nút (bộ định tuyến) và E là tập hợp các cạnh (liên kết).

• Độ phức tạp của thông điệp. Chúng ta đã thấy rằng LS yêu cầu mỗi nút biết chi phí của mỗi liên kết trong mạng. Điều này yêu cầu phải gửi tin nhắn O(\|N\| \|E\|).

Ngoài ra, bất cứ khi nào chi phí liên kết thay đổi, chi phí liên kết mới phải được gửi đến tất cả các nút. Thuật toán DV yêu cầu trao đổi thông điệp giữa các hàng xóm được kết nối trực tiếp tại mỗi lần lặp. Chúng ta đã thấy rằng thời gian cần thiết để thuật toán hội tụ có thể phụ thuộc vào nhiều yếu tố. Khi chi phí liên kết thay đổi, thuật toán DV sẽ truyền bá kết quả của chi phí liên kết đã thay đổi nếu chi phí liên kết mới dẫn đến đường dẫn có chi phí thấp nhất được thay đổi cho một trong các nút được gắn vào liên kết đó. • Tốc độ hội tụ. Chúng ta đã thấy rằng việc triển khai LS của chúng ta là thuật toán O(\|N\|2) yêu cầu các thông báo O(\|N\| \|E\|)). Thuật toán DV có thể hội tụ chậm và có thể có các vòng định tuyến trong khi thuật toán đang hội tụ. DV cũng gặp phải vấn đề đếm đến vô cùng. • Độ bền. Điều gì có thể xảy ra nếu bộ định tuyến bị lỗi, hoạt động sai hoặc bị phá hoại? Trong LS, bộ định tuyến có thể phát đi một chi phí không chính xác cho một trong các liên kết được đính kèm của nó (nhưng không phát đi các liên kết khác). Một nút cũng có thể bị hỏng hoặc làm mất bất kỳ gói nào mà nó nhận được như một phần của chương trình phát sóng LS. Nhưng nút LS chỉ tính toán các bảng chuyển tiếp của chính nó; các nút khác đang thực hiện các phép tính tương tự cho chính chúng. Điều này có nghĩa là việc tính toán tuyến đường được tách biệt phần nào trong LS, mang lại mức độ chắc chắn hơn. Trong DV, một nút có thể quảng cáo các đường dẫn có chi phí thấp nhất không chính xác tới bất kỳ hoặc tất cả các đích. (Thật vậy, vào năm 1997, một bộ định tuyến gặp trục trặc trong một ISP nhỏ đã cung cấp cho các bộ định tuyến đường trục quốc gia thông tin định tuyến sai. Điều này khiến cho các bộ định tuyến khác làm tràn lưu lượng truy cập vào bộ định tuyến gặp trục trặc và khiến phần lớn Internet bị ngắt kết nối trong vài giờ \[Neumann 1997\].) Nói chung, chúng tôi lưu ý rằng, ở mỗi lần lặp, phép tính của một nút trong DV được chuyển cho nút lân cận của nó và sau đó gián tiếp đến nút lân cận của nút lân cận đó trong lần lặp tiếp theo. Theo nghĩa này, việc tính toán nút không chính xác có thể lan truyền khắp toàn bộ mạng trong DV.

Cuối cùng, không có thuật toán nào rõ ràng là người chiến thắng thuật toán kia; thực sự, cả hai thuật toán đều được sử dụng trên Internet.

**5.3 Định tuyến nội bộ AS trên Internet: OSPF**

Trong nghiên cứu về thuật toán định tuyến cho đến nay, chúng tôi đã xem mạng đơn giản là một tập hợp các bộ định tuyến được kết nối với nhau. Một bộ định tuyến không thể phân biệt được với một bộ định tuyến khác theo nghĩa là tất cả các bộ định tuyến đều thực thi cùng một thuật toán định tuyến để tính toán đường dẫn định tuyến qua toàn bộ mạng. Trong thực tế, mô hình này và quan điểm của nó về một tập hợp các bộ định tuyến đồng nhất đều thực hiện cùng một thuật toán định tuyến là đơn giản vì hai lý do quan trọng:

• Tỉ lệ. Khi số lượng bộ định tuyến trở nên lớn, chi phí liên quan đến việc liên lạc, tính toán và lưu trữ thông tin định tuyến trở nên quá cao. hôm nay

Internet bao gồm hàng trăm triệu bộ định tuyến. Việc lưu trữ thông tin định tuyến cho các đích đến có thể có tại mỗi bộ định tuyến này rõ ràng sẽ yêu cầu lượng bộ nhớ rất lớn. Chi phí cần thiết để phát sóng kết nối và cập nhật chi phí liên kết giữa tất cả các bộ định tuyến sẽ rất lớn! Thuật toán vectơ khoảng cách được lặp lại giữa một số lượng lớn bộ định tuyến như vậy chắc chắn sẽ không bao giờ hội tụ. Rõ ràng, cần phải làm gì đó để giảm độ phức tạp của việc tính toán tuyến đường trong một mạng lớn như Internet.

• Quyền tự chủ hành chính. Như được mô tả trong Phần 1.3, Internet là một mạng gồm các ISP, trong đó mỗi ISP bao gồm mạng bộ định tuyến riêng của nó. ISP thường mong muốn vận hành mạng của mình theo ý muốn (ví dụ: chạy bất kỳ thuật toán định tuyến nào mà nó chọn trong mạng của mình) hoặc để che giấu các khía cạnh của tổ chức nội bộ mạng của mình với bên ngoài. Lý tưởng nhất là một tổ chức có thể vận hành và quản lý mạng của mình theo ý muốn trong khi vẫn có thể kết nối mạng của mình với các mạng bên ngoài khác.

Cả hai vấn đề này đều có thể được giải quyết bằng cách tổ chức các bộ định tuyến thành các hệ thống tự trị (AS), với mỗi AS bao gồm một nhóm bộ định tuyến nằm dưới cùng sự kiểm soát quản trị. Thông thường các bộ định tuyến trong một ISP và các liên kết kết nối chúng tạo thành một AS duy nhất. Tuy nhiên, một số ISP phân vùng mạng của họ thành nhiều AS. Đặc biệt, một số ISP cấp 1 sử dụng một AS khổng lồ cho toàn bộ mạng của họ, trong khi những ISP khác chia ISP của họ thành hàng chục AS được kết nối với nhau. Một hệ thống tự trị được xác định bằng số hệ thống tự trị duy nhất trên toàn cầu (ASN) \[RFC 1930\]. Các số AS, như địa chỉ IP, được cơ quan đăng ký khu vực ICANN chỉ định \[ICANN 2020\].

Routers trong cùng một AS đều chạy cùng một thuật toán định tuyến và có thông tin về nhau. Thuật toán định tuyến chạy trong hệ thống tự trị được gọi là giao thức định tuyến hệ thống nội bộ tự trị.

Mở đường dẫn ngắn nhất trước (OSPF)

Định tuyến OSPF và người anh em họ hàng gần gũi của nó, IS-IS, được sử dụng rộng rãi để định tuyến nội bộ AS trên Internet. Open in OSPF chỉ ra rằng đặc tả giao thức định tuyến có sẵn công khai (ví dụ: trái ngược với giao thức EIGRP của Cisco, giao thức này chỉ mới được mở gần đây \[Savage 2015\], sau khoảng 20 năm là giao thức độc quyền của Cisco). Phiên bản mới nhất của OSPF, phiên bản 2, được xác định trong \[RFC 2328\], một tài liệu công khai.

OSPF là giao thức trạng thái liên kết sử dụng tràn thông tin trạng thái liên kết và thuật toán đường dẫn có chi phí thấp nhất của Dijkstra. Với OSPF, mỗi bộ định tuyến sẽ xây dựng một bản đồ tôpô hoàn chỉnh (nghĩa là một biểu đồ) của toàn bộ hệ thống tự trị. Sau đó, mỗi bộ định tuyến sẽ chạy cục bộ thuật toán đường đi ngắn nhất của Dijkstra để xác định cây đường đi ngắn nhất tới tất cả các mạng con, với chính nó là nút gốc. Chi phí liên kết riêng lẻ do quản trị viên mạng định cấu hình (xem thanh bên, Nguyên tắc và Thực tiễn:

Đang đặt trọng số OSPF). Quản trị viên có thể chọn đặt tất cả chi phí liên kết thành 1, do đó đạt được định tuyến bước nhảy tối thiểu hoặc có thể chọn đặt trọng số liên kết tỷ lệ nghịch với dung lượng liên kết để ngăn cản lưu lượng truy cập sử dụng các liên kết băng thông thấp. OSPF không bắt buộc chính sách về cách đặt trọng số liên kết (đó là công việc của quản trị viên mạng), mà thay vào đó cung cấp các cơ chế (giao thức) để xác định định tuyến đường dẫn có chi phí thấp nhất cho tập hợp trọng số liên kết nhất định.

Với OSPF, bộ định tuyến sẽ phát thông tin định tuyến tới tất cả các bộ định tuyến khác trong hệ thống tự trị, không chỉ tới các bộ định tuyến lân cận. Bộ định tuyến phát thông tin trạng thái liên kết bất cứ khi nào có thay đổi về trạng thái của liên kết (ví dụ: thay đổi về chi phí hoặc thay đổi trạng thái lên/xuống). Nó cũng phát sóng trạng thái của liên kết theo định kỳ (ít nhất 30 phút một lần), ngay cả khi trạng thái của liên kết không thay đổi. RFC 2328 lưu ý rằng "việc cập nhật định kỳ các quảng cáo trạng thái liên kết này sẽ tăng thêm độ mạnh mẽ cho thuật toán trạng thái liên kết". OSPF quảng cáo được chứa trong các tin nhắn OSPF

THIẾT LẬP OSPF TRỌNG LƯỢNG LIÊN KẾT

Cuộc thảo luận của chúng tôi về định tuyến trạng thái liên kết đã ngầm giả định rằng trọng số liên kết được đặt, thuật toán định tuyến như OSPF được chạy và luồng lưu lượng truy cập theo bảng định tuyến được tính toán bởi thuật toán LS. Về mặt nguyên nhân và kết quả, các trọng số liên kết được đưa ra (tức là chúng đến trước) và kết quả (thông qua thuật toán của Dijkstra) trong các đường dẫn định tuyến giúp giảm thiểu chi phí tổng thể. Theo quan điểm này, trọng số liên kết phản ánh chi phí sử dụng liên kết (ví dụ: nếu trọng số liên kết tỷ lệ nghịch với dung lượng thì việc sử dụng liên kết dung lượng cao sẽ có trọng số nhỏ hơn và do đó hấp dẫn hơn từ quan điểm định tuyến) và thuật toán của Dijsktra giúp giảm thiểu chi phí tổng thể.

Trong thực tế, mối quan hệ nhân quả giữa trọng số liên kết và đường định tuyến có thể bị đảo ngược, với việc các nhà khai thác mạng định cấu hình trọng số liên kết để có được các đường dẫn định tuyến đạt được các mục tiêu kỹ thuật lưu lượng nhất định \[Fortz 2000, Fortz 2002\]. Ví dụ: giả sử nhà điều hành mạng ước tính lưu lượng truy cập vào mạng tại mỗi điểm vào và dành cho từng điểm đi. Sau đó, nhà điều hành có thể muốn đưa ra một định tuyến cụ thể cho các luồng đi vào để giảm thiểu việc sử dụng tối đa trên tất cả các liên kết của mạng. Nhưng với thuật toán định tuyến như OSPF, "nút" chính của người vận hành để điều chỉnh việc định tuyến các luồng qua mạng là trọng số liên kết. Vì vậy, để đạt được mục tiêu giảm thiểu việc sử dụng liên kết tối đa, nhà điều hành phải tìm tập hợp các trọng số liên kết đạt được mục tiêu này. Đây là sự đảo ngược mối quan hệ nhân quả---định tuyến mong muốn của các luồng đã được biết và các trọng số liên kết OSPF phải được tìm thấy sao cho thuật toán định tuyến OSPF dẫn đến việc định tuyến các luồng mong muốn này.

NGUYÊN TẮC TRONG THỰC HÀNH

được thực hiện trực tiếp bởi IP, với giao thức lớp trên là 89 cho OSPF. Do đó, giao thức OSPF phải tự triển khai các chức năng như truyền tin nhắn đáng tin cậy và phát sóng trạng thái liên kết. Giao thức OSPF cũng kiểm tra xem các liên kết có đang hoạt động hay không (thông qua tin nhắn HELLO được gửi đến một hàng xóm được đính kèm) và cho phép bộ định tuyến OSPF có được cơ sở dữ liệu về trạng thái liên kết trên toàn mạng của bộ định tuyến lân cận.

Một số tiến bộ được thể hiện trong OSPF bao gồm:

• Bảo vệ. Trao đổi giữa các bộ định tuyến OSPF (ví dụ: cập nhật trạng thái liên kết) có thể được xác thực. Với xác thực, chỉ các bộ định tuyến đáng tin cậy mới có thể tham gia vào giao thức OSPF trong AS, do đó ngăn chặn những kẻ xâm nhập độc hại (hoặc sinh viên mạng lấy kiến ​​thức mới tìm thấy của họ để vui chơi) tiêm thông tin không chính xác vào bảng bộ định tuyến. Theo mặc định, các gói OSPF giữa các bộ định tuyến không được xác thực và có thể bị giả mạo. Hai loại xác thực có thể được cấu hình---đơn giản và MD5 (xem Chương 8 để thảo luận về MD5 và xác thực nói chung). Với xác thực đơn giản, cùng một mật khẩu được cấu hình trên mỗi bộ định tuyến. Khi bộ định tuyến gửi gói OSPF, nó sẽ bao gồm mật khẩu ở dạng văn bản gốc. Rõ ràng, xác thực đơn giản không an toàn lắm. Xác thực MD5 dựa trên các khóa bí mật dùng chung được định cấu hình trong tất cả các bộ định tuyến. Đối với mỗi gói OSPF được gửi đi, bộ định tuyến sẽ tính toán hàm băm MD5 của nội dung của gói OSPF được gắn với khóa bí mật. (Xem phần thảo luận về mã xác thực tin nhắn ở Chương 8.) Sau đó, bộ định tuyến sẽ đưa giá trị băm thu được vào gói OSPF. Bộ định tuyến nhận, sử dụng khóa bí mật được cấu hình sẵn, sẽ tính toán hàm băm MD5 của gói và so sánh nó với giá trị băm mà gói mang theo, từ đó xác minh tính xác thực của gói. Số thứ tự cũng được sử dụng với xác thực MD5 để bảo vệ chống lại các cuộc tấn công lặp lại. • Nhiều đường dẫn có cùng chi phí. Khi nhiều đường dẫn đến đích có cùng chi phí, OSPF cho phép sử dụng nhiều đường dẫn (nghĩa là không cần chọn một đường dẫn duy nhất để mang tất cả lưu lượng truy cập khi tồn tại nhiều đường dẫn có chi phí bằng nhau). • Hỗ trợ tích hợp cho định tuyến unicast và multicast. Multicast OSPF (MOSPF) \[RFC 1584\] cung cấp các phần mở rộng đơn giản cho OSPF để cung cấp khả năng định tuyến multicast. MOSPF sử dụng cơ sở dữ liệu liên kết OSPF hiện có và thêm một loại quảng cáo trạng thái liên kết mới vào cơ chế phát sóng trạng thái liên kết OSPF hiện có. • Hỗ trợ phân cấp trong một AS duy nhất. Hệ thống tự trị OSPF có thể được cấu hình theo thứ bậc thành các khu vực. Mỗi khu vực chạy thuật toán định tuyến trạng thái liên kết OSPF riêng, trong đó mỗi bộ định tuyến trong một khu vực sẽ phát sóng trạng thái liên kết của nó tới tất cả các bộ định tuyến khác trong khu vực đó. Trong mỗi khu vực, một hoặc nhiều bộ định tuyến biên giới khu vực chịu trách nhiệm định tuyến các gói bên ngoài khu vực. Cuối cùng, chính xác một vùng OSPF trong AS được cấu hình làm vùng xương sống. Vai trò chính của vùng đường trục là định tuyến lưu lượng giữa các vùng khác trong AS. Đường trục luôn chứa tất cả các bộ định tuyến biên giới khu vực trong AS và cũng có thể chứa các bộ định tuyến không biên giới. Định tuyến liên khu vực trong AS yêu cầu gói tin phải được ưu tiên

được định tuyến đến bộ định tuyến biên khu vực (định tuyến nội khu vực), sau đó định tuyến qua đường trục đến bộ định tuyến biên khu vực nằm trong khu vực đích và sau đó được định tuyến đến đích cuối cùng.

OSPF là một giao thức tương đối phức tạp và phạm vi đề cập của chúng tôi ở đây nhất thiết phải ngắn gọn; \[Huitema 1998; Moy 1998; RFC 2328\] cung cấp thêm chi tiết.

**5.4 Định tuyến giữa các ISP: BGP**

Chúng ta vừa biết rằng OSPF là một ví dụ về giao thức định tuyến nội bộ AS. Khi định tuyến một gói tin giữa nguồn và đích trong cùng một AS, lộ trình mà gói tin đi theo hoàn toàn được xác định bởi giao thức định tuyến nội bộ AS. Tuy nhiên, để định tuyến một gói qua nhiều AS, chẳng hạn từ điện thoại thông minh ở Timbuktu đến máy chủ trong trung tâm dữ liệu ở Thung lũng Silicon, chúng ta cần một giao thức định tuyến hệ thống liên tự trị. Do giao thức định tuyến giữa các AS liên quan đến sự phối hợp giữa nhiều AS nên các AS giao tiếp phải chạy cùng một giao thức định tuyến giữa các AS. Trên thực tế, trên Internet, tất cả các AS đều chạy cùng một giao thức định tuyến giữa các AS, được gọi là Giao thức cổng biên, thường được gọi là BGP \[RFC 4271; Stewart 1999\].

BGP được cho là giao thức quan trọng nhất trong tất cả các giao thức Internet (đối thủ duy nhất còn lại là giao thức IP mà chúng ta đã nghiên cứu trong Phần 4.3), vì đây là giao thức gắn kết hàng nghìn ISP trên Internet lại với nhau. Như chúng ta sẽ sớm thấy, BGP là một giao thức phi tập trung và không đồng bộ theo hướng định tuyến vectơ khoảng cách được mô tả trong Phần 5.2.2. Mặc dù BGP là một giao thức phức tạp và đầy thách thức nhưng để hiểu Internet ở mức độ sâu hơn, chúng ta cần làm quen với nền tảng và hoạt động của nó. Thời gian chúng ta dành cho việc học BGP sẽ rất đáng nỗ lực.

**5.4.1 Vai trò của BGP**

Để hiểu trách nhiệm của BGP, hãy xem xét một AS và một bộ định tuyến tùy ý trong AS đó. Hãy nhớ lại rằng mọi bộ định tuyến đều có một bảng chuyển tiếp, bảng này đóng vai trò trung tâm trong quá trình chuyển tiếp các gói đến tới các liên kết bộ định tuyến gửi đi. Như chúng ta đã biết, đối với các đích đến nằm trong cùng một AS, các mục trong bảng chuyển tiếp của bộ định tuyến được xác định bởi giao thức định tuyến nội bộ AS của AS. Nhưng còn những điểm đến nằm ngoài AS thì sao? Đây chính xác là nơi BGP đến giải cứu.

Trong BGP, các gói không được định tuyến đến một địa chỉ đích cụ thể mà thay vào đó là các tiền tố CIDRized, với mỗi tiền tố đại diện cho một mạng con hoặc một tập hợp các mạng con.

Kết nối Internet lại với nhau: BGP

VideoLưu ý

Trong thế giới BGP, đích đến có thể có dạng 138.16.68/22, trong ví dụ này bao gồm 1.024 địa chỉ IP. Do đó, bảng chuyển tiếp của bộ định tuyến sẽ có các mục có dạng (x, I), trong đó x là tiền tố (chẳng hạn như 138.16.68/22) và I là số giao diện cho một trong các giao diện của bộ định tuyến.

Là một giao thức định tuyến giữa các AS, BGP cung cấp cho mỗi bộ định tuyến một phương tiện để:

1\. Lấy thông tin về khả năng tiếp cận tiền tố từ các AS lân cận. Đặc biệt,

BGP cho phép mỗi mạng con quảng cáo sự tồn tại của nó với phần còn lại của Internet. Một mạng con hét lên: "Tôi tồn tại và tôi ở đây" và BGP đảm bảo rằng tất cả các bộ định tuyến trên Internet đều biết về mạng con này. Nếu không có BGP, mỗi mạng con sẽ là một hòn đảo biệt lập---đơn độc, không được biết đến và không thể truy cập được bởi phần còn lại của Internet.

2\. Xác định các tuyến đường "tốt nhất" đến các tiền tố. Một bộ định tuyến có thể tìm hiểu về hai hoặc

nhiều tuyến đường khác nhau tới một tiền tố cụ thể. Để xác định tuyến đường tốt nhất, bộ định tuyến sẽ chạy cục bộ quy trình chọn tuyến BGP (sử dụng thông tin khả năng tiếp cận tiền tố mà nó thu được qua các bộ định tuyến lân cận). Tuyến đường tốt nhất sẽ được xác định dựa trên chính sách cũng như thông tin về khả năng tiếp cận.

Bây giờ chúng ta hãy đi sâu vào cách BGP thực hiện hai nhiệm vụ này.

**5.4.2 Quảng cáo BGP Thông tin tuyến đường**

Hãy xem xét mạng được hiển thị trong Hình 5.8. Như chúng ta có thể thấy, mạng đơn giản này có ba hệ thống tự trị: AS1, AS2 và AS3. Như được hiển thị, AS3 bao gồm một mạng con có tiền tố x. Đối với mỗi AS, mỗi bộ định tuyến là bộ định tuyến cổng hoặc bộ định tuyến nội bộ. Bộ định tuyến cổng là bộ định tuyến ở rìa của AS kết nối trực tiếp với một hoặc nhiều bộ định tuyến trong các AS khác. Một bộ định tuyến nội bộ chỉ kết nối với các máy chủ và bộ định tuyến trong AS của chính nó. Ví dụ, trong AS1, bộ định tuyến 1c là bộ định tuyến cổng; bộ định tuyến 1a, 1b và 1d là bộ định tuyến nội bộ. Hãy xem xét nhiệm vụ quảng cáo thông tin khả năng tiếp cận của tiền tố x tới tất cả các bộ định tuyến được hiển thị trong Hình 5.8. Ở mức độ cao, điều này rất đơn giản. Đầu tiên, AS3 gửi tin nhắn BGP tới AS2, nói rằng x tồn tại và nằm trong AS3; hãy biểu thị thông báo này là "AS3 x". Sau đó AS2 gửi tin nhắn BGP đến AS1, nói rằng x tồn tại và bạn có thể truy cập x bằng cách trước tiên đi qua AS2 rồi đến AS3; hãy biểu thị thông báo đó là "AS2 AS3 x". Theo cách này, mỗi hệ thống tự trị sẽ không chỉ tìm hiểu về sự tồn tại của x mà còn tìm hiểu về đường đi của các hệ thống tự trị dẫn đến x.

Mặc dù cuộc thảo luận trong đoạn văn trên về quảng cáo thông tin về khả năng tiếp cận BGP sẽ hiểu rõ ý tưởng chung, nhưng nó không chính xác theo nghĩa là các hệ thống tự trị không thực sự gửi tin nhắn cho nhau mà thay vào đó các bộ định tuyến sẽ gửi tin nhắn cho nhau. Để hiểu điều này, bây giờ chúng ta hãy xem lại ví dụ trong Hình 5.8. Trong BGP,

các cặp bộ định tuyến trao đổi thông tin định tuyến qua các kết nối TCP bán cố định bằng cổng 179. Mỗi kết nối TCP như vậy, cùng với tất cả các tin nhắn BGP được gửi qua kết nối, được gọi là kết nối BGP. Hơn nữa, kết nối BGP trải rộng trên hai AS được gọi là kết nối BGP (eBGP) bên ngoài và phiên BGP giữa các bộ định tuyến trong cùng một AS được gọi là kết nối BGP (iBGP) nội bộ. Ví dụ về kết nối BGP cho mạng trong Hình 5.8 được hiển thị trong Hình 5.9. Thông thường có một kết nối eBGP cho mỗi liên kết kết nối trực tiếp các bộ định tuyến cổng trong các AS khác nhau; do đó, trong Hình 5.9, có một kết nối eBGP giữa các bộ định tuyến cổng 1c và 2a và một kết nối eBGP giữa các bộ định tuyến cổng 2c và 3a.

Ngoài ra còn có các kết nối iBGP giữa các bộ định tuyến trong mỗi AS. Cụ thể, Hình 5.9 hiển thị cấu hình chung của một kết nối BGP cho mỗi cặp bộ định tuyến bên trong một AS, tạo ra một mạng lưới các kết nối TCP trong mỗi AS. Trong Hình 5.9, các kết nối eBGP được hiển thị bằng các dấu gạch ngang dài; các kết nối iBGP được hiển thị bằng dấu gạch ngang ngắn. Lưu ý rằng các kết nối iBGP không phải lúc nào cũng tương ứng với các liên kết vật lý.

Để truyền bá thông tin về khả năng tiếp cận, cả phiên iBGP và eBGP đều được sử dụng. Hãy xem xét lại việc quảng cáo thông tin khả năng tiếp cận của tiền tố x tới tất cả các bộ định tuyến trong AS1 và AS2. Trong quá trình này, cổng bộ định tuyến 3a trước tiên sẽ gửi tin nhắn eBGP "AS3 x" đến cổng bộ định tuyến 2c. Sau đó, bộ định tuyến cổng 2c sẽ gửi tin nhắn iBGP "AS3 x" tới tất cả các bộ định tuyến khác trong AS2, bao gồm cả bộ định tuyến cổng 2a. Sau đó, bộ định tuyến cổng 2a sẽ gửi tin nhắn eBGP "AS2 AS3 x" đến bộ định tuyến cổng 1c. Cuối cùng, bộ định tuyến cổng 1c sử dụng iBGP để gửi

2b

2 ngày

2a

2c

AS2

1b

1 ngày

1a

1c

AS1

3b

3d

3a

3c

AS3

X

*Hình 5.8 ♦ Mạng có ba hệ thống tự trị. AS3 bao gồm một*

mạng con có tiền tố x

nhắn "AS2 AS3 x" tới tất cả các bộ định tuyến trong AS1. Sau khi quá trình này hoàn tất, mỗi bộ định tuyến trong AS1 và AS2 nhận biết được sự tồn tại của x và cũng nhận biết được đường dẫn AS dẫn đến x.

Tất nhiên, trong một mạng thực, từ một bộ định tuyến nhất định có thể có nhiều đường dẫn khác nhau đến một đích nhất định, mỗi đường đi qua một chuỗi AS khác nhau. Ví dụ, hãy xem xét mạng trong Hình 5.10, là mạng ban đầu trong Hình 5.8, với một liên kết vật lý bổ sung từ bộ định tuyến 1d đến bộ định tuyến 3d. Trong trường hợp này, có hai đường dẫn từ AS1 đến x: đường dẫn "AS2 AS3 x" qua bộ định tuyến 1c; và đường dẫn mới "AS3 x" qua bộ định tuyến 1d.

**5.4.3 Xác định tuyến đường tốt nhất**

Như chúng ta vừa học, có thể có nhiều đường dẫn từ một bộ định tuyến nhất định đến mạng con đích. Trên thực tế, trên Internet, các bộ định tuyến thường nhận được thông tin về khả năng tiếp cận về hàng chục đường dẫn khác nhau. Làm thế nào để bộ định tuyến chọn trong số các đường dẫn này (và sau đó định cấu hình bảng chuyển tiếp cho phù hợp)?

Trước khi giải quyết câu hỏi quan trọng này, chúng tôi cần giới thiệu thêm một chút về thuật ngữ BGP. Khi bộ định tuyến quảng cáo tiền tố qua kết nối BGP, nó sẽ bao gồm tiền tố một số thuộc tính BGP. Trong biệt ngữ BGP, tiền tố cùng với các thuộc tính của nó được gọi là tuyến đường. Hai trong số các thuộc tính quan trọng hơn là AS-PATH và NEXT-HOP. Thuộc tính AS-PATH chứa danh sách các AS mà qua đó

eBGP

Chìa khóa:

iBGP

2b

2 ngày

2a

2c

AS2

1b

1 ngày

1a

1c

AS1

3b

3d

3a

3c

AS3

X

*Hình 5.9 ♦ Kết nối eBGP và iBGP*

quảng cáo đã trôi qua, như chúng ta đã thấy trong các ví dụ ở trên. Để tạo ra giá trị ASPATH, khi tiền tố được truyền tới AS, AS sẽ thêm ASN của nó vào danh sách hiện có trong AS-PATH. Ví dụ, trong Hình 5.10, có hai tuyến từ AS1 đến mạng con x: một tuyến sử dụng AS-PATH "AS2 AS3"; và một cái khác sử dụng AS-PATH "A3". Bộ định tuyến BGP cũng sử dụng thuộc tính AS-PATH để phát hiện và ngăn chặn các quảng cáo lặp lại; cụ thể, nếu một bộ định tuyến thấy rằng AS của chính nó có trong danh sách đường dẫn, nó sẽ từ chối quảng cáo.

Cung cấp liên kết quan trọng giữa các giao thức định tuyến giữa AS và nội bộ AS, thuộc tính NEXT-HOP có cách sử dụng tinh tế nhưng quan trọng. NEXT-HOP là địa chỉ IP của giao diện bộ định tuyến bắt đầu AS-PATH. Để hiểu rõ hơn về thuộc tính này, hãy tham khảo lại Hình 5.10. Như được chỉ ra trong Hình 5.10, thuộc tính NEXTHOP cho tuyến đường "AS2 AS3 x" từ AS1 đến x đi qua AS2 là địa chỉ IP của giao diện bên trái trên bộ định tuyến 2a. Thuộc tính NEXT-HOP cho tuyến đường "AS3 x" từ AS1 đến x bỏ qua AS2 là địa chỉ IP của giao diện ngoài cùng bên trái của bộ định tuyến 3d. Tóm lại, trong ví dụ về đồ chơi này, mỗi bộ định tuyến trong AS1 nhận biết được hai tuyến BGP tới tiền tố x:

IP địa chỉ giao diện ngoài cùng bên trái của bộ định tuyến 2a; AS2 AS3; x IP địa chỉ giao diện ngoài cùng bên trái của bộ định tuyến 3d; AS3; x

Ở đây, mỗi tuyến BGP được viết dưới dạng danh sách có ba thành phần: NEXT-HOP; ASPATH; tiền tố đích. Trong thực tế, tuyến đường BGP bao gồm các thuộc tính bổ sung mà hiện tại chúng tôi sẽ bỏ qua. Lưu ý rằng thuộc tính NEXT-HOP là IP

TIẾP THEO-HOP

TIẾP THEO-HOP

2b

2 ngày

2a

2c

AS2

1b

1 ngày

1a

1c

AS1

3b

3d

3a

3c

AS3

X

*Hình 5.10 ♦ Mạng được tăng cường liên kết ngang hàng giữa AS1*

và AS3

địa chỉ của bộ định tuyến không thuộc AS1; tuy nhiên, mạng con chứa địa chỉ IP này sẽ gắn trực tiếp vào AS1.

Định tuyến khoai tây nóng

Bây giờ chúng ta cuối cùng đã có thể nói về thuật toán định tuyến BGP một cách chính xác. Chúng ta sẽ bắt đầu với một trong những thuật toán định tuyến đơn giản nhất, đó là định tuyến khoai tây nóng.

Hãy xem xét bộ định tuyến 1b trong mạng trong Hình 5.10. Như vừa mô tả, bộ định tuyến này sẽ tìm hiểu về hai tuyến BGP có thể đến tiền tố x. Trong định tuyến khoai tây nóng, tuyến được chọn (trong số tất cả các tuyến có thể) là tuyến có chi phí thấp nhất đối với bộ định tuyến NEXTHOP bắt đầu tuyến đó. Trong ví dụ này, bộ định tuyến 1b sẽ tham khảo thông tin định tuyến trong AS của nó để tìm đường dẫn trong AS có chi phí thấp nhất tới bộ định tuyến NEXT-HOP 2a và đường dẫn trong AS có chi phí thấp nhất tới bộ định tuyến NEXT-HOP 3d, sau đó chọn tuyến có đường dẫn nhỏ nhất trong số các đường dẫn có chi phí thấp nhất này. Ví dụ: giả sử chi phí đó được định nghĩa là số lượng liên kết đi qua. Khi đó chi phí thấp nhất từ ​​bộ định tuyến 1b đến bộ định tuyến 2a là 2, chi phí thấp nhất từ ​​bộ định tuyến 1b đến bộ định tuyến 2d là 3 và do đó bộ định tuyến 2a sẽ được chọn. Router 1b sau đó sẽ tham khảo bảng chuyển tiếp của nó (được định cấu hình bằng thuật toán nội bộ AS) và tìm giao diện I nằm trên đường dẫn có chi phí thấp nhất tới bộ định tuyến 2a. Sau đó nó thêm (x, I) vào bảng chuyển tiếp của nó.

Các bước để thêm tiền tố external-AS vào bảng chuyển tiếp của bộ định tuyến để định tuyến khoai tây nóng được tóm tắt trong Hình 5.11. Điều quan trọng cần lưu ý là khi thêm tiền tố bên ngoài AS vào bảng chuyển tiếp, cả giao thức định tuyến giữa các AS (BGP) và giao thức định tuyến trong AS (ví dụ: OSPF) đều được sử dụng.

Ý tưởng đằng sau việc định tuyến khoai tây nóng là để bộ định tuyến 1b đưa các gói ra khỏi AS của nó càng nhanh càng tốt (cụ thể hơn là với chi phí thấp nhất có thể) mà không phải lo lắng về chi phí của các phần còn lại của đường dẫn bên ngoài AS của nó tới đích. Với tên gọi "định tuyến khoai tây nóng", một gói tương tự như một củ khoai tây nóng đang cháy trên tay bạn. Vì trời đang nóng nên bạn muốn chuyển nó cho người khác (AS khác) càng nhanh càng tốt. Như vậy là định tuyến khoai tây nóng

Tìm hiểu từ giao thức inter-AS mạng con đó

x có thể truy cập được thông qua nhiều cổng.

Sử dụng thông tin định tuyến từ

giao thức nội AS để

xác định chi phí của

đường đi có chi phí thấp nhất tới mỗi cổng.

Định tuyến khoai nóng: Chọn cổng

đó có chi phí nhỏ nhất.

Xác định từ bảng chuyển tiếp

giao diện I dẫn đến cổng có chi phí thấp nhất.

Nhập (x,I) vào bảng chuyển tiếp.

*Hình 5.11 ♦ Các bước thêm đích bên ngoài AS vào địa chỉ của bộ định tuyến*

bảng chuyển tiếp

một thuật toán ích kỷ---nó cố gắng giảm chi phí trong AS của chính nó trong khi bỏ qua các thành phần khác của chi phí đầu cuối bên ngoài AS của nó. Lưu ý rằng với định tuyến khoai tây nóng, hai bộ định tuyến trong cùng một AS có thể chọn hai đường dẫn AS khác nhau đến cùng một tiền tố. Ví dụ: chúng ta vừa thấy rằng bộ định tuyến 1b sẽ gửi các gói qua AS2 để đến x. Tuy nhiên, bộ định tuyến 1d sẽ bỏ qua AS2 và gửi các gói trực tiếp đến AS3 để tiếp cận x.

Thuật toán chọn tuyến đường

Trong thực tế, BGP sử dụng thuật toán phức tạp hơn định tuyến khoai tây nóng nhưng vẫn kết hợp định tuyến khoai tây nóng. Đối với bất kỳ tiền tố đích cụ thể nào, đầu vào của thuật toán chọn tuyến của BGP là tập hợp tất cả các tuyến đến tiền tố đó đã được bộ định tuyến học và chấp nhận. Nếu chỉ có một tuyến đường như vậy thì rõ ràng BGP sẽ chọn tuyến đường đó. Nếu có hai hoặc nhiều tuyến đường đến cùng một tiền tố thì BGP sẽ gọi tuần tự các quy tắc loại bỏ sau cho đến khi còn lại một tuyến đường:

1\. Một tuyến đường được gán một giá trị ưu tiên cục bộ như một trong các thuộc tính của nó (ngoài ra

thuộc tính AS-PATH và NEXT-HOP). Ưu tiên cục bộ của tuyến đường có thể được thiết lập bởi bộ định tuyến hoặc có thể được học từ một bộ định tuyến khác trong cùng một AS. Giá trị của thuộc tính ưu tiên cục bộ là quyết định chính sách hoàn toàn phụ thuộc vào quản trị viên mạng của AS. (Chúng tôi sẽ sớm thảo luận chi tiết về các vấn đề chính sách BGP.) Các tuyến đường có giá trị ưu tiên cục bộ cao nhất sẽ được chọn. 2. Từ các tuyến đường còn lại (tất cả đều có cùng giá trị ưu tiên cục bộ cao nhất),

tuyến đường có AS-PATH ngắn nhất sẽ được chọn. Nếu quy tắc này là quy tắc duy nhất để chọn tuyến thì BGP sẽ sử dụng thuật toán DV để xác định đường dẫn, trong đó thước đo khoảng cách sử dụng số bước nhảy AS thay vì số bước nhảy của bộ định tuyến. 3. Từ các tuyến đường còn lại (tất cả đều có cùng giá trị ưu tiên cục bộ cao nhất và

cùng độ dài AS-PATH), định tuyến khoai tây nóng được sử dụng, nghĩa là tuyến có bộ định tuyến NEXT-HOP gần nhất sẽ được chọn. 4. Nếu vẫn còn nhiều tuyến đường, bộ định tuyến sẽ sử dụng mã định danh BGP để chọn tuyến đường

tuyến đường; xem \[Stewart 1999\].

Để làm ví dụ, hãy xem xét lại bộ định tuyến 1b trong Hình 5.10. Hãy nhớ lại rằng có chính xác hai tuyến BGP tới tiền tố x, một tuyến đi qua AS2 và một tuyến đi qua AS2. Ngoài ra, hãy nhớ lại rằng nếu sử dụng định tuyến khoai tây nóng thì BGP sẽ định tuyến các gói qua AS2 tới tiền tố x. Nhưng trong thuật toán chọn tuyến đường ở trên, quy tắc 2 được áp dụng trước quy tắc 3, khiến BGP chọn tuyến đường bỏ qua AS2, vì tuyến đường đó có AS PATH ngắn hơn. Vì vậy, chúng tôi thấy rằng với thuật toán chọn tuyến đường ở trên, BGP không còn là một thuật toán ích kỷ nữa---trước tiên, nó tìm kiếm các tuyến đường có đường dẫn AS ngắn (do đó có khả năng giảm độ trễ từ đầu đến cuối).

Như đã lưu ý ở trên, BGP là tiêu chuẩn thực tế cho việc định tuyến giữa các AS cho Internet. Để xem nội dung của các bảng định tuyến BGP (lớn!) khác nhau được trích xuất từ ​​​​

bộ định tuyến trong ISP cấp 1, xem http://www.routeviews.org. BGP bảng định tuyến thường chứa hơn nửa triệu tuyến đường (nghĩa là tiền tố và thuộc tính tương ứng). Thống kê về kích thước và đặc điểm của bảng định tuyến BGP được trình bày trong \[Huston 2019b\].

**5.4.4 IP-Anycast**

Ngoài việc là giao thức định tuyến giữa các AS của Internet, BGP còn thường được sử dụng để triển khai dịch vụ IP-anycast \[RFC 1546, RFC 7094\], thường được sử dụng trong DNS. Để thúc đẩy IP-anycast, hãy cân nhắc rằng trong nhiều ứng dụng, chúng tôi quan tâm đến việc (1) sao chép cùng một nội dung trên các máy chủ khác nhau ở nhiều vị trí địa lý phân tán khác nhau và (2) yêu cầu mỗi người dùng truy cập nội dung từ máy chủ gần nhất. Ví dụ: CDN có thể sao chép video và các đối tượng khác trên máy chủ ở các quốc gia khác nhau. Tương tự, hệ thống DNS có thể sao chép các bản ghi DNS trên các máy chủ DNS trên khắp thế giới. Khi người dùng muốn truy cập nội dung được sao chép này, điều mong muốn là hướng người dùng đến máy chủ "gần nhất" có nội dung được sao chép. Thuật toán chọn tuyến đường của BGP cung cấp cơ chế tự nhiên và dễ dàng để thực hiện việc đó.

Để làm cho cuộc thảo luận của chúng ta cụ thể hơn, hãy mô tả cách CDN có thể sử dụng IPanycast. Như được hiển thị trong Hình 5.12, trong giai đoạn cấu hình IP-anycast, công ty CDN chỉ định cùng một địa chỉ IP cho mỗi máy chủ của mình và sử dụng BGP tiêu chuẩn để quảng cáo địa chỉ IP này từ mỗi máy chủ. Khi bộ định tuyến BGP nhận được nhiều quảng cáo tuyến đường cho địa chỉ IP này, nó sẽ coi những quảng cáo này là cung cấp các đường dẫn khác nhau đến cùng một vị trí thực tế (trong khi trên thực tế, các quảng cáo dành cho các đường dẫn khác nhau đến các vị trí thực tế khác nhau). Khi định cấu hình bảng định tuyến, mỗi bộ định tuyến sẽ sử dụng cục bộ thuật toán chọn tuyến BGP để chọn tuyến "tốt nhất" (ví dụ: gần nhất, được xác định bằng số lượng AS-hop) tới địa chỉ IP đó. Ví dụ: nếu một tuyến BGP (tương ứng với một vị trí) chỉ cách bộ định tuyến một bước nhảy AS và tất cả các tuyến BGP khác (tương ứng với các vị trí khác) cách xa hai bước nhảy AS trở lên, thì bộ định tuyến BGP sẽ chọn định tuyến các gói đến vị trí cách đó một bước nhảy. Sau giai đoạn quảng cáo địa chỉ BGP ban đầu này, CDN có thể thực hiện công việc chính là phân phối nội dung. Khi khách hàng yêu cầu video, CDN sẽ trả về cho khách hàng địa chỉ IP chung được sử dụng bởi các máy chủ phân tán về mặt địa lý, bất kể khách hàng ở đâu. Khi máy khách gửi yêu cầu đến địa chỉ IP đó, bộ định tuyến Internet sẽ chuyển tiếp gói yêu cầu đến máy chủ "gần nhất", như được xác định bởi thuật toán chọn tuyến BGP.

Mặc dù ví dụ CDN ở trên minh họa rõ ràng cách có thể sử dụng IP-anycast, nhưng trên thực tế, CDN thường chọn không sử dụng IP-anycast vì các thay đổi định tuyến BGP có thể dẫn đến các gói khác nhau của cùng một kết nối TCP đến các phiên bản khác nhau của máy chủ Web. Nhưng IP-anycast được hệ thống DNS sử dụng rộng rãi để hướng các truy vấn DNS tới máy chủ DNS gốc gần nhất. Nhớ lại Phần 2.4, hiện tại có 13 địa chỉ IP cho máy chủ DNS gốc. Nhưng tương ứng với mỗi địa chỉ này, có nhiều máy chủ gốc DNS, với một số địa chỉ này có

hơn 100 DNS máy chủ gốc nằm rải rác khắp nơi trên thế giới. Khi một truy vấn DNS được gửi đến một trong 13 địa chỉ IP này, IP Anycast được sử dụng để định tuyến truy vấn đến máy chủ gốc DNS gần nhất chịu trách nhiệm về địa chỉ đó. \[Li 2018\] trình bày các phép đo gần đây minh họa bất kỳ truyền hình Internet nào, việc sử dụng, hiệu suất và những thách thức.

**5.4.5 Chính sách định tuyến**

Khi bộ định tuyến chọn tuyến đến đích, chính sách định tuyến AS có thể vượt qua tất cả các cân nhắc khác, chẳng hạn như đường dẫn AS ngắn nhất hoặc định tuyến khoai tây nóng. Thật vậy, trong thuật toán chọn tuyến, các tuyến đầu tiên được chọn theo thuộc tính local-preference, giá trị của nó được cố định bởi chính sách của AS cục bộ.

Hãy minh họa một số khái niệm cơ bản về chính sách định tuyến BGP bằng một ví dụ đơn giản. Hình 5.13 cho thấy sáu hệ thống tự trị được kết nối với nhau: A, B, C, W, X và Y. Điều quan trọng cần lưu ý là A, B, C, W, X và Y là AS, không phải bộ định tuyến. Hãy

AS1

AS3 3b

3c

3a

1a

1c

1b

1 ngày

AS2

AS4

2a

2c

4a 4c

4b

Quảng cáo 212.21.21.21

Máy chủ CDN B

Máy chủ CDN A

Quảng cáo 212.21.21.21

Nhận BGP quảng cáo cho 212.21.21.21 từ AS1 và từ AS4. Chuyển tiếp về phía Máy chủ B vì nó ở gần hơn.

2b

*Hình 5.12 ♦ Sử dụng IP-anycast để đưa người dùng đến máy chủ CDN gần nhất*

giả sử rằng các hệ thống tự trị W, X và Y là các ISP truy cập và A, B và C là các mạng cung cấp đường trục. Chúng tôi cũng giả định rằng A, B và C trực tiếp gửi lưu lượng truy cập cho nhau và cung cấp thông tin BGP đầy đủ cho mạng khách hàng của họ. Tất cả lưu lượng truy cập vào mạng truy cập ISP phải được dành cho mạng đó và tất cả lưu lượng truy cập rời khỏi mạng truy cập ISP phải có nguồn gốc từ mạng đó. W và Y rõ ràng là các ISP truy cập. X là ISP truy cập nhiều nhà, vì nó được kết nối với phần còn lại của mạng thông qua hai nhà cung cấp khác nhau (một tình huống ngày càng trở nên phổ biến trong thực tế). Tuy nhiên, giống như W và Y, bản thân X phải là nguồn/đích của tất cả lưu lượng đi/vào X. Nhưng hành vi mạng sơ khai này sẽ được triển khai và thực thi như thế nào? Làm cách nào để ngăn chặn X chuyển tiếp lưu lượng giữa B và C? Điều này có thể dễ dàng thực hiện được bằng cách kiểm soát cách thức các tuyến đường BGP được quảng cáo. Đặc biệt, X sẽ hoạt động như một mạng ISP truy cập nếu nó quảng cáo (với các láng giềng B và C) rằng nó không có đường dẫn đến bất kỳ đích nào khác ngoại trừ chính nó. Nghĩa là, mặc dù X có thể biết một đường dẫn, chẳng hạn như XCY, đến mạng Y, nhưng nó sẽ không quảng cáo đường dẫn này đến B. Vì B không biết rằng X có đường dẫn đến Y, nên B sẽ không bao giờ chuyển tiếp lưu lượng đến Y (hoặc C) qua X. Ví dụ đơn giản này minh họa cách sử dụng chính sách quảng cáo tuyến đường chọn lọc để triển khai các mối quan hệ định tuyến khách hàng/nhà cung cấp.

Tiếp theo chúng ta hãy tập trung vào mạng của nhà cung cấp, chẳng hạn như AS B. Giả sử B đã biết (từ A) rằng A có đường dẫn AW đến WB. Do đó, B có thể cài đặt tuyến đường AW vào cơ sở thông tin định tuyến của nó. Rõ ràng, B cũng muốn quảng cáo đường dẫn BAW tới khách hàng của mình, X, để X biết rằng nó có thể định tuyến đến W qua B. Nhưng B có nên quảng cáo đường dẫn BAW đến C không? Nếu làm như vậy thì C có thể định tuyến lưu lượng truy cập đến W thông qua BAW. Nếu A, B và C đều là nhà cung cấp đường trục thì B có thể cảm thấy đúng rằng họ không cần phải gánh gánh nặng (và chi phí!) khi vận chuyển lưu lượng chuyển tuyến giữa A và C. B có thể cảm thấy đúng rằng công việc của A và C (và chi phí!) là đảm bảo rằng C có thể định tuyến đến/từ khách hàng của A thông qua kết nối trực tiếp giữa A và C. Hiện tại không có tiêu chuẩn chính thức nào chi phối cách các ISP đường trục định tuyến giữa họ. Tuy nhiên, một nguyên tắc chung mà các ISP thương mại tuân theo là mọi lưu lượng truy cập đi qua mạng đường trục của ISP đều phải có nguồn hoặc đích (hoặc cả hai) trong mạng là khách hàng của ISP đó; nếu không thì lưu lượng truy cập sẽ được sử dụng miễn phí trên mạng của ISP. Các thỏa thuận ngang hàng cá nhân (điều đó sẽ chi phối các câu hỏi như

A W

X

Y

B

Chìa khóa:

Mạng lưới nhà cung cấp

Mạng lưới khách hàng C

*Hình 5.13 ♦ Kịch bản chính sách BGP đơn giản*

như đã nêu ở trên) thường được đàm phán giữa các cặp ISP và thường được bảo mật; \[Huston 1999a; Huston 2012\] cung cấp một cuộc thảo luận thú vị về các thỏa thuận ngang hàng. Để biết mô tả chi tiết về cách chính sách định tuyến phản ánh mối quan hệ thương mại giữa các ISP, xem \[Gao 2001; Dmitiropoulos 2007\]. Để thảo luận về các chính sách định tuyến BGP từ quan điểm của ISP, hãy xem \[Caesar 2005b\].

TẠI SAO CÓ CÁC GIAO THỨC ĐỊNH TUYẾN INTER-AS VÀ INTRA-AS KHÁC NHAU?

Bây giờ, sau khi đã nghiên cứu chi tiết về các giao thức định tuyến giữa các AS và trong nội bộ AS cụ thể được triển khai trên Internet ngày nay, hãy kết luận bằng cách xem xét có lẽ câu hỏi cơ bản nhất mà chúng ta có thể hỏi về các giao thức này ngay từ đầu (hy vọng rằng bạn đã thắc mắc điều này từ lâu và không bị mất rừng vì cây!): Tại sao các giao thức định tuyến giữa các AS và nội bộ AS khác nhau được sử dụng?

Câu trả lời cho câu hỏi này nằm ở trọng tâm của sự khác biệt giữa mục tiêu định tuyến trong AS và giữa các AS:

• Chính sách. Trong số các AS, vấn đề chính sách chiếm ưu thế. Điều quan trọng là lưu lượng bắt nguồn từ một AS nhất định không thể đi qua một AS cụ thể khác. Tương tự, một AS nhất định có thể muốn kiểm soát lưu lượng chuyển tuyến mà nó mang theo giữa các AS khác. Chúng tôi đã thấy rằng BGP mang các thuộc tính đường dẫn và cung cấp khả năng phân phối thông tin định tuyến có kiểm soát để có thể đưa ra các quyết định định tuyến dựa trên chính sách như vậy. Trong một AS, trên danh nghĩa mọi thứ đều nằm dưới sự kiểm soát hành chính giống nhau và do đó các vấn đề chính sách đóng vai trò ít quan trọng hơn trong việc lựa chọn các tuyến đường trong AS. • Tỉ lệ. Khả năng của thuật toán định tuyến và cấu trúc dữ liệu của nó có thể mở rộng quy mô để xử lý việc định tuyến đến/giữa số lượng lớn mạng là một vấn đề quan trọng trong định tuyến giữa các AS. Trong AS, khả năng mở rộng ít được quan tâm hơn. Thứ nhất, nếu một ISP trở nên quá lớn thì luôn có thể chia nó thành hai AS và thực hiện định tuyến giữa các AS giữa hai AS mới. (Hãy nhớ lại rằng OSPF cho phép xây dựng hệ thống phân cấp như vậy bằng cách chia AS thành các khu vực.) • Hiệu suất. Bởi vì định tuyến giữa các AS thiên về chính sách nên chất lượng (ví dụ: hiệu suất) của các tuyến được sử dụng thường là mối quan tâm thứ yếu (nghĩa là tuyến đường dài hơn hoặc tốn kém hơn đáp ứng các tiêu chí chính sách nhất định có thể được thực hiện trên tuyến đường ngắn hơn nhưng không đáp ứng tiêu chí đó). Thật vậy, chúng ta thấy rằng trong số các AS, thậm chí không có khái niệm về chi phí (ngoài số bước nhảy AS) liên quan đến các tuyến đường. Tuy nhiên, trong một AS đơn lẻ, những mối quan tâm về chính sách như vậy ít quan trọng hơn, cho phép việc định tuyến tập trung nhiều hơn vào mức hiệu suất được thực hiện trên một tuyến đường.

NGUYÊN TẮC TRONG THỰC HÀNH

Điều này hoàn thành phần giới thiệu ngắn gọn của chúng tôi về BGP. Hiểu BGP rất quan trọng vì nó đóng vai trò trung tâm trên Internet. Chúng tôi khuyến khích bạn xem tài liệu tham khảo \[Stewart 1999; Huston 2019a; Labovitz 1997; Halabi 2000; Huitema 1998; Cao 2001; Feamster 2004; Caesar 2005b; Li 2007\] để tìm hiểu thêm về BGP.

**5.4.6 Ghép các mảnh lại với nhau: Có được sự hiện diện trên Internet**

Mặc dù tiểu mục này không nói về BGP nhưng nó tập hợp nhiều giao thức và khái niệm mà chúng ta đã thấy cho đến nay, bao gồm địa chỉ IP, DNS và BGP.

Giả sử bạn vừa tạo một công ty nhỏ có một số máy chủ, bao gồm một máy chủ Web công cộng mô tả các sản phẩm và dịch vụ của công ty bạn, một máy chủ thư mà từ đó nhân viên của bạn nhận được các e-mail của họ và một máy chủ DNS. Đương nhiên, bạn muốn cả thế giới có thể truy cập trang web của mình để tìm hiểu về các sản phẩm và dịch vụ thú vị của bạn. Hơn nữa, bạn muốn nhân viên của mình có thể gửi và nhận e-mail đến các khách hàng tiềm năng trên toàn thế giới.

Để đáp ứng những mục tiêu này, trước tiên bạn cần có được kết nối Internet, việc này được thực hiện bằng cách ký hợp đồng và kết nối với một ISP địa phương. Công ty của bạn sẽ có một bộ định tuyến cổng, bộ định tuyến này sẽ được kết nối với bộ định tuyến trong ISP địa phương của bạn. Kết nối này có thể là kết nối DSL thông qua cơ sở hạ tầng điện thoại hiện có, đường dây thuê riêng tới bộ định tuyến của ISP hoặc một trong nhiều giải pháp truy cập khác được mô tả trong Chương 1. ISP cục bộ của bạn cũng sẽ cung cấp cho bạn dải địa chỉ IP, ví dụ: dải địa chỉ /24 bao gồm 256 địa chỉ. Khi bạn có kết nối vật lý và phạm vi địa chỉ IP của mình, bạn sẽ chỉ định một trong các địa chỉ IP (trong phạm vi địa chỉ của bạn) cho máy chủ Web, một cho máy chủ thư của bạn, một cho máy chủ DNS, một cho bộ định tuyến cổng và các địa chỉ IP khác cho các máy chủ và thiết bị mạng khác trong mạng của công ty bạn.

Ngoài việc ký hợp đồng với ISP, bạn cũng cần phải ký hợp đồng với nhà đăng ký Internet để có được tên miền cho công ty của mình, như được mô tả trong Chương 2. Ví dụ: nếu tên công ty của bạn là Xanadu Inc., thì đương nhiên bạn sẽ cố gắng có được tên miền xanadu.com. Công ty của bạn cũng phải hiện diện trong hệ thống DNS. Cụ thể, vì người ngoài sẽ muốn liên hệ với máy chủ DNS của bạn để lấy địa chỉ IP máy chủ của bạn, nên bạn cũng cần cung cấp cho nhà đăng ký địa chỉ IP của máy chủ DNS của bạn. Sau đó, nhà đăng ký của bạn sẽ đặt một mục nhập cho máy chủ DNS của bạn (tên miền và địa chỉ IP tương ứng) trong các máy chủ tên miền cấp cao nhất .com, như được mô tả trong Chương 2. Sau khi hoàn tất bước này, bất kỳ người dùng nào biết tên miền của bạn (ví dụ: xanadu.com) sẽ có thể lấy địa chỉ IP của máy chủ DNS của bạn thông qua DNS hệ thống.

Để mọi người có thể khám phá địa chỉ IP của máy chủ Web của bạn, trong máy chủ DNS của bạn, bạn sẽ cần bao gồm các mục nhập ánh xạ tên máy chủ của máy chủ Web của bạn (ví dụ: www.xanadu.com) tới địa chỉ IP của nó. Bạn sẽ muốn có các mục tương tự cho

các máy chủ công khai khác trong công ty của bạn, bao gồm cả máy chủ thư của bạn. Theo cách này, nếu Alice muốn duyệt máy chủ Web của bạn, hệ thống DNS sẽ liên hệ với máy chủ DNS của bạn, tìm địa chỉ IP của máy chủ Web của bạn và đưa nó cho Alice. Sau đó, Alice có thể thiết lập kết nối TCP trực tiếp với máy chủ Web của bạn.

Tuy nhiên, vẫn còn một bước cần thiết và quan trọng khác để cho phép người ngoài từ khắp nơi trên thế giới truy cập vào máy chủ Web của bạn. Hãy xem xét điều gì sẽ xảy ra khi Alice, người biết địa chỉ IP của máy chủ Web của bạn, gửi một gói dữ liệu IP (ví dụ: phân đoạn TCP SYN) tới địa chỉ IP đó. Datagram này sẽ được định tuyến qua Internet, truy cập một loạt bộ định tuyến ở nhiều AS khác nhau và cuối cùng đến máy chủ Web của bạn. Khi bất kỳ một trong các bộ định tuyến nhận được datagram, nó sẽ tìm kiếm một mục trong bảng chuyển tiếp của nó để xác định cổng đi nào sẽ chuyển tiếp datagram. Do đó, mỗi bộ định tuyến cần biết về sự tồn tại của tiền tố /24 của công ty bạn (hoặc một số mục tổng hợp). Làm cách nào để bộ định tuyến nhận biết được tiền tố của công ty bạn? Như chúng ta vừa thấy, nó nhận biết được điều đó từ BGP! Cụ thể, khi công ty của bạn ký hợp đồng với một ISP địa phương và được chỉ định một tiền tố (tức là một dải địa chỉ), ISP địa phương của bạn sẽ sử dụng BGP để quảng cáo tiền tố của bạn với các ISP mà nó kết nối. Sau đó, các ISP đó sẽ sử dụng BGP để truyền bá quảng cáo. Cuối cùng, tất cả các bộ định tuyến Internet sẽ biết về tiền tố của bạn (hoặc về một số tổng hợp bao gồm tiền tố của bạn) và do đó có thể chuyển tiếp các gói dữ liệu một cách thích hợp đến máy chủ Web và thư của bạn.

**5.5 Mặt phẳng điều khiển SDN**

Trong phần này, chúng ta sẽ đi sâu vào mặt phẳng điều khiển SDN---logic toàn mạng kiểm soát việc chuyển tiếp gói giữa các thiết bị hỗ trợ SDN của mạng, cũng như cấu hình và quản lý các thiết bị này cũng như dịch vụ của chúng. Nghiên cứu của chúng tôi ở đây dựa trên cuộc thảo luận trước đó của chúng tôi về chuyển tiếp SDN tổng quát trong Phần 4.4, vì vậy trước tiên bạn có thể muốn xem lại phần đó cũng như Phần 5.1 của chương này trước khi tiếp tục. Như trong Phần 4.4, chúng ta sẽ áp dụng lại thuật ngữ được sử dụng trong tài liệu SDN và gọi các thiết bị chuyển tiếp của mạng là "bộ chuyển mạch gói" (hoặc chỉ là bộ chuyển mạch, với "gói" được hiểu), vì các quyết định chuyển tiếp có thể được thực hiện trên cơ sở địa chỉ nguồn/đích lớp mạng, địa chỉ nguồn/đích lớp liên kết, cũng như nhiều giá trị khác trong các trường tiêu đề gói lớp truyền tải, mạng và lớp liên kết.

Có thể xác định bốn đặc điểm chính của kiến ​​trúc SDN \[Kreutz 2015\]:

• Chuyển tiếp dựa trên luồng. Packet chuyển tiếp bằng các bộ chuyển mạch do SDN điều khiển có thể dựa trên bất kỳ số lượng giá trị trường tiêu đề nào trong tiêu đề lớp vận chuyển, lớp mạng hoặc lớp liên kết. Chúng ta đã thấy trong Phần 4.4 rằng tính trừu tượng của OpenFlow1.0 cho phép chuyển tiếp dựa trên 11 giá trị trường tiêu đề khác nhau. Điều này trái ngược

mạnh mẽ với cách tiếp cận truyền thống để chuyển tiếp dựa trên bộ định tuyến mà chúng tôi đã nghiên cứu trong Phần 5.2--5.4, trong đó việc chuyển tiếp các gói dữ liệu IP chỉ dựa trên địa chỉ đích IP của gói dữ liệu. Hãy nhớ lại Hình 5.2 rằng các quy tắc chuyển tiếp gói được chỉ định trong bảng luồng của switch; công việc của mặt phẳng điều khiển SDN là tính toán, quản lý và cài đặt các mục trong bảng luồng trong tất cả các thiết bị chuyển mạch của mạng. • Tách biệt mặt phẳng dữ liệu và mặt phẳng điều khiển. Sự tách biệt này được thể hiện rõ ràng trên Hình 5.2 và 5.14. Mặt phẳng dữ liệu bao gồm các bộ chuyển mạch của mạng--- các thiết bị tương đối đơn giản (nhưng nhanh) thực hiện các quy tắc "khớp và hành động" trong bảng quy trình của chúng. Mặt phẳng điều khiển bao gồm các máy chủ và phần mềm xác định và quản lý các bảng luồng của thiết bị chuyển mạch. • Chức năng điều khiển mạng: bên ngoài các bộ chuyển mạch mặt phẳng dữ liệu. Cho rằng chữ "S" trong SDN là dành cho "phần mềm", có lẽ không có gì đáng ngạc nhiên khi mặt phẳng điều khiển SDN được triển khai trong phần mềm. Tuy nhiên, không giống như các bộ định tuyến truyền thống, phần mềm này thực thi trên các máy chủ tách biệt và ở xa các bộ chuyển mạch của mạng. Như được hiển thị trong Hình 5.14, bản thân mặt phẳng điều khiển bao gồm hai thành phần---bộ điều khiển SDN (hoặc hệ điều hành mạng \[Gude 2008\]) và một bộ ứng dụng điều khiển mạng. Bộ điều khiển duy trì thông tin trạng thái mạng chính xác (ví dụ: trạng thái của các liên kết, bộ chuyển mạch và máy chủ từ xa); cung cấp thông tin này cho các ứng dụng điều khiển mạng đang chạy trong mặt phẳng điều khiển; và cung cấp các phương tiện để các ứng dụng này có thể giám sát, lập trình và điều khiển các thiết bị mạng cơ bản. Mặc dù bộ điều khiển trong Hình 5.14 được hiển thị dưới dạng một máy chủ trung tâm duy nhất, nhưng trên thực tế, bộ điều khiển chỉ tập trung về mặt logic; nó thường được triển khai trên một số máy chủ cung cấp hiệu suất phối hợp, có thể mở rộng và tính sẵn sàng cao. • Mạng có thể lập trình được. Mạng được lập trình thông qua các ứng dụng điều khiển mạng đang chạy trong mặt phẳng điều khiển. Các ứng dụng này đại diện cho "bộ não" của mặt phẳng điều khiển SDN, sử dụng các API do bộ điều khiển SDN cung cấp để chỉ định và điều khiển mặt phẳng dữ liệu trong các thiết bị mạng. Ví dụ: ứng dụng điều khiển mạng định tuyến có thể xác định đường dẫn cuối cùng giữa nguồn và đích (ví dụ: bằng cách thực thi thuật toán Dijkstra bằng cách sử dụng thông tin trạng thái nút và trạng thái liên kết được duy trì bởi bộ điều khiển SDN). Một ứng dụng mạng khác có thể thực hiện kiểm soát truy cập, nghĩa là xác định gói nào sẽ bị chặn tại một bộ chuyển mạch, như trong ví dụ thứ ba của chúng tôi ở Phần 4.4.3. Tuy nhiên, một ứng dụng khác có thể chuyển tiếp các gói theo cách thực hiện cân bằng tải máy chủ (ví dụ thứ hai mà chúng tôi đã xem xét trong Phần 4.4.3).

Từ cuộc thảo luận này, chúng ta có thể thấy rằng SDN đại diện cho một chức năng mạng "tách rời" đáng kể---các bộ chuyển mạch mặt phẳng dữ liệu, bộ điều khiển SDN và các ứng dụng điều khiển mạng là các thực thể riêng biệt, mỗi thực thể có thể được cung cấp bởi các nhà cung cấp và tổ chức khác nhau. Điều này trái ngược với mô hình tiền SDN trong đó bộ chuyển mạch/bộ định tuyến (cùng với việc triển khai giao thức và phần mềm mặt phẳng điều khiển nhúng của nó) là nguyên khối, tích hợp theo chiều dọc và được bán bởi một nhà cung cấp duy nhất. Việc tách nhóm này

Chức năng mạng trong SDN được ví như sự phát triển trước đó từ máy tính lớn (trong đó phần cứng, phần mềm hệ thống và ứng dụng được cung cấp bởi một nhà cung cấp duy nhất) sang máy tính cá nhân (với phần cứng, hệ điều hành và ứng dụng riêng biệt). Việc tách phần cứng máy tính, phần mềm hệ thống và ứng dụng đã dẫn đến một hệ sinh thái mở, phong phú được thúc đẩy bởi sự đổi mới trong cả ba lĩnh vực này; một hy vọng cho SDN là nó sẽ tiếp tục thúc đẩy và tạo điều kiện cho sự đổi mới phong phú như vậy.

Với sự hiểu biết của chúng ta về kiến ​​trúc SDN trong Hình 5.14, nhiều câu hỏi sẽ nảy sinh một cách tự nhiên. Các bảng luồng thực sự được tính toán như thế nào và ở đâu? Các bảng này được cập nhật như thế nào để phản hồi các sự kiện tại các thiết bị do SDN kiểm soát (ví dụ: một liên kết đính kèm đi lên/xuống)? Và các mục trong bảng luồng tại nhiều thiết bị chuyển mạch được phối hợp như thế nào để mang lại chức năng thống nhất và được phối hợp trên toàn mạng (ví dụ: các đường dẫn từ đầu đến cuối để chuyển tiếp gói từ nguồn đến đích hoặc tường lửa phân phối phối hợp)? Vai trò của mặt phẳng điều khiển SDN là cung cấp những khả năng này và nhiều khả năng khác.

Lộ trình

Ứng dụng điều khiển mạng

Điều khiển

máy bay

Mặt phẳng dữ liệu

Được kiểm soát SDN Switches

Kiểm soát truy cập

Cân bằng tải

Hướng Bắc

API

Hướng Nam

API

Bộ điều khiển SDN (hệ điều hành mạng)

*Hình 5.14 ♦ Các thành phần của kiến ​​trúc SDN: Điều khiển SDN*

chuyển mạch, bộ điều khiển SDN, ứng dụng điều khiển mạng

**5.5.1 Mặt phẳng điều khiển SDN: Bộ điều khiển SDN và các ứng dụng điều khiển mạng SDN**

Hãy bắt đầu cuộc thảo luận tóm tắt của chúng ta về mặt phẳng điều khiển SDN bằng cách xem xét các khả năng chung mà mặt phẳng điều khiển phải cung cấp. Như chúng ta sẽ thấy, cách tiếp cận "nguyên tắc đầu tiên" trừu tượng này sẽ dẫn chúng ta đến một kiến ​​trúc tổng thể phản ánh cách các mặt phẳng điều khiển SDN đã được triển khai trong thực tế.

Như đã lưu ý ở trên, mặt phẳng điều khiển SDN chia thành hai thành phần--- bộ điều khiển SDN và các ứng dụng điều khiển mạng SDN. Trước tiên hãy khám phá bộ điều khiển. Nhiều bộ điều khiển SDN đã được phát triển kể từ bộ điều khiển SDN đầu tiên \[Gude 2008\]; xem \[Kreutz 2015\] để biết bản khảo sát cực kỳ kỹ lưỡng. Hình 5.15 cung cấp cái nhìn chi tiết hơn về bộ điều khiển SDN chung. Chức năng của bộ điều khiển có thể được tổ chức rộng rãi thành ba lớp. Hãy xem xét các lớp này theo kiểu từ dưới lên:

• Lớp giao tiếp: giao tiếp giữa bộ điều khiển SDN và các thiết bị mạng được điều khiển. Rõ ràng, nếu bộ điều khiển SDN sẽ điều khiển hoạt động của bộ chuyển mạch, máy chủ hoặc thiết bị khác hỗ trợ SDN từ xa thì cần có một giao thức để truyền thông tin giữa bộ điều khiển và thiết bị đó. Ngoài ra, thiết bị phải có khả năng giao tiếp các sự kiện được quan sát cục bộ với bộ điều khiển (ví dụ: thông báo cho biết liên kết đính kèm đã tăng hoặc giảm, thiết bị vừa tham gia mạng hoặc nhịp tim cho biết thiết bị đã hoạt động). Những sự kiện này cung cấp cho bộ điều khiển SDN cái nhìn cập nhật về trạng thái của mạng. Giao thức này tạo thành lớp thấp nhất của kiến ​​trúc bộ điều khiển, như trong Hình 5.15. Giao tiếp giữa bộ điều khiển và các thiết bị được điều khiển đi qua cái được gọi là giao diện "hướng nam" của bộ điều khiển. Trong Phần 5.5.2, chúng ta sẽ nghiên cứu OpenFlow---một giao thức cụ thể cung cấp chức năng giao tiếp này. OpenFlow được triển khai trong hầu hết, nếu không phải tất cả, bộ điều khiển SDN. • Lớp quản lý trạng thái trên toàn mạng. Các quyết định điều khiển cuối cùng do mặt phẳng điều khiển SDN đưa ra---ví dụ: định cấu hình các bảng luồng trong tất cả các thiết bị chuyển mạch để đạt được chuyển tiếp đầu cuối mong muốn, để triển khai cân bằng tải hoặc để triển khai khả năng tường lửa cụ thể---sẽ yêu cầu bộ điều khiển phải có thông tin cập nhật về trạng thái của máy chủ, liên kết, thiết bị chuyển mạch và các thiết bị do SDN điều khiển khác trong mạng. Bảng luồng của bộ chuyển mạch chứa các bộ đếm có giá trị cũng có thể được các ứng dụng điều khiển mạng sử dụng một cách có lợi; do đó những giá trị này sẽ có sẵn cho các ứng dụng. Vì mục đích cuối cùng của mặt phẳng điều khiển là xác định các bảng luồng cho các thiết bị được điều khiển khác nhau nên bộ điều khiển cũng có thể duy trì một bản sao của các bảng này. Tất cả các thông tin này đều là ví dụ về "trạng thái" trên toàn mạng được duy trì bởi bộ điều khiển SDN. • Giao diện của lớp ứng dụng điều khiển mạng. Bộ điều khiển tương tác với các ứng dụng điều khiển mạng thông qua giao diện "hướng bắc" của nó. API này

cho phép các ứng dụng điều khiển mạng đọc/ghi trạng thái mạng và các bảng luồng trong lớp quản lý trạng thái. Các ứng dụng có thể đăng ký để được thông báo khi xảy ra sự kiện thay đổi trạng thái, để chúng có thể thực hiện hành động phản hồi các thông báo sự kiện mạng được gửi từ các thiết bị do SDN kiểm soát. Các loại API khác nhau có thể được cung cấp; chúng ta sẽ thấy rằng hai bộ điều khiển SDN phổ biến giao tiếp với các ứng dụng của họ bằng giao diện phản hồi yêu cầu REST \[Fielding 2000\].

Chúng tôi đã lưu ý nhiều lần rằng bộ điều khiển SDN có thể được coi là \"tập trung về mặt logic\", nghĩa là bộ điều khiển có thể được xem từ bên ngoài (ví dụ: từ quan điểm của các thiết bị được điều khiển SDN và điều khiển mạng bên ngoài).

Kiểm soát truy cập định tuyến

Cân bằng tải

Giao diện, trừu tượng cho các ứng dụng điều khiển mạng

Mạng

đồ thị

nghỉ ngơi

Ý định API

Giao tiếp đến/từ các thiết bị được điều khiển

Quản lý trạng thái mạnh mẽ, phân tán trên toàn mạng

Trạng thái liên kết

thông tin Host thông tin Switch

thông tin

Bảng luồng thống kê

OpenFlow SNMP

Bộ điều khiển SDN

Hướng Bắc

API

Hướng Nam

API

*Hình 5.15 ♦ Các thành phần của bộ điều khiển SDN*

ứng dụng) dưới dạng một dịch vụ nguyên khối duy nhất. Tuy nhiên, các dịch vụ này và cơ sở dữ liệu được sử dụng để lưu giữ thông tin trạng thái được triển khai trên thực tế bởi một bộ máy chủ phân tán vì khả năng chịu lỗi, tính sẵn sàng cao hoặc vì lý do hiệu suất. Với các chức năng của bộ điều khiển được triển khai bởi một tập hợp các máy chủ, ngữ nghĩa của các hoạt động nội bộ của bộ điều khiển (ví dụ: duy trì thứ tự thời gian hợp lý của các sự kiện, tính nhất quán, sự đồng thuận, v.v.) phải được xem xét \[Panda 2013\]. Những lo ngại như vậy là phổ biến trên nhiều hệ thống phân tán khác nhau; xem \[Lamport 1989, Lampson 1996\] để biết các giải pháp tinh tế cho những thách thức này. Các bộ điều khiển hiện đại như OpenDaylight \[OpenDaylight 2020\] và ONOS \[ONOS 2020\] (xem thanh bên) đã chú trọng đáng kể vào việc kiến ​​trúc một nền tảng bộ điều khiển phân tán vật lý nhưng tập trung về mặt logic, cung cấp các dịch vụ có thể mở rộng và tính sẵn sàng cao cho các thiết bị được điều khiển cũng như các ứng dụng điều khiển mạng.

Kiến trúc được mô tả trong Hình 5.15 gần giống với kiến ​​trúc của bộ điều khiển NOX được đề xuất ban đầu vào năm 2008 \[Gude 2008\], cũng như kiến ​​trúc của bộ điều khiển OpenDaylight \[OpenDaylight 2020\] và ONOS \[ONOS 2020\] SDN ngày nay (xem thanh bên). Chúng tôi sẽ trình bày một ví dụ về hoạt động của bộ điều khiển trong Phần 5.5.3. Tuy nhiên, trước tiên, hãy xem xét giao thức OpenFlow, giao thức sớm nhất và hiện tại là một trong số các giao thức có thể được sử dụng để liên lạc giữa bộ điều khiển SDN và thiết bị được điều khiển, nằm trong lớp giao tiếp của bộ điều khiển.

**5.5.2 Giao thức OpenFlow**

Giao thức OpenFlow \[OpenFlow 2009, ONF 2020\] hoạt động giữa bộ điều khiển SDN và bộ chuyển mạch do SDN điều khiển hoặc thiết bị khác triển khai API OpenFlow mà chúng tôi đã nghiên cứu trước đó trong Phần 4.4. Giao thức OpenFlow hoạt động trên TCP, với số cổng mặc định là 6653.

Trong số các thông báo quan trọng truyền từ bộ điều khiển đến công tắc được điều khiển như sau:

• Cấu hình. Thông báo này cho phép bộ điều khiển truy vấn và đặt các tham số cấu hình của bộ chuyển mạch. • Sửa đổi-Trạng thái. Thông báo này được bộ điều khiển sử dụng để thêm/xóa hoặc sửa đổi các mục trong bảng luồng của bộ chuyển mạch và để đặt các thuộc tính cổng chuyển mạch. • Trạng thái đọc. Thông báo này được bộ điều khiển sử dụng để thu thập số liệu thống kê và giá trị bộ đếm từ bảng luồng và cổng của bộ chuyển mạch. • Gửi-Packet. Thông báo này được bộ điều khiển sử dụng để gửi một gói cụ thể ra khỏi một cổng được chỉ định tại bộ chuyển mạch được điều khiển. Bản thân tin nhắn chứa gói sẽ được gửi trong tải trọng của nó.

Trong số các thông báo truyền từ bộ chuyển mạch do SDN điều khiển tới bộ điều khiển như sau:

• Loại bỏ dòng chảy. Thông báo này thông báo cho bộ điều khiển rằng một mục trong bảng quy trình đã bị xóa, chẳng hạn như do hết thời gian chờ hoặc do nhận được thông báo trạng thái sửa đổi.

• trạng thái Port. Thông báo này được switch sử dụng để thông báo cho bộ điều khiển về sự thay đổi trạng thái cổng. • Packet-trong. Hãy nhớ lại Phần 4.4 rằng một gói đến cổng chuyển mạch và không khớp với bất kỳ mục nào trong bảng luồng sẽ được gửi đến bộ điều khiển để xử lý bổ sung. Các gói trùng khớp cũng có thể được gửi đến bộ điều khiển, như một hành động được thực hiện đối với trận đấu. Tin nhắn gói vào được sử dụng để gửi các gói như vậy đến bộ điều khiển.

Thông báo OpenFlow bổ sung được xác định trong \[OpenFlow 2009, ONF 2020\].

MẠNG TOÀN CẦU ĐƯỢC ĐỊNH NGHĨA PHẦN MỀM CỦA GOOGLE

Hãy nhớ lại nghiên cứu điển hình ở Phần 2.6 rằng Google triển khai mạng diện rộng (WAN) chuyên dụng để kết nối các trung tâm dữ liệu và cụm máy chủ của mình (trong IXP và ISP). Mạng này, được gọi là B4, có mặt phẳng điều khiển SDN do Google thiết kế được xây dựng trên OpenFlow. Mạng của Google có thể thúc đẩy các liên kết WAN với mức sử dụng gần 70% trong thời gian dài (tăng gấp hai đến ba lần so với mức sử dụng liên kết thông thường) và phân chia luồng ứng dụng giữa nhiều đường dẫn dựa trên mức độ ưu tiên của ứng dụng và nhu cầu luồng hiện có \[Jain 2013\].

Mạng Google B4 đặc biệt phù hợp với SDN: (i) Google kiểm soát tất cả các thiết bị từ máy chủ biên trong IXP và ISP đến bộ định tuyến trong lõi mạng của họ; (ii) các ứng dụng sử dụng nhiều băng thông nhất là các bản sao dữ liệu quy mô lớn giữa các trang web có thể trì hoãn các ứng dụng tương tác có mức độ ưu tiên cao hơn trong thời gian tắc nghẽn tài nguyên; (iii) chỉ với vài chục trung tâm dữ liệu được kết nối thì việc điều khiển tập trung là khả thi.

Mạng B4 của Google sử dụng các bộ chuyển mạch được xây dựng tùy chỉnh, mỗi bộ chuyển mạch triển khai một phiên bản OpenFlow mở rộng hơn một chút, với Tác nhân luồng mở (OFA) cục bộ có tinh thần tương tự như tác nhân điều khiển mà chúng ta gặp trong Hình 5.2. Lần lượt, mỗi OFA kết nối với Bộ điều khiển luồng mở (OFC) trong máy chủ điều khiển mạng (NCS), sử dụng mạng "ngoài băng tần" riêng biệt, khác với mạng mang lưu lượng trung tâm dữ liệu giữa các trung tâm dữ liệu. Do đó, OFC cung cấp các dịch vụ được NCS sử dụng để liên lạc với các thiết bị chuyển mạch được điều khiển của nó, tương tự như lớp thấp nhất trong kiến ​​trúc SDN được hiển thị trong Hình 5.15. Trong B4, OFC cũng thực hiện các chức năng quản lý trạng thái, giữ trạng thái nút và liên kết trong Cơ sở thông tin mạng (NIB). Việc triển khai OFC của Google dựa trên bộ điều khiển ONIX SDN \[Koponen 2010\]. Hai giao thức định tuyến, BGP (để định tuyến giữa các trung tâm dữ liệu) và IS-IS (một giao thức gần gũi với OSPF, để định tuyến trong một trung tâm dữ liệu), được triển khai. Paxos \[Chandra 2007\] được sử dụng để thực thi các bản sao nóng của các thành phần NCS nhằm bảo vệ khỏi lỗi.

Một ứng dụng điều khiển mạng kỹ thuật lưu lượng, nằm một cách logic phía trên tập hợp các máy chủ điều khiển mạng, tương tác với các máy chủ này để cung cấp khả năng cung cấp băng thông toàn cầu, trên toàn mạng cho các nhóm luồng ứng dụng. Với B4, SDN đã có một bước nhảy vọt quan trọng trong mạng lưới hoạt động của một nhà cung cấp mạng toàn cầu. Xem \[Jain 2013; Hong 2018\] để biết mô tả chi tiết về B4.

NGUYÊN TẮC TRONG THỰC HÀNH

**5.5.3 Tương tác mặt phẳng dữ liệu và điều khiển: Một ví dụ**

Để củng cố sự hiểu biết của chúng ta về sự tương tác giữa các bộ chuyển mạch do SDN điều khiển và bộ điều khiển SDN, chúng ta hãy xem xét ví dụ được hiển thị trong Hình 5.16, trong đó thuật toán Dijkstra (mà chúng ta đã nghiên cứu trong Phần 5.2) được sử dụng để xác định các tuyến đường đi ngắn nhất. Kịch bản SDN trong Hình 5.16 có hai điểm khác biệt quan trọng so với kịch bản điều khiển mỗi bộ định tuyến trước đó trong Phần 5.2.1 và 5.3, trong đó thuật toán của Dijkstra được triển khai trong mỗi bộ định tuyến và các bản cập nhật trạng thái liên kết tràn ngập trong tất cả các bộ định tuyến mạng:

• Thuật toán Dijkstra được thực thi như một ứng dụng riêng biệt, bên ngoài các chuyển mạch gói. • Các thiết bị chuyển mạch Packet gửi các cập nhật liên kết tới bộ điều khiển SDN chứ không gửi cho nhau.

Trong ví dụ này, giả sử rằng liên kết giữa switch s1 và s2 bị hỏng; việc định tuyến đường dẫn ngắn nhất được triển khai và do đó các quy tắc chuyển tiếp luồng đến và đi tại s1, s3 và s4 bị ảnh hưởng, nhưng s2 đó

*Hình 5.16 ♦ Kịch bản bộ điều khiển SDN: Thay đổi trạng thái liên kết*

Mạng

đồ thị

nghỉ ngơi

Ý định API

Bảng luồng thống kê

OpenFlow SNMP

Trạng thái liên kết của Dijkstra

Lộ trình

s1

s2

s3

s4

Trạng thái liên kết

thông tin Host thông tin Switch

thông tin

hoạt động không thay đổi. Cũng giả sử rằng OpenFlow được sử dụng làm giao thức lớp giao tiếp và mặt phẳng điều khiển không thực hiện chức năng nào khác ngoài định tuyến trạng thái liên kết.

1\. Switch s1, gặp lỗi liên kết giữa chính nó và s2, thông báo cho SDN

bộ điều khiển thay đổi trạng thái liên kết bằng thông báo trạng thái cổng OpenFlow. 2. Bộ điều khiển SDN nhận được thông báo OpenFlow cho biết trạng thái liên kết

thay đổi và thông báo cho người quản lý trạng thái liên kết, cập nhật cơ sở dữ liệu trạng thái liên kết. 3. Ứng dụng điều khiển mạng thực hiện định tuyến trạng thái liên kết của Dijkstra

trước đây đã đăng ký để được thông báo khi trạng thái liên kết thay đổi. Ứng dụng đó nhận được thông báo về sự thay đổi trạng thái liên kết. 4. Ứng dụng định tuyến trạng thái liên kết tương tác với trình quản lý trạng thái liên kết để nhận

trạng thái liên kết được cập nhật; nó cũng có thể tham khảo các thành phần khác trong lớp quản lý trạng thái. Sau đó nó tính toán các đường dẫn có chi phí thấp nhất mới. 5. Sau đó, ứng dụng định tuyến trạng thái liên kết sẽ tương tác với trình quản lý bảng luồng,

xác định các bảng luồng sẽ được cập nhật. 6. Sau đó, trình quản lý bảng quy trình sử dụng giao thức OpenFlow để cập nhật bảng quy trình

các mục tại các công tắc bị ảnh hưởng---s1 (bây giờ sẽ định tuyến các gói đến s2 qua s4), s2 (bây giờ sẽ bắt đầu nhận các gói từ s1 thông qua công tắc trung gian s4) và s4 (bây giờ phải chuyển tiếp các gói từ s1 đến s2).

Ví dụ này đơn giản nhưng minh họa cách mặt phẳng điều khiển SDN cung cấp các dịch vụ mặt phẳng điều khiển (trong trường hợp này là định tuyến lớp mạng) đã được triển khai trước đó với điều khiển trên mỗi bộ định tuyến được thực hiện trong mỗi bộ định tuyến mạng. Giờ đây, người ta có thể dễ dàng đánh giá cao cách một ISP hỗ trợ SDN có thể dễ dàng chuyển từ định tuyến đường dẫn có chi phí thấp nhất sang phương pháp định tuyến phù hợp hơn. Thật vậy, vì bộ điều khiển có thể điều chỉnh các bảng luồng theo ý muốn, nên nó có thể thực hiện bất kỳ hình thức chuyển tiếp nào mà nó hài lòng---chỉ bằng cách thay đổi phần mềm điều khiển ứng dụng của nó. Sự dễ dàng thay đổi này phải trái ngược với trường hợp mặt phẳng điều khiển trên mỗi bộ định tuyến truyền thống, trong đó phần mềm trong tất cả các bộ định tuyến (có thể được cung cấp cho ISP bởi nhiều nhà cung cấp độc lập) phải được thay đổi.

**5.5.4 SDN: Quá khứ và Tương lai**

Mặc dù sự quan tâm sâu sắc đến SDN là một hiện tượng tương đối gần đây, nguồn gốc kỹ thuật của SDN và đặc biệt là sự tách biệt giữa các mặt phẳng dữ liệu và điều khiển, đã có lịch sử xa hơn đáng kể. Năm 2004, \[Feamster 2004, Lakshman 2004, RFC 3746\] đều lập luận về việc tách các mặt phẳng điều khiển và dữ liệu của mạng. \[van der Merwe 1998\] mô tả một khung điều khiển cho mạng ATM \[Black 1995\] với nhiều bộ điều khiển, mỗi bộ điều khiển một số bộ chuyển mạch ATM. Dự án Ethane \[Casado 2007\] đã đi tiên phong trong khái niệm về một mạng gồm các bộ chuyển mạch Ethernet dựa trên luồng đơn giản với các bảng luồng khớp-cộng-hành động, một bộ điều khiển tập trung quản lý luồng

tiếp nhận và định tuyến cũng như chuyển tiếp các gói chưa khớp từ bộ chuyển mạch sang bộ điều khiển. Một mạng lưới gồm hơn 300 thiết bị chuyển mạch Ethane đã hoạt động vào năm 2007. Ethane nhanh chóng phát triển thành dự án OpenFlow và phần còn lại (như người ta vẫn nói) là lịch sử!

Nhiều nỗ lực nghiên cứu nhằm phát triển kiến ​​trúc và khả năng SDN trong tương lai. Như chúng ta đã thấy, cuộc cách mạng SDN đang dẫn đến sự thay thế đột phá các bộ chuyển mạch và bộ định tuyến nguyên khối chuyên dụng (với cả mặt phẳng dữ liệu và điều khiển) bằng phần cứng chuyển mạch đơn giản và mặt phẳng điều khiển phần mềm phức tạp. Một cách khái quát hóa SDN được gọi là ảo hóa chức năng mạng (NFV) (mà chúng ta đã thảo luận trước đó trong Phần 4.5) cũng nhằm mục đích thay thế đột phá các hộp trung gian phức tạp (chẳng hạn như hộp trung gian có phần cứng chuyên dụng và phần mềm độc quyền cho dịch vụ/bộ nhớ đệm phương tiện) bằng các máy chủ, chuyển mạch và lưu trữ đơn giản. Lĩnh vực nghiên cứu quan trọng thứ hai tìm cách mở rộng các khái niệm SDN từ cài đặt nội bộ AS sang cài đặt liên AS \[Gupta 2014\].

NGHIÊN CỨU TRƯỜNG HỢP BỘ ĐIỀU KHIỂN SDN: BỘ ĐIỀU KHIỂN OPENDAYLIGHT VÀ ONOS

Trong những ngày đầu tiên của SDN, chỉ có một giao thức SDN duy nhất (OpenFlow \[McKeown 2008; OpenFlow 2009\]) và một bộ điều khiển SDN duy nhất (NOX \[Gude 2008\]). Kể từ đó, số lượng bộ điều khiển SDN nói riêng đã tăng lên đáng kể \[Kreutz 2015\]. Một số bộ điều khiển SDN dành riêng cho công ty và độc quyền, đặc biệt khi được sử dụng để kiểm soát các mạng độc quyền nội bộ (ví dụ: trong hoặc giữa các trung tâm dữ liệu của công ty). Nhưng nhiều bộ điều khiển khác là mã nguồn mở và được triển khai bằng nhiều ngôn ngữ lập trình khác nhau \[Erickson 2013\]. Gần đây nhất, bộ điều khiển OpenDaylight \[OpenDaylight 2020\] và bộ điều khiển ONOS \[ONOS 2020\] đã nhận được sự hỗ trợ đáng kể trong ngành. Cả hai đều là nguồn mở và đang được phát triển với sự hợp tác của Linux Foundation.

Bộ điều khiển OpenDaylight

Hình 5.17 trình bày một cái nhìn đơn giản về nền tảng bộ điều khiển OpenDaylight (ODL)

\[OpenDaylight 2020, Eckel 2017\].

Các chức năng mạng cơ bản của ODL là trung tâm của bộ điều khiển và tương ứng chặt chẽ với các khả năng quản lý trạng thái trên toàn mạng mà chúng ta gặp trong Hình 5.15. Lớp trừu tượng dịch vụ (SAL) là trung tâm thần kinh của bộ điều khiển, cho phép các thành phần và ứng dụng của bộ điều khiển gọi các dịch vụ của nhau, truy cập cấu hình và dữ liệu vận hành cũng như đăng ký các sự kiện mà chúng tạo ra. SAL cũng cung cấp giao diện trừu tượng thống nhất cho các giao thức cụ thể hoạt động giữa bộ điều khiển ODL và các thiết bị được điều khiển. Các giao thức này bao gồm OpenFlow (mà chúng tôi đã đề cập trong Phần 4.5),

NGUYÊN TẮC TRONG THỰC HÀNH

và giao thức Giao thức quản lý mạng đơn giản (SNMP) và giao thức Cấu hình mạng (NETCONF), cả hai giao thức này chúng tôi sẽ đề cập trong Phần 5.7. Giao thức quản lý cơ sở dữ liệu Open vSwitch (OVSDB) được sử dụng để quản lý chuyển mạch trung tâm dữ liệu, một lĩnh vực ứng dụng quan trọng cho công nghệ SDN. Chúng tôi sẽ giới thiệu mạng trung tâm dữ liệu trong Chương 6.

Các ứng dụng và điều phối mạng xác định cách thức chuyển tiếp mặt phẳng dữ liệu và các dịch vụ khác, chẳng hạn như tường lửa và cân bằng tải, được thực hiện trong các thiết bị được điều khiển. ODL cung cấp hai cách để các ứng dụng có thể tương tác với các dịch vụ bộ điều khiển gốc (và do đó là các thiết bị) và với nhau. Theo cách tiếp cận dựa trên API (AD-SAL), được hiển thị trong Hình 5.17, các ứng dụng giao tiếp với các mô-đun bộ điều khiển bằng cách sử dụng API phản hồi yêu cầu REST chạy trên HTTP. Các bản phát hành đầu tiên của bộ điều khiển OpenDaylight chỉ cung cấp AD-SAL. Khi ODL ngày càng được sử dụng nhiều hơn cho việc quản lý và cấu hình mạng, các bản phát hành ODL sau này đã giới thiệu cách tiếp cận ModelDriven (MD-SAL). Ở đây, ngôn ngữ mô hình hóa dữ liệu YANG \[RFC 6020\] xác định các mô hình thiết bị, giao thức, cấu hình mạng và dữ liệu trạng thái vận hành. Sau đó, các thiết bị được cấu hình và quản lý bằng cách thao tác dữ liệu này bằng giao thức NETCONF.

*Hình 5.17 ♦ Một cái nhìn đơn giản về bộ điều khiển OpenDaylight*

API REST/RESTCONF/NETCONF

Dịch vụ nâng cao

Các chức năng mạng cơ bản

Xử lý cấu trúc liên kết

Switch

mgr.

Thống kê quản lý AAA

Khám phá thiết bị

Chuyển tiếp

quy tắc mgr.

Host Trình theo dõi

Điều phối mạng và

Ứng dụng

API hướng bắc

API hướng Nam

và các plugin giao thức

Trừu tượng hóa dịch vụ

Lớp (SAL)

nhắn tin

Luồng mở NETCONF SNMP OVSDB

Cân bằng tải tường lửa kỹ thuật giao thông

config. và dữ liệu vận hành

cửa hàng

Bộ điều khiển ONOS

Figure 5.18 presents a simplified view of the ONOS controller ONOS 2020\]. Similar to the canonical controller in Figure 5.15, three layers can be identified in the ONOS controller:

• Các giao thức và trừu tượng hướng Bắc. A unique feature of ONOS is its intent framework, which allows an application to request a high-level service (e.g., to setup a connection between host A and Host B, or conversely to not allow Host A and host B to communicate) without having to know the details of how this service is performed. State information is provided to network-control applications across the northbound API either synchronously (via query) or asynchronously (via listener callbacks, e.g., when network state changes). • Lõi phân tán. Trạng thái của các liên kết, máy chủ và thiết bị của mạng được duy trì trong lõi phân phối của ONOS. ONOS được triển khai dưới dạng dịch vụ trên một tập hợp các máy chủ được kết nối với nhau, trong đó mỗi máy chủ chạy một bản sao phần mềm ONOS giống hệt nhau; số lượng máy chủ tăng lên mang lại khả năng phục vụ tăng lên. Cốt lõi ONOS

*Hình 5.18 ♦ Kiến trúc bộ điều khiển ONOS*

API REST có ý định

Hosts Đường dẫn

Cấu trúc liên kết

Liên kết thiết bị

Quy tắc dòng chảy

Thống kê

Liên kết thiết bị Host Luồng Packet

OpenFlow Netconf OVSDB

Ứng dụng điều khiển mạng

Trừu tượng về phía bắc,

giao thức

ONOS được phân phối

cốt lõi

trừu tượng về phía nam,

giao thức

**5.6 ICMP: Giao thức thông báo điều khiển Internet**

Giao thức thông báo điều khiển Internet (ICMP), được chỉ định trong \[RFC 792\], được các máy chủ và bộ định tuyến sử dụng để truyền đạt thông tin lớp mạng với nhau. Việc sử dụng ICMP điển hình nhất là để báo cáo lỗi. Ví dụ: khi chạy phiên HTTP, bạn có thể gặp phải thông báo lỗi như "Không thể truy cập mạng đích". Thông báo này có nguồn gốc từ ICMP. Tại một thời điểm nào đó, bộ định tuyến IP không thể tìm thấy đường dẫn đến máy chủ được chỉ định trong yêu cầu HTTP của bạn. Bộ định tuyến đó đã tạo và gửi thông báo ICMP tới máy chủ của bạn để báo lỗi.

ICMP thường được coi là một phần của IP, nhưng về mặt kiến ​​trúc, nó nằm ngay phía trên IP, vì các thông báo ICMP được chứa bên trong các gói dữ liệu IP. Nghĩa là, các tin nhắn ICMP được truyền dưới dạng tải trọng IP, cũng giống như các phân đoạn TCP hoặc UDP được truyền dưới dạng tải trọng IP. Tương tự, khi máy chủ nhận được một gói dữ liệu IP với ICMP được chỉ định làm giao thức lớp trên (số giao thức lớp trên là 1), nó sẽ phân tách nội dung của gói dữ liệu thành ICMP, giống như nó sẽ phân tách nội dung của gói dữ liệu thành TCP hoặc UDP.

Các thông báo ICMP có một loại và một trường mã, đồng thời chứa tiêu đề và 8 byte đầu tiên của gói dữ liệu IP khiến thông báo ICMP được tạo ngay từ đầu (để người gửi có thể xác định gói dữ liệu gây ra lỗi). Các loại thông báo ICMP đã chọn được hiển thị trong Hình 5.19. Lưu ý rằng các thông báo ICMP không chỉ được sử dụng cho các tình trạng lỗi báo hiệu.

Chương trình ping nổi tiếng gửi tin nhắn ICMP loại 8 mã 0 đến máy chủ được chỉ định. Máy chủ đích, nhìn thấy yêu cầu tiếng vang, sẽ gửi lại mã loại 0 0 ICMP phản hồi tiếng vang. Hầu hết các triển khai TCP/IP đều hỗ trợ máy chủ ping trực tiếp trong hệ điều hành; nghĩa là máy chủ không phải là một tiến trình. Chương 11 của \[Stevens 1990\] cung cấp mã nguồn cho chương trình ping client. Lưu ý rằng chương trình máy khách cần có khả năng hướng dẫn hệ điều hành tạo thông báo ICMP thuộc loại 8 mã 0.

Một thông báo ICMP thú vị khác là thông báo dập tắt nguồn. Thông báo này hiếm khi được sử dụng trong thực tế. Mục đích ban đầu của nó là thực hiện kiểm soát tắc nghẽn---để cho phép bộ định tuyến bị tắc nghẽn gửi thông báo hạn chế nguồn ICMP tới máy chủ để buộc

cung cấp các cơ chế sao chép và phối hợp dịch vụ giữa các phiên bản, cung cấp cho các ứng dụng bên trên và các thiết bị mạng bên dưới sự trừu tượng hóa của các dịch vụ cốt lõi tập trung về mặt logic. • Các giao thức và trừu tượng hóa hướng Nam. Sự trừu tượng hóa về phía nam che giấu tính không đồng nhất của các máy chủ, liên kết, bộ chuyển mạch và giao thức cơ bản, cho phép lõi phân tán là bất khả tri của cả thiết bị và giao thức. Do sự trừu tượng này, giao diện hướng nam bên dưới lõi phân tán cao hơn về mặt logic so với bộ điều khiển chuẩn của chúng tôi trong Hình 5.14 hoặc bộ điều khiển ODL trong Hình 5.17.

máy chủ đó để giảm tốc độ truyền của nó. Chúng ta đã thấy trong Chương 3 rằng TCP có cơ chế kiểm soát tắc nghẽn riêng hoạt động ở lớp truyền tải và các bit Thông báo tắc nghẽn rõ ràng có thể được các thiết bị mạng sau này sử dụng để báo hiệu tắc nghẽn.

Trong Chương 1, chúng tôi đã giới thiệu chương trình Traceroute, cho phép chúng tôi theo dõi lộ trình từ máy chủ này đến bất kỳ máy chủ nào khác trên thế giới. Điều thú vị là Traceroute được triển khai bằng tin nhắn ICMP. Để xác định tên và địa chỉ của bộ định tuyến giữa nguồn và đích, Traceroute trong nguồn sẽ gửi một loạt gói dữ liệu IP thông thường đến đích. Mỗi gói dữ liệu này mang một phân đoạn UDP với số cổng UDP không chắc chắn. Gói dữ liệu đầu tiên trong số này có TTL là 1, gói thứ hai là 2, gói thứ ba là 3, v.v. Nguồn cũng bắt đầu tính giờ cho mỗi datagram. Khi datagram thứ n đến bộ định tuyến thứ n, bộ định tuyến thứ n sẽ quan sát thấy TTL của datagram vừa hết hạn. Theo các quy tắc của giao thức IP, bộ định tuyến sẽ loại bỏ datagram và gửi thông báo cảnh báo ICMP tới nguồn (loại 11 mã 0). Thông báo cảnh báo này bao gồm tên của bộ định tuyến và địa chỉ IP của nó. Khi thông báo ICMP này quay trở lại nguồn, nguồn sẽ nhận được thời gian khứ hồi từ bộ đếm thời gian cũng như tên và địa chỉ IP của bộ định tuyến thứ n từ thông báo ICMP.

Làm cách nào để nguồn Traceroute biết khi nào nên ngừng gửi phân đoạn UDP? Hãy nhớ lại rằng nguồn tăng trường TTL cho mỗi datagram mà nó gửi. Do đó, một trong các datagram cuối cùng sẽ đến được máy chủ đích. Bởi vì datagram này chứa phân đoạn UDP với số cổng không chắc chắn, nên đích đến

*Hình 5.19 ♦ ICMP loại thông báo*

ICMP Mã loại Mô tả

tiếng vang trả lời (để ping)

mạng đích không thể truy cập được

máy chủ đích không thể truy cập được

giao thức đích không thể truy cập được

cổng đích không thể truy cập được

mạng đích không xác định

máy chủ đích không xác định

dập tắt nguồn (kiểm soát tắc nghẽn)

yêu cầu tiếng vang

quảng cáo bộ định tuyến

khám phá bộ định tuyến

TTL đã hết hạn

IP tiêu đề xấu

Máy chủ gửi thông báo ICMP không thể truy cập cổng (loại 3 mã 3) trở lại nguồn. Khi máy chủ nguồn nhận được thông báo ICMP cụ thể này, nó biết rằng nó không cần gửi các gói thăm dò bổ sung. (Chương trình Traceroute tiêu chuẩn thực sự gửi bộ ba gói có cùng TTL; do đó, đầu ra Traceroute cung cấp ba kết quả cho mỗi TTL.)

Theo cách này, máy chủ nguồn sẽ tìm hiểu số lượng và danh tính của các bộ định tuyến nằm giữa nó và máy chủ đích cũng như thời gian khứ hồi giữa hai máy chủ. Lưu ý rằng chương trình máy khách Traceroute phải có khả năng hướng dẫn hệ điều hành tạo các gói dữ liệu UDP với các giá trị TTL cụ thể và cũng phải có khả năng được hệ điều hành thông báo khi có tin nhắn ICMP đến. Bây giờ bạn đã hiểu cách Traceroute hoạt động, bạn có thể muốn quay lại và chơi với nó thêm nữa.

Phiên bản mới của ICMP đã được xác định cho IPv6 trong RFC 4443. Ngoài việc sắp xếp lại định nghĩa mã và loại ICMP hiện có, ICMPv6 cũng đã thêm các loại và mã mới theo yêu cầu của chức năng IPv6 mới. Chúng bao gồm loại "Packet Quá lớn" và mã lỗi "tùy chọn IPv6 không được nhận dạng".

**5.7 Quản lý mạng và SNMP, NETCONF/YANG**

Bây giờ chúng ta đã đi đến phần cuối của nghiên cứu về lớp mạng, chỉ có lớp liên kết trước mắt, chúng ta biết rõ rằng mạng bao gồm nhiều phần cứng và phần mềm tương tác phức tạp---từ các liên kết, bộ chuyển mạch, bộ định tuyến, máy chủ và các thiết bị khác bao gồm các thành phần vật lý của mạng cho đến nhiều giao thức kiểm soát và phối hợp các thiết bị này. Khi hàng trăm hoặc hàng nghìn thành phần như vậy được một tổ chức tập hợp lại với nhau để tạo thành một mạng, công việc của người quản trị mạng là duy trì mạng luôn "hoạt động" chắc chắn là một thách thức. Chúng ta đã thấy trong Phần 5.5 rằng bộ điều khiển tập trung về mặt logic có thể trợ giúp quá trình này trong ngữ cảnh SDN. Nhưng thách thức về quản lý mạng đã có từ rất lâu trước SDN, với bộ công cụ và phương pháp quản lý mạng phong phú giúp quản trị viên mạng giám sát, quản lý và kiểm soát mạng. Chúng ta sẽ nghiên cứu các công cụ và kỹ thuật này trong phần này, cũng như các công cụ và kỹ thuật mới đã cùng phát triển cùng với SDN.

Một câu hỏi thường gặp là "Quản lý mạng là gì?" Một định nghĩa rõ ràng, đơn giản (mặc dù một câu khá dài) về quản lý mạng từ \[Saydam 1996\] là:

Quản lý mạng bao gồm việc triển khai, tích hợp và phối hợp phần cứng, phần mềm và các yếu tố con người để giám sát, kiểm tra, thăm dò, định cấu hình, phân tích, đánh giá và kiểm soát mạng và tài nguyên phần tử để đáp ứng hiệu suất hoạt động, thời gian thực và các yêu cầu về Chất lượng dịch vụ với chi phí hợp lý.

Với định nghĩa rộng này, chúng tôi sẽ chỉ đề cập đến những điều cơ bản về quản lý mạng trong phần này---kiến trúc, giao thức và dữ liệu được mạng sử dụng.

người quản trị trong việc thực hiện nhiệm vụ của mình. Chúng tôi sẽ không đề cập đến quá trình ra quyết định của quản trị viên, trong đó các chủ đề như xác định lỗi \[Labovitz 1997; Steinder 2002; Feamster 2005; Ngô 2005; Teixeira 2006\], phát hiện dị thường \[Lakhina 2005; Barford 2009\], thiết kế/kỹ thuật mạng để đáp ứng các Thỏa thuận cấp độ dịch vụ theo hợp đồng (SLA) \[Huston 1999a\], v.v., sẽ được xem xét. Do đó, trọng tâm của chúng tôi là thu hẹp có mục đích; độc giả quan tâm nên tham khảo những tài liệu tham khảo này, những phần tổng quan tuyệt vời trong \[Subramanian 2000; Schonwalder 2010; Claise 2019\] và cách xử lý chi tiết hơn về quản lý mạng có sẵn trên trang Web dành cho văn bản này.

**5.7.1 Khung quản lý mạng**

Hình 5.20 cho thấy các thành phần chính của quản lý mạng:

• Quản lý máy chủ. Máy chủ quản lý là một ứng dụng, thường có các nhà quản lý mạng (con người) trong vòng lặp, chạy trong trạm quản lý mạng tập trung trong trung tâm điều hành mạng (NOC). Máy chủ quản lý là nơi hoạt động của quản lý mạng: nó kiểm soát việc thu thập, xử lý, phân tích và gửi thông tin và lệnh quản lý mạng. Tại đây, các hành động được bắt đầu để định cấu hình, giám sát và kiểm soát các thiết bị được quản lý của mạng. Trong thực tế, một mạng có thể có nhiều máy chủ quản lý như vậy. • Thiết bị được quản lý. Thiết bị được quản lý là một phần của thiết bị mạng (bao gồm cả phần mềm của nó) nằm trên mạng được quản lý. Thiết bị được quản lý có thể là máy chủ, bộ định tuyến, bộ chuyển mạch, hộp trung gian, modem, nhiệt kế hoặc thiết bị kết nối mạng khác. Bản thân thiết bị sẽ có nhiều thành phần có thể quản lý được (ví dụ: giao diện mạng chỉ là một thành phần của máy chủ hoặc bộ định tuyến) và các tham số cấu hình cho các thành phần phần cứng và phần mềm này (ví dụ: giao thức định tuyến nội bộ AS, chẳng hạn như OSPF). • Dữ liệu. Mỗi thiết bị được quản lý sẽ có dữ liệu, còn được gọi là "trạng thái", được liên kết với nó. Có một số loại dữ liệu khác nhau. Dữ liệu cấu hình là thông tin thiết bị được người quản lý mạng định cấu hình rõ ràng, ví dụ: địa chỉ IP do người quản lý chỉ định/cấu hình hoặc tốc độ giao diện cho giao diện thiết bị. Dữ liệu vận hành là thông tin mà thiết bị thu thập khi nó hoạt động, ví dụ: danh sách các láng giềng trực tiếp trong giao thức OSPF. Thống kê thiết bị là các chỉ báo trạng thái và số lượng được cập nhật dưới dạng người vận hành thiết bị (ví dụ: số lượng gói bị rớt trên một giao diện hoặc tốc độ quạt làm mát của thiết bị). Người quản lý mạng có thể truy vấn dữ liệu thiết bị từ xa và trong một số trường hợp, điều khiển thiết bị từ xa bằng cách ghi các giá trị dữ liệu thiết bị, như được thảo luận bên dưới. Như được hiển thị trong Hình 5.17, máy chủ quản lý cũng duy trì bản sao dữ liệu cấu hình, vận hành và thống kê của riêng nó từ các thiết bị được quản lý cũng như dữ liệu trên toàn mạng (ví dụ: cấu trúc liên kết của mạng). • Đại lý quản lý mạng. Tác nhân quản lý mạng là một quy trình phần mềm chạy trong thiết bị được quản lý, giao tiếp với máy chủ quản lý, thực hiện các hành động cục bộ tại thiết bị được quản lý dưới sự chỉ huy và kiểm soát của máy chủ quản lý. Tác nhân quản lý mạng tương tự như tác nhân định tuyến mà chúng ta đã thấy trong Hình 5.2.

• Giao thức quản lý mạng. Thành phần cuối cùng của khung quản lý mạng là giao thức quản lý mạng. Giao thức này chạy giữa máy chủ quản lý và các thiết bị được quản lý, cho phép máy chủ quản lý truy vấn trạng thái của các thiết bị được quản lý và thực hiện hành động tại các thiết bị này thông qua các đại lý của nó. Đại lý có thể sử dụng giao thức quản lý mạng để thông báo cho máy chủ quản lý về các sự kiện đặc biệt (ví dụ: lỗi thành phần hoặc vi phạm ngưỡng hiệu suất). Điều quan trọng cần lưu ý là giao thức quản lý mạng không tự quản lý mạng. Thay vào đó, nó cung cấp các khả năng mà người quản lý mạng có thể sử dụng để quản lý ("giám sát, kiểm tra, thăm dò ý kiến, định cấu hình, phân tích, đánh giá và kiểm soát") mạng. Đây là một sự khác biệt tinh tế nhưng quan trọng.

Trong thực tế, có ba cách thường được sử dụng để một nhà khai thác mạng có thể quản lý mạng, sử dụng các thành phần được mô tả ở trên:

• CLI. Nhà điều hành mạng có thể đưa ra lệnh Giao diện dòng lệnh (CLI) trực tiếp cho thiết bị. Các lệnh này có thể được nhập trực tiếp trên bảng điều khiển của thiết bị được quản lý (nếu người vận hành có mặt thực tế tại thiết bị) hoặc qua kết nối Telnet hoặc shell an toàn (SSH), có thể thông qua tập lệnh, giữa

*Hình 5.20 ♦ Các thành phần quản lý mạng*

Đại lý

Thiết bị

dữ liệu

Đại lý

Thiết bị

dữ liệu

Đại lý

Thiết bị

dữ liệu

Quản lý máy chủ/bộ điều khiển

Được quản lý

thiết bị

Được quản lý

thiết bị

Thiết bị được quản lý

Thiết bị được quản lý

Đại lý

Giao thức từ bộ điều khiển đến thiết bị Khóa:

Được quản lý

thiết bị

Người quản lý mạng

config. và dữ liệu vận hành

cửa hàng

Thiết bị

dữ liệu

Đại lý

Thiết bị

dữ liệu

quản lý máy chủ/bộ điều khiển và thiết bị được quản lý. Các lệnh CLI dành riêng cho nhà cung cấp và thiết bị và có thể khá phức tạp. Mặc dù các trình hướng dẫn mạng dày dạn kinh nghiệm có thể sử dụng CLI để định cấu hình hoàn hảo các thiết bị mạng nhưng việc sử dụng CLI dễ xảy ra lỗi và khó tự động hóa hoặc mở rộng quy mô một cách hiệu quả cho các mạng lớn. Các thiết bị mạng hướng đến người tiêu dùng, chẳng hạn như bộ định tuyến không dây tại nhà của bạn, có thể xuất menu quản lý mà bạn (người quản lý mạng!) có thể truy cập thông qua HTTP để định cấu hình thiết bị đó. Mặc dù phương pháp này có thể hoạt động tốt đối với các thiết bị đơn giản, đơn giản và ít xảy ra lỗi hơn CLI nhưng nó cũng không mở rộng được trên các mạng có quy mô lớn hơn. • SNMP/MIB. Theo phương pháp này, nhà điều hành mạng có thể truy vấn/đặt dữ liệu có trong các đối tượng Cơ sở thông tin quản lý (MIB) của thiết bị bằng cách sử dụng Giao thức quản lý mạng đơn giản (SNMP). Một số MIB dành riêng cho thiết bị và nhà cung cấp, trong khi các MIB khác (ví dụ: số lượng gói dữ liệu IP bị loại bỏ trên bộ định tuyến do lỗi trong tiêu đề gói dữ liệu IP hoặc số phân đoạn UDP nhận được tại máy chủ) không phụ thuộc vào thiết bị, cung cấp tính trừu tượng và tính tổng quát. Thông thường, nhà điều hành mạng sẽ sử dụng phương pháp này để truy vấn và giám sát trạng thái hoạt động cũng như số liệu thống kê của thiết bị, sau đó sử dụng CLI để chủ động kiểm soát/định cấu hình thiết bị. Điều quan trọng là chúng tôi lưu ý rằng cả hai phương pháp đều quản lý các thiết bị riêng lẻ. Chúng tôi sẽ đề cập đến SNMP và MIB, đã được sử dụng từ cuối những năm 1980, trong Phần 5.7.2 bên dưới. Một hội thảo quản lý mạng do Ban Kiến trúc Internet triệu tập vào năm 2002 \[RFC 3535\] đã ghi nhận không chỉ giá trị của phương pháp SNMP/MIB trong việc giám sát thiết bị mà còn lưu ý những thiếu sót của nó, đặc biệt đối với cấu hình thiết bị và quản lý mạng ở quy mô lớn. Điều này đã tạo ra cách tiếp cận gần đây nhất để quản lý mạng, sử dụng NETCONF và YANG. • NETCONF/YANG. Cách tiếp cận NETCONF/YANG có cái nhìn trừu tượng hơn, toàn mạng và toàn diện hơn đối với việc quản lý mạng, với sự nhấn mạnh hơn nhiều vào quản lý cấu hình, bao gồm chỉ định các ràng buộc về tính chính xác và cung cấp các hoạt động quản lý nguyên tử trên nhiều thiết bị được kiểm soát. YANG \[RFC 6020\] là ngôn ngữ mô hình hóa dữ liệu được sử dụng để mô hình hóa dữ liệu cấu hình và vận hành. Giao thức NETCONF \[RFC 6241\] được sử dụng để truyền đạt các hành động và dữ liệu tương thích với YANG đến/từ/giữa các thiết bị từ xa. Chúng tôi đã gặp nhanh NETCONF và YANG trong nghiên cứu điển hình về Bộ điều khiển OpenDaylight trong Hình 5.17 và sẽ nghiên cứu chúng trong Phần 5.7.3 bên dưới.

**5.7.2 Giao thức quản lý mạng đơn giản (SNMP) và Cơ sở thông tin quản lý (MIB)**

Giao thức quản lý mạng đơn giản phiên bản 3 (SNMPv3) \[RFC 3410\] là giao thức lớp ứng dụng được sử dụng để truyền tải các thông báo thông tin và điều khiển quản lý mạng giữa máy chủ quản lý và tác nhân thực thi thay mặt cho máy chủ quản lý đó. Cách sử dụng SNMP phổ biến nhất là ở chế độ phản hồi yêu cầu trong đó máy chủ quản lý SNMP gửi yêu cầu đến tác nhân SNMP, người này sẽ

nhận được yêu cầu, thực hiện một số hành động và gửi phản hồi cho yêu cầu. Thông thường, một yêu cầu sẽ được sử dụng để truy vấn (truy xuất) hoặc sửa đổi (đặt) các giá trị đối tượng MIB được liên kết với thiết bị được quản lý. Cách sử dụng phổ biến thứ hai của SNMP là để một tác nhân gửi một tin nhắn không được yêu cầu, được gọi là tin nhắn bẫy, đến máy chủ quản lý. Thông báo bẫy được sử dụng để thông báo cho máy chủ quản lý về một tình huống đặc biệt (ví dụ: giao diện liên kết tăng hoặc giảm) dẫn đến thay đổi giá trị đối tượng MIB.

Các đối tượng MIB được chỉ định bằng ngôn ngữ mô tả dữ liệu được gọi là SMI (Cấu trúc thông tin quản lý) \[RFC 2578; RFC 2579; RFC 2580\], một thành phần được đặt tên khá kỳ lạ trong khung quản lý mạng mà tên của nó không gợi ý gì về chức năng của nó. Ngôn ngữ định nghĩa chính thức được sử dụng để đảm bảo rằng cú pháp và ngữ nghĩa của dữ liệu quản lý mạng được xác định rõ ràng và rõ ràng. Các đối tượng MIB liên quan được tập hợp thành các mô-đun MIB. Tính đến cuối năm 2019, có hơn 400 RFC liên quan đến MIB và số lượng mô-đun MIB dành riêng cho nhà cung cấp (riêng tư) lớn hơn nhiều.

SNMPv3 định nghĩa bảy loại bản tin, thường được gọi là đơn vị dữ liệu giao thức---PDU---như được hiển thị trong Bảng 5.2 và được mô tả bên dưới. Định dạng của PDU được thể hiện trong Hình 5.21.

• Các PDU GetRequest, GetNextRequest và GetBulkRequest đều được gửi từ máy chủ quản lý đến tác nhân để yêu cầu giá trị của một hoặc nhiều

Bảng 5.2 ♦ Các loại PDU SNMPv3

SNMPv3 PDU Loại Người gửi-người nhận Mô tả

GetRequest manager-to-agent lấy giá trị của một hoặc nhiều phiên bản đối tượng MIB GetNextRequest manager-to-agent lấy giá trị của phiên bản đối tượng MIB tiếp theo trong danh sách hoặc bảng GetBulkRequest manager-to-agent lấy các giá trị trong khối dữ liệu lớn, ví dụ: các giá trị trong một bảng lớn InformRequest manager-to-manager thông báo cho thực thể quản lý từ xa về các giá trị MIB từ xa quyền truy cập của nó đáp lại

GetRequest từ người quản lý đến người quản lý,

GetNextRequest,

NhậnBulkRequest,

SetRequest PDU hoặc InformRequest

SNMPv2-Trap giữa tác nhân với người quản lý thông báo cho người quản lý về một sự kiện đặc biệt \#

Đối tượng MIB tại thiết bị được quản lý của đại lý. The MIB objects whose values are being requested are specified in the variable binding portion of the PDU. GetRequest, GetNextRequest, and GetBulkRequest differ in the granularity of their data requests. GetRequest can request an arbitrary set of MIB values; multiple GetNextRequests can be used to sequence through a list or table of MIB objects; GetBulkRequest cho phép trả về một khối dữ liệu lớn, tránh chi phí phát sinh nếu gửi nhiều tin nhắn GetRequest hoặc GetNextRequest. In all three cases, the agent responds with a Response PDU containing the object identifiers and their associated values. • The SetRequest PDU is used by a managing server to set the value of one or more MIB objects in a managed device. An agent replies with a Response PDU with the "noError" error status to confirm that the value has indeed been set. • InformRequest PDU được máy chủ quản lý sử dụng để thông báo cho máy chủ quản lý khác về thông tin MIB ở xa máy chủ nhận. • PDU phản hồi thường được gửi từ một thiết bị được quản lý đến máy chủ quản lý để phản hồi thông báo yêu cầu từ máy chủ đó, trả về thông tin được yêu cầu. • The final type of SNMPv3 PDU is the trap message. Thông báo bẫy được tạo không đồng bộ; nghĩa là, chúng không được tạo để đáp lại yêu cầu đã nhận mà để đáp lại một sự kiện mà máy chủ quản lý yêu cầu thông báo. RFC 3418 xác định các loại bẫy phổ biến bao gồm thiết bị khởi động nguội hoặc ấm, liên kết tăng hoặc giảm, mất hàng xóm hoặc sự kiện lỗi xác thực. A received trap request has no required response from a managing server.

*Hình 5.21 ♦ Định dạng SNMP PDU*

Loại PDU (0--3)

Lời yêu cầu

Nhận dạng

Trạng thái lỗi

(0--5)

Tên chỉ mục lỗi

Tên giá trị

Giá trị tên

Loại PDU

\(4\)

Đại lý doanh nghiệp

địa chỉ

Loại bẫy (0--7)

cụ thể

mã số

Dấu thời gian

Giá trị

Nhận/đặt tiêu đề

Tiêu đề bẫy Thông tin bẫy

PDU SNMP

Các biến cần lấy/đặt

Do tính chất đáp ứng yêu cầu của SNMP, điều đáng lưu ý ở đây là mặc dù các PDU SNMP có thể được truyền qua nhiều giao thức truyền tải khác nhau, nhưng SNMP PDU thường được truyền dưới dạng tải trọng của gói dữ liệu UDP. Thật vậy, RFC 3417 tuyên bố rằng UDP là "bản đồ giao thông ưu tiên". Tuy nhiên, vì UDP là giao thức truyền tải không đáng tin cậy nên không có gì đảm bảo rằng yêu cầu hoặc phản hồi của nó sẽ được nhận tại đích đã định. Trường ID yêu cầu của PDU (xem Hình 5.21) được máy chủ quản lý sử dụng để đánh số các yêu cầu của nó tới một tác nhân; phản hồi của tác nhân lấy ID yêu cầu của nó từ yêu cầu nhận được. Do đó, trường ID yêu cầu có thể được máy chủ quản lý sử dụng để phát hiện các yêu cầu hoặc phản hồi bị mất. Máy chủ quản lý có quyền quyết định có truyền lại yêu cầu hay không nếu không nhận được phản hồi tương ứng sau một khoảng thời gian nhất định. Đặc biệt, tiêu chuẩn SNMP không yêu cầu bất kỳ quy trình cụ thể nào để truyền lại hoặc ngay cả khi việc truyền lại phải được thực hiện ngay từ đầu. Nó chỉ yêu cầu máy chủ quản lý "cần hành động có trách nhiệm đối với tần suất và thời lượng truyền lại". Tất nhiên, điều này khiến người ta tự hỏi một giao thức "có trách nhiệm" sẽ hoạt động như thế nào!

SNMP đã phát triển qua ba phiên bản. Các nhà thiết kế của SNMPv3 đã nói rằng "SNMPv3 có thể được coi là SNMPv2 với các khả năng quản trị và bảo mật bổ sung" \[RFC 3410\]. Chắc chắn, có những thay đổi trong SNMPv3 so với SNMPv2, nhưng không nơi nào những thay đổi đó rõ ràng hơn trong lĩnh vực quản trị và bảo mật. Vai trò trung tâm của bảo mật trong SNMPv3 đặc biệt quan trọng, vì việc thiếu bảo mật đầy đủ dẫn đến việc SNMP được sử dụng chủ yếu để giám sát hơn là kiểm soát (ví dụ: SetRequest hiếm khi được sử dụng trong SNMPv1). Một lần nữa, chúng ta thấy rằng vấn đề bảo mật - chủ đề mà chúng ta sẽ đề cập chi tiết trong Chương 8 - là mối quan tâm đặc biệt, nhưng một lần nữa, mối quan tâm mà tầm quan trọng của nó đã được nhận ra có lẽ hơi muộn và chỉ sau đó mới được "thêm vào".

Cơ sở thông tin quản lý (MIB)

Trước đó chúng ta đã biết rằng dữ liệu trạng thái hoạt động của thiết bị được quản lý (và ở một mức độ nào đó là dữ liệu cấu hình của thiết bị đó) theo phương pháp SNMP/MIB để quản lý mạng được biểu diễn dưới dạng các đối tượng được tập hợp lại với nhau thành MIB cho thiết bị đó. Một đối tượng MIB có thể là một bộ đếm, chẳng hạn như số lượng gói dữ liệu IP bị loại bỏ tại bộ định tuyến do lỗi trong tiêu đề gói dữ liệu IP; hoặc số lỗi cảm nhận sóng mang trong thẻ giao diện Ethernet; thông tin mô tả chẳng hạn như phiên bản phần mềm đang chạy trên máy chủ DNS; thông tin trạng thái như liệu một thiết bị cụ thể có hoạt động chính xác hay không; hoặc thông tin dành riêng cho giao thức như đường dẫn định tuyến đến đích. Các đối tượng MIB liên quan được tập hợp thành các mô-đun MIB. Có hơn 400 mô-đun MIB được xác định trong nhiều RFC của IETC; có nhiều MIB dành riêng cho thiết bị và nhà cung cấp hơn. \[RFC 4293\] chỉ định mô-đun MIB xác định các đối tượng được quản lý (bao gồm ipSystemStatsInDelivers) để quản lý việc triển khai Giao thức Internet (IP) và Giao thức thông báo điều khiển Internet liên quan của nó (ICMP). \[RFC 4022\] chỉ định mô-đun MIB cho TCP và \[RFC 4113\] chỉ định mô-đun MIB cho UDP.

Mặc dù các RFC liên quan đến MIB khiến việc đọc khá tẻ nhạt và khô khan, nhưng dù sao cũng mang tính hướng dẫn (tức là, giống như ăn rau, \"tốt cho bạn\") để xem xét một ví dụ về đối tượng MIB, Định nghĩa loại đối tượng ipSystem-StatsInDelivers từ \[RFC 4293\] xác định bộ đếm chỉ đọc 32 bit theo dõi số lượng gói dữ liệu IP đã nhận được tại thiết bị được quản lý và được gửi thành công tới một thiết bị giao thức lớp trên. Trong ví dụ bên dưới, Counter32 là một trong những kiểu dữ liệu cơ bản được xác định trong SMI.

ipSystemStatsInCung cấp cú pháp LOẠI ĐỐI TƯỢNG Bộ đếm32 TỐI ĐA TRUY CẬP chỉ đọc TRẠNG THÁI hiện tại MÔ TẢ "Tổng số gói dữ liệu được loại bỏ thành công

phù hợp với giao thức người dùng IP (bao gồm ICMP).

Khi theo dõi số liệu thống kê giao diện,

ter của giao diện mà các datagram này được đánh địa chỉ sẽ được tăng lên. Giao diện này có thể không giống với giao diện đầu vào của một số datagram.

Sự gián đoạn trong giá trị của bộ đếm này có thể

xảy ra khi khởi tạo lại hệ thống quản lý và vào các thời điểm khác được biểu thị bằng giá trị của ipSystemStatsDiscontinuityTime."

::= { ipSystemStatsEntry 18 }

**5.7.3 Giao thức cấu hình mạng (NETCONF) và YANG**

Giao thức NETCONF hoạt động giữa máy chủ quản lý và các thiết bị mạng được quản lý, cung cấp tin nhắn để (i) truy xuất, thiết lập và sửa đổi dữ liệu cấu hình tại các thiết bị được quản lý; (ii) truy vấn dữ liệu và số liệu thống kê vận hành tại các thiết bị được quản lý; và (iii) đăng ký nhận thông báo do thiết bị được quản lý tạo ra. Máy chủ quản lý chủ động kiểm soát thiết bị được quản lý bằng cách gửi cấu hình cho thiết bị đó, được chỉ định trong tài liệu XML có cấu trúc và kích hoạt cấu hình tại thiết bị được quản lý. NETCONF sử dụng mô hình cuộc gọi thủ tục từ xa (RPC), trong đó các thông báo giao thức cũng được mã hóa bằng XML và được trao đổi giữa máy chủ quản lý và thiết bị được quản lý qua phiên hướng kết nối, an toàn, chẳng hạn như giao thức TLS (Transport Layer Bảo mật) (được thảo luận trong Chương 8) qua TCP.

Hình 5.22 cho thấy một phiên NETCONF mẫu. Đầu tiên, máy chủ quản lý thiết lập kết nối an toàn với thiết bị được quản lý. (Theo cách nói của NETCONF, máy chủ quản lý thực sự được gọi là "máy khách" và thiết bị được quản lý là "máy chủ", vì máy chủ quản lý thiết lập kết nối đến thiết bị được quản lý. Nhưng chúng ta sẽ bỏ qua điều đó ở đây để thống nhất với thuật ngữ máy chủ/máy khách quản lý mạng lâu đời hơn được hiển thị trong Hình 5.20.) Khi một kết nối an toàn đã được thiết lập, máy chủ quản lý và thiết bị được quản lý trao đổi các thông báo \<hello\>, khai báo "khả năng" của chúng---chức năng NETCONF bổ sung cho đặc tả NETCONF cơ sở trong \[RFC 6241\]. Tương tác giữa máy chủ quản lý và thiết bị được quản lý có dạng cuộc gọi thủ tục từ xa, sử dụng thông báo \<rpc\> và \<rpc-response\>. Những tin nhắn này được sử dụng để truy xuất, thiết lập, truy vấn và sửa đổi cấu hình thiết bị, dữ liệu và thống kê vận hành cũng như đăng ký nhận thông báo của thiết bị. Bản thân thông báo thiết bị được chủ động gửi từ thiết bị được quản lý đến máy chủ quản lý bằng thông báo NETCONF \<notification\>. Một phiên được đóng lại với \<thông báo đóng phiên\>.

*Hình 5.22 ♦ Phiên NETCONF giữa việc quản lý máy chủ/bộ điều khiển*

và thiết bị được quản lý

Bắt đầu phiên, trao đổi khả năng: \<hello\>

Phiên đóng: \<close-session\>

\<rpc\> \<rpc-trả lời\>

\<thông báo\>

Đại lý

Thiết bị

dữ liệu

Quản lý máy chủ/bộ điều khiển

\<rpc\>

\<rpc\>

\<rpc-trả lời\>

\<rpc-trả lời\>

config. và dữ liệu vận hành

cửa hàng

Bảng 5.3 cho thấy một số hoạt động NETCONF quan trọng mà máy chủ quản lý có thể thực hiện trên thiết bị được quản lý. Như trong trường hợp SNMP, chúng tôi thấy các hoạt động truy xuất dữ liệu trạng thái hoạt động (\<get\>) và thông báo sự kiện. Tuy nhiên, thao tác \<get-config\>, \<edit-config\>, \<lock\> và \<unlock\> thể hiện sự chú trọng đặc biệt của NETCONF vào cấu hình thiết bị. Bằng cách sử dụng các thao tác cơ bản được trình bày trong Bảng 5.3, cũng có thể tạo một tập hợp các giao dịch quản lý mạng phức tạp hơn hoàn thành một cách nguyên tử (tức là như một nhóm) và thành công trên một bộ thiết bị hoặc bị đảo ngược hoàn toàn và để các thiết bị ở trạng thái trước giao dịch. Các giao dịch đa thiết bị như vậy---"cho phép các nhà khai thác \[ing\] tập trung vào cấu hình của toàn bộ mạng thay vì các thiết bị riêng lẻ" là một yêu cầu quan trọng dành cho nhà khai thác được đưa ra trong \[RFC 3535\].

Mô tả đầy đủ về NETCONF nằm ngoài phạm vi của chúng tôi ở đây; \[RFC 6241, RFC 5277, Claise 2019; Schonwalder 2010\] cung cấp thông tin chi tiết hơn. Nhưng vì đây là lần đầu tiên chúng ta thấy các thông báo giao thức được định dạng dưới dạng tài liệu XML (chứ không phải thông báo truyền thống với các trường tiêu đề và nội dung thông báo, ví dụ như trong Hình 5.21 cho SNMP PDU), hãy kết thúc nghiên cứu ngắn gọn của chúng ta về NETCONF bằng hai ví dụ.

Trong ví dụ đầu tiên, tài liệu XML được gửi từ máy chủ quản lý đến thiết bị được quản lý là lệnh NETCONF \<get\> yêu cầu tất cả cấu hình thiết bị

Bảng 5.3 ♦ Các thao tác NETCONF đã chọn

Mô tả hoạt động NETCONF

\<get-config\> Truy xuất tất cả hoặc một phần cấu hình nhất định. Một thiết bị có thể có nhiều cấu hình. Luôn có cấu hình đang chạy/đang chạy mô tả cấu hình (đang chạy) hiện tại của thiết bị.

\<get\> Truy xuất tất cả hoặc một phần dữ liệu trạng thái cấu hình và trạng thái vận hành.

\<edit-config\> Thay đổi tất cả hoặc một phần cấu hình được chỉ định tại thiết bị được quản lý. Nếu việc chạy/cấu hình được chỉ định thì cấu hình (đang chạy) hiện tại của thiết bị sẽ được thay đổi. Nếu thiết bị được quản lý có thể đáp ứng yêu cầu, \<rpc-reply\> sẽ được gửi có chứa phần tử \<ok\>; nếu không thì phản hồi \<rpcerror\> sẽ được trả về. Nếu có lỗi, trạng thái cấu hình của thiết bị có thể được khôi phục về trạng thái trước đó.

\<lock\>, \<unlock\> Thao tác \<lock\> (\<unlock\>) cho phép máy chủ quản lý khóa (mở khóa) toàn bộ hệ thống kho dữ liệu cấu hình của một thiết bị được quản lý. Khóa nhằm mục đích tồn tại trong thời gian ngắn và cho phép khách hàng thực hiện thay đổi mà không sợ tương tác với các lệnh NETCONF, SNMP hoặc CLI khác từ các nguồn khác.

\<tạo-đăng ký\> ,

\<thông báo\>

Thao tác này bắt đầu đăng ký thông báo sự kiện sẽ gửi \<thông báo\> sự kiện không đồng bộ cho các sự kiện quan tâm được chỉ định từ thiết bị được quản lý đến máy chủ quản lý cho đến khi đăng ký bị chấm dứt.

và dữ liệu vận hành. Với lệnh này, máy chủ có thể tìm hiểu về cấu hình của thiết bị.

01 \<?xml version="1.0" mã hóa="UTF-8"?\> 02 \<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"\> \<get/\> 05 \</rpc\>

Mặc dù ít người có thể phân tích cú pháp XML trực tiếp một cách hoàn toàn, nhưng chúng tôi thấy rằng lệnh NETCONF tương đối dễ đọc và gợi nhớ đến HTTP và HTML hơn là các định dạng thông báo giao thức mà chúng tôi đã thấy đối với định dạng SNMP PDU trong Hình 5.21. Bản thân thông báo RPC trải dài từ dòng 02--05 (chúng tôi đã thêm số dòng ở đây vì mục đích sư phạm). RPC có giá trị ID thông báo là 101, được khai báo ở dòng 02 và chứa một lệnh NETCONF \<get\>. Phản hồi từ thiết bị chứa số ID phù hợp (101) và tất cả dữ liệu cấu hình của thiết bị (tất nhiên là ở định dạng XML), bắt đầu từ dòng 04, cuối cùng là đóng \</rpc-reply\>.

01 \<?xml version="1.0" mã hóa="UTF-8"?\> 02 \<rpc-reply message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"\> \<!\-- . . . tất cả dữ liệu cấu hình được trả về\... \--\>  . . .  \</rpc-trả lời\>

Trong ví dụ thứ hai bên dưới, được điều chỉnh từ \[RFC 6241\], tài liệu XML được gửi từ máy chủ quản lý đến thiết bị được quản lý sẽ đặt Đơn vị truyền tối đa (MTU) của giao diện có tên "Ethernet0/0" thành 1500 byte:

01 \<?xml version="1.0" mã hóa="UTF-8"?\> 02 \<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"\> \<edit-config\> \<target\> \<running/\> \</target\> \<configig\> \<top xmlns="http://example.com/schema/ 1.2/configig"\> \<interface\> \<name\>Ethernet0/0\</name\> \<mtu\>1500\</mtu\> \</interface\> \</top\> \</config\> \</edit-config\> 17 \</rpc\>

Bản thân thông báo RPC trải dài từ các dòng 02--17, có giá trị ID thông báo là 101 và chứa một lệnh NETCONF \<edit-config\> duy nhất, trải dài các dòng 04--15. Dòng 06 cho biết cấu hình thiết bị đang chạy tại thiết bị được quản lý sẽ được thay đổi. Dòng 11 và 12 chỉ định kích thước MTU được đặt cho giao diện Ethernet0/0.

Khi thiết bị được quản lý đã thay đổi kích thước MTU của giao diện trong cấu hình, thiết bị sẽ phản hồi lại máy chủ quản lý bằng một phản hồi OK (dòng 04 bên dưới), một lần nữa trong tài liệu XML:

01 \<?xml version="1.0" mã hóa="UTF-8"?\> 02 \<rpc-reply message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"\> \<ok/\> \</rpc-reply\>

yang

YANG là ngôn ngữ mô hình hóa dữ liệu được sử dụng để xác định chính xác cấu trúc, cú pháp và ngữ nghĩa của dữ liệu quản lý mạng được NETCONF sử dụng, giống như cách SMI được sử dụng để chỉ định MIB trong SNMP. Tất cả các định nghĩa YANG đều được chứa trong các mô-đun và một tài liệu XML mô tả thiết bị cũng như các khả năng của nó có thể được tạo ra từ mô-đun YANG.

YANG có một tập hợp nhỏ các kiểu dữ liệu tích hợp (như trong trường hợp SMI) và cũng cho phép các nhà lập mô hình dữ liệu thể hiện các ràng buộc phải được thỏa mãn bởi cấu hình NETCONF hợp lệ---một sự trợ giúp mạnh mẽ trong việc giúp đảm bảo rằng các cấu hình NETCONF đáp ứng các ràng buộc về tính chính xác và nhất quán được chỉ định. YANG cũng được sử dụng để chỉ định thông báo NETCONF.

Một cuộc thảo luận đầy đủ hơn về YANG nằm ngoài phạm vi của chúng tôi ở đây. Để biết thêm thông tin, chúng tôi giới thiệu độc giả quan tâm đến cuốn sách xuất sắc \[Claise 2019\].

**5.8 Tóm tắt**

Bây giờ chúng ta đã hoàn thành hành trình hai chương vào lõi mạng---một hành trình bắt đầu bằng nghiên cứu của chúng ta về mặt phẳng dữ liệu của lớp mạng trong Chương 4 và kết thúc ở đây với nghiên cứu của chúng ta về mặt phẳng điều khiển của lớp mạng. Chúng ta đã biết rằng mặt phẳng điều khiển là logic toàn mạng, không chỉ kiểm soát cách một gói dữ liệu được chuyển tiếp giữa các bộ định tuyến dọc theo đường dẫn từ đầu đến cuối từ máy chủ nguồn đến máy chủ đích mà còn kiểm soát cách cấu hình và quản lý các thành phần và dịch vụ của lớp mạng.

Chúng tôi đã biết rằng có hai cách tiếp cận rộng rãi trong việc xây dựng mặt phẳng điều khiển: điều khiển truyền thống trên mỗi bộ định tuyến (trong đó thuật toán định tuyến chạy trong mỗi bộ định tuyến và thành phần định tuyến trong bộ định tuyến giao tiếp với các thành phần định tuyến trong các bộ định tuyến khác) và điều khiển mạng được xác định bằng phần mềm (SDN) (trong đó bộ điều khiển tập trung hợp lý tính toán và phân phối các bảng chuyển tiếp sẽ được mỗi bộ định tuyến sử dụng). Chúng tôi đã nghiên cứu hai thuật toán định tuyến cơ bản để tính toán các đường dẫn có chi phí thấp nhất trong biểu đồ---định tuyến trạng thái liên kết và định tuyến vectơ khoảng cách---trong Phần 5.2;

CÁC BÀI TẬP VÀ CÂU HỎI về bài tập về nhà 437

các thuật toán này tìm thấy ứng dụng trong cả điều khiển trên mỗi bộ định tuyến và điều khiển SDN. Các thuật toán này là cơ sở cho hai giao thức định tuyến Internet được triển khai rộng rãi, OSPF và BGP, mà chúng tôi đã đề cập trong Phần 5.3 và 5.4. Chúng tôi đã đề cập đến cách tiếp cận SDN đối với mặt phẳng điều khiển lớp mạng trong Phần 5.5, nghiên cứu các ứng dụng điều khiển mạng SDN, bộ điều khiển SDN và giao thức OpenFlow để liên lạc giữa bộ điều khiển và các thiết bị được điều khiển SDN. Trong Phần 5.6 và 5.7, chúng ta đã đề cập đến một số điểm cơ bản về quản lý mạng IP: ICMP (Giao thức thông báo điều khiển Internet) và quản lý mạng bằng SNMP và NETCONF/YANG.

Sau khi hoàn thành nghiên cứu về lớp mạng, hành trình của chúng ta giờ đây sẽ đưa chúng ta tiến thêm một bước nữa xuống ngăn xếp giao thức, cụ thể là đến lớp liên kết. Giống như lớp mạng, lớp liên kết là một phần của mỗi thiết bị được kết nối mạng. Nhưng chúng ta sẽ thấy trong chương tiếp theo rằng lớp liên kết có nhiệm vụ cục bộ hơn nhiều là di chuyển các gói giữa các nút trên cùng một liên kết hoặc mạng LAN. Mặc dù nhiệm vụ này nhìn bề ngoài có vẻ khá đơn giản so với nhiệm vụ của lớp mạng, nhưng chúng ta sẽ thấy rằng lớp liên kết liên quan đến một số vấn đề quan trọng và hấp dẫn có thể khiến chúng ta bận rộn trong một thời gian dài.

**Bài tập về nhà vấn đề và câu hỏi**

Câu hỏi ôn tập chương 5

MỤC 5.1 R1. Mặt phẳng điều khiển dựa trên điều khiển trên mỗi bộ định tuyến có nghĩa là gì? Trong đó

Trong các trường hợp, khi chúng tôi nói rằng các mặt phẳng dữ liệu và điều khiển mạng được triển khai "nguyên khối", chúng tôi muốn nói gì? R2. Mặt phẳng điều khiển dựa trên cơ chế tập trung logic có nghĩa là gì?

điều khiển? Trong những trường hợp như vậy, mặt phẳng dữ liệu và mặt phẳng điều khiển được triển khai trong cùng một thiết bị hay trong các thiết bị riêng biệt? Giải thích.

MỤC 5.2 R3. So sánh các thuộc tính của định tuyến tập trung và định tuyến phân tán

thuật toán. Cho một ví dụ về giao thức định tuyến có cách tiếp cận tập trung và phi tập trung. R4. So sánh và đối chiếu các thuật toán định tuyến trạng thái liên kết và vectơ khoảng cách. R5. Vấn đề "đếm đến vô cùng" trong định tuyến vectơ khoảng cách là gì? R6. Có nhất thiết mọi hệ thống tự trị đều sử dụng cùng một định tuyến nội bộ AS không?

thuật toán? Tại sao hoặc tại sao không?

PHẦN 5.3--5.4 R7. Tại sao các giao thức inter-AS và Intra-AS khác nhau được sử dụng trên Internet? R8. Đúng hay sai: Khi tuyến OSPF gửi thông tin trạng thái liên kết của nó, nó sẽ được gửi

chỉ với những nút hàng xóm được gắn trực tiếp. Giải thích.

R9. Một khu vực trong hệ thống tự trị OSPF có nghĩa là gì? Tại sao là

khái niệm về diện tích được giới thiệu? R10. Xác định và đối chiếu các thuật ngữ sau: mạng con, tiền tố và tuyến BGP. R11. BGP sử dụng thuộc tính NEXT-HOP như thế nào? Nó sử dụng AS-PATH như thế nào

thuộc tính? R12. Mô tả cách quản trị viên mạng của ISP cấp cao hơn có thể triển khai

chính sách khi định cấu hình BGP. R13. Đúng hay sai: Khi bộ định tuyến BGP nhận được đường dẫn được quảng cáo từ bộ định tuyến lân cận của nó

bor, nó phải thêm danh tính riêng của mình vào đường dẫn đã nhận và sau đó gửi đường dẫn mới đó đến tất cả các hàng xóm của nó. Giải thích.

MỤC 5.5 R14. Mô tả vai trò chính của lớp truyền thông, trạng thái toàn mạng

lớp quản lý và lớp ứng dụng điều khiển mạng trong bộ điều khiển SDN. R15. Giả sử bạn muốn triển khai giao thức định tuyến mới trong điều khiển SDN

máy bay. Bạn sẽ triển khai giao thức đó ở lớp nào? Giải thích. R16. Những loại tin nhắn nào truyền qua hướng bắc và hướng bắc của bộ điều khiển SDN

API hướng nam? Ai là người nhận các tin nhắn này được gửi từ bộ điều khiển qua giao diện hướng nam và ai gửi tin nhắn đến bộ điều khiển qua giao diện hướng bắc? R17. Mô tả mục đích của hai loại thông báo OpenFlow (bạn chọn)

được gửi từ thiết bị được điều khiển đến bộ điều khiển. Mô tả mục đích của hai loại thông báo Openflow (do bạn chọn) được gửi từ bộ điều khiển đến thiết bị được điều khiển. R18. Mục đích của lớp trừu tượng hóa dịch vụ trong OpenDaylight SDN là gì

bộ điều khiển?

MỤC 5.6--5.7 R19. Kể tên bốn loại tin nhắn ICMP khác nhau R20. Hai loại tin nhắn ICMP nào được nhận tại máy chủ gửi đang thực thi

chương trình Traceroute? R21. Xác định các thuật ngữ sau trong ngữ cảnh của SNMP: máy chủ quản lý,

thiết bị được quản lý, tác nhân quản lý mạng và MIB. R22. Mục đích của các thông báo SNMP GetRequest và SetRequest là gì? R23. Mục đích của thông báo bẫy SNMP là gì?

VẤN ĐỀ 439

**Vấn đề**

P1. Nhìn vào Hình 5.3, liệt kê các đường đi từ y tới u không chứa

bất kỳ vòng lặp nào. P2. Lặp lại bài toán P1 cho các đường dẫn từ x đến z, z đến u và z đến w. P3. Hãy xem xét mạng sau đây. Với chi phí liên kết được chỉ định, hãy sử dụng Dijkstra\'s

thuật toán đường đi ngắn nhất để tính toán đường đi ngắn nhất từ ​​x đến tất cả các nút mạng. Hãy trình bày cách thức hoạt động của thuật toán bằng cách tính toán một bảng tương tự như Bảng 5.1.

x

v

bạn

z

bạn

w

P4. Xét mạng ở bài toán P3. Sử dụng thuật toán Dijkstra và

hiển thị bài làm của bạn bằng bảng tương tự như Bảng 5.1, hãy làm như sau: a. Tính đường đi ngắn nhất từ ​​t đến tất cả các nút mạng. b. Tính đường đi ngắn nhất từ ​​u đến tất cả các nút mạng. c. Tính đường đi ngắn nhất từ ​​v đến tất cả các nút mạng. d. Tính đường đi ngắn nhất từ ​​w tới tất cả các nút mạng. đ. Tính đường đi ngắn nhất từ ​​y đến tất cả các nút mạng. f. Tính đường đi ngắn nhất từ ​​z đến tất cả các nút mạng. P5. Hãy xem xét mạng được hiển thị bên dưới và giả sử rằng mỗi nút ban đầu

biết chi phí của mỗi hàng xóm của nó. Hãy xem xét thuật toán vectơ khoảng cách và hiển thị các mục trong bảng khoảng cách tại nút z.

bạn

z

v

y

x

Thuật toán Dijkstra: thảo luận và ví dụ

VideoLưu ý

P6. Hãy xem xét một cấu trúc liên kết chung (nghĩa là không phải mạng cụ thể được hiển thị ở trên) và một

phiên bản đồng bộ của thuật toán vectơ khoảng cách. Giả sử rằng tại mỗi lần lặp, một nút trao đổi vectơ khoảng cách của nó với các nút lân cận và nhận vectơ khoảng cách của chúng. Giả sử rằng thuật toán bắt đầu với mỗi nút chỉ biết chi phí cho các nút lân cận của nó, thì số lần lặp tối đa cần thiết trước khi thuật toán phân tán hội tụ là bao nhiêu? Biện minh cho câu trả lời của bạn. P7. Hãy xem xét đoạn mạng được hiển thị bên dưới. x chỉ có hai hàng xóm kèm theo

bor, w và y. w có đường dẫn có chi phí tối thiểu đến đích u (không được hiển thị) là 5 và y có đường dẫn có chi phí tối thiểu đến u là 6. Các đường dẫn đầy đủ từ w và y đến u (và giữa w và y) không được hiển thị. Tất cả chi phí liên kết trong mạng đều có giá trị nguyên dương.

x y

w

Một. Cho vectơ khoảng cách của x cho các điểm đến w, y và u. b. Đưa ra một thay đổi về chi phí liên kết cho c(x,w) hoặc c(x,y) sao cho x sẽ thông báo

các láng giềng của nó trên một đường đi có chi phí tối thiểu mới tới u nhờ thực hiện thuật toán vectơ khoảng cách. c. Đưa ra một thay đổi về chi phí liên kết cho c(x,w) hoặc c(x,y) sao cho x sẽ không

thông báo cho các hàng xóm của nó về đường đi có chi phí tối thiểu mới tới u nhờ thực hiện thuật toán vectơ khoảng cách. P8. Hãy xem xét cấu trúc liên kết ba nút được hiển thị trong Hình 5.6. Thay vì có

chi phí liên kết được hiển thị trong Hình 5.6, chi phí liên kết là c(x,y) = 3, c(y,z) = 6, c(z,x) = 4. Tính bảng khoảng cách sau bước khởi tạo và sau mỗi lần lặp của phiên bản đồng bộ của thuật toán vectơ khoảng cách (như chúng ta đã làm trong phần thảo luận trước đây về Hình 5.6). P9. Xét bài toán đếm đến vô cùng trong định tuyến vectơ khoảng cách. Sẽ

vấn đề đếm đến vô cùng xảy ra nếu chúng ta giảm chi phí của một liên kết? Tại sao? Sẽ thế nào nếu chúng ta kết nối hai nút không có liên kết? P10. Lập luận rằng đối với thuật toán vectơ khoảng cách trong Hình 5.6, mỗi giá trị trong

vectơ khoảng cách D(x) không tăng và cuối cùng sẽ ổn định ở một số bước hữu hạn. P11. Hãy xem xét Hình 5.7. Giả sử có một bộ định tuyến khác, được kết nối với bộ định tuyến

y và z. Chi phí của tất cả các liên kết được đưa ra như sau: c(x,y) = 4, c(x,z) = 50, c(y,w) = 1, c(z,w) = 1, c(y,z) = 3. Giả sử rằng thuật toán định tuyến vectơ khoảng cách bị nhiễm độc được sử dụng.

VẤN ĐỀ 441

Một. Khi định tuyến vectơ khoảng cách ổn định, bộ định tuyến w, y và z sẽ thông báo cho họ

khoảng cách đến x với nhau. Chúng nói với nhau những giá trị khoảng cách nào? b. Bây giờ giả sử chi phí liên kết giữa x và y tăng lên 60. Liệu có

vấn đề đếm đến vô cùng ngay cả khi sử dụng tính năng đảo ngược độc hại? Tại sao hoặc tại sao không? Nếu có vấn đề đếm đến vô cùng thì cần bao nhiêu lần lặp để định tuyến vectơ khoảng cách đạt lại trạng thái ổn định? Biện minh cho câu trả lời của bạn. c. Làm thế nào để bạn sửa đổi c(y,z) sao cho không có vấn đề đếm đến vô cùng

hoàn toàn nếu c(y,x) thay đổi từ 4 thành 60? P12. Mô tả cách phát hiện các vòng lặp trong đường dẫn trong BGP. P13. Liệu bộ định tuyến BGP có luôn chọn tuyến không có vòng lặp với đường dẫn ASpath ngắn nhất không?

chiều dài? Biện minh cho câu trả lời của bạn. P14. Hãy xem xét mạng được hiển thị dưới đây. Giả sử AS3 và AS2 đang chạy

OSPF cho giao thức định tuyến nội bộ AS của họ. Giả sử AS1 và AS4 đang chạy RIP cho giao thức định tuyến nội bộ AS của chúng. Giả sử eBGP và iBGP được sử dụng cho giao thức định tuyến giữa các AS. Ban đầu giả sử không có liên kết vật lý nào giữa AS2 và AS4. Một. Router 3c tìm hiểu về tiền tố x từ giao thức định tuyến nào: OSPF, RIP,

eBGP hay iBGP? b. Router 3a tìm hiểu về x từ giao thức định tuyến nào? c. Router 1c tìm hiểu về x từ giao thức định tuyến nào? d. Router 1d tìm hiểu về x từ giao thức định tuyến nào?

AS4

AS3

AS1

AS2

x

4b

4c 4a

3c

3b 3a

1c

1b

1 ngày

1a

I1 I2

2c

2a 2b

P15. Đề cập đến vấn đề trước, khi bộ định tuyến 1d tìm hiểu về x nó sẽ đặt một

mục (x, I) trong bảng chuyển tiếp của nó. Một. Tôi sẽ bằng I1 hay I2 cho mục này? Giải thích tại sao trong một câu. b. Bây giờ giả sử có một liên kết vật lý giữa AS2 và AS4, được hiển thị

bằng đường chấm chấm. Giả sử bộ định tuyến 1d biết rằng x có thể truy cập được qua AS2 cũng như qua AS3. Tôi sẽ được đặt thành I1 hay I2? Giải thích tại sao trong một câu. c. Bây giờ giả sử có một AS khác, gọi là AS5, nằm trên đường dẫn

giữa AS2 và AS4 (không thể hiện trong sơ đồ). Giả sử bộ định tuyến 1d biết rằng x có thể truy cập được qua AS2 AS5 AS4 cũng như qua AS3 AS4. Tôi sẽ được đặt thành I1 hay I2? Giải thích tại sao trong một câu. P16. Hãy xem xét mạng sau đây. ISP B cung cấp dịch vụ đường trục quốc gia

tới ISP khu vực A. ISP C cung cấp dịch vụ đường trục quốc gia cho ISP khu vực D. Mỗi ISP bao gồm một AS. B và C ngang hàng với nhau ở hai nơi bằng cách sử dụng BGP. Hãy xem xét lưu lượng truy cập đi từ A đến D. B muốn chuyển giao lưu lượng đó cho C ở Bờ Tây (để C sẽ phải chịu chi phí vận chuyển lưu lượng xuyên quốc gia), trong khi C muốn nhận lưu lượng truy cập qua điểm ngang hàng Bờ Đông của nó với B (để B sẽ vận chuyển lưu lượng trên toàn quốc). C có thể sử dụng cơ chế BGP nào để B chuyển giao lưu lượng từ A đến D tại điểm ngang hàng Bờ Đông của nó? Để trả lời câu hỏi này, bạn cần tìm hiểu kỹ đặc tả BGP.

ISP B

ISP C

ISP D

ISP A

BÀI LẬP TRÌNH SOCKET 5: ICMP PING 443

P17. Trong Hình 5.13, hãy xem xét thông tin đường dẫn đến các mạng sơ khai W,

X và Y. Dựa trên thông tin có sẵn tại W và X, quan điểm tương ứng của họ về cấu trúc liên kết mạng là gì? Biện minh cho câu trả lời của bạn. Khung nhìn cấu trúc liên kết tại Y được hiển thị bên dưới.

W

Y

X A

C

Chế độ xem cấu trúc liên kết của mạng sơ khai Y

P18. Hãy xem xét Hình 5.13. B sẽ không bao giờ chuyển tiếp lưu lượng truy cập đến Y thông qua X dựa trên

trên định tuyến BGP. Nhưng có một số ứng dụng rất phổ biến trong đó các gói dữ liệu đi đến X trước rồi đến Y. Xác định một ứng dụng như vậy và mô tả cách các gói dữ liệu đi theo đường dẫn không được định tuyến BGP đưa ra. P19. Trong Hình 5.13, giả sử có một mạng sơ khai V khác là mạng cus-

tomer của ISP A. Giả sử B và C có mối quan hệ ngang hàng và A là khách hàng của cả B và C. Giả sử A muốn có lưu lượng truy cập đến W chỉ đến từ B và lưu lượng truy cập đến V từ B hoặc C. A nên quảng cáo các tuyến của nó đến B và C như thế nào? C nhận được những tuyến đường AS nào? P20. Giả sử AS X và Z không được kết nối trực tiếp mà thay vào đó được kết nối

bởi AS Y. Hơn nữa, giả sử rằng X có thỏa thuận ngang hàng với Y và Y có thỏa thuận ngang hàng với Z. Cuối cùng, giả sử rằng Z muốn chuyển tải tất cả lưu lượng truy cập của Y nhưng không muốn chuyển tải lưu lượng truy cập của X. BGP có cho phép Z triển khai chính sách này không? P21. Hãy xem xét hai cách giao tiếp diễn ra giữa người quản lý

thực thể và thiết bị được quản lý: chế độ phản hồi yêu cầu và bẫy. Ưu và nhược điểm của hai phương pháp này là gì, về (1) chi phí, (2) thời gian thông báo khi xảy ra sự kiện đặc biệt và (3) độ tin cậy đối với các tin nhắn bị mất giữa đơn vị quản lý và thiết bị? P22. Trong Phần 5.7, chúng ta đã thấy rằng việc vận chuyển các thông báo SNMP trong

các datagram UDP không đáng tin cậy. Bạn nghĩ tại sao các nhà thiết kế SNMP lại chọn UDP thay vì TCP làm giao thức truyền tải được lựa chọn cho SNMP?

**Socket Bài tập lập trình 5: ICMP Ping**

Ở cuối Chương 2, có bốn bài tập lập trình socket. Tại đây, bạn sẽ tìm thấy bài tập thứ năm sử dụng ICMP, một giao thức được thảo luận trong chương này.

Ping là một ứng dụng mạng phổ biến được sử dụng để kiểm tra từ một vị trí từ xa xem một máy chủ cụ thể có hoạt động và có thể truy cập được hay không. Nó cũng thường được sử dụng để đo độ trễ giữa máy chủ và máy chủ đích. Nó hoạt động bằng cách gửi ICMP gói "yêu cầu tiếng vang" (tức là gói ping) đến máy chủ đích và lắng nghe ICMP phản hồi "phản hồi tiếng vang" (tức là gói pong). Ping đo RRT, ghi lại việc mất gói và tính toán tóm tắt thống kê về nhiều lần trao đổi bóng bàn (độ lệch tối thiểu, trung bình, tối đa và độ lệch chuẩn của thời gian khứ hồi).

Trong phòng thí nghiệm này, bạn sẽ viết ứng dụng Ping của riêng mình bằng Python. Ứng dụng của bạn sẽ sử dụng ICMP. Nhưng để giữ cho chương trình của bạn đơn giản, bạn sẽ không tuân theo chính xác thông số kỹ thuật chính thức trong RFC 1739. Lưu ý rằng bạn sẽ chỉ cần viết phía máy khách của chương trình, vì chức năng cần thiết ở phía máy chủ được tích hợp trong hầu hết các hệ điều hành. Bạn có thể tìm thấy đầy đủ thông tin chi tiết về bài tập này cũng như các đoạn mã Python quan trọng tại trang web http://www.pearsonhighered. com/cs-resource.

**Nhiệm vụ lập trình: Định tuyến**

Trong bài tập lập trình này, bạn sẽ viết một tập hợp các thủ tục "phân tán" để thực hiện định tuyến vectơ khoảng cách không đồng bộ được phân phối cho mạng được hiển thị bên dưới.

Bạn phải viết các quy trình sau đây để "thực thi" không đồng bộ trong môi trường mô phỏng được cung cấp cho nhiệm vụ này. Đối với nút 0, bạn sẽ viết các thủ tục:

• rtinit0(). Thói quen này sẽ được gọi một lần khi bắt đầu mô phỏng. rtinit0() không có đối số. Nó sẽ khởi tạo bảng khoảng cách của bạn ở nút 0 để phản ánh chi phí trực tiếp lần lượt là 1, 3 và 7 cho các nút 1, 2 và 3. Trong hình trên, tất cả các liên kết đều là hai chiều và chi phí theo cả hai hướng là như nhau. Sau khi khởi tạo bảng khoảng cách và bất kỳ cấu trúc dữ liệu nào khác mà quy trình nút 0 của bạn cần, nó sẽ gửi các nút lân cận được kết nối trực tiếp (trong trường hợp này là 1, 2 và 3) chi phí của các đường dẫn có chi phí tối thiểu tới tất cả các nút mạng khác.

PHÒNG THÍ NGHIỆM WIRESHARK: ICMP 445

Thông tin chi phí tối thiểu này được gửi đến các nút lân cận trong gói cập nhật định tuyến bằng cách gọi thủ tục tolayer2(), như được mô tả trong bài tập đầy đủ. Định dạng của gói cập nhật định tuyến cũng được mô tả trong bài tập đầy đủ. • rtupdate0(struct rtpkt \*rcvdpkt). Quy trình này sẽ được gọi khi nút 0 nhận được gói định tuyến được gửi đến nó bởi một trong những nút hàng xóm được kết nối trực tiếp của nó. Tham số \*rcvdpkt là con trỏ tới gói đã nhận được. rtupdate0() là "trái tim" của thuật toán vectơ khoảng cách. Các giá trị mà nó nhận được trong gói cập nhật định tuyến từ một số nút khác chứa chi phí đường đi ngắn nhất hiện tại của tôi tới tất cả các nút mạng khác. rtupdate0() sử dụng các giá trị nhận được này để cập nhật bảng khoảng cách của chính nó (như được chỉ định bởi thuật toán vectơ khoảng cách). Nếu chi phí tối thiểu của chính nó đối với nút khác thay đổi do cập nhật, nút 0 sẽ thông báo cho các hàng xóm được kết nối trực tiếp của nó về sự thay đổi chi phí tối thiểu này bằng cách gửi cho họ gói định tuyến. Hãy nhớ lại rằng trong thuật toán vectơ khoảng cách, chỉ các nút được kết nối trực tiếp mới trao đổi các gói định tuyến. Do đó, nút 1 và 2 sẽ liên lạc với nhau, nhưng nút 1 và 3 sẽ không liên lạc với nhau.

Các quy trình tương tự được xác định cho các nút 1, 2 và 3. Do đó, bạn sẽ viết tổng cộng tám thủ tục: rtinit0(), rtinit1(), rtinit2(), rtinit3(), rtupdate0(), rtupdate1(), rtupdate2() và rtupdate3(). Các quy trình này sẽ cùng nhau thực hiện tính toán không đồng bộ, phân tán của các bảng khoảng cách cho cấu trúc liên kết và chi phí được hiển thị trong hình trên trang trước.

Bạn có thể tìm thấy chi tiết đầy đủ về nhiệm vụ lập trình cũng như mã C mà bạn sẽ cần để tạo môi trường phần cứng/phần mềm mô phỏng tại http:// www.pearsonhighered.com/cs-resource. Phiên bản Java của bài tập cũng có sẵn.

**Wireshark Phòng thí nghiệm: ICMP**

Trên trang web của cuốn sách giáo khoa này, www.pearsonhighered.com/cs-resources, bạn sẽ tìm thấy một bài tập lab Wireshark kiểm tra việc sử dụng giao thức ICMP trong các lệnh ping và traceroute.

Vui lòng mô tả một hoặc hai dự án thú vị nhất mà bạn đã thực hiện trong sự nghiệp của mình. Những thách thức lớn nhất là gì?

Khi tôi còn là nhà nghiên cứu tại AT&T, một nhóm chúng tôi đã thiết kế một cách mới để quản lý việc định tuyến trong mạng đường trục của Nhà cung cấp Dịch vụ Internet. Theo truyền thống, các nhà khai thác mạng sẽ cấu hình từng bộ định tuyến riêng lẻ và các bộ định tuyến này chạy các giao thức phân tán để tính toán đường dẫn qua mạng. Chúng tôi tin rằng việc quản lý mạng sẽ đơn giản và linh hoạt hơn nếu các nhà khai thác mạng có thể thực hiện kiểm soát trực tiếp cách bộ định tuyến chuyển tiếp lưu lượng truy cập dựa trên chế độ xem toàn mạng về cấu trúc liên kết và lưu lượng. Nền tảng Kiểm soát Định tuyến (RCP) mà chúng tôi thiết kế và xây dựng có thể tính toán các tuyến đường cho tất cả các mạng của AT&T.

Jennifer Rexford là Giáo sư khoa Khoa học Máy tính tại Đại học Princeton. Nghiên cứu của cô có mục tiêu rộng lớn là làm cho mạng máy tính dễ thiết kế và quản lý hơn, đặc biệt chú trọng đến các mạng có thể lập trình được. Từ năm 1996--2004, cô là thành viên của bộ phận Hiệu suất và Quản lý Mạng tại AT&T Labs--Research. Khi làm việc tại AT&T, cô đã thiết kế các kỹ thuật và công cụ để đo lường mạng, kỹ thuật lưu lượng và cấu hình bộ định tuyến được triển khai trong mạng đường trục của AT&T. Jennifer là đồng tác giả của cuốn sách "Thực hành và giao thức web: Giao thức mạng, bộ nhớ đệm và đo lưu lượng" do Addison-Wesley xuất bản vào tháng 5 năm 2001. Cô từng là chủ tịch của ACM SIGCOMM từ năm 2003 đến năm 2007. Cô nhận bằng BSE về kỹ thuật điện tại Đại học Princeton năm 1991 và bằng Tiến sĩ về kỹ thuật điện và khoa học máy tính của Đại học Michigan năm 1996. Jennifer là người đoạt giải năm 2004. của Giải thưởng Grace Murray Hopper của ACM dành cho chuyên gia máy tính trẻ xuất sắc, Giải thưởng Giảng viên ACM Athena (2016), Giải thưởng Cố vấn Nghiên cứu và Sau đại học của NCWIT Harrold và Notkin (2017), giải thưởng ACM SIGCOMM cho những đóng góp trọn đời (2018) và Giải thưởng Internet IEEE (2019). Cô là Thành viên ACM (2008), Thành viên IEEE (2018) và Học viện Kỹ thuật Quốc gia (2014).

**Jennifer Rexford**

PHỎNG VẤN VỚI...

Được phép của Jennifer Rexford

![](media/image3.png){width="5.5in" height="7.0625in"}

xương sống trên một máy tính thông thường và có thể điều khiển các bộ định tuyến cũ mà không cần sửa đổi. Đối với tôi, dự án này rất thú vị vì chúng tôi có một ý tưởng đầy đột phá, một hệ thống làm việc và cuối cùng là một hoạt động triển khai thực sự trong mạng lưới hoạt động. Một vài năm trôi qua nhanh chóng, mạng được xác định bằng phần mềm (SDN) đã trở thành một công nghệ chủ đạo và các giao thức tiêu chuẩn (như giao thức tiêu chuẩn (như OpenFlow) và các ngôn ngữ (như P4) đã giúp việc yêu cầu các công tắc cơ bản phải làm gì trở nên dễ dàng hơn nhiều.

Bạn nghĩ mạng được xác định bằng phần mềm sẽ phát triển như thế nào trong tương lai?

Trong một bước đột phá lớn so với trước đây, phần mềm điều khiển các thiết bị mạng có thể được tạo ra bởi nhiều lập trình viên khác nhau chứ không chỉ ở các công ty bán thiết bị mạng. Tuy nhiên, không giống như các ứng dụng chạy trên máy chủ hoặc điện thoại thông minh, các ứng dụng SDN phải hoạt động cùng nhau để xử lý cùng một lưu lượng truy cập. Các nhà khai thác mạng không muốn thực hiện cân bằng tải trên một số lưu lượng và định tuyến trên các lưu lượng khác; thay vào đó, họ muốn thực hiện cân bằng tải và định tuyến cùng nhau trên cùng một lưu lượng. Các nền tảng SDN trong tương lai sẽ cung cấp khả năng tóm tắt lập trình tốt để kết hợp nhiều ứng dụng được viết độc lập với nhau. Nói rộng hơn, tính trừu tượng hóa lập trình tốt có thể giúp tạo ứng dụng dễ dàng hơn mà không phải lo lắng về các chi tiết cấp thấp như mục nhập bảng luồng, bộ đếm lưu lượng, mẫu bit trong tiêu đề gói, v.v. Ngoài ra, trong khi bộ điều khiển SDN được tập trung về mặt logic thì mạng vẫn bao gồm một tập hợp thiết bị phân tán. Các mạng lập trình trong tương lai sẽ cung cấp khả năng trừu tượng hóa tốt cho việc cập nhật một bộ thiết bị phân tán, do đó, quản trị viên mạng có thể suy luận về điều gì xảy ra với các gói đang truyền trong khi thiết bị được cập nhật. Lập trình trừu tượng cho mạng lập trình là một lĩnh vực thú vị cho nghiên cứu liên ngành giữa mạng máy tính, hệ thống phân tán và ngôn ngữ lập trình, có cơ hội thực sự mang lại tác động thực tế trong những năm tới.

Bạn nhìn thấy tương lai của mạng và Internet ở đâu?

Mạng là một lĩnh vực thú vị vì các ứng dụng và công nghệ cơ bản luôn thay đổi. Chúng tôi luôn làm mới chính mình! Cách đây mười năm ai có thể dự đoán được sự thống trị của điện thoại thông minh, cho phép người dùng di động truy cập các ứng dụng hiện có cũng như các dịch vụ dựa trên vị trí mới? Sự xuất hiện của điện toán đám mây đang thay đổi căn bản mối quan hệ giữa người dùng và ứng dụng họ chạy, đồng thời các cảm biến và bộ truyền động được nối mạng ("Internet of Things") đang tạo ra vô số ứng dụng mới (và các lỗ hổng bảo mật!). Tốc độ đổi mới thực sự truyền cảm hứng.

Mạng cơ bản là một thành phần quan trọng trong tất cả những đổi mới này. Tuy nhiên, mạng này nổi tiếng là "cản đường"---hạn chế hiệu suất, ảnh hưởng đến độ tin cậy, hạn chế các ứng dụng và làm phức tạp việc triển khai và quản lý dịch vụ. Chúng ta nên cố gắng làm cho mạng lưới trong tương lai trở nên vô hình như không khí chúng ta hít thở, để nó không bao giờ cản trở những ý tưởng mới và dịch vụ có giá trị. Để làm được điều này, chúng ta cần nâng mức độ trừu tượng lên trên các thiết bị và giao thức mạng riêng lẻ (và các từ viết tắt đi kèm của chúng!), để chúng ta có thể suy luận về mạng và các mục tiêu cấp cao của người dùng nói chung.

Những người nào đã truyền cảm hứng cho bạn một cách chuyên nghiệp?

Tôi đã được truyền cảm hứng từ lâu bởi Sally Floyd, người đã làm việc nhiều năm tại Viện Khoa học Máy tính Quốc tế. Nghiên cứu của cô luôn có mục đích, tập trung vào những thách thức quan trọng mà Internet phải đối mặt. Cô ấy đào sâu vào những câu hỏi khó cho đến khi hiểu hoàn toàn vấn đề và không gian của các giải pháp, đồng thời cô ấy dành năng lượng nghiêm túc để "biến mọi thứ thành hiện thực", chẳng hạn như đưa ý tưởng của mình vào các tiêu chuẩn giao thức và thiết bị mạng. Ngoài ra, cô còn đóng góp cho cộng đồng thông qua dịch vụ chuyên nghiệp ở nhiều tổ chức nghiên cứu và tiêu chuẩn cũng như bằng cách tạo ra các công cụ (như trình mô phỏng ns-2 và ns-3 được sử dụng rộng rãi) giúp các nhà nghiên cứu khác thành công. Cô đã nghỉ hưu vào năm 2009 và qua đời vào năm 2019, nhưng ảnh hưởng của cô đối với lĩnh vực này sẽ còn tồn tại trong nhiều năm tới.

Lời khuyên của bạn dành cho những sinh viên muốn có sự nghiệp trong khoa học máy tính và mạng là gì?

Mạng vốn là một lĩnh vực liên ngành. Việc áp dụng các kỹ thuật từ những đột phá của ngành khác trong mạng đến từ các lĩnh vực đa dạng như lý thuyết xếp hàng, lý thuyết trò chơi, lý thuyết điều khiển, hệ thống phân tán, tối ưu hóa mạng, ngôn ngữ lập trình, học máy, thuật toán, cấu trúc dữ liệu, v.v. Tôi nghĩ rằng việc trở nên thông thạo trong một lĩnh vực liên quan hoặc cộng tác chặt chẽ với các chuyên gia trong lĩnh vực đó là một cách tuyệt vời để đặt mạng lưới trên một nền tảng vững chắc hơn, để chúng ta có thể học cách xây dựng mạng lưới xứng đáng với sự tin cậy của xã hội. Ngoài các nguyên tắc lý thuyết, kết nối mạng còn thú vị vì chúng tôi tạo ra những sản phẩm thực tế mà người thực sử dụng. Nắm vững cách thiết kế và xây dựng hệ thống---bằng cách tích lũy kinh nghiệm về hệ điều hành, kiến ​​trúc máy tính, v.v.---là một cách tuyệt vời khác để nâng cao kiến ​​thức về mạng của bạn nhằm giúp biến thế giới thành một nơi tốt đẹp hơn.

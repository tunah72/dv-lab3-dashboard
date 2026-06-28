# Kịch Bản Trình Bày (Tuấn Anh - Leader)

**Thời lượng dự kiến:** 5 - 7 phút
**Vai trò:** Giới thiệu chủ đề đồ án, Mô hình dữ liệu (Data Model), Thiết kế tổng quan của Dashboard và Phân tích chuyên sâu mục tiêu Sales Trend.

---

## 1. Giới thiệu Chủ đề (1 phút)

**[Camera focus vào người trình bày, màn hình hiển thị trang bìa hoặc trang Overview]**

"Chào Thầy và các bạn, mình là Tuấn Anh, trưởng nhóm. Hôm nay, thay mặt nhóm, mình xin phép được trình bày về đồ án môn học Trực quan hóa Dữ liệu với chủ đề: **Phân tích dữ liệu bán lẻ (Retail Data Warehouse) thông qua Power BI**."

"Trong bối cảnh ngành bán lẻ ngày càng cạnh tranh, việc nắm bắt nhanh chóng sức khỏe doanh nghiệp là vô cùng quan trọng. Vì vậy, nhóm chúng mình đã lựa chọn bộ dữ liệu Retail Data Warehouse từ Kaggle, bao gồm hơn 1 triệu dòng dữ liệu giao dịch thực tế. Mục tiêu của nhóm không chỉ là vẽ biểu đồ, mà là xây dựng một **Hệ thống Dashboard Quản trị** hoàn chỉnh, giúp các cấp quản lý từ C-Level đến giám đốc vận hành có thể đưa ra quyết định dựa trên dữ liệu thật (Data-driven decision making)."

---

## 2. Mô hình Dữ liệu - Data Model (1.5 phút)

**[Chuyển màn hình sang chế độ Model View trong Power BI]**

"Trước khi đi vào phần giao diện, mình xin giới thiệu nhanh về phần cốt lõi nhất của hệ thống: **Mô hình dữ liệu (Data Model)**. 

Nhóm đã xây dựng mô hình theo cấu trúc **Star Schema** chuẩn mực với 12 bảng. Ở trung tâm là các bảng Fact ghi nhận giao dịch như `orders`, `order_items`, `payments`, `shipments`, bao quanh là các bảng Dimension như Khách hàng, Sản phẩm, Cửa hàng.

Điểm nổi bật trong mô hình của nhóm là:
1. **100% các mối quan hệ** được thiết lập chuẩn 1 chiều (Single Cross-filter direction) và Many-to-One, giúp tối ưu hiệu suất và tránh tình trạng lọc dữ liệu chồng chéo.
2. Nhóm đã tự xây dựng một **bảng Date (Date Table) chuyên biệt** bằng DAX để có thể khai thác sức mạnh của các hàm Time Intelligence, phục vụ việc so sánh tăng trưởng MoM và YoY.
3. Thay vì dùng các phép tính tự động (Implicit Measures), toàn bộ 36 phép tính toán của báo cáo đều được lập trình lại bằng DAX và lưu trữ gọn gàng trong một bảng ảo `_Measures`. Điều này đảm bảo tính chính xác tuyệt đối khi dữ liệu phình to."

---

## 3. Thiết kế Tổng quan & Tính năng (1 phút)

**[Trở lại màn hình Report View, thao tác click chuyển tab trên thanh Sidebar]**

"Về mặt thiết kế tổng quan, nhóm thống nhất sử dụng một giao diện tối giản nhưng hiện đại để làm nổi bật dữ liệu số. 

Điểm nhấn về tính năng tương tác (Features) của Dashboard bao gồm:
* **Thanh điều hướng (Sidebar Navigation):** Sử dụng tính năng Bookmarks và Buttons, người dùng có thể dễ dàng chuyển đổi mượt mà giữa 5 phân hệ phân tích: Overview, Sales Trend, Customers, Products, và Operations.
* **Hệ thống Filter đồng bộ:** Các bộ lọc về Thời gian và Khu vực được đồng bộ (Sync Slicers) trên tất cả các trang. Người dùng chỉ cần lọc một lần và insight sẽ đi theo họ xuyên suốt Dashboard.
* **Custom Tooltip:** Khi trỏ chuột vào bất kỳ biểu đồ nào, các Tooltip tùy chỉnh sẽ hiện ra để cung cấp ngay con số % tăng trưởng chi tiết mà không làm rối biểu đồ chính."

---

## 4. Phân tích Mục tiêu: Sales Trend (2.5 - 3 phút)

**[Mở trang "Sales Trend", bắt đầu thao tác rà chuột vào các biểu đồ cụ thể]**

"Bây giờ, mình xin phép đi sâu vào phân hệ phân tích đầu tiên do mình đảm nhiệm: **Sales Trend - Xu hướng Doanh thu**."

**[Chỉ vào dãy KPI Cards phía trên]**
"Nhìn vào dải KPI đầu trang, chúng ta có thể nắm bắt ngay nhịp đập tài chính của doanh nghiệp: Tổng doanh thu đạt **3.83 Tỷ đô**, Doanh thu ròng (sau khi trừ hoàn trả) là **3.75 Tỷ đô**, Giá trị trung bình mỗi đơn (AOV) ở mức **$12,759.15** và đặc biệt là Tăng trưởng so với cùng kỳ năm trước (YoY) đạt con số ấn tượng **+29.8%**. Những con số này đóng vai trò như 'mỏ neo' để đánh giá xem doanh nghiệp đang phát triển hay đi lùi."

**[Chỉ vào biểu đồ Line & Clustered Column Chart (Doanh thu & Đơn hàng)]**
"Chuyển sang biểu đồ đường và cột kết hợp này. Ở đây, mình dùng cột để biểu diễn Doanh thu và đường để biểu diễn Số lượng đơn hàng theo thời gian. 
*Insight rút ra là gì?* Nhìn vào xu hướng, chúng ta thấy đường số lượng đơn hàng và cột doanh thu di chuyển rất bám sát nhau (đồng pha). Điều này chứng tỏ sự tăng trưởng doanh thu là kết quả thực chất từ việc bán được nhiều đơn hàng hơn, chứ không chỉ đơn thuần là do tăng giá bán hay phụ thuộc vào một vài đơn hàng giá trị lớn đột biến."

**[Chỉ vào biểu đồ Line Chart so sánh YoY]**
"Biểu đồ đường bên phải thực hiện việc gộp doanh thu năm nay và doanh thu năm ngoái lên cùng một trục tháng. Nó cho thấy rất rõ hiệu suất vượt trội của năm nay so với cùng kỳ. Tại các tháng cao điểm (Peak months), doanh thu năm nay đã phá vỡ hoàn toàn kỷ lục của năm ngoái."

**[Chỉ vào biểu đồ Ribbon Chart phía dưới]**
"Và để trả lời cho câu hỏi: *Ai là người tạo ra sự tăng trưởng đó?*, mình đã sử dụng biểu đồ Ribbon Chart để phân rã doanh thu theo Phân khúc khách hàng (Segment) được tính toán từ mô hình K-Means (VIP, Loyal, New, At Risk). 
Với đặc tính của Ribbon Chart, luồng ruy-băng không chỉ hiển thị độ lớn doanh thu mà còn thể hiện **sự thay đổi thứ hạng**. Chúng ta có thể dễ dàng thấy nhóm khách hàng VIP và Loyal liên tục giữ các dải ruy-băng lớn nhất ở trên cùng qua các tháng, khẳng định đây chính là 'cột sống' đem lại dòng tiền ổn định cho doanh nghiệp."

"Đó là phần trình bày về tổng quan hệ thống và phân tích Sales Trend. Tiếp theo, xin mời bạn **[Tên thành viên tiếp theo]** sẽ trình bày về phân hệ phân tích khách hàng chuyên sâu (Customers)."

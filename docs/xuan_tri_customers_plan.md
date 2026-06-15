# Kế Hoạch Chi Tiết Thiết Kế Trang "Customers" (Khách Hàng) trên Power BI

**Dự án**: Data Visualization Dashboard - Lab 03  
**Chịu trách nhiệm chính (Owner)**: Lê Xuân Trí  
**Người tổng hợp cuối cùng (Compiler)**: Lê Đức Phúc  
**Tập tin Power BI làm việc**: `Dashboard_XuanTri_Customers.pbix`  
**Tên trang hiển thị trên báo cáo**: **Khách hàng**

Tài liệu này cung cấp kế hoạch triển khai chi tiết từng bước cho Lê Xuân Trí để hoàn thiện trang **Khách hàng** trên Power BI, đảm bảo tính đồng bộ tuyệt đối về mặt mỹ thuật, dữ liệu và kỹ thuật với các thành viên khác theo quy định chung của dự án.

---

## 1. Danh Sách Tài Liệu Cần Đọc Kỹ Trước Khi Làm
Trước khi bắt đầu kéo thả visual, Xuân Trí cần đọc kỹ các tài liệu sau để nắm được ngữ cảnh dữ liệu và các quy định thiết kế chung:

*   [Customers.md](file:///home/pearspringmind/Studying/HCMUS/Data%20Visualization/dv-lab3-dashboard/docs/Customers.md): Hướng dẫn thiết kế chi tiết trang Customers (nguồn chính).
*   [convention_note.md](file:///home/pearspringmind/Studying/HCMUS/Data%20Visualization/dv-lab3-dashboard/docs/convention_note.md): Quy ước chung về layout, font, cỡ chữ, định dạng ngôn ngữ hiển thị (tiếng Việt), sidebar navigation, reset bookmark và quy trình bàn giao.
*   [powerbi_data_model_guide.md](file:///home/pearspringmind/Studying/HCMUS/Data%20Visualization/dv-lab3-dashboard/docs/powerbi_data_model_guide.md): Hướng dẫn về mô hình dữ liệu (các bảng `customers`, `orders`, `order_items`, `Date` và luồng quan hệ dữ liệu).
*   [powerbi_dax_measures_dictionary.md](file:///home/pearspringmind/Studying/HCMUS/Data%20Visualization/dv-lab3-dashboard/docs/powerbi_dax_measures_dictionary.md): Từ điển DAX measures có sẵn trong bảng `_Measures`.

---

## 2. Giai Đoạn 1: Thiết Lập File Làm Việc & Background
1.  **Tạo File Làm Việc**: 
    *   Tru cập vào thư mục chứa file base: [Dashboard.pbix](file:///home/pearspringmind/Studying/HCMUS/Data%20Visualization/dv-lab3-dashboard/Dashboard.pbix).
    *   Tạo một bản sao và đặt tên chính xác là `Dashboard_XuanTri_Customers.pbix`. **Không làm việc trực tiếp trên file base.**
2.  **Áp Dụng Background**:
    *   Trong tab `Customers` trên Power BI, truy cập phần Format page -> Canvas background.
    *   Chọn file background đã xuất sẵn cho tab 2: [background_tab2.png](file:///home/pearspringmind/Studying/HCMUS/Data%20Visualization/dv-lab3-dashboard/design/background_tab2.png) (hoặc [background_tab2_1280x720.png](file:///home/pearspringmind/Studying/HCMUS/Data%20Visualization/dv-lab3-dashboard/design/background_tab2_1280x720.png)).
    *   Đặt **Image fit = Fit** và **Transparency = 0%** để đảm bảo background hiển thị rõ ràng và khớp khung hình 16:9.
    *   > [!IMPORTANT]
        > Nếu cần tùy chỉnh kích thước container của biểu đồ, Xuân Trí có thể chỉnh sửa trực tiếp template PowerPoint [powerbi_background_template.pptx](file:///home/pearspringmind/Studying/HCMUS/Data%20Visualization/dv-lab3-dashboard/design/powerbi_background_template.pptx). Sau khi chỉnh sửa, xuất slide tương ứng thành file PNG 16:9 rồi gán lại vào báo cáo, đồng thời ghi chú rõ thay đổi này cho Đức Phúc khi bàn giao.

---

## 3. Giai Đoạn 2: Thống Nhất Quy Chuẩn Trình Bày & Mỹ Thuật (Màu sắc, Font, Ngôn ngữ)
Để tránh lệch giao diện khi Đức Phúc gộp các trang thành dashboard final, Xuân Trí cần áp dụng chính xác các quy chuẩn sau:

*   **Font chữ**: Thống nhất dùng font **Segoe UI** (hoặc **Segoe UI Semibold** cho các tiêu đề/nút bấm. Nếu Power BI của bạn không có `Segoe UI Semibold`, hãy chọn `Segoe UI` và bật định dạng **Bold**).
*   **Cỡ chữ đề xuất**:
    *   *Tiêu đề trang*: **22 - 26 pt** (Tên trang hiển thị: **Khách hàng**).
    *   *Tiêu đề biểu đồ*: **11 - 13 pt** (Segoe UI Semibold/Segoe UI Bold).
    *   *Giá trị KPI (KPI Value)*: **22 - 28 pt** (Segoe UI Semibold/Segoe UI Bold).
    *   *Nhãn KPI (KPI Label)*: **9 - 11 pt**.
    *   *Nhãn trục (Axis label)*: **8 - 10 pt**.
    *   *Chú giải (Legend)*: **8 - 10 pt**.
    *   *Slicer Title*: **9 - 10 pt**; *Slicer Value*: **8 - 10 pt**.
    *   *Nút bấm Navigation / Reset*: **10 - 11 pt**.
*   **Ngôn ngữ hiển thị**: Tất cả thông tin người xem nhìn thấy trên màn hình (nhãn KPI, tiêu đề trục, tiêu đề slicer, tiêu đề biểu đồ) đều phải viết bằng **Tiếng Việt có dấu**.
    *   *Tên bảng và trường (field) trong model*: Giữ nguyên tiếng Anh (ví dụ: `customers[Segment]`).
    *   *Tên measure*: Giữ nguyên tiếng Anh (ví dụ: `Total Revenue`).
*   **Định dạng số liệu**:
    *   *Doanh thu (Revenue / Money)*: Định dạng tiền tệ USD, ví dụ: `$#,0.00` hoặc `$#,0`.
    *   *Số lượng / Số khách hàng / Số đơn*: Số nguyên có dấu phẩy phân cách phần nghìn, ví dụ: `#,0`.
    *   *Tỷ lệ / Tỷ trọng*: Định dạng phần trăm, ví dụ: `0.00%`.
    *   *Số dòng hàng mỗi đơn*: Số thập phân, ví dụ: `#,0.00`.

---

## 4. Giai Đoạn 3: Thiết Lập KPI Cards & Slicers
Xuân Trí thực hiện kéo thả các visual sau vào đúng khu vực quy định trên background:

### 4.1. Thiết lập 4 Thẻ KPI (KPI Cards)
Đặt ngang hàng ở vùng KPI row (theo thứ tự từ trái qua phải):

| Số thứ tự | Tên Visual (Selection Pane) | Measure sử dụng | Nhãn hiển thị tiếng Việt (Label) | Định dạng hiển thị |
| :---: | :--- | :--- | :--- | :--- |
| 1 | `KPI_Customers_TotalCustomers` | `Total Customers` | Tổng khách hàng | Số nguyên (`#,0`) |
| 2 | `KPI_Customers_RevenuePerCustomer` | `Revenue per Customer` | Doanh thu trên mỗi khách hàng | Tiền tệ (`$#,0.00`) |
| 3 | `KPI_Customers_TotalOrders` | `Total Orders` | Tổng đơn hàng | Số nguyên (`#,0`) |
| 4 | `KPI_Customers_ItemsPerOrder` | `Items per Order` | Số dòng hàng mỗi đơn | Số thập phân (`#,0.00`) |

### 4.2. Thiết lập các Bộ Lọc (Slicers)
Đặt các slicer này xếp theo chiều dọc nằm trọn bên trong khung **FILTERS** màu xanh đậm ở thanh Sidebar bên trái (đại diện bởi container `filter-container` trên layout background):

| Tên Visual (Selection Pane) | Cột dữ liệu (Field) | Tiêu đề hiển thị | Kiểu hiển thị |
| :--- | :--- | :--- | :--- |
| `SL_Customers_Year` | `Date[Year]` | Năm | Dropdown hoặc Tile ngắn |
| `SL_Customers_Month` | `Date[Year Month]` | Tháng | Dropdown |
| `SL_Customers_Segment` | `customers[Segment]` | Phân khúc khách hàng | Dropdown hoặc List |
| `SL_Customers_City` | `customers[city]` | Thành phố khách hàng | Dropdown |

---

## 5. Giai Đoạn 4: Thiết Lập Hệ Thống Biểu Đồ Chính
Trang khách hàng sẽ có tối đa 4 biểu đồ chính được phân bổ vào các container quy định sẵn trên background [background_tab2.png](file:///c:/Studying/Data%20Visualization/dv-lab3-dashboard/design/background_tab2.png) để phân tích toàn diện hành vi phân khúc và địa lý:

### Chart 1: Phân tích doanh thu theo Phân khúc
*   **Container gán trên background**: `supporting-chart-bottom` (Khung ngang dưới bên trái, X: 15.9%, Y: 73.3%, W: 36.6%, H: 22.8%)
*   **Tên visual nội bộ**: `CH_Customers_RevenueBySegment`
*   **Tiêu đề hiển thị (dạng câu hỏi)**: **Phân khúc khách hàng nào tạo ra nhiều doanh thu nhất?**
*   **Loại biểu đồ**: Bar chart (nằm ngang)
*   **Cấu hình trục & dữ liệu**:
    *   *Trục tung (Y-axis)*: `customers[Segment]`
    *   *Trục hoành (X-axis)*: `Total Revenue`
    *   *Tooltip*: `Total Customers`, `Revenue per Customer`, `Total Orders`
*   **Mục tiêu phân tích**: Xác định phân khúc đóng góp doanh thu cốt lõi của doanh nghiệp.

### Chart 2: Phân tích doanh thu theo Địa lý
*   **Container gán trên background**: `supporting-chart-right` (Khung dọc bên phải, X: 69.8%, Y: 31.7%, W: 28.0%, H: 38.3%)
*   **Tên visual nội bộ**: `CH_Customers_RevenueByCity`
*   **Tiêu đề hiển thị (dạng câu hỏi)**: **Thành phố khách hàng nào đóng góp doanh thu nổi bật nhất?**
*   **Loại biểu đồ**: Bar chart (nằm ngang) hoặc Map (nếu hiển thị tốt, không gây rối mắt)
*   **Cấu hình trục & dữ liệu**:
    *   *Trục tung (Axis/Location)*: `customers[city]`
    *   *Trục hoành (Values)*: `Total Revenue`
    *   *Tooltip*: `Total Customers`, `Revenue per Customer`
*   **Mục tiêu phân tích**: Tìm các thành phố trọng điểm có lượng khách hàng hoặc mức chi tiêu lớn.

### Chart 3: Xu hướng doanh thu phân khúc theo thời gian
*   **Container gán trên background**: `main-chart` (Khung lớn ở giữa bên trái, X: 15.9%, Y: 31.7%, W: 52.3%, H: 38.3%)
*   **Tên visual nội bộ**: `CH_Customers_SegmentRevenueTrend`
*   **Tiêu đề hiển thị (dạng câu hỏi)**: **Doanh thu theo phân khúc thay đổi như thế nào theo thời gian?**
*   **Loại biểu đồ**: Line chart
*   **Cấu hình trục & dữ liệu**:
    *   *Trục hoành (X-axis)*: `Date[Year Month]`
    *   *Chú giải (Legend)*: `customers[Segment]`
    *   *Trục tung (Y-axis)*: `Total Revenue`
    *   *Tooltip*: `Revenue per Customer`, `Total Orders`
*   **Mục tiêu phân tích**: So sánh sự phát triển và tính ổn định của các phân khúc qua từng tháng.

### Chart 4: Bảng so sánh chất lượng phân khúc
*   **Container gán trên background**: `detail-table` (Khung bảng dưới bên phải, X: 54.1%, Y: 73.3%, W: 43.8%, H: 22.8%)
*   **Tên visual nội bộ**: `CH_Customers_SegmentMatrix`
*   **Tiêu đề hiển thị (dạng câu hỏi)**: **Phân khúc nào có giá trị trung bình trên mỗi khách hàng cao nhất?**
*   **Loại biểu đồ**: Matrix hoặc Table
*   **Cấu hình trục & dữ liệu**:
    *   *Hàng (Rows)*: `customers[Segment]`
    *   *Giá trị (Values)*: `Total Customers`, `Total Revenue`, `Revenue per Customer`, `Total Orders`, `Items per Order`
*   **Mục tiêu phân tích**: Đánh giá sâu chất lượng tiêu dùng thực tế của từng phân khúc (ví dụ: segment ít khách nhưng chi tiêu mỗi khách cực lớn).
*   > [!TIP]
    > **Biểu đồ thay thế nếu không sử dụng Matrix/Table**:
    > *   *Tiêu đề hiển thị*: **Tỷ trọng khách hàng theo từng phân khúc là bao nhiêu?**
    > *   *Loại biểu đồ*: Donut chart
    > *   *Chú giải (Legend)*: `customers[Segment]`
    > *   *Giá trị (Values)*: `Total Customers`

> [!NOTE]
> **Lưu ý đặc biệt về dữ liệu**: 
> Trong dữ liệu cột `customers[Segment]` có thể xuất hiện giá trị `"Unknown"`. Đây là dữ liệu thực tế được ghi nhận trong báo cáo chất lượng dữ liệu của dự án. Xuân Trí cứ để hiển thị bình thường trên biểu đồ, xem đây là một đặc điểm dữ liệu cần lưu ý và không được ẩn đi hay coi đó là lỗi thiết kế.

---

## 6. Giai Đoạn 5: Xây Dựng Sidebar Navigation & Reset Bookmark
Đây là phần quan trọng để tạo trải nghiệm đồng nhất và tương tác tốt trên báo cáo:

### 6.1. Thiết lập thanh Sidebar Navigation (5 Buttons)
Trên sidebar bên trái, tạo 5 nút tương ứng với 5 trang báo cáo:

1.  **Tổng quan** (Overview) -> Gán Action: *Page navigation* -> chọn Page: `Overview`
2.  **Xu hướng doanh thu** (Sales Trend) -> Gán Action: *Page navigation* -> chọn Page: `Sales Trend` (kiểm tra lại tên kỹ thuật trang thực tế xem có dấu cách hay không).
3.  **Khách hàng** (Customers) -> **Đây là trang hiện tại.** Cần thiết kế nút này có trạng thái active nổi bật hơn (ví dụ: đổi màu nền nút sáng hơn, đổi màu chữ nổi bật hơn các nút còn lại). Gán Action: *None* hoặc *Page navigation* tự điều hướng về chính trang hiện tại.
4.  **Sản phẩm** (Products) -> Gán Action: *Page navigation* -> chọn Page: `Products`
5.  **Vận hành** (Operations) -> Gán Action: *Page navigation* -> chọn Page: `Operations`

> [!WARNING]
> Đặt tên nội bộ cho các nút này trong Selection Pane theo format: `BTN_Customers_<TargetPage>` (ví dụ: `BTN_Customers_Overview`, `BTN_Customers_SalesTrend`).

### 6.2. Thiết lập Button Reset Filter bằng Bookmark
Để người dùng dễ dàng xoá sạch bộ lọc về trạng thái ban đầu:
1.  **Chuẩn bị**: Đặt toàn bộ các slicer trên trang `Customers` về trạng thái mặc định (chọn "All" hoặc không chọn mục nào).
2.  **Tạo Bookmark**:
    *   Mở thẻ View trên thanh công cụ -> Bật bảng **Bookmarks** và bảng **Selection**.
    *   Trong bảng Bookmarks, chọn **Add** để tạo bookmark mới.
    *   Chuột phải vào bookmark vừa tạo, đổi tên chính xác thành `BM_Reset_Customers`.
3.  **Gán cho Nút Reset**:
    *   Chọn nút bấm Reset trên trang (nằm ở Reset area).
    *   Trong bảng Format của nút bấm, bật phần **Action**.
    *   Chọn **Type = Bookmark**, và chọn **Bookmark = BM_Reset_Customers**.

---

## 7. Giai Đoạn 6: Hướng Dẫn Phân Tích & Rút Ra Insights
Để phần bàn giao trang Customers đạt chất lượng cao nhất, Xuân Trí cần quan sát biểu đồ sau khi hoàn thành và rút ra từ **3 - 5 nhận xét (insight) ngắn gọn**, có kèm dẫn chứng số liệu. Một số hướng phân tích đề xuất:

1.  **Phân khúc chủ lực**: Phân khúc nào (`Consumer`, `Corporate`, `Home Office`) đang tạo ra tổng doanh thu lớn nhất? Tỷ trọng doanh thu của phân khúc đó chiếm khoảng bao nhiêu phần trăm?
2.  **Chất lượng phân khúc**: Phân khúc tạo ra doanh thu lớn nhất có phải là phân khúc có giá trị chi tiêu trung bình trên mỗi khách hàng (`Revenue per Customer`) cao nhất không? Hay có phân khúc nào số lượng khách hàng ít hơn nhưng chi tiêu trung bình lại vượt trội?
3.  **Điểm sáng địa lý**: Những thành phố nào đóng góp doanh thu hoặc số lượng khách hàng nổi bật nhất? Có sự tập trung doanh thu ở một vài thành phố lớn không?
4.  **Biến động theo thời gian**: Xu hướng doanh thu theo tháng của các phân khúc có ổn định không? Có tháng nào doanh thu đột biến hay sụt giảm nghiêm trọng ở một phân khúc cụ thể không?

---

## 8. Giai Đoạn 7: Checklist Bàn Giao (Handover Checklist)
Khi hoàn thành trang, Xuân Trí tiến hành kiểm tra lại toàn bộ và chuẩn bị các mục sau để gửi cho Đức Phúc gộp file final:

- [ ] File Power BI đã lưu với tên: `Dashboard_XuanTri_Customers.pbix`.
- [ ] Chụp 1 ảnh màn hình (Screenshot) trang khách hàng hoàn chỉnh sau khi thiết kế.
- [ ] Cung cấp danh sách các thẻ KPI cards đã cấu hình (gồm tên measure và nhãn tiếng Việt).
- [ ] Cung cấp danh sách các biểu đồ cùng với tiêu đề dạng câu hỏi tiếng Việt tương ứng.
- [ ] Cung cấp danh sách các slicer đã sử dụng.
- [ ] Xác nhận đã tạo bookmark reset tên là `BM_Reset_Customers` và gán thành công vào nút Reset.
- [ ] File tài liệu ghi chú 3 - 5 insight có số liệu cụ thể rút ra từ biểu đồ để phục vụ viết báo cáo và làm slide.
- [ ] Ghi chú rõ nếu có chỉnh sửa layout hoặc container trong file PowerPoint background template.
- [ ] Ghi chú chi tiết nếu có tạo thêm bất kỳ measure DAX mới nào (công thức, lý do).

---
> [!TIP]
> Hãy thực hiện đúng các quy định về đặt tên visual trong Selection Pane để Đức Phúc dễ dàng quản lý layout khi gộp trang. Mọi thắc mắc về dữ liệu hoặc các lỗi phát sinh, hãy thảo luận sớm trên group chat của nhóm để thống nhất giải quyết. Chúc Xuân Trí hoàn thành xuất sắc task này!

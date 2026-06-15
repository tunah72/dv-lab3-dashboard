# Hướng Dẫn Thiết Kế Trang Sales Trend

Owner: Dương Tuấn Anh

File Power BI làm việc đề xuất: `Dashboard_TuanAnh_SalesTrend.pbix`

Tên hiển thị trên dashboard: **Xu hướng doanh thu**

Trước khi thực hiện, đọc `docs/convention_note.md` để tuân thủ convention chung về layout, font, chart title, navigation, reset bookmark và bàn giao.

## 1. Tài Liệu Cần Đọc

- `docs/powerbi_data_model_guide.md`: đọc phần `Date`, `orders`, `order_items`, `customers`, `promotions` và luồng phân tích doanh thu theo thời gian.
- `docs/powerbi_dax_measures_dictionary.md`: đọc nhóm `Revenue`, `Orders`, `Time Intelligence`.

## 2. Mục Tiêu Trang Sales Trend

Trang Sales Trend trả lời các câu hỏi:

1. Doanh thu thay đổi như thế nào theo tháng?
2. Số đơn hàng có tăng/giảm cùng chiều với doanh thu không?
3. Doanh thu hiện tại so với cùng kỳ năm trước như thế nào?
4. Phân khúc khách hàng nào đóng góp doanh thu lớn nhất theo thời gian?
5. Giai đoạn nào có biến động MoM/YoY đáng chú ý?

## 3. KPI Cards

| Visual name | Measure | Label hiển thị |
|---|---|---|
| `KPI_SalesTrend_TotalRevenue` | `Total Revenue` | Tổng doanh thu |
| `KPI_SalesTrend_NetRevenue` | `Net Revenue` | Doanh thu ròng |
| `KPI_SalesTrend_AOV` | `Average Order Value` | Giá trị trung bình mỗi đơn |
| `KPI_SalesTrend_YoY` | `Revenue YoY %` | Tăng trưởng YoY |

Có thể thay `Net Revenue` bằng `Revenue MoM %` nếu muốn nhấn mạnh biến động theo tháng.

## 4. Measures Và Fields Cần Dùng

| Mục đích | Field/Measure |
|---|---|
| Axis thời gian | `Date[Year Month]` |
| Slicer năm | `Date[Year]` |
| Breakdown segment | `customers[Segment]` |
| Discount | `promotions[discount]`, `Average Discount` |
| Doanh thu | `Total Revenue`, `Net Revenue`, `Revenue YTD` |
| Đơn hàng | `Total Orders`, `Average Order Value` |
| Tăng trưởng | `Revenue MoM %`, `Revenue YoY %`, `Revenue Previous Year`, `Revenue YoY Change` |

## 5. Biểu Đồ Đề Xuất

### Chart 1

Title: **Doanh thu và số đơn hàng thay đổi như thế nào theo thời gian?**

Visual: Line and clustered column chart

| Bucket | Field/Measure |
|---|---|
| X-axis | `Date[Year Month]` |
| Column y-axis | `Total Revenue` |
| Line y-axis | `Total Orders` |
| Tooltip | `Revenue MoM %`, `Revenue YoY %`, `Average Order Value` |

Mục đích: xem xu hướng doanh thu và kiểm tra số đơn hàng có biến động cùng chiều hay không.

### Chart 2

Title: **Doanh thu hiện tại có vượt doanh thu cùng kỳ năm trước không?**

Visual: Line chart

| Bucket | Field/Measure |
|---|---|
| X-axis | `Date[Year Month]` |
| Y-axis | `Total Revenue`, `Revenue Previous Year` |
| Tooltip | `Revenue YoY Change`, `Revenue YoY %` |

Mục đích: so sánh doanh thu hiện tại với cùng kỳ năm trước để rút ra nhận xét YoY.

### Chart 3

Title: **Phân khúc khách hàng nào đóng góp doanh thu nhiều nhất theo thời gian?**

Visual: Ribbon chart

| Bucket | Field/Measure |
|---|---|
| X-axis | `Date[Year Month]` |
| Legend | `customers[Segment]` |
| Y-axis | `Total Revenue` |
| Tooltip | `Revenue YoY %`, `Average Order Value` |

Mục đích: theo dõi thứ hạng đóng góp doanh thu của từng segment.

### Chart 4

Title: **Tháng nào có hiệu suất doanh thu mạnh nhất hoặc yếu nhất?**

Visual: Matrix hoặc Table

| Bucket | Field/Measure |
|---|---|
| Rows | `Date[Year Month]` |
| Values | `Total Revenue`, `Total Orders`, `Average Order Value`, `Revenue MoM %`, `Revenue YoY %` |

Mục đích: đọc số liệu chi tiết theo tháng để tìm tháng tăng trưởng mạnh, tháng sụt giảm hoặc tháng có AOV bất thường.

Chart thay thế nếu không dùng Matrix:

- Title: **Mức discount có liên quan đến doanh thu và số đơn hàng không?**
- Visual: Scatter chart
- X-axis: `Average Discount`
- Y-axis: `Total Revenue`
- Size: `Total Orders`
- Legend: `customers[Segment]`

## 6. Filters / Slicers

| Slicer name | Field | Title hiển thị | Kiểu hiển thị |
|---|---|---|---|
| `SL_SalesTrend_Year` | `Date[Year]` | Năm | Dropdown hoặc tile ngắn |
| `SL_SalesTrend_Month` | `Date[Year Month]` | Tháng | Dropdown |
| `SL_SalesTrend_Segment` | `customers[Segment]` | Phân khúc khách hàng | Dropdown/list |
| `SL_SalesTrend_Discount` | `promotions[discount]` | Mức giảm giá | Dropdown hoặc range nếu phù hợp |

Nếu không đủ chỗ, ưu tiên `Date[Year]`, `Date[Year Month]`, `customers[Segment]`.

## 7. Insight Cần Rút Ra

- Doanh thu cao nhất vào tháng/năm nào?
- Doanh thu và số đơn hàng có tăng/giảm cùng nhau không?
- Tăng trưởng YoY đang tích cực hay tiêu cực?
- Phân khúc nào đóng góp doanh thu lớn nhất?
- Có tháng nào revenue tăng nhưng AOV giảm hoặc ngược lại không?

## 8. Bàn Giao

Gửi cho Đức Phúc theo checklist trong `docs/convention_note.md`, kèm 3-5 insight có số liệu hoặc bằng chứng từ chart.

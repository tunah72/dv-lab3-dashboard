# Hướng Dẫn Thiết Kế Trang Overview

Owner: Lê Đức Phúc

File Power BI làm việc đề xuất: `Dashboard_DucPhuc_Overview_Operations.pbix`

Tên hiển thị trên dashboard: **Tổng quan**

Trước khi thực hiện, đọc `docs/convention_note.md` để tuân thủ convention chung về layout, font, chart title, navigation, reset bookmark và bàn giao.

## 1. Tài Liệu Cần Đọc

- `docs/powerbi_data_model_guide.md`: đọc phần gợi ý theo page `Overview` và các luồng doanh thu, khách hàng, sản phẩm, vận hành.
- `docs/powerbi_dax_measures_dictionary.md`: đọc nhóm `Revenue`, `Orders`, `Returns`, `Shipments`.
- Đọc nhanh các file hướng dẫn `SalesTrend.md`, `Customers.md`, `Products.md`, `Operations.md` để Overview tóm tắt đúng nội dung toàn dashboard.

## 2. Mục Tiêu Trang Overview

Trang Overview là trang mở đầu và storyboard tổng quan. Trang này không đi quá sâu vào một mảng, mà trả lời:

1. Tình hình kinh doanh tổng thể đang như thế nào?
2. Doanh thu, đơn hàng và return rate ở mức nào?
3. Doanh thu thay đổi ra sao theo thời gian?
4. Phân khúc/danh mục nào là điểm nổi bật?
5. Vận hành giao hàng có rủi ro nào cần chú ý không?

## 3. KPI Cards

| Visual name | Measure | Label hiển thị |
|---|---|---|
| `KPI_Overview_TotalRevenue` | `Total Revenue` | Tổng doanh thu |
| `KPI_Overview_NetRevenue` | `Net Revenue` | Doanh thu ròng |
| `KPI_Overview_TotalOrders` | `Total Orders` | Tổng đơn hàng |
| `KPI_Overview_ReturnRate` | `Return Rate` | Tỷ lệ hoàn trả |

## 4. Measures Và Fields Cần Dùng

| Mục đích | Field/Measure |
|---|---|
| Thời gian | `Date[Year]`, `Date[Year Month]` |
| Segment khách hàng | `customers[Segment]` |
| Danh mục sản phẩm | `categories[category_name]` |
| Thành phố cửa hàng | `stores[city]` |
| Trạng thái vận chuyển | `shipments[status]` |
| Tổng quan | `Total Revenue`, `Net Revenue`, `Total Orders`, `Return Rate`, `Revenue YTD` |
| Vận hành | `Delivered Shipments`, `Shipped Shipments`, `Late Shipments`, `Late Shipment Rate` |

## 5. Biểu Đồ Đề Xuất

### Chart 1

Title: **Doanh thu tổng thể thay đổi như thế nào theo thời gian?**

Visual: Line chart

| Bucket | Field/Measure |
|---|---|
| X-axis | `Date[Year Month]` |
| Y-axis | `Total Revenue` hoặc `Revenue YTD` |
| Tooltip | `Net Revenue`, `Total Orders`, `Return Rate` |

Mục đích: mở đầu dashboard bằng xu hướng kinh doanh tổng thể.

### Chart 2

Title: **Phân khúc khách hàng nào đóng góp doanh thu chính?**

Visual: Bar chart

| Bucket | Field/Measure |
|---|---|
| Axis | `customers[Segment]` |
| Values | `Total Revenue` |
| Tooltip | `Total Orders`, `Revenue per Customer` |

Mục đích: tóm tắt nhanh điểm nổi bật của trang Customers.

### Chart 3

Title: **Danh mục sản phẩm nào tạo ra nhiều doanh thu nhất?**

Visual: Bar chart hoặc Treemap

| Bucket | Field/Measure |
|---|---|
| Group/Axis | `categories[category_name]` |
| Values | `Total Revenue` |
| Tooltip | `Total Quantity`, `Return Rate` |

Mục đích: tóm tắt nhanh điểm nổi bật của trang Products.

### Chart 4

Title: **Tình trạng vận chuyển có rủi ro cần chú ý không?**

Visual: Bar chart hoặc Donut chart

| Bucket | Field/Measure |
|---|---|
| Legend/Axis | `shipments[status]` |
| Values | `Shipment Count` |
| Tooltip | `Delivered Shipment Rate`, `Late Shipment Rate`, `Late Shipments` |

Mục đích: tóm tắt nhanh tình trạng vận hành và rủi ro late shipment.

## 6. Filters / Slicers

| Slicer name | Field | Title hiển thị | Kiểu hiển thị |
|---|---|---|---|
| `SL_Overview_Year` | `Date[Year]` | Năm | Dropdown hoặc tile ngắn |
| `SL_Overview_Month` | `Date[Year Month]` | Tháng | Dropdown |
| `SL_Overview_Segment` | `customers[Segment]` | Phân khúc khách hàng | Dropdown/list |
| `SL_Overview_Category` | `categories[category_name]` | Danh mục sản phẩm | Dropdown/list |

Nếu filter area còn chỗ, có thể thêm `stores[city]` hoặc `shipments[status]`.

## 7. Insight Cần Rút Ra

- Doanh thu và net revenue tổng thể đang ở mức nào?
- Xu hướng doanh thu tăng, giảm hay biến động theo mùa?
- Phân khúc hoặc danh mục nào là điểm nổi bật nhất?
- Return rate có đáng chú ý không?
- Shipment status có rủi ro late shipment cần nhắc trong kết luận không?

## 8. Lưu Ý Khi Làm Overview

- Nên làm Overview sau khi đã xem nhanh các trang Sales Trend, Customers, Products, Operations.
- Không đưa quá nhiều chi tiết vào Overview; chỉ chọn insight đại diện.
- Overview phải dẫn dắt người xem đi tiếp sang các trang phân tích chuyên sâu.
- Navigation và active state của Overview phải rõ vì đây là trang đầu tiên.

## 9. Bàn Giao

Vì Đức Phúc là người tổng hợp final, sau khi xong Overview cần kiểm tra lại toàn bộ page order, navigation, reset bookmark và style đồng bộ giữa 5 trang.

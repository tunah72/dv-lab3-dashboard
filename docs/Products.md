# Hướng Dẫn Thiết Kế Trang Products

Owner: Nguyễn Trần Trung Kiên

File Power BI làm việc đề xuất: `Dashboard_TrungKien_Products.pbix`

Tên hiển thị trên dashboard: **Sản phẩm**

Trước khi thực hiện, đọc `docs/convention_note.md` để tuân thủ convention chung về layout, font, chart title, navigation, reset bookmark và bàn giao.

## 1. Tài Liệu Cần Đọc

- `docs/powerbi_data_model_guide.md`: đọc phần `products`, `categories`, `suppliers`, `order_items`, `returns` và luồng doanh thu theo danh mục/supplier.
- `docs/powerbi_dax_measures_dictionary.md`: đọc nhóm `Operations`, `Orders`, `Revenue`, `Returns`.

## 2. Mục Tiêu Trang Products

Trang Products trả lời các câu hỏi:

1. Danh mục sản phẩm nào tạo ra doanh thu cao nhất?
2. Danh mục nào bán được nhiều số lượng nhất?
3. Nhóm sản phẩm/danh mục nào có rủi ro hoàn trả cao?
4. Nhà cung cấp hoặc quốc gia nhà cung cấp nào đóng góp nhiều sản phẩm/doanh thu?
5. Doanh thu sản phẩm thay đổi như thế nào theo thời gian?

## 3. KPI Cards

| Visual name | Measure | Label hiển thị |
|---|---|---|
| `KPI_Products_TotalProducts` | `Total Products` | Tổng sản phẩm |
| `KPI_Products_TotalCategories` | `Total Categories` | Tổng danh mục |
| `KPI_Products_TotalQuantity` | `Total Quantity` | Tổng số lượng bán |
| `KPI_Products_ReturnRate` | `Return Rate` | Tỷ lệ hoàn trả |

## 4. Measures Và Fields Cần Dùng

| Mục đích | Field/Measure |
|---|---|
| Danh mục | `categories[category_name]` |
| Quốc gia nhà cung cấp | `suppliers[country]` |
| Thời gian | `Date[Year]`, `Date[Year Month]` |
| Doanh thu | `Total Revenue`, `Net Revenue` |
| Số lượng | `Total Quantity` |
| Hoàn trả | `Return Count`, `Returned Item Count`, `Return Rate`, `Total Refund` |
| Sản phẩm/Nhà cung cấp | `Total Products`, `Total Categories`, `Total Suppliers` |

## 5. Biểu Đồ Đề Xuất

### Chart 1

Title: **Danh mục sản phẩm nào tạo ra nhiều doanh thu nhất?**

Visual: Bar chart hoặc Treemap

| Bucket | Field/Measure |
|---|---|
| Axis/Group | `categories[category_name]` |
| Values | `Total Revenue` |
| Tooltip | `Total Quantity`, `Return Rate`, `Total Refund` |

Mục đích: xác định danh mục chủ lực về doanh thu.

### Chart 2

Title: **Danh mục nào bán được nhiều số lượng nhất?**

Visual: Column chart

| Bucket | Field/Measure |
|---|---|
| X-axis | `categories[category_name]` |
| Y-axis | `Total Quantity` |
| Tooltip | `Total Revenue`, `Return Rate` |

Mục đích: phân biệt danh mục bán nhiều về số lượng với danh mục tạo doanh thu cao.

### Chart 3

Title: **Danh mục nào có tỷ lệ hoàn trả đáng chú ý?**

Visual: Bar chart

| Bucket | Field/Measure |
|---|---|
| Y-axis | `categories[category_name]` |
| X-axis | `Return Rate` |
| Tooltip | `Return Count`, `Returned Item Count`, `Total Refund` |

Mục đích: phát hiện rủi ro chất lượng hoặc trải nghiệm khách hàng ở từng danh mục.

### Chart 4

Title: **Quốc gia nhà cung cấp nào đóng góp nhiều sản phẩm hoặc doanh thu?**

Visual: Matrix hoặc Bar chart

| Bucket | Field/Measure |
|---|---|
| Rows/Axis | `suppliers[country]` |
| Values | `Total Suppliers`, `Total Products`, `Total Revenue`, `Total Quantity` |

Mục đích: đánh giá đóng góp theo nguồn cung.

Chart thay thế:

- Title: **Doanh thu sản phẩm thay đổi như thế nào theo thời gian?**
- Visual: Line chart
- X-axis: `Date[Year Month]`
- Legend: `categories[category_name]`
- Y-axis: `Total Revenue`

## 6. Filters / Slicers

| Slicer name | Field | Title hiển thị | Kiểu hiển thị |
|---|---|---|---|
| `SL_Products_Year` | `Date[Year]` | Năm | Dropdown hoặc tile ngắn |
| `SL_Products_Month` | `Date[Year Month]` | Tháng | Dropdown |
| `SL_Products_Category` | `categories[category_name]` | Danh mục sản phẩm | Dropdown/list |
| `SL_Products_SupplierCountry` | `suppliers[country]` | Quốc gia nhà cung cấp | Dropdown/list |

## 7. Insight Cần Rút Ra

- Danh mục nào tạo doanh thu cao nhất?
- Danh mục bán nhiều nhất có trùng với danh mục doanh thu cao nhất không?
- Danh mục nào có `Return Rate` hoặc `Total Refund` cao?
- Quốc gia nhà cung cấp nào đóng góp nhiều sản phẩm/doanh thu?
- Có danh mục nào doanh thu tốt nhưng hoàn trả cũng cao không?

## 8. Bàn Giao

Gửi cho Đức Phúc theo checklist trong `docs/convention_note.md`, kèm 3-5 insight có số liệu hoặc bằng chứng từ chart.

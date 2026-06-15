# Hướng Dẫn Thiết Kế Trang Customers

Owner: Lê Xuân Trí

File Power BI làm việc đề xuất: `Dashboard_XuanTri_Customers.pbix`

Tên hiển thị trên dashboard: **Khách hàng**

Trước khi thực hiện, đọc `docs/convention_note.md` để tuân thủ convention chung về layout, font, chart title, navigation, reset bookmark và bàn giao.

## 1. Tài Liệu Cần Đọc

- `docs/powerbi_data_model_guide.md`: đọc phần `customers`, `orders`, `order_items`, `Date` và luồng doanh thu theo segment khách hàng.
- `docs/powerbi_dax_measures_dictionary.md`: đọc nhóm `Customers`, `Revenue`, `Orders`.

## 2. Mục Tiêu Trang Customers

Trang Customers trả lời các câu hỏi:

1. Phân khúc khách hàng nào tạo ra nhiều doanh thu nhất?
2. Phân khúc nào có giá trị doanh thu trên mỗi khách hàng cao nhất?
3. Thành phố nào có lượng khách hàng hoặc doanh thu nổi bật?
4. Doanh thu theo segment thay đổi như thế nào theo thời gian?
5. Nhóm khách hàng nào nên được ưu tiên trong chiến lược kinh doanh?

## 3. KPI Cards

| Visual name | Measure | Label hiển thị |
|---|---|---|
| `KPI_Customers_TotalCustomers` | `Total Customers` | Tổng khách hàng |
| `KPI_Customers_RevenuePerCustomer` | `Revenue per Customer` | Doanh thu trên mỗi khách hàng |
| `KPI_Customers_TotalOrders` | `Total Orders` | Tổng đơn hàng |
| `KPI_Customers_ItemsPerOrder` | `Items per Order` | Số dòng hàng mỗi đơn |

## 4. Measures Và Fields Cần Dùng

| Mục đích | Field/Measure |
|---|---|
| Segment khách hàng | `customers[Segment]` |
| Thành phố khách hàng | `customers[city]` |
| Thời gian | `Date[Year]`, `Date[Year Month]` |
| Doanh thu | `Total Revenue`, `Revenue per Customer` |
| Đơn hàng | `Total Orders`, `Items per Order` |
| Khách hàng | `Total Customers` |

## 5. Biểu Đồ Đề Xuất

### Chart 1

Title: **Phân khúc khách hàng nào tạo ra nhiều doanh thu nhất?**

Visual: Bar chart

| Bucket | Field/Measure |
|---|---|
| Y-axis | `customers[Segment]` |
| X-axis | `Total Revenue` |
| Tooltip | `Total Customers`, `Revenue per Customer`, `Total Orders` |

Mục đích: xác định segment đóng góp doanh thu chính.

### Chart 2

Title: **Thành phố khách hàng nào đóng góp doanh thu nổi bật nhất?**

Visual: Bar chart hoặc Map nếu dữ liệu hiển thị tốt

| Bucket | Field/Measure |
|---|---|
| Axis/Location | `customers[city]` |
| Values | `Total Revenue` |
| Tooltip | `Total Customers`, `Revenue per Customer` |

Mục đích: xem phân bố doanh thu theo địa lý khách hàng.

### Chart 3

Title: **Doanh thu theo phân khúc thay đổi như thế nào theo thời gian?**

Visual: Line chart

| Bucket | Field/Measure |
|---|---|
| X-axis | `Date[Year Month]` |
| Legend | `customers[Segment]` |
| Y-axis | `Total Revenue` |
| Tooltip | `Revenue per Customer`, `Total Orders` |

Mục đích: so sánh xu hướng doanh thu giữa các segment.

### Chart 4

Title: **Phân khúc nào có giá trị trung bình trên mỗi khách hàng cao nhất?**

Visual: Matrix hoặc Table

| Bucket | Field/Measure |
|---|---|
| Rows | `customers[Segment]` |
| Values | `Total Customers`, `Total Revenue`, `Revenue per Customer`, `Total Orders`, `Items per Order` |

Mục đích: đánh giá chất lượng segment, không chỉ nhìn vào tổng doanh thu.

Chart thay thế:

- Title: **Tỷ trọng khách hàng theo từng phân khúc là bao nhiêu?**
- Visual: Donut chart
- Legend: `customers[Segment]`
- Values: `Total Customers`

## 6. Filters / Slicers

| Slicer name | Field | Title hiển thị | Kiểu hiển thị |
|---|---|---|---|
| `SL_Customers_Year` | `Date[Year]` | Năm | Dropdown hoặc tile ngắn |
| `SL_Customers_Month` | `Date[Year Month]` | Tháng | Dropdown |
| `SL_Customers_Segment` | `customers[Segment]` | Phân khúc khách hàng | Dropdown/list |
| `SL_Customers_City` | `customers[city]` | Thành phố khách hàng | Dropdown |

## 7. Insight Cần Rút Ra

- Phân khúc nào có tổng doanh thu cao nhất?
- Phân khúc nào có `Revenue per Customer` cao nhất?
- Thành phố nào đóng góp doanh thu hoặc số khách hàng nổi bật?
- Có segment nào tăng/giảm rõ theo thời gian không?
- Phân khúc nhiều khách nhất có phải phân khúc tạo giá trị cao nhất không?

## 8. Bàn Giao

Gửi cho Đức Phúc theo checklist trong `docs/convention_note.md`, kèm 3-5 insight có số liệu hoặc bằng chứng từ chart.

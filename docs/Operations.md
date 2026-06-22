# Hướng Dẫn Thiết Kế Trang Operations

Owner: Lê Đức Phúc

File Power BI làm việc đề xuất: `Dashboard_DucPhuc_Overview_Operations.pbix`

Tên hiển thị trên dashboard: **Vận hành**

Trước khi thực hiện, đọc `docs/convention_note.md` để tuân thủ convention chung về layout, font, chart title, navigation, reset bookmark và bàn giao.

## 1. Tài Liệu Cần Đọc

- `docs/powerbi_data_model_guide.md`: đọc phần `stores`, `employees`, `shipments`, `orders`, `Date` và luồng phân tích vận hành.
- `docs/powerbi_dax_measures_dictionary.md`: đọc nhóm `Operations`, `Shipments`, `Revenue`, `Orders`.

## 2. Mục Tiêu Trang Operations

Trang Operations trả lời các câu hỏi:

1. Thành phố/cửa hàng nào tạo ra doanh thu và số đơn hàng nổi bật?
2. Tình trạng vận chuyển đang phân bổ như thế nào?
3. Tỷ lệ giao hàng trễ có đáng lo ngại không?
4. Late shipments thay đổi như thế nào theo thời gian?
5. Hiệu suất vận hành giữa các thành phố/cửa hàng khác nhau ra sao?

## 3. KPI Cards

| Visual name | Measure | Label hiển thị |
|---|---|---|
| `KPI_Operations_TotalStores` | `Total Stores` | Tổng cửa hàng |
| `KPI_Operations_TotalEmployees` | `Total Employees` | Tổng nhân viên |
| `KPI_Operations_AverageSalary` | `Average Salary` | Lương trung bình |
| `KPI_Operations_LateShipmentRate` | `Late Shipment Rate` | Tỷ lệ giao trễ |

## 4. Measures Và Fields Cần Dùng

| Mục đích | Field/Measure |
|---|---|
| Thành phố cửa hàng | `stores[city]` |
| Trạng thái vận chuyển | `shipments[status]` |
| Thời gian | `Date[Year]`, `Date[Year Month]` |
| Doanh thu/Đơn hàng | `Total Revenue`, `Total Orders` |
| Shipment | `Shipment Count`, `Delivered Shipments`, `Shipped Shipments`, `Late Shipments`, `Delivered Shipment Rate`, `Late Shipment Rate` |
| Nhân sự | `Total Stores`, `Total Employees`, `Average Salary` |

## 5. Biểu Đồ Đề Xuất

### Chart 1

Title: **Thành phố cửa hàng nào tạo ra doanh thu cao nhất?**

Visual: Bar chart

| Bucket | Field/Measure |
|---|---|
| Y-axis | `stores[city]` |
| X-axis | `Total Revenue` |
| Tooltip | `Total Orders`, `Total Stores`, `Total Employees` |

Mục đích: xác định khu vực vận hành đóng góp doanh thu chính.

### Chart 2

Title: **Tình trạng vận chuyển đang phân bổ như thế nào?**

Visual: Donut chart hoặc Bar chart

| Bucket | Field/Measure |
|---|---|
| Legend/Axis | `shipments[status]` |
| Values | `Shipment Count` |
| Tooltip | `Delivered Shipment Rate`, `Late Shipment Rate` |

Mục đích: xem tỷ trọng delivered, shipped, late.

### Chart 3

Title: **Late shipments thay đổi như thế nào theo thời gian?**

Visual: Line and clustered column chart

| Bucket | Field/Measure |
|---|---|
| X-axis | `Date[Year Month]` |
| Column y-axis | `Late Shipments` |
| Line y-axis | `Late Shipment Rate` |
| Tooltip | `Shipment Count`, `Delivered Shipment Rate` |

Mục đích: theo dõi rủi ro giao hàng trễ theo thời gian.

### Chart 4

Title: **Quy mô nhân sự và doanh thu các thành phố ra sao?**

Visual: Lollipop Chart (Deneb / Vega-Lite)

| Bucket | Field/Measure |
|---|---|
| Y-axis | `stores[city]` |
| X-axis (Độ dài) | `Total Employees` |
| Point Size (Độ lớn) | `Total Revenue` |
| Tooltip | `Total Orders`, `Average Salary`, `Late Shipment Rate` |

Mục đích: So sánh quy mô vận hành của các thành phố.

## 6. Filters / Slicers

| Slicer name | Field | Title hiển thị | Kiểu hiển thị |
|---|---|---|---|
| `SL_Operations_Year` | `Date[Year]` | Năm | Dropdown hoặc tile ngắn |
| `SL_Operations_Month` | `Date[Year Month]` | Tháng | Dropdown |
| `SL_Operations_StoreCity` | `stores[city]` | Thành phố cửa hàng | Dropdown/list |
| `SL_Operations_ShipmentStatus` | `shipments[status]` | Trạng thái vận chuyển | Dropdown/list |

## 7. Insight Cần Rút Ra

- Thành phố nào tạo doanh thu hoặc số đơn hàng cao nhất?
- Shipment status nào chiếm tỷ trọng lớn nhất?
- `Late Shipment Rate` có cao không và tập trung ở giai đoạn nào?
- Thành phố nào có hiệu suất vận hành tốt/yếu?
- Lương trung bình hoặc số nhân viên có liên quan gì đến hiệu suất vận hành không?

## 8. Bàn Giao

Vì Đức Phúc là người tổng hợp final, sau khi xong Operations cần tự chụp screenshot, ghi 3-5 insight và kiểm tra navigation/reset giống các trang còn lại.
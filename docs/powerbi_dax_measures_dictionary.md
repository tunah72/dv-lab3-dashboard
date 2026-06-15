# Từ Điển DAX Measures Power BI

Owner: Dương Tuấn Anh

Workspace: `D:\School\DV\dv-lab3-dashboard`

Power BI file: `Dashboard.pbix`

Cập nhật: 2026-06-14

## Tổng Quan

Tất cả DAX measures được đặt trong bảng `_Measures`. Bảng này gồm 36 measures và được chia theo các display folder:

| Folder | Nhóm chỉ số |
|---|---|
| `Revenue` | Doanh thu, thanh toán, refund, discount, AOV |
| `Orders` | Đơn hàng, số lượng, order items |
| `Customers` | Khách hàng và giá trị trên mỗi khách hàng |
| `Returns` | Đơn trả, hàng trả, refund, return rate |
| `Shipments` | Số lượng shipment và tỉ lệ trạng thái vận chuyển |
| `Operations` | Cửa hàng, nhân viên, sản phẩm, danh mục, nhà cung cấp |
| `Time Intelligence` | Previous month, MoM, previous year, YoY, YTD |

Khi làm report, ưu tiên dùng measures trong `_Measures` thay vì kéo trực tiếp cột numeric vào visual.

## Revenue

| Measure | DAX | Format | Ý nghĩa | Gợi ý sử dụng |
|---|---|---|---|---|
| `Total Revenue` | `SUM ( 'order_items'[line_revenue] )` | Currency | Tổng doanh thu gộp từ các dòng sản phẩm trong đơn hàng | KPI doanh thu, revenue trend, revenue by segment/category/store |
| `Total Payments` | `SUM ( 'payments'[amount] )` | Currency | Tổng số tiền đã thanh toán | So sánh payment với revenue |
| `Total Refund` | `SUM ( 'returns'[refund] )` | Currency | Tổng tiền hoàn trả | KPI refund, return analysis |
| `Net Revenue` | `[Total Revenue] - [Total Refund]` | Currency | Doanh thu sau khi trừ refund | KPI doanh thu thực nhận |
| `Payment Gap` | `[Total Payments] - [Total Revenue]` | Currency | Chênh lệch giữa payment và gross revenue | Reconciliation chart |
| `Average Order Value` | `DIVIDE ( [Total Revenue], [Total Orders] )` | Currency | Doanh thu trung bình trên mỗi đơn hàng | KPI revenue page |
| `Average Discount` | `AVERAGE ( 'promotions'[discount] )` | Percentage | Discount trung bình của promotion | Phân tích khuyến mãi |

## Orders

| Measure | DAX | Format | Ý nghĩa | Gợi ý sử dụng |
|---|---|---|---|---|
| `Total Orders` | `DISTINCTCOUNT ( 'orders'[order_id] )` | Whole number | Số đơn hàng duy nhất | KPI, order trend, store performance |
| `Total Quantity` | `SUM ( 'order_items'[qty] )` | Whole number | Tổng số lượng sản phẩm bán ra | Product/category analysis |
| `Order Item Count` | `DISTINCTCOUNT ( 'order_items'[order_item_id] )` | Whole number | Số dòng chi tiết đơn hàng duy nhất | Mẫu số của return rate |
| `Items per Order` | `DIVIDE ( [Order Item Count], [Total Orders] )` | Decimal | Số dòng sản phẩm trung bình trên mỗi đơn | Basket-size KPI |

## Customers

| Measure | DAX | Format | Ý nghĩa | Gợi ý sử dụng |
|---|---|---|---|---|
| `Total Customers` | `DISTINCTCOUNT ( 'customers'[customer_id] )` | Whole number | Số khách hàng duy nhất | KPI customer page |
| `Revenue per Customer` | `DIVIDE ( [Total Revenue], [Total Customers] )` | Currency | Doanh thu trung bình trên mỗi khách hàng | So sánh giá trị theo segment |

## Returns

| Measure | DAX | Format | Ý nghĩa | Gợi ý sử dụng |
|---|---|---|---|---|
| `Return Count` | `DISTINCTCOUNT ( 'returns'[return_id] )` | Whole number | Số giao dịch hoàn trả | KPI returns |
| `Returned Item Count` | `DISTINCTCOUNT ( 'returns'[order_item_id] )` | Whole number | Số order item bị trả | Product return analysis |
| `Return Rate` | `DIVIDE ( [Returned Item Count], [Order Item Count] )` | Percentage | Tỉ lệ item bị trả trên tổng order items | KPI, category/product quality signal |
| `Refund per Return` | `DIVIDE ( [Total Refund], [Return Count] )` | Currency | Số tiền refund trung bình trên mỗi return | Return value analysis |

## Shipments

| Measure | DAX | Format | Ý nghĩa | Gợi ý sử dụng |
|---|---|---|---|---|
| `Shipment Count` | `DISTINCTCOUNT ( 'shipments'[shipment_id] )` | Whole number | Tổng số shipment | KPI shipment |
| `Delivered Shipments` | `CALCULATE ( [Shipment Count], 'shipments'[status] = "delivered" )` | Whole number | Số shipment có trạng thái delivered | Breakdown shipment status |
| `Shipped Shipments` | `CALCULATE ( [Shipment Count], 'shipments'[status] = "shipped" )` | Whole number | Số shipment có trạng thái shipped | Breakdown shipment status |
| `Late Shipments` | `CALCULATE ( [Shipment Count], 'shipments'[status] = "late" )` | Whole number | Số shipment bị late | KPI operations |
| `Delivered Shipment Rate` | `DIVIDE ( [Delivered Shipments], [Shipment Count] )` | Percentage | Tỉ lệ shipment delivered | Operations performance |
| `Late Shipment Rate` | `DIVIDE ( [Late Shipments], [Shipment Count] )` | Percentage | Tỉ lệ shipment late | Operations risk KPI |

## Operations

| Measure | DAX | Format | Ý nghĩa | Gợi ý sử dụng |
|---|---|---|---|---|
| `Total Stores` | `DISTINCTCOUNT ( 'stores'[store_id] )` | Whole number | Số cửa hàng duy nhất | KPI operations |
| `Total Employees` | `DISTINCTCOUNT ( 'employees'[employee_id] )` | Whole number | Số nhân viên duy nhất | KPI operations |
| `Average Salary` | `AVERAGE ( 'employees'[salary] )` | Currency | Lương trung bình | Phân tích nhân sự theo cửa hàng |
| `Total Products` | `DISTINCTCOUNT ( 'products'[product_id] )` | Whole number | Số sản phẩm duy nhất | KPI products |
| `Total Categories` | `DISTINCTCOUNT ( 'categories'[category_id] )` | Whole number | Số danh mục sản phẩm | KPI products |
| `Total Suppliers` | `DISTINCTCOUNT ( 'suppliers'[supplier_id] )` | Whole number | Số nhà cung cấp duy nhất | Supplier/product analysis |

## Time Intelligence

Nhóm measures này phụ thuộc vào bảng `Date` đã được mark as date table. Khi dùng các measures này trong chart, nên dùng `Date[Year]`, `Date[Year Month]` hoặc `Date[Date]` từ bảng `Date`.

| Measure | DAX | Format | Ý nghĩa | Gợi ý sử dụng |
|---|---|---|---|---|
| `Revenue Previous Month` | `CALCULATE ( [Total Revenue], DATEADD ( 'Date'[Date], -1, MONTH ) )` | Currency | Doanh thu của tháng trước | Monthly comparison |
| `Revenue MoM Change` | `[Total Revenue] - [Revenue Previous Month]` | Currency | Chênh lệch doanh thu so với tháng trước | Revenue trend tooltip/KPI |
| `Revenue MoM %` | `DIVIDE ( [Revenue MoM Change], [Revenue Previous Month] )` | Percentage | Tỉ lệ tăng trưởng so với tháng trước | Revenue page KPI |
| `Revenue Previous Year` | `CALCULATE ( [Total Revenue], SAMEPERIODLASTYEAR ( 'Date'[Date] ) )` | Currency | Doanh thu cùng kỳ năm trước | YoY comparison |
| `Revenue YoY Change` | `[Total Revenue] - [Revenue Previous Year]` | Currency | Chênh lệch doanh thu so với năm trước | Revenue visual |
| `Revenue YoY %` | `DIVIDE ( [Revenue YoY Change], [Revenue Previous Year] )` | Percentage | Tỉ lệ tăng trưởng so với năm trước | Revenue KPI |
| `Revenue YTD` | `TOTALYTD ( [Total Revenue], 'Date'[Date] )` | Currency | Doanh thu lũy kế từ đầu năm | Cumulative revenue trend |

## Gợi Ý Dùng Measure Theo Page

| Page | KPI nên dùng | Measure cho chart |
|---|---|---|
| `Overview` | `Total Revenue`, `Net Revenue`, `Total Orders`, `Return Rate` | `Total Revenue`, `Revenue YTD`, `Delivered Shipments`, `Shipped Shipments`, `Late Shipments` |
| `Revenue` | `Total Revenue`, `Net Revenue`, `Average Order Value`, `Revenue YoY %` | `Total Revenue`, `Revenue Previous Year`, `Revenue YoY Change`, `Total Payments`, `Total Refund`, `Payment Gap`, `Average Discount` |
| `Customers` | `Total Customers`, `Revenue per Customer`, `Total Orders`, `Items per Order` | `Total Revenue`, `Revenue per Customer`, `Total Orders` |
| `Products` | `Total Products`, `Total Categories`, `Total Quantity`, `Return Rate` | `Total Revenue`, `Total Quantity`, `Total Refund`, `Return Count`, `Total Suppliers` |
| `Operations` | `Total Stores`, `Total Employees`, `Average Salary`, `Late Shipment Rate` | `Total Revenue`, `Total Orders`, `Shipment Count`, `Late Shipments`, `Delivered Shipment Rate` |

## Quy Ước Sử Dụng

- Dùng measure làm Values trong Card, KPI, Line chart, Bar chart, Matrix.
- Dùng các field business như `Date[Year Month]`, `customers[Segment]`, `categories[category_name]`, `stores[city]`, `suppliers[country]`, `shipments[status]` cho Axis, Legend và Slicer.
- Không dùng các cột ID đã ẩn để hiển thị trên report.
- Không tạo measure mới trùng ý nghĩa với measure đã có.
- Với chart thời gian, dùng field trong bảng `Date`, không dùng trực tiếp `orders[order_date]`.
- Nếu cần thêm measure cho page riêng, ghi rõ tên measure, công thức DAX và lý do thêm để leader review.

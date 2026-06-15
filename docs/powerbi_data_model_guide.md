# Hướng Dẫn Data Model Power BI

Owner: Dương Tuấn Anh

Workspace: `D:\School\DV\dv-lab3-dashboard`

Power BI file: `Dashboard.pbix`

Cập nhật: 2026-06-14

## Tổng Quan Mô Hình

Dashboard sử dụng mô hình dữ liệu dạng star/snowflake cho bài toán phân tích bán lẻ. Các bảng giao dịch lưu doanh thu, đơn hàng, thanh toán, hoàn trả và vận chuyển. Các bảng dimension bổ sung ngữ cảnh phân tích như khách hàng, cửa hàng, sản phẩm, danh mục, nhà cung cấp, khuyến mãi và thời gian.

Mô hình hiện có 14 bảng:

| Bảng | Số dòng | Vai trò |
|---|---:|---|
| `orders` | 300,000 | Fact đơn hàng |
| `order_items` | 600,000 | Fact chi tiết đơn hàng |
| `payments` | 300,000 | Fact thanh toán |
| `returns` | 30,000 | Fact hoàn trả |
| `shipments` | 300,000 | Fact vận chuyển |
| `customers` | 50,000 | Dimension khách hàng |
| `products` | 10,000 | Dimension sản phẩm |
| `categories` | 30 | Dimension danh mục sản phẩm |
| `stores` | 100 | Dimension cửa hàng |
| `employees` | 1,000 | Bảng nhân viên theo cửa hàng |
| `suppliers` | 200 | Dimension nhà cung cấp |
| `promotions` | 50 | Dimension khuyến mãi |
| `Date` | Tạo bằng DAX | Dimension thời gian |
| `_Measures` | 36 measures | Bảng chứa DAX measures |

## Grain Của Từng Bảng

Cần nắm grain trước khi dùng bảng vào visual để tránh tính sai tổng, đếm sai số dòng hoặc lặp dữ liệu.

| Bảng | Grain | Ý nghĩa phân tích |
|---|---|---|
| `orders` | 1 dòng = 1 đơn hàng | Đếm đơn hàng, ngày đặt hàng, khách hàng, cửa hàng, khuyến mãi |
| `order_items` | 1 dòng = 1 sản phẩm trong đơn hàng | Tính số lượng bán, giá, doanh thu từng dòng |
| `payments` | 1 dòng = 1 giao dịch thanh toán | Tính tổng tiền thanh toán |
| `returns` | 1 dòng = 1 sản phẩm bị trả | Tính số lượng hàng trả và tiền hoàn |
| `shipments` | 1 dòng = 1 vận đơn/trạng thái giao hàng | Phân tích delivered, shipped, late |
| `customers` | 1 dòng = 1 khách hàng | Phân tích thành phố, ngày đăng ký, phân khúc |
| `products` | 1 dòng = 1 sản phẩm | Nối sản phẩm với danh mục và nhà cung cấp |
| `categories` | 1 dòng = 1 danh mục | Phân tích doanh thu theo danh mục |
| `stores` | 1 dòng = 1 cửa hàng | Phân tích doanh thu và vận hành theo thành phố cửa hàng |
| `employees` | 1 dòng = 1 nhân viên | Phân tích nhân sự và lương theo cửa hàng |
| `suppliers` | 1 dòng = 1 nhà cung cấp | Phân tích sản phẩm/doanh thu theo quốc gia nhà cung cấp |
| `promotions` | 1 dòng = 1 chương trình khuyến mãi | Phân tích discount |
| `Date` | 1 dòng = 1 ngày | Dùng cho filter thời gian và time intelligence |

## Relationships

Tất cả relationships đang ở trạng thái active, cardinality Many-to-One và cross-filter một chiều. Cách thiết kế này giúp filter propagation ổn định và tránh ambiguous relationship.

| Từ bảng/cột | Đến bảng/cột | Cardinality | Cross filter |
|---|---|---|---|
| `orders[order_date]` | `Date[Date]` | Many to One | Single |
| `orders[customer_id]` | `customers[customer_id]` | Many to One | Single |
| `orders[store_id]` | `stores[store_id]` | Many to One | Single |
| `orders[promotion_id]` | `promotions[promotion_id]` | Many to One | Single |
| `order_items[order_id]` | `orders[order_id]` | Many to One | Single |
| `order_items[product_id]` | `products[product_id]` | Many to One | Single |
| `products[category_id]` | `categories[category_id]` | Many to One | Single |
| `products[supplier_id]` | `suppliers[supplier_id]` | Many to One | Single |
| `payments[order_id]` | `orders[order_id]` | Many to One | Single |
| `returns[order_item_id]` | `order_items[order_item_id]` | Many to One | Single |
| `shipments[order_id]` | `orders[order_id]` | Many to One | Single |
| `employees[store_id]` | `stores[store_id]` | Many to One | Single |

## Luồng Phân Tích Chính

| Nhu cầu phân tích | Luồng filter nên hiểu |
|---|---|
| Doanh thu theo thời gian | `Date` -> `orders` -> `order_items` |
| Doanh thu theo segment khách hàng | `customers` -> `orders` -> `order_items` |
| Doanh thu theo cửa hàng | `stores` -> `orders` -> `order_items` |
| Doanh thu theo danh mục | `categories` -> `products` -> `order_items` |
| Doanh thu theo nhà cung cấp | `suppliers` -> `products` -> `order_items` |
| Thanh toán so với doanh thu | `orders` nối với cả `payments` và `order_items` |
| Hoàn trả và return rate | `returns` -> `order_items` |
| Trạng thái vận chuyển | `shipments` -> `orders` |
| Nhân viên theo cửa hàng | `stores` -> `employees` |
| Khuyến mãi và discount | `promotions` -> `orders` -> `order_items` |

## Date Table

Bảng `Date` được tạo bằng DAX dựa trên khoảng ngày của `orders[order_date]` và đã được mark as date table bằng cột `Date[Date]`.

| Cột | Cách dùng |
|---|---|
| `Date[Date]` | Dùng cho DAX time intelligence |
| `Date[Year]` | Slicer theo năm, chart theo năm |
| `Date[Quarter]` | Nhóm theo quý |
| `Date[Month Number]` | Cột sort cho tháng |
| `Date[Month]` | Hiển thị tên tháng |
| `Date[Year Month]` | Axis cho chart xu hướng theo tháng |
| `Date[Weekday Number]` | Cột sort cho thứ |
| `Date[Weekday]` | Phân tích theo thứ trong tuần |

Khi làm chart theo thời gian, ưu tiên dùng field trong bảng `Date`, không dùng trực tiếp `orders[order_date]`.

## Cột Nên Dùng Khi Làm Visual

| Bảng | Cột nên dùng | Mục đích |
|---|---|---|
| `Date` | `Year` | Slicer năm |
| `Date` | `Year Month` | Axis xu hướng theo tháng |
| `customers` | `Segment` | Slicer hoặc breakdown theo phân khúc |
| `customers` | `city` | Phân tích theo thành phố khách hàng |
| `categories` | `category_name` | Phân tích theo danh mục |
| `stores` | `city` | Slicer hoặc breakdown theo thành phố cửa hàng |
| `suppliers` | `country` | Phân tích theo quốc gia nhà cung cấp |
| `shipments` | `status` | Breakdown trạng thái vận chuyển |
| `promotions` | `discount` | Phân tích discount |

## Cột Kỹ Thuật Đã Ẩn

Các cột ID đã được ẩn khỏi report view. Chúng chỉ dùng cho relationship, không dùng để kéo vào chart hoặc slicer.

| Nhóm | Cột đã ẩn |
|---|---|
| Đơn hàng | `orders[order_id]`, `orders[customer_id]`, `orders[store_id]`, `orders[promotion_id]` |
| Chi tiết đơn hàng | `order_items[order_item_id]`, `order_items[order_id]`, `order_items[product_id]` |
| Khách hàng/cửa hàng | `customers[customer_id]`, `stores[store_id]` |
| Sản phẩm | `products[product_id]`, `products[category_id]`, `products[supplier_id]` |
| Thanh toán/hoàn trả/vận chuyển | `payments[payment_id]`, `payments[order_id]`, `returns[return_id]`, `returns[order_item_id]`, `shipments[shipment_id]`, `shipments[order_id]` |
| Dimension khác | `categories[category_id]`, `suppliers[supplier_id]`, `promotions[promotion_id]`, `employees[employee_id]`, `employees[store_id]` |

## Format Dữ Liệu

| Loại dữ liệu | Ví dụ | Format |
|---|---|---|
| Tiền tệ | Revenue, payment, refund, salary, price | `$#,0.00;($#,0.00);$0.00` |
| Số nguyên | Orders, quantity, customers, products | `#,0` |
| Số thập phân | Items per order | `#,0.00` |
| Tỉ lệ phần trăm | Return rate, shipment rate, discount, growth rate | `0.00%` |

## Gợi Ý Slicer

| Slicer | Field |
|---|---|
| Năm | `Date[Year]` |
| Tháng | `Date[Year Month]` |
| Segment khách hàng | `customers[Segment]` |
| Thành phố cửa hàng | `stores[city]` |
| Danh mục sản phẩm | `categories[category_name]` |
| Quốc gia nhà cung cấp | `suppliers[country]` |
| Trạng thái vận chuyển | `shipments[status]` |

## Gợi Ý Theo Page

| Page | Trọng tâm dữ liệu | Field nên dùng |
|---|---|---|
| `Overview` | Tổng quan doanh thu, đơn hàng, khách hàng, vận hành | `Date[Year Month]`, `customers[Segment]`, `categories[category_name]`, `stores[city]`, `shipments[status]` |
| `Revenue` | Doanh thu, thanh toán, refund, tăng trưởng | `Date[Year Month]`, `customers[Segment]`, `promotions[discount]` |
| `Customers` | Phân khúc và địa lý khách hàng | `customers[Segment]`, `customers[city]`, `Date[Year Month]` |
| `Products` | Danh mục, số lượng, return, nhà cung cấp | `categories[category_name]`, `suppliers[country]`, `Date[Year Month]` |
| `Operations` | Cửa hàng, nhân viên, vận chuyển | `stores[city]`, `shipments[status]`, `Date[Year Month]` |

## Quy Ước Khi Dùng Model

- Dùng measures trong bảng `_Measures` cho KPI và chart values.
- Dùng cột business visible cho Axis, Legend và Slicer.
- Không unhide hoặc dùng cột ID kỹ thuật trong report.
- Không tạo measure trùng lặp nếu chưa thống nhất với leader.
- Dùng `Date` table cho các chart thời gian và time intelligence.
- Nếu `customers[Segment] = Unknown` xuất hiện trong customer visual nhưng không có revenue, xem đây là đặc điểm dữ liệu cần ghi chú, không phải lỗi dashboard.

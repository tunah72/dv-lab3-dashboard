# Convention Và Lưu Ý Thiết Kế Dashboard Power BI

Tài liệu này áp dụng cho tất cả thành viên khi thiết kế các trang phân tích riêng. Mục tiêu là giúp Đức Phúc tổng hợp dashboard final nhanh, giảm lệch layout, font, filter, navigation và cách đặt tên visual.

## 1. File Làm Việc

Mỗi thành viên tạo file backup riêng từ file base, không chỉnh trực tiếp file final.

| Thành viên | Trang | File làm việc đề xuất |
|---|---|---|
| Tuấn Anh | Sales Trend | `Dashboard_TuanAnh_SalesTrend.pbix` |
| Xuân Trí | Customers | `Dashboard_XuanTri_Customers.pbix` |
| Trung Kiên | Products | `Dashboard_TrungKien_Products.pbix` |
| Đức Phúc | Overview, Operations | `Dashboard_DucPhuc_Overview_Operations.pbix` |

Không tự ý đổi tên bảng, relationship, field hoặc measure dùng chung. Nếu cần tạo measure mới, ghi rõ tên measure, công thức DAX và lý do để nhóm review trước khi đưa vào file final.

## 2. Tài Liệu Cần Đọc

Trước khi thiết kế visual, mỗi thành viên cần đọc:

- `docs/powerbi_data_model_guide.md`: nắm cấu trúc bảng, relationship, grain của từng bảng, field nên dùng cho axis/filter.
- `docs/powerbi_dax_measures_dictionary.md`: nắm các measures có sẵn trong bảng `_Measures`.
- File hướng dẫn của trang mình:
  - `docs/SalesTrend.md`
  - `docs/Customers.md`
  - `docs/Products.md`
  - `docs/Operations.md`
  - `docs/Overview.md`

## 3. Page Convention

Thống nhất tên kỹ thuật, tên hiển thị và thứ tự trang:

| Thứ tự | Tên page kỹ thuật | Tên hiển thị trên dashboard |
|---:|---|---|
| 1 | `Overview` | Tổng quan |
| 2 | `Sales Trend` | Xu hướng doanh thu |
| 3 | `Customers` | Khách hàng |
| 4 | `Products` | Sản phẩm |
| 5 | `Operations` | Vận hành |

Khi tổng hợp, Đức Phúc sẽ chuẩn hóa lại page order theo thứ tự trên. Thành viên không tự đặt tên page kỹ thuật khác convention này.

Lưu ý: nếu file Power BI hiện tại đang dùng tên page kỹ thuật `SalesTrend` không có khoảng trắng, cần kiểm tra đúng tên page thực tế khi gán Page navigation. Trong bản final, tên kỹ thuật nên thống nhất là `Sales Trend`, còn label hiển thị trên sidebar/page title là `Xu hướng doanh thu`.

## 3.1. Convention Ngôn Ngữ

Dashboard final sử dụng tiếng Việt có dấu cho toàn bộ nội dung người xem nhìn thấy.

| Loại nội dung | Ngôn ngữ cần dùng |
|---|---|
| Page title hiển thị | Tiếng Việt có dấu |
| Navigation button hiển thị | Tiếng Việt có dấu |
| Chart title | Tiếng Việt có dấu, dạng câu hỏi |
| KPI label | Tiếng Việt có dấu |
| Slicer title | Tiếng Việt có dấu |
| Tooltip title hoặc text tự viết | Tiếng Việt có dấu |
| Insight trong báo cáo/video | Tiếng Việt có dấu |
| Tên measure DAX | Giữ tiếng Anh |
| Tên table/field trong model | Giữ tiếng Anh |
| Tên visual nội bộ | Giữ tiếng Anh theo naming convention |
| Tên bookmark/button nội bộ | Giữ tiếng Anh theo naming convention |

Ví dụ:

| Kỹ thuật | Hiển thị cho người xem |
|---|---|
| `Total Revenue` | Tổng doanh thu |
| `Net Revenue` | Doanh thu ròng |
| `Total Orders` | Tổng đơn hàng |
| `Return Rate` | Tỷ lệ hoàn trả |
| `Date[Year]` | Năm |
| `Date[Year Month]` | Tháng |
| `customers[Segment]` | Phân khúc khách hàng |
| `categories[category_name]` | Danh mục sản phẩm |
| `stores[city]` | Thành phố cửa hàng |
| `shipments[status]` | Trạng thái vận chuyển |

Không dùng lẫn lộn các label tiếng Anh như `Total Revenue`, `Customers`, `Products`, `Year`, `Month` trên dashboard final, trừ khi đó là tên kỹ thuật không hiển thị cho người xem.

## 4. Layout Chung

Mỗi trang nên giữ cấu trúc:

| Khu vực | Nội dung |
|---|---|
| Sidebar | Navigation buttons đến 5 trang |
| Header | Page title và mô tả ngắn nếu cần |
| Filter area | Slicers của trang |
| KPI row | 4 KPI cards |
| Main visual | Biểu đồ quan trọng nhất của trang |
| Supporting visuals | 3 biểu đồ phụ hoặc 2 biểu đồ phụ + 1 matrix/table |
| Reset area | Button reset filter |

Canvas giữ chuẩn 16:9. Không đổi page size.

## 5. Quy Ước Khi Chỉnh PPTX Background

Các thành viên có thể chỉnh `design/powerbi_background_template.pptx` để layout phù hợp với trang phân tích, nhưng phải tuân thủ:

- Chỉ chỉnh vùng nội dung của trang, không phá bỏ sidebar, filter area và reset area.
- Nếu cần đổi kích thước chart container, vẫn giữ tối thiểu 4 vùng KPI và 4 vùng visual chính.
- Không đổi phong cách màu nền tổng thể nếu chưa thống nhất với nhóm.
- Sau khi chỉnh PPTX, export slide thành PNG đúng tỷ lệ 16:9 rồi đặt làm page background trong Power BI.
- Ghi chú cho Đức Phúc biết nếu có thay đổi layout trong PPTX.

## 6. Font Và Cỡ Chữ

### Font chữ

| Thành phần | Font |
|---|---|
| Page title | Segoe UI Semibold |
| Chart title | Segoe UI Semibold |
| KPI value | Segoe UI Semibold |
| KPI label | Segoe UI |
| Axis label | Segoe UI |
| Legend | Segoe UI |
| Data label | Segoe UI |
| Slicer title/value | Segoe UI |
| Navigation button | Segoe UI Semibold |
| Reset button | Segoe UI Semibold |

Nếu Power BI không có đúng biến thể `Segoe UI Semibold`, dùng `Segoe UI` và bật Bold cho title/button.

### Cỡ chữ

| Thành phần | Cỡ chữ đề xuất | Ghi chú |
|---|---:|---|
| Page title | 22-26 pt | Tiêu đề lớn của trang |
| Short page subtitle | 10-12 pt | Nếu có mô tả ngắn dưới title |
| KPI value | 22-28 pt | Số lớn, ưu tiên dễ đọc nhanh |
| KPI label | 9-11 pt | Ngắn gọn, không viết quá dài |
| Chart title dạng câu hỏi | 11-13 pt | Mỗi chart phải có title dạng câu hỏi |
| Axis label | 8-10 pt | Giữ nhỏ để chart không bị rối |
| Axis title | 9-10 pt | Chỉ bật nếu cần làm rõ đơn vị |
| Legend | 8-10 pt | Đặt top hoặc right tùy chart |
| Data label | 8-10 pt | Chỉ bật khi không làm rối chart |
| Tooltip text | 9-10 pt | Giữ mặc định nếu không cần chỉnh |
| Slicer title | 9-10 pt | Viết ngắn: Năm, Tháng, Phân khúc |
| Slicer value | 8-10 pt | Không để quá lớn làm vỡ layout |
| Navigation button | 10-11 pt | Đồng bộ tất cả page |
| Reset button | 10-11 pt | Giống navigation button |
| Table/Matrix header | 9-10 pt | Có thể bold |
| Table/Matrix values | 8-9 pt | Ưu tiên hiển thị đủ hàng/cột |

## 7. Chart Title Dạng Câu Hỏi

Mỗi biểu đồ phải có title dạng câu hỏi, ví dụ:

- Doanh thu thay đổi như thế nào theo thời gian?
- Phân khúc khách hàng nào đóng góp doanh thu lớn nhất?
- Danh mục sản phẩm nào có tỷ lệ hoàn trả cao?
- Tình trạng vận chuyển đang phân bổ như thế nào?

Không dùng title chung chung như `Revenue Chart`, `Bar Chart`, `Customers`, `Products`.

## 8. Màu Sắc Và Style

- Giữ nền, sidebar và phong cách tổng thể theo background đã thiết kế.
- Dùng màu nhấn sáng cho trang đang active trong sidebar.
- Dùng màu cảnh báo như cam/đỏ cho return rate, late shipment, refund hoặc negative trend.
- Không dùng quá nhiều màu trong một trang.
- Data labels chỉ bật khi cần đọc số nhanh và không làm rối chart.
- Chart title không viết ALL CAPS, trừ KPI label ngắn.

## 9. Filter / Slicer Convention

Filter chung nên dùng khi phù hợp:

| Filter | Field |
|---|---|
| Năm | `Date[Year]` |
| Tháng | `Date[Year Month]` |
| Phân khúc khách hàng | `customers[Segment]` |

Filter riêng theo trang:

| Trang | Filter thêm |
|---|---|
| Sales Trend | `promotions[discount]` nếu có insight rõ |
| Customers | `customers[city]` |
| Products | `categories[category_name]`, `suppliers[country]` |
| Operations | `stores[city]`, `shipments[status]` |
| Overview | `categories[category_name]`, `stores[city]`, `shipments[status]` nếu đủ chỗ |

Không dùng field ID kỹ thuật như `order_id`, `customer_id`, `product_id`, `store_id`, `promotion_id` làm slicer hoặc axis hiển thị.

## 10. Navigation Convention

Sidebar navigation phải có đủ 5 button:

| Label hiển thị | Action |
|---|---|
| Tổng quan | Page navigation -> `Overview` |
| Xu hướng doanh thu | Page navigation -> `Sales Trend` |
| Khách hàng | Page navigation -> `Customers` |
| Sản phẩm | Page navigation -> `Products` |
| Vận hành | Page navigation -> `Operations` |

Trang hiện tại cần có button active nổi bật hơn các button còn lại. Không đặt navigation đè lên chart, KPI hoặc slicer.

## 11. Reset Bookmark Convention

Mỗi trang cần có reset bookmark:

| Trang | Bookmark |
|---|---|
| Overview | `BM_Reset_Overview` |
| Sales Trend | `BM_Reset_SalesTrend` |
| Customers | `BM_Reset_Customers` |
| Products | `BM_Reset_Products` |
| Operations | `BM_Reset_Operations` |

Cách làm:

1. Đặt slicer/filter về trạng thái mặc định.
2. Mở Bookmarks pane.
3. Add bookmark.
4. Đổi tên bookmark theo convention.
5. Gán button `Reset` vào bookmark đó.

## 12. Naming Convention

| Loại | Format | Ví dụ |
|---|---|---|
| KPI | `KPI_PageName_MetricName` | `KPI_Customers_TotalCustomers` |
| Chart | `CH_PageName_Purpose` | `CH_Products_RevenueByCategory` |
| Slicer | `SL_PageName_FieldName` | `SL_Operations_ShipmentStatus` |
| Button | `BTN_PageName_Target` | `BTN_Customers_Overview` |
| Bookmark | `BM_Reset_PageName` | `BM_Reset_Products` |

Tên `PageName` nên dùng: `Overview`, `SalesTrend`, `Customers`, `Products`, `Operations`.

## 13. Lưu Ý Về Data Model

- Dùng measures trong bảng `_Measures` cho KPI và chart values.
- Chart theo thời gian dùng field trong bảng `Date`, không dùng trực tiếp `orders[order_date]`.
- Không dùng cột ID kỹ thuật trong report.
- Không kéo trực tiếp cột numeric nếu đã có measure tương ứng.
- Nếu visual bị sai số, kiểm tra grain của bảng trước khi kết luận dữ liệu sai.
- Nếu `customers[Segment] = Unknown` xuất hiện, xem đây là đặc điểm dữ liệu cần ghi chú, không phải lỗi dashboard.

## 14. Checklist Bàn Giao

Mỗi thành viên gửi cho Đức Phúc:

- [ ] File `.pbix` backup riêng.
- [ ] Screenshot trang hoàn chỉnh.
- [ ] Danh sách KPI cards.
- [ ] Danh sách charts và title dạng câu hỏi.
- [ ] Danh sách slicers/filters.
- [ ] Tên reset bookmark.
- [ ] 3-5 insight ngắn.
- [ ] Ghi chú nếu có thay đổi layout trong PPTX.
- [ ] Ghi chú nếu có tạo measure mới.

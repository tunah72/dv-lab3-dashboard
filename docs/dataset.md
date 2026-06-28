# Giới Thiệu Dataset: Retail Data Warehouse – Multi-Table Analytics Dataset

**Nguồn:** [Kaggle - Retail Data Warehouse – 12 Table 1M+ Rows Dataset](https://www.kaggle.com/datasets/datarspectrum/retail-data-warehouse-12-table-1m-rows-dataset)  
**Tác giả (Creator):** datarspectrum  

## 1. Tổng Quan
Dataset **"Retail Data Warehouse"** là một tập dữ liệu tổng hợp mô phỏng một môi trường kinh doanh bán lẻ quy mô lớn và chân thực. Với hơn 1 triệu dòng dữ liệu (1M+ rows), tập dữ liệu này được thiết kế đặc biệt để phục vụ cho các bài toán phân tích dữ liệu nâng cao, thực hành truy vấn SQL đa bảng, xây dựng Kho dữ liệu (Data Warehouse) và thiết kế Dashboard (như Power BI, Tableau).

Tập dữ liệu phản ánh toàn diện các hoạt động của một doanh nghiệp bán lẻ đa chi nhánh, từ giao dịch khách hàng, doanh số sản phẩm, dòng tiền thanh toán cho đến quá trình vận hành kho vận và logistics.

## 2. Cấu Trúc Dữ Liệu
Dataset tuân thủ chặt chẽ kiến trúc cơ sở dữ liệu quan hệ (relational database), bao gồm **12 bảng (tables)** độc lập nhưng có tính liên kết cao:

1. **customers** (Khách hàng): Thông tin hồ sơ, nhân khẩu học của khách hàng.
2. **stores** (Cửa hàng): Danh sách và thông tin các chi nhánh/cửa hàng.
3. **employees** (Nhân viên): Thông tin nhân sự làm việc tại hệ thống cửa hàng.
4. **categories** (Danh mục): Phân loại các nhóm sản phẩm kinh doanh.
5. **suppliers** (Nhà cung cấp): Đối tác cung ứng hàng hóa cho hệ thống.
6. **products** (Sản phẩm): Danh mục chi tiết các mặt hàng.
7. **promotions** (Khuyến mãi): Các chiến dịch giảm giá, mã ưu đãi.
8. **orders** (Đơn hàng): Thông tin tổng quan về các giao dịch mua hàng (thời gian, khách hàng, cửa hàng...).
9. **order_items** (Chi tiết đơn hàng): Chi tiết từng sản phẩm bên trong mỗi đơn hàng (bao gồm số lượng, đơn giá).
10. **payments** (Thanh toán): Lịch sử và trạng thái các giao dịch thanh toán của đơn hàng.
11. **shipments** (Vận chuyển): Trạng thái giao hàng, theo dõi luồng logistics.
12. **returns** (Hoàn trả): Ghi nhận các trường hợp trả hàng, hoàn tiền.

## 3. Đặc Điểm Nổi Bật
* **Tính liên kết (Relational Data):** Tất cả các bảng được kết nối với nhau thông qua hệ thống Khóa chính (Primary Keys) và Khóa ngoại (Foreign Keys). Điều này cho phép người dùng xây dựng Data Model hoàn chỉnh và thực hiện các câu lệnh `JOIN` phức tạp.
* **Mô phỏng quy trình thực tế:** Dataset bao phủ toàn bộ vòng đời của ngành bán lẻ, từ chuỗi cung ứng (suppliers, products) $\rightarrow$ bán hàng (orders, promotions) $\rightarrow$ hoàn tất đơn hàng (shipments, payments) và hậu mãi (returns).

## 4. Ứng Dụng Khuyến Nghị
Tập dữ liệu này là tài nguyên lý tưởng cho các dự án:
* **Thực hành SQL & Data Engineering:** Tạo lập quy trình ETL, tối ưu hóa truy vấn trên tập dữ liệu lớn.
* **Xây dựng Data Model:** Thiết kế mô hình dữ liệu dạng Star Schema hoặc Snowflake Schema.
* **Data Visualization (Trực quan hóa dữ liệu):** Phân tích xu hướng doanh thu, hiệu suất sản phẩm, đánh giá rủi ro vận chuyển và tỷ lệ hoàn hàng.
* **Machine Learning:** Hỗ trợ thực hiện các mô hình phân khúc khách hàng (RFM Clustering) hoặc dự báo doanh số (Sales Forecasting).
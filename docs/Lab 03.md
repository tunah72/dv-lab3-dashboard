# Lab 03: Trực quan hóa dữ liệu bằng Power BI

## 1 Quy định chung

- Bài làm được thực hiện theo nhóm tối thiểu 3 người và tối đa 5 người.
- Thành viên không tham gia sẽ không có điểm bài tập này.
- Bài làm phải tuân thủ theo yêu cầu đồ án.
- Các nguồn tài liệu tham khảo (nếu có) cần ghi đầy đủ trong báo cáo ở mục *Tài liệu tham khảo*.
- Các công cụ hỗ trợ trong việc code, viết báo cáo như ChatGPT, Github Copilot,... chỉ dùng như một công cụ tham khảo; nội dung phải được kiểm tra và chỉnh sửa phù hợp với bài toán đặt ra. Nếu phát hiện sử dụng công cụ AI để sinh nội dung quá nhiều, hoặc nội dung không phù hợp/sai lệch thì sẽ trừ tối đa **50%** số điểm (tùy mức độ).
- **Bài giống nhau sẽ nhận 0 điểm môn học.**
- **Các bài làm phúc khảo không đúng** (yêu cầu phúc khảo nhưng kết quả chấm lại không thay đổi hoặc không hợp lệ) sẽ bị trừ **50%** số điểm của bài tập này.

## 2 Giới thiệu đồ án

### 2.1 Giới thiệu đồ án

*Power BI* là một công cụ trực quan hóa dữ liệu mạnh mẽ do Microsoft phát triển, cho phép người dùng kết nối, xử lý và trực quan hóa dữ liệu từ nhiều nguồn khác nhau. Công cụ này hỗ trợ xây dựng các biểu đồ tương tác, *dashboard* và báo cáo trực quan, qua đó giúp người dùng khám phá dữ liệu và đưa ra các quyết định dựa trên dữ liệu.

Trong đồ án này, các nhóm sẽ sử dụng Power BI để phân tích và trực quan hóa dữ liệu từ một bộ dữ liệu quan hệ (*relational dataset*). Thông qua việc xây dựng mô hình dữ liệu, tạo các biểu đồ và *dashboard*, nhóm cần khám phá các xu hướng, mối quan hệ giữa các biến dữ liệu và rút ra các *insight* có ý nghĩa.

### 2.2 Nhiệm vụ đồ án

Trong đồ án này, các bạn sẽ thực hiện các nhiệm vụ sau:

**1. Tìm hiểu công cụ Power BI**
- Giới thiệu tổng quan về Power BI.
- Tìm hiểu các chức năng chính của Power BI như: *Import* dữ liệu, *Data transformation* (Power Query), *Data modeling*, tạo biểu đồ và *dashboard*, *filter* và *slicer*.
- Minh họa các chức năng này bằng các ví dụ sử dụng *dataset* mẫu (không liên quan đến *dataset* chính của bài).

**2. Lựa chọn dataset và xây dựng mô hình dữ liệu**
- *Dataset* sử dụng trong đồ án bắt buộc phải là **relational dataset** (dữ liệu quan hệ), bao gồm nhiều bảng dữ liệu có liên kết với nhau.
- Các bảng dữ liệu cần có mối quan hệ thông qua các khóa dữ liệu (*key*) như: *one-to-one*, *one-to-many*, *many-to-one*.
- Nhóm cần xây dựng *data model* trong Power BI bằng cách thiết lập các *relationship* giữa các bảng dữ liệu.
- Nhóm cần mô tả rõ: các bảng dữ liệu được sử dụng, ý nghĩa của từng bảng, các khóa liên kết giữa các bảng.
- *Dataset* cần có kích thước đủ lớn để có thể thực hiện phân tích và trực quan hóa.
- Các bộ dữ liệu có thể lấy từ các nguồn dữ liệu mở như: Kaggle, World Bank, Data.gov, hoặc các *open dataset* khác.

**3. Xác định mục tiêu phân tích**
- Nhóm cần xác định rõ các câu hỏi hoặc mục tiêu phân tích dựa trên *dataset* đã chọn.
- Các mục tiêu phân tích cần liên quan đến một chủ đề chung.
- Mỗi nhóm cần xác định số mục tiêu phân tích bằng với số lượng thành viên trong nhóm.

**4. Phân tích dữ liệu và trực quan hóa**
- Sử dụng Power BI để xây dựng các biểu đồ nhằm trả lời các câu hỏi phân tích đã đề ra.
- Nhóm cần sử dụng nhiều loại biểu đồ khác nhau như: *bar chart*, *line chart*, *pie chart*, *scatter plot*, *map*, *table* hoặc *matrix*,...
- Các biểu đồ cần phù hợp với tính chất của dữ liệu.
- Nhóm cần sử dụng màu sắc hợp lý để thể hiện dữ liệu và giải thích ý nghĩa của việc lựa chọn màu sắc.
- Sau khi trực quan hóa, nhóm cần phân tích và rút ra các nhận xét từ biểu đồ.

**5. Xây dựng dashboard**
- Nhóm cần thiết kế một hoặc nhiều *dashboard* tổng hợp kết quả phân tích.
- *Dashboard* cần có bố cục hợp lý, dễ theo dõi, thể hiện rõ các *insight* chính, có sử dụng *filter* hoặc *slicer* để tương tác dữ liệu.
- *Dashboard* cần được thiết kế như một *storyboard*, thể hiện rõ luồng phân tích dữ liệu.

**6. Nhận xét và kết luận**
- Tổng hợp các kết quả phân tích từ các biểu đồ và *dashboard*.
- Đưa ra các nhận xét, xu hướng hoặc *insight* quan trọng từ dữ liệu.

## 3 Yêu cầu đồ án

- Nhóm **chỉ sử dụng môi trường Power BI** để thực hiện trực quan hóa và xây dựng *dashboard*.
- *Dataset* sử dụng trong đồ án phải là **relational dataset** gồm nhiều bảng dữ liệu có liên kết với nhau.
- **Không được sử dụng** các *sample dataset* có sẵn trong Power BI.
- *Dataset* cần có:
  - Ít nhất 2–3 bảng dữ liệu.
  - Các *relationship* rõ ràng giữa các bảng.
  - Số lượng dữ liệu đủ lớn để phân tích.
- Khi sử dụng *dataset*, nhóm cần: giới thiệu nguồn dữ liệu, mô tả các bảng dữ liệu, mô tả các *relationship* giữa các bảng.
- Có thể sử dụng các thuật toán máy học để hỗ trợ phân tích dữ liệu.
- Viết báo cáo ngắn gọn và đầy đủ toàn bộ quá trình thực hiện, kết quả và nhận xét. Báo cáo **tối đa 24 trang** (không bao gồm trang bìa, mục lục và tài liệu tham khảo).
- Nội dung báo cáo bao gồm:
  1. **Thông tin nhóm xx** (với xx là tên nhóm): bảng thông tin gồm các cột STT, MSSV, Họ và tên, Tỷ lệ đóng góp của từng thành viên.
  2. **Tìm hiểu công cụ Power BI**:
     - Giới thiệu tổng quan về Power BI.
     - Trình bày các thành phần chính của Power BI như Power BI Desktop, Power BI Service, Power BI Report.
     - Trình bày các chức năng cơ bản của Power BI: *Import* dữ liệu, *Data transformation* (Power Query), *Data modeling*, *Visualization*, *Dashboard*.
     - Minh họa các chức năng trên bằng *dataset* mẫu hoặc *dataset* đơn giản (không sử dụng *dataset* chính của bài toán).
  3. **Giới thiệu bài toán phân tích**:
     - Trình bày tổng quan về bài toán phân tích dữ liệu mà nhóm thực hiện.
     - Nêu rõ mục tiêu phân tích chung của nhóm.
     - Trình bày các mục tiêu phân tích cụ thể của từng thành viên trong nhóm.
  4. **Dataset và quy trình xử lý dữ liệu**:
     - Giới thiệu nguồn dữ liệu và lý do lựa chọn *dataset*.
     - Mô tả các bảng dữ liệu và các trường dữ liệu quan trọng.
     - Mô tả các *relationship* giữa các bảng (*data model* trong Power BI).
     - Trình bày quy trình thu thập, xây dựng và tiền xử lý dữ liệu (*data cleaning*, *data transformation*,...).
  5. **Phân tích dữ liệu và trực quan hóa**:
     - Báo cáo chi tiết quy trình thực hiện phân tích của từng thành viên.
     - Nội dung phân tích cần bao gồm: mục tiêu phân tích, biểu đồ và phương pháp trực quan hóa được sử dụng, kết quả phân tích, nhận xét và rút ra kết luận.
     - Các biểu đồ và *dashboard* cần được minh họa bằng hình ảnh từ Power BI.
     - Cuối phần này cần tổng hợp và trình bày các *insight* quan trọng rút ra từ dữ liệu, đồng thời kết luận cho bài toán phân tích chung của nhóm.
  6. **Tài liệu tham khảo**: liệt kê các nguồn dữ liệu, tài liệu và website được sử dụng trong quá trình thực hiện đồ án.

## 4 Quy định nộp bài

- Nhóm cử đại diện 1 người nộp bài.
- Bài nộp là một file nén đặt tên `[MSSV_1, MSSV_2, MSSV_3].zip` bao gồm:
  1. Thư mục chứa dữ liệu hoặc link tới dữ liệu.
  2. File Power BI:
     - `[MSSV_1, MSSV_2, MSSV_3]_samples.pbix`
     - `[MSSV_1, MSSV_2, MSSV_3].pbix`
  3. File báo cáo: `[MSSV_1, MSSV_2, MSSV_3].pdf`
  4. Video trình bày phân tích.
- Trong trường hợp dữ liệu quá lớn, nhóm có thể upload dữ liệu lên Google Drive hoặc các dịch vụ lưu trữ khác, sau đó nộp link trong file nén.
- Link dữ liệu cần được giữ ở chế độ **public** ít nhất 2 năm.

## 5 Tiêu chí chấm điểm

| STT | Tiêu chí | Điểm |
|:---:|---|:---:|
| 1 | Giới thiệu Power BI và các chức năng cơ bản | 1.0 |
| 2 | Lựa chọn dataset và xây dựng relational data model | 2.0 |
| 3 | Thiết kế dashboard trực quan và hợp lý | 3.0 |
| 4 | Phân tích và rút ra insight từ dữ liệu | 3.0 |
| 5 | Chất lượng báo cáo và trình bày | 1.0 |
| **Tổng** | **Tổng điểm** | **10.0** |

## 6 Liên hệ

Mọi thắc mắc trong quá trình thực hiện vui lòng gửi mail về:
- **huyban.han@gmail.com**
- **vntan.work@gmail.com**

---
*Good luck*

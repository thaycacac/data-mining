Dưới đây là tóm tắt các điểm cốt lõi của bài học củng cố về **Thuật toán FP-Growth & Quy trình Dựng Cây FP-Tree (FP-Growth & FP-Tree Construction)**:

---

### 1. Tổng quan & Ưu điểm Khả năng Mở rộng (Scalability)

* **Giải quyết hạn chế của Apriori:** FP-Growth loại bỏ hoàn toàn việc sinh các tập ứng viên dư thừa, giúp tối ưu hóa chi phí tính toán và khả năng mở rộng trên tập dữ liệu lớn.
* **Đảm bảo tính phổ biến:** Chỉ các tập mục chắc chắn đạt ngưỡng hỗ trợ tối thiểu mới được khai phá từ cấu trúc cây, tránh việc đếm và kiểm tra không cần thiết.

---

### 2. Các Bước Dựng Cây tiền tố FP-Tree

1. **Quét dữ liệu & Lọc mục đơn lẻ:** Quét tập dữ liệu để đếm tần suất các mục đơn lẻ và lọc bỏ những mục có độ hỗ trợ dưới ngưỡng `min_sup`.
2. **Sắp xếp theo Tần suất (Frequency Order):** Sắp xếp danh sách các mục phổ biến đơn lẻ theo **tần suất giảm dần** (không sắp xếp theo thứ tự bảng chữ cái).
3. **Làm sạch & Sắp xếp lại Giao dịch:** Với từng giao dịch, loại bỏ các mục không đạt ngưỡng và reorder các mục còn lại chính xác theo thứ tự tần suất giảm dần ở trên.
4. **Chèn giao dịch vào Cây (Tree Insertion):** Chèn từng giao dịch đã chuẩn hóa thành một đường dẫn (path) trên cây FP-Tree. Các giao dịch có chung tiền tố sẽ chia sẻ chung nhánh và tự động tăng hằng số đếm (`count`).

---

### 3. Móc nối & Kiểm tra Tính Đúng đắn của Cây

* **Liên kết danh sách (Node-Links):** Tất cả các nút (nodes) trên cây đại diện cho cùng một mục được móc nối với nhau thành một danh sách liên kết (linked list), bắt nguồn từ Bảng tiêu đề (Header Table).
* **Kiểm tra nhất quán (Validation):** Thuật toán xác minh số đếm tại mỗi nút để đảm bảo tính toàn vẹn và chính xác của cấu trúc cây trước khi bước vào giai đoạn trích xuất mẫu (Pattern Extraction).

---

> **Bài học cốt lõi:** Nhờ quy trình reorder theo tần suất và móc nối nút thông minh, FP-Tree nén gọn toàn bộ dữ liệu giao dịch thành một cấu trúc cây tiền tố duy nhất, làm nền tảng cho việc trích xuất mẫu phổ biến tốc độ cao.
Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Thuật toán FP-Growth (Frequent Pattern Growth) & Cấu trúc Cây FP-Tree**:

---

### 1. Động lực & Tư tưởng Cốt lõi của FP-Growth

* **Điểm yếu của Apriori:** Sinh ra quá nhiều tập ứng viên (candidate itemsets) và phải quét cơ sở dữ liệu nhiều lần để đếm độ hỗ trợ.
* **Tư tưởng FP-Growth:** Loại bỏ hoàn toàn bước sinh ứng viên bằng cách nén cơ sở dữ liệu vào một cấu trúc cây tiền tố (**FP-Tree - Frequent Pattern Tree**), sau đó tiến hành khai phá triệt để trên cây này thông qua các tập con điều kiện (conditional subsets).

---

### 2. Quy trình Xây dựng Cây FP-Tree

1. **Lần quét dữ liệu thứ nhất (Quét 1):**
* Đếm tần suất các mục đơn lẻ và lọc bỏ các mục có độ hỗ trợ dưới ngưỡng `min_sup`.
* Sắp xếp các mục đơn lẻ còn lại theo **thứ tự giảm dần của tần suất**.


2. **Lần quét dữ liệu thứ hai (Quét 2):**
* Với mỗi giao dịch, loại bỏ các mục không phổ biến và sắp xếp lại các mục còn lại đúng theo thứ tự tần suất giảm dần đã xác định ở Bước 1.
* Chèn từng giao dịch đã sắp xếp vào **cây tiền tố (FP-Tree)**: các giao dịch chia sẻ chung chuỗi tiền tố sẽ dùng chung nhánh trên cây và tăng hằng số đếm (`count`).
* Tạo **Bảng tiêu đề (Header Table)** chứa danh sách các mục phổ biến và liên kết chuỗi (node-links) trỏ tới tất cả các nút tương ứng trên cây.



---

### 3. Khai phá Tập mục Phổ biến từ Cây FP-Tree

Với mỗi mục phổ biến trong Bảng tiêu đề (bắt đầu từ mục có tần suất thấp nhất):

* **Tạo Cơ sở Mẫu Điều kiện (Conditional Pattern Base):** Duyệt ngược từ các nút của mục đó lên gốc cây để thu thập tất cả các đường dẫn tiền tố (prefix paths) kèm theo số lần xuất hiện.
* **Xây dựng Cây FP-Tree Điều kiện (Conditional FP-Tree):** Tạo một cây FP-Tree nhỏ hơn từ cơ sở mẫu điều kiện vừa thu thập được để lọc ra các mục đạt ngưỡng hỗ trợ trong bối cảnh điều kiện đó.
* **Sinh Tập mục Phổ biến Đệ quy:** Kết hợp đệ quy mục đang xét với các mục trong cây FP-Tree điều kiện để thu được tất cả các tập mục phổ biến chứa mục đó.

---

> **Kết luận:** Nhờ phương pháp chia để trị (Divide-and-Conquer) và nén dữ liệu cấu trúc cây, FP-Growth chỉ cần quét cơ sở dữ liệu đúng **2 lần** và không sinh bất kỳ tập ứng viên rác nào, mang lại hiệu năng vượt trội hơn nhiều so với Apriori trên tập dữ liệu lớn.
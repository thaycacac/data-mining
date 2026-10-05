Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Các Kỹ thuật Nâng cao Hiệu năng Khai phá Mẫu Phổ biến (Improving Frequent Pattern Mining Efficiency)**:

---

### 1. Tách biệt Thách thức của Thuật toán Apriori

Mặc dù Apriori giúp giảm bớt không gian tìm kiếm so với duyệt cạn, thuật toán vẫn gặp phải hai điểm nghẽn hiệu năng chính trên tập dữ liệu lớn:

* **Chi phí I/O lớn:** Bắt buộc phải **quét toàn bộ cơ sở dữ liệu nhiều lần** (tương ứng với độ dài $k$ của tập mục).
* **Bùng nổ tập ứng viên (Candidate Explosion):** Số lượng tập mục ứng viên sinh ra ở các bước giữa tăng nhanh, làm gia tăng chi phí đếm độ hỗ trợ (support counting).

---

### 2. Các Chiến lược Cải thiện Hiệu năng

* **Phân hoạch Dữ liệu (Partitioning):**
* Chia cơ sở dữ liệu lớn thành các phần nhỏ (partitions) vừa với bộ nhớ RAM.
* Một tập mục muốn phổ biến trên toàn bộ dữ liệu thì **bắt buộc phải phổ biến trong ít nhất một phân hoạch**.
* Giúp xử lý song song và giảm số lần quét dữ liệu xuống chỉ còn $2$ lần.


* **Lấy mẫu Dữ liệu (Sampling):**
* Trích xuất một tập con đại diện để tính xác suất các tập mục phổ biến.
* Giảm đáng kể chi phí tính toán, có thể dùng nhiều mẫu để tăng độ chính xác.


* **Thu giảm Giao dịch (Transaction Reduction):**
* Loại bỏ ngay các giao dịch không chứa bất kỳ tập mục phổ biến nào hiện tại.
* Giúp thu nhỏ quy mô cơ sở dữ liệu cần quét cho các vòng lặp tiếp theo.



---

### 3. Cấu trúc Dữ liệu & Định dạng Biểu diễn Nâng cao

* **Cây Băm (Hash Tree):**
* Tổ chức các tập mục ứng viên vào một cấu trúc cây sử dụng hàm băm (hash function).
* Khi duyệt giao dịch, việc tìm và đếm độ hỗ trợ của các tập ứng viên diễn ra nhanh chóng bằng cách duyệt theo các nhánh cây thay vì so sánh tuyến tính.


* **Định dạng Dữ liệu Chiều dọc (Vertical Data Format / Diffset):**
* Biến đổi dữ liệu từ dạng `TID: Items` (mã giao dịch $\rightarrow$ danh sách sản phẩm) sang dạng `Item: TIDs` (sản phẩm $\rightarrow$ danh sách mã giao dịch chứa sản phẩm đó) — tương tự chỉ mục đảo (inverted index) trong máy tìm kiếm.
* Việc tính `support` của tập hợp nhiều mục chỉ đơn giản là **thao tác giao tập hợp (intersection)** giữa các danh sách `TID`, loại bỏ hoàn toàn việc phải quét lại dữ liệu thô.



---

> **Kết luận:** Bằng cách kết hợp giữa tư duy phân hoạch/lấy mẫu và tối ưu cấu trúc dữ liệu (Cây băm, Vertical format), chi phí tính toán và số lần đọc/ghi cơ sở dữ liệu được giảm thiểu đáng kể, mở đường cho việc xử lý dữ liệu quy mô lớn (Big Data).
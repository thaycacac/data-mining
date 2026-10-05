Dưới đây là tóm tắt các điểm quan trọng của bài học về **Làm sạch Dữ liệu & Tích hợp Dữ liệu (Data Cleaning & Integration)**:

---

### 1. Làm sạch Dữ liệu (Data Cleaning)

Tập trung giải quyết 3 nhóm vấn đề cốt lõi:

* **Xử lý Dữ liệu Khuyết thiếu (Incomplete Data / Missing Values):**
* *Loại bỏ:* Xóa bỏ các đối tượng hoặc thuộc tính bị thiếu dữ liệu.
* *Điền giá trị thiếu (Imputation):* Thực hiện thủ công hoặc tự động bằng cách sử dụng hằng số toàn cục (global constant), giá trị trung bình của thuộc tính (attribute mean), trung bình theo lớp (class mean), mô hình hồi quy (regression), thuật toán $k$-láng giềng gần nhất ($k$-NN), hoặc ước lượng xác suất (probabilistic estimation).


* **Xử lý Dữ liệu Nhiễu (Noisy Data):**
* *Làm mịn (Smoothing):* Sử dụng các mô hình hồi quy để điều chỉnh nhiễu.
* *Phát hiện giá trị ngoại lệ (Outliers):* Áp dụng thuật toán phân cụm (clustering) để nhận diện và loại bỏ hoặc điều chỉnh các điểm dữ liệu bất thường.


* **Xử lý Dữ liệu Không nhất quán (Inconsistent Data):**
* Sử dụng sự hiểu biết về ngữ nghĩa (semantic understanding) và phân tích thống kê để phát hiện các mâu thuẫn giữa các thuộc tính hoặc giữa các nguồn dữ liệu khác nhau, sau đó tiến hành sửa lỗi hoặc ánh xạ (mapping) lại cho đồng nhất.



---

### 2. Tích hợp Dữ liệu (Data Integration)

Kết hợp dữ liệu từ nhiều nguồn khác nhau thành một kho dữ liệu duy nhất:

* **Nhận diện Thực thể (Entity Identification):** Xác định các đối tượng giống nhau (như khách hàng, sản phẩm) khi chúng đến từ các nguồn dữ liệu có tên gọi hoặc định dạng khác nhau.
* **Xử lý Dữ liệu Dư thừa (Redundancy):** Áp dụng phân tích tương quan (correlation analysis) để phát hiện và loại bỏ các thuộc tính dư thừa hoặc trùng lặp giữa các bảng/nguồn dữ liệu.

---

> **Bài học cốt lõi:** Làm sạch triệt để và tích hợp đồng bộ là hai tiền đề quan trọng giúp loại bỏ sai lệch, đảm bảo tập dữ liệu đầu vào nhất quán và đáng tin cậy cho các thuật toán khai phá.
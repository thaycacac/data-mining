Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Biến đổi Dữ liệu (Data Transformation) & Các Phương pháp Chuẩn hóa**:

---

### 1. Tổng quan Tiền xử lý Dữ liệu

* **Làm sạch & Tích hợp:** Nhận diện và xử lý các vấn đề dữ liệu thiếu, nhiễu, không nhất quán và tích hợp dữ liệu từ nhiều nguồn khác nhau (xử lý trùng lặp, mâu thuẫn).

---

### 2. Các Kỹ thuật Biến đổi Dữ liệu (Data Transformation Techniques)

* **Làm mịn & Loại bỏ ngoại lệ (Smoothing & Outlier Removal):** Giảm bớt nhiễu và loại bỏ các điểm dữ liệu bất thường.
* **Gom cụm / Tổng hợp (Aggregation):** Tổng hợp nhiều điểm dữ liệu thành dạng tóm tắt (ví dụ: gom dữ liệu cấp Thành phố lên cấp Tỉnh/Bang).
* **Tổng quát hóa (Generalization):** Ánh xạ dữ liệu chi tiết lên các cấp độ cao hơn (ví dụ: ánh xạ sản phẩm cụ thể về Danh mục sản phẩm).
* **Rời rạc hóa (Discretization):** Chuyển đổi các giá trị số liên tục thành các khoảng (intervals) nhằm hỗ trợ thuật toán nhận diện mẫu dễ dàng hơn.
* **Xây dựng thuộc tính (Attribute Construction):** Tạo ra các thuộc tính mới từ các thuộc tính hiện có để phục vụ tốt hơn cho bài toán khai phá cụ thể.
* **Chuẩn hóa (Normalization):** Đưa các thuộc tính về cùng một thang đo so sánh được, tránh trường hợp các thuộc tính có biên độ lớn áp đảo các thuộc tính khác.

---

### 3. Các Phương pháp Chuẩn hóa phổ biến (Normalization Methods)

* **Min-Max Normalization:**
* Ánh xạ dữ liệu về một khoảng xác định, thường là $[0, 1]$.
* Công thức: $v' = \frac{v - \text{Min}}{\text{Max} - \text{Min}} (NewMax - NewMin) + NewMin$


* **Mean Normalization:**
* Đưa dữ liệu về tâm là giá trị trung bình (mean) và chia cho khoảng biến thiên ($\text{Max} - \text{Min}$).
* Thể hiện vị trí tương quan của điểm dữ liệu so với giá trị trung bình.


* **Z-score Normalization (Standardization):**
* Chuẩn hóa dữ liệu dựa trên giá trị trung bình ($\mu$) và độ lệch chuẩn ($\sigma$).
* Cho biết một giá trị nằm cách giá trị trung bình bao nhiêu độ lệch chuẩn.
* Công thức: $v' = \frac{v - \mu}{\sigma}$



---

> **Kết luận:** Các bước biến đổi và chuẩn hóa giúp dữ liệu trở nên sạch sẽ, đồng nhất về mặt thang đo và sẵn sàng cho các mô hình khai phá dữ liệu ở giai đoạn sau.
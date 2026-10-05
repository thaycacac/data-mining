Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Thu giảm Số chiều (Dimensionality Reduction) & Thu giảm Số lượng Dữ liệu (Numerosity Reduction)**:

---

### 1. Thu giảm Số chiều Dữ liệu (Dimensionality Reduction)

Tập trung vào việc giảm bớt số lượng thuộc tính (số cột) nhằm giảm độ phức tạp không gian và thời gian tính toán.

* **Lựa chọn Thuộc tính (Attribute / Feature Selection):** Loại bỏ các thuộc tính dư thừa hoặc không quan trọng.
* **Phân tích Thành phần Chính (PCA - Principal Component Analysis):** Biến đổi dữ liệu sang một hệ tọa độ mới gồm các thành phần vuông góc (orthogonal components) giữ lại phần lớn biến thiên/thông tin của dữ liệu, sau đó chỉ chọn ra các thành phần chính yếu nhất.
* **Biến đổi Wavelet (Wavelet Transformation):** Phân tích tín hiệu thành các chuỗi sóng nhỏ ở các độ chi tiết khác nhau, chỉ giữ lại các hệ số quan trọng để giảm kích thước dữ liệu mà không làm mất đi các đặc trưng chính.

---

### 2. Thu giảm Số lượng Dữ liệu (Numerosity Reduction)

Tập trung vào việc giảm số lượng điểm dữ liệu/bản ghi (số dòng) bằng cách thay thế tập dữ liệu ban đầu bằng một dạng biểu diễn nhỏ hơn.

* **Phương pháp Tham số (Parametric Methods):** Khớp dữ liệu vào một mô hình giả định (ví dụ: mô hình Hồi quy) và chỉ lưu trữ các tham số của mô hình thay vì lưu toàn bộ dữ liệu thô.
* **Phương pháp Phi tham số (Non-parametric Methods):** Không đưa ra giả định về mô hình dữ liệu:
* *Lấy mẫu (Sampling):* Lấy mẫu ngẫu nhiên có/không hoàn lại (with/without replacement), lấy mẫu phân tầng (stratified sampling), hoặc lấy mẫu theo cụm (cluster sampling) để chọn ra tập con đại diện.
* *Gom cụm (Clustering):* Đại diện cho cả một nhóm điểm dữ liệu bằng điểm tâm (centroid) và bán kính của cụm.
* *Biểu đồ tần số (Histograms):* Gom dữ liệu thành các thùng (buckets) và lưu trữ tần suất xuất hiện.
* *Tổng hợp (Aggregation):* Kết hợp nhiều điểm dữ liệu thành các chỉ số tóm tắt.



---

### 3. Tổng kết Quy trình Tiền xử lý Dữ liệu

* **Mục tiêu tổng quát:** Phát hiện và khắc phục các vấn đề của dữ liệu (thiếu, nhiễu, không nhất quán), chuẩn hóa thang đo và thu giảm quy mô dữ liệu.
* **Giá trị thực tiễn:** Tiền xử lý hiệu quả giúp cải thiện trực tiếp **chất lượng tri thức đầu ra** và **tốc độ thực thi** của các mô hình khai phá dữ liệu ở các bước tiếp theo.
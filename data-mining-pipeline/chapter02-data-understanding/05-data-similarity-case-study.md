Dưới đây là tóm tắt các điểm quan trọng của bài học về **Thực hành Hiểu dữ liệu & Lựa chọn Thước đo Tương đồng (Data Understanding in Practice)**:

---

### 1. Lựa chọn Thước đo Tương đồng phù hợp (Choosing Similarity Measures)

* **Không có một thước đo duy nhất cho mọi bài toán:** Mỗi loại thuộc tính và đặc điểm dữ liệu đòi hỏi một phương pháp tính toán độ tương đồng/khác biệt riêng.
* **Căn cứ lựa chọn:** Dựa vào các đặc tính dữ liệu như độ dày/mật độ (density), tính liên tục (continuity), độ thưa (sparsity) và tính bất đối xứng (asymmetric).
* *Mật độ & Tính liên tục:* Dùng khoảng cách **Euclidean** hoặc **Manhattan**.
* *Độ thưa & Số chiều cao:* Dùng **Cosine similarity** (văn bản) hoặc **Jaccard similarity** (tập hợp/thuộc tính bất đối xứng).



---

### 2. Thực hành Hiểu dữ liệu: Nghiên cứu tình huống Mạng xã hội (Social Media Case Study)

* Dữ liệu mạng xã hội rất phong phú: bao gồm người dùng, bài viết, tương tác/phản ứng (reactions), mốc thời gian và mạng lưới kết nối.
* **Lọc tập dữ liệu con (Subsets):** Cần chọn đúng phạm vi dữ liệu phục vụ cho mục tiêu cụ thể (ví dụ: tập trung vào phản ứng/tương tác thay vì toàn bộ cấu trúc đồ thị mạng lưới).

---

### 3. Phân tích Thống kê & Trực quan hóa dữ liệu

* **Phân tích phân phối:** Đánh giá các xu hướng tập trung và độ phân tán (ví dụ: số bài đăng trung bình của mỗi người dùng) để phát hiện kịp thời các giá trị ngoại lệ (outliers).
* **Ứng dụng Trực quan hóa:** Sử dụng sơ đồ hộp (Boxplot), biểu đồ tần số (Histogram) và biểu đồ tán xạ (Scatter plot) để khám phá cấu trúc dữ liệu, hỗ trợ cho việc tính toán độ tương đồng chính xác hơn.

---

> **Thông điệp cốt lõi:** Bài học nhấn mạnh tầm quan trọng của **tư duy phân tích (analytical reasoning)**, **tri thức ngành (domain knowledge)** và **khám phá dữ liệu cẩn thận** trước khi tiến hành các bước mô hình hóa hay thuật toán phức tạp hơn.
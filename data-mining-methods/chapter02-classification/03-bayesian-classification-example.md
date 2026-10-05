Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Phương pháp Phân lớp Bayes: Naive Bayes & Mạng Niềm tin Bayes (Bayesian Classification & Bayesian Belief Networks)**:

---

### 1. Định lý Bayes & Bộ phân lớp Naive Bayes (Naive Bayesian Classifier)

* **Định lý Bayes trong Phân lớp:**
* Tính xác suất hậu kỳ (Posterior Probability) $P(C\vert{}X)$ của một lớp $C$ khi biết tập đặc trưng/thuộc tính $X$.
* Công thức cốt lõi: $P(C\vert{}X) = \frac{P(X\vert{}C) \cdot P(C)}{P(X)}$.


* **Giả định "Ngây thơ" (Naive Assumption):**
* Giả định các thuộc tính **độc lập điều kiện (conditional independence)** với nhau khi đã biết nhãn lớp.
* Giúp đơn giản hóa việc tính toán $P(X\vert{}C)$ bằng cách nhân xác suất điều kiện của từng thuộc tính riêng lẻ:

$$P(X\vert{}C) = P(x_1\vert{}C) \cdot P(x_2\vert{}C) \cdot \dots \cdot P(x_n\vert{}C)$$




* **Hiệu chỉnh Laplace (Laplacian Correction):**
* Giải quyết sự cố **xác suất bằng 0 (Zero-Probability Problem)** khi một giá trị thuộc tính chưa từng xuất hiện trong tập huấn luyện cho một lớp cụ thể (tránh việc làm toàn bộ tích xác suất bằng 0).



---

### 2. Quy trình Thực hành & Ứng dụng Naive Bayes

1. **Tính Xác suất Tiền kỳ (Prior Probabilities):** Tính $P(C)$ cho từng lớp từ dữ liệu huấn luyện (ví dụ: Tỷ lệ hồ sơ vay được Duyệt vs. Không duyệt).
2. **Tính Xác suất Điều kiện (Conditional Probabilities):** Tính $P(x_i\vert{}C)$ cho từng thuộc tính của đối tượng mới.
3. **So sánh & Dự đoán (Maximum A Posteriori - MAP):**
* So sánh tích xác suất của từng lớp.
* Lớp có xác suất hậu kỳ cao nhất sẽ được chọn làm **nhãn lớp dự đoán (predicted label)**.



---

### 3. Mạng Niềm tin Bayes (Bayesian Belief Networks - BBN)

* **Động lực:** Khắc phục nhược điểm của Naive Bayes khi giả định độc lập thuộc tính không đúng trong thực tế.
* **Cấu trúc Mạng:**
* **Đồ thị Hướng Không Chu trình (DAG - Directed Acyclic Graph):** Các nút (nodes) đại diện cho các biến ngẫu nhiên; các cung có hướng (edges) biểu diễn mối quan hệ phụ thuộc trực tiếp giữa các biến.
* **Bảng Xác suất Điều kiện (Conditional Probability Tables - CPT):** Định lượng mối quan hệ phụ thuộc giữa mỗi nút và các nút cha của nó.


* **Giá trị mang lại:** Mô hình hóa tường minh các mối phụ thuộc điều kiện phức tạp giữa các thuộc tính, giúp nâng cao độ chính xác phân lớp trong các bài toán thực tế.

---

> **Kết luận:** Trong khi **Naive Bayes** cung cấp một giải pháp phân lớp cực kỳ nhanh, đơn giản và hiệu quả trên dữ liệu lớn, thì **Mạng Niềm tin Bayes** lại mang đến sự linh hoạt và chính xác cao hơn khi cần xử lý các thuộc tính có mối quan hệ phụ thuộc lẫn nhau.
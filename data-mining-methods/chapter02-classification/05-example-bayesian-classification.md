Dưới đây là tóm tắt các điểm cốt lõi của bài học thực hành **Áp dụng Thuật toán Phân lớp Naive Bayes & Kỹ thuật Mịn hóa Laplace (Naive Bayes Application & Laplace Smoothing)**:

---

### 1. Định lý Bayes & Quy trình So sánh Xác suất

* **Mục tiêu:** Tính xác suất hậu kỳ $P(\text{Class} \mid X)$ cho từng lớp (ví dụ: `Picnic = Yes` và `Picnic = No`) và gán nhãn thuộc lớp có xác suất cao nhất (**Maximum A Posteriori - MAP**).
* **Loại bỏ Mẫu số $P(X)$:** Theo công thức Bayes:

$$P(\text{Class} \mid X) = \frac{P(X \mid \text{Class}) \cdot P(\text{Class})}{P(X)}$$



Vì $P(X)$ là hằng số giống nhau với tất cả các lớp khi xét trên cùng một mẫu dữ liệu, nên khi so sánh ta **loại bỏ $P(X)$** và chỉ cần so sánh tử số $P(X \mid \text{Class}) \cdot P(\text{Class})$.

---

### 2. Giả định "Ngây thơ" (Naive Assumption) & Tính toán

* Các thuộc tính trong $X$ (ví dụ: `Weather = Overcast`, `Temperature = Mild`, `Humidity = High`, `Wind = False`) được giả định **độc lập với nhau** khi đã biết nhãn lớp.
* Tích xác suất điều kiện được tính đơn giản bằng cách nhân các xác suất thuộc tính thành phần:

$$P(X \mid \text{Class}) = P(x_1 \mid \text{Class}) \times P(x_2 \mid \text{Class}) \times \dots \times P(x_n \mid \text{Class})$$



---

### 3. Xử lý Sự cố Xác suất bằng 0 với Mịn hóa Laplace (Laplace Smoothing)

* **Vấn đề:** Nếu một giá trị thuộc tính chưa từng xuất hiện trong tập huấn luyện cho một lớp nào đó (ví dụ: `P(Weather = Overcast | Picnic = No) = 0`), toàn bộ tích xác suất của lớp đó sẽ **bằng 0**, triệt tiêu mọi thông tin từ các thuộc tính còn lại.
* **Giải pháp (Laplacian Correction / Smoothing):**
* Cộng thêm $1$ vào số đếm tần suất của mỗi thuộc tính ở tử số, và cộng thêm $k$ (với $k$ là số giá trị phân biệt của thuộc tính đó) vào mẫu số.
* Giúp tránh giá trị $0$ tuyệt đối mà vẫn bảo toàn tỷ lệ tương quan giữa các xác suất.



---

### 4. Quy trình 5 Bước Hoàn chỉnh của Naive Bayes

1. **Tính xác suất tiền kỳ (Prior Probabilities):** $P(\text{Class})$ cho từng lớp.
2. **Tính xác suất điều kiện (Conditional Probabilities):** $P(x_i \mid \text{Class})$ dựa trên tần suất dữ liệu.
3. **Áp dụng Mịn hóa Laplace:** Sửa đổi các xác suất điều kiện nếu có số đếm bằng $0$.
4. **Nhân tích xác suất:** Tính $P(\text{Class}) \times \prod P(x_i \mid \text{Class})$ cho mỗi lớp dựa vào giả định độc lập.
5. **So sánh & Phân lớp:** Chọn lớp có giá trị tích xác suất lớn nhất làm kết quả dự đoán.

---

> **Bài học cốt lõi:** Naive Bayes biến một bài toán tính xác suất phức tạp thành các phép nhân tần suất đơn giản. Kỹ thuật mịn hóa Laplace là cơ chế bảo vệ bắt buộc giúp mô hình hoạt động ổn định trên tập dữ liệu thực tế.
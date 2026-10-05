Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Quy trình Xây dựng Cây Quyết định (Decision Tree Induction & Attribute Selection)**:

---

### 1. Cơ bản về Cây Quyết định (Decision Tree Basics)

* **Khái niệm:** Cây quyết định thực hiện phân lớp dữ liệu bằng cách đặt ra một chuỗi câu hỏi nối tiếp nhau về các thuộc tính. Mỗi nút bên trong (internal node) đại diện cho một câu hỏi kiểm tra thuộc tính, nhánh (branch) đại diện cho kết quả kiểm tra, và nút lá (leaf node) đại diện cho nhãn lớp quyết định.
* **Ưu điểm lớn nhất:** **Tính diễn giải cao (High Interpretability)** — cho phép con người hiểu rõ chính xác mô hình dựa vào tiêu chí nào để đưa ra quyết định.

---

### 2. Quy trình Xây dựng Cây (Tree Construction)

* Thuật toán áp dụng tư tưởng **Chia để trị (Divide-and-Conquer)** từ trên xuống (top-down) và mang tính **Tham lam (Greedy Strategy)**:
1. Chọn thuộc tính tốt nhất để phân tách dữ liệu tại nút hiện tại.
2. Chia tập dữ liệu thành các tập con tương ứng với các giá trị của thuộc tính đó.
3. Lặp lại đệ quy quy trình trên cho từng tập con cho đến khi các dữ liệu ở nút lá hoàn toàn tinh khiết (pure - thuộc cùng một lớp) hoặc đạt tiêu chí dừng.



---

### 3. Tiêu chí Chọn Thuộc tính & Các Thước đo (Attribute Selection Measures)

* **Mức tăng Thông tin (Information Gain - Thuật toán ID3):**
* Dựa trên khái niệm **Độ hỗn loạn / Độ do dự (Entropy)** từ Lý thuyết Thông tin.
* *Mục tiêu:* Chọn thuộc tính giúp giảm độ hỗn loạn nhiều nhất (tăng tối đa độ tinh khiết của lớp sau phân tách).
* *Hạn chế:* Thiên vị các thuộc tính có quá nhiều giá trị duy nhất (ví dụ: `ID_Khách_hàng`), dễ gây hiện tượng **Quá khớp (Overfitting)**.


* **Tỷ lệ Mức tăng Thông tin (Gain Ratio - Thuật toán C4.5):**
* Khắc phục nhược điểm của Information Gain bằng cách chuẩn hóa mức tăng thông tin thông qua **Thông tin Phân tách (Split Information)**.
* Giúp phạt các thuộc tính chia ra quá nhiều nhánh nhỏ lẻ, ưu tiên các thuộc tính chia nhánh có ý nghĩa thực tiễn.


* **Chỉ số Gini (Gini Index - Thuật toán CART):**
* Đo lường mức độ sai lệch/không tinh khiết của tập dữ liệu ($1 - \sum p_i^2$).
* Thuật toán CART (Classification and Regression Trees) chỉ thực hiện **Phân tách Nhị phân (Binary Splits)** tại mỗi nút, giúp tạo ra cấu trúc cây cân bằng và hiệu quả về mặt tính toán.



---

> **Kết luận:** Xây dựng cây quyết định là một trong những phương pháp phân lớp kinh điển và trực quan nhất. Việc lựa chọn đúng tiêu chí phân tách (Information Gain, Gain Ratio, hay Gini Index) đóng vai trò quyết định đến độ chính xác và khả năng tổng quát hóa của mô hình.
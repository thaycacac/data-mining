Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Thuật toán Máy Vector Hỗ trợ (Support Vector Machines - SVM) & Xử lý Dữ liệu Phi tuyến (Non-linear Classification)**:

---

### 1. Hệ thống hóa các Phương pháp Phân lớp (Classification Overview)

* **Học có giám sát (Supervised Learning):** Xây dựng mô hình dựa trên tập dữ liệu đã gắn nhãn.
* **So sánh ba phương pháp cốt lõi:**
1. *Decision Trees (Cây quyết định):* Phân tách vùng dữ liệu dựa trên việc chọn thuộc tính tối ưu (Information Gain / Gini Index).
2. *Bayesian Classification (Phân lớp Bayes):* Ước lượng xác suất hậu kỳ dựa trên giả định độc lập (Naive Bayes) hoặc mạng đồ thị phụ thuộc (Bayesian Belief Networks).
3. *Support Vector Machines (SVM):* Tiếp cận dưới góc độ hình học tối ưu bằng cách tìm ranh giới phân tách lớp có lề cực đại.



---

### 2. Thuật toán Máy Vector Hỗ trợ (SVM - Support Vector Machines)

* **Siêu phẳng Tối ưu (Optimal Hyperplane):** SVM tìm một siêu phẳng quyết định để phân chia các lớp dữ liệu sao cho **khoảng cách lề (margin)** giữa hai lớp là lớn nhất (Maximum Margin).
* **Vector Hỗ trợ (Support Vectors):** Là các điểm dữ liệu nằm sát siêu phẳng quyết định nhất. Các điểm này trực tiếp định hình biên giới phân lớp; nếu loại bỏ các điểm dữ liệu khác, siêu phẳng quyết định vẫn không thay đổi.

---

### 3. Xử lý Dữ liệu Không phân tách Tuyên tính (Non-linearly Separable Data)

* **Biến đổi Không gian (Space Transformation):** Khi dữ liệu không thể phân tách bằng đường thẳng/siêu phẳng phẳng ở không gian gốc, dữ liệu sẽ được ánh xạ (transform) sang một không gian đặc trưng nhiều chiều hơn (Higher-dimensional Space) — nơi các lớp trở nên phân tách tuyến tính được.
* **Mẹo Hạt nhân (Kernel Trick / Kernel Functions):**
* *Vấn đề:* Việc tính toán ánh xạ trực tiếp lên không gian nhiều chiều tốn chi phí tính toán cực kỳ lớn.
* *Giải pháp:* Sử dụng các **hàm Kernel** (như RBF, Polynomial, Sigmoid) để tính toán trực tiếp tích vô hướng (dot product) của các vector trong không gian cao chiều mà **không cần thực sự ánh xạ toàn bộ dữ liệu** lên không gian đó.
* *Ý nghĩa:* Giúp SVM giải quyết hiệu quả bài toán phi tuyến phức tạp với chi phí tính toán thấp.



---

> **Kết luận:** SVM là một trong những thuật toán phân lớp mạnh mẽ nhất trên dữ liệu có số chiều lớn, nhờ kết hợp giữa nguyên lý tối ưu hóa lề cực đại (Maximum Margin) và sức mạnh của kỹ thuật Kernel Trick.
Dưới đây là tóm tắt các điểm cốt lõi của bài học tổng kết về **So sánh Thuật toán Phân lớp, Phương pháp Tập hợp Mô hình (Ensemble Methods) & Bộ Chỉ số Đánh giá (Model Evaluation Metrics)**:

---

### 1. Hệ thống hóa & So sánh các Thuật toán Phân lớp

| Thuật toán | Cơ chế cốt lõi | Ưu điểm nổi bật |
| --- | --- | --- |
| **Decision Trees** | Chia để trị (top-down, greedy) dựa trên Entropy/Gini | **Dễ diễn giải (Interpretable):** Đường đi quyết định minh bạch, trực quan. |
| **Bayesian Classification** | Nền tảng xác suất (Bayes' Theorem + Naive Assumption) | **Học tăng cường (Incremental):** Cập nhật mô hình khi có dữ liệu mới mà không cần huấn luyện lại từ đầu. |
| **Support Vector Machines (SVM)** | Siêu phẳng tối ưu + Kernel Trick | **Hiệu năng vượt trội:** Độ chính xác rất cao, thường đứng đầu trong các so sánh thực nghiệm. |
| **Neural Networks** | Lớp ẩn + Lan truyền ngược (Backpropagation) | **Biểu diễn phức tạp:** Học tốt mối quan hệ phi tuyến; tuy nhiên là "hộp đen" (đang được cải thiện qua Explainable AI - XAI). |

---

### 2. Các Phương pháp Tập hợp Mô hình (Ensemble Learning)

Tập hợp mô hình kết hợp nhiều bộ phân lớp cơ sở (base classifiers) để cải thiện độ chính xác và giảm rủi ro quá khớp (overfitting).

* **Bagging (Bootstrap Aggregating):**
* Huấn luyện các mô hình độc lập trên các tập con dữ liệu lấy mẫu ngẫu nhiên có hoàn lại (sampling with replacement).
* Kết hợp dự đoán bằng cơ chế **trọng số bằng nhau** (ví dụ: bỏ phiếu đa số - majority voting). *Ví dụ điển hình: Random Forest.*


* **Boosting:**
* Huấn luyện các mô hình **nối tiếp nhau (sequential)**.
* Tăng trọng số cho các mẫu dự đoán sai ở mô hình trước, gán **trọng số khác nhau** cho mỗi mô hình dựa trên tỷ lệ lỗi. Tập trung giải quyết các mẫu dữ liệu "khó phân lớp". *Ví dụ điển hình: AdaBoost, XGBoost.*



---

### 3. Kỹ thuật Split Dữ liệu & Đánh giá Mô hình (Model Evaluation)

* **Phân tách Dữ liệu Độc lập:** Sử dụng phương pháp **Holdout** (chia tập Train/Test) hoặc **K-Fold Cross-Validation** để đảm bảo đánh giá khách quan, tránh rò rỉ dữ liệu (data leakage).
* **Ma trận Nhầm lẫn (Confusion Matrix):** Tổng hợp $4$ trường hợp dự đoán:
* **TP** (True Positive), **TN** (True Negative)
* **FP** (False Positive - Lỗi Loại I), **FN** (False Negative - Lỗi Loại II)


* **Các Chỉ số Đánh giá Cốt lõi:**
* **Sensitivity / Recall (TPR):** $\frac{\text{TP}}{\text{TP} + \text{FN}}$ — Tỷ lệ phát hiện đúng các mẫu thực tế là Positive.
* **Specificity (TNR):** $\frac{\text{TN}}{\text{TN} + \text{FP}}$ — Tỷ lệ nhận diện đúng các mẫu thực tế là Negative.
* **Precision:** $\frac{\text{TP}}{\text{TP} + \text{FP}}$ — Độ chính xác trong số các mẫu được dự đoán là Positive.
* **Accuracy:** $\frac{\text{TP} + \text{TN}}{\text{Tổng số mẫu}}$ — Tỷ lệ tổng số mẫu được dự đoán đúng.



---

### 4. Đổi chác (Trade-offs) & Ngữ cảnh Ứng dụng

* **Đổi chác FP vs. FN:** Tùy thuộc vào bài toán thực tế để quyết định tối ưu chỉ số nào. Ví dụ: Trong **phát hiện gian lận** hoặc **chẩn đoán bệnh nguy hiểm**, việc bỏ sót ca bệnh (False Negative) nguy hiểm hơn nhiều so với báo động nhầm (False Positive) $\rightarrow$ Ưu tiên tối ưu **Sensitivity / Recall**.
* **Phân lớp Nhiều lớp (Multi-class Classification):** Cần cân nhắc thêm mức độ "gần đúng" của các lớp dự đoán chứ không chỉ đánh giá khớp tuyệt đối (exact match).

---

> **Kết luận:** Không có thuật toán nào là "vạn năng" (No Free Lunch Theorem). Việc chọn thuật toán, kỹ thuật Ensemble hay bộ chỉ số đánh giá phụ thuộc hoàn toàn vào **bản chất dữ liệu** và **mục tiêu kinh doanh/thực tế** của bài toán.
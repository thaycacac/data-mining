Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Đánh giá Mô hình Dự báo, Đường cong ROC & Kiểm định Thống kê So sánh Mô hình (Prediction Error, ROC Curve & Statistical Significance Testing)**:

---

### 1. Thước đo Lỗi trong Bài toán Dự báo (Prediction / Regression Error)

Đối với các mô hình dự báo giá trị số liên tục, việc đánh giá dựa trên mức độ chênh lệch giữa giá trị dự báo ($\hat{y}_i$) và giá trị thực tế ($y_i$):

* **Các thước đo phổ biến:**
* **Lỗi tuyệt đối (Absolute Error):** $\vert{}y_i - \hat{y}_i\vert{}$
* **Lỗi bình phương (Squared Error):** $(y_i - \hat{y}_i)^2$
* **Lỗi tuyệt đối trung bình (MAE - Mean Absolute Error):** $\frac{1}{n} \sum \vert{}y_i - \hat{y}_i\vert{}$
* **Lỗi bình phương trung bình (MSE - Mean Squared Error):** $\frac{1}{n} \sum (y_i - \hat{y}_i)^2$
* **Các biến thể tỷ lệ (Relative Errors):** Đo lường sai số dưới dạng phần trăm/tỷ lệ để so sánh giữa các quy mô dữ liệu khác nhau.



---

### 2. Đánh giá Trực quan bằng Đường cong ROC (ROC Curve & AUC)

* **Khái niệm:** Đường cong ROC (Receiver Operating Characteristic) biểu diễn mối quan hệ đổi chác giữa:
* Trục tung: **True Positive Rate (TPR / Sensitivity)** = $\frac{\text{TP}}{\text{TP} + \text{FN}}$
* Trục hoành: **False Positive Rate (FPR / 1 - Specificity)** = $\frac{\text{FP}}{\text{TN} + \text{FP}}$


* **Diễn giải:**
* Đường chéo ($y = x$): Đại diện cho một bộ phân lớp đoán ngẫu nhiên (Random Classifier).
* Đường cong **càng tiệm cận góc trên bên trái** (TPR cao, FPR thấp): Mô hình càng tối ưu.
* **Diện tích dưới đường cong (AUC - Area Under Curve):** Điểm AUC càng tiến gần $1.0$ thể hiện khả năng phân biệt lớp của mô hình càng vượt trội.



---

### 3. So sánh Mô hình bằng Kiểm định Thống kê t-Test (Statistical Model Comparison)

* **Động lực:** Khi so sánh hai mô hình (ví dụ: SVM vs. Random Forest) qua $k$-fold cross-validation, hiệu năng trung bình chênh lệch có thể chỉ do sự may mắn ngẫu nhiên khi chia dữ liệu.
* **Quy trình Kiểm định Paired t-Test:**
1. Tính mức chênh lệch sai số giữa hai mô hình trên từng lượt $k$-fold.
2. Tính giá trị **t-statistic** dựa trên độ lệch chuẩn và trung bình chênh lệch.
3. So sánh giá trị $t$ tính được với **giá trị tới hạn (critical value)** từ bảng phân phối $t$-Student với bậc tự do $\text{df} = k - 1$ ở mức ý nghĩa cho trước (thường là $\alpha = 0.05$).
4. **Kết luận:** Bác bỏ giả thuyết không ($H_0$) nếu $t > t_{\text{critical}}$, khẳng định một mô hình vượt trội hơn hẳn **có ý nghĩa thống kê** (statistically significant).



---

### 4. Tổng kết Toàn bộ Module Phân lớp & Dự báo (Classification & Prediction)

> **Khung tri thức hoàn chỉnh:**
> 1. **Mô hình hóa:** Đã nắm vững các thuật toán cốt lõi (Decision Trees, Naive Bayes/BBN, SVM, Neural Networks/Deep Learning, Ensemble Bagging/Boosting).
> 2. **Đánh giá Phân lớp (Discrete):** Sử dụng Confusion Matrix, Precision, Recall, F1-Score, Sensitivity/Specificity.
> 3. **Đánh giá Dự báo (Continuous):** Sử dụng MAE, MSE, RMSE, R-squared.
> 4. **So sánh & Kiểm định:** Sử dụng đường cong ROC/AUC để so sánh ngưỡng quyết định và Paired t-Test để xác nhận sự vượt trội về mặt thống kê.
> 
>
Dưới đây là tóm tắt các điểm cốt lõi của bài học mở đầu chương **Phân lớp Dữ liệu (Fundamentals of Classification & Evaluation)**:

---

### 1. Học có giám sát (Supervised Learning) vs. Học không giám sát (Unsupervised Learning)

* **Học có giám sát (Supervised Learning):** Mô hình được huấn luyện trên tập dữ liệu đã có **nhãn lớp định trước (labeled data)**. Mục tiêu là học hàm ánh xạ để gán nhãn chính xác cho các dữ liệu mới chưa từng thấy.
* **Học không giám sát (Unsupervised Learning):** Mô hình làm việc với dữ liệu **chưa có nhãn (unlabeled data)**, tự động khám phá các cấu trúc, mẫu hoặc nhóm tự nhiên (phân cụm) ẩn trong dữ liệu.

---

### 2. Phân biệt Phân lớp (Classification) & Dự báo (Prediction)

* **Phân lớp (Classification):** Dự đoán thuộc tính nhãn thuộc tập các **danh mục/lớp rời rạc (finite discrete categories)**.
* *Ví dụ:* Phát hiện giao dịch gian lận (Có/Không), chẩn đoán bệnh (Bị bệnh/Khỏe mạnh), phân loại email (Spam/Non-Spam).


* **Dự báo (Prediction / Regression):** Ước lượng các **giá trị số học liên tục (continuous numerical values)**.
* *Ví dụ:* Dự báo giá cổ phiếu, doanh thu bán hàng, số lượng lượt thích trên mạng xã hội.



---

### 3. Quy trình Phân lớp & Các Tiêu chí Đánh giá Mô hình

* **Quy trình 2 bước tiêu chuẩn:**
1. *Giai đoạn Học (Learning / Training):* Xây dựng mô hình phân lớp từ tập dữ liệu huấn luyện (Training Data).
2. *Giai đoạn Đánh giá & Phân lớp (Testing / Evaluation):* Sử dụng mô hình đã huấn luyện để dự đoán nhãn cho tập dữ liệu kiểm thử (Test Data) và so sánh nhãn dự đoán với nhãn thực tế.


* **Các tiêu chí đánh giá chất lượng mô hình:**
* **Độ chính xác (Accuracy):** Tỷ lệ dự đoán đúng nhãn trên tổng số mẫu test.
* **Tốc độ (Speed):** Thời gian cần thiết để huấn luyện mô hình (training time) và thời gian thực thi dự đoán (decision-making time).
* **Khả năng diễn giải (Interpretability):** Mức độ dễ hiểu và khả năng giải thích lý do đưa ra quyết định của mô hình (ví dụ: Cây quyết định có tính diễn giải cao hơn Mạng Nơ-ron).
* **Độ bền vững (Robustness):** Khả năng hoạt động ổn định và chính xác của mô hình khi dữ liệu đầu vào chứa nhiễu (noise) hoặc giá trị khuyết thiếu (missing values).
* **Khả năng mở rộng (Scalability):** Khả năng xử lý hiệu quả trên các tập dữ liệu quy mô rất lớn hoặc dữ liệu cập nhật tăng dần (incremental datasets).



---

> **Kết luận:** Bài học đặt nền móng lý thuyết quan trọng để chuyển tiếp từ phân tích mẫu sang Học có giám sát. Các tiêu chí đánh giá này sẽ là thước đo trực tiếp cho các thuật toán phân lớp cụ thể tiếp theo như **Decision Trees**, **Naive Bayes**, hay **k-NN**.
Dưới đây là tóm tắt các điểm quan trọng của bài học thực hành về **Hiểu dữ liệu qua ví dụ Giám sát Chất lượng Không khí Cầm tay (Mobile Air Quality Sensing)**:

---

### 1. Thu thập & Mô tả Dữ liệu

* **Nguồn dữ liệu:** Dữ liệu cảm biến chất lượng không khí thu thập từ thiết bị di động, bao gồm các chỉ số ô nhiễm ($\text{CO}, \text{CO}_2, \text{Ozone}$) cùng các yếu tố môi trường (nhiệt độ, độ ẩm).
* **Quy mô:** Thu thập từ 20–30 người dùng trong khoảng nửa năm tại nhiều địa điểm khác nhau (thành phố Boulder, các chuyến xe buýt đến Denver, sân bay, trung tâm thương mại).

---

### 2. Phân tích Thống kê & Đặc trưng Dữ liệu

* **Các câu hỏi định hình:** Xác định rõ quy mô tập dữ liệu, các loại cảm biến, số lượng người dùng, thời gian nghiên cứu và phạm vi địa lý.
* **Phân tích phân phối:** Tính giá trị trung bình, độ lệch chuẩn và phân phối để xác định khoảng giá trị bình thường, đồng thời nhận diện các **giá trị cực trị (extreme values)** so với các ngưỡng an toàn sức khỏe.

---

### 3. Trực quan hóa & So sánh Dữ liệu

* **Biểu đồ Boxplot:** Dùng để minh họa phân phối dữ liệu và so sánh giữa các người dùng, vị trí hoặc các khoảng thời gian khác nhau.
* **Phân tích Không - Thời gian (Spatial-Temporal Plotting):** Vẽ đồ thị theo không gian và thời gian giúp phát hiện các mẫu di chuyển cũng như sự biến động chất lượng không khí theo vị trí.

---

### 4. Đo lường Độ tương đồng & Khác biệt

* **Kết hợp đa thuộc tính:** Đánh giá độ tương đồng dựa trên cả **chỉ số số học** (nồng độ cảm biến) và **thuộc tính phân loại** (hoạt động của người dùng: đi xe đạp, ngủ, đi xe buýt).
* **Khoảng cách/Độ tương đồng có trọng số (Weighted Distance):** Gán trọng số lớn hơn cho các thuộc tính quan trọng — đặc biệt là khi nồng độ chất ô nhiễm vượt quá ngưỡng an toàn.

---

> **Bài học rút ra:** Cần đặt đúng câu hỏi cho tập dữ liệu, hiểu rõ ngữ nghĩa của từng chỉ số và linh hoạt điều chỉnh phương pháp phân tích theo đúng bối cảnh ứng dụng thực tế.
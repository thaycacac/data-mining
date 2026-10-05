Dưới đây là tóm tắt các điểm cốt lõi của bài học mở đầu về **Phân tích Giá trị Ngoại lệ / Phát hiện Bất thường (Outlier Analysis / Anomaly Detection)**:

---

### 1. Định nghĩa & Mục đích của Giá trị Ngoại lệ (Outliers)

* **Định nghĩa:** Giá trị ngoại lệ (outliers) là các điểm dữ liệu hoặc mẫu dữ liệu có sự **sai lệch đáng kể** so với các quy luật/mẫu hình chung thu được từ các tác vụ học máy (như Phân lớp hay Phân cụm).
* **Mục đích cốt lõi:** Phân tích ngoại lệ **không chỉ đơn thuần là tìm và xóa bỏ dữ liệu lỗi**, mà quan trọng hơn là phát hiện và thấu hiểu các sự kiện bất thường mang ý nghĩa đặc biệt (như gian lận tài chính, sự cố hệ thống, hoặc phát kiến mới).

---

### 2. Ba Loại Giá trị Ngoại lệ Chính (Types of Outliers)

1. **Ngoại lệ Toàn cục (Global Outliers / Point Anomalies):**
* Các điểm dữ liệu đơn lẻ lệch hoàn toàn so với toàn bộ phần dữ liệu còn lại dựa trên một ngưỡng đánh giá cố định.


2. **Ngoại lệ Ngữ cảnh (Contextual / Conditional Outliers):**
* Các điểm dữ liệu chỉ được xem là bất thường khi **đặt trong một ngữ cảnh hoặc kịch bản cụ thể** (ví dụ: nhiệt độ $35^\circ\text{C}$ ở mùa đông là bất thường, nhưng ở mùa hè lại là bình thường).


3. **Ngoại lệ Tập hợp (Collective Outliers):**
* Một nhóm các điểm dữ liệu liên tiếp nhau tạo thành một chuỗi/mẫu hình bất thường, mặc dù từng điểm dữ liệu riêng lẻ trong nhóm đó có thể hoàn toàn bình thường.



---

### 3. Các Ví dụ Ứng dụng Thực tế

* **Dữ liệu Môi trường & Thời tiết:** Sự biến đổi nhiệt độ bề mặt theo chu kỳ mùa (ngữ cảnh).
* **Thời gian Di chuyển (Commute Time):** Thời gian kẹt xe thay đổi bất thường dựa theo giờ cao điểm hoặc thời tiết xấu.
* **Năng lượng Gió:** Chỉ số phát điện tụt giảm bất thường báo hiệu lỗi/hỏng hóc phần cứng tuabin.
* **Mạng xã hội:** Các tương tác bất thường hoặc cấu trúc kết nối lạ giúp phát hiện tài khoản giả mạo (bot/fraud).
* **Tài chính & Ngân hàng:** Giao dịch thẻ tín dụng bất thường hoặc biến động giá cổ phiếu đột ngột giúp phát hiện gian lận và cảnh báo rủi ro.

---

> **Kết luận:** Chìa khóa của phát hiện bất thường nằm ở việc **hiểu rõ ngữ cảnh và bản chất của dữ liệu**. Xác định đúng loại ngoại lệ giúp đưa ra phương pháp phân tích và ứng dụng hiệu quả trong từng bài toán thực tế.
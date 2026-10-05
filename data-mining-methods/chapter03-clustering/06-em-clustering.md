Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Thuật toán Tối đa hóa Kỳ vọng (Expectation-Maximization - EM Algorithm)** trong Phân cụm Xác suất:

---

### 1. Tổng quan về Thuật toán EM (Expectation-Maximization)

* **Mô hình Hỗn hợp:** EM thường kết hợp với **Mô hình Hỗn hợp Gaussian (GMM)**, đại diện cho mỗi cụm bằng một phân phối xác suất được đặc trưng bởi hai tham số: **Trung bình ($\mu$)** và **Độ lệch chuẩn ($\sigma$)**.
* **Phân cụm Mờ (Soft Membership):** Mỗi điểm dữ liệu sở hữu một xác suất thuộc về từng cụm riêng biệt, thay vì bị ép buộc thuộc về một cụm cố định.

---

### 2. Hai bước Lặp của Thuật toán EM

1. **Bước E (Expectation - Kỳ vọng):**
* Tính toán xác suất thành viên (membership probability) mà mỗi điểm dữ liệu thuộc về từng cụm dựa trên các tham số mô hình hiện tại.
* Chuẩn hóa các xác suất này để tổng xác suất của một điểm trên tất cả các cụm bằng $1$.


2. **Bước M (Maximization - Tối đa hóa):**
* Cập nhật lại các tham số cụm ($\mu$ và $\sigma$) bằng cách sử dụng tổng trung bình có trọng số của các điểm dữ liệu, trong đó trọng số chính là xác suất thuộc về cụm tính được ở **Bước E**.



---

### 3. Ưu điểm & Hạn chế

* **Ưu điểm:**
* Tốc độ hội tụ nhanh và dễ triển khai tính toán nhờ các công thức cập nhật tham số dạng đóng (closed-form updates).
* Biểu diễn xuất sắc các cụm dữ liệu nằm đè lên nhau (overlapping clusters) hoặc có hình dạng phân phối phức tạp.


* **Hạn chế:**
* Đòi hỏi kích thước tập dữ liệu đủ lớn để ước lượng chính xác các thông số phân phối.
* Chi phí tính toán tăng đáng kể khi số lượng cụm hoặc số chiều dữ liệu tăng cao.



---

### 4. So sánh với Thuật toán K-Means

| Đặc tính | Thuật toán K-Means | Thuật toán EM (Expectation-Maximization) |
| --- | --- | --- |
| **Cơ chế gán** | **Hard Assignment:** Gán cố định $1$ điểm vào $1$ cụm duy nhất. | **Soft Assignment:** Gán xác suất thuộc về từng cụm cho mỗi điểm. |
| **Tham số cụm** | Chỉ cập nhật **Tâm cụm (Centroid)**. | Cập nhật cả **Trung bình ($\mu$)** và **Độ lệch chuẩn ($\sigma$)** (hình dạng & quy mô cụm). |
| **Khả năng phân tách** | Phù hợp với các cụm hình cầu, tách biệt rõ ràng. | Bắt tốt các cụm chồng lấp và phân tách ranh giới phức tạp/mờ. |

---

> **Kết luận:** EM là một thuật toán lặp cực kỳ hiệu quả, đóng vai trò nền tảng trong các bài toán phân tích dữ liệu thực tế — nơi dữ liệu thường không có ranh giới phân tách cứng mà mang tính xác suất ngẫu nhiên.
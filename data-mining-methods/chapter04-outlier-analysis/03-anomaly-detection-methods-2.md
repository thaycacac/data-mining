Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Các Phương pháp Phát hiện Ngoại lệ Chuyên sâu (Proximity, Density, Semi-Supervised, Contextual & Collective Anomalies)**:

---

### 1. Phát hiện Ngoại lệ Dựa trên Khoảng cách & Mật độ (Proximity & Density-Based)

* **Dựa trên Khoảng cách Tuyệt đối (Absolute Proximity):**
* Đo khoảng cách trực tiếp từ điểm dữ liệu tới các điểm hàng xóm gần nhất (k-NN distance).
* Đặt một ngưỡng (threshold) khoảng cách cố định: Điểm nằm quá xa các hàng xóm xung quanh sẽ bị coi là ngoại lệ.


* **Dựa trên Mật độ (Density-Based Methods):**
* Đo mật độ điểm dữ liệu trong vùng lân cận (ví dụ: thuật toán LOF - Local Outlier Factor).
* Phân biệt rõ ràng giữa các điểm cô lập nằm ở vùng **mật độ thưa thớt** (ngoại lệ) với các điểm nằm trong vùng **mật độ dày đặc** (cụm dữ liệu bình thường).



---

### 2. Phát hiện Bất thường Bán giám sát (Semi-Supervised Anomaly Detection)

* **Cơ chế:** Kết hợp sức mạnh của **Phân cụm (Học không giám sát)** và một lượng nhỏ **Nhãn dữ liệu (Học có giám sát)**.
* **Quy trình:**
1. Gom nhóm toàn bộ dữ liệu thành các cụm tự nhiên.
2. Sử dụng các điểm dữ liệu đã gắn nhãn (Bình thường hoặc Bất thường) để gán nhãn/định nghĩa bản chất cho toàn bộ cụm chứa chúng.
3. Từ đó phân loại chính xác các điểm dữ liệu chưa gắn nhãn còn lại, giúp tối ưu hiệu năng và chi phí gán nhãn.



---

### 3. Phương pháp Xử lý Ngoại lệ Ngữ cảnh & Ngoại lệ Tập hợp

* **Ngoại lệ Ngữ cảnh (Contextual Anomalies):**
* Phụ thuộc vào các thuộc tính ngữ cảnh (như thời gian, vị trí địa lý, nhiệt độ môi trường).
* *Cách phát hiện:* Phải xác định đúng khung ngữ cảnh liên quan, sau đó chia nhỏ dữ liệu và thực hiện phát hiện bất thường **bên trong từng tập con ngữ cảnh đó**.


* **Ngoại lệ Tập hợp (Collective Anomalies):**
* Liên quan đến một nhóm các đối tượng có mối quan hệ với nhau cùng lệch khỏi quỹ đạo bình thường (mặc dù xét riêng lẻ từng điểm thì không hề bất thường).
* *Cách phát hiện:* Gom nhóm các đối tượng liên quan thành một **"siêu đối tượng" (super object)** hoặc chuỗi/mạng lưới, sau đó phân tích hành vi tổng thể của tập hợp đó.



---

> **Kết luận:** Việc phân loại đúng bản chất bất thường (dựa trên khoảng cách, mật độ, ngữ cảnh hay tập hợp) giúp lựa chọn đúng kỹ thuật xử lý — từ đơn giản như lọc khoảng cách k-NN đến phức tạp như gộp siêu đối tượng hay kết hợp bán giám sát.
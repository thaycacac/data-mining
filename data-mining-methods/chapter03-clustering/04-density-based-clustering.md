Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Phương pháp Phân cụm Dựa trên Mật độ (Density-Based Clustering: DBSCAN & DENCLUE)**:

---

### 1. Khái niệm Cốt lõi về Phân cụm Dựa trên Mật độ

* **Định nghĩa Mật độ Cục bộ (Local Density):** Mật độ được xác định trong phạm vi lân cận cục bộ (bằng số lượng đối tượng nằm trong một vùng không gian), thay vì đo lường khoảng cách toàn cục (global distance) đến tâm cụm.
* **Cơ chế Phát triển Cụm:** Cụm được hình thành bằng cách mở rộng liên tục các vùng lân cận đạt độ dày mật độ trên một ngưỡng chỉ định. Điều này cho phép thuật toán **tự do tìm ra các cụm có hình dạng bất kỳ (arbitrary shapes)**.

---

### 2. Thuật toán DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

Sử dụng $2$ tham số đầu vào cốt lõi: $\epsilon$ (Bán kính lân cận - Epsilon) và $MinPts$ (Số điểm tối thiểu để đạt ngưỡng mật độ).

* **Phân loại $3$ loại Điểm Dữ liệu:**
1. **Core Points (Điểm lõi):** Có ít nhất $MinPts$ điểm dữ liệu nằm trong bán kính $\epsilon$.
2. **Border Points (Điểm biên):** Không đủ $MinPts$ trong bán kính $\epsilon$, nhưng nằm trong bán kính $\epsilon$ của một điểm Core Point.
3. **Noise Points (Nhiễu / Outliers):** Không phải Core Point cũng không phải Border Point (các điểm cô lập).


* **Cơ chế Gom cụm:** Cụm liên tục phát triển bằng cách kết nối các điểm lõi (Core Points) và điểm biên (Border Points) đạt điều kiện "có thể truy cập mật độ" (density-reachable) cho đến khi chạm đến ranh giới mật độ thấp.

---

### 3. Phương pháp DENCLUE (DENsity-based CLUstEring)

* **Hàm Mật độ Chính thức (Formal Density Function):** Áp dụng các hàm ảnh hưởng (inference functions / kernel functions) gán cho từng đối tượng dữ liệu.
* **Mật độ Hấp dẫn (Density Attractors):** Tích hợp ảnh hưởng từ nhiều đối tượng xung quanh để xác định các đỉnh mật độ (local maxima) đóng vai trò là tâm hấp dẫn của cụm.
* **Tính Linh hoạt:** Cho phép tùy biến các hàm ảnh hưởng dựa trên khoảng cách và hướng.

---

### 4. Ưu điểm Vượt trội của Phân cụm Dựa trên Mật độ

* **Bắt được Cụm Hình dạng Bất kỳ:** Khắc phục triệt để hạn chế của K-Means (vốn chỉ tìm được cụm hình cầu/hình lồi).
* **Khả năng Chống Nhiễu Tuyệt vời:** Tự động phát hiện và loại bỏ các điểm nhiễu cô lập mà không làm sai lệch ranh giới cụm.
* **Tối ưu Tính toán:** Thường chỉ cần **một lượt quét dữ liệu duy nhất (single scan)** để hình thành cụm, mang lại hiệu năng cao.

---

> **Kết luận:** Phương pháp dựa trên mật độ là giải pháp lý tưởng cho dữ liệu không gian (spatial data) có chứa nhiều nhiễu và cấu trúc cụm hình học phức tạp. Đây là mảnh ghép hoàn chỉnh bên cạnh các nhóm phân cụm Partitioning, Hierarchical, Grid-based và Probabilistic.
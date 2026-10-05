Dưới đây là tóm tắt các điểm cốt lõi của bài học về **So sánh K-Medoids vs. K-Means, Phân cụm Phân cấp (Hierarchical) & Phân cụm Dựa trên Lưới (Grid-Based)**:

---

### 1. Phương pháp Phân chia: K-Medoids vs. K-Means

* **K-Medoids (PAM - Partitioning Around Medoids):**
* *Nguyên lý:* Lựa chọn một **đối tượng dữ liệu thực tế** làm tâm cụm (medoid) để tối thiểu hóa tổng khoảng cách tới các điểm còn lại trong cụm, thay vì dùng giá trị trung bình đại diện (centroid) như K-Means.
* *Ưu điểm:* **Ít bị ảnh hưởng bởi nhiễu và giá trị ngoại lệ (outliers)** hơn so với K-Means.
* *Hạn chế:* Chi phí tính toán cao hơn hẳn K-Means do phải thử nghiệm và đánh giá tất cả các điểm dữ liệu làm medoid tiềm năng $\rightarrow$ Kém khả năng mở rộng (scalability). Kỹ thuật lấy mẫu ngẫu nhiên (như CLARA) thường được dùng để tăng hiệu năng.



---

### 2. Phân cụm Phân cấp (Hierarchical Clustering)

* **Nguyên lý:** Xây dựng cấu trúc cụm đa tầng dưới dạng sơ đồ hình cây (**Dendrogram**), cho phép khám phá dữ liệu ở nhiều mức độ chi tiết khác nhau:
* **Agglomerative (Gom cụm từ dưới lên):** Bắt đầu bằng việc coi mỗi điểm là $1$ cụm riêng lẻ, sau đó liên tục gộp các cụm gần nhất lại với nhau.
* **Divisive (Chia nhỏ từ trên xuống):** Bắt đầu bằng việc coi toàn bộ dữ liệu là $1$ cụm duy nhất, sau đó liên tục chia tách thành các cụm nhỏ hơn.


* **Đặc trưng cốt lõi:**
* Kết quả phụ thuộc vào cách định nghĩa khoảng cách giữa các cụm (Min/Single Link, Max/Complete Link, Average Link).
* **Không thể đảo ngược quyết định:** Một khi hai cụm đã gộp hoặc tách, quyết định đó không thể thay đổi ở các bước sau (khác với tính lặp cập nhật liên tục của phương pháp phân chia).



---

### 3. Phân cụm Dựa trên Lưới (Grid-Based Clustering)

* **Nguyên lý:** Chia không gian dữ liệu thành vô số ô lưới (grid cells) ở các độ phân giải khác nhau. Các ô lưới có mật độ điểm cao và nằm liền kề nhau sẽ được nhóm lại thành một cụm $\rightarrow$ Ranh giới của cụm sẽ bám theo mép của các ô lưới.
* **Ưu điểm vượt trội:**
* **Tốc độ cực nhanh & Dễ song song hóa:** Độ phức tạp tính toán phụ thuộc vào **số lượng ô lưới**, hoàn toàn độc lập với số lượng điểm dữ liệu ($n$).
* **Hỗ trợ cập nhật tăng dần (Incremental updates):** Dễ dàng duy trì và cập nhật thống kê dữ liệu bên trong từng ô khi có dữ liệu mới.



---

> **Kết luận:** Mỗi phương pháp giải quyết một bài toán cụ thể: **K-Medoids** tối ưu chống nhiễu; **Hierarchical** trực quan hóa mối quan hệ đa tầng qua Dendrogram; còn **Grid-Based** là lựa chọn số một khi cần xử lý dữ liệu quy mô khổng lồ với tốc độ cao.
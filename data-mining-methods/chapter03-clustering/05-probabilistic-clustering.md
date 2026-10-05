Dưới đây là tóm tắt các điểm cốt lõi của bài học mở đầu về **Phân cụm Xác suất & Mô hình Hỗn hợp (Probabilistic Clustering & Mixture Models)**:

---

### 1. Khái niệm Phân cụm Xác suất (Probabilistic Clustering)

* **Khác biệt với Phân cụm Truyền thống (Hard Clustering):**
* *Hard Clustering (như K-Means):* Gán cứng mỗi đối tượng dữ liệu vào duy nhất một cụm cố định.
* *Probabilistic Clustering (Soft / Fuzzy Clustering):* Gán cho mỗi đối tượng một **xác suất thuộc về (membership probability)** đối với tất cả các cụm.


* **Ý nghĩa:** Phản ánh đúng bản chất "mờ" (fuzziness) của dữ liệu thực tế — nơi một đối tượng có thể mang đặc tính chung của nhiều nhóm khác nhau.

---

### 2. Mô hình Hỗn hợp & Cụm Ẩn (Mixture Models & Hidden Clusters)

* **Phân phối Xác suất:** Mỗi cụm được đại diện bởi một phân phối xác suất toán học (thường là phân phối Chuẩn/Gaussian).
* **Cụm ẩn (Latent / Hidden Variables):** Các cụm được xem là những nhóm ẩn tạo ra dữ liệu quan sát được.
* **Phân phối Tổng thể (Overall Distribution):** Toàn bộ tập dữ liệu được coi là một **mô hình hỗn hợp (mixture model)** kết hợp từ các phân phối thành phần của từng cụm.

---

### 3. Phân cụm Dựa trên Mô hình & Mức độ Khả tóm (Model-Based Clustering & Likelihood)

* **Mục tiêu Tối ưu:** Tìm tập tham số cho mô hình hỗn hợp sao cho **tối đa hóa hàm khả tóm (Maximize Likelihood)** của tập dữ liệu quan sát được.
* **Cơ chế:** Tính xác suất gộp của toàn bộ tập dữ liệu được sinh ra bởi mô hình hỗn hợp, sau đó liên tục điều chỉnh các tham số phân phối (như trung bình $\mu$, độ lệch chuẩn $\sigma$) để khớp nhất với dữ liệu thực tế.

---

### 4. Mối liên hệ với Thuật toán K-Means

* **K-Means:** Là trường hợp đặc biệt (hard assignment) dựa trên khoảng cách hình học tới tâm cụm (centroid) gần nhất.
* **Probabilistic Clustering:** Là dạng **tổng quát hóa của K-Means** — thay vì gán cứng dựa vào khoảng cách, thuật toán tính xác suất trọng số gộp và cập nhật tham số cụm dựa trên các xác suất thành viên này.

---

> **Kết luận:** Phân cụm xác suất đặt nền móng lý thuyết cho các thuật toán học không giám sát nâng cao như **Mô hình Hỗn hợp Gaussian (GMM)** và thuật toán **Tối đa hóa Kỳ vọng (Expectation-Maximization - EM)**.
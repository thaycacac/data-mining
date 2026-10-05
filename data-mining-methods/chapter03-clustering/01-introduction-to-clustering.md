Dưới đây là tóm tắt các điểm cốt lõi của bài học tổng quan về **Mục đích, Các Phương pháp & Tiêu chí Đánh giá Phân cụm Dữ liệu (Clustering Concepts, Methods & Evaluation)**:

---

### 1. Khái niệm Cốt lõi về Phân cụm (Clustering Concepts)

* **Học không giám sát (Unsupervised Learning):** Gom nhóm các đối tượng dữ liệu mà **không có sẵn nhãn lớp** định trước.
* **Mục tiêu nguyên bản:**
* **Tối đa hóa độ tương đồng trong cùng một cụm (Intra-cluster similarity / Cohesion):** Các đối tượng trong cùng cụm càng giống nhau càng tốt.
* **Tối thiểu hóa độ tương đồng giữa các cụm khác nhau (Inter-cluster separation):** Các cụm khác nhau càng tách biệt càng tốt.


* **Độ đo (Distance / Similarity Measures):** Dựa trên các hàm khoảng cách (như Euclidean, Manhattan, Cosine) được tính toán từ các thuộc tính của đối tượng.

---

### 2. Các Phương pháp Phân cụm Chính (Clustering Methods)

1. **Phương pháp Phân chia (Partitioning Methods):** Chia trực tiếp tập dữ liệu thành $k$ cụm phân biệt (ví dụ: *K-Means, K-Medoids*).
2. **Phương pháp Phân cấp (Hierarchical Methods):** Xây dựng cây phân cụm đa tầng theo cơ chế gom cụm từ dưới lên (Agglomerative) hoặc chia nhỏ từ trên xuống (Divisive).
3. **Phương pháp Dựa trên Mật độ (Density-based Methods):** Phát hiện các cụm có hình dạng bất kỳ dựa trên mật độ điểm dữ liệu dày đặc, đồng thời tự động loại bỏ nhiễu (ví dụ: *DBSCAN, OPTICS*).
4. **Phương pháp Dựa trên Lưới (Grid-based Methods):** Chia không gian dữ liệu thành các ô lưới (cells) và thực hiện phân cụm dựa trên mật độ điểm nằm trong từng ô.
5. **Phương pháp Xác suất (Probabilistic Methods):** Gán xác suất thành viên cho từng điểm để xử lý độ không chắc chắn và mờ của dữ liệu (ví dụ: *GMM / EM*).

---

### 3. Đánh giá Chất lượng Cụm (Clustering Evaluation)

* **Xác định Tính khuynh hướng (Clustering Tendency):** Kiểm tra xem tập dữ liệu thực sự có cấu trúc cụm tự nhiên hay chỉ là dữ liệu ngẫu nhiên phân bố đồng đều (ví dụ: dùng chỉ số *Hopkins Statistic*).
* **Độ gắn kết & Độ phân tách:**
* **Cohesion:** Đo khoảng cách nội bộ giữa các điểm trong cùng cụm.
* **Separation:** Đo khoảng cách ranh giới giữa các cụm khác nhau.


* **Hệ số Dáng điệu (Silhouette Coefficient):**
* Chỉ số đánh giá tổng hợp so sánh giữa khoảng cách nội cụm trung bình ($a$) và khoảng cách tới cụm gần nhất ($b$).
* Giá trị biến thiên từ $-1$ đến $+1$: Điểm gần $+1$ thể hiện điểm dữ liệu được gán cụm rất chính xác và tách biệt.


* **Tri thức Miền (Domain Knowledge):** Kết hợp chuyên môn thực tế để tinh chỉnh số lượng cụm $k$ phù hợp và chọn ra mô hình tối ưu nhất.

---

> **Kết luận:** Phân cụm không chỉ dừng lại ở việc chạy thuật toán gom nhóm mà đòi hỏi một quy trình toàn diện: từ kiểm tra tính chất dữ liệu, lựa chọn phương pháp phân cụm phù hợp, đến việc đánh giá định lượng (Silhouette) và định tính (Domain Knowledge).
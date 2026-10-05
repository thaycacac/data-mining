Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Phương pháp Phân chia & Thuật toán Phân cụm K-Means (Partitioning Methods & K-Means Clustering)**:

---

### 1. Tổng quan về Phương pháp Phân chia (Partitioning Methods)

* **Khái niệm:** Chia tập dữ liệu gồm $n$ đối tượng thành $K$ cụm phân biệt (với $K$ được chỉ định trước).
* **Động lực sử dụng Thuật toán Giải pháp Bán tối ưu (Heuristic):** Việc duyệt toàn bộ các phương án phân chia (Brute-force) để tìm kết quả tối ưu tuyệt đối là không thể thực thi về mặt tính toán khi tập dữ liệu lớn. Do đó, các thuật toán heuristic như K-Means được áp dụng để tìm lời giải đủ tốt với chi phí hợp lý.

---

### 2. Quy trình Hoạt động của Thuật toán K-Means

1. **Khởi tạo:** Chọn ngẫu nhiên $K$ điểm dữ liệu làm **Tâm cụm ban đầu (Initial Centroids)**.
2. **Gán cụm (Assignment):** Gán mỗi điểm dữ liệu vào cụm có tâm gần nhất (thường đo bằng khoảng cách Euclidean).
3. **Cập nhật tâm (Update Centroids):** Tính lại vị trí tâm cụm mới bằng cách lấy trung bình cộng tọa độ của tất cả các điểm thuộc cụm đó.
4. **Lặp lại:** Lặp lại bước 2 và 3 cho đến khi các tâm cụm không còn thay đổi vị trí (hội tụ) hoặc đạt số vòng lặp tối đa.

> **Độ phức tạp tính toán:** $\mathcal{O}(n \cdot k \cdot t)$
> *(Trong đó $n$ là số điểm dữ liệu, $k$ là số cụm, và $t$ là số vòng lặp)*.

---

### 3. Đặc trưng Cốt lõi & Các Lưu ý Quan trọng

* **Yêu cầu đầu vào:** Phải xác định trước số lượng cụm $K$.
* **Kiểu dữ liệu:** Phù hợp nhất với **dữ liệu số (numerical data)** — nơi phép tính trung bình cộng (mean) để xác định tâm cụm có ý nghĩa toán học.
* **Độ nhạy với Khởi tạo:** Việc chọn tâm cụm ban đầu ảnh hưởng trực tiếp đến kết quả cuối cùng; chọn khởi tạo kém dễ dẫn đến nghiệm tối ưu cục bộ (local optima).
* **Hình dạng Cụm:** K-Means xu hướng tìm các **cụm hình lồi/hình cầu (convex-shaped clusters)** và hoạt động rất kém trên các tập dữ liệu có cấu trúc cụm hình dạng phức tạp/không lồi (như hình vành khăn, vòng tròn lồng nhau).
* **Độ nhạy với Nhiễu & Outliers:** Các giá trị ngoại lệ (outliers) có thể làm lệch đáng kể vị trí trung bình của tâm cụm, kéo theo việc gán cụm sai lệch cho nhiều điểm khác.

---

> **Bài học cốt lõi:** K-Means là thuật toán phân cụm phân chia kinh điển, nhanh và hiệu quả trên dữ liệu số đơn giản. Tuy nhiên, rủi ro rơi vào cực trị cục bộ, độ nhạy với nhiễu và hạn chế với cụm không có hình cầu là những điểm yếu cần khắc phục bằng các kỹ thuật như **K-Means++** hay các phương pháp phân cụm khác (DBSCAN, Hierarchical).
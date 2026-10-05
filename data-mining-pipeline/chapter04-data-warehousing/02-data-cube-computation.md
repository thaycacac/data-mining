Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Tính toán và Tối ưu hóa Khối Dữ liệu Đa chiều (Data Cube Computation & Materialization)** trong Kho dữ liệu:

---

### 1. Khái niệm Khối Dữ liệu (Data Cube) & Cuboids

* **Khối Dữ liệu (Data Cube):** Lưu trữ và tổ chức dữ liệu theo nhiều chiều phân tích (như Thời gian, Sản phẩm, Địa điểm, Nhà cung cấp).
* **Cuboid:** Biểu diễn dữ liệu ở các cấp độ tổng hợp (aggregation) khác nhau bằng cách kết hợp các tập hợp chiều khác nhau.
* *Base Cuboid:* Cấp độ dữ liệu chi tiết nhất (chứa đầy đủ tất cả các chiều).
* *Apex Cuboid:* Cấp độ tổng hợp cao nhất (chỉ chứa $1$ giá trị tổng quan cho toàn bộ dữ liệu - `ALL`).
* Tập hợp tất cả các cuboid tạo thành một **cấu trúc lưới (Lattice of Cuboids)** cho phép truy vấn dữ liệu linh hoạt.



---

### 2. Các Tiếp cận Lưu trữ / Hiện thực hóa Khối Dữ liệu (Data Cube Materialization)

* **Hiện thực hóa Toàn bộ (Full Materialization):**
* *Cách làm:* Tính toán trước và lưu lại tất cả các cuboid có thể có.
* *Ưu/Nhược điểm:* Truy vấn cực kỳ nhanh, nhưng tiêu tốn bộ nhớ lưu trữ khổng lồ và chi phí tính toán ban đầu rất cao.


* **Không tính toán trước (No Materialization):**
* *Cách làm:* Chỉ lưu trữ *Base Cuboid*, tính toán các phép tổng hợp trực tiếp khi có truy vấn (on-demand).
* *Ưu/Nhược điểm:* Tiết kiệm không gian lưu trữ, nhưng tốc độ phản hồi truy vấn rất chậm đối với tập dữ liệu lớn.


* **Hiện thực hóa Một phần (Partial Materialization):**
* *Cách làm:* Chỉ tính toán và lưu trữ trước một tập hợp các cuboid quan trọng nhất dựa trên tần suất truy vấn hoặc các giải thuật chọn lọc (heuristics).
* *Ưu/Nhược điểm:* Giải pháp cân bằng tối ưu giữa **hiệu năng truy vấn** và **dung lượng lưu trữ**.



---

### 3. Khối Dữ liệu Băng trôi (Iceberg Cubes) & Kỹ thuật Tối ưu Tính toán

Khi số lượng chiều tăng lên, số lượng cuboid tăng theo cấp số nhân ($2^N$). Các kỹ thuật sau giúp giảm đáng kể chi phí tính toán:

* **Iceberg Cubes:** Chỉ tính toán và lưu giữ các nhóm tổng hợp vượt qua một **ngưỡng giá trị tối thiểu (threshold)** nhất định (ví dụ: chỉ giữ lại các cụm có tổng doanh số $\ge 10.000\$$), bỏ qua phần dữ liệu nhỏ nhặt bên dưới.
* **Multiway Array Aggregation:** Duyệt dữ liệu theo mảng đa chiều và tính toán đồng thời nhiều phép tổng hợp trong **$1$ lần quét dữ liệu duy nhất** (single scan).
* **Bottom-up Computation (BUC):** Tính toán từ cấp tổng hợp cao nhất xuống dần chi tiết, kết hợp thuật toán **cắt tỉa (pruning)** để dừng ngay nhánh tính toán nếu giá trị tổng hợp không đạt ngưỡngthreshold.
* **Star-Cubing:** Kết hợp ưu điểm của cả hai hướng tiếp cận *Top-down* và *Bottom-up*, sử dụng cấu trúc cây (*Star-tree*) để chia sẻ kết quả tính toán chung và cắt tỉa sớm các không gian tính toán dư thừa.

---

> **Kết luận:** Lựa chọn chiến lược hiện thực hóa (*Materialization*) và thuật toán tính toán khối phù hợp giúp hệ thống OLAP duy trì tốc độ truy vấn tức thì trên các tập dữ liệu lịch sử cực lớn mà không làm bùng nổ dung lượng lưu trữ.
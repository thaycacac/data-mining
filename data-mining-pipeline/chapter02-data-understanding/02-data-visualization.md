Dưới đây là tóm tắt các điểm quan trọng của bài học về **Trực quan hóa Dữ liệu (Data Visualization)** trong việc phân tích phân phối và mối quan hệ giữa các dữ liệu:

---

### 1. Sơ đồ hộp (Boxplots)

* **Cấu trúc:** Sử dụng hình hộp để biểu diễn 50% dữ liệu ở giữa, giới hạn bởi các tứ phân vị $Q_1$ (25%) và $Q_3$ (75%), chiều dài hộp chính là khoảng tứ phân vị $\text{IQR} = Q_3 - Q_1$. Đường vạch bên trong hộp biểu thị trung vị ($Q_2$).
* **Râu sơ đồ (Whiskers) & Ngoại lệ (Outliers):** Hai đường "râu" kéo dài biểu thị giá trị nhỏ nhất và lớn nhất trong khoảng chấp nhận được. Các điểm nằm ngoài khoảng $1.5 \times \text{IQR}$ được coi là **giá trị ngoại lệ (outliers)** và hiển thị dưới dạng các điểm riêng biệt.

---

### 2. Biểu đồ tần số (Histograms) & Biểu đồ phân vị (Quantile Plots)

* **Histogram:** Chia dữ liệu thành các khoảng cố định (bins) và đếm tần suất xuất hiện, thích hợp quan sát hình dạng phân phối tổng thể (như nhóm tuổi, lưu lượng truy cập).
* **Quantile Plot & Q-Q Plot:**
* *Quantile Plot:* Hiển thị bách phân vị của dữ liệu để so sánh giữa các danh mục.
* *Q-Q Plot (Quantile-Quantile Plot):* So sánh hai tập phân phối bằng cách vẽ các điểm phân vị tương ứng của chúng để đánh giá mức độ tương đồng về mặt phân phối.



---

### 3. Biểu đồ tán xạ (Scatter Plots) & Trực quan hóa Nâng cao

* **Scatter Plot:** Biểu diễn hai thuộc tính trên trục tọa độ để phát hiện mối tương quan (thuận, nghịch hoặc không tương quan); ma trận biểu đồ tán xạ (Scatter Plot Matrix) giúp so sánh nhiều cặp thuộc tính cùng lúc.
* **Các dạng biểu đồ khác:** Line charts (biểu đồ đường), Pie charts (tròn), Heatmaps (biểu đồ nhiệt), Word clouds (đám mây từ ngữ), Network graphs (đồ thị mạng) — kết hợp màu sắc, kích thước và bố cục để gia tăng lượng thông tin truyền tải.

---

### 4. Mục đích & Kỹ thuật Trực quan hóa

* **Hai mục đích chính:**
1. *Khám phá (Exploration):* Tìm kiếm các mẫu, xu hướng hoặc điểm bất thường chưa biết trước.
2. *Diễn giải (Explanation):* Truyền tải và trình bày các tri thức đã tìm thấy một cách hiệu quả cho người khác.


* **Tự động hóa & Tương tác:** Sử dụng tính năng tương tác (zoom, lọc, hover) và tự động hóa giúp nâng cao hiệu suất phân tích, đạt sự cân bằng giữa tính đơn giản và sự phức tạp của dữ liệu.
Dưới đây là tóm tắt các điểm quan trọng của bài học về **Độ tương đồng & Độ khác biệt của Dữ liệu (Data Similarity and Dissimilarity)**:

---

### 1. Biểu diễn Dữ liệu & Ma trận Độ tương đồng

* **Ma trận Dữ liệu ($n \times p$):** Tập dữ liệu gồm $n$ đối tượng (hàng) và $p$ thuộc tính (cột).
* **Ma trận Độ tương đồng / Khác biệt ($n \times n$):** Mỗi ô thể hiện khoảng cách hoặc độ giống/khác nhau giữa từng cặp đối tượng. Đây là cơ sở quan trọng cho các thuật toán như gom cụm (clustering) hay tìm kiếm láng giềng gần nhất (k-NN).

---

### 2. Đo lường theo loại Thuộc tính (Attribute Types)

* **Thuộc tính Định danh (Nominal):** So sánh theo kiểu nhị phân đơn giản — giống nhau (độ tương đồng = 1) hoặc khác nhau (độ tương đồng = 0). Cũng có thể thiết lập thang đo độ tương đồng tùy chỉnh cho các trường hợp đặc biệt (ví dụ: mức độ tương đồng giữa các màu sắc).
* **Thuộc tính Nhị phân (Binary):** Giá trị dạng Có/Không (1/0). Việc tính toán phụ thuộc vào tính chất đối xứng của thuộc tính.

---

### 3. Thuộc tính Nhị phân Đối xứng vs. Bất đối xứng

* **Thuộc tính Nhị phân Đối xứng (Symmetric Binary):**
* Hai giá trị $0$ và $1$ có vai trò và khả năng xuất hiện ngang nhau (ví dụ: Giới tính Nam/Nữ).
* Công thức tính toán tính cả trường hợp hai đối tượng cùng mang giá trị $0$.


* **Thuộc tính Nhị phân Bất đối xứng (Asymmetric Binary):**
* Hai giá trị có tầm quan trọng khác nhau, thường sự xuất hiện ($1$) quan trọng hơn sự không xuất hiện ($0$) (ví dụ: mua hàng, triệu chứng bệnh).
* Bỏ qua các trường hợp cả hai đối tượng đều bằng $0$ (null cases) vì chúng không mang nhiều ý nghĩa.
* **Hệ số Jaccard (Jaccard Coefficient):** Là chỉ số tiêu chuẩn dùng cho thuộc tính bất đối xứng, chỉ tập trung đo lường tỷ lệ trùng khớp của các trường hợp $1$ (sự kiện tích cực cùng xảy ra).



---

> **Bài học cốt lõi:** Cần xác định chính xác kiểu thuộc tính để lựa chọn công thức đo độ tương đồng/khác biệt phù hợp, từ đó phản ánh đúng bản chất mối quan hệ giữa các đối tượng trong dữ liệu.
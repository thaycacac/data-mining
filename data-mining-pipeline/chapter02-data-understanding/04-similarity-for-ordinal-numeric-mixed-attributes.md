Dưới đây là tóm tắt các điểm quan trọng của bài học về **Đo lường Độ tương đồng và Độ khác biệt cho các Kiểu Dữ liệu Nâng cao (Measuring Similarity and Dissimilarity)**:

---

### 1. Thuộc tính Thứ bậc (Ordinal Attributes)

* **Đặc điểm:** Có tập giá trị hữu hạn và có thứ tự rõ ràng (ví dụ: Huy chương Vàng, Bạc, Đồng; Trình độ Học vấn).
* **Cách tính độ khác biệt:**
1. Chuyển đổi các giá trị theo thứ tự thành thứ hạng (ranks: $1, 2, \dots, M$).
2. Chuẩn hóa các thứ hạng về khoảng từ $0$ đến $1$ bằng công thức: $z = \frac{rank - 1}{M - 1}$.
3. Độ khác biệt giữa hai giá trị chính là khoảng cách tuyệt đối giữa các giá trị đã chuẩn hóa.



---

### 2. Độ khác biệt cho Thuộc tính Số (Numeric Attributes)

Sử dụng các khoảng cách thuộc họ **Khoảng cách Minkowski ($L_p$ norm)**:

* **Khoảng cách Manhattan ($p = 1$):** Tổng khoảng cách theo từng chiều tọa độ ($\sum \vert{}x_i - y_i\vert{}$).
* **Khoảng cách Euclidean ($p = 2$):** Khoảng cách đường thẳng theo hình học chuẩn ($\sqrt{\sum (x_i - y_i)^2}$).

**4 Tính chất cơ bản của Hàm Khoảng cách (Distance Metrics):**

* *Tự so sánh bằng 0:* $d(x, x) = 0$.
* *Tính không âm:* $d(x, y) \ge 0$.
* *Tính đối xứng:* $d(x, y) = d(y, x)$ (tuy nhiên vẫn có một số ngoại lệ trong thực tế).
* *Bất đẳng thức tam giác:* $d(x, z) \le d(x, y) + d(y, z)$.

---

### 3. Độ tương đồng Cosine cho Dữ liệu Văn bản (Cosine Similarity)

* Văn bản được biểu diễn dưới dạng các vectơ cao chiều dựa trên số lần xuất hiện của từ khóa.
* **Cosine Similarity:** Đo góc giữa hai vectơ thay vì khoảng cách độ dài. Kỹ thuật này cực kỳ hiệu quả cho dữ liệu văn bản có độ thưa lớn (sparse data) và số chiều cao.

---

### 4. Độ tương đồng cho Chuỗi thời gian (Sequential / Time Series Data)

* **Khoảng cách Euclidean:** So sánh từng điểm dữ liệu trùng khớp về mặt thời gian (đồng bộ).
* **Dynamic Time Warping (DTW):** Uốn nắn/căn chỉnh chuỗi thời gian để tìm các hình dạng (shapes) tương đồng ngay cả khi các điểm thời gian không khớp chính xác hoặc có độ trễ/lệch pha.

---

### 5. Dữ liệu hỗn hợp nhiều Kiểu thuộc tính (Mixed Attribute Types)

* Tập dữ liệu thực tế thường kết hợp cả Định danh, Nhị phân, Số và Thứ bậc.
* Độ tương đồng/khác biệt tổng thể được tính bằng **trung bình có trọng số (weighted sum)** các khoảng cách thành phần của từng thuộc tính. Trọng số có thể điều chỉnh tùy thuộc vào mức độ quan trọng của từng thuộc tính.
Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Hiểu dữ liệu: Đối tượng, Thuộc tính và Thống kê cơ bản (Data Understanding)**:

---

### 1. Đối tượng Dữ liệu & Thuộc tính (Data Objects & Attributes)

* **Đối tượng dữ liệu (Data Objects):** Là các thực thể đại diện cho tập dữ liệu (ví dụ: nhân viên, sản phẩm, bài đăng mạng xã hội). Cũng được gọi là mẫu (sample), bản ghi (record), hoặc điểm dữ liệu (data point).
* **Thuộc tính (Attributes):** Các đặc trưng mô tả đối tượng (còn gọi là feature, variable, dimension). Gồm 2 nhóm chính:
* **Phân loại / Định tính (Categorical / Qualitative):**
* *Nominal (Định danh):* Không có thứ tự (ví dụ: màu sắc, giới tính).
* *Binary (Nhị phân):* Chỉ có 2 giá trị (ví dụ: 0/1, True/False).
* *Ordinal (Thứ bậc):* Có thứ tự rõ ràng (ví dụ: Xếp loại học lực: Trung bình < Khá < Giỏi).


* **Số học / Định lượng (Numerical / Quantitative):**
* *Interval-scaled (Khoảng cách):* Không có điểm `0` tuyệt đối (ví dụ: nhiệt độ $0^\circ\text{C}$).
* *Ratio-scaled (Tỷ lệ):* Có điểm `0` tuyệt đối đại diện cho "không có gì" (ví dụ: thu nhập, khoảng cách, chiều cao).





---

### 2. Mô tả Thống kê Dữ liệu (Statistical Characterization)

* **Kích thước tập dữ liệu:** Được xác định bởi số lượng đối tượng ($N$) và số lượng thuộc tính ($D$).
* **Thuộc tính phân loại:** Tóm tắt bằng tần số xuất hiện (frequency counts) hoặc tỷ lệ phần trăm (%).
* **Thuộc tính số học:** Tóm tắt thông qua các đặc trưng về xu hướng tập trung và độ phân tán.

---

### 3. Xu hướng Tập trung & Độ phân tán (Central Tendency & Dispersion)

* **Xu hướng tập trung (Central Tendency):**
* *Mean (Trung bình):* Tổng giá trị chia cho số lượng.
* *Median (Trung vị):* Giá trị nằm ở chính giữa khi xếp thứ tự dữ liệu.
* *Mode (Yếu vị):* Giá trị xuất hiện thường xuyên nhất.
* *Midrange:* Giá trị trung bình giữa cực đại và cực tiểu ($\frac{\text{Max} + \text{Min}}{2}$).


* **Độ phân tán (Dispersion):**
* *Range (Khoảng biến thiên):* $\text{Max} - \text{Min}$.
* *Quartiles (Tứ phân vị):* Chia dữ liệu làm 4 phần bằng nhau ($Q_1, Q_2, Q_3$).
* *IQR (Khoảng tứ phân vị):* $Q_3 - Q_1$, giúp phát hiện điểm bất thường (outliers).
* *Variance (Phương sai) & Standard Deviation (Độ lệch chuẩn):* Đo lường mức độ lệch của dữ liệu so với giá trị trung bình.



---

> **Ý nghĩa:** Việc kết hợp cả xu hướng tập trung và độ phân tán giúp đánh giá chính xác hình dạng phân phối của dữ liệu (độ lệch, khoảng spread) trước khi đưa vào các bước tiền xử lý hay mô hình hóa.
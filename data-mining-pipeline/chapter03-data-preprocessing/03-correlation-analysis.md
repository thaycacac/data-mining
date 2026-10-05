Dưới đây là tóm tắt các điểm quan trọng của bài học về **Phân tích Tương quan & Phân biệt Tương quan với Quan hệ Nhân quả (Correlation Analysis & Causality)**:

---

### 1. Phân tích Tương quan cho Thuộc tính Số (Numerical Attributes)

* **Trực quan hóa:** Sử dụng **biểu đồ tán xạ (scatter plot)** để quan sát nhanh chiều hướng mối quan hệ giữa hai thuộc tính số (tương quan thuận, tương quan nghịch hoặc không tương quan).
* **Hệ số tương quan (Correlation Coefficient - Pearson):** Định lượng độ mạnh và chiều của mối quan hệ tuyến tính bằng cách so sánh độ độ lệch (deviations) so với giá trị trung bình của từng thuộc tính.

---

### 2. Phân tích Tương quan cho Thuộc tính Định danh (Nominal Attributes)

* **Kiểm định Chi-bình phương ($\chi^2$ Test):** Áp dụng cho các thuộc tính phân loại bằng cách so sánh số lần xuất hiện thực tế (observed values) với số lần xuất hiện kỳ vọng (expected values) dựa trên giả định hai thuộc tính độc lập với nhau.
* **Đánh giá:** Khoảng cách/độ chênh lệch giữa giá trị thực tế và giá trị kỳ vọng càng lớn thì khả năng hai thuộc tính định danh có mối tương quan với nhau càng cao.

---

### 3. Tương quan (Correlation) vs. Quan hệ Nhân quả (Causality)

* **Nguyên tắc cốt lõi:** **Tương quan không đồng nghĩa với Nhân quả** (*Correlation does not imply Causality*). Tương quan chỉ thể hiện sự gắn kết/kết hợp về mặt thống kê, không khẳng định thuộc tính này là nguyên nhân gây ra thuộc tính kia.
* **Các ví dụ điển hình về "Tương quan giả chia" (Spurious Correlation):**
* *Đi ngủ mang nguyên giày/dép tương quan với đau đầu:* Nguyên nhân thực sự là do say rượu trước khi ngủ.
* *Càng nhiều lính chữa cháy xuất hiện thì thiệt hại vụ cháy càng lớn:* Cả hai đều do quy mô của vụ cháy quyết định.
* *Doanh số bán kem tương quan với số vụ đuối nước:* Cả hai đều tăng vào mùa hè do thời tiết nắng nóng (biến ẩn / confounding variable).



---

> **Bài học cốt lõi:** Trong khai phá dữ liệu, chỉ sử dụng phân tích tương quan để phát hiện sự dư thừa hoặc mối liên hệ thống kê giữa các thuộc tính, tuyệt đối không vội vã đưa ra kết luận về mối quan hệ nguyên nhân - kết quả nếu không có thực nghiệm hoặc tri thức ngành chứng minh.
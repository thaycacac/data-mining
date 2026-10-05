Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Đo lường Độ tương quan trong Khai phá Luật Kết hợp: Chỉ số Lift & Kiểm định Chi-bình phương (Correlation, Lift & Chi-Square Test)**:

---

### 1. Giới hạn của Support & Confidence và Nhu cầu Đo độ Tương quan

* **Định nghĩa:** Phân tích tương quan đánh giá xem việc xuất hiện của mục $A$ có làm **tăng hoặc giảm** khả năng xuất hiện của mục $B$ hay không.
* **Vấn đề của Confidence:** Một luật có $Conf(A \Rightarrow Y)$ cao vẫn có thể gây hiểu lầm nếu bản thân $Y$ vốn đã có tần suất xuất hiện tự nhiên rất cao trong toàn bộ tập dữ liệu (khiến $A$ và $Y$ thực chất là độc lập hoặc thậm chí tương quan âm).

---

### 2. Chỉ số Lift (Lift Measure)

Chỉ số Lift so sánh xác suất xuất hiện đồng thời của $A$ và $B$ với xác suất xuất hiện độc lập của chúng:

$$\text{Lift}(A \Rightarrow B) = \frac{P(A \cup B)}{P(A) \cdot P(B)} = \frac{\text{Conf}(A \Rightarrow B)}{P(B)}$$

* **Bản chất & Ý nghĩa Giá trị:**
* **$\text{Lift} > 1$ (Tương quan dương):** Việc mua $A$ làm **tăng** khả năng mua $B$. Mối kết hợp này có giá trị thực tiễn cao.
* **$\text{Lift} = 1$ (Độc lập):** $A$ và $B$ hoàn toàn độc lập với nhau. Sự xuất hiện của $A$ không ảnh hưởng đến $B$.
* **$\text{Lift} < 1$ (Tương quan âm):** Việc mua $A$ làm **giảm** khả năng mua $B$ (hai mặt hàng mang tính thay thế hoặc loại trừ lẫn nhau).



---

### 3. Kiểm định Chi-bình phương ($\chi^2$ Test) & Cách So sánh

Áp dụng cho các thuộc tính định danh/phân loại để xác định xem mối liên hệ có ý nghĩa thống kê hay không:

* **Công thức tính:**

$$\chi^2 = \sum \frac{(O - E)^2}{E}$$



*(với $O$ là giá trị thực tế quan sát được - Observed, $E$ là giá trị kỳ vọng - Expected dựa trên giả định hai biến độc lập).*
* **Quy trình Đánh giá & Diễn giải:**
1. Tính giá trị kỳ vọng $E$ cho bảng tần số kết hợp (Contingency Table).
2. Tính tổng $\chi^2$ và so sánh với **ngưỡng ý nghĩa thống kê** (Critical Value / Threshold, ví dụ: ngưỡng $= 10$).
3. Giá trị $\chi^2$ lớn vượt trội so với ngưỡng (ví dụ: $\chi^2 = 127 > 10$) khẳng định **$A$ và $B$ có tương quan mạnh** (bác bỏ giả thuyết độc lập).
4. **Xác định chiều tương quan:** So sánh trực tiếp giá trị thực tế $O$ và kỳ vọng $E$ tại ô xuất hiện đồng thời $(A, B)$:
* Nếu $O > E \rightarrow$ **Tương quan dương (Positive Correlation)**.
* Nếu $O < E \rightarrow$ **Tương quan âm (Negative Correlation)**.





---

> **Bài học cốt lõi:** Một luật kết hợp mạnh không chỉ cần đạt chuẩn Support và Confidence, mà bắt buộc phải thông qua chỉ số **Lift > 1** hoặc kiểm định **Chi-square** để đảm bảo đó là mối quan hệ thực sự chứ không phải sự trùng hợp ngẫu nhiên.
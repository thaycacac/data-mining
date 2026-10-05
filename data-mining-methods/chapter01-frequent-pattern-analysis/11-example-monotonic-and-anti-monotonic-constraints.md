Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Ràng buộc Đơn điệu & Kháng đơn điệu trong Khai phá Mẫu Phổ biến (Monotonic vs. Anti-Monotonic Constraints)**:

---

### 1. Định nghĩa Ràng buộc Biên độ Giá (Price Range Constraint)

* **Biên độ giá (Price Range):** Được định nghĩa là hiệu số giữa giá lớn nhất và giá nhỏ nhất trong một tập mục:

$$\text{Range}(S) = \max(S) - \min(S)$$


* **Bài toán:** Xét ràng buộc $\text{Range}(S) \ge v$ (Biên độ giá của tập mục phải lớn hơn hoặc bằng một giá trị $v$ cho trước).

---

### 2. Phân tích Tính Đơn điệu (Monotonic Constraint)

* **Khái niệm:** Một ràng buộc có tính **Đơn điệu (Monotonic)** nếu một tập con $S$ đã thỏa mãn ràng buộc, thì **mọi tập cha $S'$ (bằng cách thêm mục mới vào $S$) chắc chắn cũng thỏa mãn ràng buộc đó**.
* **Áp dụng cho Biên độ Giá:**
* Khi thêm bất kỳ mục nào vào tập $S$, giá trị $\max$ chỉ có thể giữ nguyên hoặc tăng lên, còn giá trị $\min$ chỉ có thể giữ nguyên hoặc giảm đi.
* Do đó, hiệu số $\max - \min$ **chỉ có thể giữ nguyên hoặc tăng thêm**, không bao giờ giảm.
* **Kết luận:** Nếu $\text{Range}(S) \ge v$ thỏa mãn, thì $\text{Range}(S') \ge v$ cũng chắc chắn thỏa mãn. Ràng buộc $\text{Range}(S) \ge v$ là **Đơn điệu (Monotonic)**.



---

### 3. Phân tích Tính Kháng Đơn điệu (Anti-Monotonic Constraint)

* **Khái niệm:** Một ràng buộc có tính **Kháng đơn điệu (Anti-Monotonic)** nếu một tập con $S$ **vi phạm** (không thỏa mãn) ràng buộc, thì **mọi tập cha $S'$ chứa nó cũng chắc chắn vi phạm**.
* **Áp dụng cho Biên độ Giá:**
* Giả sử tập con $S$ vi phạm ràng buộc (nghĩa là $\text{Range}(S) < v$).
* Khi thêm các mục mới vào $S$, biên độ giá có thể **tăng lên** và vượt qua ngưỡng $v$, khiến tập cha $S'$ trở nên thỏa mãn ràng buộc.
* **Kết luận:** Do vi phạm ở tập con không bảo đảm vi phạm ở tập cha, ràng buộc $\text{Range}(S) \ge v$ **KHÔNG phải là Kháng đơn điệu (Not Anti-Monotonic)**.



---

### 4. Quy trình Lý luận Tổng quát (Summary of Reasoning)

Để xác định tính chất của một ràng buộc trong khai phá mẫu:

1. Hiểu rõ công thức/hàm toán học của ràng buộc (ví dụ: $\max - \min$, $\text{sum}$, $\text{avg}$).
2. Phân tích tác động của việc **thêm mục mới** vào tập hợp đối với giá trị của hàm đó.
3. Kiểm tra xem sự thay đổi có tuân theo quy tắc Đơn điệu (thỏa mãn tập con $\Rightarrow$ thỏa mãn tập cha) hay Kháng đơn điệu (vi phạm tập con $\Rightarrow$ vi phạm tập cha) để áp dụng chiến lược **cắt tỉa (pruning)** hiệu quả.

---

> **Ứng dụng thực tiễn:** Tính chất Kháng đơn điệu cho phép cắt tỉa **Top-down** (như trong Apriori đối với Support), trong khi tính chất Đơn điệu cho phép cắt tỉa **Bottom-up**, giúp thu hẹp đáng kể không gian tìm kiếm khi khai phá mẫu có ràng buộc (Constraint-based Pattern Mining).
Dưới đây là tóm tắt các điểm cốt lõi của bài học thực hành về **Thuật toán Apriori qua Ví dụ Cụ thể (Apriori Algorithm in Action)**:

---

### 1. Cơ chế Hoạt động & Ngưỡng Hỗ trợ (Support Threshold)

* Thuật toán xác định các tập mục phổ biến trong dữ liệu giao dịch dựa trên **ngưỡng hỗ trợ tối thiểu (`min_sup`)**.
* *Ví dụ:* Ngưỡng `min_sup = 0.6` nghĩa là một tập mục chỉ được coi là "phổ biến" nếu nó xuất hiện trong **ít nhất 60%** tổng số các giao dịch.

---

### 2. Hai Quy tắc Cốt lõi: Tự nối (Self-Joining) & Cắt tỉa (Pruning)

* **Tự nối (Self-Joining Step):**
* Ghép cặp các tập mục phổ biến kích thước $k-1$ để tạo ra tập mục ứng viên kích thước $k$.
* **Quy tắc:** Chỉ ghép hai tập mục nếu chúng có cùng $k-2$ mục đầu tiên. Điều này giúp loại bỏ các tổ hợp trùng lặp ngay từ bước sinh ứng viên.


* **Cắt tỉa (Pruning Step):**
* Loại bỏ ngay lập tức các ứng viên kích thước $k$ nếu **bất kỳ tập con kích thước $k-1$ nào của nó không thuộc nhóm phổ biến**.
* Quy tắc này giảm thiểu số lượng ứng viên cần kiểm tra thực tế trong tập dữ liệu.



---

### 3. Phân tích Chi tiết Ví dụ minh họa

* **Tiến trình lặp:**
1. *Đếm & Lọc $L_1$:* Đếm tần suất các mục đơn lẻ $\rightarrow$ Loại bỏ các mục có độ hỗ trợ $< 60\%$.
2. *Sinh $C_2$ & Lọc $L_2$:* Ghép các mục trong $L_1$ thành cặp $2$ mục $\rightarrow$ Đếm tần suất $\rightarrow$ Giữ lại các cặp phổ biến ($L_2$).
3. *Sinh $C_3$ & Lọc $L_3$:* Ghép các cặp từ $L_2$ để tạo ứng viên $3$ mục.


* **Kết quả ví dụ:**
* Tập mục $3$ phần tử như $\{B, C, E\}$ được xác định là tập mục phổ biến.
* Các ứng viên như $\{B, D, E\}$ hoặc $\{C, D, E\}$ bị **loại bỏ (pruned)** từ sớm vì chứa các tập con không phổ biến (ví dụ: tập con $\{D, E\}$ không đạt ngưỡng `min_sup`).



---

> **Kết luận:** Qua ví dụ cụ thể, bài học làm rõ sức mạnh của Apriori: bằng cách kết hợp quy tắc Tự nối (Self-joining) và Cắt tỉa (Pruning), thuật toán thu hẹp tối đa không gian tìm kiếm, tránh việc phải đếm tần suất trùng lặp trên toàn bộ cơ sở dữ liệu.
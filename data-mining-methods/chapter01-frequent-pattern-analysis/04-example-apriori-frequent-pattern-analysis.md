Dưới đây là tóm tắt các điểm cốt lõi của bài học thực hành tiếp theo về **Thuật toán Apriori trong Khai phá Tập mục Phổ biến**:

---

### 1. Thiết lập Ngưỡng Hỗ trợ Tối thiểu (Minimum Support Threshold)

* **Mục tiêu:** Tìm các tập hợp sản phẩm/mục được mua cùng nhau thường xuyên trong tập dữ liệu giao dịch.
* **Xác định ngưỡng:** Ngưỡng `min_sup` trong ví dụ được thiết lập là **$45\%$**.
* Với tổng số $10$ giao dịch, một tập mục bắt buộc phải xuất hiện trong **ít nhất $5$ giao dịch** mới được coi là phổ biến ($\frac{5}{10} = 50\% \ge 45\%$).



---

### 2. Quy trình Thực thi theo Từng Bước (Step-by-Step)

1. **Khởi tạo với Tập 1-mục (1-itemsets):**
* Đếm số lần xuất hiện của từng mục đơn lẻ trong $10$ giao dịch.
* Loại bỏ các mục có tần suất $< 5$ lần.


2. **Sinh Tập 2-mục (2-itemsets):**
* Kết hợp các mục đơn lẻ còn lại để tạo thành các cặp tập ứng viên $2$ mục ($C_2$).
* Quét lại cơ sở dữ liệu để đếm tần suất xuất hiện thực tế của các cặp này và lọc ra các tập $2$ mục phổ biến ($L_2$).


3. **Thử nghiệm Sinh Tập 3-mục (3-itemsets):**
* Áp dụng quy tắc ghép và cắt tỉa để cố gắng tạo tập ứng viên $3$ mục từ $L_2$.



---

### 3. Quy tắc Ghép Ứng viên & Điểm dừng Thuật toán

* **Quy tắc Ghép (Candidate Generation Rule):**
* Để ghép hai tập $k$-mục thành tập $(k+1)$-mục, hai tập đó **bắt buộc phải trùng nhau $k-1$ mục đầu tiên**.
* Nếu không thỏa mãn điều kiện này, hoặc nếu bất kỳ tập con nào của ứng viên mới nằm ngoài nhóm phổ biến, ứng viên đó bị coi là **không hợp lệ (invalid)** và bị cắt tỉa ngay.


* **Kết quả ví dụ:**
* Thu hoạch được **$4$ tập 1-mục** và **$3$ tập 2-mục** đạt đủ ngưỡng hỗ trợ ($\ge 45\%$).
* Khi thử nghiệm sinh tập $3$-mục, không có ứng viên nào thỏa mãn quy tắc ghép và điều kiện tập con phổ biến.
* **Thuật toán dừng:** Tổng cộng thu được **$7$ tập mục phổ biến** ($4$ tập $1$-mục + $3$ tập $2$-mục).



---

> **Bài học rút ra:** Thuật toán Apriori không chỉ cắt tỉa dựa trên tần suất dữ liệu thực tế mà còn tự động dừng lại ngay khi không thể tạo thêm ứng viên hợp lệ nào ở cấp độ cao hơn.
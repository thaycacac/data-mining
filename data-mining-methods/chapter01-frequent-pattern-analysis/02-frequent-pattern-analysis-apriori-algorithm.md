Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Phân tích Mẫu phổ biến & Thuật toán Apriori (Frequent Pattern Analysis & Apriori Algorithm)**:

---

### 1. Cơ bản về Phân tích Mẫu phổ biến (Frequent Pattern Analysis)

* **Khái niệm:** Phân tích mẫu phổ biến tập trung vào việc tìm kiếm các tập mục (itemsets) xuất hiện cùng nhau với tần suất cao trong dữ liệu giao dịch (transactional data).
* **Độ hỗ trợ (Support):** Là chỉ số đo lường xác suất xuất hiện của một tập mục trong toàn bộ tập giao dịch.
* **Ngưỡng hỗ trợ tối thiểu (Minimum Support Threshold - `min_sup`):** Do người phân tích thiết lập để lọc ra các tập mục đạt tiêu chuẩn được coi là "phổ biến" (frequent).

---

### 2. Thách thức & Các Khái niệm Giảm độ phức tạp

* **Bế tắc của Thuật toán Duyệt cạn (Brute-Force):** Việc liệt kê tất cả các tổ hợp tập mục khả dĩ là bất khả thi về mặt tính toán vì số lượng tổ hợp tăng theo **cấp số nhân** ($2^d$ với $d$ là số lượng mục).
* **Hai khái niệm tối ưu không gian tìm kiếm:**
* **Mẫu đóng (Closed Frequent Itemsets):** Tập mục phổ biến mà *không có tập cha nào* chứa nó có cùng độ hỗ trợ.
* **Mẫu cực đại (Maximal Frequent Itemsets):** Tập mục phổ biến lớn nhất mà *không có tập cha nào* chứa nó cũng là tập mục phổ biến (bỏ qua giá trị độ hỗ trợ chính xác).



---

### 3. Thuật toán Apriori (Apriori Algorithm)

Thuật toán Apriori giải quyết thách thức bùng nổ tổ hợp bằng chiến lược **cắt tỉa (pruning)** dựa trên tính chất đơn điệu xuống (downward closure property):

* **Nguyên lý Cắt tỉa (Apriori Property):** Nếu một tập mục là **không phổ biến** (infrequent), thì **tất cả các tập cha (supersets) chứa nó cũng chắc chắn không phổ biến** và có thể loại bỏ ngay lập tức mà không cần kiểm tra.
* **Quy trình Lặp (Iterative Process):**
1. Bắt đầu tìm các tập mục phổ biến kích thước $1$ ($L_1$).
2. Sinh tập ứng viên kích thước $k$ ($C_k$) từ các tập phổ biến kích thước $k-1$ ($L_{k-1}$).
3. Cắt tỉa các ứng viên chứa tập con không phổ biến.
4. Quét dữ liệu để tính `support` thực tế và giữ lại các ứng viên đạt `min_sup` để tạo $L_k$.
5. Lặp lại cho đến khi không còn tập mục phổ biến nào được tìm thấy.



---

> **Kết luận:** Thuật toán Apriori giúp giảm thiểu tối đa không gian tìm kiếm các tập mục phổ biến, tạo tiền đề hiệu quả để rút ra các **Luật kết hợp (Association Rules)** với các chỉ số như Độ tin cậy (Confidence) và Độ cẩu (Lift).
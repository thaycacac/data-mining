Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Rời rạc hóa (Discretization) & Thu giảm Dữ liệu (Data Reduction)**:

---

### 1. Rời rạc hóa Dữ liệu (Discretization)

Rời rạc hóa là quá trình chuyển đổi các giá trị số liên tục thành các khoảng (intervals/bins) hoặc giá trị rời rạc để đơn giản hóa việc phân tích và hỗ trợ các mô hình nhận diện mẫu.

* **Hai cách tiếp cận chung:**
* *Chia nhỏ (Splitting):* Chia một khoảng lớn thành các khoảng nhỏ hơn một cách đệ quy.
* *Gộp khoảng (Merging):* Kết hợp các khoảng lân cận có tính chất tương đồng.


* **Rời rạc hóa Không giám sát (Unsupervised Discretization):** Không sử dụng nhãn lớp (class labels).
* *Equal-width binning (Chia khoảng bằng nhau):* Chia khoảng biến thiên ($\text{Max} - \text{Min}$) thành $k$ phần có độ rộng bằng nhau.
* *Equal-frequency binning (Chia tần suất bằng nhau):* Chia sao cho mỗi khoảng chứa số lượng điểm dữ liệu bằng nhau.
* *Phân cụm (Clustering) & Phân hoạch trực quan:* Dựa trên độ tương đồng giữa các điểm dữ liệu hoặc tri thức ngành.



---

### 2. Rời rạc hóa Có giám sát (Supervised Discretization)

Sử dụng thông tin từ nhãn lớp để tạo ra các khoảng chia có ý nghĩa nhất đối với bài toán phân lớp.

* **Chia nhỏ dựa trên Độ hỗn loạn (Entropy-based Splitting):** Tìm các điểm cắt (cut points) sao cho độ hỗn loạn (entropy) trong từng khoảng là nhỏ nhất (tối đa hóa độ tinh khiết/đồng nhất của các lớp trong khoảng đó).
* **Gộp khoảng dựa trên Chi-bình phương (Chi-square Merging):** Áp dụng kiểm định $\chi^2$ để gộp các khoảng lân cận có phân phối nhãn lớp độc lập hoặc tương tự nhau.

---

### 3. Thu giảm Dữ liệu (Data Reduction)

Nhằm thu nhỏ quy mô tập dữ liệu để tăng hiệu năng tính toán nhưng vẫn giữ lại được các mẫu/thông tin quan trọng.

* **Hai hướng thu giảm:**
* *Thu giảm số chiều (Dimensionality Reduction):* Giảm số lượng thuộc tính/cột.
* *Thu giảm số lượng (Numerosity Reduction):* Giảm số lượng bản ghi/dòng (thông qua lấy mẫu, gom cụm,...).


* **Phương pháp Lựa chọn Thuộc tính (Attribute / Feature Selection):**
* *Forward Selection (Lựa chọn tiến):* Bắt đầu với tập thuộc tính rỗng và thêm dần từng thuộc tính có nhiều thông tin nhất.
* *Backward Elimination (Loại trừ lùi):* Bắt đầu với tất cả các thuộc tính và loại bỏ dần các thuộc tính ít giá trị nhất.


* **Kỹ nghệ Thuộc tính (Feature Engineering):** Kết hợp giữa tri thức ngành và các phương pháp tự động (như Cây quyết định - Decision Tree Induction) để xác định các đặc trưng quan trọng nhất phục vụ phân tích.

---

> **Kết luận:** Rời rạc hóa giúp đơn giản hóa dạng dữ liệu, còn thu giảm dữ liệu giúp giảm tải tính toán mà không làm mất đi bản chất tri thức trong tập dữ liệu ban đầu.
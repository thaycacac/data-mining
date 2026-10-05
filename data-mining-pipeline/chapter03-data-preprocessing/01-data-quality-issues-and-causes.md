Dưới đây là tóm tắt các điểm quan trọng của bài học về **Tổng quan Tiền xử lý Dữ liệu & Chất lượng Dữ liệu (Data Preprocessing & Data Quality)**:

---

### 1. Tổng quan về Tiền xử lý Dữ liệu (Data Preprocessing)

* **Vai trò:** Là bước chuẩn bị bắt buộc trong quy trình khai phá dữ liệu nhằm phát hiện và xử lý các lỗi tồn tại trong dữ liệu thô.
* **4 nhiệm vụ chính:**
1. **Làm sạch dữ liệu (Data Cleaning):** Xử lý dữ liệu thiếu, loại bỏ nhiễu và sửa lỗi không nhất quán.
2. **Tích hợp dữ liệu (Data Integration):** Kết hợp dữ liệu từ nhiều nguồn khác nhau.
3. **Biến đổi dữ liệu (Data Transformation):** Chuẩn hóa và biến đổi dữ liệu về dạng thích hợp cho thuật toán.
4. **Thu giảm dữ liệu (Data Reduction):** Nén/giảm quy mô dữ liệu nhưng vẫn giữ nguyên thông tin cốt lõi.



---

### 2. Các Khía cạnh Đánh giá Chất lượng Dữ liệu (Data Quality)

Chất lượng dữ liệu được đánh giá ở hai cấp độ:

* **Cấp độ Hệ thống / Khai thác:**
* Tính liên quan (Relevance), tính truy cập được (Accessibility), tính dễ diễn giải (Interpretability), độ tin cậy (Reliability) và tính thời sự (Timeliness).


* **Cấp độ Giá trị Dữ liệu (Data Value Level):**
* **Độ chính xác (Accuracy):** Giá trị phản ánh đúng thực tế.
* **Tính nhất quán (Consistency):** Không mâu thuẫn giữa các bảng hoặc hệ thống.
* **Độ phân giải / Chi tiết (Granularity & Precision):** Mức độ chi tiết của dữ liệu.
* **Tính đầy đủ (Completeness):** Mức độ đầy đủ, không bị khuyết thiếu.



---

### 3. Vấn đề Dữ liệu Thường gặp & Nguyên nhân

* **Hiện trạng dữ liệu thực tế:** Rất dễ bị **thiếu (incomplete)**, **nhiễu (noisy)** và **không nhất quán (inconsistent)**.
* **Nguyên nhân chính:**
* Lỗi do con người nhập liệu (human errors).
* Sự cố thiết bị phần cứng hoặc lỗi phần mềm (hardware/software failures).
* Thay đổi cấu trúc dữ liệu hoặc quy chuẩn theo thời gian (changes over time).



---

> **Thông điệp cốt lõi:** Nhận diện đúng nguyên nhân gây ra lỗi dữ liệu giúp thiết kế các quy trình tiền xử lý phù hợp, đảm bảo nguyên tắc "Dữ liệu vào sạch thì tri thức đầu ra mới chất lượng".
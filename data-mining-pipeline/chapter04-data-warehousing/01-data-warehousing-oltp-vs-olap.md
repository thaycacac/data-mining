Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Kho dữ liệu (Data Warehousing) trong Quy trình Khai phá Dữ liệu**:

---

### 1. Đặc trưng Cốt lõi của Kho Dữ liệu (Data Warehouse)

Kho dữ liệu đóng vai trò là hạ tầng quản lý và chuẩn bị dữ liệu tập trung phục vụ phân tích và đưa ra quyết định kinh doanh.

* **Hướng chủ đề (Subject-Oriented):** Tập trung vào các đối tượng hoặc chủ thể kinh doanh cụ thể (như khách hàng, sản phẩm, học viên) thay vì xử lý giao dịch hàng ngày.
* **Tích hợp (Integrated):** Kết hợp và đồng bộ dữ liệu từ nhiều nguồn khác nhau (không đồng nhất) về một quy chuẩn duy nhất.

---

### 2. So sánh Hệ thống Giao dịch (Operational) vs. Kho Dữ liệu (Data Warehouse)

* **Tính biến đổi theo thời gian (Time-Variant):**
* *Hệ thống giao dịch:* Chỉ lưu trữ dữ liệu hiện tại (real-time).
* *Kho dữ liệu:* Lưu trữ cả dữ liệu lịch sử lẫn hiện tại kèm theo mốc thời gian (timestamp) để phục vụ phân tích xu hướng.


* **Tính bất biến / Không biến động (Non-Volatile):**
* *Hệ thống giao dịch:* Thường xuyên truy vấn, cập nhật, xóa bỏ dữ liệu liên tục.
* *Kho dữ liệu:* Chủ yếu hỗ trợ các thao tác **Đọc (Read)** và **Thêm mới (Append)**, không chỉnh sửa trực tiếp dữ liệu lịch sử.



---

### 3. Khác biệt giữa OLTP và OLAP

| Đặc điểm | OLTP (Online Transactional Processing) | OLAP (Online Analytical Processing) |
| --- | --- | --- |
| **Mục tiêu** | Hỗ trợ vận hành daily, xử lý giao dịch hàng ngày | Hỗ trợ phân tích phức tạp, đưa ra quyết định chiến lược |
| **Bản chất dữ liệu** | Dữ liệu chi tiết, liên tục cập nhật | Dữ liệu tổng hợp, lịch sử, quy mô lớn |
| **Thao tác chính** | Cập nhật/thêm/xóa chi tiết nhanh chóng | Truy vấn đọc, gom cụm, xoay chiều dữ liệu |

---

### 4. Kiến trúc và Thiết kế Kho Dữ liệu

Thiết kế kho dữ liệu hiệu quả đòi hỏi sự phối hợp chặt chẽ giữa:

1. **Nguồn dữ liệu (Data Sources):** Thu thập từ nhiều hệ thống tác nghiệp khác nhau.
2. **Quá trình tích hợp (ETL - Extract, Transform, Load):** Trích xuất, biến đổi và nạp dữ liệu.
3. **Lưu trữ & Truy vấn (Storage & OLAP Engine):** Hỗ trợ các thao tác khai phá dữ liệu và phân tích đa chiều với hiệu năng cao.

---

> **Kết luận:** Kho dữ liệu cung cấp nền tảng dữ liệu lịch sử đã qua làm sạch và tích hợp, tạo tiền đề vững chắc cho các kỹ thuật mô hình hóa và khai phá dữ liệu ở giai đoạn tiếp theo.
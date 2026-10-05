Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Mô hình hóa Kho Dữ liệu & Các Thao tác trên Khối Dữ liệu Đa chiều (Data Warehouse Modeling & OLAP Operations)**:

---

### 1. Khái niệm Mô hình Kho Dữ liệu: Facts & Dimensions

Kho dữ liệu tổ chức dữ liệu theo hai thành phần chính:

* **Bảng Thực thể / Sự kiện (Fact Table):** Chứa các chỉ số đo lường định lượng của sự kiện kinh doanh (ví dụ: doanh số, số lượng bán, doanh thu).
* **Bảng Chiều / Chiều phân tích (Dimension Tables):** Chứa các thuộc tính định tính dùng để mô tả bối cảnh xung quanh sự kiện (ví dụ: Khách hàng, Thời gian, Sản phẩm, Địa điểm).

---

### 2. Các Dạng Mô hình Sơ đồ Kho Dữ liệu (Schema Models)

* **Sơ đồ Hình sao (Star Schema):**
* Gồm **1 bảng Fact** ở trung tâm kết nối trực tiếp tới nhiều bảng Dimension xung quanh.
* *Đặc điểm:* Đơn giản, truy vấn nhanh, các bảng Dimension chưa được chuẩn hóa hoàn toàn (dư thừa dữ liệu chấp nhận được).


* **Sơ đồ Bông tuyết (Snowflake Schema):**
* Biến thể của Star Schema, trong đó các bảng Dimension được chuẩn hóa thêm và phân nhánh nối với các bảng Dimension phụ khác (ví dụ: `Customer` nối tiếp tới `Card`).
* *Đặc điểm:* Tiết kiệm bộ nhớ, giảm dư thừa nhưng truy vấn phức tạp hơn do phải `JOIN` nhiều bảng.


* **Sơ đồ Chòm sao / Tập hợp sự kiện (Fact Constellation Schema):**
* Chứa **nhiều bảng Fact** dùng chung các bảng Dimension (ví dụ: Bảng Fact `Sales` và bảng Fact `Shipping` cùng chia sẻ các chiều `Item` và `Time`).
* *Đặc điểm:* Phù hợp cho các doanh nghiệp lớn có nhiều quy trình kinh doanh kết nối với nhau.



---

### 3. Mô hình Dữ liệu Đa chiều & Các Thao tác OLAP (Data Cube Operations)

Dữ liệu trong kho được tổ chức dưới dạng **Khối dữ liệu đa chiều (Data Cube)**. Nhà phân tích sử dụng 5 thao tác cơ bản để khai thác tri thức:

* **Roll-up (Gom tổng hợp):** Tăng mức độ tổng quát, giảm độ chi tiết bằng cách tổng hợp dữ liệu lên cấp cao hơn (ví dụ: từ dữ liệu cấp *Ngày* gom thành cấp *Tháng* hoặc *Năm*).
* **Drill-down (Chia chi tiết):** Ngược lại với Roll-up, đi sâu vào độ chi tiết nhỏ hơn (ví dụ: từ doanh số *Quý* tách xuống từng *Tuần* hoặc *Ngày*).
* **Slice (Cắt lát):** Chọn một giá trị cố định trên **1 chiều** để tạo thành một lát cắt 2D (ví dụ: chỉ lọc dữ liệu cho chiều `Time = 2026`).
* **Dice (Cắt khối con):** Chọn tập con trên **nhiều chiều** để tạo ra một khối dữ liệu nhỏ hơn (ví dụ: lọc `Time = Q1`, `Location = Boulder`, `Item = Electronics`).
* **Pivot / Rotate (Xoay chiều):** Xoay các trục tọa độ của khối dữ liệu để nhìn góc độ phân tích mới trên màn hình.

---

> **Bài học cốt lõi:** Việc lựa chọn sơ đồ kho dữ liệu phù hợp cùng các thao tác linh hoạt trên Data Cube giúp người làm dữ liệu nhanh chóng trích xuất thông tin tổng quan lẫn chi tiết, tạo tiền đề cho các mô hình dự báo và phân tích nâng cao.
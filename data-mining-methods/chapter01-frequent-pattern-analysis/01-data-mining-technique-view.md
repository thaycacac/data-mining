Dưới đây là tóm tắt các điểm cốt lõi của bài học về **Tổng quan các Phương pháp Mô hình hóa trong Khai phá Dữ liệu (Data Mining Modeling Techniques)**:

---

### 1. Khái niệm Cốt lõi & Khung góc nhìn Khai phá Dữ liệu

Dữ liệu sau khi qua các giai đoạn Hiểu dữ liệu, Tiền xử lý và Kho dữ liệu sẽ bước vào giai đoạn **Mô hình hóa (Modeling)**. Một dự án khai phá dữ liệu tổng thể được định hình qua **4 góc nhìn chính**:

1. **Thuộc tính dữ liệu (Data Attributes):** Kiểu dữ liệu, định dạng và đặc tính số học/phân loại.
2. **Miền ứng dụng (Application Domain):** Bối cảnh ngành (tài chính, y tế, bán lẻ, viễn thông...).
3. **Tri thức cần khám phá (Knowledge to be Discovered):** Mục tiêu đầu ra (luật kết hợp, phân lớp, phân cụm...).
4. **Kỹ thuật áp dụng (Techniques Used):** Các thuật toán toán học/thống kê/mô hình học máy phù hợp.

---

### 2. Các Kỹ thuật Khai phá Dữ liệu Chính (Key Data Mining Techniques)

* **Phân tích Mẫu phổ biến (Frequent Pattern Analysis):**
* Tự động phát hiện các tập mục (itemsets), chuỗi (sequences) hoặc cấu trúc (structures) xuất hiện lặp đi lặp lại nhiều lần trong tập dữ liệu.
* *Ứng dụng:* Khai phá luật kết hợp (Association Rules - ví dụ: bài toán Giỏ hàng "Market Basket Analysis") và phân tích tương quan.


* **Phân lớp & Dự báo (Classification & Prediction):**
* **Phân lớp (Classification):** Gán một đối tượng dữ liệu vào các **nhãn/lớp đã định trước (predefined classes)** dựa trên thuộc tính của nó (Học có giám sát - Supervised Learning).
* **Dự báo (Prediction):** Ước lượng hoặc dự đoán các giá trị **số học liên tục (continuous numerical values)** (ví dụ: dự báo giá nhà, doanh thu).


* **Phân cụm (Clustering):**
* Tự động gom nhóm các đối tượng dữ liệu dựa trên độ tương đồng mà **không cần nhãn lớp biết trước** (Học không giám sát - Unsupervised Learning).
* *Nguyên tắc cốt lõi:* Độ tương đồng trong cùng một cụm là cao nhất (**high intra-cluster similarity**), và độ tương đồng giữa các cụm khác nhau là thấp nhất (**low inter-cluster similarity**).



---

### 3. Các Kỹ thuật Bổ trợ & Ứng dụng Nâng cao

* **Phát hiện Bất thường / Ngoại lệ (Anomaly / Outlier Detection):**
* Nhận diện các điểm dữ liệu hiếm gặp hoặc hành vi khác biệt đáng kể so với phân phối/mẫu hành vi thông thường.
* *Ứng dụng:* Phát hiện gian lận tài chính (Fraud detection), phát hiện xâm nhập mạng, hoặc phát hiện lỗi thiết bị.


* **Phân tích Xu hướng & Sự tiến triển (Trend & Evolution Analysis):**
* Nghiên cứu sự thay đổi của dữ liệu theo chuỗi thời gian (Time-series data).
* Phân rã chuỗi thời gian thành các thành phần: **Xu hướng (Trend)**, **Yếu tố mùa vụ (Seasonal patterns)**, và **Biến động bất thường (Anomalies/Noise)**.



---

> **Kết luận:** Giai đoạn Mô hình hóa cung cấp một hộp dụng cụ đa dạng (Classification, Clustering, Association Rules, Anomaly Detection...). Việc lựa chọn đúng kỹ thuật phụ thuộc trực tiếp vào bản chất của dữ liệu và bài toán kinh doanh cần giải quyết.
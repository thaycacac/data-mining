Dưới đây là tóm tắt các điểm cốt lõi của bài học đi sâu vào **Toán học Thuật toán Expectation-Maximization (EM) với Phân phối Gaussian**:

---

### 1. Tổng quan Thuật toán EM với Phân phối Gaussian

* **Nguyên lý:** Thuật toán tính toán lặp để ước lượng xác suất một điểm dữ liệu thuộc về từng cụm, dựa trên các tham số của phân phối Chuẩn (Gaussian) gồm **Giá trị trung bình ($\mu$)** và **Độ lệch chuẩn ($\sigma$)**.
* **Chu trình Lặp:** Tiến hành luân phiên giữa 2 bước **E-step (Expectation)** và **M-step (Maximization)** để tối ưu hóa tham số mô hình.

---

### 2. Bước E (Expectation - Tính toán Xác suất)

* **Hàm Mật độ Xác suất (PDF):** Với mỗi điểm dữ liệu $x$ và mỗi cụm có tham số $(\mu, \sigma)$, tính giá trị mật độ xác suất Gaussian $f(x \mid \mu, \sigma)$.
* **Chuẩn hóa (Normalization):** Chuẩn hóa các giá trị xác suất này trên tất cả các cụm sao cho **tổng xác suất thành viên (membership probability)** của điểm dữ liệu $x$ đối với mọi cụm bằng $1$.

---

### 3. Bước M (Maximization - Cập nhật Tham số)

* **Cập nhật Giá trị Trung bình ($\mu$):**
* Tính lại $\mu$ mới của cụm bằng **trung bình cộng có trọng số** của tất cả các điểm dữ liệu.
* Trọng số chính là xác suất thành viên của từng điểm đối với cụm đó (tính từ bước E).


* **Cập nhật Độ lệch chuẩn ($\sigma$):**
* Tính lại $\sigma$ mới dựa trên **phương sai có trọng số** của các điểm dữ liệu so với giá trị trung bình $\mu$ vừa được cập nhật.



---

> **Kết luận:** Quá trình E-step và M-step lặp đi lặp lại liên tục giúp liên tục tinh chỉnh các tham số $(\mu, \sigma)$ của từng cụm Gaussian cho đến khi mô hình khớp tốt nhất với phân bố dữ liệu thực tế.
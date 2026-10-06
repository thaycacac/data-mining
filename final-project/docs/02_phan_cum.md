# Phân cụm (Clustering)

Áp dụng trong: `src/clustering.py`, `notebooks/04_clustering_provinces.ipynb` (RQ2).

## 1. K-Means

**Ý tưởng:** chia n điểm dữ liệu thành k cụm sao cho tổng bình phương khoảng cách từ mỗi điểm đến tâm cụm (centroid) của nó là nhỏ nhất ("inertia" / within-cluster sum of squares). Thuật toán lặp 2 bước cho đến hội tụ: (1) gán mỗi điểm vào centroid gần nhất, (2) cập nhật centroid = trung bình các điểm trong cụm.

**Nhược điểm cố hữu:** phải chọn trước k; nhạy với khởi tạo ngẫu nhiên (dự án dùng `n_init=10` — chạy 10 lần khởi tạo khác nhau, giữ kết quả tốt nhất); giả định cụm có dạng lồi/gần hình cầu, kích thước tương đối đều.

### Chọn k: Elbow method + Silhouette score

- **Elbow method:** vẽ inertia theo k, tìm điểm "khuỷu tay" nơi việc tăng k không còn giảm inertia đáng kể — mang tính trực quan, không có tiêu chí định lượng rõ ràng.
- **Silhouette score:** với mỗi điểm i, `s(i) = (b(i) - a(i)) / max(a(i), b(i))`, trong đó `a(i)` = khoảng cách trung bình đến các điểm **cùng cụm**, `b(i)` = khoảng cách trung bình nhỏ nhất đến các điểm **cụm khác gần nhất**. Giá trị trong [-1, 1]; càng gần 1 nghĩa là cụm càng tách biệt rõ (compact + well-separated). Dự án dùng ngưỡng **Silhouette > 0,3** làm tiêu chí thành công (mức "hợp lý" cho dữ liệu nhỏ, nhiều chiều — không kỳ vọng mức cao như dữ liệu lớn/ít chiều).

**Áp dụng cụ thể:** quét k=2..8 trên không gian 70 chiều gốc, Silhouette tối đa chỉ 0,259 (dưới ngưỡng) — xem mục "curse of dimensionality" bên dưới. Sau khi giảm chiều PCA-5, k=4 đạt Silhouette=0,357.

## 2. Hierarchical Clustering (Agglomerative, Ward linkage)

**Ý tưởng:** bắt đầu mỗi điểm là 1 cụm riêng, lặp lại việc **gộp 2 cụm gần nhau nhất** cho đến khi còn 1 cụm duy nhất — tạo thành một cây phân cấp (dendrogram). **Ward linkage** chọn tiêu chí gộp sao cho mức tăng tổng phương sai nội cụm (within-cluster variance) là nhỏ nhất ở mỗi bước — có xu hướng tạo cụm kích thước cân đối hơn so với các linkage khác (single/complete/average).

**Ưu điểm so với K-Means:** không cần chọn trước k (cắt dendrogram ở độ cao mong muốn để lấy số cụm bất kỳ); kết quả **xác định** (không phụ thuộc khởi tạo ngẫu nhiên); dendrogram tự nó là công cụ trực quan hữu ích để thấy cấu trúc lồng nhau giữa các tỉnh.

**Áp dụng cụ thể:** cắt ở k=4 (khớp K-Means để so sánh công bằng), đạt Silhouette=0,345; **Adjusted Rand Index (ARI)** so với K-Means = 0,84 (ARI đo mức tương đồng giữa 2 cách gán nhãn cụm, hiệu chỉnh theo yếu tố ngẫu nhiên; 1,0 = trùng khớp hoàn toàn, 0 = ngẫu nhiên) — cho thấy 2 thuật toán độc lập đi đến cấu trúc gần giống nhau, củng cố độ tin cậy.

## 3. DBSCAN

**Ý tưởng:** cụm = vùng mật độ điểm cao, ngăn cách bởi vùng mật độ thấp ("nhiễu"). Hai tham số: `eps` (bán kính lân cận) và `min_samples` (số điểm tối thiểu trong bán kính `eps` để coi là "điểm lõi"). Không cần chọn trước k — số cụm **tự xuất hiện** từ cấu trúc mật độ.

**Giả định ngầm quan trọng:** cụm được ngăn cách bởi khoảng trống mật độ rõ ràng. Khi dữ liệu biến thiên **liên tục** (không có khoảng trống), DBSCAN hoặc coi gần hết là 1 cụm lớn, hoặc (ở eps nhỏ hơn) coi phần lớn điểm là nhiễu.

**Áp dụng cụ thể và phát hiện thực nghiệm:** quét eps trên dữ liệu 34 tỉnh (PCA-5): ở eps cho Silhouette cao nhất (3,0 → 0,544), **23/34 tỉnh bị coi là nhiễu** — một minh chứng cụ thể rằng dữ liệu cấp tỉnh không có cấu trúc mật độ rõ ràng, DBSCAN không phù hợp làm thuật toán chính cho bài toán này (dù Silhouette "trên giấy" trông cao — vì tính trên rất ít điểm còn lại, không đại diện).

## 4. Gaussian Mixture Model (GMM)

**Ý tưởng:** giả định dữ liệu sinh ra từ hỗn hợp k phân phối Gauss đa biến; ước lượng tham số (trung bình, hiệp phương sai, trọng số mỗi thành phần) bằng thuật toán **EM (Expectation-Maximization)**. Khác K-Means (gán **cứng** mỗi điểm vào 1 cụm), GMM cho **xác suất mềm** (soft assignment) — một tỉnh có thể "thuộc" nhiều cụm với xác suất khác nhau, linh hoạt hơn khi ranh giới cụm không rõ ràng.

**Áp dụng cụ thể:** k=4, Silhouette=0,297 (thấp hơn K-Means một chút), ARI so với K-Means=0,63 (đồng thuận thấp hơn Hierarchical) — phản ánh GMM "nhìn" ranh giới cụm khác đi do giả định hình elip (hiệp phương sai đầy đủ) thay vì hình cầu như K-Means.

## 5. PCA (Principal Component Analysis) — giảm chiều trước khi phân cụm

**Ý tưởng:** tìm các trục trực giao (thành phần chính) theo thứ tự giải thích phương sai dữ liệu giảm dần, rồi chiếu dữ liệu lên vài trục đầu tiên — nén thông tin, loại bớt nhiễu từ các chiều ít thông tin.

**Vì sao cần ở đây — "curse of dimensionality":** 70 đặc trưng/34 mẫu khiến khoảng cách Euclidean giữa các điểm trở nên kém phân biệt (trong không gian nhiều chiều, khoảng cách giữa điểm gần nhất và xa nhất có xu hướng hội tụ về nhau — hiện tượng được chứng minh toán học, gọi là "distance concentration"). PCA giảm về 5 chiều (giữ 77,5% phương sai) giúp Silhouette tăng từ 0,259 lên 0,357 — minh chứng thực nghiệm trực tiếp cho vấn đề này trên chính dữ liệu của dự án.

**Lưu ý diễn giải:** phân cụm trên không gian PCA, nhưng **chân dung cụm (profiling)** vẫn nên quay lại không gian đặc trưng gốc (chưa chuẩn hóa) để giữ ý nghĩa thực tế (vd "Toán trung bình 4,65" dễ hiểu hơn nhiều so với "thành phần chính thứ 1 = -2,3").

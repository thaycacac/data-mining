# Phát hiện bất thường (Anomaly / Outlier Detection)

Áp dụng trong: `src/anomaly.py`, `notebooks/05_anomaly_detection.ipynb` (RQ3).

## 0. Vì sao bài toán này khó hơn 2 bài toán kia

Luật kết hợp và phân cụm có thể tự đánh giá bằng độ đo nội tại (lift, Silhouette) tính trực tiếp từ dữ liệu. Phát hiện bất thường **không có ground-truth** (không ai biết chắc thí sinh/nhóm nào thực sự "bất thường" theo nghĩa cần quan tâm) — nên không thể tính precision/recall. Cách tiếp cận chuẩn trong thực tế: dùng **nhiều phương pháp độc lập**, xem chúng có **đồng thuận** không, và kiểm tra **độ ổn định** khi đổi tham số — nếu một tín hiệu xuất hiện nhất quán qua nhiều góc nhìn, khả năng là tín hiệu thật (không phải nhiễu do một thuật toán/tham số cụ thể) sẽ cao hơn.

## 1. Baseline thống kê: Z-score và IQR

- **Z-score:** `z = (x - μ) / σ`. Thường lấy ngưỡng |z| > 2 hoặc 3 (ở phân phối chuẩn, |z|>3 chỉ xảy ra với xác suất ~0,27%). Giả định ngầm: dữ liệu xấp xỉ phân phối chuẩn.
- **IQR (Tukey's fences):** ngưỡng `[Q1 - 1,5×IQR, Q3 + 1,5×IQR]` với `IQR = Q3 - Q1` (Q1, Q3 = tứ phân vị 25%/75%). Không giả định phân phối chuẩn, bền hơn (robust) với dữ liệu lệch — thường dùng làm đối chứng cho Z-score.

**Phát hiện thực nghiệm quan trọng:** áp dụng trực tiếp lên **điểm thi cá nhân** (vd điểm Toán từng thí sinh) cho **0 kết quả** (0 thí sinh có
|z|>3) — vì điểm thi cá nhân biến thiên tự nhiên trong khoảng hẹp
[0,10], không có "ngoại lệ cực đoan" theo nghĩa thống kê cổ điển. Baseline chỉ có ý nghĩa khi áp dụng lên **đặc trưng tổng hợp cấp nhóm** (vd chênh lệch điểm trung bình 1 nhóm so với trung bình tỉnh) — ở đó phương sai nhỏ hơn nhiều nên độ lệch bất thường mới "nổi" lên rõ. **Bài học:** chọn đúng đơn vị phân tích/mức độ tổng hợp dữ liệu quan trọng không kém chọn đúng thuật toán.

## 2. Kiểm định dồn điểm (heaping)

Không phải một thuật toán outlier kinh điển, nhưng là một kỹ thuật phát hiện bất thường theo **phân phối tần suất**: so sánh tần suất quan sát được tại một giá trị cụ thể (vd điểm 5,0) với tần suất **kỳ vọng** (nội suy từ 2 giá trị lân cận). Tỷ lệ Observed/Expected lệch xa 1,0 là dấu hiệu "dồn/làm tròn" tại giá trị đó — hiện tượng tâm lý học phổ biến trong chấm thi tự luận quanh các mốc điểm quan trọng (ở đây là mốc xét tốt nghiệp ≥5,0). Dùng phép kiểm Poisson xấp xỉ `z ≈ (Observed - Expected) / √Expected` để ước lượng mức ý nghĩa — nhưng với N hàng chục nghìn, z luôn lớn ngay cả khi lệch nhỏ, nên **tỷ lệ (ratio)** mới là chỉ số diễn giải thực tế, không phải trị số z.

## 3. Isolation Forest

**Ý tưởng:** một điểm bất thường thường **dễ bị cô lập** (isolate) hơn điểm bình thường khi dùng các phép chia ngẫu nhiên. Thuật toán xây nhiều cây nhị phân (isolation trees), mỗi cây chia dữ liệu bằng cách chọn ngẫu nhiên 1 đặc trưng và 1 ngưỡng chia tại mỗi node. **Độ sâu trung bình** (qua nhiều cây) cần thiết để cô lập một điểm là điểm số bất thường: điểm bất thường có độ sâu trung bình **ngắn hơn** (dễ tách biệt khỏi phần còn lại).

**Ưu điểm:** không cần giả định phân phối, hiệu quả trên dữ liệu nhiều chiều, độ phức tạp gần tuyến tính — phù hợp cho dữ liệu lớn.

**Tham số chính:** `n_estimators` (số cây, dự án dùng 200), `contamination` (tỷ lệ ước lượng điểm bất thường trong dữ liệu — chỉ ảnh hưởng ngưỡng phân loại nhị phân, không ảnh hưởng *thứ hạng* điểm số).

## 4. Local Outlier Factor (LOF)

**Ý tưởng:** đo mật độ cục bộ (local density) của một điểm so với mật độ cục bộ của các điểm lân cận (k-nearest neighbors). LOF ≈ 1 nghĩa là mật độ tương đương hàng xóm (bình thường); LOF » 1 nghĩa là điểm này nằm ở vùng thưa hơn hẳn các hàng xóm của nó (bất thường **cục bộ** — khác Isolation Forest vốn nhìn toàn cục).

**Vì sao dùng cả 2 (IF và LOF):** 2 thuật toán dựa trên nguyên lý khác nhau (cô lập toàn cục vs mật độ cục bộ) nên **bổ sung** nhau — một điểm được cả 2 cùng gắn cờ có độ tin cậy cao hơn một điểm chỉ 1 phương pháp phát hiện.

## 5. Đo đồng thuận: Jaccard similarity

`Jaccard(A, B) = |A ∩ B| / |A ∪ B|` — áp dụng cho 2 **tập hợp top-N** đơn vị bất thường nhất theo 2 phương pháp. Giá trị 1,0 = 2 tập hoàn toàn trùng nhau; 0 = không có điểm chung. Dự án đo Jaccard giữa top-30 của Isolation Forest và LOF (kết quả: 0,32–0,36) làm thước đo đồng thuận chính — thay cho precision/recall (không khả thi vì không có nhãn đúng).

## 6. Entropy — đo độ đồng nhất của phân bố điểm trong 1 nhóm

`H = -Σ p_i log(p_i)` (Shannon entropy) trên phân bố tần suất các mức điểm trong 1 nhóm thí sinh. Entropy **thấp** nghĩa là điểm số tập trung cao vào một vài giá trị (phân bố "nhọn") — có thể là tín hiệu của tính đồng nhất bất thường (vd nhiều thí sinh cùng đạt chính xác 1 mức điểm); entropy **cao** nghĩa là điểm trải đều (phân bố "phẳng", bình thường hơn với cỡ mẫu lớn). Dùng làm một trong các đặc trưng đầu vào cho Isolation Forest/LOF ở cấp nhóm thí sinh.

# Luật kết hợp (Association Rule Mining)

Áp dụng trong: `src/association.py`, `notebooks/03_association_rules.ipynb` (RQ1).

## 1. Bài toán: Frequent Itemset Mining

Cho một tập giao dịch (transactions), mỗi giao dịch là một tập con các *item*. Mục tiêu: tìm các tập item (itemset) xuất hiện đủ thường xuyên (≥ `min_support`), rồi từ đó sinh ra các **luật** dạng `Antecedent (A) ⇒ Consequent (C)` đủ "đáng tin" (≥ `min_confidence`).

Trong dự án: **giao dịch = 1 thí sinh**, **item** = `Chon_<Mon>` (đã chọn thi môn tự chọn đó) hoặc `<Mon>_<Muc>` (mức điểm rời rạc hóa của môn đã thi). Xem `src/features.build_transactions_df`.

## 2. Ba độ đo cốt lõi

Cho luật `A ⇒ C`, với N = tổng số giao dịch:

- **Support(A⇒C)** = P(A ∩ C) = (số giao dịch chứa cả A và C) / N — đo "luật này phổ biến đến đâu".
- **Confidence(A⇒C)** = P(C | A) = Support(A∪C) / Support(A) — đo "khi có A thì xác suất có C là bao nhiêu".
- **Lift(A⇒C)** = Confidence(A⇒C) / Support(C) = P(C|A) / P(C) — đo "có A làm tăng khả năng có C bao nhiêu lần so với việc không biết gì (độc lập ngẫu nhiên)". **Lift = 1** nghĩa là A và C độc lập thống kê; **Lift > 1** nghĩa là có tương quan dương thực sự (không chỉ là trùng hợp support cao); đây là lý do dự án lọc `lift > 1` làm điều kiện bắt buộc (support/confidence cao chưa chắc đã "thú vị" nếu cả A và C vốn đã phổ biến).
- **Conviction(A⇒C)** = (1 - Support(C)) / (1 - Confidence(A⇒C)) — đo mức độ luật "gần như luôn đúng" theo hướng ngụ ý logic (giá trị càng lớn, C càng hiếm khi xảy ra mà không có A). Khác lift (đối xứng), độ đo này **không đối xứng** — phù hợp để phân biệt hướng nhân-quả tiềm năng của luật.

**Ví dụ thực tế trong dự án** (xem `03_association_rules.ipynb`): Luật `Chon_SinhHoc, Toan_Yeu ⇒ SinhHoc_Yeu` có support=1,0%, confidence=74,3%, lift=40,8 — nghĩa là trong số thí sinh *vừa* chọn thi Sinh học *vừa* yếu Toán, 74,3% cũng yếu Sinh học, và khả năng này cao gấp 40,8 lần so với tỷ lệ yếu Sinh học trung bình toàn bộ dân số — một tương quan rất mạnh, không phải ngẫu nhiên.

## 3. Apriori vs FP-Growth

### Apriori (Agrawal & Srikant, 1994)

Dựa trên tính chất **Apriori (anti-monotone)**: nếu một itemset không thường xuyên, mọi superset của nó cũng không thường xuyên. Thuật toán sinh ứng viên itemset kích thước k+1 bằng cách kết hợp các itemset thường xuyên kích thước k ("candidate generation"), rồi **quét lại toàn bộ CSDL** để đếm support của từng ứng viên, loại bỏ ứng viên dưới ngưỡng, lặp lại cho đến khi không còn ứng viên mới.

**Điểm yếu kinh điển:** số ứng viên có thể bùng nổ tổ hợp khi `min_support` thấp hoặc số item lớn — chi phí I/O (quét CSDL nhiều lần) tăng nhanh.

### FP-Growth (Han, Pei, Yin, 2000)

Xây **FP-tree** (Frequent Pattern tree) — một cấu trúc cây nén, chỉ cần **quét CSDL 2 lần** (lần 1 đếm support từng item đơn, lần 2 chèn giao dịch đã sắp theo tần suất giảm dần vào cây, các giao dịch chung tiền tố dùng chung nhánh cây). Sau đó khai thác itemset thường xuyên trực tiếp trên cây bằng đệ quy **chia để trị** (xây "conditional FP-tree" cho mỗi item), **không sinh ứng viên tường minh**.

**Lý thuyết dự đoán:** FP-Growth ổn định hơn khi `min_support` giảm (số itemset thường xuyên tăng), vì chi phí không phụ thuộc vào số ứng viên candidate như Apriori.

### Kết quả thực nghiệm trong dự án (quan trọng — không chỉ lý thuyết)

Trên 1.165.582 giao dịch, 58 item:

| min_support | Apriori | FP-Growth |
|---|---|---|
| 0,1 | 0,22s | 2,65s |
| 0,02 | 1,24s | 2,83s |
| 0,005 | 4,41s | 2,92s |
| 0,001 | **16,91s** | **2,94s** |

Ở ngưỡng cao, Apriori **nhanh hơn** (ít ứng viên vì chỉ 58 item, cài đặt ma trận bitwise của mlxtend hiệu quả; FP-Growth có overhead xây cây đệ quy bằng Python). Chỉ khi `min_support` đủ thấp (itemset thường xuyên bùng nổ), ưu thế lý thuyết của FP-Growth mới bộc lộ rõ. **Bài học:** lựa chọn thuật toán cần dựa trên đặc điểm dữ liệu cụ thể (số item, phân bố support), không áp dụng máy móc "FP-Growth luôn tốt hơn Apriori".

## 4. Lọc luật "hiển nhiên" (trivial rules)

Vì item có 2 loại (`Chon_<Mon>` và `<Mon>_<Muc>`) có quan hệ **logic tất định**: có điểm môn nào (`<Mon>_<Muc>`) thì chắc chắn đã chọn thi môn đó (`Chon_<Mon>`) — luật `<Mon>_<Muc> ⇒ Chon_<Mon>` luôn có confidence=100% nhưng không mang thông tin khai phá mới. Dự án lọc bỏ các luật này (`src/association._is_trivial_rule`) để tập luật còn lại thực sự phản ánh quan hệ *được khai phá*, không phải quan hệ định nghĩa sẵn trong dữ liệu.

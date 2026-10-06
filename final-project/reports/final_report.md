# Khai phá dữ liệu điểm thi tốt nghiệp THPT Việt Nam 2026: Luật kết hợp, Phân cụm tỉnh thành và Phát hiện bất thường

**Tác giả:** Phạm Ngọc Hòa

*Dự án Data Mining, thực hiện theo quy trình CRISP-DM đầy đủ (6 giai đoạn). Toàn bộ số liệu trong báo cáo được tính trực tiếp từ dữ liệu thật qua các notebook trong `notebooks/`, có thể chạy lại để tái lập.*

---

## 1. Giới thiệu và Business Understanding

### 1.1 Bối cảnh

Kỳ thi tốt nghiệp THPT là kỳ thi quốc gia quy mô lớn nhất Việt Nam, vừa dùng để xét tốt nghiệp THPT vừa là căn cứ chính để các trường đại học, cao đẳng xét tuyển đầu vào thông qua các tổ hợp môn (khối thi). Dữ liệu điểm thi vì vậy mang đặc tính của một bài toán **giáo dục/khảo thí (education analytics)**: hành vi lựa chọn môn học của hơn một triệu thí sinh, cấu trúc phân cấp theo địa lý (tỉnh/thành → điểm thi → thí sinh), và yêu cầu giám sát chất lượng/tính liêm chính của một quy trình đánh giá diện rộng.

Từ năm 2025, kỳ thi THPT áp dụng theo Chương trình giáo dục phổ thông 2018: mỗi thí sinh thi **2 môn bắt buộc** (Toán, Ngữ văn) và **2 môn tự chọn** trong số 9 môn (Vật lý, Hóa học, Sinh học, Lịch sử, Địa lý, Giáo dục Kinh tế – Pháp luật, Tin học, Công nghệ – Công nghiệp, Công nghệ – Nông nghiệp); Ngoại ngữ không còn là môn bắt buộc mà trở thành một lựa chọn trong nhóm môn tự chọn. Cơ cấu "2 bắt buộc + 2 tự chọn trong N" khiến dữ liệu điểm thi có cấu trúc tương tự **dữ liệu giỏ hàng (market basket)**: mỗi thí sinh là một "giao dịch", mỗi môn đã thi (kèm mức điểm) là một "mặt hàng".

Năm 2026 cũng là năm đầu tiên kỳ thi được tổ chức sau khi sáp nhập đơn vị hành chính cấp tỉnh, cả nước còn **34 tỉnh/thành phố** thay vì 63 như trước — dữ liệu điểm theo tỉnh mới này chưa từng được phân tích, nên việc phân cụm các tỉnh theo đặc điểm điểm thi là một góc nhìn hoàn toàn mới, có giá trị tham khảo cho công tác quản lý giáo dục vùng.

Dữ liệu sử dụng trong dự án: **1.208.863 thí sinh** trên toàn quốc, thu thập từ trang tra cứu điểm công khai (xem mục 2 — Dataset Description và `reports/decisions_log.md`).

### 1.2 Bài toán nghiệp vụ (Business Challenge)

Các đơn vị quản lý giáo dục (Bộ GD&ĐT, Sở GD&ĐT các tỉnh) và các trường đại học hiện thiếu một bức tranh tổng hợp, dựa trên dữ liệu, trả lời ba câu hỏi vận hành cơ bản sau mỗi kỳ thi:

1. **Thí sinh đang chọn tổ hợp môn nào, và các môn đó tương quan với nhau ra sao?** — phục vụ công tác tư vấn hướng nghiệp, dự báo nhu cầu tổ hợp xét tuyển, và điều chỉnh phân bổ giáo viên/phòng thi theo môn tự chọn.
2. **Các tỉnh/thành có khác biệt có hệ thống về đặc điểm điểm thi không, và khác biệt đó biểu hiện như thế nào?** — phục vụ phân bổ nguồn lực hỗ trợ giáo dục vùng, xác định nhóm tỉnh cần ưu tiên đầu tư.
3. **Có đơn vị (tỉnh, điểm thi) nào có phân bố điểm bất thường về mặt thống kê, cần được rà soát thêm không?** — phục vụ công tác giám sát chất lượng kỳ thi.

Đây không phải bài toán dự đoán (predictive) mà là bài toán **khám phá cấu trúc và hành vi** từ dữ liệu — đúng trọng tâm của dự án: phát hiện mẫu hình (pattern discovery), không chỉ dự báo kết quả.

### 1.3 Mục tiêu khai phá dữ liệu (Data Mining Objective)

Dự án áp dụng ba kỹ thuật khai phá dữ liệu, trong đó có ít nhất một kỹ thuật không giám sát (unsupervised), ánh xạ trực tiếp với 3 câu hỏi nghiên cứu:

| RQ | Kỹ thuật | Loại | Vì sao phù hợp |
|---|---|---|---|
| RQ1 | **Luật kết hợp** (Apriori / FP-Growth) | Pattern-based | Dữ liệu môn thi + mức điểm có cấu trúc giao dịch tự nhiên (2 bắt buộc + 2 tự chọn/9 môn); luật kết hợp phát hiện trực tiếp các tổ hợp môn/mức điểm hay đi cùng nhau mà không cần giả định trước về khối thi nào "nên" tương quan. |
| RQ2 | **Phân cụm** (K-Means, Hierarchical/Ward, DBSCAN hoặc GMM) | Unsupervised | 34 tỉnh là các đối tượng chưa có nhãn nhóm trước; phân cụm giúp phát hiện cấu trúc tự nhiên (tỉnh nào giống tỉnh nào) thay vì áp đặt phân loại hành chính (vùng miền) có sẵn. |
| RQ3 | **Phát hiện bất thường** (Z-score/IQR, Isolation Forest, LOF) | Unsupervised | Không có nhãn "gian lận/bất thường" đúng (ground truth), nên cần phương pháp không giám sát; kết hợp nhiều phương pháp để tăng độ tin cậy khi không có nhãn đối chiếu. |

Việc dùng cả 3 kỹ thuật giúp dự án khai thác dữ liệu từ ba góc độ bổ sung nhau: **quan hệ giữa các môn** (RQ1, cấp thí sinh), **cấu trúc giữa các tỉnh** (RQ2, cấp tỉnh), **điểm dị thường trong phân bố** (RQ3, cấp điểm thi) — cùng một bộ dữ liệu nhưng ba đơn vị phân tích (unit of analysis) khác nhau.

### 1.4 Giá trị nghiệp vụ (Business Value)

- **RQ1 → Tư vấn hướng nghiệp & quy hoạch tổ hợp xét tuyển:** các trường THPT và trung tâm tư vấn có thể dùng luật kết hợp để tư vấn tổ hợp môn phù hợp năng lực; các trường đại học có thể đối chiếu độ phổ biến tổ hợp môn với chỉ tiêu tuyển sinh theo khối.
- **RQ2 → Phân bổ nguồn lực giáo dục vùng:** nhóm tỉnh có đặc điểm tương đồng (vd điểm trung bình thấp, tỷ lệ chọn môn tự nhiên thấp) là cơ sở để Bộ/Sở GD&ĐT ưu tiên đầu tư đồng loạt thay vì xử lý từng tỉnh riêng lẻ.
- **RQ3 → Cơ chế giám sát chất lượng kỳ thi:** danh sách điểm thi/tỉnh có chỉ số bất thường thống kê là đầu vào để đơn vị có thẩm quyền **xem xét thêm** (không phải kết luận), giúp tập trung nguồn lực thanh tra, kiểm tra vào đúng nơi có tín hiệu đáng chú ý thay vì rà soát dàn trải.

### 1.5 Tiêu chí thành công

| RQ | Tiêu chí thành công (đo được) |
|---|---|
| RQ1 | Sinh được tối thiểu 10 luật kết hợp có **lift > 1,2** và **confidence > 0,5**, sau khi loại các luật hiển nhiên (vd suy ra trực tiếp từ định nghĩa môn bắt buộc); mỗi luật diễn giải được bằng ngôn ngữ nghiệp vụ. |
| RQ2 | Giải pháp phân cụm cuối cùng đạt **Silhouette score > 0,3** (dấu hiệu cụm tách biệt hợp lý ở dữ liệu cấp tỉnh, n=34 nên không kỳ vọng mức cao như dữ liệu lớn), đồng thời mỗi cụm phải mô tả được bằng đặc trưng cụ thể, khác biệt rõ với cụm khác. |
| RQ3 | Tối thiểu 2 phương pháp phát hiện bất thường đạt **độ đồng thuận (Jaccard) ≥ 0,5** trên top-N đơn vị bất thường nhất, và kết quả ổn định (thứ hạng không đổi quá nhiều) khi thay đổi tham số/định nghĩa nhóm — phản ánh tín hiệu bất thường là thực, không phải nhiễu do lựa chọn tham số. |

### 1.6 Giả định (Assumptions)

1. Dữ liệu đã qua xử lý loại trùng SBD bởi người thu thập (sẽ kiểm tra lại ở GIAI ĐOẠN 2).
2. Ô điểm trống tương ứng với "thí sinh không đăng ký thi môn đó", không phải lỗi thu thập — giả định này sẽ được kiểm chứng bằng cách đối chiếu số môn thi mỗi thí sinh với quy định 4 môn (2 bắt buộc + 2 tự chọn) ở GIAI ĐOẠN 2.
3. Cấu trúc 3 chữ số giữa của SBD tương ứng với "mã điểm thi" (theo quan sát của tác giả dữ liệu gốc, xem `decisions_log.md` DEC-003) — dùng làm đơn vị nhóm cấp "điểm thi" cho RQ3, có kiểm tra độ nhạy với cách nhóm khác.
4. Mã tỉnh trong dữ liệu phản ánh đúng tỉnh **nơi thí sinh dự thi**, không nhất thiết là tỉnh thường trú — phù hợp với mục tiêu phân tích "đặc điểm điểm thi theo địa bàn tổ chức thi" chứ không phải theo nơi cư trú.

### 1.7 Hạn chế (Limitations)

1. **Nguồn dữ liệu không chính thức:** Dữ liệu thu thập từ trang tra cứu công khai của một đơn vị báo chí (VietnamNet, theo mô tả gốc), không phải dữ liệu công bố chính thức từ Bộ GD&ĐT — có thể thiếu một số thí sinh (SBD không liên tục, bị tra cứu lỗi) hoặc có sai số thu thập.
2. **Không có thông tin nhân khẩu học:** Không có giới tính, loại hình trường, khu vực ưu tiên, điểm cư trú — hạn chế khả năng diễn giải nguyên nhân sâu xa của các mẫu hình phát hiện được (chỉ mô tả "có tương quan", không khẳng định "nguyên nhân").
3. **Không có ground truth cho bất thường:** Không có danh sách xác nhận gian lận/sai sót để đánh giá độ chính xác (precision/recall) của mô hình phát hiện bất thường; chỉ đánh giá được bằng độ đồng thuận và độ ổn định giữa các phương pháp.
4. **Giả định về đơn vị "điểm thi"** dựa trên suy luận cấu trúc SBD của bên thứ ba, chưa được xác nhận chính thức (xem mục 1.6, giả định 3).
5. **Phạm vi một năm:** Phân tích chính tập trung vào năm 2026; phần so sánh với 2025 (mục bonus) chỉ mang tính minh họa xu hướng, không đủ dữ liệu chuỗi thời gian để kết luận xu hướng dài hạn.
6. **Đạo đức dữ liệu:** Không có nỗ lực liên kết SBD với danh tính cá nhân thí sinh; mọi kết luận về bất thường được diễn đạt là "bất thường về mặt thống kê, cần xem xét thêm", không quy kết gian lận hay trách nhiệm cho bất kỳ đơn vị cụ thể nào.

---

## 2. Mô tả dữ liệu (Dataset Description)

**Nguồn dữ liệu:** `sdgedfegw/du-lieu-diem-thi` (GitHub, lưu qua Git LFS) — dùng thay cho repo "chính" được đề xuất ban đầu vì repo đó không có file CSV tải được (xem `decisions_log.md`, DEC-001). Dữ liệu gốc do bên thứ ba thu thập từ trang tra cứu điểm công khai, **không phải công bố chính thức của Bộ GD&ĐT**.

**Kích thước:** 1.208.863 thí sinh × 18 cột gốc (mở rộng thành 27 cột sau khi đổi tên và suy ra `province_name`), dung lượng ~133MB khi nạp vào bộ nhớ với dtype tối ưu (float32/category), file CSV thô ~79MB.

**Loại thuộc tính:**
- Định danh: `sbd` (string, 8 ký tự), `province_code`/`province_name` (34 tỉnh/thành sau sáp nhập 2025).
- Số liên tục: 12 cột điểm môn thi (thang 0–10) + `tong_diem` (thang 0–40) + 8 cột điểm tổ hợp khối thi có sẵn (thang 0–30).
- Phân loại: `ma_mon_ngoai_ngu` (7 giá trị).

**Bối cảnh thu thập:** Thu thập ngày 01/07/2026 ngay sau khi công bố điểm, qua scraper tự động tra cứu theo SBD — nghĩa là dữ liệu phản ánh kết quả thi gốc, chưa cộng điểm ưu tiên/khuyến khích xét tốt nghiệp.

Chi tiết từng cột, miền giá trị, và các phát hiện chất lượng dữ liệu: xem `reports/data_dictionary.md`.

## 3. Tiền xử lý dữ liệu (Data Pre-processing)

*(Notebook đầy đủ: `notebooks/02_data_preparation.ipynb`.)*

**Lọc thí sinh chuẩn (cho bảng giao dịch):** giữ 1.165.582/1.208.863 (96,42%), loại 43.281 (3,58%) thí sinh thiếu môn bắt buộc hoặc thi không đủ 4 môn — lý do: GIAI ĐOẠN 2 xác nhận nhóm này có hồ sơ thi khác thường, giữ lại sẽ làm nhiễu luật kết hợp (DEC-005). Các bảng đặc trưng cấp tỉnh/điểm thi vẫn dùng toàn bộ 1.208.863 thí sinh vì không yêu cầu đủ 4 môn.

**Rời rạc hóa điểm (feature transformation):** 4 mức Yếu(<5)/Trung bình(5–6,5)/Khá(6,5–8)/Giỏi(≥8) theo quy ước giáo dục phổ thông VN, chọn thay vì tứ phân vị thống kê để luật kết hợp dễ diễn giải với đối tượng nghiệp vụ và ổn định khi so sánh đa năm (DEC-006).

**Xây dựng giao dịch (transaction construction):** 1.165.582 giao dịch × 58 item khác nhau (10 item "đã chọn môn" + 48 item "môn×mức điểm"), lưu one-hot dạng boolean tại `data/processed/transactions_onehot.parquet`.

**Đặc trưng cấp tỉnh (aggregation):** 34 dòng × 70 đặc trưng số (mean/median/std/%giỏi/%yếu mỗi môn + %chọn mỗi môn tự chọn), chuẩn hóa StandardScaler (`province_features_scaled.parquet`) để không môn có phương sai lớn (vd Toán) lấn át môn phương sai nhỏ khi phân cụm.

**Đặc trưng cấp "điểm thi" (aggregation + feature engineering):** nhóm theo 3 chữ số giữa của SBD → 1.237 nhóm (trung vị 996 thí sinh/nhóm — thực chất là khối 1.000 SBD liên tiếp, xem hiệu chỉnh DEC-007), với mean/std/chênh lệch so với TB tỉnh/tỷ lệ trùng điểm mode/entropy mỗi môn. Bổ sung 3 phương án cửa sổ trượt (24/50/100 SBD) làm phân tích độ nhạy, vì nhóm theo SBD khối nghìn có thể quá thô so với quy mô phòng thi thật.

Tất cả lưu dạng Parquet trong `data/processed/` (không ghi đè `data/raw/`), đúng nguyên tắc tái lập của dự án.

## 4. Phân tích khám phá và khai phá mô tả (Exploratory & Descriptive Mining)

*(Notebook đầy đủ: `notebooks/01_data_understanding.ipynb`. Tóm tắt phát hiện chính:)*

1. **Chất lượng kỹ thuật tốt:** 0 dòng SBD trùng lặp, 0 dòng SBD không khớp cấu trúc `province_code(2) + sbd_seq(6)`, 0 dòng điểm ngoài khoảng [0, 10].
2. **Giả định "bước điểm 0,25 cố định" không đúng với đa số môn:** chỉ Ngữ văn bám lưới 0,25 (99,6%); các môn còn lại (Toán, Lý, Sử, Địa...) lệch 14–99% do đề 2026 có câu hỏi đúng/sai chấm điểm mịn hơn — xem DEC-004.
3. **Phân biệt "không thi" vs "thiếu dữ liệu":** 96,42% thí sinh thi đúng 4 môn (2 bắt buộc + 2 tự chọn); trong nhóm đó 100% có đúng 2 môn tự chọn — xác nhận ô trống ở môn tự chọn là lựa chọn không thi, không phải lỗi. 3,58% còn lại thiếu môn bắt buộc hoặc thi <4 môn, xử lý riêng ở GIAI ĐOẠN 3 (DEC-005).
4. **Tương quan giữa các môn có cấu trúc Tự nhiên/Xã hội rõ rệt:** Toán–Sinh 0,76, Toán–Lý 0,73, Toán–Hóa 0,71 (khối Tự nhiên); Văn–Địa 0,55, Văn–Sử 0,53 (khối Xã hội). Dùng làm đường cơ sở diễn giải luật kết hợp ở mục 5.
5. **Tổ hợp môn tự chọn phổ biến nhất:** Địa lý + Lịch sử (277.309 thí sinh), Hóa học + Vật lý (175.249) — phản ánh ranh giới truyền thống Xã hội/Tự nhiên vẫn chi phối lựa chọn dù chương trình mới cho tự do kết hợp.
6. **Xác nhận hiện tượng dồn điểm Ngữ văn = 5,0:** 49.195 thí sinh đạt đúng 5,0, cao hơn 1,54× so với trung bình nội suy từ điểm lân cận (4,75 và 5,25) — khớp với quan sát đã công bố của bên thu thập dữ liệu gốc. Đây là tín hiệu đầu vào cho GIAI ĐOẠN 4.3, **không phải kết luận**.

Hình minh họa: `reports/figures/02_*.png` (phổ điểm, ma trận tương quan, top tổ hợp môn, phân bố điểm Toán theo tỉnh).

## 5. Phương pháp và kết quả khai phá dữ liệu (Data Mining Methods and Results)

### 5.1 Luật kết hợp — RQ1 (`notebooks/03_association_rules.ipynb`)

**Vì sao chọn phương pháp:** dữ liệu môn thi có cấu trúc giao dịch tự nhiên (2 môn bắt buộc + 2/9 môn tự chọn); FP-Growth phù hợp vì không cần giả định trước tổ hợp nào "nên" liên quan, khai thác trực tiếp từ dữ liệu.

**Ý tưởng thuật toán:** Apriori sinh ứng viên itemset k+1 từ itemset k thường xuyên rồi quét lại dữ liệu đếm support (tốn kém khi min_support thấp); FP-Growth nén dữ liệu thành FP-tree, chỉ quét 2 lần, khai thác itemset bằng đệ quy chia-để-trị, không sinh ứng viên tường minh.

**So sánh hiệu năng thực nghiệm (1.165.582 giao dịch, 58 item):** ở min_support cao (≥0,02), Apriori nhanh hơn FP-Growth (ít ứng viên do chỉ 58 item, cài đặt ma trận bitwise của mlxtend hiệu quả). Từ min_support=0,005 trở xuống, Apriori chậm dần theo cấp số nhân (4,4s → 16,9s khi min_support: 0,005→0,001) trong khi FP-Growth gần như không đổi (~2,9s) — ưu điểm FP-Growth chỉ bộc lộ rõ khi mật độ itemset thường xuyên đủ lớn.

**Tham số cuối cùng:** min_support=0,01, min_confidence=0,6, min_lift=1,0 (loại luật hiển nhiên dạng "có điểm môn X ⇒ đã chọn môn X"). Kết quả: **479 luật** sau lọc — vượt xa tiêu chí thành công (≥10 luật, mục 1.5).

**Luật nổi bật:**
| Luật | Support | Confidence | Lift |
|---|---|---|---|
| Chọn Sinh + Toán Yếu ⇒ Sinh Yếu | 1,0% | 74,3% | 40,8 |
| Chọn Địa+GDKTPL + Văn Yếu ⇒ Địa Yếu, GDKTPL Yếu | 1,1% | 68,4% | 19,6 |
| Chọn Hóa + Toán Giỏi + Lý Giỏi ⇒ Hóa Giỏi | 1,1% | 64,7% | 17,6 |
| Chọn Sử+Lý + Toán Yếu ⇒ Lý Yếu | 1,1% | 94,6% | 7,4 |

**Diễn giải:** mẫu hình nổi bật nhất là các luật liên kết mức "Yếu" lan xuyên nhiều môn/khối (khó khăn học tập có tính hệ thống, không cục bộ 1 môn); luật liên kết mức "Giỏi" tập trung ở khối A truyền thống (Toán-Lý-Hóa), phản ánh tính đồng nhất năng lực trong nhóm khá giỏi.

### 5.2 Phân cụm tỉnh — RQ2 (`notebooks/04_clustering_provinces.ipynb`)

**Vì sao chọn phương pháp:** 34 tỉnh chưa có nhãn nhóm trước; phân cụm phát hiện cấu trúc tự nhiên thay vì áp đặt phân vùng hành chính có sẵn.

**Vấn đề gặp phải:** 70 đặc trưng/34 mẫu gây "curse of dimensionality" — Silhouette tối đa trên không gian gốc chỉ 0,259 (dưới ngưỡng thành công 0,3). **Giải pháp:** giảm chiều bằng PCA còn 5 thành phần chính (giữ 77,5% phương sai) trước khi phân cụm (DEC-008) — Silhouette tăng lên 0,357 tại k=4.

**Kết quả 3 thuật toán (k=4, không gian PCA-5):**
| Thuật toán | Silhouette | Ghi chú |
|---|---|---|
| K-Means | **0,357** | Thuật toán chính, đạt tiêu chí thành công |
| Hierarchical (Ward) | 0,345 | Đồng thuận cao với K-Means (ARI=0,84) |
| Gaussian Mixture | 0,297 | Ranh giới mềm hơn, đồng thuận thấp hơn (ARI=0,63) |
| DBSCAN (thử nghiệm) | 0,50+ nhưng... | Tới 23/34 tỉnh bị coi là nhiễu ở eps cho Silhouette cao nhất — không phù hợp vì dữ liệu biến thiên liên tục, không có khoảng trống mật độ |

**Chân dung 4 cụm (K-Means):**
1. **Miền núi phía Bắc** (Cao Bằng, Lai Châu, Lào Cai, Lạng Sơn, Sơn La, Điện Biên): Toán TB 4,65 (thấp nhất), 62% yếu Toán, quy mô nhỏ nhất (~10.357 thí sinh/tỉnh).
2. **Đô thị lớn & đồng bằng Bắc Bộ** (Hà Nội, TP.HCM, Hải Phòng, Bắc Ninh, Huế, Hà Tĩnh, Hưng Yên, Nghệ An, Ninh Bình, Phú Thọ, Quảng Ninh, Thanh Hóa): Toán TB 5,89 (cao nhất), quy mô đông nhất (~53.632/tỉnh).
3. **Nam Bộ/ĐBSCL** (An Giang, Cà Mau, Cần Thơ, Lâm Đồng, Tây Ninh, Vĩnh Long, Đồng Nai, Đồng Tháp): tỷ lệ chọn Vật lý (33%)/Hóa học (24%) cao nhất.
4. **Trung Bộ & Tây Nguyên** (Gia Lai, Khánh Hòa, Quảng Ngãi, Quảng Trị, Thái Nguyên, Tuyên Quang, Đà Nẵng, Đắk Lắk): các chỉ số ở mức trung bình.

4 cụm phát hiện hoàn toàn tự động (không đưa nhãn vùng miền trước) nhưng có **tính địa lý rõ rệt**, gần trùng phân vùng kinh tế - địa lý truyền thống — gợi ý đặc điểm điểm thi phản ánh chênh lệch phát triển kinh tế-giáo dục theo vùng.

### 5.3 Phát hiện bất thường — RQ3 (`notebooks/05_anomaly_detection.ipynb`)

**Vì sao chọn phương pháp:** không có ground-truth "gian lận" đúng, nên cần phương pháp không giám sát; kết hợp nhiều phương pháp (thống kê + học máy) để tăng độ tin cậy khi không có nhãn đối chiếu.

**Kiểm định heaping (Ngữ văn=5,0) theo tỉnh:** mức độ dồn điểm không đồng đều — cao nhất Lâm Đồng (2,61×), Đồng Nai (2,30×), Cà Mau (2,12×); gần như không có ở Sơn La, Hưng Yên, Bắc Ninh, Hà Nội (~1,0×). Diễn giải: khả năng phản ánh xu hướng làm tròn điểm quanh mốc xét tốt nghiệp của người chấm — **tín hiệu mô tả, không phải bằng chứng gian lận**.

**Baseline Z-score/IQR:** áp dụng trực tiếp lên điểm cá nhân không phát hiện gì (0 thí sinh |z|>3 — biến thiên điểm cá nhân quá hẹp). Áp dụng lên đặc trưng tổng hợp cấp nhóm (chênh lệch điểm TB nhóm so với tỉnh) mới có ý nghĩa.

**Isolation Forest + LOF** (8 đặc trưng Toán/Văn luôn đầy đủ dữ liệu, 1.237 nhóm "site_id"): Jaccard đồng thuận top-30 giữa 2 phương pháp = 0,32–0,36 (16/44 nhóm trùng nhau) — đạt nhưng không vượt xa tiêu chí 0,5 đề ra ở mục 1.5, cho thấy 2 phương pháp bắt tín hiệu hơi khác nhau (bổ sung nhau hơn là trùng lặp). Độ ổn định theo tham số `contamination`: Jaccard=1,0 ở mọi mức (0,01–0,1) — tập top-30 rất ổn định về xếp hạng.

**Độ nhạy theo định nghĩa nhóm:** so sánh site_id (khối ~1.000 SBD) với cửa sổ trượt 24/50/100 SBD — đồng thuận cấp tỉnh tăng khi cửa sổ tiệm cận quy mô site_id (Jaccard tỉnh: 0,28 ở cửa sổ 24 → 0,57 ở cửa sổ 100). **Kết luận quan trọng:** kết quả phụ thuộc đáng kể vào đơn vị nhóm được chọn — hạn chế cần nêu khi diễn giải.

**Case study đáng chú ý:** 2 nhóm `25-000`/`25-001` (Phú Thọ) được cả 2 phương pháp đồng thuận bất thường, với Toán TB 7,5+ (chênh +1,8 so với tỉnh) — **trùng khớp với chính 2 cụm mà tác giả bộ dữ liệu gốc đã quan sát thủ công và công bố** (nghi ngờ là trường chuyên, chưa xác nhận chính thức). Việc pipeline độc lập tái phát hiện đúng cụm này là một hình thức kiểm chứng chéo cho phương pháp.

**Nhắc lại nguyên tắc đạo đức:** mọi phát hiện trên chỉ là tín hiệu thống kê cần xem xét thêm, không kết luận gian lận hay quy trách nhiệm cho đơn vị cụ thể.

## 6. Đánh giá và diễn giải kết quả (Evaluation and Interpretation)

*(Notebook đầy đủ: `notebooks/06_evaluation_summary.ipynb`.)*

| RQ | Tiêu chí thành công | Kết quả thực tế | Đạt? |
|---|---|---|---|
| RQ1 — Luật kết hợp | ≥10 luật lift>1,2 & confidence>0,5 | **479 luật** (lift>1, confidence>0,6, đã loại luật hiển nhiên) | Đạt, vượt xa |
| RQ2 — Phân cụm tỉnh | Silhouette > 0,3 | K-Means (PCA-5, k=4): **Silhouette = 0,357** | Đạt |
| RQ3 — Phát hiện bất thường | Jaccard đồng thuận ≥ 0,5 (IF vs LOF, top-N) | **Jaccard = 0,32–0,36** (top-30) | Chưa đạt ngưỡng — 2 phương pháp bổ sung hơn là trùng lặp |

**Trả lời RQ1:** Có xu hướng rõ rệt. Hai tổ hợp phổ biến nhất — Địa lý+Lịch sử (23,8%) và Vật lý+Hóa học (15,0%) — phản ánh 2 khối Xã hội/Tự nhiên truyền thống vẫn chi phối lựa chọn. Về điểm số, 479 luật cho thấy khó khăn học tập mức "Yếu" lan xuyên nhiều môn/khối, trong khi năng lực "Giỏi" đồng nhất rõ nhất ở khối Toán-Lý-Hóa.

**Trả lời RQ2:** Có. 4 cụm tỉnh phát hiện tự động (Silhouette=0,357) mang **tính địa lý-kinh tế rõ rệt**: Miền núi phía Bắc (điểm thấp nhất), Đô thị lớn & đồng bằng Bắc Bộ (điểm cao nhất), Nam Bộ/ĐBSCL (thiên Tự nhiên), Trung Bộ & Tây Nguyên (trung bình). Hierarchical (Ward) xác nhận cấu trúc này (ARI=0,84 so với K-Means).

**Trả lời RQ3:** Có tín hiệu đáng chú ý nhưng đồng thuận giữa phương pháp ở mức vừa phải, và **phụ thuộc đáng kể vào cách định nghĩa đơn vị nhóm**. Phát hiện tin cậy nhất: case Phú Thọ (2 nhóm), được cả Isolation Forest, LOF, **và tác giả dữ liệu gốc (độc lập)** cùng xác định — kiểm chứng chéo hiếm có.

**So sánh ưu/nhược điểm 3 phương pháp:**

| Tiêu chí | Luật kết hợp (FP-Growth) | Phân cụm (K-Means+PCA) | Phát hiện bất thường (IF+LOF) |
|---|---|---|---|
| Chất lượng insight | Cao — luật cụ thể, định lượng (support/confidence/lift) | Cao — chân dung cụm rõ, có ý nghĩa địa lý | Trung bình — cần diễn giải thận trọng, không có ground-truth |
| Khả năng mở rộng (scalability) | Tốt (FP-Growth xử lý 1,17 triệu giao dịch trong ~3s) | Hạn chế bởi số tỉnh (n=34), không phải bởi thuật toán | Tốt (IF/LOF đều scale tuyến tính~gần tuyến tính) |
| Khả năng diễn giải | Rất cao (luật dạng "nếu...thì...") | Cao sau khi profiling, nhưng PCA làm giảm trực quan truớc khi mapping ngược | Trung bình (điểm số IF/LOF trừu tượng, cần quy đổi về đặc trưng gốc) |
| Tính thực tiễn | Trực tiếp dùng cho tư vấn hướng nghiệp | Trực tiếp dùng cho phân bổ nguồn lực vùng | Cần con người xác minh thêm trước khi hành động |

## 7. Insight và khuyến nghị nghiệp vụ (Business Insights and Recommendations)

**Insight 1 (từ RQ1):** Lựa chọn tổ hợp môn vẫn phân cực mạnh theo 2 khối Xã hội/Tự nhiên truyền thống dù chương trình 2018 cho tự do kết hợp — hệ thống tư vấn hướng nghiệp hiện tại có thể chưa khai thác hết không gian lựa chọn mới. → **Khuyến nghị:** Trường THPT/trung tâm tư vấn nên chủ động giới thiệu các tổ hợp "phi truyền thống" (vd Lý+Ngoại ngữ đã chiếm 12,1%) cho thí sinh có năng lực phù hợp nhưng chưa được định hướng, mở rộng lựa chọn nghề nghiệp.

**Insight 2 (từ RQ1):** Yếu kém học tập có tính lan tỏa xuyên môn (lift tới 40,8) — thí sinh yếu 1 môn nền tảng (Toán/Văn) có xác suất rất cao yếu cả môn tự chọn liên quan. → **Khuyến nghị:** Chương trình phụ đạo nên ưu tiên củng cố môn nền tảng (Toán, Văn) sớm thay vì chỉ tập trung vào môn thi tự chọn cuối cấp — hiệu quả lan tỏa cao hơn.

**Insight 3 (từ RQ2):** 4 cụm tỉnh tự động phát hiện trùng khớp cao với phân vùng kinh tế-địa lý — chênh lệch điểm Toán trung bình giữa cụm cao nhất và thấp nhất là 1,24 điểm/10, khoảng cách đáng kể. → **Khuyến nghị:** Bộ/Sở GD&ĐT ưu tiên phân bổ nguồn lực (giáo viên giỏi, cơ sở vật chất, chương trình hỗ trợ) theo **nhóm cụm** (6 tỉnh miền núi phía Bắc) thay vì rải đều, và dùng cụm "Đô thị lớn" làm chuẩn tham chiếu khi đặt mục tiêu cải thiện.

**Insight 4 (từ RQ3):** Mức độ dồn điểm Văn=5,0 khác biệt rất lớn giữa tỉnh (1,0×–2,6×) — không phải hiện tượng đồng đều toàn quốc. → **Khuyến nghị (cơ chế giám sát):** Thiết lập chỉ số "tỷ lệ dồn điểm tại ngưỡng xét tốt nghiệp" theo tỉnh làm một trong các chỉ báo giám sát định kỳ hậu kỳ thi — không phải để quy kết, mà để **ưu tiên nguồn lực rà soát/tập huấn chấm thi** vào nơi có tín hiệu cao nhất, hiệu quả hơn rà soát dàn trải.

**Insight 5 (từ RQ3):** Phương pháp tự động tái phát hiện đúng case bất thường mà tác giả dữ liệu gốc từng quan sát thủ công (Phú Thọ) — chứng minh tính khả thi của giám sát tự động. → **Khuyến nghị:** Xây dựng quy trình giám sát bán tự động: chạy Isolation Forest/LOF định kỳ trên dữ liệu điểm thi, đưa ra danh sách "cần xem xét thêm" cho đơn vị thanh tra — giảm tải rà soát thủ công, với điều kiện **luôn có bước xác minh của con người** trước khi đi đến bất kỳ hành động nào.

## 8. (Bonus) Kỹ thuật nâng cao — Giảm chiều & So sánh đa năm

*(Notebook: `notebooks/04_clustering_provinces.ipynb` mục 4.2.1 và `notebooks/06_evaluation_summary.ipynb` mục 8.)*

**Giảm chiều (PCA) để khám phá cấu trúc (DEC-008):** không chỉ dùng PCA để trực quan hóa 2D, mà dùng chủ động để **giải quyết curse of dimensionality** (70 đặc trưng/34 mẫu) — nâng Silhouette từ 0,259 (70 chiều gốc) lên 0,357 (5 thành phần chính, 77,5% phương sai). Đây là ví dụ cụ thể giảm chiều giúp **cải thiện khả năng diễn giải cấu trúc**, không chỉ cải thiện "hiệu năng" mô hình.

**So sánh 2026 vs 2025 (cấp quốc gia, do bất tương thích mã tỉnh — DEC-009):**
- Điểm Toán trung bình tăng 4,78→5,65 (+0,87); Ngữ văn giảm nhẹ 7,00→6,50 — nhiều khả năng do độ khó đề thi khác nhau giữa 2 năm, không kết luận về năng lực.
- Thứ hạng tổ hợp môn tự chọn phổ biến **ổn định** qua 2 năm (Lịch sử+Địa lý #1, Vật lý+Hóa học #2).
- Mẫu hình luật kết hợp **nhất quán**: cụm Toán-Lý-Hóa luôn có lift cao nhất ở cả 2 năm (17-26 cho "giỏi cùng nhau", 10-11 cho "yếu cùng nhau").
- **Giá trị của so sánh:** phân biệt được điều gì **ổn định về cấu trúc** (tương quan môn, thứ hạng tổ hợp) với điều gì **biến động theo năm** (mức điểm tuyệt đối) — mức hiểu sâu hơn phân tích 1 năm đơn lẻ.

## Tài liệu tham khảo

1. Dữ liệu điểm thi THPT 2026: `sdgedfegw/du-lieu-diem-thi` (GitHub, Git LFS). https://github.com/sdgedfegw/du-lieu-diem-thi — dùng thay cho nguồn "chính" `TruongThuHa/diem_thi_thptqg-2026-` (https://github.com/TruongThuHa/diem_thi_thptqg-2026-) không có CSV tải được, xem DEC-001.
2. Dữ liệu điểm thi THPT 2025 (chương trình GDPT 2018): cùng repo `sdgedfegw/du-lieu-diem-thi`, file `du-lieu-diem-thi-2025-ct2018.csv`.
3. mlxtend — Raschka, S. (2018). *MLxtend: Providing machine learning and data science utilities and extensions to Python's scientific computing stack.* Journal of Open Source Software.
4. scikit-learn — Pedregosa et al. (2011). *Scikit-learn: Machine Learning in Python.* JMLR 12, pp. 2825-2830.
5. Han, J., Kamber, M., & Pei, J. *Data Mining: Concepts and Techniques* (3rd ed.) — tham khảo lý thuyết Apriori/FP-Growth/K-Means/DBSCAN/Isolation Forest/LOF, dùng xuyên suốt tài liệu `docs/`.

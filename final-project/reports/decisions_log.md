# Nhật ký quyết định xử lý dữ liệu

Mỗi mục ghi lại một quyết định có ảnh hưởng đến dữ liệu hoặc kết quả, kèm lý do và bằng chứng. Đánh số tuần tự `DEC-xxx`.

---

## DEC-001 — Đổi nguồn dữ liệu chính thức sang repo "mở rộng"

**Giai đoạn:** 0 — Khởi tạo **Ngày:** 2026-10-05

**Vấn đề:** Repo "chính" được chỉ định trong đề bài (`https://github.com/TruongThuHa/diem_thi_thptqg-2026-`) có README mô tả đầy đủ bộ dữ liệu (1.200.202 thí sinh, 34 tỉnh/thành, file toàn quốc + 34 file theo tỉnh), nhưng khi kiểm tra thực tế qua GitHub API (`/contents`, `/git/trees`), thư mục `data/` trong repo **không phải là một thư mục** mà là một **file đơn lẻ tên `data`** chứa nội dung của một script Python (`prep_diemthi_2026.py`) — rõ ràng là lỗi thao tác `git add` của tác giả gốc (add nhầm file thay vì thư mục). Tương tự với `scraper` và `scripts`. Không có file CSV nào truy cập được qua `raw.githubusercontent.com` (xác nhận bằng HTTP 404 trên đường dẫn `data/diem_thi_thptqg_2026_all.csv`).

**Quyết định:** Dùng repo "mở rộng" (`https://github.com/sdgedfegw/du-lieu-diem-thi`) làm **nguồn dữ liệu chính thức duy nhất**. Repo này lưu CSV qua Git LFS, tải trực tiếp (không cần xác thực) qua `https://media.githubusercontent.com/media/sdgedfegw/du-lieu-diem-thi/main/<file>.csv`.

**Bằng chứng dữ liệu khớp nhau:** File `du_lieu_diem_thi_2026.csv` của repo mở rộng có **1.208.863 dòng** và **đúng 34 mã tỉnh** (01, 04, 08, 11, 12, 14, 15, 19, 20, 22, 24, 25, 31, 33, 37, 38, 40, 42, 44, 46, 48, 51, 52, 56, 66, 68, 75, 79, 80, 82, 86, 91, 92, 96) — khớp 100% với danh sách 34 tỉnh/thành mà repo "chính" liệt kê trong README (cùng mã số, cùng tên). Số dòng (1.208.863) rất gần với con số 1.200.202 nêu trong mô tả repo "chính" (chênh lệch ~0,7%, hợp lý vì có thể khác thời điểm cào dữ liệu/khác cách loại trùng).

**Ảnh hưởng:** Tên cột đổi từ snake_case tiếng Việt không dấu (`toan`, `ngu_van`, ...) dự kiến ban đầu sang PascalCase (`Toan`, `NguVan`, ...) theo schema thực tế của repo mở rộng — xem `reports/data_dictionary.md`. Dữ liệu còn có thêm các cột điểm tổ hợp khối thi có sẵn (KhoiA, KhoiB, ...) không có trong repo chính, có thể tận dụng làm đặc trưng bổ sung.

**Đã xác nhận với người dùng:** Có (qua AskUserQuestion, chọn phương án dùng tự động thay vì dừng lại chờ tải thủ công).

---

## DEC-002 — Tải thêm dữ liệu 2025 làm phần bonus so sánh đa năm

**Giai đoạn:** 0 — Khởi tạo **Ngày:** 2026-10-05

**Quyết định:** Tải thêm `du-lieu-diem-thi-2025-ct2018.csv` (~73MB, kỳ thi 2025 theo chương trình GDPT 2018 — gần nhất về cấu trúc môn thi với
2026) từ cùng repo mở rộng, dùng cho phân tích so sánh xu hướng điểm/tổ hợp môn 2025 vs 2026 như một kỹ thuật nâng cao bổ sung (so sánh trên các subset dữ liệu khác nhau).

**Lý do:** Phần "mở rộng, so sánh nhiều năm" vốn đã được liệt kê là tùy chọn trong yêu cầu gốc, và việc so sánh trên các subset dữ liệu khác nhau giúp phân biệt điều gì ổn định về cấu trúc với điều gì biến động theo năm. 2025-ct2018 được chọn thay vì 2025-ct2006 vì cùng chương trình giáo dục phổ thông 2018 với 2026, nên cấu trúc môn thi tự chọn (Toán+Văn+2 môn tự chọn) tương đồng nhất, giảm nhiễu khi so sánh.

**Đã xác nhận với người dùng:** Có.

---

## DEC-003 — Cấu trúc SBD dùng cho phân tích cấp điểm thi (RQ3)

**Giai đoạn:** 0 — Khởi tạo (ghi nhận trước, áp dụng ở GIAI ĐOẠN 3) **Ngày:** 2026-10-05

**Quan sát:** README của repo "chính" phân tích cấu trúc SBD dạng `[mã tỉnh 2 số] + [mã điểm thi 3 số] + [số thứ tự 3 số]`, và chỉ ra các cụm điểm thi cụ thể (vd `33000xxx`, `25000-25001xxx`) có điểm Toán trung bình vượt trội so với mặt bằng tỉnh — nhiều khả năng là trường chuyên.

**Quyết định:** Ở GIAI ĐOẠN 3, dùng **3 chữ số giữa của phần số thứ tự 6 chữ số** (`SBD_New`, sau khi trừ mã tỉnh) làm đơn vị nhóm "điểm thi" chính cho bài toán phát hiện bất thường cấp phòng/điểm thi, thay vì giả định cửa sổ ~24 SBD liên tiếp nêu trong yêu cầu gốc (vốn chỉ là ước lượng gần đúng theo quy mô phòng thi, không phản ánh ranh giới điểm thi thực tế). Vẫn giữ phương án cửa sổ trượt (24/50/100 SBD, xem `config.yaml: exam_site.sliding_window_sizes`) làm phân tích độ nhạy để đối chiếu, theo đúng yêu cầu "phải ghi rõ hạn chế này và kiểm tra độ nhạy với các kích thước nhóm khác".

**Hạn chế:** Quy tắc "3 số giữa = mã điểm thi" là suy luận từ quan sát của tác giả repo gốc trên vài cụm cụ thể, chưa có xác nhận chính thức từ đơn vị tổ chức thi. Sẽ nêu rõ hạn chế này trong `final_report.md`.

---

## DEC-004 — Bỏ giả định "bước điểm 0,25 cố định"

**Giai đoạn:** 2 — Data Understanding **Ngày:** 2026-10-06

**Vấn đề:** Yêu cầu gốc đề nghị lập data dictionary ghi "bước điểm (0,25 hay khác)". Kiểm tra thực tế trên dữ liệu: chỉ Ngữ văn có 99,6% giá trị khớp lưới 0,25 (môn tự luận, làm tròn theo quy chế). Các môn còn lại — Toán, Vật lý, Lịch sử, Địa lý, v.v. — có 14%–37% giá trị **không** khớp lưới 0,25, vì đề thi 2026 dùng định dạng hỗn hợp (trắc nghiệm + câu đúng/sai nhiều ý chấm 0,1/0,25/0,5/1 theo số ý đúng + câu trả lời ngắn), tạo ra bước điểm mịn hơn (quan sát thấy cả 0,05) — xem `reports/data_dictionary.md` mục "Thang điểm thực tế".

**Quyết định:** Không dùng lưới điểm cố định 0,25 làm tiêu chí lọc/kiểm tra chất lượng dữ liệu (các giá trị lệch lưới là hợp lệ, không phải lỗi). Ở GIAI ĐOẠN 3, ngưỡng rời rạc hóa điểm (cho bài toán luật kết hợp) sẽ dựa trên phân vị thống kê thực tế của từng môn, không áp đặt mốc tròn.

---

## DEC-005 — Xử lý thí sinh thiếu môn bắt buộc / thi không đủ 4 môn

**Giai đoạn:** 2 — Data Understanding **Ngày:** 2026-10-06

**Quan sát:** 96,42% thí sinh (1.165.582/1.208.863) thi đủ 4 môn (2 bắt buộc + 2 tự chọn) như quy chế chuẩn. Phần còn lại (3,58%) thi 1–3 môn, trong đó 16.426 thiếu Toán, 11.636 thiếu Ngữ văn, 72 thiếu cả hai. Đây nhiều khả năng là thí sinh diện đặc cách/miễn thi một phần hoặc thí sinh tự do không đăng ký đủ môn xét tốt nghiệp — không có cột "diện thí sinh" trong dữ liệu để xác nhận.

**Quyết định (áp dụng ở GIAI ĐOẠN 3):** Với bảng giao dịch luật kết hợp (đơn vị phân tích = "thí sinh dự thi chuẩn 4 môn"), loại các dòng thiếu môn bắt buộc (16.426 + 11.636 − 72 trùng ≈ 27.990 dòng, ~2,3%) để tránh luật kết hợp bị nhiễu bởi nhóm thí sinh có hồ sơ thi khác thường. Với bảng đặc trưng cấp tỉnh/điểm thi (GIAI ĐOẠN 3b, 3c) vẫn **giữ toàn bộ** thí sinh vì các thống kê mô tả (mean/std/tỷ lệ) không yêu cầu đủ 4 môn.

**Kết quả thực thi (GIAI ĐOẠN 3):** Hàm `filter_standard_candidates` giữ lại **1.165.582/1.208.863 dòng (96,42%)**, loại **43.281 dòng (3,58%)** — khớp đúng số liệu ước tính ở trên (chênh lệch nhỏ vì áp dụng đồng thời điều kiện "đủ 4 môn" và "đủ 2 môn bắt buộc" thay vì cộng dồn thô 2 điều kiện riêng lẻ).

---

## DEC-006 — Ngưỡng rời rạc hóa điểm cho bảng giao dịch (luật kết hợp)

**Giai đoạn:** 3 — Data Preparation **Ngày:** 2026-10-06

**Quyết định:** Dùng 4 mức rời rạc hóa theo quy ước phổ biến trong giáo dục phổ thông Việt Nam: **Yếu (<5) / Trung bình (5–6,5) / Khá (6,5–8) / Giỏi (≥8)** — xem `config.yaml: discretization`.

**Lý do:** Đã cân nhắc phương án chia theo tứ phân vị thống kê (bins đều số lượng mỗi nhóm), nhưng chọn ngưỡng quy ước giáo dục vì: (1) luật kết hợp sinh ra sẽ dễ diễn giải với đối tượng nghiệp vụ (giáo viên, nhà trường, phụ huynh) vốn đã quen thuộc với thang Yếu/TB/Khá/Giỏi, khớp yêu cầu "diễn giải bằng ngôn ngữ dễ hiểu"; (2) ngưỡng quy ước ổn định qua các năm, trong khi tứ phân vị sẽ đổi theo từng môn/từng năm, gây khó so sánh khi mở rộng phân tích đa năm (mục bonus). Đánh đổi: các bin có thể không cân bằng về số lượng (vd phổ điểm Ngữ văn tập trung quanh 6,5–8 nên bin "Khá" sẽ đông hơn "Yếu") — chấp nhận được vì mục tiêu là luật dễ hiểu, không phải cân bằng dữ liệu.

---

## DEC-007 — Hiệu chỉnh diễn giải "mã điểm thi" sau khi thực thi

**Giai đoạn:** 3 — Data Preparation **Ngày:** 2026-10-06

**Phát hiện:** Khi nhóm thí sinh theo 3 chữ số giữa của SBD (DEC-003), thu được 1.237 nhóm trên 34 tỉnh (~36 nhóm/tỉnh), với kích thước nhóm **rất gần 1.000** (trung vị 996, 75% nhóm có 992–998 thí sinh, tối đa 1.000). Điều này cho thấy 3 chữ số giữa thực chất chia đều số thứ tự đăng ký 6 chữ số thành các **khối liên tiếp 1.000 SBD** — đây là ranh giới mang tính **đánh số hành chính** (có thể trùng với điểm thi/cụm trường thực tế như README nguồn quan sát ở một vài trường hợp cụ thể, nhưng không có gì đảm bảo mọi khối 1.000 SBD đều là một điểm thi vật lý duy nhất).

**Quyết định:** Đổi thuật ngữ trong code/báo cáo từ "điểm thi" sang **"nhóm SBD theo khối nghìn" (site_id)** để không ngộ nhận đây là đơn vị phòng thi đã được xác nhận chính thức. Giữ nguyên làm đơn vị phân tích chính cho RQ3 (vì là ranh giới có cấu trúc rõ trong dữ liệu, tốt hơn giả định tùy ý), nhưng **bắt buộc đối chiếu với phương án cửa sổ trượt** (``build_sliding_window_features``, kích thước 24/50/100 — gần với quy mô phòng thi thật hơn) để kiểm tra độ nhạy, đúng yêu cầu gốc. Chỉ giữ nhóm có ≥10 thí sinh (``min_group_size``) để tránh nhiễu thống kê ở nhóm quá nhỏ (nhóm cuối mỗi tỉnh thường không đầy 1.000).

**Hạn chế sẽ nêu trong final_report.md:** Phát hiện bất thường ở cấp "site_id" phản ánh **cụm ~1.000 thí sinh đăng ký liên tiếp**, không phải một phòng thi (~24-40 thí sinh) theo đúng nghĩa đen — có thể che lấp bất thường cục bộ nhỏ hơn hoặc pha loãng tín hiệu. Phương án cửa sổ trượt 24 SBD mô phỏng sát quy mô phòng thi hơn, dùng làm đối chứng.

---

## DEC-008 — Giảm chiều (PCA) trước khi phân cụm cấp tỉnh

**Giai đoạn:** 4.2 — Modeling (Clustering) **Ngày:** 2026-10-06

**Vấn đề:** Bảng đặc trưng cấp tỉnh có 70 cột số nhưng chỉ 34 dòng (tỉnh) — tỷ lệ chiều/mẫu quá cao gây "curse of dimensionality": khoảng cách Euclidean giữa các điểm trở nên kém phân biệt, Silhouette score trên không gian 70 chiều chỉ đạt tối đa 0,259 (k=2) — dưới ngưỡng thành công 0,3 đề ra ở mục 1.5.

**Thử nghiệm:** Giảm chiều bằng PCA trước khi phân cụm (K-Means), quét số thành phần chính từ 5 đến 20: n_components=5 (giữ 77,5% phương sai) cho kết quả tốt nhất — Silhouette = 0,357 tại k=4, vượt ngưỡng thành công. Số thành phần càng tăng, Silhouette càng giảm dần về gần mức 70-chiều ban đầu — xác nhận nhiễu từ các chiều ít thông tin là nguyên nhân chính làm giảm chất lượng phân cụm.

**Quyết định:** Dùng không gian PCA 5 thành phần chính (từ `province_features_scaled.parquet`) làm đầu vào cho toàn bộ 3 thuật toán phân cụm (K-Means, Hierarchical/Ward, GMM) ở GIAI ĐOẠN 4.2, thay vì không gian gốc 70 chiều. Đây đồng thời là kỹ thuật nâng cao "giảm chiều để khám phá cấu trúc" (không chỉ dùng PCA để trực quan hóa 2D). Chân dung cụm (profiling) vẫn diễn giải trên các đặc trưng gốc chưa chuẩn hóa để giữ ý nghĩa thực tế (điểm trung bình, tỷ lệ chọn môn...).

---

## DEC-009 — Phạm vi so sánh 2026 vs 2025 (bonus) chỉ ở cấp quốc gia

**Giai đoạn:** 5 — Evaluation (phần bonus) **Ngày:** 2026-10-06

**Vấn đề:** Kiểm tra `data/raw/diem_thi_2025_ct2018.csv` cho thấy cột `Tinh` dùng **hệ mã 63 tỉnh cũ** (giá trị 1–64, thiếu mã 20 do Hà Tây đã sáp nhập vào Hà Nội trước đó), khác hoàn toàn với hệ **34 mã tỉnh mới** dùng cho dữ liệu 2026 (`PROVINCE_MAP`). Hai hệ mã không thể ánh xạ 1-1 (nhiều tỉnh cũ gộp thành 1 tỉnh mới với ranh giới địa lý khác).

**Quyết định:** Phần so sánh bonus 2026 vs 2025 **chỉ thực hiện ở cấp quốc gia** (phổ điểm, tỷ lệ chọn tổ hợp môn, mẫu hình luật kết hợp) — **không so sánh cấp tỉnh** để tránh kết luận sai do lệch ranh giới hành chính. Đây là hạn chế đã biết trước, nêu rõ trong `final_report.md`.

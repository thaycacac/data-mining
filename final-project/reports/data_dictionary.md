# Từ điển dữ liệu (Data Dictionary)

Nguồn: `data/raw/diem_thi_2026.csv` (xem `decisions_log.md` DEC-001). 1.208.863 dòng × 18 cột gốc (sau xử lý đổi tên: 27 cột, thêm `province_name`). Tất cả số liệu dưới đây được tính trực tiếp trên dữ liệu thật (`src/preprocessing.load_raw_csv`), không suy đoán.

## Cột gốc → nội bộ

| Cột CSV gốc | Tên nội bộ | Kiểu lưu trữ | Ý nghĩa | Miền giá trị quan sát được |
|---|---|---|---|---|
| `SBD` | `sbd` | string (giữ số 0 đầu) | Số báo danh, 8 ký tự = mã tỉnh (2) + số thứ tự (6) | vd `"01000001"` |
| `Nam` | `nam` | int16 | Năm dự thi | 26 (= 2026), hằng số |
| `Tinh` | `province_code` | int16 | Mã tỉnh, **không có số 0 dẫn đầu** trong file (khác với README gốc ghi "01") | {1,4,8,11,...,96} — 34 giá trị |
| `SBD_New` | `sbd_seq` | int32 | Số thứ tự thí sinh trong tỉnh (6 chữ số logic, lưu dạng int) | 1–139678 |
| `Toan` | `toan` | float32 | Điểm Toán /10 | xem mục Thang điểm bên dưới |
| `NguVan` | `ngu_van` | float32 | Điểm Ngữ văn /10 | bước 0,25 (99,6% giá trị) |
| `VatLy` | `vat_ly` | float32 | Điểm Vật lý /10 (môn tự chọn) | — |
| `HoaHoc` | `hoa_hoc` | float32 | Điểm Hóa học /10 (môn tự chọn) | — |
| `SinhHoc` | `sinh_hoc` | float32 | Điểm Sinh học /10 (môn tự chọn) | — |
| `LichSu` | `lich_su` | float32 | Điểm Lịch sử /10 (môn tự chọn) | — |
| `DiaLy` | `dia_ly` | float32 | Điểm Địa lý /10 (môn tự chọn) | — |
| `KinhTePhapLuat` | `kinh_te_phap_luat` | float32 | Điểm GD Kinh tế - Pháp luật /10 (môn tự chọn) | — |
| `TinHoc` | `tin_hoc` | float32 | Điểm Tin học /10 (môn tự chọn) | — |
| `CongNgheCongNghiep` | `cong_nghe_cong_nghiep` | float32 | Điểm Công nghệ - Công nghiệp /10 (môn tự chọn) | — |
| `CongNgheNongNghiep` | `cong_nghe_nong_nghiep` | float32 | Điểm Công nghệ - Nông nghiệp /10 (môn tự chọn) | — |
| `NgoaiNgu` | `ngoai_ngu` | float32 | Điểm Ngoại ngữ /10 (môn tự chọn, 1 trong 7 thứ tiếng) | — |
| `MaMonNgoaiNgu` | `ma_mon_ngoai_ngu` | category | Mã thứ tiếng ngoại ngữ | N1 Anh, N2 Nga, N3 Pháp, N4 Trung, N5 Đức, N6 Nhật, N7 Hàn |
| `TongDiem` | `tong_diem` | float32 | Tổng điểm 4 môn (2 bắt buộc + 2 tự chọn) /40 | — |
| `KhoiA..KhoiD07` | `khoi_a` … `khoi_d07` | float32 | Điểm tổ hợp xét tuyển ĐH có sẵn (A00, A01, B00, C00, D00, A02, C01, D07) /30 | chỉ có khi đủ 3 môn tổ hợp |
| *(suy ra)* | `province_name` | category | Tên tỉnh, map từ `province_code` (34 tỉnh sau sáp nhập 2025) | vd "Hà Nội" |

## Thang điểm thực tế (quan trọng — khác giả định "bước 0,25 cố định")

Kỳ thi 2026 dùng định dạng đề hỗn hợp (trắc nghiệm nhiều lựa chọn + câu hỏi đúng/sai nhiều ý + câu trả lời ngắn), mỗi dạng câu có trọng số điểm khác nhau (0,1 / 0,25 / 0,5 / 1 tùy môn và loại câu — theo mô tả repo nguồn). Kiểm tra thực tế trên dữ liệu:

| Môn | % giá trị **không** rơi đúng lưới 0,25 | Nhận xét |
|---|---|---|
| Ngữ văn | 0,41% | Tự luận, làm tròn 0,25 → gần như đúng lưới 0,25 như kỳ vọng |
| Toán | 14,21% | Có câu đúng/sai (0,1/0,25/0,5/1 theo số ý đúng) → bước điểm mịn hơn 0,25 |
| Vật lý | 26,67% | Tương tự Toán |
| Lịch sử | 34,26% | Có câu đúng/sai |
| Địa lý | 37,41% | Có câu đúng/sai |

**Kết luận:** chỉ Ngữ văn có bước điểm cố định 0,25. Các môn còn lại có bước điểm thực tế mịn hơn (quan sát thấy cả 0,05). Quyết định xử lý: khi rời rạc hóa điểm ở GIAI ĐOẠN 3, dùng ngưỡng theo phân vị thống kê thay vì giả định lưới điểm cố định — ghi nhận vào `decisions_log.md`.

## Kiểm tra chất lượng dữ liệu (kết quả thực tế)

| Kiểm tra | Kết quả |
|---|---|
| SBD khớp `province_code` (2 số) + `sbd_seq` (6 số) | **100% khớp** (0 dòng lệch) |
| SBD trùng lặp | **0 dòng trùng** |
| Điểm ngoài khoảng [0, 10] | **0 dòng** |
| Thiếu Toán (môn bắt buộc) | 16.426 dòng (1,36%) |
| Thiếu Ngữ văn (môn bắt buộc) | 11.636 dòng (0,96%) |
| Thiếu **cả hai** môn bắt buộc | 72 dòng (0,006%) |
| Số môn đã thi / thí sinh | 4 môn: 1.165.582 (96,42%) · 3 môn: 40.384 · 2 môn: 1.182 · 1 môn: 1.715 |
| Số tỉnh | 34/34 khớp kỳ vọng, dân số thí sinh từ 4.650 (Lai Châu) đến 139.678 (Hồ Chí Minh) |

**Diễn giải:** Phần lớn thí sinh thiếu môn bắt buộc hoặc thi <4 môn nhiều khả năng là thí sinh diện đặc cách/miễn thi, hoặc tự do (không thi đủ môn xét tốt nghiệp) — sẽ xử lý cụ thể ở GIAI ĐOẠN 3 (loại khỏi bảng giao dịch luật kết hợp nếu thiếu môn bắt buộc, vì không phản ánh đúng mẫu hình "tổ hợp môn tự chọn" của luồng thi chuẩn). **Giá trị trống ở các môn tự chọn = thí sinh không đăng ký thi môn đó (không phải thiếu dữ liệu)** — xác nhận bằng tỷ lệ "đúng 2 môn tự chọn" chiếm 98,6% trong số thí sinh thi đủ 4 môn.

## Hiện tượng đáng chú ý (dùng cho GIAI ĐOẠN 4.3 — phát hiện bất thường)

- **Dồn điểm Ngữ văn tại 5,0 toàn quốc:** 49.195 thí sinh đạt đúng 5,0, so với trung bình nội suy từ điểm lân cận (4,75: 20.890; 5,25: 42.813) là 31.851,5 → **tỷ lệ 1,54×** — khớp với quan sát đã công bố trong README nguồn (ước tính ~1,5×). Sẽ kiểm định heaping chính thức bằng thống kê ở GIAI ĐOẠN 4.3.
- **Tương quan giữa các môn** (Pearson, toàn quốc): Toán tương quan mạnh với khối Tự nhiên (Sinh 0,76; Vật lý 0,73; Hóa 0,71), Ngữ văn tương quan mạnh với khối Xã hội (Địa lý 0,55; Lịch sử 0,53) — phù hợp trực giác sư phạm, dùng làm cơ sở kỳ vọng khi diễn giải luật kết hợp (RQ1): luật "giỏi Toán ⇒ giỏi Sinh" sẽ không bất ngờ, luật thú vị là luật *lệch* khỏi tương quan tuyến tính thông thường.
- **Top tổ hợp 2 môn tự chọn:** Địa lý + Lịch sử (277.309 thí sinh) và Hóa học + Vật lý (175.249) là hai tổ hợp phổ biến nhất — phản ánh rõ 2 nhóm truyền thống Khoa học Xã hội / Khoa học Tự nhiên; xem `reports/figures/02_top_to_hop_tu_chon.png`.

## Hình minh họa (GIAI ĐOẠN 2)

- `reports/figures/02_pho_diem_toan_van.png` — phổ điểm Toán & Ngữ văn
- `reports/figures/02_ma_tran_tuong_quan.png` — ma trận tương quan 9 môn
- `reports/figures/02_top_to_hop_tu_chon.png` — top 10 tổ hợp môn tự chọn
- `reports/figures/02_diem_toan_theo_tinh.png` — phân bố điểm Toán theo 34 tỉnh

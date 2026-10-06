# Khai phá dữ liệu điểm thi tốt nghiệp THPT Việt Nam 2026

Dự án Data Mining: **Luật kết hợp, Phân cụm tỉnh thành và Phát hiện bất thường** trên dữ liệu điểm thi tốt nghiệp THPT 2026 (1.208.863 thí sinh, 34 tỉnh/thành sau sáp nhập). Thực hiện theo quy trình CRISP-DM đầy đủ, có thể tái lập.

**Tác giả:** Phạm Ngọc Hòa

**Báo cáo đầy đủ:** [reports/final_report.md](reports/final_report.md) **Tài liệu ôn kiến thức Data Mining:** [docs/00_tong_quan.md](docs/00_tong_quan.md) **Nhật ký quyết định xử lý dữ liệu:** [reports/decisions_log.md](reports/decisions_log.md)

## Trạng thái

- [x] Giai đoạn 0 — Khởi tạo & tải dữ liệu
- [x] Giai đoạn 1 — Business Understanding
- [x] Giai đoạn 2 — Data Understanding
- [x] Giai đoạn 3 — Data Preparation
- [x] Giai đoạn 4 — Modeling (Association Rules, Clustering, Anomaly Detection)
- [x] Giai đoạn 5 — Evaluation (+ Bonus: so sánh 2026 vs 2025)
- [x] Giai đoạn 6 — Deployment / Báo cáo

## Cài đặt

Yêu cầu Python ≥ 3.11.

```bash
cd final-project
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m ipykernel install --user --name thpt2026-venv --display-name "Python (thpt2026)"
```

## Tải dữ liệu

Dữ liệu **không** nằm trong git (xem `.gitignore`) — tải lại bằng:

```bash
.venv/bin/python -m src.data_loader
```

Lệnh này tải (idempotent — bỏ qua nếu đã có file):
- `data/raw/diem_thi_2026.csv` (~79MB, 1.208.863 dòng, 34 tỉnh) — nguồn dữ liệu chính
- `data/raw/diem_thi_2025_ct2018.csv` (~73MB) — dùng cho phần so sánh bonus

Xem lý do chọn nguồn dữ liệu này (thay vì nguồn được đề xuất ban đầu, vốn không có CSV tải được) tại `reports/decisions_log.md` (DEC-001).

## Chạy lại toàn bộ dự án từ đầu

```bash
# 1. Cài đặt môi trường + tải dữ liệu (xem trên)

# 2. Chạy unit test
.venv/bin/python -m pytest tests/ -q

# 3. Chạy lần lượt 6 notebook (theo đúng thứ tự, mỗi notebook ghi ra
#    data/processed/ hoặc reports/figures/ cho notebook sau dùng)
for nb in notebooks/0*.ipynb; do
  .venv/bin/jupyter nbconvert --to notebook --execute --inplace \
    --ExecutePreprocessor.kernel_name=thpt2026-venv \
    --ExecutePreprocessor.timeout=900 "$nb"
done
```

Toàn bộ kết quả số liệu trong `reports/final_report.md` được tính trực tiếp từ các notebook này — không có số liệu giả định/suy đoán.

## Cấu trúc thư mục

```
final-project/
├── config.yaml              # seed, đường dẫn, ngưỡng/tham số thuật toán
├── requirements.txt
├── data/
│   ├── raw/                 # dữ liệu gốc, bất biến (không có trong git)
│   ├── interim/              # (dự phòng cho bước trung gian)
│   └── processed/            # bảng giao dịch + đặc trưng, dạng Parquet
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_preparation.ipynb
│   ├── 03_association_rules.ipynb
│   ├── 04_clustering_provinces.ipynb
│   ├── 05_anomaly_detection.ipynb
│   └── 06_evaluation_summary.ipynb   # + phần bonus so sánh 2026 vs 2025
├── src/
│   ├── data_loader.py        # tải dữ liệu gốc
│   ├── preprocessing.py      # nạp, đổi tên cột, kiểm tra chất lượng
│   ├── features.py           # 3 bảng đặc trưng (giao dịch/tỉnh/điểm thi)
│   ├── association.py        # Apriori, FP-Growth, sinh luật
│   ├── clustering.py         # K-Means, Hierarchical, DBSCAN, GMM, PCA
│   ├── anomaly.py            # Z-score/IQR, heaping, Isolation Forest, LOF
│   └── visualization.py      # style chung + lưu hình
├── tests/                    # unit test cho src/preprocessing.py, src/features.py
├── docs/                     # ghi chú kiến thức Data Mining áp dụng trong dự án
└── reports/
    ├── decisions_log.md      # mọi quyết định xử lý dữ liệu, kèm lý do
    ├── data_dictionary.md
    ├── final_report.md       # báo cáo chính
    └── figures/               # toàn bộ hình, có chú thích tiếng Việt
```

## Xuất báo cáo PDF

`reports/final_report.pdf` là bản PDF đầy đủ (21 trang, có nhúng toàn bộ hình) dựng từ `reports/final_report_pdf.md` (bản sao của `final_report.md` có chèn thêm ảnh) + `reports/pdf_style.css`. Dựng lại bằng:

```bash
cd reports
pandoc final_report_pdf.md -f markdown -t html5 --standalone \
  --metadata title="Khai phá dữ liệu điểm thi THPT 2026" -o final_report.html
DYLD_FALLBACK_LIBRARY_PATH="/opt/homebrew/lib" \
  weasyprint final_report.html final_report.pdf -s pdf_style.css
rm final_report.html
```

Yêu cầu: `pandoc`, `weasyprint` (`pip install weasyprint`), và thư viện hệ thống `pango`/`gdk-pixbuf`/`glib` (`brew install pango gdk-pixbuf glib` trên macOS). Nếu sửa nội dung, chỉnh `final_report.md` trước rồi đồng bộ thủ công sang `final_report_pdf.md` (bản PDF chèn thêm `![...](figures/...)` mà bản Markdown gốc chỉ nhắc tên file).

## Nguồn dữ liệu & đạo đức dữ liệu

- Nguồn: `sdgedfegw/du-lieu-diem-thi` (GitHub), thu thập từ trang tra cứu điểm công khai, **không phải công bố chính thức của Bộ GD&ĐT** (xem DEC-001).
- Dữ liệu đã ẩn danh ở mức SBD; dự án **không** cố liên kết SBD với danh tính cá nhân, không công bố danh sách SBD cụ thể trong báo cáo.
- Mọi kết quả phát hiện bất thường (GIAI ĐOẠN 4.3 / RQ3) chỉ được diễn đạt là "bất thường về mặt thống kê, cần xem xét thêm" — **không** kết luận gian lận hay quy trách nhiệm cho bất kỳ tỉnh/điểm thi cụ thể nào.

# Tiền xử lý dữ liệu & quy trình làm việc

Áp dụng trong: `src/preprocessing.py`, `src/features.py`, toàn bộ pipeline.

## 1. Vì sao tách `data/raw` — `data/interim` — `data/processed`

Nguyên tắc **dữ liệu gốc bất biến** (`data/raw/` không bao giờ bị ghi đè) là thực hành chuẩn trong khoa học dữ liệu có thể tái lập (reproducible data science): mọi lỗi trong bước xử lý có thể sửa và chạy lại từ đầu mà không sợ mất dữ liệu gốc. `data/processed/` chứa kết quả **sẵn sàng dùng cho mô hình** (bảng giao dịch, bảng đặc trưng) — tách biệt khỏi dữ liệu thô giúp các bước Modeling (GIAI ĐOẠN 4) không phải chạy lại toàn bộ tiền xử lý mỗi lần.

## 2. Parquet + dtype tối ưu

CSV lưu mọi thứ dạng text, phải parse lại mỗi lần đọc và không giữ kiểu dữ liệu. **Parquet** là định dạng cột (columnar), nén tốt, giữ nguyên kiểu dữ liệu (dtype), đọc nhanh hơn nhiều lần so với CSV cho dữ liệu lớn. Dự án dùng `float32` thay vì `float64` mặc định của pandas cho các cột điểm (độ chính xác thập phân 0,05-0,25 không cần float64, giảm ~50% bộ nhớ) và `category` cho các cột ít giá trị lặp lại (`province_name`, `ma_mon_ngoai_ngu`) — giảm bộ nhớ đáng kể trên 1,2 triệu dòng (xem `src/preprocessing._DTYPE_MAP`).

## 3. StandardScaler trước khi phân cụm/phát hiện bất thường

`StandardScaler` biến đổi mỗi đặc trưng về trung bình 0, độ lệch chuẩn 1: `z = (x - μ) / σ`. **Vì sao bắt buộc** với K-Means/Hierarchical/GMM/ Isolation Forest/LOF: các thuật toán này dựa trên khoảng cách (Euclidean) hoặc phân vùng không gian — nếu một đặc trưng có thang đo lớn hơn hẳn (vd `n_candidates` hàng chục nghìn so với `pct_chon` trong [0,1]), nó sẽ áp đảo khoảng cách tổng, khiến các đặc trưng khác gần như vô nghĩa. Không cần chuẩn hóa cho luật kết hợp (dữ liệu nhị phân/item, không có khái niệm khoảng cách).

## 4. Rời rạc hóa (discretization) điểm số

Chuyển biến liên tục (điểm 0-10) thành biến phân loại (Yếu/TB/Khá/Giỏi) để dùng được cho luật kết hợp (vốn làm việc trên item rời rạc). Có 2 cách tiếp cận phổ biến:
- **Theo phân vị (quantile-based):** chia sao cho mỗi bin có số lượng gần bằng nhau — tối ưu cho việc "cân bằng dữ liệu" nhưng ranh giới bin vô nghĩa với người đọc (vd "yếu" có thể là <6,3 nếu đa số đạt điểm cao).
- **Theo quy ước lĩnh vực (domain convention):** dùng ranh giới đã có ý nghĩa sẵn trong lĩnh vực (ở đây: thang Yếu/TB/Khá/Giỏi quen thuộc trong giáo dục phổ thông VN). Dự án chọn cách này (xem DEC-006) vì ưu tiên **khả năng diễn giải** cho đối tượng nghiệp vụ hơn là cân bằng thống kê thuần túy — đánh đổi hợp lý khi mục tiêu cuối là luật dễ hiểu, không phải một mô hình dự đoán tối ưu.

## 5. Kiểm thử (testing) các hàm tiền xử lý

`tests/test_preprocessing.py` và `tests/test_features.py` dùng **pytest** với dữ liệu giả lập nhỏ (không phải 1,2 triệu dòng thật) để kiểm tra logic từng hàm độc lập — gọi là **unit test**. Vì sao quan trọng trong một dự án data mining: các hàm tiền xử lý (lọc dòng, rời rạc hóa, tính đặc trưng) quyết định trực tiếp chất lượng input cho mô hình — một lỗi nhỏ (vd sai biên `<` thành `<=` khi rời rạc hóa) có thể âm thầm làm sai lệch hàng trăm nghìn dòng dữ liệu mà không gây lỗi chương trình (silent failure), rất khó phát hiện nếu chỉ nhìn kết quả cuối. Test giúp bắt lỗi *trước khi* chạy trên dữ liệu thật quy mô lớn.

## 6. Tái lập kết quả (reproducibility)

- **Seed cố định (`random_seed: 42`)** cho mọi thuật toán có yếu tố ngẫu nhiên (K-Means init, train/test split nếu có, Isolation Forest) — đảm bảo chạy lại cho kết quả giống hệt.
- **Notebook chỉ gọi hàm từ `src/`**, không viết logic trực tiếp trong cell — cho phép kiểm thử logic độc lập (mục 5) và tái sử dụng giữa các notebook (vd `build_transactions_df` dùng ở cả notebook 02 và 06).
- **`config.yaml`** tập trung mọi tham số có thể thay đổi (ngưỡng, seed, min_support...) — thay đổi thử nghiệm không cần sửa code.

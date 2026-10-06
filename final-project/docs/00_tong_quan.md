# Tổng quan: Kiến thức Data Mining áp dụng trong dự án

Thư mục `docs/` ghi lại **kiến thức nền** đằng sau từng kỹ thuật dùng trong dự án, giải thích theo hướng "khái niệm là gì → vì sao dùng ở đây → áp dụng cụ thể ra sao → đọc kết quả như thế nào". Đây là tài liệu học tập (ôn lại kiến thức), **tách biệt** với `reports/final_report.md` (báo cáo nộp — chỉ trình bày kết quả) và `reports/decisions_log.md` (nhật ký quyết định xử lý dữ liệu).

## Bản đồ tài liệu

| File | Nội dung |
|---|---|
| [01_luat_ket_hop.md](01_luat_ket_hop.md) | Apriori, FP-Growth, support/confidence/lift/conviction |
| [02_phan_cum.md](02_phan_cum.md) | K-Means, Elbow, Silhouette, Hierarchical/Ward, DBSCAN, GMM, PCA |
| [03_phat_hien_bat_thuong.md](03_phat_hien_bat_thuong.md) | Z-score/IQR, Isolation Forest, Local Outlier Factor, entropy, Jaccard |
| [04_tien_xu_ly_va_quy_trinh.md](04_tien_xu_ly_va_quy_trinh.md) | CRISP-DM, StandardScaler, discretization, Parquet, kiểm thử (pytest) |

## Quy trình CRISP-DM đã áp dụng (bản đồ nhanh)

```
1. Business Understanding  -> reports/final_report.md mục 1
2. Data Understanding      -> notebooks/01_data_understanding.ipynb
3. Data Preparation        -> notebooks/02_data_preparation.ipynb
4. Modeling                -> notebooks/03, 04, 05 (.ipynb)
5. Evaluation               -> notebooks/06_evaluation_summary.ipynb
6. Deployment               -> reports/final_report.md (hoàn chỉnh) + README.md
```

Mỗi mũi tên tương ứng với một giai đoạn CRISP-DM kinh điển (Han, Kamber, Pei — *Data Mining: Concepts and Techniques*) — framework lý thuyết nền cho toàn bộ dự án.

## Vì sao dự án dùng CẢ BA kỹ thuật không giám sát thay vì chỉ 2?

Ba kỹ thuật (luật kết hợp, phân cụm, phát hiện bất thường) nhìn vào **ba đơn vị phân tích khác nhau** trên cùng một bộ dữ liệu:

| Kỹ thuật | Đơn vị phân tích | Câu hỏi trả lời |
|---|---|---|
| Luật kết hợp | 1 thí sinh = 1 giao dịch | Các *item* (môn + mức điểm) nào hay xuất hiện cùng nhau? |
| Phân cụm | 1 tỉnh = 1 điểm dữ liệu | Các *tỉnh* nào giống nhau về đặc điểm điểm thi? |
| Phát hiện bất thường | 1 nhóm thí sinh (điểm thi) = 1 điểm dữ liệu | *Nhóm* nào lệch khỏi phân bố chung một cách đáng ngờ? |

Việc đổi đơn vị phân tích (thí sinh → tỉnh → nhóm thí sinh) là lý do chính khiến ba kỹ thuật này **bổ sung** nhau thay vì trùng lặp thông tin — đây cũng là nguyên tắc thiết kế quan trọng khi làm một dự án khai phá dữ liệu đa góc nhìn.

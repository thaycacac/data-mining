"""Xây dựng 3 bảng đặc trưng phục vụ GIAI ĐOẠN 4:

1. ``build_transactions``      -> bảng giao dịch cho luật kết hợp (4.1)
2. ``build_province_features`` -> đặc trưng cấp tỉnh cho phân cụm (4.2)
3. ``build_site_features``     -> đặc trưng cấp điểm thi cho phát hiện
   bất thường (4.3), kèm phương án cửa sổ trượt để kiểm tra độ nhạy.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from scipy.stats import entropy as scipy_entropy
from sklearn.preprocessing import StandardScaler

from src.preprocessing import (
    COMPULSORY_SUBJECTS,
    ELECTIVE_SUBJECTS,
    SUBJECT_COLUMNS,
    n_subjects_taken,
)

SUBJECT_LABELS = {
    "toan": "Toan",
    "ngu_van": "NguVan",
    "vat_ly": "VatLy",
    "hoa_hoc": "HoaHoc",
    "sinh_hoc": "SinhHoc",
    "lich_su": "LichSu",
    "dia_ly": "DiaLy",
    "kinh_te_phap_luat": "GDKTPL",
    "tin_hoc": "TinHoc",
    "cong_nghe_cong_nghiep": "CNCongNghiep",
    "cong_nghe_nong_nghiep": "CNNongNghiep",
    "ngoai_ngu": "NgoaiNgu",
}


# ---------------------------------------------------------------------
# 1. Bảng giao dịch cho luật kết hợp
# ---------------------------------------------------------------------

def filter_standard_candidates(df: pd.DataFrame) -> pd.DataFrame:
    """Giữ lại thí sinh thi đúng 4 môn (2 bắt buộc + 2 tự chọn) — xem DEC-005.

    Loại các thí sinh thiếu môn bắt buộc hoặc thi không đủ 4 môn vì không
    phản ánh đúng mẫu hình "tổ hợp môn tự chọn" của luồng thi chuẩn, và
    sẽ làm nhiễu luật kết hợp.
    """
    ns = n_subjects_taken(df)
    has_compulsory = df[COMPULSORY_SUBJECTS].notna().all(axis=1)
    return df[(ns == 4) & has_compulsory].copy()


def discretize_score(score: pd.Series, edges: list[float], labels: list[str]) -> pd.Series:
    """Rời rạc hóa điểm theo các mốc quy ước giáo dục (xem DEC-006)."""
    return pd.cut(score, bins=edges, labels=labels, right=False)


def build_transactions(
    df: pd.DataFrame,
    edges: list[float],
    labels: list[str],
) -> list[list[str]]:
    """Xây danh sách giao dịch (1 thí sinh = 1 giao dịch) cho FP-Growth/Apriori.

    Mỗi giao dịch gồm 2 loại item:
    - ``Chon_<Mon>``   : thí sinh đã chọn thi môn tự chọn đó (chỉ áp dụng
      cho 10 môn tự chọn — môn bắt buộc không tạo item này vì luôn đúng,
      sẽ chỉ gây ra luật hiển nhiên).
    - ``<Mon>_<Muc>``  : mức điểm rời rạc hóa của môn đã thi (áp dụng cho
      cả 12 môn, kể cả 2 môn bắt buộc).

    Chỉ nhận thí sinh đã qua ``filter_standard_candidates``.
    """
    transactions: list[list[str]] = []
    for _, row in df.iterrows():
        items: list[str] = []
        for subj in ELECTIVE_SUBJECTS:
            if pd.notna(row[subj]):
                items.append(f"Chon_{SUBJECT_LABELS[subj]}")
        for subj in SUBJECT_COLUMNS:
            val = row[subj]
            if pd.notna(val):
                band = pd.cut([val], bins=edges, labels=labels, right=False)[0]
                items.append(f"{SUBJECT_LABELS[subj]}_{band}")
        transactions.append(items)
    return transactions


def build_transactions_df(
    df: pd.DataFrame,
    edges: list[float],
    labels: list[str],
) -> pd.DataFrame:
    """Phiên bản vector hóa (nhanh hơn nhiều so với build_transactions trên
    dữ liệu lớn) — trả về DataFrame long-format (sbd, item) để pivot thành
    one-hot ở bước gọi (xem notebooks/03)."""
    records = []
    for subj in ELECTIVE_SUBJECTS:
        taken = df[subj].notna()
        if taken.any():
            records.append(pd.DataFrame({
                "sbd": df.loc[taken, "sbd"].values,
                "item": f"Chon_{SUBJECT_LABELS[subj]}",
            }))
    for subj in SUBJECT_COLUMNS:
        mask = df[subj].notna()
        if mask.any():
            band = discretize_score(df.loc[mask, subj], edges, labels)
            records.append(pd.DataFrame({
                "sbd": df.loc[mask, "sbd"].values,
                "item": SUBJECT_LABELS[subj] + "_" + band.astype(str),
            }))
    return pd.concat(records, ignore_index=True)


# ---------------------------------------------------------------------
# 2. Đặc trưng cấp tỉnh (cho phân cụm)
# ---------------------------------------------------------------------

def build_province_features(df: pd.DataFrame) -> pd.DataFrame:
    """34 dòng (1 tỉnh/dòng): mean/median/std/tỷ lệ giỏi/tỷ lệ yếu mỗi môn
    + tỷ lệ chọn từng môn tự chọn. Dùng toàn bộ thí sinh (không lọc theo
    DEC-005) vì các thống kê mô tả không yêu cầu đủ 4 môn."""
    rows = []
    for province, g in df.groupby("province_name", observed=True):
        row: dict[str, Any] = {"province_name": province, "n_candidates": len(g)}
        for subj in SUBJECT_COLUMNS:
            vals = g[subj].dropna()
            label = SUBJECT_LABELS[subj]
            if len(vals) > 0:
                row[f"{label}_mean"] = vals.mean()
                row[f"{label}_median"] = vals.median()
                row[f"{label}_std"] = vals.std()
                row[f"{label}_pct_gioi"] = (vals >= 8).mean()
                row[f"{label}_pct_yeu"] = (vals < 5).mean()
            else:
                row[f"{label}_mean"] = np.nan
                row[f"{label}_median"] = np.nan
                row[f"{label}_std"] = np.nan
                row[f"{label}_pct_gioi"] = np.nan
                row[f"{label}_pct_yeu"] = np.nan
            if subj in ELECTIVE_SUBJECTS:
                row[f"{label}_pct_chon"] = g[subj].notna().mean()
        rows.append(row)
    return pd.DataFrame(rows).set_index("province_name").sort_index()


def scale_features(df: pd.DataFrame, columns: list[str] | None = None) -> tuple[pd.DataFrame, StandardScaler]:
    """Chuẩn hóa StandardScaler các cột số, trả về (df đã scale, scaler đã fit)."""
    columns = columns or df.select_dtypes(include=[np.number]).columns.tolist()
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[columns].fillna(df[columns].mean()))
    return pd.DataFrame(scaled, index=df.index, columns=columns), scaler


# ---------------------------------------------------------------------
# 3. Đặc trưng cấp điểm thi (cho phát hiện bất thường)
# ---------------------------------------------------------------------

def _site_code_from_seq(sbd_seq: pd.Series, slice_: tuple[int, int] = (0, 3)) -> pd.Series:
    """Suy ra mã điểm thi (3 chữ số đầu của sbd_seq 6 chữ số) — xem DEC-003."""
    seq_str = sbd_seq.astype(int).astype(str).str.zfill(6)
    start, end = slice_
    return seq_str.str.slice(start, end)


def build_site_features(
    df: pd.DataFrame,
    subjects: list[str],
    min_group_size: int = 10,
    site_code_slice: tuple[int, int] = (0, 3),
) -> pd.DataFrame:
    """Đặc trưng theo đơn vị "điểm thi" suy ra từ SBD (DEC-003): mean/std
    từng môn, chênh lệch so với TB tỉnh, tỷ lệ trùng điểm ở 1 mức phổ
    biến nhất, entropy phân bố điểm. Chỉ giữ nhóm có >= min_group_size
    thí sinh để tránh nhiễu thống kê ở nhóm quá nhỏ."""
    work = df.copy()
    work["site_code"] = _site_code_from_seq(work["sbd_seq"], site_code_slice)
    work["site_id"] = work["province_code"].astype(str) + "-" + work["site_code"]

    province_means = df.groupby("province_name", observed=True)[subjects].mean()

    rows = []
    for site_id, g in work.groupby("site_id", observed=True):
        if len(g) < min_group_size:
            continue
        province = g["province_name"].iloc[0]
        row: dict[str, Any] = {
            "site_id": site_id,
            "province_name": province,
            "n_candidates": len(g),
        }
        for subj in subjects:
            vals = g[subj].dropna()
            label = SUBJECT_LABELS[subj]
            if len(vals) >= 3:
                row[f"{label}_mean"] = vals.mean()
                row[f"{label}_std"] = vals.std()
                row[f"{label}_diff_vs_province"] = vals.mean() - province_means.loc[province, subj]
                mode_val = vals.mode()
                row[f"{label}_pct_mode_tie"] = (vals == mode_val.iloc[0]).mean() if not mode_val.empty else np.nan
                counts = vals.value_counts(normalize=True)
                row[f"{label}_entropy"] = scipy_entropy(counts)
            else:
                for suffix in ["_mean", "_std", "_diff_vs_province", "_pct_mode_tie", "_entropy"]:
                    row[f"{label}{suffix}"] = np.nan
        rows.append(row)
    if not rows:
        return pd.DataFrame(columns=["province_name", "n_candidates"]).rename_axis("site_id")
    return pd.DataFrame(rows).set_index("site_id")


def build_sliding_window_features(
    df: pd.DataFrame,
    subjects: list[str],
    window_size: int,
) -> pd.DataFrame:
    """Phương án thay thế: nhóm theo cửa sổ trượt `window_size` SBD liên
    tiếp trong cùng tỉnh (thay vì mã điểm thi suy ra từ SBD), dùng để
    kiểm tra độ nhạy của kết quả phát hiện bất thường với cách định nghĩa
    "nhóm/phòng thi" — xem yêu cầu gốc GIAI ĐOẠN 3c và DEC-003."""
    work = df.sort_values(["province_code", "sbd_seq"]).copy()
    work["window_id"] = (
        work["province_code"].astype(str) + "-w"
        + (work.groupby("province_code", observed=True).cumcount() // window_size).astype(str)
    )
    province_means = df.groupby("province_name", observed=True)[subjects].mean()

    rows = []
    for window_id, g in work.groupby("window_id", observed=True):
        if len(g) < max(3, window_size // 2):
            continue
        province = g["province_name"].iloc[0]
        row: dict[str, Any] = {"window_id": window_id, "province_name": province, "n_candidates": len(g)}
        for subj in subjects:
            vals = g[subj].dropna()
            label = SUBJECT_LABELS[subj]
            if len(vals) >= 3:
                row[f"{label}_mean"] = vals.mean()
                row[f"{label}_std"] = vals.std()
                row[f"{label}_diff_vs_province"] = vals.mean() - province_means.loc[province, subj]
            else:
                row[f"{label}_mean"] = np.nan
                row[f"{label}_std"] = np.nan
                row[f"{label}_diff_vs_province"] = np.nan
        rows.append(row)
    if not rows:
        return pd.DataFrame(columns=["province_name", "n_candidates"]).rename_axis("window_id")
    return pd.DataFrame(rows).set_index("window_id")

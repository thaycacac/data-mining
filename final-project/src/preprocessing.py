"""Nạp và làm sạch dữ liệu điểm thi THPT.

Chịu trách nhiệm: đọc CSV thô với dtype tối ưu, đổi tên cột sang
snake_case tiếng Anh, ánh xạ mã tỉnh -> tên tỉnh, và các hàm kiểm tra/
xử lý chất lượng dữ liệu (thiếu, trùng, ngoài khoảng điểm hợp lệ).
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Mã tỉnh (2 chữ số, không có số 0 dẫn đầu trong dữ liệu gốc) -> tên tỉnh,
# theo danh sách 34 tỉnh/thành sau sáp nhập 2025 (khớp cả 2 nguồn dữ liệu
# đã đối chiếu ở DEC-001).
PROVINCE_MAP: dict[int, str] = {
    1: "Hà Nội",
    4: "Cao Bằng",
    8: "Tuyên Quang",
    11: "Điện Biên",
    12: "Lai Châu",
    14: "Sơn La",
    15: "Lào Cai",
    19: "Thái Nguyên",
    20: "Lạng Sơn",
    22: "Quảng Ninh",
    24: "Bắc Ninh",
    25: "Phú Thọ",
    31: "Hải Phòng",
    33: "Hưng Yên",
    37: "Ninh Bình",
    38: "Thanh Hóa",
    40: "Nghệ An",
    42: "Hà Tĩnh",
    44: "Quảng Trị",
    46: "Huế",
    48: "Đà Nẵng",
    51: "Quảng Ngãi",
    52: "Gia Lai",
    56: "Khánh Hòa",
    66: "Đắk Lắk",
    68: "Lâm Đồng",
    75: "Đồng Nai",
    79: "Hồ Chí Minh",
    80: "Tây Ninh",
    82: "Đồng Tháp",
    86: "Vĩnh Long",
    91: "An Giang",
    92: "Cần Thơ",
    96: "Cà Mau",
}

# Môn bắt buộc theo Chương trình GDPT 2018 (áp dụng từ kỳ thi 2025).
COMPULSORY_SUBJECTS = ["toan", "ngu_van"]

# Môn tự chọn (2 trong số 9 môn này, Ngoại ngữ nằm trong nhóm tự chọn).
ELECTIVE_SUBJECTS = [
    "vat_ly", "hoa_hoc", "sinh_hoc", "lich_su", "dia_ly",
    "kinh_te_phap_luat", "tin_hoc", "cong_nghe_cong_nghiep",
    "cong_nghe_nong_nghiep", "ngoai_ngu",
]

SUBJECT_COLUMNS = COMPULSORY_SUBJECTS + ELECTIVE_SUBJECTS

# Đổi tên cột CSV gốc (PascalCase, nguồn sdgedfegw) -> tên nội bộ snake_case.
RAW_TO_INTERNAL = {
    "SBD": "sbd",
    "Nam": "nam",
    "Tinh": "province_code",
    "SBD_New": "sbd_seq",
    "Toan": "toan",
    "NguVan": "ngu_van",
    "VatLy": "vat_ly",
    "HoaHoc": "hoa_hoc",
    "SinhHoc": "sinh_hoc",
    "LichSu": "lich_su",
    "DiaLy": "dia_ly",
    "KinhTePhapLuat": "kinh_te_phap_luat",
    "TinHoc": "tin_hoc",
    "CongNgheCongNghiep": "cong_nghe_cong_nghiep",
    "CongNgheNongNghiep": "cong_nghe_nong_nghiep",
    "NgoaiNgu": "ngoai_ngu",
    "MaMonNgoaiNgu": "ma_mon_ngoai_ngu",
    "TongDiem": "tong_diem",
    "KhoiA": "khoi_a",
    "KhoiA1": "khoi_a1",
    "KhoiB": "khoi_b",
    "KhoiC": "khoi_c",
    "KhoiD": "khoi_d",
    "KhoiA02": "khoi_a02",
    "KhoiC01": "khoi_c01",
    "KhoiD07": "khoi_d07",
}

_SCORE_DTYPE = "float32"

_DTYPE_MAP = {
    "SBD": "string",
    "Nam": "int16",
    "Tinh": "int16",
    "SBD_New": "int32",
    "Toan": _SCORE_DTYPE,
    "NguVan": _SCORE_DTYPE,
    "VatLy": _SCORE_DTYPE,
    "HoaHoc": _SCORE_DTYPE,
    "SinhHoc": _SCORE_DTYPE,
    "LichSu": _SCORE_DTYPE,
    "DiaLy": _SCORE_DTYPE,
    "KinhTePhapLuat": _SCORE_DTYPE,
    "TinHoc": _SCORE_DTYPE,
    "CongNgheCongNghiep": _SCORE_DTYPE,
    "CongNgheNongNghiep": _SCORE_DTYPE,
    "NgoaiNgu": _SCORE_DTYPE,
    "MaMonNgoaiNgu": "category",
    "TongDiem": _SCORE_DTYPE,
    "KhoiA": _SCORE_DTYPE,
    "KhoiA1": _SCORE_DTYPE,
    "KhoiB": _SCORE_DTYPE,
    "KhoiC": _SCORE_DTYPE,
    "KhoiD": _SCORE_DTYPE,
    "KhoiA02": _SCORE_DTYPE,
    "KhoiC01": _SCORE_DTYPE,
    "KhoiD07": _SCORE_DTYPE,
}


def load_raw_csv(path: Path | str) -> pd.DataFrame:
    """Đọc CSV thô với dtype tối ưu bộ nhớ, đổi tên cột sang snake_case.

    Giữ SBD dạng string (string, không phải int) để không mất số 0 dẫn đầu.
    """
    df = pd.read_csv(path, dtype=_DTYPE_MAP)
    df = df.rename(columns=RAW_TO_INTERNAL)
    df["province_name"] = df["province_code"].map(PROVINCE_MAP).astype("category")
    return df


def check_sbd_consistency(df: pd.DataFrame) -> pd.Series:
    """Kiểm tra sbd = zfill(province_code, 2) + zfill(sbd_seq, 6).

    Trả về Series boolean (True = khớp) để phát hiện dòng dữ liệu bất
    thường (SBD không khớp cấu trúc kỳ vọng).
    """
    expected = (
        df["province_code"].astype(int).astype(str).str.zfill(2)
        + df["sbd_seq"].astype(int).astype(str).str.zfill(6)
    )
    return df["sbd"].astype(str) == expected


def check_duplicate_sbd(df: pd.DataFrame) -> pd.DataFrame:
    """Trả về các dòng có SBD trùng lặp (nếu có)."""
    return df[df["sbd"].duplicated(keep=False)].sort_values("sbd")


def check_score_range(df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
    """Trả về các dòng có điểm ngoài khoảng [0, 10] ở bất kỳ môn nào."""
    columns = columns or SUBJECT_COLUMNS
    mask = pd.Series(False, index=df.index)
    for c in columns:
        mask |= (df[c] < 0) | (df[c] > 10)
    return df[mask]

def check_score_step(df: pd.DataFrame, columns: list[str] | None = None, step: float = 0.25) -> pd.DataFrame:
    """Trả về các dòng có điểm không chia hết cho `step` (lệch thang điểm)."""
    columns = columns or SUBJECT_COLUMNS
    mask = pd.Series(False, index=df.index)
    for c in columns:
        vals = df[c].dropna()
        ratio = (vals / step).round()
        off = (vals - ratio * step).abs() > 1e-4
        mask |= off.reindex(df.index, fill_value=False)
    return df[mask]


def n_subjects_taken(df: pd.DataFrame) -> pd.Series:
    """Số môn đã thi của mỗi thí sinh (dựa trên các cột không rỗng)."""
    return df[SUBJECT_COLUMNS].notna().sum(axis=1)


def elective_subjects_taken(row: pd.Series) -> tuple[str, ...]:
    """Trả về tuple các môn tự chọn mà thí sinh (1 dòng) đã thi."""
    return tuple(s for s in ELECTIVE_SUBJECTS if pd.notna(row[s]))

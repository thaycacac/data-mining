import numpy as np
import pandas as pd
import pytest

from src.preprocessing import (
    PROVINCE_MAP,
    SUBJECT_COLUMNS,
    check_duplicate_sbd,
    check_sbd_consistency,
    check_score_range,
    check_score_step,
    elective_subjects_taken,
    n_subjects_taken,
)


def _make_df(rows: list[dict]) -> pd.DataFrame:
    base = {col: np.nan for col in SUBJECT_COLUMNS}
    base.update({"sbd": "00000000", "province_code": 1, "sbd_seq": 0})
    records = []
    for r in rows:
        rec = dict(base)
        rec.update(r)
        records.append(rec)
    df = pd.DataFrame(records)
    df["province_name"] = df["province_code"].map(PROVINCE_MAP)
    return df


def test_check_sbd_consistency_detects_mismatch():
    df = _make_df([
        {"sbd": "01000001", "province_code": 1, "sbd_seq": 1},
        {"sbd": "99999999", "province_code": 1, "sbd_seq": 2},  # mismatch
    ])
    ok = check_sbd_consistency(df)
    assert ok.tolist() == [True, False]


def test_check_duplicate_sbd():
    df = _make_df([
        {"sbd": "01000001", "province_code": 1, "sbd_seq": 1},
        {"sbd": "01000001", "province_code": 1, "sbd_seq": 1},
        {"sbd": "01000002", "province_code": 1, "sbd_seq": 2},
    ])
    dup = check_duplicate_sbd(df)
    assert len(dup) == 2


def test_check_score_range_flags_out_of_bounds():
    df = _make_df([
        {"toan": 8.5, "ngu_van": 7.0},
        {"toan": 10.5, "ngu_van": 7.0},  # invalid
        {"toan": -1.0, "ngu_van": 7.0},  # invalid
    ])
    bad = check_score_range(df, columns=["toan", "ngu_van"])
    assert len(bad) == 2


def test_check_score_step_flags_off_grid():
    df = _make_df([
        {"ngu_van": 7.25},  # on 0.25 grid
        {"ngu_van": 7.30},  # off grid
    ])
    off = check_score_step(df, columns=["ngu_van"], step=0.25)
    assert len(off) == 1


def test_n_subjects_taken_counts_non_null_subjects():
    df = _make_df([
        {"toan": 8.0, "ngu_van": 7.0, "vat_ly": 6.0, "hoa_hoc": 5.0},
        {"toan": 8.0, "ngu_van": 7.0},
    ])
    counts = n_subjects_taken(df)
    assert counts.tolist() == [4, 2]


def test_elective_subjects_taken_returns_only_taken_electives():
    df = _make_df([{"toan": 8.0, "ngu_van": 7.0, "vat_ly": 6.0, "hoa_hoc": 5.0}])
    taken = elective_subjects_taken(df.iloc[0])
    assert set(taken) == {"vat_ly", "hoa_hoc"}


def test_province_map_has_34_provinces():
    assert len(PROVINCE_MAP) == 34
    assert len(set(PROVINCE_MAP.values())) == 34  # tên tỉnh không trùng

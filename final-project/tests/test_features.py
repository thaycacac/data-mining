import numpy as np
import pandas as pd

from src.preprocessing import PROVINCE_MAP, SUBJECT_COLUMNS
from src.features import (
    build_province_features,
    build_site_features,
    build_transactions_df,
    discretize_score,
    filter_standard_candidates,
    scale_features,
)

EDGES = [0, 5, 6.5, 8, 10.01]
LABELS = ["Yeu", "TrungBinh", "Kha", "Gioi"]


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


def test_discretize_score_boundaries():
    s = pd.Series([4.99, 5.0, 6.49, 6.5, 7.99, 8.0, 10.0])
    bands = discretize_score(s, EDGES, LABELS)
    assert list(bands) == ["Yeu", "TrungBinh", "TrungBinh", "Kha", "Kha", "Gioi", "Gioi"]


def test_filter_standard_candidates_keeps_only_4_subject_with_compulsory():
    df = _make_df([
        {"sbd": "01000001", "toan": 8.0, "ngu_van": 7.0, "vat_ly": 6.0, "hoa_hoc": 5.0},  # keep
        {"sbd": "01000002", "toan": 8.0, "ngu_van": 7.0, "vat_ly": 6.0},  # 3 subjects, drop
        {"sbd": "01000003", "ngu_van": 7.0, "vat_ly": 6.0, "hoa_hoc": 5.0, "sinh_hoc": 4.0},  # missing toan, drop
    ])
    out = filter_standard_candidates(df)
    assert out["sbd"].tolist() == ["01000001"]


def test_build_transactions_df_generates_choice_and_band_items():
    df = _make_df([{"sbd": "01000001", "toan": 8.5, "ngu_van": 6.0, "vat_ly": 7.0, "hoa_hoc": 9.0}])
    tx = build_transactions_df(df, EDGES, LABELS)
    items = set(tx["item"])
    assert "Chon_VatLy" in items
    assert "Chon_HoaHoc" in items
    assert "Toan_Gioi" in items  # 8.5 >= 8
    assert "NguVan_TrungBinh" in items  # 6.0 in [5, 6.5)


def test_build_province_features_shape_and_rates():
    df = _make_df([
        {"province_code": 1, "toan": 9.0, "ngu_van": 8.5, "vat_ly": 4.0},
        {"province_code": 1, "toan": 4.0, "ngu_van": 8.5},
    ])
    feat = build_province_features(df)
    assert feat.loc["Hà Nội", "n_candidates"] == 2
    assert feat.loc["Hà Nội", "Toan_pct_gioi"] == 0.5  # 1/2 >= 8
    assert feat.loc["Hà Nội", "Toan_pct_yeu"] == 0.5  # 1/2 < 5


def test_scale_features_zero_mean():
    df = pd.DataFrame({"a": [1.0, 2.0, 3.0], "b": [10.0, 20.0, 30.0]})
    scaled, scaler = scale_features(df, columns=["a", "b"])
    assert np.allclose(scaled.mean().values, 0, atol=1e-8)


def test_build_site_features_respects_min_group_size():
    rows = [{"sbd": f"01{str(i).zfill(6)}", "province_code": 1, "sbd_seq": i, "toan": 7.0, "ngu_van": 7.0}
            for i in range(5)]  # only 5 candidates, below default min_group_size=10
    df = _make_df(rows)
    site = build_site_features(df, ["toan", "ngu_van"], min_group_size=10)
    assert len(site) == 0

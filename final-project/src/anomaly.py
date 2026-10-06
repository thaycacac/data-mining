"""Phát hiện bất thường (GIAI ĐOẠN 4.3 / RQ3).

Mọi kết quả ở đây chỉ được diễn đạt là "bất thường về mặt thống kê, cần
xem xét thêm" — không kết luận gian lận hay quy trách nhiệm cho bất kỳ
đơn vị cụ thể nào (xem mục Đạo đức dữ liệu, final_report.md).
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import StandardScaler

RANDOM_SEED = 42


# ---------------------------------------------------------------------
# Baseline thống kê: Z-score / IQR + kiểm định dồn điểm (heaping)
# ---------------------------------------------------------------------

def zscore_outliers(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """Trả về boolean Series: True nếu |z-score| > threshold."""
    z = (series - series.mean()) / series.std()
    return z.abs() > threshold


def iqr_outliers(series: pd.Series, k: float = 1.5) -> pd.Series:
    """Trả về boolean Series theo quy tắc IQR (Tukey's fences)."""
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    return (series < q1 - k * iqr) | (series > q3 + k * iqr)


def heaping_ratio(
    value_counts: pd.Series,
    target: float,
    neighbors: tuple[float, float],
) -> dict:
    """So sánh tần suất tại `target` với trung bình nội suy từ 2 giá trị
    lân cận `neighbors`. Trả về dict gồm observed, expected, ratio.

    Dùng kiểm định xấp xỉ Poisson (observed vs expected) để ước lượng
    mức ý nghĩa thống kê của độ lệch — chỉ mang tính mô tả, không khẳng
    định nguyên nhân.
    """
    observed = value_counts.get(target, 0)
    expected = (value_counts.get(neighbors[0], 0) + value_counts.get(neighbors[1], 0)) / 2
    ratio = observed / expected if expected > 0 else np.nan
    # z-test xấp xỉ Poisson: (O - E) / sqrt(E)
    z = (observed - expected) / np.sqrt(expected) if expected > 0 else np.nan
    return {"observed": observed, "expected": expected, "ratio": ratio, "z_approx": z}


def heaping_by_group(
    df: pd.DataFrame,
    score_col: str,
    group_col: str,
    target: float,
    neighbors: tuple[float, float],
    min_group_size: int = 500,
) -> pd.DataFrame:
    """Áp dụng heaping_ratio cho từng nhóm (vd theo tỉnh)."""
    rows = []
    for name, g in df.groupby(group_col, observed=True):
        if len(g) < min_group_size:
            continue
        vc = g[score_col].value_counts()
        res = heaping_ratio(vc, target, neighbors)
        res[group_col] = name
        res["n"] = len(g)
        rows.append(res)
    return pd.DataFrame(rows).set_index(group_col).sort_values("ratio", ascending=False)


# ---------------------------------------------------------------------
# Isolation Forest & Local Outlier Factor
# ---------------------------------------------------------------------

def _prepare_matrix(df: pd.DataFrame, columns: list[str]) -> tuple[np.ndarray, pd.Index]:
    sub = df[columns].dropna()
    scaler = StandardScaler()
    X = scaler.fit_transform(sub)
    return X, sub.index


def isolation_forest_scores(
    df: pd.DataFrame,
    columns: list[str],
    n_estimators: int = 200,
    contamination: float = 0.02,
) -> pd.Series:
    """Trả về Series điểm bất thường (càng âm/nhỏ càng bất thường), index
    khớp với các dòng không có giá trị thiếu trong `columns`."""
    X, idx = _prepare_matrix(df, columns)
    model = IsolationForest(
        n_estimators=n_estimators, contamination=contamination, random_state=RANDOM_SEED
    )
    model.fit(X)
    scores = model.decision_function(X)
    return pd.Series(scores, index=idx, name="isolation_forest_score")


def lof_scores(
    df: pd.DataFrame,
    columns: list[str],
    n_neighbors: int = 20,
    contamination: float = 0.02,
) -> pd.Series:
    """Trả về Series điểm bất thường LOF (càng âm càng bất thường)."""
    X, idx = _prepare_matrix(df, columns)
    n_neighbors = min(n_neighbors, len(X) - 1)
    model = LocalOutlierFactor(n_neighbors=n_neighbors, contamination=contamination)
    model.fit_predict(X)
    scores = model.negative_outlier_factor_
    return pd.Series(scores, index=idx, name="lof_score")


def top_n_anomalies(scores: pd.Series, n: int) -> set:
    """Trả về tập index của n đơn vị bất thường nhất (điểm thấp nhất)."""
    return set(scores.sort_values().head(n).index)


def jaccard(set_a: set, set_b: set) -> float:
    if not set_a and not set_b:
        return 1.0
    return len(set_a & set_b) / len(set_a | set_b)


def stability_across_contamination(
    df: pd.DataFrame,
    columns: list[str],
    contaminations: list[float],
    top_n: int,
    method: str = "isolation_forest",
) -> pd.DataFrame:
    """Đo độ ổn định của top-N bất thường khi đổi contamination, so với
    cấu hình đầu tiên trong danh sách làm mốc tham chiếu."""
    score_fn = isolation_forest_scores if method == "isolation_forest" else lof_scores
    ref_scores = score_fn(df, columns, contamination=contaminations[0])
    ref_top = top_n_anomalies(ref_scores, top_n)

    rows = []
    for c in contaminations:
        scores = score_fn(df, columns, contamination=c)
        top = top_n_anomalies(scores, top_n)
        rows.append({"contamination": c, "jaccard_vs_ref": jaccard(ref_top, top)})
    return pd.DataFrame(rows)

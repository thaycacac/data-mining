"""Hàm trực quan hóa dùng chung cho các notebook.

Giữ style nhất quán (seaborn whitegrid, font đủ hiển thị tiếng Việt có
dấu), và luôn lưu hình vào reports/figures/ với tên rõ nghĩa.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"

sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.dpi"] = 110


def save_fig(fig: plt.Figure, name: str) -> Path:
    """Lưu figure vào reports/figures/<name>.png (tạo thư mục nếu cần)."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    path = FIGURES_DIR / f"{name}.png"
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    return path


def plot_score_distribution(df: pd.DataFrame, subject_col: str, subject_label: str, ax=None):
    """Vẽ histogram phổ điểm 1 môn, có đường trung bình/trung vị."""
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 4))
    data = df[subject_col].dropna()
    sns.histplot(data, bins=41, binrange=(0, 10), ax=ax, color="#3b6fa0")
    ax.axvline(data.mean(), color="red", linestyle="--", label=f"TB = {data.mean():.2f}")
    ax.axvline(data.median(), color="orange", linestyle=":", label=f"Trung vị = {data.median():.2f}")
    ax.set_xlabel(f"Điểm {subject_label}")
    ax.set_ylabel("Số thí sinh")
    ax.set_title(f"Phổ điểm môn {subject_label} (n={len(data):,})")
    ax.legend()
    return ax

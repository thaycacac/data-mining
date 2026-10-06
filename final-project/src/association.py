"""Luật kết hợp (Association Rule Mining) trên bảng giao dịch môn thi.

Dùng FP-Growth (mlxtend) làm thuật toán chính trên toàn bộ dữ liệu, và
Apriori trên một mẫu con để minh họa so sánh hiệu năng (yêu cầu GIAI
ĐOẠN 4.1).
"""

from __future__ import annotations

import time

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth


def run_fpgrowth(onehot: pd.DataFrame, min_support: float) -> tuple[pd.DataFrame, float]:
    """Chạy FP-Growth, trả về (frequent_itemsets, thời gian chạy giây)."""
    t0 = time.time()
    itemsets = fpgrowth(onehot, min_support=min_support, use_colnames=True)
    return itemsets, time.time() - t0


def run_apriori(onehot: pd.DataFrame, min_support: float) -> tuple[pd.DataFrame, float]:
    """Chạy Apriori, trả về (frequent_itemsets, thời gian chạy giây)."""
    t0 = time.time()
    itemsets = apriori(onehot, min_support=min_support, use_colnames=True)
    return itemsets, time.time() - t0


def compare_runtime(
    onehot: pd.DataFrame,
    sample_sizes: list[int],
    min_support: float,
    random_state: int = 42,
) -> pd.DataFrame:
    """So sánh thời gian chạy Apriori vs FP-Growth trên các cỡ mẫu tăng dần.

    Minh họa Apriori chậm đi nhanh hơn FP-Growth khi số giao dịch tăng,
    do Apriori phải quét lại dữ liệu nhiều lần để sinh ứng viên, trong
    khi FP-Growth chỉ quét 2 lần và khai thác trên cấu trúc cây nén (FP-tree).
    """
    rows = []
    for n in sample_sizes:
        sample = onehot.sample(n=min(n, len(onehot)), random_state=random_state)
        _, t_apriori = run_apriori(sample, min_support)
        _, t_fpgrowth = run_fpgrowth(sample, min_support)
        rows.append({"n_transactions": n, "apriori_sec": t_apriori, "fpgrowth_sec": t_fpgrowth})
    return pd.DataFrame(rows)


def _subject_of(item: str) -> str:
    """Trả về tên môn gốc từ item dạng 'Chon_<Mon>' hoặc '<Mon>_<Muc>'."""
    if item.startswith("Chon_"):
        return item[len("Chon_"):]
    return item.rsplit("_", 1)[0]


def _is_trivial_rule(antecedents: frozenset, consequents: frozenset) -> bool:
    """Loại luật hiển nhiên: hệ quả là 'Chon_<Mon>' trong khi tiền đề đã
    chứa item '<Mon>_<Muc>' của cùng môn đó — luôn đúng 100% theo định
    nghĩa dữ liệu (có điểm môn nào thì chắc chắn đã chọn thi môn đó),
    không mang thông tin khai phá mới."""
    for cons in consequents:
        if cons.startswith("Chon_"):
            subj = cons[len("Chon_"):]
            if any(not a.startswith("Chon_") and _subject_of(a) == subj for a in antecedents):
                return True
    return False


def generate_rules(
    frequent_itemsets: pd.DataFrame,
    min_confidence: float,
    min_lift: float = 1.0,
) -> pd.DataFrame:
    """Sinh luật từ frequent itemsets, lọc lift > min_lift và loại luật
    hiển nhiên (xem _is_trivial_rule)."""
    if frequent_itemsets.empty:
        return pd.DataFrame()
    rules = association_rules(
        frequent_itemsets, metric="confidence", min_threshold=min_confidence,
        num_itemsets=len(frequent_itemsets),
    )
    rules = rules[rules["lift"] > min_lift].copy()
    trivial = rules.apply(
        lambda r: _is_trivial_rule(r["antecedents"], r["consequents"]), axis=1
    )
    rules = rules[~trivial]
    rules["antecedents_str"] = rules["antecedents"].apply(lambda s: ", ".join(sorted(s)))
    rules["consequents_str"] = rules["consequents"].apply(lambda s: ", ".join(sorted(s)))
    return rules.sort_values("lift", ascending=False).reset_index(drop=True)


def top_rules(rules: pd.DataFrame, n: int = 15) -> pd.DataFrame:
    cols = ["antecedents_str", "consequents_str", "support", "confidence", "lift", "conviction"]
    cols = [c for c in cols if c in rules.columns]
    return rules.sort_values("lift", ascending=False).head(n)[cols]

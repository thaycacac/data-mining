"""Phân cụm 34 tỉnh/thành theo đặc điểm điểm thi (GIAI ĐOẠN 4.2 / RQ2)."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage
from sklearn.cluster import DBSCAN, AgglomerativeClustering, KMeans
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

RANDOM_SEED = 42


def elbow_silhouette(X: np.ndarray, k_range: range) -> pd.DataFrame:
    """Tính inertia (Elbow) và Silhouette score cho mỗi k trong k_range."""
    rows = []
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=RANDOM_SEED, n_init=10)
        labels = km.fit_predict(X)
        sil = silhouette_score(X, labels) if k > 1 else np.nan
        rows.append({"k": k, "inertia": km.inertia_, "silhouette": sil})
    return pd.DataFrame(rows)


def fit_kmeans(X: np.ndarray, k: int) -> tuple[np.ndarray, KMeans]:
    km = KMeans(n_clusters=k, random_state=RANDOM_SEED, n_init=10)
    labels = km.fit_predict(X)
    return labels, km


def fit_hierarchical(X: np.ndarray, k: int, method: str = "ward") -> tuple[np.ndarray, np.ndarray]:
    """Trả về (labels, linkage_matrix). linkage_matrix dùng để vẽ dendrogram."""
    Z = linkage(X, method=method)
    model = AgglomerativeClustering(n_clusters=k, linkage=method)
    labels = model.fit_predict(X)
    return labels, Z


def fit_dbscan(X: np.ndarray, eps: float, min_samples: int) -> np.ndarray:
    model = DBSCAN(eps=eps, min_samples=min_samples)
    return model.fit_predict(X)


def fit_gmm(X: np.ndarray, k: int) -> tuple[np.ndarray, GaussianMixture]:
    model = GaussianMixture(n_components=k, random_state=RANDOM_SEED)
    labels = model.fit_predict(X)
    return labels, model


def scan_dbscan_eps(X: np.ndarray, eps_range: list[float], min_samples: int) -> pd.DataFrame:
    """Quét eps để chọn tham số DBSCAN hợp lý (silhouette chỉ tính khi >=2
    cụm thật sự, bỏ qua điểm nhiễu -1)."""
    rows = []
    for eps in eps_range:
        labels = fit_dbscan(X, eps, min_samples)
        n_clusters = len(set(labels) - {-1})
        n_noise = int((labels == -1).sum())
        sil = np.nan
        if n_clusters >= 2:
            mask = labels != -1
            if mask.sum() > n_clusters:
                sil = silhouette_score(X[mask], labels[mask])
        rows.append({"eps": eps, "n_clusters": n_clusters, "n_noise": n_noise, "silhouette": sil})
    return pd.DataFrame(rows)


def pca_2d(X: np.ndarray) -> tuple[np.ndarray, PCA]:
    pca = PCA(n_components=2, random_state=RANDOM_SEED)
    coords = pca.fit_transform(X)
    return coords, pca


def profile_clusters(raw_df: pd.DataFrame, labels: np.ndarray, columns: list[str]) -> pd.DataFrame:
    """Trung bình các đặc trưng (thang gốc, chưa chuẩn hóa) theo từng cụm —
    dùng để diễn giải "chân dung" cụm."""
    tmp = raw_df[columns].copy()
    tmp["cluster"] = labels
    return tmp.groupby("cluster").mean().round(2)

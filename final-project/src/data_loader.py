"""Tải và nạp dữ liệu điểm thi THPT từ nguồn gốc (GitHub LFS) vào data/raw/.

data/raw/ là bất biến: hàm download ở đây không bao giờ ghi đè file đã tồn
tại, trừ khi gọi với overwrite=True.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

import requests
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_config(config_path: Path | str = PROJECT_ROOT / "config.yaml") -> dict[str, Any]:
    """Đọc config.yaml thành dict."""
    with open(config_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_file(url: str, dest: Path, *, overwrite: bool = False, timeout: int = 300) -> Path:
    """Tải file qua HTTP streaming, lưu vào dest. Không ghi đè nếu đã tồn tại."""
    dest = Path(dest)
    if dest.exists() and not overwrite:
        print(f"[skip] {dest} đã tồn tại ({dest.stat().st_size:,} bytes)")
        return dest

    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp_dest = dest.with_suffix(dest.suffix + ".part")
    print(f"[download] {url} -> {dest}")
    with requests.get(url, stream=True, timeout=timeout) as r:
        r.raise_for_status()
        total = int(r.headers.get("content-length", 0))
        written = 0
        with open(tmp_dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                f.write(chunk)
                written += len(chunk)
        if total and written != total:
            raise IOError(f"Tải thiếu: nhận {written} bytes, kỳ vọng {total} bytes")
    tmp_dest.rename(dest)
    print(f"[done] {dest} ({dest.stat().st_size:,} bytes)")
    return dest


def _count_csv_rows(path: Path) -> int:
    with open(path, newline="", encoding="utf-8") as f:
        return sum(1 for _ in f) - 1  # trừ header


def fetch_raw_data(config: dict[str, Any] | None = None, *, overwrite: bool = False) -> dict[str, Path]:
    """Tải toàn bộ nguồn dữ liệu khai báo trong config.yaml['data_sources'] vào data/raw/.

    Trả về dict {source_key: local_path}. Kiểm tra số dòng/số tỉnh với
    nguồn 2026 (main) để phát hiện sớm nếu nguồn dữ liệu bị thay đổi.
    """
    config = config or load_config()
    raw_dir = PROJECT_ROOT / config["paths"]["raw_dir"]
    results: dict[str, Path] = {}

    for key, src in config["data_sources"].items():
        dest = raw_dir / src["local_name"]
        path = download_file(src["url"], dest, overwrite=overwrite)
        results[key] = path

        expected_rows = src.get("expected_rows")
        if expected_rows is not None:
            n_rows = _count_csv_rows(path)
            if n_rows != expected_rows:
                print(
                    f"[warn] {key}: số dòng thực tế {n_rows} khác kỳ vọng "
                    f"{expected_rows} — kiểm tra lại nguồn dữ liệu."
                )
            else:
                print(f"[verify] {key}: {n_rows} dòng khớp kỳ vọng.")

        expected_provinces = src.get("expected_provinces")
        if expected_provinces is not None:
            with open(path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                provinces = {row["Tinh"] for row in reader}
            if len(provinces) != expected_provinces:
                print(
                    f"[warn] {key}: số tỉnh thực tế {len(provinces)} khác "
                    f"kỳ vọng {expected_provinces}."
                )
            else:
                print(f"[verify] {key}: {len(provinces)} tỉnh khớp kỳ vọng.")

    return results


if __name__ == "__main__":
    fetch_raw_data()

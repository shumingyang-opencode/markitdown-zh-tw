#!/usr/bin/env python3
"""Localize graphify's graph.html UI to Traditional Chinese -> graph-zh.html.

Only the UI chrome is translated: page title, search placeholder, panel
headings, neighbors label, legend header, stats line and community-name
placeholders. Node labels (code identifiers) are kept as-is, per the
site-wide localization policy.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "worked" / "markitdown-source" / "graph.html"
DST = ROOT / "worked" / "markitdown-source" / "graph-zh.html"

REPLACEMENTS = [
    # (原字串, 取代字串)
    ('<html lang="en">', '<html lang="zh-Hant">'),
    ("graphify - graphify-out/graph.html", "graphify — markitdown 源碼知識圖譜（中文化界面）"),
    ('placeholder="Search nodes..."', 'placeholder="搜尋節點..."'),
    ("<h3>Node Info</h3>", "<h3>節點資訊</h3>"),
    ('<span class="empty">Click a node to inspect it</span>',
     '<span class="empty">點擊節點以檢視</span>'),
    ("<h3>Communities</h3>", "<h3>社群</h3>"),
    ("Select All", "全選"),
    ("Neighbors (${neighborIds.length})", "相鄰節點 (${neighborIds.length})"),
]


def localize(raw: str) -> str:
    out = raw
    for old, new in REPLACEMENTS:
        out = out.replace(old, new)
    # 統計列：907 nodes · 1967 edges · 71 communities
    out = re.sub(
        r"(\d+) nodes &middot; (\d+) edges &middot; (\d+) communities",
        r"\1 節點 · \2 邊 · \3 社群",
        out,
    )
    # 資料中的社群預設名 "Community N" -> "社群 N"（placeholder，非程式識別符）
    out = re.sub(r'"community_name": "Community ', '"community_name": "社群 ', out)
    return out


def main() -> None:
    if not SRC.exists():  # pragma: no cover
        print(f"找不到 {SRC}", file=sys.stderr)
        sys.exit(1)
    raw = SRC.read_text(encoding="utf-8")
    DST.write_text(localize(raw), encoding="utf-8")
    print(f"已產生 {DST}（{(DST.stat().st_size / 1024):.0f} KB）")


if __name__ == "__main__":
    main()

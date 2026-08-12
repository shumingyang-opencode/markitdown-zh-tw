# worked/markitdown-source — graphify 互動知識圖譜

本站用 **graphify 0.9.40** 掃描 MarkItDown 上游源碼產出的知識圖譜（**本站實跑**，`--code-only`，
純本機 AST、零 LLM、零 token 成本）。

## 語料

- 來源：`microsoft/markitdown`，對齊分支 `main`，釘選 commit **`fd239d5`**（v0.1.7）
- 內容：`packages/` 四個套件的 `src/` + `tests/`（190 個檔案、其中 77 個程式檔）
- 準備方式：`git clone` 後把 `packages/` 與根目錄 Dockerfile 複製到語料目錄

## 本站跑出的數字

| 項目 | 數值 |
|------|------|
| 節點 | 907 |
| 邊 | 1,967（91% EXTRACTED · 9% INFERRED） |
| 社群 | 71 |
| Token 成本 | 0（純本機） |
| 圖資料 | 907 節點 < 5,000 視覺化上限，互動圖含完整節點細節 |

## 重現方式

```bash
# 1. 準備語料（以釘選 commit）
git clone https://github.com/microsoft/markitdown.git
git -C markitdown checkout fd239d5d2be43d9b68329730206b9312c7d5a388
mkdir -p raw/corpus && cp -R markitdown/packages raw/corpus/ && cp markitdown/Dockerfile raw/corpus/

# 2. 抽取（--code-only 零 key；raw/ 在 .gitignore，需 --no-gitignore 讓 graphify 看到）
graphify extract raw/corpus --code-only --no-gitignore

# 3. 分群 + 產出 graph.html / GRAPH_REPORT.md
graphify cluster-only raw/corpus --no-label

# 4. 收錄 + 中文化
cp raw/corpus/graphify-out/graph.html worked/markitdown-source/
cp raw/corpus/graphify-out/GRAPH_REPORT.md worked/markitdown-source/
python scripts/localize-graph.py   # 產生 graph-zh.html（中文化界面）
```

## 檔案說明

- `graph.html` — 英文界面互動圖（拖曳、搜尋、點節點）
- `graph-zh.html` — 中文界面互動圖（`lang="zh-Hant"`，UI 字串中文化，節點標籤保留英文）
- `GRAPH_REPORT.md` — graphify 自動產生的結構報告（god nodes、社群、surprising connections）

## 已知限制

- 社群命名：本機無 LLM key，社群名稱保留「社群 N」placeholder；節點標籤是程式識別符，保持英文。
- 語料含 `tests/`（測試程式碼），因此圖中混有大量測試節點——這是刻意的，可觀察「測試如何呼叫主程式」。
- `raw/` 目錄為本機暫存（.gitignore），未提交至 repo。

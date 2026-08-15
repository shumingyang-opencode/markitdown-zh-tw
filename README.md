# markitdown-zh-tw · MarkItDown 繁體中文教學站

[MarkItDown](https://github.com/microsoft/markitdown) 的**非官方**繁體中文教學站。把整個 repo
（程式碼、轉換器、CLI、外掛、MCP、Azure、測試）做成中英對照的解說內容，並收錄本站實際用
markitdown 產出的**真實轉換輸出**與用 graphify 掃描源碼的**互動知識圖譜**。

> **免責聲明**：本站為第三方社群教學站，**與 Microsoft / AutoGen Team 無關**，不代表 MarkItDown 官方立場。
> MarkItDown 為 Microsoft Corporation 的商標，本站僅在描述性／教學語境下使用該名稱。

**上線網站：<https://shumingyang-opencode.github.io/markitdown-zh-tw/>**

## 目錄

- [網站亮點](#網站亮點)
- [網站地圖](#網站地圖)
- [實作案例總覽](#實作案例總覽)
- [我們怎麼跑的](#我們怎麼跑的)
- [授權](#授權)
- [上游同步](#上游同步)
- [開發](#開發)
- [如何新增一個轉換案例](#如何新增一個轉換案例)
- [已知限制](#已知限制)
- [回饋與貢獻](#回饋與貢獻)

---

## 網站亮點

1. **中英對照** — 中文口語解說為主文，英文原文與程式碼保留上游原貌。文件頁用「可展開的英文原文」，程式碼頁用「附中文註解的原始碼」。
2. **Python 逐函數講解** — 核心 `_markitdown.py`、CLI、converter 協定、Office/PDF/Web/Media 轉換器、OMML 數學、外掛與 MCP 套件，每個函數一個 `<details>` 收縮塊。
3. **策展式教學而非鏡像** — 不逐檔翻譯，聚焦 22 個轉換器、調度管線、外掛系統、Azure 整合、MCP。
4. **真實轉換輸出** — 本站用 markitdown 0.1.7 實跑 11 種格式（DOCX/XLSX/PPTX/PDF/HTML/CSV/JSON/圖片/音訊/ZIP/EPUB）的前後對照，含一次真實的失敗示範。
5. **meta 示範** — 用 markitdown 轉 markitdown 自己（dogfooding），並用 graphify 掃描源碼出互動知識圖譜（EN/ZH 雙版本）。
6. **版本釘選** — 上游對齊 `main @ fd239d5`（發行版 v0.1.7）；所有實測數字為本站實際運行取得，可追溯。

## 網站地圖

純靜態站（HTML + CSS + JS），GitHub Pages 部署於 `main` 根目錄。

```
markitdown-zh-tw/
├── index.html            首頁：MarkItDown 是什麼、三大亮點、入口卡、版本徽章
├── map.html              概念地圖：converter/priority/StreamInfo/magika/plugin/MCP/Azure
├── learning-path.html    學習路線 L0→L4：可點卡片
├── install.html          安裝指南：pip extras、uv、conda、source、Docker、疑難排解
├── about.html            授權、方法、免責聲明
├── docs/
│   ├── index.html        文件教學入口（hub）
│   ├── how-it-works.html 運作原理（調度管線：猜測→排序→accepts→convert→標準化）
│   ├── architecture.html 架構總覽（4 套件 + 核心類別職責表）
│   ├── converters.html   22 個轉換器全覽表
│   ├── cli.html          CLI 指令參考
│   ├── python-api.html   Python API（5 個 convert_* + StreamInfo）
│   ├── plugins.html      外掛系統（entry-point + markitdown-ocr + sample-plugin）
│   ├── mcp.html          markitdown-mcp（STDIO/HTTP/SSE、Docker、Claude Desktop、安全）
│   ├── cloud.html        Azure Document Intelligence vs Content Understanding
│   ├── docker.html       Docker 用法
│   ├── security.html     安全模型（I/O 權限、Sanitize、最窄 convert_*）
│   ├── worked.html       實作案例入口
│   ├── case/             五個案例頁
│   └── code/             程式碼對照（13 頁，逐函數 <details>）
│       ├── index.html    入口
│       ├── core.html     _markitdown.py（MarkItDown 類別）
│       ├── cli.html      __main__.py（argparse）
│       ├── base.html     _base_converter.py（converter 協定）
│       ├── stream-info.html  _stream_info/_uri_utils/_exceptions
│       ├── converters.html  協定實作 + 文字家族 + _markdownify
│       ├── office.html   docx（含 OMML 數學）/ xlsx / pptx
│       ├── pdf.html      _pdf_converter.py
│       ├── web.html      youtube/wikipedia/rss/zip/epub/outlook
│       ├── media.html    image/audio + exiftool/llm_caption/transcribe_audio
│       ├── cloud.html    _doc_intel / _cu
│       ├── mcp.html      markitdown-mcp 套件
│       └── ocr.html      markitdown-ocr + markitdown-sample-plugin
├── worked/
│   ├── conversions/      11 種格式的輸入樣本檔 + 轉換輸出 + README（含指令）
│   ├── dogfood/          MarkItDown 轉自己（README/pyproject/Dockerfile/GitHub 頁/PyPI 頁）
│   └── markitdown-source/ graphify 互動圖（graph.html + graph-zh.html）+ GRAPH_REPORT.md
├── scripts/
│   ├── generate-samples.py  產生各格式樣本輸入檔
│   └── localize-graph.py    graph.html → graph-zh.html（UI 中文化）
├── assets/               site.css / favicon.svg
└── LICENSE / NOTICE / GITHUB_META.md / .github/workflows/check-upstream.yml
```

## 實作案例總覽

每個案例都是「中文解說 + 真實輸出 + 本站跑的數字 + 重現步驟」。

| 案例 | 內容 | 來源方式 | 本站數字/結果 |
|---|---|---|---|
| [**Office 轉換**](docs/case/office.html) | DOCX / XLSX / PPTX | **本站實跑** 0.1.7 | 標題/清單/表格全保留；Excel 合併列會併入表格 |
| [**PDF + 網頁**](docs/case/pdf-web.html) | PDF / HTML / CSV / JSON | **本站實跑** 0.1.7 | PDF 抽取順序依版面；HTML 最擅長 |
| [**媒體 + 封裝**](docs/case/media-archive.html) | 圖片 / 音訊 / ZIP / EPUB | **本站實跑** 0.1.7 + exiftool 13.59 | 圖片 EXIF ✅；音訊純音調 → `UnknownValueError`（真實失敗示範） |
| [**Dogfood**](docs/case/dogfood.html) | README / pyproject / Dockerfile / GitHub 頁 / PyPI 頁 | **本站實跑** 0.1.7 | 純文字近乎無損；通用 HTML 會帶導覽雜訊 |
| [**graphify 掃描**](docs/case/markitdown-source.html) | markitdown 源碼（77 程式檔） | **本站實跑** graphify 0.9.40 `--code-only` | 907 節點 / 1,967 邊 / 71 社群 |

> 所有案例都是**真實工具產出**，不是示意圖。這是「用轉換工具分析轉換工具、用知識圖譜工具分析轉換工具」的 meta 示範。

## 我們怎麼跑的

### 真實轉換（markitdown 0.1.7）

```bash
# 0. 建立 uv 虛擬環境，從對齊 commit 的源碼安裝
uv venv .venv --python 3.12
uv pip install -p .venv -e "<markitdown>/packages/markitdown[all]"

# 1. 產生樣本輸入檔（python-docx / openpyxl / python-pptx / reportlab / Pillow / piexif）
.venv/Scripts/python scripts/generate-samples.py

# 2. 逐一轉換（以 docx 為例）
.venv/Scripts/markitdown worked/conversions/office/sample-report.docx -o out.md

# 3. 圖片/音訊中繼資料需 exiftool（以 EXIFTOOL_PATH 指定）
EXIFTOOL_PATH=/path/to/exiftool .venv/Scripts/markitdown worked/conversions/media/photo.jpg -o out.md
```

### dogfood（轉自己）

```bash
.venv/Scripts/markitdown "https://raw.githubusercontent.com/microsoft/markitdown/fd239d5d2be43d9b68329730206b9312c7d5a388/README.md" -o worked/dogfood/readme.md
.venv/Scripts/markitdown <markitdown>/packages/markitdown/pyproject.toml -o worked/dogfood/pyproject.md
.venv/Scripts/markitdown https://github.com/microsoft/markitdown -o worked/dogfood/github-page.md
```

### graphify 互動圖（0.9.40，純本機零 key）

```bash
git clone https://github.com/microsoft/markitdown.git
git -C markitdown checkout fd239d5d2be43d9b68329730206b9312c7d5a388
mkdir -p raw/corpus && cp -R markitdown/packages raw/corpus/ && cp markitdown/Dockerfile raw/corpus/

graphify extract raw/corpus --code-only --no-gitignore   # raw/ 在 .gitignore 故需 --no-gitignore
graphify cluster-only raw/corpus --no-label              # → graph.html + GRAPH_REPORT.md

cp raw/corpus/graphify-out/graph.html worked/markitdown-source/
cp raw/corpus/graphify-out/GRAPH_REPORT.md worked/markitdown-source/
python scripts/localize-graph.py                         # → graph-zh.html（中文化界面）
```

## 授權

- 本站內容以 **MIT License** 釋出（與上游相同），並照抄上游的授權檔：
  - [`LICENSE`](LICENSE) — MIT 全文（`Copyright (c) Microsoft Corporation.`）
  - [`NOTICE`](NOTICE) — 本站為上游非官方教學站的聲明、引用範圍、原創內容授權
- **商標**：MarkItDown 與 Microsoft 為 Microsoft Corporation 或其關聯公司之商標。MIT 授權不含商標授權；
  本站僅在「描述性／教學」語境使用該名稱，並於全站 footer 標示「與 Microsoft 無關」。
- **graphify 產出**：`worked/markitdown-source/` 的互動圖與報告由 graphify（Apache-2.0）產生，案例頁已標註出處。
- **不做二進位散布**：本站不含官方二進位，僅引述實際運行輸出；樣本輸入檔為本站自製，轉換輸出以 markitdown 實跑取得。

## 上游同步

- 本站對齊上游分支 **`main`**，釘選 commit **`fd239d5`**（發行版 v0.1.7）。
- `.github/workflows/check-upstream.yml` **每月自動**（每月 1 日 00:00 UTC + 手動觸發）檢查上游最新 SHA，並更新首頁的版本徽章。

## 開發

靜態站，純 HTML + CSS + JS，無框架、無建置步驟。

```bash
python -m http.server 8000   # 本機預覽
```

### 目錄結構速查

- `assets/site.css` — 全站樣式（深色 × 霓虹設計語言，承襲 codegraph-zh-tw / graphify-zh-tw）
- 每個 HTML 頁都是自含檔案（head 引入 site.css + Google Fonts）
- `worked/<slug>/` — 案例資產與說明

## 如何新增一個轉換案例

1. **準備樣本**：`python scripts/generate-samples.py`（或自備檔案）。
2. **轉換**：`markitdown <file> -o out.md` 實跑（可加 `-x/-m/-c` 提示）。
3. **收錄**：輸入檔 + 輸出 `.md` 放進 `worked/conversions/<group>/`。
4. **建案例頁**：依 `docs/case/*.html` 模板（中文解說 + 輸入/輸出對照 + 本站觀察 + 重現步驟）。
5. **更新** `docs/worked.html` 的案例卡與「實作案例總覽」表。

## 已知限制

- **圖片/音訊**：EXIF 需要 exiftool；描述/OCR 需要 `llm_client + llm_model`；音訊轉錄需要真人語音 + 網路 + Google API。缺任一條件會「空輸出」或「失敗降級」——見[媒體案例](docs/case/media-archive.html)。
- **PDF**：無語意結構，抽取順序依版面；掃描檔/複雜表格是弱點，高品質需求請用 Azure Content Understanding。
- **通用 HTML**：沒有專用 converter 的網站（如 GitHub/PyPI 頁）會帶入導覽雜訊——見[dogfood 案例](docs/case/dogfood.html)。
- **Azure**：兩條雲端路徑需資源與計費，本站不實跑，僅翻譯對照官方文件。
- **graphify 社群命名**：本機無 LLM key，社群名稱保留「社群 N」placeholder。

## 回饋與貢獻

- 本站是教學站，不是官方文件。發現翻譯錯誤或想補充主題，歡迎開 [issue](https://github.com/shumingyang-opencode/markitdown-zh-tw/issues)。
- 想貢獻轉換案例：跑一個真實檔案轉換，依[新增案例流程](#如何新增一個轉換案例)發 PR。

---

**相關連結**

- 上游 repo：[microsoft/markitdown](https://github.com/microsoft/markitdown)（MIT）
- PyPI：`markitdown` · `markitdown-mcp` · `markitdown-ocr` · `markitdown-sample-plugin`
- 本站 repo：[shumingyang-opencode/markitdown-zh-tw](https://github.com/shumingyang-opencode/markitdown-zh-tw)
- 本站上線：[shumingyang-opencode.github.io/markitdown-zh-tw](https://shumingyang-opencode.github.io/markitdown-zh-tw/)
- 學習路徑建議服務：[learning-path-advisor](https://shuming-yang.github.io/learning-path-advisor/) — 依角色推薦教學網站學習路徑

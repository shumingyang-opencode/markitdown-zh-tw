# worked/conversions — 真實轉換輸出

本站實作案例的「真實轉換」部分。所有 `.md` 檔案都是本機以 **markitdown 0.1.7**
（對齊上游 `main @ fd239d5`）實際執行的輸出，不是示意圖。

## 環境

- Python 3.12.8（uv 虛擬環境）
- `markitdown[all]`，版本 0.1.7，從對齊 commit 的源碼安裝：
  `uv pip install -e "packages/markitdown[all]"`
- exiftool 13.59（圖片/音訊中繼資料用），以 `EXIFTOOL_PATH` 環境變數指定
- 樣本輸入檔由本站 `scripts/generate-samples.py` 產生（python-docx / openpyxl /
  python-pptx / reportlab / Pillow / piexif / wave / zipfile）

## 各格式轉換指令與結果

| 群組 | 輸入 | 指令 | 輸出 |
|------|------|------|------|
| office | `office/sample-report.docx` | `markitdown office/sample-report.docx -o office/sample-report.md` | ✅ 保留標題/清單/表格 |
| office | `office/sales-data.xlsx` | `markitdown office/sales-data.xlsx -o office/sales-data.md` | ✅ 工作表 → Markdown 表格 |
| office | `office/pitch-deck.pptx` | `markitdown office/pitch-deck.pptx -o office/pitch-deck.md` | ✅ 每張投影片 → `<!-- Slide number: n -->` |
| pdf | `pdf/report.pdf` | `markitdown pdf/report.pdf -o pdf/report.md` | ✅ 文字與表格（讀取順序依 pdfminer 版面） |
| web | `web/example.html` | `markitdown web/example.html -o web/example.md` | ✅ HTML → 標題/連結/表格 |
| web | `web/data.csv` | `markitdown web/data.csv -o web/data.md` | ✅ CSV → 表格 |
| web | `web/data.json` | `markitdown web/data.json -o web/data.md` | ✅ JSON → 等寬程式碼區塊 |
| media | `media/photo.jpg` | `EXIFTOOL_PATH=... markitdown media/photo.jpg -o media/photo.md` | ✅ EXIF 中繼資料（LLM 描述需 `llm_client`） |
| media | `media/tone.wav` | `markitdown media/tone.wav` | ❌ `UnknownValueError`（詳見 `media/tone-error.txt`） |
| media | `media/tone.wav`（無 audio-transcription 依賴） | 同上 | ✅ 優雅降級：只輸出 metadata（`media/tone.md`） |
| archive | `archive/archive.zip` | `markitdown archive/archive.zip -o archive/archive.md` | ✅ 逐一列出 ZIP 內檔案 |
| archive | `archive/book.epub` | `markitdown archive/book.epub -o archive/book.md` | ✅ 中繼資料 + spine 各章轉換 |

> 註：`web/data.csv` 與 `web/data.json` 的輸出檔名皆為 `data.md` 會衝突，
> 故 CSV 輸出存為 `data-csv.md`、JSON 輸出存為 `data-json.md`（見下方對應檔）。

## 實際輸出一覽

- `office/sample-report.md` — Word：標題保留為 heading、項目符號變 `*`、表格變 Markdown 表格
- `office/sales-data.md` — Excel：`## <工作表名>` + 表格（注意 `Total` 列合併與 `NaN`）
- `office/pitch-deck.md` — PowerPoint：`<!-- Slide number: N -->` 註解分頁 + 標題/清單/表格
- `pdf/report.md` — PDF：pdfminer 抽取的文字（中文需字型嵌入才可正確抽取）
- `web/example.md` — HTML：`#` 標題、連結列表、表格
- `web/data-csv.md` — CSV：兩欄式表格
- `web/data-json.md` — JSON：縮排成 `{}` 程式碼區塊
- `media/photo.md` — 圖片：`ImageSize` / `DateTimeOriginal`（EXIF）
- `media/tone.md` — 音訊（無轉錄依賴）：`NumChannels` / `SampleRate` / `BitsPerSample`
- `media/tone-error.txt` — 音訊（含轉錄依賴 + 非語音）：`UnknownValueError` 真實錯誤
- `archive/archive.md` — ZIP：`Content from the zip file ...` + 各檔段落
- `archive/book.md` — EPUB：`**Title:**` 等中繼資料 + 章節內容

## 重現方式

```bash
# 1. 產生樣本輸入檔
python scripts/generate-samples.py

# 2. 逐一轉換（以 docx 為例）
.venv/Scripts/markitdown worked/conversions/office/sample-report.docx \
  -o worked/conversions/office/sample-report.md
```

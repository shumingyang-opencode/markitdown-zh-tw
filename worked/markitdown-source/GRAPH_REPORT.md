# Graph Report - D:\workspace\OpenCode\ai-agent-tech\markitdown-zh-tw\raw\corpus  (2026-08-12)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 907 nodes · 1967 edges · 71 communities (65 shown, 6 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 181 edges (avg confidence: 0.62)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `efd7249f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13
- Community 14
- Community 15
- Community 16
- Community 17
- Community 18
- Community 19
- Community 20
- Community 21
- Community 22
- Community 23
- Community 24
- Community 25
- Community 26
- Community 27
- Community 28
- Community 29
- Community 30
- Community 31
- Community 32
- Community 33
- Community 34
- Community 35
- Community 36
- Community 37
- Community 38
- Community 39
- Community 40
- Community 41
- Community 42
- Community 43
- Community 44
- Community 45
- Community 46
- Community 47
- Community 48
- Community 49
- Community 50
- Community 51
- Community 52
- Community 53
- Community 54
- Community 55
- Community 56
- Community 57
- Community 60
- Community 68
- Community 69
- Community 70

## God Nodes (most connected - your core abstractions)
1. `StreamInfo` - 154 edges
2. `MarkItDown` - 70 edges
3. `DocumentConverterResult` - 67 edges
4. `DocumentConverter` - 50 edges
5. `MissingDependencyException` - 42 edges
6. `oMath2Latex` - 31 edges
7. `ContentUnderstandingFileType` - 29 edges
8. `HtmlConverter` - 27 edges
9. `LLMVisionOCRService` - 23 edges
10. `ContentUnderstandingConverter` - 23 edges

## Surprising Connections (you probably didn't know these)
- `test_pptx_svg_without_raster_fallback()` --calls--> `MarkItDown`  [INFERRED]
  packages/markitdown/tests/test_pptx_svg.py → packages/markitdown/src/markitdown/_markitdown.py
- `_convert()` --calls--> `StreamInfo`  [INFERRED]
  packages/markitdown-ocr/tests/test_docx_converter.py → packages/markitdown/src/markitdown/_stream_info.py
- `test_docx_no_ocr_service_no_tags()` --calls--> `StreamInfo`  [INFERRED]
  packages/markitdown-ocr/tests/test_docx_converter.py → packages/markitdown/src/markitdown/_stream_info.py
- `_convert()` --calls--> `StreamInfo`  [INFERRED]
  packages/markitdown-ocr/tests/test_pdf_converter.py → packages/markitdown/src/markitdown/_stream_info.py
- `test_pdf_no_ocr_service_no_tags()` --calls--> `StreamInfo`  [INFERRED]
  packages/markitdown-ocr/tests/test_pdf_converter.py → packages/markitdown/src/markitdown/_stream_info.py

## Import Cycles
- None detected.

## Communities (71 total, 6 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.10
Nodes (15): _make_converter(), Create a converter bypassing __init__ (no SDK deps needed)., Test modality-aware analyzer routing., Document-based analyzer should be used for PDF., Document-based analyzer should auto-route MP3 to prebuilt-audioSearch., Document-based analyzer should auto-route MP4 to prebuilt-videoSearch., Without analyzer_id, PDF should auto-route to prebuilt-documentSearch., Default image routing should still use prebuilt-documentSearch. (+7 more)

### Community 1 - "Community 1"
Cohesion: 0.10
Nodes (25): AnalyzeDocumentRequest, AnalyzeResult, AzureKeyCredential, DefaultAzureCredential, DocumentAnalysisFeature, DocumentIntelligenceClient, DocumentIntelligenceConverter, DocumentIntelligenceFileType (+17 more)

### Community 2 - "Community 2"
Cohesion: 0.09
Nodes (21): _generate_table_pdf(), _make_form_page(), _make_plain_page(), _mock_pdfplumber_open(), skipif, Verify all-plain-text PDFs fall back to pdfminer. When no page has form-style…, Even for plain-text PDFs, page.close() must be called on every page., In a mixed PDF, form pages get table extraction while plain pages don't.… (+13 more)

### Community 3 - "Community 3"
Cohesion: 0.12
Nodes (23): DocxConverterWithOCR, Any, BinaryIO, Extract images from DOCX and OCR them. Returns: Dict mapping image relationship…, Replace <img> tags with numbered placeholder tokens. Returns:…, Enhanced DOCX Converter with OCR support for embedded images. Maintains…, _convert(), MockOCRService (+15 more)

### Community 4 - "Community 4"
Cohesion: 0.10
Nodes (15): Exception, Resolve analyzer modality from cache or via get_analyzer() fallback. For known…, _resolve_analyzer_modality(), Any, BinaryIO, Get first non-empty value from metadata matching given keys., Recursively search for a key in nested dictionary/list structures., Retries the operation if it fails. (+7 more)

### Community 5 - "Community 5"
Cohesion: 0.26
Nodes (6): DocumentConverterResult, The result of converting a document to Markdown., llm_caption(), BinaryIO, _CustomMarkdownify, A custom version of markdownify's MarkdownConverter. Changes include: -…

### Community 6 - "Community 6"
Cohesion: 0.10
Nodes (14): PptxConverter, Any, BinaryIO, Return the image part referenced by an ``<asvg:svgBlip>``, if any. PowerPoint…, Return (blob, content_type, filename) for a picture shape. Handles SVG images…, Converts PPTX files to Markdown. Supports heading, tables and images with alt…, _FakePart, _FakeSvgPlaceholderShape (+6 more)

### Community 7 - "Community 7"
Cohesion: 0.12
Nodes (24): MarkItDown, Enable and register converters provided by plugins. Plugins are disabled by…, (In preview) An extremely simple text-based document reader, suitable for LLM…, skipif, Validate presence or absence of specific strings., Test operations performed on StreamInfo objects., Charts with multiple series and many categories must convert correctly.…, Large, deeply nested HTML should fall back to plain-text extraction instead of… (+16 more)

### Community 8 - "Community 8"
Cohesion: 0.27
Nodes (6): BinaryIO, transcribe_audio(), Any, BinaryIO, MissingDependencyException, Converters shipped with MarkItDown may depend on optional dependencies. This…

### Community 9 - "Community 9"
Cohesion: 0.11
Nodes (18): ContentUnderstandingConverter, _is_analyzer_compatible(), Any, BinaryIO, Return True when an analyzer modality can process a file modality., Converts files using Azure Content Understanding. Provides high-quality…, Return True if the file type is in the configured set., Convert the file using CU and return Markdown with YAML front matter. (+10 more)

### Community 10 - "Community 10"
Cohesion: 0.20
Nodes (12): Enhanced DOCX Converter with OCR support for embedded images. Extracts images…, LLMVisionOCRService, OCR Service Layer for MarkItDown Provides LLM Vision-based image text…, OCR service using LLM vision models (OpenAI-compatible)., PdfConverterWithOCR, Enhanced PDF Converter with OCR support for embedded images. Extracts images…, Enhanced PDF Converter with OCR support for embedded images. Maintains document…, Any (+4 more)

### Community 11 - "Community 11"
Cohesion: 0.14
Nodes (14): DocxConverter, Converts DOCX files to Markdown. Style information (e.g., headings) and tables…, EpubConverter, Converts EPUB files to Markdown. Style information (e.g., headings) and tables…, HtmlConverter, Any, BinaryIO, Anything with content type text/html (+6 more)

### Community 12 - "Community 12"
Cohesion: 0.20
Nodes (13): FailedConversionAttempt, FileConversionException, MarkItDownException, Any, object, Base exception class for MarkItDown., Thrown when no suitable converter was found for the given file., Represents a single attempt to convert a file. (+5 more)

### Community 13 - "Community 13"
Cohesion: 0.20
Nodes (20): _convert(), MockOCRService, Any, fixture, Unit tests for PdfConverterWithOCR. For each PDF test file: convert with a mock…, _ocr_full_pages emits *[Image OCR]...[End OCR]* for each page., svc(), test_pdf_complex_layout() (+12 more)

### Community 14 - "Community 14"
Cohesion: 0.11
Nodes (14): ContentUnderstandingFileType, _detect_file_type_from_mime(), str, Supported file types for Content Understanding conversion., Test that cu_file_types restricts which formats are accepted., Test CLI argument parsing for CU flags., --use-cu without --cu-endpoint should exit with error., --use-cu and --use-docintel cannot be used together. (+6 more)

### Community 15 - "Community 15"
Cohesion: 0.12
Nodes (14): DocumentConverter, Abstract superclass of all DocumentConverters., AudioConverter, Converts audio files to markdown via extraction of metadata (if `exiftool` is…, ImageConverter, Converts images to markdown via extraction of metadata (if `exiftool` is…, OutlookMsgConverter, Converts Outlook .msg files to markdown by extracting email metadata and… (+6 more)

### Community 16 - "Community 16"
Cohesion: 0.15
Nodes (19): parametrize, skipif, Test the conversion of an HTTP:// or HTTPS:// URI., Test the conversion of a file:// URI., Test the conversion of a data URI., Test API functionality when keep_data_uris is enabled, Test the ability to guess stream info., Test the conversion of a local file. (+11 more)

### Community 17 - "Community 17"
Cohesion: 0.18
Nodes (5): Any, Convert checkboxes to Markdown [x]/[ ] syntax., Same as usual, but be sure to start with a new line, Same as usual converter, but removes JavaScript links and escapes URIs., Same as usual converter, but removes data URIs

### Community 18 - "Community 18"
Cohesion: 0.06
Nodes (21): escape_latex(), get_char(), get_val(), load(), load_string(), oMath2Latex, Pr, object (+13 more)

### Community 19 - "Community 19"
Cohesion: 0.24
Nodes (8): _detect_file_type(), Detect a supported CU file type from extension or MIME type., Copy the StreamInfo object and update it with the given StreamInfo instance…, The StreamInfo class is used to store information about a file stream. All…, StreamInfo, Test extension and MIME based file type detection., End-to-end: conflicting StreamInfo routes by extension and sends a content_type…, TestDetectFileType

### Community 20 - "Community 20"
Cohesion: 0.20
Nodes (9): _load_plugins(), Any, BinaryIO, Args: - source: can be a path (str or Path), url, or a requests.response object…, Lazy load plugins, exiting early if already loaded., Given a base guess, attempt to guess or expand on the stream info using the…, Normalize a charset string to a canonical form., Path (+1 more)

### Community 21 - "Community 21"
Cohesion: 0.14
Nodes (16): fixture, parametrize, skipif, Test the conversion of a stream with no stream info., Test CLI functionality when keep_data_uris is enabled, Test that the CLI outputs to stdout correctly., Test that the CLI outputs to a file correctly., Test that the CLI reads from stdin correctly. (+8 more)

### Community 22 - "Community 22"
Cohesion: 0.13
Nodes (11): extract_markdown_tables(), Test that extracted tables have consistent structure across all PDF types., Test that borderless table PDF has pipe-separated structure., Test that multipage invoice PDF has pipe-separated format., Test that receipt PDF doesn't incorrectly extract tables from formatted text., Test that scanned PDF has empty extraction and no tables., Test that all PDF tables have rows with pipe-separated content. Note: With gap-…, Test that borderless table extraction preserves data integrity. (+3 more)

### Community 23 - "Community 23"
Cohesion: 0.13
Nodes (11): Test extraction of borderless tables from SPARSE inventory PDF. Expected output…, Validate presence or absence of specific strings., Test that borderless table content is not duplicated excessively., Test that tables appear in correct positions relative to text., Test extraction of receipt PDF (no tables, formatted text). Expected output…, Test extraction of multipage invoice PDF with form-style layout. Expected…, Test handling of scanned/image-based PDF (no text layer). Expected output:…, Test extraction of movie theater booking PDF with complex tables. Expected… (+3 more)

### Community 24 - "Community 24"
Cohesion: 0.18
Nodes (8): Element, Any, BinaryIO, Document, Parse the type of an Atom feed. Returns None if the feed type is not recognized…, Parse the type of an RSS feed. Returns None if the feed type is not recognized…, Parse the content of an RSS feed item, Get data from first child element with the given tag name. Returns None when no…

### Community 25 - "Community 25"
Cohesion: 0.17
Nodes (10): Any, BinaryIO, Called during construction of MarkItDown instances to register converters…, Converts an RTF file in the simplest possible way., register_converters(), RtfConverter, Tests the RTF converter directly., Tests that MarkItDown correctly loads the plugin. (+2 more)

### Community 27 - "Community 27"
Cohesion: 0.24
Nodes (8): Any, BinaryIO, Enhanced XLSX Converter with OCR support for embedded images. Extracts images…, Convert XLSX with image OCR., Extract and OCR images from an Excel sheet. Args: sheet: openpyxl worksheet…, Convert column number to Excel column letter (0-indexed)., Standard conversion without OCR., XlsxConverterWithOCR

### Community 28 - "Community 28"
Cohesion: 0.18
Nodes (8): _content_type_for(), Resolve the content type to send to the CU API. Uses the resolved ``file_type``…, parametrize, Test accepts() for MIME type matching., When extension and mimetype disagree, file_type wins., Test accepts() for supported and unsupported file extensions., TestAcceptsExtension, TestAcceptsMime

### Community 29 - "Community 29"
Cohesion: 0.22
Nodes (10): AzureKeyCredential, _canonical_mime_type(), _clean_mime_type(), ContentUnderstandingClient, DefaultAzureCredential, Enum, Azure Content Understanding converter for MarkItDown. Converts files using…, Initialize the Content Understanding converter. Args: endpoint: CU resource… (+2 more)

### Community 30 - "Community 30"
Cohesion: 0.19
Nodes (8): Any, BinaryIO, exiftool_metadata(), _parse_version(), Any, BinaryIO, Any, BinaryIO

### Community 31 - "Community 31"
Cohesion: 0.14
Nodes (8): Test that PDF extraction produces expected complete outputs., Test complete output for movie theater booking PDF., Test complete output for SPARSE borderless table PDF., Test complete output for REPAIR multipage invoice PDF., Test complete output for RECEIPT retail purchase PDF., Test complete output for academic paper PDF., Test complete output for medical report scan PDF (empty, no text layer)., TestPdfFullOutputComparison

### Community 32 - "Community 32"
Cohesion: 0.17
Nodes (14): _convert_omath_to_latex(), _get_omath_tag_replacement(), pre_process_docx(), _pre_process_math(), BinaryIO, Pre-processes the math content in a DOCX -> XML file by converting OMML (Office…, Pre-processes a DOCX file with provided steps. The process works by unzipping…, Converts an OMML (Office Math Markup Language) tag to LaTeX format. Args: tag… (+6 more)

### Community 33 - "Community 33"
Cohesion: 0.17
Nodes (8): OCRResult, Any, BinaryIO, Result from OCR extraction., Initialize LLM Vision OCR service. Args: client: OpenAI-compatible client…, Extract text using LLM vision., Any, Any

### Community 34 - "Community 34"
Cohesion: 0.35
Nodes (11): _convert(), MockOCRService, fixture, Unit tests for XlsxConverterWithOCR. For each XLSX test file: convert with a…, svc(), test_xlsx_complex_layout(), test_xlsx_image_end(), test_xlsx_image_middle() (+3 more)

### Community 35 - "Community 35"
Cohesion: 0.17
Nodes (7): Test that partial numberings merge correctly even with empty lines between.…, Test that all partial numberings in a document are properly merged., Test handling of MasterFormat-style partial numbering (.1, .2, etc.)., Test that the partial numbering regex pattern correctly matches., Test that MasterFormat partial numbering stays with associated text.…, Test that MasterFormat document content is fully preserved., TestMasterFormatPartialNumbering

### Community 36 - "Community 36"
Cohesion: 0.40
Nodes (10): _convert(), MockOCRService, fixture, Unit tests for PptxConverterWithOCR. For each PPTX test file: convert with a…, svc(), test_pptx_complex_layout(), test_pptx_image_end(), test_pptx_image_middle() (+2 more)

### Community 37 - "Community 37"
Cohesion: 0.47
Nodes (3): Any, BinaryIO, Helper to safely extract and decode stream data from the MSG file.

### Community 38 - "Community 38"
Cohesion: 0.24
Nodes (8): _extract_form_content_from_words(), _extract_tables_from_words(), _merge_partial_numbering_lines(), Any, BinaryIO, Extract form-style content from a PDF page by analyzing word positions. This…, Post-process extracted text to merge MasterFormat-style partial numbering with…, Extract tables from a PDF page by analyzing word positions. This handles…

### Community 39 - "Community 39"
Cohesion: 0.24
Nodes (7): BytesIO, _extract_images_from_page(), Any, BinaryIO, Extract images from a PDF page by rendering page regions. Returns: List of…, Extract images from a PDF page using pdfplumber. Args: pdf_bytes: PDF file as…, Fallback for scanned PDFs: Convert entire pages to images and OCR them. Used…

### Community 40 - "Community 40"
Cohesion: 0.28
Nodes (8): check_plugins_enabled(), convert_to_markdown(), create_starlette_app(), main(), Convert a resource described by an http:, https:, file: or data: URI to markdown, Server, Starlette, tool

### Community 41 - "Community 41"
Cohesion: 0.31
Nodes (5): Any, BinaryIO, Document, Convenience function to extract a single occurrence of a tag (e.g., title)., Helper function to extract all occurrences of a tag (e.g., multiple authors).

### Community 42 - "Community 42"
Cohesion: 0.20
Nodes (5): PptxConverterWithOCR, Any, BinaryIO, Enhanced PPTX Converter with OCR fallback., test_pptx_no_ocr_service_no_tags()

### Community 43 - "Community 43"
Cohesion: 0.36
Nodes (4): _get_modality(), Get the modality category for a file type., Test file type → modality mapping., TestGetModality

### Community 44 - "Community 44"
Cohesion: 0.38
Nodes (5): BingSerpConverter, Any, BinaryIO, Handle Bing results pages (only the organic search results). NOTE: It is better…, Make sure we're dealing with HTML content *from* Bing.

### Community 45 - "Community 45"
Cohesion: 0.38
Nodes (5): IpynbConverter, Any, BinaryIO, Converts Jupyter Notebook (.ipynb) files to Markdown., Helper function that converts notebook JSON content to Markdown.

### Community 46 - "Community 46"
Cohesion: 0.38
Nodes (5): Any, BinaryIO, Handle Wikipedia pages separately, focusing only on the main document content., Make sure we're dealing with HTML content *from* Wikipedia., WikipediaConverter

### Community 47 - "Community 47"
Cohesion: 0.47
Nodes (4): _exit_with_error(), _handle_output(), main(), Handle output to stdout or file

### Community 48 - "Community 48"
Cohesion: 0.40
Nodes (4): Any, BinaryIO, Return a quick determination on if the converter should attempt converting the…, Convert a document to Markdown text. Parameters: - file_stream: The file-like…

### Community 49 - "Community 49"
Cohesion: 0.33
Nodes (5): file_uri_to_path(), parse_data_uri(), Convert a file URI to a local file path, test_data_uris(), test_file_uris()

### Community 51 - "Community 51"
Cohesion: 0.33
Nodes (4): Test that form-style PDF columns are separated with pipes., Test that extracted tables have proper markdown formatting., Test that form-style PDFs have pipe-separated format., TestPdfTableMarkdownFormat

### Community 52 - "Community 52"
Cohesion: 0.40
Nodes (4): Validate that a markdown table exists with expected headers and data., Validate that a table has consistent structure: - All rows have the same number…, validate_markdown_table(), validate_table_structure()

### Community 53 - "Community 53"
Cohesion: 0.38
Nodes (4): CsvConverter, Any, BinaryIO, Converts CSV files to Markdown tables.

### Community 54 - "Community 54"
Cohesion: 0.47
Nodes (4): PlainTextConverter, Any, BinaryIO, Anything with content type text/plain

### Community 55 - "Community 55"
Cohesion: 0.38
Nodes (4): Any, BinaryIO, Converts ZIP files to markdown by extracting and converting all contained…, ZipConverter

### Community 56 - "Community 56"
Cohesion: 0.50
Nodes (4): markitdown, markitdown-mcp, markitdown-ocr, markitdown-sample-plugin

### Community 68 - "Community 68"
Cohesion: 0.33
Nodes (4): PdfConverter, Converts PDFs to Markdown. Supports extracting tables into aligned Markdown…, Convert a 2D list (rows/columns) into a nicely aligned Markdown table. Args:…, _to_markdown_table()

## Knowledge Gaps
- **5 isolated node(s):** `AnalyzeResult`, `DocumentAnalysisFeature`, `markitdown-mcp`, `markitdown-ocr`, `markitdown-sample-plugin`
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `StreamInfo` connect `Community 19` to `Community 0`, `Community 1`, `Community 2`, `Community 3`, `Community 4`, `Community 5`, `Community 6`, `Community 7`, `Community 8`, `Community 9`, `Community 11`, `Community 12`, `Community 13`, `Community 14`, `Community 15`, `Community 16`, `Community 20`, `Community 24`, `Community 25`, `Community 26`, `Community 27`, `Community 28`, `Community 29`, `Community 30`, `Community 32`, `Community 33`, `Community 34`, `Community 36`, `Community 37`, `Community 38`, `Community 39`, `Community 41`, `Community 42`, `Community 43`, `Community 44`, `Community 45`, `Community 46`, `Community 47`, `Community 48`, `Community 53`, `Community 54`, `Community 55`, `Community 68`?**
  _High betweenness centrality (0.398) - this node is a cross-community bridge._
- **Why does `MarkItDown` connect `Community 7` to `Community 2`, `Community 35`, `Community 5`, `Community 6`, `Community 40`, `Community 10`, `Community 11`, `Community 12`, `Community 47`, `Community 15`, `Community 16`, `Community 50`, `Community 19`, `Community 20`, `Community 25`, `Community 60`?**
  _High betweenness centrality (0.167) - this node is a cross-community bridge._
- **Why does `DocumentConverterResult` connect `Community 5` to `Community 1`, `Community 3`, `Community 4`, `Community 6`, `Community 7`, `Community 8`, `Community 9`, `Community 11`, `Community 12`, `Community 19`, `Community 20`, `Community 24`, `Community 25`, `Community 27`, `Community 29`, `Community 30`, `Community 32`, `Community 37`, `Community 38`, `Community 39`, `Community 41`, `Community 42`, `Community 44`, `Community 45`, `Community 46`, `Community 47`, `Community 48`, `Community 53`, `Community 54`, `Community 55`, `Community 57`, `Community 68`, `Community 69`, `Community 70`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Are the 37 inferred relationships involving `StreamInfo` (e.g. with `_convert()` and `test_docx_no_ocr_service_no_tags()`) actually correct?**
  _`StreamInfo` has 37 INFERRED edges - model-reasoned connections that need verification._
- **Are the 47 inferred relationships involving `MarkItDown` (e.g. with `convert_to_markdown()` and `test_markitdown()`) actually correct?**
  _`MarkItDown` has 47 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `DocumentConverterResult` (e.g. with `StreamInfo` and `ConverterRegistration`) actually correct?**
  _`DocumentConverterResult` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `DocumentConverter` (e.g. with `StreamInfo` and `ConverterRegistration`) actually correct?**
  _`DocumentConverter` has 3 INFERRED edges - model-reasoned connections that need verification._
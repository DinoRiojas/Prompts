---
name: portfolio-analysis-reporter
description: Construct a Google Notebook in NotebookLM from source URLs (spreadsheets, research pages, market data) in Google Drive, synthesize portfolio and asset analytics, and compile an institutional-grade multi-page PDF report using ReportLab and Matplotlib. Use when asked to generate portfolio analysis reports, create financial notebooks from data sources, or build wealth review PDFs.
allowed-tools: drive notebooklm vm_shell
---
# Portfolio Analysis Reporter

A skill for creating NotebookLM knowledge bases from portfolio data sources and generating institutional-grade, multi-page financial review PDF reports using ReportLab and Matplotlib.

## When to Use

- When the user requests a comprehensive portfolio analysis or wealth review report.
- When creating a new Google Notebook in NotebookLM using data files or URLs from Google Drive.
- When compiling multi-page investment review PDFs with charts, risk analytics, asset allocations, and rebalancing recommendations.
- When automating ReportLab document compilation with custom running headers, footers, and two-pass page numbering.

## Workflow Steps

### Step 1: Ingest Data Sources and Extract URLs

1. Search Google Drive using `drive:search_files` to locate the portfolio data file (e.g. text file or spreadsheet containing asset holdings and source URLs).
2. Read the source file content using `drive:read_file_content` to extract all target URLs (Google Sheets, Morningstar, fund quotes, or benchmark endpoints) and report instructions.
3. Identify the parent folder ID on Google Drive to ensure final deliverables are saved to the correct directory.

### Step 2: Create and Populate Google Notebook

1. Call `notebooklm:create_notebook` to create a dedicated research notebook with an informative display name and business/finance category.
2. Ingest the data source URLs by calling `notebooklm:create_source` for each extracted URL (both Google Sheets and web endpoints).
3. Retrieve relevant analytical chunks using `notebooklm:retrieve_relevant_chunks` for fund risk metrics (Alpha, Beta, Sharpe, Standard Deviation), performance series, sector breakdowns, and top holdings.

### Step 3: Generate Visual Charts with Matplotlib

1. Write a Python script using Matplotlib to produce high-resolution chart images (300 DPI) saved locally on the VM.
2. Ensure consistent institutional brand palette (e.g. Navy `#003B70`, Accent Blue `#007BC8`, Slate `#5B6770`, Light Gray `#F4F6F8`, Dark Charcoal `#222222`).
3. Typical charts to generate:
   - Asset allocation donut or pie chart (Equities, Fixed Income, Cash).
   - Account balance distribution bar chart.
   - Multi-period trailing returns comparison bar chart.
   - 10-year cumulative growth of $10,000 trend lines.
   - Risk versus return scatter plot with efficient frontier positioning.
   - Macroeconomic scenario stress-testing impact waterfall/bars.
   - GICS sector breakdown horizontal bar chart against benchmark.

### Step 4: Programmatically Build Multi-Page PDF with ReportLab

1. Write a standalone Python script using ReportLab Platypus (`SimpleDocTemplate`, `Paragraph`, `Table`, `TableStyle`, `Image`, `Spacer`, `PageBreak`, `KeepTogether`).
2. Implement a two-pass `NumberedCanvas` class to dynamically compute and render running headers and footers with "Page X of Y" pagination across all pages (suppressing header/footer on the cover page).
3. Structure the document across core sections:
   - Cover Page and Executive Overview (metadata grid, macroeconomic context, fiduciary summary).
   - Asset Allocation and Account Architecture (target vs. actual weighting, drift analysis, Morningstar Style Box).
   - Performance Benchmarking and Historical Returns (multi-period trailing returns, calendar year history, benchmark attribution).
   - Risk, Beta, and Volatility Analytics (Standard Deviation, Beta, Alpha, Sharpe, Sortino, VaR, stress-test matrix).
   - Itemized Holdings and Sector Allocations (equities sleeve, fixed income/cash sleeve, look-through top holdings, account breakdown).
   - Strategic Wealth Advisory, Rebalancing, and Disclosures (phased rebalancing roadmap, asset location, tax-loss harvesting, liquidity tiers, regulatory disclaimers).
4. Wrap all table cell text inside `Paragraph` flowables and explicitly specify column widths to prevent clipping.

### Step 5: Validate and Upload Final Deliverable

1. Execute the Python build script in `vm_shell` to generate the PDF.
2. Verify page count and document layout using `pypdf` to ensure no overflowing elements or orphaned blank pages.
3. Upload the finalized PDF to Google Drive using `drive:create_file` (with `file://` URI for Base64 auto-encoding) and move to the target folder via `drive:update_file`.
4. Provide the user with clickable links to the created Google Notebook, data sources, and the generated PDF report on Google Drive.

## Gotchas

- When using `drive:create_file`, pass the `file:///path/to/file.pdf` URI in `base64_content` and leave `text_content` as an empty string.
- In ReportLab, always specify explicit `colWidths` on `Table` objects and wrap text strings in `Paragraph` flowables to enable automatic word wrapping.
- When creating two-pass canvas numbering, ensure `_saved_page_states` correctly preserves page states across multi-page documents.
- Set Matplotlib to non-interactive mode (`matplotlib.use('Agg')`) prior to importing `pyplot` to avoid GUI backend errors on headless VMs.

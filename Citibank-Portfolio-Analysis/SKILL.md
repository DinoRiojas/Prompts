---
name: citibank-portfolio-analysis
description: Ingest portfolio source documents and URLs from Google Drive, synthesize multi-account asset allocations and Morningstar fund metrics via NotebookLM, generate high-resolution institutional charts with Matplotlib, and compile a comprehensive multi-page fiduciary review PDF report using ReportLab. Use when asked to generate Citibank Portfolio Analysis reports, build wealth review PDFs for High-Net-Worth clients, or analyze multi-account Vanguard ETF portfolios.
allowed-tools: drive notebooklm vm_shell
---
# Citibank Portfolio Analysis

A skill for ingesting multi-account portfolio source documents from Google Drive into NotebookLM, synthesizing fund performance and risk analytics, generating high-resolution Matplotlib charts, and compiling institutional-grade, multi-page client review PDF reports using ReportLab Platypus.

## When to Use

- When asked to create or update a Citibank Portfolio Analysis report.

- When analyzing multi-account investment portfolios across taxable brokerage, Traditional IRA, Roth IRA, and liquid cash reserves.

- When synthesizing asset allocations and factor tilts for core index funds (such as Vanguard VOO, VTIP, BND, VYM, VUG, VTV, VB, VGT, VHT, VGIT).

- When querying fund performance, risk metrics (Alpha, Beta, Sharpe, Standard Deviation), and sector exposures from Morningstar URLs via NotebookLM.

- When generating publication-grade financial charts (asset allocation donuts, account distribution bars, trailing returns, 10-year growth of $10,000, risk-return scatter plots, and stress-testing waterfalls).

- When compiling a 15 to 25 page client PDF report using ReportLab with two-pass running headers, footers, and "Page X of Y" pagination.

## Workflow Steps

### Step 1: Ingest Data Sources and Extract URLs

1. Search Google Drive using `drive:search_files` to locate the portfolio source document (e.g., text files containing account balances, holdings, and fund research URLs).

2. Read the source file with `drive:read_file_content` to extract target data endpoints (Google Sheets holdings, Morningstar performance/risk/portfolio/quote URLs) and execution instructions.

3. Identify the parent folder ID on Google Drive to ensure final PDF deliverables are uploaded to the correct client directory.

### Step 2: Create and Populate Google Notebook in NotebookLM

1. Check existing notebooks with `notebooklm:list_notebooks` or create a new dedicated research notebook using `notebooklm:create_notebook` with category `NOTEBOOK_CATEGORY_BUSINESS`.

2. Add all extracted data source URLs to the notebook using `notebooklm:create_source` for each endpoint.

3. Retrieve relevant analytical chunks using `notebooklm:retrieve_relevant_chunks` for fund risk statistics (Alpha, Beta, Sharpe Ratio, Standard Deviation, Sortino Ratio), multi-period trailing returns, look-through top holdings, and GICS sector allocations.

### Step 3: Generate Visual Charts with Matplotlib

1. Write a Python script using Matplotlib to produce high-resolution chart images (300 DPI) saved locally on the VM.

2. Enforce the institutional Citibank brand palette: Primary Navy (`#003B70`), Accent Citi Blue (`#007BC8`), Soft Slate (`#5B6770`), Light Background (`#F4F6F8`), and Dark Charcoal (`#222222`).

3. Generate the core visual charts:
   - Asset allocation donut chart (Equities, Fixed Income, Cash).
   - Custodial account distribution bar chart.
   - Multi-period trailing returns performance comparison bar chart.
   - 10-year cumulative growth of $10,000 hypothetical investment trend lines.
   - Risk versus return scatter plot with Capital Allocation Line / Efficient Frontier curve.
   - Macroeconomic scenario stress-testing impact horizontal bar chart.
   - Look-through GICS sector exposure breakdown against the S&P 500 benchmark.

### Step 4: Programmatically Build Multi-Page PDF with ReportLab

1. Write a standalone Python script using ReportLab Platypus (`SimpleDocTemplate`, `Paragraph`, `Table`, `TableStyle`, `Image`, `Spacer`, `PageBreak`, `KeepTogether`, `HRFlowable`).

2. Implement a custom two-pass `NumberedCanvas` class to dynamically compute total page count and render running headers and footers with "Page X of Y" page numbers on all pages (suppressing on the cover page).

3. Structure the 15 to 25 page document across six core sections:
   - Cover Page and Executive Overview: Formal title, client metadata, total valuation, macroeconomic regime review, and key fiduciary findings.
   - Asset Allocation and Portfolio Structure: Macro weights, target vs. actual drift analysis, account architecture, and Morningstar Style Box mapping.
   - Performance Benchmarking and Historical Returns: Trailing return schedules, multi-period visual comparisons, 10-year growth trajectories, calendar year history, and Brinson-Fachler attribution.
   - Risk, Beta and Volatility Analytics: Risk matrix (Std Dev, Beta, Alpha, Sharpe, R-squared), risk-return CAL positioning, Value at Risk (VaR 95%/99%), and 5-scenario stress tests.
   - Itemized Holdings and Sector Allocations: Granular tables for Core Equities, Satellite Factor Tilts, Fixed Income/Cash, look-through Top 10 single-stock exposures, and global revenue exposure.
   - Strategic Wealth Advisory, Rebalancing and Disclosures: Actionable rebalancing roadmap, asset location guidelines, tax-loss harvesting rules, 3-tier liquidity architecture, and regulatory/fiduciary disclosures.

4. Wrap all table cell contents inside `Paragraph` flowables and specify explicit column widths (`colWidths`) to prevent text clipping and page overflow.

### Step 5: Validate and Upload Final Deliverable

1. Execute the Python build script in `vm_shell` to generate the PDF deliverable.

2. Verify document page count and layout using `pypdf` to ensure exact page mapping without orphaned overflow pages.

3. Upload the finalized PDF to Google Drive using `drive:create_file` with `base64_content="file:///path/to/file.pdf"`, `mime_type="application/pdf"`, and `text_content=""`. Move to the client folder with `drive:update_file`.

4. Provide the user with clickable links to the created PDF report, Google Notebook knowledge base, and underlying data sources.

## Gotchas

- Always wrap table cell contents in `Paragraph` flowables and set explicit `colWidths` on all `Table` objects in ReportLab to avoid text clipping.

- When creating two-pass canvas numbering, use `_saved_page_states` to preserve page states across multi-page documents.

- Set Matplotlib to non-interactive mode (`matplotlib.use('Agg')`) prior to importing `pyplot` to prevent GUI backend errors in headless environments.

- When uploading binary PDFs via `drive:create_file`, pass the `file:///path/to/file.pdf` URI in `base64_content` and leave `text_content` as an empty string.

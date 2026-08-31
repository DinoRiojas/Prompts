---
name: citibank-portfolio-analysis-report-generator
description: |
  Generates an institutional-grade, fiduciary-level client review PDF report ("Citibank Portfolio Analysis") for High-Net-Worth (HNW) private wealth portfolios. The skill parses portfolio holdings, asset allocations, performance metrics, and Morningstar benchmark/risk data to programmatically build an extensive multi-page ReportLab PDF report styled in institutional Citibank brand colors.
  
  
  
---

## Task & Workflow Definition

1. **Data Ingestion & Synthesis:**
   - Ingest portfolio holdings, market valuations, share counts, expense ratios, and asset classes.
   - Aggregate Morningstar quote, portfolio, performance, and risk metrics across holdings (e.g., `VOO`, `VTIP`, `BND`, `VTV`, `VYM`, `VUG`, `VB`, `VGT`, `VHT`, `VGIT`).
   - Identify and document any missing or ambiguous metrics explicitly rather than extrapolating or inventing figures.

2. **Analytics & Financial Modeling:**
   - **Allocation Analysis:** Group assets into broad classes (Equities: Large-Cap Blend, Growth, Value, Small-Cap, Sector; Fixed Income: Short/Intermediate Treasury, TIPS, Aggregate Bond; Cash Equivalents). Compute actual vs. target allocation weights.
   - **Performance Benchmarking:** Compute multi-period annualized returns (YTD, 1-Year, 3-Year, 5-Year) against blended benchmarks.
   - **Risk & Volatility Analytics:** Calculate weighted Portfolio Standard Deviation, Sharpe Ratio, Sortino Ratio, Beta, Value at Risk (VaR 95%), and evaluate portfolio behavior under macroeconomic stress-testing scenarios.
   - **Strategic Wealth Advisory:** Formulate rebalancing pathways, tax efficiency observations, and wealth preservation guidance.

3. **Programmatic Document Generation:**
   - Construct and execute a standalone, production-ready Python script utilizing `reportlab.platypus` (`SimpleDocTemplate`, `Paragraph`, `Table`, `TableStyle`, `KeepTogether`, `PageBreak`, `Spacer`) and `matplotlib`.
   - Apply a dynamic two-pass `NumberedCanvas` to calculate exact total page counts and render running headers/footers (`"Page X of Y"`).
   - Render vector/high-resolution charts (Asset Allocation Donut, Performance Comparison Bar Chart, Risk vs Return Scatter, Sector Allocation Horizontal Bar).
   - Enforce rigorous typography, paragraph wrapping within table cells, exact column widths, and strict page-budget budgeting across all 6 sections (15–25 page institutional structure).

---

## Reference Resources & Ticker Directory

### Primary Data Sources
- **Portfolio Ledger / Holdings Spreadsheet:**
  `https://docs.google.com/spreadsheets/d/1x4rvOThgFhgTdpuslqsYfhSoAibVDM3BZOUHlp2RW1s/edit?gid=861982464#gid=861982464`
- **Morningstar Fund Analytics & Risk Endpoints:**
  - `VOO` (Vanguard S&P 500 ETF): `xmex/voo` (`portfolio`, `quote`, `performance`, `risk`)
  - `VTIP` (Vanguard Short-Term Inflation-Protected Securities ETF): `xmex/vtip` (`portfolio`, `quote`, `performance`, `risk`)
  - `BND` (Vanguard Total Bond Market ETF): `xnas/bnd` (`portfolio`, `quote`, `performance`, `risk`)
  - `VTV` (Vanguard Value ETF): `xmex/vtv` (`portfolio`, `quote`, `performance`, `risk`)
  - `VYM` (Vanguard High Dividend Yield ETF): `xmex/vym` (`portfolio`, `quote`, `performance`, `risk`)
  - `VUG` (Vanguard Growth ETF): `xmex/vug` (`portfolio`, `quote`, `performance`, `risk`)
  - `VB` (Vanguard Small-Cap ETF): `xmex/vb` (`portfolio`, `quote`, `performance`, `risk`)
  - `VGT` (Vanguard Information Technology ETF): `xmex/vgt` (`portfolio`, `quote`, `performance`, `risk`)
  - `VHT` (Vanguard Health Care ETF): `xmex/vht` (`portfolio`, `quote`, `performance`, `risk`)
  - `VGIT` (Vanguard Intermediate-Term Treasury ETF): `xnas/vgit` (`portfolio`, `quote`, `performance`, `risk`)

---

## Operational Prompt & System Execution Rules

### Role & Persona
- **Role:** Principal Wealth Management Strategist & Python Reporting Architect.
- **Tone:** Strictly neutral, institutional, non-promotional, precise, and fiduciary-grade.

### Document Architecture & Section Breakdown (15–25 Pages)
1. **Section 1: Cover Page & Executive Overview (Pages 1–2)**
   - Formal title: `"Citibank Portfolio Analysis"`.
   - Portfolio metadata: Client Name, Account ID, Valuation Date, Reporting Currency, Total Valuation.
   - Executive commentary, macroeconomic backdrop, and core strategic positioning summary.
2. **Section 2: Asset Allocation & Portfolio Structure (Pages 3–6)**
   - Allocation hierarchy: Equities (Large Blend, Value, Growth, Small-Cap, Sector), Fixed Income (TIPS, Intermediate Treasuries, Broad Bonds), Cash.
   - Matplotlib donut charts illustrating actual vs. target weights and asset class breakdowns.
3. **Section 3: Performance Benchmarking & Historical Returns (Pages 7–11)**
   - Multi-period performance breakdown (YTD, 1-Year, 3-Year, 5-Year).
   - Comparison against blended benchmark index; comparative Matplotlib bar and trend charts.
4. **Section 4: Risk, Beta & Volatility Analytics (Pages 12–15)**
   - Risk matrix: Standard Deviation, Sharpe Ratio, Sortino Ratio, Beta, Max Drawdown, VaR (95%).
   - Stress-testing scenario matrix (Equity Shock -20%, Interest Rate Hike +150 bps, Stagflationary Shock).
5. **Section 5: Itemized Holdings & Sector Allocations (Pages 16–21)**
   - Granular multi-page holdings tables: Ticker, Description, Asset Class, Shares, Price, Market Value, Weight (%), Expense Ratio.
   - Sector diversification breakdown tables and geographic exposure analysis.
6. **Section 6: Strategic Wealth Advisory, Rebalancing & Disclosures (Pages 22–25)**
   - Fiduciary advisory roadmap: rebalancing action plan, tax efficiency / tax-loss harvesting observations, cash flow planning.
   - Regulatory disclosures, methodology definitions, fiduciary notices, and standard disclaimers.

### Styling & Brand Palette Guidelines
- **Primary Navy:** `#003B70`
- **Accent Citi Blue:** `#007BC8`
- **Soft Slate:** `#5B6770`
- **Light Background:** `#F4F6F8`
- **Dark Charcoal:** `#222222`
- **Accent Light Blue:** `#E6F2F8`
- **Borders / Dividers:** `#D0D7DE`

### Technical Python / ReportLab Constraints
- **Self-Contained Code:** Must contain complete imports, style setups, flowable constructions, and document compilation without placeholders, elisions, or truncation.
- **Canvas Implementation:** Subclass `canvas.Canvas` to collect total page counts during pass 1 and draw running headers/footers (`"Page X of Y"`, document title, confidential notice) on pass 2.
- **Flowable Integrity:** Every table cell containing string data must be wrapped in a `Paragraph` flowable with explicit column widths (`colWidths`) to eliminate overflow or text clipping.
- **Chart Isolation:** Matplotlib charts must be saved to buffer / temporary image files (`io.BytesIO` or `.png`) and cleanly embedded as `reportlab.platypus.Image` flowables.

---
name: portfolio-report-generator
description: Generate institutional-grade multi-page wealth management portfolio reports and financial analysis PDFs from portfolio spreadsheets, holdings data, and market research using ReportLab and Matplotlib. Use when the user asks to create, compile, or generate comprehensive portfolio analysis reports, fiduciary wealth reviews, asset allocation reviews, or multi-page client financial review PDFs.
allowed-tools: vm_shell drive google
---

# Portfolio Report Generator

## Summary

Generate comprehensive, institutional-grade, multi-page (15 to 25 pages) portfolio review and wealth management PDF reports from client holdings spreadsheets, market data, and investment benchmarks using Python (ReportLab and Matplotlib).

## When to Use

Use this skill when:

- The user requests a comprehensive, detailed, or institutional-grade portfolio analysis report or fiduciary wealth review PDF.
- The user provides portfolio spreadsheets or holdings data (e.g. Google Sheets, CSV, Excel) and asks for a multi-page client-ready PDF document.
- The task requires deep financial analytics: asset allocation breakdowns, multi-period performance benchmarking, Modern Portfolio Theory (MPT) risk statistics, look-through sector/company exposures, stress testing, tax location strategy, and rebalancing roadmaps.

## Step-by-Step Workflow

### 1. Portfolio Data Ingestion and Normalization

- Extract account and holdings data from the source document (e.g. Google Sheets via Drive tools or context services).
- Parse all accounts (taxable brokerage, traditional IRA, Roth IRA, cash/savings), recording ticker symbols, asset descriptions, share counts, market prices, cost bases, market values, and account-level/portfolio-level weights.
- Reconcile totals across accounts and cash equivalents (e.g. money market funds, bank deposit programs) to establish the exact consolidated portfolio valuation.
- Gather benchmark data, dividend yields, expense ratios, durations, and credit ratings for all held securities via search tools.

### 2. Quantitative Analytics and Benchmark Modeling

- Calculate volume-weighted portfolio metrics:
  - Capital-weighted expense ratio in basis points.
  - 12-month trailing and forward dividend/interest cash flow and portfolio yield.
  - Volume-weighted portfolio beta against primary equity benchmarks (e.g. S&P 500).
- Construct primary and secondary blended benchmarks matching the asset allocation (e.g. 85% S&P 500 / 10% Bloomberg US Aggregate / 5% Cash).
- Compute multi-period returns (YTD, 1-Year, 3-Year annualized, 5-Year annualized, cumulative).
- Derive Modern Portfolio Theory (MPT) risk metrics:
  - Annualized Standard Deviation (volatility).
  - Sharpe Ratio and Sortino Ratio.
  - Jensen's Alpha and Treynor Ratio.
  - Value at Risk (VaR 95%, 1-Month) and Conditional VaR (Expected Shortfall).
- Model stress-testing scenarios (e.g. 20% equity crash, +100 bps rate shock, stagflation, tech multiple compression).
- Aggregate look-through exposures across underlying funds: top 25 individual company holdings and GICS sector weightings.

### 3. Matplotlib Visualizations

Generate publication-quality charts (saved as high-DPI PNGs) using a consistent institutional brand palette:

- **Asset Allocation and Account Breakdown:** Donut chart of broad asset classes and horizontal bar chart of account values.
- **Fixed Income and Duration Profile:** Sleeve composition donut and duration vs. yield comparisons.
- **Cumulative Growth Trajectory:** Multi-year line chart showing hypothetical growth of capital ($1,000,000 baseline) across portfolio vs. benchmarks.
- **Risk-Return Efficiency Frontier:** Scatter plot showing volatility vs. return along the Capital Allocation Line (CAL).
- **Look-Through Sector Exposures:** Bar chart comparing portfolio look-through sectors against the benchmark.
- **Macroeconomic Stress Testing:** Horizontal bar chart illustrating dollar and percentage drawdown impacts under crisis scenarios.
- **Rebalancing Variance:** Bar chart comparing current asset weights vs. strategic target policies.

### 4. ReportLab Architecture and Canvas Mechanics

Construct the document using ReportLab Platypus:

- **Page Layout:** Standard Letter size with 0.5 to 0.75-inch margins (e.g. 36 pt left/right, 45 pt top/bottom).
- **Two-Pass NumberedCanvas:** Implement a custom canvas that records page states and draws running headers, running footers, divider lines, and dynamic page numbering ("Page X of Y") on the second pass.
- **Table Cell Formatting:** Wrap every table cell in a `Paragraph` flowable with explicit styles to prevent text clipping. Set fixed column widths that sum to the exact printable width.
- **Section Pacing:** Place explicit `PageBreak()` calls at the end of each logical page block. Keep individual page content within printable height bounds (~700 pt) to avoid unintended page overflow.

### 5. Multi-Section Report Structure

Structure the report across 6 core thematic modules:

1. **Cover Page & Executive Overview (Pages 1-2):**
   - Brand title, metadata table (client name, valuation date, advisory group, total valuation).
   - 8-card executive KPI summary (Total Wealth, Equity %, Fixed Income %, Cash %, Expense Ratio, Yield, Beta, Sharpe).
   - Executive commentary, macroeconomic backdrop, and multi-account summary table.
2. **Asset Allocation & Capital Structure (Pages 3-6):**
   - Consolidated asset class table with strategic targets and variance deltas.
   - Asset allocation and account distribution charts.
   - Morningstar 9-box equity style matrix and core-satellite breakdown.
   - Fixed income duration, yield, and credit quality schedules.
   - Multi-account tax location analysis (taxable vs. tax-deferred vs. tax-free).
3. **Performance Benchmarking & Historical Returns (Pages 7-11):**
   - Multi-period annualized return table vs. blended and peer benchmarks.
   - Visual cumulative capital trajectory chart (Growth of $1,000,000).
   - Component-level fund return breakdown and Brinson-Fachler attribution.
   - Rolling returns, market regime resilience, and upside/downside capture ratios.
   - Itemized 12-month dividend and interest cash flow schedule.
4. **Risk, Beta & Volatility Analytics (Pages 12-15):**
   - MPT quantitative risk statistics table (Std Dev, Beta, Sharpe, Sortino, VaR, CVaR).
   - Capital Allocation Line (CAL) and risk-return scatter analysis.
   - Deterministic macroeconomic shock scenario table and chart.
   - Cross-asset correlation matrix and structural diversification analysis.
5. **Itemized Holdings & Sector Allocations (Pages 16-20):**
   - Consolidated master holdings inventory with shares, prices, market values, weights, yields, and 52-week ranges.
   - Granular account-by-account holding schedules.
   - Look-through GICS equity sector allocation table and chart.
   - Top 25 underlying corporate look-through blue-chip holdings.
   - Geographic distribution and market capitalization tier analysis.
6. **Strategic Wealth Advisory, Rebalancing & Disclosures (Pages 21-25):**
   - Rebalancing roadmap table with account-specific execution steps and cash deployment plans.
   - Tax-loss harvesting protocol, replacement ETF pairs, and multi-year fee compounding advantages.
   - Fiduciary review summary, 5-point action checklist, and multi-decade wealth projections.
   - Source data provenance registry with clickable reference URLs.
   - Institutional regulatory disclosures, compliance notices, and methodology definitions.

### 6. Compilation, Verification and Export

- Execute the Python build script in the workspace environment.
- Verify the exact page count using `pypdf` to confirm it falls strictly within the required page window (e.g. 15-25 pages).
- Upload the compiled PDF to Google Drive using Drive tools and provide the user with the direct view URL.

## Best Practices and Formatting Guidelines

- **Color Palette:** Use an institutional corporate palette (e.g. Primary Navy `#003B70`, Accent Blue `#007BC8`, Slate `#5B6770`, Light Background `#F4F6F8`, Charcoal `#222222`).
- **Data Grounding:** Extract all quantitative data points directly from source materials. If data is unavailable, state the gap clearly rather than inventing figures.
- **Zero Ellipses:** Ensure Python generation code is 100% complete and self-contained with no placeholder comments or truncated sections.
- **Clean Layouts:** Maintain tight vertical spacers (Spacer height 2-4 pt) and compact table row padding (padding 1.5-3 pt) so every page fills exactly one physical PDF page.

## Gotchas

- In ReportLab canvas methods, use `colors.HexColor('#HEX')` with `setFillColor` and `setStrokeColor`; do not use non-existent methods like `setFillColorHex`.
- When instantiating `Table(data, colWidths=...)`, ensure `data` is a list of row lists (`[headers] + rows`), not a flattened list of Paragraphs.
- Always calibrate vertical heights across text and tables on each page to avoid unintentional page overflows before `PageBreak()`.
- Test PDF page count using `pypdf.PdfReader` immediately after building.

---
name: citibank-portfolio-analysis
description: Generates comprehensive institutional-grade Citibank Portfolio Analysis reports and fiduciary review PDFs (15-25 pages) for High-Net-Worth private wealth clients. Use when the user asks to generate, update, or analyze a Citibank investment portfolio report, synthesize multi-account holdings, calculate asset allocations, benchmark against blended indices, perform quantitative risk analytics, or compile wealth management PDF reviews using ReportLab and Matplotlib.
allowed-tools: drive context_service_agent vm_shell notebooklm
---

# Citibank Portfolio Analysis

Generate institutional-grade, fiduciary review PDF reports for High-Net-Worth private wealth clients managing multi-account portfolios at Citibank.

## Summary

This skill automates the extraction, synthesis, and reporting of client portfolio data across taxable brokerage accounts, Traditional IRAs, Roth IRAs, and bank cash reserves. It performs quantitative asset allocation, Modern Portfolio Theory (MPT) risk modeling, factor attribution, and tax-efficient rebalancing analysis, compiling the results into an institutional 15-25 page PDF using ReportLab Platypus and Matplotlib.

## When to Use

Use this skill in any of the following scenarios:

- The user requests a Citibank portfolio review, investment report, or fiduciary client presentation.
- The user provides an investment portfolio spreadsheet or Morningstar ETF profiles and asks to compile a multi-page PDF analysis.
- The user requests multi-account portfolio synthesis across taxable, Traditional IRA, and Roth IRA structures.
- The user asks for asset allocation rebalancing roadmaps, tax-loss harvesting evaluations, or multi-period performance benchmarking.
- The user needs programmatic PDF generation incorporating high-resolution Matplotlib charts, two-pass page numbering, and institutional branding.

## Steps

### Step 1: Retrieve and Extract Source Data

1. Download or query the client's portfolio source documents, typically a Google Sheet or CSV containing multi-account position details (e.g. `Investments_Citibank`).
2. Verify all account numbers, registration types, ticker symbols, share counts, live prices, market valuations, and existing cash balances.
3. Query ETF analytical metrics from Morningstar sources or knowledge bases for each constituent holding:
   - Trailing total returns (YTD, 1-Year, 3-Year, 5-Year, 10-Year).
   - Modern Portfolio Theory risk metrics (Standard Deviation, Sharpe Ratio, Sortino Ratio, Beta, Alpha).
   - Equity style attributes (Morningstar 9-box style classification, weighted median market cap, P/E, P/B ratios).
   - Fixed income duration, effective maturity, 30-day SEC yield, and credit ratings.
   - Look-through sector breakdowns and top equity concentrations.

### Step 2: Perform Portfolio Synthesis & Analytics

1. Calculate consolidated portfolio metrics:
   - Aggregate market value across all taxable and tax-advantaged accounts.
   - Current broad asset class weightings (Equities, Fixed Income, Alternatives, Cash Equivalents).
   - Variance against strategic policy targets (e.g. 75/20/5 or client-specified benchmark).
2. Calculate weighted portfolio risk-adjusted return metrics:
   - Annualized standard deviation using the holding covariance matrix.
   - Portfolio Sharpe Ratio and Sortino Ratio relative to the risk-free rate.
   - Value at Risk (VaR) under 95% and 99% 1-month parametric confidence intervals.
3. Formulate stress-testing scenario impacts:
   - Equity market drawdowns (-10%, -20%, -35%).
   - Interest rate shocks (+100 bps, +200 bps duration impact on fixed income).
   - Macroeconomic stagflation (inflation surge, commodity spikes, multiple compression).
4. Identify tax-advantaged rebalancing opportunities:
   - Prioritize zero-tax-drag trades within tax-deferred (Traditional IRA) and tax-exempt (Roth IRA) accounts.
   - Screen taxable brokerage lots for tax-loss harvesting or long-term capital gains preservation.

### Step 3: Generate High-Resolution Matplotlib Visualizations

Create and save high-resolution (300 DPI) charts using Citibank brand colors:

- Primary Navy: `#003B70`
- Accent Citi Blue: `#007BC8`
- Soft Slate: `#5B6770`
- Light Background: `#F4F6F8`
- Dark Charcoal: `#222222`

Key required charts:

1. `chart_asset_allocation.png`: Two-panel visualization with a donut chart of current asset weights and a bar chart of target vs actual weightings.
2. `chart_historical_returns.png`: Multi-period annualized return bar chart (YTD, 1Y, 3Y, 5Y) and 5-year cumulative growth of $100,000 trajectory plot.
3. `chart_risk_return.png`: Scatter plot of annualized standard deviation vs 5-year return across holdings, alongside a 12-month rolling volatility trend.
4. `chart_sector_exposure.png`: Horizontal bar chart of look-through sector exposures vs S&P 500 benchmark and top 10 look-through equity holdings.

### Step 4: Programmatically Build the ReportLab Platypus PDF

1. Configure document geometry using `SimpleDocTemplate` with Letter size and standard margins (36pt to 45pt).
2. Implement a two-pass `NumberedCanvas` class to dynamically record total pages and draw consistent running headers, footers, rule lines, and page numbers formatted as `Page X of Y`.
3. Construct the 25-page flowable story following the section breakdown:
   - Section 1 (Pages 1-2): Cover Page and Executive Overview with Macroeconomic Backdrop.
   - Section 2 (Pages 3-6): Asset Allocation, Drift Analysis, Equity Style Matrix, and Fixed Income Architecture.
   - Section 3 (Pages 7-11): Performance Benchmarking, Factor Attribution, Return Trajectories, Account-Level Performance, and Cash Flow Yields.
   - Section 4 (Pages 12-15): Risk Profiles, MPT Analytics, Volatility Surfaces, Scenario Stress-Testing, and Correlation Matrix.
   - Section 5 (Pages 16-21): Master Holdings Inventory, Account Reviews (Brokerage, IRA, Roth), Sector Exposures, and Liquidity Profiles.
   - Section 6 (Pages 22-25): Fiduciary Wealth Advisory, Tax-Loss Harvesting, Asset Location Optimization, Implementation Roadmap, and Regulatory Disclosures.
4. Enforce formatting integrity:
   - Wrap every table cell inside a `Paragraph` flowable to eliminate text clipping.
   - Explicitly define column widths that sum to exactly 540pt (printable width for 36pt margins).
   - Insert explicit `PageBreak()` calls between pages to guarantee strict 1-page-per-topic alignment.

### Step 5: Validate and Export Deliverables

1. Execute the Python script using `vm_shell:execute_bash`.
2. Verify total page count using `pypdf` to ensure the document contains the target 25 pages without unexpected page overflows or empty pages.
3. Export the compiled PDF to Google Drive via `drive:create_file` so the client has immediate cloud access.
4. Provide the user with direct links to the generated PDF and the standalone Python script.

## Gotchas

- Text Overflow: Any uncontained table cell or oversized spacer can cause unintended page overflow. Always set table cell padding to 2-4pt and test page counts with `pypdf`.
- Canvas Pass Order: Running footers showing total page count require two passes. Never try to hardcode the page count or write headers in `onFirstPage` / `onLaterPages` if exact dynamic counts are required.
- Font Availability: ReportLab standard builds only guarantee standard Type 1 fonts (Helvetica, Times-Roman, Courier). Do not reference external fonts like Arial or Roboto unless explicitly registered via `pdfmetrics`.
- Matplotlib Memory: Always call `plt.close()` immediately after saving figures to avoid memory bloat during multi-chart generation.
- Grounding: Never extrapolate or fabricate share prices or valuations. If live market data is not present in the source files, clearly flag the informational gap.

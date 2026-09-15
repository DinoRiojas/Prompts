# Citibank Portfolio Analysis Reference Guide

## Institutional Visual & Brand Styling

- Primary Navy: `#003B70` (headers, primary cards, main branding)
- Accent Citi Blue: `#007BC8` (subheadings, secondary lines, active highlights)
- Soft Slate: `#5B6770` (captions, sub-labels, neutral benchmarks)
- Light Background: `#F4F6F8` (alternating rows, callout background fills)
- Dark Charcoal: `#222222` (body text, table contents)
- Border Color: `#CBD5E1` (table borders, divider lines)
- Page Margins: 0.5 to 0.75 inches (36pt to 54pt)

## Standard 25-Page Document Architecture

- Section 1: Cover Page & Executive Overview (Pages 1-2)
  - Page 1: Cover page, client metadata, total relationship valuation, navigation directory.
  - Page 2: Macroeconomic environment, monetary policy backdrop, portfolio architecture.
- Section 2: Asset Allocation & Portfolio Structure (Pages 3-6)
  - Page 3: Consolidated asset allocation vs strategic policy benchmarks.
  - Page 4: Visual asset allocation donut and target vs actual comparison charts.
  - Page 5: Equity style structure across the Morningstar 9-box matrix.
  - Page 6: Fixed income sleeve duration, credit quality, and curve positioning.
- Section 3: Performance Benchmarking & Historical Returns (Pages 7-11)
  - Page 7: Multi-period trailing returns (YTD, 1Y, 3Y, 5Y) vs custom blended benchmarks.
  - Page 8: Return attribution and Brinson-Fachler factor decomposition.
  - Page 9: Multi-period performance bar chart and cumulative growth of $100k chart.
  - Page 10: Account-level performance dynamics and tax efficiency analysis.
  - Page 11: Income generation, SEC yields, and projected annual cash flows.
- Section 4: Risk, Beta & Volatility Analytics (Pages 12-15)
  - Page 12: MPT risk metrics (Std Dev, Sharpe, Sortino, Beta, VaR).
  - Page 13: Risk-return scatter plot and rolling volatility trend chart.
  - Page 14: Institutional stress-testing and scenario matrix.
  - Page 15: Cross-asset correlation matrix and diversification benefits.
- Section 5: Itemized Holdings & Sector Allocations (Pages 16-21)
  - Page 16: Master holdings inventory across all accounts.
  - Page 17: Account review for Self Direct Brokerage.
  - Page 18: Account review for Traditional IRA and Roth IRA.
  - Page 19: Sector exposure deconstruction vs S&P 500 benchmark.
  - Page 20: Sector breakdown and top 10 look-through equity holdings charts.
  - Page 21: Geographic exposure, credit distribution, and liquidity profile.
- Section 6: Strategic Wealth Advisory, Rebalancing & Disclosures (Pages 22-25)
  - Page 22: Fiduciary advisory recommendations and rebalancing guidelines.
  - Page 23: Tax-loss harvesting opportunities and asset location roadmap.
  - Page 24: Three-phase implementation roadmap and wealth plan.
  - Page 25: Regulatory disclosures, Form CRS, and fiduciary notices.

## Core Technical Rules for ReportLab

- Always wrap every table cell in Paragraph flowables to prevent text clipping.
- Explicitly define colWidths summing to the exact printable width (540pt for letter with 36pt margins).
- Use a custom two-pass NumberedCanvas to compute and render total pages ("Page X of Y").
- Do not let headings orphan; use keepWithNext=True or wrap tables in KeepTogether where appropriate.
- Export all Matplotlib figures at 300 DPI with tight bounding boxes before inserting into the Platypus story.

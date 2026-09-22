Task:
Generate a Citibank Portfolio Report and save as a pdf file using the following Resources and Prompt.

Resources:

https://docs.google.com/spreadsheets/d/1x4rvOThgFhgTdpuslqsYfhSoAibVDM3BZOUHlp2RW1s/edit?gid=861982464#gid=861982464

https://www.morningstar.com/etfs/xmex/voo/portfolio
https://www.morningstar.com/etfs/xmex/voo/quote
https://www.morningstar.com/etfs/xmex/voo/performance
https://www.morningstar.com/etfs/xmex/voo/risk

https://www.morningstar.com/etfs/xmex/vtip/portfolio
https://www.morningstar.com/etfs/xmex/vtip/quote
https://www.morningstar.com/etfs/xmex/vtip/performance
https://www.morningstar.com/etfs/xmex/vtip/risk

https://www.morningstar.com/etfs/xnas/bnd/portfolio
https://www.morningstar.com/etfs/xnas/bnd/quote
https://www.morningstar.com/etfs/xnas/bnd/performance
https://www.morningstar.com/etfs/xnas/bnd/risk

https://www.morningstar.com/etfs/xmex/vtv/portfolio
https://www.morningstar.com/etfs/xmex/vtv/quote
https://www.morningstar.com/etfs/xmex/vtv/performance
https://www.morningstar.com/etfs/xmex/vtv/risk

https://www.morningstar.com/etfs/xmex/vym/portfolio
https://www.morningstar.com/etfs/xmex/vym/quote
https://www.morningstar.com/etfs/xmex/vym/performance
https://www.morningstar.com/etfs/xmex/vym/risk

https://www.morningstar.com/etfs/xmex/vug/portfolio
https://www.morningstar.com/etfs/xmex/vug/quote
https://www.morningstar.com/etfs/xmex/vug/performance
https://www.morningstar.com/etfs/xmex/vug/risk

https://www.morningstar.com/etfs/xmex/vb/portfolio
https://www.morningstar.com/etfs/xmex/vb/quote
https://www.morningstar.com/etfs/xmex/vb/performance
https://www.morningstar.com/etfs/xmex/vb/risk

https://www.morningstar.com/etfs/xmex/vgt/portfolio
https://www.morningstar.com/etfs/xmex/vgt/quote
https://www.morningstar.com/etfs/xmex/vgt/performance
https://www.morningstar.com/etfs/xmex/vgt/risk

https://www.morningstar.com/etfs/xmex/vht/portfolio
https://www.morningstar.com/etfs/xmex/vht/quote
https://www.morningstar.com/etfs/xmex/vht/performance
https://www.morningstar.com/etfs/xmex/vht/risk

https://www.morningstar.com/etfs/xnas/vgit/portfolio
https://www.morningstar.com/etfs/xnas/vgit/quote
https://www.morningstar.com/etfs/xnas/vgit/performance
https://www.morningstar.com/etfs/xnas/vgit/risk

--------------------------------------------------------------
Prompt:

Role: Principal Wealth Management Strategist & Python Reporting Architect.

Context: 
You are operating within Gemini Notebook / NotebookLM with direct access to the attached portfolio source documents (holdings, transactions, asset valuations, and benchmark data). The objective is to produce an institutional-grade, fiduciary review document titled "Citibank Portfolio Analysis" tailored specifically for High-Net-Worth (HNW) private wealth clients.

Task:
Analyze and synthesize the portfolio data from the attached notebook sources. Write a complete, standalone, production-ready Python script using `ReportLab` (utilizing `Platypus`, `SimpleDocTemplate`, `Paragraph`, `Table`, `TableStyle`, `KeepTogether`, `PageBreak`, and `Spacer`) and `Matplotlib` to compile a fully populated 15�25 page client PDF.

Programmatically construct the document with the following section-by-section breakdown:
1. Cover Page & Executive Overview (Pages 1�2):
   - Formal title ("Citibank Portfolio Analysis"), client/portfolio metadata, total portfolio valuation summary.
   - Executive commentary, macroeconomic review, and strategic portfolio positioning overview.
2. Asset Allocation & Portfolio Structure (Pages 3�6):
   - Detailed allocation breakdowns across Equities, Fixed Income, Alternatives, Cash & Cash Equivalents.
   - High-resolution Matplotlib donut/pie charts illustrating target vs. actual weightings and asset class distributions.
3. Performance Benchmarking & Historical Returns (Pages 7�11):
   - Multi-period performance analysis (YTD, 1-Year, 3-Year, 5-Year annualized returns).
   - Direct comparison against custom blended benchmarks with visual Matplotlib trend and bar charts.
4. Risk, Beta & Volatility Analytics (Pages 12�15):
   - Portfolio risk profile: Standard Deviation, Sharpe Ratio, Sortino Ratio, Beta, and Value at Risk (VaR).
   - Stress-testing scenario matrix (e.g., equity market drawdowns, interest rate shocks, stagflation).
5. Itemized Holdings & Sector Allocations (Pages 16�21):
   - Formatted multi-page tables itemizing individual holdings, ticker symbols, share quantities, cost basis, current market value, unrealized gain/loss, and dividend yields.
   - Sector and geographic exposure breakdown charts and tables.
6. Strategic Wealth Advisory, Rebalancing & Disclosures (Pages 22�25):
   - Fiduciary advisory commentary: tax-loss harvesting opportunities, rebalancing roadmap, wealth preservation strategies.
   - Regulatory disclosures, fiduciary notices, methodology notes, and standard disclaimers.

Constraints & Execution Rules:
- Source Grounding: Extract all numerical data, holdings, weights, and valuations directly from the attached notebook sources. If any data point is missing or ambiguous, explicitly state the informational gap rather than inventing figures.
- Code Completeness: Provide 100% executable Python code without placeholders, ellipses (`...`), or truncated logic (e.g., `# add remaining pages here`). Include all necessary imports, table styles, chart generation helpers, and flowables.
- Visual & Brand Styling: Implement an institutional Citibank-aligned palette: Primary Navy (`#003B70`), Accent Citi Blue (`#007BC8`), Soft Slate (`#5B6770`), Light Background (`#F4F6F8`), and Dark Charcoal (`#222222`). Use standard page margins (0.5 to 0.75 inches) and clean typography.
- Pagination & Canvas Mechanics: Implement a custom two-pass `NumberedCanvas` class to dynamically calculate and render running headers and footers with page numbers formatted as `"Page X of Y"` across all pages.
- Formatting Integrity: Enforce proper table column widths and wrap table cell contents in `Paragraph` flowables to prevent text clipping or page overflow.

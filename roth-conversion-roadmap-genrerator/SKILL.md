---
name: roth-conversion-roadmap-generator
description: Analyzes portfolio holdings and tax baselines to build an institutional-grade, multi-year Roth conversion roadmap in Google Sheets. Use when the user asks to plan, model, or generate a Roth conversion schedule, retirement decumulation roadmap, or tax-bracket filling spreadsheet from financial files.
allowed-tools: drive sheets_agent
---

# Roth Conversion Roadmap Generator

A specialized skill for analyzing investment portfolios and tax baselines to design customized, multi-year Roth conversion roadmaps and build comprehensive Google Sheets models adhering to IRS rules and fiduciary decumulation standards.

## When to Use

- When the user asks to generate or model a multi-year Roth conversion roadmap or schedule.
- When the user requests a Google Sheet evaluating Roth conversions alongside Required Minimum Distributions (RMDs).
- When analyzing portfolio holdings (Traditional IRA, Roth IRA, taxable brokerage, cash) and tax projections to optimize bracket filling.
- When evaluating the tax sensitivity of retiring versus continuing active employment during conversion years.

## Workflow Steps

### 1. Data Extraction and Baseline Audit

- Extract portfolio balances across account types: Traditional/Rollover IRAs, Roth IRAs, taxable brokerage accounts, and cash reserves.
- Identify tax jurisdiction baselines: Federal filing status, state, and local tax residency (e.g., New York State and NYC).
- Check for existing non-deductible basis across all traditional accounts to determine the Form 8606 pro-rata taxable percentage.
- Identify current and projected income streams: Social Security, pensions, earned wages, dividends, and interest.
- Identify RMD commencement age: Age 73 for individuals born 1951-1959, or Age 75 for individuals born 1960 or later under the SECURE 2.0 Act.

### 2. Statutory RMD and Anti-Conversion Mechanics

- Apply Treasury Regulation Section 1.408A-4 (Q&A-6): RMDs cannot be converted into a Roth IRA.
- Enforce the first-dollars-out rule: The first distributions taken from a Traditional IRA in an RMD year satisfy the annual RMD first.
- If the user specifies a total traditional IRA withdrawal cap (e.g., $100,000):
  - Step A: Calculate that year's statutory RMD using the IRS Uniform Lifetime Table (Table III) divisor based on the prior year-end balance.
  - Step B: Distribute the RMD amount directly to the client as ordinary taxable income.
  - Step C: Allocate only the remainder (Total Cap minus RMD) toward the Roth conversion.

### 3. Multi-Year Conversion and Tax Modeling

- Project account balances across the conversion horizon (e.g., 5 to 10 years) applying realistic annual return assumptions on remaining balances.
- Target the elimination of Traditional IRA balances to stop mandatory taxable RMD growth in later retirement years.
- Model tax liabilities across all applicable jurisdictions:
  - Federal ordinary income tax brackets and standard/itemized deductions.
  - State and local income taxes, applying statutory exclusions (e.g., NYS Pension and Annuity Exclusion for qualifying taxpayers age 59.5+).
  - Net Investment Income Tax (NIIT 3.8%) if Modified Adjusted Gross Income exceeds statutory thresholds ($200,000 for Single, $250,000 for MFJ).
- Stress-test employment scenarios: Compare conversion tax liabilities under active employment wages versus full retirement to highlight marginal bracket differences.

### 4. Build the Google Sheet via sheets_agent

- Create a new Google Sheet in the user's Google Drive and structure it across four core tabs:
  1. Executive Summary and Portfolio: Client demographics, portfolio breakdown, baseline tax rates, and core strategic takeaways.
  2. Multi-Year Roadmap: Year-by-year table displaying IRS divisors, beginning Traditional IRA, RMD distributions, Roth conversions, total outflows, ending Traditional IRA, ending Roth IRA, and annual tax liabilities.
  3. Scenario Comparison and Retirement: Matrix comparing capped outflow strategy, flat conversion strategy, and status quo (RMD-only), alongside active wage versus retirement tax sensitivity.
  4. Tax Cliffs and IRS Rules: Educational reference detailing Treasury Regulation Section 1.408A-4, Form 8606 pro-rata mechanics, tax payment sourcing, Medicare IRMAA surcharge tiers, 5-year rules, and quarterly estimated tax safe harbor schedules.
- Invoke sheets_agent:call with a well-formed XML payload containing comprehensive gathered data and clear architectural goals.

### 5. Deliver Strategic Advisory Insights

- Present the multi-year schedule and scenario comparisons using clean, scannable Markdown tables.
- Explicitly explain the tax sourcing recommendation: Pay conversion taxes from outside taxable cash and brokerage reserves to avoid tax drag and maximize tax-free compounding inside the Roth.
- Highlight secondary tax cliffs: Screen for Medicare Part B and D IRMAA surcharge brackets (2-year lookback) and Social Security provisional income thresholds.
- Detail operational guardrails: December 31 annual conversion cutoffs, quarterly estimated tax payment safe harbors (Form 1040-ES / state vouchers), and the dual 5-year rules.
- Include a clear fiduciary disclosure that all models are for educational and strategic planning purposes.

## Gotchas and Edge Cases

- Never attempt to convert an RMD: Statutory rules strictly disallow converting RMD amounts to Roth.
- Tax withholding trap: Never recommend withholding conversion taxes from the Traditional IRA if outside liquidity is available, as it erodes compound growth and triggers early withdrawal penalties if under age 59.5.
- Medicare IRMAA cliff: Added conversion income triggers Medicare Part B and D premium surcharges two years later. Always screen MAGI against the IRMAA surcharge tiers.
- Pro-rata aggregation: All non-Roth IRAs (Traditional, SEP, SIMPLE) are aggregated when calculating taxable conversion ratios on Form 8606.

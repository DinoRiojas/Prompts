---
name: roth-conversion-strategy
description: Analyze financial and tax data in Google Drive to model multi-year Roth conversion roadmaps and generate a detailed roadmap spreadsheet in Google Sheets. Use when the user requests a Roth conversion strategy, multi-year retirement tax planning, RMD and Roth conversion modeling, or asks to evaluate converting Traditional IRA balances to Roth accounts.
allowed-tools: drive sheets_agent
---

# Roth Conversion Strategy

## Summary

This skill provides an end-to-end workflow for analyzing client portfolio holdings and tax baselines from Google Drive, designing optimized multi-year Roth conversion schedules, and generating an institutional-grade Roth conversion roadmap in Google Sheets.

## When to Use

- When the user asks to create or evaluate a Roth conversion roadmap or multi-year decumulation strategy.
- When the user provides financial or tax records in Google Drive (e.g. portfolio holdings, tax estimators, investment statements) and requests Roth conversion planning.
- When the user wants to compare Roth conversion scenarios against status-quo Required Minimum Distribution (RMD) rules.
- When the user asks to model retirement tax bracket filling, IRMAA thresholds, or tax-efficient IRA distribution sequencing.

## Interaction and Planning Workflow

### 1. Data Discovery and Ingestion

Retrieve and audit the client financial baselines from Google Drive:

- Search Google Drive for relevant folders (e.g. "Investments") and files (e.g. tax estimators such as TaxEstimator_2026.xlsx, portfolio balances such as Investments_Citibank.gsheet).
- Extract account balances:
  - Traditional IRA balance (audit pre-tax vs non-deductible after-tax basis for Form 8606 pro-rata rules).
  - Existing Roth IRA balance.
  - Taxable brokerage and cash reserves (available outside liquidity to pay conversion taxes).
- Identify client demographic and tax parameters:
  - Filing status (Single, Married Filing Jointly, Head of Household).
  - Current age, birth date, and SECURE Act 2.0 RMD commencement age (age 73 for individuals born 1951 through 1959; age 75 for individuals born 1960 or later).
  - Employment status and wage projections (transition year from active employment to full retirement).
  - Fixed retirement income: Social Security gross benefit (and taxable portion up to 85%), pensions, taxable dividends, and interest.
  - Tax jurisdiction: Federal, state, and local tax rates, standard deductions (including additional standard deduction for age 65+), and specific exemptions (e.g. NY State $20,000 pension and annuity exclusion).

### 2. Strategy and Conversion Modeling

Apply fiduciary planning mechanics and statutory IRS rules:

- Anti-Conversion Rule (IRC Section 408(d)(3)(E) and Treas. Reg. Section 1.408A-4): In any year where an RMD is required, the first dollars distributed from the Traditional IRA satisfy the RMD. RMDs can never be rolled over or converted into a Roth IRA. Only amounts distributed in excess of the annual RMD may be converted.
- Outflow Capping Logic: When working with a total annual outflow target (e.g. $100,000 total Traditional IRA distribution):
  - Annual Statutory RMD = Prior Year-End Traditional IRA Balance / IRS Uniform Lifetime Table Divisor.
  - Annual Roth Conversion Amount = max(0, Total Outflow Target - Statutory RMD).
  - If the Traditional IRA balance drops below the total target outflow, the remaining balance is converted in full.
- Tax Sourcing Strategy: Advise paying all resulting federal, state, and local conversion taxes from outside taxable cash or brokerage accounts rather than withholding from the IRA. This preserves 100% of the converted funds for tax-free compounding inside the Roth IRA and avoids early withdrawal penalties if under age 59.5.
- Multi-Year Decumulation Trajectory: Model year-by-year account balances until the Traditional IRA is completely eliminated, projecting the tax-free growth of the Roth IRA.
- Multi-Scenario Evaluation:
  - Scenario 1 (Capped Outflow): Satisfy RMD first, convert the remainder up to a specified annual cap.
  - Scenario 2 (Flat Conversion + RMD): Fixed conversion amount each year in addition to statutory RMDs.
  - Scenario 3 (Status Quo / Baseline): Take only statutory RMDs with zero conversions, highlighting future tax drag, escalating RMDs, and tax burden on heirs under the SECURE Act 10-year rule.
  - Employment Sensitivity: Compare tax liabilities and marginal rates during active earning years versus full retirement years.

### 3. Google Sheets Deliverable Generation

Create a clean, institutional Google Sheet with distinct tabs:

- Tab 1: Executive Summary & Portfolio
  - Client profile, filing status, RMD commencement age, portfolio breakdown, outside liquidity, and key strategic takeaways.
- Tab 2: Multi-Year Roadmap
  - Structured columns: Year, Age, IRS Divisor Factor, Beginning Traditional IRA Balance, Statutory RMD, Modeled Roth Conversion, Total Outflow, Ending Traditional IRA Balance, Ending Roth IRA Balance, AGI, Federal Tax, State Tax, Local Tax, and Total Tax.
- Tab 3: Scenario Comparison & Sensitivity
  - Side-by-side comparison of total taxes paid, year Traditional IRA is eliminated, ending Roth wealth, and annual tax savings between working and retired baselines.
- Tab 4: Tax Cliffs & IRS Rules
  - Reference guidelines on the Anti-Conversion Rule, Form 8606 Pro-Rata mechanics, Medicare IRMAA surcharge brackets (2-year lookback), Net Investment Income Tax (NIIT), and the Roth 5-year rules.

## Gotchas and Edge Cases

- Never convert the RMD: Ensure statutory RMDs are calculated and accounted for separately before calculating conversion amounts.
- Pro-rata rule check: Always verify whether the client has non-deductible basis in any Traditional, SEP, or SIMPLE IRA. If non-deductible basis exists, Form 8606 pro-rata rules apply.
- Medicare IRMAA tiers: Added conversion income increases Modified Adjusted Gross Income (MAGI) and can trigger higher Medicare Part B and Part D premiums two years later. Highlight these tiers in the analysis.
- Safe harbor estimated taxes: Large Roth conversions increase taxable income, requiring quarterly estimated tax payments (or withholding adjustments) to satisfy IRS safe harbor rules.
- Fiduciary disclaimer: Clearly state that all modeling is educational and strategic, designed to support decision-making alongside a licensed CPA, tax attorney, or fiduciary advisor.

---
name: sql-svr-agent
description: Specialized assistant for SQL Server reporting and batch processing analysis based on Accela FIRES schema patterns. Use when querying, troubleshooting, or drafting SQL scripts for permits, inspections, fee items, audit trails, and lien automations.
---

# SQL Server Agent (sql-svr-agent)

The `sql-svr-agent` skill equips the assistant to analyze, generate, and optimize T-SQL queries and Accela EMSE batch automation scripts modeled after the Accela FIRES database schema.

## Domain Schema & Architecture Patterns

### Primary Database Tables
- **`b1permit`**: Base permit/plan review entity. Key join columns: `serv_prov_code`, `b1_per_id1`, `b1_per_id2`, `b1_per_id3`. Public display ID: `b1_alt_id`. Common filters include `b1_per_type` (e.g. `'Plan Review'`, `'Common'`), `b1_per_sub_type` (e.g. `'Inspection'`), and `b1_appl_status <> 'Inactive'`.
- **`bchckbox`**: Form/application checklist and Application Specific Information (ASI). Common columns: `b1_checkbox_desc`, `b1_checklist_comment`, `b1_checkbox_type`. Standard pattern: PIVOT or `MAX(CASE WHEN ... THEN ... END)` partitioned by permit key to extract fields like `D.O.`, `Alpha Prefix`, `Account Type`, `Application Type`, and `No Fee`.
- **`bappspectable_value` / `baspect_value`**: Table-driven sub-attributes (ASIT), including warden tables (`TABLE_NAME = 'WARDENS'`) and billing information (`TABLE_NAME = 'BILLING INFORMATION'`).
- **`b3addres` & `b3contact`**: Site addresses and contacts. Best-practice pattern: Deduplicate using `ROW_NUMBER() OVER (PARTITION BY serv_prov_code, b1_per_id1, b1_per_id2, b1_per_id3 ORDER BY ... DESC)` (ordering by `b1_primary_addr_flg` for address, and `rec_date` for contacts).
- **`b3apo_attribute`**: Address/Parcel/Owner attributes containing identifiers like `BIN`, `BLOCK`, `LOT`, and `ADMIN COMPANY`.
- **`f4invoice`, `x4feeitem_invoice`, `f4feeitem_audit_trail`**: Invoicing and fee trail.
  - Link `b1permit` to `x4feeitem_invoice` using agency and permit triple keys.
  - Link `x4feeitem_invoice` to `f4invoice` on `invoice_nbr`.
  - Link audit trail via `feeitem_seq_nbr`.
  - Common UDF conventions: `F4INVOICE_UDF1` = Cycle / Account Type (`<Cycle>-<AcctType>`), `F4INVOICE_UDF2` = Cycle Clock Date, `F4INVOICE_UDF3` = First Dunning Date, `F4INVOICE_UDF4` = First Lien Notice Date.
- **`b6condit` & `gtmpl_attribute`**: Conditions and hold tracking, specifically for lien condition management (`b1_con_typ = 'Lien'`). Join `gtmpl_attribute` on `entity_seq1 = b1_con_nbr` and `entity_type = '11'`.

### Business Rules & Calculation Standards
1. **District Office (D.O.) Formatting**: Normalize numeric D.O. codes to two characters using `RIGHT('0' + ACTDO, 2)`. Exclude administrative D.O. codes (e.g. `'25'`, `'33'`) where automated lien/enforcement pipelines do not apply.
2. **Permit vs. Non-Permit Due Date Logic**:
   - Permit group accounts (`ACTTYPE IN ('10', '15', '20', '25')` and `ACTDO <> '19'`) use a 455-day aging threshold: `DATEADD(day, 455, CONVERT(DATE, F4INVOICE_UDF2))`.
   - Non-permit accounts use a 120-day aging threshold: `DATEADD(day, 120, CONVERT(DATE, F4INVOICE_UDF2))`.
3. **JSON Metadata Filters**: Process invoice JSON tags cleanly using `JSON_VALUE(INVOICE_COMMENT, '$.<flag>')` or structured wildcard matching (e.g., verifying `secondReminder: true`, and checking that `doNotProcess`, `lienAdded`, or penalty flags are not set).

## Guidelines for Generating & Refactoring Scripts

1. **Temp Table Staging over Massive Nested CTEs**: For complex report runs or large date windows, stage initial invoice cohorts into temporary tables (`#TMP_Returned_Values`, `#TMP_do_unit`, `#TMP_lien`) with explicit drops (`DROP TABLE IF EXISTS #...`) to minimize memory pressure and optimize execution plans.
2. **Deterministic Date Parsing**: Use safe conversion functions like `TRY_CONVERT(date, ...)` or validate with `ISDATE(...) = 1` prior to conversion. Ensure date arithmetic respects `SET DATEFORMAT mdy;`.
3. **Accela EMSE Batch Integration**: When bridging SQL scripts to EMSE JavaScript batch jobs (`batch_ir_lien`, `batch_ir_lien_notice`), match parameter passing conventions (`aa.env.getValue(...)`), maintain condition lookups, and handle agency mask sequence lookups via proxy invokers.

---
title: "Adyen Marketplace Balance Platform Payout Report"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reports-and-fees/payout-report"
raw_files:
  - "adyen/docs/marketplaces/reports-and-fees/payout-report/2026-09-15.md"
tags: [adyen, marketplaces, platforms, reporting, payouts, reconciliation]
---

## Overview

This 2026-09-15 Marketplace-path [[adyen]] Balance Platform Payout Report guide belongs under [[adyen-reporting]] for modern [[adyen-platforms]] scheduled payout sweeps. It calls the report daily and available to platforms with daily, weekly or monthly payout schedules. Data is said to arrive shortly after daily processing, around 2:00 AM CEST, covering payouts processed midnight-to-midnight CEST and their debit/credit transactions. A day with no processed payouts yields an empty report (raw lines 15–27).

## Key takeaways

- **Scope and grain:** The report identifies paid-out account holders and contributing transactions. Filter by Account Holder, Balance Account and Currency to inspect a particular account (raw lines 21–31). The prose says “one record line per account, per currency,” but the sample displays multiple capture rows and a negative booked `bankTransfer` row for the same account/currency. Treat the exact row grain as ambiguous in this snapshot; the transaction-level sample must not be compressed into one aggregate row (lines 31, 49–68).
- **Available balance and rolling carry:** Scheduled payout calculation considers the existing balance and expected future debits/credits. Pending refunds or chargebacks can be withheld, leaving a nonzero rolling balance carried into the next report (raw lines 33–35). To investigate those pending transactions, use the Balance Platform Accounting Report and filter transfers whose booking date precedes the payout date while value date follows it (line 37). The sample's positive capture rows and negative booked payout rows are illustrative account-ledger entries, not beneficiary-bank receipts (lines 49–68).
- **Clocks and identifiers:** The report window and approximate availability are described in CEST; the Payout Date column is defined as the CET date on which payout is **initiated**. Booking Date means the booking time and Value Date means when funds are available; each has its own timezone column (raw lines 21–25, 89–92, 117). This page does not reconcile CEST/CET daylight-saving wording. `Transfer Id` identifies a pending debit/credit, while `Transaction Id` identifies a completed debit/credit in the balance ledger; neither ID alone proves external bank credit (lines 87–88).
- **Retrieval and columns:** Customer Area can generate automatically by schedule or manually for a date. The page lists frequency as daily, weekly or monthly while also calling the report daily; the CSV filename pattern is `balanceplatform_payout_report_YYYY_MM_DD.csv` (raw lines 19, 29, 39–41). Standard columns include account holder/balance account, currency, category/type/status, signed `Balance (PC)`, `Rolling Balance (PC)`, references, PSP payment references and Payout Date. Optional columns include PSP modification references, Store, Payment Method, Managed Risk Blocked Amount and Platform Payment Split Type. Customer Area settings may produce additional columns absent from the linked sample (lines 43–45, 70–133).

## Detail locators

- Report eligibility, CEST window, empty-day behavior, filters and rolling-balance investigation: raw lines 15–41.
- Illustrative multiple capture and booked bank-transfer rows: raw lines 43–68; compare the row-grain statement at line 31.
- Standard column definitions and distinct ID/date/account fields: raw lines 70–117; optional columns: lines 119–133.

## Evidence boundary

This report supports balance-platform payout reconciliation for scheduled sweeps. It does not cover every on-demand or CashOut movement merely because a user balance account changed. A booked bank-transfer row and payout-initiation date are platform-ledger evidence, not independent proof of beneficiary bank receipt. Preserve the source's one-line-versus-multiple-row and CEST-versus-CET wording instead of inferring a settled reporting grain or timezone conversion. The sample is illustrative, and report configuration may add fields.

## Related

- [[adyen-reporting]] — reporting and reconciliation concept.
- [[adyen-platforms]] — modern Marketplace balance-platform context.
- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — existing Platforms-path accounting-report route for booking/value-date detail.
- [[source-adyen-docs-marketplaces-payout-webhooks]] — separate transfer and bank-status events.

## Raw Sources

- [[raw/adyen/docs/marketplaces/reports-and-fees/payout-report/2026-09-15|Pinned Marketplace Payout Report guide, captured 2026-09-15]]

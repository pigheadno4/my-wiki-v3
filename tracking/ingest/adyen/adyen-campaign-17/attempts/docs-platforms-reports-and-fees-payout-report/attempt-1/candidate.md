---
title: "Adyen Balance Platform Payout Report"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reports-and-fees/payout-report"
raw_files:
  - "adyen/docs/platforms/reports-and-fees/payout-report/2026-09-15.md"
tags: [adyen, platforms, reporting, payouts, reconciliation]
---

## Overview

The Balance Platform Payout Report is an Adyen for Platforms report for platforms with scheduled daily, weekly or monthly payout sweeps. The page calls it a daily report, says data becomes available shortly after daily payout processing at approximately 2:00 AM CEST, and describes payouts processed from midnight to midnight CEST with their contributing debit and credit transactions. No payout day yields an empty report. A report line or payout initiation date does not independently prove beneficiary-bank receipt. [[adyen]] [[adyen-platforms]] [[adyen-reporting]]

## Key takeaways

- **Account and transaction scope:** filter by Account Holder, Balance Account and Currency to inspect a payout for a particular account. The prose says one record line per account and currency, yet the displayed sample has multiple captured-payment rows plus a negative booked `bankTransfer` row for each account/currency. Preserve the transaction-row view and treat the prose as a grain ambiguity rather than assuming a single aggregate line.
- **Balances and timing:** available payout amount considers present balance and expected future debits/credits. Pending refunds or chargebacks can be withheld, leaving a non-zero rolling balance carried into the next report. To investigate it, the page directs readers to the Balance Platform Accounting Report, filtering transfers with booking date before and value date after the payout date. The sample's positive capture rows and negative booked bank-transfer row bring rolling balance to zero; these signs are examples, while `Balance (PC)` is defined as the amount debited or credited in payment currency.
- **Identifiers and columns:** standard columns include Account Holder, Balance Account, Currency, Transfer Id for a pending debit/credit, Transaction Id for a completed debit/credit, Booking Date, Value Date, Category, Type, Status, Balance (PC), Rolling Balance (PC), Reference, Description, Counterparty Balance Account Id, PSP payment references and Payout Date. Optional columns include PSP modification references, Store, Payment Method, Managed Risk Blocked Amount and Platform Payment Split Type. Do not collapse pending transfer and completed transaction IDs or infer a matching bank credit from them.
- **Date qualification:** the page describes the report's processing window and approximate availability in CEST, while the Payout Date column is defined as the date in CET when payout is initiated. Booking Date is the booking time and Value Date is when funds are available, with separate timezone columns. These are different clocks and meanings; the guide does not resolve daylight-saving interpretation across them.
- **Retrieval and evidence:** Customer Area can generate reports automatically on a schedule or manually for a day; the page lists frequency as daily, weekly or monthly despite calling the report daily. Default and added columns can vary by report settings, and a generated report may contain columns absent from the sample. The CSV pattern is `balanceplatform_payout_report_YYYY_MM_DD.csv`. Report rows and a booked bank transfer support platform-ledger reconciliation, not a beneficiary statement, legal ownership conclusion or payout-success guarantee.

## Detail locators

- Raw lines 15–41: scheduled-sweep eligibility, CEST window and approximate availability, empty reports, Customer Area generation, account/currency filter and rolling-balance investigation.
- Raw lines 43–68: sample row set with multiple capture rows and negative booked bankTransfer entries; compare against one-line prose at line 31.
- Raw lines 70–117: standard columns and definitions for transfer/transaction IDs, dates/time zones, category/type/status, signed Balance (PC), Rolling Balance and Payout Date.
- Raw lines 119–133: optional modification, Store, Payment Method, Managed Risk Blocked Amount and split-type columns.

## Related

- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — transfer booking/value-date detail for withheld balances.
- [[source-adyen-docs-platforms-payout-webhooks]] — separate transfer status events.
- [[source-adyen-docs-platforms-managed-payouts]] — scheduled-payout context.

## Raw Sources

- [[raw/adyen/docs/platforms/reports-and-fees/payout-report/2026-09-15|Balance Platform Payout Report snapshot, fetched 2026-09-15]]

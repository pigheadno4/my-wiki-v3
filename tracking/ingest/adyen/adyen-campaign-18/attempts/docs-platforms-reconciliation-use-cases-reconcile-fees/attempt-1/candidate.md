---
title: "Reconcile fees | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reconciliation-use-cases/reconcile-fees"
raw_files:
  - "adyen/docs/platforms/reconciliation-use-cases/reconcile-fees/2026-09-15.md"
tags: [adyen, platforms, reconciliation, fees, reports]
---

## Overview

This [[adyen]] for Platforms example explains how to reconcile balance-platform fee bookings across the Payment accounting report, Settlement detail report and Balance Platform Accounting Report. It distinguishes per-transaction payment fees, daily aggregate Processing fees and monthly invoicing adjustments. See [[adyen-reporting]] for the reporting route and evidence boundary.

## Key takeaways

- Interchange, Scheme fees, Markup and Commission assessed per transaction are deducted when captured payment funds are booked to balance accounts. The fee may go to the platform's liable balance account or a user's balance account according to split instructions at payment or capture. Adyen-assessed Processing fees are totaled daily and booked to the liable balance account; other fees and volume adjustments are assessed at monthly invoicing, with the overall adjustment booked to the liable balance account. These are distinct grains and booking moments. [Raw: lines 21–25]
- For full fee reconciliation, the page points to the Payment accounting report's event-level fee lines, including per-transaction fees confirmed at `SentForSettle` and Processing fees accumulated for instructions received on the same date. The later `Settled` event and Payable Batch help explain timing of the daily Processing fee booking. The example's EUR 100 payment uses PSP reference `F2FTV3THPB9Z2C33` and merchant reference `UUID1`; those values are illustrative. [Raw: lines 29–31, 36–54, 86]
- The Settlement detail report example shows the aggregate daily Processing fee as `Type` `Fee`, and gives Creation Date, Modification Reference and Batch Number to align the aggregate with a balance-platform booking. It also records monthly adjustments as `InvoiceDeduction`. Its `Settled` line repeats transaction fee information already in Payment accounting, so summing both without accounting for that overlap would double-count. [Raw: lines 88–107]
- In the Balance Platform Accounting Report example, Platform Payment fee columns show per-transaction charges on a dedicated fee balance account. The total daily Processing fee is instead booked to the default liable BalanceAccount as `Type` `fee`, daily in arrears; inspect the PSP Modification Merchant Reference. The sample has distinct Booking Date and Value Date columns and status rows, so match report event, account, reference, currency and dates before treating a row as a booked fee. [Raw: lines 109–132]
- The report snippets show selected columns and rows for illustration. The guide and its example do not establish that a particular platform's reports were complete, that reconciliation executed, that a fee was owed by a specific user, that a payment finally settled, or that bank funds arrived. [Raw: line 42; example tables, lines 56–132]

## Detail locators

- Fee assessment and report roles: raw lines 19–32.
- Example identity and Payment accounting lifecycle, Processing fees and Payable Batch: raw lines 34–86.
- Settlement detail `Fee` / `InvoiceDeduction` rows, Creation Date, Modification Reference and Batch Number: raw lines 88–107.
- Balance Platform Accounting fee columns, account allocation, status rows, Booking Date and Value Date: raw lines 109–132.

## Related

- [[adyen-reporting]] — provider reporting and reconciliation evidence
- [[adyen-platforms]] — balance-platform account context
- [Reconciliation use cases](https://docs.adyen.com/platforms/reconciliation-use-cases) — parent guide
- [Balance Platform Accounting Report](https://docs.adyen.com/platforms/reports-and-fees/balance-platform-accounting-report) — linked report reference
- [Payment accounting report](https://docs.adyen.com/reporting/invoice-reconciliation/payment-accounting-report) — linked report reference
- [Settlement detail report](https://docs.adyen.com/reporting/settlement-detail-report) — linked report reference

## Raw Sources

- [[raw/adyen/docs/platforms/reconciliation-use-cases/reconcile-fees/2026-09-15|Adyen Platforms reconcile fees — collected 2026-09-15]]

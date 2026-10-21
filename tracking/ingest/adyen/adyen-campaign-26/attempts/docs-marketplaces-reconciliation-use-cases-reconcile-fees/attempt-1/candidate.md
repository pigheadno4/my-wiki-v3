---
title: "Reconcile fees | Adyen Marketplaces"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reconciliation-use-cases/reconcile-fees"
raw_files:
  - "adyen/docs/marketplaces/reconciliation-use-cases/reconcile-fees/2026-09-15.md"
tags: [adyen, marketplaces, platforms, reconciliation, fees, reports]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplace-path [[adyen-reporting]] worked example reconciles fee assessments and balance-platform bookings across the Payment accounting report, Settlement detail report and Balance Platform Accounting Report. It concerns the newer balance-platform account model: a platform liable balance account and, according to payment/capture split instructions, a user's balance account. It does not describe Classic Platforms accounts or prove that a particular platform's reports reconcile.

## Key takeaways

- Per-transaction Interchange, Scheme fees, Markup and Commission are deducted when captured payment funds are booked to balance accounts. The fee is deducted from the platform liable balance account or booked to a user's balance account according to split instructions given at payment or capture. Adyen Processing fees are assessed as a daily total and booked to the liable account; other fees and volume adjustments are assessed monthly, with the overall invoicing adjustment booked to that account (raw **Reconcile fees**, lines 19–25). These are different fee grains and booking times.
- For event-level fees, the Payment accounting report confirms per-transaction fees at `SentForSettle`; received payment instructions accumulate Processing fees through the day. The later `Settled` event and `Payable Batch` help explain timing of the daily aggregate Processing-fee booking. The EUR 100/PSP-reference example is illustrative and its snippets show only selected rows/columns (raw **Payment accounting report**, lines 34–54, 56–86).
- The Settlement detail report shows the aggregate daily Processing charge as `Type: Fee`, with Creation Date, Modification Reference and Batch Number for matching to the liable-account booking. It also shows monthly adjustments as `InvoiceDeduction`. The payment's `Settled` line repeats per-transaction fee information already represented in the Payment accounting report; adding both as distinct fees would double-count the example (raw **Settlement detail report**, lines 88–107).
- In the Balance Platform Accounting Report example, per-transaction fee columns point to a dedicated fees balance account, while the total daily Processing fees are booked to the default liable balance account as `Type: fee`, daily in arrears. Its example shows distinct Booking Date and Value Date and received/authorised/final fee rows; align account, references, amount/currency, status and dates before claiming a booking. A sample row is not proof of actual settlement or bank receipt (raw **Balance Platform Accounting Report**, lines 109–132).

## Detail locators

- Fee assessment cadence and each report's role: raw lines 19–32.
- Example payment identity, Payment accounting lifecycle, CET TimeZone, Processing fee line and Payable Batch: raw lines 34–86.
- Settlement detail aggregate `Fee`, later `BalancePlatformTransfer`, monthly `InvoiceDeduction` statement and batch/reference fields: raw lines 88–107.
- Balance Platform Accounting Report fee columns, user/liable accounts, signed fees, status rows, booking/value dates and PSP modification reference: raw lines 109–132.

## Related

- [[adyen-reporting]] — report routes, grain and evidence boundary.
- [[adyen-platforms]] — balance-platform account context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/marketplaces/reconciliation-use-cases/reconcile-fees/2026-09-15|Reconcile fees, captured 2026-09-15]]

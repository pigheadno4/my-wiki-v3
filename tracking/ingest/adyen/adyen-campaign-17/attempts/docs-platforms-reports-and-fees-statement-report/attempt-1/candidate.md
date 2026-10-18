---
title: "Adyen Balance Platform Statement Report"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reports-and-fees/statement-report"
raw_files:
  - "adyen/docs/platforms/reports-and-fees/statement-report/2026-09-15.md"
tags: [adyen, platforms, reporting, balance-accounts, reconciliation]
---

## Overview

The Balance Platform Statement Report is a daily Adyen for Platforms report showing starting balance, balance-changing transactions and ending balance by available currency for included balance accounts. The page positions it as an alternative for tracking daily balance changes to the Balance Platform Accounting Report and as a route to transactions included in scheduled and on-demand payouts. Crucially, a balance account with both opening and ending balance zero is omitted, so absence from this report alone cannot establish that no intraday activity occurred. [[adyen]] [[adyen-platforms]] [[adyen-reporting]]

## Key takeaways

- **Generation and scope:** Customer Area can generate this report automatically on a schedule or manually for a specific day. The linked sample CSV is illustrative; an account-generated report may include more data or columns based on balance-platform settings. The page does not state a report cutoff time, service role or retention period.
- **Identifiers and event grain:** columns distinguish Account Holder and Balance Account IDs, Category/Type/Status, Transfer Id for a pending debit or credit, and Transaction Id for a completed debit or credit. PSP payment and modification merchant/PSP references are separate fields. The page's Reference and Description rows both call their content an identifier of a pending debit/credit; do not infer a unique join rule from that repeated wording alone.
- **Amounts and dates:** `Amount` is listed as the amount of a transfer or transaction with data type Alpha text; separate starting/ending balance values and currencies define the daily balance frame. Booking Date is the booking time, while Value Date is when funds are available, each with its own time-zone column. The page does not define sign semantics for Amount or a numeric parsing contract; consult actual report data and the Accounting Report before interpreting debits and credits.
- **Payout and proof boundary:** the report can help track transactions included in scheduled and on-demand payouts. It does not present a bank-credit status, payout-return field, successful payout example or beneficiary statement. A balance change or completed Transaction Id does not by itself prove a beneficiary bank received funds.

## Detail locators

- Raw lines 15–32: daily report purpose, zero-opening/ending omission, payout-tracking use, generation routes and sample variability.
- Raw lines 34–58: account identifiers, Category/Type/Status, pending Transfer Id, completed Transaction Id and payment/modification references.
- Raw lines 59–68: booking versus value date, currency and Amount, separate starting/ending balance fields.
- Raw lines 69–78: reserved future columns without current defined behavior.

## Related

- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — detailed balance-event and accounting fields.
- [[source-adyen-docs-platforms-reports-and-fees-payout-report]] — scheduled-payout report and rolling balance.
- [[source-adyen-docs-platforms-custom-payouts-on-demand-payouts]] — on-demand payout request and status route.

## Raw Sources

- [[raw/adyen/docs/platforms/reports-and-fees/statement-report/2026-09-15|Balance Platform Statement Report snapshot, fetched 2026-09-15]]

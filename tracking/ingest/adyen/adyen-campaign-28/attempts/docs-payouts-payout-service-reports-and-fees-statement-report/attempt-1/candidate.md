---
title: "Adyen Payout Service Balance Platform Statement report"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/reports-and-fees/statement-report"
raw_files:
  - "adyen/docs/payouts/payout-service/reports-and-fees/statement-report/2026-09-15.md"
tags: [adyen, payout-service, reporting, statement-report, balance-accounts]
---

## Overview

This Payout Service-path report reference (modified and captured 2026-09-15) describes a **daily Balance Platform Statement Report** with starting balance, transactions that changed the balance and ending balance for available currencies. It is offered as an alternative to the Balance Platform Accounting Report for within-day balance changes and as a route for tracking internal funds transfers. The page states that a balance account with **both opening and ending balance zero is omitted**; therefore its “all transactions” description cannot be read as a guarantee that every zero-to-zero account's activity appears. See [[adyen]] and [[adyen-reporting]].

## Key takeaways

- **Generation and grain:** Customer Area can generate this Statement Report automatically on a schedule or manually for a specific day. Rows expose Balance Platform, Account Holder and Balance Account identifiers, category/type/status, amount/currency and starting/ending balance fields. The raw does not specify a universal one-row-per-transfer or one-row-per-transaction rule, so use the report fields and actual file to establish grain. A downloaded sample is illustrative; account settings may add columns or data.
- **Pending versus completed IDs:** The table describes **Transfer Id** as identifying a pending debit/credit and **Transaction Id** as identifying a completed debit/credit. Treat these as separate identifiers, not interchangeable joins. It also gives PSP payment/modification merchant and PSP references. The table labels both `Reference` and `Description` as a unique identifier of a pending debit or credit; preserve that wording as a table ambiguity rather than assigning new semantics.
- **Dates, timezone and amount:** The report has Booking Date and its time-zone column, Value Date and its time-zone column, three-character currency codes, and `Amount` typed **Alpha text**. Starting/ending balances are likewise typed Alpha text with their currency columns. This page does not define an amount sign rule, minor-unit conversion, report cutoff timezone or beneficiary-bank receipt. Consult the actual export and more specific reconciliation guides for those.
- **Scope limits:** Categories include bank, card, grants, internal, issuedCard, platformPayment, topUp and upgrade; the values do not alone prove a payout or settlement lifecycle. The report is balance-account ledger evidence at its described daily scope, not proof of final transfer receipt by a third-party bank.

## Detail locators

- Purpose, zero-to-zero omission, Accounting Report alternative and scheduled/manual generation: pinned raw lines 15-32.
- Platform/holder/account, category/type/status, Transfer/Transaction IDs and PSP references: pinned raw lines 34-58.
- Booking/Value dates and time zones, currency/amount/start/end balances, reserved future columns: pinned raw lines 59-78.

## Related

- [[adyen-reporting]] — main reporting concept and reciprocal source route.
- [[adyen-payouts]] — Payout Service product context.
- [[source-adyen-docs-payouts-payout-service-reports-and-fees-balance-platform-accounting-report]] — separate accounting-report grain and event definitions.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/reports-and-fees/statement-report/2026-09-15|Payout Service Balance Platform Statement report, captured 2026-09-15]]

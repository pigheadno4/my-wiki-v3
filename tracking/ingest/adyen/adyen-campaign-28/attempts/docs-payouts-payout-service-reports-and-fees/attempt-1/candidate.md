---
title: "Payout Service reports and fees overview"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/reports-and-fees"
raw_files:
  - "adyen/docs/payouts/payout-service/reports-and-fees/2026-09-15.md"
tags: [adyen, payouts, payout-service, reporting, reconciliation, fees]
---

## Overview

This 2026-09-15-captured [[adyen]] Payout Service overview maps **Adyen account** and **balance platform** reports to enterprise-payout reconciliation and fee analysis. It says complete monthly financial reconciliation uses a combination of the two report families, while narrower tasks may use one report. The map is not a completed reconciliation, invoice approval, bank deposit or payout receipt. See [[adyen-reporting]] and [[adyen-payouts]] (raw lines 15–28).

## Key takeaways

- On the **Adyen account** side, the Payment accounting report is **optional** for full reconciliation and supplies payment lifecycle/per-event processing-cost detail, but **excludes balance-platform transaction charges** for payouts, transfers and KYC. The **required** Settlement details report carries payment funds, per-transaction costs, invoice-origin adjustments and optional tracking of one-off inbound wire deposits. The **required** Monthly invoice totals preceding-month assessed fees and adjustments. These are separate grains, not interchangeable sources (raw lines 30–38).
- On the **balance-platform** side, the Balance Platform Accounting Report is **optional** for full reconciliation and tracks balance-changing transfer lifecycle events/statuses and webhook corroboration. The **required** Balance Platform Statement Report supplies daily opening/closing balances for accounts that changed that day, influencing events and transactions in scheduled/on-demand payouts. A received/authorised/booked report row is not itself beneficiary-bank receipt (raw lines 40–47).
- The page says Adyen deducts fees from settlement and by default debits them from the account. Monthly fee reconciliation needs different grains: transaction-level calculated fee breakdown in Balance Platform Accounting, monthly fee/adjustment totals in the invoice, and aggregate processing-fee/invoice-adjustment lines in Settlement details. A fee appearing in one report does not by itself prove its invoice total or settlement debit (raw lines 49–59).
- The fee matrix lists processing interchange, scheme, markup and blended commission per transaction when Adyen is PSP; US-only Visa FanF by period and Mastercard Merchant Location Fee by store; and per-instruction Fund Transfer Service and Payout Service plus per-sub-merchant KYC service fees on the monthly invoice. It gives categories/assessment bases and report locations, **not rates or a merchant-specific bill** (raw lines 61–73).

## Detail locators

- Scope, scheduled/manual generation and full-month report combination: raw lines 19–28.
- Adyen-account report purposes and required/optional labels: raw lines 30–38.
- Balance-platform report purposes and required/optional labels: raw lines 40–47.
- Fee deduction, reconciliation grain and fee matrix: raw lines 49–73.

## Related

- [[source-adyen-docs-payouts-payout-service-reports-and-fees-balance-platform-accounting-report]]
- [[source-adyen-docs-payouts-payout-service-reports-and-fees-statement-report]]
- [[source-adyen-docs-payouts-payout-service-reconcile-balances]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/reports-and-fees/2026-09-15|Pinned Payout Service reports-and-fees overview]]

---
title: "Adyen Payout Service — Reconcile fund transfers"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/reconciliation-use-cases/reconcile-transfers"
raw_files:
  - "adyen/docs/payouts/payout-service/reconciliation-use-cases/reconcile-transfers/2026-09-15.md"
tags: [adyen, payouts, payout-service, reconciliation, transfers, reporting]
---

## Overview

This 2026-09-15 [[adyen]] Payout Service guide describes how to track payouts and internal transfers to or from a payout account. It routes transfer-lifecycle tracking and transaction-webhook verification to the Balance Platform Accounting Report or Balance Platform Statement Report. See [[adyen-reporting]] for the reporting context.

## Key takeaways

- To reconcile transfers, combine transaction webhooks with either named report using the **transaction PSP reference**, **Status**, and **Amount**. This is a matching method; the page does not supply a worked join, amount-sign convention, time-window rule, or proof that a particular webhook was processed.
- Identify internal fund transfers by `category=internal` and `type=internalTransfer`; third-party bank payouts by `category=bank` and `type=bankTransfer`; and third-party card payouts by `category=card` and `type=cardTransfer`. These are distinct transfer types in the Payout Service account context.
- A matched webhook/report entry supports the documented reconciliation check. This short guide does not establish final settlement or beneficiary bank/card receipt; use the underlying transfer lifecycle and transaction/report evidence for the specific case.

## Detail locators

- Purpose and two tracking steps: pinned raw lines 15–22.
- Reconciliation match fields and named reports: pinned raw line 24.
- Transfer category/type lookup table: pinned raw lines 26–32.

## Related

- [[source-adyen-docs-payouts-payout-service-reports-and-fees-balance-platform-accounting-report]] — report field and event reference.
- [[source-adyen-docs-payouts-payout-service-reports-and-fees-statement-report]] — statement balance and transaction reference.
- [[source-adyen-docs-payouts-payout-service-transfer-transactions-transaction-webhooks]] — transaction webhook lifecycle context.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/reconciliation-use-cases/reconcile-transfers/2026-09-15|Adyen Docs snapshot: Reconcile fund transfers (2026-09-15)]]

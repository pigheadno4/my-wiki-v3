---
title: "Adyen Payout Service balance-position spot checks"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/reconciliation-use-cases/verify-balances"
raw_files:
  - "adyen/docs/payouts/payout-service/reconciliation-use-cases/verify-balances/2026-09-15.md"
tags: [adyen, payout-service, reconciliation, balance-report, balance-accounts]
---

## Overview

This Payout Service-path guide (modified and captured 2026-09-15) explains **spot-checking balance-account positions** before on-demand payouts to a user's third-party bank account or card. It routes operators to a dated Balance Platform Balance Report and separately mentions a real-time Configuration API lookup for a payout account's balance. The page does **not** state a reconciliation formula, pending-versus-booked transaction rule, universal report cutoff time zone or proof that any payout reached a beneficiary. See [[adyen]] and [[adyen-reporting]].

## Key takeaways

- **Daily report grain:** The guide says the Balance Platform Balance Report shows opening and closing balances for a **given day**, across account holders, balance accounts and balance-account currencies. The illustrated June 8, 2022 report has three rows: USD and CAD for one balance account and USD for another. Its opening timestamps are June 8 00:00 CEST and closing timestamps June 9 00:00 CEST. Those dates and zone describe the sample, not a guaranteed timezone configuration for every generated report.
- **How to inspect:** The documented report route is to obtain a Balance Platform Balance Report for a specific date and filter it to the needed account/currency. Separately, `GET /balanceAccounts/{id}` in the Configuration API is described as a real-time payout-account balance lookup. A daily opening/closing snapshot is not equivalent to that real-time balance or to a verified available-for-payout amount at a later instant.
- **Evidence boundary:** The worked table contains example balances, not an accounting roll-forward from detailed transactions. This page links to the Accounting Report but does not define a pending/booked formula or reconcile individual debit/credit events. It does not establish actual bank/card payout initiation, booking or recipient receipt.

## Detail locators

- Purpose and payout-availability motivation: pinned raw lines 15-21.
- Daily Balance Report scope, report retrieval/filtering and real-time Configuration API route: pinned raw lines 23-34.
- Three-row account/currency sample and its opening/closing dates/timezone: pinned raw lines 36-44.
- Accounting/report links only, without formula: pinned raw lines 46-49.

## Related

- [[adyen-reporting]] — main report/reconciliation concept and reciprocal source route.
- [[adyen-payouts]] — payout context.
- [[source-adyen-docs-payouts-payout-service-reports-and-fees-balance-platform-accounting-report]] — separate Accounting Report field and event reference.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/reconciliation-use-cases/verify-balances/2026-09-15|Payout Service balance verification guide, captured 2026-09-15]]

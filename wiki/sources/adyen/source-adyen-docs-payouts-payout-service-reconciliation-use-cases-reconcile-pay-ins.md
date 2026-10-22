---
title: "Adyen Payout Service: reconcile pay ins"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/reconciliation-use-cases/reconcile-pay-ins"
raw_files:
  - "adyen/docs/payouts/payout-service/reconciliation-use-cases/reconcile-pay-ins/2026-09-15.md"
tags: [adyen, payout-service, reporting, reconciliation, pay-ins]
---

## Overview

This 2026-09-15-captured [[adyen]] Payout Service guide explains how to use [[adyen-reporting]] to reconcile individual PSP transactions with aggregate settlement pay-ins to a balance account, and to identify top-ups in that report flow. It describes report matching, not a beneficiary-bank receipt or an executed reconciliation for a particular merchant. See the full pinned raw for the field values and report links (lines 19–50).

## Key takeaways

- The guide uses the Settlement Details Report together with either the Balance Platform Statement Report or Balance Platform Accounting Report (lines 23–27).
- For merchants using a balance platform strictly as a pass-through transfer mechanism, filter the balance-platform report by Category `platformPayment`, Type `balanceAdjustment`, and Status `booked`. Its Reference and Description fields contain JSON with merchant account, currency and settlement batch number (lines 29–41).
- Match the corresponding merchant account and batch in the Settlement Details Report, then filter its Type to `BalancePlatformTransfer` and by Currency (lines 43–49). This is a batch-level join between PSP detail and aggregate balance-platform pay-in, not a one-to-one match of every PSP event to a separate balance-account transfer.
- The Settlement Details Report can contain `reserveAdjustment` top-ups and/or individual `capture`, `refund`, `chargeback` and other transactions. Their gross amounts, fees and net amounts add up to the `BalancePlatformTransfer` amount (line 50). The page gives no sign convention or time-zone reconciliation rule; inspect the actual report columns and related report guides before assigning debit/credit direction or period boundaries. A `reserveAdjustment` report entry here does not by itself establish a recurring direct-debit top-up.

## Detail locators

- Report set and scope: raw lines 19–27.
- Pass-through balance-platform filters and batch identifiers: raw lines 29–41.
- Settlement Details match, currency filter and component amounts: raw lines 43–50.

## Related

- [[adyen]]
- [[adyen-reporting]]
- [[source-adyen-docs-payouts-payout-service-reports-and-fees]]
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/reconciliation-use-cases/reconcile-pay-ins/2026-09-15|Full pinned Adyen reconciliation guide]]
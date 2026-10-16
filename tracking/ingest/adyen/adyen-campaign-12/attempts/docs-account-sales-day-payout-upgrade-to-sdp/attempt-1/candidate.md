---
title: "Upgrade to Sales day payout | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/sales-day-payout/upgrade-to-sdp"
raw_files:
  - "adyen/docs/account/sales-day-payout/upgrade-to-sdp/2026-09-15.md"
tags: [adyen, sales-day-payout, merchant-settlement, reconciliation, payable-batch]
---

## Overview

This 2026-09-15 [[adyen]] Docs snapshot explains how moving a merchant from Pass-through payout to Sales day payout changes **merchant payable-batch booking** and the Settlement Details Report, Payment Accounting Report, Customer Area status and webhook picture. It concerns Adyen's ordinary payout of merchant sales funds, not the legacy Payout API for sending money to another recipient. [[adyen-sales-day-payout]] [[adyen-reporting]]

## Key takeaways

- Under Pass-through payout, funds enter a payable batch when the card scheme or payment method settles, so one sales day's transactions can span batches. Under Sales day payout, Adyen groups a sales day's transactions in one payable batch and pays it after a **fixed payout delay**, potentially booking funds to the merchant batch before Adyen receives them from the scheme or method. This guide does not give the delay length, cutoff, time zone, region, fees or eligibility rules. See raw lines 15–23.
- The Sales day payout Settlement Details Report adds `CaptureFailed` (debit), `RefundFailed` (credit), `SettledReversed` (debit after 30 days without funds), and `RefundNotCleared` (credit after 30 days without refund clearing). They adjust earlier `Settled` or `Refunded` entries, rather than representing new payments or refunds. A late clearing can produce a subsequent `Settled` or `Refunded` booking. See raw lines 25–40.
- The capture and refund flow tables map each scenario separately across SDR entry, PAR record type, Customer Area status and webhook. A reversal before the **value date** may appear in PAR/status but leave no SDR entry; after the value date, the SDR records an adjustment. A 30-day reversal is shown without its own webhook, while a later settlement or definitive failure has its own mapped route. Do not equate a PAR record, Customer Area status or webhook with bank payout arrival. See raw lines 42–94.
- The raw refund table contains internal inconsistencies: the failure-before/after-value-date prose calls the reversal a debit while the after-date SDR cell says `RefundFailed` credit; the before-date PAR cell says `CaptureFailed` under a refund scenario; the definitive-failure row says funds were already debited after showing a credit reversal. Use the exact scenario rows rather than silently resolving those conflicts. See raw lines 79–91.
- The refund footnote says a `REFUND` webhook reflects processing of the request for a captured payment and gives no insight into successful acceptance by the external payment method. See raw line 94.

## Detail locators

- **Payout-model comparison:** raw lines 15–23.
- **Four additional journal types and 30-day adjustments:** raw lines 25–40.
- **Capture mapping by value date and 30-day outcome:** raw lines 42–71.
- **Refund mapping, conflicting wording and webhook qualification:** raw lines 73–94.

## Related

- [[adyen]]
- [[adyen-sales-day-payout]]
- [[adyen-reporting]]
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — SDR field and journal reference
- [[source-adyen-docs-reporting-invoice-reconciliation-payment-accounting-report]] — PAR reference

## Raw Sources

- [[raw/adyen/docs/account/sales-day-payout/upgrade-to-sdp/2026-09-15|Upgrade to Sales day payout — collected 2026-09-15]]

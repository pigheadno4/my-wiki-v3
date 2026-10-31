---
title: "Adyen Sales Day Payout"
type: concept
category: technology
tags: [adyen, sales-day-payout, merchant-settlement, payable-batch, reconciliation]
---

## Definition

Sales day payout is Adyen's merchant-settlement model that groups transactions from one sales day into a payable batch and pays that batch after a fixed delay, even when a card scheme or payment method has not yet settled those funds to Adyen. Pass-through payout instead books funds to the merchant payable batch when the scheme or method settles, which can spread one sales day across multiple batches. This is a merchant-sales payout model, distinct from the legacy Payout API for paying another recipient. [[source-adyen-docs-account-sales-day-payout-upgrade-to-sdp]]

## Reconciliation boundary

The upgrade guide adds four Settlement Details Report adjustment journal types for failed capture, failed refund, delayed scheme settlement and uncleared refund. Such entries adjust earlier `Settled` or `Refunded` bookings; report and Customer Area states must be read at their own grain and do not alone prove bank-deposit arrival. The captured guide supplies no specific payout delay, cutoff, time zone, region, fee or eligibility rule. Its refund flow table has conflicting debit/credit and record-type wording, so use the source's row-level locators for those cases.

## Sources

- [[source-adyen-api-explorer-webhooks-latest-post-settled-reversed]] — 2026-09-15-captured SETTLED_REVERSED webhook reference for debit reversal of settled capture after 30-day scheme/method nonreceipt, scoped to enabled Sales Day Payout merchants.


- [[source-adyen-docs-account-pass-through-payout]] — 2020-modified, 2026-09-15-captured Adyen guide to pass-through merchant settlement: scheme/method receipt assigns sales to payable batches, one sales day can span batches, adjustments join as they occur and currency-specific bank holidays delay timing; batch assignment is not bank receipt.


- [[source-adyen-docs-account-getting-paid]] — 2020-modified, 2026-09-15-captured Adyen merchant-account getting-paid guide to sales-day/pass-through payable batches, net deductions, currency and bank-holiday qualifications, distinct payout-view/change roles, and bank-arrival limits; payout instruction is not bank receipt.


- [[source-adyen-docs-account-sales-day-payout]] — 2026-09-15 Adyen Sales day payout model guide: local-time-zone sales-day cutoff, delay to payable-batch assignment, regional and method-mix limits, adjustments, two-hour batch close, bank instruction, and holiday effects; it does not prove bank receipt.


- [[source-adyen-docs-account-sales-day-payout-upgrade-to-sdp]] — 2026-09-15 Adyen Docs snapshot of the Pass-through-to-Sales-day model change, additional SDR journals and capture/refund reconciliation flows.

## Related

- [[adyen]]
- [[adyen-reporting]]

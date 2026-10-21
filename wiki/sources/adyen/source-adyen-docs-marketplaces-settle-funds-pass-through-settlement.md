---
title: "Adyen Marketplace pass-through settlement"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/settle-funds/pass-through-settlement"
raw_files:
  - "adyen/docs/marketplaces/settle-funds/pass-through-settlement/2026-09-15.md"
tags: [adyen, marketplaces, platforms, settlement, deprecated]
---

## Overview

This 2020-modified Marketplace guide, captured 2026-09-15, describes **pass-through settlement**: payment proceeds reach settlement batches when schemes or payment methods send funds to Adyen, so one sales day's payments can settle across multiple business days and each batch can mix sales days. The page explicitly says this model is **deprecated and unavailable to new integrations after July 1, 2025**. It is a balance-account settlement model, not proof of an external payout or bank receipt. [[adyen]] [[adyen-platforms]]

## Key takeaways

- Scheme/payment-method funding timing determines when sales enter a settlement batch; after a batch closes, Adyen says it settles those funds on the next business day. Its daily-frequency illustration spreads one Monday sales day across January 2–7 and mixes sales days in a settlement. Treat those dates as an illustration, not a fixed settlement schedule for a payment (raw lines 19–31).
- Refunds, chargebacks and other adjustments are added or subtracted before settlement when they occur, potentially on a different date from the sale. Available funds settle on working days Monday–Friday, excluding bank holidays; a capture-day bank holiday extends the delay (raw lines 33–39).
- This model does not support reconciliation by sales-day totals. To reconcile individual payments, track them in Balance Platform Accounting Reports, rather than treating batch day or payout date as a sales-day total (raw lines 21–23).
- The page says pass-through is enabled by default on a balance account and documents a Configuration API PATCH `/balanceAccounts/{id}` to revert an existing account from sales-day settlement: `platformPaymentConfiguration.salesDayClosingTime: "00:00"` with `settlementDelayDays: null`. The TEST curl uses `/bcl/v2`; the returned balance account shows the closing time without a settlement-delay field. Its parameter table states an integer `settlementDelayDays` enables sales-day settlement and closing time allows 00:00–07:00 on the hour. This dated configuration example does **not** override the explicit post–July 1, 2025 new-integration deprecation or establish live eligibility for an account (raw lines 41–62, 278–305).
- A configured balance account, a received scheme batch or the illustrative next-business-day settlement statement does not itself demonstrate a particular payment settled, available balance, user payout or bank receipt. Use payment-level accounting and the separate payout evidence for those outcomes (raw lines 21–39, 278–305).

## Detail locators

- Deprecation, scheme/method timing, batch composition, adjustments, working-day timing and payment-level reconciliation: raw lines 17–39.
- Existing-account revert PATCH and versioned TEST/SDK examples: lines 41–276. Response, closing-time and settlement-delay fields: lines 278–305.

## Related

- [[adyen]] — provider.
- [[adyen-platforms]] — modern platform/Marketplace settlement context.
- [[source-adyen-docs-platforms-settle-funds-pass-through-settlement]] — separate Platforms-path guide.
- [[source-adyen-docs-platforms-settle-funds]] — sales-day settlement alternative.
- [[adyen-classic-platforms]] — distinct legacy integration.

## Raw Sources

- [[raw/adyen/docs/marketplaces/settle-funds/pass-through-settlement/2026-09-15|Marketplace pass-through settlement — 2026-09-15 snapshot]]

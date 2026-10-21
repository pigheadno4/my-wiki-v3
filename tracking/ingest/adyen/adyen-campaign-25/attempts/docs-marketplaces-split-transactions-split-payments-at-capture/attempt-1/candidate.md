---
title: "Adyen Marketplace split payments at capture"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/split-transactions/split-payments-at-capture"
raw_files:
  - "adyen/docs/marketplaces/split-transactions/split-payments-at-capture/2026-09-15.md"
tags: [adyen, marketplaces, platforms, split-payments, capture]
---

## Overview

This 2023-modified Marketplace-path guide, captured 2026-09-15, explains how a marketplace using [[adyen]] can supply or change split instructions when capturing a payment on behalf of users. It belongs under [[adyen-platforms]]: the user balance account, marketplace liable balance account, payment authorization, capture, balance booking and eventual payout are separate roles or stages (raw lines 19–25, 51–80, 593–666).

## Key takeaways

- The guide requires Checkout API credentials, a server that accepts standard webhooks with transfer or transaction webhook subscription, and manual capture enabled or a capture delay; capture-time splitting works only for payment methods supporting separate captures (raw lines 27–45). The marketplace posts to `/payments/{paymentPspReference}/captures` using the authorization `pspReference`, with a `splits` array. The capture request has a different `pspReference` (lines 51–59, 593–599).
- Capture-time instructions can override payment-request splits, but the guide recommends payment-time instructions because methods without delayed capture might otherwise book incorrectly. If the capture amount differs from authorization, splits **must** be present in the capture request; without them all funds go to the marketplace's liable balance account. `Surcharge` and `Tip` are unsupported in capture-time splits (lines 25, 39–49, 1674–1678).
- `BalanceAccount` directs sale value to the named user's balance account; `Commission` books the marketplace's commission to its liable account; `PaymentFee` can charge a specified balance account. The table also describes `Remainder`, `TopUp` and other fee types; `amount.currency` is required for conversion, `reference` for `BalanceAccount`, and `TopUp` is unsupported in a `/sessions` request. The USD 80 example allocates USD 76 sale and USD 4 commission, with transaction fees charged to a user account; these are illustrative values, not a default allocation (raw lines 61–122).
- A capture response with `status: received` does not establish capture or booking. Listen for the `CAPTURE` outcome and the per-split transfer and transaction webhooks to distinguish received, authorised, captured and booked balance movements (raw lines 593–666, 674–990, 991–1640). The guide's test samples distinguish payment PSP reference from capture modification PSP reference.
- The API validates split format but **not** the destination balance accounts. A nonexistent destination or one attached to a closed account holder can cause the full transaction **and fees** to book to the marketplace's liable balance account despite a successful transaction; a later internal fund transfer is the documented correction route (raw lines 646–650). Split references aid reconciliation; absent references aggregate entries in reports (lines 1674–1676).

## Detail locators

- Request fields, conditional values and versioned Checkout test/library samples: raw lines 51–591; the curl URL uses Checkout test v72, while individual language snippets specify separate library versions. Their credentials, IDs and amounts are examples.
- Capture receipt and target-account failure: raw lines 593–650. Transfer/transaction webhook stages for sale, fee and commission legs: lines 652–1640.
- Additional fee splitting, FX remainder, chargeback, top-up and reporting-reference routes: raw lines 1641–1678.

## Evidence boundary

The snapshot is a Marketplace guide within the modern Platforms model, not Classic Platforms or a proof of a specific marketplace's seller, merchant of record, fund ownership, capture, settlement, payout or bank receipt. The examples have internal inconsistencies: the narrative charges fees to the user's sale account, while the fee webhook uses a second user balance account (lines 74–79, 1006–1034); the NodeJS example uses EUR where the narrative and other examples use USD (lines 74–79, 331–338); the commission transaction sample shows a negative amount and user account IDs despite describing a credit to the marketplace liable account (lines 1594–1638). Treat these sample payloads as illustrative and use actual webhook/report evidence for a real ledger.

## Related

- [[adyen-platforms]] — modern platform and Marketplace route.
- [[adyen-payment-capture]] — authorization and capture outcome boundary.
- [[adyen-platform-internal-transfers]] — corrective transfer route.

## Raw Sources

- [[raw/adyen/docs/marketplaces/split-transactions/split-payments-at-capture/2026-09-15|Pinned Marketplace capture-time split guide, captured 2026-09-15]]

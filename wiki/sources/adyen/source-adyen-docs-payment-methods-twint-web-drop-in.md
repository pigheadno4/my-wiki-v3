---
title: "TWINT Web Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/twint/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/twint/web-drop-in/2026-09-15.md"
tags: [adyen, twint, web, drop-in, tokenization, capture]
---

## Overview

This Adyen TWINT Web Drop-in add-on documents separate Sessions and Advanced server-side flows for an existing integration. In both, the merchant adds TWINT in Customer Area and handles a `redirect` action. The Sessions requirement explicitly says Checkout API v68 or later; the Advanced requirements list does not state that minimum. The page's ordinary-payment sections say no extra TWINT parameters for `/sessions` or `/payments`, while later sections give separate token-payment and capture instructions (raw lines 17–42, 105–133, 184–250).

## Key takeaways

- Each flow allows an *optional* individual `Twint` import with `AdyenCheckout` and `Dropin` for tree shaking; this is a performance choice, not a TWINT-specific ordinary-payment field or mandatory import (raw lines 44–54, 117–127).
- Both recurring sections say to create a shopper token with `storePaymentMethod: true` and a `shopperReference` of at least three characters in `/payments`. When details are stored, a `recurring.token.created` lifecycle webhook supplies `storedPaymentMethodId`, `eventId` (initial payment PSP reference) and `shopperReference`; the server must receive that webhook. For later token payments, the guide lists the stored ID, same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. The guide does not spell out a shopper-consent procedure (raw lines 56–95, 135–174, 213–250).
- Both flow sections say a live Customer Area request for TWINT is needed before live acceptance; test status can be checked in the test Customer Area (raw lines 97–103, 176–182).
- The later capture section says TWINT is captured automatically by default when Capture Delay is `Immediate` or `1–7 days`; with `Manual` delay, the merchant must capture before the seven-day authorization expiry. It permits a single partial capture but not multiple partial captures, and says any unclaimed remainder is automatically cancelled (raw lines 184–211).
- The partial-capture prose calls the request field `modificationAmount` for `/payments/{paymentPspReference}/captures`, yet the adjacent JSON example uses `amount` and is labeled `/capture request`. Treat that as an unresolved field/endpoint example mismatch; do not copy the sample as an authoritative schema. The example's CHF and amount are illustrative and do not establish broader eligibility (raw lines 190–209).

## Detail locators

- Sessions prerequisites, v68 minimum, redirect and ordinary `/sessions` scope: raw lines 25–42.
- Optional imports, recurring token lifecycle and live request under Sessions: raw lines 44–103.
- Advanced prerequisites, ordinary `/payments` scope, token lifecycle and live request: raw lines 105–182.
- Capture delay, seven-day expiry, partial-capture limit, sample mismatch and cancellation: raw lines 184–211.
- Repeated Advanced recurring instructions: raw lines 213–250.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-payment-capture]]
- [[source-adyen-docs-payment-methods-twint]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/twint/web-drop-in/2026-09-15|TWINT Web Drop-in, fetched 2026-09-15]]

---
title: "Adyen PayPal Web Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypal/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypal/web-drop-in/2026-09-15.md"
tags: [adyen, paypal, web-drop-in, online-payments, wallet]
---

## Overview

This [[adyen]] PayPal guide, last modified and captured 2026-09-15, adds PayPal Smart Payment Buttons to an **existing Web Drop-in integration** (buttons from Drop-in v3.7.0) after separate PayPal setup. It distinguishes the default Drop-in v5.0.0+ `/sessions` flow from an additional-use-case `/payments` flow, then covers PayPal risk data, client configuration, payment outcome, recurring tokens, refunds and Seller Protection. See [[adyen-online-payments]]. This is an integration snapshot, not current PayPal/merchant eligibility, an actual authorization, capture, settlement, refund or recipient-funds record.

## Key takeaways

- **Server and setup scope:** the existing Drop-in and PayPal setup are prerequisites. `/sessions` is described as the v5.0.0+ default; `/payments` is the additional-use-case branch, whose examples send `paymentMethod.type: paypal` and `subtype: sdk`. The HUF section says PayPal expects rounded whole transaction and line-item amounts that add up; Adyen-side rounding can leave a mismatch that PayPal rejects. Sample USD/EUR amounts, library versions and test endpoints are examples. See raw lines 15–40, 516–570, 1041–1045.
- **Risk data is conditional:** `additionalData.paypalPairingId` is only for customer-initiated transactions using Fraudnet with the same pairing ID at Fraudnet and Adyen. PayPal risk fields apply to marketplaces and some verticals according to PayPal's instructions, and are sent as a stringified `additional_data` array; the marketplace field table is illustrative and the PayPal account manager determines the applicable fields. Do not infer that every merchant must send it or that three sample fields suffice. See raw lines 42–50, 520–528, 1047–1119. The `/payments` PHP sample uses placeholder values for `paypalRisk` and `shopperReference` that differ from adjacent samples (raw lines 684–690); it is not a verified complete request.
- **Client configuration and capabilities:** the `/sessions` tab states no extra PayPal configuration; the `/payments` tab marks global `amount` and `countryCode` required, while its snippet describes `countryCode` as test-only and live-derived. The page gives a popup-policy instruction, then optional CSP nonce (v5.2.0+), button style, shipping/user-input callbacks, PayPal Credit/Pay Later controls, per-payment `intent` (v5.34.0+), and a PayPal Component Venmo-hide option when merchant and shopper are both in the US. Pay Later's listed regions/local-currency and cross-border caveats are dated capability statements, not merchant eligibility. See raw lines 1121–1274.
- **Outcome boundary:** `resultCode` is for showing the shopper current status; even `Authorised` can be followed by a risk-rule failure. Wait for `AUTHORISATION` webhooks for the order decision; `OFFER_CLOSED` is received only when enabled. `Pending`, `Received`, `Error`, `Refused` and `Cancelled` have separate shopper/order treatment. Authorization is distinct from later capture and settlement. See raw lines 1276–1313.
- **Recurring tokens:** the page strongly recommends explicit shopper permission for later recurring charges. Direct merchants need PayPal Vault permissions; marketplaces or indirect-settlement merchants are directed to Adyen Support, and token sharing across PayPal accounts requires suitable account configuration. Zero-value token creation has endpoint/version conditions: `/sessions` needs v5.3.0+; `/payments` needs either `intent: tokenize` on v5.34.0+ or global amount configuration on v5.3.0+. Without the `/payments` configuration, the page says no token is created. For a zero-value request, include `shopperEmail` and `amount.value: 0`; do not include `shopperEmail` under that instruction for non-zero requests. The page routes the actual shopper reference/token receipt to `recurring.token.created`, not merely the request submission. See raw lines 1315–1386.
- **Cancel/refund and protection:** uncaptured PayPal payments are cancelable, while captured payments use refund. For immediate-capture partial refunds the prose calls for refunded-item `lineItems`, although its parameter table does not mark that field required and says Adyen adds a dummy line item for mismatched totals. The example refund response is `received` with a **refund** PSP reference, not final refund completion. The detailed delayed-capture section requires `capturePspReference` only when later capture, multiple partial captures enabled and more than one partial capture are all true; omitting it in that case can fail. Seller Protection is described for physical goods with specified request fields and a test eligibility check, not automatic coverage. See raw lines 1388–1522.

> [!warning] Contradiction
> The partial-refund summary broadly says later-captured payments need `capturePspReference` (raw lines 1392–1395), while the detailed rule limits that requirement to the three conditions at lines 1473–1481. The immediate-capture prose says include `lineItems`, although its table leaves Required blank (lines 1397–1408). The refund illustration also changes from the preceding USD shoes/socks payment to an EUR polo-shirt refund (lines 59–84, 1412–1442); it cannot establish a valid refund of that earlier sample order. Use the applicable documented condition and actual captured payment/capture reference, and verify the request contract before acting.

The test section uses PayPal business and personal **sandbox** roles; its live section requires a live PayPal business account and says PayPal is available only when the shopper is logged in with a valid PayPal payment method. These are prerequisites, not evidence a particular merchant or shopper passed them. See raw lines 1524–1544.

## Detail locators

- Prerequisites, endpoint-specific fields and test request examples: raw lines 15–1040.
- HUF rounding, conditional Fraudnet/risk fields and stringified formatting: raw lines 1041–1119.
- Sessions/Advanced client configuration and optional button controls: raw lines 1121–1274.
- Synchronous result versus AUTHORISATION/OFFER_CLOSED webhook: raw lines 1276–1313.
- Recurring permission, zero-value token gates and token webhook: raw lines 1315–1386.
- Cancel, refund/capture conditions, illustrative responses and Seller Protection: raw lines 1388–1522.
- Sandbox and live account/shopper prerequisites: raw lines 1524–1544.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-refunds]]
- [[adyen-payment-capture]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypal/web-drop-in/2026-09-15|PayPal Web Drop-in guide — collected 2026-09-15]]

---
title: "Adyen PayPal Android Drop-in guide"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypal/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypal/android-drop-in/2026-09-15.md"
tags: [adyen, paypal, android, drop-in, online-payments, redirects]
---

## Overview

This [[adyen]] page, last modified 2021-07-26 and captured 2026-09-15, explains adding PayPal to an **existing Android Drop-in** integration. The app displays PayPal and handles the shopper redirect/return; the merchant server requests `/paymentMethods`, sends `/payments`, and submits returned details to `/payments/details`. PayPal setup is a prerequisite. This historical guide and its test examples do not establish current merchant or shopper eligibility, a completed authorization, capture, settlement or refund. See [[adyen-online-payments]].

## Key takeaways

- Drop-in uses `/paymentMethods` `countryCode`, `amount.currency` and minor-unit `amount.value` to show methods. Pass `paymentComponentData.paymentMethod` from Android to the server for `/payments`; the request table calls for `channel: Android` and a `returnUrl` from `RedirectComponent.getReturnUrl(context)`. A redirect `action` goes back to the app. The page's currency example is blank (`****`), and the server-language snippets are illustrative, not a complete verified Android request. See raw lines 21–42 and 124–678.
- For **HUF** transactions, this page says PayPal expects the transaction and line-item amounts rounded to whole amounts and their rounded totals to match; otherwise PayPal may reject a mismatch after Adyen rounds. The listed `lineItems` and `paypalRisk` are optional request topics in general, while PayPal risk information is required for marketplaces and specific verticals as determined with a PayPal account manager. `additionalData.paypalRisk` uses a stringified `additional_data` array; `paypalPairingId` applies only when using Magnes with the same ID sent to Magnes and Adyen. Do not apply the marketplace example field list universally. See raw lines 40–138.
- Several `/payments` language examples are inconsistent with their own prose: PHP puts `STATE_DATA` in `paypalRisk` and the stringified-risk placeholder in `shopperReference`; the Python `paypalRisk` literal is not validly escaped; Go labels API library v10.4.0 but imports v9. Use the raw prose and a version-matched API reference before implementation. The curl request is a Checkout test v72 example, not evidence of a live call. See raw lines 140–650.
- After redirect return, send `actionComponentData.details` from Drop-in to server `/payments/details`. Its synchronous `resultCode` is for the shopper display, not the final order outcome: even `Authorised` may later fail under post-authorisation risk rules; `Pending`/`Received` are unresolved. Wait for the `AUTHORISATION` webhook; `OFFER_CLOSED` timeout reporting is available only if that non-default event is enabled. Distinguish `Refused`, `Cancelled` and `Error` responses by the page's separate actions. See raw lines 679–751.
- PayPal recurring use requires seller-account **Reference Transactions** enabled by PayPal Support and recurring permissions granted to Adyen, plus recurring-token lifecycle webhooks. Initial `/sessions` or `/payments` token parameters specify `Subscription` or `UnscheduledCardOnFile`, `Ecommerce`, `shopperReference` and `storePaymentMethod: true`; `shopperEmail` is required for a zero-value authorization and should be omitted otherwise. The page says the `recurring.token.created` webhook arrives when the initial payment has settled and contains `storedPaymentMethodId`; later requests use that token, the same shopper reference, `ContAuth` and the matching recurring model. A requested token or enabled permission is not a successful later charge. See raw lines 753–810.
- For an uncaptured PayPal payment the page routes to **cancel**; after capture it routes to **refund**. For partial refunds with immediate capture, it instructs including the refunded `lineItems` and matching their sum to `amount`, though the adjacent API table does not mark `lineItems` required and says Adyen adds a dummy item if totals differ. The `/refunds` response example has `status: received` and a new refund `pspReference`, not proof of completion. For delayed capture, `capturePspReference` is needed **when later capture, multiple partial captures enabled and more than one partial capture are all true**; use the capture response's PSP reference, not the original payment reference. See raw lines 812–932.
- The page scopes Seller Protection to physical goods and tells participating merchants to supply delivery address, shopper name and line items, then check a test transaction's eligibility. Live setup separately requires a live PayPal business account and environment configuration; the page says PayPal appears live only when the shopper is logged in and has a valid PayPal payment method. Sandbox checks and submitted fields do not prove actual Seller Protection coverage or live availability. See raw lines 934–969.

## Detail locators

- **Prerequisites, availability inputs, Android-to-server handoff:** raw lines 15–42.
- **HUF rounding, conditional risk fields and format:** raw lines 44–123.
- **Server request table, test examples and redirect action:** raw lines 124–678.
- **Return details, synchronous status versus webhooks:** raw lines 679–751.
- **Recurring permissions, zero-value email and settled-payment token webhook:** raw lines 753–810.
- **Cancel/refund split and conditional capture reference:** raw lines 812–932.
- **Seller Protection, sandbox and live account/shopper conditions:** raw lines 934–969.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-refunds]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypal/android-drop-in/2026-09-15|Adyen PayPal Android Drop-in — captured 2026-09-15]]

---
title: "Adyen PayPal with iOS Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypal/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypal/ios-drop-in/2026-09-15.md"
tags: [adyen, paypal, ios, drop-in, recurring-payments]
---

## Overview

This 2026-09-15 Adyen guide adds PayPal to an existing **iOS Drop-in** integration after the PayPal setup steps. It calls `/sessions` the default for Drop-in v5.0.0 or later and gives `/payments` for an additional use case. The page's code snippets use test Checkout API v71 for Sessions and v72 for Payments, with older and varied API-library versions; they are examples, not a single version-neutral implementation. [[adyen]] [[adyen-ios-sdk]]

## Key takeaways

- The request tables describe optional `lineItems`; `additionalData.paypalPairingId` applies only to customer-initiated transactions using Fraudnet with the same pairing ID sent to Fraudnet and Adyen. `additionalData.paypalRisk` applies to marketplaces and merchants in specific verticals when PayPal tells them to send risk fields. The required keys can vary by merchant; the fields are sent as a stringified `additional_data` array, and the PayPal account manager is the stated authority for applicability. The example risk payload does not make risk fields universal.
- For HUF transactions, PayPal expects the transaction and line-item amounts rounded to whole amounts that add up. Adyen warns a mismatch after its own rounding can cause PayPal to reject the transaction; the guide recommends merchant-side rounding and checking the sum.
- There is no required PayPal-specific Drop-in configuration in the v5.0.0+ or v4.x.x tabs. The synchronous `resultCode` is for current shopper status only: even `Authorised` can later fail under post-authorization risk rules. The guide directs order decisions to the final `AUTHORISATION` webhook; `OFFER_CLOSED` for an unfinished payment is received only if that non-default event is enabled. These outcomes concern payment authorization, not proof of capture, settlement, payout or recipient funds.
- PayPal recurring payments have extra seller-account steps: PayPal Support must enable Reference Transactions, and the merchant must grant the stated recurring permissions to Adyen. Enable recurring-token lifecycle webhooks; initial token requests use `Ecommerce`, a shopper reference and `Subscription` or `UnscheduledCardOnFile`, with `shopperEmail` required only for a zero-value authorization. The guide says `recurring.token.created` arrives after settlement and carries `storedPaymentMethodId` for later `ContAuth` requests. A requested token is not evidence that the initial payment settled or a later payment succeeded.
- Before capture, the guide routes to cancellation; after capture, to refund. For immediate capture it says partial refunds need `lineItems`, but its table leaves `lineItems` unmarked as required and ambiguously calls them items the shopper should pay for while the next sentence says to specify only refunded items. For delayed capture, it states `capturePspReference` is needed when later capture, multiple partial captures enabled and more than one partial capture are all true; use the capture reference, not the payment reference, or the refund can fail. The sample refund response says `status: received` and does not prove funds returned.
- PayPal Seller Protection in this guide is scoped to physical goods and program participation; it asks for delivery address, shopper name and line items and recommends checking test-payment eligibility. Live operation separately requires a live PayPal business account and environment configuration. The page says live PayPal appears only when the shopper is logged in and has a valid PayPal payment method. This snapshot does not prove current merchant, shopper or country eligibility.
- Treat code as illustrative: the `/payments` PHP example puts `STATE_DATA` in `paypalRisk` and `STRINGIFIED_ADDITIONAL_DATA_ARRAY` in `shopperReference`, unlike the surrounding prose and other examples; Python risk strings are not escaped as valid Python literals, Ruby risk objects use non-JSON syntax, and Go snippets label library v10.4.0 while importing v9 paths. Verify fields and serialization against the chosen API/library version before implementation.

## Detail locators

- Existing Drop-in and PayPal setup prerequisites, endpoint choice, optional/conditional request fields: [[raw/adyen/docs/payment-methods/paypal/ios-drop-in/2026-09-15|PayPal iOS Drop-in raw]], lines 15–44 and 510–522.
- Sessions v71 test examples and library versions: [[raw/adyen/docs/payment-methods/paypal/ios-drop-in/2026-09-15|PayPal iOS Drop-in raw]], lines 46–508.
- Payments v72 test examples, `paypal`/`sdk` method, PHP/Go/Python/Ruby example discrepancies: [[raw/adyen/docs/payment-methods/paypal/ios-drop-in/2026-09-15|PayPal iOS Drop-in raw]], lines 524–1033.
- HUF rounding and conditional marketplace/vertical risk fields with stringified formatting: [[raw/adyen/docs/payment-methods/paypal/ios-drop-in/2026-09-15|PayPal iOS Drop-in raw]], lines 1035–1113.
- Drop-in configuration, result codes, authorization and optional webhook details: [[raw/adyen/docs/payment-methods/paypal/ios-drop-in/2026-09-15|PayPal iOS Drop-in raw]], lines 1115–1162.
- Reference Transactions, recurring permissions, token creation after settlement and later token charge: [[raw/adyen/docs/payment-methods/paypal/ios-drop-in/2026-09-15|PayPal iOS Drop-in raw]], lines 1164–1221.
- Capture-dependent cancellation/refund routes, line-item wording conflict, refund response and capture-reference condition: [[raw/adyen/docs/payment-methods/paypal/ios-drop-in/2026-09-15|PayPal iOS Drop-in raw]], lines 1223–1343.
- Seller Protection, sandbox test and live-account/shopper conditions: [[raw/adyen/docs/payment-methods/paypal/ios-drop-in/2026-09-15|PayPal iOS Drop-in raw]], lines 1345–1380.

## Related

- [[adyen-ios-sdk]] — native Drop-in and merchant-server integration boundary.
- [[adyen-tokenization]] — token lifecycle and stored-method scope.
- [[adyen-online-payments]] — payment-result and webhook context.
- [[adyen-refunds]] — captured-payment refund context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypal/ios-drop-in/2026-09-15|Adyen PayPal iOS Drop-in guide (2026-09-15 snapshot)]]

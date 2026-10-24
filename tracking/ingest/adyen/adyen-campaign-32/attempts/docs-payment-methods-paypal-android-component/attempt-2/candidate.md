---
title: "Adyen PayPal Android Redirect Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypal/android-component"
raw_files:
  - "adyen/docs/payment-methods/paypal/android-component/2026-09-15.md"
tags: [adyen, paypal, android, redirect, online-payments]
---

## Overview

Adyen guide for adding PayPal to an existing Android Components integration through the Redirect Component. The shopper leaves the app for PayPal and the merchant server submits returned details. The page metadata says last modified 2021-07-26; this copy was captured 2026-09-15 and contains versioned test examples. It does not prove present merchant or shopper-account enablement, authorization, capture, settlement, refund or funds receipt.

## Key takeaways

- Existing Android Components integration and PayPal setup are prerequisites. `/paymentMethods` discovery uses supported `countryCode`, `amount.currency` and minor-unit `amount.value`; the page’s currency example is blank (`****`), so it supplies no specific currency rule. A listed `paypal` type is a method-selection result, not completed setup or payment (raw lines 15–40).
- The server’s Advanced `/payments` request sets `paymentMethod.type: paypal`; the table describes `channel: Android`, `returnUrl` from `RedirectComponent.getReturnUrl(context)`, optional `lineItems`, Magnes-only `paypalPairingId` and PayPal-required risk fields for marketplaces or specified verticals. Risk-field applicability is merchant-specific; ask the PayPal account manager. `additionalData.paypalRisk` uses a stringified `additional_data` key/value array. For HUF, transaction and item amounts must round to whole HUF and reconcile or PayPal may reject (raw lines 42–139).
- A `/payments` response can contain a redirect `action`, which the server passes to the app; after the shopper returns, the server sends `actionComponentData.details` to `/payments/details`. The shown `RedirectShopper` and `Authorised` responses are examples. Synchronous `resultCode` is for current shopper messaging; AUTHORISATION webhooks determine final outcome, including failures after apparent authorization. `OFFER_CLOSED` arrives only when enabled. None of these statuses alone proves capture or settlement (raw lines 649–750).
- Recurring requires PayPal Support-enabled Reference Transactions on the seller account, PayPal recurring permissions granted to Adyen, and token lifecycle webhooks. The initial token request is described with `Subscription` or `UnscheduledCardOnFile`, `Ecommerce`, unique `shopperReference`, `storePaymentMethod: true`, and `shopperEmail` only for zero-value authorization. After settlement, `recurring.token.created` supplies the stored payment method ID; later token requests use the same shopper reference, `ContAuth`, and `recurringProcessingModel` set to `Subscription` or `UnscheduledCardOnFile`; this page does not say that later model must match the initial selection. The guide does not itself describe a shopper-consent or billing-agreement screen; do not infer one from these fields (raw lines 753–810).
- Before capture, cancel; after capture, refund. For partial refunds after immediate capture, the guide directs `lineItems` for the refunded items and says Adyen can add a dummy line item if its sum differs from `amount`. For later capture, `capturePspReference` is needed when delayed capture, multiple partial captures enabled and more than one partial capture are all true; use the capture response PSP reference, not the payment reference. A `received` refund example is request receipt, not proof of funds returned (raw lines 812–932).
- PayPal Seller Protection applies only to physical goods here and has delivery-address, shopper-name and line-item guidance. Sandbox testing uses distinct PayPal business and personal accounts. Live use requires a live PayPal business account and configuration; the page says PayPal is available only when the shopper is logged in and has a valid funding method. Request snippets conflict with field guidance: the `/payments` table says to set `channel: Android` and derive `returnUrl` from `RedirectComponent.getReturnUrl(context)`, but every shown request example omits `channel` and uses a fixed generic HTTPS return URL. Those example URLs are not established to return to the Android Component. The PHP sample also puts a stringified-array placeholder in `shopperReference`, the Python sample embeds unescaped JSON in a string, and the Ruby sample shows a non-JSON stringified risk map. Keep the table guidance primary; do not copy the snippets as complete implementations (raw lines 133–160, 286–302, 374, 406, 488, 522, 530–541, 580–589, 644, 934–969).

## Detail locators

- Setup and method discovery: raw lines 15–40.
- HUF rounding and marketplace/vertical risk fields: raw lines 42–124.
- `/payments` field table and language/version examples: raw lines 126–649.
- Redirect return, result codes and webhook outcomes: raw lines 650–750.
- Recurring authorization, token webhook and later charge fields: raw lines 753–810.
- Cancel/refund and partial-capture-specific refund rules: raw lines 812–932.
- Seller Protection and test/live account conditions: raw lines 934–969.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-payment-capture]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypal/android-component/2026-09-15|Adyen PayPal Android Component snapshot]]

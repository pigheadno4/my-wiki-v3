---
title: "Stripe: Accept a Payment with Mondu"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/mondu/accept-a-payment"
raw_files:
  - "stripe-mondu-accept-payment-2025.md"
tags: [stripe, bnpl, mondu, buy-now-pay-later, b2b, europe, checkout, payment-intents, elements]
---

## Summary

Stripe’s May 6, 2026 full guide describes Mondu (`mondu`) as a single-use payment method with 30-day net terms and customer authorization by redirect. The November 7, 2026 capture is a selector for Checkout, Elements with Checkout Sessions API, Elements with Payment Intents API, and Direct API. The route details below come from the May guide. The linked November variants would be needed to verify November API, SDK, and Checkout currency details.

## Integration routes in the May 6, 2026 guide

- **Hosted-style Checkout.** The example sets `success_url` on the Checkout Session. The compatibility section lists Europe as the supported business-location category, lists EUR for presentment, and requires all line items in a Session to use the same currency. It lists payment mode as supported and setup and subscription modes as unsupported. The Elements route backed by Checkout Sessions lists the same conditions. Use the compatibility prose for the May Checkout currency scope given the malformed currency comment in the hosted example. For order fulfillment, this route points to the Checkout fulfillment guide. See lines 18–35, 44–74, and 95–112.
- **Elements with Checkout Sessions.** The server creates the Session with `ui_mode: elements` and `return_url` and passes its client secret to the frontend. The guide collects, validates, and saves the customer email on the client unless it is set as `customer_email`, supplied by a `customer_account` or `customer` with an email, or independently validated and supplied at confirmation. The client uses the Checkout SDK and its `confirm` method. The May HTML/JS example uses `initCheckoutElementsSdk`, loads Dahlia directly or specifies `@stripe/stripe-js` 7.0.0 or later for module loading. The React instructions specify React Stripe.js 5.0.0 or later and the Stripe.js loader 8.0.0 or later. See lines 125–251, 330–345, 378–391, and 488–527.
- **Elements with PaymentIntents.** The server creates the PaymentIntent and returns its client secret. The client uses Stripe.js `stripe.confirmPayment` with `return_url`. Accounts v2 `customer_account` and Customers v1 `customer` are separate examples for saving and retrieving payment methods. See lines 799–933 and 960–981.
- **Direct API.** Create the PaymentIntent on the server and use its client secret with Stripe.js `stripe.confirmPayment` and `return_url` on the client. The optional server-driven redirect supplies `return_url` at confirmation, checks for `requires_action`, and uses the URL under `next_action.redirect_to_url`. The Direct API currency section lists EUR as the default, CHF for Switzerland, and GBP for GB. See lines 1179–1195, 1268–1362, and 1376–1380.

## Payment result and optional manual capture in the May guide

- **Payment result.** In the May Direct API route, verify the PaymentIntent status on the return page using the redirect parameters described in lines 1315–1320. The Elements with PaymentIntents and Direct API sections identify `payment_intent.succeeded` as the payment-completion event and recommend listening for it to trigger work such as fulfillment. A browser return alone does not establish payment completion. See lines 1076–1080 and 1358–1362.
- **Optional manual capture.** The Elements with PaymentIntents section sets `capture_method: manual` to authorize first. After successful authorization the PaymentIntent transitions to `requires_capture`. A capture request takes the full authorized amount by default or a specified amount up to that total. If capture does not occur within seven days, Stripe cancels the PaymentIntent and sends `payment_intent.canceled`. See lines 1094–1140.
- **Testing and errors.** The May Elements examples describe approve/decline controls on the sandbox test page and a redirect to Mondu in live mode. The May PaymentIntent error tables include `payment_intent_invalid_currency`, `payment_intent_authentication_failure`, and `payment_intent_redirect_confirmation_without_return_url`. See lines 564–568, 1142–1158, and 1382–1392.

## Related

- [[stripe]]
- [[stripe-bnpl]]
- [[source-stripe-mondu]] — Stripe’s method overview for dated Connect and general currency coverage. The May overview marks Connect No and the November overview marks it Yes. These are method-level documentation entries.

## Raw Sources

- [[raw/stripe-mondu-accept-payment-2025|May 6, 2026 full guide]] — verbatim webpage content (1392 lines); fixed `_Prices_` (×2), `_sandbox_` (×2), `_PaymentIntent_` (×2), `_client secret_` (×2), `_webhook_` (×2); downloaded 1 CDN image to `raw/assets/`

## Related raw API references

- [[raw/stripe-payments-mondu-accept-a-payment-2026-11-07|November 7, 2026 variant selector]] — navigation to four integration variants

---
title: "Stripe Docs — Accept a payment using local cards in South Korea"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/kr-card/accept-a-payment"
raw_files:
  - "stripe-kr-card-accept-payment-2025.md"
tags: [stripe, south-korea, krw, kr-card, local-payment-methods, nicepay, payment-intents, checkout]
---

## Summary

The May 8, 2026 guide shows how South Korea-based customers pay with locally issued South Korean cards using `kr_card` through Checkout or the Direct API. Both paths describe a redirect to Stripe's local processor partner to authenticate and authorize, followed by a return to the merchant. The November 7, 2026 capture retains the purpose and links to Checkout and Direct API variants. The linked implementation bodies are outside that capture.

## May Checkout compatibility and examples

The May Checkout guide lists 28 merchant locations (AT, BE, CY, DE, DK, EE, ES, FI, FR, GB, GR, HK, HR, HU, IE, IT, JP, LT, LU, LV, MT, NL, PT, SE, SG, SI, SK, and US). It lists payment, setup, and subscription modes, with all line items in KRW and a **100 KRW minimum**. For dynamic methods Stripe evaluates currency, payment-method restrictions, and other eligibility parameters. The May manual-list examples add `kr_card` to `payment_method_types`.

- The May hosted Node example uses `mode: 'payment'` and `success_url`.
- The May embedded Node example uses `mode: 'payment'`, `ui_mode: 'embedded_page'`, and `return_url`.

The examples illustrate payment mode. The compatibility list gives the broader mode scope. See May raw lines 8–106 and the server API version warning below.

## May Direct API and NICEPAY disclosure

The server creates a PaymentIntent with amount, KRW, and `kr_card` in its historical `payment_method_types` list. The May Node create example also passes `payment_method_data.type: 'kr_card'`, beyond the fields named in the create prose. Send the **PaymentIntent client secret** to the browser via an endpoint or server-rendered form. The browser calls `stripe.confirmPayment` with the secret and `return_url`. Its May example also passes `payment_method_data.type: 'kr_card'`. The customer selects their issuer and authorizes on the partner page. The May sample uses the Stripe.js Dahlia script. The sample destructures `error` from the confirmation result, but its error branch reads `result.error.message`. That sample mismatch remains in the historical raw (lines 246–271).

The **May Direct API client section** requires the merchant to identify NICEPAY and link its terms on the checkout page:

> After submission, you’re redirected to complete next steps. This transaction is processed through NICEPAY in accordance with NICEPAY’s [terms of use](https://start.nicepay.co.kr/homepage/terms/bill.do).

The May Checkout variant describes the processor redirect. The disclosure requirement or exemption for hosted and embedded Checkout remains undetermined from that variant.

## Server API version boundary for the May examples

The separate changelogs document HTTP 400 for writing `payment_method_types` on the linked `2026-09-30.endive` Checkout Session Create and PaymentIntent Create endpoints. Checkout continues to return the computed compatibility list. PaymentIntent Create uses error code `payment_method_types_no_longer_supported` and its computed response property is read-only. The Intent changelog's separate Impact paragraph names `2026-08-26.preview`, while its versioned endpoints and REST table name Endive.

The cited alternatives are Dashboard-managed dynamic payment methods with optional `excluded_payment_method_types`, or `allowed_payment_method_types` filtered for compatibility. Compatibility filtering and actual `kr_card` display are separate. The server REST scope is distinct from the May browser's Dahlia script and the November navigation capture.

## Return, tests, and payment outcome

The May Direct API return URL includes `payment_intent` and `payment_intent_client_secret` for looking up the Intent status. Check the Intent to display the result. A redirect, returned identifiers, or browser callback alone provides no evidence of payment approval, fulfillment, settlement, or bank payout.

The May Checkout sandbox has **Local cards** with authorize/fail choices on a Stripe-hosted test page. The Direct API guide uses test API keys and the test redirect. Authorization in these fixtures transitions the Intent from `requires_action` to `succeeded`. Failure transitions it to `requires_payment_method`. These are test-only results.

The May Direct API guide describes `payment_intent.succeeded` as the payment completion event and recommends asynchronous event handling for post-payment actions. It describes Dashboard handling, a custom webhook, and partner apps. See May lines 274–301.

## CDN Assets

- `raw/assets/stripe-kr-card-payment-flow.mov` — May payment-flow demo video (4.8 MB)

## Related Pages

- [[stripe-korea-payment-methods]] — South Korea payment methods
- [[source-stripe-korea-payment-methods]] — method overview, installments, disputes, and refunds
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-kr-card-accept-payment-2025|2026-05-08 local Korean cards acceptance guide]]

## Related raw API references

- [[raw/stripe-payments-kr-card-accept-a-payment-2026-11-07|2026-11-07 Checkout and Direct API variant index]]
- [[raw/stripe-changelog-endive-2026-09-30-remove-payment-method-types-checkout-sessions-2026-11-07|2026-11-07 Endive Checkout Sessions changelog]] — Create request-field scope
- [[raw/stripe-changelog-endive-2026-09-30-removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents-2026-11-07|2026-11-07 Endive Intents changelog]] — Create request-field and preview-label scope

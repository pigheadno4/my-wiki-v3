---
title: "Stripe Docs — Accept a payment using Kakao Pay in South Korea"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/kakao-pay/accept-a-payment"
raw_files:
  - "stripe-kakao-pay-accept-payment-2025.md"
tags: [stripe, south-korea, krw, kakao-pay, local-payment-methods, nicepay, payment-intents, checkout]
---

## Summary

The full 2026-05-08 guide describes one-time Kakao Pay (`kakao_pay`) acceptance through Checkout or a Direct API PaymentIntent, with a redirect to Stripe's local processor partner for authentication and authorization. The 2026-11-07 capture at the canonical URL is a navigation index for Checkout and Direct API variants only. It does not reverify the May requirements, availability, or payment outcomes (old raw lines 8-20, 110-120; new raw lines 5-14).

## Dated compatibility and prerequisites

- The May guide lists 27 supported business locations and says Kakao Pay is unavailable in Singapore. Its supported and presentment currency is KRW; it lists payment, setup, and subscription modes (old raw lines 22-41). The latter two are compatibility listings, not procedures supplied by this acceptance guide.
- For the May Checkout route, every line item must be in KRW, the minimum accepted amount is 100 KRW, and the buyer's email must be provided. The 2,000,000 KRW cap is on customer stored-value top-ups; the guide states no maximum for card passthrough transactions (old raw lines 38-51). The sample Sessions omit an explicit email field, so the exact way each Checkout integration supplies it is not shown by those samples (old raw lines 47-103).
- In the May Direct API route, the server creates a KRW PaymentIntent with `payment_method_types: ["kakao_pay"]` and the buyer's `payment_method_data.billing_details.email`. The client receives its client secret for confirmation (old raw lines 135-161). The secret key stays on the server; the client uses a publishable key and client secret (old raw lines 141-161, 247-265).

## Checkout path in the May guide

Stripe says eligible methods may be surfaced automatically by dynamic payment methods. The explicit `kakao_pay` entry in `payment_method_types` belongs to the alternative manual-configuration path (old raw lines 12-16, 43-51). Its hosted Session example uses `mode: "payment"`, KRW line items and `success_url`; the full embedded-page example adds `ui_mode: "embedded_page"` and uses `return_url` (old raw lines 53-103). Neither Session creation nor browser return establishes a paid outcome.

The May Checkout sandbox test selects Kakao Pay and Pay, then permits authorization or failure on a Stripe-hosted redirect page. It describes PaymentIntent transitions from `requires_action` to `succeeded` on test authorization or `requires_payment_method` on test failure (old raw lines 106-108). These are test states, not guaranteed live outcomes.

## Direct API path in the May guide

The server-created PaymentIntent includes the amount, KRW currency, Kakao Pay type, and buyer email. The client calls `stripe.confirmPayment` with the PaymentIntent client secret, `payment_method_data.type: "kakao_pay"`, and a `return_url`; the customer is redirected to the local processor for issuer selection and authorization (old raw lines 135-156, 236-273).

Only the May Direct API client-side section explicitly instructs the merchant to show the processor identity and NICEPAY terms language/link on its checkout page (old raw lines 230-235). The May Checkout section does not give a parallel merchant-page instruction (old raw lines 8-108); these captures do not establish how hosted or embedded Checkout supplies that disclosure. Do not generalize the Direct API page instruction to every UI route.

The redirect return URL carries `payment_intent` and `payment_intent_client_secret` query parameters; verify the PaymentIntent status to decide what result to display (old raw lines 283-288). In May test mode, authentication changes a PaymentIntent from `requires_action` to `succeeded`, while a failed test changes it to `requires_payment_method` (old raw lines 290-292). The guide says Stripe sends `payment_intent.succeeded` when payment completes and recommends asynchronous events over a client callback for fulfillment (old raw lines 294-299). A redirect or callback alone is not payment success.

## Historical example warning

The May Direct API error branch destructures `error` from `confirmPayment` but then reads `result.error.message`, a mismatched variable in the illustrative snippet (old raw lines 263-279). Do not copy that line as a working error handler. The November index provides no replacement code.

## Related Pages

- [[stripe-korea-payment-methods]] — South Korean payment methods concept and dated Kakao Pay route qualifications
- [[source-stripe-korea-payment-methods]] — South Korea overview
- [[source-stripe-kakao-pay-set-up-future-payments]] — separate future-payment setup guide
- [[source-stripe-kr-card-accept-payment]] — KR card acceptance comparison
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-kakao-pay-accept-payment-2025|Kakao Pay acceptance guide, captured 2026-05-08]] — full historical Checkout and Direct API variants

## Related raw API references

- [[raw/stripe-payments-kakao-pay-accept-a-payment-2026-11-07|Kakao Pay acceptance variant index, captured 2026-11-07]] — navigation only; Checkout and Direct API links

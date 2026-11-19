---
title: "Stripe: Accept a Payment with Billie"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/billie/accept-a-payment"
raw_files:
  - "stripe-billie-accept-payment-2025.md"
tags: [stripe, bnpl, billie, buy-now-pay-later, b2b, checkout, payment-intents, elements, mobile]
---

## Overview

The May 6, 2026 full guide describes integrating Billie's single-use, business Pay by Invoice method across hosted Checkout, Checkout Sessions with Elements, Payment Intents with Elements, Direct API, iOS, and Android. It gives 7–120 day payment terms and describes customer authorization through a redirect. The November 7 capture at the canonical URL is only a six-destination variant index; it supplies navigation, not refreshed payment behavior, availability, or eligibility. See [[stripe]] and [[stripe-bnpl]].

## Key takeaways from the May 2026 guide

- **Path-specific compatibility:** Hosted Checkout and Checkout Sessions with Elements each list EUR supported and presentment currency, payment mode yes, and setup/subscription modes no. Checkout Session line-item Prices must share one currency; the hosted Checkout section gives a 0.01 EUR minimum. The Payment Intents with Elements section uses EUR in examples, without an Elements-wide EUR-only compatibility statement. Direct API and both mobile sections list country-mapped EUR, SEK, NOK, DKK, GBP, and CHF. These historical path descriptions do not resolve current variant behavior.
- **Different return destinations:** Hosted Checkout's Session example uses `success_url`. The Checkout Sessions with Elements examples use `return_url`. The Payment Intents with Elements and Direct API redirect-confirmation paths provide `return_url`; the latter also explains a `requires_action` / `redirect_to_url` manual redirect. The iOS section uses an app return URL and callback for webview dismissal. A blanket `return_url` requirement across every path is unsupported.
- **Separate objects and outcomes:** The hosted Checkout example creates a Checkout Session with `success_url`; it does not show a client-secret handoff or client confirmation. Checkout Sessions with Elements returns a Session client secret, while Payment Intents with Elements, Direct API, iOS, and Android use PaymentIntent client-secret paths for client-side confirmation or redirect. Creating a Session or Intent, returning to an app or page, or receiving a client callback does not itself establish payment success. For post-payment actions, the guide directs readers to the `payment_intent.succeeded` event rather than a client callback.
- **Optional manual capture:** In the PaymentIntent section, `capture_method: manual` authorizes first. After successful authorization the Intent reaches `requires_capture`; a capture request must follow within seven days or Stripe cancels the Intent and emits `payment_intent.canceled`. The guide also describes optional cancellation.
- **Advice and testing:** Unified `line_items` cart data is recommended to maximize approval rates and was marked early access, not a universal required field. The sandbox Billie flow offers an approve/decline test page; the described live path redirects to Billie. The guide's `dahlia` Stripe.js, React package floors, iOS compatibility, and Android 23.7.0 are May examples, not verified November requirements.

## Detail locators

- Hosted Checkout compatibility, Session creation, and `success_url`: [[raw/stripe-billie-accept-payment-2025|May full guide]], lines 22–75.
- Checkout Sessions with Elements compatibility, server-created Session/client secret, and `return_url` examples: same raw, lines 93–208; client confirmation and testing, lines 494–574.
- Payment Intents with Elements server/client flow, redirect confirmation, events, optional capture, line-item advice, sandbox/live testing, and error codes: same raw, lines 576–1170. The error table includes `payment_intent_invalid_currency`, `payment_intent_authentication_failure`, and `payment_intent_redirect_confirmation_without_return_url` for PaymentIntent confirmation.
- Direct API redirect, status check, country-currency list, and error codes: same raw, lines 1172–1407.
- iOS and Android PaymentIntent/client-secret and SDK examples, callbacks, and country-currency lists: same raw, lines 1409–1914.

## Related

- [[source-stripe-billie]] — Billie product, country, dispute, refund, and Connect details.
- [[stripe-bnpl]] — provider BNPL index and reciprocal source route.

## Raw Sources

- [[raw/stripe-billie-accept-payment-2025|Billie accept-payment full guide, fetched 2026-05-06]] — factual evidence for the dated integration details above.

## Related raw API references

- [[raw/stripe-payments-billie-accept-a-payment-2026-11-07|Billie accept-payment variant index, fetched 2026-11-07]] — navigation-only capture listing Checkout; Elements via Checkout Sessions API or Payment Intents API; Direct API; iOS; and Android. The linked variants were not fetched in this packet, so this index does not revise the May guide's mechanics or prove current support.

---
title: "Stripe: Accept a Payment with Alma"
type: source
date_ingested: 2026-05-06
date_updated: 2026-11-15
canonical_url: https://docs.stripe.com/payments/alma/accept-a-payment
original_format: webpage
raw_files:
  - "stripe-alma-accept-payment-2025.md"
tags: [stripe, bnpl, alma, buy-now-pay-later, checkout, payment-intents, elements, ios, android]
---

## Summary

The 2026-11-07 capture of Stripe's Alma acceptance guide is a variant index. It links Checkout, Elements, Direct API, iOS, and Android, but contains no integration steps or payment behavior. The five paths and details below come from the retained 2026-05-06 guide; the November index neither revalidates nor removes them. See [[stripe]] and [[stripe-bnpl]].

## Dated integration details (2026-05-06 capture)

Alma is described as a single-use method for 2, 3, or 4 installments. Customers authorize with Alma after a redirect. The old guide's explicit Alma PaymentIntent examples use `eur`; its currency tables and invalid-currency error say Alma supports EUR. The old iOS and Android *dynamic payment-method* examples instead set `currency: "usd"`. Those generic examples conflict with the Alma currency tables and do not establish USD Alma eligibility. Check the applicable variant and currently pinned currency authority before using either mobile example as Alma eligibility guidance. (Old raw lines 18-18, 703-713, 938-945, 1051-1087, 1194-1200, 1300-1335, 1413-1420.)

- **Checkout:** The hosted Checkout Session example uses `success_url`; embedded Checkout uses `return_url`. The old guide requires same-currency line items for its Checkout path. These Session examples must not inherit the PaymentIntent confirmation requirement below. (Old raw lines 33-90.)
- **Elements and Direct API:** Create a PaymentIntent with the amount and supported currency on the server, send its client secret to the client, and confirm for Alma. The old error table says to provide a `return_url` **when confirming a PaymentIntent with Alma**; Elements and Direct API confirmation examples include it. The Direct API variant also shows an optional server confirmation and manual redirect after `requires_action` and `next_action.redirect_to_url`. (Old raw lines 127-173, 392-394, 703-713, 733-750, 822-910.)
- **iOS and Android:** The old guide includes separate Mobile Payment Element branches. Its iOS SDK statement is iOS 13+ and its Android Gradle sample uses version 23.7.0; these are historical sample details, not a November SDK compatibility check. Android prose names `PaymentHandler.confirmPayment`, while its Kotlin sample uses `PaymentLauncher.confirm`; verify the selected SDK/version API before copying that flow. (Old raw lines 946-972, 1154-1173, 1220-1265, 1362-1405.)

## Authorization, capture, and outcome boundaries (2026-05-06 capture)

- In the old Elements branch, mobile authentication redirects to Alma and then to the PaymentIntent `return_url`; desktop web shows a QR code. An authentication session expires after one hour, and the desktop QR code can be refreshed up to 20 times. For an Alma PaymentIntent left in `requires_action` without action for an hour, the old guide says Stripe detaches the PaymentMethod and moves the PaymentIntent to `requires_payment_method`. This is a scoped state claim, not a universal expiry for all intents. (Old raw lines 605-620, 693-702.)
- When `capture_method: "manual"` is used, successful authorization moves the PaymentIntent to `requires_capture`; capture is a separate request. Stripe cancels an uncaptured PaymentIntent after the seven-day window and emits `payment_intent.canceled`. This window applies to that manual-capture flow. (Old raw lines 622-665.)
- A browser return, client callback, or QR modal closing does not by itself prove final payment or capture. Inspect PaymentIntent status on return and handle `payment_intent.succeeded` through an event handler before fulfillment actions. The old sandbox flow redirects to a test approval/decline page, whereas the live flow redirects to Alma. (Old raw lines 488-543, 617-618, 670-692, 912-917.)
- The old error table includes `payment_intent_invalid_currency` (Alma only `eur`), `missing_required_parameter`, `payment_intent_payment_attempt_failed`, and `payment_intent_redirect_confirmation_without_return_url`. The last error is specific to confirming an Alma PaymentIntent. (Old raw lines 703-713.)

## Related raw API references

- [[raw/stripe-payments-alma-accept-a-payment-2026-11-07|Alma acceptance variant index, 2026-11-07]] — 2026-11-07 variant-navigation index only; it links five UI/platform branches and supplies no refreshed behavioral rule.

## Raw Sources

- [[raw/stripe-alma-accept-payment-2025|Alma acceptance guide, 2026-05-06]] — 2026-05-06 detailed webpage capture (1437 lines; filename retained), including Checkout, Elements, Direct API, iOS, and Android variants.

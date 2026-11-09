---
title: "Stripe: Accept a Payment"
type: source
date_ingested: 2026-11-09
canonical_url: https://docs.stripe.com/payments/accept-a-payment
original_format: webpage
raw_files:
  - "stripe-accept-a-payment-2025.md"
  - "stripe-design-payments-integration-2025.md"
tags: [stripe, checkout, payment-element, payment-intents, mobile, ios, android, react-native, webhooks, saved-payment-methods]
---

## Summary

The 2026-11-07 capture of the base URL is a 20-line index linking to Checkout, Elements, and mobile variants. It contains no implementation body. The retained 2026-04-20 capture contains the detailed hosted Checkout, embedded Checkout, Checkout Sessions Elements, Payment Intents Elements, iOS, Android, and React Native guides. The index's omission of the older Payment Intents Elements link does not establish removal or deprecation. The parameterized November variant bodies were not captured here, so their current examples, availability, and version requirements remain unverified.

## Web integration paths in the 2026-04-20 guide

| Path | Checkout `ui_mode` | Dated integration distinction |
| --- | --- | --- |
| Stripe-hosted Checkout | Hosted redirect | Create a Checkout Session server-side and redirect the customer to its URL. |
| Embedded Checkout form | `embedded_page` | Create a Checkout Session and render its embedded page; the older variant URL uses `ui=embedded-form`. |
| Payment Element with Checkout Sessions API | `elements` | Initialize Checkout from the Session `client_secret` with `stripe.initCheckoutElementsSdk` or React `CheckoutElementsProvider`; confirm through Checkout actions. |
| Payment Element with Payment Intents API | Not a Checkout `ui_mode` | Create a PaymentIntent, initialize Elements with its `client_secret`, and use `stripe.confirmPayment`; this is a distinct API flow. |

The November index links hosted Checkout, a variant labeled **Full embedded page** (`ui=embedded-page`), and Elements with `api-integration=checkout`. It also links iOS, Android, and React Native. The changed embedded-page label and query alone do not establish a behavior migration from the older embedded-form variant.

## Checkout Sessions: dated behavior

- The older hosted guide says a Checkout Session expires after 24 hours by default. It describes branding choices including preset fonts, corner radii, colors, and logo.
- For the Checkout Sessions Elements variant, the Session `client_secret` initializes Checkout; `checkout.confirm` or loaded Checkout actions confirm the payment. The older document recommends this path for most integrations, while Payment Intents offers a separate lower-level flow. The raw page's agent-directed text is historical page content, not an instruction to this wiki.
- The older guide shows `payment_intent_data.capture_method: 'manual'` on Session creation. The resulting PaymentIntent can later be captured via Dashboard or `stripe.paymentIntents.capture(id)`; obtain its ID from `session.payment_intent`.

## Server-side payment events

| Dated flow | Event | Meaning and response |
| --- | --- | --- |
| Checkout Sessions | `checkout.session.completed` | Customer completed the Session. For immediately paid orders, confirm paid status before fulfillment; for delayed methods, completion alone is not final payment success. |
| Checkout Sessions | `checkout.session.async_payment_succeeded` | Delayed payment succeeded; fulfill according to the order's rules. |
| Checkout Sessions | `checkout.session.async_payment_failed` | Delayed payment failed; notify the customer and offer a way to retry. |
| Payment Intents and the older mobile variants | `payment_intent.succeeded` | Payment succeeded; use this server event for fulfillment or other post-payment work. |
| Payment Intents and the older mobile variants | `payment_intent.processing` | Payment initiated but has not completed; communicate the pending status. |
| Payment Intents and the older mobile variants | `payment_intent.payment_failed` | Payment failed; handle the failure and possible retry. |

The 2026-04-20 guide recommends server-side event handling because a client can leave before its callback runs. A redirect, return page, or completed sheet is not a universal paid-funds signal. Fulfillment timing remains conditional on the payment method and the order's risk tolerance.

## Saved payment methods in the older Checkout guide

- `payment_intent_data.setup_future_usage: 'off_session'` saves an eligible method for later off-session use; subscription mode can save for subsequent payments. Cards saved this way have `allow_redisplay: limited` and do not automatically prefill returning Checkout purchases.
- `saved_payment_method_options.payment_method_save: 'enabled'` presents an optional consent checkbox in payment or subscription mode. If selected, Checkout saves with `allow_redisplay: always`, allowing eligible saved cards to prefill. `payment_method_remove: 'enabled'` can expose removal.
- The save-checkbox path needs a customer-configured Account or Customer. For a new customer, the dated guide uses `customer_creation: 'always'`; without a customer object the customer and method are not saved through this path. Checkout can save cards and other methods for off-session charging but only prefills saved cards.
- The older guide describes Accounts v2 as generally available for Connect users and in public preview for other Stripe users. Participants in that preview need a preview API version. Its recommendation to model customers as customer-configured Accounts is conditional on that context; Customer v1 remains a documented alternative.

## Mobile PaymentSheet in the older guide

| Platform | Dated API shape |
| --- | --- |
| iOS (Swift) | `PaymentSheet`, `PaymentSheet.Configuration`, and `present(from:completion:)`; a `PaymentSheet.FlowController` supports a separate selection and confirmation flow. |
| Android (Kotlin) | `PaymentSheet`, `PaymentSheet.Configuration`, and `presentWithPaymentIntent`; FlowController supports a separate flow. |
| React Native | `useStripe()` exposes `initPaymentSheet` and `presentPaymentSheet`; `customFlow: true` can use `confirmPaymentSheetPayment` after selection. |

When `allowsDelayedPaymentMethods` is enabled, a completed PaymentSheet result can precede final payment success or failure. The dated guide says to confirm the customer's order in the UI after a completed sheet, while waiting for successful payment before fulfilling goods. Keep the order acknowledgement, payment state, and fulfillment decision separate.

## Test examples in the older guide

| Number | Example outcome |
| --- | --- |
| `4242424242424242` | Card succeeds without authentication. |
| `4000002500003155` | Card requires authentication. |
| `4000000000009995` | Card declines with an insufficient-funds-like code. |
| `6205500000000000004` | UnionPay card with variable-length number. |

These are test-mode examples from the dated guide, not live authorization guarantees.

## Related Pages

- [[source-stripe-checkout-sessions]] — Checkout Sessions API features and UI modes
- [[source-stripe-payment-intents]] — PaymentIntent lifecycle and status
- [[stripe-checkout]] — Checkout concept and fulfillment conditions
- [[stripe-payment-intents]] — separate Payment Intents path
- [[stripe]] — Stripe company page

## Related raw API references

- [[stripe-payments-accept-a-payment-2026-11-07]] — navigation-only variant index fetched 2026-11-07; links are discovery pointers, not captured implementation bodies

## Raw Sources

- [[stripe-accept-a-payment-2025]] — full integration guide fetched 2026-04-20: hosted and embedded Checkout, Checkout Sessions Elements, Payment Intents Elements, mobile PaymentSheet, webhooks, saved methods, auth and capture, and test examples
- [[stripe-design-payments-integration-2025]] — historical integration overview: Payment Links, Checkout, Elements, and Mobile Elements

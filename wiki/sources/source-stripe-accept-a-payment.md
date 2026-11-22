---
title: "Stripe: Accept a Payment"
type: source
date_ingested: 2026-11-09
date_updated: 2026-11-22
canonical_url: https://docs.stripe.com/payments/accept-a-payment
original_format: webpage
raw_files:
  - "stripe-payments-online-payments-2026-11-07.md"
  - "stripe-accept-a-payment-2025.md"
  - "stripe-design-payments-integration-2025.md"
tags: [stripe, checkout, payment-element, payment-intents, mobile, ios, android, react-native, webhooks, saved-payment-methods]
---

## Summary

The 2026-11-07 capture of the base URL is a 20-line index linking to Checkout, Elements, and mobile variants. It contains no implementation body. The retained 2026-04-20 capture contains the detailed hosted Checkout, embedded Checkout, Checkout Sessions Elements, Payment Intents Elements, iOS, Android, and React Native guides. The index's omission of the older Payment Intents Elements link does not establish removal or deprecation. The parameterized November variant bodies were not captured here, so their current examples, availability, and version requirements remain unverified.

## Online payments decision guide

Stripe's full November 7, 2026 [Online payments guide](https://docs.stripe.com/payments/online-payments) covers the Optimized Checkout Suite. Its options include no-code Payment Links without a website, a recommended full prebuilt page embedded on or redirected from the merchant site, a separate prebuilt embedded Checkout Form, custom Stripe Elements, and the Mobile Payment Element for iOS, Android, and React Native. Checkout studio is marked **Private preview** for launching, configuring, and monitoring Checkout from the Dashboard, including payment-method configuration. The separate studio guide describes these Dashboard workflows without establishing general availability.

Stripe recommends Checkout Sessions for most integrations. Use `price_data` for basic collection or build fuller flows with line items, addresses, subscriptions, discounts, shipping, order and receipt handling, dynamic inventory or line-item updates, and Adaptive Pricing. Stripe Tax is integrated through `automatic_tax.enabled=true` when applicable. The lower-level Payment Intents API leaves the final amount and checkout lifecycle with the merchant. Tax and Subscriptions need separate integration where used, and the merchant implements shipping, discounts, address and order tracking, currency conversion, and amount changes. Adaptive Pricing is a Checkout Sessions capability in this comparison. PaymentIntents can separately specify `receipt_email`; that is separate from integrated checkout order tracking and receipts.

Checkout Sessions have checkout lifecycle events and expire 24 hours after creation by default. The captured creation reference allows `expires_at` between 30 minutes and 24 hours from creation. The overview compares PaymentIntent payment-status events and the absence of automatic Checkout Session expiry on that route. Its event comparison is scoped to the two API paths.

Dynamic payment methods control ordering and display. Payment method rules govern availability, configurations group methods by checkout scenario, and the Dashboard can A/B test payment methods. Link offers saved credit/debit cards and US bank accounts and names Instant Bank Payments and Klarna. Use the separate Link paths for Checkout, Web Elements, and native iOS, Android and React Native, and configure Link under Wallets. Eligibility depends on business, currency, amount, customer location, and recurring or off-session use. Shopify, Squarespace, and Adobe Commerce are partner or plugin discovery links.

The April 20, 2026 Online payments guide stated the account signup and Dashboard prerequisite and linked to online sales, subscriptions, quotes and invoices, in-person acceptance, and tips and donations. Its Checkout Sessions Elements example uses a Session `client_secret`, Checkout initializer or React provider, and Checkout confirmation. The separate April implementation below retains that distinction from a PaymentIntent's client secret and `stripe.confirmPayment`. The November overview's omission of the old no-code links and signup instruction establishes no removal or waiver.

### Checkout UI values and completion

The separate **Accept a Payment** November index uses `ui=embedded-page` as a URL selector. In the captured create API, the full embedded page uses `ui_mode=embedded_page`. The November Checkout Form quickstart sends `ui_mode=form` for the separate embedded form. The Stripe `2026-03-25.dahlia` Checkout Session creation contract replaces `hosted`, `embedded`, and `custom` with `hosted_page`, `embedded_page`, and `elements` and adds `form` separately. Requests using any of the three old values fail on that API version. The April and November metadata examples in [[source-stripe-checkout-sessions]] literally use `ui_mode=custom`. Treat this value as dated sample evidence and use the API contract for the deployed version.

For a return page, `status=complete` represents checkout completion while payment may still be processing. For a paid order, verify `payment_status=paid` server-side or wait for `checkout.session.async_payment_succeeded` when a delayed method remains pending. Handle `checkout.session.async_payment_failed` separately. No-payment-required orders have their own completion rule. See the event table below and the [[stripe-checkout]] fulfillment guidance.

## Web integration paths in the 2026-04-20 guide

| Path | Checkout `ui_mode` | Dated integration distinction |
| --- | --- | --- |
| Stripe-hosted Checkout | Hosted redirect | Create a Checkout Session server-side and redirect the customer to its URL. |
| Embedded form (April label) | `embedded_page` | The April `ui=embedded-form` variant creates a Checkout Session and renders a full embedded page in an iframe. The distinct November Checkout Form quickstart uses `ui_mode=form`. |
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

- [[raw/stripe-payments-accept-a-payment-2026-11-07]] — navigation-only variant index fetched 2026-11-07; links are discovery pointers, not captured implementation bodies

## Raw Sources

- [[raw/stripe-payments-online-payments-2026-11-07]] — full November 7, 2026 `/payments/online-payments` decision guide, separate from `/payments/accept-a-payment`
- [[raw/stripe-accept-a-payment-2025]] — full integration guide fetched 2026-04-20: hosted and embedded Checkout, Checkout Sessions Elements, Payment Intents Elements, mobile PaymentSheet, webhooks, saved methods, auth and capture, and test examples
- [[raw/stripe-design-payments-integration-2025]] — April 20, 2026 `/payments/online-payments` overview of Payment Links, Checkout, Elements, and Mobile Elements

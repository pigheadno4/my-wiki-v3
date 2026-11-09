---
title: "Stripe: Accept a Payment"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-accept-a-payment-2025.md"
  - "stripe-design-payments-integration-2025.md"
tags: [stripe, checkout, payment-element, payment-intents, mobile, ios, android, react-native, webhooks, saved-payment-methods]
---

## Summary

Comprehensive Stripe payment integration guide covering all UI modes (web + mobile) and integration patterns. Includes embedded LLM instructions recommending Checkout Sessions over Payment Intents.

## 4 Web UI Modes

| Mode | `ui_mode` | Complexity | Description |
| --- | --- | --- | --- |
| Stripe-hosted page | *(redirect)* | 2/5 | Redirect customer to Stripe's hosted checkout page |
| Embedded form | `embedded_page` | 2/5 | Embed prebuilt Checkout form on your site via iframe |
| Embedded components | `embedded_checkout` | 3/5 | Custom checkout using Stripe Elements components |
| Payment Element + Checkout Sessions | `elements` | 3/5 | Stripe-recommended; Payment Element initialized with `client_secret` |

## Key Integration Facts

- **Checkout Session expires 24h** by default
- **Stripe-hosted customization**: 20 preset fonts, 3 border radius presets, custom colors/logo
- **LLM instruction (embedded in page)**: Use Checkout Sessions + Payment Element over Payment Intents — less code, Adaptive Pricing only available here
- **`ui_mode: "elements"`**: `client_secret` initializes Checkout (`stripe.initCheckoutElementsSdk`); confirm via `checkout.confirm` (React: `CheckoutElementsProvider` from `@stripe/react-stripe-js/checkout`)

## 3 Key Webhooks

| Event | Trigger | Action |
| --- | --- | --- |
| `checkout.session.completed` | Customer completes payment | Fulfill order |
| `checkout.session.async_payment_succeeded` | Delayed method (e.g. ACH) succeeds | Fulfill order |
| `checkout.session.async_payment_failed` | Delayed method fails | Notify customer, bring back on-session |

> Fulfill via webhooks, not redirect — redirect is unreliable.

## Saved Payment Methods

- **Off-session**: `payment_intent_data.setup_future_usage: 'off_session'` — saves PM to charge later
- **Prefill checkbox**: `saved_payment_method_options.payment_method_save: 'enabled'` — shows optional save checkbox; sets `allow_redisplay: always`
- **Prefill removal**: `saved_payment_method_options.payment_method_remove: 'enabled'`
- **`allow_redisplay`**: controls whether saved PM is prefilled; `limited` (set by setup_future_usage/subscription) = not prefilled; `always` (customer opted in) = prefilled
- **Accounts v2**: recommended over Customer v1 for Connect; use `customer_account` param

## Auth + Capture

- Set `payment_intent_data.capture_method: 'manual'` on Checkout Session creation
- Capture later via Dashboard or `stripe.paymentIntents.capture(id)`
- Fetch PaymentIntent ID from Session object (`session.payment_intent`)

## Mobile (PaymentSheet)

| Platform | Key APIs |
| --- | --- |
| iOS (Swift) | `STPPaymentSheet`, `STPPaymentSheetConfiguration`, `present(from:completion:)` |
| Android (Kotlin) | `PaymentSheet`, `PaymentSheet.Configuration`, `presentWithPaymentIntent` |
| React Native | `useStripe()` → `initPaymentSheet`, `presentPaymentSheet`, `confirmPaymentSheetPayment` |

- **Custom flow** (`customFlow: true` / `customFlow = true`): collect payment details first, confirm later — enables custom buy button
- **Delayed payment methods** (`allowsDelayedPaymentMethods: true`): hold order in pending state; fulfill only after `payment_intent.succeeded` webhook

## Test Cards

| Number | Behavior |
| --- | --- |
| 4242424242424242 | Succeeds, no auth required |
| 4000002500003155 | Requires 3DS authentication |
| 4000000000009995 | Declined (insufficient_funds) |
| 6205500000000000004 | UnionPay (variable length 13-19 digits) |

## Related Pages

- [[source-stripe-checkout-sessions]] — Checkout Sessions API: 3 UI modes, 5 built-in features, Adaptive Pricing
- [[source-stripe-payment-intents]] — PaymentIntents lifecycle
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-accept-a-payment-2025]] — Full integration guide: 4 web UI modes, webhooks, saved PMs, auth+capture, iOS/Android/React Native PaymentSheet, test cards (6128 lines, 13 images)
- [[stripe-design-payments-integration-2025]] — Integration overview: 4 paths (Payment Links, Checkout, Elements, Mobile Elements), 5 no-code options

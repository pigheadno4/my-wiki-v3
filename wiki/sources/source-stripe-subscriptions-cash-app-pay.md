---
title: "Stripe Subscriptions — Set Up Cash App Pay Subscription"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/cash-app-pay"
raw_files:
  - "stripe-subscriptions-cash-app-pay-2026.md"
tags: [stripe, billing, subscriptions, cash-app-pay, setup-intents, payment-intents, checkout, qr-code]
---

## Summary

The 2026-05-13 combined guide describes three Cash App Pay subscription paths: Setup Intents API (save a payment method, then subscribe), Subscriptions API (create and confirm separately), and a Stripe-hosted Checkout page. Direct API examples use QR display or mobile redirect for authentication. The 2026-11-07 capture at the same canonical URL is only an index linking these three variants; it does not verify their current fields, eligibility, or runtime results.

## Three integration paths

### Path 1: SetupIntents API

1. In the 2026-05-13 Node.js example, the server creates a SetupIntent with `confirm=true`, `usage='off_session'`, `payment_method_types=['cashapp']`, `mandate_data`, and `return_url`. The example does not establish each field as a requirement for every SetupIntent integration.
2. Status → `requires_action` → use `next_action.cashapp_handle_redirect_or_display_qr_code` to redirect (mobile) or show QR (desktop)
3. The May guide describes the SetupIntent reaching `succeeded` after customer authentication; a QR display or redirect by itself is not a success signal.
4. Server: Create subscription with `default_payment_method` from SetupIntent PM

```js
// Step 4 - create subscription
stripe.subscriptions.create({
  customer: customerId,
  items: [{ price: priceId }],
  default_payment_method: paymentMethodId
})
```

### Path 2: Subscriptions API (PaymentIntents)

1. Server: Create subscription with `payment_behavior=default_incomplete`, `payment_settings.save_default_payment_method='on_subscription'`; expand `latest_invoice.confirmation_secret`
2. The May confirm-step prose names `payment_method_types=cashapp`, while its adjacent curl example sends `payment_method_data[type]=cashapp`, `mandate_data`, and `return_url`. This capture does not resolve the intended confirm parameter; do not transpose the SetupIntent or Checkout Session fields into this request.
3. The PaymentIntent can return `requires_action`; the customer then authenticates through redirect or QR. The May guide states that the PaymentIntent moves to `succeeded` after authentication and the subscription becomes active **after a successful payment**, not merely after a QR display or redirect.

### Path 3: Checkout (hosted)

```js
stripe.checkout.sessions.create({
  payment_method_types: ['card', 'cashapp'],
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

## Authentication UX: QR code + redirect

- **Direct API examples, mobile**: customer is redirected to Cash App; after authentication, the guide describes a redirect to the example `return_url`.
- **Direct API examples, desktop**: `next_action.cashapp_handle_redirect_or_display_qr_code` can display a QR code for Cash App authentication.
- **`mandate_data` and `return_url`**: shown in the May SetupIntent and PaymentIntent-confirm examples. The May Checkout Session example omits both; these captures do not establish universal requiredness across all three paths.

## Testing

In the 2026-05-13 Checkout variant:

- **Mobile sandbox**: tapping Subscribe opens a test approval/decline page.
- **Desktop sandbox**: scanning the QR opens a test approval/decline URL.
- **Live mode**: the guide says there is no test approval/decline choice after redirect or scan. This describes its flow, not a verified payment or account outcome.

## Related pages

- [[stripe-cash-app-pay]] — concept page
- [[stripe-amazon-pay]] — Amazon Pay subscriptions (similar 3-path structure)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Related raw API references

- [[raw/stripe-billing-subscriptions-cash-app-pay-2026-11-07|2026-11-07 variant index]] — links to Setup Intents API, Subscriptions API, and Stripe-hosted page variants; their current content was not captured here.

## Raw Sources

- [[raw/stripe-subscriptions-cash-app-pay-2026|2026-05-13 combined Cash App Pay subscription guide]] — detailed historical evidence for all three variants

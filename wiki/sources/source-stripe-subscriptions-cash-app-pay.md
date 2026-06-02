---
title: "Stripe Subscriptions — Set Up Cash App Pay Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-cash-app-pay-2026.md"
tags: [stripe, billing, subscriptions, cash-app-pay, setup-intents, payment-intents, checkout, qr-code]
---

## Summary

Integration guide for Cash App Pay subscriptions. Three integration paths: SetupIntents API (pre-authorize then subscribe), Subscriptions API (create + confirm in two calls), and Checkout (hosted page). Key characteristic: QR code or mobile redirect for authentication.

## Three integration paths

### Path 1: SetupIntents API

1. Server: Create SetupIntent with `confirm=true`, `usage='off_session'`, `payment_method_types=['cashapp']`, `mandate_data`, `return_url`
2. Status → `requires_action` → use `next_action.cashapp_handle_redirect_or_display_qr_code` to redirect (mobile) or show QR (desktop)
3. After authentication → SetupIntent `succeeded`
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
2. Server: `POST /v1/payment_intents/:id/confirm` with `payment_method_data[type]=cashapp`, `mandate_data`, `return_url`
3. Status → `requires_action` → redirect/QR for authentication → subscription activates

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

- **Mobile**: tapping Subscribe redirects to Cash App app; after auth, Cash App redirects to `return_url`
- **Desktop**: displays QR code (`next_action.cashapp_handle_redirect_or_display_qr_code`); customer scans with Cash App → auto-redirects
- **`mandate_data`**: required — captures customer acceptance (type=online, IP, user agent, accepted_at timestamp)
- **`return_url`**: required for all paths

## Testing

- **Mobile test**: tap Subscribe → test approval/decline page (in sandbox)
- **Desktop test**: scan QR with any QR reader → test URL for approve/decline
- **Live mode**: Cash App auto-approves after redirect/scan — no approve/decline option

## Related pages

- [[stripe-cash-app-pay]] — concept page
- [[stripe-amazon-pay]] — Amazon Pay subscriptions (similar 3-path structure)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-cash-app-pay-2026]] — verbatim Stripe docs webpage

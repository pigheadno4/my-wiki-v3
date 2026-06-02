---
title: "Stripe Checkout: Fulfill Orders"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-after-payment-2025.md"
  - "stripe-checkout-fulfillment-2025.md"
tags: [stripe, checkout, fulfillment, webhooks, checkout-session, payment-links, idempotency, delayed-payments]
---

## Summary

Comprehensive guide for fulfilling orders received via Checkout Sessions API (including Payment Links). Covers the dual-trigger pattern (webhook + landing page), the idempotent `fulfill_checkout` function pattern, delayed payment methods, Stripe CLI testing, and landing page URL configuration.

## Key Takeaways

- **Dual trigger pattern**: webhook (required — handles all cases) + landing page redirect (optional — for immediate UX when customer is present)
- **`fulfill_checkout` function requirements**: idempotent (safe to call multiple times concurrently); expand `line_items`; check `payment_status !== 'unpaid'`; record fulfillment status
- **Webhook events to handle**: `checkout.session.completed` + `checkout.session.async_payment_succeeded` (delayed PMs); optionally `checkout.session.async_payment_failed`
- **Hosted**: `success_url` with `{CHECKOUT_SESSION_ID}` — Checkout waits up to 10s for webhook response before redirecting; **not** supported for organization webhook endpoints
- **Embedded**: `return_url` with `{CHECKOUT_SESSION_ID}`
- **Payment Links**: `after_completion.redirect.url` with `{CHECKOUT_SESSION_ID}` (API) or After Payment tab in Dashboard
- **Stripe CLI**: `stripe listen --forward-to localhost:4242/webhook` for local testing
- **Auto-pagination**: use for sessions with many line items

## `fulfill_checkout` Function Pattern

```js
async function fulfillCheckout(sessionId) {
  // 1. Must be idempotent (safe to call multiple times for same session)
  // 2. Check if already fulfilled — skip if so
  const session = await stripe.checkout.sessions.retrieve(sessionId, {
    expand: ['line_items'],
  });
  // 3. Only fulfill if payment received
  if (session.payment_status !== 'unpaid') {
    // 4. Provision access / ship goods / update inventory
    // 5. Record fulfillment status for this session ID
  }
}
```

## Webhook Event Handler Pattern

Listen for both immediate and delayed events:

```js
if (
  event.type === 'checkout.session.completed' ||
  event.type === 'checkout.session.async_payment_succeeded'
) {
  fulfillCheckout(event.data.object.id);
}
```

## Fulfillment Actions (examples)

- Provision access to services
- Trigger shipment / logistics
- Save payment + line item copy to your DB
- Send custom receipt (if Stripe receipts disabled)
- Reconcile adjustable quantities
- Update inventory / stock records

## Landing Page Configuration

| Mode | Param | Template var |
| --- | --- | --- |
| Hosted Checkout | `success_url` | `{CHECKOUT_SESSION_ID}` |
| Embedded Checkout | `return_url` | `{CHECKOUT_SESSION_ID}` |
| Payment Links (API) | `after_completion.redirect.url` | `{CHECKOUT_SESSION_ID}` |
| Payment Links (Dashboard) | After Payment tab → Don't show confirmation page | `{CHECKOUT_SESSION_ID}` |

> Hosted Checkout waits up to 10s for webhook response before redirecting. Not supported for organization-level webhook endpoints.

## Delayed vs Immediate Payment Methods

| | Immediate (cards) | Delayed (ACH, bank transfers) |
| --- | --- | --- |
| Event on session complete | `checkout.session.completed` with `payment_status: 'paid'` | `checkout.session.completed` with `payment_status: 'unpaid'` → later `checkout.session.async_payment_succeeded` |
| Fulfill on | `checkout.session.completed` | `checkout.session.async_payment_succeeded` |

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-checkout-dashboard-payment-methods]] — Delayed notification PMs list (Bacs, ACH, etc.)

## Raw Sources

- [[stripe-checkout-after-payment-2025]] — Navigation index: fulfill orders, redirect behavior, abandoned carts, GA4, receipts
- [[stripe-checkout-fulfillment-2025]] — Full fulfillment guide: fulfill_checkout function, webhook handler, dual-trigger pattern, Stripe CLI, landing page config, hosted + embedded variants

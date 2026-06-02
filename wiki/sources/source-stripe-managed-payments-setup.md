---
title: "Build a Checkout Integration with Managed Payments"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-managed-payments-setup-2025.md"
tags: [stripe, managed-payments, checkout, merchant-of-record, subscriptions, one-time-payments, tax-behavior, webhooks]
---

## Summary

Full integration guide for Managed Payments with Stripe Checkout. Covers product/price creation (subscriptions and one-time), Checkout Session creation with `managed_payments.enabled`, webhooks, testing, and tax behavior configuration.

## Prerequisites

- Accept Managed Payments ToS in Dashboard
- API version `2025-03-31.basil` or later
- All products in cart must be eligible (one ineligible product blocks entire session)

## Key API Param

```javascript
// The single flag that enables Managed Payments on a Checkout Session
stripe.checkout.sessions.create({
    line_items: [{ price: priceId, quantity: 1 }],
    managed_payments: { enabled: true },   // KEY
    mode: 'subscription',                  // or 'payment'
    success_url: 'https://example.com/success',
})
```

## Product/Price Setup

- Products must have an eligible `tax_code` (labeled "Eligible for Managed Payments" in Dashboard)
- Dashboard preview pane shows tax amount by customer location in real time
- Subscriptions: set `recurring.interval` on price
- One-time: omit `recurring` on price

## Webhooks

| Event | When |
| --- | --- |
| `checkout.session.completed` | Successful checkout |
| `checkout.session.async_payment_succeeded` | Delayed PM (e.g., ACH) succeeds |
| `checkout.session.async_payment_failed` | Delayed PM fails |

Use webhooks instead of relying on success page redirect for post-payment logic.

## Tax Behavior

Default = exclusive (tax added on top of price). Override:
- Set `tax_behavior` on the Price object, OR
- Dashboard → Tax → "Include tax in prices" setting

## Important Notes

- **Customer authorization caveat**: subscription PM authorized for Managed Payments only — need separate consent to charge same PM outside Managed Payments
- **All-or-nothing**: ALL products in session must be Managed Payments eligible
- **Link test passcode**: `000000`; test purchases don't appear in Link app (live mode only)

## Related Pages

- [[stripe-managed-payments]] — concept page
- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-managed-payments-how-it-works]] — operational details

## Raw Sources

- [[stripe-managed-payments-setup-2025]] — verbatim integration guide (~531 lines)

---
title: "Stripe Docs — Set up future payments using Elements and Link"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-link-save-and-reuse-2025.md"
tags: [stripe, link, setup-intents, save-and-reuse, payment-element, link-authentication-element, accounts-v2, off-session]
---

## Summary

SetupIntent counterpart to the PaymentIntent custom checkout guide. Same three email strategies (pass/collect/LAE) + Accounts v2 dual-path throughout. Key difference: saves payment details without immediate charge; charges later off-session.

## Key Differences from PaymentIntent Guide

| Aspect | PaymentIntent Guide | This Guide (SetupIntent) |
| --- | --- | --- |
| API | PaymentIntents | SetupIntents |
| Submit | `stripe.confirmPayment()` | `stripe.confirmSetup()` |
| Accounts v2 | No | Yes — `customer_account` throughout |
| Charge timing | Immediate | Later (off-session) |
| Manual capture | Yes (7-day window) | N/A |

## Server-side Flow

1. Create Customer (`customers.create`) or Account (`v2.core.accounts.create`)
2. Create SetupIntent with `customer`/`customer_account` and `payment_method_types: ['card', 'link']`
3. Return `client_secret` to client

## Charge Later

```js
// List saved PMs
stripe.paymentMethods.list({ customer: '{{ID}}', type: 'link' })

// Create and immediately confirm PaymentIntent
stripe.paymentIntents.create({
  confirm: true,
  payment_method: '{{PM_ID}}',
  customer: '{{CUSTOMER_ID}}',  // or customer_account
  off_session: true,
  amount, currency,
})
```

## CDN Assets

All 7 images reused from `source-stripe-add-link-elements-integration`:
- `stripe-link-in-payment-element.png`, `stripe-link-lape-unregistered.png`, `stripe-link-collect-email-returning.png`, `stripe-link-with-elements.png`, `stripe-link-prefill-pe-new-user.png`, `stripe-link-prefill-lae-new-user.png`, `stripe-link-appearance-example.png`

## Related Pages

- [[stripe-link]] — Link concept page (Custom Checkout Page section)
- [[source-stripe-add-link-elements-integration]] — PaymentIntent counterpart (immediate payment)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-link-save-and-reuse-2025]] — verbatim webpage content (1,263 lines)

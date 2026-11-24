---
title: "Stripe Recurring Payments Overview"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-recurring-payments-overview-2025.md"
tags: [stripe, recurring-payments, subscriptions, invoices, installments, billing, checkout, elements, payment-links]
---

## Summary

Stripe's comprehensive guide to recurring payment options. Covers use cases, payment types (subscriptions, invoices, saved PM charges), product comparison (Payment Links → API), and detailed subscription creation via Dashboard, Payment Links, Checkout, and Elements.

## Use Cases

1. Accept recurring payments
2. Split purchases into installments
3. Enable customers to manage subscriptions (customer portal)
4. Accept recurring donations
5. Migrate existing subscriptions to Stripe

## Three Payment Types

| Type | Key Feature |
| --- | --- |
| **Subscriptions** (Stripe Billing) | Full lifecycle management, Dashboard + API, Connect support |
| **Recurring invoices** | Hosted by Stripe, no website required, Stripe Tax support |
| **Charges on saved PMs** | PaymentIntents API, `save_during_payment` or `save_and_reuse` patterns |

**Installments caveat**: some markets prohibit subscription schedules for installment plans (may be mistaken for ongoing subscriptions).

## Product Comparison

| Product | Code required | Website | Notes |
| --- | --- | --- | --- |
| Payment Links | None | No | Share via SMS/email/social |
| Invoicing | Minimal/none | No | Stripe hosts payment page |
| Subscriptions | None/optional | No | Most flexible |
| Checkout | Minimal | Yes (Stripe hosts) | Stripe Tax supported |
| Elements | More | Yes | Full appearance customization |
| API | Most | Yes | Own UI, maximum control |

## Subscription Creation Patterns

### Dashboard
Create via Dashboard → Subscriptions → +Create subscription.

### Payment Links
Select "Sell a subscription" when creating the payment link.

### Checkout
```javascript
stripe.checkout.sessions.create({
    mode: 'subscription',
    line_items: [{ price: priceId, quantity: 1 }],
    subscription_data: { billing_mode: { type: 'flexible' } },
    success_url: 'https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
})
```

### Elements (Subscriptions API)
```javascript
// Accounts v2
stripe.subscriptions.create({
    customer_account: customerAccountId,  // Accounts v2
    items: [{ price: priceId }],
    payment_behavior: 'default_incomplete',
    payment_settings: { save_default_payment_method: 'on_subscription' },
    billing_mode: { type: 'flexible' },
    expand: ['latest_invoice.confirmation_secret'],
})

// Customers v1: use customer: customerId instead
```

Key: `payment_behavior: 'default_incomplete'` creates inactive subscription awaiting payment; `expand: ['latest_invoice.confirmation_secret']` returns client_secret for frontend confirmation.

## Key Facts

- `billing_mode: { type: 'flexible' }` — new flexible billing mode on subscriptions
- Accounts v2 uses `customer_account` instead of `customer`
- `expand: ['latest_invoice.confirmation_secret']` replaces older `expand: ['latest_invoice.payment_intent']` pattern
- Hosted invoice scheduled payments: US only

## Related Pages

- [[recurring-payments]] — generic recurring payments concept page
- [[stripe-subscriptions]] — Stripe subscriptions concept page

## Raw Sources

- [[stripe-recurring-payments-overview-2025]] — verbatim guide (~1500+ lines, full product comparison + code examples)

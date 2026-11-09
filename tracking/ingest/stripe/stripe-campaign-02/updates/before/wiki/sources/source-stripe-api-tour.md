---
title: "Stripe API Tour"
type: source
date_ingested: 2026-04-19
original_format: webpage
raw_files:
  - "stripe-api-tour-2025.md"
tags: [stripe, payment-intents, payment-methods, charge, checkout, webhooks, events]
---

## Summary

Conceptual overview of the Stripe API — how core objects fit together, the PaymentIntent lifecycle, and best practices for combining objects. First Stripe source in this wiki.

## Key Takeaways

- **PaymentIntent** is the central object for every modern Stripe payment; tracks the full lifecycle
- **Retry rule**: failed payment → confirm same PaymentIntent with new payment details (don't create a new one); improves conversion
- **Charge** is created at confirmation to represent one specific money movement attempt
- **Event objects** represent activity; webhook endpoints respond to them; Checkout/Payment Links have pre-written responses
- **5 integration paths**: Payment Intents (direct), Stripe Elements, Stripe Checkout, Payment Links, Subscriptions/Invoicing

## PaymentIntent Lifecycle

```
requires_payment_method
  → requires_confirmation
    → processing
      → succeeded
      → requires_payment_method (retry with new payment details)
```

## Key Objects

| Object | Role |
| --- | --- |
| PaymentIntent | Tracks intent + lifecycle of one payment |
| PaymentMethod | Stores payment credentials (card, bank, etc.) |
| Charge | One specific attempt to move money |
| SetupIntent | Saves a PaymentMethod for future use without charging |
| Event | Represents activity (charge succeeded, failed, etc.) |
| Customer | Optional; tracks customer info and saved payment methods |
| Subscription | Manages recurring billing |
| Product / Price | Catalog for what's being sold |

## Related Pages

- [[stripe]] — Stripe company page
- [[recurring-payments]] — generic recurring payments concept
- [[disputes]] — generic disputes concept

## Raw Sources

- [[stripe-api-tour-2025]] — Stripe API tour: core object philosophy, PaymentIntent lifecycle, Charge, PaymentMethod, Elements, Events/webhooks, 5 integration paths

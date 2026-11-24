---
title: "Stripe Payment Methods API"
type: source
date_ingested: 2026-04-19
original_format: webpage
raw_files:
  - "stripe-payment-methods-api-2025.md"
tags: [stripe, payment-methods, webhooks, ach, sepa, bank-debit, customer-actions]
---

## Summary

Reference for the Stripe Payment Methods API — how PaymentMethod objects work, customer action types, immediate vs delayed notification, single-use vs reusable payment methods, and webhook events.

## Key Takeaways

- **PaymentMethod object**: contains payment details (card expiry, billing address) but NOT transaction info (amount/currency); has `type` field + type-specific hash (e.g. `sepa_debit: {}`)
- **Create PaymentMethods via Stripe.js** — recommended for safely handling sensitive payment data
- **Cards (excl. 3DS)**: no customer action; immediate notification
- **ACH/bank debits**: delayed notification; order stays `processing` until resolved; hold order in pending state
- **Single-use** (some bank transfers): consumed after attempt; cannot attach to Customer
- **Reusable** (cards, bank debits): set up for future use to reduce declines and auth friction

## Customer Action Types (via `next_action`)

| Type | Example |
| --- | --- |
| Redirect to bank | Authorize via bank's online service |
| One-time code | Microdeposits — customer provides code |
| Push funds | Bank transfers — customer sends funds |

## Immediate vs Delayed Notification

| Type | PaymentIntent status on success | Example |
| --- | --- | --- |
| Immediate | `succeeded` (guaranteed funds) | Cards |
| Delayed | `processing` → `succeeded`/`requires_payment_method` | ACH, SEPA debits |

For delayed: hold order in pending state; don't fulfill until `payment_intent.succeeded` webhook.

## Single-use vs Reusable

| | Attach to Customer | Example |
| --- | --- | --- |
| Reusable | Yes | Cards, bank debits |
| Single-use | No (consumed after attempt) | Some bank transfers |

## PaymentMethod Object Structure

```json
{
  "id": "pm_123",
  "type": "sepa_debit",
  "billing_details": { "email": "...", "name": "..." },
  "sepa_debit": { "bank_code": "...", "last4": "3000", "country": "FR" }
}
```

## Webhook Events

| Event | Trigger | Action |
| --- | --- | --- |
| `payment_intent.processing` | Payment submitted (delayed methods only) | Wait |
| `payment_intent.succeeded` | Payment succeeded | Fulfill order |
| `payment_intent.payment_failed` | Payment failed | Notify customer for new method |

## Related Pages

- [[stripe]] — Stripe company page
- [[source-stripe-payment-intents]] — PaymentIntents + SetupIntents lifecycle

## Raw Sources

- [[stripe-payment-methods-api-2025]] — Payment Methods API: 3 customer action types, immediate vs delayed notification, single-use vs reusable, PaymentMethod object structure, webhook events

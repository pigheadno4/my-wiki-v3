---
title: "Stripe — Card Payments Without Bank Authentication"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-payments-without-auth-2026.md"
tags: [stripe, payment-intent, card-element, legacy, us-canada, error-on-requires-action]
---

## Summary

Legacy US/CA-only integration using CardElement + `createPaymentMethod`. Declines any payment requiring bank authentication. No webhooks needed.

## Key Characteristics

- **US/CA only**: banks in these regions rarely require 2FA
- **Synchronous**: payment succeeds or fails immediately
- **`error_on_requires_action: true`**: Stripe auto-fails payments requiring authentication
- **No webhooks required** for post-payment actions

## Flow

1. Client: `elements.create('card')` → `stripe.createPaymentMethod({ type: 'card', card: cardElement })` → send `paymentMethod.id` to server
2. Server: `stripe.paymentIntents.create({ payment_method: id, confirm: true, error_on_requires_action: true })`
3. Return `{ success: true }` or `{ error: message }`

## Comparison to Global Integration

| Feature | This | Global |
| --- | --- | --- |
| US/CA support | ✓ | ✓ |
| Bank auth payments | Declined | Handled |
| Webhooks needed | No | Yes (recommended) |
| Global customers | ✗ | ✓ |

## Test Cards

- `4242424242424242` → succeeds
- `4000000000009995` → insufficient funds
- `4000002500003155` → `authentication_not_handled` (fails as expected)

## Related Pages

- [[stripe-payment-intents]] — concept page (updated with legacy pattern note)

## Raw Sources

- [[stripe-payments-without-auth-2026]] — verbatim card payments without auth guide (418 lines)

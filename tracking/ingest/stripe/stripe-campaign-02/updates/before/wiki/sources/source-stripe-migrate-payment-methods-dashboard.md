---
title: "Migrate Payment Methods to the Dashboard"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-migrate-payment-methods-dashboard-2025.md"
tags: [stripe, payment-methods, dashboard, dynamic-payment-methods, payment-intents, checkout-sessions, delayed-notification, apple-pay, google-pay, webhooks, testing]
---

## Summary

Migration guide for switching both Checkout Sessions and Payment Intents integrations from hardcoded `payment_method_types` to Dashboard-managed dynamic payment methods. Mostly parallel content for both API paths, with differences in webhook event names for delayed notification handling.

> See also [[source-stripe-checkout-dashboard-payment-methods]] which covers the Checkout Sessions path in more depth.

## Migration Step (Both Paths)

Remove `payment_method_types` from your Intent/Session creation call. Non-default payment methods (bank redirects) are initially **disabled** after migration — must re-enable in Dashboard.

## Apple Pay / Google Pay Defaults

- **Apple Pay**: enabled by default
- **Google Pay**: **disabled** by default
- Google Pay won't show even if enabled when automatic tax is on without shipping address collection

## Delayed Notification Payment Methods

9 specific methods requiring additional webhook handling:
Bacs Direct Debit, Bank transfers, Boleto, Canadian pre-authorized debits, Konbini, OXXO, Pay by Bank, SEPA Direct Debit, ACH Direct Debit

### Checkout Sessions Webhook Events

| Event | Description | Action |
| --- | --- | --- |
| `checkout.session.completed` | Customer authorized payment | Create order; check `payment_status === 'paid'` before fulfilling |
| `checkout.session.async_payment_succeeded` | Funds cleared | Fulfill order |
| `checkout.session.async_payment_failed` | Payment declined | Email customer to retry |

### Payment Intents Webhook Events

| Event | Action |
| --- | --- |
| `payment_intent.succeeded` | Fulfill order |
| `payment_intent.payment_failed` | Handle failure |

## Test Credentials (Both Paths)

### Cards
| Card | Scenario |
| --- | --- |
| `4242424242424242` | Success, no auth |
| `4000002500003155` | Requires 3DS authentication |
| `4000000000009995` | Declined (insufficient_funds) |
| `6205500000000000004` | UnionPay (13–19 digit variable length) |

### Bank Debits
| Method | Success account | Fail account |
| --- | --- | --- |
| BECS | `900123456` / BSB `000000` | `111111113` / BSB `000000` |
| SEPA | `AT321904300235473204` | `AT861904300235473202` |

- Redirect-based methods: use test redirect page → "Complete test payment" or "Fail test payment"
- Alipay: use any redirect-based PM → complete on redirect page
- BLIK: use email patterns to simulate failures

## Related Pages

- [[source-stripe-checkout-dashboard-payment-methods]] — Checkout Sessions path in depth
- [[stripe-checkout]] — Checkout concept page
- [[stripe-payment-intents]] — Payment Intents concept page

## Raw Sources

- [[stripe-migrate-payment-methods-dashboard-2025]] — verbatim migration guide (both API paths)

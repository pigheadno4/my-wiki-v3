---
title: "Stripe Checkout: Migrate Payment Methods to the Dashboard"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-payment-methods-2025.md"
  - "stripe-checkout-dashboard-payment-methods-2025.md"
tags: [stripe, checkout, payment-methods, dynamic-payment-methods, dashboard, apple-pay, google-pay, delayed-notification, async-payments, webhooks]
---

## Summary

Guide for migrating Stripe Checkout from manually specified `payment_method_types` to Dashboard-managed dynamic payment methods. Covers Apple Pay / Google Pay defaults, the overflow menu UI, delayed notification payment method handling, and a comprehensive test table.

## Key Takeaways

- **Migration**: remove `payment_method_types` param → uses Dashboard settings; non-default PMs (bank redirects) turn off on migration and must be re-enabled in Dashboard
- **Dynamic selection**: Stripe picks PMs based on currency, transaction amount, restrictions, and customer location; popular PMs shown prominently, others in overflow menu
- **Apple Pay**: enabled by default; **Google Pay**: disabled by default
- **Google Pay filtered**: when `automatic_tax` enabled without `shipping_address_collection`
- **Delayed notification PMs** (2–14 day confirmation): Bacs, bank transfers, Boleto, Canadian PAD, Konbini, OXXO, Pay by Bank, SEPA, ACH Direct Debit

## Delayed Notification Payment Methods

When adding delayed notification PMs, must handle 3 events (not just `checkout.session.completed`):

| Event | Description | Action |
| --- | --- | --- |
| `checkout.session.completed` | Customer submitted form | Create order; check `payment_status === 'paid'` before fulfilling |
| `checkout.session.async_payment_succeeded` | Funds cleared | Fulfill order |
| `checkout.session.async_payment_failed` | Payment declined/failed | Email customer to retry |

> **Key pattern**: on `checkout.session.completed`, check `session.payment_status`. If `'paid'` → fulfill immediately. If not (e.g., `'unpaid'` for debit) → wait for async event.

## Test Coverage

| Category | Payment methods |
| --- | --- |
| Cards | 4242... (success), 4000 0025 0000 3155 (3DS), 4000...9995 (decline), UnionPay (variable length) |
| Wallets | Alipay (redirect + immediate) |
| Bank redirects | BECS Direct Debit, Bancontact/EPS/iDEAL/P24, Pay by Bank, BLIK (multiple failure modes) |
| Bank debits | SEPA Direct Debit (success + failure) |
| Vouchers | Boleto, OXXO |

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-checkout-sessions]] — Checkout Sessions API, async payment events

## Raw Sources

- [[stripe-checkout-payment-methods-2025]] — Manage payment methods: dynamic vs manual (payment_method_types), Dashboard settings
- [[stripe-checkout-dashboard-payment-methods-2025]] — Migrate to Dashboard: migration steps, Apple Pay/Google Pay defaults, delayed notification webhook pattern, full test table

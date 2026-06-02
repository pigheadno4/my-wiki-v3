---
title: "Stripe Docs — Custom payment methods"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-custom-payment-methods-2025.md"
tags: [stripe, custom-payment-methods, cpmt, third-party, payment-element, connect, compliance]
---

## Summary

Overview of Stripe Custom Payment Methods (CPM) — enabling payment methods processed entirely outside Stripe to be surfaced in the Stripe ecosystem (Payment Element, Subscriptions, Invoicing) for unified reporting and billing workflows.

## Key Facts

- **PM type in API**: `type: 'custom'`, `custom[type]` = `cpmt_...` ID (configured in Dashboard)
- **CPM type IDs not API-retrievable**: store in your own database; retrieve during payment method creation
- **50+ presets** for common external payment methods; or set custom display name + logo
- **Transactions recorded to Stripe** optionally via payment-record API for unified reporting

## Integration Support Matrix

| Integration | Supported |
| --- | --- |
| Connect | ✓ |
| Payment Element | ✓ |
| Mobile Payment Element | ✓ |
| Subscriptions | ✓ |
| Invoicing | ✓ |
| Customer Portal | ✓ |
| Checkout | ✗ |
| Payment Links | ✗ |
| Express Checkout Element | ✗ |

## Connect Support

Platform can create CPMs in connected accounts using its own CPM types or the connected account's CPM types. Pass `stripeAccount` header when creating the payment method.

## Compliance

- **Restricted methods**: crypto payment methods in Indonesia and Thailand are prohibited
- **Marks requirements**: must follow PM provider brand guidelines; cannot modify Marks or use one provider's Marks for another
- **Stripe disclaimer**: Stripe is not responsible for CPM transactions (disputes, refunds, settlements, funds flows); merchant bears full responsibility for PSP agreement compliance and correct CPM presentation; must immediately remove CPMs if PSP agreement terminates

## Related Pages

- [[stripe-custom-payment-methods]] — concept page (full setup flow, display types, mobile integration)
- [[source-stripe-payment-element-custom-payment-methods]] — primary implementation reference
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-custom-payment-methods-2025]] — verbatim webpage content

---
title: "Use Payment Links with Managed Payments"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-managed-payments-payment-links-2025.md"
tags: [stripe, managed-payments, payment-links, merchant-of-record, variable-pricing, subscriptions]
---

## Summary

Guide for using Managed Payments with Payment Links (no-code and API paths). Same `managed_payments.enabled` flag as Checkout but applied to `paymentLinks.create()`. Includes unique rules: immutable MoR state, iOS Stripe app restriction, variable pricing, and additional unsupported params.

## Key API Param

```javascript
stripe.paymentLinks.create({
    managed_payments: { enabled: true },
    line_items: [{ price: priceId, quantity: 1 }],
    // up to 20 line items for flat rate; 1 for variable pricing
})
```

## Variable Pricing

```javascript
// Create variable price
stripe.prices.create({
    currency: 'usd',
    custom_unit_amount: { enabled: true },
    product: productId,
})
// then use that price in paymentLinks.create
```

## Subscription via Payment Links

Specify a price with `type=recurring` in `line_items`. Use `subscription_data` for config (trials, etc.).

## Unique Rules (vs Checkout)

- **Immutable MoR state**: cannot enable on existing links; cannot disable after enabling — must create new link
- **iOS Stripe app**: cannot create Managed Payments payment links via iOS Stripe app — use web Dashboard
- **Up to 20 line items** for flat rate; **1 line item** for variable/customer-defined pricing

## Unsupported Parameters (Payment Links)

| Category | Parameters to remove |
| --- | --- |
| Tax | `automatic_tax`, `tax_id_collection` |
| Payment methods | `payment_method_types` |
| Shipping | `shipping_address_collection`, `shipping_options` |
| Connect | `application_fee_amount`, `application_fee_percent`, `on_behalf_of`, `transfer_data`, `payment_intent_data.transfer_group` |
| Post-sale | `subscription_data.invoice_settings`, `invoice_creation` |
| Statement descriptors | `payment_intent_data.statement_descriptor`, `payment_intent_data.statement_descriptor_suffix` |
| Consent | `consent_collection.payment_method_reuse_agreement.position` |
| Submit type | `submit_type='donate'`, `submit_type='book'` |
| Customization | `custom_text` (standardized checkout, no custom text) |

## Related Pages

- [[stripe-managed-payments]] — concept page
- [[stripe-payment-links]] — Payment Links concept page
- [[source-stripe-managed-payments-setup]] — Checkout variant (same managed_payments.enabled, different object)
- [[source-stripe-inapp-digital-goods-payment-links]] — non-MoR Payment Links for iOS digital goods

## Raw Sources

- [[stripe-managed-payments-payment-links-2025]] — verbatim guide (~221 lines)

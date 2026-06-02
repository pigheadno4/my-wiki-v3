---
title: "Update a Checkout Integration to Use Managed Payments"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-managed-payments-update-checkout-2025.md"
tags: [stripe, managed-payments, checkout, migration, unsupported-parameters, subscriptions, one-time-payments]
---

## Summary

Migration guide for adding Managed Payments to an existing Checkout integration. Key value: comprehensive tables of parameters that must be removed when enabling Managed Payments. Existing subscriptions cannot be migrated (new only).

> For new integrations, see [[source-stripe-managed-payments-setup]].

## Critical Caveat

**Existing subscriptions are NOT eligible** — during preview, only new subscriptions purchased through a Managed Payments Checkout Session are supported. Cannot retrofit existing subscriptions.

## Steps to Migrate

1. Update each product's `tax_code` to an eligible Managed Payments code
2. Add `managed_payments: { enabled: true }` to Checkout Session creation
3. Remove unsupported parameters (see tables below)

## Inline Tax Code (price_data pattern)

```javascript
// If creating products inline in the Checkout Session:
price_data: {
    product_data: {
        name: 'My Product',
        tax_code: '{{TAX_CODE}}',  // add this
    },
    // ...
}
```

## Unsupported Parameters — Subscriptions

| Category | Parameters to remove |
| --- | --- |
| Adaptive Pricing | `adaptive_pricing` (always on) |
| Tax | `automatic_tax`, `tax_id_collection`, `subscription_data.default_tax_rates` |
| Payment methods | `payment_method_configuration`, `payment_method_options`, `payment_method_types` |
| Customer update | `customer_update[name]`, `customer_update[address]` (MP always collects) |
| Shipping | `shipping_address_collection`, `shipping_options` (digital only) |
| Connect | `subscription_data.application_fee_percent`, `subscription_data.on_behalf_of`, `subscription_data.transfer_data` |
| Post-sale | `subscription_data.invoice_settings`, `invoice_creation` (MP handles) |

## Unsupported Parameters — One-Time Payments

| Category | Parameters to remove |
| --- | --- |
| Tax | `automatic_tax`, `tax_id_collection` |
| Payment methods | `excluded_payment_method_types`, `adaptive_pricing`, `payment_intent_data.setup_future_usage`, `payment_method_configuration`, `payment_method_options.{pm}.setup_future_usage`, `payment_method_types` |
| Customer update | `customer_update[name]`, `customer_update[address]` |
| Shipping | `shipping_address_collection`, `shipping_options`, `payment_intent_data.shipping` |
| Connect | `payment_intent_data.application_fee_amount`, `payment_intent_data.on_behalf_of`, `payment_intent_data.transfer_data`, `payment_intent_data.transfer_group` |
| Post-sale | `invoice_creation`, `payment_intent_data.statement_descriptor`, `payment_intent_data.statement_descriptor_suffix`, `payment_intent_data.receipt_email` |

## Related Pages

- [[stripe-managed-payments]] — concept page
- [[source-stripe-managed-payments-setup]] — new integration guide (same managed_payments.enabled param)

## Raw Sources

- [[stripe-managed-payments-update-checkout-2025]] — verbatim migration guide (~280 lines)

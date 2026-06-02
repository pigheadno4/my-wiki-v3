---
title: "Stripe Checkout: Collect Taxes"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-taxes-2025.md"
tags: [stripe, checkout, tax, stripe-tax, automatic-tax, accounts-v2, checkout-sessions]
---

## Summary

Guide for enabling Stripe Tax on Checkout sessions. Covers new vs existing customer flows, Accounts v2 vs Customers v1 API paths, `customer_update` for address propagation, and wallet-specific constraints.

## Key Takeaways

- `automatic_tax: { enabled: true }` — single param enables Stripe Tax on any Checkout session
- **Tax location priority**: shipping address > billing address (fallback)
- **New customers**: Checkout auto-creates customer + saves address; no extra params needed
- **Existing customers**: 2 paths — use existing address on customer, or use address collected during checkout
- **Accounts v2** (GA for Connect, public preview otherwise): `customer_account` param; verify `automatic_indirect_tax.status = 'active'`; recommended over Customers v1
- **Customers v1**: `customer` param; verify `tax.automatic_tax = 'supported'` or `'not_collecting'`
- **Address propagation**: `customer_update.shipping: 'auto'` (shipping sessions) or `customer_update.address: 'auto'` (billing-only sessions) — copies checkout-entered address to the customer record
- **Google Pay**: requires shipping address collection or existing customer with saved shipping address
- **Apple Pay**: requires browser supporting Apple Pay v12+
- **Result**: `total_details.amount_tax` on Checkout Session object; also viewable in Dashboard

## Params Reference

| Param | Purpose |
| --- | --- |
| `automatic_tax.enabled: true` | Enable Stripe Tax |
| `customer` / `customer_account` | Attach existing customer (v1 / v2) |
| `customer_update.shipping: 'auto'` | Copy checkout shipping address to customer |
| `customer_update.address: 'auto'` | Copy checkout billing address to customer |
| `shipping_address_collection` | Required for Google Pay + Tax to coexist |

## Accounts v2 vs Customers v1

| | Accounts v2 | Customers v1 |
| --- | --- | --- |
| Param | `customer_account` | `customer` |
| Validate addresses | `automatic_indirect_tax.status = 'active'` | `tax.automatic_tax = 'supported'/'not_collecting'` |
| Shipping field | `configuration.customer.shipping.address` | `shipping.address` |
| Billing field | `identity.individual.address` or `identity.business_details.address` | `address` |
| Status | GA (Connect) / public preview (others) | Generally available |
| Recommendation | Preferred for new integrations | Legacy |

## Related Pages

- [[stripe-tax]] — Stripe Tax concept page
- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-checkout-shipping]] — ShippingRate API (shipping rates, delivery estimates, shipping tax codes)

## Raw Sources

- [[stripe-checkout-taxes-2025]] — Collect taxes: automatic_tax param, new vs existing customers, Accounts v2 + Customers v1 paths, customer_update, Google Pay / Apple Pay constraints

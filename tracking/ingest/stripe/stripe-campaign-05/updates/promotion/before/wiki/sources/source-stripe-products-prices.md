---
title: "Stripe Products and Prices"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-products-prices-2025.md"
  - "stripe-manage-products-prices-2025.md"
tags: [stripe, products, prices, catalog, subscriptions, checkout, invoices, pricing-models]
---

## Summary

How Stripe's Product and Price objects model a business catalog. Core resources for Checkout, Payment Links, Subscriptions, Invoices, and Quotes integrations.

## Key Takeaways

- **Custom product IDs** — unlike most Stripe resources, you can choose your own product ID (use internal system IDs for easy reconciliation)
- **Prices are immutable** — never modify `unit_amount`; archive (`active: false`) and create new price instead
- **`price_data`** — creates temporary Price objects invisible in Dashboard catalog; use for dynamic amounts (e.g. donations); Product objects may persist
- **Max recurring interval**: 3 years
- **Subscription constraint**: all prices must share same `recurring.interval` + `recurring.interval_count` (unless flexible billing mode)
- **Archive not delete**: products/prices can't be deleted in general; only archive; Stripe stores indefinitely for transaction history

## Product vs Price

| | Product | Price |
| --- | --- | --- |
| Defines | What you sell | How much + how often |
| ID | Custom (you choose) | Stripe-generated |
| Required fields | Name | Amount, currency, product |
| Optional | Description, image, tax code | Default price, tax_behavior |

## Price Types

| Type | Notes |
| --- | --- |
| One-time | Single charge |
| Recurring | Subscription billing; specify interval |
| Inline (`price_data`) | Dynamic amount at checkout; temp Price object, invisible in Dashboard |
| Pay-what-you-want | Customer sets amount; one-time only (no recurring) |
| Multi-currency | One Price object for multiple currencies |
| Tiered / usage-based | Configure with different `unit_amount` tiers |

## Compatibility Table (key entries)

| Feature | Checkout | Payment Links | Quotes | Subscriptions | Invoices |
| --- | --- | --- | --- | --- | --- |
| Product images | ✓ | ✓ | Ignored | Ignored | Ignored |
| Recurring prices | ✓ | ✓ | ✓ | ✓ | ✓ |
| Multi-currency prices | ✓ | ✓ | Ignored | ✓ | Ignored |
| Tiered prices | ✓ | **Disallowed** | ✓ | ✓ | ✓ |
| Usage-based prices | ✓ | **Disallowed** | ✓ | ✓ | ✓ |
| Decimal amounts | ✓ | **Disallowed** | ✓ | ✓ | ✓ |
| Customer chooses price | ✓ | ✓ | **Disallowed** | **Disallowed** | **Disallowed** |

**Disallowed** = cannot use that product/price with this API at all.
**Ignored** = feature has no effect but product/price still usable.

## How Each API Uses Prices

- **Checkout**: specify price `id` per line item; renders product name + image
- **Payment Links**: Dashboard-created; renders product name + image
- **Subscriptions**: price must be recurring; billing period = `recurring.interval`; multiple prices OK if same interval
- **Quotes**: models one-off invoice or subscription; auto-creates invoices/subscriptions on acceptance
- **Invoices**: specify price `id` per line item; uses `product.name` in invoice PDF

## Related Pages

- [[stripe]] — Stripe company page
- [[source-stripe-checkout-sessions]] — Checkout Sessions API
- [[paypal-subscriptions]] — PayPal's equivalent subscription/plan model

## Raw Sources

- [[stripe-products-prices-2025]] — Products & Prices: custom IDs, price immutability, price_data, compatibility table, subscription constraints, archive rules
- [[stripe-manage-products-prices-2025]] — Manage Products & Prices: CRUD operations, lookup_key + transfer_lookup_key, multi-currency per-API rules, rounding per line item, delete rules, copy-to-live-mode (one-time), import sync pattern

---
title: "Stripe Products and Prices"
type: source
date_ingested: 2026-04-20
date_updated: 2026-11-22
original_format: webpage
raw_files:
  - "stripe-products-prices-2025.md"
  - "stripe-manage-products-prices-2025.md"
tags: [stripe, products, prices, catalog, subscriptions, checkout, invoices, pricing-models]
---

## Summary

How Stripe's Product and Price objects model a business catalog. Core resources for Checkout, Payment Links, Subscriptions, Invoices, and Quotes integrations.

The April 20, 2026 overview at https://docs.stripe.com/products-prices/how-products-and-prices-work describes catalog objects and compatibility. The April 20 and November 7, 2026 captures of https://docs.stripe.com/products-prices/manage-prices describe Dashboard and API catalog management. Each guide has its own scope.

- **Custom product IDs** — unlike most Stripe resources, you can choose your own product ID (use internal system IDs for easy reconciliation)
- **Prices are immutable** — never modify `unit_amount`; archive (`active: false`) and create new price instead
- **`price_data`** — creates temporary Price objects invisible in Dashboard catalog; use for dynamic amounts (e.g. donations); Product objects may persist
- **Max recurring interval**: 3 years
- **Subscription constraint**: all prices must share same `recurring.interval` + `recurring.interval_count` (unless flexible billing mode)
- **Archive not delete**: products/prices can't be deleted in general; only archive; Stripe stores indefinitely for transaction history

- **Product.** Give the Product a name. An optional custom ID can map it to your own catalog. Optional description, image and tax code affect downstream integrations. The management guide requires at least one Price to save a Product in the Dashboard. This is a Dashboard save requirement. The API also documents creating a Product with `default_price_data` in one request.
- **Price.** A Price belongs to a Product and carries the amount, currency, and recurrence or other pricing model. One Product can have multiple Prices. A default Price must be active, and the first Price added with a new Dashboard Product becomes the default.
- **Change an amount.** Create a replacement Price, switch to its ID and archive the old Price with `active=false`. The guide lists `metadata`, `nickname` and `active` in its generic edit note, separately illustrates `lookup_key` in a Price update, and documents adding currency options to an existing Price in the Dashboard. These passages do not establish an exhaustive edit-field list.
- **Archive.** Archiving a Product or Price prevents adding that item to new invoices or subscriptions. Existing subscriptions using the archived item remain active until canceled. Both archive passages say existing Payment Links using the Product are deactivated, including the paragraph about a Price. For an existing Product, archive prose links to updating `active=false`, while both archive examples submit a Product-create request with `active=false`. The create examples do not demonstrate updating the existing Product. Unarchive by updating `active=true`.
- **Delete.** The management guides say only Products without associated Prices can be deleted, while their Dashboard paragraph says to delete or archive an associated Price first. These passages leave the archive-only deletion path unresolved. The Dashboard can delete an unused Price. The Price API documents archival instead of deletion. Stripe retains archived catalog information for transaction history.

| | Product | Price |
| --- | --- | --- |
| Defines | What you sell | How much + how often |
| ID | Custom (you choose) | Stripe-generated |
| Required fields | Name | Amount, currency, product |
| Optional | Description, image, tax code | Default price, tax_behavior |

| Type | Scope |
| --- | --- |
| One-time | Single charge |
| Recurring | Subscription billing; specify interval |
| Inline (`price_data`) | Dynamic amount at checkout; temp Price object, invisible in Dashboard |
| Pay-what-you-want | Customer sets amount; one-time only (no recurring) |
| Multi-currency | One Price object for multiple currencies |
| Tiered / usage-based | Configure with different `unit_amount` tiers |

## April 2026 overview compatibility

These entries are the same in the April and November catalog overviews.

| Feature | Checkout | Payment Links | Quotes | Subscriptions | Invoices |
| --- | --- | --- | --- | --- | --- |
| Product images | ✓ | ✓ | Ignored | Ignored | Ignored |
| Recurring prices | ✓ | ✓ | ✓ | ✓ | ✓ |
| Multi-currency prices | ✓ | ✓ | Ignored | ✓ | Ignored |
| Tiered prices | ✓ | Disallowed | ✓ | ✓ | ✓ |
| Usage-based prices | ✓ | Disallowed | ✓ | ✓ | ✓ |
| Decimal amounts | ✓ | Disallowed | ✓ | ✓ | ✓ |
| Customer chooses price | ✓ | ✓ | Disallowed | Disallowed | Disallowed |

**Disallowed** = cannot use that product/price with this API at all.
**Ignored** = feature has no effect but product/price still usable.

## Integration and multi-currency selection

- **Checkout**: specify price `id` per line item; renders product name + image
- **Payment Links**: Dashboard-created; renders product name + image
- **Subscriptions**: price must be recurring; billing period = `recurring.interval`; multiple prices OK if same interval
- **Quotes**: models one-off invoice or subscription; auto-creates invoices/subscriptions on acceptance
- **Invoices**: specify price `id` per line item; uses `product.name` in invoice PDF

## Related Pages

- [[stripe]] — Stripe company page
- [[stripe-checkout]] — Checkout integration concept
- [[source-stripe-checkout-sessions]] — Checkout Sessions API
- [[paypal-subscriptions]] — PayPal's subscription and plan model

## Raw Sources

- [[stripe-products-prices-2025]] — Products & Prices: custom IDs, price immutability, price_data, compatibility table, subscription constraints, archive rules
- [[stripe-manage-products-prices-2025]] — Manage Products & Prices: CRUD operations, lookup_key + transfer_lookup_key, multi-currency per-API rules, rounding per line item, delete rules, copy-to-live-mode (one-time), import sync pattern

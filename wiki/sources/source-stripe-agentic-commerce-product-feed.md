---
title: "Stripe — ACS Catalog Feed Specification"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-agentic-commerce-product-feed-2026.md"
tags: [stripe, agentic-commerce, product-feed, catalog, inventory, pricing, promotions, csv]
---

## Summary

Full field reference for the four ACS catalog feed types: product, inventory, pricing, and promotions. Submitted as CSV via the v2 `ProductCatalogImport` API.

## Four Feed Types

| Feed | Modes | Use |
| --- | --- | --- |
| `product` | `upsert` or `replace` | Full catalog with all attributes |
| `inventory` | `upsert` only | Stock availability + quantity updates |
| `pricing` | `upsert` only | Price + sale price updates |
| `promotions` | `upsert` only | Discount rules |

**Replace mode** (product only): products absent from file are permanently deleted. **Upsert**: partial updates, missing products unchanged.

**Deletion**: set `delete=true` in product row — only `id` + `delete` are read.

**Discovery-only**: `disable_checkout=true` — syndicated for agent search/ranking, but checkout redirects to `link` URL.

## Product Feed Required Fields

`id` (SKU, max 100 chars), `title` (max 150), `description` (max 5000), `link`, `brand` (most categories), `price` (ISO 4217), `availability` (in_stock/out_of_stock/preorder/backorder), `inventory_quantity` OR `inventory_not_tracked=true`

## Key Field Formats

**Shipping**: `country:delivery_area:service:speed_range:price` (comma-separated multiples); `shipping_cost_basis: per_order/per_item`; `free_shipping_threshold` for order-level free shipping.

**Tax**: `stripe_product_tax_code` (Stripe Tax) OR `third_party_tax_code: anrok:code`; `tax_behavior: inclusive/exclusive`

**Fees**: `country:region:fee_label:fee_amount` (e.g., recycling fees, bottle deposits)

**Variants**: `item_group_id` (same for all variants in a group); `color`, `size`, `gender`, `material`; up to 3 custom variant option name/value pairs

**Product relationships**: `relationship_type:target_id` — types: `upsell`, `cross_sell`, `substitute`, `accessory`; max 10 per product

**Compliance**: `product_warning` with types `legal_disclaimer`, `safety_warning`, `prop_65`; `age_restriction` (integer)

**Reviews**: `product_review_count` + `product_review_rating` (1-5); `popularity_score` (0-5); `return_rate` (0-100%)

## Promotions Feed Key Fields

Discount types: percentage, fixed amount, buy_x_get_y. Apply to specific products/categories. Redemption limits and date ranges supported.

## Related Pages

- [[stripe-agentic-commerce-product-feed]] — concept page
- [[stripe-agentic-commerce]] — ACS context
- [[source-stripe-agentic-commerce-for-sellers]] — seller integration using feeds

## Raw Sources

- [[stripe-agentic-commerce-product-feed-2026]] — verbatim catalog feed field reference (366 lines)

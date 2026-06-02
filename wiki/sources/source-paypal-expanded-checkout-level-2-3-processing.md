---
title: "PayPal Expanded Checkout: Level 2/Level 3 Processing"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-level-2-3-processing.md"
tags: [paypal, expanded-checkout, level-2, level-3, interchange, ic-plus-plus, b2b, corporate-cards, orders-api, supplementary-data]
---

## PayPal Expanded Checkout: Level 2/Level 3 Processing

Reference for L2/L3 card processing data — additional transaction fields sent under `supplementary_data.card` in the Orders v2 API that allow IC++ merchants to qualify for lower interchange rates on corporate and purchase credit cards.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/processing/>

Last updated: 2026-01-07

## Key Takeaways

### What it is

Card processing has three tiers. Higher levels require more data but yield lower interchange fees (relevant for IC++ pricing merchants). Most B2C merchants stay at Level 1; L2/L3 is primarily a B2B feature for corporate purchasing cards.

| Level | Who benefits | Interchange |
| ----- | ------------ | ----------- |
| L1 | All merchants | Higher |
| L2 | IC++ merchants with corp/purchase cards | Lower |
| L3 | IC++ merchants with corp/purchase cards | Lowest |

### Eligibility constraints

- **Geography**: US only, USD only
- **Card types**: Corporate and purchase credit cards only — consumer cards and debit cards are L1 only regardless
- **Networks**: Visa + Mastercard (L2 + L3); Amex (L2 only); Discover (L1 only)
- **Pricing model**: IC++ (interchange-plus) required — flat-rate merchants don't benefit

### API location

L2/L3 data goes under `purchase_units[].supplementary_data.card`:

```json
"supplementary_data": {
  "card": {
    "level_2": { ... },
    "level_3": { ... }
  }
}
```

### Level 2 required fields

- `invoice_id` — invoice number / PO number
- `tax_total` — tax amount as separate money object (not rolled into total)

### Level 3 required fields (superset of L2)

All L2 fields, plus:

- `shipping_amount` — freight/shipping + handling
- `duty_amount` — import/export duties
- `discount_amount` — discount applied
- `shipping_address` — destination address
- `ships_from_postal_code` — origin ZIP
- `line_items[]` — per-item array with: `name`, `description`, `upc`, `unit_amount`, `tax`, `discount_amount`, `total_amount`, `unit_of_measure`, `quantity`, `commodity_code`

### Field consistency requirement

Fields in `supplementary_data` **must match** corresponding fields in `purchase_units`. Key mappings:

| supplementary_data | purchase_units |
| ------------------ | -------------- |
| `card.level_2.invoice_id` | `invoice_id` |
| `card.level_2.tax_total` | `amount.breakdown.tax_total` |
| `card.level_3.shipping_amount` | `amount.breakdown.shipping` |
| `card.level_3.discount_amount` | `amount.breakdown.discount` |
| `card.level_3.shipping_address` | `shipping.address` |
| `card.level_3.line_items[n]` | `items[n]` (name, description, upc, unit_amount, tax, quantity) |

Full mapping table in raw file (24 field pairs).

### 3 critical consistency rules

1. **Conflict resolution**: when `supplementary_data` and `purchase_units` fields disagree, `supplementary_data` takes precedence
2. **PATCH consistency**: when PATCHing `purchase_units`, must also PATCH `supplementary_data` simultaneously
3. **PATCH omission**: if `supplementary_data` is omitted from a PATCH request, it is **automatically deleted** — not preserved

> [!warning] PATCH gotcha
> Omitting `supplementary_data` from a PATCH request silently deletes it. Always include both objects together when updating order details.

## Raw Sources

- [[paypal-expanded-checkout-level-2-3-processing]] — verbatim webpage content with full Create Order curl example, 24-field mapping table, and consistency rules

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-customize-overview]] — full customization catalog (14 features)

---
title: "PayPal Checkout: Pass Line-item Details"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-pass-line-items.md"
tags: [paypal, checkout, line-items, orders-api, invoice, sku, dispute-management, patch-order]
---

## PayPal Checkout: Pass Line-item Details

Official PayPal guide for passing itemised purchase details in the Create Order request — displayed to buyers on the PayPal review page, in post-purchase emails, and in account transaction history.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/pass-line-items/>

Last updated: 2025-05-06

## Key Takeaways

### Where line items appear

- PayPal review page (during checkout)
- Post-purchase email to buyer
- Buyer's PayPal account → Activity → Transactions → All transactions

### Business value

- Reduces disputes — buyer verified items before paying
- Improves dispute resolution — merchant has item specifics on record
- Increases conversion through transparency

### `items[]` fields reference

| Attribute | Required | Notes |
| --------- | -------- | ----- |
| `name` | Yes | Item name |
| `quantity` | Yes | Whole number |
| `unit_amount` | Yes | Must align with `amount.breakdown.item_total` |
| `description` | No | Detailed description |
| `sku` | No | Stock keeping unit |
| `url` | No | Link to item — visible to buyer |
| `category` | No | `DIGITAL_GOODS`, `PHYSICAL_GOODS`, `DONATION` |
| `image_url` | No | Item image — size/type restrictions apply |
| `tax` | No | Per-unit tax — must align with `amount.breakdown.tax_total` |
| `upc` | No | UPC barcode — type + code |

### Amount breakdown constraint

If you pass `items[]`, the sum of `unit_amount × quantity` across all items **must equal** `amount.breakdown.item_total`. Similarly, sum of `tax` fields must equal `amount.breakdown.tax_total`. Mismatches cause validation errors.

### Updating line items post-approval

Use `PATCH /v2/checkout/orders/{id}` with JSON Patch operations (`add`, `remove`, `replace`). Required when:
- Shipping changes affect deliverable items (via shipping callback)
- Buyer makes purchase changes after reviewing the paysheet
- Merchant-side changes before capture

## Images

- `raw/assets/paypal-line-items-paysheet-example.png` — PayPal review page showing line-item details (names, quantities, prices)

## Raw Sources

- [[paypal-checkout-pass-line-items]] — verbatim webpage content + downloaded image

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
- [[source-paypal-checkout-overcharge-handling]] — also uses PATCH order; related flow
- [[source-paypal-best-practices-one-time-payment]] — recommends passing line items for transparency

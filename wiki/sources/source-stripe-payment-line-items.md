---
title: "Stripe — Payment Line Items"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-payment-line-items-2026.md"
tags: [stripe, payment-line-items, l2-l3, interchange, commercial-cards, klarna, paypal, payment-intents]
---

## Summary

Payment line items is a PaymentIntents API feature for passing structured transaction metadata to unlock interchange savings, facilitate reconciliation, and improve authorization rates for Klarna and PayPal.

## Benefits

| Benefit | Who it helps |
| --- | --- |
| L2/L3 interchange savings | IC+ pricing users with eligible commercial cards (Visa, MC, AmEx) |
| Reconciliation | Merchants serving government or enterprise customers |
| Higher auth rates | Klarna and PayPal use line item data in underwriting |

## Geographic Scope

- **Cards L2/L3**: US domestic (US merchants + US-issued cards, excluding territories) and intra-EU (EU merchants + EU cards)
- **Klarna**: global
- **PayPal**: global

## L2 vs L3 Requirements

### L2 (Payment Intents API)

- `tax[total_tax_amount]`
- `payment_details[order_reference]`

### L3/Product 3 (Payment Intents API)

- `line_item[product_name]`
- `line_item[unit_cost]`
- `line_item[quantity]`
- `line_item[product_code]`
- `line_item[unit_of_measure]`
- `line_item[tax][total_tax_amount]`
- `payment_details[order_reference]`

### Checkout Sessions API

- L2: auto-populated by Checkout from existing line items
- L3: requires quantity, price unit_amount, product name, product unit_label

## Eligibility Constraints

- **Card types**: L2 — Business, Purchasing, Corporate; L3 — Purchasing and Corporate only
- **Card networks**: Visa, Mastercard, American Express (AmEx requires direct network agreement for savings)
- **MCC exclusions**: hospitality (airlines, hotels, car rental), fast food, direct marketing, certain retail and utility codes — see raw for full list
- **Sales tax**: L2 Visa requires 0.1–22%; L2 Mastercard requires 0.1–30% (certain MCC exemptions exist)
- **Visa CEDP**: Visa's Commercial Enhanced Data Program replaces US Level 2/3 programs

## Field Limits

- **Max line items**: 200 total; AmEx receives only first 4
- `product_name`: max 1024 chars (cards truncated to 26 alphanumeric; PayPal to 127)
- `product_code`: max 12 chars
- `unit_of_measure`: max 12 chars, alphanumeric
- `payment_details[order_reference]`: max 25 alphanumeric chars for cards; 255 chars for Klarna (visible in app)
- `payment_details[customer_reference]`: max 25 alphanumeric chars (cards only)

## Key Rules

- `tax[total_tax_amount]` and `line_item[tax][total_tax_amount]` are **mutually exclusive**
- `discount_amount` and `line_item[discount_amount]` are **mutually exclusive**
- Line items can be set during **confirmation** or **capture** (except PayPal does not support setting at capture)
- If set at confirmation with manual capture, no need to re-send at capture
- Line items **not included** in API response by default — expand with `amount_details.line_items`
- **Arithmetic validation** enforced by default; set `enforce_arithmetic_validation: false` to bypass (errors surfaced in `amount_details.error`; L2/L3 savings lost if mismatch)

## Payment-Method-Specific Fields

Pass card+klarna+paypal data in a single request under `payment_method_options`:
- **Card**: `commodity_code` (max 12 chars, alphanumeric, no spaces)
- **Klarna**: `product_url`, `image_url` (max 4096), `reference` (max 255, shown in app), `subscription_reference`
- **PayPal**: `description` (max 127), `category` (digital_goods / physical_goods / donation), `sold_by`

Klarna: total amount is `(unit_cost × quantity) − discount_amount + tax.total_tax_amount` (no explicit amount field).

## Related Pages

- [[stripe-payment-line-items]] — concept page
- [[stripe-payment-intents]] — concept page (PaymentIntents API)

## Raw Sources

- [[stripe-payment-line-items-2026]] — verbatim Payment Line Items guide (826 lines)

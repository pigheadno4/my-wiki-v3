---
title: "Stripe Payment Line Items"
type: concept
category: technology
tags: [stripe, payment-line-items, l2-l3, interchange, commercial-cards, klarna, paypal, payment-intents]
---

## Overview

Payment line items is a PaymentIntents API feature that passes structured order metadata alongside a payment. It serves three distinct purposes: unlocking **L2/L3 interchange savings** on eligible commercial cards, facilitating **customer reconciliation**, and improving **authorization rates** for Klarna and PayPal.

## API Structure

Fields passed via `amount_details` and `payment_details` on `stripe.paymentIntents.create()`:

- `amount_details.line_items[]` — per-item data (product_name, unit_cost, quantity, product_code, unit_of_measure, tax, discount_amount, payment_method_options)
- `amount_details.tax` — top-level tax (mutually exclusive with per-item tax)
- `amount_details.shipping` — from/to postal codes + amount
- `amount_details.discount_amount` — top-level discount (mutually exclusive with per-item discount)
- `payment_details.order_reference` — unique order ID (required for L2 and L3)
- `payment_details.customer_reference` — customer ID (cards only)

Line items are **not returned by default** — expand with `amount_details.line_items`.

## L2/L3 Interchange Program

Card networks (Visa, Mastercard, AmEx) offer reduced interchange rates when sufficient order data is passed:

| Level | Card Types | Key Required Fields |
| --- | --- | --- |
| L2 | Business, Purchasing, Corporate | `tax[total_tax_amount]`, `order_reference` |
| L3/Product 3 | Purchasing, Corporate only | + `product_name`, `unit_cost`, `quantity`, `product_code`, `unit_of_measure`, `line_item[tax]` |

**Geographic scope**: US domestic (US merchant + US-issued card, no territories) and intra-EU (EU merchant + EU card). **IC+ pricing required.**

AmEx requires a direct network agreement for savings. AmEx receives only the first 4 line items (200 max for Visa/MC).

Visa's US program is now called **Commercial Enhanced Data Program (CEDP)**, replacing the old Level 2/3 programs.

Many MCC categories are ineligible (hotels, airlines, car rental, restaurants, direct marketing) — see [[source-stripe-payment-line-items]] for full excluded MCC lists.

> **Mutual exclusivity**: Payment line items and [[stripe-industry-metadata]] (T&E industry-specific data) cannot be sent on the same PaymentIntent. Travel/hospitality merchants must choose one.

## Klarna and PayPal

Both use line item data in underwriting models to approve more credit-based options. Key differences:

- **Klarna**: Stripe derives total amount from `(unit_cost × quantity) − discount + tax` — no explicit amount field
- **PayPal**: Does not support setting line items during capture (confirmation only)

Payment-method-specific fields nested under `line_item[payment_method_options][klarna|paypal|card]`:

- **Klarna**: product_url, image_url, reference (shown in app), subscription_reference
- **PayPal**: description, category (digital_goods / physical_goods / donation), sold_by
- **Card**: commodity_code (UNSPSC, NAICS, NAPCS, etc.)

## Flexible Payment Scenarios

### Multicapture

Line items work with multicapture (cards only — Klarna/PayPal not supported):

- Can add `amount_details` at first capture even if absent at creation
- If set at creation, must include or explicitly unset at first capture
- Once included in any capture, must continue in all subsequent captures
- `discount_amount`, `tax.total_tax_amount`, `shipping.amount` are **summed** across captures
- `shipping.from_postal_code` / `to_postal_code` must not change across captures
- `line_items` are **aggregated** across captures
- Partial capture: `amount_to_capture: 0` + `final_capture: true` → `succeeded` with only first-capture items

### Overcapture

Pass updated `amount_details` during capture that is consistent with the larger capture amount.

### Incremental Authorization

Use `incrementAuthorization()` endpoint. Pass updated `amount_details` consistent with the new total authorized amount after the increment.

### Partial Authorization

If the card partially authorizes a lower amount than requested, the original line items may not match the authorized amount. Stripe sets `amount_details.error.code: amount_details_amount_mismatch`.

- **Fix at capture**: provide reconciled `amount_details` matching the partial amount → error cleared, L2/L3 savings preserved
- **Capture without fix**: error persists, Stripe does not send mismatched line items to card networks → L2/L3 savings lost

### Surcharge

Pass surcharge via `amount_details[surcharge][amount]`. Do **not** add surcharge as a separate line item — doing so causes a 400 arithmetic error because Stripe validates line items against `amount` exclusive of surcharge. See [[stripe-surcharge]].

## Arithmetic Validation

Stripe validates that line item totals match the payment amount by default. To bypass:

```js
amount_details: { enforce_arithmetic_validation: false, ... }
```

Errors appear in `amount_details.error`. Cards with arithmetic mismatches won't qualify for L2/L3 savings even if validation is bypassed.

## Sources

- [[source-stripe-payment-line-items]] — full feature guide, field requirements, MCC tables, code samples
- [[source-stripe-payment-line-items-flexible]] — multicapture/overcapture/incremental auth/partial auth/surcharge behavior

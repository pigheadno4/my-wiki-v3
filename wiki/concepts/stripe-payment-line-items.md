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

| Program in the November 7, 2026 guide | Card types | Key PaymentIntent fields |
| --- | --- | --- |
| Mastercard Level 2 | Business, Purchasing, Corporate | Transaction tax and order reference |
| Mastercard Level 3 | Purchasing and Corporate | Order reference, line-item product name, unit cost, quantity, product code and unit of measure, plus transaction-level or per-item tax |
| Visa Product 3 | Purchasing, Corporate and Business | Same Level 3/Product 3 field group in the guide |

**Geographic scope**: US domestic (US merchant + US-issued card, no territories) and intra-EU (EU merchant + EU card). **IC+ pricing required.**

AmEx requires a direct network agreement for savings. AmEx receives only the first 4 line items (200 max for Visa/MC).

The November 7, 2026 Stripe guide says US Visa Level 2 ended in April 2026, with Visa savings through **Commercial Enhanced Data Program (CEDP) Product 3**. The guide still prints Visa Level 2 figures for historical context.

Many MCC categories are ineligible (hotels, airlines, car rental, restaurants, direct marketing) — see [[source-stripe-payment-line-items]] for full excluded MCC lists.

> **Industry metadata.** The May and November 2026 guides say card and PayPal line items cannot be sent alongside [[stripe-industry-metadata|travel-industry metadata]]. Klarna has a separate Extra Merchant Data path in private preview.

## Klarna and PayPal

Both use line item data in underwriting models to approve more credit-based options. Key differences:

- **Klarna**: Stripe derives total amount from `(unit_cost × quantity) − discount + tax` — no explicit amount field
- **PayPal**: Does not support setting line items during capture (confirmation only)

PaymentIntent method-specific fields go under each `amount_details[line_items][index][payment_method_options][method]` entry, with `klarna`, `paypal`, or `card` for the method:

- **Klarna**: product_url, image_url, reference (shown in app), subscription_reference
- **PayPal**: description, category (digital_goods / physical_goods / donation), sold_by
- **Card**: commodity_code (UNSPSC, NAICS, NAPCS, etc.)

## Flexible Payment Scenarios

### Multicapture

Multicapture is conditional on payment-method support and excludes Klarna and PayPal. Use manual capture and request multicapture when available.

- Add `amount_details` or `amount_details[line_items]` on the first capture if absent at creation. Include or explicitly unset each field that was present at creation.
- The general later-capture rule requires continuing fields previously supplied and prohibits adding fields omitted in preceding captures.
- Stripe sums `discount_amount`, `tax.total_tax_amount` and `shipping.amount` and aggregates line items. Shipping postal codes are optional and must stay consistent if supplied.
- A partial nonfinal capture can remain `requires_capture`. The May and November guides illustrate a zero-amount final capture with `final_capture: true` that omits new amount details and returns only the first capture’s items. This example is specific to the illustrated finalization.

### Overcapture

Pass an `amount_to_capture` up to `maximum_amount_capturable` and update `amount_details` to match the actual larger capture amount.

### Incremental Authorization

Use `increment_authorization` to increase the authorization up to the payment method’s limit. Pass updated `amount_details` matching the new authorized total. A later capture collects funds.

### Partial Authorization

If the card partially authorizes a lower amount than requested, the original line items may not match the authorized amount. Stripe sets `amount_details.error.code: amount_details_amount_mismatch`.

- **Fix at capture**: Reconcile `amount_details` to the partially authorized amount. This clears the error and allows Stripe to send card line-item data to networks. Actual L2/L3 savings depend on qualification.
- **Capture without fix**: error persists, Stripe does not send mismatched line items to card networks → L2/L3 savings lost

### Surcharge

Include the surcharge in the PaymentIntent `amount` and record it under `amount_details[surcharge][amount]`. Adding it as a separate line item as well produces an HTTP 400 in the guide’s incorrect example. The November 7, 2026 guide directs tax with a surcharge to top-level `amount_details[tax][total_tax_amount]`. See [[stripe-surcharge]].

## Arithmetic Validation

Stripe validates that line item totals match the payment amount by default. To bypass:

```js
amount_details: { enforce_arithmetic_validation: false, ... }
```

Errors appear in `amount_details.error`. Cards with arithmetic mismatches won't qualify for L2/L3 savings even if validation is bypassed.

## Sources

- [[source-stripe-payment-line-items]] — May and November 2026 feature guides with network and MCC eligibility, PaymentIntent and Checkout fields, arithmetic validation, and flexible scenario links.
- [[source-stripe-payment-line-items-flexible]] — multicapture/overcapture/incremental auth/partial auth/surcharge behavior

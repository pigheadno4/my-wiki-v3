---
title: "Stripe — Payment Line Items for Flexible Payments"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-payment-line-items-flexible-2026.md"
tags: [stripe, payment-line-items, multicapture, overcapture, incremental-authorization, partial-authorization, surcharge, flexible-payments]
---

## Summary

Companion guide to the Payment Line Items feature, covering how to use `amount_details` line items with complex payment flows: multicapture, overcapture, incremental authorization, partial authorization, and surcharge.

## Multicapture Rules

- Not supported for Klarna or PayPal (cards only)
- `amount_details` can be added at first capture even if absent at creation
- If set at creation, must include or explicitly unset at first capture; once started, must continue in all subsequent captures
- `discount_amount`, `tax.total_tax_amount`, `shipping.amount` are **summed** across captures
- `shipping.from_postal_code` / `to_postal_code` must not change across captures
- `line_items` are **aggregated** across captures
- To partially capture and finish: `amount_to_capture: 0` + `final_capture: true`

## Overcapture Rules

- Pass updated `amount_details` consistent with the larger capture amount
- Uses `request_overcapture: 'if_available'`

## Incremental Authorization Rules

- Uses `request_incremental_authorization: 'if_available'` at creation
- Call `incrementAuthorization()` to increase authorized amount
- Pass updated `amount_details` consistent with new total authorized amount

## Partial Authorization Rules

- Uses `request_partial_authorization: 'if_available'` at creation
- If card authorizes less than requested, original line items may mismatch → `amount_details.error.code: amount_details_amount_mismatch`
- **Fix at capture**: provide updated `amount_details` matching partial amount → error cleared, Stripe sends to networks → L2/L3 savings eligible
- **Capture without fix**: error persists, line items not sent to networks → L2/L3 savings lost

## Surcharge Rules

- Pass `amount_details[surcharge][amount]` for the surcharge value
- Total `amount` on PaymentIntent must be inclusive of surcharge
- Do **not** add surcharge as a separate line item — causes 400 arithmetic error (Stripe validates line items against amount exclusive of surcharge)

## Related Pages

- [[stripe-payment-line-items]] — concept page (updated with these rules)
- [[source-stripe-payment-line-items]] — main feature guide
- [[stripe-surcharge]] — surcharge concept page

## Raw Sources

- [[stripe-payment-line-items-flexible-2026]] — verbatim flexible payments guide (1,359 lines)

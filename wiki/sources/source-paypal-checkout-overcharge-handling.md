---
title: "PayPal Checkout: Overcharge Handling"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-overcharge-handling.md"
tags: [paypal, checkout, overcharge, psd2, sca, payer-action-required, patch-order, confirm-payment-source, orders-api]
---

## PayPal Checkout: Overcharge Handling

Official PayPal guide for handling the `PAYER_ACTION_REQUIRED` error when a buyer is charged more than the amount they originally approved — a PSD2/SCA compliance requirement.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/overcharge-handling/>

Last updated: 2025-05-06

## Key Takeaways

### Why this exists (PSD2)

Under PSD2, charging more than the agreed amount requires Strong Customer Authentication (SCA) — PayPal implements this as a **re-authorization** step. If you capture more than the buyer approved, you get `PAYER_ACTION_REQUIRED` (HTTP 422) and must redirect the buyer back to PayPal.

### Typical trigger

Shipping cost added **after** buyer approval — buyer approves order total at checkout, merchant then patches the order to add shipping, new total exceeds approved amount → overcapture error on capture.

### Full flow

```
1. Buyer approves order at checkout (original amount)
2. Buyer returns to merchant → selects shipping
3. PATCH /v2/checkout/orders/{id} → update amount with shipping
4. POST /v2/checkout/orders/{id}/capture
   → HTTP 422 PAYER_ACTION_REQUIRED (if new amount > approved amount)
5. (Optional) POST /v2/checkout/orders/{id}/confirm-payment-source
   → set return_url / cancel_url / SET_PROVIDED_ADDRESS
6. Redirect buyer to payer-action URL from error response links[]
7. Buyer re-approves new amount → redirected to return_url
8. POST /v2/checkout/orders/{id}/capture → HTTP 201 COMPLETED
```

### Key API endpoints

| Action | Endpoint |
| ------ | -------- |
| Patch order amount | `PATCH /v2/checkout/orders/{id}` |
| Capture | `POST /v2/checkout/orders/{id}/capture` |
| Confirm payment source (optional) | `POST /v2/checkout/orders/{id}/confirm-payment-source` |

### `PAYER_ACTION_REQUIRED` error structure

The error response includes a `links[]` array with:
- `rel: "payer-action"` → the URL to redirect the buyer to for re-approval

```json
{ "rel": "payer-action", "href": "https://www.sandbox.paypal.com/checkoutnow?token=XYZ", "method": "GET" }
```

### Confirm payment source (optional step)

Use `POST .../confirm-payment-source` before redirecting to set:
- `return_url` / `cancel_url` (required if not set in Create Order)
- `shipping_preference: SET_PROVIDED_ADDRESS` — prevents buyer from changing address during re-approval
- `payment_method_preference: IMMEDIATE_PAYMENT_REQUIRED`
- `user_action: PAY_NOW`

## Images

- `raw/assets/paypal-overcharge-handling-flow.png` — swimlane diagram of the full integration flow

## Raw Sources

- [[paypal-checkout-overcharge-handling]] — verbatim webpage content + downloaded image

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-authorize-and-capture]] — related: 2-step payment flow also uses Payments API
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog

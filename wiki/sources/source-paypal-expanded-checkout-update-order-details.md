---
title: "PayPal Expanded Checkout: Update Order Details"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-update-order-details.md"
tags: [paypal, expanded-checkout, orders-api, patch, update-order, commit, shipping, tax, invoice]
---

## PayPal Expanded Checkout: Update Order Details

Guide for PATCHing an order after buyer approval in the Expanded Checkout (ACDC) integration — used when final amounts (shipping, tax) aren't known at order creation time.

Source URL: <https://developer.paypal.com/docs/checkout/advanced/customize/update-order-details/>

Last updated: 2025-12-22

## Key Takeaways

### When to use

- Final amount (shipping, tax) determined after buyer approval
- Shipping address needs updating after collection
- Capturing a different total without requiring buyer re-approval

### `commit=false` → Continue button

Adding `commit=false` to the SDK script tag switches the checkout button from **Pay Now** to **Continue**, signaling to the buyer that amounts may still change:

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT-ID&commit=false"></script>
```

> [!warning] `commit=false` trade-off
> Using `commit=false` **reduces available payment methods** — not all funding sources support post-approval order modification. Avoid PATCH if possible; determine the final amount before buyer approval instead.

### PATCH request

JSON Patch format (`op`/`path`/`value`) against `PATCH /v2/checkout/orders/{ORDER-ID}`:

```bash
curl -v -X PATCH https://api-m.sandbox.paypal.com/v2/checkout/orders/{ORDER-ID} \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -d '{
    "op": "add",
    "path": "/purchase_units/@reference_id=='\''PUHF'\''/invoice_id",
    "value": { "integration_artifact": "INV-HighFashions" }
  }'
```

Updatable fields: `amount`, `invoice_id`, `custom_id`, shipping address.

Path syntax uses reference_id selector: `/purchase_units/@reference_id=='PUHF'/field_name`.

### vs Standard Checkout version

The Standard Checkout equivalent (`source-paypal-checkout-update-order-details`) covers the same PATCH mechanics but in the Buttons-only context without CardFields. This Expanded Checkout version is for ACDC integrations with CardFields + Buttons.

## Raw Sources

- [[paypal-expanded-checkout-update-order-details]] — verbatim webpage content with commit=false script tag and PATCH curl sample

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-checkout-update-order-details]] — Standard Checkout equivalent (same PATCH mechanic, Buttons-only context)
- [[source-paypal-expanded-checkout-level-2-3-processing]] — L2/L3 PATCH gotcha: omitting supplementary_data deletes it

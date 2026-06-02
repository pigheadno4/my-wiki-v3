---
title: "PayPal Checkout: Update Order Details"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-update-order-details.md"
tags: [paypal, checkout, patch-order, orders-api, commit-false, continue-button, shipping]
---

## PayPal Checkout: Update Order Details

Official PayPal guide for patching an existing order after buyer approval — updating amounts, shipping, invoice ID, or other fields using `PATCH /v2/checkout/orders/{id}`.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/update-order-details/>

Last updated: 2025-12-22

## Key Takeaways

### When to use PATCH

- Final amount not known until after buyer approves (e.g. shipping cost calculated post-approval)
- Shipping address needs updating after buyer provides it
- `invoice_id` or `custom_id` needs to be set or changed

### `commit=false` → Continue button

When you plan to PATCH the order after approval, signal this to the buyer by using `commit=false` in the script tag, which swaps "Pay Now" → "Continue":

```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT-ID&commit=false"></script>
```

> **Trade-off**: `commit=false` reduces available payment methods — not all funding sources support post-approval order modification. Avoid PATCH when possible; determine final amount before approval.

### PATCH operation

`PATCH /v2/checkout/orders/{ORDER-ID}` accepts JSON Patch operations. Updatable fields: `amount`, `invoice_id`, `custom_id`, shipping address fields.

Partner headers used: `PayPal-Partner-Attribution-Id` (BN code) and `PayPal-Auth-Assertion`.

### Relationship to overcharge handling

If the PATCH increases the amount beyond what the buyer approved, capture will return `PAYER_ACTION_REQUIRED` — requiring buyer re-approval. See [[source-paypal-checkout-overcharge-handling]] for the re-authorization flow.

## Raw Sources

- [[paypal-checkout-update-order-details]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-overcharge-handling]] — what happens when PATCH raises amount above approved total
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog

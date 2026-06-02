---
title: Update order details
slug: /docs/checkout/standard/customize/update-order-details/
createTime: '2024-03-03T22:42:14.748Z'
updateTime: '2025-12-22T04:50:46.582Z'
---

# Update order details

For increased flexibility when obtaining payments from buyers, you can update an existing order. Updating orders allows you to:

- Determine additional amounts, including shipping and tax.
- Capture a different total amount without the payer re-approving the order.
- Update fields, such as shipping address, after collecting them from the payer.

## Know before you code

### Expanded Checkout

- Complete the steps in Get started to get your sandbox account login information and access token from the Developer Dashboard.
- This feature modifies an existing Checkout integration and uses the following:
  - PayPal JavaScript SDK
  - Orders REST API — Create order and Update order

## Implementation

If you update the final amount of the order after the payer approves the payment, or update other amount fields such as shipping or tax, show a **Continue** button during checkout instead of a **Pay Now** button. A **Continue** button indicates to the payer that the amount or other details might change before they complete the order.

To show a **Continue** button, add `commit=false` in the script tag:

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT-ID&commit=false">
</script>
```

> **Tip:** Using `commit=false` reduces the number of payment methods shown to your payer because not all funding sources can be used when modifying the order. When possible, determine the final amount before the payer approves the transaction, and avoid using `PATCH`.

Before you capture the money from the order, call the Orders API on your server with the `ORDER-ID`.

Fields you can update: `amount`, `invoice_id`, `custom_id`.

### Sample request — Update order details

```curl
curl -v -X PATCH https://api-m.sandbox.paypal.com/v2/checkout/orders/{ORDER-ID} \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS-TOKEN' \
  -H 'PayPal-Partner-Attribution-Id: BN-CODE' \
  -H 'PayPal-Auth-Assertion: AUTH-ASSERTION-JWT' \
  -d '{
    "op": "add",
    "path": "/purchase_units/@reference_id=='\''PUHF'\''/invoice_id",
    "value": {
      "integration_artifact": "INV-HighFashions"
    }
  }'
```

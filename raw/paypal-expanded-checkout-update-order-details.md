<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/update-order-details/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Update order details
slug: /docs/checkout/advanced/customize/update-order-details/
createTime: '2025-03-25T14:22:35.604Z'
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
  - Orders REST API - Create order and Update order

 

### Explore PayPal APIs with Postman
You can use Postman to explore and test PayPal APIs.


If you update the final amount of the order after the payer approves the payment, or update other amount fields, such as shipping or tax, show a **Continue** button during checkout instead of a **Pay Now** button. A **Continue** button indicates to the payer that the amount or other details might change before they complete the order.

To show a **Continue** button, add commit=false in the script tag as shown in the following example:

#### Show a continue button
```html
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT-ID&commit=false">
</script>
```

**Tip:** Using commit=false reduces the number of payment methods that are shown to your payer because not all funding sources can be used when modifying the order. When possible, determine the final amount before the payer approves the transaction, and avoid using PATCH.


Before you capture the money from the order, call the Orders API on your server with the ORDER-ID.

- Change ACCESS-TOKEN to your access token.
- Replace BN-CODE with your PayPal attribution ID to receive revenue attribution.
- Replace AUTH-ASSERTION-JWT with your PayPal auth assertion token.

You can pass in a different amount, invoice_id, and custom_id. See the following code sample:

#### Update order details
```bash
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

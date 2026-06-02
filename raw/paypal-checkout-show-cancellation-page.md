---
title: 'Show cancellation page '
slug: /docs/checkout/standard/customize/show-cancellation-page/
createTime: '2024-02-23T23:30:10.073Z'
updateTime: '2025-05-06T21:57:35.649Z'
---

# Show cancellation page

Show a page to your payers to confirm that the payment was cancelled.

## Know before you code

### Expanded Checkout

- Complete the steps in Get started to get your sandbox account login information and access token from the Developer Dashboard.
- This feature modifies an existing Checkout integration and uses the following:
  - PayPal JavaScript SDK
  - Orders REST API — Create order and Update order

## Implementation

Add the `onCancel` function to the JavaScript that renders the PayPal buttons to show a cancellation page when a payer cancels a payment:

```javascript
paypal.Buttons({
    onCancel: function(data) {
        // Show a cancel page or return to cart
    }
}).render('#paypal-button-container');
```

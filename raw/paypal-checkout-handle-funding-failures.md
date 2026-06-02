---
title: Handle funding failures
slug: /docs/checkout/standard/customize/handle-funding-failures/
createTime: '2024-02-23T23:53:43.135Z'
updateTime: '2025-05-13T15:16:43.051Z'
---

# Handle funding failures

If your payer's funding source fails, the Orders API returns an `INSTRUMENT_DECLINED` error. A funding source might fail for the following reasons:

- The billing address associated with the payment method is incorrect.
- The transaction exceeds the card limit.
- The card issuer denied the transaction.

To handle this error, restart the payment so the payer can select a different payment option.

## Know before you code

### PayPal Checkout

Complete the steps in Get started to get your sandbox account login information and access token from the Developer Dashboard.

This feature modifies an existing PayPal Checkout integration and uses the following:

- PayPal JavaScript SDK
- Orders REST API — Create order endpoint

## Handling INSTRUMENT_DECLINED

Restarting the payment is required if you directly call the Orders API from your server. If you use `actions.order.capture()`, the script automatically restarts the checkout flow and prompts the payer to select a different funding source.

Restart the payment in the `onApprove` function as follows:

### Restart the payment

```javascript
paypal.Buttons({
  onApprove: function (data, actions) {
    return fetch('/my-server/capture-paypal-transaction', {
      headers: {
        'content-type': 'application/json'
      },
      body: JSON.stringify({
        orderID: data.orderID
      })
    }).then(function(res) {
      return res.json();
    }).then(function(captureData) {
      if (captureData.error === 'INSTRUMENT_DECLINED') { // Your server response structure and key names are what you choose
        return actions.restart();
      }
    });
  }
}).render('#paypal-button-container');
```

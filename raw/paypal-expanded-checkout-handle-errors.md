<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/handle-errors/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Handle buyer errors
slug: /docs/checkout/advanced/customize/handle-errors/
createTime: '2024-08-15T06:11:38.377Z'
updateTime: '2025-05-14T15:19:25.605Z'
---


# Handle buyer errors
Handle payer errors to provide a unique payer experience.

## Know before you code
Required:
- This feature modifies an existing Expanded Checkout integration
- This integration uses the following:
  - PayPal JavaScript SDK
  - Orders REST API - Create order endpoint


## Buyer checkout error
If an error prevents buyer checkout, alert the user that an error has occurred with the buttons using the onError callback:

```javascript
paypal.Buttons({
  onError: function(err) {
    // For example, redirect to a specific error page
    window.location.href = "/your-error-page-here";
  }
}).render('#paypal-button-container');
```

This error handler is a catch-all. Errors at this point are not expected to be handled beyond showing a generic error message or page.


## Script not loading error
If null pointer errors prevent the script from loading, provide a different checkout experience:

```javascript
if (window.paypal && window.paypal.Buttons) {
  // render the buttons
} else {
  // show a fallback experience
}
```

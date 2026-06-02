---
title: Handle buyer checkout errors
slug: /docs/checkout/standard/customize/handle-errors/
createTime: '2024-03-02T00:38:20.396Z'
updateTime: '2025-05-14T12:41:48.380Z'
---

# Handle buyer checkout errors

Use `onError` callbacks and alternate checkout pages to handle buyer checkout errors.

## Know before you code

### PayPal Checkout

Complete the steps in Get started to get your sandbox account login information and access token from the Developer Dashboard.

This feature modifies an existing PayPal Checkout integration and uses the following:

- JavaScript SDK: Adds PayPal-supported payment methods.
- Orders REST API: Create, update, retrieve, authorize, and capture orders.

## Error handling patterns

If an error prevents buyer checkout, alert the user that an error has occurred with the buttons using the `onError` callback.

### Buyer checkout error

```javascript
paypal.Buttons({
    onError: function(err) {
        // For example, redirect to a specific error page
        window.location.href = "/your-error-page-here";
    }
}).render('#paypal-button-container');
```

This error handler is a catch-all. Errors at this point are not expected to be handled beyond showing a generic error message or page.

### Script not loading error

If null pointer errors prevent the script from loading, provide a different checkout experience.

```javascript
if (window.paypal && window.paypal.Buttons) {
    // render the buttons
} else {
    // show a fallback experience
}
```

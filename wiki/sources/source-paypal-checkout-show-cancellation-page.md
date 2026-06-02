---
title: "PayPal Checkout: Show Cancellation Page"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-show-cancellation-page.md"
tags: [paypal, checkout, oncancel, cancellation, javascript-sdk]
---

## PayPal Checkout: Show Cancellation Page

Official PayPal guide for handling buyer-initiated payment cancellations via the `onCancel` callback. One of PayPal's two recommended starting customizations (alongside validate user input).

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/show-cancellation-page/>

Last updated: 2025-05-06

## Key Takeaways

Single-callback implementation — add `onCancel` to the Buttons config:

```javascript
paypal.Buttons({
    onCancel: function(data) {
        // Show a cancel page or return to cart
    }
}).render('#paypal-button-container');
```

### Relationship to other handlers

| Handler | Trigger | Recommended action |
| ------- | ------- | ------------------ |
| `onCancel` | Buyer explicitly cancels in PayPal pop-up | Show cancellation page or return to cart |
| `onError` | Unrecoverable SDK/flow error | Redirect to error page |
| `onApprove` + `INSTRUMENT_DECLINED` | Payment method fails | Call `actions.restart()` |

This is the simplest customization in the catalog — PayPal recommends it as a starting point because it closes a UX gap: without `onCancel`, a buyer who cancels gets no feedback and may be confused about whether the order was placed.

## Raw Sources

- [[paypal-checkout-show-cancellation-page]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-handle-errors]] — related: onError catch-all handler
- [[source-paypal-checkout-handle-funding-failures]] — related: INSTRUMENT_DECLINED recovery
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog (recommends this as starting point)

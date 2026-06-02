---
title: "PayPal Checkout: Handle Funding Failures"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-handle-funding-failures.md"
tags: [paypal, checkout, instrument-declined, funding-failures, onapprove, actions-restart, orders-api]
---

## PayPal Checkout: Handle Funding Failures

Official PayPal guide for handling `INSTRUMENT_DECLINED` errors — when a buyer's funding source fails and the payment needs to restart.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/handle-funding-failures/>

Last updated: 2025-05-13

## Key Takeaways

### When `INSTRUMENT_DECLINED` occurs

- Incorrect billing address on the payment method
- Transaction exceeds card limit
- Card issuer denial

### Two integration paths — different behaviour

| Integration style | What happens on `INSTRUMENT_DECLINED` |
| ----------------- | ------------------------------------- |
| `actions.order.capture()` (client-side) | SDK **automatically** restarts flow and prompts buyer to choose another funding source |
| Direct Orders API call from server | Must **manually** call `actions.restart()` in `onApprove` |

### Manual restart pattern (server-side capture)

```javascript
paypal.Buttons({
  onApprove: function (data, actions) {
    return fetch('/my-server/capture-paypal-transaction', { ... })
      .then(res => res.json())
      .then(captureData => {
        if (captureData.error === 'INSTRUMENT_DECLINED') {
          return actions.restart(); // re-opens checkout for buyer to pick another method
        }
      });
  }
}).render('#paypal-button-container');
```

> Note: The error key name (`captureData.error`) is determined by your own server response structure — not a fixed PayPal field. Map your server's error representation to the `INSTRUMENT_DECLINED` check.

### Relationship to other error handlers

- `INSTRUMENT_DECLINED` in `onApprove` → `actions.restart()` — recoverable (this page)
- `onError` → redirect to error page — unrecoverable catch-all (see [[source-paypal-checkout-handle-errors]])
- `onCancel` — buyer-initiated cancellation

## Raw Sources

- [[paypal-checkout-handle-funding-failures]] — verbatim webpage content

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-handle-errors]] — related: unrecoverable error handling via `onError`
- [[source-paypal-checkout-integrate-one-time-payment]] — base integration showing `INSTRUMENT_DECLINED` in context
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog

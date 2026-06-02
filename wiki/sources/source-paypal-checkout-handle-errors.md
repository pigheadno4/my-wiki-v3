---
title: "PayPal Checkout: Handle Buyer Checkout Errors"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-checkout-handle-errors.md"
  - "paypal-expanded-checkout-handle-errors.md"
tags: [paypal, checkout, expanded-checkout, error-handling, onerror, fallback, javascript-sdk]
---

## PayPal Checkout: Handle Buyer Checkout Errors

Official PayPal guide for handling two distinct checkout error scenarios: SDK runtime errors via `onError`, and SDK load failures via a `window.paypal` guard.

Source URL: <https://developer.paypal.com/docs/checkout/standard/customize/handle-errors/>

Last updated: 2025-05-14

## Key Takeaways

### Two error scenarios

| Scenario | Cause | Handler |
| -------- | ----- | ------- |
| Checkout error | Error during PayPal button flow | `onError` callback |
| Script load failure | Null pointer / SDK fails to load | `window.paypal && window.paypal.Buttons` guard |

### `onError` — catch-all handler

```javascript
paypal.Buttons({
    onError: function(err) {
        window.location.href = "/your-error-page-here";
    }
}).render('#paypal-button-container');
```

Explicitly a **catch-all** — PayPal states errors here are not expected to be handled with specific logic beyond a generic error message or redirect. Don't try to parse `err` for recovery logic here; use `onApprove` error handling (e.g. `INSTRUMENT_DECLINED` → `actions.restart()`) for recoverable payment errors instead.

### Script load guard — fallback checkout experience

```javascript
if (window.paypal && window.paypal.Buttons) {
    // render the buttons
} else {
    // show a fallback experience (e.g. redirect to manual payment form)
}
```

Handles cases where the PayPal JS SDK fails to load entirely (network issues, ad blockers, etc.).

### Relationship to other error handlers

- `onError` — unrecoverable SDK/flow errors (this page)
- `onApprove` + `INSTRUMENT_DECLINED` → `actions.restart()` — recoverable funding failures (see [[source-paypal-checkout-integrate-one-time-payment]])
- `onCancel` — buyer-initiated cancellation (separate handler)

### Expanded Checkout confirmation

The Expanded Checkout handle-errors page (separate URL, same last-updated date) confirms that **identical patterns apply to ACDC integrations** — same `onError` catch-all and same `window.paypal && window.paypal.Buttons` script guard. No Expanded Checkout-specific error handlers exist beyond what Standard Checkout already documents.

## Raw Sources

- [[paypal-checkout-handle-errors]] — verbatim Standard Checkout webpage content
- [[paypal-expanded-checkout-handle-errors]] — Expanded Checkout version (confirms identical patterns)

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[source-paypal-checkout-customize-overview]] — full customization feature catalog
- [[source-paypal-checkout-integrate-one-time-payment]] — base integration with `onError` and `onCancel` in context

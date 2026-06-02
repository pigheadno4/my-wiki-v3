---
title: "PayPal Expanded Checkout: Integration Guide"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-integrate.md"
tags: [paypal, expanded-checkout, card-fields, 3d-secure, sca, orders-api, payments-api, authorize-capture, billing-address, node-js]
---

## PayPal Expanded Checkout: Integration Guide

Official full integration guide for PayPal Expanded Checkout using the **CardFields** JS SDK component (not the legacy HostedFields). Includes complete frontend and Node.js backend code samples.

Source URL: <https://developer.paypal.com/docs/checkout/expanded/integrate/>

## Key Takeaways

### Script tag — `components=buttons,card-fields`

Expanded Checkout requires **both** components in the script tag:

```html
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&currency=USD&components=buttons,card-fields&enable-funding=venmo"></script>
```

Also links the PayPal card fields CSS:
```html
<link rel="stylesheet" href="https://www.paypalobjects.com/webstatic/en_US/developer/docs/css/cardfields.css" />
```

### Frontend architecture — two parallel components

Both share the **same** `createOrderCallback` and `onApproveCallback` functions:

```
paypal.Buttons({ createOrder, onApprove }).render("#paypal-button-container")
paypal.CardFields({ createOrder, onApprove }).NameField().render("#card-name-field-container")
                                             .NumberField().render(...)
                                             .CVVField().render(...)
                                             .ExpiryField().render(...)
```

### `cardField.isEligible()` — required gate

Must check before rendering any card fields. If not eligible, card fields do not show.

### `cardField.submit({ billingAddress })` — merchant-triggered

Unlike PayPal Buttons (buyer-clicked), card payment is submitted via the merchant's own "Pay now with Card" button. The billing address object is passed into `submit()`:

```javascript
cardField.submit({
    billingAddress: {
        addressLine1, addressLine2, adminArea1, adminArea2,
        countryCode, postalCode
    }
})
```

### `onApprove` — critical difference for card vs button payments

```javascript
// actions.restart() ONLY for Buttons, NOT for card payments
if (errorDetail?.issue === "INSTRUMENT_DECLINED" && !data.card && actions) {
    return actions.restart();  // only fires for PayPal button flow
}
```

`data.card` being truthy means the payment was via CardFields — `actions.restart()` is not applicable in that case.

### 3DS integration — `paymentSource.card.attributes.verification`

Passed in the **server-side** Create Order payload:

```javascript
paymentSource: {
    card: {
        attributes: {
            verification: {
                method: "SCA_ALWAYS",   // or "SCA_WHEN_REQUIRED"
            },
        },
    },
},
```

- `SCA_ALWAYS` — authenticate every transaction
- `SCA_WHEN_REQUIRED` — only when regional mandate requires it (PSD2 countries only)

### Additional server routes vs Standard Checkout

Expanded Checkout adds three routes Standard Checkout does not have:

| Route | Method | Purpose |
| ----- | ------ | ------- |
| `POST /api/orders/:orderID/authorize` | `ordersController.authorizeOrder()` | Auth-only (no capture) |
| `POST /orders/:authorizationId/captureAuthorize` | `paymentsController.captureAuthorize()` | Capture a prior authorization |
| `POST /api/payments/refund` | `paymentsController.refundCapturedPayment()` | Refund a capture |

Note: `captureAuthorize` uses `{ finalCapture: false }` — allowing partial or multiple captures.

### Billing address fields (merchant-rendered)

Billing address is collected in the merchant's own HTML inputs (not PayPal-hosted) and passed via `cardField.submit()`. Six fields: `addressLine1`, `addressLine2`, `adminArea1`, `adminArea2`, `countryCode`, `postalCode`.

### Go-live requirement

Requires requesting **Expanded Credit and Debit Card Payments** capability on the business account — not automatically available.

## Raw Sources

- [[paypal-expanded-checkout-integrate]] — verbatim webpage content with full HTML, app.js, and server.js code samples

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-expanded-checkout]] — Expanded Checkout concept page
- [[source-paypal-expanded-checkout-getting-started]] — prerequisites and environment setup
- [[source-paypal-checkout-integrate-one-time-payment]] — Standard Checkout integration (simpler baseline)
- [[source-paypal-checkout-authorize-and-capture]] — authorize/capture pattern (also used in Expanded)
- [[source-paypal-javascript-sdk-reference]] — `CardFields` API reference

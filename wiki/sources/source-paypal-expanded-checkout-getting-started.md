---
title: "PayPal Expanded Checkout: Getting Started"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-expanded-checkout-getting-started.md"
tags: [paypal, expanded-checkout, hosted-card-fields, 3d-secure, acdc, card-fields, liability-shift, javascript-sdk, orders-api]
---

## PayPal Expanded Checkout: Getting Started

Official getting started guide for PayPal Expanded Checkout — the advanced integration that adds hosted credit/debit card fields directly on the merchant's page, alongside PayPal buttons, with 3D Secure (3DS) support.

Source URL: <https://developer.paypal.com/docs/checkout/expanded/get-started/>

## Key Takeaways

### Expanded Checkout vs Standard Checkout

| Feature | Standard Checkout | Expanded Checkout |
| ------- | ----------------- | ----------------- |
| Payment methods | PayPal, Venmo, Pay Later buttons | All standard + hosted card fields on-page |
| Card entry | Redirects to PayPal | Inline hosted fields on merchant's page |
| Branding | PayPal-branded | Merchant-branded card fields |
| 3DS support | Basic | Full 3DS with `liabilityShift` |
| Sandbox requirement | Standard account | **Expanded Credit and Debit Card Payments** capability required |

### Integration Architecture — Hosted Card Fields + 3DS

```
Page load → script tag loads JS SDK
  → SDK renders Card Fields component (inline on page)
  → SDK renders PayPal Buttons alongside
Buyer fills card details → clicks Submit
  → cardFields.submit() called
  → createOrder callback → server → POST /v2/checkout/orders (with 3DS params)
  → orderId returned to page
  → 3DS challenge shown if required by bank
  → onApprove callback returns liabilityShift response
  → server → POST /v2/checkout/orders/{id}/capture
  → page handles capture response
```

### Key new concept: `liabilityShift`

The `onApprove` callback returns a `liabilityShift` field indicating whether fraud liability has shifted from the merchant to the card issuer following 3DS authentication. Merchants use this to decide whether to proceed with capture.

### Key new SDK method: `cardFields.submit()`

Unlike the standard Buttons flow where `createOrder`/`onApprove` callbacks drive everything, Expanded Checkout uses `cardFields.submit()` triggered by the merchant's own Submit button click.

### Sandbox capability requirement

Unlike Standard Checkout, Expanded Checkout requires the **Expanded Credit and Debit Card Payments** capability explicitly enabled on the sandbox business account:

> Apps & Credentials → App → Features → Accept payments → Expanded Credit and Debit Card Payments ✓

### Node.js dependencies

Same as Standard Checkout: `@paypal/paypal-server-sdk@1.0.0`, `dotenv`, `express`, `body-parser`.

Note: `package.json` name is `paypal-expanded-integration-backend-node` (vs `paypal-checkout-integration-backend-node` for standard).

## Images

- `raw/assets/paypal-expanded-checkout-3ds-sequence-diagram.png` — 13-step sequence diagram showing Hosted Card Fields + 3DS integration flow
- `raw/assets/paypal-expanded-checkout-payment-methods.png` — optimal payment method placement on product detail, cart, and checkout pages

## Raw Sources

- [[paypal-expanded-checkout-getting-started]] — verbatim webpage content + downloaded images

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page (Standard)
- [[source-paypal-checkout-getting-started]] — Standard Checkout getting started (simpler flow without card fields)
- [[source-paypal-checkout-integrate-one-time-payment]] — Standard one-time payment integration

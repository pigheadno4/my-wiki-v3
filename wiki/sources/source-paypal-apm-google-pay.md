---
title: "Integrate Google Pay with JS SDK for Direct Merchants"
type: source
date_ingested: 2026-04-14
original_format: webpage
raw_files:
  - "paypal-apm-google-pay.md"
  - "paypal-apm-google-pay-test-cards.md"
  - "paypal-googlepay-sdk-v6.md"
tags: [paypal, google-pay, apm, javascript-sdk, javascript-sdk-v6, orders-api, direct-merchant, 3d-secure, push-payment]
---

## Overview

Full integration guide for accepting Google Pay as a one-time payment method on the web using the PayPal JS SDK and Orders v2 API. Covers sandbox setup, dual-SDK integration (PayPal + Google Pay), payment sheet, 3DS handling, and go-live steps.

Source URL: <https://developer.paypal.com/docs/checkout/apm/google-pay/>

Last updated: 2025-05-09

## Key Takeaways

### Availability

**36 countries, 22 currencies** — 36 countries including Greece (same as Apple Pay; both add Greece vs standard 35-country vault list).

### Browser support

Works on **all major browsers**: Chrome, Firefox, Safari, Edge — unlike Apple Pay which requires Safari (without latest SDK).

### Scope

**One-time payments with buyer present only.** Japan: TPAN not supported by local processors; must override `allowedAuthMethods = ['PAN_ONLY']`.

### Dual SDK integration

Both scripts required:

```html
<!-- PayPal JS SDK -->
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=googlepay"></script>
<!-- Google Pay SDK -->
<script async src="https://pay.google.com/gp/p/js/pay.js" onload="onGooglePayLoaded()"></script>
```

### 2 PayPal SDK touchpoints

| Method | Purpose |
| --- | --- |
| `paypal.Googlepay().config()` | Returns `allowedPaymentMethods` + `merchantInfo` for `PaymentDataRequest` |
| `paypal.Googlepay().confirmOrder({ orderId, paymentMethodData })` | Confirms order with Google Pay token |
| `paypal.Googlepay().initiatePayerAction({ orderId })` | Triggers 3DS authentication when `PAYER_ACTION_REQUIRED` |

### Integration flow

1. `paypal.Googlepay().config()` → check eligibility, get `allowedPaymentMethods` + `merchantInfo`
2. `isReadyToPay()` → render button if eligible
3. `loadPaymentData(paymentDataRequest)` → show Google Pay sheet
4. `onPaymentAuthorized` callback → create order → `confirmOrder()` → capture
5. If `PAYER_ACTION_REQUIRED`: `initiatePayerAction()` → check `liability_shift` → capture

### Japan override

```javascript
paymentDataRequest.allowedPaymentMethods[0].parameters.allowedAuthMethods = ['PAN_ONLY'];
```

### 3DS handling

`confirmOrder()` returns `status: PAYER_ACTION_REQUIRED` → call `initiatePayerAction({ orderId })` → check `orderResponse.payment_source.google_pay.card.authentication_result` → capture if `liability_shift` acceptable.

### Go-live

Production onboarding: `paypal.com/bizsignup/add-product?product=payment_methods&capabilities=GOOGLE_PAY`

### SDK API reference (included in this guide)

- `config()` → `ConfigResponse`: `allowedPaymentMethods`, `merchantInfo`
- `confirmOrder(params)` → `ConfirmOrderResponse`: `id`, `status`, `payment_source`, `links`
- `initiatePayerAction(params)` → `InitiatePayerActionResponse`: `liabilityShift`
- `ConfirmOrderParams`: `orderId` (required), `paymentMethodData` (required), `shippingAddress`, `billingAddress`, `email` (all optional)

## Test Cards

Source URL: <https://developer.paypal.com/docs/checkout/apm/test-cards/google-pay/>

Last updated: 2025-05-09

Test cards for 5 countries (US, CA, GB, IT, FR). Any future expiry + 3-digit CVV (4-digit for Amex).

| Scenario | Cards |
| --- | --- |
| Successful (basic) | 17 cards — Amex, Discover, MC, Visa, FR Cartes Bancaire |
| 3DS step-up success | 15 cards — US/CA/GB/IT/FR across Amex, MC, Visa |
| 3DS frictionless success | 1 card — FR Cartes Bancaire |
| 3DS step-up failure | 5 US Visa cards |

## Raw Sources

- [[paypal-apm-google-pay]] — verbatim integration guide with full code samples and SDK reference
- [[paypal-apm-google-pay-test-cards]] — test card suite: 38 cards across 5 countries, 3DS success/failure scenarios

## Relevant Wiki Pages

- [[paypal-apm]] — APM overview with all 11 supported methods
- [[source-paypal-apm-apple-pay]] — Apple Pay integration (same 36-country list, similar dual-SDK pattern)
- [[paypal-googlepay-sdk-v6]] — SDK v6 integration (docs.paypal.ai): `googlepay-payments` component, `getGooglePayConfig()`, `confirmOrder({orderId, paymentMethodData})`, `status !== "PAYER_ACTION_REQUIRED"` gate before capture, `SCA_WHEN_REQUIRED` in order payload

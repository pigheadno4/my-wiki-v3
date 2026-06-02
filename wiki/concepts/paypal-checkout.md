---
title: "PayPal Checkout"
type: concept
category: technology
tags: [paypal, checkout, javascript-sdk, orders-api, payment-gateway, venmo]
---

# PayPal Checkout

PayPal Checkout is PayPal's standard e-commerce integration product that allows merchants to accept PayPal, Venmo, and card payments on their websites via a JavaScript SDK and server-side REST API.

## How It Works

PayPal Checkout uses a **two-sided integration**: a client-side JavaScript SDK renders payment buttons and manages the checkout pop-up, while a server-side integration handles order creation and capture via the Orders REST API.

### Integration Architecture

```
Buyer → Merchant Page (JS SDK buttons)
         ↓ createOrder callback
       Merchant Server → POST /v2/checkout/orders → PayPal Orders API
         ↓ Order ID returned
       JS SDK → Launches checkout pop-up
         ↓ Buyer approves
       Merchant Server → POST /v2/checkout/orders/{id}/capture → PayPal Orders API
```

### Key Components

| Component | Role |
|-----------|------|
| PayPal JS SDK | Renders buttons, manages checkout pop-up, fires callbacks |
| `createOrder` callback | Initiates order on merchant server after button click |
| `onApprove` callback | Triggered after buyer approval; merchant captures payment |
| Orders REST API | Server-side order lifecycle (create, capture, authorize) |
| PayPal Server SDK | Language-specific wrappers for the Orders REST API |

## Buyer Experience

1. PayPal/Venmo/Card buttons appear on product, cart, or checkout pages
2. Buyer clicks a button → checkout pop-up opens
3. Pop-up shows buyer's default shipping address and shipping options (set by merchant in the Orders API call)
4. Buyer can change shipping address and payment method
5. Buyer confirms and clicks "Complete Purchase"
6. PayPal processes payment server-side

## Button Placement Best Practice

PayPal recommends surfacing buttons at **three points** in the purchase journey:
- Product detail pages
- Cart pages
- Checkout pages

This reduces friction and allows buyers to initiate PayPal Checkout from wherever they prefer.

## Relevant Companies

- [[paypal]] — PayPal company overview

## Error Handling

| Scenario | Handler | Action |
| -------- | ------- | ------ |
| Funding source declined | `onApprove` → `INSTRUMENT_DECLINED` | Call `actions.restart()` — recoverable |
| Other payment error | `onApprove` → other error detail | Show failure message |
| Script/load error | `onError` callback | Redirect to error page |
| Buyer cancels | `onCancel` callback | Return to cart |

## App Switch

PayPal supports deep-linking into the native PayPal mobile app. Requires `appSwitchWhenAvailable: true` on the client and `appSwitchPreference.launchPaypalApp: true` in the server-side `experienceContext`. On return, call `buttons.resume()` if `buttons.hasReturned()`.

## JS SDK v6 Key Details

- **Script**: `https://www.paypal.com/web-sdk/v6/core` (prod) / `https://www.sandbox.paypal.com/web-sdk/v6/core` (sandbox)
- **clientToken** (vaulting + Fastlane only): expires **15 minutes**; bound to domain; generate with `response_type=client_token` + `domains[]` params
- **8 components**: paypal-payments, venmo-payments, paypal-guest-payments, paypal-messages, card-fields, fastlane, googlepay-payments, applepay-payments
- **5 pageType values**: checkout, product-details, cart, mini-cart, home
- **Eligibility**: `findEligibleMethods({currencyCode})` → `.isEligible("paypal"|"paylater"|"credit")`, `.getDetails()` returns `productCode` (Pay Later) / `countryCode` (Credit)
- **Session methods**: `createPayPalOneTimePaymentSession()`, `createPayLaterOneTimePaymentSession()`, `createPayPalCreditOneTimePaymentSession()`
- **Web components**: `<paypal-button>`, `<paypal-pay-later-button>`, `<paypal-credit-button>`
- **Security**: NEVER pass item total from browser; validate order on server before capture

## Payment Failure Webhook Events

- `PAYMENT.CAPTURE.COMPLETED` — successful capture
- `PAYMENT.CAPTURE.DENIED` — failed capture (asynchronous — bank may initially authorize then later decline)

See [[source-paypal-payment-failures]] for the full 19 error codes and recovery patterns.

## Sources

- [[source-paypal-checkout-getting-started]] — Official getting started guide
- [[source-paypal-checkout-integrate-one-time-payment]] — Full integration guide with frontend + backend code
- [[source-paypal-payment-failures]] — Payment failures: 19 error codes, actions.restart(), async failures, webhook events
- [[source-paypal-js-sdk-v6-setup]] — JS SDK v6 canonical setup: script URLs, clientToken 15min expiry, 8 components, eligibility API, Pay Later/Credit sessions, web components
- [[source-paypal-security-guidelines]] — Security guidelines: CSP + SRI for SDK; load only from official CDN; validate payment events server-side before fulfilling

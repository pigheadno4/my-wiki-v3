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

### Historical package evidence: `@paypal/paypal-js@8.4.2`

The exact `8.4.2` package snapshot exposes the v6 loader from the `./sdk-v6` export. Its TypeScript surface requires `clientToken` for `createInstance()` and conditionally adds methods for three declared components: `paypal-payments`, `venmo-payments`, and `paypal-legacy-billing-agreements`. The separately versioned React package appears in the same monorepo snapshot only as repository context; it is not part of the `@paypal/paypal-js@8.4.2` release identity.

This historical surface is narrower than the later v6 product documentation summarized above. Treat package-qualified release evidence as authoritative for version-specific questions and the current product documentation as authoritative for current integrations.

### Version 9 package evidence

The exact `@paypal/paypal-js@9.8.0` surface accepts either `clientId` or `clientToken`, expands conditional instance typing to nine components, and adds `hydrateEligibleMethods()` for pre-fetched eligibility. Its declared components include PayPal, Venmo, guest payments, messages, subscriptions, Card Fields, Apple Pay, Google Pay, and legacy billing agreements.

`@paypal/react-paypal-js@9.3.0` exposes the v6 React API through `@paypal/react-paypal-js/sdk-v6` while retaining the root export for the legacy integration. `PayPalProvider` supports deferred string or Promise credentials, defaults to `paypal-payments`, and can hydrate server-fetched eligibility. Session hooks and prebuilt web-component buttons cover PayPal, Venmo, Pay Later, Credit, guest payments, subscriptions, saved payments, Card Fields, Apple Pay, and Google Pay.

### Version 10 environment requirement

`@paypal/paypal-js@10.0.0` makes `environment` mandatory for the v6 `loadCoreSdkScript()` call. Pass either `environment: "production"` or `environment: "sandbox"` explicitly. The TypeScript declaration requires the property, and runtime validation throws before script loading when it is missing or invalid.

The coordinated `@paypal/react-paypal-js@10.0.0` release makes the same value mandatory on the v6 `PayPalProvider`. A client ID does not select the environment: even a live client ID loads the sandbox host when paired with `environment="sandbox"`. Upgrades from v9 must therefore audit every direct loader call and every v6 React provider before deployment. This focused major-version change does not, by itself, add a payment method or change the legacy root integration.

### Version 10.0.1 and React 10.1.0

`@paypal/paypal-js@10.0.1` augments `HTMLElementTagNameMap` for eight v6 custom elements, so non-React TypeScript code receives typed results from `document.createElement()` and `document.querySelector()`. The declarations cover PayPal, Venmo, Pay Later, Credit, basic-card button/container, PayPal Messages, and Apple's registered button. The v6 Pay Later country-code type also adds Canada.

`@paypal/react-paypal-js@10.1.0` extends the explicit-environment rule to the server-side `useFetchEligibleMethods()` helper. Omitting or passing an invalid environment throws before it selects `api-m.paypal.com` or `api-m.sandbox.paypal.com`; this prevents production server rendering from hydrating a production client with sandbox eligibility.

## Payment Failure Webhook Events

- `PAYMENT.CAPTURE.COMPLETED` — successful capture
- `PAYMENT.CAPTURE.DENIED` — failed capture (asynchronous — bank may initially authorize then later decline)

See [[source-paypal-payment-failures]] for the full 19 error codes and recovery patterns.

## Sources

- [[source-paypal-checkout-getting-started]] — Official getting started guide
- [[source-paypal-checkout-integrate-one-time-payment]] — Full integration guide with frontend + backend code
- [[source-paypal-payment-failures]] — Payment failures: 19 error codes, actions.restart(), async failures, webhook events
- [[source-paypal-js-sdk-v6-setup]] — JS SDK v6 canonical setup: script URLs, clientToken 15min expiry, 8 components, eligibility API, Pay Later/Credit sessions, web components
- [[source-github-paypal-js]] — cumulative package-qualified repository evidence and exact source snapshots
- [[paypal-braintree-integration]] — Braintree client-token, nonce, and server-processing boundary for PayPal v6 React flows
- [[source-paypal-security-guidelines]] — Security guidelines: CSP + SRI for SDK; load only from official CDN; validate payment events server-side before fulfilling

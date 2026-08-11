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

The exact `@paypal/paypal-server-sdk@2.3.0` TypeScript baseline wraps Orders v2 alongside Payments v2, Vault v3, Transaction Search v1, and Subscriptions v1. The reviewed `2.4.0` delta adds typed `ORDER_COMPLETE_ON_PAYMENT_APPROVAL` processing instructions to create/confirm request and Order response models. Its Orders controller covers create, get, patch, confirm, authorize, capture, and tracking operations; Sandbox is the default environment and automatic retries are disabled by default. See [[source-github-paypal-typescript-server-sdk]] for the package-qualified boundary and eligibility cautions.

The exact REST-contract baseline at `90e8041` independently defines Orders 2.32 create/get/patch/confirm/authorize/capture/tracking operations and Payments 2.12 authorization, capture, refund, and eligible-method operations. Orders models PayPal, Venmo, cards, Apple Pay, Google Pay, and multiple local methods, but schema presence is not merchant or buyer eligibility evidence. See [[source-github-paypal-rest-api-specifications]].

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

### Current v6 sample baseline at `b5f2df2`

The `paypal-examples/v6-web-sdk-sample-integration` baseline combines static JavaScript, React/TypeScript, and Node.js examples. The standard PayPal flow fetches a server-owned client ID, checks PayPal, Pay Later, and Credit eligibility separately, starts the selected session with an unresolved create-order promise to preserve browser transient activation, and captures on approval.

The React sample uses `@paypal/react-paypal-js@10.1.0` through `/sdk-v6` and explicitly sets `environment="sandbox"`, matching the v10 requirement below. Its dropdown gates Venmo, Pay Later, and Credit with `useEligibleMethods()` while retaining PayPal and guest card choices. These examples establish integration shape, not merchant or regional eligibility.

### Historical server-side sample at `5409a3b`

The September 2023 `paypal-examples/paypal-sdk-server-side-integration` baseline uses PayPal JS SDK 5.1.x with a Fastify/TypeScript server. The browser sends cart SKU and quantity to the merchant server; the server resolves prices from its own catalog, obtains and caches an OAuth access token, creates the order, and captures or authorizes after approval. Partner examples add `PayPal-Partner-Attribution-Id` and either `PayPal-Auth-Assertion` or a payee merchant ID for connected-merchant calls.

The capture helper generates one `PayPal-Request-Id` and reuses it for a single delayed retry after a 5xx response. The retry drops the original `Prefer` header, however, and Create Order does not generate an idempotency key. Treat this as a historical retry pattern rather than current production-ready code.

> [!warning] Historical sample defects
> The retained sample has several implementation defects: its custom API-base override is broken by operator precedence; the GET-order route validates a query parameter but reads the request body; its non-success path parses the response body twice; the shipping route does not require `shippingAddress`; and discount values are multiplied by 100 while other amount components are not. Preserve these defects when using the sample as version-specific evidence.

### Historical checkout-components runtime: `4.1.47`

The exact `@paypal/checkout-components@4.1.47` snapshot implements the Zoid-based `paypal-buttons` and `paypal-checkout` components. Its decorated `createOrder` callback must return a nonempty string order ID. The alternative billing-agreement path is mutually exclusive with `createOrder` and requires `vault=true`.

Funding visibility combines server-provided eligibility with layout, platform, branding, and remembered-funding constraints. The historical horizontal layout retains at most two eligible sources. In this v4 runtime, Venmo is mobile-only and cannot be the primary button.

This is historical implementation evidence from 2019, not current availability guidance. Later PayPal product documentation supports both mobile Venmo app switch and desktop QR checkout, so version-specific questions must distinguish the old runtime from the current product.

### checkout-components v5 accumulated runtime: `5.0.425`

The exact `@paypal/checkout-components@5.0.425` source exposes separate interfaces for Buttons, Marks, Card Fields, Payment Fields, Hosted Buttons, Wallet, and Saved Payment Methods. Its protected component surface also includes Checkout, Venmo, and QR Code. This is the accumulated v5 architecture; the exact `5.0.425` patch only forwards bfcache events through post-robot.

The v5 Venmo funding config supports purchase and experiment-gated vault-without-purchase flows. Its implementation distinguishes desktop-web from mobile-web channels and carries native-browser, popup, app-switch, and QR-related state. Product availability and merchant eligibility must still be checked against current documentation.

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

### Core 10.1.0 and React 10.2.0

`@paypal/paypal-js@10.1.0` reads legacy-loader `environment` and `sdkBaseUrl` settings only from own properties. An inherited `environment="sandbox"` value can no longer change the production-default SDK URL through prototype pollution.

`@paypal/react-paypal-js@10.2.0` renames the server async function to `fetchEligibleMethods()`; `useFetchEligibleMethods()` remains a deprecated alias for migration compatibility. React eligibility hydration now treats the provider's stored `null` payload and an omitted consumer payload as equivalent. The hydrated result is reused only for a no-payload `useEligibleMethods()` call; a supplied payload still requests eligibility for that configuration.

### React 10.2.1 SSR eligibility coordination

`@paypal/react-paypal-js@10.2.1` prevents a no-payload `useEligibleMethods()` effect from racing `PayPalProvider` while it hydrates a server-fetched eligibility response. The provider exposes pending, resolved, or rejected hydration state before child effects run; the no-payload hook waits and reuses the hydrated result. A hook with an explicit payload still fetches immediately because server hydration cannot satisfy that distinct client payload.

For SSR, await `fetchEligibleMethods()` and pass the resolved value, not a Promise, as `eligibleMethodsResponse`. Call `useEligibleMethods()` without a payload to consume it.

## Payment Failure Webhook Events

- `PAYMENT.CAPTURE.COMPLETED` — successful capture
- `PAYMENT.CAPTURE.DENIED` — failed capture (asynchronous — bank may initially authorize then later decline)

See [[source-paypal-payment-failures]] for the full 19 error codes and recovery patterns.

## Sources

- [[source-paypal-checkout-getting-started]] — Official getting started guide
- [[source-paypal-checkout-integrate-one-time-payment]] — Full integration guide with frontend + backend code
- [[source-paypal-payment-failures]] — Payment failures: 19 error codes, actions.restart(), async failures, webhook events
- [[source-paypal-js-sdk-v6-setup]] — JS SDK v6 canonical setup: script URLs, clientToken 15min expiry, 8 components, eligibility API, Pay Later/Credit sessions, web components
- [[source-github-paypal-checkout-components]] — historical checkout presentation, callback, funding eligibility, and Venmo runtime evidence
- [[source-github-paypal-js]] — cumulative package-qualified repository evidence and exact source snapshots
- [[source-github-v6-web-sdk-sample-integration]] — current runnable v6 HTML, React, and Node integration baseline
- [[source-github-paypal-sdk-server-side-integration]] — historical JS SDK 5.1.x client/server sample, partner headers, retries, shipping patches, and retained defects
- [[paypal-braintree-integration]] — Braintree client-token, nonce, and server-processing boundary for PayPal v6 React flows
- [[source-paypal-security-guidelines]] — Security guidelines: CSP + SRI for SDK; load only from official CDN; validate payment events server-side before fulfilling
- [[source-github-paypal-rest-api-specifications]] — exact-SHA Orders, Payments, Vault, Webhooks, and supporting REST contracts

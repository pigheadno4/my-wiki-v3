---
title: "GitHub: paypal-examples/v6-web-sdk-sample-integration"
type: source
date_ingested: 2026-04-17
date_updated: 2026-08-04
original_format: github-repo
raw_files:
  - "github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/manifest.json"
  - "github-paypal-v6-samples.md"
tags: [paypal, web-sdk-v6, samples, node-js, react, card-fields, venmo, google-pay, apple-pay, apm, subscriptions, vault, fastlane, github-repository]
---

## Overview

`paypal-examples/v6-web-sdk-sample-integration` is PayPal's runnable sample repository for v6 Web SDK checkout flows. This cumulative page preserves the manually selected April 2026 evidence at commit `dd9ef8a53c71d9d2107ad94c23b73b62f9811258` and adds the approved full baseline at `default-branch@b5f2df2` (`b5f2df209b0bfd10b1a3cde600088ddf21e43523`).

Repository: <https://github.com/paypal-examples/v6-web-sdk-sample-integration>

## Evidence Boundary

- The current capsule retains 257 files totaling 854,493 bytes. It excludes three tests, seven images, and one lockfile under reviewed capsule policy.
- The sample demonstrates public integration contracts and orchestration. It does not establish merchant eligibility, regional availability, account enablement, certification, or production behavior.
- No generated comparison connects the legacy `dd9ef8a` selection to `b5f2df2`; the earlier 36-file review is preserved as historical context and the current full baseline was compared manually during ingest.
- Upstream README statements are not treated as stronger than contradictory implementation code.

## Grounding Excerpts

> "make one-time payments with different payment methods like PayPal and Venmo"
>
> `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/README.md:3-7`

> "do not await this async function since it can cause transient activation issues"
>
> `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/client/components/paypalPayments/oneTimePayment/html/src/recommended/app.js:96-101`

> "the order is auto-completed on approval, so no separate capture call is needed"
>
> `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/client/components/localPaymentMethods/README.md:177-182`

> "PayPal recommends storing this value in your database and NOT returning it back to the browser."
>
> `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/server/node/src/routes/vaultRouteHandler.ts:91-96`

> "Awaiting initiatePayerAction here would leave the Google Pay window open on top of (and blocking) the 3DS modal."
>
> `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/client/components/googlepayPayments/threeDSecure/html/src/app.js:102-109`

## Current Architecture at `b5f2df2`

The repository combines static HTML/JavaScript examples, a React/TypeScript multi-flow application, and a Node.js Express backend. The backend uses `@paypal/paypal-server-sdk`, keeps product prices in a server-owned catalog, validates request bodies with Zod, and generates a fresh `PayPal-Request-Id` UUID for create, capture, subscription, and vault operations.

Browser initialization uses either a public client ID or a browser-safe client token. The client-token route requests `response_type=client_token`; `domains[]` is added when configured because Fastlane requires it. Server API credentials remain in environment variables.

## One-Time Checkout

The recommended PayPal flow initializes `paypal-payments`, calls `findEligibleMethods({ currencyCode: "USD" })`, and separately gates PayPal, Pay Later, and Credit buttons. Each button starts its matching one-time-payment session with `presentationMode: "auto"` and a not-yet-awaited create-order promise so browser transient activation is retained. Approval is followed by server-side capture.

Venmo follows the same create, session-start, approve, and capture shape through `venmo-payments` and `createVenmoOneTimePaymentSession()`. The sample checks `isEligible("venmo")`; repository presence alone does not prove a merchant can offer Venmo.

Advanced PayPal examples retain redirect, direct app switch, payment-handler, asynchronous merchant validation, eligibility hydration, sandboxed iframe, and iframe-controlled redirect patterns. The redirect-in-iframe example disables automatic redirect and delegates top-level navigation to the merchant page.

## Cards, Guest Payments, and Fastlane

Card Fields exposes separate number, expiry, and CVV components. One-time submission returns `succeeded`, `canceled`, or `failed`; only success proceeds to capture. The 3DS variant creates an order with `SCA_ALWAYS` for sandbox testing. Save-without-purchase uses a setup token, submits it through `createCardFieldsSavePaymentSession()`, then upgrades it to a payment token server-side.

Guest Payments supports click-to-open, automatic on-load, and shipping-callback patterns. Shipping callbacks can reject a non-US address or an unavailable shipping option; adding those callbacks changes presentation behavior to a popup or modal.

Fastlane uses a browser-safe client token, `identity.lookupCustomerByEmail()`, member authentication, saved address selection, and `FastlanePaymentComponent().getPaymentToken()`. The resulting single-use card token is sent to the server and placed in `paymentSource.card.singleUseToken`. The README's `/paypal-api/checkout/orders/create` endpoint is stale; the implementation calls `/paypal-api/checkout/orders/create-order-for-card-with-single-use-token`.

## Vault and Subscriptions

The repository demonstrates both `VAULT_WITH_PAYMENT` and `VAULT_WITHOUT_PAYMENT`:

- PayPal purchase plus vault sets `savePayment: true` in the session and `storeInVault: ON_SUCCESS` on the order.
- PayPal and Card Fields save-without-purchase create a setup token, collect approval, upgrade it to a long-lived payment token, and keep that payment token server-side.
- Apple Pay purchase plus vault adds `paymentSource.applePay.attributes.vault.storeInVault: ON_SUCCESS` before confirm and capture.

The subscription example initializes `paypal-subscriptions`, requests `RECURRING_PAYMENT` eligibility, and starts `createPayPalSubscriptionPaymentSession()`. The server uses an existing `PAYPAL_SUBSCRIPTION_PLAN_ID` or creates a sample product and active monthly plan before creating the subscription. This demonstrates the API sequence, not complete subscription lifecycle management.

## Apple Pay and Google Pay

Apple Pay requires both SDKs, device capability, merchant/domain validation, and a matching amount between the Apple payment request and PayPal order. The sample validates the merchant, confirms the order with Apple's token and contacts, then captures. Its setup README also requires enabling Apple Pay on the PayPal app and registering the HTTPS domain.

Google Pay similarly combines the PayPal and Google SDKs. The 3DS example treats `PAYER_ACTION_REQUIRED` specially: it resolves Google's authorization callback so the Google sheet closes, then invokes `initiatePayerAction({ orderId })`, retrieves the order's authentication result, and captures. The example always captures after authentication; production code may instead gate capture on liability-shift and authentication values.

## Local Payment Methods

The current sample catalog contains 46 local-method implementations spanning wallets, bank methods, vouchers, and pay-later products. Each uses a method-specific component, eligibility key, session constructor, sandbox buyer country, and currency.

Most newer examples send `ORDER_COMPLETE_ON_PAYMENT_APPROVAL` and retrieve the completed order after approval. Six retained implementations instead perform an explicit capture: Bancontact, BLIK, EPS, iDEAL, P24, and SEPA.

> [!warning] Contradiction - local-method completion
> The shared README states that local methods are auto-completed and need no separate capture. The six implementations above create without `ORDER_COMPLETE_ON_PAYMENT_APPROVAL` and call the capture route in `onApprove`. Treat completion behavior as method- and implementation-specific until the upstream sample is reconciled.

## React Multi-Flow Application

The React capsule declares `@paypal/react-paypal-js@10.1.0`, React 19.2.5, TypeScript 6.0.2, and `@paypal/paypal-server-sdk@2.1.0`. `PayPalProvider` uses the `/sdk-v6` export with `environment="sandbox"` and loads PayPal, Venmo, Guest Payments, Subscriptions, Card Fields, Messages, Apple Pay, and Google Pay components.

Pages demonstrate product, cart, and checkout routing; stacked and dropdown payment choices; Card Fields; Apple Pay; Google Pay; subscriptions; vault-with-purchase; save-without-purchase; PayPal Messages; and error boundaries. The dropdown gates Venmo, Pay Later, and Credit with `useEligibleMethods()` and always includes PayPal and guest card choices.

The React README contains stale snippets: its provider example omits the required v10 `environment`, names `paypalServerSdk.ts` instead of `paypalServerSdkClient.ts`, and documents a payment-token endpoint that does not match the router. Use the collected implementation for exact calls.

## Change from the April 2026 Review

The earlier review retained 36 selected files. The current baseline expands the evidence to 257 files and adds:

- a full React/TypeScript multi-flow sample;
- Fastlane member and guest flows;
- Google Pay 3DS orchestration;
- Apple Pay purchase-with-vault;
- server-side eligibility, product, subscription, and order-retrieval routes;
- a much larger local-payment-method catalog;
- complete HTML entry points and iframe examples.

Existing core PayPal, Venmo, Card Fields, Apple Pay, Google Pay, Guest Payments, Messages, and subscription examples mostly receive error handling, naming, or supporting-page updates. Server order handling now accepts a validated intent and optional processing instruction and exposes an order-retrieval route.

## Related

- Company: [[paypal]]
- Checkout: [[paypal-checkout]]
- Local methods: [[paypal-apm]]
- Fastlane: [[paypal-fastlane]]
- Vaulting: [[paypal-vault]]
- Subscriptions: [[paypal-subscriptions]]
- Apple Pay: [[paypal-apple-pay]]
- Google Pay: [[paypal-google-pay]]
- Repository history: [[changelog-github-v6-web-sdk-sample-integration]]

## Raw Sources

- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/manifest.json` - immutable exact-SHA baseline at `b5f2df209b0bfd10b1a3cde600088ddf21e43523`
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/README.md` - repository scope and setup
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/client/components/localPaymentMethods/README.md` - current local-method catalog and shared guidance
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/client/prebuiltPages/react/README.md` - React application overview and declared versions
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/server/node/src/routes/ordersRouteHandler.ts` - order construction, retrieval, and capture
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/server/node/src/routes/vaultRouteHandler.ts` - setup-token and payment-token flow
- `raw/github-paypal-v6-samples.md` - legacy review pointer at `dd9ef8a53c71d9d2107ad94c23b73b62f9811258`

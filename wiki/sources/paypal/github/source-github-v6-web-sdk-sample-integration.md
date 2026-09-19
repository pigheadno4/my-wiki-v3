---
title: "GitHub: paypal-examples/v6-web-sdk-sample-integration"
type: source
date_ingested: 2026-04-17
date_updated: 2026-09-19
original_format: github-repo
raw_files:
  - "github/paypal/v6-web-sdk-sample-integration/snapshots/2026-09-19-bb23e7c/manifest.json"
  - "github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/manifest.json"
  - "github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/manifest.json"
  - "github-paypal-v6-samples.md"
tags: [paypal, web-sdk-v6, samples, node-js, react, card-fields, venmo, google-pay, apple-pay, apm, subscriptions, vault, fastlane, github-repository]
---

## Overview

`paypal-examples/v6-web-sdk-sample-integration` is PayPal's runnable sample repository for v6 Web SDK checkout flows. This cumulative page preserves the manually selected April 2026 evidence at commit `dd9ef8a53c71d9d2107ad94c23b73b62f9811258`, the approved full baseline at `default-branch@b5f2df2`, and the contained Apple Pay delta at `default-branch@de90a89` (`de90a89c90b06421ca34241e7162236e2b04fd79`).

Repository: <https://github.com/paypal-examples/v6-web-sdk-sample-integration>

The latest collected baseline is `default-branch@bb23e7c` (`bb23e7c63305a872326f43c3d52c5edd53e20b43`, committed September 17, collected September 19, 2026). It adds ACH Wallet, optional cardholder-name fields, and local-method automatic presentation. Earlier commit-qualified findings below remain historical reference, not overwritten by this full additive update.

## Evidence Boundary

- The `de90a89` capsule retains 259 files totaling 864,367 bytes and excludes 11 files totaling 393,130 bytes under reviewed capsule policy. The generated comparison identifies eight retained changes from `b5f2df2`.
- The current `bb23e7c` capsule retains 262 files / 877,954 bytes with the same 11 exclusions. Comparison with `de90a89`: three added and 62 modified files; 197 unchanged retained files verified by SHA-256. Under an explicitly approved one-time focused-reading exception, all changed files and prior versions plus affected dependencies were read completely; the entire 532-path full-mode assignment was not semantically reread. Registry and immutable packet remain unchanged.
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

> "Using a clientToken (instead of a bare clientId) lets the Web SDK derive the merchantId it needs internally from the token itself"
>
> `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/files/client/components/applepayPayments/basicOneTimePayment/html/src/app.js:7-10`

> "The Web SDK drives the entire Apple Pay sheet (merchant validation, payment method selection, and authorization) on your behalf."
>
> `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/files/client/components/applepayPayments/basicOneTimePayment/html/src/app.js:94-97`

> "Apple's own apple-pay-sdk.js script is not required here."
>
> `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/files/client/components/applepayPayments/basicOneTimePayment/html/src/index.html:115-120`

## Architecture Baseline at `b5f2df2`

The repository combines static HTML/JavaScript examples, a React/TypeScript multi-flow application, and a Node.js Express backend. The backend uses `@paypal/paypal-server-sdk`, keeps product prices in a server-owned catalog, validates request bodies with Zod, and generates a fresh `PayPal-Request-Id` UUID for create, capture, subscription, and vault operations.

Browser initialization uses either a public client ID or a browser-safe client token. The client-token route requests `response_type=client_token`; `domains[]` is added when configured because Fastlane requires it. Server API credentials remain in environment variables.

## One-Time Checkout

The recommended PayPal flow initializes `paypal-payments`, calls `findEligibleMethods({ currencyCode: "USD" })`, and separately gates PayPal, Pay Later, and Credit buttons. Each button starts its matching one-time-payment session with `presentationMode: "auto"` and a not-yet-awaited create-order promise so browser transient activation is retained. Approval is followed by server-side capture.

Venmo follows the same create, session-start, approve, and capture shape through `venmo-payments` and `createVenmoOneTimePaymentSession()`. The sample checks `isEligible("venmo")`; repository presence alone does not prove a merchant can offer Venmo.

Advanced PayPal examples retain redirect, direct app switch, payment-handler, asynchronous merchant validation, eligibility hydration, sandboxed iframe, and iframe-controlled redirect patterns. The redirect-in-iframe example disables automatic redirect and delegates top-level navigation to the merchant page.

## Cards, Guest Payments, and Fastlane

At `b5f2df2`, Card Fields exposes separate number, expiry, and CVV components. One-time submission returns `succeeded`, `canceled`, or `failed`; only success proceeds to capture. The 3DS variant creates an order with `SCA_ALWAYS` for sandbox testing. HTML save-without-purchase uses a setup token, submits it through `createCardFieldsSavePaymentSession()`, then upgrades it to a payment token server-side. The React exception and later name field are documented below.

Guest Payments supports click-to-open, automatic on-load, and shipping-callback patterns. Shipping callbacks can reject a non-US address or an unavailable shipping option; adding those callbacks changes presentation behavior to a popup or modal.

Fastlane uses a browser-safe client token, `identity.lookupCustomerByEmail()`, member authentication, saved address selection, and `FastlanePaymentComponent().getPaymentToken()`. The resulting single-use card token is sent to the server and placed in `paymentSource.card.singleUseToken`. The README's `/paypal-api/checkout/orders/create` endpoint is stale; the implementation calls `/paypal-api/checkout/orders/create-order-for-card-with-single-use-token`.

## Vault and Subscriptions

The repository demonstrates both `VAULT_WITH_PAYMENT` and `VAULT_WITHOUT_PAYMENT`:

- PayPal purchase plus vault sets `savePayment: true` in the session and `storeInVault: ON_SUCCESS` on the order.
- HTML PayPal and Card Fields save-without-purchase create a setup token, collect approval, upgrade it to a long-lived payment token, and keep that payment token server-side. Database persistence remains a placeholder; the React card flow does not perform that final token exchange.
- Apple Pay purchase plus vault adds `paymentSource.applePay.attributes.vault.storeInVault: ON_SUCCESS` before confirm and capture.

The subscription example initializes `paypal-subscriptions`, requests `RECURRING_PAYMENT` eligibility, and starts `createPayPalSubscriptionPaymentSession()`. The server uses an existing `PAYPAL_SUBSCRIPTION_PLAN_ID` or creates a sample product and active monthly plan before creating the subscription. This demonstrates the API sequence, not complete subscription lifecycle management.

## Apple Pay and Google Pay

The merchant-driven recommended Apple Pay flow requires both SDKs, device capability, merchant/domain validation, and a matching amount between the Apple payment request and PayPal order. It validates the merchant, confirms the order with Apple's token and contacts, then captures. Its setup README also requires enabling Apple Pay on the PayPal app and registering the HTTPS domain.

At `de90a89`, a separate **Basic Apple Pay** example offers a narrower merchant integration. It initializes `applepay-payments` with a browser-safe client token, checks `isEligible("basic_apple_pay")`, creates `createBasicApplePayOneTimePaymentSession()` with approve/cancel/error callbacks, checks `canMakePayments()`, and calls `start()` with a create-order promise. In this path the PayPal Web SDK drives merchant validation, payment-method selection, and authorization, so the example does not load Apple's separate JavaScript SDK. The merchant server still creates and captures the PayPal order.

The existing recommended and vault examples remain merchant-driven: they load Apple's SDK, create `ApplePaySession`, handle Apple's callbacks, call PayPal merchant validation and order confirmation, and then capture. The Basic addition is therefore an alternative orchestration pattern, not a replacement or proof of eligibility.

Google Pay similarly combines the PayPal and Google SDKs. The 3DS example treats `PAYER_ACTION_REQUIRED` specially: it resolves Google's authorization callback so the Google sheet closes, then invokes `initiatePayerAction({ orderId })`, retrieves the order's authentication result, and captures. The example always captures after authentication; production code may instead gate capture on liability-shift and authentication values.

## Local Payment Methods

The current sample catalog contains 46 local-method implementations spanning wallets, bank methods, vouchers, and pay-later products. Each uses a method-specific component, eligibility key, session constructor, sandbox buyer country, and currency.

Most newer examples send `ORDER_COMPLETE_ON_PAYMENT_APPROVAL` and retrieve the completed order after approval. Six retained implementations instead perform an explicit capture: Bancontact, BLIK, EPS, iDEAL, P24, and SEPA.

> [!warning] Contradiction - local-method completion
> The shared README states that local methods are auto-completed and need no separate capture. The six implementations above create without `ORDER_COMPLETE_ON_PAYMENT_APPROVAL` and call the capture route in `onApprove`. Treat completion behavior as method- and implementation-specific until the upstream sample is reconciled.

## React Multi-Flow Application

The `b5f2df2` React capsule declared `@paypal/react-paypal-js@10.1.0`, React 19.2.5, and TypeScript 6.0.2. At `de90a89`, the sample moves to `@paypal/react-paypal-js@^10.4.0`, React/React DOM 19.2.8, TypeScript 6.0.3, and adds `@types/applepayjs@^14.0.9`. Its Apple Pay availability guard now checks the native `ApplePaySession` global with `typeof`, matching the core 11/React 10.4 type migration. `PayPalProvider` continues to use the `/sdk-v6` export with `environment="sandbox"` and loads PayPal, Venmo, Guest Payments, Subscriptions, Card Fields, Messages, Apple Pay, and Google Pay components.

The Node server keeps `@paypal/paypal-server-sdk@^2.4.0`; its `de90a89` package changes are Dotenv and development-tool upgrades, not PayPal API or route behavior changes. The README change only corrects list indentation.

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

## Change from `b5f2df2` to `de90a89`

The generated comparison contains eight paths: two added Basic Apple Pay files and six modified navigation, React, typing, documentation, and package-manifest files. No server route or PayPal Server SDK source changed.

- Adds the Basic Apple Pay one-time-payment example and links it from the sample catalog.
- Moves merchant identity input from browser-safe client ID to browser-safe client token for that Basic flow.
- Replaces merchant-driven Apple lifecycle callbacks with PayPal session callbacks and `start()` for the Basic flow; recommended and vault flows remain unchanged.
- Upgrades the React sample from `@paypal/react-paypal-js ^10.1.0` to `^10.4.0`, adds native Apple Pay typings, and corrects the capability guard.
- Updates React, router, Vite, lint, formatting, and Node development dependencies; `@paypal/paypal-server-sdk ^2.4.0` is unchanged.

## Change from `de90a89` to `bb23e7c`

### ACH Wallet: new HTML client and server route

The new `client/components/bankAchPayments/walletPayment/html/` sample initializes `bank-ach-payments` with a browser-safe client token, a UUID client metadata ID and `pageType: "checkout"`. It checks `ach` eligibility with USD, `ONE_TIME_PAYMENT`, and `100.00`; creates `createBankAchWalletPaymentSession({ standardEntryClassCode: "WEB", ... })`; and connects the `bank-ach-wallet-payments` element to a lazy create-order callback:

```js
const createOrderSession = () => createOrder();
walletSession.connect("bank-ach-wallet-payments", createOrderSession);
```

This excerpt assumes the sample's initialized session and server-backed helper. Unlike the older ACH button's `start()` with an order promise, `connect()` receives a callback for later order creation. No React ACH Wallet implementation is introduced.

Approval calls `POST /paypal-api/checkout/orders/:orderId/capture-ach-wallet`. The new handler retrieves the order; returns early on a non-200 GET response; constructs a record with order ID, optional bank name/last digits/account holder, first purchase-unit amount/currency, and server timestamp; calls `storeConsent()`; then captures using `return=minimal` and a fresh request UUID. `.env.sample` now includes ACH Wallet in its `DOMAINS` guidance; the existing auth endpoint conditionally passes `domains[]`.

> [!warning] Contradiction - ACH consent storage and approval enforcement
> The README describes storing consent, but `storeConsent()` only calls `console.log`. The comment says the order must be APPROVED, but the handler does not inspect `orderDetails.status` before capture. A TypeScript assertion accesses optional `bank.achDebit` fields not modeled by the declared response type; it neither validates them nor proves deserialization retains them. This sample is not evidence of durable consent storage, regulatory compliance, or final settlement. See [[paypal-ach]].

The wallet's hardcoded USD 100 eligibility amount also differs from its empty create-order request: the server default catalog cart totals USD 205 (two USD 75 items plus one USD 55 item). This default-cart pattern already exists in the older ACH button. Align eligibility and order amounts when adapting either example. The new README describes US merchants/USD and links a limited-release guide; treat that as snapshot guidance, not verified current enablement.

### Optional cardholder name, including React

HTML recommended, 3DS and save-card examples add and mount `createCardFieldsComponent({ type: "name", placeholder: "Name" })`. The README calls this optional. The two HTML one-time variants replace the example billing postal code `95131` with `countryCode: "US"`; this does not remove postal-code requirements for all integrations.

The React sample declares `@paypal/react-paypal-js ^10.5.0` (previously `^10.4.0`) and imports `PayPalCardNameField` from `/sdk-v6` for both one-time and save-card forms. Field-only excerpt, rendered inside the existing `PayPalCardFieldsProvider` and initialized payment session:

```tsx
import { PayPalCardNameField } from "@paypal/react-paypal-js/sdk-v6";

<PayPalCardNameField
  placeholder="Enter name"
  containerStyles={{ height: "3rem" }}
/>
```

The one-time parent wires validation handlers into that provider. The hook retains required number, expiry and CVV checks and adds this optional-name condition:

```ts
(!fieldsState.name || fieldsState.name.isEmpty || fieldsState.name.isValid)
```

An absent/empty name is accepted; a populated invalid name is not. Validity, empty/notempty, and blur events update the field state. Successful one-time submission is checked through `submitResponse.state === "succeeded"` before a separate server capture. The snippet is not a complete checkout and does not establish payment success.

> [!warning] Contradiction - React save-card completion
> The React save-card page has a bare Card Fields provider without this validation hook. It displays success after setup-token submission, without calling the final payment-token endpoint. The HTML save-card flow does call `/paypal-api/vault/payment-token/create`, but the server's `savePaymentTokenToDatabase()` is empty. This corrects the earlier broad vault description; the React gap was already present at `de90a89`, not introduced by the name field. See [[paypal-vault]].

### Local-method presentation and dependencies

All 46 local-method HTML implementations change `presentationMode: "popup"` to `presentationMode: "auto"`. Session callbacks and completion strategy are unchanged: Bancontact, BLIK, EPS, iDEAL, P24 and SEPA still explicitly capture; the other 40 use order auto-completion plus retrieval. `auto` delegates presentation choice, not proof of browser-specific behavior.

> [!warning] Contradiction - local-method presentation guidance
> The shared README and some comments still describe popup mode, while code requests auto. The independently collected React 10.5.0 LPM wrappers are typed popup-only; do not assume the HTML change updates that package contract. See [[paypal-apm]] and [[source-github-paypal-js]].

The Node sample moves `@paypal/paypal-server-sdk ^2.4.0` to `^2.5.0`, alongside environment/tooling updates. These manifest ranges do not establish exact installed versions or ingest the Server SDK's own release behavior. Existing Apple Pay, Google Pay, PayPal, Venmo, Fastlane and subscription implementation files are unchanged by hash. The externally hosted Web SDK runtime remains outside this snapshot.

### Exact evidence for this update

Paths below are under `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-09-19-bb23e7c/files/`:

- `client/components/bankAchPayments/walletPayment/html/README.md` and `src/recommended/app.js` (session at line 61; `connect()` at line 99), plus its HTML entry point.
- `server/node/src/routes/ordersRouteHandler.ts:533-599` - consent logging and capture; `src/routes/index.ts` - route; `src/productCatalog.ts` - default-cart prices.
- `client/prebuiltPages/react/src/hooks/useCardFieldsValidation.ts:94` - optional-name condition; `src/payments/oneTimePayment/components/PayPalCardFieldsOneTimePayment.tsx` and `src/payments/savePayment/components/PayPalCardFieldsSavePayment.tsx` - field and completion code.
- `client/components/localPaymentMethods/idealPayments/html/src/app.js:98` - representative `auto` option; all 46 changed implementations were read, not inferred from this one example.
- `client/prebuiltPages/react/package.json` and `server/node/package.json` - declared ranges, not lockfile resolutions.

## Related

- Company: [[paypal]]
- Checkout: [[paypal-checkout]]
- ACH: [[paypal-ach]]
- Card fields: [[paypal-expanded-checkout]]
- Local methods: [[paypal-apm]]
- Fastlane: [[paypal-fastlane]]
- Vaulting: [[paypal-vault]]
- Subscriptions: [[paypal-subscriptions]]
- Apple Pay: [[paypal-apple-pay]]
- Google Pay: [[paypal-google-pay]]
- Repository history: [[changelog-github-v6-web-sdk-sample-integration]]

## Raw Sources

- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-09-19-bb23e7c/manifest.json` - immutable exact-SHA capsule for ACH Wallet, card-name and LPM presentation update
- `tracking/github/repos/paypal/v6-web-sdk-sample-integration/comparisons/default-branch/de90a89--bb23e7c/comparison.json` - 65 changed paths, 197 unchanged
- `tracking/github/repos/paypal/v6-web-sdk-sample-integration/ingest-review-9b81f89d.md` - user-approved focused-reading exception and operator review record

- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/manifest.json` - immutable exact-SHA snapshot for the Basic Apple Pay delta
- `tracking/github/repos/paypal/v6-web-sdk-sample-integration/comparisons/default-branch/b5f2df2--de90a89/comparison.json` - generated eight-path comparison
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/files/client/components/applepayPayments/basicOneTimePayment/html/src/app.js` - Basic Apple Pay initialization, eligibility, session, order, and capture orchestration
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/files/client/components/applepayPayments/basicOneTimePayment/html/src/index.html` - Basic flow scripts and UI entry point
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/files/client/prebuiltPages/react/package.json` - React 10.4 and Apple Pay typing dependencies
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/manifest.json` - immutable exact-SHA baseline at `b5f2df209b0bfd10b1a3cde600088ddf21e43523`
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/README.md` - repository scope and setup
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/client/components/localPaymentMethods/README.md` - current local-method catalog and shared guidance
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/client/prebuiltPages/react/README.md` - React application overview and declared versions
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/server/node/src/routes/ordersRouteHandler.ts` - order construction, retrieval, and capture
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/server/node/src/routes/vaultRouteHandler.ts` - setup-token and payment-token flow
- `raw/github-paypal-v6-samples.md` - legacy review pointer at `dd9ef8a53c71d9d2107ad94c23b73b62f9811258`

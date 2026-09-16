---
title: "GitHub: braintree/braintree-web"
type: source
date_ingested: 2026-07-28
date_updated: 2026-09-16
original_format: github-repo
raw_files:
  - "github/braintree/braintree-web/snapshots/2026-09-15-732ed09/manifest.json"
  - "github/braintree/braintree-web/snapshots/2026-07-28-41460fb/manifest.json"
  - "github/braintree/braintree-web/snapshots/2026-07-27-bae582d/manifest.json"
tags: [braintree, javascript-sdk, checkout, hosted-fields, venmo, paypal, 3d-secure, github-repository]
---

## Overview

`braintree/braintree-web` contains Braintree's modular browser SDK. The retained history begins with `braintree-web@3.143.0`; the latest retained release is `braintree-web@3.145.0` at exact SHA `732ed094354d650605e678d98246ce6332952ad3`. The `3.143.0` baseline and `3.144.0` additions remain preserved below.

Repository: <https://github.com/braintree/braintree-web>

## Evidence Boundary

- The snapshots prove implementation present in the retained `braintree-web@3.143.0`, `3.144.0`, and `3.145.0` releases. They do not replace current product documentation or prove merchant, buyer, country, or payment-method eligibility.
- The package exposes SDK components, not Braintree Web Drop-in. Drop-in is a separately versioned repository.
- The latest snapshot retains 28 stories that show intended integration scenarios. Tests, fixtures, and mocks are excluded, so test-only behavior is outside this capsule.
- PayPal Checkout v6 and Fastlane delegate runtime behavior to PayPal SDKs. This source covers the Braintree adapters and nonce boundary, not the complete delegated runtimes.
- Legacy modules retained in source, including Masterpass and Visa Checkout, are implementation history rather than evidence that merchants should start new integrations with them.

## Grounding Excerpts

> "A suite of tools for integrating Braintree in the browser."
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/README.md:3`

> "For a ready-made payment UI, see Braintree Web Drop-in."
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/README.md:7`

> "Instances of this class can load the PayPal SDK, create payment sessions, and tokenize payments."
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/src/paypal-checkout-v6/paypal-checkout-v6.js:31`

> "single_use - intended as a one time transaction"
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/src/venmo/index.js:50-52`

> "Update Fastlane SDK loader package from `@paypal/accelerated-checkout-loader` to `@paypal/fastlane-sdk-loader`"
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/CHANGELOG.md:5-7`

> "**Edit FI (Funding Instrument)** allows returning buyers with a vaulted Billing Agreement to view and change their saved PayPal payment method inline during checkout."
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/files/.storybook/stories/PayPalCheckout/PayPalCheckoutEditFI.stories.ts:28`

> "Requires the client token to have been generated with a `preferredPaymentMethodToken`. Only applicable to the `checkout` flow."
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/files/src/paypal-checkout/paypal-checkout.js:549`

> "When `true`, prompts the customer for a shipping address."
>
> `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/files/src/paypal-checkout-v6/paypal-checkout-v6.js:1436`

> "Fix venmo.create() failing to create when isIncognito promise fails"
>
> `raw/github/braintree/braintree-web/releases/braintree-web/3.144.0/2026-07-28/release-notes.md:10-11`

### 3.145.0 Grounding Excerpts

> `return loadClientScript(src, true);`
>
> `raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/lib/create-deferred-client.js:41`

> `if (account.details && account.details.implicitlyVaultedPaymentMethodToken) {`
>
> `raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/paypal-checkout-v6/paypal-checkout-v6.js:2719`

> `return Promise.reject(new BraintreeError(errors.VENMO_ECD_DISABLED));`
>
> `raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/venmo/venmo.js:136`

> `convertToBraintreeError(err, errors.FASTLANE_SDK_LOAD_ERROR)`
>
> `raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/fastlane/fastlane.js:58`

## Package and Client Architecture

The top-level package exports 23 components. Each component can be consumed from the aggregate `braintree-web` package or as an individual browser/CommonJS/AMD module. Most creation methods accept either an existing `Client` or authorization from which the SDK creates a deferred client, and asynchronous methods support promises when no callback is supplied.

The client parses a tokenization key or client token, retrieves gateway configuration, and provides REST and GraphQL request paths. Browser metadata and SDK version are attached to requests. The merchant server remains responsible for generating client tokens when required and for consuming browser-generated payment-method nonces.

## Hosted Fields and Cards

Hosted Fields injects Braintree-hosted frames into merchant-selected containers for card number, CVV, expiration, postal code, and cardholder name. The merchant controls supported styling and listens for focus, emptiness, validity, card-type, submit-request, and BIN events without hosting sensitive field inputs directly.

`tokenize()` validates field state, sends the card data through the client, and returns a payment-method nonce and card details. A CVV-only path can tokenize against an existing authorization fingerprint. The README distinguishes this iframe model from direct card submission through the lower-level client API, which changes PCI scope.

The broader card surface includes American Express rewards-balance verification and UnionPay capability, enrollment, and tokenization flows. Vault Manager can delete a vaulted payment method, but this client operation does not describe the server-side vault lifecycle.

## 3D Secure

The 3D Secure component verifies a card nonce and BIN with transaction amount and optional account, exemption, challenge, customer, billing, shipping, device, and custom-field data. A merchant can inspect lookup data before calling `next()` to continue a challenge, initialize a challenge from a server-side lookup response, or prepare browser data for a server lookup.

The result includes a new nonce plus `liabilityShifted` and `liabilityShiftPossible`; source examples explicitly leave acceptance decisions to the merchant when liability does not shift. The retained implementation supports 3DS2 framework and modal/iframe orchestration and includes historical 3DS1 compatibility notes.

## PayPal Checkout v6

`paypalCheckoutV6` coordinates Braintree with PayPal Web SDK v6. It can:

- load and initialize the PayPal SDK;
- discover eligible PayPal, Pay Later, and Credit methods;
- create one-time, Pay Later, checkout-with-vault, and billing-agreement sessions;
- create PayPal Messages;
- start, focus, and close vault-initiated checkout for repeat purchases; and
- convert approval identifiers or billing tokens into Braintree payment-method nonces.

Session options cover amount, currency, intent, shipping callbacks, contact preferences, address overrides, commit behavior, and billing-agreement plan metadata where applicable. Eligibility and method presence in code do not establish account enablement.

At `3.144.0`, the shared v6 payment-session path also forwards optional locale, landing-page type, user action, risk-correlation ID, shipping-address enablement, and shipping-address editability. Checkout-with-vault can additionally carry `planType` and formatted `planMetadata` for recurring, subscription, unscheduled, or installment agreement patterns. These are client-side request capabilities; product availability and valid combinations still depend on current Braintree and PayPal guidance.

### Checkout-with-Vault Tokenization in 3.145.0

Previously, the presence of `billingToken` selected the billing-agreement-only request. In `3.145.0`, the adapter distinguishes three cases:

| Approval input | Request behavior |
| --- | --- |
| Billing token without order/payment identifier | Pure billing-agreement vaulting; `vault: false` can opt out of automatic vaulting on this branch. |
| Order/payment identifier plus payer identifier, without billing token | One-time checkout tokenization. |
| Billing token plus order/payment identifier and payer identifier | Checkout-with-vault; sends `billingAgreementToken` together with the checkout fields. |

`orderID`/`orderId`, `paymentID`/`paymentId`, and `payerID`/`payerId` aliases are accepted. Checkout branches require the payer identifier; billing-token-only vaulting does not. The adapter posts to Braintree `payment_methods/paypal_accounts`. It conditionally copies `account.details.implicitlyVaultedPaymentMethodToken` into the returned payload, so the release note's returning-token wording must not be read as an unconditional guarantee. This remains Braintree tokenization, not a direct Orders API capture.

The v6 SDK-loading path now uses the shared asset loader with `forceScriptReload: true` when a load is needed, reports enriched load-failure analytics, and retains underlying error detail. The existing early return when `window.paypal.version` is present remains; this is not proof that every call reloads the SDK. The non-v6 loader is a separate implementation.

## PayPal View/Edit Funding Instrument

`3.144.0` adds a non-v6 `paypalCheckout` path for a returning buyer to view or change the PayPal funding instrument behind an existing vaulted Billing Agreement. The merchant must generate the Braintree client token with a `preferredPaymentMethodToken`, call checkout `createPayment()` with `editBillingAgreement: true`, and use the PayPal SDK's `SavedPaymentMethods` component.

The SDK exchanges the client token's `paymentMethodIdJwt` for a billing-agreement JWT and supplies it to the PayPal SDK as `data-user-id-token`, unless the merchant explicitly supplied that data attribute. The edit flag adds `editBillingAgreementJwt` only to the `checkout` flow, not the vault flow. If the JWT exchange fails, initialization continues without the generated token, so the release does not guarantee that Edit FI will be available for every returning buyer.

## Venmo

The standalone Venmo component tokenizes through mobile app switch and optional fallback experiences. Browser support is configuration-sensitive: merchants can restrict new tabs and webviews, allow non-default browsers, choose iOS redirect/manual-return handling, and control cancellation when the buyer returns early.

Desktop support can render a QR flow, while optional desktop or mobile web login provides a non-app path. `paymentMethodUsage` declares `single_use` or `multi_use`; the latter is intended for a nonce that will be vaulted and reused through Braintree. Merchant eligibility, supported environments, and server processing still require product guidance beyond this source snapshot.

In `3.144.0`, rejection of the asynchronous incognito-detection check no longer rejects `venmo.create()`. The SDK falls back to an unknown, non-private result and continues normal client creation and Venmo enablement checks. This is failure isolation, not evidence that Venmo is supported in private browsing.

### Desktop QR Changes in 3.145.0

Desktop QR now receives `collectCustomerBillingAddress` and `collectCustomerShippingAddress`. Requesting either flag requires gateway configuration `payWithVenmo.enrichedCustomerDataEnabled`; otherwise desktop creation rejects with `VENMO_ECD_DISABLED` before the desktop-setup fallback. For the modern mutation selected by a nonempty `paymentMethodUsage`, truthy flags are forwarded under `paysheetDetails`. The legacy QR mutation used without `paymentMethodUsage` does not forward them. The retained DesktopQR story uses `single_use` and requests both addresses; returned `payerInfo` still depends on the backend response.

The modal refresh adds a rescan action on the waiting face, distinct rescan/error-view analytics, custom fonts, and a larger branded QR canvas rendered with the new `qrcode@1.5.4` dependency. Rescan requests a new payment context and polling cycle. The waiting text and UI state do not establish approval or payment completion; the result remains driven by the payment-context response. QR rendering validates HTTPS and the `venmo.com` hostname. The mobile hash-change flow now shares the cross-browser document-visibility helper.

## Loading and Popup Recovery in 3.145.0

- **Deferred client:** when client script loading is needed, any initial load rejection triggers one forced reload. The implementation does not restrict this retry to a diagnosed suspend failure. Successful client creation after retry emits recovery analytics; final load errors include the failure kind and `details.originalError`. Existing-client and already-loaded-client paths remain separate.
- **Shared FrameService:** targets the dispatch frame explicitly and adds domain verification, delayed visibility-listener installation (500 ms), suspend/resume callbacks, and a delayed closed-frame check (1,000 ms) after a recorded suspend. Cleanup removes listeners and timers. PopupBridge takes a separate early-return path.
- **PayPal and LocalPayment:** non-v6 vault-initiated checkout and popup-based local payments wire suspend/resume/recovered analytics into FrameService. A recovered event is emitted on a successful popup callback before tokenization; it is not proof of a nonce, authorization, or settlement. This is not automatic popup reopening or payment resumption.
- **FraudNet:** load failure emits enriched analytics when a client is supplied and still resolves to `null`. DataCollector can reject if no collector instance remains; analytics does not turn missing device data into success.
- **Fastlane:** the load/initialization catch uses error conversion. Existing Braintree errors pass through; other errors become `FASTLANE_SDK_LOAD_ERROR` with the original error retained. The delegated loader remains `@paypal/fastlane-sdk-loader@1.2.1`.

## Other Payment and Decision Surfaces

- Apple Pay and Google Pay adapters build wallet configuration and parse wallet responses into Braintree nonces.
- Local Payment starts popup, redirect, app-switch, and selected QR flows for configured local methods; retained code includes Swish, crypto, BLIK, MB WAY, Bancomat Pay, and pay-upon-invoice branches.
- US bank account and Instant Verification cover bank login/verification and ACH mandate details; SEPA creates mandate and nonce data.
- Data Collector combines enabled fraud-device signals into device data for server transactions.
- Payment Ready creates or updates a customer session from hashed identifiers and device/app signals, then requests payment recommendations.
- Preferred Payment Methods supplies browser/device preference signals; it is not payment-method eligibility.

## Fastlane Dependency

The Braintree Fastlane component loads and initializes the external Fastlane SDK with Braintree configuration and optional device data. At `3.143.0`, the package depends on `@paypal/fastlane-sdk-loader@1.2.1`.

The exact release replaces the previous loader package name but does not establish a Fastlane product-behavior change. Questions about identity, profile, checkout UI, or delegated payment behavior must also consult current Fastlane documentation or an independently retained runtime source.

## `3.143.0` Release Findings

The release updates `credit-card-type` to `10.2.0` and replaces `@paypal/accelerated-checkout-loader` with `@paypal/fastlane-sdk-loader`. No migration action or direct payment-flow change is documented in the release notes.

All broader findings above are the cumulative baseline present at the exact release SHA, not changes introduced by `3.143.0`.

## `3.144.0` Release Findings

The release adds PayPal View/Edit Funding Instrument support, expands PayPal Checkout v6 payment-resource and session options, updates `framebus` from `6.0.3` to `6.1.0`, and prevents failed incognito detection from aborting `venmo.create()`.

The exact-SHA comparison contains 319 byte-identical retained files, 10 changed files, and one added Edit FI story relative to `3.143.0`. The durable architecture sections remain valid; the additions above identify the material payment-flow changes without replacing the earlier baseline.

## `3.145.0` Release Findings

The `2026-08-24` release fixes PayPal v6 checkout-with-vault tokenization, extends Venmo desktop address passthrough and QR presentation, and improves script-load and popup recovery diagnostics. `@braintree/asset-loader` changes from `2.0.3` to `2.1.0`; `qrcode@1.5.4` is added. The repository package adds an npm engine constraint of `>11.7.0`; this is not a browser-support requirement.

The approved high-priority delta compares `3.144.0` to `3.145.0`: two retained files added, 27 modified, and 303 byte-identical. Every changed retained file and its patch was read fully. The user approved mechanical disposition checking for excluded upstream test/lockfile/tooling changes for this item only. Snapshot integrity and all 47 upstream dispositions were checked; this is not a claim to have read the entire upstream repository or run its payment flows.

## Related

- [[changelog-github-braintree-web]] — package-qualified release ledger
- [[braintree]] — company and knowledge-status page
- [[braintree-web-sdk]] — product concept and integration boundaries
- [[paypal-braintree-integration]] — PayPal v6/Braintree nonce flow
- [[paypal-fastlane]] — delegated Fastlane product concept

## Raw Sources

- [3.145.0 snapshot manifest](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/manifest.json)
- [3.145.0 release manifest](../../../../raw/github/braintree/braintree-web/releases/braintree-web/3.145.0/2026-09-15/manifest.json)
- [3.145.0 release notes](../../../../raw/github/braintree/braintree-web/releases/braintree-web/3.145.0/2026-09-15/release-notes.md)
- [3.144.0 to 3.145.0 comparison](../../../../tracking/github/repos/braintree/braintree-web/comparisons/braintree-web/3.144.0--3.145.0/comparison.md)
- [PayPal v6 implementation](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/paypal-checkout-v6/paypal-checkout-v6.js)
- [Venmo implementation](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/venmo/venmo.js) and [desktop context/polling](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/venmo/external/venmo-desktop.js)
- [QR renderer](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/venmo/internal/ui-elements/qr-code-view.js)
- [Deferred client loader](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/lib/create-deferred-client.js) and [FrameService](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/lib/frame-service/external/frame-service.js)
- [Non-v6 PayPal](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/paypal-checkout/paypal-checkout.js) and [LocalPayment](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/local-payment/external/local-payment.js)
- [FraudNet](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/data-collector/fraudnet.js) and [DataCollector caller](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/data-collector/index.js)
- [Fastlane adapter](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/fastlane/fastlane.js) and [package dependencies](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/package.json)

- Snapshot manifest: `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/manifest.json`
- Release manifest: `raw/github/braintree/braintree-web/releases/braintree-web/3.144.0/2026-07-28/manifest.json`
- Release notes: `raw/github/braintree/braintree-web/releases/braintree-web/3.144.0/2026-07-28/release-notes.md`
- Comparison manifest: `tracking/github/repos/braintree/braintree-web/comparisons/braintree-web/3.143.0--3.144.0/comparison.json`
- Readable comparison: `tracking/github/repos/braintree/braintree-web/comparisons/braintree-web/3.143.0--3.144.0/comparison.md`
- Edit FI story: `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/files/.storybook/stories/PayPalCheckout/PayPalCheckoutEditFI.stories.ts`
- PayPal Checkout: `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/files/src/paypal-checkout/paypal-checkout.js`
- PayPal Checkout v6: `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/files/src/paypal-checkout-v6/paypal-checkout-v6.js`
- Venmo entry point: `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/files/src/venmo/index.js`
- Snapshot manifest: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/manifest.json`
- Release manifest: `raw/github/braintree/braintree-web/releases/braintree-web/3.143.0/2026-07-27/manifest.json`
- Release notes: `raw/github/braintree/braintree-web/releases/braintree-web/3.143.0/2026-07-27/release-notes.md`
- Package manifest: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/package.json`
- Component registry: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/components.json`
- Hosted Fields: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/src/hosted-fields/`
- 3D Secure: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/src/three-d-secure/`
- PayPal Checkout v6: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/src/paypal-checkout-v6/`
- Venmo: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/src/venmo/`

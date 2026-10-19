---
title: "GitHub: braintree/braintree-web"
type: source
date_ingested: 2026-07-28
date_updated: 2026-10-19
original_format: github-repo
raw_files:
  - "github/braintree/braintree-web/snapshots/2026-10-19-f3357c4/manifest.json"
  - "github/braintree/braintree-web/snapshots/2026-09-27-893d4e7/manifest.json"
  - "github/braintree/braintree-web/supplements/2026-09-27-893d4e7-1540eb0a/manifest.json"
  - "github/braintree/braintree-web/snapshots/2026-09-15-732ed09/manifest.json"
  - "github/braintree/braintree-web/snapshots/2026-07-28-41460fb/manifest.json"
  - "github/braintree/braintree-web/snapshots/2026-07-27-bae582d/manifest.json"
tags: [braintree, javascript-sdk, checkout, hosted-fields, venmo, paypal, 3d-secure, github-repository]
---

## Overview

`braintree/braintree-web` contains Braintree's modular browser SDK. The retained history begins with `braintree-web@3.143.0`; the latest ingested release is `braintree-web@3.147.0` at exact SHA `f3357c49c7b71f079d031c3ddf89cdfe444f6511`. All earlier version findings remain preserved below.

Repository: <https://github.com/braintree/braintree-web>

## Evidence Boundary

- The snapshots prove implementation present in the retained `braintree-web@3.143.0` through `3.147.0` releases. They do not replace current product documentation or prove merchant, buyer, country, or payment-method eligibility.
- The package exposes SDK components, not Braintree Web Drop-in. Drop-in is a separately versioned repository.
- The `3.146.0` snapshot adds the Edit Saved Payment story to the earlier 28 stories. Tests, fixtures, and mocks remain excluded; the approved helper supplement does not change future collection policy.
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

### v6 View/Edit Saved Payment in 3.146.0

`createEditSavedPaymentSession()` extends Edit FI to the v6 adapter. This is not the first returning-buyer support: vault-initiated checkout already exists in the retained `3.143.0` baseline. It is also separate from the non-v6 `3.144.0` path above.

1. Resolve the authenticated buyer's existing vaulted PayPal payment-method token. For a new buyer, the story first creates a billing agreement, tokenizes approval, and calls its vault helper to obtain the persistent `legacyId`. An existing returning buyer skips that setup; a one-time nonce is not the preferred vaulted token.
2. Generate a client token with the preferred payment-method context, then create a fresh Braintree client and `paypalCheckoutV6` instance. The sample helper's `preferredPaymentMethodToken` maps to GraphQL `input.clientToken.paymentMethodId`.
3. Place `<paypal-saved-payment-methods>` in the DOM before `loadPayPalSDK()`. Create the edit session with `amount`, `currency`, and `onApprove`; defaults are `intent: "authorize"`, `commit: false`, and presentation mode `auto`.
4. The adapter lazily exchanges `paymentMethodIdJwt` for a billing-agreement JWT, initializes the `paypal-saved-payment-methods` component, and eagerly creates the delegated edit session so the saved-method iframe can render before a click. It passes the resulting JWT as `billingAgreementIdToken`.
5. On buyer interaction, call `session.start()`. The adapter creates a checkout payment resource and passes its order promise to the delegated session. The payment resource's `editBillingAgreementJwt` field uses the original `paymentMethodIdJwt`, not the exchanged display JWT.
6. On approval, call `tokenizePayment({ orderId, payerId })` and send the nonce to the merchant server. Approval, display, and tokenization are not transaction authorization or settlement. This is a checkout-bound edit flow, not evidence for standalone vault-management or direct PayPal Orders API processing.

**Failure boundaries:** absent payment-method JWT throws `PAYPAL_CHECKOUT_V6_EDIT_SAVED_PAYMENT_NOT_SUPPORTED`. Billing-agreement JWT exchange failure logs a warning and allows the edit attempt to continue; a successful setup call does not establish successful iframe authentication. Session creation/start and tokenization need their own error handling. The amount/currency/onApprove guard checks truthiness, not complete input validity.

**Demo safety:** the fully retained helper is sandbox tooling, not a production backend. It performs Basic-authenticated GraphQL requests in the browser using environment-supplied credentials, and may fall back to a static token when generation fails. Keep these requests, authenticated-buyer ownership checks, and trusted amount calculation server-side in production. A static fallback does not guarantee the preferred-method context. Do not copy the story's raw nonce/error display into production.

**Presentation forwarding:** one-time, Pay Later, checkout-with-vault, billing-agreement, and edit session paths now pass `autoRedirect` and `fullPageOverlay` through to the hosted SDK. Start-level options take precedence through a truthy fallback; this is not evidence that all presentation modes or arbitrary nested options are supported.

**Package boundary:** the new adapter method is in `braintree-web@3.146.0`. The independently retained PayPal JS core `11.1.1` / React `10.5.1` declarations and v6 React surface do not expose a dedicated typed edit API/wrapper. This does not establish absence in the remotely hosted PayPal runtime. See [[source-github-paypal-js]].

### 3.146.0 Grounding Excerpts

- `Requires the client token to have been generated with a` followed by `preferredPaymentMethodToken` in `files/src/paypal-checkout-v6/paypal-checkout-v6.js:2177` (JSDoc).
- `billingAgreementIdToken: self._billingAgreementJwt,` in the same file, delegated edit-session options.
- `variables.input.clientToken.paymentMethodId = preferredPaymentMethodToken;` in the supplemental `.storybook/utils/sdk-config.ts`.
- `var DANGEROUS_KEYS = ["__proto__", "constructor", "prototype"];` in `files/src/hosted-fields/internal/models/evented-model.js:5`.

## Hardening in 3.146.0

Hosted Fields' EventedModel `get()` and `set()` reject path segments named `__proto__`, `constructor`, or `prototype`, including the terminal setter key. This is a bounded property-path guard, not proof of universal prototype-pollution protection.

Payment Request configures `verifyDomain: isVerifiedDomain`, initially empty target frames, and adds its internal iframe after creation. The existing verifier requires HTTPS and an allowed PayPal/Braintree base hostname. Payment Request internal messaging, 3DS authentication completion, and UnionPay internal messaging explicitly target `window.parent`. `framebus` changes from `6.1.0` to `6.2.0`; dependency internals and hosted-browser acceptance were not tested in this ingest.

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

## `3.146.0` Release Findings and Reading Scope

Released 2026-09-15 and collected 2026-09-27. The user approved full additive ingest for the new payment flow, overriding the script's delta recommendation, with a one-time focused-reading exception. The comparison has one added and twelve modified retained files and 320 unchanged files. Changed implementation/content, the complete new story and helper, affected local dependencies, and prior behavior were reviewed; unchanged snapshot files and cumulative changelog history were checked mechanically. All 665 file hashes across the two snapshots matched. Older source/changelog history remains intact. This is not a claim to have reread the complete repository, run its tests, or executed payment flows.

The helper is an immutable exact-SHA supplement linked through work item `github-9eb53b57a85a75efdb3e`. The original snapshot and collection-time packet remain unchanged.

## `3.147.0` App-Switch Return, Locale and BIN Hardening

Released 2026-10-12; additive full ingest on 2026-10-19 against `3.146.0`. The user approved full mode with focused reading, overriding the packet's delta/high recommendation because SDK initialization and redirect recovery change. The snapshot retains 333 files: eight modified, 325 unchanged, none added/removed. All 666 prior/current file hashes and sizes were verified. Review fully covered changed implementation/content and affected prior/dependency code; unchanged source sections, cumulative changelog history, manifests and duplicated diff inventories were checked mechanically. The effective full list is 342 paths, not a claim of 342 semantic full-file reads or a whole-upstream-tree audit. No supplemental collection was needed.

### Return Check and Resume

The [v6 adapter](../../../../raw/github/braintree/braintree-web/snapshots/2026-10-19-f3357c4/files/src/paypal-checkout-v6/paypal-checkout-v6.js) adds `hasReturned(url?)` and `resume(urlOrQueryItems?)` to the common payment-session wrapper and the billing-agreement wrapper. The common payment path serves one-time PayPal/Credit, Pay Later and checkout-with-vault; billing agreements choose PayPal or Credit without purchase. This is redirect/app-switch recovery, not the introduction of returning-buyer checkout or saved-payment editing, which have separate preserved histories above. No new return-helper API is established for Edit Saved Payment or vault-initiated checkout by these changes.

On the return page, load the SDK, recreate the appropriate session with its configuration and callbacks, await `hasReturned()`, then resume only if true. URL/query arguments are forwarded to the hosted SDK; these adapter methods do not themselves parse or authenticate every return parameter. `_getOrCreateAppSwitchSession` lazily creates and memoizes a delegated session for the return-check/resume pair, so this page does not need to call `start()` first. Resume delegates directly without making a fresh order/billing-token request in this wrapper; approval tokenization and merchant-server transaction processing remain separate.

Illustrative return branch, adapted from the retained JSDoc; `checkout` is the Braintree `paypalCheckoutV6` instance and `options` includes trusted amount/currency, return/cancel URLs and merchant-owned approval/cancel/error handling. Not executed:

```javascript
await checkout.loadPayPalSDK();
const session = checkout.createOneTimePaymentSession(options);
if (await session.hasReturned()) {
  await session.resume();
} else {
  // Attach session.start(...) to the buyer's payment-button interaction.
}
```

**Failure and lifecycle limits:** `hasReturned()` returns a Promise, so a synchronous `if (session.hasReturned())` tests the Promise rather than the boolean result. A missing ready instance and pending initialization promise produces `PAYPAL_CHECKOUT_V6_INSTANCE_NOT_READY`. The return-session cache retains that rejected promise and other asynchronous creation failures; later SDK loading alone does not repair the same wrapper. Initialize first; after resolving a setup failure, create a fresh appropriate session wrapper rather than assuming a cached retry. The ready-instance session factory may also throw synchronously, so keep setup inside error handling. `start()` still creates its own delegated session and retains the synchronous-ready/user-activation path; do not assume a prior return check makes every fresh `start()` Safari-safe.

Return-check true/false and resume started/succeeded/failed analytics are added. Resume resolution or its success event is not authoritative authorization, capture, settlement or merchant enablement. The merchant still validates order/buyer context and consumes the approved nonce through its Braintree server flow. No hosted-SDK execution or return-path test was performed.

### Locale Forwarding and Shared State

`_initializePayPalInstance` now accepts locale and normalizes underscores to hyphens (`fr_FR` -> `fr-FR`). New SDK instances receive it in `createInstance` options. Existing instances use `updateLocale` only if available; pending instance promises apply it after resolution. One-time, Pay Later, checkout-with-vault and billing-agreement creators forward their locale. `findEligibleMethods()` now reuses the shared checkout initialization/promise path instead of unnecessarily creating a separate instance. This fixes an earlier gap between forwarding locale in the payment request and applying it to hosted SDK UI.

The module caches locale with the owning `window.paypal` reference so later component types without an explicit locale can reuse it; replacement of that global invalidates the cached lookup. This is page-wide language state, not isolated per button or wrapper. Existing-instance updates remain conditional on the delegated `updateLocale` method. Coordinate language changes and check actual UI in the merchant integration rather than assuming independent concurrent locales.

> [!warning] Contradiction
> Initializer comments describe the last successfully applied locale, but the new-instance/pending paths record the request before successful resolution and do not restore the earlier locale when creation fails. The cache can therefore retain a failed/pending request. This is not transactional locale rollback or confirmation of the displayed language. The same version-qualified discrepancy is recorded in [[paypal-braintree-integration]].

### Hosted Fields BIN-Length Validation

The [external constructor](../../../../raw/github/braintree/braintree-web/snapshots/2026-10-19-f3357c4/files/src/hosted-fields/external/hosted-fields.js) copies merchant options, validates the copied `binVerificationLength`, then makes that property non-writable and non-configurable before frame configuration is forwarded. This avoids repeatedly invoking a changing getter and forwarding a different value from the one validated. Public input remains numeric 6 or 8, or omission; an invalid supplied value throws `INSTANTIATION_OPTION_INVALID`. This is not a new arbitrary BIN-length option.

The separate [internal card model](../../../../raw/github/braintree/braintree-web/snapshots/2026-10-19-f3357c4/files/src/hosted-fields/internal/models/credit-card-form.js) normalizes missing/invalid values to the [shared default](../../../../raw/github/braintree/braintree-web/snapshots/2026-10-19-f3357c4/files/src/hosted-fields/shared/constants.js) of 6 before number-change/BIN events use it. Do not describe the internal fallback as public acceptance of invalid merchant configuration. The constructor's frozen property does not freeze the entire configuration or establish comprehensive card-data/security protection.

### Dependencies, Migration and Limits

`inject-stylesheet` changes 7.0.0 -> 7.1.0. `framebus` remains 6.2.0, `credit-card-type` 10.2.0 and Fastlane loader 1.2.1. The dependency implementation was not audited; no new runtime behavior is inferred from its bump. All 13 upstream changes reconcile to eight retained changes and five policy exclusions (three tests, lockfile, release tooling). Excluded test changes are not executed evidence.

No mandatory migration is stated in the release notes. For adopters, verify awaited return detection, correct return-session recreation, missing SDK/initialization failure and retry, cancellation, nonce/server processing, page-wide locale coordination, and omitted/6/8/invalid BIN-length input. Older View/Edit Saved Payment, vault-initiated checkout, Venmo, Hosted Fields prototype guards and nonce-processing boundaries remain intact. This release does not update the independent PayPal sample or React wrapper evidence. No cross-company comparison, build, upstream tests, browser, wallet, payment or settlement execution was performed.

### 3.147.0 Grounding Excerpts

> `allowedBinVerificationLengths: [6, 8],`
>
> [Hosted Fields constants, line 11](../../../../raw/github/braintree/braintree-web/snapshots/2026-10-19-f3357c4/files/src/hosted-fields/shared/constants.js#L11)

> `writable: false,`
>
> [External constructor, line 471](../../../../raw/github/braintree/braintree-web/snapshots/2026-10-19-f3357c4/files/src/hosted-fields/external/hosted-fields.js#L471)

> `var normalizedLocale = locale && locale.replace(/_/g, "-");`
>
> [v6 adapter, line 607](../../../../raw/github/braintree/braintree-web/snapshots/2026-10-19-f3357c4/files/src/paypal-checkout-v6/paypal-checkout-v6.js#L607)

> `if (cache.promise) {`
>
> [v6 adapter, line 1523](../../../../raw/github/braintree/braintree-web/snapshots/2026-10-19-f3357c4/files/src/paypal-checkout-v6/paypal-checkout-v6.js#L1523)

> `if (await session.hasReturned()) {`
>
> [Corrected v6 JSDoc example, line 1872](../../../../raw/github/braintree/braintree-web/snapshots/2026-10-19-f3357c4/files/src/paypal-checkout-v6/paypal-checkout-v6.js#L1872)

## Related

- [[changelog-github-braintree-web]] — package-qualified release ledger
- [[braintree]] — company and knowledge-status page
- [[braintree-web-sdk]] — product concept and integration boundaries
- [[paypal-braintree-integration]] — PayPal v6/Braintree nonce flow
- [[paypal-fastlane]] — delegated Fastlane product concept

## Raw Sources

- [3.147.0 snapshot](../../../../raw/github/braintree/braintree-web/snapshots/2026-10-19-f3357c4/manifest.json)
- [3.147.0 release identity](../../../../raw/github/braintree/braintree-web/releases/braintree-web/3.147.0/2026-10-19/manifest.json) and [release notes](../../../../raw/github/braintree/braintree-web/releases/braintree-web/3.147.0/2026-10-19/release-notes.md)
- [3.146.0 to 3.147.0 comparison](../../../../tracking/github/repos/braintree/braintree-web/comparisons/braintree-web/3.146.0--3.147.0/comparison.json)

- [3.146.0 snapshot manifest](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-27-893d4e7/manifest.json)
- [3.146.0 release manifest](../../../../raw/github/braintree/braintree-web/releases/braintree-web/3.146.0/2026-09-27/manifest.json) and [release notes](../../../../raw/github/braintree/braintree-web/releases/braintree-web/3.146.0/2026-09-27/release-notes.md)
- [3.145.0 to 3.146.0 comparison](../../../../tracking/github/repos/braintree/braintree-web/comparisons/braintree-web/3.145.0--3.146.0/comparison.md)
- [v6 adapter](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-27-893d4e7/files/src/paypal-checkout-v6/paypal-checkout-v6.js) and [complete edit demo](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-27-893d4e7/files/.storybook/stories/PayPalCheckoutV6/EditSavedPayment.stories.ts)
- [Helper supplement manifest](../../../../raw/github/braintree/braintree-web/supplements/2026-09-27-893d4e7-1540eb0a/manifest.json) and [complete sandbox helper](../../../../raw/github/braintree/braintree-web/supplements/2026-09-27-893d4e7-1540eb0a/files/.storybook/utils/sdk-config.ts)
- [Canonical evidence attachment](../../../../tracking/github/repos/braintree/braintree-web/evidence-attachments/github-9eb53b57a85a75efdb3e/attachment.json)
- [Hosted Fields guard](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-27-893d4e7/files/src/hosted-fields/internal/models/evented-model.js) and [Payment Request frame configuration](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-27-893d4e7/files/src/payment-request/external/payment-request.js)

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

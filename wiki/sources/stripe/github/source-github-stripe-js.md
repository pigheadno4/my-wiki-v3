---
title: "GitHub: stripe/stripe-js"
type: source
date_ingested: 2026-07-30
date_updated: 2026-09-01
original_format: github-repo
raw_files:
  - "github/stripe/stripe-js/snapshots/2026-09-01-9c83132/manifest.json"
  - "github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/manifest.json"
  - "github/stripe/stripe-js/snapshots/2026-08-21-1a6a2c6/manifest.json"
  - "github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/manifest.json"
  - "github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/manifest.json"
tags: [stripe, stripe-js, javascript, typescript, elements, checkout, github-repository]
---

## Overview

`stripe/stripe-js` publishes `@stripe/stripe-js`, the CommonJS and ES module loader plus TypeScript declarations for Stripe.js. This cumulative page preserves the approved `@stripe/stripe-js@8.11.0` baseline, the full major-version transition to `@stripe/stripe-js@9.12.1`, and approved declaration deltas through `9.15.0` at commit `9c83132a5333ffd757be55c75f44524023b5a39e`.

Repository: <https://github.com/stripe/stripe-js>

## Evidence Boundary

- The npm package loads Stripe-hosted Stripe.js; it does not contain a self-hostable Stripe.js runtime.
- Package source proves loader behavior and the public TypeScript contract. It does not prove server API behavior or the implementation behind the remotely loaded `window.Stripe`.
- `@stripe/stripe-js` package versions and Stripe.js release trains are related but distinct. Version-specific answers must identify both when relevant.
- The declarations track a broad API surface, including legacy APIs. A declared method is not by itself a recommendation to start a new integration with that method.
- Current Stripe documentation can be newer than either retained package version. Later package releases are added cumulatively rather than replacing older sections.
- The 9.14.0 upstream release notes retain their empty-section template and do not classify the listed commits. The exact retained comparison is the authority for the release findings below.
- The 9.15.0 release changes declarations only: it does not change the loader or include the remotely hosted Stripe.js implementation. The new types do not independently prove runtime rollout or merchant eligibility.

> [!warning] Contradiction
> The v9 declarations conflict with the April 2026 snapshot in [[source-stripe-checkout-elements-beta-changelog]] on which train is latest and whether `initCheckout()` remains a current entrypoint. Treat that page as historical Clover migration guidance and use package-qualified evidence for version-specific implementation work.

## Grounding Excerpts

> "You cannot include it in a bundle or host it yourself. This package wraps the global `Stripe` function provided by the Stripe.js script as an ES module."
>
> `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/README.md:8-10`

> "Updates for this package only impact tooling around the `loadStripe` helper itself and the TypeScript type definitions provided for Stripe.js."
>
> `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/README.md:13-15`

> "If you call `loadStripe` in a server environment it will resolve to `null`."
>
> `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/README.md:50-55`

> "Ensure that we only attempt to load Stripe.js at most once"
>
> `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/src/shared.ts:101-104`

> "The Stripe object is your entrypoint to the rest of the Stripe.js SDK."
>
> `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/types/stripe-js/stripe.d.ts:1412-1415`

> "export const RELEASE_TRAIN: ReleaseTrain = 'dahlia';"
>
> `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/src/shared.ts:15`

> "Updates for this package only impact tooling around the `loadStripe` helper itself and the TypeScript type definitions provided for Stripe.js. Updates do not affect runtime availability of features of Stripe.js."
>
> `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/README.md:12-16`

> "Form SDK actions omit the client-only update methods that are handled internally by the CheckoutForm UI."
>
> `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/types/stripe-js/checkout.d.ts:774-786`

> "Use `stripe.handleNextAction` to handle the required next action when a SharedPaymentToken has a `requires_action` status."
>
> `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/types/stripe-js/stripe.d.ts:678-688`

> "Control whether the promotion code collection UI is displayed in the CheckoutForm."
>
> `raw/github/stripe/stripe-js/snapshots/2026-08-21-1a6a2c6/files/types/stripe-js/checkout.d.ts:472-484`

> "Only applies when `allow_promotion_codes`is enabled on the Checkout Session."
>
> `raw/github/stripe/stripe-js/snapshots/2026-08-21-1a6a2c6/files/types/stripe-js/checkout.d.ts:477-484`

> "The subset of `StripePaymentElementOptions` that can be updated after the `PaymentElement` has been created."
>
> `raw/github/stripe/stripe-js/snapshots/2026-08-21-1a6a2c6/files/types/stripe-js/elements/payment.d.ts:406-422`

> "Control wallet behavior options in the Payment Element."
>
> `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/elements/payment.d.ts:339-342,400-403`

> "Additional options to configure the Custom Payment Method in the Express Checkout Element."
>
> `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/elements-group.d.ts:1470-1495`

> "[customPaymentMethodId: string]: {available: boolean} | undefined;"
>
> `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/elements/express-checkout.d.ts:600-612`

> "@deprecated Dynamic shipping updates are deprecated in Embedded Checkout."
>
> `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/embedded-checkout.d.ts:164-169`

> `"version": "9.15.0"`
>
> `raw/github/stripe/stripe-js/snapshots/2026-09-01-9c83132/files/package.json:3`

> `metadata?: MetadataParam;`
>
> `raw/github/stripe/stripe-js/snapshots/2026-09-01-9c83132/files/types/api/confirmation-tokens.d.ts:116`

> `buttonBoxShadow?: string;`
>
> `raw/github/stripe/stripe-js/snapshots/2026-09-01-9c83132/files/types/stripe-js/elements-group.d.ts:1250`

## Package Status

| Package | Latest ingested release | Stripe.js train | Evidence status |
| --- | --- | --- | --- |
| `@stripe/stripe-js` | `9.15.0` | `dahlia` | Approved 9.15 declaration delta; prior v9 and v8 retained |

This table reports wiki ingest progress, not the latest version published upstream.

## Responsibility and Package Shape

The package manifest exposes:

- CommonJS through `lib/index.js`;
- ES modules through `lib/index.mjs`;
- declarations through `lib/index.d.ts`;
- the side-effect-free loader through the `pure` entrypoint; and
- copied declaration and runtime output through generated `dist` targets referenced by the public entrypoints.

The retained package requires Node.js 12.16 or newer and documents TypeScript 3.1.1 or newer for consumers. Its examples use `loadStripe()`, create an Elements group, mount a Card Element, and call `stripe.createPaymentMethod()` on submit.

## Version 8

### `@stripe/stripe-js@8.11.0`

#### Runtime Loading

The standard entrypoint schedules Stripe.js loading immediately after import. It searches existing scripts under `https://js.stripe.com`, reuses a recognized v3 or named-train script, or injects `https://js.stripe.com/clover/stripe.js`. A single cached promise coordinates concurrent calls. A failed load clears that promise so a later call can retry.

Outside a browser, `loadScript()` resolves to `null`, making import safe in isomorphic code. After loading, `initStripe()` requires a string publishable key, creates the Stripe instance, and registers wrapper name, package version, and load start time when the runtime exposes `_registerWrapper`.

With a test publishable key, the wrapper compares the loaded runtime version with the expected `clover` train and warns on a mismatch. That warning is diagnostic; the wrapper still initializes the returned Stripe object.

#### Standard and Pure Entrypoints

Importing `@stripe/stripe-js` has a script-loading side effect. `@stripe/stripe-js/pure` defers loading until the first `loadStripe()` call.

The pure entrypoint additionally exposes:

```ts
loadStripe.setLoadParameters({advancedFraudSignals: false});
```

The setting must be supplied before `loadStripe()` runs. Repeating the same parameters is tolerated, but changing parameters after the first call throws. If a Stripe.js script already exists, its parameters win and the wrapper warns.

#### Public Stripe.js Surface

The v8 declarations make the `Stripe` object the primary client entrypoint. Major API families include:

- PaymentIntent confirmation and retrieval, including card, wallets, bank methods, BNPL, vouchers, and redirect methods;
- SetupIntent confirmation and retrieval for reusable payment credentials;
- PaymentMethod and ConfirmationToken creation;
- Elements creation through either a client secret or client-side `mode`, amount, and currency;
- Payment Request, token, Source, Orders, Identity, Financial Connections, Radar Session, and Issuing nonce helpers;
- Checkout Elements through `initCheckout()` and its `initCheckoutElementsSdk()` alias; and
- Embedded Checkout through `initEmbeddedCheckout()`.

Constructor options include a connected-account ID, API version override, locale, beta flags, and developer-tooling settings.

#### Elements

The retained Elements declarations cover Card, Payment, Express Checkout, Address, Shipping Address, Link Authentication, AU Bank Account, IBAN, Payment Request Button, Payment Method Messaging, Currency Selector, Tax ID, and Issuing Elements.

Every normal Element inherits lifecycle operations such as `mount`, `blur`, `clear`, `destroy`, `focus`, and `unmount`. `StripeElements` can update group options, fetch updates, submit validation, create supported element types, and retrieve mounted elements.

The Payment Element supports tabs, accordion, or automatic layout; configurable fields, terms, wallets, saved methods, and ordering; and change events carrying completion, value, collapse, and payment-method information.

The Express Checkout Element declares Apple Pay, Google Pay, PayPal, and Link presentation controls; ready, click, confirm, cancel, shipping-address, and shipping-rate events; and resolve or reject callbacks for merchant updates. These declarations describe wallet presentation and confirmation callbacks, not independent recurring-payment capability.

#### Checkout

The v8 `StripeCheckout` contract exposes element factories and `loadActions()`. The action surface includes:

- confirmation;
- promotion-code application and removal;
- shipping and billing address updates;
- email and phone updates;
- line-item quantity changes;
- tax-ID and shipping-option updates; and
- `runServerUpdate()` for a merchant server callback.

The session model includes line items, recurring details, shipping, discounts, taxes, totals, saved payment methods, and status. `StripeEmbeddedCheckout` remains a separate mountable instance.

#### Payment and Setup Method Coverage

The declaration capsule includes typed confirmation data for cards, PayPal, Amazon Pay, Apple Pay-related flows, Google Pay-related PaymentMethod data, Cash App Pay, Klarna, Affirm, Afterpay/Clearpay, bank debits, bank redirects, bank transfers, vouchers, and regional methods. Exact eligibility, country availability, recurring support, and runtime behavior require the corresponding Stripe product documentation and account configuration.

## Version 9

### `@stripe/stripe-js@9.12.1`

#### Release Train and Runtime Boundary

Version 9 changes the package's pinned Stripe.js train from `clover` to `dahlia`. The loader now injects `https://js.stripe.com/dahlia/stripe.js`, and test-key initialization warns when an already loaded runtime does not match that train.

The package boundary does not change: Stripe.js remains a Stripe-hosted runtime, while this repository supplies loading behavior and TypeScript declarations. The package README explicitly warns that `loadStripe()` loads the latest Stripe.js runtime and that package updates do not determine runtime feature availability. Therefore, the v9 declarations prove the package's typed contract, not rollout or account eligibility for every declared feature.

#### Checkout API Reshape

The v9 declarations replace the generic v8 `StripeCheckout` naming with `StripeCheckoutElementsSdk` and introduce a beta `StripeCheckoutFormSdk`:

- `initCheckout()` is removed; `initCheckoutElementsSdk()` is the Elements entrypoint.
- `initCheckoutFormSdk()` adds a beta form integration with `createForm()` and `getForm()`.
- `initEmbeddedCheckout()` is renamed to `createEmbeddedCheckoutPage()`.
- The former Payment Form Element contract is renamed to `CheckoutForm`, including its event discriminator.
- Form SDK actions deliberately omit imperative email, phone, address, and tax-ID updates because the form UI owns those fields.

Checkout session state expands with optional items, removable line items, price IDs, decimal unit amounts, unit labels, currency options, surcharge state and totals, and richer recurring and tax details. The action contract adds `validateElements()`, `addOptionalLineItem()`, and `removeOptionalLineItem()`.

These are cumulative v8-to-v9 contract findings. They are not all changes introduced by the 9.12.1 patch itself.

#### Elements Changes

`StripeElements.update()` now returns `Promise<void>`, allowing callers to await propagation across rendered Elements. The group adds Contact Details and beta Terms Element creation and lookup, while retaining the beta Currency Selector Element.

The Payment Element adds:

- an `availablepaymentmethodschange` event;
- payment-method-specific billing-detail field configuration;
- a larger typed payment-method union;
- Klarna terms-display configuration; and
- a stricter radio-layout option that no longer accepts a boolean.

Address Element value retrieval can request Latin or localized formatting. Tax ID Element options add verification behavior, and change events can report `pending`, `verified`, `unverified`, or `unavailable`.

#### Client Surface and Migration

The v9 `Stripe` interface removes client-side `createSource()` and `retrieveSource()` plus `SourceResult`; token creation remains declared. Existing Source-based integrations must not assume that upgrading to v9 preserves those typed client helpers.

The interface also adds a `handleNextAction({hashedValue})` overload for Shared Payment Tokens requiring action. This declaration establishes the client handoff shape only; the complete agent/seller flow remains owned by the Shared Payment Tokens product documentation.

For a v8-to-v9 migration:

1. replace `initCheckout()` with `initCheckoutElementsSdk()`;
2. replace `initEmbeddedCheckout()` with `createEmbeddedCheckoutPage()`;
3. migrate Payment Form Element names to Checkout Form where using that beta surface;
4. remove uses of client-side Source creation or retrieval from the typed integration;
5. await `elements.update()` where ordering matters; and
6. re-run TypeScript checks for changed Checkout, Payment Element, Address, Tax ID, and wallet option contracts.

### `@stripe/stripe-js@9.13.0`

Version 9.13.0 is a contained TypeScript contract update on the retained `dahlia` train. It does not change the package's loader boundary or establish runtime rollout by itself.

Checkout Form options add `features.promotionCodeCollection?: 'auto' | 'never'`. The default is `auto`, and the setting only controls whether the promotion-code collection UI is displayed when the Checkout Session already has `allow_promotion_codes` enabled. It does not enable promotion codes on the session.

Payment Element `update()` now accepts `Partial<StripePaymentElementUpdateOptions>` instead of all partial creation options. The updateable subset is `defaultValues`, `business`, `paymentMethodOrder`, `fields`, `readOnly`, `terms`, `layout`, and `applePay`. In particular, `wallets` remains a creation option but is no longer accepted by the typed post-creation update call. Consumers upgrading from 9.12.1 should run TypeScript checks around every `paymentElement.update()` call and move wallet visibility configuration to element creation.

### `@stripe/stripe-js@9.14.0`

Version 9.14.0 remains on the retained `dahlia` train and changes public declarations rather than the loader implementation. Its upstream release notes list commits under an unfinished template, so the exact 9.13.0-to-9.14.0 comparison provides the reliable change classification.

#### Wallet Contact Collection

Payment Element adds `walletOptions` with boolean `emailRequired` and `phoneNumberRequired` fields. The option is available both to standard Elements and Checkout Elements Payment Element creation. Unlike the separate `wallets` visibility option, `walletOptions` is included in `StripePaymentElementUpdateOptions`, so contact requirements can be changed after element creation in the typed contract.

#### Embedded Custom Payment Methods

`CustomPaymentMethod.options` becomes optional and supports either `static` or `embedded` form rendering. The new `payment` property is an alias for Payment Element configuration. Embedded rendering receives an `HTMLDivElement` through required `handleRender()` and can define optional `handleDestroy()` cleanup.

A beta `expressCheckout` property adds an embedded Custom Payment Method button with the same render-and-cleanup lifecycle. Express Checkout's `availablepaymentmethodschange` event now accepts dynamic custom payment-method IDs in addition to built-in wallet keys.

> [!warning] Versioned availability
> Existing product documentation in [[stripe-custom-payment-methods]] records Express Checkout Element as unsupported. The v9.14 declarations explicitly mark this new surface as requiring beta access. Treat it as typed preview evidence, not proof of general runtime availability or merchant eligibility.

#### Embedded Checkout Shipping Deprecation

`StripeEmbeddedCheckoutOptions.onShippingDetailsChange` remains declared but is now marked deprecated because dynamic shipping updates are deprecated in Embedded Checkout. Existing integrations can retain the callback for their pinned version, but new work must verify Stripe's current replacement path rather than following older dynamic-shipping guidance unchanged.

### `@stripe/stripe-js@9.15.0`

Version 9.15.0 is a contained additive TypeScript declaration update on the retained `dahlia` train. The package loader, entrypoints, Node engine, and dependency ranges do not change.

#### ConfirmationToken Metadata

`ConfirmationTokenCreateParams` adds `metadata?: MetadataParam`, allowing typed web integrations to include metadata under `params` when calling `stripe.createConfirmationToken({elements, params})`. The declaration documents a maximum of 50 keys and uses the existing Stripe metadata parameter type. The exact type tests accept a string-valued `order_id` and reject a boolean value.

This declaration adds compile-time support; it does not independently establish server persistence behavior or the availability of the remotely hosted Stripe.js implementation.

#### Elements Button Shadow Variable

`Appearance.variables` adds `buttonBoxShadow?: string`. This is an additive styling type for Stripe Elements buttons. No other Appearance variable, Element lifecycle, or payment behavior changes in the retained comparison.

## Compatibility and Operational Notes

- Stripe.js must be loaded from `js.stripe.com` for the documented PCI boundary.
- The default import loads Stripe.js as a side effect; use `/pure` when deferred loading is required.
- Server rendering must handle `loadStripe()` resolving to `null`.
- Content Security Policy must allow the Stripe.js origins required by Stripe.
- Stripe recommends loading Stripe.js throughout the site to improve advanced fraud signals; disabling those signals is an explicit pure-entrypoint choice.
- Minor and patch package releases can include small backwards-incompatible declaration corrections without changing the remote Stripe.js runtime.
- In `9.13.0`, Checkout Form promotion-code visibility depends on the server-created Session setting, and Payment Element wallet visibility must be configured at creation rather than through the typed `update()` call.
- In `9.14.0`, wallet contact requirements can be created or updated through `walletOptions`; this does not make the separate `wallets` visibility option updateable.
- In `9.15.0`, ConfirmationToken metadata and `buttonBoxShadow` are additive typed options; existing integrations have no documented migration requirement.
- Embedded Custom Payment Method rendering requires trusted content, explicit cleanup, and beta-access verification. The declaration does not transfer third-party payment processing to Stripe.
- Embedded Checkout dynamic shipping updates are deprecated; version-specific maintenance guidance must not be presented as the recommended new-integration path.

## Related

- Company: [[stripe]]
- Concepts: [[stripe-elements]], [[stripe-checkout]], [[stripe-express-checkout-element]], [[stripe-payment-intents]], [[stripe-radar]]
- History: [[changelog-github-stripe-js]]

## Raw Sources

- `raw/github/stripe/stripe-js/snapshots/2026-09-01-9c83132/manifest.json` — exact-SHA v9.15.0 source capsule
- `raw/github/stripe/stripe-js/releases/stripe-js/9.15.0/2026-09-01/manifest.json` — package-qualified v9.15.0 release record
- `raw/github/stripe/stripe-js/releases/stripe-js/9.15.0/2026-09-01/release-notes.md` — upstream v9.15.0 release notes
- `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.14.0--9.15.0/comparison.md` — retained v9.14.0-to-v9.15.0 comparison
- `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.14.0--9.15.0/diff.patch` — exact retained delta
- `raw/github/stripe/stripe-js/snapshots/2026-09-01-9c83132/files/types/api/confirmation-tokens.d.ts` — ConfirmationToken metadata typing
- `raw/github/stripe/stripe-js/snapshots/2026-09-01-9c83132/files/types/stripe-js/elements-group.d.ts` — Elements `buttonBoxShadow` appearance variable
- `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/manifest.json` — exact-SHA v9.14.0 source capsule
- `raw/github/stripe/stripe-js/releases/stripe-js/9.14.0/2026-08-21/manifest.json` — package-qualified v9.14.0 release record
- `raw/github/stripe/stripe-js/releases/stripe-js/9.14.0/2026-08-21/release-notes.md` — upstream release notes with unfinished template
- `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.13.0--9.14.0/comparison.md` — retained v9.13.0-to-v9.14.0 comparison
- `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.13.0--9.14.0/diff.patch` — exact retained delta
- `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/elements/payment.d.ts` — wallet contact collection and update typing
- `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/elements-group.d.ts` — embedded Payment and Express Checkout Custom Payment Methods
- `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/elements/express-checkout.d.ts` — dynamic custom-method availability keys
- `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/embedded-checkout.d.ts` — dynamic shipping callback deprecation
- `raw/github/stripe/stripe-js/snapshots/2026-08-21-1a6a2c6/manifest.json` — exact-SHA v9.13.0 source capsule
- `raw/github/stripe/stripe-js/releases/stripe-js/9.13.0/2026-08-21/manifest.json` — package-qualified v9.13.0 release record
- `raw/github/stripe/stripe-js/releases/stripe-js/9.13.0/2026-08-21/release-notes.md` — exact v9.13.0 release notes
- `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.12.1--9.13.0/comparison.md` — retained v9.12.1-to-v9.13.0 comparison
- `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.12.1--9.13.0/diff.patch` — exact retained delta
- `raw/github/stripe/stripe-js/snapshots/2026-08-21-1a6a2c6/files/types/stripe-js/checkout.d.ts` — Checkout Form promotion-code display control
- `raw/github/stripe/stripe-js/snapshots/2026-08-21-1a6a2c6/files/types/stripe-js/elements/payment.d.ts` — Payment Element updateable-option subset
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/manifest.json` — exact-SHA v9.12.1 source capsule
- `raw/github/stripe/stripe-js/releases/stripe-js/9.12.1/2026-07-30/manifest.json` — package-qualified v9 release record
- `raw/github/stripe/stripe-js/releases/stripe-js/9.12.1/2026-07-30/release-notes.md` — exact 9.12.1 patch note
- `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/8.11.0--9.12.1/comparison.md` — retained v8-to-v9 path comparison
- `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/8.11.0--9.12.1/diff.patch` — exact retained transition patch
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/README.md` — v9 train and runtime boundary
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/src/shared.ts` — Dahlia loader implementation
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/types/stripe-js/stripe.d.ts` — v9 Stripe client contract
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/types/stripe-js/elements-group.d.ts` — v9 Elements group contract
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/types/stripe-js/checkout.d.ts` — v9 Checkout Elements and Form SDK contracts
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/manifest.json` — exact-SHA v8.11.0 source capsule
- `raw/github/stripe/stripe-js/releases/stripe-js/8.11.0/2026-07-30/manifest.json` — package-qualified release record
- `raw/github/stripe/stripe-js/releases/stripe-js/8.11.0/2026-07-30/release-notes.md` — upstream release notes
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/README.md` — package boundary, usage, and versioning
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/src/shared.ts` — script discovery, loading, retry, and initialization
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/src/index.ts` — side-effecting entrypoint
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/src/pure.ts` — deferred loader and load parameters
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/types/stripe-js/stripe.d.ts` — Stripe client contract
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/types/stripe-js/elements-group.d.ts` — Elements group contract
- `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/types/stripe-js/checkout.d.ts` — Checkout Elements contract

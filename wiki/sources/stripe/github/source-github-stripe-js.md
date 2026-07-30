---
title: "GitHub: stripe/stripe-js"
type: source
date_ingested: 2026-07-30
date_updated: 2026-07-30
original_format: github-repo
raw_files:
  - "github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/manifest.json"
  - "github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/manifest.json"
tags: [stripe, stripe-js, javascript, typescript, elements, checkout, github-repository]
---

## Overview

`stripe/stripe-js` publishes `@stripe/stripe-js`, the CommonJS and ES module loader plus TypeScript declarations for Stripe.js. This cumulative page preserves the approved `@stripe/stripe-js@8.11.0` baseline and adds the full major-version transition to `@stripe/stripe-js@9.12.1` at commit `43d35b1b0e324475ea9f9cb867ad2c4e7dabe3f8`.

Repository: <https://github.com/stripe/stripe-js>

## Evidence Boundary

- The npm package loads Stripe-hosted Stripe.js; it does not contain a self-hostable Stripe.js runtime.
- Package source proves loader behavior and the public TypeScript contract. It does not prove server API behavior or the implementation behind the remotely loaded `window.Stripe`.
- `@stripe/stripe-js` package versions and Stripe.js release trains are related but distinct. Version-specific answers must identify both when relevant.
- The declarations track a broad API surface, including legacy APIs. A declared method is not by itself a recommendation to start a new integration with that method.
- Current Stripe documentation can be newer than either retained package version. Later package releases are added cumulatively rather than replacing older sections.

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

## Package Status

| Package | Latest ingested release | Stripe.js train | Evidence status |
| --- | --- | --- | --- |
| `@stripe/stripe-js` | `9.12.1` | `dahlia` | Approved full major transition; v8 retained |

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

## Compatibility and Operational Notes

- Stripe.js must be loaded from `js.stripe.com` for the documented PCI boundary.
- The default import loads Stripe.js as a side effect; use `/pure` when deferred loading is required.
- Server rendering must handle `loadStripe()` resolving to `null`.
- Content Security Policy must allow the Stripe.js origins required by Stripe.
- Stripe recommends loading Stripe.js throughout the site to improve advanced fraud signals; disabling those signals is an explicit pure-entrypoint choice.
- Minor and patch package releases can include small backwards-incompatible declaration corrections without changing the remote Stripe.js runtime.

## Related

- Company: [[stripe]]
- Concepts: [[stripe-elements]], [[stripe-checkout]], [[stripe-express-checkout-element]], [[stripe-payment-intents]], [[stripe-radar]]
- History: [[changelog-github-stripe-js]]

## Raw Sources

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

---
title: "GitHub: stripe/stripe-js"
type: source
date_ingested: 2026-07-30
original_format: github-repo
raw_files:
  - "github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/manifest.json"
tags: [stripe, stripe-js, javascript, typescript, elements, checkout, github-repository]
---

## Overview

`stripe/stripe-js` publishes `@stripe/stripe-js`, the CommonJS and ES module loader plus TypeScript declarations for Stripe.js. This page starts with the approved full baseline for `@stripe/stripe-js@8.11.0` at commit `d7bbb144b783287300ff7e63aec7c8133b52460e`.

Repository: <https://github.com/stripe/stripe-js>

## Evidence Boundary

- The npm package loads Stripe-hosted Stripe.js; it does not contain a self-hostable Stripe.js runtime.
- Package source proves loader behavior and the public TypeScript contract. It does not prove server API behavior or the implementation behind the remotely loaded `window.Stripe`.
- `@stripe/stripe-js` package versions and Stripe.js release trains are related but distinct. Version-specific answers must identify both when relevant.
- The declarations track a broad API surface, including legacy APIs. A declared method is not by itself a recommendation to start a new integration with that method.
- Current Stripe documentation can be newer than this historical v8.11.0 baseline. Later package releases are added cumulatively rather than replacing this section.

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

## Package Status

| Package | Latest ingested release | Stripe.js train | Evidence status |
| --- | --- | --- | --- |
| `@stripe/stripe-js` | `8.11.0` | `clover` | Approved full baseline |

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

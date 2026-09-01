---
title: "GitHub changelog: stripe/stripe-js"
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
tags: [stripe, stripe-js, javascript, typescript, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-js`. Cumulative implementation knowledge belongs in [[source-github-stripe-js]] and the linked immutable snapshots.

## `@stripe/stripe-js@9.15.0` — Change Set `9c83132` (2026-08-31)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@stripe/stripe-js` | `9.14.0` | `9.15.0` | 2026-08-31 | `9c83132a5333ffd757be55c75f44524023b5a39e` | Delta |

**Important change:** `ConfirmationTokenCreateParams` adds `metadata?: MetadataParam`, and Elements `Appearance.variables` adds `buttonBoxShadow?: string`.

**Developer or merchant impact:** TypeScript integrations can now pass typed metadata to `stripe.createConfirmationToken()` and type a button shadow in Elements appearance configuration. The package loader and remotely hosted runtime implementation do not change.

**Migration action:** None documented. Existing integrations can adopt either option when needed and should verify Stripe-hosted runtime and server behavior separately from declaration presence.

**Updated source sections:** overview; evidence boundary; grounding excerpts; package status; v9.15.0 delta; compatibility notes; Stripe company; Stripe Elements and Payment Intents concepts; provider index.

**Evidence boundary:** The release is an additive declaration update. Two modified type-test fixtures confirm intended values but remain intentionally excluded from the raw source capsule; their exact diff is retained in the comparison. No dependency, loader, removal, or runtime implementation change is present.

**Evidence:**

- Release manifest: `raw/github/stripe/stripe-js/releases/stripe-js/9.15.0/2026-09-01/manifest.json`
- Release notes: `raw/github/stripe/stripe-js/releases/stripe-js/9.15.0/2026-09-01/release-notes.md`
- Snapshot manifest: `raw/github/stripe/stripe-js/snapshots/2026-09-01-9c83132/manifest.json`
- Comparison manifest: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.14.0--9.15.0/comparison.json`
- Comparison: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.14.0--9.15.0/comparison.md`
- Exact patch: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.14.0--9.15.0/diff.patch`
- ConfirmationToken types: `raw/github/stripe/stripe-js/snapshots/2026-09-01-9c83132/files/types/api/confirmation-tokens.d.ts`
- Elements appearance types: `raw/github/stripe/stripe-js/snapshots/2026-09-01-9c83132/files/types/stripe-js/elements-group.d.ts`

## `@stripe/stripe-js@9.14.0` — Change Set `8daa6fa` (2026-08-20)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@stripe/stripe-js` | `9.13.0` | `9.14.0` | 2026-08-20 | `8daa6fad5d318aa9e18aa0e1833e4249c08e4682` | Delta |

**Important change:** Payment Element adds updateable wallet email and phone requirements. Custom Payment Methods gain embedded Payment Element rendering and a beta embedded Express Checkout button surface with dynamic availability keys. Embedded Checkout dynamic shipping updates are deprecated.

**Developer or merchant impact:** Payment Element and Checkout Elements can require wallet-provided email or phone values through `walletOptions`. Custom Payment Method integrations can own render and cleanup callbacks inside Payment Element, and beta-enabled merchants gain corresponding Express Checkout typing. Existing Embedded Checkout integrations using `onShippingDetailsChange` now receive a deprecation signal.

**Migration action:** Distinguish updateable `walletOptions` from creation-only wallet visibility; implement deterministic cleanup for embedded Custom Payment Method UI; verify beta access before using Custom Payment Methods in Express Checkout; and avoid starting new Embedded Checkout dynamic-shipping work without confirming Stripe's current replacement.

**Updated source sections:** evidence boundary; grounding excerpts; package status; v9.14.0 delta; compatibility notes; Stripe company; Elements, Express Checkout, Custom Payment Methods, and Checkout concepts; provider index.

**Evidence boundary:** The upstream release notes retain empty template headings and list commits without classification. The exact comparison establishes the public type changes. The `js-yaml` development lockfile bump is excluded from the retained capsule and has no demonstrated merchant runtime impact. Beta declarations do not prove rollout or account eligibility.

**Evidence:**

- Release manifest: `raw/github/stripe/stripe-js/releases/stripe-js/9.14.0/2026-08-21/manifest.json`
- Release notes: `raw/github/stripe/stripe-js/releases/stripe-js/9.14.0/2026-08-21/release-notes.md`
- Snapshot manifest: `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/manifest.json`
- Comparison manifest: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.13.0--9.14.0/comparison.json`
- Comparison: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.13.0--9.14.0/comparison.md`
- Exact patch: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.13.0--9.14.0/diff.patch`
- Checkout Elements types: `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/checkout.d.ts`
- Elements group and Custom Payment Method types: `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/elements-group.d.ts`
- Express Checkout types: `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/elements/express-checkout.d.ts`
- Payment Element types: `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/elements/payment.d.ts`
- Embedded Checkout types: `raw/github/stripe/stripe-js/snapshots/2026-08-21-8daa6fa/files/types/stripe-js/embedded-checkout.d.ts`

## `@stripe/stripe-js@9.13.0` — Change Set `1a6a2c6` (2026-08-04)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@stripe/stripe-js` | `9.12.1` | `9.13.0` | 2026-08-04 | `1a6a2c6dc4fd25ccd0c52f42136ee98776f0c2f5` | Delta |

**Important change:** Checkout Form adds `features.promotionCodeCollection` with `auto` and `never` values. Payment Element narrows its typed `update()` input to an explicit subset of creation options.

**Developer or merchant impact:** Promotion-code UI visibility can be suppressed client-side, but only for a Checkout Session that already enables `allow_promotion_codes`; this option does not activate promotion codes. Existing TypeScript code that updates Payment Element `wallets` after creation no longer type-checks, while `defaultValues`, `business`, `paymentMethodOrder`, `fields`, `readOnly`, `terms`, `layout`, and `applePay` remain updateable.

**Migration action:** Run TypeScript checks on every `paymentElement.update()` call, move wallet visibility configuration to Payment Element creation, and keep `allow_promotion_codes` as the server-side prerequisite before using Checkout Form promotion-code display control.

**Updated source sections:** package status; v9.13.0 delta; compatibility notes; Stripe company; Stripe Elements and Stripe Checkout concepts; provider index.

**Evidence boundary:** This is a package declaration delta on the existing `dahlia` train. It proves the public TypeScript contract at the retained SHA, not Stripe-hosted runtime rollout or account eligibility. Tests confirm the intended type boundary but were excluded from the retained source capsule; the exact repository comparison preserves those changes.

**Evidence:**

- Release manifest: `raw/github/stripe/stripe-js/releases/stripe-js/9.13.0/2026-08-21/manifest.json`
- Release notes: `raw/github/stripe/stripe-js/releases/stripe-js/9.13.0/2026-08-21/release-notes.md`
- Snapshot manifest: `raw/github/stripe/stripe-js/snapshots/2026-08-21-1a6a2c6/manifest.json`
- Comparison manifest: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.12.1--9.13.0/comparison.json`
- Comparison: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.12.1--9.13.0/comparison.md`
- Exact patch: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/9.12.1--9.13.0/diff.patch`
- Checkout Form types: `raw/github/stripe/stripe-js/snapshots/2026-08-21-1a6a2c6/files/types/stripe-js/checkout.d.ts`
- Payment Element types: `raw/github/stripe/stripe-js/snapshots/2026-08-21-1a6a2c6/files/types/stripe-js/elements/payment.d.ts`

## `@stripe/stripe-js@9.12.1` — Change Set `43d35b1` (2026-07-27)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@stripe/stripe-js` | `8.11.0` | `9.12.1` | 2026-07-27 | `43d35b1b0e324475ea9f9cb867ad2c4e7dabe3f8` | Full |

**Important change:** The exact 9.12.1 release note only bumps `brace-expansion` in the Parcel example. The full retained v8-to-v9 comparison is broader because this is a major-version transition: v9 targets the `dahlia` Stripe.js train, reshapes Checkout into explicit Elements and beta Form SDK contracts, renames Embedded Checkout initialization, expands Elements and Checkout types, removes client-side Source helpers, and adds Shared Payment Token next-action typing.

**Developer or merchant impact:** Existing v8 integrations can encounter compile-time breaks around `initCheckout`, `initEmbeddedCheckout`, Payment Form Element names, `elements.update()`, Source helpers, and several option types. Checkout gains optional-item and surcharge state, validation actions, Contact Details and Terms Elements, and a beta form-owned integration surface.

**Migration action:** Replace `initCheckout()` with `initCheckoutElementsSdk()`, replace `initEmbeddedCheckout()` with `createEmbeddedCheckoutPage()`, migrate Payment Form names to Checkout Form where applicable, remove typed client-side Source calls, await `elements.update()` when sequencing matters, and re-run TypeScript checks across Checkout and Element configuration. Verify account and runtime availability separately from declaration presence.

**Updated source sections:** package status; v9 release train and runtime boundary; Checkout API reshape; Elements changes; client surface and migration; Stripe company; Stripe Elements and Stripe Checkout concepts.

**Evidence boundary:** The dependency bump is the only change attributable specifically to the 9.12.1 patch note. All other findings describe the cumulative exact-SHA difference between the retained 8.11.0 and 9.12.1 capsules. The package continues to load a Stripe-hosted runtime, so declarations do not prove feature rollout or merchant eligibility.

**Evidence:**

- Release manifest: `raw/github/stripe/stripe-js/releases/stripe-js/9.12.1/2026-07-30/manifest.json`
- Release notes: `raw/github/stripe/stripe-js/releases/stripe-js/9.12.1/2026-07-30/release-notes.md`
- Snapshot manifest: `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/manifest.json`
- Comparison manifest: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/8.11.0--9.12.1/comparison.json`
- Comparison: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/8.11.0--9.12.1/comparison.md`
- Exact patch: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/8.11.0--9.12.1/diff.patch`
- Package boundary: `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/README.md`
- Checkout types: `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/types/stripe-js/checkout.d.ts`
- Elements types: `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/types/stripe-js/elements-group.d.ts`
- Stripe client types: `raw/github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/files/types/stripe-js/stripe.d.ts`

## `@stripe/stripe-js@8.11.0` — Change Set `d7bbb14` (2026-03-18)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@stripe/stripe-js` | Initial retained baseline | `8.11.0` | 2026-03-18 | `d7bbb144b783287300ff7e63aec7c8133b52460e` | Full |

**Important change:** This first retained release establishes the v8 `clover` baseline for the Stripe.js loader and TypeScript declarations. The `8.11.0` release note specifically adds `paymentMethods` to Payment Form Element and renames its `wallets` option to `expressCheckout`.

**Developer or merchant impact:** Consumers gain the package-qualified v8 loader, Elements, Checkout, PaymentIntent, SetupIntent, wallet, and payment-method type baseline. Payment Form Element integrations upgrading to 8.11.0 should use the new option names and re-run TypeScript checks.

**Migration action:** Replace the prior Payment Form Element `wallets` option with `expressCheckout` where applicable, review the added `paymentMethods` option, and verify the integration against the `clover` Stripe.js train. No runtime migration is inferred beyond the release note and retained declarations.

**Updated source sections:** repository responsibility; v8 loading behavior; standard and pure entrypoints; Stripe.js client surface; Elements; Checkout; Stripe Elements and Stripe Checkout concepts.

**Evidence boundary:** This is the initial retained Stripe JS baseline, so no prior exact-SHA comparison exists. The release-specific change comes from upstream release notes; broader findings describe the complete retained 8.11.0 source capsule and must not be attributed solely to this patch.

**Evidence:**

- Release manifest: `raw/github/stripe/stripe-js/releases/stripe-js/8.11.0/2026-07-30/manifest.json`
- Release notes: `raw/github/stripe/stripe-js/releases/stripe-js/8.11.0/2026-07-30/release-notes.md`
- Snapshot manifest: `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/manifest.json`
- Package manifest: `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/package.json`
- Loader implementation: `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/src/shared.ts`
- Payment Form Element types: `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/types/stripe-js/elements/payment-form.d.ts`
- Checkout types: `raw/github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/files/types/stripe-js/checkout.d.ts`

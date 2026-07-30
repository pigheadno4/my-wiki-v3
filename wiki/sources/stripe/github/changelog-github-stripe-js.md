---
title: "GitHub changelog: stripe/stripe-js"
type: source
date_ingested: 2026-07-30
date_updated: 2026-07-30
original_format: github-repo
raw_files:
  - "github/stripe/stripe-js/snapshots/2026-07-30-43d35b1/manifest.json"
  - "github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/manifest.json"
tags: [stripe, stripe-js, javascript, typescript, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-js`. Cumulative implementation knowledge belongs in [[source-github-stripe-js]] and the linked immutable snapshots.

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

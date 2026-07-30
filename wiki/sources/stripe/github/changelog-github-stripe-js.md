---
title: "GitHub changelog: stripe/stripe-js"
type: source
date_ingested: 2026-07-30
original_format: github-repo
raw_files:
  - "github/stripe/stripe-js/snapshots/2026-07-30-d7bbb14/manifest.json"
tags: [stripe, stripe-js, javascript, typescript, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-js`. Cumulative implementation knowledge belongs in [[source-github-stripe-js]] and the linked immutable snapshots.

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

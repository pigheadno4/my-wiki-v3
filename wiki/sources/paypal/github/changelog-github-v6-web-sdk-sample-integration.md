---
title: "GitHub changelog: paypal-examples/v6-web-sdk-sample-integration"
type: source
date_ingested: 2026-08-04
date_updated: 2026-09-19
original_format: github-repo
raw_files:
  - "github/paypal/v6-web-sdk-sample-integration/snapshots/2026-09-19-bb23e7c/manifest.json"
  - "github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/manifest.json"
  - "github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/manifest.json"
  - "github-paypal-v6-samples.md"
tags: [paypal, web-sdk-v6, samples, changelog, github-repository]
---

## Overview

Commit-qualified history for `paypal-examples/v6-web-sdk-sample-integration`. Durable integration guidance belongs in [[source-github-v6-web-sdk-sample-integration]].

## `default-branch@bb23e7c` - ACH Wallet and Card Name (2026-09-17)

| Ref | Prior SHA | Current SHA | Ingest mode |
| --- | --- | --- | --- |
| `main` | `de90a89c90b06421ca34241e7162236e2b04fd79` | `bb23e7c63305a872326f43c3d52c5edd53e20b43` | Full additive; approved focused-reading exception |

Collected and ingested September 19, 2026. Three added files and 62 modified files; 197 unchanged retained files verified by hash. Full reads covered all changed files, prior versions, and affected dependencies, not all 532 default assigned paths. Prior baselines remain in the cumulative source.

### New and changed behavior

- Adds HTML ACH Wallet using a browser-safe client token, `bank-ach-payments`, `ach` eligibility, `standardEntryClassCode: "WEB"`, and `connect()` with a lazy create-order callback.
- Adds `POST /paypal-api/checkout/orders/:orderId/capture-ach-wallet`: get order, construct/log a consent record, then capture. Environment guidance now includes ACH Wallet for domain configuration.
- Adds optional name fields to HTML recommended/3DS/save-card and React one-time/save-card examples. One-time React validation accepts an empty name but rejects a populated invalid name.
- Changes all 46 local-method HTML examples from popup to auto presentation, retaining their separate explicit-capture and auto-completion strategies.
- Raises declared React wrapper range `^10.4.0` to `^10.5.0` and Server SDK range `^2.4.0` to `^2.5.0`. These are dependency declarations, not exact package release ingests.

### Findings and limits

- ACH consent storage is console logging only; the capture handler does not locally enforce the documented APPROVED status. Optional bank fields are asserted, not validated. No compliance or settlement proof.
- ACH eligibility uses USD 100 while the empty order request creates the USD 205 default cart; reconcile before use.
- React save-card success does not include the final payment-token exchange. This gap predates the update; HTML performs the exchange but database persistence is still a placeholder.
- Shared LPM guidance still says popup while HTML code requests auto. React LPM wrapper typing remains a separate package boundary.
- No React ACH Wallet example or changed Apple Pay/Google Pay/subscription implementation is established.

Updated source sections: evidence boundary; card/vault scope corrections; new ACH, name-field, presentation, dependency and limitation sections. Concepts: new [[paypal-ach]], plus [[paypal-checkout]], [[paypal-apm]], [[paypal-expanded-checkout]], and [[paypal-vault]]. Company, index and logs updated; source count unchanged.

**Evidence:**

- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-09-19-bb23e7c/manifest.json`
- `tracking/github/repos/paypal/v6-web-sdk-sample-integration/comparisons/default-branch/de90a89--bb23e7c/comparison.json`
- `tracking/github/repos/paypal/v6-web-sdk-sample-integration/comparisons/default-branch/de90a89--bb23e7c/diff.patch`
- `tracking/github/repos/paypal/v6-web-sdk-sample-integration/ingest-review-9b81f89d.md`

## `default-branch@de90a89` - Basic Apple Pay Delta (2026-08-29)

| Ref | Prior SHA | Current SHA | Ingest mode |
| --- | --- | --- | --- |
| `main` | `b5f2df209b0bfd10b1a3cde600088ddf21e43523` | `de90a89c90b06421ca34241e7162236e2b04fd79` | Delta |

### Payment behavior

- Adds a Basic Apple Pay one-time-payment example using a browser-safe client token, `basic_apple_pay` eligibility, and `createBasicApplePayOneTimePaymentSession()`.
- PayPal's session drives merchant validation, payment-method selection, and authorization through `start()`; the Basic page does not load Apple's separate JavaScript SDK.
- The merchant server still creates the PayPal order and captures the approved `orderId`.
- Existing recommended and purchase-with-vault Apple Pay examples remain merchant-driven and unchanged.

### React and dependency changes

- Upgrades `@paypal/react-paypal-js` from `^10.1.0` to `^10.4.0` and adds `@types/applepayjs ^14.0.9`.
- Changes the React capability guard from optional `window.ApplePaySession` access to a guarded native `ApplePaySession` global.
- Updates React, router, Vite, lint, formatting, Dotenv, and Node development dependencies.
- Keeps `@paypal/paypal-server-sdk ^2.4.0`; no server route implementation changed.

### Evidence and impact

The generated comparison contains eight retained path changes with no evidence gaps or unclassified changes. The update adds one alternative Apple Pay orchestration contract and does not establish merchant enablement, regional availability, or production eligibility.

**Updated wiki areas:** cumulative repository source; PayPal Apple Pay concept; PayPal company and provider index.

**Evidence:**

- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/manifest.json`
- `tracking/github/repos/paypal/v6-web-sdk-sample-integration/comparisons/default-branch/b5f2df2--de90a89/comparison.json`
- `tracking/github/repos/paypal/v6-web-sdk-sample-integration/comparisons/default-branch/b5f2df2--de90a89/diff.patch`
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/files/client/components/applepayPayments/basicOneTimePayment/html/src/app.js`
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/files/client/prebuiltPages/react/package.json`

## `default-branch@b5f2df2` - Full Baseline (2026-07-15)

| Ref | Prior reviewed SHA | Current SHA | Ingest mode |
| --- | --- | --- | --- |
| `main` | `dd9ef8a53c71d9d2107ad94c23b73b62f9811258` | `b5f2df209b0bfd10b1a3cde600088ddf21e43523` | Full |

The accepted capsule contains 257 selected files and 11 policy exclusions. It is the first collector-managed baseline, so no generated commit comparison exists for the prior manually reviewed SHA.

### Major additions since the legacy review

- React/TypeScript multi-flow application using `@paypal/react-paypal-js@10.1.0` with explicit sandbox environment.
- Fastlane member and guest checkout using browser-safe client tokens and single-use card tokens.
- Google Pay 3DS flow that closes the Google sheet before starting payer action.
- Apple Pay purchase-with-vault example.
- Expanded Node routes for products, order retrieval, eligibility, subscriptions, and multiple order shapes.
- Local-payment-method catalog expanded from six retained European examples to 46 method implementations.
- Complete HTML, configuration, and sandboxed-iframe sources around the previously selected JavaScript files.

### Existing-flow changes

- Common request helpers add response-status checks and clearer failures.
- Server order creation accepts validated `intent` and optional `processingInstruction` values.
- Apple Pay, Card Fields, Google Pay, Guest Payments, PayPal, Venmo, Messages, and subscription samples receive supporting documentation or implementation refinements.
- The current local-method README introduces a shared auto-completion claim that conflicts with six explicit-capture implementations; the cumulative source records the discrepancy.

### Evidence and impact

This is a broad architecture and payment-behavior expansion, justifying full ingest. The sample proves code patterns at this SHA but does not prove merchant eligibility or current production availability.

**Updated wiki areas:** cumulative repository source; PayPal Checkout; APMs; Fastlane; Apple Pay; Google Pay; Vault; Subscriptions; PayPal company and provider index.

**Evidence:**

- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/manifest.json`
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/README.md`
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/client/prebuiltPages/react/README.md`
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/client/components/localPaymentMethods/README.md`
- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/files/server/node/src/routes/index.ts`

## Historical Reviewed Baseline - `dd9ef8a` (reviewed 2026-04-17)

The initial manual review retained 36 files covering PayPal one-time payment and advanced presentation modes, PayPal and card vaulting, Card Fields and 3DS, Venmo, Apple Pay, Google Pay, Guest Payments, Messages, subscriptions, ACH, SEPA, and six European local methods.

This evidence remains valid only as commit-qualified historical context. It was not collected through the current immutable snapshot system.

**Evidence:**

- `raw/github-paypal-v6-samples.md`
- `raw/github-paypal-v6-samples/`

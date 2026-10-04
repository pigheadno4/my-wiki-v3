---
title: "GitHub changelog: paypal-examples/v6-web-sdk-sample-integration"
type: source
date_ingested: 2026-08-04
date_updated: 2026-10-04
original_format: github-repo
raw_files:
  - "github/paypal/v6-web-sdk-sample-integration/snapshots/2026-10-04-a318bcf/manifest.json"
  - "github/paypal/v6-web-sdk-sample-integration/snapshots/2026-09-19-bb23e7c/manifest.json"
  - "github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-30-de90a89/manifest.json"
  - "github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/manifest.json"
  - "github-paypal-v6-samples.md"
tags: [paypal, web-sdk-v6, samples, changelog, github-repository]
---

## Overview

Commit-qualified history for `paypal-examples/v6-web-sdk-sample-integration`. Durable integration guidance belongs in [[source-github-v6-web-sdk-sample-integration]].

## `default-branch@a318bcf` - Direct PayPal Saved Payment Methods (2026-09-29)

| Ref | Prior SHA | Current SHA | Ingest mode |
| --- | --- | --- | --- |
| `main` | `bb23e7c63305a872326f43c3d52c5edd53e20b43` | `a318bcf7cb8a458b180df553ab459db3a5a79586` | Full additive; approved option-1 focused reading |

Collected/ingested October 4, 2026. Two added and twelve modified retained files, 250 unchanged, no deletion. All changed files and twelve prior versions plus affected dependencies read fully; 262 prior and 264 current file hashes verified. The full 537-path assignment was not semantically reread; immutable inventories, packet and earlier wiki history are preserved.

### New and changed behavior

- Adds a static direct-PayPal returning-buyer preview/edit page using `paypal-saved-payment-methods`, its custom element and `createPayPalEditSavedPaymentSession({ commit: false, ... })`.
- Client-token route accepts `target_customer_id` or a `vault_id` claim; a `B-`-prefixed ID selects `billing_agreement_id`. This is distinct from Braintree's preferred-token/nonce path.
- Editing creates an order without a vault ID, stores the approved ID and captures it on Submit Order. Direct submission includes the vault ID and avoids recapture if Create Order returned `COMPLETED`; customer-ID-only configuration requires approval first.
- Save-payment response exposes payment-token/customer IDs for local testing, with an explicit production server-side-storage warning; actual database persistence remains empty.
- Core dependency range `^10.0.1` -> `^11.2.0`; React wrapper `^10.5.0` -> `^10.5.2`. TypeScript button guards become early returns, lint/tool ranges advance, and two iframe examples move Node 20 -> 22. No new React saved-method page or wrapper is established.

### Findings and limits

- HTML's either-ID/not-both instruction is not enforced; blank/both inputs can reach the token endpoint.
- Failed/ineligible reinitialization can leave the earlier visible element/session; overlapping initialization has no generation guard. No browser reproduction was performed.
- Server has no inspected customer-authentication/ownership binding; identifier display, empty persistence, unchecked "captured" labels and fresh per-request UUIDs are not production security, settlement or duplicate-payment guarantees.
- The September 27 direct-v6 frontend-gap analysis now has a dated sample-code update; historical findings remain, while typed/React parity, eligibility and live behavior remain unproven.
- Changed test and lockfile are excluded under existing policy. No runtime, payment, build or browser test; no registry or collection-policy change.

Updated source sections: latest identity, evidence boundary, new saved-method flows, token handoff, limitations and exact evidence. Concepts: [[paypal-checkout]], [[paypal-vault]]. Company/index/logs and the dated [[analysis-paypal-v5-v6-returning-buyer-frontend-gap]] updated; company source count unchanged.

**Evidence:**

- `raw/github/paypal/v6-web-sdk-sample-integration/snapshots/2026-10-04-a318bcf/manifest.json`
- `tracking/github/repos/paypal/v6-web-sdk-sample-integration/comparisons/default-branch/bb23e7c--a318bcf/comparison.json`
- `tracking/github/repos/paypal/v6-web-sdk-sample-integration/comparisons/default-branch/bb23e7c--a318bcf/diff.patch`
- `tracking/github/repos/paypal/v6-web-sdk-sample-integration/ingest-review-9765a512.md`

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

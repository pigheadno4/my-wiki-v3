---
title: "GitHub changelog: paypal-examples/v6-web-sdk-sample-integration"
type: source
date_ingested: 2026-08-04
date_updated: 2026-08-04
original_format: github-repo
raw_files:
  - "github/paypal/v6-web-sdk-sample-integration/snapshots/2026-08-04-b5f2df2/manifest.json"
  - "github-paypal-v6-samples.md"
tags: [paypal, web-sdk-v6, samples, changelog, github-repository]
---

## Overview

Commit-qualified history for `paypal-examples/v6-web-sdk-sample-integration`. Durable integration guidance belongs in [[source-github-v6-web-sdk-sample-integration]].

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

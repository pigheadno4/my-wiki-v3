---
title: "GitHub changelog: paypal-examples/v6-web-sdk-with-braintree-sdk-sample-integration"
type: source
date_ingested: 2026-08-17
date_updated: 2026-10-02
original_format: github-repo
raw_files:
  - "github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-10-02-06bc2de/manifest.json"
  - "github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-10-02-06bc2de-9592883c/manifest.json"
  - "github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/manifest.json"
  - "github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-08-16-f1c7123-dd2b315d/manifest.json"
tags: [paypal, braintree, web-sdk-v6, samples, changelog, github-repository]
---

## Overview

Commit-qualified history for `paypal-examples/v6-web-sdk-with-braintree-sdk-sample-integration`. Durable architecture and implementation guidance belongs in [[source-github-v6-web-sdk-with-braintree-sdk-sample-integration]].

## `default-branch@06bc2de` - Additive Full Ingest (2026-10-01)

| Ref | Prior accepted SHA | Current SHA | Ingest mode |
| --- | --- | --- | --- |
| `main` | `f1c712374f674ce6f0b2683f105871dcb969d2d7` | `06bc2de96264a29f33ff7b6eb0d566c1cd162b0a` | Full, approved focused reading |

Collected and ingested October 2. Current snapshot: 68 files, 137,194 bytes; approved saved-payment frontend supplement: two files, 10,784 bytes. The retained inventory reports eight added/modified paths and 60 unchanged. Five paths are actual upstream changes within the comparison pathspec; React `index.html`, React `utils.ts` and Node `.nvmrc` are newly retained but identical to the prior supplement. Do not report those three as new functionality. The supplemented frontend lies outside the unchanged collection policy.

### Changes and integration impact

- Static navigation adds View/Edit Saved Payment. The billing-agreement example exposes the newly vaulted token and customer ID for demo setup.
- Token generation accepts a preferred token or customer lookup and introduces a server-side sandbox GraphQL helper using `input.clientToken.paymentMethodId`.
- The supplemented frontend loads Braintree Web `3.146.0`, creates a fresh v6 edit session with authorize intent and commit false, tokenizes approval, and separately submits an edited nonce or the existing vault token.
- The transaction route expands the earlier nonce-only contract to exactly one truthy nonce/token and still requests settlement submission.
- Existing React source and dependency declarations remain unchanged; this commit is not a React edit wrapper or an independently versioned PayPal JS release.

### Migration and limits

Resolve saved-method ownership from authenticated server-side identity; do not copy the sample's trusted-browser identifier inputs or browser-controlled amount. Keep GraphQL credentials on the server. Check the Braintree result and persist authoritative payment state. The unconditional frontend "captured" message conflicts with its unchecked result and is mirrored in the source and concept; neither tokenization nor submission proves settlement or durable default-funding-instrument mutation. No runtime/payment test was performed.

Full mode was approved because token generation and payment submission change together. The focused-reading exception covered complete changed retained files, both supplemental frontend files and affected prior/dependency code; unchanged evidence and inventories were verified by hash. All prior history below remains.

**Updated wiki areas:** cumulative source's `default-branch@06bc2de` section; [[paypal-braintree-integration]]; PayPal company, provider index and logs.

**Evidence:** [current snapshot](../../../../raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-10-02-06bc2de/manifest.json), [frontend supplement](../../../../raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-10-02-06bc2de-9592883c/manifest.json), [comparison](../../../../tracking/github/repos/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/comparisons/default-branch/f1c7123--06bc2de/comparison.md).

- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-10-02-06bc2de/manifest.json` - root-qualified immutable commit evidence
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-10-02-06bc2de-9592883c/manifest.json` - approved supplemental frontend evidence
- `tracking/github/repos/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/comparisons/default-branch/f1c7123--06bc2de/comparison.json` - exact-SHA comparison identity and content hashes

## `default-branch@f1c7123` - Full Baseline (2026-06-25)

| Ref | Prior accepted SHA | Current SHA | Ingest mode |
| --- | --- | --- | --- |
| `main` | none | `f1c712374f674ce6f0b2683f105871dcb969d2d7` | Full |

This is the first accepted baseline. The snapshot retains 64 selected files totaling 130,398 bytes and excludes one test file totaling 1,151 bytes. A linked three-file supplement adds dependencies discovered during review without changing the exact SHA.

### Baseline scope

- Static Braintree Web `3.142.0` examples for one-time payment, line items, shipping updates, Smart Payment Stack, checkout with vault, billing agreements, and PayPal Messages.
- Billing-agreement metadata examples for `RECURRING`, `SUBSCRIPTION`, and `UNSCHEDULED` plan types.
- React 19 sample using `@paypal/react-paypal-js@^10.1.0` with prebuilt and custom-hook payment integrations.
- Node 20 server using `braintree@^3.36.0` for client-token generation, transaction sales, product lookup, customer creation, and payment-method storage.

### Impact and boundaries

The baseline establishes a runnable Braintree-account integration path and nonce-based server handoff. It also records production gaps: browser-controlled amounts, per-request customer creation, sandbox-only gateway configuration, unrestricted CORS, exposed exception text, and no authoritative settlement-state handling.

The README's PayPal/Venmo feature-setting instruction is not treated as an implemented Venmo payment flow. Repository presence and button rendering do not prove merchant or buyer eligibility.

**Updated wiki areas:** cumulative repository source; [[paypal-braintree-integration]]; PayPal company, provider index, and provider logs.

**Evidence:**

- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/manifest.json`
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/README.md`
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/client/paypalOneTimePayments/smartStack/src/app.js`
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/client/paypalBillingAgreements/recurring/src/app.js`
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/files/server/node/src/routes/transactionRouteHandler.ts`
- `raw/github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-08-16-f1c7123-dd2b315d/manifest.json`

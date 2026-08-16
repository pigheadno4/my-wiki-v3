---
title: "GitHub changelog: paypal-examples/v6-web-sdk-with-braintree-sdk-sample-integration"
type: source
date_ingested: 2026-08-17
original_format: github-repo
raw_files:
  - "github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/snapshots/2026-08-16-f1c7123/manifest.json"
  - "github/paypal/v6-web-sdk-with-braintree-sdk-sample-integration/supplements/2026-08-16-f1c7123-dd2b315d/manifest.json"
tags: [paypal, braintree, web-sdk-v6, samples, changelog, github-repository]
---

## Overview

Commit-qualified history for `paypal-examples/v6-web-sdk-with-braintree-sdk-sample-integration`. Durable architecture and implementation guidance belongs in [[source-github-v6-web-sdk-with-braintree-sdk-sample-integration]].

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

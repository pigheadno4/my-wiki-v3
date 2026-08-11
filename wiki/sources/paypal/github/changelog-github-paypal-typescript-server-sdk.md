---
title: "GitHub changelog: paypal/paypal-typescript-server-sdk"
type: source
date_ingested: 2026-08-10
date_updated: 2026-08-10
original_format: github-repo
raw_files:
  - "github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-dbdbdd0/manifest.json"
  - "github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/manifest.json"
tags: [paypal, typescript, server-sdk, changelog, github-repository]
---

## Overview

Package-qualified history for `paypal/paypal-typescript-server-sdk`. Durable SDK behavior belongs in [[source-github-paypal-typescript-server-sdk]]; this page records reviewed releases and future deltas without replacing older findings.

## `@paypal/paypal-server-sdk@2.4.0` - Delta (2026-06-05)

| Package | Prior reviewed release | Exact SHA | Ingest mode |
| --- | --- | --- | --- |
| `@paypal/paypal-server-sdk@2.4.0` | `@paypal/paypal-server-sdk@2.3.0` | `dbdbdd06f18a06d633c66bbc27d7d7a54283e1a3` | Delta |

The 397-file, 924,075-byte capsule adds a typed Orders processing instruction, explicitly selects the default base URL for OAuth token requests, and regenerates API documentation/model metadata. It preserves the five-controller package architecture established by the `2.3.0` baseline.

### Exact delta

- Adds `ProcessingInstruction.OrderCompleteOnPaymentApproval` with wire value `ORDER_COMPLETE_ON_PAYMENT_APPROVAL` to create/confirm request and Order response typing.
- Adds `req.baseUrl('default')` to OAuth client-credentials token acquisition.
- Adds authentication and successful-response sections to generated controller documentation, marks many generated response properties read-only, and normalizes PayPal documentation URLs.
- Advances package and README references to `2.4.0`.
- Supplies no upstream `2.4.0` release notes; the exact delta is derived from the retained comparison.

### Evidence

- `raw/github/paypal/paypal-typescript-server-sdk/releases/paypal-server-sdk/2.4.0/2026-08-10/manifest.json`
- `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-dbdbdd0/manifest.json`
- `tracking/github/repos/paypal/paypal-typescript-server-sdk/comparisons/paypal-server-sdk/2.3.0--2.4.0/comparison.json`

## `@paypal/paypal-server-sdk@2.3.0` - Full Baseline (2026-04-01)

| Package | Prior reviewed release | Exact SHA | Ingest mode |
| --- | --- | --- | --- |
| `@paypal/paypal-server-sdk@2.3.0` | Legacy unpinned `2.3.0` stub | `b37cec58f2cdeecf5b9b7a7c15131cc5f4fff712` | Full |

The accepted 2026-08-10 capsule contains 396 files totaling 911,587 bytes. It establishes an exact baseline for the five controller families, generated request/response types, OAuth client-credentials client, CommonJS/ESM package surface, configuration, retries, and errors.

### Baseline impact

- Replaces an unpinned README-level wiki summary with fully read, exact-SHA source evidence.
- Preserves the Orders, Payments, Vault, Transaction Search, and Subscriptions controller contracts.
- Records Sandbox and zero-retry defaults, Node.js `>=14.17.0`, endpoint-specific headers, broad payment-source typing, and full subscription lifecycle coverage.
- Corrects the wiki's Vault method names to the `2.3.0` API: `createSetupToken()` and `createPaymentToken()`.

### Release-attribution update

The upstream `2.3.0` release record contains no notes. The repository changelog collected with `2.4.0` now identifies `2.3.0` as fixing ESM/CommonJS build differences. The entry remains a full-surface baseline; only that build fix is attributed specifically to `2.3.0`.

### Historical sequence retained in the baseline

| Version | Retained upstream summary |
| --- | --- |
| `2.2.0` | Added missing subscriber email/payer fields and PayPal vault `store_in_vault` fields |
| `2.1.0` | Corrected Transaction Search naming and shipment-carrier `OTHERS` |
| `2.0.0` | Added Transaction Search and Subscriptions; breaking model renames and shipping-callback model removal |
| `1.1.0` | Added Apple Pay and Google Pay models and optional fields |
| `1.0.0` | GA for Orders, Payments, and Vault |

### Evidence

- `raw/github/paypal/paypal-typescript-server-sdk/releases/paypal-server-sdk/2.3.0/2026-08-10/manifest.json`
- `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/manifest.json`
- `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/files/CHANGELOG.md`
- `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/files/README.md`
- `raw/github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/files/package.json`

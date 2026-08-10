---
title: "GitHub changelog: paypal/paypal-typescript-server-sdk"
type: source
date_ingested: 2026-08-10
original_format: github-repo
raw_files:
  - "github/paypal/paypal-typescript-server-sdk/snapshots/2026-08-10-b37cec5/manifest.json"
tags: [paypal, typescript, server-sdk, changelog, github-repository]
---

## Overview

Package-qualified history for `paypal/paypal-typescript-server-sdk`. Durable SDK behavior belongs in [[source-github-paypal-typescript-server-sdk]]; this page records reviewed releases and future deltas without replacing older findings.

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

### Release-attribution boundary

The upstream `2.3.0` release record contains no notes, and the retained repository changelog ends at `2.2.0`. This entry therefore treats all reviewed behavior as a `2.3.0` baseline and does not claim that `2.3.0` introduced it. The already-collected `2.4.0` work item remains a separate delta and must be approved and ingested serially.

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

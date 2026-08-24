---
title: "GitHub changelog: paypal/paypal-php-server-sdk"
type: source
date_ingested: 2026-08-24
date_updated: 2026-08-24
original_format: github-repo
raw_files:
  - "github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/manifest.json"
tags: [paypal, php, server-sdk, changelog, github-repository]
---

## Overview

Package-qualified history for `paypal/paypal-php-server-sdk`. Durable SDK behavior belongs in [[source-github-paypal-php-server-sdk]]; this page records reviewed releases and future deltas without replacing older findings.

## `paypal/paypal-server-sdk@2.4.0` - Full Baseline (2026-08-21)

| Package | Prior reviewed release | Exact SHA | Ingest mode |
| --- | --- | --- | --- |
| `paypal/paypal-server-sdk@2.4.0` | Legacy unpinned `2.2.0` stub | `b6be767b759ac3e3ad1d32dde7143a0927f5892b` | Full |

The accepted 2026-08-24 capsule contains 689 files totaling 2,641,320 bytes. It establishes an exact baseline for the five controller families, generated request/response models, OAuth client credentials, configuration, retries, logging, proxies, HTTP wrappers, and errors.

### Baseline impact

- Replaces an unpinned README-level `2.2.0` wiki summary with fully read, exact-SHA `2.4.0` source evidence.
- Preserves Orders, Payments, Vault, Transaction Search, and Subscriptions controller contracts.
- Records PHP `^7.2 || ^8.0`, Sandbox and zero-retry defaults, endpoint-specific idempotency guidance, and the package's US-only Vault label.
- Corrects the old comparison claim that configurable retries and proxies distinguish PHP from TypeScript; both reviewed packages expose these facilities.
- Preserves generated Venmo and other payment-source models as type evidence without treating them as merchant-availability proof.

### Release-attribution boundary

The upstream release record contains no `2.4.0` notes, and the repository changelog ends at `2.3.0`. The complete `2.4.0` package is therefore the baseline, but no feature in it is labeled as a `2.4.0` addition without a prior exact PHP snapshot comparison.

### Historical sequence retained in the baseline

| Version | Retained upstream summary |
| --- | --- |
| `2.3.0` | Added Orders `processing_instruction` fields and corrected documentation URLs |
| `2.2.0` | Added missing subscriber email/payer fields and PayPal vault `store_in_vault` fields |
| `2.1.0` | Corrected Transaction Search naming and shipment-carrier `OTHERS` |
| `2.0.0` | Added Transaction Search and Subscriptions; breaking model renames and shipping-callback model removal |
| `1.1.0` | Added Apple Pay and Google Pay models, proxy support, and optional fields |
| `1.0.0` | GA for Orders, Payments, and Vault |

### Evidence

- `raw/github/paypal/paypal-php-server-sdk/releases/paypal-server-sdk/2.4.0/2026-08-24/manifest.json`
- `raw/github/paypal/paypal-php-server-sdk/releases/paypal-server-sdk/2.4.0/2026-08-24/release-notes.md`
- `raw/github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/manifest.json`
- `raw/github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/files/CHANGELOG.md`
- `raw/github/paypal/paypal-php-server-sdk/snapshots/2026-08-24-b6be767/files/README.md`
- `tracking/github/repos/paypal/paypal-php-server-sdk/ingest-packets/github-26220457423a12b6b561/packet.json`

---
title: "GitHub changelog: paypal/paypal-rest-api-specifications"
type: source
date_ingested: 2026-08-11
date_updated: 2026-08-11
original_format: github-repo
raw_files:
  - "github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/manifest.json"
tags: [paypal, openapi, api-spec, changelog, github-repository]
---

## Overview

Commit-qualified history for `paypal/paypal-rest-api-specifications`. Durable schema knowledge belongs in [[source-github-paypal-rest-api-specifications]]; this page records reviewed repository baselines and future deltas without replacing older findings.

## `default-branch@90e8041` - Full Baseline (2026-04-07)

| Ref | Prior reviewed baseline | Exact SHA | Ingest mode |
| --- | --- | --- | --- |
| `default-branch@90e8041` | Legacy unpinned April collection | `90e8041ffe02d80c452d2b476bedd59a8d219bdc` | Full |

The accepted 2026-08-11 capsule contains 16 files totaling 3,415,255 bytes: 13 OpenAPI contracts plus README, package metadata, and license. The exact SHA and all 13 OpenAPI file hashes match the April 2026 collection, so this entry establishes a canonical exact-SHA baseline rather than a new upstream delta.

### Baseline impact

- Migrates the cumulative source into the canonical PayPal/GitHub hierarchy and preserves the legacy raw stub.
- Replaces a high-level API list with fully reviewed operation, schema, enum, and evidence-boundary coverage.
- Corrects OpenAPI format metadata: Orders and Payments are 3.0.4; the other retained contracts are 3.0.3.
- Separates Catalog Products CRUD from the Subscriptions specification.
- Corrects the wiki's recurring-charge schema: Orders `stored_credential` uses `payment_type`; Vault owns wallet `usage_pattern`.
- Records 13 declared API versions and 115 total operations without treating schema presence as product availability.

### Evidence

- `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/manifest.json`
- `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/files/README.md`
- `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/files/openapi/`
- `raw/github/paypal/paypal-rest-api-specifications/snapshots/2026-08-11-90e8041/files/package.json`

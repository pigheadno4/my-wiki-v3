---
title: "GitHub changelog: Adyen/adyen-node-api-library"
type: source
date_ingested: 2026-08-02
original_format: github-repo
raw_files:
  - "github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/manifest.json"
tags: [adyen, nodejs, server-sdk, checkout-api, cloud-device-api, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-node-api-library`. Cumulative implementation knowledge belongs in [[source-github-adyen-node-api-library]] and the linked immutable snapshots.

## `@adyen/api-library@32.0.0` (2026-07-15)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@adyen/api-library` | Initial baseline | `32.0.0` | `99d1a0cf69c8660952baffd1437b00aae2fa4f23` | Full |

**Important findings:** Checkout API moves to v72 with breaking request-model changes. Cloud Device API v1 becomes a first-class replacement for legacy cloud Terminal API use, including device management, region routing, and an encrypted Nexo variant.

**Developer or merchant impact:** Checkout integrations must update removed or newly required fields before upgrading. Cloud point-of-sale integrations can remain on legacy Terminal cloud in this baseline, but new features are directed to Cloud Device API and live usage requires region and credential-role configuration.

**Migration action:** Supply Australian direct-debit holder name; replace removed donation, conversion, authentication-only, and enhanced-scheme fields; use `checkoutAttemptId` and `mpiData` where applicable. For Cloud Device migration, account for generated model names and types, wrapped async responses, merchant/device parameters, matching `POIID`, and event-notification handling.

**Additional release scope:** Authorization updates gain CIT/MIT classification and synchronous adjustment data. Transfer models and cash-out/tracing features change outside the checkout focus. Nexo and webhook HMAC handling receive fixes. Node.js 24 is a CI tooling update; the package runtime declaration remains Node.js 18 or newer.

**Updated source sections:** package and client setup; transport; Checkout API v72; Checkout migration; Cloud Device API; notifications and HMAC; broader API inventory.

**Evidence boundary:** This is the first retained exact-SHA baseline, so no prior snapshot comparison exists. Release-introduced claims come from the release record; broader architecture is cumulative behavior present at the same SHA.

**Evidence:**

- Release manifest: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.0.0/2026-08-02/manifest.json`
- Release notes: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.0.0/2026-08-02/release-notes.md`
- Snapshot manifest: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/manifest.json`
- Checkout implementation: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/src/services/checkout/`
- Cloud Device migration: `raw/github/adyen/adyen-node-api-library/snapshots/2026-08-02-99d1a0c/files/doc/MigratingToCloudDeviceApi.md`

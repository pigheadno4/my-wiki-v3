---
title: "GitHub changelog: Adyen/adyen-node-api-library"
type: source
date_ingested: 2026-10-04
original_format: github-repo
raw_files:
  - "github/adyen/adyen-node-api-library/snapshots/2026-10-04-134f500/manifest.json"
  - "github/adyen/adyen-node-api-library/snapshots/2026-10-04-afd3bb4/manifest.json"
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

## `@adyen/api-library@32.0.0` -> `@adyen/api-library@32.1.0` (2026-09-03)

Exact SHA `afd3bb485d84d861324a183b99839431bafa4e68`; additive full ingest
with approved focused reading, completed 2026-10-04. All older history retained.

**Important findings:** Sessions gain `updateSession` for amount changes, required
callback `sessionData`, and a finalizing `payable` flag. Payment/donation/action
discriminator mappings are populated. PayPal order updates gain delivery address,
shipping and discount amounts; enriched scheme data and third-party token templates
extend typed checkout requests. Checkout remains v72; runtime remains Node.js >=18.

**Migration:** Review removed Checkout error exports and Paybright enum, gopay
stored-method mapping, and custom HTTP clients' new `string | Buffer` payload
contract. Finalize only when the trusted server amount is final; `payable: true`
prevents further Session updates. Request models are not merchant eligibility proof.

**Additional scope:** Buffered multipart helper and Document Collector upload
service, Session Authentication export, form-data 4.0.6 and micromatch override.
Broader domain models/transitive security fixes remain inventory or notes-level.
Five notification types are unchanged coverage from the old supplement. The HMAC
README example is corrected without changing the validator implementation.

**Updated source sections:** 32.1.0 lifecycle, models, transport/dependency and
evidence-boundary sections; existing notification prose narrowed to actual branches.
Concept, company, provider index/log and root log updated; source count unchanged.

**Evidence:**
- Snapshot: `raw/github/adyen/adyen-node-api-library/snapshots/2026-10-04-afd3bb4/manifest.json`
- Release record: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.1.0/2026-10-04/manifest.json`
- Release notes: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.1.0/2026-10-04/release-notes.md`
- Comparison: `tracking/github/repos/adyen/adyen-node-api-library/comparisons/api-library/32.0.0--32.1.0/comparison.json`, `comparison.md` and `diff.patch`
- Exact implementation paths are listed in [[source-github-adyen-node-api-library]].

## `@adyen/api-library@32.1.0` -> `@adyen/api-library@32.2.0` (2026-09-24)

Exact SHA `134f50078ca8889ff21e6c76f71c6377ddcb2120`; delta ingest with
approved focused reading, completed 2026-10-04. Earlier history preserved.

**Important findings:** Non-proxy HTTPS agent caching per HTTP client instance;
optional constructor AgentOptions for explicit keep-alive; agent preserved on
HTTPS 308 redirects; cache invalidated when a different certificate path is installed.
Certificate loading errors reject before sending. Existing one-hop and host checks
remain. Checkout v72 and Node.js >=18 are unchanged.

**Migration/impact:** Reuse the merchant Client instance to keep the agent cache.
Default options do not explicitly enable keep-alive; proxy agents are still created
per request. Same certificate path returns early, so in-place file replacement is
not automatically detected. No performance or payment execution claim.

**Broader scope:** Notes announce Payments App sub-merchant boarding-token data;
excluded domain models prevent exact field/eligibility claims. The mutable `HEAD`
changelog link in notes is not the comparison authority.

**Updated sections:** cumulative 32.2.0 transport and inventory findings;
Node concept, company status, provider index and logs. Source count remains 14;
unique ingested Adyen package releases becomes 21.

**Evidence:**
- Snapshot: `raw/github/adyen/adyen-node-api-library/snapshots/2026-10-04-134f500/manifest.json`
- Release record: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.2.0/2026-10-04/manifest.json`
- Notes: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.2.0/2026-10-04/release-notes.md`
- Transport: `raw/github/adyen/adyen-node-api-library/snapshots/2026-10-04-134f500/files/src/httpClient/httpURLConnectionClient.ts`
- Comparison: `tracking/github/repos/adyen/adyen-node-api-library/comparisons/api-library/32.1.0--32.2.0/comparison.json`, `comparison.md` and `diff.patch`

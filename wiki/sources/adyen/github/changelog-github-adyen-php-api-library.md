---
title: "GitHub changelog: Adyen/adyen-php-api-library"
type: source
date_ingested: 2026-08-20
date_updated: 2026-10-29
original_format: github-repo
raw_files:
  - "github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/manifest.json"
  - "github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/manifest.json"
tags: [adyen, php, server-sdk, checkout-api, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-php-api-library`. The collection release ID is `adyen-php-api-library@30.0.2`; the installable Composer package is `adyen/php-api-library@30.0.2`. Cumulative implementation knowledge belongs in [[source-github-adyen-php-api-library]] and the linked immutable snapshots.

## `adyen/php-api-library@30.1.0` (2026-09-24; ingested 2026-10-29)

- From 30.0.2, SHA `7eda6b3956a61d41a1fb87ab6d4ef30c7d6712cb`, tag v30.1.0. Approved full additive ingest with focused reading; all older knowledge preserved. The collector's adyen-php-api-library alias and installable Composer adyen/php-api-library identify this same release.
- Classic Payments v68 adds transactionLinkId request/response model maps, constructors and getters/setters. Documentation scopes it to Mastercard TLID/MIT contract chains when Adyen does not tokenize, with ContAuth and Subscription/UnscheduledCardOnFile. The setter does not enforce these conditions; networkTxReference remains, and Checkout v71 is unchanged. No identifier equivalence or merchant eligibility guarantee.
- Client adds setRegion, storing region only, and deprecates retrieveCloudEndpoint. Config keys and endpoint responsibility differ between retained client and the release-noted PosPayment flow; PosPayment is outside the capsule. Do not promise end-to-end routing or change Checkout prefix instructions. Existing helper comment versus actual unsupported-region throw is qualified in source/concept.
- Foreign Exchange v1, Payments App and transfer/transaction/management webhook changes are announcement/inventory-level coverage, not retained implementation. Notes include obsolete advice status removal as well as new tracing/network fields; do not project them onto tokenization webhooks.
- Development-only PHP CodeSniffer becomes 4.0.2; runtime PHP >=7.3/extensions unchanged. Security recommendation flags are not payment-runtime vulnerability proof; the stale security support table is unchanged.
- Both 447-file snapshots verified: six modified/441 unchanged; all 894 size/SHA-256/Git blob identities match. All 45 upstream changes dispositioned (six retained/39 exclusions), no gaps/unclassified changes. Full assignment456 paths/7,513,409 bytes; complete changed retained files, affected prior context and cumulative source/changelog read, unchanged files/manifests/inventories mechanically verified under approval. Existing concept first, source/company/index/logs updated, source_count unchanged. No extra collection, SDK/API/payment execution, commit or push.

Evidence:
- `raw/github/adyen/adyen-php-api-library/snapshots/2026-10-29-7eda6b3/manifest.json`
- `raw/github/adyen/adyen-php-api-library/releases/adyen-php-api-library/30.1.0/2026-10-29/manifest.json` - adjacent release-notes.md
- `tracking/github/repos/adyen/adyen-php-api-library/comparisons/adyen-php-api-library/30.0.2--30.1.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-adyen-php-api-library]] - exact source paths and five located quotes

## `adyen/php-api-library@30.0.2` (2026-08-05)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `adyen/php-api-library` | Initial baseline | `30.0.2` | `6ef96571834bc460201df8aea8c89882b2043cd8` | Full |

**Important findings:** The release updates generated Stored Value services and models, fixes PHP 8.5 `curl_close()` deprecation behavior, converts deprecations to errors in project checks, and updates development dependencies. A generated Payments update was reverted before release.

**Developer or merchant impact:** PHP 8.5 integrations avoid the deprecated close call. The release notes do not establish a net new Payments API contract because the generated Payments change was reverted.

**Migration action:** No mandatory merchant migration is documented. Use the package's PHP 7.3-or-later runtime baseline and provide a merchant-specific live URL prefix for live Checkout requests.

**Updated source sections:** package and client setup; transport; Checkout API v71; classic Payments and Recurring APIs; tokenization webhooks and signatures; broader API inventory; exact release findings.

**Evidence boundary:** This is the first retained exact-SHA baseline, so no prior snapshot comparison exists. Release-introduced claims come from the release record; broader architecture is cumulative behavior present at the same SHA. The stale `SECURITY.md` support table is retained as a contradiction, not current policy.

**Evidence:**

- Release manifest: `raw/github/adyen/adyen-php-api-library/releases/adyen-php-api-library/30.0.2/2026-08-19/manifest.json`
- Release notes: `raw/github/adyen/adyen-php-api-library/releases/adyen-php-api-library/30.0.2/2026-08-19/release-notes.md`
- Snapshot manifest: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/manifest.json`
- Runtime version: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/VERSION`
- Client implementation: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/src/Adyen/Client.php`
- Contradictory security table: `raw/github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/files/SECURITY.md`

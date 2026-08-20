---
title: "GitHub changelog: Adyen/adyen-php-api-library"
type: source
date_ingested: 2026-08-20
original_format: github-repo
raw_files:
  - "github/adyen/adyen-php-api-library/snapshots/2026-08-19-6ef9657/manifest.json"
tags: [adyen, php, server-sdk, checkout-api, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-php-api-library`. The collection release ID is `adyen-php-api-library@30.0.2`; the installable Composer package is `adyen/php-api-library@30.0.2`. Cumulative implementation knowledge belongs in [[source-github-adyen-php-api-library]] and the linked immutable snapshots.

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

---
title: "GitHub changelog: braintree/braintree_ios"
type: source
date_ingested: 2026-10-04
original_format: github-repo
raw_files:
  - "github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/manifest.json"
  - "github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/manifest.json"
  - "github/braintree/braintree_ios/snapshots/2026-10-04-2a9aa1e/manifest.json"
  - "github/braintree/braintree_ios/snapshots/2026-10-04-eb7f88e/manifest.json"
  - "github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/manifest.json"
tags: [braintree, ios, mobile-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree_ios`. Cumulative implementation knowledge belongs in [[source-github-braintree-ios]] and the linked immutable snapshot.

## `braintree-ios@7.13.0` (2026-09-23)

Delta from `braintree-ios@7.12.0` to `braintree-ios@7.13.0`; SHA `020dfb7a7803ec3ce8b2df2a0f71e386a4bf84e3`; ingested 2026-10-04.

**Changes, impact and migration:** Declared iOS minimum 16 -> 15; PayPal return-tokenization background task and cancellation/error handling; iOS 15-compatible locale, card validation and CVV-delay APIs. Apple Pay recurring metadata remains iOS 16+ in the demo. Review deployment targets and error handling, but do not treat code 15 as definitive OS-expiry proof. No local build/payment test.

**Updated source sections:** 7.13.0 delta and raw evidence; [[braintree-ios-sdk]]. Prior baseline/history preserved. No substantive cross-company comparison or unresolved contradiction: changes are version-qualified.

**Evidence:** `raw/github/braintree/braintree_ios/releases/braintree-ios/7.13.0/2026-10-04/manifest.json`; `raw/github/braintree/braintree_ios/releases/braintree-ios/7.13.0/2026-10-04/release-notes.md`; `raw/github/braintree/braintree_ios/snapshots/2026-10-04-020dfb7/manifest.json`; `tracking/github/repos/braintree/braintree_ios/comparisons/braintree-ios/7.12.0--7.13.0/comparison.json`. Implementation paths in [[source-github-braintree-ios]]. User-approved focused reading; binary/build/payment behavior not tested.


## `braintree-ios@7.12.0` (2026-09-16)

Delta from `braintree-ios@7.11.0` to `braintree-ios@7.12.0`; SHA `09bc25a1564b0eb8c802d2ef396ec27ceaf9cd2f`; ingested 2026-10-04.

**Changes, impact and migration:** Upstream Xcode 27/iOS 27 support statement; PayPalMessages dependency 1.0.0 -> 2.0.0. Minimum iOS remains 16 in this release. Source-only model relocations preserve payload behavior, and the recursive Card pod glob includes moved files. Amex SwiftUI demo adds nonce completion after its non-error rewards lookup path. Review dependency resolution/builds separately; binaries not tested.

**Updated source sections:** 7.12.0 delta and raw evidence; [[braintree-ios-sdk]]. Prior baseline/history preserved. No substantive cross-company comparison or unresolved contradiction: changes are version-qualified.

**Evidence:** `raw/github/braintree/braintree_ios/releases/braintree-ios/7.12.0/2026-10-04/manifest.json`; `raw/github/braintree/braintree_ios/releases/braintree-ios/7.12.0/2026-10-04/release-notes.md`; `raw/github/braintree/braintree_ios/snapshots/2026-10-04-09bc25a/manifest.json`; `tracking/github/repos/braintree/braintree_ios/comparisons/braintree-ios/7.11.0--7.12.0/comparison.json`. Implementation paths in [[source-github-braintree-ios]]. User-approved focused reading; binary/build/payment behavior not tested.


## `braintree-ios@7.11.0` (2026-08-28)

Delta from `braintree-ios@7.10.0` to `braintree-ios@7.11.0`; SHA `2a9aa1e20b1d066cb97c66af3e2ccd7f17e90fc0`; ingested 2026-10-04.

**Changes, impact and migration:** Risk packaging/signing repair, not a new payment API. PayPalRisk 5.6.0 replaces the local framework declaration. Carthage consumers must update XCFrameworks and embed the now-dynamic PPRiskMagnes framework. Source import remains unchanged. Signing and dynamic-linkage claims are upstream release statements, not local binary validation.

**Updated source sections:** 7.11.0 delta and raw evidence; [[braintree-ios-sdk]]. Prior baseline/history preserved. No substantive cross-company comparison or unresolved contradiction: changes are version-qualified.

**Evidence:** `raw/github/braintree/braintree_ios/releases/braintree-ios/7.11.0/2026-10-04/manifest.json`; `raw/github/braintree/braintree_ios/releases/braintree-ios/7.11.0/2026-10-04/release-notes.md`; `raw/github/braintree/braintree_ios/snapshots/2026-10-04-2a9aa1e/manifest.json`; `tracking/github/repos/braintree/braintree_ios/comparisons/braintree-ios/7.10.0--7.11.0/comparison.json`. Implementation paths in [[source-github-braintree-ios]]. User-approved focused reading; binary/build/payment behavior not tested.


## `braintree-ios@7.10.0` (2026-08-27)

Delta from `braintree-ios@7.9.0` to `braintree-ios@7.10.0`, SHA `eb7f88e8e4ad03fcf79ce5e2926755f7934201d0`, ingested 2026-10-04.

**Changes:** optional campaign IDs on PayPal Checkout and beta Shopper Insights inputs; optional ISO-8601 recommendation expiry string; vaulted Venmo externalID now parsed from details.commonId. SwiftUI demo migration covers Apple Pay, card and iDEAL, with scrollable/intrinsic-height PayPal and Shopper Insights controls.

**Impact and migration:** campaign inputs are opt-in and do not establish eligibility. Applications must handle optional expiry themselves. Venmo vault identity consumers can receive externalID when supplied by the response; it remains optional. No new server transaction or automatic recurring-charge flow. Existing baseline preserved.

**Updated source sections:** 7.10.0 delta, evidence boundaries and raw links; [[braintree-ios-sdk]] campaign/identity section. No substantive cross-provider comparison or contradiction; version-specific additive change.

**Evidence:** `raw/github/braintree/braintree_ios/releases/braintree-ios/7.10.0/2026-10-04/manifest.json`; `raw/github/braintree/braintree_ios/releases/braintree-ios/7.10.0/2026-10-04/release-notes.md`; `raw/github/braintree/braintree_ios/snapshots/2026-10-04-eb7f88e/manifest.json`; `tracking/github/repos/braintree/braintree_ios/comparisons/braintree-ios/7.9.0--7.10.0/comparison.json`. Exact implementation paths in [[source-github-braintree-ios]]. Focused reading approved; no build/runtime test.

## `braintree-ios@7.9.0` (2026-07-21)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree-ios` | Initial baseline | `7.9.0` | `4e987ca19f03b65a0d303b4c3ec95e0c723be971` | Full |

**Exact release change:** BraintreeUIComponents now declares iOS 16 as its minimum deployment target, matching the other modules.

**Developer or merchant impact:** Applications using BraintreeUIComponents must meet the same iOS 16 floor as the rest of the v7 SDK. The release does not introduce a new payment method or transaction flow.

**Migration action:** Treat this as the first exact-SHA baseline. Applications moving from v6 must separately follow the retained v7 guide: adopt iOS 16/Xcode 16.2/Swift 5.10, construct requests through initializers, initialize feature clients with authorization, configure Venmo universal links, update PayPal app-query configuration, and remove PayPal Native Checkout.

**Updated source sections:** Baseline and package structure; authorization and nonce boundary; PayPal; Venmo; Apple Pay; cards and 3DS; additional modules; v7 migration and exact release finding.

**Evidence boundary:** No prior exact-SHA Braintree iOS snapshot exists in the wiki, so this baseline has no comparison manifest. Historical `CHANGELOG.md` entries and `V7_MIGRATION.md` provide cumulative context but are not equivalent to separately retained prior versions.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree_ios/releases/braintree-ios/7.9.0/2026-08-01/manifest.json`
- Release notes: `raw/github/braintree/braintree_ios/releases/braintree-ios/7.9.0/2026-08-01/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/manifest.json`
- Repository changelog: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/CHANGELOG.md`
- v7 migration guide: `raw/github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/files/V7_MIGRATION.md`

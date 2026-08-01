---
title: "GitHub changelog: braintree/braintree_ios"
type: source
date_ingested: 2026-08-01
original_format: github-repo
raw_files:
  - "github/braintree/braintree_ios/snapshots/2026-08-01-4e987ca/manifest.json"
tags: [braintree, ios, mobile-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree_ios`. Cumulative implementation knowledge belongs in [[source-github-braintree-ios]] and the linked immutable snapshot.

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

---
title: "GitHub changelog: braintree/braintree_android"
type: source
date_ingested: 2026-08-01
original_format: github-repo
raw_files:
  - "github/braintree/braintree_android/snapshots/2026-08-01-51f183a/manifest.json"
tags: [braintree, android, mobile-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree_android`. Cumulative implementation knowledge belongs in [[source-github-braintree-android]] and the linked immutable snapshots.

## `braintree-android@5.30.0` (2026-07-21)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree-android` | Initial baseline | `5.30.0` | `51f183a48557d0fd00eefa541712df0c4f21ee28` | Full |

**Important findings:** The release exposes public suspend functions across the principal payment modules, removes the unsupported Visa Checkout module, deprecates the remaining Visa Checkout configuration fields, updates Android build targets, and fixes explicit sizing for PayPal and Venmo buttons.

**Developer or merchant impact:** Kotlin integrations can call the newly public coroutine APIs directly. Integrations must not plan new Visa Checkout work and should remove remaining Visa configuration dependencies before the next major version. Existing PayPal and Venmo UI integrations receive more predictable sizing.

**Migration action:** Treat this as the first exact-SHA baseline. For older v4 or early-v5 applications, follow the retained v5 migration guide's request/result/launcher model and preserve pending redirect requests across app or browser returns. Confirm payment-method enablement separately from SDK availability.

**Updated source sections:** Initial Android architecture; modules and payment surfaces; PayPal; Venmo and vaulting; cards and 3DS; Shopper Insights; exact `5.30.0` findings.

**Evidence boundary:** No prior exact-SHA Braintree Android snapshot exists in the wiki, so this release has no repository comparison manifest. Historical entries in `CHANGELOG.md` and the migration guides provide context but are not equivalent to retained version snapshots.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree_android/releases/braintree-android/5.30.0/2026-08-01/manifest.json`
- Release notes: `raw/github/braintree/braintree_android/releases/braintree-android/5.30.0/2026-08-01/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/manifest.json`
- Repository changelog: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/CHANGELOG.md`
- v5 migration guide: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/v5_MIGRATION_GUIDE.md`
- PayPal/Venmo button sizing: `raw/github/braintree/braintree_android/snapshots/2026-08-01-51f183a/files/UIComponents/`

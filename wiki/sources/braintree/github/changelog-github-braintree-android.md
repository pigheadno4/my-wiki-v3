---
title: "GitHub changelog: braintree/braintree_android"
type: source
date_ingested: 2026-10-04
original_format: github-repo
raw_files:
  - "github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/manifest.json"
  - "github/braintree/braintree_android/snapshots/2026-10-04-2695a48/manifest.json"
  - "github/braintree/braintree_android/snapshots/2026-10-04-438d33a/manifest.json"
  - "github/braintree/braintree_android/snapshots/2026-08-01-51f183a/manifest.json"
tags: [braintree, android, mobile-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree_android`. Cumulative implementation knowledge belongs in [[source-github-braintree-android]] and the linked immutable snapshots.

## `braintree-android@5.33.0` (2026-09-16)

Delta from `braintree-android@5.32.0` to `braintree-android@5.33.0`; SHA `04b82bbb1cb49e3a5ad44bac920704ba03c99317`; ingested 2026-10-04.

**Changes:** Compose CardFields plus remembered controller, shared validation state, formatting, focus advancement, accessibility/error presentation and CVV hint/momentary masking. The merchant's submit button invokes CardClient tokenization through the controller, which merges entered fields with optional Card data and returns a nonce or failure. README adds a sample; retained build changes add test dependencies and release metadata.

**Impact and migration:** install UIComponents, create a controller with actual authorization, render CardFields and gate submit with isFormValid. submit has no validation/in-flight guard and does not clear fields. Number/expiration/CVV use saveable TextFieldValue state; masking is not secure-storage proof. Default ViewModel ownership does not establish independent state for multiple forms. Send the nonce to the server; this is not transaction completion, 3DS, vault activation or Drop-in compatibility evidence. Platform targets unchanged; excluded catalog changes and the older Browser Switch mismatch remain unresolved. No Android build/UI/payment test.

**Updated source sections:** additive 5.33.0 Compose integration, validation/display, submit/saved-state caveats and evidence limits; Android concept/company/index. All previous release sections preserved; no cross-company comparison warranted.

**Evidence:** `raw/github/braintree/braintree_android/releases/braintree-android/5.33.0/2026-10-04/manifest.json`; `raw/github/braintree/braintree_android/releases/braintree-android/5.33.0/2026-10-04/release-notes.md`; `raw/github/braintree/braintree_android/snapshots/2026-10-04-04b82bb/manifest.json`; `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.32.0--5.33.0/comparison.json` and `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.32.0--5.33.0/diff.patch`. Exact implementation paths in [[source-github-braintree-android]]. User-approved focused reading; all raw and older knowledge retained.

## `braintree-android@5.32.0` (2026-08-27)

Delta from `braintree-android@5.31.0` to `braintree-android@5.32.0`; SHA `2695a481d8cd56a3d6db379297e6682663d2c94e`; ingested 2026-10-04.

**Changes:** optional checkout campaigns and beta Shopper Insights session campaigns; explicit first-GraphQL-error handling for sessions and recommendations; nullable recommendation expiresAt; commonId fallback for vaulted Venmo nonce externalId; public registry/lifecycle/context GooglePayLauncher constructor. Deep-link fallback KDoc is clarified; build/docs examples and Dokka output change.

**Impact and migration:** campaign IDs associate requests, not campaign provisioning or eligibility. Handle public Failure results and recommendation staleness explicitly; expiry is a string, not enforced/refreshed by the SDK. Venmo payerInfo can still overwrite commonId, so a nonempty externalId is not guaranteed. Observe Google Pay constructor/launch lifecycle requirements. Scheme guidance is documentation, not a new runtime validator. Android API 23/Java 11 and compile/target API 37 remain; the prior Browser Switch discrepancy remains unresolved. No SDK build or payment test.

**Updated source sections:** additive 5.32.0 campaigns, error/expiry handling, Venmo identity, Google Pay constructor and documentation boundaries; concept/company/index. Preserved all earlier history; no cross-company comparison warranted.

**Evidence:** `raw/github/braintree/braintree_android/releases/braintree-android/5.32.0/2026-10-04/manifest.json`; `raw/github/braintree/braintree_android/releases/braintree-android/5.32.0/2026-10-04/release-notes.md`; `raw/github/braintree/braintree_android/snapshots/2026-10-04-2695a48/manifest.json`; `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.31.0--5.32.0/comparison.json` and `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.31.0--5.32.0/diff.patch`. Exact implementation paths in [[source-github-braintree-android]]. User-approved focused reading; all raw and older knowledge retained.

## `braintree-android@5.31.0` (2026-08-03)

Delta from `braintree-android@5.30.0` to `braintree-android@5.31.0`; SHA `438d33ac42c92ca7489c3fec3b45d088a75a8361`; ingested 2026-10-04.

**Changes:** shared PayPal Checkout/Vault authorization request adds device model and available/total memory under app_switch_context.device_info when app switch passes installed-app/resolution checks and an app-link return URL exists. Missing ActivityManager preserves the base request. The memory values are integer byte counts divided by 1024 squared; device data is automatically populated, not a new merchant request input.

**Impact and migration:** retained source shows additional outgoing device context, not guaranteed app-switch eligibility or a new transaction flow. The new helper does not consult hasUserLocationConsent; separate DataCollector consent handling is unchanged. Android API 23/Java 11 requirements and API 37 compile/target remain. Inspect actual dependency resolution and app behavior separately; no build/payment test.

> [!warning] Contradiction
> Release notes report Browser Switch 3.6.0; retained DEPENDENCIES.md still lists 3.5.1. The build uses a version-catalog alias whose catalog is outside the capsule. Resolved version and dependency internals remain unverified; both authorities are retained in [[source-github-braintree-android]] and [[braintree-android-sdk]].

**Updated source sections:** 5.31.0 delta, capsule-scope correction and raw evidence; Android concept/company/index. Preserved 5.30.0 baseline; no cross-company comparison warranted.

**Evidence:** `raw/github/braintree/braintree_android/releases/braintree-android/5.31.0/2026-10-04/manifest.json`; `raw/github/braintree/braintree_android/releases/braintree-android/5.31.0/2026-10-04/release-notes.md`; `raw/github/braintree/braintree_android/snapshots/2026-10-04-438d33a/manifest.json`; `tracking/github/repos/braintree/braintree_android/comparisons/braintree-android/5.30.0--5.31.0/comparison.json`. Exact implementation/documentation paths in [[source-github-braintree-android]]. User-approved focused reading; full raw evidence preserved.

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

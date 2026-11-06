---
title: "GitHub changelog: Adyen/adyen-android"
type: source
date_ingested: 2026-08-01
date_updated: 2026-11-07
original_format: github-repo
raw_files:
  - "github/adyen/adyen-android/snapshots/2026-11-07-73df655/manifest.json"
  - "github/adyen/adyen-android/snapshots/2026-11-07-405b582/manifest.json"
  - "github/adyen/adyen-android/supplements/2026-11-07-405b582-93095740/manifest.json"
  - "github/adyen/adyen-android/snapshots/2026-08-01-5314fad/manifest.json"
tags: [adyen, android, kotlin, mobile-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-android`. Cumulative implementation knowledge belongs in [[source-github-adyen-android]] and the linked immutable snapshots.

## `adyen-android@5.20.0` (2026-07-30)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `adyen-android` | Initial baseline | `5.20.0` | `5314fad1389a8def9d8e3377f27f7405e303faba` | Full |

**Important finding:** The release raises both the compile SDK and target SDK versions to Android API 36.

**Developer or merchant impact:** Consumers need an Android build toolchain and application configuration compatible with API 36. The retained release note does not claim a payment API, checkout behavior, or merchant-facing feature change.

**Migration action:** Verify build compatibility and run the merchant application's Android regression suite after updating. No SDK API migration or breaking change is documented.

**Updated source sections:** Platform, distribution, and lifecycle; `5.20.0` release finding.

Broader Drop-in, Session, Component, card, action, wallet, analytics, and payment-method behavior is the initial cumulative baseline, not release-specific change evidence.

### Evidence

- `raw/github/adyen/adyen-android/releases/adyen-android/5.20.0/2026-08-01/manifest.json`
- `raw/github/adyen/adyen-android/releases/adyen-android/5.20.0/2026-08-01/release-notes.md`
- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/manifest.json`
- `raw/github/adyen/adyen-android/snapshots/2026-08-01-5314fad/files/gradle/libs.versions.toml`

## `adyen-android@5.21.0` (2026-10-27)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `adyen-android` | `5.20.0` | `5.21.0` | `405b582a7b2060aceac756eae7b6bd3757e0c084` | Full additive; focused reading approved |

Ingested 2026-11-07 as `github-7ed8658609166ae83227`. Full overrides the script's delta recommendation to give the broad build migration explicit treatment; all `5.20.0` knowledge remains.

**Important findings:** CardView restores the store-payment-details switch from output state after address lookup. Native redirect submission/serialization reports non-cancellation failures through the error channel, wrapping non-CheckoutException errors. Adyen 3DS2 advances `2.2.27` -> `2.2.28`; Kotlin/AGP catalog pins advance to `2.3.21` / `9.4.1`; AndroidX/Compose/Coroutines also update. Card/BACS examples adopt dispatcher-based back handling.

**Compatibility boundary:** The exact-SHA supplement proves Android Java source/target **11**, distinct from catalog/tooling target **17**, and upstream Gradle wrapper `9.8.0`. Compile/min catalog values remain 36/21. Retrofit `3.0.0` belongs to the example-app dependency, not an established SDK-core networking rewrite. Convention plugins configure API-validation workarounds; their configuration is not a successful build/test or evidence that all generated dump churn removes authored APIs.

**Migration action:** Regression-test address lookup/store choice and redirect failure callbacks; verify consuming-app build and dependency compatibility. Delegated 3DS2 internals, consumer minimum JDK and universal binary compatibility are not established by this capsule. No Android build, device or payment execution.

**Updated source sections:** New `adyen-android@5.21.0` full additive findings, migration table and exact build-supplement links; Android SDK concept, company, provider catalog and logs. No source-count increment.

### Evidence

- `raw/github/adyen/adyen-android/releases/adyen-android/5.21.0/2026-11-07/manifest.json`
- `raw/github/adyen/adyen-android/releases/adyen-android/5.21.0/2026-11-07/release-notes.md`
- `raw/github/adyen/adyen-android/snapshots/2026-11-07-405b582/manifest.json`
- `tracking/github/repos/adyen/adyen-android/comparisons/adyen-android/5.20.0--5.21.0/comparison.json`
- `tracking/github/repos/adyen/adyen-android/comparisons/adyen-android/5.20.0--5.21.0/comparison.md`
- `tracking/github/repos/adyen/adyen-android/comparisons/adyen-android/5.20.0--5.21.0/diff.patch`
- `raw/github/adyen/adyen-android/supplements/2026-11-07-405b582-93095740/manifest.json`
- `tracking/github/repos/adyen/adyen-android/evidence-attachments/github-7ed8658609166ae83227/attachment.json`
- Exact card/redirect/catalog/example and all five supplemental file locators: [[source-github-adyen-android]].

## `adyen-android@5.22.0` (2026-10-30)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `adyen-android` | `5.21.0` | `5.22.0` | `73df6558fa5868a2c14449ac2e0c6379fc349798` | Full additive; focused reading approved |

Ingested 2026-11-07 as `github-a2920dfadabf8c5faa3b`, after completing `5.21.0`. Security-impact full mode remains full despite only three retained files changing; all previous histories are preserved.

**Important findings:** Upstream release notes state that eight compromised eMudhra intermediate CAs are blocked on devices without Google Play services; Play-services devices had already received Google's automatic protection. Retained source establishes OkHttp/logging `4.12.0` -> `4.12.1` and moving URL image saving onto the existing shared cached OkHttp image loader, not the dependency's actual blocklist contents or verified certificate rejection.

**Implementation impact:** Image load errors now wrap as `CheckoutException("Failed to load image", error)`, separately from malformed URLs. Bitmap recycling moves out of the common save helper and into the path that created a bitmap from a View, avoiding that recycling operation on loader-provided cached bitmaps. No new public payment API or comprehensive resource/cancellation guarantee is demonstrated.

**Migration action:** Review the security release and resolved dependencies, then exercise download/save failures and cached-image reuse on relevant devices. No Android build, device/certificate or payment execution was performed. Earlier Java/build-tooling and delegated SDK facts remain explicitly version-qualified; the supplement is still only exact-5.21.0 evidence.

**Updated source sections:** New `adyen-android@5.22.0` full additive security/image findings, latest pointer and exact raw links; Android SDK concept, company/catalog/logs. No source-count increment.

### Evidence

- `raw/github/adyen/adyen-android/releases/adyen-android/5.22.0/2026-11-07/manifest.json`
- `raw/github/adyen/adyen-android/releases/adyen-android/5.22.0/2026-11-07/release-notes.md`
- `raw/github/adyen/adyen-android/snapshots/2026-11-07-73df655/manifest.json`
- `tracking/github/repos/adyen/adyen-android/comparisons/adyen-android/5.21.0--5.22.0/comparison.json`
- `tracking/github/repos/adyen/adyen-android/comparisons/adyen-android/5.21.0--5.22.0/comparison.md`
- `tracking/github/repos/adyen/adyen-android/comparisons/adyen-android/5.21.0--5.22.0/diff.patch`
- Exact catalog, image-saving, shared loader and HTTP factory file locators: [[source-github-adyen-android]].

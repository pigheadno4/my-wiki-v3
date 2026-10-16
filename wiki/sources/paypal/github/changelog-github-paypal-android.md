---
title: "GitHub changelog: paypal/paypal-android"
type: source
date_ingested: 2026-07-31
date_updated: 2026-10-16
original_format: github-repo
raw_files:
  - "github/paypal/paypal-android/snapshots/2026-10-16-d100313/manifest.json"
  - "github/paypal/paypal-android/snapshots/2026-10-16-3540adf/manifest.json"
  - "github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/manifest.json"
  - "github-paypal-android.md"
tags: [paypal, android, kotlin, mobile, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `paypal/paypal-android`. Durable architecture and integration guidance belongs in [[source-github-paypal-android]].

## `paypal-android@3.1.0` - Serial Delta (2026-10-16)

| Package | From | To | Published | Exact SHA | Mode |
| --- | --- | --- | --- | --- | --- |
| `paypal-android` | `3.0.0` | `3.1.0` | 2026-10-06 | `d100313f2247b512cedf6080bb7b6ecaada26d42` | Delta |

Collected and ingested 2026-10-16; changelog date 2026-10-05 differs from GitHub publication. Retained comparison: 17 modified, one removed, 260 unchanged; no added file. This is capsule scope, not an exhaustive upstream repository comparison.

**Release-note changes:** make the required `TokenType` accessible to external integrations and replace the embedded Magnes JAR to avoid collisions with other PayPal SDKs. Source confirms removal of the enum's library-group annotation, addition to `CorePayments.api`, and relocation of Magnes imports. Binary coexistence has not been tested and the JAR is not retained.

**Additional source findings:** optional BN code now flows from CoreConfig through shopper-session params into experimentation context. The demo adds BN-code settings UI, initializes/stores its card-vault client before use, and removes order-level user action while retaining `createPayPalSession` user action. The null-client demo defect documented at `3.0.0` is therefore resolved at this exact SHA. Excluded custom-environment repository/variant wiring prevents proving the settings UI's full persistence/consumption path.

**Migration and impact:** integrations needing the session token enum should use this corrected API rather than copying restricted `3.0.0` declarations; direct `CoreConfig.bnCode` now participates in session eligibility. Keep session prewarming, finish handling and server order/token finalization. The return-routing discrepancy and LSAT-header caution remain; no new Venmo support or merchant eligibility is established.

**Updated sections:** new source delta and dated resolution facts, Android/Vault concepts, company, catalog and logs. All changed retained source and affected prior code read fully, with generated inventories and duplicated diff mechanically verified under explicit per-release approval; previous histories remain intact. No cross-company comparison needed, upstream execution, commit or push.

**Evidence:**
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-d100313/manifest.json`
- `raw/github/paypal/paypal-android/releases/paypal-android/3.1.0/2026-10-16/manifest.json`
- `raw/github/paypal/paypal-android/releases/paypal-android/3.1.0/2026-10-16/release-notes.md`
- `tracking/github/repos/paypal/paypal-android/comparisons/paypal-android/3.0.0--3.1.0/comparison.json`
- Exact implementation paths and excerpts: [[source-github-paypal-android]].

## `paypal-android@3.0.0` - Additive Full Ingest (2026-10-16)

| Package | From | To | Published | Exact SHA | Mode |
| --- | --- | --- | --- | --- | --- |
| `paypal-android` | `2.3.0` | `3.0.0` | 2026-08-19 | `3540adff974abdc20371d66fe47748e4c5174592` | Full |

Collected and ingested 2026-10-16. The upstream changelog labels the release 2026-08-18, one day before GitHub publication. Comparison: 63 added, 64 modified, 27 removed, one renamed and 150 unchanged retained files; policy changes mean these are capsule counts, not the entire upstream diff.

**New contract:** `paypal-web-payments` / `PayPalWebCheckoutClient` become `paypal-payments` / `PayPalClient`; `CoreEnvironment` replaces `Environment`. Prewarm a shopper session before checkout or vault, then use ID-based `start` / `vault` with `PayPalResultCallback`, resolve the return with finish methods, and finalize server-side. App switch combines server eligibility with local installed-app/routing checks and a browser fallback URL.

**Breaking changes:** `CoreConfig` requires a merchant ID alongside the client ID; request objects and deprecated synchronous/explicit-auth-state overloads are removed; phone identity is structured. Fraud collection removes old overloads and logging configuration. Card/PayPal result presentation no longer exposes auth state.

**Important findings:** prewarming is consumed per attempt and is not restored by `instanceState`; `TokenType` remains library-group restricted despite the public required parameter; fallback-scheme validation and final signatures differ from release-note migration wording; the card-vault demo leaves its nullable client uninitialized. LSAT request headers also differ between the API request and RestClient construction, without a reproduced provider failure. Native Venmo is still not established.

**Migration:** change artifact/imports/config enum, configure return routes and prewarm for every attempt; preserve return handling and server-owned finalization. Do not copy obsolete native/v2 migration examples or the card-vault demo's null-client wiring. This full ingest adds version-qualified knowledge and preserves every older baseline, not a latest-only rewrite.

**Updated sections:** source v3 integration/session/routing/cards/fraud/cautions, Android and Vault concepts, company/catalog/logs. No cross-company comparison warranted. All 278 retained files, assigned prior files and notes read fully; generated inventories/diff mechanically verified under the explicit one-time exception. Variant source sets, session GraphQL resource and Magnes binary remain outside this capsule; no build or live payment proof.

**Evidence:**
- `raw/github/paypal/paypal-android/snapshots/2026-10-16-3540adf/manifest.json`
- `raw/github/paypal/paypal-android/releases/paypal-android/3.0.0/2026-10-16/manifest.json`
- `raw/github/paypal/paypal-android/releases/paypal-android/3.0.0/2026-10-16/release-notes.md`
- `tracking/github/repos/paypal/paypal-android/comparisons/paypal-android/2.3.0--3.0.0/comparison.json`
- Exact implementation paths and grounding excerpts: [[source-github-paypal-android]].

## `paypal-android@2.3.0` - Change Set `d69a2fa` (2025-11-03)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `paypal-android` | Legacy retained 1.x-era context | `2.3.0` | 2025-11-03 | `d69a2fad7a96155e71f2681dc7cbfa9957fff544` | Full |

**Exact release change:** `PayPalWebCheckoutClient.start(activity, request, callback)` adds asynchronous callback support. The synchronous `start(activity, request)` overload is deprecated.

**Developer or merchant impact:** checkout launch now performs client-configuration work off the caller path and reports the browser-presentation result through `PayPalWebStartCallback` on the main dispatcher. Existing integrations should migrate the launch call while retaining their `finishStart(intent)` deep-link handling and server capture or authorization.

**Migration action:** replace calls expecting an immediate presentation result with the callback overload. Handle `PayPalPresentAuthChallengeResult.Success` or `Failure` inside the callback, then continue to resolve the returning intent with `finishStart(intent)`.

**Updated source sections:** evidence boundary; package status; modules; v2 lifecycle; cards and 3DS; card and PayPal vaulting; `2.3.0` checkout launch; Venmo boundary; buttons; fraud protection; historical v1 context; Android SDK and Vault concepts; PayPal company and provider indexes.

**Evidence boundary:** no automated comparison exists between the legacy manually selected SHA and `2.3.0`. The callback overload is the exact `2.3.0` change; the v2 lifecycle and other module behavior are cumulative baseline context.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-android/releases/paypal-android/2.3.0/2026-07-31/manifest.json`
- Release notes: `raw/github/paypal/paypal-android/releases/paypal-android/2.3.0/2026-07-31/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/manifest.json`
- Checkout client: `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/PayPalWebPayments/src/main/java/com/paypal/android/paypalwebpayments/PayPalWebCheckoutClient.kt`
- Cumulative upstream history: `raw/github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/files/CHANGELOG.md`

## `paypal-android@2.2.0` - Accumulated Context (2025-10-01)

Card and PayPal browser-presentation methods moved from `ComponentActivity` to plain `Activity`. The release also restored public visibility for `PayPalPresentAuthChallengeResult.authState` after an accidental breaking change.

This is cumulative changelog context, not a separately collected `2.2.0` release capsule.

## `paypal-android@2.1.2` - Accumulated Context (2025-09-26)

Card and PayPal clients added `instanceState` and `restore()`, plus finish methods that use internally retained auth state. Older finish overloads requiring an explicit auth-state string were deprecated. Releases `2.1.0` and `2.1.1` are marked unsupported upstream.

This is cumulative changelog context, not a separately collected `2.1.2` release capsule.

## `paypal-android@2.0.1` - Accumulated Context (2025-09-24)

PayPal checkout explicit cancellation was corrected from `Failure` to `Canceled`, and PayPal vault explicit cancellation was corrected from `Success` to `Canceled`.

This is cumulative changelog context, not a separately collected `2.0.1` release capsule.

## `paypal-android@2.0.0` - Accumulated Major-Version Context (2025-03-18)

Version 2 removed `PayPalNativePayments`, replaced card listeners with callback result types, introduced explicit card authorization-challenge presentation and finish methods, removed PayPal web listeners, and introduced explicit PayPal checkout/vault finish result types. It also moved to Java 17, Kotlin 1.9.24, and Android Gradle Plugin 8.7.1 at that release point.

This context comes from the collected `2.3.0` cumulative changelog and migration guide; it is not a separately collected `2.0.0` release capsule.

## Historical Reviewed Context (2026-04-13 review)

The earlier SHA `2685f88374fa09c17e5af6f3ea88ba622d940901` established the version 1 listener-based Card and PayPal Web flows, `CardClient(Context, CoreConfig)`, instance-state recovery, merchant-server orchestration, and the absence of Venmo from `PayPalWebCheckoutFundingSource`. Those findings remain explicitly versioned history.

**Evidence:**

- Legacy capsule pointer: `raw/github-paypal-android.md`
- Legacy retained files: `raw/github-paypal-android/`

---
title: "GitHub changelog: Adyen/adyen-react-native"
type: source
date_ingested: 2026-10-04
date_updated: 2026-10-21
original_format: github-repo
raw_files:
  - "github/adyen/adyen-react-native/releases/react-native/2.13.0/2026-10-21/manifest.json"
  - "github/adyen/adyen-react-native/snapshots/2026-10-21-68acfa3/manifest.json"
  - "github/adyen/adyen-react-native/releases/react-native/2.12.0/2026-10-04/manifest.json"
  - "github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/manifest.json"
tags: [adyen, react-native, mobile-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-react-native`. Cumulative implementation knowledge belongs in [[source-github-adyen-react-native]] and the linked immutable evidence.

## `@adyen/react-native@2.13.0` (2026-10-16)

| Package | From | To | Exact SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@adyen/react-native` | `@adyen/react-native@2.12.0` | `@adyen/react-native@2.13.0` | `68acfa3ab6976482fd4f9e3a0c075eb649b75d70` | Delta, approved focused reading |

**Ingested:** 2026-10-21. All historical `2.12.0` knowledge and both dated release-note records remain preserved.

**Features/fixes:** Android-only optional Google Pay `merchantInfo` (`merchantName`, Google-issued `merchantId`); public export of the existing `ApplePayAuthorizationResult` type; iOS recursive view search and embedded CardView safe-area fixes. JavaScript package import now forwards its version to native analytics instead of native build-time placeholders; this is not a native dependency selector or a new merchant-facing configuration API.

**Dependencies/build:** Android native `5.19.0` -> `5.20.0`; iOS native `5.25.1` -> `5.26.0`. Android library defaults compile 35 -> 36, target 34 -> 36, with consuming-project overrides still authoritative. React Native peer requirement stays `>=0.76.0`, optional Expo `>=52`. The native CocoaPods sunset notice does not establish wrapper SPM support: its README/podspec still use CocoaPods. UPI Smart Intent already appeared in the older wrapper note and is not newly attributed to this release.

**Additional implementation:** Example API/configuration providers are injected, including a Netlify demo backend client and read-only external card settings. Stored-method removal moves into AdvancedCheckout. The Netlify client throws for stored-method removal, balance/order operations and Session-result lookup; Sessions demos bypass their extra lookup in direct-result mode. The direct client still places its API key on-device. These demo paths do not change the server-side credential/verification requirement or prove payment success. The example also stops forcing card address lookup when the setting is absent. Contributor docs/package metadata introduce public TypeScript API reporting, but the generated report/build script and CI are excluded from this capsule. Android 3DS2 version retrieval becomes lazy; ActionFragment property visibility changes are internal, not a new payment feature.

**Migration/testing:** Optional Google Pay settings do not replace registration or Adyen merchant-account selection. Import the Apple Pay result type from the package instead of an internal path. Review consuming Android API-level settings; regression-test both wallets, redirects/actions and iOS embedded cards near the bottom safe area. Do not copy demo credentials, hardcoded stored-card CVV or direct callback fulfillment into production. No SDK build, device or payment execution was performed.

**Evidence/read scope:** Current/prior capsules have 305/301 files: six added, 43 modified, two deleted, 256 unchanged. All 606 file sizes/SHA-256/Git blob IDs and packet/comparison hashes checked. User approved mechanical verification of generated inventories/duplicated diff while changed retained source, notes, affected prior code and cumulative wiki pages were read fully. No evidence gaps or unclassified changes in the packet; tests/CI/generated build output remain outside the reviewed capsule. Updated existing concept first, cumulative source/changelog, company, index and logs; source count unchanged.

### `2.13.0` evidence

- [Release identity](../../../../raw/github/adyen/adyen-react-native/releases/react-native/2.13.0/2026-10-21/manifest.json) and [[raw/github/adyen/adyen-react-native/releases/react-native/2.13.0/2026-10-21/release-notes|release notes]]
- [Exact-SHA snapshot](../../../../raw/github/adyen/adyen-react-native/snapshots/2026-10-21-68acfa3/manifest.json)
- [Comparison](../../../../tracking/github/repos/adyen/adyen-react-native/comparisons/react-native/2.12.0--2.13.0/comparison.json) and [retained patch](../../../../tracking/github/repos/adyen/adyen-react-native/comparisons/react-native/2.12.0--2.13.0/diff.patch)
- [[source-github-adyen-react-native]] - implementation links, code examples, grounding excerpts and historical knowledge

## `@adyen/react-native@2.12.0` note revision (collected 2026-10-04)

**Ingest mode:** Documentation-only delta. Release identity and SHA remain `@adyen/react-native@2.12.0` at `2912c913266b2d1df73882980303b563ea04ab63`; the original release date remains 2026-07-13.

**Difference from the 2026-08-01 note:** Added a dependency table with native release links for Android `5.19.0` and iOS `5.25.1`; bolded those versions in existing bullets. No feature or dependency-version changes. All 301 retained source files are unchanged; no new source snapshot is needed.

**Merchant/developer impact:** No integration or migration action follows from this note revision. Native dependency boundaries and all historical implementation findings remain unchanged in [[source-github-adyen-react-native]].

### Revision evidence

- `raw/github/adyen/adyen-react-native/releases/react-native/2.12.0/2026-10-04/manifest.json`
- `raw/github/adyen/adyen-react-native/releases/react-native/2.12.0/2026-10-04/release-notes.md`
- Prior note: `raw/github/adyen/adyen-react-native/releases/react-native/2.12.0/2026-08-01/release-notes.md`
- Unchanged snapshot: `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/manifest.json`

## `@adyen/react-native@2.12.0` (2026-07-13)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@adyen/react-native` | Initial baseline | `2.12.0` | `2912c913266b2d1df73882980303b563ea04ab63` | Full |

**Important changes:** Standalone PayByBank and Apple Pay `merchantCapabilities` were added. Sessions instant payments became more reliable. Android fixes cover Twint storage-field parity, Google Pay and instant payments across device rotation, and blocking dismissal of an active-payment screen. iOS fixes an embedded CardView dismissal crash.

**Dependency changes:** Adyen Android moved to `5.19.0`, Adyen iOS to `5.25.1`, and the repository development baseline to React Native `0.85`. The note attributes UPI Smart Intent on both platforms and Bizum instant payments on iOS to the native SDK updates.

**Developer or merchant impact:** Integrations can offer standalone PayByBank where backend and merchant eligibility permit, restrict Apple Pay sheet card capabilities to debit or credit, and receive lifecycle fixes on both native platforms. Every consumer should regression-test Sessions, device rotation, active-payment dismissal, and embedded CardView cleanup because the wrapper and both delegated native SDK baselines changed.

**Migration action:** No breaking API migration is documented. Review Apple Pay capability configuration, verify redirect and lifecycle setup, and test against Adyen Android `5.19.0` and Adyen iOS `5.25.1` rather than assuming behavior from newer native releases.

**Updated source sections:** package and platform status; integration modes and server boundary; architecture and lifecycle; Components and actions; wallets; native dependency boundary; exact release finding; integration guidance.

**Evidence boundary:** This is the first retained exact-SHA baseline, so there is no prior immutable snapshot for an automated source diff. Only the upstream release-note items are attributed specifically to `2.12.0`; broader SDK behavior is cumulative implementation evidence at the same SHA. The tagged tree's local package-version placeholder is not treated as the package release identity.

### Evidence

- `raw/github/adyen/adyen-react-native/releases/react-native/2.12.0/2026-08-01/manifest.json`
- `raw/github/adyen/adyen-react-native/releases/react-native/2.12.0/2026-08-01/release-notes.md`
- `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/manifest.json`
- `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/package.json`
- `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/adyen-react-native.podspec`
- `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/android/dependencies.gradle`
- `raw/github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/files/docs/Architecture.md`

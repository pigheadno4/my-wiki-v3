---
title: "GitHub changelog: paypal/paypal-android"
type: source
date_ingested: 2026-07-31
date_updated: 2026-07-31
original_format: github-repo
raw_files:
  - "github/paypal/paypal-android/snapshots/2026-07-31-d69a2fa/manifest.json"
  - "github-paypal-android.md"
tags: [paypal, android, kotlin, mobile, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `paypal/paypal-android`. Durable architecture and integration guidance belongs in [[source-github-paypal-android]].

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

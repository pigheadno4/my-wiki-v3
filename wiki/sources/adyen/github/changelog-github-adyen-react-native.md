---
title: "GitHub changelog: Adyen/adyen-react-native"
type: source
date_ingested: 2026-08-02
original_format: github-repo
raw_files:
  - "github/adyen/adyen-react-native/snapshots/2026-08-01-2912c91/manifest.json"
tags: [adyen, react-native, mobile-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-react-native`. Cumulative implementation knowledge belongs in [[source-github-adyen-react-native]] and the linked immutable evidence.

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

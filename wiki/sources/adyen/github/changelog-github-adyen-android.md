---
title: "GitHub changelog: Adyen/adyen-android"
type: source
date_ingested: 2026-08-01
original_format: github-repo
raw_files:
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

---
title: "GitHub changelog: Adyen/adyen-ios"
type: source
date_ingested: 2026-08-01
original_format: github-repo
raw_files:
  - "github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/manifest.json"
tags: [adyen, ios, swift, mobile-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-ios`. Cumulative implementation knowledge belongs in [[source-github-adyen-ios]] and the linked immutable snapshots.

## `adyen-ios@5.25.1` (2026-06-04)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `adyen-ios` | Initial baseline | `5.25.1` | `5f6779b31299e3067de3a5279a816f3b8d2fbdf3` | Full |

**Important finding:** The release fixes a layout issue that could affect Component form rendering when Adyen iOS is embedded through a cross-platform SDK.

**Developer or merchant impact:** React Native or Flutter wrapper integrations may receive corrected native form sizing or presentation. The release note does not identify a specific form or source file, so narrower claims are not supported by this baseline.

**Migration action:** No API migration or breaking change is documented. Wrapper integrations should regression-test their native Component forms after updating.

**Updated source sections:** platform and distribution; context and integration modes; Session and advanced flow; cards and storage; Apple Pay and actions; native app handoffs; analytics, privacy, and cross-platform wrappers.

**Evidence boundary:** This is the first retained Adyen iOS baseline, so no prior exact-SHA comparison exists. The layout fix comes from the upstream release note; broader SDK architecture comes from the complete retained source capsule at the same SHA.

**Evidence:**

- Release manifest: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.25.1/2026-08-01/manifest.json`
- Release notes: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.25.1/2026-08-01/release-notes.md`
- Snapshot manifest: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/manifest.json`
- Cross-platform identity: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/Adyen/Helpers/CheckoutPlatformParams.swift`
- Form infrastructure: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/Adyen/UI/Form/`

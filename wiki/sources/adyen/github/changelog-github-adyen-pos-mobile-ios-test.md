---
title: "GitHub changelog: adyen/adyen-pos-mobile-ios-test"
type: source
date_ingested: 2026-10-30
date_updated: 2026-10-30
original_format: github-repo
raw_files:
  - "github/adyen/adyen-pos-mobile-ios-test/snapshots/2026-10-30-5e22343/manifest.json"
tags: [adyen, mobile-pos, ios, test-environment, release-history, github-repository]
---

## Overview

Independent repository-qualified history for `adyen/adyen-pos-mobile-ios-test`. Durable facts belong to [[source-github-adyen-pos-mobile-ios-test]]. Do not merge this TEST-only distribution's history with the main repository merely because both publish AdyenPOS. Future full/delta ingests append knowledge and preserve all older baselines.

## Initial Baseline: `AdyenPOS@3.22.0` (2026-10-27)

- **Identity:** repository adyen/adyen-pos-mobile-ios-test; tag v3.22.0; SHA `5e2234351d6164f11911d09efed4630fe82e0050`; collected and ingested 2026-10-30.
- **Mode/read:** approved full; all 30 assigned paths and both packet files read completely, no exception. Capsule contains 27 files, seven sample Swift files and 51,055 bytes. No prior collected baseline/comparison exists; sample architecture is not described as introduced in this release.
- **Baseline:** TEST-only binary products, shared PaymentService/Terminal API model, tapToPay/cardReader selection, SwiftUI transactionModal versus UIKit presentation, and built-in reader management. TerminalAPIKit resolution records 1.3.0, not dependency implementation evidence.
- **Release announcements:** ten added languages, OS-language fallback, iOS 26 close-button consistency, primary-language/initial-flash fixes; Xcode 26.3 and NYC1 PIN support expiry 2027-04-13. Binary internals were not audited and expiry is not generalized.
- **Integration cautions:** comments require setupToken forwarding but code omits it, uses a placeholder backend and ignores HTTP status. Warm-up failure is suppressed and results only printed. Entitlement presence is not provisioning proof; README still links 3.21.0 docs.
- **Independent configuration:** SwiftUI adds Bluetooth/camera descriptions with no target deployment override over project 17.0; UIKit explicitly targets 18.4. The main repo instead explicitly targets 18.4 in all four target configurations. Seven sample Swift files match across collected repositories, but four other files differ; this is not a version delta or binary-runtime equivalence proof.
- **Updated sections:** existing Mobile POS concept first, reciprocal contradiction warning, independent source/changelog, company/repository-qualified release counts, provider catalog and logs. No new concept or cross-company comparison; main and website histories preserved.
- **Execution boundary:** no SDK/dependency download, build, credentials, provisioning, device/API/payment execution, commit or push.

## Raw Sources

- [Snapshot and retained-file inventory](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/snapshots/2026-10-30-5e22343/manifest.json)
- [Release identity](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/releases/adyenpos/3.22.0/2026-10-30/manifest.json)
- [Release announcements](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/releases/adyenpos/3.22.0/2026-10-30/release-notes.md)
- [Shared model](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/snapshots/2026-10-30-5e22343/files/POSSampleApp/SampleAppSwiftUI/MainViewModel.swift)

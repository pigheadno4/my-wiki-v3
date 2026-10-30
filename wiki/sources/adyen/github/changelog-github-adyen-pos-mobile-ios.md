---
title: "GitHub changelog: adyen/adyen-pos-mobile-ios"
type: source
date_ingested: 2026-10-30
date_updated: 2026-10-30
original_format: github-repo
raw_files:
  - "github/adyen/adyen-pos-mobile-ios/snapshots/2026-10-30-689bdbd/manifest.json"
tags: [adyen, mobile-pos, ios, terminal-api, release-history, github-repository]
---

## Overview

Package-qualified repository history for `adyen/adyen-pos-mobile-ios`. Durable integration details and evidence limits belong to [[source-github-adyen-pos-mobile-ios]]. Keep SDK binary, sample code, external TerminalAPIKit dependency and separately dated website histories distinct. Future full/delta ingests append knowledge without removing older versions.

## Initial Baseline: `AdyenPOS@3.22.0` (2026-10-27)

- **Identity:** tag v3.22.0; SHA `689bdbdd7197545fbf15160ea64461a53b02b432`; collected and ingested 2026-10-30.
- **Mode/read:** approved full, all 30 assigned paths read end to end, including every retained file and generated manifest; no focused-reading exception. The 27-file capsule contains seven Swift files and 50,860 bytes. No prior collected release or comparison exists; baseline sample architecture is not described as introduced by this release.
- **Baseline:** TEST/LIVE binary manifests; shared PaymentService/Terminal API transaction model; SwiftUI viewModifier/transactionModal versus UIKit view-controller presentation; built-in reader management, delegate hooks and best-effort warm-up. Sample targets link TEST. External TerminalAPIKit resolution is 1.3.0, not dependency implementation evidence.
- **Release changes:** ten added languages, OS-language fallback, iOS 26 close-button consistency and label/language-flash fixes. Upstream says built with Xcode 26.3 and NYC1 PIN support expires 2027-04-13. Binary implementation was not inspected; expiry is not generalized to all features or releases.
- **Integration cautions:** sample registration comment requires setupToken forwarding, but implementation omits it, uses a placeholder URL and ignores HTTP status. Warm-up errors are swallowed; payment results are only printed. Target iOS 18.4 differs from project default 17.0; entitlement-file presence is not signing/provisioning proof. README doc links still target 3.21.0; stale DocC and binaries remain excluded.
- **Updated sections:** existing Mobile POS concept first with reciprocal registration warning, cumulative source/changelog, company source/release counts, provider catalog and logs. No new concept or cross-company comparison needed. Existing website/repository histories preserved.
- **Execution boundary:** no Xcode build, SDK/dependency download, credentials, device/API/payment execution, commit or push.

## Raw Sources

- [Snapshot and full retained-file inventory](../../../../raw/github/adyen/adyen-pos-mobile-ios/snapshots/2026-10-30-689bdbd/manifest.json)
- [Package-qualified release record](../../../../raw/github/adyen/adyen-pos-mobile-ios/releases/adyenpos/3.22.0/2026-10-30/manifest.json)
- [Release announcements](../../../../raw/github/adyen/adyen-pos-mobile-ios/releases/adyenpos/3.22.0/2026-10-30/release-notes.md)
- [Shared model and incomplete registration](../../../../raw/github/adyen/adyen-pos-mobile-ios/snapshots/2026-10-30-689bdbd/files/POSSampleApp/SampleAppSwiftUI/MainViewModel.swift)

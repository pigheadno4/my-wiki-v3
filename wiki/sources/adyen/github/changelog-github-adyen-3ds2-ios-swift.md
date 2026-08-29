---
title: "GitHub changelog: Adyen/adyen-3ds2-ios-swift"
type: source
date_ingested: 2026-08-29
original_format: github-repo
raw_files:
  - "github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/manifest.json"
tags: [adyen, ios, swift, 3d-secure, 3ds2, authentication, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-3ds2-ios-swift`. Cumulative integration knowledge belongs in [[source-github-adyen-3ds2-ios-swift]] and the linked immutable snapshots. The separate `adyen/adyen-3ds2-ios` repository retains its own history in [[changelog-github-adyen-3ds2-ios]].

## `adyen-3ds2-ios-swift@3.0.1` (2025-09-16)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `adyen-3ds2-ios-swift` | Initial baseline | `3.0.1` | `1596f558f39d9e706030ab77ebcf8c01492d1ecd` | Full |

**Important findings:** The release notes identify Swift 6 warning fixes and a clipped-logo fix for iOS 26. The retained public interface is compiled with Swift 6 and exposes concurrency-aware APIs, but the binary framework prevents implementation-level verification of either fix.

**Developer or merchant impact:** Integrators using Swift Package Manager need Xcode 16 or newer according to the README. New code can use async transaction initialization, async authentication parameters, and async challenge execution. Older `ADY*` compatibility types remain present but are deprecated and marked for future removal.

**Migration action:** Regression-test transaction initialization, challenge presentation and return handling, cancellation, multi-scene continuity, custom appearance, and iOS 26 logo rendering. Prefer Swift-native types over `LegacyInterface`. Verify license terms and Carthage repository identity with Adyen because the retained upstream metadata conflicts.

**Updated source sections:** Evidence boundary; distribution and platform metadata; transaction and server flow; challenge flow and lifecycle; errors and security warnings; appearance and privacy; legacy compatibility; `3.0.1` release finding.

Broader transaction, challenge, lifecycle, warning, privacy, appearance, and compatibility behavior is the initial cumulative baseline, not release-specific change evidence.

### Evidence gaps and contradictions

- The SDK implementation remains a binary XCFramework; the public `.swiftinterface` proves declarations but not implementation behavior.
- The capsule retains one canonical dynamic iOS ARM64 public surface, not every static, simulator, Catalyst, or architecture slice.
- README API links use classic Payment API v64 flows and do not establish current recommendations for new integrations.
- The podspec says Apache 2.0, while `LICENSE` and README say MIT.
- The README's Carthage command points to `adyen/adyen-3ds2-ios`, not `adyen/adyen-3ds2-ios-swift`.

### Evidence

- `raw/github/adyen/adyen-3ds2-ios-swift/releases/adyen-3ds2-ios-swift/3.0.1/2026-08-29/manifest.json`
- `raw/github/adyen/adyen-3ds2-ios-swift/releases/adyen-3ds2-ios-swift/3.0.1/2026-08-29/release-notes.md`
- `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/manifest.json`
- `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/README.md`
- `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/Adyen3DS2_Swift.podspec`
- `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/LICENSE`
- `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/XCFramework/Dynamic/Adyen3DS2_Swift.xcframework/ios-arm64/Adyen3DS2_Swift.framework/Modules/Adyen3DS2_Swift.swiftmodule/arm64-apple-ios.swiftinterface`
- `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/XCFramework/Dynamic/Adyen3DS2_Swift.xcframework/ios-arm64/Adyen3DS2_Swift.framework/PrivacyInfo.xcprivacy`

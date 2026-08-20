---
title: "GitHub changelog: Adyen/adyen-3ds2-ios"
type: source
date_ingested: 2026-08-19
original_format: github-repo
raw_files:
  - "github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/manifest.json"
tags: [adyen, ios, 3d-secure, 3ds2, authentication, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-3ds2-ios`. Cumulative integration knowledge belongs in [[source-github-adyen-3ds2-ios]] and the linked immutable snapshots.

## `adyen-3ds2-ios@2.4.4` (2025-11-05)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `adyen-3ds2-ios` | Initial baseline | `2.4.4` | `00862adbc079d0be943666a4ad2523deb31f9546` | Full |

**Important findings:** The release adds Device Information 1.7 support and fixes memory warnings plus navigation-bar behavior for iOS 26.

**Developer or merchant impact:** Device-information payload behavior changes within the binary runtime. The iOS 26 fix aligns with the public navigation-bar background property becoming ignored and deprecated. The memory-warning impact cannot be narrowed from the retained binary/public-header capsule.

**Migration action:** Regression-test native challenges, multi-scene handoff, memory pressure, and iOS 26 navigation after updating. Review the retained privacy manifest and merchant-app disclosures because device information is part of authentication request data.

**Updated source sections:** Evidence boundary; distribution and platform metadata; transaction and server flow; challenge flow and errors; lifecycle and scene handling; security and privacy; challenge UI; `2.4.4` release finding.

Broader transaction, challenge, error, lifecycle, warning, privacy, and UI behavior is the initial cumulative baseline, not release-specific change evidence.

### Evidence gaps

- The SDK implementation is retained only as a binary XCFramework; code-level verification of release changes is unavailable.
- The capsule retains the selected dynamic iOS-arm64 public surface, not every advertised framework variant or platform slice.
- The README references classic Payment API v64 endpoints and should not be treated as proof of the current API recommendation.
- `ADYWarning.h` incorrectly associates its warning class with `ChallengeParameters` in the specification note.

### Evidence

- `raw/github/adyen/adyen-3ds2-ios/releases/adyen-3ds2-ios/2.4.4/2026-08-17/manifest.json`
- `raw/github/adyen/adyen-3ds2-ios/releases/adyen-3ds2-ios/2.4.4/2026-08-17/release-notes.md`
- `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/manifest.json`
- `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/README.md`
- `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/XCFramework/Dynamic/Adyen3DS2.xcframework/ios-arm64/Adyen3DS2.framework/Headers/ADYNavigationBarAppearance.h`
- `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/XCFramework/Dynamic/Adyen3DS2.xcframework/ios-arm64/Adyen3DS2.framework/PrivacyInfo.xcprivacy`

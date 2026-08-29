---
title: "GitHub: Adyen/adyen-3ds2-ios-swift"
type: source
date_ingested: 2026-08-29
original_format: github-repo
raw_files:
  - "github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/manifest.json"
tags: [adyen, ios, swift, 3d-secure, 3ds2, authentication, mobile-sdk, github-repository]
---

## Overview

`Adyen/adyen-3ds2-ios-swift` distributes Adyen's Swift-native binary iOS runtime for EMV 3-D Secure transactions and challenges. This cumulative page begins with package-qualified release `adyen-3ds2-ios-swift@3.0.1` at exact SHA `1596f558f39d9e706030ab77ebcf8c01492d1ecd`.

Repository: <https://github.com/Adyen/adyen-3ds2-ios-swift>

## Evidence boundary

- The capsule retains package metadata, documentation, the dynamic iOS ARM64 framework's generated public headers, its public Swift module interface, and its privacy manifest. The runtime implementation remains binary.
- The public `.swiftinterface` proves callable declarations and availability annotations, but it cannot independently verify cryptography, device-information collection, challenge rendering, or the implementation of release fixes.
- This repository and `adyen/adyen-3ds2-ios` are independently versioned evidence histories. Similar APIs and the compatibility namespace do not make `3.0.1` a proven replacement for every `2.4.4` behavior.
- README examples use classic `/authorise` and Payment API v64 `/authorise3ds2` links. They establish the retained SDK contract, not the currently recommended integration path for a new merchant.
- The snapshot proves SDK behavior, not merchant enablement, issuer behavior, authentication success, liability shift, or regional eligibility.

## Grounding excerpts

> "With this SDK, you can accept 3D Secure 2.0 payments via Adyen."
>
> `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/README.md:3`

> "Use the `transaction`'s `authenticationRequestParameters` in your call to `/authorise3ds2`."
>
> `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/README.md:74`

> "Because of recent updates to the 3D Secure protocol, we strongly recommend that you provide the `threeDSRequestorAppURL` parameter as a universal link."
>
> `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/README.md:102`

> "Note the older interface is deprecated and this interface will be removed in the next couple of versions."
>
> `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/README.md:144`

> "Swift 6 warnings"
>
> `raw/github/adyen/adyen-3ds2-ios-swift/releases/adyen-3ds2-ios-swift/3.0.1/2026-08-29/release-notes.md:2`

## Distribution and platform metadata

The repository advertises CocoaPods, Carthage, Swift Package Manager, dynamic and static XCFrameworks, and manual integration. `Package.swift` packages the dynamic XCFramework as a binary target, declares iOS 10 and macOS 10.15, and has no package dependencies. The podspec also declares iOS 10. The retained public interface was compiled as a Swift 6 library-evolution module for iOS 13 ARM64, so package deployment declarations and this selected compiled slice describe different boundaries.

The README requires Xcode 16 or newer for Swift Package Manager and asks consumers to select at least version `3.0.0`. Static integration must copy the resource bundle and include or merge the privacy manifest into the application bundle.

> [!warning] Contradiction
> The podspec labels the license as Apache 2.0, while the retained `LICENSE` file and README identify MIT. The README's Carthage command also references `adyen/adyen-3ds2-ios` instead of this Swift repository. These are upstream metadata defects; consumers should verify the intended license and Carthage source with Adyen.

## Transaction and server flow

The app creates `ServiceParameters` from the directory-server identifier, public key, and root certificates returned by Adyen. It supplies the message version selected by the 3DS Server and initializes `Transaction` with a security delegate and appearance configuration.

The public API supports async initialization and a completion-based initializer. `authenticationRequestParameters` is async and returns device information, SDK application and transaction identifiers, SDK reference number, ephemeral public key, and message version for submission through the merchant server to `/authorise3ds2`. `MessageVersion` supports `2.1.0` and `2.2.0`.

## Challenge flow and lifecycle

`ChallengeParameters` carries the 3DS Server transaction ID, ACS transaction ID, ACS reference number, ACS signed content, and optional requestor app URL. The README strongly recommends a universal link for the app URL; it may be omitted for protocol `2.1.0`.

`Transaction.performChallenge` has callback and async variants and returns `ChallengeResult.transactionStatus`. The app submits that status in its second `/authorise3ds2` call. `Transaction.Constants.minimumChallengeTimeout` defines the lower timeout boundary, while the retained interface exposes no maximum.

The app must retain the transaction until authentication completes and should share it across iPadOS multi-window or Mac Catalyst scenes. The public API supports explicit close and challenge cancellation. The binary interface does not expose enough implementation to prove when sensitive data is destroyed.

## Errors and security warnings

`ThreeDSError` exposes an error code, optional field, cancellation indicator, and base64 representation. `ErrorType` distinguishes directory-server, fingerprinting, secure-channel, ACS response, request, cancellation, timeout, message, extension, transaction-identifier, version, and response-counter failures.

`SecurityWarningsDelegate` receives low-, medium-, or high-severity `Warning` values. The warnings carry identifiers and messages, but the retained public interface does not reveal the internal checks that produce them.

## Appearance and privacy

`AppearanceConfiguration` controls background and text colors, status bar, modal presentation, navigation, labels, text fields, selection controls, switches, information views, and submit, cancel, resend, and out-of-band button styles. The interface also exposes challenge-loading helpers and image providers; underscore-prefixed public declarations should not be treated as stable merchant-facing APIs without separate documentation.

The privacy manifest declares coarse location collection for app functionality, not linked to the user and not used for tracking. It declares required-reason access to UserDefaults (`CA92.1`) and file timestamps (`C617.1`), disables tracking, and lists no tracking domains. This is a package declaration, not a complete privacy inventory for the merchant app.

## Legacy compatibility

The public interface retains a deprecated `LegacyInterface` namespace containing `ADYService`, `ADYTransaction`, challenge, appearance, warning, progress, and runtime-error types. The README provides typealiases for older integrations but states that the interface will be removed in the next couple of versions. New integration work should use the Swift-native value types and `Transaction` APIs.

## `3.0.1` release finding

Release `3.0.1` documents Swift 6 warning fixes and a clipped-logo fix for iOS 26. The Swift 6 module and concurrency annotations are visible in the public interface, but the exact warning and logo implementation changes are not independently inspectable in the binary capsule. No migration steps or breaking API changes are documented.

Broader transaction, challenge, error, lifecycle, warning, privacy, appearance, and compatibility behavior is the initial cumulative baseline, not change evidence introduced solely by `3.0.1`.

## Related

- [[changelog-github-adyen-3ds2-ios-swift]] - package-qualified release ledger
- [[adyen-3ds2-ios-sdk]] - shared durable iOS integration concept
- [[source-github-adyen-3ds2-ios]] - independently versioned Objective-C-oriented distribution
- [[source-github-adyen-ios]] - parent iOS checkout SDK and adapter boundary
- [[adyen-ios-sdk]] - parent iOS SDK concept
- [[source-github-adyen-3ds2-android]] - independently versioned Android counterpart
- [[adyen]] - company and knowledge-status page

## Raw sources

- Snapshot manifest: `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/manifest.json`
- Release manifest: `raw/github/adyen/adyen-3ds2-ios-swift/releases/adyen-3ds2-ios-swift/3.0.1/2026-08-29/manifest.json`
- Release notes: `raw/github/adyen/adyen-3ds2-ios-swift/releases/adyen-3ds2-ios-swift/3.0.1/2026-08-29/release-notes.md`
- README: `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/README.md`
- Package metadata: `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/Adyen3DS2_Swift.podspec` and `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/Package.swift`
- Public Swift interface: `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/XCFramework/Dynamic/Adyen3DS2_Swift.xcframework/ios-arm64/Adyen3DS2_Swift.framework/Modules/Adyen3DS2_Swift.swiftmodule/arm64-apple-ios.swiftinterface`
- Public headers: `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/XCFramework/Dynamic/Adyen3DS2_Swift.xcframework/ios-arm64/Adyen3DS2_Swift.framework/Headers/`
- Privacy manifest: `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/XCFramework/Dynamic/Adyen3DS2_Swift.xcframework/ios-arm64/Adyen3DS2_Swift.framework/PrivacyInfo.xcprivacy`

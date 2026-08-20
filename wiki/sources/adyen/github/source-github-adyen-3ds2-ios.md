---
title: "GitHub: Adyen/adyen-3ds2-ios"
type: source
date_ingested: 2026-08-19
original_format: github-repo
raw_files:
  - "github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/manifest.json"
tags: [adyen, ios, 3d-secure, 3ds2, authentication, mobile-sdk, github-repository]
---

## Overview

`Adyen/adyen-3ds2-ios` contains Adyen's standalone native iOS runtime for EMV 3-D Secure transactions and challenges. This cumulative page begins with package-qualified release `adyen-3ds2-ios@2.4.4` at exact SHA `00862adbc079d0be943666a4ad2523deb31f9546`.

Repository: <https://github.com/Adyen/adyen-3ds2-ios>

## Evidence boundary

- The snapshot proves retained public integration behavior for `2.4.4`. It does not prove current merchant enablement, issuer behavior, authentication success, liability shift, or regional eligibility.
- The capsule retains package metadata, the dynamic XCFramework's public Objective-C headers, and its privacy manifest. The SDK implementation remains binary, so cryptography, device-information collection, memory-warning fixes, and challenge rendering cannot be independently inspected.
- The SDK is a delegated runtime used by Adyen iOS. Adyen iOS's adapter and this repository remain independently versioned evidence histories.
- README links use the classic `/authorise` and Payment API v64 `/authorise3ds2` flow. They prove the retained SDK contract, not that those API versions are the current recommended integration for a new merchant.
- `ADYWarning.h` says the warning class corresponds to `ChallengeParameters`; this appears inconsistent with the class purpose and is preserved as an upstream documentation defect.

## Grounding excerpts

> "With this SDK, you can accept 3D Secure 2.0 payments via Adyen."
>
> `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/README.md:3`

> "Use the `transaction`'s `authenticationRequestParameters` in your call to Adyen backend."
>
> `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/README.md:67`

> "Because of recent updates to the 3D Secure protocol, we strongly recommend that you provide the `threeDSRequestorAppURL` parameter as a universal link."
>
> `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/README.md:88`

> "This method should be called when no challenge is performed. When a challenge is performed, all sensitive data is removed automatically."
>
> `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/XCFramework/Dynamic/Adyen3DS2.xcframework/ios-arm64/Adyen3DS2.framework/Headers/ADYTransaction.h:97-99`

> "Device information 1.7 supported."
>
> `raw/github/adyen/adyen-3ds2-ios/releases/adyen-3ds2-ios/2.4.4/2026-08-17/release-notes.md:2`

## Distribution and platform metadata

The SDK is distributed through CocoaPods, Carthage, Swift Package Manager, dynamic or static XCFramework integration, and manual installation. The retained CocoaPods and Swift package metadata declare iOS 10; `Package.swift` also declares macOS 10.15 and packages the dynamic XCFramework as a binary target. The README requires Xcode 16 or newer for Swift Package Manager.

Static framework integrations must copy the resource bundle and merge the privacy manifest into the app bundle. This snapshot retains only the selected dynamic framework public surface, so it does not establish the complete contents of every distribution variant.

## Transaction and server flow

The app initializes `ADYServiceParameters` with a directory-server identifier, base64-encoded JWK public key, and root certificates represented as compact JWS. `ADYService` initializes asynchronously and creates an `ADYTransaction` using the protocol message version chosen by the 3DS Server.

`ADYAuthenticationRequestParameters` contains JWE-encrypted device information, SDK application and transaction identifiers, the EMVCo SDK reference number, ephemeral public key as JWK, and message version. The app submits those parameters through its merchant server to `/authorise3ds2`. If transaction creation fails, the README serializes the `NSError` with `base64Representation` and submits it to Adyen.

## Challenge flow and errors

Challenge parameters include the 3DS Server transaction ID, ACS transaction ID, ACS reference number, signed ACS content, and optional `threeDSRequestorAppURL`. The URL is ignored for protocol `2.1.0`; for later flows the SDK strongly recommends a universal link for out-of-band return handling.

The transaction supports delegate and completion-handler variants. A successful challenge returns `ADYChallengeResult.transactionStatus` for the second `/authorise3ds2` call. On failure, the README collects available 3DS Server, ACS, and SDK transaction identifiers plus error details, submits the base64 error representation, and sends transaction status `U`.

Runtime errors distinguish unknown directory servers, secure-channel setup failures, invalid ACS responses, failed or timed-out ACS requests, challenge timeout, and shopper cancellation. Protocol-error `userInfo` keys expose identifiers and details needed for diagnosis. Custom challenge timeouts must be at least 300 seconds and have no documented maximum.

## Lifecycle and scene handling

The app must retain `ADYTransaction` until authentication finishes. For iPadOS multi-window and Mac Catalyst, the README recommends sharing service and transaction objects between scenes so a shopper can continue after switching windows.

`ADYTransaction.close` releases resources when no challenge is performed. When a challenge runs, the public header says sensitive data is removed automatically. The transaction also exposes explicit challenge cancellation and an optional progress view; completion-based progress show and hide methods replace deprecated synchronous variants.

## Security and privacy

`ADYService.warnings` returns low-, medium-, or high-severity initialization warnings. A transaction can also send real-time warning-list changes to `ADYSecurityWarningsDelegate`.

The retained privacy manifest declares coarse location collection for app functionality, not linked to the user and not used for tracking. It declares required-reason access to UserDefaults (`CA92.1`) and file timestamps (`C617.1`), no tracking domains, and tracking disabled. These are package declarations, not proof of the internal collection implementation or a complete merchant-app privacy inventory.

## Challenge UI

`ADYAppearanceConfiguration` controls challenge background, status-bar style, modal presentation, shared colors, navigation bar, labels, text fields, selection controls, switches, information views, and submit, continue, next, cancel, resend, or out-of-band buttons. Button configuration includes text transform, enabled, disabled, and highlighted colors plus corner radius.

The navigation-bar background color is deprecated and ignored from iOS 26. That public API change aligns with the release note's iOS 26 navigation-bar fix, but the binary capsule cannot verify the implementation.

## `2.4.4` release finding

Release `2.4.4` adds Device Information 1.7 support and fixes memory warnings plus navigation-bar behavior for iOS 26. No migration steps or breaking API changes are documented. The deprecated navigation background property is visible in the retained public header; the device-information and memory behavior remain binary-only release claims.

Broader transaction, challenge, error, lifecycle, security-warning, privacy, and UI behavior is the initial cumulative baseline, not change evidence introduced solely by `2.4.4`.

## Related

- [[changelog-github-adyen-3ds2-ios]] - package-qualified release ledger
- [[adyen-3ds2-ios-sdk]] - durable integration concept
- [[source-github-adyen-ios]] - parent iOS checkout SDK and adapter boundary
- [[adyen-ios-sdk]] - parent iOS SDK concept
- [[source-github-adyen-3ds2-android]] - independently versioned Android counterpart
- [[adyen]] - company and knowledge-status page

## Raw sources

- Snapshot manifest: `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/manifest.json`
- Release manifest: `raw/github/adyen/adyen-3ds2-ios/releases/adyen-3ds2-ios/2.4.4/2026-08-17/manifest.json`
- Release notes: `raw/github/adyen/adyen-3ds2-ios/releases/adyen-3ds2-ios/2.4.4/2026-08-17/release-notes.md`
- README: `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/README.md`
- Package metadata: `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/Adyen3DS2.podspec` and `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/Package.swift`
- Public headers: `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/XCFramework/Dynamic/Adyen3DS2.xcframework/ios-arm64/Adyen3DS2.framework/Headers/`
- Privacy manifest: `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/XCFramework/Dynamic/Adyen3DS2.xcframework/ios-arm64/Adyen3DS2.framework/PrivacyInfo.xcprivacy`

---
title: "Adyen 3DS2 iOS SDK"
type: concept
category: technology
tags: [adyen, ios, 3d-secure, 3ds2, authentication, sdk, challenge-flow]
---

## Adyen 3DS2 iOS SDK

Adyen's standalone iOS 3DS2 SDK supplies the native EMV 3-D Secure transaction and challenge runtime used by Adyen iOS. The wiki retains two independently versioned distributions: `Adyen3DS2@2.4.4` from `adyen/adyen-3ds2-ios` at exact SHA `00862adbc079d0be943666a4ad2523deb31f9546`, and the Swift-native `adyen-3ds2-ios-swift@3.0.1` from `adyen/adyen-3ds2-ios-swift` at exact SHA `1596f558f39d9e706030ab77ebcf8c01492d1ecd`.

## Integration flow

The app creates `ADYServiceParameters` from directory-server values returned by Adyen, asynchronously initializes `ADYService`, and creates an `ADYTransaction` using the message version selected by the 3DS Server. The transaction's `ADYAuthenticationRequestParameters` contain encrypted device information and SDK identifiers that the app submits through its server to `/authorise3ds2`.

When Adyen requires a challenge, the app builds `ADYChallengeParameters` from the 3DS Server transaction ID, ACS transaction ID, ACS reference number, signed ACS content, and an optional app-return URL. A universal link is strongly recommended for the return URL. Challenge completion returns a transaction status; failure returns an `NSError` whose base64 representation and status `U` are sent to Adyen.

## Lifecycle and errors

The app must retain its service and transaction while authentication is in progress, including across iPadOS multi-window or Mac Catalyst scene changes. Custom challenge timeouts must be at least 300 seconds and have no documented maximum.

If no challenge occurs, the app calls `close` to release transaction resources. After a challenge, sensitive transaction data is removed automatically. Runtime errors distinguish unknown directory servers, secure-channel setup failures, invalid ACS responses, request failures or timeouts, challenge timeout, and shopper cancellation. Protocol errors expose 3DS Server, ACS, and SDK transaction identifiers plus error details when available.

## Security, privacy, and UI

Initialization and the transaction security delegate expose low-, medium-, and high-severity warnings. The retained privacy manifest declares coarse location for app functionality as not linked to the user and not used for tracking. It also declares required-reason access to UserDefaults and file timestamps and lists no tracking domains.

Challenge appearance supports navigation, labels, text fields, selection controls, information views, switches, background and status-bar styling, modal presentation, and submit, continue, next, cancel, resend, and out-of-band buttons. Navigation-bar background color is deprecated and ignored from iOS 26. Progress-view calls with completion handlers replace the deprecated synchronous show and hide methods.

## Distribution and release boundary

The SDK is distributed as a binary XCFramework through CocoaPods, Carthage, Swift Package Manager, or manual framework integration. The retained package metadata declares iOS 10 as the deployment target and requires Xcode 16 or newer for Swift Package Manager according to the README.

Release `2.4.4` adds Device Information 1.7 support and fixes memory warnings plus the navigation bar for iOS 26. Those are release-note claims; the capsule retains public headers and a binary framework, not implementation source for independent code-level verification.

## Swift-native `3.0.1` baseline

The Swift-native package keeps the same directory-server, authentication-request, challenge, transaction-status, security-warning, privacy, and appearance responsibilities while exposing Swift value types and concurrency-aware APIs. `Transaction` can initialize asynchronously, exposes asynchronous authentication parameters, supports callback and async challenge execution, and provides explicit `close`, challenge cancellation, and a minimum challenge-timeout constant. The public interface supports message versions `2.1.0` and `2.2.0`.

The retained Swift interface also contains a deprecated `LegacyInterface` namespace for the older `ADYService`, `ADYTransaction`, appearance, warning, challenge, and error surfaces. Its declarations repeatedly say those compatibility APIs will not be supported in future versions, so migration work should use `ServiceParameters`, `Transaction`, `ChallengeParameters`, `AppearanceConfiguration`, `Warning`, and the other Swift-native types.

Release `3.0.1` documents Swift 6 warning fixes and an iOS 26 clipped-logo fix. The package is still a binary XCFramework: the retained public `.swiftinterface` proves the callable API, but it does not expose the implementation behind cryptography, device information, challenge rendering, or the release fixes.

> [!warning] Contradiction
> The `3.0.1` podspec labels the package license as Apache 2.0 while the retained `LICENSE` file contains the MIT License. The README's Carthage command also points to `adyen/adyen-3ds2-ios`, not the Swift repository. Treat both as upstream metadata defects until Adyen clarifies them.

## Related

- [[source-github-adyen-3ds2-ios]] - cumulative exact-SHA SDK evidence
- [[changelog-github-adyen-3ds2-ios]] - package-qualified release ledger
- [[source-github-adyen-3ds2-ios-swift]] - cumulative Swift-native exact-SHA evidence
- [[changelog-github-adyen-3ds2-ios-swift]] - Swift-native package-qualified release ledger
- [[adyen-ios-sdk]] - parent checkout SDK and adapter boundary
- [[adyen-3ds2-android-sdk]] - independently versioned Android counterpart
- [[source-github-adyen-ios]] - independently versioned parent repository evidence
- [[adyen]] - company and knowledge-status page

## Sources

- `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/manifest.json` - exact-SHA source capsule
- `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/README.md` - installation, transaction, challenge, scene-lifecycle, and UI flow
- `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/XCFramework/Dynamic/Adyen3DS2.xcframework/ios-arm64/Adyen3DS2.framework/Headers/ADYTransaction.h` - challenge timeout and transaction cleanup
- `raw/github/adyen/adyen-3ds2-ios/snapshots/2026-08-17-00862ad/files/XCFramework/Dynamic/Adyen3DS2.xcframework/ios-arm64/Adyen3DS2.framework/PrivacyInfo.xcprivacy` - retained privacy declarations
- `raw/github/adyen/adyen-3ds2-ios/releases/adyen-3ds2-ios/2.4.4/2026-08-17/release-notes.md` - exact release claims
- `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/manifest.json` - exact-SHA Swift-native source capsule
- `raw/github/adyen/adyen-3ds2-ios-swift/snapshots/2026-08-29-1596f55/files/XCFramework/Dynamic/Adyen3DS2_Swift.xcframework/ios-arm64/Adyen3DS2_Swift.framework/Modules/Adyen3DS2_Swift.swiftmodule/arm64-apple-ios.swiftinterface` - Swift-native public API
- `raw/github/adyen/adyen-3ds2-ios-swift/releases/adyen-3ds2-ios-swift/3.0.1/2026-08-29/release-notes.md` - Swift 6 and iOS 26 release claims

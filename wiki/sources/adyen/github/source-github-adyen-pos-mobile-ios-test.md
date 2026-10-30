---
title: "GitHub: adyen/adyen-pos-mobile-ios-test"
type: source
date_ingested: 2026-10-30
date_updated: 2026-10-30
original_format: github-repo
raw_files:
  - "github/adyen/adyen-pos-mobile-ios-test/snapshots/2026-10-30-5e22343/manifest.json"
tags: [adyen, mobile-pos, ios, test-environment, terminal-api, swiftui, github-repository]
---

## Overview

Initial full baseline of `AdyenPOS@3.22.0` in `adyen/adyen-pos-mobile-ios-test`, tag `v3.22.0`, SHA `5e2234351d6164f11911d09efed4630fe82e0050`. Released 2026-10-27; collected and ingested 2026-10-30. This is a TEST-only binary SDK distribution and merchant-device SwiftUI/UIKit POS sample, not SDK implementation source or a unit-test suite.

All 30 assigned paths were read in full, plus both packet files: 27 retained files, seven sample Swift files, 51,055 bytes, snapshot manifest, release manifest and notes. No focused-reading exception or prior collected baseline exists. Baseline integration logic is not asserted to be newly introduced in 3.22.0. Future ingests must append version-qualified knowledge and preserve this history.

## Key takeaways

- This repository distributes only TEST products. The same package/version in the main repository does not make their histories interchangeable.
- The seven retained Swift files match the main repository's collected baseline, including its incomplete backend-registration callback.
- SwiftUI and UIKit share PaymentService and Terminal API request logic, but use different presentation APIs.
- SwiftUI permission/deployment settings differ from the main repository; neither configuration is a verified SDK compatibility or provisioning result.
- Release notes announce localization/UI changes and a version-scoped NYC1 PIN expiry; runtime internals remain outside this capsule.

## Package and Environment Identity

Package.swift declares package name `AdyenPOS`, Swift tools 5.6 and no package dependencies. Its products are `AdyenPOSTEST` and `ADYPOSTEST`; the latter includes both corresponding binary targets. There are no LIVE products in this manifest. Both targets refer to version 3.22.0 Test ZIPs under `https://pos-mobile-test.cdn.adyen.com/adyen-pos-ios/3.22.0/Test/`.

The declared AdyenPOS checksum is `70cc8bb6284a6f50826ea31338ed4f390a9f3a6798c849bde73c00e56820ab16`; ADYPOS is `c4646cfca04a9972cafaf5b6f234f64d42ca9b37e26ed28c3731fcc4afc1880c`. These match the TEST checksums declared by the separately collected main repository. Neither binary download, signature validation nor byte-for-byte binary comparison was performed. README explicitly restricts this distribution to the ADYEN TEST environment; its go-live link is navigation, not evidence that live prerequisites are satisfied.

Both app targets link AdyenPOSTEST and TerminalAPIKit. The external Terminal API package permits versions from 1.0.0 up to the next major; Package.resolved records 1.3.0 at `f3fb9e4f7ff80077db093858db94e4f5ccfaa944`. Recorded resolution is not a permanent hard pin for future resolves. That dependency's models/Coder implementation belong to another repository and were not collected here.

## Payment and Presentation Flow

MainViewModel lazily retains `PaymentService(delegate: self)`; comments require retaining both service and delegate because the service holds its delegate weakly. Transaction initiation reads installationId, constructs a TerminalAPIKit payment message, obtains `getPaymentInterface(with:)` and awaits performTransaction using an encoded Payment.Request. Responses and caught errors are printed. There is no implemented outcome reconciliation, fulfillment decision, reversal/refund or explicit duplicate/in-flight protection; binary-internal behavior is not inspectable.

The request header uses protocol 3.0, service/payment/request classification, a six-character UUID prefix serviceIdentifier, UUID saleIdentifier and installationId as poiIdentifier. The body uses UUID/date sale transaction identification and fixed USD 50. These are demonstration values, not currency/amount eligibility or guaranteed identifier uniqueness.

SwiftUI buttons select tapToPay or cardReader with viewModifier presentation, and apply transactionModal to the view; device management uses a sheet containing DeviceManagementView. UIKit selects the same interfaces with presentingViewController and presents DeviceManagementViewController. The retained sample describes reader management for NYC1 rather than Tap to Pay alone. SwiftUI's task and UIKit's viewDidLoad trigger initialization; this is not an execution-tested lifecycle guarantee.

Initialization assigns the device-manager delegate and calls `try? await paymentService.warmUp()`, suppressing warm-up failure. Four custom reader-management callbacks are empty. The built-in UI and delegate hooks do not establish custom discovery/retry UX, transaction readiness or a production recovery strategy.

## Backend Registration and Sample Contradiction

The delegate signature is `register(with setupToken: String) async throws -> String`. Comments require forwarding setupToken to the merchant backend so that backend calls `/sessions`, rather than calling the provider endpoint directly from the app. The decoded response contains sdkData, which the method returns.

> [!warning] Contradiction
> Despite that comment, the implementation creates a URLRequest from a placeholder backend URL without including setupToken in a body, header or query. It sets no explicit method/body or authentication and discards the response metadata without checking HTTP status. Invalid URL construction returns an empty string. This unfinished template is not a working registration integration. [[adyen-mobile-pos]] retains the reciprocal warning.

Transport/decoding failures can throw, but HTTP failure is not explicitly classified. A merchant needs an actual authenticated backend contract, token forwarding and response handling; provider session fields and recovery behavior require separately versioned evidence rather than inference from this sample.

## Build Settings and Cross-Repository Boundary

UIKit Debug and Release explicitly target iOS 18.4. SwiftUI Debug/Release do not set a target deployment override, while project Debug/Release set 17.0. This describes retained build-setting inheritance, not proof of the binary SDK's supported minimum or a successful build. SwiftUI declares generated Info.plist Bluetooth/camera usage descriptions; UIKit declares both in its Info.plist. Permission strings are not runtime authorization.

The entitlement file contains `com.apple.developer.proximity-reader.payment.acceptance=true`, but the project does not explicitly set CODE_SIGN_ENTITLEMENTS. File presence does not prove signing application or Apple approval. Sample SWIFT_VERSION 5.0, manifest tools 5.6 and release-note Xcode 26.3 are distinct metadata. The shared scheme targets UIKit. No build, package resolution, provisioning or device/payment execution was performed.

Compared only with the collected `adyen/adyen-pos-mobile-ios` 3.22.0 capsule, 23 of 27 corresponding files match, including all seven Swift files. Differences are root LICENSE copyright year, Package.swift products/CDN, README TEST notice/documentation links, and project.pbxproj permission/deployment settings. The main repository explicitly sets 18.4 for all four target configurations. These are cross-repository snapshot differences, not a historical version delta or proof of binary implementation equivalence. Keep [[source-github-adyen-pos-mobile-ios]] independent.

## Release `AdyenPOS@3.22.0`: Announcements

- Adds Catalan, Croatian, Czech, Estonian, Icelandic, Japanese, Latvian, Lithuanian, Romanian and Russian.
- Falls back to OS language when the app language is unsupported before English.
- Makes close buttons consistent across transaction, pairing and device-management screens on iOS 26.
- Corrects primary-language labels and an initial app-language flash in payment UI.
- Notes a build with Xcode 26.3 and NYC1 PIN support expiry on 2027-04-13.

These are upstream announcements, not locally inspected binary changes. The expiry applies to this release's NYC1 PIN support, not universally to Tap to Pay or other versions.

## Evidence Limits and Query Routing

At this exact tag the README still links 3.21.0 developer documentation/tutorials. Preserve this mismatch; later default-branch corrections are not this snapshot. Generated DocC, binary internals/public headers and dependency implementation are outside scope. Empty packet evidence_gaps means configured collection completeness, not complete API coverage.

For detailed API/OS/device/region eligibility, session fields, offline/refund/status behavior or live migration, consult the corresponding dated website or exact-version repository evidence. Missing detail needs separately approved collection or supplements. Identify the repository as well as AdyenPOS version when querying these two distributions. No new concept or cross-company comparison is warranted.

## Grounding Quotes

Locations are within this snapshot's files/ directory.

1. `> :warning: This repo applies to the ADYEN TEST ENVIRONMENT ONLY` - README.md:3.
2. `name: "AdyenPOS",` - Package.swift:7.
3. `lazy var paymentService = PaymentService(delegate: self)` - POSSampleApp/SampleAppSwiftUI/MainViewModel.swift:17.
4. `let request = URLRequest(url: url)` - same file:104, alongside the setupToken requirement in comments.
5. `INFOPLIST_KEY_NSBluetoothAlwaysUsageDescription = "This application requires Bluetooth to pair and connect with the card readers";` - POSSampleApp/POSSampleApp.xcodeproj/project.pbxproj:358.

## Related

- Company: [[adyen]]
- Concept: [[adyen-mobile-pos]]
- History: [[changelog-github-adyen-pos-mobile-ios-test]]
- Independent main distribution: [[source-github-adyen-pos-mobile-ios]]
- Dated website route: [[source-adyen-docs-point-of-sale-mobile-ios-build]]

## Raw Sources

- [Exact-SHA snapshot inventory](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/snapshots/2026-10-30-5e22343/manifest.json)
- [Release identity](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/releases/adyenpos/3.22.0/2026-10-30/manifest.json)
- [Release announcements](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/releases/adyenpos/3.22.0/2026-10-30/release-notes.md)
- [Distribution manifest](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/snapshots/2026-10-30-5e22343/files/Package.swift)
- [Shared model and incomplete registration](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/snapshots/2026-10-30-5e22343/files/POSSampleApp/SampleAppSwiftUI/MainViewModel.swift)
- [SwiftUI presentation](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/snapshots/2026-10-30-5e22343/files/POSSampleApp/SampleAppSwiftUI/MainView.swift)
- [UIKit presentation](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/snapshots/2026-10-30-5e22343/files/POSSampleApp/SampleAppUIKit/MainViewController.swift)
- [Project configuration](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/snapshots/2026-10-30-5e22343/files/POSSampleApp/POSSampleApp.xcodeproj/project.pbxproj)
- [Dependency resolution](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/snapshots/2026-10-30-5e22343/files/POSSampleApp/POSSampleApp.xcodeproj/project.xcworkspace/xcshareddata/swiftpm/Package.resolved)
- [TEST notice and documentation links](../../../../raw/github/adyen/adyen-pos-mobile-ios-test/snapshots/2026-10-30-5e22343/files/README.md)

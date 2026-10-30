---
title: "GitHub: adyen/adyen-pos-mobile-ios"
type: source
date_ingested: 2026-10-30
date_updated: 2026-10-30
original_format: github-repo
raw_files:
  - "github/adyen/adyen-pos-mobile-ios/snapshots/2026-10-30-689bdbd/manifest.json"
tags: [adyen, mobile-pos, ios, tap-to-pay, card-reader, terminal-api, swiftui, github-repository]
---

## Overview

Initial full baseline for `AdyenPOS@3.22.0`, repository `adyen/adyen-pos-mobile-ios`, tag `v3.22.0`, exact SHA `689bdbdd7197545fbf15160ea64461a53b02b432`. Released 2026-10-27, collected and ingested 2026-10-30. This is a merchant iOS POS app integration for Tap to Pay on iPhone and NYC1 readers, not Adyen's online-checkout iOS SDK.

All 30 assigned paths were read in full: 27 retained files (seven Swift files; 50,860 bytes), snapshot manifest, release manifest and notes. Both packet files were also read. There is no prior collected baseline or comparison; baseline architecture below is not attributed as newly introduced in 3.22.0. Later ingests must append package-qualified knowledge without replacing this baseline.

## Key takeaways

- Package.swift distributes four TEST/LIVE binary products; SDK implementation and downloaded XCFrameworks are outside this capsule.
- SwiftUI and UIKit share the same model, Terminal API payment request and PaymentService; presentation differs by UI framework.
- Backend registration is deliberately incomplete in the sample: the setupToken described in comments is not forwarded by its code.
- Both sample targets select the TEST product. The sample's target settings, entitlement file and dependency lock are evidence of configuration, not successful provisioning or live enablement.
- Release notes announce language/UI changes and a version-specific NYC1 PIN expiry. README documentation links still name 3.21.0.

## Distribution and Dependency Identity

Package name is `AdyenPOS`, with Swift tools 5.6. Products are `AdyenPOSTEST`, `ADYPOSTEST`, `AdyenPOSLIVE` and `ADYPOSLIVE`; each ADYPOS product includes its matching AdyenPOS target. Four binaryTarget declarations reference version 3.22.0 Test/Live CDN ZIPs with separate checksums. These are declared checksums, not proof this ingest downloaded or verified the binaries, signatures or runtime internals. The root manifest has no package dependencies; the sample project separately depends on TerminalAPIKit.

Both sample app targets link `AdyenPOSTEST` and TerminalAPIKit. The project allows the Terminal API dependency from 1.0.0 up to the next major; Package.resolved records `adyen-terminal-api-ios@1.3.0`, revision `f3fb9e4f7ff80077db093858db94e4f5ccfaa944`. That lock is a recorded resolution, not an immutable requirement that every future resolve must choose 1.3.0. The other repository owns the message models and Coder implementation; no dependency implementation was collected here.

## Shared Transaction Flow

`MainViewModel` owns a lazy `PaymentService(delegate: self)`. Its comments require strong retention of both the service and delegate, because the service's delegate is weak. UIKit's scene owns its controller/model; SwiftUI constructs its model from the app and passes it to the view. The sample is not a demonstrated lifecycle/concurrency guarantee for every host application.

Transaction initiation reads `paymentService.installationId`, builds a TerminalAPIKit `Message<PaymentRequest>`, obtains `getPaymentInterface(with:)` for the selected interface and awaits `performTransaction`. Request data is encoded with `Coder.encode` and wrapped in `Payment.Request`. The response is printed; errors are caught and printed. No final-status parsing, server-side reconciliation, reversal/refund, duplicate-request protection or production fulfillment workflow is implemented by these samples.

The example header uses protocolVersion 3.0, service/payment/request message classification, a six-character UUID prefix as serviceIdentifier, a UUID saleIdentifier and installationId as poiIdentifier. The body uses another UUID/time sale transaction and fixed USD 50. Those are demonstration values, not an amount/currency eligibility rule or a proven identifier-uniqueness strategy. Example payment construction alone does not establish additional Terminal API operation support.

## SwiftUI, UIKit and Device Management

SwiftUI's Tap to Pay and Card Reader buttons call the shared flow with `.tapToPay` or `.cardReader` and `.viewModifier`. The view applies `.transactionModal(with: viewModel.paymentService, logo: nil)`; device management appears in a sheet using DeviceManagementView. `.task(viewModel.initializePOSSDK)` starts initialization.

UIKit invokes the same interfaces using `.presentingViewController(self, logo: nil)`, and presents DeviceManagementViewController for reader management. viewDidLoad launches initialization. The reader-management UI is described as necessary for NYC1 integrations, not for Tap to Pay alone.

Initialization assigns the device-manager delegate and calls `try? await paymentService.warmUp()`: warm-up failure is swallowed. All four custom device callbacks are empty. These hooks demonstrate where an app can implement custom reader management; they do not implement discovery/error UX, robust retry or payment readiness state. Buttons do not add an explicit single-transaction/in-flight guard, and SDK-internal serialization is not inspectable here.

## Backend Registration and Sample Contradiction

The PaymentServiceDelegate method is `register(with setupToken: String) async throws -> String`. Comments instruct the app to call its merchant backend, supply setupToken and have that backend call `/sessions`; the app must not call that provider endpoint directly. The response structure contains sdkData, returned to the SDK.

> [!warning] Contradiction
> The comment requires forwarding setupToken, but the retained implementation creates a URLRequest from a placeholder backend address and never places setupToken into a body, header or query. It adds no explicit backend authentication, request method/body or HTTP-status check, and discards the URLSession response metadata. A failed URL construction returns an empty string. This is an unfinished integration template, not a working backend-session implementation. [[adyen-mobile-pos]] carries the reciprocal warning.

Transport/JSON decoding errors can throw, but an HTTP error is not explicitly classified before decoding. An app needs a real authenticated backend contract, setup-token propagation and appropriate response handling. Exact provider request fields, SDK session recovery and production security behavior require their own version-qualified evidence; they are not inferred from this placeholder.

## Build and Provisioning Boundaries

All four app target Debug/Release configurations set iOS 18.4; the two project-level configurations still say 17.0. Target settings must not be collapsed into an SDK-wide minimum, nor the project default treated as an overriding app minimum. Root Swift tools 5.6 and sample SWIFT_VERSION 5.0 are separate metadata from the release's stated Xcode build toolchain.

The retained entitlement file declares `com.apple.developer.proximity-reader.payment.acceptance=true`, but the project does not explicitly set CODE_SIGN_ENTITLEMENTS. File presence is not evidence of an applied signing entitlement or Apple approval. UIKit Info.plist declares Bluetooth and camera usage descriptions; the SwiftUI target uses generated Info.plist settings and this capsule does not establish equivalent permission strings there. Host provisioning and both target configurations require review before execution. The shared scheme targets UIKit; no app build, dependency resolution, SDK execution or physical-device test was performed.

## Release `AdyenPOS@3.22.0`: Announcements

- Adds Catalan, Croatian, Czech, Estonian, Icelandic, Japanese, Latvian, Lithuanian, Romanian and Russian.
- Uses the device OS language when the app language is unsupported before falling back to English.
- Makes close-button presentation consistent across transaction, pairing and device-management screens on iOS 26.
- Fixes primary-language labels and an initial app-language flash in payment UI.
- Notes Xcode 26.3 and NYC1 PIN support expiry on 2027-04-13.

These are upstream release statements; the binary implementation was not audited. The expiry is scoped to this release's NYC1 PIN support, not an assertion that all functionality or Tap to Pay expires on the same date.

## Evidence Limits and Query Routing

The retained README points to 3.21.0 developer documentation/tutorials despite the 3.22.0 package manifest. Preserve that mismatch. The bundled DocC archive was intentionally left outside the approved capsule and supplies no current-version facts here. No public SDK headers/interfaces or binary contents were retained. Packet evidence_gaps being empty means the configured collection scope is complete, not that every integration question is answered.

For detailed APIs, device/iOS availability, countries/methods, session fields, refunds/status/offline behavior or later changes, read the corresponding version-qualified source first; use a separately approved documentation or exact-SHA supplement collection when evidence is missing. Website build guides remain separately dated evidence. No new eligibility, certification, provisioning, live-payment success or current-version replacement of older website knowledge is claimed. A passing mention of other SDKs does not warrant a cross-company comparison page.

## Grounding Quotes

Locations below are inside this snapshot's files/ directory.

1. `name: "AdyenPOS",` — Package.swift:7.
2. `lazy var paymentService = PaymentService(delegate: self)` — POSSampleApp/SampleAppSwiftUI/MainViewModel.swift:17.
3. `try? await paymentService.warmUp()` — same file:59.
4. `let request = URLRequest(url: url)` — same file:104, read with setupToken contract at 100-103.
5. `IPHONEOS_DEPLOYMENT_TARGET = 18.4;` — POSSampleApp/POSSampleApp.xcodeproj/project.pbxproj:306; all target settings read with project-level 17.0 at 456/510.

## Related

- Company: [[adyen]]
- Concept: [[adyen-mobile-pos]]
- History: [[changelog-github-adyen-pos-mobile-ios]]
- Separate online SDK: [[adyen-ios-sdk]]
- Dated website route: [[source-adyen-docs-point-of-sale-mobile-ios-build]]

## Raw Sources

- [Exact-SHA snapshot inventory](../../../../raw/github/adyen/adyen-pos-mobile-ios/snapshots/2026-10-30-689bdbd/manifest.json)
- [Release identity](../../../../raw/github/adyen/adyen-pos-mobile-ios/releases/adyenpos/3.22.0/2026-10-30/manifest.json)
- [Release notes](../../../../raw/github/adyen/adyen-pos-mobile-ios/releases/adyenpos/3.22.0/2026-10-30/release-notes.md)
- [Distribution manifest](../../../../raw/github/adyen/adyen-pos-mobile-ios/snapshots/2026-10-30-689bdbd/files/Package.swift)
- [Shared transaction/session model](../../../../raw/github/adyen/adyen-pos-mobile-ios/snapshots/2026-10-30-689bdbd/files/POSSampleApp/SampleAppSwiftUI/MainViewModel.swift)
- [SwiftUI presentation](../../../../raw/github/adyen/adyen-pos-mobile-ios/snapshots/2026-10-30-689bdbd/files/POSSampleApp/SampleAppSwiftUI/MainView.swift)
- [UIKit presentation](../../../../raw/github/adyen/adyen-pos-mobile-ios/snapshots/2026-10-30-689bdbd/files/POSSampleApp/SampleAppUIKit/MainViewController.swift)
- [Build configuration](../../../../raw/github/adyen/adyen-pos-mobile-ios/snapshots/2026-10-30-689bdbd/files/POSSampleApp/POSSampleApp.xcodeproj/project.pbxproj)
- [Recorded dependency resolution](../../../../raw/github/adyen/adyen-pos-mobile-ios/snapshots/2026-10-30-689bdbd/files/POSSampleApp/POSSampleApp.xcodeproj/project.xcworkspace/xcshareddata/swiftpm/Package.resolved)
- [README and documentation links](../../../../raw/github/adyen/adyen-pos-mobile-ios/snapshots/2026-10-30-689bdbd/files/README.md)

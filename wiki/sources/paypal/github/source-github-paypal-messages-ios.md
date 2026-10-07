---
title: "GitHub: paypal/paypal-messages-ios"
type: source
date_ingested: 2026-04-14
date_updated: 2026-10-07
original_format: github-repo
raw_files:
  - "github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/manifest.json"
  - "github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/manifest.json"
  - "github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/manifest.json"
  - "github-paypal-messages-ios.md"
tags: [paypal, ios, swift, messaging, pay-later, paypal-credit, uikit, swiftui, github-repository]
---

## Overview

`paypal/paypal-messages-ios` is PayPal's standalone native iOS package for rendering promotional Pay Later and PayPal Credit messages. The latest ingested release is package-qualified `paypal-messages-ios@2.0.0` at exact SHA `e3ee08c5310096457ea709f49b8b22b6b385a916`. The approved `1.2.0` baseline at `432d6b832714b2615106c3f2a748ac61654d8bbd` remains preserved below.

This package displays financing messages and a learn-more/application modal. It is not a checkout SDK: the retained source does not create, approve, authorize, or capture a payment.

Repository: <https://github.com/paypal/paypal-messages-ios>

## Evidence Boundary

- The capsule retains 66 source, demo, build, documentation, and release-history files. Tests, fixtures, and binary artwork are excluded by policy.
- The managed `1.2.0` capsule uses the same exact SHA as the April 2026 manual collection. That earlier source and raw stub remain preserved; the October collection adds the independently retained `2.0.0` release.
- Public API and source establish integration behavior, not merchant approval, buyer eligibility, geography, or the offer PayPal will return for a transaction.
- `2.0.0` is the latest ingested release. The October 7 tag check found it as the latest stable tag; this is not a perpetual latest-upstream guarantee.
- The untagged `develop` commit `fdd1868` changes only `README.md`. It is documentation-policy evidence, not a package release or proof of a code-level compatibility change.

## Grounding Excerpts

> "This package facilitates rendering PayPal messages to promote offers such as Pay Later and PayPal Credit to customers."
>
> `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/files/README.md:3`

> "This messaging component is intended for use with the Braintree SDK only."
>
> `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/files/README.md:5`

> "Consumer's country (Integrations must be approved by PayPal to use this option)"
>
> `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/files/Sources/PayPalMessages/Config/PayPalMessageConfig.swift:19`

> "Changing its value will cause the message content being refetched always."
>
> `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/files/Sources/PayPalMessages/PayPalMessageView.swift:164`

> "Function invoked when a user has begun the PayPal Credit application"
>
> `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/files/Sources/PayPalMessages/Delegates/PayPalMessageDelegates.swift:15`

## Requirements and Distribution

`1.2.0` requires iOS 14+, Swift 5.8+, and Xcode 14.3+. It supports CocoaPods, Swift Package Manager, and Carthage. The public view is UIKit-based and provides `PayPalMessageView.Representable` for SwiftUI.

At released baseline `1.2.0`, the README recommended integrating through the broader [[source-github-paypal-ios|PayPal iOS SDK]]. Untagged `develop` commit `fdd1868` removes that recommendation and instead says the component is intended only for the Braintree SDK: merchants must have a Braintree account and integrate the Braintree SDK, while PPCP SDK integrations are unsupported.

> [!warning] Versioned policy boundary
> At the August ingest, the Braintree-only statement was evidenced only on untagged `develop@fdd1868`. The newly retained `2.0.0` README includes it in a tagged release. Preserve the earlier boundary as documentation history; neither the README-only commit nor the retained v2 implementation diff establishes a new runtime account-enforcement mechanism.

## Major Version 2 - `paypal-messages-ios@2.0.0`

Released September 10, 2026; collected and fully ingested October 7, 2026. The complete assigned 66-file capsule was read, not the entire upstream repository. Against `1.2.0`, six retained files changed and 60 are hash-identical. All twelve upstream changed paths have a packet disposition; Carthage metadata, Xcode project files and a test mock remain outside the reviewed capsule.

### Requirements and Merchant Policy

| Requirement | Historical `1.2.0` | `2.0.0` |
| --- | --- | --- |
| Minimum iOS | 14.0 | 15.0, enforced in retained SPM and CocoaPods configuration |
| Swift / Xcode | Swift 5.8+ / Xcode 14.3+ | Same documented minimums |
| README integration guidance | Recommended the PayPal iOS SDK | Requires a Braintree account and Braintree SDK integration; PPCP SDK integrations unsupported |

The tagged v2 README carries the earlier `fdd1868` policy. `2.0.0` is the first retained managed release containing this statement; the snapshot evidence distinguishes a released integration policy from proof of code-level account validation. The changelog attributes the disclaimer to the same documentation commit. Keeping v1 for iOS 14 compatibility does not itself prove current merchant eligibility or support under the newer policy.

### Implementation and Migration

- `Package.swift` selects the `2.0.0` binary release URL, updates its checksum and raises `.iOS(.v14)` to `.iOS(.v15)`. `PayPalMessages.podspec` advances its version and iOS floor as well. The release notes report matching Xcode project updates; those excluded projects were not read as raw implementation evidence.
- `BuildInfo.version` advances to `2.0.0`. Existing request, modal and analytics code consumes this value, so outgoing version attribution changes without new APIs in those files.
- `Environment.swift` replaces `if case .develop(_, let devTouchpoint, let stageTag)` with the equivalent combined-binding syntax `if case let .develop(_, devTouchpoint, stageTag)`. The retained patch shows no endpoint or query-selection change.
- Configuration, public views, delegates, message/modal request logic, merchant-profile caching, rendering, analytics implementation and retained demos are unchanged. No new messaging feature or checkout-payment API is established by the retained changes.
- The existing `setConfig` omission of `environment`, `merchantID` and `partnerAttributionID` remains in `2.0.0`. Set the public properties explicitly or rebuild the view when these contexts change; upgrading does not fix this risk.
- Before adopting v2, raise the app's supported iOS floor, confirm the documented Braintree integration prerequisites and test the exact packaged artifact. The SPM checksum is retained metadata, not proof that the binary was downloaded, built or exercised; no device/runtime QA was performed.

### Version 2 Grounding Excerpts

> "you must have a Braintree account and the Braintree SDK integrated. PPCP SDK integrations are not supported."
>
> `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/README.md:5`

> `platforms: [.iOS(.v15)],`
>
> `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/Package.swift:8`

> `s.platform        = :ios, "15.0"`
>
> `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/PayPalMessages.podspec:11`

> `public internal(set) static var version: String = "2.0.0"`
>
> `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/Sources/PayPalMessages/Enums/BuildInfo.swift:5`

## Major Version 1 - Preserved Integration Knowledge

The following configuration, rendering, modal, demo and privacy description was grounded at `1.2.0`. The corresponding retained implementation is unchanged at `2.0.0`, except for the version attribution and equivalent environment pattern binding noted above; deployment and merchant-policy boundaries are versioned separately.

## Configuration Contract

`PayPalMessageConfig` combines `PayPalMessageData` and `PayPalMessageStyle`.

| Area | Fields |
| --- | --- |
| Merchant identity | required `clientID`; optional partner-only `merchantID` and `partnerAttributionID` |
| Execution | `environment`, `channel`, `ignoreCache` |
| Transaction context | `amount`, `pageType`, `offerType`, `buyerCountry` |
| Localization | `language`, `locale` |
| Presentation | `logoType`, `color`, `textAlign` |

Standard and partner initializers are separate. `buyerCountry` is not a general override: its source comment says integrations require PayPal approval to use it.

Supported preferred offers are short-term Pay Later, long-term Pay Later, Pay in 1, and PayPal Credit no-interest. Page types cover home, product listing, product details, cart, mini-cart, checkout, and search results. The service may still return a generic message, so a preferred offer is not an eligibility guarantee.

## Rendering and Update Lifecycle

Creating `PayPalMessageView` triggers a message fetch. Changes to identity, environment, amount, placement, offer, buyer country, localization, logo type, channel, or cache policy queue a refetch. Color and alignment changes only rerender the retained response.

`setConfig` always queues a refetch, but its exact `1.2.0` implementation does not copy `environment`, `merchantID`, or `partnerAttributionID` from the replacement config. It is therefore not a complete environment or partner-identity replacement. Set those public view properties explicitly or rebuild the view when that context changes; do not assume `setConfig` alone applies them.

Before requesting content, the SDK retrieves and caches a merchant-profile hash by client ID plus merchant ID. A hard TTL forces refresh; crossing the soft TTL returns cached data while refreshing in the background. A disabled merchant profile suppresses the hash.

The message request sends transaction and integration context to `/credit-presentment/native/message`. HTTP 200 responses are decoded into message text, disclaimer/link text, offer/product group, logo placement, modal close-button configuration, language, and tracking data. Errors expose an optional PayPal debug ID, issue, and description through `PayPalMessageError`.

## Interaction and Modal

`PayPalMessageViewStateDelegate` reports loading, success, and error. `PayPalMessageViewEventDelegate` reports message click and the start of a PayPal Credit application.

The modal delegate surface reports show, close, in-modal link click, and calculator submission events. Wrapper and partner integrations can identify themselves globally with `PayPalMessageConfig.setGlobalAnalytics(integrationName:integrationVersion:)`; this is analytics attribution, not payment attribution or merchant enablement.

Tapping a successfully rendered message opens a bottom-sheet-style `WKWebView` modal. The modal carries the same merchant and transaction context, emits show/close/click/calculation events internally, opens external links in `SFSafariViewController`, and supports reloading when language or locale changes. The message is noninteractive until content renders successfully.

## UIKit and SwiftUI Integration

The demo contains equivalent UIKit and SwiftUI configuration surfaces. Both debounce input changes, rebuild the message configuration, and display loading, success, error, click, and apply state. The SwiftUI path wraps the UIKit control with `UIViewRepresentable`; it is not an independent SwiftUI rendering engine.

## Styling, Localization, and Accessibility

Logo styles are inline, primary, alternative, or text-only. Colors are black, white, monochrome, or grayscale, and alignment is left, center, or right. The renderer chooses PayPal or PayPal Credit artwork from the returned product group, replaces a server-provided logo placeholder, adds an underlined learn-more link, and supports Dynamic Type.

`1.2.0` adds bold rendering for server message substrings delimited by `%bold%`. It also records both requested and rendered language in analytics. Accessibility output substitutes readable branding for logo placeholders, labels the whole message as a button, and gives the modal close control alternative text.

## Analytics and Privacy

The SDK batches render, click, error, and modal events into CloudEvents every five seconds. Payload context can include client ID, optional merchant and partner IDs, merchant-profile hash, amount, page type, country, requested/rendered language, style, integration identity, and timing. The logging request derives a Basic authorization value from the client ID.

The included privacy manifest declares UserDefaults access for app functionality and says tracking is not used. This repository evidence should still be reviewed against the merchant application's own privacy disclosures.

## Version History Boundary

The retained changelog establishes the stable `1.0.0`, `1.1.0`, `1.2.0` and `2.0.0` history. Only `1.2.0` and `2.0.0` have immutable managed release snapshots; earlier releases remain cumulative context. See [[changelog-github-paypal-messages-ios]].

The separate untagged `432d6b8` to `fdd1868` comparison records the later Braintree-only documentation policy without fabricating a package version.

## Related

- Company: [[paypal]]
- Product concept: [[paypal-pay-later]]
- Parent mobile SDK: [[paypal-ios-sdk]]
- Android counterpart: [[source-github-paypal-messages-android]]
- Cross-platform analysis: [[analysis-paypal-messages-ios-vs-android]]
- Release history: [[changelog-github-paypal-messages-ios]]

## Raw Sources

- `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/manifest.json` - full assigned v2 source capsule, 66 retained files
- `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/2.0.0/2026-10-07/manifest.json` - package-qualified release identity
- `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/2.0.0/2026-10-07/release-notes.md` - major migration and documentation history
- `tracking/github/repos/paypal/paypal-messages-ios/comparisons/paypal-messages-ios/1.2.0--2.0.0/comparison.json` - retained capsule comparison metadata
- `tracking/github/repos/paypal/paypal-messages-ios/comparisons/paypal-messages-ios/1.2.0--2.0.0/diff.patch` - six retained changed files; full upstream dispositions are in the ingest packet
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/README.md` - released Braintree-only policy and toolchain requirements
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/Package.swift` - iOS 15 floor and versioned binary target
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/PayPalMessages.podspec` - CocoaPods iOS 15 floor
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/Sources/PayPalMessages/Enums/BuildInfo.swift` - v2 version attribution
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/Sources/PayPalMessages/Enums/Environment.swift` - equivalent development pattern binding
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-10-07-e3ee08c/files/Sources/PayPalMessages/PayPalMessageViewModel.swift` - unchanged configuration replacement risk
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/manifest.json` - untagged `develop` documentation-policy snapshot
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/files/README.md` - Braintree-account, Braintree-SDK, and PPCP-support boundary
- `tracking/github/repos/paypal/paypal-messages-ios/comparisons/default-branch/432d6b8--fdd1868/comparison.json` - exact ref comparison metadata
- `tracking/github/repos/paypal/paypal-messages-ios/comparisons/default-branch/432d6b8--fdd1868/diff.patch` - README-only patch
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/manifest.json` - exact-SHA bounded source capsule
- `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/1.2.0/2026-08-12/manifest.json` - package-qualified release record
- `raw/github/paypal/paypal-messages-ios/releases/paypal-messages-ios/1.2.0/2026-08-12/release-notes.md` - exact `1.2.0` release notes
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/files/CHANGELOG.md` - cumulative upstream release history
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/files/README.md` - requirements and integration boundary
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/files/Sources/PayPalMessages/Config/PayPalMessageConfig.swift` - public configuration API
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/files/Sources/PayPalMessages/PayPalMessageView.swift` - UIKit and SwiftUI view contract
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/files/Sources/PayPalMessages/PayPalMessageViewModel.swift` - fetch and render lifecycle
- `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/files/Sources/PayPalMessages/PayPalMessageModalViewModel.swift` - modal URL and event bridge
- `raw/github-paypal-messages-ios.md` - legacy April 2026 collection stub for the same exact SHA

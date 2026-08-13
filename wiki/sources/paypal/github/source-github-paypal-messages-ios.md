---
title: "GitHub: paypal/paypal-messages-ios"
type: source
date_ingested: 2026-04-14
date_updated: 2026-08-13
original_format: github-repo
raw_files:
  - "github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/manifest.json"
  - "github/paypal/paypal-messages-ios/snapshots/2026-08-12-432d6b8/manifest.json"
  - "github-paypal-messages-ios.md"
tags: [paypal, ios, swift, messaging, pay-later, paypal-credit, uikit, swiftui, github-repository]
---

## Overview

`paypal/paypal-messages-ios` is PayPal's standalone native iOS package for rendering promotional Pay Later and PayPal Credit messages. The approved baseline is package-qualified `paypal-messages-ios@1.2.0` at exact SHA `432d6b832714b2615106c3f2a748ac61654d8bbd`.

This package displays financing messages and a learn-more/application modal. It is not a checkout SDK: the retained source does not create, approve, authorize, or capture a payment.

Repository: <https://github.com/paypal/paypal-messages-ios>

## Evidence Boundary

- The capsule retains 66 source, demo, build, documentation, and release-history files. Tests, fixtures, and binary artwork are excluded by policy.
- The managed capsule uses the same exact SHA as the April 2026 manual collection. This page migrates that earlier source into the canonical hierarchy and preserves its raw stub; it does not represent a newer upstream release.
- Public API and source establish integration behavior, not merchant approval, buyer eligibility, geography, or the offer PayPal will return for a transaction.
- `1.2.0` is the latest ingested release, not a claim that it remains latest upstream.
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

> [!warning] Untagged policy boundary
> This Braintree-only statement is present on `develop` after `1.2.0`, not in a collected semantic release. Treat it as the current repository documentation policy at `fdd1868`, while retaining `1.2.0` behavior as released history. Because only `README.md` changed, the evidence does not establish a code-level compatibility change or the first package version enforcing the policy.

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

The retained changelog establishes the stable `1.0.0`, `1.1.0`, and `1.2.0` history, but only `1.2.0` has an immutable managed release snapshot. See [[changelog-github-paypal-messages-ios]].

The separate untagged `432d6b8` to `fdd1868` comparison records the later Braintree-only documentation policy without fabricating a package version.

## Related

- Company: [[paypal]]
- Product concept: [[paypal-pay-later]]
- Parent mobile SDK: [[paypal-ios-sdk]]
- Android counterpart: [[source-github-paypal-messages-android]]
- Cross-platform analysis: [[analysis-paypal-messages-ios-vs-android]]
- Release history: [[changelog-github-paypal-messages-ios]]

## Raw Sources

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

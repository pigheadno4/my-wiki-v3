---
title: "GitHub: paypal/paypal-messages-android"
type: source
date_ingested: 2026-04-14
date_updated: 2026-08-12
original_format: github-repo
raw_files:
  - "github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/manifest.json"
  - "github-paypal-messages-android.md"
tags: [paypal, android, kotlin, messaging, pay-later, paypal-credit, views, compose, github-repository]
---

## Overview

`paypal/paypal-messages-android` is PayPal's standalone native Android library for rendering promotional Pay Later and PayPal Credit messages. The approved baseline is package-qualified `paypal-messages-android@1.3.0` at exact SHA `f1aa138cc6822cc11d68ac4bfdee3cf183aedbc2`.

The library fetches a financing message, renders it in a native view, and opens a web-backed learn-more/application modal. It is not a checkout SDK: the retained source does not create, approve, authorize, or capture a payment.

Repository: <https://github.com/paypal/paypal-messages-android>

## Evidence Boundary

- The capsule retains 123 source, demo, resource, build, documentation, and release-history files. Tests and fixtures are excluded by policy.
- This managed SHA differs from the April 2026 manual collection at `1d2238c9e5ec3564ad5d8060c474e008ab7bf779`. The old raw stub is preserved, but current behavior is grounded in the managed `f1aa138` capsule.
- The README says the library is still in development and recommends sandbox use until an official release is available. A stable tag and publication automation do not establish general availability.
- `1.3.0` is the latest ingested release, not a claim that it remains latest upstream.
- Public offer enums and buyer-country inputs do not establish merchant approval, buyer eligibility, geography, or the offer PayPal will return.

## Grounding Excerpts

> "We recommend using the library in the sandbox environment until an official release is available."
>
> `raw/github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/files/README.md:16`

> "The PayPalMessages Library is available for Android SDK 23+."
>
> `raw/github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/files/README.md:22`

> "The Jetpack view does not currently work to show PayPalMessages"
>
> `raw/github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/files/DEVELOPMENT.md:46`

> `this.onApply = config.events?.onClose ?: {}`
>
> `raw/github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/files/library/src/main/java/com/paypal/messages/ModalFragment.kt:396`

## Requirements and Distribution

The README sets Android SDK 23+ and says the library is published to Maven Central. The retained build identifies group `com.paypal.messages` and artifact `paypal-messages`, but its version sources conflict with the release record: the GitHub tag is `1.3.0`, root Gradle metadata says `1.1.14`, and the checked-in POM says `1.1.10`. Verify the live Maven coordinate/version before installation rather than inferring `com.paypal.messages:paypal-messages:1.3.0` from this capsule alone.

License evidence also conflicts: the repository `LICENSE` file is MIT, while Gradle/POM publication metadata declares Apache License 2.0. The capsule cannot resolve which license governs a distributed artifact.

## Configuration Contract

`PayPalMessageConfig` combines message data, style, view-state callbacks, and event callbacks.

| Area | Fields |
| --- | --- |
| Merchant identity | required `clientID`; optional partner `merchantID` and `partnerAttributionID` |
| Execution | `environment` (`SANDBOX`, `LIVE`, or development variants) |
| Transaction context | `amount`, `buyerCountry`, `offerType`, `pageType` |
| Localization | typed `PayPalLanguage` and `PayPalLocale` |
| Presentation | logo type, color, and text alignment |
| View state | `onLoading`, `onSuccess`, `onError` |
| Message events | `onClick`, `onApply` |

Preferred offers are short-term Pay Later, long-term Pay Later, Pay in 1, and PayPal Credit no-interest. Page types cover home, product listing, product details, cart, mini-cart, checkout, and search results. These are request preferences; the response can still select another or generic message.

XML attributes expose client ID, amount, buyer country, offer/page type, logo, color, and alignment. Programmatic configuration exposes the broader contract. Unlike the iOS source, this Android capsule does not document buyer-country override approval, so the field's presence must not be treated as permission to use it.

## Rendering and Update Lifecycle

`PayPalMessageView` is a `FrameLayout` backed by a `TextView`. It retrieves merchant-profile data, calls the native message endpoint, renders server text and branding, and enables click behavior after successful content. Loading, success, and error callbacks report the view lifecycle.

Public property changes trigger a debounced content update. Style output supports primary, alternative, inline, or text-only branding; black, white, monochrome, or grayscale colors; and left, center, or right alignment. The resource capsule includes both PayPal and PayPal Credit logo variants.

`1.3.0` adds bold rendering for server substrings marked with `%bold%` and records rendered language in analytics. These changes affect presentation and telemetry, not payment execution.

## Modal and Callbacks

Tapping a rendered message opens a bottom-sheet/modal WebView. AppCompat activities use `ModalFragment`; other contexts use `PayPalModalActivity`. The modal emits show, close, click, calculation, and application-start events, and opens external links with an Android view intent. Production SSL errors are cancelled; the development build may bypass them.

The exact `1.3.0` source has two callback risks:

- `ModalFragment.init()` assigns `config.events.onClose` to both `onClose` and `onApply`. On the fragment path, an Apply action can therefore invoke the close callback instead of the merchant's apply callback.
- `ModalDisplayManager` starts `PayPalModalActivity` before registering callbacks in its static registry. Because the activity reads that registry in `onCreate`, callback delivery has an ordering race; the capsule does not prove that every launch loses callbacks.

These are version-qualified source findings, not confirmed production incident reports.

## Configuration and Shared-State Risks

`PayPalMessageView.setConfig()` copies identity, transaction, localization, style, and callbacks but does not copy `config.data.environment`. A caller changing environments through a full config replacement can therefore leave the view on its previous environment.

Merchant-profile cache storage is one application-wide SharedPreferences record rather than a record keyed by client or merchant ID. The analytics logger is also a singleton with a mutable static client ID, and the API layer holds mutable global environment/debug fields. Multiple differently configured message views in one process can therefore share or overwrite state. Treat this as a concurrency/integration risk and isolate configuration until a later release demonstrates otherwise.

## Views and Jetpack Compose

The public `PayPalComposableMessage` wraps `PayPalMessageView` with Compose `AndroidView`; it is not an independent renderer. Source comments recommend falling back to the standard view if compatibility issues occur. More importantly, the retained `DEVELOPMENT.md` leaves the Jetpack run instructions commented out and explicitly says the Jetpack view does not currently work. Demo source presence is not readiness evidence.

For this baseline, the XML/AppCompat path is the better-evidenced integration path, subject to the fragment callback defect above.

## Analytics and Caching

The SDK batches render, click, error, and modal events for five seconds before sending CloudEvent-style analytics. Context can include client ID, partner identifiers, merchant-profile hash, amount, placement, buyer country, requested/rendered language, style, integration identity, and timing.

Merchant-profile data uses soft and hard TTL behavior: fresh cache is reused, soft-expired cache is reused while refreshed, hard-expired cache is replaced before use, and a server flag can disable the cache flow. Because Android stores one unkeyed record, this lifecycle is not equivalent to the iOS cache keyed by client and merchant identity.

## Version History Boundary

The retained cumulative changelog establishes stable history from `1.0.0` through `1.1.0`, while the managed release record establishes `1.3.0` and compares it to `1.2.0`. Only `1.3.0` has an immutable managed release snapshot. See [[changelog-github-paypal-messages-android]].

## Related

- Company: [[paypal]]
- Product concept: [[paypal-pay-later]]
- Android checkout SDK: [[paypal-android-sdk]]
- iOS counterpart: [[source-github-paypal-messages-ios]]
- Cross-platform analysis: [[analysis-paypal-messages-ios-vs-android]]
- Release history: [[changelog-github-paypal-messages-android]]

## Raw Sources

- `raw/github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/manifest.json` - exact-SHA bounded source capsule
- `raw/github/paypal/paypal-messages-android/releases/paypal-messages-android/1.3.0/2026-08-12/manifest.json` - package-qualified release record
- `raw/github/paypal/paypal-messages-android/releases/paypal-messages-android/1.3.0/2026-08-12/release-notes.md` - exact `1.3.0` release notes
- `raw/github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/files/CHANGELOG.md` - cumulative upstream release history
- `raw/github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/files/README.md` - availability and Android requirement
- `raw/github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/files/library/src/main/java/com/paypal/messages/PayPalMessageView.kt` - public view and configuration lifecycle
- `raw/github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/files/library/src/main/java/com/paypal/messages/ModalFragment.kt` - AppCompat modal and callback mapping
- `raw/github/paypal/paypal-messages-android/snapshots/2026-08-12-f1aa138/files/library/src/main/java/com/paypal/messages/data/ModalDisplayManager.kt` - modal dispatch and callback registry
- `raw/github-paypal-messages-android.md` - legacy April 2026 collection stub

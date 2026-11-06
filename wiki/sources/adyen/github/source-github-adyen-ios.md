---
title: "GitHub: Adyen/adyen-ios"
type: source
date_ingested: 2026-10-15
date_updated: 2026-11-07
original_format: github-repo
raw_files:
  - "github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/manifest.json"
  - "github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-11-07/manifest.json"
  - "github/adyen/adyen-ios/snapshots/2026-10-14-da34749/manifest.json"
  - "github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/manifest.json"
tags: [adyen, ios, swift, mobile-sdk, drop-in, components, github-repository]
---

## Overview

`Adyen/adyen-ios` contains Adyen's modular native iOS checkout SDK. It provides an all-in-one Drop-in, individual payment Components, Session orchestration, follow-up action handling, card and bank-detail encryption, and optional integrations for Apple Pay, Cash App Pay, Twint, WeChat Pay, card scanning, and delegated authentication. This cumulative page begins with package-qualified release `adyen-ios@5.25.1` at exact SHA `5f6779b31299e3067de3a5279a816f3b8d2fbdf3`.

Repository: <https://github.com/Adyen/adyen-ios>

Newest ingested release: `adyen-ios@5.27.0`, published 2026-10-30, exact SHA `15167f660094853d204dc6cd25a068eddf1bc2b2`, ingested 2026-11-07. Its full additive section below preserves the `5.25.1` baseline, `5.26.0` implementation and dated notes correction; new behavior is not retroactively attributed to earlier releases.

## Evidence boundary

- The snapshot proves retained implementation at `adyen-ios@5.25.1`, released on 2026-06-04. It does not establish current product eligibility, merchant enablement, or regional availability.
- Payment-method models and Components are client integration surfaces. The merchant backend or Session response remains authoritative for available methods and transaction results.
- The capsule retains the complete selected SDK and Demo Swift source but excludes tests, generated documentation, media, and binary frameworks by policy.
- Adyen 3DS2, authentication, networking, WeChat Pay, Cash App Pay, and Twint behavior is partly delegated to separately versioned dependencies. This page records Adyen iOS's adapter boundary, not the complete dependency runtime.

## Grounding excerpts

> "iOS Drop-in: an all-in-one solution, the quickest way to accept payments on your iOS app."
>
> `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/README.md:25-27`

> "It can handle the required steps internally such as `/payments` and `/payment/details` calls and partial payment calls"
>
> `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/AdyenSession/AdyenSession.swift:14-17`

> "Please use your own web server between your app and adyen checkout API."
>
> `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/Demo/Configuration.swift:19-20`

> "After receiving a payment response, you must call `finalizeIfNeeded(with:completion:)` regardless of whether the payment succeeded or failed."
>
> `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/AdyenComponents/Apple Pay/ApplePayComponent.swift:44-48`

> "Fixed a layout issue that could affect component's form rendering in cross-platform SDK integrations."
>
> `raw/github/adyen/adyen-ios/releases/adyen-ios/5.25.1/2026-08-01/release-notes.md:3`

## Platform and distribution

The retained README marks the 5.x line active and lists iOS 12, Xcode 15, and Swift 5.7 as minimum requirements. Distribution is available through Swift Package Manager, CocoaPods, and Carthage.

The package is divided into Core, Drop-in, Session, Card, Components, Actions, Encryption, SwiftUI, CardScanner, Cash App Pay, Twint, WeChat Pay, and delegated-authentication products. Swift Package Manager pins Adyen 3DS2 `2.4.4`, Authentication `3.2.0`, Networking `3.0.1`, WeChat Pay `2.2.0`, and Cash App Pay `0.6.2`; Twint is a binary target. CocoaPods and Carthage metadata have their own dependency declarations, so integrations should use the dependency graph of their selected package manager.

## Context and integration modes

Every Component receives an `AdyenContext`, which wraps an `APIContext`, optional payment amount and country, and analytics provider. `APIContext` validates the client key and selects test or region-specific live checkout-shopper endpoints. It is client-side context, not a substitute for merchant server credentials.

Drop-in owns payment-method presentation, selection, detail collection, loading and cancellation state, stored-method removal, partial-payment reloads, and follow-up action routing. Its configuration controls payment-method-specific options, list behavior, styles, localization, Apple Pay, card fields, Cash App Pay, and action handling.

Individual Components expose payment-method-specific UI and return `PaymentComponentData` through delegates. That data includes the payment-method details, amount, optional partial-payment order, storage choice, installments, and SDK metadata. The merchant then submits it through a Session or its own backend flow.

## Session and advanced flow

`AdyenSession` initializes asynchronously from a server-created session ID and session data. The setup response supplies amount, country, locale, payment methods, and server-owned Component configuration. Session acts as the Drop-in or Component delegate and can internally perform payments, additional details, balance checks, order creation and cancellation, and stored-method disabling.

Merchants can take over the Session payments or additional-details step through `AdyenSessionPaymentsHandler` and `AdyenSessionPaymentDetailsHandler`. Otherwise Session processes actions and reports final result codes such as Authorised, Refused, Pending, Cancelled, Error, Received, or PresentToShopper.

The retained advanced-flow demo instead calls payment-method, `/payments`, `/payments/details`, order, balance, and stored-method endpoints through merchant-owned delegates. It passes returned actions into Drop-in and explicitly finalizes the active Component. The demo's direct API-key mode is testing-only; its source recommends a merchant backend for production.

## Payment methods, cards, and storage

The core decodes regular and stored payment methods into typed models, while Drop-in builds a Component only when the corresponding module and required configuration are available. It can render instant, stored, regular, and already-paid groups, preselect a stored method, skip the list when one regular method remains, and remove a stored method through merchant or Session delegates.

The Card Component supports card-brand and BIN detection, co-badged selection, card scanning, holder name, billing address, storage consent, installments, stored-card security code, Korean authentication fields, and Brazilian tax identifiers. Session-owned installment and storage settings override local Card configuration where applicable.

Card data is encrypted field-by-field or as one token with an Adyen-provided public key. ACH Direct Debit similarly encrypts account and routing numbers. Client encryption reduces raw-detail exposure but does not remove the merchant's obligation to use the supported server flow and applicable compliance controls.

Partial-payment support can check gift-card or voucher balance, create an order, reload the available methods against the remaining amount, track already-paid methods, and cancel the order.

## Apple Pay and follow-up actions

`ApplePayComponent` validates device and supported-network availability, wraps `PKPaymentAuthorizationViewController`, and submits the authorized token through the common payment delegate. Configuration covers billing and shipping contacts, shipping methods, coupon codes, card funding source, onboarding, and automatic dismissal. Integrations must call `finalizeIfNeeded` after both successful and failed payment responses so the Apple Pay sheet receives the correct result.

`AdyenActionComponent` dispatches redirect, native redirect, 3DS2 fingerprint and challenge, delegated authentication, SDK, await, voucher, QR-code, and document actions. Redirect flows may use an in-app browser or external application and return details for the next payment-details call. QR-code and await flows use method-specific polling and expiration behavior.

3DS2 is delegated to `Adyen3DS2`, with Adyen iOS coordinating fingerprint submission, challenges, redirects, and optional delegated authentication. The pinned `Adyen3DS2@2.4.4` runtime is independently documented in [[source-github-adyen-3ds2-ios]]; authentication remains a separate dependency boundary.

## Native wallet and app handoffs

Cash App Pay uses its external SDK, a merchant redirect URL, and one-time and optional on-file grants; Session can control whether the storage field appears. Twint submits SDK-mode payment details and requires callback/action configuration backed by its binary SDK. WeChat Pay is unavailable in the simulator, requires configured query schemes, and hands the action to the independently versioned WeChat SDK on a real device.

These modules establish integration adapters. They do not prove that a payment method is enabled for a merchant or that every behavior of the delegated SDK is represented in this source capsule.

## Analytics, privacy, and cross-platform wrappers

Initial analytics record SDK and wrapper version, platform, locale, device and screen characteristics, amount or Session context, and the presented payment methods. Event analytics batch render, interaction, submit, action, validation, and error information; merchants can disable event analytics through `AnalyticsConfiguration`, while the initial request uses the resulting analytics level.

The privacy manifest declares product interaction for analytics and user ID, contact, payment, name, email, phone, and physical-address categories for app functionality. It marks the declared categories as not linked to the user and not used for tracking.

`CheckoutPlatformParams` lets approved wrappers identify iOS, React Native, or Flutter and override the reported wrapper version. The exact `5.25.1` release fixes a Component form-rendering layout issue in cross-platform integrations. Because this is the first retained baseline and the release note names no file, the fix is not attributed to a particular implementation path.

## `5.25.1` release finding

The exact release has one documented fix: Component form layout could render incorrectly when embedded through a cross-platform SDK. The merchant impact is limited to wrapper-hosted form presentation; no API migration or breaking change is documented.

Broader Drop-in, Session, Component, card, action, wallet, analytics, and privacy findings above describe accumulated behavior present at the exact SHA, not changes introduced solely by `5.25.1`.

## `5.26.0` update from `5.25.1`

### Reading and evidence boundary

Approved additive full ingest with the user-approved focused-reading exception: read all 23 added/modified retained files completely, the full cumulative source and changelog, release records/notes, retained-code diff and affected prior code/dependencies. Verified the 686 prior and 689 current files mechanically by hash and size, including 666 unchanged files; large manifest and comparison inventories were checked mechanically rather than claimed as full textual reads. All 7,943 upstream changes have dispositions: 23 retained and 7,920 intentional policy exclusions, largely generated documentation and tests. The packet reports no unclassified change or evidence gap within its configured scope.

This is source inspection, not an SDK build, physical-device, accessibility, Cash App Pay or payment test. An automatic security-review signal is a triage heuristic, not proof of an advisory or exploitable vulnerability. External SDK implementation remains separate.

### Grounding excerpts

> "This is the **last release available through CocoaPods**."
>
> `raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-10-14/release-notes.md:6`

> "which could submit an over-length code while only showing the truncated value."
>
> `raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-10-14/release-notes.md:16`

> `set { applePayComponent.order = newValue }`
>
> `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/AdyenDropIn/Components/PreApplePayComponent.swift:63`

> "Unused. Minor unit digits depend only on the currency code. Kept for API compatibility."
>
> `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Adyen/Formatters/AmountFormatter.swift:32`

### Apple Pay remaining-amount order propagation

The existing `ComponentManager` assigns `paymentComponent.order = order` after building a payment Component. In `5.25.1`, the pre-Apple-Pay wrapper had no explicit forwarding property. In `5.26.0`, its `order` getter/setter delegates to the inner Apple Pay Component. The unchanged Apple Pay submission path includes that order in `PaymentComponentData` alongside token details and amount. This connects the remaining-amount Apple Pay payment to the partial-payment order after, for example, gift-card use. It does not introduce split-payment orchestration, remove merchant-server requirements, or prove authorization/capture success.

Evidence: `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/AdyenDropIn/Components/PreApplePayComponent.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/AdyenDropIn/Utilities/ComponentManager.swift` and `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/AdyenComponents/Apple Pay/ApplePayComponentExtensions.swift`.

### Card security-code value and input handling

The prior `CardSecurityCodeFormatter` truncated only `formattedValue`. `FormTextItem.textDidChange` separately stores `sanitizedValue`, so displayed truncation was not the same as truncating the stored field value. The new formatter overrides sanitization, first normalizing numeric input and then limiting it to four digits for Amex or three for other/unknown brands; formatted output uses the same sanitizer. The view rejects over-limit single-character edits but lets multi-character replacements reach the formatter. Deletion remains permitted.

The shared brand-length helper also feeds placeholders and brand-bound validators. Do not generalize this to every standalone validator: `CardSecurityCodeValidator()` still initializes a three-to-four-digit range; publisher/fixed-brand initializers set the exact brand length. This change bounds the retained field's sanitized value, not overall payment acceptance or a claim that all historical over-length submissions succeeded.

Evidence: `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/AdyenCard/Formatters/CardSecurityCodeFormatter.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/AdyenCard/Form/FormCardSecurityCodeItemView.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/AdyenCard/Validators/CardSecurityCodeValidator.swift` and `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Adyen/UI/Form/Items/Text/FormTextItem.swift`.

### Source-derived currency conversion change

`AmountFormatter` replaces its limited currency override switch and locale-based fraction lookup with `CurrencyMinorDigitsProvider`. The provider uppercases currency codes, uses the retained Adyen table when present, and falls back to system ICU/CLDR currency data otherwise. The table retains Adyen-specific values such as ISK/CLP at two decimals and IDR/CVE at zero. It is not an enabled-currency or merchant-eligibility list.

Major/minor conversions keep `localeIdentifier` in their signatures but no longer use it for decimal-place selection. Formatted display still sets the requested locale. Existing conversion arithmetic remains: the Double overload converts the scaled value to `Int`; the Decimal overload rounds toward zero. This is not a new arbitrary-precision or rounding-guarantee feature. Currency conversion is a code finding not explicitly listed in the release notes.

Evidence: `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Adyen/Formatters/AmountFormatter.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Adyen/Core/Providers/CurrencyMinorDigitsProvider/CurrencyMinorDigitsProvider.swift` and `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Adyen/Core/Providers/CurrencyMinorDigitsProvider/CurrencyMinorDigitsProvider+Data.swift`.

### Adaptive presentation and app-return examples

The release notes announce iPhone Duo support; retained code establishes safe-area and adaptive-layout changes, not independently verified device compatibility. Regular modal toolbars use safe-area constraints while custom navigation bars retain fixed-height constraints. Scroll-enabled forms anchor to content/frame layout guides with explicit horizontal and bottom padding; form/list items set directional margins. Keyboard observation clips against the notification's screen (falling back to the main screen), publishes taller frames immediately, and delays shorter/hidden frames until a 0.15-second quiet interval.

`FormTextItemStyle` changes default inactive title/separator colors to `formTextItemInactive`: light `#757575`, dark `#8E8E93`, with the light fallback before iOS 13. Custom title/separator colors are not replaced; generic `componentSecondaryLabel` and `componentSeparator` remain unchanged. This is not a measured accessibility-compliance result.

The SwiftUI demo handles initial scene URL contexts and subsequent open-URL events through a common helper that forwards to `RedirectComponent` and conditionally posts the Cash App Pay notification. The UIKit AppDelegate adds scene configuration for iOS 13+ and retains its legacy window setup for earlier versions. The new `Demo/UIKit/SceneDelegate.swift` and scene plist changes are outside the configured capsule: full UIKit scene-return wiring is not established by the retained AppDelegate alone. No automatic claim is made about a merchant app adopting the demo changes.

Evidence: `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Adyen/Core/ToolBar/ModalToolbar.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Adyen/UI/Form/FormViewController.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Adyen/Utilities/KeyboardObserver.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Adyen/UI/Form/Items/Text/FormTextItemStyle.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Adyen/UI/Styles/CoreColors.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Demo/SwiftUI/SceneDelegate.swift` and `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Demo/UIKit/AppDelegate.swift`.

### Distribution announcement and retained discrepancy

> [!warning] Contradiction
> The `5.26.0` release notes call this the final CocoaPods release and announce SPM/Carthage distribution afterward, but the same-tag README still advertises CocoaPods and the podspec remains present. Preserve both: the announcement does not mean `5.26.0` is unavailable through CocoaPods, and repository evidence alone does not verify package-registry availability or CocoaPods' broader shutdown schedule. The discrepancy is also recorded in [[adyen-ios-sdk]].

The retained requirements remain iOS 12, Xcode 15 and Swift 5.7; no dependency change is reported by this comparison. Future upgrade planning should account for the announced distribution change without rewriting the historical `5.25.1` installation guidance.

### `5.26.0` release-note correction (2026-11-07 capture)

> [!warning] Contradiction
> The CocoaPods statement and excerpt above describe the original 2026-10-14 capture. The revised `5.26.0` notes collected on 2026-11-07 remove that notice and change the heading from "iPhone Duo and CocoaPods" to "iPhone Duo". Preserve the old capture as history, but do not treat it as the current distribution cutoff. [[adyen-ios-sdk]] records the same dated correction.

This is a notes-only delta at the unchanged `da347498d07b843e5af3f9eb871376514ffdf38c` SHA: all 689 retained files and all Apple Pay, CVC, currency-conversion, layout and demo findings remain unchanged. It is not a new package version, implementation fix or proof of package-registry availability. The revised record retains the original release timestamp 2026-10-07; collection and ingestion occurred on 2026-11-07. A code comparison is not fabricated for a same-SHA notes revision. Original raw and all older wiki knowledge remain intact.

Evidence: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-10-14/release-notes.md`, `raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-11-07/manifest.json`, `raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-11-07/release-notes.md` and `tracking/github/repos/adyen/adyen-ios/ingest-packets/github-03f5682f5c6d30579f8c/packet.json` / `tracking/github/repos/adyen/adyen-ios/ingest-packets/github-03f5682f5c6d30579f8c/packet.md`.

## `adyen-ios@5.27.0` full additive update

Exact boundary: `5.26.0` (`da347498d07b843e5af3f9eb871376514ffdf38c`) -> `5.27.0` (`15167f660094853d204dc6cd25a068eddf1bc2b2`). Released 2026-10-30; collected and ingested 2026-11-07, after the notes-only correction above completed. Full mode uses the approved focused read: all 13 changed retained files, affected prior/dependency code, release evidence and cumulative wiki history; 676 unchanged files and generated inventories checked mechanically. The snapshot has 689 files; all 7,780 upstream paths are dispositioned (13 retained, 7,767 intentional exclusions), with no packet-reported gaps/unclassified changes. This is not a full upstream-repository read or runtime test. Security-keyword triage is not an independently established security advisory.

### VoiceOver controls and form guidance

| Surface | Retained `5.27.0` behavior | Boundary |
| --- | --- | --- |
| Store-payment toggle | Native UISwitch owns the label and accessibility element; separate label excluded, prior VoiceOver-status-dependent wrapper switching removed | UI accessibility wiring, not new token storage or consent semantics |
| Expiry/CVC format | Shared label combines title, expected input format and a currently shown validation error; format remains through validation/reset | AdyenInternal SPI implementation, not a new merchant payment request field |
| Card logos | Disables collection selection and iOS-15+ focus; images use accessibilityLabel and image trait | Does not prove removal of card-network selection elsewhere |
| Address/toolbar titles | Adds header trait through FormLabelItem and ModalToolbar | Code-level semantics, not measured accessibility compliance |
| Cancel button | Localized cancel label assigned regardless of button image/style | No physical-device/localization test here |

`FormValidatableValueItemView` adds `accessibilityInputFormat` and `isShowingValidationError`; it recomputes labels when title, validation message, format or validation state changes. `FormTextItemView.accessibilityLabelView` resolves to the text field, so the constructed description reaches that control. Expiry creation supplies localized format text and now stores the supplied localizationParameters; the CVC view supplies the selected brand's localized digit-count placeholder to the shared label builder. Its existing sanitized-value/length policy from `5.26.0` is not a new change in this release.

The new property is on a type annotated `@_spi(AdyenInternal)`. Do not present it as a supported new merchant configuration option or as a reason to depend on internal SDK types. Likewise, descriptive store-payment labeling does not replace server-side tokenization, eligibility or fulfillment verification.

### Additional source-derived changes

**Submit activation:** The shared SubmitButton gains this override, beyond the five release-note highlights:

```swift
override public func accessibilityActivate() -> Bool {
    guard isEnabled, isUserInteractionEnabled else { return false }
    sendActions(for: .touchUpInside)
    return true
}
```

The existing loading-indicator setter disables the control while loading and re-enables it afterward. The new override therefore respects that control state before sending its normal action. It is not an end-to-end payment success, duplicate-submission guarantee or new merchant callback API.

**Scanner overlay:** CardScannerOverlayView creates center/aspect/width constraints once, retains its width constraint, updates it before super.layoutSubviews, then publishes roiFrame. Width is now `max(0, min(bounds.width, bounds.height) - 24)`, rather than recreating constraints on each layout with an unclamped width. This establishes layout/constraint handling only, not measured speed, recognition accuracy or verified device rotation behavior.

### Distribution notice and compatibility

> [!warning] Contradiction
> The original October capture attached the final-CocoaPods notice to `5.26.0`; the revised notes remove it there, and the `5.27.0` notes now identify this release as the final CocoaPods release, with SPM/Carthage for future distribution. Both dated claims remain recorded. Do not use the superseded `5.26.0` wording as current guidance. [[adyen-ios-sdk]] and [[changelog-github-adyen-ios]] preserve the same correction.

Same-tag README still documents CocoaPods installation, and Adyen.podspec declares `5.27.0`. These current-version files can coexist with a final-version announcement; neither the notice nor this inspection proves that `5.27.0` is unavailable from the registry, that it was installed successfully, or a global CocoaPods shutdown date. Minimum README requirements remain iOS 12, Xcode 15 and Swift 5.7; the podspec retains iOS 12 / Swift 5.7. Retained Package.swift/Cartfile and dependency pins are unchanged. Older distribution and integration evidence is preserved, and this native upgrade does not change an independently pinned wrapper automatically.

**Merchant regression checks:** exercise VoiceOver storage toggling, expiry/CVC format descriptions before/after editing and validation, logo/header/cancel navigation, enabled versus loading/disabled submit activation, and scanner layout/resizing. Plan future package-manager upgrades using the corrected version-qualified notice. No Swift/Xcode build, dependency installation, device/VoiceOver, accessibility-compliance or payment execution was performed in this ingest.

## Related

- [[changelog-github-adyen-ios]] - package-qualified release ledger
- [[adyen-ios-sdk]] - native SDK concept
- [[source-github-adyen-3ds2-ios]] - independently versioned native 3DS2 runtime
- [[source-github-adyen-wechatpay-ios]] - independently versioned WeChat SDK binary wrapper
- [[adyen-wechatpay-ios-wrapper]] - wrapper ownership and native handoff boundary
- [[source-github-adyen-web]] - independently versioned browser SDK
- [[adyen]] - company and knowledge-status page
- [[co-badged-cards]] - cross-provider network-choice concept

## Raw sources

- `5.27.0` snapshot: `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/manifest.json`
- `5.27.0` release: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.27.0/2026-11-07/manifest.json` and `raw/github/adyen/adyen-ios/releases/adyen-ios/5.27.0/2026-11-07/release-notes.md`
- `5.26.0` -> `5.27.0` comparison: `tracking/github/repos/adyen/adyen-ios/comparisons/adyen-ios/5.26.0--5.27.0/comparison.json`, `tracking/github/repos/adyen/adyen-ios/comparisons/adyen-ios/5.26.0--5.27.0/comparison.md` and `tracking/github/repos/adyen/adyen-ios/comparisons/adyen-ios/5.26.0--5.27.0/diff.patch`
- Toggle/format: `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/Adyen/UI/Form/Items/Toggle/FormToggleItemView.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/Adyen/UI/Form/Items/Value/Validatable/FormValidatableValueItemView.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/AdyenCard/Form/FormCardExpiryDateItem.swift` and `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/AdyenCard/Form/FormCardSecurityCodeItemView.swift`
- Logos/headers: `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/AdyenCard/Form/FormCardLogosItemView.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/Adyen/Core/ToolBar/ModalToolbar.swift`, `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/Adyen/UI/Form/Items/Address/FormAddressItem.swift` and `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/Adyen/UI/Form/Items/Basic Items/FormLabelItem.swift`
- Submit/scanner: `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/Adyen/UI/Views/SubmitButton.swift` and `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/AdyenCardScanner/Sources/CardScannerOverlayView.swift`
- Label dependency: `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/Adyen/UI/Form/Items/Text/FormTextItemView.swift`
- Distribution/version: `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/README.md`, `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/Adyen.podspec` and `raw/github/adyen/adyen-ios/snapshots/2026-11-07-15167f6/files/Adyen/Helpers/AdyenSdkVersion.swift`
- Revised `5.26.0` release record: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-11-07/manifest.json`
- Revised `5.26.0` notes: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-11-07/release-notes.md`
- New snapshot: `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/manifest.json`
- New release record: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-10-14/manifest.json`
- New release notes: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.26.0/2026-10-14/release-notes.md`
- New README/podspec: `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/README.md` and `raw/github/adyen/adyen-ios/snapshots/2026-10-14-da34749/files/Adyen.podspec`
- Exact comparison: `tracking/github/repos/adyen/adyen-ios/comparisons/adyen-ios/5.25.1--5.26.0/comparison.json` and `tracking/github/repos/adyen/adyen-ios/comparisons/adyen-ios/5.25.1--5.26.0/diff.patch`
- Snapshot manifest: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/manifest.json`
- Release manifest: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.25.1/2026-08-01/manifest.json`
- Release notes: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.25.1/2026-08-01/release-notes.md`
- README: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/README.md`
- Package manifest: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/Package.swift`
- Session: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/AdyenSession/`
- Drop-in: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/AdyenDropIn/`
- Actions: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/AdyenActions/`
- Card and encryption: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/AdyenCard/` and `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/AdyenEncryption/`
- Demo flows: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/files/Demo/Common/IntegrationExamples/`

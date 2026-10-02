---
title: "GitHub: stripe/stripe-ios"
type: source
date_ingested: 2026-05-13
date_updated: 2026-10-02
original_format: github-repo
raw_files:
  - "github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/manifest.json"
  - "github/stripe/stripe-ios/supplements/2026-10-02-9f0d5aa-8ad0f8dd/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/manifest.json"
  - "github/stripe/stripe-ios/supplements/2026-10-02-7037819-bd3ee3a4/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-7037819/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-841b697/manifest.json"
  - "github/stripe/stripe-ios/supplements/2026-09-30-841b697-f58a4b7c/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-8444041/manifest.json"
  - "github/stripe/stripe-ios/supplements/2026-09-30-8444041-bea35b75/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/manifest.json"
  - "github-stripe-ios.md"
tags: [stripe, ios, swift, mobile, sdk, payments, apple-pay, payment-sheet, embedded-payment-element, connect, identity, financial-connections, crypto-onramp, github-repository]
---

## Overview

`stripe/stripe-ios` publishes Stripe's official modular Swift SDK for native iOS payments and adjacent products. This cumulative page preserves the legacy `25.14.0` manual capsule and adds the approved `stripe-ios@26.4.1` full baseline at commit `d9252fd0a4a6d369fa45bb06f74c4e818c914f91`.

Repository: <https://github.com/stripe/stripe-ios>

The approved `stripe-ios@26.5.0` delta at `a1ea788163dee511239e2cfefe27cad576f045d3` adds the version-qualified findings below without replacing the `26.4.1` baseline or legacy knowledge.

## Evidence Boundary

- The approved `26.12.1` full additive ingest overrides generated delta for the incompatible STP polling signature. Approved focused reading covers all changed retained files, affected prior code and three supplemental files; unchanged history/inventories are checked mechanically, not claimed as fresh full source reads. Current/prior capsules contain 276/275 files: one added, 22 modified, 253 unchanged, none removed. The effective full reading list has 290 paths. All 551 retained hashes matched during review; upstream dispositions cover 23 retained and 6,600 policy-excluded paths, not semantic review of all upstream code. Current availability/form factories, Checkout controller/API/Apple Pay context, Financial Connections enforcement/event internals, generic poller/action mapping and CryptoOnramp error/upload helpers remain gaps. No SDK build, device, eligibility or payment testing.

- The approved `26.12.0` full additive ingest uses focused reading of changed retained content and affected prior code, with unchanged history/inventories checked mechanically. Both snapshots contain 275 files: 16 modified, 259 unchanged. The effective full list has 284 paths; this exception does not claim a fresh read of all unchanged code. Current outer Checkout/session implementation, CryptoOnramp request/result models and Image implementation, HTML rendering, Identity rendering, StripeCore header handling and card-scan internals are excluded. No SDK build, device or payment testing was performed.

- The approved `26.11.0` full additive ingest uses the release-specific focused-reading exception: all 21 added/changed retained files and the exact-SHA supplemental controller read fully (unchanged cumulative changelog history checked mechanically), with affected prior code compared. The capsule contains 275 files: two added, 19 modified, 254 unchanged. Full mode reflects broad confirmation behavior changes, not a claim to have reread all unchanged code. Request serialization/API implementation, current poller, wallet context, Link visibility consumers, method availability/form factories and Identity rendering remain gaps. No SDK build, device, payment or eligibility testing was performed.

- The approved `26.10.0` bounded delta uses focused reading of all changed retained content and affected prior code, with unchanged history and inventories checked mechanically. The 273-file capsule has 16 modifications and 257 unchanged files. Release announcements are distinguished from retained implementation. Current availability/form factories, CryptoOnramp identifier models, Identity controller/UI, Link consumers and Checkout/Apple Pay internals remain excluded; older supplements do not establish their current behavior. No SDK build, device or payment testing was performed.

- The approved `26.9.0` full additive ingest uses focused reading: all changed/new retained implementation and both exact-SHA supplemental files read fully, affected prior code compared, unchanged files and cumulative history checked mechanically. The 273-file snapshot has ten additions, 31 modifications and 232 unchanged files. Full mode reflects broad confirmation and SPI compatibility changes, not a fresh read of all unchanged code. The effective full-mode list has 286 paths; the release-specific exception remains explicit.
- Current Checkout request serialization, poll-response decoding, backend timeout enforcement, Apple Pay wrapper/context, availability/form factories and delegated Financial Connections/Link internals remain excluded. The two-file supplement closes the controller/poller evidence gap only. No SDK build, simulator, runtime payment, settlement or eligibility verification was performed.

- The approved `26.8.0` full additive ingest uses the release-specific focused-reading exception: changed retained implementation/content and affected prior code were read, while inventories and unchanged history were checked mechanically. The 263-file capsule has 30 modifications, one addition and 232 unchanged files. Two exact-SHA supplemental Checkout files were collected with separate approval and read fully. Full mode reflects broad confirmation changes, not a claim to have reread all unchanged files or the whole repository.
- `26.8.0` retains the outer CheckoutController and Apple Pay wrapper through the supplement, but excludes `CheckoutApplePayContext` and other delegated internals. This closes the outer-result evidence gap only; no SDK build, runtime payment or eligibility testing was performed. Earlier exclusions below describe their respective versions.

- The approved `26.7.0` delta uses the focused-reading exception documented in `tracking/github/repos/stripe/stripe-ios/reviews/github-78ba61fe5193c202d74a.md`. All changed retained implementation was read fully; affected prior code was compared and unchanged history/manifests checked mechanically. The 262-file capsule has two additions, 26 modifications and 234 unchanged files. Of 53 prior-only paths, only three were deleted upstream; 21 were modified upstream but not retained currently, and 29 were not listed in the upstream inventory. Missing current coverage is not deletion.
- Current outer Checkout implementation, Link button-visibility helper, autocomplete service/flag decoder and Financial Connections Lite implementation are excluded. The `26.6.0` Checkout warning is historical, not a verified `26.7.0` readiness assessment. No SDK build, runtime payment or eligibility testing was performed.

- The approved `26.6.0` full additive ingest uses the focused-reading exception: all newly retained and changed implementation was read, affected prior code was compared, and unchanged evidence/history was checked mechanically. The current capsule has 313 files: 55 newly retained, 27 modified, one removed, and 231 unchanged against the prior capsule. Of the 55 newly retained files, seven were added upstream, ten modified upstream, and 38 were not in the upstream change list. Collection-scope growth is not synonymous with new release functionality.
- The `26.6.0` capsule adds Checkout session and billing-sync internals, but still excludes Link funding-source detection, method availability/form factories/polling UI, Crypto Onramp API requests, and appearance helpers. No SDK build, simulator, live payment, or merchant eligibility check was performed.
- The `26.5.0` snapshot retains 259 files: 22 modified and 237 unchanged against `26.4.1`. Approved focused reading covered all changed implementation and release/diff content; manifests and unchanged cumulative history were checked mechanically. No SDK build, simulator, payment execution, or merchant eligibility verification was performed.
- Excluded `26.5.0` details include FlowController selection-restoration helpers, Checkout session/billing-sync internals, form-factory tax logic, changed Link UI internals, and Crypto Onramp network/API implementation. Retained callers support bounded findings, not complete delegated behavior. Tempo support is release-note evidence only.
- The `26.4.1` capsule retains 259 documentation, build, example, public API, and implementation files, including 245 Swift files. Tests, fixtures, generated documentation, CI, and general tooling are excluded by policy.
- This is a bounded public-source capsule, not a full repository mirror. A later query that needs excluded implementation requires an immutable supplement tied to the exact SHA.
- The legacy `25.14.0` evidence is a manually selected capsule. No automated comparison exists from its SHA to `26.4.1`, so retained findings are not represented as a complete file-by-file diff.
- Public types and payment-method models do not prove merchant eligibility, geographic availability, enabled Dashboard configuration, connected-account support, or preview access.
- `PaymentSheetResult.completed` does not prove that funds moved. Fulfillment remains gated by a successful server-side Stripe payment event.

## Grounding Excerpts

> "This means the sensitive data is sent directly to Stripe instead of passing through your server."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/README.md:37`

> "The Stripe iOS SDK supports all Apple supported Xcode versions and is compatible with apps targeting iOS 15 or above."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/README.md:113`

> "The payment may still be processing at this point; don't assume money has successfully moved."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet.swift:18-23`

> "If this is set to true, make sure your integration listens to webhooks for notifications on whether a payment has succeeded or not."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetConfiguration.swift:79-82`

> "Fixed an issue where some Alipay payments incorrectly reported failure after succeeding."
>
> `raw/github/stripe/stripe-ios/releases/stripe-ios/26.4.1/2026-07-31/release-notes.md:1-3`

## Package Status

| Package | Latest ingested release | Exact SHA | Evidence status |
| --- | --- | --- | --- |
| `stripe-ios` | `26.12.1` | `9f0d5aa20e6a690ff4d78b35c307f0fb88d6f36c` | Approved full additive ingest with focused reading and three-file supplement; all earlier baselines and deltas retained |

This table reports wiki ingest progress, not the latest release published upstream.

## Architecture

The retained package manifest and source expose these principal layers:

1. `StripePaymentSheet` owns PaymentSheet, FlowController, Embedded Payment Element, CustomerSheet, Link configuration, appearance, and deferred confirmation.
2. `StripePayments` owns low-level PaymentIntent, SetupIntent, PaymentMethod, token, Source, Radar, microdeposit, and authentication APIs.
3. `StripeApplePay` provides a lightweight `STPApplePayContext`, including an App Clip oriented installation surface.
4. Product modules expose Connect embedded components, Financial Connections, Identity, Issuing, card scanning, and alpha Crypto Onramp coordination.
5. UIKit and SwiftUI examples demonstrate PaymentSheet, FlowController, Embedded Payment Element, and direct US bank account collection.

The package manifest includes internal support modules such as `StripeCore`, `StripeUICore`, `Stripe3DS2`, and `StripeCameraCore`. Their inclusion is inventory evidence, not a claim that their internal APIs are supported merchant surfaces.

## Core Payment Surfaces

### PaymentSheet

PaymentSheet is the prebuilt collect-and-confirm UI. It supports an existing PaymentIntent client secret, an existing SetupIntent client secret, and an `IntentConfiguration` deferred flow. The `26.4.1` baseline also retains Checkout Session initialization; this is not a generally available, complete Checkout confirmation guarantee. In `26.6.0`, the shared confirmation function rejects Checkout intents and directs them to the unfinished `Checkout.confirm` SPI below. Callback, async, UIKit, and SwiftUI presentation paths are retained.

`PaymentSheet.Configuration` controls merchant display, customer credentials, Apple Pay, Link, appearance, billing and shipping collection, return URLs, delayed methods, payment-method ordering, card-brand acceptance, custom methods, and external methods. These client options do not override account or Intent eligibility.

### FlowController

FlowController separates selection from confirmation for merchant-owned checkout composition. The app creates the controller, presents payment options, renders `PaymentOptionDisplayData`, and confirms from its own buy button. Current APIs include callback and async creation, presentation, confirmation, and update operations.

### Embedded Payment Element

`EmbeddedPaymentElement` puts payment-method selection directly into UIKit or SwiftUI. Its contract includes creation, configuration updates, payment-option display data, clearing selection, delegate-based height and option updates, and async confirmation. The merchant supplies the confirm button and a presenting view controller.

### CustomerSheet

CustomerSheet manages saved payment methods using Customer Session credentials. Configuration covers billing collection, preferred networks, card-brand acceptance, Apple Pay, appearance, return URLs, and card scanning. The v25 migration removed the older ephemeral-key-secret customer configuration in favor of Customer Sessions.

## `stripe-ios@26.5.0` Integration Delta

### Standalone Link and billing configuration

The top-level `StripePaymentSheet.LinkConfiguration`, not the nested `PaymentSheet.LinkConfiguration`, adds optional `billingDetailsCollectionConfiguration`. Nil keeps the base `PaymentElementConfiguration` value. Both the internal `collectPaymentMethod` flow and private-preview `present` flow apply the override; the internal `collectName` flag can subsequently force name collection. `LinkAppearance` exposes its existing colors, primary-button dimensions, style, and reduced-branding settings to `LinkControllerPreview` consumers.

This remains private preview. Controller creation checks native-Link device support; configuration availability is not merchant-access proof. Collection returns a PaymentMethod, and separate SetupIntent confirmation remains an existing contract, not a new `26.5.0` capability.

`PaymentSheet.BillingDetailsCollectionConfiguration` also gains a public initializer: name, phone, email, and address collection default to automatic; attaching defaults defaults to false; allowed countries defaults to an empty list. This additive Swift API was found by reading source despite the automated comparison's empty `public_api_changes` array.

### Selection, cancellation, and presentation

- Embedded forms capture the accepted valid option on Continue. Cancellation reconstructs form state from that accepted option instead of retaining canceled edits. Restoration handles form-backed linked banks, new/external methods, and Link signup; Apple Pay has no form parameters. When restoration fails and the option changed, selection is cleared.
- Checkout-backed saved-method selection records the prior state, suppresses delegate publication, disables interaction, and displays loading while awaiting billing-address sync. Success reselects the saved method if it remains available, persists the default, notifies, and then invokes immediate-action completion. Failure restores prior selection/form, reenables interaction, and presents an error. Refresh preserves pending/loading state. The actual server sync contract is excluded.
- SwiftUI `EmbeddedViewRepresentable` resolves presentation from `uiView.window`, refreshes on window attachment, avoids a bottom-sheet presenter, and retries while a controller is dismissing. This is not a claim that every SDK fallback stopped using application-global presentation.
- FlowController captures a selection snapshot before presenting options and invokes restoration/rebuilding before publishing the canceled result. Its Link wallet shortcut also requires a prior Continue action. The caller rebuilds with current saved methods; excluded snapshot helpers limit conclusions about detailed persistence behavior.

### Internal Checkout confirmation and other scope

`PaymentSheet+CheckoutSessionAPI.swift` now omits `save_payment_method` when `noPaymentRequired` is true; otherwise it uses the confirm type's save choice. After committing the session, it dispatches a returned SetupIntent first, then a PaymentIntent, and fails if neither is present. The definition of `noPaymentRequired` and session internals are excluded: do not infer complete subscription, free-order, or generally available Checkout integration support from these branches.

CustomerSheet passes `collectsTaxFromBillingAddress: false` into form-factory plumbing; that is not evidence of a new merchant tax feature. The release notes announce Tempo wallet-address registration for alpha Crypto Onramp, but the relevant network/API implementation is not retained. Podspec changes establish a version bump without a deployment-floor change; the Apple Pay podspec alone establishes no integration change.

### Delta grounding excerpts

> "If `nil`, uses the billing details collection configuration from the `PaymentElementConfiguration` passed at init."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Link/LinkConfiguration.swift:31`

> `guard pendingBillingAddressSyncSelection == nil else { return }`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElement+Internal.swift:97`

> `guard !checkoutSession.noPaymentRequired else { return nil }`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+CheckoutSessionAPI.swift:61`

> `if let setupIntent = response.setupIntent {`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+CheckoutSessionAPI.swift:100`

## `stripe-ios@26.6.0` Additive Baseline

### MB WAY and Bizum

The release announces PaymentSheet support for MB WAY and Bizum. `STPPaymentMethodType` adds `mb_way` and `bizum`. Next-action decoding recognizes `mb_way_await_authorization` and `await_authorization`; the handler presents PaymentSheet polling for MB WAY and Bizum respectively, without a Safari controller.

Both branches require `PaymentSheetAuthenticationContext` and `STPPaymentHandlerPaymentIntentActionParams`. Non-PaymentSheet contexts fail as unsupported; SetupIntent action parameters also fail. The params factory needs no method-specific params object for these types, which does not mean billing information is never required. Form construction, availability logic, and the polling view model are excluded. Do not infer merchant/country/currency eligibility, timing, or settlement from these branches.

### Private-preview Link errors and alpha wallet deletion

`LinkController.present` now checks an error from native Link selection before interpreting a missing option as cancellation or creating a PaymentMethod. The release notes identify the no-funding-sources case, previously falling back silently to card. `PayWithNativeLinkController` forwards a failed full result into the selection error callback. Internal `collectPaymentMethod` and FlowController selection callbacks ignore the added error argument; do not extend the preview contract to every Link consumer. The actual funding-source detection code is excluded.

Alpha `CryptoOnrampCoordinator.deleteWalletAddress(walletId:)` takes the registered wallet ID, not its address string. It requires Link account information, awaits the API call, records success afterward, and maps errors through the coordinator's existing error path. Error analytics now carry available request IDs. The excluded API implementation leaves endpoint, idempotency, persistence, and server-side deletion semantics unverified.

### Checkout confirmation architecture and readiness

The old `PaymentSheet+CheckoutSessionAPI.swift` is removed. New `Checkout+Confirm.swift` and `Checkout+Confirm+Link.swift` own Checkout confirmation; the ordinary `PaymentSheet.confirm` path explicitly rejects Checkout intents. Shared Bacs mandate and saved-card CVC preconfirmation actions return an async result, and Link web/native controllers accept injected confirmation handlers. These changes do not remove ordinary PaymentIntent, SetupIntent, or deferred PaymentSheet flows.

> [!warning] Checkout SPI is unfinished at `26.6.0`
> `Checkout.confirm` can commit a returned session response, then discards its internal payment result and returns `.canceled` because result mapping is unfinished. Its Apple Pay branch also returns canceled with an implementation TODO. Express Checkout Apple Pay/Link tap handlers and Shipping Address completion are unfinished. Do not present this SPI as a production integration recipe or interpret its canceled result as proof that no payment occurred. These are observed limits at this SHA, not all proven newly introduced regressions.

The old helper committed the session before next-action handling. The new helper returns a session response with its result, and the outer Checkout method commits afterward. SetupIntent handling still precedes PaymentIntent; missing both remains an error, and `noPaymentRequired` still suppresses `save_payment_method`.

### Newly retained session knowledge

The expanded capsule now exposes session status, customer/saved methods, totals, currency choices, billing and shipping operations, configuration, and a serialized update queue. `noPaymentRequired` means `paymentStatus == .noPaymentRequired`, not simply a zero total. Billing sync skips details without a country and sends a billing tax-region update only when automatic tax uses billing. These findings close specific evidence gaps at `26.6.0`; the older capsule's exclusions remain historically accurate.

The presence of models and controls does not prove complete UI support: line-item decoding handles one-time price items, currency-selector text includes unfinished localization, and the confirmation/UI limits above remain. Do not date every newly retained behavior's introduction to this release.

### Other retained changes

- Package.swift stops processing Resources/JSON; CustomerSheet removes local and Elements Session form-spec loading. The upstream inventory records form-spec/resource deletions, but replacement factory implementation is excluded, so complete UI equivalence is unverified.
- Appearance properties now reference helper constants; their excluded implementation prevents a numerical-equivalence claim from these callers alone. FPX bank brands gain SPI CaseIterable conformance.
- Eight retained podspecs bump versions without a deployment-floor change. This does not establish a standalone Apple Pay integration change. Existing task-cancellation defers are not new in this release.

### Grounding excerpts

> "MB WAY is not supported outside of PaymentSheet."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift:1410`

> "Checkout Session confirmation must go through Checkout.confirm, not PaymentSheet.confirm."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+API.swift:56`

> `return paymentStatus == .noPaymentRequired`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Session+Internal.swift:51`

> "Deletes the given crypto wallet from the current Link account."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripeCryptoOnramp/StripeCryptoOnramp/Source/Components/CryptoOnrampCoordinator.swift:138`

## `stripe-ios@26.7.0` Integration Delta

### Financial Connections Lite migration

PaymentSheet now depends on `StripeFinancialConnectionsLite`. The retained package manifest registers its product and target with a StripeCore dependency, and the PaymentSheet podspec adds the corresponding dependency. Manual/Carthage PaymentSheet installations must embed `StripeFinancialConnectionsLite.xcframework`; the migration guide states no additional action for CocoaPods/SPM. The actual Lite implementation is excluded, so this is packaging and migration evidence, not proof of complete bank-payment behavior.

### Link visibility and autocomplete

`PaymentSheet.LinkConfiguration.Display.walletButtonHidden` leaves Link enabled while hiding its payment-element button/row. Its `shouldDisplay` value remains true while `shouldShowButton` is false; `.never` returns false for both. Embedded construction and update-time preservation of a previous Link selection now call `PaymentSheet.shouldShowLinkButton` rather than `isLinkEnabled`. The helper implementation is not retained, so these callers do not prove every Link UI path.

Illustrative configuration for this version (not runtime-tested):

```swift
var configuration = PaymentSheet.Configuration()
configuration.link.display = .walletButtonHidden
```

The STP SPI `useAutocompleteEndpoints` property is removed from PaymentSheet, Embedded and CustomerSheet configuration and their shared protocol. CustomerSheet now passes `elementsSession.shouldUseAutocompleteProxyEndpoints` directly instead of combining it with the configuration flag. The add-payment controller passes this flag directly to the autocomplete initializer. Release notes announce internal-service autocomplete, but excluded service/flag-decoder code prevents claiming that every request unconditionally uses it.

### Vipps and version attribution

PaymentMethod type/decoder/parameters gain `vipps`; new `STPPaymentMethodVipps` and `STPPaymentMethodVippsParams` expose typed response and request surfaces. Parameters include a convenience initializer and serialization mapping. The payment handler adds `.vipps` to the group for which `_isProcessingIntentSuccess` returns false: `processing` alone is not a completed flow. This does not establish merchant eligibility, general availability, or complete PaymentSheet/Checkout integration.

The cumulative changelog newly inserts `vipps_preview=v1` beta-header guidance under 26.6.0, plus AddressElement no-swipe-dismiss, cancel/discard and unsaved-change dialog notes under 26.5.0. These are retrospective annotations, not proof of newly introduced 26.7.0 behavior or of those implementations in older retained SHAs. The typed Vipps additions are observed between the actual 26.6.0 and 26.7.0 snapshots. Preserve the previously recorded 26.4.0 public-beta milestone rather than silently redating it.

### Grounding excerpts

> "No action is required for CocoaPods or Swift Package Manager users."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/files/CHANGELOG.md:8`

> `case walletButtonHidden`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetConfiguration.swift` - Link display enum

> `useAutocompleteEndpoints: elementsSession.shouldUseAutocompleteProxyEndpoints,`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/CustomerSheet/CustomerSheet.swift:202`

The historical unfinished outer Checkout finding remains qualified to 26.6.0. Its current implementation is outside this capsule, so do not infer either continued failure or a fix from retained unchanged confirmation helpers.

## `stripe-ios@26.8.0` Additive Baseline

### Checkout confirmation and Apple Pay limits

The confirmation engine now extends `CheckoutController`, with typed Apple Pay, Link and conventional new/saved payment-method flows. It rejects closed sessions, concurrent confirmation and pending session updates, serializes confirmation, commits a returned session response and maps the result. Link completion without a returned session fails explicitly; recursive Link payment-method confirmation reuses the payment engine without repeating preconfirmation UI.

The exact-SHA supplemental controller's `confirm(from:)` reaches this engine. Its `succeeded(paymentStatus:)` may carry paid, unpaid or no-payment-required status; it is not settlement proof. The controller is STP/ReactNativeSDK SPI, not a generally available merchant recipe. Standard `PaymentSheet.confirm` still rejects Checkout sessions and directs callers to `CheckoutController.confirm`.

> [!info] Version-qualified Checkout evidence
> The 26.6.0 always-canceled outer mapping is historical; the observed 26.8.0 controller returns the mapped confirmation result. The first fixed release is not established because the 26.7.0 outer controller was excluded. The prior retained Apple Pay TODO/canceled branch now delegates to an Apple Pay wrapper, but its `CheckoutApplePayContext` implementation remains excluded. Do not infer complete wallet authorization, request construction, Express Checkout readiness or general availability from this wrapper.

The supplemental controller documents that a nil-presenter key-window fallback is incompatible with multi-scene apps. Its initialization applies shipping defaults/normalization before creating PaymentElement; these newly retained details are not all proven new in this release. Its server-update API documents a 20-second timeout and session refresh, while delegated queue/timeout details remain outside this supplement. The confirmation engine still dispatches SetupIntent before PaymentIntent, fails if neither exists and suppresses saving for no-payment-required sessions.

### FPX and decline messages

FPX gains Agrobank, Bank of China and MBSB Bank. Enum additions follow `unknown`, preserving existing case order. The mapping implementation moves to dictionaries. Status API codes are Agrobank AGRO02/AGRO01 (business/individual), Bank of China nil/BOCM01, and MBSB MBSB001/MBSB001. These are SDK mappings, not live bank availability or merchant eligibility verification.

`STPPaymentHandler._error` now uses an existing localized error description before the generic API-code mapping. This preserves supplied card-decline text after 3DS rather than changing approval rules or success states.

### Private-preview Link and low-level options

Top-level `StripePaymentSheet.LinkConfiguration`, distinct from nested `PaymentSheet.LinkConfiguration`, gains optional `financialConnectionsPermissions: [String]?`. `LinkController` transfers it into deferred setup configuration before loading. Nil requests no specific permissions; configuration does not prove consent or data access. `LinkSettings` also decodes `link_payment_method_bank_account_data_consent` within `link_payment_session_context`; downstream consent behavior remains unverified.

`STPConfirmAlipayOptions` gains currency (documented as required for SetupIntent confirmation) and future usage (Alipay supports off-session). SetupIntent inferred-mandate handling includes Alipay. Private-preview `STPConfirmKlarnaOptions` accepts interoperability tokens for PaymentIntent/SetupIntent confirmation and partner confirmation tokens for PaymentIntent only. `STPSetupIntentConfirmParams.paymentMethodOptions` gains private-preview encoding/copying support. The retained `PaymentSheet.makeSetupIntentParams` does not automatically forward incoming payment options; low-level fields do not establish a complete PaymentSheet integration.

Mandate providers gain MainActor isolation. Eight podspecs only bump versions, with no deployment-floor change. README changes describe pinned cached SwiftLint use, not verified execution of the excluded tooling.

### Historical attribution

The cumulative changelog preserves all 2,118 previous lines and inserts 13 lines. Some insertions are retrospective: horizontal-layout Link presentation and Alipay notes appear under 26.7.0, and Klarna options under 26.5.0. Preserve upstream labels separately from code observed changing between the retained 26.7.0 and 26.8.0 SHAs. The annotations do not prove those additions existed in the earlier snapshot; the horizontal-layout fix's complete implementation is not retained.

### Grounding excerpts

> `return .succeeded(paymentStatus: response.paymentStatus)`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift:230`

> "Link completed Checkout confirmation without returning the confirmed session."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm+Link.swift:44`

> "Checkout Session confirmation must go through CheckoutController.confirm, not PaymentSheet.confirm."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+API.swift:56`

> "Three-letter ISO currency code in lowercase. Required when confirming a SetupIntent."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePayments/StripePayments/Source/API Bindings/Models/PaymentIntents/STPConfirmAlipayOptions.swift:15`

## `stripe-ios@26.9.0` Additive Baseline

### Payment-method API bindings

Kakao Pay (`kakao_pay`), Korean cards (`kr_card`), Naver Pay (`naver_pay`), PAYCO (`payco`) and SeQura (`sequra`) gain type identifiers, response decoding/properties, parameter factories, convenience initializers and serialization mappings. Korean cards expose a brand enum with unknown fallback and optional last4, documented as potentially absent for American Express. Naver Pay exposes optional buyer ID and card/points/unknown funding; its params serialize `fundingString` under `funding`, while assigning typed unknown clears that string. The other new parameter types have no typed method-specific fields, but allow additional API parameters. Optional billing arguments do not establish that the backend never requires billing details.

PaymentIntent and SetupIntent mandate-inference lists add Kakao Pay, Korean cards and Naver Pay, not PAYCO or SeQura. All five enter the payment handler's group where `processing` alone is not success. New payment-method enum cases precede `unknown`; do not assume every existing numeric enum value is preserved. Bindings do not prove complete PaymentSheet support, merchant eligibility, country/currency coverage or preview access.

### Checkout confirmation and polling

Checkout builds a shared confirmation request, then confirms, handles the returned Intent and polls when the returned session is open. It explicitly fails failed submissions, manual-approval requirements and orchestration responses. PaymentIntent now takes precedence over SetupIntent; missing both fails. A successful handler result must include the returned Intent. Canceled/failed results preserve the available session response.

The supplemental poller uses a 30-second elapsed-time budget and passes remaining time to requests. Normal minimum spacing between request starts is 0.5 seconds. Request errors retry until the budget expires; HTTP 429 increases spacing to 2, 4 and at most 8 seconds, resetting after a successful request. The excluded API client's timeout enforcement prevents promising a strict observed wall-clock limit.

`requiresPaymentMethod` takes priority over state classification. Active, processing-sync-payment and processing-subscription states continue polling; succeeded, processing-async-payment and pending-async-customer-action return client completion. Failed asynchronous payment and invalid/expired states have distinct outcomes. The caller retrieves the latest session and fails for those outcomes or requires-payment-method; if retrieval fails, it retains the original response with the retrieval error.

Both completed and timed-out polling outcomes proceed to response reconstruction from the original confirm response plus the client-completed Intent. A succeeded PaymentIntent sets complete/paid; a processing PaymentIntent sets complete without forcing paid; a succeeded SetupIntent sets complete. Other fields are preserved. This is client-side reconstruction, not a fresh successful backend retrieval. The source comment about completed-session retrieval returning HTTP 400 is upstream commentary, not live verification.

> [!info] Completion is not settlement
> Checkout's SPI result is now `completed(paymentStatus:)`, replacing 26.8.0's `succeeded(paymentStatus:)`. A polling timeout can reach this result after Intent handling. Neither timeout nor SDK completion establishes that funds moved; fulfillment remains gated by successful server-side payment events.

### Request construction, Link and SPI compatibility

New methods use session email only when billing email is nil, then create a PaymentMethod. Hidden/deselected/selected save-checkbox states produce nil/false/true request values; saved methods use a nil save choice and prefer recollected CVC options over existing ones. Request serialization is excluded: do not carry forward the older no-payment-required save suppression as verified 26.9.0 behavior. Confirmation-challenge completion for new methods is scheduled in a deferred Task, not an awaited end-to-end guarantee.

Link wallet callbacks now require a Link option and recurse through `confirmLink`; produced new/saved methods use shared Checkout confirmation. The prior route accepted conventional new/saved options directly. Link completion without a returned session still fails.

Checkout-specific Embedded and FlowController creation overloads, including async FlowController creation, become internal. Ordinary public Intent-based creation remains. Embedded Checkout creation accepts an initial option and maps it to initial row selection; the changed row conversion helper is excluded. The controller creates PaymentElement only when configured, fails confirmation when absent, and asserts/force-unwraps in `getPaymentElement()`. Adaptive-pricing allowance follows whether a currency selector is configured. Shipping updates require an explicit name argument and accept nil address to clear; when shipping drives tax, clearing retains the prior country for the tax-region update. Delegated update internals limit server-persistence claims.

These are STP/ReactNativeSDK SPI observations, not a supported production integration recipe. Keep the 26.8.0 SetupIntent-first and `succeeded` findings intact as history. The 20-second merchant-update timeout and multi-scene presenter warning are unchanged, not new 26.9.0 features.

### Permissions, Link preview and Apple Pay limits

FinancialConnectionsSheet gains STP SPI `hasRequestedDataPermissions`, default false, forwarded to its API client. LinkAccountSession decodes `permissions` with an empty-array fallback. Public sheet presentation rejects a payment-details host result as unsupported rather than exposing a new public success result. Excluded API/host internals prevent claims about consent or actual data access.

Link preview rendering changes `unparsable` to `generic`, using a Link icon and card-category preview. The excluded decoder/UI internals prevent concluding that arbitrary unknown methods are accepted. Several confirmation and UI helpers gain MainActor isolation.

New internal Apple Pay helpers map automatic/full billing-address collection to postal address, always-name to billing name, and always-email/phone to shipping contact fields. The relevant changed wallet callers, wrapper and context are not retained at this SHA. This is helper-level evidence, not proof of actual Apple Pay request behavior, Express Checkout readiness or general availability. Eight retained podspecs only bump versions, without a deployment-floor change.

### Grounding excerpts

> `if let paymentIntent = response.paymentIntent {`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-841b697/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift:434`

> `case completed(paymentStatus: Session.Status.PaymentStatus)`
>
> `raw/github/stripe/stripe-ios/supplements/2026-09-30-841b697-f58a4b7c/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/CheckoutController.swift:379`

> `initialSelection: initialPaymentOption.map(RowButtonType.init)`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-841b697/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElement.swift:134`

> `permissions: response["permissions"] as? [String] ?? [],`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-841b697/files/StripePayments/StripePayments/Source/API Bindings/Models/ACH/LinkAccountSession.swift:51`

## `stripe-ios@26.10.0` Integration Delta

### Announced PaymentSheet support versus API bindings

The release announces PaymentSheet support for Naver Pay, Korean cards, PAYCO and SeQura. This advances the release-note coverage beyond 26.9.0's API-binding announcement; it does not announce Kakao Pay PaymentSheet support. Availability/form factories are outside the capsule, so do not infer merchant eligibility, country/currency coverage, complete integration steps or runtime success from these notes.

### PaymentIntent mandate inference

`STPPaymentIntentConfirmParams.mandateDataIfRequired` removes `krCard` and `naverPay` from the inferred-mandate list; `kakaoPay` remains. The getter still returns explicitly supplied mandate data before computing a default. `STPSetupIntentConfirmParams` is unchanged by hash and retains the prior list, including Korean cards and Naver Pay. Preserve the 26.9.0 behavior as history: this delta is PaymentIntent-specific SDK inference, not a universal removal of mandate requirements.

### Branding, Identity and Embedded rendering

The new `financialConnectionsLinkBrandOverride` helper returns explicit Onelink, otherwise account Onelink, otherwise nil. Explicit ordinary Link does not force that helper's override. The general `resolvedLinkBrand` logic is unchanged; do not replace its precedence with this narrow Financial Connections rule. Downstream consumers are excluded.

Identity configuration gains SPI `BiometricConsentConfiguration.hideBrandingHeader` and optional `biometricConsent`; the public brand-logo initializer leaves it nil. Native initialization passes the whole configuration to the flow controller. This configures a branding header, not consent suppression or verification bypass. Actual controller and consent-screen implementation is excluded.

Embedded initial selection restoration adds the change button and sublabel without animation. `addChangeButton(animated:)` defaults to true for other callers; its false branch sets the visible alpha after height adjustment. Excluded RowButton internals and lack of device testing limit broader UI-equivalence claims.

### Checkout Apple Pay and other announcements

`ApplePayConfirmationParameters` gains `shippingAddressRequired`; the retained Payment Element caller passes false and calls a session-aware Apple Pay confirmation helper. Changed wallet helpers, context and outer controller are excluded at this SHA. This is caller-level evidence, not a general optional-shipping rule, merchant-facing option, Express Checkout readiness claim or proof of complete Apple Pay behavior.

README and release notes add Arabic (Saudi Arabia). Alpha CryptoOnramp notes add Canada SIN, Colombia NIT and Philippines TIN to `IdType`, plus `idType` to `KycInfo` initialization; those implementations are not retained. Eight retained podspecs change only their versions, without a deployment-floor change.

### Grounding excerpts

> "Added support for Naver Pay."
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/files/CHANGELOG.md` - 26.10.0 PaymentSheet section

> `return _mandateData`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/files/StripePayments/StripePayments/Source/API Bindings/Models/PaymentIntents/STPPaymentIntentConfirmParams.swift` - explicit mandate getter precedence

> `addChangeButton(animated: false)`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentMethodsView.swift` - initial selection restoration

> `shippingAddressRequired: false`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift` - Payment Element Apple Pay caller

## `stripe-ios@26.11.0` Additive Baseline

### Checkout without a selected payment method

`makeConfirmationFlow` accepts an optional PaymentElement and first selects `.withoutPaymentMethod` when `session.paymentOption == nil`. Only a session with a selected option requires the element. Its authentication context uses configured element appearance or a default. The approved current controller supplement shows `confirm(from:)` resolving a presenter, forwarding its optional element to this builder, rejecting an invalid flow and otherwise calling the confirmation engine. This remains STP/ReactNativeSDK SPI, not a generally available merchant integration recipe.

The new request uses the session ID and amount, nil payment-method ID/type, return URL, attribution and optional session email. The branch has no zero-amount condition; it does not prove complete free-order or subscription support. Existing closed-session, concurrent-confirmation and pending-update guards remain. Conventional method confirmation still performs preconfirmation, builds its request, commits a returned session and maps the result. Manual-approval, failed-submission and orchestration responses still fail; PaymentIntent retains precedence over SetupIntent.

### Missing Intent and polling result semantics

A response with neither PaymentIntent nor SetupIntent now sets `clientCompletedIntent` to nil instead of failing immediately. Open sessions still poll. A completed polling outcome sets `didPollToCompletion`; timeout proceeds without setting it. In the nil-Intent branch only that flag changes reconstructed session status to complete, without forcing payment status to paid.

> [!warning] SDK completion can leave the session open
> After a nil-Intent response and polling timeout, successful response decoding can still reach `.completed(updatedResponse)` with the original open session status and unchanged payment status. This is a retained-code finding, not a runtime reproduction. SDK completion proves neither session completion nor settlement; use server-side payment evidence before fulfillment.

Existing reconstruction remains version-qualified: succeeded PaymentIntent sets complete/paid, processing PaymentIntent sets complete without forcing paid, and succeeded SetupIntent sets complete. The current supplemental controller exposes completed/canceled/failed and paid/unpaid/no-payment-required results. Its other session/update behavior is current evidence, not all newly introduced at 26.11.0: the immediate prior controller was not retained. Older controller/poller supplements are not substitutes for current evidence.

### Scalapay and mandate inference

Scalapay gains the `scalapay` identifier, enum case before `unknown`, response property/decoder, parameter factory/convenience initializer and form serialization. Response models retain all response fields; params have no typed method-specific fields but allow additional API parameters. An optional billing argument does not establish that billing is optional on the backend. The payment handler includes Scalapay among methods for which `processing` alone is not success. PaymentSheet support is announced in release notes; excluded availability/form factories prevent an eligibility or complete UI-support claim from the bindings alone.

PaymentIntent inferred-mandate handling removes Kakao Pay. Explicitly supplied mandate data still wins. Do not generalize this PaymentIntent change to SetupIntent or to backend mandate requirements.

### Link, Identity, Apple Pay and historical annotations

`PaymentSheet.LinkConfiguration.Display.walletButtonHidden` documentation now shows the button/row when an existing Link user is detected and hides it otherwise. `shouldDisplay` remains true for automatic/walletButtonHidden and false for never; the old `shouldShowButton` property is removed. Preserve 26.7.0's unconditional-hiding documentation as history. The downstream visibility consumers are excluded, so this is not device-verified rendering behavior.

Identity adds SPI `PrimaryButtonStyle`, default or custom background/text colors, defaulting to the standard style. Documentation recommends dynamic colors and retains default disabled styling; secondary buttons are unaffected. Rendering implementation is excluded. Checkout's `ApplePayConfirmationParameters` removes `billingDetailsCollectionConfiguration` and its caller argument; this does not prove Apple Pay stops requesting billing information because delegated wallet context is excluded. README/release notes add Welsh. Eight retained podspec changes are version-only, not deployment-floor changes.

The new cumulative changelog retrospectively inserts Kakao Pay PaymentSheet support under 26.10.0. The earlier retained 26.10.0 notes did not announce it; both observations remain valid for their evidence dates. Do not infer the first implementation release from the later annotation. All 2,148 prior changelog lines survive with eleven insertions (ten release-block lines and this one annotation).

### Grounding excerpts

> `if session.paymentOption == nil {`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift:101`

> `clientCompletedIntent = nil`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift:527`

> `if didPollToCompletion {`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift:587`

> `return .completed(updatedResponse)`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift:613`

## `stripe-ios@26.12.0` Additive Baseline

### Alpha partner-terms flows

CryptoOnrampCoordinator adds MainActor `presentTermsAndConditionsIfNeeded(from:)` and `presentTermsOfServiceIfNeeded(from:)`. Each uses available Link account information to retrieve terms for transactionTerms or termsOfService. A notRequired response returns without presenting UI; a required declaration supplies HTML to the matching Link presenter. Acceptance awaits `confirmPartnerTerms` using that declaration ID and account information, discarding the response value. Only accepted results log completion analytics. Canceled results remain distinct and errors use existing mapping. The coordinator remains CryptoOnrampAlpha SPI, not general availability.

Link's separate STP `PartnerTermsResult` has accepted/canceled, whereas the coordinator also handles notRequired. Its shared HTML confirmation helper awaits the acceptance callback before dismissing and resumes in the dismissal completion. Callback failure dismisses and throws; cancellation bypasses acceptance. User attestation now reuses the helper with the same retained callback ordering. API serializers, CryptoOnramp result/model definitions and HTML controller implementation are excluded: this caller evidence does not establish idempotency, durable backend acceptance, HTML sanitization, complete regulatory compliance or merchant eligibility.

### Confirmation-wrapper cleanup

Embedded `_confirm` and FlowController `confirm` remove their Checkout-specific pendingOperations rejection and enqueueSessionUpdate wrapper, calling shared PaymentSheet.confirm directly. General latest-update guards remain. Embedded still prevents reconfirmation and reenables interaction on failure/cancellation; FlowController preserves selected-option and SEPA-mandate checks and completed-Link default persistence.

> [!info] Version-qualified Checkout boundary
> Shared PaymentSheet.confirm still rejects Checkout intents and directs callers to CheckoutController.confirm; the async bridge uses that same entry. Removing these wrappers does not prove unguarded working Checkout confirmation or removal of all concurrency protections. Checkout+Confirm.swift is unchanged by hash, but current outer CheckoutController and session internals changed upstream and are excluded. The 26.11.0 supplemental controller remains historical evidence, not proof of current caller behavior. No runtime safety or new free-order-support claim follows.

### Styling, packaging and announcements

Identity adds STP SecondaryButtonStyle with default/custom background and text colors and a default-valued property. Documentation recommends dynamic colors, retains default disabled styling and leaves primary buttons unaffected. Actual rendering is excluded. Package.swift adds CryptoOnramp localization resources; the eight retained podspecs only bump versions, without a deployment-floor or standalone Apple Pay integration change.

Release notes announce removal of public StripeCryptoOnramp.Image exposure, including linkIconSquare. Its changed implementation is excluded; retained coordinator code still uses the image internally. Do not confuse removal of public access with asset deletion or invent a replacement public API. The announced StripeCore additionalHeaders support for GET/POST/DELETE STP APIs and card-scanning funding-warning fix also lack retained implementation. Header precedence, scanner mechanics and device behavior remain unverified.

The cumulative changelog retrospectively adds card-program-name support for saved methods with CustomerSessions under 26.11.0. That annotation was absent from the earlier snapshot. Preserve the upstream historical label separately from first-implementation attribution; changed display/category/form implementation is excluded. All 2,159 previous changelog lines remain, with twelve insertions.

### Grounding excerpts

> `case .notRequired:`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/files/StripeCryptoOnramp/StripeCryptoOnramp/Source/Components/CryptoOnrampCoordinator.swift:961`

> `declarationId: declaration.id,`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/files/StripeCryptoOnramp/StripeCryptoOnramp/Source/Components/CryptoOnrampCoordinator.swift:966`

> `try await onConfirm()`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Link/LinkController.swift:997`

## `stripe-ios@26.12.1` Additive Baseline

### Pix bindings and mandate inference

Release notes announce Pix API bindings and PaymentSheet support. `STPPaymentMethodType` adds pix before unknown, with identifier `pix` and display name Pix; do not assume every older numeric enum value stays fixed. The SPI generic params factory needs no method-specific params object for Pix, not proof that billing details are optional. PaymentIntent inference honors explicit mandate data first, resolves the supplied method type or params type, and adds Pix only for offSession future usage. The static general PaymentIntent inference list does not add Pix. SetupIntent adds Pix to its inference list while retaining explicit-data precedence. These changes do not establish every setup, recurring or merchant-eligibility scenario.

Next-action decoding recognizes `pix_display_qr_code` and exposes `STPIntentActionPixDisplayQrCode`. QR data, PNG/SVG image URLs and expiry are optional. Although the public hostedInstructionsURL property is optional, decoding requires a parseable string URL; invalid details downgrade the action to unknown. URL parsing alone is not absolute-HTTPS validation. Unix-seconds expiry becomes Date. The model description redacts QR data but still prints URLs and retains allResponseFields, not complete sensitive-data redaction.

### Hosted instructions, polling and compatibility

The handler requires hosted instructions and PaymentSheetAuthenticationContext, otherwise failing as unsupported. It passes the optional return URL to the redirect helper with useWebAuthSession false; that helper tries native URL opening before its Safari fallback. Its completion requests Pix polling. Pending Pix QR action or processing alone is not treated as client success.

The exact-SHA supplemental polling files establish client settings: no displayed countdown, a configured two-second retry interval, API expiry when present and a 24-hour fallback. Appearance/foreground schedules polling after five seconds; background/disappearance suspends it. At the deadline, polling suspends and a final force poll is scheduled three seconds later. These are client scheduling settings, not a guaranteed request cadence or backend expiry. Pending results remain pending; success updates the action Intent and reports succeeded. Failure or a non-success deadline enters error UI, hides cancel, shows back, dismisses Safari if present and completes as canceled. User cancellation also reports canceled. Generic IntentStatusPoller and action-result mapping are excluded.

> [!warning] Still-pending Pix can reach redirect cancellation
> `STPPaymentHandler.swift:1696` exempts only PayNow and PromptPay from cancellation when redirect retrieval still requires action. The retained PollingBudget initializer has no Pix-specific budget. Consequently this path can complete canceled for still-pending Pix after redirect return/dismissal instead of leaving completion solely to the polling UI. This is a code-path risk, not a device reproduction; concurrency/UI effects remain unverified. A canceled SDK result is not proof that no bank payment occurred.

The STP protocol `presentPollingVCForAction` changes its action from PaymentIntent-specific to shared STPPaymentHandlerActionParams; Embedded and FlowController conformers change accordingly. This is an incompatible signature for custom SPI conformers, not a general merchant public API break. The Pix branch does not reject SetupIntent action parameters, but excluded shared mapping prevents inferring complete SetupIntent/recurring support.

### Pre-collected Financial Connections consent

Callback/async present and presentForToken overloads accept optional preCollectedConsent, store it on the sheet and forward it to the host. The supplemental public NSObject type holds a Stripe-issued consent object ID and collectedAt as Unix seconds. Capture actual affirmative acceptance of the complete issued text; preserve that timestamp across retries/reopening, rather than replacing it with launch time. The SDK does not validate the ID, timestamp plausibility, expiry or clock skew. Server evaluation determines whether its consent pane can be skipped; supplying evidence is not guaranteed bypass.

The new overloads assign stored state at lines 211, 237, 323 and 349; host forwarding is at line 426. Old overloads and dismissal do not clear it. On a reused sheet, an old overload can inherit earlier consent; explicitly passing nil through a new overload resets it. This is retained state behavior, not proof that the backend accepts stale evidence. Release-note claims about preserving no_eligible_accounts in onEvent and session-context diagnostics lack the changed host/event implementation and remain announcements.

### Checkout, CryptoOnramp and historical attribution

Checkout+Confirm removes the new-method branch's missing billing-email fallback from session.email before creating the PaymentMethod. Its no-method customerData email mapping remains, as do confirmation guards and the earlier nil-Intent/poll-timeout completion caution. The comment about legacy email requirements is upstream commentary, not live API verification. This does not establish a global email-requirement change or general public Checkout support; current outer controller/API/Apple Pay context is excluded.

Alpha CryptoOnramp post-auth failure now passes the error and available PaymentIntent into checkoutError. The excluded helper prevents independently verifying exact error-field preservation. The current cumulative changelog inserts error/decline/type preservation and `uploadFile(at:purpose:authorizationSecret:progress:)` with FileUploadError SPI under 26.12.0. Preserve these later annotations without rewriting that older raw evidence or claiming the first implementation at its SHA. Legacy StripeFile purpose conversion maps cryptoOnrampKYCDocument to unknown, not new legacy-upload support.

All 2,171 prior cumulative changelog lines remain byte-identical, with 13 inserted lines: eleven in the new release block and two retrospective annotations. Eight podspecs only bump versions, retaining iOS 15 and Swift 5 declarations; no standalone Apple Pay integration or deployment-floor change is established.

### Grounding excerpts

> `func presentPollingVCForAction(action: STPPaymentHandlerActionParams, type: STPPaymentMethodType, safariViewController: SFSafariViewController?)`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/files/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift:2761`

> `} else if paymentMethodType != .paynow && paymentMethodType != .promptPay {`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/files/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift:1696`

> `self.complete(with: .canceled)`
>
> `raw/github/stripe/stripe-ios/supplements/2026-10-02-9f0d5aa-8ad0f8dd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/ViewControllers/PollingViewController.swift:296`

> "Supplying it does not"
> "guarantee that Financial Connections will skip its consent pane."
>
> `raw/github/stripe/stripe-ios/supplements/2026-10-02-9f0d5aa-8ad0f8dd/files/StripeCore/StripeCore/Source/Connections Bindings/FinancialConnectionsPreCollectedConsent.swift:11-12`

> `self.preCollectedConsent = preCollectedConsent`
>
> `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/files/StripeFinancialConnections/StripeFinancialConnections/Source/FinancialConnectionsSheet.swift:211`

## Completion and Delayed Methods

`PaymentSheetResult` returns `completed`, `canceled`, or `failed`. `completed` is the end of the SDK interaction, not settlement proof. The source explicitly directs merchants to transition to a generic receipt and fulfill only after receiving a successful Stripe payment event.

`allowsDelayedPaymentMethods` enables methods that may settle later or require subsequent customer action, including bank debits and voucher-style methods. When enabled, webhook handling is mandatory for success and failure determination.

## Apple Pay

`STPApplePayContext` presents Apple Pay, creates a PaymentMethod from `PKPayment`, delegates Intent confirmation, and reports completion. It supports async delegate methods, request customization, shipping updates, coupon changes, explicit dismissal, and presentation without requiring the old retained view-controller pattern.

The `StripeApplePay` module is the lightweight option for Apple Pay-only integrations and App Clips. Apple Pay completion is still subject to server-side event verification before fulfillment.

## Low-Level Payments and Authentication

`STPAPIClient` exposes callback and async operations for PaymentMethods, tokens, legacy Sources, PaymentIntents, SetupIntents, microdeposit verification, and Radar Sessions. It also exposes Apple Pay conversions and payment-method-specific option models.

`STPPaymentHandler` confirms PaymentIntents and SetupIntents and handles redirects, app-to-app flows, and native 3DS2 authentication through `STPAuthenticationContext`. Current method names explicitly identify PaymentIntent or SetupIntent operations; older generic methods remain deprecated aliases.

The retained models cover cards, bank accounts, Link, Alipay, BLIK, Cash App Pay, PayPal, PayPay, Revolut Pay, Swish, TWINT, WeChat Pay, Wero, and other methods. Model presence is not proof that PaymentSheet supports every method or that a merchant can enable it.

## Specialized Product Modules

### Connect

`EmbeddedComponentManager` creates account onboarding, account management, payment details, notification banner, payouts, payments, and check-scanning components. Payments and Payouts became public API in `26.3.0`. The client still depends on server-created access credentials and product eligibility.

### Financial Connections

`FinancialConnectionsSheet` presents a server-created Financial Connections Session and returns session or token-oriented results. It exposes callback and async presentation and optional event handling.

### Identity

`IdentityVerificationSheet` presents document and selfie verification from a server-created Verification Session client secret. The retained API includes configuration, presentation, and explicit completed, canceled, and failed outcomes.

### Crypto Onramp

The alpha `CryptoOnrampCoordinator` covers Link account discovery and authentication, KYC, compliance identifiers, user attestation, wallet registration and ownership verification, payment-method collection, crypto payment-token creation, and checkout. Alpha and private-preview APIs must not be represented as generally available.

### Issuing

`STPPushProvisioningContext` supports adding Issuing cards to Apple Wallet. `STPPinManagementService` remains public but is deprecated in favor of Issuing Elements.

## Platform and Migration Requirements

| Requirement | `26.4.1` baseline |
| --- | --- |
| iOS | 15+ |
| iOS 13/14 fallback | `stripe-ios@25.17.0` |
| Catalyst | macOS 12+ |
| Package managers | Swift Package Manager and CocoaPods supported |
| Carthage | Binaries published, but CLI integration no longer officially tested |

Version 26 raises the deployment target from iOS 13 to iOS 15. Version 25 broadly adopts async APIs and strict-concurrency annotations, makes Customer Sessions and Confirmation Tokens generally available, renames several payment APIs, and removes deprecated Source-era behaviors. Applications crossing either major version must follow `MIGRATING.md` and regression-test payment completion, redirects, 3DS, delayed methods, saved methods, Apple Pay, and Swift concurrency.

## Version History

### `stripe-ios@26.12.1`

Published 2026-09-28 (matching notes heading); approved full additive ingest from stripe-ios@26.12.0 with focused reading and a three-file exact-SHA supplement. Full overrides generated delta because the STP polling signature is incompatible. Adds Pix and consent/confirmation findings without replacing older baselines. Retrospective annotations remain distinct from original release evidence. See [[changelog-github-stripe-ios]]; this is ingest progress, not a latest-upstream claim.

### `stripe-ios@26.12.0`

Release metadata records publication on 2026-09-22; the notes heading says 2026-09-21. Approved full additive ingest from stripe-ios@26.11.0 with focused reading, overriding generated delta because of the announced public alpha Image API removal. Adds the bounded findings above and preserves prior history. See [[changelog-github-stripe-ios]]; this is ingest progress, not a latest-upstream claim.

### `stripe-ios@26.11.0`

Released 2026-09-14; approved full additive ingest from `stripe-ios@26.10.0`, overriding the generated delta recommendation because confirmation behavior changes broadly. Focused reading and the one-file current controller supplement preserve all earlier history. The retrospective Kakao Pay annotation is distinguished from original release evidence. See [[changelog-github-stripe-ios]]; this is ingest progress, not a latest-upstream claim.

### `stripe-ios@26.10.0`

Release metadata records publication on 2026-09-09; the upstream notes use a 2026-09-08 heading. Approved bounded delta from `stripe-ios@26.9.0`, using focused reading. Adds the announcements and scoped implementation findings above. Older cumulative changelog content beginning at 26.9.0 is byte-identical. See [[changelog-github-stripe-ios]]; this is ingest progress, not a latest-upstream claim.

### `stripe-ios@26.9.0`

Released 2026-08-31; approved full additive ingest from `stripe-ios@26.8.0`, with focused reading and two exact-SHA supplemental files. Adds payment-method bindings and broad Checkout polling/confirmation/SPI findings above. The cumulative changelog adds only four release lines, preserving all 2,131 older lines. See [[changelog-github-stripe-ios]]. This is ingest progress, not a latest-upstream claim.

### `stripe-ios@26.8.0`

Released 2026-08-24; approved full additive ingest from `stripe-ios@26.7.0` with the focused-reading exception and two-file exact-SHA supplement. Adds the Checkout confirmation baseline, FPX mappings, decline-text fix, Link permissions and low-level option findings above. Historical knowledge and exclusions remain version-qualified. See [[changelog-github-stripe-ios]].

### `stripe-ios@26.7.0`

Released 2026-08-17; approved delta from `stripe-ios@26.6.0`. Adds the Lite packaging migration, Link button-hiding option, autocomplete configuration changes and typed Vipps findings above. Three changelog insertions preserve all 2,103 prior lines. Historical annotations and current Checkout evidence gaps remain explicit. See [[changelog-github-stripe-ios]].

### `stripe-ios@26.6.0`

Released 2026-08-10; full additive ingest from `26.5.0` because collection policy expands and confirmation architecture changes. Adds the MB WAY/Bizum, preview Link error, and alpha wallet-deletion findings above. The newly retained Checkout implementation is explicitly unfinished. The cumulative changelog adds only the 26.6.0 block; 2,092 historical lines are unchanged. See [[changelog-github-stripe-ios]] for exact release and comparison evidence.

### `stripe-ios@26.5.0`

Released 2026-08-03; ingested as a delta from `stripe-ios@26.4.1`. The release notes identify private-preview Link billing/appearance customization and alpha Tempo registration; retained source additionally exposes the selection, presentation, and internal confirmation changes above.

**Retrospective annotations:** the new cumulative changelog adds SwiftUI multi-scene presentation and Link default-selection notes under `26.4.1`, plus a Connect onboarding first-dismissal callback note under `26.4.0`. Those annotations are absent from the old retained snapshot. Record them as newly observed upstream historical annotations, not proof that the older retained SHA contains the implementation or that every added bullet belongs to `26.5.0`. Connect implementation is excluded. Exact release and comparison links are in [[changelog-github-stripe-ios]].

### `stripe-ios@26.4.1`

The exact patch fixes some successful Alipay payments being incorrectly reported as failures. It does not introduce the broader architecture summarized above.

### Accumulated `25.15.0--26.4.0` Context

- `25.15.0--25.17.0` adds Onelink, saved-card art, Identity manual capture, richer Crypto Onramp errors, and the `InstantBankPaymentsController` rename.
- `26.0.0` raises the minimum iOS version to 15.
- `26.1.0--26.2.0` fixes Swift Package Manager and CustomerSheet issues and revises alpha Crypto Onramp attestation and error contracts.
- `26.3.0` adds alpha wallet-ownership verification, private-preview standalone Link APIs, and public Connect Payments/Payouts components.
- `26.4.0` makes `STPAPIClient.betas` public and separates private-preview Link SetupIntent confirmation.

These milestones come from the cumulative changelog, not automated comparisons against every intermediate release.

### Legacy `stripe-ios@25.14.0`

The May 2026 manual capsule established the modular SDK, PaymentSheet, FlowController, Embedded Payment Element, CustomerSheet, Apple Pay, low-level API bindings, 3DS handling, localization, and the iOS 13 platform floor. Those findings remain queryable and are extended rather than replaced.

## Integration Guidance

- Prefer PaymentSheet for a maintained prebuilt checkout, FlowController for merchant-owned composition, and Embedded Payment Element for inline payment-method UI.
- Create Intents and customer or session credentials on the backend; return only publishable configuration and client secrets to the app.
- Treat `completed` as completion of the SDK interaction, not settlement evidence; fulfill from successful server-side events.
- Verify payment-method, country, currency, connected-account, and preview eligibility independently of public API presence.
- Use Apple in-app purchase APIs for digital products or services consumed in the app, subject to current policy and regional rules.
- Review `MIGRATING.md` before major upgrades and pin `25.17.0` when iOS 13 or 14 support remains mandatory.

## Related

- Company: [[stripe]]
- Concept: [[stripe-ios-sdk]]
- Native counterpart: [[source-github-stripe-android]]
- React Native bridge: [[source-github-stripe-react-native]]
- Higher-level billing SDK: [[source-stripe-billing-ios-sdk]]
- History: [[changelog-github-stripe-ios]]

## Raw Sources

- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/manifest.json` - exact-SHA 26.12.1 capsule; all retained paths and hashes
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.12.1/2026-09-30/manifest.json` - package-qualified release identity/publication
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.12.1/2026-09-30/release-notes.md` - announcements
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.12.0--26.12.1/comparison.json` - comparison; adjacent comparison.md and diff.patch
- `raw/github/stripe/stripe-ios/supplements/2026-10-02-9f0d5aa-8ad0f8dd/manifest.json` - consent type and polling controller/model evidence
- `tracking/github/repos/stripe/stripe-ios/evidence-attachments/github-722f2ffc82b5d6e5375c/attachment.json` - approved attachment
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/files/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift` - Pix redirect, status and SPI signature
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/files/StripePayments/StripePayments/Source/PaymentHandler/PollingBudget.swift` - fully read affected dependency; no Pix-specific redirect budget
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/files/StripePayments/StripePayments/Source/API Bindings/Models/Shared/STPIntentActionPixDisplayQrCode.swift` - QR decoding, expiry and description
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/files/StripePayments/StripePayments/Source/API Bindings/Models/PaymentIntents/STPPaymentIntentConfirmParams.swift` - offSession Pix mandate inference and explicit precedence
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/files/StripePayments/StripePayments/Source/API Bindings/Models/SetupIntents/STPSetupIntentConfirmParams.swift` - SetupIntent inference, distinct from PaymentIntent
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/files/StripeFinancialConnections/StripeFinancialConnections/Source/FinancialConnectionsSheet.swift` - consent overloads, state and forwarding
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift` - email fallback removal and confirmation limits
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/files/CHANGELOG.md` - new block and later historical annotations
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/files/StripeCryptoOnramp/StripeCryptoOnramp/Source/Components/CryptoOnrampCoordinator.swift` - post-authentication error/Intent forwarding; helper excluded
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/manifest.json` - exact-SHA 26.12.0 capsule
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.12.0/2026-09-30/manifest.json` - release identity/publication date
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.12.0/2026-09-30/release-notes.md` - announcements
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.11.0--26.12.0/comparison.json` - comparison; comparison.md and diff.patch accompany it
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/files/StripeCryptoOnramp/StripeCryptoOnramp/Source/Components/CryptoOnrampCoordinator.swift` - terms requirements, presentation and acceptance caller
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Link/LinkController.swift` - HTML confirmation callback ordering
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElement+Internal.swift` - scoped queue-wrapper removal
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetFlowController.swift` - confirmation guards and direct caller
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+API.swift` - retained shared confirmation entry and async bridge, targeted dependency read
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/files/StripeIdentity/StripeIdentity/Source/IdentityVerificationSheet.swift` - secondary-button styling
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/files/Package.swift` - localization packaging
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/files/CHANGELOG.md` - release block and retrospective annotation

- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/manifest.json` - exact-SHA 26.11.0 capsule
- `raw/github/stripe/stripe-ios/supplements/2026-10-02-7037819-bd3ee3a4/manifest.json` - approved current controller supplement
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.11.0/2026-09-30/manifest.json` - package-qualified release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.11.0/2026-09-30/release-notes.md` - release announcements
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.10.0--26.11.0/comparison.json` - comparison; comparison.md and diff.patch accompany it
- `tracking/github/repos/stripe/stripe-ios/evidence-attachments/github-266fd96ba1fdc3d98b71/attachment.json` - supplement attachment
- `raw/github/stripe/stripe-ios/supplements/2026-10-02-7037819-bd3ee3a4/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/CheckoutController.swift` - current SPI caller and result contract
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift` - no-method confirmation and missing-Intent reconstruction
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetConfiguration.swift` - revised Link visibility documentation
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/files/StripeIdentity/StripeIdentity/Source/IdentityVerificationSheet.swift` - SPI primary-button styling
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/files/StripePayments/StripePayments/Source/API Bindings/Models/PaymentMethods/STPPaymentMethodParams.swift` - Scalapay parameter construction and serialization
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/files/StripePayments/StripePayments/Source/API Bindings/Models/PaymentIntents/STPPaymentIntentConfirmParams.swift` - PaymentIntent mandate inference
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/files/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift` - Scalapay processing classification
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/files/CHANGELOG.md` - new release and retrospective Kakao Pay annotation

- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/manifest.json` - exact-SHA 26.10.0 capsule
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.10.0/2026-09-30/manifest.json` - release identity and publication date
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.10.0/2026-09-30/release-notes.md` - PaymentSheet, localization and alpha announcements
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.9.0--26.10.0/comparison.json` - identities; comparison.md and diff.patch accompany it
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/files/StripePayments/StripePayments/Source/API Bindings/Models/PaymentIntents/STPPaymentIntentConfirmParams.swift` - mandate inference and explicit precedence
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentElementConfiguration.swift` - Financial Connections branding helper
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/files/StripeIdentity/StripeIdentity/Source/IdentityVerificationSheet.swift` - SPI branding-header configuration
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentMethodsView.swift` - restoration animation
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift` - bounded Apple Pay caller evidence

- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-841b697/manifest.json` - exact-SHA 26.9.0 capsule
- `raw/github/stripe/stripe-ios/supplements/2026-09-30-841b697-f58a4b7c/manifest.json` - approved controller/poller supplement
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.9.0/2026-09-30/manifest.json` - release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.9.0/2026-09-30/release-notes.md` - API-binding announcements
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.8.0--26.9.0/comparison.json` - inventory; comparison.md and diff.patch accompany it
- `tracking/github/repos/stripe/stripe-ios/evidence-attachments/github-bbbff15398aa9f59171d/attachment.json` - supplemental evidence linkage
- `raw/github/stripe/stripe-ios/supplements/2026-09-30-841b697-f58a4b7c/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/CheckoutController.swift` - SPI result and configuration contract
- `raw/github/stripe/stripe-ios/supplements/2026-09-30-841b697-f58a4b7c/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/CheckoutSessionPoller.swift` - polling budget, retries and outcomes
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-841b697/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift` - shared confirmation and client response reconstruction
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-841b697/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm+Link.swift` - Link confirmation routing
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-841b697/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetConfiguration.swift` - internal Apple Pay contact-field helpers
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-841b697/files/StripeFinancialConnections/StripeFinancialConnections/Source/FinancialConnectionsSheet.swift` - permissions flag and public result limits
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-841b697/files/StripePayments/StripePayments/Source/API Bindings/Models/PaymentMethods/STPPaymentMethodParams.swift` - new payment-method parameters
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-841b697/files/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift` - processing-state classification

- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/manifest.json` - exact-SHA 26.8.0 capsule
- `raw/github/stripe/stripe-ios/supplements/2026-09-30-8444041-bea35b75/manifest.json` - approved two-file supplement
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.8.0/2026-09-30/manifest.json` - release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.8.0/2026-09-30/release-notes.md` - announcements
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.7.0--26.8.0/comparison.json` - comparison inventory; comparison.md and diff.patch accompany it
- `tracking/github/repos/stripe/stripe-ios/evidence-attachments/github-4ef7ad96d01f40cfff58/attachment.json` - supplement attachment
- `raw/github/stripe/stripe-ios/supplements/2026-09-30-8444041-bea35b75/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/CheckoutController.swift` - SPI entry point and result contract
- `raw/github/stripe/stripe-ios/supplements/2026-09-30-8444041-bea35b75/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm+ApplePay.swift` - delegated wallet wrapper, not its underlying context
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift` - typed confirmation flows and mapping
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm+Link.swift` - Link confirmation result handling
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+API.swift` - Checkout rejection and SetupIntent option boundary
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Link/LinkConfiguration.swift` - preview permissions
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Link/LinkController.swift` - permission configuration propagation
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePayments/StripePayments/Source/API Bindings/Models/Shared/LinkSettings.swift` - consent-string decoder
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePayments/StripePayments/Source/API Bindings/Models/STPFPXBankBrand.swift` - bank mappings
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift` - decline-text priority
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePayments/StripePayments/Source/API Bindings/Models/PaymentIntents/STPConfirmAlipayOptions.swift` - currency and future usage
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePayments/StripePayments/Source/API Bindings/Models/PaymentIntents/STPConfirmKlarnaOptions.swift` - private-preview tokens
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/files/StripePayments/StripePayments/Source/API Bindings/Models/SetupIntents/STPSetupIntentConfirmParams.swift` - option encoding and mandate handling

- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/manifest.json` - exact-SHA 26.7.0 capsule
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.7.0/2026-09-30/manifest.json` - package release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.7.0/2026-09-30/release-notes.md` - announcements
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.6.0--26.7.0/comparison.json` - upstream inventory; comparison.md and diff.patch accompany it
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/files/MIGRATING.md` - Lite installation requirement
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/files/Package.swift` - module dependency declarations
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetConfiguration.swift` - Link visibility and removed SPI
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/CustomerSheet/CustomerSheet.swift` - server-driven autocomplete flag
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElement.swift` - selection visibility caller
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/files/StripePayments/StripePayments/Source/API Bindings/Models/PaymentMethods/STPPaymentMethodParams.swift` - Vipps request support
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/files/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift` - Vipps processing-state classification

- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/manifest.json` - exact-SHA 26.6.0 expanded capsule
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.6.0/2026-09-30/manifest.json` - package release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.6.0/2026-09-30/release-notes.md` - release announcements
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.5.0--26.6.0/comparison.json` - upstream dispositions and identities; comparison.md and diff.patch accompany it
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift` - authorization-context guards
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Link/LinkController.swift` - preview error handling
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripeCryptoOnramp/StripeCryptoOnramp/Source/Components/CryptoOnrampCoordinator.swift` - alpha deletion contract
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout.swift` - session operations and unfinished confirmation-result mapping
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm.swift` - new confirmation owner
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Confirm+Link.swift` - delegated Link confirmation
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+Session+Internal.swift` - session/tax/payment-status semantics
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Checkout+BillingAddress.swift` - billing-sync gate
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+API.swift` - shared preconfirmation and Checkout rejection
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Express Checkout Element/ExpressCheckoutElementUIView.swift` - unfinished button actions
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Checkout/Shipping Address Element/ShippingAddressElement.swift` - unfinished completion delegate
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/manifest.json` - exact-SHA `26.5.0` capsule
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.5.0/2026-09-29/manifest.json` - package release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.5.0/2026-09-29/release-notes.md` - private-preview Link and alpha Tempo announcements
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.4.1--26.5.0/comparison.json` - classified comparison; `diff.patch` in the same directory retains the complete selected-file diff
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Link/LinkConfiguration.swift` - optional billing override
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Link/LinkAppearance.swift` - preview appearance surface
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Link/LinkController.swift` - override application and preview flow
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetConfiguration.swift` - additive billing initializer
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedFormViewController.swift` - cancellation reconstruction
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElement+Internal.swift` - pending billing sync and restoration caller
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedViewRepresentable.swift` - own-window presentation
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetFlowController.swift` - selection snapshot caller
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+CheckoutSessionAPI.swift` - confirmation branches
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/manifest.json` - exact-SHA `26.4.1` bounded source capsule
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.4.1/2026-07-31/manifest.json` - package-qualified release record
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.4.1/2026-07-31/release-notes.md` - exact upstream release note
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/README.md` - purpose, security, modules, policy boundary, and requirements
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/MIGRATING.md` - major-version migration requirements
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/CHANGELOG.md` - cumulative upstream release history
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/Package.swift` - product, target, dependency, and platform inventory
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet.swift` - result and prebuilt-sheet contract
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetConfiguration.swift` - configuration and delayed-method boundary
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetFlowController.swift` - custom-flow contract
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElement.swift` - inline element lifecycle
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripeApplePay/StripeApplePay/Source/ApplePayContext/STPApplePayContext.swift` - Apple Pay lifecycle
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePayments/StripePayments/Source/API Bindings/STPAPIClient+Payments.swift` - low-level payment operations
- `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/StripePayments/StripePayments/Source/PaymentHandler/STPPaymentHandler.swift` - confirmation, redirects, and 3DS handling
- `raw/github-stripe-ios.md` - legacy `25.14.0` capsule pointer

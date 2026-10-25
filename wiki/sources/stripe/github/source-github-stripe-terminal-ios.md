---
title: "GitHub: stripe/stripe-terminal-ios"
type: source
date_ingested: 2026-08-31
date_updated: 2026-10-25
original_format: github-repo
raw_files:
  - "github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/manifest.json"
  - "github/stripe/stripe-terminal-ios/snapshots/2026-10-25-00cd46d/manifest.json"
  - "github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/manifest.json"
tags: [stripe, terminal, ios, swift, mobile, sdk, card-present, tap-to-pay, offline-payments, github-repository]
---

## Overview

`stripe/stripe-terminal-ios` distributes Stripe's proprietary native iOS SDK for custom in-person checkout. This cumulative page establishes the approved `StripeTerminal@5.8.0` baseline at exact commit `c027d6dc2258c774412cb7933cbb959488c16b63` from public headers, the open-source example application, support policy, and release history.

Additive ingests on 2026-10-25 retain the `5.8.1` maintenance delta and the `6.0.0` full major boundary at `79cfb3225553a7a5cceb8325f1c1f9087f792128`. The general sections below retain the v5 baseline; the version-qualified v6 section overrides incompatible APIs and defaults without deleting that history.

Repository: <https://github.com/stripe/stripe-terminal-ios>

## Evidence Boundary

- Stripe states that the SDK implementation is proprietary and closed source. The retained public headers are authoritative for the exposed API contract, while the example application demonstrates integration patterns rather than internal runtime behavior.
- The v5 capsule retains 235 files: 169 public API files, 60 example files, build metadata, documentation, license, and release history. The v6 capsule retains 243 files. Tests, generated binaries, assets, CI, and unrelated tooling are excluded.
- API presence does not prove merchant eligibility, country or currency availability, preview access, reader firmware compatibility, or account configuration.
- Several retained surfaces are preview-gated or conditionally compiled, including surcharging, MOTO, collect-data, Tap to Pay offline mode, and USB support.
- An SDK completion does not independently prove capture or settlement. Manual-capture integrations must synchronously notify their backend to capture, and fulfillment should follow server-side payment state.

## Package Status

| Package | Latest ingested release | Exact SHA | Evidence status |
| --- | --- | --- | --- |
| `StripeTerminal` v6 | `6.0.0` | `79cfb3225553a7a5cceb8325f1c1f9087f792128` | Approved additive full ingest; v5 history preserved |
| `StripeTerminal` v5 | `5.8.1` | `00cd46de3ad9a7847c5d8ccb30abcf311a1e26e0` | Approved delta; 5.8.0 baseline preserved |

This table reports wiki ingest progress, not the latest release published upstream.

## Platform and Installation (v5 Baseline)

- `StripeTerminal@5.8.0` requires iOS 15 or later. Its binary Swift Package target downloads `StripeTerminal.xcframework` for the exact `5.8.0` release; CocoaPods supports `pod 'StripeTerminal', '~> 5.0'`.
- Location services are mandatory for accepting payments. Bluetooth reader integrations also require the Bluetooth usage description and `bluetooth-central` background mode.
- Version 5 is built with Xcode 26 and Swift 6.2. The support policy places 5.x in active development through October 2027 and schedules its hard block for October 2028.
- Major versions follow active, maintenance, and deprecated phases; after the hard-block date, obsolete versions can no longer discover or connect readers or process payments.

## Initialization and Backend Boundary

Call `Terminal.initWithTokenProvider(...)` before accessing `Terminal.shared`. The token provider authenticates to the merchant backend, which creates a fresh Terminal ConnectionToken and returns its secret. The SDK can connect to one reader and perform one operation at a time.

The retained example backend client also owns location listing/creation, internet-reader registration, PaymentIntent capture, and other secret-key operations. Switching Stripe accounts requires disconnecting the reader, clearing cached credentials, changing the token provider's backend identity, and reconnecting with a new token.

## Reader Discovery and Connection

The API exposes Bluetooth scan and proximity discovery, internet-reader discovery, Tap to Pay discovery, and conditionally compiled USB discovery. Mobile and Tap to Pay connections require a Stripe Terminal Location ID. Internet readers can be registered and managed through the backend.

`easyConnect` combines discovery and connection for Tap to Pay and internet readers when a discovery filter identifies exactly one reader. Traditional discovery remains delegate-driven and returns a cancelable operation.

Tap to Pay connections can include a connected account in `onBehalfOf`, a cardholder-facing merchant display name, Terms of Service presentation behavior, and automatic reconnection. The app can independently check whether the relevant account has accepted Apple's Tap to Pay terms.

Modern Bluetooth, USB, and Tap to Pay configurations enable automatic reconnection by default. Integrations must handle reconnect start, success, failure, and ordinary disconnect reasons rather than inferring unexpected disconnects from the global connection status alone.

## Reader Updates

Required reader updates can run during connection and block use until complete. The app must implement update progress and completion UI and keep the device awake and near the reader. Optional updates can be installed through `installAvailableUpdate`.

Test-mode configurations can simulate available, required, required-offline, and low-battery update scenarios. Canceling a required update can make connection fail with an unsupported-reader-version error.

## Payment Lifecycle

Two supported payment patterns coexist:

1. Split flow: create or retrieve a PaymentIntent, call `collectPaymentMethod`, then `confirmPaymentIntent`.
2. Combined flow: call `processPaymentIntent`, which performs collection and confirmation as one cancelable operation.

Collection updates are initially local to the SDK. Confirmation authorizes the payment. For manual capture, the app must synchronously call its backend to capture the PaymentIntent; abandoning an intent after an unknown confirmation result without reconciliation risks duplicate charges.

Collection configuration controls tipping, customer cancellation, offline behavior, payment-method updates, and preview capabilities. Customer cancellation is enabled by default where the reader supports it. Reader-display cart data is presentation-only and does not determine the charged amount.

## Saving Payment Details

SetupIntents support split `collectSetupIntentPaymentMethod` plus `confirmSetupIntent` and combined `processSetupIntent` flows. The app must collect cardholder consent and pass `allowRedisplay`; collection alone does not persist the payment method to Stripe.

In `5.8.0`, `SCPSetupAttemptCardPresentDetails.generatedCardExpanded` and `SCPSetupIntent.paymentMethodExpanded` expose full expanded `SCPPaymentMethod` objects. This reduces follow-up retrieval for supported saving flows but does not remove consent or server-side customer-management requirements.

`readReusableCard` remains a legacy/deprecated approach. Stripe warns that it does not create a card-present transaction and therefore loses card-present pricing and liability benefits; SetupIntents are the maintained saving path.

## Offline Payments

Offline behavior is selected per collection as `preferOnline`, `requireOnline`, or `forceOffline`. A locally created offline PaymentIntent can have no Stripe ID until forwarding; `offlineDetails` supplies a local identifier and whether upload is required. Merchant-defined metadata is important for reconciliation.

The SDK reports offline status for both the app and connected smart reader, including queued counts and currency totals, and announces forwarding progress through `SCPOfflineDelegate`. Once connectivity returns, queued intents must be forwarded and then captured where required. Clearing local application state can therefore affect unresolved offline evidence.

The simulator can independently place the SDK and smart reader in immediate-failure, timeout, or intermittent offline modes. These controls are test-only and fail for live-mode readers. Tap to Pay offline processing entered private preview in 5.6.0 and must not be treated as generally available.

## Refunds (v5 Baseline)

`processRefund` combines collection and confirmation for in-person refund methods such as Interac. The older split refund methods are deprecated. Ordinary refunds that do not require cardholder presence remain server-side or Dashboard operations.

Unknown outcomes require reconciliation: a timeout can leave refund status unknown, while a returned failure reason indicates a declined refund. Interac refund construction requires the original PaymentIntent client secret in version 5.

## Tap to Pay and QR Methods

Tap to Pay requires a retained delegate for reader input, display prompts, update lifecycle, and optional payment-method selection and QR display. QR processing blocks until the app invokes the delegate completion after presenting the code.

The API surface includes WeChat Pay, PayNow, PayPay, Affirm, and Klarna details or selection types. Their presence is not universal availability. QR methods can be region-, reader-, capture-mode-, or preview-constrained and are not interchangeable with offline card-present processing.

## Reader and Checkout Features

- On-reader tipping can use an eligible amount; tip availability also depends on reader and Location configuration.
- Surcharge surfaces expose eligibility, maximum amount, configured amount, and customer-consent collection. The feature remains access- and reader-version-dependent.
- Smart readers can collect selection, signature, email, phone, text, and numeric inputs, with optional toggles.
- Supported readers can print content. `5.8.0` adds an explicit low-battery printing error.
- Supported mobile readers can collect non-payment magstripe or NFC data through preview APIs; this is not payment-card processing.
- Supported readers expose accessibility and buzzer settings. `5.8.0` can read current/max buzzer volume and set low, high, or a custom value from `1...maxVolume`.
- Dynamic currency conversion, MOTO, multicapture, reauthorization, overcapture, donation, and surcharge APIs require independent account, reader, and release checks.

## Errors, Logging, and Testing

The error model distinguishes integration misuse, invalid configuration, network and API errors, card declines, reader and update failures, offline failures, printer failures, and Tap to Pay conditions. Confirmation errors may carry the updated Intent and an API error, which should drive retry decisions.

Version `5.8.0` adds error, warning, and info log levels in addition to verbose and none. Log listeners are diagnostic only and may be invoked on any thread; application behavior must not depend on log text.

The simulator supports card brands, decline and PIN scenarios, input outcomes, offline failures, and reader updates. Simulated success does not replace physical-reader, account-eligibility, connectivity, capture, webhook, or settlement testing.

## Version History

### `StripeTerminal@5.8.0`

Adds buzzer-volume management, expanded SetupIntent payment methods, granular logging, an unknown-device fallback, and a printer-low-battery error. It also corrects Bluetooth disconnect reasons and a Tap to Pay collection crash.

### Version 5 Major Boundary

Version 5 raises the minimum to iOS 15, requires explicit SDK initialization, adds combined process and Swift async APIs, adds a reconnecting status, changes cancellation and connection-state semantics, defaults customer cancellation on where supported, removes P400 support, and deprecates split refund confirmation.

### Accumulated `5.1.0--5.7.0` Context

The retained upstream history adds EasyConnect; internet-reader filtering; mPOS and Tap to Pay QR methods; Tap to Pay compatibility checks; tip eligibility; richer API errors; multicapture and reauthorization previews; simulated offline/update scenarios; Tap to Pay offline private preview; localized API errors; overcapture status; and preview surcharging. These are cumulative-history findings, not independent comparisons of every release.

## Integration Guidance

- Keep secret-key operations, ConnectionToken creation, capture, and authoritative reconciliation on the backend.
- Persist enough merchant and local identifiers to reconcile unknown and offline outcomes before retrying or creating replacement Intents.
- Treat reader type, firmware, country, currency, account enablement, and preview enrollment as runtime prerequisites separate from SDK symbols.
- Implement disconnect, auto-reconnect, required-update, cancellation, and background/foreground transitions as first-class checkout states.
- Use SetupIntents with explicit consent for reusable payment details.
- Test both split and combined flows only if the application supports both; do not mix their state transitions accidentally.
- Review the migration guide and support lifecycle before every major upgrade because end-of-life versions are eventually blocked.

## `StripeTerminal@5.8.1` Offline Maintenance Delta

Delta-ingested 2026-10-25 from `5.8.0`. GitHub publication is October 9 UTC; the release note labels October 8. Three retained files change and 232 remain unchanged. No exposed payment API change is present in the retained comparison; iOS 15 remains the package minimum.

Stripe reports that offline PaymentIntents previously dropped merchant-supplied creation parameters, causing Tap to Pay collection failures for destination charges using `onBehalfOf`. This is an upstream binary-fix statement, not independently inspected SDK implementation or a reproduced payment result. Existing consent, Connect configuration, reader/account prerequisites, offline reconciliation and capture responsibilities remain.

The public source changes only the cumulative changelog, `Package.swift` binary download/checksum and `SCPSDKVersion`. The example and other public headers are unchanged. All changed assigned content and affected prior code were read; unchanged files/history and inventories were mechanically verified under the approved focused-reading exception. No SDK binary, build, physical reader or payment test was executed. All older version knowledge remains preserved.

### Located Grounding

- `releases/stripeterminal/5.8.1/2026-10-25/release-notes.md:3`: "offline PaymentIntents dropped merchant-supplied creation parameters".
- `snapshots/2026-10-25-00cd46d/files/Package.swift:8`: `.iOS(.v15)`.
- `snapshots/2026-10-25-00cd46d/files/PublicHeaders/SCPTerminal.h:55`: `static NSString *const SCPSDKVersion = @"5.8.1";`.

Paths above are under `raw/github/stripe/stripe-terminal-ios/`. See [[changelog-github-stripe-terminal-ios]] for the complete package-qualified evidence boundary.

## `StripeTerminal@6.0.0` Additive Full Ingest

Full-ingested 2026-10-25 after completing the 5.8.1 delta. Release date 2026-10-07; exact SHA `79cfb3225553a7a5cceb8325f1c1f9087f792128`. This is a public-header/example integration baseline, not a read of the proprietary binary. All earlier wiki knowledge and immutable raw evidence remain available.

### Branch and Reading Boundary

The maintenance tip 5.8.1 and major tip 6.0.0 diverge from common baseline 5.8.0; 5.8.1 was published later. The immutable queued packet compares 5.8.1 -> 6.0.0 as endpoints. The additional 5.8.0 -> 6.0.0 comparison establishes v6 evolution from the common ancestor. Both were reviewed; their patches differ only in prior changelog/version/binary metadata. Neither comparison establishes whether the closed-source v6 binary contains or excludes the 5.8.1 offline fix.

The v6 snapshot contains ten added, 56 modified, two removed and 177 unchanged retained files relative to 5.8.1. Under the user's focused-reading exception, changed headers/examples, affected prior code, release notes, both branch comparisons and cumulative wiki history were read; unchanged raw, historical changelog sections and generated inventories were mechanically verified. The historical changelog suffix beginning at 5.8.0 is identical across all three snapshots. No SDK build, simulator, physical reader, payment or settlement verification was performed.

### Distribution and Compatibility

- iOS 16 is the deployment minimum. The binary is built using Xcode 27/Swift 6.4, but the notes require Xcode 16+/Swift 6+ for integrators; a module-interface compiler flag avoids requiring the newer module-selector syntax.
- The cumulative changelog announces SPM-only publication of new releases **including patches to earlier SDK versions**. Existing CocoaPods versions keep working but receive no further updates there. The README changes the SPM URL to `https://github.com/stripe/stripe-terminal-ios-spm`; manual binary installation remains documented.
- The example now opens `Example.xcodeproj`, removes its Podfile/lock, and shifts window setup from AppDelegate toward scene configuration. The bounded capsule does not retain the referenced SceneDelegate, so it does not establish a complete buildable example or its launch implementation.
- Retained `SUPPORT.md` is unchanged and still ends its dated table at v5. Preserve the v5 lifecycle evidence; do not invent a v6 hard-block date from an annual-release pattern.

### Capture and Checkout State

`PaymentIntentParametersBuilder` changes its default from `.manual` to `.automaticAsync`; `.automatic` and explicit `.manual` remain choices. This concerns SDK-side creation, not a retroactive change to every backend-created PaymentIntent. On-receipt tipping, incremental authorization and extended authorization require explicit manual capture. The example chooses manual for those options and only calls its capture backend when the returned Intent requires capture and capture was not skipped. Offline forwarding and unknown-outcome reconciliation still require backend state checks.

> [!warning] Contradiction
> `SCPPaymentIntentParameters.h:65` and the release notes specify automatic-async capture as the default, while `SCPTerminal.h:554-561` still says confirmation authorizes but does not capture and requires synchronous backend capture without qualifying the capture method. Apply that latter guidance to manual-capture flows, not universally to v6. Select the capture method explicitly and inspect the Intent state. The reciprocal warning is in [[stripe-terminal]].

### Required Consent and Public-Model Migration

| Area | v6 contract / migration |
| --- | --- |
| SetupIntent collection | Build `CollectSetupIntentConfigurationBuilder(allowRedisplay: ...)`; pass the required configuration as `setupConfig` to collect or `collectConfig` to process. Consent remains mandatory; the header documents `.always` or `.limited`. The demo's selectable `.unspecified` and default `.always` do not override that contract. |
| SetupIntent PaymentMethod | `paymentMethod` now returns the expanded object formerly named `paymentMethodExpanded`; `paymentMethodId` supplies the former ID-valued `paymentMethod`. |
| PaymentIntent Charge | Replace `charges` with nullable `latestCharge`/`latestChargeId`; the note describes compatibility with either `latest_charge` or a legacy charges list. The note directs invoice-relationship retrieval to the server API. |
| Instrument vs transaction | `PaymentMethod.cardPresent`/`interacPresent` return `PaymentMethodCardPresentDetails`, including available/preferred networks and nullable expiry. Transaction-only receipt, generated-card, authorization and capture fields remain under `PaymentMethodDetails.cardPresent`/`interacPresent`. `CardPresentDetails.networks` is removed; instrument `networks` replaces it. |
| Strings, not old enums | Brand, network, funding and read-method values become API strings where declared. Missing funding is nil; missing read method is `"unknown"`; new API values are preserved. Replace enum comparisons and removed `stringFromCardBrand`/`stringFromReadMethod` helpers. The umbrella drops the old enum imports even though historical header files remain in the retained tree. |
| Additional fields | Card-present details expose nullable `paymentAccountReference`, described as linking a physical card and wallet tokens to the same underlying payment account; absence must remain supported. PaymentIntent also exposes optional `application` and `review` IDs. |
| Removed aliases | Use `stripeDescription`, not deprecated parameter `description` aliases. Replace simulator `availableReaderUpdate`/old update enum with connection `testReaderUpdate`. |

These are SDK model/compile migrations, not evidence of general card-saving eligibility, customer attachment, account enablement or new legal consent.

### Reader Delegates, Cancellation and Updates

`MobileReaderDelegate` and `TapToPayReaderDelegate` inherit shared `ReaderInteractionDelegate`. Rename the five Tap to Pay update/input/display callbacks to `reader(...)` forms. Implement the concrete reader delegate, not the shared base directly. Mobile optional-update availability stays on `MobileReaderDelegate`; shared installation callbacks also cover mandatory Tap to Pay configuration during connection, not optional Tap to Pay update discovery.

Blocking payment selection and QR display move to separate `ReaderPaymentInteractionDelegate.reader(_:didRequestInteraction:)`. Set it on Bluetooth/USB/Tap to Pay connection configuration and retain it until disconnect; the connection references it weakly. Handle `PaymentMethodSelectionInteraction` or `QrCodeDisplayInteraction` and call its completion to continue payment. The example's persistent announcers forward these events to participating view controllers.

Reader/customer cancellation is `.canceledByReader` (2021), including Tap to Pay sheet dismissal/PIN back-out; SDK-requested cancellation remains `.canceled` (2020). Audit cancellation branches for both. The retained `PaymentViewController.handlePaymentError` still tests only `.canceled` before invoking its cancel-PaymentIntent branch; do not copy that as complete v6 cancellation handling. This is a static example observation, not a reproduced runtime SDK defect.

Internet connection `allowCustomerCancel` is removed; use per-collection `customerCancellation`, enabled by default on supported readers. Printer-low-battery error becomes general `.readerBatteryLow` (same numeric code 4007). The release reports a reconnect fix preserving a refined peer-removed-pairing reason. Simulator offline configuration loses its account-access error, but live-mode rejection remains; this does not promote real offline processing to GA.

### Refund Migration and Preview Features

- **In-person refund:** rename `RefundParameters`/Builder to `ProcessRefundParameters`/Builder. `processRefund` still collects and confirms where cardholder presence is required. Deprecated split collection and old parameterless confirmation overloads are removed.
- **Private-preview no-collection refund:** new `confirmRefund(parameters)` uses a connected reader for authentication without reader UI/card presentation. Supply PaymentIntent ID/client secret, optionally amount (omission refunds all remaining refundable amount), reason, metadata, Connect reversal/application-fee flags or instructions email. Wait for completion; if an error contains no Refund, reconcile with the backend **before creating another refund**. Do not confuse this with the removed split confirmation API or treat it as bypassing Interac presence requirements.
- **Refund response:** `stripeId` becomes nullable. Handle `canceled`, `requiresAction` and optional `nextAction` details (instruction-email metadata/expiry), not only a successful object return.
- **Mexico MSI installments preview:** enable installments under card-present PaymentIntent options. Read `availablePlans` after collection and cardholder-selected `plan` after confirmation. Symbols and example wiring do not prove country/card/account eligibility or preview access.
- **Swish preview:** adds the method type and location/reader details on PaymentMethod and transaction details. Presence is not general release or eligibility proof.
- **WisePad 3 surcharge:** notes add amount surcharge and confirm-time consent; collect-time `surchargeNotice` remains unsupported. Existing preview/account/firmware gates still apply.

### Located Grounding

Paths are under `raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/`:

- `CHANGELOG.md:6`: "including patches to earlier SDK versions" (within the SPM-only publication announcement).
- `PublicHeaders/SCPPaymentIntentParameters.h:65`: "Defaults to `SCPCaptureMethodAutomaticAsync`."
- `PublicHeaders/SCPCollectSetupIntentConfiguration.h:44`: "`allowRedisplay` must be set to `always` or `limited`."
- `PublicHeaders/SCPReaderPaymentInteractionDelegate.h:22`: "The provided delegate must be retained by your application until the reader disconnects."
- `PublicHeaders/SCPTerminal.h:774-775`: "The connected reader is used to authenticate the request, but this method does" / "not display reader UI or ask the cardholder to present a payment method."

## Related

- Company: [[stripe]]
- Concept: [[stripe-terminal]]
- Affected concepts: [[stripe-terminal-save-payment-details]], [[stripe-terminal-refunds]], [[stripe-terminal-tipping]], [[stripe-terminal-incremental-authorizations]], [[stripe-terminal-extended-authorizations]]
- General iOS payments SDK: [[source-github-stripe-ios]]
- History: [[changelog-github-stripe-terminal-ios]]

## Raw Sources

- [6.0.0 snapshot](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/manifest.json), [release](raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/6.0.0/2026-10-25/manifest.json), [notes](raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/6.0.0/2026-10-25/release-notes.md), [common-baseline comparison](tracking/github/repos/stripe/stripe-terminal-ios/comparisons/stripeterminal/5.8.0--6.0.0/comparison.json), and [cross-branch endpoint comparison](tracking/github/repos/stripe/stripe-terminal-ios/comparisons/stripeterminal/5.8.1--6.0.0/comparison.json).
- [v6 cumulative changelog](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/CHANGELOG.md), [README](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/README.md), [package](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/Package.swift), and [support policy](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/SUPPORT.md).
- [v6 capture creation contract](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPPaymentIntentParameters.h), [Terminal APIs and capture comment](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPTerminal.h), [SetupIntent consent](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPCollectSetupIntentConfiguration.h), [SetupIntent model](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPSetupIntent.h), and [PaymentIntent model](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPPaymentIntent.h).
- [v6 instrument details](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPPaymentMethodCardPresentDetails.h), [transaction details](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPCardPresentDetails.h), [payment interaction delegate](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPReaderPaymentInteractionDelegate.h), and [interaction types](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPPaymentInteraction.h).
- [v6 payment example](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/Example/Example/PaymentViewController.swift), [creation/options example](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/Example/Example/StartPaymentViewController.swift), and [SetupIntent example](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/Example/Example/StartSetupIntentViewController.swift).
- [v6 refund parameters](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPConfirmRefundParameters.h), [in-person parameters](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPProcessRefundParameters.h), [installments](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPInstallmentsParameters.h), and [Swish](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/PublicHeaders/SCPSwishDetails.h).
- [5.8.1 snapshot](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-00cd46d/manifest.json), [release](raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/5.8.1/2026-10-25/manifest.json), [notes](raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/5.8.1/2026-10-25/release-notes.md), and [5.8.0 to 5.8.1 comparison](tracking/github/repos/stripe/stripe-terminal-ios/comparisons/stripeterminal/5.8.0--5.8.1/comparison.json).
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/manifest.json` - exact-SHA bounded source capsule
- `raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/5.8.0/2026-08-31/manifest.json` - package-qualified release record
- `raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/5.8.0/2026-08-31/release-notes.md` - exact `5.8.0` release notes
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/README.md` - repository purpose, requirements, installation, and closed-source boundary
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/SUPPORT.md` - support lifecycle and hard-block schedule
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/CHANGELOG.md` - cumulative version history
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/PublicHeaders/SCPTerminal.h` - initialization, connection, payment, SetupIntent, refund, offline, and reader APIs
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/PublicHeaders/StripeTerminal.h` - exported public surface
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/Example/Example/APIClient.swift` - example backend boundary
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/Example/Example/PaymentViewController.swift` - payment and capture orchestration
- `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/Example/Example/OfflineUIHandler.swift` - offline status and forwarding UI


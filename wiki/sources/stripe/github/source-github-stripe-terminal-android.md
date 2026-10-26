---
title: "GitHub: stripe/stripe-terminal-android"
type: source
date_ingested: 2026-08-31
date_updated: 2026-10-26
original_format: github-repo
raw_files:
  - "github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/manifest.json"
  - "github/stripe/stripe-terminal-android/snapshots/2026-10-26-abb16f5/manifest.json"
  - "github/stripe/stripe-terminal-android/snapshots/2026-10-26-846d401/manifest.json"
  - "github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/manifest.json"
tags: [stripe, terminal, android, kotlin, java, mobile, sdk, card-present, tap-to-pay, offline-payments, github-repository]
---

## Overview

`stripe/stripe-terminal-android` distributes Stripe's proprietary Android SDK for custom in-person checkout. This cumulative page establishes the approved `stripeterminal@5.8.0` baseline at exact commit `b3de15b57201df0aa0e0235ccbe8e81bf9abaa8f` from generated public API documentation, the open-source Kotlin and Java examples, support policy, and release history.

Additive ingests on 2026-10-26 preserve the 5.8.1/5.8.2 maintenance deltas and the full 6.0.0 major boundary. General sections retain the historical v5 baseline; the explicit v6 section below qualifies incompatible APIs and defaults without replacing older knowledge.

Repository: <https://github.com/stripe/stripe-terminal-android>

## Evidence Boundary

- Stripe states that the SDK implementation is proprietary and closed source. The retained generated API documentation defines the public contract, while the example applications show integration patterns rather than internal runtime behavior.
- The initial v5 capsule retains 447 files and assigned 88 evidence paths. The v6 capsule retains 450 files; its approved full assignment expands to 94 paths. Tests and proprietary implementation source are not evidence here. The focused-reading exception is documented per release below.
- API presence does not prove merchant eligibility, country or currency availability, preview access, device certification, reader firmware compatibility, or account configuration.
- SDK callbacks do not independently prove capture, settlement, or fulfillment. Manual-capture integrations must notify their backend to capture and reconcile authoritative server-side state.

## Package Status

| Package | Latest ingested release | Exact SHA | Evidence status |
| --- | --- | --- | --- |
| `com.stripe:stripeterminal` v6 | `6.0.0` | `0829be9e77842bc12a6ba56d64fd152b53506025` | Approved additive full; all v5 history preserved |
| `com.stripe:stripeterminal` v5 | `5.8.2` | `abb16f502cbe0fcc82f673c246c86c883a5c2fdc` | Approved delta; 5.8.0/5.8.1 preserved |

This table reports wiki ingest progress, not the latest release published upstream.

## Platform and Installation (v5 Baseline)

- The SDK supports Android API level 26 and later, Kotlin, and Java 8. Decreasing `minSdkVersion` does not bypass Stripe's runtime API-level validation.
- Standard reader integrations use `implementation("com.stripe:stripeterminal:5.8.0")`.
- Tap to Pay replaces that dependency with matching versions of `com.stripe:stripeterminal-taptopay:5.8.0` and `com.stripe:stripeterminal-core:5.8.0`. Mixed Terminal artifact versions are unsupported.
- The Kotlin example also uses the optional `stripeterminal-ktx` module, introduced in version 5 for suspend wrappers around asynchronous Terminal APIs.

## Android Permissions and Lifecycle

Location access must remain enabled for reader use and payments. At `5.8.0`, `ACCESS_COARSE_LOCATION` is sufficient for SDK location reporting. The SDK declares its reader-discovery Bluetooth permissions; applications that derive physical location from Bluetooth scans or otherwise need precise location must explicitly declare and request their own fine-location permissions.

The SDK is application-lifecycle aware. A custom `Application` subclass must call `TerminalApplicationDelegate.onCreate(this)` from `Application.onCreate`, and the manifest must name that subclass. The Java and Kotlin examples request location and relevant Bluetooth permissions before initializing Terminal.

## Initialization and Backend Boundary

Initialize the singleton with `Terminal.init(...)` using the application context, a log level, a `TokenProvider`, a `TerminalListener`, an optional `OfflineListener`, and a `LocaleConfig`. The overload without `LocaleConfig` is deprecated. `Terminal.getInstance()` is valid only after initialization.

The example backend supplies `/connection_token`, `/create_location`, `/capture_payment_intent`, and `/cancel_payment_intent`. Secret-key operations and authoritative reconciliation remain server responsibilities. Switching account context requires disconnecting the reader, clearing cached credentials while disconnected, changing backend identity, and acquiring a token for the new account.

## Reader Discovery and Connection

The retained examples route among Bluetooth, internet, Tap to Pay, and USB discovery. Mobile and Tap to Pay readers require a Stripe Terminal Location. `discoverReaders` returns a cancelable operation; `easyConnect` combines discovery and connection for supported flows.

Applications must model discovery, connection, reconnecting, disconnection, and reader-software update states explicitly. One Terminal instance connects to one reader and performs one operation at a time. Reader discovery and successful connection do not by themselves prove the merchant or device is eligible for every exposed reader type.

## Payment Lifecycle

Two payment patterns coexist:

1. Split flow: create or retrieve a PaymentIntent, call `collectPaymentMethod`, then call `confirmPaymentIntent`.
2. Combined flow: call `processPaymentIntent`, introduced in version 5 to combine collection and confirmation.

The examples create or retrieve the Intent through the SDK, collect and confirm it, and then call the merchant backend to capture when the confirmed Intent is in a manual-capture state. Unknown callback outcomes require server-side retrieval before retrying or creating a replacement payment.

Collection configuration controls customer cancellation, offline behavior, tipping, and whether the PaymentIntent is updated with collected details. Reader cart-display data is presentational and does not determine the amount charged.

## Saving Payment Details

SetupIntents support split `collectSetupIntentPaymentMethod` plus `confirmSetupIntent` and combined `processSetupIntent` flows. The integration must obtain cardholder consent and provide `AllowRedisplay`; collection alone is not evidence that a reusable PaymentMethod was stored or attached to the intended Customer.

The SDK can create or retrieve SetupIntents, cancel an in-progress SetupIntent, and forward offline SetupIntents when supported. Customer ownership and later off-session charging remain backend concerns.

## Refunds (v5 Baseline)

`processRefund` is the maintained combined path for in-person refund flows. The older `collectRefundPaymentMethod` and `confirmRefund` split methods remain in the API but are deprecated. Ordinary refunds that do not require cardholder presence remain server-side or Dashboard operations.

Refund failures and timeouts require reconciliation rather than blind retries. API availability does not remove payment-method-specific requirements such as in-person Interac refund handling.

## Offline Payments

The SDK exposes offline status, an `OfflineListener`, per-collection offline behavior, simulated offline configuration, and forwarding callbacks. The Java and Kotlin examples record forwarded offline PaymentIntents, then call their backend to capture when the forwarded Intent requires capture and no further upload is pending.

Offline Intents may begin without a Stripe ID, so applications need durable local and merchant identifiers for reconciliation. Clearing app data can remove unresolved local evidence. Version `5.7.0` fixed a data-loss bug introduced in `5.6.0` that could permanently delete stored offline payments when upgrading from `4.1.0` or earlier; affected integrations should upgrade directly to a fixed version rather than deploying `5.6.0` as an intermediate step.

## Tap to Pay on Android

Tap to Pay has its own matched Maven artifacts and discovery/connection path. The API also exposes Tap to Pay UX configuration. Device certification, Android version, NFC, Google Mobile Services, hardware security, security-patch age, merchant country, and account enablement remain external prerequisites that this repository capsule does not prove.

Version `5.8.0` fixes PIN collection failures on certain device models. That fix is patch-specific and does not establish universal PIN or Tap to Pay availability.

## Reader Operations and Updates

The public surface supports available-update installation, reader update callbacks, reader settings, printing, reboot, barcode scanning, display updates, structured input collection, and preview data collection. Integrations must keep update progress and completion visible and must not assume every reader supports every operation.

At `5.8.0`, supported readers expose current and maximum buzzer volume and accept low, high, or exact values. Printing can fail with `PRINTER_LOW_BATTERY`. These symbols do not prove support on a particular deployed reader or firmware version.

## Version History

### `stripeterminal@5.8.0`

Adds low-battery printing failure, buzzer-volume settings, coarse-location sufficiency, and revised Bluetooth manifest declarations. It fixes initialization crashes on unsupported Android Keystore implementations, slow-network reader-update timeouts, and Tap to Pay PIN failures on some devices.

### Version 5 Major Boundary

Version `5.0.0` introduced combined payment, SetupIntent, and refund process APIs; Kotlin coroutine wrappers; `easyConnect`; and an explicit `RECONNECTING` state. It also changed initialization, credential clearing, connected-reader timing, customer-cancellation defaults, cancellation completion, and several configuration names. Upgrading from 4.x requires a migration review rather than a package-number substitution.

### Accumulated `5.1.0--5.7.0` Context

The retained history adds mobile-reader QR payments, locale-configured API errors, overcapture status, Tap to Pay surcharging preview, and numerous reader, cancellation, offline-forwarding, generated-card, and Keystore fixes. These are cumulative-history findings from the `5.8.0` snapshot, not exact repository comparisons for every intermediate release.

## Support Lifecycle

Major versions receive roughly one year each of active development, maintenance, and deprecation before hard blocking. The retained schedule places 5.x in active development with patch support through October 2027 and a hard block in October 2028. Version 4.x is in maintenance and is scheduled for hard block in October 2027; versions 1.x through 3.x are scheduled for hard block in January 2027.

After a hard block, affected versions cannot discover or connect readers or process payments. Tap to Pay can require upgrades sooner than the general schedule.

## Integration Guidance

- Keep ConnectionToken creation, capture, cancellation, and authoritative reconciliation on the backend.
- Request Android permissions before Terminal initialization and keep the application delegate wired for the whole process lifecycle.
- Persist identifiers needed to reconcile unknown and offline outcomes before retrying.
- Treat reader type, firmware, device certification, country, account enablement, and preview enrollment as runtime prerequisites separate from API symbols.
- Review migration notes before every major upgrade and avoid Android `5.6.0` as an intermediate upgrade for installations with offline records from `4.1.0` or earlier.
- Test Java or Kotlin callbacks, cancellation, background transitions, disconnect/reconnect, required updates, offline forwarding, capture, and physical-reader behavior independently.

## `stripeterminal@5.8.1` Tap to Pay Delta

Delta-ingested 2026-10-26 from 5.8.0 at SHA `846d401d1f7bc686a2c12d6def4342471c25a625`, release date 2026-09-14. The exact-SHA changelog announces China UnionPay payment-method support in Hong Kong for Tap to Pay on Android. This does not establish broader geographic availability, card/device/account eligibility, or inspected proprietary implementation.

There are 341 modified and 106 unchanged retained files. All 337 modified generated API pages are byte-identical to the prior version after replacing only the release version string. Other changes are the changelog, README dependency examples and the Java/Kotlin Gradle dependency versions; retained application implementation is unchanged. Keep Tap to Pay/core artifacts matched, now at 5.8.1, and preserve the Android API 26 minimum and existing permission/lifecycle obligations.

User-approved focused reading fully covered changed authored files, new changelog text, affected prior code and cumulative wiki history; version-only docs, unchanged history and inventories were checked mechanically. Both 447-file snapshots match their hashes/sizes; prior raw changelog history from 5.8.0 is identical. No SDK build, emulator/device, reader or payment execution. All prior wiki knowledge remains.

### Located Grounding

Under `raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-846d401/files/`:

- `CHANGELOG.md:12`: "Added China Union Pay payment method support in Hong Kong for Tap to Pay on Android."
- `README.md:9`: "The Stripe Terminal Android SDK is compatible with apps supporting Android API level 26* and above."
- `Example/javaapp/build.gradle.kts:46`: `val stripeTerminalVersion = "5.8.1"`.

## `stripeterminal@5.8.2` UnionPay Maintenance Delta

Delta-ingested 2026-10-26 after 5.8.1 completed, SHA `abb16f502cbe0fcc82f673c246c86c883a5c2fdc`, released 2026-10-02. The exact-SHA changelog reports a fix for payment failures with China UnionPay cards in Tap to Pay. It does not announce new countries or a public API migration. This is a proprietary SDK fix statement, not a locally reproduced transaction result.

As in 5.8.1, 341 retained files are modified and 106 unchanged; all 337 changed API pages differ only by release version strings, and other changes are README, two example Gradle files and changelog. Matched artifacts advance to 5.8.2. The changelog also edits the old 5.8.1 wording from "Union Pay" to "UnionPay"; this spelling correction is not a newly introduced capability. The original quote and historical attribution above remain intact.

Focused reading covered all changed authored content, affected prior code, comparison and cumulative wiki history. Raw hashes, version-only docs and generated inventories were mechanically verified. Historical raw changelog differs only by that spelling correction plus the new entry. No SDK/device/payment execution; all prior knowledge preserved.

### Located Grounding

Under `raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-abb16f5/files/`:

- `CHANGELOG.md:11`: "Fixed an issue that caused payment failures for China UnionPay cards."
- `README.md:29`: `implementation("com.stripe:stripeterminal:5.8.2")`.
- `Example/javaapp/build.gradle.kts:46`: `val stripeTerminalVersion = "5.8.2"`.

## `stripeterminal@6.0.0` Additive Full Ingest

Full-ingested 2026-10-26 after completing both patch ingests, exact SHA `0829be9e77842bc12a6ba56d64fd152b53506025`, released 2026-10-07. This is additive public API/example knowledge; it is not proprietary runtime inspection or a successful SDK/device/payment test. All older source sections, quotes and release identities remain available.

### Reading and Evidence Boundary

Relative to 5.8.2: 341 modified, eight added, five removed and 101 unchanged retained files. Effective full assignment: 94 paths / 6,520,286 bytes, including a 5,166,982-byte generated comparison. The user approved focused reading for all three releases: fully read changed authored files, semantic API changes, affected prior code, new changelog material and cumulative wiki history; mechanically verify unchanged/version-only evidence, history and generated inventories/diffs. The review covered all changed authored files, including event/model files outside the normal reading selectors, all 105 current API pages with changed main-content text and the five removed prior pages. HTML was parsed structurally for content reads; exact raw HTML and the original diff remain immutable.

All 1,791 retained files across baseline and three updates match size, SHA-256 and Git blob IDs. New release bodies only contain dependency instructions and links to mutable master; version claims below instead use the exact-SHA raw changelog, API pages and example evidence.

Some announced model/configuration types are outside this bounded capsule. Their migration summaries are attributed to the exact release changelog, not a claim to have inspected every property or proprietary implementation. Deep implementation questions may require a separately approved exact-SHA supplement. No new collection or registry policy was introduced during ingest.

### Android Build, Permissions and Lifecycle

The release requires compile SDK 35+ and says SDK dependencies move to Kotlin 2.3.21. This is not a requirement for every device to run Android 15: retained README and example build settings still specify minimum API 26. Standard Terminal and Tap to Pay/core artifacts must stay version-matched, now at 6.0.0. The example still targets Java 8 bytecode.

`Terminal.init` now requires `LocaleConfig`; the old overload without it is removed. The Java example explicitly supplies `LocaleConfig.HardcodedLocale.Builder("en-US").build()`. Location permission and `TerminalApplicationDelegate` lifecycle wiring remain necessary. Tap to Pay's deprecated location-ID connection constructor is removed; use `TapUseCase.Pay(locationId)` for that use case.

Tap to Pay adds a `MODIFY_AUDIO_SETTINGS` permission requirement so payment audio is not muted. The retained app manifests do not explicitly declare it; no merged SDK manifest or runtime permission proof was produced, so absence there alone does not prove that the final app lacks it. Review the merged manifest in a real integration. Consumer Proguard changes are upstream release statements, not locally validated shrinker results.

### Capture Default and Example Caution

SDK-side `PaymentIntentParameters.Builder` changes its default to `CaptureMethod.AutomaticAsync`, replacing `Manual`. Explicit Manual is required for receipt tipping and incremental/extended authorization. The Java and Kotlin event fragments now explicitly select Manual when extended/incremental authorization is requested. This builder change does not retroactively redefine every backend-created PaymentIntent.

> [!warning] Contradiction
> The v6 changelog specifies automatic-async capture, but retained `confirm-payment-intent.html` still unconditionally says confirmation only authorizes and requires synchronous backend capture; `PaymentIntent.captureMethod` documentation lists only automatic/default and manual. Those old descriptions are incomplete for the new builder default. Apply manual-flow guidance only where appropriate, choose capture explicitly and inspect authoritative state. [[stripe-terminal]] records the reciprocal conflict.

The Java event example's successful process callback calls `ApiClient.capturePaymentIntent` whenever an Intent ID exists, without checking `REQUIRES_CAPTURE`. That code is unchanged around the new default, so it must not be copied as universally correct for automatic-async payments. This is a static integration risk, not a reproduced SDK defect or proof of a duplicate charge. The changed Kotlin event flow stores the processed Intent rather than capturing inline; it is not evidence that every manual payment has been captured. Backend reconciliation and fulfillment checks remain mandatory.

`TerminalRepository` in the retained Kotlin example is an in-memory Intent/refund ledger with merchant metadata, not durable backend storage. Its transaction IDs aid local lookup but do not alone establish restart-safe reconciliation of offline/unknown payments.

### Consent and Data-Model Migration

| Area | v6 migration |
| --- | --- |
| SetupIntent consent | `allowRedisplay` moves into required `CollectSetupIntentConfiguration`; pass `config` to collect or `collectConfig` to process. The demos construct `Builder(AllowRedisplay.ALWAYS)`; real consent must determine the value. The separate method argument/default empty configuration is removed. |
| Charges/invoice | Replace `getCharges()` with nullable `latestCharge`/`latestChargeId`; invoice relationship must be retrieved through the server API. The ledger-card example uses `latestCharge` for card brand/last4. |
| Card-present parent models | Release notes split the top-level type into reusable `PaymentMethod.CardPresent` and transaction-specific `Charge.CardPresent`. Instrument details keep networks, add brandProduct and nullable expiry; transaction details retain receipt and authorization-lifecycle information, not instrument networks. |
| SetupAttempt details | `SetupIntentPaymentMethodDetails` and `SetupIntentCardPresentDetails` become `SetupAttemptPaymentMethodDetails` and `SetupAttemptCardPresentDetails`; the detail type property becomes public per note. |
| Refund models | `RefundParameters` becomes `ProcessRefundParameters`, including `ByChargeId`/`ByPaymentIntentId`; `Refund.id` is nullable. |
| Reader support/errors | `ReaderSupportResult.NotSupported` exceptions are restricted to TerminalException per note. General `READER_BATTERY_LOW` replaces printer-specific low battery. |

Many regenerated model pages stop displaying property initializers such as `= null` or `= 0` while keeping types and descriptions. That presentation change alone does not prove a runtime default/nullability change. Constructor defaults remain visible where specified. Android migrations are not interchangeable with iOS class/property names or its enum-to-string changes.

### Payment UI, Cancellation and Tap to Pay

For mobile readers, move `onQrCodeDisplayRequired` and `onPaymentMethodSelectionRequired` out of `MobileReaderListener`. Implement separate `ReaderPaymentInteractionListener.onInteractionRequired`, inspect the concrete PaymentInteraction, display the required UI and invoke its callback. Bluetooth, USB and external-USB connection configurations gain an optional listener alongside the status listener. Its default is null, but a transaction fails if it needs an interaction and no listener was supplied. This is not an innocuous optional callback for QR/selection flows. The listener API and connection contract, rather than unchanged examples, define this migration; do not transplant iOS connection wiring into Android Tap to Pay.

Reader-originated cancellation now reports `CANCELED_BY_READER`; programmatic SDK cancellation remains `CANCELED`. Audit both cases without treating operation cancellation as proof that a PaymentIntent was canceled. Tap to Pay expired-session attestation now uses `SESSION_EXPIRED` instead of generic connection error.

`TapToPayReaderListener.onUpdateRequirementsAvailable` reports upcoming requirements during or after connection. Requirements identify the minimum update version and enforcement timestamp per note. The retained method docs explicitly make the callback advisory: surface a non-blocking scheduling warning; it does not install an update, change connection state or itself block payment acceptance. Future enforcement and this notification are distinct.

Tap to Pay UX models are no longer Parcelable. Migrate DarkMode to Theme and colors/darkMode accessors/builders to colorScheme/theme; the theme default changes from LIGHT to SYSTEM. These are compile/serialization and presentation changes, not evidence of broader payment eligibility. MOTO authorization-code support on smart readers requires firmware 2.45+ per note. Deprecated simulator update fields/enums are replaced with connection `testReaderUpdate` on Bluetooth/USB; live-mode update simulation remains invalid.

### Refund Preview, History and Limits

The old split refund collection/confirmation methods are removed. In-person refunds continue through `processRefund(ProcessRefundParameters, ...)`; Interac cardholder-presence requirements are unchanged. The new **private-preview** `confirmRefund(ConfirmRefundParameters, RefundCallback)` is a different, non-collecting API, with a Unit/void return rather than the removed cancelable overload. A successful callback can still return `requires_action`; display `Refund.nextAction` instructions. If a failure has no attached Refund, reconcile with the backend before creating another one. The release announces mobile/Tap to Pay/internet-reader availability within preview, not universal merchant access. The bounded evidence does not establish every parameter or justify copying iOS's reader-authentication assumptions.

The v6 cumulative changelog retrospectively adds known-issue notes for missing `generated_card` in 5.4.0–5.6.0 and clarifies that 5.7.0 fixed it. These are historical clarifications, not newly fixed v6 behavior. Existing offline database-loss history is preserved separately. All other prior raw history changes were mechanically checked; the old wiki attribution is retained.

Retained SUPPORT.md is unchanged and still ends its dated schedule at v5. Do not invent a v6 hard-block date. No Android MSI/Swish feature or SPM/CocoaPods distribution policy is inferred from the iOS release. Preview access, supported reader/firmware, device certification, network and merchant/account prerequisites remain independent.

### Located Grounding

Under `raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/`:

- `CHANGELOG.md:49-50`: "now defaults `captureMethod` to `CaptureMethod.AutomaticAsync` instead of" / "`CaptureMethod.Manual`."
- `CHANGELOG.md:59`: "a `compileSdkVersion` set to 35 (Android 15) or above."
- `docs/external/com.stripe.stripeterminal.external.models/-connection-configuration/-bluetooth-connection-configuration/reader-payment-interaction-listener.html:76`: "A transaction fails if it requires an interaction and no listener is provided."
- `docs/external/com.stripe.stripeterminal.external.callable/-tap-to-pay-reader-listener/on-update-requirements-available.html:76`: "It does not install an update, change the reader connection state, or block payment acceptance."
- `Example/javaapp/src/main/java/com/stripe/example/javaapp/fragment/event/EventFragment.java:142`: `ApiClient.capturePaymentIntent(paymentIntentId);` (inside successful callback, without a capture-state guard).

## Related

- Company: [[stripe]]
- Concept: [[stripe-terminal]]
- Affected concepts: [[stripe-terminal-save-payment-details]], [[stripe-terminal-refunds]], [[stripe-terminal-tipping]], [[stripe-terminal-incremental-authorizations]], [[stripe-terminal-extended-authorizations]]
- iOS counterpart: [[source-github-stripe-terminal-ios]]
- History: [[changelog-github-stripe-terminal-android]]

## Raw Sources

- [6.0.0 snapshot](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/manifest.json), [release](raw/github/stripe/stripe-terminal-android/releases/stripeterminal/6.0.0/2026-10-26/manifest.json), [release body](raw/github/stripe/stripe-terminal-android/releases/stripeterminal/6.0.0/2026-10-26/release-notes.md), [exact changelog](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/CHANGELOG.md), and [5.8.2 to 6.0.0 comparison](tracking/github/repos/stripe/stripe-terminal-android/comparisons/stripeterminal/5.8.2--6.0.0/comparison.json).
- [v6 README](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/README.md), [build requirements](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/Example/build.gradle.kts), [Java event example](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/Example/javaapp/src/main/java/com/stripe/example/javaapp/fragment/event/EventFragment.java), [Kotlin event example](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/Example/kotlinapp/src/main/java/com/stripe/example/fragment/event/EventFragment.kt), [Kotlin processing](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/Example/kotlinapp/src/main/java/com/stripe/example/viewmodel/EventViewModel.kt), and [Kotlin in-memory ledger](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/Example/kotlinapp/src/main/java/com/stripe/example/TerminalRepository.kt).
- [v6 collect SetupIntent](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/docs/core/com.stripe.stripeterminal/-terminal/collect-setup-intent-payment-method.html), [process SetupIntent](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/docs/core/com.stripe.stripeterminal/-terminal/process-setup-intent.html), [capture-comment evidence](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/docs/core/com.stripe.stripeterminal/-terminal/confirm-payment-intent.html), [capture-property text](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/docs/external/com.stripe.stripeterminal.external.models/-payment-intent/capture-method.html), and [preview refund](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/docs/core/com.stripe.stripeterminal/-terminal/confirm-refund.html).
- [v6 interaction listener](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/docs/external/com.stripe.stripeterminal.external.callable/-reader-payment-interaction-listener/on-interaction-required.html), [connection obligation](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/docs/external/com.stripe.stripeterminal.external.models/-connection-configuration/-bluetooth-connection-configuration/reader-payment-interaction-listener.html), [Tap to Pay update notification](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/docs/external/com.stripe.stripeterminal.external.callable/-tap-to-pay-reader-listener/on-update-requirements-available.html), and [support schedule](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/SUPPORT.md).
- [5.8.2 snapshot](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-abb16f5/manifest.json), [release](raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.2/2026-10-26/manifest.json), [release body](raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.2/2026-10-26/release-notes.md), [exact changelog](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-abb16f5/files/CHANGELOG.md), and [comparison](tracking/github/repos/stripe/stripe-terminal-android/comparisons/stripeterminal/5.8.1--5.8.2/comparison.json).
- [5.8.1 snapshot](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-846d401/manifest.json), [release](raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.1/2026-10-26/manifest.json), [release body](raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.1/2026-10-26/release-notes.md), [exact changelog](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-846d401/files/CHANGELOG.md), [README](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-846d401/files/README.md), and [comparison](tracking/github/repos/stripe/stripe-terminal-android/comparisons/stripeterminal/5.8.0--5.8.1/comparison.json).
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/manifest.json` - exact-SHA bounded source capsule
- `raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.0/2026-08-31/manifest.json` - package-qualified release record
- `raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.0/2026-08-31/release-notes.md` - exact `5.8.0` release note
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/README.md` - requirements, installation, lifecycle, Tap to Pay dependencies, and closed-source boundary
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/SUPPORT.md` - support lifecycle and hard-block schedule
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/CHANGELOG.md` - cumulative package history
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/docs/core/com.stripe.stripeterminal/-terminal/index.html` - public Terminal API surface
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/Example/kotlinapp/src/main/java/com/stripe/example/StripeTerminalApplication.kt` - Kotlin initialization and lifecycle integration
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/Example/kotlinapp/src/main/java/com/stripe/example/TerminalRepository.kt` - Kotlin in-memory Intent/refund ledger and merchant metadata
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/Example/javaapp/src/main/java/com/stripe/example/javaapp/fragment/PaymentFragment.java` - Java payment and backend capture flow
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/Example/javaapp/src/main/java/com/stripe/example/javaapp/OfflineModeHandler.java` - Java offline forwarding and capture handling

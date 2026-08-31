---
title: "GitHub: stripe/stripe-terminal-android"
type: source
date_ingested: 2026-08-31
date_updated: 2026-08-31
original_format: github-repo
raw_files:
  - "github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/manifest.json"
tags: [stripe, terminal, android, kotlin, java, mobile, sdk, card-present, tap-to-pay, offline-payments, github-repository]
---

## Overview

`stripe/stripe-terminal-android` distributes Stripe's proprietary Android SDK for custom in-person checkout. This cumulative page establishes the approved `stripeterminal@5.8.0` baseline at exact commit `b3de15b57201df0aa0e0235ccbe8e81bf9abaa8f` from generated public API documentation, the open-source Kotlin and Java examples, support policy, and release history.

Repository: <https://github.com/stripe/stripe-terminal-android>

## Evidence Boundary

- Stripe states that the SDK implementation is proprietary and closed source. The retained generated API documentation defines the public contract, while the example applications show integration patterns rather than internal runtime behavior.
- The capsule retains 447 files. The approved ingest assigned 88 evidence paths covering public Terminal API pages, examples, package setup, support policy, and release history; tests and proprietary implementation source are not evidence here.
- API presence does not prove merchant eligibility, country or currency availability, preview access, device certification, reader firmware compatibility, or account configuration.
- SDK callbacks do not independently prove capture, settlement, or fulfillment. Manual-capture integrations must notify their backend to capture and reconcile authoritative server-side state.

## Package Status

| Package | Latest ingested release | Exact SHA | Evidence status |
| --- | --- | --- | --- |
| `com.stripe:stripeterminal` | `5.8.0` | `b3de15b57201df0aa0e0235ccbe8e81bf9abaa8f` | Approved full baseline |

This table reports wiki ingest progress, not the latest release published upstream.

## Platform and Installation

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

## Refunds

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

## Related

- Company: [[stripe]]
- Concept: [[stripe-terminal]]
- iOS counterpart: [[source-github-stripe-terminal-ios]]
- History: [[changelog-github-stripe-terminal-android]]

## Raw Sources

- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/manifest.json` - exact-SHA bounded source capsule
- `raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.0/2026-08-31/manifest.json` - package-qualified release record
- `raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.0/2026-08-31/release-notes.md` - exact `5.8.0` release note
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/README.md` - requirements, installation, lifecycle, Tap to Pay dependencies, and closed-source boundary
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/SUPPORT.md` - support lifecycle and hard-block schedule
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/CHANGELOG.md` - cumulative package history
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/docs/core/com.stripe.stripeterminal/-terminal/index.html` - public Terminal API surface
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/Example/kotlinapp/src/main/java/com/stripe/example/StripeTerminalApplication.kt` - Kotlin initialization and lifecycle integration
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/Example/kotlinapp/src/main/java/com/stripe/example/TerminalRepository.kt` - Kotlin reader and Intent orchestration
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/Example/javaapp/src/main/java/com/stripe/example/javaapp/fragment/PaymentFragment.java` - Java payment and backend capture flow
- `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/Example/javaapp/src/main/java/com/stripe/example/javaapp/OfflineModeHandler.java` - Java offline forwarding and capture handling

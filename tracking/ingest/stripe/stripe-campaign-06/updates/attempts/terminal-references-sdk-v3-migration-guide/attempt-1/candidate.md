---
title: "Stripe Terminal: SDK Migration Guide (v3.0.0)"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/references/sdk-v3-migration-guide"
raw_files:
  - "stripe-terminal-sdk-v3-migration-guide-2025.md"
tags: [stripe, stripe-terminal, sdk, ios, android, migration, v3]
---

## Summary

The 2026-05-01 [[stripe]] [[stripe-terminal|Terminal]] guide documents migrating existing iOS and Android integrations from pre-v3 SDKs to 3.0.0. The 2026-11-07 capture gives the v3.0.0 migration purpose and links the iOS and Android variants. The migration details below come from the May guide.

## Breaking Changes Summary

- Both SDKs rename `processPayment` to `confirmPaymentIntent` and `processRefund` to `confirmRefund`. The iOS guide says the parameters stay the same and names the renamed errors `SCPConfirmPaymentIntentError` and `SCPConfirmRefundError`. The Android guide says the method behavior stays the same.
- Both remove `readReusableCard`. The guide recommends creating, collecting, and confirming a SetupIntent in the SDK to save a payment method without a charge.
- Discovery configuration became a protocol on iOS and an interface on Android, with implementations for specific reader discovery methods.

**Historical offline private preview**. In the May guide's v3 migration, Stripe first enables offline payments for the account in its backend. The integrator must then disconnect and reconnect to the reader with the SDK for the configuration to take effect. A PaymentIntent created offline can have a null `stripeId` on iOS or `id` on Android. See the separate [[source-stripe-terminal-offline-collect-card-payments|offline collection guide]] for later integration evidence.

## iOS-Specific Changes

- The minimum moves from iOS 11 for the v2.x branch to iOS 13 for v3.
- `discoverReaders` completes when `connectReader` is called. A failed connection requires a new `discoverReaders` call to resume discovery. An integration can also connect to a previously discovered reader or retry connecting without active discovery. Canceling discovery completes with `SCPErrorCanceled`.
- `SCPErrorBusy` is removed. The SDK queues new commands while another is running and executes them after preceding commands complete. Integrations that used the busy error as a signal need to account for potential queue buildup.
- Parameter and configuration classes such as `SCPCollectConfiguration` and `SCPPaymentIntentParameters` become immutable and use builders. `build()` throws in Swift and takes an `NSError **` out-parameter in Objective-C.
- `SCPReconnectionDelegate` now receives the reader instance. The method names replace `terminal` with `reader`.

## Android-Specific Changes

- The minimum moves from Android 5.0 (API 21) for the v2.x branch to Android 8.0 (API 26) for v3. Lowering `minSdkVersion` cannot bypass the SDK's runtime check.
- Location permission is required for every discovery configuration and checked at reader discovery. Only `BluetoothDiscoveryConfiguration` requires Bluetooth permissions, which the SDK checks at discovery.
- With a Bluetooth or USB reader requiring an update, status stays `CONNECTING` while the update installs. The SDK reports connected and ready only after the required update completes successfully.
- For Parcel access, replace `writeParcelable`/`readParcelable` with `writeSerializable`/`readSerializable`. The guide advises against persisting SDK model data across versions because model changes can make earlier data unreadable.
- `BluetoothReaderListener` and `UsbReaderListener` are replaced by `ReaderListener`. `Reader.registeredLocation` becomes `Reader.location`, and `Reader.device` is replaced by `Reader.bluetoothDevice` and `Reader.usbDevice`.
- `CaptureMethod.getManual()` is replaced by `CaptureMethod.MANUAL`. Use `CollectConfiguration.Builder` in place of the removed constructor.
- `CardDetails.fingerprint` and `CardPresentDetails.fingerprint` are removed from the Android SDK. The guide routes fingerprint access to Stripe server-side SDKs. See May's renamed and removed API list for other changes.

## Related

- [[source-stripe-terminal-design-custom-pos]] — new integration design
- [[source-github-stripe-terminal-ios]] and [[source-github-stripe-terminal-android]] — later version-specific SDK evidence

## Raw Sources

- [[raw/stripe-terminal-sdk-v3-migration-guide-2025|2026-05-01 v3.0.0 migration guide]] — iOS and Android variant bodies

## Related raw API references

- [[raw/stripe-terminal-references-sdk-v3-migration-guide-2026-11-07|2026-11-07 v3.0.0 migration variant index]]

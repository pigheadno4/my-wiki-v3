---
title: "Stripe Terminal: SDK Migration Guide (v3.0.0)"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-sdk-v3-migration-guide-2025.md"
tags: [stripe, stripe-terminal, sdk, ios, android, migration, v3]
---

## Summary

Breaking changes and migration guide for Stripe Terminal iOS and Android SDK v3.0.0.

## Breaking Changes Summary

**`processPayment` → `confirmPaymentIntent`**; `processRefund` → `confirmRefund` (both platforms — only rename, behavior unchanged).

**`readReusableCard` removed** (both platforms) → use SetupIntents instead.

**DiscoveryConfiguration** became a protocol/interface with per-reader-type implementations instead of a generic class with `DiscoveryMethod` enum.

**Offline payments**: `PaymentIntent.stripeId` (iOS) / `PaymentIntent.id` (Android) is null for offline payments — code must handle null safely.

## iOS-Specific Changes

- Min iOS: 11 → **13**
- `SCPErrorBusy` removed: SDK now queues commands internally — simplify any busy-state tracking code
- Parameters/Configuration classes now **immutable with Builder pattern** (`SCPCollectConfiguration`, `SCPPaymentIntentParameters`, etc.); `build()` throws in Swift
- `SCPReconnectionDelegate` now provides the reader instance (not terminal) — replace `terminal` with `reader` in method names
- `discoverReaders` completion now called when `connectReader` starts; `connectReader` no longer requires `discoverReaders` to be running

## Android-Specific Changes

- Min Android: API 21 → **API 26**
- **Permissions** now checked at discovery time (not SDK init); Bluetooth only required for `BluetoothDiscoveryConfiguration`
- Reader stays `CONNECTING` during required update installation (previously reported `CONNECTED` prematurely)
- **Parcelable → Serializable**: update `writeParcelable`/`readParcelable` to `writeSerializable`/`readSerializable`
- `BluetoothReaderListener` + `UsbReaderListener` → `ReaderListener`
- `Reader.registeredLocation` → `Reader.location`; `Reader.device` → `Reader.bluetoothDevice`/`Reader.usbDevice`
- `CaptureMethod.getManual()` → `CaptureMethod.MANUAL`
- `CardDetails.fingerprint`/`CardPresentDetails.fingerprint` removed (access via server-side SDKs)
- `CollectConfiguration` constructor removed → use `CollectConfiguration.Builder`

## Raw Sources

- [[stripe-terminal-sdk-v3-migration-guide-2025]] — verbatim webpage content

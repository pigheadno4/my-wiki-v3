---
title: "Stripe Terminal: SDK Migration Guide (v5.0.0)"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-sdk-migration-guide-2025.md"
tags: [stripe, stripe-terminal, sdk, ios, android, migration, v5]
---

## Summary

Breaking changes and migration guide for Stripe Terminal iOS and Android SDK v5.0.0.

## Breaking Changes Summary

**Unified payment methods** (both platforms):
- `processPaymentIntent` replaces `collectPaymentMethod` + `confirmPaymentIntent` (two steps → one)
- `processRefund` replaces `collectRefundPaymentMethod` + `confirmRefund`
- `processSetupIntent` replaces `collectSetupIntentPaymentMethod` + `confirmSetupIntent`

**Customer cancellation**: now **enabled by default** on all supported readers. API changed from `Bool` to `SCPCustomerCancellation` enum (iOS) / `CustomerCancellation` enum (Android). Use `.disableIfAvailable` / `DISABLE_IF_AVAILABLE` to restore prior behavior.

**New ConnectionStatus**: `.reconnecting` (iOS) / `RECONNECTING` (Android). `connectedReader` / `getConnectedReader()` is nil during reconnect.

**`easyConnect`**: new method combining discover + connect in one call (iOS 5.1+, Android 5.0+). Supports `discoveryFilter` by serial or reader ID.

**Interac refunds**: PaymentIntent ID now requires `clientSecret` too.

## iOS-Specific Changes

- Min iOS: 14 → **15**
- `Terminal.setTokenProvider` removed → use `Terminal.initWithTokenProvider(_:)` before accessing `Terminal.shared`
- `DiscoveryConfiguration` direct init removed → must use Builder classes
- Swift async/await supported for all Terminal methods

## Android-Specific Changes

- `Terminal.initTerminal` renamed to `Terminal.init`; now requires nullable `OfflineListener`
- **Apps on Devices**: all `Handoff` class names renamed to `AppsOnDevices` (e.g., `HandoffDiscoveryConfiguration` → `AppsOnDevicesDiscoveryConfiguration`); Maven artifact `stripeterminal-handoffclient` → `stripeterminal-appsondevices`
- Kotlin Coroutines: optional module `stripeterminal-ktx:5.0.0` adds `suspend` wrappers
- **Tap to Pay on Android**: now requires Android 13+; hardware-backed KeyStore v100+; debug options enabled → `TAP_TO_PAY_INSECURE_ENVIRONMENT` error; `TapZone` class refactored (indicator + position → single `TapZone` object)

## Raw Sources

- [[stripe-terminal-sdk-migration-guide-2025]] — verbatim webpage content (full iOS + Android before/after code examples)

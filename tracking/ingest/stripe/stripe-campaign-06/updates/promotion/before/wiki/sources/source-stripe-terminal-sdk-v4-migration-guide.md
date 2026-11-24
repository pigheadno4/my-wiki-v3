---
title: "Stripe Terminal: SDK Migration Guide (v4.0.0)"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-sdk-v4-migration-guide-2025.md"
tags: [stripe, stripe-terminal, sdk, ios, android, migration, v4]
---

## Summary

Breaking changes and migration guide for Stripe Terminal iOS and Android SDK v4.0.0.

## Breaking Changes Summary

**Global save-after-payment**: `allow_redisplay` replaces `customerConsentCollected` on both SetupIntents and PaymentIntents; enables saving payment details outside the US.

**Consolidated `connectReader`**: all platform-specific methods (`connectBluetoothReader`, `connectInternetReader`, `connectLocalMobileReader`, etc.) unified into `connectReader`. Reader delegate/listener moved into ConnectionConfiguration instead of method parameter.

**Auto-reconnect on by default**: `SCPReconnectionDelegate` (iOS) / `ReaderReconnectionListener` (Android) removed; reconnect events integrated into respective Reader delegates (`MobileReaderDelegate`, `TapToPayReaderDelegate`). Disable with `autoReconnectOnUnexpectedDisconnect = false`.

**New `discovering`/`DISCOVERING` ConnectionStatus**: represents when discovery is running. Multiple simultaneous `discoverReaders` now cancels the ongoing operation (returns `CANCELED_DUE_TO_INTEGRATION_ERROR`) instead of queuing.

**Disconnect callbacks consolidated**: `terminal:didReportUnexpectedReaderDisconnect` (iOS) / `TerminalListener::onUnexpectedReaderDisconnect` (Android) removed. Use `reader:didDisconnect:` / `onDisconnect` in the per-reader-type delegate/listener instead.

**Cancelable confirms**: `confirmPaymentIntent`, `confirmSetupIntent`, `confirmRefund` now return `Cancelable`. `cancelPaymentIntent`/`cancelSetupIntent` also cancel any ongoing collection — no need to cancel separately first.

## iOS-Specific Changes

- Min iOS: 13 → **14**
- `BluetoothReaderDelegate` → `MobileReaderDelegate`
- `collectedAt` → `storedAt` in `SCPOfflineDetails`
- "local mobile" / "apple built in" → "Tap To Pay" in all names and error codes
- `paymentMethodTypes` now uses `SCPPaymentMethodType` enum (not strings)
- `SCPSetupIntent.stripeId` now nullable

## Android-Specific Changes

- `TerminalException.TerminalErrorCode` moved to standalone `TerminalErrorCode` enum
- `ReaderListener` → `MobileReaderListener`
- `LocalMobile` → `TapToPay` everywhere (`LocalMobileDiscoveryConfiguration` → `TapToPayDiscoveryConfiguration`, etc.)
- TapToPay Maven artifact: `stripeterminal-localmobile` → `com.stripe:stripeterminal-taptopay:4.0.0`
- `java.util.Date` → millisecond timestamps in `ReaderSoftwareUpdate::requiredAt`, `OfflineDetails::storedAt`
- Tap to Pay: 60s timeout → `CARD_READ_TIMED_OUT`; `Location` fields now immutable

## Raw Sources

- [[stripe-terminal-sdk-v4-migration-guide-2025]] — verbatim webpage content (full iOS + Android before/after code examples)

---
title: "Stripe Terminal: SDK Migration Guide (v4.0.0)"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/references/sdk-v4-migration-guide"
raw_files:
  - "stripe-terminal-sdk-v4-migration-guide-2025.md"
tags: [stripe, stripe-terminal, sdk, ios, android, migration, v4]
---

## Summary

The May 1, 2026 capture documents breaking changes for existing [[stripe-terminal|Stripe Terminal]] iOS and Android integrations migrating to SDK 4.0.0.

## Breaking Changes Summary

**Save after payment**: The v4 guide documents saving payment details outside the US. For the in-person PaymentIntent flow, pass `setup_future_usage` at creation and `allow_redisplay` at collection.

**Save without payment**: `collectSetupIntentPaymentMethod` replaces the direct SetupIntent flow’s `customerConsentCollected` parameter with `allowRedisplay`.

**Consolidated `connectReader`**: all platform-specific methods (`connectBluetoothReader`, `connectInternetReader`, `connectLocalMobileReader`, etc.) unified into `connectReader`. Reader delegate/listener moved into ConnectionConfiguration instead of method parameter.

**Auto-reconnection**: v4 enables auto-reconnection by default after an unexpected disconnect for mobile and Tap to Pay readers. iOS removed `SCPReconnectionDelegate` and moved its callbacks into the respective reader delegates. Android replaced the separate `ReaderReconnectionListener` configuration parameter with the relevant reader listener, which inherits reconnection events. Set the platform’s `autoReconnectOnUnexpectedDisconnect` option to `false` to disable the behavior.

**New `discovering`/`DISCOVERING` ConnectionStatus**: Represents when discovery is running. A new `discoverReaders` request cancels the in-progress discovery with the platform’s integration-cancellation error and starts immediately. Smart and Tap to Pay reader discovery invokes its completion callback when the operation ends.

**Disconnect callbacks consolidated**: `terminal:didReportUnexpectedReaderDisconnect` (iOS) / `TerminalListener::onUnexpectedReaderDisconnect` (Android) removed. Use `reader:didDisconnect:` / `onDisconnect` in the per-reader-type delegate/listener instead.

If enabled auto-reconnection fails and the reader disconnects, the reader delegate or listener receives both the reconnection-failure and disconnect callbacks.

**Cancelable confirms**: `confirmPaymentIntent`, `confirmSetupIntent`, and `confirmRefund` return a `Cancelable` in the v4 guide. Calling `cancelPaymentIntent` or `cancelSetupIntent` also stops any ongoing payment processing, including collection.

## iOS-Specific Changes

- Terminal iOS SDK 4.0.0 requires iOS 14 or higher. Existing Terminal iOS SDK 3.x versions continue to support iOS 13 and later.
- `BluetoothReaderDelegate` → `MobileReaderDelegate`
- `collectedAt` → `storedAt` in `SCPOfflineDetails`
- "local mobile" / "apple built in" → "Tap To Pay" in all names and error codes
- `paymentMethodTypes` now uses `SCPPaymentMethodType` enum (not strings)
- `SCPSetupIntent.stripeId` now nullable

## Android-Specific Changes

- `TerminalException.TerminalErrorCode` moved to standalone `TerminalErrorCode` enum
- `ReaderListener` → `MobileReaderListener`
- `LocalMobile` → `TapToPay` everywhere (`LocalMobileDiscoveryConfiguration` → `TapToPayDiscoveryConfiguration`, etc.)
- Tap to Pay moves to Maven coordinate `com.stripe:stripeterminal-taptopay:4.0.0`. The predecessor artifact stops receiving updates.
- `java.util.Date` → millisecond timestamps in `ReaderSoftwareUpdate::requiredAt`, `OfflineDetails::storedAt`
- For Tap to Pay on Android, `collectPaymentMethod` and `collectSetupIntentPaymentMethod` time out after 60 seconds with `CARD_READ_TIMED_OUT`.
- `Location` fields become immutable.

## Detail Locators

- The May 1, 2026 full guide’s **Migrate to version 4.0.0** section records smart-reader MOTO preview and the access-request route at that date.

## Raw Sources

- [[raw/stripe-terminal-sdk-v4-migration-guide-2025|May 1, 2026 full iOS and Android v4 migration guide with before-and-after examples]]

## Related raw API references

- [[raw/stripe-terminal-references-sdk-v4-migration-guide-2026-11-07|November 7, 2026 v4 migration index with iOS and Android variant links]]

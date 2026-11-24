---
title: "Stripe Terminal: SDK Migration Guide (v5.0.0)"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
raw_files:
  - "stripe-terminal-sdk-migration-guide-2025.md"
tags: [stripe, stripe-terminal, sdk, ios, android, migration, v5]
---

## Summary

The 2026-05-01 migration guide covers breaking changes for the Stripe Terminal iOS and Android SDKs when upgrading to v5.0.0.

## Breaking Changes Summary

**Unified payment methods** (both platforms):
- Stripe recommends `processPaymentIntent` to collect and confirm in one call. The existing `collectPaymentMethod` and `confirmPaymentIntent` methods continue to work in v5.
- Use `processRefund` for the combined refund flow. The two-step `collectRefundPaymentMethod` and `confirmRefund` methods are deprecated in v5.
- `processSetupIntent` combines the setup intent collection and confirmation steps.

**Customer cancellation** is enabled by default on supported readers. Use `.disableIfAvailable` with the iOS `SCPCustomerCancellation` enum or `CustomerCancellation.DISABLE_IF_AVAILABLE` on Android to opt out.

**Connection status** adds `.reconnecting` on iOS and `RECONNECTING` on Android. On iOS, `connectedReader` is `nil` during reconnection until it succeeds. The Android guide documents `getConnectedReader()` returning `null` during initial connection until the attempt succeeds.

**`easyConnect`** combines discovery and connection for smart readers and Tap to Pay on iOS 5.1 or later. The Android guide documents it for smart readers, Tap to Pay, and Apps on Devices. Internet reader discovery supports filtering by serial number or reader ID.

**Interac refunds** require the PaymentIntent's `clientSecret` when using its PaymentIntent ID. The charge-ID path does not require it.

## iOS-Specific Changes

- The v5 minimum is iOS 15. Existing iOS SDK 4.x releases support iOS 14 and later.
- `Terminal.setTokenProvider` was removed. Use `Terminal.initWithTokenProvider(_:)` before accessing `Terminal.shared`.
- Use the associated builder classes to initialize `DiscoveryConfiguration` objects.
- Terminal methods have Swift async variants.

## Android-Specific Changes

- `Terminal.initTerminal` was renamed to `Terminal.init` and now requires a nullable `OfflineListener` parameter.
- **Apps on Devices** renamed its `Handoff` classes to `AppsOnDevices` (for example, `HandoffDiscoveryConfiguration` to `AppsOnDevicesDiscoveryConfiguration`). The Maven artifact changed from `stripeterminal-handoffclient` to `stripeterminal-appsondevices`. Stripe says it will no longer update the old artifact.
- The optional `stripeterminal-ktx:5.0.0` module adds Kotlin coroutine `suspend` wrappers.
- **Tap to Pay on Android** requires Android 13 or later and hardware-backed KeyStore key agreement from SDK 5.0.0. Check the hardware support with `supportsReadersOfType()` or `FEATURE_HARDWARE_KEYSTORE` version 100 or later. Production reader discovery fails with `TAP_TO_PAY_INSECURE_ENVIRONMENT` if device debug options are enabled. The simulated Tap to Pay reader is exempt from this debug-options restriction. The guide also covers the refactored `TapZone` object and lists Discover acceptance as public preview.

## Related

- [[stripe]]
- [[stripe-terminal]]

## Raw Sources

- [[stripe-terminal-sdk-migration-guide-2025]] — 2026-05-01 v5.0.0 migration guide with full iOS and Android before/after examples

## Related raw API references

- [[raw/stripe-terminal-references-sdk-migration-guide-2026-11-07|2026-11-07 Terminal SDK v6.0.0 migration guide index]] — navigation to the [iOS](https://docs.stripe.com/terminal/references/sdk-migration-guide.md?terminal-sdk-platform=ios) and [Android](https://docs.stripe.com/terminal/references/sdk-migration-guide.md?terminal-sdk-platform=android) variants. The capture contains the index only.

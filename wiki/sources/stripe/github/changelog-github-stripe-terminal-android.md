---
title: "GitHub changelog: stripe/stripe-terminal-android"
type: source
date_ingested: 2026-08-31
date_updated: 2026-08-31
original_format: github-repo
raw_files:
  - "github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/manifest.json"
tags: [stripe, terminal, android, kotlin, java, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-terminal-android`. Durable architecture and integration knowledge belongs in [[source-github-stripe-terminal-android]]; this page records package-qualified changes and migration impact.

## `stripeterminal@5.8.0` - Change Set `b3de15b` (2026-08-17)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `com.stripe:stripeterminal` | Initial retained baseline | `5.8.0` | 2026-08-17 | `b3de15b57201df0aa0e0235ccbe8e81bf9abaa8f` | Full |

### Exact Release Changes

- Adds `TerminalErrorCode.PRINTER_LOW_BATTERY` for print operations blocked by reader battery level.
- Reads and sets buzzer volume on supported readers through `getReaderSettings` and `setReaderSettings`, with low, high, or exact volume values.
- Makes `ACCESS_COARSE_LOCATION` sufficient for SDK location reporting. Apps that need precise location for their own behavior must explicitly retain and request fine location.
- Declares the SDK's Bluetooth discovery permissions, including `BLUETOOTH_SCAN` with `neverForLocation` on Android 12+ and fine location capped at Android 11 for BLE compatibility.
- Fixes `Terminal.init()` crashes on devices with unsupported Android Keystore implementations.
- Fixes mobile-reader software updates timing out on slow network connections.
- Fixes Tap to Pay PIN collection failures on certain device models.

### Developer and Merchant Impact

Applications can reduce location permission scope when they do not need precise location, but should review their merged manifest rather than assume previous transitive declarations remain unchanged. Reader-management interfaces can expose buzzer settings and report low-battery print failures. Initialization, update, and Tap to Pay PIN paths are more resilient on affected devices.

### Migration Action

No general breaking API migration is documented for `5.8.0`. Android teams should inspect the merged manifest, add explicit fine-location declarations only when their application needs them, feature-detect reader settings, handle the new print error, and retest Keystore initialization, slow updates, and Tap to Pay PIN entry on supported devices.

### Evidence Boundary

The exact additions and fixes above come from the `5.8.0` changelog entry. The broader reader, payment, SetupIntent, refund, offline, and support knowledge in the cumulative source is baseline evidence and must not be attributed solely to this patch.

### Evidence

- Release manifest: `raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.0/2026-08-31/manifest.json`
- Release notes: `raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.0/2026-08-31/release-notes.md`
- Snapshot manifest: `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/manifest.json`
- Cumulative changelog: `raw/github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/files/CHANGELOG.md`

## Version 5 Major Boundary (`5.0.0`, 2025-11-03)

- Adds combined `processPaymentIntent`, `processSetupIntent`, and `processRefund` operations.
- Adds optional Kotlin coroutine wrappers in `com.stripe:stripeterminal-ktx`.
- Adds `easyConnect` for Tap to Pay, smart-reader, and Apps on Devices flows and introduces `ConnectionStatus.RECONNECTING`.
- Replaces `initTerminal` with `Terminal.init`, changes credential-clearing and connected-reader timing, and renames multiple payment and refund configuration classes.
- Enables customer cancellation by default where supported and changes cancellation completion and payment-status behavior.

An upgrade from 4.x requires a complete migration review; it is not a patch-level replacement.

## Accumulated `5.1.0--5.7.0` Context

| Release | Retained milestone |
| --- | --- |
| `5.1.0` | Simulated MOTO, mobile-reader QR payments, Tap to Pay simulation and connection fixes |
| `5.2.0--5.5.0` | Reader, payment-method, Tap to Pay, update, and generated-card fixes plus preview capabilities |
| `5.6.0` | Locale-configured API errors and an offline database migration bug affecting upgrades from `4.1.0` or earlier |
| `5.7.0` | Fix for the `5.6.0` offline data-loss bug, overcapture status, Tap to Pay surcharging preview, and additional generated-card and Keystore fixes |

These entries are cumulative upstream history retained in the `5.8.0` snapshot, not automated comparisons against every intermediate tag.

## Support Lifecycle

The retained policy gives each major approximately one year of active development, one year of maintenance, and one deprecated year before hard blocking. For 5.x, patch support runs through October 2027 and the hard-block date is October 2028. Version 4.x is scheduled for hard block in October 2027; versions 1.x through 3.x are scheduled for hard block in January 2027. Tap to Pay may impose earlier upgrade requirements.

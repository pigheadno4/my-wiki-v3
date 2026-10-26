---
title: "GitHub changelog: stripe/stripe-terminal-android"
type: source
date_ingested: 2026-08-31
date_updated: 2026-10-26
original_format: github-repo
raw_files:
  - "github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/manifest.json"
  - "github/stripe/stripe-terminal-android/snapshots/2026-10-26-abb16f5/manifest.json"
  - "github/stripe/stripe-terminal-android/snapshots/2026-10-26-846d401/manifest.json"
  - "github/stripe/stripe-terminal-android/snapshots/2026-08-31-b3de15b/manifest.json"
tags: [stripe, terminal, android, kotlin, java, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-terminal-android`. Durable architecture and integration knowledge belongs in [[source-github-stripe-terminal-android]]; this page records package-qualified changes and migration impact.

## `stripeterminal@6.0.0` - Change Set `0829be9` (2026-10-07)

Approved additive full ingest from 5.8.2, completed 2026-10-26 after both deltas. Exact SHA `0829be9e77842bc12a6ba56d64fd152b53506025`. Preserves every v5 release section, quote and raw reference. Counts: 341 modified, eight added, five removed and 101 unchanged retained files; effective full assignment 94 paths / 6,520,286 bytes. User-approved focused reading covers authored changes, semantic API changes, affected prior code and wiki history; unchanged/version-only/generated evidence checked mechanically. All 1,791 files across four snapshots pass size/SHA-256/Git identities.

### Upgrade Findings

- **Platform:** compile SDK 35+, SDK Kotlin 2.3.21 dependencies; retained README/example minimum API remains 26. These are build/dependency requirements, not Android 15 on every customer device. Match all Terminal artifacts. Initialization now requires LocaleConfig; old Tap to Pay constructor becomes TapUseCase.Pay.
- **Capture:** SDK builder defaults to AutomaticAsync. Explicit Manual for receipt tipping/incremental/extended auth; changed Java/Kotlin event examples enforce Manual for authorization extensions. Java still captures on any successful Intent ID without a status guard: static integration risk, not a proven duplicate charge. Reciprocal capture-documentation contradiction recorded in source and Terminal concept.
- **Consent/models:** consent moves into required CollectSetupIntentConfiguration; demo ALWAYS is not proof of consent. latestCharge/latestChargeId replace getCharges; invoice retrieval moves server-side. Separate PaymentMethod.CardPresent/Charge.CardPresent and SetupAttempt detail renames; nullable instrument expiry and Refund ID; ProcessRefundParameters rename. Changelog is the authority for model/config types outside the capsule.
- **Reader UI:** separate ReaderPaymentInteractionListener on mobile Bluetooth/USB/external-USB connections; missing listener causes failure if the transaction needs an interaction. Invoke the concrete interaction callback. This is not the iOS delegate contract. Reader cancellation CANCELED_BY_READER differs from SDK CANCELED; low-battery error generalized.
- **Tap to Pay:** MODIFY_AUDIO_SETTINGS requirement; upcoming-update callback is advisory and does not itself block payment acceptance/install updates/change connection state. UX types lose Parcelable, names become Theme/colorScheme and default becomes SYSTEM; expired attestation session uses SESSION_EXPIRED. No merged-manifest or device execution proof.
- **Refund preview:** new non-collecting confirmRefund(parameters, callback) is distinct from removed old split confirmation. Successful callback may require action; unknown outcome without attached Refund requires reconciliation before creating another refund. In-person Interac rules and preview access gates remain.
- **Other:** MOTO authorization code needs smart-reader firmware 2.45+; SDK Proguard changes and Tap to Pay cancellation fixes are upstream release statements. Old simulator-update APIs removed. No Android MSI/Swish or iOS distribution-policy inference.

### Historical Clarification and Limits

The raw changelog retrospectively identifies 5.4.0–5.6.0 as affected by missing generated_card, fixed in 5.7.0, and adds corresponding known-issue sections. These are not newly fixed v6 issues. Older wiki attribution and the distinct offline database-loss history remain intact. Regenerated property-initializer text is not proof of changed runtime defaults. Unchanged SUPPORT.md has no dated v6 schedule row; no date is inferred.

Six concepts updated first, then cumulative source/history/company/index/logs. Source count 666 preserved. No additional collection/supplement, SDK build, device/payment execution, commit or push. See [[source-github-stripe-terminal-android]] for located quotes, contradictions, exact example/API evidence and remaining scope limits.

Evidence: [snapshot](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/manifest.json), [release](raw/github/stripe/stripe-terminal-android/releases/stripeterminal/6.0.0/2026-10-26/manifest.json), [notes](raw/github/stripe/stripe-terminal-android/releases/stripeterminal/6.0.0/2026-10-26/release-notes.md), [exact changelog](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-0829be9/files/CHANGELOG.md), [comparison](tracking/github/repos/stripe/stripe-terminal-android/comparisons/stripeterminal/5.8.2--6.0.0/comparison.json).

## `stripeterminal@5.8.2` - Change Set `abb16f5` (2026-10-02)

Approved serial focused-reading delta from 5.8.1, ingested 2026-10-26, SHA `abb16f502cbe0fcc82f673c246c86c883a5c2fdc`. Reports a Tap to Pay China UnionPay payment-failure fix. No retained implementation or semantic API change: 337 version-only documentation changes plus README, two Gradle files and changelog; 106 unchanged files. The old 5.8.1 note's "Union Pay" spelling becomes "UnionPay"; original wiki attribution/quote preserved. Raw/packet hashes and unchanged/version-only evidence verified mechanically; changed authored content, affected prior code and cumulative history read fully. Concept first, then source/history/company/catalog/logs; no SDK/payment test or deletion of older history.

Evidence: [snapshot](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-abb16f5/manifest.json), [release](raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.2/2026-10-26/manifest.json), [notes](raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.2/2026-10-26/release-notes.md), [exact changelog](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-abb16f5/files/CHANGELOG.md), [comparison](tracking/github/repos/stripe/stripe-terminal-android/comparisons/stripeterminal/5.8.1--5.8.2/comparison.json). Details [[source-github-stripe-terminal-android]].

## `stripeterminal@5.8.1` - Change Set `846d401` (2026-09-14)

Approved focused-reading delta from 5.8.0, ingested 2026-10-26, SHA `846d401d1f7bc686a2c12d6def4342471c25a625`. Adds China UnionPay support in Hong Kong for Tap to Pay on Android per exact-SHA changelog. No retained example implementation change; 337 API pages change only version strings, with four other modified files (changelog, README, two Gradle files) and 106 unchanged files. Both 447-file snapshots hash/size checked; historical changelog retained. Use matched 5.8.1 artifacts; no new minimum-device-API or public API contract follows. Proprietary runtime/eligibility/payment behavior not independently tested. Updated Terminal concept first, then source/history/company/index/logs; all prior history preserved.

Evidence: [snapshot](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-846d401/manifest.json), [release](raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.1/2026-10-26/manifest.json), [notes](raw/github/stripe/stripe-terminal-android/releases/stripeterminal/5.8.1/2026-10-26/release-notes.md), [exact changelog](raw/github/stripe/stripe-terminal-android/snapshots/2026-10-26-846d401/files/CHANGELOG.md), [comparison](tracking/github/repos/stripe/stripe-terminal-android/comparisons/stripeterminal/5.8.0--5.8.1/comparison.json). Details [[source-github-stripe-terminal-android]].

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

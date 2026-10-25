---
title: "GitHub changelog: stripe/stripe-terminal-ios"
type: source
date_ingested: 2026-08-31
date_updated: 2026-10-25
original_format: github-repo
raw_files:
  - "github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/manifest.json"
  - "github/stripe/stripe-terminal-ios/snapshots/2026-10-25-00cd46d/manifest.json"
  - "github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/manifest.json"
tags: [stripe, terminal, ios, swift, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-terminal-ios`. Durable architecture and integration knowledge belongs in [[source-github-stripe-terminal-ios]]; this page records package-qualified changes and migration impact.

## `StripeTerminal@6.0.0` - Change Set `79cfb32` (2026-10-07)

Approved additive full ingest, completed 2026-10-25 after the 5.8.1 delta. Exact SHA `79cfb3225553a7a5cceb8325f1c1f9087f792128`. All v5 knowledge remains. Package-version order here is not publication order: 5.8.1 was published after 6.0.0, and their branches diverge from 5.8.0.

### Changes and Migration

- **Distribution/platform:** iOS 16 minimum; Xcode 16+/Swift 6+ for integrators versus Xcode 27/Swift 6.4 used to build the binary. Cumulative raw changelog announces SPM-only new releases, including patches for older versions; existing CocoaPods versions continue working without future CocoaPods updates. README points SPM at `stripe-terminal-ios-spm`; example switches to `.xcodeproj` and removes Podfiles.
- **Payment capture:** client builder defaults to `.automaticAsync`, replacing `.manual`. Explicitly select manual for receipt tipping, incremental and extended authorization. Retained example enforces this and captures through its backend only for `requiresCapture` when not skipped. Recorded a reciprocal contradiction for the older unqualified manual-capture comment still in the v6 header.
- **Consent/model breaking changes:** required `CollectSetupIntentConfigurationBuilder(allowRedisplay:)` and collect/process configuration; SetupIntent expanded `paymentMethod` versus ID `paymentMethodId`; PaymentIntent `latestCharge`/`latestChargeId` instead of `charges`; server retrieval for the invoice relationship per the note. Separate instrument/transaction card-present models; nullable instrument expiry; API-string brand/network/funding/read-method fields, nullable funding and future-value handling; old conversion helpers/enum exports removed. Optional payment-account reference and application/review IDs exposed.
- **Reader migration:** shared reader-prefixed lifecycle/display callbacks; separate weakly referenced, app-retained payment-interaction delegate and completion-driven selection/QR types. Optional mobile-reader update availability is not Tap to Pay optional-update support. Per-collection cancellation replaces connection `allowCustomerCancel`.
- **Cancellation/errors:** reader/customer cancellation becomes `.canceledByReader` (2021), SDK cancellation stays `.canceled` (2020). Example's cancel-Intent error branch still checks only the latter. Printer-specific low battery becomes general `.readerBatteryLow`; reconnect note fixes refined peer-removal reasons. Broader simulated-offline access is not live offline GA.
- **Refunds:** rename process-refund parameters and remove deprecated split overloads. Private-preview `confirmRefund(parameters)` authenticates through a connected reader without card collection/UI; unknown outcomes must be reconciled before creating another refund. Nullable Refund ID plus canceled/requiresAction/nextAction handling. Interac presence requirements remain.
- **Previews and reader support:** Mexico MSI enablement and post-collect available plans/post-confirm selected plan; Swish method/details; WisePad 3 amount surcharge and confirm-time consent, but no collect-time `surchargeNotice`. Merchant, firmware, country and preview eligibility remain independent gates.
- **Other migration:** use `stripeDescription` instead of deprecated parameter description aliases; connection `testReaderUpdate` instead of the deprecated simulator update property/enum.

### Evidence and Reading Boundary

The queued cross-branch 5.8.1 -> 6.0.0 packet has ten added, 56 modified, two removed and 177 unchanged retained files. Reviewed both it and the common-ancestor 5.8.0 -> 6.0.0 comparison; proprietary v6 inclusion of the 5.8.1 fix remains unproven. User-approved focused reading fully covered changed headers/examples, affected prior code, new history/notes and cumulative wiki; unchanged files/history and generated inventories were mechanically verified. All 713 files across three snapshots match size/SHA-256/Git blob identities; the raw history starting at 5.8.0 is unchanged.

Updated six existing concepts first, then the cumulative source/history, company, provider index and logs. No source-count change, other repository ingestion, SDK build, reader/payment execution, commit or push. The capsule excludes SceneDelegate/build configuration, and the unchanged support schedule has no dated v6 row; neither gap is filled by inference.

**Evidence:** [snapshot](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/manifest.json), [release](raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/6.0.0/2026-10-25/manifest.json), [notes](raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/6.0.0/2026-10-25/release-notes.md), [raw changelog](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-79cfb32/files/CHANGELOG.md), [common-baseline comparison](tracking/github/repos/stripe/stripe-terminal-ios/comparisons/stripeterminal/5.8.0--6.0.0/comparison.json), [cross-branch comparison](tracking/github/repos/stripe/stripe-terminal-ios/comparisons/stripeterminal/5.8.1--6.0.0/comparison.json). Exact header/example links and located quotes: [[source-github-stripe-terminal-ios]].

## `StripeTerminal@5.8.1` - Change Set `00cd46d` (2026-10-09)

Approved focused-reading delta from `5.8.0`, ingested 2026-10-25. Exact SHA `00cd46de3ad9a7847c5d8ccb30abcf311a1e26e0`; GitHub publication October 9 UTC versus October 8 in the note. Three modified retained files, 232 unchanged.

**Change:** upstream reports an offline PaymentIntent parameter-preservation fix for Tap to Pay destination charges using `onBehalfOf`. Public evidence contains only the changelog, binary URL/checksum and SDK version constant changes. No exposed API migration or iOS-minimum change; proprietary binary behavior was not independently verified.

**Reading and preservation:** all changed header/package content, notes, comparison and cumulative wiki context read; historical changelog suffix and current/prior raw hashes verified mechanically under approval. Updated the existing Terminal concept first, source/history, company/catalog/logs; all older history and source_count preserved. No upstream build/reader/payment execution.

**Evidence:** [snapshot](raw/github/stripe/stripe-terminal-ios/snapshots/2026-10-25-00cd46d/manifest.json), [release](raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/5.8.1/2026-10-25/manifest.json), [notes](raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/5.8.1/2026-10-25/release-notes.md), [comparison](tracking/github/repos/stripe/stripe-terminal-ios/comparisons/stripeterminal/5.8.0--5.8.1/comparison.json). See [[source-github-stripe-terminal-ios]].

## `StripeTerminal@5.8.0` - Change Set `c027d6d` (2026-08-18)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `StripeTerminal` | Initial retained baseline | `5.8.0` | 2026-08-18 | `c027d6dc2258c774412cb7933cbb959488c16b63` | Full |

### Exact Release Changes

- Reads and sets buzzer volume on supported readers through reader settings. Custom volume must be within `1...maxVolume`; unsupported readers report unavailable or fail the update.
- Exposes complete PaymentMethod objects through `generatedCardExpanded` and `paymentMethodExpanded` for SetupIntent saving flows.
- Adds `error`, `warning`, and `info` logging thresholds.
- Adds a printer-low-battery error and an `unknown` device type for unrecognized readers.
- Corrects mobile-reader Bluetooth disconnect reasons, including out-of-range and removed-pairing cases.
- Fixes a Tap to Pay on iPhone crash when the connected reader or reader account ID is unexpectedly unavailable during collection.

### Developer and Merchant Impact

Reader-management applications can expose buzzer controls and distinguish unsupported hardware. SetupIntent integrations can consume expanded PaymentMethod data without assuming that consent or server-side customer management disappeared. Disconnect telemetry becomes more actionable, and Tap to Pay collection is more resilient.

### Migration Action

No release-specific breaking migration is documented for `5.8.0`. Integrations should feature-detect buzzer support, handle `DeviceType.unknown` conservatively, avoid depending on old inaccurate disconnect reasons, and test low-battery printing and Tap to Pay collection failure paths.

### Evidence Boundary

The exact `5.8.0` additions and fixes come from its release note. The broader payment, reader, offline, SetupIntent, refund, and migration knowledge in the cumulative source is baseline evidence and must not be attributed solely to this patch.

### Evidence

- Release manifest: `raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/5.8.0/2026-08-31/manifest.json`
- Release notes: `raw/github/stripe/stripe-terminal-ios/releases/stripeterminal/5.8.0/2026-08-31/release-notes.md`
- Snapshot manifest: `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/manifest.json`
- Public API: `raw/github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/files/PublicHeaders/`

## Version 5 Major Boundary (`5.0.0`, 2025-11-03)

- Raises the deployment target from iOS 14 to iOS 15 and uses Xcode 26 / Swift 6.2.
- Replaces token-provider mutation with mandatory `Terminal.initWithTokenProvider` before `Terminal.shared`.
- Adds combined `processPaymentIntent`, `processSetupIntent`, and `processRefund` operations plus Swift async variants.
- Adds explicit reconnecting state and changes when `connectedReader` becomes visible.
- Changes cancellation completion guarantees, credential-clearing behavior, discovery configuration construction, payment-status transitions, and default customer cancellation.
- Removes P400 support, removes `SCPJSONDecodable`, and deprecates split refund collection/confirmation.

An upgrade from 4.x requires a full migration review; it is not a patch-level replacement.

## Accumulated `5.1.0--5.7.0` Context

| Release | Retained milestone |
| --- | --- |
| `5.1.0` | EasyConnect, internet-reader filters, mPOS QR payment callbacks, simulated MOTO |
| `5.2.0` | WisePad 3 tip eligibility, M2 surcharging preview, Tap to Pay QR callbacks and compatibility checks |
| `5.3.0` | Reader-connection race crash fix |
| `5.4.0` | Donation, multicapture, and reauthorization previews; capture deadline and richer API errors |
| `5.5.0` | Refactored surcharge model, Tap to Pay account-link check, simulated offline/update scenarios |
| `5.6.0` | Tap to Pay offline private preview, overcapture status, API-error locale configuration |
| `5.7.0` | Tap to Pay surcharging preview and corrected critical-battery disconnect reason |

These entries are cumulative upstream history retained in the `5.8.0` snapshot, not automated comparisons against every intermediate tag.

## Support Lifecycle

The retained policy gives each major one year of active development, one year of maintenance, and one deprecated year before hard blocking. For 5.x, patch support runs through October 2027 and the hard-block date is October 2028. Tap to Pay can impose earlier upgrade constraints.


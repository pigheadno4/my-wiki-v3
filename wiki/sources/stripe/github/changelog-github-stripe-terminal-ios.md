---
title: "GitHub changelog: stripe/stripe-terminal-ios"
type: source
date_ingested: 2026-08-31
date_updated: 2026-08-31
original_format: github-repo
raw_files:
  - "github/stripe/stripe-terminal-ios/snapshots/2026-08-31-c027d6d/manifest.json"
tags: [stripe, terminal, ios, swift, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-terminal-ios`. Durable architecture and integration knowledge belongs in [[source-github-stripe-terminal-ios]]; this page records package-qualified changes and migration impact.

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


---
title: "GitHub changelog: Adyen/adyen-web"
type: source
date_ingested: 2026-07-26
original_format: github-repo
raw_files:
  - "github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-08-09-c98ea8a/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/manifest.json"
tags: [adyen, checkout, web-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-web`. Cumulative implementation knowledge belongs in [[source-github-adyen-web]] and the linked immutable snapshots.

## `@adyen/adyen-web@6.42.0` (2026-08-04)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@adyen/adyen-web` | `6.41.1` | `6.42.0` | `1e157f8bc62b9519d68becedd9c1267180810e77` | Delta |

**Important findings:** Drop-in emits a new `paymentListDisplayed` analytics event with rendered methods, display modes, display order, and unavailable `/paymentMethods` entries. Partial billing-address forms retain the merchant country so US ZIP and ZIP+4 formatting and validation apply. 3DS2 iframes gain permission-policy attributes for payment, WebAuthn, and SPC challenges, with an internal Visa passkey path adding credential creation and sandbox controls.

**Developer or merchant impact:** Drop-in telemetry can distinguish what shoppers were shown from methods returned but not rendered. US partial-address checkout no longer loses country-specific postal rules. Passkey-capable 3DS challenges receive the iframe permissions required for delegated credential operations.

**Migration action:** No breaking migration is documented. Review analytics governance for the new payment-list event, and retest partial US billing addresses if the integration supplies country without rendering a country field. The passkey switch is internal and is not evidence of a general merchant configuration surface.

**Updated source sections:** Evidence boundary; 3D Secure 2 and action safety; analytics, risk, and sensitive-data boundary; `6.42.0` minor-release behavior; Adyen company summary and provider index.

**Evidence boundary:** The exact-SHA snapshot retains the checkout-facing Drop-in and 3DS2 files. The approved supplement retains the changed internal Address and IFrame files. Tests remain excluded by collection policy, and server-side analytics use or passkey eligibility is outside this repository capsule.

**Evidence:**

- Release manifest: `raw/github/adyen/adyen-web/releases/adyen-web/6.42.0/2026-08-09/manifest.json`
- Release notes: `raw/github/adyen/adyen-web/releases/adyen-web/6.42.0/2026-08-09/release-notes.md`
- Snapshot manifest: `raw/github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/manifest.json`
- Comparison manifest: `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.41.1--6.42.0/comparison.json`
- Human-readable comparison: `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.41.1--6.42.0/comparison.md`
- Source supplement: `raw/github/adyen/adyen-web/supplements/2026-08-09-1e157f8-b6a47e83/manifest.json`

## `@adyen/adyen-web@6.41.1` (2026-07-30)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@adyen/adyen-web` | `6.41.0` | `6.41.1` | `c98ea8a7fe3c504075509755a0eda2264042d076` | Delta |

**Important findings:** OpenInvoice error focus is scoped to the active Component container; interactive selectors stop Enter-key events from reaching the root payment submission handler; address formatting defers trimming until blur to prevent duplicate IME characters; and BIN lookup gains narrower internal Card element types. The patch also updates `@paypal/paypal-js` from `10.0.0` to `10.0.2` and `@types/googlepay` from `0.7.10` to `0.7.11`.

**Developer or merchant impact:** Merchants with multiple OpenInvoice Components avoid cross-instance error focus. Keyboard users can activate selectors without accidentally submitting payment, and shoppers using input method editors avoid duplicated address characters.

**Migration action:** No breaking migration is documented. Upgrade when affected by these accessibility, keyboard, or IME issues, and recheck custom keyboard handlers that wrap Adyen controls.

**Updated source sections:** Evidence boundary; PayPal Fastlane dependency; `6.41.1` patch behavior; Adyen company summary and provider index.

**Evidence boundary:** Release notes identify the fixes, while the approved exact-SHA supplement retains the changed implementation files that fell outside the standard checkout capsule. Tests remain excluded by collection policy. The dependency bump does not prove behavior inside the independently versioned PayPal runtime.

**Evidence:**

- Release manifest: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.1/2026-08-09/manifest.json`
- Release notes: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.1/2026-08-09/release-notes.md`
- Snapshot manifest: `raw/github/adyen/adyen-web/snapshots/2026-08-09-c98ea8a/manifest.json`
- Comparison manifest: `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.41.0--6.41.1/comparison.json`
- Human-readable comparison: `tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.41.0--6.41.1/comparison.md`
- Source supplement: `raw/github/adyen/adyen-web/supplements/2026-08-09-c98ea8a-4b5b69c5/manifest.json`

## `@adyen/adyen-web@6.41.0` (2026-07-16)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@adyen/adyen-web` | Initial baseline | `6.41.0` | `b19eec7054340a1526c87d450fd7dfff75794ed9` | Full |

**Important findings:** The release propagates `healthcare` through `onBinLookup`, detects a missing valid domain in a 3DS2 challenge notification URL, replaces deprecated `keypress` handling, removes explicit `any` types in several Components, hides component-level installments in Sessions, and restores Drop-in `aria-checked` state when the first method remains closed.

**Developer or merchant impact:** Define installments when creating the Session, not on the Card Component, for Sessions integrations. Invalid 3DS2 challenge notification domains now fail before an unfinishable challenge is rendered. Drop-in integrations using `openFirstPaymentMethod=false` gain corrected assistive state.

**Migration action:** Review any Sessions integration that supplies Card installments locally and move that configuration to Session creation. No other breaking migration is documented for this patch.

**Updated source sections:** Sessions and advanced flow; Card behavior; 3D Secure 2 and action safety; accessibility; Adyen company summary; co-badged-cards implementation evidence.

**Evidence boundary:** This is the first retained Adyen Web baseline, so no prior exact-SHA comparison exists. Patch findings come from upstream release notes and the complete retained source capsule; broader source-page findings describe accumulated `6.41.0` behavior.

**Evidence:**

- Release manifest: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.0/2026-07-26/manifest.json`
- Release notes: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.0/2026-07-26/release-notes.md`
- Snapshot manifest: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/manifest.json`
- Card session guard: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Card/Card.tsx`
- 3DS2 challenge validation: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/ThreeDS2/components/Challenge/PrepareChallenge3DS2.tsx`
- Drop-in payment-method item: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/packages/lib/src/components/Dropin/components/PaymentMethod/PaymentMethodItem/PaymentMethodItem.tsx`

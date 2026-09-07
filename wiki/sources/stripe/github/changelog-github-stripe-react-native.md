---
title: "GitHub changelog: stripe/stripe-react-native"
type: source
date_ingested: 2026-07-30
date_updated: 2026-09-05
original_format: github-repo
raw_files:
  - "github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-09-01-a628bc0/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/manifest.json"
  - "github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/manifest.json"
  - "github-stripe-react-native.md"
tags: [stripe, react-native, mobile, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-react-native`. Cumulative implementation knowledge belongs in [[source-github-stripe-react-native]] and the linked immutable evidence.

## `@stripe/stripe-react-native@0.75.0` - Change Set `e0a845f` (2026-08-19)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@stripe/stripe-react-native` | `0.74.0` | `0.75.0` | 2026-08-19 | `e0a845f40749703480146c9d70721b9007d0516d` | Delta |

**Important changes:** Android Crypto Onramp gains Samsung Pay configuration, availability checking, payment collection, and example wiring. Five error discriminants are added: `InvalidWalletOwnershipSignatureError`, `WalletOwnershipChallengeExpiredError`, `InvalidWalletOwnershipChallengeError`, `WalletNotFoundError`, and `UnsupportedNetworkError`. Native pins advance Android `23.15.0--23.16.0` and iOS `26.6.0--26.7.0`.

**Developer or merchant impact:** Configure `samsungPay.serviceId`, check `isSamsungPaySupported()`, and collect with `collectPaymentMethod('SamsungPay', { samsungPay: { currencyCode, amount, orderNumber } })`. Amount uses minor units; order number must be unique. The app supplies Samsung Pay SDK `2.22.00` because Stripe does not bundle it. Enable the Android Onramp module. The iOS availability bridge returns false. This is Onramp-specific and does not establish ordinary PaymentSheet Samsung Pay support.

**Migration action:** Review exhaustive error and payment-display switches, retain generic error fallbacks, and test readiness, cancellation, token creation, and server/session checkout. The sample's fixed collection and session amounts differ; align real transaction amounts with server pricing. Wallet challenge APIs existed in `0.70.0`; this release adds narrower failure classification.

**Evidence boundary:** The release notes document the two feature groups; native version bumps come from build configuration. Complete Android Onramp implementation/setup files fall outside the retained capsule, although changed hunks are in the comparison. Deep Android runtime questions need full-file evidence. No native device checkout was executed. The GitHub release timestamp is August 19; the upstream changelog heading is August 18.

**Updated sections:** cumulative source/package status/native pins/Onramp/version history; React Native and Crypto Onramp concepts; company; provider index; logs. Existing historical sections remain.

**Evidence:**

- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.75.0/2026-09-01/manifest.json`
- `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.75.0/2026-09-01/release-notes.md`
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/manifest.json`
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.74.0--0.75.0/comparison.json`
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.74.0--0.75.0/comparison.md`
- `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.74.0--0.75.0/diff.patch`
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/src/types/Onramp.ts`
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/src/hooks/useOnramp.tsx`
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/ios/OnrampErrors.swift`
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/ios/StripeOnrampSdk.mm`
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/example/src/screens/Onramp/CryptoOnrampFlow.tsx`
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/android/gradle.properties`
- `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-e0a845f/files/stripe-react-native.podspec`

## `@stripe/stripe-react-native@0.74.0` — Change Set `a628bc0` (2026-08-12)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@stripe/stripe-react-native` | `0.73.0` | `0.74.0` | 2026-08-12 | `a628bc062f7018946d306e9e41b6ed5d75560cbc` | Delta |

**Important changes:** iOS Apple Pay parameters gain `supportedNetworks`, which restricts the networks offered for one request and overrides defaults plus `additionalEnabledNetworks`. Stripe iOS advances `26.5.0--26.6.0`, and Stripe Android advances `23.14.0--23.15.0`. The retained SHA also adds experimental Connect notification-banner and native external-link handling.

**Developer or merchant impact:** React Native applications can narrow the iOS Apple Pay sheet to selected networks. Invalid raw network strings are dropped by the native mapper. The Connect banner is not exported from the retained package root or `connect/Components` barrel, so it is not a supported public integration surface in this evidence.

**Migration action:** Use Apple-documented `PKPaymentNetwork` raw values, regression-test the rendered Apple Pay sheet, and verify the native wrapper upgrades on both platforms. Do not depend on the experimental Connect banner until Stripe publishes and exports it as a supported API.

**Evidence boundary:** The release note establishes only Apple Pay `supportedNetworks`. Override semantics, invalid-string handling, native dependency pins, and experimental Connect implementation come from the exact retained source comparison. They do not independently establish merchant eligibility, hosted rollout, or every delegated native SDK behavior.

**Evidence:**

- Release manifest: `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.74.0/2026-09-01/manifest.json`
- Release notes: `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.74.0/2026-09-01/release-notes.md`
- Snapshot manifest: `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-a628bc0/manifest.json`
- Comparison manifest: `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.73.0--0.74.0/comparison.json`
- Comparison narrative: `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.73.0--0.74.0/comparison.md`
- Exact patch: `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.73.0--0.74.0/diff.patch`
- Apple Pay type contract: `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-a628bc0/files/src/types/PlatformPay.ts`
- Apple Pay native mapping: `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-a628bc0/files/ios/ApplePayUtils.swift`
- Connect banner implementation: `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-a628bc0/files/src/components/NotificationBanner.tsx`

## `@stripe/stripe-react-native@0.73.0` — Change Set `8b1bc13` (2026-08-04)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@stripe/stripe-react-native` | `0.72.0` | `0.73.0` | 2026-08-04 | `8b1bc1370bd493baee8e692dbff54c973e311db2` | Delta |

**Important changes:** Stripe iOS advances `26.4.1--26.5.0`, Stripe Android advances `23.13.1--23.14.0`, private-preview Link Controller configuration gains billing-field collection and appearance controls, and Crypto Onramp gains Tempo network typing. The implementation comparison also shows the iOS PaymentSheet and Embedded Payment Element bridges reading deferred-intent `captureMethod` from the nested `mode` object.

**Developer or merchant impact:** Link Controller preview integrations can configure billing collection and UI styling on both platforms. Deferred-intent iOS integrations should keep `captureMethod` inside `intentConfiguration.mode`; the corrected bridge now consumes that nested value. Tempo exposure is an SDK contract, not proof of merchant or regional availability.

**Migration action:** Keep the explicit Link SetupIntent confirmation introduced in `0.72.0`; optionally add billing collection or appearance configuration after confirming preview access. Regression-test Android `23.14.0`, iOS `26.5.0`, and manual/automatic-async deferred capture flows.

**Evidence boundary:** The release note establishes the native SDK upgrades, Link configuration additions, and Tempo support. The nested `captureMethod` correction comes from the exact retained implementation diff and is not stated in the release note. Native dependency bumps do not independently establish every behavior change inside `stripe-ios` or `stripe-android`.

**Evidence:**

- Release manifest: `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.73.0/2026-09-01/manifest.json`
- Release notes: `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.73.0/2026-09-01/release-notes.md`
- Snapshot manifest: `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/manifest.json`
- Comparison manifest: `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.72.0--0.73.0/comparison.json`
- Comparison narrative: `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.72.0--0.73.0/comparison.md`
- Exact patch: `tracking/github/repos/stripe/stripe-react-native/comparisons/stripe-react-native/0.72.0--0.73.0/diff.patch`
- Link configuration: `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/files/src/types/LinkController.ts`
- Link appearance: `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/files/src/types/LinkAppearance.ts`
- Onramp network types: `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/files/src/types/Onramp.ts`
- iOS PaymentSheet bridge: `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/files/ios/StripeSdkImpl+PaymentSheet.swift`
- iOS Embedded bridge: `raw/github/stripe/stripe-react-native/snapshots/2026-09-01-8b1bc13/files/ios/StripeSdkImpl+Embedded.swift`

## `@stripe/stripe-react-native@0.72.0` — Change Set `e752a71` (2026-07-27)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `@stripe/stripe-react-native` | Legacy retained `0.65.1` context | `0.72.0` | 2026-07-27 | `e752a71aec30a0ed88e605345cff3ad74053b623` | Full |

**Important change:** The exact release updates Stripe iOS SDK `26.3.0--26.4.1`, Stripe Android SDK `23.12.0--23.13.1`, and changes private-preview Link Controller SetupIntent handling. `presentLinkController` now selects the payment method without confirming the SetupIntent; the application explicitly calls `confirmLinkControllerSetupIntent` afterward.

**Developer or merchant impact:** Integrations using the private-preview Link controller must add the explicit confirmation step or their SetupIntent flow will stop after selection. All consumers should regression-test both platforms because the release updates both delegated native SDKs.

**Migration action:** After successful `presentLinkController`, call `confirmLinkControllerSetupIntent(clientSecret)`. Verify preview access, handle errors from selection and confirmation separately, and test against Android SDK `23.13.1` and iOS SDK `26.4.1`.

**Updated source sections:** evidence boundary; architecture; payment surfaces; Link Controller; Connect; onramp; components and hooks; platform requirements; version history; integration guidance; Stripe company; React Native concept; provider index.

**Evidence boundary:** The Link behavior and native SDK upgrades are the only changes attributable specifically to the exact `0.72.0` release note. The broader API and architecture findings describe the complete retained `0.72.0` baseline. No immutable automated comparison exists from the legacy `0.65.1` manual capsule.

**Evidence:**

- Release manifest: `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.72.0/2026-07-30/manifest.json`
- Release notes: `raw/github/stripe/stripe-react-native/releases/stripe-react-native/0.72.0/2026-07-30/release-notes.md`
- Snapshot manifest: `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/manifest.json`
- Package manifest: `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/package.json`
- Public exports: `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/src/index.tsx`
- Link hook: `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/src/hooks/useLinkController.tsx`
- Cumulative upstream history: `raw/github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/files/CHANGELOG.md`

## Accumulated `0.66.0--0.71.0` Context

The retained upstream changelog records the main milestones between the legacy and current capsules:

| Release range | Retained milestone |
| --- | --- |
| `0.66.0--0.70.0` | Crypto onramp compliance identifiers, typed errors, wallet-ownership APIs, Arbitrum, and payment-collection changes |
| `0.68.0` | Push-provisioning contract changes and wearable support |
| `0.69.0` | Connect Account Onboarding, Payments, and Payouts embedded components recorded as GA; standalone Link Controller private preview |
| `0.71.0` | Pay by Bank added to direct PaymentIntent and SetupIntent confirmation |

These entries provide release-history context, not a complete automated diff against `0.65.1`.

## Legacy `@stripe/stripe-react-native@0.65.1` Context (2026-05-13 review)

The pre-collector 14-file capsule established PaymentSheet, direct Intent functions, Platform Pay, Financial Connections, Radar, Connect, crypto onramp, card and address components, the app-store purchase boundary, and the Android SDK 36 requirement.

This context remains historically queryable. The `0.72.0` baseline extends the cumulative source page and does not erase the old findings.

**Evidence:**

- Legacy capsule pointer: `raw/github-stripe-react-native.md`
- Legacy retained files: `raw/github-stripe-react-native/`

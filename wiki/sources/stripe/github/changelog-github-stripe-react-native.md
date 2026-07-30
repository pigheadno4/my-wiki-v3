---
title: "GitHub changelog: stripe/stripe-react-native"
type: source
date_ingested: 2026-07-30
date_updated: 2026-07-30
original_format: github-repo
raw_files:
  - "github/stripe/stripe-react-native/snapshots/2026-07-30-e752a71/manifest.json"
  - "github-stripe-react-native.md"
tags: [stripe, react-native, mobile, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-react-native`. Cumulative implementation knowledge belongs in [[source-github-stripe-react-native]] and the linked immutable evidence.

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

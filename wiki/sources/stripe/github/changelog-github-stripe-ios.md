---
title: "GitHub changelog: stripe/stripe-ios"
type: source
date_ingested: 2026-07-31
date_updated: 2026-07-31
original_format: github-repo
raw_files:
  - "github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/manifest.json"
  - "github-stripe-ios.md"
tags: [stripe, ios, swift, mobile, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-ios`. Durable architecture and integration knowledge belongs in [[source-github-stripe-ios]] and the linked immutable evidence.

## `stripe-ios@26.4.1` - Change Set `d9252fd` (2026-07-24)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-ios` | Legacy retained `25.14.0` context | `26.4.1` | 2026-07-24 | `d9252fd0a4a6d369fa45bb06f74c4e818c914f91` | Full |

**Exact release change:** fixes an issue where some Alipay payments incorrectly reported failure after succeeding.

**Developer or merchant impact:** merchants using Alipay should upgrade before treating an SDK failure result as reliable for this affected path. The full baseline also exposes current PaymentSheet, Embedded Payment Element, Apple Pay, low-level payments, Connect, Identity, Financial Connections, Issuing, and Crypto Onramp contracts, but those broader findings are not attributed to this patch.

**Migration action:** no release-specific API migration is documented for `26.4.1`. Existing integrations should regression-test Alipay and retain server-side event verification. Applications moving from v25 to v26 must raise their deployment target to iOS 15 or stay on `25.17.0` for iOS 13 and 14.

**Updated source sections:** evidence boundary; package status; architecture; payment surfaces; completion boundary; Apple Pay; low-level APIs; specialized modules; requirements; version history; integration guidance; Stripe iOS concept; Stripe company; provider index.

**Evidence boundary:** there is no automated comparison from the legacy manual `25.14.0` capsule. The exact patch note is release-specific; other `25.15.0--26.4.0` milestones are cumulative changelog context.

**Evidence:**

- Release manifest: `raw/github/stripe/stripe-ios/releases/stripe-ios/26.4.1/2026-07-31/manifest.json`
- Release notes: `raw/github/stripe/stripe-ios/releases/stripe-ios/26.4.1/2026-07-31/release-notes.md`
- Snapshot manifest: `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/manifest.json`
- Migration guide: `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/MIGRATING.md`
- Cumulative upstream history: `raw/github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/files/CHANGELOG.md`

## Accumulated `25.15.0--26.4.0` Context

| Release | Retained milestone |
| --- | --- |
| `25.15.0` | Adds Onelink support |
| `25.16.0` | Adds saved-card art through Customer Sessions and fixes Japanese address handling |
| `25.17.0` | Adds Identity manual capture, rich Crypto Onramp errors, and renames `LinkPaymentController` to `InstantBankPaymentsController` |
| `26.0.0` | Raises the minimum deployment target to iOS 15 |
| `26.1.0` | Fixes Swift Package Manager and CustomerSheet issues and renames alpha attestation APIs |
| `26.2.0` | Revises alpha Crypto Onramp error contracts |
| `26.3.0` | Adds alpha wallet-ownership verification, private-preview standalone Link APIs, and public Connect Payments/Payouts components |
| `26.4.0` | Makes `STPAPIClient.betas` public and separates private-preview Link SetupIntent confirmation |

These entries are release-history context, not complete automated comparisons against the old manual capsule.

## Legacy `stripe-ios@25.14.0` Context (2026-05-13 review)

The legacy capsule established PaymentSheet, FlowController, Embedded Payment Element, CustomerSheet, Apple Pay, low-level Intent APIs, 3DS handling, localization, and the iOS 13 deployment floor. The `26.4.1` baseline extends those findings instead of replacing them.

**Evidence:**

- Legacy capsule pointer: `raw/github-stripe-ios.md`
- Legacy retained files: `raw/github-stripe-ios/`

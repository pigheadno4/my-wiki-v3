---
title: "GitHub changelog: stripe/stripe-android"
type: source
date_ingested: 2026-07-31
date_updated: 2026-07-31
original_format: github-repo
raw_files:
  - "github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/manifest.json"
  - "github-stripe-android.md"
tags: [stripe, android, kotlin, mobile, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-android`. Durable architecture and integration knowledge belongs in [[source-github-stripe-android]] and the linked immutable evidence.

## `stripe-android@23.13.1` - Change Set `dc874ce` (2026-07-24)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-android` | Legacy retained `23.8.0` context | `23.13.1` | 2026-07-24 | `dc874ce7c62dd433664ec4e312efeb9300c21795` | Full |

**Exact release change:** fixes an Alipay test-mode issue where the SDK could fail to reconcile and close out a payment.

**Developer or merchant impact:** teams testing Alipay should upgrade before relying on test-mode completion and reconciliation behavior. The full baseline also exposes the current builder-first PaymentSheet, direct Intent, Google Pay, Connect, Identity, Financial Connections, Crypto Onramp, messaging, and card-scan contracts, but those broader findings are not attributed to this patch.

**Migration action:** no release-specific API migration is documented for `23.13.1`. Existing integrations should run Alipay test flows and retain their server-side event and reconciliation checks. Applications moving from pre-v23 must also satisfy Android API 23, SDK 36, Gradle, AGP, Kotlin, and Compose requirements in `MIGRATING.md`.

**Updated source sections:** evidence boundary; package status; architecture; payment surfaces; Google Pay; specialized modules; requirements; version history; integration guidance; Stripe Android concept; Stripe company; provider index.

**Evidence boundary:** there is no automated comparison from the legacy manual `23.8.0` capsule. The exact patch note is release-specific; other `23.9.0--23.13.0` milestones are cumulative changelog context.

**Evidence:**

- Release manifest: `raw/github/stripe/stripe-android/releases/stripe-android/23.13.1/2026-07-31/manifest.json`
- Release notes: `raw/github/stripe/stripe-android/releases/stripe-android/23.13.1/2026-07-31/release-notes.md`
- Snapshot manifest: `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/manifest.json`
- Migration guide: `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/MIGRATING.md`
- Cumulative upstream history: `raw/github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/files/CHANGELOG.md`

## Accumulated `23.9.0--23.13.0` Context

| Release | Retained milestone |
| --- | --- |
| `23.9.2` | Richer payment/setup confirmation errors plus expanded Crypto Onramp diagnostics |
| `23.10.0` | Identity manual document capture and updated Crypto Onramp compliance identifiers |
| `23.11.0` | Renamed Crypto Onramp EU attestation APIs |
| `23.12.0` | Connect Payments and Payouts embedded components marked GA; standalone Link controller added in private preview |
| `23.13.0` | Localized declined-card errors from 3DS2; explicit post-selection Link SetupIntent confirmation |

These entries are release-history context, not complete automated comparisons against the old manual capsule.

## Legacy `stripe-android@23.8.0` Context (2026-05-13 review)

The legacy 10-file capsule established PaymentSheet, FlowController, CustomerSheet, Embedded Payment Element, low-level Intent APIs, Google Pay, 3DS2 customization, and Android/Compose requirements. The `23.13.1` baseline extends those findings instead of replacing them.

**Evidence:**

- Legacy capsule pointer: `raw/github-stripe-android.md`
- Legacy retained files: `raw/github-stripe-android/`

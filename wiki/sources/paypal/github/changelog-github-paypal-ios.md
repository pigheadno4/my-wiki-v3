---
title: "GitHub changelog: paypal/paypal-ios"
type: source
date_ingested: 2026-07-31
date_updated: 2026-07-31
original_format: github-repo
raw_files:
  - "github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/manifest.json"
  - "github-paypal-ios.md"
tags: [paypal, ios, swift, mobile, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `paypal/paypal-ios`. Durable architecture and integration guidance belongs in [[source-github-paypal-ios]].

## `paypal-ios@2.0.1` - Change Set `2008a6d` (2025-11-03)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `paypal-ios` | Legacy retained 1.x-era context | `2.0.1` | 2025-11-03 | `2008a6de7c00a2ae53c669932d5fb19674c35b1e` | Full |

**Exact release changes:** `PayPalWebCheckoutClient.start()` now recognizes `opType=cancel` in deep-link URLs, and `vault()` recognizes the cancellation path. Both changes fix issue 361.

**Developer or merchant impact:** buyer cancellation is returned through the v2 error result instead of being misread as another web-flow outcome. Integrations should handle `PayPalError.checkoutCanceledError` and `PayPalError.vaultCanceledError` distinctly from operational failures.

**Migration action:** applications upgrading from 1.x must replace checkout, PayPal vault, card approval, and card vault delegates with `Result<Success, CoreSDKError>` completion handlers or async/await. Cancellation delegate callbacks become domain errors. Public `CardError`, `PayPalError`, and `NetworkingError` values can be compared through equatable `CoreSDKError`.

**Updated source sections:** evidence boundary; package status; modules; v2 API model; card and vault flows; cancellation behavior; native funding-source boundary; buttons; fraud and privacy; historical v1 context; PayPal iOS and Vault concepts; PayPal company and provider indexes.

**Evidence boundary:** no automated comparison exists between the legacy manual SHA and `2.0.1`. The two cancellation fixes are exact `2.0.1` changes; the delegate-to-Result migration and other architecture are cumulative `2.0.0` and baseline context.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-ios/releases/paypal-ios/2.0.1/2026-07-31/manifest.json`
- Release notes: `raw/github/paypal/paypal-ios/releases/paypal-ios/2.0.1/2026-07-31/release-notes.md`
- Snapshot manifest: `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/manifest.json`
- Migration guide: `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/v2_MIGRATION_GUIDE.md`
- Cumulative upstream history: `raw/github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/files/CHANGELOG.md`

## `paypal-ios@2.0.0` - Accumulated Major-Version Context (2025-03-18)

Version 2 replaces `CardDelegate`, `CardVaultDelegate`, `PayPalWebCheckoutDelegate`, and `PayPalVaultDelegate` with completion handlers and Swift concurrency. GA completion handlers use `Result<Success, CoreSDKError>`. Cancellation becomes an error result; domain-specific error enums become public; and `CoreSDKError` becomes equatable.

This context is retained from the `2.0.1` cumulative changelog and migration guide. It is not a separately collected `2.0.0` release capsule.

## Historical Reviewed Context (2026-04-13 review)

The earlier SHA `600a97a5f69ea6f44db3cf2f8b631276fd0152d8` established the 1.x delegate model, `CardClient(config:)`, card vaulting, demo server orchestration, PaymentButtons, and the lowercase `.paylater` source case. The cumulative source keeps these findings under an explicit version 1 boundary.

**Evidence:**

- Legacy capsule pointer: `raw/github-paypal-ios.md`
- Legacy retained files: `raw/github-paypal-ios/`

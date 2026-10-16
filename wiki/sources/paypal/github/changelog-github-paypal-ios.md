---
title: "GitHub changelog: paypal/paypal-ios"
type: source
date_ingested: 2026-07-31
date_updated: 2026-10-16
original_format: github-repo
raw_files:
  - "github/paypal/paypal-ios/snapshots/2026-10-16-de98414/manifest.json"
  - "github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/manifest.json"
  - "github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/manifest.json"
  - "github/paypal/paypal-ios/snapshots/2026-07-31-2008a6d/manifest.json"
  - "github-paypal-ios.md"
tags: [paypal, ios, swift, mobile, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `paypal/paypal-ios`. Durable architecture and integration guidance belongs in [[source-github-paypal-ios]].

## `paypal-ios@3.1.1` - Change Set `de98414` (2026-10-08)

Comparison manifest: [3.1.0 to 3.1.1](tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/3.1.0--3.1.1/comparison.json).

**Boundary:** `paypal-ios@3.1.0` (`67e4a9635f8e3ff829221c6d64573590937d1a2f`) -> `paypal-ios@3.1.1` (`de98414f5cf74dc3db2239a4828b4760ef391d20`); approved **delta** on 2026-10-16, item `github-85652bd08413a3ffc568`. Nine changed retained files fully read, affected prior code read in preceding full cycle; 153 unchanged paths hash-verified. Generated manifests/inventories/duplicated diff mechanically verified under approval.

**Changes:** optional BN code flows from CoreConfig through the session API into encoded experimentation context; nil is explicit JSON null. Demo adds trimmed BN input, separate UserDefaults persistence and CoreConfigManager forwarding. Pod/analytics version advances; CardClient diff is whitespace-only, not a payment behavior change. iOS 16 and exact risk dependency remain.

**Impact/cautions:** no new payment or vault API, native Venmo support or automatic merchant enablement. BN forwarding is not verified attribution credit. Demo Clear leaves separately persisted BN state intact, and changing settings is not proof of updating existing clients. Earlier return-validation, action-error, funding-selector and server-finalization boundaries remain.

**Support/history:** later cumulative CHANGELOG marks `3.0.0` unsupported and points to `3.1.0`, moving original v3 descriptions under `3.1.0`. Preserve the original release records and exact source attribution below; add the later notice without erasing previously ingested knowledge.

**Updated sections:** `3.1.1` source delta and support notice, SDK/Vault concepts, company/catalog/logs. No cross-company comparison warranted, no runtime payment test, commit or push.

**Evidence:** [snapshot](raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/manifest.json), [release record](raw/github/paypal/paypal-ios/releases/paypal-ios/3.1.1/2026-10-16/manifest.json), [notes](raw/github/paypal/paypal-ios/releases/paypal-ios/3.1.1/2026-10-16/release-notes.md), [comparison](tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/3.1.0--3.1.1/comparison.md), [session API](raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/files/Sources/PayPalPayments/APIRequests/CreateShopperSessionAPI.swift), [cumulative changelog](raw/github/paypal/paypal-ios/snapshots/2026-10-16-de98414/files/CHANGELOG.md).

## `paypal-ios@3.1.0` - Change Set `67e4a96` (2026-08-28)

Comparison manifest: [3.0.0 to 3.1.0](tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/3.0.0--3.1.0/comparison.json).

**Boundary:** `paypal-ios@3.0.0` (`fc69f404fa68b2c7336a684296543a67e0e809d5`) -> `paypal-ios@3.1.0` (`67e4a9635f8e3ff829221c6d64573590937d1a2f`); user-approved **full override** on 2026-10-16, item `github-5cce6532a34ea07a94ef`. All 162 current source files read, including 151 unchanged files; eleven modified retained files. Generated evidence mechanically verified under approval.

**Changes and migration:** minimum iOS 14 -> 16 across README/SPM/podspec; vendored risk framework -> external `paypal/paypal-risk-ios` exact `5.6.0`, product/pod `PayPalRisk`. `userAction` now reaches session `paymentType` as CONTINUE/PAY/COMMIT. Local installed-app check is removed, request installed flag becomes optimistic true and analytics installed flag nil. Server eligibility and OS-open success still gate app switching; failed opening falls back to browser.

**Reconfirmed full baseline:** session prewarm and callback-based ID APIs, merchant ID, separate app/browser returns, card Result/async and 3DS, merchant-server capture/token exchange, no native Venmo. The absent invalid-action error, return-binding caution and funding-selector removal persist. Risk dependency internals/builds and payment outcomes are unverified.

**Updated sections:** added full `3.1.0` source baseline, requirements/dependency/routing history, SDK and Vault concepts, company/catalog/logs. Preserved v1/v2 and `3.0.0`; resolved hardcoded-PAY only for `3.1.0`, without erasing earlier findings. No cross-company comparison warranted.

**Evidence:** [snapshot](raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/manifest.json), [release record](raw/github/paypal/paypal-ios/releases/paypal-ios/3.1.0/2026-10-16/manifest.json), [notes](raw/github/paypal/paypal-ios/releases/paypal-ios/3.1.0/2026-10-16/release-notes.md), [comparison](tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/3.0.0--3.1.0/comparison.md), [session API](raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Sources/PayPalPayments/APIRequests/CreateShopperSessionAPI.swift), [Package.swift](raw/github/paypal/paypal-ios/snapshots/2026-10-16-67e4a96/files/Package.swift).

## `paypal-ios@3.0.0` - Change Set `fc69f40` (2026-08-19)

Comparison manifest: [2.0.1 to 3.0.0](tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/2.0.1--3.0.0/comparison.json).

**Later support notice:** the CHANGELOG collected with `3.1.1` marks `3.0.0` unsupported and recommends `3.1.0`. Original release/source findings remain below; later rearranged release notes do not change this exact-SHA history.

**Boundary:** `paypal-ios@2.0.1` (`2008a6de7c00a2ae53c669932d5fb19674c35b1e`) -> `paypal-ios@3.0.0` (`fc69f404fa68b2c7336a684296543a67e0e809d5`); approved **full** ingest on 2026-10-16, item `github-28bbeeaf63ba759b78ef`.

**Changes:** rename module/client/results/funding enum and CoreEnvironment; require merchant ID with optional BN configuration; add mandatory shopper-session prewarm and ID-based checkout/vault; remove old PayPal request and async entry points and legacy PatchCCO types; surface PayPal UpdateClientConfig failures; enrich unstructured networking errors. Public `PayPalSessionType` expresses checkout versus vault intent, not Android's token API. Funding enum remains lowercase `.paylater` with no Venmo.

**Integration impact:** retain the client, start a new prewarm per attempt, obtain order/setup-token IDs server-side, route app-return URLs separately from browser callbacks, and finish capture/authorization or payment-token exchange server-side. App-switch requires installed-app detection and server eligibility at this exact version. Card Result/async APIs remain. iOS minimum is 14 in this snapshot; binary/framework and app entitlement contents are not collected.

**Cautions:** selected userAction is not forwarded into the session request (default PAY); documented invalid-user-action error is absent. The public start no longer accepts a funding-source selector; legacy demo button input is unused. Internal return parsing does not bind host/scheme/order. Card UpdateClientConfig still logs/continues, and 3DS-attempt flags do not establish liability shift. The source records URL-builder and stale README/toolchain discrepancies without claiming reproduced payment failures.

**Reading and preservation:** all 162 current files plus assigned prior source/release evidence fully read; generated manifests/inventories/duplicated diff mechanically verified under user approval. Retained comparison: 31 added, 45 modified, 14 removed, 6 renamed, 80 unchanged. Existing v1/v2 knowledge remains. Updated v3 source baseline, SDK/Vault concepts, company/catalog/logs; no cross-company comparison warranted.

**Evidence:** [snapshot](raw/github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/manifest.json), [release record](raw/github/paypal/paypal-ios/releases/paypal-ios/3.0.0/2026-10-16/manifest.json), [original notes](raw/github/paypal/paypal-ios/releases/paypal-ios/3.0.0/2026-10-16/release-notes.md), [comparison](tracking/github/repos/paypal/paypal-ios/comparisons/paypal-ios/2.0.1--3.0.0/comparison.md), [client](raw/github/paypal/paypal-ios/snapshots/2026-10-16-fc69f40/files/Sources/PayPalPayments/PayPalClient.swift).

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

---
title: "GitHub changelog: stripe/stripe-ios"
type: source
date_ingested: 2026-07-31
date_updated: 2026-10-02
original_format: github-repo
raw_files:
  - "github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/manifest.json"
  - "github/stripe/stripe-ios/supplements/2026-10-02-9f0d5aa-8ad0f8dd/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/manifest.json"
  - "github/stripe/stripe-ios/supplements/2026-10-02-7037819-bd3ee3a4/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-7037819/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-841b697/manifest.json"
  - "github/stripe/stripe-ios/supplements/2026-09-30-841b697-f58a4b7c/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-8444041/manifest.json"
  - "github/stripe/stripe-ios/supplements/2026-09-30-8444041-bea35b75/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/manifest.json"
  - "github/stripe/stripe-ios/snapshots/2026-07-31-d9252fd/manifest.json"
  - "github-stripe-ios.md"
tags: [stripe, ios, swift, mobile, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-ios`. Durable architecture and integration knowledge belongs in [[source-github-stripe-ios]] and the linked immutable evidence.

## `stripe-ios@26.12.1` - Change Set `9f0d5aa` (2026-09-28)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-ios` | `stripe-ios@26.12.0` | `stripe-ios@26.12.1` | 2026-09-28 | `9f0d5aa20e6a690ff4d78b35c307f0fb88d6f36c` | Full additive, approved focused reading |

**Pix:** API bindings and announced PaymentSheet support; hosted-instructions redirect and polling require a PaymentSheet authentication context. Pending action/processing is not success. Explicit mandate data wins; PaymentIntent inference adds Pix for offSession future usage, while SetupIntent adds it to its inference list. These bindings do not establish every recurring/setup or eligibility scenario.

**Supplemental polling evidence:** no countdown, configured two-second interval, API expiry or a 24-hour fallback; polling begins after a five-second scheduled delay. Failure/non-success deadline completes canceled, not failed. The redirect-retrieval path also lacks the PayNow/PromptPay cancellation exemption for Pix, whose PollingBudget is nil. Still-pending Pix can reach canceled on return/dismissal. This is a code-path risk, not device reproduction or proof of no bank payment; server verification remains required.

**Consent:** Financial Connections callback/async overloads accept a Stripe-issued consent ID and actual acceptance timestamp. Preserve the timestamp across retries/reopening. Server evaluation controls whether the pane is skipped; the SDK does not validate the evidence. Old overloads do not clear stored consent on a reused sheet; use an explicit nil through a new overload to reset. no_eligible_accounts and session-context diagnostics remain announcement-only findings because event/host internals are excluded.

**Checkout and historical annotations:** new-method billing email is no longer filled from session.email; no-method customerData email remains. Earlier timeout/completion caveats still apply. CryptoOnramp post-auth failure forwards available Intent/error to an excluded helper. Later error-detail and file-upload SPI notes are inserted under 26.12.0, not proof of first implementation at its earlier SHA. All 2,171 prior changelog lines remain, with 13 insertions.

**Impact and migration:** custom STP polling conformers must change PaymentIntent-specific action parameters to shared STPPaymentHandlerActionParams. This incompatible SPI signature motivates full mode despite the patch version; it is not a general public merchant API break. Review reused consent and removed email-fallback assumptions; do not fulfill solely on SDK results. Eight podspecs retain iOS 15/Swift 5 declarations and establish no standalone Apple Pay change.

**Evidence boundary:** 276 current/275 prior retained files: one added, 22 modified, 253 unchanged, none removed. 6,623 upstream dispositions: 23 retained, 6,600 policy-excluded, not full semantic repository review. Approved focused reading covers changed content/affected prior code and all three supplemental files; unchanged history/inventories checked mechanically. Full effective list: 290 paths. Availability/form factories, current Checkout/Apple Pay internals, consent enforcement/event internals, generic poller/action mapping and CryptoOnramp helper internals remain gaps. No SDK/device/payment or eligibility testing.

**Updated sections:** existing iOS and Pix concepts first; cumulative source/status/history, this changelog, company catalog, provider index and logs. All older knowledge and source count preserved; no cross-company comparison.

**Evidence:**
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.12.1/2026-09-30/manifest.json` - package-qualified release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.12.1/2026-09-30/release-notes.md` - announcements
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-9f0d5aa/manifest.json` - snapshot
- `raw/github/stripe/stripe-ios/supplements/2026-10-02-9f0d5aa-8ad0f8dd/manifest.json` - approved consent and polling evidence
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.12.0--26.12.1/comparison.json` - comparison; adjacent comparison.md and diff.patch
- `tracking/github/repos/stripe/stripe-ios/evidence-attachments/github-722f2ffc82b5d6e5375c/attachment.json` - supplement attachment
- [[source-github-stripe-ios]] - durable findings and exact implementation locations

## `stripe-ios@26.12.0` - Change Set `bc51b33` (2026-09-22)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-ios` | `stripe-ios@26.11.0` | `stripe-ios@26.12.0` | 2026-09-22 (notes heading: 2026-09-21) | `bc51b3323a06c029c561474547910bff0db82fc8` | Full additive, approved focused reading |

**Retained changes:** alpha coordinator methods retrieve partner-terms requirements, skip unnecessary presentation and await declaration-ID acceptance through Link. Link adds STP terms UI methods and a shared HTML confirmation helper; errors propagate and cancellation does not accept. Identity adds secondary-button styling. SPM adds CryptoOnramp localization resources.

**Confirmation boundary:** Embedded/FlowController remove Checkout-specific queue wrappers, but ordinary update guards remain and shared PaymentSheet.confirm still rejects Checkout intents. Current outer Checkout/session implementation is excluded; older controller supplements do not establish current behavior. Do not infer unguarded Checkout payment execution.

**Announcements and migration:** release notes remove public CryptoOnramp Image exposure, including linkIconSquare; consumers of that alpha API must account for its removal without assuming a replacement. StripeCore additionalHeaders SPI and the card-scan funding-warning fix remain release-note evidence only. No general deployment-floor change or mandatory migration is established by the retained podspecs.

**Historical annotation:** card-program-name support for saved methods with CustomerSessions is newly inserted under 26.11.0. Preserve the later annotation, not an exact first-implementation claim. All 2,159 previous changelog lines remain with twelve insertions.

**Evidence boundary:** 275 files, 16 modified, 259 unchanged; 216 upstream dispositions (16 retained, 200 excluded). Approved full mode overrides generated delta for announced API incompatibility. Focused reading covers changed content/affected prior code; unchanged history and inventories checked mechanically. The effective full reading list has 284 paths. API serializers, HTML/Identity rendering, Image implementation, header handling, scanner and current Checkout internals remain gaps. No SDK/device/payment testing.

**Updated sections:** existing iOS concept first, cumulative source/status/history, this changelog, company catalog, provider index and logs. Older knowledge and source count preserved; no cross-company comparison.

**Evidence:**
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.12.0/2026-09-30/manifest.json` - release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.12.0/2026-09-30/release-notes.md` - announcements
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-bc51b33/manifest.json` - snapshot
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.11.0--26.12.0/comparison.json` - comparison; adjacent comparison.md and diff.patch
- [[source-github-stripe-ios]] - exact implementation evidence and durable findings

## `stripe-ios@26.11.0` - Change Set `7037819` (2026-09-14)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-ios` | `stripe-ios@26.10.0` | `stripe-ios@26.11.0` | 2026-09-14 | `70378192e4b345bd4283511e1f6a3151591ebecf` | Full additive, approved focused reading |

**Announcements and bindings:** Scalapay API bindings and PaymentSheet support; Welsh localization. The typed model/params and processing classification are retained; availability/form factories are not. These do not prove merchant eligibility or end-to-end payment support.

**Confirmation behavior:** Checkout SPI can build a no-payment-method flow before requiring a PaymentElement. The current supplemental controller reaches this path. Missing both Intent types no longer fails immediately. Completed polling sets session status in the nil-Intent branch; timeout can still yield SDK completion with an open session and unchanged payment status. No zero-amount guard establishes general free-order/subscription support. No runtime reproduction or settlement proof is claimed.

**Other changes:** PaymentIntent mandate inference removes Kakao Pay while retaining explicit-data precedence. Link walletButtonHidden documentation permits visibility for recognized users; its old shouldShowButton property is removed. Identity adds SPI primary-button styling. Removing the Checkout Apple Pay billing-configuration argument is not proof that wallet billing collection stops.

**Impact and migration:** preview consumers must handle the changed no-method/missing-Intent path and must not fulfill solely from SDK completion. Recheck Link UI assumptions against current implementation before relying on the documented returning-user behavior. No mandatory general migration or deployment-floor change appears in the retained release material.

**Historical annotation:** the current cumulative changelog adds Kakao Pay PaymentSheet support under 26.10.0, absent from that release's earlier retained notes. Preserve it as a retrospective annotation, not proof of the first implementation release. All 2,148 prior lines remain with eleven insertions.

**Evidence boundary:** 275 retained files: two added, 19 modified, 254 unchanged; one exact-SHA supplemental controller read fully. Full mode overrides the generated delta recommendation for broad confirmation changes. Approved focused reading covers changed content and affected prior code; unchanged history/inventories were checked mechanically. Request/API serialization, current poller, wallet context, Link consumers, availability/form factories and Identity rendering remain excluded. Supplemental controller observations are not all newly introduced in this release. No SDK/device/payment testing.

**Updated sections:** existing iOS concept first; cumulative source/status/history, this changelog, company catalog, provider index and logs. Older knowledge and source count preserved; no cross-company comparison.

**Evidence:**

- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.11.0/2026-09-30/manifest.json` - package-qualified release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.11.0/2026-09-30/release-notes.md` - announcements
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-7037819/manifest.json` - snapshot
- `raw/github/stripe/stripe-ios/supplements/2026-10-02-7037819-bd3ee3a4/manifest.json` - current controller supplement
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.10.0--26.11.0/comparison.json` - comparison; comparison.md and diff.patch accompany it
- `tracking/github/repos/stripe/stripe-ios/evidence-attachments/github-266fd96ba1fdc3d98b71/attachment.json` - attachment
- [[source-github-stripe-ios]] - exact implementation paths and durable findings

## `stripe-ios@26.10.0` - Change Set `e5778f6` (2026-09-09)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-ios` | `stripe-ios@26.9.0` | `stripe-ios@26.10.0` | 2026-09-09 (notes heading: 2026-09-08) | `e5778f68b39a298c4fcf920d2587e54bb020d8e4` | Bounded delta, approved focused reading |

**Announcements:** PaymentSheet support for Naver Pay, Korean cards, PAYCO and SeQura; Arabic (Saudi Arabia); alpha CryptoOnramp Canada SIN, Colombia NIT, Philippines TIN and `KycInfo.idType`. These are not merchant-eligibility or end-to-end implementation verification. Kakao Pay is not included in this PaymentSheet announcement.

**Retained implementation:** PaymentIntent inferred-mandate defaults remove Korean cards and Naver Pay, retain Kakao Pay and still honor explicit mandate data. SetupIntent is unchanged. A narrow Financial Connections helper prefers explicit/account Onelink without changing general Link-brand resolution. Identity adds SPI branding-header configuration, not consent bypass. Embedded initial restoration suppresses animation. The retained Apple Pay caller supplies `shippingAddressRequired: false` to a session-aware helper; excluded wallet internals prevent broader shipping claims.

**Impact and migration:** distinguish 26.9.0 bindings from 26.10.0 announced PaymentSheet support; do not apply PaymentIntent inference changes to SetupIntent. No mandatory general migration is stated in the retained release notes. Podspec changes are version-only. Verify merchant eligibility independently and preserve server-event fulfillment checks.

**Evidence boundary:** 273 retained files, 16 modified, 257 unchanged, no additions/removals. Changed content and affected prior code were read using the approved exception; inventories and unchanged history were checked mechanically. Older changelog history beginning at 26.9.0 is byte-identical. Availability/form factories, CryptoOnramp models, Identity UI/controllers, Link consumers, RowButton and current Checkout/Apple Pay internals remain excluded. Earlier supplements do not prove current behavior. No SDK/device/payment testing.

**Updated sections:** existing iOS concept first, cumulative source/status/history, this changelog, company catalog, provider index and logs. Older knowledge and source count retained; no cross-company comparison.

**Evidence:**

- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.10.0/2026-09-30/manifest.json` - package-qualified release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.10.0/2026-09-30/release-notes.md` - announcements
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-e5778f6/manifest.json` - snapshot
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.9.0--26.10.0/comparison.json` - comparison; comparison.md and diff.patch accompany it
- [[source-github-stripe-ios]] - exact implementation paths and durable findings

## `stripe-ios@26.9.0` - Change Set `841b697` (2026-08-31)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-ios` | `stripe-ios@26.8.0` | `stripe-ios@26.9.0` | 2026-08-31 | `841b697a9c45a97a36ade02d9184c7d11b927e82` | Full additive, approved focused reading |

**Announcement:** API bindings for Kakao Pay, Korean cards, Naver Pay, PAYCO and SeQura. Typed models/parameters do not establish merchant eligibility or complete PaymentSheet availability. Mandate inference adds the first three; processing alone is not a completed Intent for any of the five.

**Broader implementation:** Checkout shares request construction/confirmation, handles PaymentIntent before SetupIntent, rejects manual approval/orchestration and polls open sessions. Polling has a 30-second elapsed-time budget and HTTP 429 backoff, without verified backend timeout enforcement. Completed and timed-out outcomes can both reach client-side response reconstruction; completion is not settlement. Link routes returned Link options through its Checkout flow.

**Compatibility:** Checkout SPI renames `succeeded` to `completed`, makes Checkout-specific Embedded/FlowController creation internal and supports an optional PaymentElement. Shipping clear and currency-selector configuration change at the controller boundary. Ordinary public Intent-based creation remains. Several helpers gain MainActor isolation. Permission plumbing and internal Apple Pay contact-field helpers have explicit downstream evidence limits.

**Impact and migration:** SPI consumers must account for result/visibility changes; do not infer a generally available integration recipe. Keep server-event fulfillment checks. Preserve 26.8.0's opposite Intent precedence and old result as version-qualified history. No-payment-required save suppression is not verified in 26.9.0 because request serialization moved into excluded code. No deployment-floor change appears in retained podspec diffs.

**Evidence boundary:** 273 snapshot files, ten additions, 31 modifications, 232 unchanged; two supplemental files read fully. Full mode reflects broad confirmation behavior, overriding the generated delta recommendation with user approval. Focused reading covers changed/new retained implementation and affected prior code; inventories and unchanged history were checked mechanically. Four changelog lines were inserted and all 2,131 prior lines preserved. Current wallet internals, request serializer, poll decoder and delegated permission behavior remain gaps. No SDK build, runtime payment or eligibility verification.

**Updated sections:** existing iOS concept first, cumulative source/status/version history, this changelog, company catalog, provider index and logs. Older knowledge and source count retained; no cross-company comparison.

**Evidence:**

- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.9.0/2026-09-30/manifest.json` - package-qualified release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.9.0/2026-09-30/release-notes.md` - announcements
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-841b697/manifest.json` - snapshot
- `raw/github/stripe/stripe-ios/supplements/2026-09-30-841b697-f58a4b7c/manifest.json` - controller/poller evidence
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.8.0--26.9.0/comparison.json` - inventory; comparison.md and diff.patch accompany it
- `tracking/github/repos/stripe/stripe-ios/evidence-attachments/github-bbbff15398aa9f59171d/attachment.json` - attachment
- [[source-github-stripe-ios]] - exact implementation paths and durable findings

## `stripe-ios@26.8.0` - Change Set `8444041` (2026-08-24)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-ios` | `stripe-ios@26.7.0` | `stripe-ios@26.8.0` | 2026-08-24 | `844404116961cb66eb8d67253386b4d564c66e87` | Full additive, approved focused reading |

**Announcements:** FPX Agrobank, Bank of China and MBSB; preserved card-decline messages after 3DS; private-preview Link Financial Connections permission configuration.

**Broader retained implementation:** CheckoutController SPI introduces typed confirmation flows, guards pending/concurrent operations, commits returned sessions and maps results. The approved supplemental controller reaches this engine; Link completion without a returned session fails. The Apple Pay wrapper delegates to excluded CheckoutApplePayContext, so full wallet behavior remains unverified. Standard PaymentSheet confirmation still rejects Checkout sessions. Low-level Alipay currency/future-usage and Klarna token options do not imply automatic PaymentSheet forwarding.

**Impact and migration:** preserve server-event fulfillment checks. Preview callers must respect the CheckoutController SPI boundary and presenter requirements; do not derive a production integration recipe from internal signatures. The 26.6.0 always-canceled outer mapping remains historical; the exact first fixed release is unknown because the 26.7.0 outer controller was not retained. Podspec bumps do not change the deployment floor.

**Historical annotations:** the current changelog inserts Alipay and horizontal-layout Link notes under 26.7.0 and Klarna under 26.5.0. These labels are separate from implementation observed changing at this SHA boundary. All 2,118 previous lines survive, with 13 insertions.

**Evidence boundary:** 263 snapshot files: 30 modified, one added, 232 unchanged; two supplemental files read fully. The user approved full additive ingest with focused reading of changed retained content and affected prior code, mechanical inventory/hash checks and preservation of unchanged history. This is not a fresh full read of all unchanged implementation or a full-repository review. No SDK build, runtime payment or merchant eligibility verification.

**Updated sections:** existing iOS concept first, cumulative source baseline/status/history/raw links, this changelog, company catalog, provider index and logs. All prior knowledge retained; no new source count or cross-company comparison.

**Evidence:**

- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.8.0/2026-09-30/manifest.json` - release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.8.0/2026-09-30/release-notes.md` - announcements
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-8444041/manifest.json` - snapshot
- `raw/github/stripe/stripe-ios/supplements/2026-09-30-8444041-bea35b75/manifest.json` - approved supplement
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.7.0--26.8.0/comparison.json` - inventory; comparison.md and diff.patch accompany it
- `tracking/github/repos/stripe/stripe-ios/evidence-attachments/github-4ef7ad96d01f40cfff58/attachment.json` - immutable supplemental evidence linkage
- [[source-github-stripe-ios]] - exact source files and durable findings

## `stripe-ios@26.7.0` - Change Set `62c2070` (2026-08-17)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-ios` | `stripe-ios@26.6.0` | `stripe-ios@26.7.0` | 2026-08-17 | `62c2070c57f20b4d632b25fc62780841f8883cc8` | Delta, approved focused reading |

**Release and migration:** PaymentSheet adds a Financial Connections Lite dependency. Manual/Carthage integrations must embed its xcframework; CocoaPods/SPM need no extra action according to the retained migration guide. Release notes also announce internal-service autocomplete and Link's `walletButtonHidden` option.

**Retained implementation:** Link remains enabled with its button hidden; Embedded row construction and selection retention now use a button-visibility helper. CustomerSheet takes the autocomplete endpoint flag directly from Elements Session; the STP SPI configuration switch is removed. Vipps gains typed models, parameters and serialization, and its `processing` state is not treated as completed by the payment handler. Merchant eligibility and full delegated behavior are not established.

**Historical annotations:** newly inserted beta-header guidance under 26.6.0 and AddressElement dismissal notes under 26.5.0 are upstream retrospective annotations, not new 26.7.0 features. All 2,103 earlier changelog lines are preserved. Typed Vipps additions are observed between the retained SHAs; do not infer their presence in the older SHA from heading dates.

**Evidence boundary:** 262 current files, two added, 26 modified, 234 unchanged. Of 53 prior-only paths, three are upstream deletions, 21 upstream modifications lack current retained content, and 29 are not listed upstream. Current outer Checkout, Link visibility helper, autocomplete service and Lite implementation remain gaps. The unfinished Checkout finding remains specific to 26.6.0, neither confirmed nor resolved for this release. Changed retained source was read fully under the approved exception; manifests and unchanged history were checked mechanically. No SDK build, runtime payment or eligibility tests.

**Updated sections:** existing iOS concept first, cumulative source and changelog, company catalog, provider index and logs. All older version knowledge preserved; no new source or cross-company comparison.

**Evidence:**

- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.7.0/2026-09-30/manifest.json` - release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.7.0/2026-09-30/release-notes.md` - announcements
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-62c2070/manifest.json` - exact-SHA snapshot
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.6.0--26.7.0/comparison.json` - identities and inventory
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.6.0--26.7.0/diff.patch` - implementation differences and retrospective annotations
- [[source-github-stripe-ios]] - exact raw implementation paths and durable findings

## `stripe-ios@26.6.0` - Change Set `3410ff0` (2026-08-10)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-ios` | `stripe-ios@26.5.0` | `stripe-ios@26.6.0` | 2026-08-10 | `3410ff0853b66e5ade3e8763e99f3ddb5dd77bc3` | Full additive, approved focused reading |

**Release announcements:** MB WAY and Bizum support in PaymentSheet; private-preview LinkController reports a no-funding-sources error rather than silently falling back to card; alpha Crypto Onramp adds `deleteWalletAddress(walletId:)`.

**Retained implementation:** the authorization branches require PaymentSheet context and PaymentIntent action params, rejecting standalone contexts and SetupIntents. Preview Link `present` forwards selection errors, while internal collection/FlowController callbacks discard the added error argument. Wallet deletion uses a wallet ID and Link account information; its API implementation is excluded.

**Checkout architecture and warning:** confirmation moves from the removed PaymentSheet helper into Checkout helpers, and shared PaymentSheet confirmation rejects Checkout intents. At this SHA, outer `Checkout.confirm` commits a returned response but discards the internal result and returns canceled; its Apple Pay branch and Express Checkout/Shipping Address actions remain unfinished. This SPI is not a production integration recommendation, and its canceled result does not prove no payment occurred. Session commit now occurs after internal next-action handling rather than before it. SetupIntent dispatch still precedes PaymentIntent.

**Expanded evidence, not all new features:** newly retained session code defines `noPaymentRequired` by payment status and limits billing tax-region sync to automatic tax using billing. Of 55 capsule additions, seven are upstream additions, ten upstream modifications, and 38 are not upstream changes. Preserve these as a 26.6.0 evidence baseline rather than assigning all behavior to this release.

**Other changes:** Package.swift and CustomerSheet remove JSON/form-spec loading; excluded replacement factories prevent a full UI-equivalence claim. Appearance defaults reference excluded helpers; FPX banks gain SPI CaseIterable. Podspecs only bump versions, without evidence of a deployment-floor or standalone Apple Pay integration change.

**Impact and migration:** independently verify payment-method eligibility. Preview users must handle errors, not just cancellation. Do not port Checkout confirmation based on unfinished SPI signatures alone. No mandatory general migration is stated in the retained release notes. SDK completion remains distinct from server-confirmed payment success.

**Evidence boundary:** full mode follows policy expansion and confirmation architecture, not the minor version number alone. Changed/newly retained implementation was read under the approved exception; unchanged files and 2,092 historical changelog lines were checked mechanically. Snapshot counts: 313 current, 259 prior; 55 added, 27 modified, one removed, 231 unchanged. Upstream inventory has 45 retained and 819 excluded changes. Excluded Link detection, availability/form/polling internals, alpha API requests, and appearance helpers remain limits. No SDK/runtime/payment or eligibility testing.

**Updated sections:** iOS concept first; cumulative source evidence boundary, status, Checkout qualification, new baseline, quotes/history/raw links; company, provider index and logs. Older versions and source count retained. No cross-company comparison.

**Evidence:**

- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.6.0/2026-09-30/manifest.json` - release identity
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.6.0/2026-09-30/release-notes.md` - announcements
- `raw/github/stripe/stripe-ios/snapshots/2026-09-30-3410ff0/manifest.json` - exact-SHA capsule
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.5.0--26.6.0/comparison.json` - upstream inventory and identity
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.5.0--26.6.0/diff.patch` - selected-file implementation changes
- [[source-github-stripe-ios]] - exact implementation paths and durable findings

## `stripe-ios@26.5.0` - Change Set `a1ea788` (2026-08-03)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-ios` | `stripe-ios@26.4.1` | `stripe-ios@26.5.0` | 2026-08-03 | `a1ea788163dee511239e2cfefe27cad576f045d3` | Delta |

**Release announcements:** optional billing-details collection configuration for standalone Link and LinkAppearance customization through `LinkControllerPreview`, both private preview; Tempo wallet-address registration for alpha Crypto Onramp (release-note evidence only).

**Retained implementation changes:**

- Public billing-collection initializer accepts field/address modes, attaching defaults, and allowed countries. Standalone Link's nil override preserves its base configuration; internal `collectName` can subsequently force name collection.
- Embedded cancellation rebuilds the accepted form state. Checkout-backed saved-method selection waits for billing-address sync before notifying/completing; failure restores prior selection and displays an error.
- SwiftUI Embedded resolves presentation through the embedded view's own window. FlowController invokes snapshot restoration on cancellation and gates its Link wallet shortcut on Continue.
- Internal Checkout confirmation suppresses `save_payment_method` for `noPaymentRequired`, then dispatches the response's SetupIntent before PaymentIntent. This is not proof of public free-order or subscription support.
- CustomerSheet's new tax-collection flag is internal plumbing. Podspec bumps do not establish Apple Pay integration or platform-floor changes.

**Merchant/developer impact and migration:** no mandatory release-specific migration is documented. Preview Link users can configure billing collection and appearance; regression-test canceled form edits, saved-method sync failure, multi-window presentation, and canceled FlowController selection. The iOS 15 floor and server-event fulfillment boundary remain. Collection and separate SetupIntent confirmation predate this delta.

**Version attribution:** the newer cumulative changelog retrospectively inserts multi-scene Embedded presentation and Link default-selection notes under `26.4.1`, and a Connect first-dismissal callback note under `26.4.0`. The older retained snapshot lacks these annotations. Preserve upstream historical labels separately from implementation differences observed between the two retained SHAs; do not silently rewrite older evidence. The Connect implementation is excluded.

**Evidence boundary:** 22 retained files modified, 237 unchanged, no additions/removals. User-approved focused reading covered changed implementation/content fully, with manifests and unchanged changelog segments checked mechanically. Excluded restoration helpers, Checkout internals, Link UI internals, tax factory, and Crypto network/API code limit semantic claims. The automated empty `public_api_changes` array is not exhaustive Swift API analysis. No SDK build, simulator, runtime payment, or eligibility testing was performed.

**Updated sections:** cumulative source's evidence boundary, status, integration delta, grounding excerpts, version history and raw links; iOS concept; company catalog; provider index and logs. Historical source knowledge retained; no new source page or cross-company comparison.

**Evidence:**

- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.5.0/2026-09-29/manifest.json` - release record
- `raw/github/stripe/stripe-ios/releases/stripe-ios/26.5.0/2026-09-29/release-notes.md` - release announcements
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/manifest.json` - exact-SHA snapshot
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.4.1--26.5.0/comparison.json` - comparison identity and dispositions
- `tracking/github/repos/stripe/stripe-ios/comparisons/stripe-ios/26.4.1--26.5.0/diff.patch` - selected-file changes and retrospective changelog insertions
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Link/LinkController.swift` - Link configuration application
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElement+Internal.swift` - selection/sync caller
- `raw/github/stripe/stripe-ios/snapshots/2026-09-29-a1ea788/files/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+CheckoutSessionAPI.swift` - internal confirmation
- [[source-github-stripe-ios]] - additional exact source paths and durable behavior

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

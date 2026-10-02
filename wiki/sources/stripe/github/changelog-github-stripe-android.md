---
title: "GitHub changelog: stripe/stripe-android"
type: source
date_ingested: 2026-07-31
date_updated: 2026-10-02
original_format: github-repo
raw_files:
  - "github/stripe/stripe-android/snapshots/2026-09-29-a074a95/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-d47cf89/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-a95cc0e/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-f5e7f5c/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-c5f31a3/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-a8d0e74/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-03dc31c/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-09-29-f286cb8/manifest.json"
  - "github/stripe/stripe-android/snapshots/2026-07-31-dc874ce/manifest.json"
  - "github-stripe-android.md"
tags: [stripe, android, kotlin, mobile, sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `stripe/stripe-android`. Durable architecture and integration knowledge belongs in [[source-github-stripe-android]] and the linked immutable evidence.

## `stripe-android@23.21.0` - Change Set `a074a95` (2026-09-28)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-android` | `stripe-android@23.20.0` | `stripe-android@23.21.0` | 2026-09-28 | `a074a9500e14932f00ce9cef250a3c63940f9837` | Additive full override, approved focused reading |

**Changes:** host-owned ViewModel/SavedStateHandle callback identifiers replace the shared PaymentSheet default in affected constructor/builder paths. Embedded Payment Element announces preview API configuration; the retained example opts in and supplies a server-returned publishable key, while PaymentSheet's related setters remain library-group restricted. Financial Connections adds prior-collected-consent forwarding and announces no-eligible-accounts/telemetry error changes. Experimental Onramp adds authenticated conditional terms methods, callbacks and result declarations. MB WAY and mixed-PAN-length BIN fixes are announced; MB WAY enum declarations are retained.

**Impact/migration:** host-scoped callback wiring is not proof of per-instance isolation or restored callback delivery. Review generated public API references and custom CollectBankAccountLauncher implementers: removed/changed generated declarations and added abstract consent overloads carry compatibility risk. Preview credentials are not a general merchant PaymentSheet API or proof of tenant isolation. Consent forwarding does not establish consent-screen skipping; Onramp acceptance does not establish checkout completion. Routing, error, terms enforcement and other excluded internals remain evidence gaps.

**Historical attribution:** current CHANGELOG adds Identity background-color notes under 23.20.0 and terms-method notes under 23.19.0, and moves the KYC note from 23.17.1 to 23.18.0. Preserve prior raw/wiki history; these labels do not override the observed retained API boundaries. The 4,823-line prior changelog becomes 4,843 lines with 23 insertions and three moved/deleted lines, not insert-only preservation.

**Scope/updated:** twelve modified/40 unchanged retained files per 52-file capsule; 104 matching hashes and 757 classified upstream dispositions. Effective full inventory checked under the approved focused-reading exception: changed implementation/content, affected declarations and prior context read; unchanged source/history and inventories checked mechanically. Android/Onramp concepts first, cumulative source/changelog/company/index/logs; older knowledge and source count retained. No extra collection, build/device/payment testing, commit or push.

**Evidence:**
- `raw/github/stripe/stripe-android/releases/stripe-android/23.21.0/2026-09-29/manifest.json`
- `raw/github/stripe/stripe-android/releases/stripe-android/23.21.0/2026-09-29/release-notes.md`
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a074a95/manifest.json`
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.20.0--23.21.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-stripe-android]] - contracts, grounding excerpts, example and exact raw paths

## `stripe-android@23.20.0` - Change Set `d47cf89` (2026-09-21)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-android` | `stripe-android@23.19.0` | `stripe-android@23.20.0` | 2026-09-21 | `d47cf89930d90601526f74eb6d6ab66b8fdc7e83` | Delta, approved focused reading |

**Changes:** Bizum PaymentSheet announcement and observed Bizum/AwaitAuthorization enum additions; Alipay+ and Alipay SDK redirect fix announcement. GooglePayLauncher now explicitly supplies GooglePayConfig(context) to repository factories in four host paths while keeping readiness/currency gates. Generated NFC accessor and test-only Financial Connections Compose dependency added.

**Impact/migration:** review exhaustive enum switches; test enabled Bizum, Alipay and Google Pay paths. Declarations do not establish eligibility or authorization timing. GooglePayConfig/repository and Bizum/Alipay implementation remain excluded; no new merchant launcher call or key/account/tokenization behavior is inferred. Earlier floors/contracts/history retained.

**Scope/updated:** eight modified/44 unchanged files in each 52-file capsule; all 104 hashes match, 712 upstream dispositions. Complete current/prior launcher and changed short content/declaration blocks reviewed; inventories/history mechanically checked. All 4,815 prior changelog lines remain with eight insertions. Android concept first, source/changelog/company/index/logs; source count unchanged. No extra collection, build/device/payment testing, commit or push.

**Evidence:**
- `raw/github/stripe/stripe-android/releases/stripe-android/23.20.0/2026-09-29/manifest.json`
- `raw/github/stripe/stripe-android/releases/stripe-android/23.20.0/2026-09-29/release-notes.md`
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-d47cf89/manifest.json`
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.19.0--23.20.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-stripe-android]] - contracts, exact raw paths and limitations

## `stripe-android@23.19.0` - Change Set `a95cc0e` (2026-09-15)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-android` | `stripe-android@23.18.0` | `stripe-android@23.19.0` | 2026-09-15 | `a95cc0edd5154f91251fe3881c7c943048c6399c` | Full override, approved focused reading |

**Changes:** WalletButtonHidden documentation now permits a visible Link entry for detected existing users while keeping automatic verification/inline sign-up enabled. Internal shouldShowButton getter removed; shouldDisplay remains true and public compiled inventories unchanged. Release notes announce Welsh/Arabic localization and a half-visible-sheet race fix. Gradle enables optimized resource shrinking.

**Impact/migration:** do not rely on the enum name for unconditional button hiding; test existing/new/account-switch cases. Earlier always-hidden contract remains version-qualified, not deleted. Link detection/rendering, translations/RTL and race-fix internals are excluded; no runtime guarantees. README lists Welsh but omits Arabic without disproving its release announcement. Shrinking setting is not app-size/build/device proof.

**Scope/updated:** 52 files per capsule, five modified/47 unchanged, 104 matching hashes, 942 upstream dispositions. Explicit full override with focused reading; complete affected current/prior LinkConfiguration blocks and changed short content reviewed; unchanged expanded inventory/history checked mechanically. All 4,806 prior changelog lines remain with nine insertions. Android/Link concepts first, source/changelog/company/index/logs; older knowledge/count retained. No extra collection, build/device/payment tests, commit or push.

**Evidence:**
- `raw/github/stripe/stripe-android/releases/stripe-android/23.19.0/2026-09-29/manifest.json`
- `raw/github/stripe/stripe-android/releases/stripe-android/23.19.0/2026-09-29/release-notes.md`
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a95cc0e/manifest.json`
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.18.0--23.19.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-stripe-android]] - old/new contract distinction and exact raw links

## `stripe-android@23.18.0` - Change Set `f5e7f5c` (2026-09-08)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-android` | `stripe-android@23.17.1` | `stripe-android@23.18.0` | 2026-09-08 | `f5e7f5ceb26a194f38a561c8c687265ef5fcc16d` | Full override, approved focused reading |

**Changes:** PaymentSheet announces six methods (SeQura, PAYCO, Korean cards, Naver Pay, Kakao Pay, Scalapay); compiled API adds corresponding type/creation declarations. AddressElement announces Stripe-hosted autocomplete by default. Onramp adds IdType/KycInfo declarations. Identity adds library-group-restricted biometric consent header configuration; Play Services Wallet dependency advances to 20.0.0.

**Impact/migration:** review exhaustive method/IdType switches and test applicable address/payment flows. Signatures do not establish eligibility, serialization, defaults, mandate handling or complete integration recipes. Earlier keyless migration and scoped module floors remain intact; restricted Identity controls are not general merchant APIs. Root build change removes a test exclusion, not a runtime feature.

**Historical attribution:** the new changelog places KYC types under 23.17.1 retrospectively, absent from that retained release's API/notes. Preserve the label separately from the observed 23.17.1 -> 23.18.0 declaration boundary. All 4,790 prior changelog lines remain with sixteen insertions.

**Scope/updated:** 52 files per capsule, nine modified/43 unchanged; 104 matching hashes, 954 upstream dispositions. Approved full mode with focused reading: changed source/declarations/context and prior affected evidence reviewed; unchanged inventory/history checked mechanically. Android/Onramp/BNPL/Korean-method concepts first, source/changelog, company/index/logs; older knowledge/count preserved. PaymentSheet, autocomplete and KYC request internals excluded. No extra collection, build/device/payment tests, commit or push.

**Evidence:**
- `raw/github/stripe/stripe-android/releases/stripe-android/23.18.0/2026-09-29/manifest.json`
- `raw/github/stripe/stripe-android/releases/stripe-android/23.18.0/2026-09-29/release-notes.md`
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f5e7f5c/manifest.json`
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.17.1--23.18.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-stripe-android]] - declarations, restricted contract and limitations

## `stripe-android@23.17.1` - Change Set `c5f31a3` (2026-08-31)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-android` | `stripe-android@23.17.0` | `stripe-android@23.17.1` | 2026-08-31 | `c5f31a3043aaafe2904441d59619a4f2c8c40291` | Full override, approved focused reading |

**Changes:** announced Klarna billing-country refresh, Wero duplicate-country and Link 2FA Not you? logout fixes. Their implementation remains excluded. Compiled PaymentSheet removes the generated public StripeGooglePayButtonBinding class; Identity adds a generated top-app-bar accessor.

**Impact/migration:** direct binding references have source/binary compatibility risk; the removal does not establish removal of Google Pay and generated classes should not be treated as supported merchant integration APIs. Regression-test the announced address/account-switch fixes. Earlier module floors, keyless migration and Identity contracts remain version-qualified. All 4,783 prior changelog lines remain with seven new lines.

**Scope/updated:** 52 files per capsule, six modified/46 unchanged, 104 matching hashes, 263 upstream dispositions. Explicit full override with focused reading; changed short content/API class context and prior removed declaration reviewed, unchanged full inventory/history mechanically checked. Android concept first, cumulative source/changelog, company/index/logs; old knowledge/count retained. No extra collection, runtime tests, commit or push.

**Evidence:**
- `raw/github/stripe/stripe-android/releases/stripe-android/23.17.1/2026-09-29/manifest.json`
- `raw/github/stripe/stripe-android/releases/stripe-android/23.17.1/2026-09-29/release-notes.md`
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-c5f31a3/manifest.json`
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.17.0--23.17.1/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-stripe-android]] - prior declaration, current boundary and limitations

## `stripe-android@23.17.0` - Change Set `93ef69a` (2026-08-24)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-android` | `stripe-android@23.16.0` | `stripe-android@23.17.0` | 2026-08-24 | `93ef69a77a4fa528db4a5e95714394c4dcb2463c` | Full override, approved focused reading |

**Changes/impact:** keyless-autocomplete migration deprecates Google Places configuration without removing existing setters; Identity adds optional brandColor, preserving one-argument construction but changing compiled copy/default-copy signatures. Recompile callers. Identity/Onramp production builds require API 24, not every SDK module; Identity adds MediaPipe Tasks Vision 0.10.35. Alipay SetupIntent/direct API and supported-session guided 3D selfie capture are release announcements with implementation gaps.

**Migration/history:** remove Places key call/argument as directed by MIGRATING.md and test address collection; review app floor for affected modules and dependent binaries. New cumulative changelog labels API 24 under 23.15.0 retrospectively; preserve that later label separately from the observed 23.16.0 -> 23.17.0 build change. All 4,769 prior changelog lines remain with 14 insertions; prior migration content remains with five insertions.

**Scope/updated:** 52 files per capsule, 12 modified/40 unchanged, 104 verified hashes and 762 upstream dispositions. Full override approved, effective expanded inventory checked under the focused-reading exception. Changed source/API/build/migration context and affected prior code reviewed; unchanged history carried forward mechanically. Android/Onramp concepts first, cumulative source/history, company/index/logs; source count and old knowledge retained. No extra collection, build/device/payment tests, commit or push.

**Evidence:**
- `raw/github/stripe/stripe-android/releases/stripe-android/23.17.0/2026-09-29/manifest.json`
- `raw/github/stripe/stripe-android/releases/stripe-android/23.17.0/2026-09-29/release-notes.md`
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-93ef69a/manifest.json`
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.16.0--23.17.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-stripe-android]] - contracts, compatibility and exact raw paths

## `stripe-android@23.16.0` - Change Set `a8d0e74` (2026-08-18)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-android` | `stripe-android@23.15.0` | `stripe-android@23.16.0` | 2026-08-18 | `a8d0e742fa6eb7ba637ce9968d03ce5b4c75dbf0` | Full override, approved focused reading |

**Changes:** Link WalletButtonHidden keeps Link enabled while hiding its button, with returning-user/inline-signup contract retained; authenticated Onramp deleteWalletAddress delegates by wallet ID and exposes Completed/Failed result signatures. Release notes announce default inline address autocomplete across PaymentSheet, FlowController and AddressElement; underlying implementation remains excluded.

**Impact/migration:** hiding Link is not disabling it. Review enum switches and regression-test address collection; do not infer removed Places prerequisites. Onramp deletion requires authenticated Link context by contract; request authorization, propagation, idempotency and retries are unverified. README platform floors are unchanged; build additions are test-only.

**Historical attribution:** the new changelog also inserts autocomplete announcements under 23.15.0, absent from that earlier retained release evidence. Preserve the later label without claiming a proven first implementation release. All 4,753 prior changelog lines survive with 16 insertions.

**Scope/updated:** additive full mode explicitly approved for broad announced defaults; focused reading covers changed implementation/declarations and affected prior context, unchanged evidence mechanically verified. 52 files per capsule, ten modified/42 unchanged, 104 matching hashes, 577 upstream dispositions. Android/Onramp concepts first, cumulative source/history, company/index/logs; all older knowledge retained. No extra collection, build/device/payment tests, commit or push.

**Evidence:**
- `raw/github/stripe/stripe-android/releases/stripe-android/23.16.0/2026-09-29/manifest.json`
- `raw/github/stripe/stripe-android/releases/stripe-android/23.16.0/2026-09-29/release-notes.md`
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-a8d0e74/manifest.json`
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.15.0--23.16.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-stripe-android]] - exact implementation context, signatures and limitations

## `stripe-android@23.15.0` - Change Set `03dc31c` (2026-08-10)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-android` | `stripe-android@23.14.0` | `stripe-android@23.15.0` | 2026-08-10 | `03dc31c4dad8d94f08153e87b9782095fdb8036f` | Delta, approved focused reading |

**Changes:** optional Crypto Onramp Samsung Pay declarations: configuration/readiness, selection/display, availability and typed errors. App must provide Samsung Pay SDK. Signature-only evidence does not establish parameter meanings/defaults, SDK version compatibility, readiness/credential/error mapping or ordinary PaymentSheet support. Release-note-only Link no-funding-sources fix and three FPX banks/alphabetic ordering remain explicit implementation gaps.

**Impact/migration:** Onramp integrators must supply the optional wallet SDK and handle new availability/error/enum variants without equating collection with checkout or settlement. No mandatory general merchant migration or minimum Android change is established. Build changes are test tooling/device configuration, not proof of execution. All 4,744 prior changelog lines survive with nine insertions.

**Scope:** 52 files, seven modified/45 unchanged, 545 upstream dispositions; approved focused reading, both retained capsules hash-verified. No SDK/device/payment or eligibility testing. Updated Android/Onramp concepts first, cumulative source/changelog, company/index and logs; older knowledge/source count retained.

**Evidence:**
- `raw/github/stripe/stripe-android/releases/stripe-android/23.15.0/2026-09-29/manifest.json`
- `raw/github/stripe/stripe-android/releases/stripe-android/23.15.0/2026-09-29/release-notes.md`
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-03dc31c/manifest.json`
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.14.0--23.15.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-stripe-android]] - exact declarations and limitations

## `stripe-android@23.14.0` - Change Set `f286cb8` (2026-08-03)

| Package | From | To | Release date | SHA | Ingest mode |
| --- | --- | --- | --- | --- | --- |
| `stripe-android` | `stripe-android@23.13.1` | `stripe-android@23.14.0` | 2026-08-03 | `f286cb86cdd9be1b90913c12a7194ce04758de12` | Delta, approved focused reading |

**Changes/impact:** private-preview Link appearance contracts and billing-collection configuration setter; CryptoNetwork.Tempo declaration and announced internal preview API-version pinning. Signatures establish callable surfaces, not defaults, rendering, serialization or merchant eligibility. No general migration or deployment-floor change is established; preview users should check styling/collection assumptions and retain payment-event fulfillment gates.

**Historical annotation:** billingDetailsCollectionConfiguration is inserted under 23.13.1 in the newer changelog, absent from the earlier retained API/notes. Preserve that later attribution rather than retroactively changing old evidence. All 4,733 prior changelog lines survive with eleven insertions.

**Scope:** 52 files, six modified/46 unchanged; 337 upstream dispositions. Approved focused reading includes changed declarations/enclosing blocks and affected prior code; unchanged history/inventories mechanically checked. Link UI/billing, Onramp request/network and current Checkout/Google Pay internals remain excluded. No build/device/payment tests.

**Updated:** Android and Crypto Onramp concepts first; cumulative source/status/history, changelog, company/catalog/index and logs. Older knowledge/source count unchanged; no comparison page.

**Evidence:**
- `raw/github/stripe/stripe-android/releases/stripe-android/23.14.0/2026-09-29/manifest.json`
- `raw/github/stripe/stripe-android/releases/stripe-android/23.14.0/2026-09-29/release-notes.md`
- `raw/github/stripe/stripe-android/snapshots/2026-09-29-f286cb8/manifest.json`
- `tracking/github/repos/stripe/stripe-android/comparisons/stripe-android/23.13.1--23.14.0/comparison.json` - adjacent comparison.md/diff.patch
- [[source-github-stripe-android]] - durable contracts, quotes and exact API evidence

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

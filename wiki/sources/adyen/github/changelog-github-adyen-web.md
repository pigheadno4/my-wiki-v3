---
title: "GitHub changelog: Adyen/adyen-web"
type: source
date_ingested: 2026-07-26
date_updated: 2026-09-15
original_format: github-repo
raw_files:
  - "github/adyen/adyen-web/snapshots/2026-09-14-b29934f/manifest.json"
  - "github/adyen/adyen-web/supplements/2026-09-14-b29934f-d296b082/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-09-14-f10995d/manifest.json"
  - "github/adyen/adyen-web/supplements/2026-09-14-f10995d-55e9e1ba/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-09-14-b989173/manifest.json"
  - "github/adyen/adyen-web/supplements/2026-09-14-b989173-20c08eb4/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-08-09-1e157f8/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-08-09-c98ea8a/manifest.json"
  - "github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/manifest.json"
tags: [adyen, checkout, web-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-web`. Cumulative implementation knowledge belongs in [[source-github-adyen-web]] and the linked immutable snapshots.

## `@adyen/adyen-web@6.45.0` (2026-09-10)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@adyen/adyen-web` | `6.44.0` | `6.45.0` | `b29934f6cf5de6e1912039f669b48ae45b75d3fd` | Full, additive |

**Important findings:** opt-in review-page checkout introduces `onReview`, `onAction`, and Sessions-only `processPayment`. Supported submit paths validate and return review data before payment; final confirmation and action presentation become merchant responsibilities. Payment-method exceptions, gift-card partial payments, and branch-specific PayByBankPix behavior prevent treating this as a universal review flow. Donation amount gains a checkout fallback; Google Pay gains nonce forwarding; address validation permits ordinary punctuation while rejecting invalid characters; Drop-in avoids repeated payment-method rendering. Select receives spacing/color adjustments.

**Dependencies:** PayPal JS 10.0.3 to 10.1.0, Preact 10.29.7 to 10.29.8, Google Pay types 0.7.11 to 0.7.12. These are independently versioned dependencies, not proof of delegated runtime behavior.

**Migration:** `processPayment` returns void and does not repeat Component validation or `beforeSubmit`. Preserve transformations, prevent repeated/stale confirmation, mount/dispose actions, and implement errors plus remaining-order handling. Advanced integrations retain their backend payment path. `onAction` also changes ordinary mounted UIElement response handling. The stories demonstrate intent but print the full payment payload and omit production recovery/cleanup; do not copy those omissions. Recheck address validation, Google Pay CSP setup and custom Select styling.

> [!warning] Contradiction
> Retained ADRs lag code: response types already include `askDonation`; `processPayment` calls `onOrderUpdated` without the described `core.update`; PayByBankPix exclusion depends on its branch. The cumulative source and [[adyen-review-page-checkout]] record the implementation-qualified interpretation.

**Mode and updated pages:** user-approved full ingest reflects the new cross-component lifecycle. The generated security signal is CSP, not a confirmed vulnerability. Added the 6.45.0 source section, five exact-code grounding excerpts, review-page concept, company/index/log updates; preserved all older sections and kept source count unchanged.

**Evidence boundary:** serial reading of the assigned packet, comparison and 26-file exact-SHA supplement, including two ADRs and three stories. Standard capsule: 221 files, 13 modified and 208 unchanged. No upstream test, browser, payment, screen-reader or delegated runtime validation. Full does not mean every upstream file was retained.

**Evidence:**

- [Snapshot](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-b29934f/manifest.json)
- [Supplement](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b29934f-d296b082/manifest.json)
- [Release identity](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.45.0/2026-09-14/manifest.json)
- [Release notes](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.45.0/2026-09-14/release-notes.md)
- [Comparison](../../../../tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.44.0--6.45.0/comparison.json)
- [[source-github-adyen-web]] - implementation details and grounding

## `@adyen/adyen-web@6.44.0` (2026-08-19)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@adyen/adyen-web` | `6.43.0` | `6.44.0` | `f10995d33491d8107c01a27dec2bc1fc4d6e28b0` | Delta |

**Important findings:** shared keyboard dispatch moves to keydown while retaining `onEnterKeyPressed`; nested controls isolate action keys and dual-brand selection retains native button activation. CVC error keys gain Amex-specific resolution; release notes report expiry/CVC format guidance in error states. Form defaults tolerate null inputs, and CardInput normalizes partial-address country to uppercase. Loading, final QR status, card error clearing, and repeated screen-reader messages gain targeted lifecycle fixes.

**Dependencies:** Preact 10.29.2 to 10.29.7; Secured Fields constant 6.2.1 to 6.3.0. PayPal JS remains 10.0.3. The changed 3DS2 files are formatting-only, not a new passkey feature.

**Merchant/developer impact and migration:** recheck Enter-key callbacks, nested controls, Amex custom translations, null form initialization, lowercase country values, and assistive announcements. Required validation remains in place. No incompatible top-level export or broad checkout architecture change was established.

**Updated source sections:** overview/evidence boundary, additive 6.44.0 behavior and grounding excerpts, raw links; co-badged-cards keyboard evidence; company/index/logs. Earlier releases remain intact; source count is unchanged. No new concept, cross-company comparison, or contradiction entry was warranted.

**Mode decision:** the generated full/high recommendation remains unchanged. Its security keyword matched "security code" (CVC), not evidence of a vulnerability. The user approved delta after review of the assigned current source and 40-file supplement bounded the changes.

**Evidence boundary:** the 221-file standard capsule has 24 modified, one added, and 196 unchanged files; the supplement retains 40 files. Translation JSONs and the external Secured Fields runtime were not audited. Standalone tests were excluded; diff test excerpts are not executed proof. No browser, screen-reader, or payment runtime verification was performed.

**Evidence:**

- [Snapshot](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-f10995d/manifest.json)
- [Supplement](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-f10995d-55e9e1ba/manifest.json)
- [Release identity](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.44.0/2026-09-14/manifest.json)
- [Release notes](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.44.0/2026-09-14/release-notes.md)
- [Comparison](../../../../tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.43.0--6.44.0/comparison.json)
- [Source details and implementation links](source-github-adyen-web.md)

## `@adyen/adyen-web@6.43.0` (2026-08-12)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@adyen/adyen-web` | `6.42.0` | `6.43.0` | `b98917359c0b5b701ef99b583aef44f447e73bf6` | Delta |

**Important findings:** internal Select options gain tags with info/success variants. Supporting text moves below the option name and disappears from the collapsed control. Filterable wrapper clicks toggle the list while clicks on the open filter input keep it open. Long-name layout can shrink beside tags; the existing result-announcement region uses a dedicated visually-hidden class. The PayPal JS dependency changes from 10.0.2 to 10.0.3.

**Merchant/developer impact:** selected supporting text is no longer persistently visible, so recheck affected UX and custom CSS. Tags are literal presentation labels, not translated keys or payment eligibility/pricing logic. Internal Select/Tag types are not a new top-level merchant API.

**Migration action:** no breaking public export change is established. Recheck collapsed dropdown labels, long names, keyboard/read-only behavior, and custom styling. Consult the independent PayPal JS source for delegated dependency behavior.

**Updated source sections:** overview and evidence boundary, 6.43.0 grounding and minor-release behavior, immutable links; Adyen company/index/log. Previous versions remain intact. Concept audit found no new product or relevant concept change; no cross-company comparison or contradiction entry was warranted.

**Evidence boundary:** standard capsule has two modified package manifests and 218 unchanged files. The approved supplement adds 14 exact-SHA Select/Tag source/style files including three stories. Tests were not collected as standalone supplement files or executed; generated diff excerpts may contain upstream test changes. No browser, screen-reader, payment runtime, or delegated PayPal runtime test was performed.

**Evidence:**

- [Snapshot](../../../../raw/github/adyen/adyen-web/snapshots/2026-09-14-b989173/manifest.json)
- [Supplement](../../../../raw/github/adyen/adyen-web/supplements/2026-09-14-b989173-20c08eb4/manifest.json)
- [Release identity](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.43.0/2026-09-14/manifest.json)
- [Release notes](../../../../raw/github/adyen/adyen-web/releases/adyen-web/6.43.0/2026-09-14/release-notes.md)
- [Comparison](../../../../tracking/github/repos/adyen/adyen-web/comparisons/adyen-web/6.42.0--6.43.0/comparison.json)
- [Source details and exact implementation links](source-github-adyen-web.md)

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

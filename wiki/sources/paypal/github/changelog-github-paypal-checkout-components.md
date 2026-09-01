---
title: "GitHub changelog: paypal/paypal-checkout-components"
type: source
date_ingested: 2026-09-01
original_format: github-repo
raw_files:
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-01-9bb1162/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-01-1e6da34/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-01-a7b2d95/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-09-01-48d428c/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/manifest.json"
tags: [paypal, checkout, javascript-sdk, changelog, github-repository, venmo]
---

## Overview

Chronological release synthesis for `paypal/paypal-checkout-components`. Cumulative implementation knowledge belongs in [[source-github-paypal-checkout-components]] and the linked immutable snapshots.

## `@paypal/checkout-components@5.0.431` (2026-08-24)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/checkout-components` | `5.0.430` | `5.0.431` | `9bb1162373b4dd96d5a3196dbfab41990f606bb7` | Delta |

**Important findings:** The package version advances to `5.0.431`; the changelog records only `chore(release): 5.0.430`. Changed retained files are limited to the changelog, package manifest, and generated bundle. No authored source, public API export, or dependency range change is reported.

**Developer or merchant impact:** `5.0.431` carries forward the `5.0.429` restoration of the plain `PayPal` generic iframe title. No new merchant or runtime behavior is established.

**Migration action:** None documented.

**Updated source sections:** overview; evidence boundary; grounding excerpts; `5.0.431` release-only boundary; PayPal company and provider index version references.

**Evidence boundary:** Upstream release notes were unavailable. Generated-bundle churn is not used to infer a new capability when no authored source changed.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.431/2026-09-01/manifest.json`
- Snapshot manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-9bb1162/manifest.json`
- Comparison: `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.430--5.0.431/comparison.json`
- Changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-9bb1162/files/CHANGELOG.md`
- Package manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-9bb1162/files/package.json`

## `@paypal/checkout-components@5.0.430` (2026-08-24)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/checkout-components` | `5.0.429` | `5.0.430` | `1e6da3424d7bb5654bf4a2479702b521dc69aa01` | Delta |

**Important findings:** The package version advances to `5.0.430`; the changelog records only `chore(release): 5.0.429`. Changed retained files are limited to the changelog, package manifest, and generated bundle. No authored source, public API export, or dependency range change is reported.

**Developer or merchant impact:** `5.0.430` carries forward the `5.0.429` restoration of the plain `PayPal` generic iframe title. No new merchant or runtime behavior is established.

**Migration action:** None documented.

**Updated source sections:** overview; evidence boundary; grounding excerpts; `5.0.430` release-only boundary; PayPal company and provider index version references.

**Evidence boundary:** Upstream release notes were unavailable. Generated-bundle churn is not used to infer a new capability when no authored source changed.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.430/2026-09-01/manifest.json`
- Snapshot manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-1e6da34/manifest.json`
- Comparison: `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.429--5.0.430/comparison.json`
- Changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-1e6da34/files/CHANGELOG.md`
- Package manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-1e6da34/files/package.json`

## `@paypal/checkout-components@5.0.429` (2026-08-24)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/checkout-components` | `5.0.428` | `5.0.429` | `a7b2d958ce0510951a811e5c152181fd16d1512a` | Delta |

**Important findings:** This release completely reverts the `5.0.428` screen-reader title change. A no-funding-source Buttons iframe is again titled plain `PayPal`, while funding-specific titles remain `PayPal-<fundingSource>`. No public API export or dependency range changes are reported.

**Developer or merchant impact:** The distinct `PayPal Payment Buttons` generic title exists only in `5.0.428`; it must not be assumed for `5.0.429`. The source does not explain why the accessibility fix was reverted or identify a replacement mitigation.

**Migration action:** No merchant API action is documented. Accessibility validation should be version-specific, especially for deployments moving from `5.0.428` to `5.0.429`.

**Updated source sections:** overview; evidence boundary; grounding excerpts; `5.0.429` accessibility fix revert; PayPal Checkout concept; PayPal company and provider index version references.

**Evidence boundary:** Upstream release notes were unavailable. The changelog proves the explicit revert and the source diff proves exact restoration of the prior title expression; affected screen readers, browsers, and rollback rationale remain undocumented.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.429/2026-09-01/manifest.json`
- Snapshot manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-a7b2d95/manifest.json`
- Comparison: `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.428--5.0.429/comparison.json`
- Changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-a7b2d95/files/CHANGELOG.md`
- Buttons component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-a7b2d95/files/src/zoid/buttons/component.jsx`
- Package manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-a7b2d95/files/package.json`

## `@paypal/checkout-components@5.0.428` (2026-08-18)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/checkout-components` | `5.0.427` | `5.0.428` | `861ab38f819840054eaed903bfc1ce32eb9b535f` | Delta |

**Important findings:** The no-funding-source Buttons iframe title changes from plain `PayPal` to `PayPal Payment Buttons`; funding-specific titles remain `PayPal-<fundingSource>`. The changelog identifies this as a fix for a duplicate PayPal screen-reader announcement. No public API export or dependency range changes are reported.

**Developer or merchant impact:** Assistive-technology users receive a distinct generic button-container title instead of one that collides with the PayPal funding title. The merchant callback and payment contracts are unchanged.

**Migration action:** No merchant action is documented. Consumers pinned to older component bundles need a version containing this fix to receive it.

**Updated source sections:** overview; evidence boundary; grounding excerpts; `5.0.428` screen-reader title fix; PayPal Checkout concept; PayPal company and provider index version references.

**Evidence boundary:** Upstream release notes were unavailable. The changelog describes the accessibility outcome, while the retained source proves the exact iframe-title branch. It does not identify affected screen readers or browser versions.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.428/2026-09-01/manifest.json`
- Snapshot manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/manifest.json`
- Comparison: `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.427--5.0.428/comparison.json`
- Changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/files/CHANGELOG.md`
- Buttons component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/files/src/zoid/buttons/component.jsx`
- Package manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-861ab38/files/package.json`

## `@paypal/checkout-components@5.0.427` (2026-08-14)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/checkout-components` | `5.0.426` | `5.0.427` | `6afd3b4e8a9c176ef3d59217cab257af286d1c03` | Delta |

**Important findings:** Austria joins Germany in the Pay Later runtime branch that renders `Später Bezahlen`, and both responsive label-sizing paths now include the `AT` product variant. Rebranded button and overlay styles replace the `PayPal Plain` family with `PayPalOpen-Regular`. The packet reports no public API export change.

**Developer or merchant impact:** Eligible Austrian Pay Later presentation receives the localized label and matching compact sizing. This exact source does not prove that a merchant or buyer is eligible for Pay Later in Austria. The font change is visual presentation, while the `@percy/playwright` pin affects repository testing only.

**Migration action:** No merchant JavaScript API migration is documented. Teams that fork or visually test the component should account for the font-family change and pinned Percy Playwright version.

**Updated source sections:** overview; evidence boundary; grounding excerpts; `5.0.427` Austria Pay Later presentation; Pay Later and Checkout concepts; PayPal company and provider index version references.

**Evidence boundary:** Upstream release notes were unavailable. Findings come from the retained changelog, package manifest, complete assigned delta, exact comparison, and source implementation. Backend-provided `AT` variant handling is presentation evidence, not product-availability evidence.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.427/2026-09-01/manifest.json`
- Snapshot manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/manifest.json`
- Comparison: `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.426--5.0.427/comparison.json`
- Changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/CHANGELOG.md`
- Pay Later label logic: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/src/funding/paylater/config.jsx`
- Responsive sizing logic: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/src/ui/buttons/styles/styleUtils.js`
- Rebranded page font: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/src/ui/buttons/styles/page.js`
- Package manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-6afd3b4/files/package.json`

## `@paypal/checkout-components@5.0.426` (2026-08-04)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/checkout-components` | `5.0.425` | `5.0.426` | `48d428cb79a6d13162cc223cac044043afacdfe5` | Delta |

**Important findings:** The release upgrades Prettier from `^2.5.1` to `^3.9.6`, changes the declared development engines from Node `^18`/npm `8` to Node `^22`/npm `10`, pins `.nvmrc` to `22.22.3`, and moves `@krakenjs/zoid` from `^10.5.3` to `^10.6.0`. The packet reports no public API export change.

**Developer or merchant impact:** Repository contributors and source builders must use the newer Node/npm toolchain. The broad retained diff is primarily formatting and legacy tooling cleanup; it is not evidence of a new checkout capability or merchant eligibility change.

**Migration action:** Consumers rebuilding or contributing to this repository should align with Node 22, npm 10, and Prettier 3. Hosted JavaScript SDK integrators have no documented merchant API migration in this release.

**Updated source sections:** overview; evidence boundary; grounding excerpts; `5.0.426` maintenance boundary; PayPal company and provider index version references.

**Evidence boundary:** Upstream release notes were unavailable, so the release finding comes from the retained changelog, package manifest, complete assigned delta, and exact comparison. The Zoid range change does not by itself prove a user-visible runtime change.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.426/2026-09-01/manifest.json`
- Snapshot manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-48d428c/manifest.json`
- Comparison: `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/5.0.425--5.0.426/comparison.json`
- Changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-48d428c/files/CHANGELOG.md`
- Package manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-48d428c/files/package.json`
- Node pin: `raw/github/paypal/paypal-checkout-components/snapshots/2026-09-01-48d428c/files/.nvmrc`

## `@paypal/checkout-components@5.0.425` (2026-07-22)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/checkout-components` | `4.1.47` | `5.0.425` | `e03bffc45b7a3c7f36346a514f34ebbd168dd403` | Full |

**Important findings:** The exact patch forwards bfcache events through post-robot. Across the accumulated v5 history, the runtime expands beyond v4 Buttons and Checkout with public Card Fields, Marks, Payment Fields, Hosted Buttons, Wallet, and Saved Payment Methods interfaces; Venmo gains desktop/QR handling and vault-without-purchase implementation.

**Developer or merchant impact:** Treat each capability as version-qualified runtime evidence. Venmo vault-without-purchase remains experiment-gated in this source, and shipping callbacks are excluded for its vaultable app-switch/QR presentation. Merchant availability still requires current product documentation and account eligibility.

**Migration action:** Major upgrades from v4 must review component loading, callback contracts, funding eligibility, popup/app-switch behavior, and the matching `paypal/paypal-js` integration. The `5.0.425` patch itself requires no documented merchant API migration.

**Updated source sections:** evidence boundary; v5 accumulated architecture; PayPal Checkout, Vault, and Expanded Checkout concepts; PayPal company summary.

**Evidence boundary:** Upstream release notes were unavailable. The exact patch finding comes from the retained changelog; broader findings come from the complete retained source capsule and the `4.1.47` to `5.0.425` comparison. They do not prove current merchant availability.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-checkout-components/releases/checkout-components/5.0.425/2026-07-23/manifest.json`
- Snapshot manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/manifest.json`
- Comparison: `tracking/github/repos/paypal/paypal-checkout-components/comparisons/checkout-components/4.1.47--5.0.425/comparison.json`
- Changelog: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/CHANGELOG.md`
- Public interfaces: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/interface/`
- Venmo funding config: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/funding/venmo/config.jsx`
- Saved Payment Methods component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/files/src/zoid/saved-payment-methods/component.jsx`

## `@paypal/checkout-components@4.1.47` (2019-02-07)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `@paypal/checkout-components` | Initial baseline | `4.1.47` | `289055a52c55911417d25082681ac626c4c9d160` | Full |

**Important findings:** The historical runtime implements Zoid-based PayPal Buttons and Checkout components, validates merchant order and billing-agreement callbacks, filters funding by server eligibility plus layout/platform constraints, and limits horizontal layouts to two funding sources. Its Venmo configuration is mobile-only and secondary.

**Developer or merchant impact:** A merchant-supplied `createOrder` callback must return a string order ID. Billing agreements cannot be configured together with order creation and require `vault=true`. Button visibility depends on eligibility and presentation context, not configuration alone.

**Migration action:** None for this historical baseline. Use it to answer version-specific v4 questions, not as the implementation guide for a current PayPal integration.

**Updated source sections:** repository responsibility; merchant callback contract; funding eligibility; historical Venmo behavior; public and security boundary; PayPal Checkout concept and company summary.

**Evidence boundary:** No upstream release notes were available for this tag. Findings come from the complete retained 90-file source capsule. The snapshot does not prove current product availability or later desktop Venmo QR behavior.

**Evidence:**

- Release manifest: `raw/github/paypal/paypal-checkout-components/releases/checkout-components/4.1.47/2026-07-23/manifest.json`
- Snapshot manifest: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/manifest.json`
- Release notes record: `raw/github/paypal/paypal-checkout-components/releases/checkout-components/4.1.47/2026-07-23/release-notes.md`
- README: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/README.md`
- Buttons component: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/buttons/component.jsx`
- Funding eligibility: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/funding/funding.js`
- Venmo funding config: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/funding/venmo/config.jsx`
- Public button interface: `raw/github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/files/src/interface/button.js`

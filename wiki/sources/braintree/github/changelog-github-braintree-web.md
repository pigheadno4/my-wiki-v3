---
title: "GitHub changelog: braintree/braintree-web"
type: source
date_ingested: 2026-07-28
date_updated: 2026-09-16
original_format: github-repo
raw_files:
  - "github/braintree/braintree-web/snapshots/2026-09-15-732ed09/manifest.json"
  - "github/braintree/braintree-web/snapshots/2026-07-28-41460fb/manifest.json"
  - "github/braintree/braintree-web/snapshots/2026-07-27-bae582d/manifest.json"
tags: [braintree, javascript-sdk, changelog, github-repository]
---

## Overview

Chronological release synthesis for `braintree/braintree-web`. Cumulative implementation knowledge belongs in [[source-github-braintree-web]] and the linked immutable snapshots.

## `braintree-web@3.145.0` (2026-08-24)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree-web` | `3.144.0` | `3.145.0` | `732ed094354d650605e678d98246ce6332952ad3` | Delta (high priority) |

**Important findings:** PayPal Checkout v6 sends billing-token and checkout identifiers together for checkout-with-vault and conditionally exposes the gateway's `implicitlyVaultedPaymentMethodToken`. Venmo desktop QR gains ECD-gated billing/shipping-address passthrough, a refreshed modal, custom fonts, and rescan handling. Deferred client loading retries once; popup flows observe suspend/resume and recheck closure. FraudNet reports load failures and Fastlane preserves underlying errors. `@braintree/asset-loader` changes from `2.0.3` to `2.1.0`; `qrcode@1.5.4` is added.

**Developer or merchant impact:** Pass the full approval data, including `billingToken`, for checkout-with-vault; verify any independently versioned wrapper forwards it. Desktop address collection requires ECD enablement and the modern `paymentMethodUsage` mutation. Returned addresses and vaulted tokens remain backend-dependent. Popup recovery analytics is emitted before tokenization and must not be treated as payment success.

**Migration action:** No mandatory migration is stated in the release notes. Exercise checkout-with-vault, ECD-disabled and enabled Venmo QR paths, rescan/cancel, background-return handling, and script-load failure in the merchant integration. The repository adds npm `>11.7.0`; do not interpret this as a browser requirement. The v6 script loader changes independently of the non-v6 loader; Fastlane's external loader remains `1.2.1`.

**Updated source sections:** PayPal Checkout v6; Venmo; loading and popup recovery; grounding excerpts; exact release findings. Existing `3.143.0` and `3.144.0` knowledge is preserved.

**Evidence boundary:** All 29 added/modified retained files and their diffs were read fully; 303 retained files are unchanged. All 47 upstream changes reconcile to 29 retained and 18 excluded dispositions. For this work item only, the user approved mechanical disposition validation instead of full reading of excluded test/lockfile/tooling diffs. Exact file hashes were checked; upstream tests and hosted payment flows were not run.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree-web/releases/braintree-web/3.145.0/2026-09-15/manifest.json`
- Release notes: `raw/github/braintree/braintree-web/releases/braintree-web/3.145.0/2026-09-15/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/manifest.json`
- Comparison manifest: `tracking/github/repos/braintree/braintree-web/comparisons/braintree-web/3.144.0--3.145.0/comparison.json`
- [Readable comparison](../../../../tracking/github/repos/braintree/braintree-web/comparisons/braintree-web/3.144.0--3.145.0/comparison.md)
- [PayPal v6 tokenization](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/paypal-checkout-v6/paypal-checkout-v6.js)
- [Venmo desktop implementation](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/venmo/external/venmo-desktop.js)
- [Shared deferred loader](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/lib/create-deferred-client.js)
- [FrameService](../../../../raw/github/braintree/braintree-web/snapshots/2026-09-15-732ed09/files/src/lib/frame-service/external/frame-service.js)

## `braintree-web@3.144.0` (2026-07-27)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree-web` | `3.143.0` | `3.144.0` | `41460fba05c1ea1222e795b36a10765a6699b8e7` | Full |

**Important findings:** PayPal Checkout adds View/Edit Funding Instrument for returning buyers with a vaulted Billing Agreement and a client token generated with `preferredPaymentMethodToken`. PayPal Checkout v6 forwards new plan, locale, presentation, risk, and shipping options. Venmo creation now survives failure of the incognito-detection promise. `framebus` moves from `6.0.3` to `6.1.0`.

**Developer or merchant impact:** Eligible Braintree merchants can expose PayPal saved-payment-method editing in checkout and configure more of the v6 experience/session payload. A browser-detection failure no longer aborts Venmo component creation.

**Migration action:** No mandatory migration is documented. Edit FI requires server-side client-token generation with a preferred payment-method token plus `editBillingAgreement: true` in the checkout payment resource. Treat the new v6 fields as optional and validate product eligibility and supported combinations against current guidance.

**Updated source sections:** Evidence boundary; PayPal Checkout v6; PayPal View/Edit Funding Instrument; Venmo; exact release findings; Braintree company and integration concepts.

**Evidence boundary:** The comparison shows 319 retained files are byte-identical, 10 files changed, and one story was added. Edit FI availability depends on client-token context and delegated PayPal SDK `SavedPaymentMethods`; incognito-detection fallback does not prove private-browser support.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree-web/releases/braintree-web/3.144.0/2026-07-28/manifest.json`
- Release notes: `raw/github/braintree/braintree-web/releases/braintree-web/3.144.0/2026-07-28/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/manifest.json`
- Comparison manifest: `tracking/github/repos/braintree/braintree-web/comparisons/braintree-web/3.143.0--3.144.0/comparison.json`
- Readable comparison: `tracking/github/repos/braintree/braintree-web/comparisons/braintree-web/3.143.0--3.144.0/comparison.md`
- Edit FI story: `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/files/.storybook/stories/PayPalCheckout/PayPalCheckoutEditFI.stories.ts`
- PayPal Checkout implementation: `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/files/src/paypal-checkout/paypal-checkout.js`
- PayPal Checkout v6 implementation: `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/files/src/paypal-checkout-v6/paypal-checkout-v6.js`
- Venmo entry point: `raw/github/braintree/braintree-web/snapshots/2026-07-28-41460fb/files/src/venmo/index.js`

## `braintree-web@3.143.0` (2026-06-11)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `braintree-web` | Initial baseline | `3.143.0` | `bae582d791026c143abb91c3bdcada92b8c060f6` | Full |

**Important findings:** The release updates `credit-card-type` to `10.2.0` and replaces `@paypal/accelerated-checkout-loader` with `@paypal/fastlane-sdk-loader`.

**Developer or merchant impact:** The package now loads Fastlane through the renamed loader dependency. The release notes do not identify a checkout-flow or public-API behavior change.

**Migration action:** No application migration is documented for this release. Integrations that directly inspect or constrain dependency package names should account for the loader rename.

**Updated source sections:** Package and client architecture; Fastlane dependency; exact release findings; Braintree company baseline.

**Evidence boundary:** This is the first retained Braintree Web baseline, so no prior exact-SHA comparison exists. Patch findings come from the release notes and package manifest; broader source-page findings describe accumulated `3.143.0` behavior.

**Evidence:**

- Release manifest: `raw/github/braintree/braintree-web/releases/braintree-web/3.143.0/2026-07-27/manifest.json`
- Release notes: `raw/github/braintree/braintree-web/releases/braintree-web/3.143.0/2026-07-27/release-notes.md`
- Snapshot manifest: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/manifest.json`
- Package manifest: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/package.json`
- Repository changelog: `raw/github/braintree/braintree-web/snapshots/2026-07-27-bae582d/files/CHANGELOG.md`

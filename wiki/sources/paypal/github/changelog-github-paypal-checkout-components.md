---
title: "GitHub changelog: paypal/paypal-checkout-components"
type: source
date_ingested: 2026-07-23
original_format: github-repo
raw_files:
  - "github/paypal/paypal-checkout-components/snapshots/2026-07-23-e03bffc/manifest.json"
  - "github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/manifest.json"
tags: [paypal, checkout, javascript-sdk, changelog, github-repository, venmo]
---

## Overview

Chronological release synthesis for `paypal/paypal-checkout-components`. Cumulative implementation knowledge belongs in [[source-github-paypal-checkout-components]] and the linked immutable snapshots.

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

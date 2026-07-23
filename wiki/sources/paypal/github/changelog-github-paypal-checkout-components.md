---
title: "GitHub changelog: paypal/paypal-checkout-components"
type: source
date_ingested: 2026-07-23
original_format: github-repo
raw_files:
  - "github/paypal/paypal-checkout-components/snapshots/2026-07-23-289055a/manifest.json"
tags: [paypal, checkout, javascript-sdk, changelog, github-repository, venmo]
---

## Overview

Chronological release synthesis for `paypal/paypal-checkout-components`. Cumulative implementation knowledge belongs in [[source-github-paypal-checkout-components]] and the linked immutable snapshots.

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

---
title: "GitHub changelog: Adyen/adyen-magento2"
type: source
date_ingested: 2026-08-25
original_format: github-repo
raw_files:
  - "github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/manifest.json"
tags: [adyen, adobe-commerce, magento2, checkout, changelog, github-repository]
---

## Overview

Chronological release synthesis for `Adyen/adyen-magento2`. The installable Composer package and collection release ID are `adyen/module-payment@11.0.0`. Cumulative implementation knowledge belongs in [[source-github-adyen-magento2]] and the linked immutable snapshots.

## `adyen/module-payment@11.0.0` (2026-07-08)

| Package | From | To | SHA | Ingest mode |
| --- | --- | --- | --- | --- |
| `adyen/module-payment` | Initial retained baseline; upstream comparison starts at `10.10.3` | `11.0.0` | `4206983499d829ef695185ac78af06b9bdfe96c6` | Full |

**Important findings:** This major release targets Magento 2.4.8 and PHP 8.2-8.5, upgrades Checkout Components to 6.35.0 and the PHP API Library to v29, enables the NEA region, adds stale payment-response cleanup, and fixes partial-payment invoice and order-state consistency. Contract-sensitive changes affect payment-method filtering, `/payments/details` error shape, authorized-amount comparison, capture-mode lookup, and stored `cc_type` data.

**Developer or merchant impact:** Merchants upgrading from 10.x must validate Magento and PHP compatibility, customizations around payment-method filtering and details errors, capture configuration, partial-payment accounting, and cron execution. Checkout UI and server behavior also cross independently versioned Web Components and PHP library boundaries.

**Migration action:** Upgrade through Composer, run Magento setup upgrade, verify cron and webhook processing, and regression-test headful or headless checkout, actions, stored methods, capture/refund, partial gift-card payments, and custom extensions. Do not edit the default plugin when an extension point can carry the customization.

**Updated source sections:** compatibility and installation; payment-method discovery; headful and headless checkout; modifications and order state; gift cards, POS, and Giving; vaulting; webhook and cron operations; release findings and caveats.

**Evidence boundary:** This is the first retained exact-SHA baseline, so the wiki does not hold the full `10.10.3` implementation. Release-introduced claims come from the release notes; broader architecture is cumulative behavior present at 11.0.0. The observed callback-argument mismatch and residual `supports_auto_capture` configuration are code-review caveats, not confirmed runtime regressions.

**Evidence:**

- Release manifest: `raw/github/adyen/adyen-magento2/releases/module-payment/11.0.0/2026-08-25/manifest.json`
- Release notes: `raw/github/adyen/adyen-magento2/releases/module-payment/11.0.0/2026-08-25/release-notes.md`
- Snapshot manifest: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/manifest.json`
- Compatibility metadata: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/composer.json`
- Checkout callback builder: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/view/frontend/web/js/model/adyen-checkout.js`
- Generic payment renderer: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/view/frontend/web/js/view/payment/method-renderer/adyen-pm-method.js`

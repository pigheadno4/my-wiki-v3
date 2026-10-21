---
title: "Adyen Marketplace payout reporting components"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/components-overview/after-payment/payouts-component"
raw_files:
  - "adyen/docs/marketplaces/components-overview/after-payment/payouts-component/2026-09-15.md"
tags: [adyen, marketplaces, platforms, ui-components, payout-reporting]
---

## Overview

This 2026-09-15 Marketplace-path Platform Experience guide covers embedding **Payouts Overview** and **Payout Details** reporting components in a platform user's portal. They display completed automatic-payout records, captured funds, adjustments, net payouts and remaining balance by balance account. The components read reporting data; they do not initiate a payout or independently establish that a beneficiary bank received funds. Feature guidance can vary by library version. [[adyen]] [[adyen-platform-components]]

## Key takeaways

- Prerequisites are an **Adyen for Platforms** integration, Balance Platform API key for the Session Authentication API, and Adyen-assigned **Payouts Overview Component: View** role on that credential. Configure generation of the Balance Platform Payout report; check applicable language, country/region and browser support. The report coverage described here is for **automatic payouts with a default settlement delay**; manual payouts, pass-through payouts and sales-day payout T+0 are excluded. See raw lines 36-56.
- **Payouts Overview** lists completed automatic payouts for a selected balance account and period, with captured funds, aggregated adjustments and net payout in that balance account's currency. **Payout Details** provides the breakdown and any remaining balance, embedded as a modal by default or mounted separately. The period filter is UTC+0 and defaults to Last 30 days. See raw lines 60-118.
- The raw calls net payout the final amount credited to the user's bank account (line 66), but a component display or completed label is **reporting UI**, not independent bank-statement or transfer-outcome proof. Keep captured funds, adjustment aggregation, net payout and bank receipt separate.
- The platform **server** creates a Session Authentication `POST /sessions` token with `allowOrigin`, `product: platform`, and `policy.resources` scoped to the relevant `accountHolderId`/`accountHolder` plus the Payouts Overview view role. On live, `allowOrigin` supports HTTPS only. The front end loads the library and uses `onSessionCreate` to retrieve and refresh the whole session object; the component's default environment is test unless set to live. See raw lines 147-197, 251-262 and 319-368.
- The Payout Details initializer takes a balance-account `id` and ISO `date`; `onRecordSelection` can pass balance account ID/date from overview for separate detail display. The standalone JavaScript sample omits a comma between its `id` and `date` properties (raw lines 362-366), so it is illustrative rather than copy-ready. Library selection, optional SRI when embedding CDN assets, customization and localization are version-specific implementation details in raw lines 199-818; `availableTranslations` is deprecated (raw line 259).

## Detail locators

- Opening and `## Requirements`, raw lines 15-56: purpose, version caveat, role/API/report setup and automatic-payout coverage limits.
- `## Payouts Overview component` and `## Payout Details component`, raw lines 60-118: account/currency grain, adjustments, remaining balance, modal/separate display, UTC+0 filters.
- `## 1. Create an authentication session from your server`, raw lines 147-197: server-side credential, role, scoped policy, product and origin.
- `## 2. Install component library` and `## 3. Initialize components`, raw lines 199-398: npm/CDN options, versioned SRI, callback, default test environment, per-component fields and sample syntax defect.
- Optional localization, appearance and data customization, raw lines 400-796; supported languages, raw lines 798-814.

## Related

- [[adyen-platform-components]] — owning Platform Experience component concept.
- [[adyen-platforms]] — Marketplace route within Adyen for Platforms.
- [[source-adyen-docs-platforms-components-overview-after-payment-payouts-component]] — separately pinned Platforms-path guide; its own raw governs its claims and locators.

## Raw Sources

- [[raw/adyen/docs/marketplaces/components-overview/after-payment/payouts-component/2026-09-15|Adyen Marketplace payout components guide, captured 2026-09-15]]

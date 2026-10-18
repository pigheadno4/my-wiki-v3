---
title: "Adyen for Platforms payout components"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/components-overview/after-payment/payouts-component"
raw_files:
  - "adyen/docs/platforms/components-overview/after-payment/payouts-component/2026-09-15.md"
tags: [adyen, platforms, components, payout-reporting, dashboards]
---

## Overview

This 2026-09-15 Adyen for Platforms guide explains how to embed Platform Experience **Payouts Overview** and **Payout Details** components in a platform user's portal. They display payout reporting for a balance account, including captured funds, aggregated adjustments and net payout, using the Balance Platform Payout Report. This is a reporting UI and authentication-session integration, not an API for initiating payouts or independent proof that a beneficiary bank received funds. The page warns that features vary by library version.

## Key takeaways

- The guide requires an Adyen for Platforms integration, Balance Platform API key for Session Authentication API, and Adyen-assigned **Payouts Overview Component: View** API credential role. The Balance Platform Payout Report must be generated; language, country/region and browser support must be checked. Its stated report limitation is automatic payouts with default settlement delay; manual payouts, pass-through payouts and sales-day payout T+0 are unsupported here. Component display cannot fill these report-coverage gaps.
- **Payouts Overview** lists automatic payouts for a selected balance account/time period, with captured funds, adjustments and net payout in that account's currency. **Payout Details** shows one payout's breakdown and remaining balance, embedded as a modal by default or initialized separately. The time-period filter uses UTC+0 and defaults to last 30 days. The raw calls net payout the final bank-credit amount, but a component value or completed label alone is not independent bank statement or transfer-outcome proof.
- A platform server requests Session Authentication API `/sessions` with `allowOrigin`, `product: platform`, and policy resources scoped to an `accountHolderId` plus the View role; live `allowOrigin` requires HTTPS. The client receives the complete session object via `onSessionCreate`, initializes the Platform Experience library and mounts the component. The page offers npm or versioned CDN script/CSS with SRI hashes. Session creation and rendering are access/display steps, not payout execution.
- For a separate Details view, the parameter table says `id` is the **balance account ID** and `date` is an ISO payout date; `onRecordSelection` returns `balanceAccountId` and `date`. A later example labels its `id` value `<SELECTED_PAYOUT_ID>`, contradicting that table/callback, and the earlier standalone Details code sample omits a comma after `id`. Do not copy those examples without resolving the identifier and syntax against the selected library version. The page deprecated `availableTranslations`; optional localization, appearance and custom-data controls remain version-sensitive.

## Detail locators

- Opening and `Requirements` — reporting-only component purpose, version caveat, Session Authentication role/key, payout-report scope and language/region/browser setup (raw lines 15–56).
- `Payouts Overview component` and `Payout Details component` — account/time filters, UTC+0 window, default last 30 days, amount display, modal or separate detail view (lines 60–118).
- `Create an authentication session from your server` — server `/sessions`, account-holder resource, role, product, origin/HTTPS and response object (lines 145–200).
- `Install component library` and `Initialize components` — npm/CDN-SRI options, deprecated translation setting, test/live environment, `onSessionCreate`, mount and identifier/date example conflict (lines 202–397).
- Optional localization, appearance and data customization, including callback return-shape and custom-field translation rules, plus supported locales (lines 398–818).

## Related

- Company: [[adyen]]
- Main concept: [[adyen-platform-components]]
- Platform context: [[adyen-platforms]]
- Related source: [[source-adyen-docs-platforms-reports-and-fees-payout-report]]

## Raw Sources

- [[raw/adyen/docs/platforms/components-overview/after-payment/payouts-component/2026-09-15|2026-09-15 Platforms payout components guide]]

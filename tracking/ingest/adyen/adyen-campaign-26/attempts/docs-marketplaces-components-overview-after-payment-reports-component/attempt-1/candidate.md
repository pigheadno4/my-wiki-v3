---
title: "Marketplace Reports Overview component"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/components-overview/after-payment/reports-component"
raw_files:
  - "adyen/docs/marketplaces/components-overview/after-payment/reports-component/2026-09-15.md"
tags: [adyen, marketplaces, platform-experience, reports, components]
---

## Overview

This pinned Marketplace guide describes the Platform Experience **Reports Overview** component for a platform user's portal. It lists downloadable reports for a specified balance account and time period and can add platform-defined fields, icons, links or buttons. The page says features vary by library version. See [[adyen]] and [[adyen-platform-components]] (raw lines 15–37, 57–76).

## Key takeaways

- The component currently supports **only the Payout report**, backed by the Balance Platform Payout report. The stated coverage is automatic payouts with a default settlement delay; it excludes manual payouts, pass-through payouts and sales-day payout **T+0**. The Payout report list describes completed automatic payouts and their debit/credit transactions, not an independent beneficiary-bank receipt (raw lines 43–55, 78–82).
- Prerequisites include an Adyen for Platforms integration, a Balance Platform API key with **Reports Overview Component: View** assigned by an Adyen contact, a generated Balance Platform Payout report, and applicable language, region and browser support checks (raw lines 43–55).
- A platform backend creates a Session authentication API token via POST `/sessions`. The request carries `allowOrigin`, `product: platform`, and a policy scoped to the linked **accountHolderId** resource plus the Reports Overview view role. Live `allowOrigin` supports HTTPS only. The server passes the complete session object to the front end for initialization and refresh (raw lines 126–181, 228–295).
- The UI downloads generated CSV reports and filters by balance account and time period. The guide states report data is generated daily at **midnight UTC+0**; the default time filter is **Last 30 days**. If `balanceAccountId` is fixed at initialization, the balance-account selector is hidden (raw lines 73–109, 245–257).
- The front end uses the Platform Experience library from npm or versioned script/CSS assets; script embedding calls for Adyen's version-specific SRI hashes. `onSessionCreate` is required, the default environment is TEST, and `availableTranslations` is deprecated. Optional appearance/data/localization settings do not change the Payout report's coverage or prove payout execution (raw lines 183–295, 298–651).

## Detail locators

- Current report coverage, role, generation and supported-platform constraints: raw lines 27–55.
- Account/date filters and UTC generation: raw lines 57–109.
- Scoped server session, frontend install and initialization: raw lines 111–295.
- Optional style, custom fields/callbacks and locales: raw lines 298–669.

## Related

- [[adyen]]
- [[adyen-platform-components]]
- [[adyen-reporting]]
- [[adyen-platforms]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/components-overview/after-payment/reports-component/2026-09-15|Pinned Reports component guide]]

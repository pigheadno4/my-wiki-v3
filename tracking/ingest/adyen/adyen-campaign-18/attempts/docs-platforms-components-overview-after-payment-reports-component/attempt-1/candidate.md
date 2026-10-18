---
title: "Adyen Platform Experience Reports component"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/components-overview/after-payment/reports-component"
raw_files:
  - "adyen/docs/platforms/components-overview/after-payment/reports-component/2026-09-15.md"
tags: [adyen, platforms, components, payout-report, reporting]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes the Platform Experience Reports Overview component for a user portal. It lists and downloads generated reports by balance account and time period, currently only the Payout report backed by the Balance Platform Payout report. The component presents report files and optional custom dashboard data; it does not initiate a payout or independently confirm a beneficiary bank credit. See [[adyen]], [[adyen-platforms]] and [[adyen-platform-components]].

## Key takeaways

- **Coverage limit:** The page says the component currently supports only the Payout report, designed for automatic payouts with default settlement delay. It explicitly excludes manual payouts, pass-through payouts and sales-day payout T+0. The guide directs setting up Balance Platform Payout report generation first. The component's report-type table describes automatic payouts completed for a specific balance account and associated debit/credit transactions; do not treat a missing file as proof that no other payout occurred.
- **Access and integration:** The guide requires an Adyen for Platforms integration, a Balance Platform API key with Reports Overview Component: View role, and a server-created Session authentication token scoped to an account-holder resource, that role, allowed origin, and product platform. The front end installs or embeds the Platform Experience library and refreshes the session through onSessionCreate. Live origins require HTTPS; embedded script/styles use version-specific SRI hashes. Version-dependent features, TEST defaults and sample tokens are implementation examples, not current account access proof.
- **Display grain:** Users can download a generated CSV and filter listed reports by balance account and time period. The time-filter section states report data is generated daily at midnight UTC+0. That describes this component's listing cadence; it does not guarantee a Payout report exists for every account and day. An optional balanceAccountId pins the component to one account and hides account switching. The report contains payout-linked debits/credits, not an independent bank receipt.
- **Customization:** Optional dataCustomization can add fields, icons, links and buttons; a custom field requires onDataRetrieve to return report records extended with custom data. The page also documents error/support and filter callbacks, localization, CSS changes and custom-field translations. Such custom data is platform-supplied UI content, separate from the underlying generated report.

## Detail locators

- Identity, version caveat, requirements and report limitations: pinned raw lines 15-55.
- Reports Overview, CSV, Payout report scope, filters and UTC time statement: pinned raw lines 59-109.
- Server Session authentication policy, role and example: pinned raw lines 111-180.
- Library installation, versioned SRI and component initializer/callbacks: pinned raw lines 182-303.
- Appearance, custom data and translation requirements: pinned raw lines 317-650; supported locales: lines 653-673.

## Related

- [[adyen-platform-components]] — Platform Experience concept and reciprocal source route.
- [[adyen-platforms]] — parent platform context.

## Related raw API references

- [[raw/adyen/docs/platforms/reports-and-fees/payout-report/2026-09-15|Balance Platform Payout report]] — underlying report guide; navigation only.

## Raw Sources

- [[raw/adyen/docs/platforms/components-overview/after-payment/reports-component/2026-09-15|Adyen Report components, captured 2026-09-15]]

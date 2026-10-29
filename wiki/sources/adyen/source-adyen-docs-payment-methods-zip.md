---
title: "Adyen Zip payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/zip"
raw_files:
  - "adyen/docs/payment-methods/zip/2026-09-15.md"
tags: [adyen, zip, buy-now-pay-later, redirect, australia, united-states]
---

## Overview

This Adyen Docs Zip overview was last modified 2024-07-15 and captured 2026-09-15. It introduces Zip as a buy now, pay later method, naming Zip Pay and Zip Money in Australia, and lists AU/US and AUD/USD in a redirect-flow capability row. It describes shopper selection of a weekly, fortnightly or monthly installment schedule. The historical table and guide links do not establish current account enablement, product eligibility or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The described shopper flow redirects from the merchant website or app to Zip for account sign-in and SMS one-time-password authentication, then back to the merchant. The return step alone does not establish authorization, capture or settlement (pinned raw lines 24–30).
- The feature row marks recurring, refunds including partial and multiple partial, separate and partial captures including multiple partial, and chargebacks with checkmarks. These are overview indicators rather than API instructions or merchant entitlements. The row lists **AU, US** and **AUD, USD** but does not explicitly pair each country with its currency or define country-specific product behavior (lines 32–34).
- The page routes to Web, iOS, Android, API-only and Pay by Link guides. These child paths own implementation requirements and lifecycle detail (lines 36–66).

> [!warning] Missing separate-capture note
> The feature row marks separate captures with “See note,” but no corresponding note appears in this captured page (raw lines 32–66). Its separate-capture conditions cannot be recovered from this overview alone; verify the relevant child or capture guidance before using the table as an operational rule.

## Detail locators

- Page identity, modification/capture dates and Zip Pay/Zip Money description: pinned raw lines 1–22.
- Shopper redirect and SMS authentication: lines 24–30. Capability row and unresolved separate-capture note: lines 32–34.
- Platform and API/Pay by Link routes: lines 36–66.

## Related

- [[adyen-online-payments]] — provider online-payments concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/zip/2026-09-15|Zip overview, captured 2026-09-15]]

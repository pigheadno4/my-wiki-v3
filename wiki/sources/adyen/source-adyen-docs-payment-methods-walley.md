---
title: "Adyen Walley payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/walley"
raw_files:
  - "adyen/docs/payment-methods/walley/2026-09-15.md"
tags: [adyen, walley, buy-now-pay-later, b2c, b2b, nordics]
---

## Overview

This Adyen Docs Walley overview was last modified 2024-07-17 and captured 2026-09-15. It describes Walley as a Nordic buy now, pay later redirect method supporting both B2C and B2B. Its matrix gives distinct payment method types and regional scopes; the page routes to Web, iOS, Android and API-only guides. It does not establish current merchant eligibility, account enablement or a successful transaction. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The **B2C** row uses payment method type `walley` and lists DK, FI, NO, SE with DKK, EUR, NOK, SEK. The **B2B** row uses `walley_b2b` and lists FI, NO, SE with EUR, NOK, SEK. Both are redirect flows. The page explicitly limits payments in Denmark **or** with DKK currency to B2C. The rows list countries and currencies but do not explicitly pair each other country with a currency (pinned raw lines 23–32).
- For both rows, the capability matrix marks recurring and multiple partial refunds unavailable; it marks refunds, partial refunds, separate captures, partial captures, multiple partial captures and chargebacks available. These are overview indicators, not a complete API recipe or proof of merchant-specific entitlement (lines 25–28).
- **Authorised payments must be captured within 90 days** (line 30). The page does not detail the consequence of missing the deadline; follow the relevant child or capture guide for implementation and outcome handling.
- Platform routes are Web, iOS, Android and API-only (lines 34–58). These child guides own the request fields and integration-specific prerequisites.

## Detail locators

- Method description, B2C/B2B types, regional and capability rows, capture window: pinned raw lines 23–32.
- Web, iOS, Android and API-only routes: lines 34–58.

## Related

- [[adyen-online-payments]] — provider online-payments concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/walley/2026-09-15|Walley overview, captured 2026-09-15]]

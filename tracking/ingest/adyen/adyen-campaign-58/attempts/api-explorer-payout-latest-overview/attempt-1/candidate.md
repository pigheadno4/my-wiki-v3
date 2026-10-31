---
title: "Adyen Payout API v68 overview (deprecated)"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payout/latest/overview"
raw_files:
  - "adyen/api-explorer/Payout/latest/overview/2026-09-15.md"
tags: [adyen, payouts, payout-api, deprecated, api-overview]
---

## Overview

This 2026-09-15-captured **Payout API v68** overview describes legacy endpoints for storing payout details and submitting, confirming or declining payouts. It explicitly says the Payout API is **deprecated and no longer supports new integrations**. New integrations are directed to the Transfers API; existing Payout API users are directed to their Adyen contact for migration. This legacy API is distinct from the newer Transfers API and its resource model. [[adyen]] [[adyen-payouts]]

## Key takeaways

- The page requires **two API credentials**: one for storing payout details and submitting payouts, another for confirming or declining them. It tells readers without those credentials to contact Support. It shows API-key authentication using `X-API-Key` or basic username/password authentication, with a submission example (raw lines 27–45).
- The listed server and sample payout URL are **test** `https://pal-test.adyen.com/pal/servlet/Payout/v68`. The live example uses a company-specific `{PREFIX}-pal-live.adyenpayments.com` host and credentials from the live Customer Area. `latest` in the documentation route does not change the captured `v68` endpoint version (raw lines 47–66).
- The General catalog lists six POST operations: `/confirmThirdParty` (confirm), `/declineThirdParty` (cancel), `/payout` (instant card payout), `/storeDetail` (store details), `/storeDetailAndSubmitThirdParty` (store and submit), and `/submitThirdParty` (submit). These are operation summaries, not request/response schemas or proof of a payout, confirmation, cancellation or recipient credit. The page does not state a default-denial behavior; consult specific operation and Online payouts guides for lifecycle details (raw lines 68–78).

## Detail locators

- Deprecation, migration direction and stated scope: raw lines 5–25. Separate credential duties and authentication alternatives: lines 27–45. Versioning, test and live hosts/credentials: lines 47–66. Full endpoint catalog: lines 68–78.

## Related

- [[adyen-card-payouts]] — legacy instant card payout route and its eligibility limits.
- [[adyen-payouts]] — broader payout concepts and distinction from Payout Service/Transfers API.

## Raw Sources

- [[raw/adyen/api-explorer/Payout/latest/overview/2026-09-15|Payout API v68 overview, captured 2026-09-15]]

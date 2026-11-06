---
title: "Capital API: calculate a preliminary dynamic offer"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/post/dynamicOffers/(id)/calculate"
raw_files:
  - "adyen/api-explorer/capital/latest/post/dynamicOffers/(id)/calculate/2026-11-07.md"
tags: [adyen, capital, dynamic-offers, api-explorer]
---

## Overview

This 2026-11-07 Capital API `latest` v1 reference describes `POST /dynamicOffers/{id}/calculate`: calculate a preliminary offer from a user's selected financing amount and a dynamic-offer ID. **The result is informational only and cannot initiate a grant.** The captured TEST and LIVE servers are `/capital/v1` at the respective balance-platform API hosts. See [[adyen]] and [[adyen-capital]].

## Key takeaways

- Required path `id` identifies the dynamic offer. The request body requires `amount`, including ISO currency and integer value in minor units. No additional body inputs or amount range are stated here. The page lists 120 requests per minute for each of TEST and LIVE.
- A 200 preliminary result requires account-holder ID, proposed payout amount, `loan` or `cashAdvance` contract type, start/end validity times, fee amount, and repayment basis points. APR basis points, term and threshold are optional parents or fields; if term is present its estimated days are required, while maximum days applies only to a loan. The response describes hypothetical offer and grant terms, not a grant resource or payout.
- The reference lists 422 request validation error with optional problem fields; it does not specify authentication role, idempotency, approval, grant creation, or disbursement behavior for this calculation.

## Detail locators

- Purpose, rate limits, servers, and required request: pinned raw lines 5–36.
- 200 offer terms and nested requiredness: pinned raw lines 38–64.
- 422 validation problem schema: pinned raw lines 67–83.

## Related

- [[adyen-capital]] — financing lifecycle.
- [[source-adyen-api-explorer-capital-latest-get-dynamicoffers]] — dynamic-offer inventory.

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/post/dynamicOffers/(id)/calculate/2026-11-07|Dynamic-offer calculation API Explorer snapshot]]
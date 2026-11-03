---
title: "Adyen Balance Platform API GET /grantOffers/{grantOfferId} — get a grant offer"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/grantOffers/(grantOfferId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/grantOffers/(grantOfferId)/2026-11-03.md"
tags: [adyen, capital, balance-platform-api, grant-offers]
---

## Overview

The 2026-11-03 capture of the Balance Platform API Explorer reference describes `GET /grantOffers/{grantOfferId}` as returning the details of one grant offer on the listed test base `https://balanceplatform-api-test.adyen.com/bcl/v2`. The required path value is the offer's unique `grantOfferId`; this is a read operation for [[adyen-capital]], not an offer acceptance or a grant request.

## Key takeaways

- In the 200 response, `accountHolderId` is required and identifies the account holder to which the grant is offered. Optional top-level fields include principal `amount`, `contractType` (`cashAdvance` or `loan`), validity dates `startsAt` and `expiresAt`, `fee`, offer `id`, and `repayment`. Required nested fields apply when their optional parent objects are present; the principal and fee monetary values use currency codes and minor units.
- The repayment schema describes a required `basisPoints` value within optional `repayment`, deducted daily from incoming net volume. Optional `term` has required `estimatedDays`; `maximumDays` is optional and described only for `loan`. Optional `threshold` describes a 30-day repayment amount. These fields describe offer terms, not evidence of actual deductions or completed repayment.
- The reference lists 400, 401, 403, 422 and 500 errors. The 401 and 403 descriptions distinguish authentication from permission; no credential role is named. The generic 422 and 500 example payloads mention payment-instrument information/creation, so they do not establish grant-offer-specific restrictions or failures.
- A successful lookup establishes only that this request returned offer details in the captured contract. The page gives no live endpoint, current meaning of `latest`, idempotency rule, offer acceptance, eligibility or approval guarantee, grant creation, disbursement, bank receipt, or lifecycle/status transition.

## Detail locators

- `## Servers` and `## Parameters > ### Path parameters` — test base and required offer ID.
- `## Responses > ### 200 Success` — response schema, conditional nested requiredness, money units and repayment terms.
- `## Responses > ### 400 Client Error` through `### 500 Server Error` — error schemas; `## Response examples` — generic error payloads, including unrelated payment-instrument details.

## Related

- [[adyen]] — provider.
- [[adyen-capital]] — financing and offer context.
- [[source-adyen-api-explorer-balanceplatform-latest-get-grantoffers]] — captured offer-list route, a separate endpoint.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/grantOffers/(grantOfferId)/2026-11-03|2026-11-03 captured API Explorer reference]]

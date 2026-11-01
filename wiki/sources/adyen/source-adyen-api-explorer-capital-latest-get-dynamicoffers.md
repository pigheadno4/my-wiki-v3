---
title: "Adyen Capital GET /dynamicOffers — available dynamic offers"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/capital/latest/get/dynamicOffers"
raw_files:
  - "adyen/api-explorer/capital/latest/get/dynamicOffers/2026-09-15.md"
tags: [adyen, capital, dynamic-offers, business-financing]
---

## Overview

This 2026-09-15 API Explorer `latest` snapshot describes Capital `GET /dynamicOffers`, a read operation that returns available dynamic offers for the required `accountHolderId` query parameter. It is an offer lookup, not a grant request, accepted offer, disbursement or funding confirmation. See [[adyen]] and [[adyen-capital]].

## Key takeaways

- The page lists separate test and live Capital `/capital/v1` server bases. `accountHolderId` is the required query parameter. Optional `financingType` has the listed value `businessFinancing`; if omitted, the operation returns all available types. These are endpoint contract statements, not current eligibility for any particular account holder.
- The `200 Success` body requires a `dynamicOffers` array. Each listed offer has required account-holder and offer IDs, `contractType` (`loan` or `cashAdvance`), `financingType` (`businessFinancing`), `startsAt` and `expiresAt` validity timestamps, and `minimumAmount`/`maximumAmount` objects with required ISO currency and integer minor-unit value. A required `repayment` object contains a required `term` object; this page does not expand that term's fields. An array schema does not assert that any offer is available for a particular holder.
- The `422 Client Error` section describes request validation. Its problem fields, including `invalidFields`, are optional; `message`, `name` and `value` are marked required only within an `invalidFields` item when such an item is present. A successful offer lookup does not establish formal terms acceptance, grant creation, money transfer or repayment.

## Detail locators

- Purpose, test/live server bases and query parameters: raw lines 5–24. Complete 200 response schema, including offer range, validity, contract type and repayment term: raw lines 25–47.
- 422 validation-error response schema and nested field requirements: raw lines 50–66. The pinned page gives no request or response JSON example or separate response-header contract.

## Related

- [[adyen]] — provider context.
- [[adyen-capital]] — Capital offer versus grant lifecycle.
- [[source-adyen-docs-capital-get-grant-offers]] — separate offer-choice guide.

## Raw Sources

- [[raw/adyen/api-explorer/capital/latest/get/dynamicOffers/2026-09-15|Adyen Capital latest GET /dynamicOffers, captured 2026-09-15]]

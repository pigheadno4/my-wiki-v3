---
title: "Adyen Foreign Exchange API v1: calculate currency amounts and rates"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/foreignexchange/latest/post/rates/calculate"
raw_files:
  - "adyen/api-explorer/foreignexchange/latest/post/rates/calculate/2026-09-15.md"
tags: [adyen, foreign-exchange, currency-conversion, api]
---

## Overview

This captured Foreign Exchange API v1 reference documents `POST /rates/calculate`, which calculates amounts and rates for a proposed transaction currency conversion. It returns calculation data that may be used in payment requests; the response does not execute a payment, conversion, refund, or settlement. See [[adyen]] and [[adyen-currencies-and-fx]].

## Key takeaways

- The request schema requires `exchangeCalculations`, an array whose entries require `exchangeSide` (`buy` or `sell`), `sourceAmount` (three-character currency and integer value in minor units), `targetCurrency`, and transaction `type` (`splitPayment` or `splitRefund`). It gives no array-size, supported-pair, quote-duration, or rate-lock constraint.
- A 200 response may contain calculation entries with `targetAmount` and `appliedExchangeRate`; the latter includes Adyen's markup. The page does not break out a separate fee or promise that a later transaction uses the same rate.
- Listed errors are 401, 403 and 422. The 422 example illustrates invalid currency and negative source value; it is example validation evidence, not a complete rule set. The 403 example mentions token-policy resources, so it does not establish an FX-specific permission requirement.
- The capture lists test and live `/fx/api/v1` server URLs. Their listing and the `latest` page URL do not prove account eligibility, current pair availability, or a fixed current API release.

## Detail locators

- Purpose and test/live server URLs: pinned raw lines 5–15.
- Required request fields and example: pinned raw lines 19–56.
- 200 response fields and calculation example: pinned raw lines 57–74, 133–169.
- Error schemas and examples: pinned raw lines 77–131, 171–219.

## Related

- [[adyen-currencies-and-fx]] — currency and conversion concept.
- [[source-adyen-docs-development-resources-currency-codes]] — separate minor-unit reference.

## Raw Sources

- [[raw/adyen/api-explorer/foreignexchange/latest/post/rates/calculate/2026-09-15|Captured POST /rates/calculate API Explorer page]]

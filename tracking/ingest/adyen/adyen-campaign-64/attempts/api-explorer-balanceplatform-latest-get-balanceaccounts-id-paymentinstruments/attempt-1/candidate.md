---
title: "Adyen Balance Platform API v2: GET /balanceAccounts/{id}/paymentInstruments"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/paymentInstruments"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/paymentInstruments/2026-11-02.md"
tags: [adyen, balance-platform, payment-instruments, issuing, api, pagination]
---

## Overview

This 2026-11-02 Balance Platform API v2 reference describes `GET /balanceAccounts/{id}/paymentInstruments`, a paginated list of card or bank-account payment instruments associated with a balance account. The page shows only the TEST server, `https://balanceplatform-api-test.adyen.com/bcl/v2`; its `latest` documentation route does not verify current live availability. See [[adyen]], [[adyen-issuing]] and [[adyen-business-accounts]].

## Key takeaways

- The balance-account `id` is the required **path** parameter. Optional query parameters are `status` (all statuses by default), `limit` (10 items by default, maximum 100), and `offset` (items to skip). The page shows no request body or idempotency contract for this read operation.
- A 200 response has required `hasNext`, `hasPrevious`, and `paymentInstruments` fields. Each listed instrument's schema requires `balanceAccountId`, instrument `id`, `issuingCountryCode`, and `type` (`card` or `bankAccount`). `card` and `bankAccount` are optional type-dependent objects; requiredness of fields nested under them is distinct from whether those parent objects appear. Replacement IDs, group ID, reference and status are optional.
- The status description distinguishes active, inactive, suspended and permanently closed instruments. It says creation defaults to active unless card form factor and issuing country cause an exception, such as inactive physical cards in the US. That lifecycle wording does not mean this GET activates, changes or closes an instrument. A listed active status is not evidence of a successful authorization, capture, booking or settlement.
- The card schema says `cvc` is returned only in a **POST** response for single-use virtual cards, while the PAN is masked by default and returned unmasked only for single-use virtual cards. Do not infer that this GET returns CVC or an unmasked PAN; the sample GET response shows masked card numbers and no CVC.
- The documented errors are 400, 401 (authentication required), 403 (insufficient permissions), 422 and 500. The 422 and 500 examples describe changing a payment instrument's balance-account ID or creating an instrument, not this list operation; they are not endpoint-specific failure or reversal evidence.

## Detail locators

- Purpose, TEST server, required path ID and optional pagination/status filters: pinned raw lines 5–27.
- 200 response shape, card/bank-account branches, identities, status and replacement fields: pinned raw lines 29–76.
- Error schemas and illustrative 200/error examples: pinned raw lines 79–297.

## Related

- [[adyen-issuing]] — issued-card context.
- [[adyen-business-accounts]] — business-account context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-paymentinstruments]] — separate creation endpoint.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/paymentInstruments/2026-11-02|Balance-account payment-instrument list snapshot]]
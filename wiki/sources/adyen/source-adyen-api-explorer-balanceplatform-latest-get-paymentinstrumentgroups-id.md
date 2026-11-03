---
title: "Balance Platform API: Get a payment instrument group"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstrumentGroups/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/paymentInstrumentGroups/(id)/2026-11-02.md"
tags: [adyen, balance-platform, payment-instrument-groups, api]
---

## Overview

This captured Balance Platform API v2 `GET /paymentInstrumentGroups/{id}` reference returns details of a payment instrument group. The only listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. It is a resource read, not payment-instrument activation or transaction evidence. [[adyen]] [[adyen-issuing]] [[adyen-platforms]]

## Key takeaways

- The required path `id` uniquely identifies the payment instrument group. The reference specifies no query parameters or request body. See **Parameters**, lines 12–17.
- A 200 response requires `balancePlatform`, the balance platform to which the group belongs, and `txVariant`, its transaction variant. Response `id` is optional in the schema and identifies the group named by the path; optional `description`, `properties` and `reference` may also appear. The page gives no allowed `txVariant` list, properties schema, defaults or limits. See **200 Success**, lines 19–32.
- The 200 example uses `txVariant: mc`, but this is illustrative, not the only supported variant. The response establishes successful retrieval of group details, not whether an instrument is issued, linked, enabled, authorized, or used in a successful transaction. See **Response examples**, lines 134–145.
- Listed errors are 400 request problem, 401 authentication required, 403 insufficient permissions, 422 validation error and 500 server failure. The generic 422/500 examples describe payment-instrument operations and cannot be used to infer this GET's specific failure behavior. This capture is a TEST-server snapshot; `latest` does not establish live availability or caller eligibility. The page does not specify idempotency, group deletion or propagation, asynchronous outcome, reversal or version conflict.

## Detail locators

- **Parameters**, lines 12–17: required group path ID.
- **Responses**, lines 19–132: success fields and error statuses/schema.
- **Response examples**, lines 134–211: illustrative group and generic errors.

## Related

- [[adyen-issuing]] — payment instrument group and transaction-rule context.
- [[adyen-platforms]] — balance platform resource context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstrumentGroups/(id)/2026-11-02|Captured payment instrument group GET reference (2026-11-02)]]

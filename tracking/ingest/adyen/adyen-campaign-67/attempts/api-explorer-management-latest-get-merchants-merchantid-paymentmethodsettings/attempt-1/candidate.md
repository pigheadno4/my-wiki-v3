---
title: "Adyen Management API: List merchant payment method settings"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/2026-11-05.md"
tags: [adyen, management-api, payment-methods, merchant-accounts]
---

## Overview

The captured Management API `GET /merchants/{merchantId}/paymentMethodSettings` returns details for the merchant account's payment methods. The pinned reference lists the v3 TEST server `https://management-test.adyen.com/v3` and requires an API credential with the Management API—Payment methods read role. The required path `merchantId` identifies the merchant account. See [[adyen]] and [[adyen-payment-method-variants]].

## Key takeaways

- Optional query filters are `businessLineId` and `storeId`; optional `pageNumber` and `pageSize` control pagination. `pageSize` defaults to 10 and has a maximum of 100.
- A 200 response has optional `data` entries and pagination `_links`, with required top-level `itemsTotal` and `pagesTotal`. Each returned method has a required resource `id`; optional fields include `type` (variant), `enabled`, `allowed`, `verificationStatus`, `businessLineId`, `storeIds`, countries/currencies and method-specific settings. The reference says `allowed` becomes true after Adyen screens the merchant account; `verificationStatus` can be `valid`, `pending`, `invalid` or `rejected`. `typesWithErrors` can identify methods not successfully requested.
- The readback is configuration and status evidence for the returned scope and snapshot. An `enabled` flag alone is not the same as Adyen's `allowed` screening flag or a `valid` verification status, and this endpoint does not itself execute a payment or establish live acceptance, capture, settlement or compliance.
- The reference also lists 204 with no content; 400, 401, 403, 422, 429 and 500 errors. No request body, mutation, idempotency key or activation transition is documented for this GET.

## Detail locators

- Purpose, credential role, TEST server, path and query parameters: raw lines 5–30.
- Pagination, payment-method result fields and method-specific settings: raw lines 32–205. See especially `allowed` (line 62), `enabled` (104), resource `id` (115), `type` (185), `verificationStatus` (191), totals and `typesWithErrors` (203–205).
- Success and error response schemas: raw lines 208–328.

## Related

- [[adyen-payment-method-variants]]
- [[adyen-api-access]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/paymentMethodSettings/2026-11-05|Adyen Management API merchant payment method settings list, captured 2026-11-05]]

---
title: "Get a merchant store | Adyen Management API v3"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(storeId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(storeId)/2026-11-03.md"
tags: [adyen, management-api, point-of-sale, stores, merchants]
---

## Overview

This [[adyen]] Management API reference, captured 2026-11-03, describes `GET /merchants/{merchantId}/stores/{storeId}` to retrieve one store's details. The listed server is `https://management-test.adyen.com/v3`. The API credential needs either **Management API—Stores read** or **Management API—Stores read and write**; the page notes live rate limits without numeric values. See [[adyen-pos-store-management]] for the store administration context.

## Key takeaways

- Both path parameters are required strings: `merchantId` identifies the merchant account, and `storeId` identifies the store. This is a scoped read, with no request body or query parameters in the captured page. [Raw: lines 20–26]
- A `200` response has a store-detail schema with optional top-level fields including Adyen-generated `id`, owning `merchantId`, `reference`, address, business-line IDs, shopper statements, split configuration, status, and registered payment-facilitator `subMerchantData`. Nested required flags apply inside their optional parent objects; they do not make the parents required. The `204` alternative says processing succeeded with no additional content, so it supplies no store representation. [Raw: lines 28–71]
- The status description says a newly created store is `active`; `inactive` blocks new terminal transactions while outstanding captures can still proceed; `closed` is irreversible and reassigns terminals to merchant inventory. A retrieved status alone does not establish assigned/boarded terminals, enabled payment methods, an authorized payment, or settlement. The response also describes optional business-line, split-configuration and sub-merchant identities; those IDs are not interchangeable with the merchant account or store ID. [Raw: lines 47–67]
- `400`, `401`, `403`, `422`, and `500` cover malformed request, authentication, permissions, validation, and server processing errors. Error bodies include problem details and `requestId`; use the error sections for their field-level requiredness. [Raw: lines 74–171]

> [!warning] Contradiction
> The listed server is Management API `/v3`, but the `200` example's `_links.self.href` points to `/v1/stores/...`. The example's `reference` is `Springfield Shop` with a space, while the field description allows letters, digits, hyphens and underscores. Treat the example as illustrative; it does not settle the endpoint version or allowed reference syntax. [Raw: lines 17–18, 57, 173–200]

## Detail locators

- Purpose, role requirement, live rate-limit note and TEST v3 server: raw lines 5–18.
- Required path identities: raw lines 20–26.
- Response fields and nested/conditional descriptions: raw lines 28–67.
- `204` and error response schemas: raw lines 70–171.
- Illustrative `200` response and its v1/reference mismatches: raw lines 173–200.

## Related

- [[adyen-pos-store-management]] — merchant store administration and readiness context.
- [[source-adyen-api-explorer-management-latest-get-stores]] — separate paged store-list reference.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/stores/(storeId)/2026-11-03|Management API get merchant store — captured 2026-11-03]]
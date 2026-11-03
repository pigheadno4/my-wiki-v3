---
title: "GET /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins — list credential allowed origins | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/2026-11-03.md"
tags: [adyen, management-api, api-credentials, allowed-origins, client-side-authentication]
---

## Overview

This 2026-11-03-captured [[adyen]] Management API reference describes `GET /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins`: a list read for the API credential identified in the path under the specified company account. Both path IDs are required, and the calling credential needs **Management API—API credentials read and write**. The only listed server is TEST `https://management-test.adyen.com/v3`. The target credential ID and each returned allowed-origin ID identify different resource types; the page does not say whether the calling credential is also the target. See [[adyen-api-access]]. [Raw: lines 5–22, 32–36]

## Key takeaways

- A `200` reports a succeeded list request. The response schema marks top-level `data` (array of allowed-origin objects) optional. Within each object, `domain` is required and `id` and `_links` are optional; `_links.self` is marked required within `_links`. Preserve these nested conditions rather than treating the sample's two items and IDs as guaranteed. [Raw: lines 24–36, 138–165]
- The response is credential-scoped configuration readback. It does not create or remove origins, issue or rotate a client key, prove an origin has propagated to a browser-side check, or demonstrate a payment or authenticated client request. No query parameters, request body, pagination, idempotency or propagation timing are specified in this reference. [Raw: lines 5–36]
- The page lists `400` request, `401` authentication, `403` permission, `422` validation and `500` server errors with structured problem-body fields. The generic `requestId` description comparing it to `pspReference` does not imply this lookup initiated a payment. [Raw: lines 39–136]

> [!warning] Contradiction
> The listed TEST server is `/v3`, but both allowed-origin self links in the `200` example use `/v1/companies/.../apiCredentials/.../allowedOrigins/...`. The snapshot does not reconcile the version difference; example hrefs are not proof of a v3 route or current live availability. [Raw: lines 13–14, 138–165]

## Detail locators

- Purpose, caller role, TEST server and required company/credential IDs: raw lines 5–22.
- `200` array and nested field requiredness: raw lines 24–36.
- Errors and problem-body fields: raw lines 39–136.
- Two-item response example and `/v1` self links: raw lines 138–165.

## Related

- [[adyen-api-access]] — credential and client-side access context
- [[source-adyen-api-explorer-management-latest-get-me-allowedorigins]] — separate API-key-selected `/me` allowed-origin read

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/2026-11-03|Management API company-credential allowed-origin list — captured 2026-11-03]]
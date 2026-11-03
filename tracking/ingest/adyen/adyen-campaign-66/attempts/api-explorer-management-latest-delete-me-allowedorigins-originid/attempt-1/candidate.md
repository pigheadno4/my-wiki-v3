---
title: "DELETE /me/allowedOrigins/{originId} — remove an allowed origin | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/me/allowedOrigins/(originId)"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/me/allowedOrigins/(originId)/2026-11-03.md"
tags: [adyen, management-api, api-credentials, allowed-origins, client-side-authentication]
---

## Overview

This 2026-11-03-captured [[adyen]] Management API reference describes `DELETE /me/allowedOrigins/{originId}` for the allowed origin identified by required path `originId`. The API key on the request identifies the API credential whose configuration is affected; the page says any Management API role can make the request. Its only listed server is TEST `https://management-test.adyen.com/v3`. This is credential-scoped configuration, not a company-wide or merchant-wide origin removal. See [[adyen-api-access]]. [Raw: lines 5–20]

## Key takeaways

- `originId` is the unique ID of the allowed-origin resource, distinct from the request API key and its API credential. The operation lists no query parameters or request-body schema. [Raw: lines 7–20]
- The listed success is HTTP `204`; the page says to use the actual response code for request status and supplies no success response body or replacement origin record. A success response documents this deletion request, not propagation timing, an effective browser-side origin check, client-key rotation or payment authorization. [Raw: lines 22–25]
- The page lists `400` request, `401` authentication, `403` permissions, `422` validation and `500` server errors. Its problem-body tables include required `detail`, `errorCode`, `status`, `title` and `type`, and optional `instance`, `invalidFields`, `requestId` and `response`. The generic `requestId` description referencing `pspReference` is not evidence of a payment. [Raw: lines 28–125]
- The snapshot provides no idempotency, retry, deletion reversal, propagation or live endpoint rule. The documentation URL segment `latest` does not establish current availability or eligibility. [Raw: lines 1–25]

## Detail locators

- Operation, credential selection, role statement and TEST v3 server: raw lines 5–13.
- Required `originId` path field: raw lines 15–20.
- Bodyless `204` status wording: raw lines 22–25.
- Error statuses and structured problem fields: raw lines 28–125.

## Related

- [[adyen-api-access]] — API credential identity and access context
- [[source-adyen-api-explorer-management-latest-get-me-allowedorigins]] — separate read of credential-scoped allowed origins
- [[source-adyen-api-explorer-management-latest-post-me-allowedorigins]] — separate creation operation

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/me/allowedOrigins/(originId)/2026-11-03|Management API allowed-origin deletion — captured 2026-11-03]]
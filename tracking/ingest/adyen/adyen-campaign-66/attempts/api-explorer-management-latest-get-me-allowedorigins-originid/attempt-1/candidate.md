---
title: "Get one API credential allowed origin | Adyen Management API v3"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/me/allowedOrigins/(originId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/me/allowedOrigins/(originId)/2026-11-03.md"
tags: [adyen, management-api, api-credentials, allowed-origins, client-side-authentication]
---

## Overview

This [[adyen]] Management API reference, captured 2026-11-03, describes `GET /me/allowedOrigins/{originId}` for reading one allowed-origin record. The request API key selects the API credential under `me`; the required path `originId` selects the allowed origin for that credential. The listed server is `https://management-test.adyen.com/v3`, and the reference permits any Management API role. See [[adyen-api-access]] for credential scope.

## Key takeaways

- `originId` is a required string path identifier. The captured operation lists no query parameters or request body; it does not create, change, or remove an origin. [Raw: lines 5–20]
- A `200` response lists required `domain`, optional allowed-origin `id`, and optional `_links`; `_links.self` is marked required only within the optional parent. The returned domain and ID are readback for the API-key-selected credential, not evidence of origin propagation, a client key, successful browser authentication, or an authorized payment. [Raw: lines 22–34]
- `400`, `401`, `403`, `422`, and `500` describe request interpretation, authentication, permissions, validation, and server failures. Their problem-detail response tables include `requestId`; see the raw for exact field requiredness. [Raw: lines 37–134]

## Detail locators

- Purpose, credential selection, role and TEST v3 server: raw lines 5–13.
- Required origin path ID: raw lines 15–20.
- `200` allowed-origin schema: raw lines 22–34.
- Failure categories and body schemas: raw lines 37–134.

## Related

- [[adyen-api-access]] — API credential identity and account scope.
- [[source-adyen-api-explorer-management-latest-get-me-allowedorigins]] — separate list of allowed origins for the request API key.
- [[source-adyen-api-explorer-management-latest-post-me-allowedorigins]] — separate create reference.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/me/allowedOrigins/(originId)/2026-11-03|Management API allowed-origin detail — captured 2026-11-03]]
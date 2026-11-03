---
title: "POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateClientKey — Generate client key | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/generateClientKey"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/generateClientKey/2026-11-03.md"
tags: [adyen, management-api, api-credentials, client-key, authentication]
---

## Overview

This 2026-11-03 Management API v3 reference describes `POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateClientKey` on the listed `https://management-test.adyen.com/v3` server. It returns a new client key for the API credential identified by required `apiCredentialId` under required merchant account `merchantId`. The calling API credential needs `Management API—API credentials read and write`. The client key is distinct from an API key for server requests. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- The captured parameters table lists only the two required path IDs, with no request-body or query fields. No default, numeric rate limit, or idempotency rule is stated.
- The page says the new client key can be used a few minutes after generation and the old client key stops working 24 hours after a new one is generated. A `200` response schema requires `clientKey`; the separate `204` success has no additional content. A response alone is not a demonstration that client-side authentication has already succeeded.
- Listed failures are `400` request problem, `401` authentication required, `403` insufficient permissions, `422` validation error and `500` server error. The reference does not specify exact propagation time within “a few minutes,” retry/idempotency behavior, deletion, asynchronous approval, or version-conflict handling. Its TEST server listing is not live availability evidence.

## Detail locators

- Operation, new/old client-key timing, required role and TEST v3 server: raw lines 5–14.
- Required merchant and API-credential path IDs: raw lines 16–22.
- `200` `clientKey` response and bodyless `204`: raw lines 24–36.
- `400`, `401`, `403`, `422`, `500` error descriptions and repeated schemas: raw lines 39–136.

## Related

- [[source-adyen-api-explorer-management-latest-post-merchants-merchantid-apicredentials]] — Separate merchant-scoped API-credential creation reference.
- [[source-adyen-docs-development-resources-client-side-authentication]] — General client-key and allowed-origin guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/generateClientKey/2026-11-03|Pinned Adyen merchant client-key generation reference (2026-11-03)]]

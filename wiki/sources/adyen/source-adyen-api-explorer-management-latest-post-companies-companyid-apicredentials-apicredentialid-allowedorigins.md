---
title: "Adyen Management API v3: create an API credential allowed origin"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/2026-11-03.md"
tags: [adyen, management-api, api-credentials, allowed-origins]
---

## Overview

This 2026-11-03-captured Management API v3 reference describes `POST /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins`, which adds an allowed origin to a specified API credential under a company account. The listed TEST server is `https://management-test.adyen.com/v3`; the caller's API credential requires **Management API—API credentials read and write**. Both path IDs are required. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- The request-body table marks `domain` required, `id` optional and `_links` optional; if `_links` appears, `self` is marked required within it. The table does not independently say whether the whole body is required. Its example sends only `domain`, so it illustrates a minimal shape without proving that every domain value is accepted.
- `200` indicates the request succeeded and its response table marks `domain` required, with `id` and `_links` optional. The example shows an allowed-origin ID and self-link, but this is not evidence of client-key generation, successful browser authentication, effective origin acceptance in a later request or payment execution. The page does not specify propagation time, idempotency or deletion/reversal behavior.
- `400`, `401` authentication, `403` permissions, `422` validation and `500` errors are listed. The generic error body's `requestId`/`pspReference` wording does not turn origin creation into a payment event. The dated TEST capture does not establish current live access.

> [!warning] Contradiction
> The listed TEST server is `/v3`, while the `200` example self-link uses `/v1`. The sample does not resolve the route-version mismatch; treat its link as illustrative.

## Detail locators

- Raw lines 5–32: purpose, role, TEST v3 server, required path IDs and request-body property requiredness.
- Raw lines 34–54: request example and `200` response schema; lines 57–154: error responses.
- Raw lines 156–171: illustrative response and `/v1` self-link conflict.

## Related

- [[adyen-api-access]] — credential and client-side access context.
- [[source-adyen-api-explorer-management-latest-get-me-allowedorigins]] — separate allowed-origin read for the key-selected credential.
- [[source-adyen-docs-development-resources-client-side-authentication]] — separate client-side key and origin guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/2026-11-03|2026-11-03 allowed-origin create reference]]
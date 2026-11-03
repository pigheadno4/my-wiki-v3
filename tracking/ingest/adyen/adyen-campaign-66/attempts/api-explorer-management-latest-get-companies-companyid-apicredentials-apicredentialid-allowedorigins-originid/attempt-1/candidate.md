---
title: "Adyen Management API v3: get a credential's allowed origin"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)/2026-11-03.md"
tags: [adyen, management-api, api-credentials, allowed-origins]
---

## Overview

This captured Management API v3 `GET /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId}` reference reads the allowed-origin resource identified under a specific company account and API credential. All three path IDs are required strings. The listed server is `https://management-test.adyen.com/v3`; the calling API credential needs **Management API—API credentials read and write**. See [[adyen-api-access]] and [[adyen]].

## Key takeaways

- A successful 200 returns a required `domain` and optional allowed-origin `id` and `_links`; if `_links` is present, its `self` child is marked required. The operation lists no query or request body, defaults, numerical limits, or idempotency behavior.
- This read reports configured origin data. It does not add an origin, generate a client key, establish browser-side acceptance, authenticate a future request, or prove any payment outcome.
- The page lists 400, 401, 403, 422 and 500 errors. Authentication and permission failures are explicit.

> [!warning] Contradiction
> The listed TEST server is `/v3` (raw line 14), but the 200 example's `self.href` uses `/v1/companies/` (raw line 150). The example does not establish a v3 self-link route or the correct Live route.

## Detail locators

- Purpose, caller role and TEST server: raw lines 5–14.
- Required company, credential and origin path IDs: raw lines 16–23.
- 200 response schema: raw lines 25–37.
- Error contracts: raw lines 40–137.
- Illustrative 200 response and older-version self link: raw lines 139–154.

## Related

- [[adyen-api-access]] — credential and allowed-origin context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)/2026-11-03|GET allowed origin captured 2026-11-03]]
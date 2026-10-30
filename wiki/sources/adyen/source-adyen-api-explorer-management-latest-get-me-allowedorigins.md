---
title: "Adyen Management API v3: Get allowed origins for the API credential"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/me/allowedOrigins"
raw_files:
  - "adyen/api-explorer/Management/latest/get/me/allowedOrigins/2026-09-15.md"
tags: [adyen, management-api, api-credentials, allowed-origins]
---

## Overview

Captured Management API test-server reference for `GET /me/allowedOrigins`. It returns allowed origins **for the API credential identified by the API key used in the request**. Any Management API role can make this read. An allowed origin is a credential-associated domain record; this lookup does not create an origin, rotate a client key, or list every credential's origins. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- The shown server is `https://management-test.adyen.com/v3`. The page has no query, path, or request-body parameter table; credential selection is via the request API key in the operation description.
- The 200 schema marks the top-level `data` array optional. Within an allowed-origin object, `domain` and `_links.self` are marked required, while `id` and `_links` itself are optional. Preserve that nested schema distinction; the page has no response example.
- Listed errors are 400 request parsing/understanding, 401 authentication, 403 permissions, 422 validation, and 500 server processing. The capture gives no propagation timing, current origin configuration, client-key validity, or proof that a browser origin is accepted in a live payment flow.

## Detail locators

- Credential scope, any-role permission, and test server: pinned raw lines 5–12.
- 200 response schema: `## Responses` → `### 200 Success`, lines 14–26.
- Error meanings and schemas: `## Responses`, lines 29–126.

## Related

- [[source-adyen-docs-development-resources-client-side-authentication]] — client-key and allowed-origin context, separate from this Management API read.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/me/allowedOrigins/2026-09-15|Captured GET /me/allowedOrigins API Explorer reference (2026-09-15)]]

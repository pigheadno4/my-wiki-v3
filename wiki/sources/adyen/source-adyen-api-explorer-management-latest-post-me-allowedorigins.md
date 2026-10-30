---
title: "Adyen Management API v3: add an allowed origin to the current API credential"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/me/allowedOrigins"
raw_files:
  - "adyen/api-explorer/Management/latest/post/me/allowedOrigins/2026-09-15.md"
tags: [adyen, management-api, api-credentials, allowed-origins, client-side-authentication]
---

## Overview

This captured Management API v3 test-server reference documents `POST /me/allowedOrigins`. It adds an allowed origin to the list for the API credential identified by the request's API key. This is a credential-scoped configuration operation, not a company-wide origin change. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- The page says any Management API role can make the request. The request body requires `domain`; `id` and `_links` are optional, with nested `_links.self` marked required only if the links object is supplied.
- A 200 says the request succeeded. Its response requires `domain` and may include `id` and links. This page does not specify exact domain syntax, scheme/port handling, wildcard acceptance, duplicate handling, propagation timing, or a browser-side authentication result. Follow the linked allowed-origins guidance for rules outside this endpoint schema.
- Listed errors are 400, 401, 403, 422 and 500. The captured server is `https://management-test.adyen.com/v3`; `latest` does not identify a fixed current release or prove live credential access.

## Detail locators

- Purpose, credential selection, role and test server: pinned raw lines 5–13.
- Request-body properties: pinned raw lines 17–24.
- 200 response properties: pinned raw lines 26–38.
- Error statuses and schemas: pinned raw lines 41–138. No request or response JSON examples are present in this capture.

## Related

- [[adyen-api-access]] — credential roles and scope.
- [[source-adyen-docs-development-resources-client-side-authentication]] — separate client-key and allowed-origin guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/me/allowedOrigins/2026-09-15|Captured POST /me/allowedOrigins API Explorer page]]

---
title: "Adyen Management API v3: POST /me/generateClientKey"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/me/generateClientKey"
raw_files:
  - "adyen/api-explorer/Management/latest/post/me/generateClientKey/2026-09-15.md"
tags: [adyen, management-api, client-key, api-credentials]
---

## Overview

This 2026-09-15-captured Management API v3 test-server reference defines `POST /me/generateClientKey` to generate a **client key** for authentication of requests from a payment environment. The caller's **API credential** must have the `Management API—API credentials read and write` role. The generated client key is distinct from the API credential/API key used to call the Management API; see [[adyen-api-access]].

## Key takeaways

- The new client key can be used a few minutes after generation. The old client key stops working 24 hours after the new one is generated. This rotation window is specific to the client key stated here; do not substitute the API-key rotation behavior described elsewhere.
- The 200 response requires a `clientKey` string. The snapshot documents no request parameters or body, no specific client-key scope beyond the payment environment wording, and no live-key generation result.
- Documented errors are 400 request problem, 401 authentication required, 403 insufficient permissions, 422 validation and 500 server processing failure. The 200 means the generation request succeeded; it does not prove client-side use, payment execution, or live readiness.

## Detail locators

- Purpose, propagation/old-key expiry, required role and test v3 server: raw lines 5–16.
- 200 response field: raw lines 18–26. Error schemas: raw lines 29–126.

## Related

- [[adyen-api-access]] — credential and role context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/me/generateClientKey/2026-09-15|POST /me/generateClientKey captured 2026-09-15]]

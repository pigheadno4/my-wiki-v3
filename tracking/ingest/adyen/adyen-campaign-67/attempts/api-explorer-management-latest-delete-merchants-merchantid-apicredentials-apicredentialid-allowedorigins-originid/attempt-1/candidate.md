---
title: "Adyen Management API v3: delete a merchant API credential allowed origin"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)/2026-11-05.md"
tags: [adyen, management-api, api-credentials, allowed-origins]
---

## Overview

This 2026-11-05-captured Management API reference documents `DELETE /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId}`: removal of the identified allowed origin for an API credential under a merchant account. The caller's API credential needs the `Management API—API credentials read and write` role. The listed server is TEST `https://management-test.adyen.com/v3`; the capture does not establish a Live endpoint or current account access. The page says Adyen stops accepting client-side requests from the removed domain as soon as the origin is removed. This changes allowed-origin configuration, not the API credential itself, and does not establish payment authorization or settlement. [[adyen]] [[adyen-api-access]]

## Key takeaways

- All three string path parameters are required: `merchantId` identifies the merchant account, `apiCredentialId` the API credential, and `originId` the allowed origin. The reference lists no query parameters or request body (raw lines 16–23).
- Success is HTTP 204, with no returned resource or response-body schema; the page directs the reader to the actual response code for request status (raw lines 25–28). No idempotency key, default, or numeric limit is specified in this endpoint capture.
- The immediate-effect statement concerns client-side requests from the removed domain. The reference does not report a client-request observation, restoration procedure, or broader propagation behavior (raw lines 5–7).

## Detail locators

- Purpose, immediate effect, caller role, TEST v3 server and required path identities: raw lines 5–23.
- 204 success and status instruction: raw lines 25–28.
- 400 request, 401 authentication, 403 permission, 422 validation and 500 server errors, with error-body fields: raw lines 31–128. No response examples are supplied.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)/2026-11-05|Management API DELETE merchant credential allowed origin, captured 2026-11-05]]

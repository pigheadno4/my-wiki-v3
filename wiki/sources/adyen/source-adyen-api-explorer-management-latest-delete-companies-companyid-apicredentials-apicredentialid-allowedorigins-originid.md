---
title: "Adyen Management API: delete a company API credential allowed origin"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)/2026-11-03.md"
tags: [adyen, management-api, api-credentials, allowed-origins]
---

## Overview

This 2026-11-03 Management API reference documents deletion of the allowed origin identified by `originId` under a specified company account and API credential. It requires the calling API credential's `Management API—API credentials read and write` role and lists a TEST v3 server. The page says Adyen stops accepting client-side requests from that domain as soon as the origin is removed. This is an allowed-origin configuration change, not deletion of the API credential or evidence of a payment outcome. [[adyen]] [[adyen-api-access]]

## Key takeaways

- Required string path parameters are `companyId` (company account), `apiCredentialId` (API credential), and `originId` (allowed origin). No request body or query parameters are listed (raw lines 16–23).
- The success response is HTTP 204 with no response body schema. The page directs the reader to the actual response code for request status (raw lines 25–28).
- The stated immediate effect concerns acceptance of client-side requests from the removed domain. The reference gives no restoration procedure, broader propagation timing, or live client-request observation (raw lines 5–7).

## Detail locators

- Purpose, effect, required role, TEST v3 server, and path IDs: raw lines 5–23.
- 204 success status: raw lines 25–28.
- 400 request, 401 authentication, 403 permission, 422 validation, and 500 server-error schemas: raw lines 31–128. No response examples are supplied.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/companies/(companyId)/apiCredentials/(apiCredentialId)/allowedOrigins/(originId)/2026-11-03|Management API DELETE allowed origin, captured 2026-11-03]]

---
title: "Adyen Management API v3: List allowed origins for a merchant API credential"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/2026-11-03.md"
tags: [adyen, management-api, api-credentials, allowed-origins]
---

## Overview

This captured Management API reference describes `GET /merchants/{merchantId}/apiCredentials/{apiCredentialId}/allowedOrigins`, which reads the allowed origins for the API credential identified in the path under a merchant account. The documented server is `https://management-test.adyen.com/v3`. The calling API credential must have **Management API—API credentials read and write**. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- Both string path parameters are required: `merchantId` identifies the merchant account, and `apiCredentialId` identifies the credential whose origins are listed. The reference specifies no query parameters, request body, pagination, default, or limit.
- A 200 says the read request succeeded. The response-body `data` array is optional; each returned origin has a required `domain` field, optional origin `id`, and optional `_links` whose `self` object is required if `_links` appears. The 204 success response has no additional content.
- This readback does not add or remove an origin, generate a client key, prove later client-side acceptance or successful API authentication, or establish merchant/payment eligibility. The reference documents 400, 401, 403, 422 and 500 errors. It gives no idempotency, propagation, review/approval, deletion/reversal, or downstream financial outcome contract.

> [!warning] Version conflict
> The Servers section names the TEST `/v3` base URL, while both illustrative 200 origin `self.href` links use `/v1`. This snapshot does not resolve which version a current response link would use.

## Detail locators

- Purpose, required credential role and test server: raw lines 5–14.
- Required path identifiers: raw lines 16–22.
- 200 and 204 response fields: raw lines 24–40.
- Error response schemas: raw lines 43–140.
- Illustrative origins and older-version links: raw lines 142–170.

## Related

- [[adyen-api-access]] — credential permissions and allowed-origin context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/(apiCredentialId)/allowedOrigins/2026-11-03|Adyen Management API merchant-credential allowed-origins list, captured 2026-11-03]]

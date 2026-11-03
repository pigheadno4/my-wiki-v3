---
title: "Adyen Management API v3: Generate a company credential client key"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/generateClientKey"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/generateClientKey/2026-11-03.md"
tags: [adyen, management-api, api-credentials, client-key]
---

## Overview

This 2026-11-03-captured Management API v3 reference describes `POST /companies/{companyId}/apiCredentials/{apiCredentialId}/generateClientKey`, which generates a new **client key** for the API credential identified by the company and credential path IDs. The listed server is TEST `https://management-test.adyen.com/v3`. The `latest` URL and TEST server do not establish current Live availability or caller access. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- The **calling** API credential must have `Management API—API credentials read and write`. Both string path IDs are required: `companyId` is a company-account ID and `apiCredentialId` is the target API credential ID. The page specifies no request body, query parameters, default, numeric rate limit or idempotency behavior. The target credential and the calling credential are distinct roles in the request; the page does not say they must be the same.
- A 200 says the request succeeded and requires a `clientKey` string in the response. This is client-key generation, not API-key generation or an API credential creation response. The new client key can be used a few minutes after generation; the old client key stops working 24 hours after generation. The returned key and timing statement do not prove immediate browser acceptance or successful client-side authentication.
- The page lists 400, 401, 403, 422 and 500 errors. It states no safe-retry/idempotency contract, rollback, deletion, asynchronous approval, payment authorization, capture or settlement outcome. A 200 documents successful generation for the specified target, not Live account eligibility or payment execution.

## Detail locators

- Purpose, new/old client-key timing, caller role, TEST server and both path IDs: pinned raw lines 5–22.
- 200 response field and requiredness: lines 24–32.
- Error descriptions and problem fields: lines 35–132.

## Related

- [[adyen-api-access]] — API credential and client-key scope.
- [[source-adyen-api-explorer-management-latest-post-me-generateclientkey]] — separate `/me` client-key generation reference.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/generateClientKey/2026-11-03|Company credential client-key generation snapshot]]

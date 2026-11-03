---
title: "Adyen Management API v3: Generate a company API credential key"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/generateApiKey"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/generateApiKey/2026-11-03.md"
tags: [adyen, management-api, api-credentials, api-key-rotation]
---

## Overview

The captured [[adyen]] Management API v3 TEST `POST /companies/{companyId}/apiCredentials/{apiCredentialId}/generateApiKey` returns a new API key for the target API credential in the company-account path. The calling credential must have the `Management API—API credentials read and write` role. The path company ID, target credential ID, and caller credential are distinct. This is a key-generation operation, not proof that a later request authenticates or has endpoint permission. See [[adyen-api-access]].

## Key takeaways

- The required string path parameters are `companyId` and `apiCredentialId`. The captured page shows no query or request body. The server is `https://management-test.adyen.com/v3`; it does not supply a live server URL.
- A 200 means the request succeeded and its response body requires the generated `apiKey` string. The page says the new key can be used a few minutes after generation and the old key stops working 24 hours after generation. Returning the key is distinct from a verified successful call using it.
- The page states no idempotency contract, rate limit, retry behavior, conditional input, deletion/reversal, or later approval state. Repeating a key-generation request should not be assumed harmless from this snapshot.
- This endpoint's key timing differs from the separately captured Customer Area credential guide; the 24-hour predecessor window is common to both statements, but the new-key activation time is unresolved.

> [!warning] Contradiction
> This Management API v3 reference says the new API key can be used a few minutes after generation (pinned raw line 7). The separately captured [[source-adyen-docs-development-resources-api-credentials|Adyen API credentials guide]] says a newly generated key becomes active immediately (its pinned raw line 82). Do not substitute either timing statement for the other or assume immediate usability of this API-generated key.

## Detail locators

- Purpose, key timing, caller role, TEST server and path IDs: pinned raw lines 5–22.
- 200 response and required `apiKey`: pinned raw lines 24–32.
- 400, 401, 403, 422, and 500 errors: pinned raw lines 35–132. Generic error `requestId`/`pspReference` wording is not evidence of a payment.
- The `latest` URL and 2026-11-03 TEST snapshot do not establish present availability, live eligibility, successful authentication, or payment execution.

## Related

- [[source-adyen-docs-development-resources-api-credentials]] — separately captured Customer Area credential-administration guide; conflicting new-key activation timing above.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/apiCredentials/(apiCredentialId)/generateApiKey/2026-11-03|2026-11-03 pinned API Explorer snapshot]]

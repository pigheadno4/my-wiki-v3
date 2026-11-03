---
title: "Adyen Management API v3: generate a merchant credential API key"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/generateApiKey"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/generateApiKey/2026-11-03.md"
tags: [adyen, management-api, api-credentials, api-keys, merchant-accounts]
---

## Overview

This 2026-11-03 [[adyen]] Management API reference describes `POST /merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey` for generating a new API key for the credential identified under the merchant account in the path. The calling API credential needs `Management API—API credentials read and write`. The captured server is `https://management-test.adyen.com/v3`; no live server URL is supplied here. This is key generation, not a credential-role or merchant-account activation operation or proof of successful use at another endpoint. [[adyen-api-access]]

## Key takeaways

- Required path strings are `merchantId`, the merchant account, and `apiCredentialId`, the target API credential. No query parameter, request body, default or request-count limit is documented. The operation is not described as idempotent; the reference gives no retry or duplicate-generation behavior.
- The page says the new API key can be used **a few minutes after** generation, while the old API key stops working **24 hours after** a new one is generated. Those are this endpoint's stated timing boundaries; a `200` response containing a key does not prove the new key already works or that a downstream request is authorized.
- A `200` says the request succeeded and its response body requires the generated `apiKey` string. The reference also lists `204` success without additional content, which cannot supply that documented key in a body. It lists `400`, `401`, `403`, `422` and `500` errors. It does not describe credential deletion, key-revocation controls, activation of a merchant account, payment execution or payout status.

> [!warning] Contradiction
> This merchant-credential Management API endpoint says a newly generated key is usable after **a few minutes**. The separately captured [[source-adyen-docs-marketplaces-manage-access-api-credentials-web-service|balance-platform Customer Area credential guide]] says its new API key becomes active **immediately**. Those are different credential routes; the snapshots do not establish one universal activation time. The existing [[adyen-api-access]] concept states immediate activation without this distinction.

## Detail locators

- **Purpose, new/old-key timing, caller role and captured test server:** raw lines 5–14.
- **Required merchant and credential path IDs:** raw lines 16–22.
- **200 key field and 204 no-content form:** raw lines 24–36.
- **Error response schemas:** raw lines 39–136.

## Related

- [[adyen-api-access]] — API credential scope and lifecycle.
- [[source-adyen-docs-marketplaces-manage-access-api-credentials-web-service]] — separate balance-platform Customer Area key route with different activation wording.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/apiCredentials/(apiCredentialId)/generateApiKey/2026-11-03|Management API v3 merchant API-key generation — collected 2026-11-03]]
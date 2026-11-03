---
title: "Adyen Management API v3: List merchant API credentials"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/2026-11-03.md"
tags: [adyen, management-api, api-credentials, merchant-account]
---

## Overview

This 2026-11-03-captured Management API v3 reference describes `GET /merchants/{merchantId}/apiCredentials`, a paginated list of API credentials for the merchant account identified by required path `merchantId`. The listed server is TEST `https://management-test.adyen.com/v3`; the `latest` URL and TEST server do not establish current Live availability or caller access. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- The calling API credential needs `Management API—API credentials read and write`, even for this GET. Optional query `pageSize` defaults to 10 and has maximum 100; optional `pageNumber` selects a page. No request body or idempotency behavior is specified.
- A 200 says the request succeeded. Required top-level `itemsTotal` and `pagesTotal` report counts; optional `data` holds credential records and optional `_links` holds pagination references. When pagination `_links` appears, `first`, `last` and `self` are marked required; `next` and `prev` depend on adjacent pages. A separate 204 reports successful processing with no additional content.
- Within each returned credential record, the schema requires `active`, `allowedIpAddresses`, public `clientKey`, credential `id`, `roles` and `username`. `active=true` is required to use a credential, but readback does not prove successful authentication, effective role/account access or a payment outcome. An empty allowed-IP list means requests are allowed from any IP; a nonempty list causes a security error for requests from an unlisted IP. Optional allowed-origin objects concern client-side origins, separate from server IP allowlisting.
- Optional linked resources include allowed origins, merchant, company, `generateApiKey` and `generateClientKey`. The link descriptions say a preceding key remains valid for 24 hours after a new key is generated, but this GET only lists links and does not generate or rotate keys. The response schema contains a public client key; it does not list a secret API-key value. The populated example illustrates credential records and roles, not actual grants to this caller or a Live account.
- Listed errors are 400, 401, 403, 422 and 500. The page does not describe credential creation, deactivation, deletion, propagation, asynchronous approval or version-conflict behavior for this read.

> [!warning] Contradiction
> The endpoint lists the TEST `/v3` server (raw line 14), but the sample pagination and credential-resource `href` values use `/v1` (lines 185–195 and 211–543). The example does not establish a consistent v3 resource-link contract.

## Detail locators

- Purpose, required caller role, TEST server, merchant path ID and paging parameters: pinned raw lines 5–28.
- 200 pagination, credential fields, IP/origin and key-link descriptions: lines 30–70; 204 no-content result: lines 73–74.
- Error descriptions and problem fields: lines 77–174; illustrative response and v1 links: lines 176–548.

## Related

- [[adyen-api-access]] — API credential identity, roles and account scope.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/apiCredentials/2026-11-03|Merchant API credential list snapshot]]

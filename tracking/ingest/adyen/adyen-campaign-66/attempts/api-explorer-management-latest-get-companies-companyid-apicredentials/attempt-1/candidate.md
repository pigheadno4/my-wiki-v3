---
title: "Adyen Management API v3: list company API credentials"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/2026-11-03.md"
tags: [adyen, management-api, api-credentials, pagination]
---

## Overview

This 2026-11-03-captured Management API v3 reference describes `GET /companies/{companyId}/apiCredentials`, a paged listing of API credentials for the company account identified by required path `companyId`. The listed TEST server is `https://management-test.adyen.com/v3`, and the caller's API credential requires **Management API—API credentials read and write**. See [[adyen]] and [[adyen-api-access]].

## Key takeaways

- Optional `pageSize` defaults to 10 and has a maximum of 100; optional `pageNumber` selects the page. The `200` response requires `itemsTotal` and `pagesTotal`; top-level `_links` and `data` are marked optional. Pagination links are nested under `_links`, with first/last/self marked required if that object appears and next/prev conditional on available pages.
- Each returned credential can include `id`, `username`, `clientKey`, `active`, `roles`, `allowedIpAddresses`, allowed origins, associated merchant accounts, certificate `subjectDN` and resource links. The response table marks `id`, `username`, `clientKey`, `active`, `roles` and `allowedIpAddresses` required within each `data` item, while `data` itself is optional. An empty allowed-IP list permits requests from any IP; a nonempty list blocks requests from other IPs with a security error.
- `associatedMerchantAccounts` lists explicit merchant access; when the credential has company access, access to all its merchant accounts is implied and those merchants are omitted from that list. `clientKey` is public and used for client-side authentication; it is distinct from an API key. The listed key-generation links and 24-hour old-key overlap descriptions are navigation and lifecycle context, not evidence this GET generated either key.
- A `200` listing establishes captured metadata, not successful authentication, current role entitlement, origin acceptance, key rotation, payment authorization or settlement. `400`, `401`, `403`, `422` and `500` errors are listed. This read specifies no idempotency, deletion, activation, propagation or financial outcome.

> [!warning] Contradiction
> The listed TEST server is `/v3`, but the `200` example's pagination, credential and related links use `/v1`. The example does not establish the v3 response-link paths; treat its values as illustrative.

## Detail locators

- Raw lines 5–28: purpose, role, TEST server, company ID and pagination defaults/limit.
- Raw lines 30–71: response page counts, credential fields, account-scope, IP and key-link descriptions.
- Raw lines 74–171: error schema; lines 173–521: full illustrative ten-item page and `/v1` link conflict.

## Related

- [[adyen-api-access]] — credential identity, scope and lifecycle.
- [[source-adyen-api-explorer-management-latest-overview]] — Management API orientation.
- [[source-adyen-api-explorer-management-latest-get-me]] — API-key-selected credential lookup.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/apiCredentials/2026-11-03|2026-11-03 credential-list endpoint reference]]
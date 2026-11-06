---
title: "Adyen Management API v3: list merchant webhook configurations"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/webhooks"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/webhooks/2026-11-05.md"
tags: [adyen, management-api, webhooks, merchant-account]
---

## Overview

This 2026-11-05-captured Management API reference describes `GET /merchants/{merchantId}/webhooks`: a paged list of webhook configurations for the identified merchant account. It explicitly excludes configurations for the merchant's parent company account. The listed server is `https://management-test.adyen.com/v3`. The calling API credential needs either **Management API—Webhooks read** or **Management API—Webhooks read and write**. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- `merchantId` is the required merchant-account path ID. Optional integer query parameters are `pageSize` (default 10, maximum 100) and `pageNumber`; the reference specifies no request body.
- A `200` response requires `itemsTotal` and `pagesTotal`. `data`, `accountReference` and pagination `_links` are optional. If pagination `_links` appears, `first`, `last` and `self` are required within it, while `next` and `prev` depend on page availability.
- For each webhook object, the response table marks `active`, `communicationFormat`, `type` and `url` required. `active=true` is necessary to receive account events according to the field description; listing that flag does not prove delivery, receipt, event correctness or payment outcome. Other fields include optional ID, account reference, certificate flags, error flag, HMAC-key check value, additional settings and resource links; their definitions and conditional details remain in the raw table.
- The reference also lists `204` success with no additional content and `400`, `401`, `403`, `422` and `500` error classes. A readback neither creates or changes a webhook nor executes the example's HMAC-generation or test links.

> [!warning] Contradiction
> The listed TEST server uses `/v3`, but the `200` example's pagination and webhook resource links use `/v1`. Those example URLs do not resolve the current versioned route or a Live route.

## Detail locators

- Raw opening paragraphs and `## Servers`: merchant-only scope, parent-company exclusion, caller roles and TEST host.
- Raw `## Parameters`: required merchant ID and pagination defaults/maximum.
- Raw `## Responses > ### 200 Success`: pagination, webhook object fields, conditional company-level schema fields, TLS/format/type options and response-requiredness.
- Raw `## Responses > ### 204 Success` and error sections: no-content and failure shapes.
- Raw `## Response examples > ### 200 Success`: illustrative single webhook and version-conflicting links; sample values are not general defaults.

## Related

- [[adyen-webhooks]] — webhook delivery concepts and source routes.
- [[source-adyen-api-explorer-management-latest-overview]] — Management API family overview.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/webhooks/2026-11-05|GET merchant webhooks, captured 2026-11-05]]
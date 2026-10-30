---
title: "Adyen Balance Platform API v2: GET /scaAssociations"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/scaAssociations"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/scaAssociations/2026-09-15.md"
tags: [adyen, balance-platform, sca, api-reference]
---

## Overview

This captured Balance Platform API v2 test-server reference defines `GET /scaAssociations`: a paginated read of SCA device associations for a specified entity. It is an API Explorer `latest` URL captured on 2026-09-15, not evidence of the currently served version or live access. The entity is selected by `entityId` and `entityType`; the allowed types here are `accountHolder`, `legalEntity`, and `paymentInstrument`. These are distinct resource identities in [[adyen-platforms|Adyen for Platforms]].

## Key takeaways

- The query-parameter table marks `pageNumber`, `pageSize`, `entityId`, and `entityType` required, while giving defaults of zero and five for the first two. This apparent required/default tension is left as documented; the snapshot does not establish omission behavior. The first page index is zero.
- A successful response has `data`, `itemsTotal`, `pagesTotal`, and `_links`. Each association has a device ID and type, entity ID and type, creation time, and `status` of `active` or `pendingApproval`; a human-readable device name is optional. The response indicates listed associations and their reported statuses, not that a pending device has been approved or verified.
- Documented errors are 400 invalid input, 401 authentication required, 403 insufficient permissions, and 500 server processing failure. The page does not name a credential role or grant access to a particular entity. This read endpoint does not establish creation, deletion, propagation timing, payment execution, or funds movement.

## Detail locators

- Query parameters, allowed entity types, and defaults: raw `## Parameters` / `### Query parameters`, lines 12–20.
- Response fields, pagination links, and association statuses: raw `### 200 Success`, lines 24–50.
- Error response structures: raw `### 400 Client Error` through `### 500 Server Error`, lines 53–126.
- Illustrative two-association account-holder response: raw `## Response examples`, lines 128–163; the sample IDs and statuses are examples, not a guaranteed result.

## Related

- [[adyen-platforms]] — platform entity context.
- [[adyen-api-access]] — general credential context; endpoint permission requirements are limited to the 401/403 descriptions in this snapshot.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/scaAssociations/2026-09-15|GET /scaAssociations captured 2026-09-15]]

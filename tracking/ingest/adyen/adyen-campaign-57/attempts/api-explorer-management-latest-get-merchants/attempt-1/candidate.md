---
title: "Adyen Management API GET /merchants — accessible merchant accounts"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/2026-09-15.md"
tags: [adyen, management-api, merchant-accounts, pagination, api-access]
---

## Overview

This 2026-09-15 Management API Explorer capture documents `GET /merchants` on the `/v3` test server. It lists merchant accounts accessible to the calling API credential, in pages. The required credential role is `Management API—Account read`. A list read is scoped by credential access and does not create a merchant account or prove live enablement.

## Key takeaways

- Optional `pageSize` defaults to 10 and has a maximum of 100; `pageNumber` selects a page. The 200 schema requires `itemsTotal` and `pagesTotal`, while `data` and pagination `_links` are optional; `first`, `last` and `self` are required within `_links` when it is present, and `next`/`prev` are conditional on adjacent pages.
- Merchant entries can include company ID, merchant ID, legal-entity name/city, capture delay, shopper interaction, settlement currency, data-center prefixes, status and related resource links. The status descriptions distinguish `PreActive`, `Active`, `InactiveWithModifications`, `Inactive` and irreversible `Closed`; payment processing and payouts at `Active` additionally require the company account to be `Active`. A returned status is a captured account field, not proof of successful payment or payout.
- The page also lists 204 success with no content, plus 400, 401, 403, 422 and 500 errors. The 200 example's links use `/v1` despite the `/v3` server; one sample `status` contains a merchant-name placeholder, one card-like `captureDelay` uses lower-case values while the schema capitalizes labels, and one item's link path uses its merchant name in place of its ID. Treat the example as illustrative, not authoritative URL/status values.
- Test data-center prefixes are described as empty, with `default` returned in test. The reference does not establish current live URL prefixes, actual credential scope, merchant creation, company activation, payment execution or bank receipt.

## Detail locators

- `## Servers`, `## Parameters` → captured test base, role and page controls.
- `## Responses` → 200/204 response forms, merchant fields/status semantics and generic errors.
- `## Response examples` → illustrative page and the version, status and link inconsistencies.

## Related

- [[adyen]] — provider.
- [[adyen-account-structure]] — company and merchant account hierarchy.
- [[adyen-api-access]] — API credential role and scope context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/2026-09-15|2026-09-15 captured API Explorer reference]]

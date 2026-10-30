---
title: "Adyen Management API v3: list stores"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/stores"
raw_files:
  - "adyen/api-explorer/Management/latest/get/stores/2026-09-15.md"
tags: [adyen, management-api, pos, stores, pagination, api]
---

## Overview

This 2026-09-15-captured Management API v3 reference documents `GET /stores`, a paged read of store records. The listed server is `https://management-test.adyen.com/v3`. The page requires an API credential with **Management API—Stores read** or **Management API—Stores read and write** role; the response is limited to the stores accessible to that credential, not proof of operational readiness. See [[adyen]] and [[adyen-pos-store-management]].

## Key takeaways

- The optional query filters are merchant-account `merchantId` and store `reference`; `pageSize` defaults to 10 and is capped at 100, while `pageNumber` selects a page. The response marks `itemsTotal` and `pagesTotal` required, while top-level `_links` and `data` are optional. Within `_links`, first/last/self are marked required if that object appears; next/prev are conditional.
- A store entry can include Adyen-generated `id`, owning `merchantId`, store `reference`, address, business-line IDs, localized shopper statements, split configuration and sub-merchant data. The response table's conditional descriptions for address/state, business lines, external references and sub-merchant fields should not be mistaken for query requirements of this read; use the raw field rows for their exact scope.
- The `status` field is optional in the response schema and may be `active`, `inactive` or `closed`. The reference says active is assigned automatically on creation; inactive blocks terminals under the store from accepting new transactions while outstanding captures remain possible; closed is irreversible and reassigns terminals to merchant inventory. Reading a status does not create a store, activate a terminal, configure a payment method or prove a successful POS transaction.
- The page notes live-environment rate limits without giving numbers. It lists `400`, `401`, `403`, `422` and `500` errors. Its `200` example is internally inconsistent: links use **v1 merchant-scoped** paths although the listed server is **v3 `/stores`**, and `pagesTotal: 1` accompanies a last/next link to page 2 and two records despite `pageSize=1`. Treat the example as illustrative, not an implementation endpoint or pagination invariant.

## Detail locators

- Purpose, role requirement, live rate-limit note and v3 test server: raw lines 5–18.
- Optional filters and page controls: lines 20–28.
- Response page counts, links, store identity, field conditions and statuses: lines 30–80.
- Error meanings and problem-body schema: lines 83–180.
- Inconsistent v1 paths, page counts and illustrative stores: lines 182–251.

## Related

- [[adyen-pos-store-management]] — store administration and operational lifecycle.
- [[adyen-terminal-management]] — separate terminal assignment and boarding context.
- [[source-adyen-docs-point-of-sale-design-your-integration-determine-account-structure-automate-store-management]] — broader Management API automation guide.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/stores/2026-09-15|GET /stores API Explorer capture]]

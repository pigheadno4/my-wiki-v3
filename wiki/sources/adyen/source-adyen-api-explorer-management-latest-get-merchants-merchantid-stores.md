---
title: "Adyen Management API v3: List stores for a merchant account"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/stores"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/stores/2026-11-03.md"
tags: [adyen, management-api, stores, point-of-sale]
---

## Overview

This 2026-11-03-captured Management API v3 reference describes `GET /merchants/{merchantId}/stores`, a paginated list of stores for the merchant account named by required path `merchantId`. The listed server is TEST `https://management-test.adyen.com/v3`; Live requests are said to have rate limits, but this page gives no numeric limit. The `latest` URL and TEST server do not establish current Live availability or caller access. See [[adyen]] and [[adyen-pos-store-management]].

## Key takeaways

- The calling API credential must have either `Management API—Stores read` or `Management API—Stores read and write`. The required `merchantId` is a merchant-account identifier, not a company, legal-entity or store ID. Optional query `reference` filters by store reference; optional `pageSize` defaults to 10 and has a maximum of 100; optional `pageNumber` selects a page. No request body or idempotency behavior is specified for this GET.
- A 200 says the request succeeded. Required top-level `itemsTotal` and `pagesTotal` report counts; optional `data` contains store objects and optional `_links` contains pagination references. Within a present `_links`, `first`, `last` and `self` are marked required, while `next` and `prev` are conditional on adjacent pages. A separate 204 denotes successful processing with no additional content. A successful response therefore does not guarantee a populated store list.
- Listed store fields include Adyen-generated store `id`, `merchantId`, `reference`, address, business-line IDs, external reference, shopper-statement fields, optional split-configuration IDs, `status`, and conditional sub-merchant data. These are response-schema fields, not additional GET inputs. The raw table has optional parent objects with required nested fields and country/business-line/external-reference conditions; consult the schema before using individual values.
- The `status` description says new stores are automatically `active`; `inactive` blocks new terminal transactions while outstanding capture remains possible; `closed` is irreversible and reassigns terminals to merchant inventory. Listing a status is readback, not evidence that this GET created, changed or closed a store, boarded a terminal, enabled payment methods, authorized a payment or completed capture. Generic errors include 400, 401, 403, 422 and 500.

> [!warning] Contradiction
> The endpoint lists the TEST `/v3` server (raw line 18), but the sample pagination and store `href` values use `/v1` (lines 200–209, 233, 254). The example also reports `itemsTotal: 2`, `pagesTotal: 1` while linking a last/next page 2 with `pageSize=1` (lines 200–214). Do not treat those example links or counts as a consistent v3 pagination contract.

## Detail locators

- Purpose, required role, Live rate-limit notice, server, path and query parameters: pinned raw lines 5–33.
- 200 pagination and store response schema, including nested conditions and status semantics: lines 35–85; 204 no-content response: lines 88–89.
- Error descriptions and problem fields: lines 92–189; inconsistent illustrative 200 response: lines 191–259.

## Related

- [[adyen-pos-store-management]] — store administration and terminal-readiness context.
- [[adyen-api-access]] — API credential and role context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/stores/2026-11-03|Merchant store list snapshot]]

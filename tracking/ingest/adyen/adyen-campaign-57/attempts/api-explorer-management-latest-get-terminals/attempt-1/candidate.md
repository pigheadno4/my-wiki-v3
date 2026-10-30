---
title: "Adyen Management API: list terminals"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/terminals"
raw_files:
  - "adyen/api-explorer/Management/latest/get/terminals/2026-09-15.md"
tags: [adyen, management-api, terminals, point-of-sale, api-reference]
---

## Overview

Captured Management API v3 test-server `GET /terminals` reference. It lists payment terminals accessible to the API credential and matching the supplied filters. The credential needs the **Management API — Terminal actions read** role. This is fleet inventory and assignment information, not proof of a device's live connectivity or successful transaction. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- All query parameters are optional. `pageSize` defaults to 20 and has a maximum of 100; `pageNumber` chooses the page. Filters cover brand/model, store IDs, merchant IDs and countries. `otpQuery` or `searchQuery` causes other query parameters to be ignored; `searchQuery` matches terminal IDs containing the given text.
- A 200 response requires `itemsTotal` and `pagesTotal`; `_links` and `data` are optional. Where `_links` is present, its `first`, `last`, and `self` objects are marked required, with `next`/`prev` conditional on page availability. Returned terminal details can include terminal `id`, model, serial number, firmware, store/merchant/company assignment, and connectivity information. Do not conflate these IDs with each other.
- Assignment status distinguishes `inventory` (cannot process transactions), `boarded` (boarded to store or store-representing merchant account and can process transactions), `deployed`, and `reassignmentInProgress` (wait for synchronization). An inventory read does not prove a particular terminal is online, synchronized, fully configured, or able to complete a payment. Last-activity and last-transaction timestamps are omitted when older than 14 days.
- The sample includes a `next` link while `pagesTotal` is 1. Treat sample pagination as illustrative; use the response schema and actual links rather than inferring a guaranteed next page.

## Detail locators

- Raw `## Parameters` / `### Query parameters`: all filters, precedence, and paging values.
- Raw `## Responses` / `### 200 Success`: assignment-state meanings, nested terminal fields, page links and counts.
- Raw `## Response examples`: illustrative terminal and link object; error schemas under 400/401/403/422/500.

## Related

- [[source-adyen-docs-point-of-sale-automating-terminal-management-assign-terminals-api]] — reassignment and boarding flow.
- [[adyen-payment-terminals]] — physical terminal context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/terminals/2026-09-15|Management API v3 GET /terminals reference (2026-09-15 capture)]]

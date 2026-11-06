---
title: "List merchant terminal-theme metadata (Adyen Management API)"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalThemes"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalThemes/2026-11-07.md"
tags: [adyen, management-api, terminal-themes, point-of-sale]
---

## Overview

This 2026-11-07 Management API `latest` reference documents `GET /merchants/{merchantId}/terminalThemes`: a paginated list of terminal-theme metadata for the merchant account in the path. The listed server is Test `/v3`, and the API credential needs `Management API - Terminal themes read and write`.

## Key takeaways

- `merchantId` is required. Optional `search` filters theme names by case-insensitive substring; `page` defaults to 1 and `pageSize` to 10 themes per page. The `422` example shows a `pageSize` of 200 rejected with a message saying 1–100, but the query-parameter table states no formal range.
- A `200` response has required `data` and `hasNextPage`. Each listed theme has required `id`, `name` and display `mode` (`dark` or `light`). `hasNextPage` signals more pages after this one.
- The list excludes image and video assets. The reference directs a separate theme-detail GET for the asset URLs. Listing metadata does not establish a theme's assignment, installation, effective display on a terminal, or payment readiness.
- The reference lists `400`, `401`, `403`, `404`, `422` and `500` errors. Its `403` example describes no access to the requested account, and its `404` example cannot distinguish missing from inaccessible account.

## Detail locators

- Raw lines 5–29: purpose, metadata-only boundary, role, Test server, merchant ID and optional filters/defaults.
- Raw lines 31–67: `200` fields and documented error status headings.
- Raw lines 69–173: illustrative success/error bodies, including the `pageSize` validation message at lines 144–160.

## Related

- [[adyen]]
- [[adyen-android-terminals]]
- [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalThemes/2026-11-07|GET merchant terminal themes, 2026-11-07 capture]]

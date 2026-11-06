---
title: "Adyen Management API: Update a store terminal logo"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/stores/(storeId)/terminalLogos"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/stores/(storeId)/terminalLogos/2026-11-07.md"
tags: [adyen, management-api, terminal-management, store, terminal-logo]
---

## Overview

This 2026-11-07 capture of Adyen's Management API `latest` PATCH reference lists a TEST `/v3` server. It updates the logo configured at a store for one payment terminal model per request. The store-model logo applies to terminals of that model under the store unless an individual terminal has a different logo. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- `storeId` is a required path parameter and `model` a required query parameter. The captured model enumeration is in the raw parameter table.
- The body table marks `data` optional. To change the logo, supply a Base64-encoded image string; an empty logo value restores inheritance from a higher merchant or company account. The examples show `{"data": ""}` for removal.
- The API credential needs **Management API—Terminal settings read and write**. The page notes Live rate limits, while its listed server is TEST `https://management-test.adyen.com/v3`.
- A `200 Success` means the request succeeded; the response body table marks `data` optional. The removal example depicts inherited image data, but does not guarantee that field in every response or establish on-device display. This configuration response does not establish payment execution.

## Detail locators

- Path, query and body fields: raw **Parameters**, lines 23–40.
- Removal/upload examples and success schema: raw **Request examples** and **Responses**, lines 42–65.
- Error statuses and fields: raw **Responses**, lines 68–165 (400, 401, 403, 422, 500).
- Example response shapes: raw **Response examples**, lines 167–182.

## Related

- [[adyen-terminal-management]] — terminal fleet configuration and its device-state boundary.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/stores/(storeId)/terminalLogos/2026-11-07|Management API store terminal-logo PATCH (2026-11-07)]]

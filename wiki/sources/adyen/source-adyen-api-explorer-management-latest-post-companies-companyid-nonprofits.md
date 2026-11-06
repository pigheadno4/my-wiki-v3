---
title: "Adyen Management API: list compatible Giving nonprofits"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/nonprofits"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/nonprofits/2026-11-07.md"
tags: [adyen, management-api, giving, nonprofits]
---

## Overview

This captured [[adyen]] Management API `latest` reference documents `POST /companies/{companyId}/nonprofits` on the v3 test server. Despite its POST method, it **returns a list** of supported nonprofit organizations to choose from for a Giving campaign; the list is restricted to nonprofits compatible with all account holders supplied in the request. It does not create a nonprofit or campaign. See [[adyen-giving]].

## Key takeaways

- Required path `companyId` identifies the company account. Required body `accountHolderIds` supplies the account holders for compatibility filtering. Optional query filters are UN Sustainable Development Goal, page number, page size (default 10, maximum 100), and search term (maximum 100 characters). The raw does not state an operation-specific credential role.
- A `200` response requires `itemsTotal` and `pagesTotal`. The `nonprofits` array and `_links` object are optional. If nonprofit entries are returned, their cause and organization metadata are described in the raw table; cause `id` and nonprofit `id` are separately optional Adyen-generated identifiers.
- The result is a documented compatibility list for the supplied account-holder IDs, not evidence of nonprofit verification, current account eligibility, campaign creation or activation, donation success, settlement, or bank receipt. A `503` says campaign management is temporarily unavailable for the account while donations themselves are unaffected.

## Detail locators

- `## Parameters` → path, query, and request-body tables: company and account-holder identities, goal/search filters, pagination defaults and limits.
- `## Responses` → `200 Success`: totals, optional links/list, nonprofit metadata and nested causes.
- `## Responses` → `400`, `401`, `403`, `422`, `500`, and `503`: failure categories; error-envelope top-level fields are optional.

## Related

- [[adyen]]
- [[adyen-giving]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/nonprofits/2026-11-07|Management API compatible nonprofit list, captured 2026-11-07]]

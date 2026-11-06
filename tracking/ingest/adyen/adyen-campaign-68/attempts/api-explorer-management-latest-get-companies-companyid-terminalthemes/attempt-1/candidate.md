---
title: "Adyen Management API: list company terminal themes"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalThemes"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalThemes/2026-11-07.md"
tags: [adyen, management-api, android-terminals, terminal-themes]
---

## Overview

This 2026-11-07 Management API `latest` reference describes `GET /companies/{companyId}/terminalThemes` on the listed TEST `/v3` server. It lists theme metadata for the selected company and its associated merchant accounts, with pagination. Images and videos are absent; the reference directs a separate theme-detail GET to obtain asset URLs. Listing a theme does not apply it to a terminal or establish on-device display. See [[adyen]] and [[adyen-android-terminals]].

## Key takeaways

- `companyId` is the required path ID of the company account. The API credential needs `Management API - Terminal themes read and write`. Optional `search` filters theme names by case-insensitive substring; `page` starts at 1 by default; `pageSize` defaults to 10. The parameter table states no `pageSize` maximum, although a `422` example rejects `200` with a message saying `1` to `100`; treat that as an illustrative validation example, not a complete limit contract.
- `200` has required `data` for the requested page and required `hasNextPage`. Each theme entry requires unique `id`, `name`, and display `mode` of `dark` or `light`. The list contains metadata only. `hasNextPage` signals more list pages, not applied themes or downloaded assets.
- Documented errors are `400`, `401`, `403`, `404`, `422`, and `500`; examples show inaccessible-account wording for `403` and `404`. Neither a list result nor its example verifies theme application, terminal software compatibility, display, payment activity, or current Live eligibility.

## Detail locators

- Purpose, role, TEST server, path and query parameters: pinned raw lines 5–29.
- `200` required list metadata and pagination field, and error headings: pinned raw lines 31–67.
- Illustrative success and error payloads: pinned raw lines 69–173, including the `422` `pageSize` example at lines 144–162.

## Related

- [[adyen-android-terminals]] — Android terminal theme and deployment context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalThemes/2026-11-07|2026-11-07 pinned company terminal themes list reference]]
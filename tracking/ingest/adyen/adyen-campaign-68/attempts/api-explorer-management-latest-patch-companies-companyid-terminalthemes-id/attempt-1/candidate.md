---
title: "Adyen Management API: update terminal-theme metadata"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/terminalThemes/(id)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/companies/(companyId)/terminalThemes/(id)/2026-11-07.md"
tags: [adyen, management-api, android-terminals, terminal-themes]
---

## Overview

This captured [[adyen]] Management API `latest` reference documents `PATCH /companies/{companyId}/terminalThemes/{id}` on the v3 test server. It changes terminal-theme metadata: the name and dark/light display mode. It does not describe changing theme assets or applying the theme to a terminal. See [[adyen-android-terminals]].

## Key takeaways

- Required path `companyId` identifies the company account and `id` the theme. The credential needs `Management API - Terminal themes read and write`.
- The request body marks both `mode` and `name` optional. `mode` permits `dark` or `light`; `name` is typed `string,null` and must be unique per account within the same company context. The reference does not define empty-body behavior or what a null name does.
- `200 OK` requires response `id`, `mode`, and `name`. Error responses listed are `400`, `401`, `403`, `404`, `422`, and `500`. The `422` example illustrates a duplicate-name validation error; the example does not establish all possible errors.
- Successful metadata readback does not establish that any asset changed, any theme was assigned or applied, or a device displayed it.

## Detail locators

- `## Parameters` → path parameters and request body: company/theme IDs, optional name/mode, uniqueness and allowed mode values.
- `## Request examples` → `update-terminal-theme-request`: illustrative name/mode update.
- `## Responses` → `200 Success` and the listed error statuses.
- `## Response examples` → `200 Success` and error examples, including owner/company lookup and duplicate-name cases.

## Related

- [[adyen]]
- [[adyen-android-terminals]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/terminalThemes/(id)/2026-11-07|Management API terminal-theme metadata PATCH, captured 2026-11-07]]

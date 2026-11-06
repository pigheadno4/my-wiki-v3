---
title: "Adyen Management API: Delete a terminal theme"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/companies/(companyId)/terminalThemes/(id)"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/companies/(companyId)/terminalThemes/(id)/2026-11-07.md"
tags: [adyen, management-api, android-terminals, terminal-themes]
---

## Overview

This 2026-11-07-captured Management API `latest` reference lists a TEST `/v3` server for `DELETE /companies/{companyId}/terminalThemes/{id}`. It deletes the theme identified by `id` under the company account identified by `companyId`. [[adyen]] [[adyen-android-terminals]]

## Key takeaways

- If the theme is currently in use, first deactivate it with `/companies/{companyId}/terminalThemes/unapply` before deleting it. The page states no other deletion precondition.
- Both `companyId` and theme `id` are required path parameters. The caller's API credential needs **Management API - Terminal themes read and write**. No query parameter or request body is listed.
- `204` is described as “Theme deleted” and has no response body in this reference. It does not describe asset retention or deletion, device propagation, or what a terminal displays after deletion.
- The listed errors are `401` unauthorized, `403` forbidden, `404` not found, `409` conflict, and `500` internal server error. Their JSON examples are illustrative; the page provides no more specific `409` condition.

## Detail locators

- Deletion and unapply condition, caller role, TEST server: raw lines 5–14.
- Required path parameters and `204`: raw lines 16–27.
- Error statuses and examples: raw lines 30–112.

## Related

- [[adyen-android-terminals]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/companies/(companyId)/terminalThemes/(id)/2026-11-07|DELETE company terminal theme, captured 2026-11-07]]

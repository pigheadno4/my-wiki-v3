---
title: "Management API v3: delete a merchant terminal theme"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/terminalThemes/(id)"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/terminalThemes/(id)/2026-11-07.md"
tags: [adyen, management-api, terminal-themes, deletion]
---

## Overview

This captured Management API v3 TEST reference describes `DELETE /merchants/{merchantId}/terminalThemes/{id}`, which deletes the identified terminal theme for a merchant account. A theme currently in use must first be deactivated through `/merchants/{merchantId}/terminalThemes/unapply` before deletion. The credential needs the Management API - Terminal themes read and write role. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- Both path values are required: `merchantId` identifies the merchant account and `id` identifies the theme. The page lists the TEST host `https://management-test.adyen.com/v3`; it supplies no live host.
- A 204 success says "Theme deleted" and defines no response body. Deletion is destructive, and this endpoint does not state a restore path or propagation timing.
- The listed errors are 401 unauthorized, 403 forbidden, 404 not found, 409 conflict, and 500 internal server error. Error JSON is illustrative; the 404 example refers to an account not found or not accessible and does not establish every possible cause of 404.

## Detail locators

- Purpose, in-use prerequisite, role, and TEST server: raw lines 5–14.
- Required path parameters: raw lines 16–22.
- Success and error status definitions: raw lines 24–47.
- Error response examples: raw lines 49–113.

## Related

- [[adyen-terminal-management]] — Management API terminal administration.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/terminalThemes/(id)/2026-11-07|Management API v3 merchant terminal-theme deletion (2026-11-07)]]

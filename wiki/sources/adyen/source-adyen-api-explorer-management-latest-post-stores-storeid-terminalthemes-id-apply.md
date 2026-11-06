---
title: "Apply a terminal theme to a store"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/stores/(storeId)/terminalThemes/(id)/apply"
raw_files:
  - "adyen/api-explorer/Management/latest/post/stores/(storeId)/terminalThemes/(id)/apply/2026-11-07.md"
tags: [adyen, management-api, terminal-themes, android-terminals]
---

## Overview

Captured Management API `latest` v3 TEST POST reference for applying a theme by ID across Android terminals under a store. An individual terminal's different theme takes precedence. See [[adyen]] and [[adyen-android-terminals]].

## Key takeaways

- The path requires the store's `storeId` and terminal theme `id`. The API credential needs the Management API - Terminal themes read and write role. The captured server is `https://management-test.adyen.com/v3`.
- The 403 response example says the theme must be owned by the merchant account to which the store or terminal belongs, or by the company. This is an example's stated ownership condition, not evidence that every supplied ID passes it.
- The documented success is `200 OK` with no response body shown. It confirms this request's success, not theme readback, propagation timing, or visible application on each device. The reference lists 401, 403, 404 and 500 errors; the 404 example says the account was not found or accessible.
- This operation applies a theme assignment. The reference does not describe deleting a theme, changing individual-terminal overrides, payment execution or a reversal procedure.

## Detail locators

- Purpose, terminal override, required role and TEST v3 server: raw lines 5–14.
- Required path IDs and 200 response: raw lines 16–27.
- Error status list and 403 ownership / 404 access examples: raw lines 30–97.

## Related

- [[adyen-android-terminals]] — terminal themes and Android terminal context.
- [[adyen-terminal-management]] — fleet administration context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/stores/(storeId)/terminalThemes/(id)/apply/2026-11-07|Store terminal-theme apply reference, captured 2026-11-07]]
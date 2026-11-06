---
title: "Adyen Management API: unapply a store terminal theme"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/stores/(storeId)/terminalThemes/unapply"
raw_files:
  - "adyen/api-explorer/Management/latest/post/stores/(storeId)/terminalThemes/unapply/2026-11-07.md"
tags: [adyen, management-api, terminal-themes, point-of-sale]
---

## Overview

This 2026-11-07-captured Management API `latest` v3 TEST POST reference resets the terminal-theme assignment for the store identified by `storeId`. It changes the store assignment; the theme resource remains unchanged and is not deleted. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- After the store assignment is removed, Android terminals under the store switch to the custom theme at the next higher applied level (merchant account or company), or to the default Adyen theme. An individually applied custom theme remains in use on that terminal.
- The only documented input is the required string path parameter `storeId`. The access instructions require an API credential with `Management API - Terminal themes read and write`. No request body, query parameter, default, or propagation time is specified.
- If the store has no custom theme applied, the endpoint still returns `200 OK` without error. The `200` example contains `status: "success"`; that response is not an on-device readback or proof that any terminal has already switched themes.
- Listed errors are 401, 403, 404, and 500. The 403 example describes lack of access to the requested account; the 404 example says the account cannot be found or accessed. The response does not report a deleted theme, terminal status, or payment outcome.

## Detail locators

- Pinned raw, lines 5–18: assignment reset, inheritance, individual-terminal exception, preserved theme, no-op `200`, role, and TEST v3 server.
- Pinned raw, lines 20–46: path parameter and response statuses.
- Pinned raw, lines 48–109: illustrative `200` and error bodies, including account-access details.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/stores/(storeId)/terminalThemes/unapply/2026-11-07|Store terminal-theme unapply reference, captured 2026-11-07]]

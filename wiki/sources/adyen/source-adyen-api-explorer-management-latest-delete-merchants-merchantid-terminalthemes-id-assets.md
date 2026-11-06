---
title: "Adyen Management API: delete a merchant terminal-theme asset"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/merchants/(merchantId)/terminalThemes/(id)/assets"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/terminalThemes/(id)/assets/2026-11-07.md"
tags: [adyen, management-api, terminal-themes, terminal-assets]
---

## Overview

Captured [[adyen]] Management API `DELETE /merchants/{merchantId}/terminalThemes/{id}/assets` reference, with a v3 test server. It deletes one asset from a terminal theme owned by the merchant account in the path. The required `type` and `model` query parameters identify that asset; `merchantId` and theme `id` are required path identifiers. The API credential needs the **Management API - Terminal themes read and write** role.

## Key takeaways

- A logo uses `type=logo` and `model=All`. Deletion is blocked if the theme owner cannot edit logos. Other screen types require a single Android terminal model; `idleScreen` and `shopperEngagementScreen` support only SFO1 or M450.
- The documented 204 means the asset was deleted. The reference does not state when a terminal displays a changed theme or whether an applied theme is automatically updated on device.
- The reference lists 401, 403, 404, 422, and 500 failures. Its 403 example illustrates the logo edit prohibition; 404 illustrates a missing type/model asset. Example details are not guaranteed error text.

## Detail locators

- Test v3 server, role, and required path/query parameters: raw lines 7–31. The complete `type` screen list and model restrictions are in lines 30–31.
- Response statuses: raw lines 33–56; error examples: raw lines 58–129.

## Related

- [[adyen-terminal-management]] — terminal fleet and theme administration boundary.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/merchants/(merchantId)/terminalThemes/(id)/assets/2026-11-07|Merchant terminal-theme asset deletion, 2026-11-07]]

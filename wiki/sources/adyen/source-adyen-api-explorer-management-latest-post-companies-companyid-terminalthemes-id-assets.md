---
title: "Adyen Management API: Add a terminal-theme asset"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/assets"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/assets/2026-11-07.md"
tags: [adyen, management-api, terminal-management, terminal-themes]
---

## Overview

Captured Management API v3 reference for adding an image or video asset to the terminal theme identified by theme `id` under company account `companyId`. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- Required query `type` selects a screen type or element and required `model` selects the Android terminal model; the request uses multipart/form-data with one required `file` part declaring a supported Content-Type. The permitted type/model/media combinations are constrained: `logo` uses `All`, while certain screen types and video are limited to SFO1 or M450. Consult the raw mapping before uploading.
- Asset size is at most 100 MB for SFO1/M450 or 10 MB for other models. Generic or missing file Content-Type is rejected with `422`. An existing asset for the same type/model combination makes this add request fail; use the separate replace endpoint.
- The credential needs **Management API - Terminal themes read and write**. The endpoint is rate limited; the captured server is `https://management-test.adyen.com/v3`.
- `201` returns required `model`, `type` and tokenized CDN `url`, with the URL valid for 24 hours. Asset creation and a returned URL do not themselves state that the theme was applied to terminals or displayed on devices.

## Detail locators

- Type/model media restrictions, size and duplicate behavior: raw lines 5–23.
- Credential, server, required path/query and file fields: raw lines 25–51.
- `201` schema and 400, 401, 403, 404, 422, 429, 500 errors: raw lines 53–91; response examples: lines 93–210.

## Related

- [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/assets/2026-11-07|Management API v3 terminal-theme asset add reference]]

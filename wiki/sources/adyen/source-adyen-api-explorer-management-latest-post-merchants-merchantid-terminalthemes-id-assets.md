---
title: "Adyen Management API: add a merchant terminal-theme asset"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets/2026-11-07.md"
tags: [adyen, management-api, terminal-management, terminal-themes]
---

## Overview

This captured Management API v3 reference adds an image or video asset to a terminal theme owned by the merchant account identified by `merchantId`; `id` identifies the theme. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- Required query parameters `type` and `model` choose the screen element and Android terminal model. Upload the asset as multipart/form-data with one required `file` part declaring a supported, specific Content-Type. The type/model/media combinations are constrained: `logo` uses `All`; `idleScreen`, `shopperEngagementScreen`, and video are limited to SFO1 or M450. See the raw mapping for the remaining image formats and model constraints.
- The size limit is 100 MB for SFO1 or M450, and 10 MB for other models. A generic or missing file Content-Type is rejected with `422`. Adding a duplicate `type`/`model` combination fails; use the separate replace endpoint.
- The credential needs **Management API - Terminal themes read and write**. This endpoint is rate limited; the captured server is `https://management-test.adyen.com/v3`.
- `201 Created` returns required `model`, `type`, and a CDN `url` with a token query parameter, valid for 24 hours. The creation response does not establish that a theme has been applied to a terminal or displayed on a device.

## Detail locators

- Purpose, media mapping, limits, duplicate behavior and credential role: raw lines 5–27.
- Test server, required path and query parameters, and multipart file field: raw lines 29–51.
- `201` response schema, error statuses and illustrative response bodies: raw lines 53–210, including duplicate and file-size `422` examples at lines 157–185.

## Related

- [[adyen-terminal-management]] — Terminal fleet administration and theme context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets/2026-11-07|Management API v3 merchant terminal-theme asset add reference]]

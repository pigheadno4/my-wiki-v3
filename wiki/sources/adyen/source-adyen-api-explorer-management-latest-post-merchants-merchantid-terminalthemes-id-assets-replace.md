---
title: "Adyen Management API: replace a merchant terminal-theme asset"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets/replace"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets/replace/2026-11-07.md"
tags: [adyen, management-api, terminal-themes, terminal-assets, point-of-sale]
---

## Overview

This 2026-11-07-captured Management API `latest` reference describes replacing an existing image or video asset in a terminal theme owned by the merchant account in the path. The listed server is TEST `/v3`; the endpoint is rate limited in Live. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- Required path parameters are merchant-account `merchantId` and terminal-theme `id`. Required query parameters `type` and `model` select the existing asset. Replacement works only when the theme already has that exact type/model combination; otherwise the request fails and the separate asset-add endpoint is needed. This POST is replacement, not theme creation or application to devices.
- The credential needs `Management API - Terminal themes read and write`. Upload one required multipart/form-data `file` part with a supported, specific Content-Type. Generic or missing Content-Type, including `application/octet-stream`, is rejected with `422`. Supported media types depend on type/model: SVG is only for `logo`/`All`; MP4 or QuickTime only for SFO1/M450; JPEG/JPG or PNG for models other than `All`; GIF excludes SFO1/M450. The model limit is 100 MB for SFO1/M450 and 10 MB for all other models.
- The query table restricts `logo` to `All`, `idleScreen` and `shopperEngagementScreen` to SFO1/M450, and other screen types to a single Android terminal model. Read the raw table for the full type list. No default model/type or idempotency rule is stated.
- `200` returns required `type`, `model`, and `url`; the URL is a CDN link containing a token and is valid for 24 hours. This readback establishes the replacement response, not on-device theme application, current account eligibility, or payment processing. The reference lists `400`, `401`, `403`, `404`, `422`, `429`, and `500` errors; examples illustrate missing theme/asset, unauthorized logo change, file-size validation, and rate limit, without guaranteeing those are the only causes.

## Detail locators

- Purpose, existing type/model requirement, supported Content-Types, model-size limits, role and TEST server: [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets/replace/2026-11-07#L5|raw lines 5–32]].
- Required path/query/file fields, `200` body, and error codes: [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets/replace/2026-11-07#L34|raw lines 34–93]].
- Success and error examples: [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets/replace/2026-11-07#L95|raw lines 95–213]].

## Related

- [[adyen-terminal-management]] — terminal administration and application boundary.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/terminalThemes/(id)/assets/replace/2026-11-07|Captured Management API merchant terminal-theme asset replacement reference]]

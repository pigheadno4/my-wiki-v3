---
title: "Replace a company terminal-theme asset"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/assets/replace"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/assets/replace/2026-11-07.md"
tags: [adyen, management-api, android-terminals, terminal-themes]
---

## Overview

This 2026-11-07 snapshot of the [[adyen]] Management API `latest` POST reference lists the v3 TEST server for replacing an **existing** image or video asset of a company-owned terminal theme. Required path IDs identify the company account and theme; required query `type` and `model` identify the existing asset pair. If that pair is absent, this replacement request fails and the separate asset-creation endpoint is needed. The credential requires **Management API - Terminal themes read and write**. The endpoint is rate limited.

## Key takeaways

- Upload exactly one multipart/form-data part named `file` with a supported, specific Content-Type; generic or missing Content-Type such as `application/octet-stream` is rejected with `422`. SVG is only for `logo` with model `All`; JPEG/PNG exclude `All`; MP4/QuickTime are only for SFO1/M450; GIF excludes SFO1/M450.
- The `model` query allows `All` only for `logo`; `idleScreen` and `shopperEngagementScreen` require SFO1/M450. Maximum upload size is 100 MB for SFO1/M450 and 10 MB for other models. The raw table owns the full screen-type descriptions and combinations.
- A `200` returns asset `model`, `type`, and tokenized CDN `url` valid for 24 hours. This is asset replacement readback, not evidence that the theme has been applied to a terminal or displayed. The `403` example shows a theme-specific logo-modification denial; `404` examples distinguish missing theme from absent asset pair.

## Detail locators

- Replacement prerequisite, media mapping, size limits, role and TEST server: raw lines 5–32.
- Required path/query fields and multipart file: lines 34–53.
- `200` response and 24-hour URL: lines 55–65; example: 95–106.
- Errors: `400` lines 68–69 and 108–118; `401` 72–73 and 120–130; `403` 76–77 and 132–144; `404` 80–81 and 146–168; `422` 84–85 and 170–188; `429` 88–89 and 190–201; `500` 92–93 and 203–213.

## Related

- [[adyen-android-terminals]] — Android terminal customization context.
- [[adyen-terminal-management]] — terminal administration.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/(id)/assets/replace/2026-11-07|Replace terminal-theme asset reference (2026-11-07)]]

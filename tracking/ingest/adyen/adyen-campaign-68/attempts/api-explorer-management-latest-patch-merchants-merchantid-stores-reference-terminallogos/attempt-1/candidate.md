---
title: "Adyen Management API: Update store terminal logo by merchant and reference"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(reference)/terminalLogos"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(reference)/terminalLogos/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, terminal-management]
---

## Overview

Captured Management API v3 reference for PATCH of a store's logo for one terminal model, scoped by merchant account ID and store reference. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- `merchantId` and store `reference` are required path parameters; `model` is a required query parameter. The request body lists optional `data`: a Base64-encoded image string to change the model's logo, or an empty value to restore inheritance from merchant or company level.
- The configured logo applies to terminals of that model under the store unless an individual terminal has a different logo. Only one model can be updated per request.
- The API credential needs the **Management API—Terminal settings read and write** role. Live requests are subject to rate limits. The captured server is `https://management-test.adyen.com/v3`.
- Documented success is `200` with optional response `data`, or `204` without content. These responses describe request processing, not verified display on each terminal. The remove-logo response example depicts inherited image data; it is an example, not a response guarantee.

## Detail locators

- Path, model values, and request body: raw lines 23–41.
- Remove and upload request examples: raw lines 43–57; response status and optional body: lines 58–70; response examples: lines 172–188.
- Documented 400, 401, 403, 422 and 500 errors and their field schemas: raw lines 73–170.

## Related

- [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/stores/(reference)/terminalLogos/2026-11-07|Management API v3 store terminal logo PATCH reference]]

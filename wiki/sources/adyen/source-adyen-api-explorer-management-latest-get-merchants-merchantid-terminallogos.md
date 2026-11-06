---
title: "Adyen Management API: Get merchant terminal logo"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalLogos"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalLogos/2026-11-07.md"
tags: [adyen, management-api, terminal-management, terminal-logo]
---

## Overview

This captured Management API `latest` reference lists a TEST `/v3` server for `GET /merchants/{merchantId}/terminalLogos`. It reads the logo configured for one terminal model at the merchant account identified by `merchantId`; it does not change the configuration. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- `merchantId` is a required path parameter and `model` is a required query parameter. The caller's API credential needs either **Management API—Terminal settings read** or **Management API—Terminal settings read and write**. The raw parameter table lists the supported model values.
- The merchant-level logo applies to terminals of that model under the merchant account unless a store or individual-terminal logo overrides it. A returned image is Base64 encoded and must be decoded to obtain the image file.
- `200` reports success with an optional `data` string; `204` reports successful processing with no additional content. Neither response establishes what an individual terminal displays. The captured reference also lists `400`, `401`, `403`, `422`, and `500` errors.
- Live requests are subject to rate limits. The captured TEST server and readback do not establish current Live access, device application, or payment execution.

## Detail locators

- Request purpose, inheritance, roles, and Live rate-limit notice: raw lines 5–20.
- Required path/query parameters and model values: raw lines 22–33.
- Success response and optional Base64 `data`: raw lines 35–47; illustrative `200` example: lines 149–158.
- Error codes and response schemas: raw lines 50–147.

## Related

- [[adyen-terminal-management]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalLogos/2026-11-07|GET merchant terminal logo, captured 2026-11-07]]

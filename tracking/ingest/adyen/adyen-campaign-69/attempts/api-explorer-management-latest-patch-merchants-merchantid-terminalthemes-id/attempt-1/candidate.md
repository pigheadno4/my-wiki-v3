---
title: "Adyen Management API merchant terminal-theme metadata update"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalThemes/(id)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalThemes/(id)/2026-11-07.md"
tags: [adyen, management-api, terminal-themes, merchant, point-of-sale]
---

## Overview

This 2026-11-07-captured Management API `latest` v3 Test reference documents `PATCH /merchants/{merchantId}/terminalThemes/{id}` to change the name or dark/light mode metadata of the merchant-path terminal theme identified by `id`. It is a metadata update, separate from theme asset management and application to a terminal. See [[adyen]] and [[adyen-android-terminals]].

## Key takeaways

- The caller's API credential must have the **Management API - Terminal themes read and write** role. Both `merchantId` (merchant account) and `id` (theme) are required path identifiers.
- The request table marks both body properties optional: `mode` accepts `dark` or `light`; `name` is typed `string,null` and must be unique per account within the same company context. The page specifies no default, name length limit, or required body-property combination.
- A `200 OK` response contains required `id`, `mode`, and `name` fields for the theme. Its response schema types `name` as `string`, although the request schema also permits `null`; the page does not explain the result of sending `null`. The example is illustrative, not proof of asset change, theme application, propagation to a device, or payment execution.
- The reference lists `400`, `401`, `403`, `404`, `422`, and `500` errors. Example details include access denied, theme not found for the specified owner/company context, and a duplicate name. It states no idempotency rule, version conflict handling, deletion/reversal effect, propagation timing, or device-state readback. The captured Test endpoint does not establish a Live endpoint or current account eligibility.

## Detail locators

- Purpose, credential role, and v3 Test server: raw lines 5–14.
- Path identifiers, request schema and example: raw lines 16–39.
- `200` response schema and example: raw lines 40–50, 76–87.
- Error statuses and examples: raw lines 53–74, 89–171.

## Related

- [[adyen-android-terminals]] — Android-terminal and theme source route.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalThemes/(id)/2026-11-07|Merchant terminal-theme metadata PATCH, captured 2026-11-07]]

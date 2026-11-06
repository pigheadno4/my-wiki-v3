---
title: "Adyen Management API: get a merchant terminal theme"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalThemes/(id)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalThemes/(id)/2026-11-07.md"
tags: [adyen, management-api, terminal-themes, point-of-sale]
---

## Overview

This 2026-11-07-captured Management API `latest` v3 TEST reference reads one terminal theme by merchant-account `merchantId` and theme `id`. A `200` response returns theme metadata and CDN URLs for added assets. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- Both path identifiers are required strings. The documented request has no query parameters or body. Its access instructions name the `Management API - Terminal themes read and write` API-credential role.
- The `200` response table marks `id`, `name`, `mode` (`dark` or `light`), and `assets` required. Each listed asset has required `model`, `type` (`logo`, `homeScreen`, `idleScreen`, `afterPaymentScreen`, or `shopperEngagementScreen`), and `url`. Asset CDN URLs include a `?token=` query parameter and are valid for 24 hours; do not treat an example URL as durable. If the theme lacks permission to customize terminal logos, its logo URL leads to the Adyen logo.
- The listed errors are 400, 401, 403, 404, and 500. The 404 example says no theme was found for the given ID and account. A theme readback establishes the returned theme data, not that assets are applied or visible on a terminal, or that a payment can be processed.

> [!warning] Contradiction
> The access instructions require `Management API - Terminal themes read and write`, but the 403 example says `Missing required role: Management API - Terminal settings read and write`. This capture does not resolve which role the endpoint enforces.

## Detail locators

- Pinned raw, lines 5–15: purpose, logo-permission behavior, role instruction, and TEST v3 server.
- Pinned raw, lines 19–39: required path parameters and `200` response fields, asset types, tokenized 24-hour URLs.
- Pinned raw, lines 42–59: response-status list; lines 61–84: illustrative success response; lines 86–147: illustrative error responses, including conflicting 403 role wording and account-scoped 404 detail.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalThemes/(id)/2026-11-07|Merchant terminal-theme GET reference, captured 2026-11-07]]

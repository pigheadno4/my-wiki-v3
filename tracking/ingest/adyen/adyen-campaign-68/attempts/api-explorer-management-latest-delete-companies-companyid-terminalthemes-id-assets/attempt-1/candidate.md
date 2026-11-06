---
title: "Adyen Management API: Delete one terminal theme asset"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/delete/companies/(companyId)/terminalThemes/(id)/assets"
raw_files:
  - "adyen/api-explorer/Management/latest/delete/companies/(companyId)/terminalThemes/(id)/assets/2026-11-07.md"
tags: [adyen, management-api, android-terminals, terminal-themes, assets]
---

## Overview

This 2026-11-07 Management API `latest` reference lists the TEST `/v3` server for deleting **one asset** from a terminal theme owned by a company. It does not describe deletion of the theme itself. [[adyen]] [[adyen-android-terminals]]

## Key takeaways

- Required path parameters are `companyId` (company account) and `id` (terminal theme). Required query parameters `type` and `model` select the asset. `logo` requires `model=All`; every other screen type requires one Android model. `idleScreen` and `shopperEngagementScreen` are supported only for `SFO1` or `M450`. The raw query table enumerates the screen types.
- The caller's API credential needs **Management API - Terminal themes read and write**. Logo deletion is blocked if the theme owner cannot edit logos.
- `204` says the asset was deleted and returns no response body. The reference lists `401`, `403`, `404`, `422` and `500` errors, with examples of forbidden logo modification, absent selected asset, and invalid asset type. It does not specify fallback visuals or when terminals apply the change; deletion success is not on-device or payment proof.

## Detail locators

- Purpose, role, server and selectors: raw lines 5–31.
- Status descriptions and error examples: raw lines 33–128.

## Related

- [[adyen-android-terminals]] — Android terminal and theme retrieval.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/delete/companies/(companyId)/terminalThemes/(id)/assets/2026-11-07|Management API terminal theme asset deletion (2026-11-07)]]

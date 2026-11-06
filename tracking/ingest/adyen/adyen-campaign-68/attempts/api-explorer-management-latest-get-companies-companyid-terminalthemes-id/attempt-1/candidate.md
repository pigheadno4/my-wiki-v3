---
title: "Get a company terminal theme"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalThemes/(id)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalThemes/(id)/2026-11-07.md"
tags: [adyen, management-api, android-terminals, terminal-themes]
---

## Overview

This 2026-11-07 snapshot of the [[adyen]] Management API `latest` GET reference lists the v3 TEST server for reading one terminal theme. Required path parameters are the unique company-account `companyId` and theme `id`. The operation introduction requires the **Management API - Terminal themes read and write** credential role.

## Key takeaways

- A `200` returns required theme `id`, `name`, display `mode` (`dark` or `light`), and `assets` array. Each asset has required terminal `model`, screen `type`, and a tokenized CDN `url` valid for 24 hours. The raw table lists logo, home, idle, after-payment, and shopper-engagement screen types.
- The reference says the theme's logo URL leads to the Adyen logo if the theme lacks permission to customize terminal logos. Asset URLs and theme metadata are readback, not proof that a terminal has applied or displayed the theme.
- The captured errors are `400`, `401`, `403`, `404`, and `500`. The `404` example says no theme was found for the ID and specified account.

> [!warning] Contradiction
> The operation introduction specifies **Management API - Terminal themes read and write** (raw lines 10–12), while the `403` example's detail says **Management API - Terminal settings read and write** (line 117). The example does not resolve the actual role requirement.

## Detail locators

- Purpose, logo permission condition, role and TEST server: raw lines 5–15.
- Required company and theme IDs: lines 17–23.
- `200` schema and 24-hour URL lifetime: lines 25–39; response example: 61–84.
- Error descriptions and examples, including role mismatch: lines 42–59 and 86–147.

## Related

- [[adyen-android-terminals]] — Android terminal theme context.
- [[adyen-terminal-management]] — terminal fleet administration.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalThemes/(id)/2026-11-07|Get terminal theme reference (2026-11-07)]]

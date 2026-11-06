---
title: "Adyen Management API: apply a theme to one Android terminal"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/(id)/apply"
raw_files:
  - "adyen/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/(id)/apply/2026-11-07.md"
tags: [adyen, management-api, android-terminals, terminal-themes, api-explorer]
---

## Overview

This 2026-11-07-captured Management API v3 Test reference applies the theme identified by `id` to the Android terminal identified by `terminalId`. The terminal must already be deployed or boarded. This terminal-scoped action is distinct from creating theme metadata or adding assets, and the `200 OK` description contains no device-state readback. [[adyen]] [[adyen-android-terminals]]

## Key takeaways

- The API credential needs **Management API - Terminal themes read and write**. The captured server is `https://management-test.adyen.com/v3`; no live server is supplied on this page.
- Both path parameters are required: `id` is the theme's unique identifier, and `terminalId` is the terminal's unique identifier. No request body, defaults or limits are specified here.
- The introduction requires a deployed or boarded terminal. A `422` example repeats that requirement; a `403` example says the theme must belong to the terminal/store's merchant account or its company. Treat these examples as illustrated failures, not a complete eligibility matrix.
- `200 Success` is described as `OK` without a response body or device-confirmation field. It documents successful handling of the apply request, but does not show on-device display, propagation timing, a payment outcome, or later device state.

## Detail locators

- Purpose, deployed/boarded prerequisite, role and Test v3 server: [[raw/adyen/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/(id)/apply/2026-11-07#L5|raw lines 5–14]].
- Required theme and terminal path IDs, `200 OK` and listed errors: [[raw/adyen/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/(id)/apply/2026-11-07#L16|raw lines 16–47]].
- Error examples, including theme ownership and terminal assignment: [[raw/adyen/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/(id)/apply/2026-11-07#L49|raw lines 49–115]].

## Related

- [[adyen-android-terminals]] — Android terminal themes and device evidence boundary.
- [[adyen-terminal-management]] — terminal fleet administration context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/(id)/apply/2026-11-07|Adyen terminal-scoped theme apply reference capture, 2026-11-07]]

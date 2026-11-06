---
title: "Adyen Management API: unapply a terminal theme from one terminal"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/unapply"
raw_files:
  - "adyen/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/unapply/2026-11-07.md"
tags: [adyen, management-api, terminal-management, terminal-themes]
---

## Overview

This captured Management API v3 reference resets the custom theme assignment for the Android terminal identified by required path `terminalId`. The terminal falls back to a custom theme applied at the next higher store, merchant-account, or company level, or to the default Adyen theme. The theme resource remains unchanged and is not deleted. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- The terminal must be deployed or boarded. The API credential needs **Management API - Terminal themes read and write**. The captured server is `https://management-test.adyen.com/v3`.
- If no custom theme is currently applied directly to the terminal, the request still returns `200 OK` without error. `200` is therefore not proof that a terminal-level assignment existed before the call.
- The response section lists `200 OK` and 401, 403, 404, 422, and 500 errors. Its `200` example contains `status: success`, but the page provides no response-field schema. The `422` example concerns a terminal that is not deployed or boarded.

## Detail locators

- Assignment reset, fallback, no deletion, no-op success and credential role: raw lines 5–15.
- Test server and required terminal path ID: raw lines 17–25. Status codes: raw lines 27–50; illustrative response bodies: raw lines 52–127.

## Related

- [[adyen-terminal-management]] — Terminal fleet configuration and theme context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/terminals/(terminalId)/terminalThemes/unapply/2026-11-07|Management API v3 terminal-theme unapply reference]]

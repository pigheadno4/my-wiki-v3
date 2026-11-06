---
title: "Adyen Management API: update a terminal logo"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/terminals/(terminalId)/terminalLogos"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/terminals/(terminalId)/terminalLogos/2026-11-07.md"
tags: [adyen, management-api, terminal-logo, point-of-sale]
---

## Overview

This captured Management API reference updates the logo of the payment terminal identified by the required path `terminalId`. Its listed server is TEST `/v3`; the page also notes live rate limits. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- Send the image as a Base64-encoded string in `data`. An empty logo value restores the logo inherited from the store, merchant account, or company account. The body table marks `data` optional; it does not specify an image size or dimension limit here.
- The API credential needs `Management API—Terminal settings read and write`.
- `200` means the request succeeded; its response body may contain `data`. The removal example shows an inherited logo string, and the upload example shows the supplied logo string. Examples do not guarantee that `data` is always present or prove when the logo appears on a device.
- The page lists 400, 401, 403, 422, and 500 errors. A successful configuration response does not establish payment execution or current live eligibility.

## Detail locators

- Raw lines 5–33: purpose, inheritance/reset, credential role, live rate limit, TEST server, path and body fields.
- Raw lines 35–49: removal and upload request examples; lines 50–158: success and error schemas; lines 160–175: illustrative success bodies.

## Related

- [[adyen]]
- [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/terminals/(terminalId)/terminalLogos/2026-11-07|Captured Management API PATCH terminal logo reference]]

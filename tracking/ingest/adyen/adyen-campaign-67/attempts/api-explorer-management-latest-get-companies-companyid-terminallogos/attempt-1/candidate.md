---
title: "Management API: Get company terminal logo"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalLogos"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalLogos/2026-11-05.md"
tags: [adyen, management-api, terminal-logos, terminal-settings]
---

## Overview

The captured Management API `GET /companies/{companyId}/terminalLogos` reads the logo configured for a specified payment-terminal model at a company account. Its required path `companyId` identifies that company; required query `model` selects a terminal model from the reference's enumerated values. The page lists the Test `https://management-test.adyen.com/v3` server and requires the caller's API credential to have **Management API—Terminal settings read** or **Management API—Terminal settings read and write**. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- The company-level logo applies to terminals of the specified model under that company unless a different logo is configured at a lower level: merchant account, store, or individual terminal. This GET reads the company configuration; it does not identify any particular terminal's effective displayed image.
- A `200` means the read request succeeded. The response's `data` string is optional in the schema and, when present, holds the image file as Base64 text. Decode that string to obtain the image file. The response example's `BASE-64_ENCODED_STRING` is illustrative.
- The reference states that Live requests are subject to rate limits but provides no numeric threshold here. It lists 400, 401, 403, 422, and 500 errors. It specifies no request body, idempotency mechanism, logo update/deletion, propagation or device-application timing, Live server URL, or payment outcome. A readback does not establish device display, successful boarding, merchant eligibility, or payment execution.

## Detail locators

- Purpose, Base64 format, lower-level overrides, caller roles, Live rate-limit caveat, and Test server: raw lines 5–21.
- Required `companyId` path and `model` query, including the complete model value list: raw lines 23–34.
- `200` optional `data` string: raw lines 36–44. Error statuses and schemas: lines 47–144. Illustrative JSON response: lines 146–154.

## Related

- [[adyen-terminal-management]] — terminal-settings administration and inheritance context.
- [[source-adyen-docs-point-of-sale-automating-terminal-management-configure-terminals-api]] — separate configuration guide for company, merchant, store, and terminal levels.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalLogos/2026-11-05|Pinned Management API company terminal-logo GET reference]]
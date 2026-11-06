---
title: "Adyen Management API: update merchant terminal logo"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalLogos"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalLogos/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, terminal-management, logos]
---

## Overview

This captured [[adyen]] Management API `latest` reference documents `PATCH /merchants/{merchantId}/terminalLogos` on the v3 test server. It updates the logo for one terminal model under the merchant account. The merchant-level logo applies to that model's terminals unless a store or individual terminal has a different logo. See [[adyen-terminal-management]].

## Key takeaways

- Supply the merchant account identifier in the path and a required `model` query parameter. The raw query-parameter table lists the allowed model values. The request body table marks `data` optional; the operation prose says a Base64-encoded image changes the logo and an empty logo value restores inheritance from the company account.
- The API credential needs the `Management API—Terminal settings read and write` role. The reference warns that live requests have rate limits, while its displayed server is `https://management-test.adyen.com/v3`.
- A `200` response says the request succeeded and may include Base64 `data`; a `204` says processing succeeded without content. Neither response documents when a physical terminal displays the logo. The reference does not specify idempotency, propagation timing, or a device-state confirmation.

## Detail locators

- `## Parameters` → `### Path parameters`, `### Query parameters`, and `### Request body`: merchant ID, terminal-model allowlist, and optional `data`.
- `## Request examples` → `remove-logo` and `upload-logo`; examples illustrate the payloads, without adding validation rules.
- `## Responses` → `200 Success`, `204 Success`, and `400`, `401`, `403`, `422`, `500` errors; consult the raw tables for optional versus required fields.
- `## Response examples` → `200 Success`: illustrative inherited-logo and uploaded-logo data.

## Related

- [[adyen]]
- [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/terminalLogos/2026-11-07|Management API merchant terminal-logo PATCH, captured 2026-11-07]]

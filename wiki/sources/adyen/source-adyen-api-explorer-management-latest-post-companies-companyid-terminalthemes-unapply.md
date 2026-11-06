---
title: "Adyen Management API: Unapply a company terminal theme"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/unapply"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/unapply/2026-11-07.md"
tags: [adyen, management-api, android-terminals, terminal-themes]
---

## Overview

This 2026-11-07 Management API `latest` reference documents `POST /companies/{companyId}/terminalThemes/unapply` on the shown TEST v3 server (`https://management-test.adyen.com/v3`). It resets the theme assignment for the company account identified by required path `companyId`. [[adyen]] · [[adyen-android-terminals]]

## Key takeaways

- Terminals under that company switch to the default Adyen theme **unless** a custom theme is assigned at merchant, store, or individual-terminal level; those lower-level assignments continue to control their terminals. The theme resource itself remains unchanged and is **not deleted**.
- The API credential needs **Management API - Terminal themes read and write**. The reference specifies no request body or query parameter beyond required company `companyId`.
- `200 OK` is also returned without error when no custom theme is currently applied at company level. The `200` example has `{"status":"success"}`, but no response-body schema is defined here. A successful call does not prove a particular terminal has displayed the default theme or that a lower-level override was removed; the reference gives no propagation time.
- The reference lists `401` Unauthorized, `403` Forbidden, `404` Not Found, and `500` Internal Server Error, with illustrative error bodies. It states no idempotency, rollback, deletion, version/conflict, approval, or financial-execution contract for this unapply operation.

## Detail locators

- Company-assignment effect, lower-level fallback, nondeletion, no-custom-theme success, caller role, TEST server and required path: raw lines 5–25.
- Status descriptions: raw lines 27–46. Illustrative `200` and error bodies: raw lines 48–108.

## Related

- [[adyen]] · [[adyen-android-terminals]] · [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/terminalThemes/unapply/2026-11-07|2026-11-07 captured company terminal-theme unapply reference]]

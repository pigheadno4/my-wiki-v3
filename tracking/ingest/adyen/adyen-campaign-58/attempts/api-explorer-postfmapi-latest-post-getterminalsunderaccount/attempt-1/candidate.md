---
title: "Adyen deprecated POS API: List terminals under an account"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/postfmapi/latest/post/getTerminalsUnderAccount"
raw_files:
  - "adyen/api-explorer/postfmapi/latest/post/getTerminalsUnderAccount/2026-09-15.md"
tags: [adyen, point-of-sale, terminals, terminal-management, deprecated]
---

## Overview

This 2026-09-15 API Explorer snapshot documents POST `/getTerminalsUnderAccount` on the displayed `postfmapi/terminal/v1` test server. It lists terminal assignments at company, merchant or store scope. The page says POS Terminal Management API was deprecated January 1, 2025, support stopped April 1, 2025, and Management API is the fleet-automation route. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- `companyAccount` is required. Company-only scope includes terminals at all account levels; optional `merchantAccount` narrows to that merchant and its stores, and is required when `store` is supplied. Optional `store` is a store code and narrows results to terminals assigned to that store (raw lines 14–47).
- The 200 schema requires the response `companyAccount`; optional company `inventoryTerminals` and `merchantAccounts` distinguish company inventory from merchant-level inventory and in-store assignments. Each merchant object requires `merchantAccount`; each store object requires `store`, with optional store `inStoreTerminals`, merchant account code and store status (raw lines 50–68). Terminal strings are device identifiers, distinct from merchant-account identifiers and store codes.
- The page defines in-store terminal state as ready for boarding **or** already boarded. A listed assignment therefore does not prove a terminal was boarded, configured, online or able to process a payment (raw lines 5–7, 57–68). Store status values and implications are in the raw table at line 67; they are store properties, not device readiness.
- Errors listed are 400, 401, 403, 422 and 500. The 400/403/422/500 bodies are illustrated with generic examples and do not establish a particular live account's permissions or terminal state (raw lines 71–251).

## Detail locators

- Operation and dated deprecation/support cutoff: raw lines 5–12. Filter fields and company/merchant/store request examples: raw lines 14–47.
- 200 nested response schema and store status enum: raw lines 48–68. Three scoped success examples: raw lines 135–203.
- Error categories, body fields and examples: raw lines 71–133 and 205–251.

## Related

- [[adyen-terminal-management]] — modern fleet-management context and reciprocal route.
- [[source-adyen-api-explorer-management-latest-get-terminals]] — separate Management API v3 terminal-list contract; do not substitute its schema for this deprecated API.

## Raw Sources

- [[raw/adyen/api-explorer/postfmapi/latest/post/getTerminalsUnderAccount/2026-09-15|POS Terminal Management API list endpoint, captured 2026-09-15]]

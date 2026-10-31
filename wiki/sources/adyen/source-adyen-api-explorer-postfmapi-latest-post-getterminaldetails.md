---
title: "Adyen POS Terminal Management API v1: POST /getTerminalDetails"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/postfmapi/latest/post/getTerminalDetails"
raw_files:
  - "adyen/api-explorer/postfmapi/latest/post/getTerminalDetails/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-management, deprecated-api]
---

## Overview

This 2026-09-15 API Explorer capture documents `POST /getTerminalDetails` on the listed TEST POS Terminal Management v1 server. It looks up one physical terminal by its unique `[Device model]-[Serial number]` ID and returns fleet/assignment details like those shown in Customer Area and the Terminal Fleet report. The page states that POS Terminal Management API was deprecated from 2025-01-01, support stopped 2025-04-01, and fleet automation should use the Management API. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The request body requires `terminal` as a string ID. A 200 response requires `companyAccount` and `terminal`; `merchantAccount`, `store`, `storeDetails`, `merchantInventory`, `terminalStatus`, network identifiers, last activity/transaction times and other attributes are optional. Nested `storeDetails.store` is required only within the optional `storeDetails` object.
- A response with only `companyAccount` as an account level means company inventory. `merchantAccount` without `store` means merchant assignment. When returned for a merchant assignment, `merchantInventory=true` means merchant inventory and cannot be boarded; `false` means in-store merchant assignment and ready to be boarded or already boarded. A returned `store` names store assignment. These are distinct assignment/boarding states, not proof of current payment readiness.
- Optional `storeDetails.status` has store activation states; `Active` is described as enabling payment processing for that store. Optional `terminalStatus` reports recent online or pending reassignment states, not a payment authorization result. Last activity and transaction times are omitted if older than 14 days, so absence does not prove no historical activity. The example terminal is `SwitchedOff` despite store assignment and `merchantInventory=false`; it does not demonstrate a currently ready device.
- The page lists 400 request reading/understanding, 401 authentication, 403 insufficient permissions, 422 validation and 500 server errors. Its generic examples and TEST URL do not show a live device, successful boarding, payment-method setup or executed payment. No named API role is specified here.

## Detail locators

- Identity, dated deprecation and TEST v1 server: raw lines 5–19.
- Request example and 200 response schema/assignment, boarding and status semantics: raw lines 21–73.
- Error classes and schemas: raw lines 76–138; illustrative terminal and generic error examples: lines 140–222.

## Related

- [[adyen-terminal-management]] — Management API and fleet procedures.

## Raw Sources

- [[raw/adyen/api-explorer/postfmapi/latest/post/getTerminalDetails/2026-09-15|POS Terminal Management API getTerminalDetails capture]]

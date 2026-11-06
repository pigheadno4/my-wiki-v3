---
title: "Adyen Management API v3: reassign a terminal"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/terminals/(terminalId)/reassign"
raw_files:
  - "adyen/api-explorer/Management/latest/post/terminals/(terminalId)/reassign/2026-11-05.md"
tags: [adyen, management-api, terminal-management, reassignment]
---

## Overview

This 2026-11-05-captured Management API reference documents `POST /terminals/{terminalId}/reassign` for moving a payment terminal to a company account, merchant account, merchant account inventory, or store. The caller needs the `Management API—Assign Terminal` role. The listed server is TEST `https://management-test.adyen.com/v3`; the page says Live requests are rate limited but gives no numeric limit here. A successful request is a reassignment API result, not proof of on-device boarding, payment readiness, transaction processing, or settlement. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- The path requires the terminal's string `terminalId`. The request body lists optional `companyId`, `merchantId`, `storeId`, and `inventory` fields for distinct assignment destinations; no single body property is schema-marked universally required (raw lines 18–32).
- For reassignment to a merchant account, the prose requires `inventory` with `merchantId`. `inventory: true` places the terminal in merchant inventory, where the page says it cannot process transactions; `false` assigns it directly to the merchant account, which the page describes as able to process transactions. This is a destination distinction, not evidence a particular device has boarded or processed a payment (raw lines 29–31).
- The merchant and store JSON request examples illustrate separate destinations; they do not establish the full set of valid combinations or a default `inventory` value (raw lines 34–49).
- HTTP 200 is the documented success status, with no success response-body schema. The page says to inspect the actual response code for request status. It separately lists 400, 401, 403, 422, and 500 errors; it gives no idempotency or reversal contract (raw lines 50–153).

## Detail locators

- Purpose, role, Live rate-limit qualification, and TEST server: raw lines 5–16.
- Path ID, body identities, conditional inventory rule, and request examples: raw lines 18–49.
- 200 status and error schemas: raw lines 50–153.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/terminals/(terminalId)/reassign/2026-11-05|Management API terminal reassignment, captured 2026-11-05]]

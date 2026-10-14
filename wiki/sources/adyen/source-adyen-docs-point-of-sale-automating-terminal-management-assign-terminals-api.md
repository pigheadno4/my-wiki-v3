---
title: "Adyen Docs: Assign terminals with Management API"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/automating-terminal-management/assign-terminals-api"
raw_files:
  - "adyen/docs/point-of-sale/automating-terminal-management/assign-terminals-api/2026-09-15.md"
tags: [adyen, point-of-sale, management-api, terminal-management, terminal-assignment]
---

## Overview

Adyen's unversioned POS guide, captured 2026-09-15, explains how to reassign physical payment terminals with Management API. Reassignment changes the terminal's account level and inventory state so that it can be boarded; boarding is a separate step before the terminal can process transactions. This is fleet administration, not Terminal API payment messaging. [[adyen]] · [[adyen-terminal-management]] · [[adyen-pos-store-management]]

## Key takeaways

- The guide replaces the unsupported classic POS Terminal Management API for automated assignment with Management API. A new terminal starts in company or merchant inventory. A store-bound terminal must be reassigned to the store and then boarded. Where merchant accounts represent stores, reassignment to the merchant account must explicitly set `inventory: false` to take it out of inventory before boarding; `inventory: true` keeps it unable to transact.
- Use a POS integration and an API credential with an API key and task-specific roles: **Management API—Stores read** or **Stores read and write** for store details, **Terminal actions read** for terminal details, and **Assign Terminal** for assignment. A cloud Terminal API integration can use its existing API key if the Management API roles are present. Subscribe to **Terminal assignment complete** webhooks. Live assignment endpoints have rate limits; the linked rate-limit guide holds the details.
- Discover the target store's `storeId` with `GET /merchants/{merchantId}/stores` and the device's `id` and current assignment with `GET /terminals`, subject to credential access. The `terminalId` path parameter uses device-model plus serial-number format. Reassign with `POST /terminals/{terminalId}/reassign` and the relevant `storeId`, `merchantId` plus required `inventory`, or `companyId` body field.
- HTTP 200/OK for reassignment is an asynchronous request response, not proof that reassignment or boarding has finished. The guide says the online terminal downloads and applies the new configuration. A delayed reassignment can trigger `terminalAssignment.completed`; its payload names the assigned account or store, event time, and terminal ID. This is assignment completion, not evidence of a completed boarding or payment.

## Detail locators

- **Account level and states:** raw “Account level and status of terminals” (lines 38–51) defines company/merchant/store assignment and `inventory`, `reassignmentInProgress`, `deployed`, and `boarded` states. An account setup may have no store level.
- **Identifiers and list response:** raw “Get a list of stores” (lines 53–228) gives merchant-scoped store lookup and `storeId`; “Get terminal details” (lines 294–472) gives credential-scoped terminal listing, `id`, assignment, and device attributes. Example curl and library calls use the test Management API v3 endpoint; examples are illustrative, not proof of a live account's inventory or assignment.
- **Request and outcome:** raw “Reassign terminals” (lines 580–600, 990–992) gives path/body parameter semantics, merchant `inventory` condition, HTTP 200/OK, asynchronous processing, and online configuration application. Store and merchant request examples start at lines 603 and 792.
- **Webhook:** raw “Terminal assignment complete webhooks” (lines 994–1014) specifies **Terminal assignment complete**, not **Standard**, and the `terminalAssignment.completed` payload. See “Requirements” (lines 25–36) for role and live-rate-limit pointers.

## Related

- [[adyen-terminal-management]] — Management API fleet administration
- [[adyen-pos-store-management]] — store identity and administration
- [[adyen-terminal-api]] — separate POS-to-terminal payment messages
- [[adyen-api-access]] — general API credential and role background

## Raw Sources

- [[raw/adyen/docs/point-of-sale/automating-terminal-management/assign-terminals-api/2026-09-15|Adyen Assign terminals guide, fetched 2026-09-15]]

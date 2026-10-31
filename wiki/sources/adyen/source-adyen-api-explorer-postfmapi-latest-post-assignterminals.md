---
title: "Adyen deprecated POS Terminal Management API v1: POST /assignTerminals"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/postfmapi/latest/post/assignTerminals"
raw_files:
  - "adyen/api-explorer/postfmapi/latest/post/assignTerminals/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-management, deprecated-api]
---

## Overview

This 2026-09-15-captured reference describes `POST /assignTerminals` on the **POS Terminal Management API v1 TEST** server. It assigns one or more terminal IDs to a merchant account or store, reassigns between merchants or stores, or returns terminals to company inventory. The page says this API was deprecated from January 1, 2025 and support stopped April 1, 2025; it directs fleet automation to the separate Management API. Do not apply this v1 request/response contract to Management API operations.

## Key takeaways

- The request table marks `companyAccount` and `terminals` (array of terminal IDs) required. To return terminals to company inventory, supply only those two fields. `merchantAccount` names the merchant account used for merchant or subordinate-store assignment; `store` is a store code. These are assignments of physical terminal IDs, not payment requests.
- `merchantInventory` is conditionally required when assigning to a merchant account and must not be used for store assignment. `true` assigns to merchant inventory, where terminals cannot be boarded. `false` assigns as in-store terminals; the page describes them as ready to be boarded and to process payments through that merchant account. This describes an assignment state, not evidence that a particular device has boarded, synchronized, received configuration, or processed a payment.
- A 200 body has required per-terminal `results`; inspect each terminal's value. `Done` means assigned, `AssignmentScheduled` means assignment will happen asynchronously, `RemoveConfigScheduled` means a previously assigned and boarded terminal must synchronize with Adyen, and `Error` means assignment failed for that terminal. A 200 alone does not establish that all requested assignments finished.
- Listed errors are 400 (request reading/understanding), 401 (authentication), 403 (insufficient permissions), 422 (validation), and 500 (server processing). The examples show three 200 results with `RemoveConfigScheduled`, plus illustrative error bodies; they are not a promise for every assignment.

## Detail locators

- Purpose, dated deprecation and TEST v1 endpoint: pinned raw, lines 5–12.
- Request field conditions and company/merchant/store examples: `## Parameters > ### Request body` and `## Request examples`, lines 14–59.
- Per-terminal result meanings: `## Responses > ### 200 Success`, lines 60–68; error descriptions: lines 71–133; response examples: lines 135–212.

## Related

- [[adyen-terminal-management]] — terminal-fleet context and current Management API routes.
- [[source-adyen-docs-point-of-sale-automating-terminal-management-assign-terminals-api]] — separate Management API assignment guide; do not transfer its contract to this deprecated v1 endpoint.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/postfmapi/latest/post/assignTerminals/2026-09-15|deprecated POS Terminal Management API v1 assignment capture]]

---
title: "Adyen Management API: List company terminal actions"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalActions"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalActions/2026-11-05.md"
tags: [adyen, management-api, terminal-actions, point-of-sale]
---

## Overview

This [[adyen]] Management API `latest` reference, captured 2026-11-05, lists terminal actions scheduled for the company named by `companyId` through `GET /companies/{companyId}/terminalActions`. Adyen-scheduled actions are excluded. The listed server is `https://management-test.adyen.com/v3`; the text also says Live requests are subject to rate limits, without giving a numeric limit here.

## Key takeaways

- The API credential needs either **Management API—Terminal actions read** or **Management API—Terminal actions read and write**. The required path `companyId` uniquely identifies the company account. Optional query filters are `type` (four Android app/certificate install/uninstall actions) and `status` (`pending`, `successful`, `failed`, `cancelled`, `tryLater`).
- Optional `pageSize` defaults to 20 and has a maximum of 100; `pageNumber` selects the page. The page does not specify a `pageNumber` default or total-count/pagination metadata in the response.
- A 200 indicates the list request succeeded. Its optional `data` array contains optional per-action `id`, `terminalId`, `actionType`, `config`, `scheduledAt`, `confirmedAt`, `status`, and `result`. An item's reported status and result describe that action, not every terminal action in the company or a payment outcome. The sample shows a cancelled action; it is illustrative, not a default outcome.
- The reference documents 400, 401, 403, 422 and 500 errors. It gives no idempotency, scheduling, cancellation, reversal, or device-application contract for this read endpoint. The snapshot is not evidence of current account eligibility, live device state, or successful payment execution.

## Detail locators

- List scope and Adyen-scheduled exclusion, caller roles, Live rate-limit qualification, and Test server: opening text and `## Servers`, lines 5-17.
- Required company ID, optional type/status filters, page size default and maximum, and page number: `## Parameters`, lines 19-33.
- Success meaning and optional action fields: `### 200 Success`, lines 35-51.
- Error meanings and problem-body schemas: `### 400 Client Error` (lines 54-71), `### 401 Client Error` (74-91), `### 403 Client Error` (94-111), `### 422 Client Error` (114-131), and `### 500 Server Error` (134-151).
- Illustrative cancelled action: `## Response examples`, lines 153-173.

## Related

- Company: [[adyen]]
- Concept: [[adyen-terminal-management]]

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalActions/2026-11-05|Adyen Management API — List company terminal actions (2026-11-05)]]

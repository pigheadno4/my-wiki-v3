---
title: "Adyen Management API v3: get a company terminal action"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalActions/(actionId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalActions/(actionId)/2026-11-05.md"
tags: [adyen, management-api, terminal-management, terminal-actions]
---

## Overview

This 2026-11-05-captured Management API reference describes `GET /companies/{companyId}/terminalActions/{actionId}`, a read of the terminal action identified by `actionId` under a company account. The listed server is `https://management-test.adyen.com/v3`. The API credential must have **Management API—Terminal actions read** or **Management API—Terminal actions read and write**. The reference separately warns that live requests are subject to rate limits, without giving a numeric limit here. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- Required string path parameters are `companyId` (company account) and `actionId` (terminal action). The page lists no query parameters or request body.
- HTTP `200` returns terminal-action details. All listed top-level response fields are schema-optional: `id`, `terminalId`, `actionType`, `config`, `scheduledAt`, `confirmedAt`, `result`, and `status`. Listed action types cover Android app and certificate install/uninstall. Listed statuses are `pending`, `successful`, `failed`, `cancelled`, and `tryLater`. `confirmedAt` is described as the time the action was carried out.
- The `successful` sample is an example of a returned action state, not a guarantee for other actions. A GET readback does not schedule or execute an action, establish current terminal configuration or payment readiness, or prove a payment outcome.

## Detail locators

- Purpose, credential roles, live-rate-limit notice, TEST server, and path IDs: raw lines 5–25.
- `200` terminal-action response fields, types, status values, and timing labels: raw lines 27–42.
- `400`, `401`, `403`, `422`, and `500` problem response schemas: raw lines 45–142. `401` is authentication required and `403` is insufficient permissions.
- Example `InstallAndroidCertificate` action with `successful` status: raw lines 144–159.

## Related

- [[adyen-terminal-management]] — terminal fleet administration and action routes.
- [[adyen-api-access]] — API credential context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalActions/(actionId)/2026-11-05|Adyen Management API get company terminal action, captured 2026-11-05]]

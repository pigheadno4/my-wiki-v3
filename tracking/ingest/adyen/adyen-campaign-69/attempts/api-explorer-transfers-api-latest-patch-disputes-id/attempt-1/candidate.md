---
title: "Adyen Issuing: update a raised dispute"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers-api/latest/patch/disputes/(id)"
raw_files:
  - "adyen/api-explorer/transfers-api/latest/patch/disputes/(id)/2026-11-07.md"
tags: [adyen, issuing, raised-disputes, transfers-api]
---

## Overview

Captured [[adyen]] `PATCH /disputes/{id}` reference at a `transfers-api` URL with Balance Platform BTL v4 test and live servers. It updates information for a raised Issuing dispute identified by required path `id`, or changes its status from draft to submitted or closed. This raised-cardholder-dispute route is distinct from merchant chargeback defense and funds-movement transfer operations.

## Key takeaways

- **Submitted and closed are final for updates.** Upload all supporting attachments through `POST /disputes/{id}/attachments` before submission. Submitting sends the raised dispute to the card scheme for review and acquirer defense; closing ends card-scheme review eligibility.
- The request table marks reason-specific `*Info` objects and `status` optional, while prose requires the matching information object for each dispute `type`. The `other` type is deprecated and must not be created or submitted. See the raw for the exact conditional fields; response-only fields must not be assumed to be PATCH inputs.
- A 200 says the request succeeded and returns a dispute representation with optional status and other fields. It does not establish a card-scheme decision, chargeback or fee reversal, or financial booking. The reference also documents 401 authentication required, 403 insufficient permissions, and 422 validation error.

> [!warning] Contradiction
> The PATCH request table labels `status` as an **object** while describing draft/submitted/closed values; the 200 response table labels `status` as a **string**. The capture provides no request example or nested request-status schema to resolve the input representation. Do not infer the PATCH JSON shape from the response table.

## Detail locators

- Final status effects, attachment prerequisite, servers, and path ID: raw lines 5–24.
- PATCH body table, optional top-level entries, conditional reason information, deprecated `other`, and status type: raw lines 27–36.
- 200 representation and reason-specific nested conditions: raw lines 38–121. Its required `transactionId` and `type` are response fields, not declared PATCH-body requirements.
- Structured 401/403/422 error schemas: raw lines 124–178.

## Related

- [[adyen-issuing]] — raised disputes for issued-card transactions.
- [[source-adyen-api-explorer-transfers-api-latest-post-disputes]] — separate draft creation reference.

## Raw Sources

- [[raw/adyen/api-explorer/transfers-api/latest/patch/disputes/(id)/2026-11-07|Raised-dispute PATCH, 2026-11-07]]

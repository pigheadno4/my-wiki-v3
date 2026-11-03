---
title: "PATCH /mandates/{mandateId} — Amend a direct debit mandate | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/mandates/(mandateId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/mandates/(mandateId)/2026-11-03.md"
tags: [adyen, balance-platform, business-accounts, direct-debit, mandates, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `PATCH /mandates/{mandateId}` to amend a specified direct debit mandate. Its captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest`, while the server path identifies v2. See [[adyen-business-accounts]] for the product context. [Raw: lines 5–10]

## Key takeaways

- The path requires the unique string `mandateId`. The request-body table lists only `paymentInstrumentId` (string or null), marked optional, as the identifier of the payment instrument linked to the mandate. The page specifies no body-level requiredness, other request field, null/omission effect, query parameter, default, value limit, caller-role name or idempotency contract. [Raw: lines 12–23]
- A 202 says the amendment request has been accepted. There is no success response-body schema or amended mandate status in this page. Acceptance alone does not confirm that the linked instrument changed, the mandate was approved or activated, a direct debit was collected, or funds moved. The page gives no propagation time, asynchronous completion signal or reversal behavior. [Raw: lines 25–30]
- The documented failures are 401 authentication required, 403 insufficient permission, 404 mandate not found, 422 request validation and 500 server processing. Their problem-body fields are mostly optional; required `message`, `name` and `value` apply within any included `invalidFields` entry, not to every error response. No example, conflict/version response or current live-eligibility guarantee appears in this snapshot. [Raw: lines 31–123]

## Detail locators

- Purpose, captured TEST v2 server, path identity and request body: pinned raw lines 5–23.
- Accepted 202 response and error meanings/schemas: lines 25–123.

## Related

- [[adyen-business-accounts]] — Business Accounts and direct debit context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/mandates/(mandateId)/2026-11-03|PATCH mandate amendment — captured 2026-11-03]]
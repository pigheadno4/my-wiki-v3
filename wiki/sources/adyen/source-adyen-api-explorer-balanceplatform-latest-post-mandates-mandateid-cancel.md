---
title: "POST /mandates/{mandateId}/cancel — Cancel a mandate | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/mandates/(mandateId)/cancel"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/mandates/(mandateId)/cancel/2026-11-03.md"
tags: [adyen, balance-platform, business-accounts, direct-debit, mandates, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `POST /mandates/{mandateId}/cancel`, a request to cancel a specified direct debit mandate. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest` while the server path identifies `v2`. See [[adyen-business-accounts]] for the Business Accounts context.

## Key takeaways

- The sole listed input is required string path `mandateId`, the unique mandate identifier. This page specifies no query parameters, request body, caller role, idempotency key or cancellation conditions. Authentication and permission failures are listed, but without a credential-role definition. [Raw: lines 5–17, 25–60]
- A `202 Success` says only that the request has been accepted. The reference gives no 202 response body, returned mandate or cancellation status, confirmation event, completion timing or reversal behavior. Acceptance should not be read as proof that the mandate is already cancelled, that a direct debit was stopped or that funds were reversed. [Raw: lines 19–24]
- The documented failures are 401 authentication required, 403 insufficient permissions, 404 mandate not found, 422 validation error and 500 server-processing failure. Their problem-body fields are largely optional; an `invalidFields` entry, if present, has required `message`, `name` and `value` properties. The page does not explain retry, duplicate-request or state-conflict behavior. [Raw: lines 25–117]
- This dated TEST v2 capture does not establish current live availability, an account's eligibility, compliance, collection outcome, bank movement or receipt. The endpoint's stated action is mandate cancellation; payment and settlement outcomes require separate evidence. [Raw: lines 5–24]

## Detail locators

- Purpose, TEST v2 server and required path parameter: pinned raw lines 5–17.
- `202` accepted response without a success body: lines 19–24.
- Error meanings and problem-body schemas: lines 25–117.

## Related

- [[adyen-business-accounts]] — Business Accounts and direct debit context.
- [[source-adyen-api-explorer-balanceplatform-latest-get-mandates]] — separate mandate-list read reference.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/mandates/(mandateId)/cancel/2026-11-03|POST cancel mandate — captured 2026-11-03]]
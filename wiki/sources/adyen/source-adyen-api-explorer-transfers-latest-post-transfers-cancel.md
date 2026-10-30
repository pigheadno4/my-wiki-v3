---
title: "Adyen Transfers API v4: Cancel transfers under review"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/cancel"
raw_files:
  - "adyen/api-explorer/transfers/latest/post/transfers/cancel/2026-09-15.md"
tags: [adyen, transfers-api, platforms, transfer-review, cancellation]
---

## Overview

Captured Transfers API v4 test-server reference for `POST /transfers/cancel`. It **initiates** cancellation of a list of transfers that triggered additional review; Adyen sends the cancel-request outcome by webhook. This endpoint is about reviewed transfer requests, not a general reversal of booked transfers or proof that funds were returned. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- Use requires the `TransferService Approve` API-credential role and required account-holder capabilities; the reference directs setup of these permissions through an Adyen contact. The linked capabilities page is navigation, not a list of exact capability names on this capture.
- The optional `Idempotency-Key` header has a 64-character maximum; UUID is recommended. The request-body table marks `transferIds` (array of transfer identifiers) **No**. The example supplies two IDs, but this capture does not separately mark the body required or specify empty-list behavior or a batch maximum.
- The 200 passage says to look at the actual response code for request status; its example body is `{}`. A successful HTTP response does not establish cancellation outcome. Use the later webhook outcome; no cancellation webhook schema or resulting funds movement is shown here.
- 401 authentication, 403 permission, 422 validation and 500 server errors are documented. Their generic error schemas include optional `routingDetails`, which does not itself establish that a cancellation attempt routed a bank transfer.

## Detail locators

- Purpose, review eligibility, role/capability prerequisites, and test server: pinned raw lines 5–18.
- Header and request-body tables, request example: `## Parameters` and `## Request examples`, lines 20–43.
- 200 acknowledgement and error schemas: `## Responses`, lines 44–147; empty 200 example: `## Response examples`, lines 149–156.

## Related

- [[source-adyen-docs-platforms-custom-payouts-on-demand-payouts-approve-cancel-payouts]] — broader platform review lifecycle, with its own scope and qualifications.
- [[adyen-platform-internal-transfers]] — narrower internal-transfer context.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/post/transfers/cancel/2026-09-15|Captured POST /transfers/cancel API Explorer reference (2026-09-15)]]

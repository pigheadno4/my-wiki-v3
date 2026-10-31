---
title: "Adyen Account API v6: Close an account holder"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Account/latest/post/closeAccountHolder"
raw_files:
  - "adyen/api-explorer/Account/latest/post/closeAccountHolder/2026-09-15.md"
tags: [adyen, classic-platforms, account-api, account-holders, closure]
---

## Overview

This API Explorer snapshot, captured 2026-09-15 under `Account/latest`, documents POST `/closeAccountHolder` on the displayed Account v6 test server. It changes a Classic Platforms account holder to `Closed`, a final status. The request identifies the holder by `accountHolderCode`. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- Closure is final: the holder cannot process transactions, receive payouts, or reopen. The page says payments made to an account belonging to a `Closed` holder are sent to the platform's liable account (raw line 7). This is a consequential routing statement, not evidence of an actual payment or transfer.
- The request-body table marks `accountHolderCode` required. The captured page does not document a separate permission name, a closure idempotency key, or a request-body precondition beyond that field (raw lines 12–25). A related Classic verification guide narrows closure of a `Suspended` holder: none of its verification checks may have `FAILED` status. See [[source-adyen-docs-classic-platforms-verification-process]] and its raw status table, line 144; do not apply this condition to every holder status.
- HTTP 200 is described as a succeeded request; HTTP 202 is accepted for processing while processing is incomplete. Both response tables show an optional `accountHolderStatus` object with required `status` if that object is present, plus optional scheduled events, payout and processing state, `invalidFields`, `pspReference` and `resultCode` (raw lines 27–100). A 202 receipt alone does not establish completed closure or any completed financial outcome.
- The listed failures are 400 request reading/understanding, 401 authentication, 403 insufficient permissions, 422 validation, and 500 server processing. The generic 400/403 example codes are examples, not an exhaustive error contract (raw lines 103–191).

## Detail locators

- Endpoint, final-state effects and displayed test server: raw lines 5–10. Required holder code and request example: raw lines 12–25.
- 200 and 202 response descriptions and field schema: raw lines 27–100. In `accountHolderStatus.events`, the schema permits `InactivateAccount` and `RefundNotPaidOutTransfers`; the table describes these as scheduled events, not completed actions (raw lines 35–54 and 72–91).
- Error categories, body fields and generic examples: raw lines 103–191. The 400/403 error-body `pspReference` description says "PSP reference of the payment"; this endpoint is account-holder closure, so do not recast that schema wording as proof of a payment.

## Related

- [[adyen-classic-platforms]] — Classic account-holder context and reciprocal route.
- [[source-adyen-docs-classic-platforms-verification-process]] — separate Classic status matrix and the condition on closing a suspended holder.
- [[adyen-platforms]] — separate newer balance-platform resource model.

## Raw Sources

- [[raw/adyen/api-explorer/Account/latest/post/closeAccountHolder/2026-09-15|Account API Explorer POST closeAccountHolder, captured 2026-09-15]]

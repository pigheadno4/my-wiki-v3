---
title: "POST /transfers/approve — Initiate approval of reviewed transfers | Adyen Transfers API"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/approve"
raw_files:
  - "adyen/api-explorer/transfers/latest/post/transfers/approve/2026-09-15.md"
tags: [adyen, transfers, transfer-review, approval, sca, api-explorer]
---

## Overview

This [[adyen]] Transfers API Explorer snapshot documents `POST /transfers/approve` for initiating approval of transfers that triggered additional review. Adyen says it sends the approval-request outcome through webhooks. The captured server is TEST `https://balanceplatform-api-test.adyen.com/btl/v4`; the URL says `latest`, while the server path identifies `v4`. The transfer IDs identify already initiated transfers, not account holders, balance accounts or recipients. See [[adyen-platforms]].

## Key takeaways

- The page requires an API credential with the **TransferService Approve** role and the account holder's required capabilities; it directs the reader to an Adyen contact to set up those permissions. It does not identify a human approver or state that the API caller and initiating user must be distinct. A separate Business Accounts guide labels the role **TransferService Approval**; preserve this wording discrepancy and verify the applicable grant rather than treating either label as a demonstrated current permission. [Raw: lines 7–15]
- The header table marks `WWW-Authenticate` for SCA and `Idempotency-Key` optional. The latter is described as a unique message identifier of at most 64 characters, with UUID recommended. This page does not say when SCA applies, define a challenge sequence or guarantee replay behavior. [Raw: lines 20–26]
- The body table marks `transferIds` optional and describes it as an array of transfer IDs to approve. The two-ID payload is illustrative; the page states no batch limit, and optionality does not establish what omission does. The related Business Accounts workflow guide gives its own one-to-500 limit and conditional SCA choice, which are not stated in this API Explorer page. [Raw: lines 29–44]
- The 200 section says to look at the actual response code and shows `{}` as its only success example. Since the opening says the approval-request outcome arrives through webhooks, this response is not evidence that review was approved, the transfer finished, funds were booked, or a recipient bank received them. [Raw: lines 5–7, 45–48, 138–145]
- The page lists 401 authentication required, 403 insufficient permissions, 422 validation error and 500 server-processing failure. Error schemas include conditional `routingDetails` with bank-transfer priorities; those nested details do not create a transfer route or success guarantee for this approval call. [Raw: lines 51–136]

## Detail locators

- Purpose, role/capability setup and TEST v4 server: pinned raw lines 5–18.
- Optional SCA/idempotency headers, `transferIds` body field and sample: lines 20–44.
- 200 acknowledgement, error headings/schemas and empty success example: lines 45–145.

## Related

- [[adyen-platforms]] — platform-transfer context and reciprocal route.
- [[source-adyen-docs-business-accounts-send-funds-approve-cancel-transfers]] — separate Business Accounts review guide with batch, conditional SCA and webhook details; its role label differs from this API page.
- [[adyen-business-accounts]] — product context for the related review guide.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/post/transfers/approve/2026-09-15|POST /transfers/approve — captured 2026-09-15]]

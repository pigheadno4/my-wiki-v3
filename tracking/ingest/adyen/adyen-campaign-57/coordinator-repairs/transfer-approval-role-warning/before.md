---
title: "Adyen Business Accounts: Approve or cancel transfer requests"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/send-funds/approve-cancel-transfers"
raw_files:
  - "adyen/docs/business-accounts/send-funds/approve-cancel-transfers/2026-09-15.md"
tags: [adyen, business-accounts, transfers, approvals, sca]
---

## Overview

This 2026-09-15 capture of an Adyen Business Accounts guide (page metadata last modified 2020-09-11) covers an optional additional review of an initiated balance-platform transfer. A reviewer with the stated API role approves or cancels the pending transfer. Approval authorizes Adyen to continue processing; cancellation or 30 days without action causes the pending transfer to fail. None of these review results establishes completed transfer or bank receipt.

## Key takeaways

- The flow begins when the initiating POST `/transfers` request includes a `review` object. The page requires the web-service API key to have the **TransferService Approval role** and a Transfer Webhooks subscription for the approval workflow.
- POST `/transfers/approve` or POST `/transfers/cancel` takes a body `transferIds` array of one to 500 transfer IDs. These identify transfers, not balance accounts or recipient bank accounts. A reviewer can act on multiple pending transfers in one request. Cancellation and 30-day inaction prevent further processing of that transfer request; approval resumes processing.
- If SCA applies, the guide says to authenticate either the initiating user or the approving reviewer. To perform SCA during approval, set `review.scaOnApproval: true` in the initial POST `/transfers` request. The page links to the separate SCA workflow for its implementation.
- HTTP 200 on an approve/cancel API call is a request response, not final settlement proof. Transfer webhooks communicate review state: a created event for `status: received`, `reason: pending`, `review.numberOfApprovalsRequired: 1`; updated events for approved `authorised/approved` or canceled `cancelled/unknown`. The guide describes expiry after 30 days but does not provide an expiry payload example.

## Detail locators

- `## Requirements` and `## How it works` (raw lines 23–50): credential role, webhook prerequisite, review initiation, decision consequences and 30-day deadline.
- `## Approve transfers` (52–259) and `## Cancel transfers` (272–479): endpoints, batch size, TEST examples and HTTP 200 responses. Versioned SDK examples include idempotency keys; this page does not state replay or duplicate-processing semantics.
- `### Strong Customer Authentication (SCA) for approving transfers` (261–270): conditional SCA choice and `scaOnApproval` placement on the initiating request. `## Get status updates on transfer reviews` (481–748): created/updated webhook routes and example status/reason pairs. The introductory event list omits approval, although the later approved tab explicitly documents it; use the approved tab for that path.

## Related

- [[adyen-business-accounts]] — Business Accounts product context.
- [[adyen]] — provider context.
- [[source-adyen-docs-business-accounts-send-funds-make-transfer-request]] — the initiating request and optional review field.

## Raw Sources

- [[raw/adyen/docs/business-accounts/send-funds/approve-cancel-transfers/2026-09-15|Approve or cancel transfers (captured 2026-09-15)]]

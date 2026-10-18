---
title: "Adyen for Platforms transfer approval and cancellation"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/internal-fund-transfers/approve-cancel-transfers"
raw_files:
  - "adyen/docs/platforms/internal-fund-transfers/approve-cancel-transfers/2026-09-15.md"
tags: [adyen, platforms, transfers, approval, cancellation]
---

## Overview

This Adyen for Platforms guide, last modified 2020-09-11 and captured 2026-09-15, describes an optional additional-review gate on Transfers API requests. A platform includes a `review` object in POST `/transfers`; the request waits for a team reviewer to approve or cancel before Adyen processes it. Approval authorizes continued processing, cancellation fails the pending request, and no decision within 30 days also fails it. This page is filed under internal fund transfers, but its webhook examples identify `category: bank` and `type: bankTransfer`; do not treat those illustrative payloads as proof of a two-sided internal balance-account transfer or a bank receipt.

## Key takeaways

- Reviewers require a web service API key with **TransferService Approval role**, and the guide requires Transfer Webhooks. The platform decides which team members have review permission. The page does not specify a separate Customer Area review role or imply that this approval role grants the initial transfer-initiation role.
- POST `/transfers/approve` or `/transfers/cancel` with an array of one to 500 `transferIds`. The code samples target a test endpoint and show an idempotency key for API-library requests. A successful HTTP 200 response to either review call is request acknowledgement; approval means Adyen continues processing, not that funds are booked or received. Cancellation and 30-day no-action expiry stop processing of the pending request, according to this guide. It does not provide a retry, reversal, or post-processing cancellation procedure.
- The pending-review transfer-created webhook uses `status: received`, `reason: pending` and `review.numberOfApprovalsRequired: 1`. The approved transfer-updated webhook uses `status: authorised` and `reason: approved`; the cancellation example uses `status: cancelled` and `reason: unknown`. Do not infer that `reason: unknown` is a universal semantic explanation for cancellations, or that `authorised` proves booked funds. The page names cancellation and 30-day expiry webhook events but provides no separate expired-event payload here.
- The example webhook's `category: bank` and `type: bankTransfer` make its status illustration broader than an internal balance-account movement. Use the relevant transfer-process and webhook guides to check the actual source/destination legs and later outcomes. None of the illustrative webhook balances establishes a specific transfer's legal ownership, completion or beneficiary bank receipt.

## Detail locators

- `Requirements` and `How it works` — reviewer role, webhook subscription, POST `/transfers` review object, pending state, approve/cancel/30-day branches and multiple-transfer review (raw lines 23–50).
- `Approve transfers` — `/transfers/approve`, `transferIds` maximum 500, test request examples and HTTP 200 response (lines 52–259).
- `Cancel transfers` — `/transfers/cancel`, `transferIds` maximum 500, test request examples and HTTP 200 response (lines 261–468).
- `Get status updates on transfer reviews` — transfer-created/updated webhook route, pending/approved/cancelled status and reason values, no-action expiry mention, and bank-transfer example scope (lines 470–736).

## Related

- Company: [[adyen]]
- Main concept: [[adyen-platform-internal-transfers]]
- Parent concept: [[adyen-platforms]]
- Related source: [[source-adyen-docs-platforms-internal-fund-transfers-internal-transfer-webhooks]]

## Raw Sources

- [[raw/adyen/docs/platforms/internal-fund-transfers/approve-cancel-transfers/2026-09-15|2026-09-15 Platforms transfer approval and cancellation guide]]

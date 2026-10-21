---
title: "Approve or cancel Marketplace-path on-demand payouts"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/custom-payouts/on-demand-payouts/approve-cancel-payouts"
raw_files:
  - "adyen/docs/marketplaces/custom-payouts/on-demand-payouts/approve-cancel-payouts/2026-09-15.md"
tags: [adyen, marketplaces, platforms, custom-payouts, payout-review, transfers]
---

## Overview

This 2020-modified, 2026-09-15-captured Marketplace-path guide explains an optional additional review of an initiated on-demand payout transfer before Adyen processes it. The platform includes a `review` object in Transfers API POST `/transfers`; an eligible team reviewer then approves or cancels the pending payout. Approval authorizes continued processing, while cancellation or 30 days without a decision fails that request. These are review-state transitions, not evidence of a booked payout or beneficiary-bank receipt. See [[adyen]] and [[adyen-platforms]] for provider and modern balance-platform context.

## Key takeaways

- The reviewing web-service API key needs **TransferService Approval role**, and the page requires Transfer Webhooks. It describes granting team members the role through Customer Area, but does not establish a mandatory distinct reviewer or a technically enforced separation-of-duties policy. The linked on-demand guide owns the detailed initial payout request.
- Submit POST `/transfers/approve` or `/transfers/cancel` with a `transferIds` array naming one to 500 initiated payouts. The curl examples use a TEST balance-platform `/btl/v4` endpoint, while the SDK snippets have pinned library versions and TEST environments. The page says a successful review API request returns HTTP 200; that acknowledges the review action, not downstream payout or bank credit.
- A `review` object on the original payout transfer makes it pending approval. Approval authorizes the payout request and Adyen continues processing it. Cancellation fails the request and Adyen no longer processes it; no action within 30 days after initiation has the same failure consequence. The page does not provide a same-request retry or post-processing cancellation path.
- Transfer-webhook tracking separates the states: `balancePlatform.transfer.created` identifies a pending review with `status: received`, `reason: pending` and an illustrative `review.numberOfApprovalsRequired: 1`; `balancePlatform.transfer.updated` illustrates approval as `authorised`/`approved` and cancellation as `cancelled`/`unknown`. The prose mentions expiry updates but provides no separate expiry payload. TEST outgoing bank-transfer examples do not demonstrate final booked transfer, bank arrival or a general requirement for exactly one approval.

## Detail locators

- Review purpose, role/webhook requirements, trigger, pending state, approval/cancellation and 30-day no-action failure: raw lines 15–50.
- Approval endpoint, 1–500 IDs, TEST v4 curl/SDK snippets and HTTP 200: lines 52–259. Cancellation endpoint, same bound, TEST snippets and HTTP 200: lines 261–468.
- Review event types and pending/approval/cancellation examples: lines 470–736. `received`/`pending`: 487–560; `authorised`/`approved`: 563–651; `cancelled`/`unknown`: 653–736.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — modern platform balance-account and payout model.
- [[source-adyen-docs-marketplaces-custom-payouts]] — Marketplace custom-payout scope and prerequisites.
- [[source-adyen-docs-platforms-custom-payouts-on-demand-payouts-approve-cancel-payouts]] — separately pinned Platforms-path version of this review guide.

## Related raw API references

- The raw guide links to Transfers API and on-demand payout initiation, plus payout-webhook detail; these pages own current request schema and later financial-state interpretation.

## Raw Sources

- [[raw/adyen/docs/marketplaces/custom-payouts/on-demand-payouts/approve-cancel-payouts/2026-09-15|Adyen Docs: Approve or cancel payouts (2026-09-15 snapshot; page last modified 2020-09-11)]]

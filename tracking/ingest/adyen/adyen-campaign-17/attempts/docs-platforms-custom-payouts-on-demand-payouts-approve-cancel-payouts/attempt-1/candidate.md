---
title: "Approve or cancel Adyen Platforms on-demand payouts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/custom-payouts/on-demand-payouts/approve-cancel-payouts"
raw_files:
  - "adyen/docs/platforms/custom-payouts/on-demand-payouts/approve-cancel-payouts/2026-09-15.md"
tags: [adyen, platforms, custom-payouts, payout-review, transfers]
---

## Overview

This Adyen for Platforms guide, last modified 2020-09-11 and captured 2026-09-15, explains an additional review for an initiated on-demand payout transfer before Adyen processes it. A platform includes a `review` object in a Transfers API `POST /transfers` request; a designated reviewer then approves or cancels the pending request. Approval authorizes that transfer request to continue processing. Cancellation or 30 days without action fails that request so Adyen no longer processes it. These are review transitions, not proof that the user's bank received funds.

## Key takeaways

- The review API key must have the `TransferService Approval role`, and the page requires Transfer Webhooks. The text describes assigning eligible team members the required role through Customer Area; it does not establish that a distinct person or a particular separation-of-duties policy is technically enforced. The linked on-demand payout guide describes how to trigger review with `review` at initiation.
- Use `POST /transfers/approve` or `POST /transfers/cancel` with a body `transferIds` array. Each request can name one to 500 initiated payouts. The curl examples use the balance-platform test endpoint at `/btl/v4`; language SDK examples are versioned and run in TEST. A successful approval/cancellation API call returns HTTP 200, which is a response to the review action rather than bank-credit evidence.
- Approval moves the pending transfer to `authorised` with reason `approved` in the illustrated `balancePlatform.transfer.updated` event and lets Adyen continue processing. Cancellation fails the request, and the illustrated update has status `cancelled` with reason `unknown`. If no reviewer acts within 30 days after initiation, that payout request fails and Adyen no longer processes it. This page does not describe retrying the same failed transfer or creating a replacement request.
- Review state is tracked with Transfer Webhooks: `balancePlatform.transfer.created` identifies a review-required transfer as `received` with reason `pending` and an example `review.numberOfApprovalsRequired=1`; `balancePlatform.transfer.updated` communicates approval or cancellation. The displayed payloads are TEST examples, including outgoing bank-transfer balance mutations. The page lists expiry among webhook events but supplies no separate expiry payload. Neither `received` nor `authorised` establishes booked payout or beneficiary bank receipt.

## Detail locators

- `## Requirements` and `## How it works`: API approval role, Transfer Webhooks, initiation `review` object, pending decision and 30-day expiry.
- `## Approve payouts` and `## Cancel payouts`: `transferIds` body, 500-ID bound, TEST v4 curl/versioned SDK examples and HTTP 200 response.
- `## Get status updates on payout reviews`: created/updated webhook types and review transitions.
- `### Tab: Additional review required`, `### Tab: Payout approved`, `### Tab: Payout canceled`: exact sample `status`, `reason`, approval-count fields and outgoing balance events.

## Related

- [[adyen-platforms]] — main Platforms concept and source route.
- [[source-adyen-docs-platforms-custom-payouts]] — custom-payout scope and prerequisite overview.
- [[source-adyen-docs-platforms-custom-payouts-on-demand-payouts]] — initiation and review-trigger route.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/custom-payouts/on-demand-payouts/approve-cancel-payouts/2026-09-15|Adyen approve or cancel payouts (fetched 2026-09-15)]]

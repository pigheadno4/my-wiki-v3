---
title: "Adyen Payout Service approve or cancel bank payouts"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts/approve-cancel-payouts"
raw_files:
  - "adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/approve-cancel-payouts/2026-09-15.md"
tags: [adyen, payout-service, bank-payouts, transfer-review, transfers-api]
---

## Overview

This [[adyen]] Payout Service bank-payout review guide, last modified 2020-09-11 and captured 2026-09-15, covers an **optional additional review** triggered on a Transfers API payout request. A team member must approve or cancel before Adyen processes it. It belongs under [[adyen-payouts]] and applies to the pending review state of this payout route, not the legacy Online Payout API or a general reversal of already booked payouts.

## Key takeaways

- Include a `review` object in POST `/transfers` to trigger an additional review. The request remains pending approval until a team reviewer acts. Approval authorizes Adyen to **continue processing**, while cancellation or no action within 30 days makes the request fail and prevents further processing. The reviewer permission is controlled by the **TransferService Approval role** on the web service API key; subscribe to Transfer webhooks. See raw lines 19–50.
- POST `/transfers/approve` or POST `/transfers/cancel` with a required `transferIds` array. Each endpoint accepts one or more IDs, up to **500** per request; examples use two IDs and TEST credentials. HTTP 200 is an API-request response, not proof of an individual transfer's later booking, bank credit or return-free completion. See raw lines 52–77, 259–286 and 468.
- Transfer webhooks distinguish a review-required `balancePlatform.transfer.created` with `status: received`, `reason: pending`, `review.numberOfApprovalsRequired: 1`, from an approved `balancePlatform.transfer.updated` with `status: authorised`, `reason: approved`, and a canceled update with `status: cancelled`, `reason: unknown`. The page also says expiry after 30 days generates a review-status notification, though it does not show a separate expiry payload. These are review-stage statuses, not bank-receipt evidence. See raw lines 470–495, 563–571 and 653–660.
- The prose describes cancellation/expiry as a payout that “fails,” while the displayed cancellation webhook uses `status: cancelled`; preserve the distinct prose outcome and event status rather than rewriting cancellation as `status: failed`. The approved sample's outgoing bank transfer has a reservation mutation; it does not show a booked debit or receiving-bank credit. See raw lines 44–48, 623–650 and 653–735.

## Evidence boundary

The review is optional and conditional on the payout request's `review` object. The guide does not say an already processed or booked payout can be cancelled through these endpoints. Approval is a gate that lets processing continue; it is not final payout authorization in a card-payment sense, booked debit, settlement or bank receipt. Batch HTTP 200 and TEST webhook examples do not establish a specific live recipient outcome.

## Detail locators

- Review trigger, role, 30-day expiry and outcomes: raw lines 19–50.
- Approve/cancel batch request shape and TEST examples: raw lines 52–468.
- Review-stage webhook types, fields and examples: raw lines 470–735.

## Related

- [[adyen-payouts]]
- [[source-adyen-docs-payouts-payout-service-payout-lifecycle]]
- [[source-adyen-docs-payouts-payout-service-pay-out-to-bank-accounts]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/approve-cancel-payouts/2026-09-15|Payout Service bank-payout approval/cancellation guide, 2026-09-15 capture]]

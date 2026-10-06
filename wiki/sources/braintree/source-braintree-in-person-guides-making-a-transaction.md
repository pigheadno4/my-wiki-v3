---
title: "Braintree In-Person Sale and Refund Transactions"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/making-a-transaction"
raw_files:
  - "braintree/in-person/guides/making-a-transaction-2026-09-16.md"
tags: [braintree, in-person, card-reader, transactions, refunds]
---

## Overview

This collected [[braintree|Braintree]] website guide describes POS and server coordination with a card reader to request and monitor card-present charges, together with qualified cancellation, partial-authorization, refund and reversal, receipt-data, and manual-entry routes. It is unversioned website guidance, not GitHub or exact-commit schema evidence, current account or hardware eligibility, feature enablement, or proof that an API request was accepted, a card was authorized, a transaction was captured or submitted for settlement, settlement completed, or funds arrived.

## Key takeaways

- A charge request creates an In-Store Context and supplies at least `readerId`, `merchantAccountId`, and `transaction.amount`. The page says Sandbox does not validate the merchant-account ID, while production requires it for all card-reader interactions. Charging is described as authorization followed by automatic capture only if authorization succeeds.
- The request-charge mutation must include a unique `Idempotency-Key`; when communication fails after the customer completes the reader interaction, retrying with the same key is the documented route to recover the original transaction without creating a duplicate charge.
- The charge-request example returns an In-Store Context in `PENDING`; this request acceptance and context state are separate from authorization and capture. The application then polls the context, whose `COMPLETE` state makes a transaction object available; the transaction has its own ID and lifecycle status, and the included successful example is only `SUBMITTED_FOR_SETTLEMENT`, not proof of settlement or funding.
- Cancellation can return the reader to idle only before a payment instrument is presented. A cancel response of `COMPLETE` means the charge was already processed, so the guide says to retrieve status and then perform a reversal or refund; it separately records error code `96716` for attempts to cancel a context already in `PROCESSING` or `COMPLETE`.
- Partial authorization has a page-stated October 2023 behavior and integration path. It can be controlled per transaction with `acceptPartialAuthorization`; otherwise the account feature must be enabled. A partially authorized context is `COMPLETE` with `statusReason` `PARTIALLY_AUTHORIZED`, and the POS must handle the remaining tender rather than treating context completion as full collection.
- Refund paths remain distinct: a referenced refund uses the original transaction ID and cannot exceed its authorized amount; reversal lets Braintree select void versus refund from settlement status; and an unreferenced reader refund requires the customer and payment instrument to be present plus environment-qualified enablement. Unreferenced context `COMPLETE` indicates the refund completed, while the example refund object separately shows `SUBMITTED_FOR_SETTLEMENT`.

## Detail locators

- `Initializing the Reader for Charging` (raw lines 19–30) — minimum request fields, Sandbox/production merchant-account qualification, automatic-capture meaning, idempotency requirement, and request/response examples.
- `Checking the Reader Charge Status` (raw lines 31–43) — customer interaction, two-second polling guidance, context and transaction fields, test-amount qualification, and example pending, complete, decline, network-error, and gateway-reject responses.
- `Charge Flow Example Sequence Diagram` and `Recommended Timeout Logic` (raw lines 44–64) — explicitly illustrative flow, the reader's stated 180-second maximum checkout timeout, and suggested POS request/poll timeout sequence.
- `Cancelling a Charge` (raw lines 66–70) — pre-presentation cancellation boundary, idle-reader effect, processed-context recovery route, and error code `96716`.
- `Partial Authorizations` (raw lines 71–88) — remaining-tender behavior, status fields, Sandbox test amount, API-flag override, and account-level enablement condition.
- `Refunding Your Customer` (raw lines 91–146) — referenced refund, settlement-aware reversal, unreferenced refund and its enablement, refund reversal, and authorization adjustment for partial reversal.
- `Receipt Data Handling` (raw lines 149–192) — provider-described mandatory and optional EMV receipt fields, declined and EMV-chip-declined fields, and the warning that PayPal/Braintree does not enforce EMV-compliant receipts.
- `Manual Key Entry Transactions` (raw lines 195–213) — MOTO or unreadable-card fallback routes through Braintree Hosted Fields or Drop-in UI; the linked integration targets, not this page, govern their exact platform and SDK versions.
- `Important Tips for building out your charge/refund flows` (raw lines 216–231) — merchant-account ID, idempotency, timeout, receipt-data, and reconciliation routes.

## Related

- Company: [[braintree]]
- Concept: [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/in-person/guides/making-a-transaction-2026-09-16|Braintree In-Person Initiate a Sale or Refund (fetched 2026-09-16)]]

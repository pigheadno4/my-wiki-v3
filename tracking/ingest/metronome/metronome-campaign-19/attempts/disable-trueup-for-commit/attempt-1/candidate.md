---
title: "Metronome API: Disable True-up for a Commit"
type: source
date_ingested: 2026-08-21
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/disable-trueup-for-commit.md"
raw_files:
  - "metronome/api-reference/credits-and-commits/disable-trueup-for-commit-2026-07-13.md"
tags: [metronome, api, credits-and-commits, postpaid-commit, true-up]
---

## Overview

This API reference documents `POST /v1/contracts/commits/disableTrueup`, an authenticated operation that prevents Metronome from generating the true-up invoice for one postpaid commit. It is a narrow invoice-generation control: the page does not define a balance mutation, forgiveness of the unmet commitment, or any downstream accounting effect.

## Key takeaways

- Postpaid-commit usage is paid in arrears. When total payment during the access period is below the committed amount, Metronome otherwise describes a final true-up invoice on `invoice_date`.
- The request identifies the customer, contract, and commit with required UUID fields; `amendment_id` is an optional UUID when the commit belongs to an amendment.
- The endpoint says the true-up invoice will not be generated. It does not document a cutoff relative to `invoice_date`, retroactive effect, reversal or re-enablement, repeated-call behavior, or idempotency guarantees.
- The response map documents `200`, `400`, and `404`. Error bodies contain a message, but the page does not enumerate which conditions produce each error.

## Operation and request

The bearer-authenticated endpoint is `POST /v1/contracts/commits/disableTrueup`. Its JSON body requires `customer_id`, `contract_id`, and `commit_id`, each formatted as a UUID. The optional `amendment_id` identifies the amendment containing the commit when applicable.

A successful `200` response contains `data.id` as a UUID. The example value matches the submitted `commit_id`, but the schema names the response only as `Id` and does not independently define whether `data.id` is always the commit ID.

## True-up and lifecycle boundaries

The operation suppresses generation of the final true-up invoice for the identified postpaid commit. The source does not say that it archives, deletes, edits, or resets the commit; changes the access-period usage or paid amount; changes the commit balance or ledger; voids an invoice already generated; or waives the underlying commercial obligation.

The source also does not specify how late the call may occur relative to `invoice_date`, whether it can act after invoice generation or finalization, whether suppression can be reversed, or whether another API or contract edit can re-enable the invoice. No idempotency key, uniqueness key, retry guidance, concurrency behavior, or repeated-call outcome is documented, so safe retry semantics cannot be inferred.

Only generic `400 Bad request` and `404 Not Found` failures are listed. The page does not map malformed identifiers, cross-customer or cross-contract mismatches, wrong commit type, already-generated invoices, repeated calls, or timing violations to specific responses. It likewise does not define propagation to ledger entries, balance retrieval, revenue reports, data exports, webhooks, external accounts-receivable systems, or other invoices.

> [!warning] Scope qualification
> Existing descriptions that a shortfall produces a final postpaid true-up invoice need the qualifier that the invoice may be disabled with this endpoint. That is a conditional exception, not evidence that the normal true-up rule or the underlying commit balance is removed.

## Related

- Companies: [[metronome]]
- Concepts: [[metronome-credits-and-commits]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/disable-trueup-for-commit-2026-07-13|2026-07-13 snapshot — disable-true-up endpoint and OpenAPI schema]]

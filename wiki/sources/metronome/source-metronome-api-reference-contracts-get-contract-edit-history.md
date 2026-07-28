---
title: "Metronome Get Contract Edit History API"
type: source
date_ingested: 2026-07-28
canonical_url: "https://docs.metronome.com/api-reference/contracts/get-contract-edit-history.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/contracts/get-contract-edit-history-2026-07-13.md"
tags: [metronome, contracts, audit-history, api-reference]
---

## Overview

This Metronome API reference documents `POST /v2/contracts/getEditHistory`, an authenticated endpoint that returns the recorded edit history for one customer contract. It supports auditing contract-term changes because Metronome says the history includes edits made in the UI, through `editContract`, and through other contract-changing endpoints such as `updateContractEndDate`.

## Key takeaways

- The request requires UUID `customer_id` and `contract_id` values; the documented response is a `data` array of `ContractEdit` records.
- A `ContractEdit` requires an edit identifier and can include a timestamp and uniqueness key, plus additions, updates, archives, and removals across contract configuration.
- The history can expose changes to overrides, discounts, scheduled charges, commits, credits, recurring commits or credits, usage filters, subscriptions, contract name or end date, refunds, and threshold-billing configuration.
- The reference documents `400` errors with `ContractNotFound` or `CustomerNotFound`; it does not document pagination parameters, cursors, limits, or next-page fields.

## Details

### Request and audit purpose

Send a bearer-authenticated `POST` request to `/v2/contracts/getEditHistory` with the customer and contract UUIDs. The endpoint is an audit view rather than a mutation: it lists the edits made to that contract and is intended to show what changed, when, and by whom.

### Response edit structure

The successful payload contains `data`, an array of `ContractEdit` objects. Each edit requires an `id` and may include `timestamp` and `uniqueness_key`. Its fields are grouped by change operation: additions such as overrides, discounts, scheduled charges, commits, credits, recurring commitments or credits, usage filters, subscriptions, and threshold configurations; updates to those objects as well as contract name, end date, refund invoices, and subscription quantities or seats; and archival or removal arrays for commits, credits, scheduled charges, and overrides. The example demonstrates an added prepaid commit with access and invoice schedules and an added multiplier override.

### Important documented constraints

This endpoint's reference does not define pagination, so a consumer should not assume a cursor or page-size contract from this page. Several embedded edit structures carry their own validation rules: a uniqueness key is 1–128 characters and reusing it for record creation is described as producing a `409`; commit or credit `specifiers` cannot be used together with `applicable_product_ids` or `applicable_product_tags`; and subscription quantity updates require `starting_at`. The endpoint's explicit error response is `400` with a code and message, where the documented codes are `ContractNotFound` and `CustomerNotFound`.

## Related

- Companies: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/get-contract-edit-history-2026-07-13|2026-07-13 snapshot — Get Contract Edit History API schema]]

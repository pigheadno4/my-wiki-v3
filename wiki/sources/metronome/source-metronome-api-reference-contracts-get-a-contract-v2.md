---
title: "Metronome API: Get a Contract (v2)"
type: source
date_ingested: 2026-08-26
canonical_url: "https://docs.metronome.com/api-reference/contracts/get-a-contract-v2.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/contracts/get-a-contract-v2-2026-07-13.md"
tags: [metronome, api, contracts, credits, commits]
---

## Overview

Bearer-authenticated `POST /v2/contracts/get` retrieves one customer's contract by `customer_id` and `contract_id`. It is the contract-state read for inspecting the term, pricing configuration, credits and commits, charges, transitions, schedules, and other attached configuration, including a historical view through `as_of_date`.

## Query-critical facts

- The payload schema requires UUID `customer_id` and `contract_id` properties. The enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is not established.
- `as_of_date` accepts an optional RFC 3339 timestamp and returns the full contract configuration as of that point, supporting inspection of terms that changed through edits.
- `include_balance` adds credit and commit balances, and `include_ledgers` adds their ledgers; both make the query slower. `include_ledgers` cannot be combined with `as_of_date`.
- The success response wraps a `ContractV2` object in `data`. Its core identity includes contract `id`, `customer_id`, and `starting_at`; the larger response can expose pricing, commitments, credits, overrides, scheduled charges, transitions, statement schedules, subscriptions, thresholds, provider schedules, and hierarchy configuration.
- `has_more.commits` or `has_more.credits` indicates that this contract read omitted additional items; callers must use the respective list endpoints for complete collections.
- The documented `400` response distinguishes `CustomerNotFound` and `ContractNotFound`.

## Material boundaries

- The request object does not declare `additionalProperties: false`; unknown-field rejection must not be inferred. Some response fields are explicitly client-configuration- or feature-dependent, so schema presence does not establish universal availability.
- The balance schema defines a current accessible balance, including future-dated manual ledger entries for active segments, while `as_of_date` provides historical contract configuration. This page does not define historical balance semantics, and it forbids only `include_ledgers`—not `include_balance`—with `as_of_date`; do not assume the balance is historical or snapshot-consistent.
- The API-wide [[source-metronome-api-reference-idempotency|POST idempotency authority]] applies `Idempotency-Key` result replay to this POST read. Replaying a key can return the original result and therefore is not proof of a fresh contract read; this endpoint adds no cache, freshness, read-after-edit consistency, concurrency, or recovery guarantee.

## Raw detail coverage

The exact request fields, complete `ContractV2` property catalog, required and nullable fields, enums, examples, feature-gated fields, balance and ledger-entry unions, schedules, overrides, recurring grants, thresholds, subscriptions, hierarchy objects, provider configuration, and error schemas remain in the complete raw reference linked below.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-contracts-amend-a-contract]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/get-a-contract-v2-2026-07-13|2026-07-13 snapshot - complete endpoint, response schema, examples, and error definitions]]

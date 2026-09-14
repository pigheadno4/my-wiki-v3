---
title: "List customer contracts (v1)"
type: source
date_ingested: 2026-09-13
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/contracts/list-customer-contracts-v1"
raw_files:
  - "metronome/api-reference/contracts/list-customer-contracts-v1-2026-08-28.md"
tags: [metronome, api-reference, contracts, customers]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/contracts/list`, which retrieves all contracts for one customer for contract-history and current-agreement views. The response can include pricing and terms plus credits, commitments, optional ledgers, and optional balances.

> [!warning] Legacy version
> This is the legacy v1 operation. Metronome directs new integrations to the v2 endpoint for enhanced features; this source does not establish request or response compatibility between the versions.

## Query-critical routes

- Within a supplied JSON object, UUID `customer_id` is the only required property. The enclosing OpenAPI `requestBody` is not marked required.
- `starting_at` selects contracts whose `effective_at` is on or after an RFC 3339 timestamp, while `covering_date` selects contracts effective on a timestamp; the two filters cannot be supplied together. `include_archived` controls archived-contract inclusion.
- `include_ledgers` requests commit ledgers and `include_balance` requests credit and commit balances; Metronome warns that either option may make the query slower.
- HTTP `200` places an array of `Contract` objects at top-level `data`. Each `Contract` requires identity plus `initial`, `current`, and `amendments`; use the referenced component schemas for their exact nested pricing, term, credit, commitment, transition, subscription, threshold, hierarchy, and billing-provider fields.

## Raw-detail locators

- Operation identity, bearer security, version warning, and request selectors: OpenAPI `paths./v1/contracts/list.post`, especially `requestBody.content.application/json.schema` (raw lines 20-145).
- Success envelope and immediate contract placement: `paths./v1/contracts/list.post.responses.200.content.application/json.schema` (raw lines 147-160).
- Returned contract structure: `components.schemas.Contract`, `ContractWithoutAmendments`, and `ContractAmendment` (beginning at raw lines 330, 450, and 636).
- Optional commit and credit expansions: `components.schemas.Commit` and `Credit`; ledger variants are under `CommitLedger` and `CreditLedger`, and calculated balance semantics are under `BalanceForCommitsAndCredits` (raw lines 886-1223 and 2081-2161).

## Related

- Company: [[metronome]]
- Main concept: [[metronome-customers-and-contracts]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/list-customer-contracts-v1-2026-08-28|2026-08-28 snapshot - legacy customer-contract listing operation, filters, response contract schemas, ledger variants, and balance semantics]]

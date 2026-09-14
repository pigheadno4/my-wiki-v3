---
title: "Metronome API: List Customer Contracts (v2)"
type: source
date_ingested: 2026-09-13
canonical_url: "https://docs.metronome.com/api-reference/contracts/list-customer-contracts-v2"
original_format: webpage
raw_files:
  - "metronome/api-reference/contracts/list-customer-contracts-v2-2026-08-28.md"
tags: [metronome, api-reference, contracts, customers, contract-history]
---

## Overview

This API reference documents bearer-authenticated `POST /v2/contracts/list` for listing one customer's contracts in chronological order. Use it to determine whether a customer has a contract, inspect the current agreement, or build a history of the customer's contract tiers; use the distinct contract-get operation when selecting one contract by ID.

## Query-critical facts

- Within the JSON payload, `customer_id` is required. The optional `starting_at`, `covering_date`, and `include_archived` fields select the returned contract history; `starting_at` and `covering_date` cannot be supplied together.
- Passing `covering_date` equal to the current time is the documented way to list contracts active now. The page describes the overall result order as chronological.
- Optional `include_ledgers` and `include_balance` controls add commit/credit ledger or balance detail, and the page warns that either expansion may make the response slower.
- HTTP `200` places the contract array at `data`; each item routes to `components.schemas.ContractV2`.

## Material completeness boundary

> [!warning] Embedded commit and credit collections can be incomplete
> A returned contract can expose `has_more.commits` or `has_more.credits`. When either flag is true, use the respective dedicated list endpoint for the full collection rather than treating the embedded contract arrays as complete.

## API and raw-detail locators

- **Operation and authentication:** `## OpenAPI` -> document-level `security` -> `bearerAuth`, and `paths` -> `/v2/contracts/list` -> `post`.
- **Customer and history selection:** the operation's `requestBody` -> `application/json` -> `schema` documents required `customer_id` and the optional archive, time, ledger, and balance controls, including the mutually exclusive time filters.
- **Response placement and contract detail:** the operation's `responses` -> `200` -> `application/json` requires `data`, whose array items reference `components.schemas.ContractV2`; that schema routes the complete contract, pricing, grants, schedules, provider configuration, subscription, threshold, hierarchy, and feature-qualified detail.
- **Embedded collection completeness:** `components.schemas.HasMore` documents the commit and credit flags and names the dedicated list routes. The operation's `responses` -> `400` contains its documented error shape.

## Related

- Company: [[metronome]]
- Primary concept: [[metronome-customers-and-contracts]]
- Single-contract retrieval: [[source-metronome-api-reference-contracts-get-a-contract-v2]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/list-customer-contracts-v2-2026-08-28|List customer contracts (v2)]] — complete collected documentation and embedded OpenAPI operation

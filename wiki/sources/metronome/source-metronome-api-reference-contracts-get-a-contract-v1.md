---
title: "Metronome API Reference: Get a Contract (v1)"
type: source
date_ingested: 2026-09-13
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/contracts/get-a-contract-v1"
raw_files:
  - "metronome/api-reference/contracts/get-a-contract-v1-2026-08-28.md"
tags: [metronome, contracts, api, retrieval]
---

## Overview

This API reference documents the legacy v1 operation for retrieving one identified customer's contract. It provides exact navigation to the selectors, optional balance and ledger expansions, and the returned contract representation.

## Key takeaways

- Send a bearer-authenticated `POST` request to `/v1/contracts/get`. Within a supplied JSON object, `customer_id` and `contract_id` are required UUID selectors; the OpenAPI operation does not mark the enclosing `requestBody` as required.
- `include_ledgers` and `include_balance` optionally expand commit-ledger and credit/commit-balance detail, and the documentation warns that either expansion may make the query slower.
- A successful response places the selected contract under `data`; its detailed state is defined at `components.schemas.Contract` and the referenced component schemas.

> [!warning] Legacy version
> This is the v1 get-contract endpoint. Metronome directs new clients to implement the v2 endpoint.

## Detail navigation

- Operation, method, path, and authentication: `OpenAPI > security` and `paths > /v1/contracts/get > post`.
- Contract selectors and optional expansions: `paths > /v1/contracts/get > post > requestBody > content > application/json > schema > required/properties`.
- Success envelope and returned contract detail: `paths > /v1/contracts/get > post > responses > 200 > content > application/json > schema > properties > data`, then `components > schemas > Contract` and its referenced schemas.
- Not-found response: `paths > /v1/contracts/get > post > responses > 404` and `components > responses > NotFound`.

## Related

- Companies: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/get-a-contract-v1-2026-08-28|Get a contract (v1) — 2026-08-28]] — complete pinned API reference and OpenAPI schema

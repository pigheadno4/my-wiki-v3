---
title: "Metronome API: Get the Net Balance of a Customer"
type: source
date_ingested: 2026-09-09
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/get-the-net-balance-of-a-customer"
raw_files:
  - "metronome/api-reference/credits-and-commits/get-the-net-balance-of-a-customer-2026-08-28.md"
tags: [metronome, api-reference, credits, commits, customer-balance]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/contracts/customerBalances/getNetBalance` operation. It returns one customer's combined current balance across the matching credits and commits rather than the individual balance and ledger detail exposed by `listBalances`.

## Key takeaways

- Separate filter objects are ORed: a credit or commit is included when it matches any object. Conditions within one filter object are ANDed. Filters can narrow the calculation by balance type, exact credit or commit ID, and custom fields.
- The response places numeric `balance` and UUID `credit_type_id` inside the required `data` object. The credit type identifies the fiat or custom pricing unit in which the balance is denominated; omitting `credit_type_id` defaults the calculation to USD cents.
- `invoice_inclusion_mode` defaults to `FINALIZED_AND_DRAFT`, which includes deductions from pending draft invoices; `FINALIZED` excludes those draft deductions.
- The feature-annotated `access_type` defaults to `SPEND`. Selecting `QUANTITY` forbids supplying `credit_type_id`; use the raw request schema for its accepted values and placement.

> [!warning] Customer-hierarchy scope
> A child-customer query excludes shared commits from parent contracts. Query the parent customer directly when those shared commit balances are required.

> [!warning] Negative-segment calculation
> Manual ledger entries can make an individual segment balance negative, but this endpoint treats that segment as zero when calculating the combined net balance. Use `listBalances` for the underlying per-balance ledger detail.

## API and detail locators

- Operation and authentication: `## OpenAPI` -> document-level `security` -> `bearerAuth`, and `paths` -> `/v1/contracts/customerBalances/getNetBalance` -> `post`.
- Request selection: `requestBody` -> `content` -> `application/json` -> `schema` -> `properties` documents `credit_type_id`, `access_type`, `filters`, and `invoice_inclusion_mode`; `components` -> `schemas` -> `BalanceFilter` holds the balance-type, ID, and custom-field detail. The payload schema requires `customer_id`, while the enclosing OpenAPI `requestBody` is not marked required, so omitted-body runtime behavior is not established.
- Response placement: `responses` -> `200` -> `content` -> `application/json` -> `schema` requires outer `data`, then requires `balance` and `credit_type_id` within that object. The same response section routes the example; `responses` -> `400` routes the generic error schema.

## Related

- Company: [[metronome]]
- Main concept: [[metronome-credits-and-commits]]
- Detailed balances and ledgers: [[source-metronome-api-reference-credits-and-commits-list-balances]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/get-the-net-balance-of-a-customer-2026-08-28|Get the net balance of a customer]] — complete collected documentation and embedded OpenAPI operation

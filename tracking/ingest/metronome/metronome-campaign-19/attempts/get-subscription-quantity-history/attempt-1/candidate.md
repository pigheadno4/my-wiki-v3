---
title: "Metronome Get Subscription Quantity History API"
type: source
date_ingested: 2026-08-21
canonical_url: "https://docs.metronome.com/api-reference/contracts/get-subscription-quantity-history.md"
original_format: webpage
raw_files:
  - "metronome/api-reference/contracts/get-subscription-quantity-history-2026-07-13.md"
tags: [metronome, contracts, subscriptions, seat-based-billing, api-reference]
---

## Overview

This Metronome API reference documents `POST /v1/contracts/getSubscriptionQuantityHistory`, a bearer-authenticated read endpoint for retrieving a subscription's historical quantities and prices. It is intended to support customer-facing views of seat-count changes, but it deliberately excludes future scheduled quantity changes.

## Key takeaways

- The JSON request schema requires UUID `customer_id`, `contract_id`, and `subscription_id` identifiers.
- The successful response requires a top-level `data` value whose schema can contain the subscription identifier, a fiat credit-type identifier, and an array of effective-dated history entries.
- Every history entry requires `starting_at` and `data`; each item in `data` requires numeric `quantity`, `unit_price`, and `total` values.
- Historical quantity and price states can support an in-product seat-count history. Future scheduled quantity changes are outside this endpoint and must be viewed through `getContract`.
- The documented error response is HTTP `400` with `code` and `message`; the listed codes are `ContractNotFound`, `CustomerNotFound`, and `SubscriptionNotFound`.

## Request and authentication

Send a bearer-authenticated `POST` request to `/v1/contracts/getSubscriptionQuantityHistory`. The request schema requires three UUID strings: `customer_id`, `contract_id`, and `subscription_id`. The page does not document query parameters, pagination inputs, or a request-side time range.

## Response history structure

A `200` response requires a top-level `data` property referencing `SubscriptionQuantityHistory`. That object defines optional `subscription_id`, `fiat_credit_type_id`, and `history` properties. Each item in `history` requires a date-time `starting_at` and a `data` array; every data item requires numeric `quantity`, `unit_price`, and `total` fields.

The example contains one effective date with a single quantity-price-total item and a later effective date with two items. The reference does not define the business relationship among multiple items at one effective date, the monetary scale or currency semantics of `unit_price` and `total`, or whether `total` is always calculated as quantity multiplied by unit price.

## Historical and ordering boundaries

The endpoint returns historical quantities and prices, including information suited to showing changes in seat count. It does not include future changes even though subscription quantity can be changed for a past or future effective time; the page directs consumers to `getContract` for future scheduled quantity changes.

`starting_at` identifies when a history entry begins, but the page does not document an ending timestamp, sort order, duplicate handling, pagination, retention window, or whether the returned history is exhaustive. Consumers should not infer chronological ordering from the displayed example.

## Errors and undocumented behavior

The only documented error response is HTTP `400`, whose schema requires string `code` and `message` fields. The enumerated codes cover missing contracts, customers, and subscriptions. This page does not specify authorization-failure responses, malformed-UUID behavior, identifier-ownership mismatch behavior, rate limits, retry semantics, or whether an empty history is possible.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-subscriptions]], [[metronome-customers-and-contracts]]
- Related audit endpoint: [[source-metronome-api-reference-contracts-get-contract-edit-history]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/get-subscription-quantity-history-2026-07-13|2026-07-13 snapshot — subscription quantity and price history API schema]]

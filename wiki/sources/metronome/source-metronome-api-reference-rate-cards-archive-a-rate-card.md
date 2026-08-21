---
title: "Metronome API: Archive a Rate Card"
type: source
date_ingested: 2026-08-21
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/rate-cards/archive-a-rate-card.md"
raw_files:
  - "metronome/api-reference/rate-cards/archive-a-rate-card-2026-07-13.md"
tags: [metronome, api, rate-cards, pricing-lifecycle, archival]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/contract-pricing/rate-cards/archive` operation. Metronome describes archival as a permanent disablement that prevents the card from being used in new contracts and removes it from contract-creation workflows while preserving pricing for existing contracts. The page defines a small ID-in/ID-out schema and a `404` response, but it does not define restoration, propagation mechanics, concurrent requests, or retry semantics.

## Key takeaways

- Archiving permanently disables the rate card for new contracts and stops it from appearing in contract-creation workflows.
- Existing contract pricing is preserved, but the page does not explain whether that means a copied pricing snapshot, a retained reference, or some other mechanism.
- The JSON body uses the `Id` schema, whose `id` property is a required UUID; the `requestBody` object itself is not marked `required: true`.
- A successful `200` response requires `data`, which uses the same required-UUID `Id` schema. The only operation-specific error listed is `404` for a resource that was not found.

## Endpoint contract

| Item | Documented value |
| --- | --- |
| Method and path | `POST /v1/contract-pricing/rate-cards/archive` |
| Operation ID | `archiveRateCard-v1` |
| Authentication | Top-level HTTP bearer authentication through `bearerAuth` |
| Request media type | `application/json` |
| Request shape | `Id`; its `id` field is required and formatted as a UUID |
| Success | `200`; the response object requires `data`, which is an `Id` object |
| Listed endpoint error | `404`; `Error.message` is required |

The request description says the caller supplies the rate-card ID to archive. Although the referenced `Id` schema requires `id`, this OpenAPI fragment does not mark the enclosing `requestBody` as required. It therefore does not explicitly establish the runtime behavior of an omitted body, a missing ID, a malformed UUID, or an extra property.

## Archive lifecycle and contract boundary

The stated future-use boundary is narrow: an archived card cannot be used in new contracts and no longer appears in contract-creation workflows. The page does not say whether an archived card remains retrievable through other API or dashboard views, whether its aliases remain resolvable, or how an in-flight contract-creation request is handled.

For contracts that already use the card, the page promises preserved pricing. It does not define whether the contract retains a live card relationship or a snapshot, whether later card or product changes can still propagate, how draft or finalized invoices are affected, or when the preservation becomes effective. Calling the operation permanent establishes durable disablement, but this page documents no restoration endpoint, deletion behavior, retention period, or audit-history representation.

## Errors, retries, and concurrency

The operation lists only `404`, with the generic message that the specified resource was not found. It does not distinguish a nonexistent ID from an already archived card or describe whether authorization filtering can also appear as not found. The operation does not list validation, authentication, authorization, conflict, rate-limit, or server-error responses.

This endpoint page does not mention `Idempotency-Key`, duplicate archive calls, atomicity, concurrency ordering, race behavior with contract creation, or retry guidance. Those behaviors must not be inferred from the successful response or the word "permanently"; consult the separate API-wide authentication, status-code, and idempotency references when implementing a client.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-products-and-rate-cards]], [[metronome-customers-and-contracts]]
- API operations: [[metronome-api-idempotency]]
- Related sources: [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-status-codes]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/rate-cards/archive-a-rate-card-2026-07-13|2026-07-13 snapshot — archive endpoint, lifecycle description, request and response schemas]]

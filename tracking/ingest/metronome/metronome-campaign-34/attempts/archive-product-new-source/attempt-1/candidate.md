---
title: "Metronome Archive a Product API"
type: source
date_ingested: 2026-08-31
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/products/archive-a-product"
raw_files:
  - "metronome/api-reference/products/archive-a-product-2026-07-13.md"
tags: [metronome, api, products, rate-cards, pricing-lifecycle, archival]
---

## Overview

This OpenAPI page documents bearer-authenticated `POST /v1/contract-pricing/products/archive`, an irreversible product-lifecycle mutation selected by product UUID. Archival preserves the operation of rate cards already associated with the product, prevents the product from being selected for newly created rates, and retains product retrieval through the UI and API.

## Query-critical facts

- A supplied JSON payload requires UUID `product_id`, which identifies the product to archive. The enclosing OpenAPI `requestBody` is not marked `required: true`, so omitted-body behavior is not established; the payload schema also does not declare `additionalProperties: false`, so unknown-field behavior is undocumented.
- Archival changes future pricing-catalog availability rather than erasing the product: current associated rate cards continue to function, while newly created rates can no longer select the archived product. The page does not say that an existing rate is recreated, modified, frozen, or detached.
- The archived product remains retrievable in the UI and API. Current List authority separately excludes archived products by default unless its archive filter includes them, while Get remains the single-product route; neither adjacent read substitutes for this mutation's lifecycle contract.
- Product archival cannot be reversed. The page names no unarchive, delete, replacement, or restoration workflow and does not establish whether creating another product preserves identity, references, history, rates, or reporting continuity.
- HTTP `200` requires top-level `data`, whose generic `Id` object requires UUID `id`; the example repeats the requested product UUID, but the schema does not separately label the returned value as product-resource identity rather than archive-operation identity. A successful ID response does not itself expose the archived representation, affected rate cards or rates, propagation state, or completion timestamp.

## Material boundaries

“Current rate cards ... continue to function as normal” is limited to already associated rate cards, and “no longer available ... for newly created rates” is limited to future rate creation. The page does not define behavior for concurrent product archival and rate creation; in-flight or scheduled rate changes; aliases, packages, contracts, overrides, entitlements, commits, credits, or discounts; rating of late or corrected usage; draft, finalized, regenerated, or historical invoices; exports and reports; or whether existing-rate preservation uses a snapshot or retained product reference. Do not convert the narrow continuity statement into a guarantee that every historical or downstream financial result is unchanged.

The endpoint lists generic HTTP `400 Bad request` and `404` not-found responses whose shared error schema requires string `message`. It does not map malformed or missing input, an unknown or already archived product, forbidden visibility, incompatible current state, conflict, rate limiting, timeout, or server failure to specific behavior; nor does it define atomicity, rollback, concurrent mutation ordering, read-after-write visibility, propagation timing, affected-object discovery, or partial-effect recovery.

Because this mutation uses POST, the separate API-wide [[metronome-api-idempotency|`Idempotency-Key` authority]] applies: after execution begins, identical same-key parameters replay the original result, changed parameters return HTTP `409`, keys persist for at least 24 hours, and a cached result can be HTTP `500`. This endpoint adds no archive-specific guarantee for no-key, different-key, or expired-key calls; repeated archival or an already archived product; concurrency with new-rate creation or product reads; cached or ambiguous failures; or propagation and recovery. Same-key replay recovers the original result, not fresh proof that every catalog, rate, contract, invoice, export, or UI surface reflects the archive. [[source-metronome-api-reference-idempotency]]

## Raw-detail coverage map

- **Operation and identity:** production server, bearer security, POST path, operation ID, request example, required payload `product_id`, UUID format, and absent request-wrapper required marker are in raw.
- **Lifecycle:** existing associated-rate-card continuity, exclusion from newly created rates, retained UI/API retrieval, and irreversible no-unarchive boundary are in raw; restoration, deletion, replacement, propagation, and affected-object enumeration are not documented.
- **Response placement:** required top-level `data`, nested required UUID `id`, repeated-ID example, and lack of an archived product representation, operation identity, affected-rate list, state marker, or completion time are in raw.
- **Failures and schema limits:** generic `400`, generic `404`, required error message, schemas without closed-object declarations, and the absence of endpoint-specific conflict, retry, concurrency, atomicity, rollback, or recovery rules are in raw.
- **Authority boundary:** use Product Get and archive-filtered List for their own retrieval contracts, rate-card authorities for rate-card and contract-pricing lifecycle, and the API-wide idempotency source for request-result replay. None extends this page's narrow continuity claim to historical rating, invoice recalculation, downstream reporting, or cross-surface propagation.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-products-and-rate-cards]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-products-get-a-product]], [[source-metronome-api-reference-products-list-products]], [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]], [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]], [[source-metronome-api-reference-rate-cards-archive-a-rate-card]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/products/archive-a-product-2026-07-13|2026-07-13 snapshot - complete product-archive lifecycle statement, request and response identity schemas, errors, and OpenAPI metadata]]

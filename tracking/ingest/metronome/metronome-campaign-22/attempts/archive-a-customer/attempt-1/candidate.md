---
title: "Metronome API Reference: Archive a Customer"
type: source
date_ingested: 2026-08-24
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/customers/archive-a-customer.md"
raw_files:
  - "metronome/api-reference/customers/archive-a-customer-2026-07-13.md"
tags: [metronome, customers, api-reference, archival, contracts, invoices, notifications]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/customers/archive` operation for irreversibly archiving a Metronome customer while preserving API and UI visibility for audit. The endpoint automatically archives the customer's contracts as of the current date, voids all corresponding invoices, preserves ingest-alias reservation, and stops associated notifications from being triggered. Exact invoice-state treatment, downstream effects, retry recovery, and transaction boundaries remain outside this endpoint's documented contract.

## Key takeaways

- Customer archival is intended for a customer onboarded by mistake and cannot be reversed through unarchiving; the archived customer remains viewable through the API and UI for audit purposes.
- Archiving automatically archives all contracts as of the current date and voids all corresponding invoices. The page does not distinguish invoice states or establish effects in Stripe, an ERP, a marketplace, a payment processor, or another customer-A/R system.
- An archived customer's ingest aliases remain reserved. To reuse one, it must be removed from the customer before archival; this alias mechanism is separate from request-result replay through `Idempotency-Key`.
- Notifications associated with the customer will no longer be triggered, but the page does not identify notification families or define queued-event, webhook-delivery, or in-flight behavior.
- The enclosing OpenAPI `requestBody` is not marked `required: true`, while its referenced `Id` payload schema requires one UUID-formatted `id`; omitted-body and unknown-property behavior are undocumented.
- HTTP `200` requires `data` containing an `Id`; the operation also lists `400 Bad request` and generic `404 Not Found` responses whose error object requires string `message`.

## Endpoint and request contract

The documented production server is `https://api.metronome.com`, the operation ID is `archiveCustomer-v1`, and the OpenAPI document applies HTTP bearer authentication. The operation defines no path or query parameters. Its JSON request body references the generic `Id` object, whose required `id` property is a UUID-formatted string.

The operation's `requestBody` supplies a description, JSON schema reference, and example but does not set `required: true`. Requiredness of payload property `id` must therefore remain separate from operation-level body requiredness. Neither the request wrapper nor `Id` schema specifies `additionalProperties`, so the page does not establish whether unknown request fields are accepted, ignored, or rejected. It also does not document lookup by ingest alias, deprecated external ID, contract ID, or invoice ID.

## Customer, contract, and invoice lifecycle

Metronome positions this operation as cleanup for a customer onboarded by mistake. Archival is irreversible according to the page, but it preserves the customer record for audit access through both the API and UI. The page does not define retention duration, API retrieval route, authorization for archived records, archive timestamp visibility, propagation latency, or read-after-write consistency; the separate customer get and list references own their response schemas and filters.

The mutation automatically archives all contracts effective as of the current date and voids all corresponding invoices. The page supplies no contract or invoice identifiers and no control equivalent to the contract-archive endpoint's `void_invoices` flag. It does not partition draft, scheduled, finalized, already distributed, corrected, or previously voided invoices; define contract-term, credit, commit, balance, or ledger effects; or establish ordering and atomicity across customer, contract, and invoice changes.

The phrase "void all corresponding invoices" is scoped to this customer-archive authority. It does not establish cancellation in Stripe, an ERP, a marketplace, a payment processor, or another customer-A/R system, nor does it prove refund, tax, accounting, revenue, settlement, or reconciliation outcomes. The separate credit-memo authority states that a Metronome invoice void does not itself void a downstream invoice, so operators must not extend this endpoint's wording into downstream completion.

## Ingest aliases and notification boundary

The page says ingest aliases remain idempotent for archived customers and directs callers to remove an alias before archival if they need to reuse it. That durable reservation is a customer-identity mechanism: the page does not define the removal operation, alias normalization, archive-versus-removal races, whether all aliases are released atomically, or any post-archive release path. It must not be conflated with the API-wide `Idempotency-Key` header used for POST retries.

Associated notifications will no longer be triggered after archival. The endpoint does not identify whether this covers threshold, system, offset, or other notifications; define timing relative to the archive response; or specify handling for an evaluation already running, an event already created, or a webhook already queued or delivered. It therefore establishes trigger suppression wording, not webhook cancellation, delivery recall, or downstream action reversal.

## Success, errors, idempotency, and recovery

HTTP `200` requires a top-level `data` property referencing the generic `Id` schema, which in turn requires UUID `id`. The response example repeats the request UUID, but the generic schema does not separately label the returned value or include archival state, `archived_at`, affected contract or invoice identifiers, notification status, or an operation record. A successful response therefore does not by itself expose completion details for each documented side effect.

The endpoint lists `400 Bad request` and `404` for a specified resource not found. Both use an error object requiring string `message`; no machine-readable error code or field-level validation detail is supplied. The page does not distinguish malformed or missing bodies, malformed UUIDs, inaccessible customers, active versus already archived state, or failures during contract, invoice, alias, or notification effects, and it does not list operation-specific `401`, `403`, `409`, `429`, or `5xx` responses.

The separate [[source-metronome-api-reference-idempotency|API-wide idempotency authority]] applies `Idempotency-Key` to all POST endpoints: the same key with identical parameters returns the original result, changed parameters return HTTP `409 Conflict`, keys persist for at least 24 hours, and a cached result can be HTTP `500`. This archive endpoint neither repeats nor narrows those guarantees. A same-key replay recovers the original result rather than proving a fresh archive execution or a current read of every side effect; neither authority defines archive-specific no-key or different-key behavior, expired-key retries, repeated archival, concurrency ordering, partial-failure state, safe changed-key recovery, or reconciliation after an ambiguous response.

## Authority separation and contradiction check

No direct contradiction was found when each authority remains source-scoped. The get-customer schema's optional nullable `archived_at` and the list endpoint's `only_archived` filter are consistent with this page's explicit API visibility claim, while those read authorities still own their exact response and filtering contracts. The API-wide idempotency authority independently confirms that ingest aliases remain reserved when a customer is archived and separately defines POST header replay.

The contract-archive source gives state-specific invoice effects and a required finalized-invoice flag for that different mutation, whereas this customer-archive page broadly says all corresponding invoices are voided with no flag. The invoice-void and credit-memo authorities likewise provide narrower Metronome-versus-downstream boundaries. These are unresolved scope differences between distinct operations, not evidence that customer archival exposes the contract endpoint's flag, invoice eligibility rules, balance effects, or downstream cancellation.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-alerts-and-notifications]], [[metronome-api-idempotency]]
- Customer and contract context: [[source-metronome-api-reference-customers-get-a-customer]], [[source-metronome-api-reference-customers-list-customers]], [[source-metronome-api-reference-contracts-archive-a-contract]]
- Invoice context: [[source-metronome-api-reference-invoices-void-an-invoice]], [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]]
- API context: [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-status-codes]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/customers/archive-a-customer-2026-07-13|2026-07-13 snapshot — customer archival lifecycle, aliases, notifications, and OpenAPI contract]]

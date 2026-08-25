---
title: "Metronome API Reference: Archive a Customer"
type: source
date_ingested: 2026-08-25
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/customers/archive-a-customer.md"
raw_files:
  - "metronome/api-reference/customers/archive-a-customer-2026-07-13.md"
tags: [metronome, customers, api-reference, archival, contracts, invoices, notifications]
---

## Overview

This API reference documents the bearer-authenticated `POST /v1/customers/archive` operation on the production server `https://api.metronome.com`. It irreversibly archives a Metronome customer while preserving API and UI visibility for audit, automatically archives the customer's contracts as of the current date, voids all corresponding invoices, preserves ingest-alias reservation, and stops associated notifications from being triggered. Exact invoice-state treatment, notification timing, downstream effects, retry recovery, and transaction boundaries remain outside this endpoint's documented contract.

## Key takeaways

- Customer archival is intended for a customer onboarded by mistake. The customer cannot be unarchived but remains viewable through the API and UI for audit.
- Archiving automatically archives all contracts as of the current date and voids all corresponding invoices. The endpoint does not partition invoice states or expose a control over those effects.
- An archived customer's ingest aliases remain reserved. To reuse an alias, it must be removed from the customer before archival.
- The archive page says associated notifications will no longer be triggered; it does not define timing or treatment of notification work already generated or in flight.
- The enclosing OpenAPI `requestBody` is not marked `required: true`, while the referenced `Id` payload requires one UUID-formatted `id`. Omitted-body and unknown-property behavior are undocumented.
- HTTP `200` requires `data` containing an `Id`. The operation also lists `400 Bad request` and generic `404 Not Found`; their error schema requires string `message`.

## Endpoint and request contract

The OpenAPI document names `https://api.metronome.com` as the production server and applies top-level HTTP bearer authentication. The operation ID is `archiveCustomer-v1`; the operation defines no path or query parameters. Its JSON request body references the generic `Id` object, whose required `id` property is a UUID-formatted string.

The operation's `requestBody` supplies a description, JSON schema reference, and example but does not set `required: true`. Requiredness of payload property `id` is therefore distinct from operation-level body requiredness. Neither the request wrapper nor `Id` specifies `additionalProperties`, so the page does not establish whether unknown request fields are accepted, ignored, or rejected. It also does not document lookup by ingest alias, deprecated external ID, contract ID, or invoice ID.

## Customer, contract, and invoice lifecycle

Metronome positions this operation as cleanup for a customer onboarded by mistake. Archival is irreversible, but the archived customer remains visible through both the API and UI for audit. The page does not define retention duration, the retrieval route, authorization for archived records, archive timestamp visibility, propagation latency, or read-after-write consistency; the separate get- and list-customer sources own their response fields and filters.

The mutation automatically archives all contracts effective as of the current date and voids all corresponding invoices. The archive page identifies no affected contract or invoice IDs, invoice-state partition, ordering, or atomicity. The separate [[source-metronome-api-reference-contracts-archive-a-contract|contract-archive authority]] documents a different mutation with its own finalized-invoice flag and state-specific effects; those controls must not be imported into customer archival. The separate [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos|invoice-correction authority]] says a Metronome void does not itself void a downstream invoice. Accordingly, the customer-archive wording does not prove Stripe, ERP, marketplace, payment, refund, tax, accounting, revenue, settlement, webhook, or reconciliation completion.

## Ingest aliases and notification boundary

The page says ingest aliases remain idempotent for archived customers and directs callers to remove an alias before archival if they need to reuse it. This is a customer-identity reservation, not request-result replay through `Idempotency-Key`. The archive page does not define the removal operation, alias normalization, archive-versus-removal races, whether all aliases are released atomically, or a post-archive release path.

The assigned archive authority is limited to the statement that associated notifications will no longer be triggered. The separate [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications|notification lifecycle authority]] distinguishes threshold, system, and offset notifications and documents asynchronous JSON webhook delivery, retry, and at-least-once behavior. The archive page does not say which notification families its suppression covers, when suppression takes effect relative to the archive response, or what happens to evaluation or delivery work already generated or in flight. It therefore does not establish webhook cancellation or delivery recall.

## Success, errors, idempotency, and recovery

HTTP `200` requires a top-level `data` property referencing the generic `Id` schema, which requires UUID `id`. The response example repeats the request UUID, but the schema does not label the returned value or include archival state, `archived_at`, affected contract or invoice identifiers, notification status, or an operation record. A successful response therefore does not expose completion details for each documented side effect.

The operation lists `400 Bad request` and `404` for a specified resource not found. Both use an error object requiring string `message`; no machine-readable error code or field-level validation detail is supplied. The page does not distinguish malformed or missing bodies, malformed UUIDs, inaccessible customers, active versus already archived state, or failures during contract, invoice, alias, or notification effects.

The separate [[source-metronome-api-reference-idempotency|API-wide idempotency authority]] applies `Idempotency-Key` to all POST endpoints: the same key with identical parameters returns the original result, changed parameters return HTTP `409 Conflict`, keys persist for at least 24 hours, and a cached result can be HTTP `500`. This archive endpoint does not repeat or narrow those guarantees and gives no archive-specific retry contract. A same-key replay returns the original result rather than proving a fresh archive execution or a current read of its side effects; archive-specific no-key, different-key, expired-key, repeated-call, concurrency, partial-failure, and reconciliation behavior remain undocumented.

## Authority separation and contradiction check

No direct contradiction was found when each authority remains source-scoped. The get-customer schema's optional nullable `archived_at` and the list endpoint's `only_archived` filter are consistent with this page's explicit API visibility statement, while those read sources still own the exact response and filtering contracts. The notification lifecycle guide owns notification taxonomy and asynchronous delivery; the idempotency source owns API-wide POST replay; and the contract-archive and invoice-correction sources own their distinct invoice-state and downstream boundaries. None of those sources turns customer archival into a documented unarchive path, webhook recall, downstream invoice cancellation, or fresh-state retry.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-alerts-and-notifications]], [[metronome-api-idempotency]]
- Customer and contract context: [[source-metronome-api-reference-customers-get-a-customer]], [[source-metronome-api-reference-customers-list-customers]], [[source-metronome-api-reference-contracts-archive-a-contract]]
- Invoice context: [[source-metronome-api-reference-invoices-void-an-invoice]], [[source-metronome-guides-invoices-invoice-optimization-issue-credit-memos]]
- Notification context: [[source-metronome-guides-customers-billing-set-up-notifications-create-and-manage-notifications]]
- API context: [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-status-codes]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/customers/archive-a-customer-2026-07-13|2026-07-13 snapshot - customer archival lifecycle, aliases, notifications, and OpenAPI contract]]

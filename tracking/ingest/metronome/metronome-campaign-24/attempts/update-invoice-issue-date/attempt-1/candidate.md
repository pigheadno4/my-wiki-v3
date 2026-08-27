---
title: "Metronome API Reference: Update Invoice Issue Date"
type: source
date_ingested: 2026-08-27
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/contracts/update-invoice-issue-date.md"
raw_files:
  - "metronome/api-reference/contracts/update-invoice-issue-date-2026-07-13.md"
tags: [metronome, contracts, invoices, issue-date, api]
---

## Overview

This OpenAPI page documents bearer-authenticated `POST /v1/contracts/updateInvoiceIssueDate`, which reschedules one invoice that remains in `DRAFT`. It changes that invoice's issue date without changing the contract terms or the recurring billing schedules that generate future invoices.

## Query-critical facts

- The target invoice must still be `DRAFT`, and its new issue date must not be later than the contract end date. The supplied date is an RFC 3339 timestamp.
- When a JSON payload is supplied, `UpdateInvoiceIssueDatePayload` requires UUID-formatted `invoice_id` and date-time `issue_date`. The enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is undocumented. The payload schema does not declare `additionalProperties`, so unknown-field behavior is also unspecified.
- The mutation changes only the identified invoice. It does not change future billing cycles, underlying contract terms, or recurring invoice schedules for associated charges or commits; Metronome instead directs callers to edit-contract or edit-commit operations when both the issue date and future billing schedule must change.
- HTTP `200` requires `data` referencing an `Id` object whose required `id` is UUID-formatted. The request and response examples use different UUIDs, and the page does not identify what resource the returned ID represents. The documented failures are generic HTTP `400` and `404` error objects requiring a string `message`; no condition-to-status mapping is provided.
- The separate [[source-metronome-api-reference-idempotency|API-wide POST idempotency authority]] applies `Idempotency-Key`: identical parameters with the same key replay the original result, changed parameters return `409`, keys persist for at least 24 hours, and a cached result can be HTTP `500`. This endpoint adds no issue-date-specific guarantee for no-key or expired-key retries, concurrent rescheduling, read-after-write visibility, cached-error recovery, or the state reached after an ambiguous failure.

## Material boundaries

This operation is not a contract- or commit-schedule edit: it reschedules one draft invoice and expressly leaves later cycles and contract terms unchanged. The page does not define whether an earlier versus later date has different finalization behavior, whether the change is reversible, how it interacts with grace periods or simultaneous invoice finalization, when reads and exports reflect the new date, or whether any downstream Stripe, marketplace, ERP, tax, delivery, collection, payment, or accounting record is updated.

## Raw-detail coverage map

Use the raw page for the exact production server and path, bearer security declaration, operation ID, complete request property descriptions and example, success envelope and UUID example, generic `400` and `404` error schemas, and the shared OpenAPI tag catalog. The raw page contains no endpoint-specific retry, concurrency, propagation, or recovery contract beyond those exposed detail categories.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-invoicing]], [[metronome-customers-and-contracts]], [[metronome-credits-and-commits]], [[metronome-api-idempotency]]
- Related source: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/update-invoice-issue-date-2026-07-13|2026-07-13 snapshot - draft-invoice issue-date mutation, schedule boundary, request and response schemas, and errors]]

---
title: "Metronome API Reference: Void a Credit Grant"
type: source
date_ingested: 2026-08-26
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credit-grants/void-a-credit-grant.md"
raw_files:
  - "metronome/api-reference/credit-grants/void-a-credit-grant-2026-07-13.md"
tags: [metronome, credit-grants, plans, contracts, invoicing, api]
---

## Overview

This OpenAPI page documents bearer-authenticated `POST /v1/credits/voidGrant`, which voids a credit grant. It is a deprecated Plans endpoint, and Metronome directs new clients to Contracts without identifying a replacement operation or migration mapping.

## Query-critical facts

- The request object requires UUID-formatted `id` when a JSON payload is supplied. The enclosing `requestBody` is not marked required, so omitted-body behavior is not documented.
- Optional `void_credit_purchase_invoice` voids the purchase invoice associated with the grant when true. The page does not define its omitted or false behavior, invoice eligibility, downstream propagation, payment or refund effects, tax or accounting treatment, or atomicity with the grant void.
- Optional `release_uniqueness_key` resets this grant's uniqueness key for reuse when true. This endpoint-specific capability qualifies the API-wide idempotency summary that describes release as available only for Alerts. The page does not define the omitted or false behavior, when reuse becomes visible, concurrent reuse, or rollback after partial failure.
- HTTP 200 requires `data.id`, a UUID, but the request and response examples use different UUIDs; the page does not identify whether the response ID is the voided grant ID or another resource. HTTP 400 uses an error object requiring only a string `message`.
- The API-wide [[source-metronome-api-reference-idempotency|POST idempotency authority]] applies `Idempotency-Key`: identical same-key parameters replay the original result, changed parameters return `409`, and retention is at least 24 hours. This endpoint adds no void-specific repeated-call, concurrency, cached-error recovery, state-visibility, or reconciliation guarantee.

## Material boundaries

The page does not state preconditions or eligible grant states, whether voiding restores consumed or remaining balance, how ledgers or invoices reflect the transition, whether the mutation is reversible, or when reads observe it. Its purchase-invoice option does not establish effects in Stripe, an ERP, a marketplace, or another downstream A/R system. The endpoint is legacy Plans authority, not a Contracts implementation guide.

## Raw-detail coverage map

Use the raw page for the exact OpenAPI server and path, bearer security declaration, request property types and descriptions, request and response UUID examples, success and generic error schemas, operation ID, and the full shared tag descriptions. The raw schema does not declare `additionalProperties`, so unknown-field behavior is unspecified.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-credits-and-commits]], [[metronome-invoicing]], [[metronome-api-idempotency]], [[metronome-customers-and-contracts]]
- Related source: [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/credit-grants/void-a-credit-grant-2026-07-13|2026-07-13 snapshot - deprecated Plans credit-grant void mutation, invoice and uniqueness-key options, and OpenAPI responses]]

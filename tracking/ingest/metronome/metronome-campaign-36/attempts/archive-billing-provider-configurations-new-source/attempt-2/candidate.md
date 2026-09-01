---
title: "Metronome API Reference: Archive Billing Provider Configurations for a Customer"
type: source
date_ingested: 2026-09-01
canonical_url: "https://docs.metronome.com/api-reference/customers/archive-billing-provider-configurations-for-a-customer"
original_format: webpage
raw_files:
  - "metronome/api-reference/customers/archive-billing-provider-configurations-for-a-customer-2026-07-13.md"
tags: [metronome, api, customers, contracts, billing-providers, invoicing, idempotency]
---

## Overview

Bearer-authenticated `POST /v1/archiveCustomerBillingProviderConfigurations` archives one or more billing-provider configurations belonging to one customer. The archive takes effect immediately; when an active contract uses a targeted configuration, Metronome says it archives that configuration on the contract, immediately stops metering to downstream systems, suppresses a grace-period invoice from customer delivery, and disables associated spend- and credit-based threshold recharge configurations.

## Query-critical facts

- Within a supplied JSON payload, `customer_id` and `customer_billing_provider_configuration_ids` are required, and the targeted configuration IDs are configurations belonging to that supplied single customer. The customer and every configuration ID are UUID-formatted, but the configuration-ID array has no `minItems` or `uniqueItems` constraint and the example repeats one ID. The enclosing OpenAPI `requestBody` is not marked `required: true`, and the payload has no `additionalProperties: false`; omitted-body, empty-array, duplicate-ID, and unknown-field runtime behavior are not established.
- Archival is immediate. If an active contract uses a targeted configuration, the page says Metronome archives the configuration on that contract and immediately stops metering to downstream systems. It does not define whether "metering" means provider reporting, invoice delivery, Metronome rating, usage acceptance, or some combination, nor does it identify affected contracts or downstream systems in the response.
- Archiving during an invoice grace period means the invoice is not sent to the customer. This is a delivery consequence, not evidence that the invoice is voided, deleted, finalized, recalculated, refunded, or canceled downstream; the endpoint does not define treatment of earlier finalized or already-sent invoices.
- The operation automatically disables both spend-based and credit-based threshold recharge configurations on contracts using the archived provider. It does not establish the state of an already initiated charge, payment-gate workflow, pending commit, payment, invoice, balance, ledger entry, webhook, or downstream provider object, or define how a disabled configuration can be safely restored or replaced.
- Multiple configurations belonging to the supplied single customer can be submitted together, and any validation failure for one prevents the entire operation from succeeding. The page does not map a foreign-customer configuration ID to a response or define validation order, concurrency ordering, atomicity, rollback after execution begins, or recovery from partial or ambiguous effects.
- The page says archival can free uniqueness keys for reuse with new billing-provider configurations. It does not identify the key, its scope, release timing, or reuse conflict behavior; this resource-lifecycle statement must not be conflated with the API-wide `Idempotency-Key` request-result cache.

## Material boundaries and contradictions

> [!warning] Success response documentation conflicts
> The narrative says a successful response contains `success` and `error`, but the OpenAPI HTTP `200` schema instead requires top-level `data` referencing `CustomerBillingProviderArchivePayload`, which requires the customer UUID and configuration-ID array. The page does not reconcile these shapes, and neither representation exposes an affected-contract list, archive timestamp, disabled-threshold list, downstream status, or reconciliation result.

The dedicated [[source-metronome-guides-implement-metronome-core-concepts-provision-customer|customer-provisioning guide]] separately says direct archival makes a configuration reusable on another customer, immediately removes it from an active contract, stops billing to the destination, and prevents provisioning a replacement configuration on that contract. Preserve that guide-scoped beta boundary separately: this endpoint itself promises only uniqueness-key reuse and does not define configuration-ID reassignment, replacement, restoration, retention, read-after-write visibility, or a recovery workflow. The scheduled provider-change guide is also a distinct controlled transition; it does not make this immediate archive operation a schedule edit or guarantee continuity to another destination.

The operation lists generic HTTP `400` and `500` error bodies with required string `message`, but it does not map a foreign-customer configuration ID or other invalid customer/configuration identity, already-archived state, active-contract conflicts, authentication, authorization, rate limits, downstream failure, or partial effects to specific outcomes. A successful response proves only the documented Metronome archive result, not provider cancellation, invoice delivery or cancellation, payment, refund, tax, settlement, accounting, webhook completion, or reconciliation.

The separate API-wide [[source-metronome-api-reference-idempotency|`Idempotency-Key` authority]] applies to this POST. Metronome persists a provided-key result only after execution begins, meaning validation passed and no pre-execution concurrent-request conflict prevented execution. Identical same-key parameters then replay that original result, changed parameters return HTTP `409`, retention is at least 24 hours, and an admitted HTTP `500` can be persisted; the same key then replays that cached error. The idempotency authority directs callers to investigate resulting system state and decide whether to resolve manually or retry rather than assume a changed key is safe. The separate [[source-metronome-api-reference-status-codes|status-code authority]] instead advises checking whether a resource was partially created after `5XX` and then retrying with a different key. Neither authority defines one universally safe recovery sequence for immediate provider-configuration archival, contract detachment, grace-period invoice suppression, threshold disablement, or downstream convergence. Validation failures and pre-execution concurrent-request conflicts are not established cached results. The endpoint adds no no-key, another-key, expired-key, repeated-archive, concurrent archive or provider-change, read-after-write, rollback, final recovery, or fresh-state verification contract; a same-key replay is not fresh proof of current contract, invoice, threshold, metering, provider, or reconciliation state.

## Raw-detail coverage map

| Detail category | Exact evidence route |
| --- | --- |
| Production server, bearer security, POST path, operation ID, immediate archive purpose, active-contract effect, and downstream-metering wording | [[raw/metronome/api-reference/customers/archive-billing-provider-configurations-for-a-customer-2026-07-13|complete archive-operation raw]] |
| Supplied-payload required properties, same-customer ownership precondition, UUID formats, configuration-ID array, repeated-ID example, absent request-body required marker, foreign-customer failure unknown, and unspecified closed-object behavior | [[raw/metronome/api-reference/customers/archive-billing-provider-configurations-for-a-customer-2026-07-13|complete archive-operation raw]] |
| Grace-period invoice suppression, spend- and credit-based threshold disablement, multi-configuration validation boundary, and uniqueness-key reuse wording | [[raw/metronome/api-reference/customers/archive-billing-provider-configurations-for-a-customer-2026-07-13|complete archive-operation raw]] |
| Narrative `success`/`error` fields versus required OpenAPI `data` payload, plus generic HTTP `400`/`500` error schema | [[raw/metronome/api-reference/customers/archive-billing-provider-configurations-for-a-customer-2026-07-13|complete archive-operation raw]] |

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-customers-and-contracts]], [[metronome-integrations]], [[metronome-invoicing]], [[metronome-credits-and-commits]], [[metronome-spend-threshold-billing]], [[metronome-api-idempotency]]
- Configuration and transition authorities: [[source-metronome-api-reference-customers-set-billing-provider-configurations-for-a-customer]], [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]], [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]]
- Invoice and retry authorities: [[source-metronome-guides-implement-metronome-core-concepts-how-invoicing-works]], [[source-metronome-api-reference-idempotency]], [[source-metronome-api-reference-status-codes]]

## Raw Sources

- [[raw/metronome/api-reference/customers/archive-billing-provider-configurations-for-a-customer-2026-07-13|2026-07-13 snapshot - immediate provider-configuration archival, active-contract effects, threshold disablement, request and response schemas, and error boundaries]]

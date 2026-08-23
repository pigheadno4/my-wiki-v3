---
title: "Create a credit"
type: source
date_ingested: 2026-08-23
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/create-a-credit.md"
raw_files:
  - "metronome/api-reference/credits-and-commits/create-a-credit-2026-07-13.md"
tags: [metronome, credits-and-commits, customer-credits, api]
---

## Overview

This API reference documents Metronome's bearer-authenticated `POST /v1/contracts/customerCredits/create` endpoint on `https://api.metronome.com`. It creates a customer-level credit that can span all of a customer's contracts or be limited to selected contracts, although the page recommends adding credits directly through contract create or edit APIs in most cases. This is a future-balance creation operation; the page does not establish historical invoice reversal, a credit memo, refund behavior, or an external accounts-receivable adjustment.

## Key takeaways

- The `requestBody` wrapper is not marked `required: true`, while the referenced payload requires `customer_id`, `priority`, `product_id`, and `access_schedule`. The document therefore defines required properties when a payload is supplied but does not define omitted-body runtime behavior.
- `access_schedule.schedule_items` is required, and every item requires numeric `amount`, inclusive RFC 3339 `starting_at`, and exclusive RFC 3339 `ending_before`. `credit_type_id` defaults to USD cents when omitted.
- Contract scope can be limited with `applicable_contract_ids`; the prose says an empty value is cross-contract, while the schema says omission applies to all contracts. Product eligibility can use IDs, tags, or `specifiers`, but `specifiers` cannot be combined with either direct selector.
- Lower numeric priority is consumed first, and the page says contract-level commits and credits win equal-priority ties over customer-level ones. The broader prioritization guide adds balance-type, rollover, applicability, cost-basis, and schedule tie-breakers, so this endpoint summary is not a complete global ordering algorithm.
- HTTP `200` requires `data.id`, a UUID. The operation lists generic `400` and `404` errors requiring a string `message`; the `uniqueness_key` schema separately says duplicate credit or commit creation fails with `409`, which the operation response map omits.
- The top-level payload, schedule-item, specifier, and exclusion objects do not declare `additionalProperties`; unknown-field behavior is therefore unspecified. Only the pricing-group map, presentation-group map, and `custom_fields` map explicitly allow arbitrary keys with string values.

## Request-body requiredness and core fields

The OpenAPI document applies HTTP bearer authentication globally. The operation's `requestBody` contains an `application/json` schema reference but no `required: true`. Within `CreateCustomerCreditPayload`, `customer_id`, `priority`, `product_id`, and `access_schedule` are required. `customer_id` and `product_id` are UUID-formatted strings, while `priority` is a number.

This required-property list must not be presented as proof that a completely omitted body is rejected: the wrapper does not declare that requirement. The payload schema also does not set `additionalProperties`, so it does not say whether unknown top-level fields are accepted, ignored, or rejected. It does not define null handling, numeric bounds for priority, authorization scope beyond bearer authentication, or field-level failure mappings.

## Access amount and timing

`access_schedule` distributes credit to the customer. Its object requires `schedule_items`; each item requires numeric `amount`, an inclusive RFC 3339 `starting_at`, and an exclusive RFC 3339 `ending_before`. The optional UUID-formatted `credit_type_id` defaults to USD cents.

The schema provides no `minItems`, so it does not establish that `schedule_items` must be nonempty. It also gives no positivity, zero, integer, precision, maximum, or rounding rule for `amount`; no ordering, overlap, adjacency, gap, or start-before-end validation; and no time-zone rule beyond RFC 3339 formatting and the inclusive/exclusive endpoint descriptions. The prose says the schedule defines when and how much credit becomes available, usually aligned to a contract or beginning immediately and expiring later, but it does not define ledger-entry creation time, balance-read visibility, eventual consistency, editability, cancellation, expiry processing, or concurrency with usage and invoicing.

## Contract scope, product eligibility, and usage filters

`applicable_contract_ids` limits the credit to selected contracts. The prose says leaving it empty permits use across all customer contracts, while the schema says the same for omission; its array items are strings without a UUID format annotation. The page does not define an invalid, archived, duplicate, foreign-customer, or later-created contract's behavior.

The required `product_id` identifies the credit's product even when eligible usage is unrestricted. Separate `applicable_product_ids` and `applicable_product_tags` narrow drawdown; when both are absent, the credit applies to all products. The page does not state whether those two direct selector fields may be combined with each other or how empty arrays differ from omission.

Alternatively, `specifiers` filter eligible usage. Usage must satisfy at least one specifier. A specifier can select one product UUID, require all listed product tags, and match arbitrary string-valued pricing-group or presentation-group maps. `specifiers` cannot be combined with either direct product selector. The feature-gated `exclude` array removes usage matching its inclusion criteria and all listed exclusion tags. No field inside a specifier or exclusion object is marked required, and the page does not define empty-specifier behavior, selector evaluation against missing dimensions, case sensitivity, duplicate entries, atomic validation, or unknown fields on these enclosing objects.

## Priority and ordering boundary

The endpoint page states that lower numeric priority is consumed first when several credits apply and that equal-priority contract-level commits and credits precede customer-level ones. This is consistent with the existing wiki when treated as this endpoint's concise ordering summary, but it is incomplete rather than globally exhaustive. The dedicated prioritization source separately places rollover and balance type ahead of some priority comparisons and adds cost basis, product and usage specificity, schedule times, and applicable-contract count as further tie-breakers. The endpoint does not define concurrent drawdown ordering, transaction isolation, ledger atomicity, or whether a priority change can affect already-rated or finalized usage.

## Optional presentation and integration fields

Optional `name` is a nonempty string described as displayed on invoices. Optional `description` is for the UI and API and is explicitly not exposed to end customers. The endpoint does not define invoice states, line-item placement, finalized-invoice effects, downstream-provider propagation, or whether the description appears in exports or webhooks.

`custom_fields` is labeled for the `contract_credit` entity and references an object whose arbitrary values must be strings. This endpoint does not define allowed keys, configured-key validation, uniqueness, limits, overwrite behavior, persistence, deletion, or propagation; those broader custom-field behaviors remain owned by the dedicated custom-fields authority. NetSuite sales-order and Salesforce opportunity IDs are strings whose availability depends on client configuration. `rate_type` accepts uppercase and lowercase `COMMIT_RATE` and `LIST_RATE`, but the page gives no semantics or precedence for those values.

## Success, errors, and idempotency boundaries

A documented `200 Success` returns JSON with required top-level `data`; `data` requires UUID `id`. The page does not say whether that ID identifies a fully usable balance, expose any created-resource state, or provide a retrieval link.

The operation lists `400 Bad request` and generic `404 Not found`; both use an error object requiring only string `message`. It gives no endpoint-specific error codes, examples, or mappings and does not list `401`, `403`, `409`, `429`, or `5xx`. Separately, `uniqueness_key` is a 1-128 character string whose reuse after creating a credit or commit prevents a new record and fails with `409`. The page does not define key scope, retention, release, normalization, races, or whether a failed attempt consumes the key.

The separate API-wide [[source-metronome-api-reference-idempotency|idempotency authority]] applies `Idempotency-Key` to all POST endpoints: identical parameters with the same key replay the original result, changed parameters return `409`, retention is at least 24 hours, and a cached result can be `500`. Those guarantees are API-wide rather than stated by this endpoint page. Neither source defines how the header interacts with `uniqueness_key`, no-key or different-key duplicate behavior, expired-key retries, concurrent credit creation, endpoint-specific recovery after a cached error, or how to reconcile a response lost after creation. The general [[source-metronome-api-reference-status-codes|status-code guidance]] must likewise not be mistaken for endpoint-specific error coverage.

## Lifecycle and propagation unknowns

This endpoint creates a customer-level spending allowance or free balance and returns an ID. It does not define update, archive, delete, reversal, or transition operations; the created ledger's initial state; visibility in balance APIs; notification or webhook emission; propagation timing to draft or finalized invoices, reports, exports, alerts, contracts, or account hierarchies; effects on external A/R, Stripe, tax, payment, refund, or revenue-recognition systems; partial failure; or transaction boundaries. The recommendation that contract-level credits are easier for finance teams is operational guidance, not an accounting, revenue-recognition, or reconciliation guarantee.

No direct contradiction was found with the existing Metronome concepts or source pages. The endpoint fills the customer-credit creation gap beside the existing customer-commit source, while its abbreviated priority wording and finance recommendation require the qualifications above.

## Related

- Company: [[metronome]]
- Concepts: [[metronome-credits-and-commits]], [[metronome-api-idempotency]], [[metronome-products-and-rate-cards]], [[metronome-currencies-and-custom-pricing-units]], [[metronome-custom-fields]], [[metronome-invoicing]]
- Related sources: [[source-metronome-api-reference-credits-and-commits-create-a-commit]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-prioritization-rules]], [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-custom-fields]], [[source-metronome-api-reference-idempotency]], [[source-metronome-api-reference-status-codes]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/create-a-credit-2026-07-13|2026-07-13 snapshot - customer-level credit creation, schedule, applicability, priority, response, and error schema]]

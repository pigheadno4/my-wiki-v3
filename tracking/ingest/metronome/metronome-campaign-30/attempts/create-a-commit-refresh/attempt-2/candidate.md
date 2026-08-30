---
title: "Create a commit"
type: source
date_ingested: 2026-08-30
canonical_url: "https://docs.metronome.com/api-reference/credits-and-commits/create-a-commit"
original_format: webpage
raw_files:
  - "metronome/api-reference/credits-and-commits/create-a-commit-2026-08-28.md"
  - "metronome/api-reference/credits-and-commits/create-a-commit-2026-07-13.md"
tags: [metronome, credits-and-commits, customer-commits, api]
---

## Overview

This API reference documents bearer-authenticated `POST /v1/contracts/customerCommits/create`, which creates a customer-level prepaid or postpaid spending commitment that can span all of a customer's contracts or be limited to selected contracts. Metronome says to use contract create or edit for most standard commitments and reserves this endpoint for cross-contract or enterprise-wide use.

## Query-critical facts

- The enclosing OpenAPI `requestBody` is not marked required. Within a supplied `CreateCustomerCommitPayload`, `customer_id`, `type`, `priority`, `product_id`, and `access_schedule` are required; omitted-body runtime behavior remains undocumented. The payload and its schedule, specifier, and exclusion objects do not declare `additionalProperties: false`, so unknown-field behavior is also undocumented; only the pricing-group, presentation-group, and `custom_fields` maps explicitly permit arbitrary string-valued properties.
- `type` accepts upper- or lowercase prepaid and postpaid values. For postpaid commits, the narrative and field descriptions require `invoice_schedule`, require matching access- and invoice-schedule totals, allow only one item in each schedule, and require `invoice_contract_id` unless `do_not_invoice` is true. For prepaid commits, omitting `invoice_schedule` creates a complimentary commit without an invoice; an invoiced prepaid commit requires `invoice_contract_id` unless `do_not_invoice` is true. These are conditional prose/schema-description rules: neither `invoice_schedule` nor `invoice_contract_id` appears in the payload's OpenAPI `required` array.
- At immediate parent `ScheduleDurationInput`, `schedule_items` is required. Each access item requires numeric `amount`, inclusive RFC 3339 `starting_at`, and exclusive RFC 3339 `ending_before`. Optional, feature-gated `access_type` makes `SPEND` deduct the dollar cost of usage and `QUANTITY` deduct the number of units used, defaulting to `SPEND` when omitted; the property is also marked `x-stainless-skip: true`. Optional `credit_type_id` independently defaults to USD cents. The page does not define generated-client exposure, non-USD or custom-unit compatibility, quantity denomination, conversion, precision, rounding, or mixed-mode priority.
- At immediate parent `SchedulePointInTimeInput`, the description requires either `schedule_items` or `recurring_schedule`, although the object itself has no OpenAPI required list. Within supplied `schedule_items`, each item's OpenAPI required array lists only `timestamp`, while the array and field descriptions require either numeric `amount` or both `unit_price` and `quantity`; their product determines amount, while sending `amount` makes unit price equal amount and quantity equal 1. The recurring object requires `starting_at`, `ending_before`, `frequency`, and `amount_distribution` and its descriptions require the same amount-or-pair financial form. Its optional `credit_type_id` defaults to USD cents. The page gives no precision, rounding, sign, bounds, tax, collection, or reconciliation contract.
- UUID `product_id` identifies the fixed product used to invoice the commit amount even when eligible usage is unrestricted. Eligible usage can use product IDs, product tags, or `specifiers`; if none is provided, the descriptions say the commit applies to all products, and `specifiers` cannot be combined with either direct selector. `applicable_contract_ids` limits contract scope; omission applies the commit to all contracts, while the narrative calls an empty value cross-contract. Empty-array versus omission behavior is unresolved.
- Lower numeric priority is consumed first. At equal priority, contract-level commits and credits precede customer-level ones. This endpoint-local rule is not the complete rollover, balance-type, applicability, cost-basis, or schedule ordering algorithm documented elsewhere.
- HTTP `200` requires `data.id`; the operation also lists generic `400` and `404` error objects. Optional 1-128 character `uniqueness_key` prevents another credit or commit from being created with a previously used key and documents HTTP `409`, which is absent from the operation response map.

## Identity, lifecycle, financial, and retry boundaries

The endpoint's `uniqueness_key` is a resource-creation identity guard, not request-result replay. The separate API-wide [[source-metronome-api-reference-idempotency|idempotency authority]] applies `Idempotency-Key` to all POST endpoints: identical same-key parameters replay the original result, changed parameters return `409`, retention is at least 24 hours, and a cached result can be `500`. Neither authority defines interaction or precedence between the keys, customer-commit uniqueness-key scope or release, failed-attempt consumption, concurrent creation, another or expired header key, or recovery after an ambiguous or cached failure.

For postpaid commits, the narrative places customer payment when the commitment expires, at the end of `access_schedule`; the `invoice_schedule` description separately says the true-up invoice is generated at its scheduled time. The page documents no constraint aligning those times. These are source-scoped lifecycle statements, not proof of collection, settlement, downstream-provider success, or any state after invoice generation.

The create response exposes a UUID ID but no initial balance or ledger representation, read-after-write visibility, archive or edit transition, expiry processing, notification or webhook behavior, invoice-finalization propagation, downstream billing-provider result, tax, collection, settlement, refund, external accounts-receivable, revenue-recognition, partial-failure, or transaction-boundary guarantee. `SPEND` and `QUANTITY` define drawdown bases, while the access and invoice schedules separately retain their exact `amount`, `unit_price`, `quantity`, and optional `credit_type_id` fields; do not relabel all numeric values as dollars, cents, cost, quantity, or remaining balance.

> [!warning] Documentation ambiguities
> The narrative says an empty `applicable_contract_ids` value is cross-contract, while the schema says omission applies to all contracts; it does not define whether an empty array and omission are equivalent. For postpaid commits, the narrative places customer payment at commitment expiry, the end of `access_schedule`, while `invoice_schedule` says the true-up invoice is generated at its scheduled time; no alignment constraint is documented. The reusable invoice-schedule schema also exposes `recurring_schedule`, while postpaid-specific prose permits only one item in each schedule, so recurring invoice-schedule support for postpaid commits remains unresolved. The prose names lowercase commit types while the schema accepts both cases, and the uniqueness-key description documents `409` even though the response map omits it.

## Raw-detail coverage map

| Raw detail category | Exact raw coverage |
| --- | --- |
| Purpose and scope | Cross-contract and enterprise-wide use, preferred contract create/edit alternative, prepaid versus postpaid purpose, contract scope, product targeting, and priority guidance |
| Request and result | Production server, bearer scheme, POST path, operation ID, request-body wrapper and example, required payload list, HTTP `200` ID envelope, generic `400`/`404`, and duplicate `409` wording |
| Access schedule | Complete spend-or-quantity mode, credit-type default, amount and inclusive/exclusive timestamps, nested required list, field annotations, and exact enum aliases |
| Invoice schedule | Postpaid payment at access-schedule expiry versus true-up invoice generation at the invoice schedule's time with no documented alignment constraint; point-in-time and recurring forms; parent, item, and recurring conditional requiredness; amount versus unit-price-and-quantity rules; frequency and distribution enums; and `do_not_invoice` default and scope |
| Applicability and optional fields | Contract and product selectors, specifiers and exclusions, arbitrary string-valued maps, custom fields, rate type, display metadata, and configuration-dependent NetSuite and Salesforce IDs |

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-credits-and-commits]], [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-api-idempotency]]
- Supporting concepts: [[metronome-products-and-rate-cards]], [[metronome-currencies-and-custom-pricing-units]]
- Related sources: [[source-metronome-api-reference-contracts-create-a-contract]], [[source-metronome-api-reference-contracts-edit-a-contract]], [[source-metronome-api-reference-credits-and-commits-edit-a-commit]], [[source-metronome-api-reference-credits-and-commits-create-a-credit]], [[source-metronome-guides-pricing-packaging-apply-credits-and-commits-prioritization-rules]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/credits-and-commits/create-a-commit-2026-08-28|2026-08-28 snapshot - cross-contract commit creation, spend-or-quantity access, conditional invoicing, schedules, applicability, identity, response, and errors]]
- [[raw/metronome/api-reference/credits-and-commits/create-a-commit-2026-07-13|2026-07-13 snapshot - prior customer-level commit creation, schedules, applicability, priority, response, and errors]]

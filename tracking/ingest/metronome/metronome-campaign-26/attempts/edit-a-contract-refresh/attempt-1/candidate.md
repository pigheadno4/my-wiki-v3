---
title: "Metronome API Reference: Edit a Contract"
type: source
date_ingested: 2026-08-28
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/contracts/edit-a-contract"
raw_files:
  - "metronome/api-reference/contracts/edit-a-contract-2026-08-28.md"
  - "metronome/api-reference/contracts/edit-a-contract-2026-07-13.md"
tags: [metronome, contracts, contract-editing, api, invoicing]
---

## Overview

This OpenAPI page documents bearer-authenticated `POST /v2/contracts/edit`, a feature-enabled mutation for changing an existing contract's commercial terms and lifecycle configuration without replacing the contract. The endpoint can add, update, archive, or remove many contract components and returns an edit-related result, while leaving important atomicity and recovery behavior undefined.

## Query-critical facts

- When a JSON payload is supplied, `EditContractPayload` requires UUID-formatted `customer_id` and `contract_id`. The enclosing OpenAPI `requestBody` is not marked required, so omitted-body behavior is undocumented. The payload schema does not declare `additionalProperties`, so top-level unknown-field behavior is also unspecified.
- The mutation surface includes commits and credits, recurring grants, discounts, overrides, scheduled charges, subscriptions, spend and prepaid-balance thresholds, spend trackers, contract name and end date, payment terms, and billing- or revenue-system configuration. Arrays and nested objects represent distinct add, update, archive, and remove actions; the page does not establish atomicity across a mixed edit, validation order, partial-success behavior, or concurrent-edit ordering.
- Draft invoices update immediately to reflect a contract edit. Finalized invoices remain unchanged unless they are voided and regenerated in the UI or API; the page does not extend that statement to downstream billing providers, payment, refunds, tax, revenue systems, or accounting reconciliation. Contract editing must be enabled for the endpoint.
- `update_contract_end_date` sets an exclusive RFC 3339 end timestamp and is nullable. The separate `allow_contract_ending_before_finalized_invoice` control defaults to `true`: it permits an end date earlier than the `end_timestamp` of existing finalized invoices, leaves those invoices unchanged, and requires voiding and regenerating finalized usage invoices to incorporate the new end date. The page does not define how a mixed edit is rolled back if another component fails.
- Updates to recurring commits and recurring credits affect only generated grants whose access schedules have not started. Expired grants and grants with active access schedules remain unchanged, but the endpoint does not define mixed eligible/ineligible-array behavior, error reporting, or the visibility timing of generated-child changes.
- Added commit and credit access schedules can use the feature-gated `access_type` to draw down either priced spend (`SPEND`) or usage units (`QUANTITY`); omission defaults to `SPEND`. The page does not define migration of an existing balance between modes, unit compatibility, mixed-mode priority, or invoice and ledger representation.
- Subscription creation within an edit now exposes feature-gated Stripe `payment_gate_config`. A linked recurring commit or credit can use `access_policy` to release each child balance after payment for its billing period or release all child balances after the first payment. The schema does not define payment-state authority, failure and retry behavior, pending-balance visibility, revocation, concurrency, or reconciliation with Stripe.
- For either the spend-threshold or prepaid-balance-threshold update, changing `is_enabled` from `false` to `true` causes immediate evaluation regardless of prior state. Usage reaching the spend threshold, or balance falling to the prepaid threshold, initiates a threshold charge. The page does not say that charge initiation guarantees payment or commit availability, nor define atomicity with other edits, evaluation ordering, downstream invoice/provider effects, concurrency, or ambiguous-failure recovery.
- HTTP `200` requires `data.id`; `data.edit` is optional in the schema. The narrative instead promises the edit ID and complete edit details, while the success example reuses the request's `contract_id` as `data.id`. The page does not reconcile whether the required ID identifies the edit or contract, nor whether complete edit details are guaranteed in every success.
- This endpoint snapshot exposes optional `uniqueness_key` with a 1-128 character schema and wording that reuse prevents a duplicate record and fails with HTTP `409`, although the operation response map omits `409`. The earlier 2026-07-13 [[source-metronome-api-reference-idempotency|API-wide idempotency authority]] labels contract-edit uniqueness-key support as coming soon, so the newer schema exposure does not by itself resolve runtime enablement. This unresolved authority conflict is distinct from API-wide POST `Idempotency-Key` result replay. Neither page defines the two keys' interaction, uniqueness-key scope or release, no-key or expired-key retries, concurrent ordering, or recovery after cached or ambiguous failures.

## Material boundaries and contradictions

The request schema says `add_billing_provider_configuration_update` and the feature-gated revenue-system equivalent currently support only adding a configuration to a contract that does not already have one. That is an API-page limitation, not proof of external-provider readiness, invoice delivery, revenue posting, or reconciliation.

> [!warning] Billing-provider edit scope conflict
> This endpoint schema limits the billing-provider field to adding a configuration when the contract has none, while [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]] documents provider-to-provider changes on existing contracts through the same edit surface. The sources do not establish whether the API description is stale, configuration-dependent, or narrower than the guide; verify current account enablement and runtime behavior before implementing a provider transition.

The page also does not define authorization errors, rollback, cross-component validation and atomicity, edit-history propagation timing, webhook behavior, or recovery after a timeout or cached error. Its schema is not a legal, accounting, tax, or external-system authority.

## Raw-detail coverage map

Use the raw page for the exact production server, bearer security declaration, operation ID, request example, complete add/update/archive/remove payload families, conditional required properties, null and omission semantics that are explicitly documented, schedule timestamps and effective-time enums, feature-gated fields, limits, nested pricing, subscription payment-gate and recurring-balance access-policy schemas, spend-versus-quantity access schedules, threshold-commit duration and rollover controls, complete `ContractEdit` response schema, success example, and `400` error enum. The raw page also exposes response/request naming asymmetries, enum casing variants, and every nested subscription, credit, commit, override, threshold, spend-tracker, provider, and revenue-system schema; those ordinary details are intentionally routed to raw rather than reconstructed here.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-customers-and-contracts]], [[metronome-invoicing]], [[metronome-credits-and-commits]], [[metronome-spend-threshold-billing]], [[metronome-api-idempotency]], [[metronome-integrations]], [[metronome-subscriptions]]
- Related sources: [[source-metronome-guides-pricing-packaging-make-pricing-changes-edit-contract]], [[source-metronome-guides-customers-billing-manage-customers-schedule-billing-provider-change]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/contracts/edit-a-contract-2026-08-28|2026-08-28 snapshot - refreshed contract-edit mutation, payment-gated subscription access policy, spend-versus-quantity balances, required identifiers, mutable term families, invoice and recurring-grant lifecycle effects, threshold charge initiation, duplicate prevention, provider limits, response schema, and errors]]
- [[raw/metronome/api-reference/contracts/edit-a-contract-2026-07-13|2026-07-13 snapshot - prior contract-edit mutation, required identifiers, mutable term families, invoice and recurring-grant lifecycle effects, threshold charge initiation, duplicate prevention, provider limits, response schema, and errors]]

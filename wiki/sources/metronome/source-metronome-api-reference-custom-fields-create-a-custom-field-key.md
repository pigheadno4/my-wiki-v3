---
title: "Metronome API Reference: Create a Custom Field Key"
type: source
date_ingested: 2026-08-30
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/custom-fields/create-a-custom-field-key"
raw_files:
  - "metronome/api-reference/custom-fields/create-a-custom-field-key-2026-07-13.md"
tags: [metronome, api, custom-fields, metadata, idempotency, invoicing]
---

## Overview

Bearer-authenticated `POST /v1/customFields/addKey` creates an allowed custom-field key for a selected `ManagedEntity` request value. The operation defines a key and whether later values must be unique; setting an object-specific value is a separate operation. The page also identifies alert-scoping and invoice-metadata uses, but successful key creation is not evidence that any value has been set, evaluated, or propagated.

## Query-critical facts

- Within a supplied JSON payload, `entity`, `key`, and boolean `enforce_uniqueness` are required. The enclosing OpenAPI `requestBody` is not marked `required: true`, and the payload object does not declare `additionalProperties: false`; omitted-body and unknown-field runtime behavior are therefore not established. The page gives no key syntax, length, normalization, case-sensitivity, namespace, or reserved-name rules.
- `entity` references a 19-value `ManagedEntity` request enum: `alert`, `billable_metric`, `charge`, `commit`, `contract_credit`, `contract_product`, `contract`, `customer`, `discount`, `invoice`, `professional_service`, `product`, `rate_card`, `scheduled_charge`, `subscription`, `package_commit`, `package_credit`, `package_subscription`, and `package_scheduled_charge`. This schema surface does not reconcile the page's broad summary language with its Customer-specific use bullet or the separate custom-fields overview, which says custom fields apply to most entities but lists only customer, product, contract, commit, credit, scheduled charge, rate card, and alert. The sources leave product versus `contract_product`, credit versus `contract_credit`, package variants, invoice, discount, charge, subscription, billable-metric, professional-service, and other label or coverage relationships unexplained; the enum must not be generalized into a reconciled platform-wide support catalog.
- `enforce_uniqueness` configures a constraint on values later assigned under the key: if uniqueness is enabled, an attempt to set a value that already exists fails. This endpoint page does not define the comparison or entity scope, treatment of null or empty values, normalization, archived-object behavior, when the constraint becomes active, whether the conflicting value belongs to the same or another object or `ManagedEntity` type, or an error status or body for that later failure. The separate custom-fields overview independently says uniqueness limits reuse across multiple objects and remains enforced for archived objects; that broader overview-level guidance does not resolve this endpoint's comparison boundary or prove cross-`ManagedEntity` enforcement.
- Custom-field values on commits, credits, and contracts can scope alert evaluation. Product custom fields can set Stripe-integration invoice metadata, and values for customers, contracts, invoices, products, commits, scheduled charges, and subscriptions are described as passed down to the invoice. The page does not define destination field paths, precedence, timing, draft-versus-finalized behavior, retroactivity, update or deletion propagation, export visibility, downstream acceptance, or reconciliation; creating the key alone does not trigger these outcomes.
- The operation lists HTTP `200` with description `Success` but provides no response content schema or example. It gives no create-key failure catalog, duplicate-key behavior, authorization or validation mapping, atomicity, read-after-create visibility, concurrent-create ordering, update or deletion lifecycle, or recovery after an ambiguous result.
- Separately, the API-wide [[source-metronome-api-reference-idempotency|POST idempotency authority]] supports `Idempotency-Key` on all POST endpoints: after a request begins execution, an identical same-key retry returns the persisted original result, changed parameters return HTTP `409`, keys are retained for at least 24 hours, and a cached result can be HTTP `500`. The create-key page adds no endpoint-specific rule for another or expired key, concurrent calls, cached-error state, or reconciliation. Its `enforce_uniqueness` flag is a future value constraint, not an idempotency key or create-request replay mechanism.

## Material boundaries and tensions

- Preserve three unreconciled entity-applicability surfaces: the endpoint's broad summary, its Customer-specific use bullet, and its 19-value request enum. The separate overview adds a fourth, narrower prose surface by saying most entities while naming eight. None proves that another surface is merely illustrative, that prose labels and enum labels are equivalent, or that the enum is a platform-wide support catalog.
- The documented uniqueness failure occurs when a later value is set, not necessarily when the key is created. The page does not establish whether creating a duplicate key succeeds, conflicts, or changes an existing definition, nor whether `enforce_uniqueness` can later be changed. Preserve the overview's cross-object and archived-object guidance as overview-scoped authority without importing it as a definition of this endpoint's comparison scope or inferring behavior across `ManagedEntity` types.
- Alert scoping and invoice propagation describe uses of set custom-field values. An HTTP `200` with description `Success` from `addKey`, for which the page provides no response content schema or example, proves neither that a value exists nor that an alert, invoice, Stripe object, data export, or external-system record has changed.

## Raw-detail coverage map

Use the exact raw page for the complete `ManagedEntity` enum and the `professional_service` `x-mint-enum` annotation; operation path, method, operation ID, bearer-security declaration, broad summary and Customer-specific use language, request description, required payload-property list, example payload, uniqueness wording, alert and invoice usage guidance, the HTTP `200` Success description, and shared OpenAPI tag descriptions. The raw page also preserves the absent operation-level request-body required marker, absent closed-object declaration, absent response content schema or example, and absent create-key error catalog. Use the dedicated custom-fields overview for its narrower entity list and its independent cross-object and archived-object uniqueness guidance, dedicated value-mutation references for object-value persistence and lifecycle, the dedicated idempotency authority for POST retry guarantees, and dedicated alert, invoice, Stripe-integration, and export sources for downstream behavior.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-custom-fields]], [[metronome-api-idempotency]], [[metronome-invoicing]]
- Supporting concepts: [[metronome-alerts-and-notifications]], [[metronome-integrations]]
- Related sources: [[source-metronome-api-reference-custom-fields]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/custom-fields/create-a-custom-field-key-2026-07-13|2026-07-13 snapshot — custom-field key creation schema, managed-entity scope, uniqueness constraint, downstream uses, and response boundary]]

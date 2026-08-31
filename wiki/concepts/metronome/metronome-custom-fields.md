---
title: "Metronome Custom Fields"
type: concept
category: technology
tags: [metronome, custom-fields, metadata, integrations]
---

## Definition

Metronome custom fields attach metadata such as foreign keys and other descriptors to platform objects. They preserve relationships between Metronome entities and records in external systems so those systems can contextualize Metronome data and support connected business processes.

## Entity scope and persistence

### Custom-field key creation contract

`POST /v1/customFields/addKey` adds an allowed custom-field key for one selected `ManagedEntity`. Within a supplied payload, `entity`, `key`, and boolean `enforce_uniqueness` are required, while the enclosing request body is not marked required and the object is not explicitly closed to unknown properties. The assigned endpoint presents unreconciled entity-applicability surfaces: broad summary language, a Customer-specific use bullet, and a 19-value request enum (`alert`, `billable_metric`, `charge`, `commit`, `contract_credit`, `contract_product`, `contract`, `customer`, `discount`, `invoice`, `professional_service`, `product`, `rate_card`, `scheduled_charge`, `subscription`, `package_commit`, `package_credit`, `package_subscription`, `package_scheduled_charge`). The existing overview independently says custom fields apply to most entities but lists only customer, product, contract, commit, credit, scheduled charge, rate card, and alert. Preserve all surfaces without treating any prose as merely illustrative or the enum as a reconciled platform-wide catalog; product versus `contract_product`, credit versus `contract_credit`, package variants, invoice, discount, charge, subscription, billable-metric, professional-service, and other label or coverage relationships remain unexplained. The exact enum and `professional_service` annotation remain in the raw source. `enforce_uniqueness` governs later value assignment: setting an already-existing value fails, but this endpoint does not define comparison or entity scope, normalization, activation timing, cross-`ManagedEntity` behavior, or an error response for that failure. The overview separately says uniqueness limits reuse across multiple objects and remains enforced for archived objects; preserve that broader overview-scoped guidance without importing it as this endpoint's comparison boundary. The create operation lists HTTP `200` with description `Success` but no response content schema or example, and it does not define a create-key error catalog, duplicate-key behavior, visibility, concurrency, or lifecycle. [[source-metronome-api-reference-custom-fields-create-a-custom-field-key]]

`POST /v1/customFields/removeKey` removes an `entity` and `key` pair from the custom-field allowlist. Within a supplied payload both properties are required, and `entity` is selected from the endpoint's 19-value managed-entity enum. Removal prevents future use across every instance of that entity type and makes existing values inaccessible, but the page does not say that stored values are physically erased, whether historical exports or invoices retain them, or whether re-adding the key restores access. The enclosing request body is not marked required, unknown-property behavior is unspecified, and the sole documented response is HTTP `200` without a response schema. [[source-metronome-api-reference-custom-fields-delete-a-custom-field-key]]

The legacy Plan-detail representation requires `custom_fields` and models it as an arbitrary-key object with string values annotated for the `plan` entity. The endpoint establishes this response shape but does not define configured-key completeness, key or value limits, ordering, permissions, redaction, freshness, mutation, persistence, export behavior, or propagation into invoices. [[source-metronome-api-reference-plans-get-plan-details]]

The overview lists customers, products, contracts, commits, credits, scheduled charges, rate cards, and alerts as supported entities. Values persist with an object and are returned wherever that object appears in the Metronome app, API calls, and data exports.

The customer-credit create schema accepts `custom_fields` for the `contract_credit` entity. The referenced `CustomField` is a typed object with `additionalProperties: {type: string}`. Under OpenAPI 3.0.1, neither schema sets `nullable: true`, so a supplied `custom_fields` value must be a non-null object and each supplied arbitrary property value must be a non-null string at the schema boundary. The endpoint does not define configured-key validation, uniqueness, limits, endpoint-specific runtime error mapping for invalid nulls, deletion-by-null semantics, overwrite behavior, persistence, API or export visibility, invoice propagation, or archived-credit handling; those behaviors must come from the dedicated custom-fields authority rather than this create operation.

The `listBalances` Commit and Credit response schemas can each expose optional `custom_fields` through an arbitrary-key object whose additional-property values are strings. The Commit field is annotated as entity `commit`; the Credit field is annotated `contract_credit`. This endpoint does not define key format, value length, field count, visibility, redaction, permissions, availability, or unset-value behavior.

The single-product response can expose optional `custom_fields` on `ProductListItem`, annotated as entity `contract_product`. The referenced object permits arbitrary property names whose values are strings. This endpoint establishes only the read shape and does not define configured-key validation, limits, ordering, visibility, redaction, permissions, freshness, persistence, export behavior, invoice propagation, or archived-product handling.


Package-term custom fields pass down to associated contracts. Package custom fields cannot be changed after they are set, while their contract-level descendants can be updated through `/customFields/setValues`; the guide lists package commit, credit, scheduled-charge, and subscription entities. [[source-metronome-guides-implement-metronome-core-concepts-packages-overview]]

Alert specifiers for the combined credit-and-commit low-balance alert filter applicable commits and credits by custom-field key-value conditions. A specific key and value includes matching balances; a key without a value groups evaluation by each unique value; exclusions remove matching balances after inclusion. Setting or updating a custom-field value on an applicable credit or commit triggers reevaluation of each balance alert using those specifiers. This is alert-evaluation behavior, not proof that the custom-field change mutates balance, ledger, contract, invoice, payment, or merchant entitlement state. The guide does not define case sensitivity, missing-key handling, duplicate conditions, concurrent-update ordering, or group-history behavior. [[source-metronome-guides-customers-billing-set-up-notifications-create-alert-specifiers]] [[source-metronome-api-reference-custom-fields]]

## Uniqueness

Uniqueness is intended for foreign entities that have a one-to-one relationship with a Metronome object. Enforcement continues for archived objects; resolving a duplicate involving an archived object requires resetting that object's field value.

## Invoice propagation

For Avalara AvaTax on Stripe-delivered invoices, the guide creates a case-sensitive Metronome Product custom field named `TaxCode`, assigns each product an Avalara tax code, and maps `ContractProduct.TaxCode` to `invoiceitem.metadata.TaxCode`. The page does not reconcile the Product and `ContractProduct` labels. It gives two source-scoped descriptions for a missing code—standard state sales tax for the customer's jurisdiction and an Avalara default rate that may misclassify—so neither should be generalized into a universal fallback code or behavior. [[source-metronome-integrations-tax-integrations-avalara]]

A Product custom field can propagate to the associated invoice line item. The overview's `stripe_product_id` example uses this propagation to link an invoice line item to a Stripe product when creating invoices in Stripe.

A managed custom-invoice integration can use Metronome custom fields as external-system identity mappings. The QuickBooks example recommends `qbo_item_id` on Product, `qbo_customer_id` on Customer, and optional `qbo_memo_ref` on Contract; customer and item objects live in the selected billing system, and a newly created QBO customer ID is written back to Metronome. These names and mappings are QBO-specific examples, not universal foreign-key, synchronization, uniqueness, or reconciliation guarantees. [[source-metronome-integrations-invoice-integrations-custom-invoice-integrations]]

For native Stripe Tax, a Product custom field named `stripe_product_id` maps the external Stripe product onto `invoiceitem.price.product`. Multiple Metronome products can intentionally share one Stripe product when they share a tax code, so the guide prohibits `enforce_uniqueness`; it also creates the field on `Product` while the mapping row names `ContractProduct`, leaving that entity-label relationship unresolved. [[source-metronome-integrations-tax-integrations-stripe-tax]]


The single-invoice response can expose optional invoice-level `custom_fields`. That property declares an object with unrestricted `additionalProperties: true` and no value schema, while client-group annotations qualify its documented availability. This endpoint does not establish key or value types, limits, redaction, permissions, freshness, configured-field absence, or general availability for that invoice-level map.

## Product listing surface

`POST /v1/contract-pricing/products/list` can return optional product `custom_fields` as an object with arbitrary property names and string values, annotated for the `contract_product` entity. The endpoint does not define key or value length, entry limits, ordering, visibility, redaction, configured-key absence, freshness, or whether every product custom field is returned. Listing the map does not mutate it or independently establish invoice-line propagation. [[source-metronome-api-reference-products-list-products]]


## Billable-metric response shape

The `GET /v1/billable-metrics` response schema can expose `custom_fields` on each returned billable metric as an object with arbitrary property names and string values. The field is optional because only metric `id` and `name` are required. This endpoint does not document custom-field key, value, or entry-count limits, visibility rules, redaction behavior, or whether every field configured elsewhere is returned through this listing. [[source-metronome-api-reference-billable-metrics-list-all-billable-metrics]]

## Customer retrieval surface

`GET /v1/customers/{customer_id}` returns the required customer `custom_fields` property as an open object with string-valued properties inside the customer detail. The endpoint does not define configured map-key ordering or endpoint-specific freshness, and its separate `customer_config` object must not be conflated with custom fields. [[source-metronome-api-reference-customers-get-a-customer]]


`GET /v1/customers` requires `custom_fields` on every returned customer detail as an arbitrary-key object with string values. The listing endpoint does not define key ordering, entry limits, visibility, redaction, freshness, or whether every configured customer field is returned. [[source-metronome-api-reference-customers-list-customers]]


The `POST /v1/customers/{customer_id}/setName` success representation can also include optional customer `custom_fields`, referencing the same arbitrary-key, string-valued map shape. Unlike the dedicated customer-detail retrieval schema, this mutation's `Customer` required list does not include `custom_fields`. The endpoint changes only `name` and does not define custom-field mutation, ordering, freshness, visibility, or propagation. [[source-metronome-api-reference-customers-update-a-customer-name]]

## Limits of the overview

The overview establishes the purpose, supported object examples, persistence, uniqueness, and invoice-line propagation of custom fields. It does not establish endpoint methods, request or response schemas, or endpoint-specific behavior; those details require complete reads of the relevant API references.

## Sources

- [[source-metronome-integrations-invoice-integrations-stripe]] — `stripe_product_id` as the required Metronome product custom-field mapping for payment-gated Stripe invoice line-item creation

- [[source-metronome-api-reference-custom-fields]] — overview, supported entity scope, persistence, uniqueness, and product-to-invoice-line propagation

- [[source-metronome-api-reference-billable-metrics-list-all-billable-metrics]] - billable-metric response custom fields as an arbitrary-key, string-valued object and undocumented limits

- [[source-metronome-api-reference-customers-get-a-customer]] — customer-detail retrieval of the string-valued custom-field map and endpoint-specific read boundaries

- [[source-metronome-api-reference-credits-and-commits-create-a-credit]] - contract-credit custom-field input shape and endpoint-specific validation and propagation limits

- [[source-metronome-api-reference-credits-and-commits-list-balances]] - optional commit and contract-credit custom-field response maps, string-valued additional properties, and endpoint-level limits and visibility unknowns


- [[source-metronome-api-reference-customers-list-customers]] — required customer-list custom-field response map and endpoint-specific visibility and freshness limits


- [[source-metronome-api-reference-customers-update-a-customer-name]] — optional string-valued customer custom-field map in the name-mutation response and non-mutation boundary


- [[source-metronome-api-reference-invoices-get-an-invoice]] - invoice-level unrestricted custom-field response shape and availability, typing, permission, and freshness limits

- [[source-metronome-api-reference-products-get-a-product]] - optional `contract_product`-annotated custom-field response map, arbitrary string-valued properties, and endpoint-specific visibility and freshness unknowns

- [[source-metronome-api-reference-products-list-products]] — optional string-valued product custom-field map and endpoint-specific visibility and freshness unknowns



- [[source-metronome-integrations-invoice-integrations-netsuite]] - product custom fields as NetSuite item foreign keys, mapping-error repair, and case-sensitive invoice metadata IDs for reconciliation

## Related

- [[metronome-integrations]]
- [[metronome-products-and-rate-cards]]
- [[metronome-customers-and-contracts]]
- [[metronome-invoicing]]
- [[metronome-reporting-and-analytics]]

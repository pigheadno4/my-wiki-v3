---
title: "Metronome API Reference: Create or Update Customer Ingest Aliases"
type: source
date_ingested: 2026-08-31
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/customers/create-or-update-customer-ingest-aliases"
raw_files:
  - "metronome/api-reference/customers/create-or-update-customer-ingest-aliases-2026-07-13.md"
tags: [metronome, api, customers, ingest-aliases, event-ingestion, idempotency]
---

## Overview

Bearer-authenticated `POST /v1/customers/{customer_id}/setIngestAliases` replaces the ingest-alias set of one customer identified by a required Metronome UUID. Aliases let usage events carry an application-owned identifier in `customer_id`; the operation can also model child organizations and can change which customer receives usage associated with a moved alias. This endpoint's state-level idempotence is distinct from the API-wide `Idempotency-Key` result cache.

## Query-critical facts

- The path `customer_id` is required and UUID-formatted. Within a supplied JSON payload, `ingest_aliases` is required and contains strings from 1 to 128 characters, with at most 2,000 items. The enclosing OpenAPI `requestBody` is not marked `required: true`, neither the payload object nor operation declares an `additionalProperties` policy, and the array has no `minItems`; omitted-body behavior, unknown-field handling, duplicate-element handling, and runtime acceptance of an empty array are not established.
- The explicit usage guideline says the call is idempotent and **fully replaces** the customer's alias set. Treat the submitted array as desired replacement state, not as an additive merge, despite the request-body description calling it "The aliases to add." The page does not define a patch mode, partial preservation, ordering significance, or a returned representation of the resulting set.
- An ingest alias can be supplied as the `customer_id` on usage events. The page says switching an alias to another customer associates all corresponding usage with the new customer and says multiple aliases can model child organizations under one customer. It does not define which historical, draft, finalized, rated, credited, invoiced, exported, or downstream records are reassociated, when the change becomes visible, or how to verify propagation.
- The separate API-wide alias authority says an alias already in use conflicts with HTTP `409` and must first be removed from its original customer, including an archived customer. Read together, "switching" is a remove-then-assign lifecycle, not evidence that one call can steal an alias from another customer. The assigned endpoint itself lists no conflict or other failure response.
- The operation lists only HTTP `200 Success` and provides no response content schema or example. It does not expose the applied set, affected events, propagation state, or an operation identifier, and it defines no endpoint-specific validation, not-found, authorization, alias-conflict, partial-failure, rollback, or reconciliation body.
- Endpoint-level idempotence means repeating the same desired set should not create an additional alias resource or a different final set. Separately, the API-wide `Idempotency-Key` authority applies to all POST endpoints: after execution begins, identical same-key parameters replay the persisted original result, changed parameters return HTTP `409`, retention is at least 24 hours, and a cached result can be HTTP `500`. Neither source defines no-key or different-key recovery, behavior after key expiry, concurrent replacement ordering, whether result replay proves current alias state, or safe recovery after an ambiguous failure.

## Material boundaries and tensions

- Preserve the endpoint's full-replacement rule over the weaker request description "The aliases to add"; implementing this as merge semantics can silently retain aliases that the caller meant to remove. Conversely, the schema's absence of `minItems` is not endpoint-specific runtime proof that an empty array successfully clears every alias.
- Preserve the API-wide remove-first precondition when interpreting this page's switching statement. The sources do not define atomic cross-customer transfer, transient unassigned intervals, concurrent writers, winner selection, isolation, or rollback if removal succeeds and assignment fails.
- "All corresponding usage" establishes an attribution consequence but not its temporal or financial closure. The page gives no read-after-write, event-reprocessing, invoice recalculation, finalized-document, ledger, alert, report, export, webhook, CRM, or downstream billing-provider guarantee.

## Raw-detail coverage map

Use the exact raw page for the operation path and ID, production server and bearer scheme, customer UUID parameter, complete replacement and switching language, child-organization guidance, request example, required payload-property list, alias length and count constraints, and sole HTTP `200` response description. The raw also preserves the absent request-body required marker, absent `minItems`, absent closed-object policy, absent response content schema, and absent endpoint failure catalog. Use the dedicated idempotency authority for alias reservation and POST request-cache behavior, the ingest-events authority for event payload and deduplication semantics, and the customer provisioning and retrieval authorities for broader customer lifecycle and read surfaces.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-customers-and-contracts]], [[metronome-event-ingestion]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-api-reference-idempotency]], [[source-metronome-api-reference-usage-ingest-events]], [[source-metronome-api-reference-customers-create-a-customer]], [[source-metronome-api-reference-customers-get-a-customer]], [[source-metronome-api-reference-customers-archive-a-customer]], [[source-metronome-guides-implement-metronome-core-concepts-provision-customer]]

## Raw Sources

- [[raw/metronome/api-reference/customers/create-or-update-customer-ingest-aliases-2026-07-13|2026-07-13 snapshot - customer ingest-alias replacement, usage reassignment, request schema, and response boundary]]

---
title: "Metronome API Reference: Get an Embeddable Customer Dashboard"
type: source
date_ingested: 2026-08-31
original_format: webpage
canonical_url: "https://docs.metronome.com/api-reference/customers/get-an-embeddable-customer-dashboard"
raw_files:
  - "metronome/api-reference/customers/get-an-embeddable-customer-dashboard-2026-08-28.md"
tags: [metronome, api, dashboards, embedded-ui, customer-portals]
---

## Overview

Bearer-authenticated `POST /v1/dashboards/getEmbeddableUrl` generates a customer-specific URL for embedding a Metronome billing dashboard in an iframe. The operation covers invoice, usage, and commit-and-credit views plus optional presentation controls, but its generated-URL contract is intentionally narrow: the page does not establish an exact lifetime, refresh or revocation behavior, browser-exposure controls, or dashboard-data freshness.

## Query-critical facts

- Within a supplied JSON payload, UUID `customer_id` and `dashboard` are required; `dashboard` is one of `invoices`, `usage`, or `commits_and_credits`. The enclosing OpenAPI `requestBody` is not marked `required: true`, and neither the payload nor its nested option objects declare `additionalProperties: false`, so omitted-body and unknown-field runtime behavior are not established.
- Optional `dashboard_options` is an array whose items require string `key` and `value`. The narrative says dashboard options are supported only for the invoices dashboard and documents zero-usage-line-item, contract, invoice-type, and invoice-status filters. The schema additionally lists deprecated `hide_voided_invoices` and `billable_status_filter`; it gives value semantics for the deprecated key but none for `billable_status_filter`. The page does not define whether option/dashboard mismatches are rejected, ignored, or applied.
- Optional `color_overrides` supplies named dashboard colors and hex-string values. Its item schema does not require either `name` or `value`, and the page defines no validation, fallback, contrast, accessibility, or unsupported-color behavior.
- HTTP `200` requires a top-level `data` object whose `url` property is a string, but `url` is not listed as required inside `data`. The example places the generated URL at `data.url` on `embeddable-dashboards.metronome.com`; there is no separately returned token, expiry timestamp, dashboard identifier, or refresh handle.
- The narrative characterizes the returned URL as secure, time-limited, iframe-ready, customer-specific, and containing authentication tokens plus configuration parameters. That is generated-URL authority, distinct from the bearer token used to call the API. The page does not define whether the URL inherits caller permissions, its exact TTL or start time, single-use or sharing behavior, rotation, revocation, regeneration, invalidation after customer or contract changes, origin restrictions, CSP or cookie requirements, logging or referrer exposure, or behavior after expiry.
- The operation documents only generic HTTP `400 Bad request`. It gives no endpoint-specific authorization, not-found, unsupported-dashboard, option-validation, rate-limit, timeout, token-minting, partial-result, or recovery contract.
- The separate API-wide POST idempotency authority applies `Idempotency-Key` result replay to all POST endpoints: identical same-key parameters return the original result and keys persist for at least 24 hours. The endpoint does not relate that retention window to the generated URL's unspecified lifetime, so replay is not proof that a URL was newly minted, remains valid, or reflects fresh dashboard configuration or customer state.

## Material boundaries and tensions

> [!warning] Narrative versus option schema
> The narrative's invoices-only option list names four keys, while the payload schema enumerates two more: deprecated `hide_voided_invoices` and undocumented-value `billable_status_filter`. Treat the schema as evidence that those key names are documented, not as proof of runtime acceptance for every dashboard type or of any unlisted value semantics.

> [!warning] Promised URL versus response requiredness
> The prose presents a secure time-limited URL as the key result, but the success schema requires only `data`; nested `data.url` is optional in the schema. The page does not resolve whether a successful response can omit the URL or how a caller should recover if it does.

This API surface is separate from Metronome's beta dashboards and generated CSV reports inside the Metronome app, whose enablement, audience, and freshness statements do not define the embedded URL's lifecycle. It is also separate from the operator-focused Metronome Dashboard Quickstart. A dedicated hierarchy guide separately says invoice and commit embeddable dashboards do not work for customers whose contract participates in a hierarchy; this endpoint page does not repeat that limitation, explain its failure mode, or say whether the `usage` dashboard is affected.

## Raw-detail coverage map

- **Operation and request:** use the raw page for the exact production path, POST method, bearer-security declaration, operation ID, request example, supplied-payload requiredness, dashboard enum, and absence of an operation-level request-body required marker or closed-object declaration.
- **Dashboard controls:** use raw for the complete dashboard-option key enum and value descriptions, the deprecated key annotation, the full color-name enum, the example overrides, and immediate-parent requiredness.
- **Response and failure:** use raw for the required outer `data` object, optional nested URL schema, example host and placement, and the sole documented `400` response.
- **Lifecycle and exposure:** the raw prose establishes only that the URL is customer-specific, contains authentication tokens and configuration parameters, and is time-limited and iframe-ready. It does not provide an expiry value, freshness marker, refresh or revocation API, browser isolation requirements, failure recovery, or a relationship between URL lifetime and API-wide idempotency retention.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-reporting-and-analytics]], [[metronome-security-principles]], [[metronome-customers-and-contracts]], [[metronome-api-idempotency]]
- Related sources: [[source-metronome-guides-reporting-insights-in-app-reporting]], [[source-metronome-guides-get-started-metronome-dashboard-quickstart]], [[source-metronome-guides-pricing-packaging-billing-model-guides-model-hierarchical-customer-relationships]], [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-idempotency]]

## Raw Sources

- [[raw/metronome/api-reference/customers/get-an-embeddable-customer-dashboard-2026-08-28|2026-08-28 snapshot - customer-scoped embedded dashboard request, generated URL response, options, colors, authentication, and lifecycle boundaries]]

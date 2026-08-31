---
title: "Build API-powered customer dashboards"
type: source
date_ingested: 2026-08-31
canonical_url: "https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/customer-dashboards-and-reporting"
original_format: webpage
raw_files:
  - "metronome/guides/customers-billing/optimize-customer-experience/customer-dashboards-and-reporting-2026-08-28.md"
tags: [metronome, customer-dashboards, usage, balances, invoice-breakdowns, embedded-ui]
---

## Overview

This guide presents two customer-facing billing-visibility patterns: a merchant-owned dashboard whose backend queries Metronome APIs, and Metronome-hosted invoice, usage, or commit-and-credit dashboards embedded by generated URL. It routes usage, current spend, detailed and net balances, invoice history, and self-service presentation, but its worked payloads and pseudocode are illustrations rather than current endpoint authority.

## Query-critical facts

- The merchant-owned pattern is frontend to merchant backend to Metronome. Metronome API bearer tokens stay in the backend; the guide expressly says not to expose them to users or frontend clients. The dedicated authentication authority places the bearer value in the `Authorization` header and documents customer-token permissions separately from the credential-bearing URL returned for an embedded dashboard.
- Current granular-usage authority is bearer-authenticated `POST /v1/usage`. Its supplied payload requires `starting_on`, `ending_before`, and `window_size`; customer selection is `customer_ids`, while metric selection is `billable_metrics`, whose items carry `id` and optional nested `group_by`. HTTP `200` requires sibling `data` and nullable `next_page`; each current item uses customer and metric identity, `start_timestamp`, `end_timestamp`, `value`, and optional `groups`. The guide instead sends singular top-level `customer_id`, `billable_metric_id`, and `group_by`, then illustrates `group_key`, `group_value`, `starting_on`, and `ending_before` inside each item. Preserve this as material guide-versus-current-API drift and do not implement the guide shape as the current contract.
- For customer balances, bearer-authenticated `POST /v1/contracts/customerBalances/list` is the detailed commit-or-credit route. The guide requests ledgers, calculated balance, contract balances, and records with access on or after `starting_at`; it says `include_balance: true` returns value available now and excludes upcoming segments. Current HTTP `200` requires envelope siblings `data` and nullable `next_page`. Bearer-authenticated `POST /v1/contracts/customerBalances/getNetBalance` is the aggregate route; current success places required `balance` and `credit_type_id` under required outer `data`. Both operations have required properties inside supplied payloads while their OpenAPI `requestBody` wrappers are not marked required, and neither page establishes omitted-body behavior.
- Current spend authority is bearer-authenticated `GET /v1/customers/{customer_id}/invoices/breakdowns`, with required RFC 3339 `starting_on` and `ending_before` query values and optional hourly or daily `window_size`. HTTP `200` requires sibling `data` and nullable `next_page`; each `data` item is an invoice window containing `line_items`, not one response object per line item. The guide correctly illustrates negative commit or credit application lines, but those observations do not prove ledger mutation, immutable accounting state, downstream delivery, payment, tax, or reconciliation.
- The current invoice-breakdown authority caps a daily request at 35 days and an hourly request at 24 hours, supports cursor traversal, and says backdated usage can change breakdowns after invoice finalization. It defines no revision, as-of selector, freshness SLA, cursor snapshot, or immutable historical-population guarantee. The guide's "real-time" usage, balance, and spend language likewise supplies no measurable visibility or cross-endpoint consistency commitment.
- Bearer-authenticated `POST /v1/dashboards/getEmbeddableUrl` accepts required `customer_id` and dashboard selector within a supplied payload; the dashboard enum is `invoices`, `usage`, or `commits_and_credits`. Current HTTP `200` requires outer `data` but does not require nested `data.url`. The dedicated page calls the customer-specific iframe URL time-limited and token-bearing but gives no TTL, expiry timestamp, refresh, revocation, origin, sharing, browser-exposure, permission-inheritance, or data-freshness contract.
- The guide describes embedded invoice history for draft, finalized, and voided invoices up to 90 days old; usage metrics on the current contract for the past 30, 60, or 90 days; and current and historical commit and credit grants, deductions, access schedules, balances, and expirations. Invoice-only options cover zero-usage lines, contract, invoice type, and status. These UI descriptions do not broaden the generated-URL lifecycle or prove complete API, export, accounting, or hierarchy coverage.

## Material boundaries and contradictions

> [!warning] Usage worked example conflicts with the current dedicated API
> The guide's singular usage selectors and item-level group and time fields do not match the current batch payload or `UsageBatchAggregate` schema. Use the dedicated current operation for method, body nesting, required fields, item placement, grouping, and pagination; retain this guide for the customer-dashboard outcome and illustrative transformation only.

> [!warning] Spend pseudocode is not copy-ready
> The backend loop unconditionally reads `line_item['presentation_group_values']['region']`, while the guide's own applied-credit line has no `presentation_group_values`. Its backend emits direct region keys, but the frontend searches for keys ending `_start`, so the two snippets do not share one chart-data contract. The unconditional `/ 100` conversion is supported only by the example's `USD (cents)` credit type and must not be generalized to other fiat or custom pricing units.

The guide's lowercase color names such as `gray_dark` and `primary_medium` differ from the dedicated request enum's `Gray_dark` and `Primary_medium`. Treat the current dedicated schema as request authority and do not infer case normalization. The guide also mentions Data Export as an adjacent integration option but supplies no destination, table-grain, cadence, freshness, duplicate-delivery, completeness, or reconciliation procedure; use the dedicated Data Export sources for those decisions.

Because `/v1/usage`, `/list`, `/getNetBalance`, and `/getEmbeddableUrl` are POST operations, the separate API-wide `Idempotency-Key` authority applies. Identical same-key parameters replay the original result, changed parameters conflict, retention is at least 24 hours, and a cached result can be HTTP `500`. For these read or URL-generation operations, replay does not prove fresh usage, balance, invoice, dashboard configuration, or a newly minted and still-valid embedded URL; endpoint-specific cursor, concurrency, recovery, and freshness behavior remains undocumented.

## Raw-detail coverage map

- **Merchant-owned UI:** use raw for dashboard goals, the backend/frontend boundary, all usage, detailed-balance, net-balance, and invoice-breakdown requests and responses, chart pseudocode, screenshots, and illustrative identifiers and values.
- **Usage and spend examples:** use raw for the October windows, region breakdowns, response examples, commit-deduction illustration, and pseudocode defects; use current dedicated API authorities for request nesting, requiredness, response placement, pagination, temporal caps, and schema.
- **Balances:** use raw for the prepaid-and-reward scenario, grant and ledger examples, available-now statement, aggregation pseudocode, and net-balance route; use dedicated authorities for complete filters, pagination, denomination, calculated-balance floor, freshness, and response schemas.
- **Embedded UI:** use raw for the three dashboard descriptions, 90-day invoice history, 30/60/90-day usage views, commit-and-credit history, invoice option list, iframe flow, and color walkthrough; use the dedicated endpoint for current option enums, supplied-payload requiredness, `data.url` placement, errors, and URL-lifecycle unknowns.
- **Adjacent export:** the raw page only names Data Export as an integration feature. It does not contain the export delivery, schema, freshness, environment, deduplication, or completeness contract.

## Related

- Company: [[metronome]]
- Primary concepts: [[metronome-reporting-and-analytics]], [[metronome-billable-metrics]], [[metronome-credits-and-commits]], [[metronome-invoicing]], [[metronome-security-principles]]
- Supporting concepts: [[metronome-api-idempotency]], [[metronome-currencies-and-custom-pricing-units]], [[metronome-customers-and-contracts]], [[metronome-usage-based-billing]]
- Dedicated authorities: [[source-metronome-api-reference-authentication]], [[source-metronome-api-reference-credits-and-commits-list-balances]], [[source-metronome-api-reference-invoices-list-invoice-breakdowns]], [[source-metronome-api-reference-customers-get-an-embeddable-customer-dashboard]], [[source-metronome-api-reference-idempotency]]
- Export context: [[source-metronome-guides-reporting-insights-data-export-overview]], [[source-metronome-guides-reporting-insights-data-export-database-reference]]

## Raw Sources

- [[raw/metronome/guides/customers-billing/optimize-customer-experience/customer-dashboards-and-reporting-2026-08-28|2026-08-28 snapshot - merchant-built and embedded customer dashboards, worked API examples, UI scopes, and authority conflicts]]

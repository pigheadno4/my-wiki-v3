---
title: "Metronome Billable Metrics"
type: concept
category: technology
tags: [metronome, billable-metrics, aggregation, usage-based-billing]
---

## Definition

A Metronome billable metric defines a per-customer aggregation over a selected subset of usage events. It connects raw event data to a chargeable product by declaring which events match, which property to aggregate, how to aggregate it, and how to group the result.

## Matching and aggregation

The Basic Filters editor always creates a streaming billable metric. Its worked API-call example matches event type `api_request`, filters `status` to `success`, requires `user_id` to exist, uses `COUNT`, and groups the result by `user_id`; the equivalent API payload expresses those choices with `event_type_filter.in_values`, `property_filters`, `aggregation_type`, and nested `group_keys`. The example does not define general multi-filter boolean rules, include/exclude precedence, coercion, duplicate handling, time windows, late events, or when matching begins.

- The create API allows either a SQL string or standard filter/aggregation fields; SQL is mutually exclusive with aggregation type, event-type filter, property filters, aggregation key, and group keys.
- All supplied property filters must pass. Event and property filters support include and exclude lists, while property filters also control existence.
- `event_type_filter` limits matching by event type and can be omitted to consider all event types.
- `property_filters` declare expected event properties. A property marked `exists=true` prevents matching when that property is absent.
- `aggregation_key` selects the value to aggregate.
- Streaming metrics support `COUNT`, `SUM`, `MAX`, and `LATEST`; `LATEST` uses the most recent property value in the billing period. Distinct counts require a SQL metric.
- The create endpoint additionally enumerates lower-, title-, and uppercase forms of `UNIQUE`, contradicting the guide's SQL-only distinct-count direction. It does not define UNIQUE semantics or promise general case normalization.
- `group_keys` divide usage into buckets, similar to SQL `GROUP BY`, and can support grouped invoice presentation.
- A pricing group key permits dimension-specific rates, while a presentation group key creates invoice breakdowns without changing the price.
- When presentation and pricing dimensions are both needed, their properties must be combined in one compound metric group key. On a streaming metric, each group-key property must first use an `Exists` or `In` property filter, and group keys cannot be edited after creation.
- Customer-level group-key cardinality approaching one thousand values can increase API latency; the guide treats this as a reason to contact Metronome, not a hard limit.
- Context retained on usage events can support later metric changes. The event-design guide uses `domain` for grouped usage reporting and `data_center` for region-specific metrics and prices.
- A billable metric aggregates one property by default. Derived calculations across properties, such as multiplying recipient count by message size, require a SQL-based metric.
- Each usage product references one previously created metric, while the same metric can support multiple products. Product-side pricing and presentation keys can use only group keys already defined on that metric.
- One usage event can contribute to multiple billable metrics. The architecture guide does not define matching precedence or safeguards against unintended multi-product charging, so this cardinality should not be interpreted as automatic charge deduplication.
- Dimensional pricing can map one metric to one product and then many rates. Rate combinations depend on product pricing keys whose properties originate as group keys on the underlying metric; the rate-card guide does not supersede metric creation or immutability rules.

## SQL query, output, and timing semantics

- SQL metrics query `events` through `event_type`, `timestamp`, and `properties.field_name`; Metronome applies customer and billing-period filtering. The concept currently leaves SQL output rules undefined; replace that boundary with the documented multi-column rule: `value` is preferred, the first returned column is the fallback when `value` is absent, other columns can become pricing or presentation keys, and unused extra columns are summed over. The page does not define the quantity-column rule for a one-column result or runtime behavior for missing, duplicate, or nonnumeric quantity columns.

> [!warning] Cross-source SQL output contradiction
> The earlier create-metrics guide and its source summary call `value` required, while the SQL Editor guide documents first-column fallback for a multi-column result without `value`. Treat `value` as preferred rather than universally mandatory for that documented multi-column case, and add a reciprocal contradiction warning to the earlier source summary.

- The SQL Editor documents `COUNT`, `SUM`, `MAX`, `MIN`, `AVG`, timestamp-based `EARLIEST` and `LATEST`, and `COUNT DISTINCT`, plus bounded math, logic, `DATE_TRUNC` to hour or day, and `CAST`. This aligns with the neighboring guides’ direction to use SQL for distinct counts but does not reconcile their `UNIQUE` label or the API enum.
- In the guide’s simple `SUM` example, the default `hour` breakdown incurs each event as usage is ingested. For that example only, `service period` moves the full quantity of 30 and its cost to the final period window, applies the final $20 price to the full quantity, and requires a credit or commit to cover the last instant of the period. These outcomes do not establish the behavior of every non-additive aggregation, overlapping schedule, late-event, or invoice-finalization case.
- SQL metric swaps may be scheduled within a billing period. In the guide’s two-SQL-metric average example, the combined value after the swap is the new metric through the current day plus the old metric through the swap day minus the new metric through the swap day; the new metric’s pre-swap term is zero in that example, and the documented incurred quantities are example-scoped. The page does not define exact cutoff inclusivity, timezones, one-SQL/one-streaming transitions, `service period` interactions, falling values, negative adjustments, late corrections, finalized-invoice behavior, or subsequent-period behavior.
- The documented SQL item list does not identify a dialect or define literal Unicode-versus-ASCII comparison syntax, type coercion, null behavior, precision, output limits, tie handling, or error semantics.

## Lifecycle boundary

### Sampled event-to-metric diagnostics

`POST /v1/events/search` can return an optional `matched_billable_metrics` array for events retrieved by transaction ID within the last 34 days. Each returned metric object inherits required `id` and `name` and may expose aggregation, grouping, filtering, custom-field, SQL, and archive fields in the returned schema alongside deprecated `group_by`, `aggregate`, `aggregate_keys`, and `filter`. Its search-specific aggregation enum includes case variants of count, latest, max, sum, and unique plus `custom_sql`; this does not resolve the existing `UNIQUE`-versus-SQL-distinct ambiguity or promise case normalization.

Metronome positions this sampling-only, heavily rate-limited endpoint for checking whether raw events match active billable metrics and for investigating pipeline changes or metric misconfiguration. The page does not define whether matches reflect ingest-time or search-time metric configuration, whether an absent or empty array means no match or unavailable diagnostics, or how archived metrics, reflow, late changes, and duplicate events affect the result. A sampled match is evidence about the returned event, not proof that every intended event matched, was rated, reached an invoice, or prevented revenue leakage.

Contract usage filters impose upstream schema requirements. For streaming metrics, the filter key must be an existing group key and must join pricing and presentation keys in one compound key when those dimensions coexist. For SQL metrics, the filter key must be present as an underlying event property.

The SDK and event-design guides state that billable metrics match only usage events sent after metric creation by default. The create-metrics guide adds that Metronome retains raw events and can perform a representative-assisted reflow when earlier events need to apply to a new streaming metric. The page does not define reflow timing, eligibility, cost, or operational limits.

> [!warning] Documentation scope
> The event-design source says new metrics cannot apply retroactively, while the create-metrics guide documents a Metronome-assisted reflow exception. Treat forward-only attribution as the default self-service behavior and reflow as an exception requiring confirmation.

> [!warning] Create-schema contradictions
> The endpoint says `aggregation_key` must name a property filter, is required when SQL is absent, and is inapplicable to count, while only `name` is schema-required and another description incorrectly calls it the aggregation type. Property-filter `not_in_values` also says empty is allowed and non-empty is required. Nested group-key limits, duplicate behavior, SQL output rules, and include/exclude precedence are not defined.

The dashboard quickstart distinguishes streaming metrics for most real-time aggregation use cases from SQL metrics for calculations such as daily averages, unique period counts, or weighted formulas. It also states that group keys, property filters, and aggregation settings cannot be modified after metric creation.

The ingest API reference says accepted events are matched to billable metrics and become immediately available for usage and spend calculations, but it does not define per-event match results or failure behavior.

After metric creation, the guide recommends sending test events through `/ingest` and retrieving them by `transaction_id` through `searchEvents`; the response can show the matched metric and customer.

Because usage-event structures target particular metrics, changing the producer schema can stop downstream metrics from recording usage. Metronome recommends validating and testing event-structure changes with a representative.

## Retrieval APIs

`GET /v1/billable-metrics/{billable_metric_id}` returns one metric configuration under `data`; only `id` and `name` are required in `BillableMetricV1`. An archived metric remains retrievable with RFC 3339 `archived_at` and stops processing new usage events. The endpoint documents `404`, but not archive propagation, permissions, rate limits, or consistency.

`GET /v1/customers/{customer_id}/billable-metrics` lists metrics available to one customer. It accepts limits from `1` to `100`, returns required nullable `next_page`, and can filter to the current plan or include archived metrics. Items require `id` and `name` and can carry current standard or SQL fields plus deprecated `group_by`, `aggregate`, `aggregate_keys`, and `filter`.

`GET /v1/billable-metrics` provides an account-wide, bearer-authenticated configuration inventory with optional `limit` (`1` to `100`), string `next_page`, and boolean `include_archived` query parameters. Archived metrics are excluded by default and require `include_archived=true`; HTTP `200` requires a `data` array and nullable `next_page`. Returned items require only UUID `id` and string `name`, while filters, aggregation, grouping, custom fields, SQL, and archive timestamp remain optional. The endpoint supplies no ordering, cursor-lifetime or snapshot guarantee, metric-type discriminator, product association, orphan-status field, or non-200 response contract. Its example also repeats the schema defect in which `aggregation_key: bytes` does not name any listed property filter.

The retrieval schemas preserve the create-schema conflicts: `UNIQUE` remains unexplained, SQL and standard configuration have no discriminator, and include/exclude precedence, empty `not_in_values`, aggregation-key requiredness, and group-key limits remain undefined. The customer-list example also uses `aggregation_key: bytes` without a matching property-filter name and shows conflicting `group_by` and `group_keys` values.

## Group-key alert scoping

Dimension-scoped spend alerts require their `group_values` key to be a group key on the underlying billable metrics associated with the customer's contract. Products whose metric lacks the key do not contribute to that threshold. Metronome recomputes the selected usage as if the key were a presentation group, so tiered pricing, quantity rounding, and `MAX` aggregation apply to the subset. A customer can use three distinct keys for spend-threshold notifications; a fourth is blocked. When one key has more than 5,000 values for that customer, the guide calls for representative consultation rather than defining a hard maximum.

## Sources

- [[source-metronome-api-reference-usage-search-events]] — sampled transaction-ID retrieval, optional matched-metric configuration diagnostics, 34-day occurrence window, heavy-rate-limit boundary, and non-exhaustive leakage evidence

- [[source-metronome-guides-implement-metronome-core-concepts-billable-metrics-sql-editor]] — SQL functions and outputs, breakdown granularity, scheduled metric swaps, and unresolved SQL-runtime boundaries

- [[source-metronome-guides-implement-metronome-core-concepts-billable-metrics-basic-filters]] — Basic Filters event matching, property existence, grouped `COUNT`, streaming aggregation set, and unresolved `UNIQUE` boundary
- [[source-metronome-guides-events-send-usage-events]] — required event fields plus string-property representation and precision rationale

- [[source-metronome-guides-get-started-developer-sdks]] — metric definition, filters, aggregation operations, grouping, and creation-time boundary
- [[source-metronome-guides-events-design-usage-events]] — future metric flexibility and the non-retroactive processing boundary
- [[source-metronome-guides-get-started-metronome-dashboard-quickstart]] — streaming and SQL roles, downstream group-key uses, and immutability
- [[source-metronome-api-reference-usage-ingest-events]] — ingest-time matching statement and response-documentation boundary
- [[source-metronome-guides-implement-metronome-core-concepts-create-billable-metrics]] — streaming and SQL roles, group-key constraints, assisted reflow, and matching tests
- [[source-metronome-guides-implement-metronome-core-concepts-send-usage-events]] — single-property default, SQL-derived aggregation boundary, and event-schema change risk
- [[source-metronome-guides-implement-metronome-core-concepts-create-products-contracts]] — metric-to-product cardinality and product-side group-key dependency
- [[source-metronome-guides-get-started-how-metronome-works]] — event-to-metric cardinality and metering-layer role
- [[source-metronome-guides-implement-metronome-core-concepts-provision-contract]] — usage-filter prerequisites for streaming and SQL metrics
- [[source-metronome-guides-implement-metronome-core-concepts-create-manage-rate-cards]] — metric/product/many-rate relationship
- [[source-metronome-api-reference-billable-metrics-create-a-billable-metric]] — create schema, SQL exclusivity, filters, aggregation contradictions, nested groups, and UUID response
- [[source-metronome-api-reference-billable-metrics-get-a-billable-metric]] — single-metric retrieval, archive visibility, and response-schema boundaries
- [[source-metronome-api-reference-billable-metrics-get-billable-metrics-for-a-customer]] — customer-scoped pagination, filters, deprecated fields, and example defects
- [[source-metronome-guides-customers-billing-optimize-customer-experience-customer-controls]] — group-key requirements, subset repricing, three-key limit, and high-cardinality consultation for spend alerts

- [[source-metronome-api-reference-billable-metrics-list-all-billable-metrics]] - account-wide configuration listing, 1-100 cursor pagination, archived-by-default exclusion, response-schema boundaries, and the aggregation-key example defect

## Related

- [[metronome-event-ingestion]]
- [[metronome-products-and-rate-cards]]
- [[metronome-usage-based-billing]]

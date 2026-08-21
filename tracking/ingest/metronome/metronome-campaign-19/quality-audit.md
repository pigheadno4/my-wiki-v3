# Metronome Campaign 19 Close Quality Audit

- Auditor posture: independent Sol-high close audit
- Audit date: 2026-08-21
- Fixed sample: `list-account-level-billing-providers`, `search-events`, `get-subscription-quantity-history`
- Query families per page: factual retrieval; boundary and contradiction handling; exact raw deep-dive and navigation
- `closure_approved: true`
- `expansion_required: false`

## Verdict

**PASS.** All nine fixed-sample queries passed. No material partial or failure was found, so the audit stops at the required three-page sample and does not expand to the other two Campaign 19 pages.

This audit did not use worker or reviewer summaries as evidence. For every sampled job, it independently read the full canonical source and full assigned raw page, inspected relevant canonical concept context, and read the Metronome company page and provider index. Attempt-2 candidates were used only for byte-equality promotion checks.

## Mechanical totals

| Check | Result |
| --- | ---: |
| Sampled pages | 3 |
| Query cases | 9 |
| Query passes | 9 |
| Query partials | 0 |
| Query failures | 0 |
| Raw SHA-256 matches | 3/3 |
| Canonical sources byte-equal approved attempt-2 candidates | 3/3 |
| Exact canonical URLs | 3/3 |
| Exact `raw_files` entries | 3/3 |
| Exact path-qualified Raw Sources backlinks | 3/3 |
| Company catalog entries exactly once | 3/3 |
| Provider-index entries exactly once | 3/3 |
| Fact-bearing source-to-concept reciprocal targets present | 4/4 |
| Targeted wiki validation | 8/8 source, concept, and company files passed |

`wiki/metronome-index.md` was checked directly as the provider catalog. It intentionally has no YAML frontmatter, so it was excluded from the page-schema validator after that validator reported only the non-applicable missing-frontmatter condition. Its sampled entries and counts were checked mechanically.

For the fixed Campaign 19 sample, the catalog totals are exact: all three sampled source links occur once, and only once, in both the company page and provider index. The company frontmatter reports `source_count: 117`; this audit did not reinterpret that campaign-close count from unrelated historical catalog entries.

## 1. list-account-level-billing-providers

### Evidence identity and promotion

- Canonical source: `wiki/sources/metronome/source-metronome-api-reference-settings-list-account-level-billing-providers.md`
- Raw source: `raw/metronome/api-reference/settings/list-account-level-billing-providers-2026-07-13.md`
- Raw SHA-256: `551bec920ee2040d737c6bf789c7fda844067ca5f8593b044944a910c55e3524` — match
- Approved attempt-2 candidate equality: exact byte match
- Canonical URL: `https://docs.metronome.com/api-reference/settings/list-account-level-billing-providers.md` — exact
- Raw frontmatter entry and backlink: exact
- Company entry: exactly one
- Provider-index entry: exactly one
- Fact-bearing reciprocal concept: `wiki/concepts/metronome/metronome-integrations.md` cites the source in both the durable fact and Sources catalog; the source links `[[metronome-integrations]]`.
- `[[metronome-customers-and-contracts]]` and `[[metronome-invoicing]]` are contextual navigation links rather than concepts receiving a new durable fact from this raw page, so they do not require reciprocal citations to this source.

### BP-F1 — factual retrieval

**Query:** What does the endpoint list, how is pagination represented, and what fields are guaranteed for each returned entry?

**Answer supported by source and raw:** `POST /v1/listConfiguredBillingProviders` enumerates account-configured billing providers and delivery-method configurations. The optional request object documents a nullable UUID `next_page` cursor; neither `requestBody` nor the property is marked required. HTTP 200 requires a `data` array. Each item requires `billing_provider`, UUID `delivery_method_id`, `delivery_method`, and an open-ended `delivery_method_configuration`. The response may also carry a nullable UUID `next_page`.

The source accurately preserves all nine provider enum values and all four delivery-method enum values. It also preserves that delivery configuration may omit security-sensitive values.

**Verdict: PASS.**

### BP-B1 — boundary and contradiction handling

**Query:** Can a caller treat `delivery_method_id` as a customer billing-provider configuration or contract selector, and does enumeration prove invoice-delivery readiness?

**Answer supported by source, raw, and concept context:** No. The raw page describes an account-level enumeration and says the identifier is used for a customer, but it does not establish equivalence with the distinct customer configuration and contract selector identifiers documented in integration context. The canonical source explicitly prevents that substitution. It also correctly states that enumeration does not create or mutate mappings, prove that a customer or contract selects the provider, or guarantee routing, readiness, payment collection, tax, reconciliation, or downstream delivery success.

The request schema documents `next_page` but does not set `additionalProperties: false`; the source correctly leaves unknown whether unrecognized request fields are accepted, ignored, or rejected. No contradiction was found.

**Verdict: PASS.**

### BP-N1 — exact raw deep-dive and navigation

**Query:** Can a reader navigate from the canonical source to the exact raw snapshot and verify the authoritative URL and schema boundaries?

**Answer:** Yes. `canonical_url`, `raw_files`, and the path-qualified Raw Sources link all exactly identify the approved URL and dated raw file. The raw hash matches the trusted Campaign 19 value. The source is byte-identical to the attempt-2 candidate and is present exactly once in both provider catalogs.

**Verdict: PASS.**

## 2. search-events

### Evidence identity and promotion

- Canonical source: `wiki/sources/metronome/source-metronome-api-reference-usage-search-events.md`
- Raw source: `raw/metronome/api-reference/usage/search-events-2026-07-13.md`
- Raw SHA-256: `2869bcb9d81a7cde19bd11dde93807374b6bd295ec4dc03b892b6090200a3aaa` — match
- Approved attempt-2 candidate equality: exact byte match
- Canonical URL: `https://docs.metronome.com/api-reference/usage/search-events.md` — exact
- Raw frontmatter entry and backlink: exact
- Company entry: exactly one
- Provider-index entry: exactly one
- Fact-bearing reciprocals: `wiki/concepts/metronome/metronome-event-ingestion.md` and `wiki/concepts/metronome/metronome-billable-metrics.md` each cite this source and accurately preserve its sampling, matching, time-window, configuration-snapshot, and completeness boundaries.
- `wiki/concepts/metronome/metronome-api-idempotency.md` correctly cites the separate idempotency authority, not this derivative search page. The search source links both that concept and the authoritative idempotency source, so no incorrect reciprocal attribution is required.

### SE-F1 — factual retrieval

**Query:** What can Search Events retrieve and what response information can it return?

**Answer supported by source and raw:** Bearer-authenticated `POST /v1/events/search` retrieves events by supplied transaction IDs when the events occurred within the last 34 days. When a body is supplied, its schema requires a `transactionIds` string array, while the enclosing `requestBody` is not marked required. HTTP 200 returns an array whose items require `id`, `transaction_id`, `customer_id`, `event_type`, and RFC 3339 `timestamp`; optional diagnostics include open event properties, `processed_at`, `is_duplicate`, a matched customer, and matched billable metrics with returned schema/configuration fields.

The source correctly records that the endpoint is heavily rate limited and intended only for sampling, without inventing a numeric rate limit, pagination, result ordering, missing-ID behavior, array limits, or exact cutoff inclusivity.

**Verdict: PASS.**

### SE-B1 — boundary and contradiction handling

**Query:** Does a sampled match prove complete ingestion, correct billing, or absence of revenue leakage, and does a keyed replay prove fresh matching state?

**Answer supported by source, raw, and concept context:** No. A returned event and its matches are evidence only for that returned sample. They do not prove that every producer event arrived, every intended metric matched, quantities were rated correctly, invoices included the usage, downstream billing succeeded, or revenue leakage was prevented or recovered.

The canonical source correctly integrates the separate API-wide `Idempotency-Key` authority: identical parameters with the same key replay the original result, changed parameters produce 409, retention is at least 24 hours, and an HTTP 500 result may be cached. It then correctly distinguishes replay from freshness: the endpoint does not define no-key, different-key, expired-key, concurrent-call, snapshot-refresh, or search-specific cached-error recovery behavior.

The raw response schema supplies returned metric configuration fields, but does not define whether matches reflect ingest-time, search-time, or another configuration snapshot. The source and concepts preserve that boundary, the absent-versus-empty match ambiguity, reflow/archive/duplicate uncertainty, and the internal `not_in_values` empty-versus-nonempty wording conflict. No material contradiction was suppressed.

**Verdict: PASS.**

### SE-N1 — exact raw deep-dive and navigation

**Query:** Can a reader reach the exact Search Events snapshot and the separate idempotency authority without conflating them?

**Answer:** Yes. The canonical URL, raw file entry, path-qualified backlink, and raw SHA all match. The page is byte-identical to the approved attempt-2 candidate. Its Related section links the exact event-ingestion, billable-metric, and idempotency contexts and links the separate canonical idempotency source for the cross-source POST replay contract.

**Verdict: PASS.**

## 3. get-subscription-quantity-history

### Evidence identity and promotion

- Canonical source: `wiki/sources/metronome/source-metronome-api-reference-contracts-get-subscription-quantity-history.md`
- Raw source: `raw/metronome/api-reference/contracts/get-subscription-quantity-history-2026-07-13.md`
- Raw SHA-256: `cddb9b26136f83c02562f3634edd94dce4c029e5fd0128b256cd6319bd23b543` — match
- Approved attempt-2 candidate equality: exact byte match
- Canonical URL: `https://docs.metronome.com/api-reference/contracts/get-subscription-quantity-history.md` — exact
- Raw frontmatter entry and backlink: exact
- Company entry: exactly one
- Provider-index entry: exactly one
- Fact-bearing reciprocal concept: `wiki/concepts/metronome/metronome-subscriptions.md` cites the source and preserves the historical-versus-future quantity boundary.
- `[[metronome-customers-and-contracts]]` is contextual navigation rather than a concept receiving a new durable fact from this endpoint, so no reciprocal citation is required.

### SQ-F1 — factual retrieval

**Query:** What identifiers are required and what history structure does the endpoint return?

**Answer supported by source and raw:** Bearer-authenticated `POST /v1/contracts/getSubscriptionQuantityHistory` defines an OpenAPI `requestBody` without marking the body itself required. Within its JSON object schema, UUID `customer_id`, `contract_id`, and `subscription_id` are required. HTTP 200 requires top-level `data`, which references `SubscriptionQuantityHistory`; its `subscription_id`, `fiat_credit_type_id`, and `history` properties are optional. Each history entry requires RFC 3339 `starting_at` and `data`, and every nested data item requires numeric `quantity`, `unit_price`, and `total`.

The source correctly records the HTTP 400 error schema and its three listed codes: `ContractNotFound`, `CustomerNotFound`, and `SubscriptionNotFound`.

**Verdict: PASS.**

### SQ-B1 — boundary and contradiction handling

**Query:** Can this endpoint supply future scheduled seat changes or be treated as an ordered, exhaustive monetary ledger?

**Answer supported by source, raw, and concept context:** No. The raw page explicitly excludes future changes and directs readers to `getContract` for scheduled future quantity state. The canonical source preserves that distinction. It also correctly avoids claiming sort order, an ending timestamp, pagination, retention, exhaustive history, duplicate semantics, or the relationship among multiple data items at one effective date.

The response schema does not define the monetary unit, scale, or currency meaning of `unit_price` and `total`, and it does not guarantee that total always equals quantity multiplied by unit price. The source preserves these unknowns and does not infer chronological ordering from the example. No contradiction was found with the subscription concept.

**Verdict: PASS.**

### SQ-N1 — exact raw deep-dive and navigation

**Query:** Can a reader navigate to the exact quantity-history snapshot and then to the proper future-state context?

**Answer:** Yes. The exact URL, raw file entry, path-qualified raw backlink, and SHA-256 all match the trusted Campaign job. The canonical page is byte-identical to the attempt-2 candidate. It links `[[metronome-subscriptions]]` for lifecycle context and identifies `getContract` as the future-state route without inventing a nonexistent source-page link.

**Verdict: PASS.**

## Expansion decision

No query was partial or failed. All sampled facts remained grounded, all material limitations and contradictions were preserved, and all required mechanical relationships passed. Therefore:

- `expansion_required: false`
- Pages audited: 3
- Queries completed: 9
- Additional Campaign 19 pages audited: 0
- `closure_approved: true`

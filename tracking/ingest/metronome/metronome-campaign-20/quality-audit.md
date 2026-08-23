# Metronome Campaign 20 close quality audit

- Audit date: 2026-08-23
- Auditor role: independent, repository-read-only Sol audit
- Fixed sample: `get-a-customer`, `list-balances`, `create-a-credit`
- `closure_approved`: **true**
- `expansion_required`: **false**

## Verdict

The fixed three-page sample passes the Campaign 20 close quality gate. Each sampled source supports efficient factual retrieval, preserves the important uncertainty or contradiction boundaries found in the complete raw page, and provides a path-qualified backlink for exact raw deep-dives. No sampled result was materially partial or incorrect, so the immutable expansion rule does not require a full five-page semantic audit.

This approval is a content-and-link audit verdict, not a throughput verdict. The campaign needed multiple attempts before approval, so its first-pass performance remains a separate negative result.

## Mechanical integrity

For all five Campaign 20 jobs, including the two pages outside the semantic sample:

- The current raw SHA-256 equals the immutable manifest SHA.
- The canonical source is byte-for-byte equal to the final reviewer-approved candidate.
- `canonical_url` exactly matches the manifest.
- `raw_files` points to the assigned raw page.
- The `## Raw Sources` link is path-qualified, omits only the `.md` extension as required by the wiki convention, and resolves to the assigned immutable raw file.
- The company page contains the source wikilink exactly once.
- The Metronome provider index contains the source wikilink exactly once.
- Every reviewer-approved fact-bearing concept block and reciprocal source-link block occurs exactly once in its target concept.

Targeted validation of the five sources, eleven touched Metronome concepts, and the company page passed: `validate_wiki: OK (17 file(s) checked, no issues)`. The provider index was checked directly for exactly-once entries because index pages intentionally do not use source-page YAML frontmatter.

## Query-quality sample

### 1. Get a customer — standard API read

**Factual retrieval: pass.** The source accurately retrieves the required UUID path identifier, required `data` envelope, required `CustomerDetail` fields, deprecated `external_id`, usage-event `ingest_aliases`, nullable archive timestamp, open string-valued custom-field map, and configuration-dependent billable-status shape.

**Boundary and contradiction retrieval: pass.** It keeps customer detail separate from customer billing-provider configuration, distinguishes required nullable `salesforce_account_id` from the surrounding customer configuration, and does not invent not-found, freshness, archived-customer visibility, alias lifecycle, or billable-status transition behavior. No unresolved contradiction with the existing creation, provisioning, custom-field, or event-ingestion summaries was found.

**Exact raw deep-dive: pass.** The canonical URL, frontmatter raw path, and path-qualified raw backlink all resolve to the trusted customer raw page. Reciprocal durable-fact and source links are present in customers-and-contracts, custom-fields, and event-ingestion.

### 2. List balances — long/schema-heavy API list

**Factual retrieval: pass.** The source accurately captures the JSON payload's required `customer_id`, optional filters and expansion flags, endpoint-specific body cursor, 1-25 limit with default 25, required `data` plus nullable `next_page` response, Commit/Credit union, schedule and denomination limits, calculated-balance floor, custom-field maps, and ledger families.

**Boundary and contradiction retrieval: pass.** It prominently preserves four query-critical differences instead of flattening them: body pagination versus the API-wide query-parameter convention and general 100 cap; archive lifecycle versus the endpoint's repeated-credit wording and Commit/Credit schema asymmetry; signed ledger sum versus the non-negative calculated-balance exception; and uppercase/expanded OpenAPI ledger enums versus lowercase or differently named guide values. It also leaves freshness, cursor consistency, archive visibility, denomination, and replay freshness unknown where the documentation is silent.

**Exact raw deep-dive: pass.** The canonical URL, raw path, and path-qualified raw backlink resolve to the trusted 1,464-line raw page. The fact-bearing reciprocal updates are present in credits-and-commits, customers-and-contracts, currencies-and-custom-pricing-units, and custom-fields. The related idempotency link in the source is contextual: the durable `Idempotency-Key` guarantee is owned by the separate API-wide authority, so this page does not need a duplicate fact-bearing concept citation merely for being a POST read.

### 3. Create a credit — ordinary API mutation

**Factual retrieval: pass.** The source accurately distinguishes the request-body wrapper from the payload's required fields, captures the access-schedule requirements and USD-cent default, contract scope, product and specifier filters, lower-number priority, equal-priority contract-level precedence, success ID, generic 400/404 errors, and the separate uniqueness-key 409 behavior.

**Boundary and contradiction retrieval: pass.** It preserves the unresolved all-products-versus-specifiers wording, the exact `any` exclusion-entry versus `all` tags-within-one-entry semantics, the difference between endpoint priority prose and the broader ordering guide, and the separation between resource `uniqueness_key` and API-wide `Idempotency-Key`. It does not infer amount constraints, schedule cardinality, lifecycle transitions, balance visibility, downstream invoice/accounting propagation, concurrency, or recovery behavior. Its OpenAPI 3.0.1 nullability statements are limited to the schema boundary and leave endpoint error mapping unknown.

**Exact raw deep-dive: pass.** The canonical URL, raw path, and path-qualified raw backlink resolve to the trusted mutation raw page. Fact-bearing reciprocal updates are present in credits-and-commits, API idempotency, products and rate cards, currencies and custom pricing units, custom fields, and invoicing.

## Archetype annotation and retry-defect attribution

This section annotates the five jobs from their manifest and recorded review history. It does not change routing, prompts, rules, or state.

| Job | Read-only archetype | Earlier retry defects | Checklist implication |
| --- | --- | --- | --- |
| `get-a-customer` | API Read | OpenAPI nullability overstatement; evidence excerpts did not cover the required envelope and response fields; required custom-field semantics were blurred; concept insertion anchor was stale | API Read checks should cover path identity, success envelope, optional/nullable response fields, archive visibility, response-map limits, and exact existing-concept anchors. |
| `list-all-billable-metrics` | API List/schema | A GET page with no defined `requestBody` was overstated as proving no-body behavior; custom-field concept coverage was missed; quotes did not directly ground pagination, required fields, or the aggregation-key/example conflict | API List checks should separate absence of a request schema from runtime rejection, audit pagination/default/order boundaries, compare examples against schema, and inspect reusable response maps such as custom fields. |
| `list-balances` | API List/schema-heavy | Response-envelope shape and endpoint-specific pagination were initially flattened; archive asymmetry, ledger enum conflicts, currency boundaries, and custom-field coverage were missed; later evidence excerpts still did not prove optionality or full schema absence claims | Schema-heavy List checks need union/envelope mapping, endpoint-versus-global convention comparison, complete required/property boundaries, lifecycle visibility, enum comparison across authorities, and evidence for absence claims. |
| `create-a-credit` | API Mutation | Product-selector ambiguity was synthesized away; exclusion `any`/`all` logic was misstated; uniqueness-key release wording lost the Alerts-only boundary; quotes omitted nested schemas and errors; OpenAPI nullability was later overstated as unknown | Mutation checks should separate wrapper and payload requiredness, trace nested selectors and errors, distinguish resource uniqueness from request replay, enumerate lifecycle/propagation unknowns, and apply OpenAPI nullability precisely. |
| `set-up-account-level-billing-provider` | Integration Setup + Mutation | Evidence excerpts did not directly cover bearer security, provider/delivery enums, required payload fields, open-ended configuration, secret-bearing cloud examples, success ID, or generic 400/409 errors | Integration Setup checks should cover supported-provider enums, secret-bearing configuration examples, open-object boundaries, returned configuration identity, API-wide idempotency versus provider-side effects, and downstream readiness/reconciliation unknowns. |

The retry history aligns strongly with future archetype-aware checklist needs: most failures cluster around page-shape-specific schema traversal, contradiction surfaces, evidence coverage, and concept placement. The history also shows that archetype hints alone would not replace independent semantic review: selector ambiguity, ledger-name contradictions, archive lifecycle interactions, and provider-side propagation require cross-source judgment rather than format checks.

## Close recommendation

Approve Campaign 20 content closure after the coordinator's normal campaign-close validators and state transition. Do not expand this quality audit to all five pages. Record the first-pass and retry counts separately when deciding whether the Campaign 20 preflight changes improved throughput.

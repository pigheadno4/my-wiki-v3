# Metronome Campaign 21 Close Quality Audit

- `closure_approved: true`
- `expansion_required: false`
- Fixed semantic sample: `list-customers`, `get-an-invoice`, `how-invoicing-works`
- Expanded sample: none
- Audit mode: independent repository-read-only review

## Verdict

The five promoted source pages are mechanically intact, and all three fixed-sample pages pass factual retrieval, boundary or contradiction retrieval, and exact raw deep-dive navigation. No sampled query is partial or failed, so the manifest's expansion rule does not authorize reviewing the other two pages semantically.

Campaign 21 may close as a content-quality pass, but it does **not** pass its archetype-throughput pilot criteria. The playbook gave reviewers a useful defect taxonomy and kept review attention on query-critical boundaries, but it did not improve first-pass worker accuracy: first-pass approval was `0/5`, four jobs required a full semantic retry, and three of those then needed a bounded evidence-only third attempt.

## Fixed semantic sample

### `list-customers` — pass

- **Factual retrieval:** The source correctly routes to bearer-authenticated `GET /v1/customers`, identifies all six optional query filters, preserves the 1–100 page limit, and distinguishes the required `data` array and nullable `next_page` envelope. It correctly preserves required customer identity, alias, configuration, timestamp, and custom-field fields plus the optional archived and configuration-dependent billable-status fields.
- **Boundary retrieval:** The source explicitly leaves combined-filter behavior, ordering, default page size, cursor lifetime, snapshot consistency, freshness, errors, and read-after-write behavior undocumented. It also preserves the prose-only `customer_ids` limit versus schema-level `salesforce_account_ids.maxItems` asymmetry without converting it into a contradiction.
- **Shared concepts:** Customer, event-ingestion, and custom-field concept pages preserve the durable facts and contain reciprocal source links. The source links back to each fact-bearing concept.
- **Raw deep-dive:** Frontmatter points to exactly `metronome/api-reference/customers/list-customers-2026-07-13.md`, and `## Raw Sources` contains the exact path-qualified backlink to the immutable raw snapshot.

### `get-an-invoice` — pass

- **Factual retrieval:** The source correctly retrieves the customer-scoped GET path, required UUID identifiers, optional zero-quantity filter, required `data` envelope, required invoice and line-item fields, applied-credit or commit representation, custom-pricing-unit conversion line, hierarchy attribution, and optional downstream billing and revenue-system records.
- **Boundary and contradiction retrieval:** It preserves the undocumented `include_list_prices` parameter reference, the narrative `amount_due` versus absent schema field, non-enum invoice status and type examples, optional versus prose-conditionally-required hierarchy fields, unresolved `billable_status` shape, generic-only 404 contract, and downstream outcome limits. Most importantly, it preserves uppercase `VOID` from the read surface alongside lowercase `voided` from the void-operation authority without inventing normalization.
- **Shared concepts:** Invoicing, credits and commits, custom pricing units, integrations, and custom-fields pages contain the approved durable facts and reciprocal source links. The source links back to all five concepts.
- **Raw deep-dive:** Frontmatter and `## Raw Sources` resolve exactly to `raw/metronome/api-reference/invoices/get-an-invoice-2026-07-13.md`.

### `how-invoicing-works` — pass

- **Factual retrieval:** The source correctly distinguishes contract-generated usage and scheduled invoices, usage grace-period behavior, scheduled finalization windows, draft/finalized/void lifecycle, credit and commit application, and pricing-versus-presentation grouping.
- **Boundary and contradiction retrieval:** It does not turn “real time” into an SLA, does not extend Metronome finalization into delivery, payment, tax, or accounting proof, and preserves the guide's schema prose (`billing_period_*`, `issue_date`) versus worked payload (`start_timestamp`, `end_timestamp`, `issued_at`) conflict. It also preserves the example's negative commitment line without quantity or unit price despite the guide's universal line-item wording.
- **Shared concepts:** Invoicing, customers and contracts, products and rate cards, credits and commits, usage-based billing, and billable-metrics pages contain the approved durable facts and reciprocal source links. The source links back to all six concepts.
- **Raw deep-dive:** Frontmatter and `## Raw Sources` resolve exactly to `raw/metronome/guides/implement-metronome/core-concepts/how-invoicing-works-2026-07-13.md`.

## All-five mechanical and reciprocal-link audit

All five jobs pass every required invariant:

| Job | Raw SHA | Canonical = final candidate | Canonical URL | `raw_files` | Exact raw backlink | Company exactly once | Index exactly once | Fact-bearing reciprocal links |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `get-an-invoice` | pass | pass | pass | pass | pass | pass | pass | pass, 5/5 concept targets |
| `list-customers` | pass | pass | pass | pass | pass | pass | pass | pass, 3/3 concept targets |
| `update-a-customer-name` | pass | pass | pass | pass | pass | pass | pass | pass, 4/4 concept targets |
| `how-invoicing-works` | pass | pass | pass | pass | pass | pass | pass | pass, 6/6 concept targets |
| `aws-marketplace-integration` | pass | pass | pass | pass | pass | pass | pass | pass, 7/7 concept targets |

The raw hashes match the immutable manifest values. Each canonical source is byte-identical to its final reviewer-approved candidate. Each approved durable-fact concept target links to the source, and each source links back to every such concept target.

Catalog counts are internally consistent: `225` canonical raw pages, `127` source summaries, and `104` raw pages without source summaries.

## Archetype playbook outcome

### Final content quality

Pass. The fixed sample returns accurate source-level facts, preserves query-critical unknowns and contradictions, and provides exact raw navigation. Mechanical coverage passes across all five pages.

### Reviewer guidance and defect attribution

Useful. Review defects map cleanly to the playbook's information classes:

- API List / Schema: shared-fact quote coverage was incomplete even though the candidate semantics were correct.
- API Read: cross-authority status casing, schema scope, hierarchy, downstream-record, and custom-field grounding needed correction.
- API Mutation: the worker over-attributed the 160-character truncation rule to a read authority that did not establish it.
- Concept / Guide: scheduled timing wording, lifecycle evidence, schema-versus-example evidence, and two missed fact-bearing concept placements required correction.
- Integration Guide: fixed-term versus customer-controlled listing lifecycle and freely chosen contract-dimension identifiers versus mandatory `usage_fee` were initially compressed incorrectly.

This indicates that the playbook helped reviewers name defects consistently. It did not prevent those defects at worker handoff.

### First-pass approval and retries

- First-pass approval: `0/5`, below the required `4/5`.
- Total worker attempts: `13` for five pages.
- Full reviews: `9`; targeted reviews: `4`.
- Full semantic retry cycles: `4` (`update-a-customer-name`, `get-an-invoice`, `how-invoicing-works`, and `aws-marketplace-integration`), above the pilot limit of one.
- Bounded evidence-only retry cycles: `4` (`list-customers` attempt 2 plus attempt 3 for the three jobs that needed quote-only follow-up).

### Elapsed throughput

The campaign started at `2026-08-24T14:08:31Z`; the last reviewer approval was recorded at approximately `2026-08-24T14:52:40Z`, an elapsed review-path time of about `44m 09s`. This exceeds the playbook's desirable `35m` target by about nine minutes, before final close-audit work. The event ledger has no per-event timestamps and `completed_at` is not yet set, so this uses the campaign start plus the final review file timestamp and should not be presented as a fully instrumented end-to-end metric.

## Pilot decision

- Content closure: **approved**.
- Query-audit expansion: **not required**.
- Archetype pilot success: **failed on first-pass accuracy, retry count, and desired throughput**.
- Production implication: keep the campaign-local playbook as useful review guidance/evidence, but do not promote it as a proven provider-rule throughput optimization or use Campaign 21 to authorize cross-provider rollout.
- No registry, new schema, new reviewer layer, or other framework is recommended from this result.

## Validation evidence

- `validate_wiki.py`: pass for the five sources, all touched concepts, and the Metronome company page (`18` files).
- `validate_metronome_capsule.py`: pass (`225` raw, `127` sources, `104` pending).
- `git diff --check`: pass.

# Metronome Campaign 16 query-quality audit

- Audit date: 2026-08-19
- Manifest: `tracking/ingest/metronome/metronome-campaign-16/manifest.json`
- Audited pages: all five manifest jobs
- `overall_decision`: **pass**
- `expansion_triggered`: **true**
- `expansion_completed`: **true**
- `expansion_required`: **false**
- `closure_approved`: **true**
- Material open defects: **none**

The initial three-page sample found one material retrieval omission in `provision-your-customer`. The coordinator applied one bounded semantic repair, independently rechecked below. Because the initial result required expansion, this audit then completed the same three-query review for `prepaid-credits` and `get-commit-and-usage-analytics`. No additional defect was found.

## Bounded provision repair recheck

### Exact grounding

Raw lines 11–15 introduce the three subscription configurations. Line 13 states that a standard subscription charges a recurring fee each billing period and that all usage is either included or paid for separately in arrears. The repair preserves that exact distinction:

- Canonical source line 18 adds it to the three-model key takeaway.
- Canonical source line 26 repeats it in the standard-provisioning section.
- `wiki/concepts/metronome/metronome-subscriptions.md:12` preserves all three models: standard included-or-separate-arrears usage, pooled balance with contract-level overages, and individual-seat balance with contract-level overages.

The two canonical-source changes are the only diff from the approved attempt-2 candidate and accurately restate raw line 13 without expanding its scope. Therefore the canonical source now equals the **approved attempt-2 candidate plus one independently rechecked coordinator repair**; it is intentionally not byte-equal to the candidate. Candidate SHA-256 is `de16a9960fd6681b00bf1742829ad78577718df781533a9871c62ef60ee9a184`; repaired canonical SHA-256 is `e31b6214bd155306cbe9ee726ff1dbe8b080eb24685eb70866667047f1981b42`.

### Targeted rerun

1. **Retrieval — pass after repair.** Query: “What are Metronome’s three subscription configurations, and how is usage or overage handled in each?” The repaired source and concept now answer the standard, pooled, and individual-seat cases completely.
2. **Affected link integrity — pass.** The repaired source links `[[metronome-subscriptions]]` exactly once, and the concept links `[[source-metronome-guides-pricing-packaging-subscription-provision-your-customer]]` exactly once. No affected link was removed or duplicated.

The other two provision queries and the eight other previously passing sampled queries were not rerun.

## Integrity, promotion, backlink, and reciprocity

| Job | Raw SHA-256 | Final candidate and canonical status | Exact raw backlink | Required concept reciprocity |
| --- | --- | --- | --- | --- |
| `prioritization-rules` | **pass** — `6a7de2bdaf54f399f84bf92c5d659609cf66200435c9b8afdeb42388bc770dae` equals manifest | **pass** — approved attempt 1 candidate and canonical are byte-equal (`b1ef00db7a3878284568d907af90d55aae26be5cd0eab9c5b14ed233c5ae4827`) | **pass** — canonical lines 7–8 and 51–53 identify the exact nested raw | **pass** — credits/commits and invoicing are bidirectional exactly once |
| `model-hierarchical-customer-relationships` | **pass** — `68e9ad571f34795094ed9df13c150e429ec363c0c6ff7adcff36e74e7faeb58b` equals manifest | **pass** — approved attempt 2 candidate and canonical are byte-equal (`812a90b954004de0979d4abb0fdf52acea49b85708dae3917df51801c688e149`) | **pass** — canonical lines 7–8 and 72–74 identify the exact nested raw | **pass** — customers/contracts, credits/commits, invoicing, alerts, reporting, and currencies are bidirectional exactly once |
| `provision-your-customer` | **pass** — `f15e1af11efebe9b9c75fa84c5dc40b23afe57eeb286d7194f00d13d79553555` equals manifest and was unchanged | **pass with bounded repair** — approved attempt-2 candidate plus the independently rechecked raw-line-13 repair; not byte-equal by design | **pass** — the existing exact nested raw backlink remains at canonical lines 65–67 | **pass** — subscriptions, credits/commits, and invoicing remain bidirectional exactly once; affected subscriptions link checked directly |
| `prepaid-credits` | **pass** — `b3f5763c3a6c2c07c7cf553447d914a86be2e654184c1c9d05b3913b4f21e523` equals manifest | **pass** — final attempt-2 targeted review is approved; receipt, candidate, and canonical are byte-equal (`4b36182b1c8c4e812fd13591b2a00050974c38fbbabc459933ee453a6a6c0637`) | **pass** — canonical lines 63–65 identify the exact nested raw | **pass** — credits/commits and alerts cite the source exactly once at concept lines 146 and 58; the source links both targets |
| `get-commit-and-usage-analytics` | **pass** — `ce5a5ad4b54fdf845be5ddca609332df4b9c37093725597819a19733c837f211` equals manifest | **pass** — final attempt-2 full review is approved; receipt, candidate, and canonical are byte-equal (`a61445cf198da2b7699d3a8b6e942ad9cb460af0bdb678c383a2deb2ea55094d`) | **pass** — canonical lines 79–81 identify the exact nested raw | **pass** — reporting/analytics and credits/commits cite the source exactly once at concept lines 71 and 148; the source links both targets |

## Query results

### `prioritization-rules`

1. **Retrieval — pass.** “Which credit or commit burns down first, and which eligible invoice line receives it first?” The source gives the rollover/prepaid/postpaid order, documented rollover and prepaid tie-breakers, and the independent invoice-line order (lines 18–36).
2. **Boundary/contradiction completeness — pass.** “Can priority move postpaid ahead of prepaid, and is usage applicability definitely a postpaid tie-breaker?” The source preserves type precedence, the rollover exception, and the unresolved omission from the abbreviated postpaid list (lines 26–32 and 40–43).
3. **Raw-backlink deep dive — pass.** The path-qualified backlink at lines 51–53 opens the exact immutable raw whose hash matches the manifest.

Page total: **3 pass / 0 partial / 0 fail**.

### `model-hierarchical-customer-relationships`

1. **Retrieval — pass.** “How do I model shared parent commitments and parent-paid consolidated invoices?” The source covers separate customers/contracts, `all`/`none`/`contract_ids` child access, self-paid overages, parent `CONCATENATE`, child `PARENT` plus `CONSOLIDATE`, inclusion conditions, and origin attribution (lines 20–50).
2. **Boundary/contradiction completeness — pass.** “What hierarchy limits, alert/reporting caveats, unsupported behavior, and monetary conflicts must I account for?” The source preserves lifecycle and consolidation unknowns, Stripe-only support, delayed parent-alert evaluation, the truncated spend-alert sentence, dashboard scope, and the dollar-label versus USD-cent contradictions (lines 30–64).
3. **Raw-backlink deep dive — pass.** The path-qualified backlink at lines 72–74 opens the exact immutable raw whose hash matches the manifest.

Page total: **3 pass / 0 partial / 0 fail**.

### `provision-your-customer`

1. **Retrieval — pass after bounded repair.** “What are Metronome’s three subscription configurations, and how is usage or overage handled in each?” Canonical lines 18 and 26 and subscriptions-concept line 12 now preserve the raw line-13 standard-model boundary alongside the two credit models.
2. **Boundary/contradiction completeness — pass (retained).** “What must individual-seat credits configure, and which field, support-limit, charging, and invoice-routing caveats remain?” The source covers the charging gate, terminology boundary, advance-only anchor, conditional provider routing, stable seat identity, 1,000-seat support boundary, `SEAT_BASED`, field-name contradiction, and lifecycle unknowns.
3. **Raw-backlink deep dive — pass (retained).** The exact nested raw backlink remains at canonical lines 65–67.

Page total: **3 pass / 0 partial / 0 fail**.

### `prepaid-credits`

1. **Retrieval — pass.** “How does the Stripe-backed prepaid-credit flow grant balance, enforce access, recharge, and show balance?” The source correctly separates Metronome’s payment-gated `add_commits`, alert, recharge, and balance-view roles from the merchant-owned entitlement flag and request denial (lines 14–42). It preserves success/failure wording as documentation evidence rather than silently normalizing it.
2. **Boundary/contradiction completeness — pass.** “Which examples and runtime assumptions must not be copied directly?” The source flags the reversed access interval, three conflicting threshold-configuration keys, commit-versus-invoice failure-state conflict, undefined amount units, staging endpoint, webhook/access timing limits, idempotency and concurrency unknowns, and Stripe-specific evidence boundary (lines 40–55). Both fact-bearing concepts preserve the merchant-enforcement and zero-alert boundaries.
3. **Raw-backlink deep dive — pass.** “Where can I inspect the exact purchase, alert, recharge, and balance examples?” The path-qualified backlink at lines 63–65 opens the exact immutable raw whose hash matches the manifest.

Page total: **3 pass / 0 partial / 0 fail**.

### `get-commit-and-usage-analytics`

1. **Retrieval — pass.** “How should a GTM dashboard compare expected commit pacing with actual burn and turn the result into outreach?” The source preserves access-schedule pacing, commit-attributed finalized/current-period consumption, date-spine and cumulative-burn modeling, merchant-selected forecasts, and illustrative over/on/under-consumption actions (lines 20–58).
2. **Boundary/contradiction completeness — pass.** “Can the published SQL be run as a coherent export query, and what prevents misclassification or overcounting?” The source explicitly preserves the alias defects, unresolved base-versus-breakdown table families, table-specific grain/cadence, snapshot selection, independent object-storage deduplication, null-commit on-demand-versus-overage contradiction, and heuristic-not-enforcement boundary (lines 20–71). Both fact-bearing concepts carry the table-grain and null-attribution cautions with reciprocal citations.
3. **Raw-backlink deep dive — pass.** “Where can I inspect the exact SQL placeholders, joins, fields, and playbook bands?” The path-qualified backlink at lines 79–81 opens the exact immutable raw whose hash matches the manifest.

Page total: **3 pass / 0 partial / 0 fail**.

## Mechanical campaign-wide checks

Each manifest source exists exactly once in both `wiki/companies/metronome.md` and `wiki/metronome-index.md`:

- `prioritization-rules`
- `prepaid-credits`
- `provision-your-customer`
- `get-commit-and-usage-analytics`
- `model-hierarchical-customer-relationships`

Required counts remain present:

- Company frontmatter: `source_count: 102` at `wiki/companies/metronome.md:5`.
- Company knowledge status: `102` ingested / `129` raw without summaries at `wiki/companies/metronome.md:154-155`.
- Provider index coverage: `102` ingested / `129` raw without summaries at `wiki/metronome-index.md:15-16`.

## Final totals and closure

- Audited pages: **5 / 5**
- Queries: **15 pass / 0 partial / 0 fail**
- Page outcomes: **5 pass / 0 partial / 0 fail**
- Bounded repairs independently rechecked: **1 pass**
- Material open defects: **0**
- `overall_decision`: **pass**
- `expansion_required`: **false** — the required expansion is complete
- `closure_approved`: **true**

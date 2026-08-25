# Metronome Campaign 22 Independent Close Quality Audit

Date: 2026-08-25  
Scope: `metronome-campaign-22` only  
Repository posture: read-only; this report is the only audit output  

## Verdict

```yaml
closure_approved: true
expansion_required: false
mechanical_verdict: pass
semantic_sample_verdict: pass
material_defects: []
```

Campaign 22's five promoted source pages and approved shared concept updates satisfy the campaign-close quality gates audited here. All fixed-sample semantic queries passed, so the rule requiring expansion on any material partial or fail was not triggered. This is a quality-audit approval to close; the campaign state and monitor still say `active` / `incomplete`, so the coordinator must perform the normal terminal state update separately.

The provider index's missing frontmatter is the established Metronome provider-index convention and is not treated as a Campaign 22 defect.

## Evidence read

The audit read the complete governing `CLAUDE.md`, `rules/ingest.md`, and `rules/psp/metronome.md`; the complete Campaign 22 manifest, selection review, archetype playbook, jobs, monitor, campaign state, and event ledger; and every final approved attempt's input, candidate, receipt, review, and suggestions. It also checked the current promoted sources, affected shared concepts, company page, and Metronome index.

For the immutable semantic sample, the audit read each assigned raw source completely:

- `archive-a-customer`
- `list-products`
- `non-monotonically-increasing-metrics`

The remaining two jobs were mechanically audited and their final approved artifacts were read, but their raws were not added to the semantic sample because no fixed-sample query was partial or failed.

## Mechanical audit

All five jobs passed every required job-level check.

| Check | Passed | Total |
| --- | ---: | ---: |
| Trusted raw SHA-256 equals current raw bytes | 5 | 5 |
| Promoted canonical source is byte-equal to final approved candidate | 5 | 5 |
| Candidate equals terminal receipt `source_page` | 5 | 5 |
| Suggestions equal terminal receipt `suggestions` | 5 | 5 |
| Exact manifest `canonical_url` in source frontmatter | 5 | 5 |
| Exact nested manifest raw path in `raw_files` | 5 | 5 |
| Exact path-qualified assigned-raw backlink, exactly once | 5 | 5 |
| Campaign source entry exactly once on company page | 5 | 5 |
| Campaign source entry exactly once on Metronome index | 5 | 5 |

Catalog entry total: **10/10** exact-once campaign entries across company plus provider index.

All terminal-review-approved concept blocks were then checked as exact multi-line strings in their declared canonical targets:

| Shared update class | Passed exactly once | Total |
| --- | ---: | ---: |
| Durable fact blocks | 29 | 29 |
| Reciprocal fact-bearing source links | 28 | 28 |
| All approved concept blocks | 57 | 57 |

No approved block is missing or duplicated. Every approved source-to-concept relationship has its fact-bearing reciprocal source link. The company `source_count` and provider-index source-summary coverage both remain `132`, matching the 132 canonical Metronome source-summary files; the five Campaign 22 additions are individually present exactly once in both reverse catalogs.

## Fixed semantic query audit

Query total: **9/9 pass**.  
Factual retrieval: **3/3 pass**.  
Boundary or contradiction retrieval: **3/3 pass**.  
Exact raw deep dive: **3/3 pass**.  
Partial: **0**. Fail: **0**.

| Job | Query family | Audit query | Result | Finding |
| --- | --- | --- | --- | --- |
| `archive-a-customer` | Factual retrieval | What does customer archival do to the customer, contracts, invoices, aliases, and notifications? | Pass | The source retrieves irreversible archival, API/UI audit visibility, current-date archival of all contracts, voiding of corresponding invoices, alias reservation/reuse prerequisite, and suppression of associated notification triggers. |
| `archive-a-customer` | Boundary / contradiction | Does success prove downstream invoice cancellation, webhook recall, fresh state on retry, or a contract-archive-style invoice-state partition? | Pass | The source keeps the customer-archive authority separate from contract archival, downstream invoice correction, notification delivery, and API-wide idempotency. It explicitly leaves downstream Stripe/ERP/marketplace, already-generated or in-flight notification work, transactionality, retry recovery, and side-effect completion details unknown. |
| `archive-a-customer` | Exact raw deep dive | Where are request/body requiredness, identity format, success/error envelopes, authentication, and immutable evidence? | Pass | The source distinguishes the unmarked enclosing `requestBody` from required UUID `id`, retains bearer/production-server evidence, lists required `data.id` on 200 plus 400/404 string-message errors, and links exactly once to the assigned path-qualified raw snapshot. |
| `list-products` | Factual retrieval | How do archive filtering, pagination, product identity, state, history, and configuration work? | Pass | The source retrieves default archived-product exclusion, the three archive-filter values, optional 1-100 limit and cursor, required `data`/nullable `next_page`, required item/state/update surfaces, complete-version-history wording, composite fields, quantity conversion/rounding, custom fields, NetSuite IDs, and compound metric-group-key requirements. |
| `list-products` | Boundary / contradiction | What should not be inferred about nulls, ordering, cursor consistency, history semantics, product types, integration readiness, or idempotent freshness? | Pass | The source preserves non-null OpenAPI object/string schemas while leaving runtime error mapping unknown; explicitly leaves ordering, cursor lifetime, snapshot consistency, update chronology/inheritance, and read-after-write unspecified; flags `PRO_SERVICE` versus the four-type guide; and prevents NetSuite field presence or same-key replay from becoming readiness or freshness claims. |
| `list-products` | Exact raw deep dive | Can a reader reach the exact list schema and verify filters, pagination, required fields, enum values, and optional configuration? | Pass | The path-qualified raw backlink is exact and singular. The promoted source preserves the operation/body/query separation and the schema details needed to route a field-level investigation back to the complete immutable raw. |
| `non-monotonically-increasing-metrics` | Factual retrieval | How are falling `LATEST` values billed, covered, rated, and exposed by invoice-breakdown versus usage queries? | Pass | The source retrieves incremental billing, negative quantities/credits, effective-window commit and credit coverage, current-rate pricing after a rate change, chronological no-look-ahead credit application, and incremental invoice-breakdown versus absolute latest usage-query semantics. |
| `non-monotonically-increasing-metrics` | Boundary / contradiction | What happens to a negative invoice total, and does full-period coverage reliably prevent one? | Pass | The source preserves downstream finalization, refund, tax, payment, settlement, accounting, and reconciliation unknowns. It explicitly records the raw's unresolved conflict: the full-period-credit example yields `-$20`, while the later recommendation says full-period coverage avoids unexpected negative totals. |
| `non-monotonically-increasing-metrics` | Exact raw deep dive | Can a reader verify the numerical examples and distinguish factual raw from navigation-only API references? | Pass | The assigned guide is linked once with a path-qualified raw backlink; the `7 -> 9 -> 10 -> 5`, rate-change, `-$40`, and `-$20` examples are retained. The invoice-breakdown and usage API raws are correctly labeled navigation-only and are not used as factual evidence for endpoint schemas. |

The three sampled sources are query-useful semantic indexes: they retain the important facts, source-scoped contradictions, implementation boundaries, authority links, and exact immutable raw route without pretending to transcribe every field.

## Archetype v2 quality and throughput assessment

Final quality passed, but archetype v2 did **not** demonstrate the intended first-pass quality or retry improvement.

Ledger:

- Attempt-1 approvals: **0/5**; the pilot target was at least **4/5**.
- Final attempts by job: **2 / 3 / 2 / 2 / 2**.
- Full semantic retry cycles: **5**; the pilot target was no more than **1**.
- Targeted retry cycles: **1**.
- Worker attempts: **11**.
- Reviews: **11** = **10 full + 1 targeted**.
- Coordinator repairs so far: **0**.
- Campaign state: still active; elapsed completion time is unavailable, so the approximately 35-minute desirability target cannot be honestly assessed.

Compared with Campaign 21, worker attempts fell from 13 to 11, a reduction of two attempts (about 15%). That limited reduction is real, and zero coordinator repairs is positive. It is not enough to claim throughput improvement: Campaign 22 still had 0/5 first-pass approvals, required five full semantic retry cycles versus Campaign 21's four, added one targeted retry, and has no terminal elapsed time. The playbook's claim-to-evidence, authority-separation, and concept-impact checks are visible in the final corrected pages, but the ledger shows that independent review and retries—not first-pass worker self-checks—were what achieved closure quality.

Conclusion: keep archetype v2 campaign-local. Final content quality supports Campaign 22 closure, but the pilot fails its own promotion criteria and does not justify weakening independent review, changing production routing, adding machinery, or rolling the playbook out across providers.

## Material defects and expansion decision

Material Campaign 22 defects found: **none**.

The fixed manifest sample produced no partial or fail across its nine required queries, and all five pages passed the complete mechanical audit. Therefore:

```yaml
closure_approved: true
expansion_required: false
```

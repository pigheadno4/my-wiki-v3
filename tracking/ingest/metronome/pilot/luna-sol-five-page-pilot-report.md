# Metronome GPT-5.6 Luna Five-Page Pilot Report

## Decision

**`scale_with_changes`**

GPT-5.6 Luna is suitable as a constrained raw-reading and evidence-drafting worker, but not as an autonomous ingestion or promotion authority. All five cases reached an approved result only after GPT-5.6 Sol review, and every final receipt is `approved_with_repairs`. Sol approval, concept ownership, contradiction review, shared-file updates, and final promotion must remain mandatory.

Before processing the remaining 220-page queue, implement cumulative retry accounting, claim-level evidence, targeted quote repair, page-type extraction, and a minimal worker runtime. Scale in bounded batches with independent sampling rather than launching the whole queue at once.

## Case Results

| Case | Raw lines | Luna attempts | Exact quotes | Final status | Sol repairs | Repair minutes |
| --- | ---: | ---: | ---: | --- | ---: | ---: |
| Invoicing overview | 31 | 2 | 5 | approved with repairs | 3 | 6 |
| Getting-started shadow | 140 | 2 | 5 | approved with repairs | 5 | 5 |
| Developer SDK walkthrough | 944 | 1 | 5 | approved with repairs | 5 | 18 |
| Data-export database reference | 1,600 | 1 | 4 | approved with repairs | 5 | 14 |
| Create-contract API reference | 4,561 | 1 | 4 | approved with repairs | 5 | 16 |
| **Total** | **7,276** | **7** | **23** | **5 accepted cases** | **23** | **59** |

The four production cases created four new canonical source pages, bringing the capsule to 5 ingested sources and 220 pending pages. The shadow case correctly left the existing baseline and shared coverage unchanged.

## Luna Reliability

- All five accepted outputs passed schema, identity, exact-quote, raw-link, and write-boundary validation.
- Two of five jobs required the single allowed retry. Both failures were exact-quote failures, but the invoicing attempt also contained unrelated fabricated invoice-state material before rereading the source.
- The shadow retry demonstrates a process flaw: attempt 1 was more complete but had one incorrect quote range; regenerating the whole output fixed the quote and degraded content coverage.
- Event streams from every page show premature schema-shaped or fabricated drafts before the model completed the raw read. The accepted final JSONs were grounded, but output-schema enforcement alone does not prevent this behavior.
- A small global quote set cannot validate every claim in long pages. The 4,561-line API case used four quotes, one of which was only a field name.
- Luna proposed overly granular concepts in both short-page cases. Taxonomy decisions must remain coordinator-owned.

## Sol Repairs

The 23 recorded repairs fall mainly into five recurring groups:

1. **Omissions:** lifecycle boundaries, event windows, effective-time rules, package restrictions, gated fields, and conditional requirements.
2. **Structure:** converting page-shaped drafts into query-oriented maps and separating overview material from exhaustive raw reference.
3. **Taxonomy:** consolidating short-page sub-concepts and mapping broad guides to the planned provider taxonomy.
4. **Wording:** narrowing compliance/beta/response-code claims to exactly what the source supports.
5. **Contradictions and examples:** preserving source-internal namespace, timestamp, response-list, and field-name mismatches without generalizing them into platform behavior.

The independent review found two SDK example inconsistencies missed by the initial Sol pass: a Node.js `V1` namespace mismatch and the Go metric snippet's missing `group_keys`. These are now recorded on the canonical SDK source. It also found that the create-contract receipt claimed a prose/schema naming mismatch was preserved when the source only used the schema name; the canonical source now states the mismatch explicitly.

## Cost and Timing

| Metric | Reported value |
| --- | ---: |
| Worker elapsed time | 963.5 seconds (16.1 minutes) |
| Input tokens in accepted worker receipts | 1,945,957 |
| Cached input tokens | 1,637,120 |
| Output tokens | 33,976 |
| Reasoning output tokens | 12,803 |
| Coordinator repair time | 59 minutes |

No currency cost is reported because the repository has no authoritative Luna price mapping. Token totals are **lower bounds**, not complete run totals: the current runner overwrites usage with the latest attempt instead of summing discarded attempts. Codex worker startup also loads substantial plugin, skill, instruction, and memory context; the database page alone reports 843,051 input tokens. This runtime is not yet token-efficient enough for a 220-page scale-out.

## Deterministic Validation Coverage

The validators successfully enforce:

- job/model/role identity;
- allowed and forbidden write paths;
- structured output and receipt fields;
- 3–5 exact raw-line quotes;
- canonical URL, raw path, and raw deep-dive link;
- Sol model ownership of final approval;
- passing validation entries in accepted receipts;
- capsule source-count reconciliation and focused wiki rules.

They do not detect:

- omissions, misleading emphasis, or taxonomy over-fragmentation;
- whether every summary claim is supported by evidence;
- conditional or mutually exclusive OpenAPI requirements;
- internal documentation inconsistencies and cross-language sample drift;
- content regression after a quote-only retry;
- missing rejected-attempt reasons or understated cumulative token usage.

## Independent Review

The requested read-only reviewer recommends **`scale_with_changes`**. It judged all Sol-finalized pages accurate and query-useful, with strong raw links, but found Luna unsafe for autonomous promotion.

Per-case conclusions:

- **Invoicing:** accepted draft is accurate after taxonomy and ASC 606 repairs; the first event stream fabricated unrelated invoice states before recovery.
- **Shadow baseline:** the strong baseline clearly wins on route coverage, equal billing-model emphasis, scope boundary, and title. Targeted quote repair would have preserved the better first Luna summary.
- **SDK:** final page is strong, but independent review found two additional cross-language example inconsistencies now added to the source.
- **Database:** Sol's grain, nullability, and beta-scope repairs were accurate; no additional material error was found.
- **Create contract:** final request-family map is accurate; the reviewer identified weak threshold grounding and one receipt/source preservation mismatch, now corrected in the source.

The review also confirmed the systematic risks described above: premature fabricated drafts, sparse evidence, mandatory repair burden, retry regression, incomplete attempt receipts, understated retry tokens, and large agent-runtime overhead.

## Coordinator Assessment

The coordinator agrees with `scale_with_changes`. The architecture is viable because ownership boundaries worked: Luna never promoted canonical content, Sol caught material issues, raw links remained intact, and deterministic checks prevented two invalid quote sets from being accepted. The same evidence shows that Luna cannot safely replace the strong coordinator.

The initial scale target should be a small mixed batch after tooling changes, with Sol reviewing every page and an independent reviewer sampling the batch. Stop conditions should include repeated factual reconstruction, critical omissions, high repair time, failed page-type extractors, or cumulative token use above the agreed budget.

## Required Changes Before Scale-Out

1. **Minimal Luna runtime:** disable unrelated plugins, skills, memory, and repository context; preferably pass the complete raw content directly to a structured model request.
2. **Claim-level evidence:** attach quote IDs or line ranges to every takeaway and material fact, plus explicit `sections_covered` and `material_omissions` fields.
3. **Attempt-complete receipts:** persist per-attempt validation errors, retry reason, rejected-output path, token usage, and cumulative totals.
4. **Targeted quote repair:** if content is otherwise valid, deterministically locate the quote and correct its line bounds instead of regenerating the whole summary.
5. **Page-type extraction:** add OpenAPI structural extraction, SDK cross-language comparison, and database table/grain/warning extraction before asking Luna to summarize.
6. **Richer output schema:** add `scope_boundaries`, `conditional_requirements`, `feature_gates`, `internal_inconsistencies`, and `sections_covered`.
7. **Mandatory strong review:** keep Sol as concept owner, contradiction reviewer, shared-index/log writer, canonical promoter, and final approver.
8. **Batch and sample:** validate a small mixed batch after these changes; use periodic independent review and do not automatically release the remaining queue.

## Evidence

- Jobs: [`jobs/`](jobs/)
- Luna runs and rejected attempts: [`runs/`](runs/)
- Baseline and Sol final receipts: [`receipts/`](receipts/)
- Luna output schema: [`schemas/luna-output.schema.json`](schemas/luna-output.schema.json)
- Pilot design: [`../../../../docs/superpowers/specs/2026-07-14-metronome-luna-sol-pilot-design.md`](../../../../docs/superpowers/specs/2026-07-14-metronome-luna-sol-pilot-design.md)
- Execution plan: [`../../../../docs/superpowers/plans/2026-07-14-metronome-luna-sol-five-page-pilot.md`](../../../../docs/superpowers/plans/2026-07-14-metronome-luna-sol-five-page-pilot.md)
- Provider operations: [`../../../../wiki/metronome-log.md`](../../../../wiki/metronome-log.md)

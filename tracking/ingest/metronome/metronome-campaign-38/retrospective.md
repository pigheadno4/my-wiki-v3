# Campaign 38 — retrieval-source confirmation retrospective

## Outcome

- Five approved new sources; first-pass approval **5/5**.
- Five worker attempts and five independent full initial reviews; zero retries, targeted rereviews, full rereviews, or coordinator semantic repairs.
- Single final retrieval audit **10/10 PASS**, with zero extra searches or route repairs. See [quality audit](quality-audit.md).
- Started `2026-09-08T09:27:23Z`; campaign completed `2026-09-08T09:50:22Z`: **1,379 seconds / 22m59s**. This measures execution through audit/operational closure, excluding subsequent retrospective writing and git commit.
- All approvals and promotions were observed complete at `09:44:35Z` (17m12s after start); the remaining interval to closure was 5m47s. These are phase observations, not per-agent performance instrumentation.
- Assigned raws total 1,111 lines. Promoted sources average 287.8 whitespace-delimited words, including frontmatter and navigation.

## What changed

1. Workers and reviewers used the same retrieval-oriented acceptance contract: read the full assigned raw, distinguish section roles, retain a smaller set of useful assertions and consequential warnings, and use raw locators for detail. Example payloads did not automatically become general claims.
2. Explicit maturity and example-specific qualifications were highlighted before dispatch. Retained claims still required evidence; reducing coverage did not authorize unsupported simplification.
3. Concepts received five reciprocal navigation entries across four existing concepts. Only credit/commit targeting needed a new matching-logic paragraph; there was no default page-by-page knowledge duplication.
4. Concept review followed the provider index to the main concept, then inspected the proposed section and relevant context, semantic fit, and reciprocal source link. It did not redo unrelated concept synthesis. Index links are entry points, not factual evidence.
5. The final ten predetermined questions were split into two disjoint audit groups. This preserved full raw grounding for detail questions while avoiding a duplicated coordinator audit.
6. Normal close aggregation enriched three existing index descriptions with contract-lifecycle, offset-configuration-lookup, and usage-targeting vocabulary. These were non-blocking discoverability improvements, not failed-route repairs.

## Comparison and limits

| Measure | Campaign 37 | Campaign 38 |
| --- | --- | --- |
| First-pass approvals | 3/5 | 5/5 |
| Full initial reviews | 5 | 5 |
| Targeted rereviews | 2 | 0 |
| Full rereviews | 0 | 0 |
| Operational closure | 27m52s | 22m59s |
| Raw lines | 1,989 | 1,111 |
| Final query audit | 10/10 | 10/10 |

C38 closed 4m53s earlier, but its raw corpus was substantially shorter and the pages differed. This is encouraging confirmation, not a controlled speed benchmark or proof of token savings. Five pages cannot establish stable production first-pass rates. Full initial independent reviews remain a substantial model-work component.

## Verification and scope

One close mechanical verification passed: 11 touched wiki files, unchanged raw hashes, candidate/promotion equality (ignoring final newline only), six approved shared updates present exactly once, intended reciprocal navigation, company/provider catalog entries and coverage counts, capsule validation, and diff checks. Capsule totals are 310 immutable raw snapshots, 192 sources, and 100 raw snapshots without a source; 186 sources are official-documentation summaries. The frozen never-ingested inventory has 40 canonical identities remaining.

No runtime schema, model, concurrency, collection behavior, or new monitoring framework was introduced. Existing runtime `dry_run` metadata is retained; canonical promotion is evidenced separately by the wiki files and close checks. Post-close report/index/log formatting receives only scoped validation, not another semantic audit.

The post-close generic validator flagged the provider index's pre-existing absence of YAML frontmatter. Its established router format was preserved; all index wikilinks were checked separately and passed. Log validation and report-target existence checks passed. No validator or index-schema change was introduced for this format mismatch.

## Next optimization

Keep the same narrow retrieval contract for a subsequent approved five-page sample. Continue preventing qualification/scope mistakes before dispatch, retain critical warnings, and make index descriptions express likely query vocabulary. Review only changed concept assertions and their relevant context, plus unique reciprocal navigation; expand reading only when an actual overlap or contradiction warrants it. Do not turn successful navigation into permission to skip evidence review, bulk-migrate providers, or build a new registry.

# Stripe Node 23.0.0 full-ingest receipt

- Date: 2026-10-18.
- Work item: `github-fc2596c23efd4fe6756c`.
- Identity: `stripe@22.6.2` -> `stripe@23.0.0`, SHA `fe645f63d645011aca38dff9e245c1cf7b9ae60e`.
- User-approved mode: full, additive, all v22 knowledge retained.
- Reading exception: fully read runtime/shared code, examples and exact-SHA handler supplement; read changed generated API sections and affected prior code; mechanically verify unchanged schemas, old historical changelog, manifests/inventories and duplicated diff. No repository-wide full-read claim.
- Current/prior snapshots: 68/68 retained files, SHA-256, size and Git blob verification passed. 35 modified, 33 unchanged, no additions/removals. Supplement hash/size passed; validator accepts its canonical attachment and exact-SHA identity.
- Comparison: all 1,119 upstream changed paths classified, including 995 excluded `.hark` fragments; original snapshot/packet unmodified. Packet comparison budgets adjusted only for this reviewed registry entry, retaining source selectors and source limits.
- Historical raw changelog is regenerated, not byte-identical: anchors/reordering, date changes and a historical PR-reference difference were detected mechanically. Older raw remains immutable. No historical wiki facts were updated from the regenerated older notes.
- Grounding: five exact quoted lines and locations recorded in the source's v23 chapter.
- Concepts updated first: Node SDK, Checkout, PaymentIntents, Subscriptions. Then cumulative source/changelog, company, provider index/log and root log. No new source pages; source_count remains 666. No cross-company comparison warranted.
- Contradictions qualified: retry count comments versus platform defaults; zero tolerance in snapshot versus thin helpers; stale low-level helper spelling; explicit subscription pause versus trial-only status comment; old example Node requirement versus Node20 engines.
- Findings reviewed against implementation: callback client newly binds resources/request sender using withStripeContext, drops stripeAccount and shares telemetry/emitter; thin versus snapshot names; body-read classification without automatic rerequest; dynamically eligible Checkout allowlist; scoped request-field removals; separate direct/scheduled resume payment defaults.

## Validation

- `validate_wiki.py`: eight typed touched files pass, no issues. Root log and provider index have no YAML frontmatter by existing convention and were checked separately, not converted.
- Source and changelog relative evidence links exist; both provider index entries occur exactly once. Existing source retained-history block and old raw links remain byte-identical; the entire changelog from 22.6.2 onward remains byte-identical.
- `validate_github_collection.py`: same 12 existing errors in six unrelated repositories (packet budgets and resulting invalid-packet reports), none for Stripe Node. After completion, pending work items: zero. Work item is `ingested`, approved mode `full`. Do not report global validation clean.
- Focused Stripe Node comparison-budget regression test passes; `git diff --check` passes. All five grounding quotes match the exact immutable raw lines.
- The earlier full code suite for the scoped budget change ran 811 tests: 809 passed, two existing registry assertions failed (Adyen Postman 30 versus 40 files, PayPal Messages iOS v1-only expectation versus registered v2). Unrelated failures left untouched; documentation-only ingest does not alter that code result.
- No upstream SDK tests/build, package installation, hosted/runtime payment, or Connect routing execution. No commit or push authorized for this ingest.

## Next Action

Work item closed and generated progress refreshed. Next: scoped commit/push approval, preserving concurrent Adyen campaign and other unrelated workspace changes.

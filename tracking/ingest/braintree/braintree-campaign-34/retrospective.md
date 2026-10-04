# Braintree C34 timing and retrospective

Status: complete. Operational close: 2026-10-04T05:21:52Z. Elapsed 33m04s, versus C33 42m11s (9m07s / 21.6% shorter). Raw volume decreased 57.3%; this is not evidence of concurrency-only causality.

- Runtime initialized: 2026-10-04T04:48:48Z.
- First ten workers confirmed running: 2026-10-04T04:51:58Z (3m10s after initialization).
- Primary raw volume: 1,682 lines across twenty pages (C33: 3,937 lines).
- Live native capacity confirmed: ten simultaneous child workers plus coordinator. Worker/reviewer/auditor roles share those ten slots.

Remaining worker, review, catalog, query-analysis/handoff and close milestones will be recorded as observed. No causal speed claim from this differently sized content set.

- Last initial worker completion: 2026-10-04T05:06:43Z (17m55s from initialization).
- Last independent review completion: 2026-10-04T05:12:41Z (23m53s).
- Canonical sources and aggregate company/index routes ready: 2026-10-04T05:13:09Z (24m21s).
- Worker/initial-review results: twenty approved, nineteen first-pass; twenty full initial reviews and one targeted retry review; zero repeated full reviews.
- Only retry: Chase bank-change source overclaimed that the procedure was not an API operation. Raw documents a Control Panel upload without proving API absence; correction narrowed the sentence and preserved all other bytes, quotes and suggestions. Coordinator performed no semantic repair.
- Post-initial-worker review/publication window overlaps worker completion and receipt handling; these elapsed milestones are not additive per-role CPU durations.

- Source volume: 10,237 words (512/page); zero mechanical format repairs.
- Last initial query analysis: 2026-10-04T05:16:50Z; last initial audit artifact timestamp: 2026-10-04T05:18:06Z. Reports observed after handoff, not assumed complete at analysis end.
- Query audit initially found one missing provider-index edge to the generic reconciliation concept. This also exposed an incorrect initial Group A route PASS. Coordinator added only the navigation edge; affected route/hash checks were targeted, without source rewrite or another full raw read. Group E recheck passed at 2026-10-04T05:19:59Z; original failure retained.
- Structural close checks passed for all twenty candidate/source byte pairs, raw hashes, unique canonical ownership, approved shared updates, reciprocal links, exhaustive website catalogs and 352=335+17 counts. Typed wiki validation: 30/30. The temporary checker compared the parsed source_count string to an integer on its first run; comparison was corrected without wiki edits. This is a checker issue, not a source-content failure.

- Final affected Group A route recheck completed: 2026-10-04T05:20:44Z; final queries 40/40.
- Campaign closed: 2026-10-04T05:21:52Z. Query analysis/initial handoff and targeted route-repair/closure occupied 8m43s after catalogs were ready; do not attribute this whole window to model reasoning.

## Small next-round improvements

- Keep the confirmed ten-slot rolling pool; do not add roles or validation systems.
- During the existing catalog write, ensure the main concept of each new source is actually exposed from the provider index, including generic concepts. This would have prevented the single navigation repair without another review layer.
- Draft query reports directly as a route plus two short answers and shared notes once. Initial report writing still took 63–84 seconds between analysis and artifact timestamps and copied substantial routine detail; avoid extra inventory and repeated snapshot/outcome caveats.
- Use verified raw locators for routine detail, and avoid repeating the same eligibility/evidence caveat in overview, takeaways and warnings. No hard word cap or rewriting accepted sources.
- Capacity improvement is confirmed, but latency is not proportional to slot count: the 27-line Adyen overview took about eight minutes from dispatch to worker completion, whereas the 204-line first page completed much faster. Native task/tool/model queue time is not isolated by the existing timestamps; report the observed variance without creating a profiler.

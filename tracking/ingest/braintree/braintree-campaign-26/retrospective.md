# Braintree C26 timing and outcomes

Status: COMPLETE. Initialized at `2026-10-02T10:44:44Z`; closed at `2026-10-02T11:16:13Z`: **31m29s operational wall clock**. User approved exact C26 manifest after C25 and simplifications were committed/pushed. Ten jobs, three dynamic slots, independent per-page first review; no new code/rules or reviewer waiver. No execution interruption was observed.

Ten jobs approved and promoted; first full-review pass **8/10**. Ten full and two targeted reviews; no repeated full semantic review. Fixed query audit **20/20**. Ten sources total **4,548 whitespace-delimited words**. One external A1 schema repair preceded accepted handoff; no automatic list-format repairs and zero canonical coordinator repairs. Typed-page validation passed **16** pages. Braintree now catalogs **232 sources = 215 website + 17 GitHub**. Exact candidate equality, raw hashes, approved concept-update presence, reciprocal routes and catalog uniqueness/counts passed.

## Role observations

Intervals include setup, reading and handoff; parallel intervals overlap and must not be summed into wall time.

| Role | Start UTC | End UTC | Duration |
| --- | --- | --- | --- |
| JavaScript migration worker A1 | 10:45:18 | 10:47:11 | 1m53s |
| Auth client iOS worker A1 | 10:45:41 | 10:47:22 | 1m41s |
| Auth branding JavaScript worker A1 | 10:45:55 | 10:47:40 | 1m45s |
| JavaScript migration full review | 10:47:32 | 10:48:56 | 1m24s |
| Auth client iOS full review | 10:48:37 | 10:50:22 | 1m45s |
| Auth branding Android worker A1 | 10:49:45 | 10:50:33 | 48s |
| Auth branding JavaScript full review | 10:50:22 | 10:51:39 | 1m17s |
| Auth client iOS worker A2 | 10:51:42 | 10:52:41 | 59s |
| Auth branding Android full review | 10:52:48 | 10:53:01 | 13s |
| Auth branding JavaScript worker A2 | 10:52:36 | 10:53:31 | 55s |
| Auth client iOS targeted review | 10:54:00 | 10:54:26 | 26s |
| Auth branding JavaScript targeted review | 10:55:18 | 10:55:46 | 28s |
| Auth client Android worker A1 | 10:55:17 | 10:57:24 | 2m07s |
| SDK deprecation JavaScript worker A1 (reported creation-to-handoff, not full role interval) | 10:57:02 | 10:58:04 | 1m02s |
| Auth branding iOS worker A1 | 10:56:40 | 10:58:27 | 1m47s |
| Auth client Android full review | not retained | 10:59:44 | not reconstructable |
| Auth branding iOS full review | 11:00:40 | 11:00:56 | 16s |
| SDK deprecation JavaScript full review | not retained | 11:02:04 | not reconstructable |
| SDK deprecation iOS worker A1 | not retained | 11:02:40 | not reconstructable |
| SDK deprecation Android worker A1 (raw-read-to-complete window) | 11:02:59 | 11:04:04 | 1m05s |
| Auth client JavaScript worker A1 (artifact-to-validation window) | 11:04:29 | 11:04:43 | 14s |
| SDK deprecation iOS full review | 11:03:44 | 11:05:07 | 1m23s |
| SDK deprecation Android full review | 11:05:00 | 11:06:18 | 1m18s |
| Auth client JavaScript full review | 11:05:47 | 11:06:57 | 1m10s |

One A1 handoff had `warnings` as a string instead of an array. The coordinator's combined accept/dispatch call aborted on assignment mismatch after projected validation failure, before state persistence. A direct existing-validator check identified the schema defect; the worker repaired only the external field to `[same text]` at 10:59:50Z, before accepted handoff. No new attempt or semantic rereview was consumed. This is handoff repair overhead, not a first-review semantic failure.

## Stage observations

Operational start: 10:44:44Z. First three handoffs: 10:47:11Z–10:47:40Z. Role reading now uses the 955-word consolidated entry plus trusted order and concise provider notes, not the prior 6,725-word general/provider/history bundle. Early intervals do not establish a causal or campaign-level speedup.

Last semantic review ended at 11:06:57Z; accepted by coordinator and final sources promoted by 11:07:49Z. Query group A was dispatched before the last reviews ended, using the complete concept route; group C overlapped final promotion. Aggregate catalog/count edits were in place by 11:10:41Z (first post-edit observation; exact edit time was not retained). These overlap, not additive stages.

| Operational window | Observations | Wall span / qualification |
| --- | --- | --- |
| Initialization through last semantic review | 10:44:44–11:06:57 | 22m13s; includes setup, role reading, drafting/review, bounded retries, dispatch and interleaved promotion |
| Last review through final-source promotion | 11:06:57–11:07:49 | 52s; query audit already overlaps |
| Fixed query audit | Group A already dispatched by 11:06:19; final handoff 11:14:02 | Exact first dispatch timestamp not separately retained; at least 7m43s, overlapping final promotion/catalog aggregation |
| Final audit handoff through mechanical close/runtime completion | 11:14:02–11:16:13 | 2m11s; includes report acceptance, logs, mechanical checks and runtime close |

Query analysis-end/handoff observations: A 11:07:32/11:08:17 (45s); B 11:10:22/11:10:22 (0s reported); C 11:09:10/11:09:14 (4s); D 11:10:36/11:10:51 (15s); E 11:13:01/11:14:02 (61s). These overlap and are not additive latency. C's one extra complete JavaScript-branding read policed variant boundaries; B's two extra complete Connect/server-side reads verified URL responsibilities. Other groups required no extra full raw reads.

## Findings and bounded next opportunities

C26 closed 15m27s sooner than C25, about **33% shorter**. It also had two rather than four targeted reviews and 4,548 rather than 5,628 source words. The selections differ and C25 included interruption/recovery, so this is an observed campaign result, not proof that the role entry alone caused the reduction. The required role entry now has about 86% fewer words; that input-volume reduction is independently established. No eligible list-format defect appeared in C26, so its automatic repair path has test coverage but no measured live savings here.

The two first-review blockers were distinct: iOS retained the guide's trusted-source prose without surfacing its code contradiction; the JavaScript branding reciprocal description said server-generated redirect rather than redirect via server-generated connect_url. Both were corrected with bounded diffs and 26/28-second targeted reviews, not repeat full analysis. Keeping reciprocal descriptions to variant plus document purpose would avoid unnecessary behavioral assertions; material source security conflicts still require preservation.

Smallest next guidance refinement, requiring separate approval: state the existing `warnings` string-array type explicitly in the concise role entry and encourage purpose-only reciprocal navigation descriptions. Do not add a validator, registry, review layer or automatic schema coercion. Final audit reporting still had 45/61-second handoff tails in two groups; keep the already-approved direct concise format rather than adding another reporting pass.

One close-check assertion incorrectly counted an older company's inline fact citation as a duplicate catalog entry. Inspection confirmed one list entry plus one legitimate inline contradiction citation. The catalog check was narrowed to list entries; historical content was not modified. This diagnostic false positive was not a source or campaign quality failure.

No raw collection, GitHub ingest, code/rule change, commit, push or next campaign was performed by C26 execution. Post-close retrospective writing is excluded from operational wall clock.

## Separately approved post-close guidance clarification

The user approved the two bounded guidance refinements after campaign close. `rules/ingest-roles.md` now explicitly requires `warnings` to be an array of strings (`[]` when none) and defaults reciprocal source descriptions to document type/version plus purpose rather than detailed behavioral claims. Material warnings and necessary durable concept facts remain required. No validator, schema coercion, registry, review layer or historical-output change was added; this follow-up is outside C26 operational timing.

Verification: 150 ingestion-related tests passed and scoped `git diff --check` passed. Full repository discovery aborted at the existing unrelated GitHub `test_release_notes_are_secret_scanned_before_publication` exception-handling issue (`SecretFindingsBlocked is immutable`); that other workflow was not modified.

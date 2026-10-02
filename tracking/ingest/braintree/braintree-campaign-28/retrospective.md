# Braintree C28 timing and bounded follow-up

## Outcome

Ten approved sources; first pass 9/10; ten full plus one targeted review; no full retry. Fixed query audit 20/20, typed validation 19/19, zero automatic formatting or canonical semantic repairs. Source text totals 5,863 whitespace-delimited words. All 1,586 primary raw file lines were available to the assigned complete reads; related evidence was read only for retained claims/conflicts.

## Observed stages

| Milestone/window | Time | Interpretation |
| --- | --- | --- |
| Initialize → last accepted full review | 13:53:31–14:26:29 UTC; 32m58s | Overlapping workers, reviews and one bounded correction; includes dispatch-capacity waiting |
| Last review → final source promotion | 14:26:29–14:26:48; 19s | Approved updates precede exact candidate promotion |
| Fixed queries | First report at 14:18:18; last handoff 14:28:38 | Analysis began before first report; overlapping window, not an additive duration |
| Catalog aggregation observed complete | 14:28:40 | Company/index entries and source_count updated once |
| Last query handoff → runtime close | 14:28:38–14:31:38; 3m00s | Reports/logs, mechanical/typed checks and terminal state |
| Total | 13:53:31–14:31:38; 38m07s | C27 was 34m39s; this is not a controlled A/B comparison |
| Post-close report/status handoff | 14:31:38–14:34:04; about 2m26s | Runtime duration excludes final report writing; observed initialization-to-handoff is about 40m33s |

## Why elapsed did not fall

- Near 14:00 UTC the coordinator sent a timing-only follow-up to the completed JavaScript reviewer. It appeared as pending_init and occupied host capacity; interrupt did not release it. A new styling reviewer and a completed-role follow-up each hit the thread limit. Styling review began once another worker completed. Worker/reviewer scheduling conservatively used two child slots while the pending thread remained, rather than claiming three active ingestion slots.
- Around 14:15–14:16 the same pending reviewer was given the already-approved group E query job; the task ran and handed off at 14:18:18. Three usable slots then resumed. The capacity loss is therefore partly a coordinator handoff mistake, not evidence that the source method needs another quality layer. Exact lower-level initialization time was unavailable; do not turn this approximate interval into a precise overhead attribution.
- The single bounded correction took approximately 14:16:40–14:20:52 across worker and targeted reviewer. It addressed consequential refund semantics and an incorrect reciprocal source identity, not style or optional detail.
- Some report handoffs followed analysis by roughly 39–57 seconds. Groups A/B unnecessarily copied their dispatch prompts because “prompt artifact” was ambiguous. Groups C/D were explicitly asked to return promptly without prompt copying.
- Two transient close-check assumptions were corrected before typed validation: GitHub sources are in a nested folder, and the partial-settlement source legitimately has additional fully read factual raws. A catalog patch also used a nonexistent company heading and failed without changing files before being corrected. These were coordinator tooling/placement assumptions, not worker quality retries or canonical content repairs. The generic 19-page validator and scoped diff check each ran successfully once; no test suite or new validator was introduced.

## Next approved-method improvement

Keep the existing method and exact approval boundary. Do not message a completed role merely to obtain a timing estimate; use its initial handoff and existing records. Reuse a role only for a real approved next task. Check actual host capacity before dispatch, fill available slots promptly, and ask for concise query answers without prompt copies or prose polishing. Use recursive source enumeration and permit fully read supporting raw evidence in the existing close check. No new monitoring schema, retries, review layer or campaign is authorized by this retrospective.

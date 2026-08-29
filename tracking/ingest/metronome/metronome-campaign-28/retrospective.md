# Metronome Campaign 28 retrospective

## Result

- Started: `2026-08-29T03:35:00Z`
- Completed: `2026-08-29T04:07:16Z`
- Elapsed: 1,936 seconds (32 minutes 16 seconds)
- Final approval: 5/5
- First-pass approval: 3/5
- Worker attempts: 7
- Full reviews: 7
- Targeted reviews: 0
- Coordinator semantic repairs: 0

The campaign finished 89 seconds slower than Campaign 27 but remained within the non-binding 35-minute observation target. Quality and the 9/9 query audit passed; the planned first-pass and retry-count gates did not.

## What worked

- Three guide and integration pages passed on attempt 1, including cross-system Anrok authority and data-export delivery boundaries.
- Dynamic slots avoided a batch barrier, and four approved sources were promoted while the remaining work continued.
- Review caught two material defects before promotion: incorrect `custom_fields` nesting on List Products, and broadened `SPEND` semantics plus authority and concept-routing gaps on Create Credit.
- The coordinator performed no semantic source repair and no third full raw read.

## What cost time

- List Products and Create Credit each required a second complete worker read and a second complete reviewer read because the defects changed factual schema or financial meaning. Those two retry cycles account for the difference between the planned five reviews and the observed seven.
- Two first-attempt workers wrote candidate and receipt staging files before controller ingestion. Their contents were byte-equal to the returned results; the coordinator deleted only those premature copies and let the controller recreate them. No semantic work was repeated, but future worker prompts should continue to state that only the controller writes attempt staging.
- The fixed three-page closing audit remained an intentional quality cost.

## Recommendation

Do not increase campaign size yet. Keep the current architecture and make only two bounded worker-brief corrections for the next Metronome sample: require explicit parent-schema placement for API list fields, and preserve raw financial units and source authority verbatim before paraphrasing. Keep controller-only staging writes explicit. Run another five-page mixed sample; do not add a registry, new scheduler feature, or extra test layer.

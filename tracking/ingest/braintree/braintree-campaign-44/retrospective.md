# Braintree C44 timing and small optimization findings

Runtime12:14:43–13:10:49UTC:56m06s. C43 was51m02s; C44 is5m04s (9.9percent) longer. Faster total completion was not demonstrated. Fifty sources/100fixed queries remain unchanged scope, with ten shared rolling child slots and Sol medium worker/different Sol high initial reviewer.

## Overlapping stage windows

| Stage | UTC window | Measurement |
| --- | --- | --- |
| Worker dispatch/drafting/corrections |12:14:43–13:02:48|53matched artifacts; attempt-directory birth to external artifact modification, median111s/max240s; includes dispatch overhead|
| Independent reviews/corrections |12:17:18–13:04:30|50full reviews median116s/max239s;3targeted reviews median63s/max86s; review-input modification to external artifact modification|
| Canonical promotion |12:24:15–13:04:42|Source birth window; overlaps drafting/review/queries|
| Query report saving |12:31:24–13:10:49|13reports/100questions; saving window is not active model compute|
| Shared aggregation and close |Approximately13:04:55–13:10:49|One catalog/count/log aggregation, one structural close, one65-file typed validation; mostly overlaps final query wait|

Windows overlap and must not be added. External mtimes and filesystem birth times are approximate lifecycle evidence, not token counts or isolated model compute. Two external worker artifacts had modification times later than accepted receipts; their negative handoff intervals were excluded rather than treated as speedups. Valid handoff timing covers51/53receipts.

Handoff wait median81s/max179s versus C43 110s/288s: about26percent lower median and38percent lower maximum. Worker median111s versus103s, full review116s versus99s, targeted63s versus62s. Improvements in controller handoff were offset by slower initial review and the serial tail. The final reports-overview correction delayed the last four-page query group until source promotion around13:04:42; its external report was saved13:10:30 and archived13:10:49. That approximately6-minute tail includes dispatch, evidence reads and report writing, not just pure reading.

Primary raw volume22,468→12,940words (-42.4percent); source volume24,328→20,153 (-17.2percent). Query reports14,308→13,784words (-3.7percent). Compact-report guidance produced only a modest output-size reduction. Different page/product scopes and supporting conflicts prevent a causal model-speed comparison.

## Quality and corrections

Initial accepted approvals47/50 (94percent), but original first-submitted review verdicts46/50 (92percent). One Swift-example syntax observation was independently reconsidered nonblocking under the approved retrieval contract; no worker retry or repeat full read. Both original observation and accepted review remain durable.

Three actual worker corrections: Channel API versus generic webhook acknowledgement/retry scope and missing webhook route; merchant responsibility versus ownership for In-Person authentication; optional custom-field report grouping and central reporting discoverability. All three retries used targeted unchanged-hash/diff/context reviews. No mechanical receipt rejection, reviewer schema repair, terminal rejection or semantic coordinator source amendment. One mechanical concept insertion repair restored historical wording and exact approved new text, independently checked by group M.

Fixed queries100/100PASS; no query source correction. Full-read immutable raw provenance and reciprocal links remain required. Parallel dispatch and verification-before-completion skills supported isolated outputs and evidence-backed closure; no new framework was added.

## Next small decisions

1. Do not describe C44 as a throughput improvement: handoff improved, total duration did not. Keep current rolling scheduler and exact approval boundaries.
2. Front-load likely shared-concept routes and optionality in the existing worker check, especially broad reporting overviews; no invariant registry or new validator. This addresses observed failures without expanding source fact density.
3. Keep audit answers genuinely retrieval-oriented and short. Reports still total13,784words despite the compact instruction; avoid repeated non-proof inventories and exhaustive projection/field lists. Preserve the100approved questions unless the user explicitly approves a smaller future audit scope.
4. For future rounds, consider dispatching riskier broad overview pages earlier so a bounded late correction does not gate the final audit group. Use existing manifest ordering only; do not build a performance scheduler.

Commit/push and next campaign require separate approval.96successful previously unreferenced website variants remain after these50new sources; the27,225-word validation-errors-all-node page remains separately deferred and eligible.

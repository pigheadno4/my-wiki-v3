# Braintree C14 execution notes

Status: COMPLETE. Exact10-page execution approved2026-09-22.
Runtime start12:59:53Z. All10 hashes and absent raw/canonical/target ownership
verified after overnight pause; C13 complete. Baseline101=85website+16GitHub.
Three Sol medium workers started with persisted orders; all canonical/shared
writes coordinator-owned. No raw edits, collection, code/rule changes, GitHub
ingest, commit/push or next campaign authorized. Actual stage timing recorded
here and in audit reports; overlapping windows are not additive.

## Early observations

- Initial Create, Testing and Manage handoffs arrived at13:05:09Z,
  13:05:48Z and13:06:29Z. Individual worker start times were not separately
  captured, so these are handoff observations, not precise service durations.
- Overview worker13:07:06–13:09:25Z; Plans worker13:10:25–13:12:22Z.
- Create full review13:06:55–13:08:38Z and Testing full review
  13:06:07–13:09:36Z both approved first attempt; sources promoted.
- Manage full review13:10:06–13:12:49Z requested a bounded charge-or-credit
  qualification correction. Overview full review13:10:28–13:12:27Z requested
  restoring indefinite Past Due retries and directly grounding retained status
  definitions. Both corrections use targeted review; no full reread requested.
- These are retained-summary qualification defects, not requests to copy
  routine API detail. Existing subject/condition/action drafting self-check
  applies; no new validation mechanism or report field was introduced.

Manage correction13:14:43–13:17:02Z; targeted review13:17:55–13:18:20Z.
Overview correction13:14:48–13:16:47Z. Plans first review13:15:03–13:16:25Z
requested replacing the overly broad `subscription identity` with `plan name
and description`; correction13:17:31–13:18:54Z and targeted review
13:20:23–13:20:55Z approved. All five initial guides approved by about13:21Z.
No full retry review. These corrections and their handoffs consumed slots that
otherwise could serve the remaining pages; do not attribute all elapsed time
to raw length or full rereading.

Manage promotion needed one placement-only normalization: its approved concept
suggestion combined two labeled snippets/anchors. Same reviewer confirmed exact
extraction into each named heading; see attempt2/placement-normalization.md.
Canonical candidate and receipt are unchanged. Count one bounded coordinator
placement repair, not a semantic rewrite. Do not generalize the helper exception.

Transactions worker13:18:58–13:22:06Z; full review13:22:35–13:25:08Z
requested a bounded distinction between a snake_case prose/link label and the
actual camelCase Node request option. Disbursement worker13:20:16–13:22:26Z;
Submerchant worker13:23:16–13:28:07Z. Group B audit analysis13:22:02–13:23:26Z,
handoff13:28:07Z:4/4 PASS. The4m41s analysis-end-to-handoff span is observed,
not assumed model reasoning or backend latency. Accepted report only narrows
`concept lists each source once` to `concept Sources section` because Manage
also has the approved fact-bearing link; no repeated raw audit.

Disbursement full review13:31:34–13:32:32Z and Submerchant full review
13:32:16–13:32:57Z approved first attempts. Transactions bounded correction
13:32:01–13:34:08Z preserved all quotes/suggestions and distinguished the
actual Node field from the collected prose label. Seven pages promoted by
about13:33Z; Group D starts while the remaining work proceeds.

Transactions targeted review13:34:26–13:35:07Z approved. Test webhook worker
13:33:29–13:34:48Z; full review13:35:33–13:36:08Z approved first attempt.
Auth worker13:35:32–13:38:20Z. Group D audit13:34:03–13:34:27Z with handoff
13:34:32Z passed4/4. Group A audit13:35:57–13:36:24Z with initial handoff
13:36:29Z passed4/4, but coordinator found its answer had re-omitted the
indefinite-retry qualification already fixed in the approved source. Same
auditor corrected that report sentence and clarified new-subscription-only
inheritance wording from existing evidence; no source change or full reread.
Keep report corrections separate from source retries and promotion repairs.

Group C audit13:37:13–13:38:38Z; handoff13:38:44Z,4/4 PASS. Coordinator
corrected only the report's root section label from `PSPs` to `PSP Indexes`.
Auth full review13:39:26–13:39:55Z approved first attempt. All10 canonical
sources promoted and aggregate company/index/log updated by13:41Z.
One mechanical close passed:10 exact approved candidates, immutable hashes,
canonical identities and unique owners, quotes, raw backlinks, approved concept
snippets, reciprocal/catalog links and counts;111=95website+16GitHub;
16 touched typed files. Scoped git whitespace check also passed.
The only snippet-equality exception is the documented exact two-heading
placement extraction for Manage; canonical source/candidate equality is exact.

## Final result and elapsed time

Closed2026-09-22T13:43:13Z; elapsed43m20s (2600s).10/10 approved and
20/20 fixed queries PASS. First-pass content6/10, four targeted corrections,
zero full retries and one approved placement-only coordinator repair.
All worker handoffs were accepted without runtime-format retries.

| Stage | Observed UTC window | Interpretation |
| --- | --- | --- |
| Startup to first worker handoff |12:59:53–13:05:09|5m16s; individual initial worker start times unavailable |
| Worker handoffs, including corrections |13:05:09–13:38:20|33m11s delivery window, not summed model service time |
| Independent review analysis |13:06:07–13:39:55|33m48s overlapping window;10 full+4 targeted |
| Fixed query audit |13:22:02–13:41:23|19m21s overlapping window;five groups; Group A report-only correction included |
| Final promotion/aggregate/mechanical close |approximately13:40–13:41:19|about1m19s; earlier promotions incremental |
| Last audit handoff to runtime closure |13:41:23–13:43:13|1m50s delivery/acceptance/report/closure |

Windows overlap and must not be added. Runtime closure excludes any final
retrospective formatting after13:43:13. C13 took24m50s: this run is18m30s
slower, not evidence of improved throughput. C14 has1067 logical raw lines
versus C13's1418, so raw length alone does not explain this difference.

Observed contributors are four correction loops rather than one; guide-level
summary qualifications and Node prose/code naming required bounded fixes;
review/worker/auditor roles compete for the same three slots; and delivery or
coordinator-dispatch gaps remain. Group B alone recorded4m41s between analysis
end and report handoff. Other uninstrumented intervals cannot be labeled model
reasoning, tool latency or queue time with confidence.

Keep the next improvement small and within existing drafting guidance: retain
the raw's specific nouns and alternatives rather than broad synonyms; omit
incidental fields from retrieval prose when not necessary, but verify actual
SDK spelling whenever retaining one; hand off concise reports immediately.
No new registry, validator, mandatory checklist artifact or full-review round
was added. Any policy change or next campaign still requires separate approval.

No raw edits, collection, GitHub ingest, code/rule changes, commit/push or
subsequent campaign. Unrelated shared-checkout work preserved.

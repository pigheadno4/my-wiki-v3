# Braintree C15 execution notes

Status: COMPLETE. Exact ten-page manifest approved and closed 2026-09-23.
Runtime started 2026-09-23T11:03:46Z. Preflight confirmed ten immutable hashes,
canonical URLs, absent source ownership and targets, C14 completion, and the
111-source baseline (95 website plus 16 GitHub). Three Sol medium workers were
dispatched with persisted orders for Best Practices, Authorization Responses,
and Exceptions. All canonical, shared, and campaign state writes remain with
the coordinator. Timing windows recorded below will overlap and must not be
summed. No raw, code, rule, GitHub, commit, push, or new-campaign work is in
the authorized execution scope.

## Result and elapsed time

- Runtime: 2026-09-23T11:03:46Z to 11:37:15Z, **33m29s** wall time.
- Ten initial workers produced ten accepted candidate handoffs. Nine of ten
  received first-pass content approval. Best Practices received one bounded
  timeout-phrase correction and targeted review; no full retry review.
- Ten initial full reviews plus one targeted review. All ten final candidates
  were promoted; coordinator semantic repairs: zero.
- Five fixed query groups, four questions each, passed 20/20. Audit windows
  overlapped remaining worker/reviewer activity: first started 11:27:52Z,
  final handoff 11:36:45Z. Four groups identified pending direct aggregate
  catalogs at audit time; the final check confirmed them after aggregation.
- Canonical company/index/log aggregation occurred once; the campaign-scoped
  mechanical close and scoped whitespace check passed before runtime close.

The windows overlap: worker, reviewer, query-audit and coordinator time must
not be summed. The largest visible elapsed segment was completing the ten
independent worker/full-review pairs under three child slots; the 20 query
checks were deliberately overlapped with the tail of ingestion. This round
improved on a batch barrier but still spent 33m29s for ten pages, so the
remaining speed opportunity is reducing first-pass candidate/review handoff
latency, not adding another validator or another audit layer. The one actual
first-pass defect was a narrow server-SDK timeout noun/scope error; preserving
raw-specific actor and condition wording in worker drafts is the direct
prevention cue for the next approved campaign.

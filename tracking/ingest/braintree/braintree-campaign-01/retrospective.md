# Braintree C01 execution notes

Status: COMPLETE. User approved exact five-page execution on 2026-09-19.
Runtime 2026-09-19T07:51:15Z–2026-09-19T10:34:27Z, 2h43m12s elapsed including
the session interruption. No commit or push performed.

## Timing and dispatch

- First three trusted worker orders persisted individually and immediately
  dispatched: transaction-sale-node, get-started, webhooks-overview. Three
  native Sol medium children confirmed; no prior active child agents.
- By 07:52:46Z all three were active. Agent-reported work intervals and
  subsequent coordinator observations will be recorded below; these windows
  overlap and must not be added to claim campaign wall time.
- Provider-qualified runtime selector: `braintree/braintree-campaign-01`.
  Legacy scheduler preflight prose is overridden by the explicitly attached
  retrieval contract; no Metronome factual authority applies to Braintree.

## Approval and promotion

Get Started attempt 1 approved and promoted with both exact concept updates
before the source by 08:01:10Z. Company baseline: 16 cumulative GitHub sources;
website sources from this campaign are counted separately and added once at close.

- Sale worker: 07:52:20–07:54:49Z (2m29s); start worker: first captured
  observation 07:53:53Z, completion 07:54:57Z (not a complete duration).
- Webhooks worker: 07:52:51–07:55:44Z (2m53s).
- Get Started full reviewer: 07:56:52–07:58:31Z (1m39s), approved.
- Control Panel worker: 07:56:56–07:59:13Z (2m17s).
- Sale initial review requested one bounded omission fix: risk/fraud data
  prerequisite and retrieval vocabulary. Final observed review/handoff window
  07:58:10–07:58:33Z is not the complete review duration.
- Sale targeted worker correction: 08:00:19–08:01:20Z (1m01s), validated.
  No full raw retry requested. Coordinator's redundant explicit retry call
  was rejected because changes_requested already queued the job; no duplicate
  attempt was created. Continued from that existing queue state.

## Interruption and resumed work

- Control Panel correction completed 08:05:22Z (worker interval 08:04:32–08:05:22Z).
  Its reviewer resumed at 10:24:26Z and approved at 10:24:54Z (28s targeted).
  The 2h19m04s between correction completion and reviewer resume is a visible
  inter-observation gap, not demonstrated model execution time. Exact session
  suspension boundaries were not recorded; do not claim a precise active-only
  campaign duration by subtracting an invented pause interval.
- At 10:25:11Z runtime reconciliation found only the completed Control Panel
  reviewer in the native agent list. Webhooks attempt-2 handoff existed in /tmp;
  cards review output did not. Accepted the saved webhooks correction and
  resumed its targeted review; restarted only the missing cards first review
  against the existing trusted order. No candidates were regenerated.
- Control Panel approved attempt-2 concept and source promoted after resume.
  Sale approved attempt 2 had already been promoted by 08:04:44Z. Query audit A
  starts against the two already linked SDK routes while remaining reviews run.

## Final result

- Five sources promoted exactly from independently approved receipts. First pass
  2/5 (Get Started and JavaScript v3 cards). Sale, Webhooks and Control Panel each
  required one targeted correction. Five completed full initial reviews, three
  targeted rereviews, zero full retries, zero coordinator semantic repairs.
  One cards first review was interrupted without a result and restarted; its
  unrecorded effort is not included in completed-review counts.
- Query audit 10/10 PASS, no extra full reads or query repairs. Two new concepts
  and three existing concepts updated; website and GitHub source ownership stay
  distinct. Cumulative source count 21 (16 GitHub plus five website summaries),
  excluding 16 separate GitHub changelog pages.
- Shared company/provider catalog updates complete by 10:30:00Z. Provider log
  added at close. One aggregate mechanical check passed: 12 typed wiki pages,
  all five exact candidate/receipt/source equalities, hashes, canonical URLs,
  raw_files/Raw Sources identity and reverse ownership, approved concept updates,
  reciprocal routes, catalog uniqueness and source count. Mechanical elapsed
  0.610s. No unit suite repeated in this documentation-only campaign.

## Stage timing and limits

| Stage | Observed duration / interval |
| --- | --- |
| Initial worker role time | Sale 2m29s; Webhooks 2m53s; Control Panel 2m17s; cards 1m39s. Get Started start missing, so no complete sum |
| Targeted worker corrections | Sale 1m01s; Control Panel 50s; Webhooks handoff preserved but exact interval unavailable |
| Initial full reviews | Get Started 1m39s; Webhooks 2m43s; Control Panel 2m41s. Sale start and resumed cards start unavailable |
| Targeted rereviews | Sale 47s; Control Panel 28s; Webhooks 1m15s — 2m30s role time total |
| Query audit A | 10:27:00–10:28:58Z: 1m24s analysis plus 34s handoff/report |
| Query audit B | 10:30:27–10:33:02Z: 1m59s analysis plus 36s handoff/report |
| Final audit handoff to operational close | 10:33:02–10:34:27Z: 1m25s, includes report acceptance, log and mechanical close |
| Mechanical validation | 0.610s |
| Total recorded wall time | 2h43m12s, includes interruption and queue/handoff time |

The visible 2h19m04s gap is not a precisely instrumented pause. Subtracting it
leaves 24m08s, but that is only an inter-observation residual, **not** a measured
active-only runtime. Individual role intervals overlap. Promotion/shared-write
time was not separately timed, so no invented duration is supplied. This sample
does not establish a reliable speedup over C46's uninterrupted 21m18s.

## Small next improvement (proposal, not a new rule)

All three first-pass failures were bounded: omitted risk/fraud prerequisite,
lost ACH Direct Debit event qualification, and broadened Dashboard/receipt verbs.
For the next worker prompt, check the subject, qualifying condition and action
of each retained sentence once before handoff, including concept suggestions.
Prefer dropping incidental enumerations over paraphrasing them broadly. Preserve
material prerequisite warnings. This reuses the current retrieval contract;
no new validation layer, memory registry or full-review round is proposed.

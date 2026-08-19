# Metronome Campaign 15 Selection Review

- Status: **completed — 2/3 approved; throughput gate failed; no promotion**
- Purpose: measure a smaller production-shaped workflow without weakening the
  independent semantic gate: Sol workers create three isolated source
  candidates, and different Sol reviewers perform one complete-source review
  focused on source correctness, important omissions, contradictions, and the
  factual validity of concept-update signals.
- Scope boundary: this proposal does not read the raw bodies in full, initialize
  campaign state, spawn workers or reviewers, promote candidates, or edit any
  canonical source, concept, company, index, or log page.
- Selection method: metadata only — raw path, source URL, first heading, line
  count, SHA-256, prior-manifest membership, and source-target existence.
- Selection: three short pricing and packaging guides that are absent from all
  earlier Metronome campaign manifests and have no canonical source page.
- Runtime ceiling: one coordinator plus at most three repository-read-only
  native agents. Slots remain dynamic; a completed worker releases its slot to
  a ready reviewer or the next worker without a batch barrier.
- Models: Sol is used for both worker and reviewer roles. The reviewer must be a
  different agent from the worker for the same page.

| # | Job | Lines | Pilot role |
| ---: | --- | ---: | --- |
| 1 | `target-credit-and-commits` | 176 | short credits/commits guide |
| 2 | `manage-seats` | 194 | short subscription guide |
| 3 | `guarantee-zero-overages` | 205 | short credits/commits guide |

## Simplified review boundary

The worker still reads exactly one complete raw page, extracts three to five
verbatim quotes, and returns one source candidate. It leaves company, index,
and log suggestions empty. It proposes only fact-bearing concept changes,
reciprocal source links, or contradictions that require semantic judgment.

The independent reviewer still reads that complete raw page. The reviewer must
reject material factual errors, unsupported claims, important omissions,
missed contradictions, incorrect raw links, and unsupported or missing concept
signals. It validates the meaning and grounding of a concept signal, but does
not spend time polishing its final shared-page wording or reviewing mechanical
company, index, and log entries.

After all three reviews, the coordinator does not perform a third full-source
read. It groups only reviewer-approved concept signals by exact target and
prepares each shared target once; it derives company, index, and log entries
mechanically. Canonical application remains a separate approval decision after
the pilot result.

## Pass criteria

- All three first-attempt candidates pass the independent complete-source
  semantic review without a material factual correction or important omission.
- A bounded unchanged-hash correction may receive one targeted diff review for
  frontmatter, raw links, formatting, wording, or an already identified field.
  A correction requiring renewed interpretation fails this throughput pilot;
  retries are not used merely to improve its score.
- Hash, canonical URL, quote-substring, fixed result schema, raw backlink, and
  duplicate-link checks all pass.
- Reviewer-approved concept signals can be grouped by target without semantic
  conflict. Any unresolved conflict pauses promotion and requires a narrow
  coordinator decision or additional review.
- Campaign timing uses the existing `started_at` and `completed_at` evidence;
  no new performance-monitoring subsystem is added.

## Decision after the pilot

- `3/3` with no material correction: recommend this narrowed reviewer scope for
  similar low-risk Metronome guide pages, then request approval before canonical
  promotion or a larger campaign.
- Any material correction, missed contradiction, or missing concept signal:
  keep the existing full reviewer workflow for that page class and do not scale
  this optimization.

Explicit approval of this exact manifest authorizes initialization and complete
reads of only these three raw pages. It does not authorize canonical promotion,
API/schema-heavy pages, bulk ingestion, or cross-PSP rollout.

## Outcome

- Runtime: 890 seconds (`2026-08-19T12:18:29Z` to
  `2026-08-19T12:33:19Z`).
- `target-credit-and-commits`: approved after its first complete-source review.
- `manage-seats`: rejected after the first complete-source review found a
  material unassigned-seat error and unsupported concept-signal grounding.
- `guarantee-zero-overages`: the source interpretation was materially accurate;
  one unchanged-hash targeted retry repaired quote coverage and USD-scaling
  links, then passed targeted review.
- Totals: three full reviews, one targeted review, zero coordinator repairs,
  two approved jobs, and one rejected job.
- The required `3/3` gate did not pass. No candidate, concept signal, company
  entry, index entry, or log entry was promoted to the canonical wiki.

The detailed decision is in `pilot-verdict.md`.

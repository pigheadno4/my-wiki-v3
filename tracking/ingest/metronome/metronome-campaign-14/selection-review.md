# Metronome Campaign 14 Selection Review

- Status: **completed calibration — gate failed; no promotion**
- Purpose: test whether one Sol-medium full-read worker plus deterministic and
  lightweight coordinator checks can replace routine per-page reviewers.
- Production hypothesis: one Sol-medium worker per raw page; the coordinator
  checks receipts, formatting, links, duplicates, and shared-file proposals but
  does not reread the complete raw page.
- Calibration only: all five candidates receive independent Sol-high full-source
  review after worker completion. This is a one-time quality measurement, not
  the proposed production workflow.
- Selection method: five fresh pending-source pages absent from every earlier
  Metronome campaign manifest and from `wiki/sources/metronome/`.
- Inspection performed: path, source URL, first heading, line count, file hash,
  and source-page existence. A header check also exposed the opening paragraph of
  `hybrid-business-models`; it did not influence selection. No complete raw read,
  ingest, or semantic body analysis occurred.
- Runtime: one coordinator and at most three repository-read-only Sol-medium
  workers. Reviewers are repository-read-only; only the coordinator owns state
  and canonical writes.
- Promotion gate: no candidate is promoted until all five calibration reviews
  pass with zero material factual error or omission.

| # | Job | Lines | Sample role |
| ---: | --- | ---: | --- |
| 1 | `hybrid-business-models` | 389 | standard guide and fixed audit sample |
| 2 | `asc-606-revenue-recognition` | 555 | complex financial guide |
| 3 | `netsuite-integration` | 456 | integration/configuration and fixed audit sample |
| 4 | `list-invoice-breakdowns` | 1,133 | schema-heavy API and fixed audit sample |
| 5 | `discounting-on-commits` | 426 | ordinary pricing guide |

## Pass criteria

- Zero material factual inversion, unsupported durable claim, important omission,
  or missed contradiction across all five independent reviews.
- Deterministic failures in hash, canonical URL, quote substring, frontmatter,
  raw backlink, schema, or duplicate links are not accepted.
- Bounded mechanical corrections are allowed and counted separately; any fix
  requiring renewed interpretation of the raw page fails the no-review hypothesis.
- A passing pilot authorizes a later production proposal using Sol-medium workers,
  lightweight coordinator review, and only a fixed three-page campaign audit.
  It does not itself authorize bulk ingestion or cross-PSP rollout.

Approval authorizes initialization and complete reads of only these five raw
pages by their assigned Sol-medium workers, followed by one independent Sol-high
calibration review per page. It does not authorize canonical promotion until the
five-page gate passes.

## Outcome

- The approved manifest ran on 2026-08-05.
- Result: `0/5` pages met the no-review gate.
- Four first reviewable candidates required substantive full-source correction.
- `list-invoice-breakdowns` first failed deterministic quote-substring validation;
  after a quote-only resubmission, its full-source review also required substantive
  correction.
- No candidate was promoted and no canonical source, concept, company, index, or
  log page was changed by this campaign.
- The detailed evidence and production decision are recorded in
  `pilot-verdict.md`.

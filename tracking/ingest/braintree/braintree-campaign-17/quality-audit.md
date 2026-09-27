# Braintree C17 quality and close audit

## Outcome

The exact ten-page Control Panel manifest has ten independently approved jobs and ten promoted website sources. Five fixed query groups cover all twenty predetermined navigation/detail questions: **20/20 PASS after one bounded cross-page repair**. Group A and B reports retain their initial consistency-fail finding and the subsequent repaired verdict; Groups C–E passed without repair.

## Review and correction evidence

- Sixteen worker starts produced fifteen valid candidates and one invalid Webhooks handoff (`status: completed` rather than `candidate_ready`). The runtime recorded `worker_result_invalid`; its documented `retry_job` path queued attempt 2. The corrected handoff was validated and then received its first **full** independent semantic review. No invalid candidate was promoted.
- Fifteen independent semantic reviews comprised ten full first reviews and five targeted reviews of bounded corrections on unchanged raw hashes. Five full reviews requested corrections to quote coverage or concept-route wording; their five targeted retries were approved. All jobs finished approved within the three-attempt limit.
- Concept suggestions were promoted only after their exact update IDs were approved, and before their corresponding source pages. Company and provider catalogs were updated once after all ten jobs. No worker/reviewer edited the repository.

## Cross-page eligibility repair

Reporting Overview raw lines 39–44 say the Transaction-Level Fee Report is US-only. The dedicated Fee Report raw lines 17–18 instead say default availability is US/Australia for IC+ and US/Australia/Brazil for flat-rate or blended pricing. Both belong to the 2026-09-16 collection; neither establishes current eligibility or supersedes the other. Group A/B audits identified that both initial promoted sources stated their own raw accurately but omitted the contradiction.

An independent narrow review approved reciprocal `Collected eligibility conflict` warnings and the provenance treatment. The coordinator added each fully read opposing raw as the second `raw_files` entry and under `## Raw Sources`, and removed the dedicated fee raw from the overview's navigation-only references. The exact post-audit diff from the two original approved candidates consists only of those paired warnings and raw-evidence links/frontmatter changes. The immutable candidates, receipts and first reviews remain historical evidence. These are **two coordinator-repaired source pages**; the other eight canonical sources still equal their approved candidates byte for byte. No other source or concept meaning was changed by the repair.

## Mechanical close evidence

- All ten pinned raw SHA-256 values and canonical URLs match the manifest and source provenance. Each of the ten primary raw paths has one canonical owner; the two additional raw references above are explicitly supplemental conflict evidence. Every final receipt equals its candidate, each receipt has three to five verbatim quotes present in its pinned raw, and all approved concept snippets occur exactly once.
- Root → Braintree index → concept → source → path-qualified raw routes resolve. The company and provider index each list the ten C17 sources exactly once. `wiki/sources/braintree/` contains **125 website + 16 GitHub = 141** source pages, matching `source_count: 141`; changelogs are excluded. `raw/braintree/` has no working-tree changes.
- `scripts/validate_wiki.py` checked the ten sources, four touched concepts, company and provider log: **OK, 16 files, no issues**. Scoped `git diff --check` passed for tracked C17 wiki edits; fifteen untracked C17 source/query-audit files passed trailing-whitespace checks. The five reports contain four explicit PASS question verdicts each.
- This was documentation-only work. No code/rule changes or full code test suite were introduced; no Metronome-specific capsule validator was claimed for Braintree.

No raw collection, GitHub ingest, commit, push or next campaign is part of C17 execution.

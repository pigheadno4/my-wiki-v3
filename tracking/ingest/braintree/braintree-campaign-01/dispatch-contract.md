# Braintree C01 dispatch contract

Status: exact manifest execution approved by the user on 2026-09-19.
Runtime provider-path support is ready. See selection-review.md.

Initialize using this manifest. Every subsequent CLI command uses
`--campaign braintree/braintree-campaign-01`; a bare campaign ID intentionally
retains the legacy Metronome default. Do not change the stored campaign_id to
include the provider prefix.

Read CLAUDE.md, rules/ingest.md, rules/psp/braintree-ingest.md, its explicitly
adopted retrieval contract and the exact trusted role order. Provider-specific
substitutions in braintree-ingest.md take precedence over Metronome names.

Use gpt-5.6-sol medium workers and different gpt-5.6-sol high initial reviewers.
At most three active child roles combined, bounded by actual capacity; no fixed
batch barrier. Prefer ready reviews while keeping one worker active when work
remains. Prioritize bounded targeted corrections within each role queue. Do not
interrupt active roles or waive gates to fill a slot.

One pinned raw per job, fully read before drafting/review. Retain three-to-five
exact located quotes and existing candidate/suggestion/receipt/review schemas.
External handoff artifacts only for workers/reviewers; coordinator is the only
repository writer. Source claims serve retrieval, not exhaustive schema copying.
Preserve material warnings and SDK/version/client-server distinctions. Review
against that same scope; optional detail remaining discoverable in raw does
not itself justify rejection.

Use targeted correction/review only when prior findings, unchanged evidence and
the actual diff bound impact. Broad misunderstanding or uncertain impact needs
full review. Maximum three attempts under the existing failure transitions.
Never silently repair semantics in coordinator promotion.

Incrementally promote only independently approved concept suggestions followed
by the exact approved source. Group company/index/log/count writes once at
close, preserving concurrent GitHub work. Check source/candidate equality,
pinned hashes, canonical URL, raw forward links and raw_files reverse lookup,
approved concept reciprocal routes, catalog uniqueness and actual source count.
Run existing generic typed-page validation on touched typed wiki pages, not
frontmatter-free indexes. Do not run a Metronome-only capsule check on Braintree.

Run the ten predeclared questions once, with compact answer-and-locator output,
requested object/action checks and query-rule gap sweeps. Every evidence file
selected to answer a detail question must be fully read. Correct concrete
failures; do not add another three-page audit or rewrite passing reports for style.
Record stage times as observed, not reconstructed from untimestamped events.

No collection/retry, GitHub ingestion, raw edits, new scheduler/registry,
automatic next campaign, commit or push.

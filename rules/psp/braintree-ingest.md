# Braintree website-document retrieval pilot

Scope: completed `braintree-campaign-01` and preparation of `braintree-campaign-02`,
each with its own exact manifest and dispatch contract under
`tracking/ingest/braintree/<campaign-id>/`. C02 preparation is approved;
execution requires separate approval of its pinned manifest. C01 remains closed.
Provider-path support is verified; this is not bulk rollout authority.

Read `CLAUDE.md` and `rules/ingest.md`. For this pilot, adopt the retrieval
semantics and role controls in `rules/psp/metronome-ingest.md`, with these
explicit provider substitutions only:

- Provider: Braintree, not Metronome. The Metronome document supplies workflow
  instructions, never evidence for Braintree product claims.
- Raw root: `raw/braintree/`; website source root: `wiki/sources/braintree/`.
- Navigation: `wiki/index.md` → `wiki/braintree-index.md` → relevant concept.
- Company: `wiki/companies/braintree.md`; operation log: `wiki/braintree-log.md`.
- Tracking: `tracking/ingest/braintree/<approved-campaign-id>/`.
- Use the five jobs and ten questions in this campaign, not any Metronome list.
- Do not run the Metronome-specific capsule validator against Braintree or
  claim that it validates Braintree. Use existing generic typed-page validation
  and the same explicit hash, candidate, link, catalog and count checks.

This is a provider-specific authorization for the parallel-review exception
once the exact manifest is approved and the runtime blocker is resolved.
Use Sol medium workers and different Sol high initial reviewers, at most three
dynamic child slots in total, and coordinator-only repository writes. Keep
complete raw reads, three-to-five located quotes, per-source approval, bounded
targeted corrections, maximum three attempts, and incremental promotion of
individually approved concept updates followed by their source candidates.
Aggregate company/index/log/count changes once at close. No reviewer waiver.

Preserve concrete SDK language/version and client/server scope. A collected
SDK fallback is evidence only for that concrete variant, not its failed parent
or sibling variants. Website docs and GitHub source capsules remain separate
source owners: link to existing concepts where relevant, investigate discovered
conflicts, but do not rewrite or ingest GitHub work items in this campaign.
Never infer current support from collection success or immutable storage.

Sources are retrieval entries, not replacement API specifications. Preserve
central meaning and material warnings; route routine parameters, examples and
tables to verified raw locations. Concepts default to useful reciprocal routes
rather than copied detail. Add a concept only when the existing concept audit
finds a genuine topic gap. Keep fully read evidence under Raw Sources and
unread navigation under Related raw API references. Derive raw-to-source
lookup from `raw_files`; do not modify raw.

## Worker handoff self-check (approved after C01)

For future separately approved Braintree campaigns adopting this guidance,
make one bounded pass over the retained source sentences and concept suggestions
before handoff. Check each sentence's **subject, qualifying conditions, and
action** against its supporting raw passage. Preserve SDK/version, payment-method
and event scope; do not turn navigation into a capability or a specific setup
action into a general feature. C01 examples: retain **ACH Direct Debit** when
describing transaction-status notifications; distinguish **links to reports**
from summarizing reports; retain **enabling email receipts**, not generic receipts.
Also check that a material prerequisite for a retained capability remains
discoverable, such as the supporting-data prerequisite for risk/fraud tools.

If an incidental detail is unnecessary for retrieval, remove it rather than
broaden its wording; never remove a consequential warning or prerequisite merely
to shorten the source. Use the already-read evidence and inspect the relevant
passage when needed. This is part of drafting, not another full raw read,
separate checklist artifact, result field, validator, or reviewer round. It does
not retroactively change C01's approved artifacts or authorize a next campaign.

No collector repair, collection retry, new registry/scheduler, historical
rewrite, commit, push, or campaign beyond the explicitly approved scope is
authorized by this document.

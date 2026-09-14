# Metronome retrieval-oriented ingest contract

This is the direct, consolidated entry for future exact-manifest-approved
Metronome campaigns that explicitly adopt it. It consolidates the C37–C39
retrieval workflow; it is not retrospective authorization for another campaign.
Read with `CLAUDE.md`, `rules/ingest.md`, the provider router, the approved
campaign selection/manifest and the unmodified trusted role order. Historical
contracts and attempts are not prerequisites or factual evidence.

## Precedence and fixed controls

Within an adopting campaign, this contract supersedes conflicting legacy
semantic preflight: exhaustive concept fan-out, mandatory schema completeness,
unconditional per-POST idempotency expansion, cross-API analysis of details left
in raw, and automatic full rereview of every factual wording correction.
Do not edit trusted order identity/schema values to implement this override;
attach this named contract to both worker and reviewer dispatches.

Preserve one completely read raw per source, exact canonical URL and SHA-256,
three-to-five located verbatim quotes, existing result schemas, independent
initial review, coordinator-only repository writes, and at most three attempts.
Use Sol medium workers and different Sol high reviewers, per-page review, and
three dynamic native-agent slots beside the coordinator, bounded by actual
available capacity. No Luna/Terra substitution, reviewer waiver, new result
fields, classifier, registry, worktree requirement, or monitoring subsystem is
introduced.

## Worker: accurate retrieval entry, not full specification

Read the entire assigned raw before writing the candidate. Use its sections by
their role while reading; do not emit a separate segmentation artifact:

| Content role | Treatment |
| --- | --- |
| Identity, purpose, intended use | Summarize accurately with useful query vocabulary |
| Central capability or transition | Retain enough meaning to select the right evidence |
| Explicit deprecation, destructive effect, consequential limit | Preserve a short warning when omission risks misuse |
| Fields, enums, examples, error tables, setup detail | Default to a category and verified raw locator, not copied field lists or schema analysis |
| External/API-wide authority | Link when useful; read it if needed for a retained claim or discovered conflict |

For each proposed source assertion, ask whether it helps select the correct
operation, understand its central effect, or avoid material misuse. If none
applies, omit the assertion and provide a verified raw-detail locator where
useful. Apply this test while drafting, not through a separate analysis artifact
or repeated shortening pass. Required-field lists, enum values, pagination
bounds, response-property inventories and generic errors are not default source
content. For example, retain "product type cannot be changed"; do not append
a catalog of unpromised downstream outcomes or generic response fields.
There is no hard word limit: preserve every consequential warning needed for
the retained meaning, and do not rewrite accepted sources just to shorten them.
Keep consequential warnings and discovered conflicts that affect safe use;
narrowing a claim must not hide those warnings. Preserve explicit BETA/preview,
version, example, time and modal qualifications of retained behavior. Do not turn an example into
a guarantee or an available action into a requirement. Distinguish enclosing
OpenAPI request-body requiredness from required payload properties; infer no
runtime behavior from absent schema constraints. Omit unnecessary assertions
instead of enumerating hypothetical unknowns. Give the shortest verified
heading, operation or schema locator sufficient to find the detail. Do not
describe inline versus referenced placement unless useful; any placement claim
that is retained must be checked against the raw.

Read related authority only to substantiate a retained cross-source claim or
investigate a discovered relevant conflict, not every adjacent API. Keep known
conflicts affecting retained claims visible with a short warning and evidence
routes; resolving them is not required. Raw immutability preserves provenance,
not upstream correctness or current applicability. Unread related documents
provide navigation only, never factual evidence.

Use the source schema in `CLAUDE.md`: undated source slug, correct frontmatter,
`canonical_url` copied exactly from the order, and nested raw paths relative to
`raw/` in `raw_files`. Include exact path-qualified `[[raw/...]]` links under
`## Raw Sources` for fully read evidence; put unread navigation-only raw under
`## Related raw API references`. Keep history newest first on a separately
approved refresh. Never edit raw to add reverse links: derive reverse lookup
from `raw_files`.

Return exactly the trusted result-contract keys with nonempty quote text and
location, source candidate and supported suggestions. For each quote, verify
its location against the pinned raw: use an unambiguous heading/schema path
or line numbers obtained from `rg -n` / `nl -ba` output, never estimated from
memory or an excerpt's relative position. Confirm the quoted text occurs at
that location; disambiguate repeated text with its enclosing section. Keep the
existing location string and result schema. Use only
`durable_fact` or `reciprocal_source_link` update kinds; represent contradictions
in proposed text/warnings. Leave company/index/log suggestion arrays empty.
Workers and reviewers may write their assigned external handoff artifacts but
must not edit repository files or run coordinator transitions.

## Concepts: index-led, purpose-fit, reciprocal

Start at `wiki/index.md` → `wiki/metronome-index.md` to select the main concept.
Read its relevant section and navigation, plus enough context to detect an
overlap or contradiction. A valid link alone does not prove relevance; indexes
and concepts are navigation aids, not factual authorities. Read an adjacent
concept only when needed for a meaningful route or actual conflict.

Default to the main concept's reciprocal source link with a one-line purpose;
do not copy source-level field lists, enum tables or response shapes into it.
Add supporting routes for retrieval value, not incidental fields. Change
concept prose only when a definition, principal flow or important existing
statement changes; otherwise propose navigation only.
A supported fact citation can supply the main reciprocal route without a second
Sources entry. Review uniqueness within the intended navigation section;
a separate supported inline citation is not automatically a duplicate.

## Independent reviewer and bounded corrections

For every first attempt, a different reviewer reads the complete assigned raw,
candidate, quotes and shared suggestions. Apply this same retrieval contract.
Check retained claim truth, purpose/object/version, consequential warnings,
discoverable central topics, exact provenance/detail locators, and semantic
validity and reciprocal placement of proposed updates. Do not reread whole
company/index/log files or unrelated concept sections.

Block false/misleading retained claims, wrong identity or scope, missing
material warnings or known conflicts, undiscoverable central topics, and broken
required evidence/navigation routes. Apply the same detail-retention test to
source and concept proposals; do not demand optional schema expansion merely
because the raw contains it. Every omission blocker must name a
concrete query, the misleading answer/wrong selection, and why the raw route
cannot adequately cover it. Ordinary detail remaining in raw, optional global
rules, tangential concepts and style preferences are nonblocking.

Before returning changes_requested, make one blocker-completeness pass within
this scope and return all visible blockers together. Prefer the smallest fix:
narrow/remove a claim, restore a qualification, add a warning or repair a route.
Use existing review-result keys; approval may list shared update IDs as strings,
while rejected updates carry verdict/reason objects.

Use targeted review when unchanged evidence, prior findings and the actual diff
bound the impact, even when a factual sentence changes. Reuse the original
worker/reviewer where available and inspect only corrections, evidence/context
and affected suggestions/links. Unchanged hash alone is insufficient. Use full
review for central misunderstanding, broad meaning changes, changed evidence,
unresolved broad contradiction, or impact that cannot be bounded. Never waive
the first review or silently let the coordinator perform a semantic repair.

## Coordinator: dispatch, promotion, closure

Pin exact raw paths/hashes, source targets and the predetermined questions before
approval. Use available metadata, length and semantic risk to order the manifest
before dispatch; short pages can still cross important authority boundaries.
No metadata assessment replaces the full raw read.

Use existing runtime/orders/receipts. Persist each trusted order, immediately
dispatch its native agent and confirm an agent ID before processing another
completion. Reconcile interrupted dispatch rather than issuing duplicate work.
On completion, accept the handoff through existing required validation and
state transitions, then fill an available slot with eligible work before
promotion, retrospective prose or routine progress reporting. Persist the next
trusted order before dispatch; never skip approval gates or dispatch unresolved
work merely to keep a slot busy. Keep required timing observations at the event,
but defer their narrative. Prepare short role instructions and approved paths
ahead of time; the emitted trusted order remains authoritative. Do not create
another queue, dispatch artifact or monitoring field for this preparation.
The dynamic pool has no batch barrier:

- Subtract all active workers, reviewers and auditors from actual capacity.
- Prefer ready reviews, reserving one worker slot only if work is queued and no
  worker is active; otherwise an active worker satisfies that reserve.
- Fill remaining capacity with queued workers. Never reserve idle reviewers or
  start more reviewers than ready candidates.
- Within each role's queue, prioritize existing `targeted` corrections/reviews,
  then use `queue_position` within each priority group. Full retries and first
  attempts retain ordinary queue priority. This does not change review-first
  slot allocation, worker reservation, attempt limits, or running assignments;
  never preempt active work. No new priority field is required.

Only the coordinator writes canonical sources, shared files, tracking and
commits. Promote only independently approved jobs: serially apply that job's
approved concept updates, then its exact source candidate. Resolve shared-target
overlap without broadening approved meaning; seek narrow review for an actual
conflict. Apply each approved update once. Pause stops new promotion while
preserving accepted pages and attempt evidence. Follow the existing bounded
failure/retry/rejection state transitions; do not restart failed historical jobs.

Aggregate company/provider-index/provider-log/count changes once at close.
Derive catalog entries from approved sources, retain all intended reciprocal
routes, and enrich existing index descriptions with useful query vocabulary.
No separate shared-close agent or default third coordinator full-raw review:
reread only disputed/uncertain evidence or material unresolved risk. Mechanical
repairs do not require semantic rereview unless meaning changes.

For the separately approved five-page confirmation, keep three manifest
audit_job_ids as exemplars and run the ten predetermined navigation/detail
questions as one final audit, not an additional three-page full-content audit.
Start from index → concept → source → exact raw; detail answers read the raw
fully under `rules/query-and-synthesis.md`, including its existing gap-sweep
requirements. Record route, evidence, extra searches, verdict and repairs.
During this campaign audit's gap sweep, discovering an older snapshot of the
same canonical page does not itself require reading it. Select historical raw
when the question asks about history/version differences, a discovered relevant
conflict needs investigation, or answering the question otherwise requires it.
Record that reason briefly with the existing extra-read notes. Do not infer
historical equivalence or absence of changes from metadata or unread content.
Every selected evidence file must still be read completely; this does not
reduce the worker's or initial reviewer's complete pinned-raw read, or skip
related/unlinked evidence needed to answer the question.
Before answering each question, restate its requested object/action and check
that the source/raw reached through navigation matches it (for example, commit
is not credit). Record this beside the route in the existing audit report,
without a new schema or checklist file. The coordinator checks this identity
against the assigned question before accepting the verdict. A wrong-object
audit answer is invalid: correct only affected questions, preserving unrelated
valid results and distinguishing auditor error from a genuine retrieval failure.
Write the audit directly into the existing Markdown report: one actual route
per page, then one concise entry per question containing object/action match,
direct requested answer, exact raw locator and PASS/FAIL (or unresolved verdict).
Do not draft a long report and then summarize it. Reuse the route and evidence
locator when unchanged; record a different route if one was needed.
For questions asking where fields are documented, give the verified schema
locator rather than copying its inventory; when a question asks for specific
field values or semantics, answer those explicitly from the evidence.
Record shared gap-sweep
results, extra full reads and reciprocal-link checks once per group; expand
only concrete failures or material uncertainty. Omit repeated pass rationales,
conclusions and optional schema inventories. Keep material qualifications in
the direct answer. This shortens reporting, not required
reading, checks or question coverage. After one completeness check, hand off
the report without stylistic polishing; distinguish analysis end from final
handoff time in the existing timing notes.
Disjoint groups may overlap remaining promotions; do not repeat tasks.
Failed retrieval or wrong answers block successful closure; resolve them or
record a failed pilot, never expand source detail merely to pre-answer raw
queries. Larger samples or changed audit policies need separate approval.

At close, check all promoted source/candidate equality, raw hashes, exact and
reciprocal links, duplicate catalog entries, approved-update presence, provider
counts, touched typed wiki files and capsule consistency once; correct concrete
failures without rerunning unrelated semantic reviews. Treat frontmatter-free
indexes as routers, not typed pages. Run existing unit tests when code, rules
or validators change, not after every documentation-only source.

Use existing monitor, receipts, audit and retrospective for first-pass rate,
attempts, full/targeted reviews, word counts, retrieval misses and elapsed time.
started_at/completed_at measure operational closure. Journal events without
timestamps do not establish stage durations; use explicit UTC observations when
requested and distinguish overlapping windows, queueing and post-close reporting.
Commit only the approved scope when authorized; no automatic push, collection,
next campaign, bulk migration or cross-PSP rollout.

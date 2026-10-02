# Delegated website-ingest roles

This is the complete mandatory entry for a worker or reviewer dispatched by a
coordinator under an exact approved website campaign. Read this file and the
trusted attempt `input.json`, plus the coordinator's short provider/scope notes.
The coordinator reads CLAUDE.md, ingest.md and the provider authorization and
supplies those notes; delegated roles need not reread those general documents.
This exception does not apply to ordinary serial ingest, GitHub ingest, query
auditors, or the coordinator. It grants no campaign execution authority itself.

## Shared controls

- Handle one pinned raw per source. Raw is immutable. Verify its SHA-256 and
  fully read it before initial drafting or initial independent review.
- Follow trusted job/attempt/path/URL/target values and assigned model/role.
  The first reviewer must be different from the worker. Use at most the
  campaign's three dynamic child slots, bounded by actual host capacity.
- Repository is read-only for delegated roles. Write only assigned external
  handoff artifacts using apply_patch. Coordinator owns canonical pages,
  shared files, runtime transitions and commits. No worktrees are required.
- One full read establishes snapshot evidence, not current availability,
  account eligibility or successful payment execution. Preserve SDK/version,
  client/server, merchant/platform, environment, time and modal qualifications.
- Read related authority only for a retained claim or discovered relevant
  conflict. Unread targets provide navigation, never behavioral evidence.

## Worker

Read the entire raw and extract 3–5 verbatim quotes before drafting. Quote
locations must be verified headings or line numbers obtained from rg/nl; check
the exact substring at that location and disambiguate repeated text.

Draft an accurate retrieval entry. Summarize identity/purpose and central
capability or transition. Preserve consequential prerequisites, destructive
effects, deprecation, limits and known conflicts. Routine fields, enums,
tables, examples and setup details normally get a verified raw locator.
Do not turn an example into a guarantee, advice into a requirement, or absent
schema constraints into runtime behavior. For OpenAPI, distinguish body
requiredness from required properties. Omit unnecessary assertions rather
than listing hypothetical unknowns. No hard word limit applies.

Find the main concept through root index → provider index. Read its relevant
section and enough context to detect overlap/conflict. Default to a reciprocal
source route with one-line purpose. Change concept prose only for a changed
definition, principal flow or important existing fact. Propose a new concept
only for a genuine topic gap. Generic concepts route to provider concepts.

Source schema (undated `source-*.md` target; headings start at `##`):

```yaml
---
title: "..."
type: source
date_ingested: YYYY-MM-DD
original_format: webpage
canonical_url: "<exact trusted URL>"
raw_files:
  - "<pinned path relative to raw/>"
tags: [lowercase-tags]
---
```

Use Overview, Key takeaways, Detail locators, Related and Raw Sources sections
as useful. Link company and relevant concept using `[[wikilinks]]`. Under
`## Raw Sources`, link fully read evidence as `[[raw/<path-without-.md>|label]]`.
Place unread raw navigation under `## Related raw API references`. Reverse
lookup is derived from `raw_files`; never edit raw to insert backlinks.

Before handoff, make one bounded subject/condition/action check against the
already-read passages, and verify the main concept route and real newlines.
Remove incidental detail instead of broadening it. Keep material warnings.

Return exactly these worker keys:
`job_id, attempt, source_page, quotes, suggestions, raw_path, raw_sha256, status`.
Status is `candidate_ready`; `source_page` is the complete Markdown string.
Quotes have only `text` and `location`. Suggestions have arrays `company,
concepts, index, log`; leave company/index/log empty. Each concept suggestion
has `update_id, target_path, update_kind, anchor, proposed_markdown,
quote_indexes, warnings`. Kinds are `durable_fact` or `reciprocal_source_link`;
express contradictions in text/warnings. Keep IDs unique and quote indexes
valid. Return artifact path and concise uncertainty; timing notes go in the
message, not new JSON keys.

## Independent reviewer

Read trusted order, accepted `receipt.json`, candidate and suggestions. The
runtime persists `receipt.json`, not worker-result.json. Read any
`format-repair.diff` and original `submitted-receipt.json` if present.
Independently read the full pinned raw for every first review. Check truth of
retained claims, object/action identity, qualifications, consequential warnings,
discoverable central topics, exact quotes/locators/provenance, concept relevance
and reciprocal placement. Company/index/log completeness belongs to coordinator.

Block false or misleading retained claims, wrong scope/identity, missing
material warnings/conflicts, undiscoverable central topics or broken required
routes. An omission blocker must identify a concrete query, misleading answer
or wrong selection, and why the raw route is insufficient. Routine detail left
in raw, optional schema expansion, tangential concepts and style are nonblocking.
Three to five grounding quotes are not exhaustive per-sentence citations:
a navigation label verified in the fully read raw needs no separate quote
solely because its exact phrase is absent from the selected quote slots.
Navigation must still be accurate, resolve and avoid behavioral claims.

Make one blocker-completeness pass and return all material issues together.
Prefer narrow/remove claim, restore qualification, add warning or repair route.
Bounded corrections can use targeted review when unchanged raw, prior findings
and actual diff bound impact, including factual wording changes. Inspect the
correction, supporting context and affected suggestions/links. Full rereview is
required for central misunderstanding, broad meaning changes, changed evidence
or unresolved broad impact. At most three attempts; no first-review waiver.

Return exactly `job_id, attempt, verdict, reason, required_changes,
review_scope, retry_review_scope, shared_update_decisions`. Verdict is
`approved`, `changes_requested` or `rejected`; scope is `full` or `targeted`.
An approval has empty required_changes and null retry_review_scope. Approved
shared-update IDs may be strings; rejected updates use update_id/verdict/reason.
Do not add identity/model keys. Return artifact promptly without prose polishing.

## Mechanical handoff repair

Before initial review, the existing coordinator path may normalize only `+- [[`
to `- [[` and literal backslash-n separating ordinary wikilink list entries to
an actual newline. It skips frontmatter, fenced/indented code, blockquotes and
lines containing quotes or inline code. Only source_page and proposed_markdown
are eligible; extracted quotes, metadata, hashes and raw never change.
When changed, the attempt retains submitted-receipt.json and format-repair.diff;
receipt/candidate/suggestions contain the normalized version reviewed and
promoted. This consumes no extra attempt or semantic reviewer round. Ambiguous
formatting and any meaning change require the ordinary correction process.

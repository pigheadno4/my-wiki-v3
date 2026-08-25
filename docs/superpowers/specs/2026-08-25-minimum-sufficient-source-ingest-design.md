# Minimum Sufficient Source Ingest Design

**Date:** 2026-08-25
**Status:** User-approved design; written specification awaiting final review
**Initial pilot:** Metronome Campaign 23
**Future scope:** Stripe, Adyen, PayPal, Braintree, and other provider capsules after provider-specific validation

## Goal

Improve first-pass ingest acceptance and reduce repeated complete-source reads by
treating a source page as a reliable query router rather than a second copy of
the raw page. Preserve immutable raw as the complete evidence layer, keep
cross-source durable synthesis in concept pages, and make review block only on
defects that can materially mislead a future query or integration decision.

## Evidence behind the change

Campaigns 20 through 22 reached acceptable final query quality but had very
low first-pass acceptance. Adding archetype reminders improved defect
attribution, not throughput, because worker and reviewer behavior still
favored exhaustive reconstruction of the raw page and broad concept coverage.
That caused secondary schema details, optional concept links, quote ranges, and
wording defects to trigger repeated semantic work.

The new design changes source granularity and the review contract together. It
does not weaken raw collection or the first independent review in the initial
pilot.

## Non-goals

This design does not:

- reduce canonical English raw collection;
- permit partial raw reads by workers or first reviewers;
- change the existing `source_required`, `raw_reference`, and
  `semantic_triage` routing dispositions;
- add a registry, database, scheduler, monitoring service, scoring system, or
  new worktree model;
- cancel independent complete-source review in the first pilot;
- bulk-rewrite the existing Metronome source corpus;
- make secondary concepts or detailed schemas disappear from raw;
- authorize cross-provider rollout before a provider-specific pilot.

## Knowledge-layer responsibilities

### Raw page: complete evidence

Raw preserves the complete canonical documentation and immutable historical
versions. It remains the final authority for fields, enums, examples, limits,
errors, and low-level API behavior. Every generated source provides an exact
raw backlink so a future query can deepen from the curated summary into the
full evidence.

### Source page: query router

A source page contains the minimum durable knowledge needed to:

- determine whether the page is relevant to a query;
- avoid a materially wrong conclusion;
- identify the primary concepts involved;
- recognize important boundaries and contradictions; and
- navigate to the exact raw page for detailed evidence.

It is not expected to reproduce every schema property, optional field, enum,
example, error, or unknown behavior.

### Concept page: cross-source synthesis

Concept pages preserve stable knowledge that helps queries across several
sources. A worker identifies only the concepts primary to the assigned page.
Secondary concept suggestions may be returned for coordinator consideration,
but their omission does not fail the page.

### Company and provider indexes: discovery

Company pages and provider indexes remain exhaustive catalogs of canonical
source pages. They do not duplicate source facts. The coordinator owns these
shared files and updates them once per campaign.

### Campaign evidence and provider lessons: process state

Campaign files preserve orders, attempts, receipts, reviews, failures, and
closure evidence. A small provider-owned lessons file records repeated process
mistakes. Neither campaign tracking nor lessons is a product-knowledge source.

## Minimum Sufficient Source contract

All five document archetypes use one logical source contract. The existing
frontmatter conventions remain intact, including `title`, `type`,
`date_ingested`, `original_format`, `canonical_url`, `raw_files`, and `tags`.
The body contains the following logical sections.

### Overview

One concise passage states what the page is for, the object or lifecycle stage
it applies to, and any important scope exclusion.

### Core facts

Normally three to seven durable facts capture the operation, state change,
principal inputs and outputs, lifecycle result, or material financial,
failure, propagation, and idempotency semantics. This is a semantic budget,
not a validator-enforced numeric limit.

### Boundaries and contradictions

Normally one to three material boundaries preserve an official-document
conflict, a prose-versus-example conflict, an important undocumented behavior,
or a conclusion that the page does not authorize. Ordinary optional fields and
low-impact unknowns do not need exhaustive enumeration.

### Coverage map

The coverage map names the detailed topics available in the exact raw page,
such as the complete request/response schema, enum catalog, errors, pagination,
webhook payload, SQL, or worked example. It is navigation, not a substitute
summary and not evidence from an unread related page.

### Related concepts

The source normally links one to three primary concepts. A page may have more
when its actual subject requires them; the range is guidance, not a hard cap.

A concept is primary when it directly defines the page purpose, operation,
lifecycle, or integration outcome and its omission would impair a realistic
query. A concept is secondary when it reflects an optional field, incidental
schema surface, or tangential capability that raw navigation can safely cover.

### Sources

The page preserves the official canonical URL, `raw_files` version list, and
an exact path-qualified raw backlink. `Raw Sources` contains only pages read
completely and used as evidence. Navigation-only pages remain separately
labelled `Related raw API references` under the existing evidence boundary.

### Inclusion test

A candidate fact belongs in the source body when one or both of these are
true:

1. omitting it can cause the query agent to select the wrong page or answer
   incorrectly; or
2. it changes an integration decision, amount, state, lifecycle, or failure
   treatment.

If neither is true and the coverage map can accurately route the reader to
the raw detail, the fact normally stays only in raw.

## Archetype overlays

An overlay guides reading and review but does not create a new schema,
frontmatter format, routing disposition, or compound document type. Each page
has one primary archetype based on its principal query use. It may borrow an
adjacent checklist item when needed.

### API Read

Preserve the object identity, lookup purpose, key locator, returned state,
time-view or history semantics, and any material visibility or consistency
boundary. Route complete response schemas, nullable fields, examples, and
error catalogs to raw. Distinguish a required property inside a supplied
payload from a required request body or runtime behavior.

### API List / Schema

Preserve collection scope, principal filters and pagination model, documented
ordering or time-window behavior, completeness limits, and material
schema-versus-example conflicts. Route the complete filter catalog, cursor
fields, enums, and object schema to raw. Do not infer closed-schema behavior
without explicit `additionalProperties: false` authority.

### API Mutation

Preserve the precondition, principal state transition, observable result, and
material lifecycle, billing, invoice, failure, propagation, retry, concurrency,
or idempotency semantics established by official authority. Route the full
payload, optional parameters, examples, and error catalog to raw. An endpoint
that uniquely establishes required fields or durable failure/propagation
semantics retains those facts even when otherwise schema-heavy.

### Concept / Guide

Preserve the concept definition, principal actors, lifecycle or data flow,
decision points, material integration limits, and meaningful conflicts with
API or worked-example evidence. Route long examples, operational walkthroughs,
variants, calculations, and low-frequency edge cases to raw. Do not promote a
product guide into legal, accounting, or compliance authority.

### Integration Guide

Preserve the integration outcome, system boundary, responsibility split,
identity mapping, state or data flow, material recovery behavior, and relevant
environment or version scope. Route detailed setup steps, UI paths, payloads,
optional provider settings, and troubleshooting catalogs to raw. Do not treat
Metronome documentation as a complete guarantee of the external platform.

## Review and retry contract

### First review

For the initial pilot, a different strong-model reviewer reads the complete
assigned raw page and relevant authority/context. The complete read determines
whether the compressed source is safe; it does not require the source to
reconstruct the raw page.

### Blocking defects

Only these defects produce `changes_requested`:

1. a core factual error;
2. omission that changes an integration, amount, state, lifecycle, or failure
   decision;
3. treating an example, inference, or secondary source as durable official
   authority;
4. omitting a material contradiction;
5. a missing or incorrect primary concept;
6. an incorrect canonical/raw link that prevents evidence deep dive; or
7. a coverage-map omission that hides an entire detail category central to the
   page's purpose.

### Non-blocking defects

The reviewer approves with coordinator actions for secondary concept gaps,
ordinary fields/enums/examples absent from the source, non-material wording,
formatting or ordering, mechanically repairable quote ranges, shared catalog
updates, and coverage-map wording that does not change factual routing.

These defects do not consume a worker retry.

### Retry scope

- A bounded correction covers a local factual omission, link, format, wording,
  quote range, or identified field while the raw hash is unchanged. Review
  checks only the authorized diff and its context.
- A full semantic retry covers core misunderstanding, material omission,
  authority confusion, new factual meaning, or unresolved contradiction. The
  reviewer rereads the complete source evidence.
- A secondary concept omission is a coordinator action, not a retry.

The existing maximum of three worker attempts remains. If the same blocking
defect survives a second correction, the coordinator first checks whether the
trusted order is unclear. A third materially defective attempt is recorded as
failed or rejected while unrelated campaign jobs continue.

### Coordinator boundary

The coordinator accepts reviewer verdicts, validates handoff contracts,
performs canonical promotion, applies approved shared-file changes, verifies
primary source/concept reciprocity, and runs final mechanical and sampled query
checks. It does not perform a default third complete raw read. Disputed or
uncertain evidence still permits an explicit coordinator reread under the
existing campaign rule.

## Provider lessons

Metronome uses a small coordinator-owned file at:

```text
tracking/ingest/metronome/lessons.md
```

The file has one section per archetype. A lesson is added only when the same
process failure occurs on at least two different pages, can be expressed as a
specific preventive check, and is not already covered by the general ingest
rule or overlay. Each entry contains the concise check, the campaigns where it
recurred, and at most one applicability boundary.

Workers and reviewers read only the section for the assigned archetype. A
one-off page defect remains in its campaign retrospective. Obsolete lessons
are replaced or removed rather than accumulated forever. Product facts,
contradictions, and detailed incident narratives never enter this file.

When the same lesson later recurs across multiple providers, a separate
approved change may promote it into `rules/ingest.md`. No automatic promotion
or registry is introduced.

## Campaign 23 mixed-archetype pilot

### Selection

The manifest selects exactly five un-ingested canonical raw pages: one API
Read, one API List / Schema, one API Mutation, one Concept / Guide, and one
Integration Guide. The sample includes different lengths and complexity,
including at least one schema-misreading risk and one lifecycle or external
system boundary. It must not select only easy pages.

The exact five-page manifest requires separate user approval before execution.

### Controlled variables

Campaign 23 changes source granularity and its review contract only. It keeps:

- the current strong-model worker path;
- a different strong-model full reviewer for every first attempt;
- complete raw reads by both roles;
- current coordinator-only writes and campaign tracking;
- current raw hashes, collection evidence, canonical promotion, concurrency,
  and close-validation approach; and
- no coordinator default third full read.

This isolates whether Minimum Sufficient Source improves throughput without
confounding the result with weaker review.

### Measurements

Use existing campaign state to record first-pass approvals, bounded retries,
full semantic retries, attempts per page, campaign start to final-review time,
fixed query results, exact raw deep-dive success, and primary-concept backlink
completeness. Do not add a telemetry subsystem.

### Quality gate

The pilot closes only when:

- all five canonical sources contain no material factual defect;
- the fixed query audit passes;
- all five sources route precisely to their raw evidence;
- primary concept backlinks are complete; and
- compression has not removed a fact needed for a material integration
  decision.

Efficiency is assessed comparatively rather than by a new hard numeric gate:
first-pass acceptance should improve, full semantic retries should decline,
reviewers should stop blocking on secondary exhaustive coverage, and total
attempts and elapsed time should improve relative to Campaigns 20 through 22.

### Expansion

If quality passes and efficiency improves, run a second five-page pilot that
adds within-archetype variation while retaining complete first reviews. Only
after two stable rounds may reviewer sampling be designed as a separate pilot.

If quality passes without efficiency improvement, do not expand. Attribute
the remaining defects to the worker contract, review contract, or lesson
guidance and make only an evidence-supported correction. If quality declines,
pause the approach and do not authorize cross-provider rollout.

## Incremental migration and periodic updates

Do not bulk-rewrite existing sources. Apply the new contract to new source
generation and migrate an existing source only when:

- its raw hash changes;
- query use exposes a retrieval defect;
- audit finds a material fact, authority, or link problem;
- it enters an explicitly approved migration sample; or
- a primary concept restructuring requires a coordinated source change.

An old source being more detailed than the new profile is not itself a
migration trigger.

Collection continues to preserve every canonical raw version. The canonical
source represents current curated knowledge and records the applicable version
through `raw_files`; campaign evidence records the verified hash. The source is
not duplicated once per historical raw version.

The periodic queue follows both content and approved routing state:

```text
raw hash unchanged
  -> no approved disposition change: no model work
  -> approved raw_reference -> source_required promotion: ingest now

raw hash changed
  -> existing source_required source: read complete latest raw and update
  -> missing source: apply existing routing/triage rules
```

For an existing source, a changed core fact updates the source body; a new
field or enum normally changes only the coverage map; a changed primary
concept updates both links; a secondary concept remains coordinator judgment;
and formatting-only raw changes require no semantic rewrite. Hash and diff
locate changes but never replace a complete latest-raw read.

## Cross-provider rollout

After two stable Metronome pilots, extract only the shared source contract and
overlay behavior. Each provider keeps its own lessons file and runs a separate
five-page mixed-archetype pilot before production use. Metronome-specific
lessons do not automatically become Stripe, Adyen, PayPal, or Braintree rules.

## Acceptance of this design

The design is ready for implementation planning when:

- all source, concept, raw, index, and lessons responsibilities are
  unambiguous;
- the five overlays remain guidance over one source contract;
- blocking and non-blocking review defects are explicitly separated;
- only material semantic risk triggers another complete review;
- Campaign 23 changes no unrelated scheduler, model, or tracking subsystem;
- the exact manifest remains a separate approval gate; and
- migration is incremental rather than a corpus rewrite.

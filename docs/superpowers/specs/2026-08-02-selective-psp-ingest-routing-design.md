# Selective PSP Ingest Routing Design

**Date:** 2026-08-02
**Status:** User-approved; Campaign 12 complete; post-pilot routing amendment approved
**Pilot:** Metronome Campaign 12
**Future scope:** Stripe, Adyen, PayPal, Braintree, and other provider capsules

## Goal

Keep complete immutable canonical raw collections while generating and
maintaining source summaries only where they materially improve future query
speed, routing, reuse, or semantic safety. Preserve direct raw fallback for
exact API details and make periodic ingest proportional to valuable changes,
not total corpus size.

## Problem

Recent ten-page Metronome campaigns took roughly 43–72 minutes. A source page
normally requires one complete worker read and one independent complete
reviewer read; corrections add more passes. Applying that process to every
CRUD endpoint duplicates precise raw API material and does not scale to larger
Stripe, Adyen, PayPal, or Braintree corpora.

Source pages are a curated query-acceleration layer, not a required duplicate
of every raw page. Raw remains the source of truth.

## Non-goals

This design does not:

- stop complete canonical raw collection;
- weaken the review gate for a source page that is actually generated;
- delete, merge, or bulk-rewrite existing source pages;
- create a numeric scoring system, analytics platform, new scheduler, or
  provider-specific ingest engine;
- treat a related raw link as evidence that its contents were read;
- start Campaign 12 as part of approving or documenting this design.

## Evidence and navigation boundary

An overview source separates two kinds of raw links.

### Raw Sources

`## Raw Sources` lists only raw pages read completely and used as factual
evidence for the source body. Every claim in the overview must be supportable
from those pages.

### Related raw API references

`## Related raw API references` lists relevant raw pages that were not used as
factual evidence. These are navigation targets for future exact-detail queries
and must be explicitly labelled as not summarized.

An overview may say that a related raw endpoint exists and route a reader to
it. It must not state the endpoint's method, fields, limits, side effects, or
other behavior unless that raw page was completely read and promoted through
the normal evidence and review path.

Related raw pages may be selected from an explicit official overview link, an
unambiguous official documentation subtree, or an authoritative collection
inventory/sitemap relationship. A generic keyword match alone is insufficient.

## Routing dispositions

Each canonical raw page has one ingest disposition:

| Disposition | Meaning | Model work |
| --- | --- | --- |
| `source_required` | A durable curated source materially improves queries or semantic safety. | Complete worker read and independent complete review. |
| `raw_reference` | Exact raw is the preferred authority; an overview or query sweep provides discovery. | No routine model work. |
| `semantic_triage` | Metadata is insufficient to decide safely. | One complete strong-model read; generate a source only when the decision is `source_required`. |

The coordinator initially classifies pages from canonical URL, title,
documentation hierarchy, sitemap/navigation relationships, page type,
existing source coverage, and risk category. It does not read every raw body
to build the routing list.

### Default `source_required` signals

- Official overview, concept, architecture, how-it-works, workflow, migration,
  or integration guide.
- Cross-endpoint behavior, state transitions, or lifecycle semantics.
- Money, invoices, refunds, disputes, settlement, reconciliation, accounting,
  authentication, security, permissions, webhooks, or idempotency.
- Important limits, warnings, contradictions, irreversible effects, or
  operational boundaries.
- Repeated query use or a demonstrated reusable knowledge gap.

### Default `raw_reference` signals

- One operation under an already-routed topic overview.
- Mechanical create, retrieve, list, update, or delete reference dominated by
  request/response schema.
- Exact fields, enum values, errors, or version-specific reference detail that
  is safer to retrieve from raw.
- No metadata signal of cross-endpoint, lifecycle, financial, security, or
  irreversible behavior.

These signals are insufficient when the endpoint is the only plausible
authority for durable facts that future queries need. A CRUD-shaped or
schema-heavy page does not default to `raw_reference` merely because its facts
are expressed as request fields, validation behavior, or endpoint-local prose.

### Default `semantic_triage` signals

An apparently narrow endpoint whose title suggests cancellation, reversal,
voiding, archiving, regeneration, retry, destructive scope, or another
potentially important side effect. High-risk ambiguity biases toward a source,
not toward silent deferral.

Also use `semantic_triage` when metadata cannot rule out that the endpoint is
the sole authority for required request fields or durable failure,
propagation, deletion, lifecycle, uniqueness, idempotency, or state-transition
semantics. Triage decides whether those facts warrant `source_required`; it
does not assume that every endpoint needs a source.

## Routing authority

Each provider uses one coordinator-owned routing file:

```text
tracking/ingest/<provider>/routing.json
```

Each entry contains only:

- `canonical_url`;
- `disposition`;
- `anchor_source` or proposed `source_target`;
- a concise decision reason.

The routing file does not duplicate the current raw path, collection date, or
raw hash. `tracking/collections/<provider>/inventory-current.json` remains the
authority for those values, and the two files join by canonical URL.

Campaign files remain the authority for one execution's selected tasks,
status, receipts, reviews, and close evidence.

## Ingest queue triggers

Raw hash change is not the only ingest trigger. Model work can be caused by a
content change or an approved routing change.

For `source_required`:

```text
needs_ingest =
    source target does not exist
    OR source does not cover the current raw version
```

This queues a raw-reference page immediately after an approved promotion to
`source_required`, even when its raw hash is unchanged. It can enter the next
authorized ingest campaign or an explicitly approved one-page on-demand
ingest; it does not wait for another collection run.

For `raw_reference`, a raw change refreshes the navigation target after the
collection checkpoint but does not create a source by default.

For `semantic_triage`, a new page, a changed raw version, or a newly assigned
triage disposition queues one complete triage read.

Therefore the no-work condition is:

> No raw content change, no routing decision change, no approved promotion,
> and no source coverage gap.

No separate `promotion_pending` state is required. A query may propose a
promotion; only an approved routing change makes it executable.

## Periodic collection and routing flow

1. Collect every English canonical raw page and preserve immutable versions.
2. Reconcile the current collection inventory and hashes.
3. Join current inventory with provider routing by canonical URL.
4. Queue changed or missing `source_required` coverage.
5. Refresh latest navigation targets for changed `raw_reference` pages after
   collection approval, without changing source facts.
6. Queue new, changed, or newly assigned `semantic_triage` pages.
7. Run approved source ingest and triage tasks.
8. Apply canonical and shared writes once, then run the existing bounded close
   validations.

Collection itself never edits wiki pages. Navigation refresh is a separate,
coordinator-owned post-collection routing step. It updates only the explicitly
marked related-raw section and passes deterministic link/hash checks; it does
not claim that the new raw version was summarized.

## Query-driven promotion

Queries continue to use:

```text
index/concept -> curated source -> exact raw fallback
```

A query may answer directly from a completely read raw page without creating
a source in the same operation. It may recommend promotion when a raw page is
repeatedly useful, contributes durable reusable knowledge, exposes an
overview gap, or contains important boundaries or contradictions.

After approval, routing changes to `source_required`. A missing source target
then queues ingest independently of raw hash.

## Metronome Campaign 12 pilot

The pilot classifies the complete six-page Custom Fields family but reads only
three selected samples.

| Page | Initial disposition | Pilot action |
| --- | --- | --- |
| Custom Fields overview | `source_required` | Complete Sol worker read, candidate, and independent complete Sol review. |
| Create a Custom Field Key | `raw_reference` | No source; one complete Sol audit read to test for a false-negative classification. |
| Delete a Custom Field Key | `semantic_triage` | Complete Sol triage read and independent complete Sol decision review. |
| List Custom Field Keys | `raw_reference` | Navigation only; no complete read. |
| Set Custom Field Values | `semantic_triage` | Record classification only in this pilot. |
| Delete Custom Fields | `semantic_triage` | Record classification only in this pilot. |

The expected maximum is about five complete reads: two for the overview, one
for the raw-reference audit, and two for the semantic-triage decision. The
pilot does not expand to six-page full ingest.

The first pilot reuses the existing coordinator ownership and native agents
but does not modify the scheduler or production campaign schema. Its directory
contains the exact manifest/selection record, a three-row coordinator-owned
monitor, and one final quality audit. Agents write only isolated temporary
artifacts; the coordinator alone writes canonical and tracking files.

### Pilot decision contracts

The overview worker returns a source candidate, three to five grounding
quotes, related raw navigation, and shared-file suggestions. The reviewer
checks that every factual claim comes from the overview raw and that all
related raw links exist without being used as undeclared evidence.

The raw-reference auditor returns only a classification, reason, missed
durable facts, and risk assessment. Discovery of a material hidden semantic
boundary fails that classification and tightens the routing rule; it does not
silently expand the current task.

The semantic-triage worker returns `source_required` or `raw_reference`, three
to five grounding quotes, and a reason. A different Sol reviewer reads the
same raw completely. Disagreement conservatively resolves to
`source_required` and is recorded once without a classification retry loop.

### Pilot quality gate

The pilot passes only when:

1. Overview facts are grounded exclusively in its declared Raw Source.
2. All five related raw links exist and belong to the Custom Fields family.
3. The raw-reference audit finds no omitted material reusable or high-risk
   semantics; otherwise the classification rule is revised and the miss is
   recorded.
4. The semantic-triage decision has an independent complete review;
   disagreement safely promotes the page.
5. Three fixed queries pass: an overview question, an exact create-endpoint
   question that routes to raw, and a delete-boundary question that does not
   invite overview guessing.
6. Touched-page and Metronome capsule validation run once.
7. `started_at`, `completed_at`, and complete-read count are recorded for
   comparison with earlier campaigns.

Elapsed time is an observed outcome, not a reason to waive the quality gate.

## Campaign 12 outcome and routing amendment

Campaign 12 validated the layered ingest architecture but rejected the initial
classification rule for broad provider rollout. The Custom Fields overview was
promoted successfully, while the complete audit of `Create a Custom Field Key`
changed its disposition from `raw_reference` to `source_required`. That page is
the sole evidence in the sampled family for required request fields and for
durable uniqueness, failure, managed-entity, and invoice-propagation behavior.
The independently reviewed delete-key page also resolved to
`source_required` because deletion makes existing values inaccessible.

The correction is deliberately narrow: expand the `semantic_triage` trigger;
do not make every API endpoint `source_required` and do not weaken complete
source review. This amendment does not instantiate a routing registry, mutate
the approved Campaign 12 manifest, reclassify the remaining corpus, or start a
new ingest campaign.

### Worked regression example

```text
Input metadata:
  title = Create a Custom Field Key
  page type = one create endpoint under an existing overview

Unsafe old result:
  raw_reference
  reason = mechanical create endpoint dominated by request schema

Required corrected result:
  semantic_triage
  reason = the endpoint may be the sole authority for required fields,
           validation/failure behavior, uniqueness, or propagation semantics

Observed triage result for this page:
  source_required
  reason = complete reading confirmed durable unique facts
```

The regression passes when the corrected rule prevents the metadata-only
classifier from assigning `raw_reference` directly in this case. It does not
prejudge another endpoint after triage: a page with no unique durable facts may
still resolve to `raw_reference`.

## Multi-provider adoption

The three dispositions, evidence/navigation boundary, queue triggers, query
fallback, and periodic flow belong in the common ingest rules. A provider rule
may add only its risk exceptions and documentation-structure hints.

Examples of likely provider-specific high-risk areas include Stripe invoice
finalization and meter adjustment, PayPal capture/refund/dispute/subscription
lifecycle, Adyen webhooks/modifications/settlement/platform balances, and
Braintree vault/transaction/3DS/recurring behavior. These are routing hints,
not factual claims about a page that has not been read.

Each new provider runs one bounded calibration pilot across all three
dispositions. Routine cycles do not repeat that pilot. Recalibration occurs
only after a material documentation-structure or parser change, a material
raw-reference miss, repeated query routing failure, or high-risk
misclassification.

## Existing-source migration

Migration is prospective and incremental.

1. Preserve every existing source page and wikilink.
2. Initialize routing decisions without rewriting source bodies.
3. Continue maintaining high-value existing sources as `source_required`.
4. An existing mechanical endpoint may route as `raw_reference` while its
   historical source remains available.
5. Reconsider that source only when its raw changes or query evidence promotes
   it.
6. If a changed raw-reference source is not maintained, retain its old
   `raw_files` evidence and add a clear latest-raw navigation/staleness notice;
   never list a new raw version as summarized without rereading it.
7. A later approved promotion returns it to normal source maintenance.

There is no bulk deletion, frontmatter migration, or source consolidation.
Legacy flat raw layouts may continue to join routing through canonical URLs;
they do not need an immediate directory migration.

## Failure handling

- Missing or invalid related raw links fail the mechanical close check.
- A claim grounded only in a related raw reference fails source review.
- Ambiguous high-risk classification uses `semantic_triage` rather than an
  unsupported raw-only decision.
- Triage disagreement promotes safely and does not enter a retry loop.
- A query promotion recommendation remains non-executable until approved.
- An approved promotion with a missing source target is never suppressed by
  an unchanged raw hash.

## Acceptance

The design is ready for broader adoption when the Metronome pilot demonstrates
that:

- all three routing paths are discoverable and correctly recorded;
- overview facts and navigation-only raw links remain clearly separated;
- exact-detail queries reach current raw evidence;
- a query-driven promotion queues ingest without requiring content drift;
- the raw-reference sample contains no material missed reusable semantics, or
  the rule is revised transparently when it does;
- the pilot completes with materially fewer complete reads than six-page full
  ingest while passing its fixed quality gate;
- no scheduler, scoring service, bulk migration, or repeated test framework is
  required to obtain the result.

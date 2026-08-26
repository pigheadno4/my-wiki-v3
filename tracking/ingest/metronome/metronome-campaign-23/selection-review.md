# Metronome Campaign 23 Minimum Sufficient Source pilot

**Status:** Awaiting exact-manifest approval
**Mode:** Five-page dry-run pilot with per-page independent review
**Source baseline:** 225 canonical raw pages, 132 source pages, 99 raw pages without source summaries

## Goal

Test whether the approved Minimum Sufficient Source contract improves
first-pass acceptance and reduces complete semantic retries while preserving
complete raw evidence, strong workers, independent complete-source reviewers,
primary concept reciprocity, and exact raw deep dives.

The pilot changes source granularity and the review blocking contract only. It
does not change collection, routing states, scheduler behavior, result schemas,
model routing, close validators, or coordinator ownership.

## Metadata-only selection method

Selection used only the current collection inventory, raw path, line count,
SHA-256, canonical `.md` fetch URL, prior campaign membership, and canonical
source-target absence. No selected raw body was read to prepare this proposal.

All five raw paths remain in the capsule's 99-page pending list, and every
declared canonical source target is absent.

| Job | Archetype | Lines | SHA-256 | Selection purpose |
| --- | --- | ---: | --- | --- |
| `get-a-contract-v2` | API Read | 3091 | `fc929b1ed102106ef829006f505ee630159f5c895aa65dbb80270202007bb48f` | Longest/schema-heavy sample for object identity, time view, visibility boundaries, coverage routing, and compression safety |
| `list-invoices` | API List / Schema | 1126 | `dfb113ebaffb31bf7fecd97329451c145ca5cb593cfaea1b080c6433b3dfb2be` | Large collection sample for filters, pagination, ordering/completeness limits, and schema-detail routing |
| `void-a-credit-grant` | API Mutation | 166 | `c917e52bbe854ca7a0c0eef6eae037616a75af2edfa6fbb92b4a3ffc602bd3d8` | Short mutation for state, financial/lifecycle effects, idempotency authority, and recovery boundaries |
| `packages-overview` | Concept / Guide | 193 | `5e26b9b02883832ed82dd64b805ec3751fb910bbc81f1e9d179f7881ec7b83ff` | Compact concept guide for definitions, actors, lifecycle/data flow, examples, and primary concept selection |
| `azure` | Integration Guide | 261 | `a616695b72d172eb01c53970e0245c3d506e0b749909c2693c2b994265cb3f36` | External integration sample for responsibility, identity, data-flow, environment, and external-platform boundaries |

## Closed-campaign boundary

`packages-overview` appeared in the closed negative Campaign 13 manifest but
remained queued at attempt 0 and has no attempt directory, candidate, receipt,
or review. Campaign 23 treats it as a fresh per-page-review job. It may not
resume or reuse Campaign 13 state or evidence.

The other four job IDs do not appear in an earlier Metronome campaign manifest
or jobs file.

## Worker and reviewer contract

- Every job uses a strong-model worker that reads its complete assigned raw,
  the Campaign 23 playbook, and only its matching lessons section.
- Every first attempt receives a distinct strong-model reviewer that reads the
  complete assigned raw and applies the same archetype overlay.
- A source preserves query-critical facts, material boundaries, a coverage
  map, primary concepts, and exact raw navigation rather than transcribing the
  complete schema or example catalog.
- Only material factual, authority, contradiction, primary-concept, and
  evidence-navigation defects block approval.
- Secondary concepts, ordinary raw details, non-material wording/formatting,
  bounded quote repairs, and mechanical shared-file work are coordinator
  actions recorded in the existing review `reason`; they do not consume a
  worker retry.
- Unchanged-hash bounded corrections receive targeted review. Core semantic or
  authority corrections receive another complete review.
- The coordinator remains the only canonical/shared-file writer and performs
  no default third complete raw read.

## Fixed audit sample

- `void-a-credit-grant`: standard short mutation.
- `get-a-contract-v2`: longest and schema-heaviest page.
- `packages-overview`: ordinary cross-structure concept sample.

Each sample receives factual retrieval, boundary or contradiction retrieval,
and exact raw deep-dive checks. A material partial/fail or missing primary
reciprocal link expands semantic audit to all five pages. Mechanical hash,
candidate equality, canonical URL, raw backlink, catalog duplication, counts,
and touched links are checked across every promoted page.

## Measurements and decision

Use existing campaign state and evidence to record:

- first-pass approvals;
- bounded versus full semantic retries;
- attempts and full versus targeted reviews;
- campaign start to final reviewer approval time;
- fixed or expanded query results;
- exact raw deep-dive success; and
- primary concept reciprocity.

Final quality must pass. Efficiency is compared with Campaigns 20 through 22
rather than enforced by a new validator threshold. A second five-page
Metronome pilot is recommended only if quality passes and efficiency improves.
Reviewer sampling and cross-provider rollout remain separate future decisions.

## Authorization boundary

Approval authorizes Campaign 23 initialization, complete reads of only these
five raw pages, strong-model workers, distinct complete-source strong-model
reviewers, bounded retries, reviewer-approved promotion, and fixed or expanded
close audit. It does not authorize a sixth page, reuse of Campaign 13 output,
reviewer sampling, another provider, bulk migration, remote push, or unrelated
file modification.

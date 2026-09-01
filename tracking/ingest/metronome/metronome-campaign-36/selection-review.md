# Metronome Campaign 36 live risk-gated review proposal

**Status:** Awaiting exact-manifest approval
**Mode:** Five new Minimum Sufficient Sources with live risk-gated review
**Current baseline:** 226 current English canonical pages; 177 total source
summaries; 171 official-documentation summaries; 55 pages in the immutable
never-ingested planning inventory remain without source coverage

## Goal

Test whether one fixed low-risk sample can safely remove redundant independent
reviews from a small Metronome campaign while preserving complete worker reads,
immutable raw evidence, exact backlinks, coordinator-owned canonical writes,
and fail-closed expansion. This changes only reviewer coverage. It does not
change source granularity, raw collection, worker model, result schema, retry
limit, shared-file ownership, or close validation.

## Mechanical selection boundary

Selection reconciled the frozen 80-page planning inventory with current source
canonical URLs, leaving 55 uncovered identities. It used only canonical URL,
raw path and SHA-256, first heading and introductory metadata, line count,
prior-manifest membership, and source-target absence. No selected raw body was
read end to end, and these preliminary routes authorize no source facts.

| Job | Lines | Initial route | Pilot role |
| --- | ---: | --- | --- |
| `create-a-credit-grant-new-source` | 308 | mandatory | Financial mutation, deprecated Plans-to-Contracts boundary, and fixed audit page |
| `archive-billing-provider-configurations-new-source` | 218 | mandatory | Immediate cross-system lifecycle mutation and downstream-metering boundary |
| `list-custom-field-keys-new-source` | 191 | provisional | Compact read-only list and fixed eligible sample |
| `list-contracts-associated-with-package-new-source` | 243 | provisional | Read-only association list with time-period and completeness pressure |
| `list-offset-lifecycle-notification-configurations-new-source` | 225 | provisional | Read-only notification-configuration list and fixed audit page |

Total assigned raw size is 1,185 lines. Dispatch the two mandatory jobs and
the fixed sample first so required reviews and the release gate start as early
as possible. `list-custom-field-keys` appeared in the Campaign 12 metadata-only
manifest as navigation-only, but it received no complete read, candidate, or
source promotion. Campaign 36 must not read or reuse Campaign 12 artifacts or
classification decisions as source evidence.

## Live risk route

Every strong Sol worker reads exactly one complete raw page and returns the
normal Minimum Sufficient Source, three to five exact quotes, a coverage map,
primary concept routes, reciprocal shared suggestions, and an exact
path-qualified raw backlink.

The mandatory jobs proceed directly to a different strong Sol complete-source
reviewer. After each provisional worker finishes, the coordinator records one
grounded route:

- `review_required` for any material financial or lifecycle meaning, state
  transition, durable failure/retry/idempotency/concurrency/propagation fact,
  cross-system authority or reconciliation boundary, or material requiredness,
  pagination, time-window, or schema-versus-narrative conflict;
- `sample_eligible` only when the complete read finds none of those triggers.

The fixed `list-custom-field-keys-new-source` sample always receives a complete
review if it remains eligible. Other eligible candidates wait in
`review_deferred`. An eligible sample approval records per-page waiver evidence
and releases the deferred candidates. If the sample escalates, requests a
material correction, or is rejected, the gate fails and every deferred or
later provisional candidate requires full review. A passed sample may cover a
later eligible candidate in this same campaign only; it grants no standing
policy for another campaign.

## Promotion, audit, and success gates

Canonical promotion waits until all jobs are terminal and the three immutable
candidate audit jobs pass: `create-a-credit-grant-new-source`,
`list-custom-field-keys-new-source`, and
`list-offset-lifecycle-notification-configurations-new-source`. The audit reads
each complete candidate and raw page and checks factual retrieval, a material
boundary or contradiction, exact raw deep dive, and primary reciprocal links.
A material defect in any waived candidate fails this pilot and blocks
promotion; it is not silently repaired.

Success requires:

- five of five final candidates approved with no coordinator semantic repair;
- the fixed eligible sample passes its first complete review;
- at least two of the three provisional pages receive valid review waivers;
- the fixed candidate audit passes 9/9 before promotion;
- hashes, exact candidate identity, raw backlinks, reciprocal links, shared
  updates, company/index entries, counts, capsule validation, and diff checks
  pass once;
- elapsed time is at most 35 minutes. Timing is observational and never waives
  quality.

If fewer than two pages remain eligible, the result is inconclusive for
throughput rather than permission to weaken the trigger. If the sample or audit
finds a material defect, the result is failed and nothing is promoted.

## Authorization boundary

This proposal and `manifest.json` do not initialize Campaign 36 or authorize
agent dispatch. Explicit approval of this exact manifest would authorize only
the five complete raw reads, risk routes, required reviews, one fixed sample,
bounded retries, pre-promotion candidate audit, approved shared updates,
canonical promotion, one close validation, and one local campaign commit.

It does not authorize a sixth page, another sample, reuse of earlier candidate
content, Luna or Terra, a risk registry or score, classifier agents, bulk
ingestion, another campaign or PSP, remote push, or unrelated-file changes.

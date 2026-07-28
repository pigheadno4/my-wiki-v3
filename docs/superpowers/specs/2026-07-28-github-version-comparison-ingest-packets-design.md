# GitHub Version Comparison and Ingest Packets

## Status

Approved.

## Goal

Reduce the time required to process routine GitHub releases without weakening
the wiki's evidence or approval boundaries.

The collector will turn an exact version comparison into a deterministic,
review-ready ingest packet. Same-major releases default to delta ingest when
all changed evidence is bounded. Initial baselines, major transitions, and
unbounded changes remain full ingest or manual review.

Collection still stops at `awaiting_approval`. Wiki ingest remains
user-approved, serial, and agent-authored.

## Problem

The collector already writes immutable snapshots, release records, changed
path lists, and Git patches. The current ingest-mode recommendation is too
broad: release-note words such as `payment`, `checkout`, `vault`, or `venmo`
force full ingest even when the exact change is small and fully bounded.

This made `braintree-web@3.143.0` to `3.144.0` expensive to process. The new
snapshot contained 330 files, but comparison by path and blob hash showed:

- 319 retained files were byte-identical;
- 10 retained files changed;
- one retained story was added; and
- the material knowledge changes were limited to PayPal View/Edit Funding
  Instrument, PayPal Checkout v6 options, Venmo initialization resilience, and
  one dependency update.

The script should prove which evidence is unchanged and organize the changed
evidence before ingest begins.

## Boundaries

### The script does

- compare exact package-qualified versions and SHAs;
- account for every upstream changed path;
- compare retained snapshot files by path and content hash;
- classify retained changed evidence;
- detect dependency and public export changes;
- generate deterministic JSON and Markdown packets;
- recommend full or delta ingest with explicit mechanical reasons;
- identify blocking evidence gaps and unclassified changes; and
- stop at the existing approval gate.

### The script does not

- edit source, changelog, company, concept, index, or log pages;
- approve or activate a work item;
- authorize skipping missing or unclassified evidence;
- let an LLM control mode, priority, or lifecycle state; or
- change immutable snapshots, release records, or comparisons.

An LLM may later summarize a packet, suggest affected wiki sections, or
propose grounding excerpts. Such output is non-authoritative and cannot alter
the canonical packet JSON or queue state.

## Authority Model

There remains one authority for each concern:

| Concern | Authority |
| --- | --- |
| Repository intent and capsule policy | `tracking/github/repo-registry.toml` |
| Immutable upstream evidence | `raw/github/<company>/<repo>/` |
| Exact version difference | generated comparison directory |
| Approval and lifecycle state | `tracking/github/work-items.json` |
| Deterministic ingest scope | canonical ingest packet JSON |
| Durable knowledge | cumulative wiki source and changelog pages |

An ingest packet is derived evidence, not another lifecycle store. It can be
regenerated from accepted snapshots, release records, comparisons, and
registry policy.

## Architecture

Extend `collect_github_repos.py` after snapshot, release, and comparison
publication:

```text
discover exact releases
-> collect immutable evidence
-> compare exact SHAs
-> classify all changed paths
-> compare retained blob hashes
-> build ingest packet
-> recommend full or delta
-> publish work item in awaiting_approval
```

Use a focused packet builder module rather than adding more comparison logic
to the CLI file. The module consumes existing typed records and returns one
canonical packet model. It does not perform Git network operations or queue
transitions.

### Queued ingest packet layout

```text
tracking/github/repos/<company>/<repo>/
└── ingest-packets/<work-item-id>/
    ├── packet.json
    └── packet.md
```

The path is derived from repository identity and work-item ID. New work items
add an `ingest_packet` evidence pointer containing that path. The pointer is
not packet state and does not change lifecycle authority. It is optional only
for historical work items created before packet support.

### Ad hoc comparison packet layout

The existing `compare` command can generate a read-only packet for two
retained package versions without creating a work item:

```text
tracking/github/repos/<company>/<repo>/
└── comparisons/<package>/<from>--<to>/
    ├── comparison.json
    ├── comparison.md
    ├── diff.patch
    ├── review-packet.json
    └── review-packet.md
```

Queued ingest and ad hoc review packets use the same builder and
classification rules. Only the queued packet carries a work-item ID and can
be used by the ingest lifecycle.

## Comparison Model

The packet distinguishes two related views.

### Upstream diff

Use Git rename detection and record every added, modified, deleted, or renamed
repository path between the exact SHAs. Each changed path must have exactly
one disposition:

- `retained-evidence`;
- `intentional-policy-exclusion`; or
- `blocking-evidence-gap`.

Tests and fixtures excluded by approved capsule policy are intentional
exclusions. A changed production, documentation, example, or story file that
should be retained but is absent is a blocking gap.

No changed path may disappear from the packet merely because it is outside the
published snapshot.

### Retained evidence diff

Compare prior and current snapshot manifests by path and SHA-256:

- unchanged;
- modified;
- added;
- removed; and
- renamed when the upstream rename links equal blob content.

Unchanged retained files are not required reading for delta ingest. Their
prior and current hashes prove identity.

For an initial baseline there is no retained evidence diff. Every snapshot
file is baseline required reading.

## Evidence Classification

The first implementation supports repositories using
`npm-tracked-source-v1`.

Every retained changed file receives one primary class:

- `package-manifest`;
- `release-history`;
- `public-source`;
- `documentation`;
- `example`;
- `story`;
- `translation`;
- `repository-context`; or
- `unclassified`.

Classification reuses capsule policy, package ownership, required roots,
declared public targets, and existing test/story/fixture classifiers. It does
not infer production safety from filename keywords alone.

Optional affected-area labels provide review hints:

```text
src/venmo/**                 -> Venmo
src/paypal-checkout/**       -> PayPal Checkout
src/three-d-secure/**        -> 3D Secure
src/hosted-fields/**         -> Hosted Fields
*.stories.*                  -> Integration scenarios
package manifest dependency  -> Dependencies
```

Area labels never determine full or delta mode. An unclassified retained
source file blocks automatic delta recommendation.

## Dependency and Public API Comparison

For each package, compare normalized package-manifest fields:

- package version;
- dependencies;
- optional dependencies;
- peer dependencies;
- public `exports`;
- `main`;
- `module`;
- `types`;
- `typings`; and
- `bin`.

The packet records dependency additions, removals, and version-specification
changes separately from source changes.

Public export additions are delta-eligible but high review priority. Public
export removals, retargeting, or structurally incompatible changes require
full ingest. A malformed or unsupported export structure is a blocking gap,
not a guessed compatibility decision.

## Mode Recommendation

### Delta default

Recommend `delta` for an already-ingested same-major release when:

- prior and current exact identities are known;
- every upstream changed path has a non-blocking disposition;
- all required changed evidence is retained and classified;
- comparison and packet budgets are satisfied;
- there is no public export removal or incompatible retargeting; and
- no capsule-policy change invalidates the prior evidence boundary.

Payment-related release-note terms increase review priority and affected-area
labels. They do not force full ingest.

### Full recommendation

Recommend `full` for:

- an initial package baseline;
- a major-version transition;
- a public export removal or incompatible retargeting;
- a source-capsule policy change;
- a missing or ambiguous prior snapshot;
- an upstream diff or packet exceeding reviewed limits;
- a security change whose impact cannot be bounded.

A small security patch with complete, classified evidence may remain delta
with `high` review priority. Security terminology alone does not require
rereading unrelated unchanged files.

### Manual review

Use the existing `needs_manual_review` lifecycle when packet construction
cannot establish a safe full or delta scope. This includes missing required
changed evidence, unclassified retained source, invalid identities, and
unsupported comparison structures. Do not publish a normal
`awaiting_approval` item with an incomplete packet.

## Packet Contract

`packet.json` is canonical UTF-8 JSON with sorted object keys and no
insignificant whitespace. It contains:

- format version and packet kind;
- repository, package, version, SHA, and collection identities;
- work-item ID for queued packets;
- expected wiki targets and existing wiki context;
- snapshot, release, and comparison evidence paths;
- upstream changed paths with dispositions;
- retained evidence counts and per-file hash transitions;
- dependency changes;
- public export changes;
- evidence classifications and affected-area hints;
- unclassified changes;
- evidence gaps;
- required reading;
- unchanged evidence count;
- recommendation mode, priority, and ordered reason codes; and
- SHA-256 of the generated Markdown representation.

`packet.md` renders the same model for humans and ingest agents. It contains no
additional decisions.

`required_reading` contains only paths that exist and must be read.
`wiki_context` contains existing cumulative pages that must be read.
`expected_wiki_targets` records source and changelog paths that do not yet
exist for an initial baseline and must be created during ingest.

For multi-package releases sharing one SHA, one queued packet has a repository
summary and separate package sections. Shared snapshot evidence appears once.

## Required Reading

### Delta packet

The packet lists:

- current cumulative source page and repository changelog page in
  `wiki_context`;
- every assigned release note;
- every assigned comparison;
- every changed retained source, documentation, example, and story file;
- relevant current package manifests; and
- prior package manifests when needed to interpret dependency or export
  changes.

The ingest agent must read every listed item in full before editing wiki
knowledge. Unchanged retained files do not need to be reread.

### Full packet

The packet lists:

- every current snapshot file;
- every assigned release note and comparison;
- current cumulative source and repository changelog pages in `wiki_context`
  when they exist;
- missing baseline page destinations in `expected_wiki_targets`;
- relevant prior-version context; and
- manifests required to verify evidence identity.

This preserves the existing full-ingest meaning. Full ingest adds knowledge
without replacing validated older-version content.

## CLI Behavior

Periodic collection keeps its existing commands. Successful collection shows
the packet in `status`:

```text
State: awaiting_approval
Recommended mode: delta
Review priority: high
Packet: tracking/.../ingest-packets/github-.../packet.md
Required reading: 8 files
Unclassified changes: 0
Evidence gaps: 0
```

`next-ingest` prints the packet path and required-reading summary after it
atomically activates one approved item. It does not read evidence or edit the
wiki.

The existing `compare` command writes `review-packet.json` and
`review-packet.md` alongside the comparison for any two retained,
package-qualified versions. It does not create or mutate queue state.

## Publication and Failure Handling

Build packet files in temporary storage and publish them atomically. Packet
publication is required before a new work item can reach
`awaiting_approval`.

On failure:

- publish no partial packet;
- preserve accepted snapshots, releases, comparisons, and earlier packets;
- do not publish or advance a normal approval item;
- use existing bounded retries for transient filesystem failures; and
- route deterministic identity, classification, budget, or evidence failures
  to `needs_manual_review`.

Regeneration with identical inputs must produce byte-identical packet files.

## Validation

Extend `validate_github_collection.py` to verify:

- canonical packet JSON and Markdown hash;
- packet path and work-item identity;
- exact equality between a new work item's `ingest_packet` pointer and its
  deterministic packet path;
- repository, package, version, and exact SHA links;
- existence and hashes of referenced immutable evidence;
- complete changed-path disposition;
- retained added/modified/removed/unchanged counts against manifests;
- existence of every required-reading path;
- absence of blocking gaps for delta recommendations;
- deterministic recommendation mode, priority, and reason order;
- one packet per queued work item; and
- exact equality between generated `status.md` packet summaries and state.

Existing ingested work items without an `ingest_packet` pointer remain valid.
Every newly collected work item must carry the pointer and pass packet
validation through all later lifecycle states. The validator must not
retroactively invent packets for immutable historical work.

## Testing

Required focused tests:

- same-major payment release with bounded changes recommends delta;
- initial package baseline recommends full;
- major transition recommends full;
- public export addition is delta-eligible and high priority;
- public export removal or retargeting recommends full;
- dependency-only update recommends delta;
- Git rename is represented without false add/remove duplication;
- approved test or fixture exclusion is accounted for but not required reading;
- unclassified changed source blocks delta;
- missing required changed evidence blocks normal approval;
- packet budget overflow routes to manual review;
- multi-package shared-SHA release produces one packet with package sections;
- baseline packet lists the complete snapshot;
- queued and ad hoc packets share classification behavior;
- packet JSON and Markdown are deterministic;
- validator rejects packet/work-item identity mismatch;
- validator accepts historical pre-packet work items; and
- existing collection, retry, approval, and serial-ingest tests remain green.

Add a Braintree conformance fixture for `3.143.0` to `3.144.0`. It must report
319 unchanged retained files, 10 modified retained files, one added retained
story, no removed retained files, and a delta recommendation with high review
priority.

## Rollout

1. Add packet models, canonical serialization, and focused unit tests.
2. Add retained-manifest and upstream-path accounting.
3. Replace broad release-note mode triggers with the approved deterministic
   rules.
4. Generate queued packets before work-item publication.
5. Extend status, `next-ingest`, and validation.
6. Extend ad hoc comparison output.
7. Run focused tests, the full suite, offline GitHub validation, and
   `git diff --check`.
8. Dry-run a retained Braintree comparison and review its packet.
9. Enable packet enforcement for newly collected work items only.

## Acceptance Criteria

- Routine same-major releases no longer become full solely because release
  notes contain payment-related words.
- Every upstream changed path is retained, intentionally excluded, or a
  blocking evidence gap.
- Delta required reading contains every changed retained knowledge-bearing
  file and no unchanged file.
- Full required reading preserves the complete-capsule rule.
- The Braintree conformance fixture produces the expected 319/10/1 retained
  evidence counts.
- Collection and ad hoc comparison packets are deterministic and validated.
- Collection still stops at approval and never edits wiki knowledge.
- LLM output cannot control recommendation or lifecycle state.
- Existing immutable evidence and historical work items remain valid.

## Out of Scope

- automatic wiki editing or automatic ingest approval;
- LLM-controlled mode or lifecycle decisions;
- permanent shared clone caching;
- ingesting tests or changing existing capsule exclusions;
- semantic interpretation of arbitrary source code;
- non-NPM repository adapters in this implementation; and
- redesigning the work-item state machine.

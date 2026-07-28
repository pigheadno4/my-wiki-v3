# GitHub Version Comparison and Ingest Packets Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:subagent-driven-development` (recommended) or
> `superpowers:executing-plans` to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate deterministic, review-ready ingest packets for exact GitHub
package release comparisons so bounded same-major updates can use delta ingest
without weakening evidence, validation, or approval gates.

**Architecture:** Upgrade comparison manifests to persist rename-aware upstream
changes, then add one focused `github_ingest_packets.py` module that derives
retained-file accounting, evidence classifications, dependency/API changes,
required reading, and mechanical recommendations from immutable manifests and
local Git evidence. The existing collector publishes packet files atomically
before finalizing a new work item; the work-item queue retains lifecycle
authority and stores only an evidence pointer. The existing validator checks
packets without requiring a clone.

**Tech Stack:** Python 3.9 standard library, frozen dataclasses, canonical JSON,
Git CLI, `unittest`, TOML registry policy, and the existing GitHub collection
and validation modules.

## Global Constraints

- Keep `tracking/github/repo-registry.toml` as policy authority.
- Keep accepted raw snapshots and release records immutable.
- Keep `tracking/github/work-items.json` as the only lifecycle authority.
- Do not edit wiki knowledge automatically.
- Do not approve or activate a work item automatically.
- Collection may process releases in batches; ingest remains user-approved,
  globally serial, and full-read for every path in `required_reading`.
- Implement only `npm-tracked-source-v1`; reject unsupported adapters.
- Exclude tests and fixtures according to capsule policy; retain stories when
  policy includes them.
- Account for every upstream added, modified, deleted, or renamed path.
- Do not let release-note keywords alone force full ingest.
- Do not let LLM output alter packet JSON, mode, priority, or queue state.
- Preserve comparison format v1 and packet-less work items as valid history.
- Publish no partial comparison or packet directory on failure.
- Keep `CLAUDE copy.md` untracked and untouched.

---

### Task 1: Persist Rename-Aware Upstream Changes

**Files:**
- Modify: `scripts/github_pilot_store.py`
- Modify: `scripts/github_validation.py`
- Modify: `tests/test_github_pilot_store.py`
- Modify: `tests/test_github_validation.py`

**Interfaces:**
- Add `UpstreamChange(status, old_path, new_path)` in
  `github_pilot_store.py`.
- Add
  `read_upstream_changes(repo_root, from_sha, to_sha, pathspecs=())` for
  reusable local-Git inspection. Empty `pathspecs` means the complete
  repository diff; comparison publication passes its bounded package
  pathspecs.
- Extend `ComparisonRecord` with
  `upstream_changes: Tuple[UpstreamChange, ...]`.
- Write comparison format v2 with `upstream_changes`; continue validating
  existing format v1 manifests.
- Use `git diff --name-status -M --find-renames=50%` over the union of prior
  and current package pathspecs.

- [ ] **Step 1: Add failing store tests for statuses and renames**

Add
`test_comparison_persists_added_modified_deleted_and_renamed_paths()`.
Construct two exact commits using the existing store fixture, call
`write_package_comparison()` with its concrete fixture paths and SHAs, and
assert:

```python
self.assertEqual(
    (
        UpstreamChange("added", "", "src/new.stories.js"),
        UpstreamChange("deleted", "docs/old.md", ""),
        UpstreamChange("modified", "src/index.ts", "src/index.ts"),
        UpstreamChange("renamed", "src/old.ts", "src/new.ts"),
    ),
    record.upstream_changes,
)
```

Also assert that `changed_paths` remains a sorted compatibility union of every
non-empty old/new path.

- [ ] **Step 2: Run the focused store test**

```bash
python3 -m unittest \
  tests.test_github_pilot_store.PilotStoreTests.test_comparison_persists_added_modified_deleted_and_renamed_paths
```

Expected: `ERROR` because `UpstreamChange` and v2 metadata do not exist.

- [ ] **Step 3: Parse Git name-status output deterministically**

Implement a private parser that accepts only:

```text
A<TAB>path
M<TAB>path
D<TAB>path
RNNN<TAB>old-path<TAB>new-path
```

Normalize them to `added`, `modified`, `deleted`, and `renamed`. Reject
unmerged, copied, malformed, unsafe, duplicate, or pathspec-escaping rows with
`PilotStoreError`. Sort by `(new_path or old_path, old_path, status)`.

- [ ] **Step 4: Publish comparison format v2 atomically**

Add `upstream_changes` to canonical `comparison.json`, keep `changed_paths`
for compatibility, and render statuses in `comparison.md`. The existing
`diff.patch` remains the exact patch.

- [ ] **Step 5: Add validator compatibility tests**

Add tests that:

- accept an existing format v1 comparison;
- accept a valid format v2 comparison;
- reject malformed rename rows;
- reject mismatch between `changed_paths` and the status-row path union.

- [ ] **Step 6: Run focused comparison tests**

```bash
python3 -m unittest tests.test_github_pilot_store tests.test_github_validation
git diff --check
```

Expected: all tests pass and `git diff --check` prints nothing.

- [ ] **Step 7: Commit the comparison foundation**

```bash
git add scripts/github_pilot_store.py scripts/github_validation.py \
  tests/test_github_pilot_store.py tests/test_github_validation.py
git commit -m "feat: persist rename-aware GitHub comparisons"
```

---

### Task 2: Build the Deterministic Packet Model

**Files:**
- Create: `scripts/github_ingest_packets.py`
- Create: `tests/test_github_ingest_packets.py`
- Modify: `scripts/github_capsule_selection.py`
- Modify: `tests/github_test_support.py`
- Modify: `tests/test_github_capsule_selection.py`

**Interfaces:**
- Add frozen inputs:

```python
@dataclass(frozen=True)
class PackagePacketInput:
    package: str
    from_version: str
    to_version: str
    from_sha: str
    to_sha: str
    release_manifest: str
    comparison_manifest: str
    prior_snapshot_manifest: str
    upstream_changes: Tuple[UpstreamChange, ...]
    release_notes_revision: bool = False


@dataclass(frozen=True)
class PacketRecommendation:
    mode: str
    priority: str
    reasons: Tuple[str, ...]


@dataclass(frozen=True)
class IngestPacket:
    document: dict
    markdown: bytes
```

- Add this public builder signature:

```python
def build_ingest_packet(
    root: Path,
    config: RepoConfig,
    work_item_id: str,
    snapshot_manifest: str,
    package_inputs: Sequence[PackagePacketInput],
    packet_kind: str,
) -> IngestPacket
```

- `packet_kind` is exactly `queued` or `ad-hoc`.
- The builder reads existing local artifacts but performs no network or queue
  operations.

- [ ] **Step 1: Add packet fixture helpers**

Extend `tests/github_test_support.py` with narrowly scoped helpers that write
canonical snapshot, release, and v2 comparison fixtures. Keep Git mutation
helpers unchanged.

- [ ] **Step 2: Add failing retained-diff tests**

Cover:

- unchanged, modified, added, and removed snapshot files by path/SHA-256;
- rename collapse only when a v2 upstream rename links equal blob content;
- no false add/remove rows for a valid rename;
- baseline count and required reading containing every current snapshot file.

Assert exact count dictionaries, per-file transitions, and sorted output.

- [ ] **Step 3: Implement strict artifact loading and retained accounting**

In `github_ingest_packets.py`:

- resolve every path beneath `root` without symlink escape;
- reject duplicate JSON keys and unknown required artifact shapes;
- index snapshot file rows by path;
- compute transitions from manifest hashes, not working-tree content;
- verify package, version, repository, and SHA identities across inputs;
- retain unchanged counts while excluding unchanged files from delta reading.

- [ ] **Step 4: Add failing classification and disposition tests**

Cover the approved classes:

```text
package-manifest
release-history
public-source
documentation
example
story
translation
repository-context
unclassified
```

Also cover upstream dispositions:

```text
retained-evidence
intentional-policy-exclusion
blocking-evidence-gap
```

Tests and fixtures excluded by policy must be intentional exclusions. An
included `.stories.*` file must classify as `story`. A changed required-root
source absent from the snapshot must become a blocking gap.

- [ ] **Step 5: Implement classification using stored evidence**

Use snapshot `purpose`, `classification_reason`, package ownership, configured
roots/includes, and approved category classifiers. Path suffixes may select
documentation/example/story/translation labels, but may not turn an absent
required source into an exclusion.

Expose a small public
`classify_excluded_categories(path: str, enabled: Sequence[str])` facade in
`github_capsule_selection.py`; make both capsule selection and packet
classification call it. Do not duplicate test/fixture/story matching logic.

Add deterministic affected-area labels for Venmo, PayPal Checkout, 3D Secure,
Hosted Fields, integration stories, and dependencies. Labels are informational
only.

- [ ] **Step 6: Add failing manifest comparison tests**

Compare normalized fields from prior/current package manifests:

```text
version
dependencies
optionalDependencies
peerDependencies
exports
main
module
types
typings
bin
```

Cover dependency add/remove/specification change, export addition, export
removal, retargeting, and malformed unsupported export structures.

- [ ] **Step 7: Implement dependency and public API comparison**

Emit separate sorted sections for dependency and public API changes. Treat
export addition as compatible, removal/retargeting as incompatible, and
unsupported structures as blocking rather than guessing.

- [ ] **Step 8: Add failing recommendation tests**

Prove:

- initial baseline -> `full`;
- major transition -> `full`;
- bounded same-major payment change -> `delta`, `high`;
- dependency-only same-major change -> `delta`;
- export addition -> `delta`, `high`;
- export removal/retargeting -> `full`;
- bounded security patch -> `delta`, `high`;
- unbounded security impact -> `full`;
- release-notes-only revision -> `delta` with the revised release notes in
  required reading;
- unclassified source or blocking gap -> `PacketBuildError`;
- packet budget overflow -> `PacketBuildError`.

- [ ] **Step 9: Implement ordered mechanical recommendations**

Use stable reason ordering. Keywords can raise priority or add area labels but
cannot force full. Compare capsule-policy hashes when a prior packet provides
one. Store the current normalized capsule-policy hash in every packet. For a
bootstrap comparison without a prior packet, require both accepted snapshots,
record `policy-history-bootstrap`, raise review priority to `high`, and do not
claim historical policy continuity. A later mismatch against the preceding
packet's policy hash requires `full`.

- [ ] **Step 10: Add determinism and multi-package tests**

Build the same packet twice and assert byte-identical canonical JSON and
Markdown. Prove a shared-SHA work item produces one repository packet with
sorted package sections and one shared snapshot section.

- [ ] **Step 11: Run the packet unit suite**

```bash
python3 -m unittest tests.test_github_ingest_packets
git diff --check
```

Expected: all packet tests pass.

- [ ] **Step 12: Commit the packet model**

```bash
git add scripts/github_ingest_packets.py tests/test_github_ingest_packets.py \
  scripts/github_capsule_selection.py tests/test_github_capsule_selection.py \
  tests/github_test_support.py
git commit -m "feat: build deterministic GitHub ingest packets"
```

---

### Task 3: Publish Packets Atomically

**Files:**
- Modify: `scripts/github_ingest_packets.py`
- Modify: `tests/test_github_ingest_packets.py`

**Interfaces:**
- Add
  `publish_queued_packet(root: Path, config: RepoConfig, packet: IngestPacket) -> Path`.
- Add
  `publish_review_packet(comparison_directory: Path, packet: IngestPacket) -> Path`.

- Queued destination:
  `tracking/github/repos/<company>/<repo>/ingest-packets/<work-item-id>/`
- Ad hoc files:
  `review-packet.json` and `review-packet.md` beside `comparison.json`.

- [ ] **Step 1: Add failing publication tests**

Prove:

- queued and ad hoc layouts are exact;
- JSON is canonical and contains the SHA-256 of exact Markdown bytes;
- identical publication is idempotent;
- conflicting existing bytes are rejected;
- a simulated second-write failure leaves no partial packet;
- repository-root symlink escape is rejected.

- [ ] **Step 2: Implement one shared atomic publisher**

Write both files to owned temporary storage, `fsync` files, and replace the
destination only after both bytes are complete. Reuse containment and cleanup
patterns from `github_pilot_store.py`; do not create a general artifact
framework.

- [ ] **Step 3: Run packet publication tests**

```bash
python3 -m unittest tests.test_github_ingest_packets
git diff --check
```

Expected: all tests pass with no partial directories.

- [ ] **Step 4: Commit atomic publication**

```bash
git add scripts/github_ingest_packets.py tests/test_github_ingest_packets.py
git commit -m "feat: publish GitHub ingest packets atomically"
```

---

### Task 4: Integrate Packets With Collection and Queue Output

**Files:**
- Modify: `scripts/collect_github_repos.py`
- Modify: `scripts/github_work_items.py`
- Modify: `tests/test_collect_github_repos.py`
- Modify: `tests/test_github_work_items.py`
- Modify: `tests/test_github_pilot_e2e.py`

**Interfaces:**
- Add optional `ingest_packet: str = ""` to `WorkItem`.
- Accept packet-less historical JSON, but make
  `finalize_collected_work_item()` reject every new normal item without a
  packet pointer.
- Add packet summary input to `render_status()` rather than duplicating packet
  counts in queue state.
- Keep failure/manual-review items able to exist without a normal packet.

- [ ] **Step 1: Add failing queue compatibility tests**

Prove:

- historical JSON without `ingest_packet` still loads and round-trips;
- a new collected item cannot finalize without a packet;
- a new collected item with the deterministic packet pointer finalizes;
- pointer changes are rejected as evidence mutation;
- status renders packet path, priority, required-reading count, unclassified
  count, and evidence-gap count from a supplied packet summary.

- [ ] **Step 2: Extend the work-item schema without new lifecycle state**

Add the optional field to serialization, identity/evidence comparison, merging,
and status. Keep all current transitions unchanged.

- [ ] **Step 3: Add failing collection integration tests**

Update the local PayPal fixture to collect:

- one baseline packet shared by both packages;
- one same-major update packet;
- one major transition packet.

Assert packet publication precedes the single atomic queue write, exact pointer
path, baseline/full behavior, same-major/delta behavior, and no wiki writes.

- [ ] **Step 4: Wire the collector in this exact order**

```text
publish snapshot
-> publish release records
-> publish v2 comparisons
-> build work-item identity
-> build and publish queued packet
-> attach packet pointer
-> finalize awaiting_approval item
```

Convert each `_PackageContext` into `PackagePacketInput`. Use packet
recommendations when constructing `PackageChange`; retire broad keyword
recommendations from normal successful collection. Preserve the existing
bounded collection failure path.

For every non-baseline package input, call `read_upstream_changes()` without
pathspecs so paths outside the retained capsule are still dispositioned.
Deduplicate identical `(from_sha, to_sha)` repository diffs in a shared-SHA
packet while preserving package assignment. The package comparison remains
bounded to its package pathspecs.

- [ ] **Step 5: Route deterministic packet gaps to manual review**

Catch `PacketBuildError` as deterministic review evidence. Preserve accepted
snapshot/release/comparison artifacts, publish no partial packet, and create no
normal `awaiting_approval` item.

- [ ] **Step 6: Extend ad hoc compare**

Make `compare_one()` build `review-packet.json` and `review-packet.md` from the
same builder without creating or mutating a work item.

- [ ] **Step 7: Extend operator output**

`status` must show packet summary fields. `next-ingest` must atomically claim
one approved item and print its packet path and required-reading summary; it
must not read evidence or edit wiki pages.

- [ ] **Step 8: Run collection and queue tests**

```bash
python3 -m unittest \
  tests.test_github_work_items \
  tests.test_collect_github_repos \
  tests.test_github_pilot_e2e
git diff --check
```

Expected: all tests pass, with collection stopping at `awaiting_approval`.

- [ ] **Step 9: Commit collector integration**

```bash
git add scripts/collect_github_repos.py scripts/github_work_items.py \
  tests/test_collect_github_repos.py tests/test_github_work_items.py \
  tests/test_github_pilot_e2e.py
git commit -m "feat: queue GitHub ingest packets for review"
```

---

### Task 5: Validate Packet Evidence End To End

**Files:**
- Modify: `scripts/github_validation.py`
- Modify: `tests/test_github_validation.py`

**Interfaces:**
- Extend `GitHubReport` with inspected queued and ad hoc packets.
- Add packet indexes by relative path and work-item ID.
- Recompute recommendations from canonical packet facts; do not trust stored
  mode or priority alone.

- [ ] **Step 1: Add failing packet validation tests**

Cover:

- canonical JSON and Markdown hash;
- deterministic queued path and work-item identity;
- repository/package/version/SHA links;
- evidence file existence and referenced hashes;
- complete upstream disposition;
- retained transition counts against snapshots;
- required-reading existence and containment;
- no gaps/unclassified changes for delta;
- recommendation mode/priority/reason order;
- one queued packet per packet-enabled work item;
- exact generated status;
- rejected packet/work-item mismatch;
- accepted historical packet-less work item.

- [ ] **Step 2: Inspect packet artifacts without raising**

Glob queued `packet.json` and ad hoc `review-packet.json`, retain bounded parse
errors in the report, and reject duplicate JSON keys.

- [ ] **Step 3: Implement packet validation**

Reuse packet-module parsing/recommendation helpers where doing so cannot hide
independent evidence checks. Validation must work from persisted artifacts
alone and must not clone or contact GitHub.

- [ ] **Step 4: Run focused validation**

```bash
python3 -m unittest tests.test_github_validation
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: tests pass. The repository validator reports only pre-existing,
unrelated wiki lint findings, if any; no new GitHub collection errors.

- [ ] **Step 5: Commit validator support**

```bash
git add scripts/github_validation.py tests/test_github_validation.py
git commit -m "feat: validate GitHub ingest packet evidence"
```

---

### Task 6: Lock the Braintree Conformance Case

**Files:**
- Create: `tests/fixtures/github/braintree-web-3.143.0--3.144.0/fixture.json`
- Create: `tests/fixtures/github/braintree-web-3.143.0--3.144.0/prior-manifest.json`
- Create: `tests/fixtures/github/braintree-web-3.143.0--3.144.0/current-manifest.json`
- Create: `tests/fixtures/github/braintree-web-3.143.0--3.144.0/comparison.json`
- Modify: `tests/test_github_ingest_packets.py`

**Interfaces:**
- Fixture contains metadata and hashes only; do not duplicate the full source
  capsule in tests.
- Expected retained result:
  `319 unchanged`, `10 modified`, `1 added story`, `0 removed`.
- Expected recommendation: `delta`, priority `high`.

- [ ] **Step 1: Generate a bounded fixture from accepted artifacts**

Use the already accepted Braintree `3.143.0` and `3.144.0` manifests and
comparison. Copy only canonical identity rows, retained file metadata, and
upstream status rows needed to replay packet accounting.

- [ ] **Step 2: Add the failing conformance test**

Assert exact counts, the added story classification, zero blocking gaps, no
unchanged file in delta required reading, `delta`, and `high`.

- [ ] **Step 3: Fix only reusable packet behavior exposed by the fixture**

Do not add Braintree-specific mode logic or hard-coded file totals. Any fix
must operate through general classifications, dispositions, and
recommendation signals.

- [ ] **Step 4: Run the conformance and packet suites**

```bash
python3 -m unittest \
  tests.test_github_ingest_packets.GitHubIngestPacketTests.test_braintree_3_143_0_to_3_144_0_conformance
python3 -m unittest tests.test_github_ingest_packets
git diff --check
```

Expected: exact `319/10/1/0`, `delta`, and `high`.

- [ ] **Step 5: Commit the conformance fixture**

```bash
git add tests/fixtures/github/braintree-web-3.143.0--3.144.0 \
  tests/test_github_ingest_packets.py
git commit -m "test: lock Braintree delta packet conformance"
```

---

### Task 7: Document and Verify the Operator Workflow

**Files:**
- Modify: `rules/github-repos.md`
- Modify: `CLAUDE.md` only if its workflow-index wording requires a route
  update; otherwise leave it unchanged.

**Interfaces:**
- Document packet locations, full/delta/manual-review rules, `compare` output,
  `status`, `next-ingest`, and the serial full-read boundary.
- State explicitly that full ingest appends/refines cumulative knowledge and
  preserves old version findings.

- [ ] **Step 1: Update GitHub workflow rules**

Add concise operator commands and enforce:

```text
collect -> review packet -> user approve -> next-ingest
```

For delta ingest, read every `required_reading` and `wiki_context` path in
full. For full ingest, read the complete current snapshot plus listed history.
Never treat packet generation as ingest approval.

- [ ] **Step 2: Run focused and full verification**

```bash
python3 -m unittest \
  tests.test_github_pilot_store \
  tests.test_github_ingest_packets \
  tests.test_github_work_items \
  tests.test_collect_github_repos \
  tests.test_github_pilot_e2e \
  tests.test_github_validation
python3 -m unittest discover -s tests
python3 scripts/validate_github_collection.py
python3 scripts/validate_wiki.py
git diff --check
```

Expected:

- all unit tests pass;
- GitHub packet validation adds no errors;
- any global wiki findings are listed as pre-existing or fixed before commit;
- `git diff --check` prints nothing.

- [ ] **Step 3: Run an offline Braintree ad hoc comparison smoke test**

Use the retained exact Braintree versions:

```bash
python3 scripts/collect_github_repos.py compare \
  --repo braintree/braintree-web \
  --from braintree-web@3.143.0 \
  --to braintree-web@3.144.0
```

Review generated `review-packet.json` and `review-packet.md`. Confirm exact
counts, zero gaps, deterministic rerun bytes, `delta`, and `high`. This command
must not alter `tracking/github/work-items.json` or wiki pages.

- [ ] **Step 4: Review the final diff**

```bash
git status --short
git diff --stat
git diff --check
```

Confirm no automatic wiki edits, no queue lifecycle transition, no unrelated
files, and no staged `CLAUDE copy.md`.

- [ ] **Step 5: Commit the workflow documentation**

```bash
git add rules/github-repos.md
# Run only when CLAUDE.md's workflow-index route changed:
git add CLAUDE.md
git commit -m "docs: define GitHub ingest packet workflow"
```

- [ ] **Step 6: Push and verify the exact remote commit**

```bash
git push origin main
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

Expected: local `HEAD` and `origin/main` resolve to the same full SHA.

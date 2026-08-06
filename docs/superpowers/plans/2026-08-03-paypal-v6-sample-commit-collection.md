# PayPal v6 Sample Commit Collection Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add reusable exact-default-branch GitHub collection and comparison support, then dry-run a bounded full-source capsule for `paypal-examples/v6-web-sdk-sample-integration` without publishing raw evidence or starting ingest.

**Architecture:** Add `commit-tree-v1` beside the existing NPM and tagged-tree adapters. Commit repositories use repository-qualified `ref_changes`, exact-SHA snapshots, commit comparisons, and a generated repository-level collection index; release repositories retain their current package-qualified records and behavior. The PayPal sample policy includes all selected client and Node server payment source while excluding tests, lockfiles, images, CI, deployment, generated output, dependencies, and real environment files.

**Tech Stack:** Python 3 standard library, `unittest`, Git CLI, TOML registry, canonical JSON, Markdown rules and generated status files.

## Global Constraints

- Read `CLAUDE.md`, `rules/github-repos.md`, and the approved design before each implementation session.
- Follow test-driven development: write one focused failing test, confirm the intended failure, implement the minimum behavior, and rerun focused tests.
- Do not change the output or behavior of `npm-tracked-source-v1` or `tagged-tree-v1` for existing release repositories.
- Do not fabricate semantic versions, package releases, tags, or release notes for commit repositories.
- Commit work items use `ref_changes`; release work items use `package_changes`; one item cannot contain both.
- Build and validate evidence in temporary storage before publishing any immutable artifact.
- Do not run package managers, builds, browser automation, or the sample application.
- Do not automatically edit wiki pages, approve a work item, call `next-ingest`, or start ingest.
- The first pilot dry run targets one current default-branch SHA and does not select historical commits.
- The pilot retains all selected client and server payment integration source, not only core PayPal flows.
- Leave unrelated files, including `CLAUDE copy.md` and user-owned Metronome work, untouched.
- The actual baseline collection is a separate user-approved action after the dry-run inventory is reviewed.

---

## File Structure

### New modules

- `scripts/github_commit_tree.py`: resolve one configured repository source identity from an exact commit tree.
- `scripts/github_collection_index.py`: build, render, load, and atomically publish repository-level collection state.
- `tests/test_github_commit_tree.py`: exact-tree selection and failure tests.
- `tests/test_github_collection_index.py`: generated JSON/Markdown and scheduling-state tests.
- `rules/github/release-tracked.md`: package-release discovery, comparison, and ingest routing.
- `rules/github/commit-tracked.md`: exact-SHA baseline, comparison, and ingest routing.
- `rules/github/supplements.md`: approved exact-SHA supplement routing.

### Existing modules with focused changes

- `scripts/github_capsule_policy.py`: adapter-specific `focus_packages` versus `source_id` schema.
- `scripts/github_registry.py`: enabled-policy validation by version strategy.
- `scripts/github_capsule_selection.py`: commit adapter dispatch and shared file selection.
- `scripts/github_work_items.py`: `RefChange`, mutual-exclusion validation, lifecycle serialization, and status rendering.
- `scripts/github_pilot_store.py`: default-branch comparison storage.
- `scripts/github_ingest_packets.py`: commit review-packet input and rendering.
- `scripts/collect_github_repos.py`: strategy dispatch, exact default-branch collection, unchanged detection, and index regeneration.
- `scripts/github_validation.py`: commit snapshots, comparisons, packets, work items, indexes, and ingested-page contracts.
- `tracking/github/repo-registry.toml`: reviewed PayPal sample capsule, enabled only after dry-run budget review.
- `rules/github-repos.md`: common workflow router rather than duplicated strategy detail.

---

### Task 1: Make Registry And Capsule Policy Commit-Aware

**Files:**
- Modify: `scripts/github_capsule_policy.py`
- Modify: `scripts/github_registry.py`
- Modify: `tests/test_github_capsule_policy.py`
- Modify: `tests/test_github_registry.py`

**Interfaces:**
- Produces: `COMMIT_TREE_ADAPTER = "commit-tree-v1"`
- Produces: `CapsuleConfig.source_id: str`
- Produces: `validate_enabled_policy(repo: RepoConfig) -> List[str]` with release and commit branches
- Consumes later: Tasks 2, 5, 6, and 7 use the normalized commit capsule contract.

- [ ] **Step 1: Add failing adapter-schema tests**

Add tests equivalent to:

```python
def test_commit_tree_policy_uses_repository_source_identity(self):
    capsule = CapsuleConfig(
        id="paypal-v6-sample-source",
        adapter="commit-tree-v1",
        source_id="v6-web-sdk-sample-integration",
        dependency_scope="configured-repository-paths",
        changed_path_policy="policy-bounded",
        default_required_roots=("client/components", "server/node/src"),
    )
    payload = json.loads(build_effective_policy(capsule, (), (), ()).canonical_bytes)
    self.assertEqual("exact-commit-tree-v1", payload["workspace_resolver"])
    self.assertEqual("v6-web-sdk-sample-integration", payload["source_id"])
    self.assertNotIn("focus_packages", payload)

def test_commit_tree_forbids_release_only_policy_fields(self):
    with self.assertRaisesRegex(ValueError, "commit-tree-v1 forbids focus_packages"):
        build_effective_policy(
            CapsuleConfig(
                id="invalid",
                adapter="commit-tree-v1",
                source_id="sample",
                focus_packages=("fake-package",),
            ),
            (), (), (),
        )
```

Add registry tests proving an enabled commit row requires `track="default-branch"`, no version tracks, exactly one commit capsule, and a nonempty safe `source_id`. Preserve existing enabled release-row assertions byte-for-byte.

- [ ] **Step 2: Run tests and confirm the missing-adapter failure**

Run:

```bash
python3 -m unittest tests.test_github_capsule_policy tests.test_github_registry
```

Expected: commit adapter/source identity tests fail; existing release tests continue to pass.

- [ ] **Step 3: Implement adapter-specific policy normalization**

Add:

```python
COMMIT_TREE_ADAPTER = "commit-tree-v1"
CAPSULE_ADAPTERS = frozenset((NPM_CAPSULE_ADAPTER, TAGGED_TREE_ADAPTER, COMMIT_TREE_ADAPTER))
WORKSPACE_RESOLVERS[COMMIT_TREE_ADAPTER] = "exact-commit-tree-v1"
DEPENDENCY_SCOPES[COMMIT_TREE_ADAPTER] = "configured-repository-paths"
```

Change `CapsuleConfig` so `focus_packages` defaults to `()` and `source_id` defaults to `""`. Parse `source_id` as an adapter-specific optional TOML key. Normalize with these exact rules:

- NPM/tagged adapters require `focus_packages` and forbid `source_id`.
- Commit adapter requires one safe `source_id` and empty `focus_packages`.
- Commit adapter forbids generated target paths and package overrides.
- The canonical policy payload contains only the identity field valid for its adapter.

Branch `validate_enabled_policy` by `version_strategy`: release strategies retain existing checks; `commit` requires default-branch tracking, no version tracks, and one commit capsule.

- [ ] **Step 4: Run policy and registry regression tests**

Run:

```bash
python3 -m unittest tests.test_github_capsule_policy tests.test_github_registry tests.test_github_npm_workspace tests.test_github_tagged_tree
```

Expected: all pass with unchanged release policy hashes in existing fixtures.

- [ ] **Step 5: Commit**

```bash
git add scripts/github_capsule_policy.py scripts/github_registry.py tests/test_github_capsule_policy.py tests/test_github_registry.py
git commit -m "feat: define commit tree collection policy"
```

---

### Task 2: Resolve A Bounded Exact-Commit Capsule

**Files:**
- Create: `scripts/github_commit_tree.py`
- Modify: `scripts/github_capsule_selection.py`
- Create: `tests/test_github_commit_tree.py`
- Modify: `tests/test_github_capsule_selection.py`

**Interfaces:**
- Produces: `resolve_commit_workspace(tree: GitTree, capsule: CapsuleConfig) -> WorkspaceResolution`
- Extends: `resolve_capsule_workspace(..., versions=None) -> WorkspaceResolution`
- Extends: `resolve_capsule(...) -> CapsuleResolution`
- Consumes: existing `GitTree`, category classifier, secret scanner, allowlist, hash, and budget logic.

- [ ] **Step 1: Add failing exact-tree workspace tests**

Build a local fixture repository containing client payment examples, server source, tests, lockfiles, an image, CI, `.env.sample`, a real `.env`, and an oversized file. Assert:

```python
workspace = resolve_commit_workspace(tree, capsule)
self.assertEqual(1, len(workspace.packages))
self.assertEqual("v6-web-sdk-sample-integration", workspace.packages[0].name)
self.assertEqual("", workspace.packages[0].version)
self.assertEqual("repository-source", workspace.packages[0].reason)
```

Assert required roots/includes expand only tracked regular blobs, are sorted, and fail when missing. The source identity is evidence metadata, not a package release.

- [ ] **Step 2: Run the new test and confirm import failure**

Run:

```bash
python3 -m unittest tests.test_github_commit_tree
```

Expected: failure because `github_commit_tree.py` does not exist.

- [ ] **Step 3: Implement exact-tree workspace resolution**

Implement `resolve_commit_workspace` to:

- require `COMMIT_TREE_ADAPTER`;
- enumerate tracked regular blobs from one exact `GitTree`;
- expand configured roots and literal includes;
- reject missing required paths and unsafe paths;
- return one immutable `WorkspacePackage` using `source_id`, empty version, no dependencies, and sorted owned paths; and
- avoid parsing NPM manifests, tags, build systems, or release metadata.

- [ ] **Step 4: Add failing capsule-dispatch and exclusion tests**

In `tests/test_github_capsule_selection.py`, prove commit resolution:

- includes configured client/server source, READMEs, manifests, and `.env.sample`;
- excludes `*.test.*`, test configuration classified as tests, lockfiles, images, `.github/`, deployment-only files, real `.env`, dependencies, and generated output;
- retains all selected local-payment examples;
- uses `source_id` in `CapsuleFile.package` only as the existing ownership field, while packet/work-item code treats it as repository evidence;
- fails closed on secrets, unsupported binary files selected explicitly, and file/byte budgets; and
- leaves NPM/tagged selection results unchanged.

- [ ] **Step 5: Add commit dispatch using shared safety logic**

Dispatch `resolve_capsule_workspace` and `resolve_capsule` to the new resolver when `capsule.adapter == COMMIT_TREE_ADAPTER`. Reuse existing selected-blob reads, category classification, secret scanning, allowlists, canonical policy hash, and budget checks. Do not duplicate those protections in `github_commit_tree.py`.

- [ ] **Step 6: Run selection tests**

Run:

```bash
python3 -m unittest tests.test_github_commit_tree tests.test_github_capsule_selection tests.test_github_npm_workspace tests.test_github_tagged_tree
```

Expected: all pass.

- [ ] **Step 7: Commit**

```bash
git add scripts/github_commit_tree.py scripts/github_capsule_selection.py tests/test_github_commit_tree.py tests/test_github_capsule_selection.py
git commit -m "feat: select exact commit source capsules"
```

---

### Task 3: Add Commit-Qualified Work Items And Recommendations

**Files:**
- Modify: `scripts/github_work_items.py`
- Modify: `tests/test_github_work_items.py`

**Interfaces:**
- Produces: `RefChange`
- Produces: `RefChangeSignals`
- Produces: `recommend_ref_ingest_mode(signals: RefChangeSignals) -> Tuple[str, Tuple[str, ...]]`
- Produces: `build_ref_work_item(...) -> WorkItem`
- Extends: `WorkItem.package_changes` and `WorkItem.ref_changes` as mutually exclusive tuples.

- [ ] **Step 1: Add failing commit work-item tests**

Add tests for:

```python
change = RefChange(
    ref_kind="default-branch",
    ref_name="main",
    from_sha="",
    to_sha="b" * 40,
    display_identity="default-branch@bbbbbbb",
    comparison_manifest="",
    recommended_mode="full",
    reasons=("initial-commit-baseline",),
)
item = build_ref_work_item(
    "paypal-examples/v6-web-sdk-sample-integration",
    "b" * 40,
    "2026-08-03",
    (change,),
    "raw/github/paypal-examples/v6-web-sdk-sample-integration/snapshots/2026-08-03-bbbbbbb/manifest.json",
)
self.assertEqual((), item.package_changes)
self.assertEqual((change,), item.ref_changes)
```

Also assert stable IDs, canonical save/load round trips, old release queue compatibility, package/ref mutual exclusion, exact SHA validation, default-branch display identity, lifecycle transitions, failure retry, approval, claim, and completion.

- [ ] **Step 2: Add failing mechanical recommendation tests**

Assert these exact results:

- empty `from_sha` -> `full`, `initial-commit-baseline`;
- 1 contained client file -> `delta`, `contained-commit-change`;
- server authentication/route paths -> `full`, `server-architecture-signal`;
- paths containing Orders, Vault, Subscriptions, eligibility, capture, or payment flow boundaries -> `full`, `payment-behavior-signal`;
- more than `BROAD_CHANGE_FILE_LIMIT` selected files -> `full`, `broad-change-set`.

- [ ] **Step 3: Run work-item tests and confirm failure**

Run:

```bash
python3 -m unittest tests.test_github_work_items
```

Expected: missing `RefChange`, `build_ref_work_item`, and ref recommendation failures.

- [ ] **Step 4: Implement optional commit change serialization**

Add immutable dataclasses and validators. Preserve legacy release JSON exactly by omitting empty `ref_changes`; commit items omit `package_changes` and include `ref_changes`. The parser accepts exactly one nonempty family. Work-item ID hashing uses repository, exact SHA, ref kind/name, and evidence revision for commit items.

Extend status rendering so commit items show `default-branch@<short-sha>`, from/to SHA, recommendation, comparison link, required reading, and lifecycle state without a package-release section.

- [ ] **Step 5: Run lifecycle regression tests**

Run:

```bash
python3 -m unittest tests.test_github_work_items
```

Expected: all release and commit tests pass.

- [ ] **Step 6: Commit**

```bash
git add scripts/github_work_items.py tests/test_github_work_items.py
git commit -m "feat: add commit-qualified GitHub work items"
```

---

### Task 4: Publish Commit Comparisons And Review Packets

**Files:**
- Modify: `scripts/github_pilot_store.py`
- Modify: `scripts/github_ingest_packets.py`
- Modify: `tests/test_github_pilot_store.py`
- Modify: `tests/test_github_ingest_packets.py`

**Interfaces:**
- Produces: `write_ref_comparison(root, config, repo_root, ref_name, from_sha, from_paths, to_sha, to_paths) -> ComparisonRecord`
- Produces: `RefPacketInput`
- Produces: `build_ref_ingest_packet(...) -> IngestPacket`
- Consumes: Task 3 `RefChange` and existing snapshot manifests.

- [ ] **Step 1: Add failing commit comparison tests**

Create two exact local commits with modified, added, renamed, deleted, and excluded files. Assert the output directory is:

```text
tracking/github/repos/paypal-examples/v6-web-sdk-sample-integration/
comparisons/default-branch/<from-short-sha>--<to-short-sha>/
```

Assert `comparison.json` records `ref_kind`, `ref_name`, full SHAs, pathspecs, upstream changes, hashes, and changed selected paths, with no package/version fields. Assert identical reruns reuse byte-identical artifacts and conflicting destinations fail closed.

- [ ] **Step 2: Add failing commit packet tests**

Construct `RefPacketInput` and assert packet JSON/Markdown contain:

- repository, exact ref identity, author/commit dates, and snapshot;
- baseline or comparison transition;
- required reading containing the packet's snapshot manifest and every selected file;
- selected changes, excluded changes, evidence gaps, and unclassified changes;
- deterministic full/delta recommendation; and
- expected PayPal source, commit changelog, company, concept-audit, index, and log targets.

Assert release packet fixtures remain byte-identical.

- [ ] **Step 3: Run store and packet tests and confirm failure**

Run:

```bash
python3 -m unittest tests.test_github_pilot_store tests.test_github_ingest_packets
```

Expected: missing commit comparison and packet interfaces.

- [ ] **Step 4: Implement commit comparison storage**

Factor only shared atomic write, Git diff, upstream change, hash, and scan behavior. Keep `write_package_comparison` output unchanged. `write_ref_comparison` writes the commit-specific schema and uses `default-branch/<from>--<to>` paths.

- [ ] **Step 5: Implement commit packet construction**

Add `build_ref_ingest_packet` as a commit-specific public entry point backed by shared packet validation/rendering. Do not add fake packages or release manifests. Add loader/summary support so approval and `next-ingest` validate commit packet required reading exactly like release packets.

- [ ] **Step 6: Run packet/store regression tests**

Run:

```bash
python3 -m unittest tests.test_github_pilot_store tests.test_github_ingest_packets
```

Expected: all pass, including existing canonical package packet hashes.

- [ ] **Step 7: Commit**

```bash
git add scripts/github_pilot_store.py scripts/github_ingest_packets.py tests/test_github_pilot_store.py tests/test_github_ingest_packets.py
git commit -m "feat: publish commit comparison packets"
```

---

### Task 5: Route Collection Through The Commit Strategy

**Files:**
- Modify: `scripts/collect_github_repos.py`
- Modify: `tests/test_collect_github_repos.py`
- Modify: `tests/test_github_pilot_e2e.py`

**Interfaces:**
- Produces: `CommitInventory(selected_file_count, selected_utf8_bytes, excluded_file_count, excluded_utf8_bytes)`
- Produces: `CommitCollectionResult(repo_id, state, ref_ids, snapshot_paths, work_item_ids, errors, inventory)`
- Adds internal: `_collect_commit_attempt(...) -> CommitCollectionResult`
- Adds internal: `_latest_accepted_ref(items, repo_id) -> Optional[WorkItem]`
- Consumes: Tasks 1-4 policy, selection, ref work-item, comparison, and packet interfaces.

- [ ] **Step 1: Add failing baseline and future collection tests**

Using local Git remotes, assert:

- `backfill` with no accepted baseline resolves the exact default branch and produces one full commit work item;
- `backfill` with an accepted baseline returns `unchanged`;
- `future` with unchanged SHA returns `unchanged`;
- changed SHA with selected byte-identical files returns `unchanged` and publishes nothing;
- excluded-only changes return `unchanged`;
- contained selected changes create a delta comparison/work item;
- broad selected changes create a full comparison/work item;
- `--release` for a commit repository raises `CollectionUsageError`;
- dry run returns ref identity plus selected/excluded counts and bytes but publishes no snapshot, packet, comparison, queue, or index; and
- an exact `--repo` combined with `--dry-run` may load one disabled row only when its complete policy validates;
- non-dry-run collection of a disabled row still fails before clone; and
- release repository tests remain unchanged.

- [ ] **Step 2: Run collection tests and confirm release-only failure**

Run:

```bash
python3 -m unittest tests.test_collect_github_repos tests.test_github_pilot_e2e
```

Expected: commit configurations fail in release candidate selection.

- [ ] **Step 3: Add top-level strategy dispatch**

Keep `collect_one` retry and failure protection common. Its return annotation becomes `Union[CollectionResult, CommitCollectionResult]`. Preserve `CollectionResult` and existing release CLI JSON exactly. Add a branch-specific serializer so commit output uses `ref_ids` and `inventory`, while release output retains `release_ids` and does not gain null commit fields.

Dispatch inside `_collect_attempt`:

```python
if config.version_strategy == "commit":
    return _collect_commit_attempt(...)
return _collect_release_attempt(...)
```

Move current release behavior into `_collect_release_attempt` without changing its inputs, output, ordering, or persisted artifacts.

- [ ] **Step 4: Implement exact default-branch collection**

The commit attempt must:

1. obtain the cloned repository's discovered default branch;
2. resolve and fetch its exact SHA;
3. construct `GitTree` at that SHA;
4. resolve the commit capsule;
5. find the last accepted ref item for the repository;
6. compare selected fingerprints before publishing;
7. publish one snapshot only for new selected evidence;
8. write a comparison only when a prior selected baseline exists;
9. build one `RefChange`, packet, and work item;
10. finalize at `awaiting_approval`; and
11. preserve existing retry/manual-review behavior.

Failure context must build a stable ref work-item identity even when failure occurs before snapshot publication. No release records or release-note requests execute in this branch.

In CLI repository selection, use `enabled_only=False` only for an exact `--repo` combined with `--dry-run`. Continue validating registry and capsule policy before clone. Do not permit company-wide, batch, or non-dry execution of disabled rows.

- [ ] **Step 5: Run collection and end-to-end tests**

Run:

```bash
python3 -m unittest tests.test_collect_github_repos tests.test_github_pilot_e2e
```

Expected: all release and commit scenarios pass.

- [ ] **Step 6: Commit**

```bash
git add scripts/collect_github_repos.py tests/test_collect_github_repos.py tests/test_github_pilot_e2e.py
git commit -m "feat: collect default branch GitHub evidence"
```

---

### Task 6: Generate And Validate The Repository Collection Index

**Files:**
- Create: `scripts/github_collection_index.py`
- Modify: `scripts/collect_github_repos.py`
- Modify: `scripts/github_validation.py`
- Create: `tests/test_github_collection_index.py`
- Modify: `tests/test_github_validation.py`

**Interfaces:**
- Produces: `CollectionIndexRow`
- Produces: `build_collection_index(repos, items, checked_state, today) -> dict`
- Produces: `render_collection_index(document: dict) -> str`
- Produces: `write_collection_index(root, repos, items, checked_state, today) -> None`
- Consumes: registry rows, release/ref work items, and per-run checked state.

- [ ] **Step 1: Add failing index tests**

Assert canonical JSON and Markdown include all 71 registry repositories and these exact actions:

- disabled row -> `disabled`;
- enabled repository without accepted work -> `collect-baseline`;
- unchanged and not due -> `wait`;
- awaiting delta -> `review-delta`;
- awaiting full -> `review-full`;
- approved/ingesting -> `ingest`;
- retryable collection failure -> `retry`;
- policy/manual failure -> `manual-review`.

Assert frequency computes `next_due_date` from last checked date for weekly/monthly values, output sorts by company/priority/repo ID, Markdown is deterministic, and malformed or mismatched views fail validation.

- [ ] **Step 2: Run index tests and confirm import failure**

Run:

```bash
python3 -m unittest tests.test_github_collection_index
```

Expected: failure because the index module does not exist.

- [ ] **Step 3: Implement repository-level index generation**

Use canonical JSON and atomic writes for:

```text
tracking/github/collection-index.json
tracking/github/collection-index.md
```

Each row includes repository identity, company, enabled, priority, strategy, adapter, frequency, last checked date, last accepted ref, latest discovered ref, comparison base, queue state, next due date, next action, and bounded last error.

Regenerate the index after non-dry-run collection results and lifecycle/status operations. Do not change index files during dry runs.

- [ ] **Step 4: Extend deterministic validation**

Inspect and validate both index files. Rebuild the expected Markdown from JSON, verify canonical JSON, registry coverage, known actions, exact repository ordering, work-item consistency, and absence of mutable registry fields.

Also extend snapshot, comparison, packet, work-item, and ingested-page validators for commit artifacts. Release validation remains strict and unchanged.

- [ ] **Step 5: Run index and validation tests**

Run:

```bash
python3 -m unittest tests.test_github_collection_index tests.test_github_validation
```

Expected: all pass.

- [ ] **Step 6: Run the complete offline GitHub suite**

Run:

```bash
python3 -m unittest discover -s tests -p 'test_github_*.py'
python3 -m unittest tests.test_collect_github_repos
python3 scripts/validate_github_collection.py
```

Expected: all tests pass and the validator reports no structural errors.

- [ ] **Step 7: Commit**

```bash
git add scripts/github_collection_index.py scripts/collect_github_repos.py scripts/github_validation.py tests/test_github_collection_index.py tests/test_github_validation.py tracking/github/collection-index.json tracking/github/collection-index.md
git commit -m "feat: generate GitHub collection strategy index"
```

---

### Task 7: Split Strategy Rules And Configure The Disabled Pilot

**Files:**
- Modify: `rules/github-repos.md`
- Create: `rules/github/release-tracked.md`
- Create: `rules/github/commit-tracked.md`
- Create: `rules/github/supplements.md`
- Modify: `CLAUDE.md`
- Modify: `tracking/github/repo-registry.toml`
- Modify: `tracking/github/collection-index.json`
- Modify: `tracking/github/collection-index.md`
- Modify: `tests/test_github_registry.py`

**Interfaces:**
- Produces: human routing from registry `version_strategy` to one strategy rule.
- Produces: complete but disabled PayPal sample `commit-tree-v1` policy for inventory dry run.

- [ ] **Step 1: Add failing registry assertions for the pilot policy**

Assert the PayPal sample row remains `repo_type="sample-app"`, tier 1, monthly, default-branch/commit, and initially disabled. Assert its one capsule has the exact roots/includes from the approved design, excludes tests/fixtures, uses `text-secrets-v1`, and has no package version tracks.

- [ ] **Step 2: Write focused strategy rules**

Move only strategy-specific detail from `rules/github-repos.md`. Keep common immutability, approval, serial ingest, failure, and validation rules in the main file. Add routing that requires reading:

- `release-tracked.md` for release strategies;
- `commit-tracked.md` for commit strategy; and
- `supplements.md` before supplement collection.

Document that scripts execute adapters from registry data; scripts do not parse Markdown rules to select behavior.

- [ ] **Step 3: Add the complete disabled capsule policy**

Add the approved roots/includes and conservative provisional dry-run limits:

```toml
max_file_bytes = 512000
max_capsule_files = 320
max_capsule_utf8_bytes = 3000000
max_packet_files = 370
max_packet_utf8_bytes = 4000000
```

Keep `enabled=false` until Task 8 reviews live inventory and replaces provisional budgets with measured values plus modest headroom.

Run `python3 scripts/collect_github_repos.py status` after changing registry policy so both generated collection-index views record the pilot's commit adapter while keeping `next_action="disabled"`.

- [ ] **Step 4: Run rules/registry and full offline validation**

Run:

```bash
python3 -m unittest tests.test_github_registry tests.test_github_capsule_policy
python3 -m unittest discover -s tests -p 'test_github_*.py'
python3 -m unittest tests.test_collect_github_repos
python3 scripts/validate_github_collection.py
```

Expected: all pass; existing enabled repositories remain executable; the complete disabled pilot policy is valid but not scheduled.

- [ ] **Step 5: Commit**

```bash
git add CLAUDE.md rules/github-repos.md rules/github/release-tracked.md rules/github/commit-tracked.md rules/github/supplements.md tracking/github/repo-registry.toml tracking/github/collection-index.json tracking/github/collection-index.md tests/test_github_registry.py
git commit -m "docs: route GitHub collection by strategy"
```

---

### Task 8: Run The PayPal Sample Inventory Dry Run And Enable The Pilot

**Files:**
- Modify after review: `tracking/github/repo-registry.toml`
- Modify: `tests/test_github_registry.py`
- Generated after policy change: `tracking/github/collection-index.json`
- Generated after policy change: `tracking/github/collection-index.md`

**Interfaces:**
- Consumes: complete disabled policy from Task 7.
- Produces: reviewed numeric budgets, `enabled=true`, and an index action of `collect-baseline`.
- Does not produce: raw snapshot, comparison, work item, packet, approval, or wiki edits.

- [ ] **Step 1: Run the network-enabled dry run**

First capture the scoped worktree state, then run with explicit network approval:

```bash
git status --porcelain=v1 --untracked-files=all -- raw/github tracking/github/work-items.json
python3 scripts/collect_github_repos.py collect \
  --repo paypal-examples/v6-web-sdk-sample-integration \
  --mode backfill \
  --dry-run
git status --porcelain=v1 --untracked-files=all -- raw/github tracking/github/work-items.json
```

Expected: `state="discovered"`, one exact default-branch SHA, selected/excluded file counts and UTF-8 bytes, zero snapshot paths, zero work-item IDs, and identical scoped worktree output before and after the dry run.

- [ ] **Step 2: Review inventory before enabling**

Confirm the selected list contains all intended client/server flows and excludes tests, lockfiles, images, CI, deployment, dependencies, generated output, and real `.env`. Inspect any secret finding, unsupported file, missing root, or unclassified path before proceeding.

Set each file/byte budget to the measured value plus 15 percent headroom, rounded up to a clear integer. Keep `max_file_bytes=512000` unless a selected text file legitimately requires a higher reviewed limit. Keep packet limits at least the selected count/bytes plus snapshot, packet, and comparison metadata headroom.

- [ ] **Step 3: Enable the reviewed pilot and update assertions**

Change only this row to `enabled=true`, update exact budget assertions, and run `python3 scripts/collect_github_repos.py status` to regenerate the collection index. The row must report `next_action="collect-baseline"` because no accepted snapshot exists.

- [ ] **Step 4: Run final deterministic verification**

Run:

```bash
python3 -m unittest tests.test_github_registry tests.test_collect_github_repos
python3 -m unittest discover -s tests -p 'test_github_*.py'
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all pass. Confirm `git status --short` contains only planned files plus pre-existing unrelated user files.

- [ ] **Step 5: Commit the enabled pilot**

```bash
git add tracking/github/repo-registry.toml tracking/github/collection-index.json tracking/github/collection-index.md tests/test_github_registry.py
git commit -m "feat: enable PayPal v6 sample collection"
```

- [ ] **Step 6: Stop at the real-collection approval gate**

Report the exact dry-run SHA, selected/excluded counts and bytes, capsule budget headroom, validation results, commit IDs, and unrelated worktree files. Request explicit approval before running the non-dry collection command.

---

## Final Review Checklist

- [ ] Existing release artifacts and work-item JSON remain byte-compatible.
- [ ] Commit repositories never create package release records.
- [ ] Default-branch reads are pinned to one exact SHA per run.
- [ ] Selected-evidence equality suppresses excluded-only or byte-identical changes.
- [ ] Commit comparisons and packets contain no fabricated package versions.
- [ ] Collection index covers every registry repository and matches its Markdown view.
- [ ] Pilot dry run publishes no raw evidence or queue item.
- [ ] Pilot capsule retains every intended payment integration source family.
- [ ] No automatic approval, ingest, wiki edit, build, or scheduler is introduced.
- [ ] All GitHub tests and deterministic validation pass.
- [ ] Unrelated worktree changes remain untouched.

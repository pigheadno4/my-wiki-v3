# PayPal Messages Braintree Policy Boundary Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add approval-gated exact-ref boundary collection for release-tracked repositories, then preserve and serially ingest the untagged PayPal Messages Braintree-only README changes for iOS and Android.

**Architecture:** Keep normal semantic-release discovery unchanged. Add an explicit `collect-ref` path that resolves two full SHAs, verifies direct ancestry, reuses or publishes immutable snapshots through the repository's existing capsule, creates a commit-qualified comparison and `ref_changes` work item, and stops at `awaiting_approval`. After separate packet approvals, ingest iOS and Android serially and then update the paired cross-platform analysis.

**Tech Stack:** Python 3 standard library, Git CLI, TOML registry, JSON/Markdown evidence artifacts, `unittest`, existing GitHub capsule/packet/work-item modules.

## Global Constraints

- Raw GitHub evidence is immutable and exact-SHA qualified.
- `paypal-messages-ios@1.2.0` at `432d6b832714b2615106c3f2a748ac61654d8bbd` remains the iOS released baseline.
- `paypal-messages-android@1.3.0` at `f1aa138cc6822cc11d68ac4bfdee3cf183aedbc2` remains the Android released baseline.
- The iOS boundary is `432d6b832714b2615106c3f2a748ac61654d8bbd -> fdd18681f486a3b2f1c60e3c47f8669f55a73a96`.
- The Android direct boundary is `1d2238c9e5ec3564ad5d8060c474e008ab7bf779 -> 0424354a5fa0ab697275186fe101d105838ac03e`; `v1.3.0` remains separate released context.
- Untagged commits create no package release record and must never be described as semantic releases.
- Exact-ref collection must not change normal monthly release scheduling or the latest accepted package release.
- Collection stops at `awaiting_approval`; ingest is serial, full-read, and separately approved for each work item.
- The Braintree wording is a documentation-policy and merchant-eligibility signal, not proof of a code-level compatibility change.
- Leave unrelated `CLAUDE copy.md` untouched.

## File Structure

- Modify `scripts/collect_github_repos.py`: exact-ref orchestration, CLI command, retries, and status generation.
- Modify `scripts/github_ingest_packets.py`: permit commit-qualified packets from an existing tagged-tree capsule.
- Modify `scripts/github_pilot_store.py`: generate ref comparisons using either a commit source ID or a tagged focus package.
- Modify `scripts/github_collection_index.py`: show pending exact-ref work without replacing release status or cadence.
- Modify `rules/github-repos.md` and `rules/github/release-tracked.md`: document exact-ref boundary use and approval rules.
- Modify `tests/test_collect_github_repos.py`: exact-ref collection and CLI lifecycle tests.
- Modify `tests/test_github_ingest_packets.py`: tagged-tree ref packet tests.
- Modify `tests/test_github_pilot_store.py`: tagged-tree ref comparison tests.
- Modify `tests/test_github_collection_index.py`: package-release status preservation tests.
- Generate `raw/github/paypal/paypal-messages-{ios,android}/snapshots/`: immutable boundary snapshots.
- Generate `tracking/github/repos/paypal/paypal-messages-{ios,android}/comparisons/default-branch/`: exact-ref comparisons.
- Generate `tracking/github/repos/paypal/paypal-messages-{ios,android}/ingest-packets/`: approval packets.
- Modify the two cumulative source pages and changelogs during serial ingest.
- Modify `wiki/analyses/analysis-paypal-messages-ios-vs-android.md` after both ingests.
- Modify root/PayPal indexes and logs only where required by the ingest and analysis rules.

---

### Task 1: Generalize Ref Evidence for Tagged-Tree Capsules

**Files:**
- Modify: `scripts/github_pilot_store.py:526-630`
- Modify: `scripts/github_ingest_packets.py:311-475`
- Test: `tests/test_github_pilot_store.py`
- Test: `tests/test_github_ingest_packets.py`

**Interfaces:**
- Consumes: `CapsuleConfig.adapter`, `CapsuleConfig.source_id`, and `CapsuleConfig.focus_packages`.
- Produces: `_ref_evidence_owner(capsule: CapsuleConfig) -> str`; `build_ref_ingest_packet(...)` accepting `commit-tree-v1` and `tagged-tree-v1` capsules without creating release evidence.

- [ ] **Step 1: Write failing store and packet tests**

Add a tagged-tree fixture with one focus package and assert that `write_ref_comparison()` writes `comparison.json`, `comparison.md`, and `diff.patch`. Add a packet test using two tagged-tree snapshots and this input:

```python
ref_input = RefPacketInput(
    ref_kind="default-branch",
    ref_name="develop",
    from_sha=before_sha,
    to_sha=after_sha,
    comparison_manifest=comparison_path,
    prior_snapshot_manifest=before_manifest,
    upstream_changes=changes,
    excluded_changes=(),
)
```

Assert that the packet has `ref`, not `packages`, contains no release manifest, and includes both snapshot manifests plus the comparison artifacts in `required_reading`.

- [ ] **Step 2: Run focused tests and verify the adapter guards fail**

Run:

```bash
python3 -m unittest \
  tests.test_github_pilot_store \
  tests.test_github_ingest_packets
```

Expected: the new tests fail because ref comparisons access an empty `source_id` and ref packets currently require `commit-tree-v1`.

- [ ] **Step 3: Add one evidence-owner helper**

Implement in `github_pilot_store.py`:

```python
def _ref_evidence_owner(capsule: CapsuleConfig) -> str:
    if capsule.adapter == COMMIT_TREE_ADAPTER:
        return capsule.source_id
    if capsule.adapter == TAGGED_TREE_ADAPTER and len(capsule.focus_packages) == 1:
        return capsule.focus_packages[0]
    raise PilotStoreError("ref comparison requires commit-tree-v1 or tagged-tree-v1")
```

Use this helper for generated comparison `CapsuleFile.package` instead of directly reading `capsule.source_id`.

- [ ] **Step 4: Permit tagged-tree ref packets**

Change the packet guard to:

```python
adapter = config.capsules[0].adapter
if adapter not in (COMMIT_TREE_ADAPTER, TAGGED_TREE_ADAPTER):
    raise PacketBuildError(
        "ref packet requires commit-tree-v1 or tagged-tree-v1"
    )
```

Keep `_validate_ref_input()` restricted to `ref_kind == "default-branch"`, and keep the existing exact-SHA, comparison, budget, required-reading, and wiki-target checks.

- [ ] **Step 5: Run focused tests**

Run the same two unittest modules. Expected: all tests pass.

- [ ] **Step 6: Commit Task 1**

```bash
git add scripts/github_pilot_store.py scripts/github_ingest_packets.py \
  tests/test_github_pilot_store.py tests/test_github_ingest_packets.py
git commit -m "Support tagged-tree ref evidence"
```

### Task 2: Add Exact-Ref Boundary Collection

**Files:**
- Modify: `scripts/collect_github_repos.py:100-740`
- Test: `tests/test_collect_github_repos.py`

**Interfaces:**
- Consumes: `RepoConfig`, two full SHAs, existing capsule policy, `publish_source_snapshot`, `write_ref_comparison`, `build_ref_ingest_packet`, and `build_ref_work_item`.
- Produces: `collect_ref_boundary(root: Path, config: RepoConfig, from_sha: str, to_sha: str, dry_run: bool = False, clone_source: Optional[Path] = None, collection_date: Optional[str] = None, max_attempts: int = 3) -> CommitCollectionResult`.

- [ ] **Step 1: Write failing exact-ref tests**

Create a local tagged-tree repository with `README.md`, `CHANGELOG.md`, one required source root, a before commit, an unrelated branch commit, and an after commit. Add tests asserting:

```python
result = collect_ref_boundary(
    root,
    config,
    before_sha,
    after_sha,
    clone_source=remote,
    collection_date="2026-08-13",
)
self.assertEqual("awaiting_approval", result.state)
self.assertEqual(("default-branch@" + after_sha[:7],), result.ref_ids)
```

Also assert:

- the work item has empty `package_changes` and one `ref_changes` entry;
- `from_sha` and `to_sha` are exact;
- both snapshots and one comparison exist;
- no release directory is created under the test repository's `raw/github/alpha/example/releases/` path;
- rerunning the same request returns `unchanged` without another snapshot or work item;
- a short SHA is rejected;
- identical SHAs are rejected;
- a non-ancestor pair is rejected;
- a disabled repository is rejected except in dry-run;
- an existing accepted `from` snapshot is reused.

- [ ] **Step 2: Run the new tests and verify failure**

Run:

```bash
python3 -m unittest \
  tests.test_collect_github_repos.ExactRefBoundaryCollectionTests
```

Expected: FAIL because `collect_ref_boundary` does not exist.

- [ ] **Step 3: Implement strict request validation**

Add a full-SHA regular expression and reject invalid requests before publication:

```python
_FULL_SHA = re.compile(r"[0-9a-f]{40}")

def _require_boundary_sha(value: str, label: str) -> str:
    if not isinstance(value, str) or _FULL_SHA.fullmatch(value) is None:
        raise CollectionUsageError(label + " must be a full lowercase Git SHA")
    return value
```

Require `from_sha != to_sha`, `max_attempts` from one through three, an enabled repository for non-dry-run, exactly one capsule, and adapter `tagged-tree-v1` or `commit-tree-v1`.

- [ ] **Step 4: Resolve refs and verify ancestry before writes**

Clone to temporary storage, fetch selectors in the form `commit:` followed by the full SHA, and run:

```python
try:
    run_git(["merge-base", "--is-ancestor", from_sha, to_sha], clone_path)
except GitCommandError as error:
    if error.returncode == 1:
        raise CollectionUsageError("from SHA must be an ancestor of to SHA") from error
    raise
```

Resolve the repository default branch name for `RefChange.ref_name`, but identify the evidence as `default-branch@` followed by the first seven characters of `to_sha` because the supplied SHA is immutable.

- [ ] **Step 5: Resolve both capsules without fabricating releases**

Use a helper that supplies adapter-specific selection metadata:

```python
def _ref_capsule_versions(capsule: CapsuleConfig, sha: str):
    if capsule.adapter == TAGGED_TREE_ADAPTER:
        return {capsule.focus_packages[0]: "unreleased-" + sha[:7]}
    return None
```

Call `resolve_capsule()` for both trees with changed paths and this metadata. The synthetic value is internal capsule ownership metadata only; it must not appear as a release identity or create a release record.

- [ ] **Step 6: Publish/reuse snapshots, comparison, packet, and work item**

Publish the before snapshot only when no exact-SHA snapshot exists. Always reuse an existing immutable match. Publish the after snapshot, then call `write_ref_comparison()` and `build_ref_ingest_packet()`.

Construct the change as:

```python
change = RefChange(
    ref_kind="default-branch",
    ref_name=default_branch,
    from_sha=from_sha,
    to_sha=to_sha,
    display_identity="default-branch@" + to_sha[:7],
    comparison_manifest=comparison_manifest,
    recommended_mode=packet.document["recommendation"]["mode"],
    reasons=tuple(packet.document["recommendation"]["reasons"]),
)
```

Reject publication if the packet has evidence gaps or unclassified changes. Finalize one work item at `awaiting_approval`; do not approve or ingest it.

- [ ] **Step 7: Add retry and failure behavior**

Use the existing retryable exception set and bounded failure recording. A failed run must not publish a partial destination, create a release record, or change existing accepted evidence. After retries are exhausted, preserve exact ref identity in the failed work item.

- [ ] **Step 8: Run focused tests**

Run the exact-ref test class. Expected: all tests pass.

- [ ] **Step 9: Commit Task 2**

```bash
git add scripts/collect_github_repos.py tests/test_collect_github_repos.py
git commit -m "Add exact-ref boundary collection"
```

### Task 3: Add CLI, Index Preservation, and Rules

**Files:**
- Modify: `scripts/collect_github_repos.py:1790-1955`
- Modify: `scripts/github_collection_index.py:250-390`
- Modify: `rules/github-repos.md`
- Modify: `rules/github/release-tracked.md`
- Test: `tests/test_collect_github_repos.py`
- Test: `tests/test_github_collection_index.py`

**Interfaces:**
- Consumes: `collect_ref_boundary(...)` from Task 2.
- Produces: CLI `collect-ref --repo paypal/paypal-messages-ios --from 432d6b832714b2615106c3f2a748ac61654d8bbd --to fdd18681f486a3b2f1c60e3c47f8669f55a73a96 [--dry-run]`; collection-index logic that exposes actionable ref work while preserving package-release status and cadence.

- [ ] **Step 1: Write failing CLI and index tests**

Assert parser acceptance for:

```bash
python3 scripts/collect_github_repos.py collect-ref \
  --repo paypal/paypal-messages-ios \
  --from 432d6b832714b2615106c3f2a748ac61654d8bbd \
  --to fdd18681f486a3b2f1c60e3c47f8669f55a73a96 \
  --dry-run
```

Build an index fixture containing an ingested package release plus an `awaiting_approval` ref boundary. Assert:

- `last_accepted_ref` remains the package-qualified release;
- `last_checked_date`, `next_due_date`, and normal cadence are unchanged by exact-ref collection;
- while pending, `latest_discovered_ref` shows the exact `default-branch@` short-SHA identity and `next_action` is `review-delta` or `review-full`;
- after the ref item is `ingested`, `latest_discovered_ref` returns to the release scan value and `last_accepted_ref` remains package-qualified.

- [ ] **Step 2: Run focused tests and verify failure**

```bash
python3 -m unittest \
  tests.test_collect_github_repos \
  tests.test_github_collection_index
```

Expected: the new CLI and release-preservation assertions fail.

- [ ] **Step 3: Add the CLI command**

Add:

```python
collect_ref = commands.add_parser("collect-ref")
collect_ref.add_argument("--repo", required=True)
collect_ref.add_argument("--from", dest="from_sha", required=True)
collect_ref.add_argument("--to", dest="to_sha", required=True)
collect_ref.add_argument("--dry-run", action="store_true")
```

Route it to `collect_ref_boundary()` before the ordinary `collect_one()` path and print the existing `CommitCollectionResult` payload.

- [ ] **Step 4: Preserve release-oriented collection-index fields**

For repositories whose `version_strategy != "commit"`:

- select `last_accepted_ref` only from accepted work items with `package_changes`;
- let an actionable exact-ref item drive `queue_state` and `next_action`;
- let a pending exact-ref item temporarily drive `latest_discovered_ref` and `comparison_base`;
- do not persist an exact-ref run into checked release-scan fields;
- after the exact-ref item reaches `ingested`, render release identity and cadence from the latest release item or checked release scan.

Do not change index behavior for `version_strategy == "commit"` repositories.

- [ ] **Step 5: Document exact-ref boundaries**

Add the command and these rules to both GitHub rule files:

- exact refs are opt-in query evidence, not scheduled release discovery;
- `from` must be an ancestor of `to`;
- release-tracked repositories keep semantic release authority;
- untagged work uses `ref_changes` and creates no release record;
- collection stops at approval and serial ingest still applies.

- [ ] **Step 6: Run focused and full tests**

```bash
python3 -m unittest \
  tests.test_collect_github_repos \
  tests.test_github_collection_index
python3 -m unittest discover -s tests
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all tests and validators pass.

- [ ] **Step 7: Commit Task 3**

```bash
git add scripts/collect_github_repos.py scripts/github_collection_index.py \
  rules/github-repos.md rules/github/release-tracked.md \
  tests/test_collect_github_repos.py tests/test_github_collection_index.py
git commit -m "Expose exact-ref boundary workflow"
```

### Task 4: Collect and Review Both Boundaries

**Files:**
- Generate: `raw/github/paypal/paypal-messages-ios/snapshots/2026-08-13-fdd1868/`
- Generate: `raw/github/paypal/paypal-messages-android/snapshots/2026-08-13-1d2238c/`
- Generate: `raw/github/paypal/paypal-messages-android/snapshots/2026-08-13-0424354/`
- Generate: corresponding comparison, packet, work-item, status, and collection-index artifacts under `tracking/github/`

**Interfaces:**
- Consumes: `collect-ref` from Task 3 and the existing accepted iOS `1.2.0` snapshot.
- Produces: two independently reviewable work items at `awaiting_approval`.

- [ ] **Step 1: Dry-run iOS**

```bash
python3 scripts/collect_github_repos.py collect-ref \
  --repo paypal/paypal-messages-ios \
  --from 432d6b832714b2615106c3f2a748ac61654d8bbd \
  --to fdd18681f486a3b2f1c60e3c47f8669f55a73a96 \
  --dry-run
```

Verify the retained `1.2.0` snapshot is reusable and no filesystem evidence changes occur.

- [ ] **Step 2: Collect iOS boundary**

Run the same command without `--dry-run`. Read the generated packet, manifest, comparison Markdown, and patch in full. Confirm only README is changed and the packet has no evidence gaps or unclassified changes.

- [ ] **Step 3: Dry-run and collect Android boundary**

```bash
python3 scripts/collect_github_repos.py collect-ref \
  --repo paypal/paypal-messages-android \
  --from 1d2238c9e5ec3564ad5d8060c474e008ab7bf779 \
  --to 0424354a5fa0ab697275186fe101d105838ac03e \
  --dry-run
python3 scripts/collect_github_repos.py collect-ref \
  --repo paypal/paypal-messages-android \
  --from 1d2238c9e5ec3564ad5d8060c474e008ab7bf779 \
  --to 0424354a5fa0ab697275186fe101d105838ac03e
```

Read the generated packet and every comparison artifact in full. Confirm README is the only boundary change. Separately verify retained Android `v1.3.0` README lacks the disclaimer.

- [ ] **Step 4: Validate and commit collection evidence**

```bash
python3 scripts/validate_github_collection.py
git diff --check
```

Commit only generated boundary evidence and tracking state:

```bash
git add raw/github/paypal/paypal-messages-ios \
  raw/github/paypal/paypal-messages-android \
  tracking/github
git commit -m "Collect PayPal Messages Braintree policy boundaries"
```

- [ ] **Step 5: Stop for packet approval**

Report both work-item IDs, exact boundaries, packet recommendations, required-reading counts, and any evidence gaps. Do not approve, claim, or ingest either item until the user explicitly approves it.

### Task 5: Serially Ingest the iOS Policy Delta

**Files:**
- Modify: `wiki/sources/paypal/github/source-github-paypal-messages-ios.md`
- Modify: `wiki/sources/paypal/github/changelog-github-paypal-messages-ios.md`
- Modify: `wiki/concepts/paypal-pay-later.md`
- Modify: `wiki/paypal-index.md`
- Modify: `wiki/paypal-log.md`
- Modify: `wiki/log.md`

**Interfaces:**
- Consumes: explicitly approved iOS work item and its complete required-reading list.
- Produces: version-preserving iOS source/changelog updates and a completed iOS work item.

- [ ] **Step 1: Claim only the approved iOS item**

```bash
python3 scripts/collect_github_repos.py next-ingest
```

Verify the claimed ID is the approved iOS boundary. If it is not, stop without editing wiki pages.

- [ ] **Step 2: Perform the complete serial read**

Read the cumulative source page, changelog, packet JSON/Markdown, manifests, comparison files, and every path in `required_reading` in full, one by one.

- [ ] **Step 3: Append unreleased policy history**

Add an `Unreleased documentation-policy change - default-branch@fdd1868` section. State that the README now requires Braintree account/SDK integration and excludes PPCP SDK integrations, while `paypal-messages-ios@1.2.0` remains the latest ingested tagged package and its README recommended the PayPal iOS SDK.

Do not rewrite old `1.2.0` behavior as Braintree-only. Add exact snapshot and comparison paths to the source and changelog.

- [ ] **Step 4: Validate and complete the work item**

```bash
python3 scripts/validate_wiki.py \
  wiki/sources/paypal/github/source-github-paypal-messages-ios.md \
  wiki/sources/paypal/github/changelog-github-paypal-messages-ios.md \
  wiki/paypal-log.md
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py complete-ingest --item "$IOS_ITEM_ID"
git diff --check
```

- [ ] **Step 5: Commit Task 5**

Set `IOS_ITEM_ID` to the exact iOS work-item ID reported in Task 4. Stage only the iOS ingest pages and generated lifecycle state. Commit:

```bash
git commit -m "Ingest PayPal Messages iOS policy boundary"
```

### Task 6: Serially Ingest the Android Policy Delta

**Files:**
- Modify: `wiki/sources/paypal/github/source-github-paypal-messages-android.md`
- Modify: `wiki/sources/paypal/github/changelog-github-paypal-messages-android.md`
- Modify: `wiki/concepts/paypal-pay-later.md`
- Modify: `wiki/paypal-index.md`
- Modify: `wiki/paypal-log.md`
- Modify: `wiki/log.md`

**Interfaces:**
- Consumes: explicitly approved Android work item after iOS reaches `ingested`.
- Produces: version-preserving Android source/changelog updates and a completed Android work item.

- [ ] **Step 1: Claim only the approved Android item**

Run `next-ingest` and verify the claimed work-item ID before editing.

- [ ] **Step 2: Perform the complete serial read**

Read the cumulative source page, changelog, packet JSON/Markdown, both new manifests, comparison files, every required path, and the retained `v1.3.0` README in full.

- [ ] **Step 3: Append unreleased policy history**

Add an `Unreleased documentation-policy change - default-branch@0424354` section. Identify `1d2238c -> 0424354` as the direct default-branch boundary and keep `paypal-messages-android@1.3.0` as separate released context whose README lacks the disclaimer.

Do not infer code incompatibility from the README-only delta. Add exact snapshot and comparison paths.

- [ ] **Step 4: Validate and complete the work item**

Set `ANDROID_ITEM_ID` to the exact Android work-item ID reported in Task 4. Run targeted `validate_wiki`, `validate_github_collection.py`, `python3 scripts/collect_github_repos.py complete-ingest --item "$ANDROID_ITEM_ID"`, and `git diff --check`.

- [ ] **Step 5: Commit Task 6**

```bash
git commit -m "Ingest PayPal Messages Android policy boundary"
```

### Task 7: Update the Paired Analysis and Verify the Campaign

**Files:**
- Modify: `wiki/analyses/analysis-paypal-messages-ios-vs-android.md`
- Modify: `wiki/index.md`
- Modify: `wiki/paypal-index.md`
- Modify: `wiki/log.md`
- Modify: `wiki/paypal-log.md`

**Interfaces:**
- Consumes: both ingested repository histories.
- Produces: one cross-platform merchant recommendation with an explicit released-versus-unreleased timeline.

- [ ] **Step 1: Add the shared policy timeline**

Document:

- iOS tagged `1.2.0` README before policy and untagged `fdd1868` after policy;
- Android tagged `1.3.0` release context, direct `1d2238c -> 0424354` branch boundary, and untagged status;
- current repository recommendation: use with Braintree account and Braintree SDK; PPCP SDK integrations are unsupported;
- evidence limitation: README policy does not prove a code-level compatibility switch.

- [ ] **Step 2: Update navigation and logs without duplicating the analysis entry**

Keep the existing root and PayPal index links and update both descriptions to mention the untagged Braintree-only policy boundary. Append one concise cross-platform analysis log entry after both serial ingests.

- [ ] **Step 3: Run final verification**

```bash
python3 scripts/validate_wiki.py \
  wiki/analyses/analysis-paypal-messages-ios-vs-android.md \
  wiki/sources/paypal/github/source-github-paypal-messages-ios.md \
  wiki/sources/paypal/github/changelog-github-paypal-messages-ios.md \
  wiki/sources/paypal/github/source-github-paypal-messages-android.md \
  wiki/sources/paypal/github/changelog-github-paypal-messages-android.md \
  wiki/paypal-log.md
python3 scripts/validate_github_collection.py
python3 -m unittest discover -s tests
git diff --check
```

Expected: all deterministic validators pass and the complete unittest suite reports zero failures.

- [ ] **Step 4: Commit Task 7**

```bash
git add wiki/analyses/analysis-paypal-messages-ios-vs-android.md \
  wiki/index.md wiki/paypal-index.md wiki/log.md wiki/paypal-log.md
git commit -m "Analyze PayPal Messages Braintree policy shift"
```

- [ ] **Step 5: Report completion and next step**

Report exact commits, test counts, collection/ingest state, the merchant-facing conclusion, and whether the branch has been pushed. The next operational step is monitoring future tagged releases to determine which first includes the Braintree-only disclaimer.

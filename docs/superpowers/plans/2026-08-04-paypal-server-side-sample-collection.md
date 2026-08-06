# PayPal Server-Side Sample Collection Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Configure and collect one bounded exact-commit baseline for `paypal-examples/paypal-sdk-server-side-integration`, stopping at the approval gate before wiki ingest.

**Architecture:** Reuse the existing `commit-tree-v1` adapter and registry-driven collector. First register a complete but disabled capsule, use the supported dry run to verify its live inventory, then enable and collect one immutable default-branch baseline. No collector behavior or wiki page is changed by this plan.

**Tech Stack:** Python 3 standard library, `unittest`, Git CLI, TOML registry, canonical JSON, Markdown tracking views.

## Global Constraints

- Read `CLAUDE.md`, `rules/github-repos.md`, `rules/github/commit-tracked.md`, and the approved design before execution.
- Include Orders, Hosted Fields, client-token, shipping, and subscription create/activate/revise evidence.
- Include `src/`, `public/`, `docs/`, `README.md`, `example.env`, `package.json`, and `tsconfig.json`.
- Exclude tests, lockfiles, CI, development tooling, generated output, dependencies, Git metadata, and real environment files.
- Track the remote default branch by exact full commit SHA; do not fabricate package versions or release records.
- Do not run package managers, the sample application, or browser automation.
- Do not approve a work item, call `next-ingest`, edit wiki pages, or start ingest.
- Leave unrelated Metronome, ingest-pilot, and untracked user files untouched.

---

## File Structure

- Modify `tracking/github/repo-registry.toml`: stable capsule policy and enabled state.
- Modify `tests/test_github_registry.py`: exact policy and inventory assertions.
- Regenerate `tracking/github/collection-index.json`: machine-readable schedule state.
- Regenerate `tracking/github/collection-index.md`: deterministic operator view.
- Generate during collection under `raw/github/paypal/paypal-sdk-server-side-integration/`: immutable exact-SHA snapshot.
- Generate during collection under `tracking/github/repos/paypal/paypal-sdk-server-side-integration/`: deterministic ingest packet.
- Modify during collection `tracking/github/work-items.json` and `tracking/github/status.md`: approval-gated work-item state.

---

### Task 1: Register A Complete Disabled Capsule

**Files:**
- Modify: `tracking/github/repo-registry.toml`
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/collection-index.json`
- Modify: `tracking/github/collection-index.md`

**Interfaces:**
- Produces: one valid disabled `commit-tree-v1` profile for `paypal-examples/paypal-sdk-server-side-integration`.
- Consumes later: Task 2 passes this profile to the existing exact-repository dry-run path.

- [ ] **Step 1: Add a failing registry-policy test**

Add `test_paypal_server_side_sample_has_reviewed_disabled_commit_policy` beside the existing PayPal v6 sample test. Assert the repository is disabled, tier 1, monthly, `track="default-branch"`, `version_strategy="commit"`, has no version tracks, and has exactly one capsule with:

```python
self.assertEqual("commit-tree-v1", capsule.adapter)
self.assertEqual("paypal-sdk-server-side-integration", capsule.source_id)
self.assertEqual(("docs", "public", "src"), capsule.default_required_roots)
self.assertEqual(
    ("README.md", "example.env", "package.json", "tsconfig.json"),
    capsule.include_paths,
)
self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
self.assertEqual("text-secrets-v1", capsule.secret_detector)
self.assertEqual(512000, capsule.max_file_bytes)
self.assertEqual(50, capsule.max_capsule_files)
self.assertEqual(250000, capsule.max_capsule_utf8_bytes)
self.assertEqual(60, capsule.max_packet_files)
self.assertEqual(900000, capsule.max_packet_utf8_bytes)
```

- [ ] **Step 2: Run the focused test and confirm it fails**

Run:

```bash
python3 -m unittest tests.test_github_registry.GitHubRegistryTests.test_paypal_server_side_sample_has_reviewed_disabled_commit_policy
```

Expected: failure because the disabled inventory row has no capsule.

- [ ] **Step 3: Add the approved disabled capsule**

Keep `enabled=false` and append this capsule beneath the existing repository row:

```toml
[[repos.capsules]]
id="paypal-server-side-sample-source"
adapter="commit-tree-v1"
source_id="paypal-sdk-server-side-integration"
dependency_scope="configured-repository-paths"
changed_path_policy="policy-bounded"
default_required_roots=["docs","public","src"]
include_paths=["README.md","example.env","package.json","tsconfig.json"]
excluded_categories=["tests","fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=512000
max_capsule_files=50
max_capsule_utf8_bytes=250000
max_packet_files=60
max_packet_utf8_bytes=900000
```

This reviewed limit includes the 754,799-byte required-reading set measured during the first publication attempt and leaves 145,201 bytes of headroom for mandatory wiki context.

- [ ] **Step 4: Regenerate and validate disabled state**

Run:

```bash
python3 scripts/collect_github_repos.py status
python3 -m unittest tests.test_github_registry
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all pass; the collection index reports adapter `commit-tree-v1` and `next_action="disabled"` for this repository.

- [ ] **Step 5: Commit the disabled profile**

```bash
git add tracking/github/repo-registry.toml tracking/github/collection-index.json tracking/github/collection-index.md tests/test_github_registry.py
git commit -m "feat: configure PayPal server-side sample capsule"
```

---

### Task 2: Dry-Run The Inventory And Enable Collection

**Files:**
- Modify: `tracking/github/repo-registry.toml`
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/collection-index.json`
- Modify: `tracking/github/collection-index.md`

**Interfaces:**
- Consumes: the complete disabled profile from Task 1.
- Produces: a reviewed enabled profile whose next action is `collect-baseline`.
- Does not produce: raw snapshots, packets, comparisons, work items, or wiki edits.

- [ ] **Step 1: Record scoped state and run the network dry run**

Run with explicit network approval:

```bash
git status --porcelain=v1 --untracked-files=all -- raw/github tracking/github/work-items.json tracking/github/repos/paypal/paypal-sdk-server-side-integration
python3 scripts/collect_github_repos.py collect --repo paypal-examples/paypal-sdk-server-side-integration --mode backfill --dry-run
git status --porcelain=v1 --untracked-files=all -- raw/github tracking/github/work-items.json tracking/github/repos/paypal/paypal-sdk-server-side-integration
```

Expected: `state="discovered"`, one exact default-branch SHA, selected and excluded counts/bytes, zero snapshot paths, zero work-item IDs, and identical scoped Git state before and after.

- [ ] **Step 2: Review the exact dry-run inventory**

Confirm all selected paths belong to `src/`, `public/`, `docs/`, or the four literal root files. Confirm subscription create, activate, and revise source plus browser examples are selected. Confirm tests, `package-lock.json`, `.github/`, lint/format/version tooling, and real environment files are excluded. Stop on any secret finding, missing required root, unsupported file, or budget error.

- [ ] **Step 3: Enable only the reviewed repository**

Change this row to `enabled=true`. In `APPENDIX_A_INVENTORY`, change only this repository's enabled value from `False` to `True`; rename the focused test to `test_paypal_server_side_sample_has_reviewed_enabled_commit_policy` and assert `self.assertTrue(repo.enabled)`.

Run:

```bash
python3 scripts/collect_github_repos.py status
```

Expected: the collection index reports `next_action="collect-baseline"`.

- [ ] **Step 4: Run deterministic verification**

```bash
python3 -m unittest tests.test_github_registry tests.test_collect_github_repos
python3 -m unittest discover -s tests -p 'test_github_*.py'
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all tests and validators pass. The only planned changes are the registry, registry test, and two generated collection-index files.

- [ ] **Step 5: Commit the enabled profile**

```bash
git add tracking/github/repo-registry.toml tracking/github/collection-index.json tracking/github/collection-index.md tests/test_github_registry.py
git commit -m "feat: enable PayPal server-side sample collection"
```

- [ ] **Step 6: Stop at the baseline-collection approval gate**

Report the exact dry-run SHA, selected/excluded counts and bytes, validation results, and commit IDs. Request explicit approval before Task 3.

---

### Task 3: Publish The Baseline And Stop Before Ingest

**Files:**
- Create: `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/<collection-date>-<short-sha>/manifest.json`
- Create: `raw/github/paypal/paypal-sdk-server-side-integration/snapshots/<collection-date>-<short-sha>/files/`
- Create: `tracking/github/repos/paypal/paypal-sdk-server-side-integration/ingest-packets/<work-item-id>/packet.json`
- Create: `tracking/github/repos/paypal/paypal-sdk-server-side-integration/ingest-packets/<work-item-id>/packet.md`
- Modify: `tracking/github/work-items.json`
- Modify: `tracking/github/status.md`
- Modify: `tracking/github/collection-index.json`
- Modify: `tracking/github/collection-index.md`

**Interfaces:**
- Consumes: the enabled, dry-run-verified registry profile.
- Produces: one immutable exact-SHA snapshot and one work item in `awaiting_approval`.
- Does not produce: wiki edits, approval, ingest claim, or source-page changes.

- [ ] **Step 1: Run the approved baseline collection**

Run with explicit network approval:

```bash
python3 scripts/collect_github_repos.py collect --repo paypal-examples/paypal-sdk-server-side-integration --mode backfill
```

Expected: one snapshot path, one work-item ID, one exact `default-branch@<short-sha>` ref, and `state="awaiting_approval"`.

- [ ] **Step 2: Validate immutable evidence and queue state**

```bash
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py status
git diff --check
```

Inspect the manifest and packet to confirm the snapshot SHA matches the resolved default branch, all selected hashes are present, no package release record was created, the recommendation is `full`, and expected wiki targets are listed without being created.

- [ ] **Step 3: Commit only collected evidence and generated tracking**

```bash
git add raw/github/paypal/paypal-sdk-server-side-integration tracking/github/repos/paypal/paypal-sdk-server-side-integration tracking/github/work-items.json tracking/github/status.md tracking/github/collection-index.json tracking/github/collection-index.md
git commit -m "feat: collect PayPal server-side sample baseline"
```

- [ ] **Step 4: Stop at serial-ingest review**

Report the work-item ID, exact SHA, selected/excluded counts and bytes, required-reading count, evidence gaps, unclassified paths, and recommendation. Do not approve or ingest until the user reviews those findings.

---

## Final Review Checklist

- [ ] The repository is tracked by exact default-branch commit, not a package version.
- [ ] Orders, Hosted Fields, client tokens, shipping, and all three subscription operations are retained.
- [ ] Tests, lockfiles, CI, tooling, generated output, dependencies, Git metadata, and real environment files are excluded.
- [ ] Dry run publishes no immutable evidence or queue state.
- [ ] Real collection creates one snapshot and one `awaiting_approval` work item.
- [ ] No wiki page, approval, or ingest state is created automatically.
- [ ] Full GitHub tests and deterministic validation pass.
- [ ] Unrelated worktree changes remain untouched.

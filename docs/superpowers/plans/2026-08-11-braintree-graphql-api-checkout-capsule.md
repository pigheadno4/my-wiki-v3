# Braintree GraphQL API Checkout Capsule Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable commit-qualified collection of the monolithic `braintree/graphql-api` schema, changelog, and README, then publish one immutable baseline work item that stops at packet review.

**Architecture:** Extend `commit-tree-v1` required-path resolution to accept either an exact regular file or the existing directory prefix without changing registry schema. Configure one narrowly bounded Braintree capsule for the repository's three root files, validate it, and use the common collector to publish an exact-SHA baseline without editing wiki knowledge.

**Tech Stack:** Python 3 `unittest`, TOML registry configuration, Git, existing GitHub collection CLI, JSON, immutable raw evidence.

## Global Constraints

- Collect `schema.graphql`, `CHANGELOG.md`, and `README.md` verbatim from one resolved default-branch SHA.
- `schema.graphql` is required evidence; do not create a derived checkout-only raw schema.
- Deep future ingest is limited to checkout, transactions, payment methods, vaulting, PayPal, Venmo, 3D Secure, and recurring billing; other domains receive only high-level inventory.
- Preserve existing directory-prefix behavior for every current `commit-tree-v1` capsule.
- Per-file limit is 650,000 bytes; capsule limits are 3 files and 800,000 UTF-8 bytes; packet limits are 6 files and 1,500,000 UTF-8 bytes.
- Missing required evidence, hash failure, strict UTF-8 failure, secret finding, or budget overflow must stop without partial publication.
- Baseline collection stops at `awaiting_approval`; do not approve, call `next-ingest`, or edit `wiki/`.
- Leave unrelated workspace files, including `CLAUDE copy.md`, untouched.

---

### Task 1: Support exact files as commit-tree required paths

**Files:**
- Modify: `tests/test_github_commit_tree.py`
- Modify: `scripts/github_commit_tree.py`

**Interfaces:**
- Consumes: `resolve_commit_workspace(tree: GitTree, capsule: CapsuleConfig) -> WorkspaceResolution`.
- Produces: required-path matching where an entry owns an exact regular file when present, otherwise all regular descendants of that directory prefix.

- [ ] **Step 1: Add the failing exact-file test**

Add this method to `CommitWorkspaceTests`:

```python
def test_resolves_exact_file_as_required_path(self):
    workspace = resolve_commit_workspace(
        self.tree(),
        self.capsule(
            default_required_roots=("README.md",),
            include_paths=(".env.sample",),
        ),
    )

    self.assertEqual(
        (".env.sample", "README.md"),
        workspace.packages[0].owned_paths,
    )
```

Extend `test_rejects_missing_required_root_and_include` with an exact missing file case:

```python
(
    self.capsule(default_required_roots=("missing.graphql",)),
    "missing-required-root",
),
```

- [ ] **Step 2: Run the focused test and verify it fails**

Run:

```bash
python3 -m unittest tests.test_github_commit_tree.CommitWorkspaceTests.test_resolves_exact_file_as_required_path
```

Expected: FAIL with `needs-policy-review:missing-required-root` because the adapter currently checks only `root + "/"` descendants.

- [ ] **Step 3: Implement exact-file-or-directory matching**

Replace the required-root loop in `resolve_commit_workspace` with:

```python
for root in normalized.default_required_roots:
    matches = {root} if root in regular_paths else {
        path for path in regular_paths if path.startswith(root + "/")
    }
    if not matches:
        _review(
            "missing-required-root",
            "source=" + normalized.source_id + " path=" + root,
        )
    owned_paths.update(matches)
```

Keep the existing error code for compatibility with generated diagnostics and tests.

- [ ] **Step 4: Run focused and regression tests**

Run:

```bash
python3 -m unittest tests.test_github_commit_tree
python3 -m unittest tests.test_github_capsule_policy tests.test_github_capsule_selection
```

Expected: all tests pass, including the existing directory-prefix fixture.

- [ ] **Step 5: Commit the shared adapter change**

```bash
git add scripts/github_commit_tree.py tests/test_github_commit_tree.py
git diff --cached --check
git commit -m "feat: support root files in commit capsules"
```

### Task 2: Enable the Braintree GraphQL API capsule

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`

**Interfaces:**
- Consumes: exact-file required-path support from Task 1 and `load_registry(path)`.
- Produces: one enabled monthly tier-1 commit policy with capsule ID `braintree-graphql-api-schema` and source ID `braintree-graphql-api`.

- [ ] **Step 1: Add the failing registry contract test**

Add this method to `RegistryTests` near other Braintree profile tests:

```python
def test_braintree_graphql_api_has_reviewed_commit_policy(self):
    repos = {
        repo.id: repo
        for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
    }
    repo = repos["braintree/graphql-api"]

    self.assertTrue(repo.enabled)
    self.assertEqual("api-specification", repo.repo_type)
    self.assertEqual("tier1", repo.priority)
    self.assertEqual("monthly", repo.collection_frequency)
    self.assertEqual("default-branch", repo.track)
    self.assertEqual("commit", repo.version_strategy)
    self.assertEqual((), repo.version_tracks)
    self.assertEqual(1, len(repo.capsules))
    capsule = repo.capsules[0]
    self.assertEqual("braintree-graphql-api-schema", capsule.id)
    self.assertEqual("commit-tree-v1", capsule.adapter)
    self.assertEqual("braintree-graphql-api", capsule.source_id)
    self.assertEqual("configured-repository-paths", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(("schema.graphql",), capsule.default_required_roots)
    self.assertEqual(("CHANGELOG.md", "README.md"), capsule.include_paths)
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual(650000, capsule.max_file_bytes)
    self.assertEqual(3, capsule.max_capsule_files)
    self.assertEqual(800000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(6, capsule.max_packet_files)
    self.assertEqual(1500000, capsule.max_packet_utf8_bytes)
```

Change only the corresponding `APPENDIX_A_INVENTORY` tuple's enabled value from `False` to `True`.

- [ ] **Step 2: Run the focused test and verify it fails**

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_braintree_graphql_api_has_reviewed_commit_policy
```

Expected: FAIL because the row is disabled and has no capsule.

- [ ] **Step 3: Add the executable registry capsule**

Replace only the existing `braintree/graphql-api` row with:

```toml
[[repos]]
id="braintree/graphql-api"
collection_frequency="monthly"
company="braintree"
url="https://github.com/braintree/graphql-api"
enabled=true
repo_type="api-specification"
priority="tier1"
track="default-branch"
version_strategy="commit"
[[repos.capsules]]
id="braintree-graphql-api-schema"
adapter="commit-tree-v1"
source_id="braintree-graphql-api"
dependency_scope="configured-repository-paths"
changed_path_policy="policy-bounded"
default_required_roots=["schema.graphql"]
include_paths=["CHANGELOG.md", "README.md"]
excluded_categories=["tests", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=650000
max_capsule_files=3
max_capsule_utf8_bytes=800000
max_packet_files=6
max_packet_utf8_bytes=1500000
```

- [ ] **Step 4: Validate the policy and full GitHub suite**

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_braintree_graphql_api_has_reviewed_commit_policy
python3 -m unittest discover -s tests -p 'test_github_*.py'
python3 scripts/validate_github_collection.py
```

Expected: all tests pass and the validator reports no policy or existing-evidence regression.

- [ ] **Step 5: Commit the registry profile**

```bash
git add tests/test_github_registry.py tracking/github/repo-registry.toml
git diff --cached --check
git commit -m "feat: enable Braintree GraphQL API collection"
```

### Task 3: Preflight and publish the immutable baseline

**Files:**
- Generate: `raw/github/braintree/graphql-api/snapshots/<date>-<short-sha>/`
- Generate: `tracking/github/repos/braintree/graphql-api/`
- Modify through collector: `tracking/github/work-items.json`
- Modify through collector: `tracking/github/status.md`
- Modify through collector: `tracking/github/collection-index.json`
- Modify through collector: `tracking/github/collection-index.md`
- Must not modify: `wiki/`

**Interfaces:**
- Consumes: enabled registry capsule and `collect --repo braintree/graphql-api --mode backfill`.
- Produces: one exact-SHA snapshot, one review packet, and one `awaiting_approval` work item with recommended mode `full`.

- [ ] **Step 1: Run a non-publishing dry run**

```bash
python3 scripts/collect_github_repos.py collect \
  --repo braintree/graphql-api \
  --mode backfill \
  --dry-run | tee /private/tmp/braintree-graphql-api-dry-run.json
```

Expected: discovery resolves one default-branch SHA and reports no published snapshot or work item. Stop if the selected paths are not exactly `CHANGELOG.md`, `README.md`, and `schema.graphql`.

- [ ] **Step 2: Capture the publication boundary**

```bash
git status --porcelain=v1 > /private/tmp/braintree-graphql-api.before
```

Expected: the baseline records only committed task work plus unrelated `CLAUDE copy.md`.

- [ ] **Step 3: Run real baseline collection**

```bash
python3 scripts/collect_github_repos.py collect \
  --repo braintree/graphql-api \
  --mode backfill | tee /private/tmp/braintree-graphql-api-collection.json
```

Expected: one snapshot and one work item are published; the work item state is `awaiting_approval` and recommended mode is `full`.

- [ ] **Step 4: Verify immutable evidence and queue state**

```bash
python3 scripts/collect_github_repos.py status
python3 scripts/validate_github_collection.py
find raw/github/braintree/graphql-api -type f | sort
find tracking/github/repos/braintree/graphql-api -type f | sort
git status --short
```

Verify the snapshot manifest contains exactly three selected files, all hashes validate, the packet has zero evidence gaps and zero unclassified retained changes, and no path under `wiki/` changed.

- [ ] **Step 5: Commit only the generated collection evidence**

```bash
git add raw/github/braintree/graphql-api \
  tracking/github/repos/braintree/graphql-api \
  tracking/github/work-items.json \
  tracking/github/status.md \
  tracking/github/collection-index.json \
  tracking/github/collection-index.md
git diff --cached --check
git commit -m "data: collect Braintree GraphQL API baseline"
```

- [ ] **Step 6: Stop at the approval gate**

Report the exact SHA, selected byte count, latest changelog date, packet findings, and work-item ID. Do not approve or ingest until the user has reviewed the packet and explicitly selected `full`.

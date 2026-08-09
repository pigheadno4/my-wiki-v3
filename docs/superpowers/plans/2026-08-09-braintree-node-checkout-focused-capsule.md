# Braintree Node Checkout-Focused Capsule Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable `braintree/braintree_node`, verify a complete runtime capsule for `braintree@3.39.0`, and stop after publishing an approval-gated baseline packet.

**Architecture:** Reuse the root-package `npm-tracked-source-v1` adapter with the complete `lib/` runtime so public exports and internal runtime dependencies stay source-complete. Collection and ingest remain separate: configuration is committed first, dry-run publishes nothing, and real collection requires an explicit user gate before it may create immutable evidence in `awaiting_approval`.

**Tech Stack:** Python 3 `unittest`, TOML registry configuration, existing GitHub collection CLI, Git, JSON/JQ, immutable Markdown/JSON evidence.

## Global Constraints

- Initial package identity is `braintree@3.39.0`.
- Official tag `3.39.0` must resolve to exact commit `7a9270aaf31eb87819add64a768652243f90007c` at collection time.
- Future stable v3 releases are retained; prereleases are excluded.
- The complete `lib/` runtime is retained; `test/`, fixtures, lockfiles, CI, build, lint, formatting, editor, Docker, and release tooling are excluded.
- Runtime `lib/braintree/test_values/` exports remain included as sandbox API evidence.
- Deep future ingest covers gateway configuration, client tokens, transactions, payment methods, customers/vault, cards, PayPal, Venmo, subscriptions, refunds, 3D Secure, validation, and checkout-relevant webhooks.
- Disputes, merchant onboarding, OAuth partner operations, document upload, settlement reporting, and unrelated administration APIs remain inventory-only.
- Snapshot limits are 220 files and 1,500,000 UTF-8 bytes; packet limits are 260 files and 2,000,000 UTF-8 bytes; per-file limit is 512,000 bytes.
- Collection must stop at `awaiting_approval`; do not approve, start ingest, or edit `wiki/`.
- Leave unrelated `CLAUDE copy.md` untouched.

---

### Task 1: Enable the reviewed Braintree Node registry profile

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`

**Interfaces:**
- Consumes: existing `load_registry()`, `VersionTrack`, `CapsuleConfig`, and `npm-tracked-source-v1` registry schema.
- Produces: executable `braintree/braintree_node` policy with one package-qualified v3 track and one root-package runtime capsule.

- [ ] **Step 1: Add the failing registry contract test**

Update the `braintree/braintree_node` row in `APPENDIX_A_INVENTORY` from `False` to `True`, then add this method to `RegistryTests` near the other Braintree profile tests:

```python
def test_braintree_node_uses_complete_runtime_checkout_profile(self):
    repos = {
        repo.id: repo
        for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
    }
    repo = repos["braintree/braintree_node"]

    self.assertTrue(repo.enabled)
    self.assertEqual(
        (
            VersionTrack(
                "package:braintree@3",
                "latest-stable",
                "all-stable",
                False,
                ("3.39.0",),
            ),
        ),
        repo.version_tracks,
    )
    self.assertEqual(1, len(repo.capsules))
    capsule = repo.capsules[0]
    self.assertEqual("braintree-node-checkout-source", capsule.id)
    self.assertEqual("npm-tracked-source-v1", capsule.adapter)
    self.assertEqual(("braintree",), capsule.focus_packages)
    self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(("lib",), capsule.default_required_roots)
    self.assertEqual((), capsule.default_generated_target_paths)
    self.assertEqual(
        ("CHANGELOG.md", "LICENSE", "README.md", "SECURITY.md", "index.js"),
        capsule.include_paths,
    )
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual("text-secrets-v1", capsule.secret_detector)
    self.assertEqual(512000, capsule.max_file_bytes)
    self.assertEqual(220, capsule.max_capsule_files)
    self.assertEqual(1500000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(260, capsule.max_packet_files)
    self.assertEqual(2000000, capsule.max_packet_utf8_bytes)
```

- [ ] **Step 2: Run the focused test and verify it fails**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_braintree_node_uses_complete_runtime_checkout_profile
```

Expected: FAIL because the registry entry is disabled and defines no version track or capsule.

- [ ] **Step 3: Replace the disabled inventory row with the executable policy**

Replace only the `braintree/braintree_node` row in `tracking/github/repo-registry.toml` with:

```toml
[[repos]]
id="braintree/braintree_node"
collection_frequency="monthly"
company="braintree"
url="https://github.com/braintree/braintree_node"
enabled=true
repo_type="server-sdk"
priority="tier2"
track="releases-and-default-branch"
version_strategy="semver-tags"
[[repos.version_tracks]]
selector="package:braintree@3"
backfill="latest-stable"
future="all-stable"
include_prerelease=false
pinned_versions=["3.39.0"]
[[repos.capsules]]
id="braintree-node-checkout-source"
adapter="npm-tracked-source-v1"
focus_packages=["braintree"]
dependency_scope="internal-runtime-closure"
changed_path_policy="policy-bounded"
default_required_roots=["lib"]
default_generated_target_paths=[]
include_paths=["CHANGELOG.md", "LICENSE", "README.md", "SECURITY.md", "index.js"]
excluded_categories=["tests", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=512000
max_capsule_files=220
max_capsule_utf8_bytes=1500000
max_packet_files=260
max_packet_utf8_bytes=2000000
```

- [ ] **Step 4: Run focused and registry regression tests**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_braintree_node_uses_complete_runtime_checkout_profile
python3 -m unittest tests.test_github_registry tests.test_github_capsule_policy tests.test_github_capsule_selection
python3 scripts/validate_github_collection.py
```

Expected: all tests pass and collection validation reports no structural errors.

- [ ] **Step 5: Review and commit only the registry policy**

Run:

```bash
git diff --check
git diff -- tests/test_github_registry.py tracking/github/repo-registry.toml
git status --short
git add tests/test_github_registry.py tracking/github/repo-registry.toml
git commit -m "feat: enable Braintree Node collection"
```

Expected: the commit contains only the registry contract test and executable Braintree Node policy. `CLAUDE copy.md` remains untracked.

### Task 2: Verify the baseline with a non-publishing dry run

**Files:**
- Read: `tracking/github/repo-registry.toml`
- Read: dry-run output only; no raw, tracking, or wiki file may be created or modified.

**Interfaces:**
- Consumes: executable policy committed by Task 1, `collect --mode backfill --dry-run`, and the capsule resolver against the exact tag in temporary storage.
- Produces: verified release identity and capsule measurements for the real-collection approval decision. The generic release dry-run verifies discovery and tag identity only; it does not execute capsule selection.

- [ ] **Step 1: Record the pre-run repository state**

Run:

```bash
git status --short
git rev-parse HEAD
```

Expected: only unrelated `CLAUDE copy.md` is untracked; no GitHub collection artifact is pending.

- [ ] **Step 2: Run the dry collection**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo braintree/braintree_node --mode backfill --dry-run
```

Expected: selection resolves only `braintree@3.39.0`, tag `3.39.0`, and exact commit `7a9270aaf31eb87819add64a768652243f90007c`. No repository evidence is published.

- [ ] **Step 3: Resolve and measure the capsule in temporary storage**

Run the configured capsule resolver against the exact tag clone outside the repository.

Expected: the capsule contains the root package evidence plus the complete `lib/` runtime, remains within all budgets, and reports no secret or identity failure.

- [ ] **Step 4: Prove the dry run published nothing**

Run:

```bash
git status --short
find raw/github/braintree/braintree_node -type f
jq '[.work_items[] | select(.repo_id == "braintree/braintree_node")] | length' tracking/github/work-items.json
```

Expected: no Braintree Node raw directory exists, the work-item count is `0`, and repository state matches Step 1.

- [ ] **Step 5: Report measurements and request the real-collection gate**

Report the resolved package, tag, SHA, selected file count, selected UTF-8 bytes, exclusions, and any warnings. Do not run real collection until the user explicitly approves it after seeing this report.

### Task 3: Publish the immutable baseline after explicit approval

**Files:**
- Create under: `raw/github/braintree/braintree_node/snapshots/`
- Create under: `raw/github/braintree/braintree_node/releases/braintree/3.39.0/`
- Create under: `tracking/github/repos/braintree/braintree_node/ingest-packets/`
- Modify generated: `tracking/github/work-items.json`
- Modify generated: `tracking/github/status.md`
- Modify generated: `tracking/github/collection-index.json`
- Modify generated: `tracking/github/collection-index.md`

**Interfaces:**
- Consumes: approved dry-run measurements and the committed registry policy.
- Produces: one exact-SHA snapshot, one package-qualified release record, one full-review packet, and one work item in `awaiting_approval`.

- [ ] **Step 1: Confirm the separate real-collection approval**

Proceed only when the user has explicitly approved real collection after Task 2. Otherwise stop with no file changes.

- [ ] **Step 2: Run the real collection**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo braintree/braintree_node --mode backfill
```

Expected: immutable evidence is published once and the new work item stops at `awaiting_approval`. Any tag mismatch, missing required path, secret finding, unsafe path, or budget failure stops without partial publication.

- [ ] **Step 3: Validate generated evidence and lifecycle state**

Run:

```bash
python3 scripts/validate_github_collection.py
python3 -m unittest tests.test_github_registry tests.test_github_capsule_policy tests.test_github_capsule_selection tests.test_github_releases tests.test_collect_github_repos tests.test_github_ingest_packets tests.test_github_work_items
jq '.work_items[] | select(.repo_id == "braintree/braintree_node") | {work_item_id,state,recommended_mode,approved_mode,sha,package_changes}' tracking/github/work-items.json
```

Expected: validation and tests pass; exactly one Braintree Node work item exists at the resolved SHA, recommends `full`, has no approved mode, and is `awaiting_approval`.

- [ ] **Step 4: Review the packet without starting ingest**

Read the generated `packet.json` and `packet.md` in full. Report required-reading count, selected evidence measurements, unclassified changes, evidence gaps, and the exact next approval command. Do not run `approve`, `next-ingest`, or edit any wiki page.

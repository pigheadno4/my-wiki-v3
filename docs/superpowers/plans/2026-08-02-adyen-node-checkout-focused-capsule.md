# Adyen Node Checkout-Focused Capsule Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable and collect a bounded `@adyen/api-library@32.0.0` capsule with deep Checkout evidence and inventory-level coverage for all other Adyen Node API services, stopping at packet review.

**Architecture:** Reuse `tagged-tree-v1` so exact configured paths, rather than recursive npm dependency closure, define the immutable snapshot. The registry retains all service implementations plus Checkout, Payment, Recurring, and standard notification model trees; detailed excluded-domain and broader webhook evidence remains available through exact-SHA supplements.

**Tech Stack:** Python 3 `unittest`, TOML registry configuration, existing GitHub collection CLI, Git, JSON/JQ, immutable Markdown/JSON evidence.

## Global Constraints

- Initial package identity is `@adyen/api-library@32.0.0`.
- Official tag `v32.0.0` must resolve to exact SHA `99d1a0cf69c8660952baffd1437b00aae2fa4f23`.
- Future stable v32 releases are retained; prereleases are excluded.
- Deep coverage includes Checkout, Payment, Recurring, client, HTTP, security, and standard payment notifications only: `src/notification/` plus `src/typings/notification/`.
- `src/webhooks.ts` and `src/typings/index.ts` are inventory-only barrels; the eleven broader `src/typings/*Webhooks/` families require exact-SHA supplements for detailed claims.
- Inventory coverage retains every `src/services/` implementation without every non-checkout generated model tree.
- Snapshot limits are 620 files and 3,500,000 UTF-8 bytes; packet limits are 700 files and 5,000,000 UTF-8 bytes; per-file limit is 512,000 bytes.
- Tests, mocks, fixtures, lockfiles, build output, and `sdk-generation-log/` are excluded.
- Changed release evidence is policy-bounded.
- Collection must stop at `awaiting_approval`; do not approve, start ingest, or edit `wiki/`.
- Leave unrelated Metronome campaign files and `CLAUDE copy.md` untouched.

---

### Task 1: Enable the bounded Adyen Node registry profile

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`

**Interfaces:**
- Consumes: existing `load_registry()`, `VersionTrack`, `CapsuleConfig`, and `tagged-tree-v1` registry schema.
- Produces: executable repository `adyen/adyen-node-api-library` with one package-qualified v32 track and one configured-path capsule.

- [ ] **Step 1: Add the failing registry contract test**

Add this method to `RegistryTests` near the other Adyen profile tests:

```python
def test_adyen_node_uses_checkout_deep_and_domain_inventory_profile(self):
    repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
    adyen_node = next(
        repo for repo in repos if repo.id == "adyen/adyen-node-api-library"
    )

    self.assertTrue(adyen_node.enabled)
    self.assertEqual(
        (
            VersionTrack(
                "package:@adyen/api-library@32",
                "latest-stable",
                "all-stable",
                False,
                ("32.0.0",),
            ),
        ),
        adyen_node.version_tracks,
    )
    self.assertEqual(1, len(adyen_node.capsules))
    capsule = adyen_node.capsules[0]
    self.assertEqual("adyen-node-checkout-source", capsule.id)
    self.assertEqual("tagged-tree-v1", capsule.adapter)
    self.assertEqual(("@adyen/api-library",), capsule.focus_packages)
    self.assertEqual("configured-repository-paths", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(
        (
            "doc",
            "src/constants",
            "src/helpers",
            "src/httpClient",
            "src/notification",
            "src/security",
            "src/services",
            "src/typings/checkout",
            "src/typings/notification",
            "src/typings/payment",
            "src/typings/recurring",
            "src/utils",
        ),
        capsule.default_required_roots,
    )
    self.assertEqual(
        (
            "LICENSE",
            "README.md",
            "VERSION",
            "package.json",
            "src/client.ts",
            "src/config.ts",
            "src/index.ts",
            "src/service.ts",
            "src/typings/index.ts",
            "src/webhooks.ts",
            "tsconfig.json",
        ),
        capsule.include_paths,
    )
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual(
        ("35829dc91506c9d75f2227a2d1fee3e2ede206ea84184245748a9d179bd2e197",),
        capsule.historical_policy_hashes,
    )
    self.assertEqual(512000, capsule.max_file_bytes)
    self.assertEqual(620, capsule.max_capsule_files)
    self.assertEqual(3500000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(700, capsule.max_packet_files)
    self.assertEqual(5000000, capsule.max_packet_utf8_bytes)
```

- [ ] **Step 2: Run the focused test and verify it fails**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_adyen_node_uses_checkout_deep_and_domain_inventory_profile
```

Expected: FAIL because the existing inventory row is disabled and has no version track or capsule.

- [ ] **Step 3: Replace the disabled inventory row with the executable policy**

Replace only the `adyen/adyen-node-api-library` row in
`tracking/github/repo-registry.toml` with:

```toml
[[repos]]
id="adyen/adyen-node-api-library"
collection_frequency="monthly"
company="adyen"
url="https://github.com/Adyen/adyen-node-api-library"
enabled=true
repo_type="server-sdk"
priority="tier2"
track="releases-and-default-branch"
version_strategy="semver-tags"
[[repos.version_tracks]]
selector="package:@adyen/api-library@32"
backfill="latest-stable"
future="all-stable"
include_prerelease=false
pinned_versions=["32.0.0"]
[[repos.capsules]]
id="adyen-node-checkout-source"
adapter="tagged-tree-v1"
focus_packages=["@adyen/api-library"]
dependency_scope="configured-repository-paths"
changed_path_policy="policy-bounded"
default_required_roots=[
  "doc",
  "src/constants",
  "src/helpers",
  "src/httpClient",
  "src/notification",
  "src/security",
  "src/services",
  "src/typings/checkout",
  "src/typings/notification",
  "src/typings/payment",
  "src/typings/recurring",
  "src/utils",
]
default_generated_target_paths=[]
include_paths=[
  "LICENSE",
  "README.md",
  "VERSION",
  "package.json",
  "src/client.ts",
  "src/config.ts",
  "src/index.ts",
  "src/service.ts",
  "src/typings/index.ts",
  "src/webhooks.ts",
  "tsconfig.json",
]
excluded_categories=["tests", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=512000
max_capsule_files=620
max_capsule_utf8_bytes=3500000
max_packet_files=700
max_packet_utf8_bytes=5000000
historical_policy_hashes=["35829dc91506c9d75f2227a2d1fee3e2ede206ea84184245748a9d179bd2e197"]
```

- [ ] **Step 4: Run focused and registry regression tests**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_adyen_node_uses_checkout_deep_and_domain_inventory_profile
python3 -m unittest tests.test_github_registry tests.test_github_capsule_policy tests.test_github_tagged_tree
python3 scripts/validate_github_collection.py
```

Expected: all tests pass and the validator reports no structural errors.

- [ ] **Step 5: Verify the diff contains no unrelated files**

Run:

```bash
git diff --check
git status --short
git diff -- tests/test_github_registry.py tracking/github/repo-registry.toml
```

Expected: only the Adyen Node test and registry row are part of this task; existing Metronome and duplicate-file changes remain unstaged.

- [ ] **Step 6: Commit the executable registry profile**

```bash
git add tests/test_github_registry.py tracking/github/repo-registry.toml
git commit -m "feat: enable Adyen Node checkout collection"
```

### Task 2: Collect and review `@adyen/api-library@32.0.0`

**Files:**
- Create under: `raw/github/adyen/adyen-node-api-library/snapshots/` using the collector-assigned dated SHA directory
- Create under: `raw/github/adyen/adyen-node-api-library/releases/api-library/32.0.0/` using the collector-assigned collection date
- Create under: `tracking/github/repos/adyen/adyen-node-api-library/ingest-packets/` using the collector-assigned work-item ID
- Modify: `tracking/github/work-items.json`
- Modify: `tracking/github/status.md`

**Interfaces:**
- Consumes: the executable registry profile from Task 1 and the existing `collect --mode backfill` command.
- Produces: one immutable exact-SHA snapshot, one package-qualified release record, one review packet, and one work item in `awaiting_approval`.

- [ ] **Step 1: Run the dry collection**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo adyen/adyen-node-api-library --mode backfill --dry-run
```

Expected: selection resolves only `@adyen/api-library@32.0.0`, tag `v32.0.0`, and SHA `99d1a0cf69c8660952baffd1437b00aae2fa4f23`; no raw or tracking state is published.

- [ ] **Step 2: Run collection**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo adyen/adyen-node-api-library --mode backfill
```

Expected: collection publishes complete immutable evidence and stops with one new work item in `awaiting_approval`. Any mismatch, missing required path, secret finding, or budget failure must stop without partial publication.

- [ ] **Step 3: Validate generated evidence offline**

Run:

```bash
python3 scripts/validate_github_collection.py
python3 -m unittest tests.test_github_registry tests.test_github_capsule_policy tests.test_github_tagged_tree tests.test_github_releases tests.test_collect_github_repos tests.test_github_ingest_packets tests.test_github_work_items
```

Expected: the validator and all focused regressions pass.

- [ ] **Step 4: Verify the immutable snapshot boundary**

Locate the generated snapshot manifest under
`raw/github/adyen/adyen-node-api-library/snapshots/`, then run:

```bash
jq '{repository,sha,collected_date,file_count:(.files|length),excluded_count:(.excluded|length)}' raw/github/adyen/adyen-node-api-library/snapshots/*/manifest.json
jq '[.files[].size] | add' raw/github/adyen/adyen-node-api-library/snapshots/*/manifest.json
find raw/github/adyen/adyen-node-api-library/snapshots -path '*/files/*' -type f | wc -l
find raw/github/adyen/adyen-node-api-library/snapshots -path '*/files/src/services/*' -type f | wc -l
find raw/github/adyen/adyen-node-api-library/snapshots -path '*/files/src/typings/checkout/*' -type f | wc -l
find raw/github/adyen/adyen-node-api-library/snapshots -path '*/files/src/typings/balancePlatform/*' -type f | wc -l
find raw/github/adyen/adyen-node-api-library/snapshots \( -path '*/__tests__/*' -o -path '*/__mocks__/*' -o -name '*.test.ts' -o -name '*.spec.ts' \) -type f | wc -l
find raw/github/adyen/adyen-node-api-library/supplements -path '*/files/src/typings/notification/*' -type f | wc -l
jq '[.files[].size] | add' raw/github/adyen/adyen-node-api-library/supplements/*/manifest.json
jq -e '(.files | length == 5) and ([.files[].path] | sort == ["src/typings/notification/amount.ts", "src/typings/notification/models.ts", "src/typings/notification/notification.ts", "src/typings/notification/notificationItem.ts", "src/typings/notification/notificationRequestItem.ts"])' raw/github/adyen/adyen-node-api-library/supplements/*/manifest.json
```

Expected: SHA matches `99d1a0cf69c8660952baffd1437b00aae2fa4f23`;
the immutable base snapshot remains 545 files and 2,357,166 bytes; the exact-SHA
`src/typings/notification/` supplement contains exactly five files and 21,450
bytes; and the reviewed base-plus-supplement boundary is 550 files and
2,378,616 bytes, under the 620-file and 3,500,000-byte limits. Service and
Checkout trees are present; the standard notification handler and five-file
model tree are self-contained; `src/webhooks.ts` and `src/typings/index.ts`
remain inventory-only; no broader `*Webhooks/` tree is collected; and both the
Balance Platform model-tree count and excluded test/mock count are zero.

- [ ] **Step 5: Review the canonical packet and lifecycle state**

Run:

```bash
python3 scripts/collect_github_repos.py status
jq '{work_item_id,repository,to_sha,recommendation,required_reading_count:(.required_reading|length),unclassified_count:(.unclassified_changes|length),evidence_gap_count:(.evidence_gaps|length)}' tracking/github/repos/adyen/adyen-node-api-library/ingest-packets/*/packet.json
jq '.work_items[] | select(.repo_id == "adyen/adyen-node-api-library") | {work_item_id,repo_id,state,recommended_mode,approved_mode,sha}' tracking/github/work-items.json
```

Read both generated `packet.json` and `packet.md` in full. Expected: exact package and SHA identity, deterministic full-baseline recommendation, no unclassified retained changes, no blocking Checkout evidence gap, and state `awaiting_approval` with no approved mode.

- [ ] **Step 6: Verify no wiki ingest occurred**

Run:

```bash
git status --short
git diff --name-only -- wiki
```

Expected: no `wiki/` file changed. Existing unrelated workspace changes remain untouched.

- [ ] **Step 7: Commit only collected Adyen Node evidence**

```bash
git add raw/github/adyen/adyen-node-api-library tracking/github/repos/adyen/adyen-node-api-library tracking/github/work-items.json tracking/github/status.md
git diff --cached --check
git commit -m "data: collect Adyen Node API Library 32.0.0"
```

- [ ] **Step 8: Report packet findings and stop**

Report package identity, release date, exact SHA, retained file and byte counts,
deep and inventory coverage, the standard notification supplement, excluded
broader webhook families, required-reading count,
unclassified and evidence-gap counts, recommendation, work-item ID, validation
results, and commit hash. Explicitly state that ingest has not started.

The next action requires a separate user decision: approve the generated work
item in full mode, request a supplement or policy correction, or leave it in
`awaiting_approval`.

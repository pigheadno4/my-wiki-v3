# PayPal TypeScript Server SDK Capsule Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable version-qualified collection for `@paypal/paypal-server-sdk`, prove complete source capsules for canonical releases `2.3.0` and `2.4.0`, and publish two immutable work items that stop at packet review.

**Architecture:** Reuse the existing release collector and `npm-tracked-source-v1` adapter with one root-package v2 track. The capsule retains complete `src/` implementation and `doc/controllers/` references while excluding duplicate generated model docs, tests, fixtures, and build output. Temporary exact-tag resolution precedes publication; real collection creates separate exact-SHA histories for `2.3.0` and `2.4.0` without replacing the legacy partial review.

**Tech Stack:** Python 3 `unittest`, TOML registry configuration, existing GitHub collection CLI, Git, JSON/JQ, immutable Markdown/JSON evidence.

## Global Constraints

- The package identity is always package-qualified as `@paypal/paypal-server-sdk@<version>`.
- Initial canonical releases are `2.3.0` at SHA `b37cec58f2cdeecf5b9b7a7c15131cc5f4fff712` and `2.4.0` at SHA `dbdbdd06f18a06d633c66bbc27d7d7a54283e1a3`; execution must re-resolve both tags.
- The legacy 16-file review at SHA `ff27fa8e18cccad1daf180fe98d3cf0ed5ed3c5b` remains a separate partial evidence identity and must not be rewritten as canonical `2.3.0`.
- Backfill selects pinned `2.3.0` and `2.4.0`; future collection retains every stable v2 release newer than the highest accepted v2 release; prereleases are excluded.
- A future major version requires a separately reviewed track and full-ingest decision.
- Retain complete `src/`, complete `doc/controllers/`, `README.md`, `CHANGELOG.md`, `LICENSE`, and the package manifest automatically resolved by the NPM adapter.
- Exclude tests, fixtures, generated `doc/models/`, generated `dist/`, build and release tooling, lockfiles, dependencies, Git metadata, and local environment files.
- Per-file limit is 512,000 bytes; capsule limits are 430 files and 3,000,000 UTF-8 bytes; packet limits are 500 files and 4,000,000 UTF-8 bytes.
- Missing required paths, package/tag mismatch, unsafe paths, strict UTF-8 failure, secret findings, or budget overflow stop for manual review; never truncate or silently increase limits.
- Real collection may fetch both releases in one command but must publish separate snapshots, release records, comparisons, packets, and work items.
- Collection stops at `awaiting_approval`; do not approve an ingest mode, call `next-ingest`, edit `wiki/`, or alter legacy raw evidence.
- Leave unrelated workspace files, including `CLAUDE copy.md`, untouched.

---

### Task 1: Enable and test the PayPal TypeScript SDK registry profile

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`

**Interfaces:**
- Consumes: `load_registry(path: Path) -> tuple[RepoConfig, ...]`, `VersionTrack`, `CapsuleConfig`, and the existing disabled inventory row.
- Produces: one enabled `paypal/paypal-typescript-server-sdk` policy using `package:@paypal/paypal-server-sdk@2` and `paypal-typescript-server-sdk-source`.

- [ ] **Step 1: Add the failing registry contract test**

Add this method to `RegistryTests` near the other PayPal repository profile tests:

```python
def test_paypal_typescript_server_sdk_uses_complete_source_profile(self):
    repos = {
        repo.id: repo
        for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
    }
    repo = repos["paypal/paypal-typescript-server-sdk"]

    self.assertTrue(repo.enabled)
    self.assertEqual("server-sdk", repo.repo_type)
    self.assertEqual("tier2", repo.priority)
    self.assertEqual("monthly", repo.collection_frequency)
    self.assertEqual("releases-and-default-branch", repo.track)
    self.assertEqual("semver-tags", repo.version_strategy)
    self.assertEqual(
        (
            VersionTrack(
                "package:@paypal/paypal-server-sdk@2",
                "latest-stable",
                "all-stable",
                False,
                ("2.3.0", "2.4.0"),
            ),
        ),
        repo.version_tracks,
    )
    self.assertEqual(1, len(repo.capsules))
    capsule = repo.capsules[0]
    self.assertEqual("paypal-typescript-server-sdk-source", capsule.id)
    self.assertEqual("npm-tracked-source-v1", capsule.adapter)
    self.assertEqual(("@paypal/paypal-server-sdk",), capsule.focus_packages)
    self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(("doc/controllers", "src"), capsule.default_required_roots)
    self.assertEqual(("dist/",), capsule.default_generated_target_paths)
    self.assertEqual(
        ("CHANGELOG.md", "LICENSE", "README.md"),
        capsule.include_paths,
    )
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual("text-secrets-v1", capsule.secret_detector)
    self.assertEqual(512000, capsule.max_file_bytes)
    self.assertEqual(430, capsule.max_capsule_files)
    self.assertEqual(3000000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(500, capsule.max_packet_files)
    self.assertEqual(4000000, capsule.max_packet_utf8_bytes)
```

Also change only the corresponding `APPENDIX_A_INVENTORY` tuple's enabled value from `False` to `True`.

- [ ] **Step 2: Run the focused test and verify it fails**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_paypal_typescript_server_sdk_uses_complete_source_profile
```

Expected: FAIL because the inventory row is disabled and has no version track or capsule.

- [ ] **Step 3: Replace the disabled inventory row with the executable policy**

Replace only the `paypal/paypal-typescript-server-sdk` row in `tracking/github/repo-registry.toml` with:

```toml
[[repos]]
id="paypal/paypal-typescript-server-sdk"
collection_frequency="monthly"
company="paypal"
url="https://github.com/paypal/PayPal-TypeScript-Server-SDK"
enabled=true
repo_type="server-sdk"
priority="tier2"
track="releases-and-default-branch"
version_strategy="semver-tags"
[[repos.version_tracks]]
selector="package:@paypal/paypal-server-sdk@2"
backfill="latest-stable"
future="all-stable"
include_prerelease=false
pinned_versions=["2.3.0", "2.4.0"]
[[repos.capsules]]
id="paypal-typescript-server-sdk-source"
adapter="npm-tracked-source-v1"
focus_packages=["@paypal/paypal-server-sdk"]
dependency_scope="internal-runtime-closure"
changed_path_policy="policy-bounded"
default_required_roots=["src", "doc/controllers"]
default_generated_target_paths=["dist/"]
include_paths=["CHANGELOG.md", "LICENSE", "README.md"]
excluded_categories=["tests", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=512000
max_capsule_files=430
max_capsule_utf8_bytes=3000000
max_packet_files=500
max_packet_utf8_bytes=4000000
```

- [ ] **Step 4: Run focused and registry regression tests**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_paypal_typescript_server_sdk_uses_complete_source_profile
python3 -m unittest tests.test_github_registry tests.test_github_capsule_policy tests.test_github_capsule_selection tests.test_github_releases
python3 scripts/validate_github_collection.py
```

Expected: all tests pass and the validator reports no structural or policy errors.

- [ ] **Step 5: Verify the diff contains only the approved policy change**

Run:

```bash
git diff --check
git status --short
git diff -- tests/test_github_registry.py tracking/github/repo-registry.toml
```

Expected: this task changes only the focused registry test and TypeScript SDK registry row. `CLAUDE copy.md` and other unrelated files remain unstaged.

- [ ] **Step 6: Commit the executable registry profile**

```bash
git add tests/test_github_registry.py tracking/github/repo-registry.toml
git diff --cached --check
git commit -m "feat: enable PayPal TypeScript SDK collection"
```

### Task 2: Prove both exact-tag capsules without publishing evidence

**Files:**
- Read: `tracking/github/repo-registry.toml`
- Read temporarily: official Git objects for tags `2.3.0` and `2.4.0`
- Must not modify: `raw/`, `tracking/github/work-items.json`, `tracking/github/status.md`, or `wiki/`

**Interfaces:**
- Consumes: the enabled registry profile from Task 1, `collect --mode backfill --dry-run`, `GitTree`, and `resolve_capsule`.
- Produces: a reviewed preflight report containing exact tag SHAs, package versions, selected counts and bytes, secret results, and the retained `2.3.0` to `2.4.0` change count.

- [ ] **Step 1: Capture the preflight workspace state**

Run:

```bash
git status --porcelain=v1 > /private/tmp/paypal-typescript-sdk-preflight.before
```

Expected: the file records the current workspace state, including unrelated pre-existing files.

- [ ] **Step 2: Run dry backfill discovery**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo paypal/paypal-typescript-server-sdk --mode backfill --dry-run | tee /private/tmp/paypal-typescript-sdk-dry-run.json
jq -e '.state == "discovered" and (.release_ids | sort) == ["@paypal/paypal-server-sdk@2.3.0", "@paypal/paypal-server-sdk@2.4.0"] and (.snapshot_paths | length == 0) and (.work_item_ids | length == 0)' /private/tmp/paypal-typescript-sdk-dry-run.json
```

Expected: the dry run selects exactly the two package-qualified pinned releases and publishes no snapshot or work item.

- [ ] **Step 3: Clone the repository into temporary storage and fetch exact tags**

Run:

```bash
export PAYPAL_TS_SDK_PREFLIGHT="$(mktemp -d /private/tmp/paypal-typescript-sdk.XXXXXX)"
git clone --filter=blob:none --no-checkout https://github.com/paypal/PayPal-TypeScript-Server-SDK "$PAYPAL_TS_SDK_PREFLIGHT"
git -C "$PAYPAL_TS_SDK_PREFLIGHT" fetch --depth=1 origin refs/tags/2.3.0:refs/tags/2.3.0 refs/tags/2.4.0:refs/tags/2.4.0
git -C "$PAYPAL_TS_SDK_PREFLIGHT" rev-parse '2.3.0^{commit}' '2.4.0^{commit}'
```

Expected: the two resolved SHAs are, in order, `b37cec58f2cdeecf5b9b7a7c15131cc5f4fff712` and `dbdbdd06f18a06d633c66bbc27d7d7a54283e1a3`. Stop if either identity differs.

- [ ] **Step 4: Resolve and verify both complete source capsules**

Run in the same shell so `PAYPAL_TS_SDK_PREFLIGHT` remains available:

```bash
PYTHONPATH=scripts python3 - <<'PY'
import json
import os
from pathlib import Path
import subprocess

from github_capsule_selection import resolve_capsule
from github_git_tree import GitTree
from github_registry import load_registry

root = Path.cwd()
repo_root = Path(os.environ["PAYPAL_TS_SDK_PREFLIGHT"])
config = next(
    repo
    for repo in load_registry(root / "tracking/github/repo-registry.toml")
    if repo.id == "paypal/paypal-typescript-server-sdk"
)
capsule = config.capsules[0]
expected = {
    "2.3.0": "b37cec58f2cdeecf5b9b7a7c15131cc5f4fff712",
    "2.4.0": "dbdbdd06f18a06d633c66bbc27d7d7a54283e1a3",
}
resolved = {}
for version, sha in expected.items():
    tree = GitTree(repo_root, sha, capsule.max_file_bytes)
    result = resolve_capsule(tree, capsule, config.secret_allowlist)
    packages = [(package.name, package.version) for package in result.workspace.packages]
    assert packages == [("@paypal/paypal-server-sdk", version)], packages
    paths = {item.path for item in result.files}
    assert {"package.json", "README.md", "CHANGELOG.md", "LICENSE"} <= paths
    assert any(path.startswith("src/") for path in paths)
    assert any(path.startswith("doc/controllers/") for path in paths)
    assert not any(path.startswith("doc/models/") for path in paths)
    assert not any(path.startswith("dist/") for path in paths)
    assert not result.secret_findings
    assert len(result.files) <= capsule.max_capsule_files
    assert sum(item.size for item in result.files) <= capsule.max_capsule_utf8_bytes
    resolved[version] = {
        "sha": sha,
        "file_count": len(result.files),
        "utf8_bytes": sum(item.size for item in result.files),
        "paths": paths,
    }

changed = set(subprocess.run(
    [
        "git",
        "-C",
        str(repo_root),
        "diff",
        "--name-only",
        expected["2.3.0"],
        expected["2.4.0"],
    ],
    check=True,
    capture_output=True,
    text=True,
).stdout.splitlines())
retained_changed = changed & (resolved["2.3.0"]["paths"] | resolved["2.4.0"]["paths"])
assert len(changed) == 155, len(changed)
assert len(retained_changed) == 58, len(retained_changed)
print(json.dumps({
    version: {
        "sha": values["sha"],
        "file_count": values["file_count"],
        "utf8_bytes": values["utf8_bytes"],
    }
    for version, values in resolved.items()
}, sort_keys=True, indent=2))
print(json.dumps({
    "repository_changed_paths": len(changed),
    "retained_changed_paths": len(retained_changed),
}, sort_keys=True))
PY
```

Expected: both package manifests match their tags, all approved roots are present, excluded trees are absent, counts stay below policy budgets, no secret finding is reported, and the exact comparison contains 155 repository changes with 58 retained changes.

- [ ] **Step 5: Prove preflight did not publish repository evidence**

Run:

```bash
git status --porcelain=v1 > /private/tmp/paypal-typescript-sdk-preflight.after
cmp /private/tmp/paypal-typescript-sdk-preflight.before /private/tmp/paypal-typescript-sdk-preflight.after
git diff --name-only -- raw tracking/github/work-items.json tracking/github/status.md wiki
```

Expected: `cmp` succeeds and no new raw, queue, status, or wiki path was produced by preflight.

- [ ] **Step 6: Report preflight findings and request explicit collection approval**

Report the re-resolved SHAs, exact per-release file and byte counts, no-secret result, and 155/58 comparison counts. Stop here until the user explicitly approves real collection.

### Task 3: Publish two immutable canonical release work items

**Files:**
- Create under: `raw/github/paypal/paypal-typescript-server-sdk/snapshots/`
- Create under: `raw/github/paypal/paypal-typescript-server-sdk/releases/paypal-server-sdk/2.3.0/`
- Create under: `raw/github/paypal/paypal-typescript-server-sdk/releases/paypal-server-sdk/2.4.0/`
- Create under: `tracking/github/repos/paypal/paypal-typescript-server-sdk/comparisons/paypal-server-sdk/`
- Create under: `tracking/github/repos/paypal/paypal-typescript-server-sdk/ingest-packets/`
- Modify: `tracking/github/work-items.json`
- Modify: `tracking/github/status.md`
- Modify: `tracking/github/collection-index.md`

**Interfaces:**
- Consumes: the approved Task 2 preflight and `collect --mode backfill`.
- Produces: two exact-SHA snapshots, two release records, the canonical `2.3.0` to `2.4.0` comparison, two packets, and two work items in `awaiting_approval`.

- [ ] **Step 1: Capture wiki state before collection**

Run:

```bash
git status --porcelain=v1 -- wiki > /private/tmp/paypal-typescript-sdk-wiki.before
```

Expected: the command records any pre-existing wiki state without changing it.

- [ ] **Step 2: Run real backfill collection after explicit approval**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo paypal/paypal-typescript-server-sdk --mode backfill | tee /private/tmp/paypal-typescript-sdk-collection.json
jq -e '.state == "awaiting_approval" and (.release_ids | sort) == ["@paypal/paypal-server-sdk@2.3.0", "@paypal/paypal-server-sdk@2.4.0"] and (.snapshot_paths | length == 2) and (.work_item_ids | length == 2) and (.errors | length == 0)' /private/tmp/paypal-typescript-sdk-collection.json
```

Expected: collection atomically publishes two separate exact-SHA work items. Any mismatch, secret finding, unsafe path, package/version mismatch, or budget failure stops without accepting partial evidence.

- [ ] **Step 3: Validate generated evidence and focused regressions**

Run:

```bash
python3 scripts/validate_github_collection.py
python3 -m unittest tests.test_github_registry tests.test_github_capsule_policy tests.test_github_capsule_selection tests.test_github_releases tests.test_collect_github_repos tests.test_github_ingest_packets tests.test_github_work_items
```

Expected: the validator and all focused suites pass.

- [ ] **Step 4: Verify immutable release identities and lifecycle state**

Run:

```bash
jq -e '.work_items | map(select(.repo_id == "paypal/paypal-typescript-server-sdk" and .state == "awaiting_approval" and .approved_mode == null)) | length == 2' tracking/github/work-items.json
jq '.work_items[] | select(.repo_id == "paypal/paypal-typescript-server-sdk") | {work_item_id,sha,state,recommended_mode,approved_mode,release_ids:[.package_changes[].release_id],ingest_packet,snapshot_manifest}' tracking/github/work-items.json
find raw/github/paypal/paypal-typescript-server-sdk/snapshots -name manifest.json -type f -print -exec jq '{repository,sha,collected_date,file_count:(.files|length),utf8_bytes:([.files[].size]|add)}' {} \;
find raw/github/paypal/paypal-typescript-server-sdk/releases/paypal-server-sdk -name manifest.json -type f -print -exec jq '{package,version,tag,sha,snapshot_manifest}' {} \;
```

Expected: one work item and release record point to canonical `2.3.0`/`b37cec58...`; the other points to `2.4.0`/`dbdbdd06...`; both remain unapproved at `awaiting_approval`; neither uses legacy SHA `ff27fa8...`.

- [ ] **Step 5: Verify the canonical comparison and evidence boundary**

Run:

```bash
jq '{repository,package,from_version,to_version,from_sha,to_sha,changed_count:(.changed_paths|length),pathspecs}' tracking/github/repos/paypal/paypal-typescript-server-sdk/comparisons/paypal-server-sdk/2.3.0--2.4.0/comparison.json
find raw/github/paypal/paypal-typescript-server-sdk/snapshots -path '*/files/src/*' -type f | wc -l
find raw/github/paypal/paypal-typescript-server-sdk/snapshots -path '*/files/doc/controllers/*' -type f | wc -l
find raw/github/paypal/paypal-typescript-server-sdk/snapshots \( -path '*/files/doc/models/*' -o -path '*/files/dist/*' -o -path '*/files/test/*' -o -path '*/files/tests/*' \) -type f | wc -l
```

Expected: the comparison is package-qualified from `2.3.0` to `2.4.0`, uses the two canonical SHAs, and classifies all 58 retained changes. Source and controller documentation are present; generated models, build output, and test trees have a zero count.

- [ ] **Step 6: Prove collection did not edit wiki knowledge**

Run:

```bash
git status --porcelain=v1 -- wiki > /private/tmp/paypal-typescript-sdk-wiki.after
cmp /private/tmp/paypal-typescript-sdk-wiki.before /private/tmp/paypal-typescript-sdk-wiki.after
```

Expected: `cmp` succeeds; collection did not create or modify a wiki page.

### Task 4: Review packets serially and stop before ingest

**Files:**
- Read: both generated `packet.json` files
- Read: both generated `packet.md` files
- Read in full: every path in each packet's `required_reading`
- Must not modify: `wiki/` or work-item approval state

**Interfaces:**
- Consumes: the two `awaiting_approval` work items from Task 3.
- Produces: a collection review report for canonical `2.3.0` first and `2.4.0` second, with ingest recommendations but no approval transition.

- [ ] **Step 1: List packets in release order**

Run:

```bash
jq -r '.work_items[] | select(.repo_id == "paypal/paypal-typescript-server-sdk") | [.package_changes[0].to_version, .work_item_id, .ingest_packet, .recommended_mode, .state] | @tsv' tracking/github/work-items.json | sort -V
```

Expected: exactly two rows appear, `2.3.0` before `2.4.0`, and both states are `awaiting_approval`.

- [ ] **Step 2: Review canonical `2.3.0` as the full baseline**

Read its `packet.json` and sibling `packet.md` in full. Enumerate its evidence with:

```bash
jq -r '.required_reading[]' tracking/github/repos/paypal/paypal-typescript-server-sdk/ingest-packets/*/packet.json | sort -u
```

Use the `2.3.0` packet's own `required_reading` list and open every listed file individually in full. Do not substitute hashes, manifests, summaries, or the legacy 16-file review for the complete canonical capsule. Confirm package identity, exact SHA, required-reading count, no unclassified retained changes, evidence gaps, exclusions, recommendation reasons, and expected wiki targets.

Expected: `2.3.0` is a canonical initial-package baseline recommended for full ingest; the review explicitly records that `ff27fa8...` remains earlier partial evidence rather than the same snapshot.

- [ ] **Step 3: Review canonical `2.4.0` against `2.3.0`**

Read its `packet.json`, sibling `packet.md`, comparison JSON/Markdown, and every `required_reading` path individually in full. Review at minimum:

- exported `ProcessingInstruction` model;
- Orders request, response, confirmation, and authorization model changes;
- Transaction Search controller and documentation changes;
- controller-reference changes across Orders, Payments, Vault, Subscriptions, and Transaction Search;
- shared model description and optionality corrections; and
- package metadata, Node compatibility, exports, and dependency changes.

Expected: every retained change is classified or explicitly reported as an evidence gap. The report notes that upstream `CHANGELOG.md` lacks a `2.4.0` section and therefore does not replace implementation evidence. Recommend the packet's evidence-driven full or delta mode without approving it.

- [ ] **Step 4: Re-run validation and verify the stop state**

Run:

```bash
python3 scripts/validate_github_collection.py
jq -e '.work_items | map(select(.repo_id == "paypal/paypal-typescript-server-sdk" and .state == "awaiting_approval" and .approved_mode == null)) | length == 2' tracking/github/work-items.json
git diff --name-only -- wiki
git diff --check
```

Expected: validation passes, both work items remain unapproved at `awaiting_approval`, and no wiki file changed.

- [ ] **Step 5: Commit only reviewed collection evidence**

Run:

```bash
git add raw/github/paypal/paypal-typescript-server-sdk tracking/github/repos/paypal/paypal-typescript-server-sdk tracking/github/work-items.json tracking/github/status.md tracking/github/collection-index.md
git diff --cached --check
git diff --cached --name-only
git commit -m "data: collect PayPal TypeScript SDK 2.3.0 and 2.4.0"
```

Expected: the commit contains only canonical collection and tracking evidence. It excludes `wiki/`, legacy raw evidence, and unrelated workspace files.

- [ ] **Step 6: Report findings and the next serial action**

Report exact release identities, file and byte counts, the canonical comparison summary, packet recommendations, evidence gaps, and validation results. State that the next action is explicit approval of canonical `@paypal/paypal-server-sdk@2.3.0` for full ingest; do not approve or claim it in this task.

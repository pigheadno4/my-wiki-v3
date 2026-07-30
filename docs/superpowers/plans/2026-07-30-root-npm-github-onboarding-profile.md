# Root npm GitHub Onboarding Profile Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prove the reusable root npm repository profile by enabling `stripe/stripe-js`, retaining the latest stable v8 and v9 releases, and stopping with validated immutable evidence and review packets awaiting approval.

**Architecture:** The existing `npm-tracked-source-v1` adapter remains the only collection implementation. A repository-specific TOML policy identifies package-qualified release tracks and bounded public-source roots; existing generic release, capsule, packet, and validation code performs collection. The Stripe pilot must not add a Stripe-specific adapter or edit wiki knowledge.

**Tech Stack:** Python 3 standard library, `unittest`, TOML registry, Git partial clones, and the existing GitHub collection and validation scripts.

## Global Constraints

- `tracking/github/repo-registry.toml` remains the only human-maintained repository policy authority.
- Use the existing `npm-tracked-source-v1` adapter with root package `@stripe/stripe-js`.
- Retain latest stable `@stripe/stripe-js@8` for historical baseline only.
- Retain latest stable `@stripe/stripe-js@9` and every future stable v9 release.
- Exclude prereleases.
- Include `src/`, `types/`, `pure/`, `examples/parcel/src/`, and `examples/rollup/src/`.
- Include standard repository context selected by the existing collector.
- Exclude tests, fixtures, example lockfiles and build configuration, dependencies, the generated `lib/` tree, and distribution artifacts as required roots.
- Retain exact tracked files referenced by public package fields such as `main`, `module`, `types`, or `exports`.
- Use limits of 512,000 bytes per file, 160 snapshot files, 2,000,000 snapshot UTF-8 bytes, 200 packet files, and 2,500,000 packet UTF-8 bytes.
- A budget failure, evidence gap, unclassified change, tag ambiguity, or package-identity mismatch stops the pilot for policy review.
- Publish no partial snapshot on failure.
- Stop successful collection at `awaiting_approval`; do not approve or ingest.
- Do not create or modify Stripe wiki source, changelog, company, concept, index, or log pages in this plan.
- Do not modify or stage unrelated Metronome Campaign 06 files or `CLAUDE copy.md`.
- A conforming future root npm repository reuses this profile and plan through its registry row and generated packet; do not create another plan unless observed evidence violates the profile contract.

---

### Task 1: Lock And Apply The Root npm Registry Policy

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`

**Interfaces:**
- Consumes: `github_registry.load_registry(path: Path) -> Tuple[RepoConfig, ...]`.
- Produces: one enabled `stripe/stripe-js` repository with two package-qualified version tracks and one bounded `npm-tracked-source-v1` capsule.
- Preserves: all other registry rows and existing generic collector behavior.

- [ ] **Step 1: Add the failing Stripe policy expectations**

In `APPENDIX_A_INVENTORY`, change only the `stripe/stripe-js` tuple's enabled value from `False` to `True`.

Add this method to `RegistryTests` before `test_registry_matches_appendix_a_inventory_and_collection_cadence`:

```python
def test_stripe_js_uses_the_root_npm_public_source_profile(self):
    repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
    stripe_js = next(repo for repo in repos if repo.id == "stripe/stripe-js")

    self.assertTrue(stripe_js.enabled)
    self.assertEqual(
        (
            VersionTrack(
                "package:@stripe/stripe-js@8",
                "latest-stable",
                "none",
            ),
            VersionTrack(
                "package:@stripe/stripe-js@9",
                "latest-stable",
                "all-stable",
            ),
        ),
        stripe_js.version_tracks,
    )
    self.assertEqual(1, len(stripe_js.capsules))
    capsule = stripe_js.capsules[0]
    self.assertEqual("stripe-js-public-source", capsule.id)
    self.assertEqual("npm-tracked-source-v1", capsule.adapter)
    self.assertEqual(("@stripe/stripe-js",), capsule.focus_packages)
    self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(
        (
            "examples/parcel/src",
            "examples/rollup/src",
            "pure",
            "src",
            "types",
        ),
        capsule.default_required_roots,
    )
    self.assertEqual((), capsule.default_generated_target_paths)
    self.assertEqual((), capsule.include_paths)
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual("text-secrets-v1", capsule.secret_detector)
    self.assertEqual(512000, capsule.max_file_bytes)
    self.assertEqual(160, capsule.max_capsule_files)
    self.assertEqual(2000000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(200, capsule.max_packet_files)
    self.assertEqual(2500000, capsule.max_packet_utf8_bytes)
```

- [ ] **Step 2: Run the focused registry tests and verify the policy is absent**

```bash
python3 -m unittest \
  tests.test_github_registry.RegistryTests.test_stripe_js_uses_the_root_npm_public_source_profile \
  tests.test_github_registry.RegistryTests.test_registry_matches_appendix_a_inventory_and_collection_cadence
```

Expected: `FAIL` because `stripe/stripe-js` is disabled and has no version tracks or capsule.

- [ ] **Step 3: Apply the approved policy to the existing Stripe JS row**

Keep the existing repository identity and metadata, change `enabled=false` to `enabled=true`, and append these child tables before the next `[[repos]]`:

```toml
[[repos.version_tracks]]
selector="package:@stripe/stripe-js@8"
backfill="latest-stable"
future="none"
include_prerelease=false
[[repos.version_tracks]]
selector="package:@stripe/stripe-js@9"
backfill="latest-stable"
future="all-stable"
include_prerelease=false
[[repos.capsules]]
id="stripe-js-public-source"
adapter="npm-tracked-source-v1"
focus_packages=["@stripe/stripe-js"]
dependency_scope="internal-runtime-closure"
changed_path_policy="policy-bounded"
default_required_roots=[
  "src",
  "types",
  "pure",
  "examples/parcel/src",
  "examples/rollup/src",
]
default_generated_target_paths=[]
include_paths=[]
excluded_categories=["tests", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=512000
max_capsule_files=160
max_capsule_utf8_bytes=2000000
max_packet_files=200
max_packet_utf8_bytes=2500000
```

Do not add a Stripe-specific adapter, path rewrite, or collector branch.

- [ ] **Step 4: Run focused profile and registry tests**

```bash
python3 -m unittest \
  tests.test_github_registry.RegistryTests.test_stripe_js_uses_the_root_npm_public_source_profile \
  tests.test_github_registry.RegistryTests.test_registry_matches_appendix_a_inventory_and_collection_cadence \
  tests.test_github_releases.GitHubReleasesTests.test_latest_stable_selects_only_the_highest_stable_candidate \
  tests.test_github_releases.GitHubReleasesTests.test_future_all_stable_selects_only_versions_absent_from_index
python3 -m unittest tests.test_github_capsule_selection
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all tests and validation pass; `git diff --check` prints nothing.

- [ ] **Step 5: Run the full offline test suite**

```bash
python3 -m unittest discover -s tests
```

Expected: `OK`. Do not weaken unrelated assertions to obtain a pass.

- [ ] **Step 6: Commit the reusable profile policy**

```bash
git add tracking/github/repo-registry.toml tests/test_github_registry.py
git diff --cached --check
git commit -m "policy: enable root npm Stripe JS capsule"
```

Expected: the commit contains exactly the registry policy and its focused test.

---

### Task 2: Collect And Validate The Stripe JS Pilot

**Files:**
- Create: `raw/github/stripe/stripe-js/snapshots/<collection-date>-<short-sha>/`
- Create: `raw/github/stripe/stripe-js/releases/stripe-js/8.11.0/<collection-date>/`
- Create: `raw/github/stripe/stripe-js/releases/stripe-js/9.12.1/<collection-date>/`
- Create: `tracking/github/repos/stripe/stripe-js/comparisons/stripe-js/8.11.0--9.12.1/`
- Create: `tracking/github/repos/stripe/stripe-js/ingest-packets/<work-item-id>/`
- Modify: `tracking/github/work-items.json`
- Modify: `tracking/github/status.md`

**Interfaces:**
- Consumes: the enabled Stripe JS registry policy from Task 1 and upstream stable tags `v8.11.0` and `v9.12.1`, verified on 2026-07-30.
- Produces: two immutable release records, exact-SHA snapshots, one v8-to-v9 comparison, and approval-gated work items with canonical review packets.
- Stops at: `awaiting_approval`, without wiki edits or ingest approval.

- [ ] **Step 1: Confirm the worktree boundary before collection**

```bash
git status --short
python3 scripts/validate_github_collection.py
```

Expected: GitHub validation passes. Record unrelated existing paths, including Metronome Campaign 06 and `CLAUDE copy.md`, and do not stage or modify them.

- [ ] **Step 2: Run the backfill collection**

```bash
python3 scripts/collect_github_repos.py collect \
  --repo stripe/stripe-js \
  --mode backfill
```

Expected: successful JSON output lists package-qualified release IDs `@stripe/stripe-js@8.11.0` and `@stripe/stripe-js@9.12.1`, with no errors. If upstream has published a newer stable v9 release since 2026-07-30, stop and update the expected version and evidence measurements before accepting output.

- [ ] **Step 3: Verify release identity and queue state**

Run this read-only assertion:

```bash
python3 -c '
import json
data = json.load(open("tracking/github/work-items.json", encoding="utf-8"))
items = [
    item for item in data["work_items"]
    if item["repo_id"] == "stripe/stripe-js"
]
release_ids = {
    change["release_id"]
    for item in items
    for change in item["package_changes"]
}
assert release_ids == {
    "@stripe/stripe-js@8.11.0",
    "@stripe/stripe-js@9.12.1",
}, release_ids
assert len(items) == 2, len(items)
assert {item["state"] for item in items} == {"awaiting_approval"}
assert all(item["ingest_packet"] for item in items)
print("stripe-js work items:", len(items))
print("release ids:", sorted(release_ids))
'
```

Expected:

```text
stripe-js work items: 2
release ids: ['@stripe/stripe-js@8.11.0', '@stripe/stripe-js@9.12.1']
```

- [ ] **Step 4: Verify every generated review packet is approval-ready**

```bash
python3 -c '
import json
from pathlib import Path
data = json.load(open("tracking/github/work-items.json", encoding="utf-8"))
items = [
    item for item in data["work_items"]
    if item["repo_id"] == "stripe/stripe-js"
]
for item in items:
    path = Path(item["ingest_packet"])
    packet = json.loads(path.read_text(encoding="utf-8"))
    assert packet["work_item_id"] == item["work_item_id"]
    assert packet["repository"] == "stripe/stripe-js"
    assert packet["required_reading"]
    assert packet["evidence_gaps"] == [], packet["evidence_gaps"]
    assert packet["unclassified_changes"] == [], packet["unclassified_changes"]
    markdown = path.with_name("packet.md")
    assert markdown.is_file(), markdown
    print(item["work_item_id"], packet["recommendation"]["mode"], len(packet["required_reading"]))
'
```

Expected: two lines, one per work item, with no assertion failure. The v8 baseline should recommend `full`; the v8-to-v9 major transition should recommend `full`.

- [ ] **Step 5: Run structural and formatting validation**

```bash
python3 scripts/validate_github_collection.py
git diff --check
git status --short -- \
  raw/github/stripe/stripe-js \
  tracking/github \
  wiki/sources/stripe \
  wiki/companies/stripe.md \
  wiki/stripe-index.md \
  wiki/stripe-log.md
```

Expected:

- GitHub validation passes.
- Raw Stripe evidence and generated tracking state are present.
- No Stripe wiki path is created or modified.

- [ ] **Step 6: Review both packet views in full**

For each Stripe work item reported by `python3 scripts/collect_github_repos.py status`:

1. Read `packet.json` in full.
2. Read `packet.md` in full.
3. Confirm release identity, exact SHA, required-reading count, recommendation, capsule budgets, evidence gaps, and unclassified changes.
4. Report the v8 packet first and the v9 packet second.

Do not run `approve`, `next-ingest`, or any wiki-editing command.

- [ ] **Step 7: Stop for user approval**

Report:

- exact package-qualified versions and SHAs;
- snapshot file and byte counts;
- release and comparison paths;
- packet paths and required-reading counts;
- recommended ingest mode for each item;
- evidence gaps and unclassified-change counts; and
- whether the root npm profile passed without collector code changes.

Do not commit the generated collection evidence until the user has reviewed the packet findings and chosen the next action.

---

## Reusing This Plan

For a future repository that satisfies the root npm profile contract:

1. Replace only the repository ID, package-qualified version tracks, bounded public roots, and measured budgets in the registry policy and focused registry test.
2. Run Task 1's focused and full validation.
3. Run Task 2 with that repository ID.
4. Stop at packet review.

Do not copy this file into a repository-specific plan. Create a new design and plan only when the repository requires a different adapter, multiple independently versioned packages, ambiguous release tags, generated-only public evidence, or another material profile exception.

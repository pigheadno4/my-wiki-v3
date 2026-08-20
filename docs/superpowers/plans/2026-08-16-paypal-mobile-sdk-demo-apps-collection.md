# PayPal Mobile SDK Demo Apps Collection Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Configure and collect checkout-focused exact-commit baselines for the PayPal Android and iOS SDK demo applications, stopping both repositories at packet review before wiki ingest.

**Architecture:** Reuse the registry-driven `commit-tree-v1` collector. Each repository receives one independent text-focused capsule and publishes its own exact-SHA snapshot, packet, and work item. The repositories are reviewed as one mobile campaign, but collection never combines their identities and never starts ingest.

**Tech Stack:** Python 3.9 standard library and project TOML fallback, `unittest`, Git CLI, TOML registry configuration, canonical JSON/Markdown evidence, existing GitHub collector and validator.

## Global Constraints

- Read `CLAUDE.md`, `rules/github-repos.md`, `rules/github/commit-tracked.md`, and the approved design before execution.
- Track each remote default branch by exact full SHA; do not fabricate package versions or release records.
- Retain checkout implementation, text runtime resources, project configuration, manifests/plists, entitlements, and README guidance.
- Exclude tests, fixtures, generated output, IDE/user state, dependency caches, CI, screenshots, videos, binary assets, and signing material.
- The Android `debug.keystore` must never be selected or copied.
- Stories and text application states remain eligible when they document integration behavior.
- Sample code does not prove merchant eligibility, regional availability, production readiness, or behavior delegated to PayPal SDK or server repositories.
- Subscription behavior is implementation evidence only when retained source implements it; README guidance alone is documentation evidence.
- Dry runs publish no raw evidence or work items. Real collection requires a separate approval and stops at `awaiting_approval`.
- Do not approve, call `next-ingest`, edit wiki pages, build either app, or run payments.
- Leave unrelated `CLAUDE copy.md` untouched.

## File Structure

- Modify `tests/test_github_registry.py`: executable contracts for both demo capsule policies and enabled states.
- Modify `tracking/github/repo-registry.toml`: two stable `commit-tree-v1` capsule policies.
- Regenerate `tracking/github/collection-index.json` and `tracking/github/collection-index.md`: deterministic scheduling state.
- Generate `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/`: Android exact-SHA evidence.
- Generate `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/`: iOS exact-SHA evidence.
- Generate repository packets under `tracking/github/repos/paypal/paypal-{android,ios}-sdk-demo-app/`.
- Modify generated `tracking/github/work-items.json` and `tracking/github/status.md` only during real collection.
- Do not create source, changelog, concept, analysis, company, index, or log pages in this plan.

---

### Task 1: Register Complete Disabled Capsule Policies

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`
- Modify generated: `tracking/github/collection-index.json`
- Modify generated: `tracking/github/collection-index.md`

**Interfaces:**
- Consumes: existing `load_registry()`, `CapsuleConfig`, and `commit-tree-v1` validation.
- Produces: two valid but disabled checkout-focused profiles that the dry-run command can inspect without publishing evidence.

- [ ] **Step 1: Add failing policy contract tests**

Add `test_paypal_mobile_demo_apps_have_reviewed_disabled_commit_policies` near the existing PayPal sample policy tests. Load both repositories and assert common identity and policy fields:

```python
for repo_id in (
    "paypal-examples/paypal-android-sdk-demo-app",
    "paypal-examples/paypal-ios-sdk-demo-app",
):
    repo = repos[repo_id]
    self.assertFalse(repo.enabled)
    self.assertEqual("sample-app", repo.repo_type)
    self.assertEqual("tier1", repo.priority)
    self.assertEqual("monthly", repo.collection_frequency)
    self.assertEqual("default-branch", repo.track)
    self.assertEqual("commit", repo.version_strategy)
    self.assertEqual((), repo.version_tracks)
    self.assertEqual(1, len(repo.capsules))
    capsule = repo.capsules[0]
    self.assertEqual("commit-tree-v1", capsule.adapter)
    self.assertEqual("configured-repository-paths", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual((), capsule.default_generated_target_paths)
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual("text-secrets-v1", capsule.secret_detector)
    self.assertEqual(512000, capsule.max_file_bytes)
    self.assertEqual(180, capsule.max_capsule_files)
    self.assertEqual(1200000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(220, capsule.max_packet_files)
    self.assertEqual(2000000, capsule.max_packet_utf8_bytes)
```

Assert the Android-specific fields:

```python
self.assertEqual("paypal-android-sdk-demo-source", android_capsule.id)
self.assertEqual("paypal-android-sdk-demo-app", android_capsule.source_id)
self.assertEqual(("app/src/main",), android_capsule.default_required_roots)
self.assertEqual(
    (
        "README.md",
        "app/build.gradle",
        "build.gradle",
        "gradle.properties",
        "gradle/libs.versions.toml",
        "settings.gradle",
    ),
    android_capsule.include_paths,
)
```

Assert the iOS-specific fields:

```python
self.assertEqual("paypal-ios-sdk-demo-source", ios_capsule.id)
self.assertEqual("paypal-ios-sdk-demo-app", ios_capsule.source_id)
self.assertEqual(("PayPalDemo",), ios_capsule.default_required_roots)
self.assertEqual(
    (
        "README.md",
        "paypal-ios-sdk-demo-app-Info.plist",
        "paypal-ios-sdk-demo-app.entitlements",
        "paypal-ios-sdk-demo-app.xcodeproj/project.pbxproj",
    ),
    ios_capsule.include_paths,
)
```

- [ ] **Step 2: Run the focused test and verify failure**

```bash
python3 -m unittest \
  tests.test_github_registry.RegistryTests.test_paypal_mobile_demo_apps_have_reviewed_disabled_commit_policies
```

Expected: failure because both disabled registry rows have no capsule.

- [ ] **Step 3: Add the Android disabled capsule**

Keep `enabled=false` and append beneath the Android row:

```toml
[[repos.capsules]]
id="paypal-android-sdk-demo-source"
adapter="commit-tree-v1"
source_id="paypal-android-sdk-demo-app"
dependency_scope="configured-repository-paths"
changed_path_policy="policy-bounded"
default_required_roots=["app/src/main"]
include_paths=["README.md","app/build.gradle","build.gradle","gradle.properties","gradle/libs.versions.toml","settings.gradle"]
excluded_categories=["tests","fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=512000
max_capsule_files=180
max_capsule_utf8_bytes=1200000
max_packet_files=220
max_packet_utf8_bytes=2000000
```

- [ ] **Step 4: Add the iOS disabled capsule**

Keep `enabled=false` and append beneath the iOS row:

```toml
[[repos.capsules]]
id="paypal-ios-sdk-demo-source"
adapter="commit-tree-v1"
source_id="paypal-ios-sdk-demo-app"
dependency_scope="configured-repository-paths"
changed_path_policy="policy-bounded"
default_required_roots=["PayPalDemo"]
include_paths=["README.md","paypal-ios-sdk-demo-app-Info.plist","paypal-ios-sdk-demo-app.entitlements","paypal-ios-sdk-demo-app.xcodeproj/project.pbxproj"]
excluded_categories=["tests","fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=512000
max_capsule_files=180
max_capsule_utf8_bytes=1200000
max_packet_files=220
max_packet_utf8_bytes=2000000
```

- [ ] **Step 5: Regenerate and validate disabled profiles**

```bash
python3 scripts/collect_github_repos.py status
python3 -m unittest tests.test_github_registry
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all checks pass; both index rows remain `disabled` and show adapter `commit-tree-v1`.

- [ ] **Step 6: Review and commit only the disabled policies**

```bash
git diff -- tests/test_github_registry.py tracking/github/repo-registry.toml tracking/github/collection-index.json tracking/github/collection-index.md
git add tests/test_github_registry.py tracking/github/repo-registry.toml tracking/github/collection-index.json tracking/github/collection-index.md
git commit -m "Configure PayPal mobile demo capsules"
```

---

### Task 2: Dry-Run Both Inventories and Enable Collection

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`
- Modify generated: `tracking/github/collection-index.json`
- Modify generated: `tracking/github/collection-index.md`
- Read only: network dry-run output and temporary clone inventory.

**Interfaces:**
- Consumes: the complete disabled profiles from Task 1.
- Produces: measured, reviewed, enabled policies with no raw snapshot or work item.

- [ ] **Step 1: Record scoped pre-run state**

```bash
git status --porcelain=v1 --untracked-files=all -- \
  raw/github/paypal/paypal-android-sdk-demo-app \
  raw/github/paypal/paypal-ios-sdk-demo-app \
  tracking/github/work-items.json \
  tracking/github/repos/paypal/paypal-android-sdk-demo-app \
  tracking/github/repos/paypal/paypal-ios-sdk-demo-app
```

Expected: no paths are present for either new repository.

- [ ] **Step 2: Run independent default-branch dry runs**

```bash
python3 scripts/collect_github_repos.py collect \
  --repo paypal-examples/paypal-android-sdk-demo-app \
  --mode backfill \
  --dry-run
python3 scripts/collect_github_repos.py collect \
  --repo paypal-examples/paypal-ios-sdk-demo-app \
  --mode backfill \
  --dry-run
```

Expected: each run resolves one default branch and full SHA, selects a nonempty bounded capsule, reports no secrets or policy errors, and publishes no snapshot or work item.

- [ ] **Step 3: Review exact selected and excluded inventories**

Confirm Android retains Kotlin/Java, manifest, Compose/UI text resources, checkout state/view models, merchant API boundary, App Links handling, Gradle dependency declarations, and README. Confirm iOS retains Swift sources, plist, entitlements, Xcode dependency metadata, checkout coordination, Payment Links, Universal Links, and README.

Confirm both exclude tests, images, videos, generated files, CI, IDE/user state, and dependency locks. Explicitly search the Android selection for `debug.keystore` and require zero matches. Stop on any secret finding, missing required path, UTF-8 failure, or budget error. If live paths differ from the policy, update the focused test and registry together, rerun both dry runs, and re-review the complete inventories before enabling.

- [ ] **Step 4: Prove dry runs published nothing**

Repeat the scoped status command from Step 1 and run:

```bash
python3 -c 'import json; p=json.load(open("tracking/github/work-items.json")); print([x["work_item_id"] for x in p["work_items"] if x["repo_id"] in {"paypal-examples/paypal-android-sdk-demo-app", "paypal-examples/paypal-ios-sdk-demo-app"}])'
```

Expected: unchanged scoped Git state and `[]`.

- [ ] **Step 5: Enable both reviewed rows and update their contract**

Change only the two rows to `enabled=true`. In `APPENDIX_A_INVENTORY`, change only their enabled values from `False` to `True`. Rename the focused test to `test_paypal_mobile_demo_apps_have_reviewed_enabled_commit_policies` and replace `self.assertFalse(repo.enabled)` with `self.assertTrue(repo.enabled)`.

- [ ] **Step 6: Regenerate and run deterministic verification**

```bash
python3 scripts/collect_github_repos.py status
python3 -m unittest tests.test_github_registry tests.test_collect_github_repos
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all checks pass and both index rows report `collect-baseline`.

- [ ] **Step 7: Commit the enabled policies and stop for collection approval**

```bash
git add tests/test_github_registry.py tracking/github/repo-registry.toml tracking/github/collection-index.json tracking/github/collection-index.md
git commit -m "Enable PayPal mobile demo collection"
```

Report each exact SHA, selected/excluded count and bytes, required-root coverage, secret result, and budget headroom. Request explicit approval before real collection.

---

### Task 3: Publish and Jointly Review Both Baselines

**Files:**
- Create: `raw/github/paypal/paypal-android-sdk-demo-app/snapshots/<date>-<short-sha>/`
- Create: `raw/github/paypal/paypal-ios-sdk-demo-app/snapshots/<date>-<short-sha>/`
- Create: `tracking/github/repos/paypal/paypal-android-sdk-demo-app/ingest-packets/<work-item-id>/`
- Create: `tracking/github/repos/paypal/paypal-ios-sdk-demo-app/ingest-packets/<work-item-id>/`
- Modify generated: `tracking/github/work-items.json`
- Modify generated: `tracking/github/status.md`
- Modify generated: `tracking/github/collection-index.json`
- Modify generated: `tracking/github/collection-index.md`

**Interfaces:**
- Consumes: the approved dry-run measurements and enabled policies.
- Produces: two independent exact-SHA snapshots and two work items at `awaiting_approval`.
- Does not produce: package releases, wiki edits, approvals, ingest claims, or a paired analysis.

- [ ] **Step 1: Run both approved baseline collections**

```bash
python3 scripts/collect_github_repos.py collect \
  --repo paypal-examples/paypal-android-sdk-demo-app \
  --mode backfill
python3 scripts/collect_github_repos.py collect \
  --repo paypal-examples/paypal-ios-sdk-demo-app \
  --mode backfill
```

Expected: each command publishes one immutable snapshot, one packet, and one `ref_changes` work item recommended as `full`; both stop at `awaiting_approval`.

- [ ] **Step 2: Read and compare both packets**

Read each `packet.json`, `packet.md`, snapshot manifest, and complete required-reading list. Confirm exact SHA linkage, zero evidence gaps, zero unclassified retained changes, no package release records, expected exclusions, no signing material, and independent source/changelog targets. Compare platform coverage without combining repository identities.

- [ ] **Step 3: Validate all generated evidence**

```bash
python3 scripts/validate_github_collection.py
python3 -m unittest \
  tests.test_github_registry \
  tests.test_github_commit_tree \
  tests.test_collect_github_repos \
  tests.test_github_ingest_packets \
  tests.test_github_work_items
git diff --check
```

Expected: all tests and validators pass, with no wiki changes.

- [ ] **Step 4: Commit only collection evidence and generated state**

```bash
git add \
  raw/github/paypal/paypal-android-sdk-demo-app \
  raw/github/paypal/paypal-ios-sdk-demo-app \
  tracking/github/repos/paypal/paypal-android-sdk-demo-app \
  tracking/github/repos/paypal/paypal-ios-sdk-demo-app \
  tracking/github/work-items.json \
  tracking/github/status.md \
  tracking/github/collection-index.json \
  tracking/github/collection-index.md
git commit -m "Collect PayPal mobile demo baselines"
```

- [ ] **Step 5: Stop at the packet approval gate**

Report both work-item IDs, exact SHAs, selected counts/bytes, required-reading counts, exclusions, evidence gaps, unclassified changes, and full-ingest recommendations. Do not approve or ingest either work item.

---

## Final Review Checklist

- [ ] Both repositories use exact default-branch commits and have independent evidence histories.
- [ ] Android and iOS checkout, return-link, lifecycle, and merchant-server boundaries are retained.
- [ ] Tests, media, generated output, user state, and signing material are excluded; `debug.keystore` is absent.
- [ ] Dry runs publish no snapshot or work item.
- [ ] Real collection creates exactly two `awaiting_approval` work items and no package release records.
- [ ] No wiki page, approval, ingest claim, or paired analysis is created automatically.
- [ ] Deterministic validation passes and unrelated worktree changes remain untouched.

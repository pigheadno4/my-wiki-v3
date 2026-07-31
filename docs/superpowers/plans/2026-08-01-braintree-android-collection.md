# Braintree Android Collection Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Configure and collect a bounded, immutable `braintree-android@5.30.0` production-source capsule, then stop with one review packet in `awaiting_approval`.

**Architecture:** Reuse the existing `tagged-tree-v1` adapter without changing collector code. Repository-specific roots, exact includes, exclusions, version selection, and budgets live in `tracking/github/repo-registry.toml`; focused tests prove that the split `UIComponents` boundary retains Kotlin/XML evidence while omitting its unsupported PNG. Collection runs only after offline checks and an isolated dry run, and it never edits the wiki.

**Tech Stack:** Python 3.9 standard library, `unittest`, TOML registry configuration, Git, existing GitHub collection and validation scripts.

## Global Constraints

- Initial identity is exactly `braintree-android@5.30.0` at tag `5.30.0` and commit `51f183a48557d0fd00eefa541712df0c4f21ee28`.
- The v5 track uses `backfill = "latest-stable"`, `future = "all-stable"`, `include_prerelease = false`, and `pinned_versions = ["5.30.0"]`.
- The capsule uses `tagged-tree-v1`, `configured-repository-paths`, and `policy-bounded`.
- Retain 13 complete production `src/main` roots and split `UIComponents` into Java/Kotlin plus readable XML roots.
- Include all 14 production module build files, the three production `proguard.pro` files, and the approved root context.
- Exclude Demo, TestUtils, tests, generated Dokka content, tooling, and `UIComponents/src/main/res/drawable-xxhdpi/card_fields_cc_discover.png`.
- Hard limits are 512,000 bytes per file, 500 snapshot files, 5,000,000 snapshot UTF-8 bytes, 550 packet files, and 6,000,000 packet UTF-8 bytes.
- More than 450 required-reading files returns to policy review.
- Do not modify shared collector behavior or weaken UTF-8, secret, hash, path, or budget checks.
- Do not approve the work item, call `next-ingest`, or edit any file under `wiki/`.
- Leave unrelated `CLAUDE copy.md` and `tracking/ingest/metronome/metronome-campaign-08/` untouched.

## File Map

| File | Responsibility |
| --- | --- |
| `tracking/github/repo-registry.toml` | Owns the executable Braintree Android v5 track and exact capsule policy. |
| `tests/test_github_registry.py` | Locks the package identity, roots, includes, exclusions, and budgets. |
| `tests/test_github_capsule_selection.py` | Proves the configured split boundary selects readable production evidence and leaves the binary PNG outside the capsule. |
| `raw/github/braintree/braintree_android/**` | Receives immutable snapshot and release evidence during approved real collection. |
| `tracking/github/repos/braintree/braintree_android/**` | Receives the immutable ingest packet and future comparisons. |
| `tracking/github/work-items.json` | Receives the approval-gated work item. |
| `tracking/github/status.md` | Receives the generated operator status. |

---

### Task 1: Configure And Test The Braintree Android Policy

**Files:**
- Modify: `tracking/github/repo-registry.toml`
- Modify: `tests/test_github_registry.py`
- Modify: `tests/test_github_capsule_selection.py`

**Interfaces:**
- Consumes: existing `VersionTrack`, `CapsuleConfig`, `load_registry()`, `resolve_capsule()`, and `tagged-tree-v1` behavior.
- Produces: one enabled `braintree/braintree_android` row with package `braintree-android`, 17 required roots, 29 exact includes, and the shared tagged-native limits.

- [ ] **Step 1: Add the failing inventory and exact-policy assertions**

In `APPENDIX_A_INVENTORY`, change only the Braintree Android row's enabled value from `False` to `True`.

Add this dedicated registry test to `RegistryTests`:

```python
def test_braintree_android_uses_the_reviewed_tagged_tree_profile(self):
    repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
    repo = next(item for item in repos if item.id == "braintree/braintree_android")

    self.assertTrue(repo.enabled)
    self.assertEqual(
        (
            VersionTrack(
                "package:braintree-android@5",
                "latest-stable",
                "all-stable",
                False,
                ("5.30.0",),
            ),
        ),
        repo.version_tracks,
    )
    self.assertEqual(1, len(repo.capsules))
    capsule = repo.capsules[0]
    self.assertEqual("braintree-android-public-source", capsule.id)
    self.assertEqual("tagged-tree-v1", capsule.adapter)
    self.assertEqual(("braintree-android",), capsule.focus_packages)
    self.assertEqual("configured-repository-paths", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(
        {
            "AmericanExpress/src/main",
            "BraintreeCore/src/main",
            "Card/src/main",
            "DataCollector/src/main",
            "GooglePay/src/main",
            "LocalPayment/src/main",
            "PayPal/src/main",
            "PayPalMessaging/src/main",
            "SEPADirectDebit/src/main",
            "ShopperInsights/src/main",
            "SharedUtils/src/main",
            "ThreeDSecure/src/main",
            "UIComponents/src/main/java",
            "UIComponents/src/main/res/drawable",
            "UIComponents/src/main/res/layout",
            "UIComponents/src/main/res/values",
            "Venmo/src/main",
        },
        set(capsule.default_required_roots),
    )
    self.assertEqual(
        {
            "README.md",
            "CHANGELOG.md",
            "v5_MIGRATION_GUIDE.md",
            "v4_MIGRATION_GUIDE.md",
            "v4.9.0+_MIGRATION_GUIDE.md",
            "APP_LINK_SETUP.md",
            "DEPENDENCIES.md",
            "LICENSE",
            "settings.gradle",
            "build.gradle",
            "gradle.properties",
            "UIComponents/src/main/AndroidManifest.xml",
            "AmericanExpress/build.gradle",
            "BraintreeCore/build.gradle",
            "Card/build.gradle",
            "DataCollector/build.gradle",
            "GooglePay/build.gradle",
            "LocalPayment/build.gradle",
            "PayPal/build.gradle",
            "PayPalMessaging/build.gradle",
            "SEPADirectDebit/build.gradle",
            "ShopperInsights/build.gradle",
            "SharedUtils/build.gradle",
            "ThreeDSecure/build.gradle",
            "UIComponents/build.gradle",
            "Venmo/build.gradle",
            "BraintreeCore/proguard.pro",
            "GooglePay/proguard.pro",
            "ThreeDSecure/proguard.pro",
        },
        set(capsule.include_paths),
    )
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual(512000, capsule.max_file_bytes)
    self.assertEqual(500, capsule.max_capsule_files)
    self.assertEqual(5000000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(550, capsule.max_packet_files)
    self.assertEqual(6000000, capsule.max_packet_utf8_bytes)
    self.assertNotIn(
        "UIComponents/src/main/res/drawable-xxhdpi",
        capsule.default_required_roots,
    )
```

Also add `braintree/braintree_android`, `braintree-android`, major `5`, pin `5.30.0`, root count `17`, and include count `29` to the table in `test_native_sdks_use_tagged_tree_profiles`.

- [ ] **Step 2: Add the failing selection fixture**

Import `load_registry` into `tests/test_github_capsule_selection.py`, then add this test to `CapsuleSelectionTests`:

```python
def test_braintree_android_policy_excludes_binary_ui_asset(self):
    repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
    repo = next(item for item in repos if item.id == "braintree/braintree_android")
    capsule = repo.capsules[0]
    files = {
        root + "/Evidence.kt": "public class Evidence\n"
        for root in capsule.default_required_roots
    }
    files.update({path: "evidence\n" for path in capsule.include_paths})
    files["UIComponents/src/main/res/drawable/paypal_logo.xml"] = "<vector />\n"
    files[
        "UIComponents/src/main/res/drawable-xxhdpi/card_fields_cc_discover.png"
    ] = b"\x89PNG\x00binary"
    files["Demo/src/main/java/Demo.kt"] = "class Demo\n"
    files["TestUtils/src/main/java/TestHelper.kt"] = "class TestHelper\n"

    result = resolve_capsule(
        self.tree(files),
        capsule,
        (),
        versions={"braintree-android": "5.30.0"},
    )
    selected = {item.path for item in result.files}

    self.assertIn(
        "UIComponents/src/main/res/drawable/paypal_logo.xml",
        selected,
    )
    self.assertIn("UIComponents/src/main/AndroidManifest.xml", selected)
    self.assertNotIn(
        "UIComponents/src/main/res/drawable-xxhdpi/card_fields_cc_discover.png",
        selected,
    )
    self.assertNotIn("Demo/src/main/java/Demo.kt", selected)
    self.assertNotIn("TestUtils/src/main/java/TestHelper.kt", selected)
```

- [ ] **Step 3: Run the focused tests and confirm the expected failure**

Run:

```bash
python3 -m unittest \
  tests.test_github_registry.RegistryTests.test_braintree_android_uses_the_reviewed_tagged_tree_profile \
  tests.test_github_capsule_selection.CapsuleSelectionTests.test_braintree_android_policy_excludes_binary_ui_asset
```

Expected: fail because the current Braintree Android row is disabled and has no version track or capsule.

- [ ] **Step 4: Configure the registry row**

Replace the inventory-only Braintree Android row with an enabled row and this version track:

```toml
[[repos.version_tracks]]
selector="package:braintree-android@5"
backfill="latest-stable"
future="all-stable"
include_prerelease=false
pinned_versions=["5.30.0"]
```

Add capsule `braintree-android-public-source` using the required roots:

```text
AmericanExpress/src/main
BraintreeCore/src/main
Card/src/main
DataCollector/src/main
GooglePay/src/main
LocalPayment/src/main
PayPal/src/main
PayPalMessaging/src/main
SEPADirectDebit/src/main
ShopperInsights/src/main
SharedUtils/src/main
ThreeDSecure/src/main
Venmo/src/main
UIComponents/src/main/java
UIComponents/src/main/res/drawable
UIComponents/src/main/res/layout
UIComponents/src/main/res/values
```

Use these 29 exact includes:

```text
README.md
CHANGELOG.md
v5_MIGRATION_GUIDE.md
v4_MIGRATION_GUIDE.md
v4.9.0+_MIGRATION_GUIDE.md
APP_LINK_SETUP.md
DEPENDENCIES.md
LICENSE
settings.gradle
build.gradle
gradle.properties
UIComponents/src/main/AndroidManifest.xml
AmericanExpress/build.gradle
BraintreeCore/build.gradle
Card/build.gradle
DataCollector/build.gradle
GooglePay/build.gradle
LocalPayment/build.gradle
PayPal/build.gradle
PayPalMessaging/build.gradle
SEPADirectDebit/build.gradle
ShopperInsights/build.gradle
SharedUtils/build.gradle
ThreeDSecure/build.gradle
UIComponents/build.gradle
Venmo/build.gradle
BraintreeCore/proguard.pro
GooglePay/proguard.pro
ThreeDSecure/proguard.pro
```

Set `default_generated_target_paths=[]`, `excluded_categories=["tests", "fixtures"]`, `secret_detector="text-secrets-v1"`, and the exact limits from Global Constraints.

- [ ] **Step 5: Run focused and complete offline verification**

Run:

```bash
python3 -m unittest \
  tests.test_github_registry \
  tests.test_github_capsule_selection \
  tests.test_github_tagged_tree
python3 -m unittest discover -s tests -p 'test_github_*.py'
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all tests and validation pass. The focused fixture proves the binary PNG is unselected while retained XML is selected.

- [ ] **Step 6: Commit the executable policy**

```bash
git add \
  tracking/github/repo-registry.toml \
  tests/test_github_registry.py \
  tests/test_github_capsule_selection.py
git commit -m "config: enable braintree android collection"
```

---

### Task 2: Prove Backfill And Capsule Selection In Isolated State

**Files:**
- Read: committed repository state exported under `/private/tmp`
- Do not modify: the real workspace's raw evidence, work items, status, or wiki

**Interfaces:**
- Consumes: `collect_github_repos.py collect --repo braintree/braintree_android --mode backfill --dry-run`.
- Produces: a dry-run report selecting only `braintree-android@5.30.0` and no persistent collection artifacts.

- [ ] **Step 1: Re-run pre-network verification**

```bash
python3 -m unittest discover -s tests -p 'test_github_*.py'
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all pass before network access.

- [ ] **Step 2: Export committed state to an isolated directory**

```bash
DRY_ROOT="$(mktemp -d /private/tmp/braintree-android-dryrun.XXXXXX)"
git archive --format=tar HEAD -o "$DRY_ROOT/repo.tar"
mkdir "$DRY_ROOT/repo"
tar -xf "$DRY_ROOT/repo.tar" -C "$DRY_ROOT/repo"
```

The archive is required because the current CLI can persist failure status from a nominal dry run.

- [ ] **Step 3: Run the isolated backfill dry run**

```bash
cd "$DRY_ROOT/repo"
python3 scripts/collect_github_repos.py collect \
  --repo braintree/braintree_android \
  --mode backfill \
  --dry-run
```

Expected result fields:

```json
{
  "errors": [],
  "release_ids": ["braintree-android@5.30.0"],
  "repo_id": "braintree/braintree_android",
  "snapshot_paths": [],
  "state": "discovered",
  "work_item_ids": []
}
```

Confirm upstream tag `5.30.0` still resolves to commit `51f183a48557d0fd00eefa541712df0c4f21ee28`. If a newer stable v5 release appears, the tag moves, required paths drift, a secret is detected, or a budget fails, stop and return to design review. Do not change limits during this task.

- [ ] **Step 4: Prove the real workspace was not modified**

Return to `/Users/tengtao/Development/wiki-v2` and run:

```bash
git status --short
```

Expected: only the pre-existing unrelated untracked paths remain. Report the dry-run release identity, tag, SHA, and any warnings to the user. No commit is produced by this task.

- [ ] **Step 5: Stop for explicit collection approval**

Do not continue to Task 3 until the user reviews the dry-run result and explicitly approves real collection.

---

### Task 3: Collect The Baseline And Stop At Ingest Approval

**Files:**
- Create: `raw/github/braintree/braintree_android/snapshots/<date>-51f183a/**`
- Create: `raw/github/braintree/braintree_android/releases/braintree-android/5.30.0/<date>/**`
- Create: `tracking/github/repos/braintree/braintree_android/ingest-packets/<work-item-id>/**`
- Modify: `tracking/github/work-items.json`
- Modify: `tracking/github/status.md`

**Interfaces:**
- Consumes: the approved registry policy and user-approved dry-run result.
- Produces: one exact-SHA snapshot, one package release record, one packet recommending `full`, and one work item in `awaiting_approval`.

- [ ] **Step 1: Confirm collection approval and clean preconditions**

Run:

```bash
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py status
git status --short
```

Expected: validation passes, no Braintree Android item exists, and only known unrelated untracked paths are present.

- [ ] **Step 2: Collect the exact approved release**

```bash
python3 scripts/collect_github_repos.py collect \
  --repo braintree/braintree_android \
  --release braintree-android@5.30.0
```

Expected: one snapshot path and one work-item ID are returned, with no errors.

- [ ] **Step 3: Validate generated evidence and lifecycle state**

Run:

```bash
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py status
python3 -m unittest discover -s tests -p 'test_github_*.py'
git diff --check
```

Inspect the generated snapshot manifest, release manifest and notes, `packet.json`, and `packet.md`. Confirm:

- repository is `braintree/braintree_android`;
- release identity is `braintree-android@5.30.0`;
- snapshot SHA is `51f183a48557d0fd00eefa541712df0c4f21ee28`;
- the snapshot contains exactly 388 files and 1,171,992 selected UTF-8 bytes unless standard collector context is reported separately and reconciled;
- required reading is at most 450 files;
- snapshot and packet hard budgets pass;
- all 14 production modules have retained readable evidence;
- `UIComponents` Kotlin, manifest, drawable XML, layout XML, and values XML are present;
- the Discover card PNG, Demo, TestUtils, tests, Dokka output, CI, and tooling are absent;
- `unclassified_changes` and `evidence_gaps` are empty;
- recommendation mode is `full`; and
- work-item state is `awaiting_approval`.

If any assertion fails, stop before committing. Preserve the failure evidence according to `rules/github-repos.md`; do not approve or ingest the item.

- [ ] **Step 4: Prove the wiki boundary**

```bash
git status --short wiki
```

Expected: no output. Do not create the expected Braintree source or changelog pages during collection.

- [ ] **Step 5: Commit only validated collection artifacts**

```bash
git add \
  raw/github/braintree/braintree_android \
  tracking/github/repos/braintree/braintree_android \
  tracking/github/work-items.json \
  tracking/github/status.md
git commit -m "data: collect braintree android 5.30.0"
```

- [ ] **Step 6: Final verification and stop**

```bash
python3 scripts/validate_github_collection.py
python3 -m unittest discover -s tests -p 'test_github_*.py'
python3 scripts/collect_github_repos.py status
git status --short --branch
```

Expected: all checks pass, the Braintree Android item remains `awaiting_approval`, no wiki file changed, and unrelated untracked paths remain untouched.

Report the packet path, work-item ID, counts, SHA, recommendation, and evidence gaps. The next workflow is packet review and separate user approval for serial full ingest; it is outside this plan.

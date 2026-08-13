# Braintree Mobile Drop-in Baselines Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Collect approval-gated current stable baselines for Braintree iOS Drop-in and Android Drop-in, ingest them serially as independent package histories, and publish one source-grounded cross-platform comparison.

**Architecture:** Reuse the existing release-tracked GitHub pipeline and `tagged-tree-v1` adapter. Each repository receives one package-qualified version track and one bounded public-source capsule. Collection may cover both repositories in one campaign, but it publishes independent exact-SHA snapshots, release records, packets, and work items. Wiki ingest remains one full-read work item at a time: iOS reaches `ingested` before Android is claimed, and the paired analysis is written only after both source histories are complete.

**Tech Stack:** Python 3 standard library, `unittest`, TOML registry configuration, Git CLI, JSON/Markdown evidence artifacts, existing GitHub collection and wiki validators.

## Global Constraints

- Initial release identities are `BraintreeDropIn@9.14.0` and `drop-in@6.17.0`; never shorten these to repository-level `v9` or `v6` labels.
- Both repositories remain independent from `braintree/braintree_ios` and `braintree/braintree_android`; parent SDK evidence may be linked but not merged into either Drop-in history.
- Use `semver-tags`, `tagged-tree-v1`, weekly collection, Tier 1 priority, stable releases only, and future `all-stable` tracking.
- Retain complete public implementation roots and useful demo or story code. Exclude tests, fixtures, generated API documentation, screenshots, image catalogs, binaries, CI, release automation, signing material, lockfiles, and unrelated tooling.
- A dry run publishes no raw, tracking, or wiki evidence. Real collection requires a separate user approval and stops both work items at `awaiting_approval`.
- Ingest is `NO BATCH, MUST PROCESS ONE BY ONE, READ FULL CONTENT OF RAW AND THEN INGEST`.
- Each initial baseline uses full ingest. Later contained releases may use delta ingest only after packet review.
- Demo presence proves an integration surface exists in the retained source; it does not prove merchant eligibility, payment-method availability, or successful payment execution.
- Do not build the mobile projects, execute payments, collect historical majors, or edit parent SDK source pages in this campaign.
- Leave unrelated `CLAUDE copy.md` untouched.

**Approved implementation note:** The shared release parser originally enforced npm lowercase naming for every adapter. Before Task 1, add case-sensitive unscoped release identities for `tagged-tree-v1` while preserving npm-package-name validation for `npm-tracked-source-v1`. This is required to retain the exact Swift package identity `BraintreeDropIn@9.14.0`.

**Measurement correction:** The first temporary capsule resolution found PNG assets beneath the broad iOS and Android demo/runtime roots. The final policy therefore uses text-only implementation, demo, and Android XML resource subroots; it retains iOS Swift demo code and Android Java/Kotlin plus manifests, layouts, animations, XML drawables, core values, and all existing localization values while excluding image catalogs and density PNGs.

## File Structure

- Modify `tests/test_github_registry.py`: executable contract for both Drop-in registry policies.
- Modify `tracking/github/repo-registry.toml`: enable both repositories, package tracks, capsule roots, explicit files, exclusions, and budgets.
- Generate independent raw snapshots and release records under `raw/github/braintree/braintree-{ios,android}-drop-in/`.
- Generate independent packets and lifecycle state under `tracking/github/repos/braintree/braintree-{ios,android}-drop-in/` and shared generated tracking files.
- Create `wiki/sources/braintree/github/source-github-braintree-ios-drop-in.md` and `changelog-github-braintree-ios-drop-in.md`.
- Create `wiki/sources/braintree/github/source-github-braintree-android-drop-in.md` and `changelog-github-braintree-android-drop-in.md`.
- Create `wiki/analyses/analysis-braintree-drop-in-ios-vs-android.md` after both ingests.
- Modify `wiki/companies/braintree.md`, `wiki/concepts/braintree-ios-sdk.md`, `wiki/concepts/braintree-android-sdk.md`, `wiki/braintree-index.md`, `wiki/braintree-log.md`, `wiki/index.md`, and `wiki/log.md` only when the completed evidence requires navigation or factual updates.

---

### Task 1: Add Executable Registry Policies

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`

**Interfaces:**
- Consumes: existing `load_registry()`, `VersionTrack`, `CapsuleConfig`, and `tagged-tree-v1` schema.
- Produces: two enabled, package-qualified, bounded public-source collection policies.

- [ ] **Step 1: Add failing registry contract tests**

Change the two rows in `APPENDIX_A_INVENTORY` from disabled to enabled. Add one test per repository, following the existing Braintree profile tests.

The iOS assertions must require:

```python
self.assertEqual(
    (
        VersionTrack(
            "package:BraintreeDropIn@9",
            "latest-stable",
            "all-stable",
            False,
            ("9.14.0",),
        ),
    ),
    repo.version_tracks,
)
self.assertEqual("braintree-ios-drop-in-public-source", capsule.id)
self.assertEqual("tagged-tree-v1", capsule.adapter)
self.assertEqual(("BraintreeDropIn",), capsule.focus_packages)
self.assertEqual(
    {
        "Demo/Application/Settings",
        "Demo/Application/SwiftUI",
        "Sources/BraintreeDropIn",
    },
    set(capsule.default_required_roots),
)
self.assertEqual(
    (
        "BraintreeDropIn.podspec",
        "BraintreeDropIn.xcodeproj/project.pbxproj",
        "CHANGELOG.md",
        "DEVELOPMENT.md",
        "Demo/Application/DemoAppDelegate.swift",
        "Demo/Application/DemoBaseViewController.swift",
        "Demo/Application/DemoContainerViewController.swift",
        "Demo/Application/DemoDropInView.swift",
        "Demo/Application/DemoDropInViewController.swift",
        "Demo/Application/DemoMerchantAPIClient.swift",
        "Demo/Application/DemoPurchaseButton.swift",
        "Demo/Application/ViewHelpers.swift",
        "LICENSE",
        "Package.swift",
        "README.md",
    ),
    capsule.include_paths,
)
```

The Android assertions must require:

```python
self.assertEqual(
    (
        VersionTrack(
            "package:drop-in@6",
            "latest-stable",
            "all-stable",
            False,
            ("6.17.0",),
        ),
    ),
    repo.version_tracks,
)
self.assertEqual("braintree-android-drop-in-public-source", capsule.id)
self.assertEqual("tagged-tree-v1", capsule.adapter)
self.assertEqual(("drop-in",), capsule.focus_packages)
self.assertEqual(
    {
        "Demo/src/main/java",
        "Demo/src/main/res/layout",
        "Demo/src/main/res/menu",
        "Demo/src/main/res/values",
        "Demo/src/main/res/xml",
        "Drop-In/src/main/java",
        "Drop-In/src/main/res/anim",
        "Drop-In/src/main/res/drawable",
        "Drop-In/src/main/res/drawable-v21",
        "Drop-In/src/main/res/layout",
        "Drop-In/src/main/res/values",
    },
    set(capsule.default_required_roots).intersection({
        "Demo/src/main/java",
        "Demo/src/main/res/layout",
        "Demo/src/main/res/menu",
        "Demo/src/main/res/values",
        "Demo/src/main/res/xml",
        "Drop-In/src/main/java",
        "Drop-In/src/main/res/anim",
        "Drop-In/src/main/res/drawable",
        "Drop-In/src/main/res/drawable-v21",
        "Drop-In/src/main/res/layout",
        "Drop-In/src/main/res/values",
    }),
)
self.assertEqual(
    (
        "ACKNOWLEDGEMENTS.md",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "DEVELOPMENT.md",
        "Demo/build.gradle",
        "Demo/src/main/AndroidManifest.xml",
        "Drop-In/build.gradle",
        "Drop-In/src/main/AndroidManifest.xml",
        "LICENSE",
        "README.md",
        "build.gradle",
        "gradle.properties",
        "settings.gradle",
        "v6_MIGRATION_GUIDE.md",
    ),
    capsule.include_paths,
)
```

The Android contract additionally enumerates every `Drop-In/src/main/res/values-*` text directory present in `6.17.0`; broad `Demo/src/main` and `Drop-In/src/main` roots are forbidden because they include PNG assets.

For both capsules assert `dependency_scope == "configured-repository-paths"`, `changed_path_policy == "policy-bounded"`, no generated targets, `excluded_categories == ("fixtures", "tests")`, `secret_detector == "text-secrets-v1"`, a 512,000-byte per-file limit, 500 capsule files / 5,000,000 UTF-8 bytes, and 550 packet files / 6,000,000 UTF-8 bytes.

- [ ] **Step 2: Run the focused tests and verify failure**

```bash
python3 -m unittest \
  tests.test_github_registry.RegistryTests.test_braintree_ios_drop_in_uses_reviewed_public_source_capsule \
  tests.test_github_registry.RegistryTests.test_braintree_android_drop_in_uses_reviewed_public_source_capsule
```

Expected: both fail because the inventory entries are disabled and have no tracks or capsules.

- [ ] **Step 3: Replace only the two disabled registry rows**

Configure the exact identities, roots, include paths, exclusions, detector, and budgets asserted in Step 1. Preserve `repo_type="drop-in"`, `priority="tier1"`, `collection_frequency="weekly"`, `track="releases-and-default-branch"`, and `version_strategy="semver-tags"`.

- [ ] **Step 4: Run focused and registry regression checks**

```bash
python3 -m unittest \
  tests.test_github_registry \
  tests.test_github_capsule_policy \
  tests.test_github_capsule_selection
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all tests pass and the validator reports no structural errors.

- [ ] **Step 5: Review and commit the policy only**

```bash
git diff -- tests/test_github_registry.py tracking/github/repo-registry.toml
git status --short
git add tests/test_github_registry.py tracking/github/repo-registry.toml
git commit -m "Enable Braintree mobile Drop-in collection"
```

### Task 2: Verify Both Baselines Without Publishing

**Files:**
- Read: `tracking/github/repo-registry.toml`
- Read: dry-run output and temporary clone measurements only.
- Must not modify: `raw/`, `tracking/github/work-items.json`, or `wiki/`.

**Interfaces:**
- Consumes: committed policies and upstream stable tags.
- Produces: exact tag/SHA identities, capsule measurements, exclusions, and a real-collection approval request.

- [ ] **Step 1: Record pre-run state**

```bash
git status --short
git rev-parse HEAD
```

- [ ] **Step 2: Run independent release dry runs**

```bash
python3 scripts/collect_github_repos.py collect \
  --repo braintree/braintree-ios-drop-in \
  --release BraintreeDropIn@9.14.0 \
  --dry-run
python3 scripts/collect_github_repos.py collect \
  --repo braintree/braintree-android-drop-in \
  --release drop-in@6.17.0 \
  --dry-run
```

Expected: each package-qualified release resolves to one stable upstream tag and one full commit SHA. Any tag ambiguity or identity mismatch blocks the campaign.

- [ ] **Step 3: Resolve and measure both capsules in temporary clones**

Run the configured capsule resolver against each exact tag. Report selected file count and UTF-8 bytes, required-root coverage, explicit include-path coverage, rejected paths, secret findings, and budget headroom.

Inspect the selected path list and confirm:

- iOS retains all text source beneath `Sources/BraintreeDropIn` and useful text demo files beneath `Demo/Application`;
- Android retains all text source/resources beneath `Drop-In/src/main` and useful text demo files beneath `Demo/src/main`;
- neither capsule retains tests, generated docs, screenshots, image catalogs, APKs, archives, lockfiles, CI, or signing files;
- story or demo-state source files are retained when they document public integration behavior.

If an approved root or explicit file is absent upstream, or a checkout-critical public file is excluded, stop and revise Task 1 with a new test before collecting.

- [ ] **Step 4: Prove the dry runs published nothing**

```bash
git status --short
find raw/github/braintree/braintree-ios-drop-in -type f
find raw/github/braintree/braintree-android-drop-in -type f
jq '[.work_items[] | select(.repo_id == "braintree/braintree-ios-drop-in" or .repo_id == "braintree/braintree-android-drop-in")] | length' tracking/github/work-items.json
```

Expected: no new raw files, no new work items, and repository state matches Step 1.

- [ ] **Step 5: Stop for real-collection approval**

Report both exact tags/SHAs and capsule measurements together. Do not remove `--dry-run` until the user explicitly approves real collection.

### Task 3: Publish and Jointly Review Both Collection Packets

**Files:**
- Generate: `raw/github/braintree/braintree-ios-drop-in/snapshots/` and `releases/`
- Generate: `raw/github/braintree/braintree-android-drop-in/snapshots/` and `releases/`
- Generate: repository packets under `tracking/github/repos/braintree/`
- Modify generated: `tracking/github/work-items.json`, `status.md`, `collection-index.json`, and `collection-index.md`

**Interfaces:**
- Consumes: the approved dry-run report.
- Produces: two immutable, independent baseline work items at `awaiting_approval`.

- [ ] **Step 1: Confirm the separate real-collection approval**

Proceed only after the user approves the measurements from Task 2.

- [ ] **Step 2: Collect both exact baselines**

```bash
python3 scripts/collect_github_repos.py collect \
  --repo braintree/braintree-ios-drop-in \
  --release BraintreeDropIn@9.14.0
python3 scripts/collect_github_repos.py collect \
  --repo braintree/braintree-android-drop-in \
  --release drop-in@6.17.0
```

Expected: each run publishes one immutable snapshot, one package release record, one packet, and one work item. Both work items stop at `awaiting_approval`; no wiki page changes.

- [ ] **Step 3: Read and compare both packets**

Read each `packet.json`, `packet.md`, snapshot manifest, release manifest, and complete required-reading path list. Compare capsule consistency across platforms while preserving independent identities. Confirm zero evidence gaps, zero unclassified retained changes, expected exclusions, exact SHA linkage, and `full` recommendation.

- [ ] **Step 4: Validate and commit collection evidence**

```bash
python3 scripts/validate_github_collection.py
python3 -m unittest \
  tests.test_github_registry \
  tests.test_github_capsule_policy \
  tests.test_github_capsule_selection \
  tests.test_github_releases \
  tests.test_collect_github_repos \
  tests.test_github_ingest_packets \
  tests.test_github_work_items
git diff --check
git add \
  raw/github/braintree/braintree-ios-drop-in \
  raw/github/braintree/braintree-android-drop-in \
  tracking/github
git commit -m "Collect Braintree mobile Drop-in baselines"
```

- [ ] **Step 5: Stop for two packet approvals**

Report each work-item ID, release identity, exact SHA, recommendation, required-reading count, selected measurements, and any warnings. Do not run `approve`, `next-ingest`, or edit `wiki/`.

### Task 4: Fully Ingest the iOS Baseline

**Files:**
- Create: `wiki/sources/braintree/github/source-github-braintree-ios-drop-in.md`
- Create: `wiki/sources/braintree/github/changelog-github-braintree-ios-drop-in.md`
- Modify only if supported: `wiki/companies/braintree.md`, `wiki/concepts/braintree-ios-sdk.md`, `wiki/braintree-index.md`, `wiki/braintree-log.md`, `wiki/index.md`, `wiki/log.md`
- Modify generated: GitHub work-item and status files.

**Interfaces:**
- Consumes: explicitly approved iOS work item and every file in its required-reading list.
- Produces: cumulative iOS Drop-in source/changelog pages and a terminal iOS work item.

- [ ] **Step 1: Approve and claim only iOS**

Resolve the exact pending iOS work-item ID from `tracking/github/work-items.json`. Run `python3 scripts/collect_github_repos.py status` and verify no different item is already `approved` or `ingesting`; if one exists, stop and finish that serial item first. Then run:

```bash
python3 scripts/collect_github_repos.py approve --item "$IOS_ITEM_ID" --mode full
python3 scripts/collect_github_repos.py next-ingest
```

Verify the claimed item is the approved iOS baseline. If another item is returned, stop without editing wiki pages.

- [ ] **Step 2: Perform the complete serial read**

Read `rules/ingest.md`, `rules/github-repos.md`, and `rules/github/release-tracked.md`, then read the packet, manifests, release metadata, every retained raw file in `required_reading`, relevant existing Braintree company/concept pages, and comparable mobile source/changelog pages in full. Record 3-5 exact grounding quotes with source paths before drafting.

- [ ] **Step 3: Write the cumulative iOS pages**

The source page must preserve:

- exact `BraintreeDropIn@9.14.0` identity, tag, SHA, collection date, upstream URL, packet, and snapshot provenance;
- package installation and parent `Braintree` SDK compatibility boundaries;
- authorization, Drop-in launch/configuration, result/cancel/error handling, payment-method nonce and server handoff;
- cards, PayPal, Venmo, Apple Pay, 3D Secure, vaulted methods, app/browser switching, customization, accessibility, and lifecycle behavior only where directly evidenced;
- demo-only, delegated-to-parent-SDK, unsupported, and unresolved boundaries.

The changelog owns the package-qualified `9.14.0` baseline and future release timeline. It links the cumulative source page and immutable raw evidence without duplicating the full implementation narrative.

- [ ] **Step 4: Audit concepts and navigation**

Update `braintree-ios-sdk.md` only for supported Drop-in relationships or delegated behavior. Add source/index/log links once, without turning Drop-in into the parent SDK or claiming a demo as availability proof.

- [ ] **Step 5: Validate, complete, and commit iOS**

```bash
python3 scripts/validate_wiki.py \
  wiki/sources/braintree/github/source-github-braintree-ios-drop-in.md \
  wiki/sources/braintree/github/changelog-github-braintree-ios-drop-in.md \
  wiki/braintree-index.md \
  wiki/braintree-log.md
python3 scripts/collect_github_repos.py complete-ingest --item "$IOS_ITEM_ID"
python3 scripts/validate_github_collection.py
git diff --check
git add \
  wiki/sources/braintree/github/source-github-braintree-ios-drop-in.md \
  wiki/sources/braintree/github/changelog-github-braintree-ios-drop-in.md \
  wiki/companies/braintree.md \
  wiki/concepts/braintree-ios-sdk.md \
  wiki/braintree-index.md wiki/braintree-log.md wiki/index.md wiki/log.md \
  tracking/github
git commit -m "Ingest Braintree iOS Drop-in baseline"
```

Stage only files actually changed. Expected: the iOS work item is `ingested`; Android remains unclaimed.

### Task 5: Fully Ingest the Android Baseline

**Files:**
- Create: `wiki/sources/braintree/github/source-github-braintree-android-drop-in.md`
- Create: `wiki/sources/braintree/github/changelog-github-braintree-android-drop-in.md`
- Modify only if supported: `wiki/companies/braintree.md`, `wiki/concepts/braintree-android-sdk.md`, `wiki/braintree-index.md`, `wiki/braintree-log.md`, `wiki/index.md`, `wiki/log.md`
- Modify generated: GitHub work-item and status files.

**Interfaces:**
- Consumes: explicitly approved Android work item after iOS is terminal, plus every Android required-reading file.
- Produces: cumulative Android Drop-in source/changelog pages and a terminal Android work item.

- [ ] **Step 1: Confirm iOS terminal, then approve and claim Android**

Verify the iOS item is `ingested`. Resolve the exact pending Android work-item ID. Run `python3 scripts/collect_github_repos.py status` and verify no different item is already `approved` or `ingesting`; if one exists, stop and preserve queue order. Then run:

```bash
python3 scripts/collect_github_repos.py approve --item "$ANDROID_ITEM_ID" --mode full
python3 scripts/collect_github_repos.py next-ingest
```

Verify the claimed item is Android before editing.

- [ ] **Step 2: Perform the complete serial read**

Re-read `rules/ingest.md`, `rules/github-repos.md`, and `rules/github/release-tracked.md`, then read the packet, manifests, release metadata, every retained raw file in `required_reading`, `v6_MIGRATION_GUIDE.md`, relevant Braintree company/concept pages, and comparable Android source/changelog pages in full. Record 3-5 grounding quotes with paths before drafting.

- [ ] **Step 3: Write the cumulative Android pages**

Preserve exact `drop-in@6.17.0` provenance and document authorization, Drop-in request/launch/result APIs, nonce/server handoff, payment-method surfaces, vault behavior, browser/app switching, Android lifecycle, customization, and accessibility only where evidenced. Keep v6 migration and parent `braintree_android` compatibility explicit. Separate demo behavior, delegated behavior, unsupported behavior, and unresolved questions.

The changelog owns the package-qualified `6.17.0` baseline and future release timeline.

- [ ] **Step 4: Audit concepts and navigation**

Update `braintree-android-sdk.md` only for supported Drop-in relationships or delegated behavior. Add source/index/log links once and preserve parent SDK version history separately.

- [ ] **Step 5: Validate, complete, and commit Android**

```bash
python3 scripts/validate_wiki.py \
  wiki/sources/braintree/github/source-github-braintree-android-drop-in.md \
  wiki/sources/braintree/github/changelog-github-braintree-android-drop-in.md \
  wiki/braintree-index.md \
  wiki/braintree-log.md
python3 scripts/collect_github_repos.py complete-ingest --item "$ANDROID_ITEM_ID"
python3 scripts/validate_github_collection.py
git diff --check
git add \
  wiki/sources/braintree/github/source-github-braintree-android-drop-in.md \
  wiki/sources/braintree/github/changelog-github-braintree-android-drop-in.md \
  wiki/companies/braintree.md \
  wiki/concepts/braintree-android-sdk.md \
  wiki/braintree-index.md wiki/braintree-log.md wiki/index.md wiki/log.md \
  tracking/github
git commit -m "Ingest Braintree Android Drop-in baseline"
```

Stage only files actually changed. Expected: both work items are terminal and independently queryable.

### Task 6: Publish the Paired Analysis and Verify the Campaign

**Files:**
- Create: `wiki/analyses/analysis-braintree-drop-in-ios-vs-android.md`
- Modify: `wiki/braintree-index.md`, `wiki/braintree-log.md`, `wiki/index.md`, `wiki/log.md`

**Interfaces:**
- Consumes: both complete cumulative source pages and both changelogs.
- Produces: one version-qualified cross-platform analysis without merging repository histories.

- [ ] **Step 1: Read both completed histories in full**

Read the two source pages and two changelogs end to end. Re-open raw evidence for any statement whose platform equivalence, merchant implication, or parent-SDK ownership is unclear.

- [ ] **Step 2: Write the comparison**

Compare UI launch/result models, authorization, nonce/server handoff, cards, PayPal, Venmo, Apple Pay/Google Pay, 3D Secure, vaulted methods, parent SDK compatibility, migration/deprecation, browser/app switching, platform lifecycle, customization, and accessibility.

Every conclusion must identify one of: equivalent, platform-specific, delegated to parent SDK, documented but not execution-proven, unsupported, or unresolved. State that Drop-in orchestrates payment-method selection and tokenization; server-side payment processing remains a separate integration responsibility.

- [ ] **Step 3: Update indexes and logs once**

Add the analysis to the Braintree and root indexes. Append one concise campaign entry to Braintree and root logs. Do not duplicate package history from the changelogs.

- [ ] **Step 4: Run final verification**

```bash
python3 scripts/validate_wiki.py \
  wiki/analyses/analysis-braintree-drop-in-ios-vs-android.md \
  wiki/sources/braintree/github/source-github-braintree-ios-drop-in.md \
  wiki/sources/braintree/github/changelog-github-braintree-ios-drop-in.md \
  wiki/sources/braintree/github/source-github-braintree-android-drop-in.md \
  wiki/sources/braintree/github/changelog-github-braintree-android-drop-in.md \
  wiki/braintree-index.md \
  wiki/braintree-log.md
python3 scripts/validate_github_collection.py
python3 -m unittest discover -s tests
git diff --check
git status --short
```

Expected: all deterministic checks pass, both work items are `ingested`, and no unrelated file is staged.

- [ ] **Step 5: Commit the analysis and report the next step**

```bash
git add \
  wiki/analyses/analysis-braintree-drop-in-ios-vs-android.md \
  wiki/braintree-index.md wiki/braintree-log.md wiki/index.md wiki/log.md
git commit -m "Compare Braintree mobile Drop-in integrations"
```

Report commits, test counts, exact package/SHA baselines, ingest states, evidence gaps, and whether the branch is pushed. The next operational step is to run the normal weekly discovery cycle and collect only newly discovered stable package releases for packet review.

# Adyen iOS Stable Baseline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable `Adyen/adyen-ios` and collect a validated, source-rich `adyen-ios@5.25.1` baseline that stops at `awaiting_approval` without editing wiki knowledge.

**Architecture:** Extend the existing human-maintained repository row with one package-qualified v5 track and one `tagged-tree-v1` capsule. Use source-bearing directory roots plus explicit module-root files to retain all 679 Swift files while omitting tests, generated docs, media, local credential configuration, and binaries. The existing collector publishes immutable raw evidence and a review packet, then enforces the approval gate.

**Tech Stack:** Python 3 standard library, `unittest`, TOML registry data, Git, existing GitHub collection scripts.

## Global Constraints

- Baseline identity is exactly `adyen-ios@5.25.1` at tag `5.25.1` and observed SHA `5f6779b31299e3067de3a5279a816f3b8d2fbdf3`.
- Stable v5 releases are eligible; prereleases, including `6.0.0-alpha.1`, are excluded.
- Use the existing `tagged-tree-v1` adapter; do not add an adapter, parser, or automatic wiki editor.
- The source capsule must contain all 630 SDK Swift files and 49 Demo Swift files observed at the pinned tag.
- Tests, fixtures, generated docs, media, localization assets, XCFramework binaries, and Demo `.xcconfig` credential files remain excluded.
- Collection must stop at `awaiting_approval`; do not approve or ingest the work item in this plan.
- Do not modify or stage `CLAUDE copy.md` or `tracking/ingest/metronome/metronome-campaign-10/`.

---

## File Map

- Modify `tracking/github/repo-registry.toml`: activate the existing Adyen iOS row and define its stable version and capsule policy.
- Modify `tests/test_github_registry.py`: update inventory truth and add exact Adyen iOS policy assertions.
- Generate `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/`: immutable exact-SHA source capsule.
- Generate `raw/github/adyen/adyen-ios/releases/adyen-ios/5.25.1/2026-08-01/`: immutable package release record.
- Generate `tracking/github/repos/adyen/adyen-ios/`: comparison, work-item, ingest-packet, and status evidence owned by the collector.
- Modify through generator only: `tracking/github/status.md` and `tracking/github/work-items.json`.
- Do not modify any file under `wiki/`.

---

### Task 1: Activate the Reviewed Adyen iOS Registry Policy

**Files:**
- Modify: `tests/test_github_registry.py:80-90`
- Modify: `tests/test_github_registry.py:819-910`
- Modify: `tracking/github/repo-registry.toml:1224-1233`

**Interfaces:**
- Consumes: `github_registry.load_registry(path) -> Tuple[RepoConfig, ...]`, `VersionTrack`, and the existing `tagged-tree-v1` capsule schema.
- Produces: one enabled `RepoConfig` for `adyen/adyen-ios` with package selector `package:adyen-ios@5` and capsule ID `adyen-ios-public-source`.

- [ ] **Step 1: Change the expected inventory row and add a failing policy test**

In `APPENDIX_A_INVENTORY`, change only the Adyen iOS enabled value from `False` to `True`:

```python
('adyen/adyen-ios', 'https://github.com/Adyen/adyen-ios', 'mobile-sdk', 'tier1', 'semver-tags', True, 'releases-and-default-branch', 'weekly'),
```

Add a dedicated test after `test_adyen_web_uses_the_reviewed_bounded_public_source_capsule`:

```python
def test_adyen_ios_uses_the_reviewed_complete_swift_source_capsule(self):
    repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
    repo = next(item for item in repos if item.id == "adyen/adyen-ios")

    self.assertTrue(repo.enabled)
    self.assertEqual(
        (
            VersionTrack(
                "package:adyen-ios@5",
                "latest-stable",
                "all-stable",
                False,
                ("5.25.1",),
            ),
        ),
        repo.version_tracks,
    )
    self.assertEqual(1, len(repo.capsules))
    capsule = repo.capsules[0]
    self.assertEqual("adyen-ios-public-source", capsule.id)
    self.assertEqual("tagged-tree-v1", capsule.adapter)
    self.assertEqual(("adyen-ios",), capsule.focus_packages)
    self.assertEqual("configured-repository-paths", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(56, len(capsule.default_required_roots))
    self.assertEqual(38, len(capsule.include_paths))
    self.assertEqual((), capsule.default_generated_target_paths)
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual(512000, capsule.max_file_bytes)
    self.assertEqual(750, capsule.max_capsule_files)
    self.assertEqual(4000000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(800, capsule.max_packet_files)
    self.assertEqual(5000000, capsule.max_packet_utf8_bytes)

    required = set(capsule.default_required_roots)
    includes = set(capsule.include_paths)
    self.assertTrue({
        "Adyen/Core",
        "AdyenActions/Components",
        "AdyenCard/Components",
        "AdyenComponents/Apple Pay",
        "AdyenDropIn/Components",
        "AdyenSession/API",
        "Demo/Common/IntegrationExamples",
    }.issubset(required))
    self.assertTrue({
        "Adyen/Assets/Generated/LocalizationKey.swift",
        "Demo/Configuration+secrets.swift",
        "Demo/Configuration.swift",
        "Package.swift",
        "MIGRATION.md",
    }.issubset(includes))
```

- [ ] **Step 2: Run the new test and confirm the registry is not operational yet**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_adyen_ios_uses_the_reviewed_complete_swift_source_capsule -v
```

Expected: FAIL because the row is disabled and has no version track or capsule.

- [ ] **Step 3: Replace the inventory-only Adyen iOS row with the reviewed runnable policy**

Keep the existing row identity fields and append this exact policy data before the next `[[repos]]` table:

```toml
enabled=true
repo_type="mobile-sdk"
priority="tier1"
track="releases-and-default-branch"
version_strategy="semver-tags"
[[repos.version_tracks]]
selector="package:adyen-ios@5"
backfill="latest-stable"
future="all-stable"
include_prerelease=false
pinned_versions=["5.25.1"]
[[repos.capsules]]
id="adyen-ios-public-source"
adapter="tagged-tree-v1"
focus_packages=["adyen-ios"]
dependency_scope="configured-repository-paths"
changed_path_policy="policy-bounded"
default_required_roots=[
  "Adyen/Analytics",
  "Adyen/Core",
  "Adyen/Formatters",
  "Adyen/Helpers",
  "Adyen/Model",
  "Adyen/UI",
  "Adyen/Utilities",
  "Adyen/Validators",
  "AdyenActions/Actions",
  "AdyenActions/Components",
  "AdyenActions/Protocols",
  "AdyenActions/UI",
  "AdyenActions/Utilities",
  "AdyenCard/Components",
  "AdyenCard/Form",
  "AdyenCard/Formatters",
  "AdyenCard/Utilities",
  "AdyenCard/Validators",
  "AdyenCardScanner/Sources",
  "AdyenCashAppPay/CashAppPayButton",
  "AdyenComponents/ACH Direct Debit",
  "AdyenComponents/Affirm",
  "AdyenComponents/Apple Pay",
  "AdyenComponents/Atome",
  "AdyenComponents/BACS Direct Debit",
  "AdyenComponents/BLIK",
  "AdyenComponents/BasicPersonalInfoFormComponent",
  "AdyenComponents/Boleto",
  "AdyenComponents/Doku",
  "AdyenComponents/Instant",
  "AdyenComponents/Issuer List",
  "AdyenComponents/MB Way",
  "AdyenComponents/OnlineBanking",
  "AdyenComponents/PayByBank",
  "AdyenComponents/PayTo",
  "AdyenComponents/Qiwi Wallet",
  "AdyenComponents/SEPA Direct Debit",
  "AdyenComponents/UPI",
  "AdyenDropIn/Components",
  "AdyenDropIn/Models",
  "AdyenDropIn/Presentation",
  "AdyenDropIn/Utilities",
  "AdyenDropIn/Views",
  "AdyenEncryption/Extensions",
  "AdyenEncryption/JOSE",
  "AdyenEncryption/Model",
  "AdyenEncryption/Payload",
  "AdyenSession/API",
  "AdyenSwiftUI/Present View Controller",
  "AdyenWeChatPay/WeChatPayActionComponent",
  "Demo/Common/Configuration",
  "Demo/Common/Helpers",
  "Demo/Common/IntegrationExamples",
  "Demo/Common/Models",
  "Demo/Common/Networking",
  "Demo/Common/PresentationDelegates",
]
default_generated_target_paths=[]
include_paths=[
  "README.md",
  "MIGRATION.md",
  "Package.swift",
  "Adyen.podspec",
  "Cartfile",
  "LICENSE",
  "Adyen/PrivacyInfo.xcprivacy",
  "Adyen/Assets/Generated/LocalizationKey.swift",
  "AdyenActions/AdyenActionComponent.swift",
  "AdyenCashAppPay/CashAppPayComponent.swift",
  "AdyenCashAppPay/CashAppPayConfiguration.swift",
  "AdyenCashAppPay/CashAppPayDetails.swift",
  "AdyenDelegatedAuthentication/AdyenDelegatedAuthentication.swift",
  "AdyenDropIn/DropInComponent.swift",
  "AdyenDropIn/DropInComponentExtensions.swift",
  "AdyenEncryption/AnyEncryptor.swift",
  "AdyenEncryption/BankDetailsEncryptor.swift",
  "AdyenEncryption/CardEncryptor.swift",
  "AdyenSession/AdyenSession+ActionComponentDelegate.swift",
  "AdyenSession/AdyenSession+DropInComponentDelegate.swift",
  "AdyenSession/AdyenSession+PartialPaymentDelegate.swift",
  "AdyenSession/AdyenSession+PaymentComponentDelegate.swift",
  "AdyenSession/AdyenSession+StoredPaymentMethodsDelegate.swift",
  "AdyenSession/AdyenSession.swift",
  "AdyenSession/AdyenSessionDelegate.swift",
  "AdyenSession/AdyenSessionResult.swift",
  "AdyenTwint/TwintComponent.swift",
  "AdyenTwint/TwintDetails.swift",
  "Demo/Configuration+secrets.swift",
  "Demo/Configuration.swift",
  "Demo/SwiftUI/AppDelegate.swift",
  "Demo/SwiftUI/ComponentsView.swift",
  "Demo/SwiftUI/ComponentsViewModel.swift",
  "Demo/SwiftUI/SceneDelegate.swift",
  "Demo/UIKit/AppDelegate.swift",
  "Demo/UIKit/ComponentsView.swift",
  "Demo/UIKit/ComponentsViewController.swift",
  "Demo/UIKit/UIView+Helpers.swift",
]
excluded_categories=["tests", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=512000
max_capsule_files=750
max_capsule_utf8_bytes=4000000
max_packet_files=800
max_packet_utf8_bytes=5000000
```

- [ ] **Step 4: Add Adyen iOS to the shared native-profile matrix without imposing the smaller native budgets**

Do not add Adyen iOS to `test_native_sdks_use_tagged_tree_profiles`, because that matrix currently asserts uniform 500-file and 5 MB capsule budgets. The dedicated test above owns Adyen's larger reviewed budgets. Leave the shared test unchanged.

- [ ] **Step 5: Run the focused registry tests**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_adyen_ios_uses_the_reviewed_complete_swift_source_capsule tests.test_github_registry.RegistryTests.test_registry_matches_appendix_a_inventory_and_collection_cadence -v
```

Expected: both tests PASS.

- [ ] **Step 6: Run the complete offline registry and tagged-tree test set**

Run:

```bash
python3 -m unittest tests.test_github_registry tests.test_github_tagged_tree tests.test_github_capsule_selection tests.test_collect_github_repos -v
```

Expected: all tests PASS with no network access.

- [ ] **Step 7: Run the offline collection validator before generating evidence**

Run:

```bash
python3 scripts/validate_github_collection.py
```

Expected: PASS for all pre-existing evidence and the new registry policy. No Adyen iOS raw or tracking output exists yet.

- [ ] **Step 8: Commit the registry policy and tests**

```bash
git add tracking/github/repo-registry.toml tests/test_github_registry.py
git diff --cached --check
git commit -m "feat: enable Adyen iOS collection"
```

Expected: the commit contains exactly the registry and registry-test changes.

---

### Task 2: Collect and Validate the Stable Baseline

**Files:**
- Generate: `raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/`
- Generate: `raw/github/adyen/adyen-ios/releases/adyen-ios/5.25.1/2026-08-01/`
- Generate: `tracking/github/repos/adyen/adyen-ios/`
- Modify through generator only: canonical files under `tracking/github/` reported by `git status`
- Must not modify: `wiki/`

**Interfaces:**
- Consumes: the enabled `RepoConfig`, official Git tag `5.25.1`, GitHub release notes, and existing collector retry/secret/budget protections.
- Produces: one exact-SHA snapshot, one package-qualified release record, one baseline work item, and one canonical ingest packet in `awaiting_approval`.

- [ ] **Step 1: Confirm clean task-owned state before network collection**

Run:

```bash
git status --short --branch
```

Expected: `main` contains the committed registry policy; only the known unrelated `CLAUDE copy.md` and `tracking/ingest/metronome/metronome-campaign-10/` paths may remain untracked.

- [ ] **Step 2: Collect the reviewed stable baseline**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo adyen/adyen-ios --mode backfill
```

Expected:

- the selected release is exactly `adyen-ios@5.25.1`;
- the resolved SHA is `5f6779b31299e3067de3a5279a816f3b8d2fbdf3`;
- the snapshot contains exactly 679 SDK/Demo Swift source files and the seven reviewed metadata/privacy files, for 686 retained files total; `Package.swift` is one of the seven metadata files and must not be double-counted as SDK/Demo source;
- no test, generated documentation, image, localization, `.xcconfig`, or XCFramework path is retained; and
- the work item stops at `awaiting_approval`.

If the tag SHA differs, a secret finding is reported, or the expected source count differs, stop and move the item to manual review. Do not weaken the policy or add a secret allowlist without a separate evidence review.

- [ ] **Step 3: Read the generated status and both review-packet representations**

Run:

```bash
python3 scripts/collect_github_repos.py status
```

Use the packet paths printed by `status`. Read `packet.json` and `packet.md` completely. Confirm package identity, release, SHA, baseline/full recommendation, required-reading list, evidence-gap count, unclassified-change count, and excluded-path dispositions agree.

Expected: one Adyen iOS item is `awaiting_approval`; no item is `approved` or `ingesting`.

- [ ] **Step 4: Verify the immutable snapshot manifest and selected path boundary**

Run:

```bash
python3 -c 'import json, pathlib; p=pathlib.Path("raw/github/adyen/adyen-ios/snapshots/2026-08-01-5f6779b/manifest.json"); d=json.loads(p.read_text()); paths=[row["path"] for row in d["files"]]; source_swift=[x for x in paths if x.endswith(".swift") and x!="Package.swift"]; blocked=("Tests/", "AdyenCardScannerTests/", "docs/", "Adyen.docc/", "XCFramework/"); assert d["sha"]=="5f6779b31299e3067de3a5279a816f3b8d2fbdf3"; assert len(paths)==686, len(paths); assert len(source_swift)==679, len(source_swift); assert not any(x.startswith(blocked) or x.endswith((".png", ".jpg", ".pdf", ".xcconfig")) for x in paths); print(len(paths), len(source_swift), d["sha"])'
```

Expected output begins with `686 679 5f6779b31299e3067de3a5279a816f3b8d2fbdf3`.

- [ ] **Step 5: Run deterministic collection validation**

Run:

```bash
python3 scripts/validate_github_collection.py
```

Expected: PASS, including snapshot hashes, release linkage, packet hash, work-item state, and generated status equality.

- [ ] **Step 6: Prove collection did not edit wiki knowledge**

Run:

```bash
git status --short
git diff --name-only -- wiki
```

Expected: the second command prints nothing. The first command lists only Adyen iOS raw/tracking outputs plus the known unrelated untracked paths.

- [ ] **Step 7: Commit only validated collection evidence**

Stage the exact Adyen iOS raw and tracking paths plus collector-generated global status files shown by `git status`; do not use `git add .`:

```bash
git add raw/github/adyen/adyen-ios tracking/github/repos/adyen/adyen-ios tracking/github/status.md tracking/github/work-items.json
git diff --cached --check
git commit -m "data: collect Adyen iOS 5.25.1 baseline"
```

Confirm the staged diff contains no `wiki/`, `CLAUDE copy.md`, or Metronome campaign path before committing.

- [ ] **Step 8: Report the approval packet and stop**

Report:

- package-qualified release and exact SHA;
- retained file and byte counts;
- evidence-gap and unclassified-change counts;
- recommended ingest mode and priority;
- snapshot, release record, and packet paths;
- test and validator results; and
- the next step: user review and explicit approval of this single work item.

Do not run `approve`, `next-ingest`, or edit any wiki page.

---

## Plan Completion Check

Before declaring execution complete:

- confirm both task commits exist;
- confirm `python3 scripts/validate_github_collection.py` passes;
- confirm the Adyen iOS item remains `awaiting_approval`;
- confirm no task-owned session is still running;
- confirm no wiki file changed; and
- leave the unrelated untracked files untouched.

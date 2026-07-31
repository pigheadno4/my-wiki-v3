# Tagged Native GitHub Collection Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a reusable `tagged-tree-v1` GitHub source-capsule adapter and use it to collect bounded, immutable evidence for `stripe/stripe-ios@26.4.1` and `stripe/stripe-android@23.13.1`.

**Architecture:** Keep the existing NPM resolver unchanged behind an adapter dispatcher. The new adapter creates one synthetic root package from an exact tagged tree, then reuses the existing path selection, secret scanning, hashing, budgets, snapshot, comparison, packet, retry, and approval lifecycle. Repository-specific paths remain data in `tracking/github/repo-registry.toml`.

**Tech Stack:** Python 3 standard library, `unittest`, Git CLI, TOML registry, existing GitHub collection scripts.

## Global Constraints

- Read `CLAUDE.md` and `rules/github-repos.md` before each implementation session.
- Follow test-driven development: add one failing test, run it, make the smallest implementation change, and rerun it.
- Do not change the output or behavior of `npm-tracked-source-v1`.
- Do not execute Swift, CocoaPods, Gradle, Kotlin, or Android builds.
- Do not mirror either repository or retain complete test, fixture, snapshot, or generated-output trees.
- Do not create a fake `package.json` for a native repository.
- Do not edit wiki knowledge pages or approve/start ingest.
- Keep each capsule at or below 500 files and 5,000,000 UTF-8 bytes.
- Keep each packet at or below 550 files and 6,000,000 UTF-8 bytes.
- Return to policy review if required reading exceeds 450 files.
- Collect and validate iOS before starting the Android network collection.
- Stop both pilot work items in `awaiting_approval`.
- Leave unrelated files, including `CLAUDE copy.md`, untouched.

---

## Task 1: Make Capsule Policy Adapter-Aware

**Files:**
- Modify: `scripts/github_capsule_policy.py`
- Modify: `scripts/github_npm_workspace.py`
- Modify: `tests/test_github_capsule_policy.py`
- Modify: `tests/test_github_registry.py`

- [ ] **Step 1: Add failing policy tests**

Add tests proving:

```python
def test_tagged_tree_policy_uses_tagged_schema_and_hashes_it(self):
    capsule = CapsuleConfig(
        id="stripe-ios-source",
        adapter="tagged-tree-v1",
        focus_packages=("stripe-ios",),
        dependency_scope="configured-repository-paths",
        changed_path_policy="policy-bounded",
        default_required_roots=("StripePayments/StripePayments/Source/API Bindings",),
    )
    policy = build_effective_policy(capsule, (), (), ())
    payload = json.loads(policy.canonical_bytes)
    self.assertEqual("single-tagged-tree-v1", payload["workspace_resolver"])
    self.assertEqual("configured-repository-paths", payload["dependency_scope"])

def test_tagged_tree_policy_requires_one_focus_identity(self):
    with self.assertRaisesRegex(ValueError, "exactly one focus package"):
        build_effective_policy(
            CapsuleConfig(
                id="invalid",
                adapter="tagged-tree-v1",
                focus_packages=("stripe-ios", "stripe-android"),
                dependency_scope="configured-repository-paths",
            ),
            (),
            (),
            (),
        )
```

Also preserve the existing canonical-byte assertion for `npm-tracked-source-v1`.

- [ ] **Step 2: Run the focused tests and confirm failure**

Run:

```bash
python3 -m unittest tests.test_github_capsule_policy tests.test_github_registry
```

Expected: the tagged adapter is rejected while all existing NPM assertions still pass up to that rejection.

- [ ] **Step 3: Add explicit adapter contracts**

In `scripts/github_capsule_policy.py`, introduce:

```python
NPM_CAPSULE_ADAPTER = "npm-tracked-source-v1"
TAGGED_TREE_ADAPTER = "tagged-tree-v1"
CAPSULE_ADAPTERS = frozenset((NPM_CAPSULE_ADAPTER, TAGGED_TREE_ADAPTER))

NPM_DEPENDENCY_SCOPE = "internal-runtime-closure"
TAGGED_TREE_DEPENDENCY_SCOPE = "configured-repository-paths"

WORKSPACE_RESOLVERS = {
    NPM_CAPSULE_ADAPTER: "npm-workspaces-v1",
    TAGGED_TREE_ADAPTER: "single-tagged-tree-v1",
}
```

Retain `CAPSULE_ADAPTER = NPM_CAPSULE_ADAPTER` only as a temporary compatibility alias while call sites are migrated in later tasks. Normalize `dependency_scope`, focus-package count, and `workspace_resolver` by adapter. Continue validating release identities with the existing package-name-safe syntax.

Update `scripts/github_npm_workspace.py` to compare explicitly with `NPM_CAPSULE_ADAPTER`.

- [ ] **Step 4: Run focused and registry tests**

Run:

```bash
python3 -m unittest tests.test_github_capsule_policy tests.test_github_registry tests.test_github_npm_workspace
```

Expected: all pass, including byte-identical NPM policy payloads.

- [ ] **Step 5: Commit**

```bash
git add scripts/github_capsule_policy.py scripts/github_npm_workspace.py tests/test_github_capsule_policy.py tests/test_github_registry.py
git commit -m "feat: add tagged tree capsule policy"
```

---

## Task 2: Resolve And Select A Tagged Repository Tree

**Files:**
- Create: `scripts/github_tagged_tree.py`
- Modify: `scripts/github_capsule_selection.py`
- Create: `tests/test_github_tagged_tree.py`
- Modify: `tests/test_github_capsule_selection.py`

- [ ] **Step 1: Add failing synthetic-workspace tests**

Use `tests.github_test_support` to build a temporary Git repository containing Swift, Kotlin, examples, tests, build files, and a token-shaped secret. Test the public interface `resolve_tagged_workspace(tree: GitTree, capsule: CapsuleConfig, versions: Mapping[str, str]) -> WorkspaceResolution`.

Assert that the result contains exactly one `WorkspacePackage` with:

```python
WorkspacePackage(
    name="stripe-ios",
    path="",
    version="26.4.1",
    reason="focus",
    owned_paths=(
        "CHANGELOG.md",
        "Package.swift",
        "StripePaymentSheet/Source/PaymentSheet.swift",
    ),
)
```

The exact `owned_paths` must be sorted, tracked blobs selected by configured roots/includes. Dependency edges, external dependencies, and declared targets must be empty. Missing or extra version-map identities and missing required paths must fail closed.

- [ ] **Step 2: Run the new tests and confirm import failure**

Run:

```bash
python3 -m unittest tests.test_github_tagged_tree
```

Expected: failure because `github_tagged_tree.py` does not exist.

- [ ] **Step 3: Implement the synthetic tagged workspace**

Implement `resolve_tagged_workspace` without parsing language or build files. It must:

- require `TAGGED_TREE_ADAPTER`;
- require exactly one focus identity and one matching supplied version;
- inspect only tracked regular blobs;
- expand configured roots and literal includes deterministically;
- reject missing required roots/includes;
- apply no NPM workspace, dependency, or export logic; and
- return sorted immutable tuples.

- [ ] **Step 4: Add failing adapter-dispatch tests**

In `tests/test_github_capsule_selection.py`, test these new interfaces:

- `resolve_capsule_workspace(tree: GitTree, capsule: CapsuleConfig, versions: Mapping[str, str]) -> WorkspaceResolution`
- `resolve_capsule(tree: GitTree, capsule: CapsuleConfig, allowlist: Sequence[SecretAllowlist], changed_paths: Sequence[str] = (), versions: Mapping[str, str] | None = None) -> CapsuleResolution`

Prove that tagged selection:

- retains configured Swift/Kotlin source and selected examples;
- excludes `Tests`, `src/test`, `src/androidTest`, fixtures, and snapshots;
- keeps stories when `stories` is absent from `excluded_categories`;
- rejects unsafe paths, secrets, oversized files, and file/byte budget overflow;
- classifies changed paths only inside configured roots/includes; and
- produces a policy hash bound to `tagged-tree-v1`.

Retain direct `resolve_npm_capsule` tests as NPM regression coverage.

- [ ] **Step 5: Implement adapter dispatch and shared tagged selection**

Add `resolve_capsule_workspace` and `resolve_capsule` to `scripts/github_capsule_selection.py`. Dispatch NPM calls to the existing functions. For tagged trees, reuse the existing blob loading, category classifier, secret scanner, allowlist, hashing, and budget enforcement, but skip package manifests, tracked JavaScript targets, and NPM package overrides.

Every selected tagged file must use the configured focus identity as `CapsuleFile.package`.

- [ ] **Step 6: Run selection tests**

Run:

```bash
python3 -m unittest tests.test_github_tagged_tree tests.test_github_capsule_selection tests.test_github_npm_workspace
```

Expected: all pass.

- [ ] **Step 7: Commit**

```bash
git add scripts/github_tagged_tree.py scripts/github_capsule_selection.py tests/test_github_tagged_tree.py tests/test_github_capsule_selection.py
git commit -m "feat: resolve tagged repository capsules"
```

---

## Task 3: Route Collection And Comparison Through The Adapter

**Files:**
- Modify: `scripts/collect_github_repos.py`
- Modify: `tests/test_collect_github_repos.py`
- Modify: `tests/test_github_releases.py`

- [ ] **Step 1: Add failing collection tests**

Add a tagged fixture and mock remote resolution so `_prepare_group` receives:

```python
{"stripe-ios": "26.4.1"}
```

Assert that tagged collection:

- calls `resolve_capsule_workspace` and `resolve_capsule`;
- accepts plain tag `26.4.1` for `stripe-ios@26.4.1`;
- accepts `v23.13.1` for `stripe-android@23.13.1`;
- does not call package-manifest or public-export readers;
- emits empty dependency and export changes; and
- computes comparison pathspecs from the synthetic package's configured `owned_paths`.

Add an NPM regression assertion showing the existing package manifest and public export path still executes.

- [ ] **Step 2: Run the focused tests and confirm failure**

Run:

```bash
python3 -m unittest tests.test_collect_github_repos tests.test_github_releases
```

Expected: tagged collection fails at the current NPM-only calls.

- [ ] **Step 3: Replace direct NPM calls with dispatch**

Update every collection, preparation, and ad hoc comparison call site in `scripts/collect_github_repos.py` to use the adapter-dispatch functions.

In `_prepare_group`:

- pass `{candidate.package: candidate.version}` for a tagged release;
- retain exact package-manifest version and public-export validation for NPM;
- use the release candidate identity/version for tagged trees;
- set tagged dependency/public-export changes to empty/false; and
- leave snapshot publication, release records, comparisons, work items, retries, and approval transitions unchanged.

- [ ] **Step 4: Run collection and release tests**

Run:

```bash
python3 -m unittest tests.test_collect_github_repos tests.test_github_releases tests.test_github_git tests.test_github_work_items
```

Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add scripts/collect_github_repos.py tests/test_collect_github_repos.py tests/test_github_releases.py
git commit -m "feat: dispatch github collection by capsule adapter"
```

---

## Task 4: Build And Validate Native Review Packets

**Files:**
- Modify: `scripts/github_ingest_packets.py`
- Modify: `scripts/github_validation.py`
- Modify: `tests/test_github_ingest_packets.py`
- Modify: `tests/test_github_validation.py`

- [ ] **Step 1: Add failing packet tests**

Build a tagged snapshot fixture without `package.json`. Assert that:

- `_validate_config` accepts both adapters;
- the tagged package root is `""`;
- release identity and version come from the release manifest;
- dependency and public API change sections are empty;
- configured required roots/includes are required reading;
- `package.json` is not implicitly required;
- hard packet limits still fail closed; and
- the NPM fixture's packet JSON remains unchanged.

- [ ] **Step 2: Run packet tests and confirm failure**

Run:

```bash
python3 -m unittest tests.test_github_ingest_packets tests.test_github_validation
```

Expected: the tagged fixture is rejected for missing `package.json` or unsupported adapter.

- [ ] **Step 3: Add adapter-specific package metadata**

Update `scripts/github_ingest_packets.py` so:

- NPM retains `_package_manifest`, dependency diff, and public API diff behavior;
- tagged trees derive one root package from the capsule and release manifest;
- `_package_roots` returns `("",)` for tagged trees;
- `_required_by_policy` does not add `package.json` for tagged trees; and
- no synthetic file is written to raw evidence.

Update validation only where an invariant currently assumes NPM. Preserve immutable hashes, release linkage, package-qualified identity checks, packet limits, and queue-state rules.

- [ ] **Step 4: Run packet and lifecycle tests**

Run:

```bash
python3 -m unittest tests.test_github_ingest_packets tests.test_github_validation tests.test_github_work_items
```

Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add scripts/github_ingest_packets.py scripts/github_validation.py tests/test_github_ingest_packets.py tests/test_github_validation.py
git commit -m "feat: support tagged tree ingest packets"
```

---

## Task 5: Configure The Stripe iOS And Android Capsules

**Files:**
- Modify: `tracking/github/repo-registry.toml`
- Modify: `tests/test_github_registry.py`
- Modify: `rules/github-repos.md`

- [ ] **Step 1: Add failing registry assertions**

Assert exact tracks:

```text
package:stripe-ios@26       pinned 26.4.1
package:stripe-android@23   pinned 23.13.1
```

Assert both rows are enabled, use `tagged-tree-v1`, use `configured-repository-paths`, enforce `policy-bounded`, and use the approved 500/5 MB snapshot and 550/6 MB packet limits.

- [ ] **Step 2: Run registry tests and confirm failure**

Run:

```bash
python3 -m unittest tests.test_github_registry
```

Expected: both rows are disabled and lack runnable policies.

- [ ] **Step 3: Configure Stripe iOS**

Use required roots for bounded maintained source, including:

```text
StripePayments/StripePayments/Source/API Bindings
StripePayments/StripePayments/Source/PaymentHandler
StripeApplePay/StripeApplePay/Source/ApplePayContext
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/CustomerSheet
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Link
```

Use literal includes for:

```text
README.md
CHANGELOG.md
MIGRATING.md
LICENSE
VERSION
Package.swift
modules.yaml
StripePayments.podspec
StripePaymentSheet.podspec
StripeApplePay.podspec
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet.swift
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+API.swift
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+DeferredAPI.swift
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+CheckoutSessionAPI.swift
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheet+SwiftUI.swift
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetConfiguration.swift
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetAppearance.swift
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetError.swift
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetFlowController.swift
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentSheetFlowController+AsyncPublicAPIs.swift
StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/PaymentElementConfiguration.swift
Example/PaymentSheet Example/PaymentSheet Example/ExampleCheckoutViewController.swift
Example/PaymentSheet Example/PaymentSheet Example/ExampleEmbeddedElementCheckoutViewController.swift
Example/PaymentSheet Example/PaymentSheet Example/ExampleSwiftUIPaymentSheet.swift
Example/Non-Card Payment Examples/Non-Card Payment Examples/USBankAccountExampleViewController.swift
```

Add the reviewed public entrypoint and distribution files for Connect, Identity, Financial Connections, Issuing, and crypto onramp as literal includes. Do not broaden those frameworks to full source roots.

- [ ] **Step 4: Configure Stripe Android**

Use narrow source roots:

```text
paymentsheet-example/src/main/java/com/stripe/android/paymentsheet/example/samples/ui/paymentsheet/complete_flow
paymentsheet-example/src/main/java/com/stripe/android/paymentsheet/example/samples/ui/paymentsheet/custom_flow
paymentsheet-example/src/main/java/com/stripe/android/paymentsheet/example/playground/embedded
```

Use literal includes for:

```text
README.md
CHANGELOG.md
MIGRATING.md
LICENSE
VERSION
settings.gradle
build.gradle
dependencies.gradle
gradle.properties
paymentsheet/build.gradle
payments-core/build.gradle
connect/build.gradle
crypto-onramp/build.gradle
paymentsheet/api/paymentsheet.api
payments-core/api/payments-core.api
connect/api/connect.api
crypto-onramp/api/crypto-onramp.api
paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheet.kt
paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheetContract.kt
paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheetLauncher.kt
paymentsheet/src/main/java/com/stripe/android/paymentsheet/PaymentSheetResult.kt
payments-core/src/main/java/com/stripe/android/Stripe.kt
payments-core/src/main/java/com/stripe/android/PaymentIntentResult.kt
payments-core/src/main/java/com/stripe/android/SetupIntentResult.kt
payments-core/src/main/java/com/stripe/android/googlepaylauncher/GooglePayLauncher.kt
payments-core/src/main/java/com/stripe/android/payments/paymentlauncher/PaymentLauncher.kt
stripe-core/src/main/java/com/stripe/android/core/exception/StripeException.kt
```

Add reviewed API signatures, module build declarations, and principal entrypoints for Identity, Financial Connections, card scan, payment-method messaging, and other specialized modules. Do not include whole module implementations.

- [ ] **Step 5: Document the reusable adapter profile**

In `rules/github-repos.md`, add a concise `tagged-tree-v1` section that states:

- one semantic tag maps to one package-qualified release identity;
- paths are registry policy, not adapter code;
- no language/build parser runs;
- no fake package manifest is created;
- the capsule is bounded evidence, not a repository mirror; and
- query-specific missing implementation uses immutable supplements.

- [ ] **Step 6: Run registry and policy tests**

Run:

```bash
python3 -m unittest tests.test_github_registry tests.test_github_capsule_policy
python3 scripts/validate_github_collection.py
```

Expected: all pass before network collection.

- [ ] **Step 7: Commit**

```bash
git add tracking/github/repo-registry.toml tests/test_github_registry.py rules/github-repos.md
git commit -m "config: enable stripe native sdk capsules"
```

---

## Task 6: Run Offline Regression And Collect Stripe iOS

**Files:**
- Test: `tests/test_github_*.py`
- Generate: `raw/github/stripe/stripe-ios/**`
- Generate: `tracking/github/repos/stripe/stripe-ios/**`
- Generate: `tracking/github/state.json`

- [ ] **Step 1: Run the complete offline GitHub suite**

Run:

```bash
python3 -m unittest discover -s tests -p 'test_github_*.py'
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all tests and validation pass before network access.

- [ ] **Step 2: Dry-run the exact iOS release**

Run:

```bash
python3 scripts/collect_github_repos.py collect \
  --repo stripe/stripe-ios \
  --release stripe-ios@26.4.1 \
  --dry-run
```

Confirm the resolved tag is `26.4.1` and SHA is `e61afc0e1677560f6d1238411e74b85e1a54e15f`.

- [ ] **Step 3: Collect iOS**

Run:

```bash
python3 scripts/collect_github_repos.py collect \
  --repo stripe/stripe-ios \
  --release stripe-ios@26.4.1
```

- [ ] **Step 4: Validate the generated iOS evidence**

Run:

```bash
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py status
```

Inspect the snapshot manifest and both packet files. Confirm:

- state is `awaiting_approval`;
- no wiki file changed;
- snapshot has at most 500 files and 5,000,000 UTF-8 bytes;
- packet has at most 550 files and 6,000,000 UTF-8 bytes;
- required reading has at most 450 files;
- `Tests`, `StripePaymentsTestUtils`, fixtures, snapshots, and generated output are absent;
- no unclassified changes or blocking evidence gaps exist; and
- selected public API, Apple Pay, PaymentSheet, migration, build, and example evidence is present.

If any condition fails, stop. Revise the registry path policy with a failing fixture test and repeat Task 5 verification. Do not start Android collection.

- [ ] **Step 5: Commit only validated immutable iOS artifacts**

```bash
git add raw/github/stripe/stripe-ios tracking/github/repos/stripe/stripe-ios tracking/github/state.json
git commit -m "data: collect stripe ios 26.4.1"
```

---

## Task 7: Collect Stripe Android And Verify Both Pilots

**Files:**
- Generate: `raw/github/stripe/stripe-android/**`
- Generate: `tracking/github/repos/stripe/stripe-android/**`
- Modify: `tracking/github/state.json`

- [ ] **Step 1: Confirm iOS remains structurally valid**

Run:

```bash
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py status
```

Expected: the iOS item remains `awaiting_approval`.

- [ ] **Step 2: Dry-run the exact Android release**

Run:

```bash
python3 scripts/collect_github_repos.py collect \
  --repo stripe/stripe-android \
  --release stripe-android@23.13.1 \
  --dry-run
```

Confirm the resolved tag is `v23.13.1` and SHA is `db6e5112d67f6de4cb2e5048fbecd251d9f23d10`.

- [ ] **Step 3: Collect Android**

Run:

```bash
python3 scripts/collect_github_repos.py collect \
  --repo stripe/stripe-android \
  --release stripe-android@23.13.1
```

- [ ] **Step 4: Validate Android and compare both pilot packets**

Run:

```bash
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py status
python3 -m unittest discover -s tests -p 'test_github_*.py'
git diff --check
```

Inspect the Android snapshot manifest and packet files. Confirm the same limits and lifecycle conditions as iOS, plus:

- `src/test`, `src/androidTest`, test-support modules, screenshot trees, and generated docs are absent;
- public API signature files, PaymentSheet, direct payment, Google Pay, result/error, build, and example evidence are present; and
- both repository items remain separate and in `awaiting_approval`.

If Android fails, revise only the Android registry path policy with fixture coverage. Do not weaken shared limits or alter the accepted iOS artifacts.

- [ ] **Step 5: Commit only validated immutable Android artifacts**

```bash
git add raw/github/stripe/stripe-android tracking/github/repos/stripe/stripe-android tracking/github/state.json
git commit -m "data: collect stripe android 23.13.1"
```

- [ ] **Step 6: Final verification**

Run:

```bash
python3 scripts/validate_github_collection.py
python3 -m unittest discover -s tests -p 'test_github_*.py'
git status --short
```

Expected: validators pass; both pilot work items are `awaiting_approval`; no wiki source/changelog page has changed; only the unrelated pre-existing `CLAUDE copy.md` may remain untracked.

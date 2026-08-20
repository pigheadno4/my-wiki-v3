# Stripe CLI Checkout-Focused Capsule Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable `stripe/stripe-cli`, verify a bounded checkout-focused source capsule for `stripe-cli@1.50.0`, and publish one approval-gated baseline packet without ingesting it.

**Architecture:** Reuse the existing `tagged-tree-v1` adapter and release workflow. Registry policy selects bounded CLI command/runtime roots plus an exact list of checkout and recurring-payment trigger definitions; tests lock the policy, dry-run verifies tag identity without publication, and real collection publishes immutable evidence before stopping at `awaiting_approval`.

**Tech Stack:** Python 3 `unittest`, TOML registry configuration, existing GitHub collection CLI, Git, JSON/JQ, immutable Markdown/JSON evidence.

## Global Constraints

- Package identity is `stripe-cli@1`; initial pinned baseline is `stripe-cli@1.50.0`.
- Tag `v1.50.0` must resolve to exact commit `a6f40658b99e4142fd63b2e4b560aa9c7ae337b1` at collection time.
- Future stable v1 releases are retained; prereleases are excluded.
- Deep evidence is limited to CLI command wiring, credentials/configuration, requests, webhook listening/forwarding, event triggering, and the six approved checkout/recurring trigger families.
- The 40 selected trigger JSON files are runtime behavior and remain eligible despite the general fixture exclusion.
- Tests, canary suites, generated protobuf Go, generated resource commands, unrelated triggers, Terminal, plugins, agent tooling, samples, sandbox tooling, and distribution artifacts remain excluded.
- Per-file limit is 1,000,000 bytes; capsule limits are 180 files and 2,500,000 UTF-8 bytes; packet limits are 220 files and 3,200,000 UTF-8 bytes.
- Collection may publish raw and tracking evidence but must stop at `awaiting_approval`; do not approve, claim ingest, or edit `wiki/`.
- Leave unrelated `CLAUDE copy.md` untouched.

---

### Task 1: Enable and lock the Stripe CLI registry profile

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`

**Interfaces:**
- Consumes: `load_registry()`, `VersionTrack`, `CapsuleConfig`, and the existing `tagged-tree-v1` schema.
- Produces: one enabled `stripe/stripe-cli` policy with a package-qualified v1 track and one bounded checkout capsule.

- [ ] **Step 1: Add the failing registry contract test**

Change the `stripe/stripe-cli` inventory tuple's enabled value from `False` to `True`. Add this test to `RegistryTests`:

```python
def test_stripe_cli_uses_checkout_focused_tagged_profile(self):
    repos = {
        repo.id: repo
        for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
    }
    repo = repos["stripe/stripe-cli"]

    self.assertTrue(repo.enabled)
    self.assertEqual(
        (
            VersionTrack(
                "package:stripe-cli@1",
                "latest-stable",
                "all-stable",
                False,
                ("1.50.0",),
            ),
        ),
        repo.version_tracks,
    )
    self.assertEqual(1, len(repo.capsules))
    capsule = repo.capsules[0]
    self.assertEqual("stripe-cli-checkout-source", capsule.id)
    self.assertEqual("tagged-tree-v1", capsule.adapter)
    self.assertEqual(("stripe-cli",), capsule.focus_packages)
    self.assertEqual("configured-repository-paths", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(
        ("pkg/config", "pkg/login", "pkg/proxy", "pkg/requests", "pkg/stripe", "pkg/websocket"),
        capsule.default_required_roots,
    )
    self.assertEqual((), capsule.default_generated_target_paths)
    self.assertEqual(75, len(capsule.include_paths))
    self.assertIn("pkg/cmd/listen.go", capsule.include_paths)
    self.assertIn("pkg/cmd/trigger.go", capsule.include_paths)
    self.assertIn(
        "pkg/fixtures/triggers/checkout.session.completed.json",
        capsule.include_paths,
    )
    self.assertIn(
        "pkg/fixtures/triggers/payment_intent.succeeded.json",
        capsule.include_paths,
    )
    self.assertIn(
        "pkg/fixtures/triggers/customer.subscription.updated.json",
        capsule.include_paths,
    )
    self.assertIn(
        "pkg/fixtures/triggers/subscription_schedule.updated.json",
        capsule.include_paths,
    )
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual("text-secrets-v1", capsule.secret_detector)
    self.assertEqual(1000000, capsule.max_file_bytes)
    self.assertEqual(180, capsule.max_capsule_files)
    self.assertEqual(2500000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(220, capsule.max_packet_files)
    self.assertEqual(3200000, capsule.max_packet_utf8_bytes)
```

- [ ] **Step 2: Run the focused test and verify it fails**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_stripe_cli_uses_checkout_focused_tagged_profile
```

Expected: FAIL because the registry row is disabled and has no version track or capsule.

- [ ] **Step 3: Implement the approved registry policy**

Set `enabled=true`, add the exact version track and capsule fields below, and do not add a glob or directory-level trigger root.

The policy header and budgets must be exactly:

```toml
[[repos.version_tracks]]
selector="package:stripe-cli@1"
backfill="latest-stable"
future="all-stable"
include_prerelease=false
pinned_versions=["1.50.0"]
[[repos.capsules]]
id="stripe-cli-checkout-source"
adapter="tagged-tree-v1"
focus_packages=["stripe-cli"]
dependency_scope="configured-repository-paths"
changed_path_policy="policy-bounded"
default_required_roots=[
  "pkg/config",
  "pkg/login",
  "pkg/proxy",
  "pkg/requests",
  "pkg/stripe",
  "pkg/websocket",
]
default_generated_target_paths=[]
include_paths=[
  "README.md",
  "ARCHITECTURE.md",
  "LICENSE",
  "go.mod",
  "cmd/stripe/main.go",
  "pkg/cmd/root.go",
  "pkg/cmd/config.go",
  "pkg/cmd/login.go",
  "pkg/cmd/logout.go",
  "pkg/cmd/switch.go",
  "pkg/cmd/whoami.go",
  "pkg/cmd/get.go",
  "pkg/cmd/post.go",
  "pkg/cmd/delete.go",
  "pkg/cmd/http.go",
  "pkg/cmd/listen.go",
  "pkg/cmd/trigger.go",
  "pkg/cmd/fixtures.go",
  "pkg/cmd/resources.go",
  "pkg/fixtures/fixtures.go",
  "pkg/fixtures/triggers.go",
  "pkg/rpcservice/events_resend.go",
  "pkg/rpcservice/fixtures.go",
  "pkg/rpcservice/listen.go",
  "pkg/rpcservice/trigger.go",
  "pkg/rpcservice/triggers_list.go",
  "pkg/rpcservice/webhook_endpoint_create.go",
  "pkg/rpcservice/webhook_endpoints_list.go",
  "rpc/common.proto",
  "rpc/events_resend.proto",
  "rpc/fixtures.proto",
  "rpc/listen.proto",
  "rpc/trigger.proto",
  "rpc/triggers_list.proto",
  "rpc/webhook_endpoint_create.proto",
  "rpc/webhook_endpoints_list.proto",
  "pkg/fixtures/triggers/checkout.session.async_payment_failed.json",
  "pkg/fixtures/triggers/checkout.session.async_payment_succeeded.json",
  "pkg/fixtures/triggers/checkout.session.completed.json",
  "pkg/fixtures/triggers/checkout.session.expired.json",
  "pkg/fixtures/triggers/customer.subscription.created.json",
  "pkg/fixtures/triggers/customer.subscription.deleted.json",
  "pkg/fixtures/triggers/customer.subscription.paused.json",
  "pkg/fixtures/triggers/customer.subscription.trial_will_end.json",
  "pkg/fixtures/triggers/customer.subscription.updated.json",
  "pkg/fixtures/triggers/invoice.created.json",
  "pkg/fixtures/triggers/invoice.deleted.json",
  "pkg/fixtures/triggers/invoice.finalized.json",
  "pkg/fixtures/triggers/invoice.marked_uncollectible.json",
  "pkg/fixtures/triggers/invoice.paid.json",
  "pkg/fixtures/triggers/invoice.payment_action_required.json",
  "pkg/fixtures/triggers/invoice.payment_failed.json",
  "pkg/fixtures/triggers/invoice.sent.json",
  "pkg/fixtures/triggers/invoice.updated.json",
  "pkg/fixtures/triggers/invoice.voided.json",
  "pkg/fixtures/triggers/payment_intent.amount_capturable_updated.json",
  "pkg/fixtures/triggers/payment_intent.canceled.json",
  "pkg/fixtures/triggers/payment_intent.created.json",
  "pkg/fixtures/triggers/payment_intent.partially_funded.json",
  "pkg/fixtures/triggers/payment_intent.payment_failed.json",
  "pkg/fixtures/triggers/payment_intent.processing.json",
  "pkg/fixtures/triggers/payment_intent.requires_action.json",
  "pkg/fixtures/triggers/payment_intent.succeeded.json",
  "pkg/fixtures/triggers/setup_intent.canceled.json",
  "pkg/fixtures/triggers/setup_intent.created.json",
  "pkg/fixtures/triggers/setup_intent.requires_action.json",
  "pkg/fixtures/triggers/setup_intent.setup_failed.json",
  "pkg/fixtures/triggers/setup_intent.succeeded.json",
  "pkg/fixtures/triggers/subscription_schedule.aborted.json",
  "pkg/fixtures/triggers/subscription_schedule.canceled.json",
  "pkg/fixtures/triggers/subscription_schedule.completed.json",
  "pkg/fixtures/triggers/subscription_schedule.created.json",
  "pkg/fixtures/triggers/subscription_schedule.expiring.json",
  "pkg/fixtures/triggers/subscription_schedule.released.json",
  "pkg/fixtures/triggers/subscription_schedule.updated.json",
]
excluded_categories=["tests", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=1000000
max_capsule_files=180
max_capsule_utf8_bytes=2500000
max_packet_files=220
max_packet_utf8_bytes=3200000
```

- [ ] **Step 4: Run focused and registry regression tests**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_stripe_cli_uses_checkout_focused_tagged_profile
python3 -m unittest tests.test_github_registry tests.test_github_capsule_policy tests.test_github_capsule_selection
python3 scripts/validate_github_collection.py
```

Expected: all tests pass and the offline validator reports no structural errors.

- [ ] **Step 5: Review and commit only the registry policy**

Run:

```bash
git diff --check
git diff -- tests/test_github_registry.py tracking/github/repo-registry.toml
git status --short
git add tests/test_github_registry.py tracking/github/repo-registry.toml
git commit -m "Enable Stripe CLI collection"
```

Expected: the commit contains only the test and executable registry policy. `CLAUDE copy.md` remains untracked.

### Task 2: Verify the baseline without publishing evidence

**Files:**
- Read: `tracking/github/repo-registry.toml`
- Read: temporary clone and dry-run output only

**Interfaces:**
- Consumes: the committed Task 1 policy and `collect --mode backfill --dry-run`.
- Produces: verified tag identity plus exact capsule file/byte measurements; no raw, tracking, or wiki evidence.

- [ ] **Step 1: Record pre-run state**

Run:

```bash
git status --short
find raw/github/stripe/stripe-cli -type f
jq '[.work_items[] | select(.repo_id == "stripe/stripe-cli")] | length' tracking/github/work-items.json
```

Expected: the raw directory is absent, work-item count is `0`, and only `CLAUDE copy.md` is unrelated workspace state.

- [ ] **Step 2: Run dry collection**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo stripe/stripe-cli --mode backfill --dry-run
```

Expected: selection resolves only `stripe-cli@1.50.0`, tag `v1.50.0`, and exact commit `a6f40658b99e4142fd63b2e4b560aa9c7ae337b1`; nothing is published.

- [ ] **Step 3: Resolve the exact-tag capsule in temporary storage**

Create an exact-tag temporary clone:

```bash
git clone --filter=blob:none --no-checkout https://github.com/stripe/stripe-cli.git /private/tmp/stripe-cli-v1.50.0
git -C /private/tmp/stripe-cli-v1.50.0 fetch --depth 1 origin tag v1.50.0
```

Then run the existing resolver from the repository root:

```bash
PYTHONPATH=scripts python3 - /private/tmp/stripe-cli-v1.50.0 <<'PY'
import json
import subprocess
import sys
from pathlib import Path

from github_capsule_selection import resolve_capsule
from github_git_tree import GitTree
from github_registry import load_registry

root = Path.cwd()
clone = Path(sys.argv[1])
repo = next(
    item
    for item in load_registry(root / "tracking/github/repo-registry.toml")
    if item.id == "stripe/stripe-cli"
)
sha = subprocess.check_output(
    ["git", "rev-list", "-n", "1", "v1.50.0"],
    cwd=clone,
    text=True,
).strip()
resolution = resolve_capsule(
    GitTree(clone, sha, repo.max_file_bytes),
    repo.capsules[0],
    repo.secret_allowlist,
    versions={"stripe-cli": "1.50.0"},
)
print(json.dumps({
    "sha": sha,
    "selected_file_count": len(resolution.files),
    "selected_utf8_bytes": sum(item.size for item in resolution.files),
    "required_roots": resolution.required_roots,
    "secret_findings": len(resolution.secret_findings),
}, indent=2))
PY
```

Expected: no missing required path, unsafe path, secret finding, identity failure, or budget failure; selected files are at most `180` and UTF-8 bytes are at most `2500000`.

- [ ] **Step 4: Prove verification published nothing**

Repeat the Step 1 commands.

Expected: raw evidence and work-item count remain unchanged.

### Task 3: Publish and review the immutable Stripe CLI baseline

**Files:**
- Create under: `raw/github/stripe/stripe-cli/snapshots/`
- Create under: `raw/github/stripe/stripe-cli/releases/stripe-cli/1.50.0/`
- Create under: `tracking/github/repos/stripe/stripe-cli/ingest-packets/`
- Modify generated: `tracking/github/work-items.json`
- Modify generated: `tracking/github/status.md`
- Modify generated: `tracking/github/collection-index.json`
- Modify generated: `tracking/github/collection-index.md`

**Interfaces:**
- Consumes: verified Task 2 release identity and capsule measurements.
- Produces: one immutable snapshot, one package-qualified release record, one review packet, and one work item at `awaiting_approval`.

- [ ] **Step 1: Run real baseline collection**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo stripe/stripe-cli --mode backfill
```

Expected: collection publishes one exact-SHA evidence set and stops at `awaiting_approval`. Any identity, required-path, secret, unsafe-path, or budget failure blocks publication.

- [ ] **Step 2: Validate generated state**

Run:

```bash
python3 scripts/validate_github_collection.py
python3 -m unittest tests.test_github_registry tests.test_github_capsule_policy tests.test_github_capsule_selection tests.test_github_releases tests.test_collect_github_repos tests.test_github_ingest_packets tests.test_github_work_items
jq '.work_items[] | select(.repo_id == "stripe/stripe-cli") | {work_item_id,state,recommended_mode,approved_mode,sha,package_changes}' tracking/github/work-items.json
```

Expected: validation and tests pass; exactly one Stripe CLI work item recommends `full`, has no approved mode, and is `awaiting_approval`.

- [ ] **Step 3: Read and report the complete packet**

Read generated `packet.json` and `packet.md` in full. Report release identity, SHA, selected file count and bytes, required-reading count, unclassified changes, evidence gaps, and packet findings. Do not run `approve`, `next-ingest`, or edit `wiki/`.

- [ ] **Step 4: Commit the reviewed collection evidence**

After packet validation, stage only generated Stripe CLI raw/tracking evidence and generated global indexes/status, then commit:

```bash
git add raw/github/stripe/stripe-cli tracking/github/repos/stripe/stripe-cli tracking/github/work-items.json tracking/github/status.md tracking/github/collection-index.json tracking/github/collection-index.md tracking/github/artifacts.lock
git commit -m "Collect Stripe CLI baseline"
```

Expected: collection evidence is committed while the work item remains `awaiting_approval`; `CLAUDE copy.md` remains untouched.

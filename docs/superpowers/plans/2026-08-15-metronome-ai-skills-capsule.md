# Metronome AI Skills Capsule Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable `metronome-industries/ai`, verify its bounded AI skills and billing-scenario capsule, and publish one approval-gated exact-SHA baseline without ingesting it.

**Architecture:** Reuse the existing `commit-tree-v1` adapter and default-branch workflow. Registry policy selects the complete public `skills/` tree plus three explicitly approved dogfood scenarios and repository context; a focused test locks that policy, temporary resolution verifies selection and budgets, and real collection publishes immutable evidence before stopping at `awaiting_approval`.

**Tech Stack:** Python 3 `unittest`, TOML registry configuration, existing GitHub collection CLI, Git, JSON/JQ, immutable Markdown/JSON evidence.

## Global Constraints

- Repository identity is `metronome-industries/ai`; source identity is `metronome-ai`.
- Track the exact upstream default-branch SHA using `version_strategy = "commit"`; do not fabricate a package version or release record.
- Collect all tracked files under `skills/` plus `README.md`, `CONTRIBUTING.md`, `LICENSE`, and exactly three approved dogfood scenarios.
- Treat the three scenario files as story-style integration evidence, not executable-test or production-behavior authority.
- Exclude test runs, scorecards, test documentation, fixtures, and future ordinary test artifacts unless separately reviewed.
- Per-file limit is 512,000 bytes; capsule limits are 80 files and 1,000,000 UTF-8 bytes; packet limits are 100 files and 1,500,000 UTF-8 bytes.
- Collection may publish raw and tracking evidence but must stop at `awaiting_approval`; do not approve, claim ingest, or edit `wiki/`.
- Leave unrelated `CLAUDE copy.md` untouched.

---

### Task 1: Enable and lock the Metronome AI registry profile

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`

**Interfaces:**
- Consumes: `load_registry()` and the existing `CapsuleConfig` commit-tree schema.
- Produces: one enabled `metronome-industries/ai` registry policy with exactly one bounded `commit-tree-v1` capsule.

- [ ] **Step 1: Add the failing registry contract test**

Change the `metronome-industries/ai` inventory tuple's enabled value from `False` to `True`. Add this method to `RegistryTests`:

```python
def test_metronome_ai_uses_complete_skills_and_scenarios_profile(self):
    repos = {
        repo.id: repo
        for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
    }
    repo = repos["metronome-industries/ai"]

    self.assertTrue(repo.enabled)
    self.assertEqual("default-branch", repo.track)
    self.assertEqual("commit", repo.version_strategy)
    self.assertEqual((), repo.version_tracks)
    self.assertEqual(1, len(repo.capsules))
    capsule = repo.capsules[0]
    self.assertEqual("metronome-ai-skills", capsule.id)
    self.assertEqual("commit-tree-v1", capsule.adapter)
    self.assertEqual("metronome-ai", capsule.source_id)
    self.assertEqual("configured-repository-paths", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(("skills",), capsule.default_required_roots)
    self.assertEqual((), capsule.default_generated_target_paths)
    self.assertEqual(
        {
            "README.md",
            "CONTRIBUTING.md",
            "LICENSE",
            "tests/dogfood/scenarios/add-new-product-to-existing.md",
            "tests/dogfood/scenarios/change-pricing-raise-rate.md",
            "tests/dogfood/scenarios/start-billing-saas-with-credits.md",
        },
        set(capsule.include_paths),
    )
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual("text-secrets-v1", capsule.secret_detector)
    self.assertEqual(512000, capsule.max_file_bytes)
    self.assertEqual(80, capsule.max_capsule_files)
    self.assertEqual(1000000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(100, capsule.max_packet_files)
    self.assertEqual(1500000, capsule.max_packet_utf8_bytes)
```

- [ ] **Step 2: Run the focused test and verify it fails**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_metronome_ai_uses_complete_skills_and_scenarios_profile
```

Expected: FAIL because the registry row is disabled and has no capsule.

- [ ] **Step 3: Implement the approved registry policy**

Set `enabled=true` and add this exact capsule below the existing repository fields:

```toml
[[repos.capsules]]
id="metronome-ai-skills"
adapter="commit-tree-v1"
source_id="metronome-ai"
dependency_scope="configured-repository-paths"
changed_path_policy="policy-bounded"
default_required_roots=["skills"]
default_generated_target_paths=[]
include_paths=[
  "README.md",
  "CONTRIBUTING.md",
  "LICENSE",
  "tests/dogfood/scenarios/add-new-product-to-existing.md",
  "tests/dogfood/scenarios/change-pricing-raise-rate.md",
  "tests/dogfood/scenarios/start-billing-saas-with-credits.md",
]
excluded_categories=["tests", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=512000
max_capsule_files=80
max_capsule_utf8_bytes=1000000
max_packet_files=100
max_packet_utf8_bytes=1500000
```

- [ ] **Step 4: Run focused and registry regression tests**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_metronome_ai_uses_complete_skills_and_scenarios_profile
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
git commit -m "Enable Metronome AI collection"
```

Expected: the commit contains only the test and executable registry policy. `CLAUDE copy.md` remains untracked.

### Task 2: Verify the default-branch capsule without publication

**Files:**
- Read: `tracking/github/repo-registry.toml`
- Read: temporary clone and dry-run output only

**Interfaces:**
- Consumes: the committed Task 1 registry policy and `collect --mode backfill --dry-run`.
- Produces: one verified live default-branch identity and exact capsule measurements; no raw, tracking, or wiki evidence.

- [ ] **Step 1: Record pre-run state**

Run:

```bash
git status --short
find raw/github/metronome/ai -type f 2>/dev/null
jq '[.work_items[] | select(.repo_id == "metronome-industries/ai")] | length' tracking/github/work-items.json
```

Expected: the raw directory is absent, work-item count is `0`, and only `CLAUDE copy.md` is unrelated workspace state.

- [ ] **Step 2: Run dry collection**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo metronome-industries/ai --mode backfill --dry-run
```

Expected: one default-branch baseline candidate is resolved and nothing is published. At design time, `main` resolved to `59193aabd9c43cca32f320d6f68f5d63d04034d4`; if the live SHA differs, report it and continue only after the selected evidence passes the same policy.

- [ ] **Step 3: Resolve and measure the exact live capsule in temporary storage**

Create a unique temporary clone and resolve its checked-out default-branch SHA:

```bash
clone_root=$(mktemp -d /private/tmp/metronome-ai-baseline.XXXXXX)
git clone --filter=blob:none --depth=1 https://github.com/Metronome-Industries/ai "$clone_root/repository"
sha=$(git -C "$clone_root/repository" rev-parse HEAD)
printf '%s\n' "$clone_root" "$sha"
```

Then run the existing resolver from the repository root:

```bash
PYTHONPATH=scripts python3 - "$clone_root/repository" "$sha" <<'PY'
import json
import sys
from pathlib import Path

from github_capsule_selection import resolve_capsule
from github_git_tree import GitTree
from github_registry import load_registry

root = Path.cwd()
clone = Path(sys.argv[1])
sha = sys.argv[2]
repo = next(
    item
    for item in load_registry(root / "tracking/github/repo-registry.toml")
    if item.id == "metronome-industries/ai"
)
resolution = resolve_capsule(
    GitTree(clone, sha, repo.max_file_bytes),
    repo.capsules[0],
    repo.secret_allowlist,
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

Expected for the inspected tree: 39 files and 227,137 bytes, with no missing required path, unsafe path, secret finding, identity failure, or budget failure. A changed live tree may vary within the approved limits of 80 files and 1,000,000 bytes.

- [ ] **Step 4: Prove verification published nothing**

Repeat Step 1.

Expected: raw evidence and work-item count remain unchanged.

### Task 3: Publish and review the immutable Metronome AI baseline

**Files:**
- Create under: `raw/github/metronome/ai/snapshots/`
- Create under: `tracking/github/repos/metronome/ai/ingest-packets/`
- Modify generated: `tracking/github/work-items.json`
- Modify generated: `tracking/github/status.md`
- Modify generated: `tracking/github/collection-index.json`
- Modify generated: `tracking/github/collection-index.md`
- Modify generated: `tracking/github/artifacts.lock`

**Interfaces:**
- Consumes: the verified Task 2 exact SHA and capsule measurements.
- Produces: one immutable commit snapshot, one review packet, and one work item at `awaiting_approval`; it produces no package release record.

- [ ] **Step 1: Run real baseline collection**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo metronome-industries/ai --mode backfill
```

Expected: collection publishes one exact-SHA evidence set and stops at `awaiting_approval`. Any required-path, secret, unsafe-path, or budget failure blocks publication and records `needs_manual_review` under the common failure policy.

- [ ] **Step 2: Validate generated state**

Run:

```bash
python3 scripts/validate_github_collection.py
python3 -m unittest tests.test_github_registry tests.test_github_capsule_policy tests.test_github_capsule_selection tests.test_github_commit_tree tests.test_collect_github_repos tests.test_github_ingest_packets tests.test_github_work_items
jq '.work_items[] | select(.repo_id == "metronome-industries/ai") | {work_item_id,state,recommended_mode,approved_mode,sha,ref_changes}' tracking/github/work-items.json
```

Expected: validation and tests pass; exactly one Metronome AI work item recommends `full`, has no approved mode, uses `ref_changes`, and is `awaiting_approval`.

- [ ] **Step 3: Read and report the complete packet**

Read generated `packet.json` and `packet.md` in full. Report default-branch identity, exact SHA, selected file count and bytes, required-reading count, unclassified changes, evidence gaps, expected wiki targets, and material billing findings. Do not run `approve`, `next-ingest`, or edit `wiki/`.

- [ ] **Step 4: Commit the reviewed collection evidence**

After packet validation, stage only generated Metronome AI raw/tracking evidence and generated global indexes/status:

```bash
git add raw/github/metronome/ai tracking/github/repos/metronome/ai tracking/github/work-items.json tracking/github/status.md tracking/github/collection-index.json tracking/github/collection-index.md tracking/github/artifacts.lock
git commit -m "Collect Metronome AI baseline"
```

Expected: collection evidence is committed while the work item remains `awaiting_approval`; `CLAUDE copy.md` remains untouched.

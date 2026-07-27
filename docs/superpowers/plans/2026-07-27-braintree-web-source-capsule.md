# Braintree Web Source Capsule Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:subagent-driven-development` (recommended) or
> `superpowers:executing-plans` to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable `braintree/braintree-web` as a registry-driven GitHub source
capsule, prove that its current `braintree-web@3.142.0` release fits the
approved production-source-plus-stories boundary, and collect exactly one
approval-gated baseline without ingesting it.

**Architecture:** The TOML registry remains the only human-maintained policy
authority. The reusable NPM capsule resolver selects the root package's full
`src/` tree and `.storybook/stories/`, adds reviewed repository context, and
excludes tests, fixtures, and `__mocks__`. Collection resolves package-qualified
releases to exact Git SHAs, publishes immutable raw evidence, and stops at the
serial ingest approval boundary.

**Tech Stack:** Python 3 standard library, `unittest`, TOML registry, Git
partial clones, and the existing GitHub collection and validation scripts.

## Global Constraints

- Keep `raw/` immutable; never rewrite an accepted snapshot.
- Do not collect Braintree Web v2.
- Select only `braintree-web@3.142.0` for this baseline.
- Retain all future stable v3 releases; exclude prereleases.
- Include full production `src/` and `.storybook/stories/`.
- Include `CHANGELOG.md` and `components.json`.
- Exclude tests, fixtures, `__mocks__`, generated `dist/`, CI, build tooling,
  and Storybook test infrastructure.
- Keep the approved 380-file / 3,000,000-byte capsule budgets and 420-file /
  3,500,000-byte packet budgets.
- Publish no partial snapshot on failure.
- Stop successful collection at `awaiting_approval`; do not approve or ingest.
- Do not create or modify Braintree wiki source, changelog, company, index, or
  log pages in this plan.
- Do not modify or stage the unrelated `CLAUDE copy.md`.

---

### Task 1: Classify `__mocks__` As Test Evidence

**Files:**
- Modify: `tests/test_github_capsule_selection.py`
- Modify: `scripts/github_capsule_selection.py`

**Interfaces:**
- Consumes: `_excluded_categories(path: str, enabled: Sequence[str])`.
- Produces: `excluded-category:tests` for files below any `__mocks__` path
  segment when the `tests` category is enabled.
- Preserves: Story files when `stories` is not an excluded category.

- [ ] **Step 1: Add the failing classifier test**

Add this test to `CapsuleSelectionTests`:

```python
def test_test_category_excludes_mock_directories_without_excluding_stories(self):
    mock_path = "src/lib/__mocks__/analytics.js"
    story_path = ".storybook/stories/HostedFields.stories.ts"
    tree = self.tree(
        {
            "package.json": manifest(name="braintree-web", version="3.142.0"),
            "src/index.js": "module.exports = {};\n",
            mock_path: "module.exports = {};\n",
            story_path: "export default {};\n",
        }
    )

    result = resolve_npm_capsule(
        tree,
        self.capsule(
            focus_packages=("braintree-web",),
            default_required_roots=("src", ".storybook/stories"),
            excluded_categories=("tests", "fixtures"),
        ),
        (),
    )

    paths = tuple(item.path for item in result.files)
    self.assertIn(story_path, paths)
    self.assertNotIn(mock_path, paths)
    self.assertIn(
        (mock_path, "excluded-category:tests"),
        result.excluded,
    )
```

- [ ] **Step 2: Run the focused test and verify the current gap**

```bash
python3 -m unittest \
  tests.test_github_capsule_selection.CapsuleSelectionTests.test_test_category_excludes_mock_directories_without_excluding_stories
```

Expected: `FAIL` because `src/lib/__mocks__/analytics.js` is still selected.

- [ ] **Step 3: Extend the reusable test category**

In `scripts/github_capsule_selection.py`, add `"__mocks__"` to the path
segments recognized by the `tests` branch of `_excluded_categories`:

```python
segment in (
    "test",
    "tests",
    "__tests__",
    "__mocks__",
    "bundle-tests",
)
```

Do not create a Braintree-specific exception or a new category.

- [ ] **Step 4: Run focused and complete capsule tests**

```bash
python3 -m unittest \
  tests.test_github_capsule_selection.CapsuleSelectionTests.test_test_category_excludes_mock_directories_without_excluding_stories
python3 -m unittest tests.test_github_capsule_selection
git diff --check
```

Expected: all tests pass and `git diff --check` prints nothing.

- [ ] **Step 5: Commit the reusable classifier fix**

```bash
git add scripts/github_capsule_selection.py tests/test_github_capsule_selection.py
git commit -m "fix: classify source mocks as tests"
```

---

### Task 2: Lock And Apply The Braintree Registry Policy

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`

**Interfaces:**
- Consumes: `github_registry.load_registry(path: Path)`.
- Produces: one enabled `braintree/braintree-web` repository with exactly one
  v3 version track and one reviewed capsule.

- [ ] **Step 1: Change the expected inventory state and add a failing policy test**

Change the `braintree/braintree-web` inventory tuple's enabled value from
`False` to `True`, then add this test to `RegistryTests`:

```python
def test_braintree_web_uses_the_reviewed_public_source_capsule(self):
    repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
    braintree = next(repo for repo in repos if repo.id == "braintree/braintree-web")

    self.assertTrue(braintree.enabled)
    self.assertEqual(
        (
            VersionTrack(
                "package:braintree-web@3",
                "latest-stable",
                "all-stable",
            ),
        ),
        braintree.version_tracks,
    )
    self.assertEqual(1, len(braintree.capsules))
    capsule = braintree.capsules[0]
    self.assertEqual("braintree-web-public-source", capsule.id)
    self.assertEqual("npm-tracked-source-v1", capsule.adapter)
    self.assertEqual(("braintree-web",), capsule.focus_packages)
    self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(
        ("src", ".storybook/stories"),
        capsule.default_required_roots,
    )
    self.assertEqual(("dist/",), capsule.default_generated_target_paths)
    self.assertEqual(("CHANGELOG.md", "components.json"), capsule.include_paths)
    self.assertEqual(("tests", "fixtures"), capsule.excluded_categories)
    self.assertEqual(512000, capsule.max_file_bytes)
    self.assertEqual(380, capsule.max_capsule_files)
    self.assertEqual(3000000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(420, capsule.max_packet_files)
    self.assertEqual(3500000, capsule.max_packet_utf8_bytes)
```

- [ ] **Step 2: Run the registry test and verify it fails**

```bash
python3 -m unittest \
  tests.test_github_registry.RegistryTests.test_braintree_web_uses_the_reviewed_public_source_capsule
```

Expected: `FAIL` because the existing Braintree Web row is disabled and has
no version track or capsule.

- [ ] **Step 3: Apply the approved policy to the existing row**

Keep the current repository metadata, change `enabled=false` to `enabled=true`,
and append these child tables before the next `[[repos]]`:

```toml
[[repos.version_tracks]]
selector="package:braintree-web@3"
backfill="latest-stable"
future="all-stable"
include_prerelease=false
[[repos.capsules]]
id="braintree-web-public-source"
adapter="npm-tracked-source-v1"
focus_packages=["braintree-web"]
dependency_scope="internal-runtime-closure"
changed_path_policy="policy-bounded"
default_required_roots=["src", ".storybook/stories"]
default_generated_target_paths=["dist/"]
include_paths=["CHANGELOG.md", "components.json"]
excluded_categories=["tests", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=512000
max_capsule_files=380
max_capsule_utf8_bytes=3000000
max_packet_files=420
max_packet_utf8_bytes=3500000
```

- [ ] **Step 4: Run policy and structural validation**

```bash
python3 -m unittest tests.test_github_registry tests.test_github_capsule_selection
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all tests pass, collection validation reports no errors, and the
diff check prints nothing.

- [ ] **Step 5: Commit the registry policy**

```bash
git add tests/test_github_registry.py tracking/github/repo-registry.toml
git commit -m "policy: enable Braintree Web source capsule"
```

---

### Task 3: Audit The Exact `v3.142.0` Capsule

**Files:**
- Read: `tracking/github/repo-registry.toml`
- Read: temporary shallow clone of `https://github.com/braintree/braintree-web`
- Read: `scripts/github_git_tree.py`
- Read: `scripts/github_capsule_selection.py`

**Interfaces:**
- Consumes: tag `v3.142.0`, its resolved full commit SHA, `GitTree`, and
  `resolve_npm_capsule`.
- Produces: exact file, byte, story, test, fixture, and mock measurements plus
  required-path assertions.

- [ ] **Step 1: Create an exact shallow audit clone and export its identity**

```bash
AUDIT_ROOT="$(mktemp -d /private/tmp/braintree-web-audit.XXXXXX)"
git clone --filter=blob:none --no-checkout --depth 1 --branch v3.142.0 \
  https://github.com/braintree/braintree-web.git \
  "$AUDIT_ROOT/repo"
export AUDIT_REPO="$AUDIT_ROOT/repo"
export SNAPSHOT_SHA="$(git -C "$AUDIT_REPO" rev-parse 'v3.142.0^{commit}')"
printf 'SNAPSHOT_SHA=%s\n' "$SNAPSHOT_SHA"
test "${#SNAPSHOT_SHA}" -eq 40
```

Expected: the tag resolves to a 40-character commit SHA. Record that exact SHA
in the execution notes; do not infer or truncate it.

- [ ] **Step 2: Resolve and audit the capsule**

Run from the wiki root in the same shell so `AUDIT_REPO` and `SNAPSHOT_SHA`
retain the exact values captured above:

```bash
PYTHONPATH=scripts python3 - <<'PY'
import os
from pathlib import Path

from github_capsule_selection import resolve_npm_capsule
from github_git_tree import GitTree
from github_registry import load_registry

root = Path.cwd()
repo = next(
    item
    for item in load_registry(root / "tracking/github/repo-registry.toml")
    if item.id == "braintree/braintree-web"
)
tree = GitTree(
    Path(os.environ["AUDIT_REPO"]),
    os.environ["SNAPSHOT_SHA"],
    repo.max_file_bytes,
)
resolution = resolve_npm_capsule(
    tree,
    repo.capsules[0],
    repo.secret_allowlist,
)
paths = tuple(item.path for item in resolution.files)
excluded = resolution.excluded
utf8_bytes = sum(item.size for item in resolution.files)
stories = tuple(path for path in paths if ".stories." in path)
tests = tuple(
    path for path in paths
    if ".test." in path
    or ".spec." in path
    or any(
        segment in ("test", "tests", "__tests__", "__mocks__", "bundle-tests")
        for segment in path.split("/")
    )
)
fixtures = tuple(
    path for path in paths
    if any(
        segment in ("fixture", "fixtures", "__fixtures__", "snapshots")
        for segment in path.split("/")
    )
)
mocks_excluded = tuple(
    path for path, reason in excluded
    if "__mocks__" in path.split("/") and reason == "excluded-category:tests"
)
required = {
    "package.json",
    "src/index.js",
    "src/client/index.js",
    "src/hosted-fields/index.js",
    "src/three-d-secure/index.js",
    "src/paypal-checkout-v6/index.js",
    "src/venmo/index.js",
    ".storybook/stories/HostedFields/HostedFields.stories.ts",
    "CHANGELOG.md",
    "components.json",
}

print("sha=" + os.environ["SNAPSHOT_SHA"])
print("files=" + str(len(paths)))
print("utf8_bytes=" + str(utf8_bytes))
print("stories=" + str(len(stories)))
print("selected_tests=" + str(len(tests)))
print("selected_fixtures=" + str(len(fixtures)))
print("excluded_mocks=" + str(len(mocks_excluded)))
assert required <= set(paths), sorted(required - set(paths))
assert stories
assert not tests
assert not fixtures
assert mocks_excluded
assert len(paths) <= repo.capsules[0].max_capsule_files
assert utf8_bytes <= repo.capsules[0].max_capsule_utf8_bytes
PY
```

Expected: every required path is present, stories and excluded mocks are
non-empty, no test or fixture is selected, and both capsule budgets pass.

- [ ] **Step 3: Record audit evidence and stop on drift**

Record the exact SHA and all printed measurements in the task report. If the
tag, package version, required paths, exclusions, or budgets differ from the
approved design, stop and return to design review. Do not raise a budget or
weaken an assertion during execution.

No repository files or commits are produced by this task.

---

### Task 4: Prove Backfill Selection In Isolated State

**Files:**
- Read: committed repository state exported to a temporary directory
- Do not modify: the working repository's generated tracking state

**Interfaces:**
- Consumes: `collect_github_repos.py collect --repo
  braintree/braintree-web --mode backfill --dry-run`.
- Produces: `state="discovered"` with exactly
  `release_ids=["braintree-web@3.142.0"]`.

- [ ] **Step 1: Export committed state into a temporary repository**

```bash
DRY_ROOT="$(mktemp -d /private/tmp/braintree-web-dryrun.XXXXXX)"
git archive --format=tar HEAD -o "$DRY_ROOT/repo.tar"
mkdir "$DRY_ROOT/repo"
tar -xf "$DRY_ROOT/repo.tar" -C "$DRY_ROOT/repo"
```

Use an archive rather than the live workspace because a failed dry run can
write failure status through the current CLI error path.

- [ ] **Step 2: Run the isolated dry run**

```bash
cd "$DRY_ROOT/repo"
python3 scripts/collect_github_repos.py collect \
  --repo braintree/braintree-web \
  --mode backfill \
  --dry-run
```

Expected JSON:

```json
{
  "errors": [],
  "release_ids": ["braintree-web@3.142.0"],
  "repo_id": "braintree/braintree-web",
  "snapshot_paths": [],
  "state": "discovered",
  "work_item_ids": []
}
```

- [ ] **Step 3: Prove the real workspace stayed clean**

Return to the real wiki root and run:

```bash
git status --short
```

Expected: only the pre-existing untracked `CLAUDE copy.md` appears. If any
generated collection state appears, stop and investigate before real
collection.

No repository files or commits are produced by this task.

---

### Task 5: Collect The Baseline And Stop At Approval

**Files:**
- Create: `raw/github/braintree/braintree-web/snapshots/<date>-<sha7>/**`
- Create: `raw/github/braintree/braintree-web/releases/braintree-web/3.142.0/**`
- Modify: `tracking/github/work-items.json`
- Modify: `tracking/github/status.md`
- Create, if produced by the collector:
  `tracking/github/repos/braintree/braintree-web/**`
- Do not modify: `wiki/**`

**Interfaces:**
- Consumes: the approved registry policy and package-qualified
  `braintree-web@3.142.0`.
- Produces: one immutable exact-SHA snapshot, one package release record,
  generated baseline change metadata, and one work item in
  `awaiting_approval`. A first baseline has no prior release comparison.

- [ ] **Step 1: Run real backfill collection**

From the wiki root:

```bash
python3 scripts/collect_github_repos.py collect \
  --repo braintree/braintree-web \
  --mode backfill
```

Expected: exit code 0, `release_ids=["braintree-web@3.142.0"]`, exactly one
snapshot path, exactly one work item ID, no errors, and
`state="awaiting_approval"`.

If collection returns `collection_failed` or `needs_manual_review`, stop.
Report the generated failure state and apply the existing retry/manual-review
rules; do not publish, approve, or ingest partial evidence.

- [ ] **Step 2: Inspect generated evidence**

```bash
git status --short
python3 scripts/collect_github_repos.py status
find raw/github/braintree/braintree-web -type f | sort
```

Read the generated snapshot manifest, release manifest, comparison/change
record, and work-item row. Confirm:

- repository ID is `braintree/braintree-web`;
- release ID is `braintree-web@3.142.0`;
- tag is `v3.142.0`;
- the snapshot SHA equals the Task 3 audit SHA;
- the work item is `awaiting_approval` with no approved ingest mode;
- selected file and byte counts match the audited policy result;
- stories are retained;
- tests, fixtures, and `__mocks__` are excluded; and
- no file under `wiki/` changed.

- [ ] **Step 3: Run complete validation**

```bash
python3 -m unittest discover -s tests
python3 scripts/validate_github_collection.py
git diff --check
git status --short
```

Expected: all tests pass, GitHub collection validation reports no errors, the
diff check prints nothing, and the only unrelated path remains
`CLAUDE copy.md`.

- [ ] **Step 4: Commit only immutable evidence and generated state**

Inspect `git status --short` first. Stage only the generated Braintree raw
evidence and generated `tracking/github/` files:

```bash
git add raw/github/braintree/braintree-web
git add tracking/github/status.md tracking/github/work-items.json
if test -d tracking/github/repos/braintree/braintree-web; then
  git add tracking/github/repos/braintree/braintree-web
fi
git diff --cached --check
git status --short
git commit -m "Collect Braintree Web 3.142.0 baseline"
```

Omit any `git add` path that does not exist or was not generated. Never use
`git add .`, and never stage `CLAUDE copy.md`.

- [ ] **Step 5: Push and verify the exact remote commit**

```bash
git push origin main
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

Expected: push succeeds and the local `HEAD` equals the remote `main` SHA.
This also publishes the already reviewed design and implementation-plan
commits if they are still local.

- [ ] **Step 6: Report the approval boundary**

Report:

- exact tag and full SHA;
- package-qualified release ID;
- snapshot path;
- file and UTF-8 byte counts;
- retained story count;
- excluded test, fixture, and mock counts;
- work-item ID;
- queue state `awaiting_approval`;
- local and remote commit SHA; and
- explicit confirmation that no Braintree wiki ingest occurred.

Wait for a separate user decision before running `approve`, `next-ingest`, or
editing any Braintree wiki authority.

## Acceptance Checklist

- [ ] `braintree/braintree-web` has one enabled v3 release track and one
  reviewed capsule.
- [ ] Backfill discovers only `braintree-web@3.142.0`.
- [ ] The exact tag target and package manifest version agree.
- [ ] Full `src/` and Storybook stories are retained.
- [ ] Tests, fixtures, `__mocks__`, and Storybook test infrastructure are
  excluded.
- [ ] Capsule and packet budgets remain unchanged and pass.
- [ ] Full tests, collection validation, and `git diff --check` pass.
- [ ] One exact-SHA work item ends at `awaiting_approval`.
- [ ] No Braintree wiki page is created or modified.
- [ ] `CLAUDE copy.md` remains untouched and untracked.

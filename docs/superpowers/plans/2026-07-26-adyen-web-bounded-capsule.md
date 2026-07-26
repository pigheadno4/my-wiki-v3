# Adyen Web Bounded Capsule Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the oversized Adyen Web source policy with the approved bounded base capsule and collect `@adyen/adyen-web@6.41.0` into the existing approval-gated work item.

**Architecture:** The registry remains the sole human-maintained policy authority. The generic NPM capsule resolver applies a smaller set of package-relative required roots, preserves stories inside those roots, excludes tests and fixtures, and retains exact-SHA supplements as the path for payment-method implementation outside the base. No collector code or budget limit changes are required.

**Tech Stack:** Python 3 standard library, `unittest`, TOML registry, Git partial clones, existing GitHub collection and validation scripts.

## Global Constraints

- Keep `max_capsule_files = 340`.
- Keep `max_capsule_utf8_bytes = 3000000`.
- Keep tests and fixtures excluded.
- Retain stories inside selected component roots.
- Reuse work item `github-9f56dfbe62e4e84b03c7`.
- Publish no partial snapshot on failure.
- Stop successful collection at `awaiting_approval`; do not ingest.
- Do not modify or stage the unrelated `CLAUDE copy.md`.

---

### Task 1: Lock And Apply The Adyen Base Policy

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`

**Interfaces:**
- Consumes: `github_registry.load_registry(path: Path) -> Tuple[RepoConfig, ...]`
- Produces: one enabled `adyen/adyen-web` `CapsuleConfig` with the approved package-relative directory roots, exact include paths, and unchanged safety budgets.

- [ ] **Step 1: Write the failing registry-policy test**

Add this test to `RegistryTests` in `tests/test_github_registry.py`:

```python
def test_adyen_web_uses_the_reviewed_bounded_public_source_capsule(self):
    repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
    adyen = next(repo for repo in repos if repo.id == "adyen/adyen-web")
    capsule = adyen.capsules[0]

    self.assertEqual(
        (
            "src/components/Card",
            "src/components/Dropin",
            "src/components/ThreeDS2",
            "src/core",
            "src/types",
        ),
        capsule.default_required_roots,
    )
    self.assertEqual(
        (
            "src/components/index.ts",
            "src/components/types.ts",
            "src/index.ts",
            "src/index.umd.ts",
            "src/types.ts",
        ),
        capsule.include_paths,
    )
    self.assertEqual(("dist/",), capsule.default_generated_target_paths)
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual(340, capsule.max_capsule_files)
    self.assertEqual(3000000, capsule.max_capsule_utf8_bytes)
```

- [ ] **Step 2: Run the test to verify it fails**

Run:

```bash
python3 -m unittest \
  tests.test_github_registry.RegistryTests.test_adyen_web_uses_the_reviewed_bounded_public_source_capsule
```

Expected: `FAIL` because the current registry still puts the five exact files
in `default_required_roots` rather than `include_paths`.

- [ ] **Step 3: Apply the bounded Adyen registry policy**

Replace only the Adyen Web capsule's required roots in
`tracking/github/repo-registry.toml`:

```toml
default_required_roots=[
  "src/types",
  "src/core",
  "src/components/Dropin",
  "src/components/Card",
  "src/components/ThreeDS2",
]
default_generated_target_paths=["dist/"]
include_paths=[
  "src/index.ts",
  "src/index.umd.ts",
  "src/types.ts",
  "src/components/index.ts",
  "src/components/types.ts",
]
excluded_categories=["tests", "fixtures"]
```

Do not change any budget, version-track, repository identity, or other
provider row.

- [ ] **Step 4: Run focused policy tests**

Run:

```bash
python3 -m unittest tests.test_github_registry tests.test_github_capsule_selection
```

Expected: all tests pass.

- [ ] **Step 5: Run structural validation**

Run:

```bash
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: collection validation reports no structural errors and the diff
check produces no output.

- [ ] **Step 6: Commit the reviewed policy**

```bash
git add tests/test_github_registry.py tracking/github/repo-registry.toml
git commit -m "policy: bound Adyen Web source capsule"
```

### Task 2: Audit The Exact v6.41.0 Capsule

**Files:**
- Read: `tracking/github/repo-registry.toml`
- Read: temporary shallow clone of `https://github.com/Adyen/adyen-web`
- Read: `scripts/github_git_tree.py`
- Read: `scripts/github_capsule_selection.py`

**Interfaces:**
- Consumes: `GitTree(repo_path: Path, treeish: full_sha, max_file_bytes: int)` and `resolve_npm_capsule(tree, capsule, allowlist) -> CapsuleResolution`. Tag `v6.41.0` must resolve to `b19eec7054340a1526c87d450fd7dfff75794ed9` before constructing `GitTree`.
- Produces: measured file count, UTF-8 byte count, story count, and proof that tests and fixtures are absent.

- [ ] **Step 1: Create an exact shallow audit clone**

Run:

```bash
git clone --filter=blob:none --no-checkout --depth 1 --branch v6.41.0 \
  https://github.com/Adyen/adyen-web.git \
  /private/tmp/adyen-web-bounded-capsule-audit
```

Expected: clone succeeds and resolves tag `v6.41.0`.

Verify the immutable tag target before resolving the capsule:

```bash
git -C /private/tmp/adyen-web-bounded-capsule-audit rev-parse v6.41.0^{commit}
```

Expected: `b19eec7054340a1526c87d450fd7dfff75794ed9`.

- [ ] **Step 2: Resolve and print the capsule measurements**

Run from the wiki root:

```bash
PYTHONPATH=scripts python3 - <<'PY'
from pathlib import Path

from github_capsule_selection import resolve_npm_capsule
from github_git_tree import GitTree
from github_registry import load_registry

root = Path.cwd()
repo = next(
    item
    for item in load_registry(root / "tracking/github/repo-registry.toml")
    if item.id == "adyen/adyen-web"
)
snapshot_sha = "b19eec7054340a1526c87d450fd7dfff75794ed9"
tree = GitTree(
    Path("/private/tmp/adyen-web-bounded-capsule-audit"),
    snapshot_sha,
    repo.max_file_bytes,
)
resolution = resolve_npm_capsule(tree, repo.capsules[0], repo.secret_allowlist)
paths = tuple(item.path for item in resolution.files)
utf8_bytes = sum(item.size for item in resolution.files)
stories = tuple(
    path for path in paths
    if "/stories/" in path or ".stories." in path
)
tests = tuple(
    path for path in paths
    if "/tests/" in path
    or "/__tests__/" in path
    or ".test." in path
    or ".spec." in path
)
fixtures = tuple(
    path for path in paths
    if "/fixture/" in path or "/fixtures/" in path
)
print("files=" + str(len(paths)))
print("utf8_bytes=" + str(utf8_bytes))
print("stories=" + str(len(stories)))
print("tests=" + str(len(tests)))
print("fixtures=" + str(len(fixtures)))
assert len(paths) <= repo.capsules[0].max_capsule_files
assert utf8_bytes <= repo.capsules[0].max_capsule_utf8_bytes
assert stories
assert not tests
assert not fixtures
PY
```

Expected:

- `files` is at most `340`;
- `utf8_bytes` is at most `3000000`;
- `stories` is greater than zero;
- `tests=0`; and
- `fixtures=0`.

- [ ] **Step 3: Verify required evidence paths are present**

Extend the audit snippet locally, without committing a new script, with:

```python
required_suffixes = (
    "/src/index.ts",
    "/src/index.umd.ts",
    "/src/types.ts",
    "/src/core/AdyenCheckout.ts",
    "/src/components/Dropin/index.ts",
    "/src/components/Card/index.ts",
    "/src/components/ThreeDS2/index.ts",
)
for suffix in required_suffixes:
    assert any(path.endswith(suffix) for path in paths), suffix
```

Expected: every assertion passes.

- [ ] **Step 4: Stop on budget failure**

If either budget assertion fails, do not increase a limit. Keep the Adyen item
in `needs_manual_review`, report the measured dependency-closure expansion,
and return to the approved design for a narrower root list.

### Task 3: Retry Collection And Stop At Approval

**Files:**
- Modify: `tracking/github/work-items.json`
- Modify: `tracking/github/status.md`
- Create on success: `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/manifest.json`
- Create on success: files selected under `raw/github/adyen/adyen-web/snapshots/2026-07-26-b19eec7/files/`
- Create on success: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.0/2026-07-26/manifest.json`
- Create on success: `raw/github/adyen/adyen-web/releases/adyen-web/6.41.0/2026-07-26/release-notes.md`

**Interfaces:**
- Consumes: existing work item `github-9f56dfbe62e4e84b03c7` in `needs_manual_review`
- Produces: the same work item in `awaiting_approval`, with immutable snapshot and package-qualified release evidence.

- [ ] **Step 1: Reopen the existing manual-review item**

Run:

```bash
python3 scripts/collect_github_repos.py retry \
  --item github-9f56dfbe62e4e84b03c7
```

Expected: the returned item has state `discovered`, the same work-item ID,
the same repository, package-qualified release, and exact SHA.

- [ ] **Step 2: Collect the bounded Adyen release**

Run:

```bash
python3 scripts/collect_github_repos.py collect \
  --repo adyen/adyen-web \
  --mode backfill
```

Expected:

```text
state: awaiting_approval
release: @adyen/adyen-web@6.41.0
work item: github-9f56dfbe62e4e84b03c7
```

No ingest command is permitted in this task.

- [ ] **Step 3: Validate immutable evidence and queue state**

Run:

```bash
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py status
```

Expected: validator reports no structural errors; status shows the Adyen item
in `awaiting_approval`, with a snapshot manifest and release manifest, and no
approved mode.

- [ ] **Step 4: Run the full test suite**

Run:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

Expected: all tests pass.

- [ ] **Step 5: Verify only intended generated evidence changed**

Run:

```bash
git status --short
git diff --check
```

Expected: only Adyen raw evidence, GitHub work-item/status state, and any
generated Adyen comparison are changed; `CLAUDE copy.md` remains untracked.

- [ ] **Step 6: Commit the immutable collection result**

```bash
git add raw/github/adyen/adyen-web \
  tracking/github/work-items.json \
  tracking/github/status.md \
  tracking/github/repos/adyen/adyen-web
git commit -m "data: collect Adyen Web 6.41.0 capsule"
```

Omit the comparison path from `git add` if the initial baseline correctly
creates no comparison directory.

- [ ] **Step 7: Push and verify remote main**

```bash
git push origin main
git ls-remote origin refs/heads/main
git rev-parse main
```

Expected: remote and local SHAs match.

- [ ] **Step 8: Report the approval gate**

Report exact file count, byte count, retained story count, excluded tests and
fixtures, release identity, SHA, work-item ID, and evidence paths. Explicitly
state that ingest has not started and requires separate user approval.

# PayPal JS Focused GitHub Collection Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a focused, release-driven `paypal/paypal-js` pilot that preserves immutable package release evidence and SHA source snapshots, recommends full or delta serial ingest, and produces cumulative source/changelog knowledge without the superseded packet lifecycle.

**Architecture:** Keep the completed registry, release discovery, exact Git-tree, npm-workspace, capsule-policy, capsule-selection, secret-scan, and budget primitives. Replace packet-oriented orchestration with three focused boundaries: `github_pilot_store.py` owns immutable raw evidence and mechanical comparisons, `github_work_items.py` owns the machine queue and generated status, and `collect_github_repos.py` coordinates release discovery and user-facing commands. Rewrite validation and rules around these authorities, then remove the superseded packet/durable-I/O implementation after the new offline end-to-end path passes.

**Tech Stack:** Python 3.9 standard library, Git CLI, TOML registry via `toml_compat.py`, `unittest`, Markdown/JSON/TOML artifacts.

## Global Constraints

- Python compatibility is 3.9.6; do not use `tomllib`, structural pattern matching, or newer typing syntax.
- Add no mandatory third-party runtime dependency.
- Package release identities are always package-qualified, such as `@paypal/paypal-js@10.0.3`.
- Raw evidence is immutable after publication.
- One exact Git SHA has one source snapshot; separately collected package releases link to it.
- Latest v8 and latest v9 are historical baselines; every stable v10 release is retained.
- Same-SHA releases discovered together create one work item with package-specific comparisons.
- Collection may discover multiple releases, but ingest is user-approved and one work item at a time.
- Full ingest preserves existing historical knowledge and adds a new version section.
- Delta ingest fully reads assigned changed evidence and does not reread unchanged historical raw files.
- No live GitHub collection or wiki ingest occurs while executing this implementation plan; Task 7 ends with an offline fixture and a dry-run command checklist.
- The approved specification is `docs/superpowers/specs/2026-07-20-paypal-js-focused-pilot-design.md`.

## File Ownership Map

| File | Responsibility |
| --- | --- |
| `scripts/github_registry.py` | Static repository and package-release policy parsing |
| `scripts/github_releases.py` | Package-qualified release discovery and retention |
| `scripts/github_capsule_selection.py` | Bounded npm source capsule plus changed release evidence |
| `scripts/github_pilot_store.py` | Immutable SHA snapshots, immutable release records, mechanical comparisons |
| `scripts/github_work_items.py` | Full/delta recommendation, queue state, retry state, generated status Markdown |
| `scripts/collect_github_repos.py` | Focused collection/status/compare/approve/next/retry CLI |
| `scripts/github_validation.py` | Offline validation of registry, raw evidence, work items, status, source, changelog |
| `rules/github-repos.md` | Collection and serial ingest procedure |
| `rules/query-and-synthesis.md` | Current/version/change/deep-source query routing |

The implementation retires `github_packets.py`, `github_reporting.py`, `github_durable_io.py`, and the old packet-oriented `github_snapshot.py` only after the focused coordinator and validator pass their offline end-to-end tests. Git history preserves the superseded implementation.

---

### Task 1: Package Release Scope And Registry Policy

**Files:**
- Modify: `scripts/github_registry.py`
- Modify: `scripts/github_releases.py`
- Modify: `tracking/github/repo-registry.toml`
- Test: `tests/test_github_registry.py`
- Test: `tests/test_github_releases.py`

**Interfaces:**
- Consumes: existing `VersionTrack`, `ReleaseCandidate`, `select_release_candidates()`.
- Produces: `backfill = "latest-stable"`; exact v8/v9 baseline tracks and all-stable v10 tracks for both PayPal packages; one `npm-tracked-source-v1` capsule policy.

- [ ] **Step 1: Add failing release-policy tests**

Add to `tests/test_github_releases.py`:

```python
def test_latest_stable_selects_only_the_highest_stable_candidate(self):
    selected = select_release_candidates(
        self._track(backfill="latest-stable"),
        self._candidates("9.0.0", "9.3.0", "9.4.0-rc.1", "9.2.5"),
    )

    self.assertEqual(("9.3.0",), tuple(item.version for item in selected))


def test_latest_stable_preserves_an_already_indexed_baseline(self):
    selected = select_release_candidates(
        self._track(backfill="latest-stable"),
        self._candidates("9.0.0", "9.3.0"),
        existing_versions=("9.2.0",),
    )

    self.assertEqual(("9.2.0", "9.3.0"), tuple(item.version for item in selected))
```

Add a registry fixture assertion to `tests/test_github_registry.py` that loads a minimal row using `latest-stable` and rejects `latest-major` as unknown.

- [ ] **Step 2: Run the focused tests and confirm failure**

Run:

```bash
python3 -m unittest tests.test_github_registry tests.test_github_releases -v
```

Expected: FAIL because `latest-stable` is not in `BACKFILL_POLICIES` and release selection rejects it.

- [ ] **Step 3: Implement `latest-stable` deterministically**

In `scripts/github_registry.py`, replace the backfill constant with:

```python
BACKFILL_POLICIES = {"all-stable", "latest-stable", "minor-baselines", "none"}
```

In `select_release_candidates()` after the `all-stable` branch and before `minor-baselines`, add:

```python
if track.backfill == "latest-stable":
    selected = []
    existing = _version_keys(existing_versions)
    for candidate in eligible:
        if _version_key(candidate.version) in existing:
            selected.append(candidate)
    if eligible:
        selected.append(eligible[-1])
    return _deduplicated_candidates(selected)
```

This keeps a previously accepted baseline addressable while selecting only the current highest stable baseline for a first backfill.

- [ ] **Step 4: Configure both PayPal package histories and the source capsule**

Replace the current `paypal/paypal-js` version tracks with these exact rows:

```toml
[[repos.version_tracks]]
selector="package:@paypal/paypal-js@8"
backfill="latest-stable"
future="none"
include_prerelease=false

[[repos.version_tracks]]
selector="package:@paypal/paypal-js@9"
backfill="latest-stable"
future="none"
include_prerelease=false

[[repos.version_tracks]]
selector="package:@paypal/paypal-js@10"
backfill="all-stable"
future="all-stable"
include_prerelease=false

[[repos.version_tracks]]
selector="package:@paypal/react-paypal-js@8"
backfill="latest-stable"
future="none"
include_prerelease=false

[[repos.version_tracks]]
selector="package:@paypal/react-paypal-js@9"
backfill="latest-stable"
future="none"
include_prerelease=false

[[repos.version_tracks]]
selector="package:@paypal/react-paypal-js@10"
backfill="all-stable"
future="all-stable"
include_prerelease=false

[[repos.capsules]]
id="paypal-js-public-source"
adapter="npm-tracked-source-v1"
focus_packages=["@paypal/paypal-js", "@paypal/react-paypal-js"]
dependency_scope="internal-runtime-closure"
default_required_roots=["src"]
default_generated_target_paths=["dist/"]
include_paths=[]
excluded_categories=["tests", "stories", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=512000
max_capsule_files=240
max_capsule_utf8_bytes=1500000
max_packet_files=280
max_packet_utf8_bytes=1800000
```

Do not change enabled states or policies for unrelated repositories in this task.

- [ ] **Step 5: Verify release scope and commit**

Run:

```bash
python3 -m unittest tests.test_github_registry tests.test_github_releases tests.test_github_capsule_policy -v
python3 scripts/validate_github_collection.py
```

Expected: tests PASS; validator reports no new registry-policy error. Existing unrelated workspace baseline findings, if any, must be recorded verbatim rather than described as a clean run.

Commit:

```bash
git add scripts/github_registry.py scripts/github_releases.py tracking/github/repo-registry.toml tests/test_github_registry.py tests/test_github_releases.py
git commit -m "feat: focus paypal js package release scope"
```

---

### Task 2: Changed-Evidence Source Capsule

**Files:**
- Modify: `scripts/github_capsule_selection.py`
- Test: `tests/test_github_capsule_selection.py`

**Interfaces:**
- Consumes: `GitTree`, `CapsuleConfig`, `SecretAllowlist`, existing workspace ownership and budgets.
- Produces: `resolve_npm_capsule(tree: GitTree, capsule: CapsuleConfig, allowlist: Sequence[SecretAllowlist], changed_paths: Sequence[str] = ()) -> CapsuleResolution`; `scan_evidence_files(files: Sequence[CapsuleFile], allowlist: Sequence[SecretAllowlist]) -> Tuple[SecretFinding, ...]`; selected changed package files use classification reason `changed-release-evidence` and still pass file limits, secret scanning, and total budgets.

- [ ] **Step 1: Add failing tests for changed source, documentation, and tests**

Extend the existing capsule fixture with `packages/widget/test/public-api.test.ts` and `packages/widget/docs/new-option.md`, then add:

```python
def test_changed_release_evidence_is_collected_outside_the_normal_capsule(self):
    resolution = resolve_npm_capsule(
        self.tree,
        self.capsule,
        (),
        changed_paths=(
            "packages/widget/test/public-api.test.ts",
            "packages/widget/docs/new-option.md",
        ),
    )

    selected = {item.path: item.classification_reason for item in resolution.files}
    self.assertEqual(
        "changed-release-evidence",
        selected["packages/widget/test/public-api.test.ts"],
    )
    self.assertEqual(
        "changed-release-evidence",
        selected["packages/widget/docs/new-option.md"],
    )


def test_changed_path_outside_included_packages_is_not_collected(self):
    resolution = resolve_npm_capsule(
        self.tree,
        self.capsule,
        (),
        changed_paths=("packages/unrelated/src/private.ts",),
    )

    self.assertNotIn(
        "packages/unrelated/src/private.ts",
        {item.path for item in resolution.files},
    )
```

Add tests proving an oversized changed file and a changed file containing a detected secret fail exactly like normal capsule files.

- [ ] **Step 2: Run the focused tests and confirm failure**

Run:

```bash
python3 -m unittest tests.test_github_capsule_selection -v
```

Expected: FAIL because `resolve_npm_capsule()` does not accept `changed_paths`.

- [ ] **Step 3: Add changed paths to selection before reads and budgets**

Change the public signature to:

```python
def resolve_npm_capsule(
    tree: GitTree,
    capsule: CapsuleConfig,
    allowlist: Sequence[SecretAllowlist],
    changed_paths: Sequence[str] = (),
) -> CapsuleResolution:
```

After workspace packages are resolved and before `_selected_blobs()`, normalize changed paths with `safe_policy_path()`. Map every path to the deepest included package whose `owned_paths` contains it, then add it to `candidate_reasons`:

```python
for path in sorted(set(changed_paths)):
    if not safe_policy_path(path):
        _review("unsafe-changed-path", path)
    owners = []
    for package in workspace.packages:
        prefix = package.path + "/" if package.path else ""
        if path.startswith(prefix) and path[len(prefix):] in package.owned_paths:
            owners.append(package)
    if not owners:
        continue
    package = sorted(owners, key=lambda item: len(item.path), reverse=True)[0]
    prefix = package.path + "/" if package.path else ""
    candidate_reasons[path] = (
        package.name,
        path[len(prefix):],
        {"changed-release-evidence"},
    )
```

Add `changed-release-evidence` to `_CLASSIFICATION_ORDER` after `include-path`. Do not bypass `_read_selected_files()`, `_scan_secrets()`, `max_file_bytes`, capsule file count, or capsule byte budgets.

Expose `scan_evidence_files()` as the public wrapper used by the snapshot store for repository-root context files. It must decode every file as strict UTF-8, run the same detector suite, apply exact blob/path/detector allowlists, and raise `SecretFindingsBlocked` when any finding remains unallowlisted. Do not duplicate detector regexes in the store.

- [ ] **Step 4: Verify capsule safety and commit**

Run:

```bash
python3 -m unittest tests.test_github_capsule_selection tests.test_github_npm_workspace tests.test_github_git_tree -v
```

Expected: PASS.

Commit:

```bash
git add scripts/github_capsule_selection.py tests/test_github_capsule_selection.py
git commit -m "feat: retain changed github package evidence"
```

---

### Task 3: Immutable Snapshot And Package Release Store

**Files:**
- Create: `scripts/github_pilot_store.py`
- Create: `tests/test_github_pilot_store.py`
- Modify: `tests/github_test_support.py`

**Interfaces:**
- Consumes: `RepoConfig`, `ReleaseCandidate`, `ReleaseNotesEvidence`, `GitTree`, `CapsuleResolution`, canonical JSON helpers.
- Produces:
  - `SourceSnapshot(repo_id, sha, collected_date, directory, manifest_path, files)`
  - `PackageReleaseRecord(release_id, package, version, tag, sha, release_date, collected_date, directory, manifest_path, notes_path, notes_sha256)`
  - `ComparisonRecord(package, from_version, to_version, from_sha, to_sha, changed_paths, patch_path, metadata_path, markdown_path)`
  - `publish_source_snapshot(root: Path, config: RepoConfig, tree: GitTree, resolution: CapsuleResolution, collected_date: str, triggering_refs: Sequence[str]) -> SourceSnapshot`
  - `publish_release_record(root: Path, config: RepoConfig, candidate: ReleaseCandidate, release_date: str, evidence: Optional[ReleaseNotesEvidence], collected_date: str) -> PackageReleaseRecord`
  - `write_package_comparison(root: Path, config: RepoConfig, repo_root: Path, package: str, from_version: str, from_sha: str, from_paths: Sequence[str], to_version: str, to_sha: str, to_paths: Sequence[str]) -> ComparisonRecord`

- [ ] **Step 1: Add failing immutable-store tests**

Create `tests/test_github_pilot_store.py` with fixture helpers from `github_test_support.py` and these cases:

```python
def test_same_sha_reuses_one_source_snapshot(self):
    first = publish_source_snapshot(
        self.root, self.config, self.tree, self.resolution,
        "2026-07-20", ("@scope/a@10.0.0",)
    )
    second = publish_source_snapshot(
        self.root, self.config, self.tree, self.resolution,
        "2026-07-21", ("@scope/b@10.1.0",)
    )

    self.assertEqual(first.directory, second.directory)
    self.assertEqual(first.manifest_path.read_bytes(), second.manifest_path.read_bytes())


def test_same_release_note_hash_is_idempotent(self):
    first = publish_release_record(
        self.root, self.config, self.candidate, "2026-07-07",
        self.evidence, "2026-07-20"
    )
    second = publish_release_record(
        self.root, self.config, self.candidate, "2026-07-07",
        self.evidence, "2026-07-21"
    )

    self.assertEqual(first.directory, second.directory)


def test_changed_release_notes_create_an_immutable_revision(self):
    first = publish_release_record(
        self.root, self.config, self.candidate, "2026-07-07",
        self.evidence, "2026-07-20"
    )
    revised = replace(self.evidence, content=b"corrected release notes\n")
    second = publish_release_record(
        self.root, self.config, self.candidate, "2026-07-07",
        revised, "2026-07-21"
    )

    self.assertNotEqual(first.directory, second.directory)
    self.assertEqual(b"original release notes\n", first.notes_path.read_bytes())
    self.assertEqual(b"corrected release notes\n", second.notes_path.read_bytes())


def test_failed_snapshot_validation_publishes_no_partial_directory(self):
    invalid = replace(
        self.resolution,
        files=(replace(self.resolution.files[0], sha256="0" * 64),),
    )

    with self.assertRaises(PilotStoreError):
        publish_source_snapshot(
            self.root, self.config, self.tree, invalid,
            "2026-07-20", ("@scope/a@10.0.0",)
        )

    self.assertFalse((self.root / "raw/github/acme/widgets/snapshots").exists())
```

Add a comparison test asserting package A compares only its own path roots and that `comparison.json`, `comparison.md`, and `diff.patch` link both SHAs.

- [ ] **Step 2: Run the new tests and confirm import failure**

Run:

```bash
python3 -m unittest tests.test_github_pilot_store -v
```

Expected: FAIL with `ModuleNotFoundError: github_pilot_store`.

- [ ] **Step 3: Define immutable evidence records and safe slugs**

Create `scripts/github_pilot_store.py` with frozen dataclasses and these public helpers:

```python
@dataclass(frozen=True)
class SourceSnapshot:
    repo_id: str
    sha: str
    collected_date: str
    directory: Path
    manifest_path: Path
    files: Tuple[str, ...]


@dataclass(frozen=True)
class PackageReleaseRecord:
    release_id: str
    package: str
    version: str
    tag: str
    sha: str
    release_date: str
    collected_date: str
    directory: Path
    manifest_path: Path
    notes_path: Path
    notes_sha256: str


def package_slug(package: str) -> str:
    value = package.lower().rsplit("/", 1)[-1]
    if not re.fullmatch(r"[a-z0-9][a-z0-9._~-]*", value):
        raise PilotStoreError("package name cannot form a safe path")
    return value
```

Reject a repository policy when two tracked package names produce the same slug; never merge their release directories.

Use `tempfile.mkdtemp(dir=str(raw_root / ".staging"))` for construction. Write files with original repository-relative paths, verify every content hash and total byte limit, write canonical `manifest.json`, then publish with `os.replace(staging, destination)`. On any exception, remove only the owned staging directory. If a SHA snapshot already exists, validate its manifest identity and return it unchanged.

Before publication, read these tracked repository-root context files when present: `README.md`, `package.json`, `package-lock.json`, `LICENSE`, and `LICENSE.md`. Represent them as `CapsuleFile` values with package `""`, purpose `repository-context`, and classification reason `repository-context`; run `scan_evidence_files()` over them. Merge them with `resolution.files`, reject duplicate paths, and enforce `config.max_file_bytes` plus `config.max_snapshot_bytes` across the final set.

- [ ] **Step 4: Publish release records separately from snapshots**

Use this path contract:

```python
release_root = (
    root / "raw" / "github" / config.company / config.id.split("/", 1)[1]
    / "releases" / package_slug(candidate.package) / candidate.version
)
```

The first record is `<collected-date>/`. If the exact `(package, version, tag, SHA, notes_sha256)` already exists, return it unchanged. If content changed, allocate `<collected-date>-r2`, then `-r3`. The release manifest must contain only:

```python
manifest = {
    "collected_date": collected_date,
    "notes_sha256": notes_sha256,
    "package": candidate.package,
    "release_date": evidence.published_at,
    "repository": config.id,
    "sha": candidate.commit_sha,
    "tag": candidate.tag,
    "version": candidate.version,
}
```

When GitHub has no release body, write an empty `release-notes.md`, set `notes_available` to `False` in the manifest, and use the resolved tag commit time passed as `release_date`. Do not synthesize upstream prose in `raw/`.

- [ ] **Step 5: Add package-specific mechanical comparisons**

Implement:

```python
def write_package_comparison(
    root: Path,
    config: RepoConfig,
    repo_root: Path,
    package: str,
    from_version: str,
    from_sha: str,
    from_paths: Sequence[str],
    to_version: str,
    to_sha: str,
    to_paths: Sequence[str],
) -> ComparisonRecord:
```

Validate SHAs and paths, use the sorted union of package roots as Git pathspecs, and run exact `git diff --name-only` and `git diff --no-ext-diff --unified=3`. Store generated artifacts under:

```text
tracking/github/repos/paypal/paypal-js/comparisons/<package-slug>/<from>--<to>/
```

`comparison.json` is the machine authority. `comparison.md` identifies the package, versions, SHAs, changed paths, and links to `diff.patch`; it must not summarize semantic product impact.

- [ ] **Step 6: Verify the store and commit**

Run:

```bash
python3 -m unittest tests.test_github_pilot_store tests.test_github_canonical tests.test_github_git_tree -v
```

Expected: PASS, with no network calls.

Commit:

```bash
git add scripts/github_pilot_store.py tests/test_github_pilot_store.py tests/github_test_support.py
git commit -m "feat: store focused github pilot evidence"
```

---

### Task 4: Full/Delta Recommendation And Work Items

**Files:**
- Create: `scripts/github_work_items.py`
- Create: `tests/test_github_work_items.py`

**Interfaces:**
- Consumes: immutable release/snapshot/comparison records from Task 3.
- Produces:
  - `ChangeSignals(package, from_version, to_version, changed_paths, public_exports_changed, release_notes)`
  - `PackageChange(package, from_version, to_version, release_id, release_manifest, comparison_manifest, recommended_mode, reasons)`
  - `WorkItem(work_item_id, repo_id, sha, collection_date, package_changes, snapshot_manifest, recommended_mode, approved_mode, state, attempts_in_run, consecutive_failed_runs, last_error, last_attempted_date)`
  - `recommend_ingest_mode(signals) -> Tuple[str, Tuple[str, ...]]`
  - `upsert_discovered_work_item(path, item) -> Tuple[WorkItem, ...]`
  - `transition_work_item(path: Path, work_item_id: str, expected: str, requested: str, approved_mode: Optional[str] = None) -> Tuple[WorkItem, ...]`
  - `record_collection_failure(path: Path, item: WorkItem, error: str, attempted_date: str, attempts_in_run: int) -> Tuple[WorkItem, ...]`
  - `render_status(items: Sequence[WorkItem]) -> str`

- [ ] **Step 1: Add failing classifier and state tests**

Create `tests/test_github_work_items.py` with:

```python
def test_baseline_and_major_upgrade_require_full_ingest(self):
    baseline = self.signals(from_version="", to_version="8.9.2")
    major = self.signals(from_version="9.3.0", to_version="10.0.0")

    self.assertEqual("full", recommend_ingest_mode(baseline)[0])
    self.assertEqual("full", recommend_ingest_mode(major)[0])


def test_small_patch_defaults_to_delta(self):
    signals = self.signals(
        from_version="10.0.2",
        to_version="10.0.3",
        changed_paths=("packages/paypal-js/src/types.ts",),
    )

    mode, reasons = recommend_ingest_mode(signals)

    self.assertEqual("delta", mode)
    self.assertIn("contained-patch-release", reasons)


def test_public_export_change_escalates_patch_to_full(self):
    signals = self.signals(
        from_version="10.0.2",
        to_version="10.0.3",
        public_exports_changed=True,
    )

    mode, reasons = recommend_ingest_mode(signals)

    self.assertEqual("full", mode)
    self.assertIn("public-exports-changed", reasons)


def test_same_sha_package_changes_form_one_work_item(self):
    item = build_work_item(
        "paypal/paypal-js", "3caece5" * 5 + "3caec",
        "2026-07-20", (self.paypal_change, self.react_change),
        self.snapshot_manifest,
    )

    self.assertEqual(2, len(item.package_changes))
    self.assertEqual("full", item.recommended_mode)


def test_user_approval_is_required_before_ingesting(self):
    save_work_items(self.path, (self.awaiting_item,))

    with self.assertRaises(WorkItemStateError):
        transition_work_item(
            self.path, self.awaiting_item.work_item_id,
            "awaiting_approval", "ingesting"
        )
```

Add retry tests proving three attempts in one run become `collection_failed`, three consecutive failed runs become `needs_manual_review`, and an explicit retry returns the item to `discovered` without changing the last successful evidence paths.

- [ ] **Step 2: Run tests and confirm import failure**

Run:

```bash
python3 -m unittest tests.test_github_work_items -v
```

Expected: FAIL with `ModuleNotFoundError: github_work_items`.

- [ ] **Step 3: Implement deterministic recommendation rules**

Use ordered reason codes and this precedence:

```python
FULL_SIGNAL_ORDER = (
    "initial-package-baseline",
    "major-version-transition",
    "public-exports-changed",
    "security-signal",
    "sdk-initialization-signal",
    "payment-behavior-signal",
    "broad-change-set",
)
BROAD_CHANGE_FILE_LIMIT = 25


def recommend_ingest_mode(signals: ChangeSignals) -> Tuple[str, Tuple[str, ...]]:
    reasons = []
    prior = parse_semver(signals.from_version) if signals.from_version else None
    current = parse_semver(signals.to_version)
    if current is None:
        raise ValueError("to_version must be semantic")
    if prior is None:
        reasons.append("initial-package-baseline")
    elif prior.major != current.major:
        reasons.append("major-version-transition")
    if signals.public_exports_changed:
        reasons.append("public-exports-changed")
    lowered = signals.release_notes.lower()
    if "security" in lowered or "cve-" in lowered:
        reasons.append("security-signal")
    if "initialization" in lowered or "load script" in lowered:
        reasons.append("sdk-initialization-signal")
    if any(word in lowered for word in ("payment", "checkout", "vault", "venmo")):
        reasons.append("payment-behavior-signal")
    if len(signals.changed_paths) > BROAD_CHANGE_FILE_LIMIT:
        reasons.append("broad-change-set")
    ordered = tuple(code for code in FULL_SIGNAL_ORDER if code in reasons)
    if ordered:
        return "full", ordered
    if prior is not None and prior.major == current.major:
        return "delta", ("contained-patch-release" if prior.minor == current.minor else "contained-minor-release",)
    return "full", ("ambiguous-version-transition",)
```

Keyword matches are escalation signals, not semantic claims. They force human review through full ingest.

- [ ] **Step 4: Implement strict JSON state and generated status**

Use one JSON object with `format_version = 1` and a sorted `work_items` array. Reject duplicate JSON keys, unknown fields, duplicate work-item IDs, unsafe paths, and invalid transitions. Build IDs from canonical JSON of repository, SHA, and sorted release IDs:

```python
def build_work_item_id(repo_id: str, sha: str, release_ids: Sequence[str]) -> str:
    payload = {
        "release_ids": sorted(set(release_ids)),
        "repository": repo_id,
        "sha": sha,
    }
    return "github-" + canonical_sha256(payload)[:20]
```

Allowed transitions are:

```python
TRANSITIONS = {
    "discovered": ("collected", "collection_failed", "needs_manual_review"),
    "collected": ("awaiting_approval",),
    "awaiting_approval": ("approved",),
    "approved": ("ingesting",),
    "ingesting": ("ingested", "needs_manual_review"),
    "collection_failed": ("discovered", "needs_manual_review"),
    "needs_manual_review": ("discovered",),
}
```

`status.md` renders repository, SHA, package releases, recommended/approved mode, state, attempt count, last error, snapshot link, and comparison links. It is regenerated from JSON after every mutation.

- [ ] **Step 5: Verify state behavior and commit**

Run:

```bash
python3 -m unittest tests.test_github_work_items tests.test_github_versions tests.test_github_canonical -v
```

Expected: PASS.

Commit:

```bash
git add scripts/github_work_items.py tests/test_github_work_items.py
git commit -m "feat: manage github pilot ingest work items"
```

---

### Task 5: Focused Release-Driven Coordinator And CLI

**Files:**
- Rewrite: `scripts/collect_github_repos.py`
- Rewrite: `tests/test_collect_github_repos.py`

**Interfaces:**
- Consumes: Tasks 1–4 and existing `clone_repository()`, `discover_release_candidates()`, `GitTree`, `resolve_npm_capsule()`.
- Produces CLI commands:
  - `collect --repo <owner/repo> --mode backfill|future [--dry-run]`
  - `collect --repo <owner/repo> --release <package@version> [--dry-run]`
  - `status`
  - `compare --repo <owner/repo> --from <package@version> --to <package@version>`
  - `approve --item <id> --mode full|delta`
  - `next-ingest`
  - `retry --item <id>`

- [ ] **Step 1: Replace packet-oriented CLI tests with focused behavior**

Keep existing fixture helpers that create local bare repositories. Replace packet assertions with:

```python
def test_backfill_groups_same_sha_releases_into_one_awaiting_item(self):
    result = collect_one(
        self.root, self.config, release_mode="backfill",
        clone_source=self.remote
    )

    self.assertEqual("awaiting_approval", result.state)
    items = load_work_items(self.root / "tracking/github/work-items.json")
    self.assertEqual(1, len(items))
    self.assertEqual(2, len(items[0].package_changes))


def test_recollection_with_no_new_release_is_unchanged(self):
    collect_one(self.root, self.config, release_mode="backfill", clone_source=self.remote)
    result = collect_one(self.root, self.config, release_mode="future", clone_source=self.remote)

    self.assertEqual("unchanged", result.state)


def test_collection_failure_does_not_create_an_ingest_item(self):
    with mock.patch("collect_github_repos.publish_source_snapshot", side_effect=OSError("disk full")):
        result = collect_one(
            self.root, self.config, release_mode="backfill",
            clone_source=self.remote, max_attempts=1
        )

    self.assertEqual("collection_failed", result.state)
    items = load_work_items(self.root / "tracking/github/work-items.json")
    self.assertEqual(1, len(items))
    self.assertEqual("collection_failed", items[0].state)
    self.assertEqual("", items[0].snapshot_manifest)


def test_approve_records_user_selected_mode_before_ingest(self):
    item = self.collect_one_item()

    approve_one(self.root, item.work_item_id, "delta")
    approved = load_work_items(self.root / "tracking/github/work-items.json")[0]

    self.assertEqual("approved", approved.state)
    self.assertEqual("delta", approved.approved_mode)
```

Add parser tests rejecting ambiguous `v10`, cross-package comparisons, collection without `--repo`, and any command that attempts collection plus ingest.

- [ ] **Step 2: Run tests against the old coordinator and confirm failure**

Run:

```bash
python3 -m unittest tests.test_collect_github_repos -v
```

Expected: FAIL because the old coordinator returns packet IDs and exposes `prepare`/`packet-state` instead of work items.

- [ ] **Step 3: Implement release discovery, chronological grouping, and SHA reuse**

Rewrite the module around this result contract:

```python
@dataclass(frozen=True)
class CollectionResult:
    repo_id: str
    state: str
    release_ids: Tuple[str, ...]
    snapshot_paths: Tuple[str, ...]
    work_item_ids: Tuple[str, ...]
    errors: Tuple[str, ...]
```

`collect_one()` must:

1. clone to a temporary directory;
2. discover all configured package tracks before creating work items;
3. select releases with backfill/future policy;
4. sort by semantic major/minor/patch, then release date and package-qualified tag for deterministic cross-package grouping;
5. group selected releases by SHA;
6. fetch release notes and publish immutable release records;
7. open `GitTree(clone_path, sha, config.max_file_bytes)`;
8. resolve the configured capsule with the union of package-specific changed paths;
9. publish or reuse the SHA snapshot;
10. compare each package with its previous selected release of the same package;
11. calculate export changes by comparing `main`, `module`, `types`, `typings`, and `exports` fields in the two package manifests;
12. recommend package modes and create one grouped work item; and
13. leave it `awaiting_approval`.

Do not import `github_packets`, `github_reporting`, `github_snapshot`, or `github_durable_io`.

- [ ] **Step 4: Implement bounded retries without a retry service**

Use `max_attempts=3`. Retry only `ReleaseEvidenceError`, `GitObjectReadError`, `GitCommandError`, `URLError`, and `OSError` from clone/fetch/read operations. Do not retry registry errors, invalid refs, unsafe paths, secret findings, or budget errors.

On exhaustion, call `record_collection_failure()` with bounded error text. A failure work item remains visible, but never transition it to `collected` or `awaiting_approval` before the release records, source snapshot, and comparisons all validate. Because raw evidence is immutable, a failed later artifact may leave valid raw evidence available for retry, but it must not appear as approved or ingested work.

- [ ] **Step 5: Implement approval, next-ingest, compare, retry, and status commands**

`approve` requires state `awaiting_approval` and stores `approved_mode`. `next-ingest` prints exactly one oldest `approved` item as JSON and makes no state change. `compare` requires package-qualified releases of the same package. `retry` requires `collection_failed` or `needs_manual_review` and returns it to `discovered`. `status` regenerates and prints `tracking/github/status.md`.

Remove `prepare` and `packet-state` parser branches. They belong to the superseded packet lifecycle.

- [ ] **Step 6: Verify focused orchestration and commit**

Run:

```bash
python3 -m unittest tests.test_collect_github_repos tests.test_github_pilot_store tests.test_github_work_items tests.test_github_releases -v
```

Expected: PASS with local fixture repositories only.

Commit:

```bash
git add scripts/collect_github_repos.py tests/test_collect_github_repos.py
git commit -m "feat: coordinate focused paypal js collection"
```

---

### Task 6: Validation, Rules, And Superseded-Code Removal

**Files:**
- Rewrite: `scripts/github_validation.py`
- Modify: `scripts/validate_github_collection.py`
- Rewrite: `tests/test_github_validation.py`
- Modify: `rules/github-repos.md`
- Modify: `rules/query-and-synthesis.md`
- Modify: `CLAUDE.md`
- Delete: `scripts/github_packets.py`
- Delete: `scripts/github_reporting.py`
- Delete: `scripts/github_durable_io.py`
- Delete: `scripts/github_snapshot.py`
- Delete: `tests/test_github_packets.py`
- Delete: `tests/test_github_reporting.py`
- Delete: `tests/test_github_durable_io.py`
- Delete: `tests/test_github_snapshot.py`

**Interfaces:**
- Consumes: focused raw/store/work-item contracts from Tasks 3–5.
- Produces: `inspect_github(root) -> GitHubReport`, `validate_github(report) -> List[str]`, focused workflow rules, no active packet/durable-I/O path.

- [ ] **Step 1: Add failing validator fixtures**

Rewrite `tests/test_github_validation.py` around focused fixtures and include:

```python
def test_valid_focused_repository_has_no_errors(self):
    report = inspect_github(self.root)

    self.assertEqual([], validate_github(report))


def test_release_record_must_link_an_existing_sha_snapshot(self):
    self.release_manifest["sha"] = "f" * 40
    self.write_release_manifest()

    errors = validate_github(inspect_github(self.root))

    self.assertIn("release record links missing SHA snapshot", "\n".join(errors))


def test_status_markdown_must_match_work_items_json(self):
    self.status_path.write_text("stale\n", encoding="utf-8")

    errors = validate_github(inspect_github(self.root))

    self.assertIn("tracking/github/status.md is stale", errors)


def test_source_and_changelog_are_both_required_after_ingest(self):
    self.work_item = replace(self.work_item, state="ingested")
    self.save_work_items()

    errors = validate_github(inspect_github(self.root))

    self.assertTrue(any("source-github-paypal-js.md" in item for item in errors))
    self.assertTrue(any("changelog-github-paypal-js.md" in item for item in errors))
```

Add tests for hash mismatch, unsafe paths, duplicate release identity without revision, missing comparison links, invalid work-item state, and a changelog entry that omits package-qualified version or raw links.

- [ ] **Step 2: Run validator tests and confirm failure**

Run:

```bash
python3 -m unittest tests.test_github_validation -v
```

Expected: FAIL because the old validator requires version indexes, packets, packet events, and packet dashboards.

- [ ] **Step 3: Rewrite validation around four authorities**

The focused validator checks:

1. registry package tracks and capsule policy;
2. immutable snapshot/release manifests and hashes;
3. work-items JSON plus generated status equality; and
4. cumulative source/changelog links for ingested items.

Keep strict JSON duplicate-key rejection and safe path checks. Remove packet, version-index, packet-event, receipt, and old dashboard inspection. `GitHubReport` must expose `repositories`, `snapshots`, `release_records`, `comparisons`, `work_items`, `source_pages`, `changelog_pages`, and `status_text` only.

- [ ] **Step 4: Replace GitHub workflow and query rules**

Rewrite `rules/github-repos.md` to match the approved specification exactly:

- package-qualified release identities;
- latest-v8/latest-v9/all-v10 pilot order;
- SHA snapshot and package release record separation;
- same-SHA grouped work items;
- user-approved serial full/delta ingest;
- cumulative `wiki/sources/paypal/github/source-github-paypal-js.md` knowledge organized by package and major version;
- separate `wiki/sources/paypal/github/changelog-github-paypal-js.md` release history;
- preservation of older validated version findings during full ingest;
- `paypal/paypal-checkout-components` as a separately collected evidence authority, never a PayPal JS subdirectory;
- bounded retries and manual review; and
- no packet terminology.

Update `rules/query-and-synthesis.md` with the approved routing table. Remove legacy instructions that modify an accepted raw stub during deep dive. Exact-SHA supplements are immutable additions.

Update only the GitHub lines in `CLAUDE.md`: directory layout, workflow summary, and source-page description. Keep `AGENTS.md` as the existing thin pointer.

- [ ] **Step 5: Remove superseded modules after import audit**

Run:

```bash
rg -n "github_packets|github_reporting|github_durable_io|from github_snapshot|packet-state|ingest packet" scripts tests rules CLAUDE.md
```

Expected before deletion: matches only in the files listed for rewrite/delete. Remove the four superseded modules and their tests. Run the command again.

Expected after deletion: no active-code or active-rule matches. Historical specs and plans may still mention the terms and are not edited in this task.

- [ ] **Step 6: Verify focused validation and commit**

Run:

```bash
python3 -m unittest tests.test_github_validation tests.test_validate_wiki -v
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: tests PASS; the focused GitHub validator passes its generated fixture/contracts; `git diff --check` produces no output. Report pre-existing general wiki validation findings separately if they remain.

Commit:

```bash
git add scripts tests rules CLAUDE.md
git commit -m "refactor: retire github packet workflow"
```

---

### Task 7: Offline End-To-End PayPal JS Pilot Rehearsal

**Files:**
- Create: `tests/fixtures/github/paypal-js/README.md`
- Create: `tests/test_github_pilot_e2e.py`
- Modify: `docs/superpowers/specs/2026-07-20-paypal-js-focused-pilot-design.md`

**Interfaces:**
- Consumes: focused CLI and all contracts from Tasks 1–6.
- Produces: a network-free local Git fixture demonstrating v8 baseline, v9 major, v10.0 full, same-SHA paired releases, v10 patch delta, v10.1 classification, unchanged recollection, failure retry, approval, and next-ingest ordering.

- [ ] **Step 1: Build the fixture entirely during the test**

`tests/fixtures/github/paypal-js/README.md` documents tag sequence and expected modes. `tests/test_github_pilot_e2e.py` creates a temporary monorepo with these package-qualified tags:

```text
@paypal/paypal-js@8.1.0
@paypal/react-paypal-js@8.9.2
@paypal/paypal-js@9.8.0
@paypal/react-paypal-js@9.3.0
@paypal/paypal-js@10.0.0
@paypal/react-paypal-js@10.0.0
@paypal/paypal-js@10.0.1
@paypal/react-paypal-js@10.1.0
@paypal/paypal-js@10.0.2
@paypal/react-paypal-js@10.1.1
```

Place paired tags on shared commits. Include real `package.json` exports, `.ts` public entry points, internal `.ts` imports, changed docs, and a changed test.

- [ ] **Step 2: Add the failing end-to-end assertion**

The test runs backfill against the local bare remote and asserts:

```python
self.assertEqual(
    (
        "@paypal/paypal-js@8.1.0",
        "@paypal/react-paypal-js@8.9.2",
        "@paypal/paypal-js@9.8.0",
        "@paypal/react-paypal-js@9.3.0",
        "@paypal/paypal-js@10.0.0",
        "@paypal/react-paypal-js@10.0.0",
        "@paypal/paypal-js@10.0.1",
        "@paypal/react-paypal-js@10.1.0",
        "@paypal/paypal-js@10.0.2",
        "@paypal/react-paypal-js@10.1.1",
    ),
    self.collected_release_ids(),
)
self.assertLess(self.snapshot_count(), self.release_record_count())
self.assertEqual("full", self.mode_for("@paypal/react-paypal-js@10.0.0"))
self.assertEqual("delta", self.mode_for("@paypal/paypal-js@10.0.1"))
self.assertEqual("unchanged", self.collect_future().state)
```

It approves only the oldest item and proves `next-ingest` returns exactly that item without changing its state.

- [ ] **Step 3: Run the rehearsal and fix only contract defects**

Run:

```bash
python3 -m unittest tests.test_github_pilot_e2e -v
```

Expected: PASS without network access or writes outside the temporary test root.

If the fixture exposes a contract defect, fix it in the owning Task 1–6 module and add the smallest focused regression test there before rerunning this test. Do not restore packet lifecycle behavior.

- [ ] **Step 4: Run the full local verification suite**

Run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_github_collection.py
python3 scripts/validate_wiki.py
git diff --check
git status --short
```

Expected:

- all unit tests pass;
- focused GitHub validation passes;
- `git diff --check` has no output;
- known general wiki validation findings are reported as baseline rather than called clean;
- no live `raw/github/paypal/paypal-js/` pilot evidence has been created by tests; and
- only intended implementation, test, rule, and plan changes remain.

- [ ] **Step 5: Record implementation conformance and commit**

Change the focused specification status from `Specification approved; implementation pending` to:

```text
Implementation complete; offline pilot conformance passed; live collection pending user approval
```

Commit:

```bash
git add tests/fixtures/github/paypal-js/README.md tests/test_github_pilot_e2e.py docs/superpowers/specs/2026-07-20-paypal-js-focused-pilot-design.md
git commit -m "test: rehearse focused paypal js pilot"
```

- [ ] **Step 6: Stop before live collection**

Report:

- commit IDs for Tasks 1–7;
- exact test and validator results;
- current worktree and branch;
- confirmation that no live collection or ingest ran; and
- the proposed next command, without running it:

```bash
python3 scripts/collect_github_repos.py collect --repo paypal/paypal-js --mode backfill --dry-run
```

Wait for explicit user approval before the networked dry run, real collection, or any wiki ingest.

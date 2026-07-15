# GitHub Repository Collection and Versioned Ingest Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a registry-driven GitHub repository collector that creates immutable curated snapshots, generated comparison and ingest packets, deterministic monitoring, and company-scoped wiki integration while preserving strictly serial, human-approved ingest.

**Architecture:** A standard-library Python CLI orchestrates focused modules for TOML compatibility, registry validation, Git ref resolution, key-file selection, immutable snapshot promotion, packet generation, state reporting, and validation. The deterministic core is completed and tested with temporary local Git repositories before any public repository is contacted. Live collection stops at a user-review gate; wiki ingest then processes exactly one complete packet at a time.

**Tech Stack:** Python 3.9.6 standard library, `unittest`, Git CLI through `subprocess`, TOML with `tomllib`/`tomli`/tested fallback, JSON/JSONL state, Markdown, Obsidian wikilinks.

## Global Constraints

- Read `CLAUDE.md` and the relevant `rules/*.md` file before each operational workflow.
- Keep `rules/github-repos.md` as a standalone workflow file.
- Collection may batch; ingest is human-kicked-off and processes exactly one packet at a time.
- Before GitHub ingest, read the complete packet, every referenced `snapshot.md`, and every required raw file.
- Accepted files under `raw/` are immutable. Never enrich or overwrite an accepted snapshot.
- Exact upstream files and the repository-owned snapshot manifest belong in `raw/`; generated diffs, summaries, status, and packets belong in `tracking/`.
- Use company-first wiki paths such as `wiki/sources/paypal/github/` and source-type-first operational paths such as `raw/github/paypal/`.
- One repository maps to one stable source page unless a separately approved exception applies.
- Keep the implementation compatible with Python 3.9.6 and add no mandatory third-party dependency.
- Keep network-dependent checks outside the default unit-test suite.
- Do not modify the unrelated untracked `CLAUDE copy.md`.
- Commit after every independently reviewable task.

## Delivery Stages

1. Tasks 1-7 build the deterministic local core and rules.
2. Task 8 proves the complete collector against local Git fixtures.
3. Task 9 performs the `paypal/paypal-js` live collection pilot, then stops for user approval.
4. Task 10 performs serial pilot ingest only after that approval.
5. Task 11 collects the remaining pilot repositories without auto-ingest.
6. Tasks 12-13 perform the deterministic source-layout and log migrations only after pilot acceptance.

## File Map

| File | Responsibility |
| --- | --- |
| `scripts/toml_compat.py` | Python 3.9-compatible TOML loading shared by PSP and GitHub registries. |
| `scripts/github_registry.py` | Registry dataclasses, validation, defaults, and selection. |
| `tracking/github/repo-registry.toml` | Human-maintained complete repository inventory and collection intent. |
| `scripts/github_git.py` | Git subprocess wrapper, selector-scoped ref fetching, repository inspection, and exact ref resolution. |
| `scripts/github_snapshot.py` | Key-file policy, hashes, snapshot naming, staging, validation, and immutable promotion. |
| `scripts/github_packets.py` | Version index, baseline packets, delta packets, and explicit comparison packets. |
| `scripts/github_reporting.py` | Collection states, packet states, JSONL events, and generated dashboards. |
| `scripts/collect_github_repos.py` | Public `collect`, `compare`, `prepare`, `status`, and `packet-state` CLI. |
| `scripts/github_validation.py` | Read-only structural inspection and validation library. |
| `scripts/validate_github_collection.py` | Validation CLI for raw snapshots, packets, indexes, and dashboards. |
| `scripts/migrate_github_wiki_layout.py` | Deterministic dry-run/apply move of legacy GitHub source pages. |
| `scripts/migrate_wiki_logs.py` | Deterministic dry-run/apply split of root log entries by company. |
| `tests/github_test_support.py` | Temporary local Git repository builder used by GitHub tests. |
| `tests/test_toml_compat.py` | TOML fallback and PSP compatibility tests. |
| `tests/test_github_registry.py` | Registry validation, defaults, selection, and full-inventory tests. |
| `tests/test_github_git.py` | Ref resolution, aliases, ambiguity, submodule, and LFS tests. |
| `tests/test_github_snapshot.py` | Selection, byte fidelity, limits, immutability, and supplement tests. |
| `tests/test_github_packets.py` | Baseline, delta, rename/delete, comparison, and raw/tracking boundary tests. |
| `tests/test_github_reporting.py` | State transitions, terminal reconciliation, and dashboard tests. |
| `tests/test_collect_github_repos.py` | CLI selection, dry-run, failure, and local end-to-end tests. |
| `tests/test_github_validation.py` | Nested raw/source reconciliation and status consistency tests. |
| `tests/test_migrate_github_wiki_layout.py` | Source owner detection, dry-run, move, and idempotence tests. |
| `tests/test_migrate_wiki_logs.py` | Log-block parsing, company classification, preservation, and idempotence tests. |

---

### Task 1: Lock the Repository Workflow Contracts

**Files:**
- Modify: `CLAUDE.md`
- Modify: `rules/github-repos.md`
- Modify: `rules/ingest.md`
- Modify: `rules/lint.md`
- Modify: `rules/raw-collection.md`
- Modify: `docs/superpowers/specs/2026-07-14-github-repository-collection-design.md`

**Interfaces:**
- Consumes: the approved design and existing global raw/ingest rules.
- Produces: the exact operational contract every subsequent task and pilot must follow.

- [ ] **Step 1: Update the root directory map and workflow routing**

Change the GitHub entries in `CLAUDE.md` to name the registry, immutable nested snapshots, generated tracking state, company-first GitHub source pages, and standalone `rules/github-repos.md` workflow. Keep schema and conventions in the root; keep procedural detail in the rule.

- [ ] **Step 2: Replace the mutable stub workflow**

Rewrite `rules/github-repos.md` with these required sections:

```markdown
## Collection modes
## Registry contract
## Immutable snapshot contract
## Baseline, delta, and comparison packets
## Collection-to-ingest boundary
## Serial repository ingest
## Stable source page and version history
## Add a company or repository
## Legacy stub compatibility
## Validation and monitoring
```

State explicitly that normal recollection never edits a legacy stub or accepted snapshot. An explicit supplement receives a new immutable `-rN` capture and `capture_kind = "supplement"`.

- [ ] **Step 3: Clarify the full-read ingest unit**

Add this repository-specific rule to `rules/ingest.md` without weakening the global one-source rule:

```markdown
For GitHub, one source cycle means one approved baseline, delta, or comparison
packet. Read the packet, every referenced snapshot manifest, and every file in
its required reading set in full before writing wiki content. Do not claim to
have read the whole upstream repository.
```

- [ ] **Step 4: Route nested orphan checks and raw boundaries**

Update `rules/lint.md` to run `python3 scripts/validate_github_collection.py` for `raw/github/` and `tracking/github/`. Update `rules/raw-collection.md` so the GitHub row points to immutable snapshots instead of mutable stub/detail enrichment.

- [ ] **Step 5: Verify rule coverage**

Run:

```bash
rg -n "repo-registry|immutable snapshot|one packet|company-first|validate_github_collection" CLAUDE.md rules/github-repos.md rules/ingest.md rules/lint.md rules/raw-collection.md
git diff --check
```

Expected: every phrase is represented in the appropriate rule; `git diff --check` exits `0`.

- [ ] **Step 6: Commit the contracts**

```bash
git add CLAUDE.md rules/github-repos.md rules/ingest.md rules/lint.md rules/raw-collection.md docs/superpowers/specs/2026-07-14-github-repository-collection-design.md
git commit -m "docs: define versioned github collection workflow"
```

---

### Task 2: Add TOML Compatibility and the Complete Repository Registry

**Files:**
- Create: `scripts/toml_compat.py`
- Create: `scripts/github_registry.py`
- Create: `tracking/github/repo-registry.toml`
- Create: `tests/test_toml_compat.py`
- Create: `tests/test_github_registry.py`
- Modify: `scripts/fetch_psp.py:56-103`
- Modify: `tests/test_fetch_psp.py`

**Interfaces:**
- Consumes: JSON-compatible TOML values, `[[repos]]` arrays, and existing `scripts/psp_config.toml`.
- Produces: `load_toml(path: Path) -> Dict[str, object]`, `load_registry(path: Path) -> Tuple[RepoConfig, ...]`, `validate_registry(repos: Sequence[RepoConfig]) -> List[str]`, and `select_repos(repos: Sequence[RepoConfig], company: Optional[str] = None, repo_id: Optional[str] = None, enabled_only: bool = True) -> Tuple[RepoConfig, ...]`.

- [ ] **Step 1: Write failing TOML and registry tests**

Create tests that require multiline arrays and arrays of tables on Python 3.9 fallback:

```python
class RegistryTests(unittest.TestCase):
    def test_loads_multiline_arrays_and_repo_tables(self):
        data = load_toml(self.write_registry(
            '[[repos]]\n'
            'id = "paypal/paypal-js"\n'
            'company = "paypal"\n'
            'url = "https://github.com/paypal/paypal-js"\n'
            'enabled = true\n'
            'repo_type = "web-sdk"\n'
            'priority = "tier1"\n'
            'track = "releases-and-default-branch"\n'
            'version_strategy = "monorepo-packages"\n'
            'requested_refs = [\n'
            '  "default-branch",\n'
            '  "package:@paypal/react-paypal-js@9",\n'
            ']\n'
        ))
        self.assertEqual(2, len(data["repos"][0]["requested_refs"]))

    def test_registry_rejects_duplicate_ids_and_mutable_state(self):
        repos = (self.repo(), self.repo())
        self.assertTrue(any("duplicate id" in error for error in validate_registry(repos)))
        self.assertTrue(any("latest_version" in error for error in validate_registry(
            (self.repo(extra={"latest_version": "10.0.0"}),)
        )))

    def test_full_inventory_has_71_rows_and_five_enabled_pilots(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        self.assertEqual(71, len(repos))
        self.assertEqual(5, len(select_repos(repos, enabled_only=True)))
```

- [ ] **Step 2: Run tests to verify failure**

Run:

```bash
python3 -m unittest tests.test_toml_compat tests.test_github_registry -v
```

Expected: import failures because the modules do not exist.

- [ ] **Step 3: Implement the shared TOML loader**

Use this public entry point:

```python
def load_toml(path: Path) -> Dict[str, object]:
    try:
        import tomllib
    except ModuleNotFoundError:
        try:
            import tomli as tomllib
        except ModuleNotFoundError:
            return _load_toml_subset(path)
    with path.open("rb") as handle:
        return tomllib.load(handle)
```

The fallback must buffer bracket-balanced multiline arrays, support `[table]` and `[[array.table]]`, parse JSON-compatible strings/bools/numbers/arrays, remove comments only when outside strings, and raise `ValueError` with the source line for malformed input. Move `fetch_psp.py` to this loader and delete its private duplicate parser.

- [ ] **Step 4: Implement immutable registry records and validation**

Define the exact public record:

```python
@dataclass(frozen=True)
class RepoConfig:
    id: str
    company: str
    url: str
    enabled: bool
    repo_type: str
    priority: str
    track: str
    version_strategy: str
    collection_frequency: str
    requested_refs: Tuple[str, ...]
    key_paths: Tuple[str, ...]
    exclude_paths: Tuple[str, ...]
    max_file_bytes: int
    max_snapshot_bytes: int
```

Defaults are `collection_frequency = "on-demand"`, empty tuples for optional lists, `max_file_bytes = 1048576`, and `max_snapshot_bytes = 10485760`. Reject unknown priority, track, or strategy values; mutable-state keys; IDs not equal to the lowercased URL owner/repository; duplicate IDs; duplicate URLs; and non-HTTPS GitHub URLs.

- [ ] **Step 5: Seed the complete registry**

Create all 71 rows from Appendix A. Set only these five rows to `enabled = true`:

```text
paypal/paypal-js
paypal-examples/v6-web-sdk-sample-integration
braintree/braintree_ios
stripe/stripe-ios
adyen/adyen-web
```

Every other row is present with `enabled = false`, an explicit priority, and an explicit version strategy.

- [ ] **Step 6: Run focused and full tests**

Run:

```bash
python3 -m unittest tests.test_toml_compat tests.test_github_registry tests.test_fetch_psp -v
python3 -m unittest discover -s tests -v
```

Expected: focused tests pass; the full suite reports at least the existing 45 tests plus the new tests with zero failures.

- [ ] **Step 7: Commit the registry foundation**

```bash
git add scripts/toml_compat.py scripts/github_registry.py scripts/fetch_psp.py tracking/github/repo-registry.toml tests/test_toml_compat.py tests/test_github_registry.py tests/test_fetch_psp.py
git commit -m "feat: add github repository registry"
```

---

### Task 3: Resolve Git References Against Local Test Repositories

**Files:**
- Create: `scripts/github_git.py`
- Create: `tests/github_test_support.py`
- Create: `tests/test_github_git.py`

**Interfaces:**
- Consumes: `RepoConfig`, a temporary clone path, and a selector such as `default-branch`, `tag:v9.1.0`, `commit:<sha>`, or `package:@scope/name@9`.
- Produces: `run_git(args, cwd=None) -> str`, `clone_repository(config, destination) -> None`, `fetch_required_refs(config: RepoConfig, clone_path: Path, selectors: Sequence[str]) -> None`, `inspect_repository(config, clone_path) -> RepoInspection`, and `resolve_ref(config, inspection, selector) -> ResolvedRef`.

- [ ] **Step 1: Write the local Git fixture builder**

Provide this test interface:

```python
def create_git_repo(root: Path) -> Path:
    repo = root / "upstream"
    repo.mkdir()
    subprocess.run(["git", "init", "-b", "main", str(repo)], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.name", "Wiki Test"], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.email", "wiki@example.test"], check=True)
    return repo

def commit_file(repo: Path, relative: str, content: str, message: str) -> str:
    path = repo / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    subprocess.run(["git", "-C", str(repo), "add", relative], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-m", message], check=True)
    return subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        check=True, text=True, capture_output=True,
    ).stdout.strip()
```

- [ ] **Step 2: Write failing ref-resolution tests**

Cover default branch, semver tags, same-SHA aliases, an exact commit, package tags, ambiguous bare majors, missing refs, submodule detection, and `.gitattributes` LFS detection. Assert a missing or ambiguous selector raises `RefResolutionError` and never falls back silently.

```python
class GitResolutionTests(unittest.TestCase):
    def test_same_sha_tags_are_aliases(self):
        sha = commit_file(self.repo, "README.md", "one\n", "initial")
        tag(self.repo, "v1.0.0")
        tag(self.repo, "release-1")
        inspection = inspect_repository(self.config(), self.repo)
        resolved = resolve_ref(self.config(), inspection, "tag:v1.0.0")
        self.assertEqual(sha, resolved.sha)
        self.assertEqual(("release-1", "v1.0.0"), resolved.aliases)

    def test_bare_monorepo_major_is_rejected(self):
        inspection = self.monorepo_with_two_v9_packages()
        with self.assertRaisesRegex(RefResolutionError, "ambiguous"):
            resolve_ref(self.monorepo_config(), inspection, "v9")
```

- [ ] **Step 3: Run tests to verify failure**

Run:

```bash
python3 -m unittest tests.test_github_git -v
```

Expected: import failure because `github_git.py` does not exist.

- [ ] **Step 4: Implement Git records and subprocess safety**

Define:

```python
@dataclass(frozen=True)
class ResolvedRef:
    repo_id: str
    ref_kind: str
    ref_name: str
    sha: str
    version: str
    aliases: Tuple[str, ...]
    upstream_commit_time: str
    release_published_at: Optional[str]

@dataclass(frozen=True)
class RepoInspection:
    default_branch: str
    refs: Tuple[ResolvedRef, ...]
    packages: Tuple[str, ...]
    has_submodules: bool
    has_lfs: bool
```

Use argument lists with `subprocess.run(check=True, text=True, capture_output=True)`. Never invoke a shell. Convert `CalledProcessError` into `GitCommandError` containing the command, exit code, and bounded stderr.

- [ ] **Step 5: Implement exact strategy resolution**

Parse semantic versions with numeric and prerelease identifiers, preserving SemVer precedence: a stable version sorts above its prereleases and numeric prerelease identifiers compare numerically. Exact prerelease selectors match only that prerelease. Package selectors must include a package namespace. Sort aliases before returning them. Clone with `git clone --filter=blob:none --no-checkout --no-tags`; `fetch_required_refs` may list remote tag metadata to resolve package or major selectors, then fetches only the selected tag refspecs or exact commit objects and never downloads all ref objects.

- [ ] **Step 6: Run tests and commit**

```bash
python3 -m unittest tests.test_github_git -v
python3 -m unittest discover -s tests -v
git add scripts/github_git.py tests/github_test_support.py tests/test_github_git.py
git commit -m "feat: resolve github repository versions"
```

Expected: all tests pass and no test contacts the network.

---

### Task 4: Create Immutable Curated Snapshots

**Files:**
- Create: `scripts/github_snapshot.py`
- Create: `tests/test_github_snapshot.py`

**Interfaces:**
- Consumes: `RepoConfig`, `ResolvedRef`, a checked-out repository, collection date, and optional prior changed paths.
- Produces: `select_key_files(config: RepoConfig, repo_root: Path, changed_paths: Sequence[str] = ()) -> SelectionResult`, `build_snapshot(config: RepoConfig, ref: ResolvedRef, repo_root: Path, raw_root: Path, staging_root: Path, collection_date: str, prior_snapshot: Optional[str] = None, capture_kind: str = "canonical") -> SnapshotRecord`, `validate_staged_snapshot(record: SnapshotRecord) -> List[str]`, and `promote_snapshot(record: SnapshotRecord) -> Path`.

- [ ] **Step 1: Write failing selection and immutability tests**

Cover required defaults, registry `key_paths`, excluded lock/build/vendor files, binary exclusion, per-file limits, total limits, exact byte hashes, same-target rejection, and supplements.

```python
def test_snapshot_copies_exact_bytes_and_keeps_diff_outside_raw(self):
    original = b"# README\n\x00not-selected"
    selected = b"# README\n"
    (repo / "README.md").write_bytes(selected)
    record = build_snapshot(config, resolved, repo, raw_root, staging_root, "2026-07-14")
    copied = record.staging_path / "files" / "README.md"
    self.assertEqual(selected, copied.read_bytes())
    self.assertFalse(any(path.name.endswith(".patch") for path in record.staging_path.rglob("*")))

def test_existing_snapshot_is_never_overwritten(self):
    target = raw_root / "paypal" / "paypal-js" / "snapshots" / "2026-07-14-v10-a1b2c3d"
    target.mkdir(parents=True)
    with self.assertRaisesRegex(SnapshotError, "already exists"):
        promote_snapshot(staged, target)
```

- [ ] **Step 2: Run tests to verify failure**

```bash
python3 -m unittest tests.test_github_snapshot -v
```

Expected: import failure because `github_snapshot.py` does not exist.

- [ ] **Step 3: Implement snapshot records and key-file policy**

Define:

```python
@dataclass(frozen=True)
class SnapshotFile:
    path: str
    sha256: str
    size: int
    purpose: str

@dataclass(frozen=True)
class SelectionResult:
    selected: Tuple[Path, ...]
    excluded: Tuple[Tuple[str, str], ...]
    total_bytes: int

@dataclass(frozen=True)
class SnapshotRecord:
    repo_id: str
    ref: ResolvedRef
    capture_kind: str
    capture_revision: int
    collection_date: str
    staging_path: Path
    target_path: Path
    files: Tuple[SnapshotFile, ...]
```

Selection order is explicit registry paths, then README/changelog/migration/package/API-spec files, then changed public entrypoints and examples. Sort every path. Use MIME-independent binary detection based on NUL bytes in the first 8 KiB.

- [ ] **Step 4: Render and validate `snapshot.md`**

The manifest must include repository URL, ID, company, type, ref kind/name, full SHA, aliases, capture kind/revision, collection and upstream dates, prior snapshot, and a complete saved/excluded file table. Validate every listed file hash and ensure every copied file is listed exactly once.

- [ ] **Step 5: Promote atomically and handle supplements**

Create staging below `raw/github/.staging/` so `Path.replace()` remains on one filesystem. Validate before promotion. For a canonical SHA already present, return unchanged. An explicit supplement chooses the next free `-rN` directory and records `capture_kind = "supplement"`.

- [ ] **Step 6: Run tests and commit**

```bash
python3 -m unittest tests.test_github_snapshot -v
python3 -m unittest discover -s tests -v
git add scripts/github_snapshot.py tests/test_github_snapshot.py
git commit -m "feat: create immutable github snapshots"
```

---

### Task 5: Build Version Indexes and Ingest Packets

**Files:**
- Create: `scripts/github_packets.py`
- Create: `tests/test_github_packets.py`

**Interfaces:**
- Consumes: immutable `SnapshotRecord` values, repository Git history, and existing `version-index.json`.
- Produces: `load_version_index(path: Path, repo_id: str) -> VersionIndex`, `record_snapshot(index: VersionIndex, snapshot: SnapshotRecord) -> VersionIndex`, `select_prior(index: VersionIndex, ref: ResolvedRef) -> Optional[VersionEntry]`, `build_baseline_packet(config: RepoConfig, current: SnapshotRecord, packet_root: Path) -> PacketRecord`, `build_delta_packet(config: RepoConfig, prior: VersionEntry, current: SnapshotRecord, repo_root: Path, packet_root: Path) -> PacketRecord`, and `build_comparison_packet(config: RepoConfig, prior: VersionEntry, current: VersionEntry, repo_root: Path, packet_root: Path) -> PacketRecord`.

- [ ] **Step 1: Write failing version-index tests**

Assert one canonical version snapshot per SHA, alias deduplication, package-namespace prior selection, branch prior selection, and supplement recording without a new version.

```python
def test_aliases_share_one_version_entry(self):
    first = record_snapshot(empty_index(), snapshot(sha="a" * 40, aliases=("v1",)))
    second = record_snapshot(first, snapshot(sha="a" * 40, aliases=("stable", "v1")))
    self.assertEqual(1, len(second.versions))
    self.assertEqual(("stable", "v1"), second.versions[0].aliases)
```

- [ ] **Step 2: Write failing packet tests**

Create two local commits with added, modified, renamed, and deleted files. Require `packet.json`, `ingest-packet.md`, `changed-files.txt`, and `source-diff.patch` under tracking. Assert no `.patch` appears under raw and the packet required-reading paths all exist.

```python
def test_delta_packet_records_deletion_and_rename(self):
    packet = build_delta_packet(config, prior, current, repo, packet_root)
    self.assertIn("D\tdocs/removed.md", packet.changed_files)
    self.assertTrue(any(line.startswith("R") for line in packet.changed_files))
    self.assertEqual("awaiting-review", packet.initial_state)
```

- [ ] **Step 3: Run tests to verify failure**

```bash
python3 -m unittest tests.test_github_packets -v
```

Expected: import failure because `github_packets.py` does not exist.

- [ ] **Step 4: Implement immutable index and packet records**

Define:

```python
@dataclass(frozen=True)
class VersionEntry:
    ref_kind: str
    ref_name: str
    version: str
    sha: str
    aliases: Tuple[str, ...]
    snapshot_path: str
    collection_date: str
    package: str
    capture_kind: str

@dataclass(frozen=True)
class VersionIndex:
    repo_id: str
    versions: Tuple[VersionEntry, ...]

@dataclass(frozen=True)
class PacketRecord:
    packet_id: str
    repo_id: str
    packet_type: str
    from_snapshot: str
    to_snapshot: str
    required_reading: Tuple[str, ...]
    changed_files: Tuple[str, ...]
    initial_state: str
    directory: Path
```

Write JSON with sorted keys and a final newline. Write to a temporary sibling and replace generated state atomically.

- [ ] **Step 5: Generate source diffs and packet Markdown**

Use `git diff --find-renames --no-ext-diff --no-textconv <from> <to> -- <selected paths>`. Exclude binary and ignored high-churn paths. The packet must distinguish evidence from generated guidance and list the exact required reading order.

- [ ] **Step 6: Run tests and commit**

```bash
python3 -m unittest tests.test_github_packets -v
python3 -m unittest discover -s tests -v
git add scripts/github_packets.py tests/test_github_packets.py
git commit -m "feat: generate github ingest packets"
```

---

### Task 6: Add State Reporting and the Public CLI

**Files:**
- Create: `scripts/github_reporting.py`
- Create: `scripts/collect_github_repos.py`
- Create: `tests/test_github_reporting.py`
- Create: `tests/test_collect_github_repos.py`

**Interfaces:**
- Consumes: registry selections, Git/snapshot/packet modules, run events, and packet transition requests.
- Produces: `append_event(path: Path, event: Mapping[str, object]) -> None`, `validate_collection_run(events: Sequence[Mapping[str, object]]) -> int`, `transition_packet(current: str, requested: str) -> str`, `render_collection_status(repos: Sequence[RepoConfig], events: Sequence[Mapping[str, object]]) -> str`, `render_ingest_status(packets: Sequence[PacketRecord], states: Mapping[str, str]) -> str`, `collect_one(root: Path, config: RepoConfig, selectors: Sequence[str]) -> CollectionResult`, `compare_one(root: Path, config: RepoConfig, from_selector: str, to_selector: str) -> PacketRecord`, and `main(argv: Optional[Sequence[str]] = None) -> int`.

- [ ] **Step 1: Write failing state-machine tests**

Use these exact transition sets:

```python
COLLECTION_TERMINAL = {
    "unchanged", "collected-baseline", "collected-change", "retry-pending", "failed"
}
PACKET_TRANSITIONS = {
    "awaiting-review": {"approved", "rejected"},
    "approved": {"ingesting", "rejected"},
    "ingesting": {"ingested", "validation-failed"},
    "validation-failed": {"approved", "rejected"},
    "ingested": set(),
    "rejected": set(),
}
```

Assert an invalid transition raises `StateTransitionError`. Assert collection reconciliation fails when one selected repo/ref lacks a terminal event.

- [ ] **Step 2: Write failing CLI tests**

Test these forms with mocked Git operations and a temporary root:

```text
collect --all --dry-run
collect --company paypal --dry-run
collect --repo paypal/paypal-js --ref default-branch
compare --repo paypal/paypal-js --from package:@paypal/react-paypal-js@8 --to package:@paypal/react-paypal-js@10
prepare --repo paypal/paypal-js --ref default-branch
status
packet-state --repo paypal/paypal-js --packet <packet-id> --from awaiting-review --to approved
```

Dry-run may resolve and report but must not create `raw/` or mutate generated state.

`--all` and `--company` select enabled rows by default. An explicit `--repo` may select a disabled row because it is an intentional one-repository request. `--include-disabled` is required to batch-select disabled rows.

- [ ] **Step 3: Run tests to verify failure**

```bash
python3 -m unittest tests.test_github_reporting tests.test_collect_github_repos -v
```

Expected: import failures because the modules do not exist.

- [ ] **Step 4: Implement append-only events and generated dashboards**

`append_event` writes one sorted JSON object plus newline using append mode. Packet history lives at `tracking/github/repos/<company>/<repo>/packets/<packet-id>/state-events.jsonl`; `packet.json` remains the immutable packet contract. Regenerate Markdown and `status.json` from registry, version indexes, packet contracts, and the latest valid events.

- [ ] **Step 5: Implement orchestration with cleanup**

Use `tempfile.TemporaryDirectory(prefix="wiki-github-")` for clones. Record one terminal event for every selected repo/ref even when resolution or clone fails. Remove staging after any failure. Return `1` for unreconciled runs or validation failure, `2` for CLI/registry misuse, and `0` only for a reconciled successful command.

- [ ] **Step 6: Run focused and full tests**

```bash
python3 -m unittest tests.test_github_reporting tests.test_collect_github_repos -v
python3 -m unittest discover -s tests -v
```

Expected: all tests pass without network access.

- [ ] **Step 7: Commit the CLI**

```bash
git add scripts/github_reporting.py scripts/collect_github_repos.py tests/test_github_reporting.py tests/test_collect_github_repos.py
git commit -m "feat: add github collection cli and monitoring"
```

---

### Task 7: Validate Snapshots, Packets, and Wiki Links

**Files:**
- Create: `scripts/github_validation.py`
- Create: `scripts/validate_github_collection.py`
- Create: `tests/test_github_validation.py`
- Modify: `tests/test_validate_wiki.py`
- Modify: `scripts/validate_wiki.py` only if a failing test proves a missing nested-path behavior.

**Interfaces:**
- Consumes: `raw/github/`, `tracking/github/`, company-first GitHub source pages, version indexes, packet state events, and generated status.
- Produces: `inspect_github(root) -> GitHubReport`, `validate_github(report) -> List[str]`, and a CLI that returns nonzero for structural errors while reporting awaiting-ingest packets as informational.

- [ ] **Step 1: Write failing structural tests**

Cover valid snapshots, bad hashes, manifest/file disagreement, duplicate canonical SHA snapshots, valid supplements, missing required-reading files, patch files under raw, invalid packet transitions, source `raw_files` ordering, path-qualified `snapshot.md` links, status disagreement, and pending packets.

```python
def test_pending_packet_is_informational_not_error(self):
    report = inspect_github(self.make_valid_tree(packet_state="awaiting-review"))
    self.assertEqual(1, len(report.pending_packets))
    self.assertEqual([], validate_github(report))

def test_generated_patch_under_raw_is_rejected(self):
    root = self.make_valid_tree()
    (root / "raw/github/paypal/paypal-js/snapshots/x/source-diff.patch").write_text("diff")
    errors = validate_github(inspect_github(root))
    self.assertTrue(any("generated patch under raw" in error for error in errors))
```

- [ ] **Step 2: Run tests to verify failure**

```bash
python3 -m unittest tests.test_github_validation -v
```

Expected: import failure because `github_validation.py` does not exist.

- [ ] **Step 3: Implement report records and validation**

Define a frozen `GitHubReport` containing snapshot paths, packet paths, pending packet IDs, source records, version indexes, dashboard records, and inspection errors. Reuse `split_frontmatter`, `parse_frontmatter`, and `WIKILINK_RE` from `validate_wiki.py`; do not duplicate YAML parsing.

- [ ] **Step 4: Extend nested link regression coverage**

Add a source fixture whose two raw entries end in `snapshot.md` but use full path-qualified wikilinks. Assert `validate_wiki.check_file` resolves both. Modify `validate_wiki.py` only if this test fails.

- [ ] **Step 5: Run validators and all tests**

```bash
python3 -m unittest tests.test_github_validation tests.test_validate_wiki -v
python3 scripts/validate_github_collection.py
python3 -m unittest discover -s tests -v
```

Expected before live collection: validator reports 0 new snapshots and 0 pending packets, with no structural errors.

- [ ] **Step 6: Commit validation**

```bash
git add scripts/github_validation.py scripts/validate_github_collection.py scripts/validate_wiki.py tests/test_github_validation.py tests/test_validate_wiki.py
git commit -m "feat: validate github collection artifacts"
```

---

### Task 8: Prove the Complete Pipeline with a Local Git Repository

**Files:**
- Modify: `tests/test_collect_github_repos.py`
- Create generated baseline files: `tracking/github/status.json`, `tracking/github/collection-status.md`, `tracking/github/ingest-status.md`

**Interfaces:**
- Consumes: the full registry and every deterministic core module.
- Produces: one local end-to-end test and clean empty production dashboards before live collection.

- [ ] **Step 1: Write a failing local end-to-end test**

The test must create a local upstream repository, run baseline collection, rerun unchanged, add/rename/delete files, run changed collection, generate a comparison, and transition one packet through approval and ingest states.

```python
def test_local_end_to_end_baseline_unchanged_change_and_compare(self):
    config = self.local_config(url=str(upstream))
    first_sha = commit_file(upstream, "README.md", "first\n", "first")
    first = collect_one(root, config, ("default-branch",))
    unchanged = collect_one(root, config, ("default-branch",))
    second_sha = commit_file(upstream, "README.md", "second\n", "second")
    second = collect_one(root, config, ("default-branch",))
    comparison = compare_one(root, config, first_sha, second_sha)
    self.assertEqual("collected-baseline", first.state)
    self.assertEqual("unchanged", unchanged.state)
    self.assertEqual("collected-change", second.state)
    self.assertEqual("comparison", comparison.packet_type)
    self.assertEqual(2, len(list((root / "raw/github/test/demo/snapshots").iterdir())))
```

The test constructs `RepoConfig` directly with a local path. Production registry loading continues to reject non-HTTPS GitHub URLs; no test-only CLI escape hatch is added.

- [ ] **Step 2: Run the test and fix only orchestration defects**

```bash
python3 -m unittest tests.test_collect_github_repos.CollectGitHubReposTests.test_local_end_to_end_baseline_unchanged_change_and_compare -v
```

Expected: PASS. Any failure must be fixed in the owning module with a focused regression assertion before proceeding.

- [ ] **Step 3: Generate empty production dashboards**

```bash
python3 scripts/collect_github_repos.py status
python3 scripts/validate_github_collection.py
```

Expected: 71 registered repositories, 5 enabled pilots, 0 collected versions, 0 ingest packets, and no validation errors.

- [ ] **Step 4: Run the complete local gate**

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all tests and validators pass.

- [ ] **Step 5: Commit the local proof**

```bash
git add tests/test_collect_github_repos.py tracking/github/status.json tracking/github/collection-status.md tracking/github/ingest-status.md
git commit -m "test: prove github collection pipeline locally"
```

---

### Task 9: Collect the `paypal/paypal-js` Pilot and Stop

**Files:**
- Modify when exact selectors are discovered: `tracking/github/repo-registry.toml`
- Create: collector-named children under `raw/github/paypal/paypal-js/snapshots/`
- Create: `tracking/github/repos/paypal/paypal-js/`
- Create: `tracking/github/runs/<run-id>/`
- Regenerate: `tracking/github/status.json`, `tracking/github/collection-status.md`, `tracking/github/ingest-status.md`

**Interfaces:**
- Consumes: live `paypal/paypal-js` refs and the enabled registry row.
- Produces: immutable current, v9, and v8 package-qualified snapshots plus reviewable packets; no wiki ingest.

- [ ] **Step 1: Read collection rules and run a no-write preflight**

```bash
python3 scripts/collect_github_repos.py collect --repo paypal/paypal-js --dry-run
```

Expected: exact default-branch and package-qualified ref resolutions are printed; no `raw/github/paypal/paypal-js/` directory is created.

- [ ] **Step 2: Resolve package ambiguity explicitly**

Confirm whether the requested v10/v9/v8 lines belong to `@paypal/react-paypal-js`, `@paypal/paypal-js`, or another package. Update `requested_refs` to exact package selectors or exact tags. Never retain a bare `v9` selector when multiple packages match.

- [ ] **Step 3: Run the live collection**

```bash
python3 scripts/collect_github_repos.py collect --repo paypal/paypal-js
```

Expected: every selected ref ends as `collected-baseline`, `collected-change`, or `unchanged`; accepted snapshots are immutable and each new packet starts in `awaiting-review`.

- [ ] **Step 4: Validate and inspect collection size**

```bash
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py status
git diff --check
```

Inspect `snapshot.md`, every packet's required-reading list, total bytes, excluded files, submodule/LFS notes, and secret-scan findings. If a packet is too large for complete reading, adjust registry key paths and create a new explicit supplement rather than editing accepted raw.

- [ ] **Step 5: Commit collection evidence**

```bash
git add tracking/github/repo-registry.toml raw/github/paypal/paypal-js tracking/github/repos/paypal/paypal-js tracking/github/runs tracking/github/status.json tracking/github/collection-status.md tracking/github/ingest-status.md
git commit -m "data: collect paypal js version pilot"
```

- [ ] **Step 6: HARD USER GATE**

Share the run manifest, resolved versions, snapshot sizes, required-reading files, and validation results. Stop. Do not approve a packet, update a wiki source page, or begin another pilot ingest until the user explicitly kicks off ingest.

---

### Task 10: Ingest PayPal JS Packets Serially After Approval

**Files:**
- Create or move: `wiki/sources/paypal/github/source-github-paypal-js.md`
- Create when materially supported: `wiki/analyses/paypal/github/analysis-paypal-js-v8-v9-v10.md`
- Modify: `wiki/paypal-index.md`
- Create or modify: `wiki/paypal-log.md`
- Modify as evidence requires: `wiki/companies/paypal.md`, relevant `wiki/concepts/paypal-*.md`
- Modify after backlink audit: legacy `wiki/sources/source-github-paypal-js-v6.md`, `wiki/sources/source-github-react-paypal-js-v8.md`
- Regenerate: `tracking/github/ingest-status.md`, `tracking/github/status.json`

**Interfaces:**
- Consumes: one user-approved packet at a time and its complete required-reading set.
- Produces: one stable current repository source page, material version history, optional version analysis, ingest receipts, and provider navigation/log entries.

- [ ] **Step 1: Approve exactly one packet**

```bash
python3 scripts/collect_github_repos.py packet-state --repo paypal/paypal-js --packet <approved-packet-id> --from awaiting-review --to approved
```

Use the exact packet ID from Task 9 in place of the shell token. Confirm all other packets remain `awaiting-review`.

- [ ] **Step 2: Read the complete packet evidence**

Read `ingest-packet.md`, every referenced `snapshot.md`, and every required raw file end to end. Record 3-5 exact quotes with paths and line ranges in the ingest receipt before any wiki write.

- [ ] **Step 3: Perform concept audit first**

Search all existing PayPal JS SDK, React SDK, checkout, card-fields, Venmo, and migration concepts. Update or create concepts before updating the stable source page.

- [ ] **Step 4: Enter ingesting state and update the stable source page**

Transition the approved packet before the first canonical wiki write:

```bash
python3 scripts/collect_github_repos.py packet-state --repo paypal/paypal-js --packet <approved-packet-id> --from approved --to ingesting
```

Move or create the canonical page at `wiki/sources/paypal/github/source-github-paypal-js.md`. Preserve `date_ingested`, add `date_updated`, list ingested snapshot anchors newest first, use path-qualified raw links, and add concise material entries under `## Version history`.

- [ ] **Step 5: Finish the complete one-packet cycle**

Update company/concepts, check contradictions, update `wiki/paypal-index.md`, append `wiki/paypal-log.md`, run validation, write the receipt, and transition the packet:

```bash
python3 scripts/validate_wiki.py wiki/sources/paypal/github/source-github-paypal-js.md wiki/companies/paypal.md
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py packet-state --repo paypal/paypal-js --packet <approved-packet-id> --from ingesting --to ingested
```

If validation fails, transition from `ingesting` to `validation-failed`, fix the current cycle, regain approval, and do not open another packet.

- [ ] **Step 6: Repeat Steps 1-5 for the next historical packet**

Process v9 and v8 independently, one complete packet per cycle. Commit after each successful packet:

```bash
git add wiki tracking/github/repos/paypal/paypal-js tracking/github/ingest-status.md tracking/github/status.json
git commit -m "wiki: ingest paypal js <resolved-version> snapshot"
```

Replace `<resolved-version>` with the exact package version recorded in the packet.

- [ ] **Step 7: Create the material comparison analysis**

Generate explicit v8-to-v9 and v9-to-v10 comparison packets, approve and read each independently, then create or update `wiki/analyses/paypal/github/analysis-paypal-js-v8-v9-v10.md`. Cite the canonical source page and path-qualified snapshots. Keep mechanical file lists and patches in tracking.

- [ ] **Step 8: Audit duplicate source pages**

Use `rg` to find every backlink to `source-github-paypal-js-v6` and `source-github-react-paypal-js-v8`. Merge unique evidence into the canonical page, replace old pages with concise compatibility pages only when removing them would break meaningful historical identity, and never alter legacy raw stubs.

- [ ] **Step 9: Run the serial-ingest gate and commit**

```bash
python3 scripts/validate_wiki.py wiki/sources/paypal/github/source-github-paypal-js.md wiki/analyses/paypal/github/analysis-paypal-js-v8-v9-v10.md wiki/paypal-index.md wiki/paypal-log.md
python3 scripts/validate_github_collection.py
python3 -m unittest discover -s tests -v
git diff --check
git add wiki tracking/github
git commit -m "wiki: analyze paypal js major versions"
```

Expected: one canonical repo source page, validated material history, and no packet left falsely marked `ingested` after a failed validation.

---

### Task 11: Collect the Remaining Cross-Company Pilots

**Files:**
- Create: raw and tracking artifacts for the enabled sample, Braintree, Stripe, and Adyen pilot rows.
- Regenerate: all GitHub dashboards and run manifests.

**Interfaces:**
- Consumes: accepted PayPal JS pilot behavior and enabled registry rows.
- Produces: baseline/delta/comparison packets proving the workflow is provider-neutral; no automatic wiki ingest.

- [ ] **Step 1: Collect one repository at a time**

Run and validate in this order:

```bash
python3 scripts/collect_github_repos.py collect --repo paypal-examples/v6-web-sdk-sample-integration
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py collect --repo braintree/braintree_ios
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py collect --repo stripe/stripe-ios
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py collect --repo adyen/adyen-web
python3 scripts/validate_github_collection.py
```

- [ ] **Step 2: Generate one previous-major comparison per SDK where resolvable**

Use package-qualified or exact tag selectors from each version index. A missing historical ref records an explicit failure; it never silently compares against another ref.

- [ ] **Step 3: Verify provider-neutral results**

Confirm key-file selection, size limits, release/tag fallback, default-branch behavior, generated diffs, and dashboards work without provider-specific branches in Python code.

- [ ] **Step 4: Commit each repository independently**

Commit each completed repository with its exact path and message:

```bash
git add raw/github/paypal/v6-web-sdk-sample-integration tracking/github/repos/paypal/v6-web-sdk-sample-integration tracking/github/runs tracking/github/status.json tracking/github/collection-status.md tracking/github/ingest-status.md
git commit -m "data: collect paypal v6 web sdk sample pilot"

git add raw/github/braintree/braintree_ios tracking/github/repos/braintree/braintree_ios tracking/github/runs tracking/github/status.json tracking/github/collection-status.md tracking/github/ingest-status.md
git commit -m "data: collect braintree ios pilot"

git add raw/github/stripe/stripe-ios tracking/github/repos/stripe/stripe-ios tracking/github/runs tracking/github/status.json tracking/github/collection-status.md tracking/github/ingest-status.md
git commit -m "data: collect stripe ios pilot"

git add raw/github/adyen/adyen-web tracking/github/repos/adyen/adyen-web tracking/github/runs tracking/github/status.json tracking/github/collection-status.md tracking/github/ingest-status.md
git commit -m "data: collect adyen web pilot"
```

Do not combine repositories into one commit.

- [ ] **Step 5: Stop at the collection boundary**

Share the consolidated collection status and ingest queue. Every packet remains `awaiting-review` unless the user separately approves its ingest.

---

### Task 12: Migrate Legacy GitHub Source Pages to Company-First Paths

**Files:**
- Create: `scripts/migrate_github_wiki_layout.py`
- Create: `tests/test_migrate_github_wiki_layout.py`
- Move on apply: `wiki/sources/source-github-*.md` to `wiki/sources/<company>/github/`
- Modify as derived: provider indexes and root navigation only where paths are written explicitly.

**Interfaces:**
- Consumes: legacy source frontmatter, `raw_files` stubs, `<!-- Repo: https://github.com/owner/repo -->` headers, and owner-to-company registry mapping.
- Produces: `plan_source_moves(root, registry) -> Tuple[SourceMove, ...]`, `validate_source_moves(moves) -> List[str]`, and `apply_source_moves(moves) -> None` with `--dry-run` as the default CLI behavior.

- [ ] **Step 1: Write failing owner and move tests**

Cover PayPal, `paypal-examples`, Stripe, mixed-case Adyen, unknown owner, destination collision, duplicate repo sources, dry-run, apply, and second-run idempotence.

```python
def test_legacy_stub_owner_maps_to_company_directory(self):
    self.write_stub("github-paypal-ios.md", "https://github.com/paypal/paypal-ios")
    source = self.write_source("source-github-paypal-ios.md", "github-paypal-ios.md")
    moves = plan_source_moves(self.root, self.registry())
    self.assertEqual(source, moves[0].source)
    self.assertEqual(
        self.root / "wiki/sources/paypal/github/source-github-paypal-ios.md",
        moves[0].destination,
    )
```

- [ ] **Step 2: Run tests to verify failure**

```bash
python3 -m unittest tests.test_migrate_github_wiki_layout -v
```

Expected: import failure because the migration module does not exist.

- [ ] **Step 3: Implement deterministic planning and apply**

Read the first raw stub named in `raw_files`, parse its exact GitHub URL, normalize owner/repo for lookup, and derive company from the registry. Unknown or conflicting ownership is an error and prevents all moves. Use `Path.replace` only after validating the entire move set. Do not modify source content merely because its path changes.

- [ ] **Step 4: Run dry-run on the real wiki**

```bash
python3 scripts/migrate_github_wiki_layout.py --dry-run
```

Expected: every remaining flat legacy GitHub source page is classified. The pre-pilot baseline is 23 pages; pages already moved by serial pilot ingest are skipped. Duplicate `paypal/paypal-js` source identities are reported for semantic audit but do not cause raw mutation.

- [ ] **Step 5: Apply and validate**

```bash
python3 scripts/migrate_github_wiki_layout.py --apply
python3 scripts/validate_wiki.py
python3 scripts/validate_github_collection.py
python3 -m unittest discover -s tests -v
```

Expected: source basenames remain unchanged, Obsidian links resolve, provider indexes retain their annotated entries, and all validators pass except explicitly documented pre-existing global wiki findings.

- [ ] **Step 6: Commit the source layout migration**

```bash
git add scripts/migrate_github_wiki_layout.py tests/test_migrate_github_wiki_layout.py wiki/sources wiki/paypal-index.md wiki/stripe-index.md wiki/index.md
git commit -m "refactor: group github sources by company"
```

---

### Task 13: Split the Root Log Deterministically

**Files:**
- Create: `scripts/migrate_wiki_logs.py`
- Create: `tests/test_migrate_wiki_logs.py`
- Modify: `wiki/log.md`
- Create or regenerate: `wiki/paypal-log.md`, `wiki/stripe-log.md`, `wiki/braintree-log.md`, `wiki/adyen-log.md`
- Preserve and append safely: `wiki/metronome-log.md`

**Interfaces:**
- Consumes: root log blocks beginning with `## `, provider names, GitHub repo/source ownership, and existing provider logs.
- Produces: `parse_log_blocks(text) -> Tuple[LogBlock, ...]`, `classify_log_block(block, ownership) -> str`, `render_provider_log(company, blocks) -> str`, and a dry-run/apply CLI with lossless reconciliation.

- [ ] **Step 1: Write failing parsing and preservation tests**

Cover provider headings, lowercase repo headings, PayPal appearing inside a Stripe product title, GitHub source-path ownership, cross-company entries, unclassified entries, preamble preservation, newest-first order, exact block text, and idempotence.

```python
def test_stripe_paypal_product_entry_stays_with_stripe(self):
    block = LogBlock(
        heading="## [2026-05-13] ingest | Stripe - PayPal Subscription Setup",
        body="- Raw: `raw/stripe-subscriptions-paypal-2026.md`\n",
    )
    self.assertEqual("stripe", classify_log_block(block, self.ownership()))

def test_reconciliation_is_lossless(self):
    result = split_logs(self.sample_log(), self.ownership())
    original = tuple(parse_log_blocks(self.sample_log()))
    emitted = tuple(block for blocks in result.values() for block in blocks)
    self.assertCountEqual(original, emitted)
```

- [ ] **Step 2: Run tests to verify failure**

```bash
python3 -m unittest tests.test_migrate_wiki_logs -v
```

Expected: import failure because `migrate_wiki_logs.py` does not exist.

- [ ] **Step 3: Implement classification precedence**

Use this order:

1. Explicit leading provider token after `|` in the heading.
2. Owned raw/source path in the block body.
3. GitHub owner/repository in the heading or body.
4. Exactly one provider token across heading and body.
5. Root log for zero or multiple matches.

Require this invariant before apply:

```text
input block count = root block count + sum(provider block counts)
```

Also hash exact block text before and after splitting and reject any mismatch.

- [ ] **Step 4: Dry-run the real 8,862-line log**

```bash
python3 scripts/migrate_wiki_logs.py --dry-run
```

Expected: counts by provider plus an explicit root/unclassified count; zero lost or duplicated blocks; no files changed.

- [ ] **Step 5: Apply and validate**

```bash
python3 scripts/migrate_wiki_logs.py --apply
python3 scripts/validate_wiki.py wiki/paypal-log.md wiki/stripe-log.md wiki/braintree-log.md wiki/adyen-log.md wiki/metronome-log.md
python3 -m unittest tests.test_migrate_wiki_logs -v
git diff --check
```

Expected: provider logs have valid `type: log` frontmatter, root log becomes a router plus cross-company/unclassified history, and all original blocks exist exactly once.

- [ ] **Step 6: Commit the log split**

```bash
git add scripts/migrate_wiki_logs.py tests/test_migrate_wiki_logs.py wiki/log.md wiki/paypal-log.md wiki/stripe-log.md wiki/braintree-log.md wiki/adyen-log.md wiki/metronome-log.md
git commit -m "refactor: split wiki logs by company"
```

---

## Final Verification

- [ ] Run the complete unit suite:

```bash
python3 -m unittest discover -s tests -v
```

- [ ] Run deterministic validators:

```bash
python3 scripts/validate_github_collection.py
python3 scripts/validate_metronome_capsule.py
python3 scripts/validate_wiki.py
```

Record GitHub and Metronome validator success separately from any documented pre-existing global wiki findings.

- [ ] Check repository state and immutable boundaries:

```bash
git diff --check
git status --short
git diff --name-only -- raw
```

Confirm every changed `raw/github/` path is a newly added immutable snapshot and no legacy raw path was modified.

- [ ] Review generated dashboards:

```bash
python3 scripts/collect_github_repos.py status
python3 scripts/validate_github_collection.py
```

Confirm registry, version indexes, collection status, ingest status, packet states, provider source pages, provider indexes, and provider logs agree.

## Appendix A: Initial Registry Inventory

Common policy by strategy:

| Strategy | `track` | Default frequency |
| --- | --- | --- |
| `monorepo-packages` | `releases-and-default-branch` | weekly for tier1 |
| `semver-tags` | `releases-and-default-branch` | weekly for tier1, monthly for tier2/3 |
| `github-release` | `releases-and-default-branch` | monthly |
| `commit` | `default-branch` | monthly for tier1/2, on-demand for tier3 |

Only rows marked `yes` are enabled for the pilot.

The `Repository` column preserves the case-sensitive GitHub URL path. The registry `id` is its lowercase owner/repository form; `url` preserves the exact case shown here.

### PayPal

| Repository | Type | Tier | Strategy | Enabled |
| --- | --- | --- | --- | --- |
| `paypal/paypal-messaging-components` | web-component | tier1 | semver-tags | no |
| `paypal/paypal-checkout-components` | web-component | tier1 | semver-tags | no |
| `paypal/paypal-android` | mobile-sdk | tier1 | semver-tags | no |
| `paypal/paypal-sdk-release` | release-index | tier2 | github-release | no |
| `paypal/paypal-js` | web-sdk | tier1 | monorepo-packages | yes |
| `paypal/paypal-ios` | mobile-sdk | tier1 | semver-tags | no |
| `paypal/postman-collections` | api-collection | tier2 | commit | no |
| `paypal/PayPal-TypeScript-Server-SDK` | server-sdk | tier2 | semver-tags | no |
| `paypal/PayPal-PHP-Server-SDK` | server-sdk | tier2 | semver-tags | no |
| `paypal/paypal-messages-ios` | messaging-sdk | tier2 | semver-tags | no |
| `paypal/paypal-messages-android` | messaging-sdk | tier2 | semver-tags | no |
| `paypal/paypal-sdk-logos` | assets | tier3 | commit | no |
| `paypal/paypal-rest-api-specifications` | api-specification | tier1 | commit | no |
| `paypal-examples/v6-web-sdk-sample-integration` | sample-app | tier1 | commit | yes |
| `paypal-examples/v6-web-sdk-with-braintree-sdk-sample-integration` | sample-app | tier1 | commit | no |
| `paypal-examples/paypal-android-sdk-demo-app` | sample-app | tier1 | commit | no |
| `paypal-examples/paypal-sdk-server-side-integration` | sample-app | tier1 | commit | no |
| `paypal-examples/paypal-ios-sdk-demo-app` | sample-app | tier1 | commit | no |

### Braintree

| Repository | Type | Tier | Strategy | Enabled |
| --- | --- | --- | --- | --- |
| `braintree/braintree_android` | mobile-sdk | tier1 | semver-tags | no |
| `braintree/braintree_ios` | mobile-sdk | tier1 | semver-tags | yes |
| `braintree/web-sdk-github-actions` | automation | tier3 | commit | no |
| `braintree/mobile-sdk-tooling` | tooling | tier3 | commit | no |
| `braintree/graphql-api` | api-specification | tier1 | commit | no |
| `braintree/credit-card-type` | utility | tier3 | semver-tags | no |
| `braintree/braintree-web` | web-sdk | tier1 | semver-tags | no |
| `braintree/uuid` | utility | tier3 | semver-tags | no |
| `braintree/popup-bridge-ios` | mobile-utility | tier3 | semver-tags | no |
| `braintree/restricted-input` | web-utility | tier3 | semver-tags | no |
| `braintree/braintree-web-drop-in` | drop-in | tier1 | semver-tags | no |
| `braintree/popup-bridge-android` | mobile-utility | tier3 | semver-tags | no |
| `braintree/braintree_php` | server-sdk | tier2 | semver-tags | no |
| `braintree/braintree_ruby` | server-sdk | tier2 | semver-tags | no |
| `braintree/braintree_node` | server-sdk | tier2 | semver-tags | no |
| `braintree/braintree-ios-drop-in` | drop-in | tier1 | semver-tags | no |
| `braintree/braintree-android-drop-in` | drop-in | tier1 | semver-tags | no |

### Stripe

| Repository | Type | Tier | Strategy | Enabled |
| --- | --- | --- | --- | --- |
| `stripe/stripe-ios` | mobile-sdk | tier1 | semver-tags | yes |
| `stripe/stripe-apps` | developer-platform | tier2 | semver-tags | no |
| `stripe/stripe-cli` | cli | tier2 | semver-tags | no |
| `stripe/stripe-android` | mobile-sdk | tier1 | semver-tags | no |
| `stripe/link-cli` | cli | tier2 | semver-tags | no |
| `stripe/stripe-react-native` | mobile-sdk | tier1 | semver-tags | no |
| `stripe/stripe-ios-spm` | release-mirror | tier3 | commit | no |
| `stripe/stripe-php` | server-sdk | tier2 | semver-tags | no |
| `stripe/stripe-node` | server-sdk | tier2 | semver-tags | no |
| `stripe/stripe-js` | web-sdk | tier1 | semver-tags | no |
| `stripe/sync-engine` | tooling | tier2 | commit | no |
| `stripe/react-stripe-js` | web-sdk | tier1 | semver-tags | no |
| `stripe/stripe-terminal-ios` | terminal-sdk | tier1 | semver-tags | no |
| `stripe/stripe-terminal-android` | terminal-sdk | tier1 | semver-tags | no |
| `stripe/ai` | developer-tooling | tier2 | commit | no |

### Metronome

| Repository | Type | Tier | Strategy | Enabled |
| --- | --- | --- | --- | --- |
| `Metronome-Industries/metronome-node` | server-sdk | tier2 | semver-tags | no |
| `Metronome-Industries/ai` | developer-tooling | tier2 | commit | no |
| `Metronome-Industries/ai-eval` | evaluation-tooling | tier3 | commit | no |
| `Metronome-Industries/mintlify-docs` | docs-source | tier2 | commit | no |
| `Metronome-Industries/terraform-provider-metronome` | terraform-provider | tier2 | semver-tags | no |

### Adyen

| Repository | Type | Tier | Strategy | Enabled |
| --- | --- | --- | --- | --- |
| `Adyen/adyen-node-api-library` | server-sdk | tier2 | semver-tags | no |
| `Adyen/adyen-react-native` | mobile-sdk | tier1 | semver-tags | no |
| `Adyen/adyen-web` | web-sdk | tier1 | semver-tags | yes |
| `Adyen/adyen-android` | mobile-sdk | tier1 | semver-tags | no |
| `Adyen/adyen-ios` | mobile-sdk | tier1 | semver-tags | no |
| `Adyen/adyen-magento2` | commerce-plugin | tier2 | semver-tags | no |
| `Adyen/adyen-pos-mobile-ios` | terminal-sdk | tier1 | semver-tags | no |
| `Adyen/adyen-pos-mobile-ios-test` | test-tooling | tier3 | commit | no |
| `Adyen/adyen-postman` | api-collection | tier2 | commit | no |
| `Adyen/adyen-php-api-library` | server-sdk | tier2 | semver-tags | no |
| `Adyen/adyen-sdk-automation` | automation | tier3 | commit | no |
| `Adyen/release-automation-action` | automation | tier3 | commit | no |
| `Adyen/adyen-3ds2-ios-swift` | authentication-sdk | tier2 | semver-tags | no |
| `Adyen/adyen-wechatpay-ios` | payment-method-sdk | tier2 | semver-tags | no |
| `Adyen/adyen-3ds2-android` | authentication-sdk | tier2 | semver-tags | no |
| `Adyen/adyen-3ds2-ios` | authentication-sdk | tier2 | semver-tags | no |

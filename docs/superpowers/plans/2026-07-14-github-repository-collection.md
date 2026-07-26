# GitHub Repository Collection and Versioned Ingest Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a registry-driven GitHub repository collector that creates immutable curated snapshots for configured release lines, preserves exact changelog and release-note evidence, generates comparison and ingest packets, monitors progress deterministically, and integrates one stable company-scoped wiki source while preserving strictly serial, human-approved ingest.

**Architecture:** A standard-library Python CLI orchestrates focused modules for TOML compatibility, registry validation, stable release-track selection, selector-scoped Git fetching, key-file and release-evidence capture, immutable snapshot promotion, packet generation, state reporting, and validation. The deterministic core is completed and tested with temporary local Git repositories before any public repository is contacted. Live PayPal JS collection applies the approved hybrid v10/v9/v8 retention policy, stops at a user-review gate, and then ingests exactly one complete release or comparison packet at a time into one stable source page.

**Tech Stack:** Python 3.9.6 standard library, `unittest`, Git CLI through `subprocess`, TOML with `tomllib`/`tomli`/tested fallback, JSON/JSONL state, Markdown, Obsidian wikilinks.

## Global Constraints

- Read `CLAUDE.md` and the relevant `rules/*.md` file before each operational workflow.
- Keep `rules/github-repos.md` as a standalone workflow file.
- Collection may batch; ingest is human-kicked-off and processes exactly one packet at a time.
- Before GitHub ingest, read the complete packet, every referenced `snapshot.md`, and every required raw file.
- Accepted files under `raw/` are immutable. Never enrich or overwrite an accepted snapshot.
- Exact upstream files, exact available GitHub release-note content, and the repository-owned snapshot manifest belong in `raw/`; generated diffs, summaries, status, and packets belong in `tracking/`.
- Version-track policy is registry-driven. Major selectors exclude prereleases by default; exact prerelease selectors remain opt-in.
- For the PayPal JS pilot, backfill every stable v10 release, selected v8/v9 minor baselines, and every future stable release in tracked lines.
- A retained release creates one immutable snapshot per unique SHA and one packet per newly collected release. Same-SHA tags become aliases rather than duplicate snapshots.
- Use company-first wiki paths such as `wiki/sources/paypal/github/` and source-type-first operational paths such as `raw/github/paypal/`.
- One repository maps to one stable source page unless a separately approved exception applies.
- Keep the implementation compatible with Python 3.9.6 and add no mandatory third-party dependency.
- Keep network-dependent checks outside the default unit-test suite.
- Do not modify the unrelated untracked `CLAUDE copy.md`.
- Commit after every independently reviewable task.

## Delivery Stages

1. Tasks 1-9 build the deterministic local core, release-retention policy, and rules.
2. Task 10 proves multi-release collection against local Git fixtures.
3. Task 11 performs the `paypal/paypal-js` live collection pilot, then stops for user approval.
4. Task 12 performs serial release and comparison ingest only after that approval.
5. Task 13 collects the remaining pilot repositories without auto-ingest.
6. Tasks 14-15 perform the deterministic source-layout and log migrations only after pilot acceptance.

## File Map

| File | Responsibility |
| --- | --- |
| `scripts/toml_compat.py` | Python 3.9-compatible TOML loading shared by PSP and GitHub registries. |
| `scripts/github_registry.py` | Registry dataclasses, validation, defaults, and selection. |
| `tracking/github/repo-registry.toml` | Human-maintained complete repository inventory and collection intent. |
| `scripts/github_versions.py` | Shared semantic-version parsing, precedence, and package-tag identity. |
| `scripts/github_git.py` | Git subprocess wrapper, selector-scoped ref fetching, repository inspection, and exact ref resolution. |
| `scripts/github_releases.py` | Stable release-track discovery, hybrid backfill selection, and optional GitHub release-note retrieval. |
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
| `tests/test_github_versions.py` | Shared semantic-version, prerelease, and package-tag behavior tests. |
| `tests/test_github_git.py` | Ref resolution, aliases, ambiguity, submodule, and LFS tests. |
| `tests/test_github_releases.py` | Stable-only major selection, hybrid backfill, release-note evidence, and periodic tag discovery tests. |
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
- Consumes: `RepoConfig`, a temporary clone path, and a selector such as `default-branch`, `tag:v9.1.0`, `commit:0123456789abcdef0123456789abcdef01234567`, or `package:@scope/name@9`.
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

### Task 4: Add Shared Version Semantics and Registry Release Tracks

**Files:**
- Create: `scripts/github_versions.py`
- Create: `tests/test_github_versions.py`
- Modify: `scripts/github_registry.py`
- Modify: `scripts/github_git.py`
- Modify: `tests/test_github_registry.py`
- Modify: `tests/test_github_git.py`

**Interfaces:**
- Consumes: semantic versions and package tags already interpreted by `github_git.py`, plus nested `[[repos.version_tracks]]` registry tables.
- Produces: `SemanticVersion`, `parse_semver(value: str) -> Optional[SemanticVersion]`, `compare_semver(left: SemanticVersion, right: SemanticVersion) -> int`, `matches_semver(candidate: SemanticVersion, target: SemanticVersion, include_prerelease: bool = False) -> bool`, `parse_package_tag(tag: str) -> Optional[Tuple[str, str]]`, and immutable `VersionTrack` values on `RepoConfig.version_tracks`.

- [ ] **Step 1: Write failing shared-version tests**

Create `tests/test_github_versions.py` with exact stable/prerelease behavior:

```python
class GitHubVersionTests(unittest.TestCase):
    def test_major_selector_excludes_newer_prerelease_by_default(self):
        target = parse_semver("10")
        stable = parse_semver("10.1.5")
        prerelease = parse_semver("10.2.0-beta.1")
        self.assertTrue(matches_semver(stable, target))
        self.assertFalse(matches_semver(prerelease, target))

    def test_exact_prerelease_matches_only_itself(self):
        target = parse_semver("10.2.0-beta.1")
        self.assertTrue(matches_semver(parse_semver("10.2.0-beta.1"), target))
        self.assertFalse(matches_semver(parse_semver("10.2.0"), target))

    def test_semver_precedence_handles_numeric_prerelease_identifiers(self):
        self.assertLess(
            compare_semver(parse_semver("10.0.0-rc.2"), parse_semver("10.0.0-rc.10")),
            0,
        )
```

Also test scoped package tags and optional leading `v`. The shared module replaces, rather than duplicates, Git-specific semantic-version parsing.

- [ ] **Step 2: Write failing version-track registry tests**

Define the exact records:

```python
@dataclass(frozen=True)
class VersionTrack:
    selector: str
    backfill: str
    future: str
    include_prerelease: bool = False
    pinned_versions: Tuple[str, ...] = ()

@dataclass(frozen=True)
class SemanticVersion:
    major: int
    minor: Optional[int]
    patch: Optional[int]
    prerelease: Optional[Tuple[str, ...]]
    is_exact: bool
```

Add `version_tracks: Tuple[VersionTrack, ...] = ()` to the end of `RepoConfig`. Test nested TOML loading, immutability, defaults, and rejection of unknown `backfill`/`future` values, empty or unparsable selectors, prerelease values that are not booleans, duplicate selectors, and non-exact `pinned_versions`. A track selector must be either a package-scoped semantic selector such as `package:@scope/name@10` or a plain semantic tag selector such as `v10`.

Allowed policies are:

```python
BACKFILL_POLICIES = {"all-stable", "minor-baselines", "none"}
FUTURE_POLICIES = {"all-stable", "none"}
```

- [ ] **Step 3: Run tests to verify failure**

```bash
python3 -m unittest tests.test_github_versions tests.test_github_registry tests.test_github_git -v
```

Expected: import and record-field failures before the shared module and registry track support exist.

- [ ] **Step 4: Implement the shared version boundary**

Move semantic-version and package-tag parsing out of `github_git.py` into `github_versions.py`. Keep exact prerelease matching available, but make non-exact major/minor selectors exclude prereleases unless the caller passes `include_prerelease=True`. Update existing Git resolution and selector-scoped fetch code to use the shared functions without changing exact tag, commit, alias, or ambiguity behavior.

- [ ] **Step 5: Implement nested immutable version tracks**

Parse `version_tracks` from each repository row, preserve registry order, and validate every nested key. Do not add a PayPal JS track to the checked-in registry yet; Task 11 live discovery must confirm the package namespace first. Keep the existing 71-row inventory and five enabled pilots unchanged.

- [ ] **Step 6: Run focused and full tests**

```bash
python3 -m unittest tests.test_github_versions tests.test_github_registry tests.test_github_git -v
python3 -m unittest discover -s tests -v
git diff --check
```

Expected: all existing selector tests remain green; a major selector chooses stable `10.1.5` over `10.2.0-beta.1`.

- [ ] **Step 7: Commit the version policy**

```bash
git add scripts/github_versions.py scripts/github_registry.py scripts/github_git.py tests/test_github_versions.py tests/test_github_registry.py tests/test_github_git.py
git commit -m "feat: add github release track policy"
```

---

### Task 5: Discover Retained Releases and Preserve Release Notes

**Files:**
- Create: `scripts/github_releases.py`
- Create: `tests/test_github_releases.py`

**Interfaces:**
- Consumes: `RepoConfig`, `VersionTrack`, remote tag metadata available through a temporary clone, and the set of versions already present in the generated version index.
- Produces: `discover_release_candidates(config: RepoConfig, clone_path: Path, track: VersionTrack) -> Tuple[ReleaseCandidate, ...]`, `select_release_candidates(track: VersionTrack, candidates: Sequence[ReleaseCandidate], existing_versions: Sequence[str] = (), mode: str = "backfill") -> Tuple[ReleaseCandidate, ...]`, and `fetch_release_notes(config: RepoConfig, candidate: ReleaseCandidate, token: Optional[str] = None, opener=None) -> Optional[ReleaseNotesEvidence]`.

- [ ] **Step 1: Write failing release-selection tests**

Define:

```python
@dataclass(frozen=True)
class ReleaseCandidate:
    package: str
    version: str
    tag: str
    object_sha: str
    commit_sha: str
    prerelease: bool

@dataclass(frozen=True)
class ReleaseNotesEvidence:
    source_url: str
    published_at: str
    content: bytes
```

Require `all-stable` to select every stable version and exclude prereleases. Require `minor-baselines` to select the first stable release, latest patch in every minor line, latest stable release, and every exact `pinned_versions` entry, with the final union deduplicated and ordered by semantic version.

```python
def test_minor_baselines_include_first_latest_per_minor_and_pins(self):
    selected = select_release_candidates(
        track(backfill="minor-baselines", pinned_versions=("9.0.1",)),
        candidates("9.0.0", "9.0.1", "9.1.0", "9.1.3", "9.2.0-beta.1"),
    )
    self.assertEqual(("9.0.0", "9.0.1", "9.1.3"), tuple(item.version for item in selected))
```

For `mode="future"`, `future="all-stable"` returns every stable candidate absent from `existing_versions`; `future="none"` returns none. Invalid modes and missing pinned versions raise `ReleaseSelectionError` rather than silently weakening retention.

- [ ] **Step 2: Write failing discovery and release-note tests**

Build a local bare remote with lightweight and annotated package tags. Assert discovery preserves the tag object SHA and peeled commit SHA, scopes candidates to the exact package and major selector, and returns no unrelated package tags.

Mock the GitHub API opener. A successful response preserves the release body as UTF-8 bytes without adding headers. HTTP 404 returns `None`; rate limits, malformed JSON, a non-string body, and other HTTP failures raise `ReleaseEvidenceError` with repository and tag context.

- [ ] **Step 3: Run tests to verify failure**

```bash
python3 -m unittest tests.test_github_releases -v
```

Expected: import failure because `github_releases.py` does not exist.

- [ ] **Step 4: Implement deterministic remote discovery**

Use `git ls-remote --tags origin` through `github_git.run_git`. Pair annotated tag rows with their `^{}` peeled rows. Listing remote ref metadata is allowed; do not fetch every tag object. A package selector accepts only tags for its exact package namespace. A plain semantic selector accepts only plain semantic tags; if matching package tags would make the namespace ambiguous, raise `ReleaseSelectionError` and require a package-scoped track.

- [ ] **Step 5: Implement hybrid selection and exact release notes**

Selection is pure and network-free. Release-note retrieval uses the standard library GitHub releases-by-tag endpoint with URL-quoted owner, repository, and tag values. Send `Accept: application/vnd.github+json`, a descriptive user agent, and optional bearer authorization. Return exact body bytes separately from metadata so `release-notes.md` can remain upstream content.

- [ ] **Step 6: Run focused and full tests**

```bash
python3 -m unittest tests.test_github_releases -v
python3 -m unittest discover -s tests -v
git diff --check
```

Expected: no default-suite test contacts the network.

- [ ] **Step 7: Commit release discovery**

```bash
git add scripts/github_releases.py tests/test_github_releases.py
git commit -m "feat: select github release history"
```

---

### Task 6: Create Immutable Curated Snapshots

**Files:**
- Modify: `scripts/github_snapshot.py`
- Modify: `tests/test_github_snapshot.py`

**Interfaces:**
- Consumes: `RepoConfig`, `ResolvedRef`, optional `ReleaseNotesEvidence`, a checked-out repository, collection date, and optional prior changed paths.
- Produces: `select_key_files(config: RepoConfig, repo_root: Path, changed_paths: Sequence[str] = ()) -> SelectionResult`, `build_snapshot(config: RepoConfig, ref: ResolvedRef, repo_root: Path, raw_root: Path, staging_root: Path, collection_date: str, prior_snapshot: Optional[str] = None, capture_kind: str = "canonical", release_notes: Optional[ReleaseNotesEvidence] = None, changed_paths: Sequence[str] = ()) -> SnapshotRecord`, `validate_staged_snapshot(record: SnapshotRecord) -> List[str]`, and `promote_snapshot(record: SnapshotRecord) -> Path`.

- [ ] **Step 1: Write failing archive-safety and evidence tests**

Retain the existing selection and immutability tests. Add tests proving:

```python
def test_changed_public_path_reaches_built_snapshot(self):
    (repo / "src/public.js").write_text("export const value = 1;\n", encoding="utf-8")
    record = build_snapshot(
        config, resolved, repo, raw_root, staging_root, "2026-07-14",
        changed_paths=("src/public.js",),
    )
    self.assertTrue((record.staging_path / "files/src/public.js").exists())

def test_symlink_and_parent_traversal_never_leave_checkout(self):
    outside = repo.parent / "secret.txt"
    outside.write_text("secret", encoding="utf-8")
    (repo / "README.md").symlink_to(outside)
    result = select_key_files(dataclasses.replace(config, key_paths=("../secret.txt",)), repo)
    self.assertEqual((), result.selected)
    self.assertTrue(any(reason == "outside-checkout" for _, reason in result.excluded))

def test_release_notes_are_exact_top_level_evidence(self):
    evidence = ReleaseNotesEvidence("https://api.github.test/release", "2026-07-14T00:00:00Z", b"# Exact notes\n")
    record = build_snapshot(
        config, resolved, repo, raw_root, staging_root, "2026-07-14",
        release_notes=evidence,
    )
    self.assertEqual(b"# Exact notes\n", (record.staging_path / "release-notes.md").read_bytes())
```

Also cover a filename containing `|`, unexpected top-level files, `.diff` rejection, manifest metadata tampering, copied-byte limit changes, advisory-lock contention, concurrent supplement allocation, unsafe promotion-parent permissions, and staging cleanup after validation or promotion failure.

- [ ] **Step 2: Run tests to verify the remediation is RED**

```bash
python3 -m unittest tests.test_github_snapshot -v
```

Expected: the new traversal, manifest-authority, release-note, no-clobber, and `changed_paths` tests fail against commit `0ac3167`.

- [ ] **Step 3: Enforce checkout containment and copied-byte limits**

Resolve every candidate and require `candidate.relative_to(repo_root.resolve())` to succeed before selection. Reject symlinks even when their target remains inside the checkout, reject absolute and `..` registry/changed paths, and verify the destination remains under `staging/files/`. Copy bytes once, then calculate size and hash from the copied bytes; enforce per-file and total limits against those bytes rather than a pre-copy `stat()` result.

- [ ] **Step 4: Make `snapshot.md` the structured integrity authority**

Keep the existing record fields:

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

`SnapshotRecord` may add immutable trusted fields for repository provenance,
release-note provenance, exact release-note SHA-256/size, and staged-directory
device/inode identity. Validation must compare the manifest and staged bytes
against those record values; changing both `release-notes.md` and its manifest
entry must still fail.

Render one versioned JSON metadata block inside `snapshot.md`, followed by human-readable saved/excluded Markdown tables. JSON is the parsing authority and safely represents valid filenames such as `docs/a|b.md`; escape Markdown table cells for display. The JSON records complete identity metadata, saved file paths/hashes/sizes/purposes, exclusions, release-note source metadata or explicit absence, and prior snapshot.

Validation parses JSON from `snapshot.md`, compares identity fields with the record, and hashes every listed file against manifest values. It rejects duplicate entries, missing or unlisted files, any top-level entry except `snapshot.md`, optional `release-notes.md`, and `files/`, and any `.patch` or `.diff` anywhere under staging. `release-notes.md` bytes are included in manifest integrity data without altering the upstream content.

- [ ] **Step 5: Promote inside a collector-private advisory-lock boundary**

Require the staging and repository snapshot parent directories to be owned by
the collector user and not group- or world-writable. Open them without
following symlinks and use descriptor-relative operations. Keep one stable
regular `.promotion.lock` file per repository, acquire
`fcntl.flock(LOCK_EX | LOCK_NB)` for the full transaction, and release it by
closing the descriptor; never delete the lock pathname.

While holding the lock, recheck canonical SHA identity, select the next
supplement `-rN`, check target absence, validate the staged-directory identity
and manifest, verify the source and target parents share a filesystem, and
promote with descriptor-relative `os.replace()`. Lock contention, unsafe
permissions, symlinks, identity mismatch, target collision, or cross-filesystem
promotion fails explicitly. Always clean only the current operation's staging
directory after failure, and never remove an existing target.

Canonical recollection still returns the existing snapshot unchanged. Supplements choose the next free revision while holding the lock and record `capture_kind = "supplement"`.

The guarantee covers cooperating collectors inside the collector-private
namespace. It does not claim protection from a malicious process running as the
same collector user and ignoring the advisory lock.

- [ ] **Step 6: Run focused and full tests**

```bash
python3 -m unittest tests.test_github_snapshot -v
python3 -m unittest discover -s tests -v
git diff --check
```

Expected: all existing Task 6 tests plus archive-safety and release-evidence regressions pass.

- [ ] **Step 7: Commit the remediated snapshot boundary**

```bash
git add scripts/github_snapshot.py tests/test_github_snapshot.py
git commit -m "fix: harden immutable github snapshots"
```

---

### Task 7: Build Version Indexes and Ingest Packets

**Files:**
- Create: `scripts/github_packets.py`
- Create: `tests/test_github_packets.py`

**Interfaces:**
- Consumes: immutable release-aware `SnapshotRecord` values, repository Git history, and existing `version-index.json`.
- Produces: `load_version_index(path: Path, repo_id: str) -> VersionIndex`, `record_snapshot(index: VersionIndex, snapshot: SnapshotRecord) -> VersionIndex`, `select_prior(index: VersionIndex, ref: ResolvedRef) -> Optional[VersionEntry]`, `build_baseline_packet(config: RepoConfig, current: SnapshotRecord, packet_root: Path) -> PacketRecord`, `build_delta_packet(config: RepoConfig, prior: VersionEntry, current: SnapshotRecord, repo_root: Path, packet_root: Path) -> PacketRecord`, and `build_comparison_packet(config: RepoConfig, prior: VersionEntry, current: VersionEntry, repo_root: Path, packet_root: Path) -> PacketRecord`.

- [ ] **Step 1: Write failing version-index tests**

Assert one canonical version snapshot per SHA, alias deduplication, package-namespace prior selection, branch prior selection, supplement recording without a new version, and release-note/changelog evidence paths retained per version entry.

```python
def test_aliases_share_one_version_entry(self):
    first = record_snapshot(empty_index(), snapshot(sha="a" * 40, aliases=("v1",)))
    second = record_snapshot(first, snapshot(sha="a" * 40, aliases=("stable", "v1")))
    self.assertEqual(1, len(second.versions))
    self.assertEqual(("stable", "v1"), second.versions[0].aliases)
```

- [ ] **Step 2: Write failing packet tests**

Create two local releases with added, modified, renamed, and deleted files. Require `packet.json`, `ingest-packet.md`, `changed-files.txt`, and `source-diff.patch` under tracking. Assert no `.patch` appears under raw, every packet starts in `awaiting-review`, one packet is created per newly collected release, and required reading includes the release snapshot manifest, exact available `release-notes.md`, every retained changelog path, and changed public files.

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
    release_notes_path: str
    changelog_paths: Tuple[str, ...]

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

Use an argument list equivalent to `git diff --find-renames --no-ext-diff --no-textconv FROM_SHA TO_SHA -- SELECTED_PATHS`, substituting the exact SHAs and selected repository paths in the subprocess call. Exclude binary and ignored high-churn paths. The packet must distinguish evidence from generated guidance, identify the exact release/package/version, link changelog and release-note evidence or state their explicit absence, and list the exact required reading order. A changelog delta is generated under tracking only; the exact changelog remains under raw.

- [ ] **Step 6: Run tests and commit**

```bash
python3 -m unittest tests.test_github_packets -v
python3 -m unittest discover -s tests -v
git add scripts/github_packets.py tests/test_github_packets.py
git commit -m "feat: generate github ingest packets"
```

---

### Task 8: Add State Reporting and the Public CLI

**Files:**
- Create: `scripts/github_reporting.py`
- Create: `scripts/collect_github_repos.py`
- Create: `tests/test_github_reporting.py`
- Create: `tests/test_collect_github_repos.py`

**Interfaces:**
- Consumes: registry selections and version tracks, release discovery/evidence, Git/snapshot/packet modules, run events, and packet transition requests.
- Produces: `append_event(path: Path, event: Mapping[str, object]) -> None`, `validate_collection_run(events: Sequence[Mapping[str, object]]) -> int`, `transition_packet(current: str, requested: str) -> str`, `render_collection_status(repos: Sequence[RepoConfig], events: Sequence[Mapping[str, object]]) -> str`, `render_ingest_status(packets: Sequence[PacketRecord], states: Mapping[str, str]) -> str`, `collect_one(root: Path, config: RepoConfig, selectors: Sequence[str] = (), release_mode: Optional[str] = None) -> CollectionResult`, `compare_one(root: Path, config: RepoConfig, from_selector: str, to_selector: str) -> PacketRecord`, and `main(argv: Optional[Sequence[str]] = None) -> int`.

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
collect --repo paypal/paypal-js --release-mode backfill --dry-run
collect --repo paypal/paypal-js --release-mode future --dry-run
compare --repo paypal/paypal-js --from package:@paypal/react-paypal-js@8 --to package:@paypal/react-paypal-js@10
prepare --repo paypal/paypal-js --ref default-branch
status
packet-state --repo paypal/paypal-js --packet "$PACKET_ID" --from awaiting-review --to approved
```

Dry-run may resolve and report but must not create `raw/` or mutate generated state.

`--release-mode backfill` enumerates the configured historical policy. `--release-mode future` selects stable releases absent from the version index. Explicit `--ref` and `--release-mode` are mutually exclusive. Every selected release is reported separately and creates at most one packet.

`--all` and `--company` select enabled rows by default. An explicit `--repo` may select a disabled row because it is an intentional one-repository request. `--include-disabled` is required to batch-select disabled rows.

- [ ] **Step 3: Run tests to verify failure**

```bash
python3 -m unittest tests.test_github_reporting tests.test_collect_github_repos -v
```

Expected: import failures because the modules do not exist.

- [ ] **Step 4: Implement append-only events and generated dashboards**

`append_event` writes one sorted JSON object plus newline using append mode. For example, PayPal JS packet history lives at `tracking/github/repos/paypal/paypal-js/packets/PACKET_ID/state-events.jsonl`; `packet.json` remains the immutable packet contract. Regenerate Markdown and `status.json` from registry, version indexes, packet contracts, and the latest valid events.

- [ ] **Step 5: Implement orchestration with cleanup**

Use `tempfile.TemporaryDirectory(prefix="wiki-github-")` for clones. For release modes, discover candidates, fetch only selected refs, fetch optional release-note evidence, and build one immutable snapshot and packet per selected release. Record one terminal event for every selected repo/ref even when resolution, release evidence, clone, or snapshot promotion fails. Remove staging after any failure. Return `1` for unreconciled runs or validation failure, `2` for CLI/registry misuse, and `0` only for a reconciled successful command.

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

### Task 9: Validate Snapshots, Packets, and Wiki Links

**Files:**
- Create: `scripts/github_validation.py`
- Create: `scripts/validate_github_collection.py`
- Create: `tests/test_github_validation.py`
- Modify: `tests/test_validate_wiki.py`
- Modify: `scripts/validate_wiki.py` only if a failing test proves a missing nested-path behavior.

**Interfaces:**
- Consumes: `raw/github/`, `tracking/github/`, registry version tracks, company-first GitHub source pages and release ledgers, version indexes, packet state events, and generated status.
- Produces: `inspect_github(root) -> GitHubReport`, `validate_github(report) -> List[str]`, and a CLI that returns nonzero for structural errors while reporting awaiting-ingest packets as informational.

- [ ] **Step 1: Write failing structural tests**

Cover valid snapshots, bad hashes, manifest/file disagreement, duplicate canonical SHA snapshots, valid supplements, missing required-reading files, patch or diff files under raw, invalid packet transitions, source `raw_files` ordering, path-qualified snapshot/changelog/release-note links, status disagreement, and pending packets. Add release-retention tests for a prerelease incorrectly selected by a stable-only track, a retained version missing from the index, two canonical snapshots for one SHA, release evidence silently absent from the manifest, and a newly collected release without exactly one packet.

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

def test_stable_track_rejects_prerelease_version_entry(self):
    report = inspect_github(self.make_valid_tree(index_version="10.2.0-beta.1"))
    self.assertTrue(any("prerelease in stable-only track" in error for error in validate_github(report)))
```

- [ ] **Step 2: Run tests to verify failure**

```bash
python3 -m unittest tests.test_github_validation -v
```

Expected: import failure because `github_validation.py` does not exist.

- [ ] **Step 3: Implement report records and validation**

Define a frozen `GitHubReport` containing registry tracks, snapshot paths, release-evidence records, packet paths, pending packet IDs, source records, version indexes, dashboard records, and inspection errors. Reuse `split_frontmatter`, `parse_frontmatter`, and `WIKILINK_RE` from `validate_wiki.py`; do not duplicate YAML parsing.

- [ ] **Step 4: Extend nested link regression coverage**

Add a source fixture whose two raw entries end in `snapshot.md` but use full path-qualified wikilinks, and whose release-ledger row links nested `CHANGELOG.md` and `release-notes.md`. Assert `validate_wiki.check_file` resolves every link. Modify `validate_wiki.py` only if this test fails.

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

### Task 10: Prove the Complete Pipeline with a Local Git Repository

**Files:**
- Modify: `tests/test_collect_github_repos.py`
- Create generated baseline files: `tracking/github/status.json`, `tracking/github/collection-status.md`, `tracking/github/ingest-status.md`

**Interfaces:**
- Consumes: the full registry, version tracks, and every deterministic core module.
- Produces: local default-branch and multi-release end-to-end tests plus clean empty production dashboards before live collection.

- [ ] **Step 1: Preserve the default-branch end-to-end test**

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

- [ ] **Step 2: Add a failing multi-release end-to-end test**

Create a local monorepo remote with stable package tags `10.0.0`, `10.1.3`, and `10.1.5`, a newer `10.2.0-beta.1`, exact changelog bytes, and mocked release-note responses. Configure an `all-stable` v10 track and assert:

```python
def test_local_release_backfill_and_future_patch(self):
    backfill = collect_one(root, config, release_mode="backfill")
    self.assertEqual(("10.0.0", "10.1.3", "10.1.5"), backfill.versions)
    self.assertEqual(3, len(backfill.packet_ids))
    self.assertFalse(any("beta" in version for version in backfill.versions))

    unchanged = collect_one(root, config, release_mode="backfill")
    self.assertEqual((), unchanged.packet_ids)

    add_release(upstream, "10.1.6", changelog=b"# 10.1.6\n")
    future = collect_one(root, config, release_mode="future")
    self.assertEqual(("10.1.6",), future.versions)
    self.assertEqual(1, len(future.packet_ids))
```

Assert every snapshot preserves exact changelog and release-note bytes, every packet remains `awaiting-review`, one SHA shared by two tags has one canonical snapshot, and a default-branch SHA differing from latest v10 is collected independently.

- [ ] **Step 3: Run the tests and fix only owning-module defects**

```bash
python3 -m unittest \
  tests.test_collect_github_repos.CollectGitHubReposTests.test_local_end_to_end_baseline_unchanged_change_and_compare \
  tests.test_collect_github_repos.CollectGitHubReposTests.test_local_release_backfill_and_future_patch -v
```

Expected: PASS. Any failure must be fixed in the owning module with a focused regression assertion before proceeding.

- [ ] **Step 4: Generate empty production dashboards**

```bash
python3 scripts/collect_github_repos.py status
python3 scripts/validate_github_collection.py
```

Expected: 71 registered repositories, 5 enabled pilots, 0 collected versions, 0 ingest packets, and no validation errors.

- [ ] **Step 5: Run the complete local gate**

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all tests and validators pass.

- [ ] **Step 6: Commit the local proof**

```bash
git add tests/test_collect_github_repos.py tracking/github/status.json tracking/github/collection-status.md tracking/github/ingest-status.md
git commit -m "test: prove github collection pipeline locally"
```

---

### Task 11: Collect the `paypal/paypal-js` Pilot and Stop

**Files:**
- Modify when exact selectors are discovered: `tracking/github/repo-registry.toml`
- Create: collector-named children under `raw/github/paypal/paypal-js/snapshots/`
- Create: `tracking/github/repos/paypal/paypal-js/`
- Create: collector-named run directories under `tracking/github/runs/`
- Regenerate: `tracking/github/status.json`, `tracking/github/collection-status.md`, `tracking/github/ingest-status.md`

**Interfaces:**
- Consumes: live `paypal/paypal-js` refs and the enabled registry row.
- Produces: every stable v10 snapshot, selected v9/v8 minor baselines, an independent changed default-branch snapshot when applicable, exact available changelog/release-note evidence, and one reviewable packet per newly collected release; no wiki ingest.

- [ ] **Step 1: Read collection rules and run a no-write preflight**

```bash
python3 scripts/collect_github_repos.py collect --repo paypal/paypal-js --release-mode backfill --dry-run
```

Expected: remote package namespaces, stable/prerelease classification, all stable v10 candidates, selected v9/v8 baseline candidates, estimated snapshot/evidence counts, and default-branch identity are printed; no `raw/github/paypal/paypal-js/` or generated state is created.

- [ ] **Step 2: Resolve package ambiguity explicitly**

Confirm whether v10/v9/v8 belong to `@paypal/react-paypal-js`, `@paypal/paypal-js`, or another package. Audit exact versions already referenced by existing `paypal-js`, `paypal-js-v6`, `react-paypal-js-v8`, and npm React v9 source pages. Identify documented migration boundaries.

Update the registry with three exact package-scoped `[[repos.version_tracks]]` tables. Form each selector from the exact package name printed by preflight plus `@10`, `@9`, or `@8`. Set v10 to `backfill = "all-stable"`; set v9 and v8 to `backfill = "minor-baselines"`; set all three to `future = "all-stable"` and `include_prerelease = false`. Write the sorted exact wiki-reference and migration-boundary audit results into each v8/v9 `pinned_versions` array, using an empty array when the audit finds none. Never commit a bare ambiguous major selector.

- [ ] **Step 3: Run the live collection**

```bash
python3 scripts/collect_github_repos.py collect --repo paypal/paypal-js --release-mode backfill
python3 scripts/collect_github_repos.py collect --repo paypal/paypal-js --ref default-branch
```

Expected: every selected release/ref ends as `collected-baseline`, `collected-change`, or `unchanged`; prereleases are explicitly excluded; same-SHA aliases share a canonical snapshot; exact available changelogs and release notes are retained; and every new release packet starts in `awaiting-review`.

- [ ] **Step 4: Validate and inspect collection size**

```bash
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py status
git diff --check
```

Inspect the run manifest, selected/excluded version list, package namespace, every `snapshot.md`, changelog/release-note availability, packet required-reading sets, total bytes, excluded files, submodule/LFS notes, and secret-scan findings. Confirm the v10 set contains every stable release and no prerelease; confirm v8/v9 implement the approved minor-baseline union. If a packet is too large for complete reading, adjust registry key paths and create a new explicit supplement rather than editing accepted raw.

- [ ] **Step 5: Commit collection evidence**

```bash
git add tracking/github/repo-registry.toml raw/github/paypal/paypal-js tracking/github/repos/paypal/paypal-js tracking/github/runs tracking/github/status.json tracking/github/collection-status.md tracking/github/ingest-status.md
git commit -m "data: collect paypal js version pilot"
```

- [ ] **Step 6: HARD USER GATE**

Share the run manifest, confirmed package namespace, selected and excluded versions, same-SHA aliases, changelog/release-note coverage, snapshot sizes, required-reading files, packet count, and validation results. Stop. Do not approve a packet, update a wiki source page, or begin another pilot ingest until the user explicitly kicks off ingest.

---

### Task 12: Ingest PayPal JS Packets Serially After Approval

**Files:**
- Create or move: `wiki/sources/paypal/github/source-github-paypal-js.md`
- Create when materially supported: `wiki/analyses/paypal/github/analysis-paypal-js-v8-v9-v10.md`
- Modify: `wiki/paypal-index.md`
- Create or modify: `wiki/paypal-log.md`
- Modify as evidence requires: `wiki/companies/paypal.md`, relevant `wiki/concepts/paypal-*.md`
- Modify after backlink audit: legacy `wiki/sources/source-github-paypal-js-v6.md`, `wiki/sources/source-github-react-paypal-js-v8.md`
- Regenerate: `tracking/github/ingest-status.md`, `tracking/github/status.json`

**Interfaces:**
- Consumes: one user-approved release or comparison packet at a time and its complete required-reading set.
- Produces: one stable current repository source page with a concise row for every ingested release, material comparison analysis, ingest receipts, and provider navigation/log entries.

- [ ] **Step 1: Approve exactly one packet**

```bash
python3 scripts/collect_github_repos.py packet-state --repo paypal/paypal-js --packet "$PACKET_ID" --from awaiting-review --to approved
```

Use the exact packet ID from the user-approved Task 11 run manifest in place of the shell token. Confirm all other packets remain `awaiting-review`.

- [ ] **Step 2: Read the complete packet evidence**

Read `ingest-packet.md`, every referenced `snapshot.md`, exact available `release-notes.md`, every retained changelog, and every required raw file end to end. Record 3-5 exact quotes with paths and line ranges in the ingest receipt before any wiki write.

- [ ] **Step 3: Perform concept audit first**

Search all existing PayPal JS SDK, React SDK, checkout, card-fields, Venmo, and migration concepts. Update or create concepts before updating the stable source page.

- [ ] **Step 4: Enter ingesting state and update the stable source page**

Transition the approved packet before the first canonical wiki write:

```bash
python3 scripts/collect_github_repos.py packet-state --repo paypal/paypal-js --packet "$PACKET_ID" --from approved --to ingesting
```

Move or create the canonical page at `wiki/sources/paypal/github/source-github-paypal-js.md`. Preserve `date_ingested`, add `date_updated`, and list every ingested snapshot anchor newest first. Keep current integration guidance separate from a `## Release history` ledger with these exact columns:

```text
Version | Release date | Commit | Snapshot | Changelog | Release notes | Change summary | Migration impact
```

Every ingested release receives one row even when its change summary is “no material integration change identified.” Snapshot, changelog, and release-note links are path-qualified; unavailable upstream evidence is labeled `not published`, not silently omitted. Do not copy full changelog or release-note text into the source page.

- [ ] **Step 5: Finish the complete one-packet cycle**

Update company/concepts, check contradictions, update `wiki/paypal-index.md`, append `wiki/paypal-log.md`, run validation, write the receipt, and transition the packet:

```bash
python3 scripts/validate_wiki.py wiki/sources/paypal/github/source-github-paypal-js.md wiki/companies/paypal.md
python3 scripts/validate_github_collection.py
python3 scripts/collect_github_repos.py packet-state --repo paypal/paypal-js --packet "$PACKET_ID" --from ingesting --to ingested
```

If validation fails, transition from `ingesting` to `validation-failed`, fix the current cycle, regain approval, and do not open another packet.

- [ ] **Step 6: Ingest every retained release serially**

After the latest stable v10 establishes current state, process remaining stable v10 packets one at a time, then selected v9 packets, then selected v8 packets. Within each group, use descending semantic-version order and keep the source ledger sorted newest first. Each release completes Steps 1-5 and receives its own commit before another packet is approved:

```bash
git add wiki tracking/github/repos/paypal/paypal-js tracking/github/ingest-status.md tracking/github/status.json
git commit -m "wiki: ingest paypal js $RESOLVED_VERSION snapshot"
```

Set `RESOLVED_VERSION` to the exact package version recorded in the packet before committing. A same-SHA alias updates the existing ledger row rather than creating a duplicate release snapshot row.

- [ ] **Step 7: Create the material comparison analysis**

Generate explicit v8-to-v9 and v9-to-v10 comparison packets and material minor-line comparisons discovered from release changelogs. Approve and read each independently. Create or update `wiki/analyses/paypal/github/analysis-paypal-js-v8-v9-v10.md` only for behavior, API, compatibility, or migration consequences. Cite the canonical source page and path-qualified snapshots; keep mechanical file lists and patches in tracking.

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

Expected: one canonical repo source page, one ledger row per retained release, validated path-qualified changelog/release-note links, material analyses only where warranted, and no packet left falsely marked `ingested` after a failed validation.

---

### Task 13: Collect the Remaining Cross-Company Pilots

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

### Task 14: Migrate Legacy GitHub Source Pages to Company-First Paths

**Files:**
- Create: `scripts/migrate_github_wiki_layout.py`
- Create: `tests/test_migrate_github_wiki_layout.py`
- Move on apply: flat GitHub pages such as `wiki/sources/source-github-paypal-js.md` to company-first paths such as `wiki/sources/paypal/github/source-github-paypal-js.md`
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

### Task 15: Split the Root Log Deterministically

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

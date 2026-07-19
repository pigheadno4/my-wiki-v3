# GitHub Source Capsule Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the accepted generic GitHub source-capsule, index-v2, immutable-event, retry, and deep-dive contracts without breaking existing release collection or starting wiki ingest.

**Architecture:** Keep format-1/2 snapshots and packet-v1 as immutable compatibility inputs. Add focused modules behind a unified version-state interface so `collect`, `compare`, `prepare`, and `status` continue to work before and after explicit index migration. A transaction coordinator owns locks, descriptors, staging, and publication; artifact builders only stage into coordinator-owned locations and never reacquire locks or promote independently.

**Tech Stack:** Python 3.9.6 standard library, `unittest`, Git CLI through `subprocess`, TOML through `scripts/toml_compat.py`, compact canonical JSON, and no mandatory third-party dependency.

## Global Constraints

- Read `CLAUDE.md`, `rules/github-repos.md`, and `docs/superpowers/specs/2026-07-18-github-source-capsule-design.md` before each task.
- Existing format-1/2 snapshots, packet-v1 directories, `state-events.jsonl`, `collection-failures.jsonl`, and `tracking/github/runs/*.jsonl` remain readable and byte-for-byte immutable.
- No new transaction, lifecycle, retry, run, or command history appends JSONL.
- Format-3 manifests contain no initiating release identity or release-derived path; both canonical locators are `<sha>:c0` capture IDs.
- `npm-tracked-source-v1` reads exact Git objects and never installs, imports, builds, tests, generates, or executes repository code.
- Selected blobs must be regular mode `100644` or `100755`, strict UTF-8, NUL-free, not an LFS pointer, within bounds, and scanned by `text-secrets-v1`.
- Defaults are `max_file_bytes = 512000`, `max_capsule_files = 120`, `max_capsule_utf8_bytes = 750000`, `max_packet_files = 160`, and `max_packet_utf8_bytes = 1000000`.
- Lock order is `repository collection -> snapshot-root promotion -> packet`; only the coordinator acquires or releases these locks during a transaction.
- Every rename is followed by source- and destination-parent directory `fsync`; every unlink by source-parent `fsync`; every new namespace component by immediate parent `fsync`.
- Packet v2 supports only `packet_type = "supplement"`; baseline, delta, and comparison remain packet v1.
- Deep-dive replay uses embedded historical policy; current registry differences report `current-policy-drift` and never recapture automatically.
- Collection may batch selection, but publishes one repository transaction at a time and never approves or ingests a packet.
- Network checks and the PayPal JS pilot remain outside the default unit suite.
- Preserve unrelated changes and commit each independently reviewable task.

## Shared Interfaces

These names are fixed before task dispatch so adjacent tasks do not invent incompatible ownership models.

```python
@dataclass(frozen=True)
class OwnedLock:
    kind: str
    descriptor: int
    device: int
    inode: int

@dataclass(frozen=True)
class DirectoryHandle:
    kind: str
    path: Path
    descriptor: int
    device: int
    inode: int

@dataclass(frozen=True)
class FinalParents:
    snapshot: Optional[DirectoryHandle]
    packet: Optional[DirectoryHandle]
    index: DirectoryHandle
    run: DirectoryHandle

@dataclass(frozen=True)
class PublicationContext:
    transaction_id: str
    transaction_root: Path
    staged_artifacts_root: Path
    io: DurableIO
    transaction_descriptor: int
    staged_artifacts_descriptor: int
    final_parents: FinalParents
    collection_lock: OwnedLock
    snapshot_lock: Optional[OwnedLock]
    packet_lock: Optional[OwnedLock]

@dataclass(frozen=True)
class StagedArtifact:
    artifact_kind: str
    staged_path: Path
    final_path: Path
    final_parent_kind: str
    final_name: str
    device: int
    inode: int
    content_hash: str
    stable_content_hash: str
    validation_profile: str
    initial_lifecycle_event_hash: str

@dataclass(frozen=True)
class PreparedOperation:
    artifacts: Tuple[StagedArtifact, ...]
    before_index: bytes
    after_index: bytes
    terminal_event: Mapping[str, object]
```

Artifact builders accept `PublicationContext`, use its already-open descriptors and `DurableIO`, write only below its staging root, and return `StagedArtifact`. `final_parent_kind` is exactly `snapshot` or `packet`; the coordinator requires `final_path == context.final_parents.<kind>.path / final_name` and validates the parent handle's path/device/inode before publication. `content_hash` covers exact publication-time bytes. `validation_profile` is `immutable-tree` or `packet-lifecycle-v2`; the packet profile reconstructs `stable_content_hash` from immutable packet files plus the exact sequence-one lifecycle event named by `initial_lifecycle_event_hash`, excluding only staging names and lifecycle events with sequence greater than one. Public v1 helpers retain their existing self-locking behavior only outside a journal transaction.

Version-state compatibility is one explicit union, `VersionState = Union[VersionIndex, VersionIndexV2]`, with exact public signatures `load_version_state(path: Path, config: RepoConfig) -> VersionState`, `render_version_state(state: VersionState) -> bytes`, `save_version_state(path: Path, state: VersionState) -> None`, `project_version_view(state: VersionState) -> VersionIndexView`, and `record_release_snapshot(state: VersionState, snapshot: SnapshotRecord) -> VersionState`. Both atomic legacy saving and transaction staging consume `render_version_state`; neither duplicates JSON serialization.

`VersionIndexView` supplies the existing command read surface: versions, capture order, branch observations, release-note paths, changelog paths, and canonical snapshot paths. After migration, normal release collection writes canonical captures and version records into v2; `compare`, `prepare`, and `status` consume the projection and continue producing their existing packet-v1/report contracts.

## File Map

| File | Responsibility |
| --- | --- |
| `scripts/github_canonical.py` | Canonical JSON, identities, npm names, paths, labels. |
| `scripts/github_capsule_policy.py` | Capsule, override, allowlist, and effective-policy records. |
| `scripts/github_git_tree.py` | Exact commit-tree enumeration and blob reads. |
| `scripts/github_npm_workspace.py` | Workspace discovery, dependency closure, exports traversal. |
| `scripts/github_capsule_selection.py` | File classification, secret scan, limits, resolution result. |
| `scripts/github_durable_io.py` | Durable syscall wrapper, named failpoints, namespace/fsync helpers. |
| `scripts/github_events.py` | Immutable chained event publication and recovery. |
| `scripts/github_transactions.py` | Coordinator-owned locks, staging, journal, publication, recovery. |
| `scripts/github_capsule_snapshot.py` | Format-3 staging and offline validation. |
| `scripts/github_index_v2.py` | V2 records, migration, binding, applicability, unified state. |
| `scripts/github_supplement_packets.py` | Packet-v2 staging, identity, reading budget. |
| `scripts/github_lifecycle.py` | Legacy state prefix plus immutable v2 transitions. |
| `scripts/github_retry.py` | Retry/quarantine history and due reducer. |
| `scripts/github_deep_dive.py` | Request identity, exact blob selection, replay/drift. |
| `scripts/github_capsule_validation.py` | New-contract read-only validation. |

---

### Task 1: Canonical Data Primitives

**Files:** Create `scripts/github_canonical.py`; create `tests/test_github_canonical.py`.

**Produces:** `canonical_json_bytes`, `canonical_sha256`, `validate_npm_package_name`, `safe_policy_path`, and `readable_label`.

- [ ] Write failing tests proving object-key sorting, semantic array preservation, UTF-8/no-newline bytes, `@scope/.pkg` and `@scope/_pkg` acceptance, invalid scope/unscoped leading-dot rejection, safe path handling, and bounded label normalization.
- [ ] Run `python3 -m unittest tests.test_github_canonical -v`; expect import failure.
- [ ] Implement the five functions using only Python 3.9 standard library and exact specification grammar.
- [ ] Run the focused tests; expect all pass.
- [ ] Commit with `git commit -m "feat: add github canonical data primitives"`.

### Task 2: Capsule Policy And Registry Parsing

**Files:** Create `scripts/github_capsule_policy.py`; create `tests/test_github_capsule_policy.py`; modify `scripts/github_registry.py`; modify `tests/test_github_registry.py`.

**Produces:** frozen `PackageOverride`, `SecretAllowlist`, `CapsuleConfig`, `EffectivePolicy`; `RepoConfig.capsules`; `RepoConfig.secret_allowlist`; `build_effective_policy`.

- [ ] Write failing tests for exact nested keys/defaults, duplicate rejection, package overrides, unsafe paths, applicable-allowlist filtering, deterministic policy hash, and rejection of mutable `policy_hash`/progress fields.
- [ ] Run `python3 -m unittest tests.test_github_capsule_policy tests.test_github_registry -v`; expect schema failures.
- [ ] Implement exact dataclasses and parsing; add only `capsules` and `secret_allowlist` to repository optional keys; preserve all existing `RepoConfig` defaults.
- [ ] Run `python3 -m unittest tests.test_github_capsule_policy tests.test_github_registry tests.test_toml_compat tests.test_fetch_psp -v`; expect all pass.
- [ ] Commit with `git commit -m "feat: parse github capsule policy"`.

### Task 3: Exact Git Tree Reader

**Files:** Create `scripts/github_git_tree.py`; create `tests/test_github_git_tree.py`; modify `tests/github_test_support.py`.

**Produces:** `GitBlob(path, oid, mode, size)` and `GitTree(repo_root, sha)` with `blobs()`, `read_blob(path)`, and duplicate-key-rejecting `read_json(path)`.

- [ ] Add commits containing regular, executable, symlink, gitlink, LFS-pointer, binary, NUL, and dirty-worktree variants.
- [ ] Write failing tests proving reads use `git ls-tree -rz --long <sha>` and `git cat-file blob <sha>:<path>`, not working-tree bytes.
- [ ] Implement exact parsing, safe POSIX path checks, and bounded blob reads without checkout execution.
- [ ] Run `python3 -m unittest tests.test_github_git_tree tests.test_github_git -v`; expect all pass.
- [ ] Commit with `git commit -m "feat: read exact github commit trees"`.

### Task 4: NPM Workspace And Exports Resolver

**Files:** Create `scripts/github_npm_workspace.py`; create `tests/test_github_npm_workspace.py`; modify `tests/github_test_support.py`.

**Produces:** `WorkspacePackage`, `DependencyEdge`, `DeclaredTarget`, `WorkspaceResolution`; `resolve_workspace(tree, capsule)`.

- [ ] Add a monorepo fixture with root/list/object workspaces, overlapping `*` patterns, internal dependency/optional/peer edges, cycles, local protocols, tracked types, conditional and array exports, null blocks, and slash-containing pattern substitutions.
- [ ] Write failing tests for closure precedence, peer metadata, RFC 6901 pointers, condition/array order, root sugar, unsafe/mixed export keys, generated targets, and unsupported workspace patterns.
- [ ] Implement workspace discovery and exports traversal exactly; never call Node or package scripts.
- [ ] Run `python3 -m unittest tests.test_github_npm_workspace -v`; expect all pass.
- [ ] Commit with `git commit -m "feat: resolve github npm workspaces"`.

### Task 5: Capsule Classification, Secret Scan, And Budgets

**Files:** Create `scripts/github_capsule_selection.py`; create `tests/test_github_capsule_selection.py`.

**Consumes:** Tasks 2-4. **Produces:** `CapsuleFile`, `SecretFinding`, `CapsuleResolution`; `resolve_npm_capsule(tree, capsule, allowlist)`.

- [ ] Write failing tests for required-rule precedence, tests/stories/fixtures exclusions, declaration directories, exact generated policy, executable blobs, every unsafe Git mode/content class, all `text-secrets-v1` vectors, exact allowlisting, and each file/count/byte boundary.
- [ ] Implement deterministic classification and secret scanning with no matched secret text in reports.
- [ ] Compute applicable allowlist from selected candidate blobs, then compute the effective policy and final required set.
- [ ] Run `python3 -m unittest tests.test_github_capsule_selection -v`; expect all pass.
- [ ] Commit with `git commit -m "feat: classify github source capsules"`.

### Task 6: Durable IO And Crash Harness

**Files:** Create `scripts/github_durable_io.py`; create `tests/test_github_durable_io.py`.

**Produces:** `DurableIO`, `InjectedCrash`, `FailpointController(target_site: Optional[str], target_occurrence: Optional[int])`, and a trace of every actual durable site and occurrence covering namespace mkdir, file write, file fsync, hard link, rename, unlink, source-parent fsync, and destination-parent fsync.

`DurableIO` has exact descriptor-based methods `__init__(failpoints: Optional[FailpointController] = None)`, `bootstrap_directory_at(parent_fd: int, components: Sequence[str]) -> int`, `write_fsync_at(parent_fd: int, name: str, content: bytes) -> os.stat_result`, `fsync_directory(descriptor: int, site: str) -> None`, `link_no_replace_at(source_parent_fd: int, source_name: str, destination_parent_fd: int, destination_name: str) -> None`, `rename_fsync_both_at(source_parent_fd: int, source_name: str, destination_parent_fd: int, destination_name: str) -> None`, and `unlink_fsync_parent_at(parent_fd: int, name: str) -> None`.

- [ ] Write a baseline trace test that records ordered `(site, occurrence)` entries for every actual durable call, then inject exactly one `InjectedCrash` at every recorded entry, discard the first `DurableIO` instance without cleanup, create a fresh instance, and inspect only reopened filesystem state.
- [ ] Implement no-follow component traversal and all six durable operations; production defaults to no failpoint.
- [ ] Run `python3 -m unittest tests.test_github_durable_io -v`; expect every recorded site occurrence to leave a documented pre- or post-operation state.
- [ ] Commit with `git commit -m "feat: add github durable io primitives"`.

### Task 7: Immutable Event Histories

**Files:** Create `scripts/github_events.py`; create `tests/test_github_events.py`.

**Consumes:** Task 6. **Produces:** `publish_event`, `load_event_history`, `recover_event_staging`, and exact event hash-chain validation.

- [ ] Write failing tests for canonical event hash/name, sequence and previous hash, frozen legacy-prefix binding, staged-only recovery, linked-before-fsync recovery, cleanup recovery, unexpected destination rejection, and no new JSONL.
- [ ] Implement sibling history/staging namespaces and no-replace hard-link publication through `DurableIO`.
- [ ] Record a baseline publication trace and every staged-only/linked-only/cleanup recovery trace. Inject at each exact `(site, occurrence)` in publication and in each recovery branch, then reopen with a second recovery pass; expect convergence or `recovery-required` only for conflicting bytes.
- [ ] Commit with `git commit -m "feat: add immutable github event histories"`.

### Task 8: Transaction Coordinator And Lock Ownership

**Files:** Create `scripts/github_transactions.py`; create `tests/test_github_transactions.py`; modify internal helper signatures in `scripts/github_snapshot.py` and `scripts/github_packets.py` only where coordinator-owned variants are required.

**Consumes:** Shared ownership interfaces and Tasks 6-7. **Produces:** `prepare_transaction`, `publish_transaction`, `recover_repository_transactions`, `inspect_transactions`.

- [ ] Write failing tests proving exact lock order, one acquisition per lock, descriptor identity, context-owned `DurableIO`, typed snapshot/packet/index/run `DirectoryHandle` path-device-inode binding, builders cannot promote or reacquire, prepared-before-publication durability, operation-specific artifact sets, and terminal-run forward boundary.
- [ ] Implement `PublicationContext` creation and internal `stage_*_with_context` adapters; retain existing public v1 helpers unchanged outside transactions. Builders file-`fsync` staged regular files and directory-`fsync` every staging directory bottom-up through the context descriptor before returning.
- [ ] Implement journal events, ownership hashes, artifact/index/run publication, rollback, and forward recovery using `DurableIO`.
- [ ] For each minimal operation shape, record normal publication plus rollback and forward-recovery traces. Crash at every exact `(site, occurrence)`, reopen, allow recovery itself to crash at every recovery occurrence, then reopen a second time and require convergence.
- [ ] Run `python3 -m unittest tests.test_github_transactions tests.test_github_snapshot tests.test_github_packets -v`; expect all pass.
- [ ] Commit with `git commit -m "feat: coordinate durable github publication"`.

### Task 9: Version-Neutral Format-3 Staging

**Files:** Create `scripts/github_capsule_snapshot.py`; create `tests/test_github_capsule_snapshot.py`; modify `scripts/github_snapshot.py` for format dispatch only.

**Consumes:** Tasks 1, 5, and 8. **Produces:** frozen `CapsuleSnapshot`, `SourceCapsuleInput`, and `DeepDiveCapsuleInput`; `stage_source_capsule(context: PublicationContext, value: SourceCapsuleInput) -> Tuple[CapsuleSnapshot, StagedArtifact]`; `stage_deep_dive_capsule(context: PublicationContext, value: DeepDiveCapsuleInput) -> Tuple[CapsuleSnapshot, StagedArtifact]`; `validate_format3_snapshot(path: Path, expected: Optional[CapsuleSnapshot] = None) -> Tuple[str, ...]`. `DeepDiveCapsuleInput` contains primitive immutable request fields (`request_id`, `question_hash`, sorted path/reason rows, files, and effective policy) and does not import Task 14 request types.

- [ ] Write failing tests for exact top-level/nested schemas, commit-only ref, `<sha>:c0` locators, version-neutral bytes/path derivation, exact Git object/mode/hash/size, ordering, purpose-specific fields, and offline embedded-policy validation.
- [ ] Implement staging only below `context.staged_artifacts_root`; require `context.snapshot_lock`; return `StagedArtifact` and never promote.
- [ ] Route format 3 validation without altering format-1/2 parsers or bytes.
- [ ] Run `python3 -m unittest tests.test_github_capsule_snapshot tests.test_github_snapshot -v`; expect all pass.
- [ ] Commit with `git commit -m "feat: stage github format three capsules"`.

### Task 10: Unified Index V2 And V1 Command Compatibility

**Files:** Create `scripts/github_index_v2.py`; create `tests/test_github_index_v2.py`; modify `scripts/github_packets.py`; modify `tests/test_github_packets.py`; modify `scripts/collect_github_repos.py`; modify `tests/test_collect_github_repos.py`.

**Produces:** `CaptureRecord`, `VersionRecord`, `VersionIndexV2`, `VersionIndexView`, and the five shared version-state functions defined above; `bind_version_package_v1`, `migrate_v1_to_v2`, `attach_capture`.

- [ ] Write failing tests for exact IDs, legacy projection, plain-tag binding during migration and future collection, package/branch/commit applicability, policy-upgrade captures, bidirectional evidence, older-revision insertion, save/load byte stability, and A-then-B same-SHA attachment.
- [ ] Implement the unified loader, `render_version_state`, and read projection; format absence selects v1, `format_version = 2` selects v2, unknown formats fail, and both atomic save and transaction staging use the same rendered bytes.
- [ ] Implement v2 release writes so normal release collection adds canonical captures/version records after migration. When existing collection creates a new same-SHA format-1/2 release supplement, project it as `legacy-supplement`, derive exact immutable release-evidence applicability, update both directions, and retain packet-v1 output.
- [ ] Add post-migration CLI tests: default-branch collect, future release collect, same-SHA release-note supplement, compare, prepare, and status must all succeed using v2 state while retaining packet-v1 output for non-capsule operations.
- [ ] Run `python3 -m unittest tests.test_github_index_v2 tests.test_github_packets tests.test_collect_github_repos -v`; expect all pass.
- [ ] Commit with `git commit -m "feat: add compatible github index v2"`.

### Task 11: Immutable Packet Lifecycle

**Files:** Create `scripts/github_lifecycle.py`; create `tests/test_github_lifecycle.py`; modify `scripts/github_reporting.py`; modify `scripts/collect_github_repos.py` packet-state routing.

**Produces:** `LifecycleSeed`; `stage_initial_packet_state(context: PublicationContext, packet_directory_fd: int, packet_id: str, repo_id: str, observed_at: datetime) -> LifecycleSeed`; `load_packet_state`; `transition_packet_state`.

- [ ] Write failing tests for frozen `state-events.jsonl`, legacy hash binding, `state-initialized`, every allowed/forbidden transition, event staging recovery, packet lock ownership, and mixed-history validation.
- [ ] Implement `stage_initial_packet_state` so packet builders place the hash-valid `state-initialized` event inside the staged packet before publication hashing. Implement future transitions under `state-events-v2/`; existing histories remain unchanged.
- [ ] Preserve exact public command: `packet-state --repo <id> --packet <id> --from <state> --to <state>`; acquire collection then packet lock, recover before reading, and reject stale `--from`.
- [ ] Run `python3 -m unittest tests.test_github_lifecycle tests.test_github_reporting tests.test_collect_github_repos -v`; expect all pass.
- [ ] Commit with `git commit -m "feat: add immutable github packet lifecycle"`.

### Task 12: Supplement Packet V2 Staging

**Files:** Create `scripts/github_supplement_packets.py`; create `tests/test_github_supplement_packets.py`; modify `scripts/github_packets.py` for packet format dispatch only.

**Consumes:** Tasks 8-11. **Produces:** `stage_supplement_packet(context: PublicationContext, config: RepoConfig, before: VersionRecord, after: VersionRecord, added_capture_ids: Sequence[str], index: VersionIndexV2) -> Tuple[PacketRecord, StagedArtifact]`; `validate_packet_v2(directory: Path, index: VersionIndexV2) -> Tuple[str, ...]`.

- [ ] Write failing tests for proper-subset endpoints, ordered set difference not limited to suffixes, applicable captures, exact required-reading order/deduplication, canonical packet ID/label, actual-budget exclusion from identity, initial lifecycle event inclusion, publication hash, sequence-one lifecycle seed binding, stable hash excluding only later lifecycle events, and all budget boundaries.
- [ ] Implement staging below coordinator root; require packet lock; call `stage_initial_packet_state` before directory hashing; return `StagedArtifact` with `validation_profile = "packet-lifecycle-v2"` and the exact `initial_lifecycle_event_hash`; never promote independently.
- [ ] Validate completed packet journals by reconstructing `stable_content_hash` from immutable packet files plus the exact sequence-one event and independently validating the complete lifecycle chain; nonterminal recovery uses exact publication `content_hash`.
- [ ] Preserve all packet-v1 parsing/building behavior.
- [ ] Run `python3 -m unittest tests.test_github_supplement_packets tests.test_github_lifecycle tests.test_github_packets -v`; expect all pass.
- [ ] Commit with `git commit -m "feat: stage github supplement packets"`.

### Task 13: Persistent Retry And Quarantine

**Files:** Create `scripts/github_retry.py`; create `tests/test_github_retry.py`.

**Produces:** `RetryUnit`, `RetryState`, `record_failure`, `record_success`, `reset_retry`, `reduce_retry_history`, `due_retry_units`.

- [ ] Write failing tests for one key across phases, stored `run_id` in attempt/reset IDs, 15-minute/2-hour/24-hour delays, attempt-four quarantine, deterministic-policy review, reset epochs, legacy prefix hash, due dedupe, lock-time recheck, and committed-transaction success reconciliation.
- [ ] Implement events below `collection-failures/events/` through Task 7; store no credentials or unbounded exception prose.
- [ ] Run `python3 -m unittest tests.test_github_retry -v`; expect all pass.
- [ ] Commit with `git commit -m "feat: persist github collection retries"`.

### Task 14: Safe Same-SHA Deep Dives

**Files:** Create `scripts/github_deep_dive.py`; create `tests/test_github_deep_dive.py`; modify `rules/query-and-synthesis.md`.

**Produces:** `DeepDiveRequest`, `load_deep_dive_request`, `resolve_deep_dive`, `check_deep_dive_replay`.

- [ ] Write failing tests for exact request schema/hash, `policy_revision`, one version/SHA, sorted reasons/paths, every unsafe Git/content class, secret findings, embedded-policy unchanged replay, current-policy drift, and explicit-revision recapture.
- [ ] Implement selection through `GitTree` and staging through Task 9; execute no repository code.
- [ ] Correct the query rule to create an immutable same-SHA request rather than edit accepted raw evidence.
- [ ] Run `python3 -m unittest tests.test_github_deep_dive -v`; expect all pass.
- [ ] Commit with `git commit -m "feat: add safe github deep dives"`.

### Task 15: CLI Operations, Reporting, And Validation

**Files:** Create `scripts/github_capsule_validation.py`; create `tests/test_github_capsule_validation.py`; modify `scripts/collect_github_repos.py`, `scripts/github_reporting.py`, `scripts/github_validation.py`, `scripts/validate_github_collection.py`, `tests/test_collect_github_repos.py`, and `tests/test_github_validation.py`.

**Adds exact commands:**

```text
migrate-index-v2 --repo <id> [--dry-run]
collect --repo <id> --capsules [--capsule-scope selected|all-indexed] [--dry-run]
deep-dive --repo <id> --request <tracking-json-path> [--dry-run]
recover --repo <id>
retry-due [--repo <id>]
retry-reset --repo <id> --operation capsule|deep-dive|index-migration|recover --selector <selector> --unit-id <id> --actor <id> --reason <text>
packet-state --repo <id> --packet <id> --from <state> --to <state>
```

- [ ] Write failing parser/dispatch tests for every required/forbidden argument combination, dry-run no-write behavior, exact operation IDs, and lifecycle/retry lock-time rechecks.
- [ ] Generate command `run_id` before registry loading; on invalid registry publish one command-level immutable failure report with sanitized args hash and no repository/retry fields.
- [ ] Integrate migration and capsule collect/attach/check through Task 8. Every capsule command, including dry-run, requires an already committed v2 index; `--capsule-scope all-indexed` enumerates version-scoped `(version_id, capsule_id, policy_hash)` scheduling units. For each unit, capture lookup separately reuses `(sha, adapter, capsule_id, policy_hash)` raw evidence and chooses collect, attach, or check, so same-SHA versions each receive their own applicability and packet decision.
- [ ] Integrate deep-dive collect/check end to end: load and replay the request, stage format-3 evidence and packet when absent, attach bidirectional index applicability, publish one `deep-dive-collect` transaction, or publish a no-artifact `deep-dive-check` transaction when unchanged.
- [ ] Wrap scheduled capsule, deep-dive, migration, and recovery units with retry recording after a trustworthy unit exists; record success after committed publication, reconcile interrupted success, and make `retry-due` dispatch the exact stored operation/selector/unit ID through the same command handlers.
- [ ] Delegate new read-only validation to `github_capsule_validation.py`; keep legacy parsers in `github_validation.py`.
- [ ] Run `python3 -m unittest tests.test_collect_github_repos tests.test_github_capsule_validation tests.test_github_validation -v`, then `python3 -m unittest discover -s tests`, then `python3 scripts/validate_github_collection.py`; expect all tests and GitHub validation pass.
- [ ] Commit with `git commit -m "feat: integrate github capsule operations"`.

### Task 16: Full Local Topology And PayPal JS Policy

**Files:** Create `tests/test_github_capsule_pipeline.py`; modify `tests/github_test_support.py`; modify `tracking/github/repo-registry.toml`.

- [ ] Build 15 canonical captures and 15 immutable legacy packet-v1 directories in a local fixture, with package/tag/branch/commit identities and at least one shared-SHA pair.
- [ ] Migrate to v2, collect one main source capsule, attach or collect 14 later supplements/packets, exercise one policy upgrade, reject an ineligible sibling package, and verify exact 15-canonical/15-legacy/1-main/14-later topology.
- [ ] Run representative collect, attach, policy-upgrade, deep-dive, and retry interruption smoke cases against the 15-capture topology; exhaustive occurrence-level publication and recovery matrices remain the minimal per-operation tests in Tasks 7-8.
- [ ] Add generic `react-paypal-js-runtime` registry policy with no PayPal-specific code, no resolved SHAs/versions/dates/progress, tracked `src`/`types`, reviewed `dist/` and `index.js`, and default limits.
- [ ] Run `python3 -m unittest tests.test_github_capsule_pipeline -v`, full discovery, GitHub validator, wiki validator, and `git diff --check`; treat the existing 17 wiki issues as baseline.
- [ ] Commit code/config/tests with `git commit -m "test: prove generic github capsule topology"`.
- [ ] In a separate follow-up documentation commit, add the completed conformance commit hash and local commands to the specification; do not claim live audit completion.

### Task 17: PayPal JS Dry-Run Conformance Pilot

**Files:** Before approval, no writes. After explicit migration approval, generated index-v2, migration transaction, and terminal run event only; no raw capsule, supplement packet, source, or ingest writes.

- [ ] Verify a clean branch, full unit suite, and GitHub validator before network access.
- [ ] Run `python3 scripts/collect_github_repos.py migrate-index-v2 --repo paypal/paypal-js --dry-run`; report the exact migration projection and stop for separate explicit approval.
- [ ] Only after that approval, run `python3 scripts/collect_github_repos.py migrate-index-v2 --repo paypal/paypal-js`, verify committed index-v2 round trip and migration transaction, and rerun the deterministic validators.
- [ ] Run `python3 scripts/collect_github_repos.py collect --repo paypal/paypal-js --capsules --capsule-scope all-indexed --dry-run` against the committed v2 index; audit every unique eligible indexed SHA without raw or packet persistence.
- [ ] Report all 15 SHAs, package closures, selected files/bytes, exclusions, generated targets, policy hashes, packet budgets, and collect/attach/check decisions.
- [ ] Stop. Migration apply and capsule collection are separate approvals; do not collect capsules, approve packets, or ingest without another explicit approval.

## Completion Gate

1. Every Task 1-16 commit passes focused tests and a task-scoped skeptical review.
2. Post-migration `collect`, `compare`, `prepare`, `status`, and packet-state compatibility tests pass.
3. A whole-branch review of `96277b2..HEAD` has no unresolved Critical or Important findings.
4. Full unit discovery and `validate_github_collection.py` pass; wiki-validator baseline is reported separately.
5. Task 17 applies only an explicitly approved index migration; capsule collection remains dry-run and no ingest begins.

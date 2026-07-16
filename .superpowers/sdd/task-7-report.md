# Task 7: Version Index and Ingest Packet Evidence

## Scope

Implemented only the Task 7 deliverables:

- `scripts/github_packets.py`
- `tests/test_github_packets.py`
- this report

The implementation does not ingest wiki content and does not write generated
patches, packet files, or index state under `raw/`. The local tests create
temporary raw snapshots solely as immutable input evidence; generated packet
artifacts are asserted to stay below temporary `tracking/github/` paths.

## Design Evidence

### Version index

- `VersionEntry`, `VersionIndex`, and `PacketRecord` are frozen dataclasses.
- `record_snapshot` creates at most one canonical entry for a SHA, merges
  aliases deterministically, and retains exact release-note/changelog paths.
- Supplement snapshots update evidence for an existing SHA without creating a
  second version entry. A supplement with no canonical entry is ignored.
- `select_prior` uses the greatest earlier semantic version within the exact
  package namespace. It derives that namespace from either the resolved ref
  name or one unambiguous package-tag alias. Branches instead select the most
  recent prior capture on the same branch.
- `save_version_index` writes sorted-key JSON with a final newline through a
  temporary sibling followed by `os.replace`.

### Packets

- Baseline, delta, and comparison packets always start in `awaiting-review`.
- Packet JSON, Markdown, changed-file lists, source patches, and initial state
  events are generated only below the supplied tracking packet root.
- Delta/comparison Git calls use argument lists through `subprocess.run`; no
  shell is used. Source patches use `git diff --find-renames --no-ext-diff
  --no-textconv FROM_SHA TO_SHA -- SELECTED_PATHS`.
- Selected diff paths are limited to retained snapshot evidence and exclude
  configured exclusions, default high-churn directories, and lockfiles.
- Required reading is deterministic: snapshot manifests, available exact
  release notes, retained changelogs, then changed evidence paths. Packet
  Markdown explicitly records absent release notes or changelogs.
- Generated Markdown labels immutable raw evidence separately from generated
  tracking guidance.

## TDD Evidence

### RED

1. Added `tests/test_github_packets.py` before `github_packets.py` existed.
2. Ran:

   ```text
   python3 -m unittest tests.test_github_packets -v
   ```

   Result: expected `ModuleNotFoundError: No module named 'github_packets'`
   (`Ran 1 test`, failed import).

3. Added an alias-derived package prior-selection regression after the initial
   implementation and ran:

   ```text
   python3 -m unittest tests.test_github_packets.GitHubPacketTests.test_package_alias_on_a_plain_tag_keeps_prior_selection_in_its_namespace -v
   ```

   Result: expected behavioral failure because `select_prior` only inspected
   `ref_name` and returned `None` for a plain-tag alias of a package release.

### GREEN

After implementing `github_packets.py` and extending package extraction to
read an unambiguous package-tag alias, ran:

```text
python3 -m unittest tests.test_github_packets -v
```

Result: `Ran 8 tests` / `OK`.

The focused tests cover canonical SHA alias deduplication, package and branch
prior selection, supplement evidence retention without a second version,
deterministic JSON index persistence, baseline/delta/comparison states, local
Git added/modified/renamed/deleted output, required raw evidence paths, and
the raw/tracking patch boundary.

## Full Verification

```text
python3 -m unittest discover -s tests -v
```

Result: `Ran 175 tests in 6.307s` / `OK`.

```text
git diff --check
git diff --cached --check
```

Result: both completed with no output (clean whitespace checks).

## Commit Evidence

Feature implementation commit:

```text
e32d043 feat: generate github ingest packets
```

## Remaining Boundary

Task 7 exposes packet/index primitives only. The later collection CLI and
reporting tasks must call `record_snapshot`/`save_version_index`, choose one
newly collected release at a time, and invoke the corresponding packet builder.
They must not transition a packet out of `awaiting-review` automatically.

## Review Remediation Evidence

### RED

- Added focused regressions before the implementation change for a SHA shared by
  two package namespaces, strict index schemas and evidence paths, tracking-only
  packet roots, retry state preservation, injected packet-write cleanup, and
  conflicting deterministic packet directories.
- `python3 -m unittest tests.test_github_packets -v` ran 15 tests with 17
  expected failures. The failures showed scalar package matching dropped the
  second namespace, permissive index parsing trusted unsafe input, packet roots
  could target `raw/` or a symlink escape, and retries overwrote packet state.

### GREEN

- A canonical entry still uses the approved `VersionEntry` schema, while prior
  selection derives all compatible package identities from its canonical ref,
  aliases, and scalar package. A direct package ref selects only its own
  namespace; an alias-only ref must identify exactly one namespace, so unrelated
  packages are never conflated.
- Version-index loading now rejects duplicate JSON keys, unknown or missing
  keys, wrong exact types, malformed identity fields, unsorted or duplicate
  aliases/evidence lists, duplicate SHA or reference entries, repository
  mismatches, and unsafe snapshot, release-note, or changelog paths. Paths are
  checked both lexically and after resolution beneath the repository-specific
  `raw/github/<company>/<repo>/` evidence root implied by the index path.
- Packet builders require a lexical and resolved `tracking/github/` root with no
  symlink component and reject traversal or `raw/` destinations before writing.
  Direct `VersionEntry` inputs receive the same evidence containment validation.
- Packet publication now uses a stable advisory `.packet.lock`, creates all
  artifacts in a temporary sibling, and renames only a completed directory.
  Existing valid deterministic packets are reused without changing their state
  event history; malformed or conflicting directories fail without overwrite.
  Temporary packet directories are removed after any write failure.

## Final Verification

- `python3 -m unittest tests.test_github_packets -v`: 15 passed.
- `python3 -m unittest discover -s tests -v`: 182 passed.
- `git diff --check`: passed with no output.

## Final Parser Correction

- A final strict-parser review found that the single-character Git reference
  `@` was still accepted for branch and alias fields. A focused RED run failed
  for both cases, then the ref validator was tightened to reject `@`, leading
  dot/slash components, repeated slashes, and nested `.lock` components.
  Focused tests remained 15/15 and the full suite remained 182/182.

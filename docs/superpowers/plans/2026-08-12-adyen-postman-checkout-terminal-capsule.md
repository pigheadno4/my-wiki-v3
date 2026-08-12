# Adyen Postman Checkout And Terminal Capsule Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable commit-qualified collection of the current Adyen Checkout and Terminal Postman evidence, validate its Postman schemas and filename sentinel, and publish one immutable baseline work item that stops at packet review.

**Architecture:** Reuse the existing `commit-tree-v1` exact-file capsule and common GitHub collector. Add one small provider-neutral validator for Postman v2.1 JSON plus required sentinel references, configure the existing Adyen registry row with ten exact paths, and publish one exact-SHA baseline without editing wiki knowledge.

**Tech Stack:** Python 3 `unittest`, JSON, TOML registry configuration, Git, existing GitHub collection CLI, immutable raw evidence.

## Global Constraints

- Collect exactly five JSON evidence files and five provenance files from one resolved default-branch SHA; the common collector additionally retains root `LICENSE` as repository context.
- The selected JSON files are Checkout v72, Recurring v68, BinLookup v54, Test Cards v1, and `in-person-payments/ipp.json`.
- The selected provenance files are `in-person-payments/readme.md`, `README.md`, `adyendev-postman-release-notes.md`, `generateAll.sh`, and `.github/workflows/sync-collections.yml`.
- Require Postman Collection v2.1 JSON and require the sync workflow to reference Checkout v72, Recurring v68, BinLookup v54, and Test Cards v1 before packet approval.
- Per-file limit is 600,000 bytes; capsule limits are 11 published files and 1,100,000 UTF-8 bytes; packet limits are 30 files and 3,000,000 UTF-8 bytes.
- Treat the default-branch commit as repository identity; API labels such as Checkout v72 are evidence attributes, not repository releases.
- Missing evidence, invalid JSON, wrong Postman schema, sentinel mismatch, strict UTF-8 failure, secret finding, hash mismatch, or budget overflow blocks packet approval.
- Baseline collection stops at `awaiting_approval`; do not approve, call `next-ingest`, or edit `wiki/`.
- Leave unrelated workspace files, including `CLAUDE copy.md`, untouched.

---

### Task 1: Add a reusable Postman snapshot validator

**Files:**
- Create: `scripts/validate_postman_capsule.py`
- Create: `tests/test_validate_postman_capsule.py`

**Interfaces:**
- Consumes: a snapshot directory containing `files/`, relative Postman JSON paths, one relative sentinel path, and required literal sentinel references.
- Produces: `validate_postman_capsule(snapshot_dir: Path, postman_paths: Sequence[str], sentinel_path: str, sentinel_references: Sequence[str]) -> ValidationResult`; raises `PostmanCapsuleValidationError` on missing files, invalid JSON, wrong schema, or missing sentinel references.
- CLI: `python3 scripts/validate_postman_capsule.py SNAPSHOT_DIR --postman-path PATH ... --sentinel-path PATH --sentinel-reference TEXT ...` exits zero and prints a JSON summary only when every check passes.

- [ ] **Step 1: Write failing validator tests**

Create `tests/test_validate_postman_capsule.py` with:

```python
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_postman_capsule import (  # noqa: E402
    PostmanCapsuleValidationError,
    validate_postman_capsule,
)


SCHEMA_V21 = "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path, payload):
    write_text(path, json.dumps(payload))


class PostmanCapsuleValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.snapshot = Path(self.directory.name)
        self.postman_path = "postman/CheckoutService-v72.json"
        self.sentinel_path = ".github/workflows/sync-collections.yml"

    def test_accepts_v21_collections_and_complete_sentinel(self):
        write_json(
            self.snapshot / "files" / self.postman_path,
            {"info": {"schema": SCHEMA_V21}, "item": []},
        )
        write_text(
            self.snapshot / "files" / self.sentinel_path,
            "CheckoutService-v72.json\nRecurringService-v68.json\n",
        )

        result = validate_postman_capsule(
            self.snapshot,
            (self.postman_path,),
            self.sentinel_path,
            ("CheckoutService-v72.json", "RecurringService-v68.json"),
        )

        self.assertEqual(1, result.postman_file_count)
        self.assertEqual(2, result.sentinel_reference_count)

    def test_rejects_invalid_json(self):
        write_text(self.snapshot / "files" / self.postman_path, "{")

        with self.assertRaisesRegex(
            PostmanCapsuleValidationError,
            r"invalid-postman-json: postman/CheckoutService-v72\.json",
        ):
            validate_postman_capsule(
                self.snapshot,
                (self.postman_path,),
                self.sentinel_path,
                ("CheckoutService-v72.json",),
            )

    def test_rejects_wrong_postman_schema(self):
        write_json(
            self.snapshot / "files" / self.postman_path,
            {
                "info": {
                    "schema": "https://schema.getpostman.com/json/collection/v2.0.0/collection.json"
                }
            },
        )

        with self.assertRaisesRegex(
            PostmanCapsuleValidationError,
            r"wrong-postman-schema: postman/CheckoutService-v72\.json",
        ):
            validate_postman_capsule(
                self.snapshot,
                (self.postman_path,),
                self.sentinel_path,
                ("CheckoutService-v72.json",),
            )

    def test_rejects_missing_sentinel_reference(self):
        write_json(
            self.snapshot / "files" / self.postman_path,
            {"info": {"schema": SCHEMA_V21}},
        )
        write_text(
            self.snapshot / "files" / self.sentinel_path,
            "CheckoutService-v72.json\n",
        )

        with self.assertRaisesRegex(
            PostmanCapsuleValidationError,
            "missing-sentinel-reference: RecurringService-v68.json",
        ):
            validate_postman_capsule(
                self.snapshot,
                (self.postman_path,),
                self.sentinel_path,
                ("CheckoutService-v72.json", "RecurringService-v68.json"),
            )

    def test_rejects_missing_selected_file(self):
        with self.assertRaisesRegex(
            PostmanCapsuleValidationError,
            r"missing-postman-file: postman/CheckoutService-v72\.json",
        ):
            validate_postman_capsule(
                self.snapshot,
                (self.postman_path,),
                self.sentinel_path,
                ("CheckoutService-v72.json",),
            )


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the tests and verify they fail**

```bash
python3 -m unittest tests.test_validate_postman_capsule -v
```

Expected: FAIL because `validate_postman_capsule` does not exist.

- [ ] **Step 3: Implement the minimal validator and CLI**

Create `scripts/validate_postman_capsule.py` with:

```python
import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Sequence


POSTMAN_V21_SCHEMA = (
    "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
)

@dataclass(frozen=True)
class ValidationResult:
    postman_file_count: int
    sentinel_reference_count: int

class PostmanCapsuleValidationError(ValueError):
    pass

def validate_postman_capsule(
    snapshot_dir: Path,
    postman_paths: Sequence[str],
    sentinel_path: str,
    sentinel_references: Sequence[str],
) -> ValidationResult:
    files_root = snapshot_dir / "files"
    for relative_path in postman_paths:
        path = files_root / relative_path
        if not path.is_file():
            raise PostmanCapsuleValidationError(
                "missing-postman-file: " + relative_path
            )
        try:
            payload = json.loads(path.read_text(encoding="utf-8", errors="strict"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise PostmanCapsuleValidationError(
                "invalid-postman-json: " + relative_path
            ) from error
        if not isinstance(payload, dict) or not isinstance(payload.get("info"), dict):
            raise PostmanCapsuleValidationError(
                "wrong-postman-schema: " + relative_path
            )
        if payload["info"].get("schema") != POSTMAN_V21_SCHEMA:
            raise PostmanCapsuleValidationError(
                "wrong-postman-schema: " + relative_path
            )

    sentinel = files_root / sentinel_path
    if not sentinel.is_file():
        raise PostmanCapsuleValidationError(
            "missing-sentinel-file: " + sentinel_path
        )
    try:
        sentinel_text = sentinel.read_text(encoding="utf-8", errors="strict")
    except UnicodeDecodeError as error:
        raise PostmanCapsuleValidationError(
            "invalid-sentinel-utf8: " + sentinel_path
        ) from error
    for reference in sentinel_references:
        if reference not in sentinel_text:
            raise PostmanCapsuleValidationError(
                "missing-sentinel-reference: " + reference
            )
    return ValidationResult(len(postman_paths), len(sentinel_references))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("snapshot_dir", type=Path)
    parser.add_argument("--postman-path", action="append", required=True)
    parser.add_argument("--sentinel-path", required=True)
    parser.add_argument("--sentinel-reference", action="append", required=True)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = validate_postman_capsule(
            args.snapshot_dir,
            tuple(args.postman_path),
            args.sentinel_path,
            tuple(args.sentinel_reference),
        )
    except (PostmanCapsuleValidationError, UnicodeDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(
        json.dumps(
            {
                "postman_file_count": result.postman_file_count,
                "sentinel_reference_count": result.sentinel_reference_count,
                "status": "ok",
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run focused and full GitHub tests**

```bash
python3 -m unittest tests.test_validate_postman_capsule -v
python3 -m unittest discover -s tests -p 'test_github_*.py'
```

Expected: all tests pass.

- [ ] **Step 5: Commit the validator**

```bash
git add scripts/validate_postman_capsule.py tests/test_validate_postman_capsule.py
git diff --cached --check
git commit -m "feat: validate Postman evidence capsules"
```

### Task 2: Enable the Adyen Postman exact-file capsule

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`
- Regenerate: `tracking/github/collection-index.json`
- Regenerate: `tracking/github/collection-index.md`

**Interfaces:**
- Consumes: existing exact-file support in `commit-tree-v1` and `load_registry(path)`.
- Produces: one enabled monthly tier-2 commit policy with capsule ID `adyen-postman-checkout-terminal` and source ID `adyen-postman`.

- [ ] **Step 1: Add the failing registry contract test**

Add `test_adyen_postman_has_reviewed_checkout_terminal_policy` to `RegistryTests`:

```python
def test_adyen_postman_has_reviewed_checkout_terminal_policy(self):
    repos = {
        repo.id: repo
        for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
    }
    repo = repos["adyen/adyen-postman"]

    self.assertTrue(repo.enabled)
    self.assertEqual("api-collection", repo.repo_type)
    self.assertEqual("tier2", repo.priority)
    self.assertEqual("monthly", repo.collection_frequency)
    self.assertEqual("default-branch", repo.track)
    self.assertEqual("commit", repo.version_strategy)
    self.assertEqual((), repo.version_tracks)
    self.assertEqual(1, len(repo.capsules))
    capsule = repo.capsules[0]
    self.assertEqual("adyen-postman-checkout-terminal", capsule.id)
    self.assertEqual("commit-tree-v1", capsule.adapter)
    self.assertEqual("adyen-postman", capsule.source_id)
    self.assertEqual("configured-repository-paths", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(
        (
            "in-person-payments/ipp.json",
            "postman/BinLookupService-v54.json",
            "postman/CheckoutService-v72.json",
            "postman/RecurringService-v68.json",
            "postman/TestCardService-v1.json",
        ),
        capsule.default_required_roots,
    )
    self.assertEqual(
        (
            ".github/workflows/sync-collections.yml",
            "README.md",
            "adyendev-postman-release-notes.md",
            "generateAll.sh",
            "in-person-payments/readme.md",
        ),
        capsule.include_paths,
    )
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual(600000, capsule.max_file_bytes)
    self.assertEqual(11, capsule.max_capsule_files)
    self.assertEqual(1100000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(30, capsule.max_packet_files)
    self.assertEqual(3000000, capsule.max_packet_utf8_bytes)
```

Change only the `adyen/adyen-postman` row in `APPENDIX_A_INVENTORY` from disabled to enabled.

- [ ] **Step 2: Run the focused test and verify it fails**

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_adyen_postman_has_reviewed_checkout_terminal_policy
```

Expected: FAIL because the registry row is disabled and has no capsule.

- [ ] **Step 3: Configure the exact ten-file capsule**

Replace only the existing `adyen/adyen-postman` row with:

```toml
[[repos]]
id="adyen/adyen-postman"
collection_frequency="monthly"
company="adyen"
url="https://github.com/Adyen/adyen-postman"
enabled=true
repo_type="api-collection"
priority="tier2"
track="default-branch"
version_strategy="commit"
[[repos.capsules]]
id="adyen-postman-checkout-terminal"
adapter="commit-tree-v1"
source_id="adyen-postman"
dependency_scope="configured-repository-paths"
changed_path_policy="policy-bounded"
default_required_roots=[
  "in-person-payments/ipp.json",
  "postman/BinLookupService-v54.json",
  "postman/CheckoutService-v72.json",
  "postman/RecurringService-v68.json",
  "postman/TestCardService-v1.json",
]
include_paths=[
  ".github/workflows/sync-collections.yml",
  "README.md",
  "adyendev-postman-release-notes.md",
  "generateAll.sh",
  "in-person-payments/readme.md",
]
excluded_categories=["tests", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=600000
max_capsule_files=11
max_capsule_utf8_bytes=1100000
max_packet_files=30
max_packet_utf8_bytes=3000000
```

- [ ] **Step 4: Validate the registry and regression suite**

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_adyen_postman_has_reviewed_checkout_terminal_policy
python3 -m unittest discover -s tests -p 'test_github_*.py'
python3 scripts/collect_github_repos.py status > /private/tmp/adyen-postman-registry-status.md
python3 scripts/validate_github_collection.py
```

Expected: all tests pass, the generated index lists Adyen Postman as enabled with `collect-baseline`, and existing evidence remains valid.

- [ ] **Step 5: Commit the registry profile**

```bash
git add tests/test_github_registry.py \
  tracking/github/repo-registry.toml \
  tracking/github/collection-index.json \
  tracking/github/collection-index.md
git diff --cached --check
git commit -m "feat: enable Adyen Postman collection"
```

### Task 3: Publish and review the immutable baseline

**Files:**
- Generate: `raw/github/adyen/adyen-postman/snapshots/<date>-<short-sha>/`
- Generate: `tracking/github/repos/adyen/adyen-postman/`
- Modify through collector: `tracking/github/work-items.json`
- Modify through collector: `tracking/github/status.md`
- Modify through collector: `tracking/github/collection-index.json`
- Modify through collector: `tracking/github/collection-index.md`
- Must not modify: `wiki/`

**Interfaces:**
- Consumes: enabled registry capsule, Postman validator, and `collect --repo adyen/adyen-postman --mode backfill`.
- Produces: one exact-SHA snapshot, one validated review packet, and one `awaiting_approval` work item with recommended mode `full`.

- [ ] **Step 1: Run the non-publishing dry run**

```bash
python3 scripts/collect_github_repos.py collect \
  --repo adyen/adyen-postman \
  --mode backfill \
  --dry-run | tee /private/tmp/adyen-postman-dry-run.json
```

Expected: discovery resolves one default-branch SHA and reports no published snapshot or work item. Stop unless selection is exactly the ten paths configured in Task 2.

- [ ] **Step 2: Capture the publication boundary**

```bash
git status --porcelain=v1 > /private/tmp/adyen-postman.before
```

Expected: the baseline records only committed task work plus unrelated `CLAUDE copy.md`.

- [ ] **Step 3: Run real baseline collection**

```bash
python3 scripts/collect_github_repos.py collect \
  --repo adyen/adyen-postman \
  --mode backfill | tee /private/tmp/adyen-postman-collection.json
```

Expected: one snapshot and one work item are published; the work item state is `awaiting_approval` and recommended mode is `full`.

- [ ] **Step 4: Resolve and validate the published snapshot**

```bash
SNAPSHOT_DIR=$(dirname "$(find raw/github/adyen/adyen-postman/snapshots -name manifest.json -type f | sort | tail -n 1)")
python3 scripts/validate_postman_capsule.py "$SNAPSHOT_DIR" \
  --postman-path postman/CheckoutService-v72.json \
  --postman-path postman/RecurringService-v68.json \
  --postman-path postman/BinLookupService-v54.json \
  --postman-path postman/TestCardService-v1.json \
  --postman-path in-person-payments/ipp.json \
  --sentinel-path .github/workflows/sync-collections.yml \
  --sentinel-reference CheckoutService-v72.json \
  --sentinel-reference RecurringService-v68.json \
  --sentinel-reference BinLookupService-v54.json \
  --sentinel-reference TestCardService-v1.json
```

Expected: JSON output reports `status: ok`, five Postman files, and four sentinel references. Any failure blocks approval; preserve the published raw evidence, correct policy if needed, recollect the same SHA, and review the replacement packet.

- [ ] **Step 5: Verify evidence integrity and packet boundaries**

```bash
python3 scripts/collect_github_repos.py status
python3 scripts/validate_github_collection.py
find raw/github/adyen/adyen-postman -type f | sort
find tracking/github/repos/adyen/adyen-postman -type f | sort
git status --short
```

Verify the manifest contains exactly ten policy-selected files plus root `LICENSE` as repository context, all hashes validate, total UTF-8 bytes stay within 1,100,000, the packet has zero evidence gaps and zero unclassified retained changes, and no path under `wiki/` changed. Review the packet's full required-reading list and confirm the source identity is `default-branch@<short-sha>`.

- [ ] **Step 6: Commit only generated collection evidence**

```bash
git add raw/github/adyen/adyen-postman \
  tracking/github/repos/adyen/adyen-postman \
  tracking/github/work-items.json \
  tracking/github/status.md \
  tracking/github/collection-index.json \
  tracking/github/collection-index.md
git diff --cached --check
git commit -m "data: collect Adyen Postman baseline"
```

- [ ] **Step 7: Stop at the approval gate**

Report the exact SHA, ten policy-selected paths plus root `LICENSE`, published byte count, Postman validation result, workflow sentinel result, packet findings, and work-item ID. Do not approve or ingest until the user reviews the packet and explicitly selects `full`.

# Stripe PHP Broad Public API Capsule Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable `stripe/stripe-php`, measure and verify a broad public-runtime capsule for `stripe-php@21.0.0`, and publish one approval-gated baseline packet without ingesting it.

**Architecture:** Reuse the existing `tagged-tree-v1` release adapter. A temporary exact-tag inventory measures the complete `lib/**/*.php` runtime plus five root metadata files before registry budgets are set; a TDD registry change locks that boundary, dry-run proves release selection without publication, and real collection publishes immutable evidence before stopping at `awaiting_approval`.

**Tech Stack:** Python 3 `unittest`, TOML registry configuration, Git, the existing GitHub collection CLI, JSON/JQ, immutable Markdown/JSON evidence.

## Global Constraints

- Collector release identity is `stripe-php@21`; Composer package identity is `stripe/stripe-php`.
- Initial baseline is exactly stable `stripe-php@21.0.0`; prereleases and all prior majors are excluded.
- Future collection retains every newer stable `21.x` release; a new major requires a separately reviewed track update.
- Retain all public runtime PHP under `lib/`, including generated resources, services, service parameters, V1/V2 events, OAuth, webhooks, transport, errors, pagination, and Test Helpers API runtime.
- Retain exactly these five root metadata files: `README.md`, `CHANGELOG.md`, `composer.json`, `init.php`, and `LICENSE`. Exclude `.php_cs.dist` as development tooling.
- Exclude repository tests, fixtures, CI, release automation, generated documentation, vendor dependencies, caches, lockfiles, binary assets, and local environment files.
- Final capsule limits are derived from the measured exact-tag inventory: file limit equals measured selected files plus `max(25, ceil(5%))`; byte limit equals measured selected UTF-8 bytes plus `max(500000, ceil(10%))`, rounded up to the next 100,000 bytes; packet limits equal capsule limits plus 20 files and 500,000 bytes.
- `max_file_bytes` remains 1,000,000 and `secret_detector` remains `text-secrets-v1`.
- If the complete broad capsule cannot satisfy safety checks, collector limits, or practical full-read serial ingest, stop for policy review. Do not omit API domains or increase limits ad hoc.
- Collection may publish raw and tracking evidence but must stop at `awaiting_approval`; do not approve, claim ingest, or edit `wiki/`.
- Leave unrelated `CLAUDE copy.md` untouched.

---

### Task 1: Measure the exact stable broad capsule without publishing

**Files:**
- Read: `docs/superpowers/specs/2026-08-14-stripe-php-broad-public-api-capsule-design.md`
- Read: temporary clone under `/private/tmp/`
- Modify: none

**Interfaces:**
- Consumes: official tag `v21.0.0` from `https://github.com/stripe/stripe-php.git`.
- Produces: exact tag SHA, stable/prerelease evidence, selected file count, selected UTF-8 byte count, largest selected file, and deterministic budget values for Task 2.

- [ ] **Step 1: Record repository state and create an isolated temporary path**

Run:

```bash
git status --short
mktemp -d /private/tmp/stripe-php-v21-inventory.XXXXXX
```

Expected: repository status shows only unrelated existing work; save the printed temporary path as `$TMP_STRIPE_PHP` for this task. Do not remove or overwrite any pre-existing path.

- [ ] **Step 2: Fetch the exact stable tag without checking out the workspace repository**

Run, replacing `$TMP_STRIPE_PHP` with the path printed in Step 1:

```bash
git clone --filter=blob:none --no-checkout --branch v21.0.0 --single-branch https://github.com/stripe/stripe-php.git "$TMP_STRIPE_PHP/repo"
git -C "$TMP_STRIPE_PHP/repo" rev-parse 'refs/tags/v21.0.0^{commit}'
git -C "$TMP_STRIPE_PHP/repo" ls-remote --tags origin 'refs/tags/v21*'
```

Expected: `v21.0.0` resolves to one full commit SHA. Any `v21.1.0-alpha.*`, `-beta.*`, or `-rc.*` tags remain excluded; no stable version newer than `21.0.0` may be silently ignored. If a newer stable v21 tag exists, stop and revise the pinned version through design review.

- [ ] **Step 3: Verify the five root metadata files and complete runtime root**

Run:

```bash
git -C "$TMP_STRIPE_PHP/repo" ls-tree -r --name-only v21.0.0 -- README.md CHANGELOG.md composer.json init.php LICENSE lib
git -C "$TMP_STRIPE_PHP/repo" ls-tree -r --name-only v21.0.0 -- tests test fixtures .github vendor docs
```

Expected: the first command lists the five approved metadata files plus all `lib/` paths. `.php_cs.dist` is not retained. The second command is inventory-only and none of its paths enter the capsule.

- [ ] **Step 4: Produce deterministic selected-file measurements**

Run this from the temporary clone:

```bash
git -C "$TMP_STRIPE_PHP/repo" ls-tree -r -l v21.0.0 -- README.md CHANGELOG.md composer.json init.php LICENSE lib | awk -F '\t' '
BEGIN { roots["README.md"]=1; roots["CHANGELOG.md"]=1; roots["composer.json"]=1; roots["init.php"]=1; roots["LICENSE"]=1 }
{
  split($1, meta, " "); size=meta[4]; path=$2
  if (roots[path] || path ~ /^lib\/.*\.php$/) {
    count++; bytes+=size
    if (size > largest) { largest=size; largest_path=path }
  }
}
END {
  file_extra=int(count*0.05+0.999999); if (file_extra < 25) file_extra=25
  byte_extra=int(bytes*0.10+0.999999); if (byte_extra < 500000) byte_extra=500000
  capsule_bytes=int((bytes+byte_extra+99999)/100000)*100000
  print "selected_files=" count
  print "selected_utf8_bytes=" bytes
  print "largest_file_path=" largest_path
  print "largest_file_bytes=" largest
  print "max_capsule_files=" count+file_extra
  print "max_capsule_utf8_bytes=" capsule_bytes
  print "max_packet_files=" count+file_extra+20
  print "max_packet_utf8_bytes=" capsule_bytes+500000
}'
git -C "$TMP_STRIPE_PHP/repo" ls-tree -r --name-only v21.0.0 -- README.md CHANGELOG.md composer.json init.php LICENSE lib | while IFS= read -r path; do
  case "$path" in
    README.md|CHANGELOG.md|composer.json|init.php|LICENSE|lib/*.php)
      git -C "$TMP_STRIPE_PHP/repo" show "v21.0.0:$path" | iconv -f UTF-8 -t UTF-8 >/dev/null || exit 1
      ;;
  esac
done
```

The command retains only regular blobs for the five named metadata files and paths matching `lib/*.php` recursively. Record the exact SHA from Step 2 and the eight actual measurement lines printed here; do not substitute symbolic values into the registry.

```text
selected files and UTF-8 bytes
largest selected path and byte size
calculated capsule file and byte limits
calculated packet file and byte limits
```

Expected: every selected path is UTF-8 text and no selected file exceeds 1,000,000 bytes. Stop before Task 2 if the selected count or bytes make complete serial reading impractical.

- [ ] **Step 5: Confirm the workspace is unchanged**

Run:

```bash
git status --short
```

Expected: no raw, tracking, registry, test, or wiki file changed. The temporary clone is not committed.

### Task 2: Enable and lock the measured Stripe PHP registry profile

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`

**Interfaces:**
- Consumes: Task 1's exact SHA and four deterministic budget values.
- Produces: one enabled `stripe/stripe-php` policy using `tagged-tree-v1`, release identity `stripe-php`, required root `lib`, and the measured budgets.

- [ ] **Step 1: Add the failing registry contract test**

Change the `stripe/stripe-php` expected inventory tuple from disabled to enabled. Add this test to `RegistryTests`:

```python
def test_stripe_php_uses_broad_public_runtime_tagged_profile(self):
    repos = {
        repo.id: repo
        for repo in load_registry(ROOT / "tracking/github/repo-registry.toml")
    }
    repo = repos["stripe/stripe-php"]

    self.assertTrue(repo.enabled)
    self.assertEqual(
        (
            VersionTrack(
                "package:stripe-php@21",
                "latest-stable",
                "all-stable",
                False,
                ("21.0.0",),
            ),
        ),
        repo.version_tracks,
    )
    self.assertEqual(1, len(repo.capsules))
    capsule = repo.capsules[0]
    self.assertEqual("stripe-php-public-runtime", capsule.id)
    self.assertEqual("tagged-tree-v1", capsule.adapter)
    self.assertEqual(("stripe-php",), capsule.focus_packages)
    self.assertEqual("configured-repository-paths", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(("lib",), capsule.default_required_roots)
    self.assertEqual((), capsule.default_generated_target_paths)
    self.assertEqual(
        ("CHANGELOG.md", "LICENSE", "README.md", "composer.json", "init.php"),
        capsule.include_paths,
    )
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual("text-secrets-v1", capsule.secret_detector)
    self.assertEqual(1000000, capsule.max_file_bytes)
    self.assertGreater(capsule.max_capsule_files, 25)
    self.assertGreater(capsule.max_capsule_utf8_bytes, 500000)
    self.assertEqual(capsule.max_capsule_files + 20, capsule.max_packet_files)
    self.assertEqual(
        capsule.max_capsule_utf8_bytes + 500000,
        capsule.max_packet_utf8_bytes,
    )
```

- [ ] **Step 2: Run the focused test and verify it fails**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_stripe_php_uses_broad_public_runtime_tagged_profile
```

Expected: FAIL because the registry row is disabled and has no version track or capsule.

- [ ] **Step 3: Implement the measured registry policy**

Set `enabled=true` and add:

```toml
[[repos.version_tracks]]
selector="package:stripe-php@21"
backfill="latest-stable"
future="all-stable"
include_prerelease=false
pinned_versions=["21.0.0"]
[[repos.capsules]]
id="stripe-php-public-runtime"
adapter="tagged-tree-v1"
focus_packages=["stripe-php"]
dependency_scope="configured-repository-paths"
changed_path_policy="policy-bounded"
default_required_roots=["lib"]
default_generated_target_paths=[]
include_paths=["CHANGELOG.md", "LICENSE", "README.md", "composer.json", "init.php"]
excluded_categories=["tests", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=1000000
```

Append the four exact budget integers calculated in Task 1 as `max_capsule_files`, `max_capsule_utf8_bytes`, `max_packet_files`, and `max_packet_utf8_bytes`. Do not add `.php_cs.dist` or another development-only root file.

- [ ] **Step 4: Run focused and registry regression tests**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_stripe_php_uses_broad_public_runtime_tagged_profile
python3 -m unittest tests.test_github_registry tests.test_github_capsule_policy tests.test_github_capsule_selection tests.test_github_tagged_tree
python3 scripts/validate_github_collection.py
```

Expected: all tests pass and the offline validator reports no structural errors.

- [ ] **Step 5: Review and commit only policy and tests**

Run:

```bash
git diff --check
git diff -- tests/test_github_registry.py tracking/github/repo-registry.toml
git status --short
git add tests/test_github_registry.py tracking/github/repo-registry.toml
git commit -m "Enable Stripe PHP collection"
```

Expected: only the registry test and registry policy are committed. `CLAUDE copy.md` remains untracked.

### Task 3: Verify release selection and broad capsule without publication

**Files:**
- Read: `tracking/github/repo-registry.toml`
- Read: temporary collector output
- Modify: none

**Interfaces:**
- Consumes: committed Task 2 policy and `collect --mode backfill --dry-run`.
- Produces: verified stable release identity without raw or work-item publication; Task 1 remains the pre-publication capsule measurement authority.

- [ ] **Step 1: Record pre-run publication state**

Run:

```bash
git status --short
find raw/github/stripe/stripe-php -type f 2>/dev/null || true
jq '[.work_items[] | select(.repo_id == "stripe/stripe-php")] | length' tracking/github/work-items.json
```

Expected: no Stripe PHP raw evidence and work-item count `0`.

- [ ] **Step 2: Run the collector dry-run**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo stripe/stripe-php --mode backfill --dry-run
```

Expected: discovery selects only `stripe-php@21.0.0`, excludes prereleases, resolves the exact Task 1 SHA, and publishes nothing.

- [ ] **Step 3: Prove dry-run immutability and run the broad regression suite**

Run:

```bash
find raw/github/stripe/stripe-php -type f 2>/dev/null || true
jq '[.work_items[] | select(.repo_id == "stripe/stripe-php")] | length' tracking/github/work-items.json
python3 -m unittest tests.test_github_registry tests.test_github_releases tests.test_github_tagged_tree tests.test_github_capsule_policy tests.test_github_capsule_selection tests.test_github_ingest_packets tests.test_collect_github_repos tests.test_github_validation
python3 scripts/validate_github_collection.py
```

Expected: no published Stripe PHP evidence, work-item count `0`, all tests pass, and validation reports no structural errors.

### Task 4: Publish and review the approval-gated baseline

**Files:**
- Create: generated exact-SHA snapshot under `raw/github/stripe/stripe-php/snapshots/`
- Create: generated release record under `raw/github/stripe/stripe-php/releases/stripe-php/21.0.0/`
- Create: generated packet under `tracking/github/repos/stripe/stripe-php/ingest-packets/`
- Modify: generated GitHub work-item, status, and collection-index files

**Interfaces:**
- Consumes: the verified Task 3 policy and exact stable release.
- Produces: one immutable snapshot, one package release record, and one `awaiting_approval` work item recommending full ingest.

- [ ] **Step 1: Run real baseline collection**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo stripe/stripe-php --mode backfill
```

Expected: one `stripe-php@21.0.0` release and exact-SHA snapshot are published. The work item stops at `awaiting_approval`; no wiki file changes.

- [ ] **Step 2: Inspect the generated packet and lifecycle state**

Run:

```bash
python3 scripts/collect_github_repos.py status
python3 scripts/validate_github_collection.py
git status --short
```

Inspect both packet files, the release record and notes, and snapshot manifest. Confirm:

- package identity is `stripe-php@21.0.0`;
- recommendation is `full` because this is an initial baseline;
- required reading includes every retained runtime and metadata file;
- evidence gaps, secret findings, unsafe paths, and unclassified changes are zero;
- file and byte counts match Task 1;
- no comparison is fabricated for the initial baseline;
- no `wiki/` path changed.

- [ ] **Step 3: Run final collection verification**

Run:

```bash
python3 -m unittest tests.test_github_registry tests.test_github_releases tests.test_github_tagged_tree tests.test_github_capsule_policy tests.test_github_capsule_selection tests.test_github_ingest_packets tests.test_collect_github_repos tests.test_github_validation
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all tests pass, validator reports no structural errors, and no whitespace errors exist.

- [ ] **Step 4: Commit only reviewed collection evidence**

Run:

```bash
git status --short
git add raw/github/stripe/stripe-php tracking/github/repos/stripe/stripe-php tracking/github/work-items.json tracking/github/status.md tracking/github/collection-index.json tracking/github/collection-index.md
git diff --cached --stat
git commit -m "Collect Stripe PHP 21.0.0 baseline"
```

Expected: the commit contains only immutable Stripe PHP evidence and generated GitHub tracking state. The item remains `awaiting_approval`; `CLAUDE copy.md` remains untracked.

## Stop Condition and Next Gate

Implementation ends after Task 4. Report the measured broad-capsule size, release identity and SHA, review recommendation, evidence gaps, and validation results. Do not run `approve`, `next-ingest`, or edit wiki content. The next action requires separate user approval of the packet and ingest mode.

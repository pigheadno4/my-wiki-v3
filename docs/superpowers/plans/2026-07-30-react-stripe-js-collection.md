# React Stripe.js Collection Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable `stripe/react-stripe-js`, collect the latest stable `@stripe/react-stripe-js@6` release into immutable GitHub evidence, and stop with one review packet in `awaiting_approval`.

**Architecture:** Extend only the existing registry row and its focused registry contract test. Reuse the `npm-tracked-source-v1` collector, generated snapshot/release/work-item stores, and existing validators without adding collector logic.

**Tech Stack:** TOML registry, Python 3.9, `unittest`, existing GitHub collection CLI.

## Global Constraints

- Live Git tag discovery identifies `@stripe/react-stripe-js@6.8.0` at SHA `5eae8d509e6cdc6ccd18d43a1173dde28a641002` as the latest stable release; the collector must recheck this during collection.
- Backfill only the latest stable v6 release; retain every future stable v6 release.
- Include `src`, `examples`, normal repository context, and eligible stories.
- Exclude tests and fixtures.
- Do not silently expand source roots or budgets after a policy failure.
- Stop in `awaiting_approval`; do not approve, claim, or ingest the work item.
- Do not edit wiki pages.
- Do not touch unrelated working-tree changes.

---

### Task 1: Make the Registry Row Executable

**Files:**
- Modify: `tests/test_github_registry.py`
- Modify: `tracking/github/repo-registry.toml`

**Interfaces:**
- Consumes: `load_registry(path) -> tuple[RepoConfig, ...]`, `VersionTrack`, and `SourceCapsulePolicy`.
- Produces: one enabled `stripe/react-stripe-js` configuration accepted by `scripts/collect_github_repos.py`.

- [ ] **Step 1: Add the failing registry assertions**

Change the inventory tuple for `stripe/react-stripe-js` from `False` to `True`, then add:

```python
def test_react_stripe_js_uses_the_root_npm_public_source_profile(self):
    repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
    react_stripe_js = next(
        repo for repo in repos if repo.id == "stripe/react-stripe-js"
    )

    self.assertTrue(react_stripe_js.enabled)
    self.assertEqual(
        (
            VersionTrack(
                "package:@stripe/react-stripe-js@6",
                "latest-stable",
                "all-stable",
            ),
        ),
        react_stripe_js.version_tracks,
    )
    self.assertEqual(1, len(react_stripe_js.capsules))
    capsule = react_stripe_js.capsules[0]
    self.assertEqual("react-stripe-js-public-source", capsule.id)
    self.assertEqual("npm-tracked-source-v1", capsule.adapter)
    self.assertEqual(("@stripe/react-stripe-js",), capsule.focus_packages)
    self.assertEqual("internal-runtime-closure", capsule.dependency_scope)
    self.assertEqual("policy-bounded", capsule.changed_path_policy)
    self.assertEqual(("examples", "src"), capsule.default_required_roots)
    self.assertEqual((), capsule.default_generated_target_paths)
    self.assertEqual((), capsule.include_paths)
    self.assertEqual(("fixtures", "tests"), capsule.excluded_categories)
    self.assertEqual("text-secrets-v1", capsule.secret_detector)
    self.assertEqual(512000, capsule.max_file_bytes)
    self.assertEqual(240, capsule.max_capsule_files)
    self.assertEqual(2500000, capsule.max_capsule_utf8_bytes)
    self.assertEqual(280, capsule.max_packet_files)
    self.assertEqual(3000000, capsule.max_packet_utf8_bytes)
```

- [ ] **Step 2: Run the focused test and verify it fails**

Run:

```bash
python3 -m unittest tests.test_github_registry.RegistryTests.test_react_stripe_js_uses_the_root_npm_public_source_profile
```

Expected: failure because the row is disabled and has no version track or capsule.

- [ ] **Step 3: Add the executable registry policy**

Replace the disabled `stripe/react-stripe-js` row with the same stable metadata plus:

```toml
enabled=true

[[repos.version_tracks]]
selector="package:@stripe/react-stripe-js@6"
backfill="latest-stable"
future="all-stable"
include_prerelease=false

[[repos.capsules]]
id="react-stripe-js-public-source"
adapter="npm-tracked-source-v1"
focus_packages=["@stripe/react-stripe-js"]
dependency_scope="internal-runtime-closure"
changed_path_policy="policy-bounded"
default_required_roots=["src", "examples"]
default_generated_target_paths=[]
include_paths=[]
excluded_categories=["tests", "fixtures"]
secret_detector="text-secrets-v1"
max_file_bytes=512000
max_capsule_files=240
max_capsule_utf8_bytes=2500000
max_packet_files=280
max_packet_utf8_bytes=3000000
```

- [ ] **Step 4: Run registry and offline collection validation**

Run:

```bash
python3 -m unittest tests.test_github_registry
python3 scripts/validate_github_collection.py
git diff --check
```

Expected: all registry tests pass, GitHub validation reports no structural errors, and the diff check prints nothing.

- [ ] **Step 5: Commit the executable policy**

```bash
git add tracking/github/repo-registry.toml tests/test_github_registry.py
git commit -m "config: enable React Stripe JS collection"
```

### Task 2: Collect and Review the Stable Baseline

**Files:**
- Create: `raw/github/stripe/react-stripe-js/snapshots/2026-07-30-*/`
- Create: `raw/github/stripe/react-stripe-js/releases/react-stripe-js/6.8.0/2026-07-30/`
- Create: `tracking/github/repos/stripe/react-stripe-js/ingest-packets/github-*/`
- Modify: `tracking/github/work-items.json`
- Modify: `tracking/github/status.md`

**Interfaces:**
- Consumes: the enabled registry row from Task 1 and upstream Git tags/releases.
- Produces: one immutable snapshot, one package-qualified release record, and one canonical review packet linked to an `awaiting_approval` work item.

- [ ] **Step 1: Run backfill collection**

Run:

```bash
python3 scripts/collect_github_repos.py collect --repo stripe/react-stripe-js --mode backfill
```

Expected: collection confirms v6.8.0 or discovers a newer stable v6 release, publishes validated immutable evidence, creates one work item, and leaves it in `awaiting_approval`. If upstream advances within major v6, use the newer discovered stable version without changing the selector.

- [ ] **Step 2: Inspect the generated packet and lifecycle state**

Run:

```bash
python3 scripts/collect_github_repos.py status
```

Read in full:

```text
tracking/github/repos/stripe/react-stripe-js/ingest-packets/github-*/packet.json
tracking/github/repos/stripe/react-stripe-js/ingest-packets/github-*/packet.md
raw/github/stripe/react-stripe-js/snapshots/2026-07-30-*/manifest.json
raw/github/stripe/react-stripe-js/releases/react-stripe-js/*/2026-07-30/manifest.json
raw/github/stripe/react-stripe-js/releases/react-stripe-js/*/2026-07-30/release-notes.md
```

Confirm:

- state is `awaiting_approval`;
- identity is package-qualified;
- snapshot and release SHAs agree;
- evidence gaps and unclassified paths are zero, or are reported without approving;
- stories are eligible and tests/fixtures are excluded;
- required-reading count and recommendation are bounded; and
- no wiki file changed.

- [ ] **Step 3: Run final deterministic validation**

Run:

```bash
python3 scripts/validate_github_collection.py
git diff --check
git status --short
```

Expected: GitHub validation reports no structural errors. Status contains only the collected React Stripe.js evidence, Task 1 files if not already committed, the plan file, and pre-existing unrelated changes.

- [ ] **Step 4: Commit the collection queue**

Stage only generated paths belonging to `stripe/react-stripe-js` plus generated work-item/status files:

```bash
git add raw/github/stripe/react-stripe-js tracking/github/repos/stripe/react-stripe-js tracking/github/work-items.json tracking/github/status.md
git commit -m "collect: add React Stripe JS stable baseline"
```

- [ ] **Step 5: Stop and report the review gate**

Report the discovered package version, SHA, file count, evidence gaps, unclassified paths, required-reading count, recommended mode, review priority, commit, and packet path.

Do not run:

```text
approve
next-ingest
complete-ingest
```

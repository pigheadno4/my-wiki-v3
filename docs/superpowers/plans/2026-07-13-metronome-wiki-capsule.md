# Metronome Wiki Capsule Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the non-ingested Metronome wiki capsule and deterministic validation needed before the first ingest pilot.

**Architecture:** Keep query-facing navigation in `wiki/` and operational collection evidence in `tracking/collections/metronome/`. Extend the general validator only for path-qualified nested raw links, and place provider-specific reconciliation in a focused Metronome capsule validator that derives source coverage, company counts, index membership, raw-version parity, and the nested orphan queue from files rather than manually maintained totals.

**Tech Stack:** Python 3.9 standard library, `unittest`, Markdown/YAML frontmatter conventions, Obsidian wikilinks, Git worktrees.

## Global Constraints

- Do not ingest or summarize any Metronome raw documentation page in this plan.
- Treat `raw/metronome/` as immutable; never normalize or edit collected vendor content.
- Keep one future source page per canonical URL under `wiki/sources/metronome/`.
- Keep provider-specific concepts under `wiki/concepts/metronome/` with globally unique `metronome-` filename prefixes.
- `wiki/metronome-index.md`, `wiki/metronome-log.md`, `wiki/companies/metronome.md`, root indexes, and calculated counts remain coordinator-owned shared files.
- Do not list raw pages as ingested sources; the initial source count is zero and the 225 Markdown documents remain an orphan ingest queue.
- Preserve the unrelated untracked `CLAUDE copy.md` file.
- Use Python 3.9-compatible syntax and standard-library dependencies only.

---

### Task 1: Support Path-Qualified Nested Raw Links

**Files:**
- Modify: `scripts/validate_wiki.py`
- Create: `tests/test_validate_wiki.py`

**Interfaces:**
- Consumes: existing `build_link_index()` and `check_file()` behavior.
- Produces: `build_link_index()` entries for both raw basenames and repository-relative extensionless raw paths such as `raw/metronome/guides/get-started/home-2026-07-13`.

- [x] **Step 1: Write failing nested-link tests**

Add tests that patch `RAW` and `WIKI` to temporary directories, create a nested raw file, and assert the link index contains both `home-2026-07-13` and `raw/metronome/guides/home-2026-07-13`. Add a source-page check using `[[raw/metronome/guides/home-2026-07-13|snapshot]]` and assert no unresolved-link error.

- [x] **Step 2: Run the focused test and confirm failure**

Run: `python3 -m unittest tests.test_validate_wiki -v`

Expected: FAIL because `build_link_index()` currently scans only top-level raw Markdown files and directories.

- [x] **Step 3: Implement recursive raw-link indexing**

Change `build_link_index()` to recurse through `RAW.rglob("*.md")`. For every raw Markdown file, add its basename stem and its extensionless path relative to `ROOT`, using POSIX separators. Preserve existing wiki basename behavior and top-level raw-directory targets.

- [x] **Step 4: Run focused and full tests**

Run:

```bash
python3 -m unittest tests.test_validate_wiki -v
python3 -m unittest discover -s tests -v
```

Expected: all tests pass.

- [x] **Step 5: Commit**

```bash
git add scripts/validate_wiki.py tests/test_validate_wiki.py
git commit -m "feat: validate nested raw wikilinks"
```

---

### Task 2: Add Deterministic Metronome Capsule Validation

**Files:**
- Create: `scripts/metronome_capsule.py`
- Create: `scripts/validate_metronome_capsule.py`
- Create: `tests/test_metronome_capsule.py`

**Interfaces:**
- Consumes: `split_frontmatter()` and `parse_frontmatter()` from `scripts/validate_wiki.py`, collected Markdown under `raw/metronome/`, source summaries under `wiki/sources/metronome/`, `wiki/metronome-index.md`, `wiki/metronome-log.md`, and `wiki/companies/metronome.md`.
- Produces: `CapsuleReport`, `inspect_capsule(root: Path) -> CapsuleReport`, `validate_capsule(report: CapsuleReport) -> list[str]`, and a CLI that prints reconciled counts plus orphan paths and exits nonzero only for structural errors.

- [x] **Step 1: Write failing reconciliation tests**

Create temporary capsule fixtures covering:

- one collected raw Markdown page with no source page, reported as one orphan without being a structural error;
- one valid source page whose `canonical_url`, `raw_files`, and `## Raw Sources` entry agree;
- duplicate source pages for the same canonical URL;
- mismatched `raw_files` and `## Raw Sources` ordering;
- a source omitted from `metronome-index.md`;
- a company `source_count` that differs from the number of Metronome source pages;
- a source path listed in the index that does not exist.

- [x] **Step 2: Run the focused test and confirm failure**

Run: `python3 -m unittest tests.test_metronome_capsule -v`

Expected: FAIL because the capsule inspection module does not exist.

- [x] **Step 3: Implement capsule inspection**

In `scripts/metronome_capsule.py`:

- model the report with Python 3.9-compatible `dataclasses`;
- exclude `_discovery/` and `_artifacts/` from raw-document counts;
- read all future `wiki/sources/metronome/*.md` pages deterministically;
- parse path-qualified `## Raw Sources` wikilinks;
- derive canonical URL ownership, source paths, index source links, company `source_count`, and orphan raw files;
- compare raw versions as exact ordered lists;
- require Metronome source `raw_files` entries to remain inside `metronome/`;
- treat the orphan queue as reportable pending work, not a validation failure.

In `scripts/validate_metronome_capsule.py`, print:

```text
Metronome capsule: <raw> raw, <sources> sources, <orphans> pending ingest
```

Then print structural errors, or print every orphan path under a `Pending ingest:` heading. Return `1` for structural errors and `0` when the capsule is structurally sound even if pending raw files remain.

- [x] **Step 4: Run focused and full tests**

Run:

```bash
python3 -m unittest tests.test_metronome_capsule -v
python3 -m unittest discover -s tests -v
```

Expected: all tests pass.

- [x] **Step 5: Commit**

```bash
git add scripts/metronome_capsule.py scripts/validate_metronome_capsule.py tests/test_metronome_capsule.py
git commit -m "feat: validate metronome capsule state"
```

---

### Task 3: Create the Empty Query Capsule and Navigation

**Files:**
- Create: `wiki/metronome-index.md`
- Create: `wiki/metronome-log.md`
- Create: `wiki/companies/metronome.md`
- Create: `wiki/sources/metronome/.gitkeep`
- Create: `wiki/concepts/metronome/.gitkeep`
- Modify: `wiki/index.md`
- Modify: `wiki/stripe-index.md`
- Modify: `scripts/validate_wiki.py`

**Interfaces:**
- Consumes: the completed collection status and run manifest.
- Produces: provider routing pages that clearly distinguish `225 collected` from `0 ingested`, plus empty tracked source/concept ownership roots.

- [x] **Step 1: Add the `log` page schema**

Add `"log": ["title", "type", "tags"]` to `REQUIRED` in `scripts/validate_wiki.py` so provider logs are validated rather than silently excluded.

- [x] **Step 2: Create the Metronome index**

Create `wiki/metronome-index.md` as the canonical provider router with:

- company link;
- explicit coverage table showing 225 collected documentation pages, 0 ingested source summaries, and 225 pending ingest;
- no source-page links while the source folder is empty;
- planned concept taxonomy shown as code filenames, not unresolved wikilinks;
- relationship links to `[[stripe]]`, `[[stripe-index]]`, and `[[metronome-log]]`;
- Markdown links to collection status and the latest collection manifest.

- [x] **Step 3: Create the company and provider log pages**

Create `wiki/companies/metronome.md` with valid company frontmatter and `source_count: 0`. Keep the body limited to capsule status, relationship routing, and the explicit statement that provider capabilities will be populated from source summaries during ingest.

Create `wiki/metronome-log.md` with valid log frontmatter and a newest-first `2026-07-13` collection entry recording 225 pages, 2 OpenAPI artifacts, 222 new items, 5 unchanged items, 17 sitemap-only pages, and zero failures. Link to operational evidence with ordinary relative Markdown links.

- [x] **Step 4: Create provider ownership roots and navigation links**

Track empty `wiki/sources/metronome/` and `wiki/concepts/metronome/` using `.gitkeep`. Add Metronome to `wiki/index.md` under PSP indexes and Companies. Add a concise `## Related platforms` section near the top of `wiki/stripe-index.md` linking only to `[[metronome-index]]` and `[[metronome]]`, without duplicating source or concept catalogs.

- [x] **Step 5: Validate the new capsule**

Run:

```bash
python3 scripts/validate_wiki.py wiki/companies/metronome.md wiki/metronome-log.md
python3 scripts/validate_metronome_capsule.py
python3 -m unittest discover -s tests -v
```

Expected: focused wiki validation passes; capsule validation reports 225 raw, 0 sources, 225 pending ingest and exits zero; all tests pass.

- [x] **Step 6: Commit**

```bash
git add scripts/validate_wiki.py wiki/index.md wiki/stripe-index.md wiki/metronome-index.md wiki/metronome-log.md wiki/companies/metronome.md wiki/sources/metronome/.gitkeep wiki/concepts/metronome/.gitkeep
git commit -m "docs: create metronome wiki capsule"
```

---

### Task 4: Document and Verify the Pilot Boundary

**Files:**
- Modify: `rules/lint.md`
- Modify: `rules/psp/metronome.md`

**Interfaces:**
- Consumes: `scripts/validate_metronome_capsule.py`.
- Produces: operator instructions that make nested Metronome orphan reporting reproducible without changing the serial ingest rule.

- [x] **Step 1: Document provider-aware orphan validation**

In `rules/lint.md`, preserve the existing top-level legacy orphan procedure and add a nested-provider subsection directing operators to run `python3 scripts/validate_metronome_capsule.py` for Metronome. State that pending orphans are expected before ingest and structural mismatches are errors.

- [x] **Step 2: Add the capsule validation command to the provider profile**

In `rules/psp/metronome.md`, add a post-collection/pre-ingest command block for `python3 scripts/validate_metronome_capsule.py` and state that collection never updates source pages or starts ingest.

- [x] **Step 3: Run final verification**

Run:

```bash
python3 -m unittest discover -s tests -v
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m py_compile scripts/*.py
python3 scripts/validate_wiki.py wiki/companies/metronome.md wiki/metronome-log.md
python3 scripts/validate_metronome_capsule.py
git diff --check
```

Also run `python3 scripts/validate_wiki.py` across the existing wiki and confirm that any nonzero result contains only the 17 previously recorded unrelated issues.

- [x] **Step 4: Commit**

```bash
git add rules/lint.md rules/psp/metronome.md
git commit -m "docs: add metronome capsule validation workflow"
```

- [x] **Step 5: Report and stop before ingest**

Report capsule paths, deterministic counts, test results, the unchanged pre-existing validator issue count, and commit IDs. Do not benchmark models or ingest a source until the user explicitly requests the ingest pilot.

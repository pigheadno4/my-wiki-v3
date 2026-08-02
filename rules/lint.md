# Rule: Lint the wiki

> This rule governs wiki health checks. You arrived here from the CLAUDE.md Workflow Index.

> **MANDATORY**: Use `TodoWrite` to create one todo item per step below before starting any lint work. Mark each item completed as you finish it — never batch completions.

## 0. Run the deterministic validator first

Run `python scripts/validate_wiki.py` across the wiki. It checks, **outside the LLM**: every page has its required frontmatter fields, every `raw_files:` entry points to a file that exists in `raw/`, every `[[wikilink]]` resolves to a real page, no `[TODO]`/placeholder text remains, and slugs are well-formed. Triage its output before the judgment-based steps below. This is the cheap, model-independent backbone of lint.

## 1. Scan all wiki pages for

- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages (no inbound links)
- Concepts mentioned but lacking their own page
- Concept pages that exist but are outdated relative to newer source pages
- Missing cross-references
- Data gaps that could be filled with a web search
- **Index drift** — pages not listed in the correct index (see the split rule below)

## 2. Verify against raw files

Raw files are NEVER modified — they are immutable source documents.

### a. Raw files without source summaries (informational inventory)

Find raw files with no reference in any wiki source page. This is the primary mechanism for seeing files added directly to `raw/` — **including everything the PSP fetcher drops in** (see `psp-collection.md`). A raw page without a source summary is informational: it may be an intentional `raw_reference`, an unresolved `semantic_triage` page, or a future source candidate. It is not a backlog that must reach zero.

- How: list all **top-level files** in `raw/` (i.e., `raw/*.md` — not files inside subdirectories or `raw/assets/`). For each, search `wiki/sources/` for its filename in `raw_files:` frontmatter. If not found anywhere, record it as an informational inventory entry. This covers dated raw files and legacy flat GitHub stubs.
- Also check legacy detail subdirectories in `raw/` that lack their corresponding legacy stub file (e.g., `raw/github-stripe-node/` exists but `raw/github-stripe-node.md` does not). New nested GitHub snapshots under `raw/github/` are validated separately below.
- Triage: present raw files without source summaries as a numbered list. For each page that needs a routing decision, propose one of the common dispositions:
  - **`raw_reference`**: retain as navigation-only raw with no routine source generation.
  - **`semantic_triage`**: queue one complete strong-model read to decide its disposition after approval.
  - **`source_required`**: queue full source generation plus independent review after approval.
- Action: user approves each routing decision or promotion. Only for approved `source_required` pages, choose during execution whether to attach the raw evidence to an existing related source page or create a new source page. Run the full ingest workflow **one source at a time** per `ingest.md`.
- Example: `raw/stripe-connect-overview-2026-06-02.md` has no source summary → record it as an informational inventory entry, propose a disposition, and decide between linking and creating only if `source_required` is approved.

#### Nested provider capsules

The legacy scan above covers top-level raw files. Provider capsules with path-preserving nested raw trees require their provider-aware deterministic checker.

For Metronome, run:

```bash
python3 scripts/validate_metronome_capsule.py
```

The command recursively reconciles `raw/metronome/` against `wiki/sources/metronome/`. Raw paths without source summaries are informational and do not make the command fail; they may be intentional `raw_reference` pages, unresolved `semantic_triage` pages, or future source candidates, and their count need not reach zero. Duplicate canonical URLs, missing raw versions, disagreement between `raw_files:` and `## Raw Sources`, index drift, or an incorrect company `source_count` remain structural errors and return a nonzero exit code.

#### Nested GitHub repository snapshots

For GitHub repository evidence and generated tracking state, run:

```bash
python3 scripts/validate_github_collection.py
```

The command validates immutable exact-SHA snapshots and package release records under `raw/github/`, the human-maintained `tracking/github/repo-registry.toml`, generated comparisons and work items, status equality, and cumulative source/changelog evidence for ingested items. Work items awaiting approval are the expected GitHub ingest queue; structural contract errors return a nonzero exit code.

### b. Accuracy spot-checks

For key source pages, compare summaries against their raw files to verify correctness.

- How: read the `raw_files:` frontmatter on the source page → read the corresponding raw files → compare key claims, numbers, and details in the summary against the full original content.
- Flag: claims in wiki that don't match the raw content, important details the summary omitted, or outdated information corrected in a newer (dated) raw file.
- Action: update the source page summary to match the raw content. Never modify the raw file.
- Note: focus on key/high-traffic source pages or pages flagged with contradictions — not every raw file every pass.

### c. Concept page staleness and gap check

- **Staleness**: for each concept page, check whether its `## Sources` links still match reality, and whether key facts (limits, timelines, API endpoints, field names) differ from the raw file content that backs those sources. Concept pages summarize and can drift.
- **Gaps**: grep `wiki/sources/` for source pages whose tags match an existing concept page's tags. If newer source pages exist on the topic that the concept page doesn't reference, update the concept page.
- **Missing concept pages**: count source pages per topic area. If 3+ source pages cover a topic with no concept page, flag it as a concept page gap.
- Action: update stale or incomplete concept pages; create missing ones using the `ingest.md` decision table. Never modify raw files.

### d. Missing `raw_files:` frontmatter

- How: scan all source pages in `wiki/sources/`. If a source page has no `raw_files:` field, find the corresponding raw file(s) by matching filenames or source URLs.
- Action: add `raw_files:` to the frontmatter with the correct raw filename(s), newest dated version first.

## 3. Report findings

Report all findings to the user as a numbered list — validator failures, orphan raw files, stale concepts, gaps, missing frontmatter, contradictions, index drift.

## 4. Fix with approval

Fix issues with user approval. For each fix, run the full ingest workflow **one source at a time** (source page → concept audit → company/concept updates → index → log). Re-run `validate_wiki.py` after fixes.

## 5. Log

Log the lint pass in `wiki/log.md`.

---

## Index split rule (reference)

The index is layered. Keep entries in the right place:

- **`wiki/index.md` (root)** — the PSP catalog (links to each `wiki/<psp>-index.md`) **plus** cross-cutting pages: comparisons (`stripe-vs-paypal-*`), analyses, **generic** concepts (`disputes`, `3d-secure`), and the overview. Each cross-cutting entry lives here **once** (single source of truth).
- **`wiki/<psp>-index.md`** — that PSP's source pages, its company page, and platform-prefixed concepts (`stripe-radar`, `paypal-vault`). Comparisons involving the PSP are **cross-linked** here, not re-listed in full.

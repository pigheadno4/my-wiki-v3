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

### a. Orphan raw files (ingest queue)

Find raw files with no reference in any wiki source page. This is the primary mechanism for catching files added directly to `raw/` — **including everything the PSP fetcher drops in** (see `psp-collection.md`).

- How: list all **top-level files** in `raw/` (i.e., `raw/*.md` — not files inside subdirectories or `raw/assets/`). For each, search `wiki/sources/` for its filename in `raw_files:` frontmatter. If not found anywhere, it's an orphan. This works uniformly for all source types and for dated filenames — GitHub repo stub files are detected the same way.
- Also check for orphan **subdirectories** in `raw/` that lack a corresponding stub file (e.g., `raw/github-stripe-node/` exists but `raw/github-stripe-node.md` does not) — these need the stub file created first, then linked via ingest.
- Triage: present all orphan raw files as a numbered list. For each, propose one of:
  - **Link**: attach to an existing related source page (prepend to `raw_files:` newest-first + add content to the page body).
  - **New**: create a new source page via the ingest workflow.
- Action: user approves per-file, then execute. Run the full ingest workflow **one source at a time** per `ingest.md` for each new source.
- Example: `raw/stripe-connect-overview-2026-06-02.md` has no reference → propose creating a new source page, or linking to existing `source-stripe-platform-guide.md` if it covers the same topic.

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

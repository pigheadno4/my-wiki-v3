# Wiki Rules Restructure + PSP Collection Subsystem — Design

- **Date:** 2026-06-02
- **Status:** Approved (brainstorming complete)
- **Author:** brainstormed with Claude
- **Supersedes scope of:** the monolithic `CLAUDE.md` / `AGENTS.md`

## Problem

The payments-wiki instruction files have three problems:

1. **`CLAUDE.md` (430 lines) and `AGENTS.md` (400 lines) are near-duplicates that have drifted ~78 lines apart.** `CLAUDE.md` has the concept-audit-first rule, decision tables, and naming conventions; `AGENTS.md` lacks them. An agent reading `AGENTS.md` follows weaker, older rules.
2. **The files are too long to maintain**, mixing always-needed reference (schema) with on-demand workflow detail.
3. **No raw-collection automation.** Stripe/PayPal/Adyen expose `llms.txt`/`.md` page variants (Adyen also `llms-full.txt`), but collection is fully manual today. The wiki has 1,076 raw files, 803 source pages, 140 concepts — ingest is the dominant activity.

## Goals

- Kill the CLAUDE/AGENTS duplication structurally (drift becomes impossible).
- Slim the root to always-needed reference; move workflows to on-demand sub-rules.
- Add a per-PSP, config-driven raw-collection subsystem (extensible to Airwallex/Braintree/…).
- Harden ingest: **never batch, one source at a time, read the full raw file first.**
- Make ingest/lint quality robust across cheaper LLMs (DeepSeek/GLM) via templates, grounding gates, a deterministic validator, and model routing.
- Split the 164 KB `index.md` into a layered root + per-PSP indexes.

## Decisions (locked during brainstorming)

| # | Decision | Choice |
|---|----------|--------|
| Topology | How CLAUDE.md / AGENTS.md relate | **One root + pointer**: `CLAUDE.md` is the slim root; `AGENTS.md` is a 2-line pointer to it + `rules/`. |
| Collection | How PSP raw collection runs | **Shared `fetch_psp.py` + per-PSP config**, invoked per-PSP. Config encodes per-PSP differences incl. `url_fixups`. |
| Decomposition | Root vs sub-rules split | **Schema stays in root** (Approach A). Workflows move to `rules/`. |
| Granularity | Number of sub-rules | **8 rule files**; `github-repos.md` is its own file. |
| Dating scope | Which raw files get dated names + diff | **All raw files going forward** get `-YYYY-MM-DD`. Existing 1,076 files are the undated baseline. |
| Retention | On re-collect change | **Keep all versions** (immutable history); `raw_files:` lists newest-first. |
| Index split | Where cross-cutting pages go | **Cross-cutting in root only**; per-PSP indexes hold that PSP's sources/company/platform-concepts and cross-link comparisons. |
| Quality | Cross-LLM guardrail | **`validate_wiki.py` + task→model routing table.** |

## Artifact map

```
CLAUDE.md                  # slim root: identity, dir map, PAGE SCHEMA, conventions,
                           #   domain guidance, gated Workflow Index
AGENTS.md                  # 2-line pointer → CLAUDE.md + rules/
rules/
  raw-collection.md        # manual raw creation (paste/URL/image/mixed), dated-naming
                           #   convention, immutability, large-content handling
  psp-collection.md        # AUTO flow: fetcher usage, run-list, staging+diff+dedup,
                           #   date-versioning, "onboard a new PSP" checklist,
                           #   two-pipelines overview, collection→ingest boundary
  psp/
    stripe.md              # docs.stripe.com · llms.txt · append .md · no full corpus
    paypal.md              # docs.paypal.ai · llms.txt · append .md · developer.paypal.com caveat
    adyen.md               # docs.adyen.com · llms.txt + llms-full.txt · append .md
  github-repos.md          # repo workflow (stub/detail/deep-dive) + special manual
                           #   ingest of PSP SDK/sample/tool repos
  ingest.md                # NO-BATCH gate, read-full-raw-first, concept-audit-first,
                           #   decision tables, TEMPLATES, grounding gate, worked
                           #   example, task→model routing table, page order, index+log
  lint.md                  # lint workflow + orphan queue + runs validate_wiki.py
  query-and-synthesis.md   # answer query → comparison/analysis filing
scripts/
  fetch_psp.py             # shared fetcher (staging, diff, dating, manifest)
  psp_config.toml          # PSP registry — extensible (add Airwallex/Braintree = 1 row)
  validate_wiki.py         # deterministic guardrail (frontmatter/links/placeholders)
wiki/
  index.md                 # root catalog: PSP list + comparisons + analyses + generic
                           #   concepts + overview
  <psp>-index.md           # per-PSP: sources + company + platform concepts (migration
                           #   of today's 164 KB index.md)
```

## Migration coverage (no rule is lost — only moved)

| Current `CLAUDE.md` section | New home |
|------------------------------|----------|
| Title / intro | `CLAUDE.md` root |
| Directory structure | `CLAUDE.md` root (updated: `rules/`, `scripts/`, layered index) |
| Page types (all frontmatter schema) | `CLAUDE.md` root |
| Conventions | `CLAUDE.md` root |
| Domain-specific guidance | `CLAUDE.md` root |
| Workflows (prose) | `CLAUDE.md` root → **gated Workflow Index** (routing table only) |
| Ingest a source — Phase 1 (verbatim check) | `rules/raw-collection.md` (manual flow) |
| Ingest a source — Phase 2 | `rules/ingest.md` |
| Handle large source content | `rules/raw-collection.md` |
| Ingest content with images | `rules/raw-collection.md` (saving) + `rules/ingest.md` (pages) |
| Ingest a GitHub repository | `rules/github-repos.md` |
| Raw file rules + tiered strategy | `rules/raw-collection.md` |
| Answer a query | `rules/query-and-synthesis.md` |
| Lint the wiki | `rules/lint.md` |

Verification: after the split, every heading from the pre-refactor `CLAUDE.md` (preserved in git at commit `32ee4dd`) maps to a row above, and `validate_wiki.py` plus a manual diff confirm coverage.

## Gated Workflow Index (the pointer mechanism)

Root `CLAUDE.md` replaces workflow prose with a routing table prefaced by a hard gate:

> **Workflows — you MUST read the full rule before acting.** The table is for routing only. Before performing a workflow, `Read` the linked rule file and follow it exactly. Do not act from this summary.

Each sub-rule opens with: *"This rule governs X; you arrived from the CLAUDE.md workflow index."* The existing MANDATORY `TodoWrite` gates (concept-audit-first; one-todo-per-lint-step) move into their sub-rules unchanged.

## PSP collection subsystem

### Two pipelines (explicit)

- **Manual flow** (unchanged): collect one raw page → verbatim verify → share key findings → wait for user approval → ingest. Human-in-the-loop, for one-off pastes/URLs/images.
- **Auto flow** (new): `fetch_psp.py` batch-collects across PSP sections → staging + diff + dedup → when **all scripts for the round finish**, writes a **round manifest** (new + changed files w/ diffs) and **pings the user to kick off ingest**. User then ingests the manifest **one at a time** per `ingest.md`.

Collection is batch (fast); ingest is strictly serial. Both converge on `rules/ingest.md`.

### `fetch_psp.py` behaviour

1. Read the PSP's discovery file (`llms.txt`, or `llms-full.txt` where available) per config.
2. Apply `url_fixups` (e.g., collapse duplicated path segments `/api-explorer/api-explorer/` → `/api-explorer/`). Log every fixup.
3. For each target page: fetch the `.md` variant, slugify URL → `raw/<psp>-<slug>-YYYY-MM-DD.md`, prepend `<!-- Source URL --> / <!-- Fetched: -->` header.
4. Write to a **staging area** first; diff against the most recent prior version of the same slug (dated *or* the undated baseline), ignoring the header line:
   - **identical** → discard staged copy (nothing to ingest);
   - **changed** → promote to `raw/`, add to round manifest with stored diff;
   - **brand-new** → promote, mark "new".
5. **Idempotent / immutable:** never overwrites an accepted raw file; only a *staged* file is ever discarded. Re-runs are safe.

### `psp_config.toml` schema (registry — extensible)

Per PSP row: `host`, `discovery_file` (`llms.txt`/`llms-full.txt`), `md_rule` (append `.md`), `has_full_corpus` (bool), `url_fixups` (list of pattern→replacement), notes. Adding Airwallex/Braintree = one new row + one `rules/psp/<psp>.md`. `psp-collection.md` carries the **"onboard a new PSP"** checklist.

### Per-PSP facts (verified 2026-06-02)

| PSP | Discovery | Host | `.md` | Full corpus |
|-----|-----------|------|-------|-------------|
| Stripe | `docs.stripe.com/llms.txt` (~400 links) | `docs.stripe.com` | append `.md` | none |
| PayPal | `docs.paypal.ai/llms.txt` | `docs.paypal.ai` (NOT `developer.paypal.com` — cert error) | append `.md` | none |
| Adyen | `docs.adyen.com/llms.txt` | `docs.adyen.com` | append `.md` | `llms-full.txt` |

## Cross-LLM ingest/lint quality

To keep quality high on cheaper models (DeepSeek/GLM):

1. **Templates over prose** — `ingest.md` ships copy-paste frontmatter templates + a body skeleton with labeled blanks.
2. **Grounding gate** — before summarizing, extract N verbatim quotes (with location) from the full raw file.
3. **Judgment → checklists** — every fork (e.g., "concept page warranted?") becomes explicit yes/no criteria + a worked example.
4. **One worked example per rule** — raw-excerpt → finished-page.
5. **`validate_wiki.py` (highest-leverage, model-independent)** — checks frontmatter completeness, `raw_files:` exist, wikilinks resolve, no placeholders, slug format. Run after ingest and during lint.
6. **Task→model routing table** (in `ingest.md`, referenced by `lint.md`): bulk source summaries (templated) → cheap model; concept synthesis / contradiction detection / comparison / analysis / lint triage (cross-page judgment) → strong model.

## Layered index

- `wiki/index.md` (root): PSP catalog (→ each `<psp>-index.md`) + cross-cutting (comparisons, analyses, generic concepts, overview). Single source of truth per cross-cutting entry.
- `wiki/<psp>-index.md`: that PSP's source pages + company page + platform-prefixed concepts (`stripe-radar`, …) + a "Comparisons involving <PSP>" cross-link section.
- One-time migration of today's 164 KB `index.md`.

## Ingest hardening (top of `rules/ingest.md`)

> 🛑 **ONE SOURCE AT A TIME — NEVER BATCH.** Ingest exactly one raw file per cycle. Before writing any wiki page you MUST `Read` the **full** raw file end-to-end — never from a partial read, a summary, or several raw files in parallel. Complete one source's full cycle (concept audit → source → company → concept → comparison → index → log) and mark its todos done **before** starting the next.

## Implementation sequence

1. **Restructure** `CLAUDE.md` (slim root + gated index) + `AGENTS.md` (pointer) + the 8 `rules/` files. Verify via the coverage table.
2. **Split** `wiki/index.md` into the layered scheme (root + per-PSP).
3. **Build + test** `fetch_psp.py` + `psp_config.toml` against one real Stripe `llms.txt` section.
4. **Build** `validate_wiki.py` and run it across the existing wiki.
5. **Write** the three PSP sub-rules (`stripe.md`, `paypal.md`, `adyen.md`).

## Out of scope

- Bulk re-collection of the existing 1,076 raw files (they remain the undated baseline; they migrate to dated naming naturally on next re-collect).
- Adding Airwallex/Braintree content (the registry supports them; ingest is a later task).
- Any change to the immutability of accepted raw files.

## Risks / mitigations

- **Lost rule during the move** → coverage table + git baseline at `32ee4dd` + `validate_wiki.py`.
- **Agent ignores a gated pointer** → strong MANDATORY language + `validate_wiki.py` as the deterministic backstop.
- **Push auth to v3** (no `gh`, different account) → handled at baseline; if it fails the user authenticates and re-pushes.

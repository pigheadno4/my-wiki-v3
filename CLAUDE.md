# Payment Industry Wiki — Schema

You are maintaining a personal knowledge base about the **Payment Industry** — how it evolves and shapes commerce. The wiki covers payment networks, fintech companies, regulations, standards, and emerging trends.

## Directory structure

```text
my-wiki-v2/
├── CLAUDE.md          # this file — schema and conventions
├── raw/               # immutable source documents (verbatim original content, never modify or summarize)
│   ├── assets/        # downloaded images referenced by sources
│   ├── <repo-slug>.md # GitHub repo stub file — lint anchor + metadata
│   └── <repo-slug>/   # GitHub repo key excerpts
├── wiki/              # LLM-generated pages (you own this layer)
│   ├── index.md       # catalog of all wiki pages
│   ├── log.md         # chronological operation log
│   ├── overview.md    # high-level payments industry overview
│   ├── companies/     # one page per company
│   ├── concepts/      # industry concepts, regulations, trends
│   ├── comparisons/   # side-by-side company comparisons
│   ├── analyses/      # filed query results and syntheses
│   └── sources/       # source summary pages
└── llm-wiki-idea.md   # reference — the pattern this wiki follows
```

## Page types

### Source summaries (`wiki/sources/`)

One page per ingested source. Filename: `source-<slugified-title>.md`

Frontmatter:

```yaml
---
title: "<source title>"
type: source
date_ingested: YYYY-MM-DD
original_format: article | paper | report | transcript | notes | webpage | github-repo | image
raw_files:
  - "<filename in raw/ directory, e.g. stripe-invoicing-overview.md>"
  - "<additional raw file if source aggregates multiple docs>"
tags: [<relevant tags>]
---
```

Body: structured summary with key takeaways, relevant quotes, and links to company/concept pages. Body headings start at `##` — the frontmatter `title:` field serves as the document's H1 in Obsidian.

The `raw_files:` frontmatter field is plain strings used by the lint workflow (grep-friendly). For Obsidian navigation, also include a **Raw Sources** section at the bottom of the body with `[[wikilinks]]` to each raw file:

```markdown
## Raw Sources
- [[paypal-checkout-getting-started]] — verbatim webpage content
- [[paypal-checkout-integrate-server-side-shipping]] — server-side shipping tab variant
```

Obsidian resolves wikilinks by shortest matching filename, so the `.md` extension is omitted and no path prefix is needed.

### Company pages (`wiki/companies/`)

Payment companies and platforms. Filename: `<slugified-name>.md`

Frontmatter:

```yaml
---
title: "<company name>"
type: company
tags: [<relevant tags>]
source_count: <number of source summary pages (wiki/sources/) mentioning this company — one per source page, not per raw file>
---
```

Body: overview, key products, pricing model, API/developer experience, market position, pros, cons, notable clients, timeline of developments. Link to sources, concepts, and comparisons.

### Concept pages (`wiki/concepts/`)

Technologies, frameworks, regulations, trends. Filename: `<slugified-concept>.md`

Frontmatter:

```yaml
---
title: "<concept name>"
type: concept
category: technology | regulation | trend | framework | standard
tags: [<relevant tags>]
---
```

Body: definition, relevance to payments, current state, key players, open questions. Link to companies and sources.

**Naming**: prefix platform-specific concepts with the company slug (e.g., `paypal-vault.md`, `stripe-radar.md`, `adyen-marketpay.md`). Generic industry concepts need no prefix (e.g., `disputes.md`, `recurring-payments.md`, `3d-secure.md`). When in doubt, ask: "does this concept exist independently of one platform?" If yes, no prefix.

### Comparison pages (`wiki/comparisons/`)

Side-by-side company analysis on a **specific dimension**. Each comparison page covers one focused topic — not everything about a company pair.

Filename: `<company-vs-company>-<dimension>.md` (e.g., `stripe-vs-paypal-subscriptions.md`, `stripe-vs-paypal-apple-pay.md`, `stripe-vs-adyen-pricing.md`)

Frontmatter:

```yaml
---
title: "<Company A> vs <Company B>: <Dimension>"
type: comparison
dimension: "<dimension being compared, e.g. subscriptions, apple-pay, bnpl, pricing>"
date_created: YYYY-MM-DD
tags: [<relevant tags>]
---
```

Body: side-by-side analysis on the specific dimension. Use markdown tables where appropriate. All claims sourced with links to source summary pages. Link to relevant concept pages (e.g., `[[subscriptions]]`, `[[apple-pay]]`) and company pages.

Multiple comparisons between the same pair are expected — each gets its own page. The index groups them by company pair for easy browsing.

### Analysis pages (`wiki/analyses/`)

Cross-cutting syntheses, reference tables, filed query results. Filename: `analysis-<slugified-title>.md`

Frontmatter:

```yaml
---
title: "<analysis title>"
type: analysis
date_created: YYYY-MM-DD
tags: [<relevant tags>]
---
```

## Conventions

- **Links**: use Obsidian-style `[[wikilinks]]` for cross-references between wiki pages.
- **Tags**: use lowercase, hyphenated tags (e.g. `fraud-detection`, `real-time-payments`, `payment-gateway`).
- **Slugs**: lowercase, hyphenated filenames (e.g. `stripe.md`, `pci-dss.md`, `interchange-fees.md`).
- **Citations**: when referencing a source, link to the source summary page — e.g. `[[source-visa-annual-report-2025]]`.
- **Contradictions**: when new information contradicts existing wiki content, note it explicitly with a `> [!warning] Contradiction` callout and update both pages.
- **Confidence**: for claims that are uncertain or evolving, use `> [!info] Evolving` callouts.

## Workflows

### Ingest a source

**Phase 1 — Raw file + verbatim check (requires user approval before Phase 2):**

1. **If the source content is markdown** (pasted text/webpage): create an **empty raw file** with just the metadata header, then ask the user to paste the full content directly into the raw file in their editor. Wait for them to confirm the paste is done before proceeding.

   **If the source is a URL to fetch**, a GitHub repo, or images: write the raw file directly with the fetched/downloaded content (download any CDN image URLs to `raw/assets/` automatically).
2. Compare the raw file against the pasted content and report:
   - **Key findings** — the most important takeaways from this source (bullet summary)
   - **Verbatim check** — list any differences between what was pasted and what was written to the raw file. If the content is verbatim, confirm that explicitly. Flag any collapsed whitespace, missing sections, or formatting changes, and note whether they are rendering artifacts (acceptable) or content changes (must fix).
3. **Wait for user approval** before proceeding to Phase 2. Do not create wiki pages until the user confirms the raw file is acceptable.

Common verbatim failure modes to watch for:

- Collapsing a bullet list of countries into a comma-separated sentence
- Removing or simplifying CSS class strings (`data-pp-*`, `.css-...`)
- Stripping link text and keeping only the URL (or vice versa)
- Renaming or relabeling code block headings (e.g. `#### **\`Sample request\`**`)
- Restructuring sections or adding new headings not in the original
- Replacing inline HTML entities (`&lt;`, `&gt;`) with the rendered characters
- Truncating large JSON/curl examples or replacing them with `[...]` placeholders
- Adding markdown formatting (bold, code ticks) that wasn't in the source
- Collapsing many blank lines that are clearly HTML rendering artifacts (acceptable — note but don't fix)

**Phase 2 — Wiki ingest (after user approval):**

> **MANDATORY**: Use `TodoWrite` to create one todo item per step below before starting any work. Mark each item completed as you finish it — never batch completions. The concept audit (step 1) must be completed and marked done before any other step begins.

1. **Concept audit** — scan `wiki/concepts/` for any existing page covering the same topic as the source. This step is MANDATORY and must run FIRST, before creating any source or company pages.
   - If a related concept page exists: update it now with new facts from the source. Do not defer.
   - If no concept page exists for a major new product or topic area: create one now, before moving to step 2.
   - Use the decision table in step 3 to determine whether a new concept page is warranted.
2. Create or update a source summary page in `wiki/sources/`:
   - If creating a **new source page**, include `raw_files:` list in frontmatter with the raw filename.
   - If **adding to an existing source page** (e.g., a second raw file about the same topic), append the new raw filename to the existing `raw_files:` list in frontmatter, and add the new content/source link to the page body.
   - This links summaries back to their full source content for future deep dives and lint verification.
3. Create or update relevant company pages in `wiki/companies/`.
4. Create or update relevant concept pages in `wiki/concepts/`. Use this decision table:

   | Situation | Action |
   | --- | --- |
   | New topic area — first source on this subject | Always create a concept page |
   | New PayPal/Stripe/Adyen product not yet in `wiki/concepts/` | Create a concept page |
   | Supplementary page — 2nd+ source on an already-covered topic | Update the existing concept page instead |
   | Thin content — setup guides, test values, troubleshooting, error code tables | Skip concept page; update existing one only if new concrete facts emerge |

   **Naming reminder**: prefix platform-specific concepts with the company slug (e.g., `paypal-vault.md`). Generic industry concepts need no prefix (e.g., `disputes.md`, `agentic-commerce.md`). Ask: "does this concept exist independently of one platform?" If yes, no prefix. If 3+ source pages exist on a topic with no concept page, that is a gap — create the concept page. **Generic concept pages should link to platform-specific implementations, not duplicate their content** — e.g., `disputes.md` explains the concept and links to `[[source-paypal-disputes-api]]`, it does not re-list all 9 PayPal endpoints.
5. Create or update relevant comparison pages in `wiki/comparisons/` if the source **substantively compares** two or more companies (e.g., pricing differences, feature comparisons, migration guides). A source that merely mentions multiple companies in passing does not warrant a comparison page.
6. Check for contradictions with existing wiki content — flag them.
7. Update `wiki/index.md` with new/updated pages.
8. Append an entry to `wiki/log.md`.

### Handle large source content

When the user shares source content that exceeds the message character limit (truncated at ~50,000 characters):

1. **Create the raw file immediately** with a placeholder or the filename derived from the content title.
2. **Notify the user** to paste the full content directly into the raw file.
3. **Wait for the user** to confirm the paste is complete before reviewing and ingesting.

Do NOT attempt to summarize truncated content — the partial view may miss critical details. Always get the full content first.

### Ingest content with images

When the user pastes or attaches images (screenshots, diagrams, photos) — either standalone or mixed with text:

1. **Save all images** to `raw/assets/` with context-based descriptive filenames (e.g., `stripe-checkout-flow-diagram.png`). If multiple images, name each based on its content.
2. **Create the raw `.md` file** in `raw/`:
   - If mixed content (text + images): write the verbatim text with `![description](assets/filename.png)` references embedded at the positions the images appeared.
   - If images only (no text): create a stub `.md` that lists each image with a brief description of what it shows.
3. **Analyze the images** — describe what each image shows and extract key information (UI flows, architecture diagrams, data tables, error messages, etc.).
4. **Discuss key takeaways** with the user, including observations from both text and images.
5. **Create or update source summary page** in `wiki/sources/`:
   - `original_format: image` (if images only) or the appropriate format for mixed content
   - `raw_files:` listing the raw `.md` file (the images in `raw/assets/` are referenced from within it, not listed separately in frontmatter)
   - Body: summary incorporating information extracted from both text and images. Embed the images in the summary where helpful using the same `raw/assets/` paths.
6. Create or update relevant **company pages** in `wiki/companies/`.
7. Create or update relevant **concept pages** in `wiki/concepts/`.
8. Create or update relevant **comparison pages** in `wiki/comparisons/` if the source **substantively compares** two or more companies.
9. Check for **contradictions** with existing wiki content — flag them.
10. Update `wiki/index.md` with new/updated pages.
11. Append an entry to `wiki/log.md`.

### Ingest a GitHub repository

When the user provides a GitHub repo URL (or the lint process finds an orphan `raw/<repo-slug>.md` stub or `raw/<repo-slug>/` directory):

1. **Clone the repo** to a temp location, checkout the default branch.
2. **Survey the repo** — read README, scan directory structure, identify files relevant to the wiki's focus (payment integration patterns, SDK usage, API schemas, examples).
3. **Propose key files to the user** — present a numbered list of files worth saving (typically 5-20). User can add or remove from the list.
4. **Create the raw stub file** `raw/<repo-slug>.md` (e.g., `raw/github-stripe-node.md`):
   - This is the **lint anchor** — the single file that `raw_files:` points to, keeping orphan detection consistent with all other source types.
   - Contents: repo URL, commit SHA, date reviewed, list of saved key files, and a pointer to the detail subfolder.
5. **Create the raw detail directory** `raw/<repo-slug>/` (e.g., `raw/github-stripe-node/`):
   - Copy approved key files, preserving their relative paths within the repo (e.g., `raw/github-stripe-node/src/resources/PaymentIntents.ts`).
6. **Create source summary page** in `wiki/sources/`:
   - `original_format: github-repo`
   - `raw_files:` listing only the stub file (e.g., `github-stripe-node.md`) — the stub references the detail subfolder internally.
   - Body: what the repo is, key APIs/patterns, integration approach, notable code examples, link to relevant company/concept pages.
7. Create or update relevant **company pages** in `wiki/companies/`.
8. Create or update relevant **concept pages** in `wiki/concepts/`.
9. Create or update relevant **comparison pages** in `wiki/comparisons/` if the source **substantively compares** two or more companies.
10. Check for **contradictions** with existing wiki content — flag them.
11. Update `wiki/index.md` with new/updated pages.
12. Append an entry to `wiki/log.md`.
13. **Clean up** the temp clone.

### Raw file rules

- The `raw/` directory is the **source of truth** — it preserves the original content exactly as received. If you need to summarize, that belongs in `wiki/sources/`, never in `raw/`.
- Raw files are **immutable** — never modify them after creation.
- Summaries and analysis belong in `wiki/sources/`, not in `raw/`.
- Always create the raw file(s) **before** creating or updating source summaries.
- The `raw_files:` frontmatter field lists filenames relative to `raw/` (e.g., `stripe-invoicing-overview.md` means `raw/stripe-invoicing-overview.md`).

#### Tiered raw file strategy by source type

| Source type | Raw file format | Rationale |
| --- | --- | --- |
| Pasted text/markdown | Verbatim `.md` copy | Content exists nowhere else — raw is the only record |
| Website URL | Fetched markdown + metadata header | Web pages change/disappear — snapshot has archival value |
| Images/screenshots | Image files in `raw/assets/` + reference in raw `.md` | Preserves the actual visual artifact |
| GitHub repo | Stub `.md` lint anchor + key excerpts in `raw/<repo-slug>/` | Stub file enables consistent lint; repo has its own version history — save what matters for the wiki's focus |

##### Pasted text/markdown

- **CRITICAL: Raw files must contain the EXACT, VERBATIM, FULL content** the user pasted — copy it word-for-word into the raw file. **DO NOT summarize, condense, paraphrase, reformat, or omit any part of the content.**
- When the user pastes content that fits within the message limit, write the entire pasted content directly to the raw file — not a summary or condensed version.

##### Website URL

- Fetch the page content and save as `.md` in `raw/`.
- Add a metadata header at the top of the raw file:

  ```html
  <!-- Source URL: https://example.com/page -->
  <!-- Fetched: YYYY-MM-DD -->
  ```

- The fetched markdown is an HTML→markdown conversion — not pixel-perfect, but the best reproducible capture.

##### Images and screenshots

- When the user pastes/attaches images, **automatically save each image** to `raw/assets/` with a context-based descriptive filename (e.g., `stripe-checkout-flow-diagram.png`, `paypal-dashboard-settings.png`).
- Multiple images in one message → save all of them, naming each based on its content.
- Reference saved images in the corresponding raw `.md` file:

  ```markdown
  ![Checkout flow diagram](assets/stripe-checkout-flow-diagram.png)
  ![Payment settings panel](assets/paypal-dashboard-settings.png)
  ```

- **Inline attachments vs CDN URLs** — these are two distinct cases:
  - **Inline attachments** (images pasted directly into the chat): can only be perceived visually — cannot be saved as bytes. Note their presence in the raw file but do not attempt to download.
  - **CDN URLs in pasted content** (e.g., `https://www.paypalobjects.com/devdoc/foo.png`): **automatically `curl` these and save to `raw/assets/`** when creating the raw file. Rewrite the image references from the CDN URL to the local `assets/filename.png` path in the raw file. Do not wait for the user to provide URLs separately — if `https://` image URLs appear in pasted content, download them immediately as part of raw file creation.

- If the source is images-only (no accompanying text), create a stub raw `.md` file that lists the images with brief descriptions.

##### Mixed content (text + images)

- Create one raw `.md` file with the verbatim text content.
- Save all images to `raw/assets/` with context-based names.
- Embed image references inline in the raw `.md` at the positions they appeared in the original content.

##### GitHub repository

Use **stub file + key excerpts** (with re-clone fallback for deeper queries).

- Create a **stub file**: `raw/<repo-slug>.md` (e.g., `raw/github-stripe-node.md`) — this is the lint anchor and the **navigation guide** for deep-dive queries:

  ```markdown
  <!-- Repo: https://github.com/org/repo -->
  <!-- Commit SHA: abc123 -->
  <!-- Date reviewed: YYYY-MM-DD -->
  <!-- Detail directory: raw/<repo-slug>/ -->
  <!-- Files saved (read directly from these paths):
    raw/<repo-slug>/path/to/file1.ts
    raw/<repo-slug>/path/to/file2.ts
  -->
  <!-- Deep-dive fallback: if a query needs files NOT listed above, re-clone from the repo URL at the commit SHA above, then save any newly discovered files into raw/<repo-slug>/ preserving their repo-relative paths -->
  ```

  **Important**: File paths in the stub must use **full `raw/` paths** (e.g., `raw/github-stripe-node/src/index.ts`), not repo-relative paths. This allows an agent to call `Read("raw/github-stripe-node/src/index.ts")` directly without inferring the prefix.

- Include a **"What each file covers" table** in the stub body — one row per saved file with a brief description of what to find there. This lets an agent select the right file for a query without opening every file:

  ```markdown
  | File | What to find there |
  | ---- | ------------------ |
  | `raw/<repo-slug>/src/load-script.ts` | Caching logic, namespace resolution |
  | `raw/<repo-slug>/types/options.d.ts` | TypeScript interface for all options |
  ```

- Create a **detail directory**: `raw/<repo-slug>/` (e.g., `raw/github-stripe-node/`)
- Save key code files into the detail directory, preserving relative paths from the repo. Focus on files relevant to the wiki's focus (payment integration patterns, SDK usage, API schemas, examples): READMEs, SDK entry points, example files, API schemas, config files — typically 5-20 files.
- In source page frontmatter, `raw_files:` lists only the stub file (e.g., `github-stripe-node.md`) — the stub references the detail subfolder internally.
- **Deep-dive fallback**: When a query requires code-level detail beyond the saved excerpts, re-clone the repo using the URL and commit SHA from the stub file. If the re-clone reveals important files not in the original excerpts, **save them** to `raw/<repo-slug>/` (preserving relative paths), update the stub file's file list and "What each file covers" table. This makes the wiki self-improving — each deep dive enriches the raw excerpts for future queries. Note the re-clone and any newly saved files in the query answer.

### Answer a query

**Flow**: Wiki summaries first (fast) → raw files for depth (fallback) → sweep for gaps → synthesize → optionally file.

1. Read `wiki/index.md` to identify relevant pages.
2. Read the relevant wiki source/company/concept pages.

   **Concept page trust rule**: treat concept pages as a fast index, not a source of truth. Concept pages summarize and can drift from the raw content over time. If a query asks for specific values (API limits, error codes, field names, exact timelines, endpoint paths), always verify against the raw file or source page summary — do not cite concept page values as final answers without verification. Use concept pages to identify *which* source pages to read next.

3. **Deep dive into raw files when needed**: If the source summary lacks sufficient detail, read the corresponding raw files (via `raw_files:` frontmatter) for the full original content. Raw files are the source of truth.

   **Triggers for raw file deep dive**:
   - Query asks for specific code samples, exact parameters, limits, or edge cases not in the summary
   - Summary uses vague language (e.g., "supports multiple methods") but query asks for the exact list
   - Query asks about testing/sandbox details often omitted from summaries
   - Two wiki pages contradict each other — raw file is the tiebreaker

   **For GitHub repo sources** — the raw file is a stub that points to a detail directory:
   1. Read the stub file (`raw/<repo-slug>.md`) — it contains a file list with full `raw/` paths and a "What each file covers" table.
   2. Use the table to identify which saved file answers the query, then `Read` it directly using the full path.
   3. If no saved file covers the query, use the repo URL and commit SHA from the stub to re-clone, find the needed file, save it to `raw/<repo-slug>/`, and update the stub's file list and table.

4. **Sweep unlinked raw files**: grep `raw/` for filenames matching the query topic. Read any relevant raw files not yet linked to a source page — they contain real content that would otherwise be silently missed. Link them to existing source pages or create new source pages as needed.
5. Synthesize an answer with `[[wikilinks]]` citations to wiki pages.
6. **Offer to file the answer** if it meets any of these criteria:
   - **Comparison**: Answer compares two or more platforms/products (e.g., "Stripe vs PayPal handling of X") → offer to file as a **comparison page** in `wiki/comparisons/`
   - **Cross-cutting**: Answer synthesizes 3+ source pages into a unified view → offer to file as an **analysis page** in `wiki/analyses/`
   - **Reusable reference**: Answer produces a table, guide, or checklist others would reference → offer to file as an **analysis page** in `wiki/analyses/`
   - User explicitly requests a filed page

   If filing, update `wiki/index.md` and append to `wiki/log.md`.

**Example walkthrough** — User asks: *"What are Stripe's chargeback fees compared to Adyen's?"*

1. `index.md` → find `source-stripe-pricing-overview.md` and `source-adyen-pricing-overview.md`
2. Source pages mention chargeback fees but lack exact amounts or edge cases
3. **Deep dive triggered** (query asks for specifics) → `raw_files:` → read the corresponding raw files → find exact fee schedules
4. Sweep `raw/` for other files mentioning "chargeback" — find unlinked raw file, create source page
5. Synthesize → return comparison table with `[[wikilinks]]`
6. Offer to file as a **comparison page** in `wiki/comparisons/` — answer compares two platforms on a specific dimension

### Lint the wiki

> **MANDATORY**: Use `TodoWrite` to create one todo item per step below before starting any lint work. Mark each item completed as you finish it — never batch completions.

1. Scan all wiki pages for:
   - Contradictions between pages
   - Stale claims superseded by newer sources
   - Orphan pages (no inbound links)
   - Concepts mentioned but lacking their own page
   - Concept pages that exist but are outdated relative to newer source pages
   - Missing cross-references
   - Data gaps that could be filled with a web search
2. **Verify against raw files** (raw files are NEVER modified — they are immutable source documents):

   **a. Orphan raw files (ingest queue)** — Find raw files with no reference in any wiki source page. This is the primary mechanism for catching files the user uploads directly to `raw/`.
   - How: List all **top-level files** in `raw/` (i.e., `raw/*.md` — not files inside subdirectories or `raw/assets/`). For each, search `wiki/sources/` for its filename in `raw_files:` frontmatter. If not found anywhere, it's an orphan. This works uniformly for all source types — GitHub repo stub files (e.g., `github-stripe-node.md`) are detected the same way as any other raw file.
   - Also check for orphan **subdirectories** in `raw/` that lack a corresponding stub file (e.g., `raw/github-stripe-node/` exists but `raw/github-stripe-node.md` does not) — these need the stub file created first, then linked via ingest.
   - Triage: Present all orphan raw files as a numbered list. For each, propose one of:
     - **Link**: attach to an existing related source page (append to `raw_files:` list + add content to the page body)
     - **New**: create a new source page via the standard ingest workflow
   - Action: User approves per-file, then execute. Run the full ingest workflow (source page → company/concept updates → index → log) for each new source.
   - Example: `raw/stripe-connect-overview.md` has no reference → propose creating a new source page or linking to existing `source-stripe-platform-guide.md` if it covers the same topic.

   **b. Accuracy spot-checks** — For key source pages, compare summaries against their raw files to verify correctness.
   - How: Read the `raw_files:` frontmatter on the source page → read the corresponding raw files → compare key claims, numbers, and details in the summary against the full original content.
   - Flag: Claims in wiki that don't match the raw content, important details the summary omitted, or outdated information that was corrected in a newer raw file.
   - Action: Update the source page summary to match the raw content. Never modify the raw file.
   - Note: Not every raw file needs spot-checking every lint pass — focus on key/high-traffic source pages or pages flagged with contradictions.

   **c. Concept page staleness and gap check** — Verify concept pages are accurate and complete.
   - **Staleness**: for each concept page, check whether its `## Sources` links still match reality, and whether key facts (limits, timelines, API endpoints, field names) differ from the raw file content that backs those sources. Concept pages summarize and can drift.
   - **Gaps**: grep `wiki/sources/` for source pages whose tags match an existing concept page's tags. If newer source pages exist on the topic that the concept page doesn't reference, update the concept page.
   - **Missing concept pages**: count source pages per topic area. If 3+ source pages cover a topic with no concept page in `wiki/concepts/`, flag it as a concept page gap.
   - Action: Update stale or incomplete concept pages. Create missing concept pages using the ingest Phase 2 decision table. Never modify raw files.

   **d. Missing `raw_files:` frontmatter** — Find source pages that lack the `raw_files:` field.
   - How: Scan all source pages in `wiki/sources/`. If a source page has no `raw_files:` field, find the corresponding raw file(s) by matching filenames or source URLs.
   - Action: Add `raw_files:` to the frontmatter with the correct raw filename(s).
   - Example: a source page has detailed content but no `raw_files:` → find the corresponding raw file(s) by matching filenames or source URLs and add them to the frontmatter.

3. Report all findings to the user as a numbered list — orphan raw files, stale concepts, gaps, missing frontmatter, contradictions.
4. Fix issues with user approval. For each fix, run the full ingest workflow (source page → concept audit → company/concept updates → index → log).
5. Log the lint pass in `wiki/log.md`.

## Domain-specific guidance

- **Payment networks** (Visa, Mastercard, etc.) are companies, not concepts.
- **Regulations** (PCI DSS, PSD2, etc.) are concepts with category `regulation`.
- Track funding rounds, acquisitions, and partnerships as timeline entries on company pages.

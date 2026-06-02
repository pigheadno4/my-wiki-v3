# Rule: Answer a query → comparison / analysis

> This rule governs answering questions and filing the result as a comparison or analysis page. You arrived here from the CLAUDE.md Workflow Index.

**Flow**: Wiki summaries first (fast) → raw files for depth (fallback) → sweep for gaps → synthesize → optionally file.

## Steps

1. Read the **root** `wiki/index.md` to find the relevant PSP index(es) and cross-cutting pages, then the relevant `wiki/<psp>-index.md` to identify specific source/company/concept pages.
2. Read the relevant wiki source/company/concept pages.

   **Concept page trust rule**: treat concept pages as a fast index, not a source of truth. Concept pages summarize and can drift from the raw content over time. If a query asks for specific values (API limits, error codes, field names, exact timelines, endpoint paths), always verify against the raw file or source page summary — do not cite concept page values as final answers without verification. Use concept pages to identify *which* source pages to read next.

3. **Deep dive into raw files when needed**: if the source summary lacks sufficient detail, read the corresponding raw files (via `raw_files:` frontmatter) for the full original content. Raw files are the source of truth.

   **Triggers for raw file deep dive**:
   - Query asks for specific code samples, exact parameters, limits, or edge cases not in the summary
   - Summary uses vague language (e.g., "supports multiple methods") but query asks for the exact list
   - Query asks about testing/sandbox details often omitted from summaries
   - Two wiki pages contradict each other — raw file is the tiebreaker

   **For GitHub repo sources** — the raw file is a stub that points to a detail directory (see `github-repos.md`):
   1. Read the stub file (`raw/<repo-slug>.md`) — it contains a file list with full `raw/` paths and a "What each file covers" table.
   2. Use the table to identify which saved file answers the query, then `Read` it directly using the full path.
   3. If no saved file covers the query, use the repo URL and commit SHA from the stub to re-clone, find the needed file, save it to `raw/<repo-slug>/`, and update the stub's file list and table.

4. **Sweep unlinked raw files**: grep `raw/` for filenames matching the query topic. Read any relevant raw files not yet linked to a source page — they contain real content that would otherwise be silently missed. Link them to existing source pages or create new source pages as needed (one at a time, per `ingest.md`).
5. Synthesize an answer with `[[wikilinks]]` citations to wiki pages.
6. **Offer to file the answer** if it meets any of these criteria:
   - **Comparison**: answer compares two or more platforms/products → offer to file as a **comparison page** in `wiki/comparisons/`.
   - **Cross-cutting**: answer synthesizes 3+ source pages into a unified view → offer to file as an **analysis page** in `wiki/analyses/`.
   - **Reusable reference**: answer produces a table, guide, or checklist others would reference → offer to file as an **analysis page**.
   - User explicitly requests a filed page.

   If filing, update `wiki/index.md` (comparisons and analyses are cross-cutting → root index) and cross-link from the relevant `wiki/<psp>-index.md`; append to `wiki/log.md`.

## Example walkthrough

User asks: *"What are Stripe's chargeback fees compared to Adyen's?"*

1. Root `index.md` → `stripe-index.md` + `adyen-index.md` → find `source-stripe-pricing-overview.md` and `source-adyen-pricing-overview.md`.
2. Source pages mention chargeback fees but lack exact amounts or edge cases.
3. **Deep dive triggered** (query asks for specifics) → `raw_files:` → read the corresponding raw files → find exact fee schedules.
4. Sweep `raw/` for other files mentioning "chargeback" — find an unlinked raw file, create a source page.
5. Synthesize → return a comparison table with `[[wikilinks]]`.
6. Offer to file as a **comparison page** (`wiki/comparisons/stripe-vs-adyen-chargeback-fees.md`) — answer compares two platforms on a specific dimension.

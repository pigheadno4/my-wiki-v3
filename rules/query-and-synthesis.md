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

   **For GitHub repository sources**, identify the repository and package before interpreting a version. Follow this evidence routing:

   | Query | Required evidence order |
   | --- | --- |
   | Current integration or API behavior | cumulative source page → latest exact-SHA snapshot when implementation detail is needed |
   | Latest change or new feature | source page → repository changelog → linked release notes, comparison, and snapshot |
   | Version-specific behavior | repository changelog → exact package-qualified release record → linked SHA snapshot |
   | Upgrade or version comparison | both changelog entries → package comparison → both exact-SHA snapshots |
   | Deep source question | exact-SHA source capsule and assigned source files; never the changelog summary alone |
   | Historical behavior | historical source-page version section → changelog entry → exact release record and snapshot |

   Read every selected evidence file in full. If the capsule does not contain enough source to answer a deep question, record the evidence gap and run a separately approved exact-SHA supplemental collection:

   ```bash
   python3 scripts/collect_github_repos.py supplement --repo <owner/repo> --sha <full-sha> --path <repo-relative-path>
   ```

   Repeat `--path` for multiple explicitly approved files. The supplement is a new immutable addition; never modify an accepted snapshot or legacy raw file.

   Search a related repository only when the documented responsibility boundary requires it. Name the different repository and evidence authority in the answer. Label default-branch or untagged SHA evidence as unreleased.

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

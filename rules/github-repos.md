# Rule: Ingest a GitHub repository

> This rule governs ingesting GitHub repos (SDKs, sample apps, integration tools, API specs). You arrived here from the CLAUDE.md Workflow Index. This is the **special manual path** for content that is *not* in a PSP's `llms.txt` — e.g., a PSP's product-integration sample/feature/tool repos.

GitHub repos use a **stub file + key excerpts** strategy (with a re-clone fallback for deeper queries). The stub is the lint anchor; the detail directory holds the saved code.

## Workflow

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
11. Update the relevant index (`wiki/index.md` and/or `wiki/<psp>-index.md`) with new/updated pages.
12. Append an entry to `wiki/log.md`.
13. **Clean up** the temp clone.

> The page-creation steps (6–12) follow the same NO-BATCH / concept-audit-first discipline as `ingest.md`. Stub files are **not** dated (they are version-anchored by commit SHA, not collection date).

## Stub file format

Create a **stub file** `raw/<repo-slug>.md` — this is the lint anchor and the **navigation guide** for deep-dive queries:

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

Include a **"What each file covers" table** in the stub body — one row per saved file with a brief description of what to find there. This lets an agent select the right file for a query without opening every file:

```markdown
| File | What to find there |
| ---- | ------------------ |
| `raw/<repo-slug>/src/load-script.ts` | Caching logic, namespace resolution |
| `raw/<repo-slug>/types/options.d.ts` | TypeScript interface for all options |
```

## Saving the detail directory

- Create a **detail directory**: `raw/<repo-slug>/` (e.g., `raw/github-stripe-node/`)
- Save key code files into the detail directory, preserving relative paths from the repo. Focus on files relevant to the wiki's focus (payment integration patterns, SDK usage, API schemas, examples): READMEs, SDK entry points, example files, API schemas, config files — typically 5-20 files.
- In source page frontmatter, `raw_files:` lists only the stub file (e.g., `github-stripe-node.md`) — the stub references the detail subfolder internally.

## Deep-dive fallback (self-improving)

When a query requires code-level detail beyond the saved excerpts, re-clone the repo using the URL and commit SHA from the stub file. If the re-clone reveals important files not in the original excerpts, **save them** to `raw/<repo-slug>/` (preserving relative paths), and update the stub file's file list and "What each file covers" table. This makes the wiki self-improving — each deep dive enriches the raw excerpts for future queries. Note the re-clone and any newly saved files in the query answer.

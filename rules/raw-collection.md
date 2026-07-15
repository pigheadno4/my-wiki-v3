# Rule: Raw content collection (manual)

> This rule governs **manually** creating raw source files — pasted text, fetched URLs, images, mixed content. You arrived here from the CLAUDE.md Workflow Index. For bulk PSP-docs collection see `psp-collection.md`; for GitHub repos see `github-repos.md`.

Raw collection is the **front end** of the manual ingest pipeline. After a raw file is created and verified here, ingest it via `ingest.md`.

## Raw file rules (source of truth)

- The `raw/` directory is the **source of truth** — it preserves the original content exactly as received. If you need to summarize, that belongs in `wiki/sources/`, never in `raw/`.
- Raw files are **immutable** — never modify an accepted raw file after creation.
- Summaries and analysis belong in `wiki/sources/`, not in `raw/`.
- Always create the raw file(s) **before** creating or updating source summaries.
- The `raw_files:` frontmatter field lists filenames relative to `raw/` (e.g., `stripe-invoicing-overview-2026-06-02.md` means `raw/stripe-invoicing-overview-2026-06-02.md`).

### Dated filenames (all new raw files)

- **Every new raw file carries a collection date**: `raw/<slug>-YYYY-MM-DD.md` (the date you created/fetched it).
- The pre-existing undated files (`raw/<slug>.md`) are the **baseline** — leave them as-is; they migrate to dated naming naturally the next time that page is re-collected.
- Source-page slugs (`source-<slug>.md`) are **never** dated — only raw files carry dates. When a source is re-collected and changes, the source page's `raw_files:` accumulates versions **newest-first**; the source summary reflects the latest and notes the delta.
- See `psp-collection.md` for the diff-on-recollect mechanics (download → diff vs prior version → keep only if changed).

## Manual pipeline — Phase 1 (raw file + verbatim check)

> Requires user approval before ingest (Phase 2 in `ingest.md`).

1. **If the source content is markdown** (pasted text/webpage): create an **empty raw file** with just the metadata header, then ask the user to paste the full content directly into the raw file in their editor. Wait for them to confirm the paste is done before proceeding.

   **If the source is a URL to fetch** or images: write the raw file directly with the fetched/downloaded content (download any CDN image URLs to `raw/assets/` automatically).
2. Compare the raw file against the pasted content and report:
   - **Key findings** — the most important takeaways from this source (bullet summary)
   - **Verbatim check** — list any differences between what was pasted and what was written to the raw file. If the content is verbatim, confirm that explicitly. Flag any collapsed whitespace, missing sections, or formatting changes, and note whether they are rendering artifacts (acceptable) or content changes (must fix).
3. **Wait for user approval** before proceeding to ingest. Do not create wiki pages until the user confirms the raw file is acceptable.

### Common verbatim failure modes to watch for

- Collapsing a bullet list of countries into a comma-separated sentence
- Removing or simplifying CSS class strings (`data-pp-*`, `.css-...`)
- Stripping link text and keeping only the URL (or vice versa)
- Renaming or relabeling code block headings (e.g. `#### **\`Sample request\`**`)
- Restructuring sections or adding new headings not in the original
- Replacing inline HTML entities (`&lt;`, `&gt;`) with the rendered characters
- Truncating large JSON/curl examples or replacing them with `[...]` placeholders
- Adding markdown formatting (bold, code ticks) that wasn't in the source
- Collapsing many blank lines that are clearly HTML rendering artifacts (acceptable — note but don't fix)

## Handle large source content

When the user shares source content that exceeds the message character limit (truncated at ~50,000 characters):

1. **Create the raw file immediately** with a placeholder or the filename derived from the content title (dated).
2. **Notify the user** to paste the full content directly into the raw file.
3. **Wait for the user** to confirm the paste is complete before reviewing and ingesting.

Do NOT attempt to summarize truncated content — the partial view may miss critical details. Always get the full content first.

## Tiered raw file strategy by source type

| Source type | Raw file format | Rationale |
| --- | --- | --- |
| Pasted text/markdown | Verbatim `.md` copy | Content exists nowhere else — raw is the only record |
| Website URL | Fetched markdown + metadata header | Web pages change/disappear — snapshot has archival value |
| Images/screenshots | Image files in `raw/assets/` + reference in raw `.md` | Preserves the actual visual artifact |
| GitHub repo | Immutable snapshot manifest plus exact selected upstream files in `raw/github/<company>/<repo>/snapshots/`; generated diffs, summaries, status, and packets in `tracking/github/` | See `github-repos.md` |
| PSP docs (bulk) | Fetched `.md` per page, dated, diff-on-recollect | See `psp-collection.md` |

### Pasted text/markdown

- **CRITICAL: Raw files must contain the EXACT, VERBATIM, FULL content** the user pasted — copy it word-for-word into the raw file. **DO NOT summarize, condense, paraphrase, reformat, or omit any part of the content.**
- When the user pastes content that fits within the message limit, write the entire pasted content directly to the raw file — not a summary or condensed version.

### Website URL

- Fetch the page content and save as `.md` in `raw/` (dated filename).
- Add a metadata header at the top of the raw file:

  ```html
  <!-- Source URL: https://example.com/page -->
  <!-- Fetched: YYYY-MM-DD -->
  ```

- The fetched markdown is an HTML→markdown conversion — not pixel-perfect, but the best reproducible capture.

### Images and screenshots

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

### Mixed content (text + images)

- Create one raw `.md` file with the verbatim text content.
- Save all images to `raw/assets/` with context-based names.
- Embed image references inline in the raw `.md` at the positions they appeared in the original content.

## Next step

Once Phase 1 is approved, ingest the raw file **one at a time** per `ingest.md`.

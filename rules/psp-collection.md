# Rule: PSP documentation collection (automated)

> This rule governs **bulk** collection of a PSP's documentation via `scripts/fetch_psp.py`. You arrived here from the CLAUDE.md Workflow Index. For one-off manual pages see `raw-collection.md`. Per-PSP specifics live in `rules/psp/<psp>.md`.

PSPs (Stripe, PayPal, Adyen, and any added later) publish machine-readable docs: an `llms.txt` index of `.md` page URLs, sometimes an `llms-full.txt` concatenated corpus. The fetcher turns that into dated raw files. **Collection is batch and fast; ingest stays strictly one-at-a-time.**

## The two pipelines

**Manual flow** (see `raw-collection.md`): collect one page → verbatim verify → share key findings → wait for approval → ingest. Human-in-the-loop, for one-off pastes/URLs/images.

**Auto flow** (this rule):
1. Run `fetch_psp.py` for a PSP (optionally scoped to a section). It batch-downloads `.md` pages into a **staging area**, diffs each against the most recent prior version, and keeps only **new or changed** files.
2. When **all collection runs for the round finish**, the fetcher writes a **round manifest** listing new files and changed files (with stored diffs).
3. **The fetcher does NOT auto-ingest.** It **pings the user to kick off ingest.**
4. The user then ingests the manifest **one source at a time** per `ingest.md`. For changed files, the stored diff lets the source page update reflect only the delta.

`lint.md`'s "orphan raw files (ingest queue)" step is the safety net that surfaces any collected file not yet ingested.

## Running the fetcher

```bash
# Collect from a PSP's llms.txt (or llms-full.txt where available):
python scripts/fetch_psp.py <psp> --from llms.txt
python scripts/fetch_psp.py <psp> --section checkout      # scope to a section
python scripts/fetch_psp.py <psp> --urls urls.txt         # explicit URL list
```

Behaviour (implemented in `fetch_psp.py`, configured per PSP in `scripts/psp_config.toml`):

1. Read the PSP's discovery file per config (`llms.txt`, or `llms-full.txt` if `has_full_corpus`).
2. **Apply `url_fixups`** — correct known malformed links before fetching. Example confirmed in smoke testing: a duplicated path segment like `/api-explorer/api-explorer/` must collapse to `/api-explorer/`. Every fixup applied is logged so re-runs are auditable.
3. For each target page: fetch the `.md` variant, slugify the URL path → `raw/<psp>-<slug>-YYYY-MM-DD.md`, and prepend:
   ```html
   <!-- Source URL: https://<host>/<path> -->
   <!-- Fetched: YYYY-MM-DD -->
   ```
4. Write to a **staging area** first, then diff against the most recent prior version of the same slug (dated *or* the undated baseline), ignoring the header lines:
   - **identical** → discard the staged copy (nothing to ingest);
   - **changed** → promote to `raw/` and add to the round manifest with the stored diff;
   - **brand-new** → promote and mark "new".
5. **Idempotent / immutable**: never overwrites an accepted raw file. Only a *staged* file is ever discarded. Re-runs are safe and only surface real changes.

## Retention

When a re-collected page changed, the previous dated version **stays** as immutable history; the new dated version is added alongside. The source page's `raw_files:` lists versions **newest-first**. (Decision: keep all versions.)

## Onboard a new PSP (≈ 5 minutes)

PSPs are a **registry**, not a fixed set. To add e.g. Airwallex or Braintree:

1. Find the PSP's discovery file (`https://<host>/llms.txt`; check for `llms-full.txt`) and confirm the `.md` page pattern (usually "append `.md`").
2. Add a row to `scripts/psp_config.toml`:
   ```toml
   [airwallex]
   host = "www.airwallex.com/docs"
   discovery_file = "llms.txt"
   md_rule = "append-.md"
   has_full_corpus = false
   url_fixups = []          # add [pattern, replacement] pairs as quirks are found
   ```
3. Create `rules/psp/airwallex.md` from the template the existing PSP files follow (host, discovery file, `.md` rule, known fixups, known GitHub integration repos).
4. Run `python scripts/fetch_psp.py airwallex --from llms.txt`, then ingest the manifest one at a time.

Nothing else in the rules hardcodes the PSP set.

## Collection → ingest boundary (do not cross it automatically)

- The fetcher's job ends at "files staged/promoted + manifest written + user pinged."
- Ingest is a **separate, human-kicked-off, one-at-a-time** activity (`ingest.md`).
- Never let a collection run flow straight into batch ingest — that violates the NO-BATCH rule and produces shallow pages.

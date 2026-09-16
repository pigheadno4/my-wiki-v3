# PSP: Adyen — collection profile

> Per-PSP collection specifics for Adyen. Used with `rules/psp-collection.md` and `scripts/psp_config.toml`. Verified 2026-06-02. (No Adyen content ingested yet — this is the collection on-ramp.)

## Discovery files (Adyen has TWO)

Adyen splits its machine-readable docs across two `llms.txt` files — you need **both**:

| Source | Discovery file | Covers | Full corpus | `.md` rule |
| --- | --- | --- | --- | --- |
| General docs | `https://docs.adyen.com/llms.txt` | guides, product docs, integration how-tos | ✅ `https://docs.adyen.com/llms-full.txt` | append `.md` (home is `https://docs.adyen.com/.md`) |
| **API Explorer** | `https://docs.adyen.com/api-explorer/llms.txt` | the **API reference** (endpoints, params, request/response) — **NOT in the general `llms.txt`** | none | append `.md` (**after the url fixup below**) |

| Field | Value |
| --- | --- |
| Doc host | `docs.adyen.com` |
| General docs raw | `raw/adyen/docs/<official-path>/YYYY-MM-DD.md` (home: `docs/index/`) |
| API Explorer raw | `raw/adyen/api-explorer/<official-path-after-api-explorer>/YYYY-MM-DD.md` |

## Known `url_fixups` (REQUIRED for API Explorer)

The API Explorer `llms.txt` lists links with a **duplicated path segment** that 404s as written — confirmed in smoke testing. Collapse it before fetching:

```
/api-explorer/api-explorer/  →  /api-explorer/
```

Example (verbatim from `api-explorer/llms.txt`):
- Listed (broken): `https://docs.adyen.com/api-explorer/api-explorer/Checkout/latest/post/sessions.md`
- Fetchable (fixed): `https://docs.adyen.com/api-explorer/Checkout/latest/post/sessions.md`

Encode this as a `[pattern, replacement]` pair in the `api-explorer` discovery entry of the `[adyen]` table in `psp_config.toml`.

## Collection notes

- Adyen explicitly documents the `.md` convention ("Every page is also available as Markdown by appending `.md` to the URL").
- Current supported command: `python scripts/fetch_psp.py adyen` collects both discovery catalogs page by page. `--source docs` or `--source api-explorer` scopes the catalog; `--limit N` is for smoke testing.
- `llms-full.txt` is available, but full-corpus splitting and `--from` are not implemented. Use the page-by-page path above.
- API reference: collect from `api-explorer/llms.txt` (with the fixup). No full corpus here — fetch each `.md` page.
- Sections include Online payments, Point of sale, Adyen for Platforms, Issuing, and Risk management. `--section` is not currently implemented.
- Preserve official URL path case, including API names. Each page owns its dated snapshots; unchanged content adds no snapshot and accepted files are never overwritten. The September 14–15 flat files were relocated byte-for-byte into this layout. Manifests and future source `raw_files` use paths relative to `raw/`; wikilinks must include the path, not the ambiguous date alone. GitHub evidence remains under `raw/github/adyen/`.

## Known GitHub integration repos (manual path — see `github-repos.md`)

Adyen publishes SDKs/sample apps on GitHub (e.g., `Adyen/adyen-web`, `Adyen/adyen-node-api-library`, `Adyen/adyen-android`, `Adyen/adyen-ios`). Ingest via the GitHub repo workflow when needed. None saved yet.

## Wiki placement

- Per-PSP index: `wiki/adyen-index.md` (create on first Adyen ingest)
- Company page: `wiki/companies/adyen.md`
- Platform concepts: `adyen-*` (e.g., `adyen-marketpay`)

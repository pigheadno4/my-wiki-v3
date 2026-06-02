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
| Raw filename | `raw/adyen-<slug>-YYYY-MM-DD.md` |

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
- General docs: prefer `--from llms-full.txt` for a complete corpus grab. Because `llms-full.txt` is one concatenated document, the fetcher must **split it back into per-page raw files** (one `raw/adyen-<slug>-YYYY-MM-DD.md` per page) so each ingests independently and orphan detection works per page.
- API reference: collect from `api-explorer/llms.txt` (with the fixup). No full corpus here — fetch each `.md` page.
- Sections include: Online payments, Point of sale, Adyen for Platforms, Issuing, Risk management. Use `--section` to scope a run.

## Known GitHub integration repos (manual path — see `github-repos.md`)

Adyen publishes SDKs/sample apps on GitHub (e.g., `Adyen/adyen-web`, `Adyen/adyen-node-api-library`, `Adyen/adyen-android`, `Adyen/adyen-ios`). Ingest via the GitHub repo workflow when needed. None saved yet.

## Wiki placement

- Per-PSP index: `wiki/adyen-index.md` (create on first Adyen ingest)
- Company page: `wiki/companies/adyen.md`
- Platform concepts: `adyen-*` (e.g., `adyen-marketpay`)

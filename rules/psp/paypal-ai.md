# PSP: PayPal.ai — collection profile

> Per-PSP collection specifics for PayPal. Used with `rules/psp-collection.md` and `scripts/psp_config.toml`. Original profile verified 2026-06-02; identity clarified 2026-09-15. The existing script/config key remains `paypal`, not `paypal-ai`.

## Docs collection

| Field | Value |
| --- | --- |
| Doc host | `docs.paypal.ai` (the LLM-optimized Mintlify mirror) |
| Discovery file | `https://docs.paypal.ai/llms.txt` |
| Full corpus | Not configured; the original 2026-06-02 check reported none |
| `.md` rule | Append `.md` to any doc URL, e.g. `https://docs.paypal.ai/developer/how-to/api/get-started.md` |
| Raw filename | `raw/paypal-<slug>-YYYY-MM-DD.md` |

> This profile covers only `docs.paypal.ai`. Legacy developer documentation follows [paypal-legacy.md](paypal-legacy.md); the upgraded portal follows [paypal-new.md](paypal-new.md). A past certificate error does not prohibit collection from the developer portal under its own profile. Do not substitute content across these corpora or assume identical coverage.

Notes:
- Paths are deep (e.g., `/developer/how-to/api/troubleshooting/common-errors/...`) — slugify carefully and keep slugs readable.

## Known `url_fixups`

- Watch for duplicated path segments in `llms.txt` links (the smoke-test class of bug, e.g. `/api-explorer/api-explorer/`). Add confirmed `[pattern, replacement]` pairs to the `[paypal]` table in `psp_config.toml`.

## Known GitHub integration repos (manual path — see `github-repos.md`)

Not in `llms.txt`; ingest via the GitHub repo workflow:
- `paypal/PayPal-JavaScript-SDK` / `paypal-js` (`raw/github-paypal-js.md`, `raw/github-paypal-js-v6.md`)
- `paypal/react-paypal-js` (`raw/github-react-paypal-js-v8.md`)
- `paypal/paypal-android` (`raw/github-paypal-android.md`), `paypal/paypal-ios` (`raw/github-paypal-ios.md`)
- Server SDKs: `raw/github-paypal-ts-server-sdk.md`, `raw/github-paypal-php-server-sdk.md`, `raw/github-paypal-payouts-php-sdk.md`
- `raw/github-paypal-rest-api-specs.md`, `raw/github-paypal-postman-collections.md`
- Components/samples: `raw/github-paypal-applepay-component.md`, `raw/github-paypal-googlepay-component.md`, `raw/github-paypal-v6-samples.md`, `raw/github-fastlane-sample-application.md`

## Wiki placement

- Per-PSP index: `wiki/paypal-index.md`
- Company page: `wiki/companies/paypal.md`
- Platform concepts: `paypal-*` (e.g., `paypal-vault`, `paypal-apm-*`)

## Current command and boundary

`python scripts/fetch_psp.py paypal` uses this host's `llms.txt`; it does not collect legacy or new developer.paypal.com. The current parser extracts absolute `.md` links. Supported options are `--source`, `--limit`, and `--dry-run`, not `--from`, `--section`, or `--urls`.

Keep existing raw filenames and versions unchanged. This identity clarification does not migrate raw or rename the config key. Collection must stop at its manifest, with errors reported separately; ingestion requires separate approval. The legacy generic script's exit code alone is not proof of complete coverage or valid Markdown bodies.

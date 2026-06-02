# PSP: PayPal — collection profile

> Per-PSP collection specifics for PayPal. Used with `rules/psp-collection.md` and `scripts/psp_config.toml`. Verified 2026-06-02.

## Docs collection

| Field | Value |
| --- | --- |
| Doc host | `docs.paypal.ai` (the LLM-optimized Mintlify mirror) |
| Discovery file | `https://docs.paypal.ai/llms.txt` |
| Full corpus | **None** — no `llms-full.txt` |
| `.md` rule | Append `.md` to any doc URL, e.g. `https://docs.paypal.ai/developer/how-to/api/get-started.md` |
| Raw filename | `raw/paypal-<slug>-YYYY-MM-DD.md` |

> ⚠️ **Use `docs.paypal.ai`, not `developer.paypal.com`.** The machine-readable `llms.txt` + `.md` pages live at `docs.paypal.ai`. `developer.paypal.com/llms.txt` returned a certificate error during verification and is the human portal, not the collection source. Keep `developer.paypal.com` only as a fallback for pages missing from the `.ai` mirror.

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

# PSP: Stripe — collection profile

> Per-PSP collection specifics for Stripe. Used with `rules/psp-collection.md` and `scripts/psp_config.toml`. Verified 2026-06-02.

## Docs collection

| Field | Value |
| --- | --- |
| Doc host | `docs.stripe.com` |
| Discovery file | `https://docs.stripe.com/llms.txt` (~400 links, grouped by product section) |
| Full corpus | **None** — no `llms-full.txt` |
| `.md` rule | Append `.md` to any doc URL, e.g. `https://docs.stripe.com/payments/quickstart.md` |
| Raw filename | `raw/stripe-<slug>-YYYY-MM-DD.md` |

Notes:
- `llms.txt` opens with a Stripe-authored instruction header (about checking npm/pip for the latest SDK version) before the `## Docs` link list — skip the header, parse the link list.
- Sections include: Payments, Checkout, Payment Methods, Link, Billing, Elements, Connect, Issuing, Radar, Terminal, Tax, Invoicing, Identity, Financial Connections, Treasury, etc. Use `--section <name>` to scope a run.

## Known `url_fixups`

- None confirmed yet. Add `[pattern, replacement]` pairs to the `[stripe]` table in `psp_config.toml` as malformed links are found during runs.

## Known GitHub integration repos (manual path — see `github-repos.md`)

Not in `llms.txt`; ingest via the GitHub repo workflow:
- `stripe/stripe-node` (`raw/github-stripe-node.md`)
- `stripe/stripe-ios` (`raw/github-stripe-ios.md`)
- `stripe/stripe-android` (`raw/github-stripe-android.md`)
- `stripe/stripe-react-native` (`raw/github-stripe-react-native.md`)
- `stripe/react-stripe-js` (`raw/github-react-stripe-js.md`)
- Stripe Postman collection (`raw/github-stripe-postman.md`)

## Wiki placement

- Per-PSP index: `wiki/stripe-index.md`
- Company page: `wiki/companies/stripe.md`
- Platform concepts: `stripe-*` (e.g., `stripe-radar`, `stripe-payment-intents`)

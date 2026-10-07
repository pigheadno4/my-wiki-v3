# Braintree C44 fixed-query audit M — positions 49–50

- Campaign: `braintree-campaign-44`
- Mode: read-only independent query audit
- Scope: approved manifest positions 49–50; exactly two fixed questions per page (4 total)
- Completed UTC: `2026-10-07T13:04:33Z`
- Result: **PASS — 4/4 queries**

## Shared checks

- **Approval, pins and provenance — PASS.** Both attempt-1 reviews are `approved`, `full`, with zero required changes; installed sources exactly match their reviewed candidates. Recomputed SHA-256 values match the manifest: Google Pay configuration `9405b7a66ec869bc918d6521264797e3030a0d33e99016448cdf14aee227e981`; Elo testing `8ef5f3a1199f440914c3d22818637d12111c660ddbba066fee4ffc8764f924a5`. Manifest URL, unique source `canonical_url`, raw `Source URL`, `raw_files`, and `Raw Sources` agree; both raws record `Fetched: 2026-09-16` and `Discovery: llms.txt,sitemap.xml`.
- **PRIMARY ownership and reciprocal routing — PASS.** Exact raw-path and canonical-URL lookups find one source owner per primary, and neither primary is reused as another source's supporting raw. Both routes resolve `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md` → source → exact raw, with reciprocal source-to-concept links. The corrected concept context keeps the historical Google Pay testing entry at `:59` and the configuration entry independently at `:61`; Elo is at `:23`. Direct provider-catalog rows are deferred shared-close work, not failures while the concept routes work.
- **Full reads, bounded gap sweep and detail limits — PASS.** The two sources, two pinned raws, central concept, and root/provider routes were read in full. One bounded filename/backlink sweep covered Google Pay and Elo sibling guides; no retained claim or conflict required supporting authority, so no sibling raw was promoted to evidence. The Google page's collapsed link/spacing and Elo's rendered fixture tables are not presented as copy-ready syntax or runnable guarantees. Exact card values, field values, settings, and external navigation remain at raw locators; the sources make no false current-support, enablement, Production, integration, or payment-outcome claim.

## Position 49 — `docs-guides-google-pay-configuration-javascript-v3` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md:61` → `wiki/sources/braintree/source-braintree-docs-guides-google-pay-configuration-javascript-v3.md` → `raw/braintree/docs/guides/google-pay/configuration/javascript/v3-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's 2026-09-16 website snapshot of Google Pay configuration on the JavaScript v3 documentation route, not an exact `braintree-web` package/version contract. For Sandbox or Production, the merchant enables Google Pay under the matching Control Panel's **Account Settings** → **Payment Methods**; a particular merchant account may require Braintree support, Production separately requires work with Google, and PayPal via Google Pay requires both PayPal and Google Pay enabled. The page does not prove current browser coverage, eligibility, account enablement, Google approval, client/server integration, payment execution, settlement, or funding. Source `:14,18-21`; raw `:16-17,20-38`.
2. **Purpose, action, conditions, warnings and detail route — PASS.** The central purpose is environment-specific configuration, with merchant-account escalation, separate Google go-live work, and dual enablement for PayPal via Google Pay preserved as material conditions. The source routes the exact availability statement, Control Panel sequence, support route, Production condition, and dual-enablement text to raw `:16-17,20-38`; malformed captured spacing is not upgraded into copy-ready instructions.

## Position 50 — `docs-guides-elo-testing` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md:23` → `wiki/sources/braintree/source-braintree-docs-guides-elo-testing.md` → `raw/braintree/docs/guides/elo/testing-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's 2026-09-16 captured, unversioned Elo testing webpage for select limited-release merchants using what the page calls the latest JavaScript v3 and server SDKs; it identifies no exact package or release. Its environment is Sandbox, its objects are three Elo credit-card fixtures plus `expirationYear` and `expirationDate` test fields, and its action scope is testing an integration or triggering expired-card errors during verification/enrollment API calls. It does not establish current access, the currently latest SDKs, Production card data, merchant enablement, a successful payment, settlement, or funding. Source `:14,18-22`; raw `:17-37`.
2. **Purpose, action, conditions, warnings and detail route — PASS.** The central purpose is fixture retrieval under limited-release, select-merchant, relative-latest-SDK and Sandbox conditions. The source preserves the Production and execution warning while routing exact card numbers to raw `:21-28` and the precise error-trigger fields/values to raw `:31-37`; no code or fixture is claimed as a universal runnable success guarantee.

## Query tally

| Page | Q1 exact scope | Q2 purpose/actions/conditions/detail route |
| --- | --- | --- |
| Google Pay configuration — JavaScript v3 | PASS | PASS |
| Elo testing | PASS | PASS |

No correction or additional supporting authority is required. **Verdict: PASS — 2/2 pages, 4/4 fixed questions.**

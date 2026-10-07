# Braintree C44 fixed-query audit — group K

- Scope: approved C44 positions 41–44; eight predetermined queries.
- Result: **PASS — 8/8 queries**.
- Completed UTC: `2026-10-07T13:00:18Z`

## Shared checks

- **Approval, pins and provenance — PASS.** All four jobs are `approved` at attempt 1. Recomputed SHA-256 matches the manifest: Amex configuration `b08c2943dbea9aad8ae04adac521ea36df4e39367fb1a8aaca025f0d1e779d95`; Credit Card Verification response (Node) `c3fd55071a676a7dd580e528c79e207863fab8d6a4243c3affe0fbb9e51a74aa`; Masterpass testing/go-live `c692fd920fa7773b6b2ffecdcfedb671680d4842e2b24c5b34d001aa2683fc40`; Elo JavaScript v3 client guide `5cc1014fa14d4ebf3814e9ba6167ac4ba89c16a9ab1ac93ef265b5ddcaceb854`. Manifest URL, source `canonical_url`, raw `Source URL`, `raw_files`, and `Raw Sources` agree; each raw records `Fetched: 2026-09-16` and `Discovery: llms.txt,sitemap.xml`; each promoted source is byte-identical to its accepted candidate.
- **PRIMARY ownership and reciprocity — PASS.** Each exact primary raw path and canonical URL has one source owner under `wiki/sources/`; none of the four source pages duplicates another primary as supporting raw. Routes resolve `wiki/index.md:11` → `wiki/braintree-index.md:813,821` → main concept → source → exact primary raw. Main-concept reciprocity is present at `wiki/concepts/braintree-payment-methods.md:23,25,27` and `wiki/concepts/braintree-server-sdk.md:49`; sources link back at their lines `39`, `37`, `35`, and `32`. Deferred direct provider-catalog rows are shared-close work, not failures while these concept routes work.
- **Full reads and bounded gap sweep — PASS.** The root/provider indexes, four sources, four pinned raws, both main concepts, and Elo's linked Web SDK concept were read in full. One bounded filename/topic sweep covered adjacent Amex, Credit Card Verification request/search, Masterpass, Elo, and SRC routes. Only Amex/Masterpass retain the same support-status conflict, so the linked SRC supporting source and its pinned raw were also read in full; other siblings remain navigation only. The Elo script tag is illustrative and nonblocking: the source makes no runnable, exact-current-package, successful-execution, or payment-outcome guarantee.

## Position 41 — `docs-guides-amex-express-checkout-configuration` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md:27` → `wiki/sources/braintree/source-braintree-docs-guides-amex-express-checkout-configuration.md` → `raw/braintree/docs/guides/amex-express-checkout/configuration-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16, unversioned website configuration page for legacy Amex Express Checkout. It covers merchant Control Panel enablement/signup, returned `client_id`/`client_key` configuration material, checkout-tag setup, and a separate Sandbox-account repetition. Android v2, iOS v4, and JavaScript v3 identify only the Client SDK generations in which replacement SRC was introduced; the page supplies no exact SDK package/runtime or payment object. Do not infer current Amex/SRC support, merchant eligibility or enablement, usable credentials, migration success, or payment execution. Source `:14,18-27`; raw `:17-35`.
2. **Purpose, action, conditions, warnings and detail route — PASS.** The central action is Control Panel **Processing** → **Payment Methods** → Amex Express Checkout **Enable**, followed by signup submission, use of the returned client credentials in the checkout tag, and repetition in the merchant's Sandbox account. The source preserves the material contradiction between replacement-by-SRC and current-tense legacy configuration, plus SRC's eligible-merchant limited release, changeable API, and access-request conditions. The fully read SRC authority separately conflicts between a January 20, 2026 end-of-support notice and current-tense limited release, so present support and a safe migration path remain unresolved. Source `:18-34`; primary raw `:17-35`; supporting source `wiki/sources/braintree/source-braintree-payment-methods-secure-remote-commerce.md:18-35`; supporting raw `raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16.md:14-23,28-48,88-90`.

## Position 42 — `docs-reference-response-credit-card-verification-node` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:821` → `wiki/concepts/braintree-server-sdk.md:49` → `wiki/sources/braintree/source-braintree-docs-reference-response-credit-card-verification-node.md` → `raw/braintree/docs/reference/response/credit-card-verification/node-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16, unversioned Node.js website response reference for Credit Card Verification data, not an exact Node package/version, request guide, or charge API. Its objects are gateway-returned product IDs and optional processor/network response code and text on some transaction and verification objects; its captured containing-object/request lists are blank. It names no environment or account qualification. Do not infer an originating operation, code-to-product mapping, approval, verification status, charge, lifecycle outcome, current enablement, or exact SDK behavior. Source `:14,18-21,30-32`; raw `:17-59`.
2. **Purpose, action, conditions, warnings and detail route — PASS.** The page's purpose is response interpretation: product IDs are generally one to three characters and describe an issued credit product, but the captured inventory is absent; network response values, when present, are raw card-network diagnostics that may explain approval or decline, while the processor response code remains the source of truth. The linked data-protection policy is not in the pinned raw and is correctly left uninterpreted. Source `:18-28`; raw `:17-18,21-46,47-59`.

## Position 43 — `docs-guides-masterpass-testing-go-live` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md:25` → `wiki/sources/braintree/source-braintree-docs-guides-masterpass-testing-go-live.md` → `raw/braintree/docs/guides/masterpass/testing-go-live-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16, unversioned website testing reference for replaced Masterpass, scoped to Sandbox card-number validation and static nonces for server-side-code simulation. The Android v2, iOS v4, and JavaScript v3 labels apply only to the replacement SRC Client SDK families; no exact client/server package, Production environment, or merchant account state is established. The objects are four static Masterpass-originating card nonces. Do not infer a client checkout, real card, current Masterpass/SRC support, account access, successful transaction, settlement, or go-live. Source `:14,18-24`; raw `:17-32`.
2. **Purpose, action, conditions, warnings and detail route — PASS.** Sandbox accepts only Braintree test credit-card numbers; vaulting or transacting with another number produces a validation error. The four fixtures simulate American Express, Discover, Mastercard, and Visa for server-side testing. Despite the title, the body contains no Production activation or go-live procedure. Its direction to limited-release SRC conflicts with the fully read SRC authority's January 20, 2026 end-of-support notice, so current support and safe migration remain unresolved. Source `:18-30`; primary raw `:17-32`; supporting source `wiki/sources/braintree/source-braintree-payment-methods-secure-remote-commerce.md:18-35`; supporting raw `raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16.md:14-23,28-48,88-90`.

## Position 44 — `docs-guides-elo-client-side-javascript-v3` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md:23` → `wiki/sources/braintree/source-braintree-docs-guides-elo-client-side-javascript-v3.md` → `raw/braintree/docs/guides/elo/client-side/javascript/v3-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16 JavaScript v3 client-side Elo checkout webpage with separate server-processing notes. It says Elo is limited to select merchants using the latest JavaScript v3 and server SDK families, but gives no exact current package/version, environment, account configuration, or coverage window; the displayed `3.94.0` script is only a captured example. Its objects/actions are Elo or dual-branded Elo/Discover cards, checkout CVV/expiration fields, and immediate or later settlement submission. Do not infer current availability, enablement, exact-package compatibility, network acceptance, authorization, settlement, funding, or payment success. Source `:14,18-20`; raw `:17-18,21-47`.
2. **Purpose, action, conditions, warnings and detail route — PASS.** The guide orients a JavaScript v3 Elo checkout: select merchants must request access; outside Brazil, dual-branded Elo/Discover transactions must use Discover; Elo cards are credit-only and require CVV plus expiration date; server processing may submit for settlement on creation or later. The source correctly routes the exact script example without turning it into a universal or current runnable requirement. Source `:18-27`; raw `:17-18,24-36,41-47`.

## Query tally

| Page | Q1 exact scope | Q2 purpose/actions/conditions/detail route |
| --- | --- | --- |
| Amex Express Checkout — Configuration | PASS | PASS |
| Credit Card Verification — Response Node | PASS | PASS |
| Masterpass — Testing and Go Live | PASS | PASS |
| Elo — Client-side JavaScript v3 | PASS | PASS |

No correction or additional supporting authority is required. **Verdict: PASS — 4/4 pages, 8/8 fixed questions.**

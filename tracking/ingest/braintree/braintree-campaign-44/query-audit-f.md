# Braintree C44 fixed-query audit — group F

- Scope: approved C44 positions 21–24; eight predetermined queries.
- Result: **PASS — 8/8 queries**.
- Completed UTC: `2026-10-07T12:43:34Z`

## Shared checks

- **Pins, URL and provenance — PASS.** All four jobs are `approved` at attempt 1. Recomputed SHA-256 matches the manifest: Network Tokens Value `450eac0c89d08f373319464390fdfedb6ff808302afb5453189fc75467e141ca`; Functions Advanced `2614124852d3d8b12a632e044b10099e1507e18bec396de7cc900bdc038b7d35`; Channel API Access Token `681950c351dab302b113b4e5a949243608bb81fed330224334b6d11fc4227c04`; Payment Method Response Node `37afc56e7533d3c4fbb256418f5519bf12953ea5fd3ebf96b28b47e19c0e5b37`. Manifest URL, source `canonical_url`, raw `Source URL`, `raw_files`, and `Raw Sources` agree; every raw records `Fetched: 2026-09-16` and `Discovery: llms.txt,sitemap.xml`.
- **PRIMARY ownership and reciprocity — PASS.** Each exact primary raw path and canonical URL has one source owner; none has supporting raw that duplicates its primary. Routes resolve `wiki/index.md:11` → `wiki/braintree-index.md:812,813,821` → main concept → source → primary raw. Concepts reciprocate at `wiki/concepts/braintree-payment-methods.md:39`, `wiki/concepts/braintree-payment-platform.md:31,33`, and `wiki/concepts/braintree-server-sdk.md:49`; sources link back at their lines `14/34`, `14/34`, `14/35`, and `39`. Direct provider-catalog rows are deferred shared-close work, not failures while concept routes work.
- **Full reads and bounded gap sweep — PASS.** The four canonical sources and four pinned raws were read in full. One bounded filename/topic sweep covered adjacent Network Tokens, Functions, Channel API, and payment-method response routes. No sibling raw was needed for a retained claim or conflict, so those remain navigation only. Captured YAML/JavaScript, curl/HTTP, callback, and Promise examples are illustrative and nonblocking: the sources make no runnable, current-support, or successful-execution guarantee and preserve the material field-shape/document gaps.

## Position 21 — `docs-guides-network-tokens-value-to-merchants` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md:39` → `wiki/sources/braintree/source-braintree-docs-guides-network-tokens-value-to-merchants.md` → `raw/braintree/docs/guides/network-tokens/value-to-merchants-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16, unversioned Network Tokens merchant-value webpage. It names no SDK/package/version, client/server procedure, environment, account-specific enablement, or network eligibility. Its objects/actions are customer-card network tokens, one-time cryptograms, Vault lifecycle updates, provisioning, and checkout use. Provider-stated authorization/conversion/security/interchange benefits are not measured outcomes, current availability, a realized rate, or payment success. Source `:14,18-22`; raw `:14-21`.
2. **Purpose, action, conditions, detail route — PASS.** The purpose is benefits orientation: Braintree says it manages provisioning, lifecycle updates, and token use. Approval language is probabilistic; checkout effects are framed as reductions in possible decline/friction; lower interchange is conditional on some networks charging more for non-token transactions. Security detail says issuer-only cryptogram decryption, merchant separation, and one-token-requestor restriction. Source `:18-30`; raw `:17-21`.

## Position 22 — `docs-guides-functions-advanced` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:812` → `wiki/concepts/braintree-payment-platform.md:33` → `wiki/sources/braintree/source-braintree-docs-guides-functions-advanced.md` → `raw/braintree/docs/guides/functions/advanced-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is a fetched 2026-09-16 Braintree Functions advanced-topics documentation preview about generated-configuration environment variables and the JavaScript invocation context. It names no client/server SDK, exact runtime/package version, eligible account, or live deployment. `sandbox`/`production` appear as illustrated configuration/metadata values, not proof of present availability or execution. Source `:14,18-21`; raw `:17-18,21-36,41-66`.
2. **Purpose, action, conditions, detail route — PASS.** A merchant can place custom variables in generated `config.yml`; the example gives a general value plus environment-specific values. A Function receives one `context` object with trigger event data and Braintree metadata; environment, invocation UUID, and request UUID meanings are routed precisely. The separate JSON example instead uses `data` and `__meta.braintreeEnvironment`; the unexplained mismatch is preserved, not normalized into a schema. Source `:18-29`; raw `:24-36,41-66,69-81`.

## Position 23 — `docs-guides-paypal-commerce-channel-api-obtaining-an-access-token` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:812` → `wiki/concepts/braintree-payment-platform.md:31` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-commerce-channel-api-obtaining-an-access-token.md` → `raw/braintree/docs/guides/paypal-commerce-channel-api/obtaining-an-access-token-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is a fetched 2026-09-16, unversioned Braintree PayPal Commerce Channel API guide for a channel obtaining a retailer-authorized access token. It names no SDK/version; the request is sandbox-only. Account roles are channel and retailer, conditioned on retailer permission; objects are channel credentials, retailer domain, access token, and validity duration. It does not prove a production endpoint, current API/retailer eligibility, issued credentials, active grant, request success, order/payment, settlement, or funding. Source `:14,18-22`; raw `:16-20,22-52`.
2. **Purpose, action, conditions, detail route — PASS.** The channel posts its client ID/secret and onboarding-supplied retailer domain, caches the token, and fetches a new one after expiry produces HTTP 403. The displayed token and `3600` are examples, not credentials or a universal lifetime. Missing permission yields HTTP 400 on token request; after revocation, existing-token requests yield 403 and new-token requests yield 400, so refresh is not claimed to restore authorization. Source `:18-30`; raw `:19-52`.

## Position 24 — `docs-reference-response-payment-method-node` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:821` → `wiki/concepts/braintree-server-sdk.md:49` → `wiki/sources/braintree/source-braintree-docs-reference-response-payment-method-node.md` → `raw/braintree/docs/reference/response/payment-method/node-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is a fetched 2026-09-16, unversioned Braintree Node.js-routed response reference for generic returned Payment Method objects. It names no exact npm package/runtime/API version, environment, account eligibility, or enablement. Its actions are response consumption: inspect `paymentMethod.default` and runtime class; shown `customer.find`/`paymentMethod.find` calls are examples, not request-schema or execution contracts. No product availability or payment outcome follows. Source `:14,18-23,32-34`; raw `:14-42,47-95`.
2. **Purpose, action, conditions, detail route — PASS.** The page routes type-specific attributes to seven linked response-object families, checks customer-default status with `.default`, and illustrates `instanceof` for Credit Card, PayPal Account, Apple Pay Card, and Android Pay Card. It does not imply that all seven have class-check examples. The damaged `such as` sentence is explicitly preserved, so containing response families are not invented or exhaustively claimed. Source `:18-30`; raw `:16-28,47-95`.

## Query tally

| Page | Q1 exact scope | Q2 purpose/actions/conditions/detail route |
| --- | --- | --- |
| Network Tokens Value to Merchants | PASS | PASS |
| Functions Advanced Topics | PASS | PASS |
| Channel API Access Token | PASS | PASS |
| Payment Method Response (Node.js) | PASS | PASS |

No correction or supporting authority is required. **Verdict: PASS — 4/4 pages, 8/8 fixed questions.**

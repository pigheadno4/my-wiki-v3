# Braintree C43 fixed-query audit J — positions 37–40

- Campaign: `braintree-campaign-43`
- Mode: read-only independent query audit
- UTC start: `2026-10-07T11:39Z`
- UTC completion: `2026-10-07T11:46:28Z`
- Scope: manifest positions 37–40; exactly two fixed questions per page (8 total)
- Result: **8 PASS / 0 FAIL**

## Shared checks, bounded gap sweep, and extra authority

- **Manifest identity, pins, URLs, and primary ownership — PASS.** Manifest path/URL, source `raw_files`/`canonical_url`, and raw line-1 Source URL agree for all four pages. Recomputed SHA-256 values are: PINless test/go-live `e2862d97ed9a2e41578807db6259426d3f72e3934a31a85c5890fefb6df56970`; GraphQL integration-guide overview `dab36000a22d58108fb704ec9d2eef6130f07770ee918e255f7de94a6b61014c`; Google Pay JavaScript v3 testing/go-live `d479e5241c46f72c7fe27bb9d6759e1242f0d394ee1c934ef7c79cb99934b0bb`; Network Tokens how-it-works `f197e7702a96161839b31983e07dd903a2856a625274e172b4773de44461fb14`. Exact raw-path and canonical-URL lookup finds one primary source owner for each.
- **Full reads and reciprocal routes — PASS.** `CLAUDE.md`, `rules/query-and-synthesis.md`, C43 selection questions/manifest positions, root/provider entries, the two relevant concept sections, all four canonical sources, and all four pinned raws were read. Each actual route resolves root index → Braintree index → main concept → canonical source → exact raw; each source/main-concept pair links reciprocally.
- **One bounded gap sweep — PASS.** The filename/claim sweep found PINless eligibility/integration/workflow/authorization/code/reference siblings; the GraphQL landing, guides, and feature guides; Google Pay method/client/configuration/server/testing siblings; and Network Tokens overview/getting-started/value/BYOT siblings. None was needed as supporting authority for a retained claim or discovered conflict, so all remain unread navigation. No sibling, current-site, package/GitHub, direct-Google, Visa/Mastercard, card-network, or issuer behavior was transferred.
- **Captured-detail limits — PASS.** The PINless raw labels Java accessors/examples under JSON fences, the Google Pay sample has an unmatched extra closing parenthesis, the GraphQL examples are explicitly pared down, and the Network Tokens flow is carried partly in image alt text. The sources do not promise runnable code, complete schema, exact deployed behavior, or exhaustive implementation detail; precise procedures, values, fields, and examples remain at verified raw locators.
- **Deferred aggregate edges — PASS, not a content failure.** Direct provider/company catalog rows and the shared company/source-count close are coordinator-owned campaign-close work. Their current absence does not break the concept-mediated routes.

## Position 37 — `docs-guides-pinless-debit-optimized-debit-routing-test-and-go-live` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:760` → `wiki/concepts/braintree-payment-methods.md:28` → `wiki/sources/braintree/source-braintree-docs-guides-pinless-debit-optimized-debit-routing-test-and-go-live.md` → `raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/test-and-go-live-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is a 2026-09-16 capture of an unversioned Braintree PINless Debit Optimized Routing test/go-live page. It covers Sandbox enablement/testing and a transition recommendation toward live use, but identifies no SDK/package version and does not establish current availability, account eligibility/enablement, Production behavior, exact runtime behavior, or authorization, payment, settlement, or funding success. Evidence: source lines 12–21; raw lines 1–20.
2. **Central action, consequential conditions/warnings, and raw detail — PASS.** PINless debit is not automatically enabled in Sandbox; a Technical account manager must enable it. Test-card fixtures route among STAR, STAR_ACCESS, ACCEL, NYCE, or PULSE based on sale amount and merchant-account MCC. Separately enabled auto-retry may move an unsuccessful debit-network attempt to Visa/Mastercard; successful/failed retry fields differ, and Sandbox amount `2046` is an explicit negative case where both attempts fail. Exact cards, accessors, payloads, and retry fixture remain at raw lines 22–28, 29–78, and 80–82; source locators are lines 23–30.

## Position 38 — `graphql-integration-guides` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:759` → `wiki/concepts/braintree-payment-platform.md:28` → `wiki/sources/braintree/source-braintree-graphql-integration-guides.md` → `raw/braintree/graphql/integration_guides-2026-09-16.md`.

3. **Exact scope and non-inference — PASS.** This is a 2026-09-16 capture of an unversioned Braintree GraphQL integration-guide orientation page, not a language SDK, exact deployed schema, exhaustive feature inventory, or current availability/merchant/region/use-case eligibility authority. The browser API Explorer is explicitly Sandbox-scoped; neither it nor the page proves credentials, access, request execution, Production behavior, payment, settlement, or funding. Evidence: source lines 12–24; raw lines 1–27.
4. **Central action, consequential conditions/warnings, and raw detail — PASS.** The page explains that available feature guides aim at end-to-end context, require each guide's availability check, and intentionally omit example fields irrelevant to the use case. It routes exact field inventory to the schema reference and resolves a missing guide as either absent API functionality or unwritten guidance, with schema/changelog/support/SDK follow-ups. Exact decision paths remain at raw lines 30–38; source locators are lines 26–32. Linked targets remain unread navigation, not behavioral evidence.

## Position 39 — `docs-guides-google-pay-testing-go-live-javascript-v3` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:760` → `wiki/concepts/braintree-payment-methods.md:25` → `wiki/sources/braintree/source-braintree-docs-guides-google-pay-testing-go-live-javascript-v3.md` → `raw/braintree/docs/guides/google-pay/testing-go-live/javascript/v3-2026-09-16.md`.

5. **Exact scope and non-inference — PASS.** This is a 2026-09-16 Braintree website guide on the Google Pay JavaScript v3 testing/go-live route. It combines an Android-device end-user test prerequisite, Sandbox behavior, and Production configuration, but does not specify an exact `braintree-web` package, current browser list/support, merchant/buyer eligibility, account or merchant-account enablement, runtime correctness, payment success, settlement, or funding. Evidence: source lines 12–26; raw lines 1–28 and 31–71.
6. **Central action, consequential conditions/warnings, and raw detail — PASS.** Full Android-device flow testing needs a stored card/PayPal account or checkout-time method addition. Sandbox returns test nonces and has Google-Pay-versus-PayPal gateway display plus environment-qualified `payer_email` behavior. Production separately requires Control Panel activation, Google domain registration, a merchant ID, and possibly Braintree contact for a specific merchant account. The illustrative `PRODUCTION` request parses payment data and hands a nonce to the merchant server, but contains an unmatched `)` and is not copy-ready or execution proof. Exact UI steps, values, sample, and contact route remain at raw lines 31–71; source locators are lines 28–35.

## Position 40 — `docs-guides-network-tokens-how-it-works` — PASS / PASS

**Actual route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:760` → `wiki/concepts/braintree-payment-methods.md:23` → `wiki/sources/braintree/source-braintree-docs-guides-network-tokens-how-it-works.md` → `raw/braintree/docs/guides/network-tokens/how-it-works-2026-09-16.md`.

7. **Exact scope and non-inference — PASS.** This is a 2026-09-16 capture of an unversioned Braintree Network Tokens flow page. It assigns Braintree the Token Service Provider and Acquirer roles and describes merchant-Vault, card-network, and issuer interactions; it is not exact SDK/package/schema authority or proof of current availability, card/account eligibility, merchant enablement, provisioning success, transaction approval, settlement, or funding. Evidence: source lines 12–21; raw lines 1–22.
8. **Central action, consequential conditions/warnings, and raw detail — PASS.** Braintree sends a vaulted PAN for network-token provisioning and stores the merchant-specific returned token; payment sends that token with a one-time cryptogram for network token-to-PAN exchange and issuer processing. Issuer/card-network lifecycle updates can refresh Vault card details and may help avoid failure, without guaranteeing continuity. Network eligibility controls tokenization, a network may run a statement-visible but non-monetary `$0` verification, and Braintree does not control that decision. Exact flow and qualifications remain at raw lines 16, 18, 20, and 22; source locators are lines 23–28.

## Handoff

- Corrections requested: none.
- Content blockers: none.
- Closure follow-up: coordinator adds/checks direct provider/company source-catalog rows and shared source-count aggregates.
- Repository files modified: none. Audit artifact only: `/tmp/braintree-c43-query-audit-j.md`.

**Verdict: PASS — 4/4 pages and 8/8 fixed questions.**

# Braintree C44 fixed-query audit J — positions 37–40

- Campaign: `braintree-campaign-44`
- Mode: read-only independent query audit
- Scope: approved manifest positions 37–40; exactly two fixed questions per page (8 total)
- Completed UTC: `2026-10-07T13:00:03Z`
- Result: **PASS — 8/8 queries**

## Shared checks

- **Approval, pins and provenance — PASS.** All four jobs are `approved` at attempt 1. Recomputed SHA-256 values match the manifest: Amex testing/go-live `41adba00cf523f6517a29ef58a88815fbdb47a655ba448fd21dade212f338011`; Venmo testing/go-live `0a4ef17e03d8514c67289c21b3d27c1808a63f1e23d5925b67eb42939607a72b`; UnionPay server-side Node `f95e2953ed8c82d8f8a5fa9822f6d859421c50bfe6b2f98c7edd309cabea807c`; Network Tokenization Node `0408e6d64ec42768549774ea30a44633d3d0db7d8a488463d175c1940e306f30`. Manifest URL, source `canonical_url`, raw `Source URL`, `raw_files`, and `Raw Sources` agree; each raw records `Fetched: 2026-09-16` and `Discovery: llms.txt,sitemap.xml`.
- **PRIMARY ownership and reciprocal routing — PASS.** Exact raw-path and canonical-URL lookup finds one source owner for each primary; no source reuses another page's primary as supporting raw. Every route resolves `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md` → source → exact raw. The concept links the four sources at lines `29,31,33,64`, and the sources link back at lines `39,33,36,33`. Direct provider-catalog rows are deferred shared-close work, not failures while these concept routes work.
- **Full reads and one bounded gap sweep — PASS.** The four sources, four pinned raws, shared concept, and root/provider routes were read in full. One filename/claim sweep covered Amex Express Checkout/SRC, Venmo, UnionPay, and Network Tokens siblings. Only retained product-status conflicts required supporting authority: the Amex overview plus SRC source/raw, and the UnionPay payment-method source/raw, were read in full. They do not duplicate a primary. Other siblings remain unread navigation and contributed no behavior.
- **Captured-detail limits — PASS.** The Amex text has collapsed tag/parameter spacing, UnionPay has illustrative callback/Promise snippets, and the Network Tokenization table carries predicate-style labels plus a malformed `network_token` explanation. The source pages do not promise copy-ready syntax, exact package behavior, runtime compatibility, exhaustive schema, successful execution, or payment outcomes; precise fixtures, request shapes, and response labels stay at verified raw locators.

## Position 37 — `docs-guides-amex-express-checkout-testing-go-live` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md:33` → `wiki/sources/braintree/source-braintree-docs-guides-amex-express-checkout-testing-go-live.md` → `raw/braintree/docs/guides/amex-express-checkout/testing-go-live-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16, unversioned testing/go-live webpage for legacy Amex Express Checkout. Its JavaScript action is the `amex:init` `env` switch from Sandbox `qa` to `production`; its objects are a named test account, test nonce, and a qualified real American Express account test. It names no exact JavaScript SDK/package/version, account-enablement operation, acceptance criterion, current Amex/SRC availability, successful transaction, settlement, or funding. Source `:14,18-20,24-27`; primary raw `:17-18,21-40`.
2. **Purpose, action, conditions, warnings, detail route — PASS.** Sandbox uses `env=qa`, the listed account fixture or `fake-amex-express-checkout-nonce`; go-live changes the same environment to `production` and says to test a real account only if possible. The source prominently preserves the material conflict: the primary calls Amex replaced by limited-release SRC, the overview simultaneously calls Amex currently available under qualifications, and the SRC authority says support ended January 20, 2026 while still inviting limited-release access. Exact credentials and environment text remain at primary raw `:21-40`; conflict evidence is at overview raw `:17-35` and SRC raw `:14-15,21-48,88-90`.

## Position 38 — `docs-guides-venmo-testing-go-live` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md:64` → `wiki/sources/braintree/source-braintree-docs-guides-venmo-testing-go-live.md` → `raw/braintree/docs/guides/venmo/testing-go-live-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16, unversioned, product-level Venmo testing/go-live webpage. It names no platform, client/server SDK family, package, or version. Its environments are Sandbox and Production; its objects/actions are app-switch simulation, returned payment-method nonce, test user, connection-removal attempt, amount-selected test disputes, Production Control Panel setup, application, review, and approval-dependent enablement. It does not prove current eligibility, account enablement, a real Venmo purchase, dispute outcome, authorization, settlement, or funding. Source `:14,18-21`; raw `:17-38`.
2. **Purpose, action, conditions, warnings, detail route — PASS.** Sandbox is limited to app-switch testing: it uses Braintree branding, returns a nonce for `VenmoJoe`, does not reflect purchases in Venmo, and rejects Sandbox connection removal with HTTP 400. `fake-venmo-account-nonce` plus `62.00` or `62.01` creates the stated test-dispute statuses. Production requires separate Control Panel setup and an application; Braintree enables payments only upon approval. Exact fixtures and linked response routes remain at raw `:17-38`; unread links are correctly labeled navigation-only at source `:35-40`.

## Position 39 — `docs-guides-unionpay-server-side-node` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md:31` → `wiki/sources/braintree/source-braintree-docs-guides-unionpay-server-side-node.md` → `raw/braintree/docs/guides/unionpay/server-side/node-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16, unversioned Node.js-routed server-side webpage for the deprecated dedicated UnionPay flow. After client tokenization, the merchant server receives a payment-method nonce and device data and illustrates `gateway.transaction.sale()` with settlement submission. It names no exact Node package/version, environment, merchant/card eligibility, processing time, Vault behavior, or successful authorization, transaction, settlement, or funding. The Discover credit-card direction is a replacement route, not proof that either path executed. Source `:14-17,21-23`; raw `:17-25,26-60`.
2. **Purpose, action, conditions, warnings, detail route — PASS.** The central action is client-to-server nonce/device-data handoff into a sale request; callback and Promise branches are illustrative request/result handling, not a success guarantee. Separate delayed settlement is stated only for a UnionPay card that is not debit. The dedicated integration is deprecated, while the fully read product authority also calls its described setup limited release; applicability to the replacement versus legacy path remains unresolved. Exact examples and condition remain at primary raw `:21-67`; the supporting conflict is at `raw/braintree/articles/guides/payment-methods/unionpay-2026-09-16.md:17-27,61-63`.

## Position 40 — `docs-reference-general-network-tokenization-node` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md:29` → `wiki/sources/braintree/source-braintree-docs-reference-general-network-tokenization-node.md` → `raw/braintree/docs/reference/general/network-tokenization/node-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16 Node-routed, unversioned server response-field reference for Braintree-managed network tokenization of vaulted Visa and Mastercard credit cards. Its account condition is merchant-account eligibility confirmed through Customer Success; its objects are card-level tokenization state, transaction-level token use, and a token-details map. It names no exact Node SDK/package/version, Sandbox/Production environment, current account enablement, token availability, BYOT request behavior, Apple Pay response behavior, or successful token processing/payment outcome. Source `:14,18-20`; raw `:16-26`.
2. **Purpose, action, conditions, warnings, detail route — PASS.** A transaction qualifies for network-token processing only when the vaulted card has been tokenized, within the stated Visa/Mastercard scope. The captured table distinguishes `is_network_tokenized?` from `processed_with_network_token?` and names `network_token`, but its final explanation is malformed; the source correctly declines to infer keys, presence rules, schema, or runnable Node syntax. Exact captured labels and explanations remain at raw `:28-41`; source locators are `:24-29`.

## Query tally

| Page | Q1 exact scope | Q2 purpose/actions/conditions/detail route |
| --- | --- | --- |
| Amex Express Checkout — Testing and Go Live | PASS | PASS |
| Venmo — Testing and Go Live | PASS | PASS |
| UnionPay — Server-side Node | PASS | PASS |
| Network Tokenization Fields — Node | PASS | PASS |

No correction or additional supporting authority is required. **Verdict: PASS — 4/4 pages, 8/8 fixed questions.**

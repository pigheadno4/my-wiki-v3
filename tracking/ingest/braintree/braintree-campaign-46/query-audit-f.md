# Braintree C46 query audit F — positions 21–24

- UTC start: `2026-10-07T23:49:06Z`
- UTC analysis end: `2026-10-07T23:51:38Z`
- UTC handoff: `2026-10-07T23:51:43Z`
- Scope: manifest positions 21–24 only; eight predetermined questions; repository read-only.
- Result: **8/8 PASS**.

## Shared checks (performed once)

- Manifest pins, source frontmatter, raw source-URL comments, and live raw files agree for all four jobs. Recomputed SHA-256 values match the manifest exactly:
  - `docs-reference-request-apple-pay-register-domain-node`: `ee014945e74d5f9c4ea3ae0960af53058befedf81a7e3e15b02b93161cabc209`
  - `docs-reference-response-apple-pay-options-node`: `a864c40f35f22db04a9223fbe456c64805189cd67960880224e99e0755e3d7f8`
  - `docs-guides-samsung-pay-testing-go-live`: `0f0ebd2ed94fa5d995e12bbda0f8edd239111265278c556a550f1cad959930a6`
  - `docs-reference-response-transaction-level-fee-report-row-node`: `d579f3277099f0a461c6066293bfb67aeab6ac32f41bf3d79e4696af57995098`
- Provenance passes: every raw records its matching canonical URL at line 1, fetch date `2026-09-16` at line 2, `llms.txt,sitemap.xml` discovery at line 3, and matching title/slug metadata at lines 6–9.
- Unique primary ownership passes: each exact canonical URL and pinned `raw_files` entry occurs in one source page under `wiki/sources/`.
- Routing and reciprocity pass: `wiki/index.md:11` routes to `wiki/braintree-index.md`; the provider index routes to `[[braintree-payment-methods]]` at line 919, `[[braintree-apple-pay]]` at line 920, and `[[braintree-server-sdk]]` at line 927. Those concepts link to the exact sources at `wiki/concepts/braintree-apple-pay.md:30,32`, `wiki/concepts/braintree-payment-methods.md:31`, and `wiki/concepts/braintree-server-sdk.md:49`; each source links back to the same main concept. Direct provider-catalog rows are deferred to structural close, so their present absence is not a content failure.
- One bounded filename/topic gap sweep found the exact pins plus adjacent Apple Pay domain routes, Samsung Pay overview/server-side pages, and distinct Control Panel/Brazil transaction-level-fee-report articles. No older version of any exact pin was found. None of the neighbors was required for these exact-object answers, so no supporting raw was promoted or automatically full-read; linked configuration, PHP, Ruby, and Pay Later pages remain navigation-only.

## 21. `docs-reference-request-apple-pay-register-domain-node`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:920` → concept `wiki/concepts/braintree-apple-pay.md:32` → source `wiki/sources/braintree/source-braintree-docs-reference-request-apple-pay-register-domain-node.md` → pinned raw `raw/braintree/docs/reference/request/apple-pay/register-domain/node-2026-09-16.md`.

**Q1 — PASS.** Object/action: this is Braintree's unversioned Node-routed request-reference page for the named Apple Pay web action `Register Domain`. The body supplies no Node request object, method, request-body or response schema, example, environment, or account qualification; instead it says only the PHP and Ruby SDKs support API management of Apple Pay web domains in this snapshot. Do not infer Node support, exact package/version behavior, domain validation, current availability, merchant eligibility, successful registration, configuration completion, or payment execution. Locators: source lines 14, 18–23; raw lines 1, 6–9, 13, 16–17.

**Q2 — PASS.** Central purpose/action: preserve the register-domain action identity while exposing the decisive route/body availability mismatch. The material warning is the PHP/Ruby-only API-management statement; the linked JavaScript v3 Apple Pay configuration page is navigation only and contributes no behavior here. Exact action identity is at raw line 13, the SDK boundary at lines 16–17, and configuration navigation at lines 22–25. Locators: source lines 18–29, 31–39; raw lines 13, 16–17, 22–25.

## 22. `docs-reference-response-apple-pay-options-node`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:920` → concept `wiki/concepts/braintree-apple-pay.md:30` → source `wiki/sources/braintree/source-braintree-docs-reference-response-apple-pay-options-node.md` → pinned raw `raw/braintree/docs/reference/response/apple-pay-options/node-2026-09-16.md`.

**Q1 — PASS.** Object/action: this is Braintree's unversioned Node.js-routed `Apple Pay Options` response-reference stub. It documents no response object fields, constraints, invocation, return value, runtime action, environment, or account scope; its only substantive statement limits API-based Apple Pay web-domain management to PHP and Ruby SDKs. Do not infer a Node response contract, exact package/version behavior, native Apple Pay scope, current support, merchant eligibility, domain registration/configuration, or payment execution. Locators: source lines 14, 18–20; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose: identify the Apple Pay Options response route and preserve its narrow domain-management availability warning, not supply a response schema or operation. The warning must not be generalized beyond Apple Pay on the web via Braintree's API. Exact object identity is at raw line 14, the PHP/Ruby-only condition at lines 17–18, and the JavaScript v3 configuration destination at lines 21–24 remains unread navigation. Locators: source lines 18–26, 28–39; raw lines 14, 17–18, 21–24.

## 23. `docs-guides-samsung-pay-testing-go-live`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:31` → source `wiki/sources/braintree/source-braintree-docs-guides-samsung-pay-testing-go-live.md` → pinned raw `raw/braintree/docs/guides/samsung-pay/testing-go-live-2026-09-16.md`.

**Q1 — PASS.** Object/action: Braintree's unversioned Samsung Pay `Testing and Go Live` route contains no testing or go-live procedure. Its complete substantive body says Samsung Pay and the guide are deprecated and directs readers to the distinct Pay Later offers guide. No SDK/version, Sandbox/Production behavior, account scope, test object, or enablement action is stated. Do not infer technical equivalence, a migration procedure, current availability, merchant eligibility, configuration, or payment execution. Locators: source lines 14, 18–20; raw lines 6–9, 14, 16–18.

**Q2 — PASS.** Central purpose: preserve the Samsung Pay and guide deprecations plus the replacement-documentation direction. The material warning is that the Pay Later redirect is documentation navigation, not Samsung Pay equivalence or migration evidence; no fixtures, environment transition, or launch steps exist. Exact title is raw line 14, product deprecation line 16, and guide deprecation/redirect lines 17–18. Locators: source lines 18–26, 28–41; raw lines 14, 16–18.

## 24. `docs-reference-response-transaction-level-fee-report-row-node`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:927` → concept `wiki/concepts/braintree-server-sdk.md:49` → source `wiki/sources/braintree/source-braintree-docs-reference-response-transaction-level-fee-report-row-node.md` → pinned raw `raw/braintree/docs/reference/response/transaction-level-fee-report-row/node-2026-09-16.md`.

**Q1 — PASS.** Object/action: this is Braintree's unversioned Node.js-routed `Transaction Level Fee Report Row` response reference. The page names no request, returning action, report-generation operation, environment, exact Node package/version, fields, types, examples, or completeness semantics. Its only account scope is that the report is beta for US merchants. Do not infer report eligibility outside that statement, stable API behavior, fee assessment, settlement, funding, or reconciliation. Locators: source lines 14, 18–20, 26–28; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose: identify the response-object route and retain its availability warning. The material conditions are beta status, US-merchant scope, and an API subject to change; there is no row schema or action to import from the title. Exact object identity is at raw line 14 and the complete availability warning at lines 17–18. Locators: source lines 18–28, 30–37; raw lines 14, 17–18.

## Completeness pass

All four manifest jobs were covered in 1-based order with two direct questions per page. Every answer names the exact reached object/action, stays within fully read same-object pinned raw authority, retains material conditions and non-inferences, and supplies resolving locators. Hashes, canonical URLs, unique primary ownership, source/concept reciprocity, and root/provider routing pass; no neighboring page was substituted and catalog-row deferral was not misclassified. **Final: 8/8 PASS; no correction request.**

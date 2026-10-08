# Braintree C46 query audit I — positions 33–36

- UTC start: `2026-10-07T23:54:28Z`
- UTC analysis end: `2026-10-07T23:56:02Z`
- UTC handoff: `2026-10-07T23:56:05Z`
- Scope: manifest positions 33–36 only; eight predetermined questions; repository read-only.
- Result: **8/8 PASS**.

## Shared checks (performed once)

- Manifest pins, live raw files, source frontmatter, and raw source-URL comments agree for all four jobs. Recomputed SHA-256 values match the manifest exactly:
  - `docs-reference-response-transaction-line-item-node`: `dd9f5feac050b4a2d624187c13a6b9507e6e3ec5160759447f4bdc40c5fde2f0`
  - `docs-reference-response-customer-node`: `449fd65a5980408784dd61de4d550327e8fe744b51a7dcb1b65cea6bbe1a7e15`
  - `docs-guides-apple-pay-configuration-android-v5`: `5aca55e99aa2fe60642858d4b11cb45bc49fab1a61b1d54b08d8430f38429995`
  - `docs-guides-hosted-fields-faq-android-v5`: `ee6f65fd2f7c2f824fedd9ab5a4a3b4aeabd8b106303ae365bc6fae6a71720e6`
- Provenance passes: every raw records its matching canonical URL at line 1, fetch date `2026-09-16` at line 2, `llms.txt,sitemap.xml` discovery at line 3, and matching title/slug metadata at lines 6–9.
- Unique primary ownership passes: each exact canonical URL and pinned `raw_files` entry occurs in one source page under `wiki/sources/`; every source has a path-qualified `## Raw Sources` backlink.
- Routing and reciprocity pass: `wiki/index.md:11` routes to `wiki/braintree-index.md`; the provider index routes to `[[braintree-server-sdk]]` at line 927, `[[braintree-apple-pay]]` at line 920, and `[[braintree-android-sdk]]` at line 930. Those concepts link to the exact sources at `wiki/concepts/braintree-server-sdk.md:49,52`, `wiki/concepts/braintree-apple-pay.md:24`, and `wiki/concepts/braintree-android-sdk.md:76`; each source links back to its selected main concept at source lines 34, 34, 35, and 35 respectively. Direct provider-catalog rows are deferred to structural close by `dispatch-contract.md:9`, so their present absence is not a content failure.
- One bounded filename/topic gap sweep found the exact pins plus adjacent Transaction Line Item request, Customer request/guide, Apple Pay platform, and Hosted Fields route variants. No older version of any exact pinned raw was found. None of the neighbors was needed for these exact-object answers, so no supporting raw was retained or automatically full-read; linked policy, platform, FAQ, and next-page destinations remain navigation-only.

## 33. `docs-reference-response-transaction-line-item-node`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:927` → concept `wiki/concepts/braintree-server-sdk.md:52` → source `wiki/sources/braintree/source-braintree-docs-reference-response-transaction-line-item-node.md` → pinned raw `raw/braintree/docs/reference/response/transaction-line-item/node-2026-09-16.md`.

**Q1 — PASS.** Object/action: this is Braintree's unversioned Node.js-routed response-reference document for the `Transaction Line Item` object. It names no creating, retrieving, or returning action, exact `braintree` package/version, environment, account qualification, containing response, field schema, example, or object purpose beyond the title. Do not infer current object availability, complete result visibility, a successful API result, transaction creation, authorization, capture, settlement, or funding. Locators: source lines 14, 18–20, 29; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose: identify the sparse response-object route and retain its only substantive warning, that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. The policy destination was not captured, so the snapshot does not establish which fields or records are limited; the separately retained `find all` page is navigation only. Exact object identity is at raw line 14 and the complete policy note is at lines 17–18. Locators: source lines 14, 18–29, 35; raw lines 14, 17–18.

## 34. `docs-reference-response-customer-node`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:927` → concept `wiki/concepts/braintree-server-sdk.md:49` → source `wiki/sources/braintree/source-braintree-docs-reference-response-customer-node.md` → pinned raw `raw/braintree/docs/reference/response/customer/node-2026-09-16.md`.

**Q1 — PASS.** Object/action: this is Braintree's unversioned Node.js-routed `Customer` response-reference document. It names no create, find, update, delete, or returning action, exact `braintree` package/version, environment, merchant/account qualification, containing response, or property/schema inventory. Do not infer current result visibility, a complete Customer contract, successful retrieval, customer lifecycle behavior, or any payment outcome. Locators: source lines 14, 18–23; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose: identify the sparse Customer response route and retain its only substantive warning, that results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products policy. The linked policy and separate customer lifecycle/request pages remain unread navigation, so no limitation detail or operation is imported. Exact object identity is at raw line 14 and the complete policy note is at lines 17–18. Locators: source lines 14, 18–29, 35, 37–43; raw lines 14, 17–18.

## 35. `docs-guides-apple-pay-configuration-android-v5`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:920` → concept `wiki/concepts/braintree-apple-pay.md:24` → source `wiki/sources/braintree/source-braintree-docs-guides-apple-pay-configuration-android-v5.md` → pinned raw `raw/braintree/docs/guides/apple-pay/configuration/android/v5-2026-09-16.md`.

**Q1 — PASS.** Object/action: this Braintree website document is titled `Configuration` and is captured on an Apple Pay Android v5 route, but its body supplies no Android configuration action. It says Apple Pay is available only for linked iOS or JavaScript SDK v3 routes; those are documentation-family labels, not exact package versions. No environment, account, merchant, device, or card qualification is stated. Do not infer native Android Apple Pay support, current iOS/JavaScript availability, Sandbox or Production enablement, credentials, certificates, Merchant IDs, domain registration, client/server behavior, completed configuration, or payment execution. Locators: source lines 14, 18–23; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: preserve the Android-route/body availability mismatch and route readers to separately evidenced platform documentation. The material warning is that neither the `/android/v5` route nor the generic configuration title establishes Android behavior, while the iOS, JavaScript v3, and generic client-side destinations are navigation only. Exact route/title identity is at raw lines 1, 6–9 and 14; the complete availability statement is at lines 17–18; next-page navigation is line 22. Locators: source lines 14, 18–30, 37–43; raw lines 1, 6–9, 14, 17–18, 22.

## 36. `docs-guides-hosted-fields-faq-android-v5`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:930` → concept `wiki/concepts/braintree-android-sdk.md:76` → source `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-faq-android-v5.md` → pinned raw `raw/braintree/docs/guides/hosted-fields/faq/android/v5-2026-09-16.md`.

**Q1 — PASS.** Object/action: this Braintree website document is titled `Troubleshooting and FAQ` and is captured on a Hosted Fields Android v5 route, but its complete substantive body says Hosted Fields is available only for JavaScript. It contains no troubleshooting question, answer, Android API, setup procedure, exact Android/Web package version, environment, account, merchant, or payment action. Do not infer native Android Hosted Fields support, current availability, exact SDK behavior, merchant eligibility, tokenization, runtime rendering, or payment execution. Locators: source lines 14, 18–22; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: preserve the Android-route/JavaScript-only mismatch and direct further retrieval to the separate JavaScript FAQ or Examples destination. The material warning is that the route and FAQ title establish no Android troubleshooting authority; both linked destinations remain navigation only. Exact route/title identity is at raw lines 1, 6–9 and 14; the complete platform statement is at lines 17–18; next-page navigation is line 22. Locators: source lines 14, 18–30, 37–40; raw lines 1, 6–9, 14, 17–18, 22.

## Completeness pass

All four manifest jobs were covered in 1-based order with two direct questions per page. Every answer identifies the exact reached provider/document/product or SDK-family scope, environment/account evidence boundary, object/action, and non-inferences; central purpose, material warnings, and precise raw locators are retained. Hashes, URLs, provenance, unique ownership, root/provider routing, and source/concept reciprocity pass. No neighboring object or unread destination was substituted, no unnecessary support file was introduced, and direct-catalog deferral was not misclassified. **Final: 8/8 PASS; no correction request.**

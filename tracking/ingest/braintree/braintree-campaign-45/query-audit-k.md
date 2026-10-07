# Braintree C45 fixed-query audit K — positions 41–44

UTC start: `2026-10-07T14:12:51Z`
UTC analysis end: `2026-10-07T14:14:24Z`
UTC handoff: `2026-10-07T14:14:24Z`

Result: **8/8 PASS**. The evidence reached for every question answers the requested object/action, not a neighboring concept.

## Position 41 — `docs-reference-response-settlement-batch-summary-node`

Route: `wiki/index.md:7` → `wiki/braintree-index.md:874` → `wiki/concepts/braintree-server-sdk.md:49` → `wiki/sources/braintree/source-braintree-docs-reference-response-settlement-batch-summary-node.md:12-43` → `raw/braintree/docs/reference/response/settlement-batch-summary/node-2026-09-16.md:1-66`. Same-object supporting purpose authority: `wiki/sources/braintree/source-braintree-settlement-batch-summary-generate-node.md:12-46` → `raw/braintree/docs/reference/request/settlement-batch-summary/generate/node-2026-09-16.md:1-40`.

**Q1. What provider/document/product/SDK/version/environment/account/object/action scope is established, and what must not be inferred?**
**Answer:** This is an unversioned Braintree website response reference routed as Node.js. Its object is the Settlement Batch Summary response and its displayed action is calling `gateway.settlementBatchSummary.generate()` in callback or Promise form, then reading `result.settlementBatchSummary.records`. It names no exact Node package/version, runtime, environment, credentials, merchant-account eligibility, or current-support guarantee. The examples must not be promoted into parameter-requiredness, a complete response schema, successful execution for an account, transaction settlement, funding, or completed reconciliation. The request authority reached is the same Settlement Batch Summary generation object, not `transaction.submitForSettlement()`.
Locators: source lines 14, 18-20, 31-32; response raw lines 20-45; supporting request raw lines 13-17.
**PASS**

**Q2. What central purpose/action and consequential conditions/warnings are documented, and where are precise procedures/values/schema details retrievable in the pinned raw?**
**Answer:** The supporting request page says generation displays total sales and credits for each batch for a particular date and may group transactions by one custom field. The response raw shows callback and Promise access to `records`; its array is explicitly only an example. Incorrect request arguments may yield validation errors. Exact invocation values are at response raw lines 23-41, example record keys/values at lines 43-66, and purpose plus the validation route at supporting request raw lines 15-17 and 38-40. These are reporting examples, not proof that any transaction settled or funds moved.
**PASS**

## Position 42 — `docs-guides-pinless-debit-optimized-debit-routing-code-samples-sdk-ruby`

Route: `wiki/index.md:7` → `wiki/braintree-index.md:866` → `wiki/concepts/braintree-payment-methods.md:25` → `wiki/sources/braintree/source-braintree-docs-guides-pinless-debit-optimized-debit-routing-code-samples-sdk-ruby.md:12-42` → `raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/sdk/ruby-2026-09-16.md:1-39`.

**Q1. What provider/document/product/SDK/version/environment/account/object/action scope is established, and what must not be inferred?**
**Answer:** This is an unversioned Braintree website Ruby SDK sample for PINless Debit Optimized Debit Routing. The objects are a transaction response's routed `debit_network` and a transaction search; the actions are reading that response field and filtering search by debit network. It establishes no Ruby package/version, runtime, credentials, environment, merchant eligibility/enablement, client/server ownership, card or network-token behavior, or current support. It must not be treated as authorization, payment, settlement, funding, or returned-result proof.
Locators: source lines 14-16, 20-23; raw lines 14-24 and 26-38.
**PASS**

**Q2. What central purpose/action and consequential conditions/warnings are documented, and where are precise procedures/values/schema details retrievable in the pinned raw?**
**Answer:** For transactions routed on debit networks, the page says `debit_network` is populated during authorization and remains available for subsequent actions. The raw follow-on-action prose is damaged (`assubmit_for_settlementandvoid`), so exact method spelling or invocation must not be reconstructed from it. The prose says retrieval may use transaction ID or routed network, while the displayed Ruby search demonstrates only `search.debit_network.is "STAR"`; `STAR` and the loop are illustrative and guarantee neither routing nor matches. Exact field access is at raw lines 14-24 and the search/filter loop at lines 26-38.
**PASS**

## Position 43 — `docs-reference-client-api-jsonp`

Route: `wiki/index.md:7` → `wiki/braintree-index.md:865` → `wiki/concepts/braintree-payment-platform.md:28` → `wiki/sources/braintree/source-braintree-docs-reference-client-api-jsonp.md:12-43` → `raw/braintree/docs/reference/client-api/jsonp-2026-09-16.md:1-24`.

**Q1. What provider/document/product/SDK/version/environment/account/object/action scope is established, and what must not be inferred?**
**Answer:** This is a narrow, unversioned Braintree Client API website reference. Its object/action is invoking most ordinarily POST-based Client API methods through a JSONP GET using `_method=POST` and a named callback. It does not establish an exact Braintree Web or other SDK/version, browser requirements, authentication, environment, account/merchant enablement, real endpoint availability, callback-safety requirements, current JSONP support, server-side gateway processing, or payment success.
Locators: source lines 14, 18-24; raw lines 14-20.
**PASS**

**Q2. What central purpose/action and consequential conditions/warnings are documented, and where are precise procedures/values/schema details retrievable in the pinned raw?**
**Answer:** The page qualifies availability as **most**, not all, Client API methods. Its example GET carries `_method=POST` and `callback=myCallbackName`; the response invokes that callback with returned JSON and adds a `status` key corresponding to the HTTP status the non-JSONP request would have returned. Unsuccessful requests return an error response, but no error schema or handling contract is defined. Exact request shape is at raw lines 16-20 and callback/status/error behavior at lines 21-24.
**PASS**

## Position 44 — `docs-guides-hipercard-and-hiper-testing`

Route: `wiki/index.md:7` → `wiki/braintree-index.md:866` → `wiki/concepts/braintree-payment-methods.md:23` → `wiki/sources/braintree/source-braintree-docs-guides-hipercard-and-hiper-testing.md:12-38` → `raw/braintree/docs/guides/hipercard-and-hiper/testing-2026-09-16.md:1-28`.

**Q1. What provider/document/product/SDK/version/environment/account/object/action scope is established, and what must not be inferred?**
**Answer:** This is an unversioned Braintree guide for testing Hipercard and Hiper in the Sandbox. Its objects are one Hipercard credit-card fixture and one Hiper credit-card fixture; its action is testing an integration. The product condition is limited release for select merchants, with an access-request route. It identifies no client/server SDK or version and does not prove current support, account enablement, Production applicability, GitHub implementation/history, or a successful payment.
Locators: source lines 14, 18-22; raw lines 17-18 and 21-27.
**PASS**

**Q2. What central purpose/action and consequential conditions/warnings are documented, and where are precise procedures/values/schema details retrievable in the pinned raw?**
**Answer:** The page's purpose is to supply Sandbox test-card fixtures for Hipercard and Hiper. Consequential boundaries are the limited-release/select-merchant condition, request-access instruction, and Sandbox-only testing scope; a test input is not Production card data or payment-outcome evidence. The exact access condition is at raw lines 17-18 and both card values, types, and descriptions are at raw lines 21-27.
**PASS**

## Shared checks

- **Pins:** all four calculated SHA-256 values exactly match the manifest: `60bdbeebcad529c8013def0b3189f96dcf7d492ebcdfeec0ebd2d85bb6e26987`, `eb1316cf2b4c3af7c4d76c89592d689a4153160a0730f66d520a446c9792e096`, `fc5a31b71c78a797be87380670905693353e72a656289687071e8d7fee004043`, and `46b0e4b48f7a25eca7eb91e3b216b02c4966fd67f0f0e7ee1781a72e02c7166b`.
- **URL/provenance:** each raw line 1 matches its manifest/source `canonical_url`; each raw records `Fetched: 2026-09-16` and `Discovery: llms.txt,sitemap.xml` at lines 2-3. Each source `raw_files` entry and `Raw Sources` link resolves to the same pinned raw.
- **Single ownership:** repository-wide source searches found exactly one owner for each exact raw path and each exact canonical URL, always the manifest-named source target.
- **Reciprocity:** root links Braintree provider index; provider index links all three used Braintree main concepts; each main concept links the exact source; each source links back to its main concept and pinned raw. The settlement supporting concept also reciprocates. Exact C45 source rows are not yet in `wiki/braintree-index.md`; per the assignment this direct catalog-row close is deferred coordinator work, not a page failure.
- **Bounded filename/topic gap sweep:** settlement siblings were the Control Panel page and same-object generate request; only the generate request was needed and fully read. Optimized-routing, Client API, and Hipercard/Hiper filename siblings did not supply evidence needed for retained claims, so no unrelated/old raw was read. No additional ownership or object/action gap was found.

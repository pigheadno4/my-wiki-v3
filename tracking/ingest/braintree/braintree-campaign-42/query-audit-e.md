# Braintree C42 query audit — group E

- Campaign: `braintree-campaign-42`
- Manifest positions: 17–20
- Started (UTC): `2026-10-07T00:58:38Z`
- Completed (UTC): `2026-10-07T01:02:04Z`
- Verdict: **PASS — 8/8 questions passed; 4/4 pages have an actual root → provider index → main concept → source → pinned raw route.**

## Shared checks

- Read `CLAUDE.md`, `rules/query-and-synthesis.md`, the C42 manifest/selection, root index, relevant provider-index section, relevant main-concept sections, all four canonical source pages, and all four pinned raws in full. No sibling/current/GitHub/direct-PayPal page was used as behavioral authority.
- Manifest identity, exact target, canonical URL, and computed SHA-256 match for all four jobs (`manifest.json:161-194`). Computed hashes: recurring iOS `52a33727…f60f31`; migration JS `c9bde883…58fa5a1`; checkout iOS `2ac64a2e…41f70b5`; SEPA JS `4e942e49…9402365`.
- Each source frontmatter points to the one pinned raw and reproduces the manifest canonical URL. Each required main concept already contains a reciprocal source link: `paypal-braintree-integration.md:71,129`, `braintree-ios-sdk.md:85`, and `braintree-payment-methods.md:23`.
- The exact new source rows in `wiki/braintree-index.md` and the company aggregate are intentionally deferred to coordinator close. Their absence is recorded separately and is not a content failure because every tested source is currently reachable through its main concept.
- Bounded raw gaps do not prevent these answers: the recurring tables contain joined tokens (`recurring raw:80-85,204-209`) and the source flags that condition (`source:22,39`); the checkout Contact Module's read-only setting is blank in the capture (`checkout raw:111-115`), so no enum value is inferred; the SEPA callback initialization block is internally malformed (`SEPA raw:47-64`), while the captured Promise initialization is coherent (`SEPA raw:68-86`), so the callback sample is not represented as executable proof.
- Extra behavioral authority reads: none.

## 17. `docs-guides-paypal-recurring-payments-ios-v7`

Actual route: `wiki/index.md:5-11` → `wiki/braintree-index.md:722-729` → `wiki/concepts/paypal-braintree-integration.md:69-75` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-recurring-payments-ios-v7.md:12-58` → `raw/braintree/docs/guides/paypal/recurring-payments/ios/v7-2026-09-16.md:1-211`.

1. **PASS — exact scope and non-inference.** This is a collected Braintree PayPal recurring-payments website guide at the iOS v7 route, with the page's own client availability stated as iOS v6+. It covers a Braintree `BTPayPalVaultRequest` Billing Agreement and later Payment Token handoff. It does not establish a direct PayPal Orders/Vault API flow, a current package release, Sandbox/Production enablement, merchant eligibility, agreement creation, or later payment success. Evidence: source `14-17`; raw `1-10,17-25,55-59,143-197`.

2. **PASS — central action, conditions, warnings, and detail route.** The buyer approves a Billing Without Purchase agreement, the merchant retains its Payment Token, and later merchant-initiated requests use that token. Creation uses `plan_type`; later transactions use `transaction_source`; `plan_metadata` belongs at agreement creation; prepaid/postpaid classification and Account Manager enablement are required. Exact RBA mappings, disclosures, example request construction, and later-token route are retrievable at raw `69-105,123-145,148-209`; joined-token rendering is explicitly bounded by source `22,33-39` and is not normalized into invented values.

## 18. `docs-guides-paypal-paypal-sdk-migration-guide-javascript-v3`

Actual route: `wiki/index.md:5-11` → `wiki/braintree-index.md:722-729` → `wiki/concepts/paypal-braintree-integration.md:125-133` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-paypal-sdk-migration-guide-javascript-v3.md:12-58` → `raw/braintree/docs/guides/paypal/paypal-sdk-migration-guide/javascript/v3-2026-09-16.md:1-537`.

3. **PASS — exact scope and non-inference.** This is Braintree's JavaScript v3 custom-PayPal migration guide from PayPal `checkout.js` (page-labeled JS SDK v4) to PayPal JS SDK v5. It explicitly excludes Drop-in, Braintree JS v2, Android, iOS, and new PayPal web integrations. It is not a PayPal Web SDK v6 migration, direct-PayPal authority, current hosted/package support, or payment-success evidence. Evidence: source `14-16,26-27`; raw `17-32`.

4. **PASS — central action, conditions, warnings, and detail route.** The migration changes SDK loading, `paypal.Button.render` to `paypal.Buttons(...).render(...)`, `payment` to flow-specific `createOrder`/`createBillingAgreement`, and `onAuthorize` to `onApprove`, while continuing Braintree `createPayment` and `tokenizePayment`. Checkout/Vault must be selected at setup; Vault requires `vault: true` plus `createBillingAgreement`, and direct script loading uses environment-specific Control Panel client IDs. Exact callback/Promise and end-to-end examples are at raw `35-138,141-315,318-537`; source routes them at `32-45` without treating example values as guarantees.

## 19. `docs-guides-paypal-checkout-with-paypal-ios-v7`

Actual route: `wiki/index.md:5-11` → `wiki/braintree-index.md:715-720` → `wiki/concepts/braintree-ios-sdk.md:81-87` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-checkout-with-paypal-ios-v7.md:12-66` → `raw/braintree/docs/guides/paypal/checkout-with-paypal/ios/v7-2026-09-16.md:1-251`.

5. **PASS — exact scope and non-inference.** This is the captured Braintree iOS v7 website route for PayPal One-time Payments: create a required-amount `BTPayPalCheckoutRequest`, call `BTPayPalClient.tokenize`, and receive a tokenized PayPal account/nonce, error, or cancellation. The nonce is a client handoff, not authorization, capture, settlement, funding, current package behavior, merchant/buyer eligibility, or direct-PayPal evidence. Evidence: source `14-16,31-35`; raw `1-10,27-69`.

6. **PASS — central action, conditions, warnings, and detail route.** The central action is one-time checkout tokenization with optional Contact, Shipping, line-item, buyer-ID, user-action, and App Switch configuration. Preserve the captured March 30, 2026 mobile-certificate warning and iOS 6.17.0+ remediation; Contact Module is US-only; Continue applies when the final amount changes and allows at most one extra completion page; App Switch links to an unread iOS v6 guide and supplies no iOS v7 implementation authority. Exact options and navigation are at raw `17-20,71-249`; source detail locators are `37-51`.

## 20. `docs-guides-sepa-direct-debit-client-side-javascript-v3`

Actual route: `wiki/index.md:5-11` → `wiki/braintree-index.md:683-708` → `wiki/concepts/braintree-payment-methods.md:21-31` → `wiki/sources/braintree/source-braintree-docs-guides-sepa-direct-debit-client-side-javascript-v3.md:12-52` → `raw/braintree/docs/guides/sepa-direct-debit/client-side/javascript/v3-2026-09-16.md:1-464`.

7. **PASS — exact scope and non-inference.** This is a 2026-09-16 Braintree JavaScript v3 custom client-side SEPA Direct Debit guide for eligible, separately enabled merchants. It covers component setup, bank/customer-data collection, and nonce tokenization, plus a JS SDK 3.110.0+ redirect variant. It does not establish Drop-in support, current availability/package behavior, account enablement, mandate acceptance, debit success, settlement, funding, or server processing. Evidence: source `14-16,29-30`; raw `1-10,17-20,88-96,254-276`.

8. **PASS — central action, conditions, warnings, and detail route.** Initialize the SEPA component, collect account-holder/IBAN/customer fields, and tokenize on customer action; optionally configure same-page redirect return. Redirect use requires every domain registered through the Braintree Control Panel in both Sandbox and Production, rejects tokenization keys, and exposes nonce/payload fields only after successful tokenization. The raw's `success=true` wording is not elevated into final debit success. Exact domain rules, environment steps, redirect parameters, fields, and tokenization examples are at raw `99-251,254-463`; source routes and constrains them at `20-30,32-42`.

## Final result

**PASS: 8/8.** No affected-question correction and no expanded audit are required. The coordinator still owns the deferred source-catalog/company aggregate rows and close validation.

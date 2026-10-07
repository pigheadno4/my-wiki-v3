# Braintree C42 fixed-query audit — Group H

- Campaign: `braintree-campaign-42`
- Assigned manifest positions: 29–32
- Started (UTC): `2026-10-07T01:10:18Z`
- Completed (UTC): `2026-10-07T01:10:51Z`
- Verdict: **FAIL — 6/8 fixed questions passed; 2 narrow content corrections required**

## Shared checks

- **Pins, identity and ownership — PASS.** Recomputed SHA-256 values match the manifest for Level 2/3 required fields `ecee9095…be63`, SEPA testing/go-live `5a98841d…a81`, Amex Express Checkout `c4b240e6…c951`, and PayPal Android client-side `f882d502…ca8`. Each manifest URL equals the source frontmatter URL and raw Source URL, and every pinned raw has exactly one `raw_files` source owner.
- **Full reads and bounded authority — PASS.** All four canonical sources and pinned raws were read completely. Exact-path, URL and filename sweeps found the selected copies plus distinct Amex Android/iOS and PayPal iOS sibling routes; no sibling, current-provider, direct PayPal/Amex, GitHub/package, eligibility, execution, settlement, funding or interchange-result behavior was imported. The separately scoped Orchestration/Adyen raw only links the Level 2/3 page and was not used as authority. Related API/setup targets remain navigation because the selected raws answer the fixed questions. Extra factual authority raws read: none.
- **Navigation and reciprocity — PASS.** One actual root → Braintree index → main concept → source → pinned raw route is recorded for each page below, and every source/main-concept pair is reciprocal. Direct provider-index source rows and company/catalog aggregation are absent but remain the campaign-wide coordinator-close task; that deferred aggregate work is not a selected-page content failure.

## Position 29 — `docs-reference-general-level-2-and-3-processing-required-fields-node`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:715` → `wiki/concepts/braintree-server-sdk.md:49` → `wiki/sources/braintree/source-braintree-docs-reference-general-level-2-and-3-processing-required-fields-node.md:12-54` → `raw/braintree/docs/reference/general/level-2-and-3-processing/required-fields/node-2026-09-16.md:1-321`.

1. **PASS — Exact scope and non-inference.** This is an unversioned Braintree website Node.js reference for Level 2/3 transaction data supplied at sale or, with internal approval, settlement submission. It is not a complete deployed field contract, package-version/current-support statement, eligibility determination, lower-interchange result, gateway acceptance or payment-lifecycle proof. Source `:14,18-26`; raw `:17-30,56-106,232-240,317-321`.
2. **PASS — Central action, material conditions, warnings and detail route.** Level 3 depends on Level 2 plus additional data and line items; processor amount checks can decline discrepancies, and EU/UK non-zero shipping can be rejected with zero shipping tax. Settlement-time Level 2/3 data requires approval, overrides sale-time Level 2/3 data and should be used instead of supplying both. The source preserves blank required-field bullets, the missing Level 2 range subject, blank affected-character fields, naming-context differences and qualified validation-error scope. Exact fields, formula and examples remain at source `:30-39` and raw `:17-147,149-240,243-321`.

## Position 30 — `docs-guides-sepa-direct-debit-testing-go-live-node`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:707` → `wiki/concepts/braintree-payment-methods.md:25` → `wiki/sources/braintree/source-braintree-docs-guides-sepa-direct-debit-testing-go-live-node.md:12-59` → `raw/braintree/docs/guides/sepa-direct-debit/testing-go-live/node-2026-09-16.md:1-136`.

3. **PASS — Exact scope and non-inference.** This is Braintree's unversioned Node.js website route for mocked and linked-PayPal-account SEPA Direct Debit Sandbox testing plus a separate Production transition. It has no exact Node package version and does not prove current SEPA availability, merchant enablement, a live debit, settlement or funding. Source `:14`; raw `:16-45,87-135`.
4. **PASS — Central action, material conditions, warnings and detail route.** Mocked testing is default but not end-to-end and sends no PayPal Sandbox data; linked testing needs same-country business Sandbox/account-app setup under the same developer account, has no negative testing and can disable some fake nonces. The business account must not be the payer. Sandbox objects/settings/credentials do not transfer; Production requires separate server credentials/settings and limited low-value real-method sales followed through settlement to deposit, with actual debits and fees. Exact setup and server example remain at source `:18-23,35-43` and raw `:16-84,87-135`.

## Position 31 — `docs-guides-amex-express-checkout-client-side-javascript-v3`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:707` → `wiki/concepts/braintree-payment-methods.md:23` → `wiki/sources/braintree/source-braintree-docs-guides-amex-express-checkout-client-side-javascript-v3.md:12-57` → `raw/braintree/docs/guides/amex-express-checkout/client-side/javascript/v3-2026-09-16.md:1-142`.

5. **PASS — Exact scope and non-inference.** This is a 2026-09-16 Braintree website JavaScript v3 route for legacy Amex Express Checkout script/button setup, global nonce callback and optional cardmember-profile lookup. It preserves the replacement-by-SRC notice, SRC limited-release/eligibility/API-change/access qualifications and the page's linked JavaScript-v2 setup mismatch. It is not current Amex/SRC support, merchant access, package behavior, profile availability or payment-outcome proof. Source `:14-16,26-33`; raw `:16-22,58-71,96-120`.
6. **FAIL — Consequential captured-code defect is not disclosed.** The Promise profile example ends with a stray backtick inside the fenced JavaScript (`raw:84`), so the displayed snippet is not directly runnable as captured. The source calls it a Promise example and routes readers to `raw:69-85` (`source:23,42`) but does not warn that syntax repair is required. Add a bounded capture-quality warning; do not infer the corrected or current SDK form. The source otherwise retains callback ordering/incompleteness, nonce/server separation, missing-profile payload semantics, profile approval/availability qualifiers and precise detail locators (`source:20-24,32-46`; `raw:25-139`).

## Position 32 — `docs-guides-paypal-client-side-android-v5`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:718` → `wiki/concepts/braintree-android-sdk.md:74` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-client-side-android-v5.md:12-51` → `raw/braintree/docs/guides/paypal/client-side/android/v5-2026-09-16.md:1-228`.

7. **PASS — Exact scope and non-inference.** This is a 2026-09-16 Braintree Android v5-routed website guide for PayPal prerequisites, direct client initialization and SDK-managed XML/Compose buttons that tokenize a successful return to a nonce. Captured dependency examples are `paypal:5.8.0` and `ui-components:5.25.0`, not current compatibility evidence; the already-past March 30, 2026 certificate notice is retained only as dated wording. It is not standalone PayPal Android, a current package statement, eligibility or transaction-success proof. Source `:14-23`; raw `:17-93`.
8. **FAIL — Consequential XML/Fragment example defect is not disclosed.** The example declares and initializes `payPalButton` but assigns the launch callback through undeclared `paypalButton` (`raw:111-123`), so that callback wiring is not directly runnable as captured. The source describes the example's pending/failure and resumed result handling and routes readers to it (`source:24,35`) without identifying the case-sensitive identifier mismatch. Add a bounded warning that the captured snippet needs repair; do not infer the intended/current SDK form. Other prerequisites, nonce boundary, persistence/clearing comments, Compose-managed return distinction, branch outcomes and raw routes are accurately retained (`source:21-26,30-38`; `raw:25-215`).

## Close result

Positions 29 and 30 pass both fixed questions. Positions 31 and 32 each fail only the material-warning/detail question because a non-runnable captured example defect is not disclosed. Main-concept reciprocity is present now; provider/company source-catalog aggregation remains separate deferred close work. Repository files were not modified.

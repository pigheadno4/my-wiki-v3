# Braintree C46 query audit H — positions 29–32

- UTC start: `2026-10-07T23:53:26Z`
- UTC analysis end: `2026-10-07T23:54:26Z`
- UTC handoff: `2026-10-07T23:54:28Z`
- Scope: manifest positions 29–32 only; eight predetermined questions; repository read-only.
- Result: **8/8 PASS**.

## Shared checks (performed once)

- Manifest pins, source frontmatter, raw source-URL comments, and live raw files agree for all four jobs. Recomputed SHA-256 values match the manifest exactly:
  - `docs-guides-paypal-paypal-credit-ios-v7`: `668524805f6bc3b23b6d7c8bbd9a47eab34e18ea138f3d373989b2f197d256e9`
  - `docs-guides-samsung-pay-client-side-ios-v7`: `4de0935cf9496a8cba967628122ef847f5cb584426dc928641560c3057211621`
  - `docs-guides-samsung-pay-client-side-javascript-v3`: `53325f74f9614bd5af843278decea9ec6fdee6491f9d4d1d2515c77d44774068`
  - `docs-guides-samsung-pay-configuration`: `436ee0dcc4bb4d04a7a25c24470225742f6b0f1338b5fa7898f6b8387715d3ee`
- Provenance passes: each raw records its matching canonical URL at line 1, fetch date `2026-09-16` at line 2, `llms.txt,sitemap.xml` discovery at line 3, and matching title/slug metadata at lines 6–9.
- Unique primary ownership passes: each exact canonical URL and pinned `raw_files` entry occurs in one source page under `wiki/sources/`.
- Routing and reciprocity pass: `wiki/index.md:11` routes to `wiki/braintree-index.md`; the provider index routes to `[[braintree-payment-methods]]` at line 919 and `[[braintree-ios-sdk]]` at line 931. Those concepts link to the exact sources at `wiki/concepts/braintree-payment-methods.md:23,25,27` and `wiki/concepts/braintree-ios-sdk.md:83`; each source links back to its same main concept at source line 35, 36, 33, or 33 respectively. Direct provider-catalog rows are deferred to structural close, so their present absence is not a content failure.
- One bounded filename/topic gap sweep found the exact pins plus separate PayPal Credit article/Android, Samsung Pay article/overview/server-side/testing, and Pay Later destinations. No older version of an exact pin was found. None of those neighbors was needed to answer these exact-route notices, so no supporting raw was promoted or automatically full-read; linked replacement/next-page targets remain navigation only.

## 29. `docs-guides-paypal-paypal-credit-ios-v7`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:931` → concept `wiki/concepts/braintree-ios-sdk.md:83` → source `wiki/sources/braintree/source-braintree-docs-guides-paypal-paypal-credit-ios-v7.md` → pinned raw `raw/braintree/docs/guides/paypal/paypal-credit/ios/v7-2026-09-16.md`.

**Q1 — PASS.** Object/action: this is a Braintree-hosted PayPal Credit document selected at an iOS v7 route. Its entire substantive body is an availability notice saying PayPal Credit is unavailable in the captured literal `iOS v5v6v7 SDK` wording and directing readers to the Pay Later offers guide. It states no environment or account scope and supplies no setup, request object, method, code, handoff, or lifecycle action. Do not split the concatenated text into independently verified versions or infer current support, merchant/buyer eligibility, account enablement, financing approval, tokenization, server processing, replacement equivalence, migration behavior, or payment execution. Locators: source lines 14–23; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: preserve the selected iOS v7 route's narrow unavailability notice and its instruction to use separate Pay Later documentation. The material warning is that this sparse snapshot is navigation/availability evidence only; the unread replacement target contributes no behavior. Exact document/product identity is at raw line 14, the availability label at line 17, and the complete SDK wording plus redirect action at line 18. Locators: source lines 14–30, 37–43; raw lines 14, 17–18.

## 30. `docs-guides-samsung-pay-client-side-ios-v7`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:27` → source `wiki/sources/braintree/source-braintree-docs-guides-samsung-pay-client-side-ios-v7.md` → pinned raw `raw/braintree/docs/guides/samsung-pay/client-side/ios/v7-2026-09-16.md`.

**Q1 — PASS.** Object/action: this is Braintree's Samsung Pay client-side iOS v7 document route with the generic heading `Client-Side Implementation`. The body only deprecates Samsung Pay and the guide and directs readers to the distinct Pay Later offers guide. It states no environment or account scope and contains no native request/response object, tokenization, nonce handoff, client/server flow, or payment action. Do not infer Pay Later equivalence, a migration procedure, current availability, merchant/buyer eligibility, account enablement, exact SDK/package behavior, GitHub implementation, or payment execution. Locators: source lines 14, 18–24; raw lines 1, 6–9, 14, 16–18.

**Q2 — PASS.** Central purpose/action: preserve the exact iOS v7 route identity while exposing that the reached authority is a deprecation/redirect notice, not an implementation guide. The material conditions are separate product and guide deprecations; the Pay Later target is unread navigation only. Exact heading is raw line 14, product deprecation line 16, and the `IMPORTANT` guide deprecation/redirect at lines 17–18. Locators: source lines 14–24, 26–42; raw lines 14, 16–18.

## 31. `docs-guides-samsung-pay-client-side-javascript-v3`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:25` → source `wiki/sources/braintree/source-braintree-docs-guides-samsung-pay-client-side-javascript-v3.md` → pinned raw `raw/braintree/docs/guides/samsung-pay/client-side/javascript/v3-2026-09-16.md`.

**Q1 — PASS.** Object/action: this is Braintree's Samsung Pay client-side JavaScript v3 document route, also headed `Client-Side Implementation`. Its complete body deprecates Samsung Pay and the guide and directs readers to Pay Later offers documentation. It states no environment or account scope and supplies no client initialization, request/response object, tokenization, nonce handoff, authorization, capture, or settlement action. Do not infer replacement equivalence, migration behavior, current availability, merchant enablement, exact package/GitHub behavior, or payment execution. Locators: source lines 14, 18–21; raw lines 1, 6–9, 14, 16–18.

**Q2 — PASS.** Central purpose/action: identify the exact JavaScript v3 route and retain its deprecation plus documentation redirect, rather than manufacture a client integration. The material warning is that the Pay Later route is a distinct destination and provides no Samsung Pay lifecycle evidence here. Exact route/title are at raw lines 6–7 and 14, Samsung Pay deprecation at line 16, and guide deprecation/redirect at lines 17–18. Locators: source lines 14–28, 30–38; raw lines 6–7, 14, 16–18.

## 32. `docs-guides-samsung-pay-configuration`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:23` → source `wiki/sources/braintree/source-braintree-docs-guides-samsung-pay-configuration.md` → pinned raw `raw/braintree/docs/guides/samsung-pay/configuration-2026-09-16.md`.

**Q1 — PASS.** Object/action: this is Braintree's unversioned Samsung Pay `Configuration` document route. Its body contains no configuration action; it deprecates Samsung Pay and the guide, directs readers to Pay Later offers documentation, and exposes a JavaScript v3 Client-side next-page link. No SDK version, environment, account scope, fields, prerequisites, request/response object, client/server flow, or payment lifecycle is stated. Do not infer replacement equivalence, migration steps, present availability, merchant eligibility, provider configuration, client behavior, or payment execution. Locators: source lines 14, 18–21; raw lines 1, 6–9, 14, 16–20.

**Q2 — PASS.** Central purpose/action: preserve the unversioned configuration-route identity while warning that its reached authority is only a product/guide deprecation and documentation redirect. The material conditions are the two distinct deprecations; both the Pay Later destination and JavaScript v3 next-page target remain navigation only. Exact heading is raw line 14, Samsung Pay deprecation line 16, guide deprecation/redirect lines 17–18, and next-page link line 20. Locators: source lines 14–28, 35–44; raw lines 14, 16–20.

## Completeness pass

All four manifest jobs were covered in 1-based order with two direct questions per page. Every answer names the exact reached document/product/SDK-version route or unversioned route, identifies absent environment/account/object/action scope, stays within fully read same-object pinned raw authority, retains material conditions and non-inferences, and supplies resolving locators. Hashes, canonical URLs, unique primary ownership, source/concept reciprocity, and root/provider routing pass; no neighboring page was substituted and catalog-row deferral was not misclassified. **Final: 8/8 PASS; no correction request.**

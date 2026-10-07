# Braintree C43 fixed-query audit — Group B

- Campaign: `braintree-campaign-43`
- Assigned manifest positions: 5–8
- Started (UTC): `2026-10-07T11:11:37Z`
- Completed (UTC): `2026-10-07T11:13:56Z`
- Verdict: **PASS — 8/8 fixed questions passed**

## Shared checks

- The four manifest pins match the raw files read in full: Contact Us `e6930177886a4d3933368b87de295d04a4d4ce5a5be510dabd252b00540faefb`; Testing Your Integration `8ef2f46ec4eb0f81a91a35b2dbefda4eb38b6d026d7d430d4009e95f12162560`; Verifone E285 `4cff691ab80c77887fc3b2572b836ce049c50c185337f5f6151318a4c6f1e60d`; Getting Product Information `e680c9f07b9da94cc98ec87acec31556ab580750630cb7b4e8f09d2338162a43`.
- For every page, the manifest canonical URL equals source-frontmatter `canonical_url` and the raw line-1 Source URL; each canonical source owns the pinned raw in `raw_files` and links it under `## Raw Sources`.
- The common route begins at `wiki/index.md:11` (`[[braintree-index]]`). Provider-to-main-concept links are present at `wiki/braintree-index.md:738,759`; all four selected source/main-concept pairs are reciprocal now (`wiki/concepts/braintree-in-person.md:14,16,18`; `wiki/concepts/braintree-payment-platform.md:28`).
- The bounded filename sweep found only the four assigned dated raws. Related-raw sections and cross-references were inspected once; none was needed because each pinned raw fully answers its two fixed questions. No current-page, sibling-page, GitHub, direct-PayPal, Verifone, or navigation-only authority was transferred into the answers.
- Provider-index direct source rows and the company/provider source catalog are deferred coordinator-close work, separate from content failure. The stray quote in the testing page's illustrative amount sentence and compacted product-property rendering are nonblocking raw presentation defects: neither source asserts a false claim or runnable guarantee.

## Position 5 — `in-person-post-launch-activities-contact-us`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:738` → `wiki/concepts/braintree-in-person.md:18` → `wiki/sources/braintree/source-braintree-in-person-post-launch-activities-contact-us.md:1-47` → `raw/braintree/in-person/post-launch-activities/contact-us-2026-09-16.md:1-116`.

1. **PASS — Exact scope and non-inference.** This is a collected, unversioned Braintree In-Person website support-routing page for hardware or integration issues in Sandbox or Production. It establishes issue-specific contact and diagnostic routes, not current service availability, an SLA or resolution time, account eligibility, reader state, or any transaction, authorization, payment, settlement, or funding outcome. Evidence: source `:12-22`; raw `:14-26,87-112`.
2. **PASS — Central action, conditions, warnings, and raw-detail route.** The central action is to open a Braintree Help Desk ticket and choose **In-Person Payment Support**, with a Customer Success Manager as a routing aid. Requested evidence is issue-dependent: hardware identity/behavior/reproduction/network/environment versus API request identity/time, available raw exchange, reader/API behavior, errors, reproduction, public gateway ID and environment. Sandbox troubleshooting routes to the integration team; urgent Production-hardware escalation remains ticket-first and only covers replacement or troubleshooting. New-hardware and onboarding selections remain separate. Exact checklists and routes are retrievable at source `:24-33` and raw `:19-112`.

## Position 6 — `in-person-guides-testing-your-integration`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:738` → `wiki/concepts/braintree-in-person.md:16` → `wiki/sources/braintree/source-braintree-in-person-guides-testing-your-integration.md:1-57` → `raw/braintree/in-person/guides/testing-your-integration-2026-09-16.md:1-60`.

3. **PASS — Exact scope and non-inference.** This is a collected, unversioned Braintree In-Person guide limited expressly to Sandbox end-to-end integration testing; no SDK or API version is established. It does not prove current product or reader availability, account/hardware eligibility, physical device behavior, Production readiness, or an actual payment, settlement, or funding outcome. Evidence: source `:12-22,24-30`; raw `:14-31`.
4. **PASS — Central action, material conditions/warnings, and raw-detail route.** The guide recommends testing from POS UI through reader API calls and test-card payment to Control Panel inspection, including unhappy paths. Sandbox and Production are entirely separate, nothing transfers, and credentials/merchant identifiers differ. Exact amounts simulate documented context/payment statuses; linked decline-code values can be used as request amounts to simulate processor responses. Digital wallets cannot be tested on Braintree dev-kit readers in Sandbox, and the readiness questionnaire plus suggested engineering review is not certification. The exact matrix, simulation sentence and checklist remain at source `:32-39` and raw `:34-60`.

## Position 7 — `in-person-hardware-verifone-e285`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:738` → `wiki/concepts/braintree-in-person.md:14` → `wiki/sources/braintree/source-braintree-in-person-hardware-verifone-e285.md:1-52` → `raw/braintree/in-person/hardware/verifone-e285-2026-09-16.md:1-103`.

5. **PASS — Exact scope and non-inference.** This is a collected, unversioned Braintree In-Person website hardware overview for the Verifone E285 only; no SDK version is established. It is not GitHub implementation evidence and does not establish current procurement or device availability, merchant/account eligibility, certification, pairing, reader-online state, Production readiness, payment-method enablement, or payment success, and it cannot be generalized to other readers. Evidence: source `:12-26`; raw `:14-45`.
6. **PASS — Central purpose/action, conditions, warnings, and raw-detail route.** The page retrieves the E285's mobile/WiFi/touchscreen positioning, kit, captured hardware specifications, entry modes, 2.4 GHz security modes, and idle-screen customization. Customization is reader-, location-, or gateway-account-scoped; the image must meet the documented file constraints, identifiers go to a PayPal Solutions or Integration Engineer, and configuration is said to refresh within 12 hours or on reboot, with post-go-live updates routed to hardware support. Exact values and procedure remain at source `:28-37` and raw `:19-101`.

## Position 8 — `docs-guides-paypal-commerce-channel-api-getting-product-information`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:759` → `wiki/concepts/braintree-payment-platform.md:28` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-commerce-channel-api-getting-product-information.md:1-39` → `raw/braintree/docs/guides/paypal-commerce-channel-api/getting-product-information-2026-09-16.md:1-153`.

7. **PASS — Exact scope and non-inference.** This is a collected, unversioned Braintree website guide for retrieving a retailer's products through the PayPal Commerce Channel API after obtaining a retailer-specific access token; its request example targets the Braintree Sandbox Commerce endpoint. It establishes no exact SDK/API version, current API availability, merchant/channel eligibility, Production enablement, inventory or price assurance, order success, fulfillment, settlement, or funding. Evidence: source `:12-21`; raw `:14-35,145-153`.
8. **PASS — Central action, material conditions/warnings, and raw-detail route.** The page documents product searches by SKU, product URL, combined name/description text, or name, returning products with variants and unique SKUs; no match yields an empty collection. The caller tracks product `in_stock` and variant `sku`, passes the chosen variant SKU into ordering, may cache results only for a few minutes, and can use `web_buy_link` as a hosted-purchase alternative. The statement that ordering obtains up-to-date product information for full cost is documented guidance, not a freshness, availability, purchase, fulfillment, settlement, or funding guarantee. Exact query syntax, Sandbox request and response example remain at source `:23-29` and raw `:16-153`.

## Close result

No affected-question correction or extra authority read is required. All four pages preserve their exact website/product/environment scope, central retrieval purpose, consequential local conditions and warnings, raw-detail route, reciprocal main-concept navigation, and non-inference boundaries.

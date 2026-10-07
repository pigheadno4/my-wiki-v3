# Braintree C45 fixed-query audit L — positions 45–48

- Audit start (UTC): `2026-10-07T14:16:34Z`
- Analysis end (UTC): `2026-10-07T14:17:13Z`
- Handoff (UTC): `2026-10-07T14:18:57Z`
- Scope: four fixed C45 jobs, eight predetermined questions; repository read-only.

## Shared checks (once)

**PASS.** `[[index]]` routes to `[[braintree-index]]`; the provider index now contains all four exact C45 source rows and also routes to `[[braintree-ios-sdk]]` and `[[braintree-payment-methods]]`; each applicable concept links to the exact source, and each source links back to its concept and to its factual raw file.

The four actual SHA-256 values exactly match the manifest pins: `a0048674…b4b9`, `b44d348c…98fc7`, `734e6c0d…a2e27`, and `dfe119ce…3b4a`. For every page, the manifest canonical URL equals the source frontmatter URL and the raw `Source URL`; the manifest raw path equals source `raw_files` and `Raw Sources`. Each raw path and each canonical URL has exactly one owner under `wiki/sources/`. The retained SRC conflict support was read in full through `[[source-braintree-payment-methods-secure-remote-commerce]]` and its factual raw; it is used only for the same SRC support-status warning, not as Masterpass implementation evidence.

The single bounded filename/topic sweep covered PayPal Commerce iOS examples/overview/setup/product cards, Masterpass client/overview/server routes, SRC, and Samsung Pay overview/server routes. It found expected adjacent navigation pages; no additional page was needed to answer the requested objects/actions. Unread Samsung Pay API-reference links and adjacent Masterpass/PayPal Commerce pages remain navigation, not evidence.

## Position 45 — `docs-guides-paypal-commerce-ios-examples`

**Route:** `[[index]]` → `[[braintree-index]]` → `[[braintree-ios-sdk]]` → `[[source-braintree-docs-guides-paypal-commerce-ios-examples]]` → `[[raw/braintree/docs/guides/paypal-commerce-ios/examples-2026-09-16]]`.

**Q1 — PASS. Requested object/action:** scope the Braintree-hosted PayPal Commerce iOS examples document and what its examples illustrate. It is an unversioned PayPal Commerce SDK examples page for iOS: the object is a store-purchase illustration plus three linked example-project directories, and the action is to show standalone, modal, and parent-controlled tab-bar store placements. No execution environment or merchant/account scope is stated. Do not infer current repository contents, buildability, modern modular `braintree-ios` behavior, SDK support, runtime results, or a completed purchase/payment from the images or links. **Locators:** raw frontmatter/title lines 1, 6–9, 14; `Store purchase flow` lines 17–19; `Example projects` and product/action descriptions lines 20–25.

**Q2 — PASS. Requested object/action:** identify the page's central illustration/routing purpose and its material limits. The page shows five linked purchase-flow images (Products, Product Detail, Product Features, Purchase Confirmation, Receipt) and directs readers to `Shop`, `ModalShop`, and `TabBarShop`, respectively described as standalone, modal, and parent-controlled tab-bar examples. The page states no requirements, eligibility, version, environment, account conditions, or success guarantee; precise project links and presentation descriptions are retrievable at the pinned raw rather than imported from neighboring setup/overview pages. **Locators:** raw lines 17–19 and 20–25.

## Position 46 — `docs-guides-masterpass-client-side-android-v5`

**Route:** `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-masterpass-client-side-android-v5]]` → `[[raw/braintree/docs/guides/masterpass/client-side/android/v5-2026-09-16]]`; same-successor support check: `[[source-braintree-payment-methods-secure-remote-commerce]]` → `[[raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16]]`.

**Q1 — PASS. Requested object/action:** scope the Masterpass client-side Android v5 route and the action it actually documents. The route is Braintree documentation labelled Android v5, but its body is only a Masterpass-to-SRC availability/migration notice: former Masterpass users are directed to integrate with SRC and request access. The notice says SRC was introduced in Android v2, iOS v4, and JavaScript v3; that history does not establish an Android v5 implementation. No environment is stated; account scope is only eligible merchants in a limited release. Do not infer Android setup, dependency/API/package behavior, tokenization, nonce handoff, transaction execution, current SRC support, enablement, or successful migration. **Locators:** raw route/title lines 1, 6–9, 14; replacement and requested action lines 17–22; navigation-only server-side link line 26.

**Q2 — PASS. Requested object/action:** state the migration direction and consequential qualifications/warnings for that same Masterpass/SRC object. Central action: integrate with SRC and contact Braintree for access. Material conditions: SRC is limited release for eligible merchants and its API is subject to change. Material warning: the separately retained SRC authority says Click to Pay/SRC would be unsupported effective January 20, 2026 and later attempts receive `Payment method not supported` with decline risk, while also retaining current-tense limited-release wording; present support and a safe executable migration path therefore remain unresolved. No precise Android procedure exists on this page. **Locators:** primary raw lines 17–22 and 26; supporting SRC raw lines 14–15, 21–25, 28–48, and 88–90.

## Position 47 — `docs-guides-masterpass-client-side-ios-v7`

**Route:** `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-masterpass-client-side-ios-v7]]` → `[[raw/braintree/docs/guides/masterpass/client-side/ios/v7-2026-09-16]]`; same-successor support check: `[[source-braintree-payment-methods-secure-remote-commerce]]` → `[[raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16]]`.

**Q1 — PASS. Requested object/action:** scope the Masterpass client-side iOS v7 route and the action present in its retained body. This is a Braintree iOS v7-routed document, but its only substantive content is the Masterpass-to-SRC availability notice directing prior Masterpass users to SRC and to request access. The iOS v7 route is not proof of an iOS v7 procedure; the notice's iOS v4 introduction statement is historical SRC generation context, not exact-package behavior. No environment is stated; account scope is limited-release eligible merchants. Do not infer client/server behavior, SDK calls, tokenization, payment lifecycle, current support, eligibility for a particular merchant, or successful migration/payment. **Locators:** raw route/title lines 1, 6–9, 14; complete availability notice line 18.

**Q2 — PASS. Requested object/action:** state the migration direction and consequential qualifications/warnings for the same Masterpass/SRC object. Central action: prior Masterpass users should integrate with SRC and contact Braintree for access. Material conditions: eligible-merchants-only limited release and API subject to change. The same retained SRC authority creates the consequential unresolved support conflict: January 20, 2026 end-of-support/error wording coexists with current-tense limited-release/access wording. The pinned iOS page contains no procedure or schema details beyond its route metadata and notice. **Locators:** primary raw lines 17–18; supporting SRC raw lines 14–15, 21–25, 28–48, and 88–90.

## Position 48 — `docs-guides-samsung-pay-server-side-node`

**Route:** `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-samsung-pay-server-side-node]]` → `[[raw/braintree/docs/guides/samsung-pay/server-side/node-2026-09-16]]`.

**Q1 — PASS. Requested object/action:** scope the Braintree Samsung Pay server-side Node route and the actions its retained body actually names. The document is Node.js-routed and server-side, but it marks Samsung Pay and the guide deprecated, redirects to the distinct Pay Later offers guide, and lists only places a payment method could be stored. It states no exact Node package/version, environment, merchant/account eligibility, or client collection behavior. Do not infer GraphQL behavior, Android/client behavior, Pay Later technical equivalence, exact runnable Node syntax, current Samsung Pay support, or successful vaulting, payment, settlement, or funding. **Locators:** raw route/title lines 1, 6–9, 14; GraphQL navigation line 18; deprecation/redirect lines 20–22; storage contexts lines 25–27.

**Q2 — PASS. Requested object/action:** identify the guide's central deprecation/storage direction and where exact routine values are retrievable. The primary warning is to stop treating this as a current Samsung Pay guide and use the Pay Later offers guide instead; that redirect does not prove equivalent behavior or provide a migration. The remaining action-oriented list names payment-method create, customer create/update, or transaction sale with `options.store_in_vault` / `options.store_in_vault_on_success`. Because the captured links render as `linkToReferenceRequest` placeholders and no Node code is present, those are request-context and option-name locators, not verified request schemas. The four related API-reference raws remain unread navigation targets, as the source explicitly records. **Locators:** primary raw lines 20–22 and 25–27; GraphQL navigation line 18.

## Result

**8/8 questions PASS; 4/4 pages PASS.** No correction or recheck is required. The coordinator-completed direct C45 provider-index rows are present.

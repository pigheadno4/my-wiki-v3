# Braintree C46 query audit J — positions 37–40

- UTC start: `2026-10-07T23:55:21Z`
- UTC analysis end: `2026-10-07T23:56:21Z`
- UTC handoff: `2026-10-07T23:56:50Z`
- Scope: manifest positions 37–40 only; eight fixed questions; repository read-only.
- Result: **8/8 PASS**.

## Shared checks (performed once)

- Manifest pins, source frontmatter, raw source-URL comments, and live raw files agree for all four jobs. Recomputed SHA-256 values match the manifest exactly:
  - `docs-guides-hosted-fields-setup-and-integration-android-v5`: `ce61ccbe5c6af602caee4fe1f7bfc8e09bc55d1be34d6c610709b6ca1691594e`
  - `docs-guides-hosted-fields-events-android-v5`: `96c45f879a5fddd85cf2e83cd513df1c46777c8ea3a0b838db17c6fec3191305`
  - `docs-guides-hosted-fields-faq-ios-v7`: `a9d67ad467db9fa88a64276e1e4ee97aea60f1844c91fae6ac8a3b9caf0475b2`
  - `docs-guides-hosted-fields-setup-and-integration-ios-v7`: `f88a33414003fe11f564401f78d49b7339f8463f4eb34a64185694a01b1d84d8`
- Provenance passes: every raw records its matching canonical URL at line 1, fetch date `2026-09-16` at line 2, `llms.txt,sitemap.xml` discovery at line 3, and matching title/slug metadata at lines 6–9.
- Unique primary ownership passes: each exact canonical URL and pinned `raw_files` entry occurs in one source page under `wiki/sources/`.
- Routing and reciprocity pass: `wiki/index.md:11` routes to `wiki/braintree-index.md`; the provider index routes to `[[braintree-web-sdk]]` at line 928, `[[braintree-android-sdk]]` at line 930, and `[[braintree-ios-sdk]]` at line 931. Those concepts link to the exact sources at `wiki/concepts/braintree-web-sdk.md:80`, `wiki/concepts/braintree-android-sdk.md:74`, and `wiki/concepts/braintree-ios-sdk.md:83,85`; each source links back to its same main concept. Direct provider-catalog rows are deferred to structural close, so their present absence is not a content failure.
- One bounded filename/topic gap sweep found the exact pins plus sibling Android/iOS/JavaScript Events and FAQ routes. No older version of any exact pin was found. The siblings were not required for these exact route/body answers, so no supporting raw was promoted or automatically full-read; linked JavaScript and next-page targets remain navigation-only.

## 37. `docs-guides-hosted-fields-setup-and-integration-android-v5`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:928` → concept `wiki/concepts/braintree-web-sdk.md:80` → source `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-setup-and-integration-android-v5.md` → pinned raw `raw/braintree/docs/guides/hosted-fields/setup-and-integration/android/v5-2026-09-16.md`.

**Q1 — PASS.** Scope/object/action: this is Braintree's Hosted Fields `Setup and Integration` document at the Android v5 route. Its body provides no Android setup action, dependency, API, field configuration, tokenization, server handoff, environment, account condition, or exact package behavior; it only says Hosted Fields is available for JavaScript and links a separate JavaScript v3 route. Do not infer Android support, current JavaScript availability, native or hosted-runtime behavior, merchant eligibility, PCI scope, successful setup, or payment execution. Locators: source lines 14, 18–22; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: preserve the Android v5 route while directing implementation retrieval to the separately authoritative JavaScript guide. The material warning is the route/body platform mismatch; `Next Page: Styling` is unread navigation and contributes no behavior here. Exact document identity is at raw line 14, the complete availability statement at lines 17–18, and next-page navigation at line 22. Locators: source lines 14, 18–28, 35–42; raw lines 14, 17–18, 22.

## 38. `docs-guides-hosted-fields-events-android-v5`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:930` → concept `wiki/concepts/braintree-android-sdk.md:74` → source `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-events-android-v5.md` → pinned raw `raw/braintree/docs/guides/hosted-fields/events/android/v5-2026-09-16.md`.

**Q1 — PASS.** Scope/object/action: this is Braintree's Hosted Fields `Events` document at the Android v5 route. It names no Android event, listener API, payload, sequence, prerequisite, environment, account scope, exact package behavior, client/server lifecycle, or result; its only substantive statement says Hosted Fields is available only for JavaScript and links the JavaScript events route. Do not infer Android Hosted Fields support, event-model parity, current JavaScript availability, merchant eligibility, runtime behavior, or payment execution. Locators: source lines 14–16, 20–28; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: retain the Android v5 route/body mismatch and route readers to the separate JavaScript Hosted Fields events authority. The JavaScript events target and `Next Page: Troubleshooting and FAQ` are navigation only, not imported event evidence. Exact document identity is at raw line 14, the complete availability statement at lines 17–18, and next-page navigation at line 22. Locators: source lines 20–35, 37–50; raw lines 14, 17–18, 22.

## 39. `docs-guides-hosted-fields-faq-ios-v7`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:931` → concept `wiki/concepts/braintree-ios-sdk.md:85` → source `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-faq-ios-v7.md` → pinned raw `raw/braintree/docs/guides/hosted-fields/faq/ios/v7-2026-09-16.md`.

**Q1 — PASS.** Scope/object/action: this is Braintree's `Troubleshooting and FAQ` document at a Hosted Fields iOS v7 route. It contains no FAQ question, remedy, native SDK call, client/server flow, tokenization result, prerequisite, environment, account scope, or lifecycle action; the complete body only says Hosted Fields is available for JavaScript. Do not infer iOS Hosted Fields support, current JavaScript availability, exact SDK or GitHub behavior, merchant eligibility, successful troubleshooting, runtime rendering, or payment execution. Locators: source lines 14, 18–23; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: preserve the iOS v7 FAQ route as platform-scope navigation and direct readers to the separate JavaScript FAQ authority. The material condition is the route/body mismatch; the linked JavaScript page is unread navigation and contributes no FAQ behavior here. Exact document identity is at raw line 14 and the complete availability statement at lines 17–18. Locators: source lines 14, 18–30, 32–43; raw lines 14, 17–18.

## 40. `docs-guides-hosted-fields-setup-and-integration-ios-v7`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:931` → concept `wiki/concepts/braintree-ios-sdk.md:83` → source `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-setup-and-integration-ios-v7.md` → pinned raw `raw/braintree/docs/guides/hosted-fields/setup-and-integration/ios/v7-2026-09-16.md`.

**Q1 — PASS.** Scope/object/action: this is Braintree's Hosted Fields `Setup and Integration` document at the iOS v7 route. It provides no integration procedure, prerequisite, native SDK call, request/response field, client/server flow, tokenization result, environment, account scope, or lifecycle action; its only substantive text says Hosted Fields is available for JavaScript. Do not infer iOS Hosted Fields support, current JavaScript availability, exact SDK or GitHub behavior, merchant eligibility, successful setup, runtime rendering, or payment execution. Locators: source lines 14, 18–23; raw lines 1, 6–9, 14, 16–17.

**Q2 — PASS.** Central purpose/action: preserve the iOS v7 setup route as platform-scope navigation and direct implementation retrieval to the separate JavaScript setup guide. The material warning is the route/body mismatch; the linked JavaScript page is unread navigation and supplies no setup behavior here. Exact document identity is at raw line 14 and the complete availability statement at lines 16–17. Locators: source lines 14, 18–30, 32–43; raw lines 14, 16–17.

## Completeness pass

All four manifest jobs were covered in 1-based order with two direct questions per page. Every answer names the exact reached route/document action, stays within fully read same-object pinned raw authority, retains the platform-mismatch warning and non-inferences, and supplies resolving locators. Hashes, canonical URLs, provenance, unique primary ownership, source/concept reciprocity, and root/provider routing pass; no sibling page was substituted and catalog-row deferral was not misclassified. **Final: 8/8 PASS; no correction request.**

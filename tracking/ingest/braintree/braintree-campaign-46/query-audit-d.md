# Braintree C46 query audit D — positions 13–16

- Result: **PASS — 8/8 fixed-question answers pass; 4/4 page routes pass shared checks.**
- Audit role: query group D, repository read-only.
- UTC start: `2026-10-07T23:46:00Z`
- UTC analysis end: `2026-10-07T23:47:40Z`
- UTC handoff: `2026-10-07T23:47:53Z`

## Shared checks (performed once)

- **PASS — manifest pins and hashes.** Positions 13–16 each have a unique manifest `raw_path`, `canonical_url`, and `source_target`; the full pinned raws hash exactly to `10afab4b7d283a5c743d5678aa263581c57f5d45f489e657dd23d4b5febd6021`, `e4d4b96c826b02be3253dd659c574d1bb7d514cc5d9edca8b5b6eca0cf45a56a`, `9171b15604827cab1f3fd3631a303594f3b0f329b0e565e6b0238b18d2a51390`, and `76e9d8f17580c969fdc5c6df9b4d0615189b5339ba069185c06b8f39e6d6cb2c`, respectively.
- **PASS — URL/provenance and unique primary ownership.** Each raw `Source URL` equals its manifest and source-frontmatter canonical URL; each source `raw_files` value points to the pinned raw; repository source-owner counts are exactly one by raw path and exactly one by canonical URL for every page.
- **PASS — root/provider/main-concept route and reciprocity.** `wiki/index.md:11` routes to `[[braintree-index]]`; `wiki/braintree-index.md:919,927-928,937` routes to all four selected concepts. Source-to-concept and concept-to-source links are reciprocal at: dispute source `:34` ↔ `wiki/concepts/disputes.md:335`; Elo source `:32` ↔ `wiki/concepts/braintree-payment-methods.md:31`; Google Pay Card source `:30` ↔ `wiki/concepts/braintree-server-sdk.md:53`; Shopper Insights source `:30` ↔ `wiki/concepts/braintree-web-sdk.md:80`.
- **PASS — bounded filename/topic gap sweep.** Related dispute request/guide, Elo family, Android Pay Card, and Shopper Insights mobile raws exist, but none is needed to support the deliberately narrow retained claims. They remain navigation/supporting candidates, not imported evidence. No older/full-raw expansion was performed.
- **Deferred close, not a failure.** The four direct source catalog rows are not yet in `wiki/braintree-index.md`; the execution contract explicitly defers catalog aggregation to close.

## Position 13 — `docs-reference-response-dispute-node`

Route: `[[index]]` → `[[braintree-index]]` → `[[disputes]]` → `[[source-braintree-docs-reference-response-dispute-node]]` → `raw/braintree/docs/reference/response/dispute/node-2026-09-16.md`.

1. **PASS — scope and non-inferences.** Braintree website, Dispute **response-reference** document on a Node.js route; no exact Node package/version or environment is stated. The reached object/action authority is the Dispute response object plus an account qualification for API dispute management: only merchants with dispute access in the Braintree Control Panel. It does not enumerate response fields or authorize inference of find/search/accept/evidence/finalize behavior, current merchant access, successful execution, lifecycle transition, bank review, settlement, or outcome. Locators: pinned raw `:1,7,14,21-22`; source `:14,18-23`.
2. **PASS — purpose, conditions/warnings, retrieval.** The captured page's complete purpose is sparse response-reference orientation. Material warnings are the PayPal Data Protection Addendum-based result limitation and the Control Panel access condition. Precise retrievable details are the heading at raw `:14`, limitation at `:17-18`, and availability at `:21-22`; no schema/procedure/value exists in this capture. Source detail locators correctly point to source `:25-29`.

## Position 14 — `docs-guides-elo-client-side-ios-v7`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-elo-client-side-ios-v7]]` → `raw/braintree/docs/guides/elo/client-side/ios/v7-2026-09-16.md`.

1. **PASS — scope and non-inferences.** Braintree Elo client-side guide route labeled iOS v7, but the body establishes only an availability notice for select merchants using page-relative “latest” JavaScript v3 and server SDKs. No environment is named. The reached action is requesting limited-release access, not native iOS implementation. Do not infer iOS SDK behavior, an exact JavaScript/server package version, current availability, account enablement, or payment execution. Locators: pinned raw `:1,7,14,17-18`; source `:14,18-22`.
2. **PASS — purpose, conditions/warnings, retrieval.** Central purpose/action: communicate Elo limited-release eligibility and direct a qualifying merchant to contact Braintree to request access. Material conditions are select-merchant status and use of the latest JavaScript v3 plus server SDKs; “latest” is relative, not package-qualified. All precise content is at raw `:17-18`; there is no iOS procedure/schema/value to retrieve. Source locators are accurate at source `:24-27`.

## Position 15 — `docs-reference-response-google-pay-card-node`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-server-sdk]]` → `[[source-braintree-docs-reference-response-google-pay-card-node]]` → `raw/braintree/docs/reference/response/google-pay-card/node-2026-09-16.md`.

1. **PASS — scope and non-inferences.** Braintree Google Pay Card **response-reference availability stub** on a Node.js route. No environment, merchant/account condition, or exact Node package/version is stated. The reached object/action is response naming/navigation: consult `AndroidPayCard`; Google Pay cards are represented as Android Pay cards in the API to avoid breaking changes, except Ruby SDK 3.0.1+. Do not infer a Node request contract, complete response schema, current capability, transaction/authorization/capture/settlement/funding, or any other payment outcome. Locators: pinned raw `:1,7,14,17-18`; source `:14,18-20`.
2. **PASS — purpose, conditions/warnings, retrieval.** Central purpose/action: redirect readers to the legacy-named Android Pay Card response reference and explain compatibility naming. The consequential warning is the Ruby SDK `3.0.1`-and-higher exception, so the Android Pay representation is not universal. The exact redirect, rationale, and exception are all retrievable at raw `:18`; no local field schema or procedure is present. Source locators correctly identify source `:22-25`.

## Position 16 — `docs-guides-shopper-insights-javascript-v3`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-web-sdk]]` → `[[source-braintree-docs-guides-shopper-insights-javascript-v3]]` → `raw/braintree/docs/guides/shopper-insights/javascript/v3-2026-09-16.md`.

1. **PASS — scope and non-inferences.** Braintree Shopper Insights (Beta) page on a JavaScript v3 route, but its body establishes a platform availability/exclusion notice only: merchants using iOS v6+ or Android v4+ are included; JavaScript and Drop-in merchants are excluded. No environment or specific account enablement is stated. The reached action is no implementation action. Do not infer JavaScript/Drop-in support, setup, exact package behavior, recommendation/analytics behavior, customer-session or consent flow, current availability/eligibility, or payment execution. Locators: pinned raw `:1,7,14,17-18`; source `:14,18-19`.
2. **PASS — purpose, conditions/warnings, retrieval.** Central purpose is to preserve the beta availability boundary and the JavaScript/Drop-in exclusion. The exact mobile generation thresholds and exclusions are retrievable at raw `:17-18`; the beta identity is at `:14`. The capture contains no procedure, values beyond those version thresholds, schema, events, or lifecycle details. Source detail locators accurately point to source `:21-25`.

## Audit disposition

No content correction or supporting-raw promotion is required for positions 13–16. All eight answers remain PASS; the only open structural action is the already-deferred close-time provider catalog aggregation.

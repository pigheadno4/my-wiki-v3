# Braintree C46 query audit K — positions 41–44

- UTC start: `2026-10-07T23:57:08Z`
- UTC analysis end: `2026-10-07T23:58:21Z`
- UTC handoff: `2026-10-07T23:58:32Z`
- Scope: manifest positions 41–44 only; eight fixed questions; repository read-only.
- Result: **8/8 PASS**.

## Shared checks (performed once)

- Manifest pins, source frontmatter, raw source-URL comments, and live raw files agree for all four jobs. Recomputed SHA-256 values match the manifest exactly:
  - `docs-guides-hosted-fields-events-ios-v7`: `877209c189741c64edf32e00cf69ee50d43c78478d9d66b15b5430aedd555060`
  - `docs-guides-hosted-fields-examples-ios-v7`: `d7e2b43f77751b9532d78c1e50871980d1a0479e31c1fe4481cdff439a2cd969`
  - `docs-guides-hosted-fields-styling-ios-v7`: `83e1135e36824f6b015f90a4eb08eb81ba35c456ad8d73f9e6e8e69f501b1390`
  - `docs-guides-hosted-fields-examples-android-v5`: `7d8288fe98cfa12228cbcd02c638e6f57ab81efa2e066744555ad42203f41145`
- Provenance passes: every raw records its matching canonical URL at line 1, fetch date `2026-09-16` at line 2, `llms.txt,sitemap.xml` discovery at line 3, and route/title metadata at lines 6–9. Manifest-wide `raw_path`, `canonical_url`, and `source_target` values are unique; each selected URL and `raw_files` value has exactly one owner under `wiki/sources/`.
- Routing and reciprocity pass: `wiki/index.md:11` routes to `wiki/braintree-index.md`; that provider index routes to `[[braintree-web-sdk]]` at line 976, `[[braintree-android-sdk]]` at line 978, and `[[braintree-ios-sdk]]` at line 979. The exact source/concept pairs are reciprocal at `wiki/concepts/braintree-ios-sdk.md:83,85`, `wiki/concepts/braintree-web-sdk.md:80`, and `wiki/concepts/braintree-android-sdk.md:77`, with source backlinks at source lines 34–36. Coordinator-owned direct catalog rows now appear at `wiki/braintree-index.md:61-64` and `wiki/companies/braintree.md:60-63`; this close-stage aggregation is not source evidence or a source change, and catalog-row deferral is not a content failure.
- One bounded filename/topic gap sweep found the four exact pins plus sibling Android/iOS/JavaScript Events, Examples, and Styling routes. No older version of an exact pin was found. The siblings are not needed for these exact route/body answers, so no supporting raw was promoted or automatically full-read; linked JavaScript targets remain navigation-only.

## 41. `docs-guides-hosted-fields-events-ios-v7`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:979` → concept `wiki/concepts/braintree-ios-sdk.md:85` → source `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-events-ios-v7.md` → pinned raw `raw/braintree/docs/guides/hosted-fields/events/ios/v7-2026-09-16.md`.

**Q1 — PASS.** Provider/document/product/SDK/version/environment/account/object/action scope: this is Braintree's Hosted Fields `Events` document at an iOS v7 route. The route does not state an exact native package version, environment, or account qualification, and the complete body supplies no event object, listener, payload, callback, state, prerequisite, client/server flow, tokenization, or lifecycle action. Its reached authority only says Hosted Fields is available for JavaScript and links the separate JavaScript v3 events route. Do not infer native iOS Hosted Fields support, event parity, current JavaScript availability, exact SDK/GitHub behavior, merchant eligibility, runtime event delivery, or payment execution. Locators: source lines 14, 18–23; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: preserve the iOS v7 Events route/body mismatch and direct event-detail retrieval to the separate JavaScript authority. The material warning is that the iOS path/title is navigation context, not native-event evidence; the linked JavaScript page remains unread navigation. Exact route identity is at raw lines 1 and 7, the heading at line 14, and the complete availability statement at lines 17–18. Locators: source lines 25–40; raw lines 1, 7, 14, 17–18.

## 42. `docs-guides-hosted-fields-examples-ios-v7`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:979` → concept `wiki/concepts/braintree-ios-sdk.md:83` → source `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-examples-ios-v7.md` → pinned raw `raw/braintree/docs/guides/hosted-fields/examples/ios/v7-2026-09-16.md`.

**Q1 — PASS.** Provider/document/product/SDK/version/environment/account/object/action scope: this is Braintree's Hosted Fields `Examples` document at an iOS v7 route. It names no exact native package version, environment, account scope, example object, configuration, SDK call, setup step, client/server handoff, tokenization result, or payment action; its only substantive statement says Hosted Fields is available for JavaScript and links the JavaScript v3 examples route. Do not infer native iOS support or examples, current JavaScript availability, exact SDK/repository behavior, merchant eligibility, runtime rendering, or successful payment execution. Locators: source lines 14, 18–24; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: retain the iOS v7 examples route as platform-scope navigation and direct example retrieval to the separate JavaScript guide. The material warning is that the route and generic `Examples` heading establish no native example; the linked target contributes no behavior until independently read. Exact route/title identity is at raw lines 1, 6–7, and 14, and the full availability statement is at lines 17–18. Locators: source lines 26–39; raw lines 1, 6–7, 14, 17–18.

## 43. `docs-guides-hosted-fields-styling-ios-v7`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:976` → concept `wiki/concepts/braintree-web-sdk.md:80` → source `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-styling-ios-v7.md` → pinned raw `raw/braintree/docs/guides/hosted-fields/styling/ios/v7-2026-09-16.md`.

**Q1 — PASS.** Provider/document/product/SDK/version/environment/account/object/action scope: this is Braintree's Hosted Fields `Styling` document at an iOS v7 route, while its body points only to JavaScript and the JavaScript v3 styling destination. It states no exact package version, environment, account qualification, native styling object, property, CSS rule, configuration action, platform prerequisite, client/server flow, or runtime result. Do not infer native iOS styling, current JavaScript support, exact SDK lifecycle or repository behavior, merchant enablement, runtime rendering, tokenization, or payment execution. Locators: source lines 14, 18–23; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: preserve the iOS route/body mismatch and route styling retrieval to the separately authoritative JavaScript v3 page. The consequential warning is that the iOS path and generic Styling title do not establish native styling, while the linked target is navigation only. Exact route identity is at raw lines 1 and 7, the heading at line 14, and the sole availability/destination statement at lines 17–18. Locators: source lines 25–38; raw lines 1, 7, 14, 17–18.

## 44. `docs-guides-hosted-fields-examples-android-v5`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:978` → concept `wiki/concepts/braintree-android-sdk.md:77` → source `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-examples-android-v5.md` → pinned raw `raw/braintree/docs/guides/hosted-fields/examples/android/v5-2026-09-16.md`.

**Q1 — PASS.** Provider/document/product/SDK/version/environment/account/object/action scope: this is Braintree's Hosted Fields `Examples` document at an Android v5 route. It states no exact Android package version, environment, account scope, example object, code, UI behavior, dependency, SDK call, client/server flow, tokenization result, or payment action; its complete substantive body only says Hosted Fields is available for JavaScript and links the separate JavaScript examples route. Do not infer native Android Hosted Fields support or examples, current JavaScript availability, exact SDK/package behavior, merchant eligibility, runtime rendering, or payment execution. Locators: source lines 14, 18–22; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: preserve the Android v5 route/body mismatch and direct example retrieval to the separate JavaScript authority. The material warning is that neither the Android route nor `Examples` heading establishes Android behavior, and the linked JavaScript page remains navigation only. Exact route identity is at raw lines 1 and 7, the heading at line 14, and the complete availability statement at lines 17–18. Locators: source lines 24–38; raw lines 1, 7, 14, 17–18.

## Completeness pass

All four manifest jobs were covered once in 1-based order with two direct answers per page. Every answer names the exact provider/document/product/route scope, matches its object/action to the fully read reached authority, retains environment/account/version absences and material non-inferences, and supplies resolving source/raw locators. Hashes, URLs, provenance, unique ownership, source/concept reciprocity, and root/provider routing pass; no sibling or supporting page was substituted, and close-owned catalog aggregation was not misclassified as source evidence or a content failure. **Final: 8/8 PASS; no correction request.**

# Braintree C46 query audit A — positions 1–4

- UTC start: `2026-10-07T23:35:44Z`
- UTC analysis end: `2026-10-07T23:37:16Z`
- UTC handoff: `2026-10-07T23:37:16Z`
- Scope: manifest positions 1–4 only; eight predetermined questions; repository read-only.
- Result: **8/8 PASS**.

## Shared checks (performed once)

- Manifest pins, live raw files, source frontmatter, and raw source-URL comments agree for all four jobs. Recomputed SHA-256 values match the manifest exactly:
  - `docs-guides-elo-overview`: `226ee9cd26d8ba3ff4b4989492bd927d3192c5ec3023815a0485e0509155c455`
  - `docs-guides-pinless-debit-optimized-debit-routing-transaction-workflow`: `91fe237d541b1c67b2e7ebffafee28e214b51849fa8266f89063ef4ae70be86d`
  - `docs-guides-samsung-pay-overview`: `56548f8edab74ad13c9c399ee0e6ce9d4a1b59ce1da9c6683f47fbaefc909264`
  - `docs-guides-hosted-fields-upgrading-from-custom-ios-v7`: `b14ae90d337ebabffff1121df358c34a4cb9b191cf53009a21d70286e02c8a2d`
- Identity and provenance pass: each raw records the matching canonical source URL at line 1, fetch date `2026-09-16` at line 2, `llms.txt,sitemap.xml` discovery at line 3, and matching title/slug metadata at lines 6–9.
- Single ownership passes: each exact canonical URL and each pinned raw path occurs in exactly one file under `wiki/sources/`.
- Discoverability and reciprocity pass: `wiki/index.md:11` routes to `wiki/braintree-index.md`; the provider index routes to `[[braintree-payment-methods]]` at line 919 and `[[braintree-ios-sdk]]` at line 931; the selected concept links to each exact source, and every source links back to that same concept. Direct provider-catalog rows are deferred to structural close and their present absence is not a content failure.
- One bounded filename-gap sweep found only the four manifest-pinned raws. No older raw or unrelated authority was opened automatically. No additional support file was required because every retained answer below is established by its same-object pinned raw; related pages remain navigation-only.

## 1. `docs-guides-elo-overview`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:29` → source `wiki/sources/braintree/source-braintree-docs-guides-elo-overview.md` → pinned raw `raw/braintree/docs/guides/elo/overview-2026-09-16.md`.

**Q1 — PASS.** Object/action: Braintree's unversioned Elo overview identifies Elo as a commonly accepted payment method in Brazil and says Braintree SDKs enable merchants to accept Elo cards like other credit cards. Access is limited release for select merchants using the page-relative latest JavaScript v3 and server SDKs, with a contact route to request access. Do not infer an exact package version, current availability, account/environment enablement, card or transaction eligibility, GitHub implementation, or authorization/settlement/funding success. Locators: source lines 14, 18–22; raw lines 17–21.

**Q2 — PASS.** Central purpose: identify Elo and its restricted access boundary, not provide an integration procedure. Material conditions are limited release, select-merchant access, the stated SDK families, and an access request. Precise retained details are at raw `AVAILABILITY` lines 17–18 and `# Overview` lines 20–21; the pinned raw contains no client/server procedure. Locators: source lines 18–27; raw lines 17–21.

## 2. `docs-guides-pinless-debit-optimized-debit-routing-transaction-workflow`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:27` → source `wiki/sources/braintree/source-braintree-docs-guides-pinless-debit-optimized-debit-routing-transaction-workflow.md` → pinned raw `raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/transaction-workflow-2026-09-16.md`.

**Q1 — PASS.** Object/action: Braintree's unversioned PINless Debit Optimized Routing workflow checks transaction eligibility; an ineligible transaction goes through Visa or Mastercard. For a refund of a sale originally sent over a PINless debit network, Braintree sends the refund on that same network and, only if unsuccessful, automatically retries the refund through Visa/Mastercard. Do not infer the eligibility criteria, account enablement, exact network selection, API/SDK instructions, client/server duties, environment behavior, or any individual transaction outcome; the retry rule is not for initial sales, successful refunds, or other transaction types. Locators: source lines 14, 18–21; raw lines 14–21.

**Q2 — PASS.** Central purpose: document the initial ineligibility fallback and the same-network sale-refund sequence. The material warning is that automatic retry applies to an unsuccessful refund after same-network routing. Precise workflow text is at raw line 16 and refund/retry text at raw line 21; the diagram asset is raw line 18. Locators: source lines 23–27; raw lines 16, 18, 21.

## 3. `docs-guides-samsung-pay-overview`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:25` → source `wiki/sources/braintree/source-braintree-docs-guides-samsung-pay-overview.md` → pinned raw `raw/braintree/docs/guides/samsung-pay/overview-2026-09-16.md`.

**Q1 — PASS.** Object/action: Braintree's unversioned Samsung Pay overview is a lifecycle notice saying Samsung Pay and its guide are deprecated and directing readers to the distinct Pay Later offers guide. Do not infer technical equivalence, a migration procedure, SDK/version or client/server behavior, current availability/eligibility, GitHub implementation, or payment execution. Locators: source lines 14, 18–21; raw lines 14–20.

**Q2 — PASS.** Central purpose: preserve the Samsung Pay deprecation and the replacement-documentation direction. The consequential warning is that the Pay Later link is documentation routing, not Samsung Pay equivalence or migration evidence. Exact deprecation is at raw line 16, guide deprecation and redirect at lines 17–18, and the Configuration next-page link at line 20 is navigation-only; no implementation procedure is present. Locators: source lines 23–27 and 34–42; raw lines 16–20.

## 4. `docs-guides-hosted-fields-upgrading-from-custom-ios-v7`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:931` → concept `wiki/concepts/braintree-ios-sdk.md:83` → source `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-upgrading-from-custom-ios-v7.md` → pinned raw `raw/braintree/docs/guides/hosted-fields/upgrading-from-custom/ios/v7-2026-09-16.md`.

**Q1 — PASS.** Object/action: this Braintree page is titled as an upgrade from Custom to Hosted Fields and is stored on an iOS v7 route, but its complete substantive body says Hosted Fields is available only for JavaScript. Treat it as sparse route/availability evidence. Do not infer iOS Hosted Fields support, an iOS migration procedure, native SDK calls, client/server flow, tokenization behavior, current availability, exact SDK/GitHub behavior, merchant eligibility, runtime rendering, or payment execution. Locators: source lines 14, 18–23; raw lines 1, 6–7, 14, 17–18.

**Q2 — PASS.** Central purpose: retain the route/body mismatch and direct actionable investigation to the linked JavaScript guide as separate, unread navigation. The material warning is that the iOS v7 path and upgrade title do not establish iOS behavior. Exact route identity is at raw lines 1 and 7, title at lines 6 and 14, and the full JavaScript-only availability statement at lines 17–18; no migration steps or schema details exist in the pinned raw. Locators: source lines 25–30 and 37–43; raw lines 1, 6–7, 14, 17–18.

## Completeness pass

All eight fixed questions restate the exact object/action and use same-object evidence. Material conditions and non-inferences are retained, locators resolve, no unsupported related-page claim was introduced, and no direct-catalog deferral was misclassified as failure. **Final: 8/8 PASS; no correction request.**

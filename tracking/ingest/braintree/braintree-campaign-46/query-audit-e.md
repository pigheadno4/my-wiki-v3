# Braintree C46 query audit E — positions 17–20

- UTC start: `2026-10-07T23:47:45Z`
- UTC analysis end: `2026-10-07T23:48:21Z`
- UTC handoff: `2026-10-07T23:48:26Z`
- Scope: manifest positions 17–20 only; eight predetermined questions; repository read-only.
- Result: **8/8 PASS**.

## Shared checks (performed once)

- Manifest pins, source frontmatter, raw source-URL comments, and live raw files agree for all four jobs. Recomputed SHA-256 values match the manifest exactly:
  - `docs-reference-response-venmo-account-node`: `d5ff99bc237aa4b546ac2440a2b1a5281dd24ba7b31bf13d695a413be1c0e863`
  - `docs-guides-unionpay-client-side-ios-v7`: `d7571a71ef087dcc00f2a7043a9a5daaa121b6c82e70206fcd39769d5fdf3c22`
  - `docs-guides-venmo-one-touch`: `1b8e589c9b7b718aa5210be0269dba51e8185ce3778cb9bf4467e5e5966de313`
  - `docs-guides-unionpay-configuration`: `0f74478cd4b86d21d75fa525eb8cff0dda9e5f80e79b474f055bc709f2c7c564`
- Provenance passes: every raw records its matching canonical URL at line 1, fetch date `2026-09-16` at line 2, `llms.txt,sitemap.xml` discovery at line 3, and matching title/slug metadata at lines 6–9.
- Unique primary ownership passes: each exact canonical URL and pinned `raw_files` entry occurs in one source page under `wiki/sources/`.
- Routing and reciprocity pass: `wiki/index.md:11` routes to `wiki/braintree-index.md`; the provider index routes to `[[braintree-server-sdk]]` at line 927 and `[[braintree-payment-methods]]` at line 919. Those concepts link to the exact sources at `wiki/concepts/braintree-server-sdk.md:51` and `wiki/concepts/braintree-payment-methods.md:25,27,29`; each source links back to the same main concept. Direct provider-catalog rows are deferred to structural close, so their present absence is not a content failure.
- One bounded filename/topic gap sweep found the pinned pages plus neighboring Venmo and UnionPay guide variants. No older version of an exact pinned raw was found. None of the neighbors was needed for a retained answer, so no supporting raw was promoted or automatically full-read; related links remain navigation-only.

## 17. `docs-reference-response-venmo-account-node`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:927` → concept `wiki/concepts/braintree-server-sdk.md:51` → source `wiki/sources/braintree/source-braintree-docs-reference-response-venmo-account-node.md` → pinned raw `raw/braintree/docs/reference/response/venmo-account/node-2026-09-16.md`.

**Q1 — PASS.** Object/action: this is Braintree's unversioned Node.js-routed `Venmo Account` response reference. It qualifies Venmo payments as limited release for select merchants and attempts to identify response objects that return the object, but both captured list entries are blank. No environment is named, and the route establishes neither an exact `braintree` package/version nor a request action. Do not infer current availability, merchant selection or enablement, containing response-object types, fields, response completeness, tokenization, authorization, capture, settlement, or funding. Locators: source lines 14, 18–23; raw lines 14, 17–18, 21–25.

**Q2 — PASS.** Central purpose: identify the Venmo Account response-reference object, preserve its select-merchant availability boundary, and expose the empty containing-response list. The material warning is that the blank entries supply no response membership or schema evidence; the Venmo guide is navigation only. Precise details are at raw `# Venmo Account` line 14, `AVAILABILITY` lines 17–18, and the response-object heading/list lines 21–25. Locators: source lines 18–29, 38–44; raw lines 14, 17–18, 21–25.

## 18. `docs-guides-unionpay-client-side-ios-v7`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:29` → source `wiki/sources/braintree/source-braintree-docs-guides-unionpay-client-side-ios-v7.md` → pinned raw `raw/braintree/docs/guides/unionpay/client-side/ios/v7-2026-09-16.md`.

**Q1 — PASS.** Object/action: this Braintree page is routed as UnionPay client-side iOS v7, but its complete substantive body only deprecates the dedicated UnionPay integration and directs readers to process UnionPay as a credit card through the Discover partnership using a separate credit-card guide. No environment or account qualification is stated. Do not infer an iOS procedure, exact Braintree iOS SDK/package behavior, current support, merchant or card eligibility, account enablement, migration equivalence, authorization, settlement, or funding. Locators: source lines 14, 18–22; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: preserve the dedicated-integration deprecation and route readers to separate credit-card documentation. The material warning is that the iOS v7 path and generic client-side title do not establish native iOS behavior, while the linked credit-card guide remains unread navigation. Exact route/title identity is at raw lines 1, 6–9 and 14; the full deprecation and Discover direction is at raw lines 17–18. Locators: source lines 21–27, 29–38; raw lines 1, 6–9, 14, 17–18.

## 19. `docs-guides-venmo-one-touch`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:27` → source `wiki/sources/braintree/source-braintree-docs-guides-venmo-one-touch.md` → pinned raw `raw/braintree/docs/guides/venmo-one-touch-2026-09-16.md`.

**Q1 — PASS.** Object/action: Braintree's unversioned `One Touch for Venmo` guide is a lifecycle notice saying that One Touch for Venmo is no longer the preferred method for accepting Venmo and directing interested readers to the separate Venmo guide. It states no SDK/version, environment, account, merchant, or buyer scope. Do not infer product removal or end of support, technical equivalence, a migration procedure, current Venmo availability, enablement, client/server behavior, or payment execution. Locators: source lines 14, 18–20; raw lines 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose: retain the narrow preferred-method lifecycle change and its Venmo-guide navigation. The material warning is that `no longer the preferred method` is not a stronger deprecation, removal, or unsupported-status claim, and the linked guide contributes no behavior until independently read. Exact identity is at raw lines 6–9 and 14; the complete notice and redirect are at raw lines 17–18. Locators: source lines 14, 18–25, 32–38; raw lines 6–9, 14, 17–18.

## 20. `docs-guides-unionpay-configuration`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:25` → source `wiki/sources/braintree/source-braintree-docs-guides-unionpay-configuration.md` → pinned raw `raw/braintree/docs/guides/unionpay/configuration-2026-09-16.md`.

**Q1 — PASS.** Object/action: Braintree's unversioned UnionPay `Configuration` route contains no configuration procedure. Its complete substantive body deprecates the dedicated UnionPay integration and directs readers toward credit-card processing through the Discover partnership and a separate credit-card guide. No SDK/version, environment, account qualification, or enablement action is stated. Do not infer current support, merchant or card eligibility, configuration fields, client/server placement, migration equivalence, authorization, settlement, or funding. Locators: source lines 14, 18–22; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: preserve the dedicated-integration deprecation and redirect configuration retrieval to separate credit-card documentation. The material warning is that the configuration title does not supply a setup contract, and the linked guide is navigation rather than proof of behavior or eligibility. Exact route/title identity is at raw lines 1, 6–9 and 14; the deprecation, Discover direction, and guide link are all at raw lines 17–18. Locators: source lines 14, 18–27, 29–38; raw lines 1, 6–9, 14, 17–18.

## Completeness pass

All four manifest jobs were covered in order, with two direct questions per page. Every answer names the exact reached object/action, stays within fully read same-object raw authority, retains material conditions and non-inferences, and supplies resolving locators. Hashes, canonical URLs, unique primary ownership, source/concept reciprocity, and root/provider routing pass; no neighboring page was substituted and catalog-row deferral was not misclassified. **Final: 8/8 PASS; no correction request.**

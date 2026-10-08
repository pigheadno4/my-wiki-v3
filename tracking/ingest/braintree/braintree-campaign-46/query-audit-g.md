# Braintree C46 query audit G — positions 25–28

- UTC start: `2026-10-07T23:53:06Z`
- UTC analysis end: `2026-10-07T23:54:51Z`
- UTC handoff: `2026-10-07T23:55:28Z`
- Scope: manifest positions 25–28 only; eight predetermined questions; repository read-only.
- Result: **8/8 PASS**.

## Shared checks (performed once)

- Manifest pins, canonical-source frontmatter, raw source-URL comments, and live raw files agree for all four jobs. Recomputed SHA-256 values match the manifest exactly:
  - `docs-reference-request-apple-pay-registered-domains-node`: `abbcc4f75389c10d8b9ce4898e1bc44035ca7cddce6466a9d01bf8a99df9fbff`
  - `docs-reference-request-apple-pay-unregister-domain-node`: `9de52d91674826afa376c38e25c466353c1dc25b63f34302c289c6f1fbc2045d`
  - `docs-guides-apple-pay-provision-for-decrypted-node`: `5e7cb78e77e3a0243e08a7d342c936a41f408d50fc6ea3a6878d458525de89c0`
  - `articles-guides-payment-methods-samsung-pay`: `3560ab155456ce39e14032b2f123301f9ab1f80992a42edefc747acd998e6560`
- Provenance passes: every pinned raw records its matching canonical URL at line 1, fetch date `2026-09-16` at line 2, `llms.txt,sitemap.xml` discovery at line 3, and matching title/slug metadata at lines 6–9.
- Unique primary ownership passes: each exact canonical URL and pinned `raw_files` entry occurs in exactly one page under `wiki/sources/`.
- Routing and reciprocity pass: `wiki/index.md:11` routes to `wiki/braintree-index.md`; the provider index routes to `[[braintree-payment-methods]]` at line 919 and `[[braintree-apple-pay]]` at line 920. The Apple Pay concept links to the three exact sources at `wiki/concepts/braintree-apple-pay.md:26,28,30`; the payment-methods concept links to the exact Samsung Pay article at `wiki/concepts/braintree-payment-methods.md:29`; every source links back to its same main concept. Direct provider-catalog source rows are deferred to structural close, so their present absence is not a content failure.
- One bounded filename/topic gap sweep found the exact pins plus adjacent Apple Pay register-domain/options routes, Samsung Pay overview/configuration/client/server/testing routes, and the separate Pay Later destination. No older version of any exact pin was found. None of those neighbors was needed to answer the exact reached object/action, so no supporting raw was retained or automatically full-read; the linked PHP/Ruby, Ruby provisioning, and Pay Later pages remain navigation only.

## 25. `docs-reference-request-apple-pay-registered-domains-node`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:920` → concept `wiki/concepts/braintree-apple-pay.md:30` → source `wiki/sources/braintree/source-braintree-docs-reference-request-apple-pay-registered-domains-node.md` → pinned raw `raw/braintree/docs/reference/request/apple-pay/registered-domains/node-2026-09-16.md`.

**Q1 — PASS.** Scope/object/action: this is Braintree's 2026-09-16, unversioned Node.js-routed Apple Pay request-reference page titled `Registered Domains`. The title names a registered-domains topic, but the body documents no Node request object or listing/management action; its only substantive statement says PHP and Ruby SDKs support managing Apple Pay web domains through the API. No exact SDK/package version, environment, account qualification, method, parameters, response, or result semantics are stated. Do not infer Node support, a list operation, current SDK support, merchant eligibility, domain registration/verification state, successful API execution, or payment processing. Locators: source lines 14, 18–23; raw lines 1, 6–9, 13, 16–17.

**Q2 — PASS.** Central purpose: preserve the exact registered-domains route identity and its decisive route/body availability mismatch. The material warning is that the captured body names PHP and Ruby only and supplies no operation; linked Apple Pay Options routes are navigation, not imported authority. Exact topic identity is at raw line 13 and the complete SDK/web-domain qualification at lines 16–17. Locators: source lines 18–30, 37–40; raw lines 13, 16–17.

## 26. `docs-reference-request-apple-pay-unregister-domain-node`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:920` → concept `wiki/concepts/braintree-apple-pay.md:28` → source `wiki/sources/braintree/source-braintree-docs-reference-request-apple-pay-unregister-domain-node.md` → pinned raw `raw/braintree/docs/reference/request/apple-pay/unregister-domain/node-2026-09-16.md`.

**Q1 — PASS.** Scope/object/action: this is Braintree's 2026-09-16, unversioned Node-routed Apple Pay request-reference page titled `Unregister Domain`. The heading identifies the intended action, but the body defines no Node request object, SDK method, request shape, effect, response, or result; it says only that PHP and Ruby SDKs support API management of Apple Pay web domains. No exact SDK/package version, environment, or merchant/account qualification is supplied. Do not infer Node support, a callable unregistration operation, current availability, eligibility, changed domain state, successful unregistration, configuration completion, or payment execution. Locators: source lines 14, 18–20, 24–27; raw lines 1, 6–9, 13, 16–17.

**Q2 — PASS.** Central purpose/action: identify the unregister-domain route while retaining that no unregister procedure is documented at the reached Node authority. The material condition is the PHP/Ruby-only availability notice; its linked Apple Pay Options pages are navigation and cannot supply an unregistration contract here. Exact action identity is at raw line 13 and the full SDK/web-domain qualification at lines 16–17. Locators: source lines 18–27, 34–39; raw lines 13, 16–17.

## 27. `docs-guides-apple-pay-provision-for-decrypted-node`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:920` → concept `wiki/concepts/braintree-apple-pay.md:26` → source `wiki/sources/braintree/source-braintree-docs-guides-apple-pay-provision-for-decrypted-node.md` → pinned raw `raw/braintree/docs/guides/apple-pay/provision-for-decrypted/node-2026-09-16.md`.

**Q1 — PASS.** Scope/object/action: this is Braintree's 2026-09-16, unversioned Node-routed Apple Pay guide titled `Provisioning for Decrypted Processing`. Its only instruction says API provisioning for decrypted Apple Pay processing is available only through the linked Ruby SDK route; it supplies no Node or Ruby provisioning call, resource, credential, decryption role, environment, account qualification, eligibility check, or exact SDK/package version. Do not infer Node support, imported Ruby behavior, current availability, account enablement, completed provisioning, decryption, authorization, settlement, or payment execution. Locators: source lines 14, 18–23; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: preserve the decrypted-processing provisioning topic and the Ruby-only API-provisioning boundary, not fabricate a Node procedure. The material warning is that the title/Node route does not establish Node support and the linked Ruby page remains unread navigation. Exact topic identity is at raw line 14 and the complete availability statement at lines 17–18. Locators: source lines 18–30, 37–39; raw lines 14, 17–18.

## 28. `articles-guides-payment-methods-samsung-pay`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:29` → source `wiki/sources/braintree/source-braintree-articles-guides-payment-methods-samsung-pay.md` → pinned raw `raw/braintree/articles/guides/payment-methods/samsung-pay-2026-09-16.md`.

**Q1 — PASS.** Scope/object/action: this is Braintree's 2026-09-16 unversioned article-level Samsung Pay lifecycle page. The complete substantive body says Samsung Pay is deprecated, says the guide is deprecated, and directs readers to the distinct Pay Later offers guide. It states no SDK/version, client/server platform, environment, account/merchant scope, setup object, migration action, or transaction lifecycle. Do not infer Pay Later equivalence, a migration procedure, current product removal or availability beyond the dated wording, merchant eligibility, enablement, successful payment execution, vaulting, settlement, or funding. Locators: source lines 14, 18–20, 24–26; raw lines 1, 6–9, 14, 16, 19–20.

**Q2 — PASS.** Central purpose/action: retain the captured Samsung Pay product-and-guide deprecation notices and the documentation redirect. The material warning is that the Pay Later link is navigation only, not technical replacement or migration authority; no setup or payment action is documented. Product identity is at raw line 14, product deprecation at line 16, and guide deprecation plus redirect at lines 19–20. Locators: source lines 18–26, 28–39; raw lines 14, 16, 19–20.

## Completeness pass

All four manifest jobs were covered in 1-based order with two direct questions per page. Every answer matches the exact reached object/action authority, stays within fully read same-object pinned raw evidence, retains material conditions and non-inferences, and supplies resolving locators. Hashes, canonical URLs, provenance, unique primary ownership, source/concept reciprocity, and root/provider routing pass; no neighboring page was substituted and catalog-row deferral was not misclassified. **Final: 8/8 PASS; no correction request.**

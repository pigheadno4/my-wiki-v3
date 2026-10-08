# Braintree C46 query audit L — position 45

- UTC start: `2026-10-07T23:52:00Z`
- UTC analysis end: `2026-10-07T23:58:35Z`
- UTC handoff: `2026-10-07T23:58:55Z`
- Scope: manifest position 45 only; two fixed questions; repository read-only.
- Result: **2/2 PASS**.

Coordinator timing note: the self-reported start above precedes this group's actual post-promotion dispatch. Exclude that start from performance calculations; retain the content checks and final verdict. External artifact time is the handoff timing authority.

## Shared checks (performed once)

- Manifest position 45 pins `docs-guides-hosted-fields-styling-android-v5`, raw `raw/braintree/docs/guides/hosted-fields/styling/android/v5-2026-09-16.md`, SHA-256 `2e927d4013d36afd109e3419293366a78eadcfca6c830ec85ba73dcfe807cd3a`, source target `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-styling-android-v5.md`, and canonical URL `https://developer.paypal.com/braintree/docs/guides/hosted-fields/styling/android/v5` (`manifest.json:412-419`). The recomputed raw hash matches exactly.
- Provenance passes: raw lines 1–3 record the matching canonical URL, fetch date `2026-09-16`, and `llms.txt,sitemap.xml` discovery; lines 6–9 preserve the title, Android v5 slug, and source timestamps. Source frontmatter lines 2–9 agrees with the manifest and raw.
- Unique primary ownership passes: the exact canonical URL and exact pinned `raw_files` value each occur in one source page under `wiki/sources/`.
- Routing and reciprocity pass: root `wiki/index.md:11` routes to `wiki/braintree-index.md`; the provider index has the exact source row at line 65; source line 34 names `[[braintree-android-sdk]]` as its main concept; concept line 74 links back to the exact source. The source also links Braintree at line 33, and the company page has the source row at line 64. Direct catalog rows deferred until structural close would not be content failures; this page's expected rows are already present.
- One bounded filename/topic gap sweep found the exact Android v5 pin, the same-date JavaScript v3 styling raw, and sibling Hosted Fields route files. No older exact Android styling raw was found. The JavaScript target is navigation-only for this exact query and was not needed as supporting authority, so it was not automatically full-read or promoted.

## 45. `docs-guides-hosted-fields-styling-android-v5`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:65` → concept `wiki/concepts/braintree-android-sdk.md:74` → source `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-styling-android-v5.md` → pinned raw `raw/braintree/docs/guides/hosted-fields/styling/android/v5-2026-09-16.md`.

**Q1 — PASS.** Provider/document/product/SDK/version/environment/account/object/action scope: this is Braintree's Hosted Fields document titled `Styling`, captured at an Android v5 route. The reached authority contains no Android styling operation, native SDK call, property, field, schema, rendering rule, client/server flow, environment, account qualification, or exact package behavior. Its complete substantive body instead says Hosted Fields is available only for JavaScript and links the separate JavaScript v3 styling route. Treat Android v5 as route metadata and the page as a sparse availability/navigation record, not an Android styling guide. Do not infer native Android Hosted Fields support or parity, current JavaScript availability, exact Android or JavaScript package/GitHub behavior, merchant eligibility, successful configuration, hosted rendering, tokenization, server processing, or payment execution. Locators: source lines 14, 18–22, 24–29; raw lines 1, 6–9, 14, 17–18.

**Q2 — PASS.** Central purpose/action: preserve the Android-route/JavaScript-only mismatch and direct styling retrieval to the separately authoritative JavaScript guide. The consequential warning is that route and title do not establish native Android styling behavior or current SDK support. The pinned raw contains no styling procedure, supported values, or schema detail: exact identity is at raw lines 1, 6–9 and 14, while the entire availability statement and only implementation-retrieval link are at raw lines 17–18. The linked JavaScript v3 page must be separately read before using its styling behavior; it contributes no behavior to this answer. Locators: source lines 14, 18–29, 36–42; raw lines 1, 6–9, 14, 17–18.

## Completeness pass

The one assigned manifest page was covered in 1-based position order with both fixed direct answers. Each answer restates the exact reached document object/action, stays within the fully read same-object pinned raw, retains the route/platform mismatch and material non-inferences, and supplies resolving locators. Hash, canonical URL, provenance, unique primary ownership, source/concept reciprocity, root/provider routing, and the bounded gap sweep all pass. No sibling or linked page was substituted, and no catalog-close deferral was misclassified. **Final: 2/2 PASS; no correction request.**

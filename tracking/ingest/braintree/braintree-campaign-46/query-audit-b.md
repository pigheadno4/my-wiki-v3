# Braintree C46 query audit B — positions 5–8

- UTC start: `2026-10-07T23:42:51Z`
- UTC analysis end: `2026-10-07T23:43:43Z`
- UTC handoff: `2026-10-07T23:43:43Z`
- Scope: manifest positions 5–8 only; eight predetermined questions; repository read-only.
- Result: **8/8 PASS**.

## Shared checks (performed once)

- Manifest pins, live raw files, source frontmatter, and raw source-URL comments agree for all four jobs. Recomputed SHA-256 values match the manifest exactly:
  - `docs-guides-hosted-fields-upgrading-from-custom-android-v5`: `77c1dba99d09c77df66e89cec82681235ede12717759c984e081b3aad981aa38`
  - `docs-guides-elo-configuration`: `47500ed54bb4b02bb1cc406801eb77960c486ec2ab52d3bfbdfc0834dd4383ca`
  - `docs-reference-request-credit-card-verification-create-node`: `077dd476a0264aa4477af8e81c434e72021f792a1917c67127669b1e510c4670`
  - `docs-guides-ach-configuration`: `84fb2b828121d5b0a74ccb9c3e54ca9d8ad8f1b84d4afaa919bc92827d004477`
- Identity and provenance pass: each raw records the matching canonical source URL at line 1, fetch date `2026-09-16` at line 2, `llms.txt,sitemap.xml` discovery at line 3, and matching title/slug metadata at lines 6–9.
- Single ownership passes: each exact canonical URL, raw source-URL comment, and pinned raw path has one primary source owner under `wiki/sources/`.
- Discoverability and reciprocity pass: `wiki/index.md:11` routes to `wiki/braintree-index.md`; the provider index routes to `[[braintree-payment-methods]]` at line 919, `[[braintree-server-sdk]]` at line 927, and `[[braintree-android-sdk]]` at line 930. The selected concepts link to each exact source at `braintree-payment-methods.md:29,31`, `braintree-server-sdk.md:51`, and `braintree-android-sdk.md:74`; every source links back to its selected main concept. Direct provider/company source-catalog rows are deferred to structural close, so their present absence is not a content failure.
- One bounded filename/topic gap sweep found only the four manifest-pinned raws. No older raw or neighboring authority was opened automatically. No supporting evidence was retained because each answer below is fully established by its same-object pinned raw; related links remain navigation-only.

## 5. `docs-guides-hosted-fields-upgrading-from-custom-android-v5`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:930` → concept `wiki/concepts/braintree-android-sdk.md:74` → source `wiki/sources/braintree/source-braintree-docs-guides-hosted-fields-upgrading-from-custom-android-v5.md` → pinned raw `raw/braintree/docs/guides/hosted-fields/upgrading-from-custom/android/v5-2026-09-16.md`.

**Q1 — PASS.** Object/action: this Braintree document is titled as an upgrade from Custom to Hosted Fields and is captured on an Android v5 route, but its complete substantive body says Hosted Fields is available only for JavaScript. The defensible action is scope triage and separate retrieval of the linked JavaScript guide. Do not infer Android Hosted Fields support, an Android migration procedure, native SDK calls, an exact Android/JavaScript package version, account or environment enablement, current availability, tokenization behavior, runtime rendering, or payment execution. Locators: source lines 14, 18–22; raw lines 1, 6–7, 14, 17–18.

**Q2 — PASS.** Central purpose: preserve the route/body mismatch, not supply an Android upgrade procedure. The material warning is that the `/android/v5` path and upgrade title do not override the JavaScript-only body. Exact route identity is at raw lines 1 and 7, title at lines 6 and 14, and the complete availability statement at lines 17–18; the linked JavaScript guide is navigation only. Locators: source lines 18–29, 36–38; raw lines 1, 6–7, 14, 17–18.

## 6. `docs-guides-elo-configuration`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:31` → source `wiki/sources/braintree/source-braintree-docs-guides-elo-configuration.md` → pinned raw `raw/braintree/docs/guides/elo/configuration-2026-09-16.md`.

**Q1 — PASS.** Object/action: Braintree's unversioned Elo configuration notice says Elo is in limited release for select merchants using what the page calls the latest JavaScript v3 and server SDKs, and directs merchants to contact Braintree to request access. Elo is not automatically enabled in Sandbox or Production accounts; a merchant ready to integrate is directed to contact Braintree. Do not infer an exact package/version, current availability, merchant selection or approval, either environment's enablement, configuration fields, client/server implementation, GitHub behavior, or authorization, payment, settlement, or funding success. Locators: source lines 14, 18–22; raw lines 17–18, 21–23.

**Q2 — PASS.** Central purpose: document Elo's limited-release access and account-enablement request boundary. Material conditions are select-merchant scope, page-relative latest JavaScript v3 plus server SDKs, and nonautomatic Sandbox/Production enablement; contacting Braintree is only a request action. Precise details are at raw `AVAILABILITY` lines 17–18 and `Braintree requirements` lines 21–23; the page supplies no Control Panel or integration procedure. Locators: source lines 18–27; raw lines 17–18, 21–23.

## 7. `docs-reference-request-credit-card-verification-create-node`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:927` → concept `wiki/concepts/braintree-server-sdk.md:51` → source `wiki/sources/braintree/source-braintree-docs-reference-request-credit-card-verification-create-node.md` → pinned raw `raw/braintree/docs/reference/request/credit-card-verification/create/node-2026-09-16.md`.

**Q1 — PASS.** Object/action: this Braintree Node.js-routed request reference describes performing a standalone credit-card verification without storing the card in the Vault. That path requires passing raw card data and should be used only in a PCI-compliant environment; uncertain readers are directed toward standard card verification with vaulting. Do not infer a reliable method name or request schema from the damaged final sentence, an exact `braintree` package/version, merchant/account enablement, Sandbox or Production behavior, compliance status, successful verification, Vault storage, sale, authorization, settlement, or funding. Locators: source lines 14, 18–23; raw lines 13–16.

**Q2 — PASS.** Central purpose: establish the no-Vault standalone verification option and its raw-card-data PCI condition. The material warning is that the captured fallback sentence is damaged around its link, so it supports only the direction to standard verification plus vaulting, not executable syntax. Exact document/action identity is at raw lines 13–15 and the PCI condition plus damaged fallback is at line 16; the separate server-side guide is navigation only. Locators: source lines 18–30, 38–40; raw lines 13–16.

## 8. `docs-guides-ach-configuration`

Route: root `wiki/index.md:11` → provider `wiki/braintree-index.md:919` → concept `wiki/concepts/braintree-payment-methods.md:29` → source `wiki/sources/braintree/source-braintree-docs-guides-ach-configuration.md` → pinned raw `raw/braintree/docs/guides/ach/configuration-2026-09-16.md`.

**Q1 — PASS.** Object/action: Braintree's unversioned ACH Direct Debit configuration notice applies to eligible merchants able to build a custom client-side JavaScript v3 integration, explicitly excludes Drop-in UI, and directs qualifying merchants to contact Braintree to request Sandbox-account enablement. Do not infer other bank-payment methods, merchant eligibility, successful enablement, a Production enablement process, configuration fields, bank-account collection or verification, nonce/server/transaction lifecycle, an exact SDK/package or GitHub implementation, current availability, payment execution, settlement, or funding. Locators: source lines 14, 18–21, 25–27; raw lines 16–19.

**Q2 — PASS.** Central purpose: state the eligibility, custom JavaScript v3, Drop-in exclusion, and Sandbox-request conditions for this ACH Direct Debit configuration route. The material warning is that contact is a request path, not account-enablement evidence, and the next-page client-side link is navigation only. Precise conditions are at raw lines 16–19 and the next-page locator is line 23; no implementation or lifecycle procedure is present. Locators: source lines 18–27, 29–34, 42–44; raw lines 16–19, 23.

## Completeness pass

All eight fixed questions identify the exact reached object/action, answer only from fully read pinned raw evidence, retain material conditions and non-inferences, and provide resolving locators. Routes are reciprocal, ownership and provenance are unique, no neighboring object was substituted, no unsupported support file was introduced, and direct-catalog deferral was not misclassified as failure. **Final: 8/8 PASS; no correction request.**

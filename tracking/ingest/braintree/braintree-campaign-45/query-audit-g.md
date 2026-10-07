# Braintree C45 fixed-query audit G

- Scope: manifest positions 25–28 only; read-only audit.
- UTC start: `2026-10-07T14:00:38Z`
- UTC analysis end: `2026-10-07T14:02:42Z`
- UTC handoff: `2026-10-07T14:03:31Z`

## Shared checks

- **Pins, URL, identity, ownership:** PASS. All four on-disk SHA-256 values equal the C45 manifest pins. Each manifest canonical URL equals both the raw `Source URL` and source-page `canonical_url`. Each canonical URL and relative raw path has exactly one owner under `wiki/sources/braintree/`; job IDs, targets, and platform/version route identities are distinct.
- **Provenance and reciprocity:** PASS. Every source page names the exact pinned raw in both `raw_files` and `Raw Sources`, links its company and main concept, and is reciprocally listed by that concept. The actual routes are `[[index]]` → `[[braintree-index]]` → the named concept → source → pinned raw. Direct C45 source rows in `braintree-index` are still deferred coordinator-close catalog work and are not content failures.
- **Bounded gap sweep / extra authority:** PASS. A single path-bounded sweep covered Google Pay configuration/client-side siblings, ACH overview/server-side siblings, and the In-Person Sandbox, Dev Kit, reader-setup, and V400m pages named by navigation. None is needed to answer these exact document/object/action questions. No extra authority was read or imported; source-page related links remain navigation-only, and no older snapshot was selected automatically.

## 25. `docs-guides-google-pay-configuration-ios-v7`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-google-pay-configuration-ios-v7]]` → `raw/braintree/docs/guides/google-pay/configuration/ios/v7-2026-09-16.md`.

- **Q1 — PASS.** Braintree website document for Google Pay configuration at an **iOS v7 route**, collected 2026-09-16. Its body establishes no iOS Google Pay configuration object or action; it instead limits Google Pay availability to JavaScript v3 and Android and carries a cross-mobile certificate-remediation action. No environment or particular merchant account is established. Do not infer iOS Google Pay support, an iOS procedure, current availability/support, exact package/GitHub behavior, browser or client/server behavior, account enablement, eligibility, or payment execution. **Locators:** raw URL/slug/title at lines 1, 5–14; availability at lines 23–24; source `Overview`, `Key takeaways`, and `Route, support and date boundary`.
- **Q2 — PASS.** For the requested configuration action, the material finding is that this page supplies **no iOS configuration procedure**. It says Google Pay is only available for JavaScript v3 and Android. Separately, its historical notice says to upgrade iOS to `6.17.0+` and Android to `4.45.0+` or `5.0.0+`, or decommission/force-upgrade affected app versions by March 30, 2026; otherwise `100%` of customer traffic from those affected versions would fail. Because collection followed that date, this is retained historical wording, not current status proof. **Precise raw detail:** lines 17–20 (versions, deadline, action, consequence), 23–24 (platform availability), 26 (malformed `undefined` navigation artifact); source `Detail locators`.

## 26. `in-person-get-started-1-integration-checklist`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-in-person]]` → `[[source-braintree-in-person-get-started-1-integration-checklist]]` → `raw/braintree/in-person/get-started-1/integration-checklist-2026-09-16.md`.

- **Q1 — PASS.** Braintree In-Person, unversioned onboarding/navigation checklist for beginning an integration: stakeholder coordination, Sandbox signup, Dev Kit request, Postman collection, reader setup/pairing, build start, and Production-transition coordination. It establishes no SDK/API version, retailer/platform operating model, account hierarchy, credential schema, device certification/current availability, approval, completed pairing, Production enablement, or authorization/payment/settlement/funding outcome. **Locators:** raw URL/slug/title at lines 1, 5–14; checklist purpose at lines 16–18; source `Overview` and `Material boundaries`.
- **Q2 — PASS.** The central action is to consult Braintree sales/engineering, sign up for Sandbox, request a Dev Kit, obtain/build a Postman collection, set up and pair the Dev Kit reader to Sandbox, then build while remaining in close engineering contact for best practices and Production transition. The consequential condition is advisory coordination, not proof that requirements are covered or any linked step succeeded; V400m is only linked navigation. **Precise raw detail:** line 20 (the complete collapsed checklist and coordination warning), line 22 (V400m/Dev Kit navigation); source `Key takeaways` and `Detail locators`.

## 27. `docs-guides-ach-client-side-android-v5`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-ach-client-side-android-v5]]` → `raw/braintree/docs/guides/ach/client-side/android/v5-2026-09-16.md`.

- **Q1 — PASS.** Braintree ACH Direct Debit client-side document at an **Android v5 route**, collected 2026-09-16. The substantive ACH statement applies to eligible merchants using **JavaScript v3**, not an Android object or action. No environment or particular account is established. Do not infer Android v5 ACH capability, bank-data collection, tokenization/nonce, verification, vaulting, server transaction or lifecycle behavior, current availability, merchant enablement, exact package compatibility, or payment execution. **Locators:** raw URL/slug/title at lines 1, 5–14; availability at lines 17–18; source `Overview`, `Key takeaways`, and `Android route versus retained body`.
- **Q2 — PASS.** For the requested Android client-side action, the page documents **no Android ACH implementation procedure**; it only routes eligible merchants to JavaScript v3. Its separate historical certificate warning directs upgrades to iOS `6.17.0+` and Android `4.45.0+` or `5.0.0+`, or decommission/force-upgrade affected app versions by March 30, 2026, with a stated `100%` traffic-failure consequence. The server-side link is navigation, not server behavior evidence. **Precise raw detail:** lines 17–18 (ACH eligibility/JavaScript v3), 21–24 (certificate action and consequence), 26 (server-side navigation); source `Detail locators`.

## 28. `docs-guides-ach-client-side-ios-v7`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-docs-guides-ach-client-side-ios-v7]]` → `raw/braintree/docs/guides/ach/client-side/ios/v7-2026-09-16.md`.

- **Q1 — PASS.** Braintree ACH Direct Debit client-side document at an **iOS v7 route**, collected 2026-09-16. Its only ACH availability statement applies to eligible merchants using **JavaScript v3** and establishes no native iOS object/action, environment, or particular account. Do not infer iOS ACH setup, collection/tokenization/verification, nonce handoff, server processing, settlement/funding, current support, account enablement, exact package/GitHub behavior, or payment execution. **Locators:** raw URL/slug/title at lines 1, 5–14; availability at lines 17–18; source `Overview`, `Key takeaways`, and `Material boundaries`.
- **Q2 — PASS.** For the requested iOS client-side action, the page documents **no iOS ACH implementation procedure**; it only points eligible merchants to JavaScript v3. Its historical certificate notice directs iOS `6.17.0+` and Android `4.45.0+` or `5.0.0+`, or decommission/force-upgrade by March 30, 2026, warning that affected app versions otherwise lose `100%` of customer traffic. The raw contains malformed `&gt;Android`, so it is formatting residue, not an operator or version relation. **Precise raw detail:** lines 17–18 (availability), 21–22 (certificate versions, deadline, action, consequence, malformed separator); source `Detail locators`.

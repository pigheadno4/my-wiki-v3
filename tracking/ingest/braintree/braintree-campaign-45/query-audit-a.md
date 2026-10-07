# Braintree C45 fixed-query audit — group A

- Scope: manifest positions 1–4 only; eight predetermined queries.
- Result: **PASS — 8/8 queries**.
- Started UTC: 2026-10-07T13:32:55Z; analysis ended UTC: 2026-10-07T13:34:55Z; handoff prepared UTC: 2026-10-07T13:35:53Z.

## Shared checks

- Integrity and identity: all four computed SHA-256 values match the manifest. Each manifest canonical URL matches both raw Source URL and source frontmatter; raw title/slug and source identity also match. Each source raw_files and Raw Sources entry points to the pinned primary raw.
- Ownership and reciprocity: every pinned raw path and canonical URL has exactly one source owner. Reciprocal main-concept links pass: Android client encryption ↔ braintree-android-sdk, Windows Phone and Reference Overview ↔ braintree-payment-platform, and Masterpass Overview ↔ braintree-payment-methods.
- Retrieval closure: wiki/index.md:11 routes to wiki/braintree-index.md; provider concept rows are at wiki/braintree-index.md:865-877. Direct C45 source catalog rows are deferred to coordinator close, so their present absence is not a content failure.
- Bounded gap sweep: exact URL/path and topic sweeps found the assigned raw, discovery inventories, sibling client-encryption and Masterpass/reference material. No older snapshot of the same URL was read. Only the consequential Masterpass/SRC support conflict required extra authority; both raw/braintree/articles/guides/payment-methods/masterpass-2026-09-16.md and raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16.md were read fully. Upgrade, certificate, and downstream API-detail links remained navigation-only.

## 1. Deprecated Client-Side Encryption — Android Library

Actual route: wiki/index.md:11 → wiki/braintree-index.md:877 → wiki/concepts/braintree-android-sdk.md:76 → wiki/sources/braintree/source-braintree-docs-deprecated-client-side-encryption-android-library.md → raw/braintree/docs/deprecated/client-side-encryption/android-library-2026-09-16.md.

**Q1 — exact scope. PASS.** Object/action match: yes — the requested object is Braintree's deprecated Android client-side-encryption library, and the documented actions are installing/importing it and encrypting card-number, CVV, and expiration strings. The page identifies encryption-2.0.0.jar, an alternative Android library-project route for SDK r6 or higher, and an Eclipse assumption; it names no Sandbox/Production environment or merchant/account condition. Do not infer current Android SDK/package or GitHub support, server handoff, gateway processing, PCI compliance, or payment outcome. Locators: source :14,18-20; raw :1,6-9,14,17-18,21-37,49-54.

**Q2 — purpose, action, conditions/warnings, detail route. PASS.** Object/action match: yes — this page's central action is field-by-field client encryption through the historical library. The consequential warning is explicit deprecation and an upgrade link. Exact values/procedure remain retrievable at raw :24-26 (jar and displayed SHA1), :27-37 (SDK r6+/Eclipse project steps), :40-48 (source/examples/support routes), and :49-54 (placeholder key and encrypt calls).

## 2. Deprecated Client-Side Encryption — Windows Phone

Actual route: wiki/index.md:11 → wiki/braintree-index.md:865 → wiki/concepts/braintree-payment-platform.md:30 → wiki/sources/braintree/source-braintree-docs-deprecated-client-side-encryption-windows-phone.md → raw/braintree/docs/deprecated/client-side-encryption/windows-phone-2026-09-16.md.

**Q1 — exact scope. PASS.** Object/action match: yes — the requested object is Braintree's deprecated Windows Phone client-encryption class library, and the actions are importing/referencing it and encrypting the three shown card-field strings. It is a .NET-rendered example but names no library/package release, Windows Phone version, runtime, build prerequisite, environment, or account scope. Do not infer current SDK/platform/repository support, successful encryption, tokenization, server/gateway behavior, PCI compliance, or any payment result. Locators: source :14,18-25; raw :1,6-9,14,17-18,21-29,41-48.

**Q2 — purpose, action, conditions/warnings, detail route. PASS.** Object/action match: yes — the historical quick start constructs Braintree with a placeholder client-side-encryption key and calls Encrypt separately for card number, CVV, and expiry. Deprecation is the controlling warning. Exact procedures and navigation are at raw :21-29 (clone/import/dependency/reference), :32-40 (source/examples/bugs), and :41-48 (example); no merchant-server handoff, errors, or payment operation is documented.

## 3. Masterpass Overview

Actual route: wiki/index.md:11 → wiki/braintree-index.md:866 → wiki/concepts/braintree-payment-methods.md:27 → wiki/sources/braintree/source-braintree-docs-guides-masterpass-overview.md → raw/braintree/docs/guides/masterpass/overview-2026-09-16.md.

**Q1 — exact scope. PASS.** Object/action match: yes — the object is the historical Mastercard Masterpass web wallet and the page's action scope is processing Masterpass payments through Braintree plus directing prior users toward SRC. The Masterpass page is unversioned; Android v2, iOS v4, and JavaScript v3 are historical Client SDK introduction labels for SRC, not current package versions or Masterpass support. No environment is named. SRC is limited to eligible merchants, subject to API change, and access-requested through Braintree. Do not infer current Masterpass/SRC availability, merchant enablement, buyer eligibility, implementation behavior, or payment execution. Locators: source :14,18-20; primary raw :1,6-9,14,17-25.

**Q2 — purpose, action, conditions/warnings, detail route. PASS.** Object/action match: yes — the page explains the one-sign-in web wallet and Braintree processing-guide purpose, but its consequential instruction says Masterpass was replaced by SRC. Preserve the unresolved warning: supporting Braintree pages also say Click to Pay/SRC is unsupported effective January 20, 2026, with Payment method not supported and decline risk, while retaining limited-release wording. The primary page contains no executable client/server procedure. Locators: primary raw :18 (replacement, limited release, API-change warning, SDK generations, access request) and :20-25 (identity/purpose/support route); supporting Masterpass raw :23-24 and SRC raw :14-15,21-48.

## 4. Reference Overview

Actual route: wiki/index.md:11 → wiki/braintree-index.md:865 → wiki/concepts/braintree-payment-platform.md:28 → wiki/sources/braintree/source-braintree-docs-reference-overview.md → raw/braintree/docs/reference/overview-2026-09-16.md.

**Q1 — exact scope. PASS.** Object/action match: yes — the object is Braintree's unversioned reference directory, and the action is navigation among client references, server request/response references, Forward API, and general material. Visible labels cover Android, iOS/iOS Drop-in, JavaScript v3 Hosted Fields/Drop-In, and a separate JavaScript v2 route; no exact package version, environment, account setup, schema, or transaction object/action is defined. Do not infer current SDK support, API contract, merchant enablement, request success, payment, settlement, or funding. Locators: source :14,18-22; raw :1,6-9,14-26,29-50.

**Q2 — purpose, action, conditions/warnings, detail route. PASS.** Object/action match: yes — the page is a routing map, not an implementation procedure. Consequential qualifications are the upcoming-certificate-change warning and Forward API eligibility. Precise request schemas/methods, response fields, errors, sandbox values, processor responses, and mitigations must be retrieved from the linked detailed references; this overview does not inventory them. Locators: raw :29-35 (request purpose and certificate route), :38-40 (response-object purpose), :43-45 (Forward API eligibility), and :48-50 (general-detail categories).

## Query tally

| Page | Q1 exact scope | Q2 purpose/actions/conditions/detail route |
| --- | --- | --- |
| Deprecated Android client encryption | PASS | PASS |
| Deprecated Windows Phone client encryption | PASS | PASS |
| Masterpass Overview | PASS | PASS |
| Reference Overview | PASS | PASS |

Eight answers are present: 8/8 PASS. No missing material fact, object/action mismatch, source-identity failure, hash failure, reciprocity failure, or unresolved field-location request was found.

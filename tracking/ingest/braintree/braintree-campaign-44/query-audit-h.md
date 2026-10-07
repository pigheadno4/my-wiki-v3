# Braintree C44 fixed-query audit — group H

- Scope: approved C44 positions 29–32; eight predetermined queries.
- Result: **PASS — 8/8 queries**.
- Completed UTC: `2026-10-07T12:51:38Z`

## Shared checks

- **Approval, pins and provenance — PASS.** All four jobs are `approved` at attempt 1. Recomputed SHA-256 matches the manifest: Google Pay Android v5 configuration `c97f7e39a2495e50d5918bf088b85420eac8e2debe3de01c039c570d6117c368`; package-tracking client `7f9802a48428090a67176673ab32450ce0467f0ee646989f05d3cfe747cbe463`; Amex server Node `9415e27e1d0754c70509a547f3f94baf79928a179727dd3a42d3d439c535a3c1`; Apple Pay testing/go-live `00151334b29d61829afadba3ad5d45fa3896b08cc51955f4a9ced58fcdb65652`. Manifest URL, source `canonical_url`, raw `Source URL`, `raw_files`, and `Raw Sources` agree; every raw records `Fetched: 2026-09-16` and `Discovery: llms.txt,sitemap.xml`.
- **PRIMARY ownership and reciprocity — PASS.** Each exact primary raw path and canonical URL has one source owner, and no source duplicates a primary as supporting raw. Routes resolve `wiki/index.md:11` → `wiki/braintree-index.md:812-814,824` → main concept → source → exact primary raw. Concepts reciprocate at `wiki/concepts/braintree-android-sdk.md:74`, `braintree-payment-platform.md:30`, `braintree-payment-methods.md:23`, and `braintree-apple-pay.md:24`; sources link back at their lines `14/35`, `39`, `36`, and `14/37`. Deferred direct provider-catalog rows are shared-close work, not failures while these concept routes work.
- **Full reads and bounded gap sweep — PASS.** The four sources, four pinned raws, and all four main concepts were read in full. One bounded filename/topic sweep covered adjacent Google Pay, package-tracking, Amex Express Checkout/SRC, and Apple Pay routes. Only the Amex page retains a cross-source conflict, so its provider-wide supporting source and pinned raw were also read in full; other siblings remain navigation only. The partial JavaScript/Swift/Kotlin examples and field notation are illustrative and nonblocking: no source makes a runnable, exact-package, successful-execution, or payment-outcome guarantee.

## Position 29 — `docs-guides-google-pay-configuration-android-v5` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:824` → `wiki/concepts/braintree-android-sdk.md:74` → `wiki/sources/braintree/source-braintree-docs-guides-google-pay-configuration-android-v5.md` → `raw/braintree/docs/guides/google-pay/configuration/android/v5-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16 Google Pay configuration webpage on the Android v5 documentation route. Its action scope is Control Panel enablement for Sandbox or Production, merchant-account-specific activation routing, separate Google production work, and dual PayPal/Google Pay enablement for PayPal via Google Pay. It names no exact Android artifact/package version, device/client tokenization object, server transaction API, completed account enablement, present eligibility, or payment result. Source `:14,18-20`; raw `:25-43`.
2. **Purpose, action, conditions, warnings, detail route — PASS.** The page's purpose is configuration prerequisites: use the matching environment's Control Panel, enable Google Pay under Account Settings → Payment Methods, contact Braintree when a particular merchant account still needs activation, and work with Google for Production. The dated certificate warning preserves its Android `4.45.0+` or `5.0.0+` wording and stated failure consequence without treating it as current certificate/package/runtime evidence. Source `:18-23,27-31`; raw `:17-20,25-43`.

## Position 30 — `docs-guides-package-tracking-client-side` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:812` → `wiki/concepts/braintree-payment-platform.md:30` → `wiki/sources/braintree/source-braintree-docs-guides-package-tracking-client-side.md` → `raw/braintree/docs/guides/package-tracking/client-side-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16, unversioned package-tracking client-configuration webpage. It illustrates PayPal user-approval line items in JavaScript, Swift, and Kotlin and a conditional client/server handoff; it names no exact client package, mobile OS/language runtime, server SDK, environment, account eligibility, or tracking-submission object. It is not proof of user approval, server acceptance, shipment, fulfillment, payment, or compatibility across SDKs. Source `:14-16,20-22`; raw `:16-18,21-72`.
2. **Purpose, action, conditions, warnings, detail route — PASS.** The central action is adding line-item metadata to the client approval request. Server-side line items may be omitted only when the Client SDK already submitted them and they have not changed. The source preserves the page's incomplete-integration warning, distinguishes the field coverage of the three snippets, and routes exact example values and the Java next-page label without borrowing behavior from unread targets. Source `:20-34`; raw `:16-18,21-73`.

## Position 31 — `docs-guides-amex-express-checkout-server-side-node` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:813` → `wiki/concepts/braintree-payment-methods.md:23` → `wiki/sources/braintree/source-braintree-docs-guides-amex-express-checkout-server-side-node.md` → `raw/braintree/docs/guides/amex-express-checkout/server-side/node-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16, unversioned Node-routed server webpage for legacy Amex Express Checkout. It documents the client-callback value as a standard payment-method nonce for a merchant server and names two card-identification fields, but shows no Node call and names no Node package/runtime, environment, account state, current enablement, transaction request, or payment outcome. The Android v2/iOS v4/JavaScript v3 labels apply to the replacement SRC client families, not Node Server SDK behavior. Source `:14-22`; raw `:17-32`.
2. **Purpose, action, conditions, warnings, detail route — PASS.** The page routes nonce-based transaction creation elsewhere and defines `card_member_expiry_date` and `card_member_number` as physical-card identification values without promising their presence on a response. Its replacement warning is preserved: the page directs prior Amex users to eligible-merchant, limited-release SRC, while the fully read provider-wide authority both announces January 20, 2026 Click to Pay/SRC end of support and calls SRC currently limited-release. The source correctly leaves current support and a safe migration path unresolved. Source `:20-31`; supporting source `wiki/sources/braintree/source-braintree-get-started-payment-methods.md:20-35`; primary raw `:17-32`; supporting raw `raw/braintree/articles/get-started/payment-methods-2026-09-16.md:14-15,87-89`.

## Position 32 — `docs-guides-apple-pay-testing-go-live` — PASS / PASS

**Route/page:** `wiki/index.md:11` → `wiki/braintree-index.md:814` → `wiki/concepts/braintree-apple-pay.md:24` → `wiki/sources/braintree/source-braintree-docs-guides-apple-pay-testing-go-live.md` → `raw/braintree/docs/guides/apple-pay/testing-go-live-2026-09-16.md`.

1. **Exact scope and non-inference — PASS.** This is Braintree's fetched 2026-09-16, unversioned Apple Pay testing/go-live webpage spanning device/web, Sandbox, development diagnosis, and Production. Its objects/actions are sandbox cards and tester accounts, returned nonces, test fixtures, Braintree-held production certificates, DPAN comparison, `publicKeyHash` diagnosis, and limited live checks. It names no exact client/server SDK package or version and does not prove current merchant/card/device/browser eligibility, account configuration, certificate match, tokenization, or transaction success. Source `:14,18-24`; raw `:16-27`.
2. **Purpose, action, conditions, warnings, detail route — PASS.** Full-flow testing requires an Apple Pay-capable device; web testing names Safari or Chrome; sandbox test cards require an iCloud sandbox tester account, and a successfully decrypted sandbox nonce still contains dummy data. Production decryption and DPAN matching, development certificate-mismatch diagnosis, and separate test-amount/nonce simulation routes are accurately scoped. The real-transaction checklist is explicitly provider guidance, not authorization, budget, or outcome evidence. Source `:18-32`; raw `:16-27`.

## Query tally

| Page | Q1 exact scope | Q2 purpose/actions/conditions/detail route |
| --- | --- | --- |
| Google Pay Configuration — Android v5 | PASS | PASS |
| Package Tracking — Client-side | PASS | PASS |
| Amex Express Checkout — Server-side Node | PASS | PASS |
| Apple Pay — Testing and Go Live | PASS | PASS |

No correction or additional supporting authority is required. **Verdict: PASS — 4/4 pages, 8/8 fixed questions.**

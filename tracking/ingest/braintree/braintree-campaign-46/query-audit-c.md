# Braintree C46 query audit C — manifest positions 9–12

## Outcome

PASS: 8/8 fixed direct answers pass. No content or provenance failure was found. Repository content was read-only; this receipt is the only artifact written.

- Campaign: `braintree-campaign-46`
- Query group: `C`
- Manifest positions: `9–12`
- Started at (UTC): `2026-10-07T23:44:40Z`
- Analysis ended at (UTC): `2026-10-07T23:45:50Z`
- Handoff at (UTC): `2026-10-07T23:46:28Z`

## Shared provenance and route checks

PASS — all four exact manifest pins resolve to the stated source target, canonical URL, and primary raw. Each raw path and canonical URL has exactly one source owner under `wiki/sources/`.

| Pos. | Job | Pinned raw SHA-256 | Result |
| ---: | --- | --- | --- |
| 9 | `docs-guides-payment-request-setup-and-integration-ios-v7` | `25c66f8f8139fcf6e518e0ef4fe3c051a72f134e7f5e3792c7d4dda644b644ae` | PASS — computed hash matches manifest |
| 10 | `docs-guides-payment-request-setup-and-integration-android-v5` | `1b259affc9bbd5939027897f29bf8011c19d1030ceff9cc0b4341e3e27107f22` | PASS — computed hash matches manifest |
| 11 | `docs-reference-response-us-bank-account-verification-node` | `11a4ec58fb3f36853598b5d227d387c25aa6016b7f9c812ded875cac2e6a2704` | PASS — computed hash matches manifest |
| 12 | `docs-guides-elo-client-side-android-v5` | `038ec73fa3d87b75086f224fb575720c19106a63020c514919db5813c33b4315` | PASS — computed hash matches manifest |

PASS — retrieval routes are reciprocal and provider-scoped:

- Root route: `wiki/index.md:11` → `[[braintree-index]]`.
- Payment Request routes (positions 9–10): `wiki/braintree-index.md:928` → `[[braintree-web-sdk]]`; concept backlinks at `wiki/concepts/braintree-web-sdk.md:82,84`; exact sources link back at source lines `30` and `33` respectively.
- US Bank Account Verification and Elo routes (positions 11–12): `wiki/braintree-index.md:919` → `[[braintree-payment-methods]]`; concept backlinks at `wiki/concepts/braintree-payment-methods.md:27,25`; exact sources link back at source lines `31` and `33` respectively.
- Every exact source has matching `canonical_url`, one matching `raw_files` owner, and a path-qualified `## Raw Sources` backlink.
- Exact direct catalog rows are not yet present in `wiki/braintree-index.md`; the dispatch contract explicitly defers direct catalog rows to coordinator close, so this is not a page failure.

Bounded filename/topic sweep: Payment Request surfaced the overview plus JavaScript v3 and the two pinned native-route captures; US Bank Account Verification surfaced only the pinned response reference; Elo surfaced overview/configuration/testing plus iOS, JavaScript, server-side, and the pinned Android route. None was needed to support a retained claim beyond the four pinned raws, so no older/sibling raw was promoted to evidence or automatically full-read.

## Position 9 — Payment Request setup and integration, iOS v7 route

Route: `wiki/index.md:11` → `wiki/braintree-index.md:928` → `wiki/concepts/braintree-web-sdk.md:84` → `wiki/sources/braintree/source-braintree-docs-guides-payment-request-setup-and-integration-ios-v7.md` → `raw/braintree/docs/guides/payment-request/setup-and-integration/ios/v7-2026-09-16.md`.

**Q1 — PASS.** Provider/document/product/SDK/version/environment/account/object/action scope: this is a Braintree-hosted `Setup and Integration` document whose canonical route and raw slug are iOS v7, while the only substantive availability statement says the Payment Request API is available with the JavaScript v3 SDK. No environment or account scope is stated, and no setup or integration action is documented on this capture. The route must not be treated as evidence of native iOS Payment Request behavior, any iOS SDK API or lifecycle, current availability, merchant enablement, buyer eligibility, or payment execution. Evidence: source `:6-8,14,18-20`; raw `:1,6-9,14,17-18,21-27`.

**Q2 — PASS.** The central purpose is scope triage/navigation: point the reader from a mismatched iOS v7 route to the JavaScript v3 Payment Request guide. The consequential warning is that the testing and Google Pay destinations are navigation only and contribute no behavior until independently read. The exact availability statement is retrievable at raw `:17-18`; the navigation-only destinations at raw `:21-27`; the route identity at raw `:7`. The source preserves these at `:18-26` without inventing a procedure.

## Position 10 — Payment Request setup and integration, Android v5 route

Route: `wiki/index.md:11` → `wiki/braintree-index.md:928` → `wiki/concepts/braintree-web-sdk.md:82` → `wiki/sources/braintree/source-braintree-docs-guides-payment-request-setup-and-integration-android-v5.md` → `raw/braintree/docs/guides/payment-request/setup-and-integration/android/v5-2026-09-16.md`.

**Q1 — PASS.** Provider/document/product/SDK/version/environment/account/object/action scope: this is a Braintree `Setup and Integration` page routed and slugged as Android v5, but its body only establishes Payment Request API availability through JavaScript v3. No environment, account qualification, native Android SDK dependency, request/result flow, nonce handoff, server processing, transaction action, or lifecycle is present. Do not infer Android support, current JavaScript support, merchant/buyer eligibility, enablement, exact SDK behavior, authorization, transaction creation, settlement, or funding. Evidence: source `:6-8,14,18,21-22`; raw `:1,6-9,14,17-18,23-29`.

**Q2 — PASS.** The central purpose/action is to route integration retrieval to the linked JavaScript v3 guide rather than supply an Android implementation. The material boundary is route/body mismatch plus navigation-only testing and Google Pay links. Exact locators: Android route identity raw `:7`; JavaScript v3 availability raw `:17-18`; related navigation raw `:23-29`. The source exposes the same precision at `:24-28`.

## Position 11 — US Bank Account Verification response, Node route

Route: `wiki/index.md:11` → `wiki/braintree-index.md:919` → `wiki/concepts/braintree-payment-methods.md:27` → `wiki/sources/braintree/source-braintree-docs-reference-response-us-bank-account-verification-node.md` → `raw/braintree/docs/reference/response/us-bank-account-verification/node-2026-09-16.md`.

**Q1 — PASS.** Provider/document/product/SDK/version/environment/account/object/action scope: this is a Braintree response-reference page on a Node route for the `Us Bank Account Verification` response object, and it states that the object is used for US Bank Account Verification. The route identifies neither an exact Node package nor a package version. No environment or account scope is stated. The object/action match is exact, but the reference is not evidence that verification occurred, that ownership was established, or that any payment was executed. It also does not establish containing response objects, fields, or behaviors because the captured list is empty. Evidence: source `:6-8,14,18-20`; raw `:1,6-9,14,20-24`.

**Q2 — PASS.** The central purpose is to identify the response object's use. The material warning says results are limited according to the linked PayPal Data Protection Addendum for Card Processing Products; the policy itself was not read, so no further policy interpretation is retained. Exact locators: identity/purpose raw `:14,20`; limitation notice raw `:17-18`; empty containing-response list raw `:21-24`. The source gives the same locators at `:22-26`.

## Position 12 — Elo client-side availability, Android v5 route

Route: `wiki/index.md:11` → `wiki/braintree-index.md:919` → `wiki/concepts/braintree-payment-methods.md:25` → `wiki/sources/braintree/source-braintree-docs-guides-elo-client-side-android-v5.md` → `raw/braintree/docs/guides/elo/client-side/android/v5-2026-09-16.md`.

**Q1 — PASS.** Provider/document/product/SDK/version/environment/account/object/action scope: this is a Braintree Elo `Client-Side Implementation` page at an Android v5 route. The body establishes only that Elo was in limited release for select merchants using the page-relative latest JavaScript v3 and server SDKs and that access could be requested through the contact route. It names no Android SDK behavior, no exact JavaScript/server package version, and no Sandbox or Production environment. Select-merchant access is the only account qualification. Do not infer Android support, exact SDK behavior, current Elo availability, merchant/environment enablement, payment execution, settlement, or funding. Evidence: source `:6-8,14,18-22`; raw `:1,6-9,14,17-18,22`.

**Q2 — PASS.** The central purpose/action is availability and access gating: Elo is limited to select merchants on the named SDK families, and the merchant is directed to contact Braintree to request access. The material warning is that `latest` is page-relative and unversioned, while the Android route is not Android implementation evidence. Exact locators: Android route raw `:7`; limited-release/select-merchant/SDK-family/access-request statement raw `:17-18`; server-side navigation raw `:22`. The source preserves these at `:24-28`.

## Completeness summary

- Four exact manifest jobs covered in order: positions `9, 10, 11, 12`.
- Two fixed questions answered for each page: `8/8` direct answers.
- Four pinned raws read completely; all four computed hashes match manifest.
- Queried object/action was checked against the reached authority for each page.
- Canonical URL, unique primary owner, main-concept reciprocity, and root/provider routing checked once.
- Bounded filename/topic gap sweep completed; no supporting raw was retained as evidence.
- Final verdict: `PASS` with no correction request.

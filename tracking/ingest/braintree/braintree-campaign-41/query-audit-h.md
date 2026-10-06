# Braintree C41 fixed-query audit H

- Assignment: positions 29-32; `docs-guides-fastlane-best-practices`, `in-person-get-started-1-account-structure`, `docs-reference-client-reference-javascript-v2-hosted-fields`, `docs-reference-general-currencies`
- Mode: read-only query audit; exactly two questions per page
- Content result: **8/8 PASS; no affected-question correction required**
- Analysis ended (UTC): `2026-10-06T15:22:28Z`
- Handoff written (UTC): `2026-10-06T15:22:28Z`

## Shared checks (recorded once)

- Manifest identity: **PASS, 4/4**. Each job ID, source target, canonical URL, pinned raw path and raw `Source URL` agree.
- Immutable evidence: **PASS, 4/4**. SHA-256 values match the manifest: Fastlane `f9e5a028...e8e3f`; account structure `8755b750...3476`; Hosted Fields `8ff22445...104e`; currencies `b3b877f8...92d3`.
- Promotion/ownership: **PASS, 4/4**. All four source targets exist, and each `raw_files` entry points to the selected manifest raw.
- Full selected-raw reads: **complete, 4/4**. No related raw was treated as evidence without a complete read.
- Bounded gap sweep: one shared filename/content sweep covered Fastlane, account structure, Hosted Fields and currencies. It found nearby product/version/account guides, but the selected raw fully answers all eight page-scoped questions. **Extra authority reads: none; not needed.**
- Root route: `wiki/index.md:5-11` -> `wiki/braintree-index.md`. Concept-to-source edges are present for all four pages.

## Deferred catalog-close notes (not content failures)

- `wiki/braintree-index.md` currently links `[[braintree-web-sdk]]` (`:658`) and `[[braintree-currencies]]` (`:651`), but has no direct `[[paypal-fastlane]]` or `[[braintree-in-person]]` concept edge. The Fastlane source remains reachable through `braintree-web-sdk -> paypal-fastlane`; the In-Person account source requires opening the existing `braintree-in-person` concept directly until aggregate close adds its provider-index edge. Per the C41 fixed policy, these are deferred catalog/index-edge items, not question failures.
- No new concept is required: `paypal-fastlane`, `braintree-in-person`, `braintree-web-sdk`, and `braintree-currencies` all exist and link their assigned source.

## 29. `docs-guides-fastlane-best-practices`

Actual route/page: `wiki/index.md:5-11` -> `wiki/braintree-index.md:658` -> `wiki/concepts/braintree-web-sdk.md:112` -> `wiki/concepts/paypal-fastlane.md:89-99` -> `wiki/sources/braintree/source-braintree-docs-guides-fastlane-best-practices.md` -> pinned raw `raw/braintree/docs/guides/fastlane/best-practices-2026-09-16.md`.

### Q1 — exact scope and non-inference

**Direct answer:** This is a collected, unversioned Braintree website best-practice guide for Fastlane guest-checkout buyer experience, member authentication/edit UX, browser-side integration recommendations, server-side profile-change handoff, and component styling/accessibility. It names no Braintree Web SDK or hosted-runtime version. Do not infer current availability, merchant enablement, buyer eligibility, authentication success, SDK compatibility, direct PayPal Orders API behavior, or authorization/capture/settlement/funding success.

**Object/action match:** The page's objects are Fastlane guest/member profile UI, client-SDK authentication/selectors, the returned nonce plus billing/shipping input, and styled Fastlane components. Its actions are recommendations/requirements for presentation, authentication refresh and handoff; a nonce/profile result is not a completed payment.

**Locators:** source `:12-16,20-28`; raw `:14-27,54-75,109-121` (especially unversioned page identity `:5-14`, Braintree handoff wording `:60-66`, WCAG requirement `:118-119`).

**Result: PASS.** Scope, modality and non-inference boundaries are explicit and raw-supported.

### Q2 — central purpose/action, conditions, warnings and detail route

**Direct answer:** The central purpose is to reduce guest/member checkout friction without removing buyer choice. The captured guide requires an upstream PayPal option, recommends email-first lookup, preserves other payment methods after authentication, calls for member address/card change controls, recommends loading the SDK at page load and calling `triggerAuthenticationFlow()` after reload, says profile changes apply only after nonce and billing/shipping information reach the stated Braintree server flow, and requires WCAG A/AA conformance. Its layout/conversion suggestions are guidance, not guarantees; exact selectors, style properties, contrast fallback and action sequence remain in raw.

**Object/action match:** `showAddressSelector()` changes address selection, `showCardSelector()` changes card selection, and `triggerAuthenticationFlow()` obtains/restores an authenticated customer result with a new nonce; none proves transaction execution.

**Locators:** source detail routes `:30-40`; raw PayPal choice/email `:17-27`, member UX/selectors `:29-49`, integration/handoff/refresh `:54-72`, styling and 4.5:1 fallback `:75-119`.

**Result: PASS.** Central actions, required-versus-recommended modality, consequential conditions and precise detail retrieval are all preserved.

## 30. `in-person-get-started-1-account-structure`

Actual route/page: `wiki/index.md:5-11` -> `wiki/braintree-index.md` (direct `braintree-in-person` edge deferred to aggregate close) -> `wiki/concepts/braintree-in-person.md:8-16` -> `wiki/sources/braintree/source-braintree-in-person-get-started-1-account-structure.md` -> pinned raw `raw/braintree/in-person/get-started-1/account-structure-2026-09-16.md`.

### Q1 — exact scope and non-inference

**Direct answer:** This collected, unversioned Braintree In-Person account-design guide documents the Gateway Account, Merchant Account ID (MAID), and virtual-only Location ID layers and their stated responsibilities. A gateway can contain multiple merchant accounts; merchant-account responsibilities include disbursement bank setup, settlement reporting, access/configuration and other listed account settings; readers pair to a Location ID, with one reader paired to one Location ID at a time. Do not infer configured accounts, current product/QR enablement, reader-online state, production readiness, or payment outcomes. Do not normalize the page's inconsistent second-model labels: prose says one MAID for all/multiple stores, while the table says merchant account for each brand and includes country/brand consequences.

**Object/action match:** Account tiers and Location IDs are configuration/reconciliation structures; reader pairing and QR enablement belong to the Location ID layer, while account design is not reader or transaction execution.

**Locators:** source `:12-23,25-34`; raw hierarchy `:19-86`, diagram/prose/table discrepancy `:91-105`.

**Result: PASS.** The promoted page preserves tier identity, pairing cardinality, the source discrepancy and outcome boundaries.

### Q2 — central purpose/action, conditions, warnings and detail route

**Direct answer:** The central action is choosing an In-Person account structure before go-live, using deposit aggregation, Amex contracts, reporting granularity, user permissions, store-opening cadence and legal-entity boundaries as decision inputs. The guide warns that the choice matters at initial setup and requires the final decision to be discussed with a PayPal Solutions Engineer or Integration Engineer. Production provisioning takes time and is separate from integration development. Exact tier functions, store/brand comparison outcomes and decision questions remain in raw.

**Object/action match:** The table compares account-design consequences; it does not instruct a universal store/brand mapping or prove production setup. Location-level reconciliation is routed elsewhere because Location ID does not appear in Braintree reporting.

**Locators:** source detail routes `:36-43`; raw comparison `:91-105`, decision warning/questions `:108-131`, go-live boundary `:136-138`; Location ID reporting boundary `:66-86`.

**Result: PASS.** Purpose, account-specific review requirement, source-label warning and exact detail routes are complete.

## 31. `docs-reference-client-reference-javascript-v2-hosted-fields`

Actual route/page: `wiki/index.md:5-11` -> `wiki/braintree-index.md:657-659` -> `wiki/concepts/braintree-web-sdk.md:78-94` -> `wiki/sources/braintree/source-braintree-docs-reference-client-reference-javascript-v2-hosted-fields.md` -> pinned raw `raw/braintree/docs/reference/client-reference/javascript/v2/hosted-fields-2026-09-16.md`.

### Q1 — exact scope and non-inference

**Direct answer:** This is the Braintree JavaScript **v2** Hosted Fields client reference for `onFieldEvent` UI/input state, detected-card metadata, iframe-internal CSS support, and Hosted Fields configuration. It does not document tokenization or server nonce handoff, certify PCI/security, assign current lifecycle status, prove Sandbox/Production availability, or prove any payment result. The version statement at raw `:149` applies only to the two tap-highlight CSS properties supported in v2.18.0+, not to every behavior on the page and not to JavaScript v3.

**Object/action match:** `onFieldEvent` observes field state, and field options configure Braintree-hosted inputs; `isValid` means fully qualified for submission, not tokenized, authorized or paid.

**Locators:** source `:12-22`; raw page/version identity `:5-17`, events `:17-57`, card type `:60-72`, styling/version qualification `:75-156`, options `:159-238`.

**Result: PASS.** SDK major, object/action scope and the narrow v2.18.0 qualification are correctly bounded.

### Q2 — central purpose/action, conditions, warnings and detail route

**Direct answer:** The page's purpose is to specify event data, allowed internal styling, and top-/field-level Hosted Fields options. `fieldStateChange` can report validity and nullable card-type metadata; unsupported iframe CSS fails with a console warning. Number and expiration are marked required only for creating/saving/using card data not already in the Vault; verification of a vaulted card may collect CVV alone. Every configured field requires a DOM `selector`; `placeholder` is optional. Exact callback shape, card metadata, CSS allowlist and selectors remain in raw.

**Object/action match:** Field-state/card-detection objects drive merchant UI behavior; configured selector/placeholder values create input presentation. They are not tokenization or transaction objects.

**Locators:** source detail routes `:24-30`; raw event object `:45-57`, card metadata `:60-72`, unsupported CSS warning and allowlist `:75-156`, required-field/Vault exception `:162-211`, selector/placeholder `:212-238`.

**Result: PASS.** The central reference purpose, consequential CSS/version/Vault conditions and retrieval locators are complete.

## 32. `docs-reference-general-currencies`

Actual route/page: `wiki/index.md:5-11` -> `wiki/braintree-index.md:648-652` -> `wiki/concepts/braintree-currencies.md:8-20` -> `wiki/sources/braintree/source-braintree-docs-reference-general-currencies.md` -> pinned raw `raw/braintree/docs/reference/general/currencies-2026-09-16.md`.

### Q1 — exact scope and non-inference

**Direct answer:** This collected Braintree general API-currency reference lists currency codes/names, marks its zero-decimal entries, records the Bulgaria BGN-to-EUR transition, and defines Braintree's scheme/exotic settlement-source categories. The list is qualified by account setup, company country and possible country-of-transaction restrictions. Do not infer current support, merchant/account/processor/payment-method eligibility, successful authorization or settlement, presentment/settlement pairings, exchange rates, or independent ISO/card-network authority.

**Object/action match:** A currency's appearance is reference/list membership; it is not account enablement or transaction acceptance. Scheme/exotic labels describe settlement sourcing, not merchant eligibility.

**Locators:** source `:12-24`; raw qualification `:14-17`, list/zero-decimal convention `:20-155`, Bulgaria transition `:160-161`, scheme/exotic definitions `:166-198`.

**Result: PASS.** The promoted page preserves exact reference scope and avoids eligibility or execution inference.

### Q2 — central purpose/action, conditions, warnings and detail route

**Direct answer:** The central purpose is retrieval of the page's qualified currency table and settlement-source categories. The consequential operational instruction is that, effective January 1, 2026, BGN is no longer supported for authorization or settlement and integrations using it for Bulgaria should use EUR. Asterisks identify the page's zero-decimal entries. Scheme currencies are supplied by the acquirer and/or card schemes for settlement; exotic currencies are sourced by Braintree instead. All uses remain account/country/restriction qualified, and the full tables stay in raw.

**Object/action match:** The only explicit integration change is BGN-to-EUR for Bulgaria; the other entries are reference data and settlement-source classifications, not proof of a runnable transaction route.

**Locators:** source detail routes `:26-32`; raw account/country qualification `:16-17`, table/asterisk `:20-155`, BGN action `:160-161`, scheme table `:166-185`, exotic table `:189-198`.

**Result: PASS.** Purpose, dated action, account qualifications, definitions and exact raw retrieval routes are all present.

## Close

- Successful content close: **yes, 8/8 PASS**.
- Material retrieval failure: **none**.
- Content correction: **none**.
- Deferred aggregate work: add/confirm provider-index routes for `paypal-fastlane` and `braintree-in-person` during C41 catalog close; do not treat those catalog edges as source-content failures.

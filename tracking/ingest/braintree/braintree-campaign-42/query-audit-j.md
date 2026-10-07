# Braintree C42 fixed-query audit J — positions 37–40

- Campaign: `braintree-campaign-42`
- Mode: read-only query audit
- Assigned jobs: manifest positions 37–40
- Required questions: 8 total, exactly 2 per page
- Analysis start (UTC): `2026-10-07T01:19:54Z`
- Analysis end (UTC): `2026-10-07T01:22:24Z`
- Result: **8 PASS / 0 FAIL** for content answers and retrieval

## Shared checks and bounded extra-evidence sweep

- Read `CLAUDE.md`, `rules/query-and-synthesis.md`, the complete C42 `manifest.json`, and `selection-review.md`. Followed the actual root/provider/main-concept/source/raw routes below. Fully read the four canonical sources and four pinned raws. Source `canonical_url` and `raw_files`, raw Source URL metadata, manifest identities, and computed SHA-256 values agree.
- Verified primary hashes: position 37 `18175cd710bd1fe7ce8eec22b0e1a0368210872cd15c76a6692dc9ccb70b8b93`; position 38 `fbfc8f39b876e70b2a3931ccc28ebe2f1243b1f7e46df6d996358d67d0300cd7`; position 39 `477f524ca3d36bf85296778431952a75b8191b12db434e77df33bae0e5f5ccaf`; position 40 `14010e3d43bbafe1b1014d6b80e1e1fa86f4ef600733ec5d2b9d9b6442005666`.
- Fully read one additional authority required by position 39's retained cross-page App Switch qualification: `wiki/sources/braintree/source-braintree-docs-guides-paypal-app-switch-ios-v7.md` and `raw/braintree/docs/guides/paypal/app-switch/ios/v7-2026-09-16.md`, SHA-256 `eeff8023bdc4193aebb980e54dc7193ae111ad18cc93a1066607a57e362d195a`. Its declared scope is the beta Braintree PayPal App Switch route for custom iOS v7 client integrations; it supplies the US/custom-integration eligibility and explicit vault/checkout opt-in conditions used below. The Vault source owns only its Vault raw, while the App Switch source owns only its App Switch raw; the Vault source's cross-source link is supporting provenance, not duplicate primary ownership.
- The bounded filename and related-reference sweep found Android/iOS/JavaScript siblings for Pay Later offers and messaging, Android Vault, PayPal Order payee-email, and six Node transaction-operation references. They were not needed for these exact-variant questions and were not used as evidence. No behavior was transferred from a current page, sibling platform/version, GitHub source, direct PayPal integration, or provider-wide assumption.
- Captured illustrative snippets include defects or incompleteness: the position-38 update fragment ends before a runnable closure and is labeled `java` while showing JavaScript-like content; the position-40 Swift examples contain malformed declarations/placement; the supporting App Switch Swift sample duplicates a label and omits a separator. These are nonblocking raw-quality observations because the retrieval entries do not claim that the examples compile, are copy-paste runnable, or prove current SDK behavior. No retained factual claim or runnable guarantee depends on repairing them.
- Bounded gaps remain explicit: position 37's prerequisite link routes to JavaScript v3 from an Android v5 page; position 38 has damaged sentences and an omitted deletion method; position 39's Vault page links App Switch detail to iOS v6 while the independently read iOS v7 App Switch page supplies the qualified opt-in evidence. None is reconstructed or silently resolved.

## Position 37 — `docs-guides-paypal-pay-later-offers-android-v5`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:718` → `wiki/concepts/braintree-android-sdk.md:78` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-pay-later-offers-android-v5.md` → `raw/braintree/docs/guides/paypal/pay-later-offers/android/v5-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a 2026-09-16 Braintree website snapshot on the Android v5 documentation route for PayPal Pay Later offers. Its client action is to set `PayPalCheckoutRequest.shouldOfferPayLater = true` so eligible customers can be shown Pay Later offers after PayPal login. Android v5 is a documentation family, not an exact package release; the page states no environment or account configuration and does not prove current product availability, merchant/buyer eligibility, that an offer appears, credit approval, authorization, capture, settlement, funding, or payment success. The captured JavaScript v3 prerequisite destination is not Android behavior authority.

Locators: source lines 12–22; raw identity and product scope lines 1–18; availability qualification lines 30–32; Android request action lines 44–53.

### Q2 — central action, conditions, warnings, and detail route — PASS

The central action is an eligibility-conditioned presentation request. Consumer products, ranges, terms, APR/interest and regulatory or credit conditions vary by country; merchant eligibility separately depends on location and integration. The page requires a prior PayPal client-side integration but its captured link points to JavaScript v3, so that mismatch remains unresolved. Additional Pay Later messaging was unavailable in the snapshot, merchants are told not to create promotional wording/material, and PayPal reserves action under the User Agreement. Country values, the prerequisite destination, request flag and exact warning remain retrievable in the pinned raw.

Locators: source lines 18–31; raw country table lines 18–28; consumer/merchant qualification lines 30–32; prerequisite mismatch lines 37–42; request flag lines 44–53; messaging prohibition lines 55–57.

## Position 38 — `docs-reference-general-paypal-advanced-options-paypal-order-server-side-node`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:729` → `wiki/concepts/paypal-braintree-integration.md:56` → `wiki/sources/braintree/source-braintree-docs-reference-general-paypal-advanced-options-paypal-order-server-side-node.md` → `raw/braintree/docs/reference/general/paypal-advanced-options/paypal-order/server-side/node-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a Braintree-hosted Node-routed website reference for server actions after successful PayPal authentication of a PayPal Order: create a Vault customer/payment method or attach one to an existing customer, optionally update the approved PayPal payment resource before vaulting, use Braintree transaction-operation routes, and delete the representing payment method to void the Order. It names no exact Node SDK package/version and no environment. It is not direct PayPal Orders API authority, a complete parameter/method contract, merchant eligibility evidence, or proof of successful authentication, vaulting, authorization, settlement, funding, refund, void, or payment execution.

Locators: source lines 12–28; raw page/action scope lines 14–22; customer-create/update examples lines 20–81; payment-resource update boundary lines 82–90; transaction navigation lines 159–167; void boundary lines 192–194.

### Q2 — central action, conditions, warnings, and detail route — PASS

After buyer authentication, the merchant creates or attaches the nonce-backed payment method. If approved transaction data changes, `PayPalPaymentResource.update()` occurs after tokenization and before `Customer.create()`; a changed total requires updated line items, and the returned replacement nonce—not the original—must be used for vaulting. Currency follows the `merchant_account_id` in the transaction call; a shipping address may make Seller Protection eligibility possible, but neither it nor the displayed `ELIGIBLE` value guarantees protection. Deleting the payment method is the documented consequential void path, while the captured deletion method name is missing. Exact sample fields and transaction-operation schemas stay routed to the pinned raw and separately listed unread references.

Locators: source lines 18–41; raw update timing/line-item condition lines 82–90; displayed optional update fields lines 93–157; transaction routes lines 159–167; currency and conditional Seller Protection lines 170–190; missing deletion invocation lines 192–194.

## Position 39 — `docs-guides-paypal-vault-ios-v7`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:719` → `wiki/concepts/braintree-ios-sdk.md:83` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-vault-ios-v7.md` → `raw/braintree/docs/guides/paypal/vault/ios/v7-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a collected Braintree website guide on the iOS v7 route for PayPal Vault tokenization. The app creates a `BTPayPalVaultRequest`, calls `BTPayPalClient.tokenize`, and sends a successful payment-method nonce to its server for separate transaction creation so the PayPal account can be charged later. It is a Braintree nonce/Vault flow, not direct PayPal Payment Method Tokens or Orders API vaulting. The route is not an exact iOS SDK package release; it states no proven environment/account enablement and does not establish current support, buyer eligibility, successful tokenization, a stored method, authorization, settlement, funding, or payment execution.

Locators: source lines 12–22; raw Vault purpose/use cases lines 14–50; request/tokenization/nonce handoff lines 53–93.

### Q2 — central action, conditions, warnings, and detail route — PASS

The central action is vault-request tokenization followed by merchant-server nonce use. The snapshot retains a dated March 30, 2026 certificate warning and iOS `6.17.0+` instruction without converting it into current v7/package status. Device data is required for non-recurring transactions initiated from Vault records. The Vault page broadly says the SDK attempts App Switch after `tokenize` when the app/user qualify, but the separately read iOS v7 beta/setup authority limits eligibility to US merchants/customers with custom client integration and requires `enablePayPalAppSwitch: true` plus `userAuthenticationEmail`; otherwise `ASWebAuthenticationSession` is the documented fallback. This supporting page does not replace or duplicate the Vault raw. Shipping collection is optional, while amount and currency must be displayed elsewhere by the merchant.

Locators: source lines 18–30; Vault raw certificate warning lines 19–22; tokenization branches lines 62–93; device-data requirement lines 95–97; broad App Switch statement/fallback and iOS v6 link lines 100–123; shipping and amount/currency lines 126–138; supporting App Switch source lines 14–28 and 32–40; supporting raw eligibility lines 23–40 and explicit opt-in lines 200–256.

## Position 40 — `docs-guides-paypal-messaging-ios-v7`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:719` → `wiki/concepts/braintree-ios-sdk.md:85` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-messaging-ios-v7.md` → `raw/braintree/docs/guides/paypal/messaging/ios/v7-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is a 2026-09-16 Braintree website guide on the iOS v7 route for displaying PayPal Pay Later messaging in a native iOS app. The action is to create an authorized `BTAPIClient`, a `BTPayPalMessagingView` and `BTPayPalMessagingRequest`, place the view, and call `start`; optional delegate callbacks describe message lifecycle. Although the page says latest iOS/Android SDKs, it names no exact iOS package release, excludes Drop-in, and is not sibling-platform or current-package authority. It does not prove merchant/customer eligibility, runtime rendering, a displayed or approved offer, credit approval, nonce creation, or payment execution.

Locators: source lines 12–22; raw identity/availability lines 1–22; invocation and illustrative view/request flow lines 65–107; optional delegate lifecycle lines 108–136.

### Q2 — central action, conditions, warnings, and detail route — PASS

The central action is rendering customized Pay Later offer messaging for an eligible one-time PayPal checkout integration. Captured eligibility is limited to eligible merchants in US, GB, DE, FR, IT, ES and AU who are current Braintree merchants, use the latest Braintree integration/native SDK, and have Pay Later options available. Merchants must follow the Acceptable Use Policy, must not add encouraging content/marketing to messages, and face category exclusions such as Real Money Gaming plus possible later exclusions. Exact dependency routes, request arguments/defaults, view layout/start details and delegate methods remain in the pinned raw; the malformed illustrative Swift does not create a runnable-code guarantee.

Locators: source lines 18–31; raw availability/eligibility and policy restrictions lines 17–38; dependencies lines 41–62; view/request/start example lines 65–107; argument/default tables and delegate reference lines 138–193.

## Deferred catalog/index closure — separate from content failures

- All four new source pages have reciprocal entries in provider-indexed main concepts now: `braintree-android-sdk` for position 37, `paypal-braintree-integration` for position 38, and `braintree-ios-sdk` for positions 39–40.
- Direct source-catalog entries for all four are not yet present in `wiki/braintree-index.md`. Coordinator-owned aggregate close should add/check them. This deferred catalog work does not change the **8 PASS / 0 FAIL** content result.
- No new company or provider source-catalog page is needed from this audit, and no source expansion or correction is requested.

## Handoff

- Corrections requested: none.
- Content blockers: none.
- Closure follow-up: add/check the four direct provider source-catalog entries during coordinator close.
- Repository files modified by this audit: none.

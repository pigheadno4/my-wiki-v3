# Braintree C41 fixed-query audit F — positions 21–24

- Campaign: `braintree-campaign-41`
- Mode: read-only query audit
- Assigned jobs: positions 21–24
- Required questions: 8 total, exactly 2 per page
- Analysis end (UTC): `2026-10-06T15:18:45Z`
- Result: **8 PASS / 0 FAIL** for content answers and retrieval

## Shared checks and bounded extra-evidence sweep

- Read `CLAUDE.md`, `rules/query-and-synthesis.md`, and the C41 fixed allocation in `selection-review.md` before auditing.
- Followed the root/provider/concept/source/raw chain. `wiki/index.md:5-11` routes to `wiki/braintree-index.md`; existing provider concept edges are `braintree-payment-platform` at `wiki/braintree-index.md:648` and `braintree-web-sdk` at `wiki/braintree-index.md:658`.
- Manifest identity, canonical URL, source `raw_files`, raw Source URL metadata, and pinned SHA-256 all match:

| Position | Job | Verified SHA-256 |
| ---: | --- | --- |
| 21 | `docs-reference-client-reference-javascript-v2-paypal` | `ae7ba8e46c0a4e572eb71e5d410d11f2f943dbca5d0ff70858ba47146c32de0f` |
| 22 | `docs-guides-paypal-commerce-channel-api-ordering-a-product` | `2c410e23d45e5e6f21e3833aaece6ff4ffba212b501d1a5901d74334bd8eed4c` |
| 23 | `in-person-reference-general-payments-terminology` | `39dbb037c531f47d87ee491362dcd415cec8d09fdd914cc21dec7bec3402c9a1` |
| 24 | `docs-guides-package-tracking-overview` | `80ee751cccf2d5648450138340c12f711367ed5595022ee3ddfb9c4547ced212` |

- Fully read all four source pages and all four pinned raws. The bounded filename/related-raw sweep found adjacent JavaScript-v2 references, Channel API access-token/error guidance, In-Person operational guides, and package-tracking client/server guides. None is needed for these eight fixed questions, so no extra full authority was read.
- Bounded gaps: the legacy PayPal raw has a rendering omission in the `authorize` description at raw line 55, so the missing option/call name must not be reconstructed. The package-tracking raw links to an external carrier inventory at raw line 97, but no collected carrier-inventory raw was found; the selected page supports the carrier-field rule, not an exact carrier enumeration.

## Position 21 — `docs-reference-client-reference-javascript-v2-paypal`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:658` → `wiki/concepts/braintree-web-sdk.md:78-86` → `wiki/sources/braintree/source-braintree-docs-reference-client-reference-javascript-v2-paypal.md` → `raw/braintree/docs/reference/client-reference/javascript/v2/paypal-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This is the collected Braintree.js **JavaScript v2** browser-client PayPal option reference for Vault and Checkout with PayPal. Its object is the nested `paypal` configuration used in Custom or Drop-in setup, plus presentation options and client callbacks; it is not JavaScript v3, PayPal Web SDK v6, a server transaction API, or evidence of current SDK support, environment availability, account enablement, authorization, settlement, or successful execution. Object/action match is exact: configure the v2 PayPal client flow and receive its callback data/nonce, not process the payment server-side.

Locators: source lines 12–22; raw identity lines 1–9; Vault/Checkout and nesting lines 17–22; version-qualified `intent` and callbacks lines 41–83; headless boundary lines 265–281.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The page's central purpose is to define PayPal client options. `singleUse` defaults to false and true selects Checkout; Checkout requires `amount` and `currency`; `intent` is available only from v2.25.0. `authorize` does not submit for settlement, while `sale` submits for settlement when the transaction is created. `onSuccess` is deprecated and signals PayPal login, not form submission; billing-address output additionally requires the account feature and is not available to every merchant. Headless mode requires merchant UI and nonce retrieval from `onPaymentMethodReceived` and does not work with Drop-in. Do not infer capture/settlement from login, callback, or nonce generation.

Locators: source lines 18–32; raw option table lines 41–83, address conditions lines 85–204, Checkout inputs/locale lines 205–264, and headless/billing-agreement details lines 265–281. The malformed omission at raw line 55 remains an explicit evidence gap rather than an inferred identifier.

## Position 22 — `docs-guides-paypal-commerce-channel-api-ordering-a-product`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:648` → `wiki/concepts/braintree-payment-platform.md:26-30` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-commerce-channel-api-ordering-a-product.md` → `raw/braintree/docs/guides/paypal-commerce-channel-api/ordering-a-product-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This unversioned collected Braintree website guide covers a **channel** ordering one retailer product variant for a user through the PayPal Commerce Channel API. The objects/actions are a Braintree SDK `payment_method_token`, shipping address, full-cost variant lookup, channel-and-retailer-specific customer access token, and `order` creation/initiation. Examples use `commerce.sandbox.braintreegateway.com`; they do not establish a current API/SDK version, production availability, merchant/channel eligibility, payment approval, fulfillment completion, settlement, or funding.

Locators: source lines 12–22; raw identity lines 1–9; flow/payment token lines 14–27; customer-scoped token lines 149–182; order object and sandbox request lines 183–223.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The documented action sequence is: collect/store the payment token, obtain the shipping address, preview the full cost, obtain a customer access token, then initiate the purchase. The guide strongly recommends presenting full cost before order creation because omission can cause confusion, chargebacks, and poor UX. Destination fields are required for the preview; promo codes are optional; shippability, tax, shipping, discount, unsupported-code 404, and unknown-SKU 404 behavior are captured. Purchase initiation requires the customer token and an `order` carrying partner order ID, variant, shipping address, vaulted-method token, and optional promo codes. HTTP 201 plus transmission to the retailer's ecommerce system and `ready to fulfill` do not prove fulfillment or downstream payment lifecycle outcomes; failures are only bounded here as 400–499 and route to separate error guidance.

Locators: source lines 18–31; raw shipping schema lines 28–42; full-cost conditions/examples lines 45–147; token lines 149–182; order request lines 183–223; response, warning, and retailer handoff lines 224–248.

## Position 23 — `in-person-reference-general-payments-terminology`

Actual retrieval route/page: `wiki/index.md:11` → `wiki/braintree-index.md` → filesystem-located `wiki/concepts/braintree-in-person.md:8-21` → `wiki/sources/braintree/source-braintree-in-person-reference-general-payments-terminology.md` → `raw/braintree/in-person/reference/general-payments-terminology-2026-09-16.md`. The missing provider-index edge to `braintree-in-person` is a deferred catalog-close item, recorded below, not a content-answer failure.

### Q1 — exact scope and non-inference — PASS

This is a collected, unversioned Braintree **In-Person terminology glossary** spanning payment-industry terms, omni-channel merchant systems, and provider-specific reader/tokenization/vaulting/offline vocabulary. It is not an API schema, transaction-state contract, certification record, or operational support/availability proof. The glossary does not define authorization, capture, sale, settlement, refund, void, reversal, or In-Store Context semantics; example mentions of capture or referenced refunds must not be promoted into lifecycle rules.

Locators: source lines 12–22; raw identity lines 1–9 and purpose line 16; section boundaries at raw lines 19, 32, and 43; raw OMS/tokenization examples at lines 37 and 48.

### Q2 — purpose, conditions, warnings, and detail route — PASS

Its central purpose is orientation: it defines PCI/E2EE/P2PE/EMV/network/interchange terms; POS, PMS, OMS, ERP, call-center and ecommerce systems; and Braintree reader, GraphQL communication, tokenization, vaulting, NFC, QR wallet, Store and Forward, offline-floor-limit, and safety-stock terms. Snapshot-specific claims require caution: the raw says the Braintree solution is E2EE and was then undergoing P2PE certification, which is not current certification proof. Tokenization and vaulting remain distinct, and glossary links to GraphQL, vaulting, QRC, offline, and solution-coverage pages are navigation only unless read separately.

Locators: source lines 18–32; raw payment-industry terms lines 19–29; omni-channel systems lines 32–40; Braintree terms lines 43–55; navigation-only links line 57.

## Position 24 — `docs-guides-package-tracking-overview`

Actual route/page: `wiki/index.md:11` → `wiki/braintree-index.md:648` → `wiki/concepts/braintree-payment-platform.md:26-30` → `wiki/sources/braintree/source-braintree-docs-guides-package-tracking-overview.md` → `raw/braintree/docs/guides/package-tracking/overview-2026-09-16.md`.

### Q1 — exact scope and non-inference — PASS

This collected, unversioned Braintree package-tracking overview covers online tangible-goods merchants adding line-item data at order creation and adding carrier tracking to eligible PayPal transactions after settlement and shipment. The key objects/actions are order line items, transaction/child-transaction ID, required `tracking_number` and `carrier`, optional payer notification and line items, and returned transaction `packages`. It does not prove present SDK support, integration qualification, shipment/delivery, PayPal App display, dispute resolution, hold release, seller-protection coverage, or authorization/capture/settlement/funding outcomes.

Locators: source lines 12–24; raw identity lines 1–9; availability lines 26–44; eligibility lines 51–59; API sequence lines 70–89; tracking request/response lines 91–125.

### Q2 — purpose, conditions, warnings, and detail route — PASS

The central workflow is to add line items when creating the order, then add tracking after the transaction settles. Qualification must be checked with the Braintree Account Manager; captured minimum client/server SDK versions and country list are snapshot conditions, not current package-version or enablement proof. Eligibility is restricted to online physical-goods merchants accepting branded PayPal payments in the listed consumer countries, excluding in-store and digital-goods/services sellers; branded-PayPal scope specifically governs automatic dispute resolution and PayPal App updates. If a transaction was submitted for partial settlements, use the child transaction ID. `tracking_number` and `carrier` are required, `notify_payer` defaults false, paired UPC fields have mutual requirements, and `paypal_tracker_id` may be delayed. Claimed experience/dispute/hold benefits are conditional provider statements, not outcome proof.

Locators: source lines 20–39; raw overview/benefits lines 16–23; availability/version tables lines 26–44 and 128–146; eligibility lines 51–59; item schema lines 70–84; request schema lines 86–112; response lines 115–125. The exact carrier enumeration remains outside the captured raw at the external link on raw line 97.

## Deferred catalog/index closure — separate from content failures

- `wiki/braintree-index.md` does not yet link the new `[[braintree-in-person]]` concept. Add that provider-index concept edge during the coordinator-owned aggregate close.
- The four approved source pages are linked from their concept pages, but their direct provider source-catalog entries are not yet present in `wiki/braintree-index.md`. This is consistent with the C41 instruction to aggregate catalog/index changes once at close.
- No new concept is required by the four audited pages beyond the already-created `braintree-in-person` retrieval entry.
- These deferred edges do not change the **8 PASS / 0 FAIL** content result; however, the position-23 root-to-source route remains incomplete until the provider-index edge is added.

## Handoff

- Corrections requested: none.
- Content blockers: none.
- Closure follow-up: provider-index/catalog edges above.
- Handoff UTC: `2026-10-06T15:19:57Z`

# Braintree C44 fixed-query audit — group C

- Scope: approved C44 jobs 9–12 only; eight predetermined queries.
- Result: **PASS — 8/8 queries**.
- Completed UTC: `2026-10-07T12:34:37Z`

## Shared checks

- Manifest/job state: all four jobs are `approved` at attempt 1 and map to the canonical source targets audited below.
- Integrity/provenance: all four computed SHA-256 values exactly match the manifest. Within the manifest, each raw path, SHA-256, canonical URL and source target is unique. Each raw begins with the same canonical `Source URL` as the manifest/source frontmatter, a `Fetched: 2026-09-16` marker, and `Discovery: llms.txt,sitemap.xml`.
- Primary ownership: each exact `raw_files` path occurs in exactly one `wiki/sources/` page; each canonical URL also occurs in exactly one source page. `## Raw Sources` points to the same pinned primary raw. No supporting raw claims primary ownership.
- Retrieval closure: `wiki/index.md:11` routes to `[[braintree-index]]`; the provider index routes to `[[braintree-payment-methods]]` (`wiki/braintree-index.md:813`) and `[[braintree-ios-sdk]]` (`:825`). Those concepts reciprocally list the four sources at `wiki/concepts/braintree-ios-sdk.md:92` and `wiki/concepts/braintree-payment-methods.md:23,58,158`. Direct provider-catalog source rows are absent, but this is the explicitly deferred shared-catalog close and is not a failure while the concept routes work.
- Bounded gap sweep: one filename/topic sweep covered PayPal Commerce iOS product cards/overview/setup, PINless debit optimized-routing integration/test/sample, UnionPay overview/client/testing, and SEPA Direct Debit overview/client/server/vault/testing. The four primary raws fully answer the fixed queries; no supporting raw was needed for a retained claim or conflict, and no unrelated fan-out was performed.

## 1. PayPal Commerce iOS Product Cards

Source: `wiki/sources/braintree/source-braintree-docs-guides-paypal-commerce-ios-product-cards.md`; primary raw: `raw/braintree/docs/guides/paypal-commerce-ios/product-cards-2026-09-16.md` (`533dad596cc24331a71c9cffbf18b6f5f872fda9d42ce6834ba4de3d80f418f8`).

**Q1 — exact scope. PASS.** This Braintree-hosted, unversioned **Product Cards** webpage belongs to the historical PayPal Commerce iOS SDK family and covers product presentation in a content-based iOS app. Its objects are SDK-provided `PPCProductCardView` views populated from a search term or product-group ID and a fetched `PPCProduct`; its actions are adding a card view, fetching a product, and initiating purchase through the card button or `purchaseProduct:` after an app-owned user action. It names no SDK release, environment, account/merchant eligibility, current availability, or completed purchase, and it must not be transferred to the modern modular `braintree-ios` package. Locators: source `:14-16,20-22,35-38`; raw `:1-9,17-22,23-47,53-67`.

**Q2 — purpose, action, conditions/warnings, detail route. PASS.** The central purpose is to embed an API-populated product card or use app-owned UI to display a fetched product and initiate its purchase. A product card displays name, image, description, cost and a buy button; the factory examples take either a search term or group ID and expose a `BOOL success`/`NSError` completion. The custom-UI example fetches by group ID and calls `[PayPalCommerce purchaseProduct:product]` only after the user initiates the purchase. The page says “initiates,” not “completes,” and the illustrated confirmation/receipt path is not runtime or payment proof. Exact detail routes: source `:20-30`; raw `:17-22` (purpose/display/action), `:23-47` (two factories), `:50-52` (illustrated card flow), `:53-67` (custom fetch/purchase), `:69-71` (illustrated custom-UI flow).

## 2. PINless Debit Optimized Routing — GraphQL Code Sample

Source: `wiki/sources/braintree/source-braintree-docs-guides-pinless-debit-optimized-debit-routing-code-samples-graphql.md`; primary raw: `raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/code-samples/graphql-2026-09-16.md` (`d67ffc4ae00f37e57f94546e9ba046c4bd616da6910ffc90a2df42d34d31a921`).

**Q1 — exact scope. PASS.** This is Braintree's unversioned GraphQL code-sample webpage for searching transactions associated with PINless debit optimized routing. The document says retrieval can use transaction ID or debit network, while the displayed operation covers only `search.transactions(input: $input)` with a `TransactionSearchInput!`, a `debitNetwork.is` example and creation-time bounds. It identifies no endpoint, credentials, headers, client/server owner, SDK/package/version, environment, account enablement or returned result. Therefore it is not current schema/enum validity, universal `STAR` availability, matching-transaction, payment, settlement or funding proof. Locators: source `:14-16,20-23`; raw `:1-9,14-16,19-23,196-209`.

**Q2 — purpose, action, conditions/warnings, detail route. PASS.** The purpose is to illustrate retrieval of optimized-routing transaction records and their selected details. The shown variables combine `debitNetwork.is: STAR` with an inclusive `createdAt` window; these are example values, and the operation-level non-null marker does not establish required nested inputs. The selection asks for page metadata and transaction nodes spanning identity/status/source, `debitNetwork`, amount, merchant/order/customer, disbursement, risk, facilitator, status-history event fragments, card snapshot, custom fields and processor response. The page supplies no transaction-ID variables example and no runnable setup. Exact detail routes: source `:20-30`; raw `:14-16` (stated search choices), `:19-194` (operation, pagination and exact projection), `:196-209` (example network/time variables).

## 3. UnionPay Testing

Source: `wiki/sources/braintree/source-braintree-docs-guides-unionpay-testing.md`; primary raw: `raw/braintree/docs/guides/unionpay/testing-2026-09-16.md` (`ed6bf50a21127bc9152d8d12ee061dc55e3223cb378d4beb272814e634960367`).

**Q1 — exact scope. PASS.** This Braintree-hosted, unversioned **Testing** webpage is a Sandbox fixture reference for the deprecated dedicated UnionPay integration. Its objects are test card numbers and verification/enrollment fields; its action scope is simulating named card and input-error scenarios. It identifies no client/server SDK or version and no merchant-account enablement. It must not be generalized to Production, the replacement credit-card-through-Discover path, current availability, or an executed payment. Locators: source `:14,18-22`; raw `:1-9,17-18,21-46`.

**Q2 — purpose, action, conditions/warnings, detail route. PASS.** The central purpose is to supply dedicated-flow Sandbox test inputs. The card table includes debit, credit, unsupported, not-online-activated, no-SMS-verification and 14–19-digit cases. The captured `does not support separate****calls` phrase is malformed and is correctly retained without interpretation. Additional verification/enrollment simulations use `smsCode: 999999` for an incorrect customer-entered code and an `expirationYear` or `expirationDate` before 2010 for an expired card. The consequential warning is the page's own deprecation redirect; it does not say these fixtures apply to the Discover credit-card route. Exact detail routes: source `:18-28`; raw `:17-18` (deprecation/redirect), `:21-36` (card fixtures), `:39-46` (special error inputs).

## 4. SEPA Direct Debit Client-Side — iOS v7 route

Source: `wiki/sources/braintree/source-braintree-docs-guides-sepa-direct-debit-client-side-ios-v7.md`; primary raw: `raw/braintree/docs/guides/sepa-direct-debit/client-side/ios/v7-2026-09-16.md` (`6b6ad41427b113d7cd41988bd1fa6bfd18b6850a6bb1a73e0a99b518b5087799`).

**Q1 — exact scope. PASS.** This is Braintree's iOS v7-routed client-side SEPA Direct Debit implementation webpage. It states an iOS v5.11+ SDK-family floor, eligible-merchant/custom-client scope, Drop-in exclusion, and separate enablement for a Sandbox or Production account. It names the `Braintree/SEPADirectDebit`, `BraintreeSEPADirectDebit` and (for Carthage) `BraintreeCore` modules/frameworks but no exact package release. Its objects are collected bank/customer fields, `BTSEPADirectDebitClient`, `BTSEPADirectDebitRequest`, a displayed mandate and the returned nonce; its action is client tokenization followed by nonce handoff to the merchant server. It is not proof of current support, mandate acceptance, server processing, debit success, settlement or funding. Locators: source `:14-16,20-26`; raw `:1-9,17-20,25-59,60-101`.

**Q2 — purpose, action, conditions/warnings, detail route. PASS.** The page's central action is to collect `accountHolderName`, `iban`, `billingAddress` and merchant-system `customerID`, construct the client/request, and call `tokenize(_:completion:)`; the prose says that launches the flow, creates and displays a mandate, and tokenizes the payment method. The Swift example uses `.oneOff`, sends the nonce server-side only on its success branch, and separately handles web-flow cancellation/other errors. `.oneOff` is an example, not a universal mandate type, and tokenization is not transaction success. The raw Swift contains illustrative naming/assignment defects, but the source does not promise runnable code and makes no false claim from them, so they are nonblocking. Exact detail routes: source `:20-34`; raw `:31-45` (module/framework setup), `:46-54` (required inputs), `:57-59` (documented action), `:60-101` (illustrative request, mandate type, callback and server handoff).

## Query tally

| Page | Q1 exact scope | Q2 purpose/actions/conditions/detail route |
| --- | --- | --- |
| PayPal Commerce iOS Product Cards | PASS | PASS |
| PINless Debit Optimized Routing GraphQL Sample | PASS | PASS |
| UnionPay Testing | PASS | PASS |
| SEPA Direct Debit Client-Side (iOS v7 route) | PASS | PASS |

Concrete uncertainty retained: the UnionPay primary raw's malformed `separate****calls` phrase and the SEPA primary raw's illustrative Swift naming/assignment defects. Neither supports a retained false claim, material misuse or runnable guarantee, so neither causes a query failure. No other material uncertainty remains after the single completeness pass.

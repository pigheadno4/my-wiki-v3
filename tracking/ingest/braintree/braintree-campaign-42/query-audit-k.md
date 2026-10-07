# Braintree C42 fixed-query audit — Group K

- Campaign: `braintree-campaign-42`
- Assigned manifest positions: 41–44
- Started (UTC): `2026-10-07T01:24:24Z`
- Completed (UTC): `2026-10-07T01:26:07Z`
- Verdict: **PASS — 8/8 fixed questions passed**

## Shared checks

- The four pinned raws and canonical source pages were read completely. Recomputed SHA-256 values match the manifest: PayPal Messaging Android `29642f77b5d33e0ca8dbeec1320523dccfa9b561e7cb1da2abe6156bef909cd0`; server-side tokenization Node `c49f18facad37481afc0bd761cd11be07de8f5de19eb9f0e8892920a19f694ce`; Masterpass JavaScript v3 `12763b2331aba2a0a51bae162c32610f9bcd38ec8f52e6a20a31cfa97459e226`; Google Pay Android v5 `0a8a19f836a164201b6966e52d06126e7d8192dfa5ad5db180d4ac2d785adeed`.
- For every page, manifest URL = source `canonical_url` = raw line-1 Source URL; `raw_files` and `## Raw Sources` identify the pinned raw, and reverse ownership lookup finds exactly one canonical source.
- The common entry is `wiki/index.md:11` → `[[braintree-index]]`. Provider-to-concept links are present at `wiki/braintree-index.md:707,715,718`; each selected source links its main concept and each main concept links back to that source. Direct provider-index source rows and company/catalog aggregates are deferred coordinator-close work, not retrieval failures.
- The bounded filename/URL sweep found the exact pins plus distinct PayPal Messaging, Masterpass, and Google Pay sibling/platform pages; no sibling behavior was imported. The Masterpass warning required one extra full authority read, `source-braintree-payment-methods-secure-remote-commerce.md` and its pinned raw, which confirms the unresolved current-tense limited-release versus January 20, 2026 end-of-support conflict at raw `:14-25,28-48,88-90`. No other navigation-only authority was needed.

## Position 41 — `docs-guides-paypal-messaging-android-v5`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:718` → `wiki/concepts/braintree-android-sdk.md:76` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-messaging-android-v5.md:1-46` → `raw/braintree/docs/guides/paypal/messaging/android/v5-2026-09-16.md:1-180`.

1. **PASS — Exact scope, eligibility, and non-inference.** This is a 2026-09-16 Braintree Android v5-routed website guide for adding PayPal Pay Later offer messaging to eligible native-app merchants. Its captured availability excludes Drop-in; eligibility names US, GB, DE, FR, IT, ES, and AU plus Braintree/latest-integration/native-SDK/one-time-PayPal-checkout and Acceptable Use Policy conditions. It does not prove current SDK support, merchant/buyer eligibility, offer or credit approval, checkout, authorization, settlement, or funding. Evidence: source `:12-22`; raw `:17-40`.
2. **PASS — Central action, warnings, and detail route.** The captured example adds `paypal-messaging:5.0.0`, creates a request and view, calls `start()`, inserts the view, and permits optional re-rendering; the optional listener reports only messaging lifecycle events. The source preserves the constructor conflict (`authorization` in prose/example versus `braintreeClient` in the table), callback-name conflict (`Failure` versus `Error`), and damaged `pageType` table. Illustrative syntax defects do not become a runnable-code guarantee. Exact construction, callbacks, fields, and defaults remain at source `:24-37` and raw `:43-178`.

## Position 42 — `docs-guides-server-side-tokenization-node`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:715` → `wiki/concepts/braintree-server-sdk.md:49` → `wiki/sources/braintree/source-braintree-docs-guides-server-side-tokenization-node.md:1-48` → `raw/braintree/docs/guides/server-side-tokenization/node-2026-09-16.md:1-161`.

3. **PASS — Exact scope and non-inference.** This is an unversioned Braintree website Node route for creating a non-vaulted, single-use payment method from raw card details through the GraphQL client on a configured gateway. The result ID is used as a typical nonce, but tokenization is not authorization, card verification, Vault storage, transaction success, settlement, or funding; the page also does not establish a package-qualified implementation, exact schema baseline, Production availability, merchant enablement, or PCI scope. Evidence: source `:12-25`; raw `:17-25,87-133,135-161`.
4. **PASS — Central action, material gap, and detail route.** The retained sequence builds `TokenizeCreditCardInput`, calls `gateway.graphQLClient.query(query, variables)` in callback or Promise form, and reads `result.data.tokenizeCreditCard.paymentMethod.id`. The central query-definition block is literally `undefined`, so the source correctly refuses to reconstruct a mutation, selection set, required fields, or runnable contract and warns that the raw-card walkthrough contains no PCI qualification. Exact inputs, invocation, response example, and Explorer iteration route remain at source `:18-34` and raw `:28-85,87-161`.

## Position 43 — `docs-guides-masterpass-client-side-javascript-v3`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:707` → `wiki/concepts/braintree-payment-methods.md:23` → `wiki/sources/braintree/source-braintree-docs-guides-masterpass-client-side-javascript-v3.md:1-44` → `raw/braintree/docs/guides/masterpass/client-side/javascript/v3-2026-09-16.md:1-212`.

5. **PASS — Exact historical scope and support boundary.** This is a Braintree JavaScript v3 website snapshot for a legacy Masterpass component, with captured `3.88.1` client and Masterpass script examples. The page says Masterpass was replaced by SRC and describes SRC as limited release, API-change-qualified, eligibility-gated, and access-requested. The canonical source correctly treats this as historical evidence, not current Masterpass/SRC availability, enablement, exact SDK behavior, or payment execution. The separate SRC authority confirms that present support and a safe migration route are unresolved. Evidence: source `:12-17,19-24`; selected raw `:17-35`; extra conflict raw `secure-remote-commerce-2026-09-16.md:14-25,28-48,88-90`.
6. **PASS — Central action, conditions, and detail route.** The flow creates a Braintree client from a tokenization key or server client token, creates the component, reveals the initially hidden button only after availability, and calls `masterpassInstance.tokenize` with `subtotal` and `currencyCode` from a customer action because a popup opens. Success hands `payload.nonce` to the server to create a transaction; popup closure and other errors remain application branches. Exact callback/Promise setup, brand-button note, tokenization options, and error branches remain at source `:21-34` and raw `:37-59,61-135,137-212`.

## Position 44 — `docs-guides-google-pay-client-side-android-v5`

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:718` → `wiki/concepts/braintree-android-sdk.md:74` → `wiki/sources/braintree/source-braintree-docs-guides-google-pay-client-side-android-v5.md:1-43` → `raw/braintree/docs/guides/google-pay/client-side/android/v5-2026-09-16.md:1-184`.

7. **PASS — Exact scope and non-inference.** This is a 2026-09-16 Braintree Android v5-routed Google Pay client guide with a captured `google-pay:5.2.0` dependency example. It covers device-readiness gating, authorization-request creation and launch, and tokenization of the return to a nonce for later processing. It does not prove current package support, merchant/device/card eligibility, Google approval, server transaction completion, or payment execution. Evidence: source `:12-20,28-34`; raw `:17-52,80-127,129-183`.
8. **PASS — Central action, warnings, and detail route.** Initialize `GooglePayLauncher` in `onCreate`, create `GooglePayClient` from a tokenization key or client token, display the button only for `ReadyToPay`, create a request after customer action, launch only `ReadyToLaunch`, then handle failure/cancel/success when tokenizing the callback result. The source preserves the material prose-versus-example mismatch (`GooglePayPaymentAuthRequest` versus `googlePayPaymentAuthResult`) and the already-past March 30, 2026 certificate notice as historical captured wording rather than current traffic evidence. Exact dependency, lifecycle, request, and result branches remain at source `:22-34` and raw `:17-20,25-77,80-127,129-183`.

## Close result

No affected-question correction or close blocker was found. All four pages preserve exact website/platform scope, central retrieval purpose, consequential conditions and warnings, raw detail routes, and required non-inference boundaries.

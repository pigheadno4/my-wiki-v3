# Braintree C42 Query Audit — Group D

- Campaign: `braintree-campaign-42`
- Scope: manifest positions 13–16; four pages; exactly eight fixed questions (two per page)
- Started (UTC): `2026-10-07T01:01:40Z`
- Completed (UTC): `2026-10-07T01:02:31Z`
- Overall verdict: **FAIL — 5/8 questions PASS, 3/8 FAIL; all four retrieval routes and manifest pins PASS**

## Shared checks

- Read the root index and Braintree provider index, then the three main concept pages, all four canonical source pages, and all four pinned raws in full. No sibling raw/source, current provider page, direct-PayPal authority, or GitHub evidence was used to answer the questions.
- Manifest identity PASS: each source `canonical_url`, source `raw_files` entry, raw `Source URL`, and manifest path/URL identify the same exact collected variant.
- SHA-256 PASS for all four pinned raws:
  - `docs-guides-paypal-recurring-payments-javascript-v3`: `712f62d8162aee310e107b1056ff51a6d07d2d0d4fabc92a036f29a57aad1a25`
  - `docs-guides-paypal-testing-go-live-ios-v7`: `aaa7beec0ba17fed34a81d5153e978aa1de17e9a14a2f048078ef743610a5235`
  - `docs-guides-paypal-recurring-payments-android-v5`: `e3a3801f45c2df127639b718763d789c4455f33abd895b174c98e424c48aa512`
  - `docs-guides-venmo-client-side-ios-v7`: `0a34d19edee0a4dd87045ccbe475756577913cceee54c80a8cb570e4519c6e0c`
- Bounded filename/related-raw sweep found the expected sibling variants and one navigation-only Checkout-with-Vault raw reference. None was needed: each fixed question is answered by its exact pinned raw. No extra authority reads were performed.
- Main-concept reciprocity PASS now for every page: each provider-index concept links to the source and each source links back to that concept.
- New source entries in the provider/company aggregate catalogs are coordinator-close work. Their present absence is not scored as a page content failure here.

## 13. `docs-guides-paypal-recurring-payments-javascript-v3` — PASS (2/2)

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:695` → `wiki/concepts/braintree-recurring-billing.md:57` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-recurring-payments-javascript-v3.md:52,58` → `raw/braintree/docs/guides/paypal/recurring-payments/javascript/v3-2026-09-16.md`.

1. **PASS — exact scope/non-inference.** This is the collected Braintree website's JavaScript v3 client route for PayPal Billing Without Purchase Checkout: create a Billing Agreement, receive/tokenize its Payment Token, and hand later merchant-initiated payment work to Braintree server operations. It is not Braintree's plan/subscription scheduler, an exact `braintree-web` release, direct PayPal Orders behavior, current enablement, or payment/capture/settlement proof. Source: lines 14, 18–22, 26–33; raw: lines 17–25, 30–59, 201–264.
2. **PASS — central action/material conditions/detail route.** The raw requires the correct RBA classification (`plan_type` at agreement creation and `transaction_source` later), creation-time-only `plan_metadata` disclosure, prepaid/postpaid classification plus Account Manager enablement, and a later single-use-token → Payment Method Create → payment-method-token handoff. The source retains those conditions and warns against the malformed duplicate table; exact matrices/examples remain retrievable at raw lines 69–145, 148–264, and 267–276. Source: lines 19–22, 32–47.

## 14. `docs-guides-paypal-testing-go-live-ios-v7` — FAIL (1/2)

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:719` → `wiki/concepts/braintree-ios-sdk.md:83` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-testing-go-live-ios-v7.md:40,44` → `raw/braintree/docs/guides/paypal/testing-go-live/ios/v7-2026-09-16.md`.

1. **PASS — exact scope/non-inference.** This is the 2026-09-16 Braintree website route under iOS v7 for mocked versus linked PayPal sandbox testing, eligibility-qualified App Switch testing/fallback, and the server-side production transition. It is not sibling-version, current-availability, direct-PayPal, exact-SHA runtime, transaction, settlement, or funding proof. Source: lines 14, 18–21, 24–25; raw: lines 16–46, 92–256, 259–382.
2. **FAIL — credential scope is overstated.** The source says the production merchant ID and public/private API keys are all “environment- and user-specific” (source line 22). The raw says sandbox/production merchant IDs and keys differ (raw lines 262–263), but only the public and private keys are explicitly both environment- and user-specific (raw lines 270–284). Correct the summary so user-specific scope attaches only to the public/private keys. The remaining consequential conditions—dedicated Account Admin API user, server-side credentials, unchanged client token, real-card/fee warning, and limited low-value settled tests—are accurately retained and routed at source lines 20–22, 27–35 and raw lines 268–382.

## 15. `docs-guides-paypal-recurring-payments-android-v5` — FAIL (1/2)

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:718` → `wiki/concepts/braintree-android-sdk.md:76` → `wiki/sources/braintree/source-braintree-docs-guides-paypal-recurring-payments-android-v5.md:56,65` → `raw/braintree/docs/guides/paypal/recurring-payments/android/v5-2026-09-16.md`.

1. **PASS — exact scope/non-inference.** This is the captured Braintree Android v5 website route for constructing a PayPal recurring Billing Agreement request and routing the resulting token toward later Braintree server payment operations. It is not a sibling platform, current Android package/support statement, standalone PayPal Android/Orders behavior, Braintree plan/subscription scheduling, or transaction outcome. Source: lines 14–16, 20–25, 27–34; raw: lines 17–25, 30–67, 140–188.
2. **FAIL — consequential example defect is not disclosed.** The Kotlin `PayPalRecurringBillingDetails` example omits a comma after `totalAmount = "32.56"` before `productName`, so the displayed snippet is not directly runnable (raw lines 162–173, specifically 165–166). The source calls the values illustrative (source line 24) but does not identify the syntax defect while routing readers to that precise procedure (source line 47). Add a bounded warning that the captured example needs syntax repair; do not infer corrected SDK behavior. Other prerequisites and warnings—RBA classification, creation-only plan metadata, prepaid/postpaid enablement, server handoff, product boundary, and malformed final table—are accurately retained at source lines 20–34, 38–50 and raw lines 51–137, 181–200.

## 16. `docs-guides-venmo-client-side-ios-v7` — FAIL (1/2)

Actual route: `wiki/index.md:11` → `wiki/braintree-index.md:719` → `wiki/concepts/braintree-ios-sdk.md:87` → `wiki/sources/braintree/source-braintree-docs-guides-venmo-client-side-ios-v7.md:49,59` → `raw/braintree/docs/guides/venmo/client-side/ios/v7-2026-09-16.md`.

1. **PASS — exact scope/non-inference.** This is the captured Braintree iOS v7 website guide for Venmo client setup, app/browser return handling, single-use versus multi-use tokenization, nonce/device-data handoff, and separate server transaction creation. It is not current package/support, Production enablement, merchant/buyer eligibility, vault success, or payment/settlement/funding evidence. Source: lines 14, 18–23, 25–26; raw: lines 27–175, 252–412.
2. **FAIL — single-use validation scope is overbroad.** The source says a “single-use attempt through `PaymentMethod.create` or `Customer.create`” returns a validation error (source line 20). The raw limits that outcome to an attempt **to vault** a `.singleUse` authorization through those operations (raw lines 293–316); it separately says a `transaction.sale` carrying vault flags processes normally but does not vault the nonce (raw line 316). Correct the summary to retain the vault-attempt qualifier. The certificate-version conflict, Sandbox/eligibility conditions, custom-order-summary service warning, Universal Link fallback, profile pairing, per-transaction device data, ECD prerequisite, and amount validations are otherwise accurately retained and precisely routed at source lines 18–26, 30–44 and raw lines 17–22, 83–175, 224–247, 293–338, 343–507.

## Required bounded corrections

1. iOS PayPal testing/go-live source: attach “user-specific” only to public/private API keys, not merchant ID.
2. Android recurring source: warn that the captured Kotlin example is syntactically incomplete at raw lines 165–166.
3. iOS Venmo source: change “single-use attempt through” to “attempt to vault a `.singleUse` authorization through.”

No repository files were modified.

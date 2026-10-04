# Braintree Campaign 39 query audit — group D

## Shared checks

- Identity **PASS**: provider `braintree`; campaign `braintree-campaign-39`; assigned manifest positions 13–16 only; action is read-only query audit of the four promoted source pages and their pinned raw objects. No repository write, transition, runtime initialization, or aggregate-catalog assumption.
- Object/canonical ownership **PASS**: all four manifest source targets exist, each names the manifest canonical URL and pinned raw file, and each canonical URL has one source owner.
- Raw integrity **PASS**: SHA-256 values match the manifest: accepted payment methods `358f73b7...bbbdbd3`; descriptors `4d1cf443...f41a68`; mitigating risk `055e4dfa...31c9b`; underwriting overview `638a6ae6...8cd5a`.
- Shared route check **PASS**: `[[index]]` → `[[braintree-index]]` → the named main concept → source is usable for every page. Direct source catalog entries remain deferred as instructed.
- Full reads **PASS**: root/Braintree indexes, three used concepts, four source pages, four pinned raw files, and the already-linked SRC source/raw were read fully. The bounded filename/topic sweep found only account/processor siblings and the underwriting periodic-review sibling; they were not used because their scopes are distinct and the assigned raw was sufficient.

## Position 13 — `articles-nab-transactions-accepted-payment-methods`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-methods]]` → `[[source-braintree-articles-nab-transactions-accepted-payment-methods]]`.

1. **Scope — PASS.** This is a Braintree-hosted `/nab/` account/processor snapshot, fetched 2026-09-16 from a page created/updated 2025-04-02. It documents the addressed account's default Visa/Mastercard setup, separately arranged Amex processing, qualified PayPal/Apple Pay/Google Pay/SRC availability, and merchant-account currency handling. Only SRC is expressly located in Australia/New Zealand; the page does not establish broader NAB region, sibling-account, present-support, pricing, eligibility, or execution scope. Raw: `raw/braintree/articles/nab/transactions/accepted-payment-methods-2026-09-16.md:1-9,17-30,49-78`.
2. **Purpose/action and limits — PASS.** Use the page to identify account-default methods and prerequisites: apply directly to Amex, supply currency-matched SE numbers, satisfy pricing-agreement/signature setup, enter PayPal Business credentials, meet wallet customer/device qualifications, and request/select an additional merchant account to reduce conversion friction. It warns about bank conversion fees, harder refunds, and increased chargebacks. Preserve the unresolved SRC conflict: the assigned raw says current limited release for eligible AU/NZ merchants, while the already-linked guide says support ended 2026-01-20 yet also says current limited release; neither snapshot proves present availability. Raw: primary `:26-44,49-78`; secondary `raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16.md:14-15,21-48,88-90`.

## Position 14 — `articles-nab-transactions-descriptors`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-control-panel]]` → `[[source-braintree-articles-nab-transactions-descriptors]]`.

1. **Scope — PASS.** This is a Braintree-hosted `/nab/` addressed-account snapshot, fetched 2026-09-16 from a page created/updated 2025-04-01. It covers statement descriptors for mobile-app/website purchases, including separate PayPal and Amex update routes. The Australian-phone and NAB-registered-trading-name conditions are field qualifications, not proof of general regional, processor, currency, account, or payment-method eligibility. Raw: `raw/braintree/articles/nab/transactions/descriptors-2026-09-16.md:1-9,14-39,44-96`.
2. **Purpose/action and limits — PASS.** The page distinguishes settled hard descriptors from API-supplied per-transaction dynamic descriptors, routes general changes through Braintree, PayPal changes through the PayPal console, and Amex changes directly to Amex. Consequential constraints—registered trading-name match, field/character rules, Australian phone, and dynamic phone-or-URL exclusivity—are retained; exact values stay in raw. The customer's bank controls final statement rendering, and the page does not prove a requested change was accepted or displayed. Raw: `:14-39,44-66,69-96`.

## Position 15 — `articles-risk-and-security-risk-factors-mitigating-risk`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-articles-risk-and-security-risk-factors-mitigating-risk]]`.

1. **Scope — PASS.** This is general, unversioned Braintree merchant risk guidance, fetched 2026-09-16 from a page created/updated 2025-04-01. It addresses a merchant's Braintree integration and underwritten account; it specifies no processor, payment method, region, or jurisdiction. Raw: `raw/braintree/articles/risk-and-security/risk-factors/mitigating-risk-2026-09-16.md:1-9,14-20,25-54`.
2. **Purpose/action and limits — PASS.** Contact Braintree for suspected compromise; disclose the business model, billing practices, expected volume, and anticipated significant changes; use suitable fraud controls, prepare chargeback evidence, and consider CAPTCHA against carding. Unusual amounts or dramatic volume increases may trigger a notified account hold pending review, and analysts may contact the merchant when action is needed. These are recommendations and assistance routes, not fraud-prevention or uninterrupted-processing guarantees; exact tool and procedure detail remains in the linked dedicated pages. Raw: `:19-20,30-39,42-54`.

## Position 16 — `articles-risk-and-security-underwriting-overview`

Route: `[[index]]` → `[[braintree-index]]` → `[[braintree-payment-platform]]` → `[[source-braintree-articles-risk-and-security-underwriting-overview]]`.

1. **Scope — PASS.** This is general Braintree merchant-account-provider underwriting guidance, fetched 2026-09-16 from a page created/updated 2025-04-02. It gives illustrative business-model and billing-risk categories but specifies no processor, payment method, region, or jurisdiction and is not a current eligibility catalog, legal rule, or individual underwriting decision. Raw: `raw/braintree/articles/risk-and-security/underwriting/overview-2026-09-16.md:1-9,14-16,25-53`.
2. **Purpose/action and limits — PASS.** The page explains Braintree's stated loss-exposure rationale and says that, after financial review, it may conditionally require a personal/corporate guarantee or a reserve collected before processing or built by withholding transaction revenue. It also directs suspected-compromise contact and preserves the snapshot statement that Braintree lacks cyberinsurance and does not indemnify. No fixed reserve amount, percentage, duration, approval criterion, or merchant outcome is documented. Raw: `:14-20,25-53,56-72`.

## Close

- Result: **8/8 answers PASS**; no material retrieval defect.
- Blockers: none.
- Approval needed: none for this read-only audit. Any correction, repository transition, catalog update, commit, or push remains coordinator-owned and separately authorized.
- Analysis ended: `2026-10-04T15:01:46Z`.
- Handoff recorded: `2026-10-04T15:02:40Z`.

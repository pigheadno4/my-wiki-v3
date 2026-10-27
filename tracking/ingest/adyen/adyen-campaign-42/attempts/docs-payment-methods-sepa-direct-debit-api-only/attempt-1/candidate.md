---
title: "Adyen SEPA Direct Debit API-only integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit/api-only"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/api-only/2026-09-15.md"
tags: [adyen, sepa-direct-debit, api-only, advanced-flow, iban, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds SEPA Direct Debit to an **existing Web API-only Advanced-flow** integration. It covers method discovery, a merchant-built form, the `/payments` request, capture, recurring tokens, and test/live setup. It is a method-specific add-on; [[source-adyen-docs-payment-methods-sepa-direct-debit]] holds broader mandate, pre-debit notice, settlement, return and chargeback rules. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Base integration and form:** The page requires an existing API-only integration with handling for an additional `direct` action and SEPA Direct Debit added in Customer Area. The merchant builds the payment form. A form instruction says to collect “issuer selection,” but the immediately following table actually lists **bank-account owner name and IBAN**; the `/payments` field table also requires those details. Do not treat the stray phrase as a SEPA issuer-list requirement. A high-level step says to include purchased-item information, while the dedicated request table and sample focus on SEPA account fields; consult the base API-only guide for any general request fields. (raw lines 23–49, 92–125)
- **Method discovery:** To include SEPA Direct Debit in the `/paymentMethods` response, the page lists specific `countryCode` values (AT, BE, CY, EE, FI, FR, DE, GR, IE, IT, LV, LT, LU, MT, NL, PT, SK, SI, ES) and `amount.currency: EUR`. The sample is a **test v72** `/paymentMethods` request and `sepadirectdebit` response; the list is a request-configuration statement, not proof of current bank or merchant eligibility or a stated API minimum version. (raw lines 51–90)
- **Payment request and intermediate result:** The dedicated `/payments` table requires `paymentMethod.sepa.ownerName` and `paymentMethod.sepa.ibanNumber`, with the instruction **not to encrypt the IBAN**. Billing address is conditionally required for the enumerated non-EEA SEPA IBAN countries/territories, not every SEPA IBAN. The test v72 payment example is illustrative; its curl line breaks around `-X POST` are not copy-ready. Its “successful payment” response shows `resultCode: Received`, which alone does not prove final authorization, capture or settled funds. (raw lines 92–136)
- **Capture:** If automatic capture is not used, the guide says to use delayed automatic or manual capture. It says SEPA Direct Debit authorizations do not expire and refers multiple partial capture enablement to Support. That capture statement is conditioned on an authorized payment; the `Received` example does not establish authorization. (raw lines 138–147)
- **Recurring:** The guide documents Subscription and UnscheduledCardOnFile tokenization using standard request fields with no extra SEPA-specific token fields. It **strongly recommends** explicit shopper permission and transparent schedule/amount to reduce chargeback risk; this advice is not the entire mandate rule. A `recurring.token.created` webhook contains `storedPaymentMethodId`; subsequent shopper-absent `/payments` use the stored ID, `shopperInteraction: ContAuth`, and the respective recurring model. Examples do not prove token creation or successful future debit. (raw lines 149–183, 506–536, 853–879)
- **Testing/live gate:** NL/AT/FR test names and IBANs plus test Customer Area status navigation are provided. Before accepting live SEPA Direct Debit, the guide says to submit a request in the **live** Customer Area. A historical sample and test result do not establish current enablement. (raw lines 1196–1208)

## Detail locators

- API-only prerequisites, high-level steps, form mismatch and bank detail table: pinned raw lines 23–49.
- `/paymentMethods` country/currency filter and v72 test response: pinned raw lines 51–90.
- Conditional billing address, unencrypted IBAN and `Received` test payment example: pinned raw lines 92–136.
- Capture modes and Support gate: pinned raw lines 138–147.
- Token creation and recurring model examples: pinned raw lines 149–505; token webhook and shopper-absent reuse: lines 506–1193. Some generated library samples omit SEPA owner/IBAN fields shown in the curl/JavaScript/Python examples; verify against the actual API/library version before implementation.
- Test data, live request and base-guide pointer: pinned raw lines 1196–1212.

## Related

- [[adyen-online-payments]] — main provider payment-method context
- [[adyen-tokenization]] — stored-method context
- [[source-adyen-docs-payment-methods-sepa-direct-debit]] — method-level mandate, notice, settlement and chargeback qualifications
- [[adyen]] — provider

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/api-only/2026-09-15|SEPA Direct Debit API-only, 2026-09-15]]

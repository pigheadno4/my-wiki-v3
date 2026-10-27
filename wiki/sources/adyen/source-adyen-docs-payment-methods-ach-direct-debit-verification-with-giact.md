---
title: "ACH Direct Debit account validation with giact gVERIFY"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit/verification-with-giact"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/verification-with-giact/2026-09-15.md"
tags: [adyen, ach, direct-debit, bank-verification, giact, tokenization]
---

## Overview

This 2026-09-15 Adyen guide describes **giact gVERIFY** bank-account validation for ACH Direct Debit, including account setup, three mutually exclusive trigger options, API-only/Drop-in/Components paths, zero-value checks, result codes and TEST fixtures. It concerns account validity/status before attempting a debit; it does **not** prove bank authorization, available funds, a valid shopper mandate or settled ACH payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The page says Nacha requires validation of **consumer WEB** bank details on the shopper's **first transaction**. giact checks a proprietary database and static rules, **not real-time bank access**, so a pass only reduces some incorrect-routing/closed-account returns. Required setup is an Adyen contract addendum, Support enablement with one selected option, ACH Direct Debit in test Customer Area, and Standard webhook **Include Bank Verification results**. It recommends validation only on initial transaction and account changes for cost reasons. See raw lines 19–32. The broader ACH overview [[source-adyen-docs-payment-methods-ach-direct-debit]] keeps mandate/SEC/return responsibilities separate.
- Exactly **one account-configured validation option** can be selected: consumer ecommerce (first ecommerce + SEC **WEB**), all ecommerce (first ecommerce with any SEC), or zero-amount payments (`amount.value=0`, independent of interaction/SEC). The guide recommends consumer ecommerce for Drop-in/Components; its table labels zero amount **API-only**. See raw lines 34–47.
- In ordinary consumer/all-ecommerce flow, Drop-in/Components collect bank number, ACH routing number and owner name; leave `hasHolderName` and `holderNameRequired` true or collect owner name yourself. Adyen submits qualifying first-payment details to giact: passed validation proceeds to a **payment attempt**, failed validation refuses. API-only collects those fields itself and receives a refusal response. A passed account check is not payment success. See raw lines 49–99.
- **Zero amount option:** API-only form collects bank number, routing number, owner name and checking/savings type; the page warns against supplying a wire routing number and says giact does **not** verify account type. Zero-value request can store details for a later real-amount debit; outcome is in the zero-value authorization response and/or `AUTHORISATION` webhook. The guide's zero-option table says API-only, but the how-to section also has a `/sessions` tab plus a `/payments` tab; do not infer Drop-in/Components support merely from the `/sessions` example. See raw lines 101–142 and 217–286.
- The `/sessions` zero-value example uses USD 0, `storePaymentMethod: true`, `storePaymentMethodMode: enabled` or `askForConsent`, and `shopperReference`; webhook fields are described as `bankVerificationResultRaw`, `bankVerificationResult` and `storedPaymentMethodId`. Its JSON example nests the token as `tokenization.storedPaymentMethodId`, so preserve the field-name mismatch. If validation passes, the page shows a later token-based `/sessions` request for the real amount; if it fails, request corrected details or another method. See raw lines 134–215. [[adyen-tokenization]]
- The `/payments` zero-value route specifies `paymentMethod.type=ach`, bank number, checking/savings type, ACH routing number, owner name, optional billing address and USD 0. It reads Passed/Failed from response or webhook; passed details are reused for a real-amount request. Its curl example has a literal `{hint:...}paymentMethod{/hint}` key rather than clean `paymentMethod` JSON, so it should not be copied as executable code. See raw lines 217–286.
- `bankVerificationResultRaw` codes include positive, negative, format and no-data/risk categories; **do not map raw codes to Passed/Failed by name alone**. TEST fixture table shows `ND00`, `RT00`, `RT03` and even `GN01` as **Passed**, while `GS02`, `RT01`, `RT02`, `RT04` are **Failed**. The `GN01` raw description says negative information found, creating a material classification tension. TEST routing number `122105278` and mock accounts only simulate outcomes. See raw lines 288–335.

## Detail locators

- Purpose, non-real-time limit, prerequisites and webhook setting: raw lines 15–32.
- Exclusive trigger options and channel guidance: raw lines 34–47.
- Consumer/all-ecommerce collection, automatic attempt/refusal: raw lines 49–99.
- Zero-value details, account-type caveat and option scope: raw lines 101–130.
- `/sessions` zero check, webhook token and later request: raw lines 134–215.
- `/payments` zero check, malformed example key and later request: raw lines 217–286.
- Raw result descriptions and TEST Passed/Failed fixtures: raw lines 288–335.

## Related

- [[adyen-online-payments]] — ACH online-payment method route.
- [[adyen-tokenization]] — zero-value token and later payment route.
- [[source-adyen-docs-payment-methods-ach-direct-debit]] — ACH eligibility, SEC, mandate, return and refund context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/verification-with-giact/2026-09-15|ACH account validation with giact, captured 2026-09-15]]

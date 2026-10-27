---
title: "Adyen ACH Direct Debit Web Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit/web-component"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/web-component/2026-09-15.md"
tags: [adyen, ach-direct-debit, web, components, sessions, advanced-flow, bank-debit]
---

## Overview

This 2026-09-15 Adyen guide adds ACH Direct Debit to an **existing Web Components** integration using Sessions or Advanced server-side flow. It covers component setup, method-specific request additions, delayed bank outcome and test data. It is not the complete integration or method-level mandate and bank-return guide. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-ach-direct-debit]].

## Key takeaways

- **Prerequisites are flow-specific:** Sessions requires an existing Web Components Sessions integration, **Checkout API v68 or later**, subscription to `DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION` for outdated bank details, and ACH added in Customer Area. Advanced lists an existing Web Components Advanced integration, the same change-notice webhook and Customer Area setup; it does **not** state the Sessions v68 minimum for Advanced. Both tables mention the `Merchant allow bank-refund` role **for issuing refunds** by API or Customer Area. That is a refund-operation permission, not a stated prerequisite to take an ACH payment. (raw lines 25–38, 121–131)
- **Component and requests:** Both flows say to import `Ach` from Adyen Web. Sessions says no additional ACH-specific `/sessions` parameters, while Advanced says none for `/payments`. Both list optional UI configuration: `enableStoreDetails` from **Web v5.24.0 or later** shows a save-details checkbox when true (default false); `hasHolderName` false hides the field if merchant passes the data (default true); `holderNameRequired` false makes the name field optional (default true). A checkbox is not proof of token creation, valid authorization or mandate. The `Ach.Configuration()` snippet is marked `bash` and the initialization example shows `newAch` with incomplete object/comment placement; use the verified base integration/API for executable code rather than copying these fragments literally. (raw lines 40–93, 133–186)
- **Delayed outcome:** After Adyen successfully receives the request, the guide says it may take **up to five business days** to learn whether the bank authorized the payment. It says bank-authorized payments appear in the Settlement details report; if the bank fails to authorize, a `CHARGEBACK` webhook follows. Request receipt, component outcome and bank authorization are separate from irrevocable funds: the ACH overview records reversals, nondefendable chargebacks and settlement-dependent refunds. The guide's `#chargebacks` anchor has no chargeback section in this captured page; use the linked ACH overview or dedicated chargebacks source for that lifecycle. (raw lines 95–101, 188–194; [[source-adyen-docs-payment-methods-ach-direct-debit]])
- **Testing:** The page allows test payments with any name and correctly formatted account/routing numbers, and says to trigger a test chargeback by prefixing `ownerName` with `chargeback:` plus an ACH return reason code, such as `chargeback:R01`. These are test-environment scenarios, not proof of live bank validation, merchant eligibility or a completed debit. This guide does not describe a separate live activation request. (raw lines 103–119, 196–212)
- **Method-level duties:** The related ACH overview says accepting merchants need a US registered entity, consumer bank-account validation, B2B bank allowlisting in applicable cases, correct SEC code, and a signed customer mandate; Components/Drop-in handle the SEC code automatically. Those eligibility and authorization duties should not be inferred as satisfied by this page's “no additional parameters” statements. (raw lines 44, 186; [[source-adyen-docs-payment-methods-ach-direct-debit]])

## Detail locators

- Sessions prerequisites, conditional refund roles, change-notice webhook and v68+ minimum: pinned raw lines 25–38.
- Sessions no-extra-request fields and component import/config/init examples: pinned raw lines 40–93.
- Sessions delayed outcome and test payment/return scenarios: pinned raw lines 95–119.
- Advanced prerequisites, import/config/init and no-extra-`/payments` statement: pinned raw lines 121–186.
- Advanced outcome and repeated test instructions: pinned raw lines 188–212; related resource links: lines 214–218.
- ACH method-level eligibility, SEC/mandate, refunds and bank-return consequences: [[source-adyen-docs-payment-methods-ach-direct-debit]].

## Related

- [[adyen-online-payments]] — online bank-debit integration context
- [[source-adyen-docs-payment-methods-ach-direct-debit]] — ACH mandate, bank verification, settlement, returns and refund context
- [[adyen-tokenization]] — broader stored-method context; this page only lists a save-details checkbox and generic tokenization pointer
- [[adyen]] — provider

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/web-component/2026-09-15|ACH Direct Debit Web Component, 2026-09-15]]

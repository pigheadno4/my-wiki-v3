---
title: "Adyen SEPA Direct Debit Web Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/web-drop-in/2026-09-15.md"
tags: [adyen, sepa-direct-debit, web, drop-in, sessions, advanced-flow, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds **SEPA Direct Debit to an existing Web Drop-in integration**, with separate Sessions and Advanced-flow instructions. It is a method-specific add-on, not a complete base integration or a statement of current merchant eligibility. See [[adyen]], [[adyen-online-payments]], and [[adyen-tokenization]].

## Key takeaways

- **Sessions flow:** Requires an existing Sessions Web Drop-in integration, Checkout API **v68 or later**, and SEPA Direct Debit added in Customer Area. The ordinary payment-session step needs no additional SEPA-specific parameters; individual `SepaDirectDebit` import is optional for tree shaking. The guide's token-creation example uses `/sessions` **v71** with standard tokenization fields. (raw lines 23–53, 63–88)
- **Advanced flow:** Requires an existing Advanced Web Drop-in integration, action handling for `action.type: direct`, and the payment method added in Customer Area. Its `/payments` request specifies `paymentMethod.sepa.ownerName` and an **unencrypted** `paymentMethod.sepa.ibanNumber`. The billing address is required for the listed non-EEA SEPA IBAN countries or territories; this condition should not be generalized to all SEPA IBANs. The illustrated initial request uses Checkout API **v72**. (raw lines 900–959)
- **Intermediate result and capture:** The Advanced example labels a response successful while showing `resultCode: Received`; that example alone does not establish final authorization, capture or settlement. If automatic capture is not used, the guide specifies delayed automatic or manual capture. It says SEPA Direct Debit authorizations do not expire, so capture can occur after authorization, and directs merchants to Support to enable multiple partial captures. The method overview separately supplies mandate, pre-debit notice, settlement and chargeback qualifications; this implementation guide does not replace them. (raw lines 962–981; [[source-adyen-docs-payment-methods-sepa-direct-debit]])
- **Recurring:** The guide covers **Subscription** and **UnscheduledCardOnFile** tokenization and strongly *recommends* explicit shopper permission and transparent schedule/amount to reduce chargeback risk. It says to use standard tokenization fields, without extra SEPA-specific token fields. A `recurring.token.created` webhook carries `storedPaymentMethodId`; later shopper-absent payments use `/payments` with the stored ID, `shopperInteraction: ContAuth`, and the corresponding recurring model. This is a documented route, not proof that a token was created or a later debit succeeded. (raw lines 55–65, 264–297, 577–604, 983–993, 1342–1373, 1653–1679)
- **Testing and live gate:** The page provides NL/AT/FR test name–IBAN pairs and says to check test payment status in Customer Area. Before live SEPA acceptance, it requires a request for SEPA Direct Debit in the **live** Customer Area. Test details and a historical guide cannot establish live enablement or a funded debit. (raw lines 884–898, 1960–1974)

## Detail locators

- Sessions prerequisites, no extra ordinary `/sessions` fields, and optional Web import: pinned raw lines 25–53.
- Sessions token creation and stored-token subsequent payment examples: pinned raw lines 55–88 and 264–881; the individual language examples should be checked against the active API/library version before reuse.
- Advanced prerequisites, conditional billing address, request fields, and `Received` response: pinned raw lines 900–970. The shown curl request has a line-break/command formatting issue around `-X POST`; treat it as a field illustration, not a copy-ready command.
- Capture and multiple-partial-capture enablement: pinned raw lines 972–981.
- Advanced token creation and reuse, including webhook and shopper-absent limitation: pinned raw lines 983–1958.
- Test data and live Customer Area request: pinned raw lines 884–898 and 1960–1974.

## Related

- [[adyen-online-payments]] — Web checkout and payment-method context
- [[adyen-tokenization]] — token creation and subsequent-payment context
- [[source-adyen-docs-payment-methods-sepa-direct-debit]] — method-level mandate, notice, settlement and chargeback context
- [[adyen]] — provider

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/web-drop-in/2026-09-15|SEPA Direct Debit Web Drop-in, 2026-09-15]]

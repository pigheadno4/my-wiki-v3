---
title: "SEPA Direct Debit iOS Component integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit/ios-component"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/ios-component/2026-09-15.md"
tags: [adyen, sepa-direct-debit, ios, components, bank-debit, tokenization, capture]
---

## Overview

This 2026-09-15 guide adds SEPA Direct Debit to an **existing iOS Components** integration, with separate Sessions and Advanced paths, `SEPADirectDebitComponent` initialization, recurring-token examples, TEST IBAN fixtures and a live Customer Area request gate. It is method-specific integration guidance, not evidence that a debit settled, a merchant is enabled, or a mandate has been satisfied. [[adyen]] [[adyen-online-payments]] [[adyen-ios-sdk]]

## Key takeaways

- **Sessions:** the base iOS Components Sessions flow must already exist, Checkout API **v68 or later** is required, and SEPA Direct Debit must be added in Customer Area. The page says no SEPA-specific parameters for the ordinary `/sessions` creation and no SEPA-specific Component configuration. Initialize `SEPADirectDebitComponent` only after finding `SEPADirectDebitPaymentMethod` in session payment methods; the snippet delegates to the session. See raw lines 25–72.
- **Advanced:** the page calls for an existing iOS Components Advanced flow and Customer Area setup, then initializes the same Component with the merchant-side delegate. The integration-type label's URL is for **Drop-in**, and the action row says handle an additional action through a `handle-the-redirect` anchor while naming `action.type: direct`; preserve that conflict rather than treating it as a clear redirect recipe. See raw lines 917–957.
- **Advanced ordinary `/payments`:** the table marks `paymentMethod.sepa.ownerName` and `paymentMethod.sepa.ibanNumber` required and says **do not encrypt the IBAN value**. Billing address fields are conditionally required for the listed **11 non-EEA SEPA countries and four territories**; the table's Required column is blank, but the prose and row description explicitly impose this condition. The example uses a DE IBAN and no billing address, so it does not test the non-EEA rule. See raw lines 959–995.
- The Advanced example labels a response `successful payment` but shows `resultCode: Received`. Treat `Received` as the example response, **not settled-funds evidence**; this guide does not document a later final-result webhook sequence. See raw lines 997–1005.
- If automatic capture is not used, the Advanced section offers delayed automatic or manual capture. It says SEPA Direct Debit authorizations do not expire and can be captured any time after authorization; multiple partial captures require Support enablement. These are source claims scoped to this SEPA guide, not a guarantee of bank settlement. See raw lines 1007–1016.
- **Recurring:** the guide supports Subscription and UnscheduledCardOnFile tokenization and **strongly recommends** explicit shopper permission plus transparency about schedule/amount; this recommendation is separate from any legal mandate requirement outside this page. Standard tokenization parameters go in `/sessions` or `/payments` for token creation without SEPA-specific extras; `recurring.token.created` later supplies `storedPaymentMethodId`. Subsequent shopper-absent Subscription or UnscheduledCardOnFile payments use `/payments` and standard tokenization fields (examples use `sepadirectdebit`, stored ID, `shopperReference`, `ContAuth` and the selected model). Do not apply the ordinary no-extra-fields statement to token creation or reuse. See raw lines 74–84, 91–107, 283–314, 596–615, 1020–1028, 1377–1408 and 1688–1715. [[adyen-tokenization]]
- Advanced token-creation examples are **not uniformly complete**: the prose/table requires owner name and IBAN for an ordinary Advanced `/payments` request, while several language examples under the token-creation subsection omit these fields; the NodeJS JavaScript and Python examples include them. Follow the stated field requirement and selected integration mode rather than treating every sample as a complete request. See raw lines 963–971, 1032–1070, 1188–1225 and 1269–1302.
- TEST provides NL/AT/FR account-name and IBAN fixtures and test Customer Area status lookup. Live acceptance requires a SEPA Direct Debit request in **live Customer Area**; the snapshot does not establish activation or successful bank debit. See raw lines 903–915 and 1995–2007.

## Detail locators

- Sessions requirements, no-extra-fields/config and Component initialization: raw lines 25–72.
- Sessions token creation/reuse prose and examples: raw lines 74–900.
- Advanced prerequisite/link/action inconsistencies and Component initialization: raw lines 917–957.
- Advanced ordinary request table, conditional non-EEA billing address and `Received` example: raw lines 959–1005.
- Delayed/manual capture and multiple-partial enablement: raw lines 1007–1016.
- Advanced recurring token creation/reuse prose and examples: raw lines 1020–1993.
- TEST fixtures and live request gate: raw lines 903–915 and 1995–2007.

## Related

- [[adyen-online-payments]] — main iOS Components route.
- [[adyen-ios-sdk]] — native Component context.
- [[adyen-tokenization]] — recurring-token lifecycle.
- [[source-adyen-docs-payment-methods-sepa-direct-debit]] — method overview and mandate/dispute context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/ios-component/2026-09-15|SEPA Direct Debit iOS Component, captured 2026-09-15]]

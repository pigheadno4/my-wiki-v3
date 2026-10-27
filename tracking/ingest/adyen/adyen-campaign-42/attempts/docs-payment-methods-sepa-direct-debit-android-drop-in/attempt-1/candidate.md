---
title: "SEPA Direct Debit Android Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/android-drop-in/2026-09-15.md"
tags: [adyen, sepa-direct-debit, android, drop-in, tokenization, capture]
---

## Overview

This Adyen Android Drop-in add-on separates Sessions and Advanced server-side flows for SEPA Direct Debit. Sessions requires an existing Drop-in integration using Checkout API v68 or later; Advanced requires an existing Android Drop-in integration with additional-action handling, labeled `action.type: direct` even though its anchor says “handle the redirect.” Both require adding the method in Customer Area. The ordinary Sessions section says no SEPA-specific `/sessions` fields, while Advanced lists account details and conditional billing address for `/payments` (raw lines 15–50, 909–953).

## Key takeaways

- Both flows show an optional `setSubmitButtonVisible` configuration entry: false hides the submit button; true is the default. The Sessions example and Advanced example are schematic, not complete application configuration (raw lines 42–62, 919–939).
- For Advanced `/payments`, the table marks `paymentMethod.sepa.ownerName` and `paymentMethod.sepa.ibanNumber` required and says not to encrypt the IBAN. It also requires street, house number/name, postal code, city and country when the IBAN country is one of the listed 11 non-EEA SEPA countries or four territories; consult the full table for the exact list (raw lines 941–953). The later language-library token-creation examples often show only `sepadirectdebit` without the table's owner/IBAN fields, so they are not complete templates for that initial request (raw lines 1016–1357).
- The Advanced response example is labeled a successful payment but contains `resultCode: Received`; this sample does not establish final authorization, capture or settled funds. The page gives no full webhook outcome sequence (raw lines 955–987). The related SEPA overview separately requires the shopper's active mandate acceptance before debit and describes chargeback risk; do not interpret this add-on's recurring-permission recommendation as the complete mandate procedure (overview raw lines 29, 37–71, 100–109).
- In Advanced flow, if automatic capture is not used, the source lists delayed automatic or manual capture. It says SEPA Direct Debit authorizations do not expire and multiple partial captures require Support enablement; these are source-scoped claims, not proof of a merchant's configuration (raw lines 989–998).
- SEPA tokenization supports Subscription and UnscheduledCardOnFile. This guide **strongly recommends** explicit permission for future recurring charges and schedule/amount transparency; it does not phrase that recommendation as the SEPA mandate rule. It says to use standard tokenization fields, with no extra SEPA-specific token fields, and to wait for `recurring.token.created` with `storedPaymentMethodId`. Shopper-absent token use is limited here to `Subscription` or `UnscheduledCardOnFile` via `/payments`, with `ContAuth` shown in examples (raw lines 64–95, 273–305, 1002–1010, 1359–1389, 1670–1697). The Advanced “create a token” curl omits a storage flag despite that label, so verify standard tokenization parameters in the linked authority rather than using the example as a complete token-creation recipe (raw lines 1008–1037).
- The test sections list example names/IBANs for NL, AT and FR, and say a request for SEPA Direct Debit in live Customer Area precedes live acceptance. They do not prove a successful debit or current account eligibility (raw lines 893–907, 1977–1989).

## Detail locators

- Sessions prerequisite, no ordinary method fields and optional submit button: raw lines 25–62.
- Sessions token creation, lifecycle webhook and shopper-absent reuse: raw lines 64–95, 273–305, 586–612.
- Advanced prerequisite, action label and account/billing request fields: raw lines 909–953.
- Advanced example `Received` and capture qualifications: raw lines 955–998.
- Advanced token-creation example limits and recurring/token reuse: raw lines 1002–1037, 1359–1389, 1670–1697.
- TEST IBAN examples and live request gate: raw lines 893–907, 1977–1989.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-payment-capture]]
- [[raw/adyen/docs/payment-methods/sepa-direct-debit/2026-09-15|SEPA Direct Debit overview (related mandate and chargeback evidence)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/android-drop-in/2026-09-15|SEPA Direct Debit Android Drop-in, fetched 2026-09-15]]

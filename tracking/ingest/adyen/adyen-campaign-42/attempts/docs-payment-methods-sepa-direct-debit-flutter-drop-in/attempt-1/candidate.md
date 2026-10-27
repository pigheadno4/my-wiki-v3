---
title: "SEPA Direct Debit Flutter Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/flutter-drop-in/2026-09-15.md"
tags: [adyen, sepa-direct-debit, flutter, drop-in, bank-debit, tokenization, capture]
---

## Overview

This 2026-09-15 guide describes SEPA Direct Debit additions to an **existing Flutter Drop-in** Sessions or Advanced integration. It covers ordinary payment request differences, recurring-token creation/reuse, Advanced capture, TEST account fixtures and a live Customer Area gate. It is not evidence of an enabled merchant, completed mandate or settled debit. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions** requires an existing Flutter Drop-in Sessions flow, Checkout API **v68 or later**, and contacting Adyen Support to add SEPA Direct Debit in Customer Area. The displayed Sessions prerequisite URL actually points to an **Advanced** Flutter Drop-in guide, while the later create-session link targets Sessions. Ordinary `/sessions` creation needs no SEPA-specific additional parameters, and Drop-in needs no SEPA-specific configuration. See raw lines 25–47.
- **Advanced** requires an existing Flutter Drop-in Advanced flow and adding SEPA Direct Debit in Customer Area. Its action row says handle an additional action with `action.type: direct`, but links to a `handle-the-redirect` anchor; read this as a source navigation/action mismatch, not a proven redirect recipe. No SEPA-specific Drop-in configuration is required. See raw lines 892–908.
- For an **Advanced ordinary `/payments`** request, the table marks `paymentMethod.sepa.ownerName` and `paymentMethod.sepa.ibanNumber` required and says **do not encrypt the IBAN value**. Billing address fields are required when the IBAN belongs to the listed 11 non-EEA SEPA countries or four territories, even though the table's Required cell is blank; the prose and row description state the condition. The DE-IBAN example without billing address does not test that rule. See raw lines 910–946.
- The Advanced example is labeled a `successful payment` response but shows `resultCode: Received`; that example is **not evidence of settlement**. If automatic capture is off, use delayed automatic or manual capture. The guide states SEPA Direct Debit authorizations do not expire and can be captured any time after authorization; **multiple partial captures need Support enablement**. See raw lines 948–967. [[adyen-payment-capture]]
- **Recurring** supports tokenization for Subscription and UnscheduledCardOnFile. The guide **strongly recommends** explicit shopper permission and transparency about schedule/amount to reduce chargebacks; it does not itself set out a mandate rule. Standard tokenization fields are used in `/sessions` or `/payments` for creation without method-specific additions. After `recurring.token.created` supplies `storedPaymentMethodId`, subsequent shopper-absent token payments use `/payments` with standard fields; examples specify `sepadirectdebit`, stored ID, `shopperReference`, `ContAuth` and the chosen model. Ordinary no-extra-field text does not remove tokenization parameters. See raw lines 49–59, 63–82, 258–287, 571–590, 969–979, 1328–1359 and 1639–1666. [[adyen-tokenization]]
- Advanced token-creation examples are not uniformly complete: the ordinary Advanced table requires owner name and IBAN, yet several language samples beneath token creation omit them while the curl, NodeJS JavaScript and Python samples include them. Treat examples as illustrative rather than as a universal complete request schema. See raw lines 914–922, 983–1007, 1008–1138, 1139–1176 and 1220–1253.
- TEST offers NL/AT/FR account-name and IBAN fixtures and test Customer Area status lookup. Before live acceptance, submit a SEPA Direct Debit request in **live Customer Area**. These instructions do not prove activation or payment success. See raw lines 878–890 and 1946–1958.

## Detail locators

- Sessions version/setup, misrouted prerequisite, no-extra-fields/configuration: raw lines 25–47.
- Sessions token creation and later `/payments` reuse: raw lines 49–876.
- Advanced setup/action mismatch and no configuration: raw lines 892–908.
- Advanced request fields, conditional billing address, `Received` example and capture: raw lines 910–967.
- Advanced token creation/reuse and sample variability: raw lines 969–1944.
- TEST fixtures and live request gate: raw lines 878–890 and 1946–1958.

## Related

- [[adyen-online-payments]] — main Flutter Drop-in method route.
- [[adyen-payment-capture]] — capture mode and asynchronous outcome context.
- [[adyen-tokenization]] — recurring-token lifecycle.
- [[source-adyen-docs-payment-methods-sepa-direct-debit]] — method overview and mandate/dispute context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/flutter-drop-in/2026-09-15|SEPA Direct Debit Flutter Drop-in, captured 2026-09-15]]

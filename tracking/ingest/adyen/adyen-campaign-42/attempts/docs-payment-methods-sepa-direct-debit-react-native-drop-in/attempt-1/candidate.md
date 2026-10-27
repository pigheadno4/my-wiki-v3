---
title: "Adyen SEPA Direct Debit React Native Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/react-native-drop-in/2026-09-15.md"
tags: [adyen, sepa-direct-debit, react-native, drop-in, sessions, advanced-flow, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds SEPA Direct Debit to an **existing React Native Drop-in** integration. It gives distinct Sessions and Advanced server-side routes, recurring token examples, and test/live setup. It does not replace the main React Native Drop-in integration or the SEPA Direct Debit mandate and settlement guidance. See [[adyen]], [[adyen-online-payments]], and [[adyen-tokenization]].

## Key takeaways

- **Sessions:** The page requires an existing Sessions React Native Drop-in integration, Checkout API **v68 or later**, and SEPA Direct Debit added in Customer Area. It says the ordinary `/sessions` request needs no additional method parameters and no extra SEPA configuration. The Sessions requirement's link, however, points to an **Advanced-flow** URL despite its Sessions label; follow the separate Sessions link at the payment-session step and verify the intended base guide. The token-creation example uses test Checkout API **v71**; this guide gives no React Native SDK version. (raw lines 23–47, 65–83)
- **Advanced:** Requires an existing Advanced React Native Drop-in integration, handling `action.type: direct`, and Customer Area method setup. It likewise says no extra SEPA configuration. For `/payments`, the guide lists `paymentMethod.sepa.ownerName` and an **unencrypted** `paymentMethod.sepa.ibanNumber`; billing address becomes required for the enumerated non-EEA SEPA IBAN countries and territories. The test request illustration uses Checkout API **v72**. Its curl line breaks around `-X POST` are not copy-ready. (raw lines 892–945)
- **Payment result and capture:** The Advanced illustration calls the response successful but shows `resultCode: Received`; that intermediate example is no proof of final authorization, capture, settlement or funded debit. When automatic capture is not used, the guide specifies delayed automatic or manual capture. It states SEPA Direct Debit authorizations do not expire and directs merchants to Support to enable multiple partial captures. (raw lines 948–967)
- **Recurring:** The guide documents tokenization for **Subscription** and **UnscheduledCardOnFile**, with standard tokenization fields and no extra SEPA-specific fields. It *strongly recommends* explicit shopper permission and transparent schedule/amount to reduce chargeback risk; this wording is advice, not a complete statement of the method-level mandate requirement. The `recurring.token.created` webhook carries `storedPaymentMethodId`; later shopper-absent token payments use `/payments`, stored ID, `ContAuth` and the applicable recurring model. Token examples do not prove token creation or a successful subsequent debit. (raw lines 49–59, 258–290, 571–597, 969–979, 1328–1358, 1639–1665)
- **Test/live boundary:** The page provides NL/AT/FR test IBAN/name pairs and a test Customer Area status path. It says a live Customer Area request for SEPA Direct Debit is needed before live acceptance. Historical examples and test status cannot prove present merchant enablement or settled funds. The related method overview retains mandate, pre-debit notice, chargeback and refund qualifications. (raw lines 878–890, 1946–1958; [[source-adyen-docs-payment-methods-sepa-direct-debit]])

## Detail locators

- Sessions prerequisites, mislabeled Advanced prerequisite URL, no extra ordinary request/configuration and v71 token example: pinned raw lines 25–83.
- Sessions token webhook and Subscription/UnscheduledCardOnFile `/payments` examples: pinned raw lines 258–875.
- Advanced prerequisites, direct action, no extra configuration, conditional billing address, request fields and v72 example: pinned raw lines 892–945.
- `Received` example, capture routes and multiple-partial-capture setup: pinned raw lines 948–967.
- Advanced token creation, webhook and reuse examples: pinned raw lines 969–1943. Several language snippets omit or assume request variables/fields; verify against the actual API/library version before reuse.
- Test data and live setup: pinned raw lines 878–890 and 1946–1958.

## Related

- [[adyen-online-payments]] — provider online-payment context
- [[adyen-tokenization]] — stored-method context
- [[adyen-react-native-sdk]] — broader React Native SDK context, separate from this API-versioned guide
- [[source-adyen-docs-payment-methods-sepa-direct-debit]] — method-level mandate and lifecycle risks
- [[adyen]] — provider

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/react-native-drop-in/2026-09-15|SEPA Direct Debit React Native Drop-in, 2026-09-15]]

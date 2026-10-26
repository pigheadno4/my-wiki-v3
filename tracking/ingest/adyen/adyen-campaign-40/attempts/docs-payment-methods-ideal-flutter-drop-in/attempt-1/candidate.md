---
title: "Adyen iDEAL | Wero Flutter Drop-in guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ideal/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/ideal/flutter-drop-in/2026-09-15.md"
tags: [adyen, ideal, wero, flutter, drop-in, redirect, sepa, recurring]
---

## Overview

This 2026-09-15 Adyen guide adds iDEAL | Wero to an existing Flutter Drop-in integration, with separate Sessions and Advanced server-side paths. It describes redirect handling for the initial method and a distinct SEPA Direct Debit token route for later shopper-absent payments. This snapshot does not prove current merchant enablement, a created token or an executed payment. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- **Sessions:** requires an existing Flutter Drop-in Sessions integration, Checkout API v68 or later, `action.type: redirect` handling and contacting Adyen Support to add iDEAL | Wero in Customer Area. The Sessions integration-type row points to an **Advanced** Flutter Drop-in URL, while its redirect and session links point to Sessions; follow the named flow and verify the main integration route. The page says there are no method-specific `/sessions` parameters or Drop-in configuration. (raw lines 23–48)
- **Advanced:** requires an existing Advanced Flutter Drop-in integration, redirect handling and adding iDEAL | Wero in Customer Area. It states no additional Drop-in configuration or normal `/payments` parameters. Unlike Sessions, this requirements table does not state a Checkout API minimum or direct merchants to contact Support for setup. These are section-specific instructions, not evidence that setup is complete. (raw lines 322–344)
- **Recurring:** the guide supports later payments through **SEPA Direct Debit**, not a repeat iDEAL redirect. It directs standard tokenization parameters to create a shopper token; `recurring.token.created` carries `storedPaymentMethodId`. It limits these tokenised payments to shopper-absent `UnscheduledCardOnFile` and `Subscription` scenarios. The illustrated subscription request uses `paymentMethod.type: sepadirectdebit`, a stored payment method ID, `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription`. This sample does not establish that token creation or a later payment succeeded. The Java example uses an EUR 15000 amount where other examples use EUR 1000 and omits `shopperReference` present in the other language examples; treat the snippets as illustrative, not one consistent request contract. (raw lines 50–275, 346–571)
- **Outcome boundary:** for the illustrated token payment, a successfully received request returns `resultCode: Received` and a `pspReference`; the guide directs payment-success tracking to webhooks. `Received` alone is not proof of authorization, capture or settlement. (raw lines 277–282, 573–578)
- **Testing:** the source warns its iDEAL | Wero TEST environment is unreliable and recommends live penny tests. The LIVE path requires an issuer bank account, a live payment, QR scan or issuer selection on the payment page, authorization and Customer Area status check. If TEST is available, `TESTNL2A` can simulate Authorised, Canceled, Pending/Received on expiration and Refused. These are conditional test instructions and result simulations, not evidence of present eligibility or live success. (raw lines 284–320, 580–616)

## Detail locators

- Sessions requirements, mismatched integration link and no-extra-field/configuration statements: pinned raw lines 25–48.
- Sessions SEPA token lifecycle and shopper-absent scope: pinned raw lines 50–77; language examples: lines 79–275.
- Advanced requirements and no-extra-field/configuration statements: pinned raw lines 322–344; repeated SEPA token route and examples: lines 346–571.
- Intermediate `Received` and webhook boundary: pinned raw lines 277–282 and 573–578.
- TEST reliability, LIVE penny test and conditional TEST simulations: pinned raw lines 284–320 and 580–616.

## Related

- [[adyen-online-payments]] — main redirect and outcome context
- [[adyen-tokenization]] — provider token lifecycle
- [[source-adyen-docs-payment-methods-ideal]] — iDEAL | Wero method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/ideal/flutter-drop-in/2026-09-15|iDEAL | Wero Flutter Drop-in guide, 2026-09-15]]

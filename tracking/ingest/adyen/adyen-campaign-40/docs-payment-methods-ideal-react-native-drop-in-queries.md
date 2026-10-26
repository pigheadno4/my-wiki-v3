# iDEAL | Wero React Native Drop-in retrieval checks

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-ideal-react-native-drop-in]]`. Token route: `[[index]]` → `[[adyen-index]]` → `[[adyen-tokenization]]` → the same source.

## Q1. What is its purpose and scope, and what cannot be inferred?

The canonical stem `source-adyen-docs-payment-methods-ideal-react-native-drop-in` is a 2026-09-15 method add-on to existing React Native Drop-in Sessions and Advanced server-side flows, with a separate SEPA token route (`raw/adyen/docs/payment-methods/ideal/react-native-drop-in/2026-09-15.md:15-36,50-69,322-350`). It does not establish current merchant or issuer enablement, a completed payment, capture or settlement; `Received` needs webhook outcome and TEST results are simulations (`:277-320,573-616`).

## Q2. What are the central capability, prerequisites, and warnings?

Sessions requires React Native Drop-in Sessions, Checkout API v68+, redirect handling and Customer Area addition, without method-specific `/sessions` or configuration additions (`raw/adyen/docs/payment-methods/ideal/react-native-drop-in/2026-09-15.md:29-48`). Its Sessions prerequisite hyperlink instead points to Advanced, while the other links target Sessions (`:33-42`). Advanced needs React Native Drop-in Advanced, redirect handling and Customer Area addition, without method-specific normal `/payments` or configuration additions (`:326-344`). Later recurring payments use separate SEPA Direct Debit token creation; `recurring.token.created` carries `storedPaymentMethodId`, and use is scoped to shopper-absent Subscription/UnscheduledCardOnFile (`:52-77,348-373`). Java sample amount and shopperReference differ from adjacent examples (`:81-130,141-157`). `Received` with PSP reference is not final success; webhooks track outcome (`:277-282,573-578`). TEST is unreliable; live penny tests are recommended, while available TEST offers `TESTNL2A` simulations including expiration as Pending or Received (`:284-320,580-616`).

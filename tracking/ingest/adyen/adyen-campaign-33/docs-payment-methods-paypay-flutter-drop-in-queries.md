# Retrieval queries — docs-payment-methods-paypay-flutter-drop-in

## Q1 — purpose and prerequisites

**Query:** What must an existing Flutter Drop-in integration add for PayPay in Sessions or Advanced flow?

**Answer:** This PayPay-specific guide assumes an existing Flutter Drop-in integration. Sessions lists Checkout API v68+, Customer Area addition and `action.type: redirect` handling; Advanced lists Customer Area addition and redirect handling but no separate v68+ statement. Both say no PayPay-specific additional configuration or request parameters for their respective `/sessions` and `/payments` requests. These do not replace the main flow requirements. The Sessions integration-type row mistakenly links to an Advanced-flow URL, while its redirect/session links lead to Sessions. Raw lines 23–48 and 63–85.

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paypay-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/paypay/flutter-drop-in/2026-09-15]].

## Q2 — TEST/LIVE and outcome boundary

**Query:** Can the TEST simulator flow prove LIVE PayPay-app readiness or final authorization/sale?

**Answer:** No. TEST names two DGFT closed-loop acquirer accounts, AUTHFlow and SALEFlow, and redirects to a DGFT simulator without needing the PayPay app. The guide says to inspect TEST transactions in the TEST Customer Area Payment list. LIVE instead requires access to an activated PayPay smartphone app through a Japan local IP address. It gives no final webhook or authorization/settlement result rule; an account name or redirect is not proof of success. Raw lines 50–61 and 87–98.

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paypay-flutter-drop-in]] → [[raw/adyen/docs/payment-methods/paypay/flutter-drop-in/2026-09-15]].

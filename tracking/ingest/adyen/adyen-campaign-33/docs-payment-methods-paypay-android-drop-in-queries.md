# Retrieval checks — PayPay Android Drop-in

Q1. What does this Android Drop-in add-on require and add in Sessions versus Advanced flow?

A1. It assumes an existing Android Drop-in integration and PayPay added in Customer Area (raw lines 19–34, 63–71). Sessions uniquely specifies Checkout API v68+ and no PayPay-specific `/sessions` or configuration fields (raw lines 33, 36–46). Advanced explicitly requires `action.type: redirect` handling and no PayPay-specific configuration or `/payments` fields (raw lines 69–83). Sessions does not separately state a redirect-handling prerequisite, though its TEST path describes a redirect (raw lines 50–57). Base-flow requirements remain external to this method add-on. Retrieve via [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paypay-android-drop-in]] → [[raw/adyen/docs/payment-methods/paypay/android-drop-in/2026-09-15]].

Q2. How do the documented TEST and LIVE conditions differ, and what outcome can be concluded?

A2. For TEST, both sections list DGFT closed-loop AUTHFlow/SALEFlow acquirer accounts, a DGFT simulator redirect without the PayPay app, and Customer Area Payment list status inspection (raw lines 50–59, 85–94). LIVE instead calls for an activated PayPay smartphone app accessed through a Japan local IP address (raw lines 61, 96). The page gives no actual merchant eligibility or final authorization/capture/settlement evidence, and the SDK/base flow owns further payment-state handling. Retrieve via [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paypay-android-drop-in]] → [[raw/adyen/docs/payment-methods/paypay/android-drop-in/2026-09-15]].

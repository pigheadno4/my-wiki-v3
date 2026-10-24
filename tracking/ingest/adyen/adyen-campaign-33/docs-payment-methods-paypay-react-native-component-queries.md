# Retrieval checks — PayPay React Native Component

Q1. Which React Native Component server flow does this PayPay page support, and what are its requirements?

A1. The page explicitly says React Native Components do not support Sessions flow (raw lines 25–29). Its Advanced branch requires an existing Components integration, `action.type: redirect` handling and PayPay in Adyen Customer Area (raw lines 31–41), while stating no additional PayPay-specific configuration or `/payments` parameters (raw lines 43–53). The Components-labelled prerequisite URL actually carries `integration=Drop-in`, whereas the other links use Components (raw lines 39–40, 53). Retrieve via [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paypay-react-native-component]] → [[raw/adyen/docs/payment-methods/paypay/react-native-component/2026-09-15]].

Q2. What TEST and LIVE conditions apply, and what does this page establish about completion?

A2. It lists DGFT closed-loop AUTHFlow/SALEFlow acquirer accounts in TEST, a DGFT simulator redirect without the PayPay app, and TEST Customer Area status inspection (raw lines 55–64). LIVE calls for an activated PayPay smartphone app through a Japan local IP address (raw line 66). This method add-on omits detailed return/webhook/final-result processing and supplies no actual authorization, capture or settlement proof. Its page title says React Component despite a React Native URL/body (raw lines 6, 8, 29, 39), so preserve that source ambiguity. Retrieve via [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paypay-react-native-component]] → [[raw/adyen/docs/payment-methods/paypay/react-native-component/2026-09-15]].

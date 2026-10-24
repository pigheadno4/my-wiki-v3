# Retrieval checks — docs-payment-methods-google-pay-react-native-drop-in

Q1. What does this React Native Drop-in Google Pay add-on require and configure?

A1. It assumes an existing React Native Drop-in integration, Google's setup steps and Google Pay added in Adyen Customer Area (raw lines 17–29). It says there are no extra Google-Pay-specific /payments fields or required Drop-in settings, while listing optional AdyenCheckout wallet/network/auth-method, price, contact and button options (raw lines 31–59). It does not pin a wrapper/native SDK or Checkout API version. Route: [[index]] → [[adyen-index]] → [[adyen-react-native-sdk]] → [[source-adyen-docs-payment-methods-google-pay-react-native-drop-in]] → [[raw/adyen/docs/payment-methods/google-pay/react-native-drop-in/2026-09-15]].

Q2. Which provider, environment, token and outcome limits matter?

A2. The optional table describes merchantAccount as a Google Merchant ID (raw line 45) and mistakenly lists ENVIRONMENT_TEST for both test and live under googlePayEnvironment (raw line 57), so neither should be generalized as production configuration without version-matched reference. Recurring merely links token creation and later token payments (raw lines 61–64). TEST suite versus mapped cards and 3DS2 brand limits are at raw lines 66–90; LIVE calls for the API Clientside Encryption Payments role, Merchant ID, Google Android deployment and valid logged-in wallet (raw lines 92–103). Sheet/redirect behavior at raw line 21 is not final authorization, capture or settlement proof. Route: [[index]] → [[adyen-index]] → [[adyen-react-native-sdk]] → [[source-adyen-docs-payment-methods-google-pay-react-native-drop-in]] → [[raw/adyen/docs/payment-methods/google-pay/react-native-drop-in/2026-09-15]].
